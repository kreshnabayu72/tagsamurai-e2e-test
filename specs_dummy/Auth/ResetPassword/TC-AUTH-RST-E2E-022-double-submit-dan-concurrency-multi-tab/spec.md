---
id: TC-AUTH-RST-E2E-022-double-submit-dan-concurrency-multi-tab
title: "Pencegahan double-submit dan penanganan race condition antar tab browser"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-89
  - TC-AUTH-RST-93
  - TC-AUTH-RST-129
  - TC-AUTH-RST-130
coverage:
  web: automated
---

# Pencegahan double-submit dan penanganan race condition antar tab browser

## Prerequisites

- User belum login (guest); browser web siap membuka beberapa tab secara paralel.
- Environment uji terisolasi dengan akses mail-catcher.
- Akun uji `budisantoso@qwertysystem.net` berstatus aktif dan terdaftar.

## Test Steps

### Pencegahan Double-Submit pada tombol [Reset Password] di halaman Request

1. Buka halaman Reset Password dan masukkan email "budisantoso@qwertysystem.net"
2. Selesaikan verifikasi reCAPTCHA
3. Lakukan klik ganda sangat cepat (rapid double-click) pada tombol [Reset Password]
4. Verifikasi tombol langsung disabled pada klik pertama sehingga klik kedua diabaikan
5. Periksa database token dan mail-catcher
6. Verifikasi tepat hanya 1 token reset yang diterbitkan dan tepat hanya 1 email reset yang dikirimkan

### Pencegahan Double-Submit pada tombol [Reset Password] di Setup New Password

7. Buka tautan reset valid pada browser
8. Masukkan password baru yang valid pada kedua field
9. Lakukan klik ganda sangat cepat pada tombol [Reset Password]
10. Verifikasi sistem hanya memproses tepat 1 transaksi pembaruan password
11. Verifikasi browser mendarat di Halaman Password Reset Successful tanpa error race condition

### Concurrency 2 tab Setup New Password untuk token yang sama

12. Siapkan token reset aktif baru untuk Budi Santoso
13. Buka tautan reset yang sama pada Tab Browser 1 dan Tab Browser 2 secara bersamaan
14. Verifikasi kedua tab sama-sama berhasil merender form Setup New Password
15. Pada Tab Browser 1, isi password baru "PasswordTab1!" lalu klik tombol [Reset Password]
16. Verifikasi Tab 1 sukses mendarat di Password Reset Successful dan token berstatus `consumed`
17. Beralih ke Tab Browser 2 (yang masih menampilkan form Setup New Password terbuka)
18. Pada Tab Browser 2, isi password baru "PasswordTab2!" lalu klik tombol [Reset Password]
19. Verifikasi server mendeteksi token sudah consumed dan menolak submit kedua
20. Verifikasi Tab 2 menampilkan Halaman 404 varian Already Used ("Reset Link Already Used")
21. Verifikasi password akun tetap "PasswordTab1!" (tidak tertimpa oleh Tab 2)

### Resend di tab lain saat form Setup New Password sedang terbuka

22. Siapkan alur request baru hingga halaman Email Sent! terbuka di Tab Browser A
23. Buka tautan email pertama di Tab Browser B sehingga form Setup New Password terbuka
24. Beralih kembali ke Tab Browser A lalu klik tombol [Resend email] setelah cooldown
25. Verifikasi token pertama di-invalidate dan token kedua terbit
26. Beralih kembali ke Tab Browser B lalu lakukan submit password pada form yang masih terbuka
27. Verifikasi server menolak submit karena token telah di-invalidate oleh aksi Resend
28. Verifikasi Tab B menampilkan Halaman 404 varian Expired ("Reset Link Expired")

## Notes

- Sesuai PRD §9.4.2 baris 7 dan 31 serta §9.4.3 Must NOT 7 & 8, sistem memiliki guard pencegahan klik ganda di front-end dan perlindungan konkurensi di backend melalui token locking untuk mencegah duplikasi reset maupun pemrosesan ganda.

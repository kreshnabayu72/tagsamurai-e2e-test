---
id: TC-AUTH-RST-E2E-021-resilience-kegagalan-server-dan-timeout
title: "Ketahanan terhadap gangguan server 5xx dan timeout pada alur Request, Resend, Validate Link, dan Submit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-50
  - TC-AUTH-RST-62
  - TC-AUTH-RST-87
  - TC-AUTH-RST-88
  - TC-AUTH-RST-90
  - TC-AUTH-RST-91
  - TC-AUTH-RST-92
  - TC-AUTH-RST-144
coverage:
  web: automated
---

# Ketahanan terhadap gangguan server 5xx dan timeout pada alur Request, Resend, Validate Link, dan Submit

## Prerequisites

- User belum login (guest); browser web berada di alur Reset Password.
- Environment uji terisolasi dengan kemampuan intercept error HTTP 500 dan network timeout (`Mode: mock`).
- Token reset valid tersedia untuk pengujian validasi link dan submit.

## Test Steps

### Kegagalan server 500 dan Timeout pada Request Reset

1. Buka halaman Reset Password dan masukkan email valid
2. Selesaikan reCAPTCHA
3. Simulasikan intercept respons server HTTP 500 Internal Server Error untuk endpoint `/request`
4. Klik tombol [Reset Password]
5. Verifikasi toast error "Error, failed to send reset link." tampil di layar
6. Verifikasi nilai field Email dipertahankan dan tombol [Reset Password] kembali enabled
7. Simulasikan intercept network timeout untuk endpoint `/request`
8. Klik tombol [Reset Password]
9. Verifikasi toast error koneksi "Connection problem. Please try again." tampil dan form tetap dapat dikirim ulang

### Kegagalan server 500 pada aksi Resend email

10. Buka halaman Email Sent! dan tunggu cooldown berakhir
11. Simulasikan intercept respons HTTP 500 untuk endpoint `/resend`
12. Klik tombol [Resend email]
13. Verifikasi toast error "Error, failed to send email to budisantoso@qwertysystem.net." tampil di kanan bawah
14. Verifikasi halaman Email Sent! tetap dipertahankan dan token yang ada tidak rusak
15. Verifikasi tombol [Resend email] kembali enabled sehingga user dapat mencoba lagi

### Kegagalan server 500 pada Validasi Tautan (GET /validate)

16. Buka tautan reset valid di browser
17. Simulasikan intercept respons HTTP 500 pada pemanggilan validasi token
18. Verifikasi layar TIDAK menampilkan Halaman 404 (karena bukan link expired atau tidak sah)
19. Verifikasi layar menampilkan ErrorState sistem dengan ilustrasi gangguan server dan tombol [Try Again]
20. Klik tombol [Try Again] setelah intercept dinonaktifkan
21. Verifikasi halaman Setup New Password berhasil dimuat normal

### Kegagalan server 500 dan Timeout pada Submit New Password

22. Pada halaman Setup New Password, masukkan password baru yang valid pada kedua field
23. Simulasikan intercept respons HTTP 500 untuk endpoint `/confirm`
24. Klik tombol [Reset Password]
25. Verifikasi toast error "Error, failed to reset password." tampil di layar
26. Verifikasi isian field password dipertahankan dan token di database TIDAK dikonsumsi (tetap `active`)
27. Simulasikan intercept network timeout untuk endpoint `/confirm`
28. Klik tombol [Reset Password]
29. Verifikasi toast error koneksi "Connection problem. Please try again." tampil, tombol enabled kembali, dan token tetap aman tidak hangus

### Integritas atomik saat kegagalan di tengah transaksi Submit

30. Lakukan simulasi kegagalan database tepat setelah penyimpanan hash password baru namun sebelum pembersihan lock/sesi selesai (fault injection)
31. Verifikasi seluruh transaksi dibatalkan (rollback)
32. Verifikasi tidak ada perubahan parsial yang tersisa di database (password lama tetap aktif dan token tidak hangus)

### Kegagalan enqueue email setelah token tersimpan (best-effort, TC-AUTH-RST-144)

33. Siapkan failure injection pada layanan enqueue/pengiriman email oleh tim BE sehingga pengiriman email reset gagal setelah token tersimpan di database
34. Lakukan Request Reset untuk `budisantoso@qwertysystem.net` (isi email, selesaikan reCAPTCHA, klik [Reset Password])
35. Verifikasi halaman Email Sent! tetap tampil tanpa toast error (identik dengan request yang emailnya terkirim)
36. Verifikasi token reset tetap tersimpan berstatus `active` di database dan entri log Success `Password reset requested` tetap tercatat
37. Setelah cooldown selesai, klik [Resend email] lalu verifikasi toast sukses "Success, email has been sent to budisantoso@qwertysystem.net." tetap tampil tanpa toast error

## Notes

- Sesuai PRD §4.1 S-AUTHRST-08, §9.6 Action Resilience, dan FI-AUTHRST-10, kegagalan teknis (5xx atau timeout) tidak boleh merugikan pengguna: form mempertahankan input data, tombol kembali enabled untuk retry, dan token reset tidak dikonsumsi. Toast failed Request/Submit 5xx mengikuti `T-AUTHRST-02`/`T-AUTHRST-03` (§7); timeout/network mengikuti C-2 §2 (`"Connection problem. Please try again."`).
- Sesuai PRD §9.6 dan §9.4.2 baris 13 & 20 serta §9.4.3 Must NOT 9, kegagalan enqueue/pengiriman email setelah commit bersifat best-effort: token tidak di-rollback, UI tetap menampilkan halaman Email Sent! (Request) atau toast sukses (Resend), tanpa toast error (TC-AUTH-RST-144, skenario 33-37 memerlukan failure injection dari tim BE).
- Pada validasi tautan token, kegagalan 5xx menampilkan ErrorState dengan tombol [Try Again], bukan Halaman 404, untuk membedakan antara gangguan server sementara dengan tautan yang tidak sah.

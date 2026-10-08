---
id: TC-AUTH-RST-E2E-002-validasi-field-email-request
title: "Validasi field Email pada halaman Request Reset: wajib diisi, format, dan batas karakter"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-13
  - TC-AUTH-RST-15
  - TC-AUTH-RST-16
  - TC-AUTH-RST-17
  - TC-AUTH-RST-18
coverage:
  web: automated
---

# Validasi field Email pada halaman Request Reset: wajib diisi, format, dan batas karakter

## Prerequisites

- User belum login (guest); browser web berada di halaman `/reset-password`.
- Environment uji terisolasi khusus pengujian otomatis.
- Widget Google reCAPTCHA v2 diselesaikan otomatis melalui test bypass token.
- User `budisantoso@qwertysystem.net` berstatus aktif dan terdaftar di database.

## Test Steps

### Validasi field Email wajib diisi

1. Buka halaman Reset Password di browser web
2. Kosongkan field Email
3. Selesaikan verifikasi reCAPTCHA
4. Klik tombol [Reset Password]
5. Verifikasi caption inline "Email must not be empty" tampil tepat di bawah field Email
6. Verifikasi browser tetap berada di halaman Reset Password dan tidak ada email atau token yang diterbitkan

### Validasi format Email dan batas domain

7. Masukkan `budisantoso` (tanpa karakter `@`) pada field Email
8. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
9. Verifikasi caption inline "Email format is incorrect" tampil di bawah field Email
10. Ganti isi field Email dengan `budisantoso@` (tanpa domain)
11. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
12. Verifikasi caption inline "Email format is incorrect" tampil di bawah field Email
13. Ganti isi field Email dengan `budisantoso@qwertysystem` (tanpa titik ekstensi domain)
14. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
15. Verifikasi caption inline "Email format is incorrect" tampil di bawah field Email
16. Ganti isi field Email dengan `budisantoso@qwertysystem.c` (hanya satu karakter TLD setelah titik)
17. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
18. Verifikasi caption inline "Email format is incorrect" tampil di bawah field Email
19. Ganti isi field Email dengan `budisantoso+alias@qwertysystem.net` (mengandung tanda `+` / sub-addressing)
20. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
21. Verifikasi request diproses sukses menuju halaman Email Sent! (format plus-address diterima sebagai email valid, sesuai `auth-foundation.md` §4.0a)

### Validasi batas panjang karakter Email (120 vs 121 karakter)

22. Masukkan email dengan total 120 karakter (103 karakter huruf `a` diikuti `@qwertysystem.net`)
23. Verifikasi caption "Max. 120 characters" tidak tampil saat mengetik 120 karakter
24. Tambahkan 1 karakter huruf sehingga total panjang email menjadi 121 karakter
25. Verifikasi caption inline "Max. 120 characters" langsung muncul secara real-time saat karakter ke-121 diketik
26. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
27. Verifikasi tombol [Reset Password] diblokir dan caption "Max. 120 characters" tetap bertahan

### Sanitasi spasi awal dan akhir (Trim)

28. Bersihkan field Email lalu masukkan `  budisantoso@qwertysystem.net  ` (dengan spasi di awal dan di akhir)
29. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
30. Verifikasi request diproses berhasil menuju halaman Email Sent!
31. Verifikasi teks pada halaman Email Sent! menampilkan "budisantoso@qwertysystem.net" tanpa karakter spasi di awal atau akhir

## Notes

- Sesuai PRD §6 V-AUTHRST-01, V-AUTHRST-02, V-AUTHRST-03, §9.9 FLD-AUTHRST-01, dan `auth-foundation.md` §4.0a, batas maksimal field email adalah 120 karakter; format ditolak jika TLD kurang dari 2 karakter. Format plus-address (tanda `+`) kini **diizinkan** dan dianggap valid (konsisten dengan Login Password/OTP); pencarian akun bersifat case-insensitive setelah normalisasi.
- Trim spasi awal dan akhir dilakukan sebelum pencarian akun dilakukan di database (`TC-AUTH-RST-13`).
- Uji proteksi payload injeksi SQL/XSS dan penegakan server terhadap email tidak valid (`TC-AUTH-RST-119`, `TC-AUTH-RST-128`) dipisahkan ke spec `TC-AUTH-RST-E2E-028` (dekomposisi GAP-RST-E2E-001).

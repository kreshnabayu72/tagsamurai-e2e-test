---
id: TC-AUTH-RST-E2E-018-submit-password-sukses-dan-404-already-used
title: "Submit New Password sukses, navigasi login, konsumsi token sekali pakai, dan Halaman 404 Already Used"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-81
  - TC-AUTH-RST-82
  - TC-AUTH-RST-83
  - TC-AUTH-RST-84
  - TC-AUTH-RST-85
  - TC-AUTH-RST-86
  - TC-AUTH-RST-127
coverage:
  web: automated
---

# Submit New Password sukses, navigasi login, konsumsi token sekali pakai, dan Halaman 404 Already Used

## Prerequisites

- User belum login (guest); membuka tautan reset valid milik `budisantoso@qwertysystem.net`.
- Halaman Setup New Password terbuka normal di browser web.
- Password baru yang akan digunakan adalah `QaBaru!2027` (memenuhi seluruh checklist policy).

## Test Steps

### State loading saat submit diproses

1. Masukkan "QaBaru!2027" pada field Password
2. Masukkan "QaBaru!2027" pada field Confirm Password
3. Klik tombol [Reset Password]
4. Verifikasi tombol [Reset Password] seketika disabled dan menampilkan spinner loading
5. Verifikasi kedua field password menjadi non-editable selama permintaan dikirim ke server

### Penyimpanan password dan konsumsi token secara atomik

6. Tunggu respons sukses dari server
7. Verifikasi password akun di database telah diperbarui menjadi hash dari `QaBaru!2027`
8. Verifikasi status token reset di database berubah menjadi `consumed` (sudah digunakan)
9. Verifikasi token yang sama tidak dapat dikonsumsi ulang oleh siapa pun

### Screening Halaman Password Reset Successful

10. Verifikasi browser berpindah ke Halaman 4 Password Reset Successful (`/password-reset-successful`)
11. Verifikasi logo TAG Samurai tampil di bagian header
12. Verifikasi title halaman adalah "Password Reset Successful"
13. Verifikasi subtitle halaman adalah "Your password has been reset successfully. You can now log in with your new password."
14. Verifikasi tombol [Go to Login Page] tampil dengan styling solid primary

### Navigasi tombol [Go to Login Page]

15. Klik tombol [Go to Login Page]
16. Verifikasi browser berpindah ke halaman Login with Password (`/login`)
17. Verifikasi form Login siap menerima input kredensial

### Pembuktian tautan yang sudah dikonsumsi membuka Halaman 404 varian Already Used

18. Buka kembali tautan reset yang sama pada tab browser baru
19. Verifikasi browser menampilkan Halaman 404 varian Already Used
20. Verifikasi title halaman adalah "Reset Link Already Used"
21. Verifikasi message halaman berbunyi: "This password reset link has already been used. If you still need to reset your password, please request a new link."
22. Verifikasi tombol [Go to Login] tampil pada halaman tersebut
23. Klik tombol [Go to Login] pada Halaman 404 Already Used
24. Verifikasi browser diarahkan ke halaman Login with Password (`/login`)

## Notes

- Sesuai PRD §4.1 S-AUTHRST-04/05, §4.2 Halaman 4 dan 5 (varian 2), §9.2 F-AUTHRST-04, dan `RSTPWD-LOGIC-01a/e`, token reset bersifat sekali pakai (single-use); begitu submit sukses, token berstatus consumed dan tautan hanya dapat merender Halaman 404 varian Already Used.

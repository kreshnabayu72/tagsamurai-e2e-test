---
id: TC-AUTH-RST-E2E-031-lock-recovery-permanent-counters
title: "Pemulihan Lock Permanen serta Counter Kegagalan dan Eskalasi Dibersihkan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-109
  - TC-AUTH-RST-110
coverage:
  web: automated
---

# Pemulihan Lock Permanen serta Counter Kegagalan dan Eskalasi Dibersihkan

## Prerequisites

- Mode: FE+BE (dengan fixture lock BE).
- Seeding: user subjek `Yuni Astuti` (`yuniastuti+{runId}-031@qwertysystem.net`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password aktif `Spectra.env.RST_PASSWORD`, tanpa gate Agreement dan MFA (fixture BE), dan lock permanen (eskalasi 7 hari, diatur fixture BE). User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`, `RST_PASSWORD_WRONG`.
- Kemampuan teknis: fixture BE untuk lock progression; mail-catcher dengan pembacaan jumlah email per alamat; reCAPTCHA mode uji; jendela privat tanpa sesi login.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat suite.md); mekanisme reset disediakan tim FE/BE.
- Hook `after` menutup semua jendela privat, menghapus sesi browser, dan mengembalikan sesi ke akun default suite.
- TC-AUTH-RST-109, TC-AUTH-RST-110: User belum login (guest); browser web.
- TC-AUTH-RST-109 data: Password baru `Spectra.env.RST_PASSWORD_NEW` pada Password dan Confirm Password.
- TC-AUTH-RST-110 data: Password salah `Spectra.env.RST_PASSWORD_WRONG` (nilai yang memenuhi format dan berbeda dari password aktif; TC menulis `SalahSalah!1`).

## Test Steps

### TC-AUTH-RST-109: Reset sukses membersihkan lock permanen

1. Buka jendela privat baru lalu buka halaman Reset Password (Request)
2. Catat jumlah email di mail-catcher untuk `yuniastuti+{runId}-031@qwertysystem.net` sebagai baseline
3. Ketik `yuniastuti+{runId}-031@qwertysystem.net`, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password]
4. Verifikasi Request pada akun terkunci diproses: browser menuju halaman Email Sent!
5. Verifikasi jumlah email di mail-catcher untuk `yuniastuti+{runId}-031@qwertysystem.net` bertambah 1 dibanding baseline (email reset masuk)
6. Buka tautan reset dari email lalu ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password, kemudian klik Button [Reset Password]
7. Verifikasi browser menuju halaman Password Reset Successful
8. Klik Button [Go to Login Page]
9. Login dengan Email `yuniastuti+{runId}-031@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD_NEW` (selesaikan reCAPTCHA)
10. Verifikasi login berhasil
11. Verifikasi tidak ada caption lock
12. Verifikasi tidak ada Alert lock
13. Verifikasi browser menuju Portal — Product Hub
14. Keluar dari akun (logout), lalu tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-RST-110: Counter kegagalan login dan eskalasi harian dibersihkan setelah reset

15. Buka jendela privat baru lalu buka halaman Login with Password
16. Login dengan Email `yuniastuti+{runId}-031@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD_WRONG` (selesaikan reCAPTCHA)
17. Verifikasi Alert Danger tampil: "Incorrect email or password" (kegagalan pertama)
18. Verifikasi Alert lock permanen "For security reasons, your account has been locked. Please reset your password to regain access." tidak tampil

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. TC-AUTH-RST-110 bergantung pada TC-AUTH-RST-109; alurnya disalin utuh dan dilanjutkan di jendela baru (S-04).
- Jendela privat ditutup dan sesi browser dihapus di akhir blok TC-AUTH-RST-109 supaya blok TC-AUTH-RST-110 tidak mewarisi sesi Portal (S-09).
- Temuan untuk QA: Post Condition TC-AUTH-RST-109 (lock progression none dan counter kegagalan login 0) dan TC-AUTH-RST-110 (counter hari itu 1 dan eskalasi 7 hari 0) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).

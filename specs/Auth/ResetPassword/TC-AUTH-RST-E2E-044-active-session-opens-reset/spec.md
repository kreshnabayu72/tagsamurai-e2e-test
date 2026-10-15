---
id: TC-AUTH-RST-E2E-044-active-session-opens-reset
title: "User dengan Sesi Aktif Membuka Halaman Reset Password dan Tautan Reset"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-10
  - TC-AUTH-RST-11
coverage:
  web: automated
---

# User dengan Sesi Aktif Membuka Halaman Reset Password dan Tautan Reset

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek `Budi Santoso` (`budisantoso+{runId}-044@qwertysystem.net`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password aktif `Spectra.env.RST_PASSWORD` dan tanpa gate Agreement dan MFA (fixture BE). Di hook `before`, user login di web (login akun aktor pertama spec ini) sehingga sesi penuh aktif; satu token reset aktif diterbitkan lewat API Request, tautan dari mail-catcher. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: mail-catcher; mengubah alamat di address bar pada tab yang sama.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- Sesi: hook `after` mengakhiri sesi `Budi Santoso` dan memulihkan sesi ke akun default suite.
- TC-AUTH-RST-10, TC-AUTH-RST-11: User `Budi Santoso` sudah login di web (sesi penuh aktif).

## Test Steps

### TC-AUTH-RST-10: User yang sudah login membuka halaman Reset Password

1. Pada tab yang sama dengan sesi aktif, ubah alamat ke halaman Reset Password lalu tekan Enter
2. Verifikasi browser menuju Portal — Product Hub
3. Verifikasi form Reset Password tidak tampil
4. Ubah alamat ke halaman Email Sent! lalu tekan Enter
5. Verifikasi browser menuju Portal — Product Hub
6. Verifikasi halaman Email Sent! tidak tampil

### TC-AUTH-RST-11: User yang sudah login membuka tautan reset tetap melihat Setup New Password

7. Buka tautan reset milik `budisantoso+{runId}-044@qwertysystem.net` dari mail-catcher pada tab yang sama dengan sesi aktif
8. Verifikasi halaman Setup New Password tampil dengan Subtitle "Set a new password to log in for budisantoso+{runId}-044@qwertysystem.net."
9. Verifikasi browser tidak diarahkan ke Portal

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Login pertama di hook `before` (S-07). Post Condition TC-AUTH-RST-11 (token tetap active) dibuktikan karena Setup New Password tampil tanpa submit.

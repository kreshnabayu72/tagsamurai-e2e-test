---
id: TC-AUTH-LP-E2E-055-lock-platform-independence-web
title: "Lock Login di Aplikasi Mobile Tidak Mengunci Login di Web"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-65
coverage:
  web: automated
---

# Lock Login di Aplikasi Mobile Tidak Mengunci Login di Web

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`): Create User lalu aktivasi dengan password `Spectra.env.LP_PASSWORD`. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: browser web; fixture BE untuk membuat user terkunci 15 menit di mobile tanpa kegagalan di web; fixture BE untuk device terpercaya di web dan penandaan tanpa gate Agreement dan MFA di web; reCAPTCHA mode uji di environment.
- TC-AUTH-LP-65: User `Maya Anggraini` (`mayaanggraini+{runId}-055@qwertysystem.net`) berstatus Activated dan Active; terkunci 15 menit di mobile (fixture BE); belum ada kegagalan di web; device terpercaya di web; tidak ada gate Agreement dan MFA di web
- TC-AUTH-LP-65: User belum login (guest); browser web
- TC-AUTH-LP-65 data: Email `mayaanggraini+{runId}-055@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-65: Lock di aplikasi mobile tidak mengunci login di web

1. Buka halaman Login with Password
2. Ketik email `mayaanggraini+{runId}-055@qwertysystem.net` di field Email
3. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
4. Selesaikan reCAPTCHA
5. Klik [Log in]
6. Verifikasi login berhasil: browser menuju Portal — Product Hub
7. Verifikasi caption lock tidak tampil
8. Logout dari web

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Langkah 8 (logout) adalah langkah penghubung supaya sesi tidak terbawa; tanpa awalan `Verifikasi` (S-03).
- TC-AUTH-LP-64 (lock di web tidak mengunci login di mobile) ada di spec `TC-AUTH-LP-E2E-017-lock-platform-independence`.
- Spec ini hanya berjalan di browser web dan memakai user sendiri (`-055`) dengan lock mobile yang di-seed fixture BE.
- Temuan untuk QA: cara membuat user terkunci "di mobile saja" tidak dijelaskan di TC-AUTH-LP-65 (lewat 3 kegagalan di app atau lewat fixture BE); spec menganggapnya fixture BE.

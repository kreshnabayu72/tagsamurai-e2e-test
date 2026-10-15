---
id: TC-AUTH-LP-E2E-017-lock-platform-independence
title: "Lock Login di Web Tidak Mengunci Login di Aplikasi Mobile"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-64
coverage:
  mobile: automated
---

# Lock Login di Web Tidak Mengunci Login di Aplikasi Mobile

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`): Create User lalu aktivasi dengan password `Spectra.env.LP_PASSWORD`. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: aplikasi native Android TAG Samurai Mobile (perangkat atau emulator); fixture BE untuk membuat user terkunci 15 menit di web tanpa kegagalan di mobile; fixture BE untuk device terpercaya di mobile dan penandaan tanpa gate Agreement dan MFA di mobile.
- TC-AUTH-LP-64: User `Maya Anggraini` (`mayaanggraini+{runId}-017@qwertysystem.net`) berstatus Activated dan Active; terkunci 15 menit di web (fixture BE); belum ada kegagalan di mobile; device terpercaya di mobile; tidak ada gate Agreement dan MFA di mobile
- TC-AUTH-LP-64: User belum login; aplikasi native Android TAG Samurai Mobile
- TC-AUTH-LP-64 data: Email `mayaanggraini+{runId}-017@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-64: Lock di web tidak mengunci login di aplikasi mobile

1. Buka layar Login with Password di aplikasi mobile
2. Ketik email `mayaanggraini+{runId}-017@qwertysystem.net` di field Email
3. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
4. Ketuk [Log in]
5. Verifikasi login berhasil: aplikasi menuju Portal — Product Hub
6. Verifikasi caption lock tidak tampil
7. Logout dari aplikasi mobile

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Langkah 7 (logout) adalah langkah penghubung supaya sesi tidak terbawa; tanpa awalan `Verifikasi` (S-03).
- TC-AUTH-LP-65 (lock di mobile tidak mengunci login di web) ada di spec `TC-AUTH-LP-E2E-055-lock-platform-independence-web`.
- Spec ini hanya berjalan di aplikasi mobile dan memakai user sendiri (`-017`) dengan lock web yang di-seed fixture BE.
- Temuan untuk QA: TC-AUTH-LP-64 dan TC-AUTH-LP-65 memakai fixture yang sama (`Maya Anggraini`) dengan state lock berlawanan tanpa menyebut cara mengatur ulang state di antara kedua TC; tiap spec men-seed user sendiri. Cara membuat user terkunci "di web saja" tidak dijelaskan (lewat 3 kegagalan di web atau lewat fixture BE); spec menganggapnya fixture BE.

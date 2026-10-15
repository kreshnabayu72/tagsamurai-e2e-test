---
id: TC-AUTH-RST-E2E-046-android-app-link
title: "App Link Android: Tautan Reset Dibuka dengan dan Tanpa Aplikasi Terpasang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-08
  - TC-AUTH-RST-09
coverage:
  mobile: automated
---

# App Link Android: Tautan Reset Dibuka dengan dan Tanpa Aplikasi Terpasang

## Prerequisites

- Mode: FE+BE (kelas d: dua kondisi perangkat berbeda).
- Seeding: dua user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password aktif `Spectra.env.RST_PASSWORD`; satu token reset aktif per user diterbitkan di hook `before` lewat API Request, email reset terbuka di perangkat Android. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: dua perangkat atau profil Android: satu dengan aplikasi TAG Samurai Mobile terpasang dan satu tanpa aplikasi; klien email di perangkat untuk mengetuk tautan reset (atau pemicu App Link setara).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-08: User `Budi Santoso` (`budisantoso+{runId}-046a@qwertysystem.net`) dengan token aktif; aplikasi TAG Samurai Mobile terpasang.
- TC-AUTH-RST-09: User `Citra Dewi` (`citradewi+{runId}-046b@qwertysystem.net`) dengan token aktif; aplikasi TAG Samurai Mobile belum terpasang.

## Test Steps

### TC-AUTH-RST-08: Tautan reset dibuka di aplikasi terpasang langsung ke Setup New Password

1. Di perangkat Android dengan aplikasi terpasang, ketuk tautan reset milik `budisantoso+{runId}-046a@qwertysystem.net` pada email
2. Verifikasi tautan dibuka di aplikasi native (bukan browser)
3. Verifikasi layar Setup New Password tampil langsung dengan Subtitle "Set a new password to log in for budisantoso+{runId}-046a@qwertysystem.net."

### TC-AUTH-RST-09: Tautan reset dibuka di perangkat tanpa aplikasi mengarah ke halaman instal

4. Di perangkat Android tanpa aplikasi terpasang, ketuk tautan reset milik `citradewi+{runId}-046b@qwertysystem.net` pada email
5. Verifikasi tautan mengarah ke halaman instal aplikasi di Play Store

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md` (Manual Only; kebutuhan dua kondisi perangkat ditulis di Prerequisites sebagai tugas tim FE).

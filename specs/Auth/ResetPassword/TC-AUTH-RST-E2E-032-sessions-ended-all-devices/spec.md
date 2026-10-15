---
id: TC-AUTH-RST-E2E-032-sessions-ended-all-devices
title: "Submit Sukses Mengakhiri Semua Sesi Aktif di Semua Device"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-113
coverage:
  web: automated
  mobile: automated
---

# Submit Sukses Mengakhiri Semua Sesi Aktif di Semua Device

## Prerequisites

- Mode: FE+BE (kelas c: multi-konteks, web dan Android).
- Seeding: user subjek `Budi Santoso` (`budisantoso+{runId}-032@qwertysystem.net`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`, tanpa gate Agreement dan MFA (fixture BE). Di hook `before`, user login di aplikasi Android (sesi mobile aktif) dan di browser web lain (sesi web aktif); satu token reset aktif diterbitkan lewat API Request, tautan dari mail-catcher. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`.
- Kemampuan teknis: aplikasi native Android TAG Samurai Mobile (perangkat atau emulator) dengan sesi aktif; dua konteks browser web (sesi web A sudah login, browser guest B tanpa sesi); mail-catcher.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat suite.md); mekanisme reset disediakan tim FE/BE.
- Hook `after` menutup semua jendela privat, menghapus sesi browser, mengeluarkan sesi aplikasi Android, dan mengembalikan sesi ke akun default suite.
- TC-AUTH-RST-113: browser guest B belum login; Password dan Confirm Password `Spectra.env.RST_PASSWORD_NEW`.

## Test Steps

### TC-AUTH-RST-113: Submit sukses mengakhiri semua sesi aktif user di semua device

1. Pastikan sesi aktif user ada di aplikasi Android dan di browser web A (disiapkan di hook `before`)
2. Di browser guest B (tanpa sesi login), buka tautan reset milik `budisantoso+{runId}-032@qwertysystem.net` dari mail-catcher
3. Ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password
4. Klik Button [Reset Password]
5. Verifikasi browser menuju halaman Password Reset Successful
6. Periksa sesi di aplikasi Android dan di browser web A
7. Verifikasi sesi di aplikasi Android berstatus Force Logged Out
8. Verifikasi user harus login ulang di aplikasi Android
9. Verifikasi sesi di browser web A berstatus Force Logged Out
10. Verifikasi user harus login ulang di browser web A

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md` (Manual Only karena memerlukan perangkat Android dan dua konteks browser; kebutuhan ditulis di Prerequisites sebagai tugas tim FE).
- Entri logout per sesi (`Logged out (password changed)`) ditulis oleh Session Management dan tidak diasersi di sini (sesuai `TC-AUTH-RST-99`).
- Temuan untuk QA: Post Condition TC-AUTH-RST-113 "sesi produk turunannya berakhir" tidak punya padanan Expected (Expected b hanya sesi Android dan browser web lain) sehingga tidak diasersi (S-01, S-15).

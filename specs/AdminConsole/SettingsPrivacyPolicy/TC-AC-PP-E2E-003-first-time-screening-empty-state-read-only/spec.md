---
id: TC-AC-PP-E2E-003-first-time-screening-empty-state-read-only
title: "First-time Setup: Screening Empty State dan Read Only Tanpa Tombol Create"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-10
  - TC-AC-PP-20
coverage:
  web: automated
---

# First-time Setup: Screening Empty State dan Read Only Tanpa Tombol Create

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before`. Akun kedua (ganti akun eksplisit di tengah spec): Read Only `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Dewi Lestari`), password `Spectra.env.AC_RO_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Dataset Riwayat C (0 versi, belum pernah Publish). Hook `before` men-seed dataset ini lewat Fixture BE; hook `after` mengembalikan dataset ke Riwayat A. Spec tidak membuat data.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).
- Kemampuan teknis: Fixture BE.
- Dokumen Privacy Policy bersifat tunggal platform-wide; suite berjalan serial (`parallel: false`).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_RO_PASSWORD` belum terdaftar: perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.

## Test Steps

### TC-AC-PP-10: First-time setup: belum ada versi menampilkan kerangka halaman dengan empty state dan [Create Privacy Policy]

1. Klik menu Settings > Privacy Policy di sidebar
2. Susuri halaman dari atas ke bawah tanpa mengklik apa pun
3. Verifikasi Header: Breadcrumb "Settings > Privacy Policy"
4. Verifikasi Header: Table Tools `Search | Filter | Download` tetap tampil
5. Verifikasi Body: table head `Version | Published At | Published By | Actions (⋯)` tetap tampil
6. Verifikasi Body: body tabel menampilkan illustration
7. Verifikasi Body: Title "No Privacy Policy has been published yet."
8. Verifikasi Body: Description "Publish the first version of the platform privacy policy."
9. Verifikasi Body: button [Create Privacy Policy] tampil
10. Verifikasi Footer: tidak ada baris data
11. Verifikasi Footer: pagination tidak menampilkan halaman

### TC-AC-PP-20: Read Only pada first-time setup tidak melihat [Create Privacy Policy]

12. Logout dari akun Total Control
13. Login sebagai Read Only (`readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_RO_PASSWORD`)
14. Klik menu Settings > Privacy Policy di sidebar
15. Amati body tabel
16. Verifikasi Title "No Privacy Policy has been published yet."
17. Verifikasi Description "Publish the first version of the platform privacy policy."
18. Verifikasi button [Create Privacy Policy] Hidden (bukan disabled)
19. Verifikasi toolbar `Search | Filter | Download` tetap tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Pembagian TC lintas spec: TC-AC-PP-146 (Download dengan nol baris, dataset Riwayat C, kelas f binary buffer) ada di spec 045 (`TC-AC-PP-E2E-045-download-screening-dan-isi-file`), bukan di spec ini.
- Langkah penghubung: langkah 2 (susur halaman), 12–13 (ganti akun eksplisit, S-07), 15 (amati).
- Temuan untuk QA:
  - Post Condition TC-AC-PP-10 dan TC-AC-PP-20 ("tabel tetap 0 versi") tidak punya langkah observasi tersendiri dan tidak diasersi.

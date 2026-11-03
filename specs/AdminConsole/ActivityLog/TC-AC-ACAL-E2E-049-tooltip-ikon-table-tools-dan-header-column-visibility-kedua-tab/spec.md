---
id: TC-AC-ACAL-E2E-049-tooltip-ikon-table-tools-dan-header-column-visibility-kedua-tab
title: "Tooltip Ikon Table Tools dan Header Column Visibility, Kedua Tab"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-13
coverage:
  web: automated
---

# Tooltip Ikon Table Tools dan Header Column Visibility, Kedua Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; kredensial `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture; nama env `AC_TC_PASSWORD` mengikuti bagian 5 konvensi dan sudah terdaftar di `.env.example` dan `spectra.config.ts`. Email akun memuat placeholder `{namaCompany}` seperti di Pre-setup TC (lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE): hover kursor dan fokus keyboard dengan tombol Tab.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- State global: tidak ada yang diubah (spec read-only, tanpa aksi tulis).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACAL-13: Tooltip ikon Table Tools dan header Column Visibility, kedua tab

1. Arahkan kursor ke icon Search pada tab Session
2. Verifikasi tooltip `Search` tampil
3. Arahkan kursor ke icon Filter
4. Verifikasi tooltip `Filter` tampil
5. Arahkan kursor ke icon Download
6. Verifikasi tooltip `Download` tampil
7. Arahkan kursor ke header `⋯`
8. Verifikasi tooltip `Column Visibility` tampil
9. Klik tab "User Action"
10. Arahkan kursor ke icon Search pada tab User Action
11. Verifikasi tooltip `Search` tampil
12. Arahkan kursor ke icon Filter
13. Verifikasi tooltip `Filter` tampil
14. Arahkan kursor ke icon Download
15. Verifikasi tooltip `Download` tampil
16. Arahkan kursor ke header `⋯`
17. Verifikasi tooltip `Column Visibility` tampil
18. Klik tab "Session"
19. Fokuskan icon Search dengan tombol Tab
20. Verifikasi tooltip `Search` tampil saat fokus keyboard

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-13). Tidak ada TC hanya-BE di spec ini.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 18 (kembali ke tab Session untuk fokus keyboard).
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` (Pre-setup No 1) dan password memakai `AC_TC_PASSWORD` (akun `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`), terdaftar di `.env.example` dan `spectra.config.ts`.
  - TC-13 menamai tooltip header `⋯` sebagai `Column Visibility`, sedangkan TC-01 dan TC-02 menyebut header itu `⋯` pada kolom Actions; spec mengikuti TC untuk masing-masing.

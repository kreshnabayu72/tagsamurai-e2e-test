---
id: TC-GS-IMPORT-E2E-003-screening-state-belum-ada-draft-tab-brand-dan-keenam-sub-tab-identik
title: "Screening State Belum Ada Draft: Tab Brand dan Keenam Sub-Tab Identik"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-15
  - TC-GS-IMPORT-16
coverage:
  web: automated
---

# Screening State Belum Ada Draft: Tab Brand dan Keenam Sub-Tab Identik

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client B (Bayu Santoso) `totalControl_automated_qaTeam2@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTB_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: spec menguji pembukaan menu Import sehingga membuka menu lewat langkah sendiri.
- Data: Client B tanpa draft pada keenam Sub-Tab dan tanpa data master (Kontrak Fixture R1); tidak ada Data Dinamis.
- Reset: hook `beforeEach` mereset Client B ke tanpa draft (skrip reset disediakan tim FE/BE); spec ini tidak membuat data sehingga tidak ada cleanup.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: hover untuk tooltip; skrip reset draft Client B.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-IMPORT-15: Screening state belum ada draft di Tab Brand

1. Buka menu Import dari sidebar
2. Perhatikan seluruh halaman
3. Verifikasi Header memuat Breadcrumb `Import > Brand`
4. Verifikasi Header memuat tombol `[?]`
5. Verifikasi Header memuat tombol icon-only `[Changelog]`
6. Verifikasi Sub-Tab `Brand (aktif) | Measurement | Position | Division | User Login | User Non Login` tampil
7. Verifikasi Staging Metric Cards: Total Rows 0 (Active)
8. Verifikasi Staging Metric Cards: Ready to Import 0 tampil Disabled (angka `0` pudar)
9. Verifikasi Staging Metric Cards: Errors 0 tampil Disabled (angka `0` pudar)
10. Verifikasi Staging Metric Cards: Duplicates 0 tampil Disabled (angka `0` pudar)
11. Hover kartu Errors
12. Verifikasi kartu Errors tidak menampilkan tooltip
13. Verifikasi TableTools Toolbar tidak tampil: tanpa Switch `Edit this page` dan tanpa Bulk Action Bar
14. Verifikasi Dropzone menggantikan Toolbar, Staging DataTable, dan Pagination
15. Verifikasi Dropzone menampilkan teks "Drag and drop your CSV or XLSX file here, or browse from your device."
16. Verifikasi Dropzone memuat Button `[Download Template]` bergaya outline, aktif, bertulisan tanpa icon
17. Verifikasi Dropzone memuat Button `[Upload File]` bergaya filled, aktif, bertulisan tanpa icon, paling kanan
18. Verifikasi Footer `[Import (0)]` Disabled
19. Hover `[Import (0)]`
20. Verifikasi muncul tooltip "No rows are ready to import."
21. Verifikasi Unsaved Banner tidak tampil
22. Verifikasi Error Summary Callout tidak tampil

### TC-GS-IMPORT-16: State belum ada draft tampil identik di keenam Sub-Tab

23. Perhatikan area tabel Sub-Tab Brand
24. Verifikasi Sub-Tab Brand menampilkan Dropzone yang memuat `[Download Template]` dan `[Upload File]`, tanpa Toolbar dan tanpa Staging DataTable
25. Verifikasi Sub-Tab Brand menampilkan Staging Metric Cards Total Rows 0, Ready to Import 0, Errors 0, dan Duplicates 0
26. Verifikasi Sub-Tab Brand menampilkan `[Import (0)]` Disabled
27. Klik Sub-Tab Measurement
28. Perhatikan area tabel Sub-Tab Measurement
29. Verifikasi Sub-Tab Measurement menampilkan Dropzone yang memuat `[Download Template]` dan `[Upload File]`, tanpa Toolbar dan tanpa Staging DataTable
30. Verifikasi Sub-Tab Measurement menampilkan Staging Metric Cards Total Rows 0, Ready to Import 0, Errors 0, dan Duplicates 0
31. Verifikasi Sub-Tab Measurement menampilkan `[Import (0)]` Disabled
32. Klik Sub-Tab Position
33. Perhatikan area tabel Sub-Tab Position
34. Verifikasi Sub-Tab Position menampilkan Dropzone yang memuat `[Download Template]` dan `[Upload File]`, tanpa Toolbar dan tanpa Staging DataTable
35. Verifikasi Sub-Tab Position menampilkan Staging Metric Cards Total Rows 0, Ready to Import 0, Errors 0, dan Duplicates 0
36. Verifikasi Sub-Tab Position menampilkan `[Import (0)]` Disabled
37. Klik Sub-Tab Division
38. Perhatikan area tabel Sub-Tab Division
39. Verifikasi Sub-Tab Division menampilkan Dropzone yang memuat `[Download Template]` dan `[Upload File]`, tanpa Toolbar dan tanpa Staging DataTable
40. Verifikasi Sub-Tab Division menampilkan Staging Metric Cards Total Rows 0, Ready to Import 0, Errors 0, dan Duplicates 0
41. Verifikasi Sub-Tab Division menampilkan `[Import (0)]` Disabled
42. Klik Sub-Tab User Login
43. Perhatikan area tabel Sub-Tab User Login
44. Verifikasi Sub-Tab User Login menampilkan Dropzone yang memuat `[Download Template]` dan `[Upload File]`, tanpa Toolbar dan tanpa Staging DataTable
45. Verifikasi Sub-Tab User Login menampilkan Staging Metric Cards Total Rows 0, Ready to Import 0, Errors 0, dan Duplicates 0
46. Verifikasi Sub-Tab User Login menampilkan `[Import (0)]` Disabled
47. Klik Sub-Tab User Non Login
48. Perhatikan area tabel Sub-Tab User Non Login
49. Verifikasi Sub-Tab User Non Login menampilkan Dropzone yang memuat `[Download Template]` dan `[Upload File]`, tanpa Toolbar dan tanpa Staging DataTable
50. Verifikasi Sub-Tab User Non Login menampilkan Staging Metric Cards Total Rows 0, Ready to Import 0, Errors 0, dan Duplicates 0
51. Verifikasi Sub-Tab User Non Login menampilkan `[Import (0)]` Disabled

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 1 membuka menu Import karena TC-GS-IMPORT-15 menyebutnya; TC-GS-IMPORT-16 berlanjut pada sesi yang sama tanpa buka ulang (Sub-Tab Brand diamati lebih dulu pada halaman yang sama, lalu klik Sub-Tab berikutnya), sehingga langkah buka menu TC-GS-IMPORT-16 tidak diulang.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2, 23, 28, 33, 38, 43, dan 48 (mengamati sesuai Langkah Uji TC) dan klik Sub-Tab (langkah 27, 32, 37, 42, 47).
- Spec melewati sekitar 35 langkah (51 langkah). Blok kedua (enam Sub-Tab) berpola homogen: langkah 23 sampai 51 mengulang pola "klik Sub-Tab, amati, verifikasi tiga klausa" untuk enam Sub-Tab; sah sebagai langkah berulang per Sub-Tab, tiap Sub-Tab berdiri sendiri.
- Temuan untuk QA:
  - Skrip reset Client B ke tanpa draft tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).

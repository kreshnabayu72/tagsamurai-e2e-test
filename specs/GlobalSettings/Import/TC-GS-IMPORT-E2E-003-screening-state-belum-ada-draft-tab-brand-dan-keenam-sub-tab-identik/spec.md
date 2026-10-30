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
13. Verifikasi Toolbar: `[Download Template]` aktif
14. Verifikasi Toolbar: `[Upload File]` aktif
15. Verifikasi Toolbar: Switch `Edit this page` Disabled
16. Hover toggle `Edit this page`
17. Verifikasi toggle `Edit this page` tidak menampilkan tooltip
18. Verifikasi Dropzone menggantikan Staging DataTable dan Pagination
19. Verifikasi Dropzone menampilkan teks "Drag and drop your CSV or XLSX file here, or browse from your device."
20. Verifikasi Dropzone memuat tombol `[Browse File]`
21. Verifikasi Footer `[Import (0)]` Disabled
22. Hover `[Import (0)]`
23. Verifikasi muncul tooltip "No rows are ready to import."
24. Verifikasi Unsaved Banner tidak tampil
25. Verifikasi Error Summary Callout tidak tampil

### TC-GS-IMPORT-16: State belum ada draft tampil identik di keenam Sub-Tab

26. Perhatikan area tabel Sub-Tab Brand
27. Verifikasi Sub-Tab Brand menampilkan Dropzone, tanpa Staging DataTable
28. Verifikasi Sub-Tab Brand menampilkan Staging Metric Cards Total Rows 0, Ready to Import 0, Errors 0, dan Duplicates 0
29. Verifikasi Sub-Tab Brand menampilkan `[Import (0)]` Disabled
30. Klik Sub-Tab Measurement
31. Perhatikan area tabel Sub-Tab Measurement
32. Verifikasi Sub-Tab Measurement menampilkan Dropzone, tanpa Staging DataTable
33. Verifikasi Sub-Tab Measurement menampilkan Staging Metric Cards Total Rows 0, Ready to Import 0, Errors 0, dan Duplicates 0
34. Verifikasi Sub-Tab Measurement menampilkan `[Import (0)]` Disabled
35. Klik Sub-Tab Position
36. Perhatikan area tabel Sub-Tab Position
37. Verifikasi Sub-Tab Position menampilkan Dropzone, tanpa Staging DataTable
38. Verifikasi Sub-Tab Position menampilkan Staging Metric Cards Total Rows 0, Ready to Import 0, Errors 0, dan Duplicates 0
39. Verifikasi Sub-Tab Position menampilkan `[Import (0)]` Disabled
40. Klik Sub-Tab Division
41. Perhatikan area tabel Sub-Tab Division
42. Verifikasi Sub-Tab Division menampilkan Dropzone, tanpa Staging DataTable
43. Verifikasi Sub-Tab Division menampilkan Staging Metric Cards Total Rows 0, Ready to Import 0, Errors 0, dan Duplicates 0
44. Verifikasi Sub-Tab Division menampilkan `[Import (0)]` Disabled
45. Klik Sub-Tab User Login
46. Perhatikan area tabel Sub-Tab User Login
47. Verifikasi Sub-Tab User Login menampilkan Dropzone, tanpa Staging DataTable
48. Verifikasi Sub-Tab User Login menampilkan Staging Metric Cards Total Rows 0, Ready to Import 0, Errors 0, dan Duplicates 0
49. Verifikasi Sub-Tab User Login menampilkan `[Import (0)]` Disabled
50. Klik Sub-Tab User Non Login
51. Perhatikan area tabel Sub-Tab User Non Login
52. Verifikasi Sub-Tab User Non Login menampilkan Dropzone, tanpa Staging DataTable
53. Verifikasi Sub-Tab User Non Login menampilkan Staging Metric Cards Total Rows 0, Ready to Import 0, Errors 0, dan Duplicates 0
54. Verifikasi Sub-Tab User Non Login menampilkan `[Import (0)]` Disabled

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 1 membuka menu Import karena TC-GS-IMPORT-15 menyebutnya; TC-GS-IMPORT-16 berlanjut pada sesi yang sama tanpa buka ulang (Sub-Tab Brand diamati lebih dulu pada halaman yang sama, lalu klik Sub-Tab berikutnya), sehingga langkah buka menu TC-GS-IMPORT-16 tidak diulang.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2, 26, 31, 36, 41, 46, dan 51 (mengamati sesuai Langkah Uji TC) dan klik Sub-Tab (langkah 30, 35, 40, 45, 50).
- Spec melewati sekitar 35 langkah (54 langkah). Blok kedua (enam Sub-Tab) berpola homogen: langkah 26 sampai 54 mengulang pola "klik Sub-Tab, amati, verifikasi tiga klausa" untuk enam Sub-Tab; sah sebagai langkah berulang per Sub-Tab, tiap Sub-Tab berdiri sendiri.
- Temuan untuk QA:
  - TC-GS-IMPORT-15 Expected d menyebut toolbar `[Download Template]` dan `[Upload File]` aktif dengan Switch `Edit this page` Disabled pada state tanpa draft; PRD §7.1 menampilkan Dropzone sebagai pengganti Staging Table (lihat juga TC-GS-IMPORT-195 pada spec lain). Spec mengikuti TC.
  - Skrip reset Client B ke tanpa draft tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).

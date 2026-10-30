---
id: TC-GS-IMPORT-E2E-018-append-ke-draft-yang-sudah-ada-dialog-confirm-append-cancel-leave
title: "Append ke Draft yang Sudah Ada: Dialog Confirm Append (Cancel, Leave, Append Records), Row Lanjut, dan Nama Lebih dari 120 Karakter Menjadi Error dengan Badge AI"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-68
  - TC-GS-IMPORT-71
  - TC-GS-IMPORT-72
  - TC-GS-IMPORT-73
  - TC-GS-IMPORT-74
coverage:
  web: automated
---

# Append ke Draft yang Sudah Ada: Dialog Confirm Append (Cancel, Leave, Append Records), Row Lanjut, dan Nama Lebih dari 120 Karakter Menjadi Error dengan Badge AI

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena spec memakai draft bersama Client A dan mock layanan AI; lihat `suite.md`.
- Akun aktor (Client A):
  - Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-71. Login sekali di hook `before` dengan `Spectra.env.GS_TC2_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`).
  - Total Control (Client A, Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-72, 68, 73, dan 74: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_TC_PASSWORD`. Hook `after` mengembalikan sesi ke Total Control Client A.
  - Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk akun aktor pertama; sesudah ganti akun, langkah membuka menu Import ditulis eksplisit.
- Data Dinamis:
  - D-01: draft Brand 12 baris `pending` (`brand-12.csv`) pada Client A yang dibuat oleh akun Total Control, disiapkan skrip fixture dan dipulihkan sebelum TC-GS-IMPORT-74 (karena TC-GS-IMPORT-73 menambah 6 baris).
  - `brand-6.csv` (header `Brand Name`; Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp).
  - `brand-overlength.csv` (header `Brand Name`; 1 baris berisi nilai sumber Brand pertama D-41, 121 karakter: `PT Samsung Electronics Indonesia Manufacturing and Distribution Company for Consumer Electronics and Home Appliances Prod`).
  - D-40: mode mock layanan AI normal (tabel D-41 dan D-42) sehingga badge saran `Samsung Electronics Indonesia` tampil pada TC-GS-IMPORT-74.
- Reset dan cleanup: hook `beforeEach` memulihkan draft dasar Client A ke D-01 (Kontrak Fixture R2); hook `after` memulihkan draft dasar dan mengembalikan mock AI ke normal. Cleanup tidak berasumsi seeding berhasil penuh.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk kedua akun, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip seed/reset draft (disediakan tim FE/BE); mock AI D-40 (disediakan tim FE/BE); ganti akun.
- State global: mode mock layanan AI (dikembalikan ke normal) dan draft Client A (dipulihkan hook).

## Test Steps

### TC-GS-IMPORT-71: Screening Dialog Confirm Append Draft saat upload ke tab yang sudah punya draft (Admin kedua)

1. Klik `[Upload File]`
2. Pilih berkas `brand-6.csv` di file picker
3. Perhatikan dialog
4. Verifikasi dialog dengan Title "Append to Draft"
5. Verifikasi Body dialog "The organization already has an active draft for this import type. Do you want to append new records to it?"
6. Verifikasi dialog memuat tombol `[Cancel]` dan `[Append Records]`
7. Klik `[Cancel]` pada dialog Append to Draft

### TC-GS-IMPORT-72: Cancel pada Dialog Confirm Append Draft tidak membuka Modal Column Mapping

8. Ganti akun: logout dari Admin kedua Client A
9. Login sebagai Total Control Client A dengan `Spectra.env.GS_TC_PASSWORD`
10. Buka menu Import dari sidebar (User berada di Import > Brand)
11. Klik `[Upload File]`
12. Pilih berkas `brand-6.csv` di file picker
13. Klik `[Cancel]` pada dialog Append to Draft
14. Perhatikan halaman dan Staging Table
15. Verifikasi dialog tertutup
16. Verifikasi Modal Column Mapping tidak terbuka
17. Verifikasi Staging Metric Cards tetap Total Rows 12
18. Verifikasi Pagination tetap `Showing 1 - 10 of 12 items`

### TC-GS-IMPORT-68: Leave pada kasus Append membiarkan draft existing utuh

19. Klik `[Upload File]`
20. Pilih berkas `brand-6.csv` di file picker
21. Klik `[Append Records]` pada dialog Append to Draft
22. Ubah dropdown Brand Name menjadi "No Column"
23. Klik `[Cancel]` pada modal
24. Klik `[Leave]` pada dialog Unsaved Changes
25. Perhatikan Staging Table
26. Verifikasi Modal Column Mapping tertutup
27. Verifikasi Staging Metric Cards tetap Total Rows 12
28. Verifikasi Pagination tetap `Showing 1 - 10 of 12 items`
29. Klik halaman 2 pada Pagination
30. Verifikasi halaman 2 hanya menampilkan `Row #` 11 dan 12
31. Verifikasi tidak ada baris Nikon
32. Klik halaman 1 pada Pagination

### TC-GS-IMPORT-73: Append Records menambahkan baris ke akhir Staging Table dan melanjutkan Row #

33. Klik `[Upload File]`
34. Pilih berkas `brand-6.csv` di file picker
35. Klik `[Append Records]` pada dialog Append to Draft
36. Perhatikan Modal Column Mapping
37. Verifikasi Modal Column Mapping terbuka
38. Klik `[Confirm Mapping]`
39. Verifikasi modal tertutup
40. Verifikasi muncul toast sukses "Success, row has been added."
41. Perhatikan Staging Metric Cards dan Footer
42. Verifikasi Staging Metric Cards: Total Rows 18, Ready to Import 18
43. Verifikasi Footer `[Import (18)]`
44. Klik halaman 2 pada Pagination
45. Verifikasi halaman 2 menampilkan `Row #` 11 sampai 18
46. Verifikasi enam baris baru (Nikon sampai Sharp) berada di akhir pada `Row #` 13-18

### TC-GS-IMPORT-74: Append berkas Brand dengan satu nama lebih dari 120 karakter membentuk baris error

47. Pulihkan draft Brand Client A ke D-01 (12 baris `pending`) dan atur mock AI mode normal D-40; muat ulang halaman Import > Brand
48. Klik `[Upload File]`
49. Pilih berkas `brand-overlength.csv` di file picker
50. Klik `[Append Records]` pada dialog Append to Draft
51. Klik `[Confirm Mapping]`
52. Verifikasi modal tertutup
53. Perhatikan Staging Table, Error Summary Callout, dan Staging Metric Cards
54. Verifikasi Error Summary Callout tampil: "Brand Name: Max. 120 characters" dengan badge "1 row"
55. Verifikasi Staging Metric Cards: Total Rows 13, Ready to Import 12, Errors 1
56. Verifikasi Pagination `Showing 1 - 10 of 13 items`
57. Klik halaman 2 pada Pagination
58. Perhatikan baris `Row #` 13
59. Verifikasi baris baru `Row #` 13 masuk Staging Table berstatus `error`
60. Verifikasi sel Brand Name baris `Row #` 13 menampilkan badge inline "AI suggestion: 'Samsung Electronics Indonesia'?"
61. Verifikasi badge memuat `[Accept]` dan `[Dismiss]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 71 (Admin kedua), lalu ganti akun ke Total Control untuk 72, 68, 73, 74. TC-GS-IMPORT-73 dan 74 menambah baris ke draft sehingga ditaruh paling akhir; draft dipulihkan ke D-01 sebelum TC-GS-IMPORT-74 (langkah 47, S-09).
- Alasan di atas sekitar 35 langkah (61 langkah): satu topik (Append ke draft yang sudah ada) pada satu draft Client A; blok pada akun lain (Admin kedua, TC-GS-IMPORT-71) di awal dengan langkah ganti akun eksplisit; tiap blok berdiri sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3, 14, 25, 36, 41, 53, 58 (mengamati sesuai Langkah Uji TC), langkah 7 (menutup dialog dengan `[Cancel]`), langkah 8 sampai 10 (ganti akun dan buka menu), langkah 47 (pemulihan draft dan mock lewat skrip fixture sinkron, tanpa penanda tunggu), langkah 29, 32, 44, 57 (pindah halaman Pagination).
- Langkah 29 sampai 32 membawa pengecekan absence `Nikon` ke halaman 2 karena draft 12 baris tampil 10 baris per halaman; langkah 30 (`Verifikasi` halaman 2 hanya memuat `Row #` 11 dan 12) adalah asersi tambahan di luar Expected TC dan menjadi anchor positif untuk absence di langkah 31 (S-03, S-14). Langkah 32 mengembalikan Pagination ke halaman 1.
- Pembagian TC: asersi AI pada TC-GS-IMPORT-74 hanya memverifikasi badge AI muncul pada baris error; perilaku Accept/Dismiss diuji di spec AI.
- Temuan untuk QA:
  - TC-GS-IMPORT-71 memakai Admin kedua Client A untuk screening dialog Append; TC tidak menyebut password/env akun, `GS_TC2_PASSWORD` baru.
  - Skrip seed/reset draft dan mode mock AI tidak didefinisikan sebagai endpoint di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
  - Post Condition TC-GS-IMPORT-73 ("Draft Brand 18 baris") dan TC-GS-IMPORT-74 ("Draft Brand 13 baris dengan 1 baris error") diasersi lewat Expected TC yang sama; tidak ada asersi tambahan.

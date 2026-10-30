---
id: TC-GS-IMPORT-E2E-069-aksi-admin-kedua-ditolak-409-saat-kunci-dipegang-append-confirm-mapping
title: "Aksi Admin Kedua Ditolak 409 saat Kunci Dipegang: Append, Confirm Mapping, Remove, Bulk Delete, Discard Draft, dan Import Commit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-238
  - TC-GS-IMPORT-239
  - TC-GS-IMPORT-240
  - TC-GS-IMPORT-241
  - TC-GS-IMPORT-245
  - TC-GS-IMPORT-246
coverage:
  web: automated
---

# Aksi Admin Kedua Ditolak 409 saat Kunci Dipegang: Append, Confirm Mapping, Remove, Bulk Delete, Discard Draft, dan Import Commit

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Dua sesi browser (kelas multi-konteks), konteks terpisah dengan sesi login sendiri, keduanya login di hook `before` dan berada di Import > Brand Client A:
  - Sesi TC: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`.
  - Sesi Admin kedua: Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC2_PASSWORD`.
  - Password tidak ditulis di spec atau fixture. Hook `after` menutup konteks Sesi Admin kedua dan mengembalikan sesi ke akun default suite.
- Data Dinamis (Client A, dipulihkan lewat skrip fixture sebelum tiap TC): D-01 draft Brand 12 baris `pending` dari `brand-12.csv` (Row # 1 `Acme Corp`, #5 `Dell`, #6 `HP Inc`); `brand-6.csv` (header `Brand Name`; Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp). D-76 varian 1 (`created_at` dimundurkan 25 jam, hanya seed backdate) sehingga Unsaved Banner tampil pada TC-GS-IMPORT-245.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk kedua sesi. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk kedua akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: sesi edit Sesi TC ditutup dengan `[Cancel]` di akhir tiap blok; draft D-01 dipulihkan antar TC.

## Test Steps

### TC-GS-IMPORT-238: Upload berkas baru (Append) oleh Admin kedua

1. [Sesi TC] Klik `⋯` pada baris #1
2. [Sesi TC] Pilih Edit
3. [Sesi Admin kedua] Klik `[Upload File]`
4. [Sesi Admin kedua] Pilih `brand-6.csv` di file picker
5. [Sesi Admin kedua] Verifikasi dialog Title "Append to Draft" dengan Body "The organization already has an active draft for this import type. Do you want to append new records to it?" dan tombol `[Cancel]` dan `[Append Records]`
6. [Sesi Admin kedua] Klik `[Append Records]` pada dialog Append to Draft
7. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
8. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
9. [Sesi Admin kedua] Verifikasi dialog tertutup
10. [Sesi Admin kedua] Verifikasi Modal Column Mapping tidak tampil
11. [Sesi Admin kedua] Muat ulang halaman Import > Brand
12. [Sesi Admin kedua] Verifikasi Staging Metric Cards Total Rows tetap 12
13. [Sesi TC] Verifikasi baris #1 tetap input aktif
14. [Sesi TC] Verifikasi footer tetap `[Cancel]` dan `[Save]`
15. [Sesi TC] Klik `[Cancel]` pada footer

### TC-GS-IMPORT-239: Confirm Mapping oleh Admin kedua

16. [Sesi Admin kedua] Klik `[Upload File]`
17. [Sesi Admin kedua] Pilih `brand-6.csv` di file picker
18. [Sesi Admin kedua] Klik `[Append Records]` pada dialog Append to Draft
19. [Sesi TC] Klik `⋯` pada baris #1
20. [Sesi TC] Pilih Edit
21. [Sesi Admin kedua] Klik `[Confirm Mapping]` pada Modal Column Mapping
22. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
23. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
24. [Sesi Admin kedua] Muat ulang halaman Import > Brand
25. [Sesi Admin kedua] Verifikasi Staging Metric Cards Total Rows tetap 12
26. [Sesi TC] Verifikasi baris #1 tetap input aktif
27. [Sesi TC] Verifikasi footer tetap `[Cancel]` dan `[Save]`
28. [Sesi TC] Klik `[Cancel]` pada footer

### TC-GS-IMPORT-240: Remove baris oleh Admin kedua

29. [Sesi TC] Klik `⋯` pada baris #1
30. [Sesi TC] Pilih Edit
31. [Sesi Admin kedua] Klik `⋯` pada baris #5
32. [Sesi Admin kedua] Pilih Remove
33. [Sesi Admin kedua] Klik `[Delete]` pada dialog Delete Row
34. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
35. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
36. [Sesi Admin kedua] Muat ulang halaman Import > Brand
37. [Sesi Admin kedua] Verifikasi Staging Metric Cards Total Rows tetap 12
38. [Sesi Admin kedua] Verifikasi baris #5 `Dell` tetap ada
39. [Sesi TC] Verifikasi baris #1 tetap input aktif
40. [Sesi TC] Verifikasi footer tetap `[Cancel]` dan `[Save]`
41. [Sesi TC] Klik `[Cancel]` pada footer

### TC-GS-IMPORT-241: Bulk Delete oleh Admin kedua

42. [Sesi TC] Klik `⋯` pada baris #1
43. [Sesi TC] Pilih Edit
44. [Sesi Admin kedua] Centang baris #5 dan #6
45. [Sesi Admin kedua] Klik `[Bulk Action ▾]`
46. [Sesi Admin kedua] Klik `[Delete]` pada overlay
47. [Sesi Admin kedua] Klik `[Delete]` pada dialog Delete Rows
48. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
49. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
50. [Sesi Admin kedua] Muat ulang halaman Import > Brand
51. [Sesi Admin kedua] Verifikasi Staging Metric Cards Total Rows tetap 12
52. [Sesi Admin kedua] Verifikasi baris #5 `Dell` dan baris #6 `HP Inc` tetap ada
53. [Sesi TC] Verifikasi baris #1 tetap input aktif
54. [Sesi TC] Verifikasi footer tetap `[Cancel]` dan `[Save]`
55. [Sesi TC] Klik `[Cancel]` pada footer

### TC-GS-IMPORT-245: Discard Draft oleh Admin kedua

56. Siapkan draft D-01 berumur 25 jam (varian 1) dan muat ulang halaman Import > Brand pada kedua sesi
57. [Sesi TC] Klik `⋯` pada baris #1
58. [Sesi TC] Pilih Edit
59. [Sesi Admin kedua] Klik `[Discard]` pada Unsaved Banner
60. [Sesi Admin kedua] Klik `[Discard Draft]` pada dialog Discard Draft
61. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
62. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
63. [Sesi Admin kedua] Muat ulang halaman Import > Brand
64. [Sesi Admin kedua] Verifikasi Unsaved Banner tetap tampil
65. [Sesi Admin kedua] Verifikasi Staging Metric Cards Total Rows tetap 12
66. [Sesi TC] Verifikasi baris #1 tetap input aktif
67. [Sesi TC] Verifikasi footer tetap `[Cancel]` dan `[Save]`
68. [Sesi TC] Klik `[Cancel]` pada footer

### TC-GS-IMPORT-246: Import (commit) oleh Admin kedua

69. [Sesi TC] Klik `⋯` pada baris #1
70. [Sesi TC] Pilih Edit
71. [Sesi Admin kedua] Klik `[Import (12)]`
72. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
73. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
74. [Sesi Admin kedua] Muat ulang halaman Import > Brand
75. [Sesi Admin kedua] Verifikasi footer `[Import (12)]` tetap Enabled
76. [Sesi Admin kedua] Verifikasi Staging Metric Cards Total Rows tetap 12 (tidak ada commit berjalan)
77. [Sesi TC] Verifikasi baris #1 tetap input aktif
78. [Sesi TC] Verifikasi footer tetap `[Cancel]` dan `[Save]`
79. [Sesi TC] Klik `[Cancel]` pada footer

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: multi-konteks (kelas c, prinsip 13c); kedua sesi UI menjadi objek asersi.
- Spec memuat 79 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (dua sesi admin pada Client A), tiap blok mengikuti pola identik (Sesi TC memegang kunci, Admin kedua mencoba satu aksi tulis, ditolak dengan dialog, sesi TC tidak berubah) dan berdiri sendiri dengan draft D-01 yang dipulihkan, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 15, 28, 41, 55, 68, 79 (menutup sesi edit Sesi TC), langkah 11, 24, 36, 50, 63, 74 (muat ulang Sesi Admin kedua), langkah 56 (menyiapkan draft berumur 25 jam).
- Aksi Admin kedua tiap blok (Upload File, Confirm Mapping, Remove, Bulk Delete, Discard, Import) tidak diasersi UI-nya selain dialog yang tampil, mengikuti Expected TC.
- Pembagian TC lintas spec: TC-GS-IMPORT-242 sampai 244 (Delete All Rows, AI Accept, AI Dismiss) ada di spec 070; TC-GS-IMPORT-247 (Create Missing Divisions) di spec 071; TC-GS-IMPORT-237, 248, 249, 679, 680 di spec 068.
- Temuan untuk QA:
  - TC-GS-IMPORT-239 dan 241 menyebut "setelah muat ulang halaman" tanpa nomor langkah pada Expected b; spec memetakan ke langkah muat ulang masing-masing.
  - TC-GS-IMPORT-240, 241, 245, 246 tidak menyebut cara menutup sesi edit Total Control; spec menambahkan `[Cancel]` sebagai langkah penghubung.

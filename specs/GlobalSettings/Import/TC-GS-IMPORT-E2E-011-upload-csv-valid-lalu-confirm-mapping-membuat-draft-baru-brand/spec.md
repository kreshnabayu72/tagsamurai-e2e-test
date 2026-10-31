---
id: TC-GS-IMPORT-E2E-011-upload-csv-valid-lalu-confirm-mapping-membuat-draft-baru-brand
title: "Upload CSV Valid Lalu Confirm Mapping Membuat Draft Baru: Brand, Measurement, dan Position (Plus Verifikasi Changelog)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-1
  - TC-GS-IMPORT-2
  - TC-GS-IMPORT-3
coverage:
  web: automated
---

# Upload CSV Valid Lalu Confirm Mapping Membuat Draft Baru: Brand, Measurement, dan Position (Plus Verifikasi Changelog)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena spec membuat draft bersama Client A; lihat `suite.md`.
- Akun aktor: Total Control (Client A, Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand; perpindahan Sub-Tab ke Measurement dan Position ditulis sebagai langkah eksplisit.
- Data Dinamis (berkas fixture D-07, satu nama berkas satu isi, nama literal Population):
  - D-01: `brand-12.csv` (header `Brand Name`; 12 baris berurutan: Acme Corp, Lenovo, Zebra Technologies, Honeywell, Dell, HP Inc, Canon, Epson, Brother, Logitech, Cisco, Asus; tidak bentrok dengan Pre-setup).
  - D-02: `measurement-6.csv` (header `Unit Name,Symbol`; Meter/m, Liter/L, Piece/pcs, Gram/g, Centimeter/cm, Dozen/dz; tidak bentrok dengan Kilogram/kg).
  - D-03: `position-6.csv` (header `Position Name`; Warehouse Supervisor, Field Technician, HR Business Partner, IT Operations Lead, Procurement Officer, Sales Executive).
- Reset: hook `beforeEach` mereset Client A ke tanpa draft pada Tab Brand, Measurement, dan Position (Precondition TC; skrip reset disediakan tim FE/BE) dan hook `after` membuang draft yang dibuat spec; draft yang dibuat TC ini menjadi draft Population Client A dan dipulihkan hook sesudah spec (Kontrak Fixture R2).
- Changelog: baseline jumlah entri Action `Import Brand`, `Import Measurement`, dan `Import Position` dicatat sebelum Upload (langkah 1 sampai 5, 29 sampai 33, 53 sampai 57); total absolut tidak diasersi (S-12).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft; pembacaan teks Pagination pada modal Changelog.
- State global: tidak ada yang diubah selain draft Client A.

## Test Steps

### TC-GS-IMPORT-1: Upload berkas CSV valid di Tab Brand lalu Confirm Mapping membuat draft baru

1. Klik tombol `[Changelog]` di header halaman
2. Klik icon Filter
3. Pilih Action `Import Brand` pada dropdown Action
4. Klik `[Apply]`
5. Catat jumlah entri hasil filter dari teks Pagination (0 bila tabel menampilkan empty state) sebagai baseline Brand
6. Tutup modal Changelog
7. Klik `[Upload File]` di toolbar
8. Pilih berkas `brand-12.csv` di file picker
9. Perhatikan Modal Column Mapping yang terbuka
10. Verifikasi Modal Column Mapping berjudul `Column Mapping: Brand`
11. Verifikasi deskripsi modal "Map columns from your uploaded file to the system attributes."
12. Verifikasi tidak ada toast upload
13. Verifikasi atribut `Brand Name` terisi otomatis dengan kolom berkas bernama sama
14. Verifikasi tidak ada Error Banner
15. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column
16. Verifikasi modal tertutup
17. Verifikasi muncul toast sukses "Success, row has been added."
18. Perhatikan Staging Table, Staging Metric Cards, Pagination, Footer, dan area di atas Staging Metric Cards
19. Verifikasi Staging Table halaman 1 menampilkan 10 baris berstatus `pending` berurut `Row #` 1-10
20. Verifikasi Pagination `Showing 1 - 10 of 12 items`
21. Verifikasi Staging Metric Cards: Total Rows 12 (Active), Ready to Import 12, Errors 0 (Disabled), Duplicates 0 (Disabled)
22. Verifikasi Footer menampilkan `[Import (12)]`
23. Verifikasi Unsaved Banner tidak tampil
24. Verifikasi tidak ada tombol `[Discard]` di halaman
25. Klik halaman 2 pada Pagination
26. Verifikasi halaman 2 menampilkan 2 baris berstatus `pending` dengan `Row #` 11-12
27. Verifikasi Pagination `Showing 11 - 12 of 12 items`
28. Klik tombol `[Changelog]` di header halaman
29. Klik icon Filter
30. Pilih Action `Import Brand` pada dropdown Action
31. Klik `[Apply]`
32. Perhatikan teks Pagination pada modal Changelog
33. Verifikasi jumlah entri hasil filter Action `Import Brand` sama dengan baseline langkah 5 (empty state bila baseline 0)
34. Tutup modal Changelog

### TC-GS-IMPORT-2: Upload berkas CSV valid di Tab Measurement lalu Confirm Mapping membuat draft baru

35. Klik Sub-Tab Measurement
36. Klik tombol `[Changelog]` di header halaman
37. Klik icon Filter
38. Pilih Action `Import Measurement` pada dropdown Action
39. Klik `[Apply]`
40. Catat jumlah entri hasil filter dari teks Pagination (0 bila empty state) sebagai baseline Measurement
41. Tutup modal Changelog
42. Klik `[Upload File]` di toolbar
43. Pilih berkas `measurement-6.csv` di file picker
44. Perhatikan Modal Column Mapping yang terbuka
45. Verifikasi Modal Column Mapping berjudul `Column Mapping: Measurement`
46. Verifikasi deskripsi modal "Map columns from your uploaded file to the system attributes."
47. Verifikasi tidak ada toast upload
48. Verifikasi atribut `Unit Name` dan `Symbol` terisi otomatis dengan kolom berkas bernama sama
49. Verifikasi tidak ada Error Banner
50. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column
51. Verifikasi modal tertutup
52. Verifikasi muncul toast sukses "Success, row has been added."
53. Perhatikan Staging Table, Staging Metric Cards, Pagination, Footer, dan area di atas Staging Metric Cards
54. Verifikasi Staging Table halaman 1 menampilkan 6 baris berstatus `pending` berurut `Row #` 1-6
55. Verifikasi Pagination `Showing 1 - 6 of 6 items`
56. Verifikasi Staging Metric Cards: Total Rows 6 (Active), Ready to Import 6, Errors 0 (Disabled), Duplicates 0 (Disabled)
57. Verifikasi Footer menampilkan `[Import (6)]`
58. Verifikasi Unsaved Banner tidak tampil
59. Verifikasi tidak ada tombol `[Discard]` di halaman
60. Klik tombol `[Changelog]` di header halaman
61. Klik icon Filter
62. Pilih Action `Import Measurement` pada dropdown Action
63. Klik `[Apply]`
64. Perhatikan teks Pagination pada modal Changelog
65. Verifikasi jumlah entri hasil filter Action `Import Measurement` sama dengan baseline langkah 40 (empty state bila baseline 0)
66. Tutup modal Changelog

### TC-GS-IMPORT-3: Upload berkas CSV valid di Tab Position lalu Confirm Mapping membuat draft baru

67. Klik Sub-Tab Position
68. Klik tombol `[Changelog]` di header halaman
69. Klik icon Filter
70. Pilih Action `Import Position` pada dropdown Action
71. Klik `[Apply]`
72. Catat jumlah entri hasil filter dari teks Pagination (0 bila empty state) sebagai baseline Position
73. Tutup modal Changelog
74. Klik `[Upload File]` di toolbar
75. Pilih berkas `position-6.csv` di file picker
76. Perhatikan Modal Column Mapping yang terbuka
77. Verifikasi Modal Column Mapping berjudul `Column Mapping: Position`
78. Verifikasi deskripsi modal "Map columns from your uploaded file to the system attributes."
79. Verifikasi tidak ada toast upload
80. Verifikasi atribut `Position Name` terisi otomatis dengan kolom berkas bernama sama
81. Verifikasi tidak ada Error Banner
82. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column
83. Verifikasi modal tertutup
84. Verifikasi muncul toast sukses "Success, row has been added."
85. Perhatikan Staging Table, Staging Metric Cards, Pagination, Footer, dan area di atas Staging Metric Cards
86. Verifikasi Staging Table halaman 1 menampilkan 6 baris berstatus `pending` berurut `Row #` 1-6
87. Verifikasi Pagination `Showing 1 - 6 of 6 items`
88. Verifikasi Staging Metric Cards: Total Rows 6 (Active), Ready to Import 6, Errors 0 (Disabled), Duplicates 0 (Disabled)
89. Verifikasi Footer menampilkan `[Import (6)]`
90. Verifikasi Unsaved Banner tidak tampil
91. Verifikasi tidak ada tombol `[Discard]` di halaman
92. Klik tombol `[Changelog]` di header halaman
93. Klik icon Filter
94. Pilih Action `Import Position` pada dropdown Action
95. Klik `[Apply]`
96. Perhatikan teks Pagination pada modal Changelog
97. Verifikasi jumlah entri hasil filter Action `Import Position` sama dengan baseline langkah 72 (empty state bila baseline 0)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (97 langkah nominal; tiga blok homogen). Alasan: ketiga blok satu pola yang sama (baca baseline Changelog, Upload, verifikasi mapping dan draft, baca Changelog), masing-masing pada Sub-Tab dan draft sendiri sehingga berdiri sendiri; kegagalan satu blok tidak menghilangkan makna blok lain. Blok baca-log berpola (langkah 1 sampai 6, 28 sampai 34, 36 sampai 41, 60 sampai 66, 68 sampai 73, 92 sampai 97) tidak dihitung ke batas ±35.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6, 34, 41, 66, 73 (tutup modal Changelog); langkah 9, 18, 32, 44, 53, 64, 76, 85, 96 (mengamati sesuai Langkah Uji TC); langkah 25 (halaman 2 hanya TC-GS-IMPORT-1); langkah 35 dan 67 (pindah Sub-Tab).
- Langkah verifikasi Changelog "sama dengan baseline" (langkah 33, 65, 97) mengasersi bahwa Upload dan Confirm Mapping tidak mencatat entri Changelog (Expected i/h TC); asersi memakai baseline jumlah entri hasil filter Action, bukan total absolut atau posisi teratas (S-12).
- Temuan untuk QA:
  - Skrip reset draft Client A (Precondition "belum ada draft aktif Tab ... pada Client A") tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
  - Berkas fixture memakai isi literal tanpa suffix `{runId}`; keunikan dijaga lewat reset draft dan Population D-01 sampai D-03.

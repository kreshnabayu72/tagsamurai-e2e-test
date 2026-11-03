---
id: TC-GS-IMPORT-E2E-012-upload-csv-valid-lalu-confirm-mapping-membuat-draft-baru-division-user
title: "Upload CSV Valid Lalu Confirm Mapping Membuat Draft Baru: Division, User Login, dan User Non Login (Plus Verifikasi Changelog)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-4
  - TC-GS-IMPORT-5
  - TC-GS-IMPORT-6
coverage:
  web: automated
---

# Upload CSV Valid Lalu Confirm Mapping Membuat Draft Baru: Division, User Login, dan User Non Login (Plus Verifikasi Changelog)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena spec membuat draft bersama Client A; lihat `suite.md`.
- Akun aktor: Total Control (Client A, Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand; perpindahan Sub-Tab ke Division, User Login, dan User Non Login ditulis sebagai langkah eksplisit.
- Data Pre-setup Client A (tidak diubah): Division Engineering (ENG), Marketing (MKT), Finance (FINC), Warehouse, Gudang; Position Store Manager, Senior Developer, Finance Manager, Technician, Supervisor; User Login `dewi.anggraini@example.com`, `rina.admin@example.com`, `budi.manager@example.com`; Custom Field Active Shift (Dropdown Pagi/Siang/Malam), Shift Notes (Text Area), Overtime Hours (Numeric 2 desimal), Emergency Phone (Phone), Join Date (Date), semuanya opsional.
- Data Dinamis (berkas fixture D-07, nama literal Population):
  - D-04: `division-6.csv` (header `Division Name,Code`; Finance & Accounting/FIN, Operations/(Code kosong), IT Support/ITS, Receiving/RCV, Procurement/PRC, Sales/SLS; tidak bentrok dengan Division maupun Code Pre-setup).
  - D-05: `user-login-8.csv` (header `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period,Shift,Overtime Hours`; 8 baris: #1 Ahmad Fauzi / ahmad.fauzi@example.com / Engineering / Senior Developer / EMP-1 / Global Settings / Shift `Siang`; #2 Citra Lestari / citra.lestari@example.com / Marketing / Position kosong / Global Settings / Active Period 30 hari setelah hari uji (YYYY-MM-DD, dihitung saat berkas disiapkan) / Shift `Siang`; #3 Budi Setiawan / budi.setiawan@example.com / Finance / Finance Manager / Global Settings;Fixed Asset / Shift `Pagi`; #4 Dedi Prakoso / dedi.prakoso@example.com / Engineering / Technician / Global Settings / Overtime Hours `1.25`; #5 Eka Putri / eka.putri@example.com / Warehouse / Supervisor / Global Settings; #6 Fajar Hidayat / fajar.hidayat@example.com / Gudang / Position kosong / Global Settings; #7 Gita Maharani / gita.maharani@example.com / Marketing / Store Manager / Global Settings;Fixed Asset; #8 Hadi Susanto / hadi.susanto@example.com / Engineering / Senior Developer / Global Settings).
  - D-06: `user-non-login-5.csv` (header `First Name,Last Name,Email,Division,Position,Employee ID,Represented By,Active Period`; #1 Siti Rahayu / siti.rahayu@example.com / Warehouse / Position kosong / Represented By dewi.anggraini@example.com; #2 Rudi Hartono / rudi.hartono@example.com / Engineering / Technician / EMP-2002 / rina.admin@example.com; #3 Maya Kusuma / maya.kusuma@example.com / Marketing / Position kosong / budi.manager@example.com; #4 Bagas Wibowo / bagas.wibowo@example.com / Finance / Finance Manager / dewi.anggraini@example.com; #5 Lia Handayani / lia.handayani@example.com / Gudang / Supervisor / rina.admin@example.com; Active Period kosong).
- Reset: hook `beforeEach` mereset Client A ke tanpa draft pada Tab Division, User Login, dan User Non Login (Precondition TC; skrip reset disediakan tim FE/BE); hook `after` membuang draft yang dibuat spec dan memulihkan draft dasar (Kontrak Fixture R2).
- Changelog: baseline jumlah entri Action `Import Division`, `Import User Login`, dan `Import User Non Login` dicatat sebelum Upload; total absolut tidak diasersi (S-12).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft; pembacaan teks Pagination pada modal Changelog.
- State global: tidak ada yang diubah selain draft Client A.

## Test Steps

### TC-GS-IMPORT-4: Upload berkas CSV valid di Tab Division lalu Confirm Mapping membuat draft baru

1. Klik Sub-Tab Division
2. Klik tombol `[Changelog]` di header halaman
3. Klik icon Filter
4. Pilih Action `Import Division` pada dropdown Action
5. Klik `[Apply]`
6. Catat jumlah entri hasil filter dari teks Pagination (0 bila empty state) sebagai baseline Division
7. Tutup modal Changelog
8. Klik `[Upload File]` di toolbar
9. Pilih berkas `division-6.csv` di file picker
10. Perhatikan Modal Column Mapping yang terbuka
11. Verifikasi Modal Column Mapping berjudul `Column Mapping: Division`
12. Verifikasi deskripsi modal "Map columns from your uploaded file to the system attributes."
13. Verifikasi tidak ada toast upload
14. Verifikasi atribut `Division Name` dan `Code` terisi otomatis dengan kolom berkas bernama sama
15. Verifikasi tidak ada Error Banner
16. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column
17. Verifikasi modal tertutup
18. Verifikasi muncul toast sukses "Success, row has been added."
19. Perhatikan Staging Table, Staging Metric Cards, Pagination, Footer, dan area di atas Staging Metric Cards
20. Verifikasi Staging Table halaman 1 menampilkan 6 baris berstatus `pending` berurut `Row #` 1-6
21. Verifikasi Pagination `Showing 1 - 6 of 6 items`
22. Verifikasi Staging Metric Cards: Total Rows 6 (Active), Ready to Import 6, Errors 0 (Disabled), Duplicates 0 (Disabled)
23. Verifikasi Footer menampilkan `[Import (6)]`
24. Verifikasi Unsaved Banner tidak tampil
25. Verifikasi tidak ada tombol `[Discard]` di halaman
26. Klik tombol `[Changelog]` di header halaman
27. Klik icon Filter
28. Pilih Action `Import Division` pada dropdown Action
29. Klik `[Apply]`
30. Perhatikan teks Pagination pada modal Changelog
31. Verifikasi modal `Changelog: Import` terbuka
32. Verifikasi jumlah entri hasil filter Action `Import Division` sama dengan baseline langkah 6 (empty state bila baseline 0)
33. Tutup modal Changelog

### TC-GS-IMPORT-5: Upload berkas CSV valid di Tab User Login lalu Confirm Mapping membuat draft baru

34. Klik Sub-Tab User Login
35. Klik tombol `[Changelog]` di header halaman
36. Klik icon Filter
37. Pilih Action `Import User Login` pada dropdown Action
38. Klik `[Apply]`
39. Catat jumlah entri hasil filter dari teks Pagination (0 bila empty state) sebagai baseline User Login
40. Tutup modal Changelog
41. Klik `[Upload File]` di toolbar
42. Pilih berkas `user-login-8.csv` di file picker
43. Perhatikan Modal Column Mapping yang terbuka
44. Verifikasi Modal Column Mapping berjudul `Column Mapping: User Login`
45. Verifikasi deskripsi modal "Map columns from your uploaded file to the system attributes."
46. Verifikasi tidak ada toast upload
47. Verifikasi atribut `First Name`, `Last Name`, `Email`, `Division`, `Position`, `Employee ID`, `Access`, `Active Period`, `Shift`, dan `Overtime Hours` terisi otomatis dengan kolom berkas bernama sama
48. Verifikasi atribut Shift Notes, Emergency Phone, dan Join Date tetap "No Column" (opsional)
49. Verifikasi tidak ada Error Banner
50. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column
51. Verifikasi modal tertutup
52. Verifikasi muncul toast sukses "Success, row has been added."
53. Perhatikan Staging Table, Staging Metric Cards, Pagination, Footer, dan area di atas Staging Metric Cards
54. Verifikasi Staging Table halaman 1 menampilkan 8 baris berstatus `pending` berurut `Row #` 1-8
55. Verifikasi Pagination `Showing 1 - 8 of 8 items`
56. Verifikasi Staging Metric Cards: Total Rows 8 (Active), Ready to Import 8, Errors 0 (Disabled), Duplicates 0 (Disabled)
57. Verifikasi Footer menampilkan `[Import (8)]`
58. Verifikasi Unsaved Banner tidak tampil
59. Verifikasi tidak ada tombol `[Discard]` di halaman
60. Klik tombol `[Changelog]` di header halaman
61. Klik icon Filter
62. Pilih Action `Import User Login` pada dropdown Action
63. Klik `[Apply]`
64. Perhatikan teks Pagination pada modal Changelog
65. Verifikasi modal `Changelog: Import` terbuka
66. Verifikasi jumlah entri hasil filter Action `Import User Login` sama dengan baseline langkah 39 (empty state bila baseline 0)
67. Tutup modal Changelog

### TC-GS-IMPORT-6: Upload berkas CSV valid di Tab User Non Login lalu Confirm Mapping membuat draft baru

68. Klik Sub-Tab User Non Login
69. Klik tombol `[Changelog]` di header halaman
70. Klik icon Filter
71. Pilih Action `Import User Non Login` pada dropdown Action
72. Klik `[Apply]`
73. Catat jumlah entri hasil filter dari teks Pagination (0 bila empty state) sebagai baseline User Non Login
74. Tutup modal Changelog
75. Klik `[Upload File]` di toolbar
76. Pilih berkas `user-non-login-5.csv` di file picker
77. Perhatikan Modal Column Mapping yang terbuka
78. Verifikasi Modal Column Mapping berjudul `Column Mapping: User Non Login`
79. Verifikasi deskripsi modal "Map columns from your uploaded file to the system attributes."
80. Verifikasi tidak ada toast upload
81. Verifikasi atribut `First Name`, `Last Name`, `Email`, `Division`, `Position`, `Employee ID`, `Represented By`, dan `Active Period` terisi otomatis dengan kolom berkas bernama sama
82. Verifikasi tidak ada Error Banner
83. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column
84. Verifikasi modal tertutup
85. Verifikasi muncul toast sukses "Success, row has been added."
86. Perhatikan Staging Table, Staging Metric Cards, Pagination, Footer, dan area di atas Staging Metric Cards
87. Verifikasi Staging Table halaman 1 menampilkan 5 baris berstatus `pending` berurut `Row #` 1-5
88. Verifikasi Pagination `Showing 1 - 5 of 5 items`
89. Verifikasi Staging Metric Cards: Total Rows 5 (Active), Ready to Import 5, Errors 0 (Disabled), Duplicates 0 (Disabled)
90. Verifikasi Footer menampilkan `[Import (5)]`
91. Verifikasi Unsaved Banner tidak tampil
92. Verifikasi tidak ada tombol `[Discard]` di halaman
93. Klik tombol `[Changelog]` di header halaman
94. Klik icon Filter
95. Pilih Action `Import User Non Login` pada dropdown Action
96. Klik `[Apply]`
97. Perhatikan teks Pagination pada modal Changelog
98. Verifikasi modal `Changelog: Import` terbuka
99. Verifikasi jumlah entri hasil filter Action `Import User Non Login` sama dengan baseline langkah 73 (empty state bila baseline 0)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (99 langkah nominal; tiga blok homogen). Alasan: ketiga blok satu pola yang sama (baca baseline Changelog, Upload, verifikasi mapping dan draft, baca Changelog), masing-masing pada Sub-Tab dan draft sendiri sehingga berdiri sendiri; kegagalan satu blok tidak menghilangkan makna blok lain. Blok baca-log berpola (langkah 2 sampai 7, 26 sampai 33, 35 sampai 40, 60 sampai 67, 69 sampai 74, 93 sampai 99) tidak dihitung ke batas ±35.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 34, 68 (pindah Sub-Tab); langkah 7, 33, 40, 67, 74 (tutup modal Changelog); langkah 10, 19, 30, 43, 53, 64, 77, 86, 97 (mengamati sesuai Langkah Uji TC).
- Langkah "sama dengan baseline" (31, 64, 96) mengasersi bahwa Upload dan Confirm Mapping tidak mencatat entri Changelog; memakai baseline jumlah entri hasil filter Action, bukan total absolut (S-12).
- Temuan untuk QA:
  - Skrip reset draft Client A tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
  - TC-GS-IMPORT-5 memakai Active Period "30 hari setelah hari uji" yang dihitung saat berkas disiapkan; berkas fixture disiapkan per run oleh tim FE/BE. Berkas literal tanpa suffix `{runId}`; keunikan dijaga lewat reset draft.

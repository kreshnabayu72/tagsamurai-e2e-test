---
id: TC-GS-POS-E2E-041-changelog-sort-dan-pagination
title: "Popup Changelog: Sort Date, Teks, Campuran, dan Modified By, Kombinasi dengan Search dan Filter, Clear, Pemulihan Empty State, dan Pagination"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-221
  - TC-GS-POS-222
  - TC-GS-POS-223
  - TC-GS-POS-224
  - TC-GS-POS-225
  - TC-GS-POS-226
  - TC-GS-POS-227
  - TC-GS-POS-228
coverage:
  web: automated
---

# Popup Changelog: Sort Date, Teks, Campuran, dan Modified By, Kombinasi dengan Search dan Filter, Clear, Pemulihan Empty State, dan Pagination

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
  - Manage user and role Create-Only (Sari Dewi) `manageUserRoleCreate_automated_{namaCompany}@qwertysystem.net` (Pre-setup 5), hanya untuk seeding lewat API di hook `before` (Create `Procurement Analyst`), dengan `Spectra.env.GS_CREATE_PASSWORD`. Tidak dipakai login UI.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position (sidebar Global Settings, sub-tab Position). Spec ini tidak menguji navigasi sehingga `## Test Steps` tidak mengulang langkah buka.
- Data Pre-setup: tidak ada yang dipakai (Changelog entitas Total Control bersifat kumulatif dan dibaca apa adanya).
- Data Dinamis (di-seed lewat API di hook `before` pada entitas Total Control; nama bersuffix per run; fixture baru `Fixture.position.changelogSeed041`), dalam urutan seeding. Totalnya 15 entri Changelog (13 Create, 1 Edit, 1 Delete), memenuhi syarat lebih dari 10 entri pada TC-GS-POS-228:
  - Kelompok A (entri paling lama): Oleh Budi Santoso: Create 10 Position populasi `iOS Developer {runId}-041`, `Legal Counsel {runId}-041`, `Marketing Executive {runId}-041`, `Quality Assurance Analyst {runId}-041`, `Data Engineer {runId}-041`, `Office Administrator {runId}-041`, `Logistics Coordinator {runId}-041`, `Payroll Specialist {runId}-041`, `Security Officer {runId}-041`, dan `Training Coordinator {runId}-041`.
  - Kelompok B (entri paling baru): Oleh Budi Santoso: Create `IT Support Specialist {runId}-041`, Edit menjadi `IT Operations Lead {runId}-041`, Create `Temporary Staff {runId}-041`, Delete `Temporary Staff {runId}-041`; lalu oleh Sari Dewi (terakhir): Create `Procurement Analyst {runId}-041`.
  - Selisih Date (TC-GS-POS-221 sampai 224, precondition d): disediakan tim FE/BE, dua kelompok entri Changelog dengan Date berselisih minimal 1 menit, yaitu Date setiap entri Kelompok A paling sedikit 1 menit lebih lama daripada Date setiap entri Kelompok B (kolom Date berketelitian menit). Asersi Date atas kedua kelompok; urutan antar-entri di dalam satu kelompok tidak diasersi.
  - Entri Changelog bersifat audit trail permanen dan tidak dibersihkan.
- Precondition d TC-GS-POS-225 dan 226: seluruh entri Kelompok A dan B ber-Date hari ini dan memenuhi Search `Position` (kolom Field bernilai `Position Name`, sehingga setiap baris cocok). Entri seed memuat Action `Create`, `Delete`, dan `Edit` (TC-GS-POS-225: sedikitnya dua Action berbeda; TC-GS-POS-226: sedikitnya satu entri `Edit` dan sedikitnya satu entri bukan `Edit`). Selisih Date antar-kelompok di atas tidak boleh membuat Kelompok A berpindah ke hari sebelumnya.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-041` yang masih ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis: seeding lewat API dengan sesi Budi dan Sari; pembacaan urutan baris, indikator panah sort, chip filter, dan tanggal hari ini dalam format General Settings (Pre-setup 22); pembacaan ukuran halaman dan nomor halaman.
- State global: tidak ada yang diubah selain flag Guided Tooltip.

## Test Steps

### TC-GS-POS-228: Pagination Popup Changelog

1. Klik ikon Changelog
2. Verifikasi User > Position > Popup Changelog: Position terbuka
3. Amati jumlah baris halaman 1
4. Verifikasi halaman 1 menampilkan 10 entri
5. Catat baris pertama halaman 1
6. Klik next
7. Verifikasi halaman 2 menampilkan entri berikutnya (baris pertama berbeda dari yang dicatat)
8. Buka Overlay Page Size
9. Verifikasi opsi ukuran `10 | 25 | 50 | 100`
10. Pilih ukuran halaman 25
11. Ketik Search `{runId}-041`, tekan Enter

### TC-GS-POS-221: Sort Date, siklus 3 klik

12. Klik header Date
13. Verifikasi header Date menampilkan indikator Oldest First (↑)
14. Verifikasi baris terurut Date dari terlama di atas: seluruh baris Kelompok A berada di atas seluruh baris Kelompok B
15. Klik header Date
16. Verifikasi header Date menampilkan indikator Newest First (↓)
17. Verifikasi baris terurut Date dari terbaru di atas: seluruh baris Kelompok B berada di atas seluruh baris Kelompok A
18. Klik header Date
19. Verifikasi indikator sort pada header Date hilang
20. Verifikasi urutan baris kembali default Date terbaru di atas: seluruh baris Kelompok B berada di atas seluruh baris Kelompok A

### TC-GS-POS-222: Sort kelas alfabetis (Action, Position Name, Field)

21. Klik header Action
22. Verifikasi header Action menampilkan indikator ↑
23. Verifikasi baris terurut Action `Create`, lalu `Delete`, lalu `Edit`
24. Klik header Action
25. Verifikasi header Action menampilkan indikator ↓
26. Verifikasi baris terurut Action `Edit`, lalu `Delete`, lalu `Create`
27. Klik header Action
28. Verifikasi indikator sort pada header Action hilang
29. Verifikasi urutan baris kembali default Date terbaru di atas: seluruh baris Kelompok B di atas seluruh baris Kelompok A
30. Klik header Position Name
31. Verifikasi header Position Name menampilkan indikator ↑
32. Verifikasi baris terurut Position Name A-Z case-insensitive
33. Klik header Position Name
34. Verifikasi header Position Name menampilkan indikator ↓
35. Verifikasi baris terurut Position Name Z-A
36. Klik header Position Name
37. Verifikasi indikator sort pada header Position Name hilang
38. Verifikasi urutan baris kembali default Date terbaru di atas: seluruh baris Kelompok B di atas seluruh baris Kelompok A
39. Catat urutan baris default sebelum sort Field
40. Klik header Field
41. Verifikasi header Field menampilkan indikator ↑
42. Verifikasi urutan baris tidak berubah (semua nilai Field `Position Name`)
43. Klik header Field
44. Verifikasi header Field menampilkan indikator ↓
45. Verifikasi urutan baris tidak berubah
46. Klik header Field
47. Verifikasi indikator sort pada header Field netral
48. Verifikasi urutan baris tidak berubah

### TC-GS-POS-223: Sort kelas campuran (Old Value, New Value) dengan nilai kosong

49. Klik header Old Value
50. Verifikasi header Old Value menampilkan indikator ↑
51. Verifikasi baris Create (Old Value `—`) berada di akhir
52. Klik header Old Value
53. Verifikasi header Old Value menampilkan indikator ↓
54. Verifikasi baris Create (Old Value `—`) berada di awal
55. Klik header Old Value
56. Klik header New Value
57. Verifikasi header New Value menampilkan indikator ↑
58. Verifikasi baris Delete (New Value `—`) berada di akhir
59. Klik header New Value
60. Verifikasi header New Value menampilkan indikator ↓
61. Verifikasi baris Delete (New Value `—`) berada di awal
62. Klik header New Value

### TC-GS-POS-224: Sort Modified By berdasarkan nama lengkap

63. Klik header Modified By
64. Verifikasi header Modified By menampilkan indikator ↑
65. Verifikasi baris `Budi S` (Budi Santoso) berada sebelum baris `Sari D` (Sari Dewi)
66. Klik header Modified By
67. Verifikasi header Modified By menampilkan indikator ↓
68. Verifikasi baris `Sari D` (Sari Dewi) berada sebelum baris `Budi S` (Budi Santoso)
69. Klik header Modified By

### TC-GS-POS-225: Kombinasi Search, Filter, Sort, dan pagination

70. Klik `✕` pada Search, tekan Enter
71. Pilih ukuran halaman 10
72. Ketik Search `Position`, tekan Enter
73. Klik ikon Filter
74. Pilih rentang Date hari ini pada field `Date`
75. Klik `[Apply]`
76. Klik header Action
77. Pilih ukuran halaman 25
78. Verifikasi tabel memuat sedikitnya satu baris sebagai baris pembanding
79. Verifikasi setiap baris yang tampil mengandung `Position`
80. Verifikasi setiap baris yang tampil memiliki Date hari ini
81. Verifikasi baris terurut Action ↑
82. Verifikasi keyword Search `Position` tetap terisi
83. Verifikasi Filter Date hari ini tetap ter-apply: setiap baris yang tampil masih ber-Date hari ini

### TC-GS-POS-226: Clear Filter dan Clear Search saling independen

84. Klik `✕` pada Search, tekan Enter
85. Klik ikon Filter
86. Klik `[Clear Field]`
87. Klik `[Apply]`
88. Klik header Action
89. Klik header Action
90. Ketik Search `Position`, tekan Enter
91. Klik ikon Filter
92. Pilih `Edit` pada dropdown `Action`
93. Klik `[Apply]`
94. Klik header Date
95. Klik ikon Filter
96. Klik `[Clear Field]`
97. Klik `[Apply]`
98. Verifikasi keyword Search `Position` tetap terisi
99. Verifikasi header Date tetap menampilkan indikator ↑
100. Klik ikon Filter
101. Pilih `Edit` pada dropdown `Action`
102. Klik `[Apply]`
103. Klik `✕` pada Search, tekan Enter
104. Verifikasi tabel memuat sedikitnya satu baris dengan Action `Edit` sebagai baris pembanding
105. Verifikasi Filter `Edit` tetap ter-apply (setiap baris yang tampil dengan Action `Edit`)
106. Verifikasi header Date tetap menampilkan indikator ↑

### TC-GS-POS-227: Pemulihan empty state Popup Changelog

107. Klik ikon Filter
108. Klik `[Clear Field]`
109. Klik `[Apply]`
110. Klik header Date
111. Klik header Date
112. Klik ikon Filter
113. Pilih `Delete` pada dropdown `Action`
114. Klik `[Apply]`
115. Ketik Search `Astronaut`, tekan Enter
116. Verifikasi Illustration empty state tampil
117. Verifikasi Title "No results found"
118. Verifikasi Description "Try adjusting your search or filter."
119. Klik `←` pada Search
120. Verifikasi baris Delete kembali tampil
121. Klik ikon Filter
122. Klik `[Clear Field]`
123. Klik `[Apply]`
124. Tutup Popup Changelog dengan klik `✕` di header

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 228, 221, 222, 223, 224, 225, 226, 227. Urutan ini menyimpang dari urutan TC sumber: TC-GS-POS-228 membaca Popup pada ukuran halaman default 10 dan tanpa Search sehingga ditaruh pertama; sesudahnya ukuran halaman 25 dan Search `{runId}-041` dipakai agar seluruh 15 entri seed tampil dalam satu halaman dan urutan lintas Action (Create, Delete, Edit) teramati; TC-GS-POS-225 sampai 227 memakai Search, Filter, dan ukuran halaman yang diubah sehingga ditaruh sesudah TC sort murni.
- Popup Changelog dibuka sekali (langkah 1) dan ditutup sekali (langkah 124); tidak ada form yang dibuka.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 (mencatat pembanding halaman), 10 dan 11 (ukuran halaman 25 dan Search `{runId}-041` untuk mempersempit ke entri seed), 39 (mencatat urutan default), klik ketiga pada header Old Value, New Value, dan Modified By (langkah 55, 62, 69) untuk mereset sort, langkah 70 dan 71 (mengosongkan Search dan mengembalikan ukuran halaman 10 sebelum TC-GS-POS-225), langkah 84 sampai 89 (membersihkan Search, Filter, dan sort Action sebelum TC-GS-POS-226), langkah 107 sampai 111 (membersihkan Filter dan sort Date sebelum TC-GS-POS-227), dan langkah 121 sampai 124 (membersihkan Filter lalu menutup Popup).
- TC-GS-POS-221 sampai 224 dijalankan dengan Search `{runId}-041` aktif (langkah 11) agar asersi urutan hanya atas entri seed milik spec; TC sumber tidak memuat Search tersebut (lihat Temuan untuk QA).
- Asersi urutan memakai baris yang tampil pada halaman aktif; dengan ukuran halaman 25 dan 15 entri seed seluruh entri tampil pada halaman 1. Sort Date (langkah 14, 17, 20) dan kembali ke default Date (langkah 20, 29, 38) diasersi atas dua kelompok entri yang Date-nya berselisih minimal 1 menit (Prerequisites); urutan antar-entri dalam satu kelompok tidak diasersi karena kolom Date berketelitian menit.
- Asersi tambahan di luar Expected TC: langkah 78 dan 104 (baris pembanding yang mendahului asersi "setiap baris yang tampil" supaya tabel kosong tidak meloloskannya; konvensi 8b butir 2). Pembandingnya generik ("sedikitnya satu baris", "sedikitnya satu baris dengan Action `Edit`") karena baris spesifik tidak dijamin tampil oleh Search, sort, dan ukuran halaman yang dipakai.
- Langkah 83 mengasersi Filter Date tetap ter-apply lewat baris yang tampil (masih ber-Date hari ini), bukan lewat nilai rentang pada Filter Panel, karena TC tidak menyebut apakah Filter Panel tetap terbuka sesudah `[Apply]` (lihat Temuan untuk QA). Nilai rentang pada Filter Panel tidak diasersi.
- Topik satu dataset Changelog (screening 038, Search 039, Filter 040, Sort 041, Setup Column 042, Download 043) dipertahankan sebagai spec terpisah karena gabungan keenamnya melewati batas ukuran jauh dan tiap spec menyiapkan dan membersihkan seeding sendiri, sehingga kegagalan keras satu spec tidak menghilangkan makna spec lain.
- Spec melewati sekitar 35 langkah (124 langkah, sebagian besar pasangan klik header dan `Verifikasi` indikator serta urutan). Seluruhnya satu kelas (Sort, kombinasi Search/Filter/Sort, dan Pagination Popup Changelog pada dataset seed yang sama, satu akun, tanpa aksi yang mengubah data), dan tiap blok TC dimulai dari sort/filter yang dibersihkan sehingga tetap bermakna bila blok lain gagal.
- Search ditulis "Ketik Search `X`, tekan Enter" atomik (konvensi bagian 8b butir 9). Search Popup Changelog ada di spec 039; Filter dropdown dan chip ada di spec 040; Setup Column di spec 042; Download di spec 043.
- Temuan untuk QA:
  - TC-GS-POS-221 sampai 224 (precondition d) mensyaratkan dua entri Date berselisih minimal 1 menit tanpa menyebut cara membentuknya; spec menyatakannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-POS-225, 226, dan 227 tidak menyebut apakah Filter Panel Popup Changelog tertutup sesudah `[Apply]` (TC-GS-POS-160 sampai 170 untuk tabel utama menyatakan Filter Panel tetap terbuka; Popup Changelog tidak disebut); spec membuka Filter lagi dengan klik ikon Filter sebelum tiap pengisian.
  - TC-GS-POS-221 sampai 224 tidak menyebut Search atau cara mengisolasi entri seed dari Changelog kumulatif entitas; spec menambahkan Search `{runId}-041` sebagai langkah penghubung sehingga hanya 15 entri seed yang tampil. Tanpa itu asersi lintas Action tidak teramati pada halaman 1.
  - TC-GS-POS-222 Expected c menyebut indikator Field "↑ lalu ↓ lalu netral" tanpa menyebut apakah sort sisi server menjaga urutan stabil untuk nilai sama; spec mengasersi urutan tidak berubah.
  - TC-GS-POS-223 menyebut klik 2× tetapi tidak menyebut pemulihan sort sesudahnya; spec menambahkan klik ketiga sebagai langkah penghubung.
  - TC-GS-POS-224 mengasumsikan sort Modified By memakai nama lengkap (Budi Santoso, Sari Dewi); entri seed hanya memuat dua aktor tersebut.
  - TC-GS-POS-225 Expected tidak menyebut halaman aktif; spec mengasersi Search, Filter, dan sort sesudah ukuran halaman diubah.
  - TC-GS-POS-226 langkah 4 menulis "`✕` + Enter di Search" tanpa menyebut apakah Enter dibutuhkan setelah `✕`; spec mengikuti urutan itu.
  - TC-GS-POS-228 precondition e (">10 entri") tidak menyebut sumber entri tambahan; spec membuat 10 Position populasi lewat API sebagai pengganti TC-GS-POS-53 (pembuatan 10 Position) sehingga entri Changelog Create bertambah 10.

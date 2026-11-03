---
id: TC-AC-DS-E2E-018-role-matrix-visibilitas-elemen-per-role
title: "Role Matrix: Visibilitas Elemen Halaman Device SKU per Role Principal dan Distributor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-60
  - TC-AC-DS-61
  - TC-AC-DS-62
  - TC-AC-DS-63
  - TC-AC-DS-64
  - TC-AC-DS-65
  - TC-AC-DS-66
  - TC-AC-DS-67
  - TC-AC-DS-68
  - TC-AC-DS-69
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Halaman Device SKU per Role Principal dan Distributor

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (akun blok 1 login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun blok 2 sampai 10 diganti lewat langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite):

| Blok | TC | Role | Akun | Env var |
|---|---|---|---|---|
| 1 | TC-AC-DS-60 | Read Only Principal PT Arunika Prima (Pre-setup #3) | `readOnlySku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_RO_PASSWORD` |
| 2 | TC-AC-DS-61 | Create-Only Principal (Pre-setup #4) | `manageSkuC_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_C_PASSWORD` |
| 3 | TC-AC-DS-62 | Update-Only Principal (Pre-setup #5) | `manageSkuU_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_U_PASSWORD` |
| 4 | TC-AC-DS-63 | Delete-Only Principal (Pre-setup #6) | `manageSkuD_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_D_PASSWORD` |
| 5 | TC-AC-DS-64 | Total Control Principal (Default User, Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |
| 6 | TC-AC-DS-65 | Full CRUD non-Total Control Principal (Pre-setup #7) | `manageSkuCUD_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_CUD_PASSWORD` |
| 7 | TC-AC-DS-66 | Read Only Distributor PT Cakra Distribusi (Pre-setup #11) | `readOnlyDist_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_DIST_RO_PASSWORD` |
| 8 | TC-AC-DS-67 | Create-Only Distributor, Local Registration aktif (Pre-setup #12) | `manageSkuDistC_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_DIST_C_PASSWORD` |
| 9 | TC-AC-DS-68 | Update-Only Distributor (Pre-setup #13) | `manageSkuDistU_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_DIST_U_PASSWORD` |
| 10 | TC-AC-DS-69 | Delete-Only Distributor (Pre-setup #14) | `manageSkuDistD_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_DIST_D_PASSWORD` |

- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 (`HHR-ARC-100` dan `BLE-KIN-GW1`, `SFR-VEL-4P`, `SFR-ZERO-01` untuk blok 1) dan seed #30 (SKU Principal), SKU Distributor PT Cakra Distribusi #31 (`LOC-NOR-01`). "Baris SKU milik entitas aktor" untuk role Principal adalah `HHR-ARC-100`, untuk role Distributor adalah `LOC-NOR-01`; baris SKU Principal bagi role Distributor adalah `HHR-ARC-100`. Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Blok 1 mengubah visibilitas kolom `Model/Type` lewat overlay Column Visibility; spec memulihkannya pada langkah 23 dan hook `after` memulihkannya bila spec gagal di tengah. Tidak ada aksi tulis atas SKU: centang checkbox pada langkah Bulk Delete hanya dipakai untuk mengamati bar bulk lalu dihilangkan.
- Env var `AC_DS_RO_PASSWORD`, `AC_DS_C_PASSWORD`, `AC_DS_U_PASSWORD`, `AC_DS_D_PASSWORD`, `AC_DS_TC_PASSWORD`, `AC_DS_CUD_PASSWORD`, `AC_DS_DIST_RO_PASSWORD`, `AC_DS_DIST_C_PASSWORD`, `AC_DS_DIST_U_PASSWORD`, dan `AC_DS_DIST_D_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Tidak ada seeding.

## Test Steps

### Blok 1: Read Only Principal (TC-AC-DS-60)

1. Verifikasi Tab, List, Detail, Changelog, dan Download tampil (Show)
2. Verifikasi tombol `[+ SKU]` Hidden
3. Verifikasi kolom checkbox bulk Hidden
4. Klik ⋯ pada baris `HHR-ARC-100`
5. Verifikasi row action `Edit` Hidden
6. Verifikasi `Delete` dan Bulk Delete Hidden
7. Verifikasi menu ⋯ tampil dan memuat `Detail` saja
8. Tutup menu aksi
9. Klik nomor halaman 2 pada Pagination
10. Verifikasi halaman 2 dapat dibuka
11. Ketik Search `BLE-KIN`, tekan Enter
12. Verifikasi hanya baris `BLE-KIN-GW1` tampil
13. Klik `(←)` pada kotak Search
14. Klik ikon Filter
15. Pilih Brand `Veltrix` pada Filter Panel
16. Klik `[Apply]`
17. Verifikasi baris `SFR-VEL-4P` dan `SFR-ZERO-01` tampil
18. Klik header kolom SKU sekali
19. Verifikasi Sort Ascending dengan baris pertama `SFR-VEL-4P`
20. Klik header kolom Actions (⋯)
21. Hilangkan centang `Model/Type` pada overlay Column Visibility
22. Verifikasi kolom Model/Type tidak tampil di tabel
23. Centang kembali `Model/Type` lalu tutup overlay Column Visibility
24. Muat ulang halaman `Settings > Device > Device SKU`

### Blok 2: Create-Only Principal (TC-AC-DS-61)

25. Ganti akun: Logout dari akun Read Only Principal
26. Login sebagai Create-Only Principal `manageSkuC_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_C_PASSWORD`
27. Buka halaman `Settings > Device > Device SKU`
28. Verifikasi Tab, List, Detail, Changelog, dan Download tampil (Show)
29. Verifikasi tombol `[+ SKU]` Show
30. Verifikasi kolom checkbox bulk Hidden
31. Klik ⋯ pada baris `HHR-ARC-100`
32. Verifikasi row action `Edit` Hidden
33. Verifikasi `Delete` dan Bulk Delete Hidden
34. Verifikasi menu ⋯ tampil dan memuat `Detail` saja

### Blok 3: Update-Only Principal (TC-AC-DS-62)

35. Ganti akun: Logout dari akun Create-Only Principal
36. Login sebagai Update-Only Principal `manageSkuU_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_U_PASSWORD`
37. Buka halaman `Settings > Device > Device SKU`
38. Verifikasi Tab, List, Detail, Changelog, dan Download tampil (Show)
39. Verifikasi tombol `[+ SKU]` Hidden
40. Verifikasi kolom checkbox bulk Hidden
41. Klik ⋯ pada baris `HHR-ARC-100`
42. Verifikasi row action `Edit` Show
43. Verifikasi `Delete` dan Bulk Delete Hidden
44. Verifikasi menu ⋯ tampil dan memuat `Detail` dan `Edit`

### Blok 4: Delete-Only Principal (TC-AC-DS-63)

45. Ganti akun: Logout dari akun Update-Only Principal
46. Login sebagai Delete-Only Principal `manageSkuD_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_D_PASSWORD`
47. Buka halaman `Settings > Device > Device SKU`
48. Verifikasi Tab, List, Detail, Changelog, dan Download tampil (Show)
49. Verifikasi tombol `[+ SKU]` Hidden
50. Verifikasi kolom checkbox bulk Show
51. Klik ⋯ pada baris `HHR-ARC-100`
52. Verifikasi row action `Edit` Hidden
53. Verifikasi `Delete` Show dan enabled
54. Verifikasi menu ⋯ tampil dan memuat `Detail` dan `Delete`
55. Centang checkbox baris `HHR-ARC-100`
56. Verifikasi Bulk Delete Show dan enabled pada bar bulk
57. Hilangkan centang checkbox baris `HHR-ARC-100`

### Blok 5: Total Control Principal (TC-AC-DS-64)

58. Ganti akun: Logout dari akun Delete-Only Principal
59. Login sebagai Total Control Principal `totalControlSku_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_TC_PASSWORD`
60. Buka halaman `Settings > Device > Device SKU`
61. Verifikasi Tab, List, Detail, Changelog, dan Download tampil (Show)
62. Verifikasi tombol `[+ SKU]` Show
63. Verifikasi kolom checkbox bulk Show
64. Klik ⋯ pada baris `HHR-ARC-100`
65. Verifikasi row action `Edit` Show
66. Verifikasi `Delete` Show dan enabled
67. Verifikasi menu ⋯ tampil dan memuat `Detail`, `Edit`, dan `Delete`
68. Centang checkbox baris `HHR-ARC-100`
69. Verifikasi Bulk Delete Show dan enabled pada bar bulk
70. Hilangkan centang checkbox baris `HHR-ARC-100`

### Blok 6: Full CRUD non-Total Control Principal (TC-AC-DS-65)

71. Ganti akun: Logout dari akun Total Control Principal
72. Login sebagai Full CRUD non-Total Control Principal `manageSkuCUD_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_CUD_PASSWORD`
73. Buka halaman `Settings > Device > Device SKU`
74. Verifikasi Tab, List, Detail, Changelog, dan Download tampil (Show)
75. Verifikasi tombol `[+ SKU]` Show
76. Verifikasi kolom checkbox bulk Show
77. Klik ⋯ pada baris `HHR-ARC-100`
78. Verifikasi row action `Edit` Show
79. Verifikasi `Delete` Show dan enabled
80. Verifikasi menu ⋯ tampil dan memuat `Detail`, `Edit`, dan `Delete`
81. Centang checkbox baris `HHR-ARC-100`
82. Verifikasi Bulk Delete Show dan enabled pada bar bulk
83. Hilangkan centang checkbox baris `HHR-ARC-100`

### Blok 7: Read Only Distributor (TC-AC-DS-66)

84. Ganti akun: Logout dari akun Full CRUD non-Total Control Principal
85. Login sebagai Read Only Distributor `readOnlyDist_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_DIST_RO_PASSWORD`
86. Buka halaman `Settings > Device > Device SKU`
87. Verifikasi Tab, List, Detail, Changelog, dan Download tampil (Show)
88. Verifikasi tombol `[+ SKU]` Hidden
89. Verifikasi kolom checkbox bulk Hidden
90. Klik ⋯ pada baris `LOC-NOR-01`
91. Verifikasi row action `Edit` Hidden pada baris milik sendiri
92. Verifikasi `Delete` dan Bulk Delete Hidden
93. Verifikasi menu ⋯ baris milik sendiri tampil dan memuat `Detail` saja
94. Tutup menu aksi
95. Klik ⋯ pada baris `HHR-ARC-100`
96. Verifikasi menu ⋯ baris Principal tampil dan memuat `Detail` saja

### Blok 8: Create-Only Distributor (TC-AC-DS-67)

97. Ganti akun: Logout dari akun Read Only Distributor
98. Login sebagai Create-Only Distributor `manageSkuDistC_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_DIST_C_PASSWORD`
99. Buka halaman `Settings > Device > Device SKU`
100. Verifikasi Tab, List, Detail, Changelog, dan Download tampil (Show)
101. Verifikasi tombol `[+ SKU]` Show
102. Verifikasi kolom checkbox bulk Hidden
103. Klik ⋯ pada baris `LOC-NOR-01`
104. Verifikasi row action `Edit` Hidden
105. Verifikasi `Delete` dan Bulk Delete Hidden
106. Verifikasi menu ⋯ tampil dan memuat `Detail` saja

### Blok 9: Update-Only Distributor (TC-AC-DS-68)

107. Ganti akun: Logout dari akun Create-Only Distributor
108. Login sebagai Update-Only Distributor `manageSkuDistU_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_DIST_U_PASSWORD`
109. Buka halaman `Settings > Device > Device SKU`
110. Verifikasi Tab, List, Detail, Changelog, dan Download tampil (Show)
111. Verifikasi tombol `[+ SKU]` Hidden
112. Verifikasi kolom checkbox bulk Hidden
113. Klik ⋯ pada baris `LOC-NOR-01`
114. Verifikasi row action `Edit` Show pada SKU milik sendiri
115. Verifikasi `Delete` dan Bulk Delete Hidden
116. Verifikasi menu ⋯ baris milik sendiri tampil dan memuat `Detail` dan `Edit`
117. Tutup menu aksi
118. Klik ⋯ pada baris `HHR-ARC-100`
119. Verifikasi row action `Edit` Hidden pada SKU Principal
120. Verifikasi menu ⋯ baris Principal tampil dan memuat `Detail` saja

### Blok 10: Delete-Only Distributor (TC-AC-DS-69)

121. Ganti akun: Logout dari akun Update-Only Distributor
122. Login sebagai Delete-Only Distributor `manageSkuDistD_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_DIST_D_PASSWORD`
123. Buka halaman `Settings > Device > Device SKU`
124. Verifikasi Tab, List, Detail, Changelog, dan Download tampil (Show)
125. Verifikasi tombol `[+ SKU]` Hidden
126. Verifikasi checkbox bulk baris `LOC-NOR-01` Show dan enabled
127. Klik ⋯ pada baris `LOC-NOR-01`
128. Verifikasi row action `Edit` Hidden
129. Verifikasi `Delete` Show pada SKU milik sendiri
130. Verifikasi menu ⋯ baris milik sendiri tampil dan memuat `Detail` dan `Delete`
131. Tutup menu aksi
132. Centang checkbox baris `LOC-NOR-01`
133. Verifikasi Bulk Delete Show pada bar bulk untuk SKU milik sendiri
134. Hilangkan centang checkbox baris `LOC-NOR-01`
135. Klik ⋯ pada baris `HHR-ARC-100`
136. Verifikasi `Delete` Hidden pada SKU Principal
137. Verifikasi menu ⋯ baris Principal tampil dan memuat `Detail` saja
138. Tutup menu aksi
139. Hover checkbox baris `HHR-ARC-100`
140. Verifikasi checkbox baris `HHR-ARC-100` Disabled dengan tooltip "You don't have permission to do this."

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Spec ditulis per blok role karena langkah tiap role berbeda dan ganti akun menuntut Step eksplisit (akun blok 1 login di hook `before`, bagian 3a). Urutan blok mengikuti urutan TC-60 sampai TC-69.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 4, 31, 41, 51, 64, 77, 90, 95, 103, 113, 118, 127, 135 (membuka menu ⋯), 8, 94, 117, 131, 138 (menutup menu), 9, 11, 13 sampai 16, 18, 20, 21 (langkah TC-60 yang hasilnya diasersi pada langkah berikutnya), 23 dan 24 (memulihkan kolom Model/Type dan mereset List, S-09), 25 sampai 27, 35 sampai 37, 45 sampai 47, 58 sampai 60, 71 sampai 73, 84 sampai 86, 97 sampai 99, 107 sampai 109, 121 sampai 123 (ganti akun dan membuka halaman), 55, 57, 68, 70, 81, 83, 132, 134, 139 (mencentang dan menghilangkan centang, atau hover, untuk mengamati bar bulk atau tooltip).
- Langkah 55, 68, 81, dan 132 (mencentang satu baris) tidak ada di langkah TC-63 sampai TC-65 dan TC-69; langkah itu diperlukan agar Bulk Delete pada bar bulk dapat teramati (S-14). Expected TC-60 menyebut Search, Filter, Sort, Pagination, dan Column Visibility aktif; langkah 9 sampai 24 mengikuti langkah 4 sampai 9 TC-60 dan dipisah per klausa Expected g (halaman 2, Search, Filter, Sort, kolom).
- Spec melewati sekitar 35 langkah (140 langkah). Alasan pertahanan: seluruh blok memeriksa visibilitas elemen halaman yang sama per role (Role Matrix 3a, satu kelas, tanpa seeding dan tanpa mengubah data); tiap blok berdiri sendiri dan kegagalan satu blok role tidak membuat blok role lain kehilangan makna. Pola langkah tiap blok (ganti akun, buka halaman, asersi visibilitas) identik tetapi hasil asersi berbeda per role, sehingga setiap blok ditulis sendiri.
- Temuan untuk QA:
  - S-12: asersi memakai nama literal Pre-setup #29/#30/#31 (`HHR-ARC-100`, `LOC-NOR-01`, `BLE-KIN-GW1`, `SFR-VEL-4P`, `SFR-ZERO-01`) karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan).
  - Fixture rancangan: ketersediaan Pre-setup #3 sampai #7, #11 sampai #14, #29, #30, dan #31 di environment belum diverifikasi.
  - TC-60 sampai TC-69 tidak menyebut baris SKU tertentu untuk "baris SKU milik entitas aktor"; spec memakai `HHR-ARC-100` untuk Principal dan `LOC-NOR-01` untuk Distributor.
  - TC-63 dan TC-69 menyebut "blokir stok terjadi saat klik" untuk Delete; spec hanya mengasersi Delete tampil dan enabled, tanpa mengklik.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.

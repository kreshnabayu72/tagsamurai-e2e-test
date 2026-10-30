---
id: TC-GS-HHR-E2E-051-filter-multi-select-chip-dan-logika
title: "Filter Daftar Reader Handheld Reader: Screening Panel, Opsi DISTINCT, Multi-select OR, Antar Field AND, Chip, Indikator, dan Opsi Dinamis"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-239
  - TC-GS-HHR-240
  - TC-GS-HHR-241
  - TC-GS-HHR-242
  - TC-GS-HHR-250
  - TC-GS-HHR-251
  - TC-GS-HHR-252
  - TC-GS-HHR-253
  - TC-GS-HHR-254
  - TC-GS-HHR-255
  - TC-GS-HHR-256
  - TC-GS-HHR-257
  - TC-GS-HHR-258
  - TC-GS-HHR-259
  - TC-GS-HHR-456
coverage:
  web: automated
---

# Filter Daftar Reader Handheld Reader: Screening Panel, Opsi DISTINCT, Multi-select OR, Antar Field AND, Chip, Indikator, dan Opsi Dinamis

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor hook `before`: Total Control (Sari Dewi), Client A, `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Akun kedua (langkah 137, TC-GS-HHR-255): Total Control Client E, `totalControl_automated_{namaClient}@qwertysystem.net` dengan nama client Client E (Client E belum memiliki reader, entri Changelog, maupun Event Log; alokasi `Short Range` 2 dan `Long Range` 2), password `Spectra.env.GS_CLIENTE_TC_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` oleh pemilik suite). Hook `after` mengembalikan sesi ke akun default suite.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; spec tidak mengulang langkah buka di `## Test Steps` kecuali setelah ganti akun.
- Client A: plan Growth, toggle `Allow Self-Purchased Device Activation` aktif, alokasi `Short Range` 8 dan `Long Range` 6, format tanggal default General Settings `dd/MM/yy` 24-hour (tidak diubah spec ini).
- Data Dinamis Seed Reader A (10 reader DD-01 sampai DD-10), dibuat lewat fixture backend sebelum eksekusi (`Fixture.hardwareHandheldReader.seedReaderA`) dan dipulihkan antar TC oleh fixture backend. Nama literal tanpa suffix `{runId}` karena asersi bergantung pada nama, opsi dropdown DISTINCT, dan jumlah baris (lihat "Temuan untuk QA"). Jumlah baris awal N = 10 dan jumlah opsi diturunkan dari seeding ini. Baris dikenali lewat Serial Number:

| ID | Device Name | Serial Number | SKU | Range Type | Brand | Model/Type | Source | Last Scanned In | Last User | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| DD-01 | Zebra RFID Reader - 1 | SN-HHR-00101 | SKU-HHR-01 | Long Range | Zebra | RFD40 | Official | Fixed Asset | Budi S | Available |
| DD-02 | Gudang Reader - 1 | SN-HHR-00102 | SKU-HHR-03 | Short Range | Chainway | C66 | Official | Supply | Sari D | Available |
| DD-03 | Zebra Mobile Reader - 1 | SN-HHR-00103 | SKU-HHR-02 | Long Range | Zebra | MC3300R | Official | Global Settings | Sari D | Damaged |
| DD-04 | Gudang Reader - 2 | SN-HHR-00104 | SKU-HHR-03 | Short Range | Chainway | C66 | Official | — | — | Missing |
| DD-05 | Chainway C72 - 1 | SN-HHR-00105 | — | Long Range | Chainway | C72 | Self-Purchased | — | — | Waiting for Approval |
| DD-06 | Zebra RFID Reader - 1 | SN-HHR-00107 | SKU-HHR-04 | Short Range | Zebra | RFD40 | Official | Supply | Sari D | Available |
| DD-07 | Honeywell CK65 - 1 | SN-HHR-00108 | — | Long Range | Honeywell | CK65 | Self-Purchased | — | — | Available |
| DD-08 | Unitech EA520 - 1 | SN-HHR-00109 | — | Short Range | Unitech | — | Self-Purchased | — | — | Available |
| DD-09 | International Handheld Terminals Ltd Ultra-Rugged Series 7000 Pro Max - 1 | SN-HHR-00110 | — | Long Range | International Handheld Terminals Ltd | Ultra-Rugged Series 7000 Pro Max | Self-Purchased | — | — | Available |
| DD-10 | Gudang Reader - 4 | SN-HHR-00205 | SKU-HHR-03 | Short Range | Chainway | C66 | Official | — | — | Waiting for Approval |

- Kolom `Status` tampil pada keadaan awal (diperlukan langkah 105). Overlay Column Visibility dipulihkan ke bawaan oleh langkah 112 dan hook `after` cadangan.
- Model Filter Panel: panel dibuka dengan klik ikon Filter, tetap terbuka sesudah `[Apply]`, dan ditutup dengan klik ikon Filter; tiap blok TC membuka panel sendiri dan menutupnya di akhir blok (lihat "Temuan untuk QA").
- Tabel "Opsi dropdown TC-GS-HHR-240" (opsi tepat; hasil DISTINCT dari Seed Reader A):

| Field | Opsi yang diharapkan |
|---|---|
| Device Name | 9 opsi: `Chainway C72 - 1`, `Gudang Reader - 1`, `Gudang Reader - 2`, `Gudang Reader - 4`, `Honeywell CK65 - 1`, `International Handheld Terminals Ltd Ultra-Rugged Series 7000 Pro Max - 1`, `Unitech EA520 - 1`, `Zebra Mobile Reader - 1`, `Zebra RFID Reader - 1` (DD-01 dan DD-06 memakai nama yang sama, tampil satu kali) |
| SKU | 4 opsi `SKU-HHR-01`, `SKU-HHR-02`, `SKU-HHR-03`, `SKU-HHR-04`; tidak ada opsi `—` |
| Range Type | `Short Range`, `Long Range` |
| Brand | 5 opsi `Zebra`, `Chainway`, `Honeywell`, `Unitech`, `International Handheld Terminals Ltd` |
| Model/Type | 6 opsi `RFD40`, `C66`, `MC3300R`, `C72`, `CK65`, `Ultra-Rugged Series 7000 Pro Max` (DD-08 tanpa Model/Type tidak menjadi opsi) |
| Source | `Official`, `Self-Purchased` |
| Last Scanned In | `Fixed Asset`, `Global Settings`, `Supply` |
| Status | `Available`, `Damaged`, `Missing`, `Waiting for Approval` |
| Last User | 2 opsi nama lengkap `Budi Santoso`, `Sari Dewi` |

- Tabel "Pilihan TC-GS-HHR-241":

| Field | Opsi dipilih | Hasil |
|---|---|---|
| Status | `Damaged`, `Missing` | 2 baris DD-03, DD-04 |
| Source | `Self-Purchased` | 4 baris DD-05, DD-07, DD-08, DD-09 |
| Range Type | `Long Range` | 5 baris DD-01, DD-03, DD-05, DD-07, DD-09 |
| Brand | `Zebra`, `Honeywell` | 4 baris DD-01, DD-03, DD-06, DD-07 |
| Model/Type | `C72`, `CK65` | 2 baris DD-05, DD-07 |
| SKU | `SKU-HHR-01`, `SKU-HHR-04` | 2 baris DD-01, DD-06 |
| Device Name | `Gudang Reader - 1`, `Honeywell CK65 - 1` | 2 baris DD-02, DD-07 |
| Last Scanned In | `Fixed Asset`, `Supply` | 3 baris DD-01, DD-02, DD-06 |

- Tabel "Dua opsi TC-GS-HHR-251/252" (Opsi 1 dipilih lebih dulu, lalu Opsi 2):

| Field | Opsi 1 | Opsi 2 |
|---|---|---|
| Device Name | `Chainway C72 - 1` | `Gudang Reader - 1` |
| SKU | `SKU-HHR-01` | `SKU-HHR-02` |
| Range Type | `Short Range` | `Long Range` |
| Brand | `Zebra` | `Chainway` |
| Model/Type | `RFD40` | `C66` |
| Source | `Official` | `Self-Purchased` |
| Last Scanned In | `Fixed Asset` | `Global Settings` |
| Last User | `Budi Santoso` | `Sari Dewi` |
| Status | `Available` | `Damaged` |

- TC-GS-HHR-456 (langkah 113 sampai 125): simulator reader USB dengan Serial Number SN-HHR-00201 (HS-01: SKU-HHR-01 Zebra RFID Reader, Long Range, Zebra / RFD40, Current Power 22 dBm, stok Hardware Stock Principal berstatus `Available`) tersambung ke komputer desktop dan driver lokal terpasang; kemampuan simulator dan driver disediakan tim FE (mekanisme simulasi tidak didefinisikan di TC, PRD, atau LLD; lihat "Temuan untuk QA"). Kuota `Long Range` Client A 5 dari 6 sehingga satu aktivasi masih diizinkan. Reader baru `Zebra RFID Reader - 2` yang dibuat spec dan pemulihan stok SN-HHR-00201 ke `Available` dibersihkan hook `after` (disediakan tim FE/BE; tidak berasumsi aktivasi berhasil penuh).
- TC-GS-HHR-256 (langkah 127 sampai 135): sesi kedua Admin B memakai sesi API yang hanya memicu penghapusan reader DD-08; akun Admin B disediakan tim FE (tidak ada di Tabel Pre-setup TC). DD-08 dipulihkan oleh fixture backend sesudah spec.
- TC-GS-HHR-255 (langkah 138 sampai 148): kemampuan teknis menahan respons request pemuat opsi dropdown filter (intercept respons tertunda) lalu melepasnya; endpoint request opsi filter tidak tertulis di TC, PRD, atau LLD yang dirujuk spec ini sehingga tidak ditulis di sini (lihat "Temuan untuk QA"). Intercept dilepas pada langkah 145 sebelum asersi akhir.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` true untuk akun Total Control Client A dan hook `after` memulihkannya (lihat `suite.md`); untuk akun Client E flag diatur hook yang sama (disediakan tim FE).
- Suite serial (`parallel: false`): spec mengubah data (aktivasi reader baru pada TC-GS-HHR-456, penghapusan DD-08 pada TC-GS-HHR-256) dan visibilitas kolom (langkah 105 dan 112), dipulihkan seperti dinyatakan di atas.

## Test Steps

### TC-GS-HHR-239: Screening Filter Panel

1. Klik ikon Filter untuk membuka panel
2. Verifikasi ikon Filter berubah gelap
3. Verifikasi Filter Panel memuat 12 field, maksimal 4 per baris
4. Verifikasi field `Device Name` multi-select searchable dengan placeholder `All device names`
5. Verifikasi field `SKU` multi-select searchable dengan placeholder `All SKUs`
6. Verifikasi field `Range Type` multi-select searchable dengan placeholder `All range types`
7. Verifikasi field `Brand` multi-select searchable dengan placeholder `All brands`
8. Verifikasi field `Model/Type` multi-select searchable dengan placeholder `All models`
9. Verifikasi field `Source` multi-select searchable dengan placeholder `All sources`
10. Verifikasi field `Last Scanned In` multi-select searchable dengan placeholder `All products`
11. Verifikasi field `Last User` multi-select searchable dengan placeholder `All users`
12. Verifikasi field `Status` multi-select searchable dengan placeholder `All statuses`
13. Verifikasi field `Reader Power` berupa range dengan dua input placeholder `Min` dan `Max`
14. Verifikasi field `Last Scanned` berupa date range picker dengan placeholder `Select date`
15. Verifikasi field `Activated At` berupa date range picker dengan placeholder `Select date`
16. Verifikasi tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan) tampil
17. Verifikasi field `Alias Name`, `Serial Number`, dan kolom lain tanpa filter tidak ada di panel
18. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-240: Opsi dropdown DISTINCT dari data tabel saat ini

19. Klik ikon Filter untuk membuka panel
20. Buka dropdown `Device Name`
21. Verifikasi dropdown `Device Name` memuat 9 opsi sesuai tabel "Opsi dropdown TC-GS-HHR-240"
22. Verifikasi opsi `Zebra RFID Reader - 1` muncul satu kali
23. Tutup dropdown `Device Name`
24. Buka dropdown `<Field>` (diulang untuk setiap baris tabel "Opsi dropdown TC-GS-HHR-240" selain `Device Name`, langkah 24 sampai 26)
25. Verifikasi dropdown memuat opsi sesuai kolom "Opsi yang diharapkan" baris tabel yang sama
26. Tutup dropdown
27. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-241: Filter multi-select, dua opsi satu field digabung OR

28. Klik ikon Filter untuk membuka panel
29. Pilih opsi pada field `<Field>` sesuai tabel "Pilihan TC-GS-HHR-241" (diulang untuk setiap baris tabel, langkah 29 sampai 33)
30. Klik `[Apply]`
31. Verifikasi tabel menampilkan baris pada kolom Hasil baris tabel yang sama
32. Klik `[Clear Field]`
33. Klik `[Apply]`
34. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-242: Filter Last User

35. Klik ikon Filter untuk membuka panel
36. Pilih `Sari Dewi` pada field `Last User`
37. Klik `[Apply]`
38. Verifikasi tabel menampilkan 3 baris DD-02, DD-03, DD-06
39. Klik `[Clear Field]`
40. Klik `[Apply]`
41. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-250: Beberapa field berbeda digabung AND

42. Klik ikon Filter untuk membuka panel
43. Pilih `Available` pada field `Status`
44. Pilih `Long Range` pada field `Range Type`
45. Klik `[Apply]`
46. Verifikasi tabel menampilkan 3 baris DD-01, DD-07, DD-09
47. Klik `[Clear Field]`
48. Klik `[Apply]`
49. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-251: Hapus chip lewat X meng-uncheck opsi

50. Klik ikon Filter untuk membuka panel
51. Pilih Opsi 1 lalu Opsi 2 pada field `<Field>` sesuai tabel "Dua opsi TC-GS-HHR-251/252" (diulang untuk setiap baris tabel, langkah 51 sampai 57)
52. Klik `(✕)` pada chip pertama (Opsi 1)
53. Verifikasi chip Opsi 1 hilang dari field
54. Buka dropdown field
55. Verifikasi checkbox Opsi 1 ter-uncheck di dropdown
56. Tutup dropdown
57. Verifikasi chip Opsi 2 tetap ada pada field
58. Klik `[Clear Field]`
59. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-252: Uncheck di dropdown menghapus chip

60. Klik ikon Filter untuk membuka panel
61. Pilih Opsi 1 lalu Opsi 2 pada field `<Field>` sesuai tabel "Dua opsi TC-GS-HHR-251/252" (diulang untuk setiap baris tabel, langkah 61 sampai 66)
62. Buka dropdown field
63. Uncheck Opsi 1 di dropdown
64. Verifikasi chip Opsi 1 hilang dari field
65. Verifikasi chip Opsi 2 tetap ada pada field
66. Tutup dropdown
67. Klik `[Clear Field]`
68. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-253: Search di dalam dropdown filter

69. Klik ikon Filter untuk membuka panel
70. Buka dropdown `Device Name`
71. Ketik `gudang` pada kotak search dropdown
72. Verifikasi dropdown memuat 3 opsi `Gudang Reader - 1`, `Gudang Reader - 2`, `Gudang Reader - 4`
73. Ganti isi kotak search dropdown dengan `zzzz`
74. Verifikasi daftar opsi dropdown kosong
75. Tutup dropdown `Device Name`
76. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-254: Banyak chip diringkas menjadi chip +N more

77. Klik ikon Filter untuk membuka panel
78. Pilih semua 9 opsi pada field `Device Name`
79. Verifikasi chip tampil sebanyak yang muat pada lebar field dan sisanya satu chip `+N more` dengan N sama dengan jumlah chip tersembunyi
80. Verifikasi field tidak melebar keluar panel
81. Verifikasi field tidak digulir horizontal
82. Klik `[Clear Field]`
83. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-257: Menutup Filter Panel tanpa Apply membuang perubahan

84. Klik ikon Filter untuk membuka panel
85. Pilih `Missing` pada field `Status` tanpa menekan `[Apply]`
86. Klik area di luar panel
87. Klik ikon Filter lagi
88. Verifikasi panel terbuka kembali dengan field `Status` kosong
89. Verifikasi tabel tetap 10 baris
90. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-258: Titik indikator pada ikon Filter

91. Klik ikon Filter untuk membuka panel
92. Pilih `Missing` pada field `Status`
93. Klik `[Apply]`
94. Klik ikon Filter untuk menutup panel
95. Verifikasi titik indikator (tanpa angka) tampil pada ikon Filter
96. Klik ikon Filter untuk membuka panel
97. Klik `[Clear Field]`
98. Klik `[Apply]`
99. Klik ikon Filter untuk menutup panel
100. Verifikasi titik indikator hilang dari ikon Filter

### TC-GS-HHR-259: Filter pada kolom tersembunyi tetap tersedia dan persist

101. Klik ikon Filter untuk membuka panel
102. Pilih `Missing` pada field `Status`
103. Klik `[Apply]`
104. Klik ikon Filter untuk menutup panel
105. Sembunyikan kolom `Status` lewat Overlay Column Visibility
106. Klik ikon Filter untuk membuka panel
107. Verifikasi field `Status` tetap ada pada Filter Panel dengan nilai `Missing`
108. Verifikasi tabel tetap menampilkan 1 baris DD-04 meski kolom `Status` tersembunyi
109. Klik `[Clear Field]`
110. Klik `[Apply]`
111. Klik ikon Filter untuk menutup panel
112. Tampilkan kembali kolom `Status` lewat Overlay Column Visibility

### TC-GS-HHR-456: Opsi Device Name bertambah setelah aktivasi tanpa reload

113. Klik ikon Filter untuk membuka panel
114. Buka dropdown `Device Name`
115. Verifikasi dropdown `Device Name` memuat 9 opsi
116. Verifikasi opsi `Zebra RFID Reader - 2` tidak ada
117. Klik ikon Filter untuk menutup panel
118. Klik `[+ Activate Reader]`
119. Klik `Long Range` pada Overlay `Select Range Type`
120. Klik `[Sync]` (reader USB SN-HHR-00201)
121. Klik `[Submit]`
122. Klik ikon Filter untuk membuka panel
123. Buka dropdown `Device Name`
124. Verifikasi dropdown `Device Name` memuat 10 opsi tanpa reload halaman
125. Verifikasi opsi `Zebra RFID Reader - 2` ada di dropdown
126. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-256: Opsi filter aktif yang recordnya dihapus admin lain dibersihkan

127. Klik ikon Filter untuk membuka panel
128. Pilih `Unitech EA520 - 1` pada field `Device Name`
129. Klik `[Apply]`
130. Pada sesi kedua (Admin B lewat sesi API) hapus reader DD-08 (`Unitech EA520 - 1`) hingga tersimpan
131. Pada sesi pertama klik `[Apply]` lagi
132. Verifikasi tidak ada crash atau pesan error pada halaman
133. Verifikasi nilai `Unitech EA520 - 1` dibersihkan dari kriteria (field `Device Name` tanpa chip)
134. Verifikasi sedikitnya satu baris reader tampil pada tabel
135. Verifikasi baris `Unitech EA520 - 1` tidak ada di tabel
136. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-255: Dropdown filter menampilkan loading dan No options available (Client E)

137. Logout dari akun Total Control Client A (ganti akun)
138. Login sebagai Total Control Client E
139. Buka Global Settings > Hardware > Handheld Reader
140. Tahan respons request pemuat opsi filter (penundaan respons)
141. Klik ikon Filter untuk membuka panel
142. Buka dropdown `Status` selama request tertunda
143. Verifikasi dropdown `Status` menampilkan skeleton atau spinner
144. Tutup dropdown `Status`
145. Lepas penundaan respons
146. Buka dropdown `Status`
147. Verifikasi teks `No options available` tampil di dropdown `Status`
148. Verifikasi tidak ada pesan error
149. Klik ikon Filter untuk menutup panel

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 239, 240, 241, 242, 250, 251, 252, 253, 254, 257, 258, 259, lalu 456, 256, dan 255. Blok baca-saja dan blok yang hanya mengubah state Filter Panel lebih dulu; TC-GS-HHR-259 mengubah visibilitas kolom dan dipulihkan pada langkah 112; TC-GS-HHR-456 menambah satu reader dan TC-GS-HHR-256 menghapus DD-08 (aksi yang mengubah data) sehingga keduanya di akhir blok Client A, dengan 456 sebelum 256 supaya baseline 9 opsi pada 456 belum terpengaruh penghapusan DD-08; TC-GS-HHR-255 memakai akun Client E dan ditaruh paling akhir karena ada langkah ganti akun eksplisit. Urutan ini menyimpang dari urutan TC sumber.
- Langkah penghubung (aksi tanpa `Verifikasi`): klik ikon Filter yang membuka atau menutup panel, `[Clear Field]` lalu `[Apply]` sesudah asersi hasil, tutup dropdown, dan langkah 112. Bagian "Klik ikon Filter" pada awal tiap blok berpasangan dengan penutupan di akhir blok.
- Langkah yang diulang per baris tabel Prerequisites: langkah 24 sampai 26 (8 iterasi), 29 sampai 33 (8 iterasi), 51 sampai 57 (9 iterasi), dan 61 sampai 66 (9 iterasi). Tiap iterasi punya `Verifikasi` yang sama.
- P-2 (pemicu bukan objek uji): TC-GS-HHR-456 memakai Sync dan Submit aktivasi (simulator USB) hanya sebagai pemicu penambahan opsi `Device Name`; TC-GS-HHR-256 memakai sesi kedua Admin B lewat sesi API hanya sebagai pemicu penghapusan DD-08 sementara asersi dilakukan di sesi pertama. Intercept penundaan respons pada TC-GS-HHR-255 menahan respons hanya untuk mengamati state loading (bukan kelas b) dan dilepas pada langkah 145.
- Anchor absence: langkah "opsi `Zebra RFID Reader - 2` tidak ada" didahului `Verifikasi` 9 opsi lain yang tampil di dropdown yang sama; langkah 135 didahului `Verifikasi` sedikitnya satu baris reader tampil; daftar opsi kosong pada TC-GS-HHR-253 didahului `Verifikasi` 3 opsi hasil `gudang`; `Verifikasi` field `Status` kosong pada TC-GS-HHR-257 dan titik indikator hilang pada TC-GS-HHR-258 didahului elemen panel atau tabel yang sudah termuat.
- Tidak ada asersi tambahan di luar Expected TC selain `Verifikasi` "sedikitnya satu baris reader tampil" (anchor) pada langkah di atas. Pembagian TC lintas spec: Setup Column dan Overlay Column Visibility ada di spec 055; Filter rentang ada di spec 052; kombinasi Search, Filter, dan Sort ada di spec 054.
- Spec memuat 149 langkah nominal (sekitar 309 langkah dengan ekspansi blok ulang; di atas smell sekitar 35 langkah). Alasan: seluruhnya satu dataset dan satu permukaan (Filter Panel Daftar Reader, kelas fungsional) pada satu akun Client A; tiap blok TC membuka panel sendiri dan menutupnya, membersihkan filter sebelum blok berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok yang mengubah data (456, 256) ada di akhir bagian Client A dan blok ganti akun (255) paling akhir sehingga bagian sebelumnya tidak terpengaruh. Ekspansi besar berasal dari empat blok ulang per field (9 field multi-select).
- Temuan untuk QA:
  - TC-GS-HHR-241: judul menyebut "dua opsi dalam satu field", tetapi Data Uji dan Expected hanya satu opsi untuk `Source` (`Self-Purchased`) dan `Range Type` (`Long Range`); spec mengikuti Expected TC. Seluruh opsi kedua field itu (dua nilai) tidak dipilih bersamaan karena hasilnya akan seluruh 10 baris.
  - TC-GS-HHR-251 dan 252: Data Uji "Dua opsi pertama tiap field" tidak menyebut urutan opsi di dropdown; spec memakai pasangan opsi eksplisit di tabel Prerequisites.
  - TC-GS-HHR-239 sampai 259: TC tidak menyatakan keadaan Filter Panel sesudah `[Apply]` (tetap terbuka atau menutup); model "tetap terbuka, ditutup dengan klik ikon Filter" diambil dari TC-GS-HHR-258 (langkah 1 menutup panel setelah Apply) dan diterapkan sebagai langkah penghubung.
  - TC-GS-HHR-255: endpoint request opsi filter dan mekanisme "penundaan respons" tidak didefinisikan di TC, PRD, atau LLD yang dirujuk; kebutuhan ditulis sebagai kemampuan teknis tanpa mengarang endpoint (S-13). Akun Total Control Client E mengikuti pola email fixture `totalControl_automated_{namaClient}@qwertysystem.net`; nilai persis tidak tertulis di Pre-setup TC.
  - TC-GS-HHR-456: mekanisme simulasi reader USB (Sync) dan pembersihan reader hasil aktivasi tidak didefinisikan di TC, PRD, atau LLD; TC berlabel Manual Only (membaca reader USB fisik). TC tidak menyebut hasil `[Submit]` (toast atau tabel) sehingga tidak diasersi; Expected b "tanpa reload halaman" diasersi pada langkah 125 dengan tidak melakukan reload di antara langkah.
  - TC-GS-HHR-256: Manual Only karena dua sesi paralel; akun Admin B tidak ada di Tabel Pre-setup TC (disediakan tim FE). Expected b "hasil tabel mengikuti kriteria yang tersisa" tidak menyebut jumlah baris; spec mengasersi baris `Unitech EA520 - 1` tidak ada dengan anchor sedikitnya satu baris reader.
  - Seed Reader A bernama literal tanpa suffix `{runId}` karena asersi bergantung pada nama dan opsi DISTINCT; pemulihan antar TC oleh fixture backend disediakan tim FE/BE tanpa mekanisme yang ditulis di TC.
  - Post Condition semua TC di spec ini `-`; tidak ada yang diasersi.

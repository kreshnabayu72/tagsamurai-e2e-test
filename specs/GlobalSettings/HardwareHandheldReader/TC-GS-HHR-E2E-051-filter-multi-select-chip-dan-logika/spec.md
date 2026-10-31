---
id: TC-GS-HHR-E2E-051-filter-multi-select-chip-dan-logika
title: "Filter Daftar Reader Handheld Reader: Screening Panel, Opsi DISTINCT, Multi-select OR, Antar Field AND, Chip, dan Indikator"
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
  - TC-GS-HHR-257
  - TC-GS-HHR-258
  - TC-GS-HHR-259
coverage:
  web: automated
---

# Filter Daftar Reader Handheld Reader: Screening Panel, Opsi DISTINCT, Multi-select OR, Antar Field AND, Chip, dan Indikator

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor hook `before`: Total Control (Sari Dewi), Client A, `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; spec tidak mengulang langkah buka di `## Test Steps` kecuali setelah ganti akun.
- Client A: plan Growth, toggle `Allow Self-Purchased Device Activation` aktif, alokasi `Short Range` 8 dan `Long Range` 6, format tanggal default General Settings `dd/MM/yy` 24-hour (tidak diubah spec ini).
- Data Dinamis (Seed Reader A, dipulihkan fixture backend): 10 reader DD-01 sampai DD-10, dibuat lewat fixture backend sebelum eksekusi (`Fixture.hardwareHandheldReader.seedReaderA`) dan dipulihkan antar TC oleh fixture backend. Pengecualian S-12 Population Seed Reader A HHR: nama literal tanpa suffix `{runId}` karena asersi bergantung pada nama, opsi dropdown DISTINCT, dan jumlah baris. Jumlah baris awal N = 10 dan jumlah opsi diturunkan dari seeding ini. Baris dikenali lewat Serial Number:

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

- Kolom `Status` tampil pada keadaan awal (diperlukan langkah 107). Overlay Column Visibility dipulihkan ke bawaan oleh langkah 114 dan hook `after` cadangan.
- Model Filter Panel: panel dibuka dengan klik ikon Filter, tetap terbuka sesudah `[Apply]`, dan ditutup dengan klik ikon Filter; tiap blok TC membuka panel sendiri dan menutupnya di akhir blok.
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

- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` true untuk akun Total Control Client A dan hook `after` memulihkannya (lihat `suite.md`).
- Suite serial (`parallel: false`): spec mengubah visibilitas kolom (langkah 107 dan 114), dipulihkan seperti dinyatakan di atas.

## Test Steps

### TC-GS-HHR-239: Screening Filter Panel

1. Klik ikon Filter untuk membuka panel
2. Verifikasi ikon Filter berubah gelap
3. Verifikasi Filter Panel memuat 12 field
4. Verifikasi field tersusun maksimal 4 per baris
5. Verifikasi field `Device Name` multi-select searchable dengan placeholder `All device names`
6. Verifikasi field `SKU` multi-select searchable dengan placeholder `All SKUs`
7. Verifikasi field `Range Type` multi-select searchable dengan placeholder `All range types`
8. Verifikasi field `Brand` multi-select searchable dengan placeholder `All brands`
9. Verifikasi field `Model/Type` multi-select searchable dengan placeholder `All models`
10. Verifikasi field `Source` multi-select searchable dengan placeholder `All sources`
11. Verifikasi field `Last Scanned In` multi-select searchable dengan placeholder `All products`
12. Verifikasi field `Last User` multi-select searchable dengan placeholder `All users`
13. Verifikasi field `Status` multi-select searchable dengan placeholder `All statuses`
14. Verifikasi field `Reader Power` berupa range dengan dua input placeholder `Min` dan `Max`
15. Verifikasi field `Last Scanned` berupa date range picker dengan placeholder `Select date`
16. Verifikasi field `Activated At` berupa date range picker dengan placeholder `Select date`
17. Verifikasi tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan) tampil
18. Verifikasi field `Alias Name`, `Serial Number`, dan kolom lain tanpa filter tidak ada di panel
19. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-240: Opsi dropdown DISTINCT dari data tabel saat ini

20. Klik ikon Filter untuk membuka panel
21. Buka dropdown `Device Name`
22. Verifikasi dropdown `Device Name` memuat 9 opsi sesuai tabel "Opsi dropdown TC-GS-HHR-240"
23. Verifikasi opsi `Zebra RFID Reader - 1` muncul satu kali
24. Tutup dropdown `Device Name`
25. Buka dropdown `<Field>` (diulang untuk setiap baris tabel "Opsi dropdown TC-GS-HHR-240" selain `Device Name`, langkah 25 sampai 27)
26. Verifikasi dropdown memuat opsi sesuai kolom "Opsi yang diharapkan" baris tabel yang sama
27. Tutup dropdown
28. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-241: Filter multi-select, dua opsi satu field digabung OR

29. Klik ikon Filter untuk membuka panel
30. Pilih opsi pada field `<Field>` sesuai tabel "Pilihan TC-GS-HHR-241" (diulang untuk setiap baris tabel, langkah 30 sampai 34)
31. Klik `[Apply]`
32. Verifikasi tabel menampilkan baris pada kolom Hasil baris tabel yang sama
33. Klik `[Clear Field]`
34. Klik `[Apply]`
35. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-242: Filter Last User

36. Klik ikon Filter untuk membuka panel
37. Pilih `Sari Dewi` pada field `Last User`
38. Klik `[Apply]`
39. Verifikasi tabel menampilkan 3 baris DD-02, DD-03, DD-06
40. Klik `[Clear Field]`
41. Klik `[Apply]`
42. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-250: Beberapa field berbeda digabung AND

43. Klik ikon Filter untuk membuka panel
44. Pilih `Available` pada field `Status`
45. Pilih `Long Range` pada field `Range Type`
46. Klik `[Apply]`
47. Verifikasi tabel menampilkan 3 baris DD-01, DD-07, DD-09
48. Klik `[Clear Field]`
49. Klik `[Apply]`
50. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-251: Hapus chip lewat X meng-uncheck opsi

51. Klik ikon Filter untuk membuka panel
52. Pilih Opsi 1 lalu Opsi 2 pada field `<Field>` sesuai tabel "Dua opsi TC-GS-HHR-251/252" (diulang untuk setiap baris tabel, langkah 52 sampai 58)
53. Klik `(✕)` pada chip pertama (Opsi 1)
54. Verifikasi chip Opsi 1 hilang dari field
55. Buka dropdown field
56. Verifikasi checkbox Opsi 1 ter-uncheck di dropdown
57. Tutup dropdown
58. Verifikasi chip Opsi 2 tetap ada pada field
59. Klik `[Clear Field]`
60. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-252: Uncheck di dropdown menghapus chip

61. Klik ikon Filter untuk membuka panel
62. Pilih Opsi 1 lalu Opsi 2 pada field `<Field>` sesuai tabel "Dua opsi TC-GS-HHR-251/252" (diulang untuk setiap baris tabel, langkah 62 sampai 67)
63. Buka dropdown field
64. Uncheck Opsi 1 di dropdown
65. Verifikasi chip Opsi 1 hilang dari field
66. Verifikasi chip Opsi 2 tetap ada pada field
67. Tutup dropdown
68. Klik `[Clear Field]`
69. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-253: Search di dalam dropdown filter

70. Klik ikon Filter untuk membuka panel
71. Buka dropdown `Device Name`
72. Ketik `gudang` pada kotak search dropdown
73. Verifikasi dropdown memuat 3 opsi `Gudang Reader - 1`, `Gudang Reader - 2`, `Gudang Reader - 4`
74. Ganti isi kotak search dropdown dengan `zzzz`
75. Verifikasi daftar opsi dropdown kosong
76. Tutup dropdown `Device Name`
77. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-254: Banyak chip diringkas menjadi chip +N more

78. Klik ikon Filter untuk membuka panel
79. Pilih semua 9 opsi pada field `Device Name`
80. Verifikasi chip tampil sebanyak yang muat pada lebar field
81. Verifikasi sisanya diringkas menjadi satu chip `+N more` dengan N sama dengan jumlah chip tersembunyi
82. Verifikasi field tidak melebar keluar panel
83. Verifikasi field tidak digulir horizontal
84. Klik `[Clear Field]`
85. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-257: Menutup Filter Panel tanpa Apply membuang perubahan

86. Klik ikon Filter untuk membuka panel
87. Pilih `Missing` pada field `Status` tanpa menekan `[Apply]`
88. Klik area di luar panel
89. Klik ikon Filter lagi
90. Verifikasi panel terbuka kembali dengan field `Status` kosong
91. Verifikasi tabel tetap 10 baris
92. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-258: Titik indikator pada ikon Filter

93. Klik ikon Filter untuk membuka panel
94. Pilih `Missing` pada field `Status`
95. Klik `[Apply]`
96. Klik ikon Filter untuk menutup panel
97. Verifikasi titik indikator (tanpa angka) tampil pada ikon Filter
98. Klik ikon Filter untuk membuka panel
99. Klik `[Clear Field]`
100. Klik `[Apply]`
101. Klik ikon Filter untuk menutup panel
102. Verifikasi titik indikator hilang dari ikon Filter

### TC-GS-HHR-259: Filter pada kolom tersembunyi tetap tersedia dan persist

103. Klik ikon Filter untuk membuka panel
104. Pilih `Missing` pada field `Status`
105. Klik `[Apply]`
106. Klik ikon Filter untuk menutup panel
107. Sembunyikan kolom `Status` lewat Overlay Column Visibility
108. Klik ikon Filter untuk membuka panel
109. Verifikasi field `Status` tetap ada pada Filter Panel dengan nilai `Missing`
110. Verifikasi tabel tetap menampilkan 1 baris DD-04 meski kolom `Status` tersembunyi
111. Klik `[Clear Field]`
112. Klik `[Apply]`
113. Klik ikon Filter untuk menutup panel
114. Tampilkan kembali kolom `Status` lewat Overlay Column Visibility

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti urutan TC sumber: 239, 240, 241, 242, 250, 251, 252, 253, 254, 257, 258, lalu 259. Blok baca-saja dan blok yang hanya mengubah state Filter Panel lebih dulu; TC-GS-HHR-259 mengubah visibilitas kolom dan dipulihkan pada langkah 114 sehingga ditaruh paling akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): klik ikon Filter yang membuka atau menutup panel, `[Clear Field]` lalu `[Apply]` sesudah asersi hasil, tutup dropdown, dan langkah 114. Bagian "Klik ikon Filter" pada awal tiap blok berpasangan dengan penutupan di akhir blok.
- Langkah yang diulang per baris tabel Prerequisites: langkah 25 sampai 27 (8 iterasi), 30 sampai 34 (8 iterasi), 52 sampai 58 (9 iterasi), dan 62 sampai 67 (9 iterasi). Tiap iterasi punya `Verifikasi` yang sama.
- Anchor absence: daftar opsi kosong pada TC-GS-HHR-253 didahului `Verifikasi` 3 opsi hasil `gudang`; `Verifikasi` field `Status` kosong pada TC-GS-HHR-257 dan titik indikator hilang pada TC-GS-HHR-258 didahului elemen panel atau tabel yang sudah termuat.
- Tidak ada asersi tambahan di luar Expected TC. Pembagian TC lintas spec: TC-GS-HHR-255, 256, dan 456 (opsi dropdown filter dinamis dan perubahan data live) ada di spec 078; Setup Column dan Overlay Column Visibility ada di spec 055; Filter rentang ada di spec 052; kombinasi Search, Filter, dan Sort ada di spec 054.
- Spec memuat 114 langkah nominal (sekitar 274 langkah dengan ekspansi blok ulang; di atas smell sekitar 35 langkah). Alasan: seluruhnya satu dataset dan satu permukaan (Filter Panel Daftar Reader, kelas fungsional) pada satu akun Client A, tanpa aksi yang mengubah data reader; tiap blok TC membuka panel sendiri dan menutupnya, membersihkan filter sebelum blok berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Ekspansi besar berasal dari empat blok ulang per field (9 field multi-select).
- Pengecualian S-12 Population Seed Reader A HHR dipakai untuk Seed Reader A (nama literal tanpa suffix `{runId}`); suite berjalan serial dan pemulihan lewat fixture backend dinyatakan di Prerequisites dan `suite.md`.
- Temuan untuk QA:
  - TC-GS-HHR-241: judul menyebut "dua opsi dalam satu field", tetapi Data Uji dan Expected hanya satu opsi untuk `Source` (`Self-Purchased`) dan `Range Type` (`Long Range`); spec mengikuti Expected TC. Seluruh opsi kedua field itu (dua nilai) tidak dipilih bersamaan karena hasilnya akan seluruh 10 baris.
  - TC-GS-HHR-251 dan 252: Data Uji "Dua opsi pertama tiap field" tidak menyebut urutan opsi di dropdown; spec memakai pasangan opsi eksplisit di tabel Prerequisites.
  - Seed Reader A bernama literal tanpa suffix `{runId}` karena asersi bergantung pada nama dan opsi DISTINCT; pemulihan antar TC oleh fixture backend disediakan tim FE/BE tanpa mekanisme yang ditulis di TC.
  - Post Condition semua TC di spec ini `-`; tidak ada yang diasersi.

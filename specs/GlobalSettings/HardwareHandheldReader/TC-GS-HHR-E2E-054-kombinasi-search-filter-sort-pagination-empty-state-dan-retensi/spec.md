---
id: TC-GS-HHR-E2E-054-kombinasi-search-filter-sort-pagination-empty-state-dan-retensi
title: "Kombinasi Search, Filter, Sort, dan Pagination Daftar Reader Handheld Reader: Irisan, Clear, Empty State, Reset Filters, dan Retensi State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-18
  - TC-GS-HHR-19
  - TC-GS-HHR-260
  - TC-GS-HHR-261
  - TC-GS-HHR-262
  - TC-GS-HHR-263
  - TC-GS-HHR-264
  - TC-GS-HHR-265
  - TC-GS-HHR-266
  - TC-GS-HHR-267
  - TC-GS-HHR-268
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, dan Pagination Daftar Reader Handheld Reader: Irisan, Clear, Empty State, Reset Filters, dan Retensi State

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor hook `before`: Total Control (Sari Dewi), Client A, `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Akun kedua (langkah 130, TC-GS-HHR-267): Total Control Client L, `totalControl_automated_{namaClient}@qwertysystem.net` dengan nama client Client L, password `Spectra.env.GS_CLIENTL_TC_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` oleh pemilik suite). Client L memiliki 26 reader `Large Reader - 1` sampai `Large Reader - 26`; seluruhnya berjenis `Short Range` supaya Filter `Range Type` = `Short Range` tetap memuat 26 baris dan halaman terakhir pada `Rows per page` 25 adalah halaman 2 (kondisi data disediakan tim FE; lihat "Temuan untuk QA"). Hook `after` mengembalikan sesi ke akun default suite.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; spec tidak mengulang langkah buka di `## Test Steps` kecuali setelah ganti akun. Klik item sidebar `Handheld Reader` mereset Search, Sort, dan Filter; state yang harus dipulihkan ditulis sebagai langkah penghubung eksplisit.
- Client A: plan Growth, format tanggal default General Settings `dd/MM/yy` 24-hour (tidak diubah spec ini).
- Data Dinamis Seed Reader A (10 reader DD-01 sampai DD-10, jumlah baris N = 10 dari seeding), dibuat lewat fixture backend sebelum eksekusi (`Fixture.hardwareHandheldReader.seedReaderA`) dan dipulihkan antar TC oleh fixture backend. Nama literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah baris (lihat "Temuan untuk QA"). Spec hanya membaca daftar. Kolom yang dicocokkan Search dan dipakai Filter dan Sort (data memuat sedikitnya dua nilai distinct pada kolom `Device Name`, `Serial Number`, `Status`, dan `Source`):

| ID | Device Name | Serial Number | Range Type | Source | Status |
|---|---|---|---|---|---|
| DD-01 | Zebra RFID Reader - 1 | SN-HHR-00101 | Long Range | Official | Available |
| DD-02 | Gudang Reader - 1 | SN-HHR-00102 | Short Range | Official | Available |
| DD-03 | Zebra Mobile Reader - 1 | SN-HHR-00103 | Long Range | Official | Damaged |
| DD-04 | Gudang Reader - 2 | SN-HHR-00104 | Short Range | Official | Missing |
| DD-05 | Chainway C72 - 1 | SN-HHR-00105 | Long Range | Self-Purchased | Waiting for Approval |
| DD-06 | Zebra RFID Reader - 1 | SN-HHR-00107 | Short Range | Official | Available |
| DD-07 | Honeywell CK65 - 1 | SN-HHR-00108 | Long Range | Self-Purchased | Available |
| DD-08 | Unitech EA520 - 1 | SN-HHR-00109 | Short Range | Self-Purchased | Available |
| DD-09 | International Handheld Terminals Ltd Ultra-Rugged Series 7000 Pro Max - 1 | SN-HHR-00110 | Long Range | Self-Purchased | Available |
| DD-10 | Gudang Reader - 4 | SN-HHR-00205 | Short Range | Official | Waiting for Approval |

- Model Filter Panel: panel dibuka dengan klik ikon Filter, tetap terbuka sesudah `[Apply]`, dan ditutup dengan klik ikon Filter; tiap pembukaan panel berpasangan dengan penutupan (lihat "Temuan untuk QA").
- Kemampuan teknis: pembacaan keyword Search, indikator sort, chip Filter, indikator Filter, `Rows per page`, halaman aktif, dan teks pagination; muat ulang halaman dengan F5; klik item sidebar.
- State yang diubah spec: `Rows per page` diubah ke 25 (blok TC-GS-HHR-262 dan 267) dan dikembalikan ke 10 pada langkah 62; Search, Filter, dan Sort dipulihkan lewat langkah penghubung di akhir tiap blok.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` true untuk akun Total Control Client A dan hook `after` memulihkannya (lihat `suite.md`); untuk akun Client L flag diatur hook yang sama (disediakan tim FE).

## Test Steps

### TC-GS-HHR-18: Empty state saat Search tidak menemukan reader

1. Ketik Search `zzzz`, tekan Enter
2. Verifikasi ilustrasi empty state tampil
3. Verifikasi judul `No results found`
4. Verifikasi deskripsi `Try adjusting your search or filter.`
5. Verifikasi tombol `[Reset Filters]` tampil
6. Klik ikon `(←)` pada search box

### TC-GS-HHR-19: Reset Filters mengosongkan Search dan seluruh Filter

7. Ketik Search `zzzz`, tekan Enter
8. Klik ikon Filter untuk membuka panel
9. Pilih `Available` pada field `Status`
10. Klik `[Apply]`
11. Klik ikon Filter untuk menutup panel
12. Verifikasi empty state `No results found` tampil
13. Verifikasi tombol `[Reset Filters]` tampil
14. Klik `[Reset Filters]`
15. Verifikasi kolom Search kosong
16. Verifikasi kolom Search tertutup
17. Verifikasi indikator Filter hilang
18. Klik ikon Filter untuk membuka panel
19. Verifikasi tidak ada chip Filter pada panel
20. Klik ikon Filter untuk menutup panel
21. Verifikasi tabel menampilkan 10 baris Seed Reader A pada halaman 1
22. Verifikasi teks pagination `Showing 1 - 10 of 10 readers`

### TC-GS-HHR-260: Search lalu Filter menghasilkan irisan

23. Ketik Search `Gudang`, tekan Enter
24. Klik ikon Filter untuk membuka panel
25. Pilih `Available` pada field `Status`
26. Klik `[Apply]`
27. Klik ikon Filter untuk menutup panel
28. Verifikasi tabel menampilkan 1 baris DD-02 (`Gudang Reader - 1`)
29. Verifikasi keyword Search `Gudang` tidak tereset oleh Apply
30. Klik ikon `(←)` pada search box
31. Klik ikon Filter untuk membuka panel
32. Klik `[Clear Field]`
33. Klik `[Apply]`
34. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-261: Filter lalu Search menghasilkan irisan yang sama

35. Klik ikon Filter untuk membuka panel
36. Pilih `Available` pada field `Status`
37. Klik `[Apply]`
38. Klik ikon Filter untuk menutup panel
39. Ketik Search `Gudang`, tekan Enter
40. Verifikasi tabel menampilkan 1 baris DD-02 (`Gudang Reader - 1`), identik dengan urutan Search lalu Filter
41. Klik ikon `(←)` pada search box
42. Klik ikon Filter untuk membuka panel
43. Klik `[Clear Field]`
44. Klik `[Apply]`
45. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-262: Kombinasi Search, Filter, Sort, dan Pagination aktif bersamaan

46. Ketik Search `reader`, tekan Enter
47. Klik ikon Filter untuk membuka panel
48. Pilih `Available` dan `Damaged` pada field `Status`
49. Klik `[Apply]`
50. Klik ikon Filter untuk menutup panel
51. Klik header `Device Name` dua kali (Descending)
52. Ubah `Rows per page` menjadi 25
53. Verifikasi tabel menampilkan 4 baris berurutan: `Zebra RFID Reader - 1` (DD-01), `Zebra RFID Reader - 1` (DD-06, tie-breaker `Serial Number` tetap Ascending), `Zebra Mobile Reader - 1` (DD-03), lalu `Gudang Reader - 1` (DD-02)
54. Verifikasi teks pagination `Showing 1 - 4 of 4 readers`
55. Verifikasi keyword Search `reader` tidak berubah saat page size diubah
56. Verifikasi sort `Device Name` Descending tidak berubah saat page size diubah
57. Klik ikon Filter untuk membuka panel
58. Verifikasi filter `Status` `Available` dan `Damaged` tidak berubah saat page size diubah
59. Klik `[Clear Field]`
60. Klik `[Apply]`
61. Klik ikon Filter untuk menutup panel
62. Ubah `Rows per page` kembali menjadi 10
63. Klik header `Device Name` kali ketiga
64. Klik ikon `(←)` pada search box

### TC-GS-HHR-263: Clear Filter saat Search dan Sort aktif

65. Ketik Search `Gudang`, tekan Enter
66. Klik header `Device Name` dua kali (Descending)
67. Klik ikon Filter untuk membuka panel
68. Pilih `Missing` pada field `Status`
69. Klik `[Apply]`
70. Klik `[Clear Field]`
71. Klik `[Apply]`
72. Klik ikon Filter untuk menutup panel
73. Verifikasi tabel menampilkan 3 baris dari keyword `Gudang`
74. Verifikasi urutan Device Name Descending: `Gudang Reader - 4`, `Gudang Reader - 2`, `Gudang Reader - 1`
75. Klik header `Device Name` kali ketiga
76. Klik ikon `(←)` pada search box

### TC-GS-HHR-264: Clear Search saat Filter dan Sort aktif

77. Ketik Search `Gudang`, tekan Enter
78. Klik ikon Filter untuk membuka panel
79. Pilih `Available` pada field `Status`
80. Klik `[Apply]`
81. Klik ikon Filter untuk menutup panel
82. Klik header `Device Name` dua kali (Descending)
83. Klik ikon `(✕)` pada search box, tekan Enter
84. Verifikasi tabel menampilkan 6 baris Status `Available`
85. Verifikasi urutan baris Device Name Descending
86. Verifikasi indikator sort `Device Name` Descending tetap aktif
87. Klik ikon Filter untuk membuka panel
88. Verifikasi filter `Status` `Available` tetap aktif
89. Klik `[Clear Field]`
90. Klik `[Apply]`
91. Klik ikon Filter untuk menutup panel
92. Klik header `Device Name` kali ketiga
93. Klik ikon `(←)` pada search box

### TC-GS-HHR-265: Berganti kolom sort tidak mereset Search dan Filter

94. Ketik Search `Gudang`, tekan Enter
95. Klik ikon Filter untuk membuka panel
96. Pilih `Official` pada field `Source`
97. Klik `[Apply]`
98. Klik ikon Filter untuk menutup panel
99. Klik header `Device Name`
100. Klik header `Serial Number`
101. Verifikasi indikator sort `Device Name` kembali netral
102. Verifikasi indikator sort `Serial Number` Ascending
103. Verifikasi tabel menampilkan 3 baris keyword `Gudang` Source `Official` berurutan Serial Number: `SN-HHR-00102`, `SN-HHR-00104`, `SN-HHR-00205`
104. Klik header `Serial Number` dua kali lagi (kembali netral)
105. Klik ikon `(←)` pada search box
106. Klik ikon Filter untuk membuka panel
107. Klik `[Clear Field]`
108. Klik `[Apply]`
109. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-266: Pemulihan dari empty state setelah melepas salah satu kontrol

110. Ketik Search `Honeywell`, tekan Enter
111. Klik ikon Filter untuk membuka panel
112. Pilih `Missing` pada field `Status`
113. Klik `[Apply]`
114. Klik ikon Filter untuk menutup panel
115. Verifikasi empty state `No results found` tampil (kombinasi `Honeywell` dan `Missing`)
116. Klik ikon `(✕)` pada search box, tekan Enter
117. Verifikasi tabel pulih menampilkan 1 baris DD-04 (`Status` `Missing`)
118. Klik ikon `(←)` pada search box
119. Klik ikon Filter untuk membuka panel
120. Klik `[Clear Field]`
121. Klik `[Apply]`
122. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-268: Klik ulang menu Handheld Reader dari sidebar mereset state

123. Ketik Search `Gudang`, tekan Enter
124. Klik header `Serial Number`
125. Klik item `Handheld Reader` pada sidebar
126. Verifikasi Search kosong
127. Verifikasi sort kembali Device Name A-Z
128. Verifikasi filter kosong (indikator Filter tidak tampil)
129. Verifikasi tabel menampilkan 10 baris

### TC-GS-HHR-267: Refresh F5 mempertahankan Search, Sort, Filter, halaman, dan Rows per page (Client L)

130. Logout dari akun Total Control Client A (ganti akun)
131. Login sebagai Total Control Client L
132. Buka Global Settings > Hardware > Handheld Reader
133. Ketik Search `Reader`, tekan Enter
134. Klik header `Serial Number`
135. Klik ikon Filter untuk membuka panel
136. Pilih `Short Range` pada field `Range Type`
137. Klik `[Apply]`
138. Klik ikon Filter untuk menutup panel
139. Ubah `Rows per page` menjadi 25
140. Buka halaman terakhir pada Pagination
141. Muat ulang halaman dengan F5
142. Verifikasi keyword Search `Reader` tetap sama
143. Verifikasi sort `Serial Number` Ascending tetap sama
144. Klik ikon Filter untuk membuka panel
145. Verifikasi filter `Range Type` `Short Range` tetap sama
146. Klik ikon Filter untuk menutup panel
147. Verifikasi `Rows per page` 25 tetap sama
148. Verifikasi halaman aktif tetap halaman terakhir
149. Klik item `Handheld Reader` pada sidebar

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 18, 19, 260, 261, 262, 263, 264, 265, 266, 268, lalu 267. Blok Client A lebih dulu; TC-GS-HHR-267 memakai akun Client L dan ditaruh paling akhir karena ada langkah ganti akun eksplisit (langkah 130); bagian sesudah ganti akun tetap bermakna walau blok sebelumnya gagal. TC-GS-HHR-268 mereset state lewat klik sidebar sehingga ditaruh sesudah blok yang memakai state. Urutan ini menyimpang dari urutan TC sumber.
- Langkah penghubung (aksi tanpa `Verifikasi`): klik ikon Filter yang membuka atau menutup panel, `[Clear Field]` lalu `[Apply]` di akhir tiap blok, klik ketiga header `Device Name` atau dua klik lagi pada header `Serial Number` untuk mengembalikan sort ke netral, klik ikon `(←)` yang menutup input Search, langkah 62 (mengembalikan `Rows per page` ke 10), dan klik sidebar di akhir TC-GS-HHR-267.
- Anchor asersi absence dan universal: `Verifikasi` empty state `No results found` pada TC-GS-HHR-19 dan 266 adalah anchor positif Search atau Filter; `Verifikasi` indikator Filter hilang dan tidak ada chip Filter (TC-GS-HHR-19) didahului `Verifikasi` tombol `[Reset Filters]` dan empty state yang membuktikan halaman termuat dan panel dapat dibuka; `Verifikasi` "6 baris Status `Available`" (TC-GS-HHR-264) mendahului `Verifikasi` urutan Descending.
- Pengecualian TC-GS-HHR-268: Expected menyebut "filter kosong", sedangkan langkah TC tidak menerapkan Filter sebelum klik sidebar; spec mengikuti TC dan mengasersi indikator Filter tidak tampil (lihat "Temuan untuk QA").
- Pembagian TC lintas spec: Search per kelas kolom ada di spec 050, Filter multi-select ada di spec 051, Filter rentang di spec 052, Sort per kolom di spec 053, Pagination tabel utama (ukuran halaman dan navigasi halaman) di spec 060.
- Spec memuat 149 langkah (di atas smell sekitar 35 langkah, tanpa ekspansi). Alasan: seluruhnya satu kelas harness (kombinasi Search, Filter, Sort, dan Pagination daftar reader yang berbagi dataset yang sama), tanpa aksi yang mengubah data; tiap blok TC membersihkan state-nya sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; blok Client L (TC-GS-HHR-267) memakai langkah ganti akun eksplisit dan tetap bermakna walau bagian Client A gagal.
- Temuan untuk QA:
  - TC-GS-HHR-267: precondition hanya menyebut "Client L memiliki 26 reader" tanpa menyebut `Range Type` reader; agar Filter `Short Range` dan `Rows per page` 25 menghasilkan halaman terakhir (halaman 2), seluruh 26 reader harus `Short Range`. Spec menulis kondisi itu sebagai kebutuhan data yang disediakan tim FE. Email akun Total Control Client L mengikuti pola fixture `totalControl_automated_{namaClient}@qwertysystem.net`; nilai persis tidak tertulis di Pre-setup TC.
  - TC-GS-HHR-260 sampai 266 dan 268: TC tidak menyatakan keadaan Filter Panel sesudah `[Apply]` (tetap terbuka atau menutup); model "tetap terbuka, ditutup dengan klik ikon Filter" diambil dari TC-GS-HHR-258 dan diterapkan sebagai langkah penghubung.
  - TC-GS-HHR-268: Expected menyebut "filter kosong", tetapi langkah TC tidak menerapkan Filter; asersi filter kosong tidak membedakan keadaan sebelum dan sesudah klik sidebar.
  - TC-GS-HHR-264: Data Uji menulis `Gudang` untuk Search, tetapi Expected menyebut 6 baris `Available` sesudah Search dikosongkan; spec mengikuti Expected (Search dikosongkan sebelum asersi).
  - TC-GS-HHR-265 langkah 4 sampai 5 mengklik header `Device Name` sekali (Ascending) lalu header `Serial Number`; spec mengikuti TC dan mengembalikan sort `Serial Number` ke netral dengan dua klik tambahan.
  - Seed Reader A bernama literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah baris; fixture backend dan pemulihannya antar TC disediakan tim FE/BE tanpa mekanisme yang ditulis di TC.
  - Post Condition semua TC di spec ini `-`; tidak ada yang diasersi.

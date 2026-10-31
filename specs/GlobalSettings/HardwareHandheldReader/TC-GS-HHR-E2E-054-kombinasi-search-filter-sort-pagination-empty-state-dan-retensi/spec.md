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
- Akun kedua (langkah 132, TC-GS-HHR-267): Total Control Client L, `totalControl_automated_{namaClient}@qwertysystem.net` dengan nama client Client L, password `Spectra.env.GS_CLIENTL_TC_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` oleh pemilik suite). Client L memiliki 26 reader `Large Reader - 1` sampai `Large Reader - 26`; seluruhnya berjenis `Short Range` supaya Filter `Range Type` = `Short Range` tetap memuat 26 baris dan halaman terakhir pada `Rows per page` 25 adalah halaman 2 (kondisi data disediakan tim FE; lihat "Temuan untuk QA"). Hook `after` mengembalikan sesi ke akun default suite.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; spec tidak mengulang langkah buka di `## Test Steps` kecuali setelah ganti akun. Klik item sidebar `Handheld Reader` mereset Search, Sort, dan Filter; state yang harus dipulihkan ditulis sebagai langkah penghubung eksplisit.
- Client A: plan Growth, format tanggal default General Settings `dd/MM/yy` 24-hour (tidak diubah spec ini).
- Data Dinamis Seed Reader A (10 reader DD-01 sampai DD-10, jumlah baris N = 10 dari seeding), dibuat lewat fixture backend sebelum eksekusi (`Fixture.hardwareHandheldReader.seedReaderA`, fixture baru) dan dipulihkan antar TC oleh fixture backend. Pengecualian S-12 Population Seed Reader A HHR: nama literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah baris. Spec hanya membaca daftar. Kolom yang dicocokkan Search dan dipakai Filter dan Sort (data memuat sedikitnya dua nilai distinct pada kolom `Device Name`, `Serial Number`, `Status`, dan `Source`):

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

- Model Filter Panel: panel dibuka dengan klik ikon Filter, tetap terbuka sesudah `[Apply]`, dan ditutup dengan klik ikon Filter; tiap pembukaan panel berpasangan dengan penutupan.
- Kemampuan teknis: pembacaan keyword Search, indikator sort, chip Filter, indikator Filter, `Rows per page`, halaman aktif, dan teks pagination; muat ulang halaman dengan F5; klik item sidebar.
- State yang diubah spec: `Rows per page` diubah ke 25 (blok TC-GS-HHR-262 dan 267) dan dikembalikan ke 10 pada langkah 60; Search, Filter, dan Sort dipulihkan lewat langkah penghubung di akhir tiap blok.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` true untuk akun Total Control Client A dan hook `after` memulihkannya (lihat `suite.md`); untuk akun Client L flag diatur hook yang sama (disediakan tim FE).

## Test Steps

### TC-GS-HHR-18: Empty state saat Search tidak menemukan reader

1. Ketik Search `zzzz`, tekan Enter
2. Verifikasi ilustrasi empty state tampil dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
3. Verifikasi tombol `[Reset Filters]` tampil
4. Klik ikon `(←)` pada search box

### TC-GS-HHR-19: Reset Filters mengosongkan Search dan seluruh Filter

5. Ketik Search `zzzz`, tekan Enter
6. Klik ikon Filter untuk membuka panel
7. Pilih `Available` pada field `Status`
8. Klik `[Apply]`
9. Klik ikon Filter untuk menutup panel
10. Verifikasi empty state `No results found` tampil
11. Verifikasi tombol `[Reset Filters]` tampil
12. Klik `[Reset Filters]`
13. Verifikasi kolom Search kosong
14. Verifikasi kolom Search tertutup
15. Verifikasi indikator Filter hilang
16. Klik ikon Filter untuk membuka panel
17. Verifikasi tidak ada chip Filter pada panel
18. Klik ikon Filter untuk menutup panel
19. Verifikasi tabel menampilkan 10 baris Seed Reader A pada halaman 1
20. Verifikasi teks pagination `Showing 1 - 10 of 10 readers`

### TC-GS-HHR-260: Search lalu Filter menghasilkan irisan

21. Ketik Search `Gudang`, tekan Enter
22. Klik ikon Filter untuk membuka panel
23. Pilih `Available` pada field `Status`
24. Klik `[Apply]`
25. Klik ikon Filter untuk menutup panel
26. Verifikasi tabel menampilkan 1 baris DD-02 (`Gudang Reader - 1`)
27. Verifikasi keyword Search `Gudang` tidak tereset oleh Apply
28. Klik ikon `(←)` pada search box
29. Klik ikon Filter untuk membuka panel
30. Klik `[Clear Field]`
31. Klik `[Apply]`
32. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-261: Filter lalu Search menghasilkan irisan yang sama

33. Klik ikon Filter untuk membuka panel
34. Pilih `Available` pada field `Status`
35. Klik `[Apply]`
36. Klik ikon Filter untuk menutup panel
37. Ketik Search `Gudang`, tekan Enter
38. Verifikasi tabel menampilkan 1 baris DD-02 (`Gudang Reader - 1`), identik dengan urutan Search lalu Filter
39. Klik ikon `(←)` pada search box
40. Klik ikon Filter untuk membuka panel
41. Klik `[Clear Field]`
42. Klik `[Apply]`
43. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-262: Kombinasi Search, Filter, Sort, dan Pagination aktif bersamaan

44. Ketik Search `reader`, tekan Enter
45. Klik ikon Filter untuk membuka panel
46. Pilih `Available` dan `Damaged` pada field `Status`
47. Klik `[Apply]`
48. Klik ikon Filter untuk menutup panel
49. Klik header `Device Name` dua kali (Descending)
50. Ubah `Rows per page` menjadi 25
51. Verifikasi tabel menampilkan 4 baris berurutan: `Zebra RFID Reader - 1` (DD-01), `Zebra RFID Reader - 1` (DD-06, tie-breaker `Serial Number` tetap Ascending), `Zebra Mobile Reader - 1` (DD-03), lalu `Gudang Reader - 1` (DD-02)
52. Verifikasi teks pagination `Showing 1 - 4 of 4 readers`
53. Verifikasi keyword Search `reader` tidak berubah saat page size diubah
54. Verifikasi sort `Device Name` Descending tidak berubah saat page size diubah
55. Klik ikon Filter untuk membuka panel
56. Verifikasi filter `Status` `Available` dan `Damaged` tidak berubah saat page size diubah
57. Klik `[Clear Field]`
58. Klik `[Apply]`
59. Klik ikon Filter untuk menutup panel
60. Ubah `Rows per page` kembali menjadi 10
61. Klik header `Device Name` kali ketiga
62. Klik ikon `(←)` pada search box

### TC-GS-HHR-263: Clear Filter saat Search dan Sort aktif

63. Ketik Search `Gudang`, tekan Enter
64. Klik header `Device Name` dua kali (Descending)
65. Klik ikon Filter untuk membuka panel
66. Pilih `Missing` pada field `Status`
67. Klik `[Apply]`
68. Klik `[Clear Field]`
69. Klik `[Apply]`
70. Klik ikon Filter untuk menutup panel
71. Verifikasi tabel menampilkan 3 baris dari keyword `Gudang`
72. Verifikasi urutan Device Name Descending: `Gudang Reader - 4`, `Gudang Reader - 2`, `Gudang Reader - 1`
73. Klik header `Device Name` kali ketiga
74. Klik ikon `(←)` pada search box

### TC-GS-HHR-264: Clear Search saat Filter dan Sort aktif

75. Ketik Search `Gudang`, tekan Enter
76. Klik ikon Filter untuk membuka panel
77. Pilih `Available` pada field `Status`
78. Klik `[Apply]`
79. Klik ikon Filter untuk menutup panel
80. Klik header `Device Name` dua kali (Descending)
81. Klik ikon `(✕)` pada search box, tekan Enter
82. Verifikasi kolom Search kosong
83. Verifikasi tabel menampilkan 6 baris Status `Available`
84. Verifikasi urutan baris Device Name Descending: `Zebra RFID Reader - 1` (DD-01), `Zebra RFID Reader - 1` (DD-06), `Unitech EA520 - 1` (DD-08), `International Handheld Terminals Ltd Ultra-Rugged Series 7000 Pro Max - 1` (DD-09), `Honeywell CK65 - 1` (DD-07), `Gudang Reader - 1` (DD-02)
85. Verifikasi indikator sort `Device Name` Descending tetap aktif
86. Klik ikon Filter untuk membuka panel
87. Verifikasi filter `Status` `Available` tetap aktif
88. Klik `[Clear Field]`
89. Klik `[Apply]`
90. Klik ikon Filter untuk menutup panel
91. Klik header `Device Name` kali ketiga
92. Klik ikon `(←)` pada search box

### TC-GS-HHR-265: Berganti kolom sort tidak mereset Search dan Filter

93. Ketik Search `Gudang`, tekan Enter
94. Klik ikon Filter untuk membuka panel
95. Pilih `Official` pada field `Source`
96. Klik `[Apply]`
97. Klik ikon Filter untuk menutup panel
98. Klik header `Device Name`
99. Klik header `Serial Number`
100. Verifikasi indikator sort `Device Name` kembali netral
101. Verifikasi indikator sort `Serial Number` Ascending
102. Verifikasi tabel menampilkan 3 baris keyword `Gudang` Source `Official` berurutan Serial Number: `SN-HHR-00102`, `SN-HHR-00104`, `SN-HHR-00205`
103. Klik header `Serial Number` dua kali lagi (kembali netral)
104. Klik ikon `(←)` pada search box
105. Klik ikon Filter untuk membuka panel
106. Klik `[Clear Field]`
107. Klik `[Apply]`
108. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-266: Pemulihan dari empty state setelah melepas salah satu kontrol

109. Ketik Search `Honeywell`, tekan Enter
110. Klik ikon Filter untuk membuka panel
111. Pilih `Missing` pada field `Status`
112. Klik `[Apply]`
113. Klik ikon Filter untuk menutup panel
114. Verifikasi empty state `No results found` tampil (kombinasi `Honeywell` dan `Missing`)
115. Klik ikon `(✕)` pada search box, tekan Enter
116. Verifikasi tabel pulih menampilkan 1 baris DD-04 (`Status` `Missing`)
117. Klik ikon `(←)` pada search box
118. Klik ikon Filter untuk membuka panel
119. Klik `[Clear Field]`
120. Klik `[Apply]`
121. Klik ikon Filter untuk menutup panel

### TC-GS-HHR-268: Klik ulang menu Handheld Reader dari sidebar mereset state

122. Ketik Search `Gudang`, tekan Enter
123. Klik header `Serial Number`
124. Klik ikon Filter untuk membuka panel
125. Pilih `Missing` pada field `Status`
126. Klik `[Apply]`
127. Klik item `Handheld Reader` pada sidebar
128. Verifikasi Search kosong
129. Verifikasi sort kembali Device Name A-Z
130. Verifikasi tabel menampilkan 10 baris
131. Verifikasi indikator Filter tidak tampil (tidak ada filter ter-Apply)

### TC-GS-HHR-267: Refresh F5 mempertahankan Search, Sort, Filter, halaman, dan Rows per page (Client L)

132. Logout dari akun Total Control Client A (ganti akun)
133. Login sebagai Total Control Client L
134. Buka Global Settings > Hardware > Handheld Reader
135. Ketik Search `Reader`, tekan Enter
136. Klik header `Serial Number`
137. Klik ikon Filter untuk membuka panel
138. Pilih `Short Range` pada field `Range Type`
139. Klik `[Apply]`
140. Klik ikon Filter untuk menutup panel
141. Ubah `Rows per page` menjadi 25
142. Buka halaman terakhir pada Pagination
143. Muat ulang halaman dengan F5
144. Verifikasi keyword Search `Reader` tetap sama
145. Verifikasi sort `Serial Number` Ascending tetap sama
146. Klik ikon Filter untuk membuka panel
147. Verifikasi filter `Range Type` `Short Range` tetap sama
148. Klik ikon Filter untuk menutup panel
149. Verifikasi `Rows per page` 25 tetap sama
150. Verifikasi halaman aktif tetap halaman terakhir
151. Klik item `Handheld Reader` pada sidebar

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 18, 19, 260, 261, 262, 263, 264, 265, 266, 268, lalu 267. Blok Client A lebih dulu; TC-GS-HHR-267 memakai akun Client L dan ditaruh paling akhir karena ada langkah ganti akun eksplisit (langkah 132); bagian sesudah ganti akun tetap bermakna walau blok sebelumnya gagal. TC-GS-HHR-268 mereset state lewat klik sidebar sehingga ditaruh sesudah blok yang memakai state. Urutan ini menyimpang dari urutan TC sumber.
- Langkah penghubung (aksi tanpa `Verifikasi`): klik ikon Filter yang membuka atau menutup panel, `[Clear Field]` lalu `[Apply]` di akhir tiap blok, klik ketiga header `Device Name` atau dua klik lagi pada header `Serial Number` untuk mengembalikan sort ke netral, klik ikon `(←)` yang menutup input Search, langkah 60 (mengembalikan `Rows per page` ke 10), dan klik sidebar di akhir TC-GS-HHR-267.
- Anchor asersi absence dan universal: `Verifikasi` empty state `No results found` pada TC-GS-HHR-19 dan 266 adalah anchor positif Search atau Filter; `Verifikasi` indikator Filter hilang dan tidak ada chip Filter (TC-GS-HHR-19) didahului `Verifikasi` tombol `[Reset Filters]` dan empty state yang membuktikan halaman termuat dan panel dapat dibuka; `Verifikasi` "6 baris Status `Available`" (TC-GS-HHR-264) mendahului `Verifikasi` urutan Descending; `Verifikasi` indikator Filter tidak tampil (TC-GS-HHR-268) didahului `Verifikasi` tabel 10 baris tampil.
- Pembagian TC lintas spec: Search per kelas kolom ada di spec 050, Filter multi-select ada di spec 051, Filter rentang di spec 052, Sort per kolom di spec 053, Pagination tabel utama (ukuran halaman dan navigasi halaman) di spec 060.
- Spec memuat 151 langkah (di atas smell sekitar 35 langkah, tanpa ekspansi). Alasan: seluruhnya satu kelas harness (kombinasi Search, Filter, Sort, dan Pagination daftar reader yang berbagi dataset yang sama), tanpa aksi yang mengubah data; tiap blok TC membersihkan state-nya sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; blok Client L (TC-GS-HHR-267) memakai langkah ganti akun eksplisit dan tetap bermakna walau bagian Client A gagal.
- Temuan untuk QA:
  - TC-GS-HHR-267: precondition hanya menyebut "Client L memiliki 26 reader" tanpa menyebut `Range Type` reader; agar Filter `Short Range` dan `Rows per page` 25 menghasilkan halaman terakhir (halaman 2), seluruh 26 reader harus `Short Range`. Spec menulis kondisi itu sebagai kebutuhan data yang disediakan tim FE. Email akun Total Control Client L mengikuti pola fixture `totalControl_automated_{namaClient}@qwertysystem.net`; nilai persis tidak tertulis di Pre-setup TC.
  - TC-GS-HHR-268: langkah TC 4 tidak menutup Filter Panel sebelum klik item `Handheld Reader` pada sidebar (model Filter Panel menyatakan panel tetap terbuka sesudah `[Apply]`); spec mengikuti TC dan keadaan panel serta penanda indikator Filter pada ikon yang tertutup tidak dinyatakan TC untuk kasus ini.
  - Seed Reader A bernama literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah baris; fixture backend dan pemulihannya antar TC disediakan tim FE/BE tanpa mekanisme yang ditulis di TC.
  - Post Condition semua TC di spec ini `-`; tidak ada yang diasersi.

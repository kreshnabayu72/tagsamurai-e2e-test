---
id: TC-GS-USER-E2E-007-search-filter-sort-pagination-download
title: Search, filter, sort, pagination, dan download di User List mencerminkan data nyata
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-358
  - TC-GS-USER-359
  - TC-GS-USER-360
  - TC-GS-USER-361
  - TC-GS-USER-362
  - TC-GS-USER-554
  - TC-GS-USER-555
  - TC-GS-USER-556
  - TC-GS-USER-557
  - TC-GS-USER-357
  - TC-GS-USER-127
  - TC-GS-USER-197
  - TC-GS-USER-198
  - TC-GS-USER-199
  - TC-GS-USER-200
  - TC-GS-USER-201
  - TC-GS-USER-202
  - TC-GS-USER-207
  - TC-GS-USER-208
  - TC-GS-USER-364
  - TC-GS-USER-128
  - TC-GS-USER-218
  - TC-GS-USER-219
  - TC-GS-USER-220
  - TC-GS-USER-221
  - TC-GS-USER-222
  - TC-GS-USER-223
  - TC-GS-USER-224
  - TC-GS-USER-225
  - TC-GS-USER-227
  - TC-GS-USER-228
  - TC-GS-USER-229
  - TC-GS-USER-230
  - TC-GS-USER-210
  - TC-GS-USER-211
  - TC-GS-USER-212
  - TC-GS-USER-216
  - TC-GS-USER-132
  - TC-GS-USER-131
  - TC-GS-USER-490
  - TC-GS-USER-491
  - TC-GS-USER-492
  - TC-GS-USER-493
  - TC-GS-USER-496
  - TC-GS-USER-497
coverage:
  web: automated
---

# Search, filter, sort, pagination, dan download di User List mencerminkan data nyata

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- Ada lebih dari 25 user secara total, tersebar di sedikitnya 2 halaman, di luar user yang tercantum di bawah
- User "Andi Saputra" punya First Name yang diawali huruf kapital
- User "budi Iskandar" punya First Name yang diawali huruf kecil, sehingga sort Name bisa diperiksa terhadap collation ICU `en-US-x-icu` dan bukan urutan biner/ASCII
- User "Budi Santoso" berstatus Active, Position "Staff", Division "Finance", Email unik yang diketahui, Employee ID "EMP-002", 1 Access, dan terakhir diubah oleh admin "Rina Kartika"
- User "Citra Wulandari" berstatus Active, Position "Manager", Division "Marketing", dan terakhir diubah oleh admin "Doni Admin"
- User "Doni Pratama" punya Access `[Fixed Asset, Global Settings]` (2 Access) dan TAG "RFID-00321"
- User "Eka Prasetyo" berstatus Inactive
- User "Fajar Nugroho" berstatus Pending Activation dan belum pernah login
- User "Gita Ayu" berstatus Activated normal, tanpa perubahan email yang tertunda
- User "Hana Melati" berstatus Activated dan punya perubahan email tertunda (`pendingEmail` terisi), sehingga Activation Status-nya "Pending Email Confirmation"
- User "Indra Kusuma" punya Position dan Employee ID yang sama-sama kosong
- User "Joko Prasetyo" punya Access `[Global Settings, Fixed Asset, Admin Console]` (3 Access)
- User "Kirana Dewi" punya Temporary User Yes dengan Temporary Until 3 hari dari hari ini
- User "Laras Ayu" punya Temporary User Yes dengan Temporary Until 10 hari dari hari ini
- Kolom Activation Status, Temporary User, Temporary Until, dan TAG adalah kolom curated (tersembunyi secara default) dan diaktifkan lewat Setup Column sebelum langkah spec ini berjalan
- Tim FE diminta menyediakan cara bagi script untuk membaca isi berkas yang benar-benar terunduh (bukan hanya nama berkas), karena beberapa langkah memverifikasi byte berkas yang sebenarnya

## Test Steps

### Search lintas kolom

1. Cari "budi.santoso" (bagian dari email "Budi Santoso" yang diketahui)
2. Verifikasi "Budi Santoso" muncul di hasil, meski kata kunci tidak cocok dengan Name-nya
3. Kosongkan pencarian
4. Cari "Manager" (Position "Citra Wulandari")
5. Verifikasi "Citra Wulandari" muncul di hasil, meski kata kunci tidak cocok dengan Name atau Email-nya
6. Kosongkan pencarian
7. Cari "Finance" (Division "Budi Santoso")
8. Verifikasi "Budi Santoso" muncul di hasil
9. Kosongkan pencarian
10. Cari "EMP-002" (Employee ID "Budi Santoso")
11. Verifikasi "Budi Santoso" muncul di hasil
12. Kosongkan pencarian
13. Cari "Rina Kartika" (admin yang terakhir mengubah "Budi Santoso")
14. Verifikasi "Budi Santoso" muncul di hasil
15. Kosongkan pencarian
16. Cari "Fixed" (bagian dari nama produk Access "Fixed Asset")
17. Verifikasi "Doni Pratama" muncul di hasil dan user tanpa Access Fixed Asset tidak muncul
18. Kosongkan pencarian
19. Cari "Pending"
20. Verifikasi "Fajar Nugroho" dan "Hana Melati" muncul di hasil, dan "Gita Ayu" (Activated, tanpa perubahan tertunda) tidak muncul
21. Kosongkan pencarian
22. Cari "Yes"
23. Verifikasi "Kirana Dewi" dan "Laras Ayu" muncul di hasil
24. Kosongkan pencarian
25. Cari "00321" (bagian dari kode TAG "Doni Pratama")
26. Verifikasi hanya "Doni Pratama" yang muncul di hasil
27. Kosongkan pencarian

### Sort Name dan collation locale

28. Klik header kolom `Name` satu kali
29. Verifikasi urutannya menaik secara alfabetis dengan collation ICU `en-US-x-icu`, sehingga "budi Iskandar" bisa muncul sebelum "Andi Saputra" menurut aturan locale, bukan selalu setelah semua nama berawalan huruf kapital seperti pada sort biner
30. Klik header kolom `Name` lagi
31. Verifikasi urutan menjadi menurun
32. Klik header kolom `Name` untuk ketiga kalinya
33. Verifikasi urutan kembali ke default

### Filter per field

34. Buka Filter Panel, pilih Status "Inactive", klik `[Apply Filter]`
35. Verifikasi hanya baris dengan Status Inactive yang muncul, termasuk "Eka Prasetyo"
36. Klik `[Clear Field]` dan verifikasi filter kembali ke placeholder default "All statuses"
37. Pilih Position "Budi Santoso" ("Staff"), klik `[Apply Filter]`
38. Verifikasi hanya baris dengan Position itu yang muncul
39. Kosongkan filter
40. Pilih Division "Budi Santoso" ("Finance"), klik `[Apply Filter]`
41. Verifikasi hanya baris dengan Division itu yang muncul
42. Kosongkan filter
43. Pilih Modified By "Rina Kartika" dan "Doni Admin" bersamaan, klik `[Apply Filter]`
44. Verifikasi "Budi Santoso" dan "Citra Wulandari" sama-sama muncul, karena Modified By menggabungkan admin terpilih dengan OR
45. Kosongkan filter
46. Pilih tanggal Last Update yang cocok dengan perubahan yang ada, klik `[Apply Filter]`
47. Verifikasi hanya baris dengan tanggal Last Update itu yang muncul
48. Kosongkan filter
49. Pilih Activation "Pending Activation", klik `[Apply Filter]`
50. Verifikasi hanya "Fajar Nugroho" yang muncul
51. Kosongkan filter
52. Pilih Activation "Pending Email Confirmation", klik `[Apply Filter]`
53. Verifikasi hanya "Hana Melati" yang muncul, dan "Gita Ayu" maupun "Fajar Nugroho" tidak muncul
54. Kosongkan filter
55. Pilih Access "Global Settings", klik `[Apply Filter]`
56. Verifikasi hanya baris yang Access-nya mencakup "Global Settings" yang muncul
57. Kosongkan filter
58. Pilih Temporary User "Yes", klik `[Apply Filter]`
59. Verifikasi hanya "Kirana Dewi" dan "Laras Ayu" yang muncul
60. Kosongkan filter
61. Pilih tanggal Temporary Until "Kirana Dewi", klik `[Apply Filter]`
62. Verifikasi hanya "Kirana Dewi" yang muncul, bukan "Laras Ayu"
63. Kosongkan filter

### Sort per kolom

64. Klik header kolom `Active` satu kali, lalu lagi, lalu untuk ketiga kalinya
65. Verifikasi siklus tiga keadaan: Active dulu, lalu Inactive dulu, lalu urutan default
66. Klik header kolom `Email` satu kali, lalu lagi, lalu untuk ketiga kalinya
67. Verifikasi siklus tiga keadaan mengurutkan secara alfabetis ke kedua arah, lalu kembali ke default
68. Klik header kolom `Position` satu kali
69. Verifikasi baris dengan Position kosong, termasuk "Indra Kusuma", berada di akhir urutan menaik
70. Klik header kolom `Division` satu kali, lalu lagi, lalu untuk ketiga kalinya
71. Verifikasi siklus tiga keadaan mengurutkan secara alfabetis ke kedua arah, lalu kembali ke default
72. Klik header kolom `Access` satu kali
73. Verifikasi "Budi Santoso" (1 Access) muncul sebelum "Doni Pratama" (2 Access), yang muncul sebelum "Joko Prasetyo" (3 Access), dan user dengan jumlah Access sama dipecah urutannya secara alfabetis menurut nama produk pertamanya
74. Klik header kolom `Employee ID` satu kali
75. Verifikasi baris dengan Employee ID kosong, termasuk "Indra Kusuma", berada di akhir
76. Klik header kolom `Modified By` satu kali
77. Verifikasi urutan mengikuti nama lengkap tiap aktor, bukan bentuk singkat yang tampil di layar
78. Klik header kolom `Last Update` satu kali
79. Verifikasi urutannya Newest First
80. Klik header kolom `Activation Status` satu kali
81. Verifikasi urutannya alfabetis ("Activated", "Pending Activation", "Pending Email Confirmation")
82. Klik header kolom `Temporary User` satu kali
83. Verifikasi urutannya Yes First
84. Klik header kolom `Temporary Until` satu kali
85. Verifikasi "Kirana Dewi" muncul sebelum "Laras Ayu" (kedaluwarsa yang lebih dekat dulu), dan baris yang bukan Temporary berada di akhir
86. Klik header kolom `TAG` satu kali
87. Verifikasi urutannya alfabetis menurut kode TAG, dan baris tanpa TAG terpasang berada di akhir

### Kombinasi Search, Filter, Sort, dan Pagination

88. Cari "Finance", lalu pilih Position "Budi Santoso" ("Staff") dan klik `[Apply Filter]`
89. Verifikasi hasilnya adalah irisan tepat antara pencarian dan filter, dan kata kunci pencarian tidak direset oleh penerapan filter
90. Kosongkan filter dan pencarian
91. Pilih Position "Staff" dan klik `[Apply Filter]`, lalu cari "Finance"
92. Verifikasi kriteria filter tetap aktif di latar belakang dan hasilnya adalah irisan tepat
93. Kosongkan filter dan pencarian
94. Dengan lebih dari 15 user tersedia, cari sebuah kata kunci, terapkan filter, klik header kolom sort, dan ubah ukuran halaman, semuanya sekaligus
95. Verifikasi keempat kondisi berlaku bersamaan tanpa saling menimpa
96. Ubah pencarian atau filter sehingga hasilnya menjadi "No results found"
97. Lepaskan salah satu kriteria yang aktif
98. Verifikasi tabel otomatis pulih dan menampilkan data yang cocok lagi

### Pagination

99. Ubah ukuran halaman menjadi 25
100. Verifikasi jumlah baris per halaman sesuai ukuran yang dipilih
101. Pindah ke halaman 2
102. Verifikasi halaman 2 menampilkan kumpulan baris berikutnya

### Download

103. Kosongkan semua pencarian dan filter yang aktif, klik Download dan pilih CSV
104. Verifikasi berkas yang terunduh bernama "User-List.csv" dan memuat semua baris (fetchAll), bukan hanya halaman yang sedang tampil
105. Terapkan Filter Division "Finance", klik Download dan pilih CSV
106. Verifikasi berkas yang terunduh hanya memuat baris dengan Division "Finance", sesuai filter aktif, bukan seluruh daftar user
107. Kosongkan filter, klik Download dan pilih CSV lagi
108. Verifikasi berkas berhasil diunduh dan tidak ada toast sukses
109. Klik Download dan pilih XLSX
110. Verifikasi berkas yang terunduh bernama "User-List.xlsx"
111. Buka berkas CSV yang terunduh dan periksa nilai selnya
112. Verifikasi kolom `Active` menampilkan teks literal "Active" atau "Inactive" (bukan boolean atau ikon), kolom `Access` menampilkan nama produk biasa yang dipisah ", " tanpa pewarnaan badge, dan field kosong (seperti Position "Indra Kusuma") menampilkan satu tanda hubung "-"
113. Sembunyikan kolom `Email` lewat Setup Column, klik Download dan pilih CSV
114. Verifikasi berkas yang terunduh tidak memuat kolom `Email`
115. Munculkan kembali kolom `Email` lewat Setup Column, klik Download dan pilih CSV
116. Verifikasi berkas yang terunduh memuat kolom `Email` lagi

## Notes

- Satu spec mencakup seluruh toolbar List (Search, Filter, Sort, Pagination, Download) di User List, semuanya di bawah Role Total Control yang sama dan entity Client yang sama, tanpa modal, mengikuti `docs/e2e-conventions.md` bagian 3.
- Spec ini membuktikan bahwa Search, Filter, Sort, dan Download benar-benar menarik dan mengembalikan baris yang tepat dari data nyata di backend. Tampilan dan perilaku List yang murni UI (interaksi search box, retensi state, Setup Column, badge, dan lainnya) dicakup spec hanya-FE dan spec lain: `TC-GS-USER-E2E-089` sampai `093` (Setup Column), `094` (search box), `095` (kolom Name dan Access), `096` (filter Access dan chip), `097` (retensi Search/Filter/Sort/seleksi).
- Setup Column itu sendiri (mencentang kolom, drag, pin/unpin, Reset to Default) tidak diverifikasi di sini. Langkah 113 sampai 116 memakai Setup Column hanya sebagai cara mencapai keadaan Download tertentu.
- TC-GS-USER-363 (Download gagal karena error server) dicakup `TC-GS-USER-E2E-080-download-gagal-server` (`Mode: mock`).
- TC-GS-USER-494 adalah duplikat isi TC-GS-USER-496 (menurut `GAP-161` yang sudah ditutup di PRD sumber). Langkah 113 sampai 114 mencakup keduanya dengan kata-kata TC-496, dan verifikasi WYSIWYG kolom juga ada di `TC-GS-USER-E2E-100-list-download-wysiwyg-kolom`.
- Membaca byte berkas unduhan yang sebenarnya (langkah 104, 106, 108, 110, 112, 114, 116) butuh dukungan tooling dari tim FE, dicatat di Prerequisites.
- Spec ini tidak membuat atau menghapus data. Setiap user yang disebut harus sudah ada sebelum run, dan tidak ada yang butuh pembersihan di luar yang sudah ditangani lingkungan khusus automation.

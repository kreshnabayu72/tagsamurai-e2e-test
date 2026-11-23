---
id: TC-FA-FAFM-UI-085-tabel-files-seleksi-bulk
title: "Tabel Files: seleksi baris, Bulk Action Bar, dan Selection Limit"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ACT-03a", "ACT-03g", "ACT-03h", "DIM-09a", "S-13", "TBL-05e", "§4.1a#p11", "§4.4#b8", "EB-BLK-1@tabel-files", "EB-BLK-4", "EB-BLK-6"]
smoke: []
dependsOn: []
trace:
  "ACT-03a": [3, 6, 10, 83, 85]
  "ACT-03g": [88, 90, 94, 96, 100, 102, 106, 113]
  "ACT-03h": [90, 96, 102, 103, 120, 122, 123]
  "DIM-09a": [88, 90, 94, 96, 100, 102]
  "S-13": [2, 3, 5, 6]
  "TBL-05e": [11, 26, 34, 35, 36]
  "§4.1a#p11": [100, 102, 103, 120, 122, 123]
  "§4.4#b8": [7, 10, 11, 15]
  "EB-BLK-1@tabel-files": [7, 8, 15, 18, 20, 21, 24, 26, 27, 29, 36, 42, 43, 45, 51, 53, 54, 61, 62]
  "EB-BLK-4": [69, 70, 71, 78, 79, 80]
  "EB-BLK-6": [91, 97, 102, 103, 104, 106, 112, 113, 115, 122, 123]
anchor: []
coverage:
  web: automated
---

# Tabel Files: seleksi baris, Bulk Action Bar, dan Selection Limit

## Prerequisites
- Aktor: Total Control (K1 sampai K7 dan K9); Read Only (K8).
- Layar awal: Tabel File Manager tab Files.
- Komponen: Tabel File Manager tab Files.
- Data:
  - DU-085-1: 12 file `Asset Photo` bernama `site-photo-{n}.jpg` (n = 1 sampai 12), Asset `Laptop Dell Latitude 5420 - 4`, Group `Head Office`; file ke-1 paling baru menurut Upload Date.
  - DU-085-2: 999 file `Asset Photo` bernama `site-photo-{n}.jpg` (n = 1 sampai 999); file ke-1 paling baru; tombol Select All membaca `Select All (999 records)`.
  - DU-085-3: 1000 file `Asset Photo` bernama `site-photo-{n}.jpg` (n = 1 sampai 1000); file ke-1 paling baru; tombol Select All membaca `Select All (1000 records)`.
  - DU-085-4: 1001 file `Asset Photo` bernama `site-photo-{n}.jpg` (n = 1 sampai 1001); file ke-1 paling baru; tombol Select All membaca `Select All (1001 records)`; toast batas `Error, only the first 1000 of 1001 rows were selected. Narrow your filter to include the rest.`; pada ukuran halaman 10 file ke-1001 berada di halaman `101`.
  - DU-085-5: 1200 file `Asset Photo` bernama `survey-{n}.jpg` (n = 1 sampai 1200); hasil Search `survey` membaca `Select All (1200 records)`; toast batas `Error, only the first 1000 of 1200 rows were selected. Narrow your filter to include the rest.`.
  - DU-085-7: kata kunci Search `survey` (cocok dengan DU-085-5) dan `site-photo-12` (hanya cocok dengan file ke-12 DU-085-1).
  - DU-085-6: 300 file `Asset Photo` bernama `site-photo-{n}.jpg` (n = 1 sampai 300) yang tidak cocok dengan kata kunci `survey`.
- Kondisi:
  - Semua kondisi: Selection Limit bernilai `1000`; data dimuat per halaman dari server; ukuran halaman bawaan 10; tab `Asset Photo` aktif; belum ada Search, filter, atau seleksi.
  - K1: tabel berisi DU-085-1; server menerima permintaan bulk Delete.
  - K2: tabel berisi DU-085-2.
  - K3: tabel berisi DU-085-3.
  - K4: tabel berisi DU-085-4.
  - K5: tabel berisi DU-085-5 dan DU-085-6.
  - K6: tabel berisi DU-085-1; server menjawab permintaan bulk Delete dengan error server.
  - K7: tabel berisi DU-085-1; permintaan bulk Delete tidak mendapat respons sampai waktu habis.
  - K8: tabel berisi DU-085-1; aktor Read Only.


## Test Steps

### Memilih satu baris menampilkan Bulk Action Bar
1. Tampilkan Tabel File Manager tab Files dengan kondisi K1
2. Verifikasi baris `site-photo-1.jpg` tampil
3. Verifikasi Bulk Action Bar tidak tampil sebelum ada baris terpilih
4. Centang baris `site-photo-1.jpg`
5. Verifikasi baris `site-photo-1.jpg` ditandai terpilih
6. Verifikasi Bulk Action Bar tampil
7. Verifikasi penghitung seleksi `1 File selected` tampil
8. Verifikasi tombol `Select All (12 records)` tampil
9. Klik tombol `Bulk Action`
10. Verifikasi menu Bulk Action memuat pilihan `Download (ZIP)`
11. Verifikasi menu Bulk Action memuat pilihan `Delete`

### Memilih banyak baris dan penghitung bentuk jamak
12. Tampilkan Tabel File Manager tab Files dengan kondisi K1
13. Centang baris `site-photo-1.jpg`
14. Centang baris `site-photo-2.jpg`
15. Verifikasi penghitung seleksi `2 Files selected` tampil

### Checkbox header: indeterminate dan halaman penuh
16. Tampilkan Tabel File Manager tab Files dengan kondisi K1
17. Centang baris `site-photo-1.jpg`
18. Verifikasi checkbox header berstatus indeterminate
19. Klik checkbox header
20. Verifikasi checkbox header berstatus tercentang
21. Verifikasi penghitung seleksi `10 Files selected` tampil setelah checkbox header diklik

### Seleksi bertahan saat pindah halaman
22. Tampilkan Tabel File Manager tab Files dengan kondisi K1
23. Klik checkbox header
24. Verifikasi penghitung seleksi `10 Files selected` tampil sebelum pindah halaman
25. Klik halaman `2`
26. Verifikasi penghitung seleksi `10 Files selected` tetap tampil di halaman 2
27. Verifikasi checkbox header tidak tercentang di halaman 2
28. Centang baris `site-photo-11.jpg`
29. Verifikasi penghitung seleksi `11 Files selected` tampil di halaman 2

### Seleksi bertahan saat Search menyembunyikan baris terpilih
30. Tampilkan Tabel File Manager tab Files dengan kondisi K1
31. Centang baris `site-photo-1.jpg`
32. Isi kotak Search dengan `site-photo-12`
33. Tekan Enter
34. Verifikasi baris `site-photo-12.jpg` tampil
35. Verifikasi baris `site-photo-1.jpg` tidak tampil
36. Verifikasi penghitung seleksi `1 File selected` tetap tampil walau baris terpilih tersembunyi

### Tombol ✕ membersihkan seluruh seleksi
37. Tampilkan Tabel File Manager tab Files dengan kondisi K1
38. Klik checkbox header
39. Klik halaman `2`
40. Centang baris `site-photo-11.jpg`
41. Klik tombol ✕ pada Bulk Action Bar
42. Verifikasi baris `site-photo-11.jpg` tampil dengan checkbox tidak tercentang
43. Verifikasi Bulk Action Bar tidak tampil setelah ✕ diklik
44. Klik halaman `1`
45. Verifikasi checkbox header tidak tercentang di halaman 1 setelah ✕ diklik

### Cancel dialog Delete tidak memproses apa pun
46. Tampilkan Tabel File Manager tab Files dengan kondisi K1
47. Centang baris `site-photo-1.jpg`
48. Centang baris `site-photo-2.jpg`
49. Klik tombol `Bulk Action`
50. Klik pilihan `Delete`
51. Verifikasi dialog dengan judul `Delete Files` tampil
52. Klik `[Cancel]`
53. Verifikasi baris `site-photo-1.jpg` masih tampil
54. Verifikasi penghitung seleksi `2 Files selected` tetap tampil setelah dialog dibatalkan

### Aksi selesai: Bulk Action Bar hilang dan seleksi bersih
55. Tampilkan Tabel File Manager tab Files dengan kondisi K1
56. Centang baris `site-photo-1.jpg`
57. Centang baris `site-photo-2.jpg`
58. Klik tombol `Bulk Action`
59. Klik pilihan `Delete`
60. Klik `[Delete]` pada dialog `Delete Files`
61. Verifikasi toast sukses `Success, file has been deleted.` tampil setelah bulk Delete dikonfirmasi
62. Verifikasi Bulk Action Bar tidak tampil setelah aksi selesai

### Bulk gagal 5xx mempertahankan bar dan seleksi
63. Tampilkan Tabel File Manager tab Files dengan kondisi K6
64. Centang baris `site-photo-1.jpg`
65. Centang baris `site-photo-2.jpg`
66. Klik tombol `Bulk Action`
67. Klik pilihan `Delete`
68. Klik `[Delete]` pada dialog `Delete Files`
69. Verifikasi toast error `Error, failed to delete file.` tampil setelah permintaan bulk Delete gagal
70. Verifikasi Bulk Action Bar masih tampil setelah kegagalan 5xx
71. Verifikasi penghitung seleksi `2 Files selected` tetap tampil setelah kegagalan 5xx

### Bulk timeout mempertahankan bar dan seleksi
72. Tampilkan Tabel File Manager tab Files dengan kondisi K7
73. Centang baris `site-photo-1.jpg`
74. Centang baris `site-photo-2.jpg`
75. Klik tombol `Bulk Action`
76. Klik pilihan `Delete`
77. Klik `[Delete]` pada dialog `Delete Files`
78. Verifikasi toast error `Connection problem. Please try again.` tampil setelah permintaan bulk Delete kehabisan waktu
79. Verifikasi Bulk Action Bar masih tampil setelah timeout
80. Verifikasi penghitung seleksi `2 Files selected` tetap tampil setelah timeout

### Aktor Read Only memakai Download (ZIP)
81. Tampilkan Tabel File Manager tab Files dengan kondisi K8
82. Centang baris `site-photo-1.jpg`
83. Verifikasi Bulk Action Bar tampil bagi aktor Read Only
84. Klik tombol `Bulk Action`
85. Verifikasi menu Bulk Action memuat pilihan `Download (ZIP)` bagi aktor Read Only

### Select All di bawah Selection Limit
86. Tampilkan Tabel File Manager tab Files dengan kondisi K2
87. Centang baris `site-photo-1.jpg`
88. Verifikasi tombol `Select All (999 records)` tampil
89. Klik tombol `Select All (999 records)`
90. Verifikasi penghitung seleksi `999 Files selected` tampil
91. Verifikasi toast batas seleksi tidak tampil setelah Select All

### Select All tepat di Selection Limit
92. Tampilkan Tabel File Manager tab Files dengan kondisi K3
93. Centang baris `site-photo-1.jpg`
94. Verifikasi tombol `Select All (1000 records)` tampil
95. Klik tombol `Select All (1000 records)`
96. Verifikasi penghitung seleksi `1000 Files selected` tampil
97. Verifikasi toast batas seleksi tidak tampil setelah Select All yang tepat di batas

### Select All melebihi Selection Limit dipotong ke 1000 baris
98. Tampilkan Tabel File Manager tab Files dengan kondisi K4
99. Centang baris `site-photo-1.jpg`
100. Verifikasi tombol `Select All (1001 records)` tampil
101. Klik tombol `Select All (1001 records)`
102. Verifikasi penghitung seleksi `1000 Files selected` tampil setelah Select All dipotong ke batas
103. Verifikasi toast `Error, only the first 1000 of 1001 rows were selected. Narrow your filter to include the rest.` tampil
104. Verifikasi Bulk Action Bar tetap tampil setelah seleksi dipotong
105. Klik tombol `Bulk Action`
106. Verifikasi menu Bulk Action masih memuat pilihan `Download (ZIP)` setelah seleksi dipotong

### Checkbox baris ke-1001 diblok setelah limit tercapai
107. Tampilkan Tabel File Manager tab Files dengan kondisi K4
108. Centang baris `site-photo-1.jpg`
109. Klik tombol `Select All (1001 records)`
110. Isi kolom `Jump to page` dengan `101`
111. Tekan Enter
112. Verifikasi baris `site-photo-1001.jpg` tampil
113. Verifikasi checkbox baris `site-photo-1001.jpg` tidak dapat dicentang
114. Arahkan kursor ke checkbox baris `site-photo-1001.jpg`
115. Verifikasi teks `You've reached the maximum selection of 1000 rows.` tersampaikan pada checkbox baris `site-photo-1001.jpg`

### Select All atas hasil Search yang melebihi Selection Limit
116. Tampilkan Tabel File Manager tab Files dengan kondisi K5
117. Isi kotak Search dengan `survey`
118. Tekan Enter
119. Centang baris `survey-1.jpg`
120. Verifikasi tombol `Select All (1200 records)` tampil
121. Klik tombol `Select All (1200 records)`
122. Verifikasi penghitung seleksi `1000 Files selected` tampil setelah Select All atas hasil Search dipotong ke batas
123. Verifikasi toast `Error, only the first 1000 of 1200 rows were selected. Narrow your filter to include the rest.` tampil

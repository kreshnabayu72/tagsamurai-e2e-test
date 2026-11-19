---
id: TC-FA-MYASSET-UI-107-tabel-borrowed-seleksi-bulk
title: "Tabel Borrowed: seleksi baris, baris nonaktif beserta alasannya, Bulk Action Bar, dan Selection Limit"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-13", "FI-14", "FI-20", "FI-21", "V-01", "§4.1b#p6", "§5#r5", "§9.4.2#r44", "EB-BLK-1@tabel-borrowed", "EB-BLK-6"]
smoke: []
dependsOn: []
trace:
  "FI-13": [4, 6]
  "FI-14": [8, 10]
  "FI-20": [15, 17]
  "FI-21": [50, 51, 52, 54]
  "V-01": [4, 8, 17, 54]
  "§4.1b#p6": [2, 4, 8, 15, 17, 18, 39, 40, 41, 50, 109, 110, 111, 114, 119]
  "§5#r5": [24, 30, 35]
  "§9.4.2#r44": [8, 10]
  "EB-BLK-1@tabel-borrowed": [13, 14, 18, 22, 28, 33, 39, 42, 44, 47, 51, 55, 58, 61, 62, 64, 66, 68, 69, 72, 77, 78]
  "EB-BLK-6": [81, 83, 84, 86, 88, 91, 93, 94, 98, 99, 103, 105, 106]
anchor: [46, 57, 71, 76]
coverage:
  web: automated
---

# Tabel Borrowed: seleksi baris, baris nonaktif beserta alasannya, Bulk Action Bar, dan Selection Limit

## Prerequisites
- Aktor: Borrower (Budi Santoso, pengguna yang membuka halaman My Asset miliknya; juga PIC Borrower atas nama Borrower tanpa akun `Agus Pratama`).
- Layar awal: Halaman My Asset > tab Borrowed
- Komponen: Tabel Borrowed (T-MYA-02)
- Data:
  - DU-107-1: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 3`, Asset ID `LPT-2026-0003`, Status `Borrowed`, Borrower `Me`, Due Date `2026-11-12`, Pengajuan Extend `null`.
  - DU-107-2: respons tiruan, satu baris tabel Borrowed: Name `Meeting Mic Set - 2`, Asset ID `MIC-2026-0002`, Status `Borrowed`, Borrower `Me`, Due Date `2026-11-10`, Pengajuan Extend `null`.
  - DU-107-3: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 9`, Asset ID `LPT-2026-0009`, Status `Overdue`, Borrower `Me`, Due Date `2026-11-06`, Pengajuan Extend `null`.
  - DU-107-4: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 8`, Asset ID `LPT-2026-0008`, Status `Waiting for Approval`, Borrower `Me`, Due Date `null`, Pengajuan Extend `null`.
  - DU-107-5: respons tiruan, satu baris tabel Borrowed: Name `Projector Epson EB-X06 - 12`, Asset ID `PRJ-2026-0012`, Status `Waiting for Handover`, Borrower `Me`, Due Date `null`, Pengajuan Extend `null`.
  - DU-107-6: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 51`, Asset ID `LPT-2026-0051`, Status `Extension Request`, Borrower `Me`, Due Date `2026-11-11`, Pengajuan Extend `menunggu review`.
  - DU-107-7: respons tiruan, satu baris tabel Borrowed: Name `Tablet Samsung Galaxy Tab - 4`, Asset ID `TAB-2026-0004`, Status `Borrowed`, Borrower `Agus Pratama`, Due Date `2026-11-11`, Pengajuan Extend `null`, PIC `Budi Santoso`.
  - DU-107-8: respons tiruan, satu baris tabel Borrowed: Name `Tablet Samsung Galaxy Tab - 5`, Asset ID `TAB-2026-0005`, Status `Overdue`, Borrower `Agus Pratama`, Due Date `2026-11-08`, Pengajuan Extend `null`, PIC `Budi Santoso`.
  - DU-107-9: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Status `Extension Approval`, Borrower `Me`, Due Date `2026-11-11`, Pengajuan Extend `menunggu approval`.
  - DU-107-10: respons tiruan, 12 baris tabel Borrowed: Name `Laptop Pinjaman {n}`, Asset ID `LPJ-2026-{n}`, Status `Borrowed`, Borrower `Me`, Due Date `2026-12-01`, Pengajuan Extend `null`.
  - DU-107-11: respons tiruan, 1001 baris tabel Borrowed: Name `Laptop Kantor {n}`, Asset ID `LKT-2026-{n}`, Status `Borrowed`, Borrower `Me`, Due Date `2026-12-01`, Pengajuan Extend `null`.
  - DU-107-12: respons tiruan, 1000 baris tabel Borrowed: Name `Laptop Gudang {n}`, Asset ID `LGD-2026-{n}`, Status `Borrowed`, Borrower `Me`, Due Date `2026-12-01`, Pengajuan Extend `null`.
  - DU-107-13: respons tiruan, 999 baris tabel Borrowed: Name `Laptop Cabang {n}`, Asset ID `LCB-2026-{n}`, Status `Borrowed`, Borrower `Me`, Due Date `2026-12-01`, Pengajuan Extend `null`.
  - DU-107-14: respons tiruan, 1001 baris tabel Borrowed: Name `Laptop Regional Jakarta {n}`, Asset ID `LRJ-2026-{n}`, Status `Borrowed`, Borrower `Me`, Due Date `2026-12-01`, Pengajuan Extend `null`.
  - DU-107-15: respons tiruan, 199 baris tabel Borrowed: Name `Printer Regional Bandung {n}`, Asset ID `PRB-2026-{n}`, Status `Borrowed`, Borrower `Me`, Due Date `2026-12-01`, Pengajuan Extend `null`.
  - DU-107-16: respons tiruan, satu baris tabel Borrowed: Name `Laptop Dell Latitude 5420 - 18`, Asset ID `LPT-2026-0018`, Status `Borrowed`, Borrower `Me`, Due Date `2026-11-13`, Pengajuan Extend `null`.
  - Label tombol Select All yang diharapkan sesudah seluruh 3 baris yang dapat dipilih terpilih adalah `Unselect All (3 records)`, dari pola `Unselect All ([N] records)` dengan [N] sama dengan `3`.
  - Label tombol Select All yang diharapkan sesudah seluruh 12 baris yang dapat dipilih terpilih adalah `Unselect All (12 records)`, dari pola `Unselect All ([N] records)` dengan [N] sama dengan `12`.
  - Label tombol Select All yang diharapkan sesudah seluruh 1000 baris yang dapat dipilih terpilih adalah `Unselect All (1000 records)`, dari pola `Unselect All ([N] records)` dengan [N] sama dengan `1000`.
  - Label tombol Select All yang diharapkan sesudah seluruh 999 baris yang dapat dipilih terpilih adalah `Unselect All (999 records)`, dari pola `Unselect All ([N] records)` dengan [N] sama dengan `999`.
  - Label tombol Select All yang diharapkan sesudah satu-satunya baris yang dapat dipilih terpilih adalah `Unselect All (1 record)`, dari pola `Unselect All ([N] records)` dengan [N] sama dengan `1`, bentuk tunggal.
  - Label tombol Select All yang diharapkan saat hasil pencarian hanya memuat satu baris yang dapat dipilih dan dua baris terpilih adalah `Select All (1 record)`, dari pola `Select All ([N] records)` dengan [N] sama dengan `1`, bentuk tunggal.
- Kondisi:
  - K1: tabel Borrowed berisi DU-107-1 sampai DU-107-9 dengan urutan bawaan Due Date terdekat dulu.
  - K2: tabel Borrowed berisi DU-107-10, diurutkan menurut nomornya.
  - K3: sama dengan K1, dan pencarian `Meeting Mic Set` menghasilkan baris DU-107-2 saja.
  - K4: Selection Limit bernilai `1000`, dan tabel Borrowed berisi DU-107-11, diurutkan menurut nomornya.
  - K5: Selection Limit bernilai `1000`, dan tabel Borrowed berisi DU-107-12, diurutkan menurut nomornya.
  - K6: Selection Limit bernilai `1000`, dan tabel Borrowed berisi DU-107-13, diurutkan menurut nomornya.
  - K7: Selection Limit bernilai `1000`, tabel Borrowed berisi DU-107-14 dan DU-107-15 yang diurutkan menurut nomornya, dan pencarian `Regional Jakarta` menghasilkan DU-107-14 saja.
  - K8: tabel Borrowed berisi DU-107-8, DU-107-2, DU-107-1, dan DU-107-16 dengan urutan bawaan Due Date terdekat dulu.

## Test Steps

### Baris yang tidak memenuhi syarat Extend nonaktif dengan alasannya
1. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
2. Verifikasi checkbox baris `Laptop Dell Latitude 5420 - 8` disabled
3. Arahkan kursor ke checkbox baris `Laptop Dell Latitude 5420 - 8`
4. Verifikasi tooltip checkbox itu berisi `Only borrowed or overdue assets can be extended.`
5. Arahkan kursor ke checkbox baris `Projector Epson EB-X06 - 12`
6. Verifikasi tooltip checkbox itu berisi `Only borrowed or overdue assets can be extended.`
7. Arahkan kursor ke checkbox baris `Laptop Dell Latitude 5420 - 51`
8. Verifikasi tooltip checkbox itu berisi `An extension is already waiting.`
9. Arahkan kursor ke checkbox baris `Laptop Dell Latitude 5420 - 10`
10. Verifikasi tooltip checkbox itu berisi `An extension is already waiting.`

### Seleksi satu baris memunculkan Bulk Action Bar dan membatasi seleksi pada satu Borrower
11. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
12. Centang baris `Laptop Dell Latitude 5420 - 3`
13. Verifikasi counter seleksi di Bulk Action Bar menampilkan jumlah `1`
14. Verifikasi checkbox header berstatus indeterminate
15. Verifikasi checkbox baris `Tablet Samsung Galaxy Tab - 4` disabled
16. Arahkan kursor ke checkbox baris `Tablet Samsung Galaxy Tab - 4`
17. Verifikasi tooltip checkbox itu berisi `Select assets from one borrower only.`
18. Verifikasi tombol `Select All (3 records)` tampil di Bulk Action Bar, tanpa menghitung baris nonaktif

### Seleksi homogen Borrowed, homogen Overdue, dan campuran memakai Bulk Action Request Extension
19. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
20. Centang baris `Laptop Dell Latitude 5420 - 3`
21. Centang baris `Meeting Mic Set - 2`
22. Verifikasi counter seleksi di Bulk Action Bar menampilkan jumlah `2`
23. Klik `Bulk Action`
24. Verifikasi menu Bulk Action memuat tepat `Request Extension`
25. Tekan Esc untuk menutup menu Bulk Action
26. Klik `×` di Bulk Action Bar
27. Centang baris `Laptop Dell Latitude 5420 - 9`
28. Verifikasi counter seleksi di Bulk Action Bar menampilkan jumlah `1`
29. Klik `Bulk Action`
30. Verifikasi menu Bulk Action memuat tepat `Request Extension`
31. Tekan Esc untuk menutup menu Bulk Action
32. Centang baris `Laptop Dell Latitude 5420 - 3`
33. Verifikasi counter seleksi di Bulk Action Bar menampilkan jumlah `2`
34. Klik `Bulk Action`
35. Verifikasi menu Bulk Action memuat tepat `Request Extension`

### Select All memilih semua baris yang dapat dipilih milik Borrower yang sama
36. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
37. Centang baris `Laptop Dell Latitude 5420 - 9`
38. Klik `Select All (3 records)`
39. Verifikasi counter seleksi di Bulk Action Bar menampilkan jumlah `3`
40. Verifikasi baris `Laptop Dell Latitude 5420 - 3`, `Meeting Mic Set - 2`, dan `Laptop Dell Latitude 5420 - 9` tercentang
41. Verifikasi baris `Tablet Samsung Galaxy Tab - 4` dan `Tablet Samsung Galaxy Tab - 5` tidak tercentang
42. Verifikasi tombol `Unselect All (3 records)` tampil[^drift-1]
43. Hapus centang baris `Meeting Mic Set - 2`
44. Verifikasi tombol `Select All (3 records)` tampil kembali
45. Klik `×` di Bulk Action Bar
46. Verifikasi tabel Borrowed masih menampilkan baris `Laptop Dell Latitude 5420 - 3`
47. Verifikasi Bulk Action Bar tidak tampil

### Checkbox header memilih baris Borrower pertama menurut urutan tabel
48. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
49. Klik checkbox header tabel
50. Verifikasi baris `Laptop Dell Latitude 5420 - 9`, `Meeting Mic Set - 2`, dan `Laptop Dell Latitude 5420 - 3` tercentang
51. Verifikasi counter seleksi di Bulk Action Bar menampilkan jumlah `3`
52. Verifikasi baris `Tablet Samsung Galaxy Tab - 4` dan `Tablet Samsung Galaxy Tab - 5` tidak tercentang dan checkbox-nya disabled
53. Arahkan kursor ke checkbox baris `Tablet Samsung Galaxy Tab - 5`
54. Verifikasi tooltip checkbox itu berisi `Select assets from one borrower only.`
55. Verifikasi checkbox header berstatus checked
56. Klik checkbox header tabel
57. Verifikasi tabel Borrowed masih menampilkan baris `Laptop Dell Latitude 5420 - 3`
58. Verifikasi Bulk Action Bar tidak tampil

### Seleksi bertahan saat pindah halaman dan Select All melintasi halaman
59. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K2
60. Klik checkbox header tabel
61. Verifikasi counter seleksi di Bulk Action Bar menampilkan jumlah `10`
62. Verifikasi tombol `Select All (12 records)` tampil
63. Klik halaman `2` pada paginasi
64. Verifikasi counter seleksi di Bulk Action Bar menampilkan jumlah `10`
65. Centang baris `Laptop Pinjaman 11`
66. Verifikasi counter seleksi di Bulk Action Bar menampilkan jumlah `11`
67. Klik `Select All (12 records)`
68. Verifikasi counter seleksi di Bulk Action Bar menampilkan jumlah `12`
69. Verifikasi tombol `Unselect All (12 records)` tampil[^drift-1]
70. Klik `Unselect All (12 records)`[^drift-1]
71. Verifikasi tabel Borrowed masih menampilkan baris `Laptop Pinjaman 11`
72. Verifikasi Bulk Action Bar tidak tampil

### Seleksi bertahan saat baris terpilih tersaring keluar oleh Search
73. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K3
74. Centang baris `Laptop Dell Latitude 5420 - 3`
75. Ketik Search `Meeting Mic Set`, tekan Enter
76. Verifikasi tabel menampilkan baris `Meeting Mic Set - 2`
77. Verifikasi baris `Laptop Dell Latitude 5420 - 3` tidak tampil di tabel
78. Verifikasi counter seleksi di Bulk Action Bar menampilkan jumlah `1`

### Select All di atas Selection Limit dipotong dan checkbox sisanya diblok
79. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K4
80. Centang baris `Laptop Kantor 1`
81. Verifikasi tombol `Select All (1001 records)` tampil
82. Klik `Select All (1001 records)`
83. Verifikasi toast `Error, only the first 1000 of 1001 rows were selected. Narrow your filter to include the rest.` tampil
84. Verifikasi counter seleksi di Bulk Action Bar menampilkan jumlah `1000`
85. Klik halaman terakhir pada paginasi
86. Verifikasi checkbox baris `Laptop Kantor 1001` disabled
87. Arahkan kursor ke checkbox baris `Laptop Kantor 1001`
88. Verifikasi tooltip checkbox itu berisi `You've reached the maximum selection of 1000 rows.`

### Select All tepat di Selection Limit memilih semua baris tanpa toast batas
89. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K5
90. Centang baris `Laptop Gudang 1`
91. Verifikasi tombol `Select All (1000 records)` tampil
92. Klik `Select All (1000 records)`
93. Verifikasi counter seleksi di Bulk Action Bar menampilkan jumlah `1000`
94. Verifikasi tombol `Unselect All (1000 records)` tampil[^drift-1]

### Select All satu di bawah Selection Limit memilih semua baris tanpa toast batas
95. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K6
96. Centang baris `Laptop Cabang 1`
97. Klik `Select All (999 records)`
98. Verifikasi counter seleksi di Bulk Action Bar menampilkan jumlah `999`
99. Verifikasi tombol `Unselect All (999 records)` tampil[^drift-1]

### Select All atas hasil pencarian yang melebihi Selection Limit dipotong
100. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K7
101. Ketik Search `Regional Jakarta`, tekan Enter
102. Centang baris `Laptop Regional Jakarta 1`
103. Verifikasi tombol `Select All (1001 records)` tampil
104. Klik `Select All (1001 records)`
105. Verifikasi toast `Error, only the first 1000 of 1001 rows were selected. Narrow your filter to include the rest.` tampil
106. Verifikasi counter seleksi di Bulk Action Bar menampilkan jumlah `1000`

### Checkbox header memilih Borrower baris pertama menurut sort walau bukan milik sendiri dan bukan Borrower dengan baris terbanyak
107. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K8
108. Klik checkbox header tabel
109. Verifikasi baris `Tablet Samsung Galaxy Tab - 5` tercentang
110. Verifikasi counter seleksi di Bulk Action Bar menampilkan jumlah `1`
111. Verifikasi baris `Meeting Mic Set - 2`, `Laptop Dell Latitude 5420 - 3`, dan `Laptop Dell Latitude 5420 - 18` tidak tercentang dan checkbox-nya disabled

### Satu-satunya baris yang dapat dipilih memakai bentuk tunggal Unselect All
112. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K8
113. Klik checkbox header tabel
114. Verifikasi tombol `Unselect All (1 record)` tampil[^drift-1]

### Satu baris hasil pencarian memakai bentuk tunggal Select All
115. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K3
116. Centang baris `Laptop Dell Latitude 5420 - 3`
117. Centang baris `Laptop Dell Latitude 5420 - 9`
118. Ketik Search `Meeting Mic Set`, tekan Enter
119. Verifikasi tombol `Select All (1 record)` tampil

[^drift-1]: Drift PRD/foundation vs kontrak komponen. foundation `prd-conventions.md` §8: tombol berubah (toggle) menjadi `"Unselect All"` saat seluruh data terselect. Kontrak `BulkActionButton#11` dan `BulkActionButton#60`: begitu semua baris yang dapat dipilih terpilih, tombol berbunyi `Unselect All (N records)` (`Unselect All (1 record)` untuk N sama dengan 1, `BulkActionButton#41`), tepat ketika jumlah terpilih sama dengan N. Diasersi: kontrak komponen (SB-7), sehingga label memuat jumlah.

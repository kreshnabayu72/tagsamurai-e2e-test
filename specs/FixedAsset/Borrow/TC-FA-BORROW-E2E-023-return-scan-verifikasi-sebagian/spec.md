---
id: TC-FA-BORROW-E2E-023-return-scan-verifikasi-sebagian
title: "Halaman Return memilih Borrower dan aset, memverifikasi lewat scan, dan mengembalikan sebagian atau seluruh aset"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-BRW-109", "FI-BRW-115", "FI-BRW-116", "FI-BRW-117", "FI-BRW-118", "FI-BRW-126", "FI-BRW-127", "FI-BRW-128", "FI-BRW-129", "FI-BRW-130", "FI-BRW-131", "FI-BRW-132", "FI-BRW-146", "FI-BRW-147", "FI-BRW-148", "FI-BRW-149", "FI-BRW-92", "FI-BRW-93", "FI-BRW-94", "FI-BRW-95", "FI-BRW-96", "FI-BRW-97", "FI-BRW-98", "FI-BRW-99", "V-BRW-34", "V-BRW-35", "§4.2.6#p1", "§4.2.6#p2", "§4.4#r12"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-109": [56, 130, 136]
  "FI-BRW-115": [55, 118]
  "FI-BRW-116": 73
  "FI-BRW-117": 74
  "FI-BRW-118": [54, 72, 117]
  "FI-BRW-126": [33, 36, 95, 97]
  "FI-BRW-127": 38
  "FI-BRW-128": [46, 102, 148]
  "FI-BRW-129": [50, 106]
  "FI-BRW-130": [50, 106, 150]
  "FI-BRW-131": 61
  "FI-BRW-132": 56
  "FI-BRW-146": 54
  "FI-BRW-147": [59, 123]
  "FI-BRW-148": [57, 120]
  "FI-BRW-149": [58, 119, 128]
  "FI-BRW-92": 13
  "FI-BRW-93": 15
  "FI-BRW-94": [15, 17]
  "FI-BRW-95": 19
  "FI-BRW-96": 8
  "FI-BRW-97": [21, 26]
  "FI-BRW-98": 21
  "FI-BRW-99": 23
  "V-BRW-34": 25
  "V-BRW-35": [21, 23]
  "§4.2.6#p1": [8, 78]
  "§4.2.6#p2": [7, 9, 11, 80, 82, 100]
  "§4.4#r12": 21
anchor: [30, 145]
coverage:
  web: automated
---

# Halaman Return memilih Borrower dan aset, memverifikasi lewat scan, dan mengembalikan sebagian atau seluruh aset

## Prerequisites
- Aktor: `Agus Pratama {runId}`, Asset Admin (Aktor Borrow) pada Group `Head Office` saja; ia bukan Borrower maupun PIC pada BRW di spec ini.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-023-1: BRW Group `Head Office`, Borrower `Joko Widodo {runId}`, Photo at end OFF, berisi baris `Borrowed` aset DU-023-2, DU-023-3, DU-023-4, dan DU-023-5.
  - DU-023-2: aset `Laptop Acer Swift {runId}`, TAG `RFID`, Group `Head Office`.
  - DU-023-3: aset `Kamera Sony ZV {runId}`, TAG `QR` yang tidak dapat dipindai, Group `Head Office`; Note laporan TAG yang dicoba `Label TAG rusak terkena air`, Report Type `Unreadable`.
  - DU-023-4: aset `Tripod Velbon {runId}`, TAG `NFC`, Group `Head Office`.
  - DU-023-5: aset `Drone DJI Mini {runId}`, TAG `RFID`, Group `Head Office`, dengan laporan Damaged dari Borrower `Joko Widodo {runId}` berstatus `Waiting for Confirmation`.
  - DU-023-6: aset `Gimbal Zhiyun {runId}`, Group `Branch Surabaya`, baris `Borrowed` atas nama `Joko Widodo {runId}` pada BRW DU-023-9.
  - DU-023-7: aset `Monitor Dell {runId}`, Group `Head Office`, baris `Borrowed` atas nama `Kartika Sari {runId}` pada BRW DU-023-10.
  - DU-023-8: aset `Printer Epson {runId}`, Group `Head Office`, tidak sedang dipinjam.
  - DU-023-11: BRW Group `Head Office`, Borrower `Joko Widodo {runId}`, Photo at end OFF, berisi baris `Borrowed` aset DU-023-12.
  - DU-023-12: aset `Speaker Bose {runId}`, TAG `RFID`, Group `Head Office`.
  - DU-023-13: BRW Group `Head Office`, Borrower `Ratna Dewi {runId}`, Photo at end ON, berisi baris aset DU-023-14 `Overdue` serta DU-023-15, DU-023-16, dan DU-023-17 `Borrowed`.
  - DU-023-14: aset `Proyektor Optoma {runId}`, TAG `RFID`, Group `Head Office`, baris `Overdue`.
  - DU-023-15: aset `Speaker Anker {runId}`, TAG `QR`, Group `Head Office`.
  - DU-023-16: aset `Mikrofon Shure {runId}`, TAG `NFC`, Group `Head Office`; Note laporan TAG yang dicoba `TAG tertutup stiker`.
  - DU-023-17: aset `Kamera GoPro {runId}`, TAG `RFID`, Group `Head Office`.
  - Opsi Borrower `Ratna Dewi {runId}` pada field Borrower menampilkan `4 assets` (aset DU-023-14 sampai DU-023-17) dan `1 overdue` (aset DU-023-14).
  - Asset ID tiap aset dibentuk sistem dan menjadi milik entri aset itu.

## Test Steps

### Return dari Borrowed Assets mengisi Borrower dan aset otomatis
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Klik tab `Borrowed Assets`
4. Ketik Search `Laptop Acer Swift {runId}`, tekan Enter
5. Klik menu ⋯ pada baris aset DU-023-2
6. Klik `Return`
7. Verifikasi halaman `Return Asset` tampil dengan judul tanpa Transaction ID
8. Verifikasi field Borrower terisi `Joko Widodo {runId}` otomatis dan daftar aset memuat aset DU-023-2 dengan Verification `Unverified`
9. Verifikasi daftar aset baris DU-023-2 memuat kolom Photo, Name, Asset ID, Brand, Model/Type, TAG, Status, Transaction ID, Group, Due Return Date, Verification, dan Return Photo, dan footer memuat `[Cancel]` dan `[Submit]` tanpa `[Clear Field]`
10. Klik field Borrower
11. Verifikasi opsi `Joko Widodo {runId}` menampilkan `5 assets`, yaitu aset yang dapat diterima Aktor ini, tanpa aset Group `Branch Surabaya`
12. Tekan Esc untuk menutup daftar opsi Borrower

### Verify Asset menerapkan hasil scan langsung ke daftar
13. Verifikasi tombol `[Verify Asset]` tampil pada toolbar Return
14. Scan TAG aset DU-023-2 lewat `[Verify Asset]`
15. Verifikasi baris DU-023-2 `Verified` tanpa dialog tambahan
16. Scan TAG aset DU-023-2 lewat `[Verify Asset]`
17. Verifikasi daftar tetap memuat satu baris DU-023-2 `Verified` karena scan ulang diabaikan
18. Scan TAG aset DU-023-4 lewat `[Verify Asset]`
19. Verifikasi baris DU-023-4 ditambahkan langsung ke daftar dengan Verification `Verified`

### Scan ditolak dengan toast error dan daftar tidak berubah
20. Scan TAG aset DU-023-8 lewat `[Verify Asset]`
21. Verifikasi toast `Error, this asset isn't borrowed.` tampil
22. Scan TAG aset DU-023-7 lewat `[Verify Asset]`
23. Verifikasi toast `Error, this asset isn't borrowed by [Borrower].` tampil
24. Scan TAG aset DU-023-6 lewat `[Verify Asset]`
25. Verifikasi toast `Error, return this asset to [Group].` tampil dengan [Group] berisi `Branch Surabaya`
26. Verifikasi daftar tetap memuat hanya baris DU-023-2 dan DU-023-4 yang `Verified`

### I Can't Scan the TAG mewajibkan Return Photo
27. Klik `[+ Asset]`
28. Pilih aset DU-023-3 pada dialog Select Asset
29. Klik `[Select]`
30. Verifikasi baris DU-023-3 masuk ke daftar dengan Verification `Unverified`
31. Klik menu ⋯ pada baris DU-023-3
32. Klik `I Can't Scan the TAG`
33. Verifikasi dialog Report TAG tampil sebagai varian identifikasi manual, bukan varian biasa
34. Isi Note laporan dengan `Label TAG rusak terkena air`
35. Klik tombol kirim laporan pada dialog Report TAG
36. Verifikasi baris DU-023-3 menampilkan Verification `TAG Reported`
37. Klik `[Submit]`
38. Verifikasi ringkasan error `1 asset needs a return photo.` tampil di atas tombol karena Return Photo baris DU-023-3 wajib walau Photo at end OFF
39. Ambil foto pada kolom Return Photo baris DU-023-3

### Remove from List membuang baris tanpa dialog
40. Klik `[+ Asset]`
41. Pilih aset DU-023-5 pada dialog Select Asset
42. Klik `[Select]`
43. Scan TAG aset DU-023-5 lewat `[Verify Asset]`
44. Klik menu ⋯ pada baris DU-023-5
45. Klik `Remove from List`
46. Verifikasi baris DU-023-5 hilang dari daftar langsung tanpa dialog
47. Klik `[+ Asset]`
48. Pilih aset DU-023-5 pada dialog Select Asset
49. Klik `[Select]`
50. Verifikasi baris DU-023-5 kembali dengan Verification `Unverified` dan Return Photo kosong, tanpa status Verified dan foto sebelumnya
51. Klik menu ⋯ pada baris DU-023-5
52. Klik `Remove from List`

### Partial return: aset yang tidak ada di daftar tetap Borrowed
53. Klik `[Submit]`
54. Verifikasi tidak ada popup konfirmasi Borrower dan toast `Success, 3 assets have been returned.` langsung tampil
55. Verifikasi halaman Borrow Detail BRW milik DU-023-1 tampil karena semua aset yang dikembalikan berasal dari BRW itu
56. Verifikasi baris aset DU-023-2, DU-023-3, dan DU-023-4 `Returned` dan dikelompokkan pada BRW milik DU-023-1
57. Verifikasi baris aset DU-023-5 tetap `Borrowed`
58. Verifikasi status header BRW milik DU-023-1 tetap `Borrowed` karena masih ada baris aktif
59. Verifikasi Borrower pada header BRW tetap `Joko Widodo {runId}` sesuai BRW
60. Klik menu ⋯ pada baris aset DU-023-5
61. Verifikasi baris aset DU-023-5 tetap memuat badge `Reported Damaged` dan laporan Borrower tetap `Waiting for Confirmation`

### Return aset dari beberapa BRW kembali ke tab Borrowed Assets
62. Klik tab `Borrowed Assets`
63. Ketik Search `Drone DJI Mini {runId}`, tekan Enter
64. Klik menu ⋯ pada baris aset DU-023-5
65. Klik `Return`
66. Klik `[+ Asset]`
67. Pilih aset DU-023-12 pada dialog Select Asset
68. Klik `[Select]`
69. Scan TAG aset DU-023-5 lewat `[Verify Asset]`
70. Scan TAG aset DU-023-12 lewat `[Verify Asset]`
71. Klik `[Submit]`
72. Verifikasi toast `Success, 2 assets have been returned.` tampil
73. Verifikasi halaman kembali ke tab `Borrowed Assets` karena aset yang dikembalikan berasal dari lebih dari satu BRW
74. Verifikasi halaman tidak berpindah ke My Asset History karena Return dijalankan Aktor Borrow, bukan Borrower self-service

### Opsi Borrower, ganti Borrower, scan membatalkan Report TAG, dan Remove from List massal pada BRW dengan baris Overdue
75. Ketik Search `Ratna Dewi {runId}`, tekan Enter
76. Klik menu ⋯ pada baris aset DU-023-15
77. Klik `Return`
78. Verifikasi field Borrower terisi `Ratna Dewi {runId}` otomatis dan daftar aset memuat aset DU-023-15
79. Klik field Borrower
80. Verifikasi opsi `Ratna Dewi {runId}` menampilkan `4 assets` dan `1 overdue`
81. Pilih opsi `Kartika Sari {runId}` pada field Borrower
82. Verifikasi daftar aset kosong karena Borrower diganti
83. Klik field Borrower
84. Pilih opsi `Ratna Dewi {runId}` pada field Borrower
85. Klik `[+ Asset]`
86. Pilih aset DU-023-15 pada dialog Select Asset
87. Klik `[Select]`
88. Klik `[+ Asset]`
89. Pilih aset DU-023-16 pada dialog Select Asset
90. Klik `[Select]`
91. Klik menu ⋯ pada baris DU-023-16
92. Klik `I Can't Scan the TAG`
93. Isi Note laporan dengan `TAG tertutup stiker`
94. Klik tombol kirim laporan pada dialog Report TAG
95. Verifikasi baris DU-023-16 menampilkan Verification `TAG Reported`
96. Scan TAG aset DU-023-16 lewat `[Verify Asset]`
97. Verifikasi baris DU-023-16 `Verified` dan tidak lagi `TAG Reported`, karena scan berhasil membatalkan Report TAG dari identifikasi manual
98. Ambil foto pada kolom Return Photo baris DU-023-16
99. Centang baris DU-023-16
100. Verifikasi bulk action `Remove from List` tampil
101. Klik bulk action `Remove from List`
102. Verifikasi baris DU-023-16 hilang dari daftar langsung tanpa dialog
103. Klik `[+ Asset]`
104. Pilih aset DU-023-16 pada dialog Select Asset
105. Klik `[Select]`
106. Verifikasi baris DU-023-16 kembali dengan Verification `Unverified` dan Return Photo kosong, tanpa foto yang diambil sebelumnya
107. Klik menu ⋯ pada baris DU-023-16
108. Klik `Remove from List`

### Partial return dari BRW dengan baris Overdue: BRW tetap Borrowed dengan penanda Overdue
109. Klik `[+ Asset]`
110. Pilih aset DU-023-17 pada dialog Select Asset
111. Klik `[Select]`
112. Scan TAG aset DU-023-15 lewat `[Verify Asset]`
113. Scan TAG aset DU-023-17 lewat `[Verify Asset]`
114. Ambil foto pada kolom Return Photo baris DU-023-15
115. Ambil foto pada kolom Return Photo baris DU-023-17
116. Klik `[Submit]`
117. Verifikasi toast `Success, 2 assets have been returned.` tampil
118. Verifikasi halaman Borrow Detail BRW milik DU-023-13 tampil karena semua aset yang dikembalikan berasal dari BRW itu
119. Verifikasi status header BRW milik DU-023-13 tetap `Borrowed` dengan penanda `Overdue`, karena baris DU-023-14 masih aktif
120. Verifikasi baris aset DU-023-14 tetap `Overdue` dan baris aset DU-023-16 tetap `Borrowed`
121. Klik menu ⋯ pada baris aset DU-023-15
122. Klik `Borrow Log`
123. Verifikasi node Returned pada Borrow Log aset DU-023-15 mencatat Borrower yang sama dengan Borrower BRW milik DU-023-13

### Semua aset yang dikembalikan sekaligus berstatus Returned di BRW asalnya
124. Klik `Transactions` pada sidebar
125. Klik `Borrow`
126. Klik tab `History`
127. Ketik Search `Joko Widodo {runId}`, tekan Enter
128. Verifikasi BRW milik DU-023-1 dan BRW milik DU-023-11 tampil dengan Status `Returned`, sesudah semua baris aktifnya kembali
129. Buka Borrow Detail BRW milik DU-023-1 dari tabel History
130. Verifikasi baris aset DU-023-5 `Returned` pada BRW milik DU-023-1
131. Klik `Transactions` pada sidebar
132. Klik `Borrow`
133. Klik tab `History`
134. Ketik Search `Joko Widodo {runId}`, tekan Enter
135. Buka Borrow Detail BRW milik DU-023-11 dari tabel History
136. Verifikasi baris aset DU-023-12 `Returned` pada BRW milik DU-023-11

### Aset yang dikeluarkan dari daftar kembali lewat scan
137. Klik `Transactions` pada sidebar
138. Klik `Borrow`
139. Klik tab `Borrowed Assets`
140. Ketik Search `Proyektor Optoma {runId}`, tekan Enter
141. Klik menu ⋯ pada baris aset DU-023-14
142. Klik `Return`
143. Scan TAG aset DU-023-14 lewat `[Verify Asset]`
144. Ambil foto pada kolom Return Photo baris DU-023-14
145. Verifikasi baris DU-023-14 `Verified` dengan foto pada kolom Return Photo
146. Klik menu ⋯ pada baris DU-023-14
147. Klik `Remove from List`
148. Verifikasi baris DU-023-14 hilang dari daftar langsung tanpa dialog
149. Scan TAG aset DU-023-14 lewat `[Verify Asset]`
150. Verifikasi baris DU-023-14 kembali dengan Verification `Unverified` dan Return Photo kosong, tanpa status Verified dan foto sebelumnya

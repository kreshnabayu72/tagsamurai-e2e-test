---
id: TC-FA-MISS-E2E-031-report-missing-dep-asset
title: "Report Missing dari Asset List dan Asset Detail: record Missing dibuat, status global aset Missing, banner Asset Detail, dan Transaction log"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.1#r1", "§9.2#b1", "§9.2#b2", "§9.2#b4", "§9.2#b5", "§9.2#b6", "§9.2#b7", "§9.2#b9", "§9.2#b14", "§3#p2", "§4.4#r3", "§7.2#r1", "§7.3#r5", "§9.6#r1", "§9.7#r1", "§9.7#p1", "§8.1#r7", "§8#r6", "§8.2#b1", "§7.1#p3", "§4.3#r1", "§4.2.3#p1", "§4.2.3#b2", "§4.2.3#b3", "§4.2.3#b5", "§4.2.4#r13", "§4.2.4#r15", "§4.2.4#r16", "§9.9#r1", "§2#b2", "§2.1#r2", "§4.8#r2", "§9.4.2#r1", "§9.4.2#r16", "§9.4.4#r1", "§9.4.4#r2", "§1.2#r11", "§1.2#r12", "§1.2#r13", "§1.2#r14", "§1.2#r16", "§1.2#r23", "§1.2#r24", "§1.2#r25", "§1.2#r26", "§1.2#r31", "§1.2#r32", "§1.2#r39", "§1.2#r47", "§1.2#r53", "§9.2#r2", "§10#r1", "§10#r2", "§10#r6", "§11#r2", "EB-FB-1@report-missing", "EB-FRM-1@report-missing", "§9.8#r1", "§9.2#b12", "§9.2#b15", "§11#r1"]
smoke: []
dependsOn: ["Asset: Asset List > aksi baris Report Missing", "Asset: Asset Detail"]
trace:
  "§9.1#r1": [12, 24]
  "§9.2#b1": [68, 72]
  "§9.2#b2": [68]
  "§9.2#b4": [68]
  "§9.2#b5": [75, 80]
  "§9.2#b6": [72]
  "§9.2#b7": [95]
  "§9.2#b9": [28, 29, 37]
  "§9.2#b14": [30]
  "§3#p2": [24, 37]
  "§4.4#r3": [12]
  "§7.2#r1": [6]
  "§7.3#r5": [12, 53]
  "§9.6#r1": [12, 45, 95]
  "§9.7#r1": [37]
  "§9.7#p1": [39]
  "§8.1#r7": [32, 77, 83]
  "§8#r6": [77, 83]
  "§8.2#b1": [45]
  "§7.1#p3": [39, 40, 42]
  "§4.3#r1": [13]
  "§4.2.3#p1": [6]
  "§4.2.3#b2": [20, 68, 144]
  "§4.2.3#b3": [28]
  "§4.2.3#b5": [7, 69, 138]
  "§4.2.4#r13": [67]
  "§4.2.4#r15": [69, 138]
  "§4.2.4#r16": [7]
  "§9.9#r1": [9]
  "§2#b2": [24, 58]
  "§2.1#r2": [4]
  "§4.8#r2": [49]
  "§9.4.2#r1": [68]
  "§9.4.2#r16": [113]
  "§9.4.4#r1": [68, 95]
  "§9.4.4#r2": [32, 45]
  "§1.2#r11": [26, 27]
  "§1.2#r12": [75, 80]
  "§1.2#r13": [86, 109]
  "§1.2#r14": [20, 144]
  "§1.2#r16": [116, 121]
  "§1.2#r23": [24, 37]
  "§1.2#r24": [37]
  "§1.2#r25": [37, 54]
  "§1.2#r26": [37]
  "§1.2#r31": [37]
  "§1.2#r32": [40]
  "§1.2#r39": [59, 81]
  "§1.2#r47": [38]
  "§1.2#r53": [58, 59]
  "§9.2#r2": [24]
  "§10#r1": [75, 80]
  "§10#r2": [86, 95, 104]
  "§10#r6": [126, 132]
  "§11#r2": [39, 45]
  "EB-FB-1@report-missing": [12]
  "EB-FRM-1@report-missing": [25]
  "§9.8#r1": [12]
  "§9.2#b12": [112, 113]
  "§9.2#b15": [104, 105, 110]
  "§11#r1": [37]
anchor: [2, 16, 137, 143]
coverage:
  web: automated
---

# Report Missing dari Asset List dan Asset Detail: record Missing dibuat, status global aset Missing, banner Asset Detail, dan Transaction log

## Prerequisites
- Aktor: Total Control `Rina W`. Aktor lain yang memicu perubahan: Total Control `Dewi Anggraini {runId}`.
- Layar awal: Assets > Assets.
- Data:
  - DU-031-1: Asset `Laptop Dell Latitude 5420 {runId}`, Group `Finance Room`, TAG QR yang belum pernah terpindai, Activity Lock `Under Maintenance`, tanpa pemegang, tanpa record Missing.
  - DU-031-2: Asset `Hand Pallet Truck {runId}`, Group `Warehouse`, dipegang `Rina W`, tanpa record Missing.
  - DU-031-3: Asset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, tanpa pemegang, tanpa record Missing.
  - DU-031-4: Asset `Monitor LG 27UL500 {runId}`, Group `Head Office`, dipegang `Sari Dewanti {runId}`, tanpa record Missing.
  - DU-031-5: Asset `Projector Epson EB-X06 {runId}`, Group `Branch Surabaya`, sudah punya satu record Missing berjalan yang dilaporkan `Rina W`.
  - DU-031-6: Asset `Toyota Innova {runId}`, Group `Branch Surabaya`, sudah punya satu record Missing berjalan dengan Last holder `Budi Santoso {runId}`, pengguna yang sudah dinonaktifkan.
  - DU-031-7: Asset `Server Dell PowerEdge {runId}`, Group `Head Office`, tanpa pemegang, tanpa record Missing.
  - DU-031-8: Asset `Meja Rapat Kayu {runId}`, Group `Head Office`, Asset Status `Unmanaged`, tanpa record Missing.
  - DU-031-9: Asset `Camera Canon EOS {runId}`, Group `Head Office`, punya satu record yang sudah selesai berstatus `Found`.
  - DU-031-10: Pengguna `Dewi Anggraini {runId}`, Total Control.
  - DU-031-11: What happened `Laptop tidak ditemukan saat pengecekan pagi di ruang Finance`.
  - DU-031-12: What happened `Hand pallet truck tidak kembali ke gudang setelah dipakai`.
  - DU-031-13: What happened `Printer dan monitor tidak ada di ruang kerja setelah renovasi`.
  - DU-031-14: What happened `Pengecekan ulang aset yang sudah dilaporkan hilang`.
  - DU-031-15: What happened `Server tidak ditemukan di rak setelah pemindahan ruang server`, dilaporkan `Dewi Anggraini {runId}`.
  - DU-031-16: What happened `Server tidak ada di ruang server saat inventarisasi`.
  - DU-031-17: Asset `Forklift Toyota 8FD {runId}`, Group `Warehouse`, dipegang `Rina W`, tanpa record Missing.
- Kondisi:
  - Date Format bernilai `DD/MM/YY`.
  - Time Format bernilai `HH:mm`.

## Test Steps

### Report Missing satu aset dari Asset List dan toast hasilnya
1. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
2. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil pada Asset List
3. Buka menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
4. Verifikasi aksi `Report Missing` tampil pada menu
5. Klik `Report Missing`
6. Verifikasi dialog berjudul `Report Missing` memuat satu isian `What happened`
7. Verifikasi kotak dampak memuat baris `The asset admins will be notified.`
8. Klik `[Report Missing]` pada dialog tanpa mengisi What happened
9. Verifikasi caption `What happened must not be empty` tampil di bawah isian What happened
10. Isi What happened `Laptop tidak ditemukan saat pengecekan pagi di ruang Finance`
11. Klik `[Report Missing]` pada dialog
12. Verifikasi toast `Success, asset has been reported missing.` tampil
13. Verifikasi badge tab `Missing` tampil dengan jumlah minimal `1`

### Aksi Report Missing hilang pada aset yang sudah dilaporkan
14. Ganti isi kotak search dengan `Printer HP LaserJet M404 {runId}`, tekan Enter
15. Buka menu `⋯` pada baris `Printer HP LaserJet M404 {runId}`
16. Verifikasi aksi `Report Missing` tampil pada menu
17. Tutup menu `⋯` dengan tombol Esc
18. Ganti isi kotak search dengan `Laptop Dell Latitude 5420 {runId}`, tekan Enter
19. Buka menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
20. Verifikasi aksi `Report Missing` tidak tampil pada menu
21. Tutup menu `⋯` dengan tombol Esc

### Record Missing tampil di tab Missing dengan kolom terisi
22. Klik tab `Missing`
23. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
24. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` berstatus `Missing`
25. Verifikasi hasil Search `Laptop Dell Latitude 5420 {runId}` hanya satu baris
26. Verifikasi kolom Reported By pada baris itu `Rina W`
27. Verifikasi kolom Reported Date pada baris itu memuat tanggal dan jam laporan menurut Date Format dan Time Format di Kondisi
28. Verifikasi kolom Last Seen pada baris itu `Unknown`
29. Verifikasi kolom Last Holder pada baris itu `—`
30. Verifikasi kolom Source pada baris itu terisi
31. Klik `Laptop Dell Latitude 5420 {runId}` pada kolom Name
32. Verifikasi dialog Missing Log memuat node `Reported missing by` oleh `Rina W` dengan What happened `Laptop tidak ditemukan saat pengecekan pagi di ruang Finance`
33. Tutup dialog Missing Log dengan `✕`

### Status global aset, banner, dan Transaction log di Asset Detail
34. Klik tab `Assets`
35. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
36. Klik `Laptop Dell Latitude 5420 {runId}` pada kolom Name
37. Verifikasi Asset Status pada Asset Detail `Missing`
38. Verifikasi Activity Lock `Under Maintenance` tetap tampil pada Asset Detail
39. Verifikasi banner `Reported missing on` tampil dengan tanggal laporan menurut Date Format di Kondisi
40. Verifikasi alasan `This asset is reported missing.` tersampaikan pada tombol transaksi yang disabled
41. Klik `[View]` pada banner
42. Verifikasi dialog `Missing Log` terbuka untuk record `Laptop Dell Latitude 5420 {runId}`
43. Tutup dialog Missing Log dengan `✕`
44. Buka Transaction log pada Asset Detail
45. Verifikasi entri `Reported missing` tampil di Transaction log

### Report Missing dari Asset Detail oleh pelapor yang juga pemegang aset
46. Buka halaman `Assets`
47. Ketik Search `Hand Pallet Truck {runId}`, tekan Enter
48. Klik `Hand Pallet Truck {runId}` pada kolom Name
49. Verifikasi tombol `[Report Missing]` tampil pada Asset Detail
50. Klik `[Report Missing]` pada Asset Detail
51. Isi What happened `Hand pallet truck tidak kembali ke gudang setelah dipakai`
52. Klik `[Report Missing]` pada dialog
53. Verifikasi toast `Success, asset has been reported missing.` tampil
54. Verifikasi Asset Status pada Asset Detail `Missing`
55. Buka halaman `Assets`
56. Klik tab `Missing`
57. Ketik Search `Hand Pallet Truck {runId}`, tekan Enter
58. Verifikasi baris `Hand Pallet Truck {runId}` berstatus `Missing`
59. Verifikasi kolom Last Holder pada baris itu `Rina W`

### Report Missing banyak aset: aset yang sudah dilaporkan dilewati
60. Klik tab `Assets`
61. Ketik Search `{runId}`, tekan Enter
62. Atur jumlah baris per halaman menjadi `100`
63. Centang baris `Printer HP LaserJet M404 {runId}`
64. Centang baris `Monitor LG 27UL500 {runId}`
65. Centang baris `Projector Epson EB-X06 {runId}`
66. Klik `Report Missing` pada bar aksi bulk
67. Verifikasi judul dialog `Report Missing Assets`
68. Verifikasi `Projector Epson EB-X06 {runId}` tampil dengan keterangan `Already reported missing` dan tautan ke Missing Log
69. Verifikasi kotak dampak memuat baris yang menyebut pemegang `Sari Dewanti {runId}` diikuti `and the asset admins will be notified.`
70. Isi What happened `Printer dan monitor tidak ada di ruang kerja setelah renovasi`
71. Klik `[Report Missing]` pada dialog
72. Verifikasi toast `Success, asset has been reported missing. Some items were skipped.` tampil

### Satu record dan satu node per aset sesudah laporan banyak aset
73. Klik tab `Missing`
74. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
75. Verifikasi baris `Printer HP LaserJet M404 {runId}` berstatus `Missing`
76. Klik `Printer HP LaserJet M404 {runId}` pada kolom Name
77. Verifikasi dialog Missing Log memuat node `Reported missing by` oleh `Rina W` dengan What happened `Printer dan monitor tidak ada di ruang kerja setelah renovasi`
78. Tutup dialog Missing Log dengan `✕`
79. Ganti isi kotak search dengan `Monitor LG 27UL500 {runId}`, tekan Enter
80. Verifikasi baris `Monitor LG 27UL500 {runId}` berstatus `Missing`
81. Verifikasi kolom Last Holder pada baris itu `Sari Dewanti {runId}`
82. Klik `Monitor LG 27UL500 {runId}` pada kolom Name
83. Verifikasi dialog Missing Log memuat node `Reported missing by` oleh `Rina W` dengan What happened `Printer dan monitor tidak ada di ruang kerja setelah renovasi`
84. Tutup dialog Missing Log dengan `✕`
85. Ganti isi kotak search dengan `Projector Epson EB-X06 {runId}`, tekan Enter
86. Verifikasi hasil Search `Projector Epson EB-X06 {runId}` hanya satu baris

### Semua aset terpilih sudah dilaporkan sehingga tidak ada yang berhasil
87. Klik tab `Assets`
88. Ketik Search `{runId}`, tekan Enter
89. Atur jumlah baris per halaman menjadi `100`
90. Centang baris `Projector Epson EB-X06 {runId}`
91. Centang baris `Toyota Innova {runId}`
92. Klik `Report Missing` pada bar aksi bulk
93. Isi What happened `Pengecekan ulang aset yang sudah dilaporkan hilang`
94. Klik `[Report Missing]` pada dialog
95. Verifikasi dialog tetap terbuka dengan `Projector Epson EB-X06 {runId}` dan `Toyota Innova {runId}` masing-masing berketerangan `Already reported missing`
96. Klik `[Cancel]` pada dialog

### Dua laporan bersamaan atas aset yang sama
97. Muat ulang halaman
98. Ketik Search `Server Dell PowerEdge {runId}`, tekan Enter
99. Buka menu `⋯` pada baris `Server Dell PowerEdge {runId}`
100. Klik `Report Missing`
101. Dewi Anggraini {runId} melaporkan `Server Dell PowerEdge {runId}` hilang dengan What happened `Server tidak ditemukan di rak setelah pemindahan ruang server`
102. Isi What happened `Server tidak ada di ruang server saat inventarisasi`
103. Klik `[Report Missing]` pada dialog
104. Verifikasi Alert pada dialog menyebut `Server Dell PowerEdge {runId}` dan `Dewi Anggraini {runId}` dengan teks `was just reported missing by`
105. Verifikasi tombol `[View Missing Log]` tampil pada Alert
106. Klik `[Cancel]` pada dialog
107. Klik tab `Missing`
108. Ketik Search `Server Dell PowerEdge {runId}`, tekan Enter
109. Verifikasi hasil Search `Server Dell PowerEdge {runId}` hanya satu baris
110. Verifikasi kolom Reported By pada baris itu `Dewi Anggraini {runId}`

### Last holder yang sudah dinonaktifkan tetap tercatat pada record
111. Ganti isi kotak search dengan `Toyota Innova {runId}`, tekan Enter
112. Verifikasi baris `Toyota Innova {runId}` berstatus `Missing`
113. Verifikasi kolom Last Holder pada baris itu `Budi Santoso {runId}`

### Record yang sudah selesai tetap terlihat di History dan Asset Detail
114. Klik sub-tab `History`
115. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
116. Verifikasi baris `Camera Canon EOS {runId}` berstatus `Found`
117. Klik tab `Assets`
118. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
119. Klik `Camera Canon EOS {runId}` pada kolom Name
120. Buka Transaction log pada Asset Detail
121. Verifikasi entri `Marked as found` tampil di Transaction log

### Delete Asset Data atas aset dengan record berjalan ditolak
122. Buka halaman `Assets`
123. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
124. Buka menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
125. Klik `Delete Asset Data`
126. Verifikasi penghapusan ditolak dan baris `Laptop Dell Latitude 5420 {runId}` tetap tampil di Asset List
127. Ganti isi kotak search dengan `{runId}`, tekan Enter
128. Atur jumlah baris per halaman menjadi `100`
129. Centang baris `Laptop Dell Latitude 5420 {runId}`
130. Centang baris `Meja Rapat Kayu {runId}`
131. Klik `Delete Asset Data` pada bar aksi bulk
132. Verifikasi penghapusan ditolak seluruhnya dan baris `Meja Rapat Kayu {runId}` tetap tampil di Asset List

### Laporan atas aset yang dipegang pelapor tidak menyebut pemegang di kotak dampak
133. Buka halaman `Assets`
134. Ketik Search `Forklift Toyota 8FD {runId}`, tekan Enter
135. Klik `Forklift Toyota 8FD {runId}` pada kolom Name
136. Klik `[Report Missing]` pada Asset Detail
137. Verifikasi dialog berjudul `Report Missing` memuat satu isian `What happened`
138. Verifikasi kotak dampak tidak memuat baris yang menyebut pemegang `Rina W` diikuti `and the asset admins will be notified.`
139. Klik `[Cancel]` pada dialog

### Tombol Report Missing tidak tampil pada Asset Detail aset yang sudah dilaporkan
140. Buka halaman `Assets`
141. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
142. Klik `Laptop Dell Latitude 5420 {runId}` pada kolom Name
143. Verifikasi banner `Reported missing on` tampil pada Asset Detail
144. Verifikasi tombol `[Report Missing]` tidak tampil pada Asset Detail

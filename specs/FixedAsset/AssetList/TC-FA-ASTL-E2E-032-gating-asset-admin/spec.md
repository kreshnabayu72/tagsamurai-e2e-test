---
id: TC-FA-ASTL-E2E-032-gating-asset-admin
title: "Gating UI untuk Asset Admin"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-10k", "ASTL-LOGIC-10l", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§2#r1", "§2#r2", "§2#r3", "§2#r4", "§2#r5", "§2#r6", "§2#r7", "§2#r8", "§2#r9", "§2#r10", "§2#r11", "§2#r12", "§2#r13", "§2#r14", "§2#r15", "§2#r16", "§2#p3", "§9.11#r1", "§9.11#r2", "§9.11#r3", "§9.11#r4", "§9.11#r5", "§9.11#r6", "§9.11#r7"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-10k": [38, 39, 40, 41, 42, 43]
  "ASTL-LOGIC-10l": [39, 43]
  "§4.8#r1": [4, 5, 9, 21]
  "§4.8#r2": [10, 11, 27, 63, 64, 68, 69, 81, 82, 86, 87, 95, 101, 102, 105, 106, 110, 115, 122, 123, 126, 127, 131, 136]
  "§4.8#r3": 12
  "§4.8#r4": 13
  "§4.8#r5": [14, 56]
  "§4.8#r6": [22, 74]
  "§4.8#r7": [16, 74]
  "§4.8#r8": 17
  "§4.8#r9": 15
  "§4.8#r10": 25
  "§4.8#r11": 28
  "§4.8#r12": [18, 29]
  "§4.8#r13": [6, 7]
  "§4.8#r14": [38, 39, 40, 41, 42, 43]
  "§2#r1": [14, 15, 16, 22]
  "§2#r2": [38, 39]
  "§2#r3": [18, 29, 42, 43]
  "§2#r4": [12, 38, 39, 40, 41]
  "§2#r5": [2, 3, 4, 5, 7, 9, 14, 16, 21, 38, 39]
  "§2#r6": [2, 3, 4, 5, 7, 9, 14, 16, 21, 38, 39]
  "§2#r7": [2, 3, 4, 5, 7, 9, 14, 16, 21, 38, 39]
  "§2#r8": [2, 3, 4, 5, 7, 9, 14, 16, 21, 38, 39]
  "§2#r9": [2, 3, 4, 5, 7, 9, 14, 16, 21, 38, 39]
  "§2#r10": [2, 3, 4, 5, 7, 9, 14, 16, 21, 38, 39]
  "§2#r11": [2, 3, 4, 5, 7, 9, 14, 16, 21, 38, 39]
  "§2#r12": [2, 3, 4, 5, 7, 9, 14, 16, 21, 38, 39]
  "§2#r13": [2, 3, 4, 5, 7, 9, 14, 16, 21, 38, 39]
  "§2#r14": [2, 3, 4, 5, 7, 9, 14, 16, 21, 38, 39]
  "§2#r15": [2, 3, 4, 5, 7, 9, 14, 16, 21, 38, 39]
  "§2#r16": [2, 3, 4, 5, 7, 9, 14, 16, 21, 38, 39]
  "§2#p3": [2, 3, 7, 14, 16]
  "§9.11#r1": [2, 3, 7]
  "§9.11#r2": [38, 39]
  "§9.11#r3": [34, 42, 43]
  "§9.11#r4": 35
  "§9.11#r5": [40, 41]
  "§9.11#r6": 48
  "§9.11#r7": 51
anchor: [33, 45, 47, 50]
coverage:
  web: automated
---

# Gating UI untuk Asset Admin

## Prerequisites
- Aktor: `Eko Pratama {runId}`, pemegang role Asset Admin (Role Transaksi, jenis Borrow) dengan cakupan Group `IT {runId}` beserta descendant.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-032-1: User, Name `Eko Pratama {runId}`, Role `Asset Admin`, Cakupan `Group IT {runId} beserta descendant`
  - DU-032-2: Group, Name `IT {runId}`
  - DU-032-3: Group, Name `Cabang Bandung {runId}`
  - DU-032-4: Asset, Name `Laptop Pro 16 {runId}`, Group `IT {runId}`, Status `Available`, TAG `RFID` berstatus `Paired`, Asset Class `Peralatan IT {runId}`, Tax Depreciation Class `Kelompok 1 {runId}`, Purchase Date `T0 − 30 hari`, Purchase Cost `18500000`, Warranty Until `T0 + 200 hari`
  - DU-032-5: Asset, Name `Kursi Kerja {runId}`, Group `IT {runId}`, Status `Available`
  - DU-032-6: Asset, Name `Kamera Mirrorless {runId}`, Group `IT {runId}`, Status `Available`, License `Unmanaged`
  - DU-032-7: Asset, Name `Printer Laser {runId}`, Group `Cabang Bandung {runId}`, Status `Available`
  - DU-032-8: Custom Field, Name `Nomor PO {runId}`, Group `Purchasing`
  - DU-032-9: Custom Field, Name `Kode Anggaran {runId}`, Group `Accounting`
  - DU-032-10: Asset, Name `Proyektor Pinjam {runId}`, Group `IT {runId}`, Status `Borrowed`
  - DU-032-11: Asset, Name `Laptop Tugas {runId}`, Group `IT {runId}`, Status `Assigned`
  - Nama baris yang diharapkan untuk Asset Name `Laptop Pro 16 {runId}` adalah `Laptop Pro 16 {runId} - 1`, dari Asset Name `Laptop Pro 16 {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kursi Kerja {runId}` adalah `Kursi Kerja {runId} - 1`, dari Asset Name `Kursi Kerja {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kamera Mirrorless {runId}` adalah `Kamera Mirrorless {runId} - 1`, dari Asset Name `Kamera Mirrorless {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Printer Laser {runId}` adalah `Printer Laser {runId} - 1`, dari Asset Name `Printer Laser {runId}`.
  - Purchase Cost yang diharapkan untuk Purchase Cost `18500000` adalah `Rp 18.500.000,00`, dari Purchase Cost `18500000`.
  - Kursi Kerja {runId} tidak memiliki Purchase Information dan Asset Name-nya tanpa Asset Class; Kamera Mirrorless {runId} adalah aset Unmanaged.
  - Aset `Laptop Pro 16 {runId}` dan `Kursi Kerja {runId}` tercatat di group `IT {runId}`; user hanya mengakses group yang sesuai cakupannya.
  - Nama baris yang diharapkan untuk Asset Name `Proyektor Pinjam {runId}` adalah `Proyektor Pinjam {runId} - 1`, dari Asset Name `Proyektor Pinjam {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Laptop Tugas {runId}` adalah `Laptop Tugas {runId} - 1`, dari Asset Name `Laptop Tugas {runId}`.
  - `Proyektor Pinjam {runId}` sedang dipinjam (Custody `Borrowed`) dan `Laptop Tugas {runId}` sedang ditugaskan (Custody `Assigned`).
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Lisensi `FA-7` aktif pada entitas.
  - Feature Suite Borrow, Assignment, dan Transfer berada di level `Full`.

## Test Steps

### Tabel, kartu, dan cakupan group tampil sesuai hak
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Laptop Pro 16 {runId} - 1`, `Kursi Kerja {runId} - 1`, dan `Kamera Mirrorless {runId} - 1` tampil di tabel
3. Verifikasi baris `Printer Laser {runId} - 1` tidak tampil di tabel
4. Verifikasi tabel dan kartu status `All` tampil
5. Verifikasi ikon `Changelog` dan tombol `Download` tampil di toolbar
6. Verifikasi Sidebar Group tampil dengan node `All Groups`
7. Verifikasi Sidebar Group memuat node `IT {runId}` dan tidak memuat node `Cabang Bandung {runId}`

### Aksi baris pada aset Available
8. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
9. Verifikasi aksi `Detail` tampil
10. Verifikasi aksi `Borrow` dan `Add to Borrow Draft` tampil
11. Verifikasi aksi `Assign`, `Add to Assignment Draft`, `Transfer`, dan `Add to Transfer Draft` tidak dirender (Hidden)
12. Verifikasi aksi `Report Disposal` tidak dirender (Hidden)
13. Verifikasi aksi `Report Damage` dan `Report Missing` tidak dirender (Hidden)
14. Verifikasi aksi `Edit` dan `Replace TAG` tidak dirender (Hidden)
15. Verifikasi aksi `Print Label` tidak dirender (Hidden)
16. Verifikasi aksi `Delete Asset Data` tidak dirender (Hidden)
17. Verifikasi aksi `Report TAG` tampil
18. Verifikasi aksi `Edit Purchase` tidak dirender (Hidden)
19. Tekan Esc

### Aksi Manage pada aset Unmanaged
20. Klik `⋯` pada baris `Kamera Mirrorless {runId} - 1`
21. Verifikasi aksi `Detail` tampil
22. Verifikasi aksi `Manage` tidak dirender (Hidden)
23. Tekan Esc

### Checkbox baris, Bar Bulk, dan aksi Bulk
24. Centang baris `Laptop Pro 16 {runId} - 1`
25. Verifikasi checkbox baris dan Bar Bulk tampil
26. Klik tombol Bulk Action
27. Verifikasi aksi Bulk `Borrow` dan `Add to Borrow Draft` tampil
28. Verifikasi aksi Bulk `Print Label`, `Add Label`, dan `Remove Label` tidak dirender (Hidden)
29. Verifikasi aksi Bulk `Edit Purchase` tidak dirender (Hidden)
30. Tekan Esc
31. Klik `×` pada Bar Bulk

### Setup Column dan sel kolom bergerbang
32. Buka Setup Column
33. Verifikasi kolom `Asset Value (Commercial)`, `Asset Class`, `Tax Depreciation Class`, `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry` tersedia di Setup Column
34. Verifikasi kolom custom field Purchasing `Nomor PO {runId}` tidak tersedia di Setup Column
35. Verifikasi kolom custom field Accounting `Kode Anggaran {runId}` tidak tersedia di Setup Column
36. Tampilkan kolom `Asset Value (Commercial)`, `Asset Class`, `Tax Depreciation Class`, `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry`
37. Tutup Setup Column
38. Verifikasi sel `Asset Value (Commercial)` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
39. Verifikasi sel `Asset Value (Commercial)` baris `Kursi Kerja {runId} - 1` menampilkan `No access`, bukan `Pending`
40. Verifikasi sel `Asset Class` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
41. Verifikasi sel `Tax Depreciation Class` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
42. Verifikasi sel `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
43. Verifikasi sel `Purchase Date` dan `Purchase Cost` baris `Kursi Kerja {runId} - 1` menampilkan `No access`, bukan `Pending`

### Dokumen Purchase dan data Accounting di Asset Detail
44. Klik Name `Laptop Pro 16 {runId} - 1`
45. Verifikasi halaman detail aset `Laptop Pro 16 {runId} - 1` terbuka bagi `Eko Pratama {runId}`
46. Buka tab `Documents`
47. Verifikasi tab `Documents` terbuka bagi `Eko Pratama {runId}`
48. Verifikasi kelompok Purchase pada tab `Documents` tidak tampil
49. Buka tab `Accounting`
50. Verifikasi tab `Accounting` terbuka bagi `Eko Pratama {runId}`
51. Verifikasi data tab `Accounting` (peringatan fisik vs buku, Depreciation, Acquisition & Value changes, Journals) tidak tampil
52. Muat ulang halaman
53. Ketik Search `{runId}`, tekan Enter

### Batch Replace TAG tidak ditawarkan pada Bar Bulk
54. Centang baris `Laptop Pro 16 {runId} - 1`
55. Klik tombol Bulk Action
56. Verifikasi aksi Bulk `Batch Replace TAG` tidak dirender (Hidden)
57. Tekan Esc
58. Klik `×` pada Bar Bulk

### Hak diubah menjadi Asset Admin jenis Transfer
59. Admin mengubah hak `Eko Pratama {runId}` pada group `IT {runId}` menjadi `Asset Admin` jenis `Transfer`
60. Muat ulang halaman
61. Ketik Search `{runId}`, tekan Enter
62. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
63. Verifikasi aksi `Transfer` dan `Add to Transfer Draft` tampil
64. Verifikasi aksi `Borrow`, `Add to Borrow Draft`, `Assign`, dan `Add to Assignment Draft` tidak dirender (Hidden)
65. Tekan Esc

### Aksi Bulk bagi Asset Admin jenis Transfer
66. Centang baris `Laptop Pro 16 {runId} - 1`
67. Klik tombol Bulk Action
68. Verifikasi aksi Bulk `Transfer` dan `Add to Transfer Draft` tampil
69. Verifikasi aksi Bulk `Borrow`, `Add to Borrow Draft`, `Assign`, dan `Add to Assignment Draft` tidak dirender (Hidden)
70. Tekan Esc
71. Klik `×` pada Bar Bulk
72. Centang baris `Kamera Mirrorless {runId} - 1`
73. Klik tombol Bulk Action
74. Verifikasi aksi Bulk `Manage` dan `Delete Asset Data` tidak dirender (Hidden)
75. Tekan Esc
76. Klik `×` pada Bar Bulk

### Hak diubah menjadi Asset Admin jenis Assignment
77. Admin mengubah hak `Eko Pratama {runId}` pada group `IT {runId}` menjadi `Asset Admin` jenis `Assignment`
78. Muat ulang halaman
79. Ketik Search `{runId}`, tekan Enter
80. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
81. Verifikasi aksi `Assign` dan `Add to Assignment Draft` tampil
82. Verifikasi aksi `Borrow`, `Add to Borrow Draft`, `Transfer`, dan `Add to Transfer Draft` tidak dirender (Hidden)
83. Tekan Esc
84. Centang baris `Laptop Pro 16 {runId} - 1`
85. Klik tombol Bulk Action
86. Verifikasi aksi Bulk `Assign` dan `Add to Assignment Draft` tampil
87. Verifikasi aksi Bulk `Borrow`, `Add to Borrow Draft`, `Transfer`, dan `Add to Transfer Draft` tidak dirender (Hidden)
88. Tekan Esc
89. Klik `×` pada Bar Bulk

### Hak dikembalikan menjadi Asset Admin jenis Borrow
90. Admin mengubah hak `Eko Pratama {runId}` pada group `IT {runId}` menjadi `Asset Admin` jenis `Borrow`
91. Muat ulang halaman
92. Ketik Search `{runId}`, tekan Enter
93. Centang baris `Laptop Pro 16 {runId} - 1`
94. Klik tombol Bulk Action
95. Verifikasi aksi Bulk `Assign`, `Add to Assignment Draft`, `Transfer`, dan `Add to Transfer Draft` tidak dirender (Hidden)
96. Tekan Esc
97. Klik `×` pada Bar Bulk

### Mark as Returned dan Mark as Unassigned pada aset Borrowed dan Assigned
98. Muat ulang halaman
99. Ketik Search `{runId}`, tekan Enter
100. Klik `⋯` pada baris `Proyektor Pinjam {runId} - 1`
101. Verifikasi aksi `Mark as Returned` tampil pada aset berstatus `Borrowed`
102. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
103. Tekan Esc
104. Klik `⋯` pada baris `Laptop Tugas {runId} - 1`
105. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Assigned`
106. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Assigned`
107. Tekan Esc
108. Centang baris `Proyektor Pinjam {runId} - 1`
109. Klik tombol Bulk Action
110. Verifikasi aksi Bulk `Mark as Returned` tampil untuk aset berstatus `Borrowed`
111. Tekan Esc
112. Klik `×` pada Bar Bulk
113. Centang baris `Laptop Tugas {runId} - 1`
114. Klik tombol Bulk Action
115. Verifikasi aksi Bulk `Mark as Unassigned` tidak dirender (Hidden) untuk aset berstatus `Assigned`
116. Tekan Esc
117. Klik `×` pada Bar Bulk

### Hak diubah menjadi Asset Admin jenis Assignment untuk aksi Mark as
118. Admin mengubah hak `Eko Pratama {runId}` pada group `IT {runId}` menjadi `Asset Admin` jenis `Assignment`
119. Muat ulang halaman
120. Ketik Search `{runId}`, tekan Enter
121. Klik `⋯` pada baris `Proyektor Pinjam {runId} - 1`
122. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
123. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
124. Tekan Esc
125. Klik `⋯` pada baris `Laptop Tugas {runId} - 1`
126. Verifikasi aksi `Mark as Unassigned` tampil pada aset berstatus `Assigned`
127. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Assigned`
128. Tekan Esc
129. Centang baris `Proyektor Pinjam {runId} - 1`
130. Klik tombol Bulk Action
131. Verifikasi aksi Bulk `Mark as Returned` tidak dirender (Hidden) untuk aset berstatus `Borrowed`
132. Tekan Esc
133. Klik `×` pada Bar Bulk
134. Centang baris `Laptop Tugas {runId} - 1`
135. Klik tombol Bulk Action
136. Verifikasi aksi Bulk `Mark as Unassigned` tampil untuk aset berstatus `Assigned`
137. Tekan Esc
138. Klik `×` pada Bar Bulk

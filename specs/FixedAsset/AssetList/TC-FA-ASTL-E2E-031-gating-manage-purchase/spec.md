---
id: TC-FA-ASTL-E2E-031-gating-manage-purchase
title: "Gating UI untuk Manage purchase"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-10d", "ASTL-LOGIC-10k", "ASTL-LOGIC-10l", "ASTL-LOGIC-10n", "ASTL-LOGIC-10o", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§2#r1", "§2#r2", "§2#r3", "§2#r4", "§2#r5", "§2#r6", "§2#r7", "§2#r8", "§2#r9", "§2#r10", "§2#r11", "§2#r12", "§2#r13", "§2#r14", "§2#r15", "§2#r16", "§2#p3", "§9.11#r1", "§9.11#r2", "§9.11#r3", "§9.11#r4", "§9.11#r5", "§9.11#r6", "§9.11#r7", "EB-AKS-5@edit-purchase"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-10d": [40, 41, 42, 43, 68, 69, 71, 81]
  "ASTL-LOGIC-10k": [36, 37, 38, 39]
  "ASTL-LOGIC-10l": 37
  "ASTL-LOGIC-10n": 31
  "ASTL-LOGIC-10o": 32
  "§4.8#r1": [4, 5, 9, 20]
  "§4.8#r2": [10, 106, 114, 115, 118, 119, 123, 128]
  "§4.8#r3": 11
  "§4.8#r4": 12
  "§4.8#r5": [13, 107]
  "§4.8#r6": 21
  "§4.8#r7": [15, 108]
  "§4.8#r8": 16
  "§4.8#r9": 14
  "§4.8#r10": [24, 76, 97]
  "§4.8#r11": 26
  "§4.8#r12": [17, 27, 79, 86, 92, 99]
  "§4.8#r13": [6, 7]
  "§4.8#r14": [36, 37, 38, 39, 40, 41, 42, 43]
  "§2#r1": [13, 14, 15, 21]
  "§2#r2": [36, 37]
  "§2#r3": [17, 27, 40, 41, 42, 43, 63, 64, 78, 79]
  "§2#r4": [11, 36, 37, 38, 39]
  "§2#r5": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37]
  "§2#r6": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37]
  "§2#r7": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37]
  "§2#r8": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37]
  "§2#r9": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37]
  "§2#r10": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37]
  "§2#r11": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37]
  "§2#r12": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37]
  "§2#r13": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37]
  "§2#r14": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37, 79, 86, 92, 99]
  "§2#r15": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37]
  "§2#r16": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37]
  "§2#p3": [2, 3, 7, 13, 15]
  "§9.11#r1": [2, 3, 7]
  "§9.11#r2": [36, 37]
  "§9.11#r3": [32, 40, 41, 42, 43]
  "§9.11#r4": 33
  "§9.11#r5": [38, 39]
  "§9.11#r6": 47
  "§9.11#r7": 50
  "EB-AKS-5@edit-purchase": [57, 58]
anchor: [45, 49]
coverage:
  web: automated
---

# Gating UI untuk Manage purchase

## Prerequisites
- Aktor: `Rina Maharani {runId}`, pemegang role Manage purchase (Read + Update) dengan cakupan Group `IT {runId}` beserta descendant.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-031-1: User, Name `Rina Maharani {runId}`, Role `Manage purchase`, Cakupan `Group IT {runId} beserta descendant`
  - DU-031-2: Group, Name `IT {runId}`, Anak `IT Support {runId}`
  - DU-031-3: Group, Name `Cabang Bandung {runId}`
  - DU-031-4: Asset, Name `Laptop Pro 16 {runId}`, Group `IT {runId}`, Status `Available`, TAG `RFID` berstatus `Paired`, Asset Class `Peralatan IT {runId}`, Tax Depreciation Class `Kelompok 1 {runId}`, Purchase Date `T0 − 30 hari`, Purchase Cost `18500000`, Warranty Until `T0 + 200 hari`
  - DU-031-5: Asset, Name `Kursi Kerja {runId}`, Group `IT {runId}`, Status `Available`
  - DU-031-6: Asset, Name `Kamera Mirrorless {runId}`, Group `IT {runId}`, Status `Available`, License `Unmanaged`
  - DU-031-7: Asset, Name `Printer Laser {runId}`, Group `Cabang Bandung {runId}`, Status `Available`
  - DU-031-8: Custom Field, Name `Nomor PO {runId}`, Group `Purchasing`
  - DU-031-9: Custom Field, Name `Kode Anggaran {runId}`, Group `Accounting`
  - DU-031-11: Asset, Name `Monitor Ultrawide {runId}`, Group `IT Support {runId}`, Status `Available`
  - DU-031-12: Asset, Name `Proyektor Pinjam {runId}`, Group `IT {runId}`, Status `Borrowed`
  - DU-031-13: Asset, Name `Laptop Tugas {runId}`, Group `IT {runId}`, Status `Assigned`
  - Nama baris yang diharapkan untuk Asset Name `Laptop Pro 16 {runId}` adalah `Laptop Pro 16 {runId} - 1`, dari Asset Name `Laptop Pro 16 {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kursi Kerja {runId}` adalah `Kursi Kerja {runId} - 1`, dari Asset Name `Kursi Kerja {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kamera Mirrorless {runId}` adalah `Kamera Mirrorless {runId} - 1`, dari Asset Name `Kamera Mirrorless {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Printer Laser {runId}` adalah `Printer Laser {runId} - 1`, dari Asset Name `Printer Laser {runId}`.
  - Purchase Cost yang diharapkan untuk Purchase Cost `18500000` adalah `Rp 18.500.000,00`, dari Purchase Cost `18500000`.
  - Kursi Kerja {runId} tidak memiliki Purchase Information dan Asset Name-nya tanpa Asset Class; Kamera Mirrorless {runId} adalah aset Unmanaged.
  - Aset `Laptop Pro 16 {runId}` dan `Kursi Kerja {runId}` tercatat di group `IT {runId}`; user hanya mengakses group yang sesuai cakupannya.
  - Purchase Cost yang diharapkan sesudah Edit Purchase adalah `Rp 19.200.000,00`, dari Purchase Cost `19200000`.
  - Nama baris yang diharapkan untuk Asset Name `Monitor Ultrawide {runId}` adalah `Monitor Ultrawide {runId} - 1`, dari Asset Name `Monitor Ultrawide {runId}`.
  - `Monitor Ultrawide {runId}` tercatat di group `IT Support {runId}`, descendant dari `IT {runId}`, tanpa Purchase Information.
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
10. Verifikasi aksi `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft` tidak dirender (Hidden)
11. Verifikasi aksi `Report Disposal` tidak dirender (Hidden)
12. Verifikasi aksi `Report Damage` dan `Report Missing` tidak dirender (Hidden)
13. Verifikasi aksi `Edit` dan `Replace TAG` tidak dirender (Hidden)
14. Verifikasi aksi `Print Label` tidak dirender (Hidden)
15. Verifikasi aksi `Delete Asset Data` tidak dirender (Hidden)
16. Verifikasi aksi `Report TAG` tampil
17. Verifikasi aksi `Edit Purchase` tampil
18. Tekan Esc

### Aksi Manage pada aset Unmanaged
19. Klik `⋯` pada baris `Kamera Mirrorless {runId} - 1`
20. Verifikasi aksi `Detail` tampil
21. Verifikasi aksi `Manage` tidak dirender (Hidden)
22. Tekan Esc

### Checkbox baris, Bar Bulk, dan aksi Bulk
23. Centang baris `Laptop Pro 16 {runId} - 1`
24. Verifikasi checkbox baris dan Bar Bulk tampil
25. Klik tombol Bulk Action
26. Verifikasi aksi Bulk `Print Label`, `Add Label`, dan `Remove Label` tidak dirender (Hidden)
27. Verifikasi aksi Bulk `Edit Purchase` tampil
28. Tekan Esc
29. Klik `×` pada Bar Bulk

### Setup Column dan sel kolom bergerbang
30. Buka Setup Column
31. Verifikasi kolom `Asset Value (Commercial)`, `Asset Class`, `Tax Depreciation Class`, `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry` tersedia di Setup Column
32. Verifikasi kolom custom field Purchasing `Nomor PO {runId}` tersedia di Setup Column
33. Verifikasi kolom custom field Accounting `Kode Anggaran {runId}` tidak tersedia di Setup Column
34. Tampilkan kolom `Asset Value (Commercial)`, `Asset Class`, `Tax Depreciation Class`, `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry`
35. Tutup Setup Column
36. Verifikasi sel `Asset Value (Commercial)` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
37. Verifikasi sel `Asset Value (Commercial)` baris `Kursi Kerja {runId} - 1` menampilkan `No access`, bukan `Pending`
38. Verifikasi sel `Asset Class` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
39. Verifikasi sel `Tax Depreciation Class` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
40. Verifikasi sel `Purchase Date` baris `Laptop Pro 16 {runId} - 1` menampilkan tanggal `T0 − 30 hari` dalam format `dd/MM/yy`
41. Verifikasi sel `Purchase Cost` baris `Laptop Pro 16 {runId} - 1` menampilkan `Rp 18.500.000,00`
42. Verifikasi sel `Purchase Date` dan `Purchase Cost` baris `Kursi Kerja {runId} - 1` menampilkan `Pending`
43. Verifikasi sel `Warranty Expiry` baris `Laptop Pro 16 {runId} - 1` menampilkan tanggal `T0 + 200 hari` dalam format `dd/MM/yy`

### Dokumen Purchase dan data Accounting di Asset Detail
44. Klik Name `Laptop Pro 16 {runId} - 1`
45. Verifikasi halaman detail aset `Laptop Pro 16 {runId} - 1` terbuka bagi `Rina Maharani {runId}`
46. Buka tab `Documents`
47. Verifikasi kelompok Purchase pada tab `Documents` tampil
48. Buka tab `Accounting`
49. Verifikasi tab `Accounting` terbuka bagi `Rina Maharani {runId}`
50. Verifikasi data tab `Accounting` (peringatan fisik vs buku, Depreciation, Acquisition & Value changes, Journals) tidak tampil

### Edit Purchase berhasil disimpan
51. Muat ulang halaman
52. Ketik Search `{runId}`, tekan Enter
53. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
54. Klik `Edit Purchase`
55. Ganti isi Purchase Cost dengan `19200000`
56. Klik `[Save]`
57. Verifikasi toast `Success, purchase data has been saved.` tampil
58. Verifikasi sel `Purchase Cost` baris `Laptop Pro 16 {runId} - 1` menampilkan `Rp 19.200.000,00`, dari Purchase Cost `19200000`

### Dialog Edit Purchase hanya memuat data Purchase
59. Muat ulang halaman
60. Ketik Search `{runId}`, tekan Enter
61. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
62. Klik `Edit Purchase`
63. Verifikasi dialog `Edit Purchase` memuat field `Purchase Date`, `Purchase Cost`, `Reference Price`, `Warranty name`, `Warranty until`, `Provider`, `Document No.`, dan `Additional costs`
64. Verifikasi dialog `Edit Purchase` tidak memuat field aset lain seperti `Asset Name`, `Group`, `TAG`, dan `Asset Class` sebagai isian
65. Tekan Esc

### Cakupan group meliputi descendant
66. Muat ulang halaman
67. Ketik Search `{runId}`, tekan Enter
68. Verifikasi baris `Monitor Ultrawide {runId} - 1` di group `IT Support {runId}` tampil di tabel
69. Verifikasi sel `Purchase Date` dan `Purchase Cost` baris `Monitor Ultrawide {runId} - 1` menampilkan `Pending`
70. Klik `⋯` pada baris `Monitor Ultrawide {runId} - 1`
71. Verifikasi aksi `Edit Purchase` tampil
72. Tekan Esc

### Hak diubah menjadi Manage purchase (Read)
73. Admin mengubah hak `Rina Maharani {runId}` pada group `IT {runId}` menjadi `Manage purchase` (Read)`
74. Muat ulang halaman
75. Ketik Search `{runId}`, tekan Enter
76. Verifikasi checkbox baris dan Bar Bulk tidak dirender (Hidden)
77. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
78. Verifikasi aksi `Detail` tampil
79. Verifikasi aksi `Edit Purchase` tidak dirender (Hidden)
80. Tekan Esc
81. Verifikasi sel `Purchase Cost` baris `Laptop Pro 16 {runId} - 1` menampilkan `Rp 19.200.000,00`

### Hak diubah menjadi Manage asset & TAG (Read + Update)
82. Admin mengubah hak `Rina Maharani {runId}` pada group `IT {runId}` menjadi `Manage asset & TAG` (Read + Update)`
83. Muat ulang halaman
84. Ketik Search `{runId}`, tekan Enter
85. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
86. Verifikasi aksi `Edit Purchase` tidak dirender (Hidden)
87. Tekan Esc

### Hak diubah menjadi Manage asset & TAG (Read + Delete)
88. Admin mengubah hak `Rina Maharani {runId}` pada group `IT {runId}` menjadi `Manage asset & TAG` (Read + Delete)`
89. Muat ulang halaman
90. Ketik Search `{runId}`, tekan Enter
91. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
92. Verifikasi aksi `Edit Purchase` tidak dirender (Hidden)
93. Tekan Esc

### Hak diubah menjadi Manage asset & TAG (Read)
94. Admin mengubah hak `Rina Maharani {runId}` pada group `IT {runId}` menjadi `Manage asset & TAG` (Read)`
95. Muat ulang halaman
96. Ketik Search `{runId}`, tekan Enter
97. Verifikasi checkbox baris dan Bar Bulk tidak dirender (Hidden)
98. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
99. Verifikasi aksi `Edit Purchase` tidak dirender (Hidden)
100. Tekan Esc

### Aksi Bulk selain Edit Purchase tidak dirender bagi Manage purchase (Read + Update)
101. Admin mengubah hak `Rina Maharani {runId}` pada group `IT {runId}` menjadi `Manage purchase` (Read + Update)
102. Muat ulang halaman
103. Ketik Search `{runId}`, tekan Enter
104. Centang baris `Laptop Pro 16 {runId} - 1`
105. Klik tombol Bulk Action
106. Verifikasi aksi Bulk `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, dan `Add to Transfer Draft` tidak dirender (Hidden)
107. Verifikasi aksi Bulk `Batch Replace TAG` tidak dirender (Hidden)
108. Verifikasi aksi Bulk `Delete Asset Data` tidak dirender (Hidden)
109. Tekan Esc
110. Klik `×` pada Bar Bulk

### Mark as Returned dan Mark as Unassigned pada aset Borrowed dan Assigned
111. Muat ulang halaman
112. Ketik Search `{runId}`, tekan Enter
113. Klik `⋯` pada baris `Proyektor Pinjam {runId} - 1`
114. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
115. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
116. Tekan Esc
117. Klik `⋯` pada baris `Laptop Tugas {runId} - 1`
118. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Assigned`
119. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Assigned`
120. Tekan Esc
121. Centang baris `Proyektor Pinjam {runId} - 1`
122. Klik tombol Bulk Action
123. Verifikasi aksi Bulk `Mark as Returned` tidak dirender (Hidden) untuk aset berstatus `Borrowed`
124. Tekan Esc
125. Klik `×` pada Bar Bulk
126. Centang baris `Laptop Tugas {runId} - 1`
127. Klik tombol Bulk Action
128. Verifikasi aksi Bulk `Mark as Unassigned` tidak dirender (Hidden) untuk aset berstatus `Assigned`
129. Tekan Esc
130. Klik `×` pada Bar Bulk

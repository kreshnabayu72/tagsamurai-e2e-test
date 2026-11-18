---
id: TC-FA-ASSIGN-E2E-061-report-damaged-saat-ditugaskan-dep-damaged
title: "Report Damaged, Cancel Damage Report, dan marker Damaged saat ditugaskan"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [D-ASG-17, FI-ASG-78, FI-ASG-79, FI-ASG-80, FI-ASG-81, FI-ASG-82, FI-ASG-84, FI-ASG-85, TS-ASG-29, EC-ASG-25, EC-ASG-88, F-ASSIGN-07.k3, F-ASSIGN-10.k2, "§9.7#r14"]
smoke: []
dependsOn: ["Damaged: Report Damaged dan Cancel Damage Report"]
trace:
  D-ASG-17: [8, 9, 11]
  FI-ASG-78: 8
  FI-ASG-79: [15, 93]
  FI-ASG-80: [23, 24, 29, 33, 51]
  FI-ASG-81: 82
  FI-ASG-82: 60
  FI-ASG-84: [38, 46, 72, 110]
  FI-ASG-85: 42
  TS-ASG-29: 91
  EC-ASG-25: [58, 69, 71, 72, 99, 107, 109, 110]
  EC-ASG-88: [54, 56, 92, 96]
  F-ASSIGN-07.k3: [45, 71, 107]
  F-ASSIGN-10.k2: 44
  "§9.7#r14": [15, 42, 54, 93]
anchor: [50, 78]
coverage:
  web: automated
---
# Report Damaged, Cancel Damage Report, dan marker Damaged saat ditugaskan

## Prerequisites
- Aktor: Aktor Assignment (Asset Admin `Dewi Lestari {runId}`, DU-061-1) tanpa hak keputusan menu Damaged.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-061-1: Karyawan `Dewi Lestari {runId}`, role Asset Admin, Group penugasan `Head Office`, Status `Active`.
  - DU-061-2: Karyawan `Budi Santoso {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, Assignee semua ASG di bawah ini.
  - DU-061-3: ASG `Assigned` untuk Assignee `Budi Santoso {runId}`, Group `Head Office`, berisi aset `Laptop Lenovo T14 {runId}` dan `Kamera Sony A7 {runId}`, tanpa Damage Report, batas efektif baris Photo at end `ON`.
  - DU-061-4: ASG `Assigned` untuk Assignee `Budi Santoso {runId}`, Group `Head Office`, berisi aset `Printer Epson L5290 {runId}` dengan Damage Report `Waiting for Confirmation` milik pelapor `Dewi Lestari {runId}`, batas efektif baris Photo at end `OFF`.
  - DU-061-5: ASG `Assigned` untuk Assignee `Budi Santoso {runId}`, Group `Head Office`, berisi aset `Proyektor ViewSonic PA503 {runId}` dengan Damage Report `Waiting for Confirmation` milik pelapor `Budi Santoso {runId}`; Report No. laporan itu milik DU-061-5, batas efektif baris Photo at end `ON`.
  - DU-061-6: Damage Report baru untuk `Laptop Lenovo T14 {runId}` dengan Photo `kerusakan-laptop.jpg` dan Description `Layar retak di sudut kanan atas`.
  - DU-061-7: Damage Report baru untuk `Kamera Sony A7 {runId}` dengan Photo `kerusakan-kamera.jpg` dan Description `Lensa tergores di bagian depan`.
  - DU-061-8: Foto Unassign `foto-unassign-laptop.jpg` untuk aset `Laptop Lenovo T14 {runId}`.
  - DU-061-9: Damage Report perbaikan untuk `Kamera Sony A7 {runId}` dengan Description `Lensa tergores dan berdebu di bagian depan`; Photo tetap `kerusakan-kamera.jpg`.
  - DU-061-10: Foto Unassign `foto-unassign-proyektor.jpg` untuk aset `Proyektor ViewSonic PA503 {runId}`.
  - DU-061-11: ASG `Assigned` untuk Assignee `Budi Santoso {runId}`, Group `Head Office`, berisi aset `Mesin Cuci Industrial Electrolux {runId}`, tanpa Damage Report, batas efektif baris Photo at end `OFF`.
  - DU-061-12: Damage Report baru untuk `Mesin Cuci Industrial Electrolux {runId}` dengan Photo `kerusakan-mesin-cuci.jpg` dan What happened `Motor mesin cuci berbunyi keras lalu mati sendiri`.
  - DU-061-13: ASG `Assigned` untuk Assignee `Budi Santoso {runId}`, Group `Head Office`, berisi aset `Tablet Samsung Galaxy Tab S8 {runId}` dengan Damage Report berstatus `Damaged` (sudah dikonfirmasi); Report No. laporan itu milik DU-061-13, batas efektif baris Photo at end `ON`.
  - DU-061-14: Foto Unassign `foto-unassign-tablet.jpg` untuk aset `Tablet Samsung Galaxy Tab S8 {runId}`.

## Test Steps

### Dialog Report Damaged meminta Photo dan Description
1. Buka tab Assigned Assets di halaman Transactions > Assignment
2. Ketik Search `Budi Santoso {runId}`, tekan Enter
3. Centang baris aset `Laptop Lenovo T14 {runId}`
4. Centang baris aset `Kamera Sony A7 {runId}`
5. Klik `Unassign` pada menu aksi bulk
6. Klik `⋯` pada baris aset `Laptop Lenovo T14 {runId}` di halaman Unassign
7. Klik `Report Damaged`
8. Verifikasi dialog `Report Damaged` tampil dengan isian Photo, Description, dan tombol `[Cancel]` dan `[Report]`
9. Verifikasi kotak Description dialog memakai placeholder `Enter description`
10. Klik `[Report]` tanpa mengisi Photo dan Description
11. Verifikasi pesan `Photo must not be empty` dan `Description must not be empty` tampil
12. Unggah Photo `kerusakan-laptop.jpg` pada dialog `Report Damaged`
13. Isi Description `Layar retak di sudut kanan atas`
14. Klik `[Report]`
15. Verifikasi kolom Status baris aset `Laptop Lenovo T14 {runId}` menampilkan badge `Reported Damaged`

### Laporan yang belum tersimpan dapat diperbaiki atau dibuang bersama asetnya
16. Klik `⋯` pada baris aset `Kamera Sony A7 {runId}` di halaman Unassign
17. Klik `Report Damaged`
18. Unggah Photo `kerusakan-kamera.jpg` pada dialog `Report Damaged`
19. Isi Description `Lensa tergores di bagian depan`
20. Klik `[Report]`
21. Klik `⋯` pada baris aset `Kamera Sony A7 {runId}` di halaman Unassign
22. Klik `Edit Damage Report`
23. Verifikasi dialog `Report Damaged` terisi Description `Lensa tergores di bagian depan`
24. Verifikasi dialog `Report Damaged` terisi Photo `kerusakan-kamera.jpg`
25. Ganti isi Description dengan `Lensa tergores dan berdebu di bagian depan`
26. Klik `[Report]`
27. Klik `⋯` pada baris aset `Kamera Sony A7 {runId}` di halaman Unassign
28. Klik `Edit Damage Report`
29. Verifikasi dialog `Report Damaged` terisi Description `Lensa tergores dan berdebu di bagian depan`
30. Klik `[Cancel]`
31. Klik `⋯` pada baris aset `Kamera Sony A7 {runId}` di halaman Unassign
32. Klik `Remove from List`
33. Verifikasi baris aset `Laptop Lenovo T14 {runId}` tetap tampil sebagai satu-satunya baris di daftar Unassign

### Submit menyimpan laporan dan menutup baris Unassigned dengan marker Damaged
34. Klik `[Verify Asset]`
35. Pindai TAG aset `Laptop Lenovo T14 {runId}`
36. Unggah Unassign Photo `foto-unassign-laptop.jpg` untuk aset `Laptop Lenovo T14 {runId}`
37. Klik `[Submit]`
38. Verifikasi toast `Success, 1 asset has been unassigned.`
39. Buka tab History di halaman Transactions > Assignment
40. Buka sub-tab By Asset
41. Ketik Search `Laptop Lenovo T14 {runId}`, tekan Enter
42. Verifikasi baris aset `Laptop Lenovo T14 {runId}` berstatus `Unassigned` dengan marker `Damaged`
43. Klik aksi `Assignment Log` pada baris aset `Laptop Lenovo T14 {runId}`
44. Verifikasi node `Damage reported by [Reporter]` dengan pelaku `Dewi Lestari {runId}` dan Description `Layar retak di sudut kanan atas` tampil
45. Verifikasi node `Unassigned by [Receiver]` dengan pelaku `Dewi Lestari {runId}` tampil
46. Verifikasi node `Unassigned by [Receiver]` memuat Photo Unassign aset `Laptop Lenovo T14 {runId}`
47. Tutup dialog `Assignment Log`

### Laporan yang dibuang bersama asetnya tidak tersimpan
48. Buka tab Assigned Assets di halaman Transactions > Assignment
49. Ketik Search `Kamera Sony A7 {runId}`, tekan Enter
50. Verifikasi baris aset `Kamera Sony A7 {runId}` tampil berstatus `Assigned`
51. Verifikasi badge `Reported Damaged` tidak tampil pada baris aset `Kamera Sony A7 {runId}`

### Aset yang sudah dilaporkan Assignee tetap bisa di-Unassign tanpa laporan kedua
52. Buka tab Assigned Assets di halaman Transactions > Assignment
53. Ketik Search `Proyektor ViewSonic PA503 {runId}`, tekan Enter
54. Verifikasi baris aset `Proyektor ViewSonic PA503 {runId}` tetap berstatus `Assigned` dengan badge `Reported Damaged`
55. Klik `⋯` pada baris aset `Proyektor ViewSonic PA503 {runId}`
56. Verifikasi aksi `Unassign` tersedia pada baris aset `Proyektor ViewSonic PA503 {runId}`
57. Klik `Unassign`
58. Verifikasi kolom Status baris aset `Proyektor ViewSonic PA503 {runId}` menampilkan badge `Reported Damaged` di halaman Unassign
59. Klik `⋯` pada baris aset `Proyektor ViewSonic PA503 {runId}` di halaman Unassign
60. Verifikasi aksi `Cancel Damage Report` tidak tersedia untuk laporan milik Assignee pada baris aset `Proyektor ViewSonic PA503 {runId}`
61. Tutup menu aksi baris
62. Klik `[Verify Asset]`
63. Pindai TAG aset `Proyektor ViewSonic PA503 {runId}`
64. Unggah Unassign Photo `foto-unassign-proyektor.jpg` untuk aset `Proyektor ViewSonic PA503 {runId}`
65. Klik `[Submit]`
66. Buka tab History di halaman Transactions > Assignment
67. Buka sub-tab By Asset
68. Ketik Search `Proyektor ViewSonic PA503 {runId}`, tekan Enter
69. Verifikasi baris aset `Proyektor ViewSonic PA503 {runId}` berstatus `Unassigned` dengan marker `Damaged`
70. Klik aksi `Assignment Log` pada baris aset `Proyektor ViewSonic PA503 {runId}`
71. Verifikasi node `Unassigned by [Receiver]` memuat Report No. laporan milik DU-061-5 tanpa laporan kedua
72. Verifikasi node `Unassigned by [Receiver]` memuat Photo Unassign aset `Proyektor ViewSonic PA503 {runId}`
73. Tutup dialog `Assignment Log`

### Cancel Damage Report membatalkan laporan milik pelapor sendiri
74. Buka tab Assigned Assets di halaman Transactions > Assignment
75. Ketik Search `Printer Epson L5290 {runId}`, tekan Enter
76. Klik `⋯` pada baris aset `Printer Epson L5290 {runId}`
77. Klik `Unassign`
78. Verifikasi kolom Status baris aset `Printer Epson L5290 {runId}` menampilkan badge `Reported Damaged` di halaman Unassign
79. Klik `⋯` pada baris aset `Printer Epson L5290 {runId}` di halaman Unassign
80. Klik `Cancel Damage Report`
81. Konfirmasi pembatalan pada dialog `Cancel Report`
82. Verifikasi kolom Status baris aset `Printer Epson L5290 {runId}` menampilkan `Assigned` dan badge `Reported Damaged` tidak tampil
83. Klik `[Cancel]` pada form Unassign yang belum diubah

### Report Damaged dari row action Assigned Assets menyimpan laporan Waiting for Confirmation
84. Buka tab Assigned Assets di halaman Transactions > Assignment
85. Ketik Search `Mesin Cuci Industrial Electrolux {runId}`, tekan Enter
86. Klik `⋯` pada baris aset `Mesin Cuci Industrial Electrolux {runId}`
87. Klik `Report Damaged`
88. Unggah Photo `kerusakan-mesin-cuci.jpg` pada dialog `Report Damaged`
89. Isi What happened `Motor mesin cuci berbunyi keras lalu mati sendiri`
90. Kirim dialog `Report Damaged`
91. Verifikasi toast `Success, damage report has been submitted.`
92. Verifikasi baris aset `Mesin Cuci Industrial Electrolux {runId}` tetap berstatus `Assigned`
93. Verifikasi baris aset `Mesin Cuci Industrial Electrolux {runId}` menampilkan badge `Reported Damaged` karena laporan berstatus `Waiting for Confirmation`

### Aset dengan laporan Damaged tetap bisa di-Unassign tanpa laporan kedua
94. Buka tab Assigned Assets di halaman Transactions > Assignment
95. Ketik Search `Tablet Samsung Galaxy Tab S8 {runId}`, tekan Enter
96. Verifikasi baris aset `Tablet Samsung Galaxy Tab S8 {runId}` tetap berstatus `Assigned` dengan badge `Damaged`
97. Klik `⋯` pada baris aset `Tablet Samsung Galaxy Tab S8 {runId}`
98. Klik `Unassign`
99. Verifikasi kolom Status baris aset `Tablet Samsung Galaxy Tab S8 {runId}` menampilkan badge `Damaged` di halaman Unassign
100. Klik `[Verify Asset]`
101. Pindai TAG aset `Tablet Samsung Galaxy Tab S8 {runId}`
102. Unggah Unassign Photo `foto-unassign-tablet.jpg` untuk aset `Tablet Samsung Galaxy Tab S8 {runId}`
103. Klik `[Submit]`
104. Buka tab History di halaman Transactions > Assignment
105. Buka sub-tab By Asset
106. Ketik Search `Tablet Samsung Galaxy Tab S8 {runId}`, tekan Enter
107. Verifikasi baris aset `Tablet Samsung Galaxy Tab S8 {runId}` berstatus `Unassigned` dengan marker `Damaged`
108. Klik aksi `Assignment Log` pada baris aset `Tablet Samsung Galaxy Tab S8 {runId}`
109. Verifikasi node `Unassigned by [Receiver]` memuat Report No. laporan milik DU-061-13 tanpa laporan kedua
110. Verifikasi node `Unassigned by [Receiver]` memuat Photo Unassign aset `Tablet Samsung Galaxy Tab S8 {runId}`
111. Tutup dialog `Assignment Log`

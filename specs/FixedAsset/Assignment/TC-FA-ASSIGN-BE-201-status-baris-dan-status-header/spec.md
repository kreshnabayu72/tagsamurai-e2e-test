---
id: TC-FA-ASSIGN-BE-201-status-baris-dan-status-header
title: "Status baris dan status header turunan, termasuk marker dan penanda"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASSIGN-LOGIC-01a", "ASSIGN-LOGIC-01b", "ASSIGN-LOGIC-01c", "ASSIGN-LOGIC-01d", "ASSIGN-LOGIC-01h", "ASSIGN-LOGIC-01i", "ASSIGN-LOGIC-01j", "ASSIGN-LOGIC-01k", "ASSIGN-LOGIC-01l", "§9.2#p3", "§9.2#p4", "§9.2#p5", "§9.2#p6", "§9.2#r1", "§9.2#r2", "§9.2#r3", "§9.2#r4", "§9.2#r5", "§9.2#r6", "§9.2#r7", "§9.2#r8", "§9.2#r9", "§9.2#r10", "§9.2#r11", "§9.2#r12", "§9.2#r13", "§9.2#r14", "§9.2#r15", "§9.2#r16", "§9.2#r17", "§9.2#r18", "§9.2#b1", "§9.2#b2", "§9.2#b3", "§9.2#p8", "§9.2#p10", "§9.2#p12", "§9.2#p13", "§9.2#p14", "§9.2#p15", "§9.2#p16", "§9.2#p17", "§9.4.3#b1"]
smoke: []
dependsOn: []
trace:
  "ASSIGN-LOGIC-01a": 8
  "ASSIGN-LOGIC-01b": [9, 10, 64]
  "ASSIGN-LOGIC-01c": [4, 7, 91]
  "ASSIGN-LOGIC-01d": [11, 28, 46]
  "ASSIGN-LOGIC-01h": 33
  "ASSIGN-LOGIC-01i": 23
  "ASSIGN-LOGIC-01j": [89, 91]
  "ASSIGN-LOGIC-01k": [21, 29]
  "ASSIGN-LOGIC-01l": 21
  "§9.2#p3": [21, 29]
  "§9.2#p4": [54, 57]
  "§9.2#p5": 33
  "§9.2#p6": [16, 30, 32, 40]
  "§9.2#r1": [2, 5, 81, 89]
  "§9.2#r2": [13, 14, 25, 77]
  "§9.2#r3": [12, 14, 35]
  "§9.2#r4": [27, 39, 43]
  "§9.2#r5": [45, 49, 51]
  "§9.2#r6": [54, 55, 99]
  "§9.2#r7": [57, 58, 100]
  "§9.2#r8": [36, 77]
  "§9.2#r9": [71, 80, 81, 88, 84]
  "§9.2#r10": 16
  "§9.2#r11": 16
  "§9.2#r12": 3
  "§9.2#r13": [16, 30, 37]
  "§9.2#r14": [32, 78]
  "§9.2#r15": [40, 47, 72]
  "§9.2#r16": [60, 61, 74, 101]
  "§9.2#r17": [82, 83]
  "§9.2#r18": [88, 85]
  "§9.2#b1": [40, 41]
  "§9.2#b2": [65, 66, 67, 85]
  "§9.2#b3": [17, 18]
  "§9.2#p8": 16
  "§9.2#p10": 16
  "§9.2#p12": 16
  "§9.2#p13": 16
  "§9.2#p14": [30, 32, 37, 47]
  "§9.2#p15": [74, 82, 65]
  "§9.2#p16": [18, 19]
  "§9.2#p17": [19, 41, 62, 93]
  "§9.4.3#b1": [21, 32]
owner: BE
---

# Status baris dan status header turunan, termasuk marker dan penanda

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`, sebagai pengaju ASG, pemberi handover, dan penerima Unassign. Approver `Rina Wijaya {runId}`: pemegang Role Transaksi `Approver` pada Group `Head Office`, bukan pengaju dan bukan Assignee.
- Data:
  - DU-201-1: Aset `Laptop Dell Latitude {runId}`, Group `Head Office`, TAG `Non TAG`, Custody `Available`, Require approval `OFF`, Need recipient confirmation `No`, Photo at start `OFF`, Photo at end `OFF`, Max assets per assignee `0`.
  - DU-201-2: Aset `Monitor LG 24 {runId}`, dengan nilai efektif yang sama seperti DU-201-1.
  - DU-201-3: Aset `Projector Epson EB-X49 {runId}`, Group `Head Office`, TAG `Non TAG`, Custody `Available`, Require approval `ON`, Approval type `Any one` dengan approver `Rina Wijaya {runId}`, Need recipient confirmation `No`, Photo at start `OFF`, Photo at end `OFF`, Max assets per assignee `0`.
  - DU-201-4: Aset `Camera Sony A7 {runId}`, dengan nilai efektif yang sama seperti DU-201-3.
  - DU-201-5: Aset `Tablet Samsung Tab S8 {runId}`, dengan nilai efektif yang sama seperti DU-201-1.
  - DU-201-6: Aset `Printer HP M404 {runId}`, dengan nilai efektif yang sama seperti DU-201-1.
  - DU-201-7: Aset `Scanner Epson DS-530 {runId}`, dengan nilai efektif yang sama seperti DU-201-1.
  - DU-201-8: Aset `Toyota Avanza {runId}`, dengan nilai efektif yang sama seperti DU-201-3.
  - DU-201-9: Aset `Toyota Innova {runId}`, dengan nilai efektif yang sama seperti DU-201-3.
  - DU-201-10: Aset `Keyboard Logitech MX {runId}`, dengan nilai efektif yang sama seperti DU-201-1.
  - DU-201-11: Aset `Headset Jabra {runId}`, Group `Head Office`, TAG `Non TAG`, Custody `In Assignment Process` karena barisnya ada di ASG milik DU-201-15, Require approval `OFF`, Need recipient confirmation `No`, Photo at start `OFF`, Photo at end `OFF`, Max assets per assignee `0`.
  - DU-201-12: Assignee `Budi Santoso {runId}`, karyawan aktif dengan akun login, tipe Assignee `Employee`.
  - DU-201-13: Approver `Rina Wijaya {runId}`, karyawan aktif dengan akun login, pemegang Role Transaksi `Approver` pada Group `Head Office`.
  - DU-201-14: Assignee Division `Finance {runId}` dengan PIC `Sari Dewi {runId}` (karyawan aktif dengan akun login, Division-nya `Finance {runId}`).
  - DU-201-15: ASG Division yang sudah diajukan untuk `Finance {runId}` dengan PIC `Sari Dewi {runId}` memuat satu baris untuk aset `Headset Jabra {runId}` berstatus `Waiting for Handover` sejak sebelum spec mulai. PIC `Sari Dewi {runId}` sudah dinonaktifkan sehingga ASG ini tanpa PIC aktif. Transaction ID ASG ini milik DU-201-15.
  - DU-201-16: Input pengajuan untuk Assignee `Budi Santoso {runId}`, tipe `Employee`, Group asal `Head Office`, Note `Penugasan alat kerja {runId}`, Purpose `Daily work` pada setiap baris.
  - DU-201-17: Approval Note Reject `Aset sedang dipakai tim lain {runId}`.
  - DU-201-19: Aset `Mouse Logitech M590 {runId}`, dengan nilai efektif yang sama seperti DU-201-1.
  - DU-201-20: Aset `Webcam Logitech C920 {runId}`, dengan nilai efektif yang sama seperti DU-201-1.
  - DU-201-18: Percobaan ditolak: Purpose baris `Laptop Dell Latitude {runId}` diganti menjadi `Training`, dan status header diubah langsung menjadi `Assigned`.
- Kondisi:
  - Level Feature Suite Assignment pada plan adalah `Full`, dan Approval Workflow tersedia di plan.
  - Setiap aset berada di Custody `Available` dan tidak berada di ASG aktif maupun Draft mana pun, kecuali aset `Headset Jabra {runId}` yang barisnya ada di ASG milik DU-201-15.
  - Transaction timeout berlaku menurut Transaction Settings tab Assign; ASG lain dalam spec ini diselesaikan lebih dulu sebelum langkah waktu berlalu dijalankan, dan ASG milik DU-201-15 masih berstatus `Waiting for Handover` ketika langkah waktu berlalu itu dijalankan.

## Test Steps

### Draft belum bernomor dan belum mengunci aset
1. Aktor Assignment menyimpan Draft untuk Assignee `Budi Santoso {runId}` dengan Note `Penugasan alat kerja {runId}`, memuat aset `Laptop Dell Latitude {runId}`, `Monitor LG 24 {runId}`, `Projector Epson EB-X49 {runId}`, `Camera Sony A7 {runId}`, dan `Tablet Samsung Tab S8 {runId}` dengan Purpose `Daily work`
2. Verifikasi kelima baris Draft berstatus `Draft`
3. Verifikasi status header Draft adalah `Draft`
4. Verifikasi Draft belum memiliki Transaction ID `ASG-YYYY-NNNN`
5. Verifikasi Custody kelima aset tetap `Available` selama berstatus `Draft`

### Submit menghasilkan satu ASG dengan satu baris per aset
6. Aktor Assignment mengajukan Submit atas Draft tersebut
7. Verifikasi ASG hasil Submit mendapat Transaction ID berformat `ASG-YYYY-NNNN` saat Submit
8. Verifikasi ASG hasil Submit memuat satu header dan lima baris, satu baris per aset
9. Verifikasi header menyimpan Assignee `Budi Santoso {runId}`, tipe Assignee `Employee`, Group asal `Head Office`, dan Note `Penugasan alat kerja {runId}`
10. Verifikasi header tidak memiliki PIC karena tipe Assignee adalah `Employee`
11. Verifikasi setiap baris menyimpan Purpose `Daily work`, status, aturan efektif, serta snapshot approver dan Approval type

### Status awal baris dan status header campuran
12. Verifikasi baris `Laptop Dell Latitude {runId}`, `Monitor LG 24 {runId}`, dan `Tablet Samsung Tab S8 {runId}` berstatus `Waiting for Handover` dengan Approval `Not required`
13. Verifikasi baris `Projector Epson EB-X49 {runId}` dan `Camera Sony A7 {runId}` berstatus `Waiting for Approval`
14. Verifikasi Custody kelima aset adalah `In Assignment Process`
15. Aktor Assignment membaca daftar ASG yang sedang berjalan
16. Verifikasi ASG tersebut tampil dengan status header `Waiting for Handover`, karena urutan 2 mengalahkan urutan 3
17. Verifikasi campuran status baris `Waiting for Handover` dan `Waiting for Approval` terbaca per baris di detail ASG, tanpa status header gabungan
18. Verifikasi status header tidak bernilai Partially approved, Expired, Overdue, Extension, maupun Waiting for Confirmation
19. Verifikasi hasil baca header tidak memuat ringkasan jumlah baris per status

### Status header tidak dapat diubah langsung dan baris tidak dapat diedit setelah Submit
20. Aktor Assignment mengubah status header ASG tersebut langsung menjadi `Assigned`
21. Verifikasi status header tetap `Waiting for Handover`, karena status header selalu dihitung ulang dari baris dan tidak pernah diubah langsung
22. Aktor Assignment mengganti Purpose baris `Laptop Dell Latitude {runId}` menjadi `Training` dan mengeluarkan aset `Camera Sony A7 {runId}` dari ASG yang sudah di-Submit
23. Verifikasi Purpose baris `Laptop Dell Latitude {runId}` tetap `Daily work` dan ASG tetap memuat lima aset
24. Aktor Assignment menyerahkan aset `Projector Epson EB-X49 {runId}` yang barisnya `Waiting for Approval`
25. Verifikasi baris `Projector Epson EB-X49 {runId}` tetap `Waiting for Approval` dan Custody tetap `In Assignment Process`

### Handover mengubah baris menjadi Assigned dan header dihitung ulang
26. Aktor Assignment menyelesaikan handover aset `Laptop Dell Latitude {runId}` tanpa konfirmasi Assignee
27. Verifikasi baris `Laptop Dell Latitude {runId}` berstatus `Assigned` dan Custody `Assigned`
28. Verifikasi baris `Laptop Dell Latitude {runId}` memuat Handed Over At dan Confirmation `Not required`
29. Verifikasi status `Assigned` tersimpan pada baris `Laptop Dell Latitude {runId}` saja, sedangkan baris `Monitor LG 24 {runId}` tetap `Waiting for Handover`
30. Verifikasi status header tetap `Waiting for Handover` karena masih ada baris `Waiting for Handover`
31. Aktor Assignment menyelesaikan handover aset `Monitor LG 24 {runId}` dan `Tablet Samsung Tab S8 {runId}` tanpa konfirmasi Assignee
32. Verifikasi status header menjadi `Waiting for Approval`, karena baris `Assigned` tidak mengalahkan baris yang masih `Waiting for Approval`
33. Verifikasi baris `Laptop Dell Latitude {runId}` tidak memiliki Due date dan tetap `Assigned` selama belum di-Unassign

### Approve dan Reject per aset oleh approver
34. Approver `Rina Wijaya {runId}` memutuskan dalam satu pengajuan: Approve aset `Projector Epson EB-X49 {runId}` dan Reject aset `Camera Sony A7 {runId}` dengan Approval Note `Aset sedang dipakai tim lain {runId}`
35. Verifikasi baris `Projector Epson EB-X49 {runId}` berstatus `Waiting for Handover` dan Custody tetap `In Assignment Process`
36. Verifikasi baris `Camera Sony A7 {runId}` berstatus `Rejected` dan Custody `Available`
37. Verifikasi status header menjadi `Waiting for Handover`
38. Aktor Assignment menyelesaikan handover aset `Projector Epson EB-X49 {runId}` tanpa konfirmasi Assignee
39. Verifikasi baris `Projector Epson EB-X49 {runId}` berstatus `Assigned`
40. Verifikasi status header menjadi `Assigned`, karena baris `Rejected` diabaikan selama masih ada baris aktif dan semua baris aktif sudah `Assigned`
41. Verifikasi baris `Camera Sony A7 {runId}` yang `Rejected` tetap tampil di detail ASG

### Baris Assigned tidak dapat ditarik kembali lewat Cancel
42. Aktor Assignment melakukan Cancel Assignment pada baris `Tablet Samsung Tab S8 {runId}` yang berstatus `Assigned`
43. Verifikasi baris `Tablet Samsung Tab S8 {runId}` tetap `Assigned` dan Custody tetap `Assigned`

### Unassign tanpa marker
44. Aktor Assignment melakukan Unassign atas aset `Laptop Dell Latitude {runId}` saja
45. Verifikasi baris `Laptop Dell Latitude {runId}` berstatus `Unassigned` tanpa marker, Custody `Available`, dan Condition aset tidak berubah
46. Verifikasi hasil Unassign tersimpan sebagai riwayat baris `Laptop Dell Latitude {runId}`
47. Verifikasi status header tetap `Assigned`, karena tiga baris `Assigned` dan satu baris `Unassigned` menghasilkan `Assigned`, dengan satu baris `Rejected` yang diabaikan
48. Aktor Assignment menyerahkan kembali aset `Laptop Dell Latitude {runId}` yang barisnya sudah `Unassigned`
49. Verifikasi baris `Laptop Dell Latitude {runId}` tetap `Unassigned` dan Custody tetap `Available`
50. Aktor Assignment melakukan Unassign sekali lagi atas aset `Laptop Dell Latitude {runId}`
51. Verifikasi baris `Laptop Dell Latitude {runId}` tetap `Unassigned` tanpa marker dan Condition aset tidak berubah

### Unassign dengan marker Damaged
52. Aktor Assignment melakukan `Report Damaged` atas aset `Monitor LG 24 {runId}` sehingga aset memiliki laporan `Damaged` yang aktif
53. Aktor Assignment melakukan Unassign atas aset `Monitor LG 24 {runId}`
54. Verifikasi baris `Monitor LG 24 {runId}` berstatus `Unassigned` dengan marker `Damaged`, dan marker tidak mengubah status baris
55. Verifikasi Custody aset `Monitor LG 24 {runId}` adalah `Available` dengan Condition `Damaged`

### Report Missing menutup baris tanpa halaman Unassign
56. Aktor Assignment melaporkan aset `Tablet Samsung Tab S8 {runId}` hilang lewat Report Missing
57. Verifikasi baris `Tablet Samsung Tab S8 {runId}` berstatus `Unassigned` dengan marker `Missing`
58. Verifikasi Custody aset `Tablet Samsung Tab S8 {runId}` adalah `Available` dengan Condition `Missing`

### Header Unassigned bila tidak ada baris aktif
59. Aktor Assignment melakukan Unassign atas aset `Projector Epson EB-X49 {runId}`
60. Verifikasi status header menjadi `Unassigned`, karena tidak ada baris aktif dan ada baris `Unassigned`
61. Verifikasi ASG tersebut tidak lagi tampil di antrean ASG yang sedang berjalan dan pindah ke riwayat
62. Verifikasi baris `Camera Sony A7 {runId}` yang `Rejected` tetap tampil di detail ASG yang `Unassigned`

### ASG Division tanpa PIC aktif menampilkan penanda No PIC
63. Aktor Assignment membaca ASG Division milik DU-201-15
64. Verifikasi header menyimpan Assignee Division `Finance {runId}` dan PIC `Sari Dewi {runId}`
65. Verifikasi status header adalah `Waiting for Handover` disertai penanda `No PIC`
66. Verifikasi penanda `No PIC` terbaca pada ASG tersebut di daftar ASG yang sedang berjalan dan di detail ASG
67. Verifikasi tindakan yang ditunggu pada ASG tersebut adalah `Change PIC` oleh Aktor Assignment

### Satu Unassigned dan satu Canceled menghasilkan header Unassigned
68. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Printer HP M404 {runId}` dan `Scanner Epson DS-530 {runId}`
69. Aktor Assignment menyelesaikan handover aset `Printer HP M404 {runId}` tanpa konfirmasi Assignee
70. Pengaju melakukan Cancel Assignment pada baris `Scanner Epson DS-530 {runId}`
71. Verifikasi baris `Scanner Epson DS-530 {runId}` berstatus `Canceled` dan Custody `Available`
72. Verifikasi status header adalah `Assigned`
73. Aktor Assignment melakukan Unassign atas aset `Printer HP M404 {runId}`
74. Verifikasi status header menjadi `Unassigned`, karena satu baris `Unassigned` dan satu baris `Canceled` menghasilkan `Unassigned`

### Satu Rejected dan satu Canceled menghasilkan header Rejected
75. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Toyota Avanza {runId}` dan `Toyota Innova {runId}`
76. Approver `Rina Wijaya {runId}` melakukan Reject atas aset `Toyota Avanza {runId}` dengan Approval Note `Aset sedang dipakai tim lain {runId}`
77. Verifikasi baris `Toyota Avanza {runId}` berstatus `Rejected` dan baris `Toyota Innova {runId}` masih `Waiting for Approval`
78. Verifikasi status header adalah `Waiting for Approval`
79. Waktu berlalu melewati Transaction timeout sejak baris `Toyota Innova {runId}` masuk `Waiting for Approval`, sehingga baris `Headset Jabra {runId}` yang masuk `Waiting for Handover` sebelum spec mulai juga melewati Transaction timeout
80. Verifikasi baris `Toyota Innova {runId}` berstatus `Canceled` oleh `System` dengan alasan `Timed out (Waiting for Approval)` dan Custody `Available`
81. Verifikasi asetnya kembali ke Draft baru berstatus `Draft`, tanpa Transaction ID, dan ASG asal tetap memuat baris `Toyota Innova {runId}` yang `Canceled`
82. Verifikasi status header menjadi `Rejected`, karena satu baris `Rejected` dan satu baris `Canceled` menghasilkan `Rejected`
83. Verifikasi ASG tersebut tidak lagi tampil di antrean ASG yang sedang berjalan dan pindah ke riwayat

### ASG Division tanpa PIC aktif ditutup sistem karena tidak diserahkan
84. Verifikasi baris `Headset Jabra {runId}` berstatus `Canceled` oleh `System` dengan alasan `Not handed over`
85. Verifikasi status header menjadi `Canceled` tanpa penanda `No PIC` di riwayat, karena penanda hanya berlaku selama ada baris aktif

### Cancel dengan Save as Draft to edit menjadikan header Canceled dan membuat Draft baru
86. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Keyboard Logitech MX {runId}`
87. Aktor Assignment melakukan Cancel atas ASG tersebut dengan `Save as Draft to edit`
88. Verifikasi baris `Keyboard Logitech MX {runId}` berstatus `Canceled`, Custody `Available`, dan status header `Canceled`, karena semua baris `Canceled`
89. Verifikasi tercipta Draft baru berstatus `Draft` tanpa Transaction ID, memuat aset `Keyboard Logitech MX {runId}` dengan keterangan `Restored from` Transaction ID ASG asal
90. Aktor Assignment mengajukan Submit atas Draft baru tersebut
91. Verifikasi ASG hasil Submit Draft baru mendapat Transaction ID `ASG-YYYY-NNNN` yang berbeda dari ASG asal, dan baris `Keyboard Logitech MX {runId}` berstatus `Waiting for Handover`

### ASG Unassigned tetap menampilkan baris Canceled di detail
92. Aktor Assignment membaca detail ASG yang memuat `Printer HP M404 {runId}` dan `Scanner Epson DS-530 {runId}`
93. Verifikasi baris `Scanner Epson DS-530 {runId}` yang `Canceled` tetap tampil di detail ASG yang berstatus header `Unassigned`

### Header Unassigned bila seluruh baris selesai adalah Unassigned bermarker
94. Aktor Assignment mengajukan Submit untuk Assignee `Budi Santoso {runId}` dengan aset `Mouse Logitech M590 {runId}` dan `Webcam Logitech C920 {runId}`
95. Aktor Assignment menyelesaikan handover aset `Mouse Logitech M590 {runId}` dan `Webcam Logitech C920 {runId}` tanpa konfirmasi Assignee
96. Aktor Assignment melakukan `Report Damaged` atas aset `Mouse Logitech M590 {runId}` sehingga aset memiliki laporan `Damaged` yang aktif
97. Aktor Assignment melakukan Unassign atas aset `Mouse Logitech M590 {runId}`
98. Aktor Assignment melaporkan aset `Webcam Logitech C920 {runId}` hilang lewat Report Missing
99. Verifikasi baris `Mouse Logitech M590 {runId}` berstatus `Unassigned` dengan marker `Damaged`
100. Verifikasi baris `Webcam Logitech C920 {runId}` berstatus `Unassigned` dengan marker `Missing`
101. Verifikasi status header ASG tersebut adalah `Unassigned`, karena tidak ada baris aktif dan semua baris selesai berstatus `Unassigned` dengan marker, tanpa baris `Unassigned` tanpa marker

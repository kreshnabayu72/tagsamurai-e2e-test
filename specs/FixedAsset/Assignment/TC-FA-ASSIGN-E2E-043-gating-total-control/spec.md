---
id: TC-FA-ASSIGN-E2E-043-gating-total-control
title: "Gating Total Control: elemen Show, Hidden, dan Disabled menurut matriks role"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r8", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#r12", "§2.1#r13", "§2.1#r14", "§2.1#r15", "§2.1#r16", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§4.8#r15", "§4.8#r16", "§4.8#r17", "§2.1#b1", "§2.1#b2", "§2.1#b3", "§4.8#p1", "§4.8#p2"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [15, 18]
  "§2.1#r2": [6, 7, 8]
  "§2.1#r3": [56, 58]
  "§2.1#r4": [59, 61]
  "§2.1#r5": 24
  "§2.1#r6": 72
  "§2.1#r7": 22
  "§2.1#r8": 23
  "§2.1#r9": 31
  "§2.1#r10": 39
  "§2.1#r11": 40
  "§2.1#r12": 49
  "§2.1#r13": 41
  "§2.1#r14": 42
  "§2.1#r15": 32
  "§2.1#r16": [15, 36]
  "§4.8#r1": [1, 11]
  "§4.8#r2": 12
  "§4.8#r3": [39, 41, 45, 46, 95, 96]
  "§4.8#r4": 4
  "§4.8#r5": 58
  "§4.8#r6": [59, 61]
  "§4.8#r7": 24
  "§4.8#r8": [22, 23, 27, 28, 31, 45, 82, 85, 86, 89, 90, 91]
  "§4.8#r9": 40
  "§4.8#r10": 49
  "§4.8#r11": 53
  "§4.8#r12": 41
  "§4.8#r13": 42
  "§4.8#r14": 78
  "§4.8#r15": 2
  "§4.8#r16": 72
  "§4.8#r17": 32
  "§2.1#b1": [70, 72]
  "§2.1#b2": 4
  "§2.1#b3": 40
  "§4.8#p1": 77
  "§4.8#p2": 65
anchor: [14, 35, 52, 69]
coverage:
  web: automated
---

# Gating Total Control: elemen Show, Hidden, dan Disabled menurut matriks role

## Prerequisites
- Aktor: Total Control, user DU-043-1, mengerjakan seluruh langkah; Assignee dan pengaju adalah user lain di Data
- Layar awal: Fixed Asset, halaman mana pun dengan sidebar dan navbar tampil
- Data:
  - DU-043-1: User (Aktor Total Control), Name `Tania Kusuma {runId}`, Role `Total Control`, Cakupan `Seluruh client`, Tampil sebagai Assignee `Tania K`
  - DU-043-2: User (Assignee Employee), Name `Budi Santoso {runId}`, Role `tanpa role Assignment`, Tampil sebagai Assignee `Budi S`
  - DU-043-3: User (Pengaju pengajuan), Name `Agus Prasetyo {runId}`, Role `Asset Admin`, Cakupan `Head Office {runId}`, Tampil sebagai pengaju `Agus P`
  - DU-043-4: Group (Group utama), Name `Head Office {runId}`, Sub-group `IT Head Office {runId}`
  - DU-043-5: Group (Group cabang), Name `Branch Surabaya {runId}`
  - DU-043-6: Division (Division dengan PIC), Name `Finance {runId}`, PIC `Budi Santoso {runId}`, Anggota lain `Sari Dewi {runId}`
  - DU-043-7: Draft (Draft berisi aset satu Group), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Aset `Laptop Dell Latitude 5420 {runId}`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-043-8: Draft (Draft berisi aset dua Group), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId} dan Branch Surabaya {runId}`, Aset 1 `Monitor LG 24 {runId}`, Group Aset 1 `Head Office {runId}`, Aset 2 `Toyota Avanza {runId}`, Group Aset 2 `Branch Surabaya {runId}`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-043-9: Draft (Draft berisi aset satu Group cabang), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Branch Surabaya {runId}`, Aset `Genset Honda EU22 {runId}`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-043-10: Draft (Draft berisi aset dengan Deny pada override), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Aset `Plotter Canon iPF770 {runId}`, Override Allow Assign aset `Deny`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-043-11: Assignment (ASG Waiting for Handover Employee), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Printer HP M404 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-043-12: Assignment (ASG Waiting for Handover Division), Assignee `Finance {runId}`, Assignee Type `Division`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Projector Epson EB-X49 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, PIC `Budi Santoso {runId}`
  - DU-043-13: Assignment (ASG Waiting for Handover di Group cabang), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Branch Surabaya {runId}`, Status `Waiting for Handover`, Aset `Tablet Samsung Tab S8 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-043-14: Assignment (ASG Waiting for Approval), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Approval`, Aset `Server Dell R740 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Waiting`, Approver aset `Tania Kusuma {runId}`
  - DU-043-15: Assignment (ASG Waiting for Approval dengan Assignee aktor), Assignee `Tania Kusuma {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Approval`, Aset `Mouse Logitech MX Master {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Waiting`, Approver aset `Tania Kusuma {runId}`
  - DU-043-16: Assignment (ASG milik aktor sebagai Assignee), Assignee `Tania Kusuma {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset 1 `Scanner Canon DR-C225 {runId}`, Aset 2 `Keyboard Logitech K380 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, Aset Assigned `Scanner Canon DR-C225 {runId}`, Aset Waiting for Handover `Keyboard Logitech K380 {runId}`, Sesi Confirm Handover `Aktif untuk Keyboard Logitech K380 {runId}`
  - DU-043-17: Assignment (ASG Assigned dengan laporan Damaged dan Missing), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Assigned`, Aset 1 `Camera Sony A7 {runId}`, Aset 2 `Laptop Asus ExpertBook {runId}`, Aset 3 `Tablet Lenovo Tab M10 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, Laporan Damaged `Laptop Asus ExpertBook {runId} dilaporkan oleh Tania Kusuma {runId}, Waiting for Confirmation`, Laporan Missing `Tablet Lenovo Tab M10 {runId} dilaporkan oleh Budi Santoso {runId}, Waiting for Confirmation`
  - DU-043-18: Assignment (ASG Assigned di Group cabang), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Branch Surabaya {runId}`, Status `Assigned`, Aset `Drone DJI Mavic 3 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-043-19: Division (Division dengan aktor sebagai PIC), Name `Operations {runId}`, PIC `Tania Kusuma {runId}`, Anggota lain `Rina Wijaya {runId}`
  - DU-043-20: Assignment (ASG Division Waiting for Handover dengan PIC aktor), Assignee `Operations {runId}`, Assignee Type `Division`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Docking Station Dell WD19 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, PIC `Tania Kusuma {runId}`
  - DU-043-21: Assignment (ASG Division Assigned dengan PIC aktor), Assignee `Operations {runId}`, Assignee Type `Division`, Group `Head Office {runId}`, Status `Assigned`, Aset `Scanner Epson DS-530 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, PIC `Tania Kusuma {runId}`
- Kondisi:
  - Feature Suite Assignment berada pada level `Full`
  - Jendela konfirmasi Handover bernilai `15 menit`
  - Sesi Confirm Handover untuk aset `Keyboard Logitech K380 {runId}` aktif: Request Confirmation sudah ditekan dan jendela konfirmasi belum habis
  - Aturan approval aset `Server Dell R740 {runId}` menunjuk aktor sebagai approver; pengaju bukan aktor

## Test Steps

### Menu Assignment di sidebar
1. Verifikasi menu `Transactions > Assignment` tampil di sidebar
2. Verifikasi menu `Approvals > Assignment` tampil di sidebar

### Quick Action Assign membuka form Assignment Request
3. Klik Quick Action pada navbar
4. Verifikasi item `Assign` tampil pada menu Quick Action
5. Klik `Assign`
6. Verifikasi form `Assignment Request` terbuka
7. Verifikasi tombol `[Save Draft]` tampil
8. Verifikasi tombol `[Submit]` tampil
9. Klik `[Cancel]` pada form yang belum diubah

### Daftar dan Detail ASG sesuai cakupan
10. Klik menu `Transactions > Assignment`
11. Verifikasi tab `Transactions`, `Assigned Assets`, dan `History` tampil
12. Verifikasi tab `Drafts` tampil
13. Ketik Search `{runId}`, tekan Enter
14. Verifikasi ASG dengan Group `Head Office {runId}` tampil pada daftar
15. Verifikasi ASG dengan Group `Branch Surabaya {runId}` tampil pada daftar
16. Ganti isi kotak Search dengan `Tablet Samsung Tab S8 {runId}`, tekan Enter
17. Klik Transaction ID pada baris ASG yang memuat aset `Tablet Samsung Tab S8 {runId}`
18. Verifikasi Assignment Detail terbuka dan memuat aset `Tablet Samsung Tab S8 {runId}`

### Aksi baris ASG pada tab Transactions
19. Klik menu `Transactions > Assignment`
20. Ketik Search `Printer HP M404 {runId}`, tekan Enter
21. Buka menu ⋯ pada baris ASG yang memuat aset `Printer HP M404 {runId}`
22. Verifikasi aksi `Hand Over` tampil dan aktif
23. Verifikasi aksi `Remind Assignee` tampil dan aktif
24. Verifikasi aksi `Cancel Assignment` tampil dan aktif
25. Ganti isi kotak Search dengan `Keyboard Logitech K380 {runId}`, tekan Enter
26. Buka menu ⋯ pada baris ASG yang memuat aset `Keyboard Logitech K380 {runId}`
27. Verifikasi aksi `Hand Over` tampil Disabled karena aktor adalah Assignee ASG ini
28. Verifikasi aksi `Remind Assignee` tampil Disabled karena aktor adalah Assignee ASG ini
29. Ganti isi kotak Search dengan `Projector Epson EB-X49 {runId}`, tekan Enter
30. Buka menu ⋯ pada baris ASG yang memuat aset `Projector Epson EB-X49 {runId}`
31. Verifikasi aksi `Change PIC` tampil dan aktif
32. Verifikasi tombol `Download` tampil pada toolbar tab `Transactions`[^drift-1]

### Aksi per aset pada tab Assigned Assets
33. Klik tab `Assigned Assets`
34. Ketik Search `{runId}`, tekan Enter
35. Verifikasi aset `Camera Sony A7 {runId}` dari ASG milik `Budi S` tampil pada By Asset
36. Verifikasi aset `Drone DJI Mavic 3 {runId}` dengan Group `Branch Surabaya {runId}` tampil pada By Asset
37. Ganti isi kotak Search dengan `Camera Sony A7 {runId}`, tekan Enter
38. Buka menu ⋯ pada baris aset `Camera Sony A7 {runId}`
39. Verifikasi aksi `Unassign` tampil dan aktif
40. Verifikasi aksi `Report Damaged` tampil dan aktif
41. Verifikasi aksi `Report Missing` tampil dan aktif
42. Verifikasi aksi `Mark as Unassigned` tidak tampil karena level Feature Suite bukan `None`
43. Ganti isi kotak Search dengan `Scanner Canon DR-C225 {runId}`, tekan Enter
44. Buka menu ⋯ pada baris aset `Scanner Canon DR-C225 {runId}`
45. Verifikasi aksi `Unassign` tampil Disabled karena aktor adalah Assignee ASG aset ini
46. Verifikasi alasan `You can't hand over or receive your own assignment.` tersampaikan pada aksi `Unassign` yang disabled
47. Ganti isi kotak Search dengan `Laptop Asus ExpertBook {runId}`, tekan Enter
48. Buka menu ⋯ pada baris aset `Laptop Asus ExpertBook {runId}`
49. Verifikasi aksi `Cancel Damage Report` tampil untuk laporan kerusakan milik aktor yang masih `Waiting for Confirmation`
50. Ganti isi kotak Search dengan `Tablet Lenovo Tab M10 {runId}`, tekan Enter
51. Buka menu ⋯ pada baris aset `Tablet Lenovo Tab M10 {runId}`
52. Verifikasi aksi `Assignment Log` tampil
53. Verifikasi aksi `Cancel Missing Report` tidak tampil

### Tab Drafts dan aksi Draft
54. Klik tab `Drafts`
55. Ketik Search `{runId}`, tekan Enter
56. Verifikasi Draft dengan aset `Genset Honda EU22 {runId}` dan Group `Branch Surabaya {runId}` tampil
57. Ganti isi kotak Search dengan `Toyota Avanza {runId}`, tekan Enter
58. Verifikasi aksi `Edit` tampil pada Draft yang memuat aset `Toyota Avanza {runId}`
59. Verifikasi aksi `Delete` tampil dan aktif pada Draft yang memuat aset `Toyota Avanza {runId}`
60. Klik `Edit` pada Draft yang memuat aset `Toyota Avanza {runId}`
61. Verifikasi tombol `[Submit]` tampil dan aktif
62. Klik `[Cancel]` pada form yang belum diubah
63. Ganti isi kotak Search dengan `Plotter Canon iPF770 {runId}`, tekan Enter
64. Klik `Edit` pada Draft yang memuat aset `Plotter Canon iPF770 {runId}`
65. Verifikasi alasan `Can't be assigned: this asset is not available for assignment.` tersampaikan pada baris aset `Plotter Canon iPF770 {runId}`, disertai kontak yang bisa dihubungi, karena aset diblok kelayakan aset (Deny pada override), bukan role
66. Klik `[Cancel]` pada form yang belum diubah

### Antrean Approvals > Assignment dan keputusan per aset
67. Klik menu `Approvals > Assignment`
68. Ketik Search `{runId}`, tekan Enter
69. Verifikasi pengajuan dengan Assignee `Budi S` dan Group `Head Office {runId}` tampil pada tab `Active`
70. Verifikasi tidak ada pengajuan dengan Assignee `Tania K` pada tab `Active`
71. Klik `Review` pada pengajuan dengan Assignee `Budi S`
72. Verifikasi pilihan `Approve` dan `Reject` tampil pada kolom `Approval` aset `Server Dell R740 {runId}`
73. Klik `[Cancel]` pada footer halaman Review tanpa memutuskan

### Task Confirm Handover di My Asset
74. Buka menu Profile pada navbar
75. Klik `My Asset`
76. Agus Prasetyo `Agus P` menekan Request Confirmation untuk aset `Keyboard Logitech K380 {runId}`, sehingga sesi konfirmasi Handover aktif dan jendela `15 menit` belum habis
77. Verifikasi Task `Confirm Handover` untuk aset `Keyboard Logitech K380 {runId}` tampil karena aktor adalah Assignee ASG itu
78. Verifikasi Task `Confirm Handover` untuk aset `Printer HP M404 {runId}` tidak tampil

### Alasan Disabled Remind Assignee bagi aktor Assignee
79. Klik menu `Transactions > Assignment`
80. Ketik Search `Keyboard Logitech K380 {runId}`, tekan Enter
81. Buka menu ⋯ pada baris ASG yang memuat aset `Keyboard Logitech K380 {runId}`
82. Verifikasi alasan `You can't hand over or receive your own assignment.` tersampaikan pada aksi `Remind Assignee` yang disabled karena aktor adalah Assignee ASG ini

### Aksi Disabled bagi aktor PIC ASG Division
83. Ganti isi kotak Search dengan `Docking Station Dell WD19 {runId}`, tekan Enter
84. Buka menu ⋯ pada baris ASG yang memuat aset `Docking Station Dell WD19 {runId}`
85. Verifikasi aksi `Remind Assignee` tampil Disabled karena aktor adalah PIC ASG Division ini
86. Verifikasi aksi `Change PIC` tampil Disabled karena aktor adalah PIC ASG Division ini
87. Ganti isi kotak Search dengan `Scanner Epson DS-530 {runId}`, tekan Enter
88. Buka menu ⋯ pada baris ASG yang memuat aset `Scanner Epson DS-530 {runId}`
89. Verifikasi aksi `Unassign` tampil Disabled karena aktor adalah PIC ASG Division ini
90. Verifikasi alasan `You can't hand over or receive your own assignment.` tersampaikan pada aksi `Unassign` ASG Division yang disabled bagi PIC
91. Verifikasi alasan `You can't hand over or receive your own assignment.` tersampaikan pada aksi `Remind Assignee` ASG Division yang disabled bagi PIC

### Aksi baris Assigned Assets bagi aktor PIC ASG Division
92. Klik tab `Assigned Assets`
93. Ketik Search `Scanner Epson DS-530 {runId}`, tekan Enter
94. Buka menu ⋯ pada baris aset `Scanner Epson DS-530 {runId}`
95. Verifikasi aksi `Unassign` tampil Disabled karena aktor adalah PIC ASG Division aset ini
96. Verifikasi alasan `You can't hand over or receive your own assignment.` tersampaikan pada aksi `Unassign` baris aset yang disabled bagi PIC

[^drift-1]: Drift PRD vs foundation. PRD §5 Global Table Rules baris Download: nama dan tooltip tombol toolbar adalah `Export`, bukan `Download`. foundation `prd-conventions.md` §9.1: icon toolbar bernama `Download` dengan tooltip `Download`, dan modul tidak menulis ulang teks tooltip itu. Diasersi: foundation, karena tombol unduh di toolbar tabel adalah pola bersama (SB-4).

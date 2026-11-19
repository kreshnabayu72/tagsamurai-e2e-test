---
id: TC-FA-ASSIGN-E2E-027-approve-any-one-approver
title: "Approve per aset dengan Approval type Any one approver"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§3#p7", "T-ASG-08", "§4.1#r19", "§4.4#r7", "TS-ASG-06", "FI-ASG-113", "FI-ASG-114", "FI-ASG-115", "FI-ASG-116", "FI-ASG-117", "FI-ASG-118", "EC-ASG-84"]
smoke: []
dependsOn: []
trace:
  "§3#p7": [4, 35, 37, 40, 41, 56, 66, 76]
  "T-ASG-08": [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 80, 81, 82, 83, 84, 86, 92, 93, 94, 96, 98, 100, 102, 104, 106, 127, 128, 129]
  "§4.1#r19": [3, 4]
  "§4.4#r7": [45, 46]
  "TS-ASG-06": [32, 53, 63, 73, 116]
  "FI-ASG-113": [11, 28]
  "FI-ASG-114": [13, 23, 25, 26, 110, 111, 121, 122]
  "FI-ASG-115": 15
  "FI-ASG-116": [12, 13, 26]
  "FI-ASG-117": [10, 32, 45, 46, 50]
  "FI-ASG-118": [45, 46]
  "EC-ASG-84": [14, 17, 18, 19]
anchor: []
coverage:
  web: automated
---

# Approve per aset dengan Approval type Any one approver

## Prerequisites
- Aktor: Approver `Rina Wulandari {runId}` (DU-027-1).
- Layar awal: Approvals > Assignment > Active.
- Data:
  - DU-027-1: User `Rina Wulandari {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`. Daftar Active-nya hanya berisi DU-027-5 sampai DU-027-8 dan DU-027-12.
  - DU-027-2: User `Tono Wibowo {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`, approver kedua pada semua aset Any one yang approver-nya dua orang, satu-satunya approver `Genset Cummins C100 {runId}`, dan satu-satunya approver `Scanner Epson DS-530 {runId}` di DU-027-12.
  - DU-027-3: User `Agus Pratama {runId}`, Role `Asset Admin`, Group penugasan `Head Office`, pengaju DU-027-5 sampai DU-027-8.
  - DU-027-4: User `Dewi Anggraini {runId}`, Role `Total Control`, pemutus `Forklift Toyota 8FD {runId}` lewat override.
  - DU-027-5: Pengajuan A, Group `Head Office`, Assignee `Sari Dewi {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 2 hari, pukul 09:00`, Confirmation Rule `Yes`, Approval type `Any one approver`; aset `Toyota Avanza {runId}` (Purpose `Field visits`, tanpa Brand, Model/Type, dan foto utama) dan `Excavator PC200 {runId}` (Purpose `Site work`) dengan approver `Rina Wulandari {runId}` dan `Tono Wibowo {runId}`, belum diputuskan; aset `Genset Cummins C100 {runId}` (Purpose `Field visits`) dengan approver hanya `Tono Wibowo {runId}`, belum diputuskan; aset `Forklift Toyota 8FD {runId}` (Purpose `Site work`) dengan approver `Rina Wulandari {runId}` dan `Tono Wibowo {runId}`, sudah `Approved` oleh `Dewi Anggraini {runId}` lewat Total Control override.
  - DU-027-6: Pengajuan B, Group `Head Office`, Assignee `Budi Santoso {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 3 hari, pukul 10:00`, Confirmation Rule `Yes`, Approval type `Any one approver`; satu aset `Printer HP M404 {runId}` (Purpose `Field visits`) dengan approver `Rina Wulandari {runId}` dan `Tono Wibowo {runId}`, belum diputuskan.
  - DU-027-7: Pengajuan C, Group `Head Office`, Assignee `Hana Putri {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 4 hari, pukul 11:30`, Confirmation Rule `Yes`, Approval type `Any one approver`; aset `Projector Epson EB-X49 {runId}` (Purpose `Field visits`) dan `Tablet Samsung Tab S8 {runId}` (Purpose `Site work`) dengan approver `Rina Wulandari {runId}` dan `Tono Wibowo {runId}`, belum diputuskan.
  - DU-027-8: Pengajuan D, Group `Head Office`, Assignee `Dewi Lestari {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 5 hari, pukul 13:15`, Confirmation Rule `Yes`, Approval type `Any one approver`; satu aset `Kamera Sony A7 {runId}` (Purpose `Site work`) dengan approver `Rina Wulandari {runId}` dan `Tono Wibowo {runId}`, belum diputuskan.
  - DU-027-12: Pengajuan E, Group `Head Office`, Assignee `Lina Marlina {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 6 hari, pukul 14:40`, Approval type `Any one approver`; aset `Laptop Lenovo T14 {runId}` (Brand `Lenovo`, Model/Type `ThinkPad T14`, Category `Computer`, Purpose `Site work`, Confirmation Rule `Yes`, memiliki foto utama) dengan approver tunggal `Rina Wulandari {runId}`; aset `Monitor Dell P2422 {runId}` (Brand `Dell`, Model/Type `P2422H`, Category `Audio Visual`, Purpose `Field visits`, Confirmation Rule `No`) dengan approver `Rina Wulandari {runId}` dan `Tono Wibowo {runId}`; aset `Scanner Epson DS-530 {runId}` (Brand `Epson`, Model/Type `DS-530`, Category `Office Equipment`, Purpose `Inventory audit`, Confirmation Rule `Yes`) dengan approver tunggal `Tono Wibowo {runId}`; ketiganya belum diputuskan.
  - DU-027-9: Approval Note `Site work postponed`, diisi pada `Excavator PC200 {runId}`.
  - DU-027-10: Approval Note `Unit sedang dalam perawatan`, diisi pada `Tablet Samsung Tab S8 {runId}`.
  - DU-027-11: Approval Note `Aset dipakai proyek lain`, diisi pada `Kamera Sony A7 {runId}`.
  - DU-027-13: Approval Note `Anggaran belum disetujui`, diisi pada `Laptop Lenovo T14 {runId}`.
  - DU-027-14: Approval Note `Perangkat dipakai proyek lain`, diisi pada `Monitor Dell P2422 {runId}`.

## Test Steps

### Halaman Review menampilkan seluruh aset pengajuan dan keterangan Not your approval
1. Ketik Search `Sari Dewi {runId}`, tekan Enter
2. Klik `Transaction ID` pada baris `Sari Dewi {runId}`
3. Verifikasi halaman Review pengajuan `Sari Dewi {runId}` terbuka dengan seluruh asetnya
4. Verifikasi tabel Review menampilkan aset `Toyota Avanza {runId}`, `Excavator PC200 {runId}`, `Genset Cummins C100 {runId}`, dan `Forklift Toyota 8FD {runId}`
5. Verifikasi tabel Review menampilkan kolom `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Purpose`, `Confirmation Rule`, `Approval Rule`, `Approval`, dan `Approval Note`
6. Verifikasi kolom `TAG` dan `Category` tidak tampil secara bawaan
7. Verifikasi `Purpose` pada baris `Toyota Avanza {runId}` bernilai `Field visits`
8. Verifikasi `Confirmation Rule` pada baris `Toyota Avanza {runId}` bernilai `Yes`
9. Verifikasi `Approval Rule` pada baris `Toyota Avanza {runId}` bernilai `Any one approver · Waiting for Approval`
10. Verifikasi `Approval` pada baris `Toyota Avanza {runId}` bernilai `Approve` secara bawaan
11. Verifikasi `Approval Note` pada baris `Toyota Avanza {runId}` memakai placeholder `Enter approval note`
12. Verifikasi `Approval` dan `Approval Note` pada baris `Genset Cummins C100 {runId}` read-only dengan keterangan `Not your approval`
13. Verifikasi baris `Genset Cummins C100 {runId}` tidak dapat dicentang untuk bulk action
14. Verifikasi `Approval Rule` pada baris `Forklift Toyota 8FD {runId}` bernilai `Approved`
15. Verifikasi tidak ada kolom `Approve Duration` pada tabel Review

### Approval Progress menampilkan aktor override dan approver snapshot yang belum bertindak
16. Klik sel `Approval Rule` pada baris `Forklift Toyota 8FD {runId}`
17. Verifikasi dialog `Approval Progress` memuat baris tambahan `Dewi Anggraini {runId}` berstatus `Approved` dengan keterangan `Total Control override`
18. Verifikasi approver `Rina Wulandari {runId}` berstatus `Not Involved` pada dialog `Approval Progress`
19. Verifikasi approver `Tono Wibowo {runId}` berstatus `Not Involved` pada dialog `Approval Progress`
20. Klik ikon silang pada dialog `Approval Progress`

### Bulk action hanya mencakup aset milik approver
21. Centang baris `Toyota Avanza {runId}`
22. Centang baris `Excavator PC200 {runId}`
23. Verifikasi toolbar bulk tampil
24. Pilih aksi bulk `Approve`
25. Verifikasi `Approval` pada baris `Toyota Avanza {runId}` dan baris `Excavator PC200 {runId}` bernilai `Approve`
26. Verifikasi `Approval` pada baris `Genset Cummins C100 {runId}` tetap read-only dengan keterangan `Not your approval`

### Reject pada satu aset memakai toggle Approval dan Approval Note
27. Ubah toggle `Approval` pada baris `Excavator PC200 {runId}` menjadi `Reject`
28. Verifikasi toggle `Approval` pada baris `Excavator PC200 {runId}` berlabel `Reject`
29. Isi `Approval Note` pada baris `Excavator PC200 {runId}` dengan `Site work postponed`

### Submit mengirim keputusan seluruh aset milik approver sekaligus dan pengajuan masih menunggu approver lain
30. Klik `[Submit]` pada halaman Review
31. Klik `[Submit]` pada dialog `Submit Approval`
32. Verifikasi toast `Success, your approval has been recorded. Waiting for the other approvers.`

### Pengajuan pindah dari Active ke History dengan hasil keputusan approver
33. Klik tab `History`
34. Ganti isi kotak search dengan `Sari Dewi {runId}`, tekan Enter
35. Verifikasi baris `Sari Dewi {runId}` tampil di tab `History` dengan Status `Waiting for Approval`
36. Arahkan kursor ke badge `Status` pada baris `Sari Dewi {runId}`
37. Verifikasi hover pada badge `Status` baris `Sari Dewi {runId}` berisi `1 approved · 1 rejected`, jumlah aset yang diputuskan
38. Klik tab `Active`
39. Ganti isi kotak search dengan `{runId}`, tekan Enter
40. Verifikasi baris `Budi Santoso {runId}` tampil di tab `Active`
41. Verifikasi tidak ada baris dengan Assignee `Sari Dewi {runId}` di tab `Active` karena seluruh aset milik approver sudah diputuskan

### Keputusan Any one langsung final dan tampil sebagai hasil
42. Klik tab `History`
43. Klik `⋯` pada baris `Sari Dewi {runId}`
44. Klik `Detail`
45. Verifikasi keputusan pertama menetapkan aset `Toyota Avanza {runId}` sebagai `Approved`
46. Verifikasi keputusan pertama menetapkan aset `Excavator PC200 {runId}` sebagai `Rejected`
47. Klik `History` pada breadcrumb

### Approve seluruh aset milik approver menghasilkan toast approved
48. Klik tab `Active`
49. Klik `Transaction ID` pada baris `Budi Santoso {runId}`
50. Verifikasi `Approval` pada baris `Printer HP M404 {runId}` bernilai `Approve` secara bawaan
51. Klik `[Submit]` pada halaman Review
52. Klik `[Submit]` pada dialog `Submit Approval`
53. Verifikasi toast `Success, assignment has been approved.`
54. Klik tab `History`
55. Ganti isi kotak search dengan `Budi Santoso {runId}`, tekan Enter
56. Verifikasi baris `Budi Santoso {runId}` tampil di tab `History` dengan Status `Approved`

### Keputusan campuran menghasilkan toast partially approved
57. Klik tab `Active`
58. Klik `Transaction ID` pada baris `Hana Putri {runId}`
59. Ubah toggle `Approval` pada baris `Tablet Samsung Tab S8 {runId}` menjadi `Reject`
60. Isi `Approval Note` pada baris `Tablet Samsung Tab S8 {runId}` dengan `Unit sedang dalam perawatan`
61. Klik `[Submit]` pada halaman Review
62. Klik `[Submit]` pada dialog `Submit Approval`
63. Verifikasi toast `Success, assignment has been partially approved.`
64. Klik tab `History`
65. Ganti isi kotak search dengan `Hana Putri {runId}`, tekan Enter
66. Verifikasi baris `Hana Putri {runId}` tampil di tab `History` dengan Status `Partially Approved`

### Reject seluruh aset milik approver menghasilkan toast rejected
67. Klik tab `Active`
68. Klik `Transaction ID` pada baris `Dewi Lestari {runId}`
69. Ubah toggle `Approval` pada baris `Kamera Sony A7 {runId}` menjadi `Reject`
70. Isi `Approval Note` pada baris `Kamera Sony A7 {runId}` dengan `Aset dipakai proyek lain`
71. Klik `[Submit]` pada halaman Review
72. Klik `[Submit]` pada dialog `Submit Approval`
73. Verifikasi toast `Success, assignment has been rejected.`
74. Klik tab `History`
75. Ganti isi kotak search dengan `Dewi Lestari {runId}`, tekan Enter
76. Verifikasi baris `Dewi Lestari {runId}` tampil di tab `History` dengan Status `Rejected`

### Format Approval Rule, Confirmation Rule, Brand, dan Model/Type pada tabel Review
77. Klik tab `Active`
78. Ganti isi kotak search dengan `Lina Marlina {runId}`, tekan Enter
79. Klik `Transaction ID` pada baris `Lina Marlina {runId}`
80. Verifikasi tabel Review memuat baris `Laptop Lenovo T14 {runId}`, `Monitor Dell P2422 {runId}`, dan `Scanner Epson DS-530 {runId}`
81. Verifikasi `Approval Rule` pada baris `Laptop Lenovo T14 {runId}` memuat nama singkat `Rina W`, dari `Rina Wulandari {runId}`, dengan penanda `(You)` dan status `Waiting for Approval`
82. Verifikasi `Approval Rule` pada baris `Scanner Epson DS-530 {runId}` bernilai `Tono W · Waiting for Approval`, nama singkat dari `Tono Wibowo {runId}`
83. Verifikasi `Confirmation Rule` pada baris `Laptop Lenovo T14 {runId}` bernilai `Yes` dan pada baris `Monitor Dell P2422 {runId}` bernilai `No`
84. Verifikasi `Brand` dan `Model/Type` pada baris `Laptop Lenovo T14 {runId}` bernilai `Lenovo` dan `ThinkPad T14`

### Foto aset membuka pratinjau
85. Klik `Photo` pada baris `Laptop Lenovo T14 {runId}`
86. Verifikasi pratinjau foto utama aset `Laptop Lenovo T14 {runId}` terbuka
87. Tutup pratinjau foto

### Kolom TAG dan Category ditampilkan lewat Setup Column
88. Klik header kolom `Actions` pada tabel Review
89. Klik `Setup Column...` pada panel Column Visibility
90. Centang kolom `TAG` dan `Category` pada modal Setup Column
91. Klik `[Save]`
92. Verifikasi kolom `TAG` dan `Category` tampil di tabel Review
93. Verifikasi `Category` pada baris `Laptop Lenovo T14 {runId}` bernilai `Computer`

### Sort kolom pada tabel Review
94. Verifikasi urutan awal baris dari atas ke bawah menurut `Name` A-Z: `Laptop Lenovo T14 {runId}`, `Monitor Dell P2422 {runId}`, `Scanner Epson DS-530 {runId}`
95. Klik header kolom `Brand`
96. Verifikasi kolom `Brand` terurut A-Z: `Monitor Dell P2422 {runId}` (`Dell`), `Scanner Epson DS-530 {runId}` (`Epson`), `Laptop Lenovo T14 {runId}` (`Lenovo`)
97. Klik header kolom `Model/Type`
98. Verifikasi kolom `Model/Type` terurut A-Z: `Scanner Epson DS-530 {runId}` (`DS-530`), `Monitor Dell P2422 {runId}` (`P2422H`), `Laptop Lenovo T14 {runId}` (`ThinkPad T14`)
99. Klik header kolom `Category`
100. Verifikasi kolom `Category` terurut A-Z: `Monitor Dell P2422 {runId}` (`Audio Visual`), `Laptop Lenovo T14 {runId}` (`Computer`), `Scanner Epson DS-530 {runId}` (`Office Equipment`)
101. Klik header kolom `Purpose`
102. Verifikasi kolom `Purpose` terurut A-Z: `Monitor Dell P2422 {runId}` (`Field visits`), `Scanner Epson DS-530 {runId}` (`Inventory audit`), `Laptop Lenovo T14 {runId}` (`Site work`)
103. Klik header kolom `Confirmation Rule`
104. Verifikasi kolom `Confirmation Rule` terurut A-Z: baris `Monitor Dell P2422 {runId}` (`No`) berada di atas baris `Laptop Lenovo T14 {runId}` dan `Scanner Epson DS-530 {runId}` (`Yes`)
105. Klik header kolom `Approval Rule`
106. Verifikasi kolom `Approval Rule` terurut A-Z: `Monitor Dell P2422 {runId}` (`Any one approver`), `Laptop Lenovo T14 {runId}` (`Rina W`), `Scanner Epson DS-530 {runId}` (`Tono W`)

### Bulk Reject beberapa aset milik approver beserta Approval Note
107. Centang baris `Laptop Lenovo T14 {runId}`
108. Centang baris `Monitor Dell P2422 {runId}`
109. Pilih aksi bulk `Reject`
110. Verifikasi `Approval` pada baris `Laptop Lenovo T14 {runId}` dan baris `Monitor Dell P2422 {runId}` bernilai `Reject`
111. Verifikasi `Approval` pada baris `Scanner Epson DS-530 {runId}` tetap read-only dengan keterangan `Not your approval`
112. Isi `Approval Note` pada baris `Laptop Lenovo T14 {runId}` dengan `Anggaran belum disetujui`
113. Isi `Approval Note` pada baris `Monitor Dell P2422 {runId}` dengan `Perangkat dipakai proyek lain`
114. Klik `[Submit]` pada halaman Review
115. Klik `[Submit]` pada dialog `Submit Approval`
116. Verifikasi toast `Success, your approval has been recorded. Waiting for the other approvers.`
117. Klik tab `History`
118. Ganti isi kotak search dengan `Lina Marlina {runId}`, tekan Enter
119. Klik `⋯` pada baris `Lina Marlina {runId}`
120. Klik `Detail`
121. Verifikasi `Approval Rule` pada baris `Laptop Lenovo T14 {runId}` bernilai `Rejected`
122. Verifikasi `Approval Rule` pada baris `Monitor Dell P2422 {runId}` bernilai `Rejected`
123. Klik `History` pada breadcrumb

### Nilai kosong Brand, Model/Type, dan Photo pada Detail read-only
124. Ganti isi kotak search dengan `Sari Dewi {runId}`, tekan Enter
125. Klik `⋯` pada baris `Sari Dewi {runId}`
126. Klik `Detail`
127. Verifikasi `Brand` pada baris `Toyota Avanza {runId}` bernilai `—`
128. Verifikasi `Model/Type` pada baris `Toyota Avanza {runId}` bernilai `—`
129. Verifikasi `Photo` pada baris `Toyota Avanza {runId}` memakai placeholder gambar standar
130. Klik `History` pada breadcrumb

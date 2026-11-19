---
id: TC-FA-ASSIGN-E2E-047-gating-monitoring-report-dan-read-only
title: "Gating Monitoring & Report dan Read Only: elemen Show, Hidden, dan Disabled menurut matriks role"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r8", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#r12", "§2.1#r13", "§2.1#r14", "§2.1#r15", "§2.1#r16", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§4.8#r15", "§4.8#r16", "§4.8#r17", "EB-AKS-4"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [8, 9, 65, 66]
  "§2.1#r2": [6, 63]
  "§2.1#r3": [5, 62]
  "§2.1#r4": [5, 62]
  "§2.1#r5": [15, 72]
  "§2.1#r6": [51, 108]
  "§2.1#r7": [13, 70]
  "§2.1#r8": [14, 71]
  "§2.1#r9": [19, 76]
  "§2.1#r10": [28, 85]
  "§2.1#r11": [29, 86]
  "§2.1#r12": [35, 92]
  "§2.1#r13": [30, 87]
  "§2.1#r14": [31, 88]
  "§2.1#r15": [20, 77]
  "§2.1#r16": [9, 24, 66, 81, 137]
  "§4.8#r1": [2, 4, 59, 61]
  "§4.8#r2": [5, 62]
  "§4.8#r3": [28, 85]
  "§4.8#r4": [6, 53, 63, 110]
  "§4.8#r5": [5, 62]
  "§4.8#r6": [5, 62]
  "§4.8#r7": [15, 72]
  "§4.8#r8": [13, 14, 70, 71]
  "§4.8#r9": [29, 86]
  "§4.8#r10": [35, 92]
  "§4.8#r11": [39, 96]
  "§4.8#r12": [30, 87]
  "§4.8#r13": [31, 88]
  "§4.8#r14": [57, 114]
  "§4.8#r15": [51, 108]
  "§4.8#r16": [51, 108]
  "§4.8#r17": [20, 77]
  "EB-AKS-4": [41, 45, 46, 50, 98, 102, 103, 107, 119, 123, 128, 132]
anchor: [12, 18, 23, 27, 34, 38, 56, 69, 75, 80, 84, 91, 95, 113, 122, 131, 136]
coverage:
  web: automated
---

# Gating Monitoring & Report dan Read Only: elemen Show, Hidden, dan Disabled menurut matriks role

## Prerequisites
- Aktor: Monitoring & Report, user DU-047-1, lalu Read Only, user DU-047-16; Assignee dan pengaju adalah user lain di Data
- Layar awal: Fixed Asset, halaman mana pun dengan sidebar dan navbar tampil
- Data:
  - DU-047-1: User (Aktor Monitoring & Report), Name `Maya Rahmawati {runId}`, Role `Monitoring & Report`, Cakupan `Group penugasan Head Office {runId}`, Tampil sebagai Assignee `Maya R`
  - DU-047-2: User (Assignee Employee), Name `Budi Santoso {runId}`, Role `tanpa role Assignment`, Tampil sebagai Assignee `Budi S`
  - DU-047-3: User (Pengaju pengajuan), Name `Agus Prasetyo {runId}`, Role `Asset Admin`, Cakupan `Head Office {runId}`, Tampil sebagai pengaju `Agus P`
  - DU-047-4: Group (Group utama), Name `Head Office {runId}`, Sub-group `IT Head Office {runId}`
  - DU-047-5: Group (Group cabang), Name `Branch Surabaya {runId}`
  - DU-047-6: Division (Division dengan PIC), Name `Finance {runId}`, PIC `Budi Santoso {runId}`, Anggota lain `Sari Dewi {runId}`
  - DU-047-7: Draft (Draft berisi aset satu Group), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Aset `Laptop Dell Latitude 5420 {runId}`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-047-8: Draft (Draft berisi aset dua Group), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId} dan Branch Surabaya {runId}`, Aset 1 `Monitor LG 24 {runId}`, Group Aset 1 `Head Office {runId}`, Aset 2 `Toyota Avanza {runId}`, Group Aset 2 `Branch Surabaya {runId}`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-047-9: Draft (Draft berisi aset satu Group cabang), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Branch Surabaya {runId}`, Aset `Genset Honda EU22 {runId}`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-047-10: Assignment (ASG Waiting for Handover Employee), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Printer HP M404 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-047-11: Assignment (ASG Waiting for Handover Division), Assignee `Finance {runId}`, Assignee Type `Division`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Projector Epson EB-X49 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, PIC `Budi Santoso {runId}`
  - DU-047-12: Assignment (ASG Waiting for Handover di Group cabang), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Branch Surabaya {runId}`, Status `Waiting for Handover`, Aset `Tablet Samsung Tab S8 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-047-13: Assignment (ASG Assigned milik aktor sebagai Assignee), Assignee `Maya Rahmawati {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Assigned`, Aset `Scanner Canon DR-C225 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-047-14: Assignment (ASG Assigned dengan laporan Damaged dan Missing), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Assigned`, Aset 1 `Camera Sony A7 {runId}`, Aset 2 `Laptop Asus ExpertBook {runId}`, Aset 3 `Tablet Lenovo Tab M10 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, Laporan Damaged `Laptop Asus ExpertBook {runId} dilaporkan oleh Budi Santoso {runId}, Waiting for Confirmation`, Laporan Missing `Tablet Lenovo Tab M10 {runId} dilaporkan oleh Budi Santoso {runId}, Waiting for Confirmation`
  - DU-047-15: Assignment (ASG Assigned di Group cabang), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Branch Surabaya {runId}`, Status `Assigned`, Aset `Drone DJI Mavic 3 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-047-16: User (Aktor Read Only), Name `Rudi Kurniawan {runId}`, Role `Read Only`, Cakupan `Seluruh client`, Tampil sebagai Assignee `Rudi K`
  - DU-047-17: Assignment (ASG Assigned milik aktor Read Only sebagai Assignee), Assignee `Rudi Kurniawan {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Assigned`, Aset `Webcam Logitech C920 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-047-18: User (Approver aset DU-047-19), Name `Putri Anggraini {runId}`, Role `Approver`, Cakupan `Group penugasan Head Office {runId} beserta descendant IT Head Office {runId}`
  - DU-047-19: Assignment (ASG Waiting for Approval), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Approval`, Aset `Headset Jabra Evolve2 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Waiting`, Approver aset `Putri Anggraini {runId}`
  - DU-047-20: Assignment (ASG Assigned di sub-group Group penugasan), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `IT Head Office {runId}`, Status `Assigned`, Aset `Smart TV Samsung 55 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
- Kondisi:
  - Feature Suite Assignment berada pada level `Full`
  - Akun `Maya Rahmawati {runId}` dan `Rudi Kurniawan {runId}` aktif, dan kredensial keduanya disediakan fase 2

## Test Steps

### Halaman Assignment untuk Monitoring & Report
1. Masuk sebagai Monitoring & Report `Maya Rahmawati {runId}`
2. Verifikasi menu `Transactions > Assignment` tampil di sidebar
3. Klik menu `Transactions > Assignment`
4. Verifikasi tab `Transactions`, `Assigned Assets`, dan `History` tampil
5. Verifikasi tab `Drafts` tidak tampil
6. Verifikasi tombol `[+ Assign]` tidak tampil pada toolbar
7. Ketik Search `{runId}`, tekan Enter
8. Verifikasi ASG dengan Group `Head Office {runId}` tampil pada daftar
9. Verifikasi ASG dengan Group `Branch Surabaya {runId}` tidak tampil pada daftar
10. Ganti isi kotak Search dengan `Printer HP M404 {runId}`, tekan Enter
11. Buka menu ⋯ pada baris ASG yang memuat aset `Printer HP M404 {runId}`
12. Verifikasi aksi `Detail` tampil
13. Verifikasi aksi `Hand Over` tidak tampil
14. Verifikasi aksi `Remind Assignee` tidak tampil
15. Verifikasi aksi `Cancel Assignment` tidak tampil
16. Ganti isi kotak Search dengan `Projector Epson EB-X49 {runId}`, tekan Enter
17. Buka menu ⋯ pada baris ASG yang memuat aset `Projector Epson EB-X49 {runId}`
18. Verifikasi aksi `Detail` tampil
19. Verifikasi aksi `Change PIC` tidak tampil
20. Verifikasi tombol `Download` tampil pada toolbar tab `Transactions`

### Assigned Assets untuk Monitoring & Report
21. Klik tab `Assigned Assets`
22. Ketik Search `{runId}`, tekan Enter
23. Verifikasi aset `Camera Sony A7 {runId}` dari ASG milik `Budi S` tampil pada By Asset
24. Verifikasi aset `Drone DJI Mavic 3 {runId}` dengan Group `Branch Surabaya {runId}` tidak tampil pada By Asset
25. Ganti isi kotak Search dengan `Camera Sony A7 {runId}`, tekan Enter
26. Buka menu ⋯ pada baris aset `Camera Sony A7 {runId}`
27. Verifikasi aksi `Assignment Log` tampil
28. Verifikasi aksi `Unassign` tidak tampil
29. Verifikasi aksi `Report Damaged` tidak tampil
30. Verifikasi aksi `Report Missing` tidak tampil
31. Verifikasi aksi `Mark as Unassigned` tidak tampil
32. Ganti isi kotak Search dengan `Laptop Asus ExpertBook {runId}`, tekan Enter
33. Buka menu ⋯ pada baris aset `Laptop Asus ExpertBook {runId}`
34. Verifikasi aksi `Assignment Log` tampil
35. Verifikasi aksi `Cancel Damage Report` tidak tampil
36. Ganti isi kotak Search dengan `Tablet Lenovo Tab M10 {runId}`, tekan Enter
37. Buka menu ⋯ pada baris aset `Tablet Lenovo Tab M10 {runId}`
38. Verifikasi aksi `Assignment Log` tampil
39. Verifikasi aksi `Cancel Missing Report` tidak tampil

### Fitur tabel untuk Monitoring & Report
40. Klik menu `Transactions > Assignment`
41. Verifikasi kotak Search, tombol Filter, kontrol Pagination, dan `Setup Column` tampil pada tab `Transactions`
42. Ketik Search `{runId}`, tekan Enter
43. Pilih Status `Waiting for Approval` pada Filter
44. Klik `[Apply]`
45. Verifikasi ASG dengan Group `Head Office {runId}` berstatus `Waiting for Approval` tampil pada daftar
46. Verifikasi ASG berstatus `Waiting for Handover` tidak tampil pada daftar
47. Klik `[Clear Field]`
48. Klik `[Apply]`
49. Klik header kolom `Status`
50. Verifikasi baris pertama berstatus `Assigned` dan baris terakhir berstatus `Waiting for Handover`

### Approvals, Quick Action, dan My Asset untuk Monitoring & Report
51. Verifikasi menu `Approvals > Assignment` tidak tampil di sidebar
52. Klik Quick Action pada navbar
53. Verifikasi item `Assign` tidak tampil pada menu Quick Action
54. Buka menu Profile pada navbar
55. Klik `My Asset`
56. Verifikasi aset `Scanner Canon DR-C225 {runId}` tampil pada tab `Assigned`
57. Verifikasi Task `Confirm Handover` tidak tampil

### Halaman Assignment untuk Read Only
58. Masuk sebagai Read Only `Rudi Kurniawan {runId}`
59. Verifikasi menu `Transactions > Assignment` tampil di sidebar
60. Klik menu `Transactions > Assignment`
61. Verifikasi tab `Transactions`, `Assigned Assets`, dan `History` tampil
62. Verifikasi tab `Drafts` tidak tampil
63. Verifikasi tombol `[+ Assign]` tidak tampil pada toolbar
64. Ketik Search `{runId}`, tekan Enter
65. Verifikasi ASG dengan Group `Head Office {runId}` tampil pada daftar
66. Verifikasi ASG dengan Group `Branch Surabaya {runId}` tampil pada daftar
67. Ganti isi kotak Search dengan `Printer HP M404 {runId}`, tekan Enter
68. Buka menu ⋯ pada baris ASG yang memuat aset `Printer HP M404 {runId}`
69. Verifikasi aksi `Detail` tampil
70. Verifikasi aksi `Hand Over` tidak tampil
71. Verifikasi aksi `Remind Assignee` tidak tampil
72. Verifikasi aksi `Cancel Assignment` tidak tampil
73. Ganti isi kotak Search dengan `Projector Epson EB-X49 {runId}`, tekan Enter
74. Buka menu ⋯ pada baris ASG yang memuat aset `Projector Epson EB-X49 {runId}`
75. Verifikasi aksi `Detail` tampil
76. Verifikasi aksi `Change PIC` tidak tampil
77. Verifikasi tombol `Download` tampil pada toolbar tab `Transactions`

### Assigned Assets untuk Read Only
78. Klik tab `Assigned Assets`
79. Ketik Search `{runId}`, tekan Enter
80. Verifikasi aset `Camera Sony A7 {runId}` dari ASG milik `Budi S` tampil pada By Asset
81. Verifikasi aset `Drone DJI Mavic 3 {runId}` dengan Group `Branch Surabaya {runId}` tampil pada By Asset
82. Ganti isi kotak Search dengan `Camera Sony A7 {runId}`, tekan Enter
83. Buka menu ⋯ pada baris aset `Camera Sony A7 {runId}`
84. Verifikasi aksi `Assignment Log` tampil
85. Verifikasi aksi `Unassign` tidak tampil
86. Verifikasi aksi `Report Damaged` tidak tampil
87. Verifikasi aksi `Report Missing` tidak tampil
88. Verifikasi aksi `Mark as Unassigned` tidak tampil
89. Ganti isi kotak Search dengan `Laptop Asus ExpertBook {runId}`, tekan Enter
90. Buka menu ⋯ pada baris aset `Laptop Asus ExpertBook {runId}`
91. Verifikasi aksi `Assignment Log` tampil
92. Verifikasi aksi `Cancel Damage Report` tidak tampil
93. Ganti isi kotak Search dengan `Tablet Lenovo Tab M10 {runId}`, tekan Enter
94. Buka menu ⋯ pada baris aset `Tablet Lenovo Tab M10 {runId}`
95. Verifikasi aksi `Assignment Log` tampil
96. Verifikasi aksi `Cancel Missing Report` tidak tampil

### Fitur tabel untuk Read Only
97. Klik menu `Transactions > Assignment`
98. Verifikasi kotak Search, tombol Filter, kontrol Pagination, dan `Setup Column` tampil pada tab `Transactions`
99. Ketik Search `{runId}`, tekan Enter
100. Pilih Status `Waiting for Approval` pada Filter
101. Klik `[Apply]`
102. Verifikasi ASG dengan Group `Head Office {runId}` berstatus `Waiting for Approval` tampil pada daftar
103. Verifikasi ASG berstatus `Waiting for Handover` tidak tampil pada daftar
104. Klik `[Clear Field]`
105. Klik `[Apply]`
106. Klik header kolom `Status`
107. Verifikasi baris pertama berstatus `Assigned` dan baris terakhir berstatus `Waiting for Handover`

### Approvals, Quick Action, dan My Asset untuk Read Only
108. Verifikasi menu `Approvals > Assignment` tidak tampil di sidebar
109. Klik Quick Action pada navbar
110. Verifikasi item `Assign` tidak tampil pada menu Quick Action
111. Buka menu Profile pada navbar
112. Klik `My Asset`
113. Verifikasi aset `Webcam Logitech C920 {runId}` tampil pada tab `Assigned`
114. Verifikasi Task `Confirm Handover` tidak tampil

### Pagination dan Setup Column untuk Monitoring & Report
115. Masuk sebagai Monitoring & Report `Maya Rahmawati {runId}`
116. Klik menu `Transactions > Assignment`
117. Klik dropdown rows per page
118. Pilih ukuran halaman `25`
119. Verifikasi ukuran halaman yang terpilih adalah `25`
120. Klik header kolom `Actions`
121. Hilangkan centang kolom `Requested By` pada panel Column Visibility
122. Verifikasi kolom `Status` tetap tampil pada tab `Transactions`
123. Verifikasi kolom `Requested By` tidak tampil pada tab `Transactions` milik aktor ini

### Pagination dan Setup Column untuk Read Only
124. Masuk sebagai Read Only `Rudi Kurniawan {runId}`
125. Klik menu `Transactions > Assignment`
126. Klik dropdown rows per page
127. Pilih ukuran halaman `25`
128. Verifikasi ukuran halaman yang terpilih adalah `25`
129. Klik header kolom `Actions`
130. Hilangkan centang kolom `Requested By` pada panel Column Visibility
131. Verifikasi kolom `Status` tetap tampil pada tab `Transactions`
132. Verifikasi kolom `Requested By` tidak tampil pada tab `Transactions` milik aktor ini

### Sub-group tidak masuk cakupan Monitoring & Report
133. Masuk sebagai Monitoring & Report `Maya Rahmawati {runId}`
134. Klik menu `Transactions > Assignment`
135. Ketik Search `{runId}`, tekan Enter
136. Verifikasi ASG dengan Group `Head Office {runId}` tampil pada daftar
137. Verifikasi ASG dengan Group `IT Head Office {runId}` yang memuat aset `Smart TV Samsung 55 {runId}` tidak tampil pada daftar



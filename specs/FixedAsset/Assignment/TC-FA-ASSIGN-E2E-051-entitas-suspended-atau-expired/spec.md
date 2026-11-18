---
id: TC-FA-ASSIGN-E2E-051-entitas-suspended-atau-expired
title: "Entitas Suspended atau Expired: aksi tulis ditolak"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-AKS-7", "EC-ASG-97", "F-ASSIGN-03.k6"]
smoke: []
dependsOn: []
trace:
  "EB-AKS-7": [3, 9, 13, 19, 23, 29, 30, 40, 41, 51, 52, 57, 60, 64, 69, 72, 79, 82, 92, 93, 100, 101, 105]
  "EC-ASG-97": [9, 10, 13, 29, 40, 51, 57, 64, 69, 79, 92, 100, 105, 109, 115, 117, 124, 129]
  "F-ASSIGN-03.k6": 44
anchor: [18]
coverage:
  web: automated
---

# Entitas Suspended atau Expired: aksi tulis ditolak

## Prerequisites
- Aktor: Total Control `Wulan Hartati {runId}` (DU-051-2) di entitas khusus DU-051-1 yang tidak dipakai spec lain
- Layar awal: Fixed Asset, halaman mana pun dengan sidebar dan navbar tampil
- Data:
  - DU-051-1: Entitas (Entitas khusus berstatus Suspended), Name `Entitas Terkunci {runId}`, Status `Suspended`, Level Feature Suite Assignment `Full`
  - DU-051-2: User (Aktor Total Control), Name `Wulan Hartati {runId}`, Role `Total Control`, Cakupan `Seluruh client`
  - DU-051-3: User (Assignee Employee), Name `Budi Santoso {runId}`, Role `tanpa role Assignment`, Tampil sebagai Assignee `Budi S`
  - DU-051-4: User (Anggota Division pengganti PIC), Name `Sari Dewi {runId}`, Role `tanpa role Assignment`
  - DU-051-5: User (Pengaju pengajuan), Name `Agus Prasetyo {runId}`, Role `Asset Admin`, Cakupan `Head Office {runId}`
  - DU-051-6: Group (Group utama), Name `Head Office {runId}`
  - DU-051-7: Division (Division dengan PIC nonaktif), Name `Finance {runId}`, PIC `Dedi Hartono {runId}`, Status PIC `Nonaktif`, Anggota lain `Sari Dewi {runId}`
  - DU-051-8: Draft (Draft yang dicoba disimpan dan diajukan), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Aset `Laptop Dell Latitude 5420 {runId}`, Purpose `Perangkat kerja tim lapangan`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-051-9: Draft (Draft yang dicoba dihapus), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Aset `Monitor LG 24 {runId}`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-051-10: Assignment (Input Purpose yang ditolak), Purpose `Dipakai tim operasional lapangan`, Aset `Laptop Dell Latitude 5420 {runId}`
  - DU-051-11: Assignment (ASG Waiting for Handover yang dicoba dibatalkan), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Printer HP M404 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-051-12: Assignment (ASG Division berjalan dengan No PIC), Assignee `Finance {runId}`, Assignee Type `Division`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Projector Epson EB-X49 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, PIC `Dedi Hartono {runId}`, Penanda `No PIC`
  - DU-051-13: Assignment (ASG Waiting for Approval yang melewati Transaction timeout), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Approval`, Aset `Server Dell R740 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Waiting`
  - DU-051-14: Assignment (ASG Waiting for Handover yang dicoba diserahkan), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Router Cisco ISR {runId}`, Jenis aset `Non TAG`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-051-15: Assignment (ASG Assigned yang dicoba di-Unassign), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Assigned`, Aset `Camera Sony A7 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-051-16: Assignment (ASG Waiting for Approval yang dicoba di-Approve), Assignee `Sari Dewi {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Approval`, Aset `Scanner Epson DS-530 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Waiting`, Approver aset `Wulan Hartati {runId}`
  - DU-051-17: Draft (Draft pertama yang dicoba dihapus secara bulk), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Aset `Kursi Ergonomis {runId}`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-051-18: Draft (Draft kedua yang dicoba dihapus secara bulk), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Aset `Meja Kerja Staf {runId}`, Origin `New`, Modified By `Agus Prasetyo {runId}`
  - DU-051-19: Assignment (ASG Waiting for Handover dengan sesi Confirm Handover aktif), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Handover`, Aset `Modem Huawei E5576 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, Sesi Confirm Handover `Aktif untuk Modem Huawei E5576 {runId}`
- Kondisi:
  - Status entitas aktor adalah `Suspended`
  - Feature Suite Assignment berada pada level `Full`
  - Transaction timeout untuk ASG yang memuat aset `Server Dell R740 {runId}` terlampaui
  - Aset `Router Cisco ISR {runId}` adalah aset Non TAG, sehingga tidak perlu di-scan untuk Handover
  - Need recipient confirmation efektif bernilai `No` untuk aset `Router Cisco ISR {runId}`, dan Photo at start serta Photo at end bernilai `OFF`
  - Sesi Confirm Handover untuk aset `Modem Huawei E5576 {runId}` aktif: Request Confirmation sudah ditekan dan jendela konfirmasi Handover bernilai `15 menit`

## Test Steps

### Modul tetap terbuka dan terbaca
1. Klik menu `Transactions > Assignment`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi ASG dengan Group `Head Office {runId}` tampil pada daftar tanpa gerbang akses dan tanpa redirect

### Save Draft ditolak
4. Klik tab `Drafts`
5. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
6. Klik `Edit` pada Draft yang memuat aset `Laptop Dell Latitude 5420 {runId}`
7. Isi Purpose aset `Laptop Dell Latitude 5420 {runId}` dengan `Dipakai tim operasional lapangan`
8. Klik `[Save Draft]`
9. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
10. Verifikasi toast `You don't have permission to do this.` tidak tampil

### Submit ditolak
11. Klik `[Submit]`
12. Klik `[Submit]` pada dialog `Submit Assignment`
13. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
14. Klik `[Cancel]` pada form
15. Klik `[Leave]`
16. Klik menu `Transactions > Assignment`
17. Ketik Search `{runId}`, tekan Enter
18. Verifikasi ASG dengan Group `Head Office {runId}` tampil pada daftar
19. Verifikasi tidak ada ASG yang memuat aset `Laptop Dell Latitude 5420 {runId}` pada daftar

### Draft tidak berubah sesudah Save Draft dan Submit ditolak
20. Klik tab `Drafts`
21. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
22. Klik `Edit` pada Draft yang memuat aset `Laptop Dell Latitude 5420 {runId}`
23. Verifikasi Purpose aset `Laptop Dell Latitude 5420 {runId}` tetap bernilai `Perangkat kerja tim lapangan`
24. Klik `[Cancel]` pada form yang belum diubah

### Delete Draft ditolak
25. Klik tab `Drafts`
26. Ketik Search `Monitor LG 24 {runId}`, tekan Enter
27. Klik `Delete` pada Draft yang memuat aset `Monitor LG 24 {runId}`
28. Klik `[Delete]` pada dialog `Delete Draft`
29. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
30. Verifikasi Draft yang memuat aset `Monitor LG 24 {runId}` masih tampil

### Cancel Assignment ditolak dan tidak tercatat di log
31. Klik tab `Transactions`
32. Ketik Search `Printer HP M404 {runId}`, tekan Enter
33. Buka menu ⋯ pada baris ASG yang memuat aset `Printer HP M404 {runId}`
34. Klik `Assignment Log`
35. Catat jumlah node pada Assignment Log aset `Printer HP M404 {runId}`
36. Tutup dialog Assignment Log
37. Buka menu ⋯ pada baris ASG yang memuat aset `Printer HP M404 {runId}`
38. Klik `Cancel Assignment`
39. Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
40. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
41. Verifikasi ASG yang memuat aset `Printer HP M404 {runId}` tetap berstatus `Waiting for Handover`
42. Buka menu ⋯ pada baris ASG yang memuat aset `Printer HP M404 {runId}`
43. Klik `Assignment Log`
44. Verifikasi jumlah node pada Assignment Log aset `Printer HP M404 {runId}` sama dengan jumlah sebelum aksi
45. Tutup dialog Assignment Log

### Change PIC ditolak
46. Ganti isi kotak Search dengan `Projector Epson EB-X49 {runId}`, tekan Enter
47. Buka menu ⋯ pada baris ASG yang memuat aset `Projector Epson EB-X49 {runId}`
48. Klik `Change PIC`
49. Pilih `Sari Dewi {runId}` pada dialog Select User
50. Klik `[Select]`
51. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
52. Verifikasi penanda `No PIC` tetap tampil pada ASG yang memuat aset `Projector Epson EB-X49 {runId}`

### Hand Over ditolak
53. Ganti isi kotak Search dengan `Router Cisco ISR {runId}`, tekan Enter
54. Buka menu ⋯ pada baris ASG yang memuat aset `Router Cisco ISR {runId}`
55. Klik `Hand Over`
56. Klik `[Complete Handover]`
57. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
58. Klik menu `Transactions > Assignment`
59. Ketik Search `Router Cisco ISR {runId}`, tekan Enter
60. Verifikasi ASG yang memuat aset `Router Cisco ISR {runId}` tetap berstatus `Waiting for Handover`

### Remind Assignee ditolak
61. Ganti isi kotak Search dengan `Printer HP M404 {runId}`, tekan Enter
62. Buka menu ⋯ pada baris ASG yang memuat aset `Printer HP M404 {runId}`
63. Klik `Remind Assignee`
64. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil

### Unassign ditolak
65. Ganti isi kotak Search dengan `Camera Sony A7 {runId}`, tekan Enter
66. Buka menu ⋯ pada baris ASG yang memuat aset `Camera Sony A7 {runId}`
67. Klik `Unassign`
68. Klik `[Submit]`
69. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
70. Klik menu `Transactions > Assignment`
71. Ketik Search `Camera Sony A7 {runId}`, tekan Enter
72. Verifikasi ASG yang memuat aset `Camera Sony A7 {runId}` tetap berstatus `Assigned`

### Approve ditolak
73. Klik menu `Approvals > Assignment`
74. Ketik Search `Sari Dewi {runId}`, tekan Enter
75. Klik `Review` pada pengajuan dengan Assignee `Sari Dewi {runId}`
76. Pilih `Approve` pada kolom `Approval` aset `Scanner Epson DS-530 {runId}`
77. Klik `[Submit]` pada halaman Review
78. Klik `[Submit]` pada dialog `Submit Approval`
79. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
80. Klik menu `Approvals > Assignment`
81. Ketik Search `Sari Dewi {runId}`, tekan Enter
82. Verifikasi pengajuan dengan Assignee `Sari Dewi {runId}` tetap tampil pada tab `Active`

### Bulk Delete Draft ditolak
83. Klik menu `Transactions > Assignment`
84. Klik tab `Drafts`
85. Ketik Search `Kursi Ergonomis {runId}`, tekan Enter
86. Centang baris Draft yang memuat aset `Kursi Ergonomis {runId}`
87. Ganti isi kotak Search dengan `Meja Kerja Staf {runId}`, tekan Enter
88. Centang baris Draft yang memuat aset `Meja Kerja Staf {runId}`
89. Klik `Bulk Action`
90. Klik `Delete` pada menu Bulk Action
91. Klik `[Delete]` pada dialog konfirmasi
92. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
93. Verifikasi Draft yang memuat aset `Meja Kerja Staf {runId}` masih tampil
94. Klik tab `Transactions`

### Status Expired memakai penolakan yang sama
95. Status entitas berubah menjadi `Expired`
96. Ganti isi kotak Search dengan `Printer HP M404 {runId}`, tekan Enter
97. Buka menu ⋯ pada baris ASG yang memuat aset `Printer HP M404 {runId}`
98. Klik `Cancel Assignment`
99. Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
100. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
101. Verifikasi ASG yang memuat aset `Printer HP M404 {runId}` tetap berstatus `Waiting for Handover`

### Status Grace memakai penolakan yang sama
102. Status entitas berubah menjadi `Grace`
103. Buka menu ⋯ pada baris ASG yang memuat aset `Printer HP M404 {runId}`
104. Klik `Remind Assignee`
105. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil

### Job sistem tetap berjalan pada entitas yang diblok
106. Job Transaction timeout berjalan untuk ASG yang memuat aset `Server Dell R740 {runId}`
107. Klik tab `History`
108. Ketik Search `Server Dell R740 {runId}`, tekan Enter
109. Verifikasi baris aset `Server Dell R740 {runId}` berstatus `Canceled` dengan alasan `Timed out (Waiting for Approval)`
110. Job jendela konfirmasi Handover berjalan untuk aset `Modem Huawei E5576 {runId}`: jendela `15 menit` habis tanpa konfirmasi
111. Klik tab `Transactions`
112. Ketik Search `Modem Huawei E5576 {runId}`, tekan Enter
113. Buka menu ⋯ pada baris ASG yang memuat aset `Modem Huawei E5576 {runId}`
114. Klik `Assignment Log`
115. Verifikasi node `Confirmation not received` tampil pada Assignment Log aset `Modem Huawei E5576 {runId}`
116. Tutup dialog Assignment Log
117. Verifikasi ASG yang memuat aset `Modem Huawei E5576 {runId}` tetap berstatus `Waiting for Handover`

### Aksi tulis dapat dicatat setelah entitas aktif kembali
118. Status entitas berubah menjadi aktif
119. Klik tab `Transactions`
120. Ketik Search `Printer HP M404 {runId}`, tekan Enter
121. Buka menu ⋯ pada baris ASG yang memuat aset `Printer HP M404 {runId}`
122. Klik `Cancel Assignment`
123. Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
124. Verifikasi toast `Success, assignment has been canceled.` tampil

### Unassign dapat dicatat setelah entitas aktif kembali
125. Ganti isi kotak Search dengan `Camera Sony A7 {runId}`, tekan Enter
126. Buka menu ⋯ pada baris ASG yang memuat aset `Camera Sony A7 {runId}`
127. Klik `Unassign`
128. Klik `[Submit]`
129. Verifikasi toast `Success, 1 asset has been unassigned.` tampil sebagai bukti aksi tulis berhasil dicatat setelah entitas aktif kembali

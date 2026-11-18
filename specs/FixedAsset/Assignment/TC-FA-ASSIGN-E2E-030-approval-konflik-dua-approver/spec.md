---
id: TC-FA-ASSIGN-E2E-030-approval-konflik-dua-approver
title: "Keputusan bersamaan dua approver dan pengajuan ditutup saat Review"
layer: ui-e2e
priority: Medium
caseType: Edge
status: ready-for-automation
sourceRules: ["D-ASG-16", "EC-ASG-11", "EC-ASG-81", "EC-ASG-52", "EC-ASG-68", "EC-ASG-69", "DO-ASG-11", "DO-ASG-12", "DO-ASG-13", "DO-ASG-14", "DO-ASG-15", "DO-ASG-16", "S-ASG-07", "ASSIGN-LOGIC-07m"]
smoke: []
dependsOn: []
trace:
  "D-ASG-16": [11, 12, 13, 15, 29, 118]
  "EC-ASG-11": [118, 125]
  "EC-ASG-81": [29, 32]
  "EC-ASG-52": [73, 75, 76, 78, 87]
  "EC-ASG-68": [53, 56, 57, 59]
  "EC-ASG-69": [94, 96, 97, 99]
  "DO-ASG-11": [11, 18]
  "DO-ASG-12": [29, 32]
  "DO-ASG-13": [41, 42]
  "DO-ASG-14": 18
  "DO-ASG-15": [15, 16, 17, 32]
  "DO-ASG-16": [53, 54, 59, 73, 94]
  "S-ASG-07": [109, 110]
  "ASSIGN-LOGIC-07m": 11
anchor: []
coverage:
  web: automated
---

# Keputusan bersamaan dua approver dan pengajuan ditutup saat Review

## Prerequisites
- Aktor: tiga aktor berjalan bersamaan di konteks terpisah; di langkah ditulis [Rina] untuk Approver `Rina Wulandari {runId}` (DU-030-1), [Tono] untuk Approver `Tono Wibowo {runId}` (DU-030-2), dan [Agus] untuk Asset Admin `Agus Pratama {runId}` (DU-030-3).
- Layar awal: Approvals > Assignment > Active untuk [Rina] dan [Tono]; Transactions > Assignment untuk [Agus].
- Data:
  - DU-030-1: User `Rina Wulandari {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`.
  - DU-030-2: User `Tono Wibowo {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`.
  - DU-030-3: User `Agus Pratama {runId}`, Role `Asset Admin`, Group penugasan `Head Office`, pengaju DU-030-4 sampai DU-030-11.
  - DU-030-4: Pengajuan 1, Group `Head Office`, Assignee `Sari Dewi {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 2 hari, pukul 09:00`, Approval type `Any one approver`; aset `Toyota Avanza {runId}` dengan approver `Rina Wulandari {runId}` dan `Tono Wibowo {runId}`; aset `Excavator PC200 {runId}` dengan approver hanya `Rina Wulandari {runId}`; belum diputuskan.
  - DU-030-5: Pengajuan 2, Group `Head Office`, Assignee `Hana Putri {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 3 hari, pukul 09:00`, Approval type `All approvers`; aset `Projector Epson EB-X49 {runId}` dengan approver `Rina Wulandari {runId}` dan `Tono Wibowo {runId}`; belum diputuskan.
  - DU-030-6: Pengajuan 3, Group `Head Office`, Assignee `Dewi Lestari {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 4 hari, pukul 09:00`, Approval type `All approvers`; aset `Kamera Sony A7 {runId}` dengan approver `Rina Wulandari {runId}` dan `Tono Wibowo {runId}`; belum diputuskan.
  - DU-030-7: Pengajuan 4, Group `Head Office`, Assignee `Joko Susilo {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 5 hari, pukul 09:00`, Approval type `Any one approver`; aset `Genset Cummins C100 {runId}` dengan approver `Rina Wulandari {runId}` dan `Tono Wibowo {runId}`; belum diputuskan.
  - DU-030-8: Pengajuan 5, Group `Head Office`, Assignee `Lina Marlina {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 6 hari, pukul 09:00`, Approval type `Any one approver`; aset `Forklift Toyota 8FD {runId}` dengan approver `Rina Wulandari {runId}` dan `Tono Wibowo {runId}`; belum diputuskan, belum ada baris Assigned; Draft hasil Cancel baris itu (DU-030-17) berisi `Forklift Toyota 8FD {runId}`.
  - DU-030-9: Pengajuan 6, Group `Head Office`, Assignee `Nina Safitri {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 7 hari, pukul 09:00`, Approval type `Any one approver`; aset `Tablet Samsung Tab S8 {runId}` dengan approver `Rina Wulandari {runId}` dan `Tono Wibowo {runId}`; belum diputuskan.
  - DU-030-10: Pengajuan 7, Group `Head Office`, Assignee `Budi Santoso {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 8 hari, pukul 09:00`, Approval type `Any one approver`; aset `Printer HP M404 {runId}` dengan approver `Rina Wulandari {runId}` dan `Tono Wibowo {runId}`; belum diputuskan.
  - DU-030-11: Pengajuan 8, Group `Head Office`, Assignee `Mira Anjani {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 9 hari, pukul 09:00`, Approval type `Any one approver`; aset `Monitor Dell P2422H {runId}` dengan approver `Rina Wulandari {runId}` dan `Tono Wibowo {runId}`; belum diputuskan.
  - DU-030-12: Approval Note `Site work postponed`, diisi [Rina] pada `Excavator PC200 {runId}`.
  - DU-030-13: Approval Note `Aset dipakai proyek lain`, diisi [Tono] pada `Projector Epson EB-X49 {runId}`.
  - DU-030-14: Approval Note `Genset dialihkan ke proyek lain`, diisi [Rina] pada `Genset Cummins C100 {runId}` dan tidak dikirim.
  - DU-030-15: Approval Note `Forklift dikembalikan ke gudang`, diisi [Rina] pada `Forklift Toyota 8FD {runId}` dan tidak dikirim.
  - DU-030-16: Approval Note `Tablet dialihkan ke cabang lain`, diisi [Rina] pada `Tablet Samsung Tab S8 {runId}` dan tidak dikirim.
  - DU-030-17: Draft untuk Assignee `Lina Marlina {runId}`, Group `Head Office`, berisi `Forklift Toyota 8FD {runId}`, terbentuk dari Cancel per baris DU-030-8 dengan `Save as Draft to edit`.
  - Riwayat keputusan [Rina] kosong sampai blok terakhir: [Rina] tidak pernah mengirim keputusan sebelum blok keputusan bersamaan.

## Test Steps

### Any one: keputusan approver lain lebih dulu membuka dialog tanpa menunggu Submit
1. [Rina] Buka halaman `Approvals > Assignment`
2. [Rina] Ketik Search `Sari Dewi {runId}`, tekan Enter
3. [Rina] Klik `Transaction ID` pada baris `Sari Dewi {runId}`
4. [Rina] Ubah toggle `Approval` pada baris `Excavator PC200 {runId}` menjadi `Reject`
5. [Rina] Isi `Approval Note` pada baris `Excavator PC200 {runId}` dengan `Site work postponed`
6. [Tono] Buka halaman `Approvals > Assignment`
7. [Tono] Ketik Search `Sari Dewi {runId}`, tekan Enter
8. [Tono] Klik `Transaction ID` pada baris `Sari Dewi {runId}`
9. [Tono] Klik `[Submit]` pada halaman Review
10. [Tono] Klik `[Submit]` pada dialog `Submit Approval`
11. Verifikasi dialog `Approval cannot be made` terbuka pada halaman Review milik [Rina] tanpa [Rina] menekan `[Submit]`
12. Verifikasi dialog `Approval cannot be made` pada halaman Review milik [Rina] memuat teks `You can no longer approve this request because it has already been done by another approver.`
13. Verifikasi dialog `Approval cannot be made` pada halaman Review milik [Rina] memiliki tombol `[Close]`

### Sesudah Close, aset yang diputuskan pihak lain read-only dan keputusan yang belum dikirim tidak tersimpan
14. [Rina] Klik `[Close]` pada dialog
15. Verifikasi dialog `Approval cannot be made` pada halaman Review milik [Rina] tertutup dan halaman Review dimuat ulang oleh `[Close]` tanpa [Rina] memuat ulang secara manual
16. Verifikasi aset `Toyota Avanza {runId}` pada halaman Review milik [Rina] read-only dengan hasil `Approved`
17. Verifikasi `Approval` pada baris `Excavator PC200 {runId}` masih `Reject` dan `Approval Note` masih berisi `Site work postponed` untuk dikirim ulang
18. Verifikasi `Approval Rule` pada baris `Excavator PC200 {runId}` belum bernilai `Approved` maupun `Rejected` karena keputusan [Rina] yang belum dikirim tidak tersimpan

### All: satu penolakan langsung menolak aset dan membuka dialog bagi approver lain
19. [Rina] Buka halaman `Approvals > Assignment`
20. [Rina] Ketik Search `Hana Putri {runId}`, tekan Enter
21. [Rina] Klik `Transaction ID` pada baris `Hana Putri {runId}`
22. [Tono] Buka halaman `Approvals > Assignment`
23. [Tono] Ketik Search `Hana Putri {runId}`, tekan Enter
24. [Tono] Klik `Transaction ID` pada baris `Hana Putri {runId}`
25. [Tono] Ubah toggle `Approval` pada baris `Projector Epson EB-X49 {runId}` menjadi `Reject`
26. [Tono] Isi `Approval Note` pada baris `Projector Epson EB-X49 {runId}` dengan `Aset dipakai proyek lain`
27. [Tono] Klik `[Submit]` pada halaman Review
28. [Tono] Klik `[Submit]` pada dialog `Submit Approval`
29. Verifikasi dialog `Approval cannot be made` terbuka pada halaman Review milik [Rina] karena [Tono] me-Reject aset `Projector Epson EB-X49 {runId}`, padahal [Rina] belum menekan `[Submit]`
30. [Rina] Klik `[Close]` pada dialog
31. [Rina] Muat ulang halaman Review
32. Verifikasi aset `Projector Epson EB-X49 {runId}` pada halaman Review milik [Rina] read-only dengan hasil `Rejected`

### All: persetujuan satu approver tidak membuka dialog bagi approver lain
33. [Rina] Buka halaman `Approvals > Assignment`
34. [Rina] Ketik Search `Dewi Lestari {runId}`, tekan Enter
35. [Rina] Klik `Transaction ID` pada baris `Dewi Lestari {runId}`
36. [Tono] Buka halaman `Approvals > Assignment`
37. [Tono] Ketik Search `Dewi Lestari {runId}`, tekan Enter
38. [Tono] Klik `Transaction ID` pada baris `Dewi Lestari {runId}`
39. [Tono] Klik `[Submit]` pada halaman Review
40. [Tono] Klik `[Submit]` pada dialog `Submit Approval`
41. Verifikasi toggle `Approval` pada baris `Kamera Sony A7 {runId}` di halaman Review milik [Rina] masih dapat diubah dan bernilai `Approve`
42. Verifikasi dialog `Approval cannot be made` tidak tampil di halaman Review milik [Rina] dalam 5 detik sesudah [Tono] menyetujui aset `Kamera Sony A7 {runId}`

### Pengajuan dibatalkan pengaju saat Review terbuka membuka dialog Assignment Canceled
43. [Rina] Buka halaman `Approvals > Assignment`
44. [Rina] Ketik Search `Joko Susilo {runId}`, tekan Enter
45. [Rina] Klik `Transaction ID` pada baris `Joko Susilo {runId}`
46. [Rina] Ubah toggle `Approval` pada baris `Genset Cummins C100 {runId}` menjadi `Reject`
47. [Rina] Isi `Approval Note` pada baris `Genset Cummins C100 {runId}` dengan `Genset dialihkan ke proyek lain`
48. [Agus] Buka halaman `Transactions > Assignment`
49. [Agus] Ketik Search `Joko Susilo {runId}`, tekan Enter
50. [Agus] Klik `⋯` pada baris `Joko Susilo {runId}`
51. [Agus] Klik `Cancel Assignment`
52. [Agus] Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
53. Verifikasi dialog `Assignment Canceled` terbuka pada halaman Review milik [Rina] dengan teks `This assignment was canceled by [Name].` dengan Name `Agus Pratama {runId}`
54. Verifikasi dialog `Assignment Canceled` pada halaman Review milik [Rina] memiliki tombol `[Back to Approvals]`
55. [Rina] Klik `[Back to Approvals]`
56. Verifikasi baris `Mira Anjani {runId}` tampil di tab `Active` milik [Rina] sesudah kembali ke Approvals
57. Verifikasi tidak ada baris dengan Assignee `Joko Susilo {runId}` di tab `Active` milik [Rina] karena pengajuan dibatalkan dan keputusan dibuang
58. [Rina] Klik tab `History`
59. Verifikasi empty state `No history yet` tampil di tab `History` milik [Rina] karena keputusan `Reject` atas `Genset Cummins C100 {runId}` yang belum dikirim dibuang dan tidak tercatat

### Cancel per baris dengan Save as Draft to edit saat Review terbuka membuang keputusan dan Draft baru tidak masuk antrean
60. [Rina] Buka halaman `Approvals > Assignment`
61. [Rina] Ketik Search `Lina Marlina {runId}`, tekan Enter
62. [Rina] Klik `Transaction ID` pada baris `Lina Marlina {runId}`
63. [Rina] Ubah toggle `Approval` pada baris `Forklift Toyota 8FD {runId}` menjadi `Reject`
64. [Rina] Isi `Approval Note` pada baris `Forklift Toyota 8FD {runId}` dengan `Forklift dikembalikan ke gudang`
65. [Agus] Buka halaman `Transactions > Assignment`
66. [Agus] Ketik Search `Lina Marlina {runId}`, tekan Enter
67. [Agus] Klik `⋯` pada baris `Lina Marlina {runId}`
68. [Agus] Klik `Detail`
69. [Agus] Klik `⋯` pada baris `Forklift Toyota 8FD {runId}`
70. [Agus] Klik `Cancel Assignment`
71. [Agus] Centang `Save as Draft to edit` pada dialog `Cancel Assignment`
72. [Agus] Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
73. Verifikasi dialog `Assignment Canceled` terbuka pada halaman Review milik [Rina] dengan teks `This assignment was canceled by [Name].` dengan Name `Agus Pratama {runId}`
74. [Rina] Klik `[Back to Approvals]`
75. Verifikasi baris `Mira Anjani {runId}` tampil di tab `Active` milik [Rina]
76. Verifikasi tidak ada baris dengan Assignee `Lina Marlina {runId}` di tab `Active` milik [Rina] karena Draft baru tidak masuk antrean sampai di-Submit ulang
77. [Rina] Klik tab `History`
78. Verifikasi empty state `No history yet` tampil di tab `History` milik [Rina] karena keputusan `Reject` atas `Forklift Toyota 8FD {runId}` yang belum dikirim dibuang dan tidak tercatat
79. [Agus] Buka halaman `Transactions > Assignment`
80. [Agus] Klik tab `Drafts`
81. [Agus] Ketik Search `Lina Marlina {runId}`, tekan Enter
82. [Agus] Klik Assignee `Lina Marlina {runId}` pada baris Draft
83. [Agus] Klik `[Submit]`
84. [Agus] Klik `[Submit]` pada dialog `Submit Assignment`
85. [Rina] Buka halaman `Approvals > Assignment`
86. [Rina] Ketik Search `Lina Marlina {runId}`, tekan Enter
87. Verifikasi baris `Lina Marlina {runId}` tampil di tab `Active` milik [Rina] sesudah Draft di-Submit ulang

### Pengajuan ditutup sistem karena batas waktu approval saat Review terbuka
88. [Rina] Buka halaman `Approvals > Assignment`
89. [Rina] Ketik Search `Nina Safitri {runId}`, tekan Enter
90. [Rina] Klik `Transaction ID` pada baris `Nina Safitri {runId}`
91. [Rina] Ubah toggle `Approval` pada baris `Tablet Samsung Tab S8 {runId}` menjadi `Reject`
92. [Rina] Isi `Approval Note` pada baris `Tablet Samsung Tab S8 {runId}` dengan `Tablet dialihkan ke cabang lain`
93. Batas waktu approval (Transaction timeout) pengajuan DU-030-9 terlewati dan pengajuan ditutup sistem
94. Verifikasi dialog `Assignment Canceled` terbuka pada halaman Review milik [Rina] dengan teks `This assignment was canceled automatically ([Reason]).` dengan Reason `Timed out (Waiting for Approval)`
95. [Rina] Klik `[Back to Approvals]`
96. Verifikasi baris `Mira Anjani {runId}` tampil di tab `Active` milik [Rina] sesudah pengajuan ditutup sistem
97. Verifikasi tidak ada baris dengan Assignee `Nina Safitri {runId}` di tab `Active` milik [Rina] karena keputusan dibuang
98. [Rina] Klik tab `History`
99. Verifikasi empty state `No history yet` tampil di tab `History` milik [Rina] karena keputusan `Reject` atas `Tablet Samsung Tab S8 {runId}` yang belum dikirim dibuang dan tidak tercatat

### Pengajuan yang sudah ditutup saat Review terbuka membuat tombol keputusan Review disabled
100. [Rina] Buka halaman `Approvals > Assignment`
101. [Rina] Ketik Search `Budi Santoso {runId}`, tekan Enter
102. [Rina] Klik `Transaction ID` pada baris `Budi Santoso {runId}`
103. [Tono] Buka halaman `Approvals > Assignment`
104. [Tono] Ketik Search `Budi Santoso {runId}`, tekan Enter
105. [Tono] Klik `Transaction ID` pada baris `Budi Santoso {runId}`
106. [Tono] Klik `[Submit]` pada halaman Review
107. [Tono] Klik `[Submit]` pada dialog `Submit Approval`
108. [Rina] Klik `[Close]` pada dialog `Approval cannot be made`
109. Verifikasi `[Submit]` pada halaman Review milik [Rina] pengajuan `Budi Santoso {runId}` tidak tampil
110. Verifikasi halaman Review milik [Rina] pengajuan `Budi Santoso {runId}` read-only tanpa tombol keputusan

### Dua approver mengirim keputusan atas aset Any one yang sama bersamaan
111. [Rina] Buka halaman `Approvals > Assignment`
112. [Rina] Ketik Search `Mira Anjani {runId}`, tekan Enter
113. [Rina] Klik `Transaction ID` pada baris `Mira Anjani {runId}`
114. [Tono] Buka halaman `Approvals > Assignment`
115. [Tono] Ketik Search `Mira Anjani {runId}`, tekan Enter
116. [Tono] Klik `Transaction ID` pada baris `Mira Anjani {runId}`
117. [Rina] dan [Tono] mengonfirmasi `[Submit]` pada dialog `Submit Approval` secara bersamaan
118. Verifikasi tepat satu dari halaman Review milik [Rina] dan halaman Review milik [Tono] menampilkan dialog `Approval cannot be made`
119. [Rina] Buka halaman `Approvals > Assignment`
120. [Rina] Klik tab `History`
121. [Tono] Buka halaman `Approvals > Assignment`
122. [Tono] Klik tab `History`
123. [Rina] Ganti isi kotak search dengan `Mira Anjani {runId}`, tekan Enter
124. [Tono] Ganti isi kotak search dengan `Mira Anjani {runId}`, tekan Enter
125. Verifikasi baris `Mira Anjani {runId}` tampil di tab `History` tepat pada salah satu dari [Rina] dan [Tono], yaitu approver yang keputusannya lebih dulu diterima server

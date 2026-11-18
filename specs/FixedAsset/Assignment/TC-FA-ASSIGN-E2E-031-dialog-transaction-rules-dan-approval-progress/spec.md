---
id: TC-FA-ASSIGN-E2E-031-dialog-transaction-rules-dan-approval-progress
title: "Dialog Transaction Rules dan Approval Progress per aset"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["D-ASG-10", "D-ASG-28", "§4.1#r17", "FI-ASG-89", "FI-ASG-90", "FI-ASG-91", "FI-ASG-92", "FI-ASG-93", "FI-ASG-94", "FI-ASG-95", "FI-ASG-96", "FI-ASG-97", "FI-ASG-98", "FI-ASG-99", "FI-ASG-100", "FI-ASG-101", "FI-ASG-102", "FI-ASG-103", "FI-ASG-104", "FI-ASG-105", "FI-ASG-106", "FI-ASG-107", "FI-ASG-108", "FI-ASG-109", "FI-ASG-110", "EC-ASG-80", "EC-ASG-83", "§4.4#r15"]
smoke: []
dependsOn: []
trace:
  "D-ASG-10": [8, 9, 10, 11, 94]
  "D-ASG-28": [109, 111, 112, 113]
  "§4.1#r17": 109
  "FI-ASG-89": [12, 17, 19, 25]
  "FI-ASG-90": [18, 25]
  "FI-ASG-91": [17, 19, 25, 26]
  "FI-ASG-92": 12
  "FI-ASG-93": [31, 32]
  "FI-ASG-94": [37, 38]
  "FI-ASG-95": [43, 51, 126, 134, 142]
  "FI-ASG-96": 44
  "FI-ASG-97": [45, 52]
  "FI-ASG-98": [99, 110]
  "FI-ASG-99": 101
  "FI-ASG-100": 102
  "FI-ASG-101": [46, 52, 103, 125, 126]
  "FI-ASG-102": 100
  "FI-ASG-103": 113
  "FI-ASG-104": [20, 112]
  "FI-ASG-105": [57, 63]
  "FI-ASG-106": 58
  "FI-ASG-107": [68, 73]
  "FI-ASG-108": [78, 79, 83]
  "FI-ASG-109": [88, 89]
  "FI-ASG-110": 118
  "EC-ASG-80": [109, 111, 112]
  "EC-ASG-83": [17, 19, 25, 26]
  "§4.4#r15": 8
anchor: []
coverage:
  web: automated
---

# Dialog Transaction Rules dan Approval Progress per aset

## Prerequisites
- Aktor: Total Control `Dewi Anggraini {runId}` (DU-031-1), yang juga approver aset `Mobil Toyota Hilux {runId}` di DU-031-25.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-031-1: User `Dewi Anggraini {runId}`, Role `Total Control`.
  - DU-031-2: User `Wawan Hartono {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`.
  - DU-031-3: User `Xena Pramesti {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`.
  - DU-031-4: User `Yuni Astuti {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`.
  - DU-031-5: User `Agus Pratama {runId}`, Role `Asset Admin`, Group penugasan `Head Office`, pengaju DU-031-9, DU-031-25, DU-031-34, dan DU-031-35.
  - DU-031-6: User `Hendra Kusuma {runId}`, Role `Group Manager`, Group penugasan `Head Office`.
  - DU-031-7: User `Gita Permata {runId}`, Role `Total Control`.
  - DU-031-8: User `Zaki Ramadhan {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`, Status `Inactive` sesudah Submit.
  - DU-031-9: ASG, Group `Head Office`, Assignee `Sari Dewi {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 5 hari, pukul 09:00`, berisi lima belas baris DU-031-10 sampai DU-031-24. `Wawan Hartono {runId}` memutuskan seluruh asetnya di ASG ini sekaligus lewat satu Submit pada `T0 − 1 hari, pukul 09:30`; `Xena Pramesti {runId}` memutuskan seluruh asetnya di ASG ini sekaligus pada `T0 − 1 hari, pukul 10:15`; approver lain di ASG ini tidak memutuskan apa pun.
  - DU-031-10: Baris `Toyota Avanza {runId}`, Approval type `Any one approver`, approver `Yuni Astuti {runId}`, `Bambang Hartono {runId}`, `Citra Lestari {runId}`, belum ada keputusan.
  - DU-031-11: Baris `Excavator PC200 {runId}`, Approval type `Any one approver`, approver `Wawan Hartono {runId}`, `Xena Pramesti {runId}`, `Yuni Astuti {runId}`; `Wawan Hartono {runId}` menyetujui pada `T0 − 1 hari, pukul 09:30` dengan Approval Note `Site work postponed`.
  - DU-031-12: Baris `Genset Cummins C100 {runId}`, Approval type `Any one approver`, approver `Xena Pramesti {runId}`, `Yuni Astuti {runId}`; `Xena Pramesti {runId}` menolak pada `T0 − 1 hari, pukul 10:15`.
  - DU-031-13: Baris `Forklift Toyota 8FD {runId}`, Approval type `All approvers`, approver `Wawan Hartono {runId}`, `Yuni Astuti {runId}`; `Wawan Hartono {runId}` menyetujui pada `T0 − 1 hari, pukul 09:30`, `Yuni Astuti {runId}` belum bertindak.
  - DU-031-14: Baris `Projector Epson EB-X49 {runId}`, Approval type `All approvers`, approver `Wawan Hartono {runId}`, `Xena Pramesti {runId}`; `Wawan Hartono {runId}` menolak pada `T0 − 1 hari, pukul 09:30`.
  - DU-031-15: Baris `Kamera Sony A7 {runId}`, Approval type `All approvers`, approver `Wawan Hartono {runId}`, `Citra Lestari {runId}`; `Wawan Hartono {runId}` menyetujui pada `T0 − 1 hari, pukul 09:30`, lalu `Agus Pratama {runId}` membatalkan pada `T0 − 1 hari, pukul 13:00` sebelum `Citra Lestari {runId}` bertindak.
  - DU-031-16: Baris `Tablet Samsung Tab S8 {runId}`, Approval type `Any one approver`, approver `Dimas Pratama {runId}`, `Eko Saputra {runId}`; ditutup sistem karena approval timeout pada `T0 − 1 hari, pukul 14:00`.
  - DU-031-17: Baris `Printer HP M404 {runId}`, Approval type `Any one approver`, approver `Bambang Hartono {runId}`, `Citra Lestari {runId}`; `Hendra Kusuma {runId}` menyetujui lewat Group Manager override pada `T0 − 1 hari, pukul 15:00`.
  - DU-031-18: Baris `Scanner Canon LiDE {runId}`, Approval type `Any one approver`, approver `Bambang Hartono {runId}`, `Citra Lestari {runId}`; `Gita Permata {runId}` menolak lewat Total Control override pada `T0 − 1 hari, pukul 15:30`.
  - DU-031-19: Baris `Monitor Dell P2422H {runId}`, daftar approver snapshot kosong sejak Submit, dirutekan ke Group Manager `Hendra Kusuma {runId}`.
  - DU-031-20: Baris `Laptop Lenovo ThinkPad T14 {runId}`, daftar approver snapshot kosong sejak Submit, dirutekan ke Total Control `Gita Permata {runId}`.
  - DU-031-21: Baris `Genset Perkins P20 {runId}`, Approval type `Any one approver`, approver `Zaki Ramadhan {runId}` yang dinonaktifkan sesudah Submit, dirutekan ulang ke Group Manager `Hendra Kusuma {runId}`.
  - DU-031-22: Baris `Server Dell R740 {runId}`, Approval type `Any one approver`, tujuh approver `Yuni Astuti {runId}`, `Bambang Hartono {runId}`, `Citra Lestari {runId}`, `Dimas Pratama {runId}`, `Eko Saputra {runId}`, `Fajar Nugroho {runId}`, `Gilang Permana {runId}`, belum ada keputusan.
  - DU-031-23: Baris `Laptop Dell Latitude 5420 {runId}`, Require approval OFF, Approval `Not required`.
  - DU-031-24: Baris `Mesin Bor Bosch GBH {runId}` dengan tiga putaran: putaran pertama `Not required`, putaran kedua `Any one approver` dengan approver `Wawan Hartono {runId}` dan `Yuni Astuti {runId}` ditolak `Wawan Hartono {runId}`, putaran ketiga `Any one approver` dengan approver `Wawan Hartono {runId}` dan `Xena Pramesti {runId}` belum diputuskan.
  - DU-031-25: Pengajuan, Group `Head Office`, Assignee `Hana Putri {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 2 hari, pukul 09:00`; aset `Mobil Toyota Hilux {runId}` dengan approver `Dewi Anggraini {runId}`, belum diputuskan; aset `Mesin Las Lincoln {runId}` Approval type `All approvers` dengan approver `Wawan Hartono {runId}` dan `Xena Pramesti {runId}`, `Wawan Hartono {runId}` menyetujui pada `T0 − 1 hari, pukul 10:00` dengan Approval Note `Site work postponed`.
  - DU-031-26: Draft, Assignee `Budi Santoso {runId}`, Group `Head Office`, aset `Printer Epson L3250 {runId}`, belum punya snapshot.
  - DU-031-27: User `Bambang Hartono {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`.
  - DU-031-28: User `Citra Lestari {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`.
  - DU-031-29: User `Dimas Pratama {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`.
  - DU-031-30: User `Eko Saputra {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`.
  - DU-031-31: User `Fajar Nugroho {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`.
  - DU-031-32: User `Gilang Permana {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office`.
  - DU-031-33: User `Rudi Hartono {runId}`, karyawan, Assignee DU-031-34, dinonaktifkan sesudah Submit.
  - DU-031-34: ASG, Group `Head Office`, Assignee `Rudi Hartono {runId}` (DU-031-33), Requested By `Agus Pratama {runId}`, Request Date `T0 − 4 hari, pukul 09:00`; baris `Router Cisco ISR4331 {runId}`, Approval type `Any one approver`, approver `Wawan Hartono {runId}`, `Xena Pramesti {runId}`, belum ada keputusan, ditutup sistem dengan alasan `Assignee deactivated` pada `T0 − 1 hari, pukul 16:00`.
  - DU-031-35: ASG, Group `Head Office`, Assignee `Tari Utami {runId}`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 4 hari, pukul 10:00`; baris `Switch Cisco C9200 {runId}`, Approval type `Any one approver`, approver `Wawan Hartono {runId}`, `Xena Pramesti {runId}`, belum ada keputusan, ditutup sistem dengan alasan `Asset reported missing` pada `T0 − 1 hari, pukul 16:30`; baris `Firewall Fortinet 60F {runId}`, Approval type `Any one approver`, approver `Wawan Hartono {runId}`, `Xena Pramesti {runId}`, belum ada keputusan, ditutup sistem dengan alasan `Approval Workflow removed` pada `T0 − 1 hari, pukul 17:00`.

## Test Steps

### Baris Any one tanpa keputusan: semua approver Waiting for Approval
1. Buka halaman `Transactions > Assignment`
2. Ketik Search `Sari Dewi {runId}`, tekan Enter
3. Klik `⋯` pada baris `Sari Dewi {runId}`
4. Klik `Detail`
5. Ketik Search `Toyota Avanza {runId}`, tekan Enter
6. Klik `⋯` pada baris `Toyota Avanza {runId}`
7. Klik `Transaction Rules`
8. Verifikasi dialog `Transaction Rules` memuat nama aset `Toyota Avanza {runId}`
9. Verifikasi dialog `Transaction Rules` memuat batas efektif `Allowed assignee`, `Need recipient confirmation`, `Photo at start`, dan `Photo at end`
10. Verifikasi `Approval` pada dialog `Transaction Rules` bernilai `Needs approval`
11. Verifikasi `Approval type` pada dialog `Transaction Rules` bernilai `Any one approver`
12. Verifikasi approver `Yuni Astuti {runId}`, `Bambang Hartono {runId}`, dan `Citra Lestari {runId}` berstatus `Waiting for Approval`
13. Klik ikon silang pada dialog `Transaction Rules`

### Baris Any one yang disetujui satu approver
14. Ganti isi kotak search dengan `Excavator PC200 {runId}`, tekan Enter
15. Klik `⋯` pada baris `Excavator PC200 {runId}`
16. Klik `Transaction Rules`
17. Verifikasi approver `Wawan Hartono {runId}` berstatus `Approved`
18. Verifikasi approver `Wawan Hartono {runId}` berstatus `Approved` disertai waktu keputusan
19. Verifikasi approver `Xena Pramesti {runId}` dan `Yuni Astuti {runId}` berstatus `Not Involved`
20. Verifikasi Approval Note `Site work postponed` milik `Wawan Hartono {runId}` tidak ditampilkan pada dialog `Transaction Rules`
21. Klik ikon silang pada dialog `Transaction Rules`

### Baris Any one yang ditolak satu approver
22. Ganti isi kotak search dengan `Genset Cummins C100 {runId}`, tekan Enter
23. Klik `⋯` pada baris `Genset Cummins C100 {runId}`
24. Klik `Transaction Rules`
25. Verifikasi approver `Xena Pramesti {runId}` berstatus `Rejected` disertai waktu keputusan
26. Verifikasi approver `Yuni Astuti {runId}` berstatus `Not Involved`
27. Klik ikon silang pada dialog `Transaction Rules`

### Baris All approvers: tiap approver punya status sendiri
28. Ganti isi kotak search dengan `Forklift Toyota 8FD {runId}`, tekan Enter
29. Klik `⋯` pada baris `Forklift Toyota 8FD {runId}`
30. Klik `Transaction Rules`
31. Verifikasi approver `Wawan Hartono {runId}` berstatus `Approved` dan approver `Yuni Astuti {runId}` berstatus `Waiting for Approval`
32. Verifikasi `Approval type` pada dialog `Transaction Rules` bernilai `All approvers (AND)`
33. Klik ikon silang pada dialog `Transaction Rules`

### Baris All approvers: satu penolakan membuat approver lain Not Involved
34. Ganti isi kotak search dengan `Projector Epson EB-X49 {runId}`, tekan Enter
35. Klik `⋯` pada baris `Projector Epson EB-X49 {runId}`
36. Klik `Transaction Rules`
37. Verifikasi approver `Wawan Hartono {runId}` berstatus `Rejected`
38. Verifikasi approver `Xena Pramesti {runId}` yang belum bertindak berstatus `Not Involved`
39. Klik ikon silang pada dialog `Transaction Rules`

### Baris dibatalkan pengaju sebelum semua approver bertindak
40. Ganti isi kotak search dengan `Kamera Sony A7 {runId}`, tekan Enter
41. Klik `⋯` pada baris `Kamera Sony A7 {runId}`
42. Klik `Transaction Rules`
43. Verifikasi approver `Citra Lestari {runId}` yang belum bertindak berstatus `Not Involved`
44. Verifikasi approver `Wawan Hartono {runId}` tetap berstatus `Approved` dengan waktu keputusannya
45. Verifikasi dialog memuat keterangan `Canceled by [Name]` dengan Name `Agus Pratama {runId}` beserta waktunya
46. Verifikasi putaran yang dibatalkan tetap tampil sebagai blok pada dialog `Transaction Rules`
47. Klik ikon silang pada dialog `Transaction Rules`

### Baris ditutup sistem karena timeout approval
48. Ganti isi kotak search dengan `Tablet Samsung Tab S8 {runId}`, tekan Enter
49. Klik `⋯` pada baris `Tablet Samsung Tab S8 {runId}`
50. Klik `Transaction Rules`
51. Verifikasi approver `Dimas Pratama {runId}` dan `Eko Saputra {runId}` yang belum bertindak berstatus `Not Involved`
52. Verifikasi dialog memuat keterangan `Canceled by system (approval timeout` beserta waktunya
53. Klik ikon silang pada dialog `Transaction Rules`

### Baris diputuskan Group Manager lewat override
54. Ganti isi kotak search dengan `Printer HP M404 {runId}`, tekan Enter
55. Klik `⋯` pada baris `Printer HP M404 {runId}`
56. Klik `Transaction Rules`
57. Verifikasi baris tambahan `Hendra Kusuma {runId}` berstatus `Approved` dengan keterangan `Group Manager override`
58. Verifikasi approver snapshot `Bambang Hartono {runId}` dan `Citra Lestari {runId}` yang belum bertindak berstatus `Not Involved`
59. Klik ikon silang pada dialog `Transaction Rules`

### Baris diputuskan Total Control lewat override
60. Ganti isi kotak search dengan `Scanner Canon LiDE {runId}`, tekan Enter
61. Klik `⋯` pada baris `Scanner Canon LiDE {runId}`
62. Klik `Transaction Rules`
63. Verifikasi baris tambahan `Gita Permata {runId}` berstatus `Rejected` dengan keterangan `Total Control override`
64. Klik ikon silang pada dialog `Transaction Rules`

### Baris dengan daftar approver kosong sejak Submit dirutekan ke Group Manager
65. Ganti isi kotak search dengan `Monitor Dell P2422H {runId}`, tekan Enter
66. Klik `⋯` pada baris `Monitor Dell P2422H {runId}`
67. Klik `Transaction Rules`
68. Verifikasi penerima `Hendra Kusuma {runId}` tampil dengan keterangan `Routed to Group Manager`
69. Klik ikon silang pada dialog `Transaction Rules`

### Baris dengan daftar approver kosong sejak Submit dirutekan ke Total Control
70. Ganti isi kotak search dengan `Laptop Lenovo ThinkPad T14 {runId}`, tekan Enter
71. Klik `⋯` pada baris `Laptop Lenovo ThinkPad T14 {runId}`
72. Klik `Transaction Rules`
73. Verifikasi penerima `Gita Permata {runId}` tampil dengan keterangan `Routed to Total Control`
74. Klik ikon silang pada dialog `Transaction Rules`

### Reroute sesudah Submit hanya tercatat di Assignment Log
75. Ganti isi kotak search dengan `Genset Perkins P20 {runId}`, tekan Enter
76. Klik `⋯` pada baris `Genset Perkins P20 {runId}`
77. Klik `Transaction Rules`
78. Verifikasi approver `Zaki Ramadhan {runId}` tampil pada dialog `Transaction Rules`
79. Verifikasi dialog `Transaction Rules` tidak memuat keterangan `Routed to Group Manager`
80. Klik ikon silang pada dialog `Transaction Rules`
81. Klik `⋯` pada baris `Genset Perkins P20 {runId}`
82. Klik `Assignment Log`
83. Verifikasi dialog `Assignment Log` memuat node `Approval rerouted`
84. Klik ikon silang pada dialog `Assignment Log`

### Daftar approver banyak tampil tanpa dipotong dan dapat di-scroll
85. Ganti isi kotak search dengan `Server Dell R740 {runId}`, tekan Enter
86. Klik `⋯` pada baris `Server Dell R740 {runId}`
87. Klik `Transaction Rules`
88. Verifikasi dialog `Transaction Rules` memuat ketujuh approver `Yuni Astuti {runId}`, `Bambang Hartono {runId}`, `Citra Lestari {runId}`, `Dimas Pratama {runId}`, `Eko Saputra {runId}`, `Fajar Nugroho {runId}`, dan `Gilang Permana {runId}` tanpa dipotong
89. Verifikasi daftar approver dapat di-scroll dengan tinggi area maksimal 5 baris
90. Klik ikon silang pada dialog `Transaction Rules`

### Baris tanpa approval
91. Ganti isi kotak search dengan `Laptop Dell Latitude 5420 {runId}`, tekan Enter
92. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
93. Klik `Transaction Rules`
94. Verifikasi `Approval` pada dialog `Transaction Rules` bernilai `Not required`
95. Klik ikon silang pada dialog `Transaction Rules`

### Blok per putaran memakai snapshot masing-masing putaran
96. Ganti isi kotak search dengan `Mesin Bor Bosch GBH {runId}`, tekan Enter
97. Klik `⋯` pada baris `Mesin Bor Bosch GBH {runId}`
98. Klik `Transaction Rules`
99. Verifikasi bagian `Approval Progress` memuat tiga blok putaran dengan blok terbaru di atas
100. Verifikasi blok terbaru terbuka dan dua blok lain terlipat
101. Verifikasi blok putaran ketiga memuat approver `Wawan Hartono {runId}` dan `Xena Pramesti {runId}` dan blok putaran kedua memuat approver `Wawan Hartono {runId}` dan `Yuni Astuti {runId}`
102. Verifikasi blok putaran pertama dengan Approval `Not required` tampil tanpa daftar approver
103. Verifikasi blok putaran kedua yang ditolak tetap tampil dengan approver `Wawan Hartono {runId}` berstatus `Rejected`
104. Klik ikon silang pada dialog `Transaction Rules`

### Approval Progress dari halaman Review menampilkan progres approver lain tanpa Approval Note
105. Buka halaman `Approvals > Assignment`
106. Ketik Search `Hana Putri {runId}`, tekan Enter
107. Klik `Transaction ID` pada baris `Hana Putri {runId}`
108. Klik sel `Approval Rule` pada baris `Mesin Las Lincoln {runId}`
109. Verifikasi dialog `Approval Progress` terbuka dengan identitas `Asset : [Asset Name]` dengan Asset Name `Mesin Las Lincoln {runId}`
110. Verifikasi dialog `Approval Progress` hanya memuat bagian Approval Progress tanpa batas efektif `Allowed assignee`
111. Verifikasi approver `Wawan Hartono {runId}` berstatus `Approved` disertai waktu keputusan pada dialog `Approval Progress`
112. Verifikasi Approval Note `Site work postponed` milik `Wawan Hartono {runId}` tidak ditampilkan pada dialog `Approval Progress`
113. Verifikasi blok putaran pengajuan ini berada paling atas dan terbuka pada dialog `Approval Progress`
114. Klik ikon silang pada dialog `Approval Progress`

### Draft yang belum diajukan tampil di tab Drafts
115. Buka halaman `Transactions > Assignment`
116. Klik tab `Drafts`
117. Ketik Search `Budi Santoso {runId}`, tekan Enter
118. Verifikasi baris Draft dengan Assignee `Budi Santoso {runId}` tampil di tab `Drafts`

### Baris ditutup sistem karena aset dilaporkan hilang
119. Buka halaman `Transactions > Assignment`
120. Klik tab `History`
121. Ganti isi kotak search dengan `Switch Cisco C9200 {runId}`, tekan Enter
122. Klik Transaction ID pada baris ASG hasil
123. Klik `⋯` pada baris `Switch Cisco C9200 {runId}`
124. Klik `Transaction Rules`
125. Verifikasi putaran approval baris `Switch Cisco C9200 {runId}` tetap tampil sebagai blok pada bagian `Approval Progress`
126. Verifikasi approver `Wawan Hartono {runId}` dan `Xena Pramesti {runId}` yang belum bertindak berstatus `Not Involved` karena baris ditutup sistem dengan alasan `Asset reported missing`
127. Klik ikon silang pada dialog `Transaction Rules`

### Baris ditutup sistem karena Approval Workflow dicabut
128. Buka halaman `Transactions > Assignment`
129. Klik tab `History`
130. Ganti isi kotak search dengan `Firewall Fortinet 60F {runId}`, tekan Enter
131. Klik Transaction ID pada baris ASG hasil
132. Klik `⋯` pada baris `Firewall Fortinet 60F {runId}`
133. Klik `Transaction Rules`
134. Verifikasi approver `Wawan Hartono {runId}` dan `Xena Pramesti {runId}` yang belum bertindak berstatus `Not Involved` karena baris ditutup sistem dengan alasan `Approval Workflow removed`
135. Klik ikon silang pada dialog `Transaction Rules`

### Baris ditutup sistem karena Assignee dinonaktifkan
136. Buka halaman `Transactions > Assignment`
137. Klik tab `History`
138. Ganti isi kotak search dengan `Router Cisco ISR4331 {runId}`, tekan Enter
139. Klik Transaction ID pada baris ASG hasil
140. Klik `⋯` pada baris `Router Cisco ISR4331 {runId}`
141. Klik `Transaction Rules`
142. Verifikasi approver `Wawan Hartono {runId}` dan `Xena Pramesti {runId}` yang belum bertindak berstatus `Not Involved` karena baris ditutup sistem dengan alasan `Assignee deactivated`
143. Klik ikon silang pada dialog `Transaction Rules`

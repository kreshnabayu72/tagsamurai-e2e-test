---
id: TC-FA-ASSIGN-E2E-026-approvals-antrean-active-history
title: "Approvals > Assignment: antrean Active, History, dan Detail read-only"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["T-ASG-06", "T-ASG-07", "F-ASSIGN-14", "F-ASSIGN-05.k4", "§4.1#r18", "§4.2.10#b1", "§4.2.10#b2", "§4.2.10#b3", "§4.2.10#p1", "§9.5#r7", "EC-ASG-79", "FI-ASG-123", "FI-ASG-124", "FI-ASG-125", "ASSIGN-LOGIC-07r", "FI-ASG-111", "FI-ASG-112", "ASSIGN-LOGIC-07y", "EC-ASG-119"]
smoke: []
dependsOn: []
trace:
  "T-ASG-06": [11, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 27, 29, 31, 33, 35, 36, 38, 39, 41, 42, 45, 46, 47, 48, 49, 53, 54, 57, 59, 96, 97, 119, 120, 122, 124, 126, 128, 130, 132, 134, 136, 137, 142, 143, 148, 149, 153, 154]
  "T-ASG-07": [67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 83, 85, 88, 89, 94, 160, 162, 164, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 190, 192, 193, 195, 196, 198, 199, 201, 202, 207, 208, 214, 215, 220, 221, 225, 226, 230, 231, 235, 239, 258, 266]
  "F-ASSIGN-14": [5, 59]
  "F-ASSIGN-05.k4": [8, 70, 102, 114]
  "§4.1#r18": 4
  "§4.2.10#b1": [10, 12, 13, 14, 70, 80]
  "§4.2.10#b2": [70, 74, 75, 76, 77, 80, 81, 82, 235, 261, 269]
  "§4.2.10#b3": [6, 68, 136, 137, 189, 190, 192, 193, 195, 196, 198, 199, 201, 202]
  "§4.2.10#p1": 2
  "§9.5#r7": [23, 79]
  "EC-ASG-79": [101, 102, 103, 104, 106, 107, 114, 115]
  "FI-ASG-123": [101, 104, 105, 106, 107, 115]
  "FI-ASG-124": [102, 103, 114]
  "FI-ASG-125": 109
  "ASSIGN-LOGIC-07r": [8, 9, 244, 251]
  "FI-ASG-111": [59, 62]
  "FI-ASG-112": [64, 246, 253]
  "ASSIGN-LOGIC-07y": [64, 246, 253]
  "EC-ASG-119": [64, 246, 253]
anchor: []
coverage:
  web: automated
---

# Approvals > Assignment: antrean Active, History, dan Detail read-only

## Prerequisites
- Aktor: Approver `Rina Wulandari {runId}` (DU-026-1). Aktor lain hanya pada blok yang menyebut namanya: `Bayu Hidayat {runId}` (DU-026-3), `Hendra Kusuma {runId}` (DU-026-16), `Dewi Anggraini {runId}` (DU-026-18), dan `Eko Santoso {runId}` (DU-026-19).
- Layar awal: halaman utama setelah masuk, sidebar tampil.
- Data:
  - DU-026-1: User `Rina Wulandari {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office` dan `Branch Surabaya`. Hanya ia yang berhak atas antrean Approvals di spec ini; daftar Active-nya hanya berisi DU-026-5, DU-026-6, dan DU-026-17.
  - DU-026-2: User `Agus Pratama {runId}`, Role `Asset Admin`, Group penugasan `Head Office`, pengaju DU-026-5, DU-026-7, DU-026-9, DU-026-11, DU-026-12, dan DU-026-13.
  - DU-026-3: User `Bayu Hidayat {runId}`, Role `Asset Admin` dan Role Transaksi `Approver`, Group penugasan `Branch Surabaya`, pengaju DU-026-6, DU-026-8, DU-026-10, DU-026-14, dan DU-026-21; approver `Drone DJI Mavic 3 {runId}` di DU-026-17.
  - DU-026-4: User `Tono Wibowo {runId}`, Role Transaksi `Approver`, Group penugasan `Head Office` dan `Branch Surabaya`, approver kedua pada DU-026-6, DU-026-10, DU-026-11, DU-026-12, dan DU-026-13, serta approver `Kamera Canon EOS R6 {runId}`, `Mikrofon Rode NT1 {runId}`, dan `Tripod Manfrotto 055 {runId}` di DU-026-17.
  - DU-026-5: Pengajuan A, Group `Head Office`, Assignee `Sari Dewi {runId}`, Total Asset `2` (`Laptop Dell Latitude 5420 {runId}`, `Monitor LG 24 {runId}`), Requested By `Agus Pratama {runId}`, Request Date `T0 − 3 hari, pukul 10:00`, Approval type `Any one approver`, belum diputuskan Rina. Dibuat lebih dulu daripada DU-026-6.
  - DU-026-6: Pengajuan B, Group `Branch Surabaya`, Assignee Division `Finance {runId}` dengan PIC `Hendra Kusuma {runId}`, Total Asset `3` (`Printer HP M404 {runId}`, `Projector Epson EB-X49 {runId}`, `Tablet Samsung Tab S8 {runId}`), Requested By `Bayu Hidayat {runId}`, Request Date `T0 − 1 hari, pukul 14:30`, Approval type `Any one approver`, belum diputuskan Rina. Approver `Projector Epson EB-X49 {runId}` dan `Tablet Samsung Tab S8 {runId}`: `Rina Wulandari {runId}` dan `Tono Wibowo {runId}` (DU-026-4). Pengaju (`Bayu Hidayat {runId}`) dan PIC (`Hendra Kusuma {runId}`) pengajuan ini tidak menjadi approver aset mana pun di dalamnya.
  - DU-026-7: Pengajuan C, Group `Head Office`, Assignee `Budi Santoso {runId}`, Total Asset `1` (`Kamera Sony A7 {runId}`), Requested By `Agus Pratama {runId}`, Request Date `T0 − 9 hari, pukul 13:40`, Decided Date `T0 − 8 hari, pukul 16:05`; Rina menyetujui satu aset; Status History `Approved`.
  - DU-026-8: Pengajuan D, Group `Branch Surabaya`, Assignee `Dewi Lestari {runId}`, Total Asset `1` (`Genset Cummins C100 {runId}`), Requested By `Bayu Hidayat {runId}`, Request Date `T0 − 13 hari, pukul 09:00`, Decided Date `T0 − 12 hari, pukul 10:30`; Rina menolak satu aset; Status History `Rejected`.
  - DU-026-9: Pengajuan E, Group `Head Office`, Assignee `Hana Putri {runId}`, Total Asset `2` (`Toyota Avanza {runId}` disetujui, `Excavator PC200 {runId}` ditolak), Requested By `Agus Pratama {runId}`, Request Date `T0 − 5 hari, pukul 08:30`, Decided Date `T0 − 4 hari, pukul 15:20`; Status History `Partially Approved`.
  - DU-026-10: Pengajuan F, Group `Branch Surabaya`, Assignee `Joko Susilo {runId}`, Total Asset `1` (`Forklift Toyota 8FD {runId}`), Approval type `All approvers`, Requested By `Bayu Hidayat {runId}`, Request Date `T0 − 2 hari, pukul 11:00`, Decided Date `T0 − 1 hari, pukul 09:15`; Rina sudah menyetujui, `Tono Wibowo {runId}` belum bertindak; Status History `Waiting for Approval`.
  - DU-026-11: Pengajuan G, Group `Head Office`, Assignee `Lina Marlina {runId}`, Total Asset `1` (`Genset Perkins P20 {runId}`), Approval type `All approvers`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 6 hari, pukul 10:10`, Decided Date `T0 − 3 hari, pukul 11:00`; Rina sudah menyetujui lalu pengaju membatalkan pengajuan; Status History `Canceled`.
  - DU-026-12: Pengajuan H, Group `Head Office`, Assignee `Rina Wulandari {runId}` (DU-026-1), Total Asset `1` (`Laptop Lenovo ThinkPad T14 {runId}`), Requested By `Agus Pratama {runId}`, Request Date `T0 − 2 hari, pukul 15:45`; approver aset itu hanya `Tono Wibowo {runId}`.
  - DU-026-13: Pengajuan I, Group `Head Office`, Assignee `Mira Anjani {runId}`, Total Asset `1` (`Monitor Dell P2422H {runId}`), Approval type `Any one approver`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 4 hari, pukul 09:50`; `Tono Wibowo {runId}` sudah menyetujui, Rina belum bertindak.
  - DU-026-14: Pengajuan J, Group `Branch Surabaya`, Assignee `Nina Safitri {runId}`, Total Asset `1` (`Scanner Canon LiDE {runId}`), Requested By `Bayu Hidayat {runId}`, Request Date `T0 − 7 hari, pukul 14:00`; dibatalkan pengaju sebelum Rina memutuskan satu asetnya pun.
  - DU-026-15: Group `Branch Surabaya` adalah anak langsung Group `Head Office`, sehingga hierarki lengkap `Branch Surabaya` adalah `Head Office > Branch Surabaya`.
  - DU-026-16: User `Hendra Kusuma {runId}`, Role Transaksi `Approver`, Group penugasan `Branch Surabaya`, karyawan anggota Division `Finance {runId}` dan PIC-nya pada DU-026-6; approver `Drone DJI Mavic 3 {runId}` di DU-026-17.
  - DU-026-17: Pengajuan K, Group `Head Office`, Assignee `Wawan Hartono {runId}`, Total Asset `4`, Requested By `Agus Pratama {runId}`, Request Date `T0 − 5 hari, pukul 16:20`, Approval type `Any one approver`; keempat barisnya: `Drone DJI Mavic 3 {runId}` berstatus `Waiting for Approval` dengan approver `Rina Wulandari {runId}`, `Hendra Kusuma {runId}`, dan `Bayu Hidayat {runId}` yang belum memutuskan; `Kamera Canon EOS R6 {runId}` berstatus `Waiting for Handover` karena `Tono Wibowo {runId}` menyetujuinya; `Mikrofon Rode NT1 {runId}` berstatus `Rejected` karena `Tono Wibowo {runId}` menolaknya; `Tripod Manfrotto 055 {runId}` berstatus `Canceled` karena pengaju membatalkan barisnya sebelum ada keputusan. Rina belum memutuskan aset mana pun di pengajuan ini.
  - DU-026-18: User `Dewi Anggraini {runId}`, Role `Total Control`, cakupan seluruh client, approver yang eligible dan menyetujui aset di DU-026-20.
  - DU-026-19: User `Eko Santoso {runId}`, Role `Group Manager`, Group binaan `Branch Surabaya`, approver yang eligible dan menyetujui aset di DU-026-21.
  - DU-026-20: Pengajuan M, Group `Head Office`, Assignee `Dani Prakoso {runId}`, Total Asset `1` (`Server Dell R740 {runId}`), Requested By `Agus Pratama {runId}`, Request Date `T0 − 8 hari, pukul 10:00`, Decided Date `T0 − 7 hari, pukul 11:15`; satu-satunya approver aset itu `Dewi Anggraini {runId}` dan ia menyetujuinya; Status History `Approved`.
  - DU-026-21: Pengajuan N, Group `Branch Surabaya`, Assignee `Fitri Handayani {runId}`, Total Asset `1` (`Switch Cisco 2960 {runId}`), Requested By `Bayu Hidayat {runId}`, Request Date `T0 − 10 hari, pukul 13:20`, Decided Date `T0 − 9 hari, pukul 09:40`; satu-satunya approver aset itu `Eko Santoso {runId}` dan ia menyetujuinya; Status History `Approved`.
  - Transaction ID setiap pengajuan dibentuk server; Transaction ID tiap baris adalah milik entri pengajuannya. DU-026-7, DU-026-8, DU-026-9, DU-026-10, dan DU-026-11 dibuat berurutan dalam urutan itu.

## Test Steps

### Menu Approvals memiliki anak Assignment dan halaman memuat tab Active dan History
1. Perluas menu `Approvals` pada sidebar
2. Verifikasi menu `Approvals` memiliki anak `Assignment`
3. Klik `Assignment`
4. Verifikasi tab `Active` dan tab `History` tampil
5. Verifikasi tab `Active` terbuka lebih dulu dengan breadcrumb `Approvals > Assignment > Active`

### Antrean Active hanya memuat pengajuan dengan aset yang belum diputuskan approver
6. Verifikasi kotak Search memakai placeholder `Search transaction ID or assignee...`
7. Ketik Search `{runId}`, tekan Enter
8. Verifikasi baris pengajuan dengan Assignee `Sari Dewi {runId}` tampil di tab `Active`
9. Verifikasi baris pengajuan dengan Assignee `Finance {runId}` tampil di tab `Active`
10. Verifikasi badge pada tab `Active` menunjukkan jumlah `3`
11. Verifikasi tidak ada baris dengan Assignee `Rina Wulandari {runId}` karena pengajuan itu milik approver sendiri
12. Verifikasi tidak ada baris dengan Assignee `Mira Anjani {runId}` karena aset Any one sudah diputuskan approver lain lebih dulu
13. Verifikasi tidak ada baris dengan Assignee `Nina Safitri {runId}` karena pengajuan dibatalkan sebelum approver memutuskan satu asetnya pun
14. Verifikasi tidak ada baris dengan Assignee `Joko Susilo {runId}` karena seluruh aset milik approver sudah diputuskan

### Kolom tabel Active menampilkan data pengajuan
15. Verifikasi tabel Active menampilkan kolom `Transaction ID`, `Group`, `Assignee`, `Total Asset`, `Requested By`, dan `Request Date`
16. Verifikasi `Transaction ID` pada baris `Sari Dewi {runId}` berformat `ASG-YYYY-NNNN` dan memiliki tombol copy
17. Verifikasi badge Group pada baris `Sari Dewi {runId}` bernilai `Head Office`
18. Verifikasi `Total Asset` pada baris `Sari Dewi {runId}` bernilai `2`
19. Verifikasi `Total Asset` pada baris `Finance {runId}` bernilai `3`
20. Verifikasi `Requested By` pada baris `Sari Dewi {runId}` bernilai `Agus Pratama {runId}`
21. Verifikasi `Request Date` pada baris `Sari Dewi {runId}` terisi
22. Verifikasi PIC `Hendra Kusuma {runId}` tersampaikan pada Assignee `Finance {runId}`

### Urutan bawaan dan sort kolom Active
23. Verifikasi urutan bawaan memuat `Request Date` terlama di atas: baris `Sari Dewi {runId}` di atas baris `Finance {runId}`
24. Klik header `Total Asset`
25. Verifikasi baris `Sari Dewi {runId}` (`Total Asset` `2`) berada di atas baris `Finance {runId}` (`Total Asset` `3`)
26. Klik header `Total Asset`
27. Verifikasi baris `Finance {runId}` berada di atas baris `Sari Dewi {runId}`
28. Klik header `Group`
29. Verifikasi baris `Finance {runId}` (Group `Branch Surabaya`) berada di atas baris `Sari Dewi {runId}` (Group `Head Office`)
30. Klik header `Requested By`
31. Verifikasi baris `Sari Dewi {runId}` (`Agus Pratama {runId}`) berada di atas baris `Finance {runId}` (`Bayu Hidayat {runId}`)
32. Klik header `Transaction ID`
33. Verifikasi baris `Sari Dewi {runId}` berada di atas baris `Finance {runId}` menurut urutan `Transaction ID` menaik

### Search di tab Active mencari kolom Searchable
34. Ganti isi kotak search dengan `Bayu Hidayat {runId}`, tekan Enter
35. Verifikasi baris `Finance {runId}` tampil
36. Verifikasi tidak ada baris dengan Assignee `Sari Dewi {runId}`
37. Ganti isi kotak search dengan `Sari Dewi {runId}`, tekan Enter
38. Verifikasi baris `Sari Dewi {runId}` tampil
39. Verifikasi tidak ada baris dengan Assignee `Finance {runId}`
40. Ganti isi kotak search dengan `Branch Surabaya`, tekan Enter
41. Verifikasi baris `Finance {runId}` tampil
42. Verifikasi tidak ada baris dengan Assignee `Sari Dewi {runId}`
43. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Filter di tab Active menyaring pengajuan
44. Klik `Filter`
45. Verifikasi field filter `Group` memakai placeholder `All groups`
46. Verifikasi field filter `Assignee` memakai placeholder `All assignees`
47. Verifikasi field filter `Total Asset` memiliki isian `Min` dan `Max`
48. Verifikasi field filter `Requested By` memakai placeholder `All users`
49. Verifikasi field filter `Request Date` memakai placeholder `Select date`
50. Isi `Min` pada field `Total Asset` dengan `3`
51. Isi `Max` pada field `Total Asset` dengan `3`
52. Klik `[Apply]`
53. Verifikasi baris `Finance {runId}` tampil
54. Verifikasi tidak ada baris dengan Assignee `Sari Dewi {runId}`
55. Klik `[Clear Field]`
56. Klik `[Apply]`
57. Verifikasi baris `Sari Dewi {runId}` dan baris `Finance {runId}` tampil kembali

### Transaction ID di tab Active membuka halaman Review untuk approver aset
58. Klik `Transaction ID` pada baris `Sari Dewi {runId}`
59. Verifikasi halaman Review terbuka dengan breadcrumb `Approvals > Assignment > Active > Review`
60. Klik `[Cancel]` pada footer halaman Review

### Halaman Review pengajuan milik approver sendiri ditolak lewat alamat langsung
61. Buka langsung alamat halaman Review pengajuan milik DU-026-5
62. Verifikasi halaman Review pengajuan `Sari Dewi {runId}` terbuka untuk approver aset itu
63. Buka langsung alamat halaman Review pengajuan milik DU-026-12
64. Verifikasi halaman Review pengajuan itu tampil read-only dengan notice `You cannot decide an assignment you requested or are assigned to.`, tanpa tombol `[Submit]`

### Antrean History memuat pengajuan yang asetnya diputuskan approver
65. Buka halaman `Approvals > Assignment`
66. Klik tab `History`
67. Verifikasi tabel History menampilkan kolom `Transaction ID`, `Status`, `Group`, `Assignee`, `Total Asset`, `Requested By`, `Request Date`, dan `Decided Date`
68. Verifikasi kotak Search memakai placeholder `Search transaction ID or assignee...` di tab `History`
69. Ketik Search `{runId}`, tekan Enter
70. Verifikasi baris dengan Assignee `Joko Susilo {runId}` tampil di tab `History` dengan Status `Waiting for Approval`
71. Verifikasi `Decided Date` pada baris `Budi Santoso {runId}` terisi
72. Verifikasi badge Group pada baris `Dewi Lestari {runId}` bernilai `Branch Surabaya`
73. Verifikasi `Total Asset` pada baris `Hana Putri {runId}` bernilai `2`
74. Verifikasi baris dengan Assignee `Budi Santoso {runId}` tampil di tab `History` dengan Status `Approved`
75. Verifikasi baris dengan Assignee `Hana Putri {runId}` tampil di tab `History` dengan Status `Partially Approved`
76. Verifikasi baris dengan Assignee `Dewi Lestari {runId}` tampil di tab `History` dengan Status `Rejected`
77. Verifikasi baris dengan Assignee `Lina Marlina {runId}` tampil di tab `History` dengan Status `Canceled`
78. Verifikasi hover pada badge `Status` baris `Hana Putri {runId}` berisi `1 approved · 1 rejected`, jumlah aset yang diputuskan
79. Verifikasi urutan bawaan memuat `Decided Date` terbaru di atas: `Joko Susilo {runId}`, `Lina Marlina {runId}`, `Hana Putri {runId}`, `Budi Santoso {runId}`, lalu `Dewi Lestari {runId}`
80. Verifikasi tidak ada baris dengan Assignee `Mira Anjani {runId}` di tab `History` karena keputusan approver lain pada aset Any one tidak membuat pengajuan masuk History
81. Verifikasi tidak ada baris dengan Assignee `Nina Safitri {runId}` di tab `History` karena pengajuan dibatalkan sebelum approver memutuskan satu asetnya pun
82. Verifikasi tidak ada baris dengan Assignee `Sari Dewi {runId}` di tab `History` karena asetnya belum diputuskan approver
83. Verifikasi tombol `Download` tampil di tab `History`

### Filter Status di tab History
84. Klik `Filter`
85. Verifikasi field filter `Status` memakai placeholder `All statuses`
86. Pilih Status `Approved` pada field filter `Status`
87. Klik `[Apply]`
88. Verifikasi baris `Budi Santoso {runId}` tampil
89. Verifikasi tidak ada baris dengan Assignee `Dewi Lestari {runId}` di tab `History`
90. Klik `[Clear Field]`
91. Klik `[Apply]`

### Download hanya ada di tab History
92. Klik `Download`
93. Pilih `Download as CSV`
94. Verifikasi berkas yang diunduh bernama `Approvals-Assignment-History`
95. Klik tab `Active`
96. Verifikasi baris `Sari Dewi {runId}` tampil di tab `Active`
97. Verifikasi tombol `Download` tidak ada di tab `Active`

### Detail di tab History membuka halaman Review read-only untuk pengajuan yang sudah ditutup
98. Klik tab `History`
99. Klik `⋯` pada baris `Hana Putri {runId}`
100. Klik `Detail`
101. Verifikasi breadcrumb `Approvals > Assignment > History > Detail`
102. Verifikasi keputusan aset `Toyota Avanza {runId}` tampil sebagai hasil `Approved`
103. Verifikasi keputusan aset `Excavator PC200 {runId}` tampil sebagai hasil `Rejected`
104. Verifikasi kolom `Approval` tidak memuat toggle `Approve` atau `Reject`
105. Verifikasi kolom `Approval Note` tidak dapat diisi
106. Verifikasi toolbar bulk tidak tampil
107. Verifikasi footer dengan `[Submit]` tidak tampil
108. Klik sel `Approval Rule` pada baris `Toyota Avanza {runId}`
109. Verifikasi dialog `Approval Progress` terbuka
110. Klik ikon silang pada dialog `Approval Progress`

### Detail di tab History membuka halaman Review read-only untuk pengajuan yang masih menunggu approver lain
111. Klik `History` pada breadcrumb
112. Klik `⋯` pada baris `Joko Susilo {runId}`
113. Klik `Detail`
114. Verifikasi keputusan aset `Forklift Toyota 8FD {runId}` tampil sebagai hasil `Waiting for Approval`
115. Verifikasi toolbar bulk dan footer dengan `[Submit]` tidak tampil

### Total Asset menghitung semua baris dan hover kolom tab Active
116. Buka halaman `Approvals > Assignment`
117. Klik tab `Active`
118. Ganti isi kotak search dengan `{runId}`, tekan Enter
119. Verifikasi baris dengan Assignee `Wawan Hartono {runId}` tampil di tab `Active`
120. Verifikasi `Total Asset` pada baris `Wawan Hartono {runId}` bernilai `4`, dihitung dari satu baris `Waiting for Approval`, satu `Waiting for Handover`, satu `Rejected`, dan satu `Canceled`
121. Arahkan kursor ke badge Group pada baris `Finance {runId}`
122. Verifikasi hierarki lengkap Group tampil sebagai `Head Office > Branch Surabaya`
123. Arahkan kursor ke nilai Assignee pada baris `Sari Dewi {runId}`
124. Verifikasi nama lengkap `Sari Dewi {runId}` tampil
125. Arahkan kursor ke nilai `Requested By` pada baris `Sari Dewi {runId}`
126. Verifikasi nama lengkap `Agus Pratama {runId}` tampil
127. Klik tombol copy pada `Transaction ID` baris `Sari Dewi {runId}`
128. Verifikasi toast `Success, Transaction ID has been copied.` tampil

### Sort kolom Assignee dan Request Date di tab Active
129. Klik header `Assignee`
130. Verifikasi kolom `Assignee` terurut A-Z: `Finance {runId}`, `Sari Dewi {runId}`, `Wawan Hartono {runId}`
131. Klik header `Request Date`
132. Verifikasi kolom `Request Date` terurut Oldest First: `Wawan Hartono {runId}`, `Sari Dewi {runId}`, `Finance {runId}`
133. Klik header `Request Date`
134. Verifikasi kolom `Request Date` terurut Newest First: `Finance {runId}`, `Sari Dewi {runId}`, `Wawan Hartono {runId}`

### Search Transaction ID di tab Active
135. Ganti isi kotak search dengan Transaction ID milik DU-026-5, tekan Enter
136. Verifikasi baris `Sari Dewi {runId}` tampil
137. Verifikasi tidak ada baris dengan Assignee `Finance {runId}`
138. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Filter Assignee, Requested By, dan Request Date di tab Active
139. Klik `Filter`
140. Pilih Assignee `Finance {runId}` pada field filter `Assignee`
141. Klik `[Apply]`
142. Verifikasi baris `Finance {runId}` tampil
143. Verifikasi tidak ada baris dengan Assignee `Sari Dewi {runId}`
144. Klik `[Clear Field]`
145. Klik `[Apply]`
146. Pilih Requested By `Bayu Hidayat {runId}` pada field filter `Requested By`
147. Klik `[Apply]`
148. Verifikasi baris `Finance {runId}` tampil
149. Verifikasi tidak ada baris dengan Assignee `Sari Dewi {runId}` dan tidak ada baris dengan Assignee `Wawan Hartono {runId}`
150. Klik `[Clear Field]`
151. Klik `[Apply]`
152. Pilih rentang `Request Date` dari T0 − 4 hari sampai T0 − 2 hari, lalu klik `[Apply]`
153. Verifikasi baris `Sari Dewi {runId}` tampil
154. Verifikasi tidak ada baris dengan Assignee `Finance {runId}` dan tidak ada baris dengan Assignee `Wawan Hartono {runId}`
155. Klik `[Clear Field]`
156. Klik `[Apply]`

### Hover kolom di tab History
157. Klik tab `History`
158. Ganti isi kotak search dengan `{runId}`, tekan Enter
159. Arahkan kursor ke badge Group pada baris `Dewi Lestari {runId}`
160. Verifikasi hierarki lengkap Group tampil sebagai `Head Office > Branch Surabaya`
161. Arahkan kursor ke nilai Assignee pada baris `Hana Putri {runId}`
162. Verifikasi nama lengkap `Hana Putri {runId}` tampil
163. Arahkan kursor ke nilai `Requested By` pada baris `Hana Putri {runId}`
164. Verifikasi nama lengkap `Agus Pratama {runId}` tampil

### Sort kolom di tab History
165. Verifikasi tabel History memuat baris `Budi Santoso {runId}`, `Dewi Lestari {runId}`, `Hana Putri {runId}`, `Joko Susilo {runId}`, dan `Lina Marlina {runId}`
166. Klik header `Status`
167. Verifikasi kolom `Status` terurut A-Z: `Budi Santoso {runId}` (`Approved`), `Lina Marlina {runId}` (`Canceled`), `Hana Putri {runId}` (`Partially Approved`), `Dewi Lestari {runId}` (`Rejected`), `Joko Susilo {runId}` (`Waiting for Approval`)
168. Klik header `Group`
169. Verifikasi kolom `Group` terurut A-Z: baris `Dewi Lestari {runId}` dan `Joko Susilo {runId}` (`Branch Surabaya`) berada di atas baris `Budi Santoso {runId}`, `Hana Putri {runId}`, dan `Lina Marlina {runId}` (`Head Office`)
170. Klik header `Assignee`
171. Verifikasi kolom `Assignee` terurut A-Z: `Budi Santoso {runId}`, `Dewi Lestari {runId}`, `Hana Putri {runId}`, `Joko Susilo {runId}`, `Lina Marlina {runId}`
172. Klik header `Total Asset`
173. Verifikasi kolom `Total Asset` terurut dari kecil ke besar: baris `Hana Putri {runId}` (`2`) berada paling bawah, di bawah keempat baris lain (`1`)
174. Klik header `Total Asset`
175. Verifikasi kolom `Total Asset` terurut dari besar ke kecil: baris `Hana Putri {runId}` (`2`) berada paling atas
176. Klik header `Requested By`
177. Verifikasi kolom `Requested By` terurut A-Z: baris `Budi Santoso {runId}`, `Hana Putri {runId}`, dan `Lina Marlina {runId}` (`Agus Pratama {runId}`) berada di atas baris `Dewi Lestari {runId}` dan `Joko Susilo {runId}` (`Bayu Hidayat {runId}`)
178. Klik header `Request Date`
179. Verifikasi kolom `Request Date` terurut Oldest First: `Dewi Lestari {runId}`, `Budi Santoso {runId}`, `Lina Marlina {runId}`, `Hana Putri {runId}`, `Joko Susilo {runId}`
180. Klik header `Request Date`
181. Verifikasi kolom `Request Date` terurut Newest First: `Joko Susilo {runId}`, `Hana Putri {runId}`, `Lina Marlina {runId}`, `Budi Santoso {runId}`, `Dewi Lestari {runId}`
182. Klik header `Decided Date`
183. Verifikasi kolom `Decided Date` terurut Oldest First: `Dewi Lestari {runId}`, `Budi Santoso {runId}`, `Hana Putri {runId}`, `Lina Marlina {runId}`, `Joko Susilo {runId}`
184. Klik header `Decided Date`
185. Verifikasi kolom `Decided Date` terurut Newest First: `Joko Susilo {runId}`, `Lina Marlina {runId}`, `Hana Putri {runId}`, `Budi Santoso {runId}`, `Dewi Lestari {runId}`
186. Klik header `Transaction ID`
187. Verifikasi kolom `Transaction ID` terurut menaik menurut urutan pembuatan: `Budi Santoso {runId}`, `Dewi Lestari {runId}`, `Hana Putri {runId}`, `Joko Susilo {runId}`, `Lina Marlina {runId}`

### Search kolom Searchable di tab History
188. Ganti isi kotak search dengan `Rejected`, tekan Enter
189. Verifikasi baris `Dewi Lestari {runId}` tampil
190. Verifikasi tidak ada baris dengan Assignee `Budi Santoso {runId}`
191. Ganti isi kotak search dengan `Branch Surabaya`, tekan Enter
192. Verifikasi baris `Joko Susilo {runId}` tampil
193. Verifikasi tidak ada baris dengan Assignee `Budi Santoso {runId}`
194. Ganti isi kotak search dengan `Hana Putri {runId}`, tekan Enter
195. Verifikasi baris `Hana Putri {runId}` tampil
196. Verifikasi tidak ada baris dengan Assignee `Budi Santoso {runId}`
197. Ganti isi kotak search dengan `Bayu Hidayat {runId}`, tekan Enter
198. Verifikasi baris `Dewi Lestari {runId}` dan baris `Joko Susilo {runId}` tampil
199. Verifikasi tidak ada baris dengan Assignee `Hana Putri {runId}`
200. Ganti isi kotak search dengan Transaction ID milik DU-026-9, tekan Enter
201. Verifikasi baris `Hana Putri {runId}` tampil
202. Verifikasi tidak ada baris dengan Assignee `Budi Santoso {runId}`
203. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Filter Assignee, Total Asset, Requested By, Request Date, dan Decided Date di tab History
204. Klik `Filter`
205. Pilih Assignee `Hana Putri {runId}` pada field filter `Assignee`
206. Klik `[Apply]`
207. Verifikasi baris `Hana Putri {runId}` tampil
208. Verifikasi tidak ada baris dengan Assignee `Budi Santoso {runId}`
209. Klik `[Clear Field]`
210. Klik `[Apply]`
211. Isi `Min` pada field `Total Asset` dengan `2`
212. Isi `Max` pada field `Total Asset` dengan `2`
213. Klik `[Apply]`
214. Verifikasi baris `Hana Putri {runId}` tampil
215. Verifikasi tidak ada baris dengan Assignee `Budi Santoso {runId}`
216. Klik `[Clear Field]`
217. Klik `[Apply]`
218. Pilih Requested By `Bayu Hidayat {runId}` pada field filter `Requested By`
219. Klik `[Apply]`
220. Verifikasi baris `Dewi Lestari {runId}` dan baris `Joko Susilo {runId}` tampil
221. Verifikasi tidak ada baris dengan Assignee `Hana Putri {runId}`
222. Klik `[Clear Field]`
223. Klik `[Apply]`
224. Pilih rentang `Request Date` dari T0 − 7 hari sampai T0 − 4 hari, lalu klik `[Apply]`
225. Verifikasi baris `Lina Marlina {runId}` dan baris `Hana Putri {runId}` tampil
226. Verifikasi tidak ada baris dengan Assignee `Budi Santoso {runId}` dan tidak ada baris dengan Assignee `Joko Susilo {runId}`
227. Klik `[Clear Field]`
228. Klik `[Apply]`
229. Pilih rentang `Decided Date` dari T0 − 13 hari sampai T0 − 7 hari, lalu klik `[Apply]`
230. Verifikasi baris `Dewi Lestari {runId}` dan baris `Budi Santoso {runId}` tampil
231. Verifikasi tidak ada baris dengan Assignee `Hana Putri {runId}`
232. Klik `[Clear Field]`
233. Klik `[Apply]`

### Transaction ID di tab History membuka Detail read-only dan Download XLSX
234. Klik `Transaction ID` pada baris `Budi Santoso {runId}`
235. Verifikasi breadcrumb `Approvals > Assignment > History > Detail`
236. Klik `History` pada breadcrumb
237. Klik `Download`
238. Pilih `Download as XLSX`
239. Verifikasi berkas yang diunduh bernama `Approvals-Assignment-History`

### Pengaju yang juga approver di pengajuan lain tidak dapat membuka Review pengajuannya sendiri lewat alamat langsung
240. Keluar dari akun lalu masuk sebagai `Bayu Hidayat {runId}`
241. Buka halaman `Approvals > Assignment`
242. Klik tab `Active`
243. Ketik Search `{runId}`, tekan Enter
244. Verifikasi baris dengan Assignee `Wawan Hartono {runId}` tampil di tab `Active`
245. Buka langsung alamat halaman Review pengajuan milik DU-026-6
246. Verifikasi halaman Review pengajuan itu tampil read-only dengan notice `You cannot decide an assignment you requested or are assigned to.`, tanpa tombol `[Submit]`

### PIC yang juga approver di pengajuan lain tidak dapat membuka Review pengajuan Division-nya lewat alamat langsung
247. Keluar dari akun lalu masuk sebagai `Hendra Kusuma {runId}`
248. Buka halaman `Approvals > Assignment`
249. Klik tab `Active`
250. Ketik Search `{runId}`, tekan Enter
251. Verifikasi baris dengan Assignee `Wawan Hartono {runId}` tampil di tab `Active`
252. Buka langsung alamat halaman Review pengajuan milik DU-026-6
253. Verifikasi halaman Review pengajuan itu tampil read-only dengan notice `You cannot decide an assignment you requested or are assigned to.`, tanpa tombol `[Submit]`

### Total Control yang menjadi approver membuka Assignment Detail dari Detail di tab History
254. Keluar dari akun lalu masuk sebagai `Dewi Anggraini {runId}`
255. Buka halaman `Approvals > Assignment`
256. Klik tab `History`
257. Ketik Search `Dani Prakoso {runId}`, tekan Enter
258. Verifikasi baris dengan Assignee `Dani Prakoso {runId}` tampil di tab `History` dengan Status `Approved`
259. Klik `⋯` pada baris `Dani Prakoso {runId}`
260. Klik `Detail`
261. Verifikasi halaman Assignment Detail terbuka dengan baris judul memuat Transaction ID berformat `ASG-YYYY-NNNN` dan kolom `Status` pada tabel Assets, tanpa kolom `Approval Rule` milik halaman Review read-only

### Group Manager yang menjadi approver membuka Assignment Detail dari Detail di tab History
262. Keluar dari akun lalu masuk sebagai `Eko Santoso {runId}`
263. Buka halaman `Approvals > Assignment`
264. Klik tab `History`
265. Ketik Search `Fitri Handayani {runId}`, tekan Enter
266. Verifikasi baris dengan Assignee `Fitri Handayani {runId}` tampil di tab `History` dengan Status `Approved`
267. Klik `⋯` pada baris `Fitri Handayani {runId}`
268. Klik `Detail`
269. Verifikasi halaman Assignment Detail terbuka dengan baris judul memuat Transaction ID berformat `ASG-YYYY-NNNN` dan kolom `Status` pada tabel Assets, tanpa kolom `Approval Rule` milik halaman Review read-only



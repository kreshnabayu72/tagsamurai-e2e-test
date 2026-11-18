---
id: TC-FA-BORROW-E2E-012-form-pilih-borrower-dan-aset
title: "Pemilihan Borrower dan aset di form Borrow Request menampilkan opsi menurut kelayakan dan cakupan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1d#p1", "§4.1d#b1", "§4.1d#b2", "§4.1d#b5", "§4.1d#b6", "§4.1d#p4", "§4.1d#r5", "§4.1d#r6", "§4.1d#r7", "§4.1d#r8", "§4.1d#r9", "§4.1d#r10", "§4.1d#r11", "§4.1d#r12", "§4.1d#r13", "§4.1d#r14", "§4.1d#r15", "§4.1d#r16", "§4.1e#p1", "§4.1e#b1", "§4.1e#b2", "§4.1e#b3", "§4.1e#b4", "§4.1e#b5", "§4.1e#r1", "§4.1e#r2", "§4.1e#r3", "§4.1e#r4", "§4.1e#r5", "§4.1e#r6", "§4.1e#r7", "§4.1e#r8", "§4.1e#r9", "§4.1e#r10", "§4.1e#r11", "§4.1e#r12"]
smoke: []
dependsOn: []
trace:
  "§4.1d#p1": [179, 180, 181, 182, 183, 187, 188]
  "§4.1d#b1": [184, 188, 323]
  "§4.1d#b2": [185, 324, 325, 326, 336]
  "§4.1d#b5": 183
  "§4.1d#b6": [325, 336, 337]
  "§4.1d#p4": [325, 326]
  "§4.1d#r5": [189, 190, 258, 269]
  "§4.1d#r6": [191, 213, 215, 238, 260, 272]
  "§4.1d#r7": [192, 221, 240, 269]
  "§4.1d#r8": [193, 217, 242, 261, 277]
  "§4.1d#r9": [194, 219, 244, 262, 282]
  "§4.1d#r10": [195, 196, 223, 246, 263, 287, 348]
  "§4.1d#r11": [206, 207, 225, 248, 264, 292]
  "§4.1d#r12": [208, 227, 250, 265, 297]
  "§4.1d#r13": [197, 198, 229, 252, 269]
  "§4.1d#r14": [199, 200, 201, 231, 254, 266, 302]
  "§4.1d#r15": [209, 210, 233, 256, 267, 307]
  "§4.1d#r16": [186, 235, 268, 312, 324, 325, 326, 328, 336, 337]
  "§4.1e#p1": [4, 9, 14]
  "§4.1e#b1": [4, 5, 6, 7, 8]
  "§4.1e#b2": [9, 10]
  "§4.1e#b3": 12
  "§4.1e#b4": 13
  "§4.1e#b5": [10, 11, 15, 16, 17]
  "§4.1e#r1": [18, 45, 67, 69, 95, 107]
  "§4.1e#r2": [19, 47, 71, 104]
  "§4.1e#r3": [20, 49, 73, 96, 111, 113, 117]
  "§4.1e#r4": [21, 51, 75, 97, 121, 123, 127]
  "§4.1e#r5": [14, 22, 23, 53, 77, 98, 131, 133, 137]
  "§4.1e#r6": [24, 61, 79, 104]
  "§4.1e#r7": [25, 26, 27, 55, 81, 99, 142]
  "§4.1e#r8": [28, 29, 30, 31, 57, 83, 100, 146, 148, 152]
  "§4.1e#r9": [37, 63, 85, 101, 156, 158, 162]
  "§4.1e#r10": [38, 39, 59, 87, 102, 167]
  "§4.1e#r11": [40, 89, 91, 103, 172]
  "§4.1e#r12": [41, 42, 65, 93, 104]
anchor: [237]
coverage:
  web: automated
---

# Pemilihan Borrower dan aset di form Borrow Request menampilkan opsi menurut kelayakan dan cakupan

## Prerequisites
- Aktor: Asset Admin `Hendra Kusuma {runId}` (Aktor Borrow) dengan Group penugasan `Head Office` dan `Branch Surabaya`.
- Layar awal: Transactions > Borrow.
- Data:
  - DU-012-1: aset `Laptop Dell Latitude {runId}`, Brand `Dell {runId}`, Model/Type `Latitude 5420 {runId}`, Group `Head Office`, TAG `NFC`, Category `Laptop {runId}`, Label `Operasional {runId}`, Custody `Available`, Max Duration `3 days`, Approval `Auto (≤ 3 days)`, Allowed borrower `Employee in any Group`, foto utama `laptop-dell-latitude.png`.
  - DU-012-2: aset `Projector Epson EB-X06 {runId}`, Brand `Epson {runId}`, Model/Type `EB-X06 {runId}`, Group `Head Office`, TAG `QR`, Category `Projector {runId}`, tanpa Label, Custody `Available`, Max Duration `5 days`, Approval `Needs approval`, Allowed borrower `Employee in any Group`, tanpa foto utama.
  - DU-012-3: aset `Excavator PC200 {runId}`, Brand `Komatsu {runId}`, Model/Type `PC200 {runId}`, Group `Head Office`, TAG `RFID`, Category `Heavy Equipment {runId}`, Label `Event {runId}`, Custody `Available`, Max Duration `7 days`, Approval `Needs approval (all must approve)`, Allowed borrower `Employee in any Group`, tanpa foto utama.
  - DU-012-4: aset `Toyota Avanza {runId}`, Brand `Toyota {runId}`, Model/Type `Avanza {runId}`, Group `Branch Surabaya`, Non TAG, Category `Car {runId}`, Label `Rapat {runId}`, Custody `Available`, Max Duration `14 days`, Approval `Needs approval`, Allowed borrower `Same Group only`, tanpa foto utama; alasan Not ready bagi Borrower `Sari Dewi {runId}` adalah `Sari Dewi {runId} can't borrow assets from Branch Surabaya.`.
  - DU-012-5: aset `Printer Canon {runId}`, Group `Branch Medan` (di luar cakupan Aktor), Custody `Available`, Allow Borrow `Allow`.
  - DU-012-6: aset `Drone DJI Mavic 3 {runId}`, Group `Head Office`, Custody `Available`, Allow Borrow `Deny` pada override aset.
  - DU-012-7: aset `Excavator PC200 Berjalan {runId}`, Group `Head Office`, Custody `In Borrow Process` (sudah ada di BRW lain).
  - DU-012-8: Aktor `Hendra Kusuma {runId}`, Email `hendra.kusuma{runId}@example.com`, Position `Coordinator {runId}`, Division `IT {runId}`, Home Group `Head Office`, role Asset Admin, Status `Active`, Activation Status `Activated`, Temporary User `No`, Active Borrows `0 assets`, Eligibility `Can borrow`.
  - DU-012-9: karyawan `Budi Santoso {runId}`, Email `budi.santoso{runId}@example.com`, Position `Staff {runId}`, Division `IT {runId}`, Home Group `Head Office`, Status `Active`, Activation Status `Activated`, Temporary User `No`, Active Borrows `15 assets`, Eligibility `Can borrow` di Select Borrower dari form Borrow Request (batas Max assets per borrower tercapai, tetapi dari form hanya Block new borrow when overdue yang dinilai); sebagai Borrower terpilih ia membuat aset di dialog Select Asset `Not ready` dengan alasan `Budi Santoso {runId} can borrow up to 10 assets at a time.`.
  - DU-012-10: karyawan `Budi Setiawan {runId}`, Email `budi.setiawan{runId}@example.com`, Position `Staff {runId}`, Division `Finance {runId}`, Home Group `Branch Surabaya`, Status `Active`, Activation Status `Activated`, Temporary User `No`, Active Borrows `0 assets`, Eligibility `Can borrow`.
  - DU-012-11: karyawan tanpa akun login `Joko Susilo {runId}`, Email `joko.susilo{runId}@example.com`, Position `Operator {runId}`, Division `Warehouse {runId}`, Home Group `Head Office`, Status `Active`, PIC `Rudi Hartono {runId}` (aktif), Active Borrows `0 assets`, Eligibility `Can borrow`.
  - DU-012-12: karyawan tanpa akun login `Wawan {runId}`, Email `wawan{runId}@example.com`, Position `Operator {runId}`, Division `Warehouse {runId}`, Home Group belum di-set, Status `Active`, tanpa PIC, Active Borrows `0 assets`, Eligibility `Blocked`.
  - DU-012-13: karyawan `Andi Pratama {runId}`, Email `andi.pratama{runId}@example.com`, Position `Operator {runId}`, Division `Warehouse {runId}`, Home Group `Branch Surabaya`, Status `Active`, Activation Status `Activated`, Temporary User `No`, Active Borrows `1 asset` berstatus Overdue (Due date T0 − 3 hari), Eligibility `Blocked` (Block new borrow when overdue).
  - DU-012-14: karyawan `Sari Dewi {runId}`, Email `sari.dewi{runId}@example.com`, Position `Analyst {runId}`, Division `Finance {runId}`, Home Group `Head Office`, TAG `EMP-0107 {runId}`, Status `Active`, Activation Status `Activated`, Temporary User `No`, Active Borrows `2 assets`, Eligibility `Can borrow`; keterangan dialog Select Asset bila ia Borrower terpilih adalah `Available assets in your groups. Eligibility is checked for Sari Dewi {runId}.`.
  - DU-012-15: karyawan `Rudi Hartono {runId}`, Email `rudi.hartono{runId}@example.com`, Position `Supervisor {runId}`, Division `Warehouse {runId}`, Home Group `Head Office`, TAG `EMP-0042 {runId}`, Status `Active`, Activation Status `Activated`, Temporary User `No`, Active Borrows `5 assets` (1 baris Waiting for Approval, 1 baris Waiting for Handover, dan 3 baris Borrowed; ditambah 1 baris Returned, 1 baris Canceled, 1 baris Rejected, dan 1 Draft yang tidak dihitung), Eligibility `Can borrow`.
  - DU-012-16: karyawan `Dewi Lestari {runId}`, Email `dewi.lestari{runId}@example.com`, Position `Staff {runId}`, Division `Operations {runId}`, Home Group `Branch Medan` (di luar cakupan Aktor), Status `Active`, Activation Status `Activated`, Temporary User `No`, Active Borrows `6 assets`, Eligibility `Can borrow`.
  - DU-012-17: karyawan `Tari Sementara {runId}`, Email `tari.sementara{runId}@example.com`, Position `Intern {runId}`, Division `Operations {runId}`, Home Group `Head Office`, Status `Active`, Activation Status `Activated`, Temporary User `Yes`, Temporary Until `T0 + 30 hari`, Active Borrows `0 assets`, Eligibility `Can borrow`; rentang saring Temporary Until yang hanya memuat dia adalah `T0 + 25 hari` sampai `T0 + 35 hari`.
  - DU-012-18: karyawan `Tono Sementara {runId}`, Email `tono.sementara{runId}@example.com`, Position `Intern {runId}`, Division `Operations {runId}`, Home Group `Head Office`, Status `Active`, Activation Status `Activated`, Temporary User `Yes`, Temporary Until `T0 + 60 hari`, Active Borrows `0 assets`, Eligibility `Can borrow`.
  - DU-012-19: karyawan `Lina Nonaktif {runId}`, akun Status `Inactive`.
  - DU-012-20: karyawan `Maya Belum Aktivasi {runId}`, akun Activation Status `Pending Activation`.
  - DU-012-21: karyawan `Nina Konfirmasi Email {runId}`, akun Activation Status `Pending Email Confirmation`.
  - DU-012-22: karyawan `Bambang Resign {runId}`, karyawan nonaktif (resign).
  - DU-012-23: karyawan `Rina Kedaluwarsa {runId}`, akun sementara dengan Temporary User `Yes`, Temporary Until `T0 − 1 hari` (sudah melewati batasnya), akun Status `Inactive` otomatis.
- Kondisi:
  - Max assets per borrower bernilai `10`.
  - Block new borrow when overdue bernilai ON.

## Test Steps

### Select Borrower memuat kandidat menurut status akun dan karyawan
1. Klik `[+ Borrow]`
2. Klik `[Select Borrower]`
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi baris `Budi Setiawan {runId}` tampil sebagai kandidat ber-akun login dengan Status `Active` dan Activation Status `Activated`
5. Verifikasi baris `Lina Nonaktif {runId}` (akun `Inactive`) tidak ada di dialog
6. Verifikasi baris `Maya Belum Aktivasi {runId}` (akun `Pending Activation`) tidak ada di dialog
7. Verifikasi baris `Nina Konfirmasi Email {runId}` (akun `Pending Email Confirmation`) tidak ada di dialog
8. Verifikasi baris `Rina Kedaluwarsa {runId}` (akun sementara yang sudah melewati batasnya dan otomatis `Inactive`) tidak ada di dialog
9. Verifikasi baris `Joko Susilo {runId}` (karyawan tanpa akun login dengan PIC aktif) tampil
10. Verifikasi baris `Wawan {runId}` (karyawan tanpa akun login dan tanpa PIC) tampil dengan Eligibility `Blocked`
11. Verifikasi pilihan radio pada baris `Wawan {runId}` disabled
12. Verifikasi baris `Bambang Resign {runId}` (karyawan nonaktif) tidak ada di dialog
13. Verifikasi baris `Hendra Kusuma {runId}` (Aktor sendiri) tampil dengan pilihan radio yang dapat dipilih
14. Verifikasi baris `Dewi Lestari {runId}` dengan Home Group `Branch Medan` di luar Group penugasan Aktor tampil dengan Eligibility `Can borrow` karena Home Group tidak dinilai pada Eligibility
15. Verifikasi baris `Budi Santoso {runId}` tampil dengan Eligibility `Can borrow` dan pilihan radionya dapat dipilih karena dari form Borrow Request hanya Block new borrow when overdue yang dinilai
16. Verifikasi baris `Andi Pratama {runId}` tampil dengan Eligibility `Blocked` dan pilihan radionya disabled
17. Verifikasi baris `Sari Dewi {runId}` dengan Eligibility `Can borrow` tampil walau Allowed borrower aset tidak dinilai di dialog ini

### Kolom Select Borrower menampilkan isi dari data
18. Verifikasi kolom `Name` pada baris `Budi Santoso {runId}` memuat `Budi Santoso {runId}`
19. Verifikasi kolom `Email` pada baris `Budi Santoso {runId}` memuat `budi.santoso{runId}@example.com`
20. Verifikasi kolom `Position` pada baris `Budi Santoso {runId}` memuat `Staff {runId}`
21. Verifikasi kolom `Division` pada baris `Budi Santoso {runId}` memuat `IT {runId}`
22. Verifikasi kolom `Home Group` pada baris `Budi Santoso {runId}` memuat `Head Office`
23. Verifikasi kolom `Home Group` pada baris `Wawan {runId}` memuat `—`
24. Verifikasi kolom `Status` pada baris `Budi Santoso {runId}` memuat `Active`
25. Verifikasi kolom `Active Borrows` pada baris `Budi Santoso {runId}` memuat `15 assets`
26. Verifikasi kolom `Active Borrows` pada baris `Budi Setiawan {runId}` memuat `0 assets`
27. Verifikasi kolom `Active Borrows` pada baris `Rudi Hartono {runId}` memuat `5 assets` yang dihitung dari 1 baris Waiting for Approval, 1 baris Waiting for Handover, dan 3 baris Borrowed, tanpa menghitung baris Returned, Canceled, Rejected, dan Draft
28. Verifikasi kolom `Eligibility` pada baris `Budi Setiawan {runId}` memuat `Can borrow`
29. Verifikasi kolom `Eligibility` pada baris `Joko Susilo {runId}` memuat `Can borrow`
30. Verifikasi alasan `Blocked` pada baris `Andi Pratama {runId}` tersampaikan: `Andi Pratama {runId} has an overdue borrow: [Asset Code], due [Date]. Return it first.` dengan Asset Code dan Date dari baris Overdue baris itu
31. Verifikasi alasan `Blocked` pada baris `Wawan {runId}` tersampaikan: `No login account and no PIC. Set a PIC in Users first.`

### Kolom curated Select Borrower tampil setelah diaktifkan di Setup Column
32. Buka Setup Column lewat ikon `⋯` pada header tabel
33. Aktifkan kolom `Activation Status`
34. Aktifkan kolom `Temporary User`
35. Aktifkan kolom `Temporary Until`
36. Aktifkan kolom `TAG`
37. Verifikasi kolom `Activation Status` pada baris `Budi Santoso {runId}` memuat `Activated`
38. Verifikasi kolom `Temporary User` pada baris `Tari Sementara {runId}` memuat `Yes`
39. Verifikasi kolom `Temporary User` pada baris `Budi Santoso {runId}` memuat `No`
40. Verifikasi kolom `Temporary Until` pada baris `Tari Sementara {runId}` memuat tanggal `T0 + 30 hari` menurut format General Settings
41. Verifikasi kolom `TAG` pada baris `Budi Santoso {runId}` memuat `—`
42. Verifikasi kolom `TAG` pada baris `Rudi Hartono {runId}` memuat `EMP-0042 {runId}`

### Search Select Borrower menyaring baris menurut kolom Searchable
43. Klik `(←)` pada kotak Search
44. Klik ikon Search
45. Verifikasi kotak Search yang kosong memuat placeholder `Search name or email...`
46. Ketik Search `budi.santoso{runId}@example.com`, tekan Enter
47. Verifikasi baris `Budi Santoso {runId}` tampil dan baris `Budi Setiawan {runId}` tidak tampil (pencarian pada kolom `Email`)
48. Ganti isi kotak search dengan `Analyst {runId}`, tekan Enter
49. Verifikasi baris `Sari Dewi {runId}` tampil dan baris `Budi Santoso {runId}` tidak tampil (pencarian pada kolom `Position`)
50. Ganti isi kotak search dengan `Operations {runId}`, tekan Enter
51. Verifikasi baris `Dewi Lestari {runId}` tampil dan baris `Budi Santoso {runId}` tidak tampil (pencarian pada kolom `Division`)
52. Ganti isi kotak search dengan `Branch Medan`, tekan Enter
53. Verifikasi baris `Dewi Lestari {runId}` tampil (pencarian pada kolom `Home Group`)
54. Ganti isi kotak search dengan `15 assets`, tekan Enter
55. Verifikasi baris `Budi Santoso {runId}` tampil (pencarian pada kolom `Active Borrows`)
56. Ganti isi kotak search dengan `Blocked`, tekan Enter
57. Verifikasi baris `Wawan {runId}` tampil (pencarian pada kolom `Eligibility`)
58. Ganti isi kotak search dengan `Yes`, tekan Enter
59. Verifikasi baris `Tari Sementara {runId}` tampil (pencarian pada kolom `Temporary User`)
60. Ganti isi kotak search dengan `Active`, tekan Enter
61. Verifikasi baris `Budi Santoso {runId}` tampil (pencarian pada kolom `Status`)
62. Ganti isi kotak search dengan `Activated`, tekan Enter
63. Verifikasi baris `Budi Santoso {runId}` tampil (pencarian pada kolom `Activation Status`)
64. Ganti isi kotak search dengan `EMP-0042 {runId}`, tekan Enter
65. Verifikasi baris `Rudi Hartono {runId}` tampil dan baris `Sari Dewi {runId}` tidak tampil (pencarian pada kolom `TAG`)
66. Ganti isi kotak search dengan `Budi Santoso {runId}`, tekan Enter
67. Verifikasi baris `Budi Santoso {runId}` tampil dan baris `Sari Dewi {runId}` tidak tampil (pencarian pada kolom `Name`)
68. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Sort Select Borrower mengurutkan baris menurut kolom
69. Verifikasi baris `Andi Pratama {runId}` tampil di atas `Budi Santoso {runId}`, `Budi Santoso {runId}` di atas `Budi Setiawan {runId}`, dan `Budi Setiawan {runId}` di atas `Sari Dewi {runId}` menurut urutan bawaan kolom `Name` dari A ke Z
70. Klik header kolom `Email`
71. Verifikasi baris `Andi Pratama {runId}` tampil di atas `Sari Dewi {runId}` menurut `Email` dari A ke Z
72. Klik header kolom `Position`
73. Verifikasi baris `Sari Dewi {runId}` tampil di atas `Rudi Hartono {runId}` menurut `Position` dari A ke Z
74. Klik header kolom `Division`
75. Verifikasi baris `Sari Dewi {runId}` tampil di atas `Dewi Lestari {runId}` menurut `Division` dari A ke Z
76. Klik header kolom `Home Group`
77. Verifikasi baris `Budi Setiawan {runId}` (Home Group `Branch Surabaya`) tampil di atas `Budi Santoso {runId}` (Home Group `Head Office`) menurut `Home Group` dari A ke Z
78. Klik header kolom `Status`
79. Verifikasi baris tersusun menurut kolom `Status` tanpa mengubah himpunan baris yang tampil
80. Klik header kolom `Active Borrows`
81. Verifikasi baris `Andi Pratama {runId}` (`1 asset`) tampil di atas `Sari Dewi {runId}` (`2 assets`), `Sari Dewi {runId}` di atas `Rudi Hartono {runId}` (`5 assets`), dan `Rudi Hartono {runId}` di atas `Budi Santoso {runId}` (`15 assets`) menurut `Active Borrows` secara numerik
82. Klik header kolom `Eligibility`
83. Verifikasi baris `Andi Pratama {runId}` (`Blocked`) tampil di atas `Sari Dewi {runId}` (`Can borrow`) menurut `Eligibility` dari A ke Z
84. Klik header kolom `Activation Status`
85. Verifikasi baris tersusun menurut kolom `Activation Status` tanpa mengubah himpunan baris yang tampil
86. Klik header kolom `Temporary User`
87. Verifikasi baris `Sari Dewi {runId}` (`No`) tampil di atas `Tari Sementara {runId}` (`Yes`) menurut `Temporary User` dari A ke Z
88. Klik header kolom `Temporary Until`
89. Verifikasi baris `Tono Sementara {runId}` (`T0 + 60 hari`) tampil di atas `Tari Sementara {runId}` (`T0 + 30 hari`) menurut `Temporary Until` dari terbaru ke terlama
90. Klik header kolom `Temporary Until`
91. Verifikasi baris `Tari Sementara {runId}` (`T0 + 30 hari`) tampil di atas `Tono Sementara {runId}` (`T0 + 60 hari`) menurut `Temporary Until` dari terlama ke terbaru
92. Klik header kolom `TAG`
93. Verifikasi baris `Rudi Hartono {runId}` (`EMP-0042 {runId}`) tampil di atas `Sari Dewi {runId}` (`EMP-0107 {runId}`) menurut `TAG` dari A ke Z

### Filter Select Borrower menyaring baris menurut kolom Filterable
94. Klik ikon Filter
95. Verifikasi field `Name` memuat placeholder `All users`
96. Verifikasi field `Position` memuat placeholder `All positions`
97. Verifikasi field `Division` memuat placeholder `All divisions`
98. Verifikasi field `Home Group` memuat placeholder `All home groups`
99. Verifikasi field `Active Borrows` memuat placeholder `Min` dan `Max`
100. Verifikasi field `Eligibility` memuat placeholder `All eligibility`
101. Verifikasi field `Activation Status` memuat placeholder `All activation statuses`
102. Verifikasi field `Temporary User` memuat placeholder `All temporary users`
103. Verifikasi field `Temporary Until` memuat placeholder `Select date`
104. Verifikasi Filter Panel tidak memuat field `Email`, `Status`, dan `TAG`
105. Pilih opsi `Sari Dewi {runId}` pada filter `Name`
106. Klik `[Apply]`
107. Verifikasi baris `Sari Dewi {runId}` tampil dan baris `Budi Santoso {runId}` tidak tampil
108. Klik `[Clear Field]`
109. Klik `[Apply]`
110. Pilih opsi `Analyst {runId}` dan `Staff {runId}` pada filter `Position`
111. Verifikasi `Analyst {runId}` dan `Staff {runId}` terpilih bersamaan pada filter `Position`
112. Ketik `Analyst {runId}` pada pencarian opsi filter `Position`
113. Verifikasi opsi `Analyst {runId}` tampil dan opsi `Staff {runId}` tidak tampil pada daftar opsi filter `Position`
114. Klik `[Clear Field]`
115. Pilih opsi `Analyst {runId}` pada filter `Position`
116. Klik `[Apply]`
117. Verifikasi baris `Sari Dewi {runId}` tampil dan baris `Budi Santoso {runId}` tidak tampil
118. Klik `[Clear Field]`
119. Klik `[Apply]`
120. Pilih opsi `IT {runId}` dan `Finance {runId}` pada filter `Division`
121. Verifikasi `IT {runId}` dan `Finance {runId}` terpilih bersamaan pada filter `Division`
122. Ketik `Finance {runId}` pada pencarian opsi filter `Division`
123. Verifikasi opsi `Finance {runId}` tampil dan opsi `IT {runId}` tidak tampil pada daftar opsi filter `Division`
124. Klik `[Clear Field]`
125. Pilih opsi `Warehouse {runId}` pada filter `Division`
126. Klik `[Apply]`
127. Verifikasi baris `Joko Susilo {runId}` dan baris `Rudi Hartono {runId}` tampil dan baris `Sari Dewi {runId}` tidak tampil
128. Klik `[Clear Field]`
129. Klik `[Apply]`
130. Pilih opsi `Head Office` dan `Branch Medan` pada filter `Home Group`
131. Verifikasi `Head Office` dan `Branch Medan` terpilih bersamaan pada filter `Home Group`
132. Ketik `Branch Medan` pada pencarian opsi filter `Home Group`
133. Verifikasi opsi `Branch Medan` tampil dan opsi `Head Office` tidak tampil pada daftar opsi filter `Home Group`
134. Klik `[Clear Field]`
135. Pilih opsi `Branch Medan` pada filter `Home Group`
136. Klik `[Apply]`
137. Verifikasi baris `Dewi Lestari {runId}` tampil dan baris `Sari Dewi {runId}` tidak tampil
138. Klik `[Clear Field]`
139. Klik `[Apply]`
140. Isi field `Active Borrows` Min `1` dan Max `5`
141. Klik `[Apply]`
142. Verifikasi baris `Andi Pratama {runId}`, `Sari Dewi {runId}`, dan `Rudi Hartono {runId}` tampil serta baris `Budi Santoso {runId}` dan `Dewi Lestari {runId}` tidak tampil (batas Min dan Max inklusif)
143. Klik `[Clear Field]`
144. Klik `[Apply]`
145. Pilih opsi `Can borrow` dan `Blocked` pada filter `Eligibility`
146. Verifikasi `Can borrow` dan `Blocked` terpilih bersamaan pada filter `Eligibility`
147. Ketik `Blocked` pada pencarian opsi filter `Eligibility`
148. Verifikasi opsi `Blocked` tampil dan opsi `Can borrow` tidak tampil pada daftar opsi filter `Eligibility`
149. Klik `[Clear Field]`
150. Pilih opsi `Blocked` pada filter `Eligibility`
151. Klik `[Apply]`
152. Verifikasi baris `Wawan {runId}` dan `Andi Pratama {runId}` tampil dan baris `Sari Dewi {runId}` dan `Budi Santoso {runId}` tidak tampil
153. Klik `[Clear Field]`
154. Klik `[Apply]`
155. Pilih opsi `Activated` dan `Pending Activation` pada filter `Activation Status`
156. Verifikasi `Activated` dan `Pending Activation` terpilih bersamaan pada filter `Activation Status`
157. Ketik `Pending Activation` pada pencarian opsi filter `Activation Status`
158. Verifikasi opsi `Pending Activation` tampil dan opsi `Activated` tidak tampil pada daftar opsi filter `Activation Status`
159. Klik `[Clear Field]`
160. Pilih opsi `Activated` pada filter `Activation Status`
161. Klik `[Apply]`
162. Verifikasi baris `Sari Dewi {runId}` tetap tampil dan baris `Joko Susilo {runId}` (tanpa akun login) tidak tampil
163. Klik `[Clear Field]`
164. Klik `[Apply]`
165. Pilih opsi `Yes` pada filter `Temporary User`
166. Klik `[Apply]`
167. Verifikasi baris `Tari Sementara {runId}` dan baris `Tono Sementara {runId}` tampil dan baris `Sari Dewi {runId}` tidak tampil
168. Klik `[Clear Field]`
169. Klik `[Apply]`
170. Pilih rentang `T0 + 25 hari` sampai `T0 + 35 hari` pada filter `Temporary Until`
171. Klik `[Apply]`
172. Verifikasi baris `Tari Sementara {runId}` tampil dan baris `Tono Sementara {runId}` tidak tampil
173. Klik `[Clear Field]`
174. Klik `[Apply]`
175. Klik ikon Filter
176. Klik `[Cancel]` pada dialog Select Borrower

### Select Asset sebelum Borrower dipilih memuat aset dalam cakupan Group
177. Klik `[+ Asset]`
178. Ketik Search `{runId}`, tekan Enter
179. Verifikasi baris `Laptop Dell Latitude {runId}` tampil di dialog Select Asset
180. Verifikasi baris `Toyota Avanza {runId}` dari Group `Branch Surabaya` tampil di dialog Select Asset
181. Verifikasi baris `Printer Canon {runId}` dari Group `Branch Medan` di luar cakupan Aktor tidak dimuat
182. Verifikasi baris `Drone DJI Mavic 3 {runId}` (Allow Borrow `Deny`) tidak dimuat
183. Verifikasi baris `Excavator PC200 Berjalan {runId}` (Custody `In Borrow Process`) tidak dimuat
184. Verifikasi keterangan di bawah judul dialog adalah `Available assets in your groups.` tanpa kalimat kedua karena Borrower belum dipilih
185. Verifikasi kolom `Eligibility` pada baris `Toyota Avanza {runId}` memuat `Ready` karena Borrower belum dipilih
186. Verifikasi kolom `Eligibility` pada baris `Laptop Dell Latitude {runId}` memuat `Ready`
187. Verifikasi dialog memuat tombol `[Cancel]` dan `[Select]` di footer
188. Verifikasi toolbar dialog memuat tombol `Search by Scan`, ikon Search, dan ikon Filter

### Kolom Select Asset menampilkan isi dari data
189. Verifikasi kolom `Photo` pada baris `Laptop Dell Latitude {runId}` memuat foto utama `laptop-dell-latitude.png`
190. Verifikasi kolom `Photo` pada baris `Projector Epson EB-X06 {runId}` tampil tanpa foto utama aset
191. Verifikasi kolom `Name` pada baris `Laptop Dell Latitude {runId}` memuat nama aset `Laptop Dell Latitude {runId}`
192. Verifikasi kolom `Asset ID` pada baris `Laptop Dell Latitude {runId}` terisi Asset ID milik DU-012-1
193. Verifikasi kolom `Brand` pada baris `Laptop Dell Latitude {runId}` memuat `Dell {runId}`
194. Verifikasi kolom `Model/Type` pada baris `Laptop Dell Latitude {runId}` memuat `Latitude 5420 {runId}`
195. Verifikasi kolom `Group` pada baris `Laptop Dell Latitude {runId}` memuat `Head Office`
196. Verifikasi kolom `Group` pada baris `Toyota Avanza {runId}` memuat `Branch Surabaya`
197. Verifikasi kolom `Max Duration` pada baris `Laptop Dell Latitude {runId}` memuat `3 days`
198. Verifikasi kolom `Max Duration` pada baris `Toyota Avanza {runId}` memuat `14 days`
199. Verifikasi kolom `Approval` pada baris `Laptop Dell Latitude {runId}` memuat `Auto (≤ 3 days)`
200. Verifikasi kolom `Approval` pada baris `Projector Epson EB-X06 {runId}` memuat `Needs approval`
201. Verifikasi kolom `Approval` pada baris `Excavator PC200 {runId}` memuat `Needs approval (all must approve)`

### Kolom curated Select Asset tampil setelah diaktifkan di Setup Column
202. Buka Setup Column lewat ikon `⋯` pada header tabel
203. Aktifkan kolom `TAG`
204. Aktifkan kolom `Category`
205. Aktifkan kolom `Label`
206. Verifikasi kolom `TAG` pada baris `Laptop Dell Latitude {runId}` memuat `NFC`
207. Verifikasi kolom `TAG` pada baris `Toyota Avanza {runId}` memuat `—` karena aset `Non TAG`
208. Verifikasi kolom `Category` pada baris `Laptop Dell Latitude {runId}` memuat `Laptop {runId}`
209. Verifikasi kolom `Label` pada baris `Laptop Dell Latitude {runId}` memuat `Operasional {runId}`
210. Verifikasi kolom `Label` pada baris `Projector Epson EB-X06 {runId}` memuat `—`

### Search Select Asset menyaring baris menurut kolom Searchable
211. Klik `(←)` pada kotak Search
212. Klik ikon Search
213. Verifikasi kotak Search yang kosong memuat placeholder `Search asset name or ID...`
214. Ketik Search `Laptop Dell Latitude {runId}`, tekan Enter
215. Verifikasi baris `Laptop Dell Latitude {runId}` tampil dan baris `Projector Epson EB-X06 {runId}` tidak tampil (pencarian pada kolom `Name`)
216. Ganti isi kotak search dengan `Dell {runId}`, tekan Enter
217. Verifikasi baris `Laptop Dell Latitude {runId}` tampil dan baris `Projector Epson EB-X06 {runId}` tidak tampil (pencarian pada kolom `Brand`)
218. Ganti isi kotak search dengan `Latitude 5420 {runId}`, tekan Enter
219. Verifikasi baris `Laptop Dell Latitude {runId}` tampil dan baris `Projector Epson EB-X06 {runId}` tidak tampil (pencarian pada kolom `Model/Type`)
220. Ketik Search dengan Asset ID milik DU-012-1, tekan Enter
221. Verifikasi baris `Laptop Dell Latitude {runId}` tampil dan baris `Projector Epson EB-X06 {runId}` tidak tampil (pencarian pada kolom `Asset ID`)
222. Ganti isi kotak search dengan `Branch Surabaya`, tekan Enter
223. Verifikasi baris `Toyota Avanza {runId}` tampil (pencarian pada kolom `Group`)
224. Ganti isi kotak search dengan `NFC`, tekan Enter
225. Verifikasi baris `Laptop Dell Latitude {runId}` tampil (pencarian pada kolom `TAG`)
226. Ganti isi kotak search dengan `Heavy Equipment {runId}`, tekan Enter
227. Verifikasi baris `Excavator PC200 {runId}` tampil dan baris `Laptop Dell Latitude {runId}` tidak tampil (pencarian pada kolom `Category`)
228. Ganti isi kotak search dengan `14 days`, tekan Enter
229. Verifikasi baris `Toyota Avanza {runId}` tampil (pencarian pada kolom `Max Duration`)
230. Ganti isi kotak search dengan `Needs approval (all must approve)`, tekan Enter
231. Verifikasi baris `Excavator PC200 {runId}` tampil (pencarian pada kolom `Approval`)
232. Ganti isi kotak search dengan `Rapat {runId}`, tekan Enter
233. Verifikasi baris `Toyota Avanza {runId}` tampil dan baris `Laptop Dell Latitude {runId}` tidak tampil (pencarian pada kolom `Label`)
234. Ganti isi kotak search dengan `Ready`, tekan Enter
235. Verifikasi baris `Laptop Dell Latitude {runId}` tampil (pencarian pada kolom `Eligibility`)
236. Ganti isi kotak search dengan `{runId}`, tekan Enter
237. Verifikasi baris `Laptop Dell Latitude {runId}`, `Projector Epson EB-X06 {runId}`, `Excavator PC200 {runId}`, dan `Toyota Avanza {runId}` tampil sebelum diurutkan

### Sort Select Asset mengurutkan baris menurut kolom
238. Verifikasi baris `Excavator PC200 {runId}` tampil di atas `Laptop Dell Latitude {runId}`, `Laptop Dell Latitude {runId}` di atas `Projector Epson EB-X06 {runId}`, dan `Projector Epson EB-X06 {runId}` di atas `Toyota Avanza {runId}` menurut urutan bawaan kolom `Name` dari A ke Z
239. Klik header kolom `Asset ID`
240. Verifikasi baris `Laptop Dell Latitude {runId}` tampil di atas `Projector Epson EB-X06 {runId}`, `Projector Epson EB-X06 {runId}` di atas `Excavator PC200 {runId}`, dan `Excavator PC200 {runId}` di atas `Toyota Avanza {runId}` menurut `Asset ID` dari A ke Z, karena DU-012-1 dibuat lebih dulu daripada DU-012-2, DU-012-2 lebih dulu daripada DU-012-3, dan DU-012-3 lebih dulu daripada DU-012-4
241. Klik header kolom `Brand`
242. Verifikasi baris `Laptop Dell Latitude {runId}` (`Dell {runId}`) tampil di atas `Projector Epson EB-X06 {runId}` (`Epson {runId}`), `Projector Epson EB-X06 {runId}` di atas `Excavator PC200 {runId}` (`Komatsu {runId}`), dan `Excavator PC200 {runId}` di atas `Toyota Avanza {runId}` (`Toyota {runId}`) menurut `Brand` dari A ke Z
243. Klik header kolom `Model/Type`
244. Verifikasi baris `Toyota Avanza {runId}` (`Avanza {runId}`) tampil di atas `Projector Epson EB-X06 {runId}` (`EB-X06 {runId}`), `Projector Epson EB-X06 {runId}` di atas `Laptop Dell Latitude {runId}` (`Latitude 5420 {runId}`), dan `Laptop Dell Latitude {runId}` di atas `Excavator PC200 {runId}` (`PC200 {runId}`) menurut `Model/Type` dari A ke Z
245. Klik header kolom `Group`
246. Verifikasi baris `Toyota Avanza {runId}` (`Branch Surabaya`) tampil di atas `Laptop Dell Latitude {runId}` (`Head Office`) menurut `Group` dari A ke Z
247. Klik header kolom `TAG`
248. Verifikasi baris `Laptop Dell Latitude {runId}` (`NFC`) tampil di atas `Projector Epson EB-X06 {runId}` (`QR`) dan `Projector Epson EB-X06 {runId}` di atas `Excavator PC200 {runId}` (`RFID`) menurut label ikon `TAG` secara alfabetis
249. Klik header kolom `Category`
250. Verifikasi baris `Toyota Avanza {runId}` (`Car {runId}`) tampil di atas `Excavator PC200 {runId}` (`Heavy Equipment {runId}`), `Excavator PC200 {runId}` di atas `Laptop Dell Latitude {runId}` (`Laptop {runId}`), dan `Laptop Dell Latitude {runId}` di atas `Projector Epson EB-X06 {runId}` (`Projector {runId}`) menurut `Category` dari A ke Z
251. Klik header kolom `Max Duration`
252. Verifikasi baris `Laptop Dell Latitude {runId}` (`3 days`) tampil di atas `Projector Epson EB-X06 {runId}` (`5 days`), `Projector Epson EB-X06 {runId}` di atas `Excavator PC200 {runId}` (`7 days`), dan `Excavator PC200 {runId}` di atas `Toyota Avanza {runId}` (`14 days`) menurut `Max Duration` secara numerik
253. Klik header kolom `Approval`
254. Verifikasi baris `Laptop Dell Latitude {runId}` (`Auto (≤ 3 days)`) tampil di atas `Projector Epson EB-X06 {runId}` (`Needs approval`) menurut `Approval` dari A ke Z
255. Klik header kolom `Label`
256. Verifikasi baris `Excavator PC200 {runId}` (`Event {runId}`) tampil di atas `Laptop Dell Latitude {runId}` (`Operasional {runId}`) dan `Laptop Dell Latitude {runId}` di atas `Toyota Avanza {runId}` (`Rapat {runId}`) menurut `Label` dari A ke Z
257. Klik header kolom `Photo`
258. Verifikasi baris `Excavator PC200 {runId}` tampil di atas `Laptop Dell Latitude {runId}` dan `Laptop Dell Latitude {runId}` di atas `Toyota Avanza {runId}` tetap menurut `Label`, karena kolom `Photo` tidak bisa diurutkan

### Filter Select Asset menyaring baris menurut kolom Filterable
259. Klik ikon Filter
260. Verifikasi field `Asset Name` memuat placeholder `All asset names`
261. Verifikasi field `Brand` memuat placeholder `All brands`
262. Verifikasi field `Model/Type` memuat placeholder `All models`
263. Verifikasi field `Group` memuat placeholder `All groups`
264. Verifikasi field `TAG` memuat placeholder `All tags`
265. Verifikasi field `Category` memuat placeholder `All categories`
266. Verifikasi field `Approval` memuat placeholder `All approvals`
267. Verifikasi field `Label` memuat placeholder `All labels`
268. Verifikasi field `Eligibility` memuat placeholder `All eligibility`
269. Verifikasi Filter Panel tidak memuat field `Photo`, `Asset ID`, dan `Max Duration`
270. Pilih opsi `Laptop Dell Latitude {runId}` pada filter `Asset Name`
271. Klik `[Apply]`
272. Verifikasi baris `Laptop Dell Latitude {runId}` tampil dan baris `Projector Epson EB-X06 {runId}` tidak tampil
273. Klik `[Clear Field]`
274. Klik `[Apply]`
275. Pilih opsi `Epson {runId}` pada filter `Brand`
276. Klik `[Apply]`
277. Verifikasi baris `Projector Epson EB-X06 {runId}` tampil dan baris `Laptop Dell Latitude {runId}` tidak tampil
278. Klik `[Clear Field]`
279. Klik `[Apply]`
280. Pilih opsi `PC200 {runId}` pada filter `Model/Type`
281. Klik `[Apply]`
282. Verifikasi baris `Excavator PC200 {runId}` tampil dan baris `Laptop Dell Latitude {runId}` tidak tampil
283. Klik `[Clear Field]`
284. Klik `[Apply]`
285. Pilih node `Branch Surabaya` pada filter `Group`
286. Klik `[Apply]`
287. Verifikasi baris `Toyota Avanza {runId}` tampil dan baris `Laptop Dell Latitude {runId}` tidak tampil
288. Klik `[Clear Field]`
289. Klik `[Apply]`
290. Pilih opsi `RFID` pada filter `TAG`
291. Klik `[Apply]`
292. Verifikasi baris `Excavator PC200 {runId}` tampil dan baris `Laptop Dell Latitude {runId}` tidak tampil
293. Klik `[Clear Field]`
294. Klik `[Apply]`
295. Pilih node `Laptop {runId}` pada filter `Category`
296. Klik `[Apply]`
297. Verifikasi baris `Laptop Dell Latitude {runId}` tampil dan baris `Projector Epson EB-X06 {runId}` tidak tampil
298. Klik `[Clear Field]`
299. Klik `[Apply]`
300. Pilih opsi `Needs approval (all must approve)` pada filter `Approval`
301. Klik `[Apply]`
302. Verifikasi baris `Excavator PC200 {runId}` tampil dan baris `Laptop Dell Latitude {runId}` tidak tampil
303. Klik `[Clear Field]`
304. Klik `[Apply]`
305. Pilih opsi `Operasional {runId}` pada filter `Label`
306. Klik `[Apply]`
307. Verifikasi baris `Laptop Dell Latitude {runId}` tampil dan baris `Excavator PC200 {runId}` tidak tampil
308. Klik `[Clear Field]`
309. Klik `[Apply]`
310. Pilih opsi `Ready` pada filter `Eligibility`
311. Klik `[Apply]`
312. Verifikasi baris `Laptop Dell Latitude {runId}` tampil
313. Klik `[Clear Field]`
314. Klik `[Apply]`
315. Klik ikon Filter
316. Klik `[Cancel]` pada dialog Select Asset

### Select Asset menilai kelayakan menurut Borrower yang dipilih
317. Klik `[Select Borrower]`
318. Ketik Search `Sari Dewi {runId}`, tekan Enter
319. Pilih baris `Sari Dewi {runId}`
320. Klik `[Select]`
321. Klik `[+ Asset]`
322. Ketik Search `{runId}`, tekan Enter
323. Verifikasi keterangan di bawah judul dialog adalah `Available assets in your groups. Eligibility is checked for Sari Dewi {runId}.`
324. Verifikasi kolom `Eligibility` pada baris `Laptop Dell Latitude {runId}` memuat `Ready` dan checkbox baris dapat dicentang
325. Verifikasi kolom `Eligibility` pada baris `Toyota Avanza {runId}` memuat `Not ready` dan checkbox baris disabled
326. Verifikasi alasan `Not ready` pada baris `Toyota Avanza {runId}` tersampaikan: `Sari Dewi {runId} can't borrow assets from Branch Surabaya.`
327. Klik header kolom `Eligibility`
328. Verifikasi baris `Toyota Avanza {runId}` (`Not ready`) tampil di atas `Laptop Dell Latitude {runId}` (`Ready`) menurut `Eligibility` dari A ke Z

### Select Asset menilai batas Max assets per borrower
329. Klik `[Cancel]` pada dialog Select Asset
330. Klik nama Borrower `Sari Dewi {runId}` pada field Borrower
331. Ketik Search `Budi Santoso {runId}`, tekan Enter
332. Pilih baris `Budi Santoso {runId}`
333. Klik `[Select]`
334. Klik `[+ Asset]`
335. Ketik Search `Laptop Dell Latitude {runId}`, tekan Enter
336. Verifikasi kolom `Eligibility` pada baris `Laptop Dell Latitude {runId}` memuat `Not ready` dan checkbox baris disabled karena batas Max assets per borrower tercapai
337. Verifikasi alasan `Not ready` pada baris `Laptop Dell Latitude {runId}` tersampaikan: `Budi Santoso {runId} can borrow up to 10 assets at a time.`
338. Klik `[Cancel]` pada dialog Select Asset

### Aset dari Group berbeda dapat dipilih bersama
339. Klik nama Borrower `Budi Santoso {runId}` pada field Borrower
340. Ketik Search `Budi Setiawan {runId}`, tekan Enter
341. Pilih baris `Budi Setiawan {runId}`
342. Klik `[Select]`
343. Klik `[+ Asset]`
344. Ketik Search `{runId}`, tekan Enter
345. Centang baris `Laptop Dell Latitude {runId}`
346. Centang baris `Toyota Avanza {runId}`
347. Klik `[Select]`
348. Verifikasi baris `Laptop Dell Latitude {runId}` dari Group `Head Office` dan baris `Toyota Avanza {runId}` dari Group `Branch Surabaya` tampil bersama di daftar aset form Borrow Request

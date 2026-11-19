---
id: TC-FA-BORROW-E2E-012-form-pilih-borrower-dan-aset
title: "Pemilihan Borrower dan aset di form Borrow Request menampilkan opsi menurut kelayakan dan cakupan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1d#p1", "§4.1d#b1", "§4.1d#b2", "§4.1d#b5", "§4.1d#b6", "§4.1d#p4", "§4.1d#r5", "§4.1d#r6", "§4.1d#r7", "§4.1d#r8", "§4.1d#r9", "§4.1d#r10", "§4.1d#r11", "§4.1d#r12", "§4.1d#r13", "§4.1d#r14", "§4.1d#r15", "§4.1d#r16", "§4.1e#p1", "§4.1e#b1", "§4.1e#b2", "§4.1e#b3", "§4.1e#b4", "§4.1e#b5", "§4.1e#r1", "§4.1e#r2", "§4.1e#r3", "§4.1e#r4", "§4.1e#r5", "§4.1e#r6", "§4.1e#r7", "§4.1e#r8", "§4.1e#r9", "§4.1e#r10", "§4.1e#r11", "§4.1e#r12"]
smoke: []
dependsOn: []
trace:
  "§4.1d#p1": [184, 185, 186, 187, 188, 192, 193]
  "§4.1d#b1": [189, 193, 370]
  "§4.1d#b2": [190, 371, 372, 373, 390]
  "§4.1d#b5": 188
  "§4.1d#b6": [372, 390, 391]
  "§4.1d#p4": [372, 373]
  "§4.1d#r5": [194, 195, 269, 280]
  "§4.1d#r6": [196, 218, 220, 242, 244, 247, 271, 282, 284, 288]
  "§4.1d#r7": [197, 226, 249, 280]
  "§4.1d#r8": [198, 222, 251, 272, 292, 294, 298]
  "§4.1d#r9": [199, 224, 253, 273, 302, 304, 308]
  "§4.1d#r10": [200, 201, 228, 255, 274, 312, 316, 402]
  "§4.1d#r11": [211, 212, 230, 257, 275, 320, 322, 326]
  "§4.1d#r12": [213, 232, 259, 276, 330, 334]
  "§4.1d#r13": [202, 203, 234, 261, 280]
  "§4.1d#r14": [204, 205, 206, 236, 263, 277, 338, 340, 344]
  "§4.1d#r15": [214, 215, 238, 265, 267, 278, 348, 350, 354]
  "§4.1d#r16": [191, 240, 279, 359, 371, 372, 373, 375, 378, 380, 390, 391]
  "§4.1e#p1": [4, 9, 14]
  "§4.1e#b1": [4, 5, 6, 7, 8]
  "§4.1e#b2": [9, 10]
  "§4.1e#b3": 12
  "§4.1e#b4": 13
  "§4.1e#b5": [10, 11, 15, 16, 17]
  "§4.1e#r1": [18, 45, 67, 69, 95, 106, 108, 112]
  "§4.1e#r2": [19, 47, 71, 104]
  "§4.1e#r3": [20, 49, 73, 96, 116, 118, 122]
  "§4.1e#r4": [21, 51, 75, 97, 126, 128, 132]
  "§4.1e#r5": [14, 22, 23, 53, 77, 98, 136, 138, 142]
  "§4.1e#r6": [24, 61, 79, 104]
  "§4.1e#r7": [25, 26, 27, 55, 81, 99, 147]
  "§4.1e#r8": [28, 29, 30, 31, 57, 83, 100, 151, 153, 157]
  "§4.1e#r9": [37, 63, 85, 101, 161, 163, 167]
  "§4.1e#r10": [38, 39, 59, 87, 102, 172]
  "§4.1e#r11": [40, 89, 91, 103, 177]
  "§4.1e#r12": [41, 42, 65, 93, 104]
anchor: [246]
coverage:
  web: automated
---

# Pemilihan Borrower dan aset di form Borrow Request menampilkan opsi menurut kelayakan dan cakupan

## Prerequisites
- Aktor: Asset Admin `Hendra Kusuma {runId}` (Aktor Borrow) dengan Group penugasan `Head Office` dan `Branch Surabaya`.
- Layar awal: Transactions > Borrow.
- Data:
  - DU-012-1: aset `Laptop Dell Latitude {runId}`, Brand `Dell {runId}`, Model/Type `Latitude 5420 {runId}`, Group `Head Office`, TAG `NFC` dengan kode tag `NFC-0001 {runId}`, Alias `Dell Kantor {runId}`, Category `Laptop {runId}`, Label `Event {runId}`, Label kedua `Operasional {runId}`, Custody `Available`, Max Duration `3 days`, Approval `Auto (≤ 3 days)`, Allowed borrower `Employee in any Group`, foto utama `laptop-dell-latitude.png`.
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
89. Verifikasi baris `Tari Sementara {runId}` (`T0 + 30 hari`) tampil di atas `Tono Sementara {runId}` (`T0 + 60 hari`) menurut `Temporary Until` dari terlama ke terbaru
90. Klik header kolom `Temporary Until`
91. Verifikasi baris `Tono Sementara {runId}` (`T0 + 60 hari`) tampil di atas `Tari Sementara {runId}` (`T0 + 30 hari`) menurut `Temporary Until` dari terbaru ke terlama
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
105. Pilih opsi `Sari Dewi {runId}` dan `Budi Santoso {runId}` pada filter `Name`
106. Verifikasi `Sari Dewi {runId}` dan `Budi Santoso {runId}` terpilih bersamaan pada filter `Name`
107. Ketik `Sari Dewi {runId}` pada pencarian opsi filter `Name`
108. Verifikasi opsi `Sari Dewi {runId}` tampil dan opsi `Budi Santoso {runId}` tidak tampil pada daftar opsi filter `Name`
109. Klik `[Clear Field]`
110. Pilih opsi `Sari Dewi {runId}` pada filter `Name`
111. Klik `[Apply]`
112. Verifikasi baris `Sari Dewi {runId}` tampil dan baris `Budi Santoso {runId}` tidak tampil
113. Klik `[Clear Field]`
114. Klik `[Apply]`
115. Pilih opsi `Analyst {runId}` dan `Staff {runId}` pada filter `Position`
116. Verifikasi `Analyst {runId}` dan `Staff {runId}` terpilih bersamaan pada filter `Position`
117. Ketik `Analyst {runId}` pada pencarian opsi filter `Position`
118. Verifikasi opsi `Analyst {runId}` tampil dan opsi `Staff {runId}` tidak tampil pada daftar opsi filter `Position`
119. Klik `[Clear Field]`
120. Pilih opsi `Analyst {runId}` pada filter `Position`
121. Klik `[Apply]`
122. Verifikasi baris `Sari Dewi {runId}` tampil dan baris `Budi Santoso {runId}` tidak tampil
123. Klik `[Clear Field]`
124. Klik `[Apply]`
125. Pilih opsi `IT {runId}` dan `Finance {runId}` pada filter `Division`
126. Verifikasi `IT {runId}` dan `Finance {runId}` terpilih bersamaan pada filter `Division`
127. Ketik `Finance {runId}` pada pencarian opsi filter `Division`
128. Verifikasi opsi `Finance {runId}` tampil dan opsi `IT {runId}` tidak tampil pada daftar opsi filter `Division`
129. Klik `[Clear Field]`
130. Pilih opsi `Warehouse {runId}` pada filter `Division`
131. Klik `[Apply]`
132. Verifikasi baris `Joko Susilo {runId}` dan baris `Rudi Hartono {runId}` tampil dan baris `Sari Dewi {runId}` tidak tampil
133. Klik `[Clear Field]`
134. Klik `[Apply]`
135. Pilih opsi `Head Office` dan `Branch Medan` pada filter `Home Group`
136. Verifikasi `Head Office` dan `Branch Medan` terpilih bersamaan pada filter `Home Group`
137. Ketik `Branch Medan` pada pencarian opsi filter `Home Group`
138. Verifikasi opsi `Branch Medan` tampil dan opsi `Head Office` tidak tampil pada daftar opsi filter `Home Group`
139. Klik `[Clear Field]`
140. Pilih opsi `Branch Medan` pada filter `Home Group`
141. Klik `[Apply]`
142. Verifikasi baris `Dewi Lestari {runId}` tampil dan baris `Sari Dewi {runId}` tidak tampil
143. Klik `[Clear Field]`
144. Klik `[Apply]`
145. Isi field `Active Borrows` Min `1` dan Max `5`
146. Klik `[Apply]`
147. Verifikasi baris `Andi Pratama {runId}`, `Sari Dewi {runId}`, dan `Rudi Hartono {runId}` tampil serta baris `Budi Santoso {runId}` dan `Dewi Lestari {runId}` tidak tampil (batas Min dan Max inklusif)
148. Klik `[Clear Field]`
149. Klik `[Apply]`
150. Pilih opsi `Can borrow` dan `Blocked` pada filter `Eligibility`
151. Verifikasi `Can borrow` dan `Blocked` terpilih bersamaan pada filter `Eligibility`
152. Ketik `Blocked` pada pencarian opsi filter `Eligibility`
153. Verifikasi opsi `Blocked` tampil dan opsi `Can borrow` tidak tampil pada daftar opsi filter `Eligibility`
154. Klik `[Clear Field]`
155. Pilih opsi `Blocked` pada filter `Eligibility`
156. Klik `[Apply]`
157. Verifikasi baris `Wawan {runId}` dan `Andi Pratama {runId}` tampil dan baris `Sari Dewi {runId}` dan `Budi Santoso {runId}` tidak tampil
158. Klik `[Clear Field]`
159. Klik `[Apply]`
160. Pilih opsi `Activated` pada filter `Activation Status`
161. Verifikasi `Activated` terpilih pada filter `Activation Status`
162. Ketik `Activated` pada pencarian opsi filter `Activation Status`
163. Verifikasi opsi `Activated` tampil pada daftar opsi filter `Activation Status`
164. Klik `[Clear Field]`
165. Pilih opsi `Activated` pada filter `Activation Status`
166. Klik `[Apply]`
167. Verifikasi baris `Sari Dewi {runId}` tetap tampil dan baris `Joko Susilo {runId}` (tanpa akun login) tidak tampil
168. Klik `[Clear Field]`
169. Klik `[Apply]`
170. Pilih opsi `Yes` pada filter `Temporary User`
171. Klik `[Apply]`
172. Verifikasi baris `Tari Sementara {runId}` dan baris `Tono Sementara {runId}` tampil dan baris `Sari Dewi {runId}` tidak tampil
173. Klik `[Clear Field]`
174. Klik `[Apply]`
175. Pilih rentang `T0 + 25 hari` sampai `T0 + 35 hari` pada filter `Temporary Until`
176. Klik `[Apply]`
177. Verifikasi baris `Tari Sementara {runId}` tampil dan baris `Tono Sementara {runId}` tidak tampil
178. Klik `[Clear Field]`
179. Klik `[Apply]`
180. Klik ikon Filter
181. Klik `[Cancel]` pada dialog Select Borrower

### Select Asset sebelum Borrower dipilih memuat aset dalam cakupan Group
182. Klik `[+ Asset]`
183. Ketik Search `{runId}`, tekan Enter
184. Verifikasi baris `Laptop Dell Latitude {runId}` tampil di dialog Select Asset
185. Verifikasi baris `Toyota Avanza {runId}` dari Group `Branch Surabaya` tampil di dialog Select Asset
186. Verifikasi baris `Printer Canon {runId}` dari Group `Branch Medan` di luar cakupan Aktor tidak dimuat
187. Verifikasi baris `Drone DJI Mavic 3 {runId}` (Allow Borrow `Deny`) tidak dimuat
188. Verifikasi baris `Excavator PC200 Berjalan {runId}` (Custody `In Borrow Process`) tidak dimuat
189. Verifikasi keterangan di bawah judul dialog adalah `Available assets in your groups.` tanpa kalimat kedua karena Borrower belum dipilih
190. Verifikasi kolom `Eligibility` pada baris `Toyota Avanza {runId}` memuat `Ready` karena Borrower belum dipilih
191. Verifikasi kolom `Eligibility` pada baris `Laptop Dell Latitude {runId}` memuat `Ready`
192. Verifikasi dialog memuat tombol `[Cancel]` dan `[Select]` di footer
193. Verifikasi toolbar dialog memuat tombol `Search by Scan`, ikon Search, dan ikon Filter

### Kolom Select Asset menampilkan isi dari data
194. Verifikasi kolom `Photo` pada baris `Laptop Dell Latitude {runId}` memuat foto utama `laptop-dell-latitude.png`
195. Verifikasi kolom `Photo` pada baris `Projector Epson EB-X06 {runId}` tampil tanpa foto utama aset
196. Verifikasi kolom `Name` pada baris `Laptop Dell Latitude {runId}` memuat nama aset `Laptop Dell Latitude {runId}`
197. Verifikasi kolom `Asset ID` pada baris `Laptop Dell Latitude {runId}` terisi Asset ID milik DU-012-1
198. Verifikasi kolom `Brand` pada baris `Laptop Dell Latitude {runId}` memuat `Dell {runId}`
199. Verifikasi kolom `Model/Type` pada baris `Laptop Dell Latitude {runId}` memuat `Latitude 5420 {runId}`
200. Verifikasi kolom `Group` pada baris `Laptop Dell Latitude {runId}` memuat `Head Office`
201. Verifikasi kolom `Group` pada baris `Toyota Avanza {runId}` memuat `Branch Surabaya`
202. Verifikasi kolom `Max Duration` pada baris `Laptop Dell Latitude {runId}` memuat `3 days`
203. Verifikasi kolom `Max Duration` pada baris `Toyota Avanza {runId}` memuat `14 days`
204. Verifikasi kolom `Approval` pada baris `Laptop Dell Latitude {runId}` memuat `Auto (≤ 3 days)`
205. Verifikasi kolom `Approval` pada baris `Projector Epson EB-X06 {runId}` memuat `Needs approval`
206. Verifikasi kolom `Approval` pada baris `Excavator PC200 {runId}` memuat `Needs approval (all must approve)`

### Kolom curated Select Asset tampil setelah diaktifkan di Setup Column
207. Buka Setup Column lewat ikon `⋯` pada header tabel
208. Aktifkan kolom `TAG`
209. Aktifkan kolom `Category`
210. Aktifkan kolom `Label`
211. Verifikasi kolom `TAG` pada baris `Laptop Dell Latitude {runId}` memuat `NFC`
212. Verifikasi kolom `TAG` pada baris `Toyota Avanza {runId}` memuat `—` karena aset `Non TAG`
213. Verifikasi kolom `Category` pada baris `Laptop Dell Latitude {runId}` memuat `Laptop {runId}`
214. Verifikasi kolom `Label` pada baris `Laptop Dell Latitude {runId}` memuat `Operasional {runId}`
215. Verifikasi kolom `Label` pada baris `Projector Epson EB-X06 {runId}` memuat `—`

### Search Select Asset menyaring baris menurut kolom Searchable
216. Klik `(←)` pada kotak Search
217. Klik ikon Search
218. Verifikasi kotak Search yang kosong memuat placeholder `Search asset name or ID...`
219. Ketik Search `Laptop Dell Latitude {runId}`, tekan Enter
220. Verifikasi baris `Laptop Dell Latitude {runId}` tampil dan baris `Projector Epson EB-X06 {runId}` tidak tampil (pencarian pada kolom `Name`)
221. Ganti isi kotak search dengan `Dell {runId}`, tekan Enter
222. Verifikasi baris `Laptop Dell Latitude {runId}` tampil dan baris `Projector Epson EB-X06 {runId}` tidak tampil (pencarian pada kolom `Brand`)
223. Ganti isi kotak search dengan `Latitude 5420 {runId}`, tekan Enter
224. Verifikasi baris `Laptop Dell Latitude {runId}` tampil dan baris `Projector Epson EB-X06 {runId}` tidak tampil (pencarian pada kolom `Model/Type`)
225. Ketik Search dengan Asset ID milik DU-012-1, tekan Enter
226. Verifikasi baris `Laptop Dell Latitude {runId}` tampil dan baris `Projector Epson EB-X06 {runId}` tidak tampil (pencarian pada kolom `Asset ID`)
227. Ganti isi kotak search dengan `Branch Surabaya`, tekan Enter
228. Verifikasi baris `Toyota Avanza {runId}` tampil (pencarian pada kolom `Group`)
229. Ganti isi kotak search dengan `NFC`, tekan Enter
230. Verifikasi baris `Laptop Dell Latitude {runId}` tampil (pencarian pada kolom `TAG`)
231. Ganti isi kotak search dengan `Heavy Equipment {runId}`, tekan Enter
232. Verifikasi baris `Excavator PC200 {runId}` tampil dan baris `Laptop Dell Latitude {runId}` tidak tampil (pencarian pada kolom `Category`)
233. Ganti isi kotak search dengan `14 days`, tekan Enter
234. Verifikasi baris `Toyota Avanza {runId}` tampil (pencarian pada kolom `Max Duration`)
235. Ganti isi kotak search dengan `Needs approval (all must approve)`, tekan Enter
236. Verifikasi baris `Excavator PC200 {runId}` tampil (pencarian pada kolom `Approval`)
237. Ganti isi kotak search dengan `Rapat {runId}`, tekan Enter
238. Verifikasi baris `Toyota Avanza {runId}` tampil dan baris `Laptop Dell Latitude {runId}` tidak tampil (pencarian pada kolom `Label`)
239. Ganti isi kotak search dengan `Ready`, tekan Enter
240. Verifikasi baris `Laptop Dell Latitude {runId}` tampil (pencarian pada kolom `Eligibility`)
241. Ganti isi kotak search dengan `Dell Kantor {runId}`, tekan Enter
242. Verifikasi baris `Laptop Dell Latitude {runId}` tampil dan baris `Projector Epson EB-X06 {runId}` tidak tampil (pencarian pada alias aset)
243. Ganti isi kotak search dengan `NFC-0001 {runId}`, tekan Enter
244. Verifikasi baris `Laptop Dell Latitude {runId}` tampil dan baris `Projector Epson EB-X06 {runId}` tidak tampil (pencarian pada kode tag aset, bukan label tipe TAG)
245. Ganti isi kotak search dengan `{runId}`, tekan Enter
246. Verifikasi baris `Laptop Dell Latitude {runId}`, `Projector Epson EB-X06 {runId}`, `Excavator PC200 {runId}`, dan `Toyota Avanza {runId}` tampil sebelum diurutkan

### Sort Select Asset mengurutkan baris menurut kolom
247. Verifikasi baris `Excavator PC200 {runId}` tampil di atas `Laptop Dell Latitude {runId}`, `Laptop Dell Latitude {runId}` di atas `Projector Epson EB-X06 {runId}`, dan `Projector Epson EB-X06 {runId}` di atas `Toyota Avanza {runId}` menurut urutan bawaan kolom `Name` dari A ke Z
248. Klik header kolom `Asset ID`
249. Verifikasi nilai kolom `Asset ID` pada baris `Laptop Dell Latitude {runId}`, `Projector Epson EB-X06 {runId}`, `Excavator PC200 {runId}`, dan `Toyota Avanza {runId}` terbaca naik dari A ke Z dari baris paling atas ke baris paling bawah menurut nilai Asset ID yang tampil di tabel
250. Klik header kolom `Brand`
251. Verifikasi baris `Laptop Dell Latitude {runId}` (`Dell {runId}`) tampil di atas `Projector Epson EB-X06 {runId}` (`Epson {runId}`), `Projector Epson EB-X06 {runId}` di atas `Excavator PC200 {runId}` (`Komatsu {runId}`), dan `Excavator PC200 {runId}` di atas `Toyota Avanza {runId}` (`Toyota {runId}`) menurut `Brand` dari A ke Z
252. Klik header kolom `Model/Type`
253. Verifikasi baris `Toyota Avanza {runId}` (`Avanza {runId}`) tampil di atas `Projector Epson EB-X06 {runId}` (`EB-X06 {runId}`), `Projector Epson EB-X06 {runId}` di atas `Laptop Dell Latitude {runId}` (`Latitude 5420 {runId}`), dan `Laptop Dell Latitude {runId}` di atas `Excavator PC200 {runId}` (`PC200 {runId}`) menurut `Model/Type` dari A ke Z
254. Klik header kolom `Group`
255. Verifikasi baris `Toyota Avanza {runId}` (`Branch Surabaya`) tampil di atas `Laptop Dell Latitude {runId}` (`Head Office`) menurut `Group` dari A ke Z
256. Klik header kolom `TAG`
257. Verifikasi baris `Laptop Dell Latitude {runId}` (`NFC`) tampil di atas `Projector Epson EB-X06 {runId}` (`QR`) dan `Projector Epson EB-X06 {runId}` di atas `Excavator PC200 {runId}` (`RFID`) menurut label ikon `TAG` secara alfabetis
258. Klik header kolom `Category`
259. Verifikasi baris `Toyota Avanza {runId}` (`Car {runId}`) tampil di atas `Excavator PC200 {runId}` (`Heavy Equipment {runId}`), `Excavator PC200 {runId}` di atas `Laptop Dell Latitude {runId}` (`Laptop {runId}`), dan `Laptop Dell Latitude {runId}` di atas `Projector Epson EB-X06 {runId}` (`Projector {runId}`) menurut `Category` dari A ke Z
260. Klik header kolom `Max Duration`
261. Verifikasi baris `Laptop Dell Latitude {runId}` (`3 days`) tampil di atas `Projector Epson EB-X06 {runId}` (`5 days`), `Projector Epson EB-X06 {runId}` di atas `Excavator PC200 {runId}` (`7 days`), dan `Excavator PC200 {runId}` di atas `Toyota Avanza {runId}` (`14 days`) menurut `Max Duration` secara numerik
262. Klik header kolom `Approval`
263. Verifikasi baris `Laptop Dell Latitude {runId}` (`Auto (≤ 3 days)`) tampil di atas `Projector Epson EB-X06 {runId}` (`Needs approval`) menurut `Approval` dari A ke Z
264. Klik header kolom `Label`
265. Verifikasi baris `Excavator PC200 {runId}` (`Event {runId}`) tampil di atas `Toyota Avanza {runId}` (`Rapat {runId}`) dan `Toyota Avanza {runId}` di atas `Laptop Dell Latitude {runId}` (`Event {runId}`, `Operasional {runId}`) menurut jumlah `Label` dari paling sedikit, dengan jumlah sama diurutkan menurut `Label` pertama dari A ke Z[^drift-1]
266. Klik header kolom `Label`
267. Verifikasi baris `Laptop Dell Latitude {runId}` (`Event {runId}`, `Operasional {runId}`) tampil di atas `Toyota Avanza {runId}` (`Rapat {runId}`) dan `Toyota Avanza {runId}` di atas `Excavator PC200 {runId}` (`Event {runId}`) menurut jumlah `Label` dari paling banyak, dengan jumlah sama diurutkan menurut `Label` pertama dari Z ke A[^drift-1]
268. Klik header kolom `Photo`
269. Verifikasi baris `Laptop Dell Latitude {runId}` tampil di atas `Toyota Avanza {runId}` dan `Toyota Avanza {runId}` di atas `Excavator PC200 {runId}` tetap menurut `Label` dari paling banyak, karena kolom `Photo` tidak bisa diurutkan

### Filter Select Asset menyaring baris menurut kolom Filterable
270. Klik ikon Filter
271. Verifikasi field `Asset Name` memuat placeholder `All asset names`
272. Verifikasi field `Brand` memuat placeholder `All brands`
273. Verifikasi field `Model/Type` memuat placeholder `All models`
274. Verifikasi field `Group` memuat placeholder `All groups`
275. Verifikasi field `TAG` memuat placeholder `All tags`
276. Verifikasi field `Category` memuat placeholder `All categories`
277. Verifikasi field `Approval` memuat placeholder `All approvals`
278. Verifikasi field `Label` memuat placeholder `All labels`
279. Verifikasi field `Eligibility` memuat placeholder `All eligibility`
280. Verifikasi Filter Panel tidak memuat field `Photo`, `Asset ID`, dan `Max Duration`
281. Pilih opsi `Laptop Dell Latitude {runId}` dan `Projector Epson EB-X06 {runId}` pada filter `Asset Name`
282. Verifikasi `Laptop Dell Latitude {runId}` dan `Projector Epson EB-X06 {runId}` terpilih bersamaan pada filter `Asset Name`
283. Ketik `Laptop Dell Latitude {runId}` pada pencarian opsi filter `Asset Name`
284. Verifikasi opsi `Laptop Dell Latitude {runId}` tampil dan opsi `Projector Epson EB-X06 {runId}` tidak tampil pada daftar opsi filter `Asset Name`
285. Klik `[Clear Field]`
286. Pilih opsi `Laptop Dell Latitude {runId}` pada filter `Asset Name`
287. Klik `[Apply]`
288. Verifikasi baris `Laptop Dell Latitude {runId}` tampil dan baris `Projector Epson EB-X06 {runId}` tidak tampil
289. Klik `[Clear Field]`
290. Klik `[Apply]`
291. Pilih opsi `Dell {runId}` dan `Epson {runId}` pada filter `Brand`
292. Verifikasi `Dell {runId}` dan `Epson {runId}` terpilih bersamaan pada filter `Brand`
293. Ketik `Dell {runId}` pada pencarian opsi filter `Brand`
294. Verifikasi opsi `Dell {runId}` tampil dan opsi `Epson {runId}` tidak tampil pada daftar opsi filter `Brand`
295. Klik `[Clear Field]`
296. Pilih opsi `Epson {runId}` pada filter `Brand`
297. Klik `[Apply]`
298. Verifikasi baris `Projector Epson EB-X06 {runId}` tampil dan baris `Laptop Dell Latitude {runId}` tidak tampil
299. Klik `[Clear Field]`
300. Klik `[Apply]`
301. Pilih opsi `Latitude 5420 {runId}` dan `EB-X06 {runId}` pada filter `Model/Type`
302. Verifikasi `Latitude 5420 {runId}` dan `EB-X06 {runId}` terpilih bersamaan pada filter `Model/Type`
303. Ketik `EB-X06 {runId}` pada pencarian opsi filter `Model/Type`
304. Verifikasi opsi `EB-X06 {runId}` tampil dan opsi `Latitude 5420 {runId}` tidak tampil pada daftar opsi filter `Model/Type`
305. Klik `[Clear Field]`
306. Pilih opsi `PC200 {runId}` pada filter `Model/Type`
307. Klik `[Apply]`
308. Verifikasi baris `Excavator PC200 {runId}` tampil dan baris `Laptop Dell Latitude {runId}` tidak tampil
309. Klik `[Clear Field]`
310. Klik `[Apply]`
311. Pilih node `Head Office` dan `Branch Surabaya` pada filter `Group`
312. Verifikasi `Head Office` dan `Branch Surabaya` terpilih bersamaan pada filter `Group` dialog Select Asset
313. Klik `[Clear Field]`
314. Pilih node `Branch Surabaya` pada filter `Group`
315. Klik `[Apply]`
316. Verifikasi baris `Toyota Avanza {runId}` tampil dan baris `Laptop Dell Latitude {runId}` tidak tampil
317. Klik `[Clear Field]`
318. Klik `[Apply]`
319. Pilih opsi `NFC` dan `QR` pada filter `TAG`
320. Verifikasi `NFC` dan `QR` terpilih bersamaan pada filter `TAG`
321. Ketik `NFC` pada pencarian opsi filter `TAG`
322. Verifikasi opsi `NFC` tampil dan opsi `QR` tidak tampil pada daftar opsi filter `TAG`
323. Klik `[Clear Field]`
324. Pilih opsi `RFID` pada filter `TAG`
325. Klik `[Apply]`
326. Verifikasi baris `Excavator PC200 {runId}` tampil dan baris `Laptop Dell Latitude {runId}` tidak tampil
327. Klik `[Clear Field]`
328. Klik `[Apply]`
329. Pilih node `Laptop {runId}` dan `Projector {runId}` pada filter `Category`
330. Verifikasi `Laptop {runId}` dan `Projector {runId}` terpilih bersamaan pada filter `Category`
331. Klik `[Clear Field]`
332. Pilih node `Laptop {runId}` pada filter `Category`
333. Klik `[Apply]`
334. Verifikasi baris `Laptop Dell Latitude {runId}` tampil dan baris `Projector Epson EB-X06 {runId}` tidak tampil
335. Klik `[Clear Field]`
336. Klik `[Apply]`
337. Pilih opsi `Auto (≤ 3 days)` dan `Needs approval` pada filter `Approval`
338. Verifikasi `Auto (≤ 3 days)` dan `Needs approval` terpilih bersamaan pada filter `Approval`
339. Ketik `Auto (≤ 3 days)` pada pencarian opsi filter `Approval`
340. Verifikasi opsi `Auto (≤ 3 days)` tampil dan opsi `Needs approval` tidak tampil pada daftar opsi filter `Approval`
341. Klik `[Clear Field]`
342. Pilih opsi `Needs approval (all must approve)` pada filter `Approval`
343. Klik `[Apply]`
344. Verifikasi baris `Excavator PC200 {runId}` tampil dan baris `Laptop Dell Latitude {runId}` tidak tampil
345. Klik `[Clear Field]`
346. Klik `[Apply]`
347. Pilih opsi `Operasional {runId}` dan `Rapat {runId}` pada filter `Label`
348. Verifikasi `Operasional {runId}` dan `Rapat {runId}` terpilih bersamaan pada filter `Label`
349. Ketik `Rapat {runId}` pada pencarian opsi filter `Label`
350. Verifikasi opsi `Rapat {runId}` tampil dan opsi `Operasional {runId}` tidak tampil pada daftar opsi filter `Label`
351. Klik `[Clear Field]`
352. Pilih opsi `Operasional {runId}` pada filter `Label`
353. Klik `[Apply]`
354. Verifikasi baris `Laptop Dell Latitude {runId}` tampil dan baris `Excavator PC200 {runId}` tidak tampil
355. Klik `[Clear Field]`
356. Klik `[Apply]`
357. Pilih opsi `Ready` pada filter `Eligibility`
358. Klik `[Apply]`
359. Verifikasi baris `Laptop Dell Latitude {runId}` tampil
360. Klik `[Clear Field]`
361. Klik `[Apply]`
362. Klik ikon Filter
363. Klik `[Cancel]` pada dialog Select Asset

### Select Asset menilai kelayakan menurut Borrower yang dipilih
364. Klik `[Select Borrower]`
365. Ketik Search `Sari Dewi {runId}`, tekan Enter
366. Pilih baris `Sari Dewi {runId}`
367. Klik `[Select]`
368. Klik `[+ Asset]`
369. Ketik Search `{runId}`, tekan Enter
370. Verifikasi keterangan di bawah judul dialog adalah `Available assets in your groups. Eligibility is checked for Sari Dewi {runId}.`
371. Verifikasi kolom `Eligibility` pada baris `Laptop Dell Latitude {runId}` memuat `Ready` dan checkbox baris dapat dicentang
372. Verifikasi kolom `Eligibility` pada baris `Toyota Avanza {runId}` memuat `Not ready` dan checkbox baris disabled
373. Verifikasi alasan `Not ready` pada baris `Toyota Avanza {runId}` tersampaikan: `Sari Dewi {runId} can't borrow assets from Branch Surabaya.`
374. Klik header kolom `Eligibility`
375. Verifikasi baris `Toyota Avanza {runId}` (`Not ready`) tampil di atas `Laptop Dell Latitude {runId}` (`Ready`) menurut `Eligibility` dari A ke Z
376. Klik ikon Filter
377. Pilih opsi `Ready` dan `Not ready` pada filter `Eligibility`
378. Verifikasi `Ready` dan `Not ready` terpilih bersamaan pada filter `Eligibility`
379. Ketik `Not ready` pada pencarian opsi filter `Eligibility`
380. Verifikasi opsi `Not ready` tampil dan opsi `Ready` tidak tampil pada daftar opsi filter `Eligibility`
381. Klik `[Clear Field]`
382. Klik ikon Filter

### Select Asset menilai batas Max assets per borrower
383. Klik `[Cancel]` pada dialog Select Asset
384. Klik nama Borrower `Sari Dewi {runId}` pada field Borrower
385. Ketik Search `Budi Santoso {runId}`, tekan Enter
386. Pilih baris `Budi Santoso {runId}`
387. Klik `[Select]`
388. Klik `[+ Asset]`
389. Ketik Search `Laptop Dell Latitude {runId}`, tekan Enter
390. Verifikasi kolom `Eligibility` pada baris `Laptop Dell Latitude {runId}` memuat `Not ready` dan checkbox baris disabled karena batas Max assets per borrower tercapai
391. Verifikasi alasan `Not ready` pada baris `Laptop Dell Latitude {runId}` tersampaikan: `Budi Santoso {runId} can borrow up to 10 assets at a time.`
392. Klik `[Cancel]` pada dialog Select Asset

### Aset dari Group berbeda dapat dipilih bersama
393. Klik nama Borrower `Budi Santoso {runId}` pada field Borrower
394. Ketik Search `Budi Setiawan {runId}`, tekan Enter
395. Pilih baris `Budi Setiawan {runId}`
396. Klik `[Select]`
397. Klik `[+ Asset]`
398. Ketik Search `{runId}`, tekan Enter
399. Centang baris `Laptop Dell Latitude {runId}`
400. Centang baris `Toyota Avanza {runId}`
401. Klik `[Select]`
402. Verifikasi baris `Laptop Dell Latitude {runId}` dari Group `Head Office` dan baris `Toyota Avanza {runId}` dari Group `Branch Surabaya` tampil bersama di daftar aset form Borrow Request

[^drift-1]: Drift PRD vs foundation. PRD §4.1d (T-BRW-04, kolom Label): Sort `Alphabetical (A–Z)`. Foundation `process/prd-process/prd-conventions.md` §9.7: kolom `+N more` diurutkan menurut jumlah nilai, ascending paling sedikit duluan dan descending paling banyak duluan, dengan tiebreaker jumlah sama berupa urutan alfabetis menurut nilai pertama (A–Z untuk ascending, Z–A untuk descending). Diasersi: foundation, karena kolom Label adalah pola bersama chip `+N more` (SB-4).

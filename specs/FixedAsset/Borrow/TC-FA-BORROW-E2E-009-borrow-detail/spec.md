---
id: TC-FA-BORROW-E2E-009-borrow-detail
title: "Borrow Detail menampilkan header BRW dan tabel Assets dengan aksi baris menurut status"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1c#p1", "§4.1c#r1", "§4.1c#r2", "§4.1c#r3", "§4.1c#r4", "§4.1c#r5", "§4.1c#r6", "§4.1c#r7", "§4.1c#r8", "§4.1c#r9", "§4.1c#r10", "§4.1c#r11", "§4.1c#r12", "§4.1c#r13", "§4.1c#r14", "§4.1c#r15", "§4.1c#r16", "§4.1c#r17", "§4.1c#r18", "§4.1c#r19", "§4.1c#p4", "§4.1c#r20", "§4.1c#r21", "§4.1c#r22", "§4.1c#r23", "§4.1c#r24", "§4.1c#r25", "§4.1c#r26", "§4.1c#r27", "§4.1c#r28", "§4.1c#r29", "§4.1c#r30", "§4.1c#r31", "§4.2#p5", "§4.2.4#p1", "§4.2.4#p2"]
smoke: []
dependsOn: []
trace:
  "§4.1c#p1": [11, 14]
  "§4.1c#r1": [17, 18, 19, 20]
  "§4.1c#r2": [15, 133, 135, 197, 198, 240, 241]
  "§4.1c#r3": [21, 137, 139, 200, 201]
  "§4.1c#r4": [22, 141, 143, 203, 204, 246, 247]
  "§4.1c#r5": [23, 145, 147, 206, 207, 252, 253]
  "§4.1c#r6": [24, 25, 26, 27, 149, 151, 209, 210, 258, 259]
  "§4.1c#r7": [38, 153, 155, 233, 234, 264, 265]
  "§4.1c#r8": [40, 157, 159, 212, 213, 270, 271]
  "§4.1c#r9": [28, 29, 161, 163, 276, 277]
  "§4.1c#r10": [42, 165, 167, 282, 283]
  "§4.1c#r11": [44, 45, 169, 171, 288, 289]
  "§4.1c#r12": [30, 31, 173, 175, 215, 216]
  "§4.1c#r13": [47, 177, 179, 218, 219, 295, 296]
  "§4.1c#r14": [32, 33, 181, 183, 221, 222, 301, 302]
  "§4.1c#r15": [49, 185, 187, 224, 225]
  "§4.1c#r16": [34, 35]
  "§4.1c#r17": [34, 35]
  "§4.1c#r18": [51, 189, 191, 227, 228]
  "§4.1c#r19": [53, 193, 195, 230, 231, 307, 308]
  "§4.1c#p4": [55]
  "§4.1c#r20": [55, 76, 80]
  "§4.1c#r21": [55, 76, 84]
  "§4.1c#r22": [55, 59, 76, 113, 331]
  "§4.1c#r23": [55, 59, 88]
  "§4.1c#r24": [56, 62, 66, 70, 118]
  "§4.1c#r25": [56, 62, 66, 69, 76, 123]
  "§4.1c#r26": [56, 62, 66, 70, 91]
  "§4.1c#r27": [56, 62, 66, 69, 95]
  "§4.1c#r28": [56, 69, 99]
  "§4.1c#r29": [56, 73, 103, 105]
  "§4.1c#r30": [55, 59, 63, 76, 108, 110]
  "§4.1c#r31": [130, 316, 317, 320, 368]
  "§4.2#p5": [11]
  "§4.2.4#p1": [3, 4, 5, 7, 8, 9, 10, 13, 327, 344, 347]
  "§4.2.4#p2": [12, 126, 127, 325, 328, 329, 334, 337, 341, 352, 353, 354, 357, 361, 367]
anchor: [131, 326, 340, 360, 366]
coverage:
  web: automated
---

# Borrow Detail menampilkan header BRW dan tabel Assets dengan aksi baris menurut status

## Prerequisites
- Aktor: Total Control `Admin Borrow {runId}` (DU-009-1), cakupan seluruh client.
- Layar awal: Transactions > Borrow, tab Transactions.
- Data:
  - DU-009-1: User `Admin Borrow {runId}`, role Total Control, cakupan seluruh client; pelapor Damage Report pada aset `Speaker JBL PartyBox 110 {runId}`.
  - Pengaju: `Agus Pratama` (Asset Admin, Group penugasan `Head Office`), tampil `Agus P`.
  - DU-009-2: BRW Borrower `Joko Susilo` (tampil `Joko S`), Group `Head Office`, pengaju `Agus P`, Note `Peminjaman untuk kegiatan pelatihan`, status header `Waiting for Handover` dengan penanda `Overdue`. Sembilan baris, dibuat berurutan dari Tripod sampai Amplifier (urutan abjad terbalik):
    - `Amplifier Yamaha A-S301 {runId}`: Returned (Brand `Yamaha`, Model/Type `A-S301`, Category `Audio`, TAG RFID, Duration `5 days`, Due Date `T0 − 7 hari`, Handed Over At `T0 − 11 hari`, Returned At `T0 − 5 hari`, Approval `Approved`, Extensions `0 / 3`, Purpose `Konser amal`, Handed Over By `Agus P`, foto utama aset tersedia, foto handover dan foto return tersimpan).
    - `Bor Listrik Bosch GSB 550 {runId}`: Rejected (Brand `Bosch`, Model/Type `GSB 550`, Category `Perkakas`, Non TAG, Duration `3 days`, Approval `Rejected`, Reason `Stok sedang dikalibrasi`, Purpose `Renovasi ruang rapat`, tanpa foto utama aset).
    - `Kamera Canon EOS 90D {runId}`: Overdue (Brand `Canon`, Model/Type `EOS 90D`, Category `Kamera`, TAG NFC, Duration `5 days`, Due Date `T0 − 2 hari`, Handed Over At `T0 − 6 hari`, Approval `Approved`, Extensions `1 / 3`, Purpose `Dokumentasi`, Handed Over By `Rina W`).
    - `Laptop Lenovo ThinkPad T14 {runId}`: Waiting for Handover (Brand `Lenovo`, Model/Type `ThinkPad T14`, Category `Laptop`, TAG RFID, Duration `4 days`, Approval `Auto-approved`, Purpose `Pelatihan karyawan`).
    - `Printer Epson L3250 {runId}`: Waiting for Approval (Brand `Epson`, Model/Type `L3250`, Category `Printer`, Non TAG, Duration `2 days`, Approval `Waiting`).
    - `Proyektor BenQ MH535 {runId}`: Borrowed (Brand `BenQ`, Model/Type `MH535`, Category `Proyektor`, TAG QR, Duration `6 days`, Due Date `T0 + 2 hari`, Handed Over At `T0 − 3 hari`, Approval `Approved`, Extensions `0 / 3`, Handed Over By `Agus P`).
    - `Speaker JBL PartyBox 110 {runId}`: Borrowed dengan Damage Report berstatus Waiting for Confirmation yang dilaporkan `Admin Borrow {runId}` (badge `Reported Damaged`, Brand `JBL`, Model/Type `PartyBox 110`, Category `Audio`, TAG QR, Duration `6 days`, Handed Over At `T0 − 2 hari`, Due Date `T0 + 3 hari`, Handed Over By `Agus P`).
    - `Tablet Samsung Tab S8 {runId}`: Borrowed dengan pengajuan Extend yang menunggu approval (tampil `Extension Approval`, Brand `Samsung`, Model/Type `Tab S8`, Category `Tablet`, TAG NFC, Duration `6 days`, Handed Over At `T0 − 2 hari`, Due Date `T0 + 3 hari`, Handed Over By `Agus P`).
    - `Tripod Manfrotto 290 {runId}`: Canceled oleh System (Brand `Manfrotto`, Model/Type `290`, Category `Tripod`, Non TAG, Duration `36 hours`, Reason `Timed out (Waiting for Approval)`).
  - DU-009-3: BRW Borrower `Kirana Putri` (tampil `Kirana P`), Group `Head Office`, dua aset berstatus Waiting for Handover dengan Approval `Auto-approved`: `Mikrofon Shure SM7B {runId}` dan `Headset Sennheiser HD 280 {runId}`.
  - DU-009-4: BRW Borrower `Lukman Hakim` (tampil `Lukman H`), Group `Head Office`, satu aset `Lampu Studio Godox SL60 {runId}` berstatus Waiting for Handover dengan Approval `Not required`.
  - DU-009-10: BRW Self-service, Borrower `Rani Wijaya` (tampil `Rani W`), Group `Head Office`, satu aset `Kamera Fujifilm X-S10 {runId}` berstatus Waiting for Handover dengan Approval `Self-service`.
  - DU-009-11: BRW Borrower `Satria Nugroho` (tampil `Satria N`), Group `Head Office`, dua aset berstatus Waiting for Handover: `Gimbal Zhiyun Crane 2 {runId}` dengan Approval `Auto-approved` dan `Tripod Velbon EX 330 {runId}` dengan Approval `Not required`.
  - DU-009-12: BRW Borrower tanpa akun `Sari Utami` (tampil `Sari U`) dengan PIC `Rina Wijaya`, Group `Head Office`, satu aset `Scanner Fujitsu iX1600 {runId}` berstatus Waiting for Handover.
  - DU-009-13: BRW Borrower tanpa akun `Teguh Santoso` (tampil `Teguh S`) tanpa PIC, Group `Head Office`, satu aset `Flashdisk Kingston 128 GB {runId}` berstatus Waiting for Handover.
  - DU-009-5: BRW Returned, Borrower `Nanda Prakoso` (tampil `Nanda P`), Group `Head Office`, satu aset `Drone DJI Air 3 {runId}` berstatus Returned dengan penanda `Missing` yang kemudian ditemukan dan berstatus Available di luar BRW aktif.
  - DU-009-6: BRW Returned, Borrower `Oki Firmansyah` (tampil `Oki F`), Group `Head Office`, dua aset `Drone DJI Mini 4 {runId}` dan `Gimbal DJI RS 4 {runId}` berstatus Returned dengan penanda `Missing` yang kemudian ditemukan dan berstatus Available di luar BRW aktif.
  - DU-009-7: BRW Returned, Borrower `Putri Amelia` (tampil `Putri A`), Group `Head Office`, satu aset `Walkie Talkie Motorola T82 {runId}` berstatus Returned dengan penanda `Missing` yang kemudian ditemukan, dan kini berada di BRW aktif DU-009-8.
  - DU-009-8: BRW Borrower `Qori Hidayat` (tampil `Qori H`), Group `Head Office`, satu aset `Walkie Talkie Motorola T82 {runId}` berstatus Borrowed.
  - DU-009-9: User `Monitor Borrow {runId}`, role Monitoring & Report, cakupan seluruh client.
- Kondisi:
  - Akun `Monitor Borrow {runId}` aktif dan kredensialnya disediakan fase 2.
  - Date Format dan Time Format di General Settings entitas berlaku untuk tampilan tanggal.
  - Max extensions efektif seluruh aset pada spec ini bernilai `3`.

## Test Steps

### Borrow Detail dibuka dari Transaction ID dan header BRW
1. Ketik Search `{runId}`, tekan Enter
2. Klik Transaction ID baris Borrower `Joko S`
3. Verifikasi breadcrumb memuat `Transactions > Borrow > Transactions > Detail`
4. Verifikasi judul halaman memuat Transaction ID BRW milik DU-009-2, badge status `Waiting for Handover`, dan badge `Overdue`
5. Verifikasi judul halaman tidak memuat ringkasan jumlah baris per status
6. Klik tombol copy pada judul
7. Verifikasi toast `Success, Transaction ID has been copied.` tampil
8. Verifikasi header menampilkan Requested By `Agus P` beserta tanggal request, Borrower `Joko S`, Group `Head Office`, Note `Peminjaman untuk kegiatan pelatihan`, dan Last Updated
9. Verifikasi header tidak memuat Purpose maupun Due date
10. Verifikasi header tidak memuat Duration
11. Verifikasi halaman tidak memiliki tab dan tidak memiliki judul `Assets`
12. Verifikasi baris info `Approval` tidak tampil karena baris BRW tidak seluruhnya tanpa approval
13. Verifikasi toolbar tabel memuat `Search by Scan`, `Search`, `Filter`, dan `Download` tanpa menu `⋯`
14. Verifikasi tabel Assets memuat 9 baris dengan aset `Amplifier Yamaha A-S301 {runId}`, `Bor Listrik Bosch GSB 550 {runId}`, `Kamera Canon EOS 90D {runId}`, `Laptop Lenovo ThinkPad T14 {runId}`, `Printer Epson L3250 {runId}`, `Proyektor BenQ MH535 {runId}`, `Speaker JBL PartyBox 110 {runId}`, `Tablet Samsung Tab S8 {runId}`, dan `Tripod Manfrotto 290 {runId}`

### Isi kolom yang tampil sejak awal
15. Verifikasi urutan baris dari atas ke bawah mengikuti Name A–Z: `Amplifier Yamaha A-S301 {runId}`, `Bor Listrik Bosch GSB 550 {runId}`, `Kamera Canon EOS 90D {runId}`, `Laptop Lenovo ThinkPad T14 {runId}`, `Printer Epson L3250 {runId}`, `Proyektor BenQ MH535 {runId}`, `Speaker JBL PartyBox 110 {runId}`, `Tablet Samsung Tab S8 {runId}`, lalu `Tripod Manfrotto 290 {runId}`
16. Klik header kolom `Photo`
17. Verifikasi urutan baris tidak berubah setelah header `Photo` diklik
18. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan foto utama aset
19. Verifikasi baris aset `Bor Listrik Bosch GSB 550 {runId}` menampilkan placeholder gambar standar karena aset tanpa foto utama
20. Verifikasi tabel Assets tidak memuat kolom `Transaction ID`, `Group`, dan `Borrower`
21. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan Asset ID milik DU-009-2 baris Amplifier
22. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan Brand `Yamaha` dan baris aset `Kamera Canon EOS 90D {runId}` menampilkan Brand `Canon`
23. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan Model/Type `A-S301` dan baris aset `Kamera Canon EOS 90D {runId}` menampilkan Model/Type `EOS 90D`
24. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan status `Returned`, baris aset `Bor Listrik Bosch GSB 550 {runId}` menampilkan status `Rejected`, dan baris aset `Tripod Manfrotto 290 {runId}` menampilkan status `Canceled`
25. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` menampilkan status `Overdue`, baris aset `Laptop Lenovo ThinkPad T14 {runId}` menampilkan status `Waiting for Handover`, dan baris aset `Printer Epson L3250 {runId}` menampilkan status `Waiting for Approval`
26. Verifikasi baris aset `Proyektor BenQ MH535 {runId}` menampilkan status `Borrowed` dan baris aset `Tablet Samsung Tab S8 {runId}` menampilkan status `Extension Approval`
27. Verifikasi baris aset `Speaker JBL PartyBox 110 {runId}` menampilkan status `Borrowed` dan badge `Reported Damaged`
28. Verifikasi baris aset `Proyektor BenQ MH535 {runId}` menampilkan Due Date `T0 + 2 hari` dan baris aset `Laptop Lenovo ThinkPad T14 {runId}` menampilkan `—` sebelum handover
29. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` menampilkan Due Date `T0 − 2 hari` sebagai Overdue
30. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan Duration `5 days` dan baris aset `Laptop Lenovo ThinkPad T14 {runId}` menampilkan Duration `4 days`
31. Verifikasi baris aset `Tripod Manfrotto 290 {runId}` menampilkan Duration `36 hours`
32. Verifikasi baris aset `Printer Epson L3250 {runId}` menampilkan Approval `Waiting`, baris aset `Proyektor BenQ MH535 {runId}` menampilkan `Approved`, dan baris aset `Laptop Lenovo ThinkPad T14 {runId}` menampilkan `Auto-approved`
33. Verifikasi baris aset `Bor Listrik Bosch GSB 550 {runId}` menampilkan Approval `Rejected` dan baris aset `Tripod Manfrotto 290 {runId}` menampilkan `—`
34. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan thumbnail Handover Photo dan thumbnail Return Photo
35. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` menampilkan `—` pada Handover Photo dan Return Photo

### Isi kolom tambahan yang ditampilkan lewat Column Visibility
36. Klik header kolom Actions `⋯`
37. Centang `TAG` pada panel Column Visibility
38. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan ikon TAG `RFID` dan baris aset `Printer Epson L3250 {runId}` menampilkan `—`
39. Centang `Category` pada panel Column Visibility
40. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan Category `Audio` dan baris aset `Kamera Canon EOS 90D {runId}` menampilkan Category `Kamera`
41. Centang `Handed Over At` pada panel Column Visibility
42. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan Handed Over At `T0 − 11 hari` dan baris aset `Printer Epson L3250 {runId}` menampilkan `—`
43. Centang `Returned At` pada panel Column Visibility
44. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan Returned At `T0 − 5 hari` dengan `late 2 days`
45. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` menampilkan `—` pada Returned At
46. Centang `Extensions` pada panel Column Visibility
47. Verifikasi baris aset `Proyektor BenQ MH535 {runId}` menampilkan Extensions `0 / 3`
48. Centang `Reason` pada panel Column Visibility
49. Verifikasi baris aset `Bor Listrik Bosch GSB 550 {runId}` menampilkan Reason `Stok sedang dikalibrasi` apa adanya dan baris aset `Tripod Manfrotto 290 {runId}` menampilkan Reason `Timed out (Waiting for Approval)`
50. Centang `Purpose` pada panel Column Visibility
51. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` menampilkan Purpose `Dokumentasi` dan baris aset `Laptop Lenovo ThinkPad T14 {runId}` menampilkan Purpose `Pelatihan karyawan`
52. Centang `Handed Over By` pada panel Column Visibility
53. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` menampilkan Handed Over By `Rina W` dan baris aset `Laptop Lenovo ThinkPad T14 {runId}` menampilkan `—`

### Aksi baris menurut status baris
54. Klik `⋯` pada baris aset `Laptop Lenovo ThinkPad T14 {runId}`
55. Verifikasi menu baris tabel Assets memuat `Borrow Log`, `Transaction Rules`, `Hand Over`, `Remind Borrower`, dan `Cancel Borrow`
56. Verifikasi menu baris tabel Assets tidak memuat `Request Extension`, `Return`, `Report Damaged`, `Report Missing`, `Cancel Damage Report`, dan `Cancel Extension`
57. Tutup menu baris
58. Klik `⋯` pada baris aset `Printer Epson L3250 {runId}`
59. Verifikasi menu baris tabel Assets memuat `Cancel Borrow` dan tidak memuat `Hand Over` maupun `Remind Borrower`
60. Tutup menu baris
61. Klik `⋯` pada baris aset `Proyektor BenQ MH535 {runId}`
62. Verifikasi menu baris tabel Assets memuat `Request Extension`, `Return`, `Report Damaged`, dan `Report Missing`
63. Verifikasi menu baris tabel Assets tidak memuat `Cancel Borrow`
64. Tutup menu baris
65. Klik `⋯` pada baris aset `Kamera Canon EOS 90D {runId}`
66. Verifikasi menu baris tabel Assets memuat `Request Extension`, `Return`, `Report Damaged`, dan `Report Missing` untuk baris Overdue
67. Tutup menu baris
68. Klik `⋯` pada baris aset `Speaker JBL PartyBox 110 {runId}`
69. Verifikasi menu baris tabel Assets memuat `Return`, `Report Missing`, dan `Cancel Damage Report`
70. Verifikasi menu baris tabel Assets tidak memuat `Request Extension` dan `Report Damaged`
71. Tutup menu baris
72. Klik `⋯` pada baris aset `Tablet Samsung Tab S8 {runId}`
73. Verifikasi menu baris tabel Assets memuat `Cancel Extension`
74. Tutup menu baris
75. Klik `⋯` pada baris aset `Tripod Manfrotto 290 {runId}`
76. Verifikasi menu baris tabel Assets memuat `Borrow Log` dan `Transaction Rules` dan tidak memuat `Cancel Borrow`, `Return`, maupun `Hand Over`
77. Tutup menu baris

### Aksi baris membuka dialog atau halaman yang sesuai
78. Klik `⋯` pada baris aset `Amplifier Yamaha A-S301 {runId}`
79. Klik `Borrow Log`
80. Verifikasi dialog Borrow Log terbuka untuk aset `Amplifier Yamaha A-S301 {runId}`
81. Tutup dialog Borrow Log
82. Klik `⋯` pada baris aset `Amplifier Yamaha A-S301 {runId}`
83. Klik `Transaction Rules`
84. Verifikasi dialog `Transaction Rules` terbuka untuk aset `Amplifier Yamaha A-S301 {runId}`
85. Tutup dialog `Transaction Rules`
86. Klik `⋯` pada baris aset `Laptop Lenovo ThinkPad T14 {runId}`
87. Klik `Remind Borrower`
88. Verifikasi toast `Success, reminder has been sent to Joko Susilo.` tampil dan baris aset `Laptop Lenovo ThinkPad T14 {runId}` tetap berstatus `Waiting for Handover`
89. Klik `⋯` pada baris aset `Proyektor BenQ MH535 {runId}`
90. Klik `Report Damaged`
91. Verifikasi dialog `Report Damaged` terbuka untuk aset `Proyektor BenQ MH535 {runId}`
92. Tutup dialog `Report Damaged` tanpa menyimpan
93. Klik `⋯` pada baris aset `Proyektor BenQ MH535 {runId}`
94. Klik `Report Missing`
95. Verifikasi dialog `Report Missing` terbuka untuk aset `Proyektor BenQ MH535 {runId}`
96. Tutup dialog `Report Missing` tanpa menyimpan
97. Klik `⋯` pada baris aset `Speaker JBL PartyBox 110 {runId}`
98. Klik `Cancel Damage Report`
99. Verifikasi dialog Cancel Damage Report terbuka untuk aset `Speaker JBL PartyBox 110 {runId}`
100. Tutup dialog Cancel Damage Report tanpa mengonfirmasi
101. Klik `⋯` pada baris aset `Tablet Samsung Tab S8 {runId}`
102. Klik `Cancel Extension`
103. Verifikasi dialog `Cancel Extension` terbuka
104. Klik `[Go Back]` pada dialog
105. Verifikasi baris aset `Tablet Samsung Tab S8 {runId}` tetap menampilkan status `Extension Approval`
106. Klik `⋯` pada baris aset `Printer Epson L3250 {runId}`
107. Klik `Cancel Borrow`
108. Verifikasi dialog `Cancel Borrow` terbuka tanpa field Reason
109. Klik `[Go Back]` pada dialog
110. Verifikasi baris aset `Printer Epson L3250 {runId}` tetap menampilkan status `Waiting for Approval`
111. Klik `⋯` pada baris aset `Laptop Lenovo ThinkPad T14 {runId}`
112. Klik `Hand Over`
113. Verifikasi halaman Handover terbuka hanya untuk aset `Laptop Lenovo ThinkPad T14 {runId}`
114. Kembali ke tab Transactions lewat segmen Origin Tab pada breadcrumb
115. Klik Transaction ID baris Borrower `Joko S`
116. Klik `⋯` pada baris aset `Proyektor BenQ MH535 {runId}`
117. Klik `Request Extension`
118. Verifikasi halaman `Extension Request` terbuka hanya untuk aset `Proyektor BenQ MH535 {runId}`
119. Kembali ke tab Transactions lewat segmen Origin Tab pada breadcrumb
120. Klik Transaction ID baris Borrower `Joko S`
121. Klik `⋯` pada baris aset `Proyektor BenQ MH535 {runId}`
122. Klik `Return`
123. Verifikasi halaman `Return Asset` terbuka hanya untuk aset `Proyektor BenQ MH535 {runId}`
124. Kembali ke tab Transactions lewat segmen Origin Tab pada breadcrumb
125. Klik Transaction ID baris Borrower `Joko S`

### Tombol aksi di bawah tabel dan Download
126. Verifikasi tombol `[Cancel Borrow]`, `[Request Extension]`, `[Return]`, dan `[Hand Over]` tampil di bawah tabel
127. Verifikasi tombol `[Review]` tidak tampil karena tidak ada pengajuan Extend yang menunggu review
128. Klik `Download`
129. Pilih `Download as CSV`
130. Verifikasi berkas terunduh dengan nama `Borrow-Assets` dan memuat 9 baris data

### Sort kolom tabel Assets lewat klik header
131. Verifikasi tabel Assets memuat 9 baris milik BRW ini
132. Klik header kolom `Name`
133. Verifikasi urutan baris dari atas ke bawah: aset `Amplifier Yamaha A-S301 {runId}`, lalu aset `Tripod Manfrotto 290 {runId}`
134. Klik header kolom `Name`
135. Verifikasi urutan baris dari atas ke bawah: aset `Tripod Manfrotto 290 {runId}`, lalu aset `Amplifier Yamaha A-S301 {runId}`
136. Klik header kolom `Asset ID`
137. Verifikasi kolom Asset ID dari atas ke bawah berurutan alfabetis menaik
138. Klik header kolom `Asset ID`
139. Verifikasi kolom Asset ID dari atas ke bawah berurutan alfabetis menurun
140. Klik header kolom `Brand`
141. Verifikasi urutan baris dari atas ke bawah: aset `Proyektor BenQ MH535 {runId}`, lalu aset `Bor Listrik Bosch GSB 550 {runId}`, lalu aset `Kamera Canon EOS 90D {runId}` (Brand `BenQ`, `Bosch`, lalu `Canon`)
142. Klik header kolom `Brand`
143. Verifikasi urutan baris dari atas ke bawah: aset `Kamera Canon EOS 90D {runId}`, lalu aset `Bor Listrik Bosch GSB 550 {runId}`, lalu aset `Proyektor BenQ MH535 {runId}` (Brand `Canon`, `Bosch`, lalu `BenQ`)
144. Klik header kolom `Model/Type`
145. Verifikasi urutan baris dari atas ke bawah: aset `Tripod Manfrotto 290 {runId}`, lalu aset `Amplifier Yamaha A-S301 {runId}`, lalu aset `Kamera Canon EOS 90D {runId}` (Model/Type `290`, `A-S301`, lalu `EOS 90D`)
146. Klik header kolom `Model/Type`
147. Verifikasi urutan baris dari atas ke bawah: aset `Kamera Canon EOS 90D {runId}`, lalu aset `Amplifier Yamaha A-S301 {runId}`, lalu aset `Tripod Manfrotto 290 {runId}` (Model/Type `EOS 90D`, `A-S301`, lalu `290`)
148. Klik header kolom `Status`
149. Verifikasi urutan baris dari atas ke bawah: aset `Proyektor BenQ MH535 {runId}`, lalu aset `Tripod Manfrotto 290 {runId}`, lalu aset `Tablet Samsung Tab S8 {runId}`, lalu aset `Kamera Canon EOS 90D {runId}`, lalu aset `Bor Listrik Bosch GSB 550 {runId}`, lalu aset `Amplifier Yamaha A-S301 {runId}`, lalu aset `Printer Epson L3250 {runId}`, lalu aset `Laptop Lenovo ThinkPad T14 {runId}` (status `Borrowed`, `Canceled`, `Extension Approval`, `Overdue`, `Rejected`, `Returned`, `Waiting for Approval`, lalu `Waiting for Handover`)
150. Klik header kolom `Status`
151. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Lenovo ThinkPad T14 {runId}`, lalu aset `Printer Epson L3250 {runId}`, lalu aset `Amplifier Yamaha A-S301 {runId}`, lalu aset `Bor Listrik Bosch GSB 550 {runId}`, lalu aset `Kamera Canon EOS 90D {runId}`, lalu aset `Tablet Samsung Tab S8 {runId}`, lalu aset `Tripod Manfrotto 290 {runId}`, lalu aset `Proyektor BenQ MH535 {runId}` (urutan status kebalikan)
152. Klik header kolom `TAG`
153. Verifikasi urutan baris dari atas ke bawah: aset `Kamera Canon EOS 90D {runId}`, lalu aset `Bor Listrik Bosch GSB 550 {runId}`, lalu aset `Proyektor BenQ MH535 {runId}`, lalu aset `Amplifier Yamaha A-S301 {runId}` (TAG `NFC`, Non TAG, `QR`, lalu `RFID`)
154. Klik header kolom `TAG`
155. Verifikasi urutan baris dari atas ke bawah: aset `Amplifier Yamaha A-S301 {runId}`, lalu aset `Proyektor BenQ MH535 {runId}`, lalu aset `Bor Listrik Bosch GSB 550 {runId}`, lalu aset `Kamera Canon EOS 90D {runId}` (TAG `RFID`, `QR`, Non TAG, lalu `NFC`)
156. Klik header kolom `Category`
157. Verifikasi urutan baris dari atas ke bawah: aset `Amplifier Yamaha A-S301 {runId}`, lalu aset `Kamera Canon EOS 90D {runId}`, lalu aset `Bor Listrik Bosch GSB 550 {runId}`, lalu aset `Tablet Samsung Tab S8 {runId}` (Category `Audio`, `Kamera`, `Perkakas`, lalu `Tablet`)
158. Klik header kolom `Category`
159. Verifikasi urutan baris dari atas ke bawah: aset `Tablet Samsung Tab S8 {runId}`, lalu aset `Bor Listrik Bosch GSB 550 {runId}`, lalu aset `Kamera Canon EOS 90D {runId}`, lalu aset `Amplifier Yamaha A-S301 {runId}` (Category `Tablet`, `Perkakas`, `Kamera`, lalu `Audio`)
160. Klik header kolom `Due Date`
161. Verifikasi urutan baris dari atas ke bawah: aset `Amplifier Yamaha A-S301 {runId}`, lalu aset `Kamera Canon EOS 90D {runId}`, lalu aset `Proyektor BenQ MH535 {runId}`, lalu aset `Speaker JBL PartyBox 110 {runId}`, lalu aset `Laptop Lenovo ThinkPad T14 {runId}` (Due Date `T0 − 7 hari`, `T0 − 2 hari`, `T0 + 2 hari`, `T0 + 3 hari`, lalu `—`, Oldest First)
162. Klik header kolom `Due Date`
163. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Lenovo ThinkPad T14 {runId}`, lalu aset `Speaker JBL PartyBox 110 {runId}`, lalu aset `Proyektor BenQ MH535 {runId}`, lalu aset `Kamera Canon EOS 90D {runId}`, lalu aset `Amplifier Yamaha A-S301 {runId}` (Due Date `—`, `T0 + 3 hari`, `T0 + 2 hari`, `T0 − 2 hari`, lalu `T0 − 7 hari`, Newest First)
164. Klik header kolom `Handed Over At`
165. Verifikasi urutan baris dari atas ke bawah: aset `Amplifier Yamaha A-S301 {runId}`, lalu aset `Kamera Canon EOS 90D {runId}`, lalu aset `Proyektor BenQ MH535 {runId}`, lalu aset `Speaker JBL PartyBox 110 {runId}`, lalu aset `Laptop Lenovo ThinkPad T14 {runId}` (Handed Over At `T0 − 11 hari`, `T0 − 6 hari`, `T0 − 3 hari`, `T0 − 2 hari`, lalu `—`, Oldest First)
166. Klik header kolom `Handed Over At`
167. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Lenovo ThinkPad T14 {runId}`, lalu aset `Speaker JBL PartyBox 110 {runId}`, lalu aset `Proyektor BenQ MH535 {runId}`, lalu aset `Kamera Canon EOS 90D {runId}`, lalu aset `Amplifier Yamaha A-S301 {runId}` (Handed Over At `—`, `T0 − 2 hari`, `T0 − 3 hari`, `T0 − 6 hari`, lalu `T0 − 11 hari`, Newest First)
168. Klik header kolom `Returned At`
169. Verifikasi urutan baris dari atas ke bawah: aset `Amplifier Yamaha A-S301 {runId}`, lalu aset `Laptop Lenovo ThinkPad T14 {runId}` (Returned At `T0 − 5 hari` sebelum `—`, Oldest First)
170. Klik header kolom `Returned At`
171. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Lenovo ThinkPad T14 {runId}`, lalu aset `Amplifier Yamaha A-S301 {runId}` (Returned At `—` sebelum `T0 − 5 hari`, Newest First)
172. Klik header kolom `Duration`
173. Verifikasi urutan baris dari atas ke bawah: aset `Tripod Manfrotto 290 {runId}`, lalu aset `Printer Epson L3250 {runId}`, lalu aset `Bor Listrik Bosch GSB 550 {runId}`, lalu aset `Laptop Lenovo ThinkPad T14 {runId}`, lalu aset `Amplifier Yamaha A-S301 {runId}`, lalu aset `Proyektor BenQ MH535 {runId}` (Duration `36 hours`, `2 days`, `3 days`, `4 days`, `5 days`, lalu `6 days`, dihitung dalam jam)
174. Klik header kolom `Duration`
175. Verifikasi urutan baris dari atas ke bawah: aset `Proyektor BenQ MH535 {runId}`, lalu aset `Amplifier Yamaha A-S301 {runId}`, lalu aset `Laptop Lenovo ThinkPad T14 {runId}`, lalu aset `Bor Listrik Bosch GSB 550 {runId}`, lalu aset `Printer Epson L3250 {runId}`, lalu aset `Tripod Manfrotto 290 {runId}` (Duration `6 days`, `5 days`, `4 days`, `3 days`, `2 days`, lalu `36 hours`)
176. Klik header kolom `Extensions`
177. Verifikasi urutan baris dari atas ke bawah: aset `Proyektor BenQ MH535 {runId}`, lalu aset `Kamera Canon EOS 90D {runId}` (Extensions `0 / 3` sebelum `1 / 3`)
178. Klik header kolom `Extensions`
179. Verifikasi urutan baris dari atas ke bawah: aset `Kamera Canon EOS 90D {runId}`, lalu aset `Proyektor BenQ MH535 {runId}` (Extensions `1 / 3` sebelum `0 / 3`)
180. Klik header kolom `Approval`
181. Verifikasi urutan baris dari atas ke bawah: aset `Proyektor BenQ MH535 {runId}`, lalu aset `Laptop Lenovo ThinkPad T14 {runId}`, lalu aset `Bor Listrik Bosch GSB 550 {runId}`, lalu aset `Printer Epson L3250 {runId}`, lalu aset `Tripod Manfrotto 290 {runId}` (Approval `Approved`, `Auto-approved`, `Rejected`, `Waiting`, lalu `—`)
182. Klik header kolom `Approval`
183. Verifikasi urutan baris dari atas ke bawah: aset `Tripod Manfrotto 290 {runId}`, lalu aset `Printer Epson L3250 {runId}`, lalu aset `Bor Listrik Bosch GSB 550 {runId}`, lalu aset `Laptop Lenovo ThinkPad T14 {runId}`, lalu aset `Proyektor BenQ MH535 {runId}` (Approval `—`, `Waiting`, `Rejected`, `Auto-approved`, lalu `Approved`)
184. Klik header kolom `Reason`
185. Verifikasi urutan baris dari atas ke bawah: aset `Bor Listrik Bosch GSB 550 {runId}`, lalu aset `Tripod Manfrotto 290 {runId}`, lalu aset `Amplifier Yamaha A-S301 {runId}` (Reason `Stok sedang dikalibrasi`, `Timed out (Waiting for Approval)`, lalu `—`)
186. Klik header kolom `Reason`
187. Verifikasi urutan baris dari atas ke bawah: aset `Amplifier Yamaha A-S301 {runId}`, lalu aset `Tripod Manfrotto 290 {runId}`, lalu aset `Bor Listrik Bosch GSB 550 {runId}` (Reason `—`, `Timed out (Waiting for Approval)`, lalu `Stok sedang dikalibrasi`)
188. Klik header kolom `Purpose`
189. Verifikasi urutan baris dari atas ke bawah: aset `Kamera Canon EOS 90D {runId}`, lalu aset `Amplifier Yamaha A-S301 {runId}`, lalu aset `Laptop Lenovo ThinkPad T14 {runId}`, lalu aset `Bor Listrik Bosch GSB 550 {runId}` (Purpose `Dokumentasi`, `Konser amal`, `Pelatihan karyawan`, lalu `Renovasi ruang rapat`)
190. Klik header kolom `Purpose`
191. Verifikasi urutan baris dari atas ke bawah: aset `Bor Listrik Bosch GSB 550 {runId}`, lalu aset `Laptop Lenovo ThinkPad T14 {runId}`, lalu aset `Amplifier Yamaha A-S301 {runId}`, lalu aset `Kamera Canon EOS 90D {runId}` (Purpose `Renovasi ruang rapat`, `Pelatihan karyawan`, `Konser amal`, lalu `Dokumentasi`)
192. Klik header kolom `Handed Over By`
193. Verifikasi urutan baris dari atas ke bawah: aset `Amplifier Yamaha A-S301 {runId}`, lalu aset `Kamera Canon EOS 90D {runId}`, lalu aset `Laptop Lenovo ThinkPad T14 {runId}` (Handed Over By `Agus P`, `Rina W`, lalu `—`)
194. Klik header kolom `Handed Over By`
195. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Lenovo ThinkPad T14 {runId}`, lalu aset `Kamera Canon EOS 90D {runId}`, lalu aset `Amplifier Yamaha A-S301 {runId}` (Handed Over By `—`, `Rina W`, lalu `Agus P`)

### Search mencocokkan nilai kolom tabel Assets
196. Ganti isi kotak search dengan `Tripod`, tekan Enter
197. Verifikasi baris aset `Tripod Manfrotto 290 {runId}` tampil
198. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
199. Ganti isi kotak search dengan Asset ID aset `Amplifier Yamaha A-S301 {runId}`, tekan Enter
200. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tampil
201. Verifikasi baris aset `Bor Listrik Bosch GSB 550 {runId}` tidak tampil
202. Ganti isi kotak search dengan `Canon`, tekan Enter
203. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` tampil
204. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
205. Ganti isi kotak search dengan `L3250`, tekan Enter
206. Verifikasi baris aset `Printer Epson L3250 {runId}` tampil
207. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
208. Ganti isi kotak search dengan `Rejected`, tekan Enter
209. Verifikasi baris aset `Bor Listrik Bosch GSB 550 {runId}` tampil
210. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
211. Ganti isi kotak search dengan `Perkakas`, tekan Enter
212. Verifikasi baris aset `Bor Listrik Bosch GSB 550 {runId}` tampil
213. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
214. Ganti isi kotak search dengan `36 hours`, tekan Enter
215. Verifikasi baris aset `Tripod Manfrotto 290 {runId}` tampil
216. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
217. Ganti isi kotak search dengan `1 / 3`, tekan Enter
218. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` tampil
219. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
220. Ganti isi kotak search dengan `Auto-approved`, tekan Enter
221. Verifikasi baris aset `Laptop Lenovo ThinkPad T14 {runId}` tampil
222. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
223. Ganti isi kotak search dengan `Stok sedang dikalibrasi`, tekan Enter
224. Verifikasi baris aset `Bor Listrik Bosch GSB 550 {runId}` tampil
225. Verifikasi baris aset `Tripod Manfrotto 290 {runId}` tidak tampil
226. Ganti isi kotak search dengan `Konser amal`, tekan Enter
227. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tampil
228. Verifikasi baris aset `Bor Listrik Bosch GSB 550 {runId}` tidak tampil
229. Ganti isi kotak search dengan `Rina W`, tekan Enter
230. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` tampil
231. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
232. Ganti isi kotak search dengan `NFC`, tekan Enter
233. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` tampil
234. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
235. Klik `(←)` pada kotak Search

### Filter Panel tabel Assets menerapkan saringan per field
236. Klik `Filter`
237. Klik field `Asset Name`
238. Pilih opsi `Tripod Manfrotto 290 {runId}`
239. Klik `[Apply]`
240. Verifikasi baris aset `Tripod Manfrotto 290 {runId}` tampil
241. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
242. Klik `[Clear Field]`
243. Klik field `Brand`
244. Pilih opsi `Canon`
245. Klik `[Apply]`
246. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` tampil
247. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
248. Klik `[Clear Field]`
249. Klik field `Model/Type`
250. Pilih opsi `L3250`
251. Klik `[Apply]`
252. Verifikasi baris aset `Printer Epson L3250 {runId}` tampil
253. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
254. Klik `[Clear Field]`
255. Klik field `Status`
256. Pilih opsi `Rejected`
257. Klik `[Apply]`
258. Verifikasi baris aset `Bor Listrik Bosch GSB 550 {runId}` tampil
259. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
260. Klik `[Clear Field]`
261. Klik field `TAG`
262. Pilih opsi `NFC`
263. Klik `[Apply]`
264. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` tampil
265. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
266. Klik `[Clear Field]`
267. Klik field `Category`
268. Pilih node `Perkakas`
269. Klik `[Apply]`
270. Verifikasi baris aset `Bor Listrik Bosch GSB 550 {runId}` tampil
271. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
272. Klik `[Clear Field]`
273. Klik field `Due Date`
274. Pilih rentang tanggal dari `T0 + 1 hari` sampai `T0 + 3 hari`
275. Klik `[Apply]`
276. Verifikasi baris aset `Proyektor BenQ MH535 {runId}` tampil
277. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` tidak tampil
278. Klik `[Clear Field]`
279. Klik field `Handed Over At`
280. Pilih rentang tanggal dari `T0 − 12 hari` sampai `T0 − 10 hari`
281. Klik `[Apply]`
282. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tampil
283. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` tidak tampil
284. Klik `[Clear Field]`
285. Klik field `Returned At`
286. Pilih rentang tanggal dari `T0 − 6 hari` sampai `T0 − 4 hari`
287. Klik `[Apply]`
288. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tampil
289. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` tidak tampil
290. Klik `[Clear Field]`
291. Klik field `Extensions`
292. Isi `Min` dengan `1`
293. Isi `Max` dengan `1`
294. Klik `[Apply]`
295. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` tampil
296. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
297. Klik `[Clear Field]`
298. Klik field `Approval`
299. Pilih opsi `Auto-approved`
300. Klik `[Apply]`
301. Verifikasi baris aset `Laptop Lenovo ThinkPad T14 {runId}` tampil
302. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil
303. Klik `[Clear Field]`
304. Klik field `Handed Over By`
305. Pilih opsi `Rina W`
306. Klik `[Apply]`
307. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` tampil
308. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` tidak tampil

### Download mengikuti saringan dan tersedia dalam CSV dan XLSX
309. Klik `[Clear Field]`
310. Klik field `Brand`
311. Pilih opsi `Canon`
312. Pilih opsi `Yamaha`
313. Klik `[Apply]`
314. Klik `Download`
315. Pilih `Download as CSV`
316. Verifikasi berkas terunduh dengan nama `Borrow-Assets` dan ekstensi `.csv`
317. Verifikasi berkas memuat 2 baris data sesuai saringan Brand
318. Klik `Download`
319. Pilih `Download as XLSX`
320. Verifikasi berkas terunduh dengan nama `Borrow-Assets` dan ekstensi `.xlsx`
321. Klik `[Clear Field]`
322. Klik `[Apply]`

### Baris info Approval, penanda header, dan tombol Hand Over pada BRW tanpa approval
323. Kembali ke tab Transactions lewat segmen Origin Tab pada breadcrumb
324. Klik Transaction ID baris Borrower `Kirana P`
325. Verifikasi baris info `Approval` menampilkan `All assets in this borrow were approved automatically.`
326. Verifikasi judul halaman memuat badge status `Waiting for Handover`
327. Verifikasi judul halaman tidak memuat badge `Overdue` karena BRW tidak memiliki baris Overdue
328. Verifikasi tombol `[Hand Over]` dan `[Cancel Borrow]` tampil di bawah tabel
329. Verifikasi tombol `[Return]` dan `[Request Extension]` tidak tampil di bawah tabel karena tidak ada baris Borrowed maupun Overdue
330. Klik `[Hand Over]` di bawah tabel
331. Verifikasi halaman Handover terbuka dengan aset `Mikrofon Shure SM7B {runId}` dan `Headset Sennheiser HD 280 {runId}`
332. Kembali ke tab Transactions lewat segmen Origin Tab pada breadcrumb
333. Klik Transaction ID baris Borrower `Lukman H`
334. Verifikasi baris info `Approval` menampilkan `No approval needed`
335. Kembali ke tab Transactions lewat segmen Origin Tab pada breadcrumb
336. Klik Transaction ID baris Borrower `Rani W`
337. Verifikasi baris info `Approval` menampilkan `No approval needed` karena baris berstatus `Self-service`
338. Kembali ke tab Transactions lewat segmen Origin Tab pada breadcrumb
339. Klik Transaction ID baris Borrower `Satria N`
340. Verifikasi tabel Assets memuat aset `Gimbal Zhiyun Crane 2 {runId}` dan `Tripod Velbon EX 330 {runId}`
341. Verifikasi baris info `Approval` tidak tampil karena baris `Auto-approved` dan `Not required` bercampur
342. Kembali ke tab Transactions lewat segmen Origin Tab pada breadcrumb
343. Klik Transaction ID baris Borrower `Sari U`
344. Verifikasi header menampilkan Borrower `Sari U` dengan penanda `PIC` untuk Borrower tanpa akun
345. Kembali ke tab Transactions lewat segmen Origin Tab pada breadcrumb
346. Klik Transaction ID baris Borrower `Teguh S`
347. Verifikasi header menampilkan Borrower `Teguh S` dengan penanda `No PIC`

### Alert aset yang ditemukan pada Borrow Detail BRW asal
348. Kembali ke tab Transactions lewat segmen Origin Tab pada breadcrumb
349. Klik tab `History`
350. Ketik Search `{runId}`, tekan Enter
351. Klik Transaction ID baris Borrower `Nanda P`
352. Verifikasi Alert `This asset was found. If Nanda Prakoso still holds it, create a new borrow to record it.` tampil di atas tabel Assets
353. Verifikasi tombol `[Cancel Borrow]`, `[Request Extension]`, `[Return]`, dan `[Hand Over]` tidak tampil di bawah tabel karena tidak ada baris yang memenuhi syaratnya

### Alert aset yang ditemukan: bentuk jamak, tidak dapat ditutup, dan hilang
354. Verifikasi Alert tidak memiliki tombol tutup
355. Kembali ke tab History lewat segmen Origin Tab pada breadcrumb
356. Klik Transaction ID baris Borrower `Oki F`
357. Verifikasi Alert `2 assets were found. If Oki Firmansyah still holds them, create a new borrow to record them.` tampil di atas tabel Assets
358. Kembali ke tab History lewat segmen Origin Tab pada breadcrumb
359. Klik Transaction ID baris Borrower `Putri A`
360. Verifikasi tabel Assets memuat aset `Walkie Talkie Motorola T82 {runId}`
361. Verifikasi Alert tidak tampil karena aset `Walkie Talkie Motorola T82 {runId}` sudah berada di BRW aktif
362. Masuk sebagai `Monitor Borrow {runId}`
363. Klik tab `History`
364. Ketik Search `{runId}`, tekan Enter
365. Klik Transaction ID baris Borrower `Nanda P`
366. Verifikasi tabel Assets memuat aset `Drone DJI Air 3 {runId}`
367. Verifikasi Alert tidak tampil bagi aktor yang bukan Aktor Borrow
368. Verifikasi tombol `Download` tampil di toolbar tabel Assets

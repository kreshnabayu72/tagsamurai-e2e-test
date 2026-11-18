---
id: TC-FA-BORROW-E2E-009-borrow-detail
title: "Borrow Detail menampilkan header BRW dan tabel Assets dengan aksi baris menurut status"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1c#p1", "§4.1c#r1", "§4.1c#r2", "§4.1c#r3", "§4.1c#r4", "§4.1c#r5", "§4.1c#r6", "§4.1c#r7", "§4.1c#r8", "§4.1c#r9", "§4.1c#r10", "§4.1c#r11", "§4.1c#r12", "§4.1c#r13", "§4.1c#r14", "§4.1c#r15", "§4.1c#r16", "§4.1c#r17", "§4.1c#r18", "§4.1c#r19", "§4.1c#p4", "§4.1c#r20", "§4.1c#r21", "§4.1c#r22", "§4.1c#r23", "§4.1c#r24", "§4.1c#r25", "§4.1c#r26", "§4.1c#r27", "§4.1c#r28", "§4.1c#r29", "§4.1c#r30", "§4.1c#r31", "§4.2#p5", "§4.2.4#p1", "§4.2.4#p2"]
smoke: []
dependsOn: []
trace:
  "§4.1c#p1": [9, 12]
  "§4.1c#r1": [15, 16]
  "§4.1c#r2": [13]
  "§4.1c#r3": [17]
  "§4.1c#r4": [18]
  "§4.1c#r5": [19]
  "§4.1c#r6": [20, 21, 22, 23]
  "§4.1c#r7": [33]
  "§4.1c#r8": [35]
  "§4.1c#r9": [24, 25]
  "§4.1c#r10": [37]
  "§4.1c#r11": [39, 40]
  "§4.1c#r12": [26]
  "§4.1c#r13": [42]
  "§4.1c#r14": [27, 28]
  "§4.1c#r15": [44]
  "§4.1c#r16": [29, 30]
  "§4.1c#r17": [29, 30]
  "§4.1c#r18": [46]
  "§4.1c#r19": [48]
  "§4.1c#p4": [50]
  "§4.1c#r20": [50, 71, 75]
  "§4.1c#r21": [50, 71, 79]
  "§4.1c#r22": [50, 54, 71, 108]
  "§4.1c#r23": [50, 54, 83]
  "§4.1c#r24": [51, 57, 61, 65, 112]
  "§4.1c#r25": [51, 57, 61, 64, 71, 116]
  "§4.1c#r26": [51, 57, 61, 65, 86]
  "§4.1c#r27": [51, 57, 61, 64, 90]
  "§4.1c#r28": [51, 64, 94]
  "§4.1c#r29": [51, 68, 98, 100]
  "§4.1c#r30": [50, 54, 58, 71, 103, 105]
  "§4.1c#r31": [122]
  "§4.2#p5": [9]
  "§4.2.4#p1": [3, 4, 6, 7, 8, 11]
  "§4.2.4#p2": [10, 118, 119, 125, 128, 132]
anchor: []
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
  - DU-009-2: BRW Borrower `Joko Susilo` (tampil `Joko S`), Group `Head Office`, pengaju `Agus P`, Note `Peminjaman untuk kegiatan pelatihan`, status header `Waiting for Handover` dengan penanda `Overdue`. Sembilan baris:
    - `Amplifier Yamaha A-S301 {runId}`: Returned (Brand `Yamaha`, Model/Type `A-S301`, Category `Audio`, TAG RFID, Duration `5 days`, Due Date `T0 − 7 hari`, Handed Over At `T0 − 11 hari`, Returned At `T0 − 5 hari`, Approval `Approved`, Extensions `0 / 3`, Purpose `Konser amal`, Handed Over By `Agus P`, foto handover dan foto return tersimpan).
    - `Bor Listrik Bosch GSB 550 {runId}`: Rejected (Brand `Bosch`, Model/Type `GSB 550`, Category `Perkakas`, Non TAG, Duration `3 days`, Approval `Rejected`, Reason `Stok sedang dikalibrasi`, Purpose `Renovasi ruang rapat`).
    - `Kamera Canon EOS 90D {runId}`: Overdue (Brand `Canon`, Model/Type `EOS 90D`, Category `Kamera`, TAG NFC, Duration `5 days`, Due Date `T0 − 2 hari`, Handed Over At `T0 − 6 hari`, Approval `Approved`, Extensions `0 / 3`, Purpose `Dokumentasi`, Handed Over By `Agus P`).
    - `Laptop Lenovo ThinkPad T14 {runId}`: Waiting for Handover (Brand `Lenovo`, Model/Type `ThinkPad T14`, Category `Laptop`, TAG RFID, Duration `4 days`, Approval `Auto-approved`, Purpose `Pelatihan karyawan`).
    - `Printer Epson L3250 {runId}`: Waiting for Approval (Brand `Epson`, Model/Type `L3250`, Category `Printer`, Non TAG, Duration `2 days`, Approval `Waiting`).
    - `Proyektor BenQ MH535 {runId}`: Borrowed (Brand `BenQ`, Model/Type `MH535`, Category `Proyektor`, TAG QR, Duration `6 days`, Due Date `T0 + 3 hari`, Handed Over At `T0 − 3 hari`, Approval `Approved`, Extensions `0 / 3`, Handed Over By `Agus P`).
    - `Speaker JBL PartyBox 110 {runId}`: Borrowed dengan Damage Report berstatus Waiting for Confirmation yang dilaporkan `Admin Borrow {runId}` (badge `Reported Damaged`, Brand `JBL`, Model/Type `PartyBox 110`, Category `Audio`, TAG QR, Duration `6 days`, Due Date `T0 + 3 hari`).
    - `Tablet Samsung Tab S8 {runId}`: Borrowed dengan pengajuan Extend yang menunggu approval (tampil `Extension Approval`, Brand `Samsung`, Model/Type `Tab S8`, Category `Tablet`, TAG NFC, Duration `6 days`, Due Date `T0 + 3 hari`).
    - `Tripod Manfrotto 290 {runId}`: Canceled oleh System (Brand `Manfrotto`, Model/Type `290`, Category `Tripod`, Non TAG, Duration `3 days`, Reason `Timed out (Waiting for Approval)`).
  - DU-009-3: BRW Borrower `Kirana Putri` (tampil `Kirana P`), Group `Head Office`, satu aset `Mikrofon Shure SM7B {runId}` berstatus Waiting for Handover dengan Approval `Auto-approved`.
  - DU-009-4: BRW Borrower `Lukman Hakim` (tampil `Lukman H`), Group `Head Office`, satu aset `Lampu Studio Godox SL60 {runId}` berstatus Waiting for Handover dengan Approval `Not required`.
  - DU-009-5: BRW Returned, Borrower `Nanda Prakoso` (tampil `Nanda P`), Group `Head Office`, satu aset `Drone DJI Air 3 {runId}` berstatus Returned dengan penanda `Missing` yang kemudian ditemukan dan berstatus Available di luar BRW aktif.
- Kondisi:
  - Date Format dan Time Format di General Settings entitas berlaku untuk tampilan tanggal.
  - Max extensions efektif seluruh aset pada spec ini bernilai `3`.

## Test Steps

### Borrow Detail dibuka dari Transaction ID dan header BRW
1. Ketik Search `{runId}`, tekan Enter
2. Klik Transaction ID baris Borrower `Joko S`
3. Verifikasi breadcrumb memuat `Transactions > Borrow > Transactions > Detail`
4. Verifikasi judul halaman memuat Transaction ID BRW milik DU-009-2, badge status `Waiting for Handover`, dan badge `Overdue`
5. Klik tombol copy pada judul
6. Verifikasi toast `Success, Transaction ID has been copied.` tampil
7. Verifikasi header menampilkan Requested By `Agus P` beserta tanggal request, Borrower `Joko S`, Group `Head Office`, Note `Peminjaman untuk kegiatan pelatihan`, dan Last Updated
8. Verifikasi header tidak memuat Purpose maupun Due date
9. Verifikasi halaman tidak memiliki tab dan tidak memiliki judul `Assets`
10. Verifikasi baris info `Approval` tidak tampil karena baris BRW tidak seluruhnya tanpa approval
11. Verifikasi toolbar tabel memuat `Search by Scan`, `Search`, `Filter`, dan `Download` tanpa menu `⋯`
12. Verifikasi tabel Assets memuat 9 baris dengan aset `Amplifier Yamaha A-S301 {runId}`, `Bor Listrik Bosch GSB 550 {runId}`, `Kamera Canon EOS 90D {runId}`, `Laptop Lenovo ThinkPad T14 {runId}`, `Printer Epson L3250 {runId}`, `Proyektor BenQ MH535 {runId}`, `Speaker JBL PartyBox 110 {runId}`, `Tablet Samsung Tab S8 {runId}`, dan `Tripod Manfrotto 290 {runId}`

### Isi kolom yang tampil sejak awal
13. Verifikasi urutan baris dari atas ke bawah mengikuti Name A–Z: `Amplifier Yamaha A-S301 {runId}`, `Bor Listrik Bosch GSB 550 {runId}`, `Kamera Canon EOS 90D {runId}`, `Laptop Lenovo ThinkPad T14 {runId}`, `Printer Epson L3250 {runId}`, `Proyektor BenQ MH535 {runId}`, `Speaker JBL PartyBox 110 {runId}`, `Tablet Samsung Tab S8 {runId}`, lalu `Tripod Manfrotto 290 {runId}`
14. Klik header kolom `Photo`
15. Verifikasi urutan baris tidak berubah setelah header `Photo` diklik
16. Verifikasi tabel Assets tidak memuat kolom `Transaction ID`, `Group`, dan `Borrower`
17. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan Asset ID milik aset itu
18. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan Brand `Yamaha` dan baris aset `Kamera Canon EOS 90D {runId}` menampilkan Brand `Canon`
19. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan Model/Type `A-S301` dan baris aset `Kamera Canon EOS 90D {runId}` menampilkan Model/Type `EOS 90D`
20. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan status `Returned`, baris aset `Bor Listrik Bosch GSB 550 {runId}` menampilkan status `Rejected`, dan baris aset `Tripod Manfrotto 290 {runId}` menampilkan status `Canceled`
21. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` menampilkan status `Overdue`, baris aset `Laptop Lenovo ThinkPad T14 {runId}` menampilkan status `Waiting for Handover`, dan baris aset `Printer Epson L3250 {runId}` menampilkan status `Waiting for Approval`
22. Verifikasi baris aset `Proyektor BenQ MH535 {runId}` menampilkan status `Borrowed` dan baris aset `Tablet Samsung Tab S8 {runId}` menampilkan status `Extension Approval`
23. Verifikasi baris aset `Speaker JBL PartyBox 110 {runId}` menampilkan status `Borrowed` dan badge `Reported Damaged`
24. Verifikasi baris aset `Proyektor BenQ MH535 {runId}` menampilkan Due Date `T0 + 3 hari` dan baris aset `Laptop Lenovo ThinkPad T14 {runId}` menampilkan `—` sebelum handover
25. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` menampilkan Due Date `T0 − 2 hari` sebagai Overdue
26. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan Duration `5 days` dan baris aset `Laptop Lenovo ThinkPad T14 {runId}` menampilkan Duration `4 days`
27. Verifikasi baris aset `Printer Epson L3250 {runId}` menampilkan Approval `Waiting`, baris aset `Proyektor BenQ MH535 {runId}` menampilkan `Approved`, dan baris aset `Laptop Lenovo ThinkPad T14 {runId}` menampilkan `Auto-approved`
28. Verifikasi baris aset `Bor Listrik Bosch GSB 550 {runId}` menampilkan Approval `Rejected` dan baris aset `Tripod Manfrotto 290 {runId}` menampilkan `—`
29. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan thumbnail Handover Photo dan thumbnail Return Photo
30. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` menampilkan `—` pada Handover Photo dan Return Photo

### Isi kolom tambahan yang ditampilkan lewat Column Visibility
31. Klik header kolom Actions `⋯`
32. Centang `TAG` pada panel Column Visibility
33. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan ikon TAG `RFID` dan baris aset `Printer Epson L3250 {runId}` menampilkan `—`
34. Centang `Category` pada panel Column Visibility
35. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan Category `Audio` dan baris aset `Kamera Canon EOS 90D {runId}` menampilkan Category `Kamera`
36. Centang `Handed Over At` pada panel Column Visibility
37. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan Handed Over At `T0 − 11 hari` dan baris aset `Printer Epson L3250 {runId}` menampilkan `—`
38. Centang `Returned At` pada panel Column Visibility
39. Verifikasi baris aset `Amplifier Yamaha A-S301 {runId}` menampilkan Returned At `T0 − 5 hari` dengan `late 2 days`
40. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` menampilkan `—` pada Returned At
41. Centang `Extensions` pada panel Column Visibility
42. Verifikasi baris aset `Proyektor BenQ MH535 {runId}` menampilkan Extensions `0 / 3`
43. Centang `Reason` pada panel Column Visibility
44. Verifikasi baris aset `Bor Listrik Bosch GSB 550 {runId}` menampilkan Reason `Stok sedang dikalibrasi` apa adanya dan baris aset `Tripod Manfrotto 290 {runId}` menampilkan Reason `Timed out (Waiting for Approval)`
45. Centang `Purpose` pada panel Column Visibility
46. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` menampilkan Purpose `Dokumentasi` dan baris aset `Laptop Lenovo ThinkPad T14 {runId}` menampilkan Purpose `Pelatihan karyawan`
47. Centang `Handed Over By` pada panel Column Visibility
48. Verifikasi baris aset `Kamera Canon EOS 90D {runId}` menampilkan Handed Over By `Agus P` dan baris aset `Laptop Lenovo ThinkPad T14 {runId}` menampilkan `—`

### Aksi baris menurut status baris
49. Klik `⋯` pada baris aset `Laptop Lenovo ThinkPad T14 {runId}`
50. Verifikasi menu baris tabel Assets memuat `Borrow Log`, `Transaction Rules`, `Hand Over`, `Remind Borrower`, dan `Cancel Borrow`
51. Verifikasi menu baris tabel Assets tidak memuat `Request Extension`, `Return`, `Report Damaged`, `Report Missing`, `Cancel Damage Report`, dan `Cancel Extension`
52. Tutup menu baris
53. Klik `⋯` pada baris aset `Printer Epson L3250 {runId}`
54. Verifikasi menu baris tabel Assets memuat `Cancel Borrow` dan tidak memuat `Hand Over` maupun `Remind Borrower`
55. Tutup menu baris
56. Klik `⋯` pada baris aset `Proyektor BenQ MH535 {runId}`
57. Verifikasi menu baris tabel Assets memuat `Request Extension`, `Return`, `Report Damaged`, dan `Report Missing`
58. Verifikasi menu baris tabel Assets tidak memuat `Cancel Borrow`
59. Tutup menu baris
60. Klik `⋯` pada baris aset `Kamera Canon EOS 90D {runId}`
61. Verifikasi menu baris tabel Assets memuat `Request Extension`, `Return`, `Report Damaged`, dan `Report Missing` untuk baris Overdue
62. Tutup menu baris
63. Klik `⋯` pada baris aset `Speaker JBL PartyBox 110 {runId}`
64. Verifikasi menu baris tabel Assets memuat `Return`, `Report Missing`, dan `Cancel Damage Report`
65. Verifikasi menu baris tabel Assets tidak memuat `Request Extension` dan `Report Damaged`
66. Tutup menu baris
67. Klik `⋯` pada baris aset `Tablet Samsung Tab S8 {runId}`
68. Verifikasi menu baris tabel Assets memuat `Cancel Extension`
69. Tutup menu baris
70. Klik `⋯` pada baris aset `Tripod Manfrotto 290 {runId}`
71. Verifikasi menu baris tabel Assets memuat `Borrow Log` dan `Transaction Rules` dan tidak memuat `Cancel Borrow`, `Return`, maupun `Hand Over`
72. Tutup menu baris

### Aksi baris membuka dialog atau halaman yang sesuai
73. Klik `⋯` pada baris aset `Amplifier Yamaha A-S301 {runId}`
74. Klik `Borrow Log`
75. Verifikasi dialog Borrow Log terbuka untuk aset `Amplifier Yamaha A-S301 {runId}`
76. Tutup dialog Borrow Log
77. Klik `⋯` pada baris aset `Amplifier Yamaha A-S301 {runId}`
78. Klik `Transaction Rules`
79. Verifikasi dialog `Transaction Rules` terbuka untuk aset `Amplifier Yamaha A-S301 {runId}`
80. Tutup dialog `Transaction Rules`
81. Klik `⋯` pada baris aset `Laptop Lenovo ThinkPad T14 {runId}`
82. Klik `Remind Borrower`
83. Verifikasi toast `Success, reminder has been sent to Joko Susilo.` tampil dan baris aset `Laptop Lenovo ThinkPad T14 {runId}` tetap berstatus `Waiting for Handover`
84. Klik `⋯` pada baris aset `Proyektor BenQ MH535 {runId}`
85. Klik `Report Damaged`
86. Verifikasi dialog `Report Damaged` terbuka untuk aset `Proyektor BenQ MH535 {runId}`
87. Tutup dialog `Report Damaged` tanpa menyimpan
88. Klik `⋯` pada baris aset `Proyektor BenQ MH535 {runId}`
89. Klik `Report Missing`
90. Verifikasi dialog `Report Missing` terbuka untuk aset `Proyektor BenQ MH535 {runId}`
91. Tutup dialog `Report Missing` tanpa menyimpan
92. Klik `⋯` pada baris aset `Speaker JBL PartyBox 110 {runId}`
93. Klik `Cancel Damage Report`
94. Verifikasi dialog Cancel Damage Report terbuka untuk aset `Speaker JBL PartyBox 110 {runId}`
95. Tutup dialog Cancel Damage Report tanpa mengonfirmasi
96. Klik `⋯` pada baris aset `Tablet Samsung Tab S8 {runId}`
97. Klik `Cancel Extension`
98. Verifikasi dialog `Cancel Extension` terbuka
99. Klik `[Go Back]` pada dialog
100. Verifikasi baris aset `Tablet Samsung Tab S8 {runId}` tetap menampilkan status `Extension Approval`
101. Klik `⋯` pada baris aset `Printer Epson L3250 {runId}`
102. Klik `Cancel Borrow`
103. Verifikasi dialog `Cancel Borrow` terbuka tanpa field Reason
104. Klik `[Go Back]` pada dialog
105. Verifikasi baris aset `Printer Epson L3250 {runId}` tetap menampilkan status `Waiting for Approval`
106. Klik `⋯` pada baris aset `Laptop Lenovo ThinkPad T14 {runId}`
107. Klik `Hand Over`
108. Verifikasi halaman Handover terbuka hanya untuk aset `Laptop Lenovo ThinkPad T14 {runId}`
109. Kembali ke Borrow Detail lewat breadcrumb
110. Klik `⋯` pada baris aset `Proyektor BenQ MH535 {runId}`
111. Klik `Request Extension`
112. Verifikasi halaman `Extension Request` terbuka hanya untuk aset `Proyektor BenQ MH535 {runId}`
113. Kembali ke Borrow Detail lewat breadcrumb
114. Klik `⋯` pada baris aset `Proyektor BenQ MH535 {runId}`
115. Klik `Return`
116. Verifikasi halaman `Return Asset` terbuka hanya untuk aset `Proyektor BenQ MH535 {runId}`
117. Kembali ke Borrow Detail lewat breadcrumb

### Tombol aksi di bawah tabel dan Download
118. Verifikasi tombol `[Cancel Borrow]`, `[Request Extension]`, `[Return]`, dan `[Hand Over]` tampil di bawah tabel
119. Verifikasi tombol `[Review]` tidak tampil karena tidak ada pengajuan Extend yang menunggu review
120. Klik `Download`
121. Pilih `Download as CSV`
122. Verifikasi berkas terunduh dengan nama `Borrow-Assets` dan memuat 9 baris data

### Baris info Approval pada BRW tanpa approval
123. Kembali ke tab Transactions lewat segmen Origin Tab pada breadcrumb
124. Klik Transaction ID baris Borrower `Kirana P`
125. Verifikasi baris info `Approval` menampilkan `All assets in this borrow were approved automatically.`
126. Kembali ke tab Transactions lewat segmen Origin Tab pada breadcrumb
127. Klik Transaction ID baris Borrower `Lukman H`
128. Verifikasi baris info `Approval` menampilkan `No approval needed`

### Alert aset yang ditemukan pada Borrow Detail BRW asal
129. Klik tab `History`
130. Ketik Search `{runId}`, tekan Enter
131. Klik Transaction ID baris Borrower `Nanda P`
132. Verifikasi Alert `This asset was found. If Nanda Prakoso still holds it, create a new borrow to record it.` tampil di atas tabel Assets

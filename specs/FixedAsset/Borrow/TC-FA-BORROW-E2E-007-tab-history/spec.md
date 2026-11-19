---
id: TC-FA-BORROW-E2E-007-tab-history
title: "Tab History menampilkan transaksi dan baris yang sudah selesai dengan rentang awal 90 hari"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1k#p1", "§4.1k#p2", "§4.1k#b1", "§4.1k#b2", "§4.1k#r1", "§4.1k#r2", "§4.1k#r3", "§4.1k#r4", "§4.1k#r5", "§4.1k#r6", "§4.1k#r7", "§4.1k#r8", "§4.1k#r9", "§4.1k#p5", "§4.1k#r10", "§4.1k#r11", "§4.1k#r16", "§4.1k#r17", "§4.1k#r18", "§4.1k#r19", "§4.1k#r20", "§4.1k#r21", "§4.1k#r22", "§4.1k#r23", "§4.1k#r24", "§4.1k#r25", "§4.1k#r26", "§4.1k#r27", "§4.1k#r28", "§4.1k#r29", "§4.1k#r30", "§4.1k#r31", "§4.1k#r32", "§4.1k#r33", "§4.1k#r34", "§4.1k#r35", "§4.1k#p8", "§4.1k#r36", "§4.1k#r37", "§9.5#r6", "§9.5#r17", "EB-SRC-5@tabel-history"]
smoke: []
dependsOn: []
trace:
  "§4.1k#p1": [2, 422, 424]
  "§4.1k#p2": [7, 10, 12, 16, 22]
  "§4.1k#b1": [4, 5, 427]
  "§4.1k#b2": [52, 53, 54]
  "§4.1k#r1": [24, 311, 313, 349, 350]
  "§4.1k#r2": [12, 25, 26, 315, 317, 352, 353, 374, 375]
  "§4.1k#r3": [27, 28, 319, 321, 355, 356, 380, 381]
  "§4.1k#r4": [4, 323, 325, 358, 359, 386, 387]
  "§4.1k#r5": [29, 30, 327, 329, 361, 362, 393, 394, 447, 448, 450, 451]
  "§4.1k#r6": [38, 39, 333, 335, 364, 365, 399, 400]
  "§4.1k#r7": [31, 32, 33, 337, 339, 367, 368, 405, 406]
  "§4.1k#r8": [34, 341, 343, 411, 412]
  "§4.1k#r9": [8, 35, 345, 347, 418, 419]
  "§4.1k#p5": [42]
  "§4.1k#r10": [42, 44]
  "§4.1k#r11": [48, 49, 430, 435]
  "§4.1k#r16": [57]
  "§4.1k#r17": [58, 114, 116, 186, 187, 229, 230]
  "§4.1k#r18": [59, 118, 120, 189, 190]
  "§4.1k#r19": [60, 122, 124, 192, 193, 235, 236]
  "§4.1k#r20": [61, 126, 128, 195, 196, 241, 242]
  "§4.1k#r21": [62, 130, 132, 198, 199, 247, 248]
  "§4.1k#r22": [63, 64, 65, 66, 99, 134, 136, 201, 202, 253, 254]
  "§4.1k#r23": [78, 80, 138, 140, 259, 260]
  "§4.1k#r24": [82, 142, 144, 204, 205, 265, 266]
  "§4.1k#r25": [67, 146, 148, 207, 208, 443]
  "§4.1k#r26": [68, 150, 152, 210, 211, 271, 272]
  "§4.1k#r27": [69, 154, 156, 277, 278]
  "§4.1k#r28": [70, 71, 158, 160, 283, 284]
  "§4.1k#r29": [72, 162, 164, 213, 214, 290, 291]
  "§4.1k#r30": [84, 85, 86, 166, 168, 216, 217]
  "§4.1k#r31": [88, 170]
  "§4.1k#r32": [90, 91, 172]
  "§4.1k#r33": [93, 94, 174, 176, 219, 220, 296, 297]
  "§4.1k#r34": [96, 178, 180, 222, 223]
  "§4.1k#r35": [55, 73, 182, 184, 303, 304]
  "§4.1k#p8": [103]
  "§4.1k#r36": [103, 105]
  "§4.1k#r37": [109, 110, 432, 437]
  "§9.5#r6": [8, 55]
  "§9.5#r17": [6, 10, 16, 18, 20]
  "EB-SRC-5@tabel-history": [75, 78]
anchor: [112, 309]
coverage:
  web: automated
---

# Tab History menampilkan transaksi dan baris yang sudah selesai dengan rentang awal 90 hari

## Prerequisites
- Aktor: Total Control `Admin Borrow {runId}` (DU-007-1), cakupan seluruh client; aktor lain pada kasus Download: Monitoring & Report `Monitor Borrow {runId}` (DU-007-10) dan Read Only `Viewer Borrow {runId}` (DU-007-11), keduanya cakupan seluruh client.
- Layar awal: Transactions > Borrow, tab Transactions.
- Data:
  - DU-007-1: User `Admin Borrow {runId}`, role Total Control, cakupan seluruh client.
  - Pengaju: `Agus Pratama` (Asset Admin, Group penugasan `Head Office`), tampil `Agus P`; `Rina Wulandari` (Total Control, seluruh client), tampil `Rina W`. Seluruh BRW selain DU-007-9 dibuat lewat form Borrow Request (Source `Admin`); DU-007-9 adalah BRW Self-service.
  - DU-007-2: BRW Returned, Borrower `Wahyu Nugroho` (tampil `Wahyu N`), Group `Head Office`, pengaju `Agus P`, Request Date `T0 − 20 hari`, Last Updated `T0 − 15 hari`. Aset `Laptop Asus ExpertBook B1402 {runId}` (Brand `Asus`, Model/Type `B1402`, Category `Laptop`, TAG RFID, alias `Laptop Pelatihan {runId}`, kode TAG `E2003412DF7C-{runId}`, Purpose `Pelatihan karyawan`, Handed Over At `T0 − 19 hari`, Returned At `T0 − 15 hari`, Extensions `0 / 3`, foto handover dan foto return tersimpan) dan `Mouse Logitech M331 {runId}` (Brand `Logitech`, Model/Type `M331`, Category `Aksesoris Komputer`, Non TAG, Returned At `T0 − 15 hari`). Kedua baris Returned, Total Asset `2`.
  - DU-007-3: BRW Returned, Borrower `Yuni Astuti` (tampil `Yuni A`), Group `Head Office`, pengaju `Agus P`, Request Date `T0 − 30 hari`, Last Updated `T0 − 25 hari`. Aset `Kamera Fujifilm X-T30 {runId}` (TAG NFC) berstatus Returned dengan penanda `Damaged`, dan `Tripod Manfrotto Compact {runId}` berstatus Returned. Total Asset `2`.
  - DU-007-4: BRW Rejected, Borrower `Zaki Firmansyah` (tampil `Zaki F`), Group `Head Office`, pengaju `Agus P`, Request Date `T0 − 10 hari`, Last Updated `T0 − 9 hari`. Aset `Proyektor BenQ MH550 {runId}` berstatus Rejected dengan Reason `Anggaran belum disetujui`. Total Asset `1`.
  - DU-007-5: BRW Canceled, Borrower `Ayu Lestari` (tampil `Ayu L`), Group `Branch Surabaya`, pengaju `Rina W`, Request Date `T0 − 8 hari`, Last Updated `T0 − 7 hari`. Aset `Speaker Bose S1 Pro {runId}` berstatus Canceled oleh System dengan Reason `Timed out (Waiting for Approval)`, dan `Mikrofon Shure SM58 {runId}` berstatus Canceled manual tanpa Reason. Total Asset `2`.
  - DU-007-6: BRW Returned terlambat, Borrower `Bagas Pratama` (tampil `Bagas P`), Group `Head Office`, pengaju `Agus P`, Request Date `T0 − 14 hari`, Last Updated `T0 − 5 hari`. Aset `Tablet Apple iPad Air {runId}` (TAG QR, Category `Tablet`, Handed Over At `T0 − 12 hari`, Extensions `1 / 3`, Due Date `T0 − 7 hari`, Returned At `T0 − 5 hari`) berstatus Returned. Total Asset `1`.
  - DU-007-7: BRW Borrowed dengan satu baris Returned, Borrower `Citra Anggraini` (tampil `Citra A`), Group `Head Office`, pengaju `Agus P`, Request Date `T0 − 6 hari`, Last Updated `T0 − 3 hari`. Aset `Drone DJI Mini 3 {runId}` berstatus Returned dengan penanda `Missing` (Last Updated baris `T0 − 3 hari`, tanpa foto return karena ditutup otomatis oleh Report Missing), dan `Baterai DJI Intelligent {runId}` yang masih berstatus Borrowed.
  - DU-007-9: BRW Self-service Returned, Borrower `Eka Putri` (tampil `Eka P`), Group `Head Office`, Source `Self-service`, Requested By `—` karena Borrower meminjam sendiri, Request Date `T0 − 12 hari`, Last Updated `T0 − 6 hari`. Aset `Headset Sony WH-CH520 {runId}` (Brand `Sony`, Model/Type `WH-CH520`, Category `Headset`, TAG QR, Purpose `Kerja jarak jauh`, Handed Over At `T0 − 11 hari`, Returned At `T0 − 6 hari`, Extensions `0 / 3`) berstatus Returned. Total Asset `1`.
  - DU-007-12: kata kunci Search alias dan kode TAG milik aset `Laptop Asus ExpertBook B1402 {runId}` pada DU-007-2, diketik langkah.
  - DU-007-10: User `Monitor Borrow {runId}`, role Monitoring & Report, cakupan seluruh client.
  - DU-007-11: User `Viewer Borrow {runId}`, role Read Only, cakupan seluruh client.
  - DU-007-8: BRW Returned dengan Last Updated di luar rentang awal, Borrower `Dimas Saputra` (tampil `Dimas S`), Group `Head Office`, pengaju `Agus P`, Request Date `T0 − 110 hari`, Last Updated `T0 − 100 hari`. Aset `Aset Lama Kursi Ergonomis {runId}` berstatus Returned.
- Kondisi:
  - Akun `Monitor Borrow {runId}` dan `Viewer Borrow {runId}` aktif dan kredensialnya disediakan fase 2.
  - Date Format dan Time Format di General Settings entitas berlaku untuk tampilan tanggal.
  - Rentang awal filter Last Updated tab History adalah `T0 − 90 hari` sampai `T0`.
  - Max extensions efektif seluruh aset pada spec ini bernilai `3`.

## Test Steps

### Tab History dan view awal By Transaction
1. Klik tab `History`
2. Verifikasi view `By Transaction` aktif
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi hasil Search memuat 6 baris dengan Borrower `Wahyu N`, `Yuni A`, `Zaki F`, `Ayu L`, `Bagas P`, dan `Eka P`
5. Verifikasi baris Borrower `Citra A` tidak tampil karena BRW-nya masih memiliki baris aktif
6. Verifikasi baris Borrower `Dimas S` tidak tampil karena Last Updated di luar rentang awal
7. Verifikasi tab History tidak memiliki kartu ringkas
8. Verifikasi urutan baris dari atas ke bawah: Borrower `Bagas P`, `Eka P`, `Ayu L`, `Zaki F`, `Wahyu N`, lalu `Yuni A`

### Filter Status dan rentang Last Updated awal 90 hari
9. Klik `Filter`
10. Verifikasi field `Last Updated` terisi rentang dari `T0 − 90 hari` sampai `T0`
11. Klik field `Status`
12. Verifikasi opsi `Returned`, `Rejected`, dan `Canceled` tampil dan opsi `Borrowed` serta `Waiting for Handover` tidak tampil
13. Tutup daftar opsi field `Status`
14. Kosongkan field `Last Updated`
15. Klik `[Apply]`
16. Verifikasi baris Borrower `Dimas S` tampil
17. Klik `[Clear Field]`
18. Verifikasi field `Last Updated` kembali terisi rentang dari `T0 − 90 hari` sampai `T0`
19. Klik `[Apply]`
20. Verifikasi baris Borrower `Dimas S` tidak tampil dan baris Borrower `Wahyu N` tetap tampil
21. Ganti isi kotak search dengan `Aset Lama Kursi Ergonomis {runId}`, tekan Enter
22. Verifikasi pesan `No results found` dan `Try adjusting your search or filter.` tampil karena rentang awal menyembunyikan semua baris
23. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Isi kolom By Transaction
24. Verifikasi Transaction ID pada setiap baris berupa tautan yang dapat diklik
25. Verifikasi baris Borrower `Wahyu N` dan `Yuni A` menampilkan status `Returned`, baris Borrower `Zaki F` menampilkan status `Rejected`, dan baris Borrower `Ayu L` menampilkan status `Canceled`
26. Verifikasi baris Borrower `Yuni A` tidak menampilkan penanda `Damaged` pada status header
27. Verifikasi baris Borrower `Wahyu N`, `Yuni A`, `Zaki F`, dan `Bagas P` menampilkan Group `Head Office`
28. Verifikasi baris Borrower `Ayu L` menampilkan Group `Branch Surabaya`
29. Verifikasi baris Borrower `Wahyu N` menampilkan Total Asset `2`, termasuk baris yang sudah Returned
30. Verifikasi baris Borrower `Zaki F` menampilkan Total Asset `1` dan baris Borrower `Ayu L` menampilkan Total Asset `2`, termasuk baris Rejected dan Canceled
31. Verifikasi baris Borrower `Wahyu N`, `Yuni A`, `Zaki F`, dan `Bagas P` menampilkan Requested By `Agus P`
32. Verifikasi baris Borrower `Ayu L` menampilkan Requested By `Rina W`
33. Verifikasi baris Borrower `Eka P` menampilkan Requested By `—` karena Borrower meminjam sendiri
34. Verifikasi Request Date baris Borrower `Wahyu N` tampil sebagai `T0 − 20 hari` dengan Date Format General Settings
35. Verifikasi Last Updated baris Borrower `Wahyu N` tampil sebagai `T0 − 15 hari` dengan Date Format General Settings
36. Klik header kolom Actions `⋯`
37. Centang `Source` pada panel Column Visibility
38. Verifikasi baris Borrower `Eka P` menampilkan Source `Self-service`
39. Verifikasi kelima baris selain `Eka P` menampilkan Source `Admin`
40. Hapus centang `Source` pada panel Column Visibility

### Aksi baris dan Download By Transaction
41. Klik `⋯` pada baris Borrower `Zaki F`
42. Verifikasi menu baris pada tabel History memuat `Detail`
43. Klik `Detail`
44. Verifikasi halaman Borrow Detail terbuka untuk BRW baris Borrower `Zaki F` tanpa tombol aksi `Hand Over`, `Return`, `Request Extension`, dan `Cancel Borrow`
45. Kembali ke tab History lewat segmen Origin Tab pada breadcrumb
46. Klik `Download`
47. Pilih `Download as CSV`
48. Verifikasi berkas terunduh memuat 6 baris data milik spec ini sesuai saringan dan kolom yang tampil
49. Verifikasi berkas terunduh dengan nama `Borrow-History` dan ekstensi `.csv`

### View By Asset memuat setiap baris yang sudah selesai
50. Klik view `By Asset`
51. Ketik Search `{runId}`, tekan Enter
52. Verifikasi hasil Search memuat 10 baris dengan aset `Laptop Asus ExpertBook B1402 {runId}`, `Mouse Logitech M331 {runId}`, `Kamera Fujifilm X-T30 {runId}`, `Tripod Manfrotto Compact {runId}`, `Proyektor BenQ MH550 {runId}`, `Speaker Bose S1 Pro {runId}`, `Mikrofon Shure SM58 {runId}`, `Tablet Apple iPad Air {runId}`, `Drone DJI Mini 3 {runId}`, dan `Headset Sony WH-CH520 {runId}`
53. Verifikasi aset `Drone DJI Mini 3 {runId}` tampil walau BRW-nya masih memuat baris aktif
54. Verifikasi aset `Baterai DJI Intelligent {runId}` yang masih Borrowed tidak tampil
55. Verifikasi urutan awal: `Drone DJI Mini 3 {runId}` tampil sebelum `Tablet Apple iPad Air {runId}`, lalu `Proyektor BenQ MH550 {runId}`, lalu `Laptop Asus ExpertBook B1402 {runId}`, lalu `Kamera Fujifilm X-T30 {runId}`

### Isi kolom By Asset
56. Klik header kolom `Photo`
57. Verifikasi klik header `Photo` tidak mengubah urutan baris
58. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Name yang memuat nama aset tersebut
59. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Asset ID milik DU-007-2
60. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Brand `Asus` dan baris aset `Mouse Logitech M331 {runId}` menampilkan Brand `Logitech`
61. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Model/Type `B1402` dan baris aset `Mouse Logitech M331 {runId}` menampilkan Model/Type `M331`
62. Verifikasi baris aset `Speaker Bose S1 Pro {runId}` menampilkan Group `Branch Surabaya` dan baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Group `Head Office`
63. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan status `Returned`
64. Verifikasi baris aset `Kamera Fujifilm X-T30 {runId}` menampilkan status `Returned` dengan penanda `Damaged`
65. Verifikasi baris aset `Drone DJI Mini 3 {runId}` menampilkan status `Returned` dengan penanda `Missing`
66. Verifikasi baris aset `Proyektor BenQ MH550 {runId}` menampilkan status `Rejected` dan baris aset `Speaker Bose S1 Pro {runId}` menampilkan status `Canceled`
67. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Transaction ID yang sama dengan baris aset `Mouse Logitech M331 {runId}` sebagai tautan
68. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Borrower `Wahyu N` dan baris aset `Tablet Apple iPad Air {runId}` menampilkan Borrower `Bagas P`
69. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Handed Over At `T0 − 19 hari` dan baris aset `Proyektor BenQ MH550 {runId}` menampilkan `—`
70. Verifikasi baris aset `Tablet Apple iPad Air {runId}` menampilkan Returned At `T0 − 5 hari` dengan `late 2 days`
71. Verifikasi baris aset `Proyektor BenQ MH550 {runId}` dan `Speaker Bose S1 Pro {runId}` menampilkan Returned At `—`
72. Verifikasi baris aset `Tablet Apple iPad Air {runId}` menampilkan Extensions `1 / 3` dan baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Extensions `0 / 3`
73. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Last Updated `T0 − 15 hari` dengan Date Format General Settings

### Kolom tambahan By Asset dan Search pada kolom tersembunyi
74. Ganti isi kotak search dengan `NFC`, tekan Enter
75. Verifikasi baris aset `Kamera Fujifilm X-T30 {runId}` tidak tampil karena kolom `TAG` tersembunyi
76. Klik header kolom Actions `⋯`
77. Centang `TAG` pada panel Column Visibility
78. Verifikasi baris aset `Kamera Fujifilm X-T30 {runId}` tampil dengan ikon TAG `NFC`
79. Ganti isi kotak search dengan `{runId}`, tekan Enter
80. Verifikasi baris aset `Mouse Logitech M331 {runId}` menampilkan `—` pada kolom `TAG`
81. Centang `Category` pada panel Column Visibility
82. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Category `Laptop`
83. Centang `Reason` pada panel Column Visibility
84. Verifikasi baris aset `Proyektor BenQ MH550 {runId}` menampilkan Reason `Anggaran belum disetujui` apa adanya
85. Verifikasi baris aset `Speaker Bose S1 Pro {runId}` menampilkan Reason `Timed out (Waiting for Approval)`
86. Verifikasi baris aset `Mikrofon Shure SM58 {runId}` menampilkan Reason `—`
87. Centang `Handover Photo` pada panel Column Visibility
88. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan thumbnail foto handover dan baris aset `Mouse Logitech M331 {runId}` menampilkan `—`
89. Centang `Return Photo` pada panel Column Visibility
90. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan thumbnail foto return dan baris aset `Mouse Logitech M331 {runId}` menampilkan `—`
91. Verifikasi baris aset `Drone DJI Mini 3 {runId}` menampilkan `—` pada kolom Return Photo karena baris ditutup otomatis oleh Report Missing
92. Centang `Source` pada panel Column Visibility
93. Verifikasi baris aset `Headset Sony WH-CH520 {runId}` menampilkan Source `Self-service`
94. Verifikasi kesembilan baris selain `Headset Sony WH-CH520 {runId}` menampilkan Source `Admin`
95. Centang `Purpose` pada panel Column Visibility
96. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Purpose `Pelatihan karyawan`

### Opsi Status By Asset
97. Klik `Filter`
98. Klik field `Status`
99. Verifikasi opsi `Returned`, `Returned · Damaged`, `Returned · Missing`, `Rejected`, dan `Canceled` tampil
100. Tutup daftar opsi field `Status`
101. Tutup Filter Panel tanpa klik `[Apply]`

### Aksi baris dan Download By Asset
102. Klik `⋯` pada baris aset `Laptop Asus ExpertBook B1402 {runId}`
103. Verifikasi menu baris memuat `Borrow Log`
104. Klik `Borrow Log`
105. Verifikasi dialog Borrow Log terbuka untuk aset `Laptop Asus ExpertBook B1402 {runId}`
106. Tutup dialog Borrow Log
107. Klik `Download`
108. Pilih `Download as XLSX`
109. Verifikasi berkas terunduh memuat 10 baris data milik spec ini sesuai saringan dan kolom yang tampil
110. Verifikasi berkas terunduh dengan nama `Borrow-History` dan ekstensi `.xlsx`

### Sort kolom By Asset lewat klik header
111. Ganti isi kotak search dengan `{runId}`, tekan Enter
112. Verifikasi hasil Search memuat 10 baris milik spec ini
113. Klik header kolom `Name`
114. Verifikasi urutan baris dari atas ke bawah: aset `Drone DJI Mini 3 {runId}`, lalu aset `Tripod Manfrotto Compact {runId}`
115. Klik header kolom `Name`
116. Verifikasi urutan baris dari atas ke bawah: aset `Tripod Manfrotto Compact {runId}`, lalu aset `Drone DJI Mini 3 {runId}`
117. Klik header kolom `Asset ID`
118. Verifikasi kolom Asset ID dari atas ke bawah berurutan alfabetis menaik
119. Klik header kolom `Asset ID`
120. Verifikasi kolom Asset ID dari atas ke bawah berurutan alfabetis menurun
121. Klik header kolom `Brand`
122. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Asus ExpertBook B1402 {runId}`, lalu aset `Mouse Logitech M331 {runId}` (Brand `Asus` sebelum `Logitech`)
123. Klik header kolom `Brand`
124. Verifikasi urutan baris dari atas ke bawah: aset `Mouse Logitech M331 {runId}`, lalu aset `Laptop Asus ExpertBook B1402 {runId}` (Brand `Logitech` sebelum `Asus`)
125. Klik header kolom `Model/Type`
126. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Asus ExpertBook B1402 {runId}`, lalu aset `Mouse Logitech M331 {runId}` (Model/Type `B1402` sebelum `M331`)
127. Klik header kolom `Model/Type`
128. Verifikasi urutan baris dari atas ke bawah: aset `Mouse Logitech M331 {runId}`, lalu aset `Laptop Asus ExpertBook B1402 {runId}` (Model/Type `M331` sebelum `B1402`)
129. Klik header kolom `Group`
130. Verifikasi urutan baris dari atas ke bawah: aset `Speaker Bose S1 Pro {runId}`, lalu aset `Laptop Asus ExpertBook B1402 {runId}` (Group `Branch Surabaya` sebelum `Head Office`)
131. Klik header kolom `Group`
132. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Asus ExpertBook B1402 {runId}`, lalu aset `Speaker Bose S1 Pro {runId}` (Group `Head Office` sebelum `Branch Surabaya`)
133. Klik header kolom `Status`
134. Verifikasi urutan baris dari atas ke bawah: aset `Speaker Bose S1 Pro {runId}`, lalu aset `Proyektor BenQ MH550 {runId}`, lalu aset `Laptop Asus ExpertBook B1402 {runId}` (status `Canceled`, `Rejected`, lalu `Returned`)
135. Klik header kolom `Status`
136. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Asus ExpertBook B1402 {runId}`, lalu aset `Proyektor BenQ MH550 {runId}`, lalu aset `Speaker Bose S1 Pro {runId}` (status `Returned`, `Rejected`, lalu `Canceled`)
137. Klik header kolom `TAG`
138. Verifikasi urutan baris dari atas ke bawah: aset `Kamera Fujifilm X-T30 {runId}`, lalu aset `Mouse Logitech M331 {runId}`, lalu aset `Laptop Asus ExpertBook B1402 {runId}` (TAG `NFC`, Non TAG, lalu `RFID`)
139. Klik header kolom `TAG`
140. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Asus ExpertBook B1402 {runId}`, lalu aset `Mouse Logitech M331 {runId}`, lalu aset `Kamera Fujifilm X-T30 {runId}` (TAG `RFID`, Non TAG, lalu `NFC`)
141. Klik header kolom `Category`
142. Verifikasi urutan baris dari atas ke bawah: aset `Mouse Logitech M331 {runId}`, lalu aset `Laptop Asus ExpertBook B1402 {runId}`, lalu aset `Tablet Apple iPad Air {runId}` (Category `Aksesoris Komputer`, `Laptop`, lalu `Tablet`)
143. Klik header kolom `Category`
144. Verifikasi urutan baris dari atas ke bawah: aset `Tablet Apple iPad Air {runId}`, lalu aset `Laptop Asus ExpertBook B1402 {runId}`, lalu aset `Mouse Logitech M331 {runId}` (Category `Tablet`, `Laptop`, lalu `Aksesoris Komputer`)
145. Klik header kolom `Transaction ID`
146. Verifikasi kolom Transaction ID dari atas ke bawah berurutan alfabetis natural menaik
147. Klik header kolom `Transaction ID`
148. Verifikasi kolom Transaction ID dari atas ke bawah berurutan alfabetis natural menurun
149. Klik header kolom `Borrower`
150. Verifikasi urutan baris dari atas ke bawah: aset `Speaker Bose S1 Pro {runId}`, lalu aset `Tablet Apple iPad Air {runId}`, lalu aset `Laptop Asus ExpertBook B1402 {runId}` (Borrower `Ayu L`, `Bagas P`, lalu `Wahyu N`)
151. Klik header kolom `Borrower`
152. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Asus ExpertBook B1402 {runId}`, lalu aset `Tablet Apple iPad Air {runId}`, lalu aset `Speaker Bose S1 Pro {runId}` (Borrower `Wahyu N`, `Bagas P`, lalu `Ayu L`)
153. Klik header kolom `Handed Over At`
154. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Asus ExpertBook B1402 {runId}`, lalu aset `Tablet Apple iPad Air {runId}`, lalu aset `Proyektor BenQ MH550 {runId}` (Handed Over At `T0 − 19 hari`, `T0 − 12 hari`, lalu `—`)
155. Klik header kolom `Handed Over At`
156. Verifikasi urutan baris dari atas ke bawah: aset `Proyektor BenQ MH550 {runId}`, lalu aset `Tablet Apple iPad Air {runId}`, lalu aset `Laptop Asus ExpertBook B1402 {runId}` (Handed Over At `—`, `T0 − 12 hari`, lalu `T0 − 19 hari`)
157. Klik header kolom `Returned At`
158. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Asus ExpertBook B1402 {runId}`, lalu aset `Tablet Apple iPad Air {runId}`, lalu aset `Proyektor BenQ MH550 {runId}` (Returned At `T0 − 15 hari`, `T0 − 5 hari`, lalu `—`)
159. Klik header kolom `Returned At`
160. Verifikasi urutan baris dari atas ke bawah: aset `Proyektor BenQ MH550 {runId}`, lalu aset `Tablet Apple iPad Air {runId}`, lalu aset `Laptop Asus ExpertBook B1402 {runId}` (Returned At `—`, `T0 − 5 hari`, lalu `T0 − 15 hari`)
161. Klik header kolom `Extensions`
162. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Asus ExpertBook B1402 {runId}`, lalu aset `Tablet Apple iPad Air {runId}` (Extensions `0 / 3` sebelum `1 / 3`)
163. Klik header kolom `Extensions`
164. Verifikasi urutan baris dari atas ke bawah: aset `Tablet Apple iPad Air {runId}`, lalu aset `Laptop Asus ExpertBook B1402 {runId}` (Extensions `1 / 3` sebelum `0 / 3`)
165. Klik header kolom `Reason`
166. Verifikasi urutan baris dari atas ke bawah: aset `Proyektor BenQ MH550 {runId}`, lalu aset `Speaker Bose S1 Pro {runId}`, lalu aset `Laptop Asus ExpertBook B1402 {runId}` (Reason `Anggaran belum disetujui`, `Timed out (Waiting for Approval)`, lalu `—`)
167. Klik header kolom `Reason`
168. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Asus ExpertBook B1402 {runId}`, lalu aset `Speaker Bose S1 Pro {runId}`, lalu aset `Proyektor BenQ MH550 {runId}` (Reason `—`, `Timed out (Waiting for Approval)`, lalu `Anggaran belum disetujui`)
169. Klik header kolom `Handover Photo`
170. Verifikasi klik header `Handover Photo` tidak mengubah urutan baris
171. Klik header kolom `Return Photo`
172. Verifikasi klik header `Return Photo` tidak mengubah urutan baris
173. Klik header kolom `Source`
174. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Asus ExpertBook B1402 {runId}`, lalu aset `Headset Sony WH-CH520 {runId}` (Source `Admin` sebelum `Self-service`)
175. Klik header kolom `Source`
176. Verifikasi urutan baris dari atas ke bawah: aset `Headset Sony WH-CH520 {runId}`, lalu aset `Laptop Asus ExpertBook B1402 {runId}` (Source `Self-service` sebelum `Admin`)
177. Klik header kolom `Purpose`
178. Verifikasi urutan baris dari atas ke bawah: aset `Headset Sony WH-CH520 {runId}`, lalu aset `Laptop Asus ExpertBook B1402 {runId}` (Purpose `Kerja jarak jauh` sebelum `Pelatihan karyawan`)
179. Klik header kolom `Purpose`
180. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Asus ExpertBook B1402 {runId}`, lalu aset `Headset Sony WH-CH520 {runId}` (Purpose `Pelatihan karyawan` sebelum `Kerja jarak jauh`)
181. Klik header kolom `Last Updated`
182. Verifikasi urutan baris dari atas ke bawah: aset `Laptop Asus ExpertBook B1402 {runId}`, lalu aset `Drone DJI Mini 3 {runId}` (Last Updated `T0 − 15 hari` sebelum `T0 − 3 hari`, Oldest First)
183. Klik header kolom `Last Updated`
184. Verifikasi urutan baris dari atas ke bawah: aset `Drone DJI Mini 3 {runId}`, lalu aset `Laptop Asus ExpertBook B1402 {runId}` (Last Updated `T0 − 3 hari` sebelum `T0 − 15 hari`, Newest First)

### Search mencocokkan nilai kolom By Asset
185. Ganti isi kotak search dengan `Tripod`, tekan Enter
186. Verifikasi baris aset `Tripod Manfrotto Compact {runId}` tampil
187. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tidak tampil
188. Ganti isi kotak search dengan Asset ID aset `Laptop Asus ExpertBook B1402 {runId}`, tekan Enter
189. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tampil
190. Verifikasi baris aset `Mouse Logitech M331 {runId}` tidak tampil
191. Ganti isi kotak search dengan `Asus`, tekan Enter
192. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tampil
193. Verifikasi baris aset `Mouse Logitech M331 {runId}` tidak tampil
194. Ganti isi kotak search dengan `M331`, tekan Enter
195. Verifikasi baris aset `Mouse Logitech M331 {runId}` tampil
196. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tidak tampil
197. Ganti isi kotak search dengan `Branch Surabaya`, tekan Enter
198. Verifikasi baris aset `Speaker Bose S1 Pro {runId}` tampil
199. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tidak tampil
200. Ganti isi kotak search dengan `Rejected`, tekan Enter
201. Verifikasi baris aset `Proyektor BenQ MH550 {runId}` tampil
202. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tidak tampil
203. Ganti isi kotak search dengan `Aksesoris Komputer`, tekan Enter
204. Verifikasi baris aset `Mouse Logitech M331 {runId}` tampil
205. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tidak tampil
206. Ganti isi kotak search dengan Transaction ID milik DU-007-4, tekan Enter
207. Verifikasi baris aset `Proyektor BenQ MH550 {runId}` tampil
208. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tidak tampil
209. Ganti isi kotak search dengan `Wahyu Nugroho`, tekan Enter
210. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tampil
211. Verifikasi baris aset `Tablet Apple iPad Air {runId}` tidak tampil
212. Ganti isi kotak search dengan `1 / 3`, tekan Enter
213. Verifikasi baris aset `Tablet Apple iPad Air {runId}` tampil
214. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tidak tampil
215. Ganti isi kotak search dengan `Anggaran belum disetujui`, tekan Enter
216. Verifikasi baris aset `Proyektor BenQ MH550 {runId}` tampil
217. Verifikasi baris aset `Speaker Bose S1 Pro {runId}` tidak tampil
218. Ganti isi kotak search dengan `Self-service`, tekan Enter
219. Verifikasi baris aset `Headset Sony WH-CH520 {runId}` tampil
220. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tidak tampil
221. Ganti isi kotak search dengan `Pelatihan karyawan`, tekan Enter
222. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tampil
223. Verifikasi baris aset `Tablet Apple iPad Air {runId}` tidak tampil
224. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Filter Panel By Asset menerapkan saringan per field
225. Klik `Filter`
226. Klik field `Asset Name`
227. Pilih opsi `Drone DJI Mini 3 {runId}`
228. Klik `[Apply]`
229. Verifikasi baris aset `Drone DJI Mini 3 {runId}` tampil
230. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tidak tampil
231. Klik `[Clear Field]`
232. Klik field `Brand`
233. Pilih opsi `Asus`
234. Klik `[Apply]`
235. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tampil
236. Verifikasi baris aset `Mouse Logitech M331 {runId}` tidak tampil
237. Klik `[Clear Field]`
238. Klik field `Model/Type`
239. Pilih opsi `M331`
240. Klik `[Apply]`
241. Verifikasi baris aset `Mouse Logitech M331 {runId}` tampil
242. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tidak tampil
243. Klik `[Clear Field]`
244. Klik field `Group`
245. Pilih opsi `Branch Surabaya`
246. Klik `[Apply]`
247. Verifikasi baris aset `Speaker Bose S1 Pro {runId}` tampil
248. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tidak tampil
249. Klik `[Clear Field]`
250. Klik field `Status`
251. Pilih opsi `Returned · Damaged`
252. Klik `[Apply]`
253. Verifikasi baris aset `Kamera Fujifilm X-T30 {runId}` tampil
254. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tidak tampil
255. Klik `[Clear Field]`
256. Klik field `TAG`
257. Pilih opsi `NFC`
258. Klik `[Apply]`
259. Verifikasi baris aset `Kamera Fujifilm X-T30 {runId}` tampil
260. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tidak tampil
261. Klik `[Clear Field]`
262. Klik field `Category`
263. Pilih opsi `Aksesoris Komputer`
264. Klik `[Apply]`
265. Verifikasi baris aset `Mouse Logitech M331 {runId}` tampil
266. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tidak tampil
267. Klik `[Clear Field]`
268. Klik field `Borrower`
269. Pilih opsi `Wahyu N`
270. Klik `[Apply]`
271. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tampil
272. Verifikasi baris aset `Tablet Apple iPad Air {runId}` tidak tampil
273. Klik `[Clear Field]`
274. Klik field `Handed Over At`
275. Pilih rentang tanggal dari `T0 − 20 hari` sampai `T0 − 18 hari`
276. Klik `[Apply]`
277. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tampil
278. Verifikasi baris aset `Tablet Apple iPad Air {runId}` tidak tampil
279. Klik `[Clear Field]`
280. Klik field `Returned At`
281. Pilih rentang tanggal dari `T0 − 16 hari` sampai `T0 − 14 hari`
282. Klik `[Apply]`
283. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tampil
284. Verifikasi baris aset `Tablet Apple iPad Air {runId}` tidak tampil
285. Klik `[Clear Field]`
286. Klik field `Extensions`
287. Isi `Min` dengan `1`
288. Isi `Max` dengan `1`
289. Klik `[Apply]`
290. Verifikasi baris aset `Tablet Apple iPad Air {runId}` tampil
291. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tidak tampil
292. Klik `[Clear Field]`
293. Klik field `Source`
294. Pilih opsi `Self-service`
295. Klik `[Apply]`
296. Verifikasi baris aset `Headset Sony WH-CH520 {runId}` tampil
297. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tidak tampil
298. Klik `[Clear Field]`
299. Klik field `Last Updated`
300. Kosongkan field `Last Updated`
301. Pilih rentang tanggal dari `T0 − 16 hari` sampai `T0 − 14 hari`
302. Klik `[Apply]`
303. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` tampil
304. Verifikasi baris aset `Tablet Apple iPad Air {runId}` tidak tampil
305. Klik `[Clear Field]`
306. Klik `[Apply]`

### Sort kolom By Transaction lewat klik header
307. Klik view `By Transaction`
308. Ganti isi kotak search dengan `{runId}`, tekan Enter
309. Verifikasi hasil Search memuat 6 baris milik spec ini
310. Klik header kolom `Transaction ID`
311. Verifikasi kolom Transaction ID dari atas ke bawah berurutan alfabetis natural menaik
312. Klik header kolom `Transaction ID`
313. Verifikasi kolom Transaction ID dari atas ke bawah berurutan alfabetis natural menurun
314. Klik header kolom `Status`
315. Verifikasi urutan baris dari atas ke bawah: Borrower `Ayu L`, lalu Borrower `Zaki F`, lalu Borrower `Wahyu N` (status `Canceled`, `Rejected`, lalu `Returned`)
316. Klik header kolom `Status`
317. Verifikasi urutan baris dari atas ke bawah: Borrower `Wahyu N`, lalu Borrower `Zaki F`, lalu Borrower `Ayu L` (status `Returned`, `Rejected`, lalu `Canceled`)
318. Klik header kolom `Group`
319. Verifikasi urutan baris dari atas ke bawah: Borrower `Ayu L`, lalu Borrower `Wahyu N` (Group `Branch Surabaya` sebelum `Head Office`)
320. Klik header kolom `Group`
321. Verifikasi urutan baris dari atas ke bawah: Borrower `Wahyu N`, lalu Borrower `Ayu L` (Group `Head Office` sebelum `Branch Surabaya`)
322. Klik header kolom `Borrower`
323. Verifikasi urutan baris dari atas ke bawah: Borrower `Ayu L`, lalu Borrower `Bagas P`, lalu Borrower `Wahyu N`
324. Klik header kolom `Borrower`
325. Verifikasi urutan baris dari atas ke bawah: Borrower `Wahyu N`, lalu Borrower `Bagas P`, lalu Borrower `Ayu L`
326. Klik header kolom `Total Asset`
327. Verifikasi urutan baris dari atas ke bawah: Borrower `Zaki F`, lalu Borrower `Wahyu N` (Total Asset `1` sebelum `2`)
328. Klik header kolom `Total Asset`
329. Verifikasi urutan baris dari atas ke bawah: Borrower `Wahyu N`, lalu Borrower `Zaki F` (Total Asset `2` sebelum `1`)
330. Klik header kolom Actions `⋯`
331. Centang `Source` pada panel Column Visibility
332. Klik header kolom `Source`
333. Verifikasi urutan baris dari atas ke bawah: Borrower `Wahyu N`, lalu Borrower `Eka P` (Source `Admin` sebelum `Self-service`)
334. Klik header kolom `Source`
335. Verifikasi urutan baris dari atas ke bawah: Borrower `Eka P`, lalu Borrower `Wahyu N` (Source `Self-service` sebelum `Admin`)
336. Klik header kolom `Requested By`
337. Verifikasi urutan baris dari atas ke bawah: Borrower `Wahyu N`, lalu Borrower `Ayu L`, lalu Borrower `Eka P` (Requested By `Agus P`, `Rina W`, lalu `—`)
338. Klik header kolom `Requested By`
339. Verifikasi urutan baris dari atas ke bawah: Borrower `Eka P`, lalu Borrower `Ayu L`, lalu Borrower `Wahyu N` (Requested By `—`, `Rina W`, lalu `Agus P`)
340. Klik header kolom `Request Date`
341. Verifikasi urutan baris dari atas ke bawah: Borrower `Yuni A`, lalu Borrower `Ayu L` (Request Date `T0 − 30 hari` sebelum `T0 − 8 hari`, Oldest First)
342. Klik header kolom `Request Date`
343. Verifikasi urutan baris dari atas ke bawah: Borrower `Ayu L`, lalu Borrower `Yuni A` (Request Date `T0 − 8 hari` sebelum `T0 − 30 hari`, Newest First)
344. Klik header kolom `Last Updated`
345. Verifikasi urutan baris dari atas ke bawah: Borrower `Yuni A`, lalu Borrower `Bagas P` (Last Updated `T0 − 25 hari` sebelum `T0 − 5 hari`, Oldest First)
346. Klik header kolom `Last Updated`
347. Verifikasi urutan baris dari atas ke bawah: Borrower `Bagas P`, lalu Borrower `Yuni A` (Last Updated `T0 − 5 hari` sebelum `T0 − 25 hari`, Newest First)

### Search mencocokkan nilai kolom By Transaction
348. Ganti isi kotak search dengan Transaction ID milik DU-007-3, tekan Enter
349. Verifikasi baris Borrower `Yuni A` tampil
350. Verifikasi baris Borrower `Wahyu N` tidak tampil
351. Ganti isi kotak search dengan `Rejected`, tekan Enter
352. Verifikasi baris Borrower `Zaki F` tampil
353. Verifikasi baris Borrower `Wahyu N` tidak tampil
354. Ganti isi kotak search dengan `Branch Surabaya`, tekan Enter
355. Verifikasi baris Borrower `Ayu L` tampil
356. Verifikasi baris Borrower `Wahyu N` tidak tampil
357. Ganti isi kotak search dengan `Zaki Firmansyah`, tekan Enter
358. Verifikasi baris Borrower `Zaki F` tampil
359. Verifikasi baris Borrower `Wahyu N` tidak tampil
360. Ganti isi kotak search dengan Asset ID aset `Kamera Fujifilm X-T30 {runId}`, tekan Enter
361. Verifikasi baris Borrower `Yuni A` tampil
362. Verifikasi baris Borrower `Wahyu N` tidak tampil
363. Ganti isi kotak search dengan `Self-service`, tekan Enter
364. Verifikasi baris Borrower `Eka P` tampil
365. Verifikasi baris Borrower `Wahyu N` tidak tampil
366. Ganti isi kotak search dengan `Rina W`, tekan Enter
367. Verifikasi baris Borrower `Ayu L` tampil
368. Verifikasi baris Borrower `Wahyu N` tidak tampil
369. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Filter Panel By Transaction menerapkan saringan per field
370. Klik `Filter`
371. Klik field `Status`
372. Pilih opsi `Rejected`
373. Klik `[Apply]`
374. Verifikasi baris Borrower `Zaki F` tampil
375. Verifikasi baris Borrower `Wahyu N` tidak tampil
376. Klik `[Clear Field]`
377. Klik field `Group`
378. Pilih opsi `Branch Surabaya`
379. Klik `[Apply]`
380. Verifikasi baris Borrower `Ayu L` tampil
381. Verifikasi baris Borrower `Wahyu N` tidak tampil
382. Klik `[Clear Field]`
383. Klik field `Borrower`
384. Pilih opsi `Yuni A`
385. Klik `[Apply]`
386. Verifikasi baris Borrower `Yuni A` tampil
387. Verifikasi baris Borrower `Wahyu N` tidak tampil
388. Klik `[Clear Field]`
389. Klik field `Total Asset`
390. Isi `Min` dengan `1`
391. Isi `Max` dengan `1`
392. Klik `[Apply]`
393. Verifikasi baris Borrower `Zaki F` dan `Bagas P` tampil
394. Verifikasi baris Borrower `Wahyu N` tidak tampil
395. Klik `[Clear Field]`
396. Klik field `Source`
397. Pilih opsi `Self-service`
398. Klik `[Apply]`
399. Verifikasi baris Borrower `Eka P` tampil
400. Verifikasi baris Borrower `Wahyu N` tidak tampil
401. Klik `[Clear Field]`
402. Klik field `Requested By`
403. Pilih opsi `Rina W`
404. Klik `[Apply]`
405. Verifikasi baris Borrower `Ayu L` tampil
406. Verifikasi baris Borrower `Wahyu N` tidak tampil
407. Klik `[Clear Field]`
408. Klik field `Request Date`
409. Pilih rentang tanggal dari `T0 − 21 hari` sampai `T0 − 19 hari`
410. Klik `[Apply]`
411. Verifikasi baris Borrower `Wahyu N` tampil
412. Verifikasi baris Borrower `Yuni A` tidak tampil
413. Klik `[Clear Field]`
414. Klik field `Last Updated`
415. Kosongkan field `Last Updated`
416. Pilih rentang tanggal dari `T0 − 16 hari` sampai `T0 − 14 hari`
417. Klik `[Apply]`
418. Verifikasi baris Borrower `Wahyu N` tampil
419. Verifikasi baris Borrower `Bagas P` tidak tampil
420. Klik `[Clear Field]`
421. Klik `[Apply]`

### Pilihan view tersimpan di URL
422. Verifikasi alamat halaman memuat `view=transaction` dan view `By Transaction` aktif
423. Klik view `By Asset`
424. Verifikasi alamat halaman memuat `view=asset`

### BRW yang masih punya baris aktif tetap di tab Transactions
425. Klik tab `Transactions`
426. Ketik Search `{runId}`, tekan Enter
427. Verifikasi baris Borrower `Citra A` tampil dengan satu baris Returned dan satu baris Borrowed

### Download tersedia untuk Monitoring & Report dan Read Only di tab History
428. Masuk sebagai `Monitor Borrow {runId}`
429. Klik tab `History`
430. Verifikasi tombol `Download` tampil di toolbar view `By Transaction`
431. Klik view `By Asset`
432. Verifikasi tombol `Download` tampil di toolbar view `By Asset`
433. Masuk sebagai `Viewer Borrow {runId}`
434. Klik tab `History`
435. Verifikasi tombol `Download` tampil di toolbar view `By Transaction`
436. Klik view `By Asset`
437. Verifikasi tombol `Download` tampil di toolbar view `By Asset`

### Klik Transaction ID baris view By Asset membuka Borrow Detail
438. Masuk sebagai `Admin Borrow {runId}`
439. Klik tab `History`
440. Klik view `By Asset`
441. Ketik Search `{runId}`, tekan Enter
442. Klik Transaction ID baris aset `Laptop Asus ExpertBook B1402 {runId}`
443. Verifikasi halaman Borrow Detail terbuka dengan Transaction ID milik DU-007-2
444. Kembali ke tab History lewat segmen Origin Tab pada breadcrumb

### Search view By Transaction mencakup alias aset dan kode TAG
445. Klik view `By Transaction`
446. Ketik Search `Laptop Pelatihan {runId}`, tekan Enter
447. Verifikasi baris Borrower `Wahyu N` tampil
448. Verifikasi baris Borrower `Yuni A` tidak tampil
449. Ganti isi kotak search dengan `E2003412DF7C-{runId}`, tekan Enter
450. Verifikasi baris Borrower `Wahyu N` tampil
451. Verifikasi baris Borrower `Yuni A` tidak tampil

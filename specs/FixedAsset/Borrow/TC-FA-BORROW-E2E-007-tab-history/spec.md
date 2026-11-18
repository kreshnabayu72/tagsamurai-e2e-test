---
id: TC-FA-BORROW-E2E-007-tab-history
title: "Tab History menampilkan transaksi dan baris yang sudah selesai dengan rentang awal 90 hari"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1k#p1", "§4.1k#p2", "§4.1k#b1", "§4.1k#b2", "§4.1k#r1", "§4.1k#r2", "§4.1k#r3", "§4.1k#r4", "§4.1k#r5", "§4.1k#r6", "§4.1k#r7", "§4.1k#r8", "§4.1k#r9", "§4.1k#p5", "§4.1k#r10", "§4.1k#r11", "§4.1k#r16", "§4.1k#r17", "§4.1k#r18", "§4.1k#r19", "§4.1k#r20", "§4.1k#r21", "§4.1k#r22", "§4.1k#r23", "§4.1k#r24", "§4.1k#r25", "§4.1k#r26", "§4.1k#r27", "§4.1k#r28", "§4.1k#r29", "§4.1k#r30", "§4.1k#r31", "§4.1k#r32", "§4.1k#r33", "§4.1k#r34", "§4.1k#r35", "§4.1k#p8", "§4.1k#r36", "§4.1k#r37", "§9.5#r6", "§9.5#r17", "EB-SRC-5@tabel-history"]
smoke: []
dependsOn: []
trace:
  "§4.1k#p1": [2]
  "§4.1k#p2": [7, 10, 12, 16, 22]
  "§4.1k#b1": [4, 5]
  "§4.1k#b2": [49, 50, 51]
  "§4.1k#r1": [24]
  "§4.1k#r2": [12, 25, 26]
  "§4.1k#r3": [27, 28]
  "§4.1k#r4": [4]
  "§4.1k#r5": [29, 30]
  "§4.1k#r6": [37]
  "§4.1k#r7": [31, 32]
  "§4.1k#r8": [33]
  "§4.1k#r9": [8, 34]
  "§4.1k#p5": [40]
  "§4.1k#r10": [40, 42]
  "§4.1k#r11": [46]
  "§4.1k#r16": [54]
  "§4.1k#r17": [55]
  "§4.1k#r18": [56]
  "§4.1k#r19": [57]
  "§4.1k#r20": [58]
  "§4.1k#r21": [59]
  "§4.1k#r22": [60, 61, 62, 63, 94]
  "§4.1k#r23": [75, 76]
  "§4.1k#r24": [79]
  "§4.1k#r25": [64]
  "§4.1k#r26": [65]
  "§4.1k#r27": [66]
  "§4.1k#r28": [67, 68]
  "§4.1k#r29": [69]
  "§4.1k#r30": [81, 82, 83]
  "§4.1k#r31": [85]
  "§4.1k#r32": [87]
  "§4.1k#r33": [89]
  "§4.1k#r34": [91]
  "§4.1k#r35": [52, 70]
  "§4.1k#p8": [98]
  "§4.1k#r36": [98, 100]
  "§4.1k#r37": [104]
  "§9.5#r6": [8, 52]
  "§9.5#r17": [6, 10, 16, 18, 20]
  "EB-SRC-5@tabel-history": [72, 75]
anchor: []
coverage:
  web: automated
---

# Tab History menampilkan transaksi dan baris yang sudah selesai dengan rentang awal 90 hari

## Prerequisites
- Aktor: Total Control `Admin Borrow {runId}` (DU-007-1), cakupan seluruh client.
- Layar awal: Transactions > Borrow, tab Transactions.
- Data:
  - DU-007-1: User `Admin Borrow {runId}`, role Total Control, cakupan seluruh client.
  - Pengaju: `Agus Pratama` (Asset Admin, Group penugasan `Head Office`), tampil `Agus P`; `Rina Wulandari` (Total Control, seluruh client), tampil `Rina W`. Seluruh BRW dibuat lewat form Borrow Request (Source `Admin`).
  - DU-007-2: BRW Returned, Borrower `Wahyu Nugroho` (tampil `Wahyu N`), Group `Head Office`, pengaju `Agus P`, Request Date `T0 − 20 hari`, Last Updated `T0 − 15 hari`. Aset `Laptop Asus ExpertBook B1402 {runId}` (Brand `Asus`, Model/Type `B1402`, Category `Laptop`, TAG RFID, Purpose `Pelatihan karyawan`, Handed Over At `T0 − 19 hari`, Returned At `T0 − 15 hari`, Extensions `0 / 3`, foto handover dan foto return tersimpan) dan `Mouse Logitech M331 {runId}` (Brand `Logitech`, Model/Type `M331`, Non TAG, Returned At `T0 − 15 hari`). Kedua baris Returned, Total Asset `2`.
  - DU-007-3: BRW Returned, Borrower `Yuni Astuti` (tampil `Yuni A`), Group `Head Office`, pengaju `Agus P`, Request Date `T0 − 30 hari`, Last Updated `T0 − 25 hari`. Aset `Kamera Fujifilm X-T30 {runId}` (TAG NFC) berstatus Returned dengan penanda `Damaged`, dan `Tripod Manfrotto Compact {runId}` berstatus Returned. Total Asset `2`.
  - DU-007-4: BRW Rejected, Borrower `Zaki Firmansyah` (tampil `Zaki F`), Group `Head Office`, pengaju `Agus P`, Request Date `T0 − 10 hari`, Last Updated `T0 − 9 hari`. Aset `Proyektor BenQ MH550 {runId}` berstatus Rejected dengan Reason `Anggaran belum disetujui`. Total Asset `1`.
  - DU-007-5: BRW Canceled, Borrower `Ayu Lestari` (tampil `Ayu L`), Group `Branch Surabaya`, pengaju `Rina W`, Request Date `T0 − 8 hari`, Last Updated `T0 − 7 hari`. Aset `Speaker Bose S1 Pro {runId}` berstatus Canceled oleh System dengan Reason `Timed out (Waiting for Approval)`, dan `Mikrofon Shure SM58 {runId}` berstatus Canceled manual tanpa Reason. Total Asset `2`.
  - DU-007-6: BRW Returned terlambat, Borrower `Bagas Pratama` (tampil `Bagas P`), Group `Head Office`, pengaju `Agus P`, Request Date `T0 − 14 hari`, Last Updated `T0 − 5 hari`. Aset `Tablet Apple iPad Air {runId}` (TAG QR, Extensions `1 / 3`, Due Date `T0 − 7 hari`, Returned At `T0 − 5 hari`) berstatus Returned. Total Asset `1`.
  - DU-007-7: BRW Borrowed dengan satu baris Returned, Borrower `Citra Anggraini` (tampil `Citra A`), Group `Head Office`, pengaju `Agus P`, Request Date `T0 − 6 hari`, Last Updated `T0 − 3 hari`. Aset `Drone DJI Mini 3 {runId}` berstatus Returned dengan penanda `Missing`, dan `Baterai DJI Intelligent {runId}` yang masih berstatus Borrowed.
  - DU-007-8: BRW Returned dengan Last Updated di luar rentang awal, Borrower `Dimas Saputra` (tampil `Dimas S`), Group `Head Office`, pengaju `Agus P`, Request Date `T0 − 110 hari`, Last Updated `T0 − 100 hari`. Aset `Aset Lama Kursi Ergonomis {runId}` berstatus Returned.
- Kondisi:
  - Date Format dan Time Format di General Settings entitas berlaku untuk tampilan tanggal.
  - Rentang awal filter Last Updated tab History adalah `T0 − 90 hari` sampai `T0`.
  - Max extensions efektif seluruh aset pada spec ini bernilai `3`.

## Test Steps

### Tab History dan view awal By Transaction
1. Klik tab `History`
2. Verifikasi view `By Transaction` aktif
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi hasil Search memuat 5 baris dengan Borrower `Wahyu N`, `Yuni A`, `Zaki F`, `Ayu L`, dan `Bagas P`
5. Verifikasi baris Borrower `Citra A` tidak tampil karena BRW-nya masih memiliki baris aktif
6. Verifikasi baris Borrower `Dimas S` tidak tampil karena Last Updated di luar rentang awal
7. Verifikasi tab History tidak memiliki kartu ringkas
8. Verifikasi urutan baris dari atas ke bawah: Borrower `Bagas P`, `Ayu L`, `Zaki F`, `Wahyu N`, lalu `Yuni A`

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
33. Verifikasi Request Date baris Borrower `Wahyu N` tampil sebagai `T0 − 20 hari` dengan Date Format General Settings
34. Verifikasi Last Updated baris Borrower `Wahyu N` tampil sebagai `T0 − 15 hari` dengan Date Format General Settings
35. Klik header kolom Actions `⋯`
36. Centang `Source` pada panel Column Visibility
37. Verifikasi kelima baris menampilkan Source `Admin`
38. Hapus centang `Source` pada panel Column Visibility

### Aksi baris dan Download By Transaction
39. Klik `⋯` pada baris Borrower `Zaki F`
40. Verifikasi menu baris pada tabel History memuat `Detail`
41. Klik `Detail`
42. Verifikasi halaman Borrow Detail terbuka untuk BRW baris Borrower `Zaki F` tanpa tombol aksi `Hand Over`, `Return`, `Request Extension`, dan `Cancel Borrow`
43. Kembali ke tab History lewat segmen Origin Tab pada breadcrumb
44. Klik `Download`
45. Pilih `Download as CSV`
46. Verifikasi berkas terunduh memuat 5 baris data milik spec ini sesuai saringan dan kolom yang tampil

### View By Asset memuat setiap baris yang sudah selesai
47. Klik view `By Asset`
48. Ketik Search `{runId}`, tekan Enter
49. Verifikasi hasil Search memuat 9 baris dengan aset `Laptop Asus ExpertBook B1402 {runId}`, `Mouse Logitech M331 {runId}`, `Kamera Fujifilm X-T30 {runId}`, `Tripod Manfrotto Compact {runId}`, `Proyektor BenQ MH550 {runId}`, `Speaker Bose S1 Pro {runId}`, `Mikrofon Shure SM58 {runId}`, `Tablet Apple iPad Air {runId}`, dan `Drone DJI Mini 3 {runId}`
50. Verifikasi aset `Drone DJI Mini 3 {runId}` tampil walau BRW-nya masih memuat baris aktif
51. Verifikasi aset `Baterai DJI Intelligent {runId}` yang masih Borrowed tidak tampil
52. Verifikasi urutan awal: `Drone DJI Mini 3 {runId}` tampil sebelum `Tablet Apple iPad Air {runId}`, lalu `Proyektor BenQ MH550 {runId}`, lalu `Laptop Asus ExpertBook B1402 {runId}`, lalu `Kamera Fujifilm X-T30 {runId}`

### Isi kolom By Asset
53. Klik header kolom `Photo`
54. Verifikasi klik header `Photo` tidak mengubah urutan baris
55. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Name yang memuat nama aset tersebut
56. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Asset ID milik DU-007-2
57. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Brand `Asus` dan baris aset `Mouse Logitech M331 {runId}` menampilkan Brand `Logitech`
58. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Model/Type `B1402` dan baris aset `Mouse Logitech M331 {runId}` menampilkan Model/Type `M331`
59. Verifikasi baris aset `Speaker Bose S1 Pro {runId}` menampilkan Group `Branch Surabaya` dan baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Group `Head Office`
60. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan status `Returned`
61. Verifikasi baris aset `Kamera Fujifilm X-T30 {runId}` menampilkan status `Returned` dengan penanda `Damaged`
62. Verifikasi baris aset `Drone DJI Mini 3 {runId}` menampilkan status `Returned` dengan penanda `Missing`
63. Verifikasi baris aset `Proyektor BenQ MH550 {runId}` menampilkan status `Rejected` dan baris aset `Speaker Bose S1 Pro {runId}` menampilkan status `Canceled`
64. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Transaction ID yang sama dengan baris aset `Mouse Logitech M331 {runId}` sebagai tautan
65. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Borrower `Wahyu N` dan baris aset `Tablet Apple iPad Air {runId}` menampilkan Borrower `Bagas P`
66. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Handed Over At `T0 − 19 hari` dan baris aset `Proyektor BenQ MH550 {runId}` menampilkan `—`
67. Verifikasi baris aset `Tablet Apple iPad Air {runId}` menampilkan Returned At `T0 − 5 hari` dengan `late 2 days`
68. Verifikasi baris aset `Proyektor BenQ MH550 {runId}` dan `Speaker Bose S1 Pro {runId}` menampilkan Returned At `—`
69. Verifikasi baris aset `Tablet Apple iPad Air {runId}` menampilkan Extensions `1 / 3` dan baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Extensions `0 / 3`
70. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Last Updated `T0 − 15 hari` dengan Date Format General Settings

### Kolom tambahan By Asset dan Search pada kolom tersembunyi
71. Ganti isi kotak search dengan `NFC`, tekan Enter
72. Verifikasi baris aset `Kamera Fujifilm X-T30 {runId}` tidak tampil karena kolom `TAG` tersembunyi
73. Klik header kolom Actions `⋯`
74. Centang `TAG` pada panel Column Visibility
75. Verifikasi baris aset `Kamera Fujifilm X-T30 {runId}` tampil dengan ikon TAG `NFC`
76. Verifikasi baris aset `Mouse Logitech M331 {runId}` menampilkan `—` pada kolom `TAG`
77. Ganti isi kotak search dengan `{runId}`, tekan Enter
78. Centang `Category` pada panel Column Visibility
79. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Category `Laptop`
80. Centang `Reason` pada panel Column Visibility
81. Verifikasi baris aset `Proyektor BenQ MH550 {runId}` menampilkan Reason `Anggaran belum disetujui` apa adanya
82. Verifikasi baris aset `Speaker Bose S1 Pro {runId}` menampilkan Reason `Timed out (Waiting for Approval)`
83. Verifikasi baris aset `Mikrofon Shure SM58 {runId}` menampilkan Reason `—`
84. Centang `Handover Photo` pada panel Column Visibility
85. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan thumbnail foto handover dan baris aset `Mouse Logitech M331 {runId}` menampilkan `—`
86. Centang `Return Photo` pada panel Column Visibility
87. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan thumbnail foto return dan baris aset `Mouse Logitech M331 {runId}` menampilkan `—`
88. Centang `Source` pada panel Column Visibility
89. Verifikasi kesembilan baris menampilkan Source `Admin`
90. Centang `Purpose` pada panel Column Visibility
91. Verifikasi baris aset `Laptop Asus ExpertBook B1402 {runId}` menampilkan Purpose `Pelatihan karyawan`

### Opsi Status By Asset
92. Klik `Filter`
93. Klik field `Status`
94. Verifikasi opsi `Returned`, `Returned · Damaged`, `Returned · Missing`, `Rejected`, dan `Canceled` tampil
95. Tutup daftar opsi field `Status`
96. Tutup Filter Panel tanpa klik `[Apply]`

### Aksi baris dan Download By Asset
97. Klik `⋯` pada baris aset `Laptop Asus ExpertBook B1402 {runId}`
98. Verifikasi menu baris memuat `Borrow Log`
99. Klik `Borrow Log`
100. Verifikasi dialog Borrow Log terbuka untuk aset `Laptop Asus ExpertBook B1402 {runId}`
101. Tutup dialog Borrow Log
102. Klik `Download`
103. Pilih `Download as XLSX`
104. Verifikasi berkas terunduh memuat 9 baris data milik spec ini sesuai saringan dan kolom yang tampil

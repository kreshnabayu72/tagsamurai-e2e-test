---
id: TC-FA-BORROW-E2E-005-tab-borrowed-assets-by-asset
title: "Tab Borrowed Assets By Asset menampilkan baris Borrowed dan Overdue dengan urutan awal, Remaining, dan aksi baris"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1j#p1", "§4.1j#p2", "§4.1j#r1", "§4.1j#r2", "§4.1j#r3", "§4.1j#r4", "§4.1j#r5", "§4.1j#r6", "§4.1j#r7", "§4.1j#r8", "§4.1j#r9", "§4.1j#r10", "§4.1j#r11", "§4.1j#r12", "§4.1j#r13", "§4.1j#r14", "§4.1j#r15", "§4.1j#r16", "§4.1j#r17", "§4.1j#r18", "§4.1j#p5", "§4.1j#r19", "§4.1j#r20", "§4.1j#r21", "§4.1j#r22", "§4.1j#r23", "§4.1j#r24", "§4.1j#r25", "§4.1j#r26", "§9.5#r4", "§9.5#r5", "EB-SRC-5@tabel-borrowed-assets"]
smoke: []
dependsOn: []
trace:
  "§4.1j#p1": [2, 4, 5]
  "§4.1j#p2": [7, 8]
  "§4.1j#r1": [11]
  "§4.1j#r2": [12, 48]
  "§4.1j#r3": [13]
  "§4.1j#r4": [14, 48, 52]
  "§4.1j#r5": [15, 48]
  "§4.1j#r6": [16, 17, 48]
  "§4.1j#r7": [18, 19, 20, 21, 48]
  "§4.1j#r8": [32, 33, 48]
  "§4.1j#r9": [36, 48]
  "§4.1j#r10": [22, 23, 48]
  "§4.1j#r11": [6, 24]
  "§4.1j#r12": [25]
  "§4.1j#r13": [26, 27, 48, 56]
  "§4.1j#r14": [38, 48]
  "§4.1j#r15": [40, 48]
  "§4.1j#r16": [42, 48]
  "§4.1j#r17": [44]
  "§4.1j#r18": [46, 48]
  "§4.1j#p5": [58]
  "§4.1j#r19": [58, 61, 72]
  "§4.1j#r20": [58, 72, 83]
  "§4.1j#r21": [87, 90, 92]
  "§4.1j#r22": [58, 73, 79]
  "§4.1j#r23": [58, 65, 73]
  "§4.1j#r24": [58, 69, 72]
  "§4.1j#r25": [59, 72, 75]
  "§4.1j#r26": [95]
  "§9.5#r4": [2]
  "§9.5#r5": [6, 9]
  "EB-SRC-5@tabel-borrowed-assets": [29, 32]
anchor: []
coverage:
  web: automated
---

# Tab Borrowed Assets By Asset menampilkan baris Borrowed dan Overdue dengan urutan awal, Remaining, dan aksi baris

## Prerequisites
- Aktor: Total Control `Admin Borrow {runId}` (DU-005-1), cakupan seluruh client.
- Layar awal: Transactions > Borrow, tab Transactions.
- Data:
  - DU-005-1: User `Admin Borrow {runId}`, role Total Control, cakupan seluruh client; pelapor Damage Report pada DU-005-8.
  - Pengaju seluruh BRW: `Agus Pratama` (Asset Admin, Group penugasan `Head Office`), tampil `Agus P`. Peminjam, Group, dan status baris tiap aset ada di entri DU-005-2 sampai DU-005-8. BRW pemilik DU-005-4 dibuat lebih dulu daripada BRW pemilik DU-005-7.
  - DU-005-2: aset `Laptop Dell Latitude {runId}`, Brand `Dell`, Model/Type `Latitude 5440`, Category `Laptop`, TAG RFID, Group `Head Office`, Borrower `Andi Pratama` (tampil `Andi P`), status baris Overdue, Due Date `T0 − 3 hari`, Remaining `3 days overdue`, Handed Over At `T0 − 5 hari`, Extensions `0 / 3`, Source `Admin`, Purpose `Presentasi klien`, Handed Over By `Agus P`.
  - DU-005-3: aset `Monitor LG 24MK {runId}` dalam BRW yang sama dengan DU-005-2, Brand `LG`, Model/Type `24MK600M`, Category `Monitor`, TAG QR, Group `Head Office`, Borrower `Andi P`, status baris Overdue, Due Date `T0 − 2 hari`, Remaining `2 days overdue`, Handed Over At `T0 − 4 hari`, Purpose `Presentasi klien`.
  - DU-005-4: aset `Proyektor Epson EB-X06 {runId}`, Brand `Epson`, Model/Type `EB-X06`, Category `Proyektor`, TAG RFID, Group `Head Office`, Borrower `Budi Santoso` (tampil `Budi S`), status baris Borrowed, Due Date `T0 + 2 hari`, Remaining `Due in 2 days`, Handed Over At `T0 − 3 hari`, Extensions `0 / 3`, Purpose `Rapat divisi`.
  - DU-005-5: aset `Kamera Sony A6400 {runId}`, Brand `Sony`, Model/Type `A6400`, Category `Kamera`, TAG NFC, Group `Branch Surabaya`, Borrower `Maya Putri` (tampil `Maya P`), status baris Borrowed, Due Date `T0`, Remaining `Due today`.
  - DU-005-6: aset `Kabel HDMI Premium {runId}` dalam BRW yang sama dengan DU-005-5, Brand `Ugreen`, Model/Type `HD104`, Category `Kabel`, Non TAG, Group `Branch Surabaya`, Borrower `Maya P`, status baris Borrowed, Due Date `T0`, Remaining `Due today`.
  - DU-005-7: aset `Tablet Samsung Tab A9 {runId}`, Brand `Samsung`, Model/Type `Tab A9`, Category `Tablet`, TAG RFID, Group `Head Office`, Borrower `Dewi Lestari` (tampil `Dewi L`), status baris Borrowed dengan pengajuan Extend yang menunggu approval (tampil `Extension Approval`), Due Date `T0 + 2 hari`, Remaining `Due in 2 days`.
  - DU-005-8: aset `Speaker JBL Charge 5 {runId}`, Brand `JBL`, Model/Type `Charge 5`, Category `Speaker`, TAG QR, Group `Head Office`, Borrower `Budi S`, status baris Borrowed dengan Damage Report berstatus Waiting for Confirmation yang dilaporkan `Admin Borrow {runId}` (tampil badge `Reported Damaged`), Due Date `T0 + 6 hari`, Remaining `Due in 6 days`.
  - DU-005-9: aset `Printer Epson L3250 {runId}` pada BRW Borrower `Citra Dewi` berstatus Waiting for Handover.
  - DU-005-10: aset `Scanner Canon LiDE 400 {runId}` pada BRW Borrower `Hendra Wijaya` berstatus Returned.
- Kondisi:
  - Date Format dan Time Format di General Settings entitas berlaku untuk tampilan Due Date dan Handed Over At.
  - Max extensions efektif seluruh aset pada spec ini bernilai `3`.

## Test Steps

### Tab Borrowed Assets hanya memuat aset yang sedang dipinjam
1. Klik tab `Borrowed Assets`
2. Verifikasi sub-tab `By Asset` aktif
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi hasil Search memuat 7 baris dengan aset `Laptop Dell Latitude {runId}`, `Monitor LG 24MK {runId}`, `Proyektor Epson EB-X06 {runId}`, `Kamera Sony A6400 {runId}`, `Kabel HDMI Premium {runId}`, `Tablet Samsung Tab A9 {runId}`, dan `Speaker JBL Charge 5 {runId}`
5. Verifikasi aset `Printer Epson L3250 {runId}` (Waiting for Handover) dan `Scanner Canon LiDE 400 {runId}` (Returned) tidak tampil

### Urutan awal By Asset
6. Verifikasi `Laptop Dell Latitude {runId}` (`3 days overdue`) tampil sebelum `Monitor LG 24MK {runId}` (`2 days overdue`), dan keduanya tampil sebelum semua baris lain
7. Verifikasi `Kabel HDMI Premium {runId}` tampil sebelum `Kamera Sony A6400 {runId}`, karena Due Date dan Transaction ID sama sehingga diurutkan menurut nama aset
8. Verifikasi `Proyektor Epson EB-X06 {runId}` tampil sebelum `Tablet Samsung Tab A9 {runId}`, karena Due Date sama dan Transaction ID aset pertama lebih kecil
9. Verifikasi `Speaker JBL Charge 5 {runId}` (`Due in 6 days`) tampil paling akhir, karena Due Date-nya paling jauh

### Isi kolom yang tampil sejak awal
10. Klik header kolom `Photo`
11. Verifikasi urutan baris tidak berubah karena kolom `Photo` tidak dapat diurutkan
12. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Name yang memuat nama aset tersebut
13. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Asset ID milik DU-005-2
14. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Brand `Dell`, baris aset `Proyektor Epson EB-X06 {runId}` menampilkan Brand `Epson`, dan baris aset `Kamera Sony A6400 {runId}` menampilkan Brand `Sony`
15. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Model/Type `Latitude 5440`, baris aset `Proyektor Epson EB-X06 {runId}` menampilkan Model/Type `EB-X06`, dan baris aset `Kamera Sony A6400 {runId}` menampilkan Model/Type `A6400`
16. Verifikasi baris aset `Laptop Dell Latitude {runId}`, `Proyektor Epson EB-X06 {runId}`, `Tablet Samsung Tab A9 {runId}`, dan `Speaker JBL Charge 5 {runId}` menampilkan Group `Head Office`
17. Verifikasi baris aset `Kamera Sony A6400 {runId}` dan `Kabel HDMI Premium {runId}` menampilkan Group `Branch Surabaya`
18. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan status `Overdue`
19. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` menampilkan status `Borrowed`
20. Verifikasi baris aset `Tablet Samsung Tab A9 {runId}` menampilkan status `Extension Approval`
21. Verifikasi baris aset `Speaker JBL Charge 5 {runId}` menampilkan status `Borrowed` dan badge `Reported Damaged`
22. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Due Date `T0 − 3 hari` sesuai Date Format General Settings
23. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` menampilkan Due Date `T0 + 2 hari` sesuai Date Format General Settings
24. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Remaining `3 days overdue`, baris aset `Proyektor Epson EB-X06 {runId}` menampilkan Remaining `Due in 2 days`, dan baris aset `Kamera Sony A6400 {runId}` menampilkan Remaining `Due today`
25. Verifikasi Transaction ID pada setiap baris aset berupa tautan yang dapat diklik
26. Verifikasi baris aset `Laptop Dell Latitude {runId}` dan `Monitor LG 24MK {runId}` menampilkan Borrower `Andi P`
27. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` dan `Speaker JBL Charge 5 {runId}` menampilkan Borrower `Budi S`

### Search tidak mencocokkan kolom TAG yang tersembunyi dan mencocokkannya lagi saat ditampilkan
28. Ganti isi kotak search dengan `NFC`, tekan Enter
29. Verifikasi baris aset `Kamera Sony A6400 {runId}` tidak tampil karena kolom `TAG` tersembunyi
30. Klik header kolom Actions `⋯`
31. Centang `TAG` pada panel Column Visibility
32. Verifikasi baris aset `Kamera Sony A6400 {runId}` tampil dengan ikon TAG `NFC`
33. Verifikasi baris aset `Kabel HDMI Premium {runId}` menampilkan `—` pada kolom `TAG`
34. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Isi kolom tambahan yang ditampilkan lewat Column Visibility
35. Centang `Category` pada panel Column Visibility
36. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Category `Laptop`
37. Centang `Handed Over At` pada panel Column Visibility
38. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Handed Over At `T0 − 5 hari` sesuai Date Format General Settings
39. Centang `Extensions` pada panel Column Visibility
40. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` menampilkan Extensions `0 / 3`
41. Centang `Source` pada panel Column Visibility
42. Verifikasi setiap baris menampilkan Source `Admin`
43. Centang `Purpose` pada panel Column Visibility
44. Verifikasi baris aset `Laptop Dell Latitude {runId}` menampilkan Purpose `Presentasi klien` dan baris aset `Proyektor Epson EB-X06 {runId}` menampilkan Purpose `Rapat divisi`
45. Centang `Handed Over By` pada panel Column Visibility
46. Verifikasi setiap baris menampilkan Handed Over By `Agus P`

### Filter Panel memuat field kolom yang filterable
47. Klik `Filter`
48. Verifikasi Filter Panel memuat field `Asset Name`, `Brand`, `Model/Type`, `Group`, `Status`, `TAG`, `Category`, `Due Date`, `Handed Over At`, `Extensions`, `Source`, `Borrower`, dan `Handed Over By`
49. Klik field `Brand`
50. Pilih opsi `Epson`
51. Klik `[Apply]`
52. Verifikasi baris aset `Proyektor Epson EB-X06 {runId}` tampil dan baris aset `Laptop Dell Latitude {runId}` tidak tampil
53. Klik `[Clear Field]`
54. Klik `[Apply]`

### Sort kolom Borrower
55. Klik header kolom `Borrower`
56. Verifikasi kolom Borrower dari atas ke bawah berurutan `Andi P`, `Andi P`, `Budi S`, `Budi S`, `Dewi L`, `Maya P`, lalu `Maya P`

### Aksi baris pada aset Borrowed tanpa Damage Report
57. Klik `⋯` pada baris aset `Proyektor Epson EB-X06 {runId}`
58. Verifikasi menu baris memuat `Borrow Log`, `Return`, `Request Extension`, `Report Damaged`, dan `Report Missing`
59. Verifikasi menu baris tidak memuat `Cancel Damage Report`
60. Klik `Borrow Log`
61. Verifikasi dialog Borrow Log terbuka untuk aset `Proyektor Epson EB-X06 {runId}`
62. Tutup dialog Borrow Log
63. Klik `⋯` pada baris aset `Proyektor Epson EB-X06 {runId}`
64. Klik `Report Damaged`
65. Verifikasi dialog `Report Damaged` terbuka
66. Tutup dialog `Report Damaged` tanpa menyimpan
67. Klik `⋯` pada baris aset `Proyektor Epson EB-X06 {runId}`
68. Klik `Report Missing`
69. Verifikasi dialog `Report Missing` terbuka
70. Tutup dialog `Report Missing` tanpa menyimpan

### Aksi baris pada aset yang sudah dilaporkan rusak oleh aktor
71. Klik `⋯` pada baris aset `Speaker JBL Charge 5 {runId}`
72. Verifikasi menu baris memuat `Borrow Log`, `Return`, `Report Missing`, dan `Cancel Damage Report`
73. Verifikasi menu baris tidak memuat `Request Extension` dan `Report Damaged`
74. Klik `Cancel Damage Report`
75. Verifikasi dialog Cancel Damage Report terbuka untuk aset `Speaker JBL Charge 5 {runId}`
76. Tutup dialog Cancel Damage Report tanpa mengonfirmasi

### Request Extension dan Return per aset membuka halaman dengan aset itu saja
77. Klik `⋯` pada baris aset `Proyektor Epson EB-X06 {runId}`
78. Klik `Request Extension`
79. Verifikasi halaman `Extension Request` terbuka dengan baris aset `Proyektor Epson EB-X06 {runId}` saja
80. Kembali ke tab Borrowed Assets lewat segmen Origin Tab pada breadcrumb
81. Klik `⋯` pada baris aset `Proyektor Epson EB-X06 {runId}`
82. Klik `Return`
83. Verifikasi halaman `Return Asset` terbuka dengan Borrower `Budi S` dan aset `Proyektor Epson EB-X06 {runId}` saja
84. Kembali ke tab Borrowed Assets lewat segmen Origin Tab pada breadcrumb

### Bulk Return hanya untuk aset satu Borrower
85. Centang baris aset `Laptop Dell Latitude {runId}`
86. Centang baris aset `Proyektor Epson EB-X06 {runId}`
87. Verifikasi aksi bulk `Return` disabled dengan tooltip `Select assets of one borrower only.`
88. Hapus centang baris aset `Proyektor Epson EB-X06 {runId}`
89. Centang baris aset `Monitor LG 24MK {runId}`
90. Verifikasi aksi bulk `Return` aktif
91. Klik aksi bulk `Return`
92. Verifikasi halaman `Return Asset` terbuka dengan Borrower `Andi P` dan aset `Laptop Dell Latitude {runId}` serta `Monitor LG 24MK {runId}`
93. Kembali ke tab Borrowed Assets lewat segmen Origin Tab pada breadcrumb

### Download di toolbar
94. Klik `Download`
95. Verifikasi `Download` pada toolbar menawarkan `Download as CSV` dan `Download as XLSX`

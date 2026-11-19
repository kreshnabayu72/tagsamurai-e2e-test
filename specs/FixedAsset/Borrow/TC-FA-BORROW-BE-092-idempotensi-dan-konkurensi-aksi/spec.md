---
id: TC-FA-BORROW-BE-092-idempotensi-dan-konkurensi-aksi
title: "Idempotensi, atomisitas, dan hasil pasangan aksi tulis yang mengenai record yang sama"
layer: be-e2e
priority: Medium
caseType: Edge
status: ready-for-automation
sourceRules: ["EC-BRW-73", "§9.6#r1", "§9.6#r2", "§9.6#r3", "§9.6#r4", "§9.6#r5", "§9.6#r6", "§9.6#r7", "§9.6#r8", "§9.6#r9", "§9.6#r10", "§9.6#r11", "§9.6#r12", "§9.6#r13", "§9.6#r14", "§9.6#r15", "§9.6#r16", "§9.6#r17", "§9.6#r18", "§9.6#r19", "EB-ERR-3", "EB-CON-3", "EB-EDG-1"]
smoke: []
dependsOn: []
owner: BE
trace:
  "EC-BRW-73": [109, 111, 113, 115]
  "§9.6#r1": [2, 3, 4, 8, 9, 11, 12]
  "§9.6#r2": 6
  "§9.6#r3": [14, 15, 16, 18, 19]
  "§9.6#r4": [21, 22, 23]
  "§9.6#r5": [27, 28, 29, 31]
  "§9.6#r6": [34, 35, 36, 38, 39]
  "§9.6#r7": [42, 43, 44]
  "§9.6#r8": [47, 48, 49]
  "§9.6#r9": [51, 52, 53, 61, 62]
  "§9.6#r10": [55, 56, 58]
  "§9.6#r11": [65, 67, 68, 69]
  "§9.6#r12": [71, 73, 75, 76]
  "§9.6#r13": [78, 79]
  "§9.6#r14": [82, 83, 84]
  "§9.6#r15": 88
  "§9.6#r16": [90, 92, 94, 96]
  "§9.6#r17": [98, 99, 101]
  "§9.6#r18": [103, 104]
  "§9.6#r19": [106, 107]
  "EB-ERR-3": [25, 96]
  "EB-CON-3": [11, 38, 75, 82]
  "EB-EDG-1": [67, 86, 96, 101, 111]
---

# Idempotensi, atomisitas, dan hasil pasangan aksi tulis yang mengenai record yang sama

## Prerequisites
- Aktor:
  - Asset Admin DU-092-26, Group penugasan Head Office dan Branch Surabaya (pelaku utama).
  - Asset Admin DU-092-27, Group penugasan Head Office (Aktor Borrow kedua, pelaku penghapusan Draft di luar cakupan).
  - Aktor Missing DU-092-37, Group penugasan Head Office.
  - Approver DU-092-28 dan Approver DU-092-29, Group penugasan Head Office, keduanya eligible untuk aset Head Office dengan mode Any one.
  - Borrower DU-092-30 dan Borrower DU-092-31, punya akun login.
- Data:
  - DU-092-5: Asset, aset Draft yang disimpan, diubah versi, dan dihapus; Asset Name `Laptop Dell Inspiron 15 {runId}`; Group `Head Office`.
  - DU-092-6: Asset, aset yang ditambahkan Aktor Borrow kedua ke Draft; Asset Name `Monitor Samsung Odyssey G5 {runId}`; Group `Head Office`.
  - DU-092-7: Asset, aset yang ditambahkan lewat Add to Borrow Draft; Asset Name `Keyboard Logitech MX Keys {runId}`; Group `Head Office`.
  - DU-092-8: Asset, aset untuk Submit berulang dan Submit bentrok; Asset Name `Proyektor Epson EB-X06 {runId}`; Group `Head Office`.
  - DU-092-9: Asset, aset untuk Borrow Now bersamaan; Asset Name `Kamera Canon EOS 90D {runId}`; Group `Head Office`.
  - DU-092-10: Asset, aset untuk Approve, Handover, dan Return; Asset Name `Laptop HP EliteBook 840 {runId}`; Group `Head Office`.
  - DU-092-11: Asset, aset dengan sesi handover yang dibatalkan; Asset Name `Tablet Samsung Galaxy Tab S7 {runId}`; Group `Head Office`.
  - DU-092-12: Asset, aset Borrowed untuk Extend berulang; Asset Name `Speaker Bose SoundLink Flex {runId}`; Group `Head Office`.
  - DU-092-13: Asset, aset Borrowed yang dikembalikan sebelum Extend gabungan; Asset Name `Mikrofon Shure MV7 {runId}`; Group `Head Office`.
  - DU-092-14: Asset, aset yang dibatalkan Borrower lebih dulu; Asset Name `Printer Epson L3250 {runId}`; Group `Head Office`.
  - DU-092-15: Asset, aset Borrowed untuk Mark as Returned yang ditolak; Asset Name `Scanner Canon DR-C225 {runId}`; Group `Head Office`.
  - DU-092-16: Asset, aset Waiting for Handover untuk Remind Borrower; Asset Name `Drone DJI Mini 3 {runId}`; Group `Head Office`.
  - DU-092-17: Asset, aset yang dikembalikan dari tempat lain; Asset Name `Gimbal DJI RS 3 {runId}`; Group `Head Office`.
  - DU-092-18: Asset, aset Return dengan Report Damaged; Asset Name `Laptop Asus Vivobook S14 {runId}`; Group `Head Office`.
  - DU-092-19: Asset, aset dengan Request Extension menunggu review; Asset Name `Monitor LG 27UL500 {runId}`; Group `Head Office`.
  - DU-092-20: Asset, aset dengan Extension menunggu approval; Asset Name `Kamera Sony ZV-1 {runId}`; Group `Head Office`.
  - DU-092-21: Asset, aset Group Head Office dalam Draft yang memuat Group di luar cakupan; Asset Name `Tablet Apple iPad 10th Gen {runId}`; Group `Head Office`.
  - DU-092-22: Asset, aset Group Branch Surabaya dalam Draft yang memuat Group di luar cakupan; Asset Name `Laptop Lenovo IdeaPad 5 {runId}`; Group `Branch Surabaya`.
  - DU-092-23: Asset, aset Draft bulk pertama; Asset Name `Printer HP LaserJet Pro M404 {runId}`; Group `Head Office`.
  - DU-092-24: Asset, aset Draft bulk kedua; Asset Name `Scanner Fujitsu ScanSnap iX1600 {runId}`; Group `Head Office`.
  - DU-092-25: Parameter pengajuan idempotensi, Duration dan Purpose pengajuan; Duration `4 Day(s)`; Purpose `Pemakaian harian {runId}`.
  - DU-092-26: User, Asset Admin pelaku utama; Name `Lestari Handayani {runId}`; Role `Asset Admin`.
  - DU-092-27: User, Asset Admin kedua; Name `Taufik Hidayat {runId}`; Role `Asset Admin`.
  - DU-092-28: User, Approver pertama; Name `Ningsih Rahayu {runId}`; Role `Approver`.
  - DU-092-29: User, Approver kedua; Name `Joko Santoso {runId}`; Role `Approver`.
  - DU-092-30: User, Borrower pertama yang punya akun login; Name `Oktavia Putri {runId}`.
  - DU-092-31: User, Borrower kedua yang punya akun login; Name `Hendro Wibowo {runId}`.
  - DU-092-32: Parameter Extension idempotensi, Durasi Extension yang diajukan; Extend duration `2 Day(s)`.
  - DU-092-33: Deskripsi Return rusak, What happened pada Return dengan Report Damaged; What happened `Layar retak di pojok kiri bawah {runId}`.
  - DU-092-34: Approve Duration valid, Approve Duration yang tidak melebihi Extend By; Approve Duration `1 Day(s)`.
  - DU-092-35: Approve Duration melebihi, Approve Duration yang melebihi Extend By; Approve Duration `3 Day(s)`.
  - DU-092-36: Asset, aset Borrowed yang ditutup Missing oleh Aktor Missing; Asset Name `Handheld Zebra TC21 {runId}`; Group `Head Office`.
  - DU-092-37: User, Aktor Missing di Group Head Office; Name `Wulan Kartika {runId}`; Group `Head Office`; Role `Asset Admin` dengan hak Aktor Missing.
  - DU-092-38: Reason Missing, Reason laporan kehilangan oleh Aktor Missing; Reason `Aset tidak ditemukan saat inventaris {runId}`.
  - DU-092-39: Photo Return rusak, Photo laporan Damaged pada Return; Photo `kerusakan-layar-{runId}.jpg`.
  - DU-092-40: Asset, aset Group Branch Surabaya dalam Draft yang di luar cakupan Asset Admin DU-092-27; Asset Name `Printer Canon imageCLASS MF445dw {runId}`; Group `Branch Surabaya`.
  - DU-092-41: Asset, aset yang ditolak masuk ke Draft di luar cakupan; Asset Name `Monitor Dell P2422H {runId}`; Group `Head Office`.
  - DU-092-42: Asset, aset Borrowed pada BRW pertama untuk Return gabungan; Asset Name `Laptop Acer TravelMate P2 {runId}`; Group `Head Office`.
  - DU-092-43: Asset, aset Borrowed pada BRW kedua yang dikembalikan lebih dulu dari tempat lain; Asset Name `Proyektor ViewSonic PA503S {runId}`; Group `Head Office`.
- Kondisi:
  - Level Borrowing entitas suite adalah Full dan Approval Workflow aktif.
  - Draft berisi aset DU-092-23 dan Draft berisi aset DU-092-24 milik Asset Admin DU-092-26; Draft berisi aset DU-092-21 dan aset DU-092-22 milik Total Control; satu Draft tanpa aset milik Asset Admin DU-092-26.
  - Baris aset DU-092-11, DU-092-14, dan DU-092-16 berstatus `Waiting for Handover` untuk Borrower DU-092-30.
  - Baris aset DU-092-12, DU-092-13, DU-092-15, DU-092-17, DU-092-18, DU-092-19, dan DU-092-20 berstatus `Borrowed` untuk Borrower DU-092-30, masing-masing dalam BRW sendiri dan Due date lebih dari 3 hari lagi.
  - Aset DU-092-19 punya Request Extension dari Borrower DU-092-30 dengan Extend By `2 Day(s)` yang menunggu review; aset DU-092-20 punya Extension yang diajukan Asset Admin DU-092-26 dan menunggu approval.
  - Aturan efektif aset DU-092-9 memuat Self service ON dan Allowed borrower yang mencakup Borrower DU-092-30 dan Borrower DU-092-31.
  - Aturan efektif aset DU-092-12, DU-092-13, dan DU-092-19 memuat Require approval OFF, sehingga Extend atas aset itu langsung berlaku.
  - Baris aset DU-092-36, DU-092-42, dan DU-092-43 berstatus `Borrowed` untuk Borrower DU-092-30, masing-masing dalam BRW sendiri dan Due date lebih dari 3 hari lagi. Akun DU-092-37 aktif dan kredensialnya disediakan fase 2.
  - Draft berisi aset DU-092-40 untuk Borrower DU-092-31 milik Total Control, hanya berisi aset Group Branch Surabaya.

## Test Steps

### Save Draft: cek versi, tanpa perubahan, dan log
1. Asset Admin DU-092-26 menyimpan Draft berisi aset DU-092-5 untuk Borrower DU-092-30
2. Verifikasi Draft berisi aset DU-092-5 tersimpan dan Transaction admin log Asset Admin DU-092-26 bertambah satu entri untuk Draft itu
3. Verifikasi header Draft dan baris aset DU-092-5 tersimpan bersama dalam satu transaksi
4. Verifikasi Last Updated Draft berisi aset DU-092-5 terisi pada penyimpanan pertama
5. Asset Admin DU-092-26 menyimpan lagi Draft berisi aset DU-092-5 tanpa mengubah isinya
6. Verifikasi penyimpanan Draft tanpa perubahan berhasil sebagai no-op, tanpa tulis, dan tidak menambah entri Transaction admin log
7. Asset Admin DU-092-27 menyimpan Draft yang sama dengan menambahkan aset DU-092-6
8. Verifikasi Transaction admin log Asset Admin DU-092-27 bertambah satu entri untuk penyimpanan Draft yang mengubah isinya
9. Verifikasi Last Updated Draft berisi aset DU-092-5 dan aset DU-092-6 diperbarui menjadi lebih baru daripada Last Updated penyimpanan pertama
10. Asset Admin DU-092-26 menyimpan Draft yang sama dari versi lama dengan Purpose `Pemakaian harian {runId}`
11. Verifikasi penyimpanan dari versi lama ditolak dengan `This draft was changed by [Name] at [Time]. Reload to see the latest version; your unsaved changes will be lost.`
12. Verifikasi Draft tidak berubah oleh penyimpanan yang ditolak dan tetap memuat aset DU-092-5 dan aset DU-092-6

### Add to Borrow Draft melewati aset yang sudah ada
13. Asset Admin DU-092-26 menjalankan `Add to Borrow Draft` untuk aset DU-092-5 dan aset DU-092-7 ke Draft Borrower DU-092-30
14. Verifikasi aset DU-092-5 yang sudah ada di Draft dilewati dan hanya aset DU-092-7 yang bertambah
15. Verifikasi penambahan aset ke Draft bersifat atomik per Draft dan tercatat di Transaction admin log
16. Verifikasi aset DU-092-7 tidak terkunci dan tanpa snapshot, dan status Custody aset DU-092-7 tetap `Available`

### Add to Borrow Draft oleh Aktor di luar cakupan Group Draft ditolak
17. Asset Admin DU-092-27 menjalankan `Add to Borrow Draft` untuk aset DU-092-41 ke Draft Borrower DU-092-31 yang berisi aset DU-092-40
18. Verifikasi penambahan aset DU-092-41 ke Draft berisi aset DU-092-40 ditolak karena Draft di luar cakupan Group Asset Admin DU-092-27
19. Verifikasi Draft berisi aset DU-092-40 tidak berubah dan tidak memuat aset DU-092-41

### Submit idempoten dan atomik
20. Asset Admin DU-092-26 mengirim Submit atas aset DU-092-8 untuk Borrower DU-092-30 dengan Duration `4 Day(s)` dan Purpose `Pemakaian harian {runId}` dua kali dengan kunci idempotensi yang sama
21. Verifikasi hanya satu BRW terbentuk untuk aset DU-092-8 dari dua pengiriman Submit
22. Verifikasi baris, Custody, snapshot, dan pengajuan approval aset DU-092-8 terbentuk bersama dalam satu transaksi
23. Verifikasi Borrow Log aset DU-092-8 memuat satu node `Borrow requested by [Actor]` dan Transaction admin log Asset Admin DU-092-26 memuat satu entri Submit
24. Asset Admin DU-092-27 mengajukan BRW untuk aset DU-092-8 atas nama Borrower DU-092-31 dengan Duration `4 Day(s)` dan Purpose `Pemakaian harian {runId}`
25. Verifikasi pengajuan kedua atas aset DU-092-8 yang sudah dipakai transaksi aktif ditolak guard dan tidak ada BRW baru

### Borrow Now dari dua pemindai bersamaan
26. Borrower DU-092-30 dan Borrower DU-092-31 menjalankan `Borrow Now` self-service atas aset DU-092-9 bersamaan dengan Duration `4 Day(s)` dan Purpose `Pemakaian harian {runId}`
27. Verifikasi tepat satu BRW terbentuk atas aset DU-092-9 dan pemindai lain ditolak tanpa mengubah data
28. Verifikasi BRW yang berhasil memuat baris `Borrowed` dan Custody aset DU-092-9 bernilai `Borrowed` dalam satu transaksi
29. Verifikasi peristiwa tercatat di Borrow Log, Transaction log aset, dan log pengguna Borrower pemenang
30. Borrower yang berhasil meminjam aset DU-092-9 mengirim ulang `Borrow Now` yang sama atas aset itu dengan kunci idempotensi yang sama
31. Verifikasi pengiriman ulang tidak membuat BRW kedua atas aset DU-092-9

### Approve dan Reject: keputusan per approver per aset
32. Asset Admin DU-092-26 mengajukan BRW untuk aset DU-092-10 atas nama Borrower DU-092-30 dengan Duration `4 Day(s)` dan Purpose `Pemakaian harian {runId}`
33. Approver DU-092-28 menyetujui aset DU-092-10 dua kali dengan kunci idempotensi yang sama
34. Verifikasi keputusan Approver DU-092-28 atas aset DU-092-10 tercatat sekali
35. Verifikasi keputusan aset, baris, Custody, dan notifikasi atas aset DU-092-10 berubah bersama dalam satu transaksi
36. Verifikasi keputusan tercatat di Borrow Log dan Transaction admin log Approver DU-092-28
37. Approver DU-092-29 menolak aset DU-092-10 sesudah keputusan Approver DU-092-28
38. Verifikasi keputusan Approver DU-092-29 ditolak dengan `You can no longer approve this request because it has already been done by another approver.`
39. Verifikasi aset DU-092-10 tetap memakai keputusan Approver DU-092-28 dan tidak berubah oleh penolakan yang ditolak

### Handover konfirmasi idempoten
40. Asset Admin DU-092-26 menyerahkan aset DU-092-10 kepada Borrower DU-092-30 dengan Condition `Normal`
41. Borrower DU-092-30 mengirim konfirmasi handover aset DU-092-10 dua kali
42. Verifikasi konfirmasi handover aset DU-092-10 menghasilkan satu baris `Borrowed`
43. Verifikasi baris dan Custody aset DU-092-10 berubah bersama dalam satu transaksi
44. Verifikasi handover tercatat satu kali di Borrow Log, Transaction log aset, dan Transaction admin log

### Cancel Request menutup sesi handover tanpa efek ulang
45. Asset Admin DU-092-26 memulai handover aset DU-092-11
46. Asset Admin DU-092-26 menjalankan `Cancel Request` atas sesi handover aset DU-092-11 dua kali
47. Verifikasi sesi handover aset DU-092-11 yang sudah ditutup tidak berefek pada permintaan kedua dan aset DU-092-11 tetap `Waiting for Handover`
48. Verifikasi Borrow Log aset DU-092-11 memuat satu node `Handover not confirmed`
49. Verifikasi sesi Cancel Request atomik per sesi Handover dan Task Borrower Borrower DU-092-30 untuk aset DU-092-11 hilang

### Return idempoten dan Report Damaged ikut Return
50. Asset Admin DU-092-26 menerima kembali aset DU-092-10 dengan Condition `Normal` dua kali dengan kunci idempotensi yang sama
51. Verifikasi Return aset DU-092-10 menghasilkan satu baris `Returned` dan satu node `Returned to [Receiver]`
52. Verifikasi baris dan Custody aset DU-092-10 berubah bersama dalam satu transaksi per BRW
53. Verifikasi Return tercatat di Borrow Log, Transaction log aset, dan Transaction admin log
54. Asset Admin DU-092-26 menerima kembali aset DU-092-18 dengan Report Damaged tanpa Photo dan dengan What happened `Layar retak di pojok kiri bawah {runId}`
55. Verifikasi Return aset DU-092-18 ditolak karena Photo wajib dan tidak ada laporan kerusakan yang dibuat
56. Verifikasi baris aset DU-092-18 tetap `Borrowed` dan BRW tidak berubah
57. Asset Admin DU-092-26 menerima kembali aset DU-092-18 dengan Report Damaged lengkap dengan Photo `kerusakan-layar-{runId}.jpg` dan What happened `Layar retak di pojok kiri bawah {runId}`
58. Verifikasi laporan kerusakan aset DU-092-18 tersimpan dalam transaksi BRW yang sama dengan Return

### Return gabungan: kegagalan satu BRW tidak membatalkan BRW lain
59. Asset Admin DU-092-26 menerima kembali aset DU-092-43 dengan Condition `Normal`
60. Asset Admin DU-092-27 menerima kembali aset DU-092-42 dan aset DU-092-43 sekaligus dengan Condition `Normal` dari halaman Return yang dibuka sebelum aset DU-092-43 dikembalikan
61. Verifikasi Return aset DU-092-43 ditolak karena baris sudah dikembalikan dan BRW aset DU-092-43 tidak berubah
62. Verifikasi Return aset DU-092-42 pada BRW lain tetap tersimpan sebagai `Returned` dan tidak ada perubahan sebagian di dalam satu BRW

### Extend idempoten dan kegagalan satu BRW tidak membatalkan BRW lain
63. Asset Admin DU-092-26 menerima kembali aset DU-092-13
64. Asset Admin DU-092-27 menjalankan Extend atas aset DU-092-12 dengan Extend duration `2 Day(s)` dua kali dengan kunci idempotensi yang sama
65. Verifikasi Due date aset DU-092-12 bertambah sekali dengan 2 hari
66. Asset Admin DU-092-27 menjalankan Extend gabungan atas aset DU-092-12 dan aset DU-092-13 dengan Extend duration `2 Day(s)` dari tabel Borrowed Assets yang dibuka sebelum aset DU-092-13 dikembalikan
67. Verifikasi Extend aset DU-092-13 ditolak karena baris sudah dikembalikan dan Due date aset DU-092-13 tidak berubah
68. Verifikasi Extend aset DU-092-12 pada BRW lain tetap berlaku dan tidak ada perubahan sebagian di dalam satu BRW
69. Verifikasi Extend tercatat di Borrow Log

### Review Extension Request: keputusan pertama berlaku
70. Asset Admin DU-092-26 mereview Request Extension Borrower DU-092-30 atas aset DU-092-19 dengan Approve Duration `3 Day(s)`
71. Verifikasi Approve Duration yang lebih besar dari Extend By yang diminta ditolak dan pengajuan tetap Extension Request
72. Asset Admin DU-092-26 mereview Request Extension Borrower DU-092-30 atas aset DU-092-19 dengan Approve Duration `1 Day(s)`
73. Verifikasi keputusan Asset Admin DU-092-26 berlaku dan Due date aset DU-092-19 bertambah 1 hari
74. Asset Admin DU-092-27 mereview Request Extension Borrower DU-092-30 atas aset DU-092-19 sesudah keputusan Asset Admin DU-092-26
75. Verifikasi pengiriman berikutnya ditolak dengan `You can no longer approve this request because it has already been done by another Asset Admin.`
76. Verifikasi review Extension atomik per BRW dan tercatat di Borrow Log

### Cancel Extension idempoten
77. Asset Admin DU-092-26 menjalankan Cancel Extension atas Extension aset DU-092-20 dua kali
78. Verifikasi Extension aset DU-092-20 dibatalkan sekali dan Borrow Log memuat satu node `Extension canceled by [Actor]`
79. Verifikasi pembatalan atomik per baris dan Due date aset DU-092-20 tidak berubah

### Cancel Borrow oleh Borrower lebih dulu dari Aktor Borrow
80. Borrower DU-092-30 membatalkan BRW aset DU-092-14 dari halaman pinjamannya
81. Asset Admin DU-092-26 menjalankan Cancel Borrow atas baris aset DU-092-14
82. Verifikasi Cancel Borrow oleh Aktor Borrow ditolak dengan `[Borrower] already canceled this borrow.` dan `Your action was not saved.`
83. Verifikasi baris aset DU-092-14 berstatus `Canceled` dan Custody aset DU-092-14 `Available` dalam satu transaksi
84. Verifikasi pembatalan oleh Borrower DU-092-30 tercatat satu kali di Borrow Log dan log pengguna Borrower DU-092-30, dan percobaan Cancel Borrow Asset Admin DU-092-26 yang ditolak tidak menulis entri Transaction admin log
85. Asset Admin DU-092-26 menjalankan Cancel Borrow sekali lagi atas baris aset DU-092-14
86. Verifikasi aksi atas baris aset DU-092-14 yang sudah selesai ditolak dan baris tidak berubah

### Mark as Returned ditolak di luar level None
87. Asset Admin DU-092-26 menjalankan Mark as Returned atas aset DU-092-15 yang berstatus Borrowed
88. Verifikasi Mark as Returned atas aset DU-092-15 ditolak server karena level Borrowing bukan None dan baris tetap `Borrowed`

### Delete Draft: cakupan, pembuat, dan idempotensi
89. Asset Admin DU-092-27 menghapus Draft berisi aset DU-092-21 dan aset DU-092-22
90. Verifikasi penghapusan Draft yang memuat Group di luar cakupan Asset Admin DU-092-27 ditolak dan Draft tetap ada
91. Asset Admin DU-092-27 menghapus Draft tanpa aset milik Asset Admin DU-092-26
92. Verifikasi penghapusan Draft tanpa aset oleh bukan pembuatnya ditolak dan Draft tetap ada
93. Asset Admin DU-092-26 menghapus Draft berisi aset DU-092-5, aset DU-092-6, dan aset DU-092-7
94. Verifikasi Draft berisi aset DU-092-5 terhapus atomik dan Transaction admin log Asset Admin DU-092-26 memuat satu entri Delete Draft
95. Asset Admin DU-092-27 menghapus Draft yang sama yang sudah dihapus pihak lain
96. Verifikasi Draft berisi aset DU-092-5 yang sudah dihapus pihak lain tetap terhapus dan penghapusan kedua tidak menambah entri Transaction admin log Asset Admin DU-092-27

### Bulk Delete Draft melewati yang di luar cakupan dan idempoten
97. Asset Admin DU-092-27 menjalankan bulk Delete Draft atas Draft berisi aset DU-092-23, Draft berisi aset DU-092-24, dan Draft berisi aset DU-092-21 dan aset DU-092-22
98. Verifikasi Draft berisi aset DU-092-23 dan aset DU-092-24 terhapus sedangkan Draft di luar cakupan dilewati dan tetap ada
99. Verifikasi penghapusan bulk atomik per Draft dan Transaction admin log Asset Admin DU-092-27 memuat satu entri untuk setiap Draft yang terhapus
100. Asset Admin DU-092-27 menjalankan bulk Delete Draft yang sama sekali lagi
101. Verifikasi Draft berisi aset DU-092-23 dan aset DU-092-24 yang sudah terhapus tetap terhapus tanpa entri log baru

### Remind Borrower tidak idempoten dan tanpa entri log
102. Asset Admin DU-092-26 menjalankan Remind Borrower atas baris aset DU-092-16 dua kali
103. Verifikasi notifikasi untuk Borrower DU-092-30 bertambah dua, satu untuk setiap pengiriman
104. Verifikasi Borrow Log aset DU-092-16 tidak memuat entri dari Remind Borrower

### Download idempoten dan tidak dicatat
105. Asset Admin DU-092-26 mengunduh daftar transaksi Borrow dua kali
106. Verifikasi kedua unduhan menghasilkan isi berkas yang sama
107. Verifikasi Transaction admin log Asset Admin DU-092-26 tidak memuat entri dari Download

### Aksi atas baris yang sudah dikembalikan dari tempat lain
108. Asset Admin DU-092-27 menerima kembali aset DU-092-17
109. Verifikasi aset DU-092-17 tidak lagi terbaca di Borrowed Assets sesudah pembacaan ulang dan terbaca di History By Asset
110. Asset Admin DU-092-26 menjalankan Return atas baris lama aset DU-092-17
111. Verifikasi aksi atas baris lama aset DU-092-17 ditolak dengan `This asset has already been returned.`

### Aksi atas baris yang ditutup Missing dari tempat lain
112. Aktor Missing DU-092-37 melaporkan kehilangan aset DU-092-36 dengan Reason `Aset tidak ditemukan saat inventaris {runId}`
113. Verifikasi baris aset DU-092-36 ditutup `Returned` dengan penanda `Missing`, tidak lagi terbaca di Borrowed Assets sesudah pembacaan ulang, dan terbaca di History By Asset
114. Asset Admin DU-092-26 menjalankan Return atas baris lama aset DU-092-36
115. Verifikasi aksi atas baris lama aset DU-092-36 ditolak dengan `This asset has already been returned.`

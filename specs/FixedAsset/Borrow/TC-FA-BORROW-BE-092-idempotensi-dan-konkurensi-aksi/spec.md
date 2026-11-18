---
id: TC-FA-BORROW-BE-092-idempotensi-dan-konkurensi-aksi
title: "Idempotensi, atomisitas, dan hasil pasangan aksi tulis yang mengenai record yang sama"
layer: be-e2e
priority: Medium
caseType: Edge
status: draft
sourceRules: ["EC-BRW-73", "§9.6#r1", "§9.6#r2", "§9.6#r3", "§9.6#r4", "§9.6#r5", "§9.6#r6", "§9.6#r7", "§9.6#r8", "§9.6#r9", "§9.6#r10", "§9.6#r11", "§9.6#r12", "§9.6#r13", "§9.6#r14", "§9.6#r15", "§9.6#r16", "§9.6#r17", "§9.6#r18", "§9.6#r19", "EB-ERR-3", "EB-CON-3", "EB-EDG-1"]
smoke: []
dependsOn: []
owner: BE
trace:
  "EC-BRW-73": [99, 101]
  "§9.6#r1": [2, 3, 8, 9]
  "§9.6#r2": 5
  "§9.6#r3": [11, 12, 13]
  "§9.6#r4": [15, 16, 17]
  "§9.6#r5": [21, 22, 23, 25]
  "§9.6#r6": [28, 29, 30, 32, 33]
  "§9.6#r7": [36, 37, 38]
  "§9.6#r8": [41, 42, 43]
  "§9.6#r9": [45, 46, 47]
  "§9.6#r10": [49, 50, 52]
  "§9.6#r11": [55, 57, 58, 59]
  "§9.6#r12": [61, 63, 65, 66]
  "§9.6#r13": [68, 69]
  "§9.6#r14": [72, 73, 74]
  "§9.6#r15": 78
  "§9.6#r16": [80, 82, 84, 86]
  "§9.6#r17": [88, 89, 91]
  "§9.6#r18": [93, 94]
  "§9.6#r19": [96, 97]
  "EB-ERR-3": [19, 86]
  "EB-CON-3": [8, 32, 65, 72]
  "EB-EDG-1": [57, 76, 86, 91, 101]
---

# Idempotensi, atomisitas, dan hasil pasangan aksi tulis yang mengenai record yang sama

## Prerequisites
- Aktor:
  - Asset Admin DU-092-26, Group penugasan Head Office dan Branch Surabaya (pelaku utama).
  - Asset Admin DU-092-27, Group penugasan Head Office (Aktor Borrow kedua).
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
- Kondisi:
  - Level Borrowing entitas suite adalah Full dan Approval Workflow aktif.
  - Draft berisi aset DU-092-23 dan Draft berisi aset DU-092-24 milik Asset Admin DU-092-26; Draft berisi aset DU-092-21 dan aset DU-092-22 milik Total Control; satu Draft tanpa aset milik Asset Admin DU-092-26.
  - Baris aset DU-092-11, DU-092-14, dan DU-092-16 berstatus `Waiting for Handover` untuk Borrower DU-092-30.
  - Baris aset DU-092-12, DU-092-13, DU-092-15, DU-092-17, DU-092-18, DU-092-19, dan DU-092-20 berstatus `Borrowed` untuk Borrower DU-092-30, masing-masing dalam BRW sendiri dan Due date lebih dari 3 hari lagi.
  - Aset DU-092-19 punya Request Extension dari Borrower DU-092-30 dengan Extend By `2 Day(s)` yang menunggu review; aset DU-092-20 punya Extension yang diajukan Asset Admin DU-092-26 dan menunggu approval.

## Test Steps

### Save Draft: cek versi, tanpa perubahan, dan log
1. Asset Admin DU-092-26 menyimpan Draft berisi aset DU-092-5 untuk Borrower DU-092-30
2. Verifikasi Draft berisi aset DU-092-5 tersimpan dan Transaction admin log Asset Admin DU-092-26 bertambah satu entri untuk Draft itu
3. Verifikasi Last Updated Draft berisi aset DU-092-5 terisi pada penyimpanan pertama
4. Asset Admin DU-092-26 menyimpan lagi Draft berisi aset DU-092-5 tanpa mengubah isinya
5. Verifikasi penyimpanan Draft tanpa perubahan berhasil sebagai no-op, tanpa tulis, dan tidak menambah entri Transaction admin log
6. Asset Admin DU-092-27 menyimpan Draft yang sama dengan menambahkan aset DU-092-6
7. Asset Admin DU-092-26 menyimpan Draft yang sama dari versi lama dengan Purpose `Pemakaian harian {runId}`
8. Verifikasi penyimpanan dari versi lama ditolak dengan `This draft was changed by [Name] at [Time]. Reload to see the latest version; your unsaved changes will be lost.`
9. Verifikasi Draft tidak berubah oleh penyimpanan yang ditolak dan tetap memuat aset DU-092-5 dan aset DU-092-6

### Add to Borrow Draft melewati aset yang sudah ada
10. Asset Admin DU-092-26 menjalankan `Add to Borrow Draft` untuk aset DU-092-5 dan aset DU-092-7 ke Draft Borrower DU-092-30
11. Verifikasi aset DU-092-5 yang sudah ada di Draft dilewati dan hanya aset DU-092-7 yang bertambah
12. Verifikasi penambahan aset ke Draft bersifat atomik per Draft dan tercatat di Transaction admin log
13. Verifikasi aset DU-092-7 tidak terkunci dan tanpa snapshot, dan status Custody aset DU-092-7 tetap `Available`

### Submit idempoten dan atomik
14. Asset Admin DU-092-26 mengirim Submit atas aset DU-092-8 untuk Borrower DU-092-30 dengan Duration `4 Day(s)` dan Purpose `Pemakaian harian {runId}` dua kali dengan kunci idempotensi yang sama
15. Verifikasi hanya satu BRW terbentuk untuk aset DU-092-8 dari dua pengiriman Submit
16. Verifikasi baris, Custody, snapshot, dan pengajuan approval aset DU-092-8 terbentuk bersama dalam satu transaksi
17. Verifikasi Borrow Log aset DU-092-8 memuat satu node `Borrow requested by [Actor]` dan Transaction admin log Asset Admin DU-092-26 memuat satu entri Submit
18. Asset Admin DU-092-27 mengajukan BRW untuk aset DU-092-8 atas nama Borrower DU-092-31 dengan Duration `4 Day(s)` dan Purpose `Pemakaian harian {runId}`
19. Verifikasi pengajuan kedua atas aset DU-092-8 yang sudah dipakai transaksi aktif ditolak guard dan tidak ada BRW baru

### Borrow Now dari dua pemindai bersamaan
20. Borrower DU-092-30 dan Borrower DU-092-31 menjalankan `Borrow Now` self-service atas aset DU-092-9 bersamaan dengan Duration `4 Day(s)` dan Purpose `Pemakaian harian {runId}`
21. Verifikasi tepat satu BRW terbentuk atas aset DU-092-9 dan pemindai lain ditolak tanpa mengubah data
22. Verifikasi BRW yang berhasil memuat baris `Borrowed` dan Custody aset DU-092-9 bernilai `Borrowed` dalam satu transaksi
23. Verifikasi peristiwa tercatat di Borrow Log, Transaction log aset, dan log pengguna Borrower pemenang
24. Borrower DU-092-30 mengirim ulang `Borrow Now` yang sama atas aset DU-092-9 dengan kunci idempotensi yang sama
25. Verifikasi pengiriman ulang tidak membuat BRW kedua atas aset DU-092-9

### Approve dan Reject: keputusan per approver per aset
26. Asset Admin DU-092-26 mengajukan BRW untuk aset DU-092-10 atas nama Borrower DU-092-30 dengan Duration `4 Day(s)` dan Purpose `Pemakaian harian {runId}`
27. Approver DU-092-28 menyetujui aset DU-092-10 dua kali dengan kunci idempotensi yang sama
28. Verifikasi keputusan Approver DU-092-28 atas aset DU-092-10 tercatat sekali
29. Verifikasi keputusan aset, baris, Custody, dan notifikasi atas aset DU-092-10 berubah bersama dalam satu transaksi
30. Verifikasi keputusan tercatat di Borrow Log dan Transaction admin log Approver DU-092-28
31. Approver DU-092-29 menolak aset DU-092-10 sesudah keputusan Approver DU-092-28
32. Verifikasi keputusan Approver DU-092-29 ditolak dengan `You can no longer approve this request because it has already been done by another approver.`
33. Verifikasi aset DU-092-10 tetap memakai keputusan Approver DU-092-28 dan tidak berubah oleh penolakan yang ditolak

### Handover konfirmasi idempoten
34. Asset Admin DU-092-26 menyerahkan aset DU-092-10 kepada Borrower DU-092-30 dengan Condition `Normal`
35. Borrower DU-092-30 mengirim konfirmasi handover aset DU-092-10 dua kali
36. Verifikasi konfirmasi handover aset DU-092-10 menghasilkan satu baris `Borrowed`
37. Verifikasi baris dan Custody aset DU-092-10 berubah bersama dalam satu transaksi
38. Verifikasi handover tercatat satu kali di Borrow Log, Transaction log aset, dan Transaction admin log

### Cancel Request menutup sesi handover tanpa efek ulang
39. Asset Admin DU-092-26 memulai handover aset DU-092-11
40. Asset Admin DU-092-26 menjalankan `Cancel Request` atas sesi handover aset DU-092-11 dua kali
41. Verifikasi sesi handover aset DU-092-11 yang sudah ditutup tidak berefek pada permintaan kedua dan aset DU-092-11 tetap `Waiting for Handover`
42. Verifikasi Borrow Log aset DU-092-11 memuat satu node `Handover not confirmed`
43. Verifikasi sesi Cancel Request atomik per sesi Handover dan Task Borrower Borrower DU-092-30 untuk aset DU-092-11 hilang

### Return idempoten dan Report Damaged ikut Return
44. Asset Admin DU-092-26 menerima kembali aset DU-092-10 dengan Condition `Normal` dua kali dengan kunci idempotensi yang sama
45. Verifikasi Return aset DU-092-10 menghasilkan satu baris `Returned` dan satu node `Returned to [Receiver]`
46. Verifikasi baris dan Custody aset DU-092-10 berubah bersama dalam satu transaksi per BRW
47. Verifikasi Return tercatat di Borrow Log, Transaction log aset, dan Transaction admin log
48. Asset Admin DU-092-26 menerima kembali aset DU-092-18 dengan Report Damaged tanpa Photo dan dengan What happened `Layar retak di pojok kiri bawah {runId}`
49. Verifikasi Return aset DU-092-18 ditolak karena Photo wajib dan tidak ada laporan kerusakan yang dibuat
50. Verifikasi baris aset DU-092-18 tetap `Borrowed` dan BRW tidak berubah
51. Asset Admin DU-092-26 menerima kembali aset DU-092-18 dengan Report Damaged lengkap dengan Photo dan What happened `Layar retak di pojok kiri bawah {runId}`
52. Verifikasi laporan kerusakan aset DU-092-18 tersimpan dalam transaksi BRW yang sama dengan Return

### Extend idempoten dan kegagalan satu BRW tidak membatalkan BRW lain
53. Asset Admin DU-092-26 menerima kembali aset DU-092-13
54. Asset Admin DU-092-27 menjalankan Extend atas aset DU-092-12 dengan Extend duration `2 Day(s)` dua kali dengan kunci idempotensi yang sama
55. Verifikasi Due date aset DU-092-12 bertambah sekali dengan 2 hari
56. Asset Admin DU-092-27 menjalankan Extend gabungan atas aset DU-092-12 dan aset DU-092-13 dengan Extend duration `2 Day(s)` dari tabel Borrowed Assets yang dibuka sebelum aset DU-092-13 dikembalikan
57. Verifikasi Extend aset DU-092-13 ditolak karena baris sudah dikembalikan dan Due date aset DU-092-13 tidak berubah
58. Verifikasi Extend aset DU-092-12 pada BRW lain tetap berlaku dan tidak ada perubahan sebagian di dalam satu BRW
59. Verifikasi Extend tercatat di Borrow Log

### Review Extension Request: keputusan pertama berlaku
60. Asset Admin DU-092-26 mereview Request Extension Borrower DU-092-30 atas aset DU-092-19 dengan Approve Duration `3 Day(s)`
61. Verifikasi Approve Duration yang lebih besar dari Extend By yang diminta ditolak dan pengajuan tetap Extension Request
62. Asset Admin DU-092-26 mereview Request Extension Borrower DU-092-30 atas aset DU-092-19 dengan Approve Duration `1 Day(s)`
63. Verifikasi keputusan Asset Admin DU-092-26 berlaku dan Due date aset DU-092-19 bertambah 1 hari
64. Asset Admin DU-092-27 mereview Request Extension Borrower DU-092-30 atas aset DU-092-19 sesudah keputusan Asset Admin DU-092-26
65. Verifikasi pengiriman berikutnya ditolak dengan `You can no longer approve this request because it has already been done by another Asset Admin.`
66. Verifikasi review Extension atomik per BRW dan tercatat di Borrow Log

### Cancel Extension idempoten
67. Asset Admin DU-092-26 menjalankan Cancel Extension atas Extension aset DU-092-20 dua kali
68. Verifikasi Extension aset DU-092-20 dibatalkan sekali dan Borrow Log memuat satu node `Extension canceled by [Actor]`
69. Verifikasi pembatalan atomik per baris dan Due date aset DU-092-20 tidak berubah

### Cancel Borrow oleh Borrower lebih dulu dari Aktor Borrow
70. Borrower DU-092-30 membatalkan BRW aset DU-092-14 dari halaman pinjamannya
71. Asset Admin DU-092-26 menjalankan Cancel Borrow atas baris aset DU-092-14
72. Verifikasi Cancel Borrow oleh Aktor Borrow ditolak dengan `[Borrower] already canceled this borrow.` dan `Your action was not saved.`
73. Verifikasi baris aset DU-092-14 berstatus `Canceled` dan Custody aset DU-092-14 `Available` dalam satu transaksi
74. Verifikasi pembatalan tercatat satu kali di Borrow Log dan Transaction admin log
75. Asset Admin DU-092-26 menjalankan Cancel Borrow sekali lagi atas baris aset DU-092-14
76. Verifikasi aksi atas baris aset DU-092-14 yang sudah selesai ditolak dan baris tidak berubah

### Mark as Returned ditolak di luar level None
77. Asset Admin DU-092-26 menjalankan Mark as Returned atas aset DU-092-15 yang berstatus Borrowed
78. Verifikasi Mark as Returned atas aset DU-092-15 ditolak server karena level Borrowing bukan None dan baris tetap `Borrowed`

### Delete Draft: cakupan, pembuat, dan idempotensi
79. Asset Admin DU-092-26 menghapus Draft berisi aset DU-092-21 dan aset DU-092-22
80. Verifikasi penghapusan Draft yang memuat Group di luar cakupan ditolak dan Draft tetap ada
81. Asset Admin DU-092-27 menghapus Draft tanpa aset milik Asset Admin DU-092-26
82. Verifikasi penghapusan Draft tanpa aset oleh bukan pembuatnya ditolak dan Draft tetap ada
83. Asset Admin DU-092-26 menghapus Draft berisi aset DU-092-5, aset DU-092-6, dan aset DU-092-7
84. Verifikasi Draft berisi aset DU-092-5 terhapus atomik dan Transaction admin log Asset Admin DU-092-26 memuat satu entri Delete Draft
85. Asset Admin DU-092-27 menghapus Draft yang sama yang sudah dihapus pihak lain
86. Verifikasi penghapusan Draft yang sudah dihapus pihak lain sukses sebagai no-op dan tidak menambah entri log

### Bulk Delete Draft melewati yang di luar cakupan dan idempoten
87. Asset Admin DU-092-26 menjalankan bulk Delete Draft atas Draft berisi aset DU-092-23, Draft berisi aset DU-092-24, dan Draft berisi aset DU-092-21 dan aset DU-092-22
88. Verifikasi Draft berisi aset DU-092-23 dan aset DU-092-24 terhapus sedangkan Draft di luar cakupan dilewati dan tetap ada
89. Verifikasi penghapusan bulk atomik per Draft dan Transaction admin log memuat satu entri untuk setiap Draft yang terhapus
90. Asset Admin DU-092-26 menjalankan bulk Delete Draft yang sama sekali lagi
91. Verifikasi Draft berisi aset DU-092-23 dan aset DU-092-24 yang sudah terhapus tetap terhapus tanpa entri log baru

### Remind Borrower tidak idempoten dan tanpa entri log
92. Asset Admin DU-092-26 menjalankan Remind Borrower atas baris aset DU-092-16 dua kali
93. Verifikasi notifikasi untuk Borrower DU-092-30 bertambah dua, satu untuk setiap pengiriman
94. Verifikasi Borrow Log aset DU-092-16 tidak memuat entri dari Remind Borrower

### Download idempoten dan tidak dicatat
95. Asset Admin DU-092-26 mengunduh daftar transaksi Borrow dua kali
96. Verifikasi kedua unduhan menghasilkan isi berkas yang sama
97. Verifikasi Transaction admin log Asset Admin DU-092-26 tidak memuat entri dari Download

### Aksi atas baris yang sudah dikembalikan dari tempat lain
98. Asset Admin DU-092-27 menerima kembali aset DU-092-17
99. Verifikasi aset DU-092-17 tidak lagi terbaca di Borrowed Assets sesudah pembacaan ulang dan terbaca di History By Asset
100. Asset Admin DU-092-26 menjalankan Return atas baris lama aset DU-092-17
101. Verifikasi aksi atas baris lama aset DU-092-17 ditolak dengan `This asset has already been returned.`

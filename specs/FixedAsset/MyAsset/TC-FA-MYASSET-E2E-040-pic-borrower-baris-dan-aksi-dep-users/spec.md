---
id: TC-FA-MYASSET-E2E-040-pic-borrower-baris-dan-aksi-dep-users
title: "PIC Borrower: baris Borrower tanpa akun, aksi atas nama, dan Confirm Handover dengan pernyataan PIC"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-20", "FI-21", "§1.2#r15", "§1.2#r25", "§1.2#r37", "§1.2#r38", "§1.2#r42", "§1.2#r43", "§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r8", "§2.1#r9", "§2.1#r10", "§2.1#r12", "§2.1#r13", "§4.1b#r12", "§4.1b#r31", "§4.1b#p6", "§4.2.3#p1", "§4.2.5#p4", "§Dialog aksi baris (tab Borrowed dan Assigned)#r7", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§9.2#b7"]
smoke: []
dependsOn: ["Users: Borrower tanpa akun beserta PIC-nya, dan User Detail > User Log", "Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "FI-20": [17, 18]
  "FI-21": [20, 21, 22, 25, 27, 28, 29]
  "§1.2#r15": 4
  "§1.2#r25": 4
  "§1.2#r37": [4, 67]
  "§1.2#r38": [6, 68]
  "§1.2#r42": [33, 34, 35, 38, 41, 44, 47, 50, 53, 71]
  "§1.2#r43": 73
  "§2.1#r1": [2, 5]
  "§2.1#r2": 13
  "§2.1#r3": [71, 77, 78, 80]
  "§2.1#r4": 44
  "§2.1#r5": [33, 47]
  "§2.1#r6": 41
  "§2.1#r7": 34
  "§2.1#r8": 35
  "§2.1#r9": [50, 53]
  "§2.1#r10": 36
  "§2.1#r12": 32
  "§2.1#r13": 37
  "§4.1b#r12": [6, 7, 9]
  "§4.1b#r31": 41
  "§4.1b#p6": [18, 20, 27, 97, 101]
  "§4.2.3#p1": [57, 58, 59, 61, 62, 63]
  "§4.2.5#p4": [73, 83, 85, 88]
  "§Dialog aksi baris (tab Borrowed dan Assigned)#r7": 83
  "§4.8#r1": 2
  "§4.8#r2": 71
  "§4.8#r3": 71
  "§4.8#r4": 13
  "§4.8#r5": 36
  "§4.8#r6": 44
  "§4.8#r7": [33, 47]
  "§4.8#r8": 34
  "§4.8#r9": 35
  "§4.8#r10": 105
  "§4.8#r11": 41
  "§4.8#r12": [50, 53]
  "§4.8#r13": 32
  "§4.8#r14": 37
  "§9.2#b7": [61, 62, 63]
anchor: [11, 104]
coverage:
  web: automated
---

# PIC Borrower: baris Borrower tanpa akun, aksi atas nama, dan Confirm Handover dengan pernyataan PIC

## Prerequisites
- Aktor: PIC Borrower `Taufik Hidayat {runId}` (DU-040-1), pengguna yang menjadi PIC dua Borrower tanpa akun.
- Layar awal: halaman Fixed Asset yang menampilkan navbar.
- Data:
  - DU-040-1: pengguna `Taufik Hidayat {runId}`, role `Read Only`, Group `Head Office`.
  - DU-040-2: Borrower tanpa akun `Hendra Kusuma`, PIC `Taufik Hidayat {runId}`. Nama tampil `Hendra K`, dari Full Name `Hendra Kusuma`. Hover kolom `Borrower` yang diharapkan `Hendra Kusuma · PIC: Taufik Hidayat {runId}`, dari Full Name dan User Name PIC.
  - DU-040-3: Borrower tanpa akun `Maya Putri`, PIC `Taufik Hidayat {runId}`.
  - DU-040-4: pinjaman aset `Laptop Lenovo E14 {runId}`, Group `Head Office`, Status `Borrowed`, Source `Admin`, Borrower `Hendra Kusuma`, Duration `2 days`, Handed Over At `T0`, Due Date `T0 + 2 hari`.
  - DU-040-5: pinjaman aset `Proyektor Epson X06 {runId}`, Group `Head Office`, Status `Borrowed`, Source `Self-service`, Borrower `Hendra Kusuma`, Duration `3 days`, Handed Over At `T0`, Due Date `T0 + 3 hari`.
  - DU-040-6: pinjaman aset `Kamera Canon M50 {runId}`, Group `Head Office`, Status `Waiting for Approval`, Source `Admin`, Borrower `Hendra Kusuma`.
  - DU-040-7: pinjaman aset `Tablet Samsung A9 {runId}`, Group `Head Office`, Status `Extension Request`, Source `Admin`, Borrower `Hendra Kusuma`. Duration `5 days`, Handed Over At `T0`, Due Date `T0 + 5 hari`. Pengajuan Extend diajukan PIC dan menunggu review Aktor Borrow.
  - DU-040-8: pinjaman aset `Mikrofon Shure SM58 {runId}`, Group `Head Office`, Status `Borrowed`, badge `Reported Damaged`, Source `Admin`, Borrower `Hendra Kusuma`, Duration `3 days`, Handed Over At `T0`, Due Date `T0 + 3 hari`. Damage Report diajukan PIC dan berstatus `Waiting for Confirmation`.
  - DU-040-9: pinjaman aset `Tripod Manfrotto 055 {runId}`, Group `Head Office`, Status `Borrowed`, badge `Reported Missing`, Source `Admin`, Borrower `Hendra Kusuma`, Duration `4 days`, Handed Over At `T0`, Due Date `T0 + 4 hari`. Laporan Missing diajukan PIC dan berstatus `Waiting for Confirmation`.
  - DU-040-10: pinjaman aset `Monitor Dell P2422H {runId}`, Group `Head Office`, Status `Borrowed`, Source `Admin`, Borrower `Me`, Duration `6 days`, Handed Over At `T0`, Due Date `T0 + 6 hari`.
  - DU-040-11: pinjaman aset `Router Mikrotik hAP {runId}`, Group `Head Office`, Status `Borrowed`, Source `Admin`, Borrower `Maya Putri`, Duration `7 days`, Handed Over At `T0`, Due Date `T0 + 7 hari`.
  - DU-040-12: pinjaman aset `Scanner Epson V39 {runId}`, Group `Head Office`, Status `Waiting for Handover`, Source `Admin`, Borrower `Hendra Kusuma`. Task `Confirm Handover` bersama DU-040-14 dengan Total Asset `2`.
  - DU-040-14: pinjaman aset `Barcode Reader Zebra DS2208 {runId}`, Group `Head Office`, Status `Waiting for Handover`, Source `Admin`, Borrower `Hendra Kusuma`. Satu sesi Handover dengan DU-040-12, jadi Task `Confirm Handover` memuat dua aset.
  - DU-040-13: pinjaman aset `Printer Canon G3010 {runId}`, Group `Head Office`, Status `Returned`, Source `Admin`, Borrower `Hendra Kusuma`.
  - Label tombol saat seluruh baris yang dapat dipilih sudah terpilih `Unselect All (4 records)`, dari `Unselect All ([N] records)` dengan N `4`.
  - Pernyataan PIC yang diharapkan `I confirm that Hendra Kusuma has received the checked assets.`, dari template PRD dengan Borrower `Hendra Kusuma`.
- Kondisi:
  - Tab Borrowed aktor memuat 10 baris, yaitu DU-040-4 sampai DU-040-12 dan DU-040-14. Tab History memuat 1 baris, yaitu DU-040-13. Tab Task memuat 1 baris, yaitu sesi Handover DU-040-12 dan DU-040-14.
  - Sort aktif tab Borrowed adalah bawaan, Due Date terdekat dulu, sehingga di antara baris yang dapat dipilih baris `Laptop Lenovo E14 {runId}` milik Borrower `Hendra Kusuma` paling awal, sebelum baris `Monitor Dell P2422H {runId}` dan `Router Mikrotik hAP {runId}`.
  - Baris Borrower `Hendra Kusuma` yang dapat dipilih untuk bulk Request Extension ada `4`: DU-040-4, DU-040-5, DU-040-8, dan DU-040-9.
  - Sesi Handover DU-040-12 dan DU-040-14 menunggu konfirmasi dan jendela konfirmasinya belum habis.
  - Halaman Extension Request bulk untuk `Laptop Lenovo E14 {runId}` dan `Proyektor Epson X06 {runId}` terisi bawaan dengan isian valid, sehingga `[Submit Request]` tidak ditolak validasi klien.

## Test Steps

### Menu My Asset dan keempat tab tersedia bagi PIC Borrower
1. Buka `My Asset` dari menu profil pada navbar
2. Verifikasi tab `Task`, `Borrowed`, `Assigned`, dan `History` tampil

### Baris Borrower tanpa akun tampil di tab Borrowed dengan kolom Borrower
3. Klik tab `Borrowed`
4. Verifikasi baris `Laptop Lenovo E14 {runId}` milik Borrower tanpa akun `Hendra Kusuma` tampil
5. Verifikasi baris `Monitor Dell P2422H {runId}` milik aktor sendiri tampil
6. Verifikasi kolom `Borrower` pada baris `Laptop Lenovo E14 {runId}` berisi `Hendra K`
7. Verifikasi kolom `Borrower` pada baris `Monitor Dell P2422H {runId}` berisi `Me`
8. Arahkan kursor ke kolom `Borrower` pada baris `Laptop Lenovo E14 {runId}`
9. Verifikasi hover kolom `Borrower` memuat `Hendra Kusuma · PIC: Taufik Hidayat {runId}`

### Tab Task memuat Task Borrow dan tidak memuat Task Assignment
10. Klik tab `Task`
11. Verifikasi baris Task `Confirm Handover` untuk pinjaman DU-040-12 dan DU-040-14 tampil dengan Total Asset `2`
12. Ketik Search `ASG`, tekan Enter
13. Verifikasi empty state `No results found` tampil karena tidak ada baris Task Assignment
14. Klik `(←)` pada kotak Search

### Seleksi bulk Request Extension hanya memuat satu Borrower
15. Klik tab `Borrowed`
16. Centang baris `Laptop Lenovo E14 {runId}`
17. Verifikasi checkbox baris `Monitor Dell P2422H {runId}` disabled
18. Verifikasi alasan `Select assets from one borrower only.` tersampaikan pada checkbox baris `Monitor Dell P2422H {runId}` yang disabled
19. Klik checkbox header tabel
20. Verifikasi baris `Laptop Lenovo E14 {runId}`, `Proyektor Epson X06 {runId}`, `Mikrofon Shure SM58 {runId}`, dan `Tripod Manfrotto 055 {runId}` tercentang
21. Verifikasi baris `Monitor Dell P2422H {runId}` dan `Router Mikrotik hAP {runId}` tidak tercentang
22. Verifikasi counter seleksi menampilkan jumlah `4`
23. Klik `✕` pada Bulk Action Bar untuk menghapus seleksi
24. Centang baris `Laptop Lenovo E14 {runId}`
25. Verifikasi tombol `Select All (4 records)` tampil
26. Klik `Select All (4 records)`
27. Verifikasi baris `Proyektor Epson X06 {runId}`, `Mikrofon Shure SM58 {runId}`, dan `Tripod Manfrotto 055 {runId}` tercentang
28. Verifikasi baris `Monitor Dell P2422H {runId}` dan `Router Mikrotik hAP {runId}` tidak tercentang
29. Verifikasi tombol `Unselect All (4 records)` tampil[^drift-1]
30. Klik `✕` pada Bulk Action Bar untuk menghapus seleksi

### Aksi baris Borrowed bagi PIC atas nama Borrower tanpa akun
31. Buka menu `⋯` pada baris `Laptop Lenovo E14 {runId}`
32. Verifikasi menu memuat `Borrow Log`
33. Verifikasi menu memuat `Request Extension`
34. Verifikasi menu memuat `Report Damaged`
35. Verifikasi menu memuat `Report Missing`
36. Verifikasi menu tidak memuat `Unassign`
37. Verifikasi menu tidak memuat `Assignment Log`
38. Verifikasi menu tidak memuat `Return` karena pinjaman bersumber `Admin`
39. Tutup menu `⋯` dengan Esc
40. Buka menu `⋯` pada baris `Proyektor Epson X06 {runId}`
41. Verifikasi menu memuat `Return`
42. Tutup menu `⋯` dengan Esc
43. Buka menu `⋯` pada baris `Kamera Canon M50 {runId}`
44. Verifikasi menu memuat `Cancel Borrow`
45. Tutup menu `⋯` dengan Esc
46. Buka menu `⋯` pada baris `Tablet Samsung A9 {runId}`
47. Verifikasi menu memuat `Cancel Extension Request`
48. Tutup menu `⋯` dengan Esc
49. Buka menu `⋯` pada baris `Mikrofon Shure SM58 {runId}`
50. Verifikasi menu memuat `Cancel Damage Report`
51. Tutup menu `⋯` dengan Esc
52. Buka menu `⋯` pada baris `Tripod Manfrotto 055 {runId}`
53. Verifikasi menu memuat `Cancel Missing Report`
54. Tutup menu `⋯` dengan Esc

### Request Extension untuk Borrower tanpa akun hanya menawarkan pinjaman Borrower itu
55. Buka menu `⋯` pada baris `Laptop Lenovo E14 {runId}`
56. Klik `Request Extension`
57. Verifikasi breadcrumb `My Asset > Borrowed > Extension Request` tampil
58. Verifikasi tabel Extension Request memuat aset `Laptop Lenovo E14 {runId}`
59. Verifikasi tabel Extension Request tidak memuat kolom `Extensions` dan `Max Duration`
60. Klik `[+ Asset]`
61. Verifikasi daftar kandidat memuat aset `Proyektor Epson X06 {runId}`
62. Verifikasi daftar kandidat tidak memuat aset `Monitor Dell P2422H {runId}` milik aktor sendiri
63. Verifikasi daftar kandidat tidak memuat aset `Router Mikrotik hAP {runId}` milik Borrower `Maya Putri`
64. Tutup daftar kandidat
65. Klik breadcrumb `Borrowed`

### Riwayat Borrower tanpa akun tampil di tab History dengan kolom Holder
66. Klik tab `History`
67. Verifikasi baris `Printer Canon G3010 {runId}` tampil
68. Verifikasi kolom `Holder` pada baris `Printer Canon G3010 {runId}` berisi `Hendra K`

### Confirm Handover atas nama Borrower tanpa akun memakai pernyataan PIC
69. Klik tab `Task`
70. Buka menu `⋯` pada baris Task `Confirm Handover` untuk pinjaman DU-040-12
71. Verifikasi menu memuat `Confirm Handover`
72. Klik `Confirm Handover`
73. Verifikasi pernyataan `I confirm that Hendra Kusuma has received the checked assets.` tampil pada dialog `Confirm Handover`
74. Centang pernyataan pada dialog `Confirm Handover`
75. Hapus centang aset `Barcode Reader Zebra DS2208 {runId}` pada dialog `Confirm Handover`
76. Klik `[Confirm]`
77. Verifikasi toast `Success, 1 asset has been handed over.` tampil
78. Verifikasi tab Task menampilkan empty state `No tasks`
79. Klik tab `Borrowed`
80. Verifikasi baris `Scanner Epson V39 {runId}` berstatus `Borrowed`
81. Buka menu `⋯` pada baris `Scanner Epson V39 {runId}`
82. Klik `Borrow Log`
83. Verifikasi node konfirmasi pada dialog Borrow Log dicatat `Confirmed by [PIC] on behalf of [Borrower]` dengan PIC `Taufik Hidayat {runId}` dan Borrower `Hendra Kusuma`

### Aset tidak tercentang pada Confirm Handover PIC tetap Waiting for Handover dan tercatat Not received
84. Tutup dialog Borrow Log dengan menekan `Escape`
85. Verifikasi baris `Barcode Reader Zebra DS2208 {runId}` berstatus `Waiting for Handover`
86. Buka menu `⋯` pada baris `Barcode Reader Zebra DS2208 {runId}`
87. Klik `Borrow Log`
88. Verifikasi node `Handover not confirmed` pada dialog Borrow Log tercatat dengan keterangan `Not received`

### Request Extension bulk oleh PIC dicatat atas nama Borrower pada tiap baris
89. Tutup dialog Borrow Log dengan menekan `Escape`
90. Centang baris `Laptop Lenovo E14 {runId}`
91. Centang baris `Proyektor Epson X06 {runId}`
92. Klik `Bulk Action`
93. Klik `Request Extension`
94. Klik `[Submit Request]` dengan isian halaman Extension Request yang terisi bawaan dan valid
95. Buka menu `⋯` pada baris `Laptop Lenovo E14 {runId}`
96. Klik `Borrow Log`
97. Verifikasi node `Extension requested` pada dialog Borrow Log dicatat `[PIC] on behalf of [Borrower]` dengan PIC `Taufik Hidayat {runId}` dan Borrower `Hendra Kusuma`
98. Tutup dialog Borrow Log dengan menekan `Escape`
99. Buka menu `⋯` pada baris `Proyektor Epson X06 {runId}`
100. Klik `Borrow Log`
101. Verifikasi node `Extension requested` pada dialog Borrow Log dicatat `[PIC] on behalf of [Borrower]` dengan PIC `Taufik Hidayat {runId}` dan Borrower `Hendra Kusuma`
102. Tutup dialog Borrow Log dengan menekan `Escape`

### Tombol Borrow an Asset tidak tampil bagi PIC Borrower di web
103. Klik tab `Borrowed`
104. Verifikasi toolbar tab Borrowed memuat `Download`, `Filter`, dan `Search`
105. Verifikasi tombol `Borrow an Asset` tidak tampil di toolbar tab Borrowed (Hidden)

[^drift-1]: Drift PRD/foundation vs kontrak komponen. foundation `prd-conventions.md` §8: tombol berubah (toggle) menjadi `"Unselect All"` saat seluruh data terselect. Kontrak `BulkActionButton#11` dan `BulkActionButton#60`: begitu semua baris yang dapat dipilih terpilih, tombol berbunyi `Unselect All (N records)`, tepat ketika jumlah terpilih sama dengan N. Diasersi: kontrak komponen (SB-7), sehingga label memuat jumlah.

---
id: TC-FA-BORROW-E2E-043-transaction-admin-log-dep-user
title: "Transaction admin log di User Detail memuat tindakan admin atas transaksi Borrow"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§8.2#p1", "§8.2#r1", "§8.2#r2", "§8.2#r3", "§8.2#r4", "§8.2#r5", "§8.2#r6", "§8.2#p2", "§8.2#p3"]
smoke: []
dependsOn: ["User: Detail User > Transaction admin log"]
trace:
  "§8.2#p1": [21, 22, 45, 47, 81, 162, 182, 184, 186, 188, 190]
  "§8.2#r1": [22, 23, 34]
  "§8.2#r2": [45, 47]
  "§8.2#r3": [88, 90, 92, 94]
  "§8.2#r4": [117, 119, 121]
  "§8.2#r5": [60, 62]
  "§8.2#r6": [81, 83]
  "§8.2#p2": [133, 143, 152, 204, 206, 208, 218, 229, 258, 260, 262, 276]
  "§8.2#p3": [18, 24]
anchor: [147, 274]
coverage:
  web: automated
---

# Transaction admin log di User Detail memuat tindakan admin atas transaksi Borrow

## Prerequisites
- Aktor: `Maya Pertiwi {runId}`, Total Control (Aktor Borrow) pada seluruh Group; ia bukan Borrower maupun PIC pada BRW kecuali DU-043-28. Aktor lain yang hanya memicu perubahan state: Approver `Budi Santoso {runId}` pada Group `Head Office`, Asset Admin `Agus Pratama {runId}` (pengaju DU-043-18), dan Asset Admin `Dewi Lestari {runId}` (DU-043-30) yang juga Borrower DU-043-31.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-043-1: karyawan `Hendra Kusuma {runId}`, Status `Active`, Eligibility `Can borrow`, Borrower pada semua BRW dan Draft kecuali DU-043-28 dan DU-043-31.
  - DU-043-2: aset `Laptop Dell Latitude {runId}`, Group `Head Office`, Custody `Available`, Approval `Auto-approve`.
  - DU-043-3: Draft Borrower `Hendra Kusuma {runId}` yang dibuat berisi aset DU-043-2, lalu diubah Note menjadi `Peminjaman untuk presentasi klien`, lalu dihapus.
  - DU-043-4: Draft milik Borrower `Hendra Kusuma {runId}`, Group `Head Office`, berisi aset DU-043-5 dan DU-043-6 dengan Duration `2 days` dan Purpose `Rapat evaluasi bulanan` pada keduanya.
  - DU-043-5: aset `Monitor LG UltraWide {runId}`, Group `Head Office`, Custody `Available`, Approval `Auto-approve`.
  - DU-043-6: aset `Keyboard Logitech MX Keys {runId}`, Group `Head Office`, Custody `Available`, Approval `Auto-approve`.
  - DU-043-7: BRW hasil Submit DU-043-4 dengan Transaction ID miliknya sendiri, status `Waiting for Handover`.
  - DU-043-8: BRW `Waiting for Handover` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, berisi aset DU-043-9.
  - DU-043-9: aset `Mouse Logitech MX Master {runId}`, Group `Head Office`, Approval `Auto-approve`.
  - DU-043-10: BRW `Waiting for Handover` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, berisi aset DU-043-11.
  - DU-043-11: aset `Webcam Logitech C920 {runId}`, Group `Head Office`, Approval `Auto-approve`.
  - DU-043-12: BRW `Borrowed` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, berisi baris DU-043-13, DU-043-14, DU-043-15, dan DU-043-16.
  - DU-043-13: aset `Projector Epson EB-X06 {runId}`, baris `Borrowed`, Due date T0 + 1 hari, Approval Extend `Auto-approve`.
  - DU-043-14: aset `Tablet Lenovo Tab P11 {runId}`, baris `Borrowed`, Due date T0 + 1 hari, Approval Extend `Needs approval`.
  - DU-043-15: aset `Speaker Bose S1 Pro {runId}`, baris `Borrowed`, Due date T0 + 1 hari, Approval Extend `Needs approval`.
  - DU-043-16: aset `Printer HP LaserJet Pro {runId}`, baris `Borrowed`, Due date T0 + 1 hari, Approval Extend `Needs approval`.
  - DU-043-17: isian Extend untuk keempat baris DU-043-12: Extend By `2`, Reason `Proyek belum selesai`.
  - DU-043-18: BRW `Waiting for Approval` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, berisi baris DU-043-19 dan DU-043-20; Approver `Budi Santoso {runId}` eligible untuk keduanya.
  - DU-043-19: aset `Scanner Canon DR-C225 {runId}`, Approval `Needs approval`.
  - DU-043-20: aset `Shredder Fellowes 99Ci {runId}`, Approval `Needs approval`.
  - DU-043-21: BRW `Waiting for Handover` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Photo at start OFF, berisi aset DU-043-22.
  - DU-043-22: aset `Drone DJI Mini 4 {runId}`, TAG `QR`, Group `Head Office`.
  - DU-043-23: BRW `Borrowed` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Photo at end OFF, berisi aset DU-043-24.
  - DU-043-24: aset `Handheld Zebra TC21 {runId}`, TAG `QR`, Group `Head Office`.
  - DU-043-25: BRW `Borrowed` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, berisi aset DU-043-26.
  - DU-043-26: aset `Genset Honda EU22i {runId}`, Group `Head Office`.
  - DU-043-27: isian Report Missing: Reason `Genset tidak kembali dari lokasi acara`.
  - DU-043-28: BRW `Borrowed` Group `Head Office`, Borrower `Maya Pertiwi {runId}`, Photo at end OFF, berisi aset DU-043-29.
  - DU-043-29: aset `Kamera Sony A7C {runId}`, TAG `QR`, Group `Head Office`.
  - DU-043-30: karyawan `Dewi Lestari {runId}`, Asset Admin pada Group `Head Office`, Status `Active`.
  - DU-043-31: BRW `Borrowed` Group `Head Office`, Borrower `Dewi Lestari {runId}`, berisi aset DU-043-32.
  - DU-043-32: aset `Mixer Yamaha MG10 {runId}`, Self service `ON`, Due date T0 + 1 hari.
  - DU-043-33: aset `Amplifier Denon PMA-600 {runId}`, Group `Head Office`, Custody `Available`, Approval `Auto-approve`; dipakai Dewi menyimpan Draft sebagai Aktor Borrow.
  - DU-043-34: isian Extend Dewi atas pinjamannya sendiri: Extend By `1`, Reason `Acara belum selesai`.
  - DU-043-35: karyawan `Budi Santoso {runId}`, Approver pada Group `Head Office`, Status `Active`.
  - DU-043-36: BRW `Borrowed` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, berisi aset DU-043-37.
  - DU-043-37: aset `Kamera Fujifilm X-T5 {runId}`, Group `Head Office`.
  - DU-043-38: isian Report Damaged: Photo `layar-pecah.jpg`, What happened `Layar kamera pecah terkena benturan`.
  - DU-043-39: karyawan `Rina Wulandari {runId}`, Status `Active`, Eligibility `Can borrow`, tanpa Draft.
  - DU-043-40: aset `Pemanas Air Modena {runId}`, Group `Head Office`, Custody `Available`, Approval `Auto-approve`.
  - DU-043-41: aset `Dispenser Cosmos {runId}`, Group `Head Office`, Custody `Available`, Approval `Auto-approve`.
  - DU-043-42: BRW `Waiting for Handover` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Photo at start OFF, berisi dua aset ber-TAG `QR`: `Kompor Portable Rinnai {runId}` dan `Blender Philips {runId}`.
  - DU-043-43: BRW `Borrowed` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Photo at end OFF, berisi dua aset ber-TAG `QR`: `Setrika Philips {runId}` dan `Mixer Sharp {runId}`.
  - DU-043-44: BRW `Extension Request` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Due date T0 + 1 hari, berisi tiga pengajuan Extend yang menunggu review dengan Extend By `2 days` dan Reason `Proyek belum selesai`: aset `Genset Kipor {runId}` (Approval Extend `Auto-approve`), aset `Pompa Air Shimizu {runId}` (Approval Extend `Needs approval`), dan aset `Kipas Angin Cosmos {runId}`.
  - DU-043-45: isian Review Extension Request: Approve Duration `2` dan Approval Note `Kebutuhan proyek belum mendesak` untuk penolakan.
  - DU-043-46: BRW `Waiting for Handover` Group `Head Office`, Borrower `Maya Pertiwi {runId}`, Photo at start OFF, aset `Teropong Bushnell {runId}`, TAG `QR`.
  - DU-043-47: karyawan tanpa akun login `Joko Susilo {runId}`, Status `Active`, PIC `Maya Pertiwi {runId}`.
  - DU-043-48: BRW `Waiting for Handover` Group `Head Office`, Borrower `Joko Susilo {runId}`, PIC `Maya Pertiwi {runId}`, Photo at start OFF, aset `Walkie Talkie Baofeng {runId}`, TAG `QR`.
  - DU-043-49: BRW `Borrowed` Group `Head Office`, Borrower `Joko Susilo {runId}`, PIC `Maya Pertiwi {runId}`, Photo at end OFF, aset `Proyektor Mini Xiaomi {runId}`, TAG `QR`.
  - DU-043-50: BRW `Waiting for Handover` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Photo at start OFF, aset `Tablet Samsung Tab A9 {runId}`, TAG `QR`.
  - DU-043-51: isian Report TAG: Report Type `Unreadable`.
  - DU-043-52: BRW `Borrowed` Group `Head Office`, Borrower `Maya Pertiwi {runId}`, aset `Gitar Yamaha F310 {runId}`.

## Test Steps

### Draft dibuat, diubah, dan Save Draft tanpa perubahan tidak menambah baris
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Klik `[+ Borrow]`
4. Klik `[Select Borrower]`
5. Pilih Borrower `Hendra Kusuma {runId}` pada dialog Select Borrower
6. Klik `[Select]`
7. Klik `[+ Asset]`
8. Pilih aset `Laptop Dell Latitude {runId}` pada dialog Select Asset
9. Klik `[Select]`
10. Klik `[Save Draft]`
11. Klik tab `Drafts` pada halaman Borrow
12. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
13. Klik menu ⋯ pada Draft berisi aset `Laptop Dell Latitude {runId}`
14. Klik `Edit`
15. Isi Note dengan `Peminjaman untuk presentasi klien`
16. Klik `[Save Draft]`
17. Klik `[Save Draft]` lagi pada Draft yang sama tanpa mengubah isi Draft
18. Verifikasi toast `No changes to save.` tampil
19. Buka User Detail `Maya Pertiwi {runId}` pada tab `Transaction admin log`
20. Ketik Search `Laptop Dell Latitude {runId}`, tekan Enter
21. Verifikasi tabel memuat kolom `Date`, `Activity`, `Transaction ID`, `Name`, `Borrower`, dan `Group`, tanpa kolom `Description`
22. Verifikasi tabel memuat baris Activity `Draft created` dengan Transaction ID `—`, Name `Laptop Dell Latitude {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office`
23. Verifikasi tabel memuat baris Activity `Draft edited` dengan Transaction ID `—`, Name `Laptop Dell Latitude {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office`
24. Verifikasi hasil Search memuat tepat dua baris, yaitu `Draft created` dan `Draft edited`, tanpa baris untuk Save Draft yang tidak mengubah isi

### Draft dihapus tercatat sebagai baris Draft
25. Klik `Transactions` pada sidebar
26. Klik `Borrow`
27. Klik tab `Drafts` pada halaman Borrow
28. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
29. Klik menu ⋯ pada Draft berisi aset `Laptop Dell Latitude {runId}`
30. Klik `Delete`
31. Klik `[Delete]` pada dialog Delete Draft
32. Buka User Detail `Maya Pertiwi {runId}` pada tab `Transaction admin log`
33. Ketik Search `Laptop Dell Latitude {runId}`, tekan Enter
34. Verifikasi tabel memuat baris Activity `Draft deleted` dengan Transaction ID `—`, Name `Laptop Dell Latitude {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office`

### Submit Draft tercatat satu baris per aset dengan Transaction ID BRW-nya
35. Klik `Transactions` pada sidebar
36. Klik `Borrow`
37. Klik tab `Drafts` pada halaman Borrow
38. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
39. Klik menu ⋯ pada Draft milik DU-043-4
40. Klik `Edit`
41. Klik `[Submit]`
42. Klik `[Submit]` pada dialog `Submit Borrow`
43. Buka User Detail `Maya Pertiwi {runId}` pada tab `Transaction admin log`
44. Ketik Search `Monitor LG UltraWide {runId}`, tekan Enter
45. Verifikasi tabel memuat baris Activity `Requested` dengan Transaction ID BRW milik DU-043-7, Name `Monitor LG UltraWide {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office`
46. Ketik Search `Keyboard Logitech MX Keys {runId}`, tekan Enter
47. Verifikasi tabel memuat baris Activity `Requested` dengan Transaction ID BRW milik DU-043-7, Name `Keyboard Logitech MX Keys {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office` sebagai baris terpisah dari aset pertama

### Cancel Borrow, termasuk Save as Draft to edit, tercatat atas nama pelaku
48. Klik `Transactions` pada sidebar
49. Klik `Borrow`
50. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
51. Klik menu ⋯ pada baris BRW milik DU-043-8
52. Klik `Cancel Borrow`
53. Klik `[Cancel Borrow]` pada dialog `Cancel Borrow`
54. Klik menu ⋯ pada baris BRW milik DU-043-10
55. Klik `Cancel Borrow`
56. Centang `Save as Draft to edit` pada dialog `Cancel Borrow`
57. Klik `[Cancel Borrow]` pada dialog `Cancel Borrow`
58. Buka User Detail `Maya Pertiwi {runId}` pada tab `Transaction admin log`
59. Ketik Search `Mouse Logitech MX Master {runId}`, tekan Enter
60. Verifikasi tabel memuat baris Activity `Canceled` dengan Transaction ID BRW milik DU-043-8, Name `Mouse Logitech MX Master {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office`
61. Ketik Search `Webcam Logitech C920 {runId}`, tekan Enter
62. Verifikasi tabel memuat baris Activity `Canceled` dengan Transaction ID BRW milik DU-043-10, Name `Webcam Logitech C920 {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office` untuk Cancel dengan Save as Draft to edit

### Extend dan Cancel Extension yang diajukan Aktor atas nama Borrower
63. Klik `Transactions` pada sidebar
64. Klik `Borrow`
65. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
66. Klik menu ⋯ pada baris BRW milik DU-043-12
67. Klik `Request Extension`
68. Isi Extend By baris `Projector Epson EB-X06 {runId}` dengan `2`
69. Isi Reason baris `Projector Epson EB-X06 {runId}` dengan `Proyek belum selesai`
70. Isi Extend By baris `Tablet Lenovo Tab P11 {runId}` dengan `2`
71. Isi Reason baris `Tablet Lenovo Tab P11 {runId}` dengan `Proyek belum selesai`
72. Isi Extend By baris `Speaker Bose S1 Pro {runId}` dengan `2`
73. Isi Reason baris `Speaker Bose S1 Pro {runId}` dengan `Proyek belum selesai`
74. Isi Extend By baris `Printer HP LaserJet Pro {runId}` dengan `2`
75. Isi Reason baris `Printer HP LaserJet Pro {runId}` dengan `Proyek belum selesai`
76. Klik `[Submit Extension]`
77. Klik `Cancel Extension` pada baris aset `Tablet Lenovo Tab P11 {runId}` di Borrow Detail BRW milik DU-043-12
78. Klik `[Cancel Extension]` pada dialog `Cancel Extension`
79. Buka User Detail `Maya Pertiwi {runId}` pada tab `Transaction admin log`
80. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
81. Verifikasi tabel memuat baris Activity `Extension requested` dengan Transaction ID BRW milik DU-043-12, Name `Projector Epson EB-X06 {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office`
82. Ketik Search `Tablet Lenovo Tab P11 {runId}`, tekan Enter
83. Verifikasi tabel memuat baris Activity `Extension canceled` dengan Transaction ID BRW milik DU-043-12, Name `Tablet Lenovo Tab P11 {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office`

### Approve dan Reject oleh Approver untuk Borrow dan Extension tercatat di log Approver
84. Approver `Budi Santoso {runId}` menyetujui aset `Scanner Canon DR-C225 {runId}` dan menolak aset `Shredder Fellowes 99Ci {runId}` pada pengajuan BRW milik DU-043-18
85. Approver `Budi Santoso {runId}` menyetujui Extension aset `Speaker Bose S1 Pro {runId}` dan menolak Extension aset `Printer HP LaserJet Pro {runId}` pada BRW milik DU-043-12
86. Buka User Detail `Budi Santoso {runId}` pada tab `Transaction admin log`
87. Ketik Search `Scanner Canon DR-C225 {runId}`, tekan Enter
88. Verifikasi tabel memuat baris Activity `Approved` dengan Transaction ID BRW milik DU-043-18, Name `Scanner Canon DR-C225 {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office`
89. Ketik Search `Shredder Fellowes 99Ci {runId}`, tekan Enter
90. Verifikasi tabel memuat baris Activity `Rejected` dengan Transaction ID BRW milik DU-043-18, Name `Shredder Fellowes 99Ci {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office`
91. Ketik Search `Speaker Bose S1 Pro {runId}`, tekan Enter
92. Verifikasi tabel memuat baris Activity `Extended` dengan Transaction ID BRW milik DU-043-12, Name `Speaker Bose S1 Pro {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office`
93. Ketik Search `Printer HP LaserJet Pro {runId}`, tekan Enter
94. Verifikasi tabel memuat baris Activity `Extension rejected` dengan Transaction ID BRW milik DU-043-12, Name `Printer HP LaserJet Pro {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office`

### Hand Over dan Return sebagai penerima tercatat per aset; Report Missing oleh Aktor Borrow tercatat di sub-tab Missing
95. Klik `Transactions` pada sidebar
96. Klik `Borrow`
97. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
98. Klik menu ⋯ pada baris BRW milik DU-043-21
99. Klik `Hand Over`
100. Scan TAG aset DU-043-22 lewat `[Verify Asset]`
101. Klik `[Request Confirmation]`
102. Klik `[Confirm on This Device]`
103. Centang checkbox pernyataan pada dialog `Confirm Receipt`
104. Klik `[Confirm]`
105. Klik `[Done]`
106. Klik menu ⋯ pada baris BRW milik DU-043-23
107. Klik `Return`
108. Scan TAG aset DU-043-24 lewat `[Verify Asset]`
109. Klik `[Submit]`
110. Buka Borrow Detail BRW milik DU-043-25 dari tabel Transactions
111. Klik menu ⋯ pada baris aset DU-043-26
112. Klik `Report Missing`
113. Isi Reason dengan `Genset tidak kembali dari lokasi acara`
114. Kirim laporan pada dialog `Report Missing`
115. Buka User Detail `Maya Pertiwi {runId}` pada tab `Transaction admin log`
116. Ketik Search `Drone DJI Mini 4 {runId}`, tekan Enter
117. Verifikasi tabel memuat baris Activity `Handed over` dengan Transaction ID BRW milik DU-043-21, Name `Drone DJI Mini 4 {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office`
118. Ketik Search `Handheld Zebra TC21 {runId}`, tekan Enter
119. Verifikasi tabel memuat baris Activity `Returned` dengan Transaction ID BRW milik DU-043-23, Name `Handheld Zebra TC21 {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office`
120. Ketik Search `Genset Honda EU22i {runId}`, tekan Enter
121. Verifikasi tidak ada baris Activity `Reported missing` untuk aset `Genset Honda EU22i {runId}` di sub-tab `Borrow`; klik sub-tab `Missing`, ketik Search `Genset Honda EU22i {runId}`, tekan Enter, lalu verifikasi baris Activity `Reported missing` dengan Name `Genset Honda EU22i {runId} - 1`, Source `Borrow`, dan Group `Head Office` tampil

### Report Damaged oleh Aktor Borrow dari halaman Borrow tercatat di sub-tab Damaged, tidak di sub-tab Borrow
122. Klik `Transactions` pada sidebar
123. Klik `Borrow`
124. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
125. Buka Borrow Detail BRW milik DU-043-36 dari tabel Transactions
126. Klik menu ⋯ pada baris aset DU-043-37
127. Klik `Report Damaged`
128. Unggah foto `layar-pecah.jpg` pada dialog `Report Damaged`
129. Isi What happened dengan `Layar kamera pecah terkena benturan`
130. Kirim laporan pada dialog `Report Damaged`
131. Buka User Detail `Maya Pertiwi {runId}` pada tab `Transaction admin log`
132. Ketik Search `Kamera Fujifilm X-T5 {runId}`, tekan Enter
133. Verifikasi tidak ada baris untuk aset `Kamera Fujifilm X-T5 {runId}` di sub-tab `Borrow`; klik sub-tab `Damaged`, ketik Search `Kamera Fujifilm X-T5 {runId}`, tekan Enter, lalu verifikasi baris Activity `Reported damaged` dengan Name `Kamera Fujifilm X-T5 {runId} - 1`, Source `Borrowed asset`, dan Group `Head Office` tampil

### Return yang diproses sendiri oleh Aktor yang juga Borrower ditandai Self-processed
134. Klik `Transactions` pada sidebar
135. Klik `Borrow`
136. Ketik Search `Maya Pertiwi {runId}`, tekan Enter
137. Klik menu ⋯ pada baris BRW milik DU-043-28
138. Klik `Return`
139. Scan TAG aset DU-043-29 lewat `[Verify Asset]`
140. Klik `[Submit]`
141. Buka User Detail `Maya Pertiwi {runId}` pada tab `Transaction admin log`
142. Ketik Search `Kamera Sony A7C {runId}`, tekan Enter
143. Verifikasi tabel memuat baris Activity `Returned` dan penanda `Self-processed` dengan Transaction ID BRW milik DU-043-28, Name `Kamera Sony A7C {runId} - 1`, Borrower `Maya Pertiwi {runId}`, dan Group `Head Office`

### Tindakan Borrower atas pinjamannya sendiri tidak menambah baris di log admin
144. Asset Admin `Dewi Lestari {runId}` menyimpan Draft berisi aset `Amplifier Denon PMA-600 {runId}` untuk Borrower `Hendra Kusuma {runId}` sebagai Aktor Borrow
145. Buka User Detail `Dewi Lestari {runId}` pada tab `Transaction admin log`
146. Ketik Search `{runId}`, tekan Enter
147. Verifikasi tabel memuat baris Activity `Draft created` dengan Transaction ID `—`, Name `Amplifier Denon PMA-600 {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office`
148. Catat jumlah baris hasil Search sebagai jumlah awal
149. Borrower `Dewi Lestari {runId}` mengajukan Extend atas pinjaman milik DU-043-31 dengan Extend By `1` dan Reason `Acara belum selesai`
150. Buka User Detail `Dewi Lestari {runId}` pada tab `Transaction admin log`
151. Ketik Search `{runId}`, tekan Enter
152. Verifikasi jumlah baris hasil Search sama dengan jumlah awal karena tindakan Borrower atas pinjamannya sendiri tidak masuk Transaction admin log

### Add to Borrow Draft bulk tercatat satu baris per aset di Draft
153. Buka daftar aset lewat sidebar `Assets` > `All`
154. Ketik Search `{runId}`, tekan Enter
155. Centang baris `Pemanas Air Modena {runId}`
156. Centang baris `Dispenser Cosmos {runId}`
157. Klik aksi bulk `Add to Borrow Draft`
158. Pilih Borrower `Rina Wulandari {runId}` pada dialog Select Borrower
159. Klik `[Select]`
160. Buka User Detail `Maya Pertiwi {runId}` pada tab `Transaction admin log`
161. Ketik Search `{runId}`, tekan Enter
162. Verifikasi tabel memuat dua baris Activity `Added to draft` yang terpisah, masing-masing dengan Transaction ID `—`, Borrower `Rina Wulandari {runId}`, dan Group `Head Office`: satu dengan Name `Pemanas Air Modena {runId} - 1` dan satu dengan Name `Dispenser Cosmos {runId} - 1`, karena satu aset menjadi satu baris

### Hand Over dan Return dengan beberapa aset tercatat satu baris per aset
163. Klik `Transactions` pada sidebar
164. Klik `Borrow`
165. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
166. Klik menu ⋯ pada baris BRW milik DU-043-42
167. Klik `Hand Over`
168. Scan TAG aset `Kompor Portable Rinnai {runId}` lewat `[Verify Asset]`
169. Scan TAG aset `Blender Philips {runId}` lewat `[Verify Asset]`
170. Klik `[Request Confirmation]`
171. Klik `[Confirm on This Device]`
172. Centang checkbox pernyataan pada dialog `Confirm Receipt`
173. Klik `[Confirm]`
174. Klik `[Done]`
175. Klik menu ⋯ pada baris BRW milik DU-043-43
176. Klik `Return`
177. Scan TAG aset `Setrika Philips {runId}` lewat `[Verify Asset]`
178. Scan TAG aset `Mixer Sharp {runId}` lewat `[Verify Asset]`
179. Klik `[Submit]`
180. Buka User Detail `Maya Pertiwi {runId}` pada tab `Transaction admin log`
181. Ketik Search `Kompor Portable Rinnai {runId}`, tekan Enter
182. Verifikasi tabel memuat baris Activity `Handed over` dengan Transaction ID BRW milik DU-043-42, Name `Kompor Portable Rinnai {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office` saja
183. Ketik Search `Blender Philips {runId}`, tekan Enter
184. Verifikasi tabel memuat baris Activity `Handed over` dengan Transaction ID BRW milik DU-043-42, Name `Blender Philips {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office` terpisah, saja
185. Ketik Search `Setrika Philips {runId}`, tekan Enter
186. Verifikasi tabel memuat baris Activity `Returned` dengan Transaction ID BRW milik DU-043-43, Name `Setrika Philips {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office` saja
187. Ketik Search `Mixer Sharp {runId}`, tekan Enter
188. Verifikasi tabel memuat baris Activity `Returned` dengan Transaction ID BRW milik DU-043-43, Name `Mixer Sharp {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office` terpisah, saja

### Tabel tidak memuat kolom Description dan Activity hanya berisi nama node
189. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
190. Verifikasi tabel tidak memuat kolom `Description` dan Activity baris `Extension requested` untuk aset `Projector Epson EB-X06 {runId}` hanya berisi nama node tanpa nama pelaku maupun detail durasi

### Review Extension Request oleh Aktor Borrow tercatat satu baris per aset
191. Klik `Transactions` pada sidebar
192. Klik `Borrow`
193. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
194. Klik menu ⋯ pada baris BRW milik DU-043-44
195. Klik `Review`
196. Isi Approve Duration baris `Genset Kipor {runId}` dengan `2`
197. Isi Approve Duration baris `Pompa Air Shimizu {runId}` dengan `2`
198. Ubah toggle Approval baris `Kipas Angin Cosmos {runId}` menjadi `Reject`
199. Isi Approval Note baris `Kipas Angin Cosmos {runId}` dengan `Kebutuhan proyek belum mendesak`
200. Klik `[Submit]`
201. Klik `[Submit]` pada dialog `Submit Approval`
202. Buka User Detail `Maya Pertiwi {runId}` pada tab `Transaction admin log`
203. Ketik Search `Genset Kipor {runId}`, tekan Enter
204. Verifikasi tabel memuat baris Activity `Extended` dengan Transaction ID BRW milik DU-043-44, Name `Genset Kipor {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office` untuk aset yang Approval Rule-nya Auto-approve
205. Ketik Search `Pompa Air Shimizu {runId}`, tekan Enter
206. Verifikasi tabel memuat baris Activity `Extension forwarded` dengan Transaction ID BRW milik DU-043-44, Name `Pompa Air Shimizu {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office` untuk aset yang Approval Rule-nya Needs approval
207. Ketik Search `Kipas Angin Cosmos {runId}`, tekan Enter
208. Verifikasi tabel memuat baris Activity `Extension rejected` dengan Transaction ID BRW milik DU-043-44, Name `Kipas Angin Cosmos {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office`

### Cancel Damage Report atas laporannya sendiri dari halaman Borrow tercatat di sub-tab Damaged, tidak di sub-tab Borrow
209. Klik `Transactions` pada sidebar
210. Klik `Borrow`
211. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
212. Buka Borrow Detail BRW milik DU-043-36 dari tabel Transactions
213. Klik menu ⋯ pada baris aset DU-043-37
214. Klik `Cancel Damage Report`
215. Konfirmasi pembatalan laporan pada dialog yang tampil
216. Buka User Detail `Maya Pertiwi {runId}` pada tab `Transaction admin log`
217. Ketik Search `Kamera Fujifilm X-T5 {runId}`, tekan Enter
218. Verifikasi tidak ada baris untuk aset `Kamera Fujifilm X-T5 {runId}` di sub-tab `Borrow`; klik sub-tab `Damaged`, ketik Search `Kamera Fujifilm X-T5 {runId}`, tekan Enter, lalu verifikasi baris Activity `Report canceled` dengan Name `Kamera Fujifilm X-T5 {runId} - 1`, Source `Borrowed asset`, dan Group `Head Office` tampil

### TAG reported dari Hand Over tercatat di log admin
219. Klik `Transactions` pada sidebar
220. Klik `Borrow`
221. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
222. Klik menu ⋯ pada baris BRW milik DU-043-50
223. Klik `Hand Over`
224. Klik menu ⋯ pada baris aset `Tablet Samsung Tab A9 {runId}` di halaman Hand Over
225. Klik `I Can't Scan the TAG`
226. Kirim laporan pada dialog Report TAG dengan Report Type `Unreadable`
227. Buka User Detail `Maya Pertiwi {runId}` pada tab `Transaction admin log`
228. Ketik Search `Tablet Samsung Tab A9 {runId}`, tekan Enter
229. Verifikasi tabel memuat baris Activity `TAG reported` dengan Transaction ID BRW milik DU-043-50, Name `Tablet Samsung Tab A9 {runId} - 1`, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office`

### Hand Over dan Return yang diproses sendiri oleh Aktor sebagai Borrower atau PIC ditandai Self-processed
230. Klik `Transactions` pada sidebar
231. Klik `Borrow`
232. Ketik Search `Maya Pertiwi {runId}`, tekan Enter
233. Klik menu ⋯ pada baris BRW milik DU-043-46
234. Klik `Hand Over`
235. Scan TAG aset `Teropong Bushnell {runId}` lewat `[Verify Asset]`
236. Klik `[Request Confirmation]`
237. Klik `[Confirm on This Device]`
238. Centang checkbox pernyataan pada dialog `Confirm Receipt`
239. Klik `[Confirm]`
240. Klik `[Done]`
241. Klik `Transactions` pada sidebar
242. Klik `Borrow`
243. Ketik Search `Joko Susilo {runId}`, tekan Enter
244. Klik menu ⋯ pada baris BRW milik DU-043-48
245. Klik `Hand Over`
246. Scan TAG aset `Walkie Talkie Baofeng {runId}` lewat `[Verify Asset]`
247. Klik `[Request Confirmation]`
248. Klik `[Confirm on This Device]`
249. Centang checkbox pernyataan pada dialog `Confirm Receipt`
250. Klik `[Confirm]`
251. Klik `[Done]`
252. Klik menu ⋯ pada baris BRW milik DU-043-49
253. Klik `Return`
254. Scan TAG aset `Proyektor Mini Xiaomi {runId}` lewat `[Verify Asset]`
255. Klik `[Submit]`
256. Buka User Detail `Maya Pertiwi {runId}` pada tab `Transaction admin log`
257. Ketik Search `Teropong Bushnell {runId}`, tekan Enter
258. Verifikasi tabel memuat baris Activity `Handed over` dan penanda `Self-processed` karena Aktor juga Borrower dengan Transaction ID BRW milik DU-043-46, Name `Teropong Bushnell {runId} - 1`, Borrower `Maya Pertiwi {runId}`, dan Group `Head Office`
259. Ketik Search `Walkie Talkie Baofeng {runId}`, tekan Enter
260. Verifikasi tabel memuat baris Activity `Handed over` dan penanda `Self-processed` karena Aktor menjadi PIC Borrower dengan Transaction ID BRW milik DU-043-48, Name `Walkie Talkie Baofeng {runId} - 1`, Borrower `Joko Susilo {runId}`, dan Group `Head Office`
261. Ketik Search `Proyektor Mini Xiaomi {runId}`, tekan Enter
262. Verifikasi tabel memuat baris Activity `Returned` dan penanda `Self-processed` karena Aktor menjadi PIC Borrower dengan Transaction ID BRW milik DU-043-49, Name `Proyektor Mini Xiaomi {runId} - 1`, Borrower `Joko Susilo {runId}`, dan Group `Head Office`

### Report dari My Asset oleh Aktor dalam peran Borrower tidak masuk log admin
263. Masuk sebagai `Maya Pertiwi {runId}`
264. Klik menu Profile pada navbar
265. Klik `My Asset`
266. Klik tab `Borrowed`
267. Klik menu ⋯ pada baris aset `Gitar Yamaha F310 {runId}`
268. Klik `Report Damaged`
269. Unggah foto `layar-pecah.jpg` pada dialog `Report Damaged`
270. Isi What happened dengan `Layar kamera pecah terkena benturan`
271. Kirim laporan pada dialog `Report Damaged`
272. Buka User Detail `Maya Pertiwi {runId}` pada tab `Transaction admin log`
273. Ketik Search `{runId}`, tekan Enter
274. Klik sub-tab `Damaged`, ketik Search `Kamera Fujifilm X-T5 {runId}`, tekan Enter, lalu verifikasi tabel memuat baris tindakan admin untuk aset `Kamera Fujifilm X-T5 {runId}` pada Transaction admin log `Maya Pertiwi {runId}`
275. Ketik Search `Gitar Yamaha F310 {runId}`, tekan Enter
276. Verifikasi tidak ada baris untuk aset `Gitar Yamaha F310 {runId}` di sub-tab `Damaged` Transaction admin log `Maya Pertiwi {runId}` karena laporan dari My Asset, juga oleh Aktor yang adalah Pelapor admin, hanya masuk User log

---
id: TC-FA-BORROW-E2E-038-borrower-aksi-dep-my-asset
title: "Borrower dan PIC bertindak dari My Asset: Confirm Handover, Cancel Borrow, Extend, Report, dan Return self-service diterima Aktor Borrow"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["DM-BRW-03", "F-BORROW-15", "FI-BRW-123", "FI-BRW-124", "FI-BRW-125", "FI-BRW-190", "FI-BRW-191", "FI-BRW-192", "FI-BRW-193", "FI-BRW-194", "FI-BRW-195", "FI-BRW-196", "FI-BRW-197", "FI-BRW-71", "FI-BRW-72", "FI-BRW-73", "FI-BRW-74", "FI-BRW-79", "FI-BRW-80", "FI-BRW-81", "§2.2#r3", "§4.1h#r1", "§4.1h#r2", "§4.1h#r3", "§4.1h#r4", "§4.1h#r5", "§4.2.7a#b1", "§4.2.7a#b2", "§4.2.7a#b3", "§4.2.7a#b4", "§4.2.7a#p1", "§4.2.7a#p2"]
smoke: []
dependsOn: ["My Asset: tab Borrowed dan Task Confirm Handover"]
trace:
  "DM-BRW-03": [29, 32]
  "F-BORROW-15": [5, 71]
  "FI-BRW-123": [126, 146]
  "FI-BRW-124": 132
  "FI-BRW-125": 143
  "FI-BRW-190": 94
  "FI-BRW-191": 106
  "FI-BRW-192": 96
  "FI-BRW-193": 97
  "FI-BRW-194": 95
  "FI-BRW-195": 98
  "FI-BRW-196": [100, 108, 114]
  "FI-BRW-197": [101, 115]
  "FI-BRW-71": 9
  "FI-BRW-72": 12
  "FI-BRW-73": [13, 18]
  "FI-BRW-74": 19
  "FI-BRW-79": 40
  "FI-BRW-80": 45
  "FI-BRW-81": 48
  "§2.2#r3": 64
  "§4.1h#r1": [5, 14]
  "§4.1h#r2": [69, 70]
  "§4.1h#r3": [73, 74, 75]
  "§4.1h#r4": [38, 40, 54, 56, 58]
  "§4.1h#r5": [5, 78, 80, 119, 126]
  "§4.2.7a#b1": 168
  "§4.2.7a#b2": [170, 172, 175, 178, 181, 183]
  "§4.2.7a#b3": [186, 188]
  "§4.2.7a#b4": [192, 194]
  "§4.2.7a#p1": [154, 158, 164]
  "§4.2.7a#p2": [165, 166, 167, 169]
anchor: [63, 142, 163]
coverage:
  web: automated
---

# Borrower dan PIC bertindak dari My Asset: Confirm Handover, Cancel Borrow, Extend, Report, dan Return self-service diterima Aktor Borrow

## Prerequisites
- Aktor: Borrower `Hendra Kusuma {runId}` (DU-038-1) bertindak dari My Asset. Aktor kedua: Asset Admin (Aktor Borrow) `Agus Pratama {runId}` pada Group `Head Office`, bukan Borrower maupun PIC pada BRW di spec ini. Aktor ketiga: PIC `Rudi Hartono {runId}` (DU-038-2) yang menjadi PIC karyawan tanpa akun `Joko Susilo {runId}` (DU-038-3). Aktor keempat: Group Manager (Aktor Borrow) `Siti Rahma {runId}` (DU-038-4) pada Group `Head Office`, hanya memicu review lebih dulu.
- Layar awal: halaman utama aplikasi.
- Data:
  - DU-038-1: karyawan `Hendra Kusuma {runId}` dengan akun login, Status `Active`, Eligibility `Can borrow`.
  - DU-038-2: karyawan `Rudi Hartono {runId}` dengan akun login, Asset Admin pada Group `Head Office`, Status `Active`.
  - DU-038-3: karyawan tanpa akun login `Joko Susilo {runId}`, Status `Active`, PIC `Rudi Hartono {runId}` (aktif).
  - DU-038-4: karyawan `Siti Rahma {runId}`, Group Manager pada Group `Head Office`, Status `Active`.
  - DU-038-5: BRW `Waiting for Handover` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, Photo at start OFF, berisi baris DU-038-6, DU-038-7, DU-038-8, dan DU-038-9; sesi konfirmasi Handover aktif untuk keempat aset yang sudah dipindai Agus.
  - DU-038-6: aset `Laptop Dell XPS {runId}`, baris `Waiting for Handover`, Duration `3 days`.
  - DU-038-7: aset `Proyektor Epson EB-W06 {runId}`, baris `Waiting for Handover`, Duration `3 days`.
  - DU-038-8: aset `Kamera Canon EOS R6 {runId}`, baris `Waiting for Handover`, Duration `3 days`.
  - DU-038-9: aset `Tablet Lenovo Tab P11 {runId}`, baris `Waiting for Handover`, Duration `3 days`.
  - DU-038-10: BRW `Waiting for Handover` Group `Head Office`, Borrower `Joko Susilo {runId}`, PIC `Rudi Hartono {runId}`, Requested By `Agus Pratama {runId}`, berisi baris DU-038-11 dan DU-038-12; sesi konfirmasi Handover aktif untuk kedua aset yang sudah dipindai Agus.
  - DU-038-11: aset `Monitor LG UltraWide {runId}`, baris `Waiting for Handover`, Duration `2 days`.
  - DU-038-12: aset `Keyboard Logitech MX Keys {runId}`, baris `Waiting for Handover`, Duration `2 days`.
  - DU-038-13: BRW `Returned` Group `Head Office`, Borrower `Joko Susilo {runId}`, PIC `Rudi Hartono {runId}`, aset `Printer HP LaserJet Pro {runId}`.
  - DU-038-14: BRW `Waiting for Approval` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, aset `Drone DJI Mini 4 {runId}`.
  - DU-038-15: BRW `Waiting for Handover` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, aset `Speaker Bose S1 Pro {runId}`, tanpa sesi konfirmasi.
  - DU-038-16: BRW `Borrowed` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, aset `Handycam Sony FDR {runId}`, Due date T0 + 3 hari.
  - DU-038-17: BRW `Overdue` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, aset `Genset Honda EU22i {runId}`, Due date T0 - 1 hari.
  - DU-038-18: BRW `Returned` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, aset `Mixer Yamaha MG10 {runId}`.
  - DU-038-19: BRW `Rejected` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, aset `Scanner Canon DR-C225 {runId}`, reason `Anggaran proyek belum disetujui`.
  - DU-038-20: BRW `Canceled` oleh sistem Group `Head Office`, Borrower `Hendra Kusuma {runId}`, aset `Amplifier Denon PMA-600 {runId}`, reason `Timed out (Waiting for Approval)`.
  - DU-038-21: BRW `Borrowed` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Due date T0 + 2 hari, berisi baris DU-038-22, DU-038-23, DU-038-24, dan DU-038-25.
  - DU-038-22: aset `Kursi Ergonomis Ergotrend {runId}`, Self service `ON` pada snapshot baris, Due date T0 + 2 hari.
  - DU-038-23: aset `Meja Lipat Informa {runId}`, Self service `OFF` pada snapshot baris, Due date T0 + 2 hari.
  - DU-038-24: aset `Lampu Studio Godox {runId}`, Self service `ON` pada snapshot baris, Due date T0 + 2 hari.
  - DU-038-25: aset `Tripod Manfrotto {runId}`, Self service `OFF` pada snapshot baris, Due date T0 + 2 hari.
  - DU-038-26: isian Extend dari sisi Borrower: Extend By `1`, Reason `Acara belum selesai`.
  - DU-038-27: BRW pinjaman self-service `Borrowed` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Source `Self-service`, Photo at start ON dan Photo at end ON, berisi aset DU-038-28 dan DU-038-29.
  - DU-038-28: aset `Mikrofon Shure SM58 {runId}`, TAG `QR`, foto handover `foto-handover-mikrofon.jpg`, dikembalikan Borrower sendiri.
  - DU-038-29: aset `Tas Kamera Lowepro {runId}`, TAG `QR`, foto handover `foto-handover-tas.jpg`, dititipkan ke Aktor Borrow Group asal.
  - DU-038-30: BRW `Extension Request` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Due date T0 + 2 hari, berisi pengajuan Extend yang menunggu review untuk baris DU-038-31 dan DU-038-32.
  - DU-038-31: aset `Televisi Samsung 43 {runId}`, Extend By `2 days`, Reason `Proyek belum selesai`, Max Duration `7 days`, Extensions `0 / 2`.
  - DU-038-32: aset `Soundbar JBL Bar 5.1 {runId}`, Extend By `2 days`, Reason `Proyek belum selesai`, Max Duration `7 days`, Extensions `0 / 2`.
  - DU-038-33: BRW `Extension Request` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, aset `Radio Handy Motorola {runId}`, Extend By `2 days`, Reason `Proyek belum selesai`.
  - DU-038-34: isian Review Extension Request: Approve Duration `3` (melebihi Extend By), Approve Duration `0`, Approve Duration yang ditolak diketik `-1` dan `1.5`, Approval Note `Kebutuhan proyek belum mendesak`, caption yang diharapkan `Max. 2 days`.

## Test Steps

### Task Confirm Handover Borrower: konfirmasi per aset menetapkan Due date hanya untuk aset tercentang
1. Masuk sebagai `Hendra Kusuma {runId}`
2. Klik menu Profile pada navbar
3. Klik `My Asset`
4. Klik tab `Task`
5. Verifikasi Task `Confirm Handover` tampil untuk BRW milik DU-038-5 karena Agus Pratama sedang menyerahkan aset dan menunggu konfirmasi Borrower
6. Klik `Confirm Handover` pada Task BRW milik DU-038-5
7. Hapus centang aset `Kamera Canon EOS R6 {runId}` pada dialog `Confirm Handover`
8. Hapus centang aset `Tablet Lenovo Tab P11 {runId}` pada dialog `Confirm Handover`
9. Verifikasi aset `Kamera Canon EOS R6 {runId}` dan aset `Tablet Lenovo Tab P11 {runId}` tidak tercentang sedangkan aset `Laptop Dell XPS {runId}` dan aset `Proyektor Epson EB-W06 {runId}` tetap tercentang
10. Konfirmasi aset tercentang pada dialog `Confirm Handover`
11. Buka Borrow Detail BRW milik DU-038-5 pada layar Aktor Borrow `Agus Pratama {runId}`
12. Verifikasi baris aset `Laptop Dell XPS {runId}` dan baris aset `Proyektor Epson EB-W06 {runId}` berstatus `Borrowed` dengan Due date terisi, sedangkan baris aset `Kamera Canon EOS R6 {runId}` dan baris aset `Tablet Lenovo Tab P11 {runId}` memiliki Due date `—`
13. Verifikasi baris aset `Kamera Canon EOS R6 {runId}` tetap `Waiting for Handover` dengan keterangan `Not received`
14. Verifikasi Task `Confirm Handover` untuk BRW milik DU-038-5 tidak ada lagi di tab `Task` Borrower sesudah konfirmasi

### Aset Not received dapat diserahkan lagi di sesi berikutnya
15. Aktor Borrow `Agus Pratama {runId}` memilih `Hand Over` pada baris BRW milik DU-038-5
16. Pindai TAG aset `Kamera Canon EOS R6 {runId}` lewat `[Verify Asset]`
17. Klik `[Request Confirmation]`
18. Verifikasi popup `Waiting for Confirmation` memuat aset `Kamera Canon EOS R6 {runId}` dengan status `Waiting` sehingga aset itu dapat diserahkan lagi di sesi berikutnya
19. Verifikasi aset `Kamera Canon EOS R6 {runId}` pada popup tidak lagi membawa keterangan `Not received`
20. Klik `[Cancel Request]`

### Borrower membatalkan aset Not received lewat Cancel Borrow dari My Asset
21. Masuk sebagai `Hendra Kusuma {runId}`
22. Klik menu Profile pada navbar
23. Klik `My Asset`
24. Klik tab `Borrowed`
25. Klik menu ⋯ pada baris aset `Tablet Lenovo Tab P11 {runId}`
26. Klik `Cancel Borrow`
27. Konfirmasi pembatalan pada dialog Cancel Borrow varian Borrower
28. Buka Borrow Detail BRW milik DU-038-5 pada layar Aktor Borrow `Agus Pratama {runId}`
29. Verifikasi baris aset `Tablet Lenovo Tab P11 {runId}` berstatus `Canceled` dan baris aset lain pada BRW milik DU-038-5 tidak berubah
30. Klik menu ⋯ pada baris aset `Tablet Lenovo Tab P11 {runId}`
31. Klik `Borrow Log`
32. Verifikasi Borrow Log memuat node `Canceled by [Actor]` dengan [Actor] berisi `Hendra Kusuma {runId}`
33. Tutup dialog Borrow Log

### PIC mengonfirmasi handover atas nama Borrower tanpa akun dari Task My Asset
34. Masuk sebagai `Rudi Hartono {runId}`
35. Klik menu Profile pada navbar
36. Klik `My Asset`
37. Klik tab `Task`
38. Verifikasi Task `Confirm Handover` untuk BRW milik DU-038-10 tampil tanpa penanda atas nama
39. Klik `Confirm Handover` pada Task BRW milik DU-038-10
40. Verifikasi dialog `Confirm Handover` menampilkan nama Borrower `Joko Susilo {runId}`, checklist aset, dan pernyataan wajib `I confirm that [Borrower] has received the checked assets.`
41. Hapus centang aset `Keyboard Logitech MX Keys {runId}` pada dialog `Confirm Handover`
42. Centang pernyataan `I confirm that [Borrower] has received the checked assets.`
43. Konfirmasi aset tercentang pada dialog `Confirm Handover`
44. Buka Borrow Detail BRW milik DU-038-10 pada layar Aktor Borrow `Agus Pratama {runId}`
45. Verifikasi baris aset `Keyboard Logitech MX Keys {runId}` tetap `Waiting for Handover` dengan keterangan `Not received`
46. Klik menu ⋯ pada baris aset `Monitor LG UltraWide {runId}`
47. Klik `Borrow Log`
48. Verifikasi detail Confirmation pada node Handed over memuat `Confirmed by [PIC] on behalf of [Borrower]` dengan [PIC] berisi `Rudi Hartono {runId}` dan [Borrower] berisi `Joko Susilo {runId}`
49. Tutup dialog Borrow Log

### My Asset hanya menampilkan baris Borrower terkait dan baris atas nama untuk PIC
50. Masuk sebagai `Rudi Hartono {runId}`
51. Klik menu Profile pada navbar
52. Klik `My Asset`
53. Klik tab `Borrowed`
54. Verifikasi baris aset `Monitor LG UltraWide {runId}` tampil di tab `Borrowed` dengan kolom `Borrower` berisi `Joko Susilo {runId}`
55. Klik menu ⋯ pada baris aset `Monitor LG UltraWide {runId}`
56. Verifikasi menu aksi baris atas nama memuat `Request Extension`
57. Klik tab `History`
58. Verifikasi baris aset `Printer HP LaserJet Pro {runId}` tampil di tab `History` dengan kolom `Holder` berisi `Joko Susilo {runId}`
59. Masuk sebagai `Hendra Kusuma {runId}`
60. Klik menu Profile pada navbar
61. Klik `My Asset`
62. Klik tab `History`
63. Verifikasi baris riwayat milik Borrower `Hendra Kusuma {runId}` tampil di tab `History`
64. Verifikasi baris aset `Printer HP LaserJet Pro {runId}` milik Borrower tanpa akun `Joko Susilo {runId}` tidak ada di My Asset `Hendra Kusuma {runId}` karena Hendra bukan PIC-nya

### My Asset memuat baris pinjaman aktif dengan Status dan Due date per baris
65. Masuk sebagai `Hendra Kusuma {runId}`
66. Klik menu Profile pada navbar
67. Klik `My Asset`
68. Klik tab `Borrowed`
69. Verifikasi baris aset `Drone DJI Mini 4 {runId}` berstatus `Waiting for Approval`, baris aset `Speaker Bose S1 Pro {runId}` berstatus `Waiting for Handover`, dan baris aset `Handycam Sony FDR {runId}` berstatus `Borrowed` dengan Due date T0 + 3 hari
70. Verifikasi baris aset `Genset Honda EU22i {runId}` berstatus `Overdue` dengan Due date T0 - 1 hari
71. Verifikasi tab `Borrowed` memuat baris pinjaman aktif milik Borrower beserta aksi Borrower pada baris itu

### My Asset memuat baris riwayat Returned, Rejected, dan Canceled beserta reason
72. Klik tab `History`
73. Verifikasi baris aset `Mixer Yamaha MG10 {runId}` berstatus `Returned`
74. Verifikasi baris aset `Scanner Canon DR-C225 {runId}` berstatus `Rejected` dengan reason `Anggaran proyek belum disetujui`
75. Verifikasi baris aset `Amplifier Denon PMA-600 {runId}` berstatus `Canceled` dengan reason `Timed out (Waiting for Approval)`

### Aksi Borrower pada baris sebelum dan sesudah handover
76. Klik tab `Borrowed`
77. Klik menu ⋯ pada baris aset `Speaker Bose S1 Pro {runId}`
78. Verifikasi menu aksi baris `Waiting for Handover` memuat `Cancel Borrow`
79. Klik menu ⋯ pada baris aset `Handycam Sony FDR {runId}`
80. Verifikasi menu aksi baris `Borrowed` memuat `Request Extension`

### Extend dari My Asset: hasil campuran langsung berlaku dan menunggu review
81. Masuk sebagai `Hendra Kusuma {runId}`
82. Klik menu Profile pada navbar
83. Klik `My Asset`
84. Klik tab `Borrowed`
85. Klik menu ⋯ pada baris aset `Kursi Ergonomis Ergotrend {runId}`
86. Klik `Request Extension`
87. Klik `[+ Asset]`
88. Pilih aset `Meja Lipat Informa {runId}` pada dialog Select Asset
89. Klik `[Select]`
90. Isi Extend By baris `Kursi Ergonomis Ergotrend {runId}` dengan `1`
91. Isi Reason baris `Kursi Ergonomis Ergotrend {runId}` dengan `Acara belum selesai`
92. Isi Extend By baris `Meja Lipat Informa {runId}` dengan `1`
93. Isi Reason baris `Meja Lipat Informa {runId}` dengan `Acara belum selesai`
94. Verifikasi breadcrumb `My Asset > Borrowed > Extension Request` dan footer `[Cancel]` dan `[Submit Request]` tampil
95. Verifikasi kolom Approval menampilkan `—` untuk baris `Kursi Ergonomis Ergotrend {runId}` dan `Review` untuk baris `Meja Lipat Informa {runId}`
96. Verifikasi baris `Kursi Ergonomis Ergotrend {runId}` yang Self service-nya ON pada snapshot baris langsung berlaku tanpa review
97. Verifikasi baris `Meja Lipat Informa {runId}` menjadi pengajuan yang menunggu review, bukan Extend yang berlaku atau pengajuan approval
98. Verifikasi catatan `1 asset will be reviewed before the new due date applies.` tampil di bawah tabel
99. Klik `[Submit Request]`
100. Verifikasi halaman kembali ke My Asset dengan toast `Success, due date has been changed for [Changed] of [Total] assets. [Submitted] sent for review.` dengan [Changed] berisi `1`, [Total] berisi `2`, dan [Submitted] berisi `1`
101. Verifikasi baris aset `Meja Lipat Informa {runId}` yang pengajuannya menunggu review tidak menampilkan `Request Extension`

### Extend dari My Asset: semua baris langsung berlaku memakai footer Submit Extension
102. Klik menu ⋯ pada baris aset `Lampu Studio Godox {runId}`
103. Klik `Request Extension`
104. Isi Extend By baris `Lampu Studio Godox {runId}` dengan `1`
105. Isi Reason baris `Lampu Studio Godox {runId}` dengan `Acara belum selesai`
106. Verifikasi footer `[Cancel]` dan `[Submit Extension]` tampil untuk pengajuan yang baris aktifnya langsung berlaku
107. Klik `[Submit Extension]`
108. Verifikasi halaman kembali ke My Asset dengan toast `Success, due date has been changed to [Date].` dengan [Date] berisi Due date baru T0 + 3 hari

### Extend dari My Asset: semua baris menunggu review
109. Klik menu ⋯ pada baris aset `Tripod Manfrotto {runId}`
110. Klik `Request Extension`
111. Isi Extend By baris `Tripod Manfrotto {runId}` dengan `1`
112. Isi Reason baris `Tripod Manfrotto {runId}` dengan `Acara belum selesai`
113. Klik `[Submit Request]`
114. Verifikasi halaman kembali ke My Asset dengan toast sukses pengajuan Extend yang menunggu review karena baris yang diajukan menunggu review
115. Verifikasi baris aset `Tripod Manfrotto {runId}` yang pengajuannya menunggu review tidak menampilkan `Request Extension`

### Borrower menarik pengajuan Extend yang menunggu review
116. Klik menu ⋯ pada baris aset `Tripod Manfrotto {runId}`
117. Klik `Cancel Extension Request`
118. Klik `[Cancel Extension]` pada dialog `Cancel Extension`
119. Verifikasi toast `Success, extension request has been canceled.` tampil dan baris aset `Tripod Manfrotto {runId}` kembali menampilkan `Request Extension`

### Return self-service oleh Borrower sendiri mengirim Review ke Aktor Borrow Group asal
120. Masuk sebagai `Hendra Kusuma {runId}`
121. Klik menu Profile pada navbar
122. Klik `My Asset`
123. Klik tab `Borrowed`
124. Klik menu ⋯ pada baris aset `Mikrofon Shure SM58 {runId}`
125. Klik `Return`
126. Verifikasi halaman Return menampilkan field Borrower terkunci pada `Hendra Kusuma {runId}` dan `[+ Asset]` hanya menawarkan aset self-service milik Borrower
127. Pindai TAG aset `Mikrofon Shure SM58 {runId}` lewat `[Verify Asset]`
128. Ambil foto return aset `Mikrofon Shure SM58 {runId}` dengan kamera perangkat
129. Klik `[Submit]`
130. Masuk sebagai `Agus Pratama {runId}`
131. Buka daftar notifikasi pada navbar
132. Verifikasi notifikasi Review diterima Aktor Borrow Group asal `Agus Pratama {runId}` dan memuat foto handover `foto-handover-mikrofon.jpg` dan foto return berdampingan

### Return self-service yang dititipkan ke Aktor Borrow tidak mengirim Review
133. Klik `Transactions` pada sidebar
134. Klik `Borrow`
135. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
136. Klik menu ⋯ pada baris BRW milik DU-038-27
137. Klik `Return`
138. Pindai TAG aset `Tas Kamera Lowepro {runId}` lewat `[Verify Asset]`
139. Ambil foto return aset `Tas Kamera Lowepro {runId}` dengan kamera perangkat
140. Klik `[Submit]`
141. Buka daftar notifikasi pada navbar
142. Verifikasi notifikasi Review untuk aset `Mikrofon Shure SM58 {runId}` tetap tampil di daftar notifikasi `Agus Pratama {runId}`
143. Verifikasi tidak ada notifikasi Review untuk aset `Tas Kamera Lowepro {runId}` karena Return diterima lewat Aktor Borrow
144. Klik menu ⋯ pada baris aset `Tas Kamera Lowepro {runId}` di Borrow Detail BRW milik DU-038-27
145. Klik `Borrow Log`
146. Verifikasi node `Returned to [Receiver]` memuat [Receiver] berisi `Agus Pratama {runId}` sebagai penerima Return yang dititipkan Borrower
147. Tutup dialog Borrow Log

### Titik masuk Review Extension Request hanya untuk BRW dengan pengajuan Extend dari My Asset
148. Masuk sebagai `Agus Pratama {runId}`
149. Klik `Transactions` pada sidebar
150. Klik `Borrow`
151. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
152. Klik menu ⋯ pada baris BRW milik DU-038-30
153. Klik `Review`
154. Verifikasi halaman Review Extension Request terbuka dengan breadcrumb `Transactions > Borrow > Transactions > Review` dari row action `Review` pada tabel Transactions
155. Klik `[Cancel]`
156. Buka Borrow Detail BRW milik DU-038-30 dari tabel Transactions
157. Klik `[Review]`
158. Verifikasi halaman Review Extension Request terbuka dari tombol `[Review]` di Borrow Detail untuk BRW dengan status header `Extension Request`
159. Klik `[Cancel]`
160. Klik `Transactions` pada sidebar
161. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
162. Klik menu ⋯ pada baris BRW milik DU-038-27
163. Verifikasi menu aksi baris BRW milik DU-038-27 memuat `Detail`
164. Verifikasi menu aksi baris BRW milik DU-038-27 tidak memuat `Review` karena tidak ada pengajuan Extend dari My Asset yang menunggu

### Isi halaman Review Extension Request
165. Verifikasi judul `Review Extension Request`, Transaction ID BRW milik DU-038-30, Borrower `Hendra Kusuma {runId}`, dan Group `Head Office` tampil sebagai info halaman
166. Verifikasi tabel memuat kolom `Name`, `Asset ID`, `Current Due Date`, `Extensions`, `Max Duration`, `Extend By`, `New Due Date`, `Approval Rule`, `Reason`, `Approval`, `Approve Duration`, dan `Approval Note`
167. Verifikasi toolbar memuat Search dengan placeholder `Search asset name or ID...` dan Filter `Current Due Date`, serta footer `[Cancel]` dan `[Submit]`
168. Verifikasi tabel tidak memiliki kolom `Group` karena Group `Head Office` sudah ada di info header
169. Verifikasi baris aset `Televisi Samsung 43 {runId}` menampilkan Extend By `2 days` dan Reason `Proyek belum selesai` sebagai nilai read-only dari Borrower

### Approval, Approve Duration, dan Approval Note per aset
170. Verifikasi toggle Approval baris `Televisi Samsung 43 {runId}` berlabel `Approve` secara default dan Approve Duration terisi `2` sama dengan Extend By yang diminta
171. Isi Approve Duration baris `Televisi Samsung 43 {runId}` dengan `3`
172. Verifikasi caption `Max. 2 days` tampil di bawah input Approve Duration dan baris `Televisi Samsung 43 {runId}` tidak dapat di-Submit sampai diperbaiki
173. Ketik `-1` pada Approve Duration baris `Televisi Samsung 43 {runId}`
174. Ketik `1.5` pada Approve Duration baris `Televisi Samsung 43 {runId}`
175. Verifikasi input Approve Duration baris `Televisi Samsung 43 {runId}` tidak menerima tanda minus maupun angka desimal
176. Isi Approve Duration baris `Televisi Samsung 43 {runId}` dengan `0`
177. Klik `[Submit]`
178. Verifikasi pesan `Approval note must not be empty` tampil pada baris `Televisi Samsung 43 {runId}` karena Approve Duration `0` dihitung Reject
179. Isi Approve Duration baris `Televisi Samsung 43 {runId}` dengan `2`
180. Ubah toggle Approval baris `Soundbar JBL Bar 5.1 {runId}` menjadi `Reject`
181. Verifikasi input Approve Duration baris `Soundbar JBL Bar 5.1 {runId}` tidak dapat diisi karena Approval berstatus `Reject`
182. Klik `[Submit]`
183. Verifikasi pesan `Approval note must not be empty` tampil pada baris `Soundbar JBL Bar 5.1 {runId}` karena Approval Note wajib untuk keputusan Reject
184. Isi Approval Note baris `Soundbar JBL Bar 5.1 {runId}` dengan `Kebutuhan proyek belum mendesak`

### Submit review memproses keputusan dan kembali ke Borrow Detail
185. Klik `[Submit]`
186. Verifikasi dialog `Submit Approval` untuk Review Extension Request tampil dengan teks `You will submit this transaction approval. Asset with 0 approved duration will be rejected and will not appear in the next step of transaction. Are you sure you want to submit it?`
187. Klik `[Submit]` pada dialog `Submit Approval`
188. Verifikasi halaman kembali ke Borrow Detail BRW milik DU-038-30 dengan toast `Success, extension request has been reviewed.`

### Aktor Borrow lain yang mereview lebih dulu membuka dialog Approval cannot be made
189. Buka halaman Review Extension Request BRW milik DU-038-33 lewat row action `Review`
190. Ubah toggle Approval baris `Radio Handy Motorola {runId}` menjadi `Reject` tanpa mengirimnya
191. Aktor Borrow `Siti Rahma {runId}` mengirim review pengajuan BRW milik DU-038-33 lebih dulu
192. Verifikasi dialog `Approval cannot be made` langsung terbuka dengan teks `You can no longer approve this request because it has already been done by another Asset Admin.` tanpa menunggu `[Submit]`
193. Klik `[OK]`
194. Verifikasi keputusan `Reject` yang belum dikirim `Agus Pratama {runId}` tidak tersimpan: hasil review BRW milik DU-038-33 mengikuti keputusan yang dikirim `Siti Rahma {runId}`

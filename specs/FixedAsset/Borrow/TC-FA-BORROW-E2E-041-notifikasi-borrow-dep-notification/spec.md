---
id: TC-FA-BORROW-E2E-041-notifikasi-borrow-dep-notification
title: "Peristiwa Borrow memicu notifikasi ke penerima menurut katalog event"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["F-BORROW-16", "§9.2#b22", "§9.2#b23", "§9.8#p1", "§9.8#r1", "§9.8#r2", "§9.8#r3", "§9.8#r4", "§9.8#r5", "§9.8#r6", "§9.8#r7", "§9.8#r8", "§9.8#r9", "§9.8#r10", "§9.8#r11", "§9.8#r12", "§9.8#r13", "§9.8#r14", "§9.8#r15", "§9.8#r16", "§9.8#p2", "§9.8#p3"]
smoke: []
dependsOn: ["Notification: katalog event Borrow"]
trace:
  "F-BORROW-16": [11, 150]
  "§9.2#b22": 36
  "§9.2#b23": [86, 88, 90]
  "§9.8#p1": [89, 90, 150]
  "§9.8#r1": [11, 21]
  "§9.8#r2": 25
  "§9.8#r3": [34, 35]
  "§9.8#r4": [41, 42, 46, 50]
  "§9.8#r5": [54, 57, 58, 61]
  "§9.8#r6": [65, 66]
  "§9.8#r7": 70
  "§9.8#r8": 74
  "§9.8#r9": 78
  "§9.8#r10": 94
  "§9.8#r11": 98
  "§9.8#r12": [102, 105, 109]
  "§9.8#r13": 113
  "§9.8#r14": [117, 120]
  "§9.8#r15": [127, 130]
  "§9.8#r16": [142, 145, 149]
  "§9.8#p2": [134, 138]
  "§9.8#p3": [14, 17, 28, 97, 123, 133]
anchor: [45, 49]
coverage:
  web: automated
---

# Peristiwa Borrow memicu notifikasi ke penerima menurut katalog event

## Prerequisites
- Aktor: Aktor Borrow `Agus Pratama {runId}` (Asset Admin pada Group `Head Office`) yang melakukan aksi di halaman Borrow dan menerima notifikasi Aktor Borrow; ia bukan Borrower maupun PIC pada BRW di spec ini. Penerima yang diamati bergantian: Approver `Budi Santoso {runId}` (DU-041-4), Borrower `Hendra Kusuma {runId}` (DU-041-1), PIC `Rudi Hartono {runId}` (DU-041-3), pengaju `Lina Sari {runId}` (DU-041-5), dan penerima laporan `Siti Rahma {runId}` (DU-041-6). Borrower tanpa akun login `Joko Susilo {runId}` (DU-041-2) menerima email Borrower.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-041-1: karyawan `Hendra Kusuma {runId}` dengan akun login, Email `hendra.kusuma{runId}@example.com`, Status `Active`.
  - DU-041-2: karyawan tanpa akun login `Joko Susilo {runId}`, Email `joko.susilo{runId}@example.com`, PIC `Rudi Hartono {runId}` (aktif), Status `Active`.
  - DU-041-3: karyawan `Rudi Hartono {runId}`, Email `rudi.hartono{runId}@example.com`, Asset Admin pada Group `Head Office`, Status `Active`.
  - DU-041-4: karyawan `Budi Santoso {runId}`, Approver pada Group `Head Office`, Status `Active`.
  - DU-041-5: karyawan `Lina Sari {runId}`, Asset Admin pada Group `Head Office`, Status `Active`.
  - DU-041-6: karyawan `Siti Rahma {runId}`, Group Manager pada Group `Head Office`, Status `Active`.
  - DU-041-7: Draft Borrower `Hendra Kusuma {runId}` berisi aset `Laptop Dell XPS {runId}`, Approval `Needs approval`, Duration `2 days`, Purpose `Rapat evaluasi bulanan`.
  - DU-041-8: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Proyektor Epson EB-W06 {runId}`, Approval Extend `Needs approval`, Due date T0 + 1 hari.
  - DU-041-9: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Meja Lipat Informa {runId}`, Self service `OFF` pada snapshot baris, Due date T0 + 2 hari.
  - DU-041-10: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, aset `Monitor LG UltraWide {runId}`; Approver `Budi Santoso {runId}` eligible.
  - DU-041-11: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, aset `Keyboard Logitech MX Keys {runId}`; Approver `Budi Santoso {runId}` eligible.
  - DU-041-12: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, aset `Mouse Logitech MX Master {runId}`; Approver `Budi Santoso {runId}` eligible.
  - DU-041-13: Draft Borrower `Hendra Kusuma {runId}` berisi aset `Webcam Logitech C920 {runId}`, Approval `Auto-approve`, Duration `1 days`, Purpose `Rekaman rapat`.
  - DU-041-14: BRW `Borrowed` Borrower `Hendra Kusuma {runId}` dengan tiga pengajuan Extension yang menunggu approval `Budi Santoso {runId}` untuk aset `Tablet Lenovo Tab P11 {runId}`, `Speaker Bose S1 Pro {runId}`, dan `Printer HP LaserJet Pro {runId}`.
  - DU-041-15: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Lina Sari {runId}`, aset `Scanner Canon DR-C225 {runId}`, satu hari sebelum batas Transaction timeout.
  - DU-041-16: BRW `Waiting for Handover` Borrower `Hendra Kusuma {runId}`, Requested By `Lina Sari {runId}`, aset `Shredder Fellowes 99Ci {runId}`, satu hari sebelum batas pengambilan.
  - DU-041-17: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Lina Sari {runId}`, aset `Drone DJI Mini 4 {runId}`, melewati batas Transaction timeout.
  - DU-041-18: BRW `Waiting for Handover` Borrower `Hendra Kusuma {runId}`, Requested By `Lina Sari {runId}`, aset `Genset Honda EU22i {runId}`, melewati batas pengambilan.
  - DU-041-19: BRW `Waiting for Handover` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, aset `Mixer Yamaha MG10 {runId}`, ketika level plan fitur Borrowing turun ke None pada T-0.
  - DU-041-20: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, aset `Amplifier Denon PMA-600 {runId}`, pada level plan fitur Borrowing None.
  - DU-041-21: BRW `Waiting for Handover` Borrower `Joko Susilo {runId}`, PIC `Rudi Hartono {runId}`, Requested By `Agus Pratama {runId}`, aset `Kamera Sony A7C {runId}`.
  - DU-041-22: BRW `Waiting for Handover` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, Photo at start OFF, aset `Handycam Sony FDR {runId}`.
  - DU-041-23: BRW `Waiting for Approval` Borrower `Hendra Kusuma {runId}`, Requested By `Lina Sari {runId}`, aset `Lampu Studio Godox {runId}`; Approver `Budi Santoso {runId}` belum bertindak.
  - DU-041-24: BRW `Waiting for Handover` Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, aset `Tripod Manfrotto {runId}`.
  - DU-041-25: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Mikrofon Shure SM58 {runId}`, baris Days dengan Due date T0 + 1 hari.
  - DU-041-26: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Radio Handy Motorola {runId}`, Due date T0 - 1 hari.
  - DU-041-27: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Kursi Ergonomis Ergotrend {runId}`, Due date T0 + 3 hari.
  - DU-041-28: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, aset `Meja Kerja Lipat {runId}`, Due date T0 + 3 hari.
  - DU-041-29: BRW `Borrowed` Borrower `Hendra Kusuma {runId}`, Requested By `Lina Sari {runId}`, Photo at end OFF, aset `Handheld Zebra TC21 {runId}`.
  - DU-041-30: BRW pinjaman self-service `Borrowed` Borrower `Hendra Kusuma {runId}`, Photo at end ON, aset `Tas Kamera Lowepro {runId}`.
  - DU-041-31: isian Extend: Extend By `2`, Reason `Proyek belum selesai`.
- Kondisi:
  - Switch Send email notifications untuk Borrow bernilai ON.
  - Level plan fitur Borrowing turun ke None pada T-0 untuk BRW DU-041-19 dan DU-041-20.

## Test Steps

### Submit dan Extend yang butuh approval memicu borrow_waiting_approval ke Approver
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Klik tab `Drafts` pada halaman Borrow
4. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
5. Klik menu ⋯ pada Draft milik Borrower `Hendra Kusuma {runId}` berisi DU-041-7
6. Klik `Edit`
7. Klik `[Submit]`
8. Klik `[Submit]` pada dialog `Submit Borrow`
9. Masuk sebagai `Budi Santoso {runId}`
10. Klik ikon notifikasi pada navbar
11. Verifikasi notifikasi bertipe `borrow_waiting_approval` varian `Borrow` diterima Approver `Budi Santoso {runId}` untuk BRW hasil Submit DU-041-7
12. Klik `[Detail]` pada notifikasi `borrow_waiting_approval`
13. Tinggalkan halaman keputusan tanpa memutuskan
14. Verifikasi notifikasi `borrow_waiting_approval` tetap Unread karena Approver belum memutuskan
15. Approver `Budi Santoso {runId}` menyetujui aset `Laptop Dell XPS {runId}` pada pengajuan BRW hasil Submit DU-041-7
16. Muat ulang halaman
17. Verifikasi notifikasi `borrow_waiting_approval` berubah menjadi Read karena Approver tidak punya lagi aset yang belum diputuskan di pengajuan itu
18. Aktor Borrow `Agus Pratama {runId}` mengajukan Extend aset `Proyektor Epson EB-W06 {runId}` pada BRW DU-041-8 dengan Extend By `2` dan Reason `Proyek belum selesai`
19. Masuk sebagai `Budi Santoso {runId}`
20. Klik ikon notifikasi pada navbar
21. Verifikasi notifikasi bertipe `borrow_waiting_approval` varian `Extension` diterima Approver `Budi Santoso {runId}` untuk aset `Proyektor Epson EB-W06 {runId}`

### Extend dari Borrower menunggu review memicu borrow_extension_review ke Aktor Borrow
22. Borrower `Hendra Kusuma {runId}` mengajukan Extend aset `Meja Lipat Informa {runId}` pada BRW DU-041-9 dengan Extend By `2` dan Reason `Proyek belum selesai`
23. Masuk sebagai `Agus Pratama {runId}`
24. Klik ikon notifikasi pada navbar
25. Verifikasi notifikasi bertipe `borrow_extension_review` diterima Aktor Borrow `Agus Pratama {runId}` untuk aset `Meja Lipat Informa {runId}`
26. Aktor Borrow `Agus Pratama {runId}` mengirim Review Extension Request untuk aset `Meja Lipat Informa {runId}`
27. Muat ulang halaman
28. Verifikasi notifikasi `borrow_extension_review` berubah menjadi Read karena Review Extension Request sudah dikirim

### Keputusan approval memicu borrow_resolved ke Borrower dan digabung per Borrower
29. Approver `Budi Santoso {runId}` menyetujui aset `Monitor LG UltraWide {runId}` pada BRW DU-041-10 dan aset `Keyboard Logitech MX Keys {runId}` pada BRW DU-041-11 pada hari yang sama
30. Approver `Budi Santoso {runId}` menolak aset `Mouse Logitech MX Master {runId}` pada BRW DU-041-12
31. Aktor Borrow `Agus Pratama {runId}` men-Submit Draft DU-041-13 yang Auto-approve
32. Masuk sebagai `Hendra Kusuma {runId}`
33. Klik ikon notifikasi pada navbar
34. Verifikasi notifikasi bertipe `borrow_resolved` varian `Approved` diterima Borrower `Hendra Kusuma {runId}` untuk aset `Webcam Logitech C920 {runId}` yang Auto-approved
35. Verifikasi notifikasi bertipe `borrow_resolved` varian `Rejected` diterima Borrower `Hendra Kusuma {runId}` untuk aset `Mouse Logitech MX Master {runId}`
36. Verifikasi BRW DU-041-10 dan BRW DU-041-11 yang disetujui pada hari yang sama digabung dalam satu notifikasi `borrow_resolved` untuk Borrower `Hendra Kusuma {runId}`

### Keputusan dan penutupan Extension memicu borrow_extension_resolved
37. Approver `Budi Santoso {runId}` menyetujui Extension aset `Tablet Lenovo Tab P11 {runId}` dan menolak Extension aset `Speaker Bose S1 Pro {runId}` pada BRW DU-041-14
38. Aktor Borrow `Agus Pratama {runId}` membatalkan Extension aset `Printer HP LaserJet Pro {runId}` pada BRW DU-041-14 lewat `Cancel Extension`
39. Masuk sebagai `Hendra Kusuma {runId}`
40. Klik ikon notifikasi pada navbar
41. Verifikasi notifikasi bertipe `borrow_extension_resolved` varian `Approved` diterima untuk aset `Tablet Lenovo Tab P11 {runId}`
42. Verifikasi notifikasi bertipe `borrow_extension_resolved` varian `Rejected` diterima untuk aset `Speaker Bose S1 Pro {runId}`
43. Masuk sebagai `Budi Santoso {runId}`
44. Klik ikon notifikasi pada navbar
45. Verifikasi notifikasi `borrow_extension_resolved` untuk aset `Tablet Lenovo Tab P11 {runId}` diterima Approver `Budi Santoso {runId}` sebagai hasil keputusannya sendiri
46. Verifikasi notifikasi bertipe `borrow_extension_resolved` varian `Canceled` diterima Approver `Budi Santoso {runId}` untuk aset `Printer HP LaserJet Pro {runId}` karena ia belum bertindak
47. Masuk sebagai `Agus Pratama {runId}`
48. Klik ikon notifikasi pada navbar
49. Verifikasi notifikasi `borrow_extension_review` untuk aset `Meja Lipat Informa {runId}` tetap tampil di daftar notifikasi `Agus Pratama {runId}`
50. Verifikasi tidak ada notifikasi tambahan untuk Aktor Borrow pengaju `Agus Pratama {runId}` atas pembatalan Extension aset `Printer HP LaserJet Pro {runId}`

### Peringatan Transaction timeout 1 hari lagi memicu borrow_almost_timeout
51. Job peringatan Transaction timeout 1 hari lagi berjalan untuk BRW DU-041-15 dan BRW DU-041-16
52. Masuk sebagai `Budi Santoso {runId}`
53. Klik ikon notifikasi pada navbar
54. Verifikasi notifikasi bertipe `borrow_almost_timeout` varian `Approver` diterima Approver `Budi Santoso {runId}` untuk BRW DU-041-15
55. Masuk sebagai `Lina Sari {runId}`
56. Klik ikon notifikasi pada navbar
57. Verifikasi notifikasi bertipe `borrow_almost_timeout` varian `Requester` diterima pengaju `Lina Sari {runId}` untuk BRW DU-041-15
58. Verifikasi notifikasi bertipe `borrow_almost_timeout` varian `PIC admin` diterima pengaju `Lina Sari {runId}` untuk pengingat batas pengambilan BRW DU-041-16
59. Masuk sebagai `Hendra Kusuma {runId}`
60. Klik ikon notifikasi pada navbar
61. Verifikasi Borrower `Hendra Kusuma {runId}` tidak menerima pengingat batas pengambilan untuk BRW DU-041-16

### Penutupan Canceled oleh sistem memicu borrow_auto_canceled
62. Job Transaction timeout berjalan untuk BRW DU-041-17 dan BRW DU-041-18
63. Masuk sebagai `Lina Sari {runId}`
64. Klik ikon notifikasi pada navbar
65. Verifikasi notifikasi bertipe `borrow_auto_canceled` varian `Approval timeout` diterima pengaju `Lina Sari {runId}` untuk BRW DU-041-17
66. Verifikasi notifikasi bertipe `borrow_auto_canceled` varian `Not picked up` diterima pengaju `Lina Sari {runId}` untuk BRW DU-041-18

### Level Borrowing turun ke None memicu borrow_auto_canceled dan borrow_returned Plan change
67. Auto-cancel di T-0 berjalan untuk BRW DU-041-19 karena level plan fitur Borrowing turun ke None
68. Masuk sebagai `Hendra Kusuma {runId}`
69. Klik ikon notifikasi pada navbar
70. Verifikasi notifikasi bertipe `borrow_auto_canceled` varian `Not available on plan` diterima Borrower `Hendra Kusuma {runId}` dengan alasan `Borrowing not available on plan`
71. Aktor Borrow `Agus Pratama {runId}` menjalankan `Mark as Returned` pada BRW DU-041-20
72. Masuk sebagai `Hendra Kusuma {runId}`
73. Klik ikon notifikasi pada navbar
74. Verifikasi notifikasi bertipe `borrow_returned` varian `Plan change` diterima Borrower `Hendra Kusuma {runId}` untuk aset `Amplifier Denon PMA-600 {runId}`

### Baris menjadi Waiting for Handover dan Remind Borrower mengirim ulang borrow_ready_pickup
75. Aktor Borrow `Agus Pratama {runId}` menyetujui BRW DU-041-21 sehingga barisnya menjadi Waiting for Handover
76. Masuk sebagai `Rudi Hartono {runId}`
77. Klik ikon notifikasi pada navbar
78. Verifikasi notifikasi bertipe `borrow_ready_pickup` untuk Borrower tanpa akun `Joko Susilo {runId}` diterima PIC `Rudi Hartono {runId}` dan memuat Group tempat ambil, Duration, dan batas pengambilan
79. Klik `Transactions` pada sidebar
80. Klik `Borrow`
81. Ketik Search `Joko Susilo {runId}`, tekan Enter
82. Klik menu ⋯ pada baris BRW milik DU-041-21
83. Klik `Remind Borrower`
84. Masuk sebagai `Rudi Hartono {runId}`
85. Klik ikon notifikasi pada navbar
86. Verifikasi notifikasi `borrow_ready_pickup` kedua diterima PIC `Rudi Hartono {runId}` sebagai notifikasi terpisah yang tidak digabung dengan notifikasi lain
87. Buka Borrow Detail BRW milik DU-041-21 pada layar Aktor Borrow
88. Verifikasi baris aset `Kamera Sony A7C {runId}` tetap `Waiting for Handover` dengan batas pengambilan yang sama dan Borrow Log aset itu tidak memuat node untuk Remind Borrower
89. Verifikasi email `borrow_ready_pickup` diterima PIC `Rudi Hartono {runId}` dengan Subject `[Title] · [Transaction ID]`, Body `Hi [Full Name],` berisi `Rudi Hartono {runId}`, tombol `[View Details]`, dan teks `On behalf of [Borrower Name]: you're receiving this because you're the PIC for [Borrower Name], who doesn't have a TAG Samurai account.` dengan [Borrower Name] berisi `Joko Susilo {runId}`
90. Verifikasi email `borrow_ready_pickup` juga diterima Borrower tanpa akun `Joko Susilo {runId}` pada `joko.susilo{runId}@example.com` dengan teks `You're receiving this email because email notifications are turned on for [Transaction Type] transactions in your company.` dengan [Transaction Type] berisi `Borrow`

### Handover memicu borrow_confirmation_required lalu borrow_handover_completed
91. Aktor Borrow `Agus Pratama {runId}` memulai Hand Over BRW DU-041-22 dan menekan `[Request Confirmation]`
92. Masuk sebagai `Hendra Kusuma {runId}`
93. Klik ikon notifikasi pada navbar
94. Verifikasi notifikasi bertipe `borrow_confirmation_required` diterima Borrower `Hendra Kusuma {runId}` untuk BRW DU-041-22
95. Borrower `Hendra Kusuma {runId}` menyelesaikan konfirmasi handover aset `Handycam Sony FDR {runId}`
96. Muat ulang halaman
97. Verifikasi notifikasi `borrow_confirmation_required` berubah menjadi Read karena Borrower menyelesaikan konfirmasi
98. Verifikasi notifikasi bertipe `borrow_handover_completed` diterima Borrower `Hendra Kusuma {runId}` untuk aset `Handycam Sony FDR {runId}`

### Cancel Borrow memicu borrow_canceled ke pihak yang bukan pelakunya
99. Aktor Borrow `Agus Pratama {runId}` membatalkan BRW DU-041-23 lewat `Cancel Borrow`
100. Masuk sebagai `Hendra Kusuma {runId}`
101. Klik ikon notifikasi pada navbar
102. Verifikasi notifikasi bertipe `borrow_canceled` diterima Borrower `Hendra Kusuma {runId}` karena bukan pelaku pembatalan BRW DU-041-23
103. Masuk sebagai `Budi Santoso {runId}`
104. Klik ikon notifikasi pada navbar
105. Verifikasi notifikasi bertipe `borrow_canceled` diterima Approver `Budi Santoso {runId}` yang belum bertindak untuk BRW DU-041-23
106. Borrower `Hendra Kusuma {runId}` membatalkan baris aset `Tripod Manfrotto {runId}` pada BRW DU-041-24 atas pinjamannya sendiri
107. Masuk sebagai `Agus Pratama {runId}`
108. Klik ikon notifikasi pada navbar
109. Verifikasi notifikasi bertipe `borrow_canceled` diterima Aktor Borrow Group asal `Agus Pratama {runId}` karena Borrower yang membatalkan BRW DU-041-24

### Job Due date dan Overdue memicu borrow_due_soon dan borrow_overdue
110. Job harian Due date reminders berjalan pukul 00:00 zona waktu penyewa untuk baris Days pada BRW DU-041-25
111. Masuk sebagai `Hendra Kusuma {runId}`
112. Klik ikon notifikasi pada navbar
113. Verifikasi notifikasi bertipe `borrow_due_soon` diterima Borrower `Hendra Kusuma {runId}` untuk aset `Mikrofon Shure SM58 {runId}`
114. Baris aset `Radio Handy Motorola {runId}` pada BRW DU-041-26 menjadi Overdue pada H+1
115. Masuk sebagai `Hendra Kusuma {runId}`
116. Klik ikon notifikasi pada navbar
117. Verifikasi notifikasi bertipe `borrow_overdue` varian Borrower diterima Borrower `Hendra Kusuma {runId}` untuk aset `Radio Handy Motorola {runId}`
118. Masuk sebagai `Agus Pratama {runId}`
119. Klik ikon notifikasi pada navbar
120. Verifikasi notifikasi bertipe `borrow_overdue` varian Aktor Borrow diterima `Agus Pratama {runId}` untuk aset `Radio Handy Motorola {runId}`
121. Return aset `Radio Handy Motorola {runId}` diselesaikan Aktor Borrow `Agus Pratama {runId}`
122. Muat ulang halaman
123. Verifikasi notifikasi `borrow_overdue` varian Aktor Borrow berubah menjadi Read karena baris itu dikembalikan

### Laporan kerusakan dan kehilangan saat dipinjam memicu borrow_damage_reported dan event modul lain
124. Borrower `Hendra Kusuma {runId}` mengirim laporan kerusakan aset `Kursi Ergonomis Ergotrend {runId}` pada BRW DU-041-27
125. Masuk sebagai `Agus Pratama {runId}`
126. Klik ikon notifikasi pada navbar
127. Verifikasi notifikasi bertipe `borrow_damage_reported` varian Aktor Borrow diterima `Agus Pratama {runId}` untuk aset `Kursi Ergonomis Ergotrend {runId}`
128. Masuk sebagai `Siti Rahma {runId}`
129. Klik ikon notifikasi pada navbar
130. Verifikasi notifikasi bertipe `borrow_damage_reported` varian Aktor penerima laporan dengan status Waiting for Confirmation diterima `Siti Rahma {runId}`
131. Aktor penerima laporan `Siti Rahma {runId}` mengonfirmasi laporan kerusakan aset `Kursi Ergonomis Ergotrend {runId}`
132. Muat ulang halaman
133. Verifikasi notifikasi `borrow_damage_reported` varian Aktor penerima laporan berubah menjadi Read karena laporan sudah dikonfirmasi
134. Verifikasi notifikasi bertipe `damaged_review_resolved` atau `damaged_resolved` untuk aset `Kursi Ergonomis Ergotrend {runId}` tercatat sebagai event milik modul laporan kerusakan
135. Borrower `Hendra Kusuma {runId}` mengirim laporan kehilangan aset `Meja Kerja Lipat {runId}` pada BRW DU-041-28
136. Masuk sebagai `Siti Rahma {runId}`
137. Klik ikon notifikasi pada navbar
138. Verifikasi notifikasi bertipe `missing_holder_reported` diterima `Siti Rahma {runId}` untuk aset `Meja Kerja Lipat {runId}` sebagai event milik modul laporan kehilangan

### Return memicu borrow_returned ke Borrower, pengaju, dan Review
139. Aktor Borrow `Agus Pratama {runId}` menerima Return aset `Handheld Zebra TC21 {runId}` pada BRW DU-041-29
140. Masuk sebagai `Hendra Kusuma {runId}`
141. Klik ikon notifikasi pada navbar
142. Verifikasi notifikasi bertipe `borrow_returned` diterima Borrower `Hendra Kusuma {runId}` untuk aset `Handheld Zebra TC21 {runId}`
143. Masuk sebagai `Lina Sari {runId}`
144. Klik ikon notifikasi pada navbar
145. Verifikasi notifikasi bertipe `borrow_returned` diterima pengaju `Lina Sari {runId}` karena berbeda dari pelaku Return dan Borrower
146. Borrower `Hendra Kusuma {runId}` mengembalikan sendiri aset `Tas Kamera Lowepro {runId}` pada BRW self-service DU-041-30 dengan foto return
147. Masuk sebagai `Agus Pratama {runId}`
148. Klik ikon notifikasi pada navbar
149. Verifikasi notifikasi `Review` bertipe `borrow_returned` diterima Aktor Borrow Group asal `Agus Pratama {runId}` dan memuat foto handover dan foto return
150. Verifikasi katalog event, penerima, Title, Body, dan path setiap notifikasi di atas mengikuti katalog event modul Notification dan bukan didefinisikan ulang oleh Borrow

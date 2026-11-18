---
id: TC-FA-BORROW-BE-087-log-transaksi-peristiwa
title: "Peristiwa dicatat sekali ke log transaksi dengan pelaku, detail, dan yang tidak dicatat"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["BORROW-LOGIC-17a", "BORROW-LOGIC-17b", "BORROW-LOGIC-17c", "BORROW-LOGIC-17d", "§8#r5", "§8#r6", "§8#r7", "§8.1#r6", "§8.1#r7", "§8.1#r8", "§8.1#r9", "§8.1#r10", "§8.1#r11", "§8.1#r12", "§8.1#r13", "§8.1#r14", "§8.1#r15", "§8.1#r16", "§8.1#r17", "§8.1#r18", "§8.1#r19", "§8.1#r20", "§8.1#r21", "§8.1#r22", "§8.1#r23", "§8.1#r24", "§8.1#r25", "§8.1#r26", "§8.1#r27", "§8.1#p4", "§8.3#b1", "§8.3#b2", "§8.3#b3", "§8.3#b4", "§8.3#p1", "§8.3#p2"]
smoke: []
dependsOn: []
owner: BE
trace:
  "BORROW-LOGIC-17a": 3
  "BORROW-LOGIC-17b": 29
  "BORROW-LOGIC-17c": 31
  "BORROW-LOGIC-17d": [8, 43]
  "§8#r5": 2
  "§8#r6": [43, 57]
  "§8#r7": [129, 130]
  "§8.1#r6": [4, 51]
  "§8.1#r7": [6, 7, 43]
  "§8.1#r8": 52
  "§8.1#r9": [11, 12]
  "§8.1#r10": [16, 17, 49, 56]
  "§8.1#r11": [19, 20, 25, 27, 28]
  "§8.1#r12": [41, 47]
  "§8.1#r13": [60, 61]
  "§8.1#r14": 63
  "§8.1#r15": [65, 66]
  "§8.1#r16": 69
  "§8.1#r17": [72, 75]
  "§8.1#r18": 83
  "§8.1#r19": 96
  "§8.1#r20": [98, 99]
  "§8.1#r21": [93, 101]
  "§8.1#r22": [76, 87, 89]
  "§8.1#r23": [122, 123]
  "§8.1#r24": 107
  "§8.1#r25": [119, 120]
  "§8.1#r26": [109, 110]
  "§8.1#r27": 113
  "§8.1#p4": [21, 30, 38, 77, 126]
  "§8.3#b1": [31, 32, 33]
  "§8.3#b2": [44, 53, 58, 84]
  "§8.3#b3": 132
  "§8.3#b4": [34, 102]
  "§8.3#p1": [133, 134]
  "§8.3#p2": [134, 135, 136, 137]
---

# Peristiwa dicatat sekali ke log transaksi dengan pelaku, detail, dan yang tidak dicatat

## Prerequisites
- Aktor:
  - Asset Admin DU-087-25, Group penugasan Head Office (pengaju, pemberi, penerima, dan pelaksana Mark as Returned).
  - Approver dengan Group penugasan Head Office, eligible untuk aset Head Office kecuali DU-087-6.
  - Aktor Missing: Asset Admin dengan hak Aktor Missing pada Group Head Office.
  - Total Control, cakupan seluruh client (hanya menyimpan Draft C).
  - Borrower DU-087-14 dan Borrower DU-087-15 (PIC tercatat di DU-087-15).
- Data:
  - DU-087-1: Asset, aset untuk pengajuan, approval, handover, Extension, dan Return; Asset Name `Laptop Latitude 5440 {runId}`; Group `Head Office`.
  - DU-087-2: Asset, aset untuk pengajuan yang ditolak; Asset Name `Proyektor Epson EB-X49 {runId}`; Group `Head Office`.
  - DU-087-3: Asset, aset untuk handover yang dibatalkan Cancel Request; Asset Name `Kamera Canon EOS R10 {runId}`; Group `Head Office`.
  - DU-087-4: Asset, aset untuk handover dikonfirmasi PIC; Asset Name `Tablet Samsung Galaxy Tab S9 {runId}`; Group `Head Office`.
  - DU-087-5: Asset, aset dengan approval otomatis; Asset Name `Printer Canon G3010 {runId}`; Group `Head Office`.
  - DU-087-6: Asset, aset tanpa approver yang eligible; Asset Name `Monitor Dell P2422H {runId}`; Group `Head Office`.
  - DU-087-7: Asset, aset yang melewati Due date; Asset Name `Speaker JBL PartyBox 110 {runId}`; Group `Head Office`.
  - DU-087-8: Asset, aset untuk laporan Damaged dan TAG; Asset Name `Laptop ThinkPad E14 {runId}`; Group `Head Office`.
  - DU-087-9: Asset, aset untuk laporan Missing ditolak dan dibatalkan; Asset Name `Scanner Epson V39 {runId}`; Group `Head Office`.
  - DU-087-10: Asset, aset untuk laporan Missing dikonfirmasi; Asset Name `Printer Epson L3250 {runId}`; Group `Head Office`.
  - DU-087-11: Asset, aset Borrowed saat level plan None; Asset Name `Drone DJI Mini 3 {runId}`; Group `Head Office`.
  - DU-087-12: Asset, aset untuk peminjaman mandiri; Asset Name `Kamera Sony ZV-E10 {runId}`; Group `Head Office`.
  - DU-087-13: Asset, aset untuk Cancel Borrow dengan Save as Draft to edit; Asset Name `Proyektor Optoma HD146X {runId}`; Group `Head Office`.
  - DU-087-14: User, Borrower yang punya akun login; Name `Rudi Hartono {runId}`.
  - DU-087-15: User, Borrower tanpa akun login dengan PIC; Name `Wahyu Setiawan {runId}`; PIC `Lina Susanti {runId}`.
  - DU-087-16: Parameter pengajuan, Duration dan Purpose setiap pengajuan; Duration `5 Day(s)`; Purpose `Presentasi klien {runId}`.
  - DU-087-17: Note approver, Note saat approver menyetujui; Note `Disetujui untuk presentasi klien {runId}`.
  - DU-087-18: Reason penolakan, Reason saat approver menolak aset; Reason `Proyektor dibutuhkan untuk acara internal {runId}`.
  - DU-087-19: Parameter Extension, Durasi Extension yang diajukan; Extend duration `2 Day(s)`.
  - DU-087-20: Reason penolakan Extension, Reason saat approver menolak Extension; Reason `Aset dijadwalkan untuk pemakaian lain {runId}`.
  - DU-087-21: Deskripsi Damage, Description laporan Damaged; Description `Layar retak di pojok kiri bawah {runId}`.
  - DU-087-22: Reason Missing, Reason laporan Missing dari Borrower; Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`.
  - DU-087-23: Reason penolakan Missing, Reason saat Aktor Missing menolak laporan; Reason `Laporan belum dapat diverifikasi {runId}`.
  - DU-087-24: Reason Mark as Returned, Reason saat Mark as Returned; Reason `Level plan turun ke None {runId}`.
  - DU-087-25: User, Asset Admin aktor spec ini, Group penugasan Head Office; Name `Bayu Nugroho {runId}`; Group `Head Office`; Role `Asset Admin`.
  - DU-087-26: Asset, aset Draft A; Asset Name `Laptop Asus Vivobook 14 {runId}`; Group `Head Office`.
  - DU-087-27: Asset, aset Draft B; Asset Name `Laptop Acer Aspire 5 {runId}`; Group `Head Office`.
  - DU-087-28: Asset, aset Draft C di Group Head Office; Asset Name `Monitor LG 24MP400 {runId}`; Group `Head Office`.
  - DU-087-29: Asset, aset Draft C di Group Branch Surabaya; Asset Name `Printer HP LaserJet M111w {runId}`; Group `Branch Surabaya`.
- Kondisi:
  - Setiap aset DU-087 Group Head Office berada di Group penugasan Asset Admin DU-087-25.
  - Aturan efektif aset DU-087-5 memuat `Auto-approve within 3 days`.
  - Tidak ada approver yang eligible untuk aset DU-087-6.
  - Baris aset DU-087-11 berstatus Borrowed dan entitas aktor berada di level plan None.
  - Draft A dan Draft B berisi aset di Group penugasan Asset Admin DU-087-25; Draft C juga berisi aset Group Branch Surabaya yang di luar cakupannya.

## Test Steps

### Pengajuan dicatat sekali dan terbaca lewat tiga tampilan
1. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-1 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
2. Verifikasi peristiwa `Borrow requested by [Actor]` untuk aset DU-087-1 tercatat tepat satu entri dengan pelaku pengaju
3. Verifikasi catatan peristiwa itu terbaca di Borrow Log per aset dalam BRW, Transaction log aset, dan Transaction admin log dari satu sumber peristiwa
4. Verifikasi detail node memuat Duration `5 Day(s)`, Purpose `Presentasi klien {runId}`, dan Approval `Waiting 1 approver`

### Keputusan approver dicatat per aset
5. Approver menyetujui aset DU-087-1 dengan Note `Disetujui untuk presentasi klien {runId}`
6. Verifikasi node `Approved by [Approver]` untuk aset DU-087-1 tercatat dengan pelaku Approver yang menyetujui
7. Verifikasi detail node memuat Approved duration `5 Day(s)`, Mode `Any one`, dan Note `Disetujui untuk presentasi klien {runId}`
8. Verifikasi keputusan approver pada aset DU-087-1 mencatat mode, waktu, dan pelaku

### Penolakan mencatat Reason apa adanya
9. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-2 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
10. Approver menolak aset DU-087-2 dengan Reason `Proyektor dibutuhkan untuk acara internal {runId}`
11. Verifikasi node `Rejected by [Approver]` untuk aset DU-087-2 tercatat dengan pelaku Approver yang menolak
12. Verifikasi detail Reason memuat `Proyektor dibutuhkan untuk acara internal {runId}` persis seperti diketik, tanpa diterjemahkan

### Cancel Borrow oleh Aktor Borrow dengan Save as Draft to edit
13. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-13 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
14. Approver menyetujui aset DU-087-13
15. Asset Admin DU-087-25 membatalkan baris aset DU-087-13 lewat Cancel Borrow dengan opsi `Save as Draft to edit`
16. Verifikasi node `Canceled by [Actor]` untuk aset DU-087-13 tercatat dengan pelaku Asset Admin DU-087-25 dan baris detail `Saved as draft`
17. Verifikasi node `Canceled by [Actor]` itu tidak memuat Reason karena pelakunya bukan `System`

### Serah terima Aktor Borrow dengan Borrower yang punya akun
18. Asset Admin DU-087-25 menyerahkan aset DU-087-1 kepada Borrower DU-087-14 dengan Condition `Normal`
19. Verifikasi node `Handed over by [Giver]` untuk aset DU-087-1 tercatat dengan pelaku Asset Admin DU-087-25
20. Verifikasi detail node memuat Duration `5 Day(s)`, Due date, Condition `Normal`, dan Confirmation `Accepted`
21. Verifikasi Borrow Log aset DU-087-1 tidak memuat node `Confirmed`, `Verified`, maupun `Level n approved`

### Serah terima untuk Borrower tanpa akun dikonfirmasi PIC
22. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-4 atas nama Borrower DU-087-15 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
23. Approver menyetujui aset DU-087-4
24. Asset Admin DU-087-25 menyerahkan aset DU-087-4 kepada Borrower DU-087-15 dengan Condition `Normal`, PIC DU-087-15 mengonfirmasi atas nama Borrower
25. Verifikasi detail node `Handed over by [Giver]` untuk aset DU-087-4 memuat Confirmation `Confirmed by [Actor or PIC] on behalf of [Borrower]`

### Peminjaman mandiri Borrower dicatat tanpa jejak di log yang tidak dipakai
26. Borrower DU-087-14 meminjam aset DU-087-12 lewat self-service dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
27. Verifikasi node `Borrowed via self-service by [Borrower]` untuk aset DU-087-12 tercatat dengan pelaku Borrower DU-087-14
28. Verifikasi detail node memuat Confirmation `Confirmed (self)`
29. Verifikasi peristiwa itu terbaca di log pengguna Borrower DU-087-14
30. Verifikasi Transaction admin log tidak memuat baris atas tindakan Borrower DU-087-14 atas pinjamannya sendiri
31. Verifikasi Changelog tidak memuat entri peristiwa Borrow atas aset DU-087-12
32. Verifikasi System Log tidak memuat entri peristiwa Borrow atas aset DU-087-12
33. Verifikasi Activity Log tidak memuat entri peristiwa Borrow atas aset DU-087-12
34. Verifikasi TAG Log aset DU-087-12 tidak memuat entri dari Borrow

### Handover dibatalkan Aktor Borrow dan Remind Borrower tidak dicatat
35. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-3 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
36. Approver menyetujui aset DU-087-3
37. Asset Admin DU-087-25 menjalankan Remind Borrower pada baris aset DU-087-3 yang berstatus Waiting for Handover
38. Verifikasi Borrow Log aset DU-087-3 tidak memuat node dari Remind Borrower
39. Asset Admin DU-087-25 memulai handover aset DU-087-3
40. Asset Admin DU-087-25 menjalankan `Cancel Request` atas handover aset DU-087-3
41. Verifikasi node `Handover not confirmed` untuk aset DU-087-3 tercatat dengan pelaku Asset Admin DU-087-25 dan baris tetap Waiting for Handover

### Approval otomatis dan jendela konfirmasi handover oleh System
42. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-5 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
43. Verifikasi node `Auto-approved` untuk aset DU-087-5 tercatat dengan pelaku `System` dan Rule `Auto-approve within 3 days`
44. Verifikasi peristiwa `Auto-approved` itu terbaca di log pengguna Borrower DU-087-14 dengan pelaku `System`
45. Asset Admin DU-087-25 memulai handover aset DU-087-5
46. Waktu berlalu sampai jendela konfirmasi handover berakhir
47. Verifikasi node `Handover not confirmed` untuk aset DU-087-5 tercatat dengan pelaku `System` dan baris tetap Waiting for Handover
48. Waktu berlalu sampai batas pengambilan aset terlewati
49. Verifikasi node `Canceled by [Actor]` untuk aset DU-087-5 tercatat dengan pelaku `System` dan Reason `Not picked up`

### Approval dialihkan dan penutupan timeout oleh System
50. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-6 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
51. Verifikasi detail Approval node `Borrow requested by [Actor]` untuk aset DU-087-6 memuat `Routed to: Group Manager (no eligible approver)`
52. Verifikasi node `Approval rerouted` untuk aset DU-087-6 tercatat dengan pelaku `System`, Routed to Group Manager, dan Reason `No eligible approver`
53. Verifikasi peristiwa approval dialihkan itu terbaca di log pengguna Borrower DU-087-14 dengan pelaku `System`
54. Waktu berlalu sampai batas Waiting for Approval terlewati
55. Job Transaction timeout berjalan
56. Verifikasi node `Canceled by [Actor]` untuk aset DU-087-6 tercatat dengan pelaku `System` dan Reason `Timed out (Waiting for Approval)`
57. Verifikasi peristiwa dari job tanpa user aktor memakai aktor `System` dan Action node katalog yang bersangkutan
58. Verifikasi peristiwa penutupan timeout itu terbaca di log pengguna Borrower DU-087-14 dengan pelaku `System`

### Extension diajukan, diteruskan, dan disetujui
59. Borrower DU-087-14 mengajukan Extend aset DU-087-1 dengan Extend duration `2 Day(s)`
60. Verifikasi node `Extension requested by [Actor]` untuk aset DU-087-1 tercatat dengan pelaku Borrower DU-087-14 dan Extend duration `2 Day(s)`
61. Verifikasi detail node itu memuat Proposed due date
62. Asset Admin DU-087-25 meneruskan permintaan Extension aset DU-087-1 ke approval
63. Verifikasi node `Extension forwarded to approval by [Actor]` untuk aset DU-087-1 tercatat dengan pelaku Asset Admin DU-087-25 dan Approval `Waiting 1 approver`
64. Approver menyetujui Extension aset DU-087-1
65. Verifikasi node `Extension approved by [Approver]` untuk aset DU-087-1 tercatat dengan pelaku Approver yang menyetujui
66. Verifikasi detail node memuat Due date lama dan baru serta Extension dengan format `n of max`

### Extension ditolak dan dibatalkan
67. Asset Admin DU-087-25 mengajukan Extend aset DU-087-1 dengan Extend duration `2 Day(s)`
68. Approver menolak Extension aset DU-087-1 dengan Reason `Aset dijadwalkan untuk pemakaian lain {runId}`
69. Verifikasi node `Extension rejected by [Actor]` untuk aset DU-087-1 tercatat dengan pelaku Approver dan Reason `Aset dijadwalkan untuk pemakaian lain {runId}`
70. Asset Admin DU-087-25 mengajukan Extend aset DU-087-1 dengan Extend duration `2 Day(s)`
71. Asset Admin DU-087-25 menjalankan Cancel Extension atas pengajuan itu
72. Verifikasi node `Extension canceled by [Actor]` untuk aset DU-087-1 tercatat dengan pelaku Asset Admin DU-087-25
73. Asset Admin DU-087-25 mengajukan Extend aset DU-087-1 dengan Extend duration `2 Day(s)`
74. Asset Admin DU-087-25 menerima kembali aset DU-087-1 dengan Condition `Normal`
75. Verifikasi node `Extension canceled by [Actor]` untuk pengajuan terakhir tercatat dengan pelaku `System` dan Reason `Asset returned`
76. Verifikasi node `Returned to [Receiver]` untuk aset DU-087-1 tercatat dengan penerima Asset Admin DU-087-25 dan Condition `Normal`
77. Verifikasi Borrow Log aset DU-087-1 tidak memuat node edit Extension

### Overdue oleh System dan pengembalian terlambat
78. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-7 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
79. Approver menyetujui aset DU-087-7
80. Asset Admin DU-087-25 menyerahkan aset DU-087-7 kepada Borrower DU-087-14 dengan Condition `Normal`
81. Waktu berlalu sampai 1 hari sesudah Due date aset DU-087-7
82. Job Overdue berjalan
83. Verifikasi node `Overdue` untuk aset DU-087-7 tercatat dengan pelaku `System` dan Due date
84. Verifikasi peristiwa `Overdue` itu terbaca di log pengguna Borrower DU-087-14 dengan pelaku `System`
85. Waktu berlalu sampai 2 hari sesudah Due date aset DU-087-7
86. Asset Admin DU-087-25 menerima kembali aset DU-087-7 dengan Condition `Normal`
87. Verifikasi detail node `Returned to [Receiver]` untuk aset DU-087-7 memuat Late dengan format `n days`

### Pengembalian mandiri oleh Borrower
88. Borrower DU-087-14 mengembalikan aset DU-087-12 lewat self-service
89. Verifikasi node `Returned via self-service by [Borrower]` untuk aset DU-087-12 tercatat dengan pelaku Borrower DU-087-14

### Damage dilaporkan lalu dibatalkan dan TAG dilaporkan
90. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-8 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
91. Approver menyetujui aset DU-087-8
92. Asset Admin DU-087-25 menjalankan `I Can't Scan the TAG` saat menyerahkan aset DU-087-8
93. Verifikasi node `TAG reported by [Reporter]` untuk aset DU-087-8 dari Handover tercatat dengan pelaku Asset Admin DU-087-25 dan kode TAG yang dilaporkan
94. Asset Admin DU-087-25 menyerahkan aset DU-087-8 kepada Borrower DU-087-14 dengan Condition `Normal`
95. Borrower DU-087-14 melaporkan kerusakan aset DU-087-8 dengan Description `Layar retak di pojok kiri bawah {runId}`
96. Verifikasi node `Damage reported by [Reporter]` untuk aset DU-087-8 tercatat dengan pelaku Borrower DU-087-14, Type, Description `Layar retak di pojok kiri bawah {runId}`, dan Report No.
97. Borrower DU-087-14 membatalkan laporan kerusakan aset DU-087-8
98. Verifikasi node `Damage report canceled by [Actor]` untuk aset DU-087-8 tercatat dengan pelaku Borrower DU-087-14 dan Report No.
99. Verifikasi baris aset DU-087-8 tetap berstatus Borrowed sesudah laporan dibatalkan
100. Asset Admin DU-087-25 menjalankan `I Can't Scan the TAG` saat menerima kembali aset DU-087-8
101. Verifikasi node `TAG reported by [Reporter]` untuk aset DU-087-8 tercatat dengan pelaku Asset Admin DU-087-25, kode semua TAG yang dilaporkan, Report Type, dan Report No.
102. Verifikasi TAG Log aset DU-087-8 memuat entri dari laporan TAG yang dipicu `I Can't Scan the TAG` saat Return

### Laporan Missing ditolak atau dibatalkan
103. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-9 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
104. Approver menyetujui aset DU-087-9
105. Asset Admin DU-087-25 menyerahkan aset DU-087-9 kepada Borrower DU-087-14 dengan Condition `Normal`
106. Borrower DU-087-14 melaporkan kehilangan aset DU-087-9 dengan Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`
107. Verifikasi node `Reported missing by [Actor]` untuk aset DU-087-9 tercatat dengan pelaku Borrower DU-087-14, Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`, dan Status `Waiting for Confirmation`
108. Aktor yang berhak atas laporan kehilangan menolak laporan kehilangan aset DU-087-9 dengan Reason `Laporan belum dapat diverifikasi {runId}`
109. Verifikasi node `Missing report rejected by [Actor]` untuk aset DU-087-9 tercatat dengan pelaku aktor yang berhak atas laporan kehilangan dan Reason `Laporan belum dapat diverifikasi {runId}`
110. Verifikasi baris aset DU-087-9 tetap berstatus Borrowed sesudah laporan ditolak
111. Borrower DU-087-14 melaporkan kehilangan aset DU-087-9 dengan Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`
112. Borrower DU-087-14 membatalkan laporan kehilangan aset DU-087-9
113. Verifikasi node `Missing report canceled by [Actor]` untuk aset DU-087-9 tercatat dengan pelaku Borrower DU-087-14

### Laporan Missing dikonfirmasi
114. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-10 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
115. Approver menyetujui aset DU-087-10
116. Asset Admin DU-087-25 menyerahkan aset DU-087-10 kepada Borrower DU-087-14 dengan Condition `Normal`
117. Borrower DU-087-14 melaporkan kehilangan aset DU-087-10 dengan Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`
118. Aktor yang berhak atas laporan kehilangan mengonfirmasi laporan kehilangan aset DU-087-10
119. Verifikasi node `Missing confirmed by [Actor]` untuk aset DU-087-10 tercatat dengan pelaku aktor yang berhak atas laporan kehilangan
120. Verifikasi baris aset DU-087-10 ditutup `Returned` dengan penanda `Missing`

### Mark as Returned saat level plan None
121. Asset Admin DU-087-25 menjalankan Mark as Returned pada aset DU-087-11 dengan Outcome `Returned` dan Reason `Level plan turun ke None {runId}`
122. Verifikasi node `Returned by [Actor]` untuk aset DU-087-11 tercatat dengan pelaku Asset Admin DU-087-25, penanda `Plan change`, Outcome `Returned`, dan Reason `Level plan turun ke None {runId}`
123. Verifikasi node `Returned by [Actor]` itu tidak memuat scan dan foto

### Bulk Delete Draft menulis satu entri per Draft yang berhasil
124. Asset Admin DU-087-25 menyimpan Draft A berisi aset DU-087-26 untuk Borrower DU-087-14
125. Asset Admin DU-087-25 menyimpan Draft B berisi aset DU-087-27 untuk Borrower DU-087-14
126. Verifikasi Borrow Log dan Transaction log aset DU-087-26 tidak memuat peristiwa dari penyimpanan Draft A
127. Total Control menyimpan Draft C berisi aset DU-087-28 dan aset DU-087-29 untuk Borrower DU-087-14
128. Asset Admin DU-087-25 menjalankan bulk Delete Draft atas Draft A, Draft B, dan Draft C
129. Verifikasi Transaction admin log Asset Admin DU-087-25 memuat satu entri untuk Draft A dan satu entri untuk Draft B
130. Verifikasi Draft C yang dilewati karena di luar cakupan tidak menulis entri di Transaction admin log Asset Admin DU-087-25

### Aksi Asset Admin hanya menulis Transaction admin log dan Download tidak dicatat
131. Asset Admin DU-087-25 mengunduh daftar transaksi Borrow
132. Verifikasi Transaction admin log Asset Admin DU-087-25 tidak memuat entri baru dari Download
133. Verifikasi tindakan transaksi Asset Admin DU-087-25 atas aset DU-087-7 tercatat di Transaction admin log sebagai surface log transaksi terpisah
134. Verifikasi tindakan itu tidak menulis Activity Log aktor Asset Admin DU-087-25
135. Verifikasi tindakan itu tidak menulis System Log aktor Asset Admin DU-087-25
136. Verifikasi riwayat aset DU-087-7 dalam BRW-nya dibaca di Borrow Log
137. Verifikasi tindakan itu disimpan sekali dan terbaca lewat Borrow Log dan Transaction admin log dari catatan yang sama

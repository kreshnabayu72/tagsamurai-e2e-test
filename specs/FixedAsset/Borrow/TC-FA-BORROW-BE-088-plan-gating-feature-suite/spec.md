---
id: TC-FA-BORROW-BE-088-plan-gating-feature-suite
title: "Ketersediaan Borrow per level None, Basic, dan Full dan penolakan server atas fitur terkunci"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["BORROW-LOGIC-19a", "BORROW-LOGIC-19b", "BORROW-LOGIC-19c", "BORROW-LOGIC-19d", "BORROW-LOGIC-19e", "BORROW-LOGIC-19f", "BORROW-LOGIC-19g", "BORROW-LOGIC-19i", "BORROW-LOGIC-19k", "BORROW-LOGIC-19l", "BORROW-LOGIC-19m", "BORROW-LOGIC-19o", "BORROW-LOGIC-19p", "BORROW-LOGIC-19q", "BORROW-LOGIC-19s", "BORROW-LOGIC-19t", "BORROW-LOGIC-19u", "BORROW-LOGIC-19v", "BORROW-LOGIC-19y", "BORROW-LOGIC-19z", "§9.11#p2", "§9.11#r1", "§9.11#r2", "§9.11#r3", "§9.11#r4", "§9.11#r5", "§9.11#r6", "§9.11#r7", "§9.11#r8", "§9.11#r9", "§9.11#r10", "§9.11#r11", "§9.11#r12", "§9.11#r13", "§9.11#r14", "§9.11#r15", "§9.11#r16", "§9.11#r17", "§9.11#r18", "§9.11#r19", "§9.11#r20", "§9.11#p6", "§9.11#p8"]
smoke: []
dependsOn: []
owner: BE
trace:
  "BORROW-LOGIC-19a": [2, 7, 61, 98]
  "BORROW-LOGIC-19b": 3
  "BORROW-LOGIC-19c": 4
  "BORROW-LOGIC-19d": 100
  "BORROW-LOGIC-19e": 101
  "BORROW-LOGIC-19f": [103, 104, 105, 106]
  "BORROW-LOGIC-19g": [108, 110]
  "BORROW-LOGIC-19i": [118, 119, 120]
  "BORROW-LOGIC-19k": [112, 113]
  "BORROW-LOGIC-19l": 114
  "BORROW-LOGIC-19m": 115
  "BORROW-LOGIC-19o": [22, 40, 46, 48, 50, 53, 56, 57]
  "BORROW-LOGIC-19p": 10
  "BORROW-LOGIC-19q": 11
  "BORROW-LOGIC-19s": 58
  "BORROW-LOGIC-19t": [21, 40, 48, 53, 59, 111]
  "BORROW-LOGIC-19u": 102
  "BORROW-LOGIC-19v": 121
  "BORROW-LOGIC-19y": 116
  "BORROW-LOGIC-19z": 122
  "§9.11#p2": 5
  "§9.11#r1": 2
  "§9.11#r2": 7
  "§9.11#r3": 61
  "§9.11#r4": 98
  "§9.11#r5": [9, 13, 15, 18, 25, 29, 33, 35, 37, 42]
  "§9.11#r6": [9, 13, 29, 33, 42]
  "§9.11#r7": 15
  "§9.11#r8": [18, 19]
  "§9.11#r9": [35, 36]
  "§9.11#r10": 37
  "§9.11#r11": [25, 27]
  "§9.11#r12": 10
  "§9.11#r13": [48, 50, 63, 65]
  "§9.11#r14": [51, 66]
  "§9.11#r15": [40, 69]
  "§9.11#r16": [46, 74]
  "§9.11#r17": [53, 76]
  "§9.11#r18": [56, 78]
  "§9.11#r19": [57, 79]
  "§9.11#r20": [21, 85]
  "§9.11#p6": [123, 124]
  "§9.11#p8": [23, 34, 54, 117]
---

# Ketersediaan Borrow per level None, Basic, dan Full dan penolakan server atas fitur terkunci

## Prerequisites
- Aktor:
  - Principal, operator di luar tenant yang mengubah plan entitas DU-088-1.
  - Total Control entitas DU-088-1, cakupan seluruh client (menyimpan Transaction Settings).
  - Asset Admin DU-088-2, Group penugasan Head Office dan Branch Surabaya.
  - Approver DU-088-3, Group penugasan Head Office, eligible untuk aset Head Office.
  - Borrower DU-088-4, punya akun login.
- Data:
  - DU-088-1: Entitas, Entitas khusus spec ini dengan plan yang diubah Principal; Entity Name `Entitas Borrow Plan {runId}`.
  - DU-088-2: User, Asset Admin pengaju, Group penugasan Head Office dan Branch Surabaya; Name `Citra Wulandari {runId}`; Role `Asset Admin`.
  - DU-088-3: User, Approver, Group penugasan Head Office; Name `Hendra Saputra {runId}`; Role `Approver`.
  - DU-088-4: User, Borrower yang punya akun login; Name `Gita Permata {runId}`.
  - DU-088-5: Asset, aset dipinjam pada level Basic, di-Extend, dilaporkan rusak, lalu dikembalikan; Asset Name `Laptop Lenovo ThinkPad T14 {runId}`; Group `Head Office`.
  - DU-088-6: Asset, aset Group lain pada form multi-Group, dipinjam lalu Overdue pada level Basic; Asset Name `Proyektor Epson EB-FH06 {runId}`; Group `Branch Surabaya`.
  - DU-088-7: Asset, aset dalam BRW yang sama dengan aset pertama, dilaporkan hilang pada level Basic; Asset Name `Tablet Samsung Galaxy Tab A9 {runId}`; Group `Head Office`.
  - DU-088-8: Asset, aset untuk Draft pada level Basic dan Full; Asset Name `Printer Canon PIXMA MG3670 {runId}`; Group `Head Office`.
  - DU-088-9: Asset, aset untuk Cancel Borrow pada level Basic; Asset Name `Kamera Sony Alpha A6400 {runId}`; Group `Head Office`.
  - DU-088-10: Asset, aset untuk timeout Not picked up pada level Basic; Asset Name `Speaker Bose S1 Pro {runId}`; Group `Head Office`.
  - DU-088-11: Asset, aset untuk self-service pada level Basic; Asset Name `Monitor Samsung S24 {runId}`; Group `Head Office`.
  - DU-088-12: Asset, aset untuk satuan Hours pada level Basic; Asset Name `Scanner Fujitsu iX1300 {runId}`; Group `Head Office`.
  - DU-088-13: Asset, aset untuk Cancel Borrow ke Draft pada level Full; Asset Name `Laptop HP ProBook 450 {runId}`; Group `Head Office`.
  - DU-088-14: Asset, aset untuk timeout Not picked up ke Draft pada level Full; Asset Name `Mikrofon Shure SM58 {runId}`; Group `Head Office`.
  - DU-088-15: Asset, aset untuk self-service pada level Full; Asset Name `Drone DJI Air 3 {runId}`; Group `Head Office`.
  - DU-088-16: Asset, aset untuk satuan Hours pada level Full; Asset Name `Gimbal DJI RS 3 {runId}`; Group `Head Office`.
  - DU-088-17: Asset, aset pada baris Waiting for Approval saat downgrade ke None; Asset Name `Laptop Dell Latitude 7440 {runId}`; Group `Head Office`.
  - DU-088-18: Asset, aset pada baris Waiting for Handover saat downgrade ke None; Asset Name `Proyektor BenQ MH550 {runId}`; Group `Head Office`.
  - DU-088-19: Asset, aset pada baris Borrowed dengan Extension menunggu saat downgrade ke None; Asset Name `Kamera Nikon Z50 {runId}`; Group `Head Office`.
  - DU-088-20: Asset, aset pada baris Overdue saat downgrade ke None; Asset Name `Tablet Apple iPad Air {runId}`; Group `Head Office`.
  - DU-088-21: Parameter pengajuan plan, Duration dan Purpose pengajuan satuan Days; Duration `4 Day(s)`; Purpose `Kunjungan klien {runId}`.
  - DU-088-22: Parameter pengajuan jam, Duration dan Purpose pengajuan satuan Hours; Duration `6 Hour(s)`; Purpose `Kunjungan klien {runId}`.
  - DU-088-23: Parameter Extension plan, Durasi Extension yang diajukan; Extend duration `2 Day(s)`.
  - DU-088-24: Transaction Settings Borrow, Nilai Transaction Settings yang disimpan sebelum downgrade; Self service `ON`; Duration unit `Hours`.
  - DU-088-25: Deskripsi kerusakan plan, Description laporan kerusakan; Description `Layar retak di pojok kiri bawah {runId}`.
  - DU-088-26: Reason kehilangan plan, Reason laporan kehilangan; Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`.
- Kondisi:
  - Spec ini memakai entitas khusus DU-088-1 yang tidak dipakai spec lain.
  - Plan entitas DU-088-1 awalnya berada di slot `free`.
  - Approval Workflow tidak aktif pada slot `paid_1` dan aktif pada slot `paid_2` dan `paid_3`.
  - Seluruh aset DU-088 berstatus `Available` dan tidak dipakai transaksi lain sebelum spec dimulai.

## Test Steps

### Slot plan free memetakan Borrowing ke level None
1. Principal menetapkan plan entitas DU-088-1 ke slot `free`
2. Verifikasi level Feature Suite Borrowing entitas DU-088-1 adalah `None`
3. Verifikasi level Borrowing yang aktif ditetapkan oleh plan entitas
4. Verifikasi Borrowing tidak punya pengaturan tersendiri untuk menyalakan atau mematikannya di luar level plan
5. Verifikasi ketersediaan Borrowing dibaca dari nilai fitur plan, bukan dari nama maupun rank plan

### Slot plan paid_1 memetakan Borrowing ke level Basic
6. Principal menetapkan plan entitas DU-088-1 ke slot `paid_1`
7. Verifikasi level Feature Suite Borrowing entitas DU-088-1 adalah `Basic`

### Pengajuan form multi-Group diterima dan dipecah pada level Basic
8. Asset Admin DU-088-2 mengajukan BRW dalam satu form untuk aset DU-088-5, DU-088-7, dan DU-088-6 atas nama Borrower DU-088-4 dengan Duration `4 Day(s)` dan Purpose `Kunjungan klien {runId}`
9. Verifikasi pengajuan diterima pada level Basic
10. Verifikasi aset DU-088-5 dan DU-088-7 dari Group Head Office masuk satu BRW dan aset DU-088-6 dari Group Branch Surabaya masuk BRW lain
11. Verifikasi baris pengajuan berstatus `Waiting for Handover` karena Approval Workflow plan `paid_1` tidak aktif, terpisah dari level Borrowing

### Handover, konfirmasi Borrower, dan Extend oleh Aktor Borrow pada level Basic
12. Asset Admin DU-088-2 menyerahkan aset DU-088-5 kepada Borrower DU-088-4 dengan Condition `Normal`
13. Verifikasi baris aset DU-088-5 berstatus `Borrowed` dengan Due date
14. Borrower DU-088-4 mengonfirmasi handover aset DU-088-5 lewat Confirm on This Device untuk satuan Days
15. Verifikasi konfirmasi Borrower atas handover aset DU-088-5 diterima
16. Asset Admin DU-088-2 menyerahkan aset DU-088-7 kepada Borrower DU-088-4 dengan Condition `Normal`
17. Asset Admin DU-088-2 menjalankan Extend aset DU-088-5 dengan Extend duration `2 Day(s)`
18. Verifikasi Extend oleh Aktor Borrow atas aset DU-088-5 langsung berlaku dan Due date bertambah
19. Verifikasi Extend aset DU-088-5 tidak melewati approval karena Approval Workflow plan `paid_1` tidak aktif

### Request Extension oleh Borrower ditolak server pada level Basic
20. Borrower DU-088-4 mengajukan Request Extension dari halaman pinjamannya untuk aset DU-088-5
21. Verifikasi pengajuan Extension oleh Borrower dari halaman pinjamannya ditolak dan tidak ada pengajuan Extension baru
22. Verifikasi level Basic tidak menyediakan Request Extension oleh Borrower
23. Verifikasi notifikasi Extension oleh Borrower tidak dikirim pada level Basic

### Report kerusakan dan kehilangan saat dipinjam pada level Basic
24. Asset Admin DU-088-2 melaporkan kerusakan aset DU-088-5 dengan Description `Layar retak di pojok kiri bawah {runId}`
25. Verifikasi laporan kerusakan aset DU-088-5 saat dipinjam diterima
26. Asset Admin DU-088-2 melaporkan kehilangan aset DU-088-7 dengan Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`
27. Verifikasi laporan kehilangan aset DU-088-7 saat dipinjam diterima

### Return dan Overdue pada level Basic
28. Asset Admin DU-088-2 menerima kembali aset DU-088-5 dengan Condition `Normal`
29. Verifikasi baris aset DU-088-5 berstatus `Returned`
30. Asset Admin DU-088-2 menyerahkan aset DU-088-6 kepada Borrower DU-088-4 dengan Condition `Normal`
31. Waktu berlalu sampai 1 hari sesudah Due date aset DU-088-6
32. Job Overdue berjalan
33. Verifikasi baris aset DU-088-6 berstatus `Overdue`
34. Verifikasi notifikasi `borrow_overdue` untuk aset DU-088-6 dikirim ke Borrower DU-088-4 pada level Basic

### Tab Transactions, History, Borrowed Assets By Asset dan kontribusi ke halaman pinjaman Borrower pada level Basic
35. Verifikasi BRW aset DU-088-5 terbaca di daftar Transactions dan History pada level Basic
36. Verifikasi aset DU-088-6 terbaca di Borrowed Assets By Asset pada level Basic
37. Verifikasi aset DU-088-6 terbaca di daftar Borrowed milik Borrower DU-088-4 dan Task Confirm Handover tersedia

### Cancel dan timeout tidak membentuk Draft pada level Basic
38. Asset Admin DU-088-2 mengajukan BRW untuk aset DU-088-9 atas nama Borrower DU-088-4 dengan Duration `4 Day(s)` dan Purpose `Kunjungan klien {runId}`
39. Asset Admin DU-088-2 menjalankan Cancel Borrow atas baris aset DU-088-9 dengan opsi `Save as Draft to edit`
40. Verifikasi opsi `Save as Draft to edit` ditolak dan tidak ada Draft baru berisi aset DU-088-9
41. Asset Admin DU-088-2 menjalankan Cancel Borrow atas baris aset DU-088-9 tanpa opsi Draft
42. Verifikasi baris aset DU-088-9 berstatus `Canceled` pada level Basic
43. Asset Admin DU-088-2 mengajukan BRW untuk aset DU-088-10 atas nama Borrower DU-088-4 dengan Duration `4 Day(s)` dan Purpose `Kunjungan klien {runId}`
44. Waktu berlalu sampai batas `Not picked up` aset DU-088-10 terlewati
45. Job Transaction timeout berjalan
46. Verifikasi baris aset DU-088-10 ditutup `Canceled` tanpa Draft baru

### Draft tidak tersedia pada level Basic
47. Asset Admin DU-088-2 menyimpan Draft berisi aset DU-088-8 untuk Borrower DU-088-4
48. Verifikasi penyimpanan Draft ditolak dan tidak ada Draft baru
49. Asset Admin DU-088-2 menjalankan `Add to Borrow Draft` untuk aset DU-088-8
50. Verifikasi `Add to Borrow Draft` ditolak dan tidak ada Draft baru
51. Verifikasi tab Drafts tidak tersedia dan permintaan tab Drafts menampilkan tab Transactions

### Self-service, satuan Hours, dan By Borrower tidak tersedia pada level Basic
52. Borrower DU-088-4 meminjam aset DU-088-11 lewat `Borrow Now` self-service dengan Duration `4 Day(s)` dan Purpose `Kunjungan klien {runId}`
53. Verifikasi peminjaman self-service aset DU-088-11 ditolak dan baris tidak terbentuk
54. Verifikasi notifikasi self-service baru tidak dikirim pada level Basic
55. Asset Admin DU-088-2 mengajukan BRW untuk aset DU-088-12 atas nama Borrower DU-088-4 dengan Duration `6 Hour(s)` dan Purpose `Kunjungan klien {runId}`
56. Verifikasi pengajuan aset DU-088-12 dengan satuan Hours ditolak karena Duration hanya Days
57. Verifikasi permintaan Borrowed Assets By Borrower mengembalikan tampilan By Asset

### Field terkunci tampil disabled dan server menolak aksi terkunci pada level Basic
58. Verifikasi field Self service dan Duration unit di Transaction Settings tampil disabled dengan tooltip `Available on plans with full Borrowing.`
59. Verifikasi server menolak setiap aksi fitur terkunci walau permintaannya lolos dari UI

### Slot plan paid_2 memetakan Borrowing ke level Full dan Draft tersedia
60. Principal menetapkan plan entitas DU-088-1 ke slot `paid_2`
61. Verifikasi level Feature Suite Borrowing entitas DU-088-1 adalah `Full`
62. Asset Admin DU-088-2 menyimpan Draft berisi aset DU-088-8 untuk Borrower DU-088-4
63. Verifikasi Draft berisi aset DU-088-8 tersimpan pada level Full
64. Asset Admin DU-088-2 menjalankan `Add to Borrow Draft` untuk aset DU-088-8
65. Verifikasi aset DU-088-8 masuk Draft bersama pada level Full
66. Verifikasi Draft berisi aset DU-088-8 terbaca di tab Drafts

### Cancel dan timeout membentuk Draft pada level Full
67. Asset Admin DU-088-2 mengajukan BRW untuk aset DU-088-13 atas nama Borrower DU-088-4 dengan Duration `4 Day(s)` dan Purpose `Kunjungan klien {runId}`
68. Asset Admin DU-088-2 menjalankan Cancel Borrow atas baris aset DU-088-13 dengan opsi `Save as Draft to edit`
69. Verifikasi baris aset DU-088-13 berstatus `Canceled` dan Draft baru berisi aset DU-088-13 terbentuk
70. Asset Admin DU-088-2 mengajukan BRW untuk aset DU-088-14 atas nama Borrower DU-088-4 dengan Duration `4 Day(s)` dan Purpose `Kunjungan klien {runId}`
71. Approver DU-088-3 menyetujui aset DU-088-14
72. Waktu berlalu sampai batas `Not picked up` aset DU-088-14 terlewati
73. Job Transaction timeout berjalan
74. Verifikasi baris aset DU-088-14 ditutup `Canceled` dan Draft baru berisi aset DU-088-14 terbentuk

### Self-service, satuan Hours, dan By Borrower tersedia pada level Full
75. Borrower DU-088-4 meminjam aset DU-088-15 lewat `Borrow Now` self-service dengan Duration `4 Day(s)` dan Purpose `Kunjungan klien {runId}`
76. Verifikasi peminjaman self-service aset DU-088-15 diterima dan baris berstatus `Borrowed`
77. Asset Admin DU-088-2 mengajukan BRW untuk aset DU-088-16 atas nama Borrower DU-088-4 dengan Duration `6 Hour(s)` dan Purpose `Kunjungan klien {runId}`
78. Verifikasi pengajuan aset DU-088-16 dengan satuan Hours diterima
79. Verifikasi Borrowed Assets By Borrower terbaca dengan Borrower DU-088-4

### Request Extension oleh Borrower diterima pada level Full dan baris disiapkan untuk downgrade
80. Asset Admin DU-088-2 mengajukan BRW untuk aset DU-088-19 atas nama Borrower DU-088-4 dengan Duration `4 Day(s)` dan Purpose `Kunjungan klien {runId}`
81. Approver DU-088-3 menyetujui aset DU-088-19
82. Asset Admin DU-088-2 menyerahkan aset DU-088-19 kepada Borrower DU-088-4 dengan Condition `Normal`
83. Borrower DU-088-4 mengonfirmasi handover aset DU-088-19
84. Borrower DU-088-4 mengajukan Request Extension dari halaman pinjamannya untuk aset DU-088-19 dengan Extend duration `2 Day(s)`
85. Verifikasi Request Extension oleh Borrower atas aset DU-088-19 diterima dan menunggu review
86. Due date aset DU-088-19 dicatat sebagai Due date sebelum downgrade
87. Asset Admin DU-088-2 mengajukan BRW untuk aset DU-088-17 atas nama Borrower DU-088-4 dengan Duration `4 Day(s)` dan Purpose `Kunjungan klien {runId}`
88. Asset Admin DU-088-2 mengajukan BRW untuk aset DU-088-18 atas nama Borrower DU-088-4 dengan Duration `4 Day(s)` dan Purpose `Kunjungan klien {runId}`
89. Approver DU-088-3 menyetujui aset DU-088-18
90. Asset Admin DU-088-2 mengajukan BRW untuk aset DU-088-20 atas nama Borrower DU-088-4 dengan Duration `4 Day(s)` dan Purpose `Kunjungan klien {runId}`
91. Approver DU-088-3 menyetujui aset DU-088-20
92. Asset Admin DU-088-2 menyerahkan aset DU-088-20 kepada Borrower DU-088-4 dengan Condition `Normal`
93. Borrower DU-088-4 mengonfirmasi handover aset DU-088-20
94. Waktu berlalu sampai 1 hari sesudah Due date aset DU-088-20
95. Job Overdue berjalan
96. Total Control menyimpan Transaction Settings Borrow dengan Self service `ON` dan Duration unit `Hours`

### Slot plan paid_3 memetakan Borrowing ke level Full
97. Principal menetapkan plan entitas DU-088-1 ke slot `paid_3`
98. Verifikasi level Feature Suite Borrowing entitas DU-088-1 adalah `Full`

### Downgrade ke None menutup menunggu, menjaga yang berjalan, dan menolak transaksi baru
99. Principal menetapkan plan entitas DU-088-1 ke slot `free` dan downgrade berlaku di T-0
100. Verifikasi menu `Transactions > Borrow` tampil disabled dengan chip Upgrade
101. Verifikasi permintaan langsung ke halaman Borrow tidak membuka fitur
102. Verifikasi halaman Borrow menampilkan state tidak tersedia mengikuti pola fitur lain yang terkunci
103. Verifikasi menu `Approvals > Borrow` tidak tampil
104. Verifikasi Quick Action Borrow tidak tampil
105. Verifikasi aksi `Borrow` dan `Add to Borrow Draft` di daftar aset tidak tampil
106. Verifikasi bagian Borrow di Transaction Settings tidak tampil
107. Asset Admin DU-088-2 mengajukan BRW untuk aset DU-088-5 atas nama Borrower DU-088-4 dengan Duration `4 Day(s)` dan Purpose `Kunjungan klien {runId}`
108. Verifikasi pengajuan BRW baru ditolak dengan kode galat `PLAN_FEATURE_UNAVAILABLE`
109. Asset Admin DU-088-2 menyerahkan aset DU-088-18 kepada Borrower DU-088-4 dengan Condition `Normal`
110. Verifikasi aksi Handover ditolak dengan kode galat `PLAN_FEATURE_UNAVAILABLE`
111. Verifikasi server menolak setiap aksi Borrow pada level None walau permintaannya lolos dari UI
112. Verifikasi Request Extension aset DU-088-19 yang menunggu ikut `Canceled` dengan Reason `Borrowing not available on plan`
113. Verifikasi Due date aset DU-088-19 sama dengan Due date yang dicatat sebelum downgrade
114. Verifikasi baris aset DU-088-17 dan aset DU-088-18 ditutup `Canceled` dan Custody kedua aset kembali `Available` karena aset belum diserahkan
115. Verifikasi baris aset DU-088-19 tetap `Borrowed` dan baris aset DU-088-20 tetap `Overdue` tanpa ditutup otomatis
116. Verifikasi status `Overdue` aset DU-088-20 tetap dihitung tanpa notifikasi `borrow_overdue` baru ke Borrower DU-088-4
117. Verifikasi notifikasi `borrow_due_soon` dan `borrow_overdue` tidak dikirim pada level None
118. Verifikasi riwayat Borrow aset DU-088-19 tetap terbaca di Transaction log aset
119. Verifikasi riwayat Borrow aset DU-088-19 tetap terbaca di Transaction admin log
120. Verifikasi riwayat Borrow aset DU-088-19 tetap terbaca di log pengguna Borrower DU-088-4
121. Verifikasi Transaction Settings Borrow tersimpan dengan Self service `ON` dan Duration unit `Hours` dipertahankan
122. Verifikasi nilai tersimpan dan transaksi berjalan aset DU-088-19 dan aset DU-088-20 tidak diubah oleh fitur yang terkunci
123. Verifikasi laporan dan widget Borrow di Reports dan Dashboard disembunyikan sementara riwayat tetap terbaca di Transaction log aset
124. Verifikasi tab Borrowed milik Borrower DU-088-4 tampil read-only tanpa Cancel, Return, Report, dan Extension selama aset DU-088-19 masih berjalan

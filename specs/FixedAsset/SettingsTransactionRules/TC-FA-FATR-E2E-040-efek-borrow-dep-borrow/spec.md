---
id: TC-FA-FATR-E2E-040-efek-borrow-dep-borrow
title: "Setting Borrow berlaku pada transaksi Borrow"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceRules: ["§4.1#r76", "§4.1#r82", "§4.1#r86", "§4.1#r178", "§9.2#b166", "§9.7#r28", "§9.7#r29", "EB-XM-2@borrow", "§4.1#r72", "§4.1#r73", "§4.1#r96", "§9.2#b92", "§9.2#b203", "§9.2#b222", "§9.2#b244", "§9.2#b384", "§9.2#b404", "§9.2#b410", "§9.2#b463", "§9.4.2#r35", "§9.4.2#r37", "§9.4.2#r40", "§9.4.2#r42", "§9.4.2#r60", "§9.4.2#r82", "§9.4.2#r122", "§9.4.2#r127", "§9.4.2#r146", "§9.7#r6", "§9.10.1#p10"]
smoke: ["§4.1#r72", "§4.1#r73", "§4.1#r96", "§9.2#b92", "§9.2#b203", "§9.2#b222", "§9.2#b244", "§9.2#b384", "§9.2#b404", "§9.2#b410", "§9.2#b463", "§9.4.2#r35", "§9.4.2#r37", "§9.4.2#r40", "§9.4.2#r42", "§9.4.2#r60", "§9.4.2#r82", "§9.4.2#r122", "§9.4.2#r127", "§9.4.2#r146", "§9.7#r6", "§9.10.1#p10"]
dependsOn:
  - "Borrow: pengajuan, Extension, dan Return"
trace:
  "§4.1#r76": 4
  "§4.1#r82": 14
  "§4.1#r86": 19
  "§4.1#r178": 22
  "§9.2#b166": 63
  "§9.7#r28": [101, 104]
  "§9.7#r29": 93
  "EB-XM-2@borrow": [63, 75, 82]
  "§4.1#r72": 3
  "§4.1#r73": 6
  "§4.1#r96": 26
  "§9.2#b92": 68
  "§9.2#b203": [93, 94]
  "§9.2#b222": 96
  "§9.2#b244": 95
  "§9.2#b384": [4, 27]
  "§9.2#b404": 32
  "§9.2#b410": 31
  "§9.2#b463": 49
  "§9.4.2#r35": 27
  "§9.4.2#r37": 37
  "§9.4.2#r40": [43, 44]
  "§9.4.2#r42": [87, 88]
  "§9.4.2#r60": 7
  "§9.4.2#r82": 82
  "§9.4.2#r122": 52
  "§9.4.2#r127": 89
  "§9.4.2#r146": 15
  "§9.7#r6": 82
  "§9.10.1#p10": 38
anchor: [10, 18, 33, 55, 65, 99]
coverage:
  web: automated
---

# Setting Borrow berlaku pada transaksi Borrow

## Prerequisites
- Aktor: Default User yang memegang Manage transaction settings (Update); aktor lain yang masuk sebagai pemicu atau pengguna: `Agus Pratama {runId}`, `Budi Santoso {runId}`, `Dewi Anggraini {runId}`, `Hendra Gunawan {runId}`, `Maya Puspita {runId}`, `Rizal Hidayat {runId}`.
- Layar awal: Fixed Asset > Borrow.
- Data:
  - DU-040-1: Group Name `Workshop {runId}`; Group tanpa Division.
  - DU-040-2: Group Name `Warehouse {runId}`; Group tanpa Division.
  - DU-040-3: Category Name `Machinery {runId}`; Category leaf.
  - DU-040-4: Category Name `Cranes {runId}`, Allow Borrow `Allow`; Category leaf dengan Allow Borrow nilai sendiri.
  - DU-040-5: User Name `Budi Santoso {runId}`, Role `Employee`, Group `Workshop {runId}`; akun aktif.
  - DU-040-6: User Name `Sari Wulandari {runId}`, Role `Employee`, Group `Workshop {runId}`; akun aktif.
  - DU-040-7: User Name `Agus Pratama {runId}`, Role `Employee`, Group `Warehouse {runId}`; akun aktif.
  - DU-040-8: User Name `Dewi Anggraini {runId}`, Role `Employee`, Group `Workshop {runId}`, Role Transaksi `Approver` dan `Aktor Borrow`; akun aktif.
  - DU-040-9: User Name `Hendra Gunawan {runId}`, Role `Group Manager`, Group `Workshop {runId}`, Role Transaksi `Aktor Borrow`; akun aktif.
  - DU-040-10: User Name `Rizal Hidayat {runId}`, Role `Employee`, Group `Warehouse {runId}`, Role Transaksi `Approver`; akun aktif.
  - DU-040-11: User Name `Maya Puspita {runId}`, Role `Employee`, Group `Warehouse {runId}`, Role Transaksi `Approver`; akun aktif.
  - DU-040-12: User Name `Joko Susilo {runId}`, Role `Employee`, Group `Warehouse {runId}`; akun aktif.
  - DU-040-13: Asset Name `Excavator PC200 {runId}`, Category `Machinery {runId}`, Group `Workshop {runId}`, Status `Available`; aset.
  - DU-040-14: Asset Name `Wheel Loader L120 {runId}`, Category `Machinery {runId}`, Group `Workshop {runId}`, Status `Borrowed`; aset.
  - DU-040-15: Asset Name `Dump Truck HD785 {runId}`, Category `Cranes {runId}`, Group `Warehouse {runId}`, Status `Overdue`; aset.
  - DU-040-16: Asset Name `Forklift FD25 {runId}`, Category `Machinery {runId}`, Group `Workshop {runId}`, Status `Available`; aset.
  - DU-040-17: Asset Name `Generator GN50 {runId}`, Category `Machinery {runId}`, Group `Workshop {runId}`, Status `Available`; aset.
  - DU-040-18: Asset Name `Welding Machine WM30 {runId}`, Category `Machinery {runId}`, Group `Workshop {runId}`, Status `Waiting for Handover`; aset.
  - DU-040-19: Asset Name `Projector PJ200 {runId}`, Category `Machinery {runId}`, Group `Workshop {runId}`, Status `Available`; aset.
  - DU-040-20: Asset Name `Surveying Total Station TS60 {runId}`, Category `Machinery {runId}`, Group `Workshop {runId}`, Status `Available`; aset.
  - DU-040-21: Asset Name `Drilling Rig DR20 {runId}`, Category `Machinery {runId}`, Group `Workshop {runId}`, Status `Available`; aset.
  - DU-040-22: Asset Name `Crane RT540 {runId}`, Category `Cranes {runId}`, Group `Warehouse {runId}`, Status `Available`; aset.
  - DU-040-23: Asset Name `Tower Crane TC50 {runId}`, Category `Cranes {runId}`, Group `Warehouse {runId}`, Status `Waiting for Approval`; aset.
  - DU-040-24: Asset Name `Air Compressor AC10 {runId}`, Category `Machinery {runId}`, Group `Warehouse {runId}`, Status `Waiting for Approval`; aset.
  - DU-040-25: Asset Name `Concrete Mixer CM40 {runId}`, Category `Machinery {runId}`, Group `Warehouse {runId}`, Status `Waiting for Handover`; aset.
  - DU-040-26: Asset Name `Pickup Hilux D-Cab {runId}`, Category `Machinery {runId}`, Group `Workshop {runId}`, Status `Returned`; aset.
  - DU-040-27: Asset Name `Printer Epson L805 {runId}`, Category `Machinery {runId}`, Group `Workshop {runId}`, Status `Available, kondisi Damaged`; aset berkondisi Damaged.
  - DU-040-28: Override Target `Excavator PC200 {runId}`, Scope `Asset`, Transaction `Borrow`, Block new borrow when overdue `ON`; override Asset untuk Borrow.
  - DU-040-29: Override Target `Wheel Loader L120 {runId}`, Scope `Asset`, Transaction `Borrow`, Max duration `7 Days`, Max extensions `2`; override Asset untuk Borrow.
  - DU-040-30: Override Target `Backhoe BH80 {runId}`, Scope `Asset`, Transaction `Borrow`, Max extensions `0`; override Asset untuk Borrow.
  - DU-040-31: Override Target `Forklift FD25 {runId}`, Scope `Asset`, Transaction `Borrow`, Allowed borrower `Same Division only`; override Asset untuk Borrow.
  - DU-040-32: Override Target `Generator GN50 {runId}`, Scope `Asset`, Transaction `Borrow`, Max assets per borrower (concurrent) `1`; override Asset untuk Borrow.
  - DU-040-33: Override Target `Projector PJ200 {runId}`, Scope `Asset`, Transaction `Borrow`, Require approval `OFF`; override Asset untuk Borrow.
  - DU-040-34: Override Target `Surveying Total Station TS60 {runId}`, Scope `Asset`, Transaction `Borrow`, Require approval `ON`; override Asset untuk Borrow.
  - DU-040-35: Override Target `Drilling Rig DR20 {runId}`, Scope `Asset`, Transaction `Borrow`, Require approval `ON`; override Asset untuk Borrow.
  - DU-040-36: Override Target `Tower Crane TC50 {runId}`, Scope `Asset`, Transaction `Borrow`, Require approval `ON`, Approval type `Any one approver`; override Asset untuk Borrow.
  - DU-040-37: Borrow Asset `Dump Truck HD785 {runId}`, Borrower `Budi Santoso {runId}`, Status `Overdue`, Handover `T0 − 10 hari`, Due date `T0 − 3 hari`; pinjaman Overdue milik Borrower.
  - DU-040-38: Borrow Asset `Wheel Loader L120 {runId}`, Borrower `Agus Pratama {runId}`, Status `Borrowed`, Handover `T0 − 5 hari`, Due date `T0 + 2 hari`; pinjaman Borrowed dengan total lama pinjam 7 hari sejak handover.
  - DU-040-39: Borrow Asset `Welding Machine WM30 {runId}`, Borrower `Sari Wulandari {runId}`, Status `Waiting for Handover`; satu baris aktif milik Borrower.
  - DU-040-40: Borrow Asset `Tower Crane TC50 {runId}`, Borrower `Agus Pratama {runId}`, Status `Waiting for Approval`, Approvers `Rizal Hidayat {runId}, Maya Puspita {runId}`; pengajuan yang diajukan sebelum Category Cranes bernilai Deny.
  - DU-040-41: Borrow Asset `Air Compressor AC10 {runId}`, Borrower `Joko Susilo {runId}`, Status `Waiting for Approval`, Diajukan `T0 − 30 hari`; pengajuan yang sudah melewati batas Transaction timeout.
  - DU-040-42: Borrow Asset `Concrete Mixer CM40 {runId}`, Borrower `Joko Susilo {runId}`, Status `Waiting for Handover`, Disetujui `T0 − 30 hari`; pengajuan yang sudah melewati batas Transaction timeout.
  - DU-040-43: Borrow Asset `Pickup Hilux D-Cab {runId}`, Borrower `Joko Susilo {runId}`, Status `Returned`, Photo at start `ada`, Photo at end `ada`; pinjaman Returned dengan foto awal dan foto akhir.
  - DU-040-44: Asset Name `Backhoe BH80 {runId}`, Category `Machinery {runId}`, Group `Workshop {runId}`, Status `Borrowed`; aset.
  - DU-040-45: Borrow Asset `Backhoe BH80 {runId}`, Borrower `Agus Pratama {runId}`, Status `Borrowed`, Handover `T0 − 2 hari`, Due date `T0 + 5 hari`; pinjaman Borrowed yang Due date-nya belum lewat.
- Kondisi:
  - Akun semua aktor di atas aktif dan kredensialnya tersedia untuk login.
  - Role Transaksi `Approver` untuk Group `Workshop {runId}` hanya dipegang `Dewi Anggraini {runId}`, dan untuk Group `Warehouse {runId}` dipegang `Rizal Hidayat {runId}` dan `Maya Puspita {runId}`.
  - Level Feature Suite Borrowing entitas bernilai `Full`.
  - `Dewi Anggraini {runId}` dan `Hendra Gunawan {runId}` berhak mengajukan Borrow karena memegang Role Transaksi `Aktor Borrow` untuk Group `Workshop {runId}`.
  - Form Extension menampilkan batas Max duration sebagai informasi pada pemilih tanggal dan menerima New due date di atas batas itu; penolakannya dievaluasi di server.
  - Pengajuan Borrow aset `Air Compressor AC10 {runId}` dan `Concrete Mixer CM40 {runId}` sudah melewati batas Transaction timeout statusnya masing-masing.

## Test Steps
### Pengajuan Borrow untuk Borrower yang punya pinjaman Overdue diblokir
1. Mulai pengajuan Borrow baru untuk aset `Excavator PC200 {runId}`
2. Pilih Borrower `Budi Santoso {runId}`
3. Verifikasi pengajuan diblokir segera setelah Borrower dipilih, sebelum Submit
4. Verifikasi pesan blokir menyebut siapa yang dapat dihubungi
5. Klik `[Submit]`
6. Verifikasi pengajuan ditolak saat Submit
7. Verifikasi penolakan berlaku lintas Category, Group, dan aset: pinjaman Overdue `Dump Truck HD785 {runId}` milik Borrower berada di Category `Cranes {runId}` dan Group `Warehouse {runId}`, berbeda dari Category `Machinery {runId}` dan Group `Workshop {runId}` milik aset yang dimohon, dan pengajuan tetap ditolak

### Extension yang membuat total melebihi Max duration ditolak
8. Masuk sebagai `Agus Pratama {runId}`
9. Buka pinjaman aset `Wheel Loader L120 {runId}` di daftar Borrow
10. Verifikasi aksi Extend ditawarkan pada pinjaman aset `Wheel Loader L120 {runId}`
11. Catat Due date pinjaman
12. Ajukan Extension 1 hari melewati batas Max duration yang ditampilkan pada form, sehingga total lama pinjam sejak handover menjadi 8 hari
13. Klik `[Submit]`
14. Verifikasi pesan blokir `Can't extend: this borrow has reached its maximum duration. Contact [Aktor Borrow].` tampil dengan nama kontak terisi pada `[Aktor Borrow]`
15. Verifikasi Extension ditolak dan Due date pinjaman sama dengan Due date yang dicatat

### Max extensions bernilai 0 tidak menawarkan Extend
16. Masuk sebagai `Agus Pratama {runId}`
17. Buka pinjaman aset `Backhoe BH80 {runId}` di daftar Borrow
18. Verifikasi pinjaman aset `Backhoe BH80 {runId}` berstatus `Borrowed`
19. Verifikasi aksi Extend tidak ditawarkan pada pinjaman aset `Backhoe BH80 {runId}`

### Foto akhir tampil bersama foto awal
20. Masuk sebagai Default User
21. Buka detail pengembalian pinjaman aset `Pickup Hilux D-Cab {runId}`
22. Verifikasi foto awal dan foto akhir sama-sama tampil pada detail pengembalian pinjaman aset `Pickup Hilux D-Cab {runId}`

### Allowed borrower menolak Borrower yang tidak memenuhi
23. Mulai pengajuan Borrow baru untuk aset `Forklift FD25 {runId}`
24. Pilih Borrower `Sari Wulandari {runId}`
25. Klik `[Submit]`
26. Verifikasi pengajuan ditolak karena Group asal aset tidak punya Division sehingga Borrower tidak memenuhi Allowed borrower
27. Verifikasi pesan blokir menyebut siapa yang dapat dihubungi

### Max assets per borrower menolak pengajuan yang melebihi kuota
28. Mulai pengajuan Borrow baru untuk aset `Generator GN50 {runId}`
29. Pilih Borrower `Sari Wulandari {runId}`
30. Klik `[Submit]`
31. Verifikasi pengajuan ditolak saat Submit karena melebihi Max assets per borrower (concurrent)
32. Verifikasi baris aktif Borrower `Sari Wulandari {runId}` berjumlah 1, yaitu aset `Welding Machine WM30 {runId}`, sehingga bersama baris baru menjadi 2 dan melebihi batas `1`

### Require approval OFF melewati langkah approval
33. Verifikasi pengajuan Borrow aset `Tower Crane TC50 {runId}` berstatus `Waiting for Approval`
34. Mulai pengajuan Borrow baru untuk aset `Projector PJ200 {runId}`
35. Pilih Borrower `Hendra Gunawan {runId}`
36. Klik `[Submit]`
37. Verifikasi langkah approval dilewati dan tidak ada permintaan approval untuk pengajuan aset `Projector PJ200 {runId}`
38. Verifikasi pengajuan aset `Projector PJ200 {runId}` langsung lanjut ke tahap eksekusi Borrow dengan status `Waiting for Handover`

### Pengaju yang menjadi satu-satunya Approver langsung Approved
39. Masuk sebagai `Dewi Anggraini {runId}`
40. Mulai pengajuan Borrow baru untuk aset `Surveying Total Station TS60 {runId}`
41. Pilih Borrower `Dewi Anggraini {runId}`
42. Klik `[Submit]`
43. Verifikasi pengajuan langsung `Approved` dengan log `Approved by system (no independent approver)`
44. Verifikasi `Dewi Anggraini {runId}` tidak menjadi approver transaksinya sendiri

### Pengaju Group Manager langsung Approved
45. Masuk sebagai `Hendra Gunawan {runId}`
46. Mulai pengajuan Borrow baru untuk aset `Drilling Rig DR20 {runId}`
47. Pilih Borrower `Hendra Gunawan {runId}`
48. Klik `[Submit]`
49. Verifikasi pengajuan langsung `Approved` dengan log `Approved by [Nama] (Group Manager — requester)` dengan `[Nama]` terisi `Hendra Gunawan {runId}`

### Aset Damaged tidak dapat dipinjam
50. Masuk sebagai Default User
51. Mulai pengajuan Borrow baru untuk aset `Printer Epson L805 {runId}`
52. Verifikasi aset `Printer Epson L805 {runId}` tidak dapat diajukan untuk Borrow karena kondisi asetnya
53. Tutup form pengajuan Borrow yang belum diubah

### Override Allow Borrow Deny dan penghapusannya tercermin di Borrow
54. Ketik Search `Crane RT540 {runId}` pada daftar aset di Fixed Asset > Borrow, tekan Enter
55. Verifikasi aksi Borrow pada baris aset `Crane RT540 {runId}` aktif
56. Buka tab Borrow pada node Category `Cranes {runId}` di Fixed Asset > Settings > Transaction Settings
57. Klik `[+ Override]` pada bagian Overrides
58. Isi Scope `Asset` dengan Target `Crane RT540 {runId}`
59. Pilih Field `Allow Borrow` dengan Value `Deny`
60. Klik `[Submit]`
61. Buka Fixed Asset > Borrow
62. Ketik Search `Crane RT540 {runId}` pada daftar aset di Fixed Asset > Borrow, tekan Enter
63. Verifikasi aksi Borrow pada baris aset `Crane RT540 {runId}` disabled, dengan alasan dan kontak tersampaikan pada aksi itu
64. Buka tab Borrow pada node Category `Cranes {runId}` di Fixed Asset > Settings > Transaction Settings
65. Verifikasi nilai Allow Borrow pada Category `Cranes {runId}` tetap `Allow`
66. Buka Fixed Asset > Borrow
67. Ketik Search `Crane RT540 {runId}` pada daftar aset di Fixed Asset > Borrow, tekan Enter
68. Verifikasi aksi Borrow pada baris aset `Crane RT540 {runId}` tetap disabled meskipun Category `Cranes {runId}` bernilai `Allow`
69. Buka tab Borrow pada node Category `Cranes {runId}` di Fixed Asset > Settings > Transaction Settings
70. Buka menu ⋯ pada baris override untuk `Crane RT540 {runId}`
71. Klik `Delete`
72. Klik `[Delete]` pada dialog Delete Override
73. Buka Fixed Asset > Borrow
74. Ketik Search `Crane RT540 {runId}` pada daftar aset di Fixed Asset > Borrow, tekan Enter
75. Verifikasi aksi Borrow pada baris aset `Crane RT540 {runId}` aktif lagi

### Perubahan nilai Category berlaku untuk transaksi baru
76. Buka tab Borrow pada node Category `Cranes {runId}` di Fixed Asset > Settings > Transaction Settings
77. Pilih nilai `Deny` pada field Allow Borrow
78. Klik `[Save]`
79. Klik `[Save]` pada dialog Save Changes
80. Buka Fixed Asset > Borrow
81. Ketik Search `Crane RT540 {runId}` pada daftar aset di Fixed Asset > Borrow, tekan Enter
82. Verifikasi aksi Borrow pada baris aset `Crane RT540 {runId}` disabled sesuai nilai baru Category `Cranes {runId}` dan evaluasi pengajuan baru memakai nilai itu

### Keputusan pertama dan transaksi berjalan memakai setting saat diajukan
83. Masuk sebagai `Maya Puspita {runId}`
84. Buka permintaan approval Borrow aset `Tower Crane TC50 {runId}` yang diajukan `Agus Pratama {runId}`
85. `Rizal Hidayat {runId}` menyetujui permintaan approval Borrow aset `Tower Crane TC50 {runId}`
86. Tolak permintaan approval yang masih terbuka di layar
87. Verifikasi keputusan pertama menentukan transaksi: pengajuan aset `Tower Crane TC50 {runId}` tidak berstatus `Rejected`
88. Verifikasi status `Maya Puspita {runId}` pada transaksi aset `Tower Crane TC50 {runId}` adalah `Not Involved`
89. Verifikasi pengajuan aset `Tower Crane TC50 {runId}`, yang diajukan sebelum Category `Cranes {runId}` bernilai `Deny`, tidak dibatalkan otomatis dan tetap diproses memakai setting saat diajukan

### Transaksi yang melewati Transaction timeout kembali ke Draft
90. Masuk sebagai Default User
91. Job Transaction timeout berjalan
92. Buka tab Drafts di Borrow
93. Verifikasi Draft baru memuat aset `Air Compressor AC10 {runId}`
94. Verifikasi Draft baru memuat aset `Concrete Mixer CM40 {runId}`
95. Verifikasi Draft baru aset `Air Compressor AC10 {runId}` tidak bernomor BRW dan pengajuannya tidak berstatus Canceled atau Expired
96. Verifikasi hasil timeout pengajuan Borrow aset `Air Compressor AC10 {runId}` adalah kembali ke Draft
97. Buka daftar Borrow
98. Ketik Search `Welding Machine WM30 {runId}`, tekan Enter
99. Verifikasi baris pembanding aset `Welding Machine WM30 {runId}` berstatus `Waiting for Handover` tampil di daftar Borrow
100. Ganti isi kotak search dengan `Air Compressor AC10 {runId}`, tekan Enter
101. Verifikasi daftar Borrow tidak memuat baris aset `Air Compressor AC10 {runId}` berstatus `Waiting for Approval`
102. Buka tab Drafts di Borrow
103. Buka detail Draft baru aset `Air Compressor AC10 {runId}`
104. Verifikasi detail Draft itu menampilkan aset `Air Compressor AC10 {runId}` dan tidak berstatus `Waiting for Approval`

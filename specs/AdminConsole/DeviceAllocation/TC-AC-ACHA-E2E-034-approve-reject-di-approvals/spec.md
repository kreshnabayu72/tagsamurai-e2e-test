---
id: TC-AC-ACHA-E2E-034-approve-reject-di-approvals
title: "Approve dan Reject di Approvals > Device Allocation: Efek pada Status, Wallet, Log, Approver Sah, dan Aksi Idempoten"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-256
  - TC-AC-ACHA-257
  - TC-AC-ACHA-258
  - TC-AC-ACHA-259
  - TC-AC-ACHA-260
  - TC-AC-ACHA-261
  - TC-AC-ACHA-262
  - TC-AC-ACHA-263
  - TC-AC-ACHA-264
  - TC-AC-ACHA-265
  - TC-AC-ACHA-474
  - TC-AC-ACHA-475
coverage:
  web: automated
---

# Approve dan Reject di Approvals > Device Allocation: Efek pada Status, Wallet, Log, Approver Sah, dan Aksi Idempoten

## Prerequisites

- Mode: FE+BE. Aksi Approve dan Reject dilakukan di Approvals > Device Allocation (modul Approvals); efeknya diasersi pada modul Device Allocation, Wallet Balance, dan Allocation Log.
- Akun (password lewat env, nama baru didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script). Login TC_DIST di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Akun lain dipakai lewat Step ganti akun eksplisit.

| Alias | Pre-setup | Email | Env password | Dipakai di |
|---|---|---|---|---|
| TC_DIST | #27 Total Control Distributor | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_DIST_PASSWORD` | TC-256, 261, 264, 265 |
| MB_ON | #32 Group Member Distributor toggle ON (pembuat) | `memberOnDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_MB_ON_PASSWORD` | TC-256 butir e, TC-261 butir e |
| GM_DIST | #29 Group Manager Group Jakarta | `groupManagerDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_GM_DIST_PASSWORD` | TC-259 |
| AA_DIST | #37 Additional Approver Group Jakarta | `additionalApprover_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_ADD_APPROVER_PASSWORD` | TC-260 |
| TC_PRIN | #21 Total Control Principal | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_PRIN_PASSWORD` | TC-257 |
| TC_P2 | #46 Total Control Partner CV Karya Mandiri | `totalControlPartner2_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_P2_PASSWORD` | TC-258, 262, 474, 475 |
| MB_APR | #42 Group Member toggle ON sekaligus Additional Approver | `memberApprover_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_MB_APR_PASSWORD` | TC-263 |

- Data Pre-setup yang dibaca: Distributor PT Global Distribusi (#3), Partner CV Karya Mandiri (#5, toggle loncat ke Principal aktif), Client PT Sejahtera Logistik (#7), PT Cipta Kreasi (#9), PT Manufaktur Unggul (#10), harga (#14, #15), kantong PT Global Distribusi $20,000.00 (#16), kantong A CV Karya Mandiri $1,000.00 (#18), kantong B CV Karya Mandiri $3,000.00 (#19).
- Data seed milik spec (seeding API di hook `before` atau langkah penyiapan tiap blok, mekanisme disediakan tim FE/BE; Allocation ID ditangkap saat runtime). Tiap blok memakai transaksi Waiting for Approval sendiri karena Approve dan Reject mengubah status secara permanen:
  - Atribut Pre-setup #49 (dibuat MB_ON): RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00 pada kantong PT Global Distribusi (saldo $20,000.00), untuk TC-256, 259, 260, 261, 264, 265, serta satu transaksi tambahan sebagai anchor TC-263.
  - Atribut #51 (dibuat MB_PRIN, Principal tanpa wallet): Handheld Reader Long Range, Quantity 10, Client PT Manufaktur Unggul, Payment Free, untuk TC-257.
  - Atribut #50 (dibuat MB_P2): NFC, Quantity 40, Client PT Cipta Kreasi, Pay From `PT Global Distribusi (Distributor)`, Total Cost $60.00, Reserve $60.00 pada kantong A, untuk TC-258 dan TC-262.
  - Atribut #70 (dibuat MB_P2): NFC, Quantity 40, Client PT Cipta Kreasi, Pay From `PT ABC (Principal)`, Total Cost $48.00, Reserve $48.00 pada kantong B, untuk TC-474 dan TC-475.
  - Atribut #65 (dibuat MB_APR): RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Total Cost $250.00, untuk TC-263.
  - Nilai literal `Batch uji`, `Stok belum siap`, dan `Tidak sesuai` diasersi TC (pengecualian S-12 nama literal, Lampiran A butir A-6).
- Kemampuan teknis (disediakan tim FE/BE, kontrak fixture tidak tertulis di TC): fixture API Pre-setup #20 untuk menyetel saldo dan Reserved kantong sebelum tiap blok, mematikan toggle loncat ke Principal CV Karya Mandiri dan memulihkannya (TC-474, 475), membaca kuota Client dan status transaksi, membaca jumlah entri Allocation Log, dan membaca jumlah notifikasi pembuat; sesi API TC_DIST (sebagai pelaku pertama TC-264 dan TC-265).
- Waktu (S-12): jam server dan jam browser sinkron; Last Updated pada List dibandingkan dengan waktu Reject yang dicatat sesudah aksi dengan toleransi satu menit.
- Kolom Cost ditampilkan lewat Setup Column pada langkah penyiapan TC-261 (precondition TC); preferensi kolom dipulihkan hook `after` suite.
- Jendela absence notifikasi in-app (pilihan spec sesuai TC-AC-ACHA-408 b dan 412, bukan nilai PRD): "Tunggu 5 detik tanpa memuat ulang halaman" ditulis sebelum asersi absence notifikasi pembuat MB_ON pada TC-AC-ACHA-264, sesudah anchor positif `Verifikasi` jumlah notifikasi pembuat sama dengan M0 + 1.
- State global yang diubah dan pemulihannya: saldo dan Reserved kantong, toggle loncat ke Principal CV Karya Mandiri; dipulihkan lewat langkah penghubung dan hook `after`. Suite berjalan serial (`parallel: false`).
- Hook suite (`suite.md`): flag Guided Tooltip halaman Device Allocation true untuk akun aktor, sesi API aktor, fixture API Pre-setup #20.

## Test Steps

### Approve oleh Total Control Distributor (TC-AC-ACHA-256)

1. Siapkan transaksi Waiting for Approval (atribut #49) dan kantong PT Global Distribusi saldo $20,000.00 Reserved $250.00 lewat fixture; catat Last Updated transaksi (LU0)
2. Buka Approvals > Device Allocation > Active Tab, buka transaksi itu
3. Klik `[Approve]`, lalu konfirmasi pada dialog
4. Verifikasi toast sukses di Approvals: "Success, transaction has been approved."
5. Buka Allocation > Device Allocation
6. Ketik Search Allocation ID transaksi blok TC-256 (atribut #49), tekan Enter
7. Verifikasi Status transaksi `Completed`
8. Verifikasi Last Updated transaksi berubah dari LU0
9. Buka Wallet Balance kantong PT Global Distribusi
10. Verifikasi Reserved $0.00
11. Verifikasi saldo $19,750.00 (Capture memakai snapshot harga, tanpa hitung ulang)
12. Buka modal Allocation Log transaksi
13. Verifikasi entri `Allocation approved by [PIC]` tanpa Description tampil
14. Verifikasi entri `Allocation approved by [PIC]` berada di atas entri `Allocation created`
15. Tutup modal

### Reject oleh Total Control Distributor (TC-AC-ACHA-261)

16. Siapkan transaksi Waiting for Approval (atribut #49) dan kantong PT Global Distribusi saldo $20,000.00 Reserved $250.00 lewat fixture; tampilkan kolom Cost lewat Setup Column, klik `[Save]`
17. Buka Approvals > Device Allocation > Active Tab, buka transaksi itu, isi Rejection Reason `Stok belum siap`
18. Klik `[Reject]`, lalu konfirmasi pada dialog
19. Verifikasi toast sukses di Approvals: "Success, transaction has been rejected."
20. Catat waktu sesudah Reject (TR), lalu buka Allocation > Device Allocation
21. Ketik Search Allocation ID transaksi blok TC-261 (atribut #49), tekan Enter
22. Verifikasi Status transaksi `Rejected` (badge danger)
23. Verifikasi Cost transaksi tetap `$250.00`
24. Buka Wallet Balance kantong PT Global Distribusi
25. Verifikasi Reserved $0.00 (Release)
26. Verifikasi saldo tetap $20,000.00
27. Buka modal Allocation Log transaksi
28. Verifikasi entri `Allocation rejected by [PIC]` dengan Description `Rejection Reason: Stok belum siap`
29. Tutup modal
30. Verifikasi Last Updated transaksi pada List sama dengan TR dengan toleransi satu menit

### Approve diulang oleh aktor yang sama (TC-AC-ACHA-264)

31. Siapkan transaksi Waiting for Approval (atribut #49) dan kantong PT Global Distribusi saldo $20,000.00 Reserved $250.00 lewat fixture
32. Buka Approvals > Device Allocation > Active Tab pada sesi UI TC_DIST
33. Verifikasi transaksi tampil sebagai Waiting for Approval
34. Catat jumlah notifikasi pembuat MB_ON (M0) lewat fixture
35. Pelaku pertama (sesi API TC_DIST) menyetujui transaksi hingga status Completed tersimpan
36. Tunggu aksi selesai (status Completed terbaca lewat fixture)
37. Verifikasi jumlah notifikasi pembuat MB_ON sama dengan M0 + 1 (notifikasi dari persetujuan pelaku pertama sudah diterima; nilainya dicatat sebagai M1)
38. Catat jumlah entri `Allocation approved` pada Allocation Log transaksi (A1) lewat fixture
39. Pada halaman Approvals yang sudah terbuka (belum dimuat ulang), klik `[Approve]` pada transaksi yang sama, lalu konfirmasi pada dialog
40. Verifikasi toast sukses "Success, transaction has been approved."
41. Verifikasi Status transaksi tetap `Completed`
42. Verifikasi saldo kantong PT Global Distribusi $19,750.00 (Capture tidak dilakukan lagi)
43. Verifikasi jumlah entri `Allocation approved` sama dengan A1 (tidak ada entri kedua)
44. Tunggu 5 detik tanpa memuat ulang halaman
45. Verifikasi jumlah notifikasi pembuat MB_ON sama dengan M1 (tidak ada notifikasi baru)

### Reject diulang oleh aktor yang sama (TC-AC-ACHA-265)

46. Siapkan transaksi Waiting for Approval (atribut #49) dan kantong PT Global Distribusi saldo $20,000.00 Reserved $250.00 lewat fixture
47. Buka Approvals > Device Allocation > Active Tab pada sesi UI TC_DIST
48. Verifikasi transaksi tampil sebagai Waiting for Approval
49. Pelaku pertama (sesi API TC_DIST) menolak transaksi dengan Rejection Reason `Stok belum siap` hingga status Rejected tersimpan
50. Tunggu aksi selesai (status Rejected terbaca lewat fixture)
51. Catat jumlah entri `Allocation rejected` pada Allocation Log transaksi (J1) dan saldo serta Reserved kantong PT Global Distribusi (S1, R1) lewat fixture
52. Pada halaman Approvals yang sudah terbuka (belum dimuat ulang), isi Rejection Reason `Stok belum siap` pada transaksi yang sama, klik `[Reject]`, lalu konfirmasi pada dialog
53. Verifikasi toast sukses "Success, transaction has been rejected."
54. Verifikasi Status transaksi tetap `Rejected`
55. Verifikasi saldo kantong PT Global Distribusi sama dengan S1 (Release tidak dilakukan lagi)
56. Verifikasi Reserved kantong PT Global Distribusi sama dengan R1
57. Verifikasi jumlah entri `Allocation rejected` sama dengan J1 (tidak ada entri kedua)

### Menu row action pembuat setelah Approve dan Reject (TC-AC-ACHA-256 butir e, TC-AC-ACHA-261 butir e)

58. Ganti akun ke MB_ON: Logout, login dengan `Spectra.env.AC_DA_MB_ON_PASSWORD`, buka Allocation > Device Allocation
59. Ketik Search Allocation ID transaksi yang disetujui (blok TC-256), tekan Enter
60. Buka menu row action `⋯` pada transaksi yang disetujui (TC-256)
61. Verifikasi menu hanya memuat `Allocation Log`
62. Verifikasi `Edit`, `Cancel Allocation`, dan `Resubmit` tidak tampil
63. Tutup menu dengan Esc
64. Ganti isi kotak search dengan Allocation ID transaksi yang ditolak (blok TC-261), tekan Enter
65. Buka menu row action `⋯` pada transaksi yang ditolak (TC-261)
66. Verifikasi menu hanya memuat `Allocation Log`
67. Verifikasi `Resubmit` tidak tersedia pada status Rejected
68. Tutup menu dengan Esc

### Group Manager pada group target sebagai approver (TC-AC-ACHA-259)

69. Ganti akun ke GM_DIST: Logout, login dengan `Spectra.env.AC_DA_GM_DIST_PASSWORD`
70. Siapkan transaksi Waiting for Approval (atribut #49) dan kantong PT Global Distribusi saldo $20,000.00 Reserved $250.00 lewat fixture
71. Buka Approvals > Device Allocation > Active Tab, buka transaksi itu
72. Klik `[Approve]`, lalu konfirmasi pada dialog
73. Verifikasi toast sukses "Success, transaction has been approved."
74. Verifikasi Status transaksi `Completed` (dibaca lewat fixture)

### Additional Approver sebagai approver (TC-AC-ACHA-260)

75. Ganti akun ke AA_DIST: Logout, login dengan `Spectra.env.AC_DA_ADD_APPROVER_PASSWORD`
76. Siapkan transaksi Waiting for Approval (atribut #49) dan kantong PT Global Distribusi saldo $20,000.00 Reserved $250.00 lewat fixture
77. Buka Approvals > Device Allocation > Active Tab, buka transaksi itu
78. Klik `[Approve]`, lalu konfirmasi pada dialog
79. Verifikasi toast sukses "Success, transaction has been approved."
80. Verifikasi Status transaksi `Completed` (dibaca lewat fixture)

### Approve transaksi Principal tanpa wallet (TC-AC-ACHA-257)

81. Ganti akun ke TC_PRIN: Logout, login dengan `Spectra.env.AC_DA_TC_PRIN_PASSWORD`
82. Siapkan transaksi Waiting for Approval (atribut #51); catat kuota Handheld Reader Long Range Client PT Manufaktur Unggul (K0) lewat fixture
83. Buka Approvals > Device Allocation > Active Tab, buka transaksi itu
84. Klik `[Approve]`, lalu konfirmasi pada dialog
85. Verifikasi toast sukses "Success, transaction has been approved."
86. Buka Allocation > Device Allocation
87. Ketik Search Allocation ID transaksi blok TC-257 (atribut #51), tekan Enter
88. Verifikasi Status transaksi `Completed`
89. Verifikasi tidak ada transaksi Capture pada wallet untuk transaksi ini (Principal tanpa wallet), dibaca lewat fixture
90. Verifikasi kuota Handheld Reader Long Range Client PT Manufaktur Unggul bertambah 10 dari K0 (dibaca lewat fixture)

### Approve dan Reject transaksi Partner, kantong terpilih (TC-AC-ACHA-258, TC-AC-ACHA-262)

91. Ganti akun ke TC_P2: Logout, login dengan `Spectra.env.AC_DA_TC_P2_PASSWORD`
92. Siapkan transaksi Waiting for Approval (atribut #50), kantong A saldo $1,000.00 Reserved $60.00, kantong B saldo $3,000.00 Reserved $0.00 lewat fixture; catat saldo dan Reserved kantong B (SB0, RB0)
93. Buka Approvals > Device Allocation > Active Tab, buka transaksi itu
94. Klik `[Approve]`, lalu konfirmasi pada dialog
95. Verifikasi toast sukses "Success, transaction has been approved."
96. Buka Wallet Balance kantong A
97. Verifikasi kantong A saldo $940.00
98. Verifikasi kantong A Reserved $0.00
99. Buka Wallet Balance kantong B
100. Verifikasi kantong B saldo sama dengan SB0 (tidak berubah)
101. Verifikasi kantong B Reserved sama dengan RB0 (tidak berubah)
102. Siapkan transaksi Waiting for Approval (atribut #50), kantong A saldo $1,000.00 Reserved $60.00 lewat fixture
103. Buka Approvals > Device Allocation > Active Tab, buka transaksi itu, isi Rejection Reason `Tidak sesuai`
104. Klik `[Reject]`, lalu konfirmasi pada dialog
105. Verifikasi toast sukses "Success, transaction has been rejected."
106. Buka Wallet Balance kantong A
107. Verifikasi kantong A Reserved $0.00
108. Verifikasi kantong A saldo tetap $1,000.00

### Approve saat Pay From tidak lagi tersedia (TC-AC-ACHA-474)

109. Siapkan transaksi Waiting for Approval (atribut #70) dan kantong B saldo $3,000.00 Reserved $48.00 lewat fixture; matikan toggle loncat ke Principal CV Karya Mandiri lewat fixture
110. Buka Approvals > Device Allocation > Active Tab, buka transaksi itu
111. Klik `[Approve]`, lalu konfirmasi pada dialog
112. Verifikasi toast sukses "Success, transaction has been approved."
113. Buka Allocation > Device Allocation
114. Ketik Search Allocation ID transaksi blok TC-474 (atribut #70), tekan Enter
115. Verifikasi Status transaksi `Completed`
116. Buka Wallet Balance kantong B
117. Verifikasi kantong B saldo $2,952.00 (Capture memakai dana yang sudah di-Reserve)
118. Verifikasi kantong B Reserved $0.00
119. Buka modal Allocation Log transaksi
120. Verifikasi entri `Allocation approved by [PIC]` tampil
121. Tutup modal

### Reject saat Pay From tidak lagi tersedia (TC-AC-ACHA-475)

122. Siapkan transaksi Waiting for Approval (atribut #70) dan kantong B saldo $3,000.00 Reserved $48.00 lewat fixture (toggle loncat ke Principal tetap mati)
123. Buka Approvals > Device Allocation > Active Tab, buka transaksi itu, isi Rejection Reason `Tidak sesuai`
124. Klik `[Reject]`, lalu konfirmasi pada dialog
125. Verifikasi toast sukses "Success, transaction has been rejected."
126. Buka Allocation > Device Allocation
127. Ketik Search Allocation ID transaksi blok TC-475 (atribut #70), tekan Enter
128. Verifikasi Status transaksi `Rejected`
129. Buka Wallet Balance kantong B
130. Verifikasi kantong B saldo $3,000.00
131. Verifikasi kantong B Reserved $0.00 (Release ke kantong B)
132. Buka modal Allocation Log transaksi
133. Verifikasi entri `Allocation rejected by [PIC]` dengan `Rejection Reason: Tidak sesuai`
134. Tutup modal
135. Pulihkan toggle loncat ke Principal CV Karya Mandiri lewat fixture

### Pembuat tidak dapat menyetujui transaksinya sendiri (TC-AC-ACHA-263)

136. Ganti akun ke MB_APR: Logout, login dengan `Spectra.env.AC_DA_MB_APR_PASSWORD`
137. Siapkan transaksi Waiting for Approval buatan MB_APR (atribut #65) dan satu transaksi Waiting for Approval buatan MB_ON (atribut #49) sebagai anchor lewat fixture
138. Buka Approvals > Device Allocation > Active Tab
139. Verifikasi subject transaksi buatan MB_ON tampil pada Active Tab
140. Verifikasi transaksi buatan MB_APR tidak muncul pada antrean Active Tab
141. Buka Allocation > Device Allocation
142. Ketik Search Allocation ID transaksi buatan MB_APR (atribut #65), tekan Enter
143. Verifikasi Status transaksi buatan MB_APR tetap `Waiting for Approval`

## Notes

- Langkah penghubung (S-03): menyiapkan seed dan state kantong lewat fixture, mencatat baseline dan waktu (LU0, TR, M0, A1, J1, S1, R1, K0, SB0, RB0), mengaktifkan kolom Cost lewat Setup Column, menutup modal dan menu, serta Step ganti akun (Logout, login) tidak punya `Verifikasi`. Pemulihan toggle loncat ke Principal dilakukan juga di hook `after`. Langkah `Tunggu 5 detik tanpa memuat ulang halaman` pada blok TC-264 juga langkah penghubung tanpa `Verifikasi` (jendela absence, lihat Prerequisites); M1 diperoleh dari `Verifikasi` jumlah notifikasi sama dengan M0 + 1 yang menjadi anchor positif asersi absence.
- Urutan TC tidak mengikuti nomor TC dan dikelompokkan per akun untuk meminimalkan ganti akun. Butir e TC-256 dan TC-261 (menu row action pembuat MB_ON) dipindah ke satu blok sesudah kedua aksi selesai agar hanya satu kali ganti akun ke MB_ON; transaksi yang dicek adalah transaksi hasil Approve dan Reject pada blok TC-256 dan TC-261.
- TC-264 dan TC-265: pelaku pertama adalah sesi API akun yang sama (TC_DIST) sebagai pemicu state (tidak memakai P-2 dan tidak ada konteks UI kedua). Halaman Approvals di sesi UI dibuka lebih dulu sehingga masih menampilkan transaksi sebagai Waiting for Approval saat `[Approve]` atau `[Reject]` ditekan kedua kalinya. TC menulis pelaku pertama "sampai toast sukses"; toast pelaku pertama tidak termasuk Expected sehingga tidak diasersi.
- Anchor absence TC-263 (bagian 8b butir 2): `Verifikasi` subject transaksi buatan MB_ON tampil pada Active Tab yang sama mendahului asersi transaksi buatan MB_APR tidak muncul. Transaksi buatan MB_ON adalah seeding minimal untuk anchor, tidak diasersi selain tampil.
- Baris target (R-16): transaksi di List ditemukan lewat Search Allocation ID yang ditangkap saat seeding sebagai langkah penghubung tanpa `Verifikasi`; langkah Search dituliskan sebagai langkah bernomor tepat sesudah tiap langkah yang membuka Allocation > Device Allocation atau login ulang ke List, dan memakai "Ganti isi kotak search dengan" bila kotak Search masih berisi (8b butir 9).
- Asersi status `Completed` pada TC-259 dan TC-260 dibaca lewat fixture karena TC tidak menyatakan surface; akun AA_DIST tidak memiliki capability Manage allocation sehingga akses ke List Device Allocation tidak dijamin.
- Alasan di atas 35 langkah: seluruh blok satu topik (efek Approve dan Reject pada modul Device Allocation) di surface Approvals yang sama; tiap blok memakai seed dan state kantong sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; ganti akun eksplisit memisahkan blok per akun (bagian 3, Pisahkan spec hanya jika ada pemisah nyata butir b). Langkah ulang Approve dan Reject sengaja ditulis per blok (bukan perulangan) karena asersi tiap blok berbeda.
- Temuan untuk QA:
  - Label tombol konfirmasi pada dialog Approve dan Reject tidak disebut di TC (hanya "konfirmasi"); spec menulis "konfirmasi pada dialog".
  - TC-257 butir b "tidak ada Capture karena Principal tanpa wallet" tidak memberi cara observasi; spec membacanya lewat fixture (disediakan tim FE/BE). Butir c (kuota Client bertambah) juga dibaca lewat fixture karena surface tidak disebut.
  - Post Condition TC-256 butir a (kuota Client bertambah 100) dan b (notifikasi pembuat), TC-258, 259, 260, 262, 474, dan 475 (Dashboard widget, Approvals History Tab, panel Stock Balance Summary, notifikasi) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-264 dan TC-265 mensyaratkan dua sesi approver yang sama; spec memodelkan sesi pertama sebagai sesi API (lihat Notes). Bila QA bermaksud dua sesi UI yang diamati keduanya, TC itu adalah kelas multi-konteks (c) dan seharusnya berada di spec multi-konteks (penempatan awal ada di spec ini).
  - TC-264 butir b "tidak ada notifikasi baru" tidak menyebut penerima; spec mengasersi notifikasi pembuat MB_ON saja.
  - TC-474 dan TC-475: TC tidak menyatakan cara "toggle loncat ke Principal dimatikan setelah transaksi dibuat" selain fixture Pre-setup #20; kontrak fixture tidak ada di TC, PRD, atau LLD (S-13).

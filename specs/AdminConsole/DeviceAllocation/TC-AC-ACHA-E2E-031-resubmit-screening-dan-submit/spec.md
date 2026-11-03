---
id: TC-AC-ACHA-E2E-031-resubmit-screening-dan-submit
title: "Resubmit: Row Action, Form Terisi dari Transaksi Canceled, Submit Berhasil, Rantai Resubmit, dan Resubmit Total Control"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-235
  - TC-AC-ACHA-236
  - TC-AC-ACHA-237
  - TC-AC-ACHA-238
  - TC-AC-ACHA-239
  - TC-AC-ACHA-240
  - TC-AC-ACHA-241
  - TC-AC-ACHA-242
  - TC-AC-ACHA-251
coverage:
  web: automated
---

# Resubmit: Row Action, Form Terisi dari Transaksi Canceled, Submit Berhasil, Rantai Resubmit, dan Resubmit Total Control

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Group Member Distributor toggle ON MB_ON (Pre-setup #32) `memberOnDistributor_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_MB_ON_PASSWORD`. Akun ganti di tengah spec: Total Control Distributor TC_DIST (Pre-setup #27) `totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_TC_DIST_PASSWORD`. Login MB_ON di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Nama env baru didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Data Pre-setup yang dibaca: Distributor PT Global Distribusi (#3), Client PT Sejahtera Logistik (#7), harga PT ABC (#14), kantong PT Global Distribusi saldo $20,000.00 (#16).
- Data seed milik spec (dibuat lewat seeding API di hook `before`; mekanisme seeding disediakan tim FE/BE; Allocation ID hasil seeding ditangkap saat runtime sebagai Dynamic Reference, tidak di-hardcode):
  - Transaksi Canceled manual milik MB_ON dengan atribut Pre-setup #52 (BLE Gateway, Quantity 50, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch lama`, Total Cost $100.00) untuk TC-237, 238, 239, 240, 242. Transaksi lama ini tetap Canceled setelah tiap Resubmit, sehingga satu transaksi dipakai berurutan.
  - Transaksi milik MB_ON berstatus Waiting for Approval (atribut #49), Completed (atribut #55), dan Rejected (atribut #54) untuk TC-236.
  - Transaksi Canceled oleh Timeout Auto-Cancel milik MB_ON dengan atribut #53 (NFC, Quantity 15, Client PT Sejahtera Logistik, Total Cost $18.00) untuk TC-241.
  - Transaksi Canceled milik TC_DIST (Pre-setup #59; atribut kategori, Quantity, dan Total Cost tidak dirinci TC) untuk TC-251.
  - Nilai literal `Batch lama` pada Notes diasersi oleh TC sehingga tidak bersuffix (pengecualian S-12 nama literal, Lampiran A butir A-6).
- Kemampuan teknis (disediakan tim FE/BE, kontrak fixture tidak tertulis di TC): fixture API Pre-setup #20 untuk mengubah harga BLE Gateway PT ABC dari $2.00 menjadi $2.20 lalu memulihkannya ke $2.00; pembacaan saldo dan Reserved kantong PT Global Distribusi; pembacaan jumlah notifikasi Notification Center TC_DIST lewat sesi API aktor (baseline).
- Kolom Cost ditampilkan lewat Setup Column pada langkah penghubung, dan ditampilkan ulang sesudah ganti akun ke TC_DIST sebelum TC-251; preferensi kolom dipulihkan hook `after` suite.
- Pemulihan dan cleanup (R-08): hook `after` memulihkan harga BLE Gateway PT ABC ke $2.00 dan seed ke 30 baris, serta membatalkan transaksi Waiting for Approval hasil Resubmit (langkah 41, 53, 61, 71, 81, dan 90) lewat fixture Pre-setup #20 (disediakan tim FE/BE). Modul tanpa Delete sehingga transaksi baru hasil Resubmit tidak dihapus; transaksi Completed hasil langkah 112 mengurangi saldo kantong PT Global Distribusi dan saldo itu dipulihkan fixture ke nilai awal.
- State global: harga BLE Gateway PT ABC diubah lalu dipulihkan (langkah penghubung dan hook `after`); suite berjalan serial (`parallel: false`).
- Hook suite: flag Guided Tooltip, sesi API aktor, fixture API Pre-setup #20, pemulihan preferensi Setup Column, dan seed 30 baris dinyatakan di `suite.md`. Hook `after` memulihkan harga dan seed lewat fixture Pre-setup #20 (Lampiran A butir A-6).

## Test Steps

### Screening menu row action (TC-AC-ACHA-235, TC-AC-ACHA-236)

1. Ketik Search Allocation ID transaksi Canceled milik MB_ON (seed Pre-setup #52), tekan Enter
2. Buka menu row action `⋯` pada transaksi Canceled milik MB_ON
3. Verifikasi menu memuat `Allocation Log` (severity dark)
4. Verifikasi menu memuat `Resubmit` (ikon `RefreshLine`, severity dark)
5. Verifikasi `Edit` dan `Cancel Allocation` tidak tampil
6. Tutup menu dengan Esc
7. Ganti isi kotak search dengan Allocation ID transaksi Waiting for Approval milik MB_ON, tekan Enter
8. Buka menu row action `⋯` pada transaksi Waiting for Approval milik MB_ON
9. Verifikasi menu memuat `Allocation Log`
10. Verifikasi menu tidak memuat `Resubmit`
11. Tutup menu dengan Esc
12. Ganti isi kotak search dengan Allocation ID transaksi Completed milik MB_ON, tekan Enter
13. Buka menu row action `⋯` pada transaksi Completed milik MB_ON
14. Verifikasi menu memuat `Allocation Log`
15. Verifikasi menu tidak memuat `Resubmit`
16. Tutup menu dengan Esc
17. Ganti isi kotak search dengan Allocation ID transaksi Rejected milik MB_ON, tekan Enter
18. Buka menu row action `⋯` pada transaksi Rejected milik MB_ON
19. Verifikasi menu memuat `Allocation Log`
20. Verifikasi menu tidak memuat `Resubmit` (Resubmit hanya untuk status Canceled)
21. Tutup menu dengan Esc

### Form Resubmit terisi (TC-AC-ACHA-237)

22. Ganti isi kotak search dengan Allocation ID transaksi Canceled milik MB_ON (seed Pre-setup #52), tekan Enter
23. Klik `Resubmit` pada transaksi Canceled milik MB_ON
24. Verifikasi Header form: judul `Allocate Device` dan ikon close `[×]` tampil
25. Verifikasi Category `BLE Gateway`, Client `PT Sejahtera Logistik`, Quantity `50`, dan Notes `Batch lama` terisi dari transaksi lama
26. Verifikasi Category, Client, Quantity, dan Notes dapat diubah
27. Verifikasi Pay From `PT ABC (Principal)` pre-filled
28. Verifikasi Pay From disabled
29. Verifikasi Preview dihitung dari harga terkini: biaya $100.00 (50 × $2.00)
30. Verifikasi Footer memuat `[Clear Field]` dan `[Submit]`
31. Verifikasi tidak ada `[Cancel]` pada Footer
32. Verifikasi tidak ada checkbox "Stay on this form after submitting"
33. Verifikasi Status dan data approval transaksi lama tidak terisi pada form
34. Tutup form dengan `[×]`

### Resubmit dari transaksi Timeout Auto-Cancel (TC-AC-ACHA-241)

35. Tampilkan kolom Cost lewat Setup Column, klik `[Save]`
36. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
37. Catat total baris transaksi pada List (B)
38. Ketik Search Allocation ID transaksi Canceled oleh Timeout Auto-Cancel milik MB_ON (seed Pre-setup #53), tekan Enter
39. Klik `Resubmit` pada transaksi Canceled oleh Timeout Auto-Cancel milik MB_ON
40. Verifikasi form terisi Category `NFC` dan Quantity `15`
41. Klik `[Submit]`
42. Verifikasi toast sukses "Success, device allocation has been resubmitted."
43. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
44. Verifikasi transaksi baru dibuat dan tampil pada List: total baris pada List bertambah satu dari B
45. Catat total baris transaksi pada List (B1)
46. Ketik Search Allocation ID transaksi Canceled milik MB_ON (seed Pre-setup #52), tekan Enter

### Resubmit memungkinkan semua field diubah (TC-AC-ACHA-242)

47. Klik `Resubmit` pada transaksi Canceled milik MB_ON (BLE Gateway, Quantity 50)
48. Ubah Category menjadi `TAG - RFID`
49. Ubah Type menjadi `User TAG`
50. Ubah Quantity menjadi `30`
51. Ubah Notes menjadi `Ganti jenis`
52. Verifikasi semua field dapat diubah: Category `RFID`, Type `User TAG`, Quantity `30`, Notes `Ganti jenis` terisi pada form
53. Klik `[Submit]`
54. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
55. Verifikasi total baris pada List bertambah satu dari B1 (langkah 45)
56. Verifikasi transaksi baru pada baris teratas List: Category `RFID`, Type `User TAG`, Quantity `30`, Cost `$90.00`
57. Ketik Search Allocation ID transaksi lama (seed Pre-setup #52), tekan Enter
58. Verifikasi transaksi lama tetap Category `BLE Gateway`, Quantity `50`, Status `Canceled`

### Resubmitted From pada log (TC-AC-ACHA-239)

59. Buka modal Allocation Log transaksi lama, catat jumlah entri log (L), lalu tutup modal
60. Klik `Resubmit` pada transaksi Canceled milik MB_ON
61. Klik `[Submit]`
62. Tunggu aksi selesai (form Resubmit tertutup)
63. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
64. Buka modal Allocation Log transaksi baru (baris teratas List sesudah Search dibersihkan)
65. Verifikasi entri `Allocation created by [PIC]` memuat `Category: BLE Gateway`, `Quantity: 50`, `From: PT Global Distribusi`, `Notes: Batch lama`, `Cost`, dan `Resubmitted From: [Allocation ID transaksi lama]`
66. Tutup modal
67. Ketik Search Allocation ID transaksi lama (seed Pre-setup #52), tekan Enter
68. Buka modal Allocation Log transaksi lama
69. Verifikasi jumlah entri log transaksi lama sama dengan L (tidak ada entri baru)
70. Tutup modal

### Resubmit tanpa batas pengulangan dan rantai (TC-AC-ACHA-240)

71. Klik `Resubmit` pada transaksi Canceled milik MB_ON, lalu klik `[Submit]`
72. Tunggu aksi selesai (form Resubmit tertutup)
73. Buka menu row action `⋯` transaksi lama
74. Verifikasi `Resubmit` tetap tersedia pada transaksi lama setelah dipakai
75. Tutup menu dengan Esc
76. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
77. Buka menu row action `⋯` transaksi baru hasil Resubmit (baris teratas List), klik `Cancel Allocation`, lalu klik `[Cancel Allocation]` pada dialog
78. Buka menu row action `⋯` transaksi baru yang dibatalkan itu
79. Verifikasi `Resubmit` tersedia pada transaksi baru yang dibatalkan
80. Catat total baris transaksi pada List (B)
81. Klik `Resubmit` pada transaksi baru yang dibatalkan itu, lalu klik `[Submit]`
82. Verifikasi transaksi ketiga tampil pada List: total baris pada List bertambah satu dari B
83. Ketik Search Allocation ID transaksi lama (seed Pre-setup #52), tekan Enter
84. Verifikasi transaksi lama tetap Status `Canceled` dengan Quantity `50`

### Submit Resubmit dengan snapshot harga terkini dan notifikasi (TC-AC-ACHA-238)

85. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
86. Ubah harga BLE Gateway PT ABC dari $2.00 menjadi $2.20 lewat fixture API
87. Catat Reserved kantong PT Global Distribusi (R) lewat fixture API, jumlah notifikasi berjudul "Waiting for your approval" milik TC_DIST (N) lewat sesi API TC_DIST, dan total baris transaksi pada List (B)
88. Ketik Search Allocation ID transaksi lama (seed Pre-setup #52), tekan Enter
89. Klik `Resubmit` pada transaksi Canceled milik MB_ON
90. Klik `[Submit]` tanpa mengubah isian
91. Verifikasi toast sukses "Success, device allocation has been resubmitted."
92. Verifikasi form Resubmit tertutup
93. Verifikasi form tidak terisi ulang (tanpa pre-fill ulang)
94. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
95. Verifikasi transaksi baru pada baris teratas List: Status `Waiting for Approval`, Quantity `50`, Cost `$110.00` (50 × $2.20)
96. Ketik Search Allocation ID transaksi lama (seed Pre-setup #52), tekan Enter
97. Verifikasi transaksi lama tetap Status `Canceled` dengan Cost `$100.00`
98. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
99. Verifikasi total baris transaksi pada List bertambah satu dari B (Submit tanpa perubahan tetap membuat transaksi baru, tidak ada skenario no-op)
100. Pulihkan harga BLE Gateway PT ABC menjadi $2.00 lewat fixture API
101. Buka Wallet Balance kantong PT Global Distribusi
102. Verifikasi Reserved bertambah $110.00 dari R
103. Buka Approvals > Device Allocation > Active Tab
104. Verifikasi subject transaksi baru tampil pada Active Tab
105. Ganti akun ke TC_DIST: Logout, login dengan `Spectra.env.AC_DA_TC_DIST_PASSWORD`, buka Notification Center
106. Verifikasi jumlah notifikasi `actionable` berjudul "Waiting for your approval" sama dengan N + 1

### Resubmit oleh Total Control langsung Completed (TC-AC-ACHA-251)

107. Buka Allocation > Device Allocation
108. Buka Setup Column, tampilkan kolom Cost, klik `[Save]`
109. Catat saldo dan Reserved kantong PT Global Distribusi (S0, R0) lewat fixture API dan total baris transaksi pada List (B3)
110. Ketik Search Allocation ID transaksi Canceled milik TC_DIST (seed Pre-setup #59), tekan Enter
111. Klik `Resubmit` pada transaksi Canceled milik TC_DIST
112. Klik `[Submit]`
113. Verifikasi toast sukses "Success, device allocation has been resubmitted."
114. Verifikasi form Resubmit tertutup
115. Verifikasi form tidak terisi ulang (tanpa pre-fill ulang)
116. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
117. Verifikasi total baris pada List bertambah satu dari B3 (langkah 109)
118. Verifikasi transaksi baru pada baris teratas List langsung Status `Completed`
119. Buka Wallet Balance kantong PT Global Distribusi
120. Verifikasi saldo berkurang sebesar Cost transaksi baru dari S0 (Capture langsung)
121. Verifikasi Reserved sama dengan R0 (tanpa Reserve)

## Notes

- Langkah penghubung (S-03): Search, pembersihan Search, menunggu aksi selesai (8b butir 8), menutup menu dengan Esc, menutup modal Allocation Log, menutup form dengan `[×]`, mengaktifkan kolom Cost lewat Setup Column (juga sesudah ganti akun ke TC_DIST pada langkah 108, karena cakupan preferensi kolom lintas akun tidak diasumsikan), memulihkan harga BLE Gateway, mencatat baseline, dan ganti akun TC_DIST (Logout, login) tidak punya `Verifikasi`. Verifikasi `Allocation Log` pada menu Waiting, Completed, dan Rejected dipakai sebagai anchor positif untuk asersi absence `Resubmit` (bagian 8b butir 2).
- Baris target (R-16): transaksi seed ditemukan di List lewat Search Allocation ID yang ditangkap saat seeding (Dynamic Reference). Langkah Search ("Ketik Search" atau "Ganti isi kotak search dengan") ditulis sebagai langkah penghubung tanpa `Verifikasi` tepat sebelum langkah yang memakai baris seed tertentu; Search dibersihkan (klik `(←)`, lalu muat ulang halaman (F5)) sebelum langkah yang membaca total baris atau mengenali transaksi baru. Total baris transaksi dicatat dalam keadaan Search kosong sebelum langkah yang membuat transaksi baru (B pada langkah 37, 80, dan 87, B1 pada langkah 45, B3 pada langkah 109) sehingga asersi "transaksi baru" memakai selisih dari baseline (S-12). Transaksi baru dikenali sebagai baris teratas List sesudah Search dibersihkan (urutan default Last Updated menurun, spec 038, TC-AC-ACHA-300) dan didukung selisih total baris; tidak ada geser jam dan tiap Submit selesai (langkah "Tunggu aksi selesai") sebelum List dibaca.
- Menutup form `[×]` pada TC-237 aman tanpa dialog karena nilai form identik dengan nilai pre-fill (TC-247).
- Urutan TC di dalam spec tidak mengikuti nomor TC: TC-241 dan TC-242 dikerjakan sebelum TC-238 karena TC-238 mengubah harga BLE Gateway; Resubmit memakai transaksi lama yang sama berurutan sehingga transaksi baru dari tiap blok tetap ada (cleanup di hook `after`). Aksi TC-251 oleh TC_DIST ditaruh paling akhir untuk meminimalkan ganti akun; langkah "Buka Notification Center sebagai Total Control Distributor" TC-238 dikerjakan pada ganti akun yang sama.
- Alasan di atas 35 langkah: seluruh blok satu topik (Resubmit) dan akun sama, tiap blok memakai transaksi seed sendiri dan bermakna walau blok lain gagal; hanya blok TC-251 memakai akun lain lewat Step ganti akun eksplisit.
- Pengecualian P-1 tidak dipakai. Tidak ada asersi absence log dalam spec ini.
- Temuan untuk QA:
  - TC-237 Expected b "Preview dihitung dari harga terkini" tanpa nilai; spec mengasersi $100.00 (50 × $2.00 harga Pre-setup #14).
  - TC-240 langkah 4 ("Batalkan transaksi baru") tidak menyebut label dialog konfirmasi; spec memakai `Cancel Allocation` row action dan tombol `[Cancel Allocation]` seperti TC pembatalan lain.
  - TC-238 Expected f menyebut notifikasi untuk Total Control Distributor tanpa menentukan Body (PRD §9.7); spec hanya mengasersi Title dan selisih jumlah terhadap baseline.
  - TC-251: atribut seed Pre-setup #59 (Category, Quantity, Cost) tidak dirinci; spec mengasersi saldo berkurang sebesar Cost transaksi baru yang tampil pada List.
  - Post Condition TC-238, 239, 240, 241, dan 251 (Dashboard widget, notifikasi ke approver pool, kuota Client, panel Stock Balance Summary) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Kontrak fixture Pre-setup #20 (ubah harga, baca saldo dan Reserved) tidak ada di TC, PRD, atau LLD; ditulis "disediakan tim FE/BE" (S-13).

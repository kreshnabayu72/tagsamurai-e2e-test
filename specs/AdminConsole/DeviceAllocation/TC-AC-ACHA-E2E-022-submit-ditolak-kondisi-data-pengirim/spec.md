---
id: TC-AC-ACHA-E2E-022-submit-ditolak-kondisi-data-pengirim
title: "Submit Allocate Device Ditolak Server karena Kondisi Data Pengirim: Lebih dari Satu Group, Tanpa Group, dan Tanpa Kantong Sumber"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHA-157
  - TC-AC-ACHA-158
  - TC-AC-ACHA-159
  - TC-AC-ACHA-160
  - TC-AC-ACHA-161
  - TC-AC-ACHA-162
  - TC-AC-ACHA-487
  - TC-AC-ACHA-488
coverage:
  web: automated
---

# Submit Allocate Device Ditolak Server karena Kondisi Data Pengirim: Lebih dari Satu Group, Tanpa Group, dan Tanpa Kantong Sumber

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji (urutan pemakaian dalam spec):

| Kode | Role | Pre-setup | Email | Env var password |
|---|---|---|---|---|
| A-02 | Total Control Distributor `PT Global Distribusi` (Hendra Wibowo) | #27 | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| A-08 | Group Member Distributor toggle ON Group Jakarta (Budi Santoso) | #32 | `memberOnDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_MB_ON_PASSWORD` |
| A-06 | Group Manager Distributor Group Jakarta toggle ON (Agus Hartono) | #29 | `groupManagerDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_GM_DIST_PASSWORD` |
| A-05 | Group Member Distributor toggle OFF (Citra Anggraini) | #33 | `memberOffDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_MB_OFF_PASSWORD` |
| A-11 | Group Member Partner `CV Mitra Solusi` toggle ON (Andi Wijaya) | #44 | `memberOnPartner1_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_MB_P1_PASSWORD` |

- Login A-02 di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal #21, `AC_TC_PASSWORD`). Ganti akun dengan langkah logout dan login eksplisit. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example` (didaftarkan tahap script); password tidak ditulis di spec.
- Data Pre-setup: Client #7 `PT Sejahtera Logistik` dan #8 `PT Retail Makmur`; kantong #16 PT Global Distribusi saldo $20,000.00 (Reserved awal $0.00) dan #17 CV Mitra Solusi; group Jakarta dan Surabaya (#3); harga #14 dan #15.
- Kondisi data per TC, disetel lewat fixture API Pre-setup #20 (disediakan tim FE/BE tanpa endpoint karangan) pada langkah yang menyebutnya: (1) entitas PT Global Distribusi berada di dua group sekaligus (Group Jakarta dan Group Surabaya) untuk TC-157, TC-158, TC-487; (2) entitas PT Global Distribusi tidak berada di group manapun untuk TC-159, TC-160, TC-488; (3) entitas PT Global Distribusi tidak punya kantong sumber untuk TC-161; (4) entitas CV Mitra Solusi tidak punya kantong sumber untuk TC-162. Hook `before` memastikan PT Global Distribusi berada di Group Jakarta dan kantong sumber Pre-setup #16 dan #17 tersedia dengan saldo awal; hook `after` memulihkan penempatan group dan kantong.
- Kemampuan baca state BE (disediakan tim FE/BE): jumlah transaksi pengirim, Reserved dan saldo kantong, dan jumlah Wallet Transaction; dicatat sebagai baseline sebelum tiap `[Submit]`.
- Tidak ada data yang dibuat spec ini (semua `[Submit]` ditolak server).
- Hook suite (dinyatakan sekali di `suite.md`): flag Guided Tooltip halaman Device Allocation disetel true untuk akun aktor dan dipulihkan di `after`, sesi API aktor, fixture API Pre-setup #20, pemulihan preferensi Setup Column.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah penempatan group dan kantong sumber entitas (state bersama).

## Test Steps

### Akun A-02 Total Control Distributor: lebih dari satu group, tanpa group, tanpa kantong sumber (TC-AC-ACHA-157, TC-AC-ACHA-159, TC-AC-ACHA-161)

1. Setel entitas PT Global Distribusi berada di dua group sekaligus (Group Jakarta dan Group Surabaya) lewat fixture API Pre-setup #20
2. Catat baseline jumlah transaksi pengirim, Reserved dan saldo kantong, dan jumlah Wallet Transaction lewat kemampuan baca state BE
3. Klik `[+ Allocation]`
4. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, isi Quantity `5`
5. Klik `[Submit]`
6. Verifikasi server menolak Submit: toast error aksi "Error, failed to create device allocation." (jalur langsung)
7. Verifikasi tidak ada transaksi baru (jumlah transaksi sama dengan baseline)
8. Verifikasi tidak ada Reserve (Reserved sama dengan baseline)
9. Verifikasi saldo kantong tetap $20,000.00
10. Verifikasi tidak ada Capture (jumlah Wallet Transaction sama dengan baseline)
11. Verifikasi form tetap terbuka
12. Verifikasi input dipertahankan: Category, Client, dan Quantity `5` tetap terisi
13. Klik `[×]`
14. Verifikasi dialog Unsaved Changes tampil
15. Klik `[Leave]`
16. Setel entitas PT Global Distribusi tidak berada di group manapun lewat fixture API Pre-setup #20
17. Catat baseline jumlah transaksi pengirim, Reserved dan saldo kantong, dan jumlah Wallet Transaction lewat kemampuan baca state BE
18. Klik `[+ Allocation]`
19. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, isi Quantity `5`
20. Klik `[Submit]`
21. Verifikasi server menolak Submit: toast error aksi "Error, failed to create device allocation." (jalur langsung)
22. Verifikasi tidak ada transaksi baru (jumlah transaksi sama dengan baseline)
23. Verifikasi tidak ada Reserve (Reserved sama dengan baseline)
24. Verifikasi saldo kantong tetap $20,000.00
25. Verifikasi tidak ada Capture (jumlah Wallet Transaction sama dengan baseline)
26. Verifikasi form tetap terbuka
27. Verifikasi input dipertahankan: Category, Client, dan Quantity `5` tetap terisi
28. Klik `[×]`
29. Verifikasi dialog Unsaved Changes tampil
30. Klik `[Leave]`
31. Pulihkan penempatan PT Global Distribusi ke Group Jakarta, lalu setel entitas PT Global Distribusi tidak punya kantong sumber lewat fixture API Pre-setup #20
32. Catat baseline jumlah transaksi pengirim, Reserved dan saldo kantong, dan jumlah Wallet Transaction lewat kemampuan baca state BE
33. Klik `[+ Allocation]` dan amati field Pay From
34. Verifikasi field Pay From tampil disabled tanpa nilai
35. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, isi Quantity `5`
36. Klik `[Submit]`
37. Verifikasi server menolak Submit: tidak ada transaksi baru (jumlah transaksi sama dengan baseline)
38. Verifikasi tidak ada Reserve (Reserved sama dengan baseline)
39. Verifikasi saldo kantong tidak berubah dari baseline
40. Verifikasi toast error aksi "Error, failed to create device allocation." (jalur langsung)
41. Verifikasi form tetap terbuka
42. Verifikasi input dipertahankan: Category, Client, dan Quantity `5` tetap terisi
43. Klik `[×]`
44. Verifikasi dialog Unsaved Changes tampil
45. Klik `[Leave]`
46. Pulihkan kantong sumber PT Global Distribusi lewat fixture API Pre-setup #20

### Akun A-08 Group Member toggle ON: lebih dari satu group dan tanpa group (TC-AC-ACHA-158, TC-AC-ACHA-160)

47. Logout, lalu login sebagai A-08 (`Budi Santoso`), buka Allocation > Device Allocation
48. Setel entitas PT Global Distribusi berada di dua group sekaligus (Group Jakarta dan Group Surabaya) lewat fixture API Pre-setup #20
49. Catat baseline jumlah transaksi pengirim, Reserved dan saldo kantong, dan jumlah Wallet Transaction lewat kemampuan baca state BE
50. Klik `[+ Allocation]`
51. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, isi Quantity `5`
52. Klik `[Submit]`
53. Verifikasi server menolak Submit: toast error aksi "Error, failed to submit device allocation." (jalur persetujuan)
54. Verifikasi tidak ada transaksi baru (jumlah transaksi sama dengan baseline)
55. Verifikasi tidak ada Reserve (Reserved sama dengan baseline)
56. Verifikasi saldo kantong tetap $20,000.00
57. Verifikasi tidak ada Capture (jumlah Wallet Transaction sama dengan baseline)
58. Verifikasi form tetap terbuka
59. Verifikasi input dipertahankan: Category, Client, dan Quantity `5` tetap terisi
60. Klik `[×]`
61. Verifikasi dialog Unsaved Changes tampil
62. Klik `[Leave]`
63. Setel entitas PT Global Distribusi tidak berada di group manapun lewat fixture API Pre-setup #20
64. Catat baseline jumlah transaksi pengirim, Reserved dan saldo kantong, dan jumlah Wallet Transaction lewat kemampuan baca state BE
65. Klik `[+ Allocation]`
66. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, isi Quantity `5`
67. Klik `[Submit]`
68. Verifikasi server menolak Submit: toast error aksi "Error, failed to submit device allocation." (jalur persetujuan)
69. Verifikasi tidak ada transaksi baru (jumlah transaksi sama dengan baseline)
70. Verifikasi tidak ada Reserve (Reserved sama dengan baseline)
71. Verifikasi saldo kantong tetap $20,000.00
72. Verifikasi tidak ada Capture (jumlah Wallet Transaction sama dengan baseline)
73. Verifikasi form tetap terbuka
74. Verifikasi input dipertahankan: Category, Client, dan Quantity `5` tetap terisi
75. Klik `[×]`
76. Verifikasi dialog Unsaved Changes tampil
77. Klik `[Leave]`

### Akun A-06 Group Manager: lebih dari satu group tanpa auto-bypass (TC-AC-ACHA-487)

78. Logout, lalu login sebagai A-06 (`Agus Hartono`), buka Allocation > Device Allocation
79. Setel entitas PT Global Distribusi berada di dua group sekaligus (Group Jakarta dan Group Surabaya) lewat fixture API Pre-setup #20
80. Catat baseline jumlah transaksi pengirim, Reserved dan saldo kantong, dan jumlah Wallet Transaction lewat kemampuan baca state BE
81. Klik `[+ Allocation]`
82. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, isi Quantity `5`
83. Klik `[Submit]`
84. Verifikasi Group Manager tidak memperoleh auto-bypass karena group target tidak dapat ditentukan: server menolak Submit tanpa transaksi baru (jumlah transaksi sama dengan baseline)
85. Verifikasi tidak ada Reserve (Reserved sama dengan baseline)
86. Verifikasi saldo kantong tetap $20,000.00
87. Verifikasi tidak ada Capture (jumlah Wallet Transaction sama dengan baseline)
88. Verifikasi toast error aksi "Error, failed to submit device allocation." (jalur persetujuan, bukan "Error, failed to create device allocation.")
89. Verifikasi form tetap terbuka
90. Verifikasi input dipertahankan: Category, Client, dan Quantity `5` tetap terisi
91. Klik `[×]`
92. Verifikasi dialog Unsaved Changes tampil
93. Klik `[Leave]`

### Akun A-05 Group Member toggle OFF: tanpa group (TC-AC-ACHA-488)

94. Logout, lalu login sebagai A-05 (`Citra Anggraini`), buka Allocation > Device Allocation
95. Setel entitas PT Global Distribusi tidak berada di group manapun lewat fixture API Pre-setup #20
96. Catat baseline jumlah transaksi pengirim, Reserved dan saldo kantong, dan jumlah Wallet Transaction lewat kemampuan baca state BE
97. Klik `[+ Allocation]`
98. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, isi Quantity `5`
99. Klik `[Submit]`
100. Verifikasi toggle OFF tidak diterapkan karena group target tidak dapat ditentukan: server menolak Submit tanpa transaksi baru (jumlah transaksi sama dengan baseline)
101. Verifikasi tidak ada Reserve (Reserved sama dengan baseline)
102. Verifikasi saldo kantong tetap $20,000.00
103. Verifikasi tidak ada Capture (jumlah Wallet Transaction sama dengan baseline)
104. Verifikasi toast error aksi "Error, failed to submit device allocation." (jalur persetujuan, bukan "Error, failed to create device allocation.")
105. Verifikasi form tetap terbuka
106. Verifikasi input dipertahankan: Category, Client, dan Quantity `5` tetap terisi
107. Klik `[×]`
108. Verifikasi dialog Unsaved Changes tampil
109. Klik `[Leave]`
110. Pulihkan penempatan PT Global Distribusi ke Group Jakarta lewat fixture API Pre-setup #20

### Akun A-11 Group Member Partner: tanpa kantong sumber (TC-AC-ACHA-162)

111. Logout, lalu login sebagai A-11 (`Andi Wijaya`), buka Allocation > Device Allocation
112. Setel entitas CV Mitra Solusi tidak punya kantong sumber lewat fixture API Pre-setup #20
113. Catat baseline jumlah transaksi pengirim, Reserved dan saldo kantong, dan jumlah Wallet Transaction lewat kemampuan baca state BE
114. Klik `[+ Allocation]` dan amati field Pay From
115. Verifikasi field Pay From tampil disabled tanpa nilai
116. Pilih Category `Hardware - BLE Gateway`, Client `PT Retail Makmur`, isi Quantity `5`
117. Klik `[Submit]`
118. Verifikasi server menolak Submit: tidak ada transaksi baru (jumlah transaksi sama dengan baseline)
119. Verifikasi tidak ada Reserve (Reserved sama dengan baseline)
120. Verifikasi saldo kantong tidak berubah dari baseline
121. Verifikasi toast error aksi "Error, failed to submit device allocation." (jalur persetujuan)
122. Verifikasi form tetap terbuka
123. Verifikasi input dipertahankan: Category, Client, dan Quantity `5` tetap terisi
124. Klik `[×]`
125. Verifikasi dialog Unsaved Changes tampil
126. Klik `[Leave]`
127. Pulihkan kantong sumber CV Mitra Solusi lewat fixture API Pre-setup #20

## Notes

- Mode FE+BE; sumber `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Subjudul `###` memetakan langkah ke id TC granular. Kasus ini adalah blokir karena kondisi data (prinsip 12) dan dipisah dari alur normal; semua `[Submit]` ditolak server sehingga spec tidak membuat data.
- Alasan spec di atas sekitar 35 langkah: semua blok satu topik (penolakan server karena kondisi data pengirim) dan satu kelas; delapan TC berstruktur identik (disalin per TC karena kondisi data, akun, dan teks toast berbeda) dan tiap blok akun serta kondisi berdiri sendiri dengan langkah ganti akun eksplisit sehingga kegagalan satu blok tidak menghilangkan makna blok lain (konvensi bagian 3, pemisah (b)). Asersi `Verifikasi` yang diulang per TC mengikuti S-01.
- Penyimpangan urutan (S-10): TC dikelompokkan menurut akun (A-02, A-08, A-06, A-05, A-11) dengan kondisi data disetel ulang di antara TC untuk meminimalkan ganti akun; urutan TC mengikuti pengelompokan ini bukan nomor TC.
- Langkah penghubung (S-03): penyetelan dan pemulihan fixture, pencatatan baseline, logout dan login ganti akun, dan penutupan form dirty lewat `[×]`, dialog Unsaved Changes, `[Leave]` (S-08).
- Asersi gabungan sesuai S-03: pada TC-487 dan TC-488 klausa "Group Manager tidak memperoleh auto-bypass" dan "toggle OFF tidak diterapkan" adalah kesimpulan dari penolakan server dan tidak teramati terpisah; diasersi bersama penolakan tanpa transaksi baru.
- Pengecualian S-12 nama literal: nama entitas dan Client Pre-setup literal (sudah ada di environment).
- Temuan untuk QA:
  - TC-161 dan TC-162 Expected b ("saldo kantong tidak berubah") tidak menyebut kantong yang dimaksud karena entitas tidak punya kantong sumber; spec mengasersi lewat baseline kemampuan baca state BE.
  - Penempatan entitas ke group (satu, lebih dari satu, tanpa group) dan penghapusan kantong sumber hanya disebut "lewat Pre-setup #20"; kontrak fixture tidak tertulis di TC, PRD, atau LLD sehingga ditulis "disediakan tim FE/BE".
  - TC-157 dan TC-487 hanya berbeda pada aktor (Total Control versus Group Manager) dan toast (create versus submit) sesuai jalur; TC-487 Dependensi merujuk TC-158.
  - Post Condition semua TC kosong ("-"); tidak ada yang tidak diasersi.

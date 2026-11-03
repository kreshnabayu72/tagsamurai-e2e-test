---
id: TC-AC-ACHA-E2E-018-form-allocate-preview-biaya-dan-saldo
title: "Form Allocate Device: Preview Biaya, Saldo Kantong, dan Harga Produk"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-121
  - TC-AC-ACHA-122
  - TC-AC-ACHA-123
  - TC-AC-ACHA-124
  - TC-AC-ACHA-125
  - TC-AC-ACHA-126
  - TC-AC-ACHA-127
  - TC-AC-ACHA-128
  - TC-AC-ACHA-129
  - TC-AC-ACHA-130
  - TC-AC-ACHA-131
  - TC-AC-ACHA-132
  - TC-AC-ACHA-478
  - TC-AC-ACHA-479
coverage:
  web: automated
---

# Form Allocate Device: Preview Biaya, Saldo Kantong, dan Harga Produk

## Prerequisites

- Mode: FE+BE. TC-479 memakai intercept parsial (tunda respons estimasi biaya) di atas backend nyata.
- Akun yang diuji:

| Kode | Role | Pre-setup | Email | Env var password |
|---|---|---|---|---|
| A-02 | Total Control Distributor `PT Global Distribusi` (Hendra Wibowo) | #27 | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| A-03 | Total Control Partner `CV Mitra Solusi` (Maya Putri) | #43 | `totalControlPartner1_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_P1_PASSWORD` |
| A-01 | Total Control Principal `PT ABC` (Admin Pratama) | #21 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login A-02 di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (A-01, `AC_TC_PASSWORD`). Ganti akun A-03 dan A-01 dengan langkah logout dan login eksplisit. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example` (didaftarkan tahap script); password tidak ditulis di spec.
- Data Pre-setup: Client #7 `PT Sejahtera Logistik`, #8 `PT Retail Makmur`, #10 `PT Manufaktur Unggul`; kantong #16 PT Global Distribusi saldo $20,000.00 dan #17 CV Mitra Solusi saldo $2,000.00; harga #14 (PT ABC) dan #15 (PT Global Distribusi).
- Data yang disetel fixture API Pre-setup #20 (disediakan tim FE/BE, tanpa endpoint karangan) pada langkah yang menyebutnya: saldo kantong PT Global Distribusi ($20,000.00, $99.99, $100.00), stok fisik BLE Gateway PT Global Distribusi 10 unit, dan harga BLE Gateway di PT ABC belum dikonfigurasi. Hook `before` menyetel saldo $20,000.00, stok fisik semula, dan harga semula; hook `after` memulihkan ketiganya.
- Data Dinamis: dua alokasi `BLE Gateway` dibuat (TC-129 Quantity 50, TC-478 Quantity 100). Efek: saldo kantong PT Global Distribusi berubah ($0.00 lalu dipulihkan fixture) dan kuota Client `PT Sejahtera Logistik` bertambah; modul tanpa Delete sehingga alokasi tidak dihapus. Allocation ID kedua alokasi ditangkap dari baris teratas List sebagai Dynamic Reference.
- Kolom Cost pada List ditampilkan lewat Setup Column (precondition TC-478). Preferensi kolom dipulihkan ke default di hook `after` (hapus preferensi kolom di browser; kemampuan disediakan tim FE) dan didaftarkan di `suite.md`.
- Tabel harga satuan sembilan jenis item (TC-126; Quantity 10; harga PT ABC, Pre-setup #14):

| Category | Type | Estimated Cost |
|---|---|---|
| `TAG - RFID` | `Object TAG` | `$25.00 (10 × $2.50/unit)` |
| `TAG - RFID` | `User TAG` | `$30.00 (10 × $3.00/unit)` |
| `Hardware - Handheld Reader` | `Long Range` | `$300.00 (10 × $30.00/unit)` |
| `Hardware - Handheld Reader` | `Short Range` | `$220.00 (10 × $22.00/unit)` |
| `TAG - NFC` | - | `$12.00 (10 × $1.20/unit)` |
| `TAG - BLE` | - | `$20.00 (10 × $2.00/unit)` |
| `TAG - GPS` | - | `$80.00 (10 × $8.00/unit)` |
| `Hardware - Smart Fixed Reader` | - | `$450.00 (10 × $45.00/unit)` |
| `Hardware - BLE Gateway` | - | `$20.00 (10 × $2.00/unit)` |

- Kemampuan teknis: `Spectra.intercept()` untuk menunda 3 detik respons permintaan estimasi biaya (endpoint tidak disebut TC, PRD, atau LLD; disediakan tim FE/BE), dilepas segera sesudah dipakai; kemampuan baca jumlah transaksi pengirim, Wallet Balance, dan Hardware Stock.
- Hook suite (dinyatakan sekali di `suite.md`): flag Guided Tooltip halaman Device Allocation disetel true untuk akun aktor dan dipulihkan di `after`, sesi API aktor, fixture API Pre-setup #20, pemulihan preferensi Setup Column.
- Suite berjalan serial (`parallel: false`); spec ini mengubah saldo kantong, stok fisik, dan harga produk (state bersama) dan memulihkannya di hook `after`, bersama seed 30 baris lewat fixture Pre-setup #20 (Lampiran A butir A-6).

## Test Steps

### Akun A-02 Distributor, saldo $20,000.00: Syarat tampil dan hitung ulang Preview (TC-AC-ACHA-124, TC-AC-ACHA-121, TC-AC-ACHA-125, TC-AC-ACHA-126, TC-AC-ACHA-127, TC-AC-ACHA-479)

1. Klik `[+ Allocation]`
2. Isi Quantity `50` tanpa memilih Category
3. Verifikasi Preview tidak dirender tanpa Category
4. Pilih Category `Hardware - BLE Gateway`
5. Verifikasi Preview tampil setelah Category dipilih dan Quantity `50` valid
6. Ubah Quantity menjadi `0`
7. Verifikasi Preview tidak dirender
8. Verifikasi pesan "Quantity must be a positive whole number" tampil
9. Verifikasi pesan saldo kurang tidak tampil (saldo tidak dievaluasi)
10. Ubah Quantity menjadi `1000001`
11. Verifikasi Preview tidak dirender
12. Verifikasi pesan "Quantity must not exceed 1,000,000" tampil
13. Pilih Client `PT Sejahtera Logistik` dan ubah Quantity menjadi `50`
14. Verifikasi Preview: Estimated Cost `$100.00 (50 × $2.00/unit)`
15. Verifikasi Preview: Your Pocket Balance `$20,000.00`
16. Verifikasi pesan saldo kurang tidak tampil
17. Verifikasi `[Submit]` enabled
18. Ubah Quantity menjadi `80` tanpa menekan tombol apa pun
19. Verifikasi Preview menghitung ulang real-time: Estimated Cost `$160.00 (80 × $2.00/unit)`
20. Verifikasi Your Pocket Balance tetap `$20,000.00`
21. Ubah Quantity menjadi `10`
22. Untuk setiap baris tabel harga satuan sembilan jenis item lakukan langkah 23 sampai 24
23. Pilih Category (dan Type bila ada) pada baris itu
24. Verifikasi Estimated Cost sama dengan kolom Estimated Cost baris itu
25. Pilih Category `TAG - RFID`
26. Verifikasi Type `Object TAG` terpilih: Estimated Cost `$25.00 (10 × $2.50/unit)`
27. Ganti Type menjadi `User TAG`
28. Verifikasi Type `User TAG`: Estimated Cost `$30.00 (10 × $3.00/unit)`
29. Klik `[Clear Field]`
30. Pilih Category `Hardware - BLE Gateway` dan Client `PT Sejahtera Logistik`
31. Pasang intercept: tunda 3 detik respons permintaan estimasi biaya
32. Isi Quantity `50` dan amati area Preview
33. Verifikasi area Preview menampilkan state skeleton selama menunggu
34. Verifikasi Estimated Cost dan Your Pocket Balance belum tampil selama menunggu
35. Tunggu respons estimasi diterima, lalu lepas intercept
36. Verifikasi skeleton hilang setelah respons diterima
37. Verifikasi Preview menampilkan Estimated Cost `$100.00 (50 × $2.00/unit)`
38. Verifikasi Preview menampilkan Your Pocket Balance `$20,000.00`
39. Klik `[×]`
40. Verifikasi dialog Unsaved Changes tampil
41. Klik `[Leave]`

### Akun A-02, saldo $99.99: Saldo kurang $0.01 memblokir Submit (TC-AC-ACHA-128)

42. Setel saldo kantong PT Global Distribusi menjadi $99.99 lewat fixture API Pre-setup #20
43. Catat baseline jumlah transaksi pengirim lewat kemampuan baca state BE
44. Klik `[+ Allocation]`
45. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, isi Quantity `50`
46. Amati `[Submit]` dan arahkan kursor ke `[Submit]` yang disabled
47. Verifikasi pesan danger real-time "Insufficient balance in your pocket. Available: $99.99. Required: $100.00." tampil
48. Verifikasi `[Submit]` disabled
49. Verifikasi tidak ada transaksi baru (jumlah transaksi sama dengan baseline)
50. Verifikasi tidak ada tooltip pada `[Submit]` yang disabled karena saldo kurang
51. Klik `[×]`
52. Verifikasi dialog Unsaved Changes tampil
53. Klik `[Leave]`

### Akun A-02, saldo $100.00: Pesan saldo kurang real-time dan saldo tepat sama dengan biaya (TC-AC-ACHA-130, TC-AC-ACHA-129)

54. Setel saldo kantong PT Global Distribusi menjadi $100.00 lewat fixture API Pre-setup #20
55. Klik `[+ Allocation]`
56. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`
57. Isi Quantity `51`
58. Verifikasi pesan "Insufficient balance in your pocket. Available: $100.00. Required: $102.00." tampil
59. Verifikasi `[Submit]` disabled
60. Ubah Quantity menjadi `50`
61. Verifikasi pesan saldo kurang hilang
62. Verifikasi `[Submit]` enabled
63. Verifikasi tidak ada pesan saldo kurang pada saldo tepat sama dengan biaya
64. Verifikasi `[Submit]` enabled pada saldo tepat sama dengan biaya
65. Klik `[Submit]`
66. Tunggu aksi selesai
67. Verifikasi baris teratas List berstatus `Completed` (Total Control auto-bypass)
68. Catat Allocation ID baris teratas List (transaksi TC-129)
69. Buka halaman Wallet Balance kantong PT Global Distribusi
70. Verifikasi saldo kantong menjadi $0.00

### Akun A-02, saldo $20,000.00 dan stok fisik 10 unit: Quantity melebihi stok fisik tetap dapat dialokasikan (TC-AC-ACHA-478)

71. Setel saldo kantong PT Global Distribusi menjadi $20,000.00 dan stok fisik BLE Gateway PT Global Distribusi menjadi 10 unit lewat fixture API Pre-setup #20
72. Buka Allocation > Device Allocation, lalu buka Setup Column dan tampilkan kolom Cost, klik `[Save]`
73. Klik `[+ Allocation]`
74. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, isi Quantity `100`
75. Verifikasi `[Submit]` enabled
76. Verifikasi tidak ada pesan terkait stok
77. Klik `[Submit]`
78. Verifikasi toast sukses "Success, device allocation has been created."
79. Verifikasi baris baru berstatus `Completed` dengan Quantity `100`
80. Catat Allocation ID baris teratas List (transaksi TC-478)
81. Verifikasi baris baru memuat Cost `$200.00`
82. Buka halaman Hardware Stock dan baca stok BLE Gateway pengirim
83. Verifikasi stok fisik BLE Gateway pada Hardware Stock tetap 10 unit

### Akun A-02, harga produk belum dikonfigurasi: Submit disabled dengan tooltip (TC-AC-ACHA-131)

84. Setel harga BLE Gateway di PT ABC menjadi belum dikonfigurasi lewat fixture API Pre-setup #20
85. Buka Allocation > Device Allocation, lalu klik `[+ Allocation]`
86. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, isi Quantity `5`
87. Arahkan kursor ke `[Submit]` yang disabled
88. Verifikasi `[Submit]` disabled
89. Verifikasi Preview tidak dirender
90. Verifikasi tooltip pada `[Submit]`: "Set product price first (Wallet > Product Price)."
91. Pindahkan fokus keyboard ke `[Submit]` dengan Tab
92. Verifikasi tooltip "Set product price first (Wallet > Product Price)." juga muncul pada keyboard focus
93. Klik `[×]`
94. Verifikasi dialog Unsaved Changes tampil
95. Klik `[Leave]`
96. Pulihkan harga BLE Gateway di PT ABC lewat fixture API Pre-setup #20

### Akun A-03 Partner: Preview memakai harga jual Distributor (TC-AC-ACHA-122)

97. Logout, lalu login sebagai A-03 (`CV Mitra Solusi`), buka Allocation > Device Allocation
98. Klik `[+ Allocation]`
99. Pilih Category `Hardware - BLE Gateway`, Client `PT Retail Makmur`, isi Quantity `50`
100. Verifikasi Preview: Estimated Cost `$125.00 (50 × $2.50/unit)`
101. Verifikasi Preview: Your Pocket Balance `$2,000.00`
102. Klik `[×]`
103. Verifikasi dialog Unsaved Changes tampil
104. Klik `[Leave]`

### Akun A-01 Principal: Tanpa Preview biaya dan tidak terpengaruh harga produk (TC-AC-ACHA-123, TC-AC-ACHA-132)

105. Logout, lalu login sebagai A-01, buka Allocation > Device Allocation
106. Klik `[+ Allocation]`
107. Pilih Category `Hardware - BLE Gateway`, Client `PT Manufaktur Unggul`, isi Quantity `50`
108. Verifikasi Preview tidak dirender
109. Verifikasi tidak ada field Pay From
110. Verifikasi `[Submit]` enabled
111. Setel harga BLE Gateway di PT ABC menjadi belum dikonfigurasi lewat fixture API Pre-setup #20
112. Ubah Quantity menjadi `5`
113. Verifikasi `[Submit]` enabled karena Principal tidak memakai harga produk
114. Verifikasi tidak ada Preview
115. Klik `[×]`
116. Verifikasi dialog Unsaved Changes tampil
117. Klik `[Leave]`

## Notes

- Mode FE+BE; sumber `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan spec di atas sekitar 35 langkah: semua blok satu topik (Preview, saldo, dan harga pada form Allocate Device) dan satu kelas; tiap blok didefinisikan oleh state kantong atau harga yang disetel fixture dan berdiri sendiri; dua submit sukses (TC-129 dan TC-478) berada di akhir blok masing-masing; langkah berulang TC-126 dihitung dengan ekspansi sembilan iterasi (langkah 23 sampai 24).
- Penyimpangan urutan (S-10): TC-124 dijalankan lebih dulu pada form pertama (urutan state: tanpa Category, Category terpilih, Quantity tidak valid) sebelum TC-121; TC-130 mendahului TC-129 pada form yang sama karena saldo $100.00 dan Quantity 50 adalah keadaan akhir TC-130; TC-478 (submit sukses) dan TC-131 diletakkan di akhir blok Distributor; TC-132 memakai form TC-123 setelah harga diatur belum dikonfigurasi.
- Langkah penghubung (S-03): `[Clear Field]` sebelum TC-479, pemasangan dan pelepasan intercept, penutupan form dirty lewat `[×]`, dialog Unsaved Changes, `[Leave]` (S-08), logout dan login ganti akun, penyetelan fixture, tampilkan kolom Cost lewat Setup Column, dan fokus keyboard ke `[Submit]` (TC-131 butir c).
- Efek submit sukses: TC-129 menyisakan saldo $0.00 dan TC-478 memotong $200.00; fixture Pre-setup #20 di hook `after` mengembalikan saldo $20,000.00.
- Pengecualian S-12 nama literal: nama entitas dan Client Pre-setup literal (sudah ada di environment); tidak ada Notes atau nama dinamis di spec ini.
- Temuan untuk QA:
  - TC-124 Expected c ("saldo tidak dievaluasi") tidak punya langkah observasi sendiri; spec mengasersinya sebagai tidak adanya pesan saldo kurang.
  - TC-129 Expected c menulis "(Capture $100.00)" tanpa langkah observasi di Wallet Transaction List; spec hanya mengasersi saldo $0.00. Post Condition kuota Client tanpa langkah observasi tidak diasersi.
  - TC-479 tidak menyebut endpoint permintaan estimasi biaya yang ditunda; spec menuliskannya sebagai kemampuan "disediakan tim FE/BE".
  - TC-131 butir c ("Tooltip juga muncul pada keyboard focus") tidak menyebut cara memfokuskan tombol yang disabled; spec memakai Tab.
  - TC-478 menyebut Hardware Stock (modul lain) dan stok fisik disetel lewat Pre-setup #20; kontrak fixture tidak tertulis.

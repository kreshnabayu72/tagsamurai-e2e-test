---
id: TC-GS-IMPORT-E2E-123-create-missing-divisions-dan-positions-per-baris-record-dibuat-baris
title: "Create Missing Divisions dan Positions per-baris: record dibuat, baris pulih ke pending, Metric Cards, Code otomatis, tanpa staging"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-323
  - TC-GS-IMPORT-324
  - TC-GS-IMPORT-325
  - TC-GS-IMPORT-326
  - TC-GS-IMPORT-336
  - TC-GS-IMPORT-346
  - TC-GS-IMPORT-350
  - TC-GS-IMPORT-351
coverage:
  web: automated
---

# Create Missing Divisions dan Positions per-baris: record dibuat, baris pulih ke pending, Metric Cards, Code otomatis, tanpa staging

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import; sub-tab dipilih di `## Test Steps`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Pre-setup Client C (tidak diubah): Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang` (5 item); Position `Store Manager`, `Senior Developer`, `Finance Manager`, `Technician`, `Supervisor` (5 item). Client C tanpa draft di Tab User Login, User Non Login, dan Division sebelum tiap TC (fixture reset, Kontrak Fixture R1).
- Data Dinamis (berkas disediakan tim QA, fixture baru `Fixture.import.berkas`; berkas User Login/Non Login standar D-45, Position kosong kecuali disebut): `user-login-logistik-4.csv` (Siti Rahmawati, Budi Santoso, Andi Pratama, Rina Wijaya; Division `Logistik`), `user-non-login-logistik-1.csv` (Ayu Lestari, Division `Logistik`, Represented By `budi.manager.c@example.com`), `user-login-store-supervisor-1.csv` (Siti Rahmawati, Division `Engineering`, Position `Store Supervisor`), `user-non-login-store-supervisor-1.csv` (Ayu Lestari, Division `Engineering`, Position `Store Supervisor`, Represented By `budi.manager.c@example.com`), `user-login-regional-sales.csv` (Siti Rahmawati, Division `Regional Sales`). Nama master data baru `Logistik`, `Store Supervisor`, dan `Regional Sales` literal sesuai TC (pengecualian S-12 untuk Name literal penentu hasil auto-generate Code, mis. `Logistik` menjadi `LOGIST`); record yang dibuat spec dihapus lewat API setelah tiap TC (R2) dan sisa dari run sebelumnya dibersihkan di hook `before`.
- Kemampuan teknis: intercept jaringan yang menunda respons permintaan Create Missing 3 detik dan menghitung permintaan (hanya untuk mengamati spinner, bukan kelas b); fixture reset draft client; penghapusan Division dan Position lewat API; pembacaan pagination dan kolom Code tabel Division.
- State global: tidak ada selain master data Client C yang dibuat dan dihapus kembali. Suite berjalan serial (`parallel: false`).
- Cleanup (hook `afterEach`/`after`, tidak berasumsi setup berhasil penuh): hapus Division `Logistik`, `Regional Sales` dan Position `Store Supervisor` bila ada, reset draft User Login, User Non Login, dan Division Client C, lepas intercept.

## Test Steps

### TC-GS-IMPORT-323: Create Missing Divisions per-baris dari Actions membuat satu Division dan baris pulih ke pending

1. Pilih sub-tab User Login
2. Klik [Upload File] di Dropzone dan pilih berkas `user-login-logistik-4.csv`
3. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
4. Verifikasi Staging Table menampilkan 4 baris `error`
5. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "4 rows"
6. Klik `⋯` pada baris #1
7. Pilih `[Create Missing Divisions]`
8. Verifikasi tidak ada dialog konfirmasi
9. Verifikasi toast sukses: "Success, division has been created."
10. Muat ulang halaman Import > User Login
11. Verifikasi keempat baris berstatus `pending`
12. Verifikasi Staging Metric Cards: Total Rows 4, Ready to Import 4, Errors 0
13. Buka Global Settings > User > Division
14. Verifikasi daftar Division memuat `Logistik`
15. Verifikasi tabel Division menampilkan 6 baris
16. Hapus Division `Logistik` lewat API dan reset draft User Login Client C lewat fixture reset

### TC-GS-IMPORT-325: Create Missing Divisions per-baris pada Tab User Non Login

17. Buka Import dan pilih sub-tab User Non Login
18. Klik [Upload File] di Dropzone dan pilih berkas `user-non-login-logistik-1.csv`
19. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
20. Verifikasi baris #1 berstatus `error`
21. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "1 row"
22. Klik `⋯` pada baris #1
23. Pilih `[Create Missing Divisions]`
24. Verifikasi toast sukses: "Success, division has been created."
25. Muat ulang halaman Import > User Non Login
26. Verifikasi baris #1 berstatus `pending`
27. Verifikasi Staging Metric Cards: Total Rows 1, Ready to Import 1, Errors 0
28. Buka Global Settings > User > Division
29. Verifikasi daftar Division memuat `Logistik`
30. Verifikasi tabel Division menampilkan 6 baris
31. Hapus Division `Logistik` lewat API dan reset draft User Non Login Client C lewat fixture reset

### TC-GS-IMPORT-350 dan TC-GS-IMPORT-351: Record baru ter-resolve pada pembacaan berikutnya dan Division hasil Create Missing memperoleh Code otomatis

TC-GS-IMPORT-350 dan 351 memiliki precondition, berkas, dan aksi pemicu yang sama (`[Create Missing Divisions]` dari Callout pada `user-login-logistik-4.csv`); satu alur menjalankan Expected keduanya.

32. Buka Import dan pilih sub-tab User Login
33. Klik [Upload File] di Dropzone dan pilih berkas `user-login-logistik-4.csv`
34. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
35. Verifikasi Staging Metric Cards: Total Rows 4, Ready to Import 0, Errors 4
36. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
37. Verifikasi toast sukses: "Success, division has been created."
38. Muat ulang halaman Import > User Login
39. Verifikasi Staging Metric Cards: Total Rows 4, Ready to Import 4, Errors 0
40. Verifikasi Footer menampilkan `[Import (4)]`
41. Buka Global Settings > User > Division dan perhatikan baris `Logistik`
42. Verifikasi kolom Code pada baris `Logistik` berisi `LOGIST`
43. Hapus Division `Logistik` lewat API dan reset draft User Login Client C lewat fixture reset

### TC-GS-IMPORT-346: Tombol Create Missing Disabled dengan spinner selama request berjalan

44. Buka Import dan pilih sub-tab User Login
45. Klik [Upload File] di Dropzone dan pilih berkas `user-login-logistik-4.csv`
46. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
47. Atur intercept jaringan agar respons permintaan Create Missing ditunda 3 detik dan hitung jumlah permintaan yang terkirim
48. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
49. Verifikasi tombol `[Create Missing Divisions]` tampil Disabled dengan spinner
50. Klik lagi tombol yang sama saat permintaan berjalan
51. Verifikasi jumlah permintaan Create Missing yang terkirim pada intercept tetap 1
52. Tunggu respons diterima, lalu lepas intercept
53. Buka Global Settings > User > Division
54. Verifikasi daftar Division memuat tepat satu `Logistik`
55. Verifikasi tabel Division menampilkan 6 baris
56. Hapus Division `Logistik` lewat API dan reset draft User Login Client C lewat fixture reset

### TC-GS-IMPORT-324: Create Missing Positions per-baris membuat Position dan baris pulih ke pending

57. Buka Import dan pilih sub-tab User Login
58. Klik [Upload File] di Dropzone dan pilih berkas `user-login-store-supervisor-1.csv`
59. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
60. Verifikasi baris #1 berstatus `error`
61. Verifikasi Error Summary Callout memuat "Position not found" dengan badge "1 row"
62. Klik `⋯` pada baris #1
63. Pilih `[Create Missing Positions]`
64. Verifikasi toast sukses: "Success, position has been created."
65. Muat ulang halaman Import > User Login
66. Verifikasi baris #1 berstatus `pending`
67. Verifikasi Staging Metric Cards: Total Rows 1, Ready to Import 1, Errors 0
68. Buka Global Settings > User > Position
69. Verifikasi daftar Position memuat `Store Supervisor`
70. Verifikasi tabel Position menampilkan 6 baris
71. Hapus Position `Store Supervisor` lewat API dan reset draft User Login Client C lewat fixture reset

### TC-GS-IMPORT-326: Create Missing Positions per-baris pada Tab User Non Login

72. Buka Import dan pilih sub-tab User Non Login
73. Klik [Upload File] di Dropzone dan pilih berkas `user-non-login-store-supervisor-1.csv`
74. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
75. Verifikasi baris #1 berstatus `error`
76. Verifikasi Error Summary Callout memuat "Position not found" dengan badge "1 row"
77. Klik `⋯` pada baris #1
78. Pilih `[Create Missing Positions]`
79. Verifikasi toast sukses: "Success, position has been created."
80. Muat ulang halaman Import > User Non Login
81. Verifikasi baris #1 berstatus `pending`
82. Verifikasi Staging Metric Cards: Total Rows 1, Ready to Import 1, Errors 0
83. Buka Global Settings > User > Position
84. Verifikasi daftar Position memuat `Store Supervisor`
85. Verifikasi tabel Position menampilkan 6 baris
86. Hapus Position `Store Supervisor` lewat API dan reset draft User Non Login Client C lewat fixture reset

### TC-GS-IMPORT-336: Create Missing Divisions menulis ke modul Division tanpa melalui staging Tab Division

87. Buka Import dan pilih sub-tab User Login
88. Klik [Upload File] di Dropzone dan pilih berkas `user-login-regional-sales.csv`
89. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
90. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
91. Verifikasi toast sukses: "Success, division has been created."
92. Buka Import > Division dan perhatikan Staging Table
93. Verifikasi Tab Division menampilkan Dropzone (belum ada draft)
94. Verifikasi Tab Division tidak memuat baris `Regional Sales`
95. Buka Global Settings > User > Division dan perhatikan daftar Division
96. Verifikasi daftar Division memuat `Regional Sales`
97. Verifikasi tabel Division menampilkan 6 baris
98. Hapus Division `Regional Sales` lewat API dan reset draft User Login Client C lewat fixture reset

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Subjudul `###` memetakan langkah ke id TC.
- Urutan: TC-GS-IMPORT-323, 325, 350/351, 346 (Division), 324, 326 (Position), 336. Tiap blok membuat dan menghapus kembali master data sendiri supaya precondition "belum ada" terpenuhi.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 17, 32, 44, 57, 72, 87 (memilih sub-tab), 13, 28, 41, 53, 68, 83, 95 (membuka daftar master data untuk observasi), 16, 31, 43, 56, 71, 86, 98 (pemulihan master data dan draft, R2 dan S-09), 47 dan 52 (intercept dipasang dan dilepas segera setelah pemicu selesai, S-09).
- Absence pada langkah 8 (dialog konfirmasi) diletakkan segera setelah pemicu (butir 11 bagian 8b) dan berjangkar pada toast sukses langkah 9; absence langkah 94 berjangkar pada Dropzone langkah 93 sebagai permukaan yang sama.
- Intercept pada langkah 47 hanya menahan respons untuk mengamati spinner (bukan kelas b, bagian 3 prinsip 13).
- Penggabungan: TC-GS-IMPORT-350 (Metric Cards sebelum dan sesudah muat ulang) dan TC-GS-IMPORT-351 (Code otomatis) dijalankan dalam satu alur karena precondition dan aksi sama; urutan asersi mengikuti urutan state.
- Spec melewati sekitar 35 langkah (98 langkah): tujuh blok homogen (satu aksi Create Missing per Tab atau jenis), satu kelas fungsional, tiap blok berdiri sendiri dengan master data dan draft sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Pembagian TC lintas spec: Create Missing massal dari Callout ada di spec 124; kegagalan sebagian di spec 125; Options di spec 129 dan 130; visibilitas tombol di spec 122; Changelog/System Log/Activity Log Create Missing di spec 128.
- Temuan untuk QA:
  - TC-GS-IMPORT-336: Post Condition b ("draft User Login berisi 1 baris `error` sampai halaman dimuat ulang") tidak punya langkah observasi dan tidak diasersi.
  - TC-GS-IMPORT-323: Expected b ("tidak ada dialog konfirmasi") bersifat absence tanpa anchor eksplisit di TC; spec memakai toast sukses berikutnya sebagai anchor.
  - Berkas `user-non-login-logistik-1.csv`, `user-non-login-store-supervisor-1.csv`, `user-login-store-supervisor-1.csv`, dan `user-login-regional-sales.csv` hanya didefinisikan pada kolom Data Uji TC, bukan Data Dinamis.
  - TC-GS-IMPORT-346: cara intercept menghitung permintaan Create Missing tidak dirinci (endpoint tidak disebut di TC); disediakan tim FE sesuai S-13.
  - Hitungan "6 baris pada tabel" mengandalkan Pre-setup 5 Division dan 5 Position; tabel Division/Position Client C tidak boleh memuat record lain dari spec yang berjalan sebelumnya.

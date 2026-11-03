---
id: TC-AC-LA-E2E-128-event-allocation-log-aksi-requester
title: "Event Allocation Log Aksi Requester: Created, Edited, Canceled, Resubmitted, Station, Storage, dan App"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-401
  - TC-AC-LA-404
  - TC-AC-LA-405
  - TC-AC-LA-409
  - TC-AC-LA-410
  - TC-AC-LA-519
  - TC-AC-LA-520
coverage:
  web: automated
---

# Event Allocation Log Aksi Requester: Created, Edited, Canceled, Resubmitted, Station, Storage, dan App

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini; halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Dewi Anggraini | #4 | Distributor PT Maju Bersama, Manage allocation Create+Read+Update | `dewiFullLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DIST_FULL_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19; `SUBS-20260101-A1B2C`), CV Mitra Sejati (Pre-setup #22; SAMS Growth `SUBS-20260105-K2L3M`), Klinik Harapan Bunda (Pre-setup #24), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price (Pre-setup #34: Concurrent User $365 per unit per tahun, Asset Control App flat $150, Asset Control Station $50.00 per Station, Storage $2 per GB), Require Approval for Allocation ON (Pre-setup #38) untuk blok TC-AC-LA-404, 405, dan 410, OFF (Pre-setup #39) untuk blok TC-AC-LA-401, 409, 519, dan 520.
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #41 dan #48 bersama):
  - `{idEdit}`: alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Dewi Anggraini, Cost snapshot $30.00 per unit (Cost $150.00) di-Reserve (bentuk Pre-setup #41);
  - `{idCancel}`: alokasi `Waiting for Approval` dengan bentuk yang sama (bentuk Pre-setup #41);
  - `{idCanceled}`: alokasi `Canceled` manual Concurrent User +5 PT Sejahtera, requester Dewi Anggraini (bentuk Pre-setup #48);
  - `{idResub}`, `{idCU}`, `{idOne}`, `{idStation}`, `{idStorage}`, `{idApp}`: Allocation ID hasil Resubmit atau Submit di spec ini.
- Kemampuan teknis (disediakan tim FE/BE): seeding alokasi dan pembersihannya; fixture waktu untuk jam server dan jam browser dengan nilai absolut; fixture backend untuk menyetel Require Approval for Allocation ON atau OFF; kemampuan membaca jumlah entri Allocation Log `{idCanceled}` (`{nLogCanceled}`), dicatat di hook `before`; fixture backend untuk menonaktifkan alokasi `Active` Asset Control App Pre-setup #53 pada `SUBS-20260105-K2L3M` sebelum blok TC-AC-LA-520 (opsi App ke Subscription yang sama diblokir selama #53 hadir) dan memulihkannya di hook `after`.
- State global: jam server dan jam browser diatur ke `22 Dec 2026` hanya pada blok TC-AC-LA-401 dan dipulihkan setelah Submit; toggle Require Approval for Allocation diubah ke OFF sesudah blok TC-AC-LA-410 dan dipulihkan di hook `after`; saldo kantong #33 dipulihkan oleh pembersihan record; alokasi Pre-setup #53 dinonaktifkan sebelum blok TC-AC-LA-520 (langkah 95) dan dipulihkan di hook `after` (S-06, pengecualian 2026-10-30; efeknya pada Last Updated dan audit trail #53 dicatat di sini).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Allocation edited by (TC-AC-LA-404)

1. Ketik Search `{idEdit}`, tekan Enter
2. Klik row action `Edit` pada alokasi milik sendiri `{idEdit}`
3. Ubah Additional Quantity dari `5` menjadi `8`
4. Klik `[Save]`
5. Klik row action `Allocation Log` pada baris `{idEdit}`
6. Verifikasi judul entri `Allocation edited by Dewi A`
7. Verifikasi Description entri memuat `Product: FAMS`, `License Type: Concurrent User`, `Target: SUBS-20260101-A1B2C`, `Quantity: +8`, `Cost: $240.00 (Wallet)`, tanpa `Resubmitted From`
8. Verifikasi entri memuat Date & Time sesuai General Settings
9. Verifikasi baris judul berupa teks biasa, bukan badge
10. Tutup modal Allocation Log

### Allocation canceled by (TC-AC-LA-405)

11. Ganti isi kotak search dengan `{idCancel}`, tekan Enter
12. Klik row action `Cancel Allocation` pada alokasi milik sendiri `{idCancel}`
13. Klik `[Cancel Request]`
14. Klik tab `History`
15. Klik row action `Allocation Log` pada baris `{idCancel}`
16. Verifikasi judul entri `Allocation canceled by Dewi A` tanpa baris Description
17. Verifikasi entri memuat Date & Time sesuai General Settings
18. Verifikasi baris judul berupa teks biasa, bukan badge
19. Tutup modal Allocation Log
20. Klik tab `Current`, klik `(←)` pada kotak Search, lalu catat baseline Allocation ID baris di halaman pertama

### Entri created hasil Resubmit (TC-AC-LA-410)

21. Klik tab `History`, ketik Search `{idCanceled}`, tekan Enter
22. Klik row action `Resubmit` pada baris `{idCanceled}`
23. Klik `[Submit]`
24. Klik tab `Current`
25. Klik `(←)` pada kotak Search, lalu catat Allocation ID record baru sebagai `{idResub}` (baris yang tidak ada pada baseline langkah 20; record baru hanya tampil di tab Current)
26. Ketik Search `{idResub}`, tekan Enter
27. Klik row action `Allocation Log` pada baris `{idResub}`
28. Verifikasi Description entri created record baru memuat `Resubmitted From: {idCanceled}`
29. Tutup modal Allocation Log
30. Klik tab `History`
31. Ganti isi kotak search dengan `{idCanceled}`, tekan Enter
32. Klik row action `Allocation Log` pada baris `{idCanceled}`
33. Verifikasi jumlah entri Allocation Log record asal `{idCanceled}` sama dengan `{nLogCanceled}` (log record asal tidak berubah)
34. Tutup modal Allocation Log
35. Setel Require Approval for Allocation OFF (Pre-setup #39) lewat fixture backend
36. Klik tab `Current`
37. Klik `(←)` pada kotak Search, lalu catat baseline Allocation ID baris di halaman pertama tab Current

### Allocation created by: Concurrent User (TC-AC-LA-401)

38. Atur jam server dan jam browser ke `22 Dec 2026` (nilai absolut)
39. Klik `[+ Allocation]`
40. Pilih Client `PT Sejahtera`
41. Pilih Target `SUBS-20260101-A1B2C`
42. Pilih Type `Concurrent User`
43. Isi Additional Quantity `10`
44. Klik `[Submit]`
45. Catat Allocation ID baris baru sebagai `{idCU}` (tidak ada pada baseline langkah 37)
46. Pulihkan jam server dan jam browser ke waktu nyata
47. Ketik Search `{idCU}`, tekan Enter
48. Klik row action `Allocation Log` pada baris `{idCU}`
49. Verifikasi judul entri `Allocation created by Dewi A`
50. Verifikasi Description entri memuat `Product: FAMS`, `License Type: Concurrent User`, `Target: SUBS-20260101-A1B2C`, `Quantity: +10`, `Cost: $100.00 (Wallet)`
51. Verifikasi entri memuat Date & Time sesuai General Settings
52. Verifikasi baris judul berupa teks biasa, bukan badge
53. Tutup modal Allocation Log
54. Klik `(←)` pada kotak Search, lalu catat baseline Allocation ID baris di halaman pertama tab Current

### Alokasi Completed langsung hanya punya entri created (TC-AC-LA-409)

55. Klik `[+ Allocation]`
56. Pilih Client `PT Sejahtera`
57. Pilih Target `SUBS-20260101-A1B2C`
58. Pilih Type `Concurrent User`
59. Isi Additional Quantity `1`
60. Klik `[Submit]`
61. Catat Allocation ID baris baru sebagai `{idOne}` (tidak ada pada baseline langkah 54)
62. Ganti isi kotak search dengan `{idOne}`, tekan Enter
63. Klik row action `Allocation Log` pada baris `{idOne}`
64. Verifikasi Allocation Log `{idOne}` memuat tepat satu entri `Allocation created by Dewi A`
65. Verifikasi Allocation Log `{idOne}` tidak memuat entri `Allocation approved`
66. Tutup modal Allocation Log
67. Klik `(←)` pada kotak Search, lalu catat baseline Allocation ID baris di halaman pertama tab Current

### Allocation created: Asset Control Station dan Storage (TC-AC-LA-519)

68. Klik `[+ Allocation]`
69. Pilih Client `Klinik Harapan Bunda`
70. Pilih Target `Client-wide`
71. Pilih Type `Asset Control Station`
72. Isi Additional Quantity `10`
73. Klik `[Submit]`
74. Catat Allocation ID baris baru sebagai `{idStation}` (tidak ada pada baseline langkah 67)
75. Ganti isi kotak search dengan `{idStation}`, tekan Enter
76. Klik row action `Allocation Log` pada baris `{idStation}`
77. Verifikasi judul entri `Allocation created by Dewi A`
78. Verifikasi Description entri memuat `License Type: Asset Control Station`, `Target: Client-wide`, `Quantity: +10`, `Cost: $500.00 (Wallet)`
79. Verifikasi Description entri tidak memuat baris `Product`
80. Tutup modal Allocation Log
81. Klik `(←)` pada kotak Search, lalu catat baseline Allocation ID baris di halaman pertama tab Current
82. Klik `[+ Allocation]`
83. Pilih Client `Klinik Harapan Bunda`
84. Pilih Target `Client-wide`
85. Pilih Type `Storage`
86. Isi Additional Quantity `50`
87. Klik `[Submit]`
88. Catat Allocation ID baris baru sebagai `{idStorage}` (tidak ada pada baseline langkah 81)
89. Ganti isi kotak search dengan `{idStorage}`, tekan Enter
90. Klik row action `Allocation Log` pada baris `{idStorage}`
91. Verifikasi judul entri `Allocation created by Dewi A`
92. Verifikasi Description entri memuat `License Type: Storage`, `Target: Client-wide`, `Quantity: +50 GB`, `Cost: $100.00 (Wallet)`
93. Verifikasi Description entri tidak memuat baris `Product`
94. Tutup modal Allocation Log

### Allocation created: Asset Control App tanpa baris Quantity (TC-AC-LA-520)

95. Nonaktifkan alokasi `Active` Asset Control App Pre-setup #53 pada `SUBS-20260105-K2L3M` lewat fixture backend hingga tersimpan
96. Klik `(←)` pada kotak Search, lalu catat baseline Allocation ID baris di halaman pertama tab Current
97. Klik `[+ Allocation]`
98. Pilih Client `CV Mitra Sejati`
99. Pilih Target `SUBS-20260105-K2L3M`
100. Pilih Type `Asset Control App`
101. Klik `[Submit]`
102. Catat Allocation ID baris baru sebagai `{idApp}` (tidak ada pada baseline langkah 96)
103. Ganti isi kotak search dengan `{idApp}`, tekan Enter
104. Klik row action `Allocation Log` pada baris `{idApp}`
105. Verifikasi judul entri `Allocation created by Dewi A`
106. Verifikasi Description entri memuat `Product: SAMS`, `License Type: Addon (Asset Control App)`, `Target: SUBS-20260105-K2L3M`, `Cost: $150.00 (Wallet)`
107. Verifikasi Description entri tidak memuat baris `Quantity`
108. Tutup modal Allocation Log

## Notes

- Alasan di atas sekitar 35 langkah (108 langkah; enam langkah baseline Allocation ID ikut menambah hitungan): seluruh blok satu topik (isi Allocation Log per event aksi requester Dewi Anggraini), satu kelas harness fungsional, dan masing-masing memakai record sendiri sehingga berdiri sendiri. Langkah yang diulang adalah pengisian form Allocate per Type (lima kali) dan pembukaan modal Allocation Log per record; blok baca-log berpola (buka modal, `Verifikasi` isi entri) tidak dihitung pada ambang smell.
- Urutan blok mengikuti kebutuhan toggle (ON untuk TC-AC-LA-404, 405, dan 410, lalu OFF untuk TC-AC-LA-401, 409, 519, dan 520) dan berbeda dari urutan sourceTc agar toggle hanya diubah satu kali.
- Asersi absence pada langkah 65, 79, 93, dan 107 adalah elemen Description pada modal yang sudah terbuka dan memuat entri created pada langkah sebelumnya sebagai anchor positif; bukan kelas g.
- Langkah penghubung (S-03, R-16): langkah 1, 11, 21, 26, 31, 47, 62, 75, 89, dan 103 (Search baris berdasarkan Allocation ID), langkah 10, 19, 29, 34, 53, 66, 80, 94, dan 108 (menutup modal), langkah 14, 24, 30, dan 36 (pindah tab; langkah 24 pindah ke tab Current sebelum mencatat ID Resubmit karena record baru hanya tampil di tab Current), langkah 35 (menyetel toggle), langkah 95 (menonaktifkan #53 untuk blok TC-AC-LA-520), langkah 38 dan 46 (mengatur dan memulihkan jam), langkah 20, 37, 54, 67, 81, dan 96 (baseline Allocation ID baris di halaman pertama tab Current sebelum tiap `[Submit]`, S-12, pola spec 042; Search dikosongkan dengan klik `(←)` pada kotak Search agar baris baru tampil, dan langkah 25 mencatat `{idResub}` pada tab dan kondisi Search yang sama dengan baseline langkah 20, dan baris baru diambil dari Allocation ID yang tidak ada pada baseline).
- Temuan untuk QA:
  - TC-AC-LA-520 mengalokasikan Asset Control App ke `SUBS-20260105-K2L3M` CV Mitra Sejati, sedangkan Pre-setup #53 sudah men-seed alokasi `Active` Asset Control App pada Subscription yang sama (opsi App ke Subscription yang sama diblokir); Submit hanya berhasil bila #53 tidak ada. TC tidak menyebut penyingkiran #53; spec menonaktifkannya lewat fixture backend yang disediakan tim FE/BE (langkah 95) dan memulihkannya di hook `after`. Pembacaan #53 sebagai baca-saja di Pre-setup diselesaikan lewat pengecualian S-06 (2026-10-30) yang dicatat di Prerequisites dan State global spec ini.
  - TC-AC-LA-404 menyebut Cost snapshot $30.00 per unit sedangkan Product Price Concurrent User adalah $365 per unit per tahun (Pre-setup #34); spec memakai snapshot seed $30.00 per unit sehingga Cost $240.00.
  - TC-AC-LA-401 menyebut `Product: FAMS` tanpa menjelaskan sumbernya; spec mengikuti TC.
  - TC-AC-LA-519 tidak menyebut tanggal acuan server; Cost Station dan Storage bukan prorata sehingga jam tidak diatur pada blok itu.
  - TC-AC-LA-409, 519, dan 520 tidak menyebut Allocation ID record baru; spec mencatat ID setelah Submit.

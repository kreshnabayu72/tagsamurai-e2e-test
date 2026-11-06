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
- State global: jam server dan jam browser diatur ke `22 Dec 2026` hanya pada blok TC-AC-LA-401 dan dipulihkan setelah Submit; toggle Require Approval for Allocation diubah ke OFF sesudah blok TC-AC-LA-410 dan dipulihkan di hook `after`; saldo kantong #33 dipulihkan oleh pembersihan record; alokasi Pre-setup #53 dinonaktifkan sebelum blok TC-AC-LA-520 (langkah 107) dan dipulihkan di hook `after` (S-06, pengecualian 2026-10-30; efeknya pada Last Updated dan audit trail #53 dicatat di sini).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Allocation edited by (TC-AC-LA-404)

1. Ketik Search `{idEdit}`, tekan Enter
2. Klik row action `Edit` pada alokasi milik sendiri `{idEdit}`
3. Ubah Additional Quantity dari `5` menjadi `8`
4. Klik `[Save]`
5. Tunggu aksi selesai
6. Klik row action `Allocation Log` pada baris `{idEdit}`
7. Verifikasi judul entri `Allocation edited by Dewi A`
8. Verifikasi Description entri memuat `Product: FAMS`, `License Type: Concurrent User`, `Target: SUBS-20260101-A1B2C`, `Quantity: +8`, `Cost: $240.00 (Wallet)`, tanpa `Resubmitted From`
9. Verifikasi entri memuat Date & Time sesuai General Settings
10. Verifikasi baris judul berupa teks biasa, bukan badge
11. Tutup modal Allocation Log

### Allocation canceled by (TC-AC-LA-405)

12. Ganti isi kotak search dengan `{idCancel}`, tekan Enter
13. Klik row action `Cancel Allocation` pada alokasi milik sendiri `{idCancel}`
14. Klik `[Cancel Request]`
15. Tunggu aksi selesai
16. Klik tab `History`
17. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
18. Ketik Search `{idCancel}`, tekan Enter
19. Klik row action `Allocation Log` pada baris `{idCancel}`
20. Verifikasi judul entri `Allocation canceled by Dewi A` tanpa baris Description
21. Verifikasi entri memuat Date & Time sesuai General Settings
22. Verifikasi baris judul berupa teks biasa, bukan badge
23. Tutup modal Allocation Log
24. Klik tab `Current`
25. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
26. Catat baseline Allocation ID baris di halaman pertama tab Current

### Entri created hasil Resubmit (TC-AC-LA-410)

27. Klik tab `History`
28. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
29. Ketik Search `{idCanceled}`, tekan Enter
30. Klik row action `Resubmit` pada baris `{idCanceled}`
31. Klik `[Submit]`
32. Tunggu aksi selesai
33. Klik tab `Current`
34. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
35. Catat Allocation ID record baru sebagai `{idResub}` (baris yang tidak ada pada baseline langkah 26; record baru hanya tampil di tab Current)
36. Ketik Search `{idResub}`, tekan Enter
37. Klik row action `Allocation Log` pada baris `{idResub}`
38. Verifikasi Description entri created record baru memuat `Resubmitted From: {idCanceled}`
39. Tutup modal Allocation Log
40. Klik tab `History`
41. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
42. Ketik Search `{idCanceled}`, tekan Enter
43. Klik row action `Allocation Log` pada baris `{idCanceled}`
44. Verifikasi jumlah entri Allocation Log record asal `{idCanceled}` sama dengan `{nLogCanceled}` (log record asal tidak berubah)
45. Tutup modal Allocation Log
46. Setel Require Approval for Allocation OFF (Pre-setup #39) lewat fixture backend
47. Klik tab `Current`
48. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
49. Catat baseline Allocation ID baris di halaman pertama tab Current

### Allocation created by: Concurrent User (TC-AC-LA-401)

50. Atur jam server dan jam browser ke `22 Dec 2026` (nilai absolut)
51. Klik `[+ Allocation]`
52. Pilih Client `PT Sejahtera`
53. Pilih Target `SUBS-20260101-A1B2C`
54. Pilih Type `Concurrent User`
55. Isi Additional Quantity `10`
56. Klik `[Submit]`
57. Catat Allocation ID baris baru sebagai `{idCU}` (tidak ada pada baseline langkah 49)
58. Pulihkan jam server dan jam browser ke waktu nyata
59. Ketik Search `{idCU}`, tekan Enter
60. Klik row action `Allocation Log` pada baris `{idCU}`
61. Verifikasi judul entri `Allocation created by Dewi A`
62. Verifikasi Description entri memuat `Product: FAMS`, `License Type: Concurrent User`, `Target: SUBS-20260101-A1B2C`, `Quantity: +10`, `Cost: $100.00 (Wallet)`
63. Verifikasi entri memuat Date & Time sesuai General Settings
64. Verifikasi baris judul berupa teks biasa, bukan badge
65. Tutup modal Allocation Log
66. Klik `(←)` pada kotak Search, lalu catat baseline Allocation ID baris di halaman pertama tab Current

### Alokasi Completed langsung hanya punya entri created (TC-AC-LA-409)

67. Klik `[+ Allocation]`
68. Pilih Client `PT Sejahtera`
69. Pilih Target `SUBS-20260101-A1B2C`
70. Pilih Type `Concurrent User`
71. Isi Additional Quantity `1`
72. Klik `[Submit]`
73. Catat Allocation ID baris baru sebagai `{idOne}` (tidak ada pada baseline langkah 66)
74. Ketik Search `{idOne}`, tekan Enter
75. Klik row action `Allocation Log` pada baris `{idOne}`
76. Verifikasi Allocation Log `{idOne}` memuat tepat satu entri `Allocation created by Dewi A`
77. Verifikasi Allocation Log `{idOne}` tidak memuat entri `Allocation approved`
78. Tutup modal Allocation Log
79. Klik `(←)` pada kotak Search, lalu catat baseline Allocation ID baris di halaman pertama tab Current

### Allocation created: Asset Control Station dan Storage (TC-AC-LA-519)

80. Klik `[+ Allocation]`
81. Pilih Client `Klinik Harapan Bunda`
82. Pilih Target `Client-wide`
83. Pilih Type `Asset Control Station`
84. Isi Additional Quantity `10`
85. Klik `[Submit]`
86. Catat Allocation ID baris baru sebagai `{idStation}` (tidak ada pada baseline langkah 79)
87. Ketik Search `{idStation}`, tekan Enter
88. Klik row action `Allocation Log` pada baris `{idStation}`
89. Verifikasi judul entri `Allocation created by Dewi A`
90. Verifikasi Description entri memuat `License Type: Asset Control Station`, `Target: Client-wide`, `Quantity: +10`, `Cost: $500.00 (Wallet)`
91. Verifikasi Description entri tidak memuat baris `Product`
92. Tutup modal Allocation Log
93. Klik `(←)` pada kotak Search, lalu catat baseline Allocation ID baris di halaman pertama tab Current
94. Klik `[+ Allocation]`
95. Pilih Client `Klinik Harapan Bunda`
96. Pilih Target `Client-wide`
97. Pilih Type `Storage`
98. Isi Additional Quantity `50`
99. Klik `[Submit]`
100. Catat Allocation ID baris baru sebagai `{idStorage}` (tidak ada pada baseline langkah 93)
101. Ketik Search `{idStorage}`, tekan Enter
102. Klik row action `Allocation Log` pada baris `{idStorage}`
103. Verifikasi judul entri `Allocation created by Dewi A`
104. Verifikasi Description entri memuat `License Type: Storage`, `Target: Client-wide`, `Quantity: +50 GB`, `Cost: $100.00 (Wallet)`
105. Verifikasi Description entri tidak memuat baris `Product`
106. Tutup modal Allocation Log

### Allocation created: Asset Control App tanpa baris Quantity (TC-AC-LA-520)

107. Nonaktifkan alokasi `Active` Asset Control App Pre-setup #53 pada `SUBS-20260105-K2L3M` lewat fixture backend hingga tersimpan
108. Klik `(←)` pada kotak Search, lalu catat baseline Allocation ID baris di halaman pertama tab Current
109. Klik `[+ Allocation]`
110. Pilih Client `CV Mitra Sejati`
111. Pilih Target `SUBS-20260105-K2L3M`
112. Pilih Type `Asset Control App`
113. Klik `[Submit]`
114. Catat Allocation ID baris baru sebagai `{idApp}` (tidak ada pada baseline langkah 108)
115. Ketik Search `{idApp}`, tekan Enter
116. Klik row action `Allocation Log` pada baris `{idApp}`
117. Verifikasi judul entri `Allocation created by Dewi A`
118. Verifikasi Description entri memuat `Product: SAMS`, `License Type: Addon (Asset Control App)`, `Target: SUBS-20260105-K2L3M`, `Cost: $150.00 (Wallet)`
119. Verifikasi Description entri tidak memuat baris `Quantity`
120. Tutup modal Allocation Log

## Notes

- Alasan di atas sekitar 35 langkah (120 langkah; enam langkah baseline Allocation ID dan langkah pengosongan kotak search sesudah pindah tab ikut menambah hitungan): seluruh blok satu topik (isi Allocation Log per event aksi requester Dewi Anggraini), satu kelas harness fungsional, dan masing-masing memakai record sendiri sehingga berdiri sendiri. Langkah yang diulang adalah pengisian form Allocate per Type (lima kali) dan pembukaan modal Allocation Log per record; blok baca-log berpola (buka modal, `Verifikasi` isi entri) tidak dihitung pada ambang smell.
- Urutan blok mengikuti kebutuhan toggle (ON untuk TC-AC-LA-404, 405, dan 410, lalu OFF untuk TC-AC-LA-401, 409, 519, dan 520) dan berbeda dari urutan sourceTc agar toggle hanya diubah satu kali.
- Asersi absence pada langkah 77, 91, 105, dan 119 adalah elemen Description pada modal yang sudah terbuka dan memuat entri created pada langkah sebelumnya sebagai anchor positif; bukan kelas g.
- Langkah penghubung (S-03, R-16): langkah 5 dan 15 dan 32 (menunggu aksi selesai sesudah `[Save]`, `[Cancel Request]`, dan `[Submit]` Resubmit karena langkah berikutnya membuka modal atau berpindah tab pada List yang sama, 8b butir 8; langkah 5 menjamin entri `Allocation edited` sudah tercatat sebelum Allocation Log dibuka), langkah 1, 12, 18, 29, 36, 42, 59, 74, 87, 101, dan 115 (Search baris berdasarkan Allocation ID), langkah 11, 23, 39, 45, 65, 78, 92, 106, dan 120 (menutup modal), langkah 16, 24, 27, 33, 40, 47 (pindah tab), langkah 17, 25, 28, 34, 41, 48 (mengosongkan kotak search tab tujuan secara eksplisit: klik `✕` pada Search lalu Enter; spec tidak mengandalkan apakah kotak Search terbawa atau ter-reset sesudah pindah tab), langkah 46 (menyetel toggle), langkah 107 (menonaktifkan #53 untuk blok TC-AC-LA-520), langkah 50 dan 58 (mengatur dan memulihkan jam), langkah 26, 49, 66, 79, 93, dan 108 (baseline Allocation ID baris di halaman pertama tab Current sebelum tiap `[Submit]`, S-12, pola spec 042; kotak Search dikosongkan lebih dulu agar baris baru tampil), langkah 35 (mencatat `{idResub}` pada tab dan kondisi Search yang sama dengan baseline langkah 26, dan baris baru diambil dari Allocation ID yang tidak ada pada baseline), dan langkah 57, 73, 86, 100, dan 114 (mencatat Allocation ID baris baru sebagai `{idCU}`, `{idOne}`, `{idStation}`, `{idStorage}`, dan `{idApp}` setelah `[Submit]`; dasar pencatatan adalah baseline langkah sebelumnya).
- Temuan untuk QA:
  - TC-AC-LA-520 mengalokasikan Asset Control App ke `SUBS-20260105-K2L3M` CV Mitra Sejati, sedangkan Pre-setup #53 sudah men-seed alokasi `Active` Asset Control App pada Subscription yang sama (opsi App ke Subscription yang sama diblokir); Submit hanya berhasil bila #53 tidak ada. TC tidak menyebut penyingkiran #53; spec menonaktifkannya lewat fixture backend yang disediakan tim FE/BE (langkah 107) dan memulihkannya di hook `after`. Pembacaan #53 sebagai baca-saja di Pre-setup diselesaikan lewat pengecualian S-06 (2026-10-30) yang dicatat di Prerequisites dan State global spec ini.
  - TC-AC-LA-404 menyebut Cost snapshot $30.00 per unit sedangkan Product Price Concurrent User adalah $365 per unit per tahun (Pre-setup #34); spec memakai snapshot seed $30.00 per unit sehingga Cost $240.00.
  - TC-AC-LA-401 menyebut `Product: FAMS` tanpa menjelaskan sumbernya; spec mengikuti TC.
  - TC-AC-LA-519 tidak menyebut tanggal acuan server; Cost Station dan Storage bukan prorata sehingga jam tidak diatur pada blok itu.
  - TC-AC-LA-409, 519, dan 520 tidak menyebut Allocation ID record baru; spec mencatat ID setelah Submit.

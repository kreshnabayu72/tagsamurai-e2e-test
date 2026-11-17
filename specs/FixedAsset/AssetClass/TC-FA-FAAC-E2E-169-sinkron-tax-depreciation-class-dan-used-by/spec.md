---
id: TC-FA-FAAC-E2E-169-sinkron-tax-depreciation-class-dan-used-by
title: "Sinkronisasi Tax Depreciation Class: Kolom Fiscal, Opsi Select, dan Modal Used By"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-568
  - TC-FA-FAAC-569
  - TC-FA-FAAC-650
  - TC-FA-FAAC-651
  - TC-FA-FAAC-652
sourceRules: ["S-15", "S-14", "§4.1.2#r14", "FAAC-LOGIC-02e"]
smoke: []
dependsOn: []
trace:
  "S-15": [14, 23, 40, 41, 60, 63, 80, 81]
  "S-14": [88, 91]
  "§4.1.2#r14": [100, 101]
  "FAAC-LOGIC-02e": 101
coverage:
  web: automated
---

# Sinkronisasi Tax Depreciation Class: Kolom Fiscal, Opsi Select, dan Modal Used By

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-FISC` memakai `Bukan bangunan – Kelompok 2`; `B-S22` Active memakai `Bukan bangunan – Kelompok 1` tanpa Asset Name; Asset Name tanpa Asset Class `Forklift 3T` (6 aset aktif); `HEAVY-EQ` (Tax Depreciation Class `Bukan bangunan – Kelompok 3`) memiliki Asset Name `Wheel Loader` (4 aset aktif); `MACHINERY` (Tax Depreciation Class `Bukan bangunan – Kelompok 2`); `OFFICE-NEW` (`Office Equipment (New)`, Tax Depreciation Class `Bukan bangunan – Kelompok 1`); `Crane Rental Unit` (0 aset aktif) disetel fixture BE ter-assign ke `OFFICE-NEW` untuk blok TC-652 (lihat butir Keadaan awal dinamis).
- Keadaan awal dinamis: `Crane Rental Unit` ter-assign ke `OFFICE-NEW` menurut precondition TC-652 (bersama TC-83 dan TC-84); fixture BE menyetelnya pada langkah pertama blok TC-652 dan memulihkan keadaan semula sesudah spec (hook `after`), karena TC lain (TC-34, TC-35, TC-270 sampai TC-281, TC-441 sampai TC-466) memerlukan `Crane Rental Unit` pada keadaan awal yang berbeda.
- Nilai form Create valid TC-569 (TC menulis Create `B-S15` tanpa nilai field lain; dipakai set Data Uji valid TC-FA-FAAC-262, dengan Tax Depreciation Class mengikuti TC-569): Class Code `B-S15`; Class Name `Sync Fifteen`; Method `Straight Line`; Useful Life `96`; Depreciation Start Convention `Full month from in-service date`; Tax Depreciation Class `Bukan bangunan – Kelompok 1`; Tax Method `Declining Balance`; Tax Depreciation Start Rule `Month of expenditure`.
- Move pada TC-651 memakai Effective From bulan berjalan menurut zona waktu General Settings (NC-11); jam server dan jam browser tidak digeser spec ini.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: Tax Depreciation Class `Bukan bangunan – Kelompok 2` kembali ke nama dan status Active seed (blok TC-568 diletakkan terakhir karena mengubahnya, S-10); B-S15 dihapus; Forklift 3T, Wheel Loader, dan Crane Rental Unit kembali ke keadaan awal semula.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-569: Create dan Delete Asset Class menghitung ulang Used By pada Tax Depreciation Class

1. Klik tab `Tax Depreciation Class`
2. Buka modal Used By baris `Bukan bangunan – Kelompok 1`
3. Catat Used By (U0)
4. Tutup modal Used By
5. Klik tab `Asset Class`
6. Klik `+ Asset Class`
7. Isi tab General: Class Code `B-S15` dan Class Name `Sync Fifteen`
8. Klik tab `Depreciation`, lalu isi Method `Straight Line`, Useful Life `96`, Depreciation Start Convention `Full month from in-service date`, Tax Depreciation Class `Bukan bangunan – Kelompok 1`, Tax Method `Declining Balance`, dan Tax Depreciation Start Rule `Month of expenditure`
9. Klik `Submit`
10. Tunggu aksi selesai
11. Klik breadcrumb `Asset Class`
12. Klik tab `Tax Depreciation Class`
13. Buka modal Used By baris `Bukan bangunan – Kelompok 1`
14. Verifikasi Used By bertambah satu dari U0
15. Tutup modal Used By
16. Klik tab `Asset Class`
17. Ketik Search `B-S15`, tekan Enter
18. Klik ikon `⋯` pada baris `B-S15`, lalu pilih `Delete`
19. Klik `Delete` pada dialog konfirmasi
20. Tunggu aksi selesai
21. Klik tab `Tax Depreciation Class`
22. Buka modal Used By baris `Bukan bangunan – Kelompok 1`
23. Verifikasi Used By berkurang satu kembali ke U0
24. Tutup modal Used By

### TC-FA-FAAC-650: Assign Asset Name menambah jumlah Asset Name pada modal Used By saat modal dibuka

25. Klik tab `Tax Depreciation Class`
26. Buka modal Used By baris `Bukan bangunan – Kelompok 1`
27. Catat Used By (U0) dan jumlah Asset Name pada baris Asset Class `B-S22` (N0)
28. Tutup modal Used By
29. Klik tab `Asset Class`
30. Klik (←) pada kotak Search
31. Klik link Class Code `B-S22` di tabel
32. Klik tab `Asset Names`
33. Klik tombol `+ Assign Asset Names`
34. Centang `Forklift 3T`
35. Klik `[Assign]`
36. Tunggu aksi selesai
37. Klik breadcrumb `Asset Class`
38. Klik tab `Tax Depreciation Class`
39. Buka modal Used By baris `Bukan bangunan – Kelompok 1` (kunjungan berikutnya)
40. Verifikasi Used By tetap U0 (jumlah Asset Class berbeda tidak berubah)
41. Verifikasi jumlah Asset Name pada baris `B-S22` bertambah satu menjadi N0 + 1, sudah berubah saat modal dibuka tanpa aksi hitung ulang khusus
42. Tutup modal Used By

### TC-FA-FAAC-651: Move Asset Name menggeser jumlah Asset Name antara dua Asset Class pada modal Used By

43. Klik tab `Tax Depreciation Class`
44. Buka modal Used By baris `Bukan bangunan – Kelompok 3`
45. Catat jumlah Asset Name pada baris `HEAVY-EQ` (K3a)
46. Tutup modal Used By
47. Buka modal Used By baris `Bukan bangunan – Kelompok 2`
48. Catat jumlah Asset Name pada baris `MACHINERY` (K2a)
49. Tutup modal Used By
50. Klik tab `Asset Class`
51. Ketik Search `HEAVY-EQ`, tekan Enter
52. Klik link Class Code `HEAVY-EQ` di tabel
53. Klik tab `Asset Names`
54. Klik ikon `⋯` pada baris `Wheel Loader`, lalu pilih `Move`
55. Pilih `Destination Asset Class` `MACHINERY – Machinery`, biarkan Effective From bulan berjalan, lalu klik `[Move]`
56. Tunggu aksi selesai
57. Klik breadcrumb `Asset Class`
58. Klik tab `Tax Depreciation Class`
59. Buka modal Used By baris `Bukan bangunan – Kelompok 3`
60. Verifikasi jumlah Asset Name pada baris `HEAVY-EQ` berkurang satu menjadi K3a - 1, sudah berubah saat modal dibuka tanpa aksi hitung ulang khusus
61. Tutup modal Used By
62. Buka modal Used By baris `Bukan bangunan – Kelompok 2`
63. Verifikasi jumlah Asset Name pada baris `MACHINERY` bertambah satu menjadi K2a + 1, sudah berubah saat modal dibuka tanpa aksi hitung ulang khusus
64. Tutup modal Used By

### TC-FA-FAAC-652: Unassign Asset Name mengurangi jumlah Asset Name pada modal Used By dan tidak mengubah Used By

65. Setel keadaan awal lewat fixture BE: `Crane Rental Unit` ter-assign ke `OFFICE-NEW` (precondition TC-652)
66. Klik tab `Tax Depreciation Class`
67. Buka modal Used By baris `Bukan bangunan – Kelompok 1`
68. Catat Used By (U0) dan jumlah Asset Name pada baris `OFFICE-NEW` (N0)
69. Tutup modal Used By
70. Klik tab `Asset Class`
71. Ganti isi kotak search dengan `OFFICE-NEW`, tekan Enter
72. Klik link Class Code `OFFICE-NEW` di tabel
73. Klik tab `Asset Names`
74. Klik ikon `⋯` pada baris `Crane Rental Unit`, lalu pilih `Unassign`
75. Klik `[Unassign]` pada dialog
76. Tunggu aksi selesai
77. Klik breadcrumb `Asset Class`
78. Klik tab `Tax Depreciation Class`
79. Buka modal Used By baris `Bukan bangunan – Kelompok 1`
80. Verifikasi Used By tetap U0 (OFFICE-NEW masih memakai Tax Depreciation Class tersebut)
81. Verifikasi jumlah Asset Name pada baris `OFFICE-NEW` berkurang satu menjadi N0 - 1, sudah berubah saat modal dibuka tanpa aksi hitung ulang khusus
82. Tutup modal Used By

### TC-FA-FAAC-568: Perubahan Tax Depreciation Class tercermin di kolom Fiscal dan opsi Select

83. Klik tab `Tax Depreciation Class`
84. Ubah nama `Bukan bangunan – Kelompok 2` menjadi `Bukan bangunan – Kelompok 2 Uji` (nama baru dari fixture)
85. Tunggu aksi selesai
86. Klik tab `Asset Class`
87. Ganti isi kotak search dengan `B-FISC`, tekan Enter
88. Verifikasi kolom Fiscal baris `B-FISC` menampilkan nama baru `Bukan bangunan – Kelompok 2 Uji`
89. Klik link Class Code `B-FISC` di tabel
90. Klik tab `Depreciation`
91. Verifikasi Tax Depreciation Class terpilih `B-FISC` tetap `Bukan bangunan – Kelompok 2 Uji` (Asset Class yang sudah memakainya tetap memakainya)
92. Kembali ke tabel Asset Class lewat Breadcrumb
93. Klik tab `Tax Depreciation Class`
94. Nonaktifkan `Bukan bangunan – Kelompok 2 Uji`
95. Tunggu aksi selesai
96. Klik tab `Asset Class`
97. Klik `+ Asset Class`
98. Klik tab `Depreciation`
99. Buka Select Tax Depreciation Class
100. Verifikasi sedikitnya satu opsi Tax Depreciation Class Active tampil pada Select
101. Verifikasi opsi `Bukan bangunan – Kelompok 2 Uji` (Inactive) tidak ditawarkan pada Select
102. Tutup Select tanpa memilih
103. Kembali ke tabel Asset Class lewat Breadcrumb

## Notes

1. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 17, 30, 51, 71, dan 86 (Search kode untuk menemukan baris target, R-16: tabel Asset Class memuat lebih dari 25 baris; isi kotak Search bertahan antar-tab (TC-415) sehingga langkah 30 mengosongkannya sebelum link `B-S22` dicari; langkah 51 mengetik pada kotak kosong, langkah 71 dan 86 mengganti isi kotak yang masih berisi Search sebelumnya), langkah 6 sampai 9 (mengisi form Create dan `Submit` dari TC-569 yang hanya menyebut Create `B-S15`; nilai di Prerequisites), langkah "Tunggu aksi selesai" sesudah aksi tulis yang hasilnya tidak diasersi langsung sebelum pindah tab, pindah tab, langkah 11, 37, 57, dan 77 (kembali ke tabel lewat breadcrumb `Asset Class` dari Detail), langkah 65 (fixture BE menyetel keadaan awal dinamis TC-652), pencatatan nilai awal (U0, N0, K3a, K2a) sebelum aksi sebagai baseline untuk asersi selisih, dan pembukaan serta penutupan modal Used By.
2. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
3. Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah karena lima TC sinkronisasi Tax Depreciation Class yang tiap bloknya berstate sendiri dan mengulang pola buka-modal; semua TC satu topik dan tiap blok berdiri sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
4. Temuan untuk QA: (a) TC-568 menulis "ubah nama atau nonaktifkan"; spec melakukan keduanya berurutan (ubah nama untuk Expected a, nonaktifkan untuk Expected b) dan nama baru berasal dari fixture. (b) TC-568 tidak menyebut dialog konfirmasi nonaktifkan; TC-569 tidak menyebut dialog konfirmasi Delete; spec menulis `Delete` pada dialog. (c) TC-569 tidak menyebut nilai Used By awal; spec mencatat U0 sebelum Create. (e) TC-569 menulis Create `B-S15` tanpa nilai field wajib; spec memakai nilai di Prerequisites (Data Uji TC-FA-FAAC-262, Tax Depreciation Class dari TC-569). (d) Expected a TC-568 "Nama baru tampil di ketiga tempat" pada Asset Class lain (pada TC-560) bukan bagian TC ini.
5. Urutan blok (S-10, S-09): blok TC-568 diletakkan terakhir karena mengubah nama lalu menonaktifkan `Bukan bangunan – Kelompok 2` yang dipakai blok TC-651 (perubahan nama dan status itu dipulihkan fixture BE di hook `after`).
6. Keadaan awal dinamis (S-14): langkah 65 menyetel `Crane Rental Unit` ter-assign ke `OFFICE-NEW` lewat fixture BE sebagai precondition TC-652; langkah ini bukan bagian TC dan tanpa `Verifikasi`.
7. Setelah `Submit` pada Create dan setelah aksi Assign, Move, atau Unassign di Detail, halaman tetap di Detail mode Edit (PRD asset-class.md; TC-75, TC-259 b); tab `Tax Depreciation Class` hanya bisa diklik dari halaman Accounting, sehingga langkah 11, 37, 57, dan 77 kembali ke tabel lewat breadcrumb `Asset Class` lebih dulu.

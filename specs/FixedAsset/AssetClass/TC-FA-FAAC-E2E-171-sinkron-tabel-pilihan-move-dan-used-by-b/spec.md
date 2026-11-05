---
id: TC-FA-FAAC-E2E-171-sinkron-tabel-pilihan-move-dan-used-by-b
title: "Sinkronisasi Versi, Status Active, dan Kunci Periode ke Assign, Pilihan Move, dan Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-562
  - TC-FA-FAAC-563
  - TC-FA-FAAC-564
  - TC-FA-FAAC-566
  - TC-FA-FAAC-586
coverage:
  web: automated
---

# Sinkronisasi Versi, Status Active, dan Kunci Periode ke Assign, Pilihan Move, dan Log

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-ASSETS4` dipakai aset; `B-IN11` Inactive; `B-FREE13` Active tanpa Asset Name; Asset Class Active `Heavy Equipment` (`HEAVY-EQ`) memiliki Asset Name `Wheel Loader`; `B-SYNC10` belum pernah diposting dan diekspor (Active); Asset Class Active `Spare Class` (`SPARE-EQ`) tanpa Asset Name; `Machinery` (`MACHINERY`) memiliki Asset Name `Pump Set`.
- Kemampuan baca log yang disediakan tim FE/BE: jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Kemampuan teknis: fixture BE untuk memicu seed posting dan export periode (NC-16) dan kemampuan baca versi Asset Class (disediakan tim FE/BE, tanpa endpoint karangan).
- Jam server dan jam browser sinkron dan tidak digeser spec ini; bulan berjalan M mengikuti zona waktu General Settings client (NC-11). Kolom Date entri log dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: B-ASSETS4 kembali tanpa versi Scheduled; B-IN11 kembali Inactive; B-FREE13 kembali Active; B-SYNC10 kembali belum pernah diposting dan diekspor; SPARE-EQ kembali Active.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-562: Penerapan versi estimasi tercermin pada Alert, log, dan Capitalization Threshold

1. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
2. Klik link Class Code `B-ASSETS4` di tabel
3. Klik tab `Depreciation`
4. Ubah Capitalization Threshold menjadi `9000000`
5. Klik `Save`
6. Pada dialog `Apply Changes` pilih Effective From dua bulan sesudah bulan berjalan (M+2), lalu klik `Apply`
7. Tunggu aksi selesai
8. Kembali ke tabel Asset Class lewat Breadcrumb
9. Klik link Class Code `B-ASSETS4` di tabel
10. Verifikasi Alert `Next version starts [MMM YYYY].` tampil (bulan M+2)
11. Kembali ke tabel Asset Class lewat Breadcrumb
12. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
13. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
14. Verifikasi baris teratas Changelog: Action `Edit`, Field `Scheduled Version`, Old Value `—`, New Value `[MMM YYYY]` bulan M+2
15. Tutup modal Changelog
16. Verifikasi (lewat kemampuan baca versi Asset Class yang disediakan tim FE/BE) versi Capitalization Threshold `9000000` berlaku pada pendaftaran aset sejak Effective From

### TC-FA-FAAC-563: Activate membuat Asset Class dapat menerima Assign dan muncul di pilihan Destination Asset Class

17. Buka Fixed Asset > Settings > Accounting > tab Asset Class
18. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
19. Aktifkan `B-IN11` lewat toggle Active, lalu klik `Activate` pada dialog
20. Tunggu aksi selesai
21. Klik link Class Code `B-IN11` di tabel
22. Klik tab `Asset Names`
23. Klik tombol `+ Assign Asset Names`
24. Verifikasi dialog `Assign Asset Names` terbuka
25. Verifikasi Dialog Blok D-20 `Asset Class Unavailable` tidak tampil
26. Klik `[Cancel]` pada dialog Assign
27. Kembali ke tabel Asset Class lewat Breadcrumb
28. Ketik Search `HEAVY-EQ`, tekan Enter
29. Klik link Class Code `HEAVY-EQ` di tabel
30. Klik tab `Asset Names`
31. Klik ikon `⋯` pada baris `Wheel Loader`, lalu pilih `Move`
32. Buka daftar `Destination Asset Class`
33. Verifikasi `B-IN11` tersedia pada daftar `Destination Asset Class` di dialog Move
34. Klik `[Cancel]` pada dialog Move
35. Kembali ke tabel Asset Class lewat Breadcrumb
36. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
37. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
38. Verifikasi baris teratas Changelog: Action `Edit`, Class Code `B-IN11`, Field `Status`, Old Value `Inactive`, New Value `Active`
39. Tutup modal Changelog
40. Buka Global Settings > User > Detail User milik aktor > Tab System Log
41. Verifikasi jumlah entri System Log bertambah tepat 1 dari Ns
42. Verifikasi baris teratas System Log: Action `Edit`, Object `Asset Class`, Name `B-IN11`, Field `Status`
43. Buka Activity Log FAMS
44. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari Na
45. Verifikasi baris teratas Activity Log: Action `Edit`, Object `Asset Class`, Name `B-IN11`, Field `Status`

### TC-FA-FAAC-564: Deactivate membuat Assign ditolak D-20 dan menyembunyikannya dari pilihan Destination Asset Class

46. Buka Fixed Asset > Settings > Accounting > tab Asset Class
47. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
48. Nonaktifkan `B-FREE13` lewat toggle Active, lalu klik `Deactivate` pada dialog `Deactivate Asset Class`
49. Tunggu aksi selesai
50. Klik link Class Code `B-FREE13` di tabel
51. Klik tab `Asset Names`
52. Klik tombol `+ Assign Asset Names`
53. Verifikasi Dialog Blok tampil: Title `Asset Class Unavailable`, Body memuat `This asset class is inactive. Activate it first.`, tombol `[OK]`
54. Klik `[OK]` pada dialog
55. Verifikasi dialog Assign tidak dibuka (tab Asset Names `B-FREE13` tetap tampil)
56. Kembali ke tabel Asset Class lewat Breadcrumb
57. Ketik Search `HEAVY-EQ`, tekan Enter
58. Klik link Class Code `HEAVY-EQ` di tabel
59. Klik tab `Asset Names`
60. Klik ikon `⋯` pada baris `Wheel Loader`, lalu pilih `Move`
61. Buka daftar `Destination Asset Class`
62. Verifikasi sedikitnya satu opsi Asset Class Active tampil pada daftar `Destination Asset Class`
63. Verifikasi `B-FREE13` tidak tersedia pada daftar `Destination Asset Class` (Asset Class Inactive tidak ditawarkan)
64. Klik `[Cancel]` pada dialog Move
65. Kembali ke tabel Asset Class lewat Breadcrumb
66. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
67. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
68. Verifikasi baris teratas Changelog: Action `Edit`, Class Code `B-FREE13`, Field `Status`, Old Value `Active`, New Value `Inactive`
69. Tutup modal Changelog
70. Buka Global Settings > User > Detail User milik aktor > Tab System Log
71. Verifikasi jumlah entri System Log bertambah tepat 1 dari Ns
72. Verifikasi baris teratas System Log: Action `Edit`, Object `Asset Class`, Name `B-FREE13`, Field `Status`
73. Buka Activity Log FAMS
74. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari Na
75. Verifikasi baris teratas Activity Log: Action `Edit`, Object `Asset Class`, Name `B-FREE13`, Field `Status`

### TC-FA-FAAC-566: Last Posted Period terisi mengunci Class Code, Guard 1, dan memicu reklasifikasi

76. Buka Fixed Asset > Settings > Accounting > tab Asset Class
77. Catat jumlah entri Changelog (Nc) dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
78. Picu seed posting dan export untuk `B-SYNC10` (Active, belum pernah diposting) lewat fixture BE
79. Tunggu aksi selesai
80. Kembali ke tabel Asset Class lewat Breadcrumb
81. Klik link Class Code `B-SYNC10` di tabel
82. Verifikasi Class Code Disabled
83. Arahkan kursor ke field Class Code
84. Verifikasi tooltip kunci Class Code tampil
85. Kembali ke tabel Asset Class lewat Breadcrumb
86. Klik ikon `⋯` pada baris `B-SYNC10`, lalu pilih `Delete`
87. Verifikasi Dialog Blok D-05 tampil
88. Tutup Dialog Blok D-05
89. Klik link Class Code `B-SYNC10` di tabel
90. Klik tab `Accounts`
91. Ganti Asset Cost `B-SYNC10` ke akun Asset Cost Active lain
92. Klik `Save`
93. Verifikasi dialog `Reclassify Balances` tampil
94. Klik `Cancel` pada dialog `Reclassify Balances`
95. Kembalikan Asset Cost ke nilai tersimpan
96. Kembali ke tabel Asset Class lewat Breadcrumb
97. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
98. Verifikasi jumlah entri Changelog bertambah tepat 2 dari Nc
99. Verifikasi dua baris teratas Changelog: Field `Last Posted Period` dan Field `Last Exported Period` (L-10 dan L-11) dengan Modified By `System`
100. Tutup modal Changelog
101. Buka Activity Log FAMS
102. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari Na
103. Verifikasi dua baris teratas Activity Log: Field `Last Posted Period` dan Field `Last Exported Period` (L-10 dan L-11) dengan Modified By `System`

### TC-FA-FAAC-586: Menonaktifkan Asset Class tanpa Asset Name menghilangkannya dari pilihan Destination Asset Class

104. Buka Fixed Asset > Settings > Accounting > tab Asset Class
105. Ketik Search `SPARE-EQ`, tekan Enter
106. Nonaktifkan `SPARE-EQ` lewat toggle Active, lalu klik `Deactivate` pada dialog `Deactivate Asset Class`
107. Tunggu aksi selesai
108. Ganti isi kotak search dengan `MACHINERY`, tekan Enter
109. Klik link Class Code `MACHINERY` di tabel
110. Klik tab `Asset Names`
111. Klik ikon `⋯` pada baris `Pump Set`, lalu pilih `Move`
112. Buka daftar `Destination Asset Class`
113. Verifikasi sedikitnya satu opsi Asset Class Active tampil pada daftar `Destination Asset Class`
114. Verifikasi opsi `SPARE-EQ – Spare Class` tidak ada pada daftar `Destination Asset Class`
115. Klik `[Cancel]` pada dialog Move

## Notes

1. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 dan 18 dan awal tiap blok TC (baseline log), langkah 28, 57, 105, dan 108 (Search kode `HEAVY-EQ`, `SPARE-EQ`, dan `MACHINERY` untuk menemukan baris target, R-16: tabel Asset Class memuat lebih dari 25 baris), langkah "Tunggu aksi selesai" sesudah aksi tulis yang hasilnya tidak diasersi langsung sebelum pindah surface (di Detail, versi Scheduled tetap di Detail sehingga kembali ke tabel lewat Breadcrumb ditulis sebagai langkah sendiri), menutup dialog dengan `[Cancel]` atau Dialog Blok, mengembalikan Asset Cost `B-SYNC10` pada TC-566 (S-09, form tidak dibiarkan dirty), dan kembali ke layar awal.
2. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC lewat kemampuan baca log. Entri baru dibaca pada baris teratas urutan default Date terbaru sesudah selisih jumlah dari baseline dibuktikan (S-14); bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah karena blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) yang tidak dihitung menurut bagian 3 smell; semua TC satu topik dan tiap blok TC berdiri sendiri dengan seed dan baseline sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
5. Temuan untuk QA: (a) TC-562 menyebut Expected "versi Capitalization Threshold baru berlaku pada pendaftaran aset" tanpa langkah pendaftaran aset; spec memakai kemampuan baca versi dari tim FE/BE (S-11). (b) TC-566 tidak menyebut teks tooltip kunci dan akun pengganti Asset Cost; spec tidak mengasersi teks tooltip. (c) TC-566 menyebut Expected d (L-10 dan L-11) tanpa langkah membuka Changelog dan Activity Log; spec membukanya sebagai langkah observasi karena Expected memuat entri log. (d) TC-563 memakai Dialog Blok D-20 tanpa menyebut judulnya; spec memakai judul `Asset Class Unavailable` dari TC-564. (e) TC-563 dan TC-564 tidak menyebut dialog konfirmasi toggle Active; spec menulis dialog `Activate` dan `Deactivate Asset Class`. (f) Pasangan TC-536 dan TC-562 sama-sama mengubah versi Scheduled tetapi pada Asset Class berbeda.

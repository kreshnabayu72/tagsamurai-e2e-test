---
id: TC-FA-FAAC-E2E-170-sinkron-tabel-pilihan-move-dan-used-by-a
title: "Sinkronisasi Create, Rename, Delete Asset Class ke Tabel, Pilihan Move, dan Used By Akun"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-559
  - TC-FA-FAAC-560
  - TC-FA-FAAC-565
  - TC-FA-FAAC-583
  - TC-FA-FAAC-588
sourceRules: ["S-01a", "S-01b", "S-01c", "S-01d", "L-01", "§8.2#p1", "§8.3#p1", "S-02a", "S-02b", "S-02c", "§9.2#r4", "ST-23", "S-06a", "S-06b", "S-06c", "S-06e", "L-05", "S-06d", "§4.2c#p1"]
smoke: []
dependsOn: []
trace:
  "S-01a": 15
  "S-01b": 21
  "S-01c": 26
  "S-01d": [30, 34, 37]
  "L-01": 31
  "§8.2#p1": [35, 96]
  "§8.3#p1": [38, 99]
  "S-02a": 45
  "S-02b": [51, 111]
  "S-02c": [56, 123]
  "§9.2#r4": 60
  "ST-23": [73, 141]
  "S-06a": [74, 142]
  "S-06b": [80, 81]
  "S-06c": [86, 137]
  "S-06e": [90, 95, 98]
  "L-05": 91
  "S-06d": 92
  "§4.2c#p1": 118
coverage:
  web: automated
---

# Sinkronisasi Create, Rename, Delete Asset Class ke Tabel, Pilihan Move, dan Used By Akun

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class Active `Heavy Equipment` (`HEAVY-EQ`) memiliki Asset Name `Wheel Loader`; `B-SYNC2` Active dengan akun terpilih, Asset Name, dan entri Changelog lama; `B-DEL4` memakai akun 11001, tanpa Asset Name, belum pernah diposting, dengan entri Create lama di Changelog; `LT-VEH` Active dengan akun Asset Cost `1-2100 – Vehicles Cost`; `MACHINERY` Active dengan Asset Name; `SPARE-EQ2` Active tanpa Asset Name, tanpa Last Posted Period, dengan Asset Cost `1-2100 – Vehicles Cost`.
- Nilai form Create valid TC-559 (TC menulis Create `B-SYNC1` dengan Asset Cost `11001 – Machinery Cost` tanpa nilai field wajib lain; dipakai set Data Uji valid TC-FA-FAAC-262): Class Code `B-SYNC1`; Class Name `Sync One`; Status Active; Method `Straight Line`; Useful Life `96`; Depreciation Start Convention `Full month from in-service date`; Tax Depreciation Class `Bukan bangunan – Kelompok 2`; Tax Method `Declining Balance`; Tax Depreciation Start Rule `Month of expenditure`; Asset Cost `11001 – Machinery Cost`; akun lain mengikuti pre-fill.
- Kemampuan baca log yang disediakan tim FE/BE: jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Jam server dan jam browser sinkron dan tidak digeser spec ini; bulan berjalan M mengikuti zona waktu General Settings client (NC-11). Kolom Date entri log dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: B-SYNC1 dihapus; Class Name B-SYNC2 dan LT-VEH kembali ke nilai seed; B-DEL4 dan SPARE-EQ2 dibuat ulang.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-559: Create Asset Class tercermin di tabel, pilihan Destination Asset Class pada Move, serta Used By akun

1. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
2. Klik tab `Chart of Accounts`
3. Buka popup Used By akun `11001 – Machinery Cost`
4. Catat Used By akun 11001 (U1)
5. Tutup popup Used By
6. Klik tab `Asset Class`
7. Klik `+ Asset Class`
8. Isi tab General: Class Code `B-SYNC1`, Class Name `Sync One`, Status Active
9. Klik tab `Depreciation`, lalu isi Method `Straight Line`, Useful Life `96`, Depreciation Start Convention `Full month from in-service date`, Tax Depreciation Class `Bukan bangunan – Kelompok 2`, Tax Method `Declining Balance`, dan Tax Depreciation Start Rule `Month of expenditure`
10. Klik tab `Accounts`, lalu pilih Asset Cost `11001 – Machinery Cost` (akun lain mengikuti pre-fill)
11. Klik `Submit`
12. Tunggu aksi selesai
13. Klik breadcrumb `Asset Class`
14. Ketik Search `B-SYNC1`, tekan Enter
15. Verifikasi baris `B-SYNC1` tampil di tabel
16. Ganti isi kotak search dengan `HEAVY-EQ`, tekan Enter
17. Klik link Class Code `HEAVY-EQ` di tabel
18. Klik tab `Asset Names`
19. Klik ikon `⋯` pada baris `Wheel Loader`, lalu pilih `Move`
20. Buka daftar `Destination Asset Class`
21. Verifikasi `B-SYNC1 – Sync One` tersedia pada daftar `Destination Asset Class` di dialog Move
22. Klik `[Cancel]` pada dialog Move
23. Kembali ke tabel Asset Class lewat Breadcrumb
24. Klik tab `Chart of Accounts`
25. Buka popup Used By akun `11001 – Machinery Cost`
26. Verifikasi Used By akun 11001 bertambah satu dari U1 dan memuat `B-SYNC1`
27. Tutup popup Used By
28. Klik tab `Asset Class`
29. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
30. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
31. Verifikasi baris teratas Changelog: Action `Create`, Class Code `B-SYNC1`
32. Tutup modal Changelog
33. Buka Global Settings > User > Detail User milik aktor > Tab System Log
34. Verifikasi jumlah entri System Log bertambah tepat 1 dari Ns
35. Verifikasi baris teratas System Log: Action `Create`, Object `Asset Class`, Name `B-SYNC1`
36. Buka Activity Log FAMS
37. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari Na
38. Verifikasi baris teratas Activity Log: Action `Create`, Object `Asset Class`, Name `B-SYNC1`

### TC-FA-FAAC-560: Rename Asset Class tercermin di tabel, pilihan Move, dan popup Used By

39. Buka Fixed Asset > Settings > Accounting > tab Asset Class
40. Klik link Class Code `B-SYNC2` di tabel
41. Ubah Class Name menjadi `Sync Renamed`
42. Klik `Save`
43. Tunggu aksi selesai
44. Ketik Search `B-SYNC2`, tekan Enter
45. Verifikasi baris `B-SYNC2` di tabel menampilkan Class Name `Sync Renamed`
46. Ganti isi kotak search dengan `HEAVY-EQ`, tekan Enter
47. Klik link Class Code `HEAVY-EQ` di tabel
48. Klik tab `Asset Names`
49. Klik ikon `⋯` pada baris `Wheel Loader`, lalu pilih `Move`
50. Buka daftar `Destination Asset Class`
51. Verifikasi `B-SYNC2 – Sync Renamed` tampil pada daftar `Destination Asset Class` di dialog Move
52. Klik `[Cancel]` pada dialog Move
53. Kembali ke tabel Asset Class lewat Breadcrumb
54. Klik tab `Chart of Accounts`
55. Buka popup Used By akun Chart of Accounts yang dipakai `B-SYNC2`
56. Verifikasi popup Used By memuat Class Name `Sync Renamed` untuk `B-SYNC2`
57. Tutup popup Used By
58. Klik tab `Asset Class`
59. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
60. Verifikasi entri Changelog lama untuk `B-SYNC2` (dari seed) tetap menampilkan Class Code `B-SYNC2` tanpa perubahan
61. Tutup modal Changelog

### TC-FA-FAAC-565: Delete menghitung ulang Used By dan menghapus Asset Class dari dropdown

62. Buka Fixed Asset > Settings > Accounting > tab Asset Class
63. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
64. Klik tab `Chart of Accounts`
65. Buka popup Used By akun `11001 – Machinery Cost`
66. Catat Used By akun 11001 (U1)
67. Tutup popup Used By
68. Klik tab `Asset Class`
69. Ketik Search `B-DEL4`, tekan Enter
70. Klik ikon `⋯` pada baris `B-DEL4` (memakai akun 11001), lalu pilih `Delete`
71. Klik `Delete` pada dialog konfirmasi
72. Ganti isi kotak search dengan `B-DEL4`, tekan Enter
73. Verifikasi empty state `No results found` tampil
74. Verifikasi `B-DEL4` tidak ada di tabel
75. Ganti isi kotak search dengan `HEAVY-EQ`, tekan Enter
76. Klik link Class Code `HEAVY-EQ` di tabel
77. Klik tab `Asset Names`
78. Klik ikon `⋯` pada baris `Wheel Loader`, lalu pilih `Move`
79. Buka daftar `Destination Asset Class`
80. Verifikasi sedikitnya satu opsi lain tampil pada daftar `Destination Asset Class`
81. Verifikasi `B-DEL4` tidak ada di dropdown `Destination Asset Class`
82. Klik `[Cancel]` pada dialog Move
83. Kembali ke tabel Asset Class lewat Breadcrumb
84. Klik tab `Chart of Accounts`
85. Buka popup Used By akun `11001 – Machinery Cost`
86. Verifikasi Used By akun 11001 berkurang satu dari U1
87. Tutup popup Used By
88. Klik tab `Asset Class`
89. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
90. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
91. Verifikasi baris teratas Changelog: Action `Delete`, Class Code `B-DEL4`
92. Verifikasi entri Changelog lama `B-DEL4` (Create dari seed) tetap tampil
93. Tutup modal Changelog
94. Buka Global Settings > User > Detail User milik aktor > Tab System Log
95. Verifikasi jumlah entri System Log bertambah tepat 1 dari Ns
96. Verifikasi baris teratas System Log: Action `Delete`, Object `Asset Class`, Name `B-DEL4`
97. Buka Activity Log FAMS
98. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari Na
99. Verifikasi baris teratas Activity Log: Action `Delete`, Object `Asset Class`, Name `B-DEL4`

### TC-FA-FAAC-583: Mengubah Class Name tercermin di dialog Assign dan Move serta popup Used By

100. Buka Fixed Asset > Settings > Accounting > tab Asset Class
101. Ketik Search `LT-VEH`, tekan Enter
102. Klik link Class Code `LT-VEH` di tabel
103. Ubah Class Name menjadi `Light Vehicles Fleet`
104. Klik `[Save]`
105. Tunggu aksi selesai
106. Ganti isi kotak search dengan `MACHINERY`, tekan Enter
107. Klik link Class Code `MACHINERY` di tabel
108. Klik tab `Asset Names`
109. Klik ikon `⋯` pada satu baris Asset Name, lalu pilih `Move`
110. Buka daftar `Destination Asset Class`
111. Verifikasi opsi `LT-VEH – Light Vehicles Fleet` tampil pada daftar `Destination Asset Class`
112. Klik `[Cancel]` pada dialog Move
113. Kembali ke tabel Asset Class lewat Breadcrumb
114. Ganti isi kotak search dengan `LT-VEH`, tekan Enter
115. Klik link Class Code `LT-VEH` di tabel
116. Klik tab `Asset Names`
117. Klik tombol `+ Assign Asset Names`
118. Verifikasi judul dialog `Assign Asset Names to Light Vehicles Fleet`
119. Klik `[Cancel]` pada dialog Assign
120. Kembali ke tabel Asset Class lewat Breadcrumb
121. Klik tab `Chart of Accounts`
122. Buka popup Used By akun `1-2100 – Vehicles Cost`
123. Verifikasi popup Used By mencantumkan nama baru `Light Vehicles Fleet`
124. Tutup popup Used By

### TC-FA-FAAC-588: Menghapus Asset Class tanpa Asset Name menghitung ulang Used By akun dan menghilangkannya dari pilihan Move

125. Buka Fixed Asset > Settings > Accounting > tab Asset Class
126. Klik tab `Chart of Accounts`
127. Buka popup Used By akun `1-2100 – Vehicles Cost`
128. Catat Used By akun `1-2100 – Vehicles Cost` (U1)
129. Tutup popup Used By
130. Klik tab `Asset Class`
131. Ketik Search `SPARE-EQ2`, tekan Enter
132. Klik ikon `⋯` pada baris `SPARE-EQ2`, lalu pilih `Delete`
133. Klik `Delete` pada dialog konfirmasi
134. Tunggu aksi selesai
135. Klik tab `Chart of Accounts`
136. Buka popup Used By akun `1-2100 – Vehicles Cost`
137. Verifikasi Used By akun `1-2100 – Vehicles Cost` berkurang satu Asset Class dari U1
138. Tutup popup Used By
139. Klik tab `Asset Class`
140. Ganti isi kotak search dengan `SPARE-EQ2`, tekan Enter
141. Verifikasi empty state `No results found` tampil
142. Verifikasi `SPARE-EQ2` tidak ada lagi di tabel Asset Class

## Notes

1. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 14, 16, 44, 46, 69, 72, 75, 101, 106, 114, 131, dan 140 (Search kode untuk menemukan baris target, R-16: tabel Asset Class memuat lebih dari 25 baris), langkah 7 sampai 11 (mengisi form Create dan `Submit` dari TC-559 yang hanya menyebut Create `B-SYNC1`; nilai di Prerequisites), langkah "Tunggu aksi selesai" sesudah aksi tulis yang hasilnya tidak diasersi langsung sebelum pindah surface atau tab, pindah tab, langkah 13 (kembali ke tabel lewat breadcrumb `Asset Class` dari Detail sesudah `Submit`), pencatatan Used By awal (U1) sebelum aksi sebagai baseline selisih, pembukaan dan penutupan popup Used By serta dialog Move dan Assign, dan baseline log pada TC-559 dan TC-565.
2. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC lewat kemampuan baca log. Entri baru dibaca pada baris teratas urutan default Date terbaru sesudah selisih jumlah dari baseline dibuktikan (S-14); bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah karena lima TC sinkronisasi yang tiap bloknya mengulang pola buka-dialog Move dan popup Used By serta blok baca-log berpola (bagian 3 smell); semua TC satu topik dan tiap blok berdiri sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
5. Temuan untuk QA: (a) Expected a TC-560 menulis "ketiga tempat dan di tabel" tetapi LK hanya memeriksa tabel, dialog Move, dan popup Used By; spec mengasersi ketiga tempat itu saja. (b) Expected b TC-560 menyebut berkas export tanpa langkah export di LK; spec hanya mengasersi entri Changelog lama dan tidak mengasersi berkas export. (c) TC-560 tidak menyebut akun yang dipakai B-SYNC2 dan entri Changelog lama; spec menambahkannya di Prerequisites. (d) TC-559 menyebut Class Name B-SYNC1 tidak ada dan tidak menyebut nilai field wajib lain; spec memakai `Sync One` dan nilai di Prerequisites (Data Uji TC-FA-FAAC-262). (e) TC-583 tidak menyebut Asset Name yang dipilih pada dialog Move; spec memakai satu baris Asset Name `MACHINERY`. (f) Penutupan dialog dengan `[Cancel]` ditulis sebagai langkah penghubung.
6. Isi kotak Search tabel Asset Class bertahan antar-tab (TC-415): langkah 72 dan 140 mengganti isi kotak yang masih berisi Search sebelumnya (`B-DEL4`, `SPARE-EQ2`), bukan mengetik pada kotak kosong.
7. Setelah `Submit` pada Create halaman tetap di Detail mode Edit (PRD asset-class.md; TC-75, TC-259 b), sehingga langkah 13 kembali ke tabel lewat breadcrumb `Asset Class` sebelum Search `B-SYNC1`.

---
id: TC-GS-UCF-E2E-063-changelog-filter-dropdown-chip-dan-logika
title: "Modal Changelog Custom Field: Screening Filter Panel, Opsi Dropdown, Chip, Filter Date Action Field Modified By, Logika AND, dan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-261
  - TC-GS-UCF-262
  - TC-GS-UCF-518
  - TC-GS-UCF-263
  - TC-GS-UCF-264
  - TC-GS-UCF-265
  - TC-GS-UCF-412
  - TC-GS-UCF-519
  - TC-GS-UCF-520
  - TC-GS-UCF-266
  - TC-GS-UCF-521
  - TC-GS-UCF-522
  - TC-GS-UCF-361
  - TC-GS-UCF-356
coverage:
  web: automated
---

# Modal Changelog Custom Field: Screening Filter Panel, Opsi Dropdown, Chip, Filter Date Action Field Modified By, Logika AND, dan Empty State

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client A Sari Dewi (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; `## Test Steps` tidak mengulang langkah buka.
- Data Pre-setup (baca-saja, tidak diubah spec ini): 6 Custom Field Pre-setup Client A dan Changelog Pre-setup 8 entri bertanggal 8 sampai 11 Sep 2026 (fixture backend): Edit `Cost Center` Value Setting `Finance, Operations` ke `Finance, Operations, Marketing` (Budi S, 11 Sep), Create `Cost Center` (Budi S, 11 Sep), Activate `Employee Grade` Status (Siti R, 10 Sep), Deactivate `Joining Date` Status (Budi S, 9 Sep), Delete `Legacy Field` (Siti R, 8 Sep), Create `Job Description` (Siti R, 10 Sep), Create `Bonus` (Budi S, 9 Sep), Create `Office Phone` (Budi S, 9 Sep). Akun `Maya P` (Read Only) tidak pernah mengubah apa pun.
- Data Population (precondition TC): 8 Custom Field Population (`Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number`) dibuat lewat API oleh Sari Dewi di hook `before` bila belum ada (seeding idempotent; menghasilkan 8 entri Create, Modified By `Sari D`); dipakai sebagai precondition TC.
- General Settings Client A: Date Format `DDD, MMM dd, yyyy`, Time Format `hh:mm a` (nilai default fixture, tidak diubah spec ini).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: date range picker pada Filter Date; dropdown multi-select searchable dengan chip; hover untuk tooltip.
- State global: tidak ada yang diubah selain flag Guided Tooltip.

## Test Steps

### TC-GS-UCF-261: Screening Filter Panel Modal Changelog

1. Klik icon Changelog
2. Klik Filter
3. Verifikasi field `Date` berupa date range dengan placeholder `Select date`
4. Verifikasi field `Action` berupa multi-select searchable dengan placeholder `All actions`
5. Verifikasi field `Field` berupa multi-select searchable dengan placeholder `All fields`
6. Verifikasi field `Modified By` berupa multi-select searchable dengan placeholder `All users`
7. Verifikasi `[Clear Field]` tampil
8. Verifikasi `[Apply]` tampil

### TC-GS-UCF-264: Opsi filter di-populate dari entri log yang ada

9. Buka dropdown Action
10. Verifikasi opsi Action memuat `Create`, `Edit`, `Delete`, `Activate`, `Deactivate`
11. Buka dropdown Modified By
12. Verifikasi opsi Modified By memuat `Budi S`, `Siti R`, `Sari D`
13. Verifikasi opsi Modified By tidak memuat `Maya P`

### TC-GS-UCF-521: Search di dalam dropdown Filter mempersempit opsi

14. Buka dropdown Field, ketik `status`
15. Verifikasi opsi Field hanya `Employee Grade — Status` dan `Joining Date — Status`
16. Buka dropdown Modified By, ketik `sar`
17. Verifikasi opsi Modified By hanya `Sari D`
18. Verifikasi pencarian internal tidak memfilter tabel Changelog sebelum `[Apply]` (sedikitnya satu entri Create tampil di tabel)

### TC-GS-UCF-266: Chip filter: Search dalam dropdown, hapus lewat (✕), dan uncheck

19. Klik `[Clear Field]`
20. Buka dropdown Action, ketik `cre`
21. Verifikasi pencarian `cre` mempersempit opsi menjadi `Create`
22. Pilih `Create`, lalu hapus ketikan, pilih `Edit`
23. Verifikasi dua chip `Create` dan `Edit` di dalam field Action
24. Klik `(✕)` pada chip `Edit`
25. Verifikasi chip `Edit` terhapus
26. Verifikasi opsi `Edit` ter-uncheck
27. Verifikasi chip `Create` tetap
28. Pilih `Edit` lagi, buka dropdown, uncheck `Create`
29. Verifikasi chip `Create` terhapus

### TC-GS-UCF-361: Chip Field dan Modified By: hapus lewat (✕), uncheck, dan logika OR dalam field

30. Klik `[Clear Field]`
31. Buka dropdown Field, pilih `Cost Center — Value Setting` dan `Employee Grade — Status`, klik `(✕)` pada chip `Cost Center — Value Setting`
32. Verifikasi chip `Cost Center — Value Setting` terhapus
33. Verifikasi opsinya (`Cost Center — Value Setting`) ter-uncheck
34. Verifikasi chip `Employee Grade — Status` tetap
35. Buka dropdown Modified By, pilih `Budi S` dan `Siti R`, lalu uncheck `Budi S` di dalam dropdown
36. Verifikasi chip `Budi S` terhapus
37. Verifikasi chip `Siti R` tetap
38. Klik `[Apply]`
39. Verifikasi entri Activate `Employee Grade` (Modified By `Siti R`) tampil
40. Verifikasi tabel hanya memuat entri Activate `Employee Grade`

### TC-GS-UCF-522: Banyak chip pada field Field diringkas menjadi chip +N more

41. Klik `[Clear Field]`
42. Buka dropdown Field, catat jumlah opsi M, lalu centang satu per satu seluruh opsi
43. Verifikasi chip yang tidak muat diringkas dalam satu chip `+N more`
44. Verifikasi jumlah chip yang tampil ditambah N sama dengan M
45. Verifikasi field Field tidak melebar keluar panel
46. Klik `[Clear Field]`

### TC-GS-UCF-356: Opsi Field memuat field yang sudah dihapus

47. Buka dropdown Field, ketik `Legacy`
48. Verifikasi opsi `Legacy Field` tampil walau field sudah dihapus
49. Klik `[Clear Field]`

### TC-GS-UCF-263: Filter Changelog per Field

50. Buka dropdown Field
51. Verifikasi opsi Field memuat teks berprefiks nama field: `Cost Center — Value Setting`, `Employee Grade — Status`, `Joining Date — Status`
52. Pilih `Cost Center — Value Setting`, klik `[Apply]`
53. Verifikasi entri Edit `Cost Center — Value Setting` tampil
54. Verifikasi tabel hanya memuat entri Edit Value Setting Cost Center

### TC-GS-UCF-262: Filter Changelog per Date, Action, dan Modified By

55. Klik `[Clear Field]`
56. Pilih Date 8 Sep 2026 sampai 11 Sep 2026, klik `[Apply]`
57. Verifikasi tabel memuat 8 entri Pre-setup
58. Tambah Action `Create`, klik `[Apply]`
59. Verifikasi tabel memuat empat entri Create Pre-setup: `Cost Center`, `Job Description`, `Bonus`, `Office Phone`
60. Kosongkan Action, pilih Modified By `Siti R`, klik `[Apply]`
61. Verifikasi tabel memuat entri Activate `Employee Grade`
62. Verifikasi tabel memuat entri Delete `Legacy Field`
63. Verifikasi tabel memuat entri Create `Job Description`
64. Verifikasi tabel hanya memuat ketiga entri tersebut

### TC-GS-UCF-518: Filter Date satu hari menampilkan entri hari itu saja

65. Klik `[Clear Field]`
66. Pilih Date 10 Sep 2026 sampai 10 Sep 2026, klik `[Apply]`
67. Verifikasi entri Activate `Employee Grade — Status` tampil
68. Verifikasi entri Create `Job Description` tampil
69. Verifikasi tabel hanya memuat dua entri tersebut
70. Verifikasi input Date menampilkan tanggal sesuai Date Format General Settings

### TC-GS-UCF-265: Kombinasi filter berlogika AND dan Search lalu Filter

71. Klik `[Clear Field]`
72. Pilih Date 8 Sep 2026 sampai 11 Sep 2026, klik `[Apply]`
73. Pilih Action `Edit` dan Modified By `Budi S`, klik `[Apply]`, lalu klik icon Filter untuk menutup panel
74. Ketik Search `Value`, tekan Enter
75. Verifikasi satu entri tampil: Edit `Cost Center — Value Setting`
76. Klik Filter
77. Verifikasi filter tetap aktif setelah Search (chip Date, Action `Edit`, dan Modified By `Budi S` pada panel Filter)

### TC-GS-UCF-412: Empty state hasil Filter tanpa Search

78. Klik icon Filter untuk menutup panel, lalu klik `(←)` pada kotak Search
79. Klik Filter, klik `[Clear Field]`
80. Pilih Action `Activate`
81. Pilih Modified By `Budi S`
82. Klik `[Apply]`
83. Verifikasi Illustration tampil
84. Verifikasi Title `No results found`
85. Verifikasi Description `Try adjusting your search or filter.`
86. Verifikasi tabel Changelog tidak menampilkan baris
87. Verifikasi Search tetap kosong

### TC-GS-UCF-519: Search lalu Filter menghasilkan irisan dan keyword tetap terisi

88. Klik `[Clear Field]`
89. Pilih Date 8 Sep 2026 sampai 11 Sep 2026, klik `[Apply]`, lalu klik icon Filter untuk menutup panel
90. Ketik Search `Create`, tekan Enter
91. Verifikasi hanya entri Action `Create` tampil
92. Verifikasi tabel memuat empat entri Create Pre-setup: `Cost Center`, `Job Description`, `Bonus`, `Office Phone`
93. Klik Filter, pilih Modified By `Siti R`, klik `[Apply]`, lalu klik icon Filter untuk menutup panel
94. Verifikasi entri Create `Job Description` (Modified By `Siti R`) tampil
95. Verifikasi tabel hanya memuat entri Create `Job Description`
96. Verifikasi keyword `Create` tetap terisi di kotak Search

### TC-GS-UCF-520: Pelepasan Search dan Filter saling independen dan empty state pulih

97. Klik `(←)` pada kotak Search
98. Klik Filter, klik `[Clear Field]`, klik `[Apply]`, lalu klik icon Filter untuk menutup panel
99. Ketik Search `Create`, tekan Enter
100. Klik Filter, pilih Modified By `Siti R`, klik `[Apply]`, lalu klik icon Filter untuk menutup panel
101. Verifikasi entri Create `Job Description` tampil
102. Verifikasi tabel hanya memuat entri Create `Job Description`
103. Kosongkan isi kotak search, tekan Enter
104. Verifikasi filter Modified By `Siti R` tetap aktif
105. Verifikasi tabel memuat entri Activate `Employee Grade — Status`
106. Verifikasi tabel memuat entri Delete `Legacy Field`
107. Verifikasi tabel memuat entri Create `Job Description`
108. Verifikasi tabel hanya memuat ketiga entri tersebut
109. Ketik Search `Marketing`, tekan Enter
110. Verifikasi empty state `No results found`
111. Verifikasi `Try adjusting your search or filter.`
112. Klik Filter, klik `[Clear Field]`, klik `[Apply]`, lalu klik icon Filter untuk menutup panel
113. Verifikasi keyword `Marketing` tetap terisi
114. Verifikasi entri Edit `Cost Center — Value Setting` tampil
115. Klik `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 261, 264, 521, 266, 361, 522, 356, 263, 262, 518, 265, 412, 519, 520. Urutan menyimpang dari urutan TC sumber: kasus yang hanya memanipulasi dropdown dan chip tanpa `[Apply]` (264, 521, 266, 361 sebelum Apply, 522, 356) dikerjakan lebih dulu pada satu pembukaan panel Filter, lalu kasus `[Apply]` dari yang paling sederhana ke kombinasi (263, 262, 518, 265, 412, 519, 520). Modal dibuka sekali (langkah 1) dan ditutup sekali (langkah 115).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka modal), langkah 2 (membuka Filter), langkah 19, 30, 41, 46, 49, 55, 65, 71, 79, 88, 98, dan 112 (`[Clear Field]` dan `[Apply]` untuk memulihkan filter sebelum TC berikutnya, S-09), langkah 78 dan 97 (`(←)` pada kotak Search untuk mereset Search sebelum TC berikutnya), langkah 76 (membuka Filter Panel untuk mengamati chip pada langkah 77), langkah 115 (menutup modal lewat `[✕]`, tanpa dialog karena tidak ada form).
- Asersi "hanya entri ..." (langkah 40, 54, 64, 69, 95, 102, 108) selalu didahului `Verifikasi` entri yang dicari tampil sebagai pembanding (bagian 8b butir 2); empty state langkah 83 sampai 87 dan 110 adalah anchor positif.
- Model Filter Panel (keputusan K-10 A, 2026-10-29): panel tetap terbuka sesudah `[Apply]` (konsisten dengan TC-GS-UCF-211, 213, dan 262 yang langsung "Tambah Action ..., [Apply]" tanpa membuka ulang). Karena itu langkah sesudah `[Apply]` yang memakai panel yang sama tidak mengklik Filter lagi (langkah 41, 55, 58, 60, 65, 71, 88), dan `[Apply]` yang diikuti aksi di luar panel (Search, `(←)`, penutupan modal) ditutup lewat klik icon Filter (langkah 73, 89, 93, 98, 100, 112; langkah 78 menggabung penutupan panel dengan `(←)`). Pola ini sama dengan spec 052 dan 053. TC-GS-UCF-265, 412, 519, 520 menulis "Klik Filter" yang dapat berarti membuka ulang panel; perlu konfirmasi QA/PRD.
- Nama field dan entri `Legacy Field` pada opsi Field (TC-GS-UCF-356) berasal dari entri Delete Pre-setup.
- Spec melewati sekitar 35 langkah (115 langkah). Seluruhnya satu kelas (Filter Panel Modal Changelog, hanya membaca, satu dataset Pre-setup); seluruh blok memakai panel Filter yang sama dan dibersihkan lewat `[Clear Field]` di antara blok, sehingga membukanya per TC tidak diperlukan. Tiap blok `[Apply]` berdiri sendiri; kegagalan keras satu blok (panel tidak terbuka) memang menghilangkan blok berikutnya, tetapi blok-blok itu tetap satu topik satu dataset (bagian 3 prinsip 1) dan dipisah dari Search, Sort, dan Setup Column (spec 062, 064, 065).
- Temuan untuk QA:
  - TC-GS-UCF-522 dan 519 (K-11 A, 2026-10-29) tidak lagi memakai total absolut: 522 mencatat jumlah opsi Field M dan mengasersi chip + N sama dengan M; 519 membatasi Filter Date 8 sampai 11 Sep 2026 lebih dulu sehingga hanya 4 entri Create Pre-setup. TC-GS-UCF-264 dan 521 masih bergantung pada opsi Modified By `Budi S`, `Siti R`, `Sari D` dan opsi Field berakhiran `— Status`; entri baru dari spec lain (audit trail permanen) dapat menambah opsi Field, tetapi tidak mengubah asersi 521 (`status` hanya cocok dua opsi bila tidak ada Deactivate/Activate lain).
  - TC-GS-UCF-522 (setelah perbaikan) tidak mematok 16 opsi; spec mencatat jumlah opsi M dari dropdown Field.
  - TC-GS-UCF-262 dan 265 menuliskan Date `8 Sep 2026 sampai 11 Sep 2026` tanpa menyatakan format tampilan date picker; spec mengikuti nilai Data Uji.
  - TC-GS-UCF-265 Expected b "Filter tetap aktif setelah Search" tidak menyebut bagaimana filter aktif teramati; spec memeriksa chip pada panel Filter.
  - TC-GS-UCF-412 Expected b menyebut "Search tetap kosong" tanpa Search diketik di TC; spec memeriksa kotak Search kosong sesudah `[Apply]`.
  - TC-GS-UCF-266 langkah 5 ("Pilih `Edit` lagi, buka dropdown, uncheck `Create`") tidak menyatakan state setelah langkah 4 secara eksplisit; spec mengikuti urutan langkah TC.

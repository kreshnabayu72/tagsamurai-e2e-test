---
id: TC-GS-POS-E2E-040-changelog-filter-dropdown-chip-dan-logika
title: "Popup Changelog: Filter Date, Dropdown Multi-select, Sinkronisasi Chip, Overflow, Logika AND/OR, dan Opsi dari Entri Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-211
  - TC-GS-POS-212
  - TC-GS-POS-213
  - TC-GS-POS-214
  - TC-GS-POS-215
  - TC-GS-POS-216
  - TC-GS-POS-217
  - TC-GS-POS-219
  - TC-GS-POS-220
coverage:
  web: automated
---

# Popup Changelog: Filter Date, Dropdown Multi-select, Sinkronisasi Chip, Overflow, Logika AND/OR, dan Opsi dari Entri Log

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
  - Manage user and role Create-Only (Sari Dewi) `manageUserRoleCreate_automated_{namaCompany}@qwertysystem.net` (Pre-setup 5), hanya untuk seeding lewat API di hook `before` (Create `Procurement Analyst`), dengan `Spectra.env.GS_CREATE_PASSWORD`. Tidak dipakai login UI.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position (sidebar Global Settings, sub-tab Position). Spec ini tidak menguji navigasi sehingga `## Test Steps` tidak mengulang langkah buka.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix): Position 15 `Field Technician` (dibuat via Import Type "Position", tanpa entri Changelog; dipakai TC-GS-POS-212); user Pre-setup 17 `Rina Wulandari` (tidak pernah menjadi aktor log Position; dipakai TC-GS-POS-212).
- Data Dinamis (di-seed lewat API di hook `before` pada entitas Total Control; nama bersuffix per run; fixture baru `Fixture.position.changelogSeed040`), dalam urutan seeding:
  - Oleh Budi Santoso: Create `IT Support Specialist {runId}-040`, Edit menjadi `IT Operations Lead {runId}-040`, Create `Temporary Staff {runId}-040`, Delete `Temporary Staff {runId}-040`.
  - Oleh Sari Dewi (terakhir): Create `Procurement Analyst {runId}-040`.
  - Entri Changelog hasil seeding bersifat audit trail permanen dan tidak dibersihkan; Changelog entitas juga memuat entri dari spec lain sehingga asersi memakai entri bersuffix `-040` sebagai penanda.
- Entri Date bukan hari ini (TC-GS-POS-213, precondition d): disediakan tim FE/BE, satu entri Changelog Position bersuffix `{runId}-040` dengan Date bukan hari ini pada entitas Total Control, dipakai pada langkah 27. Entri ini tidak dibuat atau dibersihkan spec; mekanisme penyediaannya tidak ditetapkan di TC, PRD, atau LLD (lihat Temuan untuk QA).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-040` yang masih ada (`IT Operations Lead`, `Procurement Analyst`).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- M (TC-GS-POS-217): jumlah seluruh opsi Position Name pada filter Popup Changelog, yaitu jumlah nama Position berbeda pada Changelog entitas. Karena Changelog entitas juga memuat entri spec lain, M tidak diturunkan dari seeding spec ini saja; M dihitung langkah 96 dari opsi yang dicentang.
- Kemampuan teknis: seeding lewat API dengan sesi Budi dan Sari; pembacaan chip, centang opsi, teks sel tabel Changelog, dan tanggal hari ini dalam format General Settings (Pre-setup 22).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan seperti di atas).

## Test Steps

### TC-GS-POS-211: Screening Filter Panel Popup Changelog

1. Klik ikon Changelog
2. Verifikasi User > Position > Popup Changelog: Position terbuka
3. Klik ikon Filter
4. Verifikasi Filter Panel memuat field berurutan `Date`, `Action`, `Position Name`, `Modified By`
5. Verifikasi field `Date` berupa date range picker dengan placeholder "Select date"
6. Verifikasi field `Action` berupa multi-select searchable dengan placeholder "All actions"
7. Verifikasi field `Position Name` berupa multi-select searchable dengan placeholder "All positions"
8. Verifikasi field `Modified By` berupa multi-select searchable dengan placeholder "All users"
9. Verifikasi tidak ada field filter `Field`
10. Verifikasi tombol `[Clear Field]` tampil di kiri
11. Verifikasi tombol `[Apply]` tampil di kanan

### TC-GS-POS-212: Isi opsi dropdown filter berasal dari entri log

12. Buka dropdown `Action`
13. Verifikasi opsi `Action` hanya `Create`, `Edit`, dan `Delete`
14. Tutup dropdown `Action` dengan menekan Esc
15. Buka dropdown `Position Name`
16. Verifikasi opsi `Position Name` memuat `Temporary Staff {runId}-040` (sudah dihapus)
17. Verifikasi opsi `Position Name` tidak memuat opsi `Field Technician` (tanpa entri log)
18. Tutup dropdown `Position Name` dengan menekan Esc
19. Buka dropdown `Modified By`
20. Verifikasi opsi `Modified By` memuat aktor yang tercatat `Budi S`
21. Verifikasi opsi `Modified By` memuat aktor yang tercatat `Sari D`
22. Verifikasi opsi `Modified By` tidak memuat `Rina W` (user platform tanpa entri log)
23. Tutup dropdown `Modified By` dengan menekan Esc

### TC-GS-POS-213: Filter Date

24. Pilih rentang Date hari ini saja pada field `Date`
25. Klik `[Apply]`
26. Verifikasi tabel memuat entri seed hari ini (`Procurement Analyst {runId}-040` Create)
27. Verifikasi entri Changelog bersuffix `{runId}-040` ber-Date bukan hari ini (disediakan tim FE/BE) tidak tampil
28. Verifikasi setiap baris yang tampil memiliki Date hari ini (inklusif)

### TC-GS-POS-214: Filter kelas multi-select, search internal, dan OR

29. Klik ikon Filter
30. Klik `[Clear Field]`
31. Klik `[Apply]`
32. Klik ikon Filter
33. Ketik `De` di search dropdown `Action`
34. Verifikasi search dropdown mempersempit opsi `Action` ke `Delete`
35. Centang `Delete`
36. Hapus keyword search dropdown `Action`
37. Centang `Create`
38. Verifikasi field `Action` memuat chip `Delete`
39. Verifikasi field `Action` memuat chip `Create`
40. Verifikasi field `Action` memuat tepat 2 chip
41. Klik `[Apply]`
42. Verifikasi tabel memuat baris Delete `Temporary Staff {runId}-040` dan baris Create `Procurement Analyst {runId}-040`
43. Verifikasi setiap baris yang tampil dengan Action `Create` atau `Delete`
44. Klik ikon Filter
45. Klik `[Clear Field]`
46. Klik `[Apply]`
47. Klik ikon Filter
48. Ketik `Temp` di search dropdown `Position Name`
49. Centang `Temporary Staff {runId}-040`
50. Hapus keyword search dropdown `Position Name`
51. Centang `Procurement Analyst {runId}-040`
52. Klik `[Apply]`
53. Verifikasi tabel memuat baris `Temporary Staff {runId}-040` dan baris `Procurement Analyst {runId}-040`
54. Verifikasi setiap baris yang tampil bernama `Temporary Staff {runId}-040` atau `Procurement Analyst {runId}-040`
55. Klik ikon Filter
56. Klik `[Clear Field]`
57. Klik `[Apply]`
58. Klik ikon Filter
59. Centang `Budi S` pada dropdown `Modified By`
60. Centang `Sari D` pada dropdown `Modified By`
61. Klik `[Apply]`
62. Verifikasi tabel memuat baris oleh `Budi S` dan baris oleh `Sari D`
63. Verifikasi setiap baris yang tampil dimodifikasi oleh `Budi S` atau `Sari D`

### TC-GS-POS-215: Hapus chip via ✕ menyinkronkan checkbox opsi

64. Klik ikon Filter
65. Klik `[Clear Field]`
66. Klik `[Apply]`
67. Klik ikon Filter
68. Centang `Create` dan `Delete` pada dropdown `Action`
69. Tutup dropdown `Action` dengan menekan Esc
70. Klik `✕` pada chip `Create` tanpa membuka dropdown
71. Verifikasi chip `Create` hilang
72. Verifikasi chip `Delete` tetap
73. Buka dropdown `Action`
74. Verifikasi checkbox `Create` ter-uncheck
75. Verifikasi checkbox `Delete` tetap tercentang
76. Klik `[Apply]`
77. Verifikasi tabel memuat baris Delete `Temporary Staff {runId}-040`
78. Verifikasi setiap baris yang tampil dengan Action `Delete`

### TC-GS-POS-216: Uncheck opsi di dalam dropdown menghapus chip

79. Klik ikon Filter
80. Klik `[Clear Field]`
81. Klik `[Apply]`
82. Klik ikon Filter
83. Centang `Create` dan `Delete` pada dropdown `Action`
84. Tutup dropdown `Action` dengan menekan Esc
85. Buka dropdown `Action`
86. Hilangkan centang `Delete`
87. Verifikasi chip `Delete` hilang dari field
88. Verifikasi chip `Create` tetap
89. Klik `[Apply]`
90. Verifikasi tabel memuat baris Create `Procurement Analyst {runId}-040`
91. Verifikasi setiap baris yang tampil dengan Action `Create`

### TC-GS-POS-217: Overflow chip filter Position Name

92. Klik ikon Filter
93. Klik `[Clear Field]`
94. Klik `[Apply]`
95. Klik ikon Filter
96. Centang seluruh opsi pada dropdown `Position Name` satu per satu dari atas daftar, hitung jumlah opsi yang dicentang M
97. Verifikasi chip yang muat ditampilkan
98. Verifikasi sisanya diringkas dalam chip `+N more`
99. Verifikasi jumlah chip yang tampil ditambah N sama dengan M
100. Verifikasi field tidak melebar keluar panel

### TC-GS-POS-219: Kombinasi field filter berbeda memakai logika AND

101. Klik `[Clear Field]`
102. Klik `[Apply]`
103. Klik ikon Filter
104. Pilih `Create` pada dropdown `Action`
105. Pilih `Sari D` pada dropdown `Modified By`
106. Klik `[Apply]`
107. Verifikasi tabel memuat baris `Procurement Analyst {runId}-040`
108. Verifikasi setiap baris yang tampil dengan Action `Create` dan dimodifikasi oleh `Sari D`

### TC-GS-POS-220: Search dan Filter dalam dua urutan menghasilkan irisan sama

109. Klik ikon Filter
110. Klik `[Clear Field]`
111. Klik `[Apply]`
112. Ketik Search `Operations`, tekan Enter
113. Klik ikon Filter
114. Pilih `Edit` pada dropdown `Action`
115. Klik `[Apply]`
116. Catat baris hasil urutan pertama (Search lalu Filter)
117. Klik ikon Filter
118. Klik `[Clear Field]`
119. Klik `[Apply]`
120. Kosongkan isi kotak search dengan klik `✕`, tekan Enter
121. Klik ikon Filter
122. Pilih `Edit` pada dropdown `Action`
123. Klik `[Apply]`
124. Ketik Search `Operations`, tekan Enter
125. Verifikasi tabel memuat baris Edit dengan New Value `IT Operations Lead {runId}-040`
126. Verifikasi baris hasil urutan kedua (Filter lalu Search) identik dengan baris hasil urutan pertama
127. Verifikasi setiap baris yang tampil dengan Action `Edit` dan mengandung `Operations`
128. Kosongkan isi kotak search dengan klik `✕`, tekan Enter
129. Klik ikon Filter
130. Klik `[Clear Field]`
131. Klik `[Apply]`
132. Tutup Popup Changelog dengan klik `✕` di header

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 211, 212, 213, 214, 215, 216, 217, 219, 220 (urutan numerik TC sumber). Popup Changelog dibuka sekali (langkah 1) dan ditutup sekali (langkah 132); tidak ada form yang dibuka.
- Langkah penghubung (aksi tanpa `Verifikasi`): pembukaan dan penutupan dropdown (langkah 14, 18, 23), `[Clear Field]` + `[Apply]` untuk membersihkan filter antar-TC (langkah 29 sampai 31, 44 sampai 46, 55 sampai 57, 64 sampai 66, 79 sampai 81, 92 sampai 94, 101 sampai 102, 109 sampai 111, 117 sampai 119, 129 sampai 131), pengosongan Search (langkah 120 dan 128), penutupan Popup Changelog (langkah 132), dan pencatatan hasil/jumlah (langkah 96 dan 116). Langkah 69 dan 84 (Esc) adalah langkah TC-215/216 sendiri.
- TC-GS-POS-214 langkah 4 dan 5 ("Clear Field + Apply") diterjemahkan menjadi langkah 44 sampai 46 dan 55 sampai 57 sebagai pembersih sebelum Position Name dan Modified By; pembersih sebelum Action (langkah 29 sampai 31) menghapus filter Date dari TC-GS-POS-213.
- Asersi "setiap baris yang tampil" mengacu ke halaman 1 (Date terbaru di atas, urutan default). Entri seed bersuffix `-040` dibuat paling baru dan Sari Dewi terakhir, sehingga berada di halaman 1.
- Asersi tambahan di luar Expected TC (baris pembanding yang mendahului asersi "setiap baris yang tampil" supaya tabel kosong tidak meloloskannya; konvensi 8b butir 2): langkah 26, 42, 53, 62, 77, 90, 107, dan 125 mengasersi tabel memuat baris seed bersuffix `-040` yang sesuai dengan filter. Langkah 77, 90, dan 125 adalah langkah tambahan; pada langkah 26, 42, 53, 62, dan 107 urutannya mendahului asersi "setiap baris" yang ada di Expected TC. Langkah 27 mengasersi absence entri `{runId}-040` ber-Date bukan hari ini (precondition d TC-GS-POS-213); anchor positifnya langkah 26 (entri seed hari ini pada tabel yang sama) dan langkah 27 menyusul sebelum asersi universal "setiap baris yang tampil memiliki Date hari ini" (langkah 28). Langkah 27 adalah asersi tambahan di luar Expected TC-GS-POS-213 yang menegaskan bahwa Filter Date menyaring entri lama. Langkah 17 mengasersi absence opsi `Field Technician` secara eksak (opsi bernama tepat itu); anchor positifnya langkah 16.
- Search ditulis "Ketik Search `X`, tekan Enter" atomik (langkah 112 dan 124; konvensi bagian 8b butir 9). Input Search Popup Changelog tetap terbuka sesudah `✕` (teks dikosongkan, tabel baru mereset setelah Enter); karena itu langkah 120 dan 128 menutup dengan `✕` lalu Enter, dan langkah 124 tidak memerlukan klik ikon Search. TC-GS-POS-220 langkah 3 ("Reset keduanya") diterjemahkan menjadi langkah 117 sampai 120.
- TC-GS-POS-218, 288, 289, dan 290 (sumber opsi dropdown: entitas tanpa Changelog, opsi bertambah setelah Create, Loading, dan Position dihapus) ada di spec 056. Search dan Sort Popup Changelog ada di spec 039 dan 041; Setup Column di spec 042; Download di spec 043.
- Topik satu dataset Changelog (screening 038, Search 039, Filter 040, Sort 041, Setup Column 042, Download 043) dipertahankan sebagai spec terpisah karena gabungan keenamnya melewati batas ukuran jauh dan tiap spec menyiapkan dan membersihkan seeding sendiri, sehingga kegagalan keras satu spec tidak menghilangkan makna spec lain.
- Spec melewati sekitar 35 langkah (132 langkah, sebagian besar pasangan aksi dan `Verifikasi` untuk Filter dan chip). Seluruhnya satu kelas (Filter Popup Changelog di satu modul, satu akun, tanpa aksi yang mengubah data), dan tiap blok TC dimulai dari filter bersih lewat `[Clear Field]` + `[Apply]` sehingga tetap bermakna bila blok lain gagal.
- Temuan untuk QA:
  - TC-GS-POS-213 precondition d mensyaratkan entri Changelog Position ber-Date bukan hari ini tanpa menyebut cara membentuknya; spec menyatakannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-POS-212 poin Expected c menyebut "bukan seluruh user platform" tanpa daftar yang dikecualikan; Changelog entitas bersama dapat memuat aktor lain (mis. `Andi W`). Spec mengasersi `Budi S` dan `Sari D` ada serta `Rina W` (user Pre-setup 17 tanpa entri log) tidak ada. Precondition TC-GS-POS-212 melompati butir d (a, b, c, lalu e).
  - TC-GS-POS-213, 214, 215, 216, 219, 220 tidak menyebut apakah Filter Panel Popup Changelog tertutup sesudah `[Apply]` (TC-GS-POS-160 sampai 170 untuk tabel utama menyatakan Filter Panel tetap terbuka; Popup Changelog tidak disebut); spec membuka Filter lagi dengan klik ikon Filter sebelum tiap pengisian. Spec mengasersi hasil filter pada halaman 1.
  - TC-GS-POS-217 mensyaratkan pencentangan seluruh M opsi tanpa menjamin M cukup besar agar chip meluap; bila seluruh opsi muat dalam lebar field, chip `+N more` tidak muncul dan asersi overflow (langkah 98) tidak teruji. Spec mencentang seluruh opsi dan menghitung M dari opsi yang dicentang.

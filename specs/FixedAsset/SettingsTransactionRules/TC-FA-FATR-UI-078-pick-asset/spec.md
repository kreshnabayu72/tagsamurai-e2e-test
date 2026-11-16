---
id: TC-FA-FATR-UI-078-pick-asset
title: "Dialog Select Asset: kolom dan validasi"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules:
  - "§4.1#r390"
  - "§4.1#r391"
  - "§4.1#r392"
  - "§4.1#r393"
  - "§4.1#r394"
  - "§4.1#r395"
  - "§4.1#r396"
  - "§4.1#r397"
  - "§4.1#p72"
  - "§4.4#r13"
  - "§4.5#b4"
  - "§6#r11"
  - "§7#r16"
  - "AU-BAGIAN-asampaiAU-BAGIAN-o,AU-NILAI-asampaiAU-NILAI-j,AU-TOOLTIP-asampaiAU-TOOLTIP-d"
  - "D-05"
  - "S-08"
  - "§9.5#r2"
  - "§9.5#r29"
  - "§9.9#r23"
  - "EB-TBL-1@select-asset"
  - "EB-TBL-9@select-asset"
  - "EB-FLT-6@select-asset"
smoke: []
dependsOn: []
trace:
  §4.1#r390: [7, 10, 13, 15, 39, 61, 64]
  §4.1#r391: [7, 10, 16, 39, 61]
  §4.1#r392: [7, 10, 17, 19, 20, 22, 39, 43, 45]
  §4.1#r393: [7, 10, 23, 25, 39, 46, 48]
  §4.1#r394: [7, 10, 26, 28, 29, 49, 51]
  §4.1#r395: [7, 10, 30, 32, 33, 52, 54]
  §4.1#r396: [7, 10, 34, 39, 55, 57]
  §4.1#r397: [7, 10, 35, 37, 38, 58, 60]
  §4.1#p72: [8, 10, 11]
  §4.4#r13: [78, 79]
  §4.5#b4: [88, 90]
  §6#r11: 79
  §7#r16: [92, 93]
  "AU-BAGIAN-asampaiAU-BAGIAN-o,AU-NILAI-asampaiAU-NILAI-j,AU-TOOLTIP-asampaiAU-TOOLTIP-d": [2, 17]
  D-05: [5, 85]
  S-08: [97, 98, 109, 110]
  §9.5#r2: [41, 43]
  §9.5#r29: [92, 93]
  §9.9#r23: [79, 81]
  EB-TBL-1@select-asset: [92, 97, 99, 101, 102, 103]
  EB-TBL-9@select-asset: [78, 79]
  EB-FLT-6@select-asset: [72, 74, 75]
anchor: []
coverage:
  web: automated
---

# Dialog Select Asset: kolom dan validasi

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings, Dialog Add override - Borrow yang dibuka dari All categories dengan Scope `Asset`; Dialog Select Asset dibuka dari tombol `[Select Asset]`.
- Komponen: Dialog Select Asset
- Data:
  - DU-078-1: aset Name `Excavator PC200 - 1`, Asset ID `EXC-0001`, Group `Proyek Karawang` (hierarki `Region Jawa > Proyek Karawang`), Category `Machinery` (hierarki `Heavy Equipment > Machinery`), Brand `Komatsu`, Model / Type `PC200`, Status `Active`, Labels `Heavy, Insured, Rental`.
  - DU-078-2: aset Name `Toyota Avanza - 1`, Asset ID `VEH-0001`, Group `Workshop` (hierarki `Region Jawa > Workshop`), Category `Pool car` (hierarki `Vehicle > Pool car`), tanpa Brand, tanpa Model / Type, Status `Active`, tanpa Labels.
  - DU-078-3: aset Name `Excavator PC200 - 2`, Asset ID `EXC-0002`, Group `Jakarta Selatan Distribution Center` (hierarki `Region Jawa > Jakarta Selatan Distribution Center`; badge yang diharapkan `Jakarta Sela..ution Center`, dari nama Group 35 karakter), Category `Machinery` (hierarki `Heavy Equipment > Machinery`), Brand `Komatsu`, Model / Type `PC200`, Status `Active`, Labels `Outdoor`.
  - DU-078-4: kata kunci Search `Zebra Tidak Ada`, tidak cocok dengan baris mana pun.
  - DU-078-5: filter Category `Pool car`, tidak cocok dengan baris mana pun.
- Kondisi:
  - K1: tabel berisi DU-078-1, DU-078-2, dan DU-078-3; belum ada filter yang diterapkan.
  - K2: tidak ada aset.
  - K3: sama dengan K1; respons atas Search DU-078-4 dan atas filter Category DU-078-5 tidak memuat baris.
  - K4: memuat tabel gagal karena error server.

## Test Steps

### Sifat dialog multi-select
1. Tampilkan Dialog Select Asset dengan kondisi K1
2. Verifikasi dialog memuat tabel, ikon Search, tombol filter, dan Filter Panel yang dapat dibuka
3. Centang baris `Excavator PC200 - 1`
4. Centang baris `Toyota Avanza - 1`
5. Verifikasi kedua baris `Excavator PC200 - 1` dan `Toyota Avanza - 1` tercentang sekaligus

### Susunan kolom dan Column Visibility
6. Tampilkan Dialog Select Asset dengan kondisi K1
7. Verifikasi header tabel berurutan dari kiri: checkbox, `Name`, `Asset ID`, `Group`, `Category`, `Brand`, `Model / Type`, `Status`, `Labels`
8. Verifikasi baris tabel tidak memiliki menu aksi baris
9. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
10. Verifikasi daftar Column Visibility memuat kolom `Name`, `Asset ID`, `Group`, `Category`, `Brand`, `Model / Type`, `Status`, `Labels`, seluruhnya tercentang dan tidak disabled
11. Verifikasi daftar Column Visibility tidak memuat baris untuk checkbox seleksi baris

### Format sel
12. Tampilkan Dialog Select Asset dengan kondisi K1
13. Verifikasi sel Name pada baris Asset ID `EXC-0001` berisi `Excavator PC200 - 1` apa adanya
14. Klik sel Name pada baris `Excavator PC200 - 1`
15. Verifikasi sel Name bukan tautan dan klik tidak berpindah halaman
16. Verifikasi sel Asset ID pada baris `Excavator PC200 - 1` berisi `EXC-0001`
17. Verifikasi sel Group pada baris `Excavator PC200 - 1` berisi `Proyek Karawang`
18. Arahkan kursor ke badge Group `Proyek Karawang`
19. Verifikasi hierarki lengkap `Region Jawa > Proyek Karawang` tersampaikan pada badge
20. Verifikasi badge Group pada baris `Excavator PC200 - 2` berisi `Jakarta Sela..ution Center`
21. Arahkan kursor ke badge Group `Jakarta Sela..ution Center`
22. Verifikasi hierarki lengkap `Region Jawa > Jakarta Selatan Distribution Center` tersampaikan pada badge
23. Verifikasi sel Category pada baris `Excavator PC200 - 1` berisi `Machinery`
24. Arahkan kursor ke badge Category `Machinery`
25. Verifikasi hierarki lengkap `Heavy Equipment > Machinery` tersampaikan pada badge
26. Verifikasi sel Brand pada baris `Excavator PC200 - 1` berisi `Komatsu`
27. Arahkan kursor ke badge Brand `Komatsu`
28. Verifikasi nama Brand penuh `Komatsu` tersampaikan pada badge
29. Verifikasi sel Brand pada baris `Toyota Avanza - 1` berisi `—`
30. Verifikasi sel Model / Type pada baris `Excavator PC200 - 1` berisi `PC200`
31. Arahkan kursor ke badge Model / Type `PC200`
32. Verifikasi nama Model / Type penuh `PC200` tersampaikan pada badge
33. Verifikasi sel Model / Type pada baris `Toyota Avanza - 1` berisi `—`
34. Verifikasi sel Status pada baris `Excavator PC200 - 1` berupa badge berisi `Active`
35. Verifikasi sel Labels pada baris `Excavator PC200 - 1` menampilkan dua chip pertama `Heavy` dan `Insured`, lalu `+1 more`
36. Klik `+1 more` pada baris `Excavator PC200 - 1`
37. Verifikasi popover daftar label penuh `Heavy`, `Insured`, dan `Rental`
38. Verifikasi sel Labels pada baris `Toyota Avanza - 1` berisi `—`
39. Verifikasi sel Name, Asset ID, Group, Category, dan Status di setiap baris berisi nilai dan tidak menampilkan `—`

### Field Filter Panel dan default tanpa filter
40. Tampilkan Dialog Select Asset dengan kondisi K1
41. Verifikasi tombol filter tidak menampilkan indikator filter aktif
42. Klik tombol filter di toolbar
43. Verifikasi field filter `Group` berupa multi-select dengan placeholder `All groups`
44. Klik field filter `Group`
45. Verifikasi daftar opsi field `Group` menyediakan kotak pencarian opsi
46. Verifikasi field filter `Category` berupa multi-select dengan placeholder `All categories`
47. Klik field filter `Category`
48. Verifikasi daftar opsi field `Category` menyediakan kotak pencarian opsi
49. Verifikasi field filter `Brand` berupa multi-select dengan placeholder `All brands`
50. Klik field filter `Brand`
51. Verifikasi daftar opsi field `Brand` menyediakan kotak pencarian opsi
52. Verifikasi field filter `Model / Type` berupa multi-select dengan placeholder `All models`
53. Klik field filter `Model / Type`
54. Verifikasi daftar opsi field `Model / Type` menyediakan kotak pencarian opsi
55. Verifikasi field filter `Status` berupa multi-select dengan placeholder `All statuses`
56. Klik field filter `Status`
57. Verifikasi daftar opsi field `Status` menyediakan kotak pencarian opsi
58. Verifikasi field filter `Label` berupa multi-select dengan placeholder `All labels`
59. Klik field filter `Label`
60. Verifikasi daftar opsi field `Label` menyediakan kotak pencarian opsi
61. Verifikasi Filter Panel tidak memuat field filter `Name` dan `Asset ID`

### Placeholder kotak Search
62. Tampilkan Dialog Select Asset dengan kondisi K1
63. Klik ikon Search di toolbar
64. Verifikasi kotak Search memuat placeholder `Search asset name or ID...`

### Menyembunyikan kolom tidak menghapus field filter dan filter ter-Apply
65. Tampilkan Dialog Select Asset dengan kondisi K1
66. Klik tombol filter di toolbar
67. Klik field filter `Brand`
68. Pilih opsi `Komatsu` pada field filter `Brand`
69. Klik `[Apply]`
70. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
71. Hilangkan centang kolom `Brand` pada Column Visibility
72. Verifikasi tabel tidak menampilkan header kolom `Brand`
73. Klik tombol filter di toolbar untuk membuka kembali Filter Panel
74. Verifikasi field filter `Brand` tetap ada pada Filter Panel
75. Verifikasi chip `Komatsu` tetap tampil pada field filter `Brand` dan tombol filter tetap menampilkan indikator filter aktif

### Select tanpa baris terpilih
76. Tampilkan Dialog Select Asset dengan kondisi K1
77. Klik `[Select]`
78. Verifikasi dialog Select Asset tetap terbuka
79. Verifikasi teks `You must pick an asset` tampil di footer, tepat di atas tombol `Select`
80. Centang baris `Excavator PC200 - 1`
81. Verifikasi teks `You must pick an asset` hilang

### Select dengan baris terpilih
82. Tampilkan Dialog Select Asset dengan kondisi K1
83. Centang baris `Excavator PC200 - 1`
84. Klik `[Select]`
85. Verifikasi dialog Select Asset tertutup dan badge `EXC-0001 · Excavator PC200 - 1` tampil di bawah tombol `Select Asset` pada Dialog Add override

### Menutup dialog
86. Tampilkan Dialog Select Asset dengan kondisi K1
87. Klik backdrop di luar dialog
88. Verifikasi dialog Select Asset tetap terbuka
89. Tekan `Esc`
90. Verifikasi dialog Select Asset tertutup

### Empty state belum ada aset
91. Tampilkan Dialog Select Asset dengan kondisi K2
92. Verifikasi judul empty state `No assets yet` tampil
93. Verifikasi deskripsi `Get started by creating your first asset.` tampil

### Empty state hasil Search tanpa hasil
94. Tampilkan Dialog Select Asset dengan kondisi K3
95. Klik ikon Search di toolbar
96. Ketik Search `Zebra Tidak Ada`, tekan Enter
97. Verifikasi judul empty state `No results found` tampil pada tabel Select Asset
98. Verifikasi deskripsi empty state `Try adjusting your search or filter.` tampil pada tabel Select Asset
99. Verifikasi `No assets yet` tidak tampil

### Gagal memuat tabel
100. Tampilkan Dialog Select Asset dengan kondisi K4
101. Verifikasi pesan `Unable to load this data.` tampil pada tabel Select Asset
102. Verifikasi tombol `[Try Again]` tampil pada tabel Select Asset
103. Verifikasi `No assets yet` tidak tampil

### Empty state hasil Filter tanpa hasil
104. Tampilkan Dialog Select Asset dengan kondisi K3
105. Klik tombol filter di toolbar
106. Klik field filter `Category`
107. Pilih opsi `Pool car` pada field filter `Category`
108. Klik `[Apply]`
109. Verifikasi judul empty state `No results found` tampil pada tabel Select Asset sesudah filter
110. Verifikasi deskripsi empty state `Try adjusting your search or filter.` tampil pada tabel Select Asset sesudah filter

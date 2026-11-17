---
id: TC-FA-FATR-UI-077-pick-asset-name
title: "Dialog Select Asset Name: kolom, toolbar, footer, dan validasi"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules:
  - "§4.1#r384"
  - "§4.1#r391"
  - "§4.1#r392"
  - "§4.1#r393"
  - "§4.1#r394"
  - "§4.1#r395"
  - "§4.1#r396"
  - "§4.1#r397"
  - "§4.1#r398"
  - "§4.1#r399"
  - "§4.1#r400"
  - "§4.1#r402"
  - "§4.1#r403"
  - "§4.1#r404"
  - "§4.1#r405"
  - "§4.1#r406"
  - "§4.1#r407"
  - "§4.1#r408"
  - "§4.1#r410"
  - "§4.1#r411"
  - "§4.1#r412"
  - "§4.1#r413"
  - "§4.1#r414"
  - "§4.1#r415"
  - "§4.4#r13"
  - "§4.5#b4"
  - "§6#r11"
  - "§7#r15"
  - "AU-BAGIAN-asampaiAU-BAGIAN-s,AU-NILAI-asampaiAU-NILAI-l,AU-TOOLTIP-asampaiAU-TOOLTIP-f"
  - "D-04"
  - "S-08"
  - "§9.5#r2"
  - "§9.5#r29"
  - "§9.9#r23"
  - "§9.5#r28"
  - "EB-TBL-1@select-asset-name"
  - "EB-TBL-9@select-asset-name"
  - "EB-FLT-6@select-asset-name"
  - "§5#r3"
smoke: []
dependsOn: []
trace:
  §4.1#r384: 2
  §4.1#r391: [11, 15]
  §4.1#r392: 12
  §4.1#r393: 14
  §4.1#r394: 37
  §4.1#r395: 38
  §4.1#r396: 40
  §4.1#r397: 41
  §4.1#r398: [35, 38]
  §4.1#r399: 43
  §4.1#r400: [47, 57]
  §4.1#r402: 4
  §4.1#r403: [4, 5]
  §4.1#r404: 9
  §4.1#r405: 71
  §4.1#r406: [72, 77]
  §4.1#r407: 74
  §4.1#r408: 80
  §4.1#r410: [11, 14, 17, 33, 57, 84]
  §4.1#r411: [11, 14, 18, 33, 57]
  §4.1#r412: [11, 14, 19, 21, 22, 24, 33, 47, 49]
  §4.1#r413: [11, 14, 25, 27, 28, 50, 52]
  §4.1#r414: [11, 14, 29, 30, 53, 55]
  §4.1#r415: [11, 14, 31, 32, 33, 56]
  §4.4#r13: [71, 72]
  §4.5#b4: [87, 89]
  §6#r11: 72
  §7#r15: [91, 92]
  "AU-BAGIAN-asampaiAU-BAGIAN-s,AU-NILAI-asampaiAU-NILAI-l,AU-TOOLTIP-asampaiAU-TOOLTIP-f": [3, 19]
  D-04: [2, 8]
  S-08: [96, 97, 102]
  §9.5#r2: [45, 47]
  §9.5#r29: [91, 92]
  §9.9#r23: 72
  §9.5#r28: [28, 30]
  EB-TBL-1@select-asset-name: [91, 96, 98, 104, 105, 106]
  EB-TBL-9@select-asset-name: [5, 71, 72]
  EB-FLT-6@select-asset-name: [65, 67, 68]
  "§5#r3": [111, 113]
anchor: [110]
coverage:
  web: automated
---

# Dialog Select Asset Name: kolom, toolbar, footer, dan validasi

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings, Dialog Add override - Borrow yang dibuka dari All categories dengan Scope `Asset Name`; Dialog Select Asset Name dibuka dari tombol `[Select Asset Name]`.
- Komponen: Dialog Select Asset Name
- Data:
  - DU-077-1: Asset Name `Excavator PC200`, Code `EXC-PC200`, Category `Machinery` (hierarki `Heavy Equipment > Machinery`), Labels `Heavy, Insured, Rental`, UoM `Unit`, Total Asset `12`.
  - DU-077-2: Asset Name `Toyota Avanza`, Code `VEH-AVZ`, Category `Pool car` (hierarki `Vehicle > Pool car`), tanpa Labels, tanpa UoM, Total Asset `3`.
  - DU-077-3: Asset Name `Weather Station`, Code `WTH-STN`, Category `Environmental Monitoring Equipment` (hierarki `Sensors > Environmental Monitoring Equipment`; badge yang diharapkan `Environmenta..ng Equipment`, dari nama Category 34 karakter), Labels `Outdoor`, UoM `Set`, Total Asset `0`.
  - DU-077-4: kata kunci Search `Zebra Tidak Ada`, tidak cocok dengan baris mana pun.
  - DU-077-5: filter Total Asset Min `100`, melebihi semua baris.
- Kondisi:
  - K1: tabel berisi DU-077-1, DU-077-2, dan DU-077-3; belum ada filter yang diterapkan.
  - K2: tidak ada Asset Name.
  - K3: sama dengan K1; respons atas Search DU-077-4 dan atas filter Total Asset DU-077-5 tidak memuat baris.
  - K4: memuat tabel gagal karena error server.

## Test Steps

### Judul, footer, dan sifat dialog multi-select
1. Tampilkan Dialog Select Asset Name dengan kondisi K1
2. Verifikasi judul dialog `Select Asset Name`
3. Verifikasi dialog memuat tabel, ikon Search, tombol filter, dan Filter Panel yang dapat dibuka
4. Verifikasi footer memuat tombol `Cancel` bergaya teks dan tombol `Select` bergaya filled primary
5. Verifikasi tombol `Select` aktif walau belum ada baris yang tercentang
6. Centang baris `Excavator PC200`
7. Centang baris `Toyota Avanza`
8. Verifikasi kedua baris `Excavator PC200` dan `Toyota Avanza` tercentang sekaligus
9. Verifikasi footer tidak memuat counter jumlah terpilih

### Susunan kolom dan Column Visibility
10. Tampilkan Dialog Select Asset Name dengan kondisi K1
11. Verifikasi header tabel berurutan dari kiri: checkbox, `Name`, `Code`, `Category`, `Labels`, `UoM`, `Total Asset`
12. Verifikasi baris tabel tidak memiliki menu aksi baris
13. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
14. Verifikasi daftar Column Visibility memuat kolom `Name`, `Code`, `Category`, `Labels`, `UoM`, dan `Total Asset`, seluruhnya tercentang dan tidak disabled
15. Verifikasi daftar Column Visibility tidak memuat baris untuk checkbox seleksi baris

### Format sel
16. Tampilkan Dialog Select Asset Name dengan kondisi K1
17. Verifikasi sel Name pada baris Code `EXC-PC200` berisi `Excavator PC200` apa adanya
18. Verifikasi sel Code pada baris `Excavator PC200` berisi `EXC-PC200`
19. Verifikasi sel Category pada baris `Excavator PC200` berisi `Machinery`
20. Arahkan kursor ke badge Category `Machinery`
21. Verifikasi hierarki lengkap `Heavy Equipment > Machinery` tersampaikan pada badge
22. Verifikasi badge Category pada baris `Weather Station` berisi `Environmenta..ng Equipment`
23. Arahkan kursor ke badge Category `Environmenta..ng Equipment`
24. Verifikasi hierarki lengkap `Sensors > Environmental Monitoring Equipment` tersampaikan pada badge
25. Verifikasi sel Labels pada baris `Excavator PC200` menampilkan dua chip pertama `Heavy` dan `Insured`, lalu `+1 more`
26. Klik `+1 more` pada baris `Excavator PC200`
27. Verifikasi popover daftar label penuh `Heavy`, `Insured`, dan `Rental`
28. Verifikasi sel Labels pada baris `Toyota Avanza` berisi `—`
29. Verifikasi sel UoM pada baris `Excavator PC200` berisi `Unit`
30. Verifikasi sel UoM pada baris `Toyota Avanza` berisi `—`
31. Verifikasi sel Total Asset pada baris `Excavator PC200` berisi angka bulat `12` dan rata kanan
32. Verifikasi sel Total Asset pada baris `Weather Station` berisi `0`, bukan `—`
33. Verifikasi sel Name, Code, Category, dan Total Asset di setiap baris berisi nilai dan tidak menampilkan `—`

### Toolbar dan counter jumlah terpilih
34. Tampilkan Dialog Select Asset Name dengan kondisi K1
35. Verifikasi counter jumlah terpilih tidak tampil sebelum ada baris yang tercentang
36. Centang baris `Excavator PC200`
37. Verifikasi toolbar memuat counter yang rata kiri, ikon Search, lalu tombol filter berurutan dari kiri ke kanan[^drift-2]
38. Verifikasi counter menampilkan `1 Asset Name selected`[^drift-1]
39. Centang baris `Toyota Avanza`
40. Verifikasi counter menampilkan `2 Asset Names selected`[^drift-1]
41. Verifikasi toolbar tidak memuat tombol dropdown `Bulk Action`
42. Klik ikon Search di toolbar
43. Verifikasi kotak Search memuat placeholder `Search asset name or code...`

### Field Filter Panel dan default tanpa filter
44. Tampilkan Dialog Select Asset Name dengan kondisi K1
45. Verifikasi tombol filter tidak menampilkan indikator filter aktif
46. Klik tombol filter di toolbar
47. Verifikasi field filter `Category` berupa multi-select dengan placeholder `All categories`
48. Klik field filter `Category`
49. Verifikasi daftar opsi field `Category` menyediakan kotak pencarian opsi
50. Verifikasi field filter `Label` berupa multi-select dengan placeholder `All labels`
51. Klik field filter `Label`
52. Verifikasi daftar opsi field `Label` menyediakan kotak pencarian opsi
53. Verifikasi field filter `UoM` berupa multi-select dengan placeholder `All units`
54. Klik field filter `UoM`
55. Verifikasi daftar opsi field `UoM` menyediakan kotak pencarian opsi
56. Verifikasi field filter `Total Asset` berupa rentang angka dengan placeholder `Min` dan `Max`
57. Verifikasi Filter Panel tidak memuat field filter `Name` dan `Code`

### Menyembunyikan kolom tidak menghapus field filter dan filter ter-Apply
58. Tampilkan Dialog Select Asset Name dengan kondisi K1
59. Klik tombol filter di toolbar
60. Klik field filter `UoM`
61. Pilih opsi `Unit` pada field filter `UoM`
62. Klik `[Apply]`
63. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
64. Hilangkan centang kolom `UoM` pada Column Visibility
65. Verifikasi tabel tidak menampilkan header kolom `UoM`
66. Klik tombol filter di toolbar untuk membuka kembali Filter Panel
67. Verifikasi field filter `UoM` tetap ada pada Filter Panel
68. Verifikasi chip `Unit` tetap tampil pada field filter `UoM` dan tombol filter tetap menampilkan indikator filter aktif

### Select tanpa baris terpilih
69. Tampilkan Dialog Select Asset Name dengan kondisi K1
70. Klik `[Select]`
71. Verifikasi dialog Select Asset Name tetap terbuka
72. Verifikasi teks `You must pick an asset name` tampil di footer, tepat di atas tombol `Select`
73. Centang baris `Excavator PC200`
74. Verifikasi teks `You must pick an asset name` hilang

### Pesan hilang saat dialog dibuka ulang
75. Tampilkan Dialog Select Asset Name dengan kondisi K1
76. Klik `[Select]`
77. Verifikasi teks `You must pick an asset name` tampil di footer
78. Klik `[Cancel]`
79. Klik `[Select Asset Name]` pada Dialog Add override untuk membuka ulang Dialog Select Asset Name dengan kondisi K1
80. Verifikasi teks `You must pick an asset name` tidak tampil sesudah dialog dibuka ulang

### Select dengan baris terpilih
81. Tampilkan Dialog Select Asset Name dengan kondisi K1
82. Centang baris `Excavator PC200`
83. Klik `[Select]`
84. Verifikasi dialog Select Asset Name tertutup dan badge `Excavator PC200` tampil di bawah tombol `Select Asset Name` pada Dialog Add override

### Menutup dialog
85. Tampilkan Dialog Select Asset Name dengan kondisi K1
86. Klik backdrop di luar dialog
87. Verifikasi dialog Select Asset Name tetap terbuka
88. Tekan `Esc`
89. Verifikasi dialog Select Asset Name tertutup

### Empty state belum ada Asset Name
90. Tampilkan Dialog Select Asset Name dengan kondisi K2
91. Verifikasi judul empty state `No asset names yet` tampil
92. Verifikasi deskripsi `Get started by creating your first asset name.` tampil

### Empty state hasil Search dan Filter tanpa hasil
93. Tampilkan Dialog Select Asset Name dengan kondisi K3
94. Klik ikon Search di toolbar
95. Ketik Search `Zebra Tidak Ada`, tekan Enter
96. Verifikasi judul empty state `No results found` tampil pada tabel Select Asset Name
97. Verifikasi deskripsi empty state `Try adjusting your search or filter.` tampil pada tabel Select Asset Name
98. Verifikasi `No asset names yet` tidak tampil
99. Klik tombol filter di toolbar
100. Isi Min `100` pada field filter `Total Asset`
101. Klik `[Apply]`
102. Verifikasi judul empty state `No results found` tampil pada tabel Select Asset Name sesudah filter

### Gagal memuat tabel
103. Tampilkan Dialog Select Asset Name dengan kondisi K4
104. Verifikasi pesan `Unable to load this data.` tampil
105. Verifikasi tombol `[Try Again]` tampil
106. Verifikasi `No asset names yet` tidak tampil

### Search dikirim saat Enter tanpa debounce
107. Tampilkan Dialog Select Asset Name dengan kondisi K3
108. Klik ikon Search di toolbar
109. Ketik Search `Zebra Tidak Ada` pada Dialog Select Asset Name tanpa menekan Enter
110. Verifikasi baris `Excavator PC200` masih tampil pada tabel Select Asset Name
111. Verifikasi tidak ada permintaan pencarian Select Asset Name yang dikirim sebelum Enter ditekan
112. Tekan Enter
113. Verifikasi permintaan pencarian Select Asset Name dengan kata kunci `Zebra Tidak Ada` dikirim segera setelah Enter, tanpa jeda debounce

[^drift-1]: Drift PRD vs foundation. PRD §4.1 `SAN-TOOLBAR-b` dan `SAN-TOOLBAR-c`: counter jumlah terpilih `1 asset name selected` dan `[N] asset names selected`. foundation `prd-conventions.md` §8 (dirujuk §37.2 Selection Counter): `1 → "1 [Item] selected" · N → "[N] [Items] selected"`, dengan nama entitas berkapital. Diasersi: foundation, karena counter jumlah terpilih adalah pola bersama (SB-4).
[^drift-2]: Drift PRD vs foundation. PRD §4.1 (Deviasi): counter jumlah terpilih pada dialog Select Asset Name diletakkan rata kanan di toolbar, bukan rata kiri. Foundation `prd-conventions.md` §37.2 (Selection Counter): counter di atas tabel, rata kiri, sejajar satu baris dengan Toolbar (Search + Filter). Diasersi: foundation, karena counter jumlah terpilih adalah pola bersama (SB-4).

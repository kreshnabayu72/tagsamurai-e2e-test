---
id: TC-FA-FATR-E2E-017-picker-asset-name
title: "Dialog Select Asset Name menampilkan Asset Name dari data nyata"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1#r387, §4.1#r410, §4.1#r411, §4.1#r412, §4.1#r413, §4.1#r414, §4.1#r415, §5#r3, §5#r4, D-04, §9.5#r10, §9.5#r23, §9.5#r24, §11#r9, EB-TBL-9@select-asset-name, EB-SRC-5@select-asset-name, "AU-BAGIAN-asampaiAU-BAGIAN-s,AU-NILAI-asampaiAU-NILAI-l,AU-TOOLTIP-asampaiAU-TOOLTIP-f"]
smoke: []
dependsOn: []
trace:
  §4.1#r387: [8, 19]
  §4.1#r410: [8, 22, 30]
  §4.1#r411: [9, 26, 33]
  §4.1#r412: [10, 40, 81, 93, 95, 100, 101]
  §4.1#r413: [11, 12, 24, 35, 60, 61]
  §4.1#r414: [9, 28, 38, 66, 67]
  §4.1#r415: [9, 15, 17, 71, 72, 76]
  §5#r3: [30, 31, 33, 35, 36, 38, 40, 42, 44, 60]
  §5#r4: [8, 19]
  D-04: [13, 90, 91]
  §9.5#r10: 8
  §9.5#r23: 13
  §9.5#r24: [90, 91]
  §11#r9: 8
  EB-TBL-9@select-asset-name: [13, 91]
  EB-SRC-5@select-asset-name: [46, 50, 54]
  "AU-BAGIAN-asampaiAU-BAGIAN-s,AU-NILAI-asampaiAU-NILAI-l,AU-TOOLTIP-asampaiAU-TOOLTIP-f": [13, 90, 91]
anchor: [8]
coverage:
  web: automated
---

# Dialog Select Asset Name menampilkan Asset Name dari data nyata

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-017-1: Category leaf `Machinery {runId}`, ada di entitas aktor.
  - DU-017-2: Category leaf `Laptop {runId}`, ada di entitas aktor.
  - DU-017-3: Group tingkat atas `Gudang Utama {runId}`.
  - DU-017-4: Label `Heavy {runId}`.
  - DU-017-5: Label `Imported {runId}`.
  - DU-017-6: Label `Rental {runId}`.
  - DU-017-7: Label `Staff {runId}`.
  - DU-017-8: Label `Zeta {runId}`.
  - DU-017-9: Asset Name `Excavator PC200 {runId}`, Code `EXC17-{runId}`, Category `Machinery {runId}`, UoM `Unit`, Labels `Heavy {runId}`, `Imported {runId}`, dan `Rental {runId}`, Total Asset `3`; rentang filter Total Asset yang dipakai: Min `2` Max `5` dan Min `20` Max `30`.
  - DU-017-10: Asset Name `Toyota Avanza {runId}`, Code `AVZ17-{runId}`, Category `Machinery {runId}`, UoM `Unit`, Labels `Rental {runId}` dan `Staff {runId}`, Total Asset `1`.
  - DU-017-11: Asset Name `Crane LTM900 {runId}`, Code `CRN17-{runId}`, Category `Machinery {runId}`, UoM `Set`, Labels `Heavy {runId}` dan `Zeta {runId}`, Total Asset `12`; kata kunci Search yang dipakai atasnya: `Set` dan `12`.
  - DU-017-12: Asset Name `Bulldozer D65 {runId}`, Code `BLD17-{runId}`, Category `Machinery {runId}`, UoM `Unit`, tanpa Labels (tampil `—`), Total Asset `0`; kata kunci Search tanpa hasil yang dipakai: `Zzqx {runId}`.
  - DU-017-13: Asset Name `Forklift FL25 {runId}`, Code `FRK17-{runId}`, Category `Machinery {runId}`, UoM `Unit`, nonaktif.
  - DU-017-14: Asset Name `Grader G720 {runId}`, Code `GRD17-{runId}`, Category `Machinery {runId}`, UoM `Unit`, terhapus.
  - DU-017-15: Asset Name `Printer X1 {runId}`, Code `PRT17-{runId}`, Category `Laptop {runId}`, UoM `Unit`, aktif.
  - DU-017-16: 2 aset `Excavator PC200 {runId} - {n}` dengan n dari 1 sampai 2, ber-Group `Gudang Utama {runId}`.
  - DU-017-17: aset `Toyota Avanza {runId} - 1`, ber-Group `Gudang Utama {runId}`.
  - DU-017-19: aset `Excavator PC200 {runId} - 3`, ber-Group `Gudang Utama {runId}`, berstatus Disposed.
  - DU-017-18: 12 aset `Crane LTM900 {runId} - {n}` dengan n dari 1 sampai 12, ber-Group `Gudang Utama {runId}`.
- Kondisi:
  - Nilai `{runId}` tidak memuat urutan digit `12`.
  - Kolom `Code` dialog Select Asset Name ditampilkan (bawaan).

## Test Steps

### Dialog menampilkan Asset Name aktif dalam Category terpilih dengan urutan awal Name A-Z
1. Ketik Search Sidebar Category Tree `Machinery {runId}`, tekan Enter
2. Klik node `Machinery {runId}` di Sidebar Category Tree
3. Klik tab `Borrow`
4. Klik `[+ Override]`
5. Pilih Scope `Asset Name`
6. Klik `[Select Asset Name]`
7. Ketik Search `{runId}` pada dialog Select Asset Name, tekan Enter
8. Verifikasi urutan baris dari atas ke bawah menurut Name: `Bulldozer D65 {runId}`, `Crane LTM900 {runId}`, `Excavator PC200 {runId}`, `Toyota Avanza {runId}` sebagai Name A-Z
9. Verifikasi baris `Excavator PC200 {runId}` memiliki Code `EXC17-{runId}`, UoM `Unit`, dan Total Asset `3`, termasuk aset berstatus Disposed
10. Verifikasi baris `Excavator PC200 {runId}` memiliki Category `Machinery {runId}`
11. Verifikasi baris `Excavator PC200 {runId}` memiliki Labels `Heavy {runId}`, `Imported {runId}`, dan `+1 more`
12. Verifikasi baris `Bulldozer D65 {runId}` memiliki Labels `—`
13. Verifikasi baris `Forklift FL25 {runId}`, baris `Grader G720 {runId}`, dan baris `Printer X1 {runId}` tidak tampil karena Asset Name nonaktif, terhapus, dan milik Category lain

### Sort kolom Total Asset, Name, Labels, Code, dan UoM
14. Klik header kolom Total Asset pada dialog Select Asset Name
15. Verifikasi urutan baris dari atas ke bawah menurut Name: `Bulldozer D65 {runId}`, `Toyota Avanza {runId}`, `Excavator PC200 {runId}`, `Crane LTM900 {runId}` sebagai Total Asset `0`, `1`, `3`, `12` secara ascending
16. Klik header kolom Total Asset pada dialog Select Asset Name
17. Verifikasi urutan baris dari atas ke bawah menurut Name: `Crane LTM900 {runId}`, `Excavator PC200 {runId}`, `Toyota Avanza {runId}`, `Bulldozer D65 {runId}` sebagai Total Asset secara descending
18. Klik header kolom Total Asset pada dialog Select Asset Name
19. Verifikasi urutan baris dari atas ke bawah menurut Name: `Bulldozer D65 {runId}`, `Crane LTM900 {runId}`, `Excavator PC200 {runId}`, `Toyota Avanza {runId}` kembali ke urutan bawaan Name A-Z
20. Klik header kolom Name pada dialog Select Asset Name
21. Klik header kolom Name pada dialog Select Asset Name
22. Verifikasi urutan baris dari atas ke bawah menurut Name: `Toyota Avanza {runId}`, `Excavator PC200 {runId}`, `Crane LTM900 {runId}`, `Bulldozer D65 {runId}` secara descending
23. Klik header kolom Labels pada dialog Select Asset Name
24. Verifikasi urutan baris dari atas ke bawah menurut Name: `Bulldozer D65 {runId}`, `Crane LTM900 {runId}`, `Toyota Avanza {runId}`, `Excavator PC200 {runId}` menurut jumlah label lalu label pertama secara ascending
25. Klik header kolom Code pada dialog Select Asset Name
26. Verifikasi urutan baris dari atas ke bawah menurut Name: `Toyota Avanza {runId}`, `Bulldozer D65 {runId}`, `Crane LTM900 {runId}`, `Excavator PC200 {runId}` menurut Code `AVZ17-{runId}`, `BLD17-{runId}`, `CRN17-{runId}`, `EXC17-{runId}` secara ascending
27. Klik header kolom UoM pada dialog Select Asset Name
28. Verifikasi baris `Crane LTM900 {runId}` dengan UoM `Set` tampil di atas baris `Excavator PC200 {runId}` dengan UoM `Unit` secara ascending menurut UoM

### Search mencari di semua kolom yang searchable
29. Ganti isi kotak Search dengan `Toyota Avanza {runId}`, tekan Enter
30. Verifikasi baris `Toyota Avanza {runId}` tampil karena kolom Name ikut dicari
31. Verifikasi baris `Excavator PC200 {runId}`, baris `Crane LTM900 {runId}`, dan baris `Bulldozer D65 {runId}` tidak tampil
32. Ganti isi kotak Search dengan `CRN17-{runId}`, tekan Enter
33. Verifikasi baris `Crane LTM900 {runId}` tampil karena kolom Code ikut dicari
34. Ganti isi kotak Search dengan `Imported {runId}`, tekan Enter
35. Verifikasi baris `Excavator PC200 {runId}` tampil karena kolom Labels ikut dicari
36. Verifikasi baris `Toyota Avanza {runId}` dan baris `Bulldozer D65 {runId}` tidak tampil
37. Ganti isi kotak Search dengan `Set`, tekan Enter
38. Verifikasi baris `Crane LTM900 {runId}` dengan UoM `Set` tampil karena kolom UoM ikut dicari
39. Ganti isi kotak Search dengan `Machinery {runId}`, tekan Enter
40. Verifikasi keempat baris `Bulldozer D65 {runId}`, `Crane LTM900 {runId}`, `Excavator PC200 {runId}`, dan `Toyota Avanza {runId}` tampil karena kolom Category ikut dicari
41. Ganti isi kotak Search dengan `12`, tekan Enter
42. Verifikasi `No results found` tampil pada dialog Select Asset Name karena nilai `12` hanya ada di kolom Total Asset yang tidak ikut dicari
43. Ganti isi kotak Search dengan `Zzqx {runId}`, tekan Enter
44. Verifikasi `No results found` tampil pada dialog Select Asset Name

### Search tidak lagi mencocokkan kolom yang disembunyikan
45. Ganti isi kotak Search dengan `EXC17-{runId}`, tekan Enter
46. Verifikasi baris `Excavator PC200 {runId}` tampil karena kolom Code ikut dicari
47. Klik header kolom Actions pada dialog Select Asset Name
48. Hapus centang kolom `Code`
49. Ganti isi kotak Search dengan `EXC17-{runId}` lagi, tekan Enter
50. Verifikasi `No results found` tampil pada dialog Select Asset Name karena kolom Code disembunyikan
51. Klik header kolom Actions pada dialog Select Asset Name
52. Centang kolom `Code`
53. Ganti isi kotak Search dengan `EXC17-{runId}` lagi, tekan Enter
54. Verifikasi baris `Excavator PC200 {runId}` tampil lagi karena kolom Code ditampilkan

### Filter Label, UoM, dan Total Asset
55. Ganti isi kotak Search dengan `{runId}`, tekan Enter
56. Klik ikon filter pada toolbar dialog Select Asset Name
57. Klik field `Label` pada panel filter
58. Pilih opsi `Imported {runId}`
59. Klik `[Apply]`
60. Verifikasi baris `Excavator PC200 {runId}` tampil karena memiliki Labels `Imported {runId}`
61. Verifikasi baris `Toyota Avanza {runId}`, baris `Crane LTM900 {runId}`, dan baris `Bulldozer D65 {runId}` tidak tampil
62. Klik `[Clear Field]`
63. Klik field `UoM` pada panel filter
64. Pilih opsi `Set`
65. Klik `[Apply]`
66. Verifikasi baris `Crane LTM900 {runId}` tampil karena memiliki UoM `Set`
67. Verifikasi baris `Excavator PC200 {runId}`, baris `Toyota Avanza {runId}`, dan baris `Bulldozer D65 {runId}` tidak tampil
68. Klik `[Clear Field]`
69. Pada field `Total Asset`, isi Min `2` dan Max `5`
70. Klik `[Apply]`
71. Verifikasi baris `Excavator PC200 {runId}` dengan Total Asset `3` tampil
72. Verifikasi baris `Crane LTM900 {runId}`, baris `Toyota Avanza {runId}`, dan baris `Bulldozer D65 {runId}` tidak tampil
73. Klik `[Clear Field]`
74. Pada field `Total Asset`, isi Min `20` dan Max `30`
75. Klik `[Apply]`
76. Verifikasi `No results found` tampil pada dialog Select Asset Name karena tidak ada Asset Name dengan Total Asset dalam rentang itu
77. Klik `[Clear Field]`
78. Klik field `Category` pada panel filter
79. Pilih opsi `Machinery {runId}`
80. Klik `[Apply]`
81. Verifikasi baris `Excavator PC200 {runId}` dengan Category `Machinery {runId}` tampil

### Dari All categories dialog menampilkan semua Asset Name aktif milik Company
82. Klik `[Cancel]` pada dialog Select Asset Name
83. Klik `✕` pada dialog, lalu klik `[Leave]` pada dialog Unsaved Changes
84. Klik node `All categories` di Sidebar Category Tree
85. Klik tab `Borrow`
86. Klik `[+ Override]`
87. Pilih Scope `Asset Name`
88. Klik `[Select Asset Name]`
89. Ketik Search `{runId}` pada dialog Select Asset Name, tekan Enter
90. Verifikasi baris `Excavator PC200 {runId}` dengan Category `Machinery {runId}` dan baris `Printer X1 {runId}` dengan Category `Laptop {runId}` tampil
91. Verifikasi baris `Forklift FL25 {runId}` dan baris `Grader G720 {runId}` tidak tampil

### Sort dan Filter kolom Category dari All categories
92. Klik header kolom Category pada dialog Select Asset Name
93. Verifikasi baris `Printer X1 {runId}` dengan Category `Laptop {runId}` tampil di atas baris `Excavator PC200 {runId}` dengan Category `Machinery {runId}` secara ascending menurut Category
94. Klik header kolom Category pada dialog Select Asset Name
95. Verifikasi baris `Excavator PC200 {runId}` tampil di atas baris `Printer X1 {runId}` secara descending menurut Category
96. Klik ikon filter pada toolbar dialog Select Asset Name
97. Klik field `Category` pada panel filter
98. Pilih opsi `Machinery {runId}`
99. Klik `[Apply]`
100. Verifikasi baris `Excavator PC200 {runId}` dengan Category `Machinery {runId}` tampil sesudah Filter Category dari All categories
101. Verifikasi baris `Printer X1 {runId}` tidak tampil karena Category `Laptop {runId}` tersaring keluar

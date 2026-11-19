---
id: TC-FA-ASTL-E2E-004-search
title: "Search pada tabel All Assets"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [EC-20, F-ASTL-03, FLD-01, FLD-02, FLD-03, FLD-04, FLD-05, FLD-06, FLD-07, FLD-08, FLD-09, FLD-10, FLD-11, FLD-12, FLD-13, FLD-14, FLD-15, FLD-16, FLD-17, FLD-18, FLD-19, FLD-20, FLD-21, FLD-22, FLD-23, FLD-24, FLD-25, FLD-26, "§5#r3", "§9.2#p3", "EB-SRC-2@tabel-all-assets", "EB-SRC-3@tabel-all-assets", EB-SRC-1]
smoke: [EB-SRC-1]
dependsOn: []
trace:
  EC-20: 22
  F-ASTL-03: 8
  FLD-01: 69
  FLD-02: 35
  FLD-03: 39
  FLD-04: 37
  FLD-05: 14
  FLD-06: 12
  FLD-07: 41
  FLD-08: 43
  FLD-09: 45
  FLD-10: 47
  FLD-11: 10
  FLD-12: 49
  FLD-13: 51
  FLD-14: 69
  FLD-15: 69
  FLD-16: 53
  FLD-17: 55
  FLD-18: [65, 110]
  FLD-19: [65, 114]
  FLD-20: 69
  FLD-21: 57
  FLD-22: 69
  FLD-23: 59
  FLD-24: 61
  FLD-25: 69
  FLD-26: 70
  "§5#r3": [6, 9, 67, 74]
  "§9.2#p3": [6, 8]
  "EB-SRC-2@tabel-all-assets": 77
  "EB-SRC-3@tabel-all-assets": [79, 80, 82, 83, 85, 86, 88, 89, 91, 92, 94, 95, 97, 98, 100, 104]
  EB-SRC-1: [10, 16, 18, 20, 106]
anchor: [4, 63, 72, 102]
coverage:
  web: automated
---

# Search pada tabel All Assets

## Prerequisites
- Aktor: Total Control `Sari Wulandari {runId}`.
- Layar awal: Fixed Asset > Assets (tab `Assets`).
- Data:
  - DU-004-1: User `Sari Wulandari {runId}`, role Total Control, cakupan seluruh client, memakai konfigurasi kolom bawaan, dan menjadi pengubah terakhir seluruh aset DU-004 di bawah.
  - DU-004-2: Aset `Sensor Uji - 1 {runId}`: Alias Name `Alias-Zeta {runId}`, TAG `RFID` dengan Tag Code `Tag-Zeta {runId}`, Brand `Brand-Zeta {runId}`, Model / Type `Model-Zeta {runId}`, Measurement `Unit-Zeta {runId}`, Category `Kategori-Zeta {runId}`, Group `Group-Zeta {runId}`, Division `Div-Zeta {runId}`, Labels `Label-Zeta {runId}`, Custom field `Lokasi Rak {runId}` bernilai `Zeta-Lokasi {runId}`, berstatus `Borrowed`, Asset Class `Kelas-Zeta {runId}`, Tax Depreciation Class `Pajak-Zeta {runId}`, dan Purchase Cost `7777000` (tampil `Rp 7.777.000,00`), tanpa Additional costs dan tanpa periode penyusutan Posted sehingga Asset Value (Commercial) dan Asset Value (Fiscal) masing-masing tampil `Rp 7.777.000,00` (harga perolehan). Modified By aset ini adalah `Sari Wulandari {runId}`.
  - DU-004-3: Aset `Rak Alfa - 1 {runId}`: Register Date dan Last Updated bernilai `T0` (tanggal run), Division `Procurement {runId}`, Purchase Cost belum diisi sehingga Asset Value (Commercial) bernilai `Pending`.
  - DU-004-4: Aset `Rak Beta - 1 {runId}`: Brand `Kencana {runId}`.
  - DU-004-5: Aset `Rak Beta - 2 {runId}`: Division `Kencana {runId}`.
  - DU-004-6: Aset `Rak Gamma - 1 {runId}`: Division `Head Office Room {runId}`.
  - DU-004-7: Aset `Rak Delta - 1 {runId}`: Division `Lumen Prima {runId}`.
  - DU-004-8: Aset `Rak Delta - 2 {runId}`: Division `LumenPrima {runId}`.
  - DU-004-9: Aset `Rak Eps - 1 {runId}`: Labels `Aktif {runId}`.
  - DU-004-10: Aset `Rak Eps - 2 {runId}`: Labels `Nonaktif {runId}`.
  - DU-004-11: Aset `Rak Omega - 1 {runId}`: Division `Tim 50% {runId}`.
  - DU-004-12: Aset `Rak Omega - 2 {runId}`: Division `Tim 50 Persen {runId}`.
  - DU-004-13: Aset `Rak Omega - 3 {runId}`: Division `Tim_Ops {runId}`.
  - DU-004-14: Aset `Rak Omega - 4 {runId}`: Division `TimXOps {runId}`.
  - DU-004-15: Aset `Rak Omega - 5 {runId}`: Division `Tim*Dev {runId}`.
  - DU-004-16: Aset `Rak Omega - 6 {runId}`: Division `Tim Dev {runId}`.
  - DU-004-17: Aset `Rak Omega - 7 {runId}`: Division `Tim\QA {runId}`.
  - DU-004-18: Aset `Rak Omega - 8 {runId}`: Division `TimQA {runId}`.
  - DU-004-19: Aset `Rak Omega - 9 {runId}`: Division `Tim.*Ops {runId}`.
  - DU-004-20: Aset `Rak Omega - 10 {runId}`: Division `Tim Ops {runId}`.
  - DU-004-21: Custom field aktif `Lokasi Rak {runId}` bertipe teks pada grup General.
- Kondisi:
  - Akun `Sari Wulandari {runId}` aktif dan kredensialnya tersedia.
  - Date Format bernilai `dd/MM/yy`.

## Test Steps

### Search dijalankan dengan Enter
1. Masuk sebagai `Sari Wulandari {runId}`
2. Klik menu `Fixed Asset > Assets` pada sidebar
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi baris `Rak Alfa - 1 {runId}` tampil
5. Ketik `Div-Zeta {runId}` pada kotak Search tanpa menekan Enter
6. Verifikasi baris `Rak Alfa - 1 {runId}` masih tampil karena Search belum dijalankan
7. Tekan Enter
8. Verifikasi baris `Sensor Uji - 1 {runId}` tampil
9. Verifikasi baris `Rak Alfa - 1 {runId}` tidak tampil

### Search per kelas kolom, substring, dan tanpa hasil
10. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `Div-Zeta {runId}` cocok pada kolom teks `Division`
11. Ganti isi kotak search dengan `Brand-Zeta {runId}`, tekan Enter
12. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `Brand-Zeta {runId}` cocok pada kolom badge `Brand`
13. Ganti isi kotak search dengan `RFID`, tekan Enter
14. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `RFID` cocok pada label ikon kolom `TAG`
15. Ganti isi kotak search dengan `curement {runId}`, tekan Enter
16. Verifikasi baris `Rak Alfa - 1 {runId}` tampil karena kata kunci cocok di tengah nilai `Procurement {runId}`, bukan awalan
17. Ganti isi kotak search dengan `PROCUREMENT {runId}`, tekan Enter
18. Verifikasi baris `Rak Alfa - 1 {runId}` tampil walau huruf besar dan kecilnya berbeda
19. Ganti isi kotak search dengan `Zzxqv {runId}`, tekan Enter
20. Verifikasi tabel menampilkan `No results found`
21. Klik kartu `Available`
22. Verifikasi tabel menampilkan empty state `No results found` pada kartu `Available` yang aktif, sedangkan kartu status tetap tampil
23. Klik kartu `All`

### Kolom tambahan ikut dicari bila ditampilkan
24. Ganti isi kotak search dengan `{runId}`, tekan Enter
25. Klik header kolom `Actions`
26. Centang kolom `Alias Name` pada panel Column Visibility
27. Centang kolom `Measurement` pada panel Column Visibility
28. Centang kolom `Asset Class` pada panel Column Visibility
29. Centang kolom `Tax Depreciation Class` pada panel Column Visibility
30. Centang kolom `Purchase Cost` pada panel Column Visibility
31. Centang kolom `Asset Value (Commercial)` pada panel Column Visibility
32. Centang kolom `Asset Value (Fiscal)` pada panel Column Visibility
33. Centang kolom `Lokasi Rak {runId}` pada panel Column Visibility
34. Ganti isi kotak search dengan `Sensor Uji - 1 {runId}`, tekan Enter
35. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena cocok pada kolom `Name`
36. Ganti isi kotak search dengan Asset ID milik DU-004-2, tekan Enter
37. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena cocok pada kolom `Asset ID`
38. Ganti isi kotak search dengan `Alias-Zeta {runId}`, tekan Enter
39. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `Alias-Zeta {runId}` cocok pada kolom `Alias Name`
40. Ganti isi kotak search dengan `Model-Zeta {runId}`, tekan Enter
41. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `Model-Zeta {runId}` cocok pada kolom `Model / Type`
42. Ganti isi kotak search dengan `Unit-Zeta {runId}`, tekan Enter
43. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `Unit-Zeta {runId}` cocok pada kolom `Measurement`
44. Ganti isi kotak search dengan `Kategori-Zeta {runId}`, tekan Enter
45. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `Kategori-Zeta {runId}` cocok pada kolom `Category`
46. Ganti isi kotak search dengan `Group-Zeta {runId}`, tekan Enter
47. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `Group-Zeta {runId}` cocok pada kolom `Group`
48. Ganti isi kotak search dengan `Label-Zeta {runId}`, tekan Enter
49. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `Label-Zeta {runId}` cocok pada kolom `Labels`
50. Ganti isi kotak search dengan `Borrowed`, tekan Enter
51. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `Borrowed` cocok pada kolom `Status`
52. Ganti isi kotak search dengan `Kelas-Zeta {runId}`, tekan Enter
53. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `Kelas-Zeta {runId}` cocok pada kolom `Asset Class`
54. Ganti isi kotak search dengan `Pajak-Zeta {runId}`, tekan Enter
55. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `Pajak-Zeta {runId}` cocok pada kolom `Tax Depreciation Class`
56. Ganti isi kotak search dengan `Rp 7.777.000,00`, tekan Enter
57. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `Rp 7.777.000,00` cocok pada kolom `Purchase Cost`
58. Ganti isi kotak search dengan `Zeta-Lokasi {runId}`, tekan Enter
59. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `Zeta-Lokasi {runId}` cocok pada kolom `Lokasi Rak {runId}`
60. Ganti isi kotak search dengan `Sari Wulandari {runId}`, tekan Enter
61. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `Sari Wulandari {runId}` cocok pada kolom `Modified By`
62. Ganti isi kotak search dengan `Rak Alfa - 1 {runId}`, tekan Enter
63. Verifikasi baris `Rak Alfa - 1 {runId}` tampil dengan sel `Asset Value (Commercial)` bernilai `Pending`
64. Ganti isi kotak search dengan `Pending`, tekan Enter
65. Verifikasi baris `Rak Alfa - 1 {runId}` tidak tampil karena sel `Pending` tidak cocok dengan teksnya
66. Ganti isi kotak search dengan `Tag-Zeta {runId}`, tekan Enter
67. Verifikasi tabel menampilkan `No results found` karena Tag Code tidak ikut dicari
68. Ganti isi kotak search dengan `T0` (tanggal Register Date `Rak Alfa - 1 {runId}`) ditulis menurut Date Format `dd/MM/yy`, tekan Enter
69. Verifikasi baris `Rak Alfa - 1 {runId}` tidak tampil karena kolom tanggal dan foto tidak ikut dicari, yaitu `Photo`, `Register Date`, `Last Scanned`, `Purchase Date`, `Warranty Expiry`, dan `Last Updated`
70. Verifikasi tabel tidak memuat kolom `Purchase status` sehingga nilainya tidak dicari

### Kolom yang disembunyikan tidak ikut dicari
71. Ganti isi kotak search dengan `Brand-Zeta {runId}`, tekan Enter
72. Verifikasi baris `Sensor Uji - 1 {runId}` tampil
73. Lepas centang kolom `Brand` pada panel Column Visibility
74. Verifikasi tabel menampilkan `No results found` karena kolom `Brand` yang disembunyikan tidak lagi dicari
75. Centang kolom `Brand` pada panel Column Visibility

### Kata kunci yang cocok di dua kolom berbeda
76. Ganti isi kotak search dengan `Kencana {runId}`, tekan Enter
77. Verifikasi baris `Rak Beta - 1 {runId}` (cocok pada kolom `Brand`) dan baris `Rak Beta - 2 {runId}` (cocok pada kolom `Division`) tampil bersamaan

### Karakter khusus dicari sebagai teks
78. Ganti isi kotak search dengan `Tim 50% {runId}`, tekan Enter
79. Verifikasi baris `Rak Omega - 1 {runId}` tampil karena karakter `%` dicari sebagai teks
80. Verifikasi baris `Rak Omega - 2 {runId}` dengan Division `Tim 50 Persen {runId}` tidak tampil
81. Ganti isi kotak search dengan `Tim_Ops {runId}`, tekan Enter
82. Verifikasi baris `Rak Omega - 3 {runId}` tampil karena karakter `_` dicari sebagai teks
83. Verifikasi baris `Rak Omega - 4 {runId}` dengan Division `TimXOps {runId}` tidak tampil
84. Ganti isi kotak search dengan `Tim*Dev {runId}`, tekan Enter
85. Verifikasi baris `Rak Omega - 5 {runId}` tampil karena karakter `*` dicari sebagai teks
86. Verifikasi baris `Rak Omega - 6 {runId}` dengan Division `Tim Dev {runId}` tidak tampil
87. Ganti isi kotak search dengan `Tim\QA {runId}`, tekan Enter
88. Verifikasi baris `Rak Omega - 7 {runId}` tampil karena karakter `\` dicari sebagai teks
89. Verifikasi baris `Rak Omega - 8 {runId}` dengan Division `TimQA {runId}` tidak tampil
90. Ganti isi kotak search dengan `Tim.*Ops {runId}`, tekan Enter
91. Verifikasi baris `Rak Omega - 9 {runId}` tampil karena karakter `.*` dicari sebagai teks
92. Verifikasi baris `Rak Omega - 10 {runId}` dengan Division `Tim Ops {runId}` tidak tampil

### Spasi pada kata kunci
93. Ketik Search `Lumen Prima {runId}` dengan satu spasi di awal dan satu spasi di akhir, tekan Enter
94. Verifikasi baris `Rak Delta - 1 {runId}` tampil karena spasi di awal dan di akhir dibuang saat Enter
95. Verifikasi isi kotak Search tetap memuat spasi di awal dan di akhir
96. Ganti isi kotak search dengan `Lumen Prima {runId}`, tekan Enter
97. Verifikasi baris `Rak Delta - 1 {runId}` tampil karena spasi di tengah dipertahankan
98. Verifikasi baris `Rak Delta - 2 {runId}` dengan Division `LumenPrima {runId}` tidak tampil
99. Ganti isi kotak search dengan tiga spasi, tekan Enter
100. Verifikasi baris `Rak Alfa - 1 {runId}` tampil kembali karena kata kunci yang hanya berisi spasi diperlakukan sebagai kosong
101. Ganti isi kotak search dengan `Head Office Room {runId}`, tekan Enter
102. Verifikasi baris `Rak Gamma - 1 {runId}` tampil
103. Ganti isi kotak search dengan `Head Room {runId}`, tekan Enter
104. Verifikasi baris `Rak Gamma - 1 {runId}` tidak tampil karena kata kunci tidak dipecah menjadi beberapa kata

### Nilai yang menjadi substring nilai lain
105. Ganti isi kotak search dengan `Aktif {runId}`, tekan Enter
106. Verifikasi baris `Rak Eps - 1 {runId}` dengan label `Aktif {runId}` tampil

### Search atas nilai Asset Value
107. Lepas centang kolom `Purchase Cost` pada panel Column Visibility
108. Lepas centang kolom `Asset Value (Fiscal)` pada panel Column Visibility
109. Ganti isi kotak search dengan `Rp 7.777.000,00`, tekan Enter
110. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `Rp 7.777.000,00` cocok pada kolom `Asset Value (Commercial)`
111. Centang kolom `Asset Value (Fiscal)` pada panel Column Visibility
112. Lepas centang kolom `Asset Value (Commercial)` pada panel Column Visibility
113. Ganti isi kotak search dengan `Rp 7.777.000,00`, tekan Enter
114. Verifikasi baris `Sensor Uji - 1 {runId}` tampil karena `Rp 7.777.000,00` cocok pada kolom `Asset Value (Fiscal)`

---
id: TC-FA-ASTL-E2E-005-sort
title: "Sort pada tabel All Assets"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [F-ASTL-05, FLD-01, FLD-02, FLD-03, FLD-04, FLD-05, FLD-06, FLD-07, FLD-08, FLD-09, FLD-10, FLD-11, FLD-12, FLD-13, FLD-14, FLD-15, FLD-16, FLD-17, FLD-18, FLD-19, FLD-20, FLD-21, FLD-22, FLD-23, FLD-24, FLD-25, FLD-26, "§5#r4", EB-SRT-1, EB-SRT-2, "EB-SRT-3@tabel-all-assets"]
smoke: [EB-SRT-1, EB-SRT-2, "EB-SRT-3@tabel-all-assets"]
dependsOn: []
trace:
  F-ASTL-05: 18
  FLD-01: 19
  FLD-02: [18, 27, 29]
  FLD-03: [32, 34]
  FLD-04: 126
  FLD-05: [77, 79, 149]
  FLD-06: [21, 23]
  FLD-07: [37, 39]
  FLD-08: [42, 44]
  FLD-09: [47, 49]
  FLD-10: [52, 54]
  FLD-11: [57, 59]
  FLD-12: [82, 84]
  FLD-13: [72, 74]
  FLD-14: [87, 89]
  FLD-15: [96, 153]
  FLD-16: [62, 64]
  FLD-17: [67, 69]
  FLD-18: [110, 156]
  FLD-19: [114, 158]
  FLD-20: [100, 102]
  FLD-21: [105, 107]
  FLD-22: 118
  FLD-23: 122
  FLD-24: [130, 161]
  FLD-25: 92
  FLD-26: 138
  "§5#r4": [18, 21, 23, 25, 135, 141, 143, 145]
  EB-SRT-1: [21, 27, 29, 37, 47, 77, 82, 87, 89, 92, 100, 105, 118]
  EB-SRT-2: [21, 23, 77, 79, 82, 84, 96, 100, 102, 105, 107, 130, 141, 143]
  "EB-SRT-3@tabel-all-assets": [25, 135]
anchor: []
coverage:
  web: automated
---

# Sort pada tabel All Assets

## Prerequisites
- Aktor: Total Control `Wahyu Hidayat {runId}`.
- Layar awal: Fixed Asset > Assets (tab `Assets`).
- Data:
  - DU-005-1: User `Wahyu Hidayat {runId}`, role Total Control, cakupan seluruh client, memakai konfigurasi kolom bawaan, dan menjadi pembuat serta pengubah terakhir aset DU-005-4, DU-005-5, DU-005-8, dan DU-005-9.
  - DU-005-2: Group `Gudang Utama {runId}` dengan anak `Group-A {runId}`, `Group-B {runId}`, `Group-C {runId}`, dan `Group-D {runId}`; group terpisah `Gudang Beton {runId}`.
  - DU-005-3: Custom field aktif `Lokasi Rak {runId}` bertipe teks pada grup General.
  - DU-005-4: Aset `Kompresor - 1 {runId}` (dibuat ke-1): Brand `Elan {runId}`, Alias Name `Bimo {runId}`, TAG `NFC`, Model / Type `Model-C {runId}`, Measurement `Unit {runId}`, Category `Mesin {runId}`, Group `Group-C {runId}`, Division `#Gudang {runId}`, Labels `Lbl-A {runId}, Lbl-B {runId}`, berstatus `Available`, Asset Class `Kelas B {runId}`, Tax Depreciation Class `Pajak 1 {runId}`, Purchase Date `T0 - 30 hari`, Purchase Cost `2500000`, Warranty Expiry `T0 + 50 hari`, Last Scanned `T0 - 5 hari` (pemindaian terbaru pada Audit), dan Lokasi Rak `Rak C {runId}`.
  - DU-005-5: Aset `anggur - 1 {runId}` (dibuat ke-2): Brand `Élan {runId}`, Alias Name `bimo kecil {runId}`, TAG `NFC, QR`, Model / Type `Model-A {runId}`, Measurement `Kg {runId}`, Category `Buah {runId}`, Group `Group-A {runId}`, Division `3D Printer {runId}`, Labels `—`, berstatus `Borrowed`, Asset Class `—`, Tax Depreciation Class `Pajak 2 {runId}`, Purchase Date `belum diisi`, Purchase Cost `belum diisi`, Warranty Expiry `—`, dan Lokasi Rak `Rak A {runId}`.
  - DU-005-6: Aset `Apel - 1 {runId}` (dibuat ke-3): Brand `Ezra {runId}`, Alias Name `—`, TAG `QR`, Model / Type `No Model`, Measurement `Liter {runId}`, Category `Buah {runId}`, Group `Group-B {runId}`, Division `Alfa {runId}`, Labels `Lbl-A {runId}`, berstatus `Assigned`, Asset Class `Kelas A {runId}`, Tax Depreciation Class `—`, Purchase Date `T0 - 90 hari`, Purchase Cost `900000`, Warranty Expiry `T0 + 10 hari`, Last Scanned `T0 - 2 hari` (pemindaian terbaru pada Audit), dan Lokasi Rak `Rak B {runId}`.
  - DU-005-7: Aset `Zebra - 1 {runId}` (dibuat ke-4): Brand `—`, Alias Name `Cakra {runId}`, TAG `—`, Model / Type `Model-B {runId}`, Measurement `Unit {runId}`, Category `Hewan {runId}`, Group `Group-A {runId}`, Division `zulu {runId}`, Labels `Lbl-A {runId}, Lbl-B {runId}, Lbl-C {runId}`, berstatus `Damaged`, Asset Class `Kelas C {runId}`, Tax Depreciation Class `Pajak 1 {runId}`, Purchase Date `T0 - 10 hari`, Purchase Cost `15000000`, Warranty Expiry `—`, dan Lokasi Rak `—`.
  - DU-005-8: Aset `Kompresor - 2 {runId}` (dibuat ke-5): Brand `Elan {runId}`, Alias Name `Ayu {runId}`, TAG `RFID`, Model / Type `Model-D {runId}`, Measurement `Meter {runId}`, Category `Mesin {runId}`, Group `Group-D {runId}`, Division `Bravo {runId}`, Labels `Lbl-B {runId}`, berstatus `Available`, Asset Class `Kelas B {runId}`, Tax Depreciation Class `Pajak 3 {runId}`, Purchase Date `T0 - 60 hari`, Purchase Cost `10000000`, Warranty Expiry `—`, dan Lokasi Rak `—`.
  - DU-005-9: Aset `Kompresor - 10 {runId}` (dibuat ke-6): Brand `Élan {runId}`, Alias Name `Dewa {runId}`, TAG `NFC`, Model / Type `Model-A {runId}`, Measurement `Kg {runId}`, Category `Alat {runId}`, Group `Group-B {runId}`, Division `—`, Labels `Lbl-A {runId}, Lbl-B {runId}`, berstatus `Borrowed`, Asset Class `—`, Tax Depreciation Class `Pajak 2 {runId}`, Purchase Date `belum diisi`, Purchase Cost `belum diisi`, Warranty Expiry `—`, dan Lokasi Rak `—`.
  - DU-005-11: User `Dimas Prakoso {runId}`, role Total Control, cakupan seluruh client, memakai konfigurasi kolom bawaan, dan menjadi pembuat serta pengubah terakhir aset DU-005-6 dan DU-005-7, sehingga Modified By kedua aset itu `Dimas Prakoso {runId}`.
  - DU-005-10: 12 aset `Pilar Beton - {n} {runId}` dengan `n` dari 1 sampai 12, Brand `Zulu {runId}`, Group `Gudang Beton {runId}`.
  - Aset DU-005-5, DU-005-7, DU-005-8, dan DU-005-9 belum pernah dipindai pada Audit sehingga Last Scanned-nya kosong.
  - Keenam aset tanpa Additional costs dan tanpa periode penyusutan Posted: Asset Value (Commercial) dan Asset Value (Fiscal) sama dengan Purchase Cost pada aset yang punya Asset Class dan Purchase Cost (`Apel - 1 {runId}` `900000`, `Kompresor - 1 {runId}` `2500000`, `Kompresor - 2 {runId}` `10000000`, `Zebra - 1 {runId}` `15000000`), dan `Pending` pada `anggur - 1 {runId}` dan `Kompresor - 10 {runId}`.
  - Keenam aset DU di atas dibuat berurutan dengan selang lebih dari satu menit.
  - Urutan bawaan tabel (Name A-Z lalu Increment natural) berbeda dari urutan pembuatan dan dari urutan menaik maupun menurun kolom yang diuji.
- Kondisi:
  - Akun `Wahyu Hidayat {runId}` aktif dan kredensialnya tersedia.
  - Date Format bernilai `dd/MM/yy`.

## Test Steps

### Urutan bawaan dan siklus tiga klik
1. Masuk sebagai `Wahyu Hidayat {runId}`
2. Klik menu `Fixed Asset > Assets` pada sidebar
3. Ketik Search `{runId}`, tekan Enter
4. Klik node `Gudang Utama {runId}`
5. Klik header kolom `Actions`
6. Centang kolom `Alias Name` pada panel Column Visibility
7. Centang kolom `Measurement` pada panel Column Visibility
8. Centang kolom `Last Scanned` pada panel Column Visibility
9. Centang kolom `Asset Class` pada panel Column Visibility
10. Centang kolom `Tax Depreciation Class` pada panel Column Visibility
11. Centang kolom `Asset Value (Commercial)` pada panel Column Visibility
12. Centang kolom `Asset Value (Fiscal)` pada panel Column Visibility
13. Centang kolom `Purchase Date` pada panel Column Visibility
14. Centang kolom `Purchase Cost` pada panel Column Visibility
15. Centang kolom `Warranty Expiry` pada panel Column Visibility
16. Centang kolom `Lokasi Rak {runId}` pada panel Column Visibility
17. Klik header kolom `Actions`
18. Verifikasi urutan bawaan tabel adalah Name A-Z lalu Increment natural: `anggur - 1 {runId}`, `Apel - 1 {runId}`, `Kompresor - 1 {runId}`, `Kompresor - 2 {runId}`, `Kompresor - 10 {runId}`, `Zebra - 1 {runId}`
19. Verifikasi ikon sort tidak ada pada header kolom `Photo`
20. Klik header kolom `Brand`
21. Verifikasi urutan Brand menaik (A-Z, `Elan` sebelum `Élan` sebelum `Ezra`, huruf besar dan kecil tidak dibedakan): `Kompresor - 1 {runId}` dan `Kompresor - 2 {runId}`, lalu `anggur - 1 {runId}` dan `Kompresor - 10 {runId}`, lalu `Apel - 1 {runId}`, lalu `Zebra - 1 {runId}`, dengan baris tanpa Brand di urutan terakhir
22. Klik header kolom `Brand`
23. Verifikasi urutan Brand menurun: baris tanpa Brand `Zebra - 1 {runId}` tampil paling awal dan baris `Apel - 1 {runId}` sesudahnya
24. Klik header kolom `Brand`
25. Verifikasi urutan kembali ke bawaan: `anggur - 1 {runId}`, `Apel - 1 {runId}`, `Kompresor - 1 {runId}`, `Kompresor - 2 {runId}`, `Kompresor - 10 {runId}`, `Zebra - 1 {runId}`

### Sort kolom teks dan badge
26. Klik header kolom `Name`
27. Verifikasi urutan Name menaik tetap `anggur - 1 {runId}`, `Apel - 1 {runId}`, `Kompresor - 1 {runId}`, `Kompresor - 2 {runId}`, `Kompresor - 10 {runId}`, `Zebra - 1 {runId}`, dengan `anggur` sebelum `Apel` dan Increment `2` sebelum `10`
28. Klik header kolom `Name`
29. Verifikasi urutan Name menurun: `Zebra - 1 {runId}` paling awal dan `anggur - 1 {runId}` paling akhir
30. Klik header kolom `Name`
31. Klik header kolom `Alias Name`
32. Verifikasi urutan `Alias Name` menaik: `Kompresor - 2 {runId}`, lalu `Kompresor - 1 {runId}`, lalu `anggur - 1 {runId}`, lalu `Zebra - 1 {runId}`, lalu `Kompresor - 10 {runId}`, lalu `Apel - 1 {runId}`
33. Klik header kolom `Alias Name`
34. Verifikasi urutan `Alias Name` menurun: `Apel - 1 {runId}` tampil paling awal dan `Kompresor - 2 {runId}` tampil paling akhir
35. Klik header kolom `Alias Name`
36. Klik header kolom `Model / Type`
37. Verifikasi urutan `Model / Type` menaik, dengan `No Model` diperlakukan sebagai nilai biasa: `anggur - 1 {runId}` dan `Kompresor - 10 {runId}`, lalu `Zebra - 1 {runId}`, lalu `Kompresor - 1 {runId}`, lalu `Kompresor - 2 {runId}`, lalu `Apel - 1 {runId}`
38. Klik header kolom `Model / Type`
39. Verifikasi urutan `Model / Type` menurun: `Apel - 1 {runId}` tampil paling awal
40. Klik header kolom `Model / Type`
41. Klik header kolom `Measurement`
42. Verifikasi urutan `Measurement` menaik: `anggur - 1 {runId}` dan `Kompresor - 10 {runId}`, lalu `Apel - 1 {runId}`, lalu `Kompresor - 2 {runId}`, lalu `Kompresor - 1 {runId}` dan `Zebra - 1 {runId}`
43. Klik header kolom `Measurement`
44. Verifikasi urutan `Measurement` menurun: kelompok baris `Kompresor - 1 {runId}` dan `Zebra - 1 {runId}` (bernilai sama, urutan di antara keduanya tidak diasersi) tampil paling awal
45. Klik header kolom `Measurement`
46. Klik header kolom `Category`
47. Verifikasi urutan `Category` menaik: `Kompresor - 10 {runId}`, lalu `anggur - 1 {runId}` dan `Apel - 1 {runId}`, lalu `Zebra - 1 {runId}`, lalu `Kompresor - 1 {runId}` dan `Kompresor - 2 {runId}`
48. Klik header kolom `Category`
49. Verifikasi urutan `Category` menurun: kelompok baris `Kompresor - 1 {runId}` dan `Kompresor - 2 {runId}` (bernilai sama, urutan di antara keduanya tidak diasersi) tampil paling awal dan `Kompresor - 10 {runId}` tampil paling akhir
50. Klik header kolom `Category`
51. Klik header kolom `Group`
52. Verifikasi urutan `Group` menaik: `anggur - 1 {runId}` dan `Zebra - 1 {runId}`, lalu `Apel - 1 {runId}` dan `Kompresor - 10 {runId}`, lalu `Kompresor - 1 {runId}`, lalu `Kompresor - 2 {runId}`
53. Klik header kolom `Group`
54. Verifikasi urutan `Group` menurun: `Kompresor - 2 {runId}` tampil paling awal
55. Klik header kolom `Group`
56. Klik header kolom `Division`
57. Verifikasi urutan `Division` menaik, dengan `#Gudang` sebelum `3D Printer` sebelum `Alfa`: `Kompresor - 1 {runId}`, lalu `anggur - 1 {runId}`, lalu `Apel - 1 {runId}`, lalu `Kompresor - 2 {runId}`, lalu `Zebra - 1 {runId}`, lalu `Kompresor - 10 {runId}`
58. Klik header kolom `Division`
59. Verifikasi urutan `Division` menurun: `Kompresor - 10 {runId}` tampil paling awal dan `Kompresor - 1 {runId}` tampil paling akhir
60. Klik header kolom `Division`
61. Klik header kolom `Asset Class`
62. Verifikasi urutan `Asset Class` menaik: `Apel - 1 {runId}`, lalu `Kompresor - 1 {runId}` dan `Kompresor - 2 {runId}`, lalu `Zebra - 1 {runId}`, lalu `anggur - 1 {runId}` dan `Kompresor - 10 {runId}`
63. Klik header kolom `Asset Class`
64. Verifikasi urutan `Asset Class` menurun: kelompok baris `anggur - 1 {runId}` dan `Kompresor - 10 {runId}` (bernilai sama, urutan di antara keduanya tidak diasersi) tampil paling awal dan `Apel - 1 {runId}` tampil paling akhir
65. Klik header kolom `Asset Class`
66. Klik header kolom `Tax Depreciation Class`
67. Verifikasi urutan `Tax Depreciation Class` menaik: `Kompresor - 1 {runId}` dan `Zebra - 1 {runId}`, lalu `anggur - 1 {runId}` dan `Kompresor - 10 {runId}`, lalu `Kompresor - 2 {runId}`, lalu `Apel - 1 {runId}`
68. Klik header kolom `Tax Depreciation Class`
69. Verifikasi urutan `Tax Depreciation Class` menurun: `Apel - 1 {runId}` tampil paling awal
70. Klik header kolom `Tax Depreciation Class`
71. Klik header kolom `Status`
72. Verifikasi urutan `Status` menaik, menurut label badge utama: `Apel - 1 {runId}`, lalu `Kompresor - 1 {runId}` dan `Kompresor - 2 {runId}`, lalu `anggur - 1 {runId}` dan `Kompresor - 10 {runId}`, lalu `Zebra - 1 {runId}`
73. Klik header kolom `Status`
74. Verifikasi urutan `Status` menurun: `Zebra - 1 {runId}` tampil paling awal dan `Apel - 1 {runId}` tampil paling akhir
75. Klik header kolom `Status`
76. Klik header kolom `TAG`
77. Verifikasi urutan TAG menaik menurut label ikon dengan awalan lebih pendek lebih dulu (`NFC`, lalu `NFC` dan `QR`, lalu `QR`, lalu `RFID`): `Kompresor - 1 {runId}` dan `Kompresor - 10 {runId}`, lalu `anggur - 1 {runId}`, lalu `Apel - 1 {runId}`, lalu `Kompresor - 2 {runId}`, lalu `Zebra - 1 {runId}`, dengan baris tanpa TAG di urutan terakhir
78. Klik header kolom `TAG`
79. Verifikasi urutan TAG menurun: baris tanpa TAG `Zebra - 1 {runId}` tampil paling awal
80. Klik header kolom `TAG`
81. Klik header kolom `Labels`
82. Verifikasi urutan Labels menaik menurut jumlah label terkecil dengan tiebreaker label pertama A-Z: `Apel - 1 {runId}`, lalu `Kompresor - 2 {runId}`, lalu `Kompresor - 1 {runId}` dan `Kompresor - 10 {runId}`, lalu `Zebra - 1 {runId}`, lalu `anggur - 1 {runId}`, dengan baris tanpa label di urutan terakhir
83. Klik header kolom `Labels`
84. Verifikasi urutan Labels menurun: baris tanpa label `anggur - 1 {runId}` tampil paling awal dan baris `Zebra - 1 {runId}` bermuatan tiga label sesudahnya
85. Klik header kolom `Labels`

### Sort kolom tanggal dan angka
86. Klik header kolom `Register Date`
87. Verifikasi urutan Register Date menaik (Oldest First) mengikuti urutan pembuatan: `Kompresor - 1 {runId}`, `anggur - 1 {runId}`, `Apel - 1 {runId}`, `Zebra - 1 {runId}`, `Kompresor - 2 {runId}`, `Kompresor - 10 {runId}`
88. Klik header kolom `Register Date`
89. Verifikasi urutan Register Date menurun (Newest First): `Kompresor - 10 {runId}` paling awal dan `Kompresor - 1 {runId}` paling akhir
90. Klik header kolom `Register Date`
91. Klik header kolom `Last Updated`
92. Verifikasi urutan Last Updated menaik (Oldest First) mengikuti urutan pembuatan aset: `Kompresor - 1 {runId}`, `anggur - 1 {runId}`, `Apel - 1 {runId}`, `Zebra - 1 {runId}`, `Kompresor - 2 {runId}`, `Kompresor - 10 {runId}`
93. Klik header kolom `Last Updated`
94. Klik header kolom `Last Updated`
95. Klik header kolom `Last Scanned`
96. Verifikasi urutan Last Scanned menaik (Oldest First): `Kompresor - 1 {runId}`, lalu `Apel - 1 {runId}`, lalu baris tanpa nilai Last Scanned menurut urutan bawaan `anggur - 1 {runId}`, `Kompresor - 2 {runId}`, `Kompresor - 10 {runId}`, `Zebra - 1 {runId}`
97. Klik header kolom `Last Scanned`
98. Klik header kolom `Last Scanned`
99. Klik header kolom `Purchase Date`
100. Verifikasi urutan Purchase Date menaik (Oldest First): `Apel - 1 {runId}`, lalu `Kompresor - 2 {runId}`, lalu `Kompresor - 1 {runId}`, lalu `Zebra - 1 {runId}`, lalu `anggur - 1 {runId}` dan `Kompresor - 10 {runId}`, dengan baris `Pending` di urutan terakhir
101. Klik header kolom `Purchase Date`
102. Verifikasi urutan Purchase Date menurun (Newest First): `Zebra - 1 {runId}`, lalu `Kompresor - 1 {runId}`, lalu `Kompresor - 2 {runId}`, lalu `Apel - 1 {runId}`, dengan baris `Pending` `anggur - 1 {runId}` dan `Kompresor - 10 {runId}` tetap di urutan terakhir (urutan di antara keduanya tidak diasersi)
103. Klik header kolom `Purchase Date`
104. Klik header kolom `Purchase Cost`
105. Verifikasi urutan Purchase Cost menaik secara numerik (`900000`, `2500000`, `10000000`, lalu `15000000`): `Apel - 1 {runId}`, lalu `Kompresor - 1 {runId}`, lalu `Kompresor - 2 {runId}`, lalu `Zebra - 1 {runId}`, lalu `anggur - 1 {runId}` dan `Kompresor - 10 {runId}`, dengan baris `Pending` di urutan terakhir
106. Klik header kolom `Purchase Cost`
107. Verifikasi urutan Purchase Cost menurun: `Zebra - 1 {runId}`, lalu `Kompresor - 2 {runId}`, lalu `Kompresor - 1 {runId}`, lalu `Apel - 1 {runId}`, dengan baris `Pending` `anggur - 1 {runId}` dan `Kompresor - 10 {runId}` tetap di urutan terakhir
108. Klik header kolom `Purchase Cost`
109. Klik header kolom `Asset Value (Commercial)`
110. Verifikasi baris `Pending` `anggur - 1 {runId}` dan `Kompresor - 10 {runId}` berada di urutan terakhir pada Asset Value (Commercial) menaik
111. Klik header kolom `Asset Value (Commercial)`
112. Klik header kolom `Asset Value (Commercial)`
113. Klik header kolom `Asset Value (Fiscal)`
114. Verifikasi baris `Pending` `anggur - 1 {runId}` dan `Kompresor - 10 {runId}` berada di urutan terakhir pada Asset Value (Fiscal) menaik
115. Klik header kolom `Asset Value (Fiscal)`
116. Klik header kolom `Asset Value (Fiscal)`
117. Klik header kolom `Warranty Expiry`
118. Verifikasi urutan Warranty Expiry menaik (Oldest First): `Apel - 1 {runId}` lalu `Kompresor - 1 {runId}` mendahului baris tanpa garansi (`—`)
119. Klik header kolom `Warranty Expiry`
120. Klik header kolom `Warranty Expiry`
121. Klik header kolom `Lokasi Rak {runId}`
122. Verifikasi urutan Lokasi Rak menaik menurut A-Z: `anggur - 1 {runId}`, `Apel - 1 {runId}`, lalu `Kompresor - 1 {runId}`, dan baris tanpa nilai di urutan terakhir
123. Klik header kolom `Lokasi Rak {runId}`
124. Klik header kolom `Lokasi Rak {runId}`
125. Klik header kolom `Asset ID`
126. Verifikasi nilai Asset ID pada keenam baris tersusun menaik menurut A-Z
127. Klik header kolom `Asset ID`
128. Klik header kolom `Asset ID`

### Nilai sama diurutkan menurut urutan bawaan dan sort pindah antar kolom
129. Klik header kolom `Modified By`
130. Verifikasi urutan Modified By menaik: `Apel - 1 {runId}` lalu `Zebra - 1 {runId}` (Modified By `Dimas Prakoso {runId}`, menurut urutan bawaan), mendahului `anggur - 1 {runId}`, `Kompresor - 1 {runId}`, `Kompresor - 2 {runId}`, dan `Kompresor - 10 {runId}` (Modified By `Wahyu Hidayat {runId}`, menurut urutan bawaan dengan Increment natural)
131. Klik header kolom `Modified By`
132. Klik header kolom `Modified By`
133. Klik header kolom `Brand`
134. Klik header kolom `Division`
135. Verifikasi indikator sort berpindah ke kolom `Division`, urutan mengikuti Division menaik `Kompresor - 1 {runId}`, lalu `anggur - 1 {runId}`, lalu `Apel - 1 {runId}`, lalu `Kompresor - 2 {runId}`, lalu `Zebra - 1 {runId}`, lalu `Kompresor - 10 {runId}`, dan Brand kembali netral
136. Klik header kolom `Division`
137. Klik header kolom `Division`
138. Verifikasi Filter-only `Purchase status` tidak memiliki kolom sehingga tidak dapat diurutkan

### Sort mencakup seluruh data lintas halaman
139. Klik node `All Groups`
140. Klik header kolom `Brand`
141. Verifikasi halaman 1 memuat `Kompresor - 1 {runId}`, `Kompresor - 2 {runId}`, `anggur - 1 {runId}`, `Kompresor - 10 {runId}`, dan `Apel - 1 {runId}` sebagai lima baris pertama, diikuti `Pilar Beton - 1 {runId}` sampai `Pilar Beton - 5 {runId}`
142. Klik tombol halaman `2`
143. Verifikasi halaman 2 memuat `Pilar Beton - 6 {runId}` sampai `Pilar Beton - 12 {runId}` dengan Brand `Zulu {runId}` sama di dua halaman, urut menurut Increment, lalu `Zebra - 1 {runId}` tanpa Brand di urutan paling akhir
144. Klik header kolom `Brand`
145. Verifikasi tombol halaman `2` tetap aktif sesudah arah sort berganti

### Sort TAG menurun mengikuti kebalikan urutan menaik
146. Klik node `Gudang Utama {runId}`
147. Klik header kolom `TAG`
148. Klik header kolom `TAG`
149. Verifikasi urutan TAG menurun: baris tanpa TAG `Zebra - 1 {runId}` paling awal, lalu `Kompresor - 2 {runId}` (`RFID`), lalu `Apel - 1 {runId}` (`QR`), lalu `anggur - 1 {runId}` (`NFC` dan `QR`), lalu `Kompresor - 1 {runId}` dan `Kompresor - 10 {runId}` (`NFC`, urutan di antara keduanya tidak diasersi) paling akhir
150. Klik header kolom `TAG`

### Sort Last Scanned menurun dengan nilai
151. Klik header kolom `Last Scanned`
152. Klik header kolom `Last Scanned`
153. Verifikasi urutan Last Scanned menurun (Newest First): baris tanpa nilai menurut urutan bawaan `anggur - 1 {runId}`, `Kompresor - 2 {runId}`, `Kompresor - 10 {runId}`, `Zebra - 1 {runId}` paling awal, lalu `Apel - 1 {runId}`, lalu `Kompresor - 1 {runId}`
154. Klik header kolom `Last Scanned`

### Sort Asset Value menaik menurut nilai
155. Klik header kolom `Asset Value (Commercial)`
156. Verifikasi urutan Asset Value (Commercial) menaik secara numerik: `Apel - 1 {runId}`, lalu `Kompresor - 1 {runId}`, lalu `Kompresor - 2 {runId}`, lalu `Zebra - 1 {runId}`, lalu baris `Pending` `anggur - 1 {runId}` dan `Kompresor - 10 {runId}`
157. Klik header kolom `Asset Value (Fiscal)`
158. Verifikasi urutan Asset Value (Fiscal) menaik secara numerik: `Apel - 1 {runId}`, lalu `Kompresor - 1 {runId}`, lalu `Kompresor - 2 {runId}`, lalu `Zebra - 1 {runId}`, lalu baris `Pending` `anggur - 1 {runId}` dan `Kompresor - 10 {runId}`

### Sort Modified By menurun dengan dua pengubah
159. Klik header kolom `Modified By`
160. Klik header kolom `Modified By`
161. Verifikasi urutan Modified By menurun: `anggur - 1 {runId}`, `Kompresor - 1 {runId}`, `Kompresor - 2 {runId}`, dan `Kompresor - 10 {runId}` (Modified By `Wahyu Hidayat {runId}`) mendahului `Apel - 1 {runId}` lalu `Zebra - 1 {runId}` (Modified By `Dimas Prakoso {runId}`)
162. Klik header kolom `Modified By`

---
id: TC-FA-FACO-E2E-004-filter-account-list
title: "Filter Panel Account List menyaring baris dan berkombinasi dengan Search"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1.1#r1", "§4.1.1#r4", "§4.1.1#r7", "§4.1.1#r8", "§5#b4", "§9.5#r2", "EB-FLT-4@tabel-account-list", "EB-FLT-7", "EB-FLT-3"]
smoke: ["EB-FLT-3"]
dependsOn: []
trace:
  "§4.1.1#r1": [20, 25, 26]
  "§4.1.1#r4": [7, 8, 60, 61]
  "§4.1.1#r7": [104, 105, 110]
  "§4.1.1#r8": [70, 73, 76, 79, 82, 88]
  "§5#b4": [30, 35, 36, 122, 125]
  "§9.5#r2": 4
  "EB-FLT-4@tabel-account-list": [35, 36, 38, 40, 41, 44, 45, 51, 54, 97, 100]
  "EB-FLT-7": [119, 120, 121, 122]
  "EB-FLT-3": [11, 12, 13, 19, 20, 21, 22]
anchor: [2, 49, 85, 93, 115, 116]
coverage:
  web: automated
---

# Filter Panel Account List menyaring baris dan berkombinasi dengan Search

## Prerequisites
- Aktor: pengguna Total Control di entitas khusus spec ini. Aktor lain pemicu: Admin B (DU-004-8).
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-004-11: entitas khusus `Entitas Uji Filter {runId}`, hanya dipakai spec ini, dan tidak berisi akun selain DU-004-1 sampai DU-004-7 dan DU-004-12. Pengguna yang mengubah akun di entitas ini hanya aktor dan Admin B (DU-004-8).
  - DU-004-1: akun `F1-{runId}`, Account Name `Alfa Mitra FLT {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-004-2: akun `F2-{runId}`, Account Name `Beta FLT {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-004-3: akun `F3-{runId}`, Account Name `Gamma Mitra FLT {runId}`, Account Function `Depreciation Expense`, Status `Active`.
  - DU-004-4: akun `F4-{runId}`, Account Name `Delta FLT {runId}`, Account Function `Depreciation Expense`, Status `Inactive`.
  - DU-004-5: akun `F5-{runId}`, Account Name `Epsilon FLT {runId}`, Account Function `Gain on Disposal`, Status `Active`.
  - DU-004-6: akun `F6-{runId}`, Account Name `Zeta FLT {runId}`, Account Function `Asset Cost`, Status `Active`. Account Function sesudah Edit: `Gain on Disposal`.
  - DU-004-7: akun `F7-{runId}`, Account Name `Eta FLT {runId}`, Account Function `Gain on Disposal`, Status `Active`. Account Function sesudah diubah Admin B: `Asset Cost`.
  - DU-004-8: Admin B, nama `Admin B {runId}`, role Total Control, cakupan seluruh client, akun aktif dan kredensialnya disediakan fase 2.
  - DU-004-12: akun `F8-{runId}`, Account Name `Hasil Pelepasan {runId}`, Account Function `Disposal Proceeds`, Status `Active`. Satu-satunya akun ber-Function `Disposal Proceeds` di entitas ini, tanpa entri Changelog sama sekali. Nama akunnya tidak memuat kata kunci Search yang dipakai kelompok langkah sebelumnya. Dihapus Admin B pada kelompok langkah terakhir.
- Kondisi:
  - Seluruh akun DU-004-1 sampai DU-004-7 dibuat pada hari run (T0), sehingga Last Updated akun yang belum diubah adalah T0.
  - Seluruh akun DU-004-1 sampai DU-004-5 tanpa entri Changelog sama sekali (belum pernah diubah oleh siapa pun), sehingga Modified By-nya `System` dan opsi `System` ada di field Modified By. Hal yang sama berlaku untuk DU-004-12.
  - Ukuran halaman tabel adalah 10 baris (nilai bawaan).

## Test Steps
### Tidak ada filter bawaan
1. Ketik Search `FLT {runId}`, tekan Enter
2. Verifikasi baris `F1-{runId}` tampil
3. Klik ikon Filter
4. Verifikasi tidak ada nilai yang terpilih di field Filter Panel mana pun, termasuk field Active

### Filter Function menampilkan baris yang cocok
5. Pilih `Asset Cost` pada field Function
6. Klik `[Apply]`
7. Verifikasi baris `F1-{runId}` tampil karena Function-nya `Asset Cost`
8. Verifikasi baris `F3-{runId}` tidak tampil karena Function-nya `Depreciation Expense`

### Beberapa nilai dalam satu field berlaku OR
9. Pilih `Gain on Disposal` pada field Function
10. Klik `[Apply]`
11. Verifikasi baris `F5-{runId}` tampil karena Function-nya `Gain on Disposal`
12. Verifikasi baris `F1-{runId}` tetap tampil karena Function-nya `Asset Cost`
13. Verifikasi baris `F3-{runId}` tidak tampil karena Function-nya bukan salah satu nilai yang dipilih
14. Klik `[Clear Field]`
15. Klik `[Apply]`

### Antar-field berlaku AND
16. Pilih `Asset Cost` pada field Function
17. Pilih `Active` pada field Active
18. Klik `[Apply]`
19. Verifikasi baris `F1-{runId}` tampil karena Function-nya `Asset Cost` dan Status-nya `Active`
20. Verifikasi baris `F2-{runId}` tidak tampil karena Function-nya cocok tetapi Status-nya `Inactive`
21. Verifikasi baris `F3-{runId}` tidak tampil karena Status-nya cocok tetapi Function-nya `Depreciation Expense`
22. Verifikasi baris `F4-{runId}` tidak tampil karena Function dan Status-nya sama-sama tidak cocok

### Filter Active dengan kedua nilai
23. Pilih `Inactive` pada field Active
24. Klik `[Apply]`
25. Verifikasi baris `F2-{runId}` tampil karena Status-nya `Inactive` termasuk nilai yang dipilih
26. Verifikasi baris `F1-{runId}` tetap tampil karena Status-nya `Active` termasuk nilai yang dipilih
27. Klik `[Clear Field]`
28. Klik `[Apply]`

### Search dan Filter berlaku bersamaan dengan AND, Search lebih dulu
29. Ganti isi kotak Search dengan `Mitra FLT {runId}`, tekan Enter
30. Verifikasi baris `F3-{runId}` tampil karena cocok dengan Search
31. Pilih `Asset Cost` pada field Function
32. Klik `[Apply]`
33. Klik header kolom Account Code (klik pertama)
34. Klik header kolom Account Code (klik kedua)
35. Verifikasi baris `F1-{runId}` tampil karena cocok dengan Search dan Filter
36. Verifikasi baris `F3-{runId}` tidak tampil karena cocok dengan Search tetapi tidak dengan Filter

### Clear Search mempertahankan Filter dan Sort
37. Klik `(←)` pada kotak Search
38. Verifikasi nilai `Asset Cost` pada field Function di Filter Panel tetap terpilih
39. Ketik Search `FLT {runId}`, tekan Enter
40. Verifikasi baris `F2-{runId}` tampil di atas baris `F1-{runId}` sesuai urutan Account Code menurun, dan keduanya cocok dengan Filter walau tidak dengan Search sebelumnya
41. Verifikasi baris `F3-{runId}` tidak tampil karena Filter Function masih aktif

### Clear Filter mempertahankan Search dan Sort
42. Klik `[Clear Field]`
43. Klik `[Apply]`
44. Verifikasi baris `F3-{runId}` tampil kembali karena Filter dilepas
45. Verifikasi urutan baris menurun menurut Account Code: `F7-{runId}`, `F6-{runId}`, `F5-{runId}`, `F4-{runId}`, `F3-{runId}`, `F2-{runId}`, `F1-{runId}`
46. Klik header kolom Account Code (klik ketiga)

### Filter dulu lalu Search menghasilkan irisan kosong yang pulih saat satu saringan dilepas
47. Pilih `Gain on Disposal` pada field Function
48. Klik `[Apply]`
49. Verifikasi baris `F5-{runId}` tampil karena Function-nya `Gain on Disposal`
50. Ganti isi kotak Search dengan `Mitra FLT {runId}`, tekan Enter
51. Verifikasi `No results found` tampil karena Search dan Filter masing-masing punya hasil tetapi irisannya kosong
52. Klik `[Clear Field]`
53. Klik `[Apply]`
54. Verifikasi baris `F1-{runId}` tampil kembali karena hanya Search yang tersisa

### Filter tetap bekerja pada kolom yang di-hide
55. Klik header kolom Actions `⋯`
56. Hapus centang `Function` pada panel Column Visibility
57. Klik header kolom Actions `⋯` untuk menutup panel
58. Pilih `Asset Cost` pada field Function
59. Klik `[Apply]`
60. Verifikasi baris `F1-{runId}` tampil karena Function-nya `Asset Cost` walau kolom Function di-hide
61. Verifikasi baris `F3-{runId}` tidak tampil karena Function-nya `Depreciation Expense` walau kolom Function di-hide
62. Klik `[Clear Field]`
63. Klik `[Apply]`
64. Klik header kolom Actions `⋯`
65. Centang `Function` pada panel Column Visibility
66. Klik header kolom Actions `⋯` untuk menutup panel

### Filter Last Updated dengan rentang tanggal inklusif
67. Ganti isi kotak Search dengan `FLT {runId}`, tekan Enter
68. Pilih rentang tanggal dari T0 sampai T0 (satu hari) pada field Last Updated
69. Klik `[Apply]`
70. Verifikasi baris `F1-{runId}` tampil karena Last Updated-nya T0 ada di dalam rentang satu hari
71. Pilih rentang tanggal dari T0 − 7 hari sampai T0 + 7 hari pada field Last Updated
72. Klik `[Apply]`
73. Verifikasi baris `F1-{runId}` tampil karena T0 ada di dalam rentang
74. Pilih rentang tanggal dari T0 sampai T0 + 7 hari pada field Last Updated
75. Klik `[Apply]`
76. Verifikasi baris `F1-{runId}` tampil karena T0 tepat di tanggal awal rentang
77. Pilih rentang tanggal dari T0 − 7 hari sampai T0 pada field Last Updated
78. Klik `[Apply]`
79. Verifikasi baris `F1-{runId}` tampil karena T0 tepat di tanggal akhir rentang
80. Pilih rentang tanggal dari T0 + 1 hari sampai T0 + 7 hari pada field Last Updated
81. Klik `[Apply]`
82. Verifikasi `No results found` tampil karena T0 di luar rentang
83. Klik `[Clear Field]`
84. Klik `[Apply]`
85. Verifikasi baris `F1-{runId}` tampil kembali karena Filter dilepas
86. Pilih rentang tanggal dari T0 − 7 hari sampai T0 − 1 hari pada field Last Updated
87. Klik `[Apply]`
88. Verifikasi `No results found` tampil karena T0 di luar rentang
89. Klik `[Clear Field]`
90. Klik `[Apply]`

### Record yang diubah sehingga keluar atau masuk kriteria Filter
91. Pilih `Asset Cost` pada field Function
92. Klik `[Apply]`
93. Verifikasi baris `F6-{runId}` tampil karena Function-nya `Asset Cost`
94. Klik `⋯` pada baris `F6-{runId}` > `Edit`
95. Pilih `Gain on Disposal` pada field Account Function
96. Klik `[Save]`
97. Verifikasi baris `F6-{runId}` tidak tampil karena Function-nya kini `Gain on Disposal` dan tidak cocok dengan Filter
98. Admin B mengubah Account Function `F7-{runId}` menjadi `Asset Cost`
99. Klik `[Apply]`
100. Verifikasi baris `F7-{runId}` tampil karena Function-nya kini `Asset Cost` dan cocok dengan Filter

### Filter Modified By
101. Klik `[Clear Field]`
102. Pilih `System` pada field Modified By
103. Klik `[Apply]`
104. Verifikasi baris `F1-{runId}` tampil karena Modified By-nya `System`
105. Verifikasi baris `F6-{runId}` tidak tampil karena Modified By-nya kini aktor yang mengubahnya

### Opsi filter Modified By berasal dari data tabel
106. Klik `[Clear Field]`
107. Klik `[Apply]`
108. Klik `(←)` pada kotak Search
109. Buka dropdown field Modified By
110. Verifikasi opsi field Modified By adalah `System`, nama aktor yang mengubah `F6-{runId}`, dan nama Admin B yang mengubah `F7-{runId}`
111. Tutup dropdown field Modified By

### Nilai filter Function yang stale tetap tercantum dan dibersihkan dari kriteria saat Apply
112. Pilih `Asset Cost` pada field Function
113. Pilih `Disposal Proceeds` pada field Function
114. Klik `[Apply]`
115. Verifikasi baris `F8-{runId}` tampil karena Function-nya `Disposal Proceeds`
116. Verifikasi baris `F1-{runId}` tampil karena Function-nya `Asset Cost`
117. Admin B menghapus akun `F8-{runId}`, akun terakhir ber-Function `Disposal Proceeds` di entitas ini
118. Klik `[Apply]`
119. Verifikasi baris `F1-{runId}` tampil karena tabel mengikuti kriteria yang tersisa, yaitu Function `Asset Cost`
120. Verifikasi baris `F8-{runId}` tidak tampil karena akunnya sudah dihapus
121. Verifikasi pesan error `Unable to load this data.` tidak tampil
122. Verifikasi field Function masih mencantumkan `Disposal Proceeds` dan `Asset Cost` sebagai nilai terpilih walau tidak ada lagi akun ber-Function `Disposal Proceeds`
123. Hapus centang `Disposal Proceeds` pada field Function
124. Klik `[Apply]`
125. Verifikasi field Function hanya mencantumkan `Asset Cost` sebagai nilai terpilih

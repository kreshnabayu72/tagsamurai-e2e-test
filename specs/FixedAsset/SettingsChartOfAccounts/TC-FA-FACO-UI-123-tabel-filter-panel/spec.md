---
id: TC-FA-FACO-UI-123-tabel-filter-panel
title: "Tab Chart of Accounts: Filter Panel dan indikator filter aktif"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1.1#r1", "§4.1.1#r4", "§4.1.1#r5", "§4.1.1#r6", "§4.1.1#r7", "§4.1.1#r8", "§5#b4", "EB-FLT-2@tabel-account-list", "EB-FLT-6@tabel-account-list"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r1": [3, 4, 5]
  "§4.1.1#r4": [3, 6, 7]
  "§4.1.1#r5": [3, 8, 9]
  "§4.1.1#r6": [3, 10, 11]
  "§4.1.1#r7": [3, 12, 13]
  "§4.1.1#r8": [3, 14, 15]
  "§5#b4": [3, 23, 25, 31, 98, 104]
  "EB-FLT-2@tabel-account-list": [19, 21, 22, 23, 25, 28, 30, 31, 36, 38, 45, 47, 49, 51, 52, 63, 68, 69, 71, 73, 77, 95, 96, 97, 98, 100, 102, 103, 104]
  "EB-FLT-6@tabel-account-list": [82, 85, 87, 88]
anchor: []
coverage:
  web: automated
---

# Tab Chart of Accounts: Filter Panel dan indikator filter aktif

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Tab Chart of Accounts
- Data:
  - DU-123-1: Account `1-1001`, Name `Fixed Assets – Equipment`, Function `Asset Cost`, status Active, Used By `3`, Modified By `Rina Pratiwi`.
  - DU-123-2: Account `1-2001`, Name `Accumulated Depreciation – Equipment`, Function `Accumulated Depreciation`, status Active, Used By `2`, Modified By `Budi`.
  - DU-123-3: Account `5-6001`, Name `Depreciation Expense – Admin`, Function `Depreciation Expense`, status Active, Used By `0`, Modified By `Rina Pratiwi`.
  - DU-123-4: Account `4-7001`, Name `Gain on Disposal`, Function `Gain on Disposal`, status Inactive, Used By `0`, Modified By `Budi`.
  - DU-123-5: Account `4-7002`, Name `Gain and Loss on Disposal`, Function `Loss on Disposal`, status Active, Used By `2`, Modified By `Rina Pratiwi`.
  - DU-123-6: Account `6-2001`, Name `Repairs & Maintenance Expense`, Function `Capitalization Offset`, status Active, Used By `0`, Modified By `Budi`.
  - DU-123-7: Account `1-3001`, Name `Disposal Proceeds – Clearing`, Function `Disposal Proceeds`, status Active, Used By `1`, Modified By `Rina Pratiwi`.
  - DU-123-8: daftar akun kosong, jumlah akun `0`.
  - DU-123-9: kata cari di dalam dropdown Function: `Dep`, `asset cost`, dan `Zzz`.
- Kondisi:
  - K1: tabel berisi DU-123-1 sampai DU-123-7, Filter Panel tertutup tanpa filter ter-Apply.
  - K2: seperti K1; Filter Function `Asset Cost` hanya menghasilkan akun DU-123-1.
  - K3: daftar akun kosong menurut DU-123-8.
  - K4: seperti K1; Filter Function `Gain on Disposal` dan `Loss on Disposal` bersama filter Active `Active` hanya menghasilkan akun DU-123-5.
  - K5: seperti K1; field `Function` di Filter Panel selebar itu sehingga hanya sebagian dari ketujuh chip opsi terpilih yang muat, dan selebihnya tidak muat.

## Test Steps

### Field Filter Panel dan kontrolnya
1. Tampilkan Tab Chart of Accounts dengan kondisi K1
2. Klik ikon Filter
3. Verifikasi Filter Panel memuat field `Active`, `Function`, `Used By`, `Last Used in Journal`, `Modified By`, dan `Last Updated`
4. Verifikasi field `Active` berupa dropdown multi-select yang searchable
5. Verifikasi field `Active` memuat placeholder `All statuses`
6. Verifikasi field `Function` berupa dropdown multi-select yang searchable
7. Verifikasi field `Function` memuat placeholder `All functions`
8. Verifikasi field `Used By` berupa dua input angka untuk rentang nilai
9. Verifikasi input field `Used By` memuat placeholder `Min` dan `Max`
10. Verifikasi field `Last Used in Journal` berupa pemilih rentang periode dengan granularitas bulan
11. Verifikasi field `Last Used in Journal` memuat placeholder `Select date`
12. Verifikasi field `Modified By` berupa dropdown multi-select yang searchable
13. Verifikasi field `Modified By` memuat placeholder `All users`
14. Verifikasi field `Last Updated` berupa pemilih rentang tanggal
15. Verifikasi field `Last Updated` memuat placeholder `Select date`

### Draf, Apply, dan badge titik indikator filter aktif
16. Tampilkan Tab Chart of Accounts dengan kondisi K2
17. Klik ikon Filter
18. Pilih `Asset Cost` pada filter Function
19. Verifikasi baris `1-2001` tetap tampil sebelum `[Apply]` diklik
20. Klik `[Apply]`
21. Verifikasi baris `1-1001` tampil
22. Verifikasi baris `1-2001` tidak tampil
23. Verifikasi badge titik indikator filter aktif tampil pada ikon Filter selama panel Filter terbuka
24. Klik ikon Filter
25. Verifikasi badge titik indikator filter aktif tetap tampil pada ikon Filter selama panel Filter tertutup
26. Klik ikon Filter
27. Klik `[Clear Field]`
28. Verifikasi baris `1-2001` tetap tidak tampil sebelum `[Apply]` diklik
29. Klik `[Apply]`
30. Verifikasi baris `1-2001` tampil kembali
31. Verifikasi badge titik indikator filter aktif pada ikon Filter hilang

### Menutup panel tanpa Apply membuang draf
32. Tampilkan Tab Chart of Accounts dengan kondisi K2
33. Klik ikon Filter
34. Pilih `Asset Cost` pada filter Function
35. Klik ikon Filter
36. Verifikasi baris `1-2001` tetap tampil
37. Klik ikon Filter
38. Verifikasi field `Function` memuat placeholder `All functions`

### Chip opsi, uncheck, dan hapus chip
39. Tampilkan Tab Chart of Accounts dengan kondisi K2
40. Klik ikon Filter
41. Klik field `Function`
42. Pilih `Asset Cost`
43. Pilih `Gain on Disposal`
44. Pilih `Loss on Disposal`
45. Verifikasi chip `Asset Cost`, `Gain on Disposal`, dan `Loss on Disposal` tampil pada field `Function`
46. Klik opsi `Loss on Disposal` pada daftar opsi untuk menghilangkan centang
47. Verifikasi chip `Loss on Disposal` tidak tampil pada field `Function`
48. Klik `(✕)` pada chip `Gain on Disposal`
49. Verifikasi chip `Gain on Disposal` tidak tampil pada field `Function`
50. Klik `[Apply]`
51. Verifikasi baris `1-1001` tampil
52. Verifikasi baris `4-7001` tidak tampil

### Chip overflow
53. Tampilkan Tab Chart of Accounts dengan kondisi K5
54. Klik ikon Filter
55. Klik field `Function`
56. Pilih `Asset Cost`
57. Pilih `Accumulated Depreciation`
58. Pilih `Depreciation Expense`
59. Pilih `Gain on Disposal`
60. Pilih `Loss on Disposal`
61. Pilih `Capitalization Offset`
62. Pilih `Disposal Proceeds`
63. Verifikasi opsi terpilih yang tidak muat diringkas dalam satu chip `+N more`, dengan jumlah chip yang tampil ditambah N sama dengan `7`

### Search di dalam dropdown
64. Tampilkan Tab Chart of Accounts dengan kondisi K1
65. Klik ikon Filter
66. Klik field `Function`
67. Ketik `Dep` pada kotak cari di dalam dropdown `Function`
68. Verifikasi opsi `Accumulated Depreciation` dan `Depreciation Expense` tampil
69. Verifikasi opsi `Asset Cost` tidak tampil
70. Ganti isi kotak cari dengan `asset cost`
71. Verifikasi opsi `Asset Cost` tampil
72. Ganti isi kotak cari dengan `Zzz`
73. Verifikasi teks `No results found` tampil

### Sumber opsi kosong
74. Tampilkan Tab Chart of Accounts dengan kondisi K3
75. Klik ikon Filter
76. Klik field `Function`
77. Verifikasi teks `No options available` tampil

### Menyembunyikan kolom tidak menghapus filter
78. Tampilkan Tab Chart of Accounts dengan kondisi K2
79. Klik ikon Filter
80. Pilih `Asset Cost` pada filter Function
81. Klik `[Apply]`
82. Verifikasi baris `1-1001` tampil
83. Klik `⋯` pada header kolom Actions
84. Hilangkan centang `Function` pada panel Column Visibility
85. Verifikasi header kolom `Function` tidak tampil
86. Klik ikon Filter
87. Verifikasi field `Function` masih ada di Filter Panel
88. Verifikasi baris `4-7001` tetap tidak tampil

### Clear Field melepas seluruh filter yang ter-Apply
89. Tampilkan Tab Chart of Accounts dengan kondisi K4
90. Klik ikon Filter
91. Pilih `Gain on Disposal` pada filter Function
92. Pilih `Loss on Disposal` pada filter Function
93. Pilih `Active` pada filter Active
94. Klik `[Apply]`
95. Verifikasi baris `4-7002` tampil
96. Verifikasi baris `1-1001` tidak tampil
97. Verifikasi baris `4-7001` tidak tampil
98. Verifikasi badge titik indikator filter aktif tampil pada ikon Filter
99. Klik `[Clear Field]`
100. Verifikasi baris `1-1001` tetap tidak tampil sebelum `[Apply]` diklik
101. Klik `[Apply]`
102. Verifikasi baris `1-1001` tampil kembali
103. Verifikasi baris `4-7001` tampil kembali
104. Verifikasi badge titik indikator filter aktif pada ikon Filter hilang

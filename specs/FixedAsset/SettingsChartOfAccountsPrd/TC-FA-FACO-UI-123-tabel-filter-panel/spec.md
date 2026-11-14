---
id: TC-FA-FACO-UI-123-tabel-filter-panel
title: "Tab Chart of Accounts: Filter Panel dan chip filter"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1.1#r1", "§4.1.1#r4", "§4.1.1#r5", "§4.1.1#r6", "§4.1.1#r7", "§4.1.1#r8", "§4.1.1#b2", "§4.4#r5", "§5#b3", "EB-FLT-2@tabel-account-list", "EB-FLT-6@tabel-account-list"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r1": [3, 4, 5]
  "§4.1.1#r4": [3, 6, 7]
  "§4.1.1#r5": [3, 8, 9]
  "§4.1.1#r6": [3, 10, 11]
  "§4.1.1#r7": [3, 12, 13]
  "§4.1.1#r8": [3, 14, 15]
  "§4.1.1#b2": 11
  "§4.4#r5": [27, 28, 29, 97, 98, 99, 100]
  "§5#b3": [3, 24, 25, 95]
  "EB-FLT-2@tabel-account-list": [19, 21, 22, 23, 92, 93, 94, 34, 36, 43, 45, 47, 49, 50, 61, 66, 67, 69, 71, 75]
  "EB-FLT-6@tabel-account-list": [80, 83, 84, 85]
anchor: []
coverage:
  web: automated
---

# Tab Chart of Accounts: Filter Panel dan chip filter

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
11. Verifikasi field `Last Used in Journal` memuat placeholder `Select date`[^drift-1]
12. Verifikasi field `Modified By` berupa dropdown multi-select yang searchable
13. Verifikasi field `Modified By` memuat placeholder `All users`
14. Verifikasi field `Last Updated` berupa pemilih rentang tanggal
15. Verifikasi field `Last Updated` memuat placeholder `Select date`

### Draf, Apply, chip filter aktif, dan Clear all
16. Tampilkan Tab Chart of Accounts dengan kondisi K2
17. Klik ikon Filter
18. Pilih `Asset Cost` pada filter Function
19. Verifikasi baris `1-2001` tetap tampil sebelum `[Apply]` diklik
20. Klik `[Apply]`
21. Verifikasi baris `1-1001` tampil
22. Verifikasi baris `1-2001` tidak tampil
23. Verifikasi penanda filter aktif tampil pada ikon Filter
24. Verifikasi chip filter aktif tampil di atas tabel
25. Verifikasi `Clear all` tampil di dekat chip filter aktif
26. Klik `Clear all`
27. Verifikasi chip filter aktif tidak tampil
28. Verifikasi baris `1-2001` tampil kembali
29. Verifikasi penanda filter aktif pada ikon Filter hilang

### Menutup panel tanpa Apply membuang draf
30. Tampilkan Tab Chart of Accounts dengan kondisi K2
31. Klik ikon Filter
32. Pilih `Asset Cost` pada filter Function
33. Klik ikon Filter
34. Verifikasi baris `1-2001` tetap tampil
35. Klik ikon Filter
36. Verifikasi field `Function` memuat placeholder `All functions`

### Chip opsi, uncheck, dan hapus chip
37. Tampilkan Tab Chart of Accounts dengan kondisi K2
38. Klik ikon Filter
39. Klik field `Function`
40. Pilih `Asset Cost`
41. Pilih `Gain on Disposal`
42. Pilih `Loss on Disposal`
43. Verifikasi chip `Asset Cost`, `Gain on Disposal`, dan `Loss on Disposal` tampil pada field `Function`
44. Klik opsi `Loss on Disposal` pada daftar opsi untuk menghilangkan centang
45. Verifikasi chip `Loss on Disposal` tidak tampil pada field `Function`
46. Klik `(✕)` pada chip `Gain on Disposal`
47. Verifikasi chip `Gain on Disposal` tidak tampil pada field `Function`
48. Klik `[Apply]`
49. Verifikasi baris `1-1001` tampil
50. Verifikasi baris `4-7001` tidak tampil

### Chip overflow
51. Tampilkan Tab Chart of Accounts dengan kondisi K1
52. Klik ikon Filter
53. Klik field `Function`
54. Pilih `Asset Cost`
55. Pilih `Accumulated Depreciation`
56. Pilih `Depreciation Expense`
57. Pilih `Gain on Disposal`
58. Pilih `Loss on Disposal`
59. Pilih `Capitalization Offset`
60. Pilih `Disposal Proceeds`
61. Verifikasi opsi terpilih yang tidak muat diringkas dalam satu chip `+N more`, dengan jumlah chip yang tampil ditambah N sama dengan `7`

### Search di dalam dropdown
62. Tampilkan Tab Chart of Accounts dengan kondisi K1
63. Klik ikon Filter
64. Klik field `Function`
65. Ketik `Dep` pada kotak cari di dalam dropdown `Function`
66. Verifikasi opsi `Accumulated Depreciation` dan `Depreciation Expense` tampil
67. Verifikasi opsi `Asset Cost` tidak tampil
68. Ganti isi kotak cari dengan `asset cost`
69. Verifikasi opsi `Asset Cost` tampil
70. Ganti isi kotak cari dengan `Zzz`
71. Verifikasi teks `No results found` tampil

### Sumber opsi kosong
72. Tampilkan Tab Chart of Accounts dengan kondisi K3
73. Klik ikon Filter
74. Klik field `Function`
75. Verifikasi teks `No options available` tampil

### Menyembunyikan kolom tidak menghapus filter
76. Tampilkan Tab Chart of Accounts dengan kondisi K2
77. Klik ikon Filter
78. Pilih `Asset Cost` pada filter Function
79. Klik `[Apply]`
80. Verifikasi baris `1-1001` tampil
81. Klik `⋯` pada header kolom Actions
82. Hilangkan centang `Function` pada panel Column Visibility
83. Verifikasi header kolom `Function` tidak tampil
84. Verifikasi field `Function` masih ada di Filter Panel
85. Verifikasi baris `4-7001` tetap tidak tampil

### Clear all melepas seluruh filter
86. Tampilkan Tab Chart of Accounts dengan kondisi K4
87. Klik ikon Filter
88. Pilih `Gain on Disposal` pada filter Function
89. Pilih `Loss on Disposal` pada filter Function
90. Pilih `Active` pada filter Active
91. Klik `[Apply]`
92. Verifikasi baris `4-7002` tampil
93. Verifikasi baris `1-1001` tidak tampil
94. Verifikasi baris `4-7001` tidak tampil
95. Verifikasi chip filter aktif untuk filter Function dan filter Active tampil di atas tabel
96. Klik `Clear all`
97. Verifikasi chip filter aktif tidak tampil
98. Verifikasi baris `1-1001` tampil kembali
99. Verifikasi baris `4-7001` tampil kembali
100. Verifikasi penanda filter aktif pada ikon Filter hilang

[^drift-1]: Drift PRD vs foundation. PRD §4.1.1 (kolom Last Used in Journal dan Deviasi): placeholder filter `Select period`, bukan `Select date`. foundation `prd-conventions.md` §9.8 (Filter tanggal): placeholder `Select date`. Diasersi: foundation, karena Filter Panel adalah pola bersama (SB-4).

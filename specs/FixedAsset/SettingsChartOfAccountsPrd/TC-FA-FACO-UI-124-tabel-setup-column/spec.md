---
id: TC-FA-FACO-UI-124-tabel-setup-column
title: "Tab Chart of Accounts: Column Visibility dan Setup Column"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1#r5", "§4.4#r7", "§5#b9", "EB-KOL-1@tabel-account-list", "EB-KOL-3"]
smoke: []
dependsOn: []
trace:
  "§4.1#r5": 6
  "§4.4#r7": [3, 4, 6]
  "§5#b9": [17, 18, 46, 48, 49, 51, 54, 55]
  "EB-KOL-1@tabel-account-list": [10, 11, 12, 13, 14, 15, 16, 23, 25, 26, 30, 32, 37, 39, 46, 48, 49, 51, 62, 63, 64, 69, 71, 80, 82, 97, 98, 105, 106]
  "EB-KOL-3": [88, 90]
anchor: []
coverage:
  web: automated
---

# Tab Chart of Accounts: Column Visibility dan Setup Column

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Tab Chart of Accounts
- Data:
  - DU-124-1: Account `1-1001`, Name `Fixed Assets – Equipment`, Function `Asset Cost`, status Active, Used By `3`, Last Used in Journal `Oct 2026`.
  - DU-124-2: entri Changelog dengan Action `Edit`, Account Code `1-1001`, Field `Account Name`, Old Value `Fixed Asset Equipment`, New Value `Fixed Assets – Equipment`, Modified By `Rina Pratiwi`.
- Kondisi:
  - K1: tabel berisi DU-124-1 dengan kolom tampil menurut bawaan dan belum ada konfigurasi kolom tersimpan.
  - K2: seperti K1, dengan seluruh kolom ditampilkan dan area tabel lebih sempit daripada total lebar kolom.
  - K3: seperti K1; modal Changelog berisi DU-124-2.

## Test Steps

### Membuka Setup Column dari Column Visibility
1. Tampilkan Tab Chart of Accounts dengan kondisi K1
2. Klik `⋯` pada header kolom Actions
3. Verifikasi panel Column Visibility tampil
4. Verifikasi item `Setup Column...` tampil di bagian bawah panel
5. Klik `Setup Column...`
6. Verifikasi modal `Setup Column` tampil

### Anatomi modal Setup Column
7. Tampilkan Tab Chart of Accounts dengan kondisi K1
8. Klik `⋯` pada header kolom Actions
9. Klik `Setup Column...`
10. Verifikasi judul modal `Setup Column` tampil
11. Verifikasi deskripsi `Drag and drop to rearrange the order and click the pin to freeze up to 3 columns.` tampil
12. Verifikasi ikon `[✕]` tampil di modal
13. Verifikasi tombol `[Reset to Default]` dan `[Save]` tampil
14. Verifikasi tidak ada tombol `[Cancel]` di modal
15. Verifikasi daftar kolom memuat baris `Active`, `Account Code`, `Account Name`, `Function`, `Used By`, `Last Used in Journal`, `Modified By`, dan `Last Updated`
16. Verifikasi kolom Checkbox dan kolom Actions tidak muncul sebagai baris pada daftar kolom
17. Verifikasi tidak ada baris kolom data yang berstatus pin
18. Verifikasi tidak ada pilihan preset tampilan tabel di modal

### Hide kolom dari preview sampai Save
19. Tampilkan Tab Chart of Accounts dengan kondisi K1
20. Klik `⋯` pada header kolom Actions
21. Klik `Setup Column...`
22. Hilangkan centang `Used By` pada daftar kolom
23. Verifikasi header kolom `Used By` tidak tampil pada tabel di balik modal
24. Klik `[Save]`
25. Verifikasi modal `Setup Column` tertutup
26. Verifikasi header kolom `Used By` tidak tampil pada tabel
27. Klik `⋯` pada header kolom Actions
28. Klik `Setup Column...`
29. Centang `Used By` pada daftar kolom
30. Verifikasi header kolom `Used By` tampil pada tabel di balik modal
31. Klik `[Save]`
32. Verifikasi header kolom `Used By` tampil pada tabel

### Urutan kolom diubah lewat drag and drop
33. Tampilkan Tab Chart of Accounts dengan kondisi K1
34. Klik `⋯` pada header kolom Actions
35. Klik `Setup Column...`
36. Seret baris `Function` ke atas baris `Account Name` pada daftar kolom
37. Verifikasi header kolom `Function` berada sebelum header kolom `Account Name` pada tabel di balik modal
38. Klik `[Save]`
39. Verifikasi header kolom `Function` berada sebelum header kolom `Account Name` pada tabel

### Pin kolom data dan batas tiga kolom
40. Tampilkan Tab Chart of Accounts dengan kondisi K1
41. Klik `⋯` pada header kolom Actions
42. Klik `Setup Column...`
43. Klik ikon pin pada baris `Account Code`
44. Klik ikon pin pada baris `Account Name`
45. Klik ikon pin pada baris `Function`
46. Verifikasi baris `Account Code`, `Account Name`, dan `Function` berstatus pin
47. Arahkan kursor ke ikon pin pada baris `Used By`
48. Verifikasi ikon pin pada baris `Used By` disabled
49. Verifikasi `Maximum 3 columns can be pinned at once. Unpin another column first.` tersampaikan pada ikon pin baris `Used By`
50. Klik ikon pin pada baris `Function`
51. Verifikasi ikon pin pada baris `Used By` aktif kembali

### Kolom Checkbox dan Actions selalu terpin
52. Tampilkan Tab Chart of Accounts dengan kondisi K2
53. Gulir tabel ke kanan sampai kolom paling kanan terlihat
54. Verifikasi kolom Checkbox tetap terlihat di sisi kiri tabel
55. Verifikasi kolom Actions `⋯` tetap terlihat di sisi kanan tabel

### Reset to Default
56. Tampilkan Tab Chart of Accounts dengan kondisi K1
57. Klik `⋯` pada header kolom Actions
58. Klik `Setup Column...`
59. Hilangkan centang `Used By` pada daftar kolom
60. Centang `Modified By` pada daftar kolom
61. Klik `[Reset to Default]`
62. Verifikasi baris `Used By` tercentang pada daftar kolom
63. Verifikasi baris `Modified By` tidak tercentang pada daftar kolom
64. Verifikasi header kolom `Used By` tampil pada tabel di balik modal

### Menutup modal tanpa Save membuang perubahan
65. Tampilkan Tab Chart of Accounts dengan kondisi K1
66. Klik `⋯` pada header kolom Actions
67. Klik `Setup Column...`
68. Hilangkan centang `Function` pada daftar kolom
69. Verifikasi header kolom `Function` tidak tampil pada tabel di balik modal
70. Klik `[✕]` pada modal
71. Verifikasi header kolom `Function` tampil pada tabel

### Kolom terakhir tidak bisa disembunyikan
72. Tampilkan Tab Chart of Accounts dengan kondisi K1
73. Klik `⋯` pada header kolom Actions
74. Klik `Setup Column...`
75. Hilangkan centang `Active` pada daftar kolom
76. Hilangkan centang `Account Name` pada daftar kolom
77. Hilangkan centang `Function` pada daftar kolom
78. Hilangkan centang `Used By` pada daftar kolom
79. Hilangkan centang `Last Used in Journal` pada daftar kolom
80. Verifikasi checkbox baris `Account Code` disabled
81. Arahkan kursor ke checkbox baris `Account Code`
82. Verifikasi `At least one column must remain visible.` tersampaikan pada checkbox baris `Account Code`

### Konfigurasi kolom satu tabel tidak mengubah tabel lain
83. Tampilkan Tab Chart of Accounts dengan kondisi K3
84. Klik `⋯` pada header kolom Actions
85. Klik `Setup Column...`
86. Hilangkan centang `Account Code` pada daftar kolom
87. Klik `[Save]`
88. Verifikasi header kolom `Account Code` tidak tampil pada tabel Account List
89. Klik ikon Changelog
90. Verifikasi header kolom `Account Code` tampil pada tabel modal `Changelog: Chart of Accounts`

### Kolom data yang di-pin tetap terlihat saat gulir horizontal
91. Tampilkan Tab Chart of Accounts dengan kondisi K2
92. Klik `⋯` pada header kolom Actions
93. Klik `Setup Column...`
94. Klik ikon pin pada baris `Account Code`
95. Klik `[Save]`
96. Gulir tabel ke kanan sampai kolom paling kanan terlihat
97. Verifikasi header kolom `Last Updated` terlihat
98. Verifikasi header kolom `Account Code` tetap terlihat

### Reset to Default mengembalikan urutan dan pin
99. Tampilkan Tab Chart of Accounts dengan kondisi K1
100. Klik `⋯` pada header kolom Actions
101. Klik `Setup Column...`
102. Seret baris `Function` ke atas baris `Account Name` pada daftar kolom
103. Klik ikon pin pada baris `Account Code`
104. Klik `[Reset to Default]`
105. Verifikasi baris `Function` berada sesudah baris `Account Name` pada daftar kolom
106. Verifikasi tidak ada baris kolom data yang berstatus pin

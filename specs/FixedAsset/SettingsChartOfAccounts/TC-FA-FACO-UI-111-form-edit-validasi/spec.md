---
id: TC-FA-FACO-UI-111-form-edit-validasi
title: "Form Edit Account: validasi per field simetris dengan Create"
layer: ui-client
priority: Medium
caseType: Negative
status: draft
sourceRules: [V-01, V-02, V-03, V-04, V-05, V-06, V-07, V-08, §[F-FACO-02] Edit Account#b2, EB-FRM-6@form-edit-account, EB-FRM-8@account-code, EB-FRM-8@account-name, EB-FRM-8@account-function]
smoke: []
dependsOn: []
trace:
  V-01: [6, 10, 18]
  V-02: [32, 38]
  V-03: [44, 47, 50, 55, 58, 61, 64, 67]
  V-04: [73, 75]
  V-05: [7, 11, 24]
  V-06: [83, 89, 95, 101]
  V-07: [106, 107, 112, 113, 115]
  V-08: [8, 12]
  §[F-FACO-02] Edit Account#b2: [10, 11, 12, 18, 24, 32, 55, 73, 75, 83]
  EB-FRM-6@form-edit-account: [60, 61, 66, 67, 106, 112, 115, 118, 122, 123]
  EB-FRM-8@account-code: [10, 18, 30, 32, 44, 47, 50, 55, 61, 67, 73, 75]
  EB-FRM-8@account-name: [11, 24, 81, 83, 106, 112, 115]
  EB-FRM-8@account-function: 12
anchor: [5, 29, 37, 43, 46, 49, 57, 63, 72, 80, 88, 94, 100]
coverage:
  web: automated
---

# Form Edit Account: validasi per field simetris dengan Create

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Modal Edit Account.
- Data:
  - DU-111-1: akun dengan Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, Account Function `Depreciation Expense`, Used By `0`, Last Used in Journal `—`.
  - DU-111-2: akun lain dengan Account Code `5-6002`, Account Name `Depreciation Expense – Warehouse`, Account Function `Depreciation Expense`, Used By `0`, Last Used in Journal `—`.
  - DU-111-23: Account Name `Gudang Cabang🔥`, yaitu emoji yang lolos dari blok klien.
- Kondisi:
  - K1: form Edit Account dibuka untuk akun DU-111-1, yang tidak terkunci, dan pengecekan keunikan Account Code menyatakan kode yang diketik tersedia.
  - K2: seperti K1, dan pengecekan keunikan Account Code menyatakan kode `5-6002` sudah dipakai akun DU-111-2, sedangkan `5-6001` milik akun yang sedang diedit tetap tersedia.
  - K3: seperti K1, dan field Account Name berisi nilai DU-111-23.

## Test Steps

### Field kosong ditolak setelah Save sesudah Clear Field
1. Tampilkan Modal Edit Account dengan kondisi K1
2. Klik `⋯` pada baris akun `5-6001`
3. Klik `Edit`
4. Klik `[Clear Field]`
5. Verifikasi field `Account Function` menampilkan `Select account function` sesudah `[Clear Field]` pada form Edit
6. Verifikasi caption `Account code must not be empty` tidak tampil pada field `Account Code` pada form Edit sebelum `[Save]` diklik
7. Verifikasi caption `Account name must not be empty` tidak tampil pada field `Account Name` pada form Edit sebelum `[Save]` diklik
8. Verifikasi caption `Account function must not be empty` tidak tampil pada field `Account Function` pada form Edit sebelum `[Save]` diklik
9. Klik `[Save]`
10. Verifikasi caption `Account code must not be empty` tampil pada field `Account Code` pada form Edit
11. Verifikasi caption `Account name must not be empty` tampil pada field `Account Name` pada form Edit
12. Verifikasi caption `Account function must not be empty` tampil pada field `Account Function` pada form Edit

### Account Code berisi spasi saja diperlakukan kosong
13. Tampilkan Modal Edit Account dengan kondisi K1
14. Klik `⋯` pada baris akun `5-6001`
15. Klik `Edit`
16. Ganti isi field `Account Code` dengan `   ` (tiga spasi)
17. Klik `[Save]`
18. Verifikasi caption `Account code must not be empty` tampil pada field `Account Code` pada form Edit yang hanya berisi spasi

### Account Name berisi spasi saja diperlakukan kosong
19. Tampilkan Modal Edit Account dengan kondisi K1
20. Klik `⋯` pada baris akun `5-6001`
21. Klik `Edit`
22. Ganti isi field `Account Name` dengan `   ` (tiga spasi)
23. Klik `[Save]`
24. Verifikasi caption `Account name must not be empty` tampil pada field `Account Name` pada form Edit yang hanya berisi spasi

### Batas 15 karakter Account Code pada form Edit
25. Tampilkan Modal Edit Account dengan kondisi K1
26. Klik `⋯` pada baris akun `5-6001`
27. Klik `Edit`
28. Ganti isi field `Account Code` dengan `2-3001-REVAL-01` (15 karakter)
29. Verifikasi field `Account Code` berisi `2-3001-REVAL-01` pada form Edit
30. Verifikasi caption `Max. 15 characters` tidak tampil pada field `Account Code` pada form Edit
31. Ganti isi field `Account Code` dengan `2-3001-REVAL-016` (16 karakter)
32. Verifikasi caption `Max. 15 characters` tampil pada field `Account Code` pada form Edit tanpa `[Save]` diklik

### Spasi di tepi tidak dihitung pada Account Code form Edit
33. Tampilkan Modal Edit Account dengan kondisi K1
34. Klik `⋯` pada baris akun `5-6001`
35. Klik `Edit`
36. Ganti isi field `Account Code` dengan `  2-3002-REVAL-02  ` (dua spasi di awal dan dua spasi di akhir)
37. Verifikasi field `Account Code` berisi `2-3002-REVAL-02` (15 karakter) yang diapit spasi di awal dan di akhir pada form Edit
38. Verifikasi caption `Max. 15 characters` tidak tampil pada field `Account Code` pada form Edit

### Karakter yang diizinkan pada Account Code form Edit
39. Tampilkan Modal Edit Account dengan kondisi K1
40. Klik `⋯` pada baris akun `5-6001`
41. Klik `Edit`
42. Ganti isi field `Account Code` dengan `7-1001-B`
43. Verifikasi field `Account Code` berisi `7-1001-B` pada form Edit
44. Verifikasi caption `Account code contains invalid characters` tidak tampil pada field `Account Code` pada form Edit untuk nilai yang memuat tanda hubung
45. Ganti isi field `Account Code` dengan `ASET_BARU`
46. Verifikasi field `Account Code` berisi `ASET_BARU` pada form Edit
47. Verifikasi caption `Account code contains invalid characters` tidak tampil pada field `Account Code` pada form Edit untuk nilai yang memuat garis bawah
48. Ganti isi field `Account Code` dengan `2.3003.B`
49. Verifikasi field `Account Code` berisi `2.3003.B` pada form Edit
50. Verifikasi caption `Account code contains invalid characters` tidak tampil pada field `Account Code` pada form Edit untuk nilai yang memuat titik

### Karakter di luar whitelist pada Account Code form Edit
51. Tampilkan Modal Edit Account dengan kondisi K1
52. Klik `⋯` pada baris akun `5-6001`
53. Klik `Edit`
54. Ganti isi field `Account Code` dengan `2-3004 REVAL`
55. Verifikasi caption `Account code contains invalid characters` tampil pada field `Account Code` pada form Edit tanpa `[Save]` diklik
56. Ganti isi field `Account Code` dengan `7-1001-B`
57. Verifikasi field `Account Code` berisi `7-1001-B` sesudah diganti pada form Edit
58. Verifikasi caption `Account code contains invalid characters` tidak tampil pada field `Account Code` pada form Edit sesudah nilai diganti
59. Ganti isi field `Account Code` dengan `2-3004📈`
60. Verifikasi field `Account Code` berisi `2-3004📈` tanpa karakter yang diblok pada form Edit
61. Verifikasi caption `Account code contains invalid characters` tampil pada field `Account Code` pada form Edit
62. Ganti isi field `Account Code` dengan `7-1001-B`
63. Verifikasi field `Account Code` berisi `7-1001-B` sesudah emoji diganti pada form Edit
64. Verifikasi caption `Account code contains invalid characters` tidak tampil pada field `Account Code` pada form Edit sesudah emoji diganti
65. Tempel `ASET📌BARU` ke field `Account Code`
66. Verifikasi field `Account Code` berisi `ASET📌BARU` tanpa karakter yang diblok pada form Edit
67. Verifikasi caption `Account code contains invalid characters` tampil pada field `Account Code` pada form Edit untuk teks yang ditempel

### Account Code duplikat dan akun sendiri dikecualikan
68. Tampilkan Modal Edit Account dengan kondisi K2
69. Klik `⋯` pada baris akun `5-6001`
70. Klik `Edit`
71. Ganti isi field `Account Code` dengan `5-6001`
72. Verifikasi field `Account Code` berisi `5-6001` yang sama dengan nilai tersimpan akun yang sedang diedit
73. Verifikasi caption `Account code already exists` tidak tampil pada field `Account Code` pada form Edit karena akun yang sedang diedit dikecualikan
74. Ganti isi field `Account Code` dengan `5-6002`
75. Verifikasi caption `Account code already exists` tampil pada field `Account Code` pada form Edit tanpa field kehilangan fokus

### Batas 120 karakter Account Name pada form Edit
76. Tampilkan Modal Edit Account dengan kondisi K1
77. Klik `⋯` pada baris akun `5-6001`
78. Klik `Edit`
79. Ganti isi field `Account Name` dengan `Produksi Perusahaan untuk Kelompok Aset Tetap Berwujud Tahun Buku Berjalan Periode Gudang Alat Kendaraan Bangunan Cabang` (120 karakter)
80. Verifikasi field `Account Name` terisi sesuai ketikan pada form Edit
81. Verifikasi caption `Max. 120 characters` tidak tampil pada field `Account Name` pada form Edit
82. Ganti isi field `Account Name` dengan `Produksi Perusahaan untuk Kelompok Aset Tetap Berwujud Tahun Buku Berjalan Periode Gudang Alat Kendaraan Bangunan Cabangs` (121 karakter)
83. Verifikasi caption `Max. 120 characters` tampil pada field `Account Name` pada form Edit tanpa `[Save]` diklik

### Spasi di tepi tidak dihitung pada Account Name form Edit
84. Tampilkan Modal Edit Account dengan kondisi K1
85. Klik `⋯` pada baris akun `5-6001`
86. Klik `Edit`
87. Ganti isi field `Account Name` dengan `  Produksi Perusahaan untuk Kelompok Aset Tetap Berwujud Tahun Buku Berjalan Periode Gudang Alat Kendaraan Bangunan Cabang  ` (dua spasi di awal dan dua spasi di akhir)
88. Verifikasi field `Account Name` terisi sesuai ketikan dengan spasi di tepi pada form Edit
89. Verifikasi caption `Max. 120 characters` tidak tampil pada field `Account Name` pada form Edit

### Spasi di tengah dihitung penuh pada Account Name form Edit
90. Tampilkan Modal Edit Account dengan kondisi K1
91. Klik `⋯` pada baris akun `5-6001`
92. Klik `Edit`
93. Ganti isi field `Account Name` dengan `Perusahaan  untuk  Kelompok  Aset  Tetap  Berwujud  Tahun  Buku  Berjalan  Periode  Gudang  Alat  Kendaraan  Beban  Aset`
94. Verifikasi field `Account Name` terisi sesuai ketikan dengan spasi ganda di tengah tidak dibuang pada form Edit
95. Verifikasi caption `Max. 120 characters` tidak tampil pada field `Account Name` pada form Edit karena spasi di tengah dihitung penuh dan totalnya tetap 120 karakter

### Panjang Account Name dihitung per code point pada form Edit
96. Tampilkan Modal Edit Account dengan kondisi K1
97. Klik `⋯` pada baris akun `5-6001`
98. Klik `Edit`
99. Ganti isi field `Account Name` dengan `Éroduksi Perusahaan untuk Kelompok Aset Tetap Berwujud Tahun Buku Berjalan Periode Gudang Alat Kendaraan Bangunan Beban𝒜`
100. Verifikasi field `Account Name` terisi sesuai ketikan pada form Edit
101. Verifikasi caption `Max. 120 characters` tidak tampil pada field `Account Name` pada form Edit karena panjangnya dihitung per code point sebanyak 120

### Emoji yang diketik diblok pada Account Name form Edit
102. Tampilkan Modal Edit Account dengan kondisi K1
103. Klik `⋯` pada baris akun `5-6001`
104. Klik `Edit`
105. Ganti isi field `Account Name` dengan `Beban📈 Penyusutan`
106. Verifikasi field `Account Name` berisi `Beban Penyusutan`, dari `Beban📈 Penyusutan` tanpa emoji pada form Edit
107. Verifikasi caption `Account name contains invalid characters` tidak tampil pada field `Account Name` pada form Edit

### Emoji yang ditempel diblok pada Account Name form Edit
108. Tampilkan Modal Edit Account dengan kondisi K1
109. Klik `⋯` pada baris akun `5-6001`
110. Klik `Edit`
111. Tempel `Perawatan📌 Mesin` ke field `Account Name`
112. Verifikasi field `Account Name` berisi `Perawatan Mesin`, dari `Perawatan📌 Mesin` tanpa emoji pada form Edit
113. Verifikasi caption `Account name contains invalid characters` tidak tampil pada field `Account Name` pada form Edit untuk teks yang ditempel

### Emoji yang lolos ke Account Name form Edit ditolak dengan caption
114. Tampilkan Modal Edit Account dengan kondisi K3
115. Verifikasi caption `Account name contains invalid characters` tampil pada field `Account Name` pada form Edit tanpa `[Save]` diklik

### Baris baru yang ditempel tidak masuk ke Account Name form Edit
116. Tampilkan Modal Edit Account dengan kondisi K1
117. Tempel teks `Perawatan` dan `Mesin` yang dipisah baris baru ke field `Account Name`
118. Verifikasi field `Account Name` memuat `Perawatan` dan `Mesin` tanpa karakter baris baru pada form Edit

### Tab yang ditekan tidak masuk ke Account Name form Edit
119. Tampilkan Modal Edit Account dengan kondisi K1
120. Ganti isi field `Account Name` dengan `Mesin`
121. Tekan Tab
122. Verifikasi field `Account Name` berisi `Mesin` tanpa karakter tab pada form Edit
123. Verifikasi fokus berpindah dari field `Account Name` ke kontrol berikutnya pada form Edit

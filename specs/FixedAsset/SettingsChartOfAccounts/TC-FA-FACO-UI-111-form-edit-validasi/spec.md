---
id: TC-FA-FACO-UI-111-form-edit-validasi
title: "Form Edit Account: validasi per field simetris dengan Create"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [V-01, V-02, V-03, V-04, V-05, V-06, V-07, V-08, "§[F-FACO-02] Edit Account#b2", EB-FRM-6@form-edit-account, EB-FRM-8@account-code, EB-FRM-8@account-name, EB-FRM-8@account-function]
smoke: []
dependsOn: []
trace:
  V-01: [4, 8, 14]
  V-02: [24, 28]
  V-03: [32, 35, 38, 41, 44, 47, 50, 53]
  V-04: [57, 59]
  V-05: [5, 9, 18]
  V-06: [65, 69, 73, 77]
  V-07: [80, 81, 84, 85, 87]
  V-08: [6, 10]
  §[F-FACO-02] Edit Account#b2: [8, 9, 10, 14, 18, 24, 41, 57, 59, 65]
  EB-FRM-6@form-edit-account: [46, 47, 52, 53, 80, 84, 87, 90, 94, 95]
  EB-FRM-8@account-code: [8, 14, 22, 24, 32, 35, 38, 41, 47, 53, 57, 59, 98, 99, 101]
  EB-FRM-8@account-name: [9, 18, 63, 65, 80, 84, 87]
  EB-FRM-8@account-function: 10
anchor: [3, 21, 27, 31, 34, 37, 43, 49, 56, 62, 68, 72, 76]
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
2. Klik `[Clear Field]`
3. Verifikasi field `Account Function` menampilkan `Select account function` sesudah `[Clear Field]` pada form Edit
4. Verifikasi caption `Account code must not be empty` tidak tampil pada field `Account Code` pada form Edit sebelum `[Save]` diklik
5. Verifikasi caption `Account name must not be empty` tidak tampil pada field `Account Name` pada form Edit sebelum `[Save]` diklik
6. Verifikasi caption `Account function must not be empty` tidak tampil pada field `Account Function` pada form Edit sebelum `[Save]` diklik
7. Klik `[Save]`
8. Verifikasi caption `Account code must not be empty` tampil pada field `Account Code` pada form Edit
9. Verifikasi caption `Account name must not be empty` tampil pada field `Account Name` pada form Edit
10. Verifikasi caption `Account function must not be empty` tampil pada field `Account Function` pada form Edit

### Account Code berisi spasi saja diperlakukan kosong
11. Tampilkan Modal Edit Account dengan kondisi K1
12. Ganti isi field `Account Code` dengan `   ` (tiga spasi)
13. Klik `[Save]`
14. Verifikasi caption `Account code must not be empty` tampil pada field `Account Code` pada form Edit yang hanya berisi spasi

### Account Name berisi spasi saja diperlakukan kosong
15. Tampilkan Modal Edit Account dengan kondisi K1
16. Ganti isi field `Account Name` dengan `   ` (tiga spasi)
17. Klik `[Save]`
18. Verifikasi caption `Account name must not be empty` tampil pada field `Account Name` pada form Edit yang hanya berisi spasi

### Batas 15 karakter Account Code pada form Edit
19. Tampilkan Modal Edit Account dengan kondisi K1
20. Ganti isi field `Account Code` dengan `2-3001-REVAL-01` (15 karakter)
21. Verifikasi field `Account Code` berisi `2-3001-REVAL-01` pada form Edit
22. Verifikasi caption `Max. 15 characters` tidak tampil pada field `Account Code` pada form Edit
23. Ganti isi field `Account Code` dengan `2-3001-REVAL-016` (16 karakter)
24. Verifikasi caption `Max. 15 characters` tampil pada field `Account Code` pada form Edit tanpa `[Save]` diklik

### Spasi di tepi tidak dihitung pada Account Code form Edit
25. Tampilkan Modal Edit Account dengan kondisi K1
26. Ganti isi field `Account Code` dengan `  2-3002-REVAL-02  ` (dua spasi di awal dan dua spasi di akhir)
27. Verifikasi field `Account Code` berisi `2-3002-REVAL-02` (15 karakter) yang diapit spasi di awal dan di akhir pada form Edit
28. Verifikasi caption `Max. 15 characters` tidak tampil pada field `Account Code` pada form Edit

### Karakter yang diizinkan pada Account Code form Edit
29. Tampilkan Modal Edit Account dengan kondisi K1
30. Ganti isi field `Account Code` dengan `7-1001-B`
31. Verifikasi field `Account Code` berisi `7-1001-B` pada form Edit
32. Verifikasi caption `Account code contains invalid characters` tidak tampil pada field `Account Code` pada form Edit untuk nilai yang memuat tanda hubung
33. Ganti isi field `Account Code` dengan `ASET_BARU`
34. Verifikasi field `Account Code` berisi `ASET_BARU` pada form Edit
35. Verifikasi caption `Account code contains invalid characters` tidak tampil pada field `Account Code` pada form Edit untuk nilai yang memuat garis bawah
36. Ganti isi field `Account Code` dengan `2.3003.B`
37. Verifikasi field `Account Code` berisi `2.3003.B` pada form Edit
38. Verifikasi caption `Account code contains invalid characters` tidak tampil pada field `Account Code` pada form Edit untuk nilai yang memuat titik

### Karakter di luar whitelist pada Account Code form Edit
39. Tampilkan Modal Edit Account dengan kondisi K1
40. Ganti isi field `Account Code` dengan `2-3004 REVAL`
41. Verifikasi caption `Account code contains invalid characters` tampil pada field `Account Code` pada form Edit tanpa `[Save]` diklik
42. Ganti isi field `Account Code` dengan `7-1001-B`
43. Verifikasi field `Account Code` berisi `7-1001-B` sesudah diganti pada form Edit
44. Verifikasi caption `Account code contains invalid characters` tidak tampil pada field `Account Code` pada form Edit sesudah nilai diganti
45. Ganti isi field `Account Code` dengan `2-3004📈`
46. Verifikasi field `Account Code` berisi `2-3004📈` tanpa karakter yang diblok pada form Edit
47. Verifikasi caption `Account code contains invalid characters` tampil pada field `Account Code` pada form Edit
48. Ganti isi field `Account Code` dengan `7-1001-B`
49. Verifikasi field `Account Code` berisi `7-1001-B` sesudah emoji diganti pada form Edit
50. Verifikasi caption `Account code contains invalid characters` tidak tampil pada field `Account Code` pada form Edit sesudah emoji diganti
51. Tempel `ASET📌BARU` ke field `Account Code`
52. Verifikasi field `Account Code` berisi `ASET📌BARU` tanpa karakter yang diblok pada form Edit
53. Verifikasi caption `Account code contains invalid characters` tampil pada field `Account Code` pada form Edit untuk teks yang ditempel

### Account Code duplikat dan akun sendiri dikecualikan
54. Tampilkan Modal Edit Account dengan kondisi K2
55. Ganti isi field `Account Code` dengan `5-6001`
56. Verifikasi field `Account Code` berisi `5-6001` yang sama dengan nilai tersimpan akun yang sedang diedit
57. Verifikasi caption `Account code already exists` tidak tampil pada field `Account Code` pada form Edit karena akun yang sedang diedit dikecualikan
58. Ganti isi field `Account Code` dengan `5-6002`
59. Verifikasi caption `Account code already exists` tampil pada field `Account Code` pada form Edit tanpa field kehilangan fokus

### Batas 120 karakter Account Name pada form Edit
60. Tampilkan Modal Edit Account dengan kondisi K1
61. Ganti isi field `Account Name` dengan `Produksi Perusahaan untuk Kelompok Aset Tetap Berwujud Tahun Buku Berjalan Periode Gudang Alat Kendaraan Bangunan Cabang` (120 karakter)
62. Verifikasi field `Account Name` terisi sesuai ketikan pada form Edit
63. Verifikasi caption `Max. 120 characters` tidak tampil pada field `Account Name` pada form Edit
64. Ganti isi field `Account Name` dengan `Produksi Perusahaan untuk Kelompok Aset Tetap Berwujud Tahun Buku Berjalan Periode Gudang Alat Kendaraan Bangunan Cabangs` (121 karakter)
65. Verifikasi caption `Max. 120 characters` tampil pada field `Account Name` pada form Edit tanpa `[Save]` diklik

### Spasi di tepi tidak dihitung pada Account Name form Edit
66. Tampilkan Modal Edit Account dengan kondisi K1
67. Ganti isi field `Account Name` dengan `  Produksi Perusahaan untuk Kelompok Aset Tetap Berwujud Tahun Buku Berjalan Periode Gudang Alat Kendaraan Bangunan Cabang  ` (dua spasi di awal dan dua spasi di akhir)
68. Verifikasi field `Account Name` terisi sesuai ketikan dengan spasi di tepi pada form Edit
69. Verifikasi caption `Max. 120 characters` tidak tampil pada field `Account Name` pada form Edit

### Spasi di tengah dihitung penuh pada Account Name form Edit
70. Tampilkan Modal Edit Account dengan kondisi K1
71. Ganti isi field `Account Name` dengan `Perusahaan  untuk  Kelompok  Aset  Tetap  Berwujud  Tahun  Buku  Berjalan  Periode  Gudang  Alat  Kendaraan  Beban  Aset`
72. Verifikasi field `Account Name` terisi sesuai ketikan dengan spasi ganda di tengah tidak dibuang pada form Edit
73. Verifikasi caption `Max. 120 characters` tidak tampil pada field `Account Name` pada form Edit karena spasi di tengah dihitung penuh dan totalnya tetap 120 karakter

### Panjang Account Name dihitung per code point pada form Edit
74. Tampilkan Modal Edit Account dengan kondisi K1
75. Ganti isi field `Account Name` dengan `Éroduksi Perusahaan untuk Kelompok Aset Tetap Berwujud Tahun Buku Berjalan Periode Gudang Alat Kendaraan Bangunan Beban𝒜`
76. Verifikasi field `Account Name` terisi sesuai ketikan pada form Edit
77. Verifikasi caption `Max. 120 characters` tidak tampil pada field `Account Name` pada form Edit karena panjangnya dihitung per code point sebanyak 120

### Emoji yang diketik diblok pada Account Name form Edit
78. Tampilkan Modal Edit Account dengan kondisi K1
79. Ganti isi field `Account Name` dengan `Beban📈 Penyusutan`
80. Verifikasi field `Account Name` berisi `Beban Penyusutan`, dari `Beban📈 Penyusutan` tanpa emoji pada form Edit
81. Verifikasi caption `Account name contains invalid characters` tidak tampil pada field `Account Name` pada form Edit

### Emoji yang ditempel diblok pada Account Name form Edit
82. Tampilkan Modal Edit Account dengan kondisi K1
83. Tempel `Perawatan📌 Mesin` ke field `Account Name`
84. Verifikasi field `Account Name` berisi `Perawatan Mesin`, dari `Perawatan📌 Mesin` tanpa emoji pada form Edit
85. Verifikasi caption `Account name contains invalid characters` tidak tampil pada field `Account Name` pada form Edit untuk teks yang ditempel

### Emoji yang lolos ke Account Name form Edit ditolak dengan caption
86. Tampilkan Modal Edit Account dengan kondisi K3
87. Verifikasi caption `Account name contains invalid characters` tampil pada field `Account Name` pada form Edit tanpa `[Save]` diklik

### Baris baru yang ditempel tidak masuk ke Account Name form Edit
88. Tampilkan Modal Edit Account dengan kondisi K1
89. Tempel teks `Perawatan` dan `Mesin` yang dipisah baris baru ke field `Account Name`
90. Verifikasi field `Account Name` memuat `Perawatan` dan `Mesin` tanpa karakter baris baru pada form Edit

### Tab yang ditekan tidak masuk ke Account Name form Edit
91. Tampilkan Modal Edit Account dengan kondisi K1
92. Ganti isi field `Account Name` dengan `Mesin`
93. Tekan Tab
94. Verifikasi field `Account Name` berisi `Mesin` tanpa karakter tab pada form Edit
95. Verifikasi fokus berpindah dari field `Account Name` ke kontrol berikutnya pada form Edit

### Teks bantuan Account Code pada form Edit
96. Tampilkan Modal Edit Account dengan kondisi K1
97. Ganti isi field `Account Code` dengan `2-3001-REVAL-016` (16 karakter)
98. Verifikasi caption `Max. 15 characters` tampil pada field `Account Code` pada form Edit sebelum teks bantuan diperiksa
99. Verifikasi teks bantuan `Letters, numbers, hyphens, underscores, and dots only (e.g. 1-1001)` tidak tampil pada field `Account Code` pada form Edit selama caption error tampil
100. Ganti isi field `Account Code` dengan `2-3001-REVAL-01` (15 karakter)
101. Verifikasi teks bantuan `Letters, numbers, hyphens, underscores, and dots only (e.g. 1-1001)` tampil kembali pada field `Account Code` pada form Edit

---
id: TC-FA-FACO-UI-102-form-add-validasi-name-function
title: "Form Add Account: validasi Account Name dan Account Function"
layer: ui-client
priority: Medium
caseType: Negative
status: draft
sourceRules: [V-05, V-06, V-07, V-08, §4.1.2#r2, §4.1.2#r3, §[F-FACO-01] Create Account#r3, §[F-FACO-01] Create Account#r4, §9.4.2#r3, §9.4.2#r4, EB-FRM-4@account-name, EB-FRM-6@form-add-account]
smoke: []
dependsOn: []
trace:
  V-05: [4, 7]
  V-06: [22, 29, 34, 39]
  V-07: [43, 44, 48, 49, 53]
  V-08: [5, 8]
  §4.1.2#r2: [22, 57, 61]
  §4.1.2#r3: [8, 9]
  §[F-FACO-01] Create Account#r3: [22, 24]
  §[F-FACO-01] Create Account#r4: [7, 8, 10, 15]
  §9.4.2#r3: [22, 24]
  §9.4.2#r4: [7, 8, 10, 15]
  EB-FRM-4@account-name: [20, 22]
  EB-FRM-6@form-add-account: [43, 48, 53, 64, 68, 69]
anchor: [3, 19, 28, 33, 38, 56]
coverage:
  web: automated
---

# Form Add Account: validasi Account Name dan Account Function

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Modal Add Account.
- Data:
  - DU-102-1: akun yang sudah ada dengan Account Code `ASET-EQP-01`, Account Name `Peralatan Kantor Pusat`, Account Function `Asset Cost`.
- Kondisi:
  - K1: form Add Account baru dibuka dari toolbar dan belum ada isian.
  - K2: modal Add Account terbuka dan belum ada isian, akun DU-102-1 sudah ada, dan penyimpanan akun berhasil.
  - K3: modal Add Account terbuka dan belum ada isian.

## Test Steps

### Account Name dan Account Function kosong ditolak setelah Submit
1. Tampilkan Modal Add Account dengan kondisi K1
2. Klik `[+ Account]`
3. Verifikasi field `Account Name` tampil pada modal Add Account
4. Verifikasi caption `Account name must not be empty` tidak tampil sebelum `[Submit]` diklik
5. Verifikasi caption `Account function must not be empty` tidak tampil sebelum `[Submit]` diklik
6. Klik `[Submit]`
7. Verifikasi caption `Account name must not be empty` tampil pada field `Account Name`
8. Verifikasi caption `Account function must not be empty` tampil pada field `Account Function`
9. Verifikasi field `Account Function` masih menampilkan `Select account function` sebagai pilihan kosong
10. Verifikasi modal Add Account tetap terbuka sesudah Name dan Function kosong ditolak

### Account Name berisi spasi saja diperlakukan kosong
11. Tampilkan Modal Add Account dengan kondisi K1
12. Klik `[+ Account]`
13. Ketik Account Name `   ` (tiga spasi)
14. Klik `[Submit]`
15. Verifikasi caption `Account name must not be empty` tampil pada field `Account Name`

### Batas 120 karakter Account Name
16. Tampilkan Modal Add Account dengan kondisi K1
17. Klik `[+ Account]`
18. Ketik Account Name `Biaya Penyusutan Peralatan Kantor Pusat dan Cabang Seluruh Wilayah Operasional Perusahaan untuk Kelompok Aset Tetap Buku` (120 karakter)
19. Verifikasi field `Account Name` terisi sesuai ketikan
20. Verifikasi caption `Max. 120 characters` tidak tampil pada field `Account Name`
21. Ganti isi field `Account Name` dengan `Biaya Penyusutan Peralatan Kantor Pusat dan Cabang Seluruh Wilayah Operasional Perusahaan untuk Kelompok Aset Tetap Bukus` (121 karakter)
22. Verifikasi caption `Max. 120 characters` tampil pada field `Account Name` tanpa `[Submit]` diklik
23. Klik `[Submit]`
24. Verifikasi modal Add Account tetap terbuka sesudah Name lebih dari 120 karakter ditolak

### Spasi di tepi tidak dihitung pada Account Name
25. Tampilkan Modal Add Account dengan kondisi K1
26. Klik `[+ Account]`
27. Ketik Account Name `  Biaya Penyusutan Peralatan Kantor Pusat dan Cabang Seluruh Wilayah Operasional Perusahaan untuk Kelompok Aset Tetap Buku  ` (dua spasi di awal dan dua spasi di akhir)
28. Verifikasi field `Account Name` terisi sesuai ketikan
29. Verifikasi caption `Max. 120 characters` tidak tampil pada field `Account Name`

### Spasi di tengah dihitung penuh pada Account Name
30. Tampilkan Modal Add Account dengan kondisi K1
31. Klik `[+ Account]`
32. Ketik Account Name `Pusat  dan  Cabang  Seluruh  Wilayah  Operasional  Perusahaan  untuk  Kelompok  Aset  Tetap  Berwujud  Tahun  Buku  Aset`
33. Verifikasi field `Account Name` terisi sesuai ketikan dengan spasi ganda di tengah tidak dibuang
34. Verifikasi caption `Max. 120 characters` tidak tampil pada field `Account Name` karena spasi di tengah dihitung penuh dan totalnya tetap 120 karakter

### Panjang Account Name dihitung per code point
35. Tampilkan Modal Add Account dengan kondisi K1
36. Klik `[+ Account]`
37. Ketik Account Name `Éan Cabang Seluruh Wilayah Operasional Perusahaan untuk Kelompok Aset Tetap Berwujud Tahun Buku Berjalan Periode Gudang𝒜`
38. Verifikasi field `Account Name` terisi sesuai ketikan
39. Verifikasi caption `Max. 120 characters` tidak tampil pada field `Account Name` karena panjangnya dihitung per code point sebanyak 120

### Emoji yang diketik diblok pada Account Name
40. Tampilkan Modal Add Account dengan kondisi K1
41. Klik `[+ Account]`
42. Ketik Account Name `Biaya📊 Operasional`
43. Verifikasi field `Account Name` berisi `Biaya Operasional`, dari `Biaya📊 Operasional` tanpa emoji
44. Verifikasi caption `Account name contains invalid characters` tidak tampil pada field `Account Name`

### Emoji yang ditempel diblok pada Account Name
45. Tampilkan Modal Add Account dengan kondisi K1
46. Klik `[+ Account]`
47. Tempel `Peralatan📎 Gudang` ke field `Account Name`
48. Verifikasi field `Account Name` berisi `Peralatan Gudang`, dari `Peralatan📎 Gudang` tanpa emoji
49. Verifikasi caption `Account name contains invalid characters` tidak tampil pada field `Account Name`

### Emoji yang lolos lewat seret dan lepas ditolak dengan caption
50. Tampilkan Modal Add Account dengan kondisi K1
51. Klik `[+ Account]`
52. Seret dan lepas teks `Gudang Pusat🔥` ke field `Account Name`
53. Verifikasi caption `Account name contains invalid characters` tampil pada field `Account Name` tanpa `[Submit]` diklik

### Account Name boleh sama dengan akun lain
54. Tampilkan Modal Add Account dengan kondisi K2
55. Ketik Account Name `Peralatan Kantor Pusat`
56. Verifikasi field `Account Name` berisi `Peralatan Kantor Pusat`
57. Verifikasi tidak ada caption error yang tampil pada field `Account Name` sesudah nilai yang sama dengan DU-102-1 diketik
58. Ketik Account Code `ASET-EQP-02`
59. Pilih Account Function `Asset Cost`
60. Klik `[Submit]`
61. Verifikasi modal Add Account tertutup sesudah Submit diterima dengan Account Name yang sama dengan DU-102-1

### Baris baru yang ditempel tidak masuk ke Account Name
62. Tampilkan Modal Add Account dengan kondisi K3
63. Tempel teks `Peralatan` dan `Gudang` yang dipisah baris baru ke field `Account Name`
64. Verifikasi field `Account Name` memuat `Peralatan` dan `Gudang` tanpa karakter baris baru

### Tab yang ditekan tidak masuk ke Account Name
65. Tampilkan Modal Add Account dengan kondisi K3
66. Ketik Account Name `Gudang`
67. Tekan Tab
68. Verifikasi field `Account Name` berisi `Gudang` tanpa karakter tab
69. Verifikasi fokus berpindah dari field `Account Name` ke kontrol berikutnya

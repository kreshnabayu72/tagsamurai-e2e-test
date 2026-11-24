---
id: TC-FA-FACO-UI-102-form-add-validasi-name-function
title: "Form Add Account: validasi Account Name dan Account Function"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [V-05, V-06, V-07, V-08, §4.1.2#r2, §4.1.2#r3, "§[F-FACO-01] Create Account#r3", "§[F-FACO-01] Create Account#r4", §9.4.2#r3, §9.4.2#r4, §9.9#r2, EB-FRM-4@account-name, EB-FRM-6@form-add-account]
smoke: []
dependsOn: []
trace:
  V-05: [3, 6]
  V-06: [19, 25, 29, 33]
  V-07: [36, 37, 40, 41, 43]
  V-08: [4, 7]
  §4.1.2#r2: [19, 47, 51]
  §4.1.2#r3: [7, 8]
  §[F-FACO-01] Create Account#r3: [19, 21]
  §[F-FACO-01] Create Account#r4: [6, 7, 9, 13]
  §9.4.2#r3: [19, 21]
  §9.4.2#r4: [6, 7, 9, 13]
  §9.9#r2: [47]
  EB-FRM-4@account-name: [17, 19]
  EB-FRM-6@form-add-account: [36, 40, 43, 54, 58, 59]
anchor: [2, 16, 24, 28, 32, 46]
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
  - DU-102-11: Account Name `Gudang Pusat🔥`, yaitu emoji yang lolos dari blok klien.
- Kondisi:
  - K1: form Add Account baru dibuka dari toolbar dan belum ada isian.
  - K2: modal Add Account terbuka dan belum ada isian, akun DU-102-1 sudah ada, dan penyimpanan akun berhasil.
  - K3: modal Add Account terbuka dan belum ada isian.
  - K4: modal Add Account terbuka dan field Account Name berisi nilai DU-102-11.

## Test Steps

### Account Name dan Account Function kosong ditolak setelah Submit
1. Tampilkan Modal Add Account dengan kondisi K1
2. Verifikasi field `Account Name` tampil pada modal Add Account
3. Verifikasi caption `Account name must not be empty` tidak tampil sebelum `[Submit]` diklik
4. Verifikasi caption `Account function must not be empty` tidak tampil sebelum `[Submit]` diklik
5. Klik `[Submit]`
6. Verifikasi caption `Account name must not be empty` tampil pada field `Account Name`
7. Verifikasi caption `Account function must not be empty` tampil pada field `Account Function`
8. Verifikasi field `Account Function` masih menampilkan `Select account function` sebagai pilihan kosong
9. Verifikasi modal Add Account tetap terbuka sesudah Name dan Function kosong ditolak

### Account Name berisi spasi saja diperlakukan kosong
10. Tampilkan Modal Add Account dengan kondisi K1
11. Ketik Account Name `   ` (tiga spasi)
12. Klik `[Submit]`
13. Verifikasi caption `Account name must not be empty` tampil pada field `Account Name`

### Batas 120 karakter Account Name
14. Tampilkan Modal Add Account dengan kondisi K1
15. Ketik Account Name `Biaya Penyusutan Peralatan Kantor Pusat dan Cabang Seluruh Wilayah Operasional Perusahaan untuk Kelompok Aset Tetap Buku` (120 karakter)
16. Verifikasi field `Account Name` terisi sesuai ketikan
17. Verifikasi caption `Max. 120 characters` tidak tampil pada field `Account Name`
18. Ganti isi field `Account Name` dengan `Biaya Penyusutan Peralatan Kantor Pusat dan Cabang Seluruh Wilayah Operasional Perusahaan untuk Kelompok Aset Tetap Bukus` (121 karakter)
19. Verifikasi caption `Max. 120 characters` tampil pada field `Account Name` tanpa `[Submit]` diklik
20. Klik `[Submit]`
21. Verifikasi modal Add Account tetap terbuka sesudah Name lebih dari 120 karakter ditolak

### Spasi di tepi tidak dihitung pada Account Name
22. Tampilkan Modal Add Account dengan kondisi K1
23. Ketik Account Name `  Biaya Penyusutan Peralatan Kantor Pusat dan Cabang Seluruh Wilayah Operasional Perusahaan untuk Kelompok Aset Tetap Buku  ` (dua spasi di awal dan dua spasi di akhir)
24. Verifikasi field `Account Name` terisi sesuai ketikan
25. Verifikasi caption `Max. 120 characters` tidak tampil pada field `Account Name`

### Spasi di tengah dihitung penuh pada Account Name
26. Tampilkan Modal Add Account dengan kondisi K1
27. Ketik Account Name `Pusat  dan  Cabang  Seluruh  Wilayah  Operasional  Perusahaan  untuk  Kelompok  Aset  Tetap  Berwujud  Tahun  Buku  Aset`
28. Verifikasi field `Account Name` terisi sesuai ketikan dengan spasi ganda di tengah tidak dibuang
29. Verifikasi caption `Max. 120 characters` tidak tampil pada field `Account Name` karena spasi di tengah dihitung penuh dan totalnya tetap 120 karakter

### Panjang Account Name dihitung per code point
30. Tampilkan Modal Add Account dengan kondisi K1
31. Ketik Account Name `Éan Cabang Seluruh Wilayah Operasional Perusahaan untuk Kelompok Aset Tetap Berwujud Tahun Buku Berjalan Periode Gudang𝒜`
32. Verifikasi field `Account Name` terisi sesuai ketikan
33. Verifikasi caption `Max. 120 characters` tidak tampil pada field `Account Name` karena panjangnya dihitung per code point sebanyak 120

### Emoji yang diketik diblok pada Account Name
34. Tampilkan Modal Add Account dengan kondisi K1
35. Ketik Account Name `Biaya📊 Operasional`
36. Verifikasi field `Account Name` berisi `Biaya Operasional`, dari `Biaya📊 Operasional` tanpa emoji
37. Verifikasi caption `Account name contains invalid characters` tidak tampil pada field `Account Name`

### Emoji yang ditempel diblok pada Account Name
38. Tampilkan Modal Add Account dengan kondisi K1
39. Tempel `Peralatan📎 Gudang` ke field `Account Name`
40. Verifikasi field `Account Name` berisi `Peralatan Gudang`, dari `Peralatan📎 Gudang` tanpa emoji
41. Verifikasi caption `Account name contains invalid characters` tidak tampil pada field `Account Name`

### Emoji yang lolos ke Account Name ditolak dengan caption
42. Tampilkan Modal Add Account dengan kondisi K4
43. Verifikasi caption `Account name contains invalid characters` tampil pada field `Account Name` tanpa `[Submit]` diklik

### Account Name boleh sama dengan akun lain
44. Tampilkan Modal Add Account dengan kondisi K2
45. Ketik Account Name `Peralatan Kantor Pusat`
46. Verifikasi field `Account Name` berisi `Peralatan Kantor Pusat`
47. Verifikasi tidak ada caption error yang tampil pada field `Account Name` sesudah nilai yang sama dengan DU-102-1 diketik
48. Ketik Account Code `ASET-EQP-02`
49. Pilih Account Function `Asset Cost`
50. Klik `[Submit]`
51. Verifikasi modal Add Account tertutup sesudah Submit diterima dengan Account Name yang sama dengan DU-102-1

### Baris baru yang ditempel tidak masuk ke Account Name
52. Tampilkan Modal Add Account dengan kondisi K3
53. Tempel teks `Peralatan` dan `Gudang` yang dipisah baris baru ke field `Account Name`
54. Verifikasi field `Account Name` memuat `Peralatan` dan `Gudang` tanpa karakter baris baru

### Tab yang ditekan tidak masuk ke Account Name
55. Tampilkan Modal Add Account dengan kondisi K3
56. Ketik Account Name `Gudang`
57. Tekan Tab
58. Verifikasi field `Account Name` berisi `Gudang` tanpa karakter tab
59. Verifikasi fokus berpindah dari field `Account Name` ke kontrol berikutnya

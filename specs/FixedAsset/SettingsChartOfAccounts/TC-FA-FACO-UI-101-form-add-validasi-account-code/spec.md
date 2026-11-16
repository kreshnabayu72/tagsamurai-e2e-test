---
id: TC-FA-FACO-UI-101-form-add-validasi-account-code
title: "Form Add Account: validasi Account Code"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [V-01, V-02, V-03, V-04, §4.1.2#r1, §4.5#b4, §6#p1, "§[F-FACO-01] Create Account#r1", "§[F-FACO-01] Create Account#r2", "§[F-FACO-01] Create Account#r4", §9.4.2#r1, §9.4.2#r2, §9.4.2#r4, EB-FRM-4@account-code, EB-FRM-6@form-add-account]
smoke: []
dependsOn: []
trace:
  V-01: [3, 5]
  V-02: [21, 30]
  V-03: [35, 38, 41, 44, 47, 50, 53, 56]
  V-04: 13
  §4.1.2#r1: [13, 21, 44]
  §4.5#b4: 6
  §6#p1: [3, 21, 22, 26, 34]
  §[F-FACO-01] Create Account#r1: [13, 15]
  §[F-FACO-01] Create Account#r2: [21, 24, 44]
  §[F-FACO-01] Create Account#r4: [5, 10]
  §9.4.2#r1: [13, 15]
  §9.4.2#r2: [21, 24, 44]
  §9.4.2#r4: [5, 10]
  EB-FRM-4@account-code: [19, 21]
  EB-FRM-6@form-add-account: [49, 50, 55, 56]
anchor: [2, 18, 29, 33, 37, 40, 46, 52]
coverage:
  web: automated
---

# Form Add Account: validasi Account Code

## Prerequisites
- Aktor: Total Control.
- Layar awal: Modal Add Account pada Settings > Accounting > Chart of Accounts.
- Komponen: Modal Add Account.
- Data:
  - DU-101-1: akun yang sudah ada dengan Account Code `FIN-OPS-01`, Account Name `Biaya Operasional Keuangan`, Account Function `Depreciation Expense`.
- Kondisi:
  - K1: modal Add Account terbuka dan belum ada isian.
  - K2: seperti K1, dan pengecekan keunikan Account Code menyatakan kode record DU-101-1 sudah dipakai.

## Test Steps

### Account Code kosong ditolak setelah Submit
1. Tampilkan Modal Add Account dengan kondisi K1
2. Verifikasi field `Account Code` tampil pada modal Add Account
3. Verifikasi caption `Account code must not be empty` tidak tampil sebelum `[Submit]` diklik
4. Klik `[Submit]`
5. Verifikasi caption `Account code must not be empty` tampil pada field `Account Code`
6. Verifikasi field `Account Code` memiliki `aria-describedby` yang menunjuk caption `Account code must not be empty`

### Account Code berisi spasi saja diperlakukan kosong
7. Tampilkan Modal Add Account dengan kondisi K1
8. Ketik Account Code `   ` (tiga spasi)
9. Klik `[Submit]`
10. Verifikasi caption `Account code must not be empty` tampil pada field `Account Code`

### Account Code duplikat ditolak
11. Tampilkan Modal Add Account dengan kondisi K2
12. Ketik Account Code `FIN-OPS-01`
13. Verifikasi caption `Account code already exists` tampil pada field `Account Code` tanpa field kehilangan fokus
14. Klik `[Submit]`
15. Verifikasi modal Add Account tetap terbuka sesudah kode duplikat ditolak

### Batas 15 karakter Account Code
16. Tampilkan Modal Add Account dengan kondisi K1
17. Ketik Account Code `1-1001-EQUIP-01` (15 karakter)
18. Verifikasi field `Account Code` berisi `1-1001-EQUIP-01`
19. Verifikasi caption `Max. 15 characters` tidak tampil pada field `Account Code`
20. Ganti isi field `Account Code` dengan `1-1001-EQUIP-016` (16 karakter)
21. Verifikasi caption `Max. 15 characters` tampil pada field `Account Code` tanpa `[Submit]` diklik
22. Verifikasi teks bantuan `Letters, numbers, hyphens, underscores, and dots only (e.g. 1-1001)` tidak tampil selama caption error tampil
23. Klik `[Submit]`
24. Verifikasi modal Add Account tetap terbuka sesudah kode lebih dari 15 karakter ditolak
25. Ganti isi field `Account Code` dengan `1-1001-EQUIP-01` (15 karakter)
26. Verifikasi teks bantuan `Letters, numbers, hyphens, underscores, and dots only (e.g. 1-1001)` tampil kembali pada field `Account Code`

### Spasi di tepi tidak dihitung
27. Tampilkan Modal Add Account dengan kondisi K1
28. Ketik Account Code `  1-2001-DEPRC-01  ` (dua spasi di awal dan dua spasi di akhir)
29. Verifikasi field `Account Code` berisi `1-2001-DEPRC-01` (15 karakter) yang diapit spasi di awal dan di akhir
30. Verifikasi caption `Max. 15 characters` tidak tampil pada field `Account Code`

### Karakter yang diizinkan pada Account Code
31. Tampilkan Modal Add Account dengan kondisi K1
32. Ketik Account Code `5-6001-A`
33. Verifikasi field `Account Code` berisi `5-6001-A`
34. Verifikasi teks bantuan `Letters, numbers, hyphens, underscores, and dots only (e.g. 1-1001)` tampil pada field `Account Code`
35. Verifikasi caption `Account code contains invalid characters` tidak tampil untuk nilai `5-6001-A` yang memuat tanda hubung
36. Ganti isi field `Account Code` dengan `FIN_OPS`
37. Verifikasi field `Account Code` berisi `FIN_OPS`
38. Verifikasi caption `Account code contains invalid characters` tidak tampil untuk nilai `FIN_OPS` yang memuat garis bawah
39. Ganti isi field `Account Code` dengan `1.1001.A`
40. Verifikasi field `Account Code` berisi `1.1001.A`
41. Verifikasi caption `Account code contains invalid characters` tidak tampil untuk nilai `1.1001.A` yang memuat titik

### Karakter di luar whitelist ditolak
42. Tampilkan Modal Add Account dengan kondisi K1
43. Ketik Account Code `1-1001 EQUIP`
44. Verifikasi caption `Account code contains invalid characters` tampil pada field `Account Code` tanpa `[Submit]` diklik
45. Ganti isi field `Account Code` dengan `5-6001-A`
46. Verifikasi field `Account Code` berisi `5-6001-A`
47. Verifikasi caption `Account code contains invalid characters` tidak tampil lagi pada field `Account Code`
48. Ganti isi field `Account Code` dengan `1-1001📊`
49. Verifikasi field `Account Code` berisi `1-1001📊` tanpa karakter yang diblok
50. Verifikasi caption `Account code contains invalid characters` tampil pada field `Account Code`
51. Ganti isi field `Account Code` dengan `5-6001-A`
52. Verifikasi field `Account Code` berisi `5-6001-A`
53. Verifikasi caption `Account code contains invalid characters` tidak tampil lagi pada field `Account Code`
54. Tempel `FIN📎OPS` ke field `Account Code`
55. Verifikasi field `Account Code` berisi `FIN📎OPS` tanpa karakter yang diblok
56. Verifikasi caption `Account code contains invalid characters` tampil pada field `Account Code`

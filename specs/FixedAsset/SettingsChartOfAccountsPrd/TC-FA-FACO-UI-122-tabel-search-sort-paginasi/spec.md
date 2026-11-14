---
id: TC-FA-FACO-UI-122-tabel-search-sort-paginasi
title: "Tab Chart of Accounts: siklus Search, indikator sort, dan paginasi"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.4#r6", "§5#b2", "§5#b5", "§9.5#r4", "EB-TBL-7@tabel-account-list", "EB-SRC-4@tabel-account-list", "EB-SRT-3@tabel-account-list"]
smoke: []
dependsOn: []
trace:
  "§4.4#r6": [46, 53, 54]
  "§5#b2": [5, 7]
  "§5#b5": [21, 25, 36, 38, 39, 41, 43, 74, 76, 78, 81, 85]
  "§9.5#r4": [21, 25, 28, 31, 34]
  "EB-TBL-7@tabel-account-list": [23, 27, 58, 60, 64, 66, 69, 71]
  "EB-SRC-4@tabel-account-list": [3, 5, 7, 8, 10, 11, 12, 14, 16, 18, 19]
  "EB-SRT-3@tabel-account-list": [46, 48, 50, 53, 54, 55]
anchor: []
coverage:
  web: automated
---

# Tab Chart of Accounts: siklus Search, indikator sort, dan paginasi

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Tab Chart of Accounts
- Data:
  - DU-122-1: 101 akun, Account Code `7-{n}`, Name `Akun Uji {n}`, Function `Asset Cost`, status Active, Used By `0`.
  - DU-122-2: 10 akun, Account Code `8-{n}`, Name `Akun Pas {n}`, Function `Asset Cost`, status Active, Used By `0`.
  - DU-122-3: 11 akun, Account Code `9-{n}`, Name `Akun Sisa {n}`, Function `Asset Cost`, status Active, Used By `0`.
  - DU-122-4: 30 akun, Account Code `5-{n}`, Name `Kas Cabang {n}`, Function `Asset Cost`, status Active, Used By `0`.
  - DU-122-5: 20 akun, Account Code `1-{n}`, Name `Bank Cabang {n}`, Function `Asset Cost`, status Active, Used By `0`.
  - DU-122-6: nomor halaman yang diketik pada input Jump to page: `abc`, `0`, `-1`, dan `12`.
  - DU-122-7: kata kunci Search `Kas Cabang`.
- Kondisi:
  - K1: tabel berisi DU-122-1, dengan ukuran halaman bawaan; tabel terdiri atas 11 halaman pada ukuran halaman 10.
  - K2: tabel berisi DU-122-2.
  - K3: tabel berisi DU-122-3.
  - K4: tabel berisi DU-122-4 dan DU-122-5; kata kunci Search `Kas Cabang` hanya menghasilkan akun DU-122-4, dan kotak Search kosong menghasilkan seluruh akun.
  - K5: seperti K1; Filter Function `Asset Cost` menghasilkan seluruh akun DU-122-1.

## Test Steps

### Siklus kotak Search
1. Tampilkan Tab Chart of Accounts dengan kondisi K4
2. Klik ikon Search
3. Verifikasi kotak Search terbuka dan fokus berada di input
4. Ketik `Kas Cabang` pada kotak Search tanpa menekan Enter
5. Verifikasi baris `Bank Cabang 1` tetap tampil dalam 2 detik sesudah mengetik
6. Tekan Enter pada kotak Search
7. Verifikasi baris `Kas Cabang 1` tampil
8. Verifikasi baris `Bank Cabang 1` tidak tampil
9. Klik `✕` pada kotak Search
10. Verifikasi isi kotak Search kosong
11. Verifikasi baris `Kas Cabang 1` masih tampil
12. Verifikasi baris `Bank Cabang 1` masih tidak tampil
13. Tekan Enter pada kotak Search yang kosong
14. Verifikasi baris `Bank Cabang 1` tampil kembali
15. Ketik Search `Kas Cabang`, tekan Enter
16. Verifikasi baris `Kas Cabang 1` tampil
17. Klik `(←)` pada kotak Search
18. Verifikasi kotak Search tertutup
19. Verifikasi baris `Bank Cabang 1` tampil kembali

### Ukuran halaman dan kembali ke halaman 1
20. Tampilkan Tab Chart of Accounts dengan kondisi K1
21. Verifikasi ukuran halaman terpilih `10` dan halaman 1 menampilkan 10 baris
22. Klik halaman `2`
23. Verifikasi halaman aktif adalah `2`
24. Klik dropdown Rows per page
25. Verifikasi pilihan `10`, `25`, `50`, dan `100` tersedia
26. Pilih `25`
27. Verifikasi halaman aktif adalah `1`
28. Verifikasi halaman 1 menampilkan 25 baris
29. Klik dropdown Rows per page
30. Pilih `50`
31. Verifikasi halaman 1 menampilkan 50 baris
32. Klik dropdown Rows per page
33. Pilih `100`
34. Verifikasi halaman 1 menampilkan 100 baris
35. Klik halaman `2`
36. Verifikasi halaman 2 menampilkan 1 baris

### Satu halaman penuh dan satu baris di halaman terakhir
37. Tampilkan Tab Chart of Accounts dengan kondisi K2
38. Verifikasi halaman 1 menampilkan 10 baris
39. Verifikasi tidak ada halaman `2`
40. Tampilkan Tab Chart of Accounts dengan kondisi K3
41. Verifikasi halaman 1 menampilkan 10 baris
42. Klik halaman `2`
43. Verifikasi halaman 2 menampilkan 1 baris

### Indikator sort
44. Tampilkan Tab Chart of Accounts dengan kondisi K1
45. Klik header kolom `Account Name`
46. Verifikasi indikator sort naik `↑` aktif pada header kolom `Account Name`
47. Klik header kolom `Account Name`
48. Verifikasi indikator sort turun `↓` aktif pada header kolom `Account Name`
49. Klik header kolom `Account Name`
50. Verifikasi indikator sort pada header kolom `Account Name` hilang
51. Klik header kolom `Account Name`
52. Klik header kolom `Function`
53. Verifikasi indikator sort aktif pada header kolom `Function`
54. Verifikasi indikator sort pada header kolom `Account Name` tidak aktif
55. Verifikasi header kolom Actions `⋯` tidak memiliki ikon sort

### Ganti sort tetap di halaman sekarang
56. Tampilkan Tab Chart of Accounts dengan kondisi K1
57. Klik halaman `2`
58. Verifikasi halaman aktif adalah `2`
59. Klik header kolom `Account Name`
60. Verifikasi halaman aktif tetap `2`

### Nomor halaman tidak valid
61. Tampilkan Tab Chart of Accounts dengan kondisi K1
62. Klik halaman `2`
63. Ketik `abc` pada input Jump to page, tekan Enter
64. Verifikasi halaman aktif tetap `2`
65. Ketik `0` pada input Jump to page, tekan Enter
66. Verifikasi halaman aktif adalah `1`[^drift-1]
67. Klik halaman `2`
68. Ketik `-1` pada input Jump to page, tekan Enter
69. Verifikasi halaman aktif adalah `1`[^drift-1]
70. Ketik `12` pada input Jump to page, tekan Enter
71. Verifikasi halaman aktif adalah halaman terakhir `11`[^drift-1]

### Search dan Filter Panel mengembalikan ke halaman 1
72. Tampilkan Tab Chart of Accounts dengan kondisi K4
73. Klik halaman `2`
74. Verifikasi halaman aktif adalah `2`
75. Ketik Search `Kas Cabang`, tekan Enter
76. Verifikasi halaman aktif adalah `1`
77. Klik halaman `2`
78. Verifikasi halaman aktif adalah `2`
79. Tampilkan Tab Chart of Accounts dengan kondisi K5
80. Klik halaman `2`
81. Verifikasi halaman aktif adalah `2`
82. Klik ikon Filter
83. Pilih `Asset Cost` pada filter Function
84. Klik `[Apply]`
85. Verifikasi halaman aktif adalah `1`

[^drift-1]: Drift foundation vs kontrak komponen. foundation `prd-conventions.md` §9.18: «Nomor halaman tidak valid (0, negatif, melebihi halaman terakhir, bukan angka) pada input nomor halaman: input diabaikan dan tabel tetap di halaman sekarang.» Kontrak `Paginator#9`: «a page past the last goes to the last page, a page below 1 goes to page 1». Diasersi: kontrak, karena input nomor halaman adalah mekanik komponen Paginator (SB-7); PRD §5#b5 hanya merujuk §9.18.

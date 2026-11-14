---
id: TC-FA-FACO-UI-125-tabel-bulk-seleksi
title: "Tab Chart of Accounts: seleksi baris, Bulk Action Bar, dan Selection Limit"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1.1#p4", "§3.8#r5", "§3.8#r6", "§4.8#b3", "§5#b6", "§9.4.2#r35", "§9.5#r3", "EB-BLK-1@tabel-account-list", "EB-BLK-4", "EB-BLK-6"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#p4": [9, 10, 18, 19, 26, 28]
  "§3.8#r5": [10, 18, 26]
  "§3.8#r6": [9, 19, 26, 104]
  "§4.8#b3": [9, 10, 18, 19, 26]
  "§5#b6": [7, 13, 30, 56, 57, 65, 73, 106]
  "§9.4.2#r35": [77, 82, 87, 88, 97, 98]
  "§9.5#r3": [2, 3, 4]
  "EB-BLK-1@tabel-account-list": [7, 13, 24, 30, 33, 36, 38, 42, 43, 46, 48, 49, 56, 57]
  "EB-BLK-4": [64, 65, 72, 73]
  "EB-BLK-6": [77, 78, 82, 83, 87, 88, 91, 92, 97, 98]
anchor: []
coverage:
  web: automated
---

# Tab Chart of Accounts: seleksi baris, Bulk Action Bar, dan Selection Limit

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Tab Chart of Accounts
- Data:
  - DU-125-1: 12 akun Active, Account Code `A-{n}`, Name `Akun Aktif {n}`, Function `Asset Cost`.
  - DU-125-2: 3 akun Inactive, Account Code `I-{n}`, Name `Akun Nonaktif {n}`, Function `Asset Cost`.
  - DU-125-3: 999 akun Active, Account Code `L-{n}`, Name `Akun Batas {n}`, Function `Asset Cost`.
  - DU-125-4: 1.000 akun Active, Account Code `M-{n}`, Name `Akun Pas Batas {n}`, Function `Asset Cost`.
  - DU-125-5: 1.001 akun Active, Account Code `N-{n}`, Name `Akun Lebih Batas {n}`, Function `Asset Cost`.
  - DU-125-6: 1.200 akun Active, Account Code `P-{n}`, Name `Cabang Besar {n}`, Function `Asset Cost`.
  - DU-125-7: 300 akun Active, Account Code `Q-{n}`, Name `Cabang Kecil {n}`, Function `Asset Cost`.
  - DU-125-8: kata kunci Search `Nonaktif` dan `Cabang Besar`.
  - DU-125-9: 2 akun Active yang dipakai Asset Class, Account Code `U-{n}`, Name `Akun Terpakai {n}`, Function `Asset Cost`, Used By `2`.
- Kondisi:
  - K1: tabel berisi DU-125-1 dan DU-125-2 dengan ukuran halaman bawaan; kata kunci Search `Nonaktif` hanya menghasilkan DU-125-2.
  - K2: seperti K1; konfirmasi Activate berhasil.
  - K3: seperti K1; konfirmasi Activate gagal karena error server.
  - K4: seperti K1; konfirmasi Activate tidak dijawab sampai batas waktu.
  - K5: Selection Limit bernilai `1000`; tabel berisi DU-125-3.
  - K6: Selection Limit bernilai `1000`; tabel berisi DU-125-4.
  - K7: Selection Limit bernilai `1000`; tabel berisi DU-125-5.
  - K8: Selection Limit bernilai `1000`; tabel berisi DU-125-6 dan DU-125-7; kata kunci Search `Cabang Besar` hanya menghasilkan DU-125-6.
  - K9: seperti K1, tetapi tabel berisi DU-125-9.

## Test Steps

### Default tanpa seleksi
1. Tampilkan Tab Chart of Accounts dengan kondisi K1
2. Verifikasi baris `A-1` tampil
3. Verifikasi tidak ada baris yang terpilih
4. Verifikasi Bulk Action Bar tidak tampil

### Seleksi homogen Active
5. Tampilkan Tab Chart of Accounts dengan kondisi K1
6. Centang baris `A-1`
7. Verifikasi counter `1 Account selected` tampil
8. Klik `Bulk Action`
9. Verifikasi item `Deactivate` dan `Delete` tampil
10. Verifikasi item `Activate` tidak tampil
11. Tekan `Esc`
12. Centang baris `A-2`
13. Verifikasi counter `2 Accounts selected` tampil

### Seleksi homogen Inactive
14. Tampilkan Tab Chart of Accounts dengan kondisi K1
15. Ketik Search `Nonaktif`, tekan Enter
16. Centang baris `I-1`
17. Klik `Bulk Action`
18. Verifikasi item `Activate` dan `Delete` tampil
19. Verifikasi item `Deactivate` tidak tampil

### Seleksi campuran lintas halaman
20. Tampilkan Tab Chart of Accounts dengan kondisi K1
21. Centang baris `A-1`
22. Klik halaman `2`
23. Centang baris `I-1`
24. Verifikasi counter `2 Accounts selected` tampil
25. Klik `Bulk Action`
26. Verifikasi item `Activate`, `Deactivate`, dan `Delete` tampil
27. Klik `Activate`
28. Verifikasi judul dialog `Activate Account` tampil
29. Klik `[Cancel]`
30. Verifikasi counter `2 Accounts selected` tampil

### Checkbox header dan indeterminate
31. Tampilkan Tab Chart of Accounts dengan kondisi K1
32. Centang checkbox header
33. Verifikasi counter `10 Accounts selected` tampil
34. Klik halaman `2`
35. Centang baris `A-8`
36. Verifikasi checkbox header berstatus indeterminate
37. Klik halaman `1`
38. Verifikasi counter `11 Accounts selected` tampil

### Seleksi bertahan saat Search mengubah daftar
39. Tampilkan Tab Chart of Accounts dengan kondisi K1
40. Centang baris `A-1`
41. Ketik Search `Nonaktif`, tekan Enter
42. Verifikasi baris `I-1` tampil
43. Verifikasi counter `1 Account selected` tampil

### Clear selection
44. Tampilkan Tab Chart of Accounts dengan kondisi K1
45. Centang baris `A-1`
46. Verifikasi counter `1 Account selected` tampil
47. Klik `✕` pada Bulk Action Bar
48. Verifikasi Bulk Action Bar tidak tampil
49. Verifikasi baris `A-1` tidak terpilih

### Seleksi bersih sesudah aksi selesai
50. Tampilkan Tab Chart of Accounts dengan kondisi K2
51. Ketik Search `Nonaktif`, tekan Enter
52. Centang baris `I-1`
53. Klik `Bulk Action`
54. Klik `Activate`
55. Klik `[Activate]` pada dialog `Activate Account`
56. Verifikasi Bulk Action Bar tidak tampil
57. Verifikasi baris `I-1` tidak terpilih

### Bulk gagal karena error server
58. Tampilkan Tab Chart of Accounts dengan kondisi K3
59. Ketik Search `Nonaktif`, tekan Enter
60. Centang baris `I-1`
61. Klik `Bulk Action`
62. Klik `Activate`
63. Klik `[Activate]` pada dialog `Activate Account`
64. Verifikasi toast `Error, failed to activate account.` tampil
65. Verifikasi counter `1 Account selected` tampil

### Bulk gagal karena timeout
66. Tampilkan Tab Chart of Accounts dengan kondisi K4
67. Ketik Search `Nonaktif`, tekan Enter
68. Centang baris `I-1`
69. Klik `Bulk Action`
70. Klik `Activate`
71. Klik `[Activate]` pada dialog `Activate Account`
72. Verifikasi toast `Connection problem. Please try again.` tampil
73. Verifikasi counter `1 Account selected` tampil

### Select All di bawah Selection Limit
74. Tampilkan Tab Chart of Accounts dengan kondisi K5
75. Centang baris `L-1`
76. Klik `Select All (999 records)`
77. Verifikasi counter `999 Accounts selected` tampil
78. Verifikasi tombol berubah menjadi `Unselect All`

### Select All tepat di Selection Limit
79. Tampilkan Tab Chart of Accounts dengan kondisi K6
80. Centang baris `M-1`
81. Klik `Select All (1000 records)`
82. Verifikasi counter `1000 Accounts selected` tampil
83. Verifikasi tombol berubah menjadi `Unselect All`

### Select All melebihi Selection Limit
84. Tampilkan Tab Chart of Accounts dengan kondisi K7
85. Centang baris `N-1`
86. Klik `Select All (1001 records)`
87. Verifikasi counter `1000 Accounts selected` tampil
88. Verifikasi toast `Error, only the first 1000 of 1001 rows were selected. Narrow your filter to include the rest.` tampil
89. Ketik `101` pada input Jump to page, tekan Enter
90. Arahkan kursor ke checkbox baris yang tampil di halaman `101`
91. Verifikasi checkbox baris di halaman `101` disabled
92. Verifikasi `You've reached the maximum selection of 1000 rows.` tersampaikan pada checkbox baris di halaman `101`

### Select All atas hasil Search yang melebihi Selection Limit
93. Tampilkan Tab Chart of Accounts dengan kondisi K8
94. Ketik Search `Cabang Besar`, tekan Enter
95. Centang baris `P-1`
96. Klik `Select All (1200 records)`
97. Verifikasi counter `1000 Accounts selected` tampil
98. Verifikasi toast `Error, only the first 1000 of 1200 rows were selected. Narrow your filter to include the rest.` tampil

### Dialog Blok bulk mempertahankan seleksi
99. Tampilkan Tab Chart of Accounts dengan kondisi K9
100. Centang baris `U-1`
101. Centang baris `U-2`
102. Klik `Bulk Action`
103. Klik `Deactivate`
104. Verifikasi judul dialog `Cannot Deactivate Accounts` tampil
105. Klik `[OK]`
106. Verifikasi counter `2 Accounts selected` tampil

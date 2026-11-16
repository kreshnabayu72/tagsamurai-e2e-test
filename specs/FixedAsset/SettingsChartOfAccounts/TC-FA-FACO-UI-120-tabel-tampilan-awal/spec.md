---
id: TC-FA-FACO-UI-120-tabel-tampilan-awal
title: "Tab Chart of Accounts: toolbar, kolom, dan format sel"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ST-05, "§4.1.1#r1", "§4.1.1#r2", "§4.1.1#r3", "§4.1.1#r4", "§4.1.1#r5", "§4.1.1#r6", "§4.1.1#r7", "§4.1.1#r8", "§4.2a#p1", "§5#b2", "§5#b11", "§4.2b#p3", "§9.5#r5", "§9.5#r12", "EB-TBL-2@kolom-last-used-in-journal", "EB-TBL-4@kolom-modified-by", "EB-TBL-8@tabel-account-list", EB-TBL-11, EB-XM-1]
smoke: []
dependsOn: []
trace:
  ST-05: [50, 51]
  "§4.1.1#r1": [26, 41, 42]
  "§4.1.1#r2": [27, 39]
  "§4.1.1#r3": [28, 40, 82]
  "§4.1.1#r4": [29, 43, 44, 45, 46, 47, 48, 49]
  "§4.1.1#r5": [30, 50, 51]
  "§4.1.1#r6": [31, 52, 53, 54, 55, 57]
  "§4.1.1#r7": [36, 59, 62, 65, 68, 71, 74, 77]
  "§4.1.1#r8": [37, 78, 79, 80, 85]
  "§4.2a#p1": [2, 5, 7, 10, 12, 14, 16, 19, 21, 24]
  "§5#b2": [8, 18]
  "§5#b11": [26, 27, 28, 29, 30, 31, 32]
  "§4.2b#p3": [89]
  "§9.5#r5": [26, 27, 28, 29, 30, 31, 32]
  "§9.5#r12": [53, 54, 55]
  "EB-TBL-2@kolom-last-used-in-journal": [53, 54, 55]
  "EB-TBL-4@kolom-modified-by": [59, 61, 62, 64, 65, 67, 68, 70, 71, 73, 74, 76]
  "EB-TBL-8@tabel-account-list": 83
  EB-TBL-11: [3, 4]
  EB-XM-1: [78, 79, 80]
anchor: [87]
coverage:
  web: automated
---

# Tab Chart of Accounts: toolbar, kolom, dan format sel

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Tab Chart of Accounts
- Data:
  - DU-120-1: Account `1-1001`, Name `Fixed Assets – Equipment`, Function `Asset Cost`, status Active, Used By `3`, Last Used in Journal `Oct 2026`, Modified By `Rina Pratiwi`, Last Updated `2026-03-25T09:15:00Z`. Modified By tampil `Rina P`, dari `Rina Pratiwi`. Last Updated tampil `25/03/26, 09:15`, dari `2026-03-25T09:15:00Z`.
  - DU-120-2: Account `1-2001`, Name `Accumulated Depreciation – Equipment`, Function `Accumulated Depreciation`, status Active, Used By `2`, Last Used in Journal `Sep 2026`, Modified By `Budi`, Last Updated `2026-03-24T23:30:00Z`. Modified By tampil `Budi`, dari `Budi`. Last Updated tampil `24/03/26, 23:30`, dari `2026-03-24T23:30:00Z`.
  - DU-120-3: Account `5-6001`, Name `Depreciation Expense – Admin`, Function `Depreciation Expense`, status Active, Used By `0`, Last Used in Journal kosong (belum pernah diisi), Modified By `Alexander Graham Bell`, Last Updated `2026-03-10T08:05:00Z`. Modified By tampil `Alexander G`, dari `Alexander Graham Bell`.
  - DU-120-4: Account `4-7001`, Name `Gain on Disposal`, Function `Gain on Disposal`, status Inactive, Used By `0`, Last Used in Journal bernilai null, Modified By `Dewi Anggraini`, Last Updated `2026-02-05T10:00:00Z`. Modified By tampil `Dewi A`, dari `Dewi Anggraini`.
  - DU-120-5: Account `4-7002`, Name `Gain and Loss on Disposal`, Function `Loss on Disposal`, status Active, Used By `2`, Last Used in Journal `Jul 2026`, Modified By `Dewi Anggreni`, Last Updated `2026-02-12T13:20:00Z`. Modified By tampil `Dewi A`, dari `Dewi Anggreni`.
  - DU-120-6: Account `6-2001`, Name `Repairs & Maintenance Expense`, Function `Capitalization Offset`, status Active, Used By `0`, Last Used in Journal kosong (belum pernah diisi, sehingga tanpa entri Changelog), Modified By `System`, Last Updated (waktu dibuat, tanpa entri Changelog) `2026-02-15T07:40:00Z`. Last Updated tampil `15/02/26, 07:40`, dari `2026-02-15T07:40:00Z`.
  - DU-120-7: Account `1-3001`, Name `Disposal Proceeds – Clearing`, Function `Disposal Proceeds`, status Active, Used By `1`, Last Used in Journal berupa string kosong, Modified By `Buzzlightyear Sumardi`, Last Updated `2026-01-20T16:45:00Z`. Modified By tampil `Buzzlightyear S`, dari `Buzzlightyear Sumardi`.
  - DU-120-8: Account `5-6002`, Name `Regional Procurement and Vendor Management Office Jakarta`, Function `Depreciation Expense`, status Active, Used By `1`, Last Used in Journal `Jun 2026`, Modified By `Siti Nurbaya`, Last Updated `2026-01-15T11:10:00Z`.
  - DU-120-9: Account `9-0001`, Name `<b>Kas Besar</b>`, Function `Asset Cost`, status Active, Used By `0`, Last Used in Journal bernilai null, Modified By `Rina Pratiwi`, Last Updated `2026-01-05T09:00:00Z`.
- Kondisi:
  - K1: tabel berisi DU-120-1 sampai DU-120-9 dengan kolom tampil menurut bawaan; Date Format bernilai `dd/MM/yy`, Time Format bernilai `24h`, dan Time Zone bernilai `UTC`.
  - K2: seperti K1, dengan kolom `Modified By` dan `Last Updated` ikut ditampilkan.

## Test Steps

### Elemen halaman dan toolbar
1. Tampilkan Tab Chart of Accounts dengan kondisi K1
2. Verifikasi segmen breadcrumb `Settings`, `Accounting`, dan `Chart of Accounts` tampil berurutan
3. Verifikasi segmen `Settings` dan `Chart of Accounts` berupa teks statis yang tidak bisa diklik
4. Verifikasi segmen `Accounting` bisa diklik
5. Verifikasi tab `Preferences`, `Chart of Accounts`, `Tax Depreciation Class`, dan `Asset Class` tampil di tab bar dengan `Chart of Accounts` aktif
6. Arahkan kursor ke tombol `[?]`
7. Verifikasi `Show guide` tersampaikan pada tombol `[?]`
8. Verifikasi kontrol toolbar tampil berurutan dari kiri ke kanan: Search, Filter, Download, Changelog, lalu `[+ Account]`
9. Arahkan kursor ke ikon Search
10. Verifikasi `Search` tersampaikan pada ikon Search
11. Arahkan kursor ke ikon Filter
12. Verifikasi `Filter` tersampaikan pada ikon Filter
13. Arahkan kursor ke ikon Download
14. Verifikasi `Download` tersampaikan pada ikon Download
15. Arahkan kursor ke ikon Changelog
16. Verifikasi `Changelog` tersampaikan pada ikon Changelog
17. Arahkan kursor ke `⋯` pada header kolom Actions
18. Verifikasi `Column Visibility` tersampaikan pada `⋯` di header kolom Actions
19. Verifikasi tombol `[+ Account]` tampil
20. Klik ikon Download
21. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil

### Placeholder kotak Search
22. Tampilkan Tab Chart of Accounts dengan kondisi K1
23. Klik ikon Search
24. Verifikasi kotak Search memuat placeholder `Search account...`

### Kolom default dan kolom tersembunyi
25. Tampilkan Tab Chart of Accounts dengan kondisi K1
26. Verifikasi header kolom `Active` tampil
27. Verifikasi header kolom `Account Code` tampil
28. Verifikasi header kolom `Account Name` tampil
29. Verifikasi header kolom `Function` tampil
30. Verifikasi header kolom `Used By` tampil
31. Verifikasi header kolom `Last Used in Journal` tampil
32. Verifikasi kolom `Modified By` dan `Last Updated` tidak tampil
33. Klik `⋯` pada header kolom Actions
34. Centang `Modified By` pada panel Column Visibility
35. Centang `Last Updated` pada panel Column Visibility
36. Verifikasi header kolom `Modified By` tampil
37. Verifikasi header kolom `Last Updated` tampil

### Isi sel dan format kolom data
38. Tampilkan Tab Chart of Accounts dengan kondisi K2
39. Verifikasi baris `1-1001` menampilkan Account Code `1-1001`
40. Verifikasi baris `1-1001` menampilkan Account Name `Fixed Assets – Equipment`
41. Verifikasi switch pada kolom Active baris `1-1001` dalam keadaan aktif
42. Verifikasi switch pada kolom Active baris `4-7001` dalam keadaan tidak aktif
43. Verifikasi baris `1-1001` menampilkan Function `Asset Cost`
44. Verifikasi baris `1-2001` menampilkan Function `Accumulated Depreciation`
45. Verifikasi baris `5-6001` menampilkan Function `Depreciation Expense`
46. Verifikasi baris `4-7001` menampilkan Function `Gain on Disposal`
47. Verifikasi baris `4-7002` menampilkan Function `Loss on Disposal`
48. Verifikasi baris `6-2001` menampilkan Function `Capitalization Offset`
49. Verifikasi baris `1-3001` menampilkan Function `Disposal Proceeds`
50. Verifikasi baris `1-1001` menampilkan Used By `3` sebagai angka bulat yang bisa diklik
51. Verifikasi baris `5-6001` menampilkan Used By `0` sebagai teks biasa yang tidak bisa diklik
52. Verifikasi baris `1-1001` menampilkan Last Used in Journal `Oct 2026`
53. Verifikasi baris `5-6001` menampilkan Last Used in Journal `—`
54. Verifikasi baris `4-7001` menampilkan Last Used in Journal `—`
55. Verifikasi baris `1-3001` menampilkan Last Used in Journal `—`
56. Arahkan kursor ke sel Last Used in Journal baris `5-6001`
57. Verifikasi sel Last Used in Journal baris `5-6001` tidak memiliki teks hover

### Modified By dan Last Updated
58. Tampilkan Tab Chart of Accounts dengan kondisi K2
59. Verifikasi baris `1-1001` menampilkan Modified By `Rina P`, dari `Rina Pratiwi`
60. Arahkan kursor ke sel Modified By baris `1-1001`
61. Verifikasi nama lengkap `Rina Pratiwi` tersampaikan pada sel Modified By baris `1-1001`
62. Verifikasi baris `1-2001` menampilkan Modified By `Budi`, dari `Budi`
63. Arahkan kursor ke sel Modified By baris `1-2001`
64. Verifikasi nama lengkap `Budi` tersampaikan pada sel Modified By baris `1-2001`
65. Verifikasi baris `5-6001` menampilkan Modified By `Alexander G`, dari `Alexander Graham Bell`
66. Arahkan kursor ke sel Modified By baris `5-6001`
67. Verifikasi nama lengkap `Alexander Graham Bell` tersampaikan pada sel Modified By baris `5-6001`
68. Verifikasi baris `1-3001` menampilkan Modified By `Buzzlightyear S`, dari `Buzzlightyear Sumardi`
69. Arahkan kursor ke sel Modified By baris `1-3001`
70. Verifikasi nama lengkap `Buzzlightyear Sumardi` tersampaikan pada sel Modified By baris `1-3001`
71. Verifikasi baris `4-7001` menampilkan Modified By `Dewi A`, dari `Dewi Anggraini`
72. Arahkan kursor ke sel Modified By baris `4-7001`
73. Verifikasi nama lengkap `Dewi Anggraini` tersampaikan pada sel Modified By baris `4-7001`
74. Verifikasi baris `4-7002` menampilkan Modified By `Dewi A`, dari `Dewi Anggreni`
75. Arahkan kursor ke sel Modified By baris `4-7002`
76. Verifikasi nama lengkap `Dewi Anggreni` tersampaikan pada sel Modified By baris `4-7002`
77. Verifikasi baris `6-2001` menampilkan Modified By `System`
78. Verifikasi baris `1-1001` menampilkan Last Updated `25/03/26, 09:15`, dari `2026-03-25T09:15:00Z`
79. Verifikasi baris `1-2001` menampilkan Last Updated `24/03/26, 23:30`, dari `2026-03-24T23:30:00Z`
80. Verifikasi baris `6-2001` menampilkan Last Updated `15/02/26, 07:40`, dari `2026-02-15T07:40:00Z`

### Teks panjang dan markup tampil apa adanya
81. Tampilkan Tab Chart of Accounts dengan kondisi K2
82. Verifikasi baris `5-6002` menampilkan Account Name `Regional Procurement and Vendor Management Office Jakarta` utuh tanpa dipotong
83. Verifikasi baris `9-0001` menampilkan Account Name `<b>Kas Besar</b>` apa adanya sebagai teks

### Posisi kolom Last Updated
84. Tampilkan Tab Chart of Accounts dengan kondisi K2
85. Verifikasi kolom `Last Updated` adalah kolom data terakhir sebelum kolom Actions

### Badge Function di tabel tanpa tooltip
86. Tampilkan Tab Chart of Accounts dengan kondisi K1
87. Verifikasi baris `1-1001` menampilkan badge Function `Asset Cost`
88. Arahkan kursor ke badge Function `Asset Cost` pada baris `1-1001`
89. Verifikasi tidak ada teks bantuan yang tersampaikan pada badge Function baris `1-1001`

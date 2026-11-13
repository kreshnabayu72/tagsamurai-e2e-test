---
id: TC-FA-FAREG-E2E-047-history-tabel
title: "Sub tab History: isi tabel, Search, Filter, sort, dan aksi baris"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#r46", "§4.1#r47", "§4.1#r48", "§4.1#r49", "§4.1#r50", "§4.1#r51", "§4.1#r52", "§4.1#p16", "§5#r3", "§5#r4", "§9.5#r5", "EB-FLT-5@tabel-history", "EB-SRC-5@tabel-history"]
smoke: []
dependsOn: []
trace:
  "§4.1#r47": [2, 17, 38, 41, 77]
  "§4.1#r46": [3, 15, 38, 75, 104]
  "§4.1#r48": [4, 19, 38, 47, 79]
  "§4.1#r49": [5, 6, 7, 8, 21, 29, 30, 34, 38, 52, 81]
  "§4.1#r50": [9, 23, 25, 38, 57, 83]
  "§4.1#r51": [10, 11, 25, 38, 66, 70, 85]
  "§4.1#r52": [12, 13, 27, 38, 62, 87]
  "§5#r4": [13]
  "§9.5#r5": [13]
  "§5#r3": [15]
  "EB-FLT-5@tabel-history": [66, 70, 71]
  "EB-SRC-5@tabel-history": [89, 93, 96]
  "§4.1#p16": [98, 99, 101, 108]
coverage:
  web: automated
---

# Sub tab History: isi tabel, Search, Filter, sort, dan aksi baris

## Prerequisites
- Aktor: Total Control `Dian P`, seluruh client.
- Layar awal: Assets > Registration > History.
- Data:
  - DU-047-1: Pengajuan History dengan Registration ID yang dibentuk server saat Submit, Group `Gudang Barat {runId}`, Total Asset `8`, Status `Approved`, Requested By `Maya L`, Approver `Hadi K`, Last Updated `T0 − 1 hari`.
  - DU-047-2: Pengajuan History dengan Registration ID yang dibentuk server saat Submit, Group `Gudang Timur {runId}`, Total Asset `14`, Status `Partially Approved`, Requested By `Hadi K`, Approver `Maya L`, Last Updated `T0 − 2 hari`.
  - DU-047-3: Pengajuan History dengan Registration ID yang dibentuk server saat Submit, Group `Gudang Utara {runId}`, Total Asset `3`, Status `Rejected`, Requested By `Siti N`, Approver `Rina W`, Last Updated `T0 − 3 hari`.
  - DU-047-4: Pengajuan History dengan Registration ID yang dibentuk server saat Submit, Group `Gudang Selatan {runId}`, Total Asset `97`, Status `Canceled`, Requested By `Rina W`, Approver `—`, Last Updated `T0 − 4 hari`.
  - Pengajuan DU-047-4 diajukan lebih dulu daripada DU-047-3, DU-047-3 lebih dulu daripada DU-047-2, dan DU-047-2 lebih dulu daripada DU-047-1.
  - Maya L, Hadi K, Siti N, dan Rina W adalah pengguna aktif dengan role Manage asset & TAG pada Group pengajuan masing-masing; Maya L dan Hadi K bukan Total Control.
- Kondisi: format tanggal General Settings `dd/MM/yy` dan format waktu 24 jam; seluruh kolom tabel History tampil.

## Test Steps

### Nilai sel tabel History
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi tabel sub tab History memuat baris `Gudang Barat {runId}`, `Gudang Timur {runId}`, `Gudang Utara {runId}`, `Gudang Selatan {runId}` dengan Group tampil sebagai Badge
3. Verifikasi Registration ID baris `Gudang Barat {runId}` berformat `REG-YYYYMMDD-NNNNN` dan sama dengan Registration ID milik DU-047-1
4. Verifikasi Total Asset baris `Gudang Barat {runId}` bernilai `8`
5. Verifikasi Status baris `Gudang Barat {runId}` tampil sebagai Badge `Approved` berwarna success
6. Verifikasi Status baris `Gudang Timur {runId}` tampil sebagai Badge `Partially Approved` berwarna warning
7. Verifikasi Status baris `Gudang Utara {runId}` tampil sebagai Badge `Rejected` berwarna danger
8. Verifikasi Status baris `Gudang Selatan {runId}` tampil sebagai Badge `Canceled` berwarna dark
9. Verifikasi Requested By baris `Gudang Barat {runId}` bernilai `Maya L`
10. Verifikasi Approver baris `Gudang Barat {runId}` bernilai `Hadi K`
11. Verifikasi Approver baris `Gudang Selatan {runId}` bernilai `—`
12. Verifikasi Last Updated baris `Gudang Barat {runId}` tampil dengan Date Format `dd/MM/yy` diikuti Time Format 24 jam

### Urutan awal Last Updated terbaru di atas
13. Verifikasi baris `Gudang Barat {runId}` tampil di atas baris `Gudang Timur {runId}`, baris `Gudang Timur {runId}` di atas baris `Gudang Utara {runId}`, dan baris `Gudang Utara {runId}` di atas baris `Gudang Selatan {runId}` (Last Updated terbaru di atas)

### Search pada kolom Searchable
14. Ganti isi kotak search dengan Registration ID milik DU-047-2, tekan Enter
15. Verifikasi tabel sub tab History memuat baris `Gudang Timur {runId}` dan tidak memuat baris `Gudang Barat {runId}`
16. Ganti isi kotak search dengan `Gudang Utara {runId}`, tekan Enter
17. Verifikasi tabel sub tab History memuat baris `Gudang Utara {runId}` dan tidak memuat baris `Gudang Barat {runId}`
18. Ganti isi kotak search dengan `97`, tekan Enter
19. Verifikasi tabel sub tab History memuat baris `Gudang Selatan {runId}`
20. Ganti isi kotak search dengan `Rejected`, tekan Enter
21. Verifikasi tabel sub tab History memuat baris `Gudang Utara {runId}` dan tidak memuat baris `Gudang Barat {runId}`
22. Ganti isi kotak search dengan `Siti N`, tekan Enter
23. Verifikasi tabel sub tab History memuat baris `Gudang Utara {runId}` dan tidak memuat baris `Gudang Barat {runId}`
24. Ganti isi kotak search dengan `Rina W`, tekan Enter
25. Verifikasi tabel sub tab History memuat baris `Gudang Utara {runId}`, `Gudang Selatan {runId}` dan tidak memuat baris `Gudang Barat {runId}`
26. Ganti isi kotak search dengan tanggal Last Updated baris `Gudang Timur {runId}` dalam Date Format `dd/MM/yy`, dari `T0 − 2 hari`, tekan Enter
27. Verifikasi baris `Gudang Timur {runId}` tidak tampil karena kolom Last Updated tidak dicari

### Search Status mencocokkan substring nilai lain
28. Ganti isi kotak search dengan `Approved`, tekan Enter
29. Verifikasi tabel sub tab History memuat baris `Gudang Barat {runId}`, `Gudang Timur {runId}` dan tidak memuat baris `Gudang Utara {runId}`, `Gudang Selatan {runId}`
30. Verifikasi baris `Gudang Timur {runId}` berstatus `Partially Approved` ikut tampil pada Search `Approved` karena Search mencocokkan substring
31. Klik ikon Filter
32. Pilih opsi `Approved` pada field `Status`
33. Klik `[Apply]`
34. Verifikasi tabel sub tab History memuat baris `Gudang Barat {runId}` dan tidak memuat baris `Gudang Timur {runId}`
35. Klik `[Clear Field]`
36. Klik `[Apply]`

### Filter pada kolom Filterable
37. Ganti isi kotak search dengan `{runId}`, tekan Enter
38. Verifikasi panel Filter memuat field `Group`, `Total Asset`, `Status`, `Requested By`, `Approver`, dan `Last Updated` dan tidak memuat field `Registration ID`
39. Pilih Group `Gudang Timur {runId}` pada field `Group`
40. Klik `[Apply]`
41. Verifikasi tabel sub tab History memuat baris `Gudang Timur {runId}` dan tidak memuat baris `Gudang Barat {runId}`
42. Klik `[Clear Field]`
43. Klik `[Apply]`
44. Isi Min `8` pada field `Total Asset`
45. Isi Max `14` pada field `Total Asset`
46. Klik `[Apply]`
47. Verifikasi tabel sub tab History memuat baris `Gudang Barat {runId}`, `Gudang Timur {runId}` dan tidak memuat baris `Gudang Utara {runId}`, `Gudang Selatan {runId}`
48. Klik `[Clear Field]`
49. Klik `[Apply]`
50. Pilih opsi `Rejected` pada field `Status`
51. Klik `[Apply]`
52. Verifikasi tabel sub tab History memuat baris `Gudang Utara {runId}` dan tidak memuat baris `Gudang Barat {runId}`
53. Klik `[Clear Field]`
54. Klik `[Apply]`
55. Pilih opsi `Maya L` pada field `Requested By`
56. Klik `[Apply]`
57. Verifikasi tabel sub tab History memuat baris `Gudang Barat {runId}` dan tidak memuat baris `Gudang Timur {runId}`
58. Klik `[Clear Field]`
59. Klik `[Apply]`
60. Pilih rentang tanggal `T0 − 3 hari` sampai `T0 − 2 hari` pada field `Last Updated`
61. Klik `[Apply]`
62. Verifikasi tabel sub tab History memuat baris `Gudang Timur {runId}`, `Gudang Utara {runId}` dan tidak memuat baris `Gudang Barat {runId}`, `Gudang Selatan {runId}`
63. Klik `[Clear Field]`
64. Klik `[Apply]`

### Filter Approver tidak menjadikan nilai kosong sebagai opsi
65. Buka daftar opsi field `Approver`
66. Verifikasi daftar opsi field `Approver` memuat `Hadi K`, `Maya L`, dan `Rina W` dan tidak memuat opsi `—`
67. Pilih opsi `Hadi K` pada field `Approver`
68. Pilih opsi `Maya L` pada field `Approver`
69. Klik `[Apply]`
70. Verifikasi tabel sub tab History memuat baris `Gudang Barat {runId}`, `Gudang Timur {runId}` dan tidak memuat baris `Gudang Utara {runId}`, `Gudang Selatan {runId}`
71. Verifikasi baris `Gudang Selatan {runId}` dengan Approver `—` tersaring keluar karena memilih opsi Approver apa pun menyaring keluar nilai kosong
72. Klik `[Clear Field]`
73. Klik `[Apply]`

### Sort pada kolom Sortable
74. Klik ikon sort pada header kolom `Registration ID`
75. Verifikasi urutan baris kolom `Registration ID` naik: `Gudang Selatan {runId}`, `Gudang Utara {runId}`, `Gudang Timur {runId}`, `Gudang Barat {runId}`
76. Klik ikon sort pada header kolom `Group`
77. Verifikasi urutan baris kolom `Group` naik: `Gudang Barat {runId}`, `Gudang Selatan {runId}`, `Gudang Timur {runId}`, `Gudang Utara {runId}`
78. Klik ikon sort pada header kolom `Total Asset`
79. Verifikasi urutan baris kolom `Total Asset` naik: `Gudang Utara {runId}`, `Gudang Barat {runId}`, `Gudang Timur {runId}`, `Gudang Selatan {runId}`
80. Klik ikon sort pada header kolom `Status`
81. Verifikasi urutan baris kolom `Status` naik: `Gudang Barat {runId}`, `Gudang Selatan {runId}`, `Gudang Timur {runId}`, `Gudang Utara {runId}`
82. Klik ikon sort pada header kolom `Requested By`
83. Verifikasi urutan baris kolom `Requested By` naik: `Gudang Timur {runId}`, `Gudang Barat {runId}`, `Gudang Selatan {runId}`, `Gudang Utara {runId}`
84. Klik ikon sort pada header kolom `Approver`
85. Verifikasi urutan relatif baris dengan Approver terisi pada kolom `Approver` naik: `Gudang Barat {runId}`, `Gudang Timur {runId}`, `Gudang Utara {runId}`
86. Klik ikon sort pada header kolom `Last Updated`
87. Verifikasi urutan baris kolom `Last Updated` naik (Oldest First): `Gudang Selatan {runId}`, `Gudang Utara {runId}`, `Gudang Timur {runId}`, `Gudang Barat {runId}`

### Kolom Status yang disembunyikan tidak dicari
88. Ganti isi kotak search dengan `Rejected`, tekan Enter
89. Verifikasi tabel sub tab History memuat baris `Gudang Utara {runId}`
90. Klik header kolom Actions `⋯`
91. Hilangkan centang `Status` pada panel Column Visibility
92. Ganti isi kotak search dengan `Rejected`, tekan Enter
93. Verifikasi baris `Gudang Utara {runId}` tidak tampil di tabel sub tab History
94. Centang kembali `Status` pada panel Column Visibility
95. Ganti isi kotak search dengan `Rejected`, tekan Enter
96. Verifikasi tabel sub tab History memuat baris `Gudang Utara {runId}`

### Aksi baris
97. Ganti isi kotak search dengan `{runId}`, tekan Enter
98. Verifikasi kolom `Actions` adalah kolom terakhir tabel sub tab History, sesudah kolom `Last Updated`
99. Verifikasi baris `Gudang Barat {runId}` menampilkan ikon aksi `Detail` dan `Registration Log` dan tidak menampilkan `Cancel registration`
100. Klik ikon `Detail` pada baris `Gudang Barat {runId}`
101. Verifikasi halaman Detail pengajuan terbuka dengan Registration ID milik DU-047-1
102. Klik tautan breadcrumb `History`
103. Klik Registration ID milik DU-047-2
104. Verifikasi halaman Detail pengajuan terbuka dengan Registration ID milik DU-047-2
105. Klik tautan breadcrumb `History`
106. Ganti isi kotak search dengan `{runId}`, tekan Enter
107. Klik ikon `Registration Log` pada baris `Gudang Utara {runId}`
108. Verifikasi dialog `Registration Log` tampil di atas halaman History
109. Klik ikon X pada dialog `Registration Log`

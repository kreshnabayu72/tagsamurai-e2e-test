---
id: TC-FA-FASVC-E2E-005-gating-read-only
title: "Gating Read Only: Lihat, Search, Filter, Sort, Download; Tanpa Aksi Tulis"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "RA-FASVC-01", "RA-FASVC-02", "RA-FASVC-03", "RA-FASVC-04", "RA-FASVC-05", "FASVC-LOGIC-08a", "FASVC-LOGIC-08d", "FASVC-LOGIC-08g", "FASVC-LOGIC-08h", "FASVC-LOGIC-08i", "EB-AKS-4"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [33, 44, 45, 68]
  "§2.1#r2": 36
  "§2.1#r3": [64, 65, 74, 75]
  "§2.1#r4": [66, 76]
  "§2.1#r5": 38
  "§4.8#r1": 31
  "§4.8#r2": [63, 73]
  "§4.8#r3": 36
  "§4.8#r4": [65, 74, 75]
  "§4.8#r5": 64
  "§4.8#r6": [66, 76]
  "§4.8#r7": 34
  "§4.8#r8": [35, 41]
  "RA-FASVC-01": [63, 73]
  "RA-FASVC-02": [65, 75]
  "RA-FASVC-03": 64
  "RA-FASVC-04": 74
  "RA-FASVC-05": [66, 76]
  "FASVC-LOGIC-08a": [44, 45, 68, 109, 110]
  "FASVC-LOGIC-08d": 36
  "FASVC-LOGIC-08g": [64, 65, 66, 74, 75, 76]
  "FASVC-LOGIC-08h": [63, 64, 65, 66, 73, 74, 75, 76]
  "FASVC-LOGIC-08i": 69
  "EB-AKS-4": [44, 46, 47, 49, 53, 54, 58, 60, 61, 80, 83]
anchor: [28, 79, 82]
coverage:
  web: automated
---

# Gating Read Only: Lihat, Search, Filter, Sort, Download; Tanpa Aksi Tulis

## Prerequisites
- Aktor: Read Only `Rudi ReadOnly {runId}` (cakupan `Branch Surabaya`) dan Total Control `Tania Control {runId}` sebagai pemicu.
- Layar awal: Dashboard Fixed Asset.
- Data:
  - DU-005-1: Group `Head Office`, node root pohon Group entitas aktor.
  - DU-005-2: Group `Branch Surabaya`, anak dari `Head Office`.
  - DU-005-3: Aktor `Rudi ReadOnly {runId}` dengan Role `Read Only`, cakupan `Branch Surabaya`.
  - DU-005-4: Aktor `Tania Control {runId}` dengan Role `Total Control`.
  - DU-005-5: Service Center `Servis Alfa {runId}`, Service type `Routine`, Available to `Branch Surabaya`, City `Surabaya`, Company email `layanan@servisalfa.co.id`, dibuat oleh `Tania Control {runId}`. Status `Active`. Usage `0`.
  - DU-005-6: Service Center `Servis Bravo {runId}`, Service type `Repair`, Available to `Branch Surabaya`, City `Jakarta Selatan`, Company email `layanan@servisbravo.co.id`, dibuat oleh `Tania Control {runId}` lalu di-Inactivate oleh `Tania Control {runId}`. Status `Inactive`. Usage `0`.
  - Urutan Name A-Z: `Servis Alfa {runId}` lalu `Servis Bravo {runId}`. Urutan City A-Z: `Jakarta Selatan` (`Servis Bravo {runId}`) lalu `Surabaya` (`Servis Alfa {runId}`).
  - DU-005-7: Group `Branch Malang`, anak dari `Head Office`, di luar cakupan `Rudi ReadOnly {runId}`.
  - DU-005-8: Service Center `Servis Malang Saja {runId}`, Service type `Routine`, Available to `Branch Malang`, City `Malang`, Company email `info@malangsajaro.co.id`, dibuat oleh `Tania Control {runId}`. Status `Active`. Usage `0`.
  - DU-005-9: Service Center `Servis Semua Group {runId}`, Service type `Routine`, Available to `All groups`, City `Bandung`, Company email `layanan@semuagrouproa.co.id`, dibuat oleh `Tania Control {runId}`. Status `Active`. Usage `0`.
- Kondisi:
  - Lisensi addon Maintenance aktif untuk entitas aktor.
  - Akun `Rudi ReadOnly {runId}` dan `Tania Control {runId}` aktif dan kredensialnya disediakan fase 2.
  - Master Data Count Limit bernilai `1000` dan entitas aktor berisi kurang dari 1.000 Service Center.

## Test Steps

### Total Control menyiapkan dua Service Center sebagai pemicu
1. Masuk sebagai `Tania Control {runId}`
2. Buka menu `Add-ons` pada sidebar
3. Klik `Service Center`
4. Klik `[+ Service Center]`
5. Isi Name `Servis Alfa {runId}`
6. Centang Service type `Routine`
7. Klik field Available to
8. Hapus centang node `All groups`
9. Centang node `Branch Surabaya`
10. Klik `[Select]`
11. Isi City `Surabaya`
12. Isi Company email `layanan@servisalfa.co.id`
13. Klik `[Submit]`
14. Klik `[+ Service Center]`
15. Isi Name `Servis Bravo {runId}`
16. Centang Service type `Repair`
17. Klik field Available to
18. Hapus centang node `All groups`
19. Centang node `Branch Surabaya`
20. Klik `[Select]`
21. Isi City `Jakarta Selatan`
22. Isi Company email `layanan@servisbravo.co.id`
23. Klik `[Submit]`
24. Ketik Search `Servis Bravo {runId}`, tekan Enter
25. Klik `⋯` pada baris `Servis Bravo {runId}`
26. Klik `Inactivate`
27. Klik `[Inactivate]`
28. Verifikasi kolom Status pada baris `Servis Bravo {runId}` menampilkan `Inactive`

### Menu dan toolbar bagi Read Only
29. Masuk sebagai `Rudi ReadOnly {runId}`
30. Buka menu `Add-ons` pada sidebar
31. Verifikasi menu `Service Center` tampil di bawah `Add-ons`
32. Klik `Service Center`
33. Verifikasi halaman daftar Service Center terbuka dengan breadcrumb `Add-ons > Service Center`
34. Verifikasi tombol `[Download]` tampil
35. Verifikasi tombol `[Changelog]` tampil
36. Verifikasi tombol `[+ Service Center]` tidak tampil

### Download menyediakan pilihan unduhan
37. Klik `[Download]`
38. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil
39. Tutup popover Download

### Changelog gabungan terbuka
40. Klik `[Changelog]`
41. Verifikasi modal `Changelog: Service Center` terbuka
42. Klik ikon close pada modal Changelog

### Search dan Pagination aktif dan cakupan baca terpenuhi
43. Ketik Search `{runId}`, tekan Enter
44. Verifikasi baris `Servis Alfa {runId}` tampil di tabel
45. Verifikasi baris `Servis Bravo {runId}` tampil di tabel
46. Verifikasi laporan Pagination menampilkan `Showing 1 to 2 of 2`

### Sort default Name A-Z dan sort kolom City
47. Verifikasi baris `Servis Alfa {runId}` berada di atas baris `Servis Bravo {runId}`
48. Klik header kolom `City`
49. Verifikasi baris `Servis Bravo {runId}` berada di atas baris `Servis Alfa {runId}`

### Filter Service Type aktif dan dilepas
50. Klik `[Filter]`
51. Pilih `Repair` pada filter `Service Type`
52. Klik `[Apply]`
53. Verifikasi baris `Servis Bravo {runId}` tampil di tabel
54. Verifikasi baris `Servis Alfa {runId}` tidak tampil di tabel
55. Klik `[Filter]`
56. Klik `[Clear Field]`
57. Klik `[Apply]`
58. Verifikasi baris `Servis Alfa {runId}` tampil di tabel

### Search mempersempit ke satu Service Center
59. Ganti isi kotak search dengan `Servis Bravo {runId}`, tekan Enter
60. Verifikasi baris `Servis Bravo {runId}` tampil di tabel
61. Verifikasi baris `Servis Alfa {runId}` tidak tampil di tabel

### Service Center Inactive tanpa aksi kelola bagi Read Only
62. Klik `⋯` pada baris `Servis Bravo {runId}`
63. Verifikasi aksi `Detail` tampil
64. Verifikasi aksi `Activate` tidak tampil
65. Verifikasi aksi `Edit` tidak tampil
66. Verifikasi aksi `Delete` tidak tampil
67. Klik `Detail`
68. Verifikasi halaman Detail menampilkan nama `Servis Bravo {runId}`
69. Verifikasi info `This service center also serves groups outside your access. Ask an admin who manages all of them.` tidak tampil
70. Klik breadcrumb `Service Center`

### Service Center Active tanpa aksi kelola bagi Read Only
71. Ganti isi kotak search dengan `Servis Alfa {runId}`, tekan Enter
72. Klik `⋯` pada baris `Servis Alfa {runId}`
73. Verifikasi aksi `Detail` tampil
74. Verifikasi aksi `Inactivate` tidak tampil
75. Verifikasi aksi `Edit` tidak tampil
76. Verifikasi aksi `Delete` tidak tampil

### Setup Column aktif dan pilihan kolom bertahan sesudah muat ulang
77. Klik `Column Visibility` pada header kolom Actions (⋯)
78. Hapus centang kolom `City`
79. Verifikasi header kolom `Name` tampil
80. Verifikasi header kolom `City` tidak tampil
81. Muat ulang halaman
82. Verifikasi header kolom `Name` tampil
83. Verifikasi header kolom `City` tetap tidak tampil
84. Klik `Column Visibility` pada header kolom Actions (⋯)
85. Centang kolom `City`

### Cakupan baca Read Only: di luar irisan tidak tampil dan All groups tampil
86. Masuk sebagai `Tania Control {runId}`
87. Buka menu `Add-ons` pada sidebar
88. Klik `Service Center`
89. Klik `[+ Service Center]`
90. Isi Name `Servis Malang Saja {runId}`
91. Centang Service type `Routine`
92. Klik field Available to
93. Hapus centang node `All groups`
94. Centang node `Branch Malang`
95. Klik `[Select]`
96. Isi City `Malang`
97. Isi Company email `info@malangsajaro.co.id`
98. Klik `[Submit]`
99. Klik `[+ Service Center]`
100. Isi Name `Servis Semua Group {runId}`
101. Centang Service type `Routine`
102. Isi City `Bandung`
103. Isi Company email `layanan@semuagrouproa.co.id`
104. Klik `[Submit]`
105. Masuk sebagai `Rudi ReadOnly {runId}`
106. Buka menu `Add-ons` pada sidebar
107. Klik `Service Center`
108. Ketik Search `{runId}`, tekan Enter
109. Verifikasi baris `Servis Semua Group {runId}` tampil di tabel
110. Verifikasi baris `Servis Malang Saja {runId}` tidak tampil di tabel

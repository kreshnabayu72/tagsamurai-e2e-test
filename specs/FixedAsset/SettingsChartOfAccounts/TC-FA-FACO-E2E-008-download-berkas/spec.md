---
id: TC-FA-FACO-E2E-008-download-berkas
title: "Download Account List dan Changelog menghasilkan berkas sesuai Search, Filter, dan kolom visible"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["F-FACO-11", "R-11", "§5#b8", "§5#b9", "§[F-FACO-11] Download Account List#p1", "§[F-FACO-11] Download Account List#r1", "§9.4.2#r26", "EB-FB-2@download", "EB-DL-1@tabel-account-list", "EB-DL-1@tabel-changelog", "EB-DL-2@tabel-account-list", "EB-DL-2@tabel-changelog", "EB-DL-3@tabel-account-list", "EB-DL-3@tabel-changelog"]
smoke: []
dependsOn: []
trace:
  "F-FACO-11": [5, 38]
  "R-11": [4, 26, 107, 109]
  "§5#b8": [3, 19, 46]
  "§5#b9": 58
  "§[F-FACO-11] Download Account List#p1": [5, 19]
  "§[F-FACO-11] Download Account List#r1": 27
  "§9.4.2#r26": 27
  "EB-FB-2@download": [4, 9, 26, 59]
  "EB-DL-1@tabel-account-list": [5, 19, 20, 38, 46]
  "EB-DL-1@tabel-changelog": [60, 67, 75, 93, 101]
  "EB-DL-2@tabel-account-list": [4, 9, 26]
  "EB-DL-2@tabel-changelog": [59, 68]
  "EB-DL-3@tabel-account-list": [3, 8, 18, 25]
  "EB-DL-3@tabel-changelog": [58, 66]
anchor: [3, 8, 15, 22, 25, 35, 45, 55, 58, 66, 89, 98]
coverage:
  web: automated
---

# Download Account List dan Changelog menghasilkan berkas sesuai Search, Filter, dan kolom visible

## Prerequisites
- Aktor: pengguna Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-008-1: 9 akun, Account Code `DL{n}-{runId}`, Account Name `0{n} Unduh {runId}`, Account Function `Asset Cost`, Status `Active`, untuk n 1 sampai 9 (DL1 bernama `01 Unduh {runId}`, DL9 bernama `09 Unduh {runId}`). Account Name DL1 sesudah Edit: `01 Unduh {runId} Ubah`.
  - DU-008-2: akun `DL10-{runId}`, Account Name `10 Unduh {runId}`, Account Function `Depreciation Expense`, Status `Active`.
  - DU-008-3: akun `DL11-{runId}`, Account Name `11 Unduh {runId}`, Account Function `Depreciation Expense`, Status `Active`.
  - DU-008-4: akun `DL12-{runId}`, Account Name `12 Unduh {runId}`, Account Function `Depreciation Expense`, Status `Active`.
  - Seluruh 12 akun memuat `Unduh {runId}` pada Account Name, sehingga Search `Unduh {runId}` hanya mencocokkan baris milik spec ini. Ukuran halaman tabel 10 baris, sehingga 12 baris tersebar di dua halaman.
  - Akun milik spec ini tidak punya entri Changelog sebelum langkah Edit.
  - Pada kelompok langkah sesudahnya seluruh 12 akun dinonaktifkan sekaligus lewat Bulk Deactivate (Used By `0`), sehingga Changelog yang disaring dengan runId spec ini berisi 13 entri milik spec ini: satu entri Edit Field `Account Name` untuk DL1 dan 12 entri Edit Field `Status`. Dengan ukuran halaman modal 10 entri, halaman 2 memuat 3 entri.
- Kondisi:
  - Kolom `Used By` tampil di tabel Account List (kondisi bawaan).

## Test Steps
### Download tanpa Search atau Filter memuat seluruh baris lintas halaman
1. Klik ikon Download
2. Klik `Download as CSV`
3. Verifikasi berkas terunduh bernama `Chart-of-Accounts` berekstensi `.csv`
4. Verifikasi tidak ada toast yang tampil sesudah berkas terunduh
5. Verifikasi berkas memuat 12 baris milik spec ini, yaitu Account Code `DL1-{runId}` sampai `DL12-{runId}`, walau tabel menampilkan 10 baris per halaman
6. Klik ikon Download
7. Klik `Download as XLSX`
8. Verifikasi berkas terunduh bernama `Chart-of-Accounts` berekstensi `.xlsx`
9. Verifikasi tidak ada toast sukses yang tampil sesudah unduhan XLSX

### Download mengikuti Search dan Filter yang aktif
10. Ketik Search `Unduh {runId}`, tekan Enter
11. Klik ikon Filter
12. Pilih `Depreciation Expense` pada field Function
13. Klik `[Apply]`
14. Klik ikon Filter untuk menutup Filter Panel
15. Verifikasi baris `DL10-{runId}` tampil di tabel
16. Klik ikon Download
17. Klik `Download as CSV`
18. Verifikasi berkas terunduh bernama `Chart-of-Accounts` berekstensi `.csv`
19. Verifikasi berkas memuat 3 baris, yaitu Account Code `DL10-{runId}` sampai `DL12-{runId}`
20. Verifikasi berkas tidak memuat baris Account Code `DL1-{runId}` karena tidak cocok dengan Filter

### Hasil kosong menghasilkan berkas hanya berisi baris header
21. Ganti isi kotak search dengan `01 Unduh {runId}`, tekan Enter
22. Verifikasi `No results found` tampil di tabel
23. Klik ikon Download
24. Klik `Download as CSV`
25. Verifikasi berkas terunduh bernama `Chart-of-Accounts` berekstensi `.csv` walau hasil kosong
26. Verifikasi tidak ada toast yang tampil sesudah berkas terunduh
27. Verifikasi berkas hanya berisi baris header yang memuat `Account Code`, `Account Name`, dan `Function`, tanpa satu pun baris data

### Urutan baris berkas mengikuti Sort aktif
28. Klik ikon Filter
29. Klik `[Clear Field]`
30. Klik `[Apply]`
31. Klik ikon Filter untuk menutup Filter Panel
32. Ganti isi kotak search dengan `Unduh {runId}`, tekan Enter
33. Klik header kolom Account Name (klik pertama)
34. Klik header kolom Account Name (klik kedua)
35. Verifikasi urutan 10 baris yang tampil pada halaman 1 tabel menurun menurut Account Name: `DL12-{runId}`, `DL11-{runId}`, `DL10-{runId}`, `DL9-{runId}`, `DL8-{runId}`, `DL7-{runId}`, `DL6-{runId}`, `DL5-{runId}`, `DL4-{runId}`, `DL3-{runId}`
36. Klik ikon Download
37. Klik `Download as CSV`
38. Verifikasi urutan baris di berkas sama dengan tabel, menurun menurut Account Name: `DL12-{runId}` sampai `DL1-{runId}`
39. Klik header kolom Account Name (klik ketiga)

### Kolom yang disembunyikan tidak ikut diunduh
40. Klik header kolom Actions `⋯`
41. Hapus centang `Used By` pada panel Column Visibility
42. Klik header kolom Actions `⋯` untuk menutup panel
43. Klik ikon Download
44. Klik `Download as CSV`
45. Verifikasi berkas memuat header `Account Code`, `Account Name`, dan `Function`
46. Verifikasi berkas tidak memuat header `Used By` karena kolomnya disembunyikan
47. Klik header kolom Actions `⋯`
48. Centang `Used By` pada panel Column Visibility
49. Klik header kolom Actions `⋯` untuk menutup panel

### Download modal Changelog memakai nama berkas Changelog-Chart-of-Accounts dan mengikuti Search serta kolom visible
50. Klik `⋯` pada baris `DL1-{runId}` > `Edit`
51. Ganti isi Account Name dengan `01 Unduh {runId} Ubah`
52. Klik `[Save]`
53. Klik ikon Changelog
54. Ketik Search `Unduh {runId}` pada modal Changelog, tekan Enter
55. Verifikasi entri dengan Account Code `DL1-{runId}` tampil di modal Changelog
56. Klik ikon Download pada modal Changelog
57. Klik `Download as CSV`
58. Verifikasi berkas terunduh bernama `Changelog-Chart-of-Accounts` berekstensi `.csv`
59. Verifikasi tidak ada toast yang tampil sesudah berkas Changelog terunduh
60. Verifikasi berkas memuat satu baris data, yaitu entri Account Code `DL1-{runId}`, karena Search aktif
61. Klik header kolom Actions `⋯` pada tabel Changelog
62. Hapus centang `Old Value` pada panel Column Visibility
63. Klik header kolom Actions `⋯` untuk menutup panel
64. Klik ikon Download pada modal Changelog
65. Klik `Download as XLSX`
66. Verifikasi berkas terunduh bernama `Changelog-Chart-of-Accounts` berekstensi `.xlsx`
67. Verifikasi berkas tidak memuat header `Old Value` karena kolomnya disembunyikan
68. Verifikasi tidak ada toast sukses yang tampil sesudah unduhan XLSX Changelog
69. Klik header kolom Actions `⋯` pada tabel Changelog
70. Centang `Old Value` pada panel Column Visibility
71. Klik header kolom Actions `⋯` untuk menutup panel
72. Klik `(←)` pada kotak Search modal Changelog
73. Klik ikon Download pada modal Changelog
74. Klik `Download as CSV`
75. Verifikasi berkas memuat entri Account Code `DL1-{runId}` walau Search sudah dibersihkan, yaitu cakupan seluruh entri Changelog tanpa Search

### Download Changelog tanpa Search atau Filter memuat seluruh entri lintas halaman
76. Klik `✕` pada modal Changelog
77. Centang baris `DL1-{runId}`
78. Klik `Select All (12 records)`
79. Klik `Bulk Action`
80. Klik `Deactivate`
81. Klik `[Deactivate]`
82. Klik header kolom Actions `⋯`
83. Centang `Last Updated` pada panel Column Visibility
84. Klik header kolom Actions `⋯` untuk menutup panel
85. Catat nilai Last Updated baris `DL2-{runId}`

86. Klik ikon Changelog
87. Ketik Search `{runId}` pada modal Changelog, tekan Enter
88. Klik halaman 2 pada Paginator modal Changelog
89. Verifikasi halaman 2 modal Changelog memuat 3 entri, sehingga Search `{runId}` menghasilkan 13 entri dengan 10 entri di halaman 1
90. Klik `(←)` pada kotak Search modal Changelog
91. Klik ikon Download pada modal Changelog
92. Klik `Download as CSV`
93. Verifikasi berkas memuat 13 entri milik spec ini, yaitu 12 baris Field `Status` untuk Account Code `DL1-{runId}` sampai `DL12-{runId}` dan satu baris Field `Account Name` untuk `DL1-{runId}`, lebih banyak daripada 10 baris yang tampil pada satu halaman modal

### Download Changelog mengikuti Filter yang aktif
94. Klik ikon Filter pada modal Changelog
95. Pilih `Account Name` pada field Field
96. Klik `[Apply]`
97. Ketik Search `{runId}` pada modal Changelog, tekan Enter
98. Verifikasi entri dengan Account Code `DL1-{runId}` dan Field `Account Name` tampil di modal Changelog
99. Klik ikon Download pada modal Changelog
100. Klik `Download as CSV`
101. Verifikasi berkas memuat satu baris data, yaitu entri Account Code `DL1-{runId}` dengan Field `Account Name`, dan tidak memuat baris Field `Status`, karena Filter Field `Account Name` dan Search `{runId}` aktif
102. Klik `[Clear Field]`
103. Klik `[Apply]`
104. Klik `(←)` pada kotak Search modal Changelog

### Download tidak menulis entri Changelog dan tidak memperbarui Last Updated
105. Ketik Search `{runId}` pada modal Changelog, tekan Enter
106. Klik halaman 2 pada Paginator modal Changelog
107. Verifikasi halaman 2 modal Changelog tetap memuat 3 entri, sehingga Search `{runId}` tetap menghasilkan 13 entri seperti sebelum seluruh unduhan pada kelompok sebelumnya
108. Klik `✕` pada modal Changelog
109. Verifikasi Last Updated baris `DL2-{runId}` tetap sama dengan nilai yang dicatat sebelum unduhan pada kelompok sebelumnya

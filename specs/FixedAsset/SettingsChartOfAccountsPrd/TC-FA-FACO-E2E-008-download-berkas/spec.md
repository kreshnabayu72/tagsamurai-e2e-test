---
id: TC-FA-FACO-E2E-008-download-berkas
title: "Download Account List dan Changelog menghasilkan berkas sesuai Search, Filter, dan kolom visible"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["F-FACO-11", "R-11", "§5#b7", "§5#b8", "§[F-FACO-11] Download Account List#p1", "§[F-FACO-11] Download Account List#r1", "§9.4.2#r26", "EB-FB-2@download", "EB-DL-1@tabel-account-list", "EB-DL-1@tabel-changelog", "EB-DL-2@tabel-account-list", "EB-DL-2@tabel-changelog", "EB-DL-3@tabel-account-list", "EB-DL-3@tabel-changelog"]
smoke: []
dependsOn: []
trace:
  "F-FACO-11": [5, 41]
  "R-11": [4, 30]
  "§5#b7": [3, 19, 49]
  "§5#b8": 61
  "§[F-FACO-11] Download Account List#p1": [5, 19]
  "§[F-FACO-11] Download Account List#r1": 31
  "§9.4.2#r26": 31
  "EB-FB-2@download": [4, 9, 30, 62]
  "EB-DL-1@tabel-account-list": [5, 19, 20, 41, 49]
  "EB-DL-1@tabel-changelog": [63, 70, 78]
  "EB-DL-2@tabel-account-list": [4, 9, 30]
  "EB-DL-2@tabel-changelog": [62, 71]
  "EB-DL-3@tabel-account-list": [3, 8, 18, 29]
  "EB-DL-3@tabel-changelog": [61, 69]
anchor: [3, 8, 15, 26, 29, 38, 48, 58, 61, 69]
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
21. Klik ikon Filter
22. Klik `[Clear Field]`
23. Pilih `Gain on Disposal` pada field Function
24. Klik `[Apply]`
25. Klik ikon Filter untuk menutup Filter Panel
26. Verifikasi `No results found` tampil di tabel
27. Klik ikon Download
28. Klik `Download as CSV`
29. Verifikasi berkas terunduh bernama `Chart-of-Accounts` berekstensi `.csv` walau hasil kosong
30. Verifikasi tidak ada toast yang tampil sesudah berkas terunduh
31. Verifikasi berkas hanya berisi baris header yang memuat `Account Code`, `Account Name`, dan `Function`, tanpa satu pun baris data

### Urutan baris berkas mengikuti Sort aktif
32. Klik ikon Filter
33. Klik `[Clear Field]`
34. Klik `[Apply]`
35. Klik ikon Filter untuk menutup Filter Panel
36. Klik header kolom Account Name (klik pertama)
37. Klik header kolom Account Name (klik kedua)
38. Verifikasi urutan baris tabel menurun menurut Account Name: `DL12-{runId}`, `DL11-{runId}`, `DL10-{runId}`, `DL9-{runId}`, `DL8-{runId}`, `DL7-{runId}`, `DL6-{runId}`, `DL5-{runId}`, `DL4-{runId}`, `DL3-{runId}`, `DL2-{runId}`, `DL1-{runId}`
39. Klik ikon Download
40. Klik `Download as CSV`
41. Verifikasi urutan baris di berkas sama dengan tabel, menurun menurut Account Name: `DL12-{runId}` sampai `DL1-{runId}`
42. Klik header kolom Account Name (klik ketiga)

### Kolom yang disembunyikan tidak ikut diunduh
43. Klik header kolom Actions `⋯`
44. Hapus centang `Used By` pada panel Column Visibility
45. Klik header kolom Actions `⋯` untuk menutup panel
46. Klik ikon Download
47. Klik `Download as CSV`
48. Verifikasi berkas memuat header `Account Code`, `Account Name`, dan `Function`
49. Verifikasi berkas tidak memuat header `Used By` karena kolomnya disembunyikan
50. Klik header kolom Actions `⋯`
51. Centang `Used By` pada panel Column Visibility
52. Klik header kolom Actions `⋯` untuk menutup panel

### Download modal Changelog memakai nama berkas Changelog-Chart-of-Accounts dan mengikuti Search serta kolom visible
53. Klik `⋯` pada baris `DL1-{runId}` > `Edit`
54. Ganti isi Account Name dengan `01 Unduh {runId} Ubah`
55. Klik `[Save]`
56. Klik ikon Changelog
57. Ketik Search `Unduh {runId}` pada modal Changelog, tekan Enter
58. Verifikasi entri dengan Account Code `DL1-{runId}` tampil di modal Changelog
59. Klik ikon Download pada modal Changelog
60. Klik `Download as CSV`
61. Verifikasi berkas terunduh bernama `Changelog-Chart-of-Accounts` berekstensi `.csv`
62. Verifikasi tidak ada toast yang tampil sesudah berkas Changelog terunduh
63. Verifikasi berkas memuat satu baris data, yaitu entri Account Code `DL1-{runId}`, karena Search aktif
64. Klik header kolom Actions `⋯` pada tabel Changelog
65. Hapus centang `Old Value` pada panel Column Visibility
66. Klik header kolom Actions `⋯` untuk menutup panel
67. Klik ikon Download pada modal Changelog
68. Klik `Download as XLSX`
69. Verifikasi berkas terunduh bernama `Changelog-Chart-of-Accounts` berekstensi `.xlsx`
70. Verifikasi berkas tidak memuat header `Old Value` karena kolomnya disembunyikan
71. Verifikasi tidak ada toast sukses yang tampil sesudah unduhan XLSX Changelog
72. Klik header kolom Actions `⋯` pada tabel Changelog
73. Centang `Old Value` pada panel Column Visibility
74. Klik header kolom Actions `⋯` untuk menutup panel
75. Klik `(←)` pada kotak Search modal Changelog
76. Klik ikon Download pada modal Changelog
77. Klik `Download as CSV`
78. Verifikasi berkas memuat entri Account Code `DL1-{runId}` walau Search sudah dibersihkan, yaitu cakupan seluruh entri Changelog tanpa Search

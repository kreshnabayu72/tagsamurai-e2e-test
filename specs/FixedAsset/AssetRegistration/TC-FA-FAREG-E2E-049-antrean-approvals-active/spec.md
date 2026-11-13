---
id: TC-FA-FAREG-E2E-049-antrean-approvals-active
title: "Antrean Approvals tab Active: isi, hitungan, Search, Filter, dan Review"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FAREG-LOGIC-06c", "§4.1#r127", "§4.1#r128", "§4.1#r129", "§4.1#r130", "§4.1#r131", "§4.1#p35", "§4.2.5#p1", "§4.2.5#b1", "§4.2.5#b3", "§5#r3", "§5#r4", "§9.5#r6", "§9.7#r7", "EB-SRC-5@antrean-approvals-active"]
smoke: []
dependsOn: []
trace:
  "§4.2.5#p1": [2, 4, 7]
  "§4.2.5#b1": [7, 14, 17, 18, 22, 81, 85, 88, 89, 91, 95, 98]
  "§4.1#r128": [9, 28, 35, 39, 61]
  "FAREG-LOGIC-06c": [10]
  "§9.7#r7": [10]
  "§4.1#r129": [10, 30, 35, 45, 63]
  "§4.1#r127": [11, 26, 35, 59, 85]
  "§4.1#r130": [12, 32, 35, 50, 65]
  "§4.1#r131": [13, 14, 34, 35, 55, 67]
  "§5#r4": [14]
  "§9.5#r6": [14]
  "§5#r3": [26]
  "§4.2.5#b3": [39, 45, 50, 55]
  "EB-SRC-5@antrean-approvals-active": [69, 73, 76]
  "§4.1#p35": [78, 79, 81]
coverage:
  web: automated
---

# Antrean Approvals tab Active: isi, hitungan, Search, Filter, dan Review

## Prerequisites
- Aktor: Manage asset & TAG `Maya L`, pemegang capability Update pada Group `Gudang Kenari {runId}`, `Gudang Jabon {runId}`, dan `Gudang Trembesi {runId}` dan tidak pada Group `Gudang Luar Cakupan {runId}`, approver yang bukan pengaju satu pun pengajuan data uji.
- Layar awal: Assets > Registration > Draft.
- Data:
  - DU-049-1: Pengajuan Waiting for Approval dengan Registration ID yang dibentuk server saat Submit, Group `Gudang Kenari {runId}`, Total Asset `12`, Requested By `Hadi K`, Last Updated `T0 − 1 hari`.
  - DU-049-2: Pengajuan Waiting for Approval dengan Registration ID yang dibentuk server saat Submit, Group `Gudang Jabon {runId}`, Total Asset `30`, Requested By `Siti N`, Last Updated `T0 − 2 hari`.
  - DU-049-3: Pengajuan Waiting for Approval dengan Registration ID yang dibentuk server saat Submit, Group `Gudang Trembesi {runId}`, Total Asset `5`, Requested By `Rina W`, Last Updated `T0 − 3 hari`.
  - DU-049-4: Pengajuan Waiting for Approval dengan Registration ID yang dibentuk server saat Submit, Group `Gudang Luar Cakupan {runId}`, Total Asset `4`, Requested By `Siti N`, Last Updated `T0 − 4 hari`, di luar cakupan Group aktor.
  - DU-049-1 memuat 12 aset berstatus Waiting for Approval dalam satu pengajuan.
  - Pengajuan DU-049-3 diajukan lebih dulu daripada DU-049-2, dan DU-049-2 lebih dulu daripada DU-049-1.
  - Hadi K, Siti N, dan Rina W adalah pengguna aktif dengan role Manage asset & TAG pada Group pengajuan masing-masing.
- Kondisi: format tanggal General Settings `dd/MM/yy` dan format waktu 24 jam; kolom Requested By tampil; induk menu `Approvals` pada sidebar tertutup.

## Test Steps

### Menu sidebar Approvals
1. Klik induk menu `Approvals` pada sidebar
2. Verifikasi induk menu `Approvals` terbuka dan memuat satu anak menu, yaitu `Registration`
3. Klik induk menu `Approvals` pada sidebar sekali lagi
4. Verifikasi induk menu `Approvals` tertutup dan anak menu `Registration` tersembunyi
5. Klik induk menu `Approvals` pada sidebar sekali lagi
6. Klik anak menu `Registration`
7. Verifikasi halaman antrean terbuka dengan breadcrumb `Approvals > Registration > Active`

### Nilai sel tab Active
8. Ketik Search `{runId}`, tekan Enter
9. Verifikasi tabel tab Active memuat tiga baris dengan nilai Group `Gudang Kenari {runId}`, `Gudang Jabon {runId}`, dan `Gudang Trembesi {runId}`
10. Verifikasi pengajuan `Gudang Kenari {runId}` yang memuat 12 aset tampil sebagai satu baris dengan Total Asset `12`
11. Verifikasi Registration ID baris `Gudang Kenari {runId}` berformat `REG-YYYYMMDD-NNNNN` dan sama dengan Registration ID milik DU-049-1
12. Verifikasi Requested By baris `Gudang Kenari {runId}` bernilai `Hadi K`
13. Verifikasi Last Updated baris `Gudang Kenari {runId}` tampil dengan Date Format `dd/MM/yy` diikuti Time Format 24 jam

### Urutan awal Last Updated terbaru di atas
14. Verifikasi baris `Gudang Kenari {runId}` tampil di atas baris `Gudang Jabon {runId}`, dan baris `Gudang Jabon {runId}` tampil di atas baris `Gudang Trembesi {runId}` (Last Updated terbaru di atas)

### Hitungan pada tab Active tidak mengikuti Search dan Filter
15. Catat angka N pada tab `Active (N)`
16. Ganti isi kotak search dengan `Hadi K`, tekan Enter
17. Verifikasi tabel tab Active memuat baris `Gudang Kenari {runId}` dan tidak memuat baris `Gudang Jabon {runId}`
18. Verifikasi angka N pada tab `Active (N)` sama dengan angka yang dicatat sebelum Search
19. Klik ikon Filter
20. Pilih Group `Gudang Jabon {runId}` pada field `Group`
21. Klik `[Apply]`
22. Verifikasi angka N pada tab `Active (N)` sama dengan angka yang dicatat sebelum Search dan Filter
23. Klik `[Clear Field]`
24. Klik `[Apply]`

### Search pada kolom Searchable
25. Ganti isi kotak search dengan Registration ID milik DU-049-2, tekan Enter
26. Verifikasi tabel tab Active memuat baris `Gudang Jabon {runId}` dan tidak memuat baris `Gudang Kenari {runId}`
27. Ganti isi kotak search dengan `Gudang Trembesi {runId}`, tekan Enter
28. Verifikasi tabel tab Active memuat baris `Gudang Trembesi {runId}` dan tidak memuat baris `Gudang Kenari {runId}`
29. Ganti isi kotak search dengan `30`, tekan Enter
30. Verifikasi tabel tab Active memuat baris `Gudang Jabon {runId}` dan tidak memuat baris `Gudang Kenari {runId}`
31. Ganti isi kotak search dengan `Rina W`, tekan Enter
32. Verifikasi tabel tab Active memuat baris `Gudang Trembesi {runId}` dan tidak memuat baris `Gudang Kenari {runId}`
33. Ganti isi kotak search dengan tanggal Last Updated baris `Gudang Jabon {runId}` dalam Date Format `dd/MM/yy`, dari `T0 − 2 hari`, tekan Enter
34. Verifikasi baris `Gudang Jabon {runId}` tidak tampil karena kolom Last Updated tidak dicari

### Filter pada kolom Filterable
35. Verifikasi panel Filter tab Active memuat field `Group`, `Total Asset`, `Requested By`, dan `Last Updated` dan tidak memuat field `Registration ID`
36. Ganti isi kotak search dengan `{runId}`, tekan Enter
37. Pilih Group `Gudang Jabon {runId}` pada field `Group`
38. Klik `[Apply]`
39. Verifikasi tabel tab Active memuat baris `Gudang Jabon {runId}` dan tidak memuat baris `Gudang Kenari {runId}`
40. Klik `[Clear Field]`
41. Klik `[Apply]`
42. Isi Min `12` pada field `Total Asset`
43. Isi Max `30` pada field `Total Asset`
44. Klik `[Apply]`
45. Verifikasi tabel tab Active memuat baris `Gudang Kenari {runId}`, `Gudang Jabon {runId}` dan tidak memuat baris `Gudang Trembesi {runId}`
46. Klik `[Clear Field]`
47. Klik `[Apply]`
48. Pilih opsi `Hadi K` pada field `Requested By`
49. Klik `[Apply]`
50. Verifikasi tabel tab Active memuat baris `Gudang Kenari {runId}` dan tidak memuat baris `Gudang Jabon {runId}`
51. Klik `[Clear Field]`
52. Klik `[Apply]`
53. Pilih rentang tanggal `T0 − 2 hari` sampai `T0 − 1 hari` pada field `Last Updated`
54. Klik `[Apply]`
55. Verifikasi tabel tab Active memuat baris `Gudang Kenari {runId}`, `Gudang Jabon {runId}` dan tidak memuat baris `Gudang Trembesi {runId}`
56. Klik `[Clear Field]`
57. Klik `[Apply]`

### Sort pada kolom Sortable
58. Klik ikon sort pada header kolom `Registration ID`
59. Verifikasi urutan baris kolom `Registration ID` naik: `Gudang Trembesi {runId}`, `Gudang Jabon {runId}`, `Gudang Kenari {runId}`
60. Klik ikon sort pada header kolom `Group`
61. Verifikasi urutan baris kolom `Group` naik: `Gudang Jabon {runId}`, `Gudang Kenari {runId}`, `Gudang Trembesi {runId}`
62. Klik ikon sort pada header kolom `Total Asset`
63. Verifikasi urutan baris kolom `Total Asset` naik: `Gudang Trembesi {runId}`, `Gudang Kenari {runId}`, `Gudang Jabon {runId}`
64. Klik ikon sort pada header kolom `Requested By`
65. Verifikasi urutan baris kolom `Requested By` naik: `Gudang Kenari {runId}`, `Gudang Trembesi {runId}`, `Gudang Jabon {runId}`
66. Klik ikon sort pada header kolom `Last Updated`
67. Verifikasi urutan baris kolom `Last Updated` naik (Oldest First): `Gudang Trembesi {runId}`, `Gudang Jabon {runId}`, `Gudang Kenari {runId}`

### Kolom yang disembunyikan tidak dicari
68. Ganti isi kotak search dengan `Hadi K`, tekan Enter
69. Verifikasi tabel tab Active memuat baris `Gudang Kenari {runId}`
70. Klik header kolom Actions `⋯`
71. Hilangkan centang `Requested By` pada panel Column Visibility
72. Ganti isi kotak search dengan `Hadi K`, tekan Enter
73. Verifikasi baris `Gudang Kenari {runId}` tidak tampil di tabel tab Active
74. Centang kembali `Requested By` pada panel Column Visibility
75. Ganti isi kotak search dengan `Hadi K`, tekan Enter
76. Verifikasi tabel tab Active memuat baris `Gudang Kenari {runId}`

### Aksi Review membuka halaman Approval
77. Ganti isi kotak search dengan `{runId}`, tekan Enter
78. Verifikasi kolom `Actions` adalah kolom terakhir tabel tab Active, sesudah kolom `Last Updated`
79. Verifikasi baris `Gudang Kenari {runId}` menampilkan ikon aksi `Review`
80. Klik ikon `Review` pada baris `Gudang Kenari {runId}`
81. Verifikasi halaman Approval terbuka dengan breadcrumb `Approvals > Registration > Active > Review` dan judul Registration ID milik DU-049-1
82. Klik tautan breadcrumb `Active`
83. Ganti isi kotak search dengan `{runId}`, tekan Enter
84. Klik Registration ID milik DU-049-2
85. Verifikasi halaman Approval terbuka dengan judul Registration ID milik DU-049-2
86. Klik tautan breadcrumb `Active`

### Keputusan tidak dibuat dari baris
87. Ganti isi kotak search dengan `{runId}`, tekan Enter
88. Verifikasi baris `Gudang Kenari {runId}` menampilkan ikon aksi `Review` sebagai satu-satunya ikon aksi dan tidak menampilkan `Approve`, `Return to Draft`, maupun `Reject`

### Hitungan pada tab Active mengikuti cakupan Group
89. Verifikasi tabel tab Active memuat baris `Gudang Kenari {runId}` dan tidak memuat baris `Gudang Luar Cakupan {runId}`
90. Klik `(←)` pada kotak Search
91. Verifikasi angka N pada tab `Active (N)` sama dengan nilai Z pada info paginasi `Showing X to Y of Z` tabel tab Active tanpa Search dan Filter

### Breadcrumb dan Back browser kembali ke tab Active
92. Ganti isi kotak search dengan `{runId}`, tekan Enter
93. Klik ikon `Review` pada baris `Gudang Kenari {runId}`
94. Klik tautan breadcrumb `Active`
95. Verifikasi antrean Approvals terbuka kembali pada tab `Active` dengan breadcrumb `Approvals > Registration > Active`
96. Klik ikon `Review` pada baris `Gudang Kenari {runId}`
97. Klik tombol Back browser
98. Verifikasi antrean Approvals terbuka kembali pada tab `Active` dengan breadcrumb `Approvals > Registration > Active`

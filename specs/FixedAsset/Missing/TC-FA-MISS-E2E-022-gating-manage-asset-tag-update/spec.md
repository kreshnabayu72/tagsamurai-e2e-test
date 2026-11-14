---
id: TC-FA-MISS-E2E-022-gating-manage-asset-tag-update
title: "Gating Manage asset & TAG (Update): hak per Group, record di luar Group hanya Read, Report Disposal tidak tersedia"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#r12", "§4.8#r1", "§4.8#r2", "§4.8#r5", "§4.8#r6", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§9.11#r1", "§9.11#r2", "§9.11#b1", "§2.1#b7", "§4.8#b2", "§2#b1", "§2.1#b9", "§2.1#p2", "§2.1#p7", "§2.1#p8", "§2.1#p9", "§2.1#p10", "EB-AKS-5@add-update", "EB-AKS-5@mark-as-found", "EB-AKS-5@confirm", "EB-AKS-5@reject", "§9.3#b1"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [3, 9, 12]
  "§2.1#r2": 47
  "§2.1#r5": [21, 55]
  "§2.1#r6": [30, 68, 75]
  "§2.1#r7": [22, 59]
  "§2.1#r9": 23
  "§2.1#r10": [27, 82]
  "§2.1#r11": 34
  "§2.1#r12": [5, 6, 7]
  "§4.8#r1": [1, 3]
  "§4.8#r2": 47
  "§4.8#r5": [16, 21]
  "§4.8#r6": [17, 30]
  "§4.8#r8": [23, 27]
  "§4.8#r9": [38, 42, 95, 96, 97, 100]
  "§4.8#r10": 32
  "§4.8#r11": 34
  "§9.11#r1": [7, 9, 12]
  "§9.11#r2": [38, 87]
  "§9.11#b1": [38, 42]
  "§2.1#b7": [38, 42, 95, 96, 97, 100]
  "§4.8#b2": 34
  "§2#b1": 22
  "§2.1#b9": [16, 17, 18, 21]
  "§2.1#p2": [5, 6, 22]
  "§2.1#p7": [9, 12]
  "§2.1#p8": [21, 22]
  "§2.1#p9": [16, 17, 18]
  "§2.1#p10": [7, 18, 23]
  "EB-AKS-5@add-update": 55
  "EB-AKS-5@mark-as-found": [59, 62]
  "EB-AKS-5@confirm": [67, 68]
  "EB-AKS-5@reject": [75, 78]
  "§9.3#b1": [16, 55]
anchor: [15, 26, 37, 41, 86]
coverage:
  web: automated
---

# Gating Manage asset & TAG (Update): hak per Group, record di luar Group hanya Read, Report Disposal tidak tersedia

## Prerequisites
- Aktor: pemegang Manage asset & TAG dengan Update pada Group `Head Office {runId}` (descendant `Finance Room {runId}` dan `Server Room {runId}`) dan Read pada Group `Warehouse {runId}`; capability itu saja (tanpa Create dan Delete, tanpa `View asset value`), bukan Last holder record mana pun, tanpa hak apa pun pada Group `Branch Surabaya {runId}`; lalu pemegang Manage asset & TAG dengan Update pada Group `Head Office {runId}` yang juga memegang `View asset value` pada Group `Head Office {runId}` beserta descendant.
- Layar awal: halaman Assets.
- Data:
  - DU-022-1: Missing record, Name `Laptop Dell Latitude 5420 {runId} - 22`, Asset ID `LPT-0022 {runId}`, Group `Finance Room {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`.
  - DU-022-2: Missing record, Name `Hand Pallet Truck {runId} - 3`, Asset ID `HPT-0003 {runId}`, Group `Warehouse {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`.
  - DU-022-3: Missing record, Name `Laptop Lenovo ThinkPad T14 {runId} - 4`, Asset Name `Laptop Lenovo ThinkPad T14 {runId}`, Asset ID `LPT-0004 {runId}`, Group `Server Room {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`, TAG `—` (aset tanpa TAG).
  - DU-022-4: Missing record, Name `Monitor LG 27UL500 {runId} - 11`, Asset ID `MON-0011 {runId}`, Group `Server Room {runId}`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Sari Dewi {runId}` (pemegang aset tanpa hak Aktor Missing).
  - DU-022-5: Missing record, Name `Camera Canon EOS {runId} - 1`, Asset ID `CAM-0001 {runId}`, Group `Finance Room {runId}`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Budi Santoso {runId}` (pemegang aset tanpa hak Aktor Missing).
  - DU-022-6: Missing record, Name `Projector Epson EB-X06 {runId} - 7`, Asset ID `PRJ-0007 {runId}`, Group `Head Office {runId}`, Status `Reported Disposal`, Source `Stock opname`, Last Holder `—`, dilaporkan oleh pengguna lain.
  - DU-022-7: Missing record, Name `Printer HP LaserJet M404 {runId} - 5`, Asset ID `PRN-0005 {runId}`, Group `Branch Surabaya {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`.
  - DU-022-8: Asset, Name `Scanner Zebra DS2208 {runId} - 2`, Asset ID `SCN-0002 {runId}`, Group `Finance Room {runId}`, Status `Available`, tanpa record Missing berjalan.
  - DU-022-11: Missing record, Name `Printer Canon imageCLASS {runId}`, Group `Finance Room {runId}`, Status `Reported Disposal`, Source `Manual`, Last Holder `—`, dilaporkan oleh aktor ini. Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.

## Test Steps

### Tab Missing dan sub-tab tampil untuk pemegang Update
1. Verifikasi tab `Missing` tampil pada halaman Assets
2. Klik tab `Missing`
3. Verifikasi sub-tab `Active` dan `History` tampil
4. Ketik Search `{runId}`, tekan Enter

### Cakupan per Group: Update, Read, dan tanpa hak
5. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 22` dengan Group `Finance Room {runId}` tampil
6. Verifikasi baris `Hand Pallet Truck {runId} - 3` dengan Group `Warehouse {runId}` tampil
7. Verifikasi baris `Printer HP LaserJet M404 {runId} - 5` dengan Group `Branch Surabaya {runId}` tidak tampil
8. Klik nama `Laptop Dell Latitude 5420 {runId} - 22`
9. Verifikasi dialog `Missing Log` untuk record `Laptop Dell Latitude 5420 {runId} - 22` terbuka
10. Klik `✕` pada dialog Missing Log
11. Klik nama `Hand Pallet Truck {runId} - 3`
12. Verifikasi dialog `Missing Log` untuk record `Hand Pallet Truck {runId} - 3` terbuka
13. Klik `✕` pada dialog Missing Log

### Record Group Read hanya melihat tabel dan Missing Log
14. Klik menu ⋯ pada baris `Hand Pallet Truck {runId} - 3`
15. Verifikasi aksi `Missing Log` tampil
16. Verifikasi aksi `Add Update` tidak tampil
17. Verifikasi aksi `Mark as Found` tidak tampil
18. Verifikasi aksi `Report Disposal` tidak tampil
19. Tekan `Esc`

### Aksi record Group Update tampil dan Report Disposal tidak tersedia
20. Klik menu ⋯ pada baris `Laptop Dell Latitude 5420 {runId} - 22`
21. Verifikasi aksi `Add Update` tampil
22. Verifikasi aksi `Mark as Found` tampil
23. Verifikasi aksi `Report Disposal` tidak tersedia
24. Tekan `Esc`
25. Klik menu ⋯ pada baris `Projector Epson EB-X06 {runId} - 7`
26. Verifikasi aksi `Missing Log` tampil
27. Verifikasi aksi `Cancel Disposal Report` tidak tampil
28. Tekan `Esc`
29. Klik menu ⋯ pada baris `Monitor LG 27UL500 {runId} - 11`
30. Verifikasi aksi `Review` tampil
31. Tekan `Esc`

### Toolbar tab Active: Scan Found Asset dan Download
32. Verifikasi tombol `Scan Found Asset` tampil di toolbar tab Active
33. Klik `Download`
34. Verifikasi opsi `Download as CSV` dan `Download as XLSX` tampil
35. Tekan `Esc`

### Kolom nilai finansial tidak tersedia tanpa hak View asset value
36. Klik tombol `Column Visibility` pada header tabel
37. Verifikasi kolom `Brand` tersedia pada daftar Column Visibility
38. Verifikasi daftar Column Visibility tidak memuat `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
39. Tekan `Esc`
40. Klik `Filter`
41. Verifikasi field `Brand` tampil di Filter Panel
42. Verifikasi Filter Panel tidak memuat field `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
43. Klik `Filter`

### Report Missing tersedia dari daftar aset
44. Klik tab `Assets`
45. Ketik Search `{runId}`, tekan Enter
46. Klik menu ⋯ pada baris `Scanner Zebra DS2208 {runId} - 2`
47. Verifikasi aksi `Report Missing` tampil
48. Tekan `Esc`
49. Klik tab `Missing`
50. Ketik Search `{runId}`, tekan Enter

### Add Update oleh pemegang Update tersimpan
51. Klik menu ⋯ pada baris `Laptop Dell Latitude 5420 {runId} - 22`
52. Klik `Add Update`
53. Isi Update `Terakhir terlihat di ruang rapat lantai dua {runId}`
54. Klik `[Add Update]`
55. Verifikasi toast `Success, update has been added.` tampil

### Mark as Found oleh pemegang Update tersimpan
56. Klik menu ⋯ pada baris `Laptop Lenovo ThinkPad T14 {runId} - 4`
57. Klik `Mark as Found`
58. Klik `[Mark as Found]`
59. Verifikasi toast `Success, [Asset Name] is available again.` tampil dengan Asset Name `Laptop Lenovo ThinkPad T14 {runId}`
60. Klik sub-tab `History`
61. Ketik Search `{runId}`, tekan Enter
62. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId} - 4` dengan Status `Found` tampil
63. Klik sub-tab `Active`

### Confirm laporan pemegang oleh pemegang Update
64. Klik menu ⋯ pada baris `Monitor LG 27UL500 {runId} - 11`
65. Klik `Review`
66. Klik `[Confirm]`
67. Verifikasi toast `Success, report has been confirmed.` tampil
68. Verifikasi node `Report confirmed by` tampil di dialog Missing Log
69. Klik `✕` pada dialog Missing Log

### Reject laporan pemegang oleh pemegang Update
70. Klik menu ⋯ pada baris `Camera Canon EOS {runId} - 1`
71. Klik `Review`
72. Klik `[Reject]`
73. Isi Reason `Barang ternyata masih dipakai di gudang cabang {runId}`
74. Klik `[Reject]`
75. Verifikasi toast `Success, report has been rejected.` tampil
76. Klik sub-tab `History`
77. Ketik Search `{runId}`, tekan Enter
78. Verifikasi baris `Camera Canon EOS {runId} - 1` dengan Status `Rejected` tampil

### Cancel Disposal Report tersedia untuk laporan miliknya
79. Klik sub-tab `Active`
80. Ketik Search `{runId}`, tekan Enter
81. Klik menu ⋯ pada baris `Printer Canon imageCLASS {runId}`
82. Verifikasi aksi `Cancel Disposal Report` tampil
83. Tekan `Esc`

### Manage asset & TAG (Update): kolom nilai finansial tab History tidak tersedia
84. Klik sub-tab `History`
85. Klik tombol `Column Visibility` pada header tabel
86. Verifikasi kolom `Brand` tersedia pada daftar Column Visibility
87. Verifikasi daftar Column Visibility tidak memuat `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
88. Tekan `Esc`

### Manage asset & TAG (Update) yang juga memegang View asset value: kolom nilai finansial tersedia
89. Masuk sebagai pemegang Manage asset & TAG dengan Update pada Group `Head Office {runId}` yang juga memegang `View asset value` pada Group `Head Office {runId}`
90. Klik tab `Missing`
91. Klik tombol `Column Visibility` pada header tabel
92. Centang `Purchase Cost`
93. Centang `Asset Value (Commercial)`
94. Centang `Asset Value (Fiscal)`
95. Verifikasi header kolom `Purchase Cost` tampil di tabel
96. Verifikasi header kolom `Asset Value (Commercial)` tampil di tabel
97. Verifikasi header kolom `Asset Value (Fiscal)` tampil di tabel
98. Tekan `Esc`
99. Klik `Filter`
100. Verifikasi Filter Panel memuat field `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
101. Klik `Filter`

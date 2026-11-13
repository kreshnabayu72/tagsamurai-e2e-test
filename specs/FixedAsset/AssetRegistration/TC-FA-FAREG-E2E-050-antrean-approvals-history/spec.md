---
id: TC-FA-FAREG-E2E-050-antrean-approvals-history
title: "Antrean Approvals tab History: isi, Search, Filter, dan navigasi Detail"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#r135", "§4.1#r136", "§4.1#r137", "§4.1#r138", "§4.1#r139", "§4.1#r140", "§4.1#r141", "§4.1#p39", "§4.2.5#p4", "§4.2.5#b2", "§4.2.5#b3", "§5#r3", "§5#r4", "§9.5#r6", "EB-SRC-5@antrean-approvals-history"]
smoke: []
dependsOn: []
trace:
  "§4.1#r136": [2, 17, 37, 40, 73]
  "§4.2.5#b2": [2, 13, 97, 102]
  "§4.1#r135": [3, 15, 37, 71, 102]
  "§4.1#r137": [4, 19, 37, 46, 75]
  "§4.1#r138": [5, 6, 7, 8, 21, 29, 33, 37, 51, 77]
  "§4.1#r139": [9, 23, 25, 37, 56, 79]
  "§4.1#r140": [10, 11, 25, 37, 62, 81]
  "§4.1#r141": [12, 13, 27, 37, 67, 83]
  "§5#r4": [13]
  "§9.5#r6": [13]
  "§5#r3": [15]
  "§4.2.5#b3": [37, 40, 46, 51, 56, 62, 67]
  "EB-SRC-5@antrean-approvals-history": [85, 89, 92]
  "§4.1#p39": [94, 95, 97]
  "§4.2.5#p4": [99, 104]
coverage:
  web: automated
---

# Antrean Approvals tab History: isi, Search, Filter, dan navigasi Detail

## Prerequisites
- Aktor: Total Control `Dian P`, seluruh client.
- Layar awal: Approvals > Registration > History.
- Data:
  - DU-050-1: Pengajuan History dengan Registration ID yang dibentuk server saat Submit, Group `Gudang Meranti {runId}`, Total Asset `8`, Status `Approved` karena pengaju adalah Total Control sehingga disetujui otomatis tanpa approver independen, Requested By `Eko T.`, Approver `Eko T.`, Last Updated `T0 − 1 hari`.
  - DU-050-2: Pengajuan History dengan Registration ID yang dibentuk server saat Submit, Group `Gudang Ulin {runId}`, Total Asset `14`, Status `Partially Approved`, Requested By `Hadi K.`, Approver `Maya L.`, Last Updated `T0 − 2 hari`.
  - DU-050-3: Pengajuan History dengan Registration ID yang dibentuk server saat Submit, Group `Gudang Bangkirai {runId}`, Total Asset `3`, Status `Rejected`, Requested By `Siti N.`, Approver `Rina W.`, Last Updated `T0 − 3 hari`.
  - DU-050-4: Pengajuan History dengan Registration ID yang dibentuk server saat Submit, Group `Gudang Damar {runId}`, Total Asset `97`, Status `Canceled`, Requested By `Rina W.`, Approver `—`, Last Updated `T0 − 4 hari`.
  - Pengajuan DU-050-4 diajukan lebih dulu daripada DU-050-3, DU-050-3 lebih dulu daripada DU-050-2, dan DU-050-2 lebih dulu daripada DU-050-1.
  - Eko T adalah pengguna aktif dengan role Total Control. Maya L, Hadi K, Siti N, dan Rina W adalah pengguna aktif dengan role Manage asset & TAG pada Group pengajuan masing-masing; Maya L dan Hadi K bukan Total Control.
- Kondisi: format tanggal General Settings `dd/MM/yy` dan format waktu 24 jam; seluruh kolom tabel tab History tampil.

## Test Steps

### Nilai sel tab History
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi tabel tab History memuat baris `Gudang Meranti {runId}`, `Gudang Ulin {runId}`, `Gudang Bangkirai {runId}`, `Gudang Damar {runId}` dengan Group tampil sebagai Badge
3. Verifikasi Registration ID baris `Gudang Meranti {runId}` berformat `REG-YYYYMMDD-NNNNN` dan sama dengan Registration ID milik DU-050-1
4. Verifikasi Total Asset baris `Gudang Meranti {runId}` bernilai `8`
5. Verifikasi Status baris `Gudang Meranti {runId}` tampil sebagai Badge `Approved` berwarna success
6. Verifikasi Status baris `Gudang Ulin {runId}` tampil sebagai Badge `Partially Approved` berwarna warning
7. Verifikasi Status baris `Gudang Bangkirai {runId}` tampil sebagai Badge `Rejected` berwarna danger
8. Verifikasi Status baris `Gudang Damar {runId}` tampil sebagai Badge `Canceled` berwarna dark
9. Verifikasi Requested By baris `Gudang Meranti {runId}` bernilai `Eko T.`[^drift-1]
10. Verifikasi Approver baris `Gudang Meranti {runId}` bernilai `Eko T.`, nama pengaju, karena pengajuan disetujui otomatis (Kondisi A)[^drift-1]
11. Verifikasi Approver baris `Gudang Damar {runId}` bernilai `—`
12. Verifikasi Last Updated baris `Gudang Meranti {runId}` tampil dengan Date Format `dd/MM/yy` diikuti Time Format 24 jam

### Urutan awal Last Updated terbaru di atas
13. Verifikasi baris `Gudang Meranti {runId}` tampil di atas baris `Gudang Ulin {runId}`, baris `Gudang Ulin {runId}` di atas baris `Gudang Bangkirai {runId}`, dan baris `Gudang Bangkirai {runId}` di atas baris `Gudang Damar {runId}` (Last Updated terbaru di atas)

### Search pada kolom Searchable
14. Ganti isi kotak search dengan Registration ID milik DU-050-2, tekan Enter
15. Verifikasi tabel tab History memuat baris `Gudang Ulin {runId}` dan tidak memuat baris `Gudang Meranti {runId}`
16. Ganti isi kotak search dengan `Gudang Bangkirai {runId}`, tekan Enter
17. Verifikasi tabel tab History memuat baris `Gudang Bangkirai {runId}` dan tidak memuat baris `Gudang Meranti {runId}`
18. Ganti isi kotak search dengan `97`, tekan Enter
19. Verifikasi tabel tab History memuat baris `Gudang Damar {runId}`
20. Ganti isi kotak search dengan `Rejected`, tekan Enter
21. Verifikasi tabel tab History memuat baris `Gudang Bangkirai {runId}` dan tidak memuat baris `Gudang Meranti {runId}`
22. Ganti isi kotak search dengan `Siti N`, tekan Enter
23. Verifikasi tabel tab History memuat baris `Gudang Bangkirai {runId}` dan tidak memuat baris `Gudang Meranti {runId}`
24. Ganti isi kotak search dengan `Rina W`, tekan Enter
25. Verifikasi tabel tab History memuat baris `Gudang Bangkirai {runId}`, `Gudang Damar {runId}` dan tidak memuat baris `Gudang Meranti {runId}`
26. Ganti isi kotak search dengan tanggal Last Updated baris `Gudang Ulin {runId}` dalam Date Format `dd/MM/yy`, dari `T0 − 2 hari`, tekan Enter
27. Verifikasi baris `Gudang Ulin {runId}` tidak tampil karena kolom Last Updated tidak dicari

### Search Status mencocokkan substring nilai lain
28. Ganti isi kotak search dengan `Approved`, tekan Enter
29. Verifikasi tabel tab History memuat baris `Gudang Meranti {runId}`, `Gudang Ulin {runId}` dan tidak memuat baris `Gudang Bangkirai {runId}`, `Gudang Damar {runId}`
30. Klik ikon Filter
31. Pilih opsi `Approved` pada field `Status`
32. Klik `[Apply]`
33. Verifikasi tabel tab History memuat baris `Gudang Meranti {runId}` dan tidak memuat baris `Gudang Ulin {runId}`
34. Klik `[Clear Field]`
35. Klik `[Apply]`

### Filter pada kolom Filterable
36. Ganti isi kotak search dengan `{runId}`, tekan Enter
37. Verifikasi panel Filter tab History memuat field `Group`, `Total Asset`, `Status`, `Requested By`, `Approver`, dan `Last Updated` dan tidak memuat field `Registration ID`
38. Pilih opsi Group `Gudang Ulin {runId}` pada field `Group`
39. Klik `[Apply]`
40. Verifikasi tabel tab History memuat baris `Gudang Ulin {runId}` dan tidak memuat baris `Gudang Meranti {runId}`
41. Klik `[Clear Field]`
42. Klik `[Apply]`
43. Isi Min `8` pada field `Total Asset`
44. Isi Max `14` pada field `Total Asset`
45. Klik `[Apply]`
46. Verifikasi tabel tab History memuat baris `Gudang Meranti {runId}`, `Gudang Ulin {runId}` dan tidak memuat baris `Gudang Bangkirai {runId}`, `Gudang Damar {runId}`
47. Klik `[Clear Field]`
48. Klik `[Apply]`
49. Pilih opsi `Rejected` pada field `Status`
50. Klik `[Apply]`
51. Verifikasi tabel tab History memuat baris `Gudang Bangkirai {runId}` dan tidak memuat baris `Gudang Meranti {runId}`
52. Klik `[Clear Field]`
53. Klik `[Apply]`
54. Pilih opsi `Eko T.` pada field `Requested By`[^drift-1]
55. Klik `[Apply]`
56. Verifikasi tabel tab History memuat baris `Gudang Meranti {runId}` dan tidak memuat baris `Gudang Ulin {runId}`
57. Klik `[Clear Field]`
58. Klik `[Apply]`
59. Pilih opsi `Eko T.` pada field `Approver`[^drift-1]
60. Pilih opsi `Maya L.` pada field `Approver`[^drift-1]
61. Klik `[Apply]`
62. Verifikasi tabel tab History memuat baris `Gudang Meranti {runId}`, `Gudang Ulin {runId}` dan tidak memuat baris `Gudang Bangkirai {runId}`, `Gudang Damar {runId}`
63. Klik `[Clear Field]`
64. Klik `[Apply]`
65. Pilih rentang tanggal `T0 − 3 hari` sampai `T0 − 2 hari` pada field `Last Updated`
66. Klik `[Apply]`
67. Verifikasi tabel tab History memuat baris `Gudang Ulin {runId}`, `Gudang Bangkirai {runId}` dan tidak memuat baris `Gudang Meranti {runId}`, `Gudang Damar {runId}`
68. Klik `[Clear Field]`
69. Klik `[Apply]`

### Sort pada kolom Sortable
70. Klik ikon sort pada header kolom `Registration ID`
71. Verifikasi urutan baris kolom `Registration ID` naik: `Gudang Damar {runId}`, `Gudang Bangkirai {runId}`, `Gudang Ulin {runId}`, `Gudang Meranti {runId}`
72. Klik ikon sort pada header kolom `Group`
73. Verifikasi urutan baris kolom `Group` naik: `Gudang Bangkirai {runId}`, `Gudang Damar {runId}`, `Gudang Meranti {runId}`, `Gudang Ulin {runId}`
74. Klik ikon sort pada header kolom `Total Asset`
75. Verifikasi urutan baris kolom `Total Asset` naik: `Gudang Bangkirai {runId}`, `Gudang Meranti {runId}`, `Gudang Ulin {runId}`, `Gudang Damar {runId}`
76. Klik ikon sort pada header kolom `Status`
77. Verifikasi urutan baris kolom `Status` naik: `Gudang Meranti {runId}`, `Gudang Damar {runId}`, `Gudang Ulin {runId}`, `Gudang Bangkirai {runId}`
78. Klik ikon sort pada header kolom `Requested By`
79. Verifikasi urutan baris kolom `Requested By` naik: `Gudang Meranti {runId}`, `Gudang Ulin {runId}`, `Gudang Damar {runId}`, `Gudang Bangkirai {runId}`
80. Klik ikon sort pada header kolom `Approver`
81. Verifikasi urutan relatif baris dengan Approver terisi pada kolom `Approver` naik: `Gudang Meranti {runId}`, `Gudang Ulin {runId}`, `Gudang Bangkirai {runId}`
82. Klik ikon sort pada header kolom `Last Updated`
83. Verifikasi urutan baris kolom `Last Updated` naik (Oldest First): `Gudang Damar {runId}`, `Gudang Bangkirai {runId}`, `Gudang Ulin {runId}`, `Gudang Meranti {runId}`

### Kolom Status yang disembunyikan tidak dicari
84. Ganti isi kotak search dengan `Rejected`, tekan Enter
85. Verifikasi tabel tab History memuat baris `Gudang Bangkirai {runId}`
86. Klik header kolom Actions `⋯`
87. Hilangkan centang `Status` pada panel Column Visibility
88. Ganti isi kotak search dengan `Rejected`, tekan Enter
89. Verifikasi baris `Gudang Bangkirai {runId}` tidak tampil di tabel tab History
90. Centang kembali `Status` pada panel Column Visibility
91. Ganti isi kotak search dengan `Rejected`, tekan Enter
92. Verifikasi tabel tab History memuat baris `Gudang Bangkirai {runId}`

### Aksi Detail dan navigasi kembali ke tab asal
93. Ganti isi kotak search dengan `{runId}`, tekan Enter
94. Verifikasi kolom `Actions` adalah kolom terakhir tabel tab History, sesudah kolom `Last Updated`
95. Verifikasi baris `Gudang Meranti {runId}` menampilkan ikon aksi `Detail`
96. Klik ikon `Detail` pada baris `Gudang Meranti {runId}`
97. Verifikasi Detail pengajuan read-only terbuka dengan breadcrumb `Approvals > Registration > History > Detail` dan Registration ID milik DU-050-1
98. Klik tombol Back browser
99. Verifikasi antrean Approvals terbuka kembali pada tab `History` dengan breadcrumb `Approvals > Registration > History`
100. Ganti isi kotak search dengan `{runId}`, tekan Enter
101. Klik Registration ID milik DU-050-2
102. Verifikasi Detail pengajuan read-only terbuka dengan Registration ID milik DU-050-2
103. Klik tautan breadcrumb `History`
104. Verifikasi antrean Approvals terbuka kembali pada tab `History`

[^drift-1]: Drift PRD vs foundation vs override. PRD §4.1 kolom Requested By dan Approver: `Nama singkat`. foundation `prd-conventions.md` §9.13: nama singkat `[First Name] [Last Initial]`, contoh tanpa titik (`John L`, `Alexander G`). Override O-4: nama singkat mengakhiri inisial dengan titik (`John L.`, `Alexander G.`). Diasersi: O-4, karena override menang atas foundation (SB-6).

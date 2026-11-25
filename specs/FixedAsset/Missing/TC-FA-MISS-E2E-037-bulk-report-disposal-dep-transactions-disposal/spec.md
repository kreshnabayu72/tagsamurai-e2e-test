---
id: TC-FA-MISS-E2E-037-bulk-report-disposal-dep-transactions-disposal
title: "Bulk Report Disposal: satu Group diproses dengan satu Reason, record dilewati dengan toast skipped, lintas Group dan semua dilewati diblok"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1a#p8", "§4.1a#p9", "§4.1a#p2", "§4.4#r12", "§6#r11", "§6#r12", "§6#r13", "§7.2#r5", "§7.2#r10", "§7.2#r11", "§7.3#r4", "§7.3#r13", "§4.2.4#p10", "§9.2#b17", "§9.4.2#r21", "§9.4.4#r4", "§9.6#r10", "§8#r6", "§4.1#r9", "§9.4.1#r9", "§5#r5", "§2.1#r12", "EB-BLK-2@tabel-active", "EB-BLK-3", "EB-FB-1@bulk-report-disposal", "EB-EDG-2", "§8.1#r15"]
smoke: []
dependsOn: ["Transactions Disposal: dialog Report Disposal D-DISP-13", "Transactions Disposal: tab Reported"]
trace:
  "§4.1a#p8": [8, 10]
  "§4.1a#p9": [44, 56]
  "§4.1a#p2": [3, 81]
  "§4.4#r12": [56, 69]
  "§6#r11": [69, 71]
  "§6#r12": [44, 45, 46, 47]
  "§6#r13": [56, 58]
  "§7.2#r5": [56, 69]
  "§7.2#r10": [69, 116]
  "§7.2#r11": [56]
  "§7.3#r4": [56, 69]
  "§7.3#r13": [13, 44]
  "§4.2.4#p10": [56, 69]
  "§9.2#b17": [8, 69]
  "§9.4.2#r21": [69, 116]
  "§9.4.4#r4": [69]
  "§9.6#r10": [13, 33, 44]
  "§8#r6": [18, 21, 24, 50]
  "§4.1#r9": [56, 69]
  "§9.4.1#r9": [14, 15, 16, 69]
  "§5#r5": [3, 81]
  "§2.1#r12": [63, 64]
  "EB-BLK-2@tabel-active": [73, 75, 77, 86, 87, 89, 92]
  "EB-BLK-3": [60, 56, 100, 102, 106]
  "EB-FB-1@bulk-report-disposal": [13]
  "EB-EDG-2": [30, 34]
  "§8.1#r15": [18, 21, 24]
anchor: [49, 80, 91, 115]
coverage:
  web: automated
---

# Bulk Report Disposal: satu Group diproses dengan satu Reason, record dilewati dengan toast skipped, lintas Group dan semua dilewati diblok

## Prerequisites
- Aktor: Total Control `Rina W`, yang juga Aktor Disposal.
- Layar awal: Assets > Missing > Active.
- Data:
  - DU-037-1: Asset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, dengan record Missing berstatus `Missing`.
  - DU-037-2: Asset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, dengan record Missing berstatus `Missing`.
  - DU-037-3: Asset `Monitor LG 27UL500 {runId}`, Group `Head Office`, dengan record Missing berstatus `Missing`.
  - DU-037-4: Asset `Projector Epson EB-X06 {runId}`, Group `Head Office`, dengan record Missing berstatus `Missing`.
  - DU-037-5: Asset `Hand Pallet Truck {runId}`, Group `Head Office`, dengan record Missing berstatus `Missing`.
  - DU-037-6: Asset `Scanner Zebra DS2208 {runId}`, Group `Head Office`, dengan record Missing berstatus `Missing`.
  - DU-037-7: Asset `Camera Canon EOS {runId}`, Group `Head Office`, dengan record Missing berstatus `Reported Disposal`.
  - DU-037-8: Asset `Toyota Innova {runId}`, Group `Head Office`, dengan record Missing berstatus `Missing` dan Last holder `Rina W`.
  - DU-037-9: Asset `Drill Bosch GSB {runId}`, Group `Warehouse`, dengan record Missing berstatus `Missing`.
  - DU-037-10: Asset `Server Dell PowerEdge {runId}`, Group `Head Office`, dengan record Missing berstatus `Missing`.
  - DU-037-11: Pengguna `Rina W`, Total Control.
  - DU-037-12: Reason `Aset dilaporkan hilang bersamaan dari satu lokasi`.
  - DU-037-13: Reason `Proyektor tidak ditemukan setelah acara kantor`.
  - DU-037-14: Reason `Aset dari beberapa lokasi dilaporkan untuk disposal`.
  - DU-037-15: 2 Asset `Kursi Kantor {n} {runId}`, Group `Head Office`, dengan record Missing berstatus `Missing`, sehingga seluruh Asset Active milik run ini lebih banyak daripada satu halaman berukuran `10`.
  - DU-037-16: Asset `Bor Listrik Makita {runId}`, Group `Head Office`, dengan record Missing berstatus `Missing`.
  - DU-037-17: Reason `Aset tidak ditemukan setelah audit gudang`.
- Kondisi:
  - Akun `Rina W` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Bulk Report Disposal atas banyak record satu Group diproses dengan satu Reason
1. Ketik Search `{runId}`, tekan Enter
2. Atur jumlah baris per halaman menjadi `100`
3. Verifikasi kolom Checkbox tampil pada tabel sub-tab Active
4. Centang baris `Laptop Dell Latitude 5420 {runId}`
5. Centang baris `Printer HP LaserJet M404 {runId}`
6. Centang baris `Monitor LG 27UL500 {runId}`
7. Klik `Bulk Action` pada bar aksi bulk
8. Verifikasi aksi `Report Disposal` tampil pada overlay Bulk Action
9. Klik `Report Disposal`
10. Verifikasi dialog `Report Disposal` memuat satu isian `Reason` untuk seluruh aset terpilih
11. Isi Reason `Aset dilaporkan hilang bersamaan dari satu lokasi`
12. Kirim dialog Report Disposal
13. Verifikasi toast `Success, disposal report has been created.` tampil
14. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` berstatus `Reported Disposal`
15. Verifikasi baris `Printer HP LaserJet M404 {runId}` berstatus `Reported Disposal`
16. Verifikasi baris `Monitor LG 27UL500 {runId}` berstatus `Reported Disposal`
17. Klik `Laptop Dell Latitude 5420 {runId}` pada kolom Name
18. Verifikasi dialog Missing Log memuat node `Disposal reported by` oleh `Rina W` dengan Reason `Aset dilaporkan hilang bersamaan dari satu lokasi`
19. Tutup dialog Missing Log dengan `✕`
20. Klik `Printer HP LaserJet M404 {runId}` pada kolom Name
21. Verifikasi dialog Missing Log memuat node `Disposal reported by` oleh `Rina W` dengan Reason `Aset dilaporkan hilang bersamaan dari satu lokasi`
22. Tutup dialog Missing Log dengan `✕`
23. Klik `Monitor LG 27UL500 {runId}` pada kolom Name
24. Verifikasi dialog Missing Log memuat node `Disposal reported by` oleh `Rina W` dengan Reason `Aset dilaporkan hilang bersamaan dari satu lokasi`
25. Tutup dialog Missing Log dengan `✕`

### Bulk dengan satu item memakai bentuk tunggal
26. Ganti isi kotak search dengan `Projector Epson EB-X06 {runId}`, tekan Enter
27. Centang baris `Projector Epson EB-X06 {runId}`
28. Klik `Bulk Action` pada bar aksi bulk
29. Klik `Report Disposal`
30. Verifikasi dialog `Report Disposal` memuat satu aset `Projector Epson EB-X06 {runId}`
31. Isi Reason `Proyektor tidak ditemukan setelah acara kantor`
32. Kirim dialog Report Disposal
33. Verifikasi toast `Success, disposal report has been created.` tampil
34. Verifikasi baris `Projector Epson EB-X06 {runId}` berstatus `Reported Disposal`

### Sebagian record dilewati dengan toast skipped
35. Ganti isi kotak search dengan `{runId}`, tekan Enter
36. Centang baris `Hand Pallet Truck {runId}`
37. Centang baris `Scanner Zebra DS2208 {runId}`
38. Centang baris `Camera Canon EOS {runId}`
39. Centang baris `Toyota Innova {runId}`
40. Klik `Bulk Action` pada bar aksi bulk
41. Klik `Report Disposal`
42. Isi Reason `Aset dari beberapa lokasi dilaporkan untuk disposal`
43. Kirim dialog Report Disposal
44. Verifikasi toast `Success, disposal report has been created. Some items were skipped.` tampil
45. Verifikasi baris `Hand Pallet Truck {runId}` berstatus `Reported Disposal`
46. Verifikasi baris `Scanner Zebra DS2208 {runId}` berstatus `Reported Disposal`
47. Verifikasi baris `Toyota Innova {runId}` tetap berstatus `Missing`
48. Klik `Toyota Innova {runId}` pada kolom Name
49. Verifikasi dialog Missing Log memuat node `Reported missing by`
50. Verifikasi dialog Missing Log tidak memuat node `Disposal reported by`
51. Tutup dialog Missing Log dengan `✕`

### Semua record terpilih dilewati diblok tanpa toast sukses
52. Centang baris `Camera Canon EOS {runId}`
53. Centang baris `Toyota Innova {runId}`
54. Klik `Bulk Action` pada bar aksi bulk
55. Klik `Report Disposal`
56. Verifikasi dialog `Cannot Report Disposal` memuat pesan `None of the selected records can be reported for disposal.`
57. Klik `[OK]` pada dialog
58. Verifikasi baris `Toyota Innova {runId}` tetap tercentang
59. Buka menu `⋯` pada baris `Toyota Innova {runId}`
60. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada aksi `Report Disposal` yang disabled
61. Tutup menu `⋯` dengan tombol Esc

### Seleksi lintas Group diblok
62. Klik `×` pada bar aksi bulk
63. Verifikasi baris `Drill Bosch GSB {runId}` dengan Group `Warehouse` tampil
64. Verifikasi baris `Server Dell PowerEdge {runId}` dengan Group `Head Office` tampil
65. Centang baris `Drill Bosch GSB {runId}`
66. Centang baris `Server Dell PowerEdge {runId}`
67. Klik `Bulk Action` pada bar aksi bulk
68. Klik `Report Disposal`
69. Verifikasi dialog `Cannot Report Disposal` memuat pesan `Selected assets come from more than one group. Select assets from one group.`
70. Klik `[OK]` pada dialog
71. Verifikasi baris `Drill Bosch GSB {runId}` tetap berstatus `Missing`

### Select All dan Unselect All pada tabel Active
72. Hilangkan centang baris `Server Dell PowerEdge {runId}`
73. Verifikasi tombol `Select All ([N] records)` memuat N yang sama dengan jumlah total pada info pagination
74. Klik tombol `Select All ([N] records)`
75. Verifikasi tombol berubah menjadi `Unselect All`
76. Hilangkan centang baris `Drill Bosch GSB {runId}`
77. Verifikasi tombol kembali menjadi `Select All ([N] records)` dengan N yang sama
78. Klik `×` pada bar aksi bulk

### Sub-tab History tanpa bulk
79. Klik sub-tab `History`
80. Verifikasi kolom Actions tampil pada tabel sub-tab History
81. Verifikasi kolom Checkbox tidak tampil pada tabel sub-tab History

### Select All memilih lintas halaman
82. Klik sub-tab `Active`
83. Ketik Search `{runId}`, tekan Enter
84. Atur jumlah baris per halaman menjadi `10`
85. Centang checkbox header
86. Verifikasi tombol `Select All ([N] records)` memuat N yang sama dengan jumlah total pada info pagination
87. Verifikasi jumlah total pada info pagination lebih besar daripada jumlah baris yang tampil pada satu halaman
88. Klik tombol `Select All ([N] records)`
89. Verifikasi tombol berubah menjadi `Unselect All`
90. Klik halaman `2` pada kontrol Pagination
91. Verifikasi halaman `2` memuat baris data
92. Verifikasi setiap baris pada halaman `2` tercentang
93. Klik `×` pada bar aksi bulk

### Klik ganda konfirmasi Report Disposal memproses record sekali
94. Ganti isi kotak search dengan `Bor Listrik Makita {runId}`, tekan Enter
95. Centang baris `Bor Listrik Makita {runId}`
96. Klik `Bulk Action` pada bar aksi bulk
97. Klik `Report Disposal`
98. Isi Reason `Aset tidak ditemukan setelah audit gudang`
99. Kirim dialog Report Disposal dengan klik ganda
100. Verifikasi toast `Success, disposal report has been created.` tampil hanya satu
101. Klik `Bor Listrik Makita {runId}` pada kolom Name
102. Verifikasi dialog Missing Log memuat tepat satu node `Disposal reported by` oleh `Rina W`
103. Tutup dialog Missing Log dengan `✕`
104. Buka tab `Reported` pada `Transactions > Disposal`
105. Ketik Search `Bor Listrik Makita {runId}`, tekan Enter
106. Verifikasi hasil Search `Bor Listrik Makita {runId}` hanya satu baris

### Seleksi lintas Group tidak membuka dialog Report Disposal
107. Buka halaman `Assets`
108. Klik tab `Missing`
109. Ketik Search `{runId}`, tekan Enter
110. Atur jumlah baris per halaman menjadi `100`
111. Centang baris `Drill Bosch GSB {runId}`
112. Centang baris `Server Dell PowerEdge {runId}`
113. Klik `Bulk Action` pada bar aksi bulk
114. Klik `Report Disposal`
115. Verifikasi dialog `Cannot Report Disposal` tampil
116. Verifikasi dialog `Report Disposal` dengan isian `Reason` tidak tampil
117. Klik `[OK]` pada dialog
118. Klik `×` pada bar aksi bulk

---
id: TC-FA-MISS-E2E-012-dialog-missing-log
title: "Dialog Missing Log: pintu masuk, argumen dialog, dan isi node per jenis peristiwa dari data awal"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2.2#p1", "§8.1#p1", "§8.1#r1", "§8.1#r2", "§8.1#r3", "§8.1#r4", "§8.1#r5", "§8.1#r6", "§8.1#r7", "§8.1#r8", "§8.1#r9", "§8.1#r10", "§8.1#r11", "§8.1#r12", "§8.1#r13", "§8.1#r14", "§8.1#r15", "§8.1#r16", "§8.1#r17", "§8.1#r18", "§8.1#p2", "§8#r1", "§8#r2", "§8#r3", "§8#r5", "§8#r7", "§8#r8", "§8#r9", "§8#r10", "§8#r11", "§8#p2", "§8.2#b3", "§5#r7", "§4.1#r4", "§4.1a#r29", "§4.4#r10", "§1.2#r11", "§1.2#r107", "§1.2#r108", "§7.1#r3", "§9.6#r6", "§9.7#r6", "§9.7#r9", "§9.2#b22", "§4.6#b5", "§9.1#r3"]
smoke: []
dependsOn: []
trace:
  "§4.2.2#p1": [24, 25, 26, 30, 33, 36, 112, 119, 121, 126, 129, 134, 135, 140, 141]
  "§8.1#p1": [29, 35, 36, 42, 64, 112, 113, 121, 122, 129, 130, 135, 136, 141, 142]
  "§8.1#r1": 4
  "§8.1#r2": 6
  "§8.1#r3": [43, 45, 47, 48, 82, 84, 86, 88, 89, 93, 95, 99]
  "§8.1#r4": [7, 8, 37, 38]
  "§8.1#r5": [9, 10, 35, 49, 50]
  "§8.1#r6": [11, 36, 42, 113, 122, 130, 136, 142]
  "§8.1#r7": [12, 39]
  "§8.1#r8": 72
  "§8.1#r9": [69, 75, 104]
  "§8.1#r10": 13
  "§8.1#r11": [14, 15, 16]
  "§8.1#r12": [17, 18]
  "§8.1#r13": 19
  "§8.1#r14": [76, 77, 78, 79, 105]
  "§8.1#r15": [51, 55, 65]
  "§8.1#r16": [52, 53, 54]
  "§8.1#r17": [56, 57, 58]
  "§8.1#r18": 66
  "§8.1#p2": [17, 19, 54, 58, 104, 105]
  "§8#r1": 5
  "§8#r2": 5
  "§8#r3": [12, 13, 14, 17, 19]
  "§8#r5": [14, 16, 17, 19]
  "§8#r7": [5, 27]
  "§8#r8": [14, 16]
  "§8#r9": 19
  "§8#r10": 17
  "§8#r11": [51, 52, 55, 56, 66]
  "§8#p2": 5
  "§8.2#b3": 27
  "§5#r7": 27
  "§4.1#r4": 5
  "§4.1a#r29": [23, 29]
  "§4.4#r10": 4
  "§1.2#r11": 6
  "§1.2#r107": [14, 16]
  "§1.2#r108": 21
  "§7.1#r3": [12, 39]
  "§9.6#r6": [14, 15]
  "§9.7#r6": [14, 21]
  "§9.7#r9": 13
  "§9.2#b22": [12, 13, 14, 17, 19]
  "§4.6#b5": 4
  "§9.1#r3": 5
anchor: [2]
coverage:
  web: automated
---

# Dialog Missing Log: pintu masuk, argumen dialog, dan isi node per jenis peristiwa dari data awal

## Prerequisites
- Aktor: Rina W, Total Control, tidak menjadi Last Holder satu pun record di bawah.
- Layar awal: halaman Missing, sub-tab Active.
- Data:
  - DU-012-1: Record Missing `Laptop Lenovo ThinkPad T14 {runId}`, Group `Head Office`, Status `Missing`, Source `Manual`, Last Holder `Dewi A`, Reported By `Rina W`, Reported Date `T0 − 30 hari, pukul 09:00`, Days Missing `30 days`. Asset ID dibentuk server dan menjadi milik entri ini. Node: `Reported missing by Rina W` dengan What happened `Laptop tidak ada di meja kerja setelah rapat bulanan`; `Update added by Rina W` dengan Update `Sudah dicek ke ruang arsip lantai 2, belum ditemukan`; `Detected by scan` dari reader dengan Last seen `T0 − 6 hari, pukul 11:10` dan pemindai `Gate A reader`, Count `3`; `Detected by scan` dari pengguna dengan Last seen `T0 − 2 hari, pukul 15:25` dan pemindai `Agus P`, Count `1`; `Reported found by Agus P` dengan Location `—` dan satu Photo terlampir; `Long missing` oleh `System` dengan Days missing `30`.
  - DU-012-2: Record Waiting for Confirmation `Hand Pallet Truck {runId}`, Asset ID `HPT-012-0002`, Group `Warehouse`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Joko S`, Reported By `Rudi H (on behalf of Joko S)`, Reported Date `T0 − 1 hari, pukul 07:15`, Days Missing `1 day`. Node: `Reported missing by Rudi H on behalf of Joko S` dengan What happened `Hand pallet truck tidak kembali dari area bongkar muat`.
  - DU-012-3: Record Missing `Projector Epson EB-X06 {runId}`, Asset ID `PRJ-012-0003`, Group `Branch Surabaya`, Status `Missing`, Source `Manual`, Last Holder `—`, Reported By `Agus P`, Reported Date `T0 − 10 hari, pukul 08:00`, Days Missing `10 days`. Node: `Disposal reported by Agus P` (laporan Disposal pertama, Report ID milik laporan pertama DU-012-3) dengan Reason `Aset belum ditemukan sesudah pencarian di seluruh kantor`; `Disposal report declined by Rina W` (laporan pertama) dengan Reason `Pencarian di gudang cabang masih berlangsung` dan Back to Missing `Yes`; `Disposal reported by Agus P` (laporan Disposal kedua, Report ID milik laporan kedua DU-012-3) dengan Reason `Pencarian selesai tanpa hasil`; `Disposal report canceled by Agus P` (laporan kedua) dengan Reason `Laporan diajukan sebelum pencarian selesai` dan Back to Missing `Yes`.
  - DU-012-4: Record Disposed `Drill Bosch GSB {runId}`, Asset ID `DRL-012-0004`, Group `Warehouse`, Status `Disposed`, Source `Manual`, Last Holder `—`, Reported By `Agus P`, Resolved Date `T0 − 8 hari, pukul 13:20`. Node: `Disposal reported by Agus P` dengan Reason `Bor hilang lebih dari 60 hari`; `Disposed` oleh `System` dengan Disposal No. milik DU-012-4.
  - DU-012-5: Record Rejected `Camera Canon EOS {runId}`, Asset ID `CAM-012-0005`, Group `Head Office`, Status `Rejected`, Source `Reported by holder`, Last Holder `Budi S`, Reported By `Budi S`, Resolved Date `T0 − 3 hari, pukul 09:30`. Node: `Report rejected by Rina W` dengan Reason `Aset terlihat di ruang studio lantai 3`.
  - DU-012-6: Record Canceled `Scanner Zebra DS2208 {runId}`, Asset ID `SCN-012-0006`, Group `Warehouse`, Status `Canceled`, Source `Reported by holder`, Last Holder `Joko S`, Reported By `Joko S`, Resolved Date `T0 − 5 hari, pukul 16:00`. Node: `Report canceled by Joko S`.
  - DU-012-7: Record Found `Laptop Dell Latitude 5420 {runId}`, Asset ID `LPT-012-0007`, Group `Finance Room`, Status `Found`, Source `Reported by holder`, Last Holder `Sari D`, Reported By `Sari D`, Resolved Date `T0 − 1 hari, pukul 10:00`. Node: `Report confirmed by Rina W` dengan Closed lines berisi nomor transaksi dan jenis transaksi milik satu baris transaksi berjalan atas `Sari D` yang ditutup saat Confirm (nomor transaksi dibentuk server dan menjadi milik entri ini); `Marked as found by Rina W` dengan Found at `Server Room`, Asset Status `Normal`, Manual identification `Yes` (TAG tidak dipindai, jalur `I Can't Scan the TAG`), Note `Ditemukan di laci ruang rapat lantai 2`, dan satu Photo terlampir.
  - DU-012-8: Pengguna `Agus Prasetyo {runId}`, role Total Control, seluruh client, sehingga berhak Report Missing, Report Disposal, dan membatalkan laporan Disposal-nya sendiri; tampil sebagai `Agus P`, dari `Agus Prasetyo {runId}`.
  - Pengguna pada data: Rina W, Total Control, seluruh client; Dewi A, Manage asset & TAG dengan Update pada Group Head Office; Agus P, pengguna DU-012-8; Rudi H, PIC yang tercatat bagi Joko S; Joko S, karyawan pemegang tanpa akun; Budi S dan Sari D, pemegang yang memakai akun sendiri.
  - DU-012-9: Notifikasi in-app bagi Rina W atas record DU-012-2, event `missing_holder_reported`, belum dibaca.
  - DU-012-10: Notifikasi in-app bagi Rina W atas record DU-012-7, event `missing_resolved`, belum dibaca.
  - Status global aset DU-012-2 `Missing` dan Transaction log aset itu memuat entri `Reported missing` berstatus `Waiting for Confirmation`.
  - Waktu pada data ditulis relatif terhadap waktu run `T0`, dan ditampilkan menurut Date Format dan Time Format di bawah.
- Kondisi:
  - Date Format bernilai `DD/MM/YY`
  - Time Format bernilai `HH:mm`
  - Long missing after bernilai `30`

## Test Steps

### Missing Log dibuka dari kolom Name pada record Long missing
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId}`, `Hand Pallet Truck {runId}`, dan `Projector Epson EB-X06 {runId}` tampil di sub-tab Active
3. Klik nama `Laptop Lenovo ThinkPad T14 {runId}` pada kolom Name
4. Verifikasi dialog `Missing Log` terbuka
5. Verifikasi dialog memuat record `Laptop Lenovo ThinkPad T14 {runId}` dengan Asset ID milik DU-012-1
6. Verifikasi dialog tidak menampilkan nomor transaksi record
7. Verifikasi Last Holder `Dewi A` tampil di dialog
8. Verifikasi Reported By `Rina W` tampil di dialog
9. Verifikasi badge status record `Missing` tampil
10. Verifikasi penanda `Long missing` tampil
11. Verifikasi footer `[Reject]` dan `[Confirm]` tidak tampil pada record berstatus `Missing`

### Isi node per jenis peristiwa pada record Long missing
12. Verifikasi node `Reported missing by Rina W` memuat What happened `Laptop tidak ada di meja kerja setelah rapat bulanan`
13. Verifikasi node `Update added by Rina W` memuat Update `Sudah dicek ke ruang arsip lantai 2, belum ditemukan`
14. Verifikasi node `Detected by scan` dari reader memuat Last seen `T0 − 6 hari, pukul 11:10` menurut Date Format dan Time Format, diikuti pemindai `Gate A reader`
15. Verifikasi node `Detected by scan` dari `Gate A reader` memuat Count `3`
16. Verifikasi node `Detected by scan` dari pengguna memuat Last seen `T0 − 2 hari, pukul 15:25` menurut Date Format dan Time Format, diikuti pemindai `Agus P`
17. Verifikasi node `Reported found by Agus P` memuat Location `—`
18. Verifikasi node `Reported found by Agus P` memuat Photo yang terlampir pada DU-012-1
19. Verifikasi node `Long missing` oleh `System` memuat Days missing `30`

### Last Seen di tabel sama dengan node deteksi terbaru
20. Klik `✕` pada dialog Missing Log
21. Verifikasi sel Last Seen baris `Laptop Lenovo ThinkPad T14 {runId}` menampilkan waktu `T0 − 2 hari, pukul 15:25` diikuti `Agus P`, sama dengan Last seen node `Detected by scan` terbaru

### Aksi baris Missing Log dan ketiadaan Changelog
22. Klik `⋯` pada baris `Laptop Lenovo ThinkPad T14 {runId}`
23. Verifikasi menu baris memuat `Missing Log`
24. Verifikasi menu baris memuat `Add Update` sebagai aksi atas record
25. Verifikasi menu baris memuat `Mark as Found` sebagai aksi atas record
26. Verifikasi menu baris memuat `Report Disposal` sebagai aksi atas record
27. Verifikasi menu baris tidak memuat `Changelog`
28. Klik `Missing Log`
29. Verifikasi dialog `Missing Log` terbuka untuk record `Laptop Lenovo ThinkPad T14 {runId}`
30. Verifikasi dialog tidak memuat tombol `Add Update` maupun `Mark as Found`

### Footer Reject dan Confirm pada record Waiting for Confirmation
31. Klik `✕` pada dialog Missing Log
32. Klik `⋯` pada baris `Hand Pallet Truck {runId}`
33. Verifikasi menu baris memuat `Review` sebagai aksi atas record berstatus `Waiting for Confirmation`
34. Klik `Review`
35. Verifikasi dialog `Missing Log` terbuka untuk record `Hand Pallet Truck {runId}` dengan badge status record `Waiting for Confirmation`
36. Verifikasi footer `[Reject]` dan `[Confirm]` tampil pada dialog yang dibuka lewat `Review`
37. Verifikasi Last Holder `Joko S` tampil di dialog
38. Verifikasi Reported By `Rudi H (on behalf of Joko S)` tampil di dialog
39. Verifikasi node `Reported missing by Rudi H on behalf of Joko S` memuat What happened `Hand pallet truck tidak kembali dari area bongkar muat`
40. Klik `✕` pada dialog Missing Log
41. Klik nama `Hand Pallet Truck {runId}` pada kolom Name
42. Verifikasi footer `[Reject]` dan `[Confirm]` tampil pada dialog yang dibuka lewat kolom Name

### Prev dan Next berpindah menurut urutan tabel
43. Verifikasi `Prev` Disabled karena record `Hand Pallet Truck {runId}` adalah baris pertama tabel
44. Klik `Next`
45. Verifikasi dialog memuat record `Laptop Lenovo ThinkPad T14 {runId}`
46. Klik `Next`
47. Verifikasi dialog memuat record `Projector Epson EB-X06 {runId}`
48. Verifikasi `Next` Disabled karena record `Projector Epson EB-X06 {runId}` adalah baris terakhir tabel

### Node Disposal pada record yang kembali ke Missing
49. Verifikasi badge status record `Missing` tampil
50. Verifikasi penanda `Long missing` tidak tampil karena Days Missing `10 days` di bawah Long missing after `30`
51. Verifikasi node `Disposal reported by Agus P` dengan Reason `Aset belum ditemukan sesudah pencarian di seluruh kantor` memuat Report ID milik laporan Disposal pertama DU-012-3
52. Verifikasi node `Disposal report declined by Rina W` memuat Report ID yang sama dengan laporan Disposal pertama DU-012-3
53. Verifikasi node `Disposal report declined by Rina W` memuat Reason `Pencarian di gudang cabang masih berlangsung`
54. Verifikasi node `Disposal report declined by Rina W` memuat Back to Missing `Yes`
55. Verifikasi node `Disposal reported by Agus P` dengan Reason `Pencarian selesai tanpa hasil` memuat Report ID milik laporan Disposal kedua DU-012-3
56. Verifikasi node `Disposal report canceled by Agus P` memuat Report ID yang sama dengan laporan Disposal kedua DU-012-3
57. Verifikasi node `Disposal report canceled by Agus P` memuat Reason `Laporan diajukan sebelum pencarian selesai`
58. Verifikasi node `Disposal report canceled by Agus P` memuat Back to Missing `Yes`

### Node pada record di sub-tab History
59. Klik `✕` pada dialog Missing Log
60. Klik sub-tab `History`
61. Ketik Search `{runId}`, tekan Enter
62. Klik `⋯` pada baris `Drill Bosch GSB {runId}`
63. Klik `Missing Log`
64. Verifikasi dialog `Missing Log` terbuka untuk record `Drill Bosch GSB {runId}` dari sub-tab History
65. Verifikasi node `Disposal reported by Agus P` memuat Reason `Bor hilang lebih dari 60 hari`
66. Verifikasi node `Disposed` oleh `System` memuat Disposal No. milik DU-012-4
67. Klik `✕` pada dialog Missing Log
68. Klik nama `Camera Canon EOS {runId}` pada kolom Name
69. Verifikasi node `Report rejected by Rina W` memuat Reason `Aset terlihat di ruang studio lantai 3`
70. Klik `✕` pada dialog Missing Log
71. Klik nama `Scanner Zebra DS2208 {runId}` pada kolom Name
72. Verifikasi node `Report canceled by Joko S` tampil
73. Klik `✕` pada dialog Missing Log
74. Klik nama `Laptop Dell Latitude 5420 {runId}` pada kolom Name
75. Verifikasi node `Report confirmed by Rina W` tampil
76. Verifikasi node `Marked as found by Rina W` memuat Found at `Server Room`
77. Verifikasi node `Marked as found by Rina W` memuat Asset Status `Normal`
78. Verifikasi node `Marked as found by Rina W` memuat Note `Ditemukan di laci ruang rapat lantai 2`
79. Verifikasi node `Marked as found by Rina W` memuat Photo yang terlampir pada DU-012-7
### Prev dan Next pada dialog yang dibuka dari sub-tab History
80. Klik `✕` pada dialog Missing Log
81. Klik nama `Laptop Dell Latitude 5420 {runId}` pada kolom Name
82. Verifikasi `Prev` Disabled karena record `Laptop Dell Latitude 5420 {runId}` adalah baris pertama History menurut Resolved Date terbaru dulu
83. Klik `Next`
84. Verifikasi dialog memuat record `Camera Canon EOS {runId}`
85. Klik `Next`
86. Verifikasi dialog memuat record `Scanner Zebra DS2208 {runId}`
87. Klik `Next`
88. Verifikasi dialog memuat record `Drill Bosch GSB {runId}`
89. Verifikasi `Next` Disabled karena record `Drill Bosch GSB {runId}` adalah baris terakhir History
### Prev dan Next mengikuti urutan tabel setelah Sort diubah
90. Klik `✕` pada dialog Missing Log
91. Klik header `Resolved Date`
92. Klik nama `Laptop Dell Latitude 5420 {runId}` pada kolom Name
93. Verifikasi `Next` Disabled karena record `Laptop Dell Latitude 5420 {runId}` adalah baris terakhir menurut Resolved Date terlama dulu
94. Klik `Prev`
95. Verifikasi dialog memuat record `Camera Canon EOS {runId}`
### Prev dan Next mengikuti baris tabel setelah Search diubah
96. Klik `✕` pada dialog Missing Log
97. Ganti isi kotak Search dengan `Camera Canon EOS {runId}`, tekan Enter
98. Klik nama `Camera Canon EOS {runId}` pada kolom Name
99. Verifikasi `Prev` dan `Next` Disabled karena `Camera Canon EOS {runId}` satu-satunya baris tabel hasil Search
100. Klik `✕` pada dialog Missing Log
101. Klik `(←)` pada kotak Search
### Closed lines dan Manual identification pada record Found
102. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
103. Klik nama `Laptop Dell Latitude 5420 {runId}` pada kolom Name
104. Verifikasi node `Report confirmed by Rina W` memuat Closed lines berisi nomor transaksi dan jenis transaksi milik baris yang ditutup pada DU-012-7
105. Verifikasi node `Marked as found by Rina W` memuat Manual identification `Yes`
106. Klik `✕` pada dialog Missing Log
107. Klik `(←)` pada kotak Search
### Footer Reject dan Confirm dari aksi baris Missing Log pada record Waiting for Confirmation
108. Klik sub-tab `Active`
109. Ketik Search `{runId}`, tekan Enter
110. Klik `⋯` pada baris `Hand Pallet Truck {runId}`
111. Klik `Missing Log`
112. Verifikasi dialog `Missing Log` terbuka untuk record `Hand Pallet Truck {runId}` dengan badge status record `Waiting for Confirmation`
113. Verifikasi footer `[Reject]` dan `[Confirm]` tampil pada dialog yang dibuka lewat aksi baris `Missing Log`
114. Klik `✕` pada dialog Missing Log
115. Klik `(←)` pada kotak Search
### Pintu masuk banner Asset Detail
116. Buka halaman `Assets`
117. Ketik Search `Hand Pallet Truck {runId}`, tekan Enter
118. Klik nama `Hand Pallet Truck {runId}` pada kolom Name
119. Verifikasi banner `Reported missing on` tampil pada Asset Detail
120. Klik `[View]` pada banner
121. Verifikasi dialog `Missing Log` terbuka untuk record `Hand Pallet Truck {runId}` dengan badge status record `Waiting for Confirmation`
122. Verifikasi footer `[Reject]` dan `[Confirm]` tampil pada dialog yang dibuka lewat banner
123. Klik `✕` pada dialog Missing Log
### Pintu masuk aksi baris Transaction log Asset Detail
124. Buka Transaction log pada Asset Detail
125. Buka sub-tab `Missing` pada Transaction log
126. Verifikasi entri `Reported missing` berstatus `Waiting for Confirmation` tampil
127. Klik `⋯` pada entri `Reported missing`
128. Klik `Missing Log`
129. Verifikasi dialog `Missing Log` terbuka untuk record `Hand Pallet Truck {runId}` dengan badge status record `Waiting for Confirmation`
130. Verifikasi footer `[Reject]` dan `[Confirm]` tampil pada dialog yang dibuka lewat aksi baris Transaction log
131. Klik `✕` pada dialog Missing Log
### Pintu masuk tautan notifikasi
132. Buka daftar notifikasi
133. Klik notifikasi event `missing_holder_reported` untuk `Hand Pallet Truck {runId}`
134. Verifikasi halaman Missing terbuka pada sub-tab `Active`
135. Verifikasi dialog `Missing Log` terbuka untuk record `Hand Pallet Truck {runId}` dengan badge status record `Waiting for Confirmation`
136. Verifikasi footer `[Reject]` dan `[Confirm]` tampil pada dialog yang dibuka lewat tautan notifikasi
137. Klik `✕` pada dialog Missing Log
138. Buka daftar notifikasi
139. Klik notifikasi event `missing_resolved` untuk `Laptop Dell Latitude 5420 {runId}`
140. Verifikasi halaman Missing terbuka pada sub-tab `History`
141. Verifikasi dialog `Missing Log` terbuka untuk record `Laptop Dell Latitude 5420 {runId}` dengan badge status record `Found`
142. Verifikasi footer `[Reject]` dan `[Confirm]` tidak tampil pada record berstatus `Found`
143. Klik `✕` pada dialog Missing Log

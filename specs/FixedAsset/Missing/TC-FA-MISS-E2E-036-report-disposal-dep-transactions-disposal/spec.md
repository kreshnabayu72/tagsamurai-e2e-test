---
id: TC-FA-MISS-E2E-036-report-disposal-dep-transactions-disposal
title: "Report Disposal satu record dan Cancel Disposal Report: status Reported Disposal, Mark as Found Hidden, kembali Missing, kembali Reported Disposal sesudah Request ditolak atau dibatalkan, node Disposal"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.1#r5", "§4.1a#r33", "§4.1a#r34", "§4.4#r9", "§4.4#r11", "§4.2.4#r21", "§4.2.4#r22", "§4.2.4#p9", "§4.2.4#p15", "§7.2#r4", "§7.2#r16", "§7.2#r17", "§7.3#r10", "§9.6#r9", "§9.2#r3", "§9.2#r4", "§9.2#b30", "§9.2#b31", "§9.4.2#r11", "§9.4.2#r12", "§9.4.4#r16", "§9.4.4#r17", "§8.1#r15", "§8.1#r16", "§8.1#r17", "§8.1#r18", "§8#r11", "§8.1#p2", "§9.7#r5", "§9.8#p2", "§3#p8", "§4.3#r3", "§4.3#r6", "§2.1#r9", "§2.1#r10", "§2.1#b6", "§4.8#r9", "§4.1#r11", "§4.1#r8", "§6#r2", "§6#r3", "§9.2#p11", "§9.2#p12", "§9.2#p13", "§11#r7", "§1#b4", "§1.2#r18", "§1.2#r21", "§1.2#r22", "§1.2#r96", "§1.2#r97", "§1.2#r98", "§1.2#r99", "§1.2#r100", "§1.2#r101", "§1.2#r102", "§1.2#r103", "§1.2#r35", "§1.2#r36", "§1.2#r116", "§10#r4", "§8.2#b2", "§9.4.1#r3", "EB-FB-1@report-disposal", "EB-FB-1@cancel-disposal-report", "§1.2#r45", "§9.2#r2"]
smoke: []
dependsOn: ["Transactions Disposal: dialog Report Disposal D-DISP-13", "Transactions Disposal: tab Reported > Decline dan Cancel Report", "Transactions Disposal: Dispose > form Request Write-off", "Transactions Disposal: Draft Disposal", "Transactions Disposal: Request Write-off > Reject atau Cancel Request"]
trace:
  "§9.1#r5": [10, 19]
  "§4.1a#r33": [4, 73]
  "§4.1a#r34": [14, 55]
  "§4.4#r9": [6, 10]
  "§4.4#r11": [19]
  "§4.2.4#r21": [10]
  "§4.2.4#r22": [19]
  "§4.2.4#p9": [16]
  "§4.2.4#p15": [6, 87]
  "§7.2#r4": [16]
  "§7.2#r16": [10]
  "§7.2#r17": [19]
  "§7.3#r10": [18]
  "§9.6#r9": [9, 18]
  "§9.2#r3": [10, 61, 116]
  "§9.2#r4": [51, 61, 110, 116]
  "§9.2#b30": [10, 19, 61]
  "§9.2#b31": [14, 51, 83, 91, 126]
  "§9.4.2#r11": [36, 38, 112, 116]
  "§9.4.2#r12": [13, 21, 54, 125]
  "§9.4.4#r16": [23, 38, 67]
  "§9.4.4#r17": [13, 24]
  "§8.1#r15": [23]
  "§8.1#r16": [38]
  "§8.1#r17": [24, 138]
  "§8.1#r18": [67]
  "§8#r11": [23, 24, 38, 67]
  "§8.1#p2": [61, 77, 112, 116, 119, 142, 143]
  "§9.7#r5": [10, 19, 61]
  "§9.8#p2": [10, 19, 61, 116]
  "§3#p8": [10, 19, 36, 51, 61, 112, 116]
  "§4.3#r3": [13, 54, 125]
  "§4.3#r6": [55]
  "§2.1#r9": [4]
  "§2.1#r10": [14]
  "§2.1#b6": [4, 14]
  "§4.8#r9": [4, 14]
  "§4.1#r11": [6]
  "§4.1#r8": [16]
  "§6#r2": [54]
  "§6#r3": [55]
  "§9.2#p11": [10, 51]
  "§9.2#p12": [61, 64, 112, 116, 119]
  "§9.2#p13": [13, 54]
  "§11#r7": [10, 77]
  "§1#b4": [77]
  "§1.2#r18": [10, 51]
  "§1.2#r21": [19, 36]
  "§1.2#r22": [61, 112, 116, 119]
  "§1.2#r96": [10]
  "§1.2#r97": [10, 102, 103, 107, 110]
  "§1.2#r98": [6, 51]
  "§1.2#r99": [51]
  "§1.2#r100": [51]
  "§1.2#r101": [19]
  "§1.2#r102": [14, 55]
  "§1.2#r103": [10, 51]
  "§1.2#r35": [6]
  "§1.2#r36": [6]
  "§1.2#r116": [71, 73]
  "§10#r4": [64, 65]
  "§8.2#b2": [9, 18]
  "§9.4.1#r3": [13, 54]
  "EB-FB-1@report-disposal": [9]
  "EB-FB-1@cancel-disposal-report": [18]
  "§1.2#r45": [77]
  "§9.2#r2": [19, 36]
anchor: [3, 12, 53, 82, 124]
coverage:
  web: automated
---

# Report Disposal satu record dan Cancel Disposal Report: status Reported Disposal, Mark as Found Hidden, kembali Missing, kembali Reported Disposal sesudah Request ditolak atau dibatalkan, node Disposal

## Prerequisites
- Aktor: Total Control `Rina W`, yang juga Aktor Disposal. Aktor lain yang memicu perubahan: approver Disposal yang menolak baris Request; Group Manager `Andi P`, Group Manager Head Office dengan Group binaan Head Office beserta sub-group `Finance Room` dan `Server Room`, yang membatalkan Report di tab Reported.
- Layar awal: Assets > Missing > Active.
- Data:
  - DU-036-1: Asset `Laptop Dell Latitude 5420 {runId}`, Group `Finance Room`, dengan record Missing berstatus `Missing`.
  - DU-036-2: Asset `Hand Pallet Truck {runId}`, Group `Warehouse`, dengan record Missing berstatus `Missing`.
  - DU-036-3: Asset `Scanner Zebra DS2208 {runId}`, Group `Warehouse`, dengan record Missing berstatus `Missing`.
  - DU-036-4: Asset `Drill Bosch GSB {runId}`, Group `Warehouse`, dengan record Missing berstatus `Disposed` yang ditutup `System` pada Disposal Executed, beserta Disposal No. milik entri ini.
  - DU-036-5: Asset `Laptop Lenovo ThinkPad T14 {runId}`, Group `Head Office`, dengan record Missing berstatus `Missing` yang dilaporkan pada `T0 − 34 hari`.
  - DU-036-6: Asset `Camera Canon EOS {runId}`, Group `Head Office`, tanpa record Missing, dengan Disposal Report berstatus `Reported`.
  - DU-036-7: Reason `Aset tidak ditemukan setelah penelusuran tiga minggu`.
  - DU-036-8: Reason `Aset hilang saat pemindahan gudang`.
  - DU-036-9: Reason `Aset tidak ada di lokasi terakhir`.
  - DU-036-10: Reason Decline `Aset masih dalam penelusuran`.
  - DU-036-11: What happened `Kamera hilang dari ruang studio setelah sesi foto`.
  - DU-036-12: Asset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, dengan record Missing berstatus `Missing`.
  - DU-036-13: Reason `Printer tidak ditemukan di ruang arsip`.
  - DU-036-14: Asset `Tablet Lenovo Tab M10 {runId}`, Group `Finance Room`, dengan record Missing berstatus `Missing`.
  - DU-036-15: Reason `Tablet tidak ditemukan di ruang rapat lantai dua`.
  - DU-036-16: Reason Cancel Report `Tablet ditemukan di ruang rapat lantai dua`.
- Kondisi:
  - Long missing after bernilai `30`.
  - Date Format bernilai `DD/MM/YY`.
  - Time Format bernilai `HH:mm`.
  - Akun `Rina W` dan `Andi P` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Report Disposal lalu Cancel Disposal Report atas satu record
1. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
2. Buka menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
3. Verifikasi aksi `Mark as Found` tampil pada menu
4. Verifikasi aksi `Report Disposal` tampil pada menu
5. Klik `Report Disposal`
6. Verifikasi dialog `Report Disposal` hanya memuat isian `Reason`
7. Isi Reason `Aset tidak ditemukan setelah penelusuran tiga minggu`
8. Kirim dialog Report Disposal
9. Verifikasi toast `Success, disposal report has been created.` tampil
10. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil di sub-tab Active berstatus `Reported Disposal`
11. Buka menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
12. Verifikasi aksi `Missing Log` tampil pada menu
13. Verifikasi aksi `Mark as Found` tidak tampil pada menu
14. Verifikasi aksi `Cancel Disposal Report` tampil pada menu
15. Klik `Cancel Disposal Report`
16. Verifikasi dialog `Cancel Disposal Report` terbuka
17. Kirim dialog Cancel Disposal Report
18. Verifikasi toast sukses Cancel Disposal Report tampil
19. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` kembali berstatus `Missing`
20. Buka menu `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
21. Verifikasi aksi `Mark as Found` tampil kembali pada menu

### Node Disposal di Missing Log
22. Klik `Laptop Dell Latitude 5420 {runId}` pada kolom Name
23. Verifikasi dialog Missing Log memuat node `Disposal reported by` oleh `Rina W` dengan Reason `Aset tidak ditemukan setelah penelusuran tiga minggu`
24. Verifikasi dialog Missing Log memuat node `Disposal report canceled by` oleh `Rina W` dengan Back to Missing `Yes`
25. Tutup dialog Missing Log dengan `✕`

### Decline Report oleh Aktor Disposal mengembalikan record ke Missing
26. Ganti isi kotak search dengan `Hand Pallet Truck {runId}`, tekan Enter
27. Buka menu `⋯` pada baris `Hand Pallet Truck {runId}`
28. Klik `Report Disposal`
29. Isi Reason `Aset hilang saat pemindahan gudang`
30. Kirim dialog Report Disposal
31. Buka tab `Reported` pada `Transactions > Disposal`
32. Lakukan Decline atas Report `Hand Pallet Truck {runId}` dengan Reason `Aset masih dalam penelusuran`
33. Buka halaman `Assets`
34. Klik tab `Missing`
35. Ketik Search `Hand Pallet Truck {runId}`, tekan Enter
36. Verifikasi baris `Hand Pallet Truck {runId}` berstatus `Missing`
37. Klik `Hand Pallet Truck {runId}` pada kolom Name
38. Verifikasi dialog Missing Log memuat node `Disposal report declined by` oleh `Rina W` dengan Reason `Aset masih dalam penelusuran` dan Back to Missing `Yes`
39. Tutup dialog Missing Log dengan `✕`

### Dispose menjadikan record In Disposal Process dan batalnya baris mengembalikan ke Reported Disposal
40. Ganti isi kotak search dengan `Scanner Zebra DS2208 {runId}`, tekan Enter
41. Buka menu `⋯` pada baris `Scanner Zebra DS2208 {runId}`
42. Klik `Report Disposal`
43. Isi Reason `Aset tidak ada di lokasi terakhir`
44. Kirim dialog Report Disposal
45. Buka tab `Reported` pada `Transactions > Disposal`
46. Klik `Dispose` pada Report `Scanner Zebra DS2208 {runId}`
47. Kirim form Request Disposal jenis `Write-off` atas `Scanner Zebra DS2208 {runId}`
48. Buka halaman `Assets`
49. Klik tab `Missing`
50. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
51. Verifikasi baris `Scanner Zebra DS2208 {runId}` berstatus `In Disposal Process`
52. Buka menu `⋯` pada baris `Scanner Zebra DS2208 {runId}`
53. Verifikasi aksi `Missing Log` tampil pada menu
54. Verifikasi aksi `Mark as Found` tidak tampil pada menu
55. Verifikasi aksi `Cancel Disposal Report` tidak tampil pada menu
56. Tutup menu `⋯` dengan tombol Esc
57. Batalkan baris Request Disposal atas `Scanner Zebra DS2208 {runId}` di `Transactions > Disposal`
58. Buka halaman `Assets`
59. Klik tab `Missing`
60. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
61. Verifikasi baris `Scanner Zebra DS2208 {runId}` kembali berstatus `Reported Disposal`

### Record Disposed tampil di History dengan node Disposed
62. Klik sub-tab `History`
63. Ketik Search `Drill Bosch GSB {runId}`, tekan Enter
64. Verifikasi baris `Drill Bosch GSB {runId}` berstatus `Disposed`
65. Verifikasi kolom Resolved By pada baris itu `System`
66. Klik `Drill Bosch GSB {runId}` pada kolom Name
67. Verifikasi dialog Missing Log memuat node `Disposed` oleh `System` dengan Disposal No. milik DU-036-4
68. Tutup dialog Missing Log dengan `✕`

### Record Long missing mendapat saran Report Disposal
69. Klik sub-tab `Active`
70. Ketik Search `Laptop Lenovo ThinkPad T14 {runId}`, tekan Enter
71. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId}` memuat penanda `Long missing`
72. Buka menu `⋯` pada baris `Laptop Lenovo ThinkPad T14 {runId}`
73. Verifikasi aksi `Report Disposal` tampil pada menu

### Report Missing atas aset dengan Disposal Report Reported
74. Rina W melaporkan `Camera Canon EOS {runId}` hilang lewat Report Missing dengan What happened `Kamera hilang dari ruang studio setelah sesi foto`
75. Buka tab `Reported` pada `Transactions > Disposal`
76. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
77. Verifikasi Report atas `Camera Canon EOS {runId}` berstatus `Canceled` dengan alasan `Asset reported missing` oleh `System`

### Aksi Cancel Disposal Report tidak tampil pada record Missing
78. Buka halaman `Assets`
79. Klik tab `Missing`
80. Ketik Search `Laptop Lenovo ThinkPad T14 {runId}`, tekan Enter
81. Buka menu `⋯` pada baris `Laptop Lenovo ThinkPad T14 {runId}`
82. Verifikasi aksi `Report Disposal` tampil pada menu
83. Verifikasi aksi `Cancel Disposal Report` tidak tampil pada menu
84. Tutup menu `⋯` dengan tombol Esc

### Dialog Report Disposal memuat aset yang dipilih
85. Buka menu `⋯` pada baris `Laptop Lenovo ThinkPad T14 {runId}`
86. Klik `Report Disposal`
87. Verifikasi dialog `Report Disposal` memuat aset `Laptop Lenovo ThinkPad T14 {runId}`
88. Tutup dialog Report Disposal tanpa mengirim

### Cancel Disposal Report membatalkan Report di tab Reported
89. Buka tab `Reported` pada `Transactions > Disposal`
90. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
91. Verifikasi Report atas `Laptop Dell Latitude 5420 {runId}` berstatus `Canceled`

### Draft Disposal tidak mengubah record dan tidak mengubah Report
92. Buka halaman `Assets`
93. Klik tab `Missing`
94. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
95. Buka menu `⋯` pada baris `Printer HP LaserJet M404 {runId}`
96. Klik `Report Disposal`
97. Isi Reason `Printer tidak ditemukan di ruang arsip`
98. Kirim dialog Report Disposal
99. Buka tab `Reported` pada `Transactions > Disposal`
100. Klik `Dispose` pada Report `Printer HP LaserJet M404 {runId}`
101. Simpan Draft Disposal jenis `Write-off` atas `Printer HP LaserJet M404 {runId}` tanpa Submit
102. Verifikasi Report atas `Printer HP LaserJet M404 {runId}` di tab Reported berstatus `Reported`
103. Verifikasi baris Report atas `Printer HP LaserJet M404 {runId}` di tab Reported tidak memuat penanda apa pun akibat Draft Disposal
104. Buka halaman `Assets`
105. Klik tab `Missing`
106. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
107. Verifikasi baris `Printer HP LaserJet M404 {runId}` tetap berstatus `Reported Disposal`

### Request Write-off yang ditolak mengembalikan record ke Reported Disposal dan Report ke Reported
108. Buka tab `Reported` pada `Transactions > Disposal`
109. Kirim Draft Disposal atas `Printer HP LaserJet M404 {runId}` sebagai Request Disposal jenis `Write-off`
110. Verifikasi Report atas `Printer HP LaserJet M404 {runId}` tetap tampil di tab Reported berstatus `In Disposal Process`
111. Approver menolak baris Request Disposal atas `Printer HP LaserJet M404 {runId}`
112. Verifikasi Report atas `Printer HP LaserJet M404 {runId}` kembali berstatus `Reported`
113. Buka halaman `Assets`
114. Klik tab `Missing`
115. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
116. Verifikasi baris `Printer HP LaserJet M404 {runId}` kembali berstatus `Reported Disposal`

### Request Write-off yang dibatalkan: Report kembali Reported, Mark as Found Hidden, Cancel Disposal Report tersedia lagi
117. Buka tab `Reported` pada `Transactions > Disposal`
118. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
119. Verifikasi Report atas `Scanner Zebra DS2208 {runId}` kembali berstatus `Reported`
120. Buka halaman `Assets`
121. Klik tab `Missing`
122. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
123. Buka menu `⋯` pada baris `Scanner Zebra DS2208 {runId}`
124. Verifikasi aksi `Missing Log` tampil pada menu
125. Verifikasi aksi `Mark as Found` tidak tampil pada menu
126. Verifikasi aksi `Cancel Disposal Report` tampil pada menu
127. Tutup menu `⋯` dengan tombol Esc

### Cancel Report di tab Reported oleh Group Manager menulis node Disposal report canceled by atas namanya
128. Ganti isi kotak search dengan `Tablet Lenovo Tab M10 {runId}`, tekan Enter
129. Buka menu `⋯` pada baris `Tablet Lenovo Tab M10 {runId}`
130. Klik `Report Disposal`
131. Isi Reason `Tablet tidak ditemukan di ruang rapat lantai dua`
132. Kirim dialog Report Disposal
133. `Andi P` membatalkan Report atas `Tablet Lenovo Tab M10 {runId}` lewat Cancel Report di tab `Reported` pada `Transactions > Disposal` dengan Reason `Tablet ditemukan di ruang rapat lantai dua`
134. Buka halaman `Assets`
135. Klik tab `Missing`
136. Ketik Search `Tablet Lenovo Tab M10 {runId}`, tekan Enter
137. Klik `Tablet Lenovo Tab M10 {runId}` pada kolom Name
138. Verifikasi dialog Missing Log memuat node `Disposal report canceled by` oleh `Andi P` dengan Reason `Tablet ditemukan di ruang rapat lantai dua` dan Back to Missing `Yes`
139. Tutup dialog Missing Log dengan `✕`

### Missing Log record baru atas aset dengan Report yang ditutup System dimulai dari Reported missing by
140. Ganti isi kotak search dengan `Camera Canon EOS {runId}`, tekan Enter
141. Klik `Camera Canon EOS {runId}` pada kolom Name
142. Verifikasi node paling awal dialog Missing Log adalah `Reported missing by` oleh `Rina W` dengan What happened `Kamera hilang dari ruang studio setelah sesi foto`
143. Verifikasi dialog Missing Log tidak memuat node `Disposal reported by` dan node `Disposal report canceled by`
144. Tutup dialog Missing Log dengan `✕`

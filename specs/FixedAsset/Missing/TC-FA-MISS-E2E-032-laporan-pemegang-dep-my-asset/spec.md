---
id: TC-FA-MISS-E2E-032-laporan-pemegang-dep-my-asset
title: "Laporan pemegang dari My Asset: Waiting for Confirmation, Cancel Report menjadi Canceled, status laporan di baris My Asset"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.1#r6", "§9.2#b34", "§3#p4", "§7.3#r6", "§7.3#r11", "§7.2#r3", "§7.2#r18", "§4.2.4#p8", "§9.6#r7", "§9.7#r2", "§9.7#r8", "§9.2#r1", "§9.2#r8", "§8.1#r7", "§8.1#r8", "§1.2#r18", "§1.2#r20", "§1.2#r53", "§1.2#r55", "§1.2#r57", "§1.2#r58", "§1.2#r70", "§1.2#r73", "§1.2#r122", "§1.2#r123", "§2#b3", "§2.1#r3", "§2.1#r8", "§2.1#b4", "§4.8#r3", "§4.8#r7", "§9.11#r3", "§9.4.2#r27", "§9.4.2#r22", "§9.2#b36", "§9.4.4#r20", "§9.4.4#r22", "§9.4.3#b5", "§11#r4", "§4.2.3#p2", "§4.2.4#r15", "§9.9#r1", "§9.8#r2", "§9.6#r1", "EB-FB-1@report-missing-pemegang", "EB-FB-1@cancel-report", "EB-FB-2@go-back-cancel-report", "§9.3#b1", "§4.6#b3", "§4.6#b6", "§8.2#p5", "§8.2#p10", "§8.2#p27", "§2.1#r2", "§4.8#r12", "§4.8#r2"]
smoke: []
dependsOn: ["My Asset: tab Borrowed", "My Asset: tab Assigned", "My Asset: aksi Cancel Report"]
trace:
  "§9.1#r6": [9, 27]
  "§9.2#b34": [27, 39, 40, 65]
  "§3#p4": [9, 19]
  "§7.3#r6": [8, 38]
  "§7.3#r11": [18, 72]
  "§7.2#r3": [13]
  "§7.2#r18": [31]
  "§4.2.4#p8": [13]
  "§9.6#r7": [18, 31]
  "§9.7#r2": [10, 93, 94]
  "§9.7#r8": [20, 106, 107]
  "§9.2#r1": [9, 55]
  "§9.2#r8": [19, 72, 114, 117]
  "§8.1#r7": [46, 135]
  "§8.1#r8": [51]
  "§1.2#r18": [9]
  "§1.2#r20": [19]
  "§1.2#r53": [1]
  "§1.2#r55": [9, 10]
  "§1.2#r57": [11]
  "§1.2#r58": [19, 20, 114, 117]
  "§1.2#r70": [56]
  "§1.2#r73": [69, 72]
  "§1.2#r122": [40]
  "§1.2#r123": [69]
  "§2#b3": [65]
  "§2.1#r3": [1, 8]
  "§2.1#r8": [11]
  "§2.1#b4": [11, 111]
  "§4.8#r3": [1]
  "§4.8#r7": [11, 74, 83, 85, 88]
  "§9.11#r3": [21, 22]
  "§9.4.2#r27": [61, 65, 67]
  "§9.4.2#r22": [55]
  "§9.2#b36": [55]
  "§9.4.4#r20": [39, 40, 96, 101]
  "§9.4.4#r22": [55]
  "§9.4.3#b5": [55]
  "§11#r4": [1]
  "§4.2.3#p2": [3]
  "§4.2.4#r15": [35]
  "§9.9#r1": [5]
  "§9.8#r2": [8]
  "§9.6#r1": [8, 38]
  "EB-FB-1@report-missing-pemegang": [8, 38]
  "EB-FB-1@cancel-report": [18]
  "EB-FB-2@go-back-cancel-report": [15, 79, 80]
  "§9.3#b1": [11]
  "§8.2#p5": [123]
  "§8.2#p10": [129]
  "§8.2#p27": [46, 51]
  "§4.6#b3": [3]
  "§4.6#b6": [21, 22]
  "§2.1#r2": [144]
  "§4.8#r12": [111]
  "§4.8#r2": [141, 144]
anchor: [73, 77, 82, 84, 87, 105, 110, 128, 140, 143]
coverage:
  web: automated
  android: automated
---

# Laporan pemegang dari My Asset: Waiting for Confirmation, Cancel Report menjadi Canceled, status laporan di baris My Asset

## Prerequisites
- Aktor: pemegang `Joko Santoso {runId}` tanpa hak Aktor Missing. Aktor lain: PIC `Rudi Hartono {runId}`, PIC pengganti `Wulan Sari {runId}`, pemegang `Andi Pratama {runId}` dengan hak Manage asset & TAG (Update) pada Group asetnya, dan Total Control `Rina W`.
- Layar awal: My Asset > Assigned.
- Data:
  - DU-032-1: Asset `Scanner Zebra DS2208 {runId}`, Group `Warehouse`, ditugaskan ke `Joko Santoso {runId}`, tanpa record Missing.
  - DU-032-2: Asset `Handheld Honeywell CT60 {runId}`, Group `Warehouse`, dipinjam `Joko Santoso {runId}`, tanpa record Missing.
  - DU-032-3: Asset `Projector Epson EB-X06 {runId}`, Group `Head Office`, ditugaskan ke karyawan tanpa akun `Dedi Kurniawan {runId}` dengan PIC `Rudi Hartono {runId}`, tanpa record Missing.
  - DU-032-4: Asset `Laptop Lenovo ThinkPad T14 {runId}`, Group `Head Office`, ditugaskan ke `Andi Pratama {runId}`, tanpa record Missing.
  - DU-032-5: Asset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, ditugaskan ke `Tono Wibowo {runId}` yang sudah dinonaktifkan, dengan record `Waiting for Confirmation` yang dilaporkan `Tono Wibowo {runId}` pada `T0 − 40 hari`.
  - DU-032-6: Asset `Camera Canon EOS {runId}`, Group `Head Office`, ditugaskan ke `Joko Santoso {runId}`, dengan record laporan Joko berstatus `Rejected` beralasan `Aset terlihat di gudang cabang`.
  - DU-032-7: Asset `Monitor LG 27UL500 {runId}`, Group `Head Office`, ditugaskan ke karyawan tanpa akun `Gita Permata {runId}` dengan PIC pengganti `Wulan Sari {runId}`, dengan record `Waiting for Confirmation` yang dilaporkan PIC sebelumnya `Rudi Hartono {runId}`.
  - DU-032-8: What happened `Scanner tidak ada di loker setelah shift malam`.
  - DU-032-9: What happened `Handheld tertinggal di kendaraan operasional`.
  - DU-032-10: What happened `Projector hilang dari ruang rapat setelah acara`.
  - DU-032-11: What happened `Laptop tidak ada di meja setelah perjalanan dinas`.
  - DU-032-12: Pengguna `Joko Santoso {runId}`, pemegang tanpa hak Aktor Missing.
  - DU-032-13: Pengguna `Rudi Hartono {runId}`, PIC atas nama karyawan tanpa akun.
  - DU-032-14: Pengguna `Wulan Sari {runId}`, PIC pengganti.
  - DU-032-15: Pengguna `Andi Pratama {runId}`, pemegang dengan hak Manage asset & TAG (Update) pada Group asetnya.
  - DU-032-16: Pengguna `Tono Wibowo {runId}`, pemegang yang sudah dinonaktifkan.
- Kondisi:
  - Akun `Joko Santoso {runId}`, `Rudi Hartono {runId}`, `Wulan Sari {runId}`, `Andi Pratama {runId}`, dan `Rina W` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Pemegang melaporkan aset yang ditugaskan dari My Asset
1. Verifikasi aksi `Report Missing` tampil pada baris `Scanner Zebra DS2208 {runId}`
2. Buka aksi Report Missing pada `Scanner Zebra DS2208 {runId}` di My Asset
3. Verifikasi dialog `Report Missing` tampil
4. Klik `[Report Missing]` pada dialog tanpa mengisi What happened
5. Verifikasi caption `What happened must not be empty` tampil di bawah isian What happened
6. Isi What happened `Scanner tidak ada di loker setelah shift malam`
7. Klik `[Report Missing]` pada dialog
8. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil
9. Verifikasi status laporan pada baris `Scanner Zebra DS2208 {runId}` `Waiting for Confirmation`
10. Verifikasi Asset Status pada baris `Scanner Zebra DS2208 {runId}` `Missing`
11. Verifikasi aksi `Cancel Report` tampil pada baris `Scanner Zebra DS2208 {runId}`

### Pemegang membatalkan laporan sendiri: Go Back lalu Cancel Report
12. Buka aksi Cancel Report pada `Scanner Zebra DS2208 {runId}` di My Asset
13. Verifikasi dialog `Cancel Report` memuat bullet `Scanner Zebra DS2208 {runId}` dan pertanyaan `Are you sure you want to cancel it?`
14. Klik `[Go Back]`
15. Verifikasi status laporan pada baris `Scanner Zebra DS2208 {runId}` tetap `Waiting for Confirmation`
16. Buka aksi Cancel Report pada `Scanner Zebra DS2208 {runId}` di My Asset
17. Klik `[Cancel Report]` pada dialog
18. Verifikasi toast `Success, report has been canceled.` tampil
19. Verifikasi status laporan pada baris `Scanner Zebra DS2208 {runId}` `Canceled`
20. Verifikasi aksi `Report Missing` tampil kembali pada baris `Scanner Zebra DS2208 {runId}`

### Status laporan Rejected beserta reason tampil di baris pemegang
21. Verifikasi status laporan pada baris `Camera Canon EOS {runId}` `Rejected`
22. Verifikasi reason `Aset terlihat di gudang cabang` tampil pada baris `Camera Canon EOS {runId}`

### Laporan dari tab Borrowed lalu Cancel Report atas record yang sudah berubah
23. Klik tab `Borrowed`
24. Buka aksi Report Missing pada `Handheld Honeywell CT60 {runId}` di My Asset
25. Isi What happened `Handheld tertinggal di kendaraan operasional`
26. Klik `[Report Missing]` pada dialog
27. Verifikasi status laporan pada baris `Handheld Honeywell CT60 {runId}` `Waiting for Confirmation`
28. Rina W melakukan Confirm atas laporan `Handheld Honeywell CT60 {runId}`, sementara daftar My Asset `Joko Santoso {runId}` belum dimuat ulang dan baris itu masih menampilkan status `Waiting for Confirmation`
29. Buka aksi Cancel Report pada `Handheld Honeywell CT60 {runId}` di My Asset
30. Klik `[Cancel Report]` pada dialog
31. Verifikasi dialog `Already Changed` memuat teks `This record was changed by Rina W. Reload to see the latest status.`
32. Klik `[Reload]`

### PIC melaporkan atas nama karyawan tanpa akun
33. Masuk sebagai `Rudi Hartono {runId}`
34. Buka aksi Report Missing pada `Projector Epson EB-X06 {runId}` di My Asset
35. Verifikasi kotak dampak memuat baris pemegang `Dedi Kurniawan {runId}` diikuti `and the asset admins will be notified.`
36. Isi What happened `Projector hilang dari ruang rapat setelah acara`
37. Klik `[Report Missing]` pada dialog
38. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil
39. Verifikasi status laporan pada baris `Projector Epson EB-X06 {runId}` `Waiting for Confirmation`
40. Verifikasi aksi `Cancel Report` tampil bagi PIC pada baris `Projector Epson EB-X06 {runId}`

### Node laporan di Missing Log atas laporan PIC dan laporan yang dibatalkan
41. Masuk sebagai `Rina W`
42. Buka halaman `Assets`
43. Klik tab `Missing`
44. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
45. Klik `Projector Epson EB-X06 {runId}` pada kolom Name
46. Verifikasi dialog Missing Log memuat node `Reported missing by` oleh `Rudi Hartono {runId}` atas nama `Dedi Kurniawan {runId}`
47. Tutup dialog Missing Log dengan `✕`
48. Klik sub-tab `History`
49. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
50. Klik `Scanner Zebra DS2208 {runId}` pada kolom Name
51. Verifikasi dialog Missing Log memuat node `Report canceled by` oleh `Joko Santoso {runId}`
52. Tutup dialog Missing Log dengan `✕`

### Laporan yang menunggu lama tidak ditutup otomatis dan diputuskan Aktor Missing
53. Klik sub-tab `Active`
54. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
55. Verifikasi baris `Printer HP LaserJet M404 {runId}` berstatus `Waiting for Confirmation`
56. Verifikasi aksi `Review` tampil pada baris `Printer HP LaserJet M404 {runId}`

### Pemegang dengan hak Aktor Missing melapor sebagai Pelapor admin
57. Masuk sebagai `Andi Pratama {runId}`
58. Buka aksi Report Missing pada `Laptop Lenovo ThinkPad T14 {runId}` di My Asset
59. Isi What happened `Laptop tidak ada di meja setelah perjalanan dinas`
60. Klik `[Report Missing]` pada dialog
61. Verifikasi toast `Success, asset has been reported missing.` tampil
62. Buka halaman `Assets`
63. Klik tab `Missing`
64. Ketik Search `Laptop Lenovo ThinkPad T14 {runId}`, tekan Enter
65. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId}` berstatus `Missing`
66. Buka menu `⋯` pada baris `Laptop Lenovo ThinkPad T14 {runId}`
67. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada aksi `Mark as Found` yang disabled

### PIC pengganti membatalkan laporan PIC sebelumnya
68. Masuk sebagai `Wulan Sari {runId}`
69. Verifikasi aksi `Cancel Report` tampil pada baris `Monitor LG 27UL500 {runId}`
70. Buka aksi Cancel Report pada `Monitor LG 27UL500 {runId}` di My Asset
71. Klik `[Cancel Report]` pada dialog
72. Verifikasi status laporan pada baris `Monitor LG 27UL500 {runId}` `Canceled`

### Cancel Report tidak tampil pada laporan PIC pengganti yang sudah Canceled
73. Verifikasi status laporan pada baris `Monitor LG 27UL500 {runId}` `Canceled`
74. Verifikasi aksi `Cancel Report` tidak tampil pada baris `Monitor LG 27UL500 {runId}`

### Go Back menutup dialog Cancel Report tanpa toast
75. Masuk sebagai `Rudi Hartono {runId}`
76. Buka aksi Cancel Report pada `Projector Epson EB-X06 {runId}` di My Asset
77. Verifikasi dialog `Cancel Report` memuat bullet `Projector Epson EB-X06 {runId}`
78. Klik `[Go Back]`
79. Verifikasi dialog `Cancel Report` tertutup
80. Verifikasi tidak ada toast yang tampil

### Cancel Report tidak tampil pada laporan Rejected, Canceled, dan yang sudah menjadi Missing
81. Masuk sebagai `Joko Santoso {runId}`
82. Verifikasi status laporan pada baris `Camera Canon EOS {runId}` `Rejected`
83. Verifikasi aksi `Cancel Report` tidak tampil pada baris `Camera Canon EOS {runId}`
84. Verifikasi status laporan pada baris `Scanner Zebra DS2208 {runId}` `Canceled`
85. Verifikasi aksi `Cancel Report` tidak tampil pada baris `Scanner Zebra DS2208 {runId}`
86. Klik tab `Borrowed`
87. Verifikasi Asset Status pada baris `Handheld Honeywell CT60 {runId}` `Missing`
88. Verifikasi aksi `Cancel Report` tidak tampil pada baris `Handheld Honeywell CT60 {runId}`

### Asset Detail: status global dan Transaction log atas laporan dari My Asset, dan status sesudah Cancel Report
89. Masuk sebagai `Rina W`
90. Buka halaman `Assets`
91. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
92. Klik `Projector Epson EB-X06 {runId}` pada kolom Name
93. Verifikasi Asset Status pada Asset Detail `Missing`
94. Verifikasi banner `Reported missing on` tampil pada Asset Detail
95. Buka Transaction log pada Asset Detail
96. Verifikasi entri `Reported missing` tampil di Transaction log
97. Buka halaman `Assets`
98. Ketik Search `Laptop Lenovo ThinkPad T14 {runId}`, tekan Enter
99. Klik `Laptop Lenovo ThinkPad T14 {runId}` pada kolom Name
100. Buka Transaction log pada Asset Detail
101. Verifikasi entri `Reported missing` tampil di Transaction log
102. Buka halaman `Assets`
103. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
104. Klik `Scanner Zebra DS2208 {runId}` pada kolom Name
105. Verifikasi tombol `[Report Missing]` tampil pada Asset Detail
106. Verifikasi Asset Status pada Asset Detail bukan `Missing`
107. Verifikasi banner `Reported missing on` tidak tampil pada Asset Detail

### Pemegang tanpa hak Aktor Missing tidak mendapat tab Missing
108. Masuk sebagai `Joko Santoso {runId}`
109. Buka halaman `Assets`
110. Verifikasi tab `Assets` tampil pada halaman Assets
111. Verifikasi tab `Missing` tidak tampil pada halaman Assets

### Status global aset dihitung ulang dari state aset terkini sesudah Cancel Report
112. Buka halaman `My Asset`
113. Klik tab `Assigned`
114. Verifikasi Asset Status pada baris `Scanner Zebra DS2208 {runId}` `Assigned`
115. Masuk sebagai `Wulan Sari {runId}`
116. Buka halaman `My Asset`
117. Verifikasi Asset Status pada baris `Monitor LG 27UL500 {runId}` `Assigned`

### Transaction log aset memuat laporan pemegang berstatus Waiting for Confirmation dan Cancel Report tidak membentuk baris
118. Masuk sebagai `Rina W`
119. Buka halaman `Assets`
120. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
121. Klik `Projector Epson EB-X06 {runId}` pada kolom Name
122. Buka Transaction log pada Asset Detail
123. Verifikasi entri `Reported missing` pada Transaction log berstatus `Waiting for Confirmation`
124. Buka halaman `Assets`
125. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
126. Klik `Scanner Zebra DS2208 {runId}` pada kolom Name
127. Buka Transaction log pada Asset Detail
128. Verifikasi entri `Reported missing` tampil di Transaction log
129. Verifikasi entri `Report canceled` tidak tampil di Transaction log

### Node Reported missing by atas laporan pemegang yang melapor dengan akunnya sendiri
130. Buka halaman `Assets`
131. Klik tab `Missing`
132. Klik sub-tab `History`
133. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
134. Klik `Scanner Zebra DS2208 {runId}` pada kolom Name
135. Verifikasi dialog Missing Log memuat node `Reported missing by` oleh `Joko Santoso {runId}` dengan What happened `Scanner tidak ada di loker setelah shift malam`
136. Tutup dialog Missing Log dengan `✕`

### Pemegang tanpa hak Aktor Missing tidak mendapat Report Missing sebagai Pelapor admin di Asset List dan Asset Detail
137. Masuk sebagai `Joko Santoso {runId}`
138. Buka halaman `Assets`
139. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
140. Verifikasi baris `Scanner Zebra DS2208 {runId}` tampil di daftar Assets
141. Verifikasi aksi `Report Missing` tidak tampil (Hidden) pada baris `Scanner Zebra DS2208 {runId}` di daftar Assets
142. Klik `Scanner Zebra DS2208 {runId}` pada kolom Name
143. Verifikasi Asset Status pada Asset Detail `Assigned`
144. Verifikasi tombol `[Report Missing]` tidak tampil (Hidden) pada Asset Detail

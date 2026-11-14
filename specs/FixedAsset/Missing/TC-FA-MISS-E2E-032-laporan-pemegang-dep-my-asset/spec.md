---
id: TC-FA-MISS-E2E-032-laporan-pemegang-dep-my-asset
title: "Laporan pemegang dari My Asset: Waiting for Confirmation, Cancel Report menjadi Canceled, status laporan di baris My Asset"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.1#r6", "§9.2#b32", "§3#p4", "§7.3#r6", "§7.3#r11", "§7.2#r3", "§7.2#r18", "§4.2.4#p7", "§9.6#r7", "§9.7#r2", "§9.7#r8", "§9.2#r1", "§9.2#r8", "§8.1#r7", "§8.1#r8", "§1.2#r17", "§1.2#r19", "§1.2#r52", "§1.2#r54", "§1.2#r56", "§1.2#r57", "§1.2#r69", "§1.2#r70", "§1.2#r118", "§1.2#r119", "§2#b3", "§2.1#r3", "§2.1#r8", "§2.1#b4", "§4.8#r3", "§4.8#r7", "§9.11#r3", "§9.4.2#r27", "§9.4.2#r22", "§9.2#b34", "§9.4.4#r18", "§9.4.4#r20", "§9.4.3#b5", "§11#r4", "§4.2.3#p2", "§4.2.4#r15", "§9.9#r1", "§9.8#r2", "§9.6#r1", "EB-FB-1@report-missing-pemegang", "EB-FB-1@cancel-report", "EB-FB-2@go-back-cancel-report", "§9.3#b1", "§4.6#b3", "§4.6#b6"]
smoke: []
dependsOn: ["My Asset: tab Borrowed", "My Asset: tab Assigned", "My Asset: aksi Cancel Report"]
trace:
  "§9.1#r6": [10, 28]
  "§9.2#b32": [28, 40, 41, 66]
  "§3#p4": [10, 20]
  "§7.3#r6": [9, 39]
  "§7.3#r11": [19, 73]
  "§7.2#r3": [14]
  "§7.2#r18": [32]
  "§4.2.4#p7": [14]
  "§9.6#r7": [19, 32]
  "§9.7#r2": [4, 11, 94, 95]
  "§9.7#r8": [21, 107, 108]
  "§9.2#r1": [10, 56]
  "§9.2#r8": [20, 73]
  "§8.1#r7": [47]
  "§8.1#r8": [52]
  "§1.2#r17": [10]
  "§1.2#r19": [20]
  "§1.2#r52": [1]
  "§1.2#r54": [10, 11]
  "§1.2#r56": [12]
  "§1.2#r57": [20, 21]
  "§1.2#r69": [57]
  "§1.2#r70": [70, 73]
  "§1.2#r118": [41]
  "§1.2#r119": [70]
  "§2#b3": [66]
  "§2.1#r3": [1, 9]
  "§2.1#r8": [12]
  "§2.1#b4": [12, 112]
  "§4.8#r3": [1]
  "§4.8#r7": [12, 75, 84, 86, 89]
  "§9.11#r3": [22, 23]
  "§9.4.2#r27": [62, 66, 68]
  "§9.4.2#r22": [56]
  "§9.2#b34": [56]
  "§9.4.4#r18": [40, 41, 97, 102]
  "§9.4.4#r20": [56]
  "§9.4.3#b5": [56]
  "§11#r4": [1]
  "§4.2.3#p2": [3]
  "§4.2.4#r15": [36]
  "§9.9#r1": [6]
  "§9.8#r2": [9]
  "§9.6#r1": [9, 39]
  "EB-FB-1@report-missing-pemegang": [9, 39]
  "EB-FB-1@cancel-report": [19]
  "EB-FB-2@go-back-cancel-report": [16, 80, 81]
  "§9.3#b1": [12]
  "§4.6#b3": [3]
  "§4.6#b6": [22, 23]
anchor: [74, 78, 83, 85, 88, 106, 111]
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
4. Verifikasi kotak dampak memuat baris `The asset admins will review your report. Until then, reminders are paused.`
5. Klik `[Report Missing]` pada dialog tanpa mengisi What happened
6. Verifikasi caption `What happened must not be empty` tampil di bawah isian What happened
7. Isi What happened `Scanner tidak ada di loker setelah shift malam`
8. Klik `[Report Missing]` pada dialog
9. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil
10. Verifikasi status laporan pada baris `Scanner Zebra DS2208 {runId}` `Waiting for Confirmation`
11. Verifikasi Asset Status pada baris `Scanner Zebra DS2208 {runId}` `Missing`
12. Verifikasi aksi `Cancel Report` tampil pada baris `Scanner Zebra DS2208 {runId}`

### Pemegang membatalkan laporan sendiri: Go Back lalu Cancel Report
13. Buka aksi Cancel Report pada `Scanner Zebra DS2208 {runId}` di My Asset
14. Verifikasi dialog `Cancel Report` memuat bullet `Scanner Zebra DS2208 {runId}` dan pertanyaan `Are you sure you want to cancel it?`
15. Klik `[Go Back]`
16. Verifikasi status laporan pada baris `Scanner Zebra DS2208 {runId}` tetap `Waiting for Confirmation`
17. Buka aksi Cancel Report pada `Scanner Zebra DS2208 {runId}` di My Asset
18. Klik `[Cancel Report]` pada dialog
19. Verifikasi toast `Success, report has been canceled.` tampil
20. Verifikasi status laporan pada baris `Scanner Zebra DS2208 {runId}` `Canceled`
21. Verifikasi aksi `Report Missing` tampil kembali pada baris `Scanner Zebra DS2208 {runId}`

### Status laporan Rejected beserta reason tampil di baris pemegang
22. Verifikasi status laporan pada baris `Camera Canon EOS {runId}` `Rejected`
23. Verifikasi reason `Aset terlihat di gudang cabang` tampil pada baris `Camera Canon EOS {runId}`

### Laporan dari tab Borrowed lalu Cancel Report atas record yang sudah berubah
24. Klik tab `Borrowed`
25. Buka aksi Report Missing pada `Handheld Honeywell CT60 {runId}` di My Asset
26. Isi What happened `Handheld tertinggal di kendaraan operasional`
27. Klik `[Report Missing]` pada dialog
28. Verifikasi status laporan pada baris `Handheld Honeywell CT60 {runId}` `Waiting for Confirmation`
29. Rina W melakukan Confirm atas laporan `Handheld Honeywell CT60 {runId}`, sementara daftar My Asset `Joko Santoso {runId}` belum dimuat ulang dan baris itu masih menampilkan status `Waiting for Confirmation`
30. Buka aksi Cancel Report pada `Handheld Honeywell CT60 {runId}` di My Asset
31. Klik `[Cancel Report]` pada dialog
32. Verifikasi dialog `Already Changed` memuat teks `This record was changed by Rina W. Reload to see the latest status.`
33. Klik `[Reload]`

### PIC melaporkan atas nama karyawan tanpa akun
34. Masuk sebagai `Rudi Hartono {runId}`
35. Buka aksi Report Missing pada `Projector Epson EB-X06 {runId}` di My Asset
36. Verifikasi kotak dampak memuat baris pemegang `Dedi Kurniawan {runId}` diikuti `and the asset admins will be notified.`
37. Isi What happened `Projector hilang dari ruang rapat setelah acara`
38. Klik `[Report Missing]` pada dialog
39. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil
40. Verifikasi status laporan pada baris `Projector Epson EB-X06 {runId}` `Waiting for Confirmation`
41. Verifikasi aksi `Cancel Report` tampil bagi PIC pada baris `Projector Epson EB-X06 {runId}`

### Node laporan di Missing Log atas laporan PIC dan laporan yang dibatalkan
42. Masuk sebagai `Rina W`
43. Buka halaman `Assets`
44. Klik tab `Missing`
45. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
46. Klik `Projector Epson EB-X06 {runId}` pada kolom Name
47. Verifikasi dialog Missing Log memuat node `Reported missing by` oleh `Rudi Hartono {runId}` atas nama `Dedi Kurniawan {runId}`
48. Tutup dialog Missing Log dengan `✕`
49. Klik sub-tab `History`
50. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
51. Klik `Scanner Zebra DS2208 {runId}` pada kolom Name
52. Verifikasi dialog Missing Log memuat node `Report canceled by` oleh `Joko Santoso {runId}`
53. Tutup dialog Missing Log dengan `✕`

### Laporan yang menunggu lama tidak ditutup otomatis dan diputuskan Aktor Missing
54. Klik sub-tab `Active`
55. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
56. Verifikasi baris `Printer HP LaserJet M404 {runId}` berstatus `Waiting for Confirmation`
57. Verifikasi aksi `Review` tampil pada baris `Printer HP LaserJet M404 {runId}`

### Pemegang dengan hak Aktor Missing melapor sebagai Pelapor admin
58. Masuk sebagai `Andi Pratama {runId}`
59. Buka aksi Report Missing pada `Laptop Lenovo ThinkPad T14 {runId}` di My Asset
60. Isi What happened `Laptop tidak ada di meja setelah perjalanan dinas`
61. Klik `[Report Missing]` pada dialog
62. Verifikasi toast `Success, asset has been reported missing.` tampil
63. Buka halaman `Assets`
64. Klik tab `Missing`
65. Ketik Search `Laptop Lenovo ThinkPad T14 {runId}`, tekan Enter
66. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId}` berstatus `Missing`
67. Buka menu `⋯` pada baris `Laptop Lenovo ThinkPad T14 {runId}`
68. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada aksi `Mark as Found` yang disabled

### PIC pengganti membatalkan laporan PIC sebelumnya
69. Masuk sebagai `Wulan Sari {runId}`
70. Verifikasi aksi `Cancel Report` tampil pada baris `Monitor LG 27UL500 {runId}`
71. Buka aksi Cancel Report pada `Monitor LG 27UL500 {runId}` di My Asset
72. Klik `[Cancel Report]` pada dialog
73. Verifikasi status laporan pada baris `Monitor LG 27UL500 {runId}` `Canceled`

### Cancel Report tidak tampil pada laporan PIC pengganti yang sudah Canceled
74. Verifikasi status laporan pada baris `Monitor LG 27UL500 {runId}` `Canceled`
75. Verifikasi aksi `Cancel Report` tidak tampil pada baris `Monitor LG 27UL500 {runId}`

### Go Back menutup dialog Cancel Report tanpa toast
76. Masuk sebagai `Rudi Hartono {runId}`
77. Buka aksi Cancel Report pada `Projector Epson EB-X06 {runId}` di My Asset
78. Verifikasi dialog `Cancel Report` memuat bullet `Projector Epson EB-X06 {runId}`
79. Klik `[Go Back]`
80. Verifikasi dialog `Cancel Report` tertutup
81. Verifikasi tidak ada toast yang tampil

### Cancel Report tidak tampil pada laporan Rejected, Canceled, dan yang sudah menjadi Missing
82. Masuk sebagai `Joko Santoso {runId}`
83. Verifikasi status laporan pada baris `Camera Canon EOS {runId}` `Rejected`
84. Verifikasi aksi `Cancel Report` tidak tampil pada baris `Camera Canon EOS {runId}`
85. Verifikasi status laporan pada baris `Scanner Zebra DS2208 {runId}` `Canceled`
86. Verifikasi aksi `Cancel Report` tidak tampil pada baris `Scanner Zebra DS2208 {runId}`
87. Klik tab `Borrowed`
88. Verifikasi Asset Status pada baris `Handheld Honeywell CT60 {runId}` `Missing`
89. Verifikasi aksi `Cancel Report` tidak tampil pada baris `Handheld Honeywell CT60 {runId}`

### Asset Detail: status global dan Transaction log atas laporan dari My Asset, dan status sesudah Cancel Report
90. Masuk sebagai `Rina W`
91. Buka halaman `Assets`
92. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
93. Klik `Projector Epson EB-X06 {runId}` pada kolom Name
94. Verifikasi Asset Status pada Asset Detail `Missing`
95. Verifikasi banner `Reported missing on` tampil pada Asset Detail
96. Buka Transaction log pada Asset Detail
97. Verifikasi entri `Reported missing` tampil di Transaction log
98. Buka halaman `Assets`
99. Ketik Search `Laptop Lenovo ThinkPad T14 {runId}`, tekan Enter
100. Klik `Laptop Lenovo ThinkPad T14 {runId}` pada kolom Name
101. Buka Transaction log pada Asset Detail
102. Verifikasi entri `Reported missing` tampil di Transaction log
103. Buka halaman `Assets`
104. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
105. Klik `Scanner Zebra DS2208 {runId}` pada kolom Name
106. Verifikasi tombol `[Report Missing]` tampil pada Asset Detail
107. Verifikasi Asset Status pada Asset Detail bukan `Missing`
108. Verifikasi banner `Reported missing on` tidak tampil pada Asset Detail

### Pemegang tanpa hak Aktor Missing tidak mendapat tab Missing
109. Masuk sebagai `Joko Santoso {runId}`
110. Buka halaman `Assets`
111. Verifikasi tab `Assets` tampil pada halaman Assets
112. Verifikasi tab `Missing` tidak tampil pada halaman Assets

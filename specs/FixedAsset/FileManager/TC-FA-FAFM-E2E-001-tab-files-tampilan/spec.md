---
id: TC-FA-FAFM-E2E-001-tab-files-tampilan
title: "Halaman File Manager: tab Kategori dan isi baris tab Files"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["F-FAFM-01a", "F-FAFM-01c", "F-FAFM-01d", "FAFM-LOGIC-01a", "FAFM-LOGIC-01b", "FAFM-LOGIC-01f", "FAFM-LOGIC-05e", "FAFM-LOGIC-08g", "INV-01b", "INV-01c", "INV-01d", "INV-01e", "INV-01f", "INV-01g", "INV-01h", "INV-11e", "INV-11f", "KAT-01", "KAT-02", "KAT-03", "KAT-04", "KAT-05", "KAT-06", "KAT-07", "KAT-08", "KAT-09", "T-FAFM-01", "TBL-01a", "TBL-01b", "TBL-01d", "§4.1#p6", "§4.1a#p13", "§4.2d#p3", "§4.4#b5"]
smoke: []
dependsOn: []
trace:
  "F-FAFM-01a": 3
  "F-FAFM-01c": [10, 41, 54, 57]
  "F-FAFM-01d": [31, 33, 34, 36, 41]
  "FAFM-LOGIC-01a": 15
  "FAFM-LOGIC-01b": 16
  "FAFM-LOGIC-01f": [17, 18, 19]
  "FAFM-LOGIC-05e": [14, 19]
  "FAFM-LOGIC-08g": 10
  "INV-01b": 1
  "INV-01c": 4
  "INV-01d": 4
  "INV-01e": 73
  "INV-01f": 75
  "INV-01g": [12, 22, 23]
  "INV-01h": [15, 19]
  "INV-11e": 26
  "INV-11f": 23
  "KAT-01": 10
  "KAT-02": [31, 41]
  "KAT-03": [44, 45]
  "KAT-04": 48
  "KAT-05": [52, 53]
  "KAT-06": 57
  "KAT-07": [61, 62, 63]
  "KAT-08": [63, 66, 67, 68]
  "KAT-09": [71, 72]
  "T-FAFM-01": [11, 30, 32, 33, 34, 35, 36, 37, 38, 39, 49, 58, 80, 83, 87, 92, 95, 99, 104, 107, 111]
  "TBL-01a": 12
  "TBL-01b": 14
  "TBL-01d": [13, 76]
  "§4.1#p6": [17, 18]
  "§4.1a#p13": [20, 21]
  "§4.2d#p3": [4, 5, 6, 7, 8, 11, 49, 58]
  "§4.4#b5": [40, 115, 118]
anchor: [25, 79, 82, 86, 91, 94, 98, 103, 106, 110]
coverage:
  web: automated
---

# Halaman File Manager: tab Kategori dan isi baris tab Files

## Prerequisites
- Aktor: Total Control, user `Budi Santoso` (tampil `Budi S`).
- Layar awal: halaman utama Fixed Asset (FAMS) dengan Sidebar.
- Data:
  - Group `Head Office`, `Branch Bandung`, dan `Fleet` ada di entitas aktor.
  - DU-001-1: File `laptop-front-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Laptop Dell Latitude 5420 {runId}` (status Active), Group `Head Office`, Size `820.4 KB`, Uploaded By `Budi S`.
  - DU-001-2: File `warranty-card-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Size `310.0 KB`, Uploaded By `Budi S`.
  - DU-001-3: File `warranty-scan-{runId}.pdf`, File Format `PDF`, Source `Custom Field Document`, Reference `Warranty Card`, Asset `Scanner Epson DS-530 {runId}` (status Unmanaged), Group `Branch Bandung`, Size `300.0 KB`, Uploaded By `Budi S`.
  - DU-001-4: File `damage-01-{runId}.jpg`, File Format `JPG`, Source `Damaged Photo`, Asset `Toyota Avanza {runId}` (status Active), Group `Fleet`, Size `900.0 KB`, Uploaded By `Budi S`.
  - DU-001-5: File `repair-02-{runId}.jpg`, File Format `JPG`, Source `Repair Photo`, Asset `Toyota Avanza {runId}`, Group `Fleet`, Size `880.0 KB`, Uploaded By `Budi S`.
  - DU-001-6: File `found-01-{runId}.jpg`, File Format `JPG`, Source `Found Photo`, Asset `Toyota Avanza {runId}`, Group `Fleet`, Size `700.0 KB`, Uploaded By `Budi S`.
  - DU-001-7: File `maint-before-{runId}.jpg`, File Format `JPG`, Source `Maintenance Before Photo`, Asset `Printer HP M404 {runId}` (status Disposed), Group `Branch Bandung`, Size `750.0 KB`, Uploaded By `Budi S`.
  - DU-001-8: File `maint-after-{runId}.jpg`, File Format `JPG`, Source `Maintenance After Photo`, Asset `Printer HP M404 {runId}`, Group `Branch Bandung`, Size `1.9 MB`, Uploaded By `Budi S`.
  - DU-001-9: File `dsp-auction-receipt-{runId}.pdf`, File Format `PDF`, Source `Disposal Document`, Asset `Printer HP M404 {runId}`, Group `Branch Bandung`, Size `3.2 MB`, Uploaded By `Budi S`.
  - DU-001-10: File `handover-brw-{runId}.jpg`, File Format `JPG`, Source `Handover Photo` (diunggah lewat Borrow), Asset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Size `640.0 KB`, Uploaded By `Budi S`.
  - DU-001-11: File `return-brw-{runId}.jpg`, File Format `JPG`, Source `Return Photo` (diunggah lewat Borrow), Asset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Size `610.0 KB`, Uploaded By `Budi S`.
  - DU-001-12: File `handover-asg-{runId}.jpg`, File Format `JPG`, Source `Handover Photo` (diunggah lewat Assignment), Asset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Size `630.0 KB`, Uploaded By `Budi S`.
  - DU-001-13: File `return-asg-{runId}.jpg`, File Format `JPG`, Source `Return Photo` (diunggah lewat Assignment), Asset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Size `600.0 KB`, Uploaded By `Budi S`.
  - DU-001-14: File `send-trf-{runId}.jpg`, File Format `JPG`, Source `Send Photo`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Size `560.0 KB`, Uploaded By `Budi S`.
  - DU-001-15: File `receive-trf-{runId}.jpg`, File Format `JPG`, Source `Receive Photo`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Size `570.0 KB`, Uploaded By `Budi S`.
  - DU-001-16: File `maint-before-old-{runId}.jpg`, File Format `JPG`, Source `Maintenance Before Photo`, Asset `Printer HP M404 {runId}`, Group `Branch Bandung`, Size `700.0 KB`, Uploaded By `Budi S`, sudah di-soft-delete (ada di Recycle Bin).
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `HH:mm`.

## Test Steps

### Menu File Manager membuka halaman
1. Verifikasi menu `File Manager` ada pada grup `Settings` di Sidebar FAMS
2. Klik menu `File Manager` pada grup `Settings` di Sidebar FAMS
3. Verifikasi halaman File Manager tampil

### Tab Kategori dan tab Disposed & Unmanaged Assets tampil berurutan
4. Verifikasi tab tampil berurutan: `Asset Photo`, `Asset Documents`, `Damaged`, `Missing`, `Maintenance`, `Disposal`, `Borrow`, `Assignment`, `Transfer`, lalu `Disposed & Unmanaged Assets`
5. Verifikasi tab `Asset Photo` aktif saat halaman dibuka
6. Verifikasi tidak ada tab yang menggabungkan semua file
7. Verifikasi label tab `Asset Photo` memuat total ukuran file dalam tanda kurung sesudah nama Kategori
8. Verifikasi label tab `Disposed & Unmanaged Assets` memuat total ukuran dalam tanda kurung sesudah namanya

### Tab Asset Photo menampilkan file aset Active tanpa kolom Source dan Reference
9. Ketik Search `{runId}`, tekan Enter
10. Verifikasi baris `laptop-front-{runId}.jpg` tampil
11. Verifikasi kolom `Source` dan `Reference` tidak tampil di tab `Asset Photo`

### Toolbar dan aksi baris tidak membuat, mengubah, atau mengunggah file
12. Verifikasi toolbar tabel memuat `Search`, `Filter`, dan `Download`
13. Verifikasi tombol `Changelog` dan `Recycle Bin` tampil di header kartu Storage Usage
14. Verifikasi tidak ada tombol `Create` pada toolbar tabel
15. Verifikasi tidak ada kontrol untuk mengunggah file di halaman File Manager
16. Verifikasi tidak ada kontrol untuk memilih file yang sudah ada guna dilampirkan ke record lain
17. Verifikasi aksi baris `laptop-front-{runId}.jpg` memuat `Download`
18. Verifikasi aksi baris `laptop-front-{runId}.jpg` memuat `Delete`
19. Verifikasi tidak ada aksi `Edit` pada baris `laptop-front-{runId}.jpg`
20. Verifikasi tidak ada aksi `Detail` pada baris `laptop-front-{runId}.jpg`
21. Verifikasi tidak ada tombol di halaman untuk menjalankan auto-transition, cascade purge, auto-purge, atau perhitungan Storage
22. Verifikasi pagination tampil di bawah tabel
23. Verifikasi checkbox seleksi tampil pada baris `laptop-front-{runId}.jpg`

### Checkbox dan Actions bukan kolom data
24. Klik header kolom `Actions` (`⋯`) pada tabel
25. Verifikasi daftar kolom pada panel Column Visibility memuat `File Name`
26. Verifikasi daftar kolom pada panel Column Visibility tidak memuat `Checkbox` dan `Actions`
27. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility

### Tab Asset Documents menampilkan kolom dan isi baris dari data nyata
28. Klik tab `Asset Documents`
29. Ketik Search `{runId}`, tekan Enter
30. Verifikasi header kolom tabel: `File Name`, `File Format`, `Source`, `Reference`, `Asset`, `Asset ID`, `Group`, `Size`, `Uploaded By`, dan `Upload Date`
31. Verifikasi baris `warranty-card-{runId}.pdf` tampil dengan Source `Attachment`
32. Verifikasi File Format baris `warranty-card-{runId}.pdf` bernilai `PDF`
33. Verifikasi Reference baris `warranty-card-{runId}.pdf` bernilai `General`
34. Verifikasi Asset baris `warranty-card-{runId}.pdf` tampil sebagai `[Asset Name] - [Increment]` dari aset `Laptop Dell Latitude 5420 {runId}`
35. Verifikasi Asset ID baris `warranty-card-{runId}.pdf` tampil terisi dengan Asset ID milik aset `Laptop Dell Latitude 5420 {runId}`
36. Verifikasi Group baris `warranty-card-{runId}.pdf` bernilai `Head Office`
37. Verifikasi Size baris `warranty-card-{runId}.pdf` bernilai `310.0 KB`
38. Verifikasi Uploaded By baris `warranty-card-{runId}.pdf` bernilai `Budi S`
39. Verifikasi Upload Date baris `warranty-card-{runId}.pdf` tampil mengikuti Date Format dan Time Format yang berlaku
40. Verifikasi Asset dan Reference baris `warranty-card-{runId}.pdf` berupa teks biasa dan bukan tautan
41. Verifikasi baris `warranty-scan-{runId}.pdf` milik aset Unmanaged tampil dengan Source `Custom Field Document` dan Reference `Warranty Card`

### Tab Damaged memuat file Damaged Photo dan Repair Photo
42. Klik tab `Damaged`
43. Ketik Search `{runId}`, tekan Enter
44. Verifikasi baris `damage-01-{runId}.jpg` tampil dengan Source `Damaged Photo`
45. Verifikasi baris `repair-02-{runId}.jpg` tampil dengan Source `Repair Photo`

### Tab Missing memuat file Found Photo tanpa kolom Source
46. Klik tab `Missing`
47. Ketik Search `{runId}`, tekan Enter
48. Verifikasi baris `found-01-{runId}.jpg` tampil
49. Verifikasi kolom `Source` tidak tampil di tab `Missing`

### Tab Maintenance memuat file Maintenance Before dan After Photo yang belum soft-deleted
50. Klik tab `Maintenance`
51. Ketik Search `{runId}`, tekan Enter
52. Verifikasi baris `maint-before-{runId}.jpg` tampil dengan Source `Maintenance Before Photo`
53. Verifikasi baris `maint-after-{runId}.jpg` tampil dengan Source `Maintenance After Photo`
54. Verifikasi baris `maint-before-old-{runId}.jpg` yang sudah di-soft-delete tidak tampil

### Tab Disposal memuat dokumen aset Disposed tanpa kolom Source
55. Klik tab `Disposal`
56. Ketik Search `{runId}`, tekan Enter
57. Verifikasi baris `dsp-auction-receipt-{runId}.pdf` milik aset Disposed tampil
58. Verifikasi kolom `Source` tidak tampil di tab `Disposal`

### Tab Borrow memuat foto Handover dan Return dari Borrow saja
59. Klik tab `Borrow`
60. Ketik Search `{runId}`, tekan Enter
61. Verifikasi baris `handover-brw-{runId}.jpg` tampil dengan Source `Handover Photo`
62. Verifikasi baris `return-brw-{runId}.jpg` tampil dengan Source `Return Photo`
63. Verifikasi baris `handover-asg-{runId}.jpg` tidak tampil di tab `Borrow`

### Tab Assignment memuat foto Handover dan Return dari Assignment saja
64. Klik tab `Assignment`
65. Ketik Search `{runId}`, tekan Enter
66. Verifikasi baris `handover-asg-{runId}.jpg` tampil dengan Source `Handover Photo`
67. Verifikasi baris `return-asg-{runId}.jpg` tampil dengan Source `Return Photo`
68. Verifikasi baris `handover-brw-{runId}.jpg` tidak tampil di tab `Assignment`

### Tab Transfer memuat Send Photo dan Receive Photo
69. Klik tab `Transfer`
70. Ketik Search `{runId}`, tekan Enter
71. Verifikasi baris `send-trf-{runId}.jpg` tampil dengan Source `Send Photo`
72. Verifikasi baris `receive-trf-{runId}.jpg` tampil dengan Source `Receive Photo`
73. Verifikasi tab `Transfer` sebagai tab Kategori memuat tabel file dengan toolbar `Search`, `Filter`, dan `Download`

### Tab Disposed & Unmanaged Assets adalah tab Asset Data
74. Klik tab `Disposed & Unmanaged Assets`
75. Verifikasi tab `Disposed & Unmanaged Assets` memuat tabel aset dengan header kolom `Name` dan `Status`
76. Verifikasi tombol `Changelog` dan `Recycle Bin` tetap tampil di header kartu Storage Usage

### Panel kolom dan Filter Panel tab Asset Photo tanpa kolom Source dan Reference
77. Klik tab `Asset Photo`
78. Klik header kolom `Actions` (`⋯`) pada tabel
79. Verifikasi daftar kolom pada panel Column Visibility memuat `File Name`
80. Verifikasi daftar kolom pada panel Column Visibility tidak memuat `Source` dan `Reference`
81. Klik `Setup Column...` pada panel Column Visibility
82. Verifikasi daftar kolom pada modal `Setup Column` memuat `File Name`
83. Verifikasi daftar kolom pada modal `Setup Column` tidak memuat `Source` dan `Reference`
84. Klik `[✕]` pada modal `Setup Column`
85. Klik ikon Filter
86. Verifikasi panel Filter tampil dengan field `File Format`
87. Verifikasi tidak ada field filter untuk `Source` dan `Reference`
88. Klik ikon Filter

### Panel kolom dan Filter Panel tab Missing tanpa kolom Source
89. Klik tab `Missing`
90. Klik header kolom `Actions` (`⋯`) pada tabel
91. Verifikasi daftar kolom pada panel Column Visibility memuat `File Name`
92. Verifikasi daftar kolom pada panel Column Visibility tidak memuat `Source`
93. Klik `Setup Column...` pada panel Column Visibility
94. Verifikasi daftar kolom pada modal `Setup Column` memuat `File Name`
95. Verifikasi daftar kolom pada modal `Setup Column` tidak memuat `Source`
96. Klik `[✕]` pada modal `Setup Column`
97. Klik ikon Filter
98. Verifikasi panel Filter tampil dengan field `File Format`
99. Verifikasi tidak ada field filter untuk `Source`
100. Klik ikon Filter

### Panel kolom dan Filter Panel tab Disposal tanpa kolom Source
101. Klik tab `Disposal`
102. Klik header kolom `Actions` (`⋯`) pada tabel
103. Verifikasi daftar kolom pada panel Column Visibility memuat `File Name`
104. Verifikasi daftar kolom pada panel Column Visibility tidak memuat `Source`
105. Klik `Setup Column...` pada panel Column Visibility
106. Verifikasi daftar kolom pada modal `Setup Column` memuat `File Name`
107. Verifikasi daftar kolom pada modal `Setup Column` tidak memuat `Source`
108. Klik `[✕]` pada modal `Setup Column`
109. Klik ikon Filter
110. Verifikasi panel Filter tampil dengan field `File Format`
111. Verifikasi tidak ada field filter untuk `Source`
112. Klik ikon Filter

### Name aset di tab Disposed & Unmanaged Assets berupa teks biasa
113. Klik tab `Disposed & Unmanaged Assets`
114. Ketik Search `{runId}`, tekan Enter
115. Verifikasi Name baris `Printer HP M404 {runId}` berupa teks biasa dan bukan tautan

### Asset di Recycle Bin berupa teks biasa
116. Klik `Recycle Bin` pada header kartu `Storage Usage`
117. Ketik Search `maint-before-old-{runId}`, tekan Enter
118. Verifikasi Asset baris `maint-before-old-{runId}.jpg` berupa teks biasa dan bukan tautan
119. Tutup modal `Recycle Bin`

---
id: TC-FA-FAFM-E2E-011-recycle-bin-dialog
title: "Recycle Bin: isi, konfigurasi tabel, dan tanpa Recover atau Empty All"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["F-FAFM-03a", "F-FAFM-03b", "F-FAFM-03c", "FAFM-LOGIC-03b", "FAFM-LOGIC-03c", "INV-05b", "INV-05d", "INV-05e", "INV-05f", "INV-11f", "T-FAFM-03", "TBL-03a", "TBL-04c", "TBL-05c", "§4.1#p15", "§4.1a#p8", "§9.4.3#b6", "EB-SRC-5@tabel-recycle-bin"]
smoke: []
dependsOn: []
trace:
  "F-FAFM-03a": 2
  "F-FAFM-03b": [4, 5, 6, 11, 13]
  "F-FAFM-03c": [7, 8, 9, 10, 69]
  "FAFM-LOGIC-03b": [23, 28]
  "FAFM-LOGIC-03c": [23, 30]
  "INV-05b": 2
  "INV-05d": [15, 83, 84]
  "INV-05e": [15, 32, 40]
  "INV-05f": [15, 17]
  "INV-11f": 19
  "T-FAFM-03": [4, 5, 6, 7, 8, 9, 10, 32, 33, 34, 36, 40, 41, 46, 47, 52, 53, 56, 57, 60, 61, 64, 69, 70, 75, 76, 79, 83, 84, 86, 87, 102, 105, 109, 113, 115, 117, 120]
  "TBL-03a": [32, 33]
  "TBL-04c": [11, 13]
  "TBL-05c": [19, 22, 27]
  "§4.1#p15": 27
  "§4.1a#p8": 2
  "§9.4.3#b6": [23, 28, 30]
  "EB-SRC-5@tabel-recycle-bin": [93, 98]
anchor: [4, 15, 22, 27, 32, 36, 40, 46, 52, 56, 60, 69, 75, 83, 86, 91]
coverage:
  web: automated
---

# Recycle Bin: isi, konfigurasi tabel, dan tanpa Recover atau Empty All

## Prerequisites
- Aktor: Total Control, user `Bagus Prasetyo {runId}` (tampil `Bagus P`), akun aktif dengan kredensial disediakan fase 2.
- Layar awal: halaman Settings > File Manager.
- Data:
  - Group `Kantor Pusat {runId}` (DU-011-1) dan `Cabang Surabaya {runId}` (DU-011-2) ada di entitas aktor.
  - Aset `Genset Perkins 404 {runId}` (Group `Kantor Pusat {runId}`), `Truk Mitsubishi Fuso {runId}` (Group `Cabang Surabaya {runId}`), dan `Mesin Bubut Krisbow {runId}` (Group `Kantor Pusat {runId}`) ada di entitas aktor; semua file di bawah sudah di-soft-delete dan berada di Recycle Bin.
  - DU-011-3: File File Name `kontrak-lama-{runId}.pdf`, File Format `PDF`, Category `Asset Documents`, Source `Attachment`, Asset `Genset Perkins 404 {runId}`, Group `Kantor Pusat {runId}`, Size `1.0 MB`, Deleted Date `T0 − 5 hari`, Deleted By `Bagus P`, Auto-Purge In `25 days`, dari Deleted Date dan Retensi Recycle Bin `30 hari`.
  - DU-011-4: File File Name `panduan-genset-{runId}.pdf`, File Format `PDF`, Category `Asset Documents`, Source `Custom Field Document`, Asset `Genset Perkins 404 {runId}`, Group `Kantor Pusat {runId}`, Size `500.0 KB`, Deleted Date `T0 − 6 hari`, Deleted By `Bagus P`, Auto-Purge In `24 days`, dari Deleted Date dan Retensi Recycle Bin `30 hari`.
  - DU-011-5: File File Name `foto-kerusakan-truk-{runId}.jpg`, File Format `JPG`, Category `Damaged`, Source `Damaged Photo`, Asset `Truk Mitsubishi Fuso {runId}`, Group `Cabang Surabaya {runId}`, Size `900.0 KB`, Deleted Date `T0 − 20 hari`, Deleted By `System`, Auto-Purge In `10 days`, dari Deleted Date dan Retensi Recycle Bin `30 hari`.
  - DU-011-6: File File Name `foto-perbaikan-truk-{runId}.jpg`, File Format `JPG`, Category `Damaged`, Source `Repair Photo`, Asset `Truk Mitsubishi Fuso {runId}`, Group `Cabang Surabaya {runId}`, Size `750.0 KB`, Deleted Date `T0 − 28 hari`, Deleted By `Bagus P`, Auto-Purge In `2 days`, dari Deleted Date dan Retensi Recycle Bin `30 hari`.
  - DU-011-7: File File Name `foto-sebelum-servis-{runId}.jpg`, File Format `JPG`, Category `Maintenance`, Source `Maintenance Before Photo`, Asset `Mesin Bubut Krisbow {runId}`, Group `Kantor Pusat {runId}`, Size `1.2 MB`, Deleted Date `T0 − 29 hari`, Deleted By `System`, Auto-Purge In `1 day`, dari Deleted Date dan Retensi Recycle Bin `30 hari`.
  - DU-011-8: delapan file File Name `arsip-{n}-{runId}.pdf` untuk n dari 1 sampai 8, File Format `PDF`, Category `Asset Documents`, Source `Attachment`, Asset `Genset Perkins 404 {runId}`, Group `Kantor Pusat {runId}`, Size `100.0 KB`, Deleted Date `T0 − 3 hari`, Deleted By `System`, Auto-Purge In `27 days`, dari Deleted Date dan Retensi Recycle Bin `30 hari`.
  - Deleted Date ditulis relatif terhadap waktu baca tanpa jam, dan Auto-Purge In dibulatkan ke atas dari sisa waktu menuju batas purge: `T0 − 5 hari` menjadi `25 days`, `T0 − 6 hari` menjadi `24 days`, sehingga DU-011-3 dan DU-011-4 tidak bernilai sama.
  - Himpunan file ber-runId di Recycle Bin seluruhnya berjumlah 13: DU-011-3 sampai DU-011-7 dan delapan file DU-011-8.
- Kondisi:
  - Retensi Recycle Bin bernilai `30 hari`.
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `HH:mm`.

## Test Steps

### Recycle Bin dibuka dari header kartu Storage Usage dan memuat file soft-deleted
1. Klik `Recycle Bin` pada header kartu `Storage Usage`
2. Verifikasi modal `Recycle Bin` tampil
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi Pagination menampilkan total `13` baris dalam `2` halaman
5. Verifikasi baris `kontrak-lama-{runId}.pdf` memuat Category `Asset Documents`, Source `Attachment`, Asset `Genset Perkins 404 {runId}`, Group `Kantor Pusat {runId}`, Size `1.0 MB`, dan Deleted By `Bagus P`
6. Verifikasi baris `foto-kerusakan-truk-{runId}.jpg` memuat Category `Damaged`, Source `Damaged Photo`, Asset `Truk Mitsubishi Fuso {runId}`, Group `Cabang Surabaya {runId}`, Size `900.0 KB`, dan Deleted By `System`
7. Verifikasi Auto-Purge In baris `kontrak-lama-{runId}.pdf` adalah `25 days`
8. Verifikasi Auto-Purge In baris `foto-kerusakan-truk-{runId}.jpg` adalah `10 days`
9. Verifikasi Auto-Purge In baris `foto-perbaikan-truk-{runId}.jpg` adalah `2 days`
10. Verifikasi Auto-Purge In baris `foto-sebelum-servis-{runId}.jpg` adalah `1 day`

### Urutan default Deleted Date terbaru lintas halaman
11. Verifikasi baris `kontrak-lama-{runId}.pdf` berada di urutan kesembilan dan baris `panduan-genset-{runId}.pdf` di urutan kesepuluh pada halaman 1
12. Klik halaman `2` pada Pagination
13. Verifikasi halaman 2 memuat tiga baris dari atas ke bawah: `foto-kerusakan-truk-{runId}.jpg`, `foto-perbaikan-truk-{runId}.jpg`, `foto-sebelum-servis-{runId}.jpg`
14. Klik halaman `1` pada Pagination

### Toolbar Search, Filter, Download, kotak centang, dan aksi hanya Permanently Delete
15. Verifikasi toolbar modal memuat ikon Search, Filter, dan Download
16. Klik ikon Download pada modal `Recycle Bin`
17. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil pada modal `Recycle Bin`
18. Tutup pilihan Download
19. Verifikasi kotak centang ada pada header tabel dan pada baris `kontrak-lama-{runId}.pdf`
20. Centang baris `kontrak-lama-{runId}.pdf`
21. Centang baris `panduan-genset-{runId}.pdf`
22. Verifikasi bar aksi bulk memuat aksi `Permanently Delete`
23. Verifikasi bar aksi bulk tidak memuat aksi `Recover`, `Restore`, dan `Empty All`
24. Hilangkan centang baris `kontrak-lama-{runId}.pdf`
25. Hilangkan centang baris `panduan-genset-{runId}.pdf`
26. Buka aksi baris `kontrak-lama-{runId}.pdf`
27. Verifikasi aksi `Permanently Delete` ada pada aksi baris `kontrak-lama-{runId}.pdf`
28. Verifikasi tidak ada aksi `Recover` dan `Restore` pada aksi baris `kontrak-lama-{runId}.pdf`
29. Tutup menu aksi baris
30. Verifikasi tidak ada tombol `Empty All` di modal `Recycle Bin`

### Panel Filter memuat field menurut kolom filterable
31. Klik ikon Filter
32. Verifikasi panel Filter tampil dengan field `File Format`, `Category`, `Source`, `Asset`, `Group`, `Size (KB)`, `Deleted Date`, `Deleted By`, dan `Auto-Purge In (days)`
33. Verifikasi tidak ada field filter untuk `File Name`
34. Verifikasi placeholder field `All formats`, `All categories`, `All sources`, `All assets`, `All groups`, `All users`, `Select date`, `Min`, dan `Max`

### Filter Category memuat opsi dari data tabel dan menyaring baris
35. Buka dropdown field `Category`
36. Verifikasi opsi `Asset Documents`, `Damaged`, dan `Maintenance` tampil
37. Pilih Category `Damaged`
38. Tutup dropdown field `Category`
39. Klik `[Apply]`
40. Verifikasi baris `foto-kerusakan-truk-{runId}.jpg` dan `foto-perbaikan-truk-{runId}.jpg` tampil
41. Verifikasi baris `kontrak-lama-{runId}.pdf` tidak tampil
42. Klik `[Clear Field]`
43. Klik `[Apply]`

### Filter Group memakai pemilih Tree
44. Pilih Group `Cabang Surabaya {runId}` pada panel Filter
45. Klik `[Apply]`
46. Verifikasi baris `foto-kerusakan-truk-{runId}.jpg` dan `foto-perbaikan-truk-{runId}.jpg` tampil
47. Verifikasi baris `kontrak-lama-{runId}.pdf` dan `foto-sebelum-servis-{runId}.jpg` tidak tampil
48. Klik `[Clear Field]`
49. Klik `[Apply]`

### Filter rentang Size dengan salah satu batas kosong dan di luar rentang
50. Isi Size (KB) Min `600` dan Max `1000`
51. Klik `[Apply]`
52. Verifikasi baris `foto-kerusakan-truk-{runId}.jpg` dan `foto-perbaikan-truk-{runId}.jpg` tampil
53. Verifikasi baris `panduan-genset-{runId}.pdf`, `kontrak-lama-{runId}.pdf`, dan `foto-sebelum-servis-{runId}.jpg` tidak tampil
54. Isi Size (KB) hanya Min `1200` dengan Max kosong
55. Klik `[Apply]`
56. Verifikasi baris `foto-sebelum-servis-{runId}.jpg` tampil
57. Verifikasi baris `kontrak-lama-{runId}.pdf` tidak tampil
58. Isi Size (KB) hanya Max `400` dengan Min kosong
59. Klik `[Apply]`
60. Verifikasi baris `arsip-1-{runId}.pdf` tampil
61. Verifikasi baris `panduan-genset-{runId}.pdf` tidak tampil
62. Isi Size (KB) Min `5000` dan Max `6000`
63. Klik `[Apply]`
64. Verifikasi pesan `No results found` tampil
65. Klik `[Clear Field]`
66. Klik `[Apply]`

### Filter rentang Auto-Purge In
67. Isi Auto-Purge In (days) Min `20` dan Max `26`
68. Klik `[Apply]`
69. Verifikasi baris `kontrak-lama-{runId}.pdf` dan `panduan-genset-{runId}.pdf` tampil
70. Verifikasi baris `foto-kerusakan-truk-{runId}.jpg` tidak tampil
71. Klik `[Clear Field]`
72. Klik `[Apply]`

### Filter rentang Deleted Date
73. Pilih rentang tanggal dari T0 − 6 hari sampai T0 − 4 hari pada field `Deleted Date`
74. Klik `[Apply]`
75. Verifikasi baris `kontrak-lama-{runId}.pdf` dan `panduan-genset-{runId}.pdf` tampil
76. Verifikasi baris `foto-sebelum-servis-{runId}.jpg` tidak tampil
77. Pilih rentang tanggal dari T0 − 60 hari sampai T0 − 40 hari pada field `Deleted Date`
78. Klik `[Apply]`
79. Verifikasi pesan `No results found` tampil
80. Klik `[Clear Field]`
81. Klik `[Apply]`

### Search kolom File Name dan Asset
82. Ganti isi kotak search dengan `kontrak-lama-{runId}`, tekan Enter
83. Verifikasi baris `kontrak-lama-{runId}.pdf` tampil
84. Verifikasi baris `foto-sebelum-servis-{runId}.jpg` tidak tampil
85. Ganti isi kotak search dengan `Truk Mitsubishi Fuso {runId}`, tekan Enter
86. Verifikasi baris `foto-kerusakan-truk-{runId}.jpg` tampil
87. Verifikasi baris `kontrak-lama-{runId}.pdf` tidak tampil

### Kolom searchable yang disembunyikan tidak lagi cocok dan cocok lagi saat ditampilkan
88. Klik header kolom `Actions` (`⋯`) pada tabel
89. Hilangkan centang kolom `Asset` pada panel Column Visibility
90. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility
91. Verifikasi header kolom `Asset` tidak ada lagi di tabel
92. Ganti isi kotak search dengan `Truk Mitsubishi Fuso {runId}`, tekan Enter
93. Verifikasi pesan `No results found` tampil di modal `Recycle Bin`
94. Klik header kolom `Actions` (`⋯`) pada tabel
95. Centang kolom `Asset` pada panel Column Visibility
96. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility
97. Ganti isi kotak search dengan `Truk Mitsubishi Fuso {runId}`, tekan Enter
98. Verifikasi baris `foto-kerusakan-truk-{runId}.jpg` tampil
99. Klik `(←)` pada kotak Search

### Sort Auto-Purge In menurut sisa waktu, bukan teks, dan lintas halaman
100. Ketik Search `{runId}`, tekan Enter
101. Klik ikon sort pada header kolom `Auto-Purge In`
102. Verifikasi lima baris pertama dari atas ke bawah: `foto-sebelum-servis-{runId}.jpg`, `foto-perbaikan-truk-{runId}.jpg`, `foto-kerusakan-truk-{runId}.jpg`, `panduan-genset-{runId}.pdf`, `kontrak-lama-{runId}.pdf`
103. Klik ikon sort pada header kolom `Auto-Purge In` sekali lagi
104. Klik halaman `2` pada Pagination
105. Verifikasi halaman 2 memuat tiga baris dari atas ke bawah: `foto-kerusakan-truk-{runId}.jpg`, `foto-perbaikan-truk-{runId}.jpg`, `foto-sebelum-servis-{runId}.jpg`
106. Klik halaman `1` pada Pagination
107. Klik ikon sort pada header kolom `Auto-Purge In` untuk ketiga kalinya

### Sort Deleted Date Oldest First
108. Klik ikon sort pada header kolom `Deleted Date`
109. Verifikasi baris pertama halaman 1 adalah `foto-sebelum-servis-{runId}.jpg`
110. Klik ikon sort pada header kolom `Deleted Date` sekali lagi
111. Klik ikon sort pada header kolom `Deleted Date` untuk ketiga kalinya

### File Name di Recycle Bin membuka File Preview
112. Klik File Name `kontrak-lama-{runId}.pdf` pada modal `Recycle Bin`
113. Verifikasi file `kontrak-lama-{runId}.pdf` terbuka langsung di tab browser baru
114. Tutup tab browser baru
115. Verifikasi modal `Recycle Bin` masih tampil di tab asal

### Opsi filter Asset dan Deleted By memakai nama aset dan nama lengkap
116. Buka dropdown field `Asset`
117. Verifikasi opsi `Genset Perkins 404 {runId}` tampil sebagai nama aset tanpa `- [Increment]`
118. Tutup dropdown field `Asset`
119. Buka dropdown field `Deleted By`
120. Verifikasi opsi `Bagus Prasetyo {runId}` tampil dengan nama lengkap
121. Tutup dropdown field `Deleted By`

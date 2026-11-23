---
id: TC-FA-DAMAGED-E2E-042-bulk-report-disposal-dep-disposal
title: "Bulk Report Disposal satu Group memakai satu Reason untuk semua, melewati record yang tidak lagi Damaged dengan toast Some items were skipped, dan memblok D-DMG-13 bila semua dilewati"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, D-DMG-13, D-DISP-13, "§4.2.4#r11", "§4.4#r13", V-DMG-09, TS-DMG-09, "§6#p2", "§8.3#b2", EC-DMG-35, "§9.4.4#r12", TS-DISP-15, EB-BLK-3, EB-EDG-2, "§9.2#b26", S-DMG-08, "§9.4.2#r32"]
smoke: []
dependsOn: ["Disposal: dialog Report Disposal (D-DISP-13) untuk bulk"]
trace:
  T-DMG-01: 4
  S-DMG-08: [4, 71, 73]
  EB-EDG-2: [6, 9, 10]
  "§4.4#r13": [16, 82, 100]
  D-DISP-13: [16, 24, 28, 82]
  "§9.2#b26": [16, 20, 21]
  TS-DISP-15: [19, 23, 55, 60, 63]
  "§8.3#b2": [23, 27, 42, 45, 89, 92]
  EB-BLK-3: [19, 23, 27, 63]
  V-DMG-09: [38, 39, 40, 85, 86, 87]
  TS-DMG-09: [38, 85]
  "§6#p2": [38, 55, 61, 104, 105]
  EC-DMG-35: [38, 39, 40, 45]
  "§9.4.4#r12": [42, 45, 89, 92]
  D-DMG-13: [55, 56, 57, 58, 100, 101, 102]
  "§4.2.4#r11": [55, 56, 57, 60, 63, 100]
  "§9.4.2#r32": [82, 85, 100]
anchor: []
coverage:
  web: automated
---

# Bulk Report Disposal satu Group memakai satu Reason untuk semua, melewati record yang tidak lagi Damaged dengan toast Some items were skipped, dan memblok D-DMG-13 bila semua dilewati

## Prerequisites
- Aktor: Total Control; `Admin B {runId}` (Total Control, seluruh client) hanya memicu perubahan state.
- Layar awal: Assets > Damaged > Active.
- Data:
  - DU-042-1: Damage record `Monitor Dell P2422H {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`.
  - DU-042-2: `2` Damage record `Printer HP LaserJet {runId} - 1` dan `Printer HP LaserJet {runId} - 2`, Group `Head Office`, Status `Damaged`, Source `Manual`.
  - DU-042-3: `6` Damage record `Proyektor Epson EB-X06 {runId} - 1` sampai `Proyektor Epson EB-X06 {runId} - 6`, Group `Head Office`, Status `Damaged`, Source `Manual`.
  - DU-042-4: `8` Damage record `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 1` sampai `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 8`, Group `Head Office`, Status `Damaged`, Source `Manual`.
  - DU-042-5: Damage record `Lintas Group {runId} Forklift Toyota 8FD`, Kata kunci Search `Lintas Group {runId}`, Group `Warehouse`, Status `Damaged`, Source `Manual`.
  - DU-042-6: Damage record `Lintas Group {runId} Scanner Fujitsu fi-7160`, Kata kunci Search `Lintas Group {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`.
  - DU-042-7: User `Admin B {runId}`, role Total Control, cakupan seluruh client.
  - DU-042-8: Input Reason bulk atas `Monitor Dell P2422H {runId}`: Reason `Monitor tidak menyala dan tidak layak diperbaiki`.
  - DU-042-9: Input Reason bulk atas `Printer HP LaserJet {runId} - 1` dan `Printer HP LaserJet {runId} - 2`: Reason `Printer satu Group sudah tidak layak pakai`.
  - DU-042-10: Input Reason bulk atas `Proyektor Epson EB-X06 {runId} - 1` sampai `- 6`: Reason `Proyektor satu Group sudah tidak layak pakai`.
  - DU-042-11: Input Reason bulk atas record `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara`: Reason `Panel listrik sudah tidak layak pakai`.
  - DU-042-12: Input Reason `Admin B {runId}` atas record `Proyektor Epson EB-X06 {runId} - 3` sampai `- 6` dan seluruh record `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara`: Reason `Unit sudah dilaporkan lebih dulu oleh admin lain`.
  - DU-042-13: `3` Damage record `Genset Perkins 400A {runId} - 1` sampai `Genset Perkins 400A {runId} - 3`, Group `Head Office`, Status `Damaged`, Source `Manual`.
  - DU-042-14: `2` Damage record `Rak Arsip Besi {runId} - 1` dan `Rak Arsip Besi {runId} - 2`, Group `Head Office`, Status `Damaged`, Source `Manual`.
  - DU-042-15: Input Reason bulk atas record `Genset Perkins 400A {runId} - 1` dan `- 2`: Reason `Genset sudah tidak layak pakai`.
  - DU-042-16: Input Reason `Admin B {runId}` atas record `Genset Perkins 400A {runId} - 3` dan seluruh record `Rak Arsip Besi {runId}`: Reason `Unit sudah dilaporkan lebih dulu oleh admin lain`.
- Kondisi:
  - Level Feature Suite Disposal bernilai `Basic`.
  - Selection Limit bernilai `1000`.

## Test Steps

### Bulk Report Disposal atas satu record memakai bentuk tunggal
1. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
2. Centang baris `Monitor Dell P2422H {runId}`
3. Klik `Bulk Action`
4. Verifikasi `Report Disposal` tersedia dan aktif pada daftar aksi bulk
5. Klik `Report Disposal`
6. Verifikasi dialog Report Disposal terbuka untuk `1` record `Monitor Dell P2422H {runId}` dalam bentuk tunggal yang sama dengan Report Disposal satu aset
7. Isi Reason `Monitor tidak menyala dan tidak layak diperbaiki`
8. Kirim dialog Report Disposal
9. Verifikasi toast sukses Report Disposal tampil
10. Verifikasi baris `Monitor Dell P2422H {runId}` berstatus `Reported Disposal`

### Bulk Report Disposal satu Group memakai satu Reason untuk semua record
11. Ganti isi kotak search dengan `Printer HP LaserJet {runId}`, tekan Enter
12. Centang baris `Printer HP LaserJet {runId} - 1`
13. Centang baris `Printer HP LaserJet {runId} - 2`
14. Klik `Bulk Action`
15. Klik `Report Disposal`
16. Verifikasi dialog Report Disposal terbuka dengan satu isian `Reason` untuk kedua record
17. Isi Reason `Printer satu Group sudah tidak layak pakai`
18. Kirim dialog Report Disposal dengan dua klik berturut-turut
19. Verifikasi tepat `1` toast sukses Report Disposal tampil
20. Verifikasi baris `Printer HP LaserJet {runId} - 1` berstatus `Reported Disposal`
21. Verifikasi baris `Printer HP LaserJet {runId} - 2` berstatus `Reported Disposal`
22. Klik nama aset `Printer HP LaserJet {runId} - 1` di kolom Name
23. Verifikasi dialog Damage Log record `Printer HP LaserJet {runId} - 1` memuat tepat `1` node `Disposal reported by`
24. Verifikasi baris detail node `Disposal reported by` memuat Reason `Printer satu Group sudah tidak layak pakai`
25. Tutup dialog Damage Log
26. Klik nama aset `Printer HP LaserJet {runId} - 2` di kolom Name
27. Verifikasi dialog Damage Log record `Printer HP LaserJet {runId} - 2` memuat tepat `1` node `Disposal reported by`
28. Verifikasi baris detail node `Disposal reported by` record `Printer HP LaserJet {runId} - 2` memuat Reason `Printer satu Group sudah tidak layak pakai`
29. Tutup dialog Damage Log

### Record yang tidak lagi Damaged saat Submit dilewati dan sisanya dilaporkan
30. Ganti isi kotak search dengan `Proyektor Epson EB-X06 {runId}`, tekan Enter
31. Centang baris `Proyektor Epson EB-X06 {runId} - 1`
32. Klik `Select All (6 records)`
33. Klik `Bulk Action`
34. Klik `Report Disposal`
35. `Admin B {runId}` menjalankan Report Disposal atas record `Proyektor Epson EB-X06 {runId} - 3`, `Proyektor Epson EB-X06 {runId} - 4`, `Proyektor Epson EB-X06 {runId} - 5`, dan `Proyektor Epson EB-X06 {runId} - 6` dengan Reason `Unit sudah dilaporkan lebih dulu oleh admin lain`
36. Isi Reason `Proyektor satu Group sudah tidak layak pakai`
37. Kirim dialog Report Disposal
38. Verifikasi toast `Success, asset has been reported for disposal. Some items were skipped.` tampil
39. Verifikasi baris `Proyektor Epson EB-X06 {runId} - 1` berstatus `Reported Disposal`
40. Verifikasi baris `Proyektor Epson EB-X06 {runId} - 2` berstatus `Reported Disposal`
41. Klik nama aset `Proyektor Epson EB-X06 {runId} - 1` di kolom Name
42. Verifikasi dialog Damage Log record `Proyektor Epson EB-X06 {runId} - 1` memuat tepat `1` node `Disposal reported by` dengan pelaku aktor yang menjalankan bulk
43. Tutup dialog Damage Log
44. Klik nama aset `Proyektor Epson EB-X06 {runId} - 3` di kolom Name
45. Verifikasi dialog Damage Log record `Proyektor Epson EB-X06 {runId} - 3` memuat tepat `1` node `Disposal reported by` dengan pelaku `Admin B {runId}`
46. Tutup dialog Damage Log

### Semua record dilewati memunculkan dialog blok Cannot Report Disposal
47. Ganti isi kotak search dengan `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara`, tekan Enter
48. Centang baris `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 1`
49. Klik `Select All (8 records)`
50. Klik `Bulk Action`
51. Klik `Report Disposal`
52. `Admin B {runId}` menjalankan Report Disposal atas seluruh `8` record `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara` dengan Reason `Unit sudah dilaporkan lebih dulu oleh admin lain`
53. Isi Reason `Panel listrik sudah tidak layak pakai`
54. Kirim dialog Report Disposal
55. Verifikasi dialog blok `Cannot Report Disposal` tampil
56. Verifikasi isi dialog `None of the selected records can be reported for disposal.`
57. Verifikasi daftar dialog memuat bullet `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 1` sampai `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 8`, masing-masing dengan keterangan per record, tanpa diringkas
58. Verifikasi daftar dialog dapat digulir sampai bullet terakhir `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 8`
59. Klik `OK`
60. Verifikasi bulk action bar masih tampil dengan jumlah terpilih `8`
61. Verifikasi baris `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 1` sampai `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 8` pada tabel berstatus `Reported Disposal` sesudah tabel dimuat ulang
62. Klik nama aset `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 1` di kolom Name
63. Verifikasi dialog Damage Log record `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - 1` memuat tepat `1` node `Disposal reported by` dengan pelaku `Admin B {runId}`
64. Tutup dialog Damage Log
65. Klik `×` pada bulk action bar

### Seleksi lintas Group diblok sebelum dialog Report Disposal dibuka
66. Ganti isi kotak search dengan `Lintas Group {runId}`, tekan Enter
67. Centang baris `Lintas Group {runId} Forklift Toyota 8FD`
68. Centang baris `Lintas Group {runId} Scanner Fujitsu fi-7160`
69. Klik `Bulk Action`
70. Klik `Report Disposal`
71. Verifikasi dialog blok `Selected assets come from more than one group. Select assets from one group.` tampil dengan bullet `Lintas Group {runId} Forklift Toyota 8FD` dan `Lintas Group {runId} Scanner Fujitsu fi-7160`
72. Klik `OK`
73. Verifikasi baris `Lintas Group {runId} Forklift Toyota 8FD` tetap berstatus `Damaged`
74. Klik `×` pada bulk action bar

### Record yang tidak lagi Damaged saat klik bulk disaring dari dialog Report Disposal
75. Ganti isi kotak search dengan `Genset Perkins 400A {runId}`, tekan Enter
76. Centang baris `Genset Perkins 400A {runId} - 1`
77. Centang baris `Genset Perkins 400A {runId} - 2`
78. Centang baris `Genset Perkins 400A {runId} - 3`
79. `Admin B {runId}` menjalankan Report Disposal atas record `Genset Perkins 400A {runId} - 3` dengan Reason `Unit sudah dilaporkan lebih dulu oleh admin lain`
80. Klik `Bulk Action`
81. Klik `Report Disposal`
82. Verifikasi dialog Report Disposal terbuka dengan satu isian `Reason` hanya untuk record `Genset Perkins 400A {runId} - 1` dan `Genset Perkins 400A {runId} - 2`
83. Isi Reason `Genset sudah tidak layak pakai`
84. Kirim dialog Report Disposal
85. Verifikasi toast `Success, asset has been reported for disposal. Some items were skipped.` tampil
86. Verifikasi baris `Genset Perkins 400A {runId} - 1` berstatus `Reported Disposal`
87. Verifikasi baris `Genset Perkins 400A {runId} - 2` berstatus `Reported Disposal`
88. Klik nama aset `Genset Perkins 400A {runId} - 1` di kolom Name
89. Verifikasi dialog Damage Log record `Genset Perkins 400A {runId} - 1` memuat tepat `1` node `Disposal reported by` dengan pelaku aktor yang menjalankan bulk
90. Tutup dialog Damage Log
91. Klik nama aset `Genset Perkins 400A {runId} - 3` di kolom Name
92. Verifikasi dialog Damage Log record `Genset Perkins 400A {runId} - 3` memuat tepat `1` node `Disposal reported by` dengan pelaku `Admin B {runId}`
93. Tutup dialog Damage Log

### Semua record tidak layak saat klik bulk memunculkan dialog blok Cannot Report Disposal
94. Ganti isi kotak search dengan `Rak Arsip Besi {runId}`, tekan Enter
95. Centang baris `Rak Arsip Besi {runId} - 1`
96. Centang baris `Rak Arsip Besi {runId} - 2`
97. `Admin B {runId}` menjalankan Report Disposal atas seluruh `2` record `Rak Arsip Besi {runId}` dengan Reason `Unit sudah dilaporkan lebih dulu oleh admin lain`
98. Klik `Bulk Action`
99. Klik `Report Disposal`
100. Verifikasi dialog blok `Cannot Report Disposal` tampil
101. Verifikasi isi dialog `None of the selected records can be reported for disposal.`
102. Verifikasi daftar dialog memuat bullet `Rak Arsip Besi {runId} - 1` dan `Rak Arsip Besi {runId} - 2`, masing-masing dengan keterangan per record
103. Klik `OK`
104. Verifikasi baris `Rak Arsip Besi {runId} - 1` pada tabel berstatus `Reported Disposal` sesudah tabel dimuat ulang
105. Verifikasi baris `Rak Arsip Besi {runId} - 2` pada tabel berstatus `Reported Disposal` sesudah tabel dimuat ulang
106. Klik `×` pada bulk action bar

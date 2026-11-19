---
id: TC-FA-ASTL-E2E-021-edit-purchase-satu-aset
title: "Edit Purchase satu aset tersimpan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-07a", "ASTL-LOGIC-21d", "ASTL-LOGIC-21e", "ASTL-LOGIC-21f", "EC-07", "EC-40", "§4.1i#b4", "§9.7#r13", "EB-FB-3@edit-purchase", "EB-FRM-1@edit-purchase", "EB-FRM-9", "EB-FRM-5@edit-purchase", "EB-ERR-4", "EB-FB-1@edit-purchase"]
smoke: ["EB-FRM-5@edit-purchase", "EB-ERR-4", "EB-FB-1@edit-purchase"]
dependsOn: []
trace:
  "ASTL-LOGIC-07a": [36, 46]
  "ASTL-LOGIC-21d": 14
  "ASTL-LOGIC-21e": [15, 24]
  "ASTL-LOGIC-21f": 33
  "EC-07": [46, 48]
  "EC-40": [15, 24, 33]
  "§4.1i#b4": [14, 82, 83, 88, 103, 107, 113]
  "§9.7#r13": [56, 58, 97, 98, 114]
  "EB-FB-3@edit-purchase": [46, 48]
  "EB-FRM-1@edit-purchase": [10, 58]
  "EB-FRM-9": [56, 64, 65]
  "EB-FRM-5@edit-purchase": 74
  "EB-ERR-4": 77
  "EB-FB-1@edit-purchase": 10
anchor: [4]
coverage:
  web: automated
---
# Edit Purchase satu aset tersimpan

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-021-1: aset Active Purchase `Pending` dengan Asset Class, Asset Name `Laptop Pro 16 {runId}`, tampil `Laptop Pro 16 {runId} - 1`, Brand `Lenovo`, Model/Type `ThinkPad T14`, Category `Peralatan IT`, Group `Kantor Pusat {runId}`, Status `Available`, Asset Class `Komputer Kantor`.
  - DU-021-2: aset Active Purchase `Pending` tanpa Asset Class, Asset Name `Kursi Kerja {runId}`, tampil `Kursi Kerja {runId} - 1`, Brand `Ergotec`, Model/Type `Staff 200`, Category `Furniture`, Group `Kantor Pusat {runId}`, Status `Available`.
  - DU-021-3: aset Active Purchase `Pending` dengan Asset Class, Asset Name `Server Rack {runId}`, tampil `Server Rack {runId} - 1`, Brand `Rittal`, Model/Type `TS8`, Category `Peralatan IT`, Group `Kantor Pusat {runId}`, Status `Available`, Asset Class `Komputer Kantor`.
  - DU-021-4: aset Active Purchase `Complete` dengan Asset Class, Asset Name `Printer Laser {runId}`, tampil `Printer Laser {runId} - 1`, Brand `Brother`, Model/Type `HL-L2375DW`, Category `Peralatan Kantor`, Group `Kantor Pusat {runId}`, Status `Available`, Asset Class `Komputer Kantor`, Purchase Date `T0 − 60 hari`, Purchase Cost `12500000`, garansi `Garansi Servis {runId}` sampai `T0 + 200 hari`.
  - DU-021-5: isian Edit Purchase `Laptop Pro 16 {runId} - 1`: Purchase Date `T0 − 30 hari`, Purchase Cost `0`.
  - DU-021-6: isian Edit Purchase `Kursi Kerja {runId} - 1`: Purchase Date `T0 − 30 hari`, Purchase Cost `0`.
  - DU-021-7: isian Edit Purchase `Server Rack {runId} - 1`: Purchase Date `T0 − 30 hari`, Purchase Cost `0`, Additional costs Name `Ongkos kirim` dan Amount `1500000`, sehingga Asset Value `Rp 1.500.000,00` dari Acquisition Cost `1500000`.
  - DU-021-8: isian Edit Purchase `Printer Laser {runId} - 1`: Purchase Cost `13750000`, tampil `Rp 13.750.000,00`.
  - DU-021-9: isian Edit Purchase `Printer Laser {runId} - 1` yang ditolak: Purchase Date `T0 + 1 hari`.
  - DU-021-10: isian Edit Purchase `Printer Laser {runId} - 1` yang ditolak: Warranty name `Garansi Servis {runId}`, Warranty until `T0 + 300 hari`.
  - DU-021-11: aset Active Purchase `Pending` dengan Asset Class, Asset Name `Lemari Arsip {runId}`, tampil `Lemari Arsip {runId} - 1`, Brand `Olympic`, Model/Type `LA-4`, Category `Furniture`, Group `Kantor Pusat {runId}`, Status `Available`, Asset Class `Komputer Kantor`, tanpa Warranty.
  - DU-021-12: isian Edit Purchase `Lemari Arsip {runId} - 1`: Purchase Date `T0 − 10 hari`, Purchase Cost kosong.
  - DU-021-13: isian Edit Purchase `Lemari Arsip {runId} - 1`: Purchase Cost `4000000`, tampil `Rp 4.000.000,00`.
  - DU-021-14: isian Edit Purchase `Lemari Arsip {runId} - 1`: Warranty name `Garansi Pabrik {runId}`, Warranty until `T0 + 400 hari`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Sesi pengamat: sesi browser kedua dengan aktor Total Control membuka All Assets dengan kolom `Purchase Date`, `Purchase Cost`, `Warranty Expiry`, dan `Asset Value (Commercial)` tampil, dan dengan Search yang memuat aset DU-021-1 sampai DU-021-4 dan DU-021-11, sebelum langkah 1, dan tidak dimuat ulang sesudahnya.

## Test Steps

### Purchase Cost 0 pada aset Pending membuatnya Complete
1. Ketik Search `{runId}`, tekan Enter
2. Buka Setup Column lewat menu `⋯` pada header tabel
3. Centang kolom `Purchase Date`, `Purchase Cost`, dan `Asset Value (Commercial)`
4. Verifikasi baris `Laptop Pro 16 {runId} - 1` memuat Asset Value `Pending` sebelum Edit Purchase
5. Klik menu `⋯` pada baris `Laptop Pro 16 {runId} - 1`
6. Pilih `Edit Purchase`
7. Isi Purchase Date `T0 − 30 hari`
8. Isi Purchase Cost `0`
9. Klik `[Save]`
10. Verifikasi toast `Success, purchase data has been saved.` tampil
11. Klik ikon Filter pada toolbar
12. Pilih `Complete` pada field `Purchase Status`
13. Klik `[Apply]`
14. Verifikasi baris `Laptop Pro 16 {runId} - 1` tampil pada tabel yang disaring Purchase Status `Complete` karena Purchase Date dan Purchase Cost terisi walau tanpa Warranty
15. Verifikasi Asset Value `Rp 0,00` pada baris `Laptop Pro 16 {runId} - 1` karena kelas aset sudah terdefinisi dan Additional costs tidak ada
16. Klik ikon Filter pada toolbar
17. Klik `[Clear Field]`
18. Klik `[Apply]`

### Purchase Cost 0 tanpa Asset Class membuat Asset Value Pending
19. Klik menu `⋯` pada baris `Kursi Kerja {runId} - 1`
20. Pilih `Edit Purchase`
21. Isi Purchase Date `T0 − 30 hari`
22. Isi Purchase Cost `0`
23. Klik `[Save]`
24. Verifikasi Asset Value `Pending` pada baris `Kursi Kerja {runId} - 1` walau Purchase Cost 0, karena kelas aset belum terdefinisi

### Purchase Cost 0 dengan Additional costs mengikuti Acquisition Cost
25. Klik menu `⋯` pada baris `Server Rack {runId} - 1`
26. Pilih `Edit Purchase`
27. Isi Purchase Date `T0 − 30 hari`
28. Isi Purchase Cost `0`
29. Klik `[+ Add additional cost]`
30. Isi Additional costs Name dengan `Ongkos kirim`
31. Isi Additional costs Amount dengan `1500000`
32. Klik `[Save]`
33. Verifikasi Asset Value `Rp 1.500.000,00` pada baris `Server Rack {runId} - 1` mengikuti Acquisition Cost

### Simpan tanpa perubahan adalah Edit No-Op
34. Klik menu `⋯` pada baris `Printer Laser {runId} - 1`
35. Pilih `Edit Purchase`
36. Verifikasi `[Save]` `Disabled` karena belum ada perubahan nilai
37. Klik `✕` pada form yang belum diubah
38. Klik ikon `Changelog` pada toolbar
39. Catat entri Changelog teratas
40. Tutup modal Changelog
41. Centang baris `Printer Laser {runId} - 1`
42. Klik `Bulk Action`
43. Pilih `Edit Purchase`
44. Isi `Purchase Cost (per asset)` dengan `12500000`
45. Klik `[Save]`
46. Verifikasi toast `No changes to save.` tampil dan dialog `Edit Purchase` tertutup
47. Klik ikon `Changelog` pada toolbar
48. Verifikasi Changelog tidak memuat entri baru untuk `Printer Laser {runId} - 1`
49. Tutup modal Changelog

### Perubahan satu field bertahan dan field lain tetap
50. Klik menu `⋯` pada baris `Printer Laser {runId} - 1`
51. Pilih `Edit Purchase`
52. Isi Purchase Cost `13750000`
53. Klik `[Save]`
54. Muat ulang halaman
55. Ketik Search `{runId}`, tekan Enter
56. Verifikasi Purchase Cost `Rp 13.750.000,00` dan Purchase Date `T0 − 60 hari` pada baris `Printer Laser {runId} - 1` tetap tampil sesudah muat ulang
57. Klik ikon `Changelog` pada toolbar
58. Verifikasi Changelog memuat entri baru field `Purchase Cost` untuk `Printer Laser {runId} - 1` dan tanpa entri field Purchase Date
59. Tutup modal Changelog

### Validasi yang gagal membiarkan dialog terbuka
60. Klik menu `⋯` pada baris `Printer Laser {runId} - 1`
61. Pilih `Edit Purchase`
62. Isi Purchase Date `T0 + 1 hari`
63. Klik `[Save]`
64. Verifikasi Alert `Purchase date cannot be in the future` tampil
65. Verifikasi dialog `Edit Purchase` tetap terbuka dan tidak ada toast sukses

### Nama garansi yang sudah ada ditolak dan data tetap
66. Klik `✕` pada form
67. Klik `[Leave]` pada dialog Unsaved Changes
68. Klik menu `⋯` pada baris `Printer Laser {runId} - 1`
69. Pilih `Edit Purchase`
70. Klik `[+ Add warranty]`
71. Isi Warranty name dengan `Garansi Servis {runId}`
72. Isi Warranty until dengan `T0 + 300 hari`
73. Klik `[Save]`
74. Verifikasi pesan `Warranty name already exists` tampil pada baris garansi baru
75. Klik `✕` pada form
76. Klik `[Leave]` pada dialog Unsaved Changes
77. Verifikasi baris `Printer Laser {runId} - 1` tetap menampilkan Purchase Cost `Rp 13.750.000,00` yang lama

### Purchase Complete butuh Purchase Date dan Purchase Cost, Warranty opsional
78. Klik menu `⋯` pada baris `Lemari Arsip {runId} - 1`
79. Pilih `Edit Purchase`
80. Isi Purchase Date `T0 − 10 hari` dan biarkan Purchase Cost kosong
81. Klik `[Save]`
82. Verifikasi toast `Success, purchase data has been saved.` tampil
83. Verifikasi Asset Value `Pending` pada baris `Lemari Arsip {runId} - 1` karena Purchase Cost belum terisi
84. Klik menu `⋯` pada baris `Lemari Arsip {runId} - 1`
85. Pilih `Edit Purchase`
86. Isi Purchase Cost `4000000`
87. Klik `[Save]`
88. Verifikasi Purchase Cost `Rp 4.000.000,00` dan Asset Value bukan `Pending` pada baris `Lemari Arsip {runId} - 1` walau tanpa Warranty

### Warranty Expiry mengikuti daftar Warranty yang tersimpan
89. Buka Setup Column lewat menu `⋯` pada header tabel
90. Centang kolom `Warranty Expiry`
91. Klik menu `⋯` pada baris `Lemari Arsip {runId} - 1`
92. Pilih `Edit Purchase`
93. Klik `[+ Add warranty]`
94. Isi Warranty name dengan `Garansi Pabrik {runId}`
95. Isi Warranty until dengan `T0 + 400 hari`
96. Klik `[Save]`
97. Verifikasi toast `Success, purchase data has been saved.` tampil
98. Verifikasi kolom Warranty Expiry pada baris `Lemari Arsip {runId} - 1` menampilkan tanggal `T0 + 400 hari`

### Status dihitung ulang setiap simpan
99. Klik menu `⋯` pada baris `Lemari Arsip {runId} - 1`
100. Pilih `Edit Purchase`
101. Kosongkan Purchase Date
102. Klik `[Save]`
103. Verifikasi Asset Value `Pending` pada baris `Lemari Arsip {runId} - 1` karena status Purchase dihitung ulang server dan Purchase Date kosong

### Status Purchase tetap Pending bila syarat tidak lengkap
104. Klik ikon Filter pada toolbar
105. Pilih `Pending` pada field `Purchase Status`
106. Klik `[Apply]`
107. Verifikasi baris `Lemari Arsip {runId} - 1` tampil pada tabel yang disaring Purchase Status `Pending` dengan Purchase Cost `4000000` dan Purchase Date belum diisi
108. Klik menu `⋯` pada baris `Lemari Arsip {runId} - 1`
109. Pilih `Edit Purchase`
110. Isi Purchase Date `T0 − 10 hari`
111. Kosongkan Purchase Cost
112. Klik `[Save]`
113. Verifikasi baris `Lemari Arsip {runId} - 1` tampil pada tabel yang disaring Purchase Status `Pending` dengan Purchase Date `T0 − 10 hari` dan Purchase Cost belum diisi

### Sesi lain melihat perubahan Purchase tanpa muat ulang
114. Verifikasi pada sesi pengamat, tanpa memuat ulang halaman, baris `Printer Laser {runId} - 1` menampilkan Purchase Cost `Rp 13.750.000,00`, dan baris `Lemari Arsip {runId} - 1` menampilkan Purchase Date `T0 − 10 hari`, Warranty Expiry `T0 + 400 hari`, dan Asset Value `Pending`

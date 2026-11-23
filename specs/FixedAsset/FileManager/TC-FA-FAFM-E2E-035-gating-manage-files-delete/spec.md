---
id: TC-FA-FAFM-E2E-035-gating-manage-files-delete
title: "Gating Manage files Delete: Delete pada group yang di-assign dan seleksi campuran"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02a, ACT-02b, ACT-03c, ACT-04a, ACT-05a, ACT-05b, ACT-06a, FAFM-LOGIC-05d, FAFM-LOGIC-05h, "§2#r2", "§2#r8", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#p1", "§4.8#p2", "§9.3#r1", "§9.3#r2", "§9.3#r3", "§9.3#r4", "§9.11#r4", "§9.11#r7", "EB-AKS-5@delete-file"]
smoke: []
dependsOn: []
trace:
  ACT-02a: [25]
  ACT-02b: [30]
  ACT-03c: [32, 33]
  ACT-04a: [38, 45]
  ACT-05a: [70]
  ACT-05b: [68]
  ACT-06a: [77]
  FAFM-LOGIC-05d: [14, 15, 25, 30, 82, 88]
  FAFM-LOGIC-05h: [14, 15]
  "§2#r2": [14, 16, 25, 30, 50, 86, 88]
  "§2#r8": [14, 16, 24, 25, 29, 30, 80, 82, 88]
  "§4.8#r1": [1]
  "§4.8#r2": [2]
  "§4.8#r3": [3, 4]
  "§4.8#r4": [5, 6, 7, 8, 10, 92]
  "§4.8#r5": [32, 33, 37]
  "§4.8#r6": [38, 45, 77]
  "§4.8#r7": [66, 67]
  "§4.8#r8": [25, 30]
  "§4.8#r9": [12]
  "§4.8#r10": [68, 70, 77]
  "§4.8#p1": [26, 67]
  "§4.8#p2": [32, 33, 38, 41, 67, 74, 75, 77]
  "§9.3#r1": [14, 16, 24, 29, 92]
  "§9.3#r2": [2, 50, 51]
  "§9.3#r3": [25, 30, 57]
  "§9.3#r4": [68, 70]
  "§9.11#r4": [14, 15, 16, 25, 30, 63, 80, 82, 86, 88, 89]
  "§9.11#r7": [17, 21, 65, 97, 101, 107]
  "EB-AKS-5@delete-file": [57, 59, 62]
anchor: [16, 20, 58, 64, 96, 100, 106]
coverage:
  web: automated
---

# Gating Manage files Delete: Delete pada group yang di-assign dan seleksi campuran

## Prerequisites
- Aktor: Dani Pengelola Hapus `{runId}` (pemegang capability Group Role Manage files dengan dua assignment: Delete pada group `Fleet`, Read pada group `Head Office`; tanpa assignment pada group `Branch Bandung`).
- Layar awal: Settings > File Manager, tab Kategori `Asset Photo` aktif.
- Data:
  - DU-035-1: User `Dani Pengelola Hapus {runId}`, role `Pengelola File Hapus {runId}`, assignment 1 capability `Manage files: Delete` pada group `Fleet`, assignment 2 capability `Manage files: Read` pada group `Head Office`.
  - DU-035-2: File `foto-excavator-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Excavator Mini {runId}` (Increment dibentuk server), Group `Fleet`, Size `950.0 KB`, Uploaded By `Dodi P`, Upload Date `T0 − 3 hari, pukul 11:00`, ada di tab `Asset Photo`; dihapus oleh spec ini.
  - DU-035-3: File `foto-crane-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Crane Pelabuhan {runId}` (Increment dibentuk server), Group `Fleet`, Size `820.0 KB`, Uploaded By `Dodi P`, Upload Date `T0 − 5 hari, pukul 13:45`, ada di tab `Asset Photo`.
  - DU-035-4: File `foto-printer-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Printer Kantor {runId}` (Increment dibentuk server), Group `Head Office` (Read saja), Size `410.0 KB`, Uploaded By `Budi S`, Upload Date `T0 − 6 hari, pukul 09:20`, ada di tab `Asset Photo`.
  - DU-035-5: File `foto-lemari-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Lemari Arsip {runId}` (Increment dibentuk server), Group `Branch Bandung` (tanpa assignment), Size `360.0 KB`, Uploaded By `Rina A`, Upload Date `T0 − 7 hari, pukul 15:10`, ada di tab `Asset Photo`.
  - DU-035-6: File `foto-bin-fleet-{runId}.jpg`, File Format `JPG`, Category `Asset Photo`, Source `Asset Photo`, Asset `Crane Pelabuhan {runId}` (Increment dibentuk server), Group `Fleet`, Size `300.0 KB`, Deleted By `Rina A`, Deleted Date `T0 − 1 hari, pukul 08:30`, ada di Recycle Bin dan di Changelog (aksi Delete).
  - DU-035-7: File `foto-bin-kantor-{runId}.jpg`, File Format `JPG`, Category `Asset Photo`, Source `Asset Photo`, Asset `Printer Kantor {runId}` (Increment dibentuk server), Group `Head Office`, Size `280.0 KB`, Deleted By `Rina A`, Deleted Date `T0 − 1 hari, pukul 08:45`, ada di Recycle Bin.
  - DU-035-8: File `foto-bin-lemari-{runId}.jpg`, File Format `JPG`, Category `Asset Photo`, Source `Asset Photo`, Asset `Lemari Arsip {runId}` (Increment dibentuk server), Group `Branch Bandung`, Size `250.0 KB`, Deleted By `Rina A`, Deleted Date `T0 − 2 hari, pukul 10:00`, ada di Recycle Bin dan di Changelog (aksi Delete).
  - DU-035-9: Aset `Pick-up Operasional {runId}` (Increment dibentuk server), Status `Disposed`, Group `Fleet`, ada di tab `Disposed & Unmanaged Assets`.
  - DU-035-10: Group `Fleet Workshop {runId}`, group turunan langsung dari `Fleet`.
  - DU-035-11: File `foto-forklift-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Forklift Bengkel {runId}` (Increment dibentuk server), Group `Fleet Workshop {runId}` (turunan dari group Delete), Size `700.0 KB`, Uploaded By `Dodi P`, Upload Date `T0 − 4 hari, pukul 10:30`, ada di tab `Asset Photo`.
  - DU-035-12: File `foto-bin-bengkel-{runId}.jpg`, File Format `JPG`, Category `Asset Photo`, Source `Asset Photo`, Asset `Forklift Bengkel {runId}` (Increment dibentuk server), Group `Fleet Workshop {runId}` (turunan dari group Delete), Size `220.0 KB`, Deleted By `Rina A`, Deleted Date `T0 − 2 hari, pukul 14:00`, ada di Recycle Bin.

## Test Steps

### Elemen tab Files untuk pemegang Manage files Delete
1. Verifikasi item `File Manager` tampil pada sidebar grup `Settings`
2. Verifikasi kartu `Storage Usage` tampil
3. Verifikasi tab Kategori `Asset Photo` tampil
4. Verifikasi tab `Disposed & Unmanaged Assets` tampil
5. Verifikasi kotak Search tampil
6. Verifikasi tombol `Filter` tampil
7. Verifikasi tombol `Download` tampil
8. Verifikasi tombol `Changelog` tampil pada header kartu Storage Usage
9. Klik `⋯` pada header tabel
10. Verifikasi item `Setup Column...` tampil
11. Tutup panel Column Visibility
12. Verifikasi tombol `Recycle Bin` tampil pada header kartu Storage Usage

### Scope group yang di-assign
13. Ketik Search `{runId}`, tekan Enter
14. Verifikasi baris `foto-excavator-{runId}.jpg` tampil pada tabel
15. Verifikasi baris `foto-crane-{runId}.jpg` tampil pada tabel
16. Verifikasi baris `foto-printer-{runId}.jpg` tampil pada tabel
17. Verifikasi baris `foto-lemari-{runId}.jpg` tidak ada pada tabel
18. Klik `Filter`
19. Klik filter `Group`
20. Verifikasi opsi `Fleet` dan `Head Office` tampil
21. Verifikasi opsi `Branch Bandung` tidak ada
22. Tutup panel Filter

### Aksi baris sesuai group
23. Klik `⋯` pada baris `foto-excavator-{runId}.jpg`
24. Verifikasi menu baris memuat `Download`
25. Verifikasi menu baris memuat `Delete`
26. Verifikasi `Delete` pada menu baris enabled
27. Tutup menu baris
28. Klik `⋯` pada baris `foto-printer-{runId}.jpg`
29. Verifikasi menu baris memuat `Download`
30. Verifikasi menu baris tidak memuat `Delete` (Hidden, bukan Disabled)
31. Tutup menu baris

### Seleksi campuran pada tab Files
32. Verifikasi kotak centang tampil pada baris `foto-printer-{runId}.jpg`
33. Verifikasi kotak centang tampil pada baris `foto-crane-{runId}.jpg`
34. Centang baris `foto-printer-{runId}.jpg`
35. Centang baris `foto-crane-{runId}.jpg`
36. Klik `Bulk Action` pada bulk action bar
37. Verifikasi menu bulk memuat `Download (ZIP)`
38. Verifikasi menu bulk tidak memuat `Delete` (Hidden, bukan Disabled)
39. Tutup menu bulk
40. Klik `Select All (4 records)` pada bulk action bar
41. Verifikasi pesan seleksi `4 Files selected` tampil
42. Klik tombol hapus seleksi (X) pada bulk action bar
43. Centang baris `foto-crane-{runId}.jpg`
44. Klik `Bulk Action` pada bulk action bar
45. Verifikasi menu bulk memuat `Delete`
46. Tutup menu bulk
47. Klik tombol hapus seleksi (X) pada bulk action bar

### Tab Asset Data hanya baca
48. Klik tab `Disposed & Unmanaged Assets`
49. Ketik Search `{runId}`, tekan Enter
50. Verifikasi baris aset `Pick-up Operasional {runId}` tampil pada tabel
51. Verifikasi kolom kotak centang tidak ada pada tabel (Hidden)

### Delete pada group yang di-assign tersimpan
52. Klik tab Kategori `Asset Photo`
53. Ketik Search `{runId}`, tekan Enter
54. Klik `⋯` pada baris `foto-excavator-{runId}.jpg`
55. Klik `Delete`
56. Klik `[Delete]` pada dialog `Delete File`
57. Verifikasi toast `Success, [File Name] has been deleted.` tampil dengan File Name `foto-excavator-{runId}.jpg`
58. Verifikasi baris `foto-crane-{runId}.jpg` tetap tampil pada tabel
59. Verifikasi baris `foto-excavator-{runId}.jpg` tidak ada pada tabel

### Recycle Bin dan seleksi campuran
60. Klik `Recycle Bin` pada header kartu Storage Usage
61. Ketik Search `{runId}`, tekan Enter
62. Verifikasi baris `foto-excavator-{runId}.jpg` tampil pada Recycle Bin
63. Verifikasi baris `foto-bin-fleet-{runId}.jpg` tampil pada Recycle Bin
64. Verifikasi baris `foto-bin-kantor-{runId}.jpg` tampil pada Recycle Bin
65. Verifikasi baris `foto-bin-lemari-{runId}.jpg` tidak ada pada Recycle Bin
66. Verifikasi kotak centang tampil dan enabled pada baris `foto-bin-fleet-{runId}.jpg`
67. Verifikasi kotak centang pada baris `foto-bin-kantor-{runId}.jpg` tampil dalam keadaan Disabled
68. Verifikasi aksi `Permanently Delete` tidak tersedia pada baris `foto-bin-kantor-{runId}.jpg` (Hidden, bukan Disabled)
69. Klik `⋯` pada baris `foto-bin-fleet-{runId}.jpg`
70. Verifikasi menu baris memuat `Permanently Delete`
71. Tutup menu baris
72. Centang baris `foto-bin-fleet-{runId}.jpg`
73. Klik `Select All (3 records)` pada bulk action bar
74. Verifikasi pesan seleksi `3 Files selected` tampil
75. Verifikasi kotak centang pada baris `foto-bin-kantor-{runId}.jpg` tidak tercentang
76. Klik `Bulk Action` pada bulk action bar
77. Verifikasi menu bulk memuat `Permanently Delete`
78. Tutup menu bulk

### Permanently Delete tersedia pada file di group turunan dari group Delete
79. Klik tombol hapus seleksi (X) pada bulk action bar
80. Verifikasi baris `foto-bin-bengkel-{runId}.jpg` tampil pada Recycle Bin
81. Klik `⋯` pada baris `foto-bin-bengkel-{runId}.jpg`
82. Verifikasi menu baris memuat `Permanently Delete`
83. Tutup menu baris
84. Tutup dialog Recycle Bin

### Delete tersedia pada file di group turunan dari group Delete
85. Ketik Search `{runId}`, tekan Enter
86. Verifikasi baris `foto-forklift-{runId}.jpg` tampil pada tabel
87. Klik `⋯` pada baris `foto-forklift-{runId}.jpg`
88. Verifikasi menu baris memuat `Delete`
89. Verifikasi `Delete` pada menu baris enabled
90. Tutup menu baris

### Preview file pada group yang di-assign
91. Klik nama file `foto-crane-{runId}.jpg`
92. Verifikasi file `foto-crane-{runId}.jpg` terbuka pada tab browser baru
93. Kembali ke tab File Manager

### Changelog tidak memuat file di luar group aktor
94. Klik `Changelog` pada header kartu Storage Usage
95. Ketik Search `{runId}`, tekan Enter
96. Verifikasi baris log dengan File Name `foto-bin-fleet-{runId}.jpg` tampil pada Changelog
97. Verifikasi baris log dengan File Name `foto-bin-lemari-{runId}.jpg` tidak ada pada Changelog
98. Klik `Filter` pada dialog Changelog
99. Klik filter `File Name`
100. Verifikasi opsi `foto-bin-fleet-{runId}.jpg` tampil
101. Verifikasi opsi `foto-bin-lemari-{runId}.jpg` tidak ada
102. Tutup panel Filter
103. Tutup dialog Changelog

### Hasil Download tidak memuat file di luar group aktor
104. Klik tombol `Download` pada toolbar tabel
105. Klik `Download as CSV`
106. Verifikasi baris `foto-crane-{runId}.jpg` ada pada berkas hasil Download
107. Verifikasi baris `foto-lemari-{runId}.jpg` tidak ada pada berkas hasil Download

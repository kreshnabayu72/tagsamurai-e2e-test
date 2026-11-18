---
id: TC-FA-ASSIGN-E2E-008-tab-assigned-assets
title: "Tab Assigned Assets: By Asset dan By Assignee, serta halaman Assigned Asset"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-ASG-13, T-ASG-14, "§4.1#r2", "§4.1#r13", "§4.2.14#p2", "§9.5#r3", "§9.5#r4", EC-ASG-87]
smoke: []
dependsOn: []
trace:
  T-ASG-13: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 25, 26, 27, 31, 35, 37, 42, 128, 130, 132, 135, 137]
  T-ASG-14: [46, 47, 48, 49, 50, 51, 52, 54, 56, 58, 59, 61, 64, 66, 68, 70, 72, 97, 140]
  "§4.1#r2": 3
  "§4.1#r13": 75
  "§4.2.14#p2": [75, 76, 78, 79, 80, 81, 83, 86, 88, 92, 99, 105]
  "§9.5#r3": [2, 44]
  "§9.5#r4": [9, 48]
  EC-ASG-87: [111, 115, 121, 125]
anchor: [5, 102, 110, 118]
coverage:
  web: automated
---

# Tab Assigned Assets: By Asset dan By Assignee, serta halaman Assigned Asset

## Prerequisites
- Aktor: Total Control `Hendra Kusuma {runId}`; aktor pemicu perubahan: Asset Admin `Rina Wijaya {runId}`.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-008-1: User `Hendra Kusuma {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-008-2: User `Rina Wijaya {runId}`, role Asset Admin pada Group `Head Office {runId}` dan `Branch Surabaya {runId}`; ia memicu perubahan (Unassign dan Report Missing), menyerahkan aset DU-008-7, dan bukan Assignee.
  - DU-008-3: Group `Head Office {runId}` dan Group `Branch Surabaya {runId}`.
  - DU-008-4: User `Budi Santoso {runId}` dengan Employee ID `EMP-{runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Budi S`, dari `Budi Santoso {runId}`.
  - DU-008-5: User `Sari Dewi {runId}` tanpa Employee ID, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Sari D`, dari `Sari Dewi {runId}`.
  - DU-008-6: Division `Finance {runId}` dengan PIC aktif `Dewi Anggraini {runId}`, karyawan aktif ber-akun login tanpa akses menu Assignment.
  - DU-008-7: Aset `Laptop Dell Latitude 5420 {runId}` bermerek `Dell {runId}` model `Latitude 5420 {runId}` di Group `Head Office {runId}`, berstatus `Assigned` untuk Assignee DU-008-4; tanpa foto, beralias `Lap-Dell-5420 {runId}`, ber-TAG QR, diserahkan oleh DU-008-2; Asset ID dan kode TAG dibentuk server dan menjadi milik aset ini; diserahkan pertama.
  - DU-008-8: Aset `Printer HP LaserJet M404 {runId}` bermerek `HP {runId}` model `LaserJet M404 {runId}` di Group `Branch Surabaya {runId}`, berstatus `Assigned` untuk Assignee Division `Finance {runId}`; diserahkan kedua dan satu-satunya aset Finance. Spec ini memicu Unassign oleh DU-008-2 pada aset ini.
  - DU-008-9: Aset `Proyektor Epson EB-X49 {runId}` tanpa Brand dan tanpa Model/Type di Group `Head Office {runId}`, berstatus `Assigned` untuk Assignee DU-008-5; diserahkan ketiga. Spec ini memicu Report Missing oleh DU-008-2 pada aset ini.
  - DU-008-10: Aset `Tablet Samsung Tab A8 {runId}` bermerek `Samsung {runId}` model `Tab A8 {runId}` di Group `Branch Surabaya {runId}`, berstatus `Assigned` untuk Assignee DU-008-4; diserahkan keempat. Spec ini memicu Unassign oleh DU-008-2 pada aset ini.
  - DU-008-11: nama berkas unduhan sub-tab `By Asset` adalah `Assignment-Assigned-Assets` dan sub-tab `By Assignee` adalah `Assignment-Assigned-Assets-By-Assignee`.

## Test Steps

### Tab Assigned Assets dan sub-tab By Asset
1. Klik tab `Assigned Assets`
2. Verifikasi sub-tab `By Asset` menjadi view awal dan URL memuat `?view=asset`
3. Verifikasi sub-tab `By Asset` dan `By Assignee` tersedia di tab `Assigned Assets`
4. Ketik Search `{runId}`, tekan Enter
5. Verifikasi tabel memuat tepat 4 baris, yaitu aset `Laptop Dell Latitude 5420 {runId}`, `Printer HP LaserJet M404 {runId}`, `Proyektor Epson EB-X49 {runId}`, dan `Tablet Samsung Tab A8 {runId}`
6. Verifikasi header kolom tampil berurutan dari kiri ke kanan: `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `Assigned Since`, `Transaction ID`, `Assignee`
7. Verifikasi kolom `TAG` dan `Category` tidak tampil secara awal
8. Verifikasi kolom `Confirmation`, `Purpose`, dan `Handed Over By` tidak tampil secara awal
9. Verifikasi urutan awal baris dari atas ke bawah menurut Assigned Since terlama: `Laptop Dell Latitude 5420 {runId}`, `Printer HP LaserJet M404 {runId}`, `Proyektor Epson EB-X49 {runId}`, `Tablet Samsung Tab A8 {runId}`
10. Verifikasi kolom `Name` setiap baris berformat `[Asset Name] - [Increment]`
11. Verifikasi kolom `Brand` dan `Model/Type` baris `Laptop Dell Latitude 5420 {runId}` menampilkan `Dell {runId}` dan `Latitude 5420 {runId}`
12. Verifikasi kolom `Brand` dan `Model/Type` baris `Proyektor Epson EB-X49 {runId}` menampilkan `—`
13. Verifikasi kolom `Group` baris `Laptop Dell Latitude 5420 {runId}` menampilkan `Head Office {runId}` dan baris `Tablet Samsung Tab A8 {runId}` menampilkan `Branch Surabaya {runId}`
14. Verifikasi kolom `Status` pada keempat baris menampilkan `Assigned`
15. Verifikasi kolom `Transaction ID` pada keempat baris berformat `ASG-YYYY-NNNN`
16. Verifikasi kolom `Assignee` menampilkan `Budi S` pada baris `Laptop Dell Latitude 5420 {runId}` dan `Tablet Samsung Tab A8 {runId}`, `Finance {runId}` pada baris `Printer HP LaserJet M404 {runId}`, dan `Sari D` pada baris `Proyektor Epson EB-X49 {runId}`
17. Verifikasi kolom `Assigned Since` dan `Asset ID` pada keempat baris terisi
18. Verifikasi kolom `Photo` baris `Laptop Dell Latitude 5420 {runId}` menampilkan placeholder gambar standar karena aset tidak memiliki foto
19. Arahkan kursor ke kolom `Assigned Since` baris `Laptop Dell Latitude 5420 {runId}`
20. Verifikasi `Rina Wijaya {runId}` tampil sebagai pihak yang menyerahkan aset
21. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
22. Verifikasi menu aksi baris memuat `Assignment Log`, `Unassign`, `Report Damaged`, dan `Report Missing`
23. Tutup menu aksi baris

### Filter di sub-tab By Asset
24. Klik `Filter`
25. Verifikasi field filter `Brand`, `Model/Type`, `Group`, `Status`, `Assigned Since`, `Assignee`, `TAG`, `Category`, `Confirmation`, dan `Handed Over By` tampil
26. Verifikasi placeholder `All brands`, `All models`, `All groups`, `All statuses`, `All assignees`, `All tags`, `All categories`, `All confirmations`, dan `All users` tampil pada field dropdown masing-masing
27. Verifikasi field `Assigned Since` memuat placeholder `Select date`
28. Klik `Filter`

### Bulk Unassign hanya untuk aset milik satu Assignee
29. Centang baris `Laptop Dell Latitude 5420 {runId}`
30. Klik `Bulk Action`
31. Verifikasi item `Unassign` aktif karena semua aset terpilih milik satu Assignee
32. Tutup menu `Bulk Action`
33. Centang baris `Proyektor Epson EB-X49 {runId}`
34. Klik `Bulk Action`
35. Verifikasi item `Unassign` disabled karena aset terpilih milik lebih dari satu Assignee
36. Arahkan kursor ke item `Unassign`
37. Verifikasi alasan `Select assets held by one assignee.` tersampaikan pada item `Unassign` yang disabled
38. Tutup menu `Bulk Action`
39. Klik `×` pada bar seleksi

### Export sub-tab By Asset
40. Klik `Download`[^drift-1]
41. Klik `Download as CSV`
42. Verifikasi berkas `Assignment-Assigned-Assets.csv` terunduh

### Sub-tab By Assignee
43. Klik sub-tab `By Assignee`
44. Verifikasi URL memuat `?view=assignee`
45. Ketik Search `{runId}`, tekan Enter
46. Verifikasi tabel memuat tepat 3 baris, yaitu baris Assignee `Budi S`, `Finance {runId}`, dan `Sari D`
47. Verifikasi header kolom tampil berurutan: `Assignee`, `Assignee Type`, `Group`, `Total Asset`
48. Verifikasi urutan awal baris menurut nama Assignee A-Z: `Budi S`, `Finance {runId}`, `Sari D`
49. Verifikasi baris `Budi S` menampilkan Employee ID `EMP-{runId}`
50. Verifikasi baris `Sari D` dan baris `Finance {runId}` tidak menampilkan Employee ID
51. Verifikasi kolom `Total Asset` menampilkan `2` pada baris `Budi S`, `1` pada baris `Finance {runId}`, dan `1` pada baris `Sari D`
52. Verifikasi kolom `Group` baris `Budi S` menampilkan satu badge Group diikuti `+1`

### Hover Group, Sort, Filter, dan Export di sub-tab By Assignee
53. Arahkan kursor ke kolom `Group` baris `Budi S`
54. Verifikasi daftar Group `Head Office {runId}` dan `Branch Surabaya {runId}` tampil
55. Klik header kolom `Assignee Type`
56. Verifikasi baris `Finance {runId}` tampil di atas baris `Budi S` dan baris `Sari D`
57. Klik `Filter`
58. Verifikasi field filter `Assignee`, `Assignee Type`, `Group`, dan `Total Asset` tampil
59. Verifikasi placeholder `All assignees`, `All types`, dan `All groups` tampil pada field dropdown masing-masing, serta field `Total Asset` memuat input `Min` dan `Max`
60. Klik `Filter`
61. Verifikasi tabel tidak memiliki kolom checkbox dan `Bulk Action` tidak tampil
62. Klik `Download`[^drift-1]
63. Klik `Download as CSV`
64. Verifikasi berkas `Assignment-Assigned-Assets-By-Assignee.csv` terunduh

### Search di sub-tab By Assignee mencakup aset yang dipegang
65. Ganti isi kotak search dengan `Laptop Dell Latitude 5420 {runId}`, tekan Enter
66. Verifikasi baris `Budi S` tampil karena nama aset yang dipegang ikut dicari
67. Ganti isi kotak search dengan Asset ID milik aset `Laptop Dell Latitude 5420 {runId}`, tekan Enter
68. Verifikasi baris `Budi S` tampil karena Asset ID aset yang dipegang ikut dicari
69. Ganti isi kotak search dengan alias aset `Laptop Dell Latitude 5420 {runId}`, yaitu `Lap-Dell-5420 {runId}`, tekan Enter
70. Verifikasi baris `Budi S` tampil karena alias aset yang dipegang ikut dicari
71. Ganti isi kotak search dengan kode TAG milik aset `Laptop Dell Latitude 5420 {runId}`, tekan Enter
72. Verifikasi baris `Budi S` tampil karena kode TAG aset yang dipegang ikut dicari
73. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Halaman Assigned Asset
74. Klik nama Assignee `Budi S`
75. Verifikasi halaman Assigned Asset terbuka dengan Assignee `Budi S` dan tabel memuat `Laptop Dell Latitude 5420 {runId}` dan `Tablet Samsung Tab A8 {runId}`
76. Verifikasi tabel halaman Assigned Asset tidak memuat aset `Proyektor Epson EB-X49 {runId}` milik Assignee lain
77. Klik `Search`
78. Verifikasi kotak Search memuat placeholder `Search asset name, asset ID, or transaction ID...`
79. Verifikasi halaman Assigned Asset tidak memuat kolom `Assignee`, tombol `Search by Scan`, maupun sub-tab `By Asset` dan `By Assignee`
80. Verifikasi header kolom halaman Assigned Asset tampil berurutan dari kiri ke kanan: `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `Assigned Since`, `Transaction ID`
81. Verifikasi urutan awal baris menurut Assigned Since terlama: `Laptop Dell Latitude 5420 {runId}`, `Tablet Samsung Tab A8 {runId}`
82. Klik `Filter`
83. Verifikasi field filter `Brand`, `Model/Type`, `Group`, `Status`, `Assigned Since`, `TAG`, `Category`, `Confirmation`, dan `Handed Over By` tampil dengan placeholder `All brands`, `All models`, `All groups`, `All statuses`, `All tags`, `All categories`, `All confirmations`, dan `All users` pada field dropdown masing-masing, serta placeholder `Select date` pada field `Assigned Since`
84. Klik `Filter`
85. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
86. Verifikasi menu aksi baris memuat `Assignment Log`, `Unassign`, `Report Damaged`, dan `Report Missing`
87. Klik `Assignment Log`
88. Verifikasi dialog Assignment Log untuk aset `Laptop Dell Latitude 5420 {runId}` terbuka
89. Tutup dialog Assignment Log
90. Centang baris `Laptop Dell Latitude 5420 {runId}`
91. Klik `Bulk Action`
92. Verifikasi item `Unassign` aktif pada menu `Bulk Action`
93. Tutup menu `Bulk Action`
94. Klik `×` pada bar seleksi
95. Kembali ke halaman sebelumnya

### Row action Detail membuka halaman Assigned Asset
96. Klik `⋯` pada baris `Sari D`
97. Verifikasi menu aksi baris pada sub-tab `By Assignee` memuat `Detail`
98. Klik `Detail`
99. Verifikasi halaman Assigned Asset terbuka dengan Assignee `Sari D` dan tabel memuat `Proyektor Epson EB-X49 {runId}`
100. Kembali ke halaman sebelumnya

### Assignee yang tidak lagi memegang aset
101. Klik nama Assignee `Finance {runId}`
102. Verifikasi tabel halaman Assigned Asset memuat aset `Printer HP LaserJet M404 {runId}`
103. Aktor `Rina Wijaya {runId}` melakukan Unassign aset `Printer HP LaserJet M404 {runId}` sampai berhasil
104. Muat ulang halaman
105. Verifikasi empty state `No assigned assets` dan `This assignee doesn't hold any assets.` tampil

### Baris hilang dari Assigned Assets dan muncul di History
106. Klik tab `Assigned Assets`
107. Ganti isi kotak search dengan `{runId}`, tekan Enter
108. Aktor `Rina Wijaya {runId}` melakukan Unassign aset `Tablet Samsung Tab A8 {runId}` sampai berhasil
109. Biarkan halaman terbuka selama 5 detik tanpa memuat ulang halaman
110. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil di sub-tab `By Asset`
111. Verifikasi baris `Tablet Samsung Tab A8 {runId}` tidak lagi tampil di sub-tab `By Asset` dalam 5 detik tanpa muat ulang halaman
112. Klik tab `History`
113. Klik sub-tab `By Asset`
114. Ganti isi kotak search dengan `Tablet Samsung Tab A8 {runId}`, tekan Enter
115. Verifikasi baris `Tablet Samsung Tab A8 {runId}` tampil di sub-tab `By Asset` pada tab `History`

### Report Missing dari tempat lain memindahkan baris ke History
116. Klik tab `Assigned Assets`
117. Ganti isi kotak search dengan `{runId}`, tekan Enter
118. Verifikasi baris `Proyektor Epson EB-X49 {runId}` tampil di sub-tab `By Asset`
119. Aktor `Rina Wijaya {runId}` melakukan Report Missing atas aset `Proyektor Epson EB-X49 {runId}` sampai berhasil
120. Biarkan halaman terbuka selama 5 detik tanpa memuat ulang halaman
121. Verifikasi baris `Proyektor Epson EB-X49 {runId}` tidak lagi tampil di sub-tab `By Asset` dalam 5 detik tanpa muat ulang halaman
122. Klik tab `History`
123. Klik sub-tab `By Asset`
124. Ganti isi kotak search dengan `Proyektor Epson EB-X49 {runId}`, tekan Enter
125. Verifikasi baris `Proyektor Epson EB-X49 {runId}` tampil di sub-tab `By Asset` pada tab `History` dengan penanda `Missing`

### Search sub-tab By Asset mencakup Asset ID, alias, dan kode TAG
126. Klik tab `Assigned Assets`
127. Ganti isi kotak search dengan Asset ID milik aset `Laptop Dell Latitude 5420 {runId}`, tekan Enter
128. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil di sub-tab `By Asset` karena Asset ID ikut dicari
129. Ganti isi kotak search dengan alias aset `Laptop Dell Latitude 5420 {runId}`, yaitu `Lap-Dell-5420 {runId}`, tekan Enter
130. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil di sub-tab `By Asset` karena alias ikut dicari
131. Ganti isi kotak search dengan kode TAG milik aset `Laptop Dell Latitude 5420 {runId}`, tekan Enter
132. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil di sub-tab `By Asset` karena kode TAG ikut dicari
133. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Hover Brand dan Model/Type di sub-tab By Asset
134. Arahkan kursor ke kolom `Brand` baris `Laptop Dell Latitude 5420 {runId}`
135. Verifikasi nama Brand penuh `Dell {runId}` tampil pada hover baris `Laptop Dell Latitude 5420 {runId}`
136. Arahkan kursor ke kolom `Model/Type` baris `Laptop Dell Latitude 5420 {runId}`
137. Verifikasi nama Model penuh `Latitude 5420 {runId}` tampil pada hover baris `Laptop Dell Latitude 5420 {runId}`

### Hover Assignee di sub-tab By Assignee
138. Klik sub-tab `By Assignee`
139. Arahkan kursor ke nilai Assignee `Budi S`
140. Verifikasi nama lengkap `Budi Santoso {runId}` tampil pada hover Assignee di sub-tab `By Assignee`

[^drift-1]: Drift PRD vs foundation. PRD §4.1 Matriks Aksi baris Export: nama dan tooltip tombol toolbar adalah `Export`, bukan `Download`. foundation `prd-conventions.md` §9.1: icon toolbar bernama `Download` dengan tooltip `Download`, dan modul tidak menulis ulang teks tooltip itu. Diasersi: foundation, karena tombol unduh di toolbar tabel adalah pola bersama (SB-4).

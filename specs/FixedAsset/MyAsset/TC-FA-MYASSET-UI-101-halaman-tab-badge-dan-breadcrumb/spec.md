---
id: TC-FA-MYASSET-UI-101-halaman-tab-badge-dan-breadcrumb
title: "Halaman My Asset: tab, badge jumlah, breadcrumb, dan susunan tab menurut plan"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2.1#p1", "§4.2.1#b2", "§4.2.1#b3", "§4.3#r1", "§4.3#r2", "§4.4#r1", "§4.4#r47", "§9.7#r16", "§9.10#p1", "EB-TBL-11", "EB-KOL-3"]
smoke: []
dependsOn: []
trace:
  "§4.2.1#p1": [2, 3, 7, 8, 32, 34, 36, 89, 91, 93, 95, 97]
  "§4.2.1#b2": [6, 15]
  "§4.2.1#b3": [4, 5, 11, 12, 21, 25, 29, 109, 114, 118, 120]
  "§4.3#r1": [4, 29]
  "§4.3#r2": [5, 6]
  "§4.4#r1": [47, 54, 68, 75]
  "§4.4#r47": [45, 64, 66]
  "§9.7#r16": 6
  "§9.10#p1": [2, 99, 100, 102, 103, 105, 123, 125, 126, 128, 131]
  EB-TBL-11: [37, 39]
  EB-KOL-3: [84, 86]
anchor: [10, 14, 18, 19, 27, 44, 51, 60, 63, 72, 80, 81, 107, 116, 122]
coverage:
  web: automated
---

# Halaman My Asset: tab, badge jumlah, breadcrumb, dan susunan tab menurut plan

## Prerequisites
- Aktor: Borrower, Assignee, dan PIC pengguna halaman My Asset.
- Layar awal: Halaman My Asset.
- Komponen: Halaman My Asset
- Data:
  - DU-101-1: Plan dengan Borrowing level `Full` dan Assignment `Tersedia`.
  - DU-101-2: Plan dengan Borrowing level `Basic` dan Assignment `Tidak tersedia`.
  - DU-101-3: Plan `Starter` dengan Borrowing level `None` dan Assignment `Tidak tersedia`.
  - DU-101-4: Plan dengan Borrowing level `None` dan Assignment `Tersedia`.
  - DU-101-5: dua Task `Confirm Handover` dengan Transaction ID `BRW-2026-0151` dan `BRW-2026-0152`, Group `Head Office`, Total Asset `6`, Handed Over By `Rina Wulandari`, Expires At `09/11/26, 20:41`.
  - DU-101-6: satu Task `Confirm Handover` dengan Transaction ID `ASG-2026-0072`, Group `Head Office`, Total Asset `2`, Handed Over By `Rina Wulandari`, Expires At `09/11/26, 20:48`.
  - DU-101-7: satu baris Borrowed berstatus `Overdue`: Name `Laptop Dell Latitude 5420 - 9`, Asset ID `LPT-2026-0009`, Group `Head Office`, Due Date `06/11/26`, Remaining `3 days overdue`, Borrower `Me`, Transaction ID `BRW-2026-0148`, Source `Admin`, Duration `4 days`, Handed Over At `03/11/26, 09:00`.
  - DU-101-8: sebelas baris Borrowed berstatus `Borrowed` dengan Name `Meeting Mic Set - 1` sampai `Meeting Mic Set - 11`, Asset ID `MIC-2026-1` sampai `MIC-2026-11`, Group `Head Office`, Due Date `10/11/26`, Remaining `Due in 1 day`, Borrower `Me`, Transaction ID `BRW-2026-0156`, Source `Admin`, Duration `4 days`, Handed Over At `07/11/26, 09:00`.
  - DU-101-9: pengguna tanpa Task aktif (`0`) dan tanpa baris Borrowed (`0`).
  - DU-101-10: satu baris History Borrow berstatus `Rejected`: Name `Excavator PC200 - 2`, Asset ID `EXC-2026-0008`, Group `Head Office`, Status `Rejected`, Holder `Me`, Type `Borrow`, Transaction ID `BRW-2026-0146`, Handed Over At `—`, Closed At `31/10/26, 11:30`.
  - DU-101-11: satu baris History Assignment berstatus `Unassigned`: Name `Projector Epson EB-X06 - 2`, Asset ID `PRJ-2026-0002`, Group `Head Office`, Status `Unassigned`, Holder `Me`, Type `Assignment`, Transaction ID `ASG-2026-0009`, Handed Over At `03/07/26, 10:00`, Closed At `30/10/26, 15:20`.
  - Badge jumlah yang diharapkan: tab `Task` `3` dari DU-101-5 dan DU-101-6, tab `Borrowed` `12` dari DU-101-7 dan DU-101-8, dan `11` dari DU-101-8 saja.
- Kondisi:
  - K1: plan DU-101-1; Task berisi DU-101-5 dan DU-101-6; Borrowed berisi DU-101-7 dan DU-101-8; Assigned dan History berisi daftar kosong.
  - K2: plan DU-101-1; Task dan Borrowed berisi DU-101-9; Assigned dan History berisi daftar kosong.
  - K3: plan DU-101-2; Task berisi DU-101-5; Borrowed berisi DU-101-8; History berisi daftar kosong.
  - K4: plan DU-101-4; Task berisi DU-101-5; Assigned dan History berisi daftar kosong.
  - K5: plan DU-101-3.
  - K6: plan DU-101-1; Task berisi DU-101-5 pada saat halaman tampil, lalu DU-101-6 masuk lewat pembaruan realtime; Borrowed berisi DU-101-8.
  - K7: plan DU-101-1; Task berisi DU-101-5; Borrowed berisi DU-101-8 saja, tanpa baris Overdue.
  - K8: seperti K1; pencarian `Latitude 5420 - 9` pada tab Borrowed dan saringan Status `Overdue` pada tab Borrowed masing-masing dijawab dengan satu baris, yaitu DU-101-7.
  - K9: plan DU-101-2 sesudah turun dari plan dengan Assignment; Task berisi DU-101-5 dan DU-101-6; Borrowed berisi DU-101-8; History berisi DU-101-10 dan DU-101-11.
  - K10: plan DU-101-1; Task berisi DU-101-5; Borrowed berisi DU-101-8 pada saat halaman tampil; DU-101-7 tercatat di server sesudahnya tanpa pembaruan realtime ke halaman.
  - K11: plan DU-101-1; Task berisi DU-101-5; Borrowed berisi DU-101-7 dan DU-101-8, yaitu keadaan K10 sesudah muat ulang.
  - K12: seperti K1; pencarian `ASG-2026-0072` pada tab Task dijawab satu baris, yaitu DU-101-6, dan saringan Total Asset `6` sampai `6` pada tab Task dijawab dua baris, yaitu DU-101-5.

## Test Steps

### Tab dan badge jumlah tampil pada plan dengan Borrowing dan Assignment
1. Tampilkan Halaman My Asset dengan kondisi K1
2. Verifikasi tab `Task`, `Borrowed`, `Assigned`, dan `History` tampil
3. Verifikasi Breadcrumb menampilkan `My Asset` dan `Task`
4. Verifikasi tab `Task` menampilkan badge jumlah `3`
5. Verifikasi tab `Borrowed` menampilkan badge jumlah `12`
6. Verifikasi badge tab `Borrowed` bertitik `danger` karena ada baris Overdue
7. Verifikasi tab `Assigned` tidak menampilkan badge jumlah
8. Verifikasi tab `History` tidak menampilkan badge jumlah

### Badge tidak tampil bila jumlahnya 0
9. Tampilkan Halaman My Asset dengan kondisi K2
10. Verifikasi tab `Task` dan tab `Borrowed` tampil
11. Verifikasi tab `Task` tidak menampilkan badge jumlah
12. Verifikasi tab `Borrowed` tidak menampilkan badge jumlah

### Titik danger tidak tampil tanpa baris Overdue
13. Tampilkan Halaman My Asset dengan kondisi K7
14. Verifikasi tab `Borrowed` menampilkan badge jumlah `11`
15. Verifikasi badge tab `Borrowed` tidak bertitik `danger`

### Badge Borrowed menghitung baris lintas halaman tanpa memandang Search dan Filter
16. Tampilkan Halaman My Asset dengan kondisi K8
17. Klik tab `Borrowed`
18. Verifikasi paginator tabel Borrowed menampilkan halaman `1` dan `2`
19. Verifikasi tab `Borrowed` menampilkan badge jumlah `12`
20. Ketik Search `Latitude 5420 - 9`, tekan Enter
21. Verifikasi badge tab `Borrowed` tetap `12`
22. Klik `Filter` pada toolbar
23. Pilih `Overdue` pada field `Status`
24. Klik `[Apply]`
25. Verifikasi badge tab `Borrowed` tetap `12`

### Badge Task bertambah saat Task baru masuk
26. Tampilkan Halaman My Asset dengan kondisi K6
27. Verifikasi tab `Task` menampilkan badge jumlah `2`
28. Satu Task baru masuk lewat pembaruan realtime
29. Verifikasi tab `Task` menampilkan badge jumlah `3`

### Breadcrumb mengikuti tab dan segmennya tidak bisa diklik
30. Tampilkan Halaman My Asset dengan kondisi K1
31. Klik tab `Borrowed`
32. Verifikasi Breadcrumb menampilkan `My Asset` dan `Borrowed`
33. Klik tab `Assigned`
34. Verifikasi Breadcrumb menampilkan `My Asset` dan `Assigned`
35. Klik tab `History`
36. Verifikasi Breadcrumb menampilkan `My Asset` dan `History`
37. Verifikasi segmen `My Asset` dan segmen `History` pada Breadcrumb bukan tautan
38. Klik segmen `My Asset` pada Breadcrumb
39. Verifikasi tab `History` tetap aktif

### Search tiap tab disimpan terpisah
40. Tampilkan Halaman My Asset dengan kondisi K8
41. Klik tab `Borrowed`
42. Ketik Search `Latitude 5420 - 9`, tekan Enter
43. Klik tab `Task`
44. Verifikasi tab `Task` aktif
45. Verifikasi kata kunci `Latitude 5420 - 9` tidak tampil pada Search tab `Task`
46. Klik tab `Borrowed`
47. Verifikasi Search tab `Borrowed` berisi `Latitude 5420 - 9`

### Sort tiap tab dipulihkan saat kembali
48. Tampilkan Halaman My Asset dengan kondisi K1
49. Klik tab `Borrowed`
50. Klik header kolom `Name`
51. Verifikasi header kolom `Name` terurut naik
52. Klik tab `Task`
53. Klik tab `Borrowed`
54. Verifikasi header kolom `Name` tetap terurut naik

### Filter tiap tab dipulihkan saat kembali
55. Tampilkan Halaman My Asset dengan kondisi K8
56. Klik tab `Borrowed`
57. Klik `Filter` pada toolbar
58. Pilih `Overdue` pada field `Status`
59. Klik `[Apply]`
60. Verifikasi ikon `Filter` menandai ada saringan yang diterapkan
61. Klik `Filter` pada toolbar untuk menutup panel
62. Klik tab `Task`
63. Verifikasi ikon `Filter` tampil pada tab `Task`
64. Verifikasi ikon `Filter` pada tab `Task` tidak menandai ada saringan yang diterapkan
65. Klik tab `Borrowed`
66. Verifikasi ikon `Filter` menandai ada saringan yang diterapkan
67. Klik `Filter` pada toolbar
68. Verifikasi field `Status` berisi `Overdue`

### Halaman aktif tiap tab dipulihkan saat kembali
69. Tampilkan Halaman My Asset dengan kondisi K1
70. Klik tab `Borrowed`
71. Klik halaman `2` pada paginator
72. Verifikasi halaman `2` aktif pada paginator
73. Klik tab `Task`
74. Klik tab `Borrowed`
75. Verifikasi halaman `2` tetap aktif pada paginator

### Konfigurasi kolom satu tabel tidak mengubah tabel lain
76. Tampilkan Halaman My Asset dengan kondisi K1
77. Klik tab `Borrowed`
78. Klik header kolom Actions `⋯`
79. Hilangkan centang kolom `Group`
80. Verifikasi header kolom `Name` tampil pada tabel Borrowed
81. Verifikasi header kolom `Group` tidak tampil pada tabel Borrowed
82. Tekan Esc
83. Klik tab `Task`
84. Verifikasi header kolom `Group` tampil pada tabel Task
85. Klik tab `Borrowed`
86. Verifikasi header kolom `Group` tetap tidak tampil pada tabel Borrowed

### Toolbar, paginasi, dan seleksi baris
87. Tampilkan Halaman My Asset dengan kondisi K1
88. Klik tab `Borrowed`
89. Verifikasi toolbar tab `Borrowed` memuat ikon `Search`, `Filter`, dan `Download`
90. Klik dropdown `Rows per page`
91. Verifikasi pilihan `10`, `25`, `50`, dan `100` tampil
92. Tekan Esc
93. Verifikasi baris tabel Borrowed memiliki checkbox
94. Klik tab `Assigned`
95. Verifikasi toolbar tab `Assigned` memuat ikon `Search`, `Filter`, dan `Download`
96. Klik tab `History`
97. Verifikasi toolbar tab `History` memuat ikon `Search`, `Filter`, dan `Download`

### Susunan tab pada plan tanpa Assignment
98. Tampilkan Halaman My Asset dengan kondisi K3
99. Verifikasi tab `Task`, `Borrowed`, dan `History` tampil
100. Verifikasi tab `Assigned` tidak tampil

### Susunan tab pada plan tanpa Borrowing
101. Tampilkan Halaman My Asset dengan kondisi K4
102. Verifikasi tab `Task`, `Assigned`, dan `History` tampil
103. Verifikasi tab `Borrowed` tidak tampil

### Susunan tab pada plan tanpa Borrowing dan Assignment
104. Tampilkan Halaman My Asset dengan kondisi K5
105. Verifikasi tab `Task`, `Borrowed`, `Assigned`, dan `History` tidak tampil

### Badge Task menghitung seluruh Task tanpa memandang Search dan Filter
106. Tampilkan Halaman My Asset dengan kondisi K12
107. Verifikasi tab `Task` menampilkan badge jumlah `3`
108. Ketik Search `ASG-2026-0072`, tekan Enter
109. Verifikasi badge tab `Task` tetap `3`
110. Klik `Filter` pada toolbar
111. Isi `Min` pada field `Total Asset` dengan `6`
112. Isi `Max` pada field `Total Asset` dengan `6`
113. Klik `[Apply]`
114. Verifikasi badge tab `Task` tetap `3`

### Badge Borrowed tidak berubah secara realtime dan diperbarui saat muat ulang
115. Tampilkan Halaman My Asset dengan kondisi K10
116. Verifikasi tab `Borrowed` menampilkan badge jumlah `11`
117. Satu baris Borrowed baru tercatat di server tanpa pembaruan realtime ke halaman
118. Verifikasi tab `Borrowed` tetap menampilkan badge jumlah `11`
119. Tampilkan Halaman My Asset dengan kondisi K11
120. Verifikasi tab `Borrowed` menampilkan badge jumlah `12`

### Task Assignment tidak tampil dan History tetap memuat riwayat Borrow dan Assignment pada plan tanpa Assignment
121. Tampilkan Halaman My Asset dengan kondisi K9
122. Verifikasi Task `BRW-2026-0151` dan `BRW-2026-0152` tampil pada tabel Task
123. Verifikasi Task `ASG-2026-0072` tidak tampil pada tabel Task
124. Klik tab `History`
125. Verifikasi baris `Excavator PC200 - 2` dengan Type `Borrow` tampil pada tabel History
126. Verifikasi baris `Projector Epson EB-X06 - 2` dengan Type `Assignment` tampil pada tabel History
127. Klik menu `⋯` pada baris `Excavator PC200 - 2`
128. Verifikasi menu baris hanya memuat aksi `Borrow Log`
129. Tekan Esc
130. Klik menu `⋯` pada baris `Projector Epson EB-X06 - 2`
131. Verifikasi menu baris hanya memuat aksi `Assignment Log`
132. Tekan Esc

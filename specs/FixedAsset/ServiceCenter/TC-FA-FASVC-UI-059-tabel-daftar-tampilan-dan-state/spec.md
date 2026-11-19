---
id: TC-FA-FASVC-UI-059-tabel-daftar-tampilan-dan-state
title: "Tabel Daftar: Kolom, Format, Chip +N more, Nilai Kosong, Empty, dan Gagal Muat"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["T-FASVC-01", "S-FASVC-01", "S-FASVC-02", "S-FASVC-03", "S-FASVC-05", "S-FASVC-15", "ST-FASVC-01", "ST-FASVC-02", "§4.1#r1", "§4.1#r7", "§4.2.1#p1", "§4.2.1#p2", "§4.2.7#p1", "§5#b1", "§5#b7", "§4.5#p1", "EB-TBL-1@tabel-service-center", "EB-TBL-2@kolom-specialization", "EB-TBL-2@kolom-available-to", "EB-TBL-2@kolom-brands", "EB-TBL-3@kolom-specialization", "EB-TBL-3@kolom-available-to", "EB-TBL-3@kolom-brands", "EB-TBL-4@modified-by-daftar", "EB-TBL-7@tabel-service-center", "EB-TBL-8@tabel-service-center", "EB-TBL-12", "EB-XM-1"]
smoke: []
dependsOn: []
trace:
  "T-FASVC-01": [5, 6, 9, 11, 12, 13, 15, 19, 22, 26, 27, 32, 36, 60, 61, 63, 65, 67, 69, 71, 72, 73, 75, 76, 77, 78, 80, 82, 83, 85, 86, 88, 89, 91, 92, 94, 95, 97, 98, 100, 101, 103, 104, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 124, 127, 129, 133, 174, 176, 178, 180, 182]
  "S-FASVC-01": [135]
  "S-FASVC-02": [137, 138, 139]
  "S-FASVC-03": [142, 143]
  "S-FASVC-05": [146, 147, 150]
  "S-FASVC-15": [75, 76, 77, 78]
  "ST-FASVC-01": [75]
  "ST-FASVC-02": [77]
  "§4.1#r1": [2]
  "§4.1#r7": [40, 41, 47, 48, 54, 55]
  "§4.2.1#p1": [2, 5, 7]
  "§4.2.1#p2": [2, 3, 4]
  "§4.2.7#p1": [40, 41, 42, 44, 47, 48, 49, 51, 54, 55, 56, 58]
  "§5#b1": [5, 142]
  "§5#b7": [8, 9]
  "§4.5#p1": [75, 77, 170, 171]
  "EB-TBL-1@tabel-service-center": [137, 142, 144, 146, 148]
  "EB-TBL-2@kolom-specialization": [15]
  "EB-TBL-2@kolom-available-to": [22]
  "EB-TBL-2@kolom-brands": [32]
  "EB-TBL-3@kolom-specialization": [15, 16, 17, 18, 19, 20]
  "EB-TBL-3@kolom-available-to": [22, 23, 24, 25, 26, 27, 28, 29, 30]
  "EB-TBL-3@kolom-brands": [32, 33, 34, 35, 36, 37]
  "EB-TBL-4@modified-by-daftar": [80, 82, 83, 85, 86, 88, 89, 91, 92, 94, 95, 97]
  "EB-TBL-7@tabel-service-center": [153, 155, 159, 162, 164, 167]
  "EB-TBL-8@tabel-service-center": [109]
  "EB-TBL-12": [106, 107]
  "EB-XM-1": [100, 101, 103, 104]
anchor: []
coverage:
  web: automated
---
# Tabel Daftar: Kolom, Format, Chip +N more, Nilai Kosong, Empty, dan Gagal Muat

## Prerequisites
- Aktor: Total Control; pada K11 Asset Admin dengan cakupan Group `Branch Surabaya` dan `Branch Bandung`.
- Layar awal: Add-ons > Service Center, halaman daftar Service Center.
- Komponen: Tabel Service Center
- Data:
  - DU-059-1: Service Center `PT Sejuk Abadi Teknik`, Service Type `Routine, Repair`, Specialization diterima berurutan `Refrigeration, Generator, AC`, Available To `All groups` (seluruh 5 Group master), City `Jakarta Selatan`, alamat `Jl. Wolter Monginsidi No. 25`, Province `DKI Jakarta`, Postal code `12110`, Country `Indonesia`, Brands diterima berurutan `LG, Panasonic, Daikin`, Usage `148` (Schedules `12`, Open tasks `30`, Completed tasks `90`, Other tasks `6`, Repair orders `10`), Status `Active`, Modified By `Alexander Graham Bell`, Last Updated `2026-03-25T09:15:00Z`.
  - DU-059-2: Service Center `CV Genset Prima`, Service Type `Routine`, Specialization `Generator`, Available To diterima berurutan `Branch Surabaya, Branch Malang`, City `Surabaya`, Brands kosong, Usage `24` (Schedules `4`, Open tasks `8`, Completed tasks `10`, Other tasks `2`, Repair orders `0`), Status `Active`, Modified By `Rina Wijaya`, Last Updated `2026-03-24T23:30:00Z`.
  - DU-059-3: Service Center `Bengkel Maju Motor`, Service Type `Repair`, Specialization diterima berurutan `Refrigeration, AC`, Available To `Branch Bandung`, City `Bandung`, Brands `Daikin`, Usage `0`, Status `Inactive`, Modified By `Budi`, Last Updated `2026-03-20T08:05:00Z`.
  - DU-059-4: Service Center `Lab Kalibrasi Pratama`, Service Type `Routine`, Specialization kosong, Available To diterima berurutan `Branch Malang, Branch Bandung, Branch Jakarta`, City `Johor Bahru`, Country `Malaysia` (negara company `Indonesia`), Brands diterima berurutan `Panasonic, LG`, Usage `3`, Status `Active`, Modified By `Buzzlightyear Sumardi`, Last Updated `2026-03-18T14:40:00Z`.
  - DU-059-5: Service Center `UD Cahaya Servis`, Service Type `Repair`, Specialization `Vehicle`, Available To kosong, City `Malang`, Address line, Province / State, dan Postal code kosong, Country `Indonesia`, Brands kosong, Usage `0`, Status `Inactive`, Modified By `System`, Last Updated `2026-03-19T10:00:00Z`.
  - DU-059-6: Service Center `Servis Pendingin Nusantara`, Service Type `Routine`, Specialization `AC`, Available To diterima berurutan `Branch Surabaya, Branch Jakarta, Branch Malang, Branch Bandung` (4 dari 5 Group master, tanpa `Head Office`), City `Semarang`, Brands `Panasonic`, Usage `7`, Status `Active`, Modified By `Dewi Anggraini`, Last Updated `2026-03-17T07:20:00Z`.
  - DU-059-7: Service Center `Teknik Mandiri Utama`, Service Type `Routine`, Specialization `Generator`, Available To `Branch Surabaya`, City `Surabaya`, Brands `LG`, Usage `12`, Status `Active`, Modified By `Dewi Anggreni`, Last Updated `2026-03-16T07:20:00Z`.
  - DU-059-8: Service Center `<b>Servis Kilat</b>`, Service Type `Repair`, Specialization kosong, Available To `Branch Surabaya`, City `Surabaya`, Brands kosong, Usage `1`, Status `Active`, Modified By `Rina Wijaya`, Last Updated `2026-03-15T07:20:00Z`.
  - DU-059-9: Pengaturan General Settings: Date Format `dd/MM/yy`, Time Format `24h`, Time Zone `UTC`.
  - DU-059-10: Pengaturan General Settings: Date Format `M/d/yy`, Time Format `24h`, Time Zone `UTC`.
  - DU-059-11: `25` Service Center `Servis Teknik Nusantara {n}`, Service Type `Routine`, Status `Active`.
  - DU-059-12: Isi Jump to page yang tidak valid: `99` (di atas halaman terakhir), `0` (di bawah 1), dan `abc` (bukan angka).
  - DU-059-14: Path lengkap node pada popover: Group `Head Office > Branch Surabaya`, `Head Office > Branch Malang`, `Head Office > Branch Bandung`, dan `Head Office > Branch Jakarta`; Category `Cooling > AC`, `Cooling > Refrigeration`, dan `Power > Generator`.
  - DU-059-15: Service Center `Servis Terpadu Selatan`, Service Type `Routine`, Specialization `AC`, Available To `Branch Surabaya`, City `Surabaya`, Brands `Daikin`, Usage yang terlihat aktor `0` (Schedules `0`, Open tasks `0`, Completed tasks `0`, Other tasks `0`, Repair orders `0`), Status `Active`, Modified By `Rina Wijaya`, Last Updated `2026-03-14T07:20:00Z`; seluruh rujukannya ada pada aset di Group `Branch Malang`, di luar cakupan aktor, sehingga menurut penghitungan server atas seluruh client Service Center ini sudah dipakai.
  - Last Updated DU-059-1 `2026-03-25T09:15:00Z` tampil `25/03/26, 09:15` pada DU-059-9 dan `3/25/26, 09:15` pada DU-059-10; Last Updated DU-059-2 `2026-03-24T23:30:00Z` tampil `24/03/26, 23:30` pada DU-059-9 dan `3/24/26, 23:30` pada DU-059-10.
- Kondisi:
  - K1: pengaturan memakai DU-059-9; daftar memuat DU-059-1 sampai DU-059-7 di halaman pertama; Group master berjumlah 5 (`Head Office`, `Branch Surabaya`, `Branch Malang`, `Branch Bandung`, `Branch Jakarta`); negara company `Indonesia`; bahasa antarmuka English; hierarki Group master: `Head Office` adalah induk `Branch Surabaya`, `Branch Malang`, `Branch Bandung`, dan `Branch Jakarta`; hierarki Category master: `Cooling` adalah induk `AC` dan `Refrigeration`, `Power` adalah induk `Generator`.
  - K2: pengaturan memakai DU-059-10; daftar memuat DU-059-1 dan DU-059-2.
  - K3: bahasa antarmuka Indonesia; pengaturan memakai DU-059-9; daftar memuat DU-059-1 dan DU-059-3.
  - K4: pengaturan memakai DU-059-9; respons daftar tertunda.
  - K5: pengaturan memakai DU-059-9; respons daftar kosong tanpa Service Center.
  - K6: pengaturan memakai DU-059-9; daftar memuat DU-059-1 sampai DU-059-7; respons Search `Vendor Tidak Ada` kosong.
  - K7: pengaturan memakai DU-059-9; respons daftar pertama gagal karena error server, respons sesudah `[Try Again]` memuat DU-059-3.
  - K8: pengaturan memakai DU-059-9; respons daftar memuat DU-059-11 dengan total `25` Service Center, `10` baris per halaman; urutan sort mengikuti permintaan.
  - K9: pengaturan memakai DU-059-9; daftar memuat DU-059-8.
  - K10: lebar layar sempit sehingga seluruh kolom tabel tidak muat; pengaturan memakai DU-059-9; daftar memuat DU-059-1 sampai DU-059-7.
  - K11: pengaturan memakai DU-059-9; aktor Asset Admin dengan cakupan Group `Branch Surabaya` dan `Branch Bandung`; daftar memuat DU-059-3 dan DU-059-15; respons menyatakan DU-059-15 sudah dipakai menurut penghitungan server atas seluruh client walau rujukan yang terlihat aktor `0`, dan DU-059-3 tidak dipakai.

## Test Steps

### Halaman daftar memuat breadcrumb, toolbar, kolom, dan paginasi tanpa bulk action
1. Tampilkan Tabel Service Center dengan kondisi K1
2. Verifikasi breadcrumb memuat `Add-ons > Service Center`
3. Verifikasi segmen `Add-ons` dan `Service Center` pada breadcrumb bukan tautan
4. Verifikasi tidak ada judul halaman tambahan di bawah breadcrumb
5. Verifikasi toolbar memuat `Search`, `Filter`, `Download`, `Changelog`, dan `[+ Service Center]`
6. Verifikasi tabel memuat kolom `Name`, `Service Type`, `Specialization`, `Available To`, `City`, `Brands`, `Usage`, `Status`, `Modified By`, dan `Last Updated`
7. Verifikasi paginasi tampil di bawah tabel
8. Verifikasi tabel tidak memuat kolom checkbox untuk memilih baris
9. Verifikasi baris terurut Name A-Z: `Bengkel Maju Motor`, `CV Genset Prima`, `Lab Kalibrasi Pratama`, `PT Sejuk Abadi Teknik`, `Servis Pendingin Nusantara`, `Teknik Mandiri Utama`, `UD Cahaya Servis`

### Kolom Name berupa tautan dan Service Type menampilkan badge nilai
10. Tampilkan Tabel Service Center dengan kondisi K1
11. Verifikasi Name `PT Sejuk Abadi Teknik` berupa tautan ke Detail Service Center
12. Verifikasi Service Type baris `PT Sejuk Abadi Teknik` memuat badge `Routine` dan `Repair`
13. Verifikasi Service Type baris `CV Genset Prima` memuat badge `Routine`

### Kolom Specialization menampilkan nol, satu, dua, dan lebih dari dua Category
14. Tampilkan Tabel Service Center dengan kondisi K1
15. Verifikasi Specialization baris `Lab Kalibrasi Pratama` menampilkan `All categories`
16. Verifikasi Specialization baris `CV Genset Prima` menampilkan badge `Generator`
17. Verifikasi Specialization baris `Bengkel Maju Motor` menampilkan badge `AC` lalu `Refrigeration`
18. Verifikasi Specialization baris `PT Sejuk Abadi Teknik` menampilkan badge `AC` dan `Generator`
19. Verifikasi Specialization baris `PT Sejuk Abadi Teknik` menampilkan chip `+1 more`
20. Verifikasi badge `Refrigeration` tidak tampil di sel Specialization baris `PT Sejuk Abadi Teknik`

### Kolom Available To menampilkan nol, satu, dua, lebih dari dua, semua, dan total kurang satu Group
21. Tampilkan Tabel Service Center dengan kondisi K1
22. Verifikasi Available To baris `UD Cahaya Servis` menampilkan `—`
23. Verifikasi Available To baris `Bengkel Maju Motor` menampilkan badge `Branch Bandung`
24. Verifikasi Available To baris `CV Genset Prima` menampilkan badge `Branch Malang` lalu `Branch Surabaya`
25. Verifikasi Available To baris `Lab Kalibrasi Pratama` menampilkan badge `Branch Bandung` dan `Branch Jakarta`
26. Verifikasi Available To baris `Lab Kalibrasi Pratama` menampilkan chip `+1 more`
27. Verifikasi Available To baris `PT Sejuk Abadi Teknik` menampilkan `All groups`
28. Verifikasi Available To baris `Servis Pendingin Nusantara` menampilkan badge `Branch Bandung` dan `Branch Jakarta`
29. Verifikasi Available To baris `Servis Pendingin Nusantara` menampilkan chip `+2 more`
30. Verifikasi `All groups` tidak tampil di Available To baris `Servis Pendingin Nusantara`

### Kolom Brands menampilkan nol, satu, dua, dan lebih dari dua Brand
31. Tampilkan Tabel Service Center dengan kondisi K1
32. Verifikasi Brands baris `CV Genset Prima` menampilkan `All brands`
33. Verifikasi Brands baris `Bengkel Maju Motor` menampilkan badge `Daikin`
34. Verifikasi Brands baris `Lab Kalibrasi Pratama` menampilkan badge `LG` lalu `Panasonic`
35. Verifikasi Brands baris `PT Sejuk Abadi Teknik` menampilkan badge `Daikin` dan `LG`
36. Verifikasi Brands baris `PT Sejuk Abadi Teknik` menampilkan chip `+1 more`
37. Verifikasi badge `Panasonic` tidak tampil di sel Brands baris `PT Sejuk Abadi Teknik`

### Chip +N more pada kolom Specialization membuka daftar nilai lengkap
38. Tampilkan Tabel Service Center dengan kondisi K1
39. Klik chip `+1 more` pada Specialization baris `PT Sejuk Abadi Teknik`
40. Verifikasi daftar berjudul `Specialization` tampil
41. Verifikasi daftar memuat path `Cooling > AC`, `Power > Generator`, dan `Cooling > Refrigeration`
42. Verifikasi daftar tidak memuat tombol `Close`
43. Klik icon close pada daftar
44. Verifikasi daftar tertutup

### Chip +N more pada kolom Available To membuka daftar nilai lengkap
45. Tampilkan Tabel Service Center dengan kondisi K1
46. Klik chip `+1 more` pada Available To baris `Lab Kalibrasi Pratama`
47. Verifikasi daftar berjudul `Available To` tampil
48. Verifikasi daftar memuat path `Head Office > Branch Bandung`, `Head Office > Branch Jakarta`, dan `Head Office > Branch Malang`
49. Verifikasi daftar tidak memuat tombol `Close`
50. Klik icon close pada daftar
51. Verifikasi daftar tertutup

### Chip +N more pada kolom Brands membuka daftar nilai lengkap
52. Tampilkan Tabel Service Center dengan kondisi K1
53. Klik chip `+1 more` pada Brands baris `PT Sejuk Abadi Teknik`
54. Verifikasi daftar berjudul `Brands` tampil
55. Verifikasi daftar memuat `Daikin`, `LG`, dan `Panasonic`
56. Verifikasi daftar tidak memuat tombol `Close`
57. Klik icon close pada daftar
58. Verifikasi daftar tertutup

### Kolom City menampilkan kota, negara bila beda, dan alamat lengkap saat hover
59. Tampilkan Tabel Service Center dengan kondisi K1
60. Verifikasi City baris `PT Sejuk Abadi Teknik` menampilkan `Jakarta Selatan`
61. Verifikasi City baris `Lab Kalibrasi Pratama` menampilkan `Johor Bahru, Malaysia`
62. Arahkan kursor ke City baris `PT Sejuk Abadi Teknik`
63. Verifikasi alamat lengkap `Jl. Wolter Monginsidi No. 25, Jakarta Selatan, DKI Jakarta, 12110, Indonesia` tersampaikan berurutan Address line, City, Province / State, Postal code, Country, dipisah koma dan spasi
64. Arahkan kursor ke City baris `UD Cahaya Servis`
65. Verifikasi alamat lengkap `Malang, Indonesia` tersampaikan

### Kolom Usage menampilkan angka, rincian per konsumen saat hover, dan nol
66. Tampilkan Tabel Service Center dengan kondisi K1
67. Verifikasi Usage baris `PT Sejuk Abadi Teknik` menampilkan `148`
68. Arahkan kursor ke Usage baris `PT Sejuk Abadi Teknik`
69. Verifikasi rincian `Schedules: 12 · Open tasks: 30 · Completed tasks: 90 · Other tasks: 6 · Repair orders: 10` tersampaikan
70. Arahkan kursor ke Usage baris `CV Genset Prima`
71. Verifikasi rincian `Schedules: 4 · Open tasks: 8 · Completed tasks: 10 · Other tasks: 2 · Repair orders: 0` tersampaikan
72. Verifikasi Usage baris `Bengkel Maju Motor` menampilkan `0`
73. Verifikasi Usage baris `PT Sejuk Abadi Teknik` berupa tautan ke tab Usage pada Detail Service Center

### Kolom Status menampilkan badge Active dan Inactive dengan teks
74. Tampilkan Tabel Service Center dengan kondisi K1
75. Verifikasi Status baris `CV Genset Prima` menampilkan badge `Active`
76. Verifikasi badge Status `Active` bersemantik `success`
77. Verifikasi Status baris `Bengkel Maju Motor` menampilkan badge `Inactive`
78. Verifikasi badge Status `Inactive` bersemantik `danger`

### Kolom Modified By menampilkan nama singkat dan nama lengkap saat hover
79. Tampilkan Tabel Service Center dengan kondisi K1
80. Verifikasi Modified By baris `Bengkel Maju Motor` menampilkan `Budi`
81. Arahkan kursor ke Modified By baris `Bengkel Maju Motor`
82. Verifikasi nama lengkap `Budi` tersampaikan
83. Verifikasi Modified By baris `CV Genset Prima` menampilkan `Rina W`
84. Arahkan kursor ke Modified By baris `CV Genset Prima`
85. Verifikasi nama lengkap `Rina Wijaya` tersampaikan
86. Verifikasi Modified By baris `PT Sejuk Abadi Teknik` menampilkan `Alexander G`
87. Arahkan kursor ke Modified By baris `PT Sejuk Abadi Teknik`
88. Verifikasi nama lengkap `Alexander Graham Bell` tersampaikan
89. Verifikasi Modified By baris `Lab Kalibrasi Pratama` menampilkan `Buzzlightyear S`
90. Arahkan kursor ke Modified By baris `Lab Kalibrasi Pratama`
91. Verifikasi nama lengkap `Buzzlightyear Sumardi` tersampaikan
92. Verifikasi Modified By baris `Servis Pendingin Nusantara` menampilkan `Dewi A`
93. Arahkan kursor ke Modified By baris `Servis Pendingin Nusantara`
94. Verifikasi nama lengkap `Dewi Anggraini` tersampaikan
95. Verifikasi Modified By baris `Teknik Mandiri Utama` menampilkan `Dewi A`
96. Arahkan kursor ke Modified By baris `Teknik Mandiri Utama`
97. Verifikasi nama lengkap `Dewi Anggreni` tersampaikan
98. Verifikasi Modified By baris `UD Cahaya Servis` menampilkan `System`

### Kolom Last Updated mengikuti Date Format dd/MM/yy dan Time Format 24h
99. Tampilkan Tabel Service Center dengan kondisi K1
100. Verifikasi Last Updated baris `PT Sejuk Abadi Teknik` menampilkan `25/03/26, 09:15`
101. Verifikasi Last Updated baris `CV Genset Prima` menampilkan `24/03/26, 23:30`

### Kolom Last Updated mengikuti Date Format M/d/yy
102. Tampilkan Tabel Service Center dengan kondisi K2
103. Verifikasi Last Updated baris `PT Sejuk Abadi Teknik` menampilkan `3/25/26, 09:15`
104. Verifikasi Last Updated baris `CV Genset Prima` menampilkan `3/24/26, 23:30`

### Nilai Service Type dan Name tampil persis pada bahasa antarmuka Indonesia
105. Tampilkan Tabel Service Center dengan kondisi K3
106. Verifikasi Service Type baris `PT Sejuk Abadi Teknik` memuat badge `Routine` dan `Repair`
107. Verifikasi Name baris `Bengkel Maju Motor` tampil `Bengkel Maju Motor`

### Markup pada Name tampil sebagai teks
108. Tampilkan Tabel Service Center dengan kondisi K9
109. Verifikasi Name `<b>Servis Kilat</b>` tampil apa adanya sebagai teks

### Panel Filter memuat label, tipe, dan placeholder setiap kolom yang bisa difilter
110. Tampilkan Tabel Service Center dengan kondisi K1
111. Klik `Filter`
112. Verifikasi filter `Service Type` berupa pilihan ganda dengan pencarian dan placeholder `All types`
113. Verifikasi filter `Specialization` berupa pilihan ganda berbentuk pohon dengan pencarian dan placeholder `All categories`
114. Verifikasi filter `Available To` berupa pilihan ganda berbentuk pohon dengan pencarian dan placeholder `All groups`
115. Verifikasi filter `City` berupa pilihan ganda dengan pencarian dan placeholder `All cities`
116. Verifikasi filter `Brands` berupa pilihan ganda dengan pencarian dan placeholder `All brands`
117. Verifikasi filter `Usage` berupa rentang dengan placeholder `Min` dan `Max`
118. Verifikasi filter `Status` berupa pilihan ganda dengan pencarian dan placeholder `All statuses`
119. Verifikasi filter `Modified By` berupa pilihan ganda dengan pencarian dan placeholder `All users`
120. Verifikasi filter `Last Updated` berupa rentang tanggal dengan placeholder `Select date`
121. Verifikasi tidak ada filter `Name`

### Semua kolom bisa disembunyikan lewat Column Visibility
122. Tampilkan Tabel Service Center dengan kondisi K1
123. Klik header kolom Actions `⋯`
124. Verifikasi setiap kolom `Name`, `Service Type`, `Specialization`, `Available To`, `City`, `Brands`, `Usage`, `Status`, `Modified By`, dan `Last Updated` tercentang dan aktif di daftar kolom

### Download menawarkan CSV dan XLSX dengan nama berkas Service-Centers
125. Tampilkan Tabel Service Center dengan kondisi K1
126. Klik `Download`
127. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil
128. Pilih `Download as CSV`
129. Verifikasi berkas terunduh bernama `Service-Centers.csv`

### Download XLSX memakai nama berkas Service-Centers
130. Tampilkan Tabel Service Center dengan kondisi K1
131. Klik `Download`
132. Pilih `Download as XLSX`
133. Verifikasi berkas terunduh bernama `Service-Centers.xlsx`

### Loading tampil selama daftar dimuat
134. Tampilkan Tabel Service Center dengan kondisi K4
135. Verifikasi komponen loading tampil

### Daftar kosong menampilkan empty state tanpa tombol
136. Tampilkan Tabel Service Center dengan kondisi K5
137. Verifikasi `No service centers yet` tampil
138. Verifikasi `Get started by creating your first service center.` tampil
139. Verifikasi empty state tidak memuat tombol

### Hasil pencarian kosong menampilkan No results found
140. Tampilkan Tabel Service Center dengan kondisi K6
141. Ketik Search `Vendor Tidak Ada`, tekan Enter
142. Verifikasi `No results found` tampil
143. Verifikasi `Try adjusting your search or filter.` tampil
144. Verifikasi `No service centers yet` tidak tampil

### Gagal memuat menampilkan pesan error dengan Try Again, bukan empty state
145. Tampilkan Tabel Service Center dengan kondisi K7
146. Verifikasi `Unable to load this data.` tampil
147. Verifikasi tombol `[Try Again]` tampil
148. Verifikasi `No service centers yet` dan `No results found` tidak tampil
149. Klik `[Try Again]`
150. Verifikasi baris `Bengkel Maju Motor` tampil

### Ganti page size kembali ke halaman 1
151. Tampilkan Tabel Service Center dengan kondisi K8
152. Klik halaman `2`
153. Verifikasi laporan paginasi `Showing 11 to 20 of 25` tampil
154. Pilih `25` pada Rows per page
155. Verifikasi laporan paginasi `Showing 1 to 25 of 25` tampil

### Ganti sort tetap di halaman sekarang
156. Tampilkan Tabel Service Center dengan kondisi K8
157. Klik halaman `2`
158. Klik header kolom `Name`
159. Verifikasi laporan paginasi `Showing 11 to 20 of 25` tetap tampil

### Nomor halaman tidak valid mengikuti perilaku Paginator
160. Tampilkan Tabel Service Center dengan kondisi K8
161. Isi Jump to page dengan `99`, tekan Enter
162. Verifikasi laporan paginasi `Showing 21 to 25 of 25` tampil
163. Isi Jump to page dengan `0`, tekan Enter
164. Verifikasi laporan paginasi `Showing 1 to 10 of 25` tampil
165. Klik halaman `2`
166. Isi Jump to page dengan `abc`, tekan Enter
167. Verifikasi laporan paginasi `Showing 11 to 20 of 25` tetap tampil

### Layar sempit: tabel bergulir horizontal dan kolom Actions tetap terlihat
168. Tampilkan Tabel Service Center dengan kondisi K10
169. Gulir tabel secara horizontal ke kolom paling kanan
170. Verifikasi tabel dapat digulir horizontal
171. Verifikasi kolom `Actions` pada baris `PT Sejuk Abadi Teknik` tetap terlihat

### Usage terbatas cakupan aktor tetap memblokir Delete berdasarkan total rujukan server
172. Tampilkan Tabel Service Center dengan kondisi K11
173. Klik menu `⋯` pada baris `Bengkel Maju Motor`
174. Verifikasi aksi `Delete` pada baris `Bengkel Maju Motor` aktif
175. Tutup menu `⋯` pada baris `Bengkel Maju Motor`
176. Verifikasi Usage baris `Servis Terpadu Selatan` menampilkan `0`
177. Arahkan kursor ke Usage baris `Servis Terpadu Selatan`
178. Verifikasi rincian `Schedules: 0 · Open tasks: 0 · Completed tasks: 0 · Other tasks: 0 · Repair orders: 0` tersampaikan
179. Klik menu `⋯` pada baris `Servis Terpadu Selatan`
180. Verifikasi aksi `Delete` pada baris `Servis Terpadu Selatan` disabled
181. Arahkan kursor ke aksi `Delete` pada baris `Servis Terpadu Selatan`
182. Verifikasi alasan `This service center has been used. Inactivate it instead.` tersampaikan pada aksi `Delete` yang disabled

---
id: TC-FA-FASVC-UI-064-halaman-detail-tampilan-dan-breadcrumb
title: "Halaman Detail: Tab, Breadcrumb, Info Cakupan, dan Aksi Setelah Edit atau Hapus"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#r3", "§4.1#r4", "§4.2.3#b5", "§2.2#p1", "EB-TBL-11", "§4.2.3#b4", "§4.2.3#p1"]
smoke: []
dependsOn: []
trace:
  "§4.1#r3": [13, 75, 76, 77]
  "§4.1#r4": [20]
  "§4.2.3#b5": [83, 84, 85, 86, 88, 93, 94, 95, 96, 98, 103, 104, 105, 106, 108, 113, 114, 115, 116, 117, 118, 120]
  "§2.2#p1": [122, 123, 125, 126, 128, 129, 131, 132]
  "EB-TBL-11": [2, 3, 4, 5, 8, 10]
  "§4.2.3#b4": [56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 136, 139]
  "§4.2.3#p1": [2, 12, 13, 14, 15, 18, 19, 22, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 43, 44, 45, 48, 51, 54, 76, 77]
anchor: [135, 138]
coverage:
  web: automated
---
# Halaman Detail: Tab, Breadcrumb, Info Cakupan, dan Aksi Setelah Edit atau Hapus

## Prerequisites
- Aktor: Total Control, Asset Admin (Maintenance Routine, cakupan `Branch Surabaya`), Group Manager (cakupan `Branch Surabaya`), Monitoring & Report (cakupan `Branch Surabaya`), dan Read Only (cakupan `Branch Surabaya`); tiap kondisi menyebut aktor yang dipakai.
- Layar awal: Add-ons > Service Center > Detail.
- Komponen: Halaman Service Center Detail
- Data:
  - DU-064-1: Service Center `PT Sejuk Abadi Teknik`: Service type `Routine, Repair`, Available to `Branch Surabaya, Branch Malang, Branch Bandung`, Specialization `Refrigeration, Generator, AC`, Brands `LG, Panasonic, Daikin`, Country `Indonesia`, Province / State `DKI Jakarta`, City `Jakarta Selatan`, Postal code `12110`, Address line `Jl. Wolter Monginsidi No. 25`, Company phone `+62 2150001234`, Company email `servis@sejukabadi.co.id`, Contact person Name `Andi Pratama`, Phone `+62 8139988776`, Email `andi@sejukabadi.co.id`, Primary, Notes `Kontrak servis AC tahunan`, Attachments `kontrak-servis.pdf`, Status `Active`, Usage `148`, Created by `Rina Wijaya` pada `2026-03-10T09:15:00Z`, Last updated by `Dewi Anggraini` pada `2026-03-20T16:45:00Z`.
  - DU-064-2: Service Center `UD Cahaya Servis`: Service type `Repair`, Available to kosong, Specialization kosong, Brands kosong, Country `Indonesia`, City `Malang`, tanpa Province / State, tanpa Postal code, tanpa Address line, Company phone `+62 3415551122`, tanpa Company email, tanpa Notes, tanpa Attachments, tanpa Contact persons, Status `Inactive`, Usage `0`, Created by `Rina Wijaya` pada `2026-03-01T08:00:00Z`, Last updated by `System` pada `2026-03-19T10:00:00Z`.
  - DU-064-3: Respons Usage untuk DU-064-1: Active schedules `3`, Open tasks `2`, Completed `3`, dan baris Routine `Chiller Lantai 2` (Reference `TASK-00188`, Status `Completed`, Result `Normal`).
  - DU-064-4: Respons Detail DU-064-1 sesudah aksi: Notes `Kontrak servis AC dan chiller`, Last updated by `Rina Wijaya` pada `2026-03-21T11:00:00Z`, dan respons Usage Completed `4`.
  - DU-064-5: Isi Notes baru pada Edit: `Kontrak servis AC dan chiller`.
  - DU-064-6: Hitungan dampak Inactivate untuk DU-064-1: `3` Schedule aktif dan `4` Task terbuka.
  - DU-064-7: `14` Service Center aktif `Servis Teknik Nusantara {n}` ditambah `Servis Zenit Teknik` (Usage `0`, Status `Active`, Available to `Branch Surabaya`) sebagai baris ke-15 pada urutan Name naik; state daftar sebelum membuka Detail: Search `Servis`, Filter Status `Active`, Sort Name naik, halaman `2`, `10` baris per halaman.
  - DU-064-8: Service Center `Servis Gabungan Jawa`: Service type `Routine`, Available to `Branch Surabaya, Branch Malang` (`Branch Malang` di luar cakupan aktor), City `Malang`, Status `Active`, Usage `0`.
  - DU-064-10: Service Center `Servis Zenit Teknik`: Status `Active`, Usage `0`, Available to `Branch Surabaya`; baris ke-15 pada urutan Name naik di DU-064-7.
  - DU-064-11: Service Center `Servis Mitra Elektrik`: Service type `Routine`, Country `Indonesia`, City `Bandung`, tanpa Company phone, Company email `kontak@mitraelektrik.co.id`, Status `Active`, Usage `0`.
  - DU-064-9: Pengaturan General Settings: Date Format `dd/MM/yy`, Time Format `24h`, Time Zone `UTC`.
- Kondisi:
  - K1: aktor Total Control; Detail DU-064-1; respons Usage DU-064-3; pengaturan memakai DU-064-9; daftar Service Center memuat DU-064-1.
  - K2: aktor Total Control; Detail DU-064-2; pengaturan memakai DU-064-9.
  - K3: aktor Total Control; Detail DU-064-1 dengan Notes `Kontrak servis AC tahunan`; Edit DU-064-5 berhasil; respons Detail dan Usage sesudah Save memakai DU-064-4.
  - K4: aktor Total Control; Detail DU-064-1 berstatus `Active`; respons hitungan dampak DU-064-6; Inactivate berhasil; respons Detail dan Usage sesudahnya memakai DU-064-4 dengan Status `Inactive`.
  - K5: aktor Total Control; Detail DU-064-1 berstatus `Inactive`; Activate berhasil; respons Detail dan Usage sesudahnya memakai DU-064-4 dengan Status `Active`.
  - K6: aktor Total Control; Detail `Servis Zenit Teknik` dibuka dari daftar DU-064-7 pada state tersebut; Delete berhasil; daftar dimuat ulang dengan `14` Service Center.
  - K7: aktor Asset Admin; Detail DU-064-8.
  - K8: aktor Group Manager; Detail DU-064-8.
  - K9: aktor Monitoring & Report; Detail DU-064-8.
  - K10: aktor Read Only; Detail DU-064-8.
  - K11: aktor Total Control; Detail DU-064-11.

## Test Steps

### Breadcrumb Detail: segmen pertama dan terakhir statis, segmen tengah tautan
1. Tampilkan Halaman Service Center Detail dengan kondisi K1
2. Verifikasi breadcrumb memuat `Add-ons > Service Center > Detail`
3. Verifikasi segmen `Service Center` pada breadcrumb berupa tautan
4. Verifikasi segmen `Add-ons` pada breadcrumb bukan tautan
5. Verifikasi segmen `Detail` pada breadcrumb bukan tautan

### Pindah tab tidak mengubah breadcrumb
6. Tampilkan Halaman Service Center Detail dengan kondisi K1
7. Klik tab `Usage`
8. Verifikasi breadcrumb memuat `Add-ons > Service Center > Detail`
9. Klik tab `Overview`
10. Verifikasi breadcrumb memuat `Add-ons > Service Center > Detail`

### Header Detail memuat nama, badge Status, dan tab Overview dan Usage
11. Tampilkan Halaman Service Center Detail dengan kondisi K1
12. Verifikasi judul `PT Sejuk Abadi Teknik` dengan badge Status `Active` tampil
13. Verifikasi tab `Overview` dan `Usage` tampil berurutan
14. Verifikasi tab `Overview` aktif
15. Verifikasi tab `Usage` tidak aktif

### Menu header Active menawarkan Edit, Inactivate, dan Delete
16. Tampilkan Halaman Service Center Detail dengan kondisi K1
17. Klik `⋯` pada header
18. Verifikasi menu memuat `Edit`, `Inactivate`, dan `Delete` berurutan
19. Verifikasi `Activate` tidak tampil di menu
20. Verifikasi `Changelog` tidak tampil di menu header

### Menu header Inactive menawarkan Edit, Activate, dan Delete
21. Tampilkan Halaman Service Center Detail dengan kondisi K2
22. Verifikasi judul `UD Cahaya Servis` dengan badge Status `Inactive` tampil
23. Klik `⋯` pada header
24. Verifikasi menu memuat `Edit`, `Activate`, dan `Delete` berurutan
25. Verifikasi `Inactivate` tidak tampil di menu

### Overview menampilkan seluruh field dalam urutan
26. Tampilkan Halaman Service Center Detail dengan kondisi K1
27. Verifikasi field Overview berurutan: `Service type`, `Available to`, `Specialization`, `Brands`, `Country`, `Province / State`, `City`, `Postal code`, `Address line`, `Company phone`, `Company email`, `Contact persons`, `Notes`, `Attachments`, `Created by`, `Last updated by`
28. Verifikasi Service type menampilkan badge `Routine` dan `Repair`
29. Verifikasi Country menampilkan `Indonesia`
30. Verifikasi Province / State menampilkan `DKI Jakarta`
31. Verifikasi City menampilkan `Jakarta Selatan`
32. Verifikasi Postal code menampilkan `12110`
33. Verifikasi Address line menampilkan `Jl. Wolter Monginsidi No. 25`
34. Verifikasi Company phone menampilkan `+62 2150001234`
35. Verifikasi Company email menampilkan `servis@sejukabadi.co.id`
36. Verifikasi Notes menampilkan `Kontrak servis AC tahunan`
37. Verifikasi Attachments menampilkan `kontrak-servis.pdf` dengan pilihan unduh dan pratinjau

### Contact persons memuat Name, Phone, Email, dan Primary
38. Tampilkan Halaman Service Center Detail dengan kondisi K1
39. Verifikasi Contact persons memuat baris dengan Name `Andi Pratama`
40. Verifikasi baris `Andi Pratama` memuat Phone `+62 8139988776` dan Email `andi@sejukabadi.co.id`
41. Verifikasi baris `Andi Pratama` ditandai Primary

### Available to, Specialization, dan Brands berupa badge dengan chip +N more
42. Tampilkan Halaman Service Center Detail dengan kondisi K1
43. Verifikasi Available to menampilkan badge `Branch Bandung` dan `Branch Malang` serta chip `+1 more`
44. Verifikasi Specialization menampilkan badge `AC` dan `Generator` serta chip `+1 more`
45. Verifikasi Brands menampilkan badge `Daikin` dan `LG` serta chip `+1 more`

### Chip +N more pada Available to membuka popover daftar lengkap
46. Tampilkan Halaman Service Center Detail dengan kondisi K1
47. Klik chip `+1 more` pada Available to
48. Verifikasi popover memuat `Branch Bandung`, `Branch Malang`, dan `Branch Surabaya`

### Chip +N more pada Specialization membuka popover daftar lengkap
49. Tampilkan Halaman Service Center Detail dengan kondisi K1
50. Klik chip `+1 more` pada Specialization
51. Verifikasi popover memuat `AC`, `Generator`, dan `Refrigeration`

### Chip +N more pada Brands membuka popover daftar lengkap
52. Tampilkan Halaman Service Center Detail dengan kondisi K1
53. Klik chip `+1 more` pada Brands
54. Verifikasi popover memuat `Daikin`, `LG`, dan `Panasonic`

### Created by dan Last updated by memakai nama singkat dan waktu General Settings
55. Tampilkan Halaman Service Center Detail dengan kondisi K1
56. Verifikasi `Created by` menampilkan `Rina W` diikuti `10/03/26, 09:15`
57. Verifikasi `Last updated by` menampilkan `Dewi A` diikuti `20/03/26, 16:45`
58. Verifikasi label `Modified By` dan `Last Updated` tidak tampil di Overview

### Field opsional kosong menampilkan strip dan Specialization dan Brands kosong menampilkan semua
59. Tampilkan Halaman Service Center Detail dengan kondisi K2
60. Verifikasi Province / State menampilkan `—`
61. Verifikasi Postal code menampilkan `—`
62. Verifikasi Address line menampilkan `—`
63. Verifikasi Company phone menampilkan `+62 3415551122`
64. Verifikasi Company email menampilkan `—`
65. Verifikasi Notes menampilkan `—`
66. Verifikasi Attachments menampilkan `—`
67. Verifikasi Contact persons menampilkan `—`
68. Verifikasi Specialization menampilkan `All categories`
69. Verifikasi Brands menampilkan `All brands`

### Last updated by System untuk perubahan System
70. Tampilkan Halaman Service Center Detail dengan kondisi K2
71. Verifikasi `Created by` menampilkan `Rina W` diikuti `01/03/26, 08:00`
72. Verifikasi `Last updated by` menampilkan `System` diikuti `19/03/26, 10:00`

### Tab Usage memuat ringkasan dan tabel Usage
73. Tampilkan Halaman Service Center Detail dengan kondisi K1
74. Klik tab `Usage`
75. Verifikasi tab `Usage` aktif
76. Verifikasi ringkasan memuat `Active schedules: 3` dan `Completed: 3`
77. Verifikasi tabel Usage memuat baris `Chiller Lantai 2`

### Edit dari Detail tetap di Detail dan memuat ulang data terbaru
78. Tampilkan Halaman Service Center Detail dengan kondisi K3
79. Klik `⋯` pada header
80. Pilih `Edit`
81. Ganti isi Notes dengan `Kontrak servis AC dan chiller`
82. Klik `[Save]`
83. Verifikasi toast `Success, PT Sejuk Abadi Teknik has been updated.` tampil
84. Verifikasi breadcrumb memuat `Add-ons > Service Center > Detail`
85. Verifikasi Notes menampilkan `Kontrak servis AC dan chiller`
86. Verifikasi `Last updated by` menampilkan `Rina W` diikuti `21/03/26, 11:00`
87. Klik tab `Usage`
88. Verifikasi ringkasan memuat `Completed: 4`

### Inactivate dari Detail tetap di Detail dan memuat ulang data terbaru
89. Tampilkan Halaman Service Center Detail dengan kondisi K4
90. Klik `⋯` pada header
91. Pilih `Inactivate`
92. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
93. Verifikasi toast `Success, PT Sejuk Abadi Teknik has been inactivated.` tampil
94. Verifikasi breadcrumb memuat `Add-ons > Service Center > Detail`
95. Verifikasi judul `PT Sejuk Abadi Teknik` dengan badge Status `Inactive` tampil
96. Verifikasi `Last updated by` menampilkan `Rina W` diikuti `21/03/26, 11:00`
97. Klik tab `Usage`
98. Verifikasi ringkasan memuat `Completed: 4`

### Activate dari Detail tetap di Detail dan memuat ulang data terbaru
99. Tampilkan Halaman Service Center Detail dengan kondisi K5
100. Klik `⋯` pada header
101. Pilih `Activate`
102. Klik `[Activate]` pada dialog `Activate Service Center`
103. Verifikasi toast `Success, PT Sejuk Abadi Teknik has been activated.` tampil
104. Verifikasi breadcrumb memuat `Add-ons > Service Center > Detail`
105. Verifikasi judul `PT Sejuk Abadi Teknik` dengan badge Status `Active` tampil
106. Verifikasi `Last updated by` menampilkan `Rina W` diikuti `21/03/26, 11:00`
107. Klik tab `Usage`
108. Verifikasi ringkasan memuat `Completed: 4`

### Delete dari Detail kembali ke daftar dengan state dipertahankan
109. Tampilkan Halaman Service Center Detail dengan kondisi K6
110. Klik `⋯` pada header
111. Pilih `Delete`
112. Klik `[Delete]` pada dialog `Delete Service Center`
113. Verifikasi toast `Success, Servis Zenit Teknik has been deleted.` tampil
114. Verifikasi halaman daftar Service Center dengan breadcrumb `Add-ons > Service Center` tampil
115. Verifikasi kotak Search berisi `Servis`
116. Verifikasi kolom `Name` berindikator sort naik
117. Verifikasi laporan paginasi `Showing 11 to 14 of 14` tampil
118. Verifikasi baris `Servis Zenit Teknik` tidak tampil di daftar
119. Klik `Filter`
120. Verifikasi field Status menampilkan chip `Active`

### Asset Admin melihat info cakupan pada Service Center sebagian di luar cakupan
121. Tampilkan Halaman Service Center Detail dengan kondisi K7
122. Verifikasi judul `Servis Gabungan Jawa` tampil
123. Verifikasi info `This service center also serves groups outside your access. Ask an admin who manages all of them.` tampil

### Group Manager melihat info cakupan pada Service Center sebagian di luar cakupan
124. Tampilkan Halaman Service Center Detail dengan kondisi K8
125. Verifikasi judul `Servis Gabungan Jawa` tampil
126. Verifikasi info `This service center also serves groups outside your access. Ask an admin who manages all of them.` tampil

### Monitoring & Report tidak melihat info cakupan
127. Tampilkan Halaman Service Center Detail dengan kondisi K9
128. Verifikasi judul `Servis Gabungan Jawa` tampil
129. Verifikasi info `This service center also serves groups outside your access. Ask an admin who manages all of them.` tidak tampil

### Read Only tidak melihat info cakupan
130. Tampilkan Halaman Service Center Detail dengan kondisi K10
131. Verifikasi judul `Servis Gabungan Jawa` tampil
132. Verifikasi info `This service center also serves groups outside your access. Ask an admin who manages all of them.` tidak tampil

### Alamat tampil sebagai field terpisah tanpa hover alamat
133. Tampilkan Halaman Service Center Detail dengan kondisi K1
134. Arahkan kursor ke nilai City `Jakarta Selatan`
135. Verifikasi City tetap menampilkan `Jakarta Selatan`
136. Verifikasi tidak ada popover alamat lengkap yang tampil

### Company phone kosong menampilkan strip saat Company email terisi
137. Tampilkan Halaman Service Center Detail dengan kondisi K11
138. Verifikasi Company email menampilkan `kontak@mitraelektrik.co.id`
139. Verifikasi Company phone menampilkan `—`

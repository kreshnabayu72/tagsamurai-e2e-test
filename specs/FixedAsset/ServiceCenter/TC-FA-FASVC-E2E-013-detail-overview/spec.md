---
id: TC-FA-FASVC-E2E-013-detail-overview
title: "Halaman Detail: Tab Overview, Field Kosong, Created by dan Last updated by, serta Tombol Menu"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2.3#p1", "§4.2.3#b1", "§4.2.3#b2", "§4.2.3#b3", "§4.2.3#b4", "§4.2.3#b5", "§2.2#p2", "§4.1#r2", "EC-FASVC-44", "EC-FASVC-55", "F-FASVC-02.k16"]
smoke: []
dependsOn: []
trace:
  "§4.2.3#p1": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 38]
  "§4.2.3#b1": [5, 37]
  "§4.2.3#b2": 38
  "§4.2.3#b3": [28, 29, 30, 86, 87]
  "§4.2.3#b4": [11, 12, 13, 14, 15, 22, 23, 24, 25, 34, 35, 44, 45, 46, 47, 48, 49, 50, 51]
  "§4.2.3#b5": [78, 79, 83, 84, 90, 91, 98, 99, 100]
  "§2.2#p2": [112, 116, 121, 126]
  "§4.1#r2": 4
  "EC-FASVC-44": [2, 102, 108]
  "EC-FASVC-55": [42, 43]
  "F-FASVC-02.k16": [43, 56, 60, 65, 66, 70]
anchor: [55, 120, 125]
coverage:
  web: automated
---

# Halaman Detail: Tab Overview, Field Kosong, Created by dan Last updated by, serta Tombol Menu

## Prerequisites
- Aktor: Total Control. Aktor lain: Group Manager `Rudi Hartono {runId}`, Asset Admin `Maya Puspita {runId}`, Monitoring & Report `Sari Lestari {runId}`, dan Read Only `Tono Prasetyo {runId}`.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-013-1: Group `Cabang Timur {runId}` dan Group `Cabang Barat {runId}`, tidak saling induk.
  - DU-013-2: Category `Pendingin Udara {runId}` ada di master Category; Brand `Daikin {runId}` ada di master Brand.
  - DU-013-3: User `Rina Wulandari {runId}` dan User `Dewi Anggraini {runId}`, masing-masing Role `Total Control`, cakupan Group `All groups`.
  - DU-013-4: User `Rudi Hartono {runId}`, Role `Group Manager`, cakupan Group `Cabang Timur {runId}`; User `Maya Puspita {runId}`, Role `Asset Admin` dengan Role Transaksi Maintenance Routine, cakupan Group `Cabang Timur {runId}`; User `Sari Lestari {runId}`, Role `Monitoring & Report` dengan Role Transaksi Maintenance Routine, cakupan Group `Cabang Timur {runId}`; User `Tono Prasetyo {runId}`, Role `Read Only`, cakupan Group `Cabang Timur {runId}`.
  - DU-013-5: Service Center `Detail Lengkap {runId}`, Status `Active`, Service type `Routine, Repair`, Available to `Cabang Timur {runId}, Cabang Barat {runId}`, Specialization `Pendingin Udara {runId}`, Brands `Daikin {runId}`, Country `Malaysia`, Province / State `Johor`, City `Johor Bahru {runId}`, Postal code `81200`, Address line `Jalan Tebrau No. 5`, Company phone `+60 7123456789`, Company email `kontak@detaillengkap.example`, Contact persons `Budi Santoso, +60 7123450001, budi@detaillengkap.example, Primary` dan `Sinta Maharani, +60 7123450002, sinta@detaillengkap.example`, Notes `Vendor lengkap untuk uji Detail`, Attachments satu berkas PDF di bawah 1 MB (nama berkas dibentuk server), dibuat oleh `Rina Wulandari {runId}` dan terakhir diubah oleh `Dewi Anggraini {runId}`.
  - DU-013-6: Service Center `Detail Kosong {runId}`, Status `Active`, Service type `Repair`, Available to `All groups`, Country `Malaysia`, City `Kuala Lumpur {runId}`, Company phone `+60 3123456789`, tanpa Specialization, Brands, Province / State, Postal code, Address line, Company email, Contact persons, Notes, dan Attachments.
  - DU-013-7: Service Center `Kontak Ganda {runId}`, Status `Active`, Service type `Routine`, Available to `All groups`, Country `Malaysia`, City `Ipoh {runId}`, Company phone `+60 3200010000`, Contact persons `Hadi Susanto, +60 3200010001, Primary` dan `Lina Marlina, +60 3200010002`.
  - DU-013-8: Service Center `Detail Aksi {runId}`, Status `Active`, Service type `Routine`, Available to `All groups`, Country `Malaysia`, City `Melaka {runId}`, Company phone `+60 6200020000`.
  - DU-013-9: Service Center `Detail Hapus {runId}`, Status `Active`, Service type `Repair`, Available to `All groups`, Country `Malaysia`, City `Muar {runId}`, Company phone `+60 6200030000`, Usage `0`.
  - DU-013-10: Service Center `Detail Negara {runId}`, Status `Active`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Bandung {runId}`, Company phone `+62 2112345678`.
- Kondisi: Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`; Country perusahaan entitas aktor bernilai `Indonesia`; akun `Rudi Hartono {runId}`, `Maya Puspita {runId}`, `Sari Lestari {runId}`, dan `Tono Prasetyo {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Klik Name membuka Detail dengan tab Overview aktif dan field terisi
1. Ketik Search `Detail Lengkap {runId}`, tekan Enter
2. Verifikasi kolom City pada baris `Detail Lengkap {runId}` bernilai `Johor Bahru {runId}, Malaysia`
3. Klik Name `Detail Lengkap {runId}`
4. Verifikasi halaman Detail `Detail Lengkap {runId}` terbuka
5. Verifikasi tab `Overview` aktif
6. Verifikasi header Detail memuat Name `Detail Lengkap {runId}` dengan badge Status `Active`
7. Verifikasi Overview Service type memuat `Routine` dan `Repair`
8. Verifikasi Overview Available to memuat `Cabang Timur {runId}` dan `Cabang Barat {runId}`
9. Verifikasi Overview Specialization memuat `Pendingin Udara {runId}`
10. Verifikasi Overview Brands memuat `Daikin {runId}`
11. Verifikasi Overview Country bernilai `Malaysia`
12. Verifikasi Overview Province / State bernilai `Johor`
13. Verifikasi Overview City bernilai `Johor Bahru {runId}`
14. Verifikasi Overview Postal code bernilai `81200`
15. Verifikasi Overview Address line bernilai `Jalan Tebrau No. 5`
16. Verifikasi Overview Company phone bernilai `+60 7123456789`
17. Verifikasi Overview Company email bernilai `kontak@detaillengkap.example`
18. Verifikasi Overview Contact persons memuat baris `Budi Santoso`, `+60 7123450001`, dan `budi@detaillengkap.example` bertanda Primary
19. Verifikasi Overview Contact persons memuat baris `Sinta Maharani`, `+60 7123450002`, dan `sinta@detaillengkap.example`
20. Verifikasi Overview Notes bernilai `Vendor lengkap untuk uji Detail`
21. Verifikasi Overview Attachments memuat nama berkas lampiran milik DU-013-5
22. Verifikasi Overview Created by bernilai `Rina W`
23. Verifikasi waktu Created by tampil dengan Date Format `dd/MM/yy` dan Time Format `24h`
24. Verifikasi Overview Last updated by bernilai `Dewi A`
25. Verifikasi waktu Last updated by tampil dengan Date Format `dd/MM/yy` dan Time Format `24h`
26. Catat waktu Last updated by yang tampil pada Overview
27. Klik `⋯` pada header Detail
28. Verifikasi menu memuat `Inactivate`, `Edit`, dan `Delete`
29. Verifikasi menu tidak memuat `Activate`
30. Verifikasi halaman Detail tidak memuat `Download`
31. Tekan Esc
32. Klik breadcrumb `Service Center`
33. Ganti isi kotak search dengan `Detail Lengkap {runId}`, tekan Enter
34. Verifikasi kolom Modified By pada baris `Detail Lengkap {runId}` bernilai `Dewi A`
35. Verifikasi kolom Last Updated pada baris `Detail Lengkap {runId}` sama dengan waktu Last updated by yang dicatat dari Overview
36. Klik angka Usage pada baris `Detail Lengkap {runId}`
37. Verifikasi tab `Usage` aktif
38. Verifikasi tab Usage menampilkan ringkasan teks dengan label `Active schedules`, `Open tasks`, dan `Completed`

### Field opsional yang kosong tampil sebagai nilai kosong
39. Klik breadcrumb `Service Center`
40. Ganti isi kotak search dengan `Detail Kosong {runId}`, tekan Enter
41. Klik Name `Detail Kosong {runId}`
42. Verifikasi Overview Company phone bernilai `+60 3123456789`
43. Verifikasi Overview Contact persons bernilai `—`
44. Verifikasi Overview Specialization bernilai `All categories`
45. Verifikasi Overview Brands bernilai `All brands`
46. Verifikasi Overview Province / State bernilai `—`
47. Verifikasi Overview Postal code bernilai `—`
48. Verifikasi Overview Address line bernilai `—`
49. Verifikasi Overview Company email bernilai `—`
50. Verifikasi Overview Notes bernilai `—`
51. Verifikasi Overview Attachments bernilai `—`
52. Klik breadcrumb `Service Center`
53. Klik `[Changelog]`
54. Ketik Search `Detail Kosong {runId}`, tekan Enter
55. Verifikasi tabel Changelog memuat baris dengan Action `Created`, Field `Name`, dan New Value `Detail Kosong {runId}`
56. Verifikasi tabel Changelog tidak memuat baris dengan Field yang diawali `Contact`
57. Klik ikon close pada modal `Changelog: Service Center`

### Contact person Primary dihapus dan Primary pindah
58. Ganti isi kotak search dengan `Kontak Ganda {runId}`, tekan Enter
59. Klik Name `Kontak Ganda {runId}`
60. Verifikasi Overview Contact persons memuat `Hadi Susanto` bertanda Primary dan `Lina Marlina`
61. Klik `⋯` pada header Detail
62. Klik `Edit`
63. Klik ikon hapus pada baris contact person `Hadi Susanto`
64. Klik `[Save]`
65. Verifikasi Overview Contact persons memuat `Lina Marlina` bertanda Primary
66. Verifikasi Overview Contact persons tidak memuat `Hadi Susanto`
67. Klik breadcrumb `Service Center`
68. Klik `[Changelog]`
69. Ketik Search `Kontak Ganda {runId}`, tekan Enter
70. Verifikasi tabel Changelog memuat baris dengan Action `Updated`, Field yang diawali `Contact`, dan Old Value `Hadi Susanto`
71. Klik ikon close pada modal `Changelog: Service Center`

### Edit, Inactivate, dan Activate dari Detail tetap di Detail
72. Ganti isi kotak search dengan `Detail Aksi {runId}`, tekan Enter
73. Klik Name `Detail Aksi {runId}`
74. Klik `⋯` pada header Detail
75. Klik `Edit`
76. Ganti isi Name dengan `Detail Aksi Baru {runId}`
77. Klik `[Save]`
78. Verifikasi toast `Success, Detail Aksi Baru {runId} has been updated.` tampil
79. Verifikasi header Detail memuat Name `Detail Aksi Baru {runId}`
80. Klik `⋯` pada header Detail
81. Klik `Inactivate`
82. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
83. Verifikasi toast `Success, Detail Aksi Baru {runId} has been inactivated.` tampil
84. Verifikasi header Detail memuat badge Status `Inactive`
85. Klik `⋯` pada header Detail
86. Verifikasi menu memuat `Activate` yang enabled, `Edit`, dan `Delete`
87. Verifikasi menu tidak memuat `Inactivate`
88. Klik `Activate`
89. Klik `[Activate]` pada dialog `Activate Service Center`
90. Verifikasi toast `Success, Detail Aksi Baru {runId} has been activated.` tampil
91. Verifikasi header Detail memuat badge Status `Active`

### Delete dari Detail kembali ke daftar dengan Search dipertahankan
92. Klik breadcrumb `Service Center`
93. Ganti isi kotak search dengan `Detail Hapus {runId}`, tekan Enter
94. Klik Name `Detail Hapus {runId}`
95. Klik `⋯` pada header Detail
96. Klik `Delete`
97. Klik `[Delete]` pada dialog `Delete Service Center`
98. Verifikasi toast `Success, Detail Hapus {runId} has been deleted.` tampil
99. Verifikasi halaman daftar Service Center tampil
100. Verifikasi kotak Search berisi `Detail Hapus {runId}`

### Edit Country ke negara berbeda dari negara company mengubah tampilan City
101. Ganti isi kotak search dengan `Detail Negara {runId}`, tekan Enter
102. Verifikasi kolom City pada baris `Detail Negara {runId}` bernilai `Bandung {runId}`
103. Klik `⋯` pada baris `Detail Negara {runId}`
104. Klik `Edit`
105. Pilih Country `Malaysia`
106. Ganti isi City dengan `Bandung {runId}`
107. Klik `[Save]`
108. Verifikasi kolom City pada baris `Detail Negara {runId}` bernilai `Bandung {runId}, Malaysia`

### Info cakupan tampil hanya bagi Group Manager dan Asset Admin
109. Masuk sebagai `Rudi Hartono {runId}`
110. Ketik Search `Detail Lengkap {runId}`, tekan Enter
111. Klik Name `Detail Lengkap {runId}`
112. Verifikasi Detail memuat info `This service center also serves groups outside your access. Ask an admin who manages all of them.`
113. Masuk sebagai `Maya Puspita {runId}`
114. Ketik Search `Detail Lengkap {runId}`, tekan Enter
115. Klik Name `Detail Lengkap {runId}`
116. Verifikasi Detail memuat info `This service center also serves groups outside your access. Ask an admin who manages all of them.`
117. Masuk sebagai `Sari Lestari {runId}`
118. Ketik Search `Detail Lengkap {runId}`, tekan Enter
119. Klik Name `Detail Lengkap {runId}`
120. Verifikasi header Detail memuat Name `Detail Lengkap {runId}`
121. Verifikasi info `This service center also serves groups outside your access. Ask an admin who manages all of them.` tidak tampil di halaman Detail
122. Masuk sebagai `Tono Prasetyo {runId}`
123. Ketik Search `Detail Lengkap {runId}`, tekan Enter
124. Klik Name `Detail Lengkap {runId}`
125. Verifikasi header Detail memuat Name `Detail Lengkap {runId}`
126. Verifikasi info `This service center also serves groups outside your access. Ask an admin who manages all of them.` tidak tampil di halaman Detail

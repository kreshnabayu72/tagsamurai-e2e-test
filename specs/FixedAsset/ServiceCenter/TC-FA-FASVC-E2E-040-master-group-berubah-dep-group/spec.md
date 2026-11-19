---
id: TC-FA-FASVC-E2E-040-master-group-berubah-dep-group
title: "Group Dihapus, Dipindah, atau Di-Inactivate: Available to Dilepas, Auto Inactive oleh System"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceRules: [MR-FASVC-01, MR-FASVC-02a, MR-FASVC-02b, MR-FASVC-02c, MR-FASVC-02e, MR-FASVC-07a, MR-FASVC-07b, MR-FASVC-07c, MR-FASVC-07e, EC-FASVC-12, EC-FASVC-13, EC-FASVC-56, EC-FASVC-39a, EC-FASVC-39c, F-FASVC-08.k1, F-FASVC-08.k2, F-FASVC-08.k3, FASVC-LOGIC-05h, "§8#r15", "§8#r16", "§9.2#p5", "§9.2#p7", "§9.2#p8", RA-FASVC-08, S-FASVC-12, "§9.7#r4", MR-FASVC-08a, MR-FASVC-08b, MR-FASVC-08c, EC-FASVC-57a, EC-FASVC-57b, EC-FASVC-57c, F-FASVC-08.k8, "§9.4.3#b4", T-FASVC-01]
smoke: []
dependsOn: ["Group: pohon Group dan master Group"]
trace:
  MR-FASVC-01: [24, 25, 113, 117]
  MR-FASVC-02a: [8, 12, 51]
  MR-FASVC-02b: 50
  MR-FASVC-02c: [54, 56]
  MR-FASVC-02e: [71, 104, 107]
  MR-FASVC-07a: 36
  MR-FASVC-07b: [37, 38]
  MR-FASVC-07c: [41, 42]
  MR-FASVC-07e: [64, 95, 98]
  EC-FASVC-12: [8, 9, 13, 50]
  EC-FASVC-13: [24, 25, 113, 117]
  EC-FASVC-56: [36, 37]
  EC-FASVC-39a: [54, 56]
  EC-FASVC-39c: [64, 71]
  F-FASVC-08.k1: [8, 12]
  F-FASVC-08.k2: [37, 50]
  F-FASVC-08.k3: 28
  FASVC-LOGIC-05h: [64, 66, 71, 73, 98, 107]
  "§8#r15": [12, 41, 54]
  "§8#r16": [42, 56]
  "§9.2#p5": [50, 60, 61, 79, 84, 125, 126, 128, 129, 134, 141, 143, 144, 150, 155, 162, 167, 174, 179, 187]
  "§9.2#p7": [51, 54, 55]
  "§9.2#p8": 92
  RA-FASVC-08: [62, 64, 69, 71]
  S-FASVC-12: [62, 64, 69, 71]
  "§9.7#r4": [8, 24]
  MR-FASVC-08a: 215
  MR-FASVC-08b: 211
  MR-FASVC-08c: [203, 204, 206]
  EC-FASVC-57a: 211
  EC-FASVC-57b: [203, 204, 206]
  EC-FASVC-57c: 214
  F-FASVC-08.k8: [214, 215]
  "§9.4.3#b4": 211
  T-FASVC-01: [229, 231]
anchor: [2, 3, 7, 16, 31, 32, 45, 46, 77, 82, 91, 111, 121, 139, 148, 153, 160, 165, 172, 177, 184, 189, 194, 197, 221, 225, 226, 227]
coverage:
  web: automated
---

# Group Dihapus, Dipindah, atau Di-Inactivate: Available to Dilepas, Auto Inactive oleh System

## Prerequisites
- Aktor: Total Control `Rina Wulandari {runId}` (cakupan seluruh Group) menguji layarnya. Admin Group `Dimas Pratama {runId}` (Total Control, cakupan seluruh Group) memicu perubahan di master Group dari sesinya sendiri. Group Manager `Hendra Malang {runId}` (cakupan Group `Cabang Malang {runId}`) dipakai untuk membandingkan apa yang terlihat. Group Manager `Bagas Prasetyo {runId}` (cakupan Group `Region Jawa Timur {runId}`) dan Group Manager `Yuni Astuti {runId}` (cakupan Group `Region Jawa Tengah {runId}`) dipakai untuk membandingkan cakupan sesudah Group dipindah. Asset Admin `Sari Lestari {runId}`, Monitoring & Report `Budi Santoso {runId}`, dan Read Only `Maya Putri {runId}` (masing-masing cakupan seluruh Group) dipakai untuk membandingkan apa yang terlihat. Seluruh akun aktif dan kredensialnya disediakan fase 2.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-040-1: Group `Region Jawa Timur {runId}`, parent root pohon Group, ada di entitas aktor.
  - DU-040-2: Group `Cabang Surabaya {runId}`, parent `Region Jawa Timur {runId}`.
  - DU-040-3: Group `Cabang Malang {runId}`, parent `Region Jawa Timur {runId}`.
  - DU-040-4: Group `Cabang Madiun {runId}`, parent `Region Jawa Timur {runId}`.
  - DU-040-5: Group `Unit Gresik {runId}`, parent `Region Jawa Timur {runId}`.
  - DU-040-6: Group `Region Jawa Tengah {runId}`, parent root pohon Group.
  - DU-040-7: Group `Region Sumatera {runId}`, parent root pohon Group.
  - DU-040-8: Group `Cabang Medan {runId}`, parent `Region Sumatera {runId}`.
  - DU-040-9: Group `Cabang Palembang {runId}`, parent `Region Sumatera {runId}`.
  - DU-040-10: Group `Gudang Pusat {runId}`, parent root pohon Group.
  - DU-040-11: Service Center `Bengkel Mitra Surabaya {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Malang {runId}` dan `Cabang Surabaya {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Surabaya`, Company phone Dial Code `+62` nomor `81234500401`, Company email `surabaya@mitrasurabaya.example`, Usage `0`, Status `Active`.
  - DU-040-12: Service Center `Bengkel Mitra Gresik {runId}`, Service type `Routine` dan `Repair`, Available to `Unit Gresik {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Gresik`, Company phone Dial Code `+62` nomor `81234500402`, Company email `gresik@mitragresik.example`, Usage `0`, Status `Active`.
  - DU-040-13: Service Center `Bengkel Mitra Madiun {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Madiun {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Madiun`, Company phone Dial Code `+62` nomor `81234500403`, Company email `madiun@mitramadiun.example`, Usage `0`, Status `Active`.
  - DU-040-14: Service Center `Bengkel Mitra Sumatera {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Medan {runId}` dan `Cabang Palembang {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Medan`, Company phone Dial Code `+62` nomor `81234500404`, Company email `medan@mitrasumatera.example`, Usage `0`, Status `Active`.
  - DU-040-15: User Total Control `Rina Wulandari {runId}`, cakupan seluruh Group.
  - DU-040-16: User Admin Group `Dimas Pratama {runId}`, role Total Control, cakupan seluruh Group.
  - DU-040-17: User Group Manager `Hendra Malang {runId}`, cakupan Group `Cabang Malang {runId}`.
  - DU-040-18: User Group Manager `Bagas Prasetyo {runId}`, cakupan Group `Region Jawa Timur {runId}`.
  - DU-040-19: User Group Manager `Yuni Astuti {runId}`, cakupan Group `Region Jawa Tengah {runId}`.
  - DU-040-20: Group `Cabang Kediri {runId}`, parent `Region Jawa Timur {runId}`.
  - DU-040-21: Service Center `Bengkel Mitra Kediri {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Kediri {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Kediri`, Company phone Dial Code `+62` nomor `81234500405`, Company email `kediri@mitrakediri.example`, Usage `0`, Status `Active`.
  - DU-040-22: User Asset Admin `Sari Lestari {runId}`, memegang Role Transaksi Maintenance Routine, cakupan seluruh Group.
  - DU-040-23: User Monitoring & Report `Budi Santoso {runId}`, memegang Role Transaksi Maintenance Routine, cakupan seluruh Group.
  - DU-040-24: User Read Only `Maya Putri {runId}`, cakupan seluruh Group.
  - DU-040-25: Group `Cabang Bandung {runId}`, parent root pohon Group, belum berisi aset maupun user. Nama Group ini kemudian diubah menjadi `Bandung Kota {runId}`.
  - DU-040-26: Group `Cabang Cirebon {runId}`, parent root pohon Group.
  - DU-040-27: Service Center `Bengkel Mitra Bandung {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Bandung {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Bandung`, Company phone Dial Code `+62` nomor `81234500406`, Company email `bandung@mitrabandung.example`, Usage `0`, Status `Active`.
  - DU-040-28: Group `Cabang Blitar {runId}`, parent root pohon Group, belum berisi aset maupun user.
  - DU-040-29: Service Center `Bengkel Mitra Blitar {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Blitar {runId}`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Blitar`, Company phone Dial Code `+62` nomor `81234500407`, Company email `blitar@mitrablitar.example`, Usage `0`, Status `Active`.
  - Group pada DU-040-1 sampai DU-040-10, DU-040-20, DU-040-25, DU-040-26, dan DU-040-28 belum berisi aset maupun user.
  - Pada awal spec `Unit Gresik {runId}` (DU-040-5) berada di bawah `Region Jawa Timur {runId}`, dan `Cabang Malang {runId}` yang menjadi Available to `Bengkel Mitra Surabaya {runId}` berada di bawah `Region Jawa Timur {runId}`.

## Test Steps

### Group dihapus: node dilepas selama masih ada node tersisa
1. Ketik Search `Bengkel Mitra Surabaya {runId}`, tekan Enter
2. Verifikasi baris `Bengkel Mitra Surabaya {runId}` tampil dengan Available To `Cabang Malang {runId}` dan `Cabang Surabaya {runId}`
3. Verifikasi Status baris `Bengkel Mitra Surabaya {runId}` adalah `Active`
4. Admin Group menghapus Group `Cabang Surabaya {runId}` dari master Group
5. Muat ulang halaman
6. Ganti isi kotak Search dengan `Bengkel Mitra Surabaya {runId}`, tekan Enter
7. Verifikasi Available To baris `Bengkel Mitra Surabaya {runId}` memuat `Cabang Malang {runId}`
8. Verifikasi Available To baris `Bengkel Mitra Surabaya {runId}` tidak memuat `Cabang Surabaya {runId}`
9. Verifikasi Status baris `Bengkel Mitra Surabaya {runId}` tetap `Active`
10. Klik `Changelog` pada toolbar
11. Ketik Search `Bengkel Mitra Surabaya {runId}` pada modal `Changelog: Service Center`, tekan Enter
12. Verifikasi entri dengan Action `Updated`, Field `Available to`, Old Value `Cabang Malang {runId}, Cabang Surabaya {runId}`, New Value `Cabang Malang {runId}`, dan Modified By `System` tampil
13. Verifikasi tidak ada entri dengan Action `Inactivated` untuk `Bengkel Mitra Surabaya {runId}`
14. Tutup modal `Changelog: Service Center` lewat icon close

### Group dipindah ke parent lain: rujukan tetap dan tidak ada perubahan data
15. Ganti isi kotak Search dengan `Bengkel Mitra Gresik {runId}`, tekan Enter
16. Verifikasi baris `Bengkel Mitra Gresik {runId}` tampil dengan Available To `Unit Gresik {runId}`
17. Klik `Changelog` pada toolbar
18. Ketik Search `Bengkel Mitra Gresik {runId}` pada modal `Changelog: Service Center`, tekan Enter
19. Catat jumlah baris yang tampil di modal sebagai jumlah awal
20. Tutup modal `Changelog: Service Center` lewat icon close
21. Admin Group memindahkan Group `Unit Gresik {runId}` dari parent `Region Jawa Timur {runId}` ke parent `Region Jawa Tengah {runId}`
22. Muat ulang halaman
23. Ganti isi kotak Search dengan `Bengkel Mitra Gresik {runId}`, tekan Enter
24. Verifikasi Available To baris `Bengkel Mitra Gresik {runId}` tetap memuat `Unit Gresik {runId}`
25. Verifikasi Status baris `Bengkel Mitra Gresik {runId}` tetap `Active`
26. Klik `Changelog` pada toolbar
27. Ketik Search `Bengkel Mitra Gresik {runId}` pada modal `Changelog: Service Center`, tekan Enter
28. Verifikasi jumlah baris untuk `Bengkel Mitra Gresik {runId}` di modal sama dengan jumlah awal
29. Tutup modal `Changelog: Service Center` lewat icon close

### Group di-Inactivate: diperlakukan seperti dihapus dan Service Center otomatis Inactive
30. Ganti isi kotak Search dengan `Bengkel Mitra Madiun {runId}`, tekan Enter
31. Verifikasi baris `Bengkel Mitra Madiun {runId}` tampil dengan Available To `Cabang Madiun {runId}`
32. Verifikasi Status baris `Bengkel Mitra Madiun {runId}` adalah `Active`
33. Admin Group meng-inactivate Group `Cabang Madiun {runId}` di master Group
34. Muat ulang halaman
35. Ganti isi kotak Search dengan `Bengkel Mitra Madiun {runId}`, tekan Enter
36. Verifikasi Available To baris `Bengkel Mitra Madiun {runId}` tampil `—`
37. Verifikasi Status baris `Bengkel Mitra Madiun {runId}` menjadi `Inactive`
38. Verifikasi Modified By baris `Bengkel Mitra Madiun {runId}` adalah `System`
39. Klik `Changelog` pada toolbar
40. Ketik Search `Bengkel Mitra Madiun {runId}` pada modal `Changelog: Service Center`, tekan Enter
41. Verifikasi entri dengan Action `Updated`, Field `Available to`, Old Value `Cabang Madiun {runId}`, New Value `—`, dan Modified By `System` tampil
42. Verifikasi entri dengan Action `Inactivated`, Field `Status`, Old Value `Active`, New Value `Inactive`, dan Modified By `System` tampil
43. Tutup modal `Changelog: Service Center` lewat icon close

### Group induk dihapus beserta subtree: seluruh node dilepas dalam satu event dan Service Center otomatis Inactive
44. Ganti isi kotak Search dengan `Bengkel Mitra Sumatera {runId}`, tekan Enter
45. Verifikasi Available To baris `Bengkel Mitra Sumatera {runId}` memuat `Cabang Medan {runId}` dan `Cabang Palembang {runId}`
46. Verifikasi Status baris `Bengkel Mitra Sumatera {runId}` adalah `Active`
47. Admin Group menghapus Group `Region Sumatera {runId}` beserta subtree-nya (`Cabang Medan {runId}` dan `Cabang Palembang {runId}`) dari master Group
48. Muat ulang halaman
49. Ganti isi kotak Search dengan `Bengkel Mitra Sumatera {runId}`, tekan Enter
50. Verifikasi Status baris `Bengkel Mitra Sumatera {runId}` menjadi `Inactive` dan baris tetap tampil bagi Total Control
51. Verifikasi Available To baris `Bengkel Mitra Sumatera {runId}` tampil `—`
52. Klik `Changelog` pada toolbar
53. Ketik Search `Bengkel Mitra Sumatera {runId}` pada modal `Changelog: Service Center`, tekan Enter
54. Verifikasi entri dengan Action `Updated`, Field `Available to`, Old Value `Cabang Medan {runId}, Cabang Palembang {runId}`, New Value `—`, dan Modified By `System` tampil
55. Verifikasi hanya ada satu entri dengan Action `Updated` dan Field `Available to` untuk `Bengkel Mitra Sumatera {runId}`
56. Verifikasi entri dengan Action `Inactivated`, Field `Status`, Old Value `Active`, New Value `Inactive`, dan Modified By `System` tampil
57. Tutup modal `Changelog: Service Center` lewat icon close

### Activate pada Service Center otomatis Inactive karena Group di-Inactivate ditolak selama Available to kosong
58. Ganti isi kotak Search dengan `Bengkel Mitra Madiun {runId}`, tekan Enter
59. Klik `⋯` pada baris `Bengkel Mitra Madiun {runId}`
60. Verifikasi menu `⋯` memuat `Edit`, `Activate`, dan `Delete` bagi Total Control
61. Verifikasi aksi `Delete` tidak disabled karena Usage `0`
62. Verifikasi aksi `Activate` tidak disabled
63. Klik `Activate`
64. Verifikasi dialog blok memuat pesan `Add at least one group before activating.`
65. Klik `[OK]` pada dialog blok
66. Verifikasi Status baris `Bengkel Mitra Madiun {runId}` tetap `Inactive`

### Activate pada Service Center otomatis Inactive karena Group induk dihapus ditolak selama Available to kosong
67. Ganti isi kotak Search dengan `Bengkel Mitra Sumatera {runId}`, tekan Enter
68. Klik `⋯` pada baris `Bengkel Mitra Sumatera {runId}`
69. Verifikasi aksi `Activate` tidak disabled
70. Klik `Activate`
71. Verifikasi dialog blok memuat pesan `Add at least one group before activating.`
72. Klik `[OK]` pada dialog blok
73. Verifikasi Status baris `Bengkel Mitra Sumatera {runId}` tetap `Inactive`

### Hanya Total Control yang melihat Service Center ber-Available to kosong
74. Ganti akun ke Group Manager `Hendra Malang {runId}`
75. Buka Add-ons > Service Center lewat sidebar
76. Ganti isi kotak Search dengan `Bengkel Mitra Surabaya {runId}`, tekan Enter
77. Verifikasi baris `Bengkel Mitra Surabaya {runId}` tampil
78. Ganti isi kotak Search dengan `Bengkel Mitra Madiun {runId}`, tekan Enter
79. Verifikasi pesan `No results found` tampil karena `Bengkel Mitra Madiun {runId}` ber-Available to kosong
80. Klik `Changelog` pada toolbar
81. Ketik Search `Bengkel Mitra Surabaya {runId}` pada modal `Changelog: Service Center`, tekan Enter
82. Verifikasi entri dengan Action `Updated` dan Field `Available to` untuk `Bengkel Mitra Surabaya {runId}` tampil
83. Ganti isi kotak Search dengan `Bengkel Mitra Madiun {runId}`, tekan Enter
84. Verifikasi pesan `No results found` tampil di modal karena `Bengkel Mitra Madiun {runId}` ber-Available to kosong
85. Tutup modal `Changelog: Service Center` lewat icon close
86. Ganti akun kembali ke Total Control `Rina Wulandari {runId}`

### Available to diisi lewat Edit, lalu Activate berhasil (Group di-Inactivate)
87. Buka Add-ons > Service Center lewat sidebar
88. Ketik Search `Bengkel Mitra Madiun {runId}`, tekan Enter
89. Klik `⋯` pada baris `Bengkel Mitra Madiun {runId}`, lalu klik `Edit`
90. Klik field Available to untuk membuka tree Group
91. Verifikasi tree Available to menampilkan `Gudang Pusat {runId}`
92. Verifikasi tree Available to tidak menampilkan `Cabang Madiun {runId}`
93. Centang `Gudang Pusat {runId}` pada tree Available to
94. Klik `[Save]`
95. Verifikasi Available To baris `Bengkel Mitra Madiun {runId}` memuat `Gudang Pusat {runId}`
96. Klik `⋯` pada baris `Bengkel Mitra Madiun {runId}`, lalu klik `Activate`
97. Klik `[Activate]` pada dialog `Activate Service Center`
98. Verifikasi Status baris `Bengkel Mitra Madiun {runId}` menjadi `Active`

### Available to diisi lewat Edit, lalu Activate berhasil (Group induk dihapus)
99. Ganti isi kotak Search dengan `Bengkel Mitra Sumatera {runId}`, tekan Enter
100. Klik `⋯` pada baris `Bengkel Mitra Sumatera {runId}`, lalu klik `Edit`
101. Klik field Available to untuk membuka tree Group
102. Centang `Gudang Pusat {runId}` pada tree Available to
103. Klik `[Save]`
104. Verifikasi Available To baris `Bengkel Mitra Sumatera {runId}` memuat `Gudang Pusat {runId}`
105. Klik `⋯` pada baris `Bengkel Mitra Sumatera {runId}`, lalu klik `Activate`
106. Klik `[Activate]` pada dialog `Activate Service Center`
107. Verifikasi Status baris `Bengkel Mitra Sumatera {runId}` menjadi `Active`

### Group dipindah ke parent lain: cakupan Group Manager dievaluasi menurut posisi baru
108. Ganti akun ke Group Manager `Bagas Prasetyo {runId}`
109. Buka Add-ons > Service Center lewat sidebar
110. Ketik Search `Bengkel Mitra Surabaya {runId}`, tekan Enter
111. Verifikasi baris `Bengkel Mitra Surabaya {runId}` tampil
112. Ganti isi kotak Search dengan `Bengkel Mitra Gresik {runId}`, tekan Enter
113. Verifikasi pesan `No results found` tampil karena `Unit Gresik {runId}` sudah berpindah dari `Region Jawa Timur {runId}`
114. Ganti akun ke Group Manager `Yuni Astuti {runId}`
115. Buka Add-ons > Service Center lewat sidebar
116. Ketik Search `Bengkel Mitra Gresik {runId}`, tekan Enter
117. Verifikasi baris `Bengkel Mitra Gresik {runId}` tampil dengan Available To `Unit Gresik {runId}`
118. Ganti akun kembali ke Total Control `Rina Wulandari {runId}`

### Total Control melihat Service Center ber-Available to kosong di daftar, Detail, dan Changelog gabungan
119. Buka Add-ons > Service Center lewat sidebar
120. Ketik Search `Bengkel Mitra Kediri {runId}`, tekan Enter
121. Verifikasi baris `Bengkel Mitra Kediri {runId}` tampil dengan Available To `Cabang Kediri {runId}`
122. Admin Group meng-inactivate Group `Cabang Kediri {runId}` di master Group
123. Muat ulang halaman
124. Ganti isi kotak Search dengan `Bengkel Mitra Kediri {runId}`, tekan Enter
125. Verifikasi baris `Bengkel Mitra Kediri {runId}` tetap tampil bagi Total Control dengan Available To `—`
126. Verifikasi Status baris `Bengkel Mitra Kediri {runId}` menjadi `Inactive`
127. Klik Name `Bengkel Mitra Kediri {runId}`
128. Verifikasi judul halaman Detail adalah `Bengkel Mitra Kediri {runId}`
129. Verifikasi badge Status pada header Detail adalah `Inactive`
130. Catat URL halaman Detail `Bengkel Mitra Kediri {runId}`
131. Buka Add-ons > Service Center lewat sidebar
132. Klik `Changelog` pada toolbar
133. Ketik Search `Bengkel Mitra Kediri {runId}` pada modal `Changelog: Service Center`, tekan Enter
134. Verifikasi entri dengan Action `Updated`, Field `Available to`, Old Value `Cabang Kediri {runId}`, New Value `—`, dan Modified By `System` tampil
135. Tutup modal `Changelog: Service Center` lewat icon close

### Group Manager tidak melihat Service Center ber-Available to kosong di daftar dan Detail
136. Ganti akun ke Group Manager `Hendra Malang {runId}`
137. Buka Add-ons > Service Center lewat sidebar
138. Ketik Search `Bengkel Mitra Surabaya {runId}`, tekan Enter
139. Verifikasi baris `Bengkel Mitra Surabaya {runId}` tampil
140. Ganti isi kotak Search dengan `Bengkel Mitra Kediri {runId}`, tekan Enter
141. Verifikasi pesan `No results found` tampil karena `Bengkel Mitra Kediri {runId}` ber-Available to kosong
142. Buka URL halaman Detail yang dicatat pada langkah 130
143. Verifikasi halaman menampilkan judul `Page Not Found`
144. Verifikasi halaman menampilkan teks `The page you're looking for doesn't exist or may have been moved.`

### Asset Admin tidak melihat Service Center ber-Available to kosong di daftar dan Changelog gabungan
145. Ganti akun ke Asset Admin `Sari Lestari {runId}`
146. Buka Add-ons > Service Center lewat sidebar
147. Ketik Search `Bengkel Mitra Surabaya {runId}`, tekan Enter
148. Verifikasi baris `Bengkel Mitra Surabaya {runId}` tampil
149. Ganti isi kotak Search dengan `Bengkel Mitra Kediri {runId}`, tekan Enter
150. Verifikasi pesan `No results found` tampil karena `Bengkel Mitra Kediri {runId}` ber-Available to kosong
151. Klik `Changelog` pada toolbar
152. Ketik Search `Bengkel Mitra Surabaya {runId}` pada modal `Changelog: Service Center`, tekan Enter
153. Verifikasi entri dengan Action `Updated` dan Field `Available to` untuk `Bengkel Mitra Surabaya {runId}` tampil
154. Ganti isi kotak Search dengan `Bengkel Mitra Kediri {runId}`, tekan Enter
155. Verifikasi pesan `No results found` tampil di modal karena `Bengkel Mitra Kediri {runId}` ber-Available to kosong
156. Tutup modal `Changelog: Service Center` lewat icon close

### Monitoring & Report tidak melihat Service Center ber-Available to kosong di daftar dan Changelog gabungan
157. Ganti akun ke Monitoring & Report `Budi Santoso {runId}`
158. Buka Add-ons > Service Center lewat sidebar
159. Ketik Search `Bengkel Mitra Surabaya {runId}`, tekan Enter
160. Verifikasi baris `Bengkel Mitra Surabaya {runId}` tampil
161. Ganti isi kotak Search dengan `Bengkel Mitra Kediri {runId}`, tekan Enter
162. Verifikasi pesan `No results found` tampil karena `Bengkel Mitra Kediri {runId}` ber-Available to kosong
163. Klik `Changelog` pada toolbar
164. Ketik Search `Bengkel Mitra Surabaya {runId}` pada modal `Changelog: Service Center`, tekan Enter
165. Verifikasi entri dengan Action `Updated` dan Field `Available to` untuk `Bengkel Mitra Surabaya {runId}` tampil
166. Ganti isi kotak Search dengan `Bengkel Mitra Kediri {runId}`, tekan Enter
167. Verifikasi pesan `No results found` tampil di modal karena `Bengkel Mitra Kediri {runId}` ber-Available to kosong
168. Tutup modal `Changelog: Service Center` lewat icon close

### Read Only tidak melihat Service Center ber-Available to kosong di daftar dan Changelog gabungan
169. Ganti akun ke Read Only `Maya Putri {runId}`
170. Buka Add-ons > Service Center lewat sidebar
171. Ketik Search `Bengkel Mitra Surabaya {runId}`, tekan Enter
172. Verifikasi baris `Bengkel Mitra Surabaya {runId}` tampil
173. Ganti isi kotak Search dengan `Bengkel Mitra Kediri {runId}`, tekan Enter
174. Verifikasi pesan `No results found` tampil karena `Bengkel Mitra Kediri {runId}` ber-Available to kosong
175. Klik `Changelog` pada toolbar
176. Ketik Search `Bengkel Mitra Surabaya {runId}` pada modal `Changelog: Service Center`, tekan Enter
177. Verifikasi entri dengan Action `Updated` dan Field `Available to` untuk `Bengkel Mitra Surabaya {runId}` tampil
178. Ganti isi kotak Search dengan `Bengkel Mitra Kediri {runId}`, tekan Enter
179. Verifikasi pesan `No results found` tampil di modal karena `Bengkel Mitra Kediri {runId}` ber-Available to kosong
180. Tutup modal `Changelog: Service Center` lewat icon close

### Total Control menghapus Service Center ber-Available to kosong dengan Usage 0
181. Ganti akun kembali ke Total Control `Rina Wulandari {runId}`
182. Buka Add-ons > Service Center lewat sidebar
183. Ketik Search `Bengkel Mitra Kediri {runId}`, tekan Enter
184. Verifikasi baris `Bengkel Mitra Kediri {runId}` tampil dengan Status `Inactive`
185. Klik `⋯` pada baris `Bengkel Mitra Kediri {runId}`, lalu klik `Delete`
186. Klik `[Delete]` pada dialog `Delete Service Center`
187. Verifikasi pesan `No results found` tampil karena `Bengkel Mitra Kediri {runId}` sudah dihapus

### Group di-rename: nama terkini tampil di tabel dan form, pencocokan memakai ID, Changelog lama tetap nama snapshot
188. Ganti isi kotak Search dengan `Bengkel Mitra Bandung {runId}`, tekan Enter
189. Verifikasi baris `Bengkel Mitra Bandung {runId}` tampil dengan Available To `Cabang Bandung {runId}`
190. Klik `⋯` pada baris `Bengkel Mitra Bandung {runId}`, lalu klik `Edit`
191. Klik field Available to untuk membuka tree Group
192. Centang `Cabang Cirebon {runId}` pada tree Available to
193. Klik `[Save]`
194. Verifikasi Available To baris `Bengkel Mitra Bandung {runId}` memuat `Cabang Bandung {runId}` dan `Cabang Cirebon {runId}`
195. Klik `Changelog` pada toolbar
196. Ketik Search `Bengkel Mitra Bandung {runId}` pada modal `Changelog: Service Center`, tekan Enter
197. Verifikasi entri dengan Action `Updated`, Field `Available to`, Old Value `Cabang Bandung {runId}`, dan New Value `Cabang Bandung {runId}, Cabang Cirebon {runId}` tampil
198. Catat jumlah baris yang tampil di modal sebagai jumlah awal
199. Tutup modal `Changelog: Service Center` lewat icon close
200. Admin Group mengubah nama Group `Cabang Bandung {runId}` menjadi `Bandung Kota {runId}` di master Group
201. Muat ulang halaman
202. Ganti isi kotak Search dengan `Bengkel Mitra Bandung {runId}`, tekan Enter
203. Verifikasi Available To baris `Bengkel Mitra Bandung {runId}` memuat `Bandung Kota {runId}` dan `Cabang Cirebon {runId}`
204. Verifikasi Available To baris `Bengkel Mitra Bandung {runId}` tidak memuat `Cabang Bandung {runId}`
205. Klik `⋯` pada baris `Bengkel Mitra Bandung {runId}`, lalu klik `Edit`
206. Verifikasi field Available to di dialog `Edit Service Center` memuat `Bandung Kota {runId}`
207. Klik `✕` pada form yang belum diubah
208. Klik `Filter` pada toolbar
209. Centang `Bandung Kota {runId}` pada field Available To di Filter Panel
210. Klik `[Apply]`
211. Verifikasi baris `Bengkel Mitra Bandung {runId}` tampil karena Group `Bandung Kota {runId}` dicocokkan lewat ID
212. Klik `Changelog` pada toolbar
213. Ketik Search `Bengkel Mitra Bandung {runId}` pada modal `Changelog: Service Center`, tekan Enter
214. Verifikasi entri dengan Action `Updated`, Field `Available to`, dan New Value `Cabang Bandung {runId}, Cabang Cirebon {runId}` tetap tampil dengan nama lama
215. Verifikasi jumlah baris untuk `Bengkel Mitra Bandung {runId}` di modal sama dengan jumlah awal
216. Tutup modal `Changelog: Service Center` lewat icon close

### Sort kolom chip Available To: baris ber-Available to kosong (`—`) di akhir saat ascending dan di awal saat descending
217. Klik `Filter` pada toolbar
218. Klik `[Clear Field]`
219. Klik `[Apply]`
220. Ganti isi kotak Search dengan `Bengkel Mitra Blitar {runId}`, tekan Enter
221. Verifikasi baris `Bengkel Mitra Blitar {runId}` tampil dengan Available To `Cabang Blitar {runId}`
222. Admin Group menghapus Group `Cabang Blitar {runId}` dari master Group
223. Muat ulang halaman
224. Ganti isi kotak Search dengan `{runId}`, tekan Enter
225. Verifikasi baris `Bengkel Mitra Blitar {runId}` tampil dengan Available To `—`
226. Verifikasi baris `Bengkel Mitra Bandung {runId}` tampil dengan Available To `Bandung Kota {runId}` dan `Cabang Cirebon {runId}`
227. Verifikasi baris `Bengkel Mitra Surabaya {runId}` tampil dengan Available To `Cabang Malang {runId}`
228. Klik header kolom `Available To`
229. Verifikasi baris `Bengkel Mitra Blitar {runId}` berada di akhir daftar, sesudah baris `Bengkel Mitra Bandung {runId}` dan `Bengkel Mitra Surabaya {runId}`
230. Klik header kolom `Available To`
231. Verifikasi baris `Bengkel Mitra Blitar {runId}` berada di awal daftar, sebelum baris `Bengkel Mitra Bandung {runId}` dan `Bengkel Mitra Surabaya {runId}`

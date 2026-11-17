---
id: TC-FA-DAMAGED-E2E-004-tabel-active-filter
title: "Filter Panel sub-tab Active menyaring per field dengan opsi DISTINCT dari data, OR di dalam Status termasuk penanda, dan irisan dengan Search"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, "§9.5#r7", "§9.2#b4", EB-FLT-1@tabel-active, EB-FLT-4@tabel-active, EB-FLT-5@tabel-active, EB-FLT-3]
smoke: [EB-FLT-3]
dependsOn: []
trace:
  T-DMG-01: [3, 12, 13, 16, 20, 21, 24, 25, 38, 43, 44, 47, 50, 55, 59, 63, 67, 115, 122, 125]
  "§9.5#r7": [6, 7, 29, 33]
  "§9.2#b4": [9]
  EB-FLT-1@tabel-active: [6, 7, 9, 89, 91, 93, 95, 97, 118, 127]
  EB-FLT-4@tabel-active: [73, 76, 80, 82, 84, 135, 138, 139, 142, 145, 146, 151, 153, 154]
  EB-FLT-5@tabel-active: [102, 108, 111, 133, 131, 132]
  EB-FLT-3: [12, 13, 16, 20, 21, 24, 25]
anchor: [99]
coverage:
  web: automated
---

# Filter Panel sub-tab Active menyaring per field dengan opsi DISTINCT dari data, OR di dalam Status termasuk penanda, dan irisan dengan Search

## Prerequisites
- Aktor: Total Control, user `Admin T`; aktor kedua Total Control `Bima A` (DU-004-13) hanya menjalankan aksi pemicu.
- Layar awal: halaman Assets.
- Data:
  - DU-004-1: Name `Filter Aset {runId} - 1`, Asset ID `FLT-0001-{runId}`, Group `Head Office {runId}`, Status `Damaged`, Source `Manual`, Last Holder `Sari D`, Reported By `Agus P`, Reported Date `T0 − 3 hari, pukul 11:00`, Days Damaged `3 days`.
  - DU-004-2: Name `Filter Aset {runId} - 2`, Asset ID `FLT-0002-{runId}`, Group `Branch Surabaya {runId}`, Status `Damaged`, Source `Reported by scan`, Last Holder `—`, Reported By `Dedi K`, Reported Date `T0 − 6 hari, pukul 11:00`, Days Damaged `6 days`.
  - DU-004-3: Name `Filter Aset {runId} - 3`, Asset ID `FLT-0003-{runId}`, Group `Head Office {runId}`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `—`, Reported By `Budi S`, Reported Date `T0 − 10 hari, pukul 11:00`, Days Damaged `10 days`.
  - DU-004-4: Name `Filter Aset {runId} - 4`, Asset ID `FLT-0004-{runId}`, Group `Branch Surabaya {runId}`, Status `Reported Disposal`, Source `Stock opname`, Last Holder `—`, Reported By `Agus P`, Reported Date `T0 − 14 hari, pukul 11:00`, Days Damaged `14 days`.
  - DU-004-5: Name `Filter Aset {runId} - 5`, Asset ID `FLT-0005-{runId}`, Group `Head Office {runId}`, Status `In Disposal Process`, Source `Manual`, Last Holder `—`, Reported By `Rina W`, Reported Date `T0 − 20 hari, pukul 11:00`, Days Damaged `20 days`.
  - DU-004-6: Name `Filter Aset {runId} - 6`, Asset ID `FLT-0006-{runId}`, Group `Warehouse {runId}`, Status `Damaged` berpenanda `Reported Missing`, Source `Manual`, Last Holder `—`, Reported By `Agus P`, Reported Date `T0 − 5 hari, pukul 11:00`, Days Damaged `5 days`.
  - DU-004-7: Name `Filter Aset {runId} - 7`, Asset ID `FLT-0007-{runId}`, Group `Warehouse {runId}`, Status `Damaged` berpenanda `Missing`, Source `Borrow return`, Last Holder `—`, Reported By `Rina W`, Reported Date `T0 − 8 hari, pukul 11:00`, Days Damaged `8 days`.
  - DU-004-8: Name `Filter Aset {runId} - 8`, Asset ID `FLT-0008-{runId}`, Group `Head Office {runId}`, Status `Damaged`, Source `Assign return`, Last Holder `—`, Reported By `Rina W`, Reported Date `T0 − 10 hari, pukul 11:00`, Days Damaged `10 days`.
  - DU-004-9: record `Repaired` (sudah selesai, hanya tampil di sub-tab History), Name `Filter Aset {runId} - 9`, Asset ID `FLT-0009-{runId}`, Group `Head Office {runId}`, Source `Manual`, Reported By `Rina W`.
  - DU-004-10: aset Normal tanpa record berjalan, Name `Filter Aset {runId} - 10`, Asset ID `FLT-0010-{runId}`, Group `Head Office {runId}`.
  - DU-004-11: isian Report Damaged oleh `Bima A` atas DU-004-10: What happened `Layar retak terbentur`, Damaged Photo `foto-layar-retak.jpg`.
  - DU-004-14: rentang Reported Date `T0 − 8 hari` sampai `T0 − 5 hari`; DU-004-15: rentang Reported Date `T0 − 30 hari` sampai `T0 − 25 hari`; DU-004-16: rentang Days Damaged Min `14`, Max `5`; DU-004-17: kata kunci dropdown Source `scan`, `STOCK`, dan `Tidak Ada`.
  - DU-004-18: user master `Gita P` yang tidak pernah melapor record apa pun.
  - DU-004-12: isian Mark as Repaired oleh `Bima A` atas DU-004-8: Repair note `Unit sudah diganti`; aset tanpa TAG.
  - Pengguna `Agus P`, `Dedi K`, `Budi S`, dan `Rina W` adalah user ber-runId; sumber Source `Manual` adalah laporan Pelapor admin.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - After photo required bernilai `OFF`.

## Test Steps

### Opsi filter berasal dari data tabel
1. Buka tab `Damaged` pada halaman Assets
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi tabel memuat baris `Filter Aset {runId} - 1` dan `Filter Aset {runId} - 2` dan `Filter Aset {runId} - 3` dan `Filter Aset {runId} - 4` dan `Filter Aset {runId} - 5` dan `Filter Aset {runId} - 6` dan `Filter Aset {runId} - 7` dan `Filter Aset {runId} - 8`
4. Klik ikon `Filter`
5. Buka dropdown field `Status`
6. Verifikasi opsi `Waiting for Confirmation`, `Damaged`, `Reported Disposal`, `In Disposal Process`, `Reported Missing`, dan `Missing` tampil
7. Verifikasi opsi `Repaired` tidak tampil karena nilainya hanya ada pada record sub-tab History
8. Buka dropdown field `Source`
9. Verifikasi opsi `Manual`, `Reported by scan`, `Reported by holder`, `Stock opname`, `Borrow return`, dan `Assign return` tampil

### AND antar-field dan OR di dalam satu field
10. Pilih opsi `Damaged` pada field `Status`
11. Klik `[Apply]`
12. Verifikasi baris `Filter Aset {runId} - 1` dan `Filter Aset {runId} - 2` dan `Filter Aset {runId} - 6` dan `Filter Aset {runId} - 7` dan `Filter Aset {runId} - 8` tampil, termasuk baris yang membawa penanda `Reported Missing` dan `Missing`
13. Verifikasi baris `Filter Aset {runId} - 3` dan `Filter Aset {runId} - 4` dan `Filter Aset {runId} - 5` tidak tampil
14. Pilih opsi `Reported Disposal` pada field `Status`
15. Klik `[Apply]`
16. Verifikasi baris `Filter Aset {runId} - 4` tampil bersama baris berstatus `Damaged` karena logika OR di dalam field
17. Klik `[Clear Field]`
18. Pilih opsi `Manual` pada field `Source`
19. Klik `[Apply]`
20. Verifikasi baris `Filter Aset {runId} - 1` dan `Filter Aset {runId} - 5` dan `Filter Aset {runId} - 6` tampil
21. Verifikasi baris `Filter Aset {runId} - 2` dan `Filter Aset {runId} - 3` dan `Filter Aset {runId} - 4` dan `Filter Aset {runId} - 7` dan `Filter Aset {runId} - 8` tidak tampil
22. Pilih opsi `Damaged` pada field `Status`
23. Klik `[Apply]`
24. Verifikasi baris `Filter Aset {runId} - 1` dan `Filter Aset {runId} - 6` tampil karena memenuhi Status dan Source sekaligus
25. Verifikasi baris `Filter Aset {runId} - 2` dan `Filter Aset {runId} - 3` dan `Filter Aset {runId} - 4` dan `Filter Aset {runId} - 5` dan `Filter Aset {runId} - 7` dan `Filter Aset {runId} - 8` tidak tampil

### Opsi penanda Missing menyaring record bertanda itu
26. Klik `[Clear Field]`
27. Pilih opsi `Reported Missing` pada field `Status`
28. Klik `[Apply]`
29. Verifikasi baris `Filter Aset {runId} - 6` tampil dan baris `Filter Aset {runId} - 7` tidak tampil
30. Klik `[Clear Field]`
31. Pilih opsi `Missing` pada field `Status`
32. Klik `[Apply]`
33. Verifikasi baris `Filter Aset {runId} - 7` tampil dan baris `Filter Aset {runId} - 6` tidak tampil
34. Klik `[Clear Field]`
35. Klik `[Apply]`

### Filter Group lewat tree picker
36. Pilih Group `Branch Surabaya {runId}` pada field `Group`
37. Klik `[Apply]`
38. Verifikasi baris `Filter Aset {runId} - 2` dan `Filter Aset {runId} - 4` tampil dan baris `Filter Aset {runId} - 1` dan `Filter Aset {runId} - 3` dan `Filter Aset {runId} - 5` tidak tampil
39. Klik `[Clear Field]`
40. Klik `[Apply]`

### Filter Reported Date inklusif di kedua ujung rentang
41. Pilih rentang tanggal Reported Date dari `T0 − 8 hari` sampai `T0 − 5 hari`
42. Klik `[Apply]`
43. Verifikasi baris `Filter Aset {runId} - 7` dan `Filter Aset {runId} - 2` dan `Filter Aset {runId} - 6` tampil, termasuk baris pada tanggal awal dan tanggal akhir rentang
44. Verifikasi baris `Filter Aset {runId} - 1` dan `Filter Aset {runId} - 3` dan `Filter Aset {runId} - 4` dan `Filter Aset {runId} - 5` dan `Filter Aset {runId} - 8` tidak tampil
45. Pilih rentang tanggal Reported Date dari `T0 − 6 hari` sampai `T0 − 6 hari`
46. Klik `[Apply]`
47. Verifikasi baris `Filter Aset {runId} - 2` tampil sebagai satu-satunya baris milik spec ini pada rentang satu hari
48. Pilih rentang tanggal Reported Date dari `T0 − 30 hari` sampai `T0 − 25 hari`
49. Klik `[Apply]`
50. Verifikasi tabel menampilkan `No results found`
51. Klik `[Clear Field]`
52. Klik `[Apply]`

### Filter Days Damaged dengan rentang Min dan Max
53. Isi `Min` pada field `Days Damaged` dengan `14`
54. Klik `[Apply]`
55. Verifikasi baris `Filter Aset {runId} - 4` dan `Filter Aset {runId} - 5` tampil dan baris `Filter Aset {runId} - 1` dan `Filter Aset {runId} - 2` dan `Filter Aset {runId} - 3` dan `Filter Aset {runId} - 6` dan `Filter Aset {runId} - 7` dan `Filter Aset {runId} - 8` tidak tampil
56. Klik `[Clear Field]`
57. Isi `Max` pada field `Days Damaged` dengan `5`
58. Klik `[Apply]`
59. Verifikasi baris `Filter Aset {runId} - 1` dan `Filter Aset {runId} - 6` tampil dan baris `Filter Aset {runId} - 2` dan `Filter Aset {runId} - 3` dan `Filter Aset {runId} - 4` dan `Filter Aset {runId} - 5` dan `Filter Aset {runId} - 7` dan `Filter Aset {runId} - 8` tidak tampil
60. Klik `[Clear Field]`
61. Isi `Min` pada field `Days Damaged` dengan `10`
62. Klik `[Apply]`
63. Verifikasi baris `Filter Aset {runId} - 3` dan `Filter Aset {runId} - 4` dan `Filter Aset {runId} - 5` dan `Filter Aset {runId} - 8` tampil dan baris `Filter Aset {runId} - 1` dan `Filter Aset {runId} - 2` dan `Filter Aset {runId} - 6` dan `Filter Aset {runId} - 7` tidak tampil
64. Klik `[Clear Field]`
65. Isi `Max` pada field `Days Damaged` dengan `6`
66. Klik `[Apply]`
67. Verifikasi baris `Filter Aset {runId} - 1` dan `Filter Aset {runId} - 2` dan `Filter Aset {runId} - 6` tampil dan baris `Filter Aset {runId} - 3` dan `Filter Aset {runId} - 4` dan `Filter Aset {runId} - 5` dan `Filter Aset {runId} - 7` dan `Filter Aset {runId} - 8` tidak tampil
68. Klik `[Clear Field]`
69. Klik `[Apply]`

### Search dan Filter beririsan dan saling melepas
70. Pilih opsi `Damaged` pada field `Status`
71. Klik `[Apply]`
72. Ganti isi kotak search dengan `Filter Aset {runId} - 5`, tekan Enter
73. Verifikasi tabel menampilkan `No results found` karena Search dan Filter masing-masing punya hasil tetapi irisannya kosong
74. Klik `[Clear Field]`
75. Klik `[Apply]`
76. Verifikasi baris `Filter Aset {runId} - 5` tampil kembali dan Search `Filter Aset {runId} - 5` tetap terisi
77. Ganti isi kotak search dengan `{runId}`, tekan Enter
78. Pilih opsi `Damaged` pada field `Status`
79. Klik `[Apply]`
80. Verifikasi hasil Filter dahulu lalu Search adalah baris `Filter Aset {runId} - 1` dan `Filter Aset {runId} - 2` dan `Filter Aset {runId} - 6` dan `Filter Aset {runId} - 7` dan `Filter Aset {runId} - 8`
81. Ganti isi kotak search dengan `Filter Aset {runId} - 1`, tekan Enter
82. Verifikasi baris `Filter Aset {runId} - 1` tampil dan baris `Filter Aset {runId} - 2` dan `Filter Aset {runId} - 6` dan `Filter Aset {runId} - 7` dan `Filter Aset {runId} - 8` tidak tampil
83. Klik `(←)` pada kotak Search
84. Verifikasi Filter `Damaged` tetap berlaku sehingga baris `Filter Aset {runId} - 1` dan `Filter Aset {runId} - 2` dan `Filter Aset {runId} - 6` dan `Filter Aset {runId} - 7` dan `Filter Aset {runId} - 8` tampil dan baris `Filter Aset {runId} - 3` dan `Filter Aset {runId} - 4` dan `Filter Aset {runId} - 5` tidak tampil
85. Klik `[Clear Field]`
86. Klik `[Apply]`

### Opsi dropdown dicari dan tidak dipersempit oleh Search
87. Ganti isi kotak search dengan `Filter Aset {runId} - 1`, tekan Enter
88. Buka dropdown field `Source`
89. Verifikasi opsi `Stock opname` tampil walau baris `Filter Aset {runId} - 4` tidak cocok dengan Search
90. Ketik `scan` pada kotak cari di dalam dropdown `Source`
91. Verifikasi opsi `Reported by scan` tampil dan opsi `Manual` tidak tampil
92. Ketik `STOCK` pada kotak cari di dalam dropdown `Source`
93. Verifikasi opsi `Stock opname` tampil
94. Ketik `Tidak Ada` pada kotak cari di dalam dropdown `Source`
95. Verifikasi dropdown `Source` menampilkan `No results found`
96. Buka dropdown field `Reported By`
97. Verifikasi opsi `Agus P` tampil dan opsi `Gita P` tidak tampil karena user itu tidak pernah melapor record
98. Ganti isi kotak search dengan `{runId}`, tekan Enter
99. Verifikasi baris `Filter Aset {runId} - 2` dan `Filter Aset {runId} - 5` yang Last Holder-nya `—` tampil sebelum opsi Last Holder dipilih
100. Pilih opsi `Sari D` pada field `Last Holder`
101. Klik `[Apply]`
102. Verifikasi baris `Filter Aset {runId} - 1` tampil dan baris `Filter Aset {runId} - 2` dan `Filter Aset {runId} - 5` yang Last Holder-nya `—` tidak tampil karena nilai kosong tersaring keluar
103. Klik `[Clear Field]`
104. Klik `[Apply]`
105. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Opsi filter dan hasil saringan mengikuti perubahan record oleh aktor lain
106. Pilih opsi `Assign return` pada field `Source`
107. Klik `[Apply]`
108. Verifikasi baris `Filter Aset {runId} - 8` tampil dan baris `Filter Aset {runId} - 1` dan `Filter Aset {runId} - 2` dan `Filter Aset {runId} - 3` tidak tampil
109. Klik header kolom Actions `⋯`
110. Hapus centang `Source`
111. Verifikasi baris `Filter Aset {runId} - 8` tetap tampil sesudah kolom `Source` disembunyikan karena saringan tidak bergantung pada visibilitas kolom
112. Bima A menjalankan Mark as Repaired atas `Filter Aset {runId} - 8` dengan Repair note `Unit sudah diganti`
113. Muat ulang halaman
114. Klik `[Apply]`
115. Verifikasi baris `Filter Aset {runId} - 8` tidak lagi tampil karena record keluar dari saringan
116. Klik `[Clear Field]`
117. Buka dropdown field `Source`
118. Verifikasi opsi `Assign return` tidak lagi tampil karena tidak ada record berjalan yang membawanya
119. Klik `[Clear Field]`
120. Pilih opsi `Manual` pada field `Source`
121. Klik `[Apply]`
122. Verifikasi baris `Filter Aset {runId} - 1` tampil dan baris `Filter Aset {runId} - 10` tidak tampil
123. Bima A melaporkan aset `Filter Aset {runId} - 10` rusak lewat Report Damaged dengan What happened `Layar retak terbentur` dan Damaged Photo `foto-layar-retak.jpg`
124. Klik `[Apply]`
125. Verifikasi baris `Filter Aset {runId} - 10` tampil karena record baru bersumber `Manual` masuk ke saringan
126. Buka dropdown field `Reported By`
127. Verifikasi opsi `Bima A` tampil sebagai pelapor record baru
128. Klik `[Clear Field]`
129. Klik `[Apply]`
130. Buka dropdown field `Last Holder`
131. Verifikasi opsi `Sari D` tampil pada dropdown `Last Holder`
132. Verifikasi dropdown `Last Holder` tidak memuat opsi untuk nilai kosong `—`
133. Verifikasi baris `Filter Aset {runId} - 3` yang Last Holder-nya `—` tetap tampil tanpa saringan Last Holder

### Clear Filter dan Clear Search mempertahankan Sort dan kriteria lain
134. Klik ikon sort pada header kolom `Name`
135. Verifikasi tiga baris pertama berurutan menaik: `Filter Aset {runId} - 1`, `Filter Aset {runId} - 2`, lalu `Filter Aset {runId} - 3`
136. Pilih Group `Warehouse {runId}` pada field `Group`
137. Klik `[Apply]`
138. Verifikasi dua baris pertama berurutan menaik: `Filter Aset {runId} - 6` lalu `Filter Aset {runId} - 7`
139. Verifikasi baris `Filter Aset {runId} - 1` tidak tampil karena Group `Warehouse {runId}` berlaku
140. Klik `[Clear Field]`
141. Klik `[Apply]`
142. Verifikasi Search `{runId}` tetap terisi dan tiga baris pertama tetap berurutan menaik: `Filter Aset {runId} - 1`, `Filter Aset {runId} - 2`, lalu `Filter Aset {runId} - 3`
143. Pilih opsi `Borrow return` pada field `Source`
144. Klik `[Apply]`
145. Verifikasi baris `Filter Aset {runId} - 7` tampil
146. Verifikasi baris `Filter Aset {runId} - 10` yang dibuat dengan Source `Manual` tidak tampil
147. Klik `[Clear Field]`
148. Pilih Group `Warehouse {runId}` pada field `Group`
149. Klik `[Apply]`
150. Ganti isi kotak search dengan `Filter Aset {runId} - 6`, tekan Enter
151. Verifikasi baris `Filter Aset {runId} - 6` tampil
152. Klik `(←)` pada kotak Search
153. Verifikasi Group `Warehouse {runId}` tetap berlaku dan baris berurutan menaik: `Filter Aset {runId} - 6` lalu `Filter Aset {runId} - 7`
154. Verifikasi baris `Filter Aset {runId} - 1` tidak tampil karena Group `Warehouse {runId}` tetap berlaku
155. Klik `[Clear Field]`
156. Klik `[Apply]`

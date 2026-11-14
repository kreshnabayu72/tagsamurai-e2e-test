---
id: TC-FA-FATR-UI-082-changelog-mekanik
title: "Dialog Changelog: Search, Filter, Sort, paginasi, Column Visibility, dan Download"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - "§4.1#p88"
  - "§5#r2"
  - "§5#r3"
  - "§7#r11"
  - "§9.5#r2"
  - "§9.5#r21"
  - "EB-TBL-7@changelog"
  - "EB-SRC-4@changelog"
  - "EB-FLT-2@changelog"
  - "EB-FLT-6@changelog"
  - "EB-SRT-3@changelog"
  - "EB-KOL-1@changelog"
  - "EB-DL-2@changelog"
  - "EB-DL-5"
smoke: []
dependsOn: []
trace:
  §4.1#p88: [2, 90, 91, 171]
  §5#r2: [2, 8]
  §5#r3: [13, 16]
  §7#r11: 175
  §9.5#r2: [3, 5]
  §9.5#r21: 6
  EB-TBL-7@changelog: [106, 108, 110, 112, 114, 116, 120]
  EB-SRC-4@changelog: [11, 13, 14, 17, 19, 20, 22, 24, 26, 27]
  EB-FLT-2@changelog: [32, 34, 36, 40, 42, 44, 46, 47, 50, 55, 57, 59, 71, 75]
  EB-FLT-6@changelog: [83, 85, 86]
  EB-SRT-3@changelog: [94, 96, 98, 101, 102, 103]
  EB-KOL-1@changelog: [124, 125, 126, 128, 130, 135, 140, 147, 149, 151, 157, 166, 168]
  EB-DL-2@changelog: 175
  EB-DL-5: [179, 180, 182]
anchor: [88]
coverage:
  web: automated
---

# Dialog Changelog: Search, Filter, Sort, paginasi, Column Visibility, dan Download

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings, Dialog Changelog dibuka dari tombol `[Changelog]` di header halaman.
- Komponen: Dialog Changelog
- Data:
  - DU-082-1: 26 entri (volume), Date `2026-07-{n} 10:00` dengan n 1 sampai 26 (tampil `{n}/07/26 10:00`), Action `Edit`, Category `Vehicle > Pool car`, Field `Borrow (Max duration)`, Old Value `14 days`, New Value `30 days`, Modified By `Budi Santoso`.
  - DU-082-2: entri Date `2026-06-12 09:30` (tampil `12/06/26 09:30`), Action `Edit`, Category `All categories`, Field `Borrow (Allow Borrow)`, Old Value `Allow`, New Value `Deny`, Modified By `Siti Nurbaya`.
  - DU-082-3: kata kunci Search `Allow Borrow`.
  - DU-082-4: nomor halaman tidak valid `0`.
  - DU-082-5: nomor halaman tidak valid `-1`.
  - DU-082-6: nomor halaman tidak valid `4`.
  - DU-082-7: nomor halaman tidak valid `abc`.
  - DU-082-8: kata kunci pencarian opsi `Zebra Tidak Ada`, tidak cocok dengan opsi mana pun.
  - DU-082-9: pengubah entri `Budi Santoso`.
  - DU-082-10: pengubah entri `Siti Nurbaya`.
  - DU-082-11: pengubah entri `Alexander Graham Bell`.
  - DU-082-12: pengubah entri `John Lennon`.
  - DU-082-13: pengubah entri `Buzzlightyear Sumardi`.
  - DU-082-14: pengubah entri `Rina Wulandari`.
  - DU-082-15: pengubah entri `Dewi Lestari`.
  - DU-082-16: pengubah entri `Agus Pratama`.
- Kondisi:
  - K1: tabel berisi DU-082-1 dan DU-082-2 (27 baris, tiga halaman pada ukuran halaman bawaan), baris tampil dari Date terbaru (baris pertama Date `26/07/26 10:00`); Date Format bernilai `dd/MM/yy`; Time Format bernilai `24h`; respons atas Search DU-082-3 hanya memuat DU-082-2; opsi filter `Category` adalah `Vehicle > Pool car` dan `All categories`; opsi filter `Field` adalah `Borrow (Max duration)` dan `Borrow (Allow Borrow)`; opsi filter `Modified By` adalah DU-082-9, DU-082-10, DU-082-11, DU-082-12, DU-082-13, DU-082-14, DU-082-15, dan DU-082-16.
  - K2: sama dengan K1, tetapi sumber opsi filter `Modified By` kosong.
  - K3: sama dengan K1, tetapi permintaan unduhan gagal karena error server.
  - K4: tabel berisi lebih dari 5.000 entri; server menyiapkan berkas unduhan dan baru menyelesaikannya sesudah loading screen tampil.

## Test Steps

### Default tanpa filter, paginasi, dan pilihan ukuran halaman
1. Tampilkan Dialog Changelog dengan kondisi K1
2. Verifikasi tabel menampilkan 10 baris pada halaman 1 dengan ukuran halaman `10`
3. Verifikasi tombol filter tidak menampilkan indikator filter aktif
4. Klik tombol filter di toolbar
5. Verifikasi field filter `Date`, `Category`, `Field`, dan `Modified By` menampilkan placeholder `Select date`, `All categories`, `All fields`, dan `All users`, tanpa opsi terpilih
6. Verifikasi Filter Panel tidak memuat field filter `Action`
7. Klik dropdown `Rows per page`
8. Verifikasi pilihan ukuran halaman hanya `10`, `25`, `50`, dan `100`

### Search dikirim saat Enter dan siklus kotak Search
9. Tampilkan Dialog Changelog dengan kondisi K1
10. Klik ikon Search di toolbar
11. Verifikasi kotak input Search tampil dan fokus berada pada kotak input
12. Ketik `Allow Borrow` di kotak Search tanpa menekan Enter
13. Verifikasi pencarian `Allow Borrow` belum dikirim
14. Verifikasi tabel masih menampilkan 10 baris pada halaman 1
15. Tekan Enter
16. Verifikasi pencarian `Allow Borrow` dikirim saat Enter, tanpa jeda debounce
17. Verifikasi tabel menampilkan baris hasil pencarian dengan Field `Borrow (Allow Borrow)`
18. Klik `✕` pada kotak Search
19. Verifikasi kotak Search kosong dan tetap terbuka
20. Verifikasi tabel masih menampilkan baris hasil pencarian dengan Field `Borrow (Allow Borrow)`
21. Tekan Enter dengan kotak Search kosong
22. Verifikasi tabel kembali menampilkan 10 baris pada halaman 1 tanpa saringan pencarian
23. Ketik Search `Allow Borrow`, tekan Enter
24. Verifikasi tabel menampilkan baris hasil pencarian dengan Field `Borrow (Allow Borrow)`
25. Klik `(←)` pada kotak Search
26. Verifikasi kotak Search tertutup dan hanya ikon Search yang tampil
27. Verifikasi tabel kembali menampilkan 10 baris pada halaman 1 tanpa saringan pencarian

### Filter Panel: draf dibuang, chip, hapus chip, dan indikator aktif
28. Tampilkan Dialog Changelog dengan kondisi K1
29. Klik tombol filter di toolbar
30. Klik field filter `Category`
31. Pilih opsi `Vehicle > Pool car` pada field filter `Category`
32. Verifikasi chip `Vehicle > Pool car` tampil pada field filter `Category`
33. Klik tombol filter di toolbar untuk menutup Filter Panel tanpa `[Apply]`
34. Verifikasi tabel masih menampilkan 10 baris pada halaman 1 tanpa saringan
35. Klik tombol filter di toolbar untuk membuka kembali Filter Panel
36. Verifikasi field filter `Category` menampilkan placeholder `All categories` tanpa chip `Vehicle > Pool car`, draf yang belum di-Apply dibuang
37. Klik field filter `Category`
38. Pilih opsi `All categories` pada field filter `Category`
39. Pilih opsi `Vehicle > Pool car` pada field filter `Category`
40. Verifikasi chip `All categories` dan `Vehicle > Pool car` tampil pada field filter `Category`
41. Klik `✕` pada chip `All categories` di field filter `Category`
42. Verifikasi chip `All categories` hilang dan chip `Vehicle > Pool car` tetap tampil pada field filter `Category`
43. Klik field filter `Category`
44. Verifikasi opsi `All categories` tidak tercentang dan opsi `Vehicle > Pool car` tercentang
45. Klik `[Apply]`
46. Verifikasi filter yang dikirim pada `Category` hanya memuat opsi `Vehicle > Pool car`
47. Verifikasi tombol filter menampilkan indikator filter aktif
48. Klik `[Clear Field]`
49. Klik `[Apply]`
50. Verifikasi tombol filter tidak menampilkan indikator filter aktif

### Dropdown filter: uncheck opsi dan pencarian di dalam opsi
51. Tampilkan Dialog Changelog dengan kondisi K1
52. Klik tombol filter di toolbar
53. Klik field filter `Modified By`
54. Pilih opsi `Budi Santoso` pada field filter `Modified By`
55. Verifikasi chip `Budi Santoso` tampil pada field filter `Modified By`
56. Klik opsi `Budi Santoso` sekali lagi untuk menghapus centangnya
57. Verifikasi chip `Budi Santoso` hilang dari field filter `Modified By`
58. Ketik `Zebra Tidak Ada` pada kotak pencarian opsi
59. Verifikasi daftar opsi menampilkan `No results found`

### Chip ringkasan untuk opsi terpilih yang banyak
60. Tampilkan Dialog Changelog dengan kondisi K1
61. Klik tombol filter di toolbar
62. Klik field filter `Modified By`
63. Pilih opsi `Budi Santoso` pada field filter `Modified By`
64. Pilih opsi `Siti Nurbaya` pada field filter `Modified By`
65. Pilih opsi `Alexander Graham Bell` pada field filter `Modified By`
66. Pilih opsi `John Lennon` pada field filter `Modified By`
67. Pilih opsi `Buzzlightyear Sumardi` pada field filter `Modified By`
68. Pilih opsi `Rina Wulandari` pada field filter `Modified By`
69. Pilih opsi `Dewi Lestari` pada field filter `Modified By`
70. Pilih opsi `Agus Pratama` pada field filter `Modified By`
71. Verifikasi jumlah chip yang tampil ditambah N pada chip ringkasan `+N more` sama dengan `8`

### Sumber opsi filter kosong
72. Tampilkan Dialog Changelog dengan kondisi K2
73. Klik tombol filter di toolbar
74. Klik field filter `Modified By`
75. Verifikasi daftar opsi menampilkan `No options available`

### Menyembunyikan kolom tidak menghapus field filter dan filter ter-Apply
76. Tampilkan Dialog Changelog dengan kondisi K1
77. Klik tombol filter di toolbar
78. Klik field filter `Category`
79. Pilih opsi `Vehicle > Pool car` pada field filter `Category`
80. Klik `[Apply]`
81. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
82. Hilangkan centang kolom `Category` pada Column Visibility
83. Verifikasi tabel tidak menampilkan header kolom `Category`
84. Klik tombol filter di toolbar untuk membuka kembali Filter Panel
85. Verifikasi field filter `Category` tetap ada pada Filter Panel
86. Verifikasi chip `Vehicle > Pool car` tetap tampil pada field filter `Category` dan tombol filter tetap menampilkan indikator filter aktif

### Header kolom Actions membuka Column Visibility
87. Tampilkan Dialog Changelog dengan kondisi K1
88. Verifikasi baris pertama tabel memiliki Date `26/07/26 10:00`
89. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
90. Verifikasi daftar Column Visibility tampil dan memuat `Setup Column...`
91. Verifikasi baris pertama tabel tetap memiliki Date `26/07/26 10:00`, klik header kolom Actions tidak mengubah urutan

### Siklus tiga klik sort dan kolom tanpa ikon sort
92. Tampilkan Dialog Changelog dengan kondisi K1
93. Klik header kolom `Category`
94. Verifikasi header kolom `Category` menampilkan indikator naik `(↑)`
95. Klik header kolom `Category`
96. Verifikasi header kolom `Category` menampilkan indikator turun `(↓)`
97. Klik header kolom `Category`
98. Verifikasi header kolom `Category` tidak menampilkan indikator sort
99. Klik header kolom `Category`
100. Klik header kolom `Field`
101. Verifikasi header kolom `Field` menampilkan indikator naik `(↑)`
102. Verifikasi header kolom `Category` tidak menampilkan indikator sort
103. Verifikasi header kolom Actions (`⋯`) tidak memiliki ikon sort

### Ukuran halaman, sort, dan nomor halaman tidak valid pada paginasi
104. Tampilkan Dialog Changelog dengan kondisi K1
105. Klik halaman `2`
106. Verifikasi halaman aktif adalah `2`
107. Klik header kolom `Category`
108. Verifikasi halaman aktif tetap `2` sesudah sort diganti
109. Ketik `abc` pada input nomor halaman, tekan Enter
110. Verifikasi halaman aktif tetap `2` dan input `abc` diabaikan
111. Ketik `-1` pada input nomor halaman, tekan Enter
112. Verifikasi halaman aktif berpindah ke halaman `1` karena nomor di bawah 1 dibawa ke halaman 1[^drift-1]
113. Ketik `4` pada input nomor halaman, tekan Enter
114. Verifikasi halaman aktif berpindah ke halaman `3` karena nomor melewati halaman terakhir dibawa ke halaman terakhir[^drift-1]
115. Ketik `0` pada input nomor halaman, tekan Enter
116. Verifikasi halaman aktif berpindah ke halaman `1` karena nomor di bawah 1 dibawa ke halaman 1[^drift-1]
117. Klik halaman `2`
118. Klik dropdown `Rows per page`
119. Pilih ukuran halaman `25`
120. Verifikasi halaman aktif kembali ke `1` sesudah ukuran halaman diganti

### Setup Column: anatomi modal, hide, show, batal, dan Save
121. Tampilkan Dialog Changelog dengan kondisi K1
122. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
123. Klik `Setup Column...` pada daftar Column Visibility
124. Verifikasi modal berjudul `Setup Column` dengan deskripsi `Drag and drop to rearrange the order and click the pin to freeze up to 3 columns.`
125. Verifikasi footer modal memuat tombol `[Reset to Default]` dan `[Save]`
126. Verifikasi footer modal tidak memuat tombol `[Cancel]`
127. Hilangkan centang kolom `Modified By` pada modal
128. Verifikasi tabel di balik modal tidak menampilkan header kolom `Modified By`
129. Klik `[✕]` pada modal Setup Column
130. Verifikasi tabel menampilkan header kolom `Modified By`, perubahan yang belum di-Save dibuang
131. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
132. Klik `Setup Column...` pada daftar Column Visibility
133. Hilangkan centang kolom `Modified By` pada modal
134. Klik `[Save]`
135. Verifikasi modal Setup Column tertutup dan tabel tidak menampilkan header kolom `Modified By`

### Setup Column: reorder kolom
136. Tampilkan Dialog Changelog dengan kondisi K1
137. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
138. Klik `Setup Column...` pada daftar Column Visibility
139. Seret kolom `Modified By` ke posisi pertama pada daftar kolom modal
140. Verifikasi tabel di balik modal menampilkan header kolom `Modified By` sebagai kolom data pertama

### Setup Column: pin dan batas tiga kolom
141. Tampilkan Dialog Changelog dengan kondisi K1
142. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
143. Klik `Setup Column...` pada daftar Column Visibility
144. Klik ikon pin kolom `Date`
145. Klik ikon pin kolom `Action`
146. Klik ikon pin kolom `Category`
147. Verifikasi ikon pin kolom `Field` disabled
148. Arahkan kursor ke ikon pin kolom `Field`
149. Verifikasi alasan `Maximum 3 columns can be pinned at once. Unpin another column first.` tersampaikan pada ikon pin
150. Klik ikon pin kolom `Date` untuk melepas pin
151. Verifikasi ikon pin kolom `Field` kembali aktif

### Setup Column: Reset to Default
152. Tampilkan Dialog Changelog dengan kondisi K1
153. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
154. Klik `Setup Column...` pada daftar Column Visibility
155. Hilangkan centang kolom `Old Value` pada modal
156. Klik `[Reset to Default]`
157. Verifikasi tabel di balik modal menampilkan header kolom `Old Value`

### Kolom visible terakhir tidak bisa disembunyikan
158. Tampilkan Dialog Changelog dengan kondisi K1
159. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
160. Hilangkan centang kolom `Date` pada Column Visibility
161. Hilangkan centang kolom `Action` pada Column Visibility
162. Hilangkan centang kolom `Category` pada Column Visibility
163. Hilangkan centang kolom `Field` pada Column Visibility
164. Hilangkan centang kolom `Old Value` pada Column Visibility
165. Hilangkan centang kolom `New Value` pada Column Visibility
166. Verifikasi centang kolom `Modified By` disabled
167. Arahkan kursor ke centang kolom `Modified By`
168. Verifikasi alasan `At least one column must remain visible.` tersampaikan pada centang kolom `Modified By`

### Popover Download
169. Tampilkan Dialog Changelog dengan kondisi K1
170. Klik ikon Download di toolbar
171. Verifikasi popover Download memuat opsi `Download as CSV` dan `Download as XLSX`

### Unduhan gagal
172. Tampilkan Dialog Changelog dengan kondisi K3
173. Klik ikon Download di toolbar
174. Klik `Download as CSV`
175. Verifikasi toast error `Error, failed to download Changelog-Transaction-Settings.` tampil

### Unduhan lebih dari 5.000 baris
176. Tampilkan Dialog Changelog dengan kondisi K4
177. Klik ikon Download di toolbar
178. Klik `Download as XLSX`
179. Verifikasi loading screen tampil sampai berkas siap
180. Verifikasi tidak ada toast dan tidak ada notifikasi in-app selama berkas disiapkan
181. Tunggu sampai berkas siap
182. Verifikasi loading screen hilang dan berkas langsung terunduh tanpa toast sukses

[^drift-1]: Drift PRD dan foundation vs kontrak komponen. PRD §4.1 (Dialog Changelog): tidak menetapkan perilaku nomor halaman tidak valid, paginasi mengikuti pola bersama foundation. foundation `prd-conventions.md` §9.18: «Nomor halaman tidak valid (0, negatif, melebihi halaman terakhir, bukan angka) pada input nomor halaman: input diabaikan dan tabel tetap di halaman sekarang.» Kontrak `Paginator#9`: «a page past the last goes to the last page, a page below 1 goes to page 1». Diasersi: kontrak untuk nomor `0`, `-1`, dan `4`, sehingga halaman berpindah ke halaman 1 atau halaman terakhir (SB-7); input `abc` tidak bertentangan dengan kontrak dan tetap diabaikan.

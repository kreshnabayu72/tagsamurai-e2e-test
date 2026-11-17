---
id: TC-FA-FATR-UI-072-overrides-mekanik
title: "Tabel Overrides: Search, Filter, Sort, paginasi, dan Column Visibility"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1#r292, §5#r2, §5#r3, §9.5#r2, EB-TBL-7@tabel-overrides, EB-SRC-4@tabel-overrides, EB-FLT-2@tabel-overrides, EB-FLT-6@tabel-overrides, EB-SRT-3@tabel-overrides, EB-KOL-1@tabel-overrides]
smoke: []
dependsOn: []
trace:
  §4.1#r292: [89, 90]
  §5#r2: [2, 7]
  §5#r3: [12, 15]
  §9.5#r2: [3, 5]
  EB-TBL-7@tabel-overrides: [105, 107, 109, 111, 113, 115, 119]
  EB-SRC-4@tabel-overrides: [10, 12, 13, 16, 18, 19, 21, 23, 25, 26]
  EB-FLT-2@tabel-overrides: [31, 33, 35, 39, 41, 43, 45, 46, 49, 54, 56, 58, 70, 74]
  EB-FLT-6@tabel-overrides: [82, 84, 85]
  EB-SRT-3@tabel-overrides: [93, 95, 97, 100, 101, 102]
  EB-KOL-1@tabel-overrides: [123, 124, 125, 127, 129, 131, 136, 141, 148, 150, 152, 159, 166, 168]
anchor: [87]
coverage:
  web: automated
---

# Tabel Overrides: Search, Filter, Sort, paginasi, dan Column Visibility

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings, bagian `Overrides` pada Category dan transaksi terpilih.
- Komponen: Tabel Overrides
- Data:
  - DU-072-1: 20 override (volume), Scope `Group`, Target `Proyek Cabang {n}`, Overridden `Max duration (30 days)`, Category `Vehicle > Pool car`, Created By `Budi Santoso`, Created At `2026-06-15 14:05`.
  - DU-072-2: override Scope `Group`, Target `Proyek Karawang`, Overridden `Max duration (30 days), Max extensions (1)`, Category `Vehicle > Pool car`, Created By `Siti Nurbaya`, Created At `2026-06-12 09:30`.
  - DU-072-3: kata kunci Search `Karawang`.
  - DU-072-4: nomor halaman tidak valid `0`.
  - DU-072-5: nomor halaman tidak valid `-1`.
  - DU-072-6: nomor halaman tidak valid `4`.
  - DU-072-7: nomor halaman tidak valid `abc`.
  - DU-072-8: kata kunci pencarian opsi `Zebra Tidak Ada`, tidak cocok dengan opsi mana pun.
  - DU-072-9: pembuat override `Budi Santoso`.
  - DU-072-10: pembuat override `Siti Nurbaya`.
  - DU-072-11: pembuat override `Alexander Graham Bell`.
  - DU-072-12: pembuat override `John Lennon`.
  - DU-072-13: pembuat override `Buzzlightyear Sumardi`.
  - DU-072-14: pembuat override `Rina Wulandari`.
  - DU-072-15: pembuat override `Dewi Lestari`.
  - DU-072-16: pembuat override `Agus Pratama`.
  - DU-072-17: override Scope `Asset Name`, Target `Excavator PC200`, Overridden `Max duration (10 days)`, Category `Machinery`, Created By `Alexander Graham Bell` (DU-072-11), Created At `2026-06-10 16:45`.
  - DU-072-18: override Scope `Asset`, Target `EXC-0001 · Excavator PC200 - 1`, Overridden `Allow Borrow (Deny)`, Category `Machinery`, Created By `John Lennon` (DU-072-12), Created At `2026-06-09 08:20`.
  - DU-072-19: override Scope `Group`, Target `Proyek Surabaya`, Overridden `Max extensions (2)`, Category `Vehicle > Pool car`, Created By `Buzzlightyear Sumardi` (DU-072-13), Created At `2026-06-08 13:40`.
  - DU-072-20: override Scope `Group`, Target `Proyek Medan`, Overridden `Max duration (14 days)`, Category `Vehicle > Pool car`, Created By `Rina Wulandari` (DU-072-14), Created At `2026-06-07 10:15`.
  - DU-072-21: override Scope `Group`, Target `Proyek Palembang`, Overridden `Max extensions (1)`, Category `Vehicle > Pool car`, Created By `Dewi Lestari` (DU-072-15), Created At `2026-06-06 15:30`.
  - DU-072-22: override Scope `Group`, Target `Proyek Bandung`, Overridden `Max duration (7 days)`, Category `Vehicle > Pool car`, Created By `Agus Pratama` (DU-072-16), Created At `2026-06-05 09:00`.
- Kondisi:
  - K1: tabel berisi DU-072-1, DU-072-2, dan DU-072-17 sampai DU-072-22 (27 baris, tiga halaman pada ukuran halaman bawaan), baris tampil menurut urutan data (baris pertama Target `Proyek Cabang 1`); respons atas Search DU-072-3 hanya memuat DU-072-2; opsi filter `Scope` dan `Created By` diisi dari nilai pada baris tabel itu: opsi `Scope` adalah `Group`, `Asset Name`, dan `Asset`, dan opsi `Created By` adalah DU-072-9, DU-072-10, DU-072-11, DU-072-12, DU-072-13, DU-072-14, DU-072-15, dan DU-072-16.
  - K2: tabel tanpa override, sehingga sumber opsi filter `Created By` kosong.

## Test Steps

### Default tanpa filter dan pilihan ukuran halaman
1. Tampilkan Tabel Overrides dengan kondisi K1
2. Verifikasi tabel menampilkan 10 baris pada halaman 1 dengan ukuran halaman `10`
3. Verifikasi ikon Filter tidak menampilkan indikator filter aktif
4. Klik ikon Filter di toolbar
5. Verifikasi field filter `Scope`, `Overridden`, `Created By`, dan `Category` menampilkan placeholder `All scopes`, `All fields`, `All users`, dan `All categories`, tanpa opsi terpilih
6. Klik dropdown `Rows per page`
7. Verifikasi pilihan ukuran halaman hanya `10`, `25`, `50`, dan `100`

### Search dikirim saat Enter dan siklus kotak Search
8. Tampilkan Tabel Overrides dengan kondisi K1
9. Klik ikon Search di toolbar
10. Verifikasi kotak input Search tampil dan fokus berada pada kotak input
11. Ketik `Karawang` di kotak Search tanpa menekan Enter
12. Verifikasi pencarian `Karawang` belum dikirim
13. Verifikasi tabel masih menampilkan 10 baris pada halaman 1
14. Tekan Enter
15. Verifikasi pencarian `Karawang` dikirim saat Enter, tanpa jeda debounce
16. Verifikasi tabel menampilkan baris hasil pencarian dengan Target `Proyek Karawang`
17. Klik `✕` pada kotak Search
18. Verifikasi kotak Search kosong dan tetap terbuka
19. Verifikasi tabel masih menampilkan baris hasil pencarian dengan Target `Proyek Karawang`
20. Tekan Enter dengan kotak Search kosong
21. Verifikasi tabel kembali menampilkan 10 baris pada halaman 1 tanpa saringan pencarian
22. Ketik Search `Karawang`, tekan Enter
23. Verifikasi tabel menampilkan baris hasil pencarian dengan Target `Proyek Karawang`
24. Klik `(←)` pada kotak Search
25. Verifikasi kotak Search tertutup dan hanya ikon Search yang tampil
26. Verifikasi tabel kembali menampilkan 10 baris pada halaman 1 tanpa saringan pencarian

### Filter Panel: draf dibuang, chip, hapus chip, dan indikator aktif
27. Tampilkan Tabel Overrides dengan kondisi K1
28. Klik ikon Filter di toolbar
29. Klik field filter `Scope`
30. Pilih opsi `Group` pada field filter `Scope`
31. Verifikasi chip `Group` tampil pada field filter `Scope`
32. Klik ikon Filter di toolbar untuk menutup Filter Panel tanpa `[Apply]`
33. Verifikasi tabel masih menampilkan 10 baris pada halaman 1 tanpa saringan
34. Klik ikon Filter di toolbar untuk membuka kembali Filter Panel
35. Verifikasi field filter `Scope` menampilkan placeholder `All scopes`, draf yang belum di-Apply dibuang
36. Klik field filter `Scope`
37. Pilih opsi `Group` pada field filter `Scope`
38. Pilih opsi `Asset` pada field filter `Scope`
39. Verifikasi chip `Group` dan `Asset` tampil pada field filter `Scope`
40. Klik `✕` pada chip `Group` di field filter `Scope`
41. Verifikasi chip `Group` hilang dan chip `Asset` tetap tampil pada field filter `Scope`
42. Klik field filter `Scope`
43. Verifikasi opsi `Group` tidak tercentang dan opsi `Asset` tercentang
44. Klik `[Apply]`
45. Verifikasi filter yang dikirim pada `Scope` hanya memuat opsi `Asset`
46. Verifikasi ikon Filter menampilkan indikator filter aktif
47. Klik `[Clear Field]`
48. Klik `[Apply]`
49. Verifikasi ikon Filter tidak menampilkan indikator filter aktif

### Dropdown filter: uncheck opsi dan pencarian di dalam opsi
50. Tampilkan Tabel Overrides dengan kondisi K1
51. Klik ikon Filter di toolbar
52. Klik field filter `Created By`
53. Pilih opsi `Budi Santoso` pada field filter `Created By`
54. Verifikasi chip `Budi Santoso` tampil pada field filter `Created By`
55. Klik opsi `Budi Santoso` sekali lagi untuk menghapus centangnya
56. Verifikasi chip `Budi Santoso` hilang dari field filter `Created By`
57. Ketik `Zebra Tidak Ada` pada kotak pencarian opsi
58. Verifikasi daftar opsi menampilkan `No results found`

### Chip ringkasan untuk opsi terpilih yang banyak
59. Tampilkan Tabel Overrides dengan kondisi K1
60. Klik ikon Filter di toolbar
61. Klik field filter `Created By`
62. Centang opsi `Budi Santoso` pada field filter `Created By`
63. Centang opsi `Siti Nurbaya` pada field filter `Created By`
64. Centang opsi `Alexander Graham Bell` pada field filter `Created By`
65. Centang opsi `John Lennon` pada field filter `Created By`
66. Centang opsi `Buzzlightyear Sumardi` pada field filter `Created By`
67. Centang opsi `Rina Wulandari` pada field filter `Created By`
68. Centang opsi `Dewi Lestari` pada field filter `Created By`
69. Centang opsi `Agus Pratama` pada field filter `Created By`
70. Verifikasi jumlah chip yang tampil ditambah N pada chip ringkasan `+N more` sama dengan `8`

### Sumber opsi filter kosong
71. Tampilkan Tabel Overrides dengan kondisi K2
72. Klik ikon Filter di toolbar
73. Klik field filter `Created By`
74. Verifikasi daftar opsi menampilkan `No options available`

### Menyembunyikan kolom tidak menghapus field filter dan filter ter-Apply
75. Tampilkan Tabel Overrides dengan kondisi K1
76. Klik ikon Filter di toolbar
77. Klik field filter `Scope`
78. Pilih opsi `Group` pada field filter `Scope`
79. Klik `[Apply]`
80. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
81. Hilangkan centang kolom `Scope` pada Column Visibility
82. Verifikasi tabel tidak menampilkan header kolom `Scope`
83. Klik ikon Filter di toolbar untuk membuka kembali Filter Panel
84. Verifikasi field filter `Scope` tetap ada pada Filter Panel
85. Verifikasi chip `Group` tetap tampil pada field filter `Scope` dan ikon Filter tetap menampilkan indikator filter aktif

### Header kolom Actions membuka Column Visibility
86. Tampilkan Tabel Overrides dengan kondisi K1
87. Verifikasi baris pertama tabel memiliki Target `Proyek Cabang 1`
88. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
89. Verifikasi daftar Column Visibility tampil dan memuat `Setup Column...`
90. Verifikasi baris pertama tabel tetap memiliki Target `Proyek Cabang 1`, klik header kolom Actions tidak mengubah urutan

### Siklus tiga klik sort dan kolom tanpa ikon sort
91. Tampilkan Tabel Overrides dengan kondisi K1
92. Klik header kolom `Scope`
93. Verifikasi header kolom `Scope` menampilkan indikator naik `(↑)`
94. Klik header kolom `Scope`
95. Verifikasi header kolom `Scope` menampilkan indikator turun `(↓)`
96. Klik header kolom `Scope`
97. Verifikasi header kolom `Scope` tidak menampilkan indikator sort
98. Klik header kolom `Scope`
99. Klik header kolom `Target`
100. Verifikasi header kolom `Target` menampilkan indikator naik `(↑)`
101. Verifikasi header kolom `Scope` tidak menampilkan indikator sort
102. Verifikasi header kolom Actions (`⋯`) tidak memiliki ikon sort

### Ukuran halaman, sort, dan nomor halaman tidak valid pada paginasi
103. Tampilkan Tabel Overrides dengan kondisi K1
104. Klik halaman `2`
105. Verifikasi halaman aktif adalah `2`
106. Klik header kolom `Scope`
107. Verifikasi halaman aktif tetap `2` sesudah sort diganti
108. Ketik `abc` pada input nomor halaman, tekan Enter
109. Verifikasi halaman aktif tetap `2` dan input `abc` diabaikan
110. Ketik `-1` pada input nomor halaman, tekan Enter
111. Verifikasi halaman aktif berpindah ke halaman `1` karena nomor di bawah 1 dibawa ke halaman 1
112. Ketik `4` pada input nomor halaman, tekan Enter
113. Verifikasi halaman aktif berpindah ke halaman `3` karena nomor melewati halaman terakhir dibawa ke halaman terakhir
114. Ketik `0` pada input nomor halaman, tekan Enter
115. Verifikasi halaman aktif berpindah ke halaman `1` karena nomor di bawah 1 dibawa ke halaman 1
116. Klik halaman `2`
117. Klik dropdown `Rows per page`
118. Pilih ukuran halaman `25`
119. Verifikasi halaman aktif kembali ke `1` sesudah ukuran halaman diganti

### Setup Column: anatomi modal, hide, show, batal, dan Save
120. Tampilkan Tabel Overrides dengan kondisi K1
121. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
122. Klik `Setup Column...` pada daftar Column Visibility
123. Verifikasi modal berjudul `Setup Column` dengan deskripsi `Drag and drop to rearrange the order and click the pin to freeze up to 3 columns.`
124. Verifikasi footer modal memuat tombol `[Reset to Default]` dan `[Save]`
125. Verifikasi footer modal tidak memuat tombol `[Cancel]`
126. Hilangkan centang kolom `Created By` pada modal
127. Verifikasi tabel di balik modal tidak menampilkan header kolom `Created By`
128. Centang kolom `Category` pada modal
129. Verifikasi tabel di balik modal menampilkan header kolom `Category`
130. Klik `[✕]` pada modal Setup Column
131. Verifikasi tabel menampilkan header kolom `Created By` dan tidak menampilkan header kolom `Category`, perubahan yang belum di-Save dibuang
132. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
133. Klik `Setup Column...` pada daftar Column Visibility
134. Hilangkan centang kolom `Created By` pada modal
135. Klik `[Save]`
136. Verifikasi modal Setup Column tertutup dan tabel tidak menampilkan header kolom `Created By`

### Setup Column: reorder kolom
137. Tampilkan Tabel Overrides dengan kondisi K1
138. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
139. Klik `Setup Column...` pada daftar Column Visibility
140. Seret kolom `Created At` ke posisi pertama pada daftar kolom modal
141. Verifikasi tabel di balik modal menampilkan header kolom `Created At` sebagai kolom data pertama

### Setup Column: pin dan batas tiga kolom
142. Tampilkan Tabel Overrides dengan kondisi K1
143. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
144. Klik `Setup Column...` pada daftar Column Visibility
145. Klik ikon pin kolom `Scope`
146. Klik ikon pin kolom `Target`
147. Klik ikon pin kolom `Overridden`
148. Verifikasi ikon pin kolom `Created By` disabled
149. Arahkan kursor ke ikon pin kolom `Created By`
150. Verifikasi alasan `Maximum 3 columns can be pinned at once. Unpin another column first.` tersampaikan pada ikon pin
151. Klik ikon pin kolom `Scope` untuk melepas pin
152. Verifikasi ikon pin kolom `Created By` kembali aktif

### Setup Column: Reset to Default
153. Tampilkan Tabel Overrides dengan kondisi K1
154. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
155. Klik `Setup Column...` pada daftar Column Visibility
156. Centang kolom `Category` pada modal
157. Hilangkan centang kolom `Overridden` pada modal
158. Klik `[Reset to Default]`
159. Verifikasi tabel di balik modal menampilkan header kolom `Overridden` dan tidak menampilkan header kolom `Category`

### Kolom visible terakhir tidak bisa disembunyikan
160. Tampilkan Tabel Overrides dengan kondisi K1
161. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
162. Hilangkan centang kolom `Scope` pada Column Visibility
163. Hilangkan centang kolom `Target` pada Column Visibility
164. Hilangkan centang kolom `Overridden` pada Column Visibility
165. Hilangkan centang kolom `Created By` pada Column Visibility
166. Verifikasi centang kolom `Created At` disabled
167. Arahkan kursor ke centang kolom `Created At`
168. Verifikasi alasan `At least one column must remain visible.` tersampaikan pada centang kolom `Created At`

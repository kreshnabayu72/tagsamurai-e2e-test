---
id: TC-FA-FASVC-UI-060-tabel-daftar-toolbar-mekanik
title: "Tabel Daftar: Siklus Search, Panel Filter, Indikator Sort, Setup Column, dan Download Gagal"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-SRC-4@tabel-service-center", "EB-FLT-2@tabel-service-center", "EB-FLT-6@tabel-service-center", "EB-SRT-3@tabel-service-center", "EB-KOL-1@tabel-service-center", "EB-KOL-3", "EB-DL-2@tabel-service-center", "EB-DL-5", "TS-FASVC-05", "§9.9#p4"]
smoke: []
dependsOn: []
trace:
  "EB-SRC-4@tabel-service-center": [2, 3, 5, 8, 10, 11, 16, 17, 18, 19, 25, 30, 31]
  "EB-FLT-2@tabel-service-center": [35, 38, 39, 43, 44, 49, 50, 52, 53, 57, 59, 60, 62, 63, 68, 72, 76, 78, 80, 84, 85]
  "EB-FLT-6@tabel-service-center": [90, 93, 94, 95, 96, 97]
  "EB-SRT-3@tabel-service-center": [100, 102, 104, 107, 109, 110, 112, 114, 115]
  "EB-KOL-1@tabel-service-center": [119, 120, 121, 122, 123, 124, 125, 130, 132, 133, 138, 140, 146, 153, 155, 157, 162, 164, 165, 171, 174, 179, 181, 183, 215]
  "EB-KOL-3": [187, 188, 190]
  "EB-DL-2@tabel-service-center": [194, 198]
  "EB-DL-5": [202, 203, 205, 206]
  "TS-FASVC-05": [194, 198]
  "§9.9#p4": [6]
anchor: [214]
coverage:
  web: automated
---
# Tabel Daftar: Siklus Search, Panel Filter, Indikator Sort, Setup Column, dan Download Gagal

## Prerequisites
- Aktor: Total Control.
- Layar awal: Add-ons > Service Center, halaman daftar Service Center.
- Komponen: Tabel Service Center
- Data:
  - DU-060-1: Service Center `PT Sejuk Abadi Teknik`, Service Type `Routine, Repair`, City `Jakarta Selatan`, Usage `148`, Status `Active`, Modified By `Alexander Graham Bell`.
  - DU-060-2: Service Center `CV Genset Prima`, Service Type `Routine`, City `Surabaya`, Usage `24`, Status `Active`, Modified By `Rina Wijaya`.
  - DU-060-3: Service Center `Bengkel Maju Motor`, Service Type `Repair`, City `Bandung`, Usage `0`, Status `Inactive`, Modified By `Budi`.
  - DU-060-4: Service Center `Lab Kalibrasi Pratama`, Service Type `Routine`, City `Johor Bahru`, Usage `3`, Status `Active`, Modified By `Buzzlightyear Sumardi`.
  - DU-060-5: Service Center `UD Cahaya Servis`, Service Type `Repair`, City `Malang`, Usage `0`, Status `Inactive`, Modified By `System`.
  - DU-060-6: Service Center `Servis Pendingin Nusantara`, Service Type `Routine`, City `Semarang`, Usage `7`, Status `Active`, Modified By `Dewi Anggraini`.
  - DU-060-7: Service Center `Teknik Mandiri Utama`, Service Type `Routine`, City `Surabaya`, Usage `12`, Status `Active`, Modified By `Dewi Anggreni`.
  - DU-060-8: Entri Changelog: Action `Updated`, Service Center Name `CV Genset Prima`, Field `City`, Old Value `Malang`, New Value `Surabaya`, Modified By `Rina Wijaya`.
  - DU-060-9: `5001` Service Center `Servis Teknik Nusantara {n}`, Service Type `Routine`, Status `Active`.
  - DU-060-10: Kata kunci: Search toolbar `Genset`; pencarian di dalam daftar opsi City `Kota Tidak Ada`.
- Kondisi:
  - K1: daftar memuat DU-060-1, DU-060-2, dan DU-060-3; respons Search `Genset` memuat DU-060-2 saja; tidak ada konfigurasi kolom tersimpan.
  - K2: daftar memuat DU-060-1 sampai DU-060-7 di halaman pertama; Changelog memuat DU-060-8; tidak ada konfigurasi kolom tersimpan; respons mengikuti Search, filter, dan sort yang diminta; opsi filter berasal dari nilai yang ada di data tabel.
  - K3: daftar kosong tanpa Service Center.
  - K4: daftar memuat DU-060-1 sampai DU-060-3; Download gagal karena error server.
  - K5: respons daftar memuat total DU-060-9 (`5001` baris); respons Download tertunda sampai berkas siap lalu berhasil.
  - K6: seperti K2, dan konfigurasi kolom tersimpan milik aktor menyembunyikan kolom `City`.
  - K7: seperti K2, dan konfigurasi kolom tersimpan milik aktor menyembunyikan kolom `City` dan `Brands`, menempatkan kolom `Status` sebelum kolom `Name`, dan mem-pin kolom `Status`.

## Test Steps

### Ikon Search membuka input dan pencarian berjalan saat Enter
1. Tampilkan Tabel Service Center dengan kondisi K1
2. Verifikasi ikon Search tampil di toolbar
3. Verifikasi kotak input Search belum terlihat
4. Klik ikon Search
5. Verifikasi kotak Search terbuka dengan fokus pada input
6. Verifikasi kotak Search berplaceholder `Search service center...`
7. Ketik Search `Genset` tanpa menekan Enter
8. Verifikasi tabel memuat `PT Sejuk Abadi Teknik`, `CV Genset Prima`, dan `Bengkel Maju Motor`
9. Tekan Enter
10. Verifikasi tabel memuat `CV Genset Prima`
11. Verifikasi tabel tidak memuat `PT Sejuk Abadi Teknik` dan `Bengkel Maju Motor`

### Hapus teks dengan ✕ tidak mereset sebelum Enter
12. Tampilkan Tabel Service Center dengan kondisi K1
13. Klik ikon Search
14. Ketik Search `Genset`, tekan Enter
15. Klik `✕` pada kotak Search
16. Verifikasi kotak Search tetap terbuka
17. Verifikasi kotak Search kosong
18. Verifikasi tabel memuat `CV Genset Prima`
19. Verifikasi tabel tidak memuat `PT Sejuk Abadi Teknik` dan `Bengkel Maju Motor`

### Enter dengan kotak kosong mereset pencarian
20. Tampilkan Tabel Service Center dengan kondisi K1
21. Klik ikon Search
22. Ketik Search `Genset`, tekan Enter
23. Klik `✕` pada kotak Search
24. Tekan Enter
25. Verifikasi tabel memuat `PT Sejuk Abadi Teknik`, `CV Genset Prima`, dan `Bengkel Maju Motor`

### Panah kembali menutup kotak sekaligus mereset
26. Tampilkan Tabel Service Center dengan kondisi K1
27. Klik ikon Search
28. Ketik Search `Genset`, tekan Enter
29. Klik `(←)` pada kotak Search
30. Verifikasi kotak Search tertutup
31. Verifikasi tabel memuat `PT Sejuk Abadi Teknik`, `CV Genset Prima`, dan `Bengkel Maju Motor`

### Menutup panel Filter tanpa Apply membuang draft
32. Tampilkan Tabel Service Center dengan kondisi K2
33. Klik `Filter`
34. Pilih `Inactive` pada Status
35. Verifikasi tabel masih memuat `PT Sejuk Abadi Teknik` dan `Bengkel Maju Motor`
36. Klik `Filter`
37. Klik `Filter`
38. Verifikasi tabel memuat `PT Sejuk Abadi Teknik` dan `Bengkel Maju Motor`
39. Verifikasi field Status kosong dengan placeholder `All statuses`

### Opsi terpilih tampil sebagai chip dan chip overflow diringkas
40. Tampilkan Tabel Service Center dengan kondisi K2
41. Klik `Filter`
42. Pilih `Bandung`, `Jakarta Selatan`, `Johor Bahru`, `Malang`, `Semarang`, dan `Surabaya` pada City
43. Verifikasi chip `Bandung` tampil pada City
44. Verifikasi chip ringkasan `+N more` tampil pada City

### Hapus chip lalu Apply menyaring dengan opsi tersisa
45. Tampilkan Tabel Service Center dengan kondisi K2
46. Klik `Filter`
47. Pilih `Bandung`, `Jakarta Selatan`, `Johor Bahru`, `Malang`, `Semarang`, dan `Surabaya` pada City
48. Klik `✕` pada chip `Bandung`
49. Verifikasi chip `Jakarta Selatan` tampil pada City
50. Verifikasi chip `Bandung` tidak tampil pada City
51. Klik `[Apply]`
52. Verifikasi tabel memuat `PT Sejuk Abadi Teknik`
53. Verifikasi tabel tidak memuat `Bengkel Maju Motor`

### Uncheck opsi menghapus chip dan Apply menyaring
54. Tampilkan Tabel Service Center dengan kondisi K2
55. Klik `Filter`
56. Pilih `Malang` dan `Surabaya` pada City
57. Verifikasi chip `Malang` dan `Surabaya` tampil pada City
58. Klik opsi `Malang` pada daftar opsi City
59. Verifikasi chip `Surabaya` tampil pada City
60. Verifikasi chip `Malang` tidak tampil pada City
61. Klik `[Apply]`
62. Verifikasi tabel memuat `CV Genset Prima` dan `Teknik Mandiri Utama`
63. Verifikasi tabel tidak memuat `UD Cahaya Servis`

### Pencarian di dalam dropdown filter tanpa hasil
64. Tampilkan Tabel Service Center dengan kondisi K2
65. Klik `Filter`
66. Buka daftar opsi City
67. Ketik `Kota Tidak Ada` pada kotak cari di dalam daftar opsi City
68. Verifikasi `No results found` tampil di daftar opsi City

### Sumber opsi kosong menampilkan No options available
69. Tampilkan Tabel Service Center dengan kondisi K3
70. Klik `Filter`
71. Buka daftar opsi Status
72. Verifikasi `No options available` tampil di daftar opsi Status

### Titik indikator pada ikon Filter selama ada filter ter-Apply
73. Tampilkan Tabel Service Center dengan kondisi K2
74. Klik `Filter`
75. Pilih `Inactive` pada Status
76. Verifikasi titik indikator belum tampil pada ikon Filter
77. Klik `[Apply]`
78. Verifikasi titik indikator tampil pada ikon Filter
79. Klik `Filter`
80. Verifikasi titik indikator tetap tampil pada ikon Filter
81. Klik `Filter`
82. Klik `[Clear Field]`
83. Klik `[Apply]`
84. Verifikasi tabel memuat `PT Sejuk Abadi Teknik` dan `Bengkel Maju Motor`
85. Verifikasi titik indikator tidak tampil pada ikon Filter

### Menyembunyikan kolom tidak menghapus field filter dan tidak membatalkan filter ter-Apply
86. Tampilkan Tabel Service Center dengan kondisi K2
87. Klik `Filter`
88. Pilih `Inactive` pada Status
89. Klik `[Apply]`
90. Verifikasi tabel memuat `Bengkel Maju Motor` dan `UD Cahaya Servis`
91. Klik header kolom Actions `⋯`
92. Hapus centang `Status` pada daftar kolom
93. Verifikasi kolom `Name` tampil di tabel
94. Verifikasi kolom `Status` tidak tampil di tabel
95. Verifikasi tabel masih memuat `Bengkel Maju Motor` dan `UD Cahaya Servis`
96. Verifikasi tabel tidak memuat `PT Sejuk Abadi Teknik`
97. Verifikasi field Status masih ada di Filter Panel dengan pilihan `Inactive`

### Siklus tiga klik indikator sort pada kolom Name
98. Tampilkan Tabel Service Center dengan kondisi K2
99. Klik header kolom `Name`
100. Verifikasi kolom `Name` berindikator sort naik
101. Klik header kolom `Name`
102. Verifikasi kolom `Name` berindikator sort turun
103. Klik header kolom `Name`
104. Verifikasi kolom `Name` tanpa indikator sort

### Klik kolom lain memindahkan indikator sort
105. Tampilkan Tabel Service Center dengan kondisi K2
106. Klik header kolom `City`
107. Verifikasi kolom `City` berindikator sort naik
108. Klik header kolom `Usage`
109. Verifikasi kolom `Usage` berindikator sort naik
110. Verifikasi kolom `City` tanpa indikator sort

### Kolom Actions tidak punya ikon sort
111. Tampilkan Tabel Service Center dengan kondisi K2
112. Verifikasi header kolom Actions `⋯` tidak memiliki ikon sort
113. Klik header kolom Actions `⋯`
114. Verifikasi tabel memuat `PT Sejuk Abadi Teknik`
115. Verifikasi tidak ada kolom yang berindikator sort

### Anatomi modal Setup Column
116. Tampilkan Tabel Service Center dengan kondisi K2
117. Klik header kolom Actions `⋯`
118. Klik `Setup Column...`
119. Verifikasi dialog `Setup Columns` tampil[^drift-1]
120. Verifikasi deskripsi `Drag and drop to rearrange the order and click the pin to freeze up to 3 columns.` tampil
121. Verifikasi kotak cari berplaceholder `Search column name...` tampil
122. Verifikasi daftar kolom memuat `Name`, `Service Type`, `Specialization`, `Available To`, `City`, `Brands`, `Usage`, `Status`, `Modified By`, dan `Last Updated`
123. Verifikasi bagian `Preview` tampil
124. Verifikasi tombol `[Reset to Default]` dan `[Save]` tampil di footer dialog
125. Verifikasi dialog tidak memuat tombol `[Cancel]`

### Sembunyikan kolom lewat Setup Column berlaku setelah Save
126. Tampilkan Tabel Service Center dengan kondisi K2
127. Klik header kolom Actions `⋯`
128. Klik `Setup Column...`
129. Hapus centang `City` pada daftar kolom
130. Verifikasi preview tidak memuat kolom `City`
131. Klik `[Save]`
132. Verifikasi dialog `Setup Columns` tertutup[^drift-1]
133. Verifikasi kolom `City` tidak tampil di tabel

### Tampilkan kembali kolom yang disembunyikan lewat Setup Column
134. Tampilkan Tabel Service Center dengan kondisi K6
135. Klik header kolom Actions `⋯`
136. Klik `Setup Column...`
137. Centang `City` pada daftar kolom
138. Verifikasi preview memuat kolom `City`
139. Klik `[Save]`
140. Verifikasi kolom `City` tampil di tabel

### Urutan kolom diubah dengan drag dan berlaku setelah Save
141. Tampilkan Tabel Service Center dengan kondisi K2
142. Klik header kolom Actions `⋯`
143. Klik `Setup Column...`
144. Seret baris `Status` ke atas baris `Name` pada daftar kolom
145. Klik `[Save]`
146. Verifikasi kolom `Status` tampil sebelum kolom `Name` di tabel

### Pin kolom dibatasi tiga dan ikon pin lain nonaktif
147. Tampilkan Tabel Service Center dengan kondisi K2
148. Klik header kolom Actions `⋯`
149. Klik `Setup Column...`
150. Klik pin kolom `Name`
151. Klik pin kolom `Service Type`
152. Klik pin kolom `Specialization`
153. Verifikasi ikon pin kolom `Available To` nonaktif
154. Arahkan kursor ke ikon pin kolom `Available To`
155. Verifikasi alasan `Maximum 3 columns can be pinned at once. Unpin another column first.` tersampaikan
156. Klik pin kolom `Name`
157. Verifikasi ikon pin kolom `Available To` aktif lagi

### Reset to Default mengembalikan seluruh kolom setelah Save
158. Tampilkan Tabel Service Center dengan kondisi K7
159. Klik header kolom Actions `⋯`
160. Klik `Setup Column...`
161. Klik `[Reset to Default]`
162. Verifikasi daftar kolom memuat `Name`, `Service Type`, `Specialization`, `Available To`, `City`, `Brands`, `Usage`, `Status`, `Modified By`, dan `Last Updated` dalam keadaan tercentang
163. Klik `[Save]`
164. Verifikasi tabel memuat kolom `Name`, `Service Type`, `Specialization`, `Available To`, `City`, `Brands`, `Usage`, `Status`, `Modified By`, dan `Last Updated`
165. Verifikasi urutan header tabel dari kiri ke kanan: `Name`, `Service Type`, `Specialization`, `Available To`, `City`, `Brands`, `Usage`, `Status`, `Modified By`, `Last Updated`

### Menutup dialog tanpa Save membuang perubahan
166. Tampilkan Tabel Service Center dengan kondisi K2
167. Klik header kolom Actions `⋯`
168. Klik `Setup Column...`
169. Hapus centang `City` dan `Brands` pada daftar kolom
170. Klik `✕` pada dialog `Setup Columns`[^drift-1]
171. Verifikasi tabel memuat kolom `City` dan `Brands`
172. Klik header kolom Actions `⋯`
173. Klik `Setup Column...`
174. Verifikasi kolom `City` dan `Brands` tercentang pada daftar kolom

### Kolom terakhir yang tampil tidak bisa disembunyikan
175. Tampilkan Tabel Service Center dengan kondisi K2
176. Klik header kolom Actions `⋯`
177. Klik `Setup Column...`
178. Hapus centang semua kolom kecuali `Name` pada daftar kolom
179. Verifikasi checkbox `Name` nonaktif pada daftar kolom
180. Arahkan kursor ke checkbox `Name`
181. Verifikasi alasan `At least one column must remain visible.` tersampaikan
182. Centang `City` pada daftar kolom
183. Verifikasi checkbox `Name` aktif lagi pada daftar kolom

### Konfigurasi kolom tabel daftar tidak mengubah tabel Changelog
184. Tampilkan Tabel Service Center dengan kondisi K2
185. Klik header kolom Actions `⋯`
186. Hapus centang `Modified By` pada daftar kolom
187. Verifikasi kolom `Name` tampil di tabel daftar
188. Verifikasi kolom `Modified By` tidak tampil di tabel daftar
189. Klik `Changelog`
190. Verifikasi tabel Changelog memuat kolom `Modified By`

### Download CSV gagal menampilkan toast error
191. Tampilkan Tabel Service Center dengan kondisi K4
192. Klik `Download`
193. Pilih `Download as CSV`
194. Verifikasi toast `Error, failed to download Service-Centers.` tampil

### Download XLSX gagal menampilkan toast error
195. Tampilkan Tabel Service Center dengan kondisi K4
196. Klik `Download`
197. Pilih `Download as XLSX`
198. Verifikasi toast `Error, failed to download Service-Centers.` tampil

### Download di atas 5.000 baris memakai loading screen tanpa toast
199. Tampilkan Tabel Service Center dengan kondisi K5
200. Klik `Download`
201. Pilih `Download as CSV`
202. Verifikasi loading screen tampil
203. Verifikasi toast tidak tampil
204. Berkas selesai disiapkan
205. Verifikasi loading screen tertutup
206. Verifikasi satu berkas langsung terunduh

### Reset to Default melepas pin kolom
207. Tampilkan Tabel Service Center dengan kondisi K7
208. Klik header kolom Actions `⋯`
209. Klik `Setup Column...`
210. Klik `[Reset to Default]`
211. Klik `[Save]`
212. Klik header kolom Actions `⋯`
213. Klik `Setup Column...`
214. Verifikasi daftar kolom memuat `Status`
215. Verifikasi tidak ada kolom yang ter-pin pada daftar kolom

[^drift-1]: Drift foundation vs kontrak komponen. PRD §4.1a (Setup Column mengikuti foundation, tanpa judul sendiri) dan foundation `prd-conventions.md` §9.3: modal berjudul `"Setup Column"`. Kontrak `DataTable#76`: dialog daftar kolom berjudul `Setup Columns`. Diasersi: kontrak, karena judul dialog adalah teks bawaan komponen DataTable (SB-7).

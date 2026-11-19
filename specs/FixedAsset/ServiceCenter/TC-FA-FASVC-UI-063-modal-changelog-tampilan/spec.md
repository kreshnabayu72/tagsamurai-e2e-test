---
id: TC-FA-FASVC-UI-063-modal-changelog-tampilan
title: "Modal Changelog: Kolom, Old dan New Value, Empty State, Gagal Muat, Setup Column, dan Download Gagal"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["T-FASVC-03", "EB-TBL-1@tabel-changelog", "EB-TBL-2@kolom-old-value-changelog", "EB-TBL-2@kolom-new-value-changelog", "EB-TBL-4@modified-by-changelog", "EB-TBL-7@tabel-changelog", "EB-TBL-8@tabel-changelog", "EB-KOL-1@tabel-changelog", "EB-DL-2@tabel-changelog", "S-FASVC-16"]
smoke: []
dependsOn: []
trace:
  "T-FASVC-03": [2, 3, 4, 5, 8, 10, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 24, 25, 26, 27, 28, 29, 32, 33, 36, 45, 48, 49, 50, 51, 52, 53, 162, 166]
  "EB-TBL-1@tabel-changelog": [55, 56, 57, 58, 62, 63, 64, 66, 67, 68, 70]
  "EB-TBL-2@kolom-old-value-changelog": [24, 31]
  "EB-TBL-2@kolom-new-value-changelog": [27, 34]
  "EB-TBL-4@modified-by-changelog": [36, 38, 39, 41, 42, 44, 45]
  "EB-TBL-7@tabel-changelog": [76, 78, 82, 85, 87, 90]
  "EB-TBL-8@tabel-changelog": [72, 73]
  "EB-KOL-1@tabel-changelog": [94, 95, 96, 97, 98, 99, 100, 105, 107, 108, 113, 115, 121, 128, 130, 132, 137, 139, 140, 146, 149, 154, 156, 158, 180]
  "EB-DL-2@tabel-changelog": [162, 166, 170, 171]
  "S-FASVC-16": [55, 56]
anchor: [179]
coverage:
  web: automated
---
# Modal Changelog: Kolom, Old dan New Value, Empty State, Gagal Muat, Setup Column, dan Download Gagal

## Prerequisites
- Aktor: Total Control.
- Layar awal: Add-ons > Service Center, halaman daftar Service Center, modal Changelog terbuka dari tombol `Changelog` di toolbar.
- Komponen: Modal Changelog Service Center
- Data:
  - DU-063-1: Entri Changelog Action `Updated`, Service Center Name `PT Sejuk Abadi Teknik`, Field `City`, Old Value `Bandung`, New Value `Jakarta Selatan`, Modified By `Rina Wijaya`, Date `2026-03-20T16:45:00Z`.
  - DU-063-2: Entri Changelog Action `Updated`, Service Center Name `PT Sejuk Abadi Teknik`, Field `Contact 2 · Phone`, Old Value `+62 8111111111`, New Value `+62 8222222222`, Modified By `Dewi Anggraini`, Date `2026-03-19T13:20:00Z`.
  - DU-063-3: Entri Changelog Action `Inactivated`, Service Center Name `Bengkel Maju Motor`, Field `Status`, Old Value `Active`, New Value `Inactive`, Modified By `System`, Date `2026-03-18T02:00:00Z`.
  - DU-063-4: Entri Changelog Action `Attachment added`, Service Center Name `CV Genset Prima`, Field `Attachment`, Old Value kosong, New Value `kontrak-servis.pdf`, Modified By `Budi Santoso`, Date `2026-03-17T10:30:00Z`.
  - DU-063-5: Entri Changelog Action `Attachment removed`, Service Center Name `CV Genset Prima`, Field `Attachment`, Old Value `kontrak-servis.pdf`, New Value kosong, Modified By `Budi Santoso`, Date `2026-03-16T09:00:00Z`.
  - DU-063-6: Entri Changelog Action `Activated`, Service Center Name `Bengkel Maju Motor`, Field `Status`, Old Value `Inactive`, New Value `Active`, Modified By `Rina Wijaya`, Date `2026-03-15T08:10:00Z`.
  - DU-063-7: Entri Changelog Action `Deleted`, Service Center Name `Lab Kalibrasi Pratama`, Field `Name`, Old Value `Lab Kalibrasi Pratama`, New Value kosong, Modified By `Rina Wijaya`, Date `2026-03-14T07:55:00Z`.
  - DU-063-8: Entri Changelog Action `Created`, Service Center Name `CV Genset Prima`, Field `Name`, Old Value kosong, New Value `CV Genset Prima`, Modified By `Rina Wijaya`, Date `2026-03-10T09:15:00Z`.
  - DU-063-9: Entri Changelog Action `Updated`, Service Center Name `<b>Servis Kilat</b>`, Field `Status`, Old Value `Inactive`, New Value `<i>Aktif</i>`, Modified By `Rina Wijaya`, Date `2026-03-09T09:15:00Z`.
  - DU-063-10: `25` entri Changelog `Perubahan Nusantara {n}`, Action `Updated`, Modified By `Rina Wijaya`.
  - DU-063-11: Pengaturan General Settings: Date Format `dd/MM/yy`, Time Format `24h`, Time Zone `UTC`.
  - DU-063-12: Kata kunci Search `Vendor Tidak Ada`.
- Kondisi:
  - K1: pengaturan memakai DU-063-11; respons Changelog memuat DU-063-1 sampai DU-063-8 dengan urutan Date terbaru lebih dulu; tidak ada konfigurasi kolom tersimpan; respons Search DU-063-12 kosong.
  - K2: pengaturan memakai DU-063-11; respons Changelog kosong tanpa entri.
  - K3: pengaturan memakai DU-063-11; respons Changelog pertama gagal karena error server, respons sesudah `[Try Again]` memuat DU-063-1 sampai DU-063-8.
  - K4: pengaturan memakai DU-063-11; respons Changelog memuat DU-063-9.
  - K5: pengaturan memakai DU-063-11; respons Changelog memuat DU-063-10 dengan total `25` entri, `10` baris per halaman; urutan sort mengikuti permintaan.
  - K6: seperti K1, dan konfigurasi kolom tersimpan milik aktor menyembunyikan kolom `Field`.
  - K7: seperti K1, dan konfigurasi kolom tersimpan milik aktor menyembunyikan kolom `Field` dan `Old Value` menempatkan kolom `Modified By` sebelum kolom `Date`, dan mem-pin kolom `Modified By`.
  - K8: seperti K1, dan Download gagal karena error server.
  - K9: seperti K1, dan Download berhasil.

## Test Steps

### Judul, toolbar, dan kolom modal Changelog
1. Tampilkan Modal Changelog Service Center dengan kondisi K1
2. Verifikasi modal berjudul `Changelog: Service Center` tampil
3. Verifikasi `Search`, `Filter`, dan `Download` tampil di toolbar modal
4. Verifikasi tabel memuat kolom `Date`, `Action`, `Service Center Name`, `Field`, `Old Value`, `New Value`, dan `Modified By`
5. Verifikasi tabel tidak memuat row action

### Search modal Changelog berplaceholder Search changelog
6. Tampilkan Modal Changelog Service Center dengan kondisi K1
7. Klik ikon Search
8. Verifikasi kotak Search berplaceholder `Search changelog...`

### Urutan default Date terbaru
9. Tampilkan Modal Changelog Service Center dengan kondisi K1
10. Verifikasi baris berurutan dari atas: `PT Sejuk Abadi Teknik` Date `20/03/26, 16:45`, `PT Sejuk Abadi Teknik` Date `19/03/26, 13:20`, `Bengkel Maju Motor` Date `18/03/26, 02:00`, `CV Genset Prima` Date `17/03/26, 10:30`, `CV Genset Prima` Date `16/03/26, 09:00`, `Bengkel Maju Motor` Date `15/03/26, 08:10`, `Lab Kalibrasi Pratama` Date `14/03/26, 07:55`, `CV Genset Prima` Date `10/03/26, 09:15`

### Action tampil sebagai teks biasa untuk ketujuh jenis
11. Tampilkan Modal Changelog Service Center dengan kondisi K1
12. Verifikasi Action baris `PT Sejuk Abadi Teknik` Date `20/03/26, 16:45` menampilkan `Updated`
13. Verifikasi Action baris `Bengkel Maju Motor` Date `18/03/26, 02:00` menampilkan `Inactivated`
14. Verifikasi Action baris `CV Genset Prima` Date `17/03/26, 10:30` menampilkan `Attachment added`
15. Verifikasi Action baris `CV Genset Prima` Date `16/03/26, 09:00` menampilkan `Attachment removed`
16. Verifikasi Action baris `Bengkel Maju Motor` Date `15/03/26, 08:10` menampilkan `Activated`
17. Verifikasi Action baris `Lab Kalibrasi Pratama` Date `14/03/26, 07:55` menampilkan `Deleted`
18. Verifikasi Action baris `CV Genset Prima` Date `10/03/26, 09:15` menampilkan `Created`

### Field contact person memuat nomor kontak dan nilai lama dan baru
19. Tampilkan Modal Changelog Service Center dengan kondisi K1
20. Verifikasi Field baris `PT Sejuk Abadi Teknik` Date `19/03/26, 13:20` menampilkan `Contact 2 · Phone`
21. Verifikasi Old Value baris itu menampilkan `+62 8111111111`
22. Verifikasi New Value baris itu menampilkan `+62 8222222222`

### Old Value strip untuk Created dan New Value strip untuk Deleted
23. Tampilkan Modal Changelog Service Center dengan kondisi K1
24. Verifikasi Old Value baris Created `CV Genset Prima` menampilkan `—`
25. Verifikasi New Value baris Created `CV Genset Prima` menampilkan `CV Genset Prima`
26. Verifikasi Old Value baris Deleted `Lab Kalibrasi Pratama` menampilkan `Lab Kalibrasi Pratama`
27. Verifikasi New Value baris Deleted `Lab Kalibrasi Pratama` menampilkan `—`
28. Verifikasi Old Value baris Updated `PT Sejuk Abadi Teknik` Date `20/03/26, 16:45` menampilkan `Bandung`
29. Verifikasi New Value baris Updated `PT Sejuk Abadi Teknik` Date `20/03/26, 16:45` menampilkan `Jakarta Selatan`

### Old dan New Value pada lampiran strip pada sisi yang kosong
30. Tampilkan Modal Changelog Service Center dengan kondisi K1
31. Verifikasi Old Value baris `Attachment added` menampilkan `—`
32. Verifikasi New Value baris `Attachment added` menampilkan `kontrak-servis.pdf`
33. Verifikasi Old Value baris `Attachment removed` menampilkan `kontrak-servis.pdf`
34. Verifikasi New Value baris `Attachment removed` menampilkan `—`

### Modified By tampil singkat tanpa titik dengan nama lengkap saat hover
35. Tampilkan Modal Changelog Service Center dengan kondisi K1
36. Verifikasi Modified By baris `Updated` Date `20/03/26, 16:45` menampilkan `Rina W`
37. Arahkan kursor ke Modified By baris `Updated` Date `20/03/26, 16:45`
38. Verifikasi nama lengkap `Rina Wijaya` tersampaikan
39. Verifikasi Modified By baris `Updated` Date `19/03/26, 13:20` menampilkan `Dewi A`
40. Arahkan kursor ke Modified By baris `Updated` Date `19/03/26, 13:20`
41. Verifikasi nama lengkap `Dewi Anggraini` tersampaikan
42. Verifikasi Modified By baris `Attachment added` menampilkan `Budi S`
43. Arahkan kursor ke Modified By baris `Attachment added`
44. Verifikasi nama lengkap `Budi Santoso` tersampaikan
45. Verifikasi Modified By baris `Inactivated` menampilkan `System`

### Panel Filter modal Changelog memuat label dan placeholder
46. Tampilkan Modal Changelog Service Center dengan kondisi K1
47. Klik `Filter`
48. Verifikasi filter `Date` berupa rentang tanggal dengan placeholder `Select date`
49. Verifikasi filter `Action` berupa pilihan ganda dengan pencarian dan placeholder `All actions`
50. Verifikasi filter `Service Center Name` berupa pilihan ganda dengan pencarian dan placeholder `All service centers`
51. Verifikasi filter `Field` berupa pilihan ganda dengan pencarian dan placeholder `All fields`
52. Verifikasi filter `Modified By` berupa pilihan ganda dengan pencarian dan placeholder `All users`
53. Verifikasi tidak ada filter `Old Value` dan `New Value`

### Modal tanpa entri menampilkan No changelog yet tanpa tombol
54. Tampilkan Modal Changelog Service Center dengan kondisi K2
55. Verifikasi `No changelog yet` tampil
56. Verifikasi `Activities and changes will appear here.` tampil
57. Verifikasi empty state tidak memuat tombol
58. Verifikasi `No results found` tidak tampil

### Hasil pencarian kosong menampilkan No results found
59. Tampilkan Modal Changelog Service Center dengan kondisi K1
60. Klik ikon Search
61. Ketik Search `Vendor Tidak Ada`, tekan Enter
62. Verifikasi `No results found` tampil
63. Verifikasi `Try adjusting your search or filter.` tampil
64. Verifikasi `No changelog yet` tidak tampil

### Gagal memuat menampilkan pesan error dengan Try Again, bukan empty state
65. Tampilkan Modal Changelog Service Center dengan kondisi K3
66. Verifikasi `Unable to load this data.` tampil
67. Verifikasi tombol `[Try Again]` tampil
68. Verifikasi `No changelog yet` dan `No results found` tidak tampil
69. Klik `[Try Again]`
70. Verifikasi baris `Lab Kalibrasi Pratama` Date `14/03/26, 07:55` tampil

### Teks sel yang memuat markup tampil apa adanya
71. Tampilkan Modal Changelog Service Center dengan kondisi K4
72. Verifikasi Service Center Name `<b>Servis Kilat</b>` tampil apa adanya sebagai teks
73. Verifikasi New Value `<i>Aktif</i>` tampil apa adanya sebagai teks

### Ganti page size kembali ke halaman 1
74. Tampilkan Modal Changelog Service Center dengan kondisi K5
75. Klik halaman `2`
76. Verifikasi laporan paginasi `Showing 11 to 20 of 25` tampil
77. Pilih `25` pada Rows per page
78. Verifikasi laporan paginasi `Showing 1 to 25 of 25` tampil

### Ganti sort tetap di halaman sekarang
79. Tampilkan Modal Changelog Service Center dengan kondisi K5
80. Klik halaman `2`
81. Klik header kolom `Action`
82. Verifikasi laporan paginasi `Showing 11 to 20 of 25` tetap tampil

### Nomor halaman tidak valid mengikuti perilaku Paginator
83. Tampilkan Modal Changelog Service Center dengan kondisi K5
84. Isi Jump to page dengan `99`, tekan Enter
85. Verifikasi laporan paginasi `Showing 21 to 25 of 25` tampil
86. Isi Jump to page dengan `0`, tekan Enter
87. Verifikasi laporan paginasi `Showing 1 to 10 of 25` tampil
88. Klik halaman `2`
89. Isi Jump to page dengan `abc`, tekan Enter
90. Verifikasi laporan paginasi `Showing 11 to 20 of 25` tetap tampil

### Anatomi modal Setup Column pada tabel Changelog
91. Tampilkan Modal Changelog Service Center dengan kondisi K1
92. Klik header kolom Actions `⋯`
93. Klik `Setup Column...`
94. Verifikasi dialog `Setup Columns` tampil[^drift-1]
95. Verifikasi deskripsi `Drag and drop to rearrange the order and click the pin to freeze up to 3 columns.` tampil
96. Verifikasi kotak cari berplaceholder `Search column name...` tampil
97. Verifikasi daftar kolom memuat `Date`, `Action`, `Service Center Name`, `Field`, `Old Value`, `New Value`, dan `Modified By`
98. Verifikasi bagian `Preview` tampil
99. Verifikasi tombol `[Reset to Default]` dan `[Save]` tampil di footer dialog
100. Verifikasi dialog tidak memuat tombol `[Cancel]`

### Sembunyikan kolom Field lewat Setup Column berlaku setelah Save
101. Tampilkan Modal Changelog Service Center dengan kondisi K1
102. Klik header kolom Actions `⋯`
103. Klik `Setup Column...`
104. Hapus centang `Field` pada daftar kolom
105. Verifikasi preview tidak memuat kolom `Field`
106. Klik `[Save]`
107. Verifikasi dialog `Setup Columns` tertutup[^drift-1]
108. Verifikasi kolom `Field` tidak tampil di tabel Changelog

### Tampilkan kembali kolom Field yang disembunyikan lewat Setup Column
109. Tampilkan Modal Changelog Service Center dengan kondisi K6
110. Klik header kolom Actions `⋯`
111. Klik `Setup Column...`
112. Centang `Field` pada daftar kolom
113. Verifikasi preview memuat kolom `Field`
114. Klik `[Save]`
115. Verifikasi kolom `Field` tampil di tabel Changelog

### Urutan kolom diubah dengan drag dan berlaku setelah Save
116. Tampilkan Modal Changelog Service Center dengan kondisi K1
117. Klik header kolom Actions `⋯`
118. Klik `Setup Column...`
119. Seret baris `Modified By` ke atas baris `Date` pada daftar kolom
120. Klik `[Save]`
121. Verifikasi kolom `Modified By` tampil sebelum kolom `Date` di tabel Changelog

### Pin kolom dibatasi tiga dan ikon pin lain nonaktif
122. Tampilkan Modal Changelog Service Center dengan kondisi K1
123. Klik header kolom Actions `⋯`
124. Klik `Setup Column...`
125. Klik pin kolom `Date`
126. Klik pin kolom `Action`
127. Klik pin kolom `Service Center Name`
128. Verifikasi ikon pin kolom `Field` nonaktif
129. Arahkan kursor ke ikon pin kolom `Field`
130. Verifikasi alasan `Maximum 3 columns can be pinned at once. Unpin another column first.` tersampaikan
131. Klik pin kolom `Date`
132. Verifikasi ikon pin kolom `Field` aktif lagi

### Reset to Default mengembalikan seluruh kolom setelah Save
133. Tampilkan Modal Changelog Service Center dengan kondisi K7
134. Klik header kolom Actions `⋯`
135. Klik `Setup Column...`
136. Klik `[Reset to Default]`
137. Verifikasi daftar kolom memuat `Date`, `Action`, `Service Center Name`, `Field`, `Old Value`, `New Value`, dan `Modified By` dalam keadaan tercentang
138. Klik `[Save]`
139. Verifikasi tabel memuat kolom `Date`, `Action`, `Service Center Name`, `Field`, `Old Value`, `New Value`, dan `Modified By`
140. Verifikasi urutan header tabel dari kiri ke kanan: `Date`, `Action`, `Service Center Name`, `Field`, `Old Value`, `New Value`, `Modified By`

### Menutup dialog tanpa Save membuang perubahan
141. Tampilkan Modal Changelog Service Center dengan kondisi K1
142. Klik header kolom Actions `⋯`
143. Klik `Setup Column...`
144. Hapus centang `Field` dan `Old Value` pada daftar kolom
145. Klik `✕` pada dialog `Setup Columns`[^drift-1]
146. Verifikasi tabel memuat kolom `Field` dan `Old Value`
147. Klik header kolom Actions `⋯`
148. Klik `Setup Column...`
149. Verifikasi kolom `Field` dan `Old Value` tercentang pada daftar kolom

### Kolom terakhir yang tampil tidak bisa disembunyikan
150. Tampilkan Modal Changelog Service Center dengan kondisi K1
151. Klik header kolom Actions `⋯`
152. Klik `Setup Column...`
153. Hapus centang semua kolom kecuali `Date` pada daftar kolom
154. Verifikasi checkbox `Date` nonaktif pada daftar kolom
155. Arahkan kursor ke checkbox `Date`
156. Verifikasi alasan `At least one column must remain visible.` tersampaikan
157. Centang `Field` pada daftar kolom
158. Verifikasi checkbox `Date` aktif lagi pada daftar kolom

### Download CSV gagal menampilkan toast error
159. Tampilkan Modal Changelog Service Center dengan kondisi K8
160. Klik `Download`
161. Pilih `Download as CSV`
162. Verifikasi toast `Error, failed to download Changelog-Service-Center.` tampil

### Download XLSX gagal menampilkan toast error
163. Tampilkan Modal Changelog Service Center dengan kondisi K8
164. Klik `Download`
165. Pilih `Download as XLSX`
166. Verifikasi toast `Error, failed to download Changelog-Service-Center.` tampil

### Download berhasil tanpa toast
167. Tampilkan Modal Changelog Service Center dengan kondisi K9
168. Klik `Download`
169. Pilih `Download as CSV`
170. Verifikasi satu berkas terunduh
171. Verifikasi toast tidak tampil

### Reset to Default melepas pin kolom
172. Tampilkan Modal Changelog Service Center dengan kondisi K7
173. Klik header kolom Actions `⋯`
174. Klik `Setup Column...`
175. Klik `[Reset to Default]`
176. Klik `[Save]`
177. Klik header kolom Actions `⋯`
178. Klik `Setup Column...`
179. Verifikasi daftar kolom memuat `Modified By`
180. Verifikasi tidak ada kolom yang ter-pin pada daftar kolom

[^drift-1]: Drift foundation vs kontrak komponen. PRD §4.1c tidak menetapkan judul dialog Setup Column sendiri; foundation `prd-conventions.md` §9.3: modal berjudul `"Setup Column"`. Kontrak `DataTable#76`: dialog daftar kolom berjudul `Setup Columns`. Diasersi: kontrak, karena judul dialog adalah teks bawaan komponen DataTable (SB-7).

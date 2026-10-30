---
id: TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar
title: "Overlay Column Visibility dan Setup Column Daftar Reader Handheld Reader: Screening, Hide/Show, Reorder, Pin, Reset to Default, dan Persistensi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-277
  - TC-GS-HHR-278
  - TC-GS-HHR-279
  - TC-GS-HHR-280
  - TC-GS-HHR-281
  - TC-GS-HHR-282
  - TC-GS-HHR-283
  - TC-GS-HHR-284
  - TC-GS-HHR-285
  - TC-GS-HHR-286
  - TC-GS-HHR-287
  - TC-GS-HHR-288
  - TC-GS-HHR-289
  - TC-GS-HHR-290
  - TC-GS-HHR-291
coverage:
  web: automated
---

# Overlay Column Visibility dan Setup Column Daftar Reader Handheld Reader: Screening, Hide/Show, Reorder, Pin, Reset to Default, dan Persistensi

## Prerequisites

- Mode: FE+BE (backend nyata). Preferensi kolom (visibilitas, urutan, pin) tersimpan per tabel di browser dan menjadi permanen setelah `[Save]` (kecuali Overlay Column Visibility yang langsung berlaku); tabel dimuat dari backend nyata.
- Akun aktor hook `before`: Total Control (Sari Dewi), Client A, `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Langkah 194 dan 195 (TC-GS-HHR-291) logout lalu login kembali dengan akun dan password yang sama pada browser yang sama. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader dengan konfigurasi kolom tabel Daftar Reader pada default.
- Client A: plan Growth, format tanggal default General Settings `dd/MM/yy` 24-hour (tidak diubah spec ini).
- Data Dinamis Seed Reader A (10 reader DD-01 sampai DD-10), dibuat lewat fixture backend sebelum eksekusi (`Fixture.hardwareHandheldReader.seedReaderA`) dan dipulihkan antar TC oleh fixture backend; dipakai sebagai precondition TC, tidak diasersi (asersi spec ini hanya menyangkut kolom, bukan isi baris). Spec tidak mengubah data reader.
- Data uji kolom Hideable (default tampil; urutan default pada tabel):

| Urutan default | Kolom |
|---|---|
| 1 | `Device Name` |
| 2 | `Alias Name` |
| 3 | `Serial Number` |
| 4 | `SKU` |
| 5 | `Range Type` |
| 6 | `Reader Power` |
| 7 | `Source` |
| 8 | `Last Scanned` |
| 9 | `Status` |

- Data uji kolom Curated (default tersembunyi): `Brand`, `Model/Type`, `Last Scanned In`, `Last User`, `Activated At`.
- Perulangan per kolom: langkah 27 sampai 40 (9 kolom Hideable), 41 sampai 53 (5 kolom Curated), 54 sampai 66 (9 kolom Hideable), 70 sampai 76 (5 kolom Curated), 79 sampai 95 (9 kolom Hideable), dan 99 sampai 112 (5 kolom Curated); `<Kolom>` dan `<Urutan>` diambil dari baris tabel data uji di atas.
- Kemampuan teknis: kontrol ukuran viewport sehingga tabel dapat digulir horizontal; menyeret (drag and drop) baris kolom pada Popup Setup Column dan Overlay Column Visibility; mengarahkan kursor ke ikon Pin dan checkbox disabled untuk membaca tooltip; menekan `Esc`; membaca urutan dan posisi kolom tabel (kolom data pertama, posisi saat tabel digulir); membaca dan menghapus preferensi kolom tabel di penyimpanan browser.
- Flag Guided Tooltip `guided_tooltip_seen_gs-handheld-reader`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan: konfigurasi kolom tabel Daftar Reader dikembalikan ke default (9 kolom Hideable tampil berurutan, kolom Curated tersembunyi, tanpa pin) lewat langkah pemulihan eksplisit di akhir blok yang mengubahnya (langkah 203 dan 204 untuk blok terakhir); hook `after` sebagai cadangan (`[Reset to Default]` lalu `[Save]`, atau penghapusan preferensi kolom tabel Daftar Reader di browser).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-HHR-277: Screening Overlay Column Visibility Daftar Reader

1. Arahkan kursor ke header kolom Actions `(⋯)` pada tabel Daftar Reader
2. Verifikasi tooltip header kolom Actions `Column Visibility`
3. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
4. Verifikasi daftar kolom berurutan `Device Name`, `Alias Name`, `Serial Number`, `SKU`, `Range Type`, `Reader Power`, `Source`, `Last Scanned`, `Status`, `Brand`, `Model/Type`, `Last Scanned In`, `Last User`, `Activated At`
5. Verifikasi tiap kolom memiliki checkbox
6. Verifikasi tiap kolom memiliki drag handle
7. Verifikasi checkbox 9 kolom Hideable (`Device Name` sampai `Status`) tercentang
8. Verifikasi checkbox 9 kolom Hideable (`Device Name` sampai `Status`) enabled
9. Verifikasi checkbox 5 kolom Curated (`Brand`, `Model/Type`, `Last Scanned In`, `Last User`, `Activated At`) tidak tercentang
10. Verifikasi checkbox 5 kolom Curated (`Brand`, `Model/Type`, `Last Scanned In`, `Last User`, `Activated At`) enabled
11. Verifikasi item `Setup Column...` di bagian bawah overlay

### TC-GS-HHR-278: Screening Popup Setup Column Daftar Reader

12. Klik item `Setup Column...` di bagian bawah overlay
13. Verifikasi judul `Setup Column`
14. Verifikasi deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
15. Verifikasi ikon `[✕]`
16. Verifikasi popup memuat 14 baris kolom data
17. Verifikasi tiap baris kolom data memiliki checkbox
18. Verifikasi tiap baris kolom data memiliki drag handle
19. Verifikasi tiap baris kolom data memiliki ikon Pin
20. Verifikasi baris `Actions` tidak ada
21. Hilangkan centang `Status`
22. Verifikasi tabel di balik popup tidak menampilkan kolom `Status` (merefleksikan state sementara secara real-time)
23. Centang kembali `Status`
24. Verifikasi tombol `[Reset to Default]` dan `[Save]` tampil rata kanan pada footer
25. Verifikasi tidak ada tombol `[Cancel]` pada footer
26. Klik `[✕]` (tutup popup tanpa Save)

### TC-GS-HHR-279: Ceklis kolom Hideable di Popup Setup Column: sembunyikan dan tampilkan kembali

27. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
28. Klik item `Setup Column...` di bagian bawah overlay
29. Hilangkan centang kolom `<Kolom>`
30. Verifikasi kolom `<Kolom>` hilang dari preview
31. Klik `[Save]`
32. Verifikasi kolom `<Kolom>` hilang dari tabel
33. Muat ulang halaman (F5)
34. Verifikasi tabel Daftar Reader tampil kembali (pembanding sebelum asersi absence)
35. Verifikasi kolom `<Kolom>` tetap hilang dari tabel
36. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
37. Klik item `Setup Column...` di bagian bawah overlay
38. Centang kembali kolom `<Kolom>`
39. Klik `[Save]`
40. Verifikasi kolom `<Kolom>` tampil di tabel pada posisi urutan default ke-`<Urutan>`

### TC-GS-HHR-280: Ceklis kolom Curated di Popup Setup Column: tampilkan dan sembunyikan

41. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
42. Klik item `Setup Column...` di bagian bawah overlay
43. Centang kolom `<Kolom>`
44. Verifikasi kolom `<Kolom>` tampil di preview
45. Klik `[Save]`
46. Verifikasi kolom `<Kolom>` tampil di tabel
47. Muat ulang halaman (F5)
48. Verifikasi kolom `<Kolom>` tetap tampil di tabel
49. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
50. Klik item `Setup Column...` di bagian bawah overlay
51. Lepas centang kolom `<Kolom>`
52. Klik `[Save]`
53. Verifikasi kolom `<Kolom>` hilang dari tabel

### TC-GS-HHR-281: Reorder kolom Hideable lewat drag di Popup Setup Column

54. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
55. Klik item `Setup Column...` di bagian bawah overlay
56. Seret kolom `<Kolom>` ke posisi paling atas daftar
57. Verifikasi kolom `<Kolom>` menjadi kolom data pertama pada preview
58. Klik `[Save]`
59. Verifikasi kolom `<Kolom>` menjadi kolom data pertama pada tabel
60. Muat ulang halaman (F5)
61. Verifikasi kolom `<Kolom>` tetap menjadi kolom data pertama pada tabel
62. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
63. Klik item `Setup Column...` di bagian bawah overlay
64. Klik `[Reset to Default]`
65. Klik `[Save]`
66. Verifikasi urutan kolom data pada tabel kembali ke urutan default (`Device Name` sampai `Status`, urutan pada tabel Kolom Hideable)

### TC-GS-HHR-282: Reorder kolom Curated lewat drag di Popup Setup Column

67. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
68. Klik item `Setup Column...` di bagian bawah overlay
69. Centang kelima kolom Curated (`Brand`, `Model/Type`, `Last Scanned In`, `Last User`, `Activated At`)
70. Seret kolom `<Kolom>` ke posisi paling atas daftar
71. Klik `[Save]`
72. Verifikasi kolom `<Kolom>` menjadi kolom data pertama pada tabel
73. Muat ulang halaman (F5)
74. Verifikasi kolom `<Kolom>` tetap menjadi kolom data pertama pada tabel
75. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
76. Klik item `Setup Column...` di bagian bawah overlay
77. Klik `[Reset to Default]` (pemulihan konfigurasi kolom)
78. Klik `[Save]`

### TC-GS-HHR-283: Pin dan Unpin kolom Hideable membekukan kolom ke kiri

79. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
80. Klik item `Setup Column...` di bagian bawah overlay
81. Klik ikon Pin kolom `<Kolom>`
82. Klik `[Save]`
83. Gulir tabel secara horizontal ke tepi kanan
84. Verifikasi kolom `<Kolom>` tetap di posisinya (freeze kiri) saat tabel digulir horizontal
85. Muat ulang halaman (F5)
86. Gulir tabel secara horizontal ke tepi kanan
87. Verifikasi kolom `<Kolom>` tetap di posisinya (freeze kiri) setelah muat ulang halaman
88. Gulir tabel secara horizontal kembali ke tepi kiri
89. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
90. Klik item `Setup Column...` di bagian bawah overlay
91. Klik ikon Pin kolom `<Kolom>` lagi (Unpin)
92. Klik `[Save]`
93. Gulir tabel secara horizontal ke tepi kanan
94. Verifikasi kolom `<Kolom>` ikut bergeser saat tabel digulir horizontal
95. Gulir tabel secara horizontal kembali ke tepi kiri

### TC-GS-HHR-284: Pin dan Unpin kolom Curated membekukan kolom ke kiri

96. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
97. Klik item `Setup Column...` di bagian bawah overlay
98. Centang kelima kolom Curated (`Brand`, `Model/Type`, `Last Scanned In`, `Last User`, `Activated At`)
99. Klik ikon Pin kolom `<Kolom>`
100. Klik `[Save]`
101. Gulir tabel secara horizontal ke tepi kanan
102. Verifikasi kolom `<Kolom>` tetap di posisinya (freeze kiri) saat tabel digulir horizontal
103. Gulir tabel secara horizontal kembali ke tepi kiri
104. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
105. Klik item `Setup Column...` di bagian bawah overlay
106. Klik ikon Pin kolom `<Kolom>` lagi (Unpin)
107. Klik `[Save]`
108. Gulir tabel secara horizontal ke tepi kanan
109. Verifikasi kolom `<Kolom>` ikut bergeser saat tabel digulir horizontal
110. Gulir tabel secara horizontal kembali ke tepi kiri
111. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
112. Klik item `Setup Column...` di bagian bawah overlay
113. Klik `[Reset to Default]` (pemulihan konfigurasi kolom)
114. Klik `[Save]`

### TC-GS-HHR-285: Pin ke-4 dinonaktifkan setelah tiga kolom di-pin

115. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
116. Klik item `Setup Column...` di bagian bawah overlay
117. Klik ikon Pin kolom `Device Name`, `Alias Name`, dan `Serial Number` (tiga kolom di-pin)
118. Arahkan kursor ke ikon Pin kolom `SKU`
119. Verifikasi tooltip ikon Pin kolom `SKU` `Maximum 3 columns can be pinned at once. Unpin another column first.`
120. Verifikasi ikon Pin kolom lain (di luar tiga kolom yang di-pin) disabled
121. Klik ikon Pin kolom `SKU`
122. Verifikasi kolom `SKU` tidak membeku (tidak ter-pin)
123. Klik ikon Pin kolom `Alias Name` (Unpin)
124. Verifikasi ikon Pin kolom lain (di luar dua kolom yang masih di-pin) aktif kembali
125. Klik `[✕]` (tutup popup tanpa Save)

### TC-GS-HHR-286: Reset to Default mengembalikan seluruh konfigurasi ke default setelah Save

126. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
127. Klik item `Setup Column...` di bagian bawah overlay
128. Sembunyikan kolom `Status`, tampilkan kolom `Brand`, dan pin kolom `Device Name`
129. Klik `[Save]`
130. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
131. Klik item `Setup Column...` di bagian bawah overlay
132. Klik `[Reset to Default]`
133. Verifikasi preview kembali ke 9 kolom default (`Device Name` sampai `Status`, tanpa `Brand`)
134. Verifikasi preview kembali ke urutan awal kolom
135. Verifikasi tidak ada kolom yang di-pin pada preview
136. Klik `[Save]`
137. Verifikasi tabel menampilkan konfigurasi default (9 kolom default, urutan awal, tanpa pin)
138. Muat ulang halaman (F5)
139. Verifikasi tabel tetap menampilkan konfigurasi default setelah muat ulang halaman

### TC-GS-HHR-287: Menutup Popup Setup Column lewat X atau Esc membuang perubahan preview

140. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
141. Klik item `Setup Column...` di bagian bawah overlay
142. Sembunyikan kolom `Status`
143. Klik `[✕]`
144. Verifikasi popup Setup Column tertutup
145. Verifikasi kolom `Status` tampil di tabel (state tersimpan terakhir)
146. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
147. Klik item `Setup Column...` di bagian bawah overlay
148. Sembunyikan kolom `Alias Name`
149. Tekan `Esc`
150. Verifikasi kolom `Alias Name` tetap tampil di tabel

### TC-GS-HHR-288: Kolom terakhir yang tersisa tidak dapat disembunyikan

151. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
152. Klik item `Setup Column...` di bagian bawah overlay
153. Lepas centang semua kolom kecuali `Device Name`
154. Arahkan kursor ke checkbox `Device Name`
155. Verifikasi tooltip checkbox `Device Name` `At least one column must remain visible.`
156. Verifikasi checkbox `Device Name` disabled
157. Klik checkbox `Device Name`
158. Verifikasi kolom `Device Name` tidak tersembunyi
159. Verifikasi tabel (preview) tetap memiliki 1 kolom data
160. Klik `[✕]` (tutup popup tanpa Save)

### TC-GS-HHR-289: Kolom Actions selalu di kanan, tidak muncul di Setup Column, dan tetap terlihat saat scroll

161. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
162. Klik item `Setup Column...` di bagian bawah overlay
163. Verifikasi daftar Setup Column memuat 14 baris kolom data
164. Verifikasi daftar Setup Column tidak memuat baris `Actions`
165. Klik `[✕]` (tutup popup)
166. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
167. Centang kelima kolom Curated (`Brand`, `Model/Type`, `Last Scanned In`, `Last User`, `Activated At`) pada Overlay Column Visibility
168. Tekan `Esc` (tutup overlay)
169. Gulir tabel secara horizontal ke tepi kanan
170. Verifikasi kolom Actions `(⋯)` tetap terlihat di tepi kanan tabel saat digulir horizontal
171. Gulir tabel secara horizontal kembali ke tepi kiri
172. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
173. Klik item `Setup Column...` di bagian bawah overlay
174. Klik `[Reset to Default]` (pemulihan konfigurasi kolom)
175. Klik `[Save]`

### TC-GS-HHR-290: Perubahan di Overlay Column Visibility langsung diterapkan tanpa Save

176. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
177. Lepas centang kolom `Alias Name` pada Overlay Column Visibility
178. Verifikasi kolom `Alias Name` langsung hilang dari tabel
179. Seret kolom `Status` ke posisi pertama pada Overlay Column Visibility
180. Verifikasi kolom `Status` menjadi kolom data pertama pada tabel
181. Verifikasi overlay tidak memiliki tombol `[Save]`
182. Muat ulang halaman (F5)
183. Verifikasi tabel Daftar Reader tampil kembali (pembanding sebelum asersi absence)
184. Verifikasi kolom `Alias Name` tetap hilang dari tabel
185. Verifikasi kolom `Status` tetap menjadi kolom data pertama pada tabel
186. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
187. Klik item `Setup Column...` di bagian bawah overlay
188. Klik `[Reset to Default]` (pemulihan konfigurasi kolom)
189. Klik `[Save]`

### TC-GS-HHR-291: Konfigurasi kolom tersimpan per tabel di browser dan independen antar tabel

190. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
191. Klik item `Setup Column...` di bagian bawah overlay
192. Sembunyikan kolom `Status`
193. Klik `[Save]`
194. Logout
195. Login kembali sebagai akun yang sama (`totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`) pada browser yang sama
196. Buka Global Settings > Hardware > Handheld Reader
197. Verifikasi tabel Daftar Reader tidak menampilkan kolom `Status`
198. Klik ikon Changelog
199. Verifikasi Modal Changelog menampilkan 7 kolom: `Date`, `Action`, `Device Name`, `Field`, `Old Value`, `New Value`, `Modified By`
200. Tutup Modal Changelog
201. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
202. Klik item `Setup Column...` di bagian bawah overlay
203. Klik `[Reset to Default]` (pemulihan konfigurasi kolom)
204. Klik `[Save]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`, section 4a-4.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (277 sampai 291) dipertahankan; dua TC screening (277, 278) di awal sebelum aksi yang mengubah konfigurasi kolom.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 21 sampai 26 (pengamatan preview real-time pada blok TC-GS-HHR-278: hilangkan centang `Status`, centang kembali, tutup popup tanpa Save); penutupan popup tanpa Save pada akhir blok TC-GS-HHR-285 dan 288; `[Reset to Default]` lalu `[Save]` pada akhir blok TC-GS-HHR-282, 284, 289, 290, dan 291 (pemulihan konfigurasi kolom); `Esc` yang menutup overlay; menggulir tabel kembali ke tepi kiri pada blok TC-GS-HHR-283, 284, dan 289; penutupan Modal Changelog pada blok TC-GS-HHR-291. Pembukaan popup pada langkah 75 dan 76 (akhir tiap iterasi TC-GS-HHR-282) membuka popup untuk iterasi berikutnya, dan pada iterasi terakhir untuk langkah pemulihan; pola yang sama dipakai pada langkah 111 dan 112 (TC-GS-HHR-284).
- Popup Setup Column menutup sendiri setelah `[Save]` dan `[✕]`, sehingga tiap blok dan tiap iterasi membuka popup lewat header Actions `(⋯)` dan `Setup Column...`; langkah pembuka itu merupakan prefix berulang. Pada TC-GS-HHR-282 dan 284 langkah "Centang kelima kolom Curated" dikerjakan sekali pada popup yang sama dengan iterasi pertama, sesuai langkah TC sumber.
- Langkah yang diulang per baris tabel Prerequisites (idiom "Untuk setiap baris tabel"): langkah 27 sampai 40 (9 iterasi), 41 sampai 53 (5), 54 sampai 66 (9), 70 sampai 76 (5), 79 sampai 95 (9), dan 99 sampai 112 (5). Tiap `Verifikasi` yang diulang tetap satu per klausa.
- Spec memuat 204 langkah nominal (sekitar 692 langkah dengan ekspansi blok ulang; di atas smell sekitar 35 langkah). Alasan: seluruhnya satu kelas harness (fungsional, popup dan overlay Setup Column daftar reader yang sama), satu akun, satu dataset, tanpa aksi yang mengubah data reader; tiap blok TC memulihkan konfigurasi kolom ke default sebelum blok berikutnya (hook `after` sebagai cadangan), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Pengulangan per kolom mengikuti Data Uji TC (Hideable dan Curated per kolom).
- Pembagian TC lintas spec: Setup Column tabel sekunder (TC-GS-HHR-292 sampai 305) ada di spec 056; Download terhadap kolom tersembunyi (TC-GS-HHR-308, 309) di spec 057 dan TC-GS-HHR-312 di spec 058; Pagination (TC-GS-HHR-317 sampai 325) di spec 060; Sort dan Filter di spec 052 dan 053; TC-GS-HHR-32 (Step 3 Guided Tooltip dilewati bila `Device Name` disembunyikan lewat Setup Column) di spec 007.
- Temuan untuk QA:
  - TC-GS-HHR-277: Expected a.i (tooltip header kolom Actions saat hover) tidak punya langkah hover di Langkah Uji; spec menambah langkah hover sebelum klik untuk mengamatinya.
  - TC-GS-HHR-278: Expected b.ii ("Tabel di balik popup merefleksikan state sementara secara real-time") tidak punya perubahan state di Langkah Uji; spec menambah langkah penghubung (hilangkan centang `Status`, amati, centang kembali, tutup tanpa Save).
  - TC-GS-HHR-282 dan 283: Expected menyebut "bertahan setelah F5" tetapi Langkah Uji tidak memuat refresh; spec menambah langkah muat ulang halaman. TC-GS-HHR-284 tidak menyebut F5 pada Expected, sehingga tidak ditambahkan.
  - TC-GS-HHR-281: untuk kolom `Device Name` (sudah pertama pada urutan default) menyeret ke posisi paling atas tidak mengubah urutan; asersi "menjadi kolom data pertama" lolos tetapi tidak membuktikan reorder.
  - TC-GS-HHR-283 dan 284: TC tidak menyebut syarat tabel dapat digulir horizontal pada 9 kolom default (TC-GS-HHR-283); spec mengandalkan lebar viewport dan nilai panjang pada DD-09 (kemampuan kontrol viewport di Prerequisites).
  - TC-GS-HHR-285: Expected a ("Ikon Pin kolom lain disabled") tidak menyebut apakah kolom Curated tersembunyi ikut dihitung; spec mengasersi pada seluruh baris di luar kolom yang di-pin.
  - TC-GS-HHR-289: cara "Tampilkan semua kolom curated" tidak disebut; spec memakai Overlay Column Visibility (berlaku langsung tanpa Save) lalu memulihkannya lewat `[Reset to Default]` dan `[Save]`.
  - TC-GS-HHR-291: Langkah Uji nomor 4 menyebut logout lalu login kembali sebagai akun yang sama pada browser yang sama; spec menuliskannya sebagai langkah ganti sesi eksplisit tanpa mengganti akun. Expected b menyebut "7 kolom" tanpa daftar nama; spec memakai daftar kolom dari TC-GS-HHR-292.
  - Mekanisme membaca posisi kolom, menghapus preferensi kolom di browser, dan menggulir tabel tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE.
  - Post Condition semua TC di spec ini `-`; tidak ada yang diasersi.

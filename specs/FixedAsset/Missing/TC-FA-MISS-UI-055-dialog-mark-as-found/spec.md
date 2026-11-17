---
id: TC-FA-MISS-UI-055-dialog-mark-as-found
title: "Dialog Mark as Found: field dan default, Asset Status mengubah label dan kewajiban Photo dan Note, info Found outside, validasi, Asset Status terkunci Damaged, dan respons gagal"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [§4.2.4#p2, §4.2.4#p3, §4.2.4#r4, §4.2.4#r5, §4.2.4#r6, §4.2.4#r7, §4.2.4#r8, §4.2.4#r9, §4.2.4#r10, §4.2.4#r11, §9.9#r2, §9.9#r3, §9.9#r4, §9.9#r5, §9.9#r6, §9.9#p3, §9.9#p4, §9.5#r8, §7.2#r2, §7.3#r8, §9.6#r4, §4.1#r6, §4.2.4#p6, §9.4.2#r33, §9.4.2#r8, EB-FRM-1@mark-as-found, EB-FRM-2@mark-as-found, EB-FRM-4@mark-as-found, EB-FRM-7@mark-as-found, EB-FB-1@mark-as-found, EB-ERR-1@mark-as-found, EB-SRC-6@found-at]
smoke: []
dependsOn: []
trace:
  §4.2.4#p2: [2, 3, 4, 5, 6, 7, 11, 25, 35, 55, 253, 254]
  §4.2.4#p3: [12, 14, 63, 65, 73, 74]
  §4.2.4#r4: [18, 20, 22]
  §4.2.4#r5: [141, 142]
  §4.2.4#r6: [11, 61, 168]
  §4.2.4#r7: [63, 64, 80, 143]
  §4.2.4#r8: [65, 66, 79, 144]
  §4.2.4#r9: [12, 13, 14, 15, 73, 74, 170]
  §4.2.4#r10: [10, 24, 39]
  §4.2.4#r11: [16, 35, 40]
  §9.9#r2: [6, 8, 20, 25]
  §9.9#r3: [9, 10, 24, 28, 29, 30, 31, 43, 55, 57, 58, 250]
  §9.9#r4: [11, 61, 141, 142, 168]
  §9.9#r5: [15, 66, 79, 84, 89, 91, 93, 95, 97, 99, 128, 170]
  §9.9#r6: [63, 64, 80, 104, 106, 109, 112, 115, 117, 129, 130, 243]
  §9.9#p3: [18, 20, 22]
  §9.9#p4: [80, 104, 106, 109, 110, 112, 115, 117, 120, 121, 129, 130, 230, 231, 232, 234]
  §9.5#r8: [10, 24, 29, 39]
  §7.2#r2: [2, 3]
  §7.3#r8: [148, 157, 163, 166, 170, 177, 211]
  §9.6#r4: [211, 212]
  §4.1#r6: 3
  §4.2.4#p6: [28, 29, 30, 31, 34, 43]
  §9.4.2#r33: [141, 142, 143, 144, 163]
  §9.4.2#r8: [35, 40]
  EB-FRM-1@mark-as-found: [173, 174, 177]
  EB-FRM-2@mark-as-found: [137, 139, 180, 183, 187, 189, 190, 192, 195]
  EB-FRM-4@mark-as-found: [89, 91, 93, 95, 97]
  EB-FRM-7@mark-as-found: [21, 81, 197, 198, 199, 201, 203, 236, 240, 241, 244, 251]
  EB-FB-1@mark-as-found: [146, 148, 149, 157, 211]
  EB-ERR-1@mark-as-found: [211, 212, 213, 214, 216, 217, 220, 221, 222]
  EB-SRC-6@found-at: [47, 48, 50]
anchor: [227]
coverage:
  web: automated
---
# Dialog Mark as Found: field dan default, Asset Status mengubah label dan kewajiban Photo dan Note, info Found outside, validasi, Asset Status terkunci Damaged, dan respons gagal

## Prerequisites
- Aktor: Aktor Missing dengan cakupan Group Manager Head Office; Total Control untuk K9.
- Layar awal: halaman Missing, tab Active.
- Komponen: Dialog Mark as Found (D-MIS-02)
- Data:
  - DU-055-1: Aset `Laptop Dell Latitude 5420 - 22`, Asset ID `LPT-2026-0022`, Brand `Dell`, Group `Finance Room`, Model/Type `Latitude 5420`, status record `Missing`, TAG `RFID`.
  - DU-055-2: Aset `Laptop Lenovo ThinkPad T14 - 4`, Asset ID `LPT-2026-0004`, Brand `Lenovo`, Group `Head Office`, Model/Type `ThinkPad T14`, status record `Missing`, tanpa TAG.
  - DU-055-3: Aset `Monitor LG 27UL500 - 11`, Asset ID `MON-2026-0011`, Brand `LG`, Group `Server Room`, Model/Type `27UL500`, status record `Missing`, tanpa TAG, asal Damaged + Missing.
  - DU-055-4: Pohon Group dalam cakupan Group Manager Head Office: `Head Office` (induk) berisi `Finance Room` dan `Server Room`; `Warehouse` di luar cakupan.
  - DU-055-5: Pohon Group untuk Total Control: `Head Office` (induk) berisi `Finance Room` dan `Server Room`, serta `Warehouse`.
  - DU-055-26: Aset `Printer Epson L3250 - 7`, Asset ID `PRN-2026-0007`, Brand `Epson`, Group `Head Office`, Model/Type `L3250`, status record `Missing`, tanpa TAG, dengan penanda `Long missing`: sudah `34` hari Missing, melewati Long missing after `30`.
- Kondisi:
  - K1: dialog dibuka untuk aset DU-055-1 dengan pohon Group DU-055-4; Scan TAG belum terverifikasi.
  - K2: dialog dibuka untuk aset DU-055-2 dengan pohon Group DU-055-4; simpan berhasil dan aset kembali Available; toast yang diharapkan `Success, Laptop Lenovo ThinkPad T14 is available again.`, dari Asset Name `Laptop Lenovo ThinkPad T14`.
  - K3: dialog dibuka untuk aset DU-055-3 yang berasal dari Damaged + Missing dengan pohon Group DU-055-4; simpan berhasil dan aset kembali Available; toast yang diharapkan `Success, Monitor LG 27UL500 is available again.`, dari Asset Name `Monitor LG 27UL500`.
  - K4: dialog dibuka untuk aset DU-055-2 dengan pohon Group DU-055-4; simpan berhasil dengan Asset Status Damaged; toast yang diharapkan `Success, Laptop Lenovo ThinkPad T14 is available again. A damage report has been created.`, dari Asset Name `Laptop Lenovo ThinkPad T14`.
  - K5: dialog dibuka untuk aset DU-055-2 dengan pohon Group DU-055-4; simpan berhasil tetapi status global aset bukan Available.
  - K6: dialog dibuka untuk aset DU-055-2 dengan pohon Group DU-055-4; simpan pertama gagal karena error server, simpan berikutnya berhasil dengan Asset Status Damaged.
  - K7: dialog dibuka untuk aset DU-055-2 dengan pohon Group DU-055-4; simpan gagal karena timeout.
  - K8: dialog dibuka untuk aset DU-055-2 dengan pohon Group DU-055-4; respons simpan belum diterima sampai langkah menyatakannya.
  - K9: dialog dibuka oleh Total Control untuk aset DU-055-1 dengan pohon Group DU-055-5.
  - K10: dialog dibuka untuk aset DU-055-26 dengan pohon Group DU-055-4.


## Test Steps

### Tampilan awal Mark as Found pada aset ber-TAG
1. Tampilkan Dialog Mark as Found dengan kondisi K1
2. Verifikasi judul dialog `Mark as Found`
3. Verifikasi dialog memuat isian Found at, Asset Status, Photo, dan Note serta tombol `[Cancel]` dan `[Mark as Found]`
4. Verifikasi header menampilkan nama `Laptop Dell Latitude 5420 - 22` dan Asset ID `LPT-2026-0022`
5. Verifikasi header menampilkan badge status record `Missing`
6. Verifikasi isian Scan TAG memuat tombol `[Scan TAG]`
7. Verifikasi isian Scan TAG memuat tautan `I Can't Scan the TAG`
8. Verifikasi Scan TAG bertanda wajib
9. Verifikasi Found at bertanda wajib
10. Verifikasi Found at menampilkan Group aset `Finance Room` sebagai pilihan awal
11. Verifikasi Asset Status menampilkan `Normal`
12. Verifikasi isian Photo berlabel `Photo` dan tidak bertanda wajib
13. Verifikasi isian Photo tidak memiliki helper text
14. Verifikasi placeholder Note `Enter note`
15. Verifikasi Note tidak bertanda wajib
16. Verifikasi info `Found outside its group. Transfer it back if needed.` tidak tampil

### Scan TAG belum terverifikasi saat Submit
17. Tampilkan Dialog Mark as Found dengan kondisi K1
18. Verifikasi `[Mark as Found]` aktif
19. Klik `[Mark as Found]`
20. Verifikasi caption error `Scan TAG must not be empty` tampil di bawah isian Scan TAG
21. Verifikasi isian Scan TAG memiliki `aria-describedby` yang menunjuk ke caption error itu
22. Verifikasi `[Mark as Found]` tetap aktif

### Aset tanpa TAG tidak memuat isian Scan TAG
23. Tampilkan Dialog Mark as Found dengan kondisi K2
24. Verifikasi Found at menampilkan Group aset `Head Office` sebagai pilihan awal meski bukan node terbawah
25. Verifikasi isian Scan TAG tidak tampil

### Found at: pohon Group dalam cakupan aktor dan info Found outside
26. Tampilkan Dialog Mark as Found dengan kondisi K1
27. Klik `Edit selection` pada isian Found at
28. Verifikasi pohon memuat `Head Office`, `Finance Room`, dan `Server Room`
29. Verifikasi `Finance Room` terpilih sebagai pilihan awal pohon
30. Verifikasi `Head Office` tidak dapat dipilih
31. Verifikasi `Warehouse` tidak tampil di pohon
32. Klik `Server Room`
33. Klik `[Select]` pada dialog pohon Group
34. Verifikasi Found at menampilkan `Server Room`
35. Verifikasi info `Found outside its group. Transfer it back if needed.` tampil
36. Klik `Edit selection` pada isian Found at
37. Klik `Finance Room`
38. Klik `[Select]` pada dialog pohon Group
39. Verifikasi Found at menampilkan `Finance Room`
40. Verifikasi info `Found outside its group. Transfer it back if needed.` tidak tampil

### Found at: pohon untuk Total Control memuat seluruh Group
41. Tampilkan Dialog Mark as Found dengan kondisi K9
42. Klik `Edit selection` pada isian Found at
43. Verifikasi pohon memuat `Warehouse`

### Found at: pencarian pohon
44. Tampilkan Dialog Mark as Found dengan kondisi K1
45. Klik `Edit selection` pada isian Found at
46. Ketik `Server` pada kotak `Search` dialog pohon Group
47. Verifikasi pohon menampilkan `Server Room` beserta induknya `Head Office`[^drift-1]
48. Verifikasi `Finance Room` tidak tampil di pohon[^drift-1]
49. Tekan Enter
50. Verifikasi pohon tetap menampilkan `Server Room` dan tidak menampilkan `Finance Room`[^drift-1]

### Found at kosong ditolak saat Submit
51. Tampilkan Dialog Mark as Found dengan kondisi K2
52. Klik `Edit selection` pada isian Found at
53. Klik `Head Office`
54. Klik `[Select]` pada dialog pohon Group
55. Verifikasi isian Found at menampilkan placeholder `Select group`
56. Klik `[Mark as Found]`
57. Verifikasi caption error `Found at must not be empty` tampil di bawah isian Found at
58. Verifikasi `[Mark as Found]` tetap aktif

### Asset Status Damaged mengubah label dan kewajiban Photo dan Note
59. Tampilkan Dialog Mark as Found dengan kondisi K2
60. Klik isian Asset Status
61. Verifikasi opsi `Normal` dan `Damaged` tampil
62. Klik opsi `Damaged`
63. Verifikasi isian Photo berlabel `Damaged Photo`
64. Verifikasi `Damaged Photo` bertanda wajib
65. Verifikasi placeholder Note `Enter damage description`
66. Verifikasi Note bertanda wajib

### Ganti Asset Status setelah isian terisi
67. Tampilkan Dialog Mark as Found dengan kondisi K2
68. Klik isian Asset Status
69. Klik opsi `Damaged`
70. Isi Note `Layar retak di sudut kiri atas`
71. Klik isian Asset Status
72. Klik opsi `Normal`
73. Verifikasi isian Photo kembali berlabel `Photo` dan tidak bertanda wajib
74. Verifikasi placeholder Note kembali `Enter note`

### Damaged: Note dan Damaged Photo kosong ditolak
75. Tampilkan Dialog Mark as Found dengan kondisi K2
76. Klik isian Asset Status
77. Klik opsi `Damaged`
78. Klik `[Mark as Found]`
79. Verifikasi caption error `Note must not be empty` tampil di bawah isian Note
80. Verifikasi caption error `Damaged photo must not be empty` tampil di bawah isian Damaged Photo
81. Verifikasi isian Note memiliki `aria-describedby` yang menunjuk ke caption error itu
82. Isi Note `   `
83. Klik `[Mark as Found]`
84. Verifikasi caption error `Note must not be empty` tampil di bawah isian Note

### Batas panjang Note
85. Tampilkan Dialog Mark as Found dengan kondisi K2
86. Klik isian Asset Status
87. Klik opsi `Damaged`
88. Isi Note `Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke raZ` (361 karakter)
89. Verifikasi caption error `Max. 360 characters` tampil langsung saat teks melebihi batas
90. Ganti isi Note dengan `Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke ra` (360 karakter)
91. Verifikasi caption error `Max. 360 characters` tidak tampil
92. Ganti isi Note dengan `Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum dipindahkan ke lantai tiga bangunan baru. Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum dipindahkan ke lantai tiga bangunan baru. Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum.` (360 karakter)
93. Verifikasi caption error `Max. 360 characters` tidak tampil
94. Ganti isi Note dengan `Aset belum kembali ke rak  penyimpanan sejak inventarisasi akhir bulan  dan tidak ada catatan peminjaman  terbaru.  Aset belum kembali  ke rak penyimpanan sejak inventarisasi  akhir bulan dan tidak ada  catatan peminjaman terbaru.  Aset  belum kembali ke rak penyimpanan  sejak inventarisasi akhir bulan dan  tidak ada catatan peminjaman terbaru.   Aset belum.` (360 karakter)
95. Verifikasi caption error `Max. 360 characters` tidak tampil
96. Ganti isi Note dengan `  Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke ra  `, yaitu teks batas maksimum yang diapit dua spasi di awal dan di akhir
97. Verifikasi caption error `Max. 360 characters` tidak tampil
98. Ganti isi Note dengan `H`
99. Verifikasi isian Note berisi `H`

### Format foto PNG, JPG, dan JPEG diterima tanpa pesan
100. Tampilkan Dialog Mark as Found dengan kondisi K2
101. Klik isian Asset Status
102. Klik opsi `Damaged`
103. Pilih berkas `kerusakan-unit.png` pada isian Damaged Photo
104. Verifikasi dialog `Adjust photo` tampil untuk berkas `kerusakan-unit.png`
105. Klik `Apply`
106. Verifikasi thumbnail Damaged Photo tampil
107. Klik `Delete` pada thumbnail Damaged Photo
108. Pilih berkas `kerusakan-unit.jpg` pada isian Damaged Photo
109. Verifikasi dialog `Adjust photo` tampil untuk berkas `kerusakan-unit.jpg`
110. Verifikasi tidak ada pesan kesalahan format atau ukuran pada isian Damaged Photo
111. Klik `Apply`
112. Verifikasi thumbnail Damaged Photo tampil
113. Klik `Delete` pada thumbnail Damaged Photo
114. Pilih berkas `kerusakan-unit.jpeg` pada isian Damaged Photo
115. Verifikasi dialog `Adjust photo` tampil untuk berkas `kerusakan-unit.jpeg`
116. Klik `Apply`
117. Verifikasi thumbnail Damaged Photo tampil
118. Klik `Delete` pada thumbnail Damaged Photo
119. Pilih berkas `kerusakan-besar.jpg` berukuran 3 MB pada isian Damaged Photo
120. Verifikasi dialog `Adjust photo` tampil untuk berkas `kerusakan-besar.jpg`
121. Verifikasi tidak ada pesan kesalahan ukuran pada isian Damaged Photo

### Damaged Photo valid tidak menutupi kesalahan field lain
122. Tampilkan Dialog Mark as Found dengan kondisi K2
123. Klik isian Asset Status
124. Klik opsi `Damaged`
125. Pilih berkas `kerusakan-unit.jpg` pada isian Damaged Photo
126. Klik `Apply`
127. Klik `[Mark as Found]`
128. Verifikasi caption error `Note must not be empty` tampil di bawah isian Note
129. Verifikasi thumbnail Damaged Photo tetap tampil
130. Verifikasi caption error `Damaged photo must not be empty` tidak tampil

### Berkas terunggah lalu form ditutup
131. Tampilkan Dialog Mark as Found dengan kondisi K2
132. Klik isian Asset Status
133. Klik opsi `Damaged`
134. Pilih berkas `kerusakan-unit.png` pada isian Damaged Photo
135. Klik `Apply`
136. Klik `✕` pada dialog
137. Verifikasi dialog `Unsaved Changes` tampil di atas dialog Mark as Found dengan teks `You have unsaved changes. Are you sure you want to leave?`
138. Klik `[Leave]`
139. Verifikasi dialog Mark as Found tertutup

### Asset Status terkunci Damaged pada asal Damaged + Missing
140. Tampilkan Dialog Mark as Found dengan kondisi K3
141. Verifikasi Asset Status terisi `Damaged`
142. Verifikasi Asset Status tidak dapat diubah
143. Verifikasi isian Photo berlabel `Damaged Photo`
144. Verifikasi placeholder Note `Enter damage description`

### Simpan berhasil: aset kembali Available
145. Tampilkan Dialog Mark as Found dengan kondisi K2
146. Verifikasi `[Mark as Found]` aktif
147. Klik `[Mark as Found]`
148. Verifikasi toast `Success, Laptop Lenovo ThinkPad T14 is available again.` tampil
149. Verifikasi dialog Mark as Found tertutup

### Simpan berhasil dengan Asset Status Damaged
150. Tampilkan Dialog Mark as Found dengan kondisi K4
151. Klik isian Asset Status
152. Klik opsi `Damaged`
153. Isi Note `Layar retak di sudut kiri atas`
154. Pilih berkas `kerusakan-unit.jpg` pada isian Damaged Photo
155. Klik `Apply`
156. Klik `[Mark as Found]`
157. Verifikasi toast `Success, Laptop Lenovo ThinkPad T14 is available again. A damage report has been created.` tampil

### Simpan berhasil pada asal Damaged + Missing
158. Tampilkan Dialog Mark as Found dengan kondisi K3
159. Isi Note `Layar retak di sudut kiri atas`
160. Pilih berkas `kerusakan-unit.jpg` pada isian Damaged Photo
161. Klik `Apply`
162. Klik `[Mark as Found]`
163. Verifikasi toast `Success, Monitor LG 27UL500 is available again.` tampil

### Simpan berhasil tetapi status aset bukan Available
164. Tampilkan Dialog Mark as Found dengan kondisi K5
165. Klik `[Mark as Found]`
166. Verifikasi toast `Success, asset has been marked as found.` tampil

### Note dan Photo opsional pada Normal
167. Tampilkan Dialog Mark as Found dengan kondisi K2
168. Verifikasi isian Asset Status menampilkan `Normal` tanpa disentuh
169. Klik `[Mark as Found]`
170. Verifikasi toast `Success, Laptop Lenovo ThinkPad T14 is available again.` tampil tanpa isian Note maupun Photo

### Simpan lambat: tombol dan kontrol terkunci
171. Tampilkan Dialog Mark as Found dengan kondisi K8
172. Klik `[Mark as Found]`
173. Verifikasi `[Mark as Found]` tidak bisa diklik selama simpan berjalan
174. Verifikasi isian Found at, Asset Status, Photo, Note, `[Cancel]`, dan `✕` tidak bisa dipakai selama simpan berjalan
175. Klik `[Mark as Found]`
176. Respons simpan diterima
177. Verifikasi hanya satu toast `Success, Laptop Lenovo ThinkPad T14 is available again.` tampil

### Form bersih ditutup dengan tombol silang
178. Tampilkan Dialog Mark as Found dengan kondisi K2
179. Klik `✕` pada dialog
180. Verifikasi dialog Mark as Found tertutup tanpa dialog Unsaved Changes

### Form bersih ditutup dengan Esc
181. Tampilkan Dialog Mark as Found dengan kondisi K2
182. Tekan Esc
183. Verifikasi dialog Mark as Found tertutup tanpa dialog Unsaved Changes

### Form kotor ditutup memunculkan Unsaved Changes
184. Tampilkan Dialog Mark as Found dengan kondisi K2
185. Isi Note `Layar retak di sudut kiri atas`
186. Klik area backdrop di luar dialog
187. Verifikasi dialog Mark as Found tetap terbuka dengan isian Note `Layar retak di sudut kiri atas`
188. Klik `✕` pada dialog
189. Verifikasi dialog `Unsaved Changes` tampil di atas dialog Mark as Found dengan teks `You have unsaved changes. Are you sure you want to leave?`
190. Verifikasi dialog Unsaved Changes pada dialog Mark as Found memuat tombol `[Leave]` dan `[Cancel]`
191. Tekan Esc
192. Verifikasi dialog Unsaved Changes tertutup dan dialog Mark as Found tetap terbuka dengan isian Note `Layar retak di sudut kiri atas`
193. Tekan Esc
194. Klik `[Leave]`
195. Verifikasi dialog Mark as Found tertutup

### Aksesibilitas dialog
196. Tampilkan Dialog Mark as Found dengan kondisi K1
197. Verifikasi fokus berada di dalam dialog Mark as Found
198. Verifikasi isian Found at memiliki `aria-required`
199. Verifikasi tombol `✕` pada dialog Mark as Found memiliki label aksesibel `Close dialog`
200. Tekan Tab dua puluh kali berturut-turut
201. Verifikasi fokus tetap berada di dalam dialog Mark as Found
202. Klik `✕` pada dialog
203. Verifikasi fokus kembali ke elemen pemicu dialog Mark as Found

### Simpan gagal karena error server: isian dipertahankan dan submit ulang berhasil
204. Tampilkan Dialog Mark as Found dengan kondisi K6
205. Klik isian Asset Status
206. Klik opsi `Damaged`
207. Isi Note `Layar retak di sudut kiri atas`
208. Pilih berkas `kerusakan-unit.jpg` pada isian Damaged Photo
209. Klik `Apply`
210. Klik `[Mark as Found]`
211. Verifikasi toast `Error, failed to mark asset as found.` tampil
212. Verifikasi dialog Mark as Found tetap terbuka
213. Verifikasi isian Note tetap berisi `Layar retak di sudut kiri atas`
214. Verifikasi `[Mark as Found]` aktif lagi
215. Klik `[Mark as Found]`
216. Verifikasi toast `Success, Laptop Lenovo ThinkPad T14 is available again. A damage report has been created.` tampil
217. Verifikasi dialog Mark as Found tertutup

### Simpan gagal karena timeout
218. Tampilkan Dialog Mark as Found dengan kondisi K7
219. Klik `[Mark as Found]`
220. Verifikasi toast `Connection problem. Please try again.` tampil setelah simpan Mark as Found
221. Verifikasi dialog Mark as Found tetap terbuka
222. Verifikasi `[Mark as Found]` aktif lagi

### Format di luar PNG, JPG, dan JPEG tidak diterima picker
223. Tampilkan Dialog Mark as Found dengan kondisi K2
224. Klik isian Asset Status
225. Klik opsi `Damaged`
226. Pilih berkas `kerusakan-unit.png` pada isian Damaged Photo
227. Verifikasi dialog `Adjust photo` tampil untuk berkas `kerusakan-unit.png`
228. Klik `Cancel` pada dialog `Adjust photo`
229. Pilih berkas `dokumen-kerusakan.pdf` pada isian Damaged Photo
230. Verifikasi dialog `Adjust photo` tidak tampil
231. Verifikasi thumbnail Damaged Photo tidak tampil
232. Verifikasi tidak ada pesan kesalahan format pada isian Damaged Photo
233. Pilih berkas `kerusakan-unit.gif` pada isian Damaged Photo
234. Verifikasi dialog `Adjust photo` tidak tampil

### Scan TAG bertanda aria-required
235. Tampilkan Dialog Mark as Found dengan kondisi K1
236. Verifikasi isian Scan TAG memiliki `aria-required`

### Damaged Photo dan Note: aria-required dan aria-describedby
237. Tampilkan Dialog Mark as Found dengan kondisi K2
238. Klik isian Asset Status
239. Klik opsi `Damaged`
240. Verifikasi isian Note memiliki `aria-required`
241. Verifikasi isian Damaged Photo memiliki `aria-required`
242. Klik `[Mark as Found]`
243. Verifikasi caption error `Damaged photo must not be empty` tampil di bawah isian Damaged Photo
244. Verifikasi isian Damaged Photo memiliki `aria-describedby` yang menunjuk ke caption error itu

### Found at kosong: aria-describedby
245. Tampilkan Dialog Mark as Found dengan kondisi K2
246. Klik `Edit selection` pada isian Found at
247. Klik `Head Office`
248. Klik `[Select]` pada dialog pohon Group
249. Klik `[Mark as Found]`
250. Verifikasi caption error `Found at must not be empty` tampil di bawah isian Found at
251. Verifikasi isian Found at memiliki `aria-describedby` yang menunjuk ke caption error itu

### Header record dengan penanda Long missing
252. Tampilkan Dialog Mark as Found dengan kondisi K10
253. Verifikasi header menampilkan badge status record `Missing`
254. Verifikasi header menampilkan penanda `Long missing`

[^drift-1]: Drift foundation vs kontrak komponen. PRD §4.2.4 tidak menyatakan kapan pencarian pohon Found at berjalan; foundation `prd-conventions.md` §31.3: «Pencarian pada `TreeSearchInput` berjalan saat Enter ditekan» (ekspektasi baku EB-SRC-6: «Pencarian tree berjalan saat Enter, bukan real-time»); kontrak `TreeSelect#9`: «a text field above the tree filters nodes by label ... Enter does nothing». Diasersi: kontrak, sehingga pohon tersaring saat teks diketik dan Enter tidak mengubah hasil (SB-7).

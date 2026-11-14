---
id: TC-FA-DAMAGED-UI-102-tabel-active-mekanik-toolbar
title: "Mekanik toolbar sub-tab Active: siklus kotak Search, indikator sort, Setup Column, Filter Panel, paginasi, dan popover Download gagal"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, "§5#r8", "§9.5#r4", EB-SRC-4@tabel-active, EB-SRC-6@filter-group, EB-SRC-6@filter-category, EB-SRT-3@tabel-active, EB-KOL-1@tabel-active, EB-FLT-2@tabel-active, EB-FLT-6@tabel-active, EB-TBL-7@tabel-active, EB-DL-2@tabel-active, EB-DL-5]
smoke: []
dependsOn: []
trace:
  T-DMG-01: [32, 98, 99, 100, 101, 102, 103, 104, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225]
  "§5#r8": [36, 93, 94]
  "§9.5#r4": [179, 180, 182]
  EB-SRC-4@tabel-active: [3, 5, 7, 8, 10, 11, 12, 14, 16, 17, 19, 20]
  EB-SRC-6@filter-group: [161, 163, 165, 166, 168]
  EB-SRC-6@filter-category: [172, 174, 176, 177]
  EB-SRT-3@tabel-active: [23, 25, 27, 30, 31, 32]
  EB-KOL-1@tabel-active: [35, 37, 39, 40, 42, 44, 47, 49, 53, 54, 55, 56, 58, 59, 61, 67, 68, 69, 74, 75, 77, 79, 86, 88, 90, 230, 232, 236, 238]
  EB-FLT-2@tabel-active: [97, 109, 111, 116, 118, 119, 121, 122, 123, 125, 134, 135, 137, 138, 142, 144, 149, 153, 157]
  EB-FLT-6@tabel-active: [128, 129, 130, 132]
  EB-TBL-7@tabel-active: [184, 186, 189, 191, 193, 195]
  EB-DL-2@tabel-active: [198, 199, 201]
  EB-DL-5: [205, 206]
anchor: []
coverage:
  web: automated
---

# Mekanik toolbar sub-tab Active: siklus kotak Search, indikator sort, Setup Column, Filter Panel, paginasi, dan popover Download gagal

## Prerequisites
- Aktor: Group Manager (hak lihat nilai finansial menurut Kondisi).
- Layar awal: halaman Assets, tab `Damaged`, sub-tab `Active`.
- Komponen: Tabel T-DMG-01 (sub-tab Active)
- Data:
  - DU-102-1: Record `Printer HP LaserJet M404 - 8`, Asset ID `PRN-2026-0008`, Group `Head Office`, Status `Reported Disposal`, Source `Stock opname`, Reported By `Agus Prasetyo`.
  - DU-102-2: Record `Monitor Dell P2422H - 6`, Asset ID `MON-2026-0006`, Group `Warehouse`, Status `In Disposal Process`, Source `Manual`, Reported By `Rina Wijaya`.
  - DU-102-3: Record `Camera Canon EOS - 3`, Asset ID `CAM-2026-0003`, Group `Branch Surabaya`, Status `Damaged`, Source `Manual`, Reported By `Agus Prasetyo`.
  - DU-102-4: Sebelas nilai Source pada data tabel: `Manual`, `Reported by scan`, `Reported by holder`, `Borrowed asset`, `Borrow return`, `Assigned asset`, `Assign return`, `Stock opname`, `Transfer receive`, `Missing asset`, `Registration`.
  - DU-102-5: Pohon Group dengan node `Head Office`, `Warehouse`, dan `Branch Surabaya`.
  - DU-102-6: Pohon Category dengan node `Electronics`, `Furniture`, dan `Vehicle`.
  - DU-102-7: 25 record `Office Desk Standard - {n}` (n = 1 sampai 25), Asset ID `DSK-2026-{n}`, Group `Head Office`, Status `Damaged`, Source `Manual`.
  - DU-102-8: Hasil unduhan sebanyak `5.001` baris.
- Kondisi:
  - K1: daftar memuat DU-102-1 sampai DU-102-3 dengan kolom bawaan Setup Column; pohon filter Group dan Category memuat DU-102-5 dan DU-102-6; aktor berhak melihat nilai finansial; jawaban daftar mengikuti Search, saringan, urutan, dan halaman yang dikirim tabel.
  - K2: daftar seperti K1, dengan Setup Column hanya menampilkan kolom `Name`.
  - K3: daftar seperti K1, dengan opsi filter `Source` memuat sebelas nilai pada DU-102-4.
  - K4: daftar kosong, sehingga sumber opsi filter tidak memuat nilai.
  - K5: daftar memuat 25 record pada DU-102-7 dengan ukuran halaman bawaan.
  - K6: daftar seperti K1; unduhan gagal karena error server.
  - K7: daftar seperti K1; jumlah baris hasil unduhan sesuai DU-102-8.
  - K8: daftar seperti K1; aktor tidak berhak melihat nilai finansial.

## Test Steps

### Siklus kotak Search
1. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
2. Klik ikon Search
3. Verifikasi kotak input Search tampil dan fokus berada di input
4. Ketik `Camera` pada kotak Search
5. Verifikasi baris `Printer HP LaserJet M404 - 8`, `Monitor Dell P2422H - 6`, dan `Camera Canon EOS - 3` tetap tampil sebelum Enter ditekan
6. Tekan Enter
7. Verifikasi baris `Camera Canon EOS - 3` tampil
8. Verifikasi baris `Printer HP LaserJet M404 - 8` tidak tampil
9. Klik `✕` pada kotak Search
10. Verifikasi kotak Search kosong
11. Verifikasi baris `Camera Canon EOS - 3` tetap tampil
12. Verifikasi baris `Printer HP LaserJet M404 - 8` tetap tidak tampil
13. Tekan Enter
14. Verifikasi baris `Printer HP LaserJet M404 - 8` tampil kembali
15. Ketik Search `Monitor`, tekan Enter
16. Verifikasi baris `Monitor Dell P2422H - 6` tampil
17. Verifikasi baris `Camera Canon EOS - 3` tidak tampil
18. Klik `(←)` pada kotak Search
19. Verifikasi kotak input Search tertutup
20. Verifikasi baris `Camera Canon EOS - 3` tampil kembali

### Siklus tiga klik indikator sort
21. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
22. Klik header kolom `Name`
23. Verifikasi indikator `↑` aktif pada header kolom `Name`
24. Klik header kolom `Name`
25. Verifikasi indikator `↓` aktif pada header kolom `Name`
26. Klik header kolom `Name`
27. Verifikasi indikator sort pada header kolom `Name` tidak aktif
28. Klik header kolom `Name`
29. Klik header kolom `Asset ID`
30. Verifikasi indikator `↑` aktif pada header kolom `Asset ID`
31. Verifikasi indikator sort pada header kolom `Name` tidak aktif
32. Verifikasi header kolom `Photo` tidak memiliki ikon sort

### Setup Column panel cepat berlaku langsung
33. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
34. Klik header kolom Actions (`⋯`)
35. Verifikasi daftar kolom dengan checkbox tampil dan memuat `Name`, `Asset ID`, dan `Source`
36. Verifikasi daftar kolom memuat `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
37. Verifikasi item `Setup Column...` tampil di bagian bawah panel
38. Hapus centang `Source` pada daftar kolom
39. Verifikasi header kolom `Name` tampil
40. Verifikasi header kolom `Source` tidak dirender tanpa langkah penyimpanan
41. Centang `Source` pada daftar kolom
42. Verifikasi header kolom `Source` tampil
43. Seret `Source` ke atas `Status` pada daftar kolom
44. Verifikasi header kolom `Source` tampil sebelum header kolom `Status`

### Kolom terakhir yang tampil tidak bisa disembunyikan
45. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K2
46. Klik header kolom Actions (`⋯`)
47. Verifikasi checkbox `Name` pada daftar kolom Disabled
48. Arahkan pointer ke checkbox `Name` pada daftar kolom
49. Verifikasi alasan `At least one column must remain visible.` tersampaikan pada checkbox yang Disabled

### Dialog Setup Column: anatomi, perubahan sementara tampak di tabel, dan dibuang saat ditutup
50. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
51. Klik header kolom Actions (`⋯`)
52. Klik `Setup Column...`
53. Verifikasi judul dialog `Setup Column` tampil
54. Verifikasi deskripsi `Drag and drop to rearrange the order and click the pin to freeze up to 3 columns.` tampil
55. Verifikasi tombol `[Reset to Default]` dan `[Save]` tampil
56. Verifikasi tombol `[Cancel]` tidak tampil
57. Hapus centang `Asset ID` pada dialog `Setup Column`
58. Verifikasi header kolom `Asset ID` tidak dirender pada tabel di balik dialog `Setup Column`
59. Verifikasi header kolom `Name` tetap tampil pada tabel di balik dialog `Setup Column`
60. Klik `[✕]` pada dialog `Setup Column`
61. Verifikasi header kolom `Asset ID` tampil pada tabel

### Dialog Setup Column: Save menyimpan perubahan
62. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
63. Klik header kolom Actions (`⋯`)
64. Klik `Setup Column...`
65. Hapus centang `Asset ID` pada dialog `Setup Column`
66. Klik `[Save]`
67. Verifikasi dialog `Setup Column` tertutup
68. Verifikasi header kolom `Name` tampil
69. Verifikasi header kolom `Asset ID` tidak dirender

### Reset to Default mengembalikan konfigurasi bawaan modul
70. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
71. Klik header kolom Actions (`⋯`)
72. Hapus centang `Source` pada daftar kolom
73. Klik `Setup Column...`
74. Verifikasi header kolom `Name` tampil pada tabel di balik dialog `Setup Column`
75. Verifikasi header kolom `Source` tidak dirender pada tabel di balik dialog `Setup Column`
76. Klik `[Reset to Default]`
77. Verifikasi header kolom `Source` tampil pada tabel di balik dialog `Setup Column`
78. Klik `[Save]`
79. Verifikasi header kolom `Source` tampil pada tabel

### Pin kolom dibatasi tiga
80. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
81. Klik header kolom Actions (`⋯`)
82. Klik `Setup Column...`
83. Klik ikon pin kolom `Name`
84. Klik ikon pin kolom `Asset ID`
85. Klik ikon pin kolom `Group`
86. Verifikasi ikon pin kolom `Status` Disabled
87. Arahkan pointer ke ikon pin kolom `Status`
88. Verifikasi alasan `Maximum 3 columns can be pinned at once. Unpin another column first.` tersampaikan pada ikon pin yang Disabled
89. Klik ikon pin kolom `Group`
90. Verifikasi ikon pin kolom `Status` aktif

### Kolom nilai finansial tidak ada di Setup Column bagi aktor tanpa hak
91. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K8
92. Klik header kolom Actions (`⋯`)
93. Verifikasi daftar kolom memuat `Name`
94. Verifikasi daftar kolom tidak memuat `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`

### Field Filter Panel mengikuti konfigurasi kolom
95. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
96. Klik ikon Filter
97. Verifikasi Filter Panel tampil
98. Verifikasi field `Asset Name` tampil dengan placeholder `All asset names`
99. Verifikasi field `Group` tampil dengan placeholder `All groups`
100. Verifikasi field `Status` tampil dengan placeholder `All statuses`
101. Verifikasi field `Source` tampil dengan placeholder `All sources`
102. Verifikasi field `Reported By` tampil dengan placeholder `All users`
103. Verifikasi field `Reported Date` tampil dengan placeholder `Select date`
104. Verifikasi field `Days Damaged` tampil dengan dua input berplaceholder `Min` dan `Max`

### Draft filter dibuang saat panel ditutup tanpa Apply
105. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
106. Klik ikon Filter
107. Pilih opsi `Damaged` pada field `Status`
108. Klik ikon Filter
109. Verifikasi baris `Printer HP LaserJet M404 - 8`, `Monitor Dell P2422H - 6`, dan `Camera Canon EOS - 3` tetap tampil pada tabel
110. Klik ikon Filter
111. Verifikasi field `Status` menampilkan placeholder `All statuses` tanpa opsi terpilih

### Chip opsi, Apply, indikator aktif, dan kolom disembunyikan
112. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
113. Klik ikon Filter
114. Pilih opsi `Damaged` pada field `Status`
115. Pilih opsi `Reported Disposal` pada field `Status`
116. Verifikasi chip `Damaged` dan chip `Reported Disposal` tampil pada field `Status`
117. Klik `✕` pada chip `Damaged`
118. Verifikasi chip `Reported Disposal` tetap tampil pada field `Status`
119. Verifikasi opsi `Damaged` tidak tercentang pada daftar opsi field `Status`
120. Klik `[Apply]`
121. Verifikasi baris `Printer HP LaserJet M404 - 8` tampil
122. Verifikasi baris `Camera Canon EOS - 3` tidak tampil
123. Verifikasi badge titik tampil pada ikon Filter
124. Klik ikon Filter
125. Verifikasi badge titik tetap tampil pada ikon Filter
126. Klik header kolom Actions (`⋯`)
127. Hapus centang `Status` pada daftar kolom
128. Verifikasi header kolom `Status` tidak dirender
129. Verifikasi baris `Printer HP LaserJet M404 - 8` tetap tampil
130. Verifikasi baris `Camera Canon EOS - 3` tetap tidak tampil
131. Klik ikon Filter
132. Verifikasi field `Status` tetap ada pada Filter Panel dan memuat chip `Reported Disposal`
133. Klik `[Clear Field]`
134. Verifikasi baris `Printer HP LaserJet M404 - 8` tetap tampil sebelum `[Apply]`
135. Verifikasi baris `Camera Canon EOS - 3` masih tidak tampil sebelum `[Apply]`
136. Klik `[Apply]`
137. Verifikasi baris `Camera Canon EOS - 3` tampil
138. Verifikasi badge titik tidak tampil pada ikon Filter

### Opsi dihapus centangnya dari daftar menghapus chip
139. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
140. Klik ikon Filter
141. Pilih opsi `Damaged` pada field `Status`
142. Verifikasi chip `Damaged` tampil pada field `Status`
143. Hapus centang opsi `Damaged` pada daftar opsi field `Status`
144. Verifikasi chip `Damaged` tidak tampil pada field `Status`

### Search di dalam dropdown filter tanpa hasil
145. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
146. Klik ikon Filter
147. Klik field `Status`
148. Ketik `zzz` pada kotak cari di dalam dropdown `Status`
149. Verifikasi teks `No results found` tampil di dalam dropdown `Status`

### Sumber opsi filter kosong
150. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K4
151. Klik ikon Filter
152. Klik field `Status`
153. Verifikasi teks `No options available` tampil di dalam dropdown `Status`

### Chip opsi melimpah diringkas
154. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K3
155. Klik ikon Filter
156. Pilih satu per satu seluruh sebelas opsi pada field `Source`
157. Verifikasi ringkasan `+N more` tampil pada field `Source` dan field tidak melebar keluar Filter Panel

### Pencarian tree Group berjalan saat Enter
158. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
159. Klik ikon Filter
160. Klik field `Group`
161. Verifikasi tree memuat `Head Office`, `Warehouse`, dan `Branch Surabaya`
162. Ketik `Branch` pada pencarian tree
163. Verifikasi tree masih memuat `Warehouse` sebelum Enter ditekan
164. Tekan Enter
165. Verifikasi tree memuat `Branch Surabaya`
166. Verifikasi tree tidak memuat `Warehouse`
167. Kosongkan pencarian tree, tekan Enter
168. Verifikasi tree memuat `Head Office`, `Warehouse`, dan `Branch Surabaya`

### Pencarian tree Category berjalan saat Enter
169. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
170. Klik ikon Filter
171. Klik field `Category`
172. Verifikasi tree memuat `Electronics`, `Furniture`, dan `Vehicle`
173. Ketik `Furn` pada pencarian tree
174. Verifikasi tree masih memuat `Vehicle` sebelum Enter ditekan
175. Tekan Enter
176. Verifikasi tree memuat `Furniture`
177. Verifikasi tree tidak memuat `Vehicle`

### Paginasi bawaan dan perubahan ukuran halaman
178. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K5
179. Verifikasi laporan `Showing 1 to 10 of 25` tampil
180. Verifikasi pilihan ukuran halaman `10`, `25`, `50`, dan `100` tersedia
181. Klik tombol halaman `2`
182. Verifikasi laporan `Showing 11 to 20 of 25` tampil
183. Klik header kolom `Name`
184. Verifikasi laporan `Showing 11 to 20 of 25` tetap tampil sesudah urutan berganti
185. Pilih ukuran halaman `25`
186. Verifikasi laporan `Showing 1 to 25 of 25` tampil

### Nomor halaman tidak valid
187. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K5
188. Ketik `0` pada input nomor halaman, tekan Enter
189. Verifikasi laporan `Showing 1 to 10 of 25` tetap tampil
190. Ketik `-1` pada input nomor halaman, tekan Enter
191. Verifikasi laporan `Showing 1 to 10 of 25` tetap tampil
192. Ketik `abc` pada input nomor halaman
193. Verifikasi input nomor halaman tidak menerima huruf
194. Ketik `4` pada input nomor halaman, tekan Enter
195. Verifikasi laporan `Showing 21 to 25 of 25` tampil[^drift-1]

### Download gagal menampilkan toast error
196. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K6
197. Klik ikon Download
198. Verifikasi pilihan `Download as CSV` tampil
199. Verifikasi pilihan `Download as XLSX` tampil
200. Klik `Download as CSV`
201. Verifikasi toast `Error, failed to download Damaged-Active.` tampil

### Download di atas ambang memakai layar pemuatan
202. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K7
203. Klik ikon Download
204. Klik `Download as CSV`
205. Verifikasi layar pemuatan `Downloading...` tampil sampai berkas siap
206. Verifikasi tidak ada toast informasional maupun notifikasi tentang proses unduhan

### Field Filter Panel untuk kolom lain, termasuk kolom yang tersembunyi
207. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
208. Klik ikon Filter
209. Verifikasi field `Brand` tampil dengan placeholder `All brands`
210. Verifikasi field `Model/Type` tampil dengan placeholder `All models`
211. Verifikasi field `TAG` tampil dengan placeholder `All TAGs`
212. Verifikasi field `Category` tampil dengan placeholder `All categories`
213. Verifikasi field `Last Holder` tampil dengan placeholder `All holders`
214. Verifikasi field `Measurement` tampil dengan placeholder `All units`
215. Verifikasi field `Division` tampil dengan placeholder `All divisions`
216. Verifikasi field `Label` tampil dengan placeholder `All labels`
217. Verifikasi field `Asset Class` tampil dengan placeholder `All asset classes`
218. Verifikasi field `Modified By` tampil dengan placeholder `All users`
219. Verifikasi field `Register Date` tampil dengan placeholder `Select date`
220. Verifikasi field `Purchase Date` tampil dengan placeholder `Select date`
221. Verifikasi field `Warranty Expiry` tampil dengan placeholder `Select date`
222. Verifikasi field `Last Updated` tampil dengan placeholder `Select date`
223. Verifikasi field `Purchase Cost` tampil dengan dua input berplaceholder `Min` dan `Max`
224. Verifikasi field `Asset Value (Commercial)` tampil dengan dua input berplaceholder `Min` dan `Max`
225. Verifikasi field `Asset Value (Fiscal)` tampil dengan dua input berplaceholder `Min` dan `Max`

### Dialog Setup Column: seret mengubah urutan kolom
226. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
227. Klik header kolom Actions (`⋯`)
228. Klik `Setup Column...`
229. Seret `Source` ke atas `Status` pada dialog `Setup Column`
230. Verifikasi header kolom `Source` tampil sebelum header kolom `Status` pada tabel di balik dialog `Setup Column`
231. Klik `[Save]`
232. Verifikasi header kolom `Source` tampil sebelum header kolom `Status`

### Dialog Setup Column: kolom terakhir yang tampil tidak bisa disembunyikan
233. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K2
234. Klik header kolom Actions (`⋯`)
235. Klik `Setup Column...`
236. Verifikasi checkbox `Name` pada dialog `Setup Column` Disabled
237. Arahkan pointer ke checkbox `Name` pada dialog `Setup Column`
238. Verifikasi alasan `At least one column must remain visible.` tersampaikan pada checkbox yang Disabled

[^drift-1]: Drift foundation vs kontrak komponen. PRD §9.5: `Pagination | Mengikuti prd-conventions.md §9.11, tanpa delta`; foundation `prd-conventions.md` §9.18: `input diabaikan dan tabel tetap di halaman sekarang`. Kontrak `Paginator#9`: `a page past the last goes to the last page`. Diasersi: kontrak (SB-7), sehingga nomor halaman melebihi halaman terakhir membuka halaman terakhir.

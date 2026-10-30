---
id: TC-GS-USER-E2E-118-subtab-borrowed-assets-setup-column-overlay-popup-hide-reorder-pin-reset
title: "Sub-tab Borrowed Assets: Setup Column (overlay, popup, hide, reorder, pin, reset, guard)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-739
  - TC-GS-USER-740
  - TC-GS-USER-741
  - TC-GS-USER-742
  - TC-GS-USER-743
  - TC-GS-USER-744
  - TC-GS-USER-745
  - TC-GS-USER-746
  - TC-GS-USER-747
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: Setup Column (overlay, popup, hide, reorder, pin, reset, guard)

## Prerequisites

- Mode: FE+BE. Spec hanya membaca data user; tidak ada data user yang diubah.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun: Total Control, Siti Nurhaliza, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > User List dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): `Joko Susilo` (No. 19; Access Fixed Asset + Supply Asset) sebagai pemilik tabel Borrowed Assets; `Andi Wijaya` (No. 10) sebagai PIC seed. Client FAMS aktif. `Joko Susilo` sudah punya borrowed asset Pre-setup (`B0` baris) yang tidak diubah dan ikut tampil.
- Data Dinamis (seeding FAMS atas `Joko Susilo`, 11 baris aset pinjaman supaya tabel lebih dari satu halaman; Verifikasi spec ini hanya menyangkut kolom tabel dan tidak bergantung pada nilai baris): Name `Laptop 1 {runId}-118` sampai `Laptop 11 {runId}-118`; Brand `Lenovo {runId}-118`; Model / Type `ThinkPad {runId}-118`; PIC `Andi Wijaya`; Due Return Date = hari uji + 10 hari; tanpa foto.
- Data uji: delapan kolom `Photo`, `Transaction ID`, `Name`, `Asset ID`, `Brand`, `Model / Type`, `Due Return Date`, `PIC` (semua Hideable, default tampil); susunan default menurut TC-GS-USER-739: `Photo`, `Name`, `Asset ID`, `Transaction ID`, `Brand`, `Model / Type`, `Due Return Date`, `PIC`.
- Preferensi kolom tabel Borrowed Assets tersimpan di `localStorage` per tabel dan menjadi permanen setelah `[Save]` pada Popup Setup Column (prd-conventions §9.3); "muat ulang halaman" dilakukan pada konteks browser yang sama supaya penyimpanan browser tetap ada.
- Kemampuan teknis (HK8, disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, atau LLD): seeding FAMS yang membuat aset beserta transaksi peminjaman atas `Joko Susilo` dengan Name, Brand, Model / Type, PIC, dan Due Return Date yang ditentukan; membaca Transaction ID dan Asset ID hasil seeding; membaca jumlah borrowed asset Pre-setup `Joko Susilo` sebelum seeding (disebut `B0` di bawah); menghapus atau mengembalikan aset dan transaksi seed di hook `after`.
- Kemampuan teknis tambahan: drag and drop item kolom pada Popup Setup Column; mengatur viewport sehingga tabel overflow horizontal (ukuran dipilih tim FE karena TC tidak menyebutnya) dan scroll horizontal tabel; membaca preview tabel di balik popup; mengarahkan kursor ke checkbox dan icon pin yang disabled untuk membaca tooltip; membaca dan menghapus preferensi kolom di penyimpanan browser.
- State yang diubah dan dipulihkan: setiap kolom yang di-hide, di-reorder, atau di-pin dipulihkan di dalam blok TC-nya, `[Reset to Default]` + `[Save]` pada TC-GS-USER-744 mengembalikan susunan default, dan viewport dikembalikan ke ukuran awal (langkah 261). Hook `after` (tetap jalan walau spec gagal di tengah) mengembalikan konfigurasi kolom tabel Borrowed Assets ke default (semua kolom tampil, urutan default, tanpa pin) lewat `[Reset to Default]` atau penghapusan preferensi kolom tabel di browser, mengembalikan viewport, serta membersihkan aset dan transaksi seed tanpa mengandalkan seeding berhasil penuh.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-739: Screening Overlay Column Visibility

1. Klik icon Search di User List, ketik `Joko Susilo`, tekan Enter
2. Klik Name `Joko Susilo` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Borrowed Assets`
5. Klik header kolom Actions (⋯)
6. Verifikasi Overlay menampilkan daftar kolom berurutan `Photo`, `Name`, `Asset ID`, `Transaction ID`, `Brand`, `Model / Type`, `Due Return Date`, `PIC`
7. Verifikasi kedelapan kolom berkelas Hideable: tercentang (checked) dan enabled
8. Verifikasi tidak ada kolom Curated (unchecked, enabled) di Overlay; seluruh kolom tercentang
9. Verifikasi drag handle tersedia pada tiap kolom
10. Verifikasi item `Setup Column...` tersedia di Overlay

### TC-GS-USER-740: Screening Popup Setup Column

11. Klik `Setup Column...`
12. Verifikasi Header: Title `Setup Column`
13. Verifikasi Header: deskripsi panduan `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
14. Verifikasi Header: icon `[✕]`
15. Verifikasi Body: daftar kolom dengan checkbox
16. Verifikasi Body: drag handle pada tiap kolom
17. Verifikasi Body: icon Pin pada tiap kolom
18. Verifikasi Body: preview tabel merefleksikan susunan kolom
19. Verifikasi Footer: tombol `[Reset to Default]` dan `[Save]`
20. Verifikasi Footer: tidak ada tombol `[Cancel]`

### TC-GS-USER-741: Setup Column hide dan unhide kelas Hideable

21. Hilangkan centang `Photo`
22. Verifikasi preview tabel di balik Popup Setup Column tidak memuat kolom `Photo`
23. Klik `[Save]`
24. Verifikasi kolom `Photo` tidak tampil di tabel setelah Save
25. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
26. Verifikasi kolom `Photo` tetap tidak tampil di tabel setelah F5
27. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
28. Centang kembali `Photo`
29. Klik `[Save]`
30. Verifikasi kolom `Photo` tampil kembali di tabel
31. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
32. Hilangkan centang `Transaction ID`
33. Verifikasi preview tabel di balik Popup Setup Column tidak memuat kolom `Transaction ID`
34. Klik `[Save]`
35. Verifikasi kolom `Transaction ID` tidak tampil di tabel setelah Save
36. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
37. Verifikasi kolom `Transaction ID` tetap tidak tampil di tabel setelah F5
38. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
39. Centang kembali `Transaction ID`
40. Klik `[Save]`
41. Verifikasi kolom `Transaction ID` tampil kembali di tabel
42. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
43. Hilangkan centang `Name`
44. Verifikasi preview tabel di balik Popup Setup Column tidak memuat kolom `Name`
45. Klik `[Save]`
46. Verifikasi kolom `Name` tidak tampil di tabel setelah Save
47. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
48. Verifikasi kolom `Name` tetap tidak tampil di tabel setelah F5
49. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
50. Centang kembali `Name`
51. Klik `[Save]`
52. Verifikasi kolom `Name` tampil kembali di tabel
53. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
54. Hilangkan centang `Asset ID`
55. Verifikasi preview tabel di balik Popup Setup Column tidak memuat kolom `Asset ID`
56. Klik `[Save]`
57. Verifikasi kolom `Asset ID` tidak tampil di tabel setelah Save
58. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
59. Verifikasi kolom `Asset ID` tetap tidak tampil di tabel setelah F5
60. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
61. Centang kembali `Asset ID`
62. Klik `[Save]`
63. Verifikasi kolom `Asset ID` tampil kembali di tabel
64. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
65. Hilangkan centang `Brand`
66. Verifikasi preview tabel di balik Popup Setup Column tidak memuat kolom `Brand`
67. Klik `[Save]`
68. Verifikasi kolom `Brand` tidak tampil di tabel setelah Save
69. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
70. Verifikasi kolom `Brand` tetap tidak tampil di tabel setelah F5
71. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
72. Centang kembali `Brand`
73. Klik `[Save]`
74. Verifikasi kolom `Brand` tampil kembali di tabel
75. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
76. Hilangkan centang `Model / Type`
77. Verifikasi preview tabel di balik Popup Setup Column tidak memuat kolom `Model / Type`
78. Klik `[Save]`
79. Verifikasi kolom `Model / Type` tidak tampil di tabel setelah Save
80. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
81. Verifikasi kolom `Model / Type` tetap tidak tampil di tabel setelah F5
82. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
83. Centang kembali `Model / Type`
84. Klik `[Save]`
85. Verifikasi kolom `Model / Type` tampil kembali di tabel
86. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
87. Hilangkan centang `Due Return Date`
88. Verifikasi preview tabel di balik Popup Setup Column tidak memuat kolom `Due Return Date`
89. Klik `[Save]`
90. Verifikasi kolom `Due Return Date` tidak tampil di tabel setelah Save
91. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
92. Verifikasi kolom `Due Return Date` tetap tidak tampil di tabel setelah F5
93. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
94. Centang kembali `Due Return Date`
95. Klik `[Save]`
96. Verifikasi kolom `Due Return Date` tampil kembali di tabel
97. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
98. Hilangkan centang `PIC`
99. Verifikasi preview tabel di balik Popup Setup Column tidak memuat kolom `PIC`
100. Klik `[Save]`
101. Verifikasi kolom `PIC` tidak tampil di tabel setelah Save
102. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
103. Verifikasi kolom `PIC` tetap tidak tampil di tabel setelah F5
104. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
105. Centang kembali `PIC`
106. Klik `[Save]`
107. Verifikasi kolom `PIC` tampil kembali di tabel

### TC-GS-USER-742: Setup Column drag reorder kelas Hideable

108. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
109. Seret `Photo` ke posisi pertama
110. Verifikasi preview tabel di balik Popup Setup Column menampilkan kolom `Photo` di posisi pertama
111. Klik `[Save]`
112. Verifikasi kolom `Photo` berada di posisi pertama tabel setelah Save
113. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
114. Verifikasi kolom `Photo` tetap di posisi pertama tabel setelah F5
115. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
116. Seret `Transaction ID` ke posisi pertama
117. Verifikasi preview tabel di balik Popup Setup Column menampilkan kolom `Transaction ID` di posisi pertama
118. Klik `[Save]`
119. Verifikasi kolom `Transaction ID` berada di posisi pertama tabel setelah Save
120. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
121. Verifikasi kolom `Transaction ID` tetap di posisi pertama tabel setelah F5
122. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
123. Seret `Name` ke posisi pertama
124. Verifikasi preview tabel di balik Popup Setup Column menampilkan kolom `Name` di posisi pertama
125. Klik `[Save]`
126. Verifikasi kolom `Name` berada di posisi pertama tabel setelah Save
127. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
128. Verifikasi kolom `Name` tetap di posisi pertama tabel setelah F5
129. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
130. Seret `Asset ID` ke posisi pertama
131. Verifikasi preview tabel di balik Popup Setup Column menampilkan kolom `Asset ID` di posisi pertama
132. Klik `[Save]`
133. Verifikasi kolom `Asset ID` berada di posisi pertama tabel setelah Save
134. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
135. Verifikasi kolom `Asset ID` tetap di posisi pertama tabel setelah F5
136. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
137. Seret `Brand` ke posisi pertama
138. Verifikasi preview tabel di balik Popup Setup Column menampilkan kolom `Brand` di posisi pertama
139. Klik `[Save]`
140. Verifikasi kolom `Brand` berada di posisi pertama tabel setelah Save
141. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
142. Verifikasi kolom `Brand` tetap di posisi pertama tabel setelah F5
143. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
144. Seret `Model / Type` ke posisi pertama
145. Verifikasi preview tabel di balik Popup Setup Column menampilkan kolom `Model / Type` di posisi pertama
146. Klik `[Save]`
147. Verifikasi kolom `Model / Type` berada di posisi pertama tabel setelah Save
148. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
149. Verifikasi kolom `Model / Type` tetap di posisi pertama tabel setelah F5
150. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
151. Seret `Due Return Date` ke posisi pertama
152. Verifikasi preview tabel di balik Popup Setup Column menampilkan kolom `Due Return Date` di posisi pertama
153. Klik `[Save]`
154. Verifikasi kolom `Due Return Date` berada di posisi pertama tabel setelah Save
155. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
156. Verifikasi kolom `Due Return Date` tetap di posisi pertama tabel setelah F5
157. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
158. Seret `PIC` ke posisi pertama
159. Verifikasi preview tabel di balik Popup Setup Column menampilkan kolom `PIC` di posisi pertama
160. Klik `[Save]`
161. Verifikasi kolom `PIC` berada di posisi pertama tabel setelah Save
162. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
163. Verifikasi kolom `PIC` tetap di posisi pertama tabel setelah F5

### TC-GS-USER-743: Setup Column pin dan unpin kelas Hideable

164. Sempitkan viewport sehingga tabel dapat di-scroll horizontal
165. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
166. Klik icon pin pada `Photo`
167. Verifikasi preview tabel di balik Popup Setup Column menampilkan kolom `Photo` ter-pin
168. Klik `[Save]`
169. Scroll tabel secara horizontal
170. Verifikasi kolom `Photo` membeku (sticky) saat scroll horizontal setelah Save
171. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
172. Scroll tabel secara horizontal
173. Verifikasi kolom `Photo` tetap membeku (sticky) saat scroll horizontal setelah F5
174. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
175. Klik icon pin pada `Photo` untuk unpin
176. Klik `[Save]`
177. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
178. Klik icon pin pada `Transaction ID`
179. Verifikasi preview tabel di balik Popup Setup Column menampilkan kolom `Transaction ID` ter-pin
180. Klik `[Save]`
181. Scroll tabel secara horizontal
182. Verifikasi kolom `Transaction ID` membeku (sticky) saat scroll horizontal setelah Save
183. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
184. Scroll tabel secara horizontal
185. Verifikasi kolom `Transaction ID` tetap membeku (sticky) saat scroll horizontal setelah F5
186. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
187. Klik icon pin pada `Transaction ID` untuk unpin
188. Klik `[Save]`
189. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
190. Klik icon pin pada `Name`
191. Verifikasi preview tabel di balik Popup Setup Column menampilkan kolom `Name` ter-pin
192. Klik `[Save]`
193. Scroll tabel secara horizontal
194. Verifikasi kolom `Name` membeku (sticky) saat scroll horizontal setelah Save
195. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
196. Scroll tabel secara horizontal
197. Verifikasi kolom `Name` tetap membeku (sticky) saat scroll horizontal setelah F5
198. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
199. Klik icon pin pada `Name` untuk unpin
200. Klik `[Save]`
201. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
202. Klik icon pin pada `Asset ID`
203. Verifikasi preview tabel di balik Popup Setup Column menampilkan kolom `Asset ID` ter-pin
204. Klik `[Save]`
205. Scroll tabel secara horizontal
206. Verifikasi kolom `Asset ID` membeku (sticky) saat scroll horizontal setelah Save
207. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
208. Scroll tabel secara horizontal
209. Verifikasi kolom `Asset ID` tetap membeku (sticky) saat scroll horizontal setelah F5
210. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
211. Klik icon pin pada `Asset ID` untuk unpin
212. Klik `[Save]`
213. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
214. Klik icon pin pada `Brand`
215. Verifikasi preview tabel di balik Popup Setup Column menampilkan kolom `Brand` ter-pin
216. Klik `[Save]`
217. Scroll tabel secara horizontal
218. Verifikasi kolom `Brand` membeku (sticky) saat scroll horizontal setelah Save
219. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
220. Scroll tabel secara horizontal
221. Verifikasi kolom `Brand` tetap membeku (sticky) saat scroll horizontal setelah F5
222. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
223. Klik icon pin pada `Brand` untuk unpin
224. Klik `[Save]`
225. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
226. Klik icon pin pada `Model / Type`
227. Verifikasi preview tabel di balik Popup Setup Column menampilkan kolom `Model / Type` ter-pin
228. Klik `[Save]`
229. Scroll tabel secara horizontal
230. Verifikasi kolom `Model / Type` membeku (sticky) saat scroll horizontal setelah Save
231. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
232. Scroll tabel secara horizontal
233. Verifikasi kolom `Model / Type` tetap membeku (sticky) saat scroll horizontal setelah F5
234. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
235. Klik icon pin pada `Model / Type` untuk unpin
236. Klik `[Save]`
237. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
238. Klik icon pin pada `Due Return Date`
239. Verifikasi preview tabel di balik Popup Setup Column menampilkan kolom `Due Return Date` ter-pin
240. Klik `[Save]`
241. Scroll tabel secara horizontal
242. Verifikasi kolom `Due Return Date` membeku (sticky) saat scroll horizontal setelah Save
243. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
244. Scroll tabel secara horizontal
245. Verifikasi kolom `Due Return Date` tetap membeku (sticky) saat scroll horizontal setelah F5
246. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
247. Klik icon pin pada `Due Return Date` untuk unpin
248. Klik `[Save]`
249. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
250. Klik icon pin pada `PIC`
251. Verifikasi preview tabel di balik Popup Setup Column menampilkan kolom `PIC` ter-pin
252. Klik `[Save]`
253. Scroll tabel secara horizontal
254. Verifikasi kolom `PIC` membeku (sticky) saat scroll horizontal setelah Save
255. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
256. Scroll tabel secara horizontal
257. Verifikasi kolom `PIC` tetap membeku (sticky) saat scroll horizontal setelah F5
258. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
259. Klik icon pin pada `PIC` untuk unpin
260. Klik `[Save]`
261. Kembalikan viewport ke ukuran awal

### TC-GS-USER-744: Setup Column Reset to Default

262. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
263. Seret `Model / Type` ke posisi pertama dan hilangkan centang `Brand`
264. Klik `[Save]`
265. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
266. Klik `[Reset to Default]`
267. Klik `[Save]`
268. Verifikasi susunan kolom tabel kembali default, berurutan `Photo`, `Name`, `Asset ID`, `Transaction ID`, `Brand`, `Model / Type`, `Due Return Date`, `PIC` dan seluruhnya tampil
269. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Borrowed Assets`
270. Verifikasi susunan kolom default bertahan setelah F5

### TC-GS-USER-745: Tutup Setup Column lewat [✕] membuang perubahan

271. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
272. Hilangkan centang `PIC` dan seret `Brand` ke posisi pertama
273. Klik `[✕]`
274. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir: kolom `PIC` tampil
275. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir: kolom berurutan `Photo`, `Name`, `Asset ID`, `Transaction ID`, `Brand`, `Model / Type`, `Due Return Date`, `PIC`

### TC-GS-USER-746: Guard satu kolom tersisa tidak bisa di-uncheck

276. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
277. Hilangkan centang semua kolom kecuali `PIC`
278. Arahkan kursor ke checkbox `PIC`
279. Verifikasi checkbox `PIC` tetap tampil namun disabled
280. Verifikasi tooltip `At least one column must remain visible.` tampil
281. Klik `[✕]` untuk menutup popup tanpa Save

### TC-GS-USER-747: Maksimal 3 kolom di-pin

282. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
283. Klik icon pin pada `Photo`, `Name`, dan `Asset ID`
284. Arahkan kursor ke icon pin kolom keempat, `Transaction ID`
285. Verifikasi icon pin `Transaction ID` disabled
286. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.` tampil
287. Klik `[✕]` untuk menutup popup tanpa Save

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE (preferensi kolom disimpan di browser; tabel dimuat dari backend nyata). Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (739 sampai 747) dipertahankan; dua TC screening (739, 740) di awal.
- Data target: TC sumber memakai `Ahmad Fauzi`; spec memakai `Joko Susilo` (Tabel Pre-setup No. 19) dengan populasi aset pinjaman milik spec (lebih dari satu halaman).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencari user target di User List); langkah 25, 36, 47, 58, 69, 80, 91, 102, 113, 120, 127, 134, 141, 148, 155, 162, 171, 183, 195, 207, 219, 231, 243, 255, 269 (muat ulang halaman dan membuka kembali sub-tab); langkah 164 (menyempitkan viewport); langkah 261 (mengembalikan viewport); langkah 281, 287 (menutup popup tanpa Save). Langkah "Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`" yang berulang adalah prefix berulang: popup menutup setelah `[Save]` atau `[✕]`. Popup yang masih terbuka dari TC-GS-USER-740 dipakai langkah pertama TC-GS-USER-741, dan blok kolom pertama TC-GS-USER-741 tidak membuka ulang popup.
- Tafsir TC-GS-USER-741: "uncheck lalu check, Save, refresh F5" dibaca sebagai hide, Save, F5 (kolom tetap hidden), lalu centang kembali dan Save, sehingga ketiga klausa Expected (preview, tersimpan setelah Save, bertahan setelah F5) teramati dan kolom dipulihkan sebelum kolom berikutnya. TC-GS-USER-742 dan 743 mengikuti pola yang sama: perubahan, preview, Save, F5, dengan pin dilepas (unpin) setelah F5 sebagaimana langkah TC. Reorder pada TC-GS-USER-742 tidak dipulihkan per kolom; susunan dikembalikan oleh `[Reset to Default]` pada TC-GS-USER-744 (langkah TC-GS-USER-743 tidak bergantung pada urutan kolom).
- Muat ulang halaman (F5) diikuti klik Tab `Responsibilities` dan sub-tab `Borrowed Assets` sebagai langkah penghubung: spec tidak mengasumsikan sub-tab aktif dipertahankan setelah muat ulang (tidak disebut di TC dan PRD). Pada TC-GS-USER-743 scroll horizontal diulang setelah F5 karena posisi scroll tidak dipertahankan.
- Spec melewati sekitar 35 langkah (287 langkah) karena TC-GS-USER-741, 742, dan 743 masing-masing menguji delapan kolom dengan blok identik (ubah, preview, Save, F5, periksa) ditambah dua TC screening dan empat TC penutupan, reset, dan guard; semuanya satu kelas harness (fungsional) pada Popup dan Overlay Setup Column yang sama, dan tiap blok kolom berdiri sendiri. Langkah pembuka popup yang berulang merupakan prefix berulang.
- Pembagian TC lintas spec: TC-GS-USER-387, 388, 716 sampai 721 (termasuk Search terhadap kolom `PIC` yang di-hide) ada di spec 114; TC-GS-USER-722 sampai 730 ada di spec 115; TC-GS-USER-731 sampai 735 (termasuk filter kolom `Brand` yang di-hide) ada di spec 116; TC-GS-USER-736, 737, 738, 753, 754 ada di spec 117; TC-GS-USER-389 dan 748 sampai 752 (termasuk Download terhadap kolom hidden) ada di spec 119.
- Temuan untuk QA:
  - TC-GS-USER-739: urutan kolom Overlay (`Photo | Name | Asset ID | Transaction ID | ...`) berbeda dari header tabel pada TC-GS-USER-387 (`Photo | Transaction ID | Name | Asset ID | ...`); PRD user.md §4.1.3 sejalan dengan TC-GS-USER-739. Spec ini mengikuti TC-GS-USER-739 untuk susunan default.
  - TC-GS-USER-739 Expected b: "kolom Curated unchecked & enabled" tidak punya objek karena tabel Borrowed Assets tidak memiliki kolom Curated (prd-conventions §9.3; PRD user.md §4.1.3); spec mengasersi tidak ada kolom Curated.
  - TC-GS-USER-740: "deskripsi panduan" tidak disebut teksnya; spec memakai teks dari prd-conventions §9.3. Body "icon Pin + preview tabel" tidak menyebut isi preview; spec hanya mengasersi preview tampil merefleksikan susunan kolom.
  - TC-GS-USER-741 sampai 743: langkah TC "uncheck lalu check" ambigu (hasil akhir identik dengan default); lihat tafsir di atas. Expected persistensi F5 teramati selagi perubahan masih tersimpan (hidden, posisi pertama, pin).
  - TC-GS-USER-743: TC tidak menyebut ukuran viewport; tim FE menetapkan viewport sempit supaya tabel dapat di-scroll horizontal. Pin kolom `Photo` pada posisi pertama tidak menimbulkan perbedaan visual saat scroll bila kolom itu sudah di kiri.
  - TC-GS-USER-744: langkah "Ubah urutan dan visibility kolom, Save" tidak menyebut kolom; spec memindahkan `Model / Type` ke posisi pertama dan menyembunyikan `Brand`.
  - TC-GS-USER-745: TC tidak menyebut konfigurasi yang diubah; spec menyembunyikan `PIC` dan memindahkan `Brand` ke posisi pertama.
  - TC-GS-USER-747: "kolom keempat" mengacu urutan default (`Transaction ID`).
  - Mekanisme menandai Guided Tooltip sebagai sudah dilihat, menghapus preferensi kolom di browser, dan seeding FAMS tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.

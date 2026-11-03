---
id: TC-GS-USER-E2E-136-subtab-pending-tasks-setup-column-overlay-popup-hide-reorder-pin-reset
title: "Sub-tab Pending Tasks: Setup Column (Overlay, Popup, Hide, Reorder, Pin, Reset, Guard)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-855
  - TC-GS-USER-856
  - TC-GS-USER-857
  - TC-GS-USER-858
  - TC-GS-USER-859
  - TC-GS-USER-860
  - TC-GS-USER-861
  - TC-GS-USER-862
  - TC-GS-USER-863
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Setup Column (Overlay, Popup, Hide, Reorder, Pin, Reset, Guard)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data User; yang di-seed hanya task pending FAMS milik spec (Population PT-22), dipakai sebagai isi tabel pada preview Setup Column.
- Akun: Total Control, Siti Nurhaliza (Tabel Data Uji Pre-setup No. 2), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman Global Settings > User > User List (sub-tab Login User) dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Data Pre-setup (hanya dibaca, tidak diubah): Ahmad Fauzi (Tabel Data Uji Pre-setup No. 13; entitas Client PT Maju Bersama dengan subscription Fixed Asset, sehingga Tab `Responsibilities` dan sub-tab `Pending Tasks` tampil).
- Data Dinamis, Population PT-22 (task pending milik Ahmad Fauzi; sub-tab `Pending Tasks` memuat `B0` + 22 baris sesudah seeding, dengan `B0` = jumlah task pending Pre-setup Ahmad Fauzi yang dibaca lewat kemampuan baca BE tepat sebelum seeding; kemampuan itu disediakan tim FE/BE). Task Borrowing dan Assignment di-seed di hook `before` lewat kemampuan seeding data FAMS (HK8) yang disediakan tim FE/BE; mekanisme dan endpoint-nya tidak ada di TC, PRD, atau LLD sehingga ditentukan tim FE/BE dan tidak dikarang di spec. Seeding juga mengatur Request Date dan Last Updated per kelompok; Group dan PIC task seed memakai Group dan user FAMS yang disediakan tim FE/BE dan bernama bersuffix `{runId}-136` (`{group-A}` = `Alfa {runId}-136`, `{group-B}` = `Beta {runId}-136`; PIC `{pic-A}` nama lengkap `Rina Pica {runId}-136`, `{pic-B}` nama lengkap `Sari Picb {runId}-136`), sehingga tidak bentrok dengan task Pre-setup. Task Pre-setup Ahmad Fauzi (`B0` baris) tidak diubah dan isinya tidak diasumsikan: asersi jumlah per nilai Group atau PIC memakai nama bersuffix itu, sedangkan asersi per nilai Transaction, Status, Total Asset, Request Date, atau Last Updated menyebut baris seed (task milik spec ini). Transaction ID dihasilkan sistem (contoh format PRD: `ASG-YYYYMMDD-XXXX` untuk Assignment, `BRW-YYYYMMDD-XXXX` untuk Borrowing) sehingga tidak bersuffix `{runId}`; hook `before` mencatat task yang dibuat spec dan hook `after` hanya membersihkan task itu, tanpa berasumsi seeding berhasil penuh. Record User Ahmad Fauzi tidak diubah.

  | Kelompok | Baris | Transaction | Status | Group | PIC | Total Asset | Request Date | Last Updated |
  |---|---|---|---|---|---|---|---|---|
  | P | 8 | `Assignment` | `Waiting for Acceptance` | `{group-A}` | `{pic-A}` | `1` (5 baris), `2` (3 baris) | `{rd-1}` | `{lu-1}` |
  | Q1 | 12 | `Borrowing` | `Waiting for Confirmation` | `{group-B}` | `{pic-B}` | `3` (6 baris), `10` (6 baris) | `{rd-3}` | `{lu-2}` |
  | Q2 | 2 | `Borrowing` | `Waiting for Confirmation` | `{group-A}` | `{pic-B}` | `1` (1 baris), `2` (1 baris) | `{rd-2}` | `{lu-1}` |

  Aturan nilai: `{group-A}` lebih kecil dari `{group-B}` dan `{pic-A}` lebih kecil dari `{pic-B}` menurut urutan A-Z; `{rd-1}` < `{rd-2}` < `{rd-3}` dan `{lu-1}` < `{lu-2}`, ditulis dalam Date Format General Settings (nilai default environment, tidak diubah spec); `{kw-group}` (`lfa {runId}-136`, potongan `{group-A}`) dan `{kw-pic}` (`Pica {runId}-136`, potongan nama lengkap `{pic-A}`) hanya muncul pada kolom masing-masing, dan `Acceptance` hanya muncul pada kolom Status. Turunan (baris seed): Transaction `Assignment` 8 baris dan `Borrowing` 14 baris; Group `{group-A}` 10 baris dan `{group-B}` 12 baris; PIC `{pic-A}` 8 baris dan `{pic-B}` 14 baris; Total Asset `1` 6 baris, `2` 4 baris, `3` 6 baris, `10` 6 baris; total tabel `B0` + 22 baris sehingga page size 10 menghasilkan sedikitnya 3 halaman.
- Data uji: delapan kolom `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date`, `Last Updated` (semua Hideable, default visible, tanpa pin; tabel Pending Tasks tidak memiliki kolom Curated). Asersi spec ini menyangkut kolom tabel; komposisi kelompok Population PT-22 tidak diasersi, yang dipakai hanya jumlah baris lebih dari satu halaman.
- Preferensi kolom (visibilitas, urutan, pin) tersimpan per user di browser per tabel dan menjadi permanen setelah `[Save]` (PRD `prd-conventions.md` §9.3, cache `localStorage`); "muat ulang halaman" dilakukan pada konteks browser yang sama supaya penyimpanan browser tetap ada.
- State yang diubah dan dipulihkan: preferensi kolom tabel Pending Tasks dikembalikan ke default lewat `[Reset to Default]` dan `[Save]` di langkah 293 (setelah itu TC-GS-USER-861 sampai 863 tidak menyimpan perubahan); viewport dikembalikan di langkah 285. Hook `after` (tetap jalan walau spec gagal di tengah) menghapus preferensi kolom tabel Pending Tasks di browser dan mengembalikan viewport; nama key dan cara menghapusnya tidak didefinisikan di TC, PRD, atau LLD sehingga disediakan tim FE/BE.
- Kemampuan teknis: drag and drop baris kolom pada popup Setup Column; mengarahkan kursor ke checkbox dan icon Pin disabled untuk membaca tooltip; mengatur ukuran viewport dan scroll horizontal tabel; membaca atau menghapus preferensi kolom di penyimpanan browser; seeding task pending FAMS dan pembersihannya (di atas).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-855: Screening Overlay Column Visibility

1. Klik icon Search di User List, ketik `Ahmad Fauzi`, tekan Enter
2. Klik Name `Ahmad Fauzi` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Pending Tasks`
5. Klik header kolom Actions (⋯)
6. Verifikasi overlay menampilkan daftar kolom `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date`, `Last Updated`
7. Verifikasi seluruh kolom Hideable tercentang dan enabled
8. Verifikasi tiap kolom memiliki drag handle
9. Verifikasi item `Setup Column...` tersedia di overlay

### TC-GS-USER-856: Screening Popup Setup Column

10. Klik item `Setup Column...`
11. Verifikasi Header: Title `Setup Column`
12. Verifikasi Header: deskripsi panduan tampil
13. Verifikasi Header: icon `[✕]`
14. Verifikasi Body: daftar kolom dengan checkbox
15. Verifikasi Body: drag handle pada tiap kolom
16. Verifikasi Body: icon Pin pada tiap kolom
17. Verifikasi Body: preview tabel
18. Verifikasi Footer: tombol `[Reset to Default]` dan `[Save]`
19. Verifikasi Footer: tidak ada tombol `[Cancel]`

### TC-GS-USER-857: Setup Column hide dan unhide kelas Hideable

20. Hilangkan centang kolom `Transaction ID`
21. Verifikasi preview tabel tidak memuat kolom `Transaction ID`
22. Klik `[Save]`
23. Verifikasi tabel tidak memuat kolom `Transaction ID` setelah `[Save]`
24. Muat ulang halaman (F5)
25. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
26. Verifikasi kolom `Transaction` tampil di tabel setelah F5
27. Verifikasi kolom `Transaction ID` tetap tidak tampil setelah F5
28. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
29. Centang kembali kolom `Transaction ID`
30. Klik `[Save]`
31. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
32. Hilangkan centang kolom `Transaction`
33. Verifikasi preview tabel tidak memuat kolom `Transaction`
34. Klik `[Save]`
35. Verifikasi tabel tidak memuat kolom `Transaction` setelah `[Save]`
36. Muat ulang halaman (F5)
37. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
38. Verifikasi kolom `Transaction ID` tampil di tabel setelah F5
39. Verifikasi kolom `Transaction` tetap tidak tampil setelah F5
40. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
41. Centang kembali kolom `Transaction`
42. Klik `[Save]`
43. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
44. Hilangkan centang kolom `Status`
45. Verifikasi preview tabel tidak memuat kolom `Status`
46. Klik `[Save]`
47. Verifikasi tabel tidak memuat kolom `Status` setelah `[Save]`
48. Muat ulang halaman (F5)
49. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
50. Verifikasi kolom `Transaction ID` tampil di tabel setelah F5
51. Verifikasi kolom `Status` tetap tidak tampil setelah F5
52. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
53. Centang kembali kolom `Status`
54. Klik `[Save]`
55. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
56. Hilangkan centang kolom `Group`
57. Verifikasi preview tabel tidak memuat kolom `Group`
58. Klik `[Save]`
59. Verifikasi tabel tidak memuat kolom `Group` setelah `[Save]`
60. Muat ulang halaman (F5)
61. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
62. Verifikasi kolom `Transaction ID` tampil di tabel setelah F5
63. Verifikasi kolom `Group` tetap tidak tampil setelah F5
64. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
65. Centang kembali kolom `Group`
66. Klik `[Save]`
67. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
68. Hilangkan centang kolom `PIC`
69. Verifikasi preview tabel tidak memuat kolom `PIC`
70. Klik `[Save]`
71. Verifikasi tabel tidak memuat kolom `PIC` setelah `[Save]`
72. Muat ulang halaman (F5)
73. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
74. Verifikasi kolom `Transaction ID` tampil di tabel setelah F5
75. Verifikasi kolom `PIC` tetap tidak tampil setelah F5
76. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
77. Centang kembali kolom `PIC`
78. Klik `[Save]`
79. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
80. Hilangkan centang kolom `Total Asset`
81. Verifikasi preview tabel tidak memuat kolom `Total Asset`
82. Klik `[Save]`
83. Verifikasi tabel tidak memuat kolom `Total Asset` setelah `[Save]`
84. Muat ulang halaman (F5)
85. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
86. Verifikasi kolom `Transaction ID` tampil di tabel setelah F5
87. Verifikasi kolom `Total Asset` tetap tidak tampil setelah F5
88. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
89. Centang kembali kolom `Total Asset`
90. Klik `[Save]`
91. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
92. Hilangkan centang kolom `Request Date`
93. Verifikasi preview tabel tidak memuat kolom `Request Date`
94. Klik `[Save]`
95. Verifikasi tabel tidak memuat kolom `Request Date` setelah `[Save]`
96. Muat ulang halaman (F5)
97. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
98. Verifikasi kolom `Transaction ID` tampil di tabel setelah F5
99. Verifikasi kolom `Request Date` tetap tidak tampil setelah F5
100. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
101. Centang kembali kolom `Request Date`
102. Klik `[Save]`
103. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
104. Hilangkan centang kolom `Last Updated`
105. Verifikasi preview tabel tidak memuat kolom `Last Updated`
106. Klik `[Save]`
107. Verifikasi tabel tidak memuat kolom `Last Updated` setelah `[Save]`
108. Muat ulang halaman (F5)
109. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
110. Verifikasi kolom `Transaction ID` tampil di tabel setelah F5
111. Verifikasi kolom `Last Updated` tetap tidak tampil setelah F5
112. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
113. Centang kembali kolom `Last Updated`
114. Klik `[Save]`
115. Verifikasi tabel menampilkan kedelapan kolom `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date`, `Last Updated`

### TC-GS-USER-858: Setup Column drag reorder kelas Hideable

116. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
117. Seret kolom `Transaction ID` ke posisi terakhir
118. Verifikasi preview tabel menampilkan kolom `Transaction ID` di posisi terakhir
119. Klik `[Save]`
120. Verifikasi kolom `Transaction ID` berada di posisi terakhir tabel setelah `[Save]`
121. Muat ulang halaman (F5)
122. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
123. Verifikasi kolom `Transaction ID` tetap di posisi terakhir tabel setelah F5
124. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
125. Seret kolom `Transaction` ke posisi pertama
126. Verifikasi preview tabel menampilkan kolom `Transaction` di posisi pertama
127. Klik `[Save]`
128. Verifikasi kolom `Transaction` berada di posisi pertama tabel setelah `[Save]`
129. Muat ulang halaman (F5)
130. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
131. Verifikasi kolom `Transaction` tetap di posisi pertama tabel setelah F5
132. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
133. Seret kolom `Status` ke posisi pertama
134. Verifikasi preview tabel menampilkan kolom `Status` di posisi pertama
135. Klik `[Save]`
136. Verifikasi kolom `Status` berada di posisi pertama tabel setelah `[Save]`
137. Muat ulang halaman (F5)
138. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
139. Verifikasi kolom `Status` tetap di posisi pertama tabel setelah F5
140. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
141. Seret kolom `Group` ke posisi pertama
142. Verifikasi preview tabel menampilkan kolom `Group` di posisi pertama
143. Klik `[Save]`
144. Verifikasi kolom `Group` berada di posisi pertama tabel setelah `[Save]`
145. Muat ulang halaman (F5)
146. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
147. Verifikasi kolom `Group` tetap di posisi pertama tabel setelah F5
148. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
149. Seret kolom `PIC` ke posisi pertama
150. Verifikasi preview tabel menampilkan kolom `PIC` di posisi pertama
151. Klik `[Save]`
152. Verifikasi kolom `PIC` berada di posisi pertama tabel setelah `[Save]`
153. Muat ulang halaman (F5)
154. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
155. Verifikasi kolom `PIC` tetap di posisi pertama tabel setelah F5
156. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
157. Seret kolom `Total Asset` ke posisi pertama
158. Verifikasi preview tabel menampilkan kolom `Total Asset` di posisi pertama
159. Klik `[Save]`
160. Verifikasi kolom `Total Asset` berada di posisi pertama tabel setelah `[Save]`
161. Muat ulang halaman (F5)
162. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
163. Verifikasi kolom `Total Asset` tetap di posisi pertama tabel setelah F5
164. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
165. Seret kolom `Request Date` ke posisi pertama
166. Verifikasi preview tabel menampilkan kolom `Request Date` di posisi pertama
167. Klik `[Save]`
168. Verifikasi kolom `Request Date` berada di posisi pertama tabel setelah `[Save]`
169. Muat ulang halaman (F5)
170. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
171. Verifikasi kolom `Request Date` tetap di posisi pertama tabel setelah F5
172. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
173. Seret kolom `Last Updated` ke posisi pertama
174. Verifikasi preview tabel menampilkan kolom `Last Updated` di posisi pertama
175. Klik `[Save]`
176. Verifikasi kolom `Last Updated` berada di posisi pertama tabel setelah `[Save]`
177. Muat ulang halaman (F5)
178. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
179. Verifikasi urutan kolom `Last Updated`, `Request Date`, `Total Asset`, `PIC`, `Group`, `Status`, `Transaction`, `Transaction ID` tetap setelah F5

### TC-GS-USER-859: Setup Column pin dan unpin kelas Hideable

180. Sempitkan viewport sehingga tabel dapat di-scroll horizontal
181. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
182. Klik icon Pin pada kolom `Transaction ID`
183. Verifikasi preview tabel menampilkan kolom `Transaction ID` ter-pin
184. Klik `[Save]`
185. Scroll tabel secara horizontal
186. Verifikasi kolom `Transaction ID` beku (sticky) saat scroll horizontal setelah `[Save]`
187. Muat ulang halaman (F5)
188. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
189. Scroll tabel secara horizontal
190. Verifikasi kolom `Transaction ID` tetap beku saat scroll horizontal setelah F5
191. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
192. Klik icon Pin pada kolom `Transaction ID` untuk unpin
193. Klik `[Save]`
194. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
195. Klik icon Pin pada kolom `Transaction`
196. Verifikasi preview tabel menampilkan kolom `Transaction` ter-pin
197. Klik `[Save]`
198. Scroll tabel secara horizontal
199. Verifikasi kolom `Transaction` beku (sticky) saat scroll horizontal setelah `[Save]`
200. Muat ulang halaman (F5)
201. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
202. Scroll tabel secara horizontal
203. Verifikasi kolom `Transaction` tetap beku saat scroll horizontal setelah F5
204. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
205. Klik icon Pin pada kolom `Transaction` untuk unpin
206. Klik `[Save]`
207. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
208. Klik icon Pin pada kolom `Status`
209. Verifikasi preview tabel menampilkan kolom `Status` ter-pin
210. Klik `[Save]`
211. Scroll tabel secara horizontal
212. Verifikasi kolom `Status` beku (sticky) saat scroll horizontal setelah `[Save]`
213. Muat ulang halaman (F5)
214. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
215. Scroll tabel secara horizontal
216. Verifikasi kolom `Status` tetap beku saat scroll horizontal setelah F5
217. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
218. Klik icon Pin pada kolom `Status` untuk unpin
219. Klik `[Save]`
220. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
221. Klik icon Pin pada kolom `Group`
222. Verifikasi preview tabel menampilkan kolom `Group` ter-pin
223. Klik `[Save]`
224. Scroll tabel secara horizontal
225. Verifikasi kolom `Group` beku (sticky) saat scroll horizontal setelah `[Save]`
226. Muat ulang halaman (F5)
227. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
228. Scroll tabel secara horizontal
229. Verifikasi kolom `Group` tetap beku saat scroll horizontal setelah F5
230. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
231. Klik icon Pin pada kolom `Group` untuk unpin
232. Klik `[Save]`
233. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
234. Klik icon Pin pada kolom `PIC`
235. Verifikasi preview tabel menampilkan kolom `PIC` ter-pin
236. Klik `[Save]`
237. Scroll tabel secara horizontal
238. Verifikasi kolom `PIC` beku (sticky) saat scroll horizontal setelah `[Save]`
239. Muat ulang halaman (F5)
240. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
241. Scroll tabel secara horizontal
242. Verifikasi kolom `PIC` tetap beku saat scroll horizontal setelah F5
243. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
244. Klik icon Pin pada kolom `PIC` untuk unpin
245. Klik `[Save]`
246. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
247. Klik icon Pin pada kolom `Total Asset`
248. Verifikasi preview tabel menampilkan kolom `Total Asset` ter-pin
249. Klik `[Save]`
250. Scroll tabel secara horizontal
251. Verifikasi kolom `Total Asset` beku (sticky) saat scroll horizontal setelah `[Save]`
252. Muat ulang halaman (F5)
253. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
254. Scroll tabel secara horizontal
255. Verifikasi kolom `Total Asset` tetap beku saat scroll horizontal setelah F5
256. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
257. Klik icon Pin pada kolom `Total Asset` untuk unpin
258. Klik `[Save]`
259. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
260. Klik icon Pin pada kolom `Request Date`
261. Verifikasi preview tabel menampilkan kolom `Request Date` ter-pin
262. Klik `[Save]`
263. Scroll tabel secara horizontal
264. Verifikasi kolom `Request Date` beku (sticky) saat scroll horizontal setelah `[Save]`
265. Muat ulang halaman (F5)
266. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
267. Scroll tabel secara horizontal
268. Verifikasi kolom `Request Date` tetap beku saat scroll horizontal setelah F5
269. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
270. Klik icon Pin pada kolom `Request Date` untuk unpin
271. Klik `[Save]`
272. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
273. Klik icon Pin pada kolom `Last Updated`
274. Verifikasi preview tabel menampilkan kolom `Last Updated` ter-pin
275. Klik `[Save]`
276. Scroll tabel secara horizontal
277. Verifikasi kolom `Last Updated` beku (sticky) saat scroll horizontal setelah `[Save]`
278. Muat ulang halaman (F5)
279. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
280. Scroll tabel secara horizontal
281. Verifikasi kolom `Last Updated` tetap beku saat scroll horizontal setelah F5
282. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
283. Klik icon Pin pada kolom `Last Updated` untuk unpin
284. Klik `[Save]`
285. Kembalikan viewport ke ukuran awal

### TC-GS-USER-860: Setup Column Reset to Default

286. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
287. Hilangkan centang kolom `PIC`
288. Seret kolom `Total Asset` ke posisi pertama
289. Klik `[Save]`
290. Verifikasi konfigurasi tersimpan berbeda dari default: kolom `PIC` tidak tampil dan kolom `Total Asset` berada di posisi pertama
291. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
292. Klik `[Reset to Default]`
293. Klik `[Save]`
294. Verifikasi susunan kolom kembali default: `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date`, `Last Updated` tampil berurutan tanpa pin
295. Muat ulang halaman (F5)
296. Buka kembali Tab `Responsibilities` lalu sub-tab `Pending Tasks`
297. Verifikasi susunan kolom default bertahan setelah F5

### TC-GS-USER-861: Tutup Setup Column via [✕] membuang perubahan

298. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
299. Hilangkan centang kolom `Group`
300. Klik `[✕]`
301. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir: kedelapan kolom tampil berurutan default, termasuk kolom `Group`

### TC-GS-USER-862: Guard satu kolom tersisa tidak bisa di-uncheck

302. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
303. Hilangkan centang kolom `Transaction ID`
304. Hilangkan centang kolom `Transaction`
305. Hilangkan centang kolom `Status`
306. Hilangkan centang kolom `Group`
307. Hilangkan centang kolom `PIC`
308. Hilangkan centang kolom `Total Asset`
309. Hilangkan centang kolom `Request Date`
310. Arahkan kursor ke checkbox kolom `Last Updated`
311. Verifikasi checkbox kolom `Last Updated` tetap tampil namun disabled
312. Verifikasi tooltip `At least one column must remain visible.` tampil
313. Klik `[✕]` untuk menutup popup tanpa menyimpan

### TC-GS-USER-863: Maksimal 3 kolom di-pin

314. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
315. Klik icon Pin pada kolom `Transaction ID`
316. Klik icon Pin pada kolom `Transaction`
317. Klik icon Pin pada kolom `Status`
318. Arahkan kursor ke icon Pin kolom `Group`
319. Verifikasi icon Pin kolom `Group` disabled
320. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.` tampil
321. Klik `[✕]` untuk menutup popup tanpa menyimpan

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE (preferensi kolom disimpan di browser; tabel dimuat dari backend nyata).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (855 sampai 863) dipertahankan; dua TC screening (855, 856) di awal sebelum aksi yang mengubah konfigurasi kolom.
- Langkah 1 sampai 4 memenuhi langkah awal "Klik Name `Ahmad Fauzi`, Tab `Responsibilities`, sub-tab `Pending Tasks`" dari seluruh TC sumber; layar itu dibuka sekali dan dipakai bersama. Popup Setup Column yang terbuka pada TC-GS-USER-856 dipakai langkah 20 (TC-GS-USER-857), sehingga "Klik header (⋯) → `Setup Column...`" TC-GS-USER-857 dipenuhi langkah 10.
- Siklus per kolom: TC-GS-USER-857, 858, dan 859 menuliskan siklus Save dan F5 untuk tiap kolom (delapan kali); spec menjalankan siklus itu satu per satu dan mengasersi preview, tabel setelah `[Save]`, dan persistensi setelah F5 untuk tiap kolom. Absence kolom sesudah F5 pada TC-GS-USER-857 didahului `Verifikasi` kolom lain tampil sebagai anchor (bagian 8b butir 2). Pemulihan Setup Column: TC-GS-USER-857 mencentang kembali tiap kolom dan TC-GS-USER-859 meng-unpin tiap kolom dengan `[Save]` (R-24); urutan dari TC-GS-USER-858 dipulihkan oleh `[Reset to Default]` TC-GS-USER-860; hook `after` hanya cadangan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencari user target di User List agar Name dapat diklik, bagian 8b butir 12), langkah 180 dan 285 (menyempitkan dan mengembalikan viewport untuk TC-GS-USER-859), langkah unpin tiap kolom TC-GS-USER-859 dengan `[Save]` (bagian "lalu Unpin"), langkah 313 dan 321 (menutup popup tanpa Save agar uncheck dan pin tidak tersimpan; hook `after` sebagai cadangan), serta langkah muat ulang dan buka kembali Tab dan sub-tab sesudah F5. Langkah membuka popup yang berulang ("Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`") merupakan prefix berulang.
- Urutan konfigurasi: TC-GS-USER-858 menyimpan urutan terbalik, TC-GS-USER-859 mem-pin dan meng-unpin pada urutan itu, dan TC-GS-USER-860 mengubah lalu mereset ke default; TC-GS-USER-861 sampai 863 berjalan sesudahnya pada konfigurasi default tersimpan. Langkah 290 adalah asersi tambahan (S-03) agar Reset to Default berangkat dari konfigurasi yang berbeda dari default (S-14).
- Pembagian TC lintas spec: TC-GS-USER-396, 397, dan 830 sampai 836 ada di spec 132 (Search terhadap kolom hidden: TC-GS-USER-835); TC-GS-USER-837 sampai 846 ada di spec 133; TC-GS-USER-847 sampai 851 (Filter terhadap kolom hidden: TC-GS-USER-850) ada di spec 134; TC-GS-USER-852 sampai 854, 869, dan 870 ada di spec 135; TC-GS-USER-398 dan 864 sampai 868 (Download terhadap kolom hidden: TC-GS-USER-867) ada di spec 137. TC Setup Column sub-tab Pending Approvals ada di spec 130.
- Spec melewati sekitar 35 langkah (321 langkah) karena sembilan TC Setup Column menguji delapan kolom dengan blok identik (hide, reorder, pin) pada satu popup, satu layar, satu dataset, dan satu kelas harness (fungsional). Tiap blok TC berdiri sendiri: konfigurasi dikembalikan ke default oleh langkah akhir blok atau oleh TC-GS-USER-860, sehingga satu kegagalan tidak membuat blok lain kehilangan makna. Langkah muat ulang dan pembukaan kembali sub-tab sesudah F5 serta pembukaan popup adalah prefix berulang.
- Temuan untuk QA:
  - TC-GS-USER-856 Expected a: "deskripsi panduan" tidak ditulis literal di TC; spec hanya mengasersi deskripsi tampil.
  - TC-GS-USER-858: langkah kedua menggeser `Transaction` ke posisi pertama padahal `Transaction` sudah pertama sesudah `Transaction ID` dipindah ke posisi terakhir; Expected tidak membedakannya dari kolom lain.
  - TC-GS-USER-859: TC tidak menyebut cara membuat tabel dapat di-scroll horizontal; spec menyempitkan viewport. Expected "bertahan setelah F5" untuk pin ditulis dengan scroll horizontal setelah F5.
  - TC-GS-USER-860 dan 861: "Ubah urutan dan visibility kolom" dan "ubah konfigurasi" tidak konkret; spec memakai hide `PIC` dengan seret `Total Asset` (860) dan hide `Group` (861).
  - Nama key preferensi kolom di browser dan cara menghapusnya tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE. Seeding task pending FAMS tidak punya mekanisme di TC, PRD, atau LLD; disediakan tim FE/BE.

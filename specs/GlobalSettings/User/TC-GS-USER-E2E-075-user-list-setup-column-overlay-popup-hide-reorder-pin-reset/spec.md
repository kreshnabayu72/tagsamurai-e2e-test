---
id: TC-GS-USER-E2E-075-user-list-setup-column-overlay-popup-hide-reorder-pin-reset
title: "User List: Setup Column (Overlay, Popup, Hide/Unhide, Reorder, Pin per Kolom, Reset to Default, Tutup Tanpa Simpan, Kolom Terakhir, dan Batas 3 Pin)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-441
  - TC-GS-USER-442
  - TC-GS-USER-443
  - TC-GS-USER-444
  - TC-GS-USER-445
  - TC-GS-USER-446
  - TC-GS-USER-447
  - TC-GS-USER-448
  - TC-GS-USER-449
  - TC-GS-USER-450
  - TC-GS-USER-451
  - TC-GS-USER-452
coverage:
  web: automated
---

# User List: Setup Column (Overlay, Popup, Hide/Unhide, Reorder, Pin per Kolom, Reset to Default, Tutup Tanpa Simpan, Kolom Terakhir, dan Batas 3 Pin)

## Prerequisites

- Mode: mock. Seluruh API di-mock (spec dijalankan tim FE sebagai integration test, tanpa backend nyata). Spec tidak mengubah data Pre-setup.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2). Sesi, profil, dan izin Total Control disediakan oleh payload mock; tidak ada login ke backend, sehingga spec tidak memakai env var password.
- Kebutuhan mock (nama endpoint ditentukan tim FE di tahap script): respons daftar User (sub-tab Login User) berisi sedikitnya tiga baris yang meniru user Pre-setup (mis. `Dewi Lestari`, `Budi Hartono`, `John Doe`) dengan nilai terisi pada seluruh 13 kolom (`Active`, `Name`, `Email`, `Position`, `Division`, `Access`, `Employee ID`, `Modified By`, `Last Update`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`); respons Custom Field aktif kosong, sehingga Overlay dan Popup memuat 13 kolom itu saja (TC-GS-USER-441); respons lain yang dibutuhkan layar User List (profil, izin, Guided Tooltip) memakai payload default. Bila FE menyimpan preferensi kolom lewat API, endpoint-nya ikut di-mock; bila disimpan di sisi klien, tidak ada kebutuhan mock tambahan.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22 dan Custom Field aktif No. 24) dirujuk oleh payload mock saja; spec tidak membaca atau mengubah data backend.
- Data Dinamis: tidak ada.
- Preferensi kolom (visibilitas, urutan, pin) bertahan setelah `[Save]` dan setelah muat ulang halaman (F5) pada konteks browser yang sama (`foundation/process/prd-process/prd-conventions.md` §9.3); mock tetap aktif sesudah muat ulang halaman.
- State yang diubah dan dipulihkan: konfigurasi kolom User List (visibilitas, urutan, pin) dikembalikan ke default lewat `[Reset to Default]` dan `[Save]` (langkah 153, 344, dan di TC-GS-USER-449); viewport disempitkan (langkah 156) dan dikembalikan ke ukuran awal (langkah 348). Hook `after` sebagai cadangan mengembalikan konfigurasi kolom ke default (penghapusan preferensi kolom User List di browser; mekanisme disediakan tim FE/BE) dan viewport ke ukuran awal.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: drag and drop item kolom pada Popup Setup Column; mengatur viewport; scroll horizontal tabel; hover untuk membaca tooltip; muat ulang halaman dengan mock tetap aktif; membaca dan menghapus preferensi kolom di penyimpanan browser.

## Test Steps

### TC-GS-USER-441: Screening Overlay Column Visibility

1. Klik header kolom Column Visibility (⋯)
2. Verifikasi Overlay daftar kolom memuat `Active`, `Name`, `Email`, `Position`, `Division`, `Access`, `Employee ID`, `Modified By`, `Last Update`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG` berurutan
3. Verifikasi kolom Hideable (`Active`, `Name`, `Email`, `Position`, `Division`, `Access`, `Employee ID`, `Modified By`, `Last Update`) tercentang dan enabled
4. Verifikasi kolom Curated (`Activation Status`, `Temporary User`, `Temporary Until`, `TAG`) tidak tercentang dan enabled
5. Verifikasi drag handle tersedia pada tiap kolom
6. Verifikasi item `Setup Column...` tersedia di Overlay

### TC-GS-USER-442: Screening Popup Setup Column

7. Klik item `Setup Column...`
8. Verifikasi Header: Title `Setup Column`
9. Verifikasi Header: deskripsi panduan tampil
10. Verifikasi Header: icon `[✕]` tampil
11. Verifikasi Body: daftar kolom dengan checkbox tampil
12. Verifikasi Body: drag handle tampil pada tiap kolom
13. Verifikasi Body: icon Pin tampil pada tiap kolom
14. Verifikasi Body: preview tabel tampil
15. Verifikasi Footer: tombol `[Reset to Default]` dan `[Save]` tampil
16. Verifikasi Footer: tidak ada tombol `[Cancel]`

### TC-GS-USER-443: Setup Column hide/unhide kelas Hideable default tampil

17. Hilangkan centang `Active`
18. Verifikasi kolom Active: perubahan tampil di preview, `Active` tidak tampil di preview tabel
19. Klik `[Save]`
20. Verifikasi kolom Active: tersimpan setelah Save, `Active` tidak tampil di tabel
21. Muat ulang halaman (F5)
22. Verifikasi kolom Active: bertahan setelah F5, `Active` tetap tidak tampil di tabel
23. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
24. Centang kembali `Active`
25. Hilangkan centang `Name`
26. Verifikasi kolom Name: perubahan tampil di preview, `Name` tidak tampil di preview tabel
27. Klik `[Save]`
28. Verifikasi kolom Name: tersimpan setelah Save, `Name` tidak tampil di tabel
29. Muat ulang halaman (F5)
30. Verifikasi kolom Name: bertahan setelah F5, `Name` tetap tidak tampil di tabel
31. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
32. Centang kembali `Name`
33. Hilangkan centang `Email`
34. Verifikasi kolom Email: perubahan tampil di preview, `Email` tidak tampil di preview tabel
35. Klik `[Save]`
36. Verifikasi kolom Email: tersimpan setelah Save, `Email` tidak tampil di tabel
37. Muat ulang halaman (F5)
38. Verifikasi kolom Email: bertahan setelah F5, `Email` tetap tidak tampil di tabel
39. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
40. Centang kembali `Email`
41. Hilangkan centang `Position`
42. Verifikasi kolom Position: perubahan tampil di preview, `Position` tidak tampil di preview tabel
43. Klik `[Save]`
44. Verifikasi kolom Position: tersimpan setelah Save, `Position` tidak tampil di tabel
45. Muat ulang halaman (F5)
46. Verifikasi kolom Position: bertahan setelah F5, `Position` tetap tidak tampil di tabel
47. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
48. Centang kembali `Position`
49. Hilangkan centang `Division`
50. Verifikasi kolom Division: perubahan tampil di preview, `Division` tidak tampil di preview tabel
51. Klik `[Save]`
52. Verifikasi kolom Division: tersimpan setelah Save, `Division` tidak tampil di tabel
53. Muat ulang halaman (F5)
54. Verifikasi kolom Division: bertahan setelah F5, `Division` tetap tidak tampil di tabel
55. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
56. Centang kembali `Division`
57. Hilangkan centang `Access`
58. Verifikasi kolom Access: perubahan tampil di preview, `Access` tidak tampil di preview tabel
59. Klik `[Save]`
60. Verifikasi kolom Access: tersimpan setelah Save, `Access` tidak tampil di tabel
61. Muat ulang halaman (F5)
62. Verifikasi kolom Access: bertahan setelah F5, `Access` tetap tidak tampil di tabel
63. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
64. Centang kembali `Access`
65. Hilangkan centang `Employee ID`
66. Verifikasi kolom Employee ID: perubahan tampil di preview, `Employee ID` tidak tampil di preview tabel
67. Klik `[Save]`
68. Verifikasi kolom Employee ID: tersimpan setelah Save, `Employee ID` tidak tampil di tabel
69. Muat ulang halaman (F5)
70. Verifikasi kolom Employee ID: bertahan setelah F5, `Employee ID` tetap tidak tampil di tabel
71. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
72. Centang kembali `Employee ID`
73. Hilangkan centang `Modified By`
74. Verifikasi kolom Modified By: perubahan tampil di preview, `Modified By` tidak tampil di preview tabel
75. Klik `[Save]`
76. Verifikasi kolom Modified By: tersimpan setelah Save, `Modified By` tidak tampil di tabel
77. Muat ulang halaman (F5)
78. Verifikasi kolom Modified By: bertahan setelah F5, `Modified By` tetap tidak tampil di tabel
79. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
80. Centang kembali `Modified By`
81. Hilangkan centang `Last Update`
82. Verifikasi kolom Last Update: perubahan tampil di preview, `Last Update` tidak tampil di preview tabel
83. Klik `[Save]`
84. Verifikasi kolom Last Update: tersimpan setelah Save, `Last Update` tidak tampil di tabel
85. Muat ulang halaman (F5)
86. Verifikasi kolom Last Update: bertahan setelah F5, `Last Update` tetap tidak tampil di tabel
87. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
88. Centang kembali `Last Update`
89. Klik `[Save]`

### TC-GS-USER-444: Setup Column drag reorder kelas Hideable default tampil

90. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
91. Seret `Active` ke posisi pertama
92. Verifikasi kolom Active: perubahan tampil di preview, `Active` berada di posisi pertama preview tabel
93. Klik `[Save]`
94. Verifikasi kolom Active: tersimpan setelah Save, `Active` berada di posisi pertama tabel
95. Muat ulang halaman (F5)
96. Verifikasi kolom Active: bertahan setelah F5, `Active` tetap berada di posisi pertama tabel
97. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
98. Seret `Name` ke posisi pertama
99. Verifikasi kolom Name: perubahan tampil di preview, `Name` berada di posisi pertama preview tabel
100. Klik `[Save]`
101. Verifikasi kolom Name: tersimpan setelah Save, `Name` berada di posisi pertama tabel
102. Muat ulang halaman (F5)
103. Verifikasi kolom Name: bertahan setelah F5, `Name` tetap berada di posisi pertama tabel
104. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
105. Seret `Email` ke posisi pertama
106. Verifikasi kolom Email: perubahan tampil di preview, `Email` berada di posisi pertama preview tabel
107. Klik `[Save]`
108. Verifikasi kolom Email: tersimpan setelah Save, `Email` berada di posisi pertama tabel
109. Muat ulang halaman (F5)
110. Verifikasi kolom Email: bertahan setelah F5, `Email` tetap berada di posisi pertama tabel
111. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
112. Seret `Position` ke posisi pertama
113. Verifikasi kolom Position: perubahan tampil di preview, `Position` berada di posisi pertama preview tabel
114. Klik `[Save]`
115. Verifikasi kolom Position: tersimpan setelah Save, `Position` berada di posisi pertama tabel
116. Muat ulang halaman (F5)
117. Verifikasi kolom Position: bertahan setelah F5, `Position` tetap berada di posisi pertama tabel
118. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
119. Seret `Division` ke posisi pertama
120. Verifikasi kolom Division: perubahan tampil di preview, `Division` berada di posisi pertama preview tabel
121. Klik `[Save]`
122. Verifikasi kolom Division: tersimpan setelah Save, `Division` berada di posisi pertama tabel
123. Muat ulang halaman (F5)
124. Verifikasi kolom Division: bertahan setelah F5, `Division` tetap berada di posisi pertama tabel
125. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
126. Seret `Access` ke posisi pertama
127. Verifikasi kolom Access: perubahan tampil di preview, `Access` berada di posisi pertama preview tabel
128. Klik `[Save]`
129. Verifikasi kolom Access: tersimpan setelah Save, `Access` berada di posisi pertama tabel
130. Muat ulang halaman (F5)
131. Verifikasi kolom Access: bertahan setelah F5, `Access` tetap berada di posisi pertama tabel
132. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
133. Seret `Employee ID` ke posisi pertama
134. Verifikasi kolom Employee ID: perubahan tampil di preview, `Employee ID` berada di posisi pertama preview tabel
135. Klik `[Save]`
136. Verifikasi kolom Employee ID: tersimpan setelah Save, `Employee ID` berada di posisi pertama tabel
137. Muat ulang halaman (F5)
138. Verifikasi kolom Employee ID: bertahan setelah F5, `Employee ID` tetap berada di posisi pertama tabel
139. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
140. Seret `Modified By` ke posisi pertama
141. Verifikasi kolom Modified By: perubahan tampil di preview, `Modified By` berada di posisi pertama preview tabel
142. Klik `[Save]`
143. Verifikasi kolom Modified By: tersimpan setelah Save, `Modified By` berada di posisi pertama tabel
144. Muat ulang halaman (F5)
145. Verifikasi kolom Modified By: bertahan setelah F5, `Modified By` tetap berada di posisi pertama tabel
146. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
147. Seret `Last Update` ke posisi pertama
148. Verifikasi kolom Last Update: perubahan tampil di preview, `Last Update` berada di posisi pertama preview tabel
149. Klik `[Save]`
150. Verifikasi kolom Last Update: tersimpan setelah Save, `Last Update` berada di posisi pertama tabel
151. Muat ulang halaman (F5)
152. Verifikasi kolom Last Update: bertahan setelah F5, `Last Update` tetap berada di posisi pertama tabel
153. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
154. Klik `[Reset to Default]`
155. Klik `[Save]`

### TC-GS-USER-445: Setup Column pin/unpin kelas Hideable default tampil

156. Sempitkan viewport sehingga tabel dapat di-scroll horizontal
157. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
158. Klik icon pin pada `Active`
159. Verifikasi kolom Active: perubahan tampil di preview, `Active` berstatus pin di preview tabel
160. Klik `[Save]`
161. Scroll tabel secara horizontal
162. Verifikasi kolom Active: tersimpan setelah Save, `Active` membeku (tetap terlihat) saat scroll horizontal
163. Muat ulang halaman (F5)
164. Scroll tabel secara horizontal
165. Verifikasi kolom Active: bertahan setelah F5, `Active` tetap membeku saat scroll horizontal
166. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
167. Klik icon pin pada `Active` untuk Unpin
168. Klik icon pin pada `Name`
169. Verifikasi kolom Name: perubahan tampil di preview, `Name` berstatus pin di preview tabel
170. Klik `[Save]`
171. Scroll tabel secara horizontal
172. Verifikasi kolom Name: tersimpan setelah Save, `Name` membeku (tetap terlihat) saat scroll horizontal
173. Muat ulang halaman (F5)
174. Scroll tabel secara horizontal
175. Verifikasi kolom Name: bertahan setelah F5, `Name` tetap membeku saat scroll horizontal
176. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
177. Klik icon pin pada `Name` untuk Unpin
178. Klik icon pin pada `Email`
179. Verifikasi kolom Email: perubahan tampil di preview, `Email` berstatus pin di preview tabel
180. Klik `[Save]`
181. Scroll tabel secara horizontal
182. Verifikasi kolom Email: tersimpan setelah Save, `Email` membeku (tetap terlihat) saat scroll horizontal
183. Muat ulang halaman (F5)
184. Scroll tabel secara horizontal
185. Verifikasi kolom Email: bertahan setelah F5, `Email` tetap membeku saat scroll horizontal
186. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
187. Klik icon pin pada `Email` untuk Unpin
188. Klik icon pin pada `Position`
189. Verifikasi kolom Position: perubahan tampil di preview, `Position` berstatus pin di preview tabel
190. Klik `[Save]`
191. Scroll tabel secara horizontal
192. Verifikasi kolom Position: tersimpan setelah Save, `Position` membeku (tetap terlihat) saat scroll horizontal
193. Muat ulang halaman (F5)
194. Scroll tabel secara horizontal
195. Verifikasi kolom Position: bertahan setelah F5, `Position` tetap membeku saat scroll horizontal
196. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
197. Klik icon pin pada `Position` untuk Unpin
198. Klik icon pin pada `Division`
199. Verifikasi kolom Division: perubahan tampil di preview, `Division` berstatus pin di preview tabel
200. Klik `[Save]`
201. Scroll tabel secara horizontal
202. Verifikasi kolom Division: tersimpan setelah Save, `Division` membeku (tetap terlihat) saat scroll horizontal
203. Muat ulang halaman (F5)
204. Scroll tabel secara horizontal
205. Verifikasi kolom Division: bertahan setelah F5, `Division` tetap membeku saat scroll horizontal
206. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
207. Klik icon pin pada `Division` untuk Unpin
208. Klik icon pin pada `Access`
209. Verifikasi kolom Access: perubahan tampil di preview, `Access` berstatus pin di preview tabel
210. Klik `[Save]`
211. Scroll tabel secara horizontal
212. Verifikasi kolom Access: tersimpan setelah Save, `Access` membeku (tetap terlihat) saat scroll horizontal
213. Muat ulang halaman (F5)
214. Scroll tabel secara horizontal
215. Verifikasi kolom Access: bertahan setelah F5, `Access` tetap membeku saat scroll horizontal
216. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
217. Klik icon pin pada `Access` untuk Unpin
218. Klik icon pin pada `Employee ID`
219. Verifikasi kolom Employee ID: perubahan tampil di preview, `Employee ID` berstatus pin di preview tabel
220. Klik `[Save]`
221. Scroll tabel secara horizontal
222. Verifikasi kolom Employee ID: tersimpan setelah Save, `Employee ID` membeku (tetap terlihat) saat scroll horizontal
223. Muat ulang halaman (F5)
224. Scroll tabel secara horizontal
225. Verifikasi kolom Employee ID: bertahan setelah F5, `Employee ID` tetap membeku saat scroll horizontal
226. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
227. Klik icon pin pada `Employee ID` untuk Unpin
228. Klik icon pin pada `Modified By`
229. Verifikasi kolom Modified By: perubahan tampil di preview, `Modified By` berstatus pin di preview tabel
230. Klik `[Save]`
231. Scroll tabel secara horizontal
232. Verifikasi kolom Modified By: tersimpan setelah Save, `Modified By` membeku (tetap terlihat) saat scroll horizontal
233. Muat ulang halaman (F5)
234. Scroll tabel secara horizontal
235. Verifikasi kolom Modified By: bertahan setelah F5, `Modified By` tetap membeku saat scroll horizontal
236. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
237. Klik icon pin pada `Modified By` untuk Unpin
238. Klik icon pin pada `Last Update`
239. Verifikasi kolom Last Update: perubahan tampil di preview, `Last Update` berstatus pin di preview tabel
240. Klik `[Save]`
241. Scroll tabel secara horizontal
242. Verifikasi kolom Last Update: tersimpan setelah Save, `Last Update` membeku (tetap terlihat) saat scroll horizontal
243. Muat ulang halaman (F5)
244. Scroll tabel secara horizontal
245. Verifikasi kolom Last Update: bertahan setelah F5, `Last Update` tetap membeku saat scroll horizontal
246. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
247. Klik icon pin pada `Last Update` untuk Unpin
248. Klik `[Save]`

### TC-GS-USER-446: Setup Column hide/unhide kelas Curated default tersembunyi

249. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
250. Centang `Activation Status` (default tidak tercentang)
251. Verifikasi kolom Activation Status: perubahan tampil di preview, `Activation Status` tampil di preview tabel
252. Klik `[Save]`
253. Verifikasi kolom Activation Status: tersimpan setelah Save, `Activation Status` tampil di tabel
254. Muat ulang halaman (F5)
255. Verifikasi kolom Activation Status: bertahan setelah F5, `Activation Status` tetap tampil di tabel
256. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
257. Centang `Temporary User` (default tidak tercentang)
258. Verifikasi kolom Temporary User: perubahan tampil di preview, `Temporary User` tampil di preview tabel
259. Klik `[Save]`
260. Verifikasi kolom Temporary User: tersimpan setelah Save, `Temporary User` tampil di tabel
261. Muat ulang halaman (F5)
262. Verifikasi kolom Temporary User: bertahan setelah F5, `Temporary User` tetap tampil di tabel
263. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
264. Centang `Temporary Until` (default tidak tercentang)
265. Verifikasi kolom Temporary Until: perubahan tampil di preview, `Temporary Until` tampil di preview tabel
266. Klik `[Save]`
267. Verifikasi kolom Temporary Until: tersimpan setelah Save, `Temporary Until` tampil di tabel
268. Muat ulang halaman (F5)
269. Verifikasi kolom Temporary Until: bertahan setelah F5, `Temporary Until` tetap tampil di tabel
270. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
271. Centang `TAG` (default tidak tercentang)
272. Verifikasi kolom TAG: perubahan tampil di preview, `TAG` tampil di preview tabel
273. Klik `[Save]`
274. Verifikasi kolom TAG: tersimpan setelah Save, `TAG` tampil di tabel
275. Muat ulang halaman (F5)
276. Verifikasi kolom TAG: bertahan setelah F5, `TAG` tetap tampil di tabel

### TC-GS-USER-447: Setup Column drag reorder kelas Curated default tersembunyi

277. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
278. Seret `Activation Status` ke posisi pertama
279. Verifikasi kolom Activation Status: perubahan tampil di preview, `Activation Status` berada di posisi pertama preview tabel
280. Klik `[Save]`
281. Verifikasi kolom Activation Status: tersimpan setelah Save, `Activation Status` berada di posisi pertama tabel
282. Muat ulang halaman (F5)
283. Verifikasi kolom Activation Status: bertahan setelah F5, `Activation Status` tetap berada di posisi pertama tabel
284. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
285. Seret `Temporary User` ke posisi pertama
286. Verifikasi kolom Temporary User: perubahan tampil di preview, `Temporary User` berada di posisi pertama preview tabel
287. Klik `[Save]`
288. Verifikasi kolom Temporary User: tersimpan setelah Save, `Temporary User` berada di posisi pertama tabel
289. Muat ulang halaman (F5)
290. Verifikasi kolom Temporary User: bertahan setelah F5, `Temporary User` tetap berada di posisi pertama tabel
291. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
292. Seret `Temporary Until` ke posisi pertama
293. Verifikasi kolom Temporary Until: perubahan tampil di preview, `Temporary Until` berada di posisi pertama preview tabel
294. Klik `[Save]`
295. Verifikasi kolom Temporary Until: tersimpan setelah Save, `Temporary Until` berada di posisi pertama tabel
296. Muat ulang halaman (F5)
297. Verifikasi kolom Temporary Until: bertahan setelah F5, `Temporary Until` tetap berada di posisi pertama tabel
298. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
299. Seret `TAG` ke posisi pertama
300. Verifikasi kolom TAG: perubahan tampil di preview, `TAG` berada di posisi pertama preview tabel
301. Klik `[Save]`
302. Verifikasi kolom TAG: tersimpan setelah Save, `TAG` berada di posisi pertama tabel
303. Muat ulang halaman (F5)
304. Verifikasi kolom TAG: bertahan setelah F5, `TAG` tetap berada di posisi pertama tabel

### TC-GS-USER-448: Setup Column pin/unpin kelas Curated default tersembunyi

305. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
306. Klik icon pin pada `Activation Status`
307. Verifikasi kolom Activation Status: perubahan tampil di preview, `Activation Status` berstatus pin di preview tabel
308. Klik `[Save]`
309. Scroll tabel secara horizontal
310. Verifikasi kolom Activation Status: tersimpan setelah Save, `Activation Status` membeku (tetap terlihat) saat scroll horizontal
311. Muat ulang halaman (F5)
312. Scroll tabel secara horizontal
313. Verifikasi kolom Activation Status: bertahan setelah F5, `Activation Status` tetap membeku saat scroll horizontal
314. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
315. Klik icon pin pada `Activation Status` untuk Unpin
316. Klik icon pin pada `Temporary User`
317. Verifikasi kolom Temporary User: perubahan tampil di preview, `Temporary User` berstatus pin di preview tabel
318. Klik `[Save]`
319. Scroll tabel secara horizontal
320. Verifikasi kolom Temporary User: tersimpan setelah Save, `Temporary User` membeku (tetap terlihat) saat scroll horizontal
321. Muat ulang halaman (F5)
322. Scroll tabel secara horizontal
323. Verifikasi kolom Temporary User: bertahan setelah F5, `Temporary User` tetap membeku saat scroll horizontal
324. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
325. Klik icon pin pada `Temporary User` untuk Unpin
326. Klik icon pin pada `Temporary Until`
327. Verifikasi kolom Temporary Until: perubahan tampil di preview, `Temporary Until` berstatus pin di preview tabel
328. Klik `[Save]`
329. Scroll tabel secara horizontal
330. Verifikasi kolom Temporary Until: tersimpan setelah Save, `Temporary Until` membeku (tetap terlihat) saat scroll horizontal
331. Muat ulang halaman (F5)
332. Scroll tabel secara horizontal
333. Verifikasi kolom Temporary Until: bertahan setelah F5, `Temporary Until` tetap membeku saat scroll horizontal
334. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
335. Klik icon pin pada `Temporary Until` untuk Unpin
336. Klik icon pin pada `TAG`
337. Verifikasi kolom TAG: perubahan tampil di preview, `TAG` berstatus pin di preview tabel
338. Klik `[Save]`
339. Scroll tabel secara horizontal
340. Verifikasi kolom TAG: tersimpan setelah Save, `TAG` membeku (tetap terlihat) saat scroll horizontal
341. Muat ulang halaman (F5)
342. Scroll tabel secara horizontal
343. Verifikasi kolom TAG: bertahan setelah F5, `TAG` tetap membeku saat scroll horizontal
344. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
345. Klik icon pin pada `TAG` untuk Unpin
346. Klik `[Reset to Default]`
347. Klik `[Save]`
348. Kembalikan viewport ke ukuran awal

### TC-GS-USER-449: Setup Column Reset to Default

349. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
350. Seret `Email` ke posisi pertama
351. Hilangkan centang `Position`
352. Klik `[Save]`
353. Verifikasi konfigurasi yang diubah tersimpan: `Email` berada di posisi pertama tabel dan `Position` tidak tampil
354. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
355. Klik `[Reset to Default]`
356. Klik `[Save]`
357. Verifikasi susunan kolom kembali default: `Active`, `Name`, `Email`, `Position`, `Division`, `Access`, `Employee ID`, `Modified By`, `Last Update` berurutan dan kolom Curated tidak tampil
358. Muat ulang halaman (F5)
359. Verifikasi susunan kolom default bertahan setelah F5

### TC-GS-USER-450: Tutup Setup Column via [✕] membuang perubahan

360. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
361. Hilangkan centang `Division`
362. Seret `Email` ke posisi pertama
363. Klik `[✕]`
364. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir: `Division` tampil dan urutan kolom default

### TC-GS-USER-451: Guard satu kolom tersisa tidak bisa di-uncheck

365. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
366. Hilangkan centang `Active`
367. Hilangkan centang `Email`
368. Hilangkan centang `Position`
369. Hilangkan centang `Division`
370. Hilangkan centang `Access`
371. Hilangkan centang `Employee ID`
372. Hilangkan centang `Modified By`
373. Hilangkan centang `Last Update`
374. Arahkan kursor ke checkbox `Name`
375. Verifikasi checkbox kolom terakhir (`Name`) tetap tampil namun disabled
376. Verifikasi tooltip `At least one column must remain visible.`
377. Klik `[✕]`

### TC-GS-USER-452: Maksimal 3 kolom di-pin

378. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
379. Klik icon pin pada `Active`
380. Klik icon pin pada `Name`
381. Klik icon pin pada `Email`
382. Arahkan kursor ke icon pin `Position` (kolom keempat)
383. Verifikasi icon Pin kolom keempat (`Position`) disabled
384. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
385. Klik `[✕]`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: mock (seluruh API di-mock; layar User List dan Popup Setup Column dijalankan tanpa backend). Urutan TC sumber (441 sampai 452) dipertahankan; dua TC screening (441, 442) berada di awal sebelum aksi yang mengubah konfigurasi kolom.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah `Buka Popup Setup Column lewat header Column Visibility (⋯) lalu Setup Column...` yang berulang (popup menutup sesudah `[Save]` dan `[✕]`; prefix berulang), langkah `Centang kembali` dan `Klik icon pin ... untuk Unpin` yang memulihkan kolom sebelum kolom berikutnya diuji, langkah `Klik [Reset to Default]` dan `Klik [Save]` sesudah TC-GS-USER-444 dan 448 (langkah 153 dan 344), langkah 156 dan 348 (viewport), serta `Klik [✕]` di akhir TC-GS-USER-451 dan 452 (membuang perubahan agar tidak tersimpan).
- Penyusunan blok per kolom: TC-GS-USER-443 mengubah satu kolom per blok. `Centang kembali` kolom sebelumnya dilakukan pada popup yang sama dengan `Hilangkan centang` kolom berikutnya; kolom terakhir dipulihkan di tiga langkah penutup blok.
- TC-GS-USER-446 sampai 448 mengerjakan kolom Curated: pada TC-GS-USER-446 kolom dicentang sampai tampil dan tetap tampil sampai TC-GS-USER-448 selesai, supaya hasil reorder dan pin pada TC-GS-USER-447 dan 448 teramati di tabel; seluruhnya dipulihkan oleh `[Reset to Default]` di akhir TC-GS-USER-448.
- Asersi tambahan (S-03): TC-GS-USER-449 memuat `Verifikasi` konfigurasi yang diubah tersimpan (Email pertama, Position tidak tampil) sebagai anchor bahwa Reset to Default memang mengembalikan sesuatu yang telah diubah.
- Spec melewati sekitar 35 langkah (385 langkah) karena dua belas TC Setup Column berada di satu kelas harness (fungsional, seluruh API di-mock), satu layar, dan satu popup. TC-GS-USER-443 sampai 448 mengulang blok identik per kolom (ubah, Save, F5) untuk 9 kolom Hideable dan 4 kolom Curated, dan tiap blok berdiri sendiri; Expected tiap kolom dipecah per klausa (S-01). Langkah pembuka popup yang berulang merupakan prefix berulang. Pemecahan spec ini (kelas Hideable dan Curated, atau hide/reorder/pin) tidak dilakukan; tim perlu memutuskan bila jumlah langkah dianggap terlalu besar.
- Pembagian TC lintas spec: Search terhadap kolom hidden (TC-GS-USER-419) di spec 071; filter untuk kolom hidden (TC-GS-USER-433) dan kolom Custom Field (TC-GS-USER-463) di spec 073; badge Temporary User (TC-GS-USER-1061) dan nilai Phone (TC-GS-USER-1078) di spec 074; Download terhadap kolom hidden (TC-GS-USER-456) di spec 076; Setup Column pada Modal Changelog User di spec 082.
- Temuan untuk QA:
  - TC-GS-USER-441: daftar kolom Overlay tidak memuat Custom Field aktif (`Blood Type`, `Skills`, `Emergency Phone`, Tabel Pre-setup No. 24), sedangkan TC-GS-USER-463, 1061, dan 1078 menyatakan Custom Field aktif muncul sebagai kolom di Setup Column. Spec 075 memakai payload mock tanpa Custom Field aktif supaya sesuai daftar TC-GS-USER-441.
  - TC-GS-USER-441 dan 442 menyebut item `Setup Column...`, sedangkan TC-GS-USER-1061, 1078, dan 1079 menyebut `[Setup Column]` dan header `Actions (⋯)`. Spec memakai `Setup Column...` dan header `Column Visibility (⋯)`.
  - TC-GS-USER-442: "deskripsi panduan" tidak disebut literal; spec hanya mengasersi deskripsi tampil.
  - TC-GS-USER-443: langkah "uncheck lalu check, Save, refresh F5" menghasilkan konfigurasi akhir sama dengan awal, sehingga Save dan F5 tidak membedakan konfigurasi tersimpan dari default. Spec mengasersi keadaan "tidak tampil" setelah Save dan setelah F5 dan memulihkan kolom dengan centang kembali pada popup berikutnya.
  - TC-GS-USER-446 sampai 448: kolom Curated default tersembunyi, sehingga "uncheck lalu check" tidak dapat dijalankan literal; spec mencentang kolom (tampil), lalu mengasersi tersimpan dan bertahan.
  - TC-GS-USER-445 dan 448: TC tidak menyebut ukuran viewport; tim FE menetapkan viewport yang membuat tabel dapat discroll horizontal. TC juga tidak menyebut posisi kolom yang beku (kiri); spec mengasersi kolom tetap terlihat saat scroll horizontal.
  - TC-GS-USER-449: "ubah urutan dan visibility kolom" tidak menyebut kolom yang diubah; spec memakai `Email` ke posisi pertama dan `Position` di-hide.
  - TC-GS-USER-450: "ubah konfigurasi" tidak menyebut perubahan; spec memakai `Division` di-hide dan `Email` dipindah ke posisi pertama.
  - TC-GS-USER-451: spec meng-uncheck delapan kolom Hideable dan menyisakan `Name`; TC tidak menyebut kolom yang tersisa.
  - TC-GS-USER-452: TC tidak menyebut tiga kolom yang di-pin; spec memakai `Active`, `Name`, `Email`, dengan kolom keempat `Position`.
  - Penyimpanan preferensi kolom (browser atau server) tidak disebut di TC maupun PRD User; Prerequisites menyatakan kedua kemungkinan sehingga mock tidak mengarang endpoint.

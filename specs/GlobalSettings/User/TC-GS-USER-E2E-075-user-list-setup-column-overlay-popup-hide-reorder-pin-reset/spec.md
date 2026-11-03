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
- Kebutuhan mock (Endpoint yang di-mock mengacu `global-settings/user/API/user-crud.yaml`: `POST /v2/iam/users/list`; endpoint profil, izin, Guided Tooltip, Custom Field aktif, dan preferensi kolom tidak ada di `user-crud.yaml` dan ditentukan tim FE di tahap script): respons daftar User (sub-tab Login User) berisi sedikitnya tiga baris yang meniru user Pre-setup (mis. `Dewi Lestari`, `Budi Hartono`, `John Doe`) dengan nilai terisi pada seluruh 13 kolom (`Active`, `Name`, `Email`, `Position`, `Division`, `Access`, `Employee ID`, `Modified By`, `Last Update`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`); respons Custom Field aktif kosong, sehingga Overlay dan Popup memuat 13 kolom itu saja (TC-GS-USER-441); respons lain yang dibutuhkan layar User List (profil, izin, Guided Tooltip) memakai payload default. Bila FE menyimpan preferensi kolom lewat API, endpoint-nya ikut di-mock; bila disimpan di sisi klien, tidak ada kebutuhan mock tambahan.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22 dan Custom Field aktif No. 24) dirujuk oleh payload mock saja; spec tidak membaca atau mengubah data backend.
- Data Dinamis: tidak ada.
- Preferensi kolom (visibilitas, urutan, pin) bertahan setelah `[Save]` dan setelah muat ulang halaman (F5) pada konteks browser yang sama (`foundation/process/prd-process/prd-conventions.md` §9.3); mock tetap aktif sesudah muat ulang halaman.
- State yang diubah dan dipulihkan: konfigurasi kolom User List (visibilitas, urutan, pin) dikembalikan ke default lewat `[Reset to Default]` dan `[Save]` (langkah 152 sampai 154, 343 sampai 346, dan di TC-GS-USER-449); viewport disempitkan (langkah 155) dan dikembalikan ke ukuran awal (langkah 347). Hook `after` sebagai cadangan mengembalikan konfigurasi kolom ke default (penghapusan preferensi kolom User List di browser; mekanisme disediakan tim FE/BE) dan viewport ke ukuran awal.
- Halaman Global Settings > User > User List (sub-tab Login User) dibuka hook `beforeEach` suite; tidak ada login pada mode mock.
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: drag and drop item kolom pada Popup Setup Column; mengatur viewport; scroll horizontal tabel; hover untuk membaca tooltip; muat ulang halaman dengan mock tetap aktif; membaca dan menghapus preferensi kolom di penyimpanan browser.

## Test Steps

### TC-GS-USER-441: Screening Overlay Column Visibility

1. Klik header kolom Column Visibility (⋯)
2. Verifikasi Overlay daftar kolom memuat `Active`, `Name`, `Email`, `Position`, `Division`, `Access`, `Employee ID`, `Modified By`, `Last Update`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG` berurutan
3. Verifikasi kolom Hideable (`Active`, `Name`, `Email`, `Position`, `Division`, `Access`, `Employee ID`, `Modified By`, `Last Update`) tercentang dan enabled
4. Verifikasi drag handle tersedia pada tiap kolom
5. Verifikasi item `Setup Column...` tersedia di Overlay

### TC-GS-USER-442: Screening Popup Setup Column

6. Klik item `Setup Column...`
7. Verifikasi Header: Title `Setup Column`
8. Verifikasi Header: deskripsi panduan tampil
9. Verifikasi Header: icon `[✕]` tampil
10. Verifikasi Body: daftar kolom dengan checkbox tampil
11. Verifikasi Body: drag handle tampil pada tiap kolom
12. Verifikasi Body: icon Pin tampil pada tiap kolom
13. Verifikasi Body: preview tabel tampil
14. Verifikasi Footer: tombol `[Reset to Default]` dan `[Save]` tampil
15. Verifikasi Footer: tidak ada tombol `[Cancel]`

### TC-GS-USER-443: Setup Column hide/unhide kelas Hideable default tampil

16. Hilangkan centang `Active`
17. Verifikasi kolom Active: perubahan tampil di preview, `Active` tidak tampil di preview tabel
18. Klik `[Save]`
19. Verifikasi kolom Active: tersimpan setelah Save, `Active` tidak tampil di tabel
20. Muat ulang halaman (F5)
21. Verifikasi kolom Active: bertahan setelah F5, `Active` tetap tidak tampil di tabel
22. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
23. Centang kembali `Active`
24. Hilangkan centang `Name`
25. Verifikasi kolom Name: perubahan tampil di preview, `Name` tidak tampil di preview tabel
26. Klik `[Save]`
27. Verifikasi kolom Name: tersimpan setelah Save, `Name` tidak tampil di tabel
28. Muat ulang halaman (F5)
29. Verifikasi kolom Name: bertahan setelah F5, `Name` tetap tidak tampil di tabel
30. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
31. Centang kembali `Name`
32. Hilangkan centang `Email`
33. Verifikasi kolom Email: perubahan tampil di preview, `Email` tidak tampil di preview tabel
34. Klik `[Save]`
35. Verifikasi kolom Email: tersimpan setelah Save, `Email` tidak tampil di tabel
36. Muat ulang halaman (F5)
37. Verifikasi kolom Email: bertahan setelah F5, `Email` tetap tidak tampil di tabel
38. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
39. Centang kembali `Email`
40. Hilangkan centang `Position`
41. Verifikasi kolom Position: perubahan tampil di preview, `Position` tidak tampil di preview tabel
42. Klik `[Save]`
43. Verifikasi kolom Position: tersimpan setelah Save, `Position` tidak tampil di tabel
44. Muat ulang halaman (F5)
45. Verifikasi kolom Position: bertahan setelah F5, `Position` tetap tidak tampil di tabel
46. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
47. Centang kembali `Position`
48. Hilangkan centang `Division`
49. Verifikasi kolom Division: perubahan tampil di preview, `Division` tidak tampil di preview tabel
50. Klik `[Save]`
51. Verifikasi kolom Division: tersimpan setelah Save, `Division` tidak tampil di tabel
52. Muat ulang halaman (F5)
53. Verifikasi kolom Division: bertahan setelah F5, `Division` tetap tidak tampil di tabel
54. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
55. Centang kembali `Division`
56. Hilangkan centang `Access`
57. Verifikasi kolom Access: perubahan tampil di preview, `Access` tidak tampil di preview tabel
58. Klik `[Save]`
59. Verifikasi kolom Access: tersimpan setelah Save, `Access` tidak tampil di tabel
60. Muat ulang halaman (F5)
61. Verifikasi kolom Access: bertahan setelah F5, `Access` tetap tidak tampil di tabel
62. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
63. Centang kembali `Access`
64. Hilangkan centang `Employee ID`
65. Verifikasi kolom Employee ID: perubahan tampil di preview, `Employee ID` tidak tampil di preview tabel
66. Klik `[Save]`
67. Verifikasi kolom Employee ID: tersimpan setelah Save, `Employee ID` tidak tampil di tabel
68. Muat ulang halaman (F5)
69. Verifikasi kolom Employee ID: bertahan setelah F5, `Employee ID` tetap tidak tampil di tabel
70. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
71. Centang kembali `Employee ID`
72. Hilangkan centang `Modified By`
73. Verifikasi kolom Modified By: perubahan tampil di preview, `Modified By` tidak tampil di preview tabel
74. Klik `[Save]`
75. Verifikasi kolom Modified By: tersimpan setelah Save, `Modified By` tidak tampil di tabel
76. Muat ulang halaman (F5)
77. Verifikasi kolom Modified By: bertahan setelah F5, `Modified By` tetap tidak tampil di tabel
78. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
79. Centang kembali `Modified By`
80. Hilangkan centang `Last Update`
81. Verifikasi kolom Last Update: perubahan tampil di preview, `Last Update` tidak tampil di preview tabel
82. Klik `[Save]`
83. Verifikasi kolom Last Update: tersimpan setelah Save, `Last Update` tidak tampil di tabel
84. Muat ulang halaman (F5)
85. Verifikasi kolom Last Update: bertahan setelah F5, `Last Update` tetap tidak tampil di tabel
86. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
87. Centang kembali `Last Update`
88. Klik `[Save]`

### TC-GS-USER-444: Setup Column drag reorder kelas Hideable default tampil

89. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
90. Seret `Active` ke posisi pertama
91. Verifikasi kolom Active: perubahan tampil di preview, `Active` berada di posisi pertama preview tabel
92. Klik `[Save]`
93. Verifikasi kolom Active: tersimpan setelah Save, `Active` berada di posisi pertama tabel
94. Muat ulang halaman (F5)
95. Verifikasi kolom Active: bertahan setelah F5, `Active` tetap berada di posisi pertama tabel
96. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
97. Seret `Name` ke posisi pertama
98. Verifikasi kolom Name: perubahan tampil di preview, `Name` berada di posisi pertama preview tabel
99. Klik `[Save]`
100. Verifikasi kolom Name: tersimpan setelah Save, `Name` berada di posisi pertama tabel
101. Muat ulang halaman (F5)
102. Verifikasi kolom Name: bertahan setelah F5, `Name` tetap berada di posisi pertama tabel
103. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
104. Seret `Email` ke posisi pertama
105. Verifikasi kolom Email: perubahan tampil di preview, `Email` berada di posisi pertama preview tabel
106. Klik `[Save]`
107. Verifikasi kolom Email: tersimpan setelah Save, `Email` berada di posisi pertama tabel
108. Muat ulang halaman (F5)
109. Verifikasi kolom Email: bertahan setelah F5, `Email` tetap berada di posisi pertama tabel
110. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
111. Seret `Position` ke posisi pertama
112. Verifikasi kolom Position: perubahan tampil di preview, `Position` berada di posisi pertama preview tabel
113. Klik `[Save]`
114. Verifikasi kolom Position: tersimpan setelah Save, `Position` berada di posisi pertama tabel
115. Muat ulang halaman (F5)
116. Verifikasi kolom Position: bertahan setelah F5, `Position` tetap berada di posisi pertama tabel
117. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
118. Seret `Division` ke posisi pertama
119. Verifikasi kolom Division: perubahan tampil di preview, `Division` berada di posisi pertama preview tabel
120. Klik `[Save]`
121. Verifikasi kolom Division: tersimpan setelah Save, `Division` berada di posisi pertama tabel
122. Muat ulang halaman (F5)
123. Verifikasi kolom Division: bertahan setelah F5, `Division` tetap berada di posisi pertama tabel
124. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
125. Seret `Access` ke posisi pertama
126. Verifikasi kolom Access: perubahan tampil di preview, `Access` berada di posisi pertama preview tabel
127. Klik `[Save]`
128. Verifikasi kolom Access: tersimpan setelah Save, `Access` berada di posisi pertama tabel
129. Muat ulang halaman (F5)
130. Verifikasi kolom Access: bertahan setelah F5, `Access` tetap berada di posisi pertama tabel
131. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
132. Seret `Employee ID` ke posisi pertama
133. Verifikasi kolom Employee ID: perubahan tampil di preview, `Employee ID` berada di posisi pertama preview tabel
134. Klik `[Save]`
135. Verifikasi kolom Employee ID: tersimpan setelah Save, `Employee ID` berada di posisi pertama tabel
136. Muat ulang halaman (F5)
137. Verifikasi kolom Employee ID: bertahan setelah F5, `Employee ID` tetap berada di posisi pertama tabel
138. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
139. Seret `Modified By` ke posisi pertama
140. Verifikasi kolom Modified By: perubahan tampil di preview, `Modified By` berada di posisi pertama preview tabel
141. Klik `[Save]`
142. Verifikasi kolom Modified By: tersimpan setelah Save, `Modified By` berada di posisi pertama tabel
143. Muat ulang halaman (F5)
144. Verifikasi kolom Modified By: bertahan setelah F5, `Modified By` tetap berada di posisi pertama tabel
145. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
146. Seret `Last Update` ke posisi pertama
147. Verifikasi kolom Last Update: perubahan tampil di preview, `Last Update` berada di posisi pertama preview tabel
148. Klik `[Save]`
149. Verifikasi kolom Last Update: tersimpan setelah Save, `Last Update` berada di posisi pertama tabel
150. Muat ulang halaman (F5)
151. Verifikasi kolom Last Update: bertahan setelah F5, `Last Update` tetap berada di posisi pertama tabel
152. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
153. Klik `[Reset to Default]`
154. Klik `[Save]`

### TC-GS-USER-445: Setup Column pin/unpin kelas Hideable default tampil

155. Sempitkan viewport sehingga tabel dapat di-scroll horizontal
156. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
157. Klik icon pin pada `Active`
158. Verifikasi kolom Active: perubahan tampil di preview, `Active` berstatus pin di preview tabel
159. Klik `[Save]`
160. Scroll tabel secara horizontal
161. Verifikasi kolom Active: tersimpan setelah Save, `Active` membeku (tetap terlihat) saat scroll horizontal
162. Muat ulang halaman (F5)
163. Scroll tabel secara horizontal
164. Verifikasi kolom Active: bertahan setelah F5, `Active` tetap membeku saat scroll horizontal
165. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
166. Klik icon pin pada `Active` untuk Unpin
167. Klik icon pin pada `Name`
168. Verifikasi kolom Name: perubahan tampil di preview, `Name` berstatus pin di preview tabel
169. Klik `[Save]`
170. Scroll tabel secara horizontal
171. Verifikasi kolom Name: tersimpan setelah Save, `Name` membeku (tetap terlihat) saat scroll horizontal
172. Muat ulang halaman (F5)
173. Scroll tabel secara horizontal
174. Verifikasi kolom Name: bertahan setelah F5, `Name` tetap membeku saat scroll horizontal
175. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
176. Klik icon pin pada `Name` untuk Unpin
177. Klik icon pin pada `Email`
178. Verifikasi kolom Email: perubahan tampil di preview, `Email` berstatus pin di preview tabel
179. Klik `[Save]`
180. Scroll tabel secara horizontal
181. Verifikasi kolom Email: tersimpan setelah Save, `Email` membeku (tetap terlihat) saat scroll horizontal
182. Muat ulang halaman (F5)
183. Scroll tabel secara horizontal
184. Verifikasi kolom Email: bertahan setelah F5, `Email` tetap membeku saat scroll horizontal
185. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
186. Klik icon pin pada `Email` untuk Unpin
187. Klik icon pin pada `Position`
188. Verifikasi kolom Position: perubahan tampil di preview, `Position` berstatus pin di preview tabel
189. Klik `[Save]`
190. Scroll tabel secara horizontal
191. Verifikasi kolom Position: tersimpan setelah Save, `Position` membeku (tetap terlihat) saat scroll horizontal
192. Muat ulang halaman (F5)
193. Scroll tabel secara horizontal
194. Verifikasi kolom Position: bertahan setelah F5, `Position` tetap membeku saat scroll horizontal
195. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
196. Klik icon pin pada `Position` untuk Unpin
197. Klik icon pin pada `Division`
198. Verifikasi kolom Division: perubahan tampil di preview, `Division` berstatus pin di preview tabel
199. Klik `[Save]`
200. Scroll tabel secara horizontal
201. Verifikasi kolom Division: tersimpan setelah Save, `Division` membeku (tetap terlihat) saat scroll horizontal
202. Muat ulang halaman (F5)
203. Scroll tabel secara horizontal
204. Verifikasi kolom Division: bertahan setelah F5, `Division` tetap membeku saat scroll horizontal
205. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
206. Klik icon pin pada `Division` untuk Unpin
207. Klik icon pin pada `Access`
208. Verifikasi kolom Access: perubahan tampil di preview, `Access` berstatus pin di preview tabel
209. Klik `[Save]`
210. Scroll tabel secara horizontal
211. Verifikasi kolom Access: tersimpan setelah Save, `Access` membeku (tetap terlihat) saat scroll horizontal
212. Muat ulang halaman (F5)
213. Scroll tabel secara horizontal
214. Verifikasi kolom Access: bertahan setelah F5, `Access` tetap membeku saat scroll horizontal
215. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
216. Klik icon pin pada `Access` untuk Unpin
217. Klik icon pin pada `Employee ID`
218. Verifikasi kolom Employee ID: perubahan tampil di preview, `Employee ID` berstatus pin di preview tabel
219. Klik `[Save]`
220. Scroll tabel secara horizontal
221. Verifikasi kolom Employee ID: tersimpan setelah Save, `Employee ID` membeku (tetap terlihat) saat scroll horizontal
222. Muat ulang halaman (F5)
223. Scroll tabel secara horizontal
224. Verifikasi kolom Employee ID: bertahan setelah F5, `Employee ID` tetap membeku saat scroll horizontal
225. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
226. Klik icon pin pada `Employee ID` untuk Unpin
227. Klik icon pin pada `Modified By`
228. Verifikasi kolom Modified By: perubahan tampil di preview, `Modified By` berstatus pin di preview tabel
229. Klik `[Save]`
230. Scroll tabel secara horizontal
231. Verifikasi kolom Modified By: tersimpan setelah Save, `Modified By` membeku (tetap terlihat) saat scroll horizontal
232. Muat ulang halaman (F5)
233. Scroll tabel secara horizontal
234. Verifikasi kolom Modified By: bertahan setelah F5, `Modified By` tetap membeku saat scroll horizontal
235. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
236. Klik icon pin pada `Modified By` untuk Unpin
237. Klik icon pin pada `Last Update`
238. Verifikasi kolom Last Update: perubahan tampil di preview, `Last Update` berstatus pin di preview tabel
239. Klik `[Save]`
240. Scroll tabel secara horizontal
241. Verifikasi kolom Last Update: tersimpan setelah Save, `Last Update` membeku (tetap terlihat) saat scroll horizontal
242. Muat ulang halaman (F5)
243. Scroll tabel secara horizontal
244. Verifikasi kolom Last Update: bertahan setelah F5, `Last Update` tetap membeku saat scroll horizontal
245. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
246. Klik icon pin pada `Last Update` untuk Unpin
247. Klik `[Save]`

### TC-GS-USER-446: Setup Column hide/unhide kelas Curated default tersembunyi

248. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
249. Centang `Activation Status` (default tidak tercentang)
250. Verifikasi kolom Activation Status: perubahan tampil di preview, `Activation Status` tampil di preview tabel
251. Klik `[Save]`
252. Verifikasi kolom Activation Status: tersimpan setelah Save, `Activation Status` tampil di tabel
253. Muat ulang halaman (F5)
254. Verifikasi kolom Activation Status: bertahan setelah F5, `Activation Status` tetap tampil di tabel
255. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
256. Centang `Temporary User` (default tidak tercentang)
257. Verifikasi kolom Temporary User: perubahan tampil di preview, `Temporary User` tampil di preview tabel
258. Klik `[Save]`
259. Verifikasi kolom Temporary User: tersimpan setelah Save, `Temporary User` tampil di tabel
260. Muat ulang halaman (F5)
261. Verifikasi kolom Temporary User: bertahan setelah F5, `Temporary User` tetap tampil di tabel
262. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
263. Centang `Temporary Until` (default tidak tercentang)
264. Verifikasi kolom Temporary Until: perubahan tampil di preview, `Temporary Until` tampil di preview tabel
265. Klik `[Save]`
266. Verifikasi kolom Temporary Until: tersimpan setelah Save, `Temporary Until` tampil di tabel
267. Muat ulang halaman (F5)
268. Verifikasi kolom Temporary Until: bertahan setelah F5, `Temporary Until` tetap tampil di tabel
269. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
270. Centang `TAG` (default tidak tercentang)
271. Verifikasi kolom TAG: perubahan tampil di preview, `TAG` tampil di preview tabel
272. Klik `[Save]`
273. Verifikasi kolom TAG: tersimpan setelah Save, `TAG` tampil di tabel
274. Muat ulang halaman (F5)
275. Verifikasi kolom TAG: bertahan setelah F5, `TAG` tetap tampil di tabel

### TC-GS-USER-447: Setup Column drag reorder kelas Curated default tersembunyi

276. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
277. Seret `Activation Status` ke posisi pertama
278. Verifikasi kolom Activation Status: perubahan tampil di preview, `Activation Status` berada di posisi pertama preview tabel
279. Klik `[Save]`
280. Verifikasi kolom Activation Status: tersimpan setelah Save, `Activation Status` berada di posisi pertama tabel
281. Muat ulang halaman (F5)
282. Verifikasi kolom Activation Status: bertahan setelah F5, `Activation Status` tetap berada di posisi pertama tabel
283. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
284. Seret `Temporary User` ke posisi pertama
285. Verifikasi kolom Temporary User: perubahan tampil di preview, `Temporary User` berada di posisi pertama preview tabel
286. Klik `[Save]`
287. Verifikasi kolom Temporary User: tersimpan setelah Save, `Temporary User` berada di posisi pertama tabel
288. Muat ulang halaman (F5)
289. Verifikasi kolom Temporary User: bertahan setelah F5, `Temporary User` tetap berada di posisi pertama tabel
290. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
291. Seret `Temporary Until` ke posisi pertama
292. Verifikasi kolom Temporary Until: perubahan tampil di preview, `Temporary Until` berada di posisi pertama preview tabel
293. Klik `[Save]`
294. Verifikasi kolom Temporary Until: tersimpan setelah Save, `Temporary Until` berada di posisi pertama tabel
295. Muat ulang halaman (F5)
296. Verifikasi kolom Temporary Until: bertahan setelah F5, `Temporary Until` tetap berada di posisi pertama tabel
297. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
298. Seret `TAG` ke posisi pertama
299. Verifikasi kolom TAG: perubahan tampil di preview, `TAG` berada di posisi pertama preview tabel
300. Klik `[Save]`
301. Verifikasi kolom TAG: tersimpan setelah Save, `TAG` berada di posisi pertama tabel
302. Muat ulang halaman (F5)
303. Verifikasi kolom TAG: bertahan setelah F5, `TAG` tetap berada di posisi pertama tabel

### TC-GS-USER-448: Setup Column pin/unpin kelas Curated default tersembunyi

304. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
305. Klik icon pin pada `Activation Status`
306. Verifikasi kolom Activation Status: perubahan tampil di preview, `Activation Status` berstatus pin di preview tabel
307. Klik `[Save]`
308. Scroll tabel secara horizontal
309. Verifikasi kolom Activation Status: tersimpan setelah Save, `Activation Status` membeku (tetap terlihat) saat scroll horizontal
310. Muat ulang halaman (F5)
311. Scroll tabel secara horizontal
312. Verifikasi kolom Activation Status: bertahan setelah F5, `Activation Status` tetap membeku saat scroll horizontal
313. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
314. Klik icon pin pada `Activation Status` untuk Unpin
315. Klik icon pin pada `Temporary User`
316. Verifikasi kolom Temporary User: perubahan tampil di preview, `Temporary User` berstatus pin di preview tabel
317. Klik `[Save]`
318. Scroll tabel secara horizontal
319. Verifikasi kolom Temporary User: tersimpan setelah Save, `Temporary User` membeku (tetap terlihat) saat scroll horizontal
320. Muat ulang halaman (F5)
321. Scroll tabel secara horizontal
322. Verifikasi kolom Temporary User: bertahan setelah F5, `Temporary User` tetap membeku saat scroll horizontal
323. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
324. Klik icon pin pada `Temporary User` untuk Unpin
325. Klik icon pin pada `Temporary Until`
326. Verifikasi kolom Temporary Until: perubahan tampil di preview, `Temporary Until` berstatus pin di preview tabel
327. Klik `[Save]`
328. Scroll tabel secara horizontal
329. Verifikasi kolom Temporary Until: tersimpan setelah Save, `Temporary Until` membeku (tetap terlihat) saat scroll horizontal
330. Muat ulang halaman (F5)
331. Scroll tabel secara horizontal
332. Verifikasi kolom Temporary Until: bertahan setelah F5, `Temporary Until` tetap membeku saat scroll horizontal
333. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
334. Klik icon pin pada `Temporary Until` untuk Unpin
335. Klik icon pin pada `TAG`
336. Verifikasi kolom TAG: perubahan tampil di preview, `TAG` berstatus pin di preview tabel
337. Klik `[Save]`
338. Scroll tabel secara horizontal
339. Verifikasi kolom TAG: tersimpan setelah Save, `TAG` membeku (tetap terlihat) saat scroll horizontal
340. Muat ulang halaman (F5)
341. Scroll tabel secara horizontal
342. Verifikasi kolom TAG: bertahan setelah F5, `TAG` tetap membeku saat scroll horizontal
343. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
344. Klik icon pin pada `TAG` untuk Unpin
345. Klik `[Reset to Default]`
346. Klik `[Save]`
347. Kembalikan viewport ke ukuran awal

### TC-GS-USER-449: Setup Column Reset to Default

348. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
349. Seret `Email` ke posisi pertama
350. Hilangkan centang `Position`
351. Klik `[Save]`
352. Verifikasi konfigurasi yang diubah tersimpan: `Email` berada di posisi pertama tabel dan `Position` tidak tampil
353. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
354. Klik `[Reset to Default]`
355. Klik `[Save]`
356. Verifikasi susunan kolom kembali default: `Active`, `Name`, `Email`, `Position`, `Division`, `Access`, `Employee ID`, `Modified By`, `Last Update` berurutan dan kolom Curated tidak tampil
357. Muat ulang halaman (F5)
358. Verifikasi susunan kolom default bertahan setelah F5

### TC-GS-USER-450: Tutup Setup Column via [✕] membuang perubahan

359. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
360. Hilangkan centang `Division`
361. Seret `Email` ke posisi pertama
362. Klik `[✕]`
363. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir: `Division` tampil dan urutan kolom default

### TC-GS-USER-451: Guard satu kolom tersisa tidak bisa di-uncheck

364. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
365. Hilangkan centang `Active`
366. Hilangkan centang `Email`
367. Hilangkan centang `Position`
368. Hilangkan centang `Division`
369. Hilangkan centang `Access`
370. Hilangkan centang `Employee ID`
371. Hilangkan centang `Modified By`
372. Hilangkan centang `Last Update`
373. Arahkan kursor ke checkbox `Name`
374. Verifikasi checkbox kolom terakhir (`Name`) tetap tampil namun disabled
375. Verifikasi tooltip `At least one column must remain visible.`
376. Klik `[✕]`

### TC-GS-USER-452: Maksimal 3 kolom di-pin

377. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
378. Klik icon pin pada `Active`
379. Klik icon pin pada `Name`
380. Klik icon pin pada `Email`
381. Arahkan kursor ke icon pin `Position` (kolom keempat)
382. Verifikasi icon Pin kolom keempat (`Position`) disabled
383. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
384. Klik `[✕]`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: mock (seluruh API di-mock; layar User List dan Popup Setup Column dijalankan tanpa backend). Urutan TC sumber (441 sampai 452) dipertahankan; dua TC screening (441, 442) berada di awal sebelum aksi yang mengubah konfigurasi kolom.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah `Buka Popup Setup Column lewat header Column Visibility (⋯) lalu Setup Column...` yang berulang (popup menutup sesudah `[Save]` dan `[✕]`; prefix berulang), langkah `Centang kembali` dan `Klik icon pin ... untuk Unpin` yang memulihkan kolom sebelum kolom berikutnya diuji, langkah `Klik [Reset to Default]` dan `Klik [Save]` sesudah TC-GS-USER-444 dan 448 (langkah 152 sampai 154 dan 343 sampai 346), langkah 155 dan 347 (viewport), serta `Klik [✕]` di akhir TC-GS-USER-451 dan 452 (membuang perubahan agar tidak tersimpan).
- Penyusunan blok per kolom: TC-GS-USER-443 mengubah satu kolom per blok. `Centang kembali` kolom sebelumnya dilakukan pada popup yang sama dengan `Hilangkan centang` kolom berikutnya; kolom terakhir dipulihkan di tiga langkah penutup blok.
- TC-GS-USER-446 sampai 448 mengerjakan kolom Curated: pada TC-GS-USER-446 kolom dicentang sampai tampil dan tetap tampil sampai TC-GS-USER-448 selesai, supaya hasil reorder dan pin pada TC-GS-USER-447 dan 448 teramati di tabel; seluruhnya dipulihkan oleh `[Reset to Default]` di akhir TC-GS-USER-448.
- Asersi tambahan (S-03): TC-GS-USER-449 memuat `Verifikasi` konfigurasi yang diubah tersimpan (Email pertama, Position tidak tampil) sebagai anchor bahwa Reset to Default memang mengembalikan sesuatu yang telah diubah.
- Spec melewati sekitar 35 langkah (384 langkah) karena dua belas TC Setup Column berada di satu kelas harness (fungsional, seluruh API di-mock), satu layar, dan satu popup. TC-GS-USER-443 sampai 448 mengulang blok identik per kolom (ubah, Save, F5) untuk 9 kolom Hideable dan 4 kolom Curated, dan tiap blok berdiri sendiri; Expected tiap kolom dipecah per klausa (S-01). Langkah pembuka popup yang berulang merupakan prefix berulang. Pemecahan spec ini (kelas Hideable dan Curated, atau hide/reorder/pin) tidak dilakukan; tim perlu memutuskan bila jumlah langkah dianggap terlalu besar.
- Pembagian TC lintas spec: Search terhadap kolom hidden (TC-GS-USER-419) di spec 071; filter untuk kolom hidden (TC-GS-USER-433) dan kolom Custom Field (TC-GS-USER-463) di spec 073; badge Temporary User (TC-GS-USER-1061) dan nilai Phone (TC-GS-USER-1078) di spec 074; Download terhadap kolom hidden (TC-GS-USER-456) di spec 076; Setup Column pada Modal Changelog User di spec 082.
- Overlay TC-GS-USER-441: Expected b hanya menyebut kolom Hideable (checked dan enabled) dan drag handle; asersi kolom Curated tidak tercentang tidak ditulis (bukan klausa TC saat ini).
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

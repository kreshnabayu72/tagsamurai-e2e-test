---
id: TC-GS-USER-E2E-112-tab-non-login-user-detail-setup-column-overlay-popup-hide-reorder-pin-reset
title: "Tab Non-Login User Detail: Setup Column (overlay, popup, hide, reorder, pin, reset, guard)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-697
  - TC-GS-USER-698
  - TC-GS-USER-699
  - TC-GS-USER-700
  - TC-GS-USER-701
  - TC-GS-USER-702
  - TC-GS-USER-703
  - TC-GS-USER-704
  - TC-GS-USER-705
  - TC-GS-USER-706
  - TC-GS-USER-707
  - TC-GS-USER-708
coverage:
  web: automated
---

# Tab Non-Login User Detail: Setup Column (overlay, popup, hide, reorder, pin, reset, guard)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup; state yang diubah adalah preferensi Setup Column Tab Non-Login User (dipulihkan).
- Akun: Total Control, `Siti Nurhaliza`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Master Data Position (`Finance Manager`, `Staff`, `Supervisor`, `Internal Auditor`) dan Division (`Finance`, `General Affairs`, `Legal`) Pre-setup No. 22 dan 23 sebagai nilai seed.
- Data Dinamis, holder: Login User milik spec `Ahmad Fauzi {runId}-112` (email `ahmadfauzi+{runId}-112@qwertysystem.net`, status Activated, Access Global Settings) sebagai Represented By seluruh Non-Login User di bawah. Holder milik spec dipakai, bukan `Ahmad Fauzi` Pre-setup (Tabel Data Uji Pre-setup No. 13) beserta `Agus Prasetyo` dan `Lina Marlina` Pre-setup (No. 21), karena S-06 melarang mengubah data Pre-setup bersama dan S-11 menuntut data dengan lebih dari satu halaman serta sedikitnya dua nilai distinct pada kolom yang diuji.
- Data Dinamis, 12 Non-Login User milik spec (Represented By = `Ahmad Fauzi {runId}-112`), di-seed di hook `before`. Tabel memuat 12 baris: halaman 1 berisi 10 baris dan total 2 halaman. Nilai Name, Email, dan Employee ID bersuffix `{runId}-112`; Last Update seluruh baris = waktu seeding; `{U1}` dan `{U2}` pada kolom Temporary Until adalah tanggal hari uji + 30 hari dan hari uji + 60 hari. Tidak ada `Verifikasi` spec ini yang bergantung pada nilai sel; tabel berfungsi sebagai konteks kolom dan preview Setup Column.

  | Name | Email | Employee ID | Position | Division | Active | Temporary User | Temporary Until |
  |---|---|---|---|---|---|---|---|
  | `Agus Prasetyo {runId}-112` | `nlu01+{runId}-112@qwertysystem.net` | `EMP-AGS-{runId}-112` | Finance Manager | Finance | Active | No | kosong |
  | `Bagas Santoso {runId}-112` | `nlu02+{runId}-112@qwertysystem.net` | `EMP-BGS-{runId}-112` | Staff | General Affairs | Active | No | kosong |
  | `Citra Dewanti {runId}-112` | `nlu03+{runId}-112@qwertysystem.net` | `EMP-CTR-{runId}-112` | Supervisor | Finance | Active | Yes | `{U1}` (hari uji + 30 hari) |
  | `Dimas Pranoto {runId}-112` | `nlu04+{runId}-112@qwertysystem.net` | `EMP-DMS-{runId}-112` | Staff | General Affairs | Active | No | kosong |
  | `Eka Wulandari {runId}-112` | `nlu05+{runId}-112@qwertysystem.net` | `EMP-EKA-{runId}-112` | Finance Manager | Legal | Active | No | kosong |
  | `Fitri Handayani {runId}-112` | `nlu06+{runId}-112@qwertysystem.net` | `EMP-FTR-{runId}-112` | Internal Auditor | Finance | Active | Yes | `{U2}` (hari uji + 60 hari) |
  | `Galih Permadi {runId}-112` | `nlu07+{runId}-112@qwertysystem.net` | `EMP-GLH-{runId}-112` | Staff | Legal | Active | No | kosong |
  | `Hana Kusuma {runId}-112` | `nlu08+{runId}-112@qwertysystem.net` | `EMP-HNA-{runId}-112` | Supervisor | General Affairs | Active | No | kosong |
  | `Lina Marlina {runId}-112` | `nlu09+{runId}-112@qwertysystem.net` | kosong | kosong | Legal | Inactive | No | kosong |
  | `Nadia Rahma {runId}-112` | `nlu10+{runId}-112@qwertysystem.net` | `EMP-NDR-{runId}-112` | Staff | Finance | Active | No | kosong |
  | `Rizky Fadillah {runId}-112` | `nlu11+{runId}-112@qwertysystem.net` | `EMP-RZK-{runId}-112` | Finance Manager | General Affairs | Inactive | No | kosong |
  | `Wahyu Hidayat {runId}-112` | `nlu12+{runId}-112@qwertysystem.net` | `EMP-WHY-{runId}-112` | Supervisor | Legal | Active | No | kosong |

- Kemampuan teknis (disediakan tim FE/BE; endpoint ditentukan tim FE di tahap script): seeding Login User holder dan Non-Login User dengan Represented By = holder lewat API di hook `before`; cleanup di hook `after` menghapus Non-Login User lalu holder lewat API tanpa berasumsi seeding berhasil penuh. Seeding menambah 13 user pada hitungan Master Data Count Limit gabungan Login + Non-Login User; nilai limit environment cukup besar untuk itu.
- Kolom Tab Non-Login User (PRD user.md §4.1.4): Hideable default visible `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active`, `Last Update`; Curated default hidden `Temporary User`, `Temporary Until`. Tidak ada kolom Locked; guard hanya satu kolom visible tersisa tidak dapat di-uncheck.
- Preferensi kolom (visibilitas, urutan, pin) tersimpan di browser per tabel (PRD prd-conventions.md §9.3, `localStorage`) dan menjadi permanen setelah `[Save]`; "muat ulang halaman (F5)" dilakukan pada konteks browser yang sama supaya penyimpanan browser tetap ada. Sesudah F5, spec mengklik Tab `Non-Login User` karena tab aktif saat Detail dibuka adalah Tab Role (PRD user.md, tab pertama) dan retensi tab setelah F5 tidak didefinisikan.
- Data uji per TC: kolom Hideable `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active`, `Last Update` (TC-GS-USER-699, 700, 701); kolom Curated `Temporary User`, `Temporary Until` (TC-GS-USER-702, 703, 704); TC-GS-USER-705 menggeser `Division` ke posisi pertama dan menyembunyikan `Email`; TC-GS-USER-706 menyembunyikan `Email`; TC-GS-USER-707 menyisakan `Name`; TC-GS-USER-708 mem-pin `Name`, `Email`, `Employee ID` lalu memeriksa icon Pin `Position`.
- Viewport: lebar konten tabel harus melebihi lebar viewport (overflow horizontal) supaya scroll horizontal pada TC-GS-USER-701 dan 704 teramati. Viewport disempitkan di langkah 209 dan dikembalikan ke ukuran awal di langkah 331; ukuran viewport dipilih tim FE karena TC tidak menyebutnya.
- State yang diubah dan dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): preferensi Setup Column Tab Non-Login User dikembalikan ke default (`Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active`, `Last Update` tampil berurutan, tanpa pin, kolom curated tersembunyi) lewat `[Reset to Default]` dan `[Save]` atau penghapusan preferensi kolom di browser; viewport dikembalikan ke ukuran awal. Spec sendiri memulihkan lewat `[Reset to Default]` pada TC-GS-USER-705 (langkah terakhir).
- Date Format General Settings default environment (`DD/MM/YY`); spec tidak mengubahnya.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`). Spec tidak mengubah data Pre-setup bersama (S-06).
- Kemampuan teknis: drag and drop item kolom pada Popup Setup Column; mengarahkan kursor ke checkbox dan icon Pin disabled untuk membaca tooltip; mengatur viewport; scroll horizontal tabel; membaca dan menghapus preferensi kolom di penyimpanan browser.

## Test Steps

1. Klik icon Search, ketik `Ahmad Fauzi {runId}-112`, tekan Enter
2. Klik Name `Ahmad Fauzi {runId}-112` di User List
3. Klik Tab `Non-Login User`

### TC-GS-USER-697: Screening Overlay Column Visibility

4. Klik header kolom Column Visibility (⋯)
5. Verifikasi overlay memuat daftar kolom berurutan: `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active`, `Last Update`, `Temporary User`, `Temporary Until`
6. Verifikasi kolom Hideable (`Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active`, `Last Update`) tercentang dan enabled
7. Verifikasi kolom Curated (`Temporary User`, `Temporary Until`) tidak tercentang dan enabled
8. Verifikasi drag handle tersedia pada tiap kolom di overlay
9. Verifikasi item `Setup Column...` tersedia di overlay

### TC-GS-USER-698: Screening Popup Setup Column

10. Klik item `Setup Column...`
11. Verifikasi Header: Title `Setup Column`
12. Verifikasi Header: deskripsi panduan `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
13. Verifikasi Header: icon `[✕]`
14. Verifikasi Body: daftar kolom `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active`, `Last Update`, `Temporary User`, `Temporary Until` masing-masing dengan checkbox
15. Verifikasi Body: drag handle pada tiap kolom
16. Verifikasi Body: icon Pin pada tiap kolom
17. Verifikasi Body: preview tabel
18. Verifikasi Footer: tombol `[Reset to Default]`
19. Verifikasi Footer: tombol `[Save]`
20. Verifikasi Footer tanpa tombol `[Cancel]`

### TC-GS-USER-706: Tutup Setup Column via [✕] membuang perubahan

21. Hilangkan centang `Email`
22. Verifikasi preview tabel tidak menampilkan kolom `Email`
23. Klik `[✕]`
24. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir: kolom `Email` tampil

### TC-GS-USER-707: Guard satu kolom tersisa tidak bisa di-uncheck

25. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
26. Hilangkan centang `Email`
27. Hilangkan centang `Employee ID`
28. Hilangkan centang `Position`
29. Hilangkan centang `Division`
30. Hilangkan centang `Active`
31. Hilangkan centang `Last Update`
32. Arahkan kursor ke checkbox `Name`
33. Verifikasi checkbox kolom terakhir `Name` tetap tampil namun disabled
34. Verifikasi tooltip `At least one column must remain visible.`
35. Klik `[✕]`

### TC-GS-USER-708: Maksimal 3 kolom di-pin

36. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
37. Klik icon Pin pada `Name`
38. Klik icon Pin pada `Email`
39. Klik icon Pin pada `Employee ID`
40. Arahkan kursor ke icon Pin kolom keempat `Position`
41. Verifikasi icon Pin kolom keempat `Position` disabled
42. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
43. Klik `[✕]`

### TC-GS-USER-699: Setup Column hide/unhide kelas Hideable

44. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
45. Hilangkan centang `Name`
46. Verifikasi perubahan kolom `Name` tampil di preview: kolom tidak tampil di preview tabel
47. Centang kembali `Name`
48. Klik `[Save]`
49. Verifikasi kolom `Name` tersimpan setelah Save: kolom tampil di tabel
50. Muat ulang halaman (F5)
51. Klik Tab `Non-Login User`
52. Verifikasi kolom `Name` bertahan setelah F5: kolom tampil di tabel
53. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
54. Hilangkan centang `Email`
55. Verifikasi perubahan kolom `Email` tampil di preview: kolom tidak tampil di preview tabel
56. Centang kembali `Email`
57. Klik `[Save]`
58. Verifikasi kolom `Email` tersimpan setelah Save: kolom tampil di tabel
59. Muat ulang halaman (F5)
60. Klik Tab `Non-Login User`
61. Verifikasi kolom `Email` bertahan setelah F5: kolom tampil di tabel
62. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
63. Hilangkan centang `Employee ID`
64. Verifikasi perubahan kolom `Employee ID` tampil di preview: kolom tidak tampil di preview tabel
65. Centang kembali `Employee ID`
66. Klik `[Save]`
67. Verifikasi kolom `Employee ID` tersimpan setelah Save: kolom tampil di tabel
68. Muat ulang halaman (F5)
69. Klik Tab `Non-Login User`
70. Verifikasi kolom `Employee ID` bertahan setelah F5: kolom tampil di tabel
71. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
72. Hilangkan centang `Position`
73. Verifikasi perubahan kolom `Position` tampil di preview: kolom tidak tampil di preview tabel
74. Centang kembali `Position`
75. Klik `[Save]`
76. Verifikasi kolom `Position` tersimpan setelah Save: kolom tampil di tabel
77. Muat ulang halaman (F5)
78. Klik Tab `Non-Login User`
79. Verifikasi kolom `Position` bertahan setelah F5: kolom tampil di tabel
80. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
81. Hilangkan centang `Division`
82. Verifikasi perubahan kolom `Division` tampil di preview: kolom tidak tampil di preview tabel
83. Centang kembali `Division`
84. Klik `[Save]`
85. Verifikasi kolom `Division` tersimpan setelah Save: kolom tampil di tabel
86. Muat ulang halaman (F5)
87. Klik Tab `Non-Login User`
88. Verifikasi kolom `Division` bertahan setelah F5: kolom tampil di tabel
89. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
90. Hilangkan centang `Active`
91. Verifikasi perubahan kolom `Active` tampil di preview: kolom tidak tampil di preview tabel
92. Centang kembali `Active`
93. Klik `[Save]`
94. Verifikasi kolom `Active` tersimpan setelah Save: kolom tampil di tabel
95. Muat ulang halaman (F5)
96. Klik Tab `Non-Login User`
97. Verifikasi kolom `Active` bertahan setelah F5: kolom tampil di tabel
98. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
99. Hilangkan centang `Last Update`
100. Verifikasi perubahan kolom `Last Update` tampil di preview: kolom tidak tampil di preview tabel
101. Centang kembali `Last Update`
102. Klik `[Save]`
103. Verifikasi kolom `Last Update` tersimpan setelah Save: kolom tampil di tabel
104. Muat ulang halaman (F5)
105. Klik Tab `Non-Login User`
106. Verifikasi kolom `Last Update` bertahan setelah F5: kolom tampil di tabel

### TC-GS-USER-700: Setup Column drag reorder kelas Hideable

107. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
108. Seret `Name` ke posisi pertama
109. Verifikasi perubahan kolom `Name` tampil di preview: kolom berada di posisi pertama preview tabel
110. Klik `[Save]`
111. Verifikasi kolom `Name` tersimpan setelah Save: kolom berada di posisi pertama tabel
112. Muat ulang halaman (F5)
113. Klik Tab `Non-Login User`
114. Verifikasi kolom `Name` bertahan setelah F5: kolom berada di posisi pertama tabel
115. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
116. Seret `Email` ke posisi pertama
117. Verifikasi perubahan kolom `Email` tampil di preview: kolom berada di posisi pertama preview tabel
118. Klik `[Save]`
119. Verifikasi kolom `Email` tersimpan setelah Save: kolom berada di posisi pertama tabel
120. Muat ulang halaman (F5)
121. Klik Tab `Non-Login User`
122. Verifikasi kolom `Email` bertahan setelah F5: kolom berada di posisi pertama tabel
123. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
124. Seret `Employee ID` ke posisi pertama
125. Verifikasi perubahan kolom `Employee ID` tampil di preview: kolom berada di posisi pertama preview tabel
126. Klik `[Save]`
127. Verifikasi kolom `Employee ID` tersimpan setelah Save: kolom berada di posisi pertama tabel
128. Muat ulang halaman (F5)
129. Klik Tab `Non-Login User`
130. Verifikasi kolom `Employee ID` bertahan setelah F5: kolom berada di posisi pertama tabel
131. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
132. Seret `Position` ke posisi pertama
133. Verifikasi perubahan kolom `Position` tampil di preview: kolom berada di posisi pertama preview tabel
134. Klik `[Save]`
135. Verifikasi kolom `Position` tersimpan setelah Save: kolom berada di posisi pertama tabel
136. Muat ulang halaman (F5)
137. Klik Tab `Non-Login User`
138. Verifikasi kolom `Position` bertahan setelah F5: kolom berada di posisi pertama tabel
139. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
140. Seret `Division` ke posisi pertama
141. Verifikasi perubahan kolom `Division` tampil di preview: kolom berada di posisi pertama preview tabel
142. Klik `[Save]`
143. Verifikasi kolom `Division` tersimpan setelah Save: kolom berada di posisi pertama tabel
144. Muat ulang halaman (F5)
145. Klik Tab `Non-Login User`
146. Verifikasi kolom `Division` bertahan setelah F5: kolom berada di posisi pertama tabel
147. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
148. Seret `Active` ke posisi pertama
149. Verifikasi perubahan kolom `Active` tampil di preview: kolom berada di posisi pertama preview tabel
150. Klik `[Save]`
151. Verifikasi kolom `Active` tersimpan setelah Save: kolom berada di posisi pertama tabel
152. Muat ulang halaman (F5)
153. Klik Tab `Non-Login User`
154. Verifikasi kolom `Active` bertahan setelah F5: kolom berada di posisi pertama tabel
155. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
156. Seret `Last Update` ke posisi pertama
157. Verifikasi perubahan kolom `Last Update` tampil di preview: kolom berada di posisi pertama preview tabel
158. Klik `[Save]`
159. Verifikasi kolom `Last Update` tersimpan setelah Save: kolom berada di posisi pertama tabel
160. Muat ulang halaman (F5)
161. Klik Tab `Non-Login User`
162. Verifikasi kolom `Last Update` bertahan setelah F5: kolom berada di posisi pertama tabel

### TC-GS-USER-702: Setup Column hide/unhide kelas Curated

163. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
164. Centang `Temporary User`
165. Verifikasi perubahan kolom `Temporary User` tampil di preview: kolom tampil di preview tabel
166. Klik `[Save]`
167. Verifikasi kolom `Temporary User` tersimpan setelah Save: kolom tampil di tabel
168. Muat ulang halaman (F5)
169. Klik Tab `Non-Login User`
170. Verifikasi kolom `Temporary User` bertahan setelah F5: kolom tampil di tabel
171. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
172. Hilangkan centang `Temporary User`
173. Klik `[Save]`
174. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
175. Centang `Temporary Until`
176. Verifikasi perubahan kolom `Temporary Until` tampil di preview: kolom tampil di preview tabel
177. Klik `[Save]`
178. Verifikasi kolom `Temporary Until` tersimpan setelah Save: kolom tampil di tabel
179. Muat ulang halaman (F5)
180. Klik Tab `Non-Login User`
181. Verifikasi kolom `Temporary Until` bertahan setelah F5: kolom tampil di tabel
182. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
183. Hilangkan centang `Temporary Until`
184. Klik `[Save]`

### TC-GS-USER-703: Setup Column drag reorder kelas Curated

185. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
186. Centang `Temporary User`
187. Seret `Temporary User` ke posisi pertama
188. Verifikasi perubahan kolom `Temporary User` tampil di preview: kolom berada di posisi pertama preview tabel
189. Klik `[Save]`
190. Verifikasi kolom `Temporary User` tersimpan setelah Save: kolom berada di posisi pertama tabel
191. Muat ulang halaman (F5)
192. Klik Tab `Non-Login User`
193. Verifikasi kolom `Temporary User` bertahan setelah F5: kolom berada di posisi pertama tabel
194. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
195. Hilangkan centang `Temporary User`
196. Klik `[Save]`
197. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
198. Centang `Temporary Until`
199. Seret `Temporary Until` ke posisi pertama
200. Verifikasi perubahan kolom `Temporary Until` tampil di preview: kolom berada di posisi pertama preview tabel
201. Klik `[Save]`
202. Verifikasi kolom `Temporary Until` tersimpan setelah Save: kolom berada di posisi pertama tabel
203. Muat ulang halaman (F5)
204. Klik Tab `Non-Login User`
205. Verifikasi kolom `Temporary Until` bertahan setelah F5: kolom berada di posisi pertama tabel
206. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
207. Hilangkan centang `Temporary Until`
208. Klik `[Save]`
209. Sempitkan viewport sehingga tabel dapat di-scroll horizontal

### TC-GS-USER-701: Setup Column pin/unpin kelas Hideable

210. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
211. Klik icon Pin pada `Name`
212. Verifikasi perubahan kolom `Name` tampil di preview: kolom ter-pin pada preview tabel
213. Klik `[Save]`
214. Scroll tabel secara horizontal
215. Verifikasi kolom `Name` tersimpan setelah Save: kolom beku saat scroll horizontal
216. Muat ulang halaman (F5)
217. Klik Tab `Non-Login User`
218. Scroll tabel secara horizontal
219. Verifikasi kolom `Name` bertahan setelah F5: kolom beku saat scroll horizontal
220. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
221. Klik icon Pin pada `Name` untuk Unpin
222. Klik `[Save]`
223. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
224. Klik icon Pin pada `Email`
225. Verifikasi perubahan kolom `Email` tampil di preview: kolom ter-pin pada preview tabel
226. Klik `[Save]`
227. Scroll tabel secara horizontal
228. Verifikasi kolom `Email` tersimpan setelah Save: kolom beku saat scroll horizontal
229. Muat ulang halaman (F5)
230. Klik Tab `Non-Login User`
231. Scroll tabel secara horizontal
232. Verifikasi kolom `Email` bertahan setelah F5: kolom beku saat scroll horizontal
233. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
234. Klik icon Pin pada `Email` untuk Unpin
235. Klik `[Save]`
236. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
237. Klik icon Pin pada `Employee ID`
238. Verifikasi perubahan kolom `Employee ID` tampil di preview: kolom ter-pin pada preview tabel
239. Klik `[Save]`
240. Scroll tabel secara horizontal
241. Verifikasi kolom `Employee ID` tersimpan setelah Save: kolom beku saat scroll horizontal
242. Muat ulang halaman (F5)
243. Klik Tab `Non-Login User`
244. Scroll tabel secara horizontal
245. Verifikasi kolom `Employee ID` bertahan setelah F5: kolom beku saat scroll horizontal
246. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
247. Klik icon Pin pada `Employee ID` untuk Unpin
248. Klik `[Save]`
249. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
250. Klik icon Pin pada `Position`
251. Verifikasi perubahan kolom `Position` tampil di preview: kolom ter-pin pada preview tabel
252. Klik `[Save]`
253. Scroll tabel secara horizontal
254. Verifikasi kolom `Position` tersimpan setelah Save: kolom beku saat scroll horizontal
255. Muat ulang halaman (F5)
256. Klik Tab `Non-Login User`
257. Scroll tabel secara horizontal
258. Verifikasi kolom `Position` bertahan setelah F5: kolom beku saat scroll horizontal
259. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
260. Klik icon Pin pada `Position` untuk Unpin
261. Klik `[Save]`
262. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
263. Klik icon Pin pada `Division`
264. Verifikasi perubahan kolom `Division` tampil di preview: kolom ter-pin pada preview tabel
265. Klik `[Save]`
266. Scroll tabel secara horizontal
267. Verifikasi kolom `Division` tersimpan setelah Save: kolom beku saat scroll horizontal
268. Muat ulang halaman (F5)
269. Klik Tab `Non-Login User`
270. Scroll tabel secara horizontal
271. Verifikasi kolom `Division` bertahan setelah F5: kolom beku saat scroll horizontal
272. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
273. Klik icon Pin pada `Division` untuk Unpin
274. Klik `[Save]`
275. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
276. Klik icon Pin pada `Active`
277. Verifikasi perubahan kolom `Active` tampil di preview: kolom ter-pin pada preview tabel
278. Klik `[Save]`
279. Scroll tabel secara horizontal
280. Verifikasi kolom `Active` tersimpan setelah Save: kolom beku saat scroll horizontal
281. Muat ulang halaman (F5)
282. Klik Tab `Non-Login User`
283. Scroll tabel secara horizontal
284. Verifikasi kolom `Active` bertahan setelah F5: kolom beku saat scroll horizontal
285. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
286. Klik icon Pin pada `Active` untuk Unpin
287. Klik `[Save]`
288. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
289. Klik icon Pin pada `Last Update`
290. Verifikasi perubahan kolom `Last Update` tampil di preview: kolom ter-pin pada preview tabel
291. Klik `[Save]`
292. Scroll tabel secara horizontal
293. Verifikasi kolom `Last Update` tersimpan setelah Save: kolom beku saat scroll horizontal
294. Muat ulang halaman (F5)
295. Klik Tab `Non-Login User`
296. Scroll tabel secara horizontal
297. Verifikasi kolom `Last Update` bertahan setelah F5: kolom beku saat scroll horizontal
298. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
299. Klik icon Pin pada `Last Update` untuk Unpin
300. Klik `[Save]`

### TC-GS-USER-704: Setup Column pin/unpin kelas Curated

301. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
302. Centang `Temporary User`
303. Klik icon Pin pada `Temporary User`
304. Verifikasi perubahan kolom `Temporary User` tampil di preview: kolom ter-pin pada preview tabel
305. Klik `[Save]`
306. Scroll tabel secara horizontal
307. Verifikasi kolom `Temporary User` tersimpan setelah Save: kolom beku saat scroll horizontal
308. Muat ulang halaman (F5)
309. Klik Tab `Non-Login User`
310. Scroll tabel secara horizontal
311. Verifikasi kolom `Temporary User` bertahan setelah F5: kolom beku saat scroll horizontal
312. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
313. Klik icon Pin pada `Temporary User` untuk Unpin
314. Hilangkan centang `Temporary User`
315. Klik `[Save]`
316. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
317. Centang `Temporary Until`
318. Klik icon Pin pada `Temporary Until`
319. Verifikasi perubahan kolom `Temporary Until` tampil di preview: kolom ter-pin pada preview tabel
320. Klik `[Save]`
321. Scroll tabel secara horizontal
322. Verifikasi kolom `Temporary Until` tersimpan setelah Save: kolom beku saat scroll horizontal
323. Muat ulang halaman (F5)
324. Klik Tab `Non-Login User`
325. Scroll tabel secara horizontal
326. Verifikasi kolom `Temporary Until` bertahan setelah F5: kolom beku saat scroll horizontal
327. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
328. Klik icon Pin pada `Temporary Until` untuk Unpin
329. Hilangkan centang `Temporary Until`
330. Klik `[Save]`
331. Kembalikan viewport ke ukuran awal

### TC-GS-USER-705: Setup Column Reset to Default

332. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
333. Seret `Division` ke posisi pertama
334. Hilangkan centang `Email`
335. Klik `[Save]`
336. Verifikasi konfigurasi yang diubah berlaku di tabel: kolom `Division` di posisi pertama dan kolom `Email` tidak tampil
337. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
338. Klik `[Reset to Default]`
339. Klik `[Save]`
340. Verifikasi susunan kolom kembali default: `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active`, `Last Update`
341. Muat ulang halaman (F5)
342. Klik Tab `Non-Login User`
343. Verifikasi susunan kolom default bertahan setelah F5: `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active`, `Last Update`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Holder dan 12 Non-Login User dipenuhi spec ini lewat seeding di hook `before`; spec tidak menumpang spec lain.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 697, 698 (screening, tanpa aksi), 706, 707, 708 (tutup tanpa Save dan guard yang diblokir; tidak menyimpan perubahan), 699, 700, 702, 703 (hide dan reorder yang menyimpan), 701 dan 704 (pin, memakai viewport sempit), lalu 705 (Reset to Default) di akhir. Alasan: TC yang tidak mengubah preferensi tersimpan dijalankan sebelum TC yang menyimpan; TC kelas pin dikelompokkan supaya viewport disempitkan satu kali; `[Reset to Default]` memulihkan seluruh preferensi tersimpan di akhir spec. Urutan di `tc-user.md`: 697 sampai 708.
- Langkah penghubung (aksi tanpa `Verifikasi`): pembukaan Tab (langkah 1 sampai 3); `Klik Tab Non-Login User` sesudah tiap F5; pembukaan Popup Setup Column berulang (prefix berulang, popup menutup setelah `[Save]` dan `[✕]`); `Centang` kolom curated sebelum `Seret` atau `Pin` (kolom curated default tersembunyi) dan `Hilangkan centang` kolom curated beserta `[Save]` di akhir tiap kolom curated (memulihkan default); `Unpin` beserta `[Save]` di akhir tiap kolom pin; langkah 209 dan 331 (viewport). Pada TC-GS-USER-706 popup masih terbuka dari TC-GS-USER-698, sehingga langkah 3 TC ("Buka Setup Column") dipenuhi langkah `Klik item Setup Column...`.
- Langkah 4 TC-GS-USER-699 ("uncheck lalu check, Save, refresh F5") ditulis literal: kolom di-uncheck (asersi preview), di-check kembali, lalu `[Save]` dan F5 (asersi tersimpan dan bertahan).
- Asersi tambahan (S-03, bagian 8b butir 2): TC-GS-USER-706 memverifikasi preview kolom `Email` tidak tampil sebelum `[✕]` (anchor); TC-GS-USER-705 memverifikasi konfigurasi yang diubah berlaku sebelum `[Reset to Default]` (anchor).
- Pembagian TC lintas spec: TC-GS-USER-400 sampai 403 (screening Tab, navigasi) dan 671 sampai 677 (Search, termasuk Search terhadap kolom hidden) ada di spec 108; TC-GS-USER-678 sampai 686 (Filter Panel) ada di spec 109; TC-GS-USER-687 sampai 691 (kombinasi, filter kolom hidden) ada di spec 110; TC-GS-USER-692 sampai 696, 714, dan 715 (Sort, Pagination) ada di spec 111; TC-GS-USER-404 dan 709 sampai 713 (Download termasuk kolom hidden) ada di spec 113.
- Spec melewati sekitar 35 langkah (343 langkah) karena dua belas TC berbagi satu layar (Popup Setup Column Tab Non-Login User), satu dataset (12 Non-Login User milik spec), dan satu kelas harness (fungsional). TC-GS-USER-699, 700, dan 701 masing-masing menguji tujuh kolom Hideable, TC-GS-USER-702, 703, dan 704 masing-masing dua kolom Curated, dengan blok identik per kolom yang dituntut Expected TC (Save dan F5 per kolom); tiap blok berdiri sendiri (kegagalan satu kolom tidak menghapus makna kolom lain) dan memakai popup serta tabel yang sama. Langkah pembuka popup yang berulang dan `Klik Tab` sesudah F5 merupakan prefix berulang.
- Temuan untuk QA:
  - TC-GS-USER-697 sampai 708 menyebut tabel dan Name tanpa suffix; spec memakai holder dan Non-Login User milik spec bersuffix (S-06, S-11).
  - TC-GS-USER-697 Expected a: PRD user.md §4.1.4 menyebut kolom Custom Field aktif (Pre-setup No. 24: `Blood Type`, `Skills`, `Emergency Phone`) sebagai kolom curated tambahan di tab ini; bila environment memiliki Custom Field aktif, overlay dan popup memuat kolom itu di samping sembilan kolom pada TC. Spec mengasersi sembilan kolom yang disebut TC dan tidak mengasersi ketiadaan kolom lain.
  - TC-GS-USER-698 Expected a: TC hanya menyebut "deskripsi panduan"; teks `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.` diambil dari prd-conventions.md §9.3.
  - TC-GS-USER-698 Expected b: TC tidak menyebut isi preview tabel; spec hanya mengasersi preview tampil.
  - TC-GS-USER-699: Langkah "uncheck lalu check" menghasilkan konfigurasi akhir yang sama dengan default, sehingga `[Save]` dan F5 tidak membedakan konfigurasi tersimpan dari default; asersi persistensi hanya membuktikan kolom tetap tampil.
  - TC-GS-USER-700: Kolom `Name` sudah berada di posisi pertama secara default, sehingga menyeretnya ke posisi pertama tidak mengubah urutan.
  - TC-GS-USER-702 sampai 704: kolom Curated default unchecked, sehingga "uncheck lalu check" (TC-GS-USER-702) tidak dapat dilakukan pada keadaan awal; spec mencentang kolom (tampil), memverifikasi, lalu menyembunyikannya kembali. TC-GS-USER-703 dan 704 tidak menyebut langkah mencentang kolom sebelum menggeser atau mem-pin; spec menambahkannya supaya perubahan teramati di tabel.
  - TC-GS-USER-701 dan 704: TC tidak menyebut ukuran viewport; tim FE perlu menetapkan viewport sempit supaya tabel dapat di-scroll horizontal. Expected "kolom beku saat scroll horizontal" tidak menyebut kolom lain yang bergeser; spec hanya mengasersi kolom ter-pin tetap terlihat.
  - TC-GS-USER-705: Langkah 3 ("Ubah urutan dan visibility kolom") tidak menyebut kolom; spec memakai `Division` ke posisi pertama dan `Email` disembunyikan.
  - TC-GS-USER-706: TC tidak menyebut kolom yang diubah; spec memakai `Email`.
  - TC-GS-USER-707: TC tidak menyebut kolom yang tersisa; spec menyisakan `Name`. TC tidak menyebut perilaku kolom curated yang sudah unchecked; spec tidak mengubahnya.
  - TC-GS-USER-708: TC tidak menyebut tiga kolom yang di-pin; spec memakai `Name`, `Email`, `Employee ID`, dan memeriksa icon Pin `Position` sebagai kolom keempat.
  - Retensi Tab aktif setelah F5 pada Detail User tidak didefinisikan di TC maupun PRD; spec mengklik Tab `Non-Login User` sesudah F5.
  - Mekanisme penghapusan preferensi kolom di browser dan seeding Login User dan Non-Login User tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.

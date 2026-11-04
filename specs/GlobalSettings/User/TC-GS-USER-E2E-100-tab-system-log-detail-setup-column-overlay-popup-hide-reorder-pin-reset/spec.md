---
id: TC-GS-USER-E2E-100-tab-system-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset
title: "Tab System Log Detail: Setup Column (Overlay, Popup, Guard Kolom Terakhir, Maksimal 3 Pin, Tutup dengan X, Hide/Unhide, Reorder, Pin/Unpin, dan Reset to Default)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-615
  - TC-GS-USER-616
  - TC-GS-USER-617
  - TC-GS-USER-618
  - TC-GS-USER-619
  - TC-GS-USER-620
  - TC-GS-USER-621
  - TC-GS-USER-622
  - TC-GS-USER-623
coverage:
  web: automated
---

# Tab System Log Detail: Setup Column (Overlay, Popup, Guard Kolom Terakhir, Maksimal 3 Pin, Tutup dengan X, Hide/Unhide, Reorder, Pin/Unpin, dan Reset to Default)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor UI: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 23 dan 26): hanya dibaca (Division dan Access dipakai sebagai nilai field user seed). Spec tidak mengubah atau menghapus data Pre-setup.
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). System Log memuat aksi yang dilakukan user sebagai aktor (PRD user.md §8.3). Tiap user diberi Division `Finance` dan Access `Fixed Asset`:
  - Pemilik log `Aktor Log {runId}-100`, email `aktorlog+{runId}-100@qwertysystem.net`, tier Total Control, status Activated, password `Spectra.env.USER_PASSWORD`. Aktivasi akun seed dan sesi API Aktor Log disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut mekanismenya). Seluruh aksi seed di bawah dijalankan lewat sesi API Aktor Log.
  - Target aksi `Target Alfa {runId}-100` (email `targetalfa+{runId}-100@qwertysystem.net`, Position `Staff`) dan `Target Beta {runId}-100` (email `targetbeta+{runId}-100@qwertysystem.net`).
  - Aksi seed oleh Aktor Log, berurutan (hanya data yang dipakai `Verifikasi`, S-11): (1) Create `Target Alfa`; (2) Create `Target Beta`; (3) Edit Position `Target Alfa` dari `Staff` menjadi `Supervisor`; (4) Delete `Target Beta`. Spec mengamati kolom, bukan isi baris; riwayat terisi agar tabel menampilkan baris data dan dapat di-scroll horizontal.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Target Alfa`, `Target Beta` bila masih ada, dan `Aktor Log`; hapus sisa user bersuffix `-100` dari run lama. Entri log tidak bisa dihapus. Hapus preferensi Setup Column tab System Log di browser (akun Siti) sebagai cadangan pemulihan (suite.md) dan kembalikan viewport ke bawaan.
- Preferensi Setup Column (urutan, visibilitas, pin) tersimpan lintas muat ulang halaman (TC-GS-USER-617 sampai 620). Tempat penyimpanan tidak disebut TC User; mekanisme membaca dan mengosongkannya disediakan tim FE. Hook `before` mengosongkan preferensi tab System Log sehingga spec mulai dari default (urutan `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, tujuh kolom tampil, tanpa pin). "Muat ulang halaman" dilakukan pada konteks browser yang sama supaya preferensi tetap ada.
- Kemampuan teknis: drag and drop elemen daftar kolom; hover checkbox dan icon Pin yang disabled untuk membaca tooltip; mengatur lebar viewport sehingga tabel System Log dapat di-scroll horizontal (TC tidak menyebut lebar viewport; viewport diperkecil sampai overflow horizontal) dan scroll horizontal tabel.
- State global yang diubah dan dipulihkan: preferensi Setup Column tab System Log (default dipulihkan pada TC-GS-USER-620 lewat `[Reset to Default]`, dengan hook `after` sebagai cadangan) dan lebar viewport (dipulihkan pada langkah 239). Suite berjalan serial (`parallel: false`) karena preferensi Setup Column dipakai bersama spec lain pada akun dan browser yang sama.
- Precondition TC-GS-USER-615 sampai 623: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User).

## Test Steps

### Pembukaan tab

1. Klik icon Search di User List, ketik `Aktor Log {runId}-100`, tekan Enter
2. Klik Name `Aktor Log {runId}-100`
3. Klik Tab `System Log`

### TC-GS-USER-615: Screening Overlay Column Visibility

4. Klik header Column Visibility (⋯)
5. Verifikasi overlay memuat tujuh kolom berurutan `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`
6. Verifikasi ketujuh kolom pada overlay tercentang dan enabled (kolom Hideable)
7. Verifikasi ketujuh kolom pada overlay memiliki drag handle
8. Verifikasi item `Setup Column...` tersedia di overlay

### TC-GS-USER-616: Screening Popup Setup Column

9. Klik item `Setup Column...` pada overlay
10. Verifikasi bagian Header: Title `Setup Column`
11. Verifikasi bagian Header: deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
12. Verifikasi bagian Header: icon `[✕]`
13. Verifikasi bagian Body: daftar tujuh kolom dengan checkbox
14. Verifikasi bagian Body: ketujuh kolom memiliki drag handle
15. Verifikasi bagian Body: ketujuh kolom memiliki icon Pin
16. Verifikasi bagian Body: preview tabel
17. Verifikasi bagian Footer: `[Reset to Default]` dan `[Save]`
18. Verifikasi bagian Footer: tidak ada `[Cancel]`

### TC-GS-USER-622: Guard satu kolom tersisa tidak bisa di-uncheck

19. Hilangkan centang enam kolom: `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value` (tersisa `Date`)
20. Hover checkbox `Date`
21. Verifikasi checkbox `Date` tetap tampil dan disabled
22. Verifikasi Tooltip `At least one column must remain visible.`
23. Klik `[✕]` untuk menutup popup tanpa menyimpan

### TC-GS-USER-621: Tutup Setup Column via [✕] membuang perubahan

24. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Field`
25. Klik `[✕]`
26. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir: tujuh kolom `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value` tampil berurutan

### TC-GS-USER-623: Maksimal 3 kolom di-pin

27. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon Pin pada `Date`
28. Klik icon Pin pada `Action`
29. Klik icon Pin pada `Object`
30. Hover icon Pin pada kolom keempat `Name`
31. Verifikasi icon Pin `Name` disabled
32. Verifikasi Tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
33. Klik `[✕]` untuk menutup popup tanpa menyimpan

### TC-GS-USER-617: Setup Column hide/unhide kelas Hideable

34. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Date`
35. Verifikasi preview pada popup tidak memuat kolom `Date`
36. Klik `[Save]`
37. Verifikasi kolom `Date` tidak tampil di tabel
38. Muat ulang halaman (F5)
39. Klik Tab `System Log`
40. Verifikasi kolom `Action` tampil di tabel setelah muat ulang halaman
41. Verifikasi kolom `Date` tetap tidak tampil setelah muat ulang halaman
42. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Date`
43. Verifikasi preview pada popup memuat kolom `Date`
44. Klik `[Save]`
45. Verifikasi kolom `Date` tampil kembali di tabel
46. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Action`
47. Verifikasi preview pada popup tidak memuat kolom `Action`
48. Klik `[Save]`
49. Verifikasi kolom `Action` tidak tampil di tabel
50. Muat ulang halaman (F5)
51. Klik Tab `System Log`
52. Verifikasi kolom `Date` tampil di tabel setelah muat ulang halaman
53. Verifikasi kolom `Action` tetap tidak tampil setelah muat ulang halaman
54. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Action`
55. Verifikasi preview pada popup memuat kolom `Action`
56. Klik `[Save]`
57. Verifikasi kolom `Action` tampil kembali di tabel
58. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Object`
59. Verifikasi preview pada popup tidak memuat kolom `Object`
60. Klik `[Save]`
61. Verifikasi kolom `Object` tidak tampil di tabel
62. Muat ulang halaman (F5)
63. Klik Tab `System Log`
64. Verifikasi kolom `Date` tampil di tabel setelah muat ulang halaman
65. Verifikasi kolom `Object` tetap tidak tampil setelah muat ulang halaman
66. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Object`
67. Verifikasi preview pada popup memuat kolom `Object`
68. Klik `[Save]`
69. Verifikasi kolom `Object` tampil kembali di tabel
70. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Name`
71. Verifikasi preview pada popup tidak memuat kolom `Name`
72. Klik `[Save]`
73. Verifikasi kolom `Name` tidak tampil di tabel
74. Muat ulang halaman (F5)
75. Klik Tab `System Log`
76. Verifikasi kolom `Date` tampil di tabel setelah muat ulang halaman
77. Verifikasi kolom `Name` tetap tidak tampil setelah muat ulang halaman
78. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Name`
79. Verifikasi preview pada popup memuat kolom `Name`
80. Klik `[Save]`
81. Verifikasi kolom `Name` tampil kembali di tabel
82. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Field`
83. Verifikasi preview pada popup tidak memuat kolom `Field`
84. Klik `[Save]`
85. Verifikasi kolom `Field` tidak tampil di tabel
86. Muat ulang halaman (F5)
87. Klik Tab `System Log`
88. Verifikasi kolom `Date` tampil di tabel setelah muat ulang halaman
89. Verifikasi kolom `Field` tetap tidak tampil setelah muat ulang halaman
90. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Field`
91. Verifikasi preview pada popup memuat kolom `Field`
92. Klik `[Save]`
93. Verifikasi kolom `Field` tampil kembali di tabel
94. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Old Value`
95. Verifikasi preview pada popup tidak memuat kolom `Old Value`
96. Klik `[Save]`
97. Verifikasi kolom `Old Value` tidak tampil di tabel
98. Muat ulang halaman (F5)
99. Klik Tab `System Log`
100. Verifikasi kolom `Date` tampil di tabel setelah muat ulang halaman
101. Verifikasi kolom `Old Value` tetap tidak tampil setelah muat ulang halaman
102. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Old Value`
103. Verifikasi preview pada popup memuat kolom `Old Value`
104. Klik `[Save]`
105. Verifikasi kolom `Old Value` tampil kembali di tabel
106. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `New Value`
107. Verifikasi preview pada popup tidak memuat kolom `New Value`
108. Klik `[Save]`
109. Verifikasi kolom `New Value` tidak tampil di tabel
110. Muat ulang halaman (F5)
111. Klik Tab `System Log`
112. Verifikasi kolom `Date` tampil di tabel setelah muat ulang halaman
113. Verifikasi kolom `New Value` tetap tidak tampil setelah muat ulang halaman
114. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `New Value`
115. Verifikasi preview pada popup memuat kolom `New Value`
116. Klik `[Save]`
117. Verifikasi kolom `New Value` tampil kembali di tabel

### TC-GS-USER-618: Setup Column drag reorder kelas Hideable

118. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Date` ke posisi terakhir
119. Verifikasi preview pada popup menempatkan `Date` di posisi terakhir
120. Klik `[Save]`
121. Verifikasi kolom `Date` berada di posisi terakhir tabel
122. Muat ulang halaman (F5)
123. Klik Tab `System Log`
124. Verifikasi kolom `Date` tetap di posisi terakhir tabel setelah muat ulang halaman
125. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Action` ke posisi pertama
126. Verifikasi preview pada popup menempatkan `Action` di posisi pertama
127. Klik `[Save]`
128. Verifikasi kolom `Action` berada di posisi pertama tabel
129. Muat ulang halaman (F5)
130. Klik Tab `System Log`
131. Verifikasi kolom `Action` tetap di posisi pertama tabel setelah muat ulang halaman
132. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Object` ke posisi pertama
133. Verifikasi preview pada popup menempatkan `Object` di posisi pertama
134. Klik `[Save]`
135. Verifikasi kolom `Object` berada di posisi pertama tabel
136. Muat ulang halaman (F5)
137. Klik Tab `System Log`
138. Verifikasi kolom `Object` tetap di posisi pertama tabel setelah muat ulang halaman
139. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Name` ke posisi pertama
140. Verifikasi preview pada popup menempatkan `Name` di posisi pertama
141. Klik `[Save]`
142. Verifikasi kolom `Name` berada di posisi pertama tabel
143. Muat ulang halaman (F5)
144. Klik Tab `System Log`
145. Verifikasi kolom `Name` tetap di posisi pertama tabel setelah muat ulang halaman
146. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Field` ke posisi pertama
147. Verifikasi preview pada popup menempatkan `Field` di posisi pertama
148. Klik `[Save]`
149. Verifikasi kolom `Field` berada di posisi pertama tabel
150. Muat ulang halaman (F5)
151. Klik Tab `System Log`
152. Verifikasi kolom `Field` tetap di posisi pertama tabel setelah muat ulang halaman
153. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Old Value` ke posisi pertama
154. Verifikasi preview pada popup menempatkan `Old Value` di posisi pertama
155. Klik `[Save]`
156. Verifikasi kolom `Old Value` berada di posisi pertama tabel
157. Muat ulang halaman (F5)
158. Klik Tab `System Log`
159. Verifikasi kolom `Old Value` tetap di posisi pertama tabel setelah muat ulang halaman
160. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `New Value` ke posisi pertama
161. Verifikasi preview pada popup menempatkan `New Value` di posisi pertama
162. Klik `[Save]`
163. Verifikasi kolom `New Value` berada di posisi pertama tabel
164. Muat ulang halaman (F5)
165. Klik Tab `System Log`
166. Verifikasi urutan terakhir tetap tersimpan setelah muat ulang halaman: `New Value`, `Old Value`, `Field`, `Name`, `Object`, `Action`, `Date`

### TC-GS-USER-619: Setup Column pin/unpin kelas Hideable

167. Klik header Column Visibility (⋯), klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`
168. Perkecil lebar viewport hingga tabel System Log dapat di-scroll horizontal
169. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon Pin pada `Date`
170. Verifikasi preview pada popup menampilkan `Date` ter-pin
171. Klik `[Save]`
172. Scroll tabel System Log secara horizontal
173. Verifikasi kolom `Date` membeku (sticky) saat scroll horizontal
174. Muat ulang halaman (F5)
175. Klik Tab `System Log`
176. Scroll tabel System Log secara horizontal
177. Verifikasi kolom `Date` tetap membeku setelah muat ulang halaman
178. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Date`, lalu klik `[Save]`
179. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon Pin pada `Action`
180. Verifikasi preview pada popup menampilkan `Action` ter-pin
181. Klik `[Save]`
182. Scroll tabel System Log secara horizontal
183. Verifikasi kolom `Action` membeku (sticky) saat scroll horizontal
184. Muat ulang halaman (F5)
185. Klik Tab `System Log`
186. Scroll tabel System Log secara horizontal
187. Verifikasi kolom `Action` tetap membeku setelah muat ulang halaman
188. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Action`, lalu klik `[Save]`
189. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon Pin pada `Object`
190. Verifikasi preview pada popup menampilkan `Object` ter-pin
191. Klik `[Save]`
192. Scroll tabel System Log secara horizontal
193. Verifikasi kolom `Object` membeku (sticky) saat scroll horizontal
194. Muat ulang halaman (F5)
195. Klik Tab `System Log`
196. Scroll tabel System Log secara horizontal
197. Verifikasi kolom `Object` tetap membeku setelah muat ulang halaman
198. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Object`, lalu klik `[Save]`
199. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon Pin pada `Name`
200. Verifikasi preview pada popup menampilkan `Name` ter-pin
201. Klik `[Save]`
202. Scroll tabel System Log secara horizontal
203. Verifikasi kolom `Name` membeku (sticky) saat scroll horizontal
204. Muat ulang halaman (F5)
205. Klik Tab `System Log`
206. Scroll tabel System Log secara horizontal
207. Verifikasi kolom `Name` tetap membeku setelah muat ulang halaman
208. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Name`, lalu klik `[Save]`
209. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon Pin pada `Field`
210. Verifikasi preview pada popup menampilkan `Field` ter-pin
211. Klik `[Save]`
212. Scroll tabel System Log secara horizontal
213. Verifikasi kolom `Field` membeku (sticky) saat scroll horizontal
214. Muat ulang halaman (F5)
215. Klik Tab `System Log`
216. Scroll tabel System Log secara horizontal
217. Verifikasi kolom `Field` tetap membeku setelah muat ulang halaman
218. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Field`, lalu klik `[Save]`
219. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon Pin pada `Old Value`
220. Verifikasi preview pada popup menampilkan `Old Value` ter-pin
221. Klik `[Save]`
222. Scroll tabel System Log secara horizontal
223. Verifikasi kolom `Old Value` membeku (sticky) saat scroll horizontal
224. Muat ulang halaman (F5)
225. Klik Tab `System Log`
226. Scroll tabel System Log secara horizontal
227. Verifikasi kolom `Old Value` tetap membeku setelah muat ulang halaman
228. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Old Value`, lalu klik `[Save]`
229. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon Pin pada `New Value`
230. Verifikasi preview pada popup menampilkan `New Value` ter-pin
231. Klik `[Save]`
232. Scroll tabel System Log secara horizontal
233. Verifikasi kolom `New Value` membeku (sticky) saat scroll horizontal
234. Muat ulang halaman (F5)
235. Klik Tab `System Log`
236. Scroll tabel System Log secara horizontal
237. Verifikasi kolom `New Value` tetap membeku setelah muat ulang halaman
238. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `New Value`, lalu klik `[Save]`
239. Pulihkan lebar viewport ke ukuran semula

### TC-GS-USER-620: Setup Column Reset to Default

240. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Old Value`, seret `Field` ke posisi pertama, lalu klik `[Save]`
241. Verifikasi kolom `Old Value` tidak tampil dan kolom `Field` berada di posisi pertama tabel
242. Klik header Column Visibility (⋯), lalu klik `Setup Column...`
243. Klik `[Reset to Default]`
244. Klik `[Save]`
245. Verifikasi susunan kolom kembali default: `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value` (tujuh kolom tampil)
246. Muat ulang halaman (F5)
247. Klik Tab `System Log`
248. Verifikasi susunan kolom default bertahan setelah muat ulang halaman

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemilik log: TC sumber memakai `Siti Nurhaliza` sebagai pemilik System Log; Setup Column tidak bergantung pada isi baris, tetapi tabel perlu baris agar scroll horizontal dan pin teramati. Spec memakai user milik spec (`Aktor Log`) dengan riwayat yang diketahui (S-06, S-11).
- Urutan TC dalam spec: TC-GS-USER-615, 616, 622, 621, 623, 617, 618, 619, 620. Alasan: dua TC screening (615, 616) di awal; TC-GS-USER-622 (guard), 621 (`[✕]` membuang perubahan), dan 623 (batas pin) tidak menyimpan apa pun sehingga ditaruh sebelum TC yang menyimpan (bagian 3 konvensi: validasi diblokir sebelum aksi sukses); TC-GS-USER-617, 618, 619 menyimpan konfigurasi; TC-GS-USER-620 di akhir karena reset mengembalikan konfigurasi yang diubah TC sebelumnya.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 1 sampai 3 (membuka User Detail; Name dicari di User List), langkah 23, 25, dan 33 (menutup popup tanpa menyimpan sehingga perubahan dibuang), muat ulang halaman lalu membuka kembali Tab `System Log` (langkah F5 tiap kolom pada TC-GS-USER-617 mulai langkah 38, pada TC-GS-USER-618 mulai langkah 122, pada TC-GS-USER-619 tiap kolom sesudah scroll, dan langkah 246; User Detail dibuka pada tab pertama), langkah 167 (reset ke default sebelum TC-GS-USER-619, S-09), langkah 168 (viewport diperkecil agar scroll horizontal teramati), dan langkah 239 (memulihkan viewport). Unpin tiap kolom pada TC-GS-USER-619 (terakhir langkah 238) adalah langkah TC dan sekaligus pemulihan Pin (R-24). Pemulihan Setup Column lainnya: TC-GS-USER-617 mencentang kembali tiap kolom, TC-GS-USER-618 dipulihkan oleh `[Reset to Default]` TC-GS-USER-620, dan hook `after` hanya cadangan. Langkah 241 (observasi perubahan sebelum reset) adalah asersi tambahan agar reset tidak lulus pada konfigurasi yang tidak berubah (S-03).
- Langkah membuka popup (klik header Column Visibility lalu `Setup Column...`) digabung dalam langkah aksi pertama di popup tersebut, karena `[Save]` menutup popup dan tabel diamati sesudahnya.
- Persistensi sesudah muat ulang halaman (F5) diasersi pada setiap kolom di TC-GS-USER-617, 618, dan 619 sesuai Expected TC ("bertahan setelah F5"). Absence kolom sesudah F5 pada TC-GS-USER-617 didahului `Verifikasi` kolom lain tampil sebagai anchor (bagian 8b butir 2).
- Pembagian TC lintas spec: Search, Filter, Sort, Pagination Tab System Log di spec 096 sampai 099; Download di spec 101.
- Spec melewati sekitar 35 langkah (248 langkah) karena TC-GS-USER-617, 618, dan 619 masing-masing menguji tujuh kolom dengan `Verifikasi` per klausa Expected (S-01). Semua blok satu kelas (Setup Column Tab System Log), satu akun, satu dataset, dan tiap blok berdiri sendiri karena konfigurasi dikembalikan di tiap kolom (TC-GS-USER-617 dan 619) atau di-reset (TC-GS-USER-618 dan 620).
- Temuan untuk QA: (1) TC-GS-USER-616 Expected a menyebut "deskripsi panduan" tanpa teks; spec memakai teks deskripsi dari prd-conventions §9.3 (sumber yang dirujuk kolom Referensi TC). (2) TC-GS-USER-618 langkah kedua menggeser `Action` ke posisi pertama padahal `Action` sudah pertama sesudah `Date` dipindah ke posisi terakhir; Expected tidak membedakannya dari kolom lain. (3) TC-GS-USER-619 tidak menyebut lebar viewport atau cara membuat tabel overflow agar scroll horizontal teramati. (4) TC-GS-USER-620 "Ubah urutan dan visibility kolom" tidak menyebut kolom; spec memakai sembunyikan `Old Value` dan seret `Field` ke posisi pertama. (5) TC-GS-USER-622 tidak menyebut kolom yang tersisa; spec menyisakan `Date`. (6) TC-GS-USER-623 tidak menyebut kolom yang di-pin; spec memakai `Date`, `Action`, `Object`, dengan `Name` sebagai kolom keempat. (7) Tempat penyimpanan preferensi Setup Column tab ini tidak disebut TC maupun PRD User.

---
id: TC-GS-USER-E2E-106-tab-user-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset
title: "Tab User Log Detail: Setup Column (Overlay, Popup, Hide, Reorder, Pin, Reset, Tutup, dan Guard)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-655
  - TC-GS-USER-656
  - TC-GS-USER-657
  - TC-GS-USER-658
  - TC-GS-USER-659
  - TC-GS-USER-660
  - TC-GS-USER-661
  - TC-GS-USER-662
  - TC-GS-USER-663
coverage:
  web: automated
---

# Tab User Log Detail: Setup Column (Overlay, Popup, Hide, Reorder, Pin, Reset, Tutup, dan Guard)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22 dan No. 23, 26): hanya dibaca (Division dan Access dipakai sebagai nilai field user seed). TC memakai `John Doe` (Pre-setup No. 18) sebagai pemilik log, sedangkan isi User Log-nya bergantung pada riwayat login lingkungan dan tidak boleh diubah; spec memakai user seed milik spec (S-06, S-11). Spec tidak mengubah atau menghapus data Pre-setup.
- Data Dinamis, di-seed lewat API di hook `before` (seeding minimal, S-11: spec ini mengasersi kolom, bukan isi baris; baris seed hanya agar tabel dan preview Setup Column tampil). User diberi Division `Finance` dan Access `Fixed Asset` (Pre-setup No. 23 dan 26):
  - U-1: Name `John Doe {runId}-106`, email `johndoe+{runId}-106@qwertysystem.net`, status Activated, password `Spectra.env.USER_PASSWORD`. Pemilik User Log yang diuji (pengganti `John Doe` di TC).
  - Riwayat event U-1 (3 event, dipicu berurutan di hook `before`, tanpa Change Password):
    - Event 1 (terlama): Activity `Login`, Status `Success`, Note `—`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS`.
    - Event 2: Activity `Logout`, Status `—`, Note `—`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS`.
    - Event 3 (terbaru): Activity `Login`, Status `Success`, Note `—`, IP Address `10.0.0.11`, Device / Browser `Chrome on Windows`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API U-1, serta sisa user bersuffix `-106` dari run lama. Entri User Log tidak bisa dihapus.
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak menyebut mekanisme maupun endpoint): (a) seeding user berstatus Activated lewat API dengan password `Spectra.env.USER_PASSWORD`; (b) memicu event Login (Success), Logout untuk user uji dengan IP Address dan User-Agent tertentu, berurutan dengan jeda sedikitnya satu detik antar-event supaya cap waktu tiap event berbeda. Event dipicu berurutan sesuai daftar dan bercap waktu hari uji.
- Kemampuan teknis lain: drag and drop item kolom pada Popup Setup Column; hover checkbox disabled dan icon Pin disabled untuk membaca tooltip; mengatur viewport; scroll horizontal tabel; menekan F5 pada konteks browser yang sama.
- Preferensi kolom (visibilitas, urutan, pin) tersimpan per user di browser per tabel dan menjadi permanen setelah `[Save]` (prd-conventions.md §9.3); "muat ulang halaman" dilakukan pada konteks browser yang sama supaya penyimpanan browser tetap ada. Tab aktif User Detail kembali ke Tab Role sesudah F5 (PRD user.md: tab pertama), sehingga tiap F5 diikuti klik Tab `User Log`.
- Lebar konten tabel User Log harus melebihi lebar viewport (overflow horizontal) supaya scroll horizontal pada TC-GS-USER-659 teramati. Viewport disempitkan di langkah 139 dan dikembalikan di langkah 208; ukuran viewport dipilih tim FE karena TC tidak menyebutnya.
- State yang diubah dan dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel User Log dikembalikan ke default (keenam kolom tampil berurutan `Date`, `Activity`, `Status`, `Note`, `IP Address`, `Device / Browser`, tanpa pin) lewat `[Reset to Default]` atau penghapusan preferensi kolom tabel User Log di browser (disediakan tim FE); viewport dikembalikan ke ukuran awal. Preferensi ini milik akun aktor dan dipakai spec 102 sampai 107, sehingga dipulihkan di akhir tiap spec; suite berjalan serial (`parallel: false`).
- Precondition TC-GS-USER-655 sampai 663: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User).

## Test Steps

### TC-GS-USER-655: Screening Overlay Column Visibility Tab User Log

1. Klik icon Search di User List, ketik `John Doe {runId}-106`, tekan Enter
2. Klik Name `John Doe {runId}-106`
3. Klik Tab `User Log`
4. Klik header Column Visibility (⋯)
5. Verifikasi Overlay Column Visibility memuat daftar kolom `Date`, `Activity`, `Status`, `Note`, `IP Address`, dan `Device / Browser`
6. Verifikasi keenam kolom (kelas Hideable) tercentang dan enabled
7. Verifikasi tiap kolom memiliki drag handle
8. Verifikasi item `Setup Column...` tersedia di Overlay

### TC-GS-USER-656: Screening Popup Setup Column Tab User Log

9. Klik item `Setup Column...`
10. Verifikasi Header: Title `Setup Column`
11. Verifikasi Header: deskripsi panduan tampil
12. Verifikasi Header: icon close `[✕]`
13. Verifikasi Body: daftar kolom `Date`, `Activity`, `Status`, `Note`, `IP Address`, dan `Device / Browser` masing-masing dengan checkbox tercentang
14. Verifikasi Body: drag handle pada tiap kolom
15. Verifikasi Body: icon Pin pada tiap kolom
16. Verifikasi Body: preview tabel merefleksikan susunan kolom
17. Verifikasi Footer: tombol `[Reset to Default]` dan `[Save]`
18. Verifikasi Footer: tidak ada tombol `[Cancel]`

### TC-GS-USER-657: Setup Column hide/unhide kelas Hideable

19. Hilangkan centang kolom `Date` (kolom lain tetap tercentang)
20. Verifikasi preview tabel tidak memuat kolom `Date`
21. Klik `[Save]`
22. Verifikasi tabel tidak memuat kolom `Date` (perubahan tersimpan setelah Save)
23. Muat ulang halaman (F5)
24. Klik Tab `User Log`
25. Verifikasi kolom `Activity` tampil di tabel setelah F5
26. Verifikasi kolom `Date` tetap tidak tampil setelah F5
27. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
28. Centang kembali kolom `Date`
29. Klik `[Save]`
30. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
31. Hilangkan centang kolom `Activity` (kolom lain tetap tercentang)
32. Verifikasi preview tabel tidak memuat kolom `Activity`
33. Klik `[Save]`
34. Verifikasi tabel tidak memuat kolom `Activity` (perubahan tersimpan setelah Save)
35. Muat ulang halaman (F5)
36. Klik Tab `User Log`
37. Verifikasi kolom `Date` tampil di tabel setelah F5
38. Verifikasi kolom `Activity` tetap tidak tampil setelah F5
39. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
40. Centang kembali kolom `Activity`
41. Klik `[Save]`
42. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
43. Hilangkan centang kolom `Status` (kolom lain tetap tercentang)
44. Verifikasi preview tabel tidak memuat kolom `Status`
45. Klik `[Save]`
46. Verifikasi tabel tidak memuat kolom `Status` (perubahan tersimpan setelah Save)
47. Muat ulang halaman (F5)
48. Klik Tab `User Log`
49. Verifikasi kolom `Date` tampil di tabel setelah F5
50. Verifikasi kolom `Status` tetap tidak tampil setelah F5
51. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
52. Centang kembali kolom `Status`
53. Klik `[Save]`
54. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
55. Hilangkan centang kolom `Note` (kolom lain tetap tercentang)
56. Verifikasi preview tabel tidak memuat kolom `Note`
57. Klik `[Save]`
58. Verifikasi tabel tidak memuat kolom `Note` (perubahan tersimpan setelah Save)
59. Muat ulang halaman (F5)
60. Klik Tab `User Log`
61. Verifikasi kolom `Date` tampil di tabel setelah F5
62. Verifikasi kolom `Note` tetap tidak tampil setelah F5
63. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
64. Centang kembali kolom `Note`
65. Klik `[Save]`
66. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
67. Hilangkan centang kolom `IP Address` (kolom lain tetap tercentang)
68. Verifikasi preview tabel tidak memuat kolom `IP Address`
69. Klik `[Save]`
70. Verifikasi tabel tidak memuat kolom `IP Address` (perubahan tersimpan setelah Save)
71. Muat ulang halaman (F5)
72. Klik Tab `User Log`
73. Verifikasi kolom `Date` tampil di tabel setelah F5
74. Verifikasi kolom `IP Address` tetap tidak tampil setelah F5
75. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
76. Centang kembali kolom `IP Address`
77. Klik `[Save]`
78. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
79. Hilangkan centang kolom `Device / Browser` (kolom lain tetap tercentang)
80. Verifikasi preview tabel tidak memuat kolom `Device / Browser`
81. Klik `[Save]`
82. Verifikasi tabel tidak memuat kolom `Device / Browser` (perubahan tersimpan setelah Save)
83. Muat ulang halaman (F5)
84. Klik Tab `User Log`
85. Verifikasi kolom `Date` tampil di tabel setelah F5
86. Verifikasi kolom `Device / Browser` tetap tidak tampil setelah F5
87. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
88. Centang kembali kolom `Device / Browser`
89. Klik `[Save]`
90. Verifikasi keenam kolom tampil di tabel

### TC-GS-USER-658: Setup Column drag reorder kelas Hideable

91. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
92. Seret kolom `Date` ke posisi terakhir
93. Verifikasi preview tabel menampilkan kolom `Date` di posisi terakhir
94. Klik `[Save]`
95. Verifikasi kolom `Date` berada di posisi terakhir tabel (perubahan tersimpan setelah Save)
96. Muat ulang halaman (F5)
97. Klik Tab `User Log`
98. Verifikasi kolom `Date` tetap di posisi terakhir tabel setelah F5
99. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
100. Seret kolom `Activity` ke posisi pertama
101. Verifikasi preview tabel menampilkan kolom `Activity` di posisi pertama
102. Klik `[Save]`
103. Verifikasi kolom `Activity` berada di posisi pertama tabel (perubahan tersimpan setelah Save)
104. Muat ulang halaman (F5)
105. Klik Tab `User Log`
106. Verifikasi kolom `Activity` tetap di posisi pertama tabel setelah F5
107. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
108. Seret kolom `Status` ke posisi pertama
109. Verifikasi preview tabel menampilkan kolom `Status` di posisi pertama
110. Klik `[Save]`
111. Verifikasi kolom `Status` berada di posisi pertama tabel (perubahan tersimpan setelah Save)
112. Muat ulang halaman (F5)
113. Klik Tab `User Log`
114. Verifikasi kolom `Status` tetap di posisi pertama tabel setelah F5
115. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
116. Seret kolom `Note` ke posisi pertama
117. Verifikasi preview tabel menampilkan kolom `Note` di posisi pertama
118. Klik `[Save]`
119. Verifikasi kolom `Note` berada di posisi pertama tabel (perubahan tersimpan setelah Save)
120. Muat ulang halaman (F5)
121. Klik Tab `User Log`
122. Verifikasi kolom `Note` tetap di posisi pertama tabel setelah F5
123. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
124. Seret kolom `IP Address` ke posisi pertama
125. Verifikasi preview tabel menampilkan kolom `IP Address` di posisi pertama
126. Klik `[Save]`
127. Verifikasi kolom `IP Address` berada di posisi pertama tabel (perubahan tersimpan setelah Save)
128. Muat ulang halaman (F5)
129. Klik Tab `User Log`
130. Verifikasi kolom `IP Address` tetap di posisi pertama tabel setelah F5
131. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
132. Seret kolom `Device / Browser` ke posisi pertama
133. Verifikasi preview tabel menampilkan kolom `Device / Browser` di posisi pertama
134. Klik `[Save]`
135. Verifikasi kolom `Device / Browser` berada di posisi pertama tabel (perubahan tersimpan setelah Save)
136. Muat ulang halaman (F5)
137. Klik Tab `User Log`
138. Verifikasi kolom `Device / Browser` tetap di posisi pertama tabel setelah F5

### TC-GS-USER-659: Setup Column pin/unpin kelas Hideable

139. Sempitkan viewport sehingga tabel dapat di-scroll horizontal
140. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
141. Klik icon Pin pada `Date`
142. Verifikasi preview tabel menampilkan kolom `Date` ter-pin
143. Klik `[Save]`
144. Scroll tabel secara horizontal
145. Verifikasi kolom `Date` membeku saat scroll horizontal (perubahan tersimpan setelah Save)
146. Muat ulang halaman (F5)
147. Klik Tab `User Log`
148. Scroll tabel secara horizontal
149. Verifikasi kolom `Date` tetap membeku saat scroll horizontal setelah F5
150. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
151. Klik icon Pin pada `Date` untuk unpin
152. Klik icon Pin pada `Activity`
153. Verifikasi preview tabel menampilkan kolom `Activity` ter-pin
154. Klik `[Save]`
155. Scroll tabel secara horizontal
156. Verifikasi kolom `Activity` membeku saat scroll horizontal (perubahan tersimpan setelah Save)
157. Muat ulang halaman (F5)
158. Klik Tab `User Log`
159. Scroll tabel secara horizontal
160. Verifikasi kolom `Activity` tetap membeku saat scroll horizontal setelah F5
161. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
162. Klik icon Pin pada `Activity` untuk unpin
163. Klik icon Pin pada `Status`
164. Verifikasi preview tabel menampilkan kolom `Status` ter-pin
165. Klik `[Save]`
166. Scroll tabel secara horizontal
167. Verifikasi kolom `Status` membeku saat scroll horizontal (perubahan tersimpan setelah Save)
168. Muat ulang halaman (F5)
169. Klik Tab `User Log`
170. Scroll tabel secara horizontal
171. Verifikasi kolom `Status` tetap membeku saat scroll horizontal setelah F5
172. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
173. Klik icon Pin pada `Status` untuk unpin
174. Klik icon Pin pada `Note`
175. Verifikasi preview tabel menampilkan kolom `Note` ter-pin
176. Klik `[Save]`
177. Scroll tabel secara horizontal
178. Verifikasi kolom `Note` membeku saat scroll horizontal (perubahan tersimpan setelah Save)
179. Muat ulang halaman (F5)
180. Klik Tab `User Log`
181. Scroll tabel secara horizontal
182. Verifikasi kolom `Note` tetap membeku saat scroll horizontal setelah F5
183. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
184. Klik icon Pin pada `Note` untuk unpin
185. Klik icon Pin pada `IP Address`
186. Verifikasi preview tabel menampilkan kolom `IP Address` ter-pin
187. Klik `[Save]`
188. Scroll tabel secara horizontal
189. Verifikasi kolom `IP Address` membeku saat scroll horizontal (perubahan tersimpan setelah Save)
190. Muat ulang halaman (F5)
191. Klik Tab `User Log`
192. Scroll tabel secara horizontal
193. Verifikasi kolom `IP Address` tetap membeku saat scroll horizontal setelah F5
194. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
195. Klik icon Pin pada `IP Address` untuk unpin
196. Klik icon Pin pada `Device / Browser`
197. Verifikasi preview tabel menampilkan kolom `Device / Browser` ter-pin
198. Klik `[Save]`
199. Scroll tabel secara horizontal
200. Verifikasi kolom `Device / Browser` membeku saat scroll horizontal (perubahan tersimpan setelah Save)
201. Muat ulang halaman (F5)
202. Klik Tab `User Log`
203. Scroll tabel secara horizontal
204. Verifikasi kolom `Device / Browser` tetap membeku saat scroll horizontal setelah F5
205. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
206. Klik icon Pin pada `Device / Browser` untuk unpin
207. Klik `[Save]`
208. Kembalikan viewport ke ukuran awal

### TC-GS-USER-660: Setup Column Reset to Default

209. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
210. Seret kolom `Date` ke posisi pertama
211. Hilangkan centang kolom `Note`
212. Klik `[Save]`
213. Verifikasi kolom `Date` berada di posisi pertama tabel dan kolom `Note` tidak tampil (susunan sudah diubah dan disimpan)
214. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
215. Klik `[Reset to Default]`
216. Klik `[Save]`
217. Verifikasi susunan kolom kembali default: `Date`, `Activity`, `Status`, `Note`, `IP Address`, `Device / Browser` berurutan dan seluruhnya tampil
218. Muat ulang halaman (F5)
219. Klik Tab `User Log`
220. Verifikasi susunan kolom default bertahan setelah F5

### TC-GS-USER-661: Tutup Setup Column lewat [✕] membuang perubahan

221. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
222. Hilangkan centang kolom `Note`
223. Klik `[✕]`
224. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir (kolom `Note` tampil dengan susunan default)

### TC-GS-USER-662: Guard satu kolom tersisa tidak bisa di-uncheck

225. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
226. Hilangkan centang kolom `Date`
227. Hilangkan centang kolom `Activity`
228. Hilangkan centang kolom `Status`
229. Hilangkan centang kolom `Note`
230. Hilangkan centang kolom `IP Address`
231. Arahkan kursor ke checkbox kolom terakhir `Device / Browser`
232. Verifikasi checkbox kolom `Device / Browser` tetap tampil tercentang namun disabled
233. Verifikasi tooltip `At least one column must remain visible.`
234. Klik `[✕]`

### TC-GS-USER-663: Maksimal 3 kolom di-pin

235. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
236. Klik icon Pin pada `Date`
237. Klik icon Pin pada `Activity`
238. Klik icon Pin pada `Status`
239. Arahkan kursor ke icon Pin kolom keempat `Note`
240. Verifikasi icon Pin kolom `Note` disabled
241. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
242. Klik `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemilik log: TC sumber memakai `John Doe` (Pre-setup No. 18). Spec ini tidak mengasersi isi baris; user milik spec dipakai agar tabel tampil dengan riwayat event yang diketahui dan agar preferensi kolom tidak bergantung pada riwayat lingkungan (S-06).
- Urutan TC dalam spec mengikuti `sourceTc` (655 sampai 663). Dua TC screening (655, 656) di awal sebelum aksi yang mengubah konfigurasi; TC-GS-USER-660 (Reset to Default) sesudah 657 sampai 659 yang mengubah susunan; TC-GS-USER-661 sampai 663 (menutup popup tanpa Save) di akhir sehingga tidak meninggalkan perubahan tersimpan.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 1 (mencari user di User List agar Name dapat diklik); "Klik Tab `User Log`" sesudah tiap F5 (mengembalikan tab karena F5 membuka tab pertama User Detail); "Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`" sebelum tiap blok (popup menutup sesudah `[Save]` dan `[✕]`); langkah "Centang kembali kolom" lalu `[Save]` pada TC-GS-USER-657 dan "Klik icon Pin pada ... untuk unpin" di awal blok kolom berikutnya serta langkah 206 (unpin kolom terakhir sesudah F5); langkah 139 dan 208 (menyempitkan dan mengembalikan viewport); langkah 234 dan 242 (menutup popup tanpa Save agar perubahan checkbox dan pin tidak tersimpan; hook `after` sebagai cadangan).
- Penyimpangan dari TC (dicatat sesuai S-03 dan S-15): TC-GS-USER-659 menulis "Pin, Save, scroll, F5, lalu Unpin" per kolom; unpin tiap kolom dilakukan dalam sesi popup kolom berikutnya (langkah unpin di awal blok) dan unpin kolom terakhir di langkah 206. Absence kolom sesudah F5 pada TC-GS-USER-657 didahului `Verifikasi` kolom lain tampil sebagai anchor (bagian 8b butir 2).
- Spec melewati sekitar 35 langkah (242 langkah) karena TC-GS-USER-657, 658, dan 659 masing-masing menguji enam kolom dengan blok identik (buka popup, ubah, Save, cek, F5, cek) dan tujuh TC lain memakai popup dan overlay Setup Column yang sama; semuanya satu kelas harness (fungsional), satu akun, dan satu dataset. Tiap blok kolom berdiri sendiri. Langkah pembuka popup dan F5 yang berulang merupakan prefix berulang.
- Pembagian TC lintas spec: Screening dan Search TC-GS-USER-409, 411, 412, 631 sampai 637 diverifikasi di spec 102 (TC-GS-USER-636 memakai Overlay Column Visibility); Filter Panel TC-GS-USER-638 sampai 646 di spec 103; kombinasi Search dan Filter TC-GS-USER-647 sampai 651 di spec 104; Sort, Pagination, dan kombinasi TC-GS-USER-652 sampai 654, 669, 670 di spec 105; Download TC-GS-USER-410 dan 664 sampai 668 di spec 107. Isolasi Setup Column antar sub-tab (TC-GS-USER-992 dan 993) diverifikasi di spec 158.
- Temuan untuk QA: (1) TC-GS-USER-655 sampai 663 memakai `John Doe` Pre-setup; spec memakai user seed milik spec. (2) Mekanisme memicu event Login dan Logout dengan IP Address dan User-Agent tertentu tidak disebut di TC, PRD, dan LLD; disediakan tim FE/BE. (3) TC-GS-USER-655 langkah 3 menyebut header `Actions (⋯)`, sedangkan TC-GS-USER-656 menyebutnya (⋯) dan TC lain `Column Visibility (⋯)`; spec memakai `Column Visibility (⋯)`. (4) TC-GS-USER-656 Expected a menyebut "deskripsi panduan" tanpa teks; spec hanya mengasersi deskripsi tampil. (5) TC-GS-USER-658 langkah kedua menggeser `Activity` ke posisi pertama padahal `Activity` sudah pertama sesudah `Date` dipindah ke posisi terakhir; Expected tidak membedakannya dari kolom lain. (6) TC-GS-USER-659 tidak menyebut ukuran viewport; tim FE perlu menetapkannya. (7) TC-GS-USER-660 langkah 3 tidak menyebut perubahan konkret; spec menyeret `Date` ke posisi pertama dan menyembunyikan `Note`. (8) TC-GS-USER-657 sampai 659 Expected "bertahan setelah F5" memerlukan klik Tab `User Log` sesudah F5 karena Detail membuka Tab Role; TC tidak menyebut langkah itu. (9) Mekanisme menandai Guided Tooltip sebagai sudah dilihat dan menghapus preferensi kolom di browser tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.

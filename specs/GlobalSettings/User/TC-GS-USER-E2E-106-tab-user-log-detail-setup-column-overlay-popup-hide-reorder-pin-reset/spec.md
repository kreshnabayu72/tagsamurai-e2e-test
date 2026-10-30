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
- Lebar konten tabel User Log harus melebihi lebar viewport (overflow horizontal) supaya scroll horizontal pada TC-GS-USER-659 teramati. Viewport disempitkan di langkah 123 dan dikembalikan di langkah 192; ukuran viewport dipilih tim FE karena TC tidak menyebutnya.
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
11. Verifikasi Header: deskripsi panduan `Manage column visibility, reorder, and freeze columns.`
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
25. Verifikasi kolom `Date` tetap tidak tampil setelah F5
26. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
27. Centang kembali kolom `Date`
28. Hilangkan centang kolom `Activity` (kolom lain tetap tercentang)
29. Verifikasi preview tabel tidak memuat kolom `Activity`
30. Klik `[Save]`
31. Verifikasi tabel tidak memuat kolom `Activity` (perubahan tersimpan setelah Save)
32. Muat ulang halaman (F5)
33. Klik Tab `User Log`
34. Verifikasi kolom `Activity` tetap tidak tampil setelah F5
35. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
36. Centang kembali kolom `Activity`
37. Hilangkan centang kolom `Status` (kolom lain tetap tercentang)
38. Verifikasi preview tabel tidak memuat kolom `Status`
39. Klik `[Save]`
40. Verifikasi tabel tidak memuat kolom `Status` (perubahan tersimpan setelah Save)
41. Muat ulang halaman (F5)
42. Klik Tab `User Log`
43. Verifikasi kolom `Status` tetap tidak tampil setelah F5
44. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
45. Centang kembali kolom `Status`
46. Hilangkan centang kolom `Note` (kolom lain tetap tercentang)
47. Verifikasi preview tabel tidak memuat kolom `Note`
48. Klik `[Save]`
49. Verifikasi tabel tidak memuat kolom `Note` (perubahan tersimpan setelah Save)
50. Muat ulang halaman (F5)
51. Klik Tab `User Log`
52. Verifikasi kolom `Note` tetap tidak tampil setelah F5
53. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
54. Centang kembali kolom `Note`
55. Hilangkan centang kolom `IP Address` (kolom lain tetap tercentang)
56. Verifikasi preview tabel tidak memuat kolom `IP Address`
57. Klik `[Save]`
58. Verifikasi tabel tidak memuat kolom `IP Address` (perubahan tersimpan setelah Save)
59. Muat ulang halaman (F5)
60. Klik Tab `User Log`
61. Verifikasi kolom `IP Address` tetap tidak tampil setelah F5
62. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
63. Centang kembali kolom `IP Address`
64. Hilangkan centang kolom `Device / Browser` (kolom lain tetap tercentang)
65. Verifikasi preview tabel tidak memuat kolom `Device / Browser`
66. Klik `[Save]`
67. Verifikasi tabel tidak memuat kolom `Device / Browser` (perubahan tersimpan setelah Save)
68. Muat ulang halaman (F5)
69. Klik Tab `User Log`
70. Verifikasi kolom `Device / Browser` tetap tidak tampil setelah F5
71. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
72. Centang kembali kolom `Device / Browser`
73. Klik `[Save]`
74. Verifikasi keenam kolom tampil di tabel

### TC-GS-USER-658: Setup Column drag reorder kelas Hideable

75. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
76. Seret kolom `Date` ke posisi pertama
77. Verifikasi preview tabel menampilkan kolom `Date` di posisi pertama
78. Klik `[Save]`
79. Verifikasi kolom `Date` berada di posisi pertama tabel (perubahan tersimpan setelah Save)
80. Muat ulang halaman (F5)
81. Klik Tab `User Log`
82. Verifikasi kolom `Date` tetap di posisi pertama tabel setelah F5
83. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
84. Seret kolom `Activity` ke posisi pertama
85. Verifikasi preview tabel menampilkan kolom `Activity` di posisi pertama
86. Klik `[Save]`
87. Verifikasi kolom `Activity` berada di posisi pertama tabel (perubahan tersimpan setelah Save)
88. Muat ulang halaman (F5)
89. Klik Tab `User Log`
90. Verifikasi kolom `Activity` tetap di posisi pertama tabel setelah F5
91. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
92. Seret kolom `Status` ke posisi pertama
93. Verifikasi preview tabel menampilkan kolom `Status` di posisi pertama
94. Klik `[Save]`
95. Verifikasi kolom `Status` berada di posisi pertama tabel (perubahan tersimpan setelah Save)
96. Muat ulang halaman (F5)
97. Klik Tab `User Log`
98. Verifikasi kolom `Status` tetap di posisi pertama tabel setelah F5
99. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
100. Seret kolom `Note` ke posisi pertama
101. Verifikasi preview tabel menampilkan kolom `Note` di posisi pertama
102. Klik `[Save]`
103. Verifikasi kolom `Note` berada di posisi pertama tabel (perubahan tersimpan setelah Save)
104. Muat ulang halaman (F5)
105. Klik Tab `User Log`
106. Verifikasi kolom `Note` tetap di posisi pertama tabel setelah F5
107. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
108. Seret kolom `IP Address` ke posisi pertama
109. Verifikasi preview tabel menampilkan kolom `IP Address` di posisi pertama
110. Klik `[Save]`
111. Verifikasi kolom `IP Address` berada di posisi pertama tabel (perubahan tersimpan setelah Save)
112. Muat ulang halaman (F5)
113. Klik Tab `User Log`
114. Verifikasi kolom `IP Address` tetap di posisi pertama tabel setelah F5
115. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
116. Seret kolom `Device / Browser` ke posisi pertama
117. Verifikasi preview tabel menampilkan kolom `Device / Browser` di posisi pertama
118. Klik `[Save]`
119. Verifikasi kolom `Device / Browser` berada di posisi pertama tabel (perubahan tersimpan setelah Save)
120. Muat ulang halaman (F5)
121. Klik Tab `User Log`
122. Verifikasi kolom `Device / Browser` tetap di posisi pertama tabel setelah F5

### TC-GS-USER-659: Setup Column pin/unpin kelas Hideable

123. Sempitkan viewport sehingga tabel dapat di-scroll horizontal
124. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
125. Klik icon Pin pada `Date`
126. Verifikasi preview tabel menampilkan kolom `Date` ter-pin
127. Klik `[Save]`
128. Scroll tabel secara horizontal
129. Verifikasi kolom `Date` membeku saat scroll horizontal (perubahan tersimpan setelah Save)
130. Muat ulang halaman (F5)
131. Klik Tab `User Log`
132. Scroll tabel secara horizontal
133. Verifikasi kolom `Date` tetap membeku saat scroll horizontal setelah F5
134. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
135. Klik icon Pin pada `Date` untuk unpin
136. Klik icon Pin pada `Activity`
137. Verifikasi preview tabel menampilkan kolom `Activity` ter-pin
138. Klik `[Save]`
139. Scroll tabel secara horizontal
140. Verifikasi kolom `Activity` membeku saat scroll horizontal (perubahan tersimpan setelah Save)
141. Muat ulang halaman (F5)
142. Klik Tab `User Log`
143. Scroll tabel secara horizontal
144. Verifikasi kolom `Activity` tetap membeku saat scroll horizontal setelah F5
145. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
146. Klik icon Pin pada `Activity` untuk unpin
147. Klik icon Pin pada `Status`
148. Verifikasi preview tabel menampilkan kolom `Status` ter-pin
149. Klik `[Save]`
150. Scroll tabel secara horizontal
151. Verifikasi kolom `Status` membeku saat scroll horizontal (perubahan tersimpan setelah Save)
152. Muat ulang halaman (F5)
153. Klik Tab `User Log`
154. Scroll tabel secara horizontal
155. Verifikasi kolom `Status` tetap membeku saat scroll horizontal setelah F5
156. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
157. Klik icon Pin pada `Status` untuk unpin
158. Klik icon Pin pada `Note`
159. Verifikasi preview tabel menampilkan kolom `Note` ter-pin
160. Klik `[Save]`
161. Scroll tabel secara horizontal
162. Verifikasi kolom `Note` membeku saat scroll horizontal (perubahan tersimpan setelah Save)
163. Muat ulang halaman (F5)
164. Klik Tab `User Log`
165. Scroll tabel secara horizontal
166. Verifikasi kolom `Note` tetap membeku saat scroll horizontal setelah F5
167. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
168. Klik icon Pin pada `Note` untuk unpin
169. Klik icon Pin pada `IP Address`
170. Verifikasi preview tabel menampilkan kolom `IP Address` ter-pin
171. Klik `[Save]`
172. Scroll tabel secara horizontal
173. Verifikasi kolom `IP Address` membeku saat scroll horizontal (perubahan tersimpan setelah Save)
174. Muat ulang halaman (F5)
175. Klik Tab `User Log`
176. Scroll tabel secara horizontal
177. Verifikasi kolom `IP Address` tetap membeku saat scroll horizontal setelah F5
178. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
179. Klik icon Pin pada `IP Address` untuk unpin
180. Klik icon Pin pada `Device / Browser`
181. Verifikasi preview tabel menampilkan kolom `Device / Browser` ter-pin
182. Klik `[Save]`
183. Scroll tabel secara horizontal
184. Verifikasi kolom `Device / Browser` membeku saat scroll horizontal (perubahan tersimpan setelah Save)
185. Muat ulang halaman (F5)
186. Klik Tab `User Log`
187. Scroll tabel secara horizontal
188. Verifikasi kolom `Device / Browser` tetap membeku saat scroll horizontal setelah F5
189. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
190. Klik icon Pin pada `Device / Browser` untuk unpin
191. Klik `[Save]`
192. Kembalikan viewport ke ukuran awal

### TC-GS-USER-660: Setup Column Reset to Default

193. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
194. Seret kolom `Date` ke posisi pertama
195. Hilangkan centang kolom `Note`
196. Klik `[Save]`
197. Verifikasi kolom `Date` berada di posisi pertama tabel dan kolom `Note` tidak tampil (susunan sudah diubah dan disimpan)
198. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
199. Klik `[Reset to Default]`
200. Klik `[Save]`
201. Verifikasi susunan kolom kembali default: `Date`, `Activity`, `Status`, `Note`, `IP Address`, `Device / Browser` berurutan dan seluruhnya tampil
202. Muat ulang halaman (F5)
203. Klik Tab `User Log`
204. Verifikasi susunan kolom default bertahan setelah F5

### TC-GS-USER-661: Tutup Setup Column lewat [✕] membuang perubahan

205. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
206. Hilangkan centang kolom `Note`
207. Klik `[✕]`
208. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir (kolom `Note` tampil dengan susunan default)

### TC-GS-USER-662: Guard satu kolom tersisa tidak bisa di-uncheck

209. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
210. Hilangkan centang kolom `Date`
211. Hilangkan centang kolom `Activity`
212. Hilangkan centang kolom `Status`
213. Hilangkan centang kolom `Note`
214. Hilangkan centang kolom `IP Address`
215. Arahkan kursor ke checkbox kolom terakhir `Device / Browser`
216. Verifikasi checkbox kolom `Device / Browser` tetap tampil tercentang namun disabled
217. Verifikasi tooltip `At least one column must remain visible.`
218. Klik `[✕]`

### TC-GS-USER-663: Maksimal 3 kolom di-pin

219. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
220. Klik icon Pin pada `Date`
221. Klik icon Pin pada `Activity`
222. Klik icon Pin pada `Status`
223. Arahkan kursor ke icon Pin kolom keempat `Note`
224. Verifikasi icon Pin kolom `Note` disabled
225. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
226. Klik `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemilik log: TC sumber memakai `John Doe` (Pre-setup No. 18). Spec ini tidak mengasersi isi baris; user milik spec dipakai agar tabel tampil dengan riwayat event yang diketahui dan agar preferensi kolom tidak bergantung pada riwayat lingkungan (S-06).
- Urutan TC dalam spec mengikuti `sourceTc` (655 sampai 663). Dua TC screening (655, 656) di awal sebelum aksi yang mengubah konfigurasi; TC-GS-USER-660 (Reset to Default) sesudah 657 sampai 659 yang mengubah susunan; TC-GS-USER-661 sampai 663 (menutup popup tanpa Save) di akhir sehingga tidak meninggalkan perubahan tersimpan.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 1 (mencari user di User List agar Name dapat diklik); "Klik Tab `User Log`" sesudah tiap F5 (mengembalikan tab karena F5 membuka tab pertama User Detail); "Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`" sebelum tiap blok (popup menutup sesudah `[Save]` dan `[✕]`); langkah "Centang kembali kolom" dan "Klik icon Pin pada ... untuk unpin" di awal blok kolom berikutnya serta langkah 73 dan 190 (memulihkan visibilitas dan pin kolom sebelumnya sekaligus dengan perubahan kolom berikutnya dalam satu sesi popup); langkah 123 dan 192 (menyempitkan dan mengembalikan viewport); langkah 218 dan 226 (menutup popup tanpa Save agar perubahan checkbox dan pin tidak tersimpan; hook `after` sebagai cadangan).
- Penyimpangan dari TC (dicatat sesuai S-03 dan S-15): TC-GS-USER-657 menulis "uncheck lalu check" per kolom; spec melakukan uncheck, Save, F5 (hide teramati tersimpan dan bertahan), lalu centang kembali kolom itu bersama uncheck kolom berikutnya; kolom terakhir dicentang kembali di langkah 73. TC-GS-USER-659 menulis "Pin, Save, scroll, F5, lalu Unpin" per kolom; unpin tiap kolom dilakukan dalam sesi popup kolom berikutnya (langkah unpin di awal blok) dan unpin kolom terakhir di langkah 190.
- Spec melewati sekitar 35 langkah (226 langkah) karena TC-GS-USER-657, 658, dan 659 masing-masing menguji enam kolom dengan blok identik (buka popup, ubah, Save, cek, F5, cek) dan tujuh TC lain memakai popup dan overlay Setup Column yang sama; semuanya satu kelas harness (fungsional), satu akun, dan satu dataset. Tiap blok kolom berdiri sendiri. Langkah pembuka popup dan F5 yang berulang merupakan prefix berulang.
- Pembagian TC lintas spec: Screening dan Search TC-GS-USER-409, 411, 412, 631 sampai 637 diverifikasi di spec 102 (TC-GS-USER-636 memakai Overlay Column Visibility); Filter Panel TC-GS-USER-638 sampai 646 di spec 103; kombinasi Search dan Filter TC-GS-USER-647 sampai 651 di spec 104; Sort, Pagination, dan kombinasi TC-GS-USER-652 sampai 654, 669, 670 di spec 105; Download TC-GS-USER-410 dan 664 sampai 668 di spec 107. Isolasi Setup Column antar sub-tab (TC-GS-USER-992 dan 993) diverifikasi di spec 158.
- Temuan untuk QA: (1) TC-GS-USER-655 sampai 663 memakai `John Doe` Pre-setup; spec memakai user seed milik spec. (2) Mekanisme memicu event Login dan Logout dengan IP Address dan User-Agent tertentu tidak disebut di TC, PRD, dan LLD; disediakan tim FE/BE. (3) TC-GS-USER-655 Expected b menyebut "kolom Curated unchecked & enabled", sedangkan seluruh kolom Tab User Log berkelas Hideable (PRD user.md §4.1.7); spec tidak mengasersi kolom Curated. (4) TC-GS-USER-655 langkah 3 menyebut header `Actions (⋯)`, sedangkan TC-GS-USER-656 menyebutnya (⋯) dan TC lain `Column Visibility (⋯)`; spec memakai `Column Visibility (⋯)`. (5) TC-GS-USER-656 Expected a menyebut "deskripsi panduan" tanpa teks; spec memakai teks Setup Column yang sama dengan PRD Division dan General Settings (`Manage column visibility, reorder, and freeze columns.`). (6) TC-GS-USER-657 dan 658: "uncheck lalu check" tidak mengubah konfigurasi akhir, dan kolom `Date` sudah berada di posisi pertama pada default sehingga "geser ke posisi pertama" tidak mengubah urutan (langkah drag `Date` tetap ditulis); spec mengikuti penafsiran di catatan penyimpangan. (7) TC-GS-USER-659 tidak menyebut ukuran viewport; tim FE perlu menetapkannya. (8) TC-GS-USER-660 langkah 3 tidak menyebut perubahan konkret; spec menyeret `Date` ke posisi pertama dan menyembunyikan `Note`. (9) TC-GS-USER-657 sampai 659 Expected "bertahan setelah F5" memerlukan klik Tab `User Log` sesudah F5 karena Detail membuka Tab Role; TC tidak menyebut langkah itu. (10) Mekanisme menandai Guided Tooltip sebagai sudah dilihat dan menghapus preferensi kolom di browser tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.

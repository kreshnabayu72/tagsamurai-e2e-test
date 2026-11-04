---
id: TC-GS-USER-E2E-082-modal-changelog-user-setup-column-overlay-popup-hide-reorder-pin-reset
title: "Modal Changelog User: Setup Column (Overlay, Popup, Hide/Unhide, Reorder, Pin/Unpin, Reset to Default, Guard Kolom Terakhir, dan Batas 3 Pin)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-494
  - TC-GS-USER-495
  - TC-GS-USER-496
  - TC-GS-USER-497
  - TC-GS-USER-498
  - TC-GS-USER-499
  - TC-GS-USER-500
  - TC-GS-USER-501
  - TC-GS-USER-502
coverage:
  web: automated
---

# Modal Changelog User: Setup Column (Overlay, Popup, Hide/Unhide, Reorder, Pin/Unpin, Reset to Default, Guard Kolom Terakhir, dan Batas 3 Pin)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2); kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite: login di hook `before`, hook `after` mengembalikan sesi ke akun ini. Nama singkat di kolom Modified By: `Siti N` (tooltip `Siti Nurhaliza`). Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Seeding minimal (S-11; lewat API di hook `before`; kemampuan seeding user dan perubahan user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD. Tiap user seed diberi Position `Staff` (Tabel Data Uji Pre-setup No. 22), Division `Finance` (No. 23), dan Access `Fixed Asset` (No. 26), email `<nama>+{runId}-082@qwertysystem.net`. Kuota user plan cukup untuk user seed milik spec ini (disediakan tim FE). Spec ini hanya memeriksa kolom, bukan isi baris): U-1 Create `Alfa {runId}-082` oleh Siti Nurhaliza (entri Action Create), agar riwayat Changelog terisi dan preview tabel di popup Setup Column memuat baris.
- Konfigurasi kolom (urutan, visibilitas, pin) tersimpan di `localStorage` browser dengan key unik per tabel (prd-conventions.md §9.3). Hook `before` mengosongkan konfigurasi kolom Modal Changelog User sehingga spec mulai dari default (urutan `Date` pertama, 7 kolom tampil, tanpa pin). "Muat ulang halaman" dilakukan pada konteks browser yang sama supaya `localStorage` tetap ada.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API U-1 bila masih ada; pulihkan konfigurasi kolom Modal Changelog User ke default lewat `[Reset to Default]` atau penghapusan key `localStorage` tabel itu; kembalikan viewport ke bawaan; kembalikan sesi ke akun default suite. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: drag and drop elemen daftar kolom; hover icon pin dan checkbox yang disabled (tooltip); mengatur lebar viewport sehingga tabel Changelog dapat di-scroll horizontal (TC tidak menyebut lebar viewport; viewport diperkecil sampai overflow horizontal); scroll horizontal tabel; membaca dan menghapus key `localStorage` browser.
- Precondition TC-GS-USER-494 sampai 502: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User).
- Suite serial (`parallel: false`). Changelog bersifat append-only dan dipakai bersama spec lain: asersi memakai pola baris (nilai bersuffix `{runId}-082`), bukan jumlah baris total, kecuali dinyatakan lain. Spec ini tidak mengubah atau menghapus data Pre-setup (S-06).
- State global yang diubah: konfigurasi kolom Modal Changelog User (visibilitas, urutan, pin) dan lebar viewport. Spec memulihkannya di langkah 139 sampai 213 dan di hook `after`.

## Test Steps

### TC-GS-USER-494: Screening Overlay Column Visibility
1. Klik icon Changelog di Table Tools
2. Klik header Column Visibility (⋯)
3. Verifikasi overlay memuat daftar kolom `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, `Modified By`
4. Verifikasi ketujuh kolom Hideable tercentang dan enabled
5. Verifikasi drag handle tersedia pada ketujuh kolom
6. Verifikasi item `Setup Column...` tersedia di overlay
### TC-GS-USER-495: Screening Popup Setup Column
7. Klik item `Setup Column...` pada overlay
8. Verifikasi Header: Title `Setup Column`
9. Verifikasi Header: deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
10. Verifikasi Header: icon `[✕]`
11. Verifikasi Body: daftar kolom dengan checkbox
12. Verifikasi Body: drag handle
13. Verifikasi Body: icon Pin
14. Verifikasi Body: preview tabel
15. Verifikasi Footer: `[Reset to Default]` dan `[Save]` tampil
16. Verifikasi Footer: tidak ada `[Cancel]`
17. Klik `[✕]` untuk menutup popup tanpa perubahan
### TC-GS-USER-501: Guard satu kolom tersisa tidak bisa di-uncheck
18. Klik header Column Visibility (⋯), klik `Setup Column...`
19. Hilangkan centang enam kolom: `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value` (tersisa `Modified By`)
20. Hover checkbox `Modified By`
21. Verifikasi checkbox `Modified By` tampil namun disabled
22. Verifikasi Tooltip `At least one column must remain visible.`
23. Klik `[✕]` untuk menutup popup tanpa menyimpan
### TC-GS-USER-502: Maksimal 3 kolom di-pin
24. Klik header Column Visibility (⋯), klik `Setup Column...`
25. Klik icon pin pada `Date`, `Action`, dan `User Name`
26. Hover icon pin kolom keempat (`Field`)
27. Verifikasi icon pin `Field` disabled
28. Verifikasi Tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
29. Klik `[✕]` untuk menutup popup tanpa menyimpan
### TC-GS-USER-500: Tutup Setup Column via [✕] membuang perubahan
30. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Field`
31. Klik `[✕]`
32. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir (kolom `Field` tetap tampil)
### TC-GS-USER-496: Hide dan unhide kolom kelas Hideable
33. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Date`
34. Verifikasi kolom `Date`: perubahan tampil di preview tabel popup (kolom `Date` tidak tampil)
35. Klik `[Save]`
36. Verifikasi kolom `Date`: tersimpan setelah Save (kolom `Date` tidak tampil di tabel)
37. Muat ulang halaman (F5)
38. Klik icon Changelog di Table Tools
39. Verifikasi kolom lain (`Action`) tampil di tabel setelah F5
40. Verifikasi kolom `Date`: bertahan setelah F5 (kolom `Date` tetap tidak tampil)
41. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Date`, lalu hilangkan centang `Action`
42. Verifikasi kolom `Action`: perubahan tampil di preview tabel popup (kolom `Action` tidak tampil)
43. Klik `[Save]`
44. Verifikasi kolom `Action`: tersimpan setelah Save (kolom `Action` tidak tampil di tabel)
45. Muat ulang halaman (F5)
46. Klik icon Changelog di Table Tools
47. Verifikasi kolom lain (`Date`) tampil di tabel setelah F5
48. Verifikasi kolom `Action`: bertahan setelah F5 (kolom `Action` tetap tidak tampil)
49. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Action`, lalu hilangkan centang `User Name`
50. Verifikasi kolom `User Name`: perubahan tampil di preview tabel popup (kolom `User Name` tidak tampil)
51. Klik `[Save]`
52. Verifikasi kolom `User Name`: tersimpan setelah Save (kolom `User Name` tidak tampil di tabel)
53. Muat ulang halaman (F5)
54. Klik icon Changelog di Table Tools
55. Verifikasi kolom lain (`Date`) tampil di tabel setelah F5
56. Verifikasi kolom `User Name`: bertahan setelah F5 (kolom `User Name` tetap tidak tampil)
57. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `User Name`, lalu hilangkan centang `Field`
58. Verifikasi kolom `Field`: perubahan tampil di preview tabel popup (kolom `Field` tidak tampil)
59. Klik `[Save]`
60. Verifikasi kolom `Field`: tersimpan setelah Save (kolom `Field` tidak tampil di tabel)
61. Muat ulang halaman (F5)
62. Klik icon Changelog di Table Tools
63. Verifikasi kolom lain (`Date`) tampil di tabel setelah F5
64. Verifikasi kolom `Field`: bertahan setelah F5 (kolom `Field` tetap tidak tampil)
65. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Field`, lalu hilangkan centang `Old Value`
66. Verifikasi kolom `Old Value`: perubahan tampil di preview tabel popup (kolom `Old Value` tidak tampil)
67. Klik `[Save]`
68. Verifikasi kolom `Old Value`: tersimpan setelah Save (kolom `Old Value` tidak tampil di tabel)
69. Muat ulang halaman (F5)
70. Klik icon Changelog di Table Tools
71. Verifikasi kolom lain (`Date`) tampil di tabel setelah F5
72. Verifikasi kolom `Old Value`: bertahan setelah F5 (kolom `Old Value` tetap tidak tampil)
73. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Old Value`, lalu hilangkan centang `New Value`
74. Verifikasi kolom `New Value`: perubahan tampil di preview tabel popup (kolom `New Value` tidak tampil)
75. Klik `[Save]`
76. Verifikasi kolom `New Value`: tersimpan setelah Save (kolom `New Value` tidak tampil di tabel)
77. Muat ulang halaman (F5)
78. Klik icon Changelog di Table Tools
79. Verifikasi kolom lain (`Date`) tampil di tabel setelah F5
80. Verifikasi kolom `New Value`: bertahan setelah F5 (kolom `New Value` tetap tidak tampil)
81. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `New Value`, lalu hilangkan centang `Modified By`
82. Verifikasi kolom `Modified By`: perubahan tampil di preview tabel popup (kolom `Modified By` tidak tampil)
83. Klik `[Save]`
84. Verifikasi kolom `Modified By`: tersimpan setelah Save (kolom `Modified By` tidak tampil di tabel)
85. Muat ulang halaman (F5)
86. Klik icon Changelog di Table Tools
87. Verifikasi kolom lain (`Date`) tampil di tabel setelah F5
88. Verifikasi kolom `Modified By`: bertahan setelah F5 (kolom `Modified By` tetap tidak tampil)
89. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Modified By`, lalu klik `[Save]`
### TC-GS-USER-497: Drag reorder kolom kelas Hideable
90. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Date` ke posisi pertama
91. Verifikasi kolom `Date`: perubahan tampil di preview tabel popup (kolom `Date` di posisi pertama)
92. Klik `[Save]`
93. Verifikasi kolom `Date`: tersimpan setelah Save (kolom `Date` berada di posisi pertama tabel)
94. Muat ulang halaman (F5)
95. Klik icon Changelog di Table Tools
96. Verifikasi kolom `Date`: bertahan setelah F5 (kolom `Date` tetap di posisi pertama)
97. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Action` ke posisi pertama
98. Verifikasi kolom `Action`: perubahan tampil di preview tabel popup (kolom `Action` di posisi pertama)
99. Klik `[Save]`
100. Verifikasi kolom `Action`: tersimpan setelah Save (kolom `Action` berada di posisi pertama tabel)
101. Muat ulang halaman (F5)
102. Klik icon Changelog di Table Tools
103. Verifikasi kolom `Action`: bertahan setelah F5 (kolom `Action` tetap di posisi pertama)
104. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `User Name` ke posisi pertama
105. Verifikasi kolom `User Name`: perubahan tampil di preview tabel popup (kolom `User Name` di posisi pertama)
106. Klik `[Save]`
107. Verifikasi kolom `User Name`: tersimpan setelah Save (kolom `User Name` berada di posisi pertama tabel)
108. Muat ulang halaman (F5)
109. Klik icon Changelog di Table Tools
110. Verifikasi kolom `User Name`: bertahan setelah F5 (kolom `User Name` tetap di posisi pertama)
111. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Field` ke posisi pertama
112. Verifikasi kolom `Field`: perubahan tampil di preview tabel popup (kolom `Field` di posisi pertama)
113. Klik `[Save]`
114. Verifikasi kolom `Field`: tersimpan setelah Save (kolom `Field` berada di posisi pertama tabel)
115. Muat ulang halaman (F5)
116. Klik icon Changelog di Table Tools
117. Verifikasi kolom `Field`: bertahan setelah F5 (kolom `Field` tetap di posisi pertama)
118. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Old Value` ke posisi pertama
119. Verifikasi kolom `Old Value`: perubahan tampil di preview tabel popup (kolom `Old Value` di posisi pertama)
120. Klik `[Save]`
121. Verifikasi kolom `Old Value`: tersimpan setelah Save (kolom `Old Value` berada di posisi pertama tabel)
122. Muat ulang halaman (F5)
123. Klik icon Changelog di Table Tools
124. Verifikasi kolom `Old Value`: bertahan setelah F5 (kolom `Old Value` tetap di posisi pertama)
125. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `New Value` ke posisi pertama
126. Verifikasi kolom `New Value`: perubahan tampil di preview tabel popup (kolom `New Value` di posisi pertama)
127. Klik `[Save]`
128. Verifikasi kolom `New Value`: tersimpan setelah Save (kolom `New Value` berada di posisi pertama tabel)
129. Muat ulang halaman (F5)
130. Klik icon Changelog di Table Tools
131. Verifikasi kolom `New Value`: bertahan setelah F5 (kolom `New Value` tetap di posisi pertama)
132. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Modified By` ke posisi pertama
133. Verifikasi kolom `Modified By`: perubahan tampil di preview tabel popup (kolom `Modified By` di posisi pertama)
134. Klik `[Save]`
135. Verifikasi kolom `Modified By`: tersimpan setelah Save (kolom `Modified By` berada di posisi pertama tabel)
136. Muat ulang halaman (F5)
137. Klik icon Changelog di Table Tools
138. Verifikasi kolom `Modified By`: bertahan setelah F5 (kolom `Modified By` tetap di posisi pertama)
### TC-GS-USER-498: Pin dan unpin kolom kelas Hideable
139. Klik header Column Visibility (⋯), klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`
140. Perkecil lebar viewport hingga tabel Changelog dapat di-scroll horizontal
141. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon pin pada `Date`
142. Verifikasi kolom `Date`: perubahan tampil di preview tabel popup (kolom `Date` ter-pin)
143. Klik `[Save]`
144. Scroll tabel Changelog secara horizontal
145. Verifikasi kolom `Date`: tersimpan setelah Save (kolom `Date` membeku saat scroll horizontal)
146. Muat ulang halaman (F5)
147. Klik icon Changelog di Table Tools
148. Scroll tabel Changelog secara horizontal
149. Verifikasi kolom `Date`: bertahan setelah F5 (kolom `Date` tetap membeku saat scroll horizontal)
150. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Date`, lalu klik icon pin pada `Action`
151. Verifikasi kolom `Action`: perubahan tampil di preview tabel popup (kolom `Action` ter-pin)
152. Klik `[Save]`
153. Scroll tabel Changelog secara horizontal
154. Verifikasi kolom `Action`: tersimpan setelah Save (kolom `Action` membeku saat scroll horizontal)
155. Muat ulang halaman (F5)
156. Klik icon Changelog di Table Tools
157. Scroll tabel Changelog secara horizontal
158. Verifikasi kolom `Action`: bertahan setelah F5 (kolom `Action` tetap membeku saat scroll horizontal)
159. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Action`, lalu klik icon pin pada `User Name`
160. Verifikasi kolom `User Name`: perubahan tampil di preview tabel popup (kolom `User Name` ter-pin)
161. Klik `[Save]`
162. Scroll tabel Changelog secara horizontal
163. Verifikasi kolom `User Name`: tersimpan setelah Save (kolom `User Name` membeku saat scroll horizontal)
164. Muat ulang halaman (F5)
165. Klik icon Changelog di Table Tools
166. Scroll tabel Changelog secara horizontal
167. Verifikasi kolom `User Name`: bertahan setelah F5 (kolom `User Name` tetap membeku saat scroll horizontal)
168. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `User Name`, lalu klik icon pin pada `Field`
169. Verifikasi kolom `Field`: perubahan tampil di preview tabel popup (kolom `Field` ter-pin)
170. Klik `[Save]`
171. Scroll tabel Changelog secara horizontal
172. Verifikasi kolom `Field`: tersimpan setelah Save (kolom `Field` membeku saat scroll horizontal)
173. Muat ulang halaman (F5)
174. Klik icon Changelog di Table Tools
175. Scroll tabel Changelog secara horizontal
176. Verifikasi kolom `Field`: bertahan setelah F5 (kolom `Field` tetap membeku saat scroll horizontal)
177. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Field`, lalu klik icon pin pada `Old Value`
178. Verifikasi kolom `Old Value`: perubahan tampil di preview tabel popup (kolom `Old Value` ter-pin)
179. Klik `[Save]`
180. Scroll tabel Changelog secara horizontal
181. Verifikasi kolom `Old Value`: tersimpan setelah Save (kolom `Old Value` membeku saat scroll horizontal)
182. Muat ulang halaman (F5)
183. Klik icon Changelog di Table Tools
184. Scroll tabel Changelog secara horizontal
185. Verifikasi kolom `Old Value`: bertahan setelah F5 (kolom `Old Value` tetap membeku saat scroll horizontal)
186. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Old Value`, lalu klik icon pin pada `New Value`
187. Verifikasi kolom `New Value`: perubahan tampil di preview tabel popup (kolom `New Value` ter-pin)
188. Klik `[Save]`
189. Scroll tabel Changelog secara horizontal
190. Verifikasi kolom `New Value`: tersimpan setelah Save (kolom `New Value` membeku saat scroll horizontal)
191. Muat ulang halaman (F5)
192. Klik icon Changelog di Table Tools
193. Scroll tabel Changelog secara horizontal
194. Verifikasi kolom `New Value`: bertahan setelah F5 (kolom `New Value` tetap membeku saat scroll horizontal)
195. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `New Value`, lalu klik icon pin pada `Modified By`
196. Verifikasi kolom `Modified By`: perubahan tampil di preview tabel popup (kolom `Modified By` ter-pin)
197. Klik `[Save]`
198. Scroll tabel Changelog secara horizontal
199. Verifikasi kolom `Modified By`: tersimpan setelah Save (kolom `Modified By` membeku saat scroll horizontal)
200. Muat ulang halaman (F5)
201. Klik icon Changelog di Table Tools
202. Scroll tabel Changelog secara horizontal
203. Verifikasi kolom `Modified By`: bertahan setelah F5 (kolom `Modified By` tetap membeku saat scroll horizontal)
204. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Modified By`, lalu klik `[Save]`
### TC-GS-USER-499: Setup Column Reset to Default
205. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Modified By`, seret `Field` ke posisi pertama, lalu klik `[Save]`
206. Klik header Column Visibility (⋯), lalu klik `Setup Column...`
207. Klik `[Reset to Default]`
208. Klik `[Save]`
209. Verifikasi susunan kolom kembali default: tujuh kolom tampil dengan urutan `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, `Modified By`
210. Muat ulang halaman (F5)
211. Klik icon Changelog di Table Tools
212. Verifikasi susunan kolom default bertahan setelah F5 (tujuh kolom tampil dengan urutan `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, `Modified By`)
213. Pulihkan lebar viewport ke ukuran semula

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-USER-494, 495, 501, 502, 500, 496, 497, 498, 499. Alasan: dua TC screening (494, 495) di awal; TC yang dibatalkan tanpa menyimpan (501, 502, 500) sebelum TC yang menyimpan konfigurasi (496, 497, 498); TC-GS-USER-499 (reset) di akhir karena mengembalikan konfigurasi yang diubah TC sebelumnya (bagian 3 konvensi). Modal Changelog dibuka di langkah 1 dan dibuka kembali setelah tiap muat ulang halaman.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah menutup popup (`[✕]`) sesudah screening dan TC yang dibatalkan; langkah 139 (reset ke default sebelum TC-GS-USER-498, sehingga urutan hasil seret TC-GS-USER-497 tidak terbawa) dan langkah sesudahnya (memperkecil viewport agar scroll horizontal teramati); `Klik icon Changelog` sesudah tiap F5 (muat ulang menutup modal); langkah terakhir pada blok TC-GS-USER-496 (centang kembali `Modified By`) dan TC-GS-USER-498 (unpin `Modified By`); langkah 213 (memulihkan viewport). Pada TC-GS-USER-496 dan 498, centang kembali atau unpin kolom sebelumnya dilakukan pada langkah pertama popup kolom berikutnya.
- Anchor positif (bagian 8b butir 2): pada TC-GS-USER-496, `Verifikasi kolom lain tampil di tabel setelah F5` mendahului tiap `Verifikasi` absence kolom yang di-hide sesudah F5 (langkah 39, 47, 55, 63, 71, 79, 87), sehingga kolom yang hilang tidak lolos karena tabel gagal dimuat.
- Langkah membuka popup (klik header Column Visibility lalu `Setup Column...`) digabung dalam langkah aksi pertama di popup tersebut, karena `[Save]` menutup popup dan tabel diamati sesudahnya.
- Tafsiran TC-GS-USER-496: langkah "uncheck lalu check, Save, refresh F5" dibaca sebagai hilangkan centang, `[Save]`, F5, lalu centang kembali (pada popup berikutnya); tiap klausa Expected (preview, tersimpan setelah Save, bertahan setelah F5) mendapat `Verifikasi`.
- Pembagian TC Setup Column: Setup Column tabel User List ada di spec 075. Setup Column Modal Changelog Role ada di spec 088 dan Tab Changelog Detail ada di spec 094.
- Spec melewati sekitar 35 langkah (213 langkah) karena TC-GS-USER-496, 497, dan 498 masing-masing menguji tujuh kolom dengan tiga `Verifikasi` per kolom (S-01); semua blok satu layar (Setup Column Modal Changelog User), satu akun aktor, dan satu dataset seed, serta tiap kolom berdiri sendiri karena perubahan dibuang (TC-GS-USER-500 sampai 502), diakumulasi tanpa saling bergantung (TC-GS-USER-497), atau dikembalikan di kolom berikutnya (TC-GS-USER-496 dan 498).
- Temuan untuk QA: (1) TC-GS-USER-494 Expected b menyebut kolom Curated unchecked & enabled; tabel Modal Changelog User tidak punya kolom Curated (PRD user.md §4.1.8), sehingga bagian itu tidak diasersi. (2) TC-GS-USER-495 menyebut "deskripsi panduan" tanpa teksnya; spec memakai teks deskripsi dari prd-conventions §9.3. (3) TC-GS-USER-497 langkah kolom `Date` menyeret `Date` ke posisi pertama padahal `Date` sudah di posisi pertama pada konfigurasi default; Expected tidak membedakannya dari kolom lain. (4) TC-GS-USER-498 tidak menyebut lebar viewport atau cara membuat tabel overflow agar scroll horizontal teramati. (5) TC-GS-USER-500 tidak menyebut konfigurasi yang diubah; spec menghilangkan centang `Field`. (6) TC-GS-USER-502 tidak menyebut tiga kolom yang di-pin; spec memakai `Date`, `Action`, dan `User Name`, dengan kolom keempat `Field`. (7) TC-GS-USER-499 tidak menyebut perubahan yang dilakukan sebelum reset; spec menghilangkan centang `Modified By` dan menyeret `Field` ke posisi pertama. (8) TC-GS-USER-501 tidak menyebut kolom yang tersisa; spec menyisakan `Modified By`.

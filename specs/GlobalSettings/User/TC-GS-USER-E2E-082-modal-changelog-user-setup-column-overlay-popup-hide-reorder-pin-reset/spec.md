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
- State global yang diubah: konfigurasi kolom Modal Changelog User (visibilitas, urutan, pin) dan lebar viewport. Spec memulihkannya di langkah 132 sampai 206 dan di hook `after`.

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
9. Verifikasi Header: deskripsi panduan tampil
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
39. Verifikasi kolom `Date`: bertahan setelah F5 (kolom `Date` tetap tidak tampil)
40. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Date`, lalu hilangkan centang `Action`
41. Verifikasi kolom `Action`: perubahan tampil di preview tabel popup (kolom `Action` tidak tampil)
42. Klik `[Save]`
43. Verifikasi kolom `Action`: tersimpan setelah Save (kolom `Action` tidak tampil di tabel)
44. Muat ulang halaman (F5)
45. Klik icon Changelog di Table Tools
46. Verifikasi kolom `Action`: bertahan setelah F5 (kolom `Action` tetap tidak tampil)
47. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Action`, lalu hilangkan centang `User Name`
48. Verifikasi kolom `User Name`: perubahan tampil di preview tabel popup (kolom `User Name` tidak tampil)
49. Klik `[Save]`
50. Verifikasi kolom `User Name`: tersimpan setelah Save (kolom `User Name` tidak tampil di tabel)
51. Muat ulang halaman (F5)
52. Klik icon Changelog di Table Tools
53. Verifikasi kolom `User Name`: bertahan setelah F5 (kolom `User Name` tetap tidak tampil)
54. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `User Name`, lalu hilangkan centang `Field`
55. Verifikasi kolom `Field`: perubahan tampil di preview tabel popup (kolom `Field` tidak tampil)
56. Klik `[Save]`
57. Verifikasi kolom `Field`: tersimpan setelah Save (kolom `Field` tidak tampil di tabel)
58. Muat ulang halaman (F5)
59. Klik icon Changelog di Table Tools
60. Verifikasi kolom `Field`: bertahan setelah F5 (kolom `Field` tetap tidak tampil)
61. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Field`, lalu hilangkan centang `Old Value`
62. Verifikasi kolom `Old Value`: perubahan tampil di preview tabel popup (kolom `Old Value` tidak tampil)
63. Klik `[Save]`
64. Verifikasi kolom `Old Value`: tersimpan setelah Save (kolom `Old Value` tidak tampil di tabel)
65. Muat ulang halaman (F5)
66. Klik icon Changelog di Table Tools
67. Verifikasi kolom `Old Value`: bertahan setelah F5 (kolom `Old Value` tetap tidak tampil)
68. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Old Value`, lalu hilangkan centang `New Value`
69. Verifikasi kolom `New Value`: perubahan tampil di preview tabel popup (kolom `New Value` tidak tampil)
70. Klik `[Save]`
71. Verifikasi kolom `New Value`: tersimpan setelah Save (kolom `New Value` tidak tampil di tabel)
72. Muat ulang halaman (F5)
73. Klik icon Changelog di Table Tools
74. Verifikasi kolom `New Value`: bertahan setelah F5 (kolom `New Value` tetap tidak tampil)
75. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `New Value`, lalu hilangkan centang `Modified By`
76. Verifikasi kolom `Modified By`: perubahan tampil di preview tabel popup (kolom `Modified By` tidak tampil)
77. Klik `[Save]`
78. Verifikasi kolom `Modified By`: tersimpan setelah Save (kolom `Modified By` tidak tampil di tabel)
79. Muat ulang halaman (F5)
80. Klik icon Changelog di Table Tools
81. Verifikasi kolom `Modified By`: bertahan setelah F5 (kolom `Modified By` tetap tidak tampil)
82. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Modified By`, lalu klik `[Save]`
### TC-GS-USER-497: Drag reorder kolom kelas Hideable
83. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Date` ke posisi pertama
84. Verifikasi kolom `Date`: perubahan tampil di preview tabel popup (kolom `Date` di posisi pertama)
85. Klik `[Save]`
86. Verifikasi kolom `Date`: tersimpan setelah Save (kolom `Date` berada di posisi pertama tabel)
87. Muat ulang halaman (F5)
88. Klik icon Changelog di Table Tools
89. Verifikasi kolom `Date`: bertahan setelah F5 (kolom `Date` tetap di posisi pertama)
90. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Action` ke posisi pertama
91. Verifikasi kolom `Action`: perubahan tampil di preview tabel popup (kolom `Action` di posisi pertama)
92. Klik `[Save]`
93. Verifikasi kolom `Action`: tersimpan setelah Save (kolom `Action` berada di posisi pertama tabel)
94. Muat ulang halaman (F5)
95. Klik icon Changelog di Table Tools
96. Verifikasi kolom `Action`: bertahan setelah F5 (kolom `Action` tetap di posisi pertama)
97. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `User Name` ke posisi pertama
98. Verifikasi kolom `User Name`: perubahan tampil di preview tabel popup (kolom `User Name` di posisi pertama)
99. Klik `[Save]`
100. Verifikasi kolom `User Name`: tersimpan setelah Save (kolom `User Name` berada di posisi pertama tabel)
101. Muat ulang halaman (F5)
102. Klik icon Changelog di Table Tools
103. Verifikasi kolom `User Name`: bertahan setelah F5 (kolom `User Name` tetap di posisi pertama)
104. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Field` ke posisi pertama
105. Verifikasi kolom `Field`: perubahan tampil di preview tabel popup (kolom `Field` di posisi pertama)
106. Klik `[Save]`
107. Verifikasi kolom `Field`: tersimpan setelah Save (kolom `Field` berada di posisi pertama tabel)
108. Muat ulang halaman (F5)
109. Klik icon Changelog di Table Tools
110. Verifikasi kolom `Field`: bertahan setelah F5 (kolom `Field` tetap di posisi pertama)
111. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Old Value` ke posisi pertama
112. Verifikasi kolom `Old Value`: perubahan tampil di preview tabel popup (kolom `Old Value` di posisi pertama)
113. Klik `[Save]`
114. Verifikasi kolom `Old Value`: tersimpan setelah Save (kolom `Old Value` berada di posisi pertama tabel)
115. Muat ulang halaman (F5)
116. Klik icon Changelog di Table Tools
117. Verifikasi kolom `Old Value`: bertahan setelah F5 (kolom `Old Value` tetap di posisi pertama)
118. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `New Value` ke posisi pertama
119. Verifikasi kolom `New Value`: perubahan tampil di preview tabel popup (kolom `New Value` di posisi pertama)
120. Klik `[Save]`
121. Verifikasi kolom `New Value`: tersimpan setelah Save (kolom `New Value` berada di posisi pertama tabel)
122. Muat ulang halaman (F5)
123. Klik icon Changelog di Table Tools
124. Verifikasi kolom `New Value`: bertahan setelah F5 (kolom `New Value` tetap di posisi pertama)
125. Klik header Column Visibility (⋯), klik `Setup Column...`, seret `Modified By` ke posisi pertama
126. Verifikasi kolom `Modified By`: perubahan tampil di preview tabel popup (kolom `Modified By` di posisi pertama)
127. Klik `[Save]`
128. Verifikasi kolom `Modified By`: tersimpan setelah Save (kolom `Modified By` berada di posisi pertama tabel)
129. Muat ulang halaman (F5)
130. Klik icon Changelog di Table Tools
131. Verifikasi kolom `Modified By`: bertahan setelah F5 (kolom `Modified By` tetap di posisi pertama)
### TC-GS-USER-498: Pin dan unpin kolom kelas Hideable
132. Klik header Column Visibility (⋯), klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`
133. Perkecil lebar viewport hingga tabel Changelog dapat di-scroll horizontal
134. Klik header Column Visibility (⋯), klik `Setup Column...`, klik icon pin pada `Date`
135. Verifikasi kolom `Date`: perubahan tampil di preview tabel popup (kolom `Date` ter-pin)
136. Klik `[Save]`
137. Scroll tabel Changelog secara horizontal
138. Verifikasi kolom `Date`: tersimpan setelah Save (kolom `Date` membeku saat scroll horizontal)
139. Muat ulang halaman (F5)
140. Klik icon Changelog di Table Tools
141. Scroll tabel Changelog secara horizontal
142. Verifikasi kolom `Date`: bertahan setelah F5 (kolom `Date` tetap membeku saat scroll horizontal)
143. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Date`, lalu klik icon pin pada `Action`
144. Verifikasi kolom `Action`: perubahan tampil di preview tabel popup (kolom `Action` ter-pin)
145. Klik `[Save]`
146. Scroll tabel Changelog secara horizontal
147. Verifikasi kolom `Action`: tersimpan setelah Save (kolom `Action` membeku saat scroll horizontal)
148. Muat ulang halaman (F5)
149. Klik icon Changelog di Table Tools
150. Scroll tabel Changelog secara horizontal
151. Verifikasi kolom `Action`: bertahan setelah F5 (kolom `Action` tetap membeku saat scroll horizontal)
152. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Action`, lalu klik icon pin pada `User Name`
153. Verifikasi kolom `User Name`: perubahan tampil di preview tabel popup (kolom `User Name` ter-pin)
154. Klik `[Save]`
155. Scroll tabel Changelog secara horizontal
156. Verifikasi kolom `User Name`: tersimpan setelah Save (kolom `User Name` membeku saat scroll horizontal)
157. Muat ulang halaman (F5)
158. Klik icon Changelog di Table Tools
159. Scroll tabel Changelog secara horizontal
160. Verifikasi kolom `User Name`: bertahan setelah F5 (kolom `User Name` tetap membeku saat scroll horizontal)
161. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `User Name`, lalu klik icon pin pada `Field`
162. Verifikasi kolom `Field`: perubahan tampil di preview tabel popup (kolom `Field` ter-pin)
163. Klik `[Save]`
164. Scroll tabel Changelog secara horizontal
165. Verifikasi kolom `Field`: tersimpan setelah Save (kolom `Field` membeku saat scroll horizontal)
166. Muat ulang halaman (F5)
167. Klik icon Changelog di Table Tools
168. Scroll tabel Changelog secara horizontal
169. Verifikasi kolom `Field`: bertahan setelah F5 (kolom `Field` tetap membeku saat scroll horizontal)
170. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Field`, lalu klik icon pin pada `Old Value`
171. Verifikasi kolom `Old Value`: perubahan tampil di preview tabel popup (kolom `Old Value` ter-pin)
172. Klik `[Save]`
173. Scroll tabel Changelog secara horizontal
174. Verifikasi kolom `Old Value`: tersimpan setelah Save (kolom `Old Value` membeku saat scroll horizontal)
175. Muat ulang halaman (F5)
176. Klik icon Changelog di Table Tools
177. Scroll tabel Changelog secara horizontal
178. Verifikasi kolom `Old Value`: bertahan setelah F5 (kolom `Old Value` tetap membeku saat scroll horizontal)
179. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Old Value`, lalu klik icon pin pada `New Value`
180. Verifikasi kolom `New Value`: perubahan tampil di preview tabel popup (kolom `New Value` ter-pin)
181. Klik `[Save]`
182. Scroll tabel Changelog secara horizontal
183. Verifikasi kolom `New Value`: tersimpan setelah Save (kolom `New Value` membeku saat scroll horizontal)
184. Muat ulang halaman (F5)
185. Klik icon Changelog di Table Tools
186. Scroll tabel Changelog secara horizontal
187. Verifikasi kolom `New Value`: bertahan setelah F5 (kolom `New Value` tetap membeku saat scroll horizontal)
188. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `New Value`, lalu klik icon pin pada `Modified By`
189. Verifikasi kolom `Modified By`: perubahan tampil di preview tabel popup (kolom `Modified By` ter-pin)
190. Klik `[Save]`
191. Scroll tabel Changelog secara horizontal
192. Verifikasi kolom `Modified By`: tersimpan setelah Save (kolom `Modified By` membeku saat scroll horizontal)
193. Muat ulang halaman (F5)
194. Klik icon Changelog di Table Tools
195. Scroll tabel Changelog secara horizontal
196. Verifikasi kolom `Modified By`: bertahan setelah F5 (kolom `Modified By` tetap membeku saat scroll horizontal)
197. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Modified By`, lalu klik `[Save]`
### TC-GS-USER-499: Setup Column Reset to Default
198. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Modified By`, seret `Field` ke posisi pertama, lalu klik `[Save]`
199. Klik header Column Visibility (⋯), lalu klik `Setup Column...`
200. Klik `[Reset to Default]`
201. Klik `[Save]`
202. Verifikasi susunan kolom kembali default: tujuh kolom tampil dengan urutan `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, `Modified By`
203. Muat ulang halaman (F5)
204. Klik icon Changelog di Table Tools
205. Verifikasi susunan kolom default bertahan setelah F5 (tujuh kolom tampil dengan urutan `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, `Modified By`)
206. Pulihkan lebar viewport ke ukuran semula

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-USER-494, 495, 501, 502, 500, 496, 497, 498, 499. Alasan: dua TC screening (494, 495) di awal; TC yang dibatalkan tanpa menyimpan (501, 502, 500) sebelum TC yang menyimpan konfigurasi (496, 497, 498); TC-GS-USER-499 (reset) di akhir karena mengembalikan konfigurasi yang diubah TC sebelumnya (bagian 3 konvensi). Modal Changelog dibuka di langkah 1 dan dibuka kembali setelah tiap muat ulang halaman.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah menutup popup (`[✕]`) sesudah screening dan TC yang dibatalkan; langkah 132 (reset ke default sebelum TC-GS-USER-498, sehingga urutan hasil seret TC-GS-USER-497 tidak terbawa) dan langkah sesudahnya (memperkecil viewport agar scroll horizontal teramati); `Klik icon Changelog` sesudah tiap F5 (muat ulang menutup modal); langkah terakhir pada blok TC-GS-USER-496 (centang kembali `Modified By`) dan TC-GS-USER-498 (unpin `Modified By`); langkah 206 (memulihkan viewport). Pada TC-GS-USER-496 dan 498, centang kembali atau unpin kolom sebelumnya dilakukan pada langkah pertama popup kolom berikutnya.
- Langkah membuka popup (klik header Column Visibility lalu `Setup Column...`) digabung dalam langkah aksi pertama di popup tersebut, karena `[Save]` menutup popup dan tabel diamati sesudahnya.
- Tafsiran TC-GS-USER-496: langkah "uncheck lalu check, Save, refresh F5" dibaca sebagai hilangkan centang, `[Save]`, F5, lalu centang kembali (pada popup berikutnya); tiap klausa Expected (preview, tersimpan setelah Save, bertahan setelah F5) mendapat `Verifikasi`.
- Pembagian TC Setup Column: Setup Column tabel User List ada di spec 075. Setup Column Modal Changelog Role ada di spec 088 dan Tab Changelog Detail ada di spec 094.
- Spec melewati sekitar 35 langkah (206 langkah) karena TC-GS-USER-496, 497, dan 498 masing-masing menguji tujuh kolom dengan tiga `Verifikasi` per kolom (S-01); semua blok satu layar (Setup Column Modal Changelog User), satu akun aktor, dan satu dataset seed, serta tiap kolom berdiri sendiri karena perubahan dibuang (TC-GS-USER-500 sampai 502), diakumulasi tanpa saling bergantung (TC-GS-USER-497), atau dikembalikan di kolom berikutnya (TC-GS-USER-496 dan 498).
- Temuan untuk QA: (1) TC-GS-USER-494 Expected b menyebut kolom Curated unchecked & enabled; tabel Modal Changelog User tidak punya kolom Curated (PRD user.md §4.1.8), sehingga bagian itu tidak diasersi. (2) TC-GS-USER-495 menyebut "deskripsi panduan" tanpa teksnya; spec hanya mengasersi deskripsi tampil. (3) TC-GS-USER-497 langkah kolom `Date` menyeret `Date` ke posisi pertama padahal `Date` sudah di posisi pertama pada konfigurasi default; Expected tidak membedakannya dari kolom lain. (4) TC-GS-USER-498 tidak menyebut lebar viewport atau cara membuat tabel overflow agar scroll horizontal teramati. (5) TC-GS-USER-500 tidak menyebut konfigurasi yang diubah; spec menghilangkan centang `Field`. (6) TC-GS-USER-502 tidak menyebut tiga kolom yang di-pin; spec memakai `Date`, `Action`, dan `User Name`, dengan kolom keempat `Field`. (7) TC-GS-USER-499 tidak menyebut perubahan yang dilakukan sebelum reset; spec menghilangkan centang `Modified By` dan menyeret `Field` ke posisi pertama. (8) TC-GS-USER-501 tidak menyebut kolom yang tersisa; spec menyisakan `Modified By`.

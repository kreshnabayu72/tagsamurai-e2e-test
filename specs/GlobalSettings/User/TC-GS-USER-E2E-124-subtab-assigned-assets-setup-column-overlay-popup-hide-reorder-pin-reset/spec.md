---
id: TC-GS-USER-E2E-124-subtab-assigned-assets-setup-column-overlay-popup-hide-reorder-pin-reset
title: "Sub-tab Assigned Assets: Setup Column (Overlay, Popup, Hide/Unhide, Reorder, Pin, Reset to Default, dan Guard)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-776
  - TC-GS-USER-777
  - TC-GS-USER-778
  - TC-GS-USER-779
  - TC-GS-USER-780
  - TC-GS-USER-781
  - TC-GS-USER-782
  - TC-GS-USER-783
  - TC-GS-USER-784
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Setup Column (Overlay, Popup, Hide/Unhide, Reorder, Pin, Reset to Default, dan Guard)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup user; hanya dataset Assigned Assets milik spec yang ditambahkan lalu dibersihkan.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22, hanya dibaca): Ahmad Fauzi (No. 13; Assigned Assets berisi K1).
- Data Dinamis, dataset Assigned Assets milik Ahmad Fauzi (27 baris; dengan page size 10 menjadi tiga halaman: 10, 10, 7 baris). K1 adalah data Pre-setup (hanya dibaca, tidak dihapus); K2 sampai K27 di-seed milik spec lewat kemampuan seeding data Responsibilities/FAMS (HK8) di hook `before` (disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Saat spec mulai, Assigned Assets Ahmad Fauzi hanya berisi K1 sampai K27. Transaction ID `ASG-{runId}-124-kk` dan Asset ID `AST-{runId}-124-kk` dengan kk = nomor K dua digit:
  - K1 (Pre-setup, literal dari TC-GS-USER-390): Transaction ID `ASG-20260505-0001`, Name `Company Vehicle B1234XY`, Asset ID `AST-0001`, Brand `Toyota`, Model / Type `Hilux`, PIC `Citra Wulandari`.
  - K2 sampai K4: Name `Company Vehicle V1 {runId}-124` sampai `Company Vehicle V3 {runId}-124`, Brand `Toyota`, Model / Type `Hilux`, PIC `Rudi Hartanto {runId}-124`.
  - K5 sampai K7: Name `Company Vehicle V4 {runId}-124` sampai `Company Vehicle V6 {runId}-124`, Brand `Honda`, Model / Type `Civic`, PIC `Sinta Dewi {runId}-124`.
  - K8 sampai K12: Name `Laptop L1 {runId}-124` sampai `Laptop L5 {runId}-124`, Brand `Dell`, Model / Type `Latitude 5440`, PIC `Bambang Susanto {runId}-124`.
  - K13 sampai K17: Name `Laptop L6 {runId}-124` sampai `Laptop L10 {runId}-124`, Brand `Lenovo`, Model / Type `ThinkPad T14`, PIC `Rudi Hartanto {runId}-124`.
  - K18 sampai K22: Name `Printer P1 {runId}-124` sampai `Printer P5 {runId}-124`, Brand `Canon`, Model / Type `PIXMA G3010`, PIC `Sinta Dewi {runId}-124`.
  - K23 sampai K27: Name `Printer P6 {runId}-124` sampai `Printer P10 {runId}-124`, Brand `Epson`, Model / Type `EcoTank L3250`, PIC `Bambang Susanto {runId}-124`.
  - Ringkasan: Name 27 nilai distinct; Brand 6 nilai (Toyota 4 baris, Honda 3, Dell 5, Lenovo 5, Canon 5, Epson 5); PIC 4 nilai (Citra Wulandari 1 baris, Rudi Hartanto 8, Sinta Dewi 8, Bambang Susanto 10); baris ber-Name memuat `Vehicle`: 7 (K1 sampai K7). Nilai distinct pada kolom yang di-sort, di-search, dan di-filter dipenuhi (S-11).
  - Nama literal tanpa suffix hanya K1 (Pre-setup); seluruh nilai Name, Transaction ID, Asset ID, dan PIC milik spec bersuffix `{runId}-124`. Nama Brand dan Model / Type adalah nilai master tanpa suffix.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus aset seed K2 sampai K27 lewat kemampuan seeding yang sama; data Pre-setup (K1 dan record user) tidak diubah. Seeding aset tidak mengubah record user Ahmad Fauzi.
- Data uji: tujuh kolom `Photo`, `Transaction ID`, `Name`, `Asset ID`, `Brand`, `Model / Type`, `PIC` (semua Hideable, default tampil); TC-GS-USER-778 dan 779 dijalankan per kolom (satu `[Save]` dan satu F5 per kolom); TC-GS-USER-780 dikelompokkan menjadi tiga siklus pin (`Photo`, `Transaction ID`, `Name`; `Asset ID`, `Brand`, `Model / Type`; `PIC`) karena maksimal 3 kolom ter-pin sekaligus.
- Preferensi kolom (visibilitas, urutan, pin) sub-tab Assigned Assets tersimpan per user dan menjadi permanen setelah `[Save]` (prd-conventions.md §9.3); "muat ulang halaman" dilakukan pada konteks browser yang sama supaya penyimpanan tetap ada. Overlay Column Visibility langsung berlaku.
- Lebar konten tabel harus melebihi lebar viewport (overflow horizontal) supaya scroll horizontal pada TC-GS-USER-780 teramati. Viewport disempitkan pada langkah 178 dan dikembalikan pada langkah 223; ukuran viewport dipilih tim FE karena TC tidak menyebutnya.
- Kemampuan teknis: seeding Assigned Assets (HK8) (disediakan tim FE/BE); drag and drop item kolom pada Popup Setup Column; mengatur viewport; scroll horizontal tabel; mengarahkan kursor ke checkbox dan icon Pin disabled untuk membaca tooltip; membaca dan menghapus preferensi kolom di penyimpanan browser; setelah F5 sub-tab Assigned Assets user yang sama tetap terbuka.
- State yang diubah dan dipulihkan: preferensi Setup Column sub-tab Assigned Assets dikembalikan ke default (susunan `Photo | Transaction ID | Name | Asset ID | Brand | Model / Type | PIC`, semua tampil, tanpa pin) oleh blok TC-GS-USER-781 di akhir spec (langkah 224 sampai 233); hook `after` (tetap jalan walau spec gagal di tengah) mengembalikannya lewat `[Reset to Default]` atau penghapusan preferensi kolom sub-tab Assigned Assets di browser, serta mengembalikan viewport ke ukuran awal. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik icon Search, ketik `Ahmad Fauzi`, tekan Enter
2. Klik Name `Ahmad Fauzi` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Assigned Assets`

### TC-GS-USER-776: Screening Overlay Column Visibility

5. Klik header kolom Actions (⋯)
6. Verifikasi Overlay daftar kolom: `Photo` | `Name` | `Asset ID` | `Transaction ID` | `Brand` | `Model / Type` | `PIC`
7. Verifikasi ketujuh kolom (Hideable) tercentang dan enabled
8. Verifikasi drag handle tersedia pada tiap kolom
9. Verifikasi item `Setup Column...` tersedia di overlay

### TC-GS-USER-777: Screening Popup Setup Column

10. Klik `Setup Column...`
11. Verifikasi Header: Title `Setup Column`
12. Verifikasi Header: deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
13. Verifikasi Header: icon `[✕]` tampil
14. Verifikasi Body: daftar kolom dengan checkbox
15. Verifikasi Body: drag handle pada tiap kolom
16. Verifikasi Body: icon Pin pada tiap kolom
17. Verifikasi Body: preview tabel tampil
18. Verifikasi Footer: tombol `[Reset to Default]` dan `[Save]`
19. Verifikasi Footer: tidak ada tombol `[Cancel]`

### TC-GS-USER-782: Tutup Setup Column via [✕] membuang perubahan

20. Hilangkan centang `Brand`
21. Verifikasi preview tidak memuat kolom `Brand`
22. Klik `[✕]`
23. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir: kolom `Brand` tampil

### TC-GS-USER-783: Guard satu kolom tersisa tidak bisa di-uncheck

24. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
25. Hilangkan centang `Photo`
26. Hilangkan centang `Transaction ID`
27. Hilangkan centang `Name`
28. Hilangkan centang `Asset ID`
29. Hilangkan centang `Brand`
30. Hilangkan centang `Model / Type`
31. Arahkan kursor ke checkbox kolom terakhir `PIC`
32. Verifikasi checkbox `PIC` tetap tampil namun disabled
33. Verifikasi tooltip `At least one column must remain visible.`
34. Klik `[✕]`

### TC-GS-USER-784: Maksimal 3 kolom di-pin

35. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
36. Klik icon Pin pada `Photo`
37. Klik icon Pin pada `Transaction ID`
38. Klik icon Pin pada `Name`
39. Verifikasi preview menampilkan kolom `Photo`, `Transaction ID`, dan `Name` ter-pin
40. Arahkan kursor ke icon Pin kolom keempat `Brand`
41. Verifikasi icon Pin `Brand` disabled
42. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
43. Klik `[✕]`

### TC-GS-USER-778: Setup Column hide/unhide kelas Hideable

44. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
45. Hilangkan centang `Photo`
46. Verifikasi preview tidak memuat kolom `Photo`
47. Klik `[Save]`
48. Verifikasi tabel tidak memuat kolom `Photo` setelah Save
49. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
50. Verifikasi kolom `Transaction ID` tampil di tabel setelah F5
51. Verifikasi kolom `Photo` tetap tidak tampil setelah F5
52. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
53. Centang kembali `Photo`
54. Klik `[Save]`
55. Verifikasi tabel memuat kembali kolom `Photo`
56. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
57. Hilangkan centang `Transaction ID`
58. Verifikasi preview tidak memuat kolom `Transaction ID`
59. Klik `[Save]`
60. Verifikasi tabel tidak memuat kolom `Transaction ID` setelah Save
61. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
62. Verifikasi kolom `Name` tampil di tabel setelah F5
63. Verifikasi kolom `Transaction ID` tetap tidak tampil setelah F5
64. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
65. Centang kembali `Transaction ID`
66. Klik `[Save]`
67. Verifikasi tabel memuat kembali kolom `Transaction ID`
68. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
69. Hilangkan centang `Name`
70. Verifikasi preview tidak memuat kolom `Name`
71. Klik `[Save]`
72. Verifikasi tabel tidak memuat kolom `Name` setelah Save
73. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
74. Verifikasi kolom `Transaction ID` tampil di tabel setelah F5
75. Verifikasi kolom `Name` tetap tidak tampil setelah F5
76. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
77. Centang kembali `Name`
78. Klik `[Save]`
79. Verifikasi tabel memuat kembali kolom `Name`
80. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
81. Hilangkan centang `Asset ID`
82. Verifikasi preview tidak memuat kolom `Asset ID`
83. Klik `[Save]`
84. Verifikasi tabel tidak memuat kolom `Asset ID` setelah Save
85. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
86. Verifikasi kolom `Transaction ID` tampil di tabel setelah F5
87. Verifikasi kolom `Asset ID` tetap tidak tampil setelah F5
88. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
89. Centang kembali `Asset ID`
90. Klik `[Save]`
91. Verifikasi tabel memuat kembali kolom `Asset ID`
92. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
93. Hilangkan centang `Brand`
94. Verifikasi preview tidak memuat kolom `Brand`
95. Klik `[Save]`
96. Verifikasi tabel tidak memuat kolom `Brand` setelah Save
97. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
98. Verifikasi kolom `Transaction ID` tampil di tabel setelah F5
99. Verifikasi kolom `Brand` tetap tidak tampil setelah F5
100. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
101. Centang kembali `Brand`
102. Klik `[Save]`
103. Verifikasi tabel memuat kembali kolom `Brand`
104. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
105. Hilangkan centang `Model / Type`
106. Verifikasi preview tidak memuat kolom `Model / Type`
107. Klik `[Save]`
108. Verifikasi tabel tidak memuat kolom `Model / Type` setelah Save
109. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
110. Verifikasi kolom `Transaction ID` tampil di tabel setelah F5
111. Verifikasi kolom `Model / Type` tetap tidak tampil setelah F5
112. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
113. Centang kembali `Model / Type`
114. Klik `[Save]`
115. Verifikasi tabel memuat kembali kolom `Model / Type`
116. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
117. Hilangkan centang `PIC`
118. Verifikasi preview tidak memuat kolom `PIC`
119. Klik `[Save]`
120. Verifikasi tabel tidak memuat kolom `PIC` setelah Save
121. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
122. Verifikasi kolom `Transaction ID` tampil di tabel setelah F5
123. Verifikasi kolom `PIC` tetap tidak tampil setelah F5
124. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
125. Centang kembali `PIC`
126. Klik `[Save]`
127. Verifikasi tabel memuat kembali kolom `PIC`

### TC-GS-USER-779: Setup Column drag reorder kelas Hideable

128. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
129. Seret `Photo` ke posisi terakhir
130. Verifikasi preview menempatkan `Photo` di posisi terakhir
131. Klik `[Save]`
132. Verifikasi kolom `Photo` berada di posisi terakhir tabel setelah Save
133. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
134. Verifikasi kolom `Photo` tetap di posisi terakhir tabel setelah F5
135. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
136. Seret `Transaction ID` ke posisi pertama
137. Verifikasi preview menempatkan `Transaction ID` di posisi pertama
138. Klik `[Save]`
139. Verifikasi kolom `Transaction ID` berada di posisi pertama tabel setelah Save
140. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
141. Verifikasi kolom `Transaction ID` tetap di posisi pertama tabel setelah F5
142. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
143. Seret `Name` ke posisi pertama
144. Verifikasi preview menempatkan `Name` di posisi pertama
145. Klik `[Save]`
146. Verifikasi kolom `Name` berada di posisi pertama tabel setelah Save
147. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
148. Verifikasi kolom `Name` tetap di posisi pertama tabel setelah F5
149. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
150. Seret `Asset ID` ke posisi pertama
151. Verifikasi preview menempatkan `Asset ID` di posisi pertama
152. Klik `[Save]`
153. Verifikasi kolom `Asset ID` berada di posisi pertama tabel setelah Save
154. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
155. Verifikasi kolom `Asset ID` tetap di posisi pertama tabel setelah F5
156. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
157. Seret `Brand` ke posisi pertama
158. Verifikasi preview menempatkan `Brand` di posisi pertama
159. Klik `[Save]`
160. Verifikasi kolom `Brand` berada di posisi pertama tabel setelah Save
161. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
162. Verifikasi kolom `Brand` tetap di posisi pertama tabel setelah F5
163. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
164. Seret `Model / Type` ke posisi pertama
165. Verifikasi preview menempatkan `Model / Type` di posisi pertama
166. Klik `[Save]`
167. Verifikasi kolom `Model / Type` berada di posisi pertama tabel setelah Save
168. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
169. Verifikasi kolom `Model / Type` tetap di posisi pertama tabel setelah F5
170. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
171. Seret `PIC` ke posisi pertama
172. Verifikasi preview menempatkan `PIC` di posisi pertama
173. Klik `[Save]`
174. Verifikasi kolom `PIC` berada di posisi pertama tabel setelah Save
175. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
176. Verifikasi kolom `PIC` tetap di posisi pertama tabel setelah F5
177. Verifikasi urutan tabel tetap `PIC | Model / Type | Brand | Asset ID | Name | Transaction ID | Photo` setelah F5

### TC-GS-USER-780: Setup Column pin/unpin kelas Hideable

178. Sempitkan viewport sehingga tabel dapat di-scroll horizontal
179. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
180. Klik icon Pin pada `Photo`
181. Klik icon Pin pada `Transaction ID`
182. Klik icon Pin pada `Name`
183. Verifikasi preview menampilkan kolom `Photo`, `Transaction ID`, `Name` ter-pin
184. Klik `[Save]`
185. Scroll tabel secara horizontal
186. Verifikasi kolom `Photo`, `Transaction ID`, `Name` membeku (sticky) saat scroll horizontal setelah Save
187. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
188. Scroll tabel secara horizontal
189. Verifikasi kolom `Photo`, `Transaction ID`, `Name` tetap membeku setelah F5
190. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
191. Klik icon Pin pada `Photo` untuk unpin
192. Klik icon Pin pada `Transaction ID` untuk unpin
193. Klik icon Pin pada `Name` untuk unpin
194. Klik `[Save]`
195. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
196. Klik icon Pin pada `Asset ID`
197. Klik icon Pin pada `Brand`
198. Klik icon Pin pada `Model / Type`
199. Verifikasi preview menampilkan kolom `Asset ID`, `Brand`, `Model / Type` ter-pin
200. Klik `[Save]`
201. Scroll tabel secara horizontal
202. Verifikasi kolom `Asset ID`, `Brand`, `Model / Type` membeku (sticky) saat scroll horizontal setelah Save
203. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
204. Scroll tabel secara horizontal
205. Verifikasi kolom `Asset ID`, `Brand`, `Model / Type` tetap membeku setelah F5
206. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
207. Klik icon Pin pada `Asset ID` untuk unpin
208. Klik icon Pin pada `Brand` untuk unpin
209. Klik icon Pin pada `Model / Type` untuk unpin
210. Klik `[Save]`
211. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
212. Klik icon Pin pada `PIC`
213. Verifikasi preview menampilkan kolom `PIC` ter-pin
214. Klik `[Save]`
215. Scroll tabel secara horizontal
216. Verifikasi kolom `PIC` membeku (sticky) saat scroll horizontal setelah Save
217. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
218. Scroll tabel secara horizontal
219. Verifikasi kolom `PIC` tetap membeku setelah F5
220. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
221. Klik icon Pin pada `PIC` untuk unpin
222. Klik `[Save]`
223. Kembalikan viewport ke ukuran awal

### TC-GS-USER-781: Setup Column Reset to Default

224. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
225. Hilangkan centang `Brand`
226. Klik `[Save]`
227. Verifikasi tabel tanpa kolom `Brand` dengan urutan hasil perubahan `PIC | Model / Type | Asset ID | Name | Transaction ID | Photo`
228. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
229. Klik `[Reset to Default]`
230. Klik `[Save]`
231. Verifikasi susunan kolom kembali default: `Photo | Transaction ID | Name | Asset ID | Brand | Model / Type | PIC`
232. Muat ulang halaman (F5), lalu klik Tab `Responsibilities` dan sub-tab `Assigned Assets`
233. Verifikasi susunan default tetap bertahan setelah F5: `Photo | Transaction ID | Name | Asset ID | Brand | Model / Type | PIC`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE (preferensi kolom disimpan di browser; tabel dimuat dari backend nyata). Dataset 27 baris (lebih dari satu halaman) dipenuhi spec lewat seeding di hook `before`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 776, 777 (screening), 782, 783, 784 (batal dan guard tanpa Save), 778, 779, 780 (perubahan yang disimpan), lalu 781 (Reset to Default) di akhir. TC-GS-USER-782, 783, dan 784 tidak menyimpan perubahan sehingga ditaruh sebelum TC yang menyimpan; TC-GS-USER-781 ditaruh terakhir karena sekaligus memulihkan preferensi kolom ke default. Urutan di `tc-user.md`: 776 sampai 784 berurutan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 4 (pembukaan layar bersama untuk Ahmad Fauzi), langkah 34 dan 43 (menutup popup tanpa Save supaya perubahan checkbox dan pin tidak tersimpan; hook `after` sebagai cadangan), langkah 178 dan 223 (menyempitkan dan mengembalikan viewport), serta unpin dan centang kembali yang memulihkan state pada TC-GS-USER-778 dan 780. Langkah muat ulang halaman (F5) sekaligus membuka kembali Tab `Responsibilities` dan sub-tab `Assigned Assets` (F5 tidak dijamin mempertahankan Tab dan sub-tab; penetapan PRD menjadi tindak lanjut). Langkah pembuka popup yang berulang merupakan prefix berulang. TC-GS-USER-782 memakai popup yang masih terbuka dari TC-GS-USER-777 sehingga langkah Uji 4 TC-GS-USER-782 (`Buka Setup Column`) dipenuhi langkah pembuka TC-GS-USER-777.
- Siklus per kolom: TC-GS-USER-778 dan 779 pada TC sumber memuat siklus Save dan F5 per kolom; spec menjalankannya per kolom (satu `[Save]` dan satu F5 per kolom, tujuh kali) dengan `Verifikasi` preview, tabel setelah Save, dan persistensi setelah F5 untuk tiap kolom. TC-GS-USER-780: pin dikelompokkan menjadi tiga siklus (`Photo`, `Transaction ID`, `Name`; `Asset ID`, `Brand`, `Model / Type`; `PIC`) karena maksimal 3 kolom ter-pin sekaligus; tiap siklus punya Save, scroll, F5, dan `Verifikasi` sticky sesudah Save dan sesudah F5.
- Langkah Uji TC-GS-USER-778 `uncheck lalu check, Save, refresh F5` dibaca sebagai hide, Save, F5, lalu unhide, Save: uncheck yang langsung dibatalkan sebelum Save tidak mengubah konfigurasi tersimpan.
- Urutan seretan TC-GS-USER-779 mengikuti TC: `Photo` ke posisi terakhir, lalu `Transaction ID`, `Name`, `Asset ID`, `Brand`, `Model / Type`, `PIC` ke posisi pertama satu per satu, masing-masing dengan `[Save]` dan F5, sehingga urutan akhir `PIC | Model / Type | Brand | Asset ID | Name | Transaction ID | Photo`. Seret `Transaction ID` ke posisi pertama tidak mengubah susunan karena sudah pertama sesudah `Photo` dipindah ke posisi terakhir (lihat Temuan untuk QA).
- Anchor positif dan state: verifikasi preview tidak memuat `Brand` (TC-GS-USER-782) dan verifikasi tiga kolom ter-pin (TC-GS-USER-784) mendahului asersi yang bergantung pada state itu (S-14); verifikasi footer `[Reset to Default]` dan `[Save]` mendahului asersi ketiadaan `[Cancel]`. Pada TC-GS-USER-778, tiap `Verifikasi` kolom hide `tetap tidak tampil setelah F5` didahului `Verifikasi` kolom lain tampil setelah F5 sebagai anchor positif (`Transaction ID`, atau `Name` untuk kolom `Transaction ID`; bagian 8b butir 2).
- Spec melewati sekitar 35 langkah (233 langkah) karena sembilan TC berbagi satu popup Setup Column, satu layar, satu dataset 27 baris, dan satu kelas harness (fungsional). Blok 778, 779, dan 780 menguji tujuh kolom dengan blok identik (buka popup, ubah, Save, cek, F5) dan tiap blok berdiri sendiri; blok 781 memakai susunan hasil 779 dan 780 (Reset to Default). Langkah pembuka popup yang berulang dan pasangan klik per kolom merupakan prefix berulang.
- Pembagian TC lintas spec: TC-GS-USER-390, 391, 755 sampai 760 (termasuk Search terhadap kolom hidden) ada di spec 120; TC-GS-USER-761 sampai 768 ada di spec 121; TC-GS-USER-769 sampai 773 ada di spec 122; TC-GS-USER-774, 775, 790, 791 ada di spec 123; TC-GS-USER-392 dan 785 sampai 789 (Download terhadap kolom hidden) ada di spec 125.
- Temuan untuk QA:
  - TC-GS-USER-776 butir a vs TC-GS-USER-390 butir b: urutan kolom berbeda. Overlay: `Photo | Name | Asset ID | Transaction ID | Brand | Model / Type | PIC`; tabel: `Photo | Transaction ID | Name | Asset ID | Brand | Model / Type | PIC`. Spec mengikuti masing-masing TC (overlay di langkah verifikasi overlay, tabel di langkah verifikasi urutan default TC-GS-USER-781).
  - TC-GS-USER-776 butir b: `kolom Curated unchecked & enabled`, tetapi daftar kolom TC tidak memuat kolom Curated apa pun (ketujuh kolom Hideable dan default tampil); butir Curated tidak diasersi.
  - TC-GS-USER-777: `deskripsi panduan` tidak disebut teksnya; spec memakai teks deskripsi dari prd-conventions §9.3 (sumber yang dirujuk kolom Referensi TC).
  - TC-GS-USER-778, 779, 780: `uncheck lalu check` ambigu (lihat butir pembacaan langkah). TC-GS-USER-779 langkah Uji kedua (`Transaction ID` ke posisi pertama) tidak mengubah susunan karena sudah pertama sesudah `Photo` dipindah ke posisi terakhir; Expected tidak membedakannya dari kolom lain. TC-GS-USER-780 tidak menyebut ukuran viewport dan perilaku `kolom beku` untuk tabel yang tidak overflow; disediakan tim FE.
  - TC-GS-USER-781: Langkah Uji 4 (`Ubah urutan dan visibility kolom, Save`) tidak menyebut kolom dan urutan; spec memakai susunan hasil TC-GS-USER-779 dan menyembunyikan `Brand`.
  - TC-GS-USER-784: `kolom keempat` ambigu (urutan daftar popup vs urutan tabel); spec memakai `Brand` sebagai kolom yang belum ter-pin sesudah tiga kolom ter-pin.
  - Mekanisme menandai Guided Tooltip sebagai sudah dilihat, menyiapkan data FAMS, dan menghapus preferensi kolom di browser tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE. TC tidak menyatakan apakah F5 mempertahankan Tab dan sub-tab yang terbuka; spec membuka kembali Tab `Responsibilities` dan sub-tab `Assigned Assets` sesudah tiap F5 (keputusan audit #2).

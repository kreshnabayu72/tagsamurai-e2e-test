---
id: TC-GS-USER-E2E-094-tab-changelog-detail-setup-column-overlay-popup-hide-reorder-pin-reset
title: "Tab Changelog Detail: Setup Column (Overlay, Popup, Hide, Reorder, Pin, Reset, dan Guard)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-575
  - TC-GS-USER-576
  - TC-GS-USER-582
  - TC-GS-USER-583
  - TC-GS-USER-581
  - TC-GS-USER-577
  - TC-GS-USER-578
  - TC-GS-USER-579
  - TC-GS-USER-580
coverage:
  web: automated
---

# Tab Changelog Detail: Setup Column (Overlay, Popup, Hide, Reorder, Pin, Reset, dan Guard)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza, tampil `Siti N`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before` spec ini; akun ini adalah akun default suite sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Akun aksi lewat API (tidak login UI): Manage user and role Full CRUD (Fajar Nugroho, tampil `Fajar N`) `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 4; kredensial `Spectra.env.GS_FULLCRUD_PASSWORD`). Dipakai hanya untuk membuat entri Changelog dengan Modified By kedua.
- Env var: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD`.
- Data Pre-setup yang dipakai (hanya dibaca, tidak diubah; S-06): Position `Staff`, `Supervisor`, `Finance Manager`, dan `Internal Auditor` (Tabel Data Uji Pre-setup No. 22) dan Client PT Maju Bersama dengan subscription Fixed Asset + Supply Asset (No. 26). John Doe (No. 18) yang disebut TC tidak dipakai: riwayat Changelog-nya tidak dijamin memuat sedikitnya dua nilai distinct pada kolom yang diuji (S-11) dan data Pre-setup tidak diubah (S-06), sehingga spec memakai user uji milik spec.
- Data Dinamis (user uji milik spec, seeding lewat API di hook `before`; kemampuan seeding user lewat API disediakan tim FE/BE, endpoint tidak disebut di TC dan PRD):
  - User uji: Name `Log User {runId}-094`, Email `loguser+{runId}-094@qwertysystem.net`, Position `Staff`, Employee ID `{empId1}`, Access `Fixed Asset`, Active. `{empId1}`, `{empId2}`, `{empId3}` adalah tiga Employee ID numerik murni, naik berurutan (`{empId1}` < `{empId2}` < `{empId3}`), unik per run, dibuat hook dari waktu run (tanpa suffix `{runId}` karena nilainya harus numerik murni).
  - Entri Changelog base (12 entri, urutan seeding = urutan waktu, dari terlama ke terbaru; Modified By tampil `[First Name] [Last Initial]`):
    - a. `Create` | `Name` | `—` | `Log User {runId}-094` | `Siti N`
    - b. `Edit` | `Position` | `Staff` | `Supervisor` | `Siti N`
    - c. `Edit` | `Employee ID` | `{empId1}` | `{empId2}` | `Siti N`
    - d. `Deactivate` | `Status (Global)` | `Active` | `Inactive` | `Siti N`
    - e. `Activate` | `Status (Global)` | `Inactive` | `Active` | `Siti N`
    - f. `Add Access` | `App Access` | `—` | `Supply Asset` | `Siti N`
    - g. `Remove Access` | `App Access` | `Supply Asset` | `—` | `Siti N`
    - h. `Edit` | `Position` | `Supervisor` | `Finance Manager` | `Fajar N`
    - i. `Edit` | `Position` | `Finance Manager` | `Staff` | `Fajar N`
    - j. `Edit` | `Employee ID` | `{empId2}` | `{empId3}` | `Fajar N`
    - k. `Edit` | `Position` | `Staff` | `Internal Auditor` | `Fajar N`
    - l. `Edit` | `Position` | `Internal Auditor` | `Supervisor` | `Fajar N`
  - Pelaku entri: `Siti N` lewat sesi API Total Control, `Fajar N` lewat sesi API Fajar Nugroho. Dengan demikian kolom Modified By memuat dua nilai distinct (`Siti N`, `Fajar N`); kolom Action, Field, Old Value, dan New Value memuat sedikitnya dua nilai distinct (S-11).
- Kemampuan teknis yang disediakan tim FE/BE (TC, PRD, dan LLD tidak memberi cara): memberi cap waktu pada entri seed sehingga setiap entri berjarak sedikitnya 1 menit dari entri sebelumnya mengikuti urutan huruf di atas, dan entri a (`Create`) bercap tanggal hari uji dikurangi 2 hari (H-2) sedangkan entri lain bercap hari uji. Cap waktu ini membuat urutan Date deterministik (entri terbaru di atas) dan memberi dua nilai distinct pada kolom Date.
- Kemampuan teknis: drag and drop elemen daftar kolom; hover checkbox dan icon Pin yang disabled untuk membaca tooltip; scroll horizontal tabel; membaca dan menghapus penyimpanan konfigurasi kolom browser.
- Kemampuan teknis tambahan: mengatur lebar viewport sehingga tabel Changelog dapat di-scroll horizontal (TC tidak menyebut lebar viewport; viewport diperkecil sampai overflow horizontal) dan memulihkannya.
- Konfigurasi kolom Tab Changelog (urutan, visibilitas, pin) tersimpan di browser (prd-conventions.md §9.3); PRD user.md §4.1.5 tidak menyebut mekanisme penyimpanannya. Hook `before` mengosongkan konfigurasi kolom Tab Changelog akun Total Control sehingga spec mulai dari default (6 kolom tampil, urutan `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`, tanpa pin). "Muat ulang halaman" dilakukan pada konteks browser yang sama supaya penyimpanan tetap ada. Mekanisme membaca dan mengosongkan penyimpanan itu disediakan tim FE.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus user uji `Log User {runId}-094` lewat API. Entri Changelog tidak bisa dihapus.
- Precondition TC-GS-USER-575, 576, 577, 578, 579, 580, 581, 582, 583: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); data Pre-setup (Tabel Data Uji Pre-setup No. 10 sampai 22) tersedia; user uji punya riwayat Changelog.
- Suite serial (`parallel: false`) karena spec membaca dan mengubah konfigurasi kolom Tab Changelog di browser yang sama dengan spec lain.
- State global yang diubah dan dipulihkan: konfigurasi kolom Tab Changelog (visibilitas, urutan, pin) dikembalikan ke default lewat langkah `[Reset to Default]` di akhir spec; hook `after` memulihkan konfigurasi ke nilai awal sebagai cadangan dan memulihkan viewport.

## Test Steps

### TC-GS-USER-575: Screening Overlay Column Visibility

1. Klik icon Search di User List, ketik `Log User {runId}-094`, tekan Enter
2. Klik Name `Log User {runId}-094` di User List
3. Klik Tab `Changelog`
4. Klik header kolom Actions (⋯)
5. Verifikasi overlay memuat daftar kolom berurutan `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
6. Verifikasi keenam kolom (kelas Hideable) checked
7. Verifikasi keenam kolom (kelas Hideable) enabled
8. Verifikasi drag handle tersedia pada keenam kolom
9. Verifikasi item `Setup Column...` tersedia di overlay

### TC-GS-USER-576: Screening Popup Setup Column

10. Klik item `Setup Column...` pada overlay
11. Verifikasi Header: Title `Setup Column`
12. Verifikasi Header: deskripsi panduan tampil
13. Verifikasi Header: icon `[✕]`
14. Verifikasi Body: daftar enam kolom dengan checkbox
15. Verifikasi Body: keenam kolom memiliki drag handle
16. Verifikasi Body: keenam kolom memiliki icon Pin
17. Verifikasi Body: preview tabel Changelog
18. Verifikasi Footer: `[Reset to Default]` dan `[Save]`
19. Verifikasi Footer: tanpa `[Cancel]`
20. Klik `[✕]` untuk menutup popup tanpa perubahan

### TC-GS-USER-582: Guard satu kolom tersisa tidak bisa di-uncheck

21. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Action`, `Field`, `Old Value`, `New Value`, dan `Modified By` (tersisa `Date`)
22. Hover checkbox `Date`
23. Verifikasi checkbox `Date` tetap tampil
24. Verifikasi checkbox `Date` disabled
25. Verifikasi Tooltip `At least one column must remain visible.`
26. Klik `[✕]` untuk menutup popup tanpa menyimpan

### TC-GS-USER-583: Maksimal 3 kolom di-pin

27. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu klik icon Pin pada `Date`, `Action`, dan `Field`
28. Hover icon Pin kolom keempat (`Old Value`)
29. Verifikasi icon Pin `Old Value` disabled
30. Verifikasi Tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
31. Klik `[✕]` untuk menutup popup tanpa menyimpan

### TC-GS-USER-581: Tutup Setup Column lewat [✕] membuang perubahan

32. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu hilangkan centang `Field`
33. Klik `[✕]`
34. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir (keenam kolom tampil berurutan `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`)

### TC-GS-USER-577: Setup Column hide/unhide kelas Hideable

35. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu hilangkan centang `Date`
36. Verifikasi preview Setup Column tidak menampilkan kolom `Date`
37. Klik `[Save]`
38. Verifikasi kolom `Date` tidak tampil di tabel (tersimpan setelah Save)
39. Muat ulang halaman (F5)
40. Klik Tab `Changelog`
41. Verifikasi kolom `Action` tampil di tabel setelah F5
42. Verifikasi kolom `Date` tetap tidak tampil setelah F5
43. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Date`, lalu klik `[Save]`
44. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu hilangkan centang `Action`
45. Verifikasi preview Setup Column tidak menampilkan kolom `Action`
46. Klik `[Save]`
47. Verifikasi kolom `Action` tidak tampil di tabel (tersimpan setelah Save)
48. Muat ulang halaman (F5)
49. Klik Tab `Changelog`
50. Verifikasi kolom `Date` tampil di tabel setelah F5
51. Verifikasi kolom `Action` tetap tidak tampil setelah F5
52. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Action`, lalu klik `[Save]`
53. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu hilangkan centang `Field`
54. Verifikasi preview Setup Column tidak menampilkan kolom `Field`
55. Klik `[Save]`
56. Verifikasi kolom `Field` tidak tampil di tabel (tersimpan setelah Save)
57. Muat ulang halaman (F5)
58. Klik Tab `Changelog`
59. Verifikasi kolom `Date` tampil di tabel setelah F5
60. Verifikasi kolom `Field` tetap tidak tampil setelah F5
61. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Field`, lalu klik `[Save]`
62. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu hilangkan centang `Old Value`
63. Verifikasi preview Setup Column tidak menampilkan kolom `Old Value`
64. Klik `[Save]`
65. Verifikasi kolom `Old Value` tidak tampil di tabel (tersimpan setelah Save)
66. Muat ulang halaman (F5)
67. Klik Tab `Changelog`
68. Verifikasi kolom `Date` tampil di tabel setelah F5
69. Verifikasi kolom `Old Value` tetap tidak tampil setelah F5
70. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Old Value`, lalu klik `[Save]`
71. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu hilangkan centang `New Value`
72. Verifikasi preview Setup Column tidak menampilkan kolom `New Value`
73. Klik `[Save]`
74. Verifikasi kolom `New Value` tidak tampil di tabel (tersimpan setelah Save)
75. Muat ulang halaman (F5)
76. Klik Tab `Changelog`
77. Verifikasi kolom `Date` tampil di tabel setelah F5
78. Verifikasi kolom `New Value` tetap tidak tampil setelah F5
79. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `New Value`, lalu klik `[Save]`
80. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu hilangkan centang `Modified By`
81. Verifikasi preview Setup Column tidak menampilkan kolom `Modified By`
82. Klik `[Save]`
83. Verifikasi kolom `Modified By` tidak tampil di tabel (tersimpan setelah Save)
84. Muat ulang halaman (F5)
85. Klik Tab `Changelog`
86. Verifikasi kolom `Date` tampil di tabel setelah F5
87. Verifikasi kolom `Modified By` tetap tidak tampil setelah F5
88. Klik header Column Visibility (⋯), klik `Setup Column...`, centang kembali `Modified By`, lalu klik `[Save]`

### TC-GS-USER-578: Setup Column drag reorder kelas Hideable

89. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu seret `Date` ke posisi terakhir
90. Verifikasi preview Setup Column menampilkan kolom `Date` di posisi terakhir
91. Klik `[Save]`
92. Verifikasi kolom `Date` berada di posisi terakhir tabel (tersimpan setelah Save)
93. Muat ulang halaman (F5)
94. Klik Tab `Changelog`
95. Verifikasi kolom `Date` tetap di posisi terakhir setelah F5
96. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu seret `Action` ke posisi pertama
97. Verifikasi preview Setup Column menampilkan kolom `Action` di posisi pertama
98. Klik `[Save]`
99. Verifikasi kolom `Action` berada di posisi pertama tabel (tersimpan setelah Save)
100. Muat ulang halaman (F5)
101. Klik Tab `Changelog`
102. Verifikasi kolom `Action` tetap di posisi pertama setelah F5
103. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu seret `Field` ke posisi pertama
104. Verifikasi preview Setup Column menampilkan kolom `Field` di posisi pertama
105. Klik `[Save]`
106. Verifikasi kolom `Field` berada di posisi pertama tabel (tersimpan setelah Save)
107. Muat ulang halaman (F5)
108. Klik Tab `Changelog`
109. Verifikasi kolom `Field` tetap di posisi pertama setelah F5
110. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu seret `Old Value` ke posisi pertama
111. Verifikasi preview Setup Column menampilkan kolom `Old Value` di posisi pertama
112. Klik `[Save]`
113. Verifikasi kolom `Old Value` berada di posisi pertama tabel (tersimpan setelah Save)
114. Muat ulang halaman (F5)
115. Klik Tab `Changelog`
116. Verifikasi kolom `Old Value` tetap di posisi pertama setelah F5
117. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu seret `New Value` ke posisi pertama
118. Verifikasi preview Setup Column menampilkan kolom `New Value` di posisi pertama
119. Klik `[Save]`
120. Verifikasi kolom `New Value` berada di posisi pertama tabel (tersimpan setelah Save)
121. Muat ulang halaman (F5)
122. Klik Tab `Changelog`
123. Verifikasi kolom `New Value` tetap di posisi pertama setelah F5
124. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu seret `Modified By` ke posisi pertama
125. Verifikasi preview Setup Column menampilkan kolom `Modified By` di posisi pertama
126. Klik `[Save]`
127. Verifikasi kolom `Modified By` berada di posisi pertama tabel (tersimpan setelah Save)
128. Muat ulang halaman (F5)
129. Klik Tab `Changelog`
130. Verifikasi kolom `Modified By` tetap di posisi pertama setelah F5

### TC-GS-USER-579: Setup Column pin/unpin kelas Hideable

131. Klik header Column Visibility (⋯), klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`
132. Perkecil lebar viewport hingga tabel Changelog dapat di-scroll horizontal
133. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu klik icon Pin pada `Date`
134. Verifikasi preview Setup Column menandai kolom `Date` ter-pin
135. Klik `[Save]`
136. Scroll tabel Changelog secara horizontal
137. Verifikasi kolom `Date` beku saat scroll horizontal (tersimpan setelah Save)
138. Muat ulang halaman (F5)
139. Klik Tab `Changelog`
140. Scroll tabel Changelog secara horizontal
141. Verifikasi kolom `Date` tetap beku saat scroll horizontal setelah F5
142. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Date`, lalu klik `[Save]`
143. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu klik icon Pin pada `Action`
144. Verifikasi preview Setup Column menandai kolom `Action` ter-pin
145. Klik `[Save]`
146. Scroll tabel Changelog secara horizontal
147. Verifikasi kolom `Action` beku saat scroll horizontal (tersimpan setelah Save)
148. Muat ulang halaman (F5)
149. Klik Tab `Changelog`
150. Scroll tabel Changelog secara horizontal
151. Verifikasi kolom `Action` tetap beku saat scroll horizontal setelah F5
152. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Action`, lalu klik `[Save]`
153. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu klik icon Pin pada `Field`
154. Verifikasi preview Setup Column menandai kolom `Field` ter-pin
155. Klik `[Save]`
156. Scroll tabel Changelog secara horizontal
157. Verifikasi kolom `Field` beku saat scroll horizontal (tersimpan setelah Save)
158. Muat ulang halaman (F5)
159. Klik Tab `Changelog`
160. Scroll tabel Changelog secara horizontal
161. Verifikasi kolom `Field` tetap beku saat scroll horizontal setelah F5
162. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Field`, lalu klik `[Save]`
163. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu klik icon Pin pada `Old Value`
164. Verifikasi preview Setup Column menandai kolom `Old Value` ter-pin
165. Klik `[Save]`
166. Scroll tabel Changelog secara horizontal
167. Verifikasi kolom `Old Value` beku saat scroll horizontal (tersimpan setelah Save)
168. Muat ulang halaman (F5)
169. Klik Tab `Changelog`
170. Scroll tabel Changelog secara horizontal
171. Verifikasi kolom `Old Value` tetap beku saat scroll horizontal setelah F5
172. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Old Value`, lalu klik `[Save]`
173. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu klik icon Pin pada `New Value`
174. Verifikasi preview Setup Column menandai kolom `New Value` ter-pin
175. Klik `[Save]`
176. Scroll tabel Changelog secara horizontal
177. Verifikasi kolom `New Value` beku saat scroll horizontal (tersimpan setelah Save)
178. Muat ulang halaman (F5)
179. Klik Tab `Changelog`
180. Scroll tabel Changelog secara horizontal
181. Verifikasi kolom `New Value` tetap beku saat scroll horizontal setelah F5
182. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `New Value`, lalu klik `[Save]`
183. Klik header Column Visibility (⋯), klik `Setup Column...`, lalu klik icon Pin pada `Modified By`
184. Verifikasi preview Setup Column menandai kolom `Modified By` ter-pin
185. Klik `[Save]`
186. Scroll tabel Changelog secara horizontal
187. Verifikasi kolom `Modified By` beku saat scroll horizontal (tersimpan setelah Save)
188. Muat ulang halaman (F5)
189. Klik Tab `Changelog`
190. Scroll tabel Changelog secara horizontal
191. Verifikasi kolom `Modified By` tetap beku saat scroll horizontal setelah F5
192. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Modified By`, lalu klik `[Save]`
193. Pulihkan lebar viewport ke ukuran semula

### TC-GS-USER-580: Setup Column Reset to Default

194. Klik header Column Visibility (⋯), klik `Setup Column...`, hilangkan centang `Modified By`, seret `Field` ke posisi pertama, lalu klik `[Save]`
195. Verifikasi kolom `Field` berada di posisi pertama tabel
196. Verifikasi kolom `Modified By` tidak tampil di tabel
197. Klik header Column Visibility (⋯), klik `Setup Column...`
198. Klik `[Reset to Default]`
199. Klik `[Save]`
200. Verifikasi susunan kolom kembali default: `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
201. Muat ulang halaman (F5)
202. Klik Tab `Changelog`
203. Verifikasi susunan kolom default bertahan setelah F5

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-USER-575, 576, 582, 583, 581, 577, 578, 579, 580. Alasan: dua TC screening (575, 576) di awal; TC-GS-USER-582, 583 (dibatalkan lewat `[✕]`) dan 581 (`[✕]` membuang perubahan) sebelum TC-GS-USER-577, 578, dan 579 yang menyimpan konfigurasi (bagian 3 konvensi); TC-GS-USER-580 terakhir karena reset mengembalikan konfigurasi yang diubah TC sebelumnya. Detail user dan Tab `Changelog` dibuka sekali di langkah 1 sampai 3.
- Langkah 1 sampai 3 (mencari user uji lewat Search User List, lalu klik Name dan Tab `Changelog`) adalah langkah penghubung tanpa `Verifikasi`; TC menulis "Klik Name `John Doe`" tanpa cara menemukan baris, dan user uji milik spec menggantikan John Doe (lihat Prerequisites).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah menutup popup dengan `[✕]` setelah TC-GS-USER-576, 582, dan 583; langkah "centang kembali `X`, lalu klik `[Save]`" setelah tiap kolom pada TC-GS-USER-577 (mengembalikan kolom yang disembunyikan sebelum kolom berikutnya; contoh pertama: langkah 43); langkah "unpin `X`, lalu klik `[Save]`" setelah tiap kolom pada TC-GS-USER-579 (contoh pertama: langkah 142); langkah 131 (reset ke default sebelum pin, karena TC-GS-USER-578 meninggalkan urutan kolom terbalik); langkah 132 dan 193 (memperkecil dan memulihkan viewport agar scroll horizontal teramati). Langkah membuka popup (klik header Column Visibility lalu `Setup Column...`) digabung dalam langkah aksi pertama di popup, karena `[Save]` menutup popup dan tabel diamati sesudahnya.
- TC-GS-USER-577 menguji hide per kolom: tiap kolom dihilangkan, disimpan, diverifikasi di preview, tabel, dan setelah F5, lalu dikembalikan sebelum kolom berikutnya. Kata "uncheck lalu check" pada TC tidak ditulis sebagai satu aksi karena hasil akhirnya tanpa perubahan dan tidak menghasilkan perubahan yang dapat diasersi pada preview, tabel, dan setelah F5.
- TC-GS-USER-578 menggeser `Date` ke posisi terakhir lebih dulu (langkah TC), lalu `Action`, `Field`, `Old Value`, `New Value`, dan `Modified By` ke posisi pertama berturut-turut tanpa reset di antaranya, sehingga urutan akhir `Modified By`, `New Value`, `Old Value`, `Field`, `Action`, `Date`. Sesudah `Date` di posisi terakhir, `Action` sudah berada di posisi pertama sehingga seretan `Action` tidak mengubah urutan (lihat Temuan untuk QA).
- Anchor positif tambahan (S-03, bagian 8b butir 2): sebelum tiap `Verifikasi` kolom hide `tetap tidak tampil setelah F5` ditaruh `Verifikasi` kolom lain tampil setelah F5 (`Action` untuk `Date`, `Date` untuk kolom lain). Pada TC-GS-USER-580, langkah 195 (kolom `Field` di posisi pertama) dan langkah 196 (kolom `Modified By` tidak tampil) mengamati perubahan sebelum reset agar reset tidak lulus pada konfigurasi yang tidak berubah.
- Pembagian TC Tab Changelog di User Detail: Setup Column di spec 094; Search di spec 090; Filter Panel di spec 091; kombinasi di spec 092; Sort dan Pagination di spec 093; Download di spec 095.
- Spec melewati sekitar 35 langkah (203 langkah) karena TC-GS-USER-577, 578, dan 579 masing-masing menguji enam kolom dengan `Verifikasi` untuk preview, tersimpan setelah Save, dan setelah F5 (S-01); semua blok satu kelas harness (Setup Column Tab Changelog), satu akun, satu dataset, dan tiap blok berdiri sendiri karena konfigurasi dikembalikan di tiap kolom (TC-GS-USER-577 dan 579) atau di-reset (TC-GS-USER-580).
- Temuan untuk QA: (1) Cap waktu entri Changelog (entri `Create` H-2, jarak sedikitnya 1 menit antar entri) tidak punya cara di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE (S-13). (2) Label Field Changelog untuk perubahan Employee ID tidak disebut eksplisit (PRD user.md §8.3 hanya menulis `[Field]`); spec memakai `Employee ID`. (3) TC-GS-USER-575 Expected b menyebut "kolom Curated unchecked & enabled", padahal PRD user.md §4.1.5 menetapkan semua kolom Tab Changelog Hideable (tidak ada Curated); spec mengasersi hanya kolom Hideable. (4) TC-GS-USER-575 dan 576 menyebut item `Setup Column...` (spec User List memakai `[Setup Column]`); spec mengikuti TC-GS-USER-575. (5) TC-GS-USER-576 Expected a menyebut "deskripsi panduan" tanpa teks; spec hanya mengasersi deskripsi tampil. (6) TC-GS-USER-577 "uncheck lalu check" tidak menghasilkan perubahan bersih; lihat Notes. (7) TC-GS-USER-578 menggeser `Date` ke posisi terakhir (langkah 4) lalu `Action` ke posisi pertama (langkah 5) padahal `Action` sudah pertama sesudah `Date` dipindah; Expected tidak membedakan kasus ini. (8) TC-GS-USER-579 tidak menyebut lebar viewport atau cara membuat tabel overflow. (9) TC-GS-USER-580 tidak menyebut perubahan urutan dan visibilitas yang dipakai; spec menyembunyikan `Modified By` dan menyeret `Field` ke posisi pertama; pin tidak diubah karena TC hanya menyebut urutan dan visibility. (10) TC-GS-USER-582 dan 583 tidak menyebut kolom yang dipertahankan atau di-pin; spec memakai `Date` (582) dan `Date`, `Action`, `Field` (583).


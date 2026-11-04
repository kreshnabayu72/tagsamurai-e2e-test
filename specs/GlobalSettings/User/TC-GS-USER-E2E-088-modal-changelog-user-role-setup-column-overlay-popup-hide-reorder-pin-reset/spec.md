---
id: TC-GS-USER-E2E-088-modal-changelog-user-role-setup-column-overlay-popup-hide-reorder-pin-reset
title: "Modal Changelog Role: Setup Column (overlay, popup, hide, reorder, pin, reset, guard)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-535
  - TC-GS-USER-536
  - TC-GS-USER-537
  - TC-GS-USER-538
  - TC-GS-USER-539
  - TC-GS-USER-540
  - TC-GS-USER-541
  - TC-GS-USER-542
  - TC-GS-USER-543
coverage:
  web: automated
---

# Modal Changelog Role: Setup Column (overlay, popup, hide, reorder, pin, reset, guard)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control Siti Nurhaliza (`Siti N`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 2), akun default suite. Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User).
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: tidak dipakai. TC menyebut `Ahmad Fauzi` (Tabel Data Uji Pre-setup baris 13); aksi tulis Role memakai user seed milik spec (S-06), jadi Pre-setup tidak diubah.
- Data Dinamis: user seed `Ahmad Fauzi {runId}-088`, email `ahmadfauzi+{runId}-088@qwertysystem.net`, Access `Global Settings`, bukan tier, field wajib lain diisi seadanya oleh seeding.
- Seeding minimal (S-11; lewat API oleh Siti N di hook `before`, urutan sebagai berikut; setara TC-GS-USER-902, 903, 904). Spec ini tidak mengasersi isi baris, hanya struktur kolom, sehingga riwayat Assign, Remove, dan Edit Role cukup satu per jenis:
  - 1. Assign `Manage TAG` -> `Assign | Manage TAG | Access | — | Assigned | Siti N`.
  - 2. Centang Update `Manage TAG` -> `Edit | Manage TAG | Update | Inactive | Active | Siti N`.
  - 3. Assign `Manage files` -> `Assign | Manage files | Access | — | Assigned | Siti N`.
  - 4. Remove `Manage files` -> `Remove | Manage files | Access | Assigned | — | Siti N`.
- Preferensi Setup Column (urutan, visibilitas, dan pin) Modal Changelog Role tersimpan di `localStorage` browser dengan key unik per tabel (prd-conventions.md §9.3; nama key disediakan tim FE). Hook `before` mengosongkan konfigurasi itu sehingga spec mulai dari default (urutan `Date | Action | Role | Field | Old Value | New Value | Modified By`, 7 kolom tampil, tanpa pin). "Muat ulang halaman" dilakukan pada konteks browser yang sama supaya `localStorage` tetap ada. Hook `after` mengosongkan kembali konfigurasi itu (cadangan bila spec gagal di tengah) dan mengembalikan viewport ke bawaan.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus user seed lewat API; pulihkan preferensi Setup Column dan viewport seperti di atas. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: drag and drop elemen daftar kolom pada popup Setup Column; hover checkbox disabled dan icon Pin disabled untuk membaca tooltip; mengatur lebar viewport sehingga tabel Changelog dapat di-scroll horizontal (TC tidak menyebut lebar; kontainer dipersempit sampai overflow horizontal) dan scroll horizontal tabel; membaca dan menghapus key `localStorage`.
- Precondition TC-GS-USER-535 sampai 543: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); data pre-setup User tersedia; riwayat Changelog Role user seed terisi.
- Suite serial (`parallel: false`) karena preferensi kolom disimpan di browser yang sama dengan spec lain, lihat `suite.md`.
- State global yang dipulihkan: preferensi Setup Column Modal Changelog Role (default, tanpa pin) dan viewport.

## Test Steps

### TC-GS-USER-535: Screening Overlay Column Visibility

1. Ketik Search `Ahmad Fauzi {runId}-088`, tekan Enter
2. Klik Name `Ahmad Fauzi {runId}-088` di User List
3. Klik Tab `Role`
4. Klik icon Changelog di toolbar Tab Role
5. Klik header kolom Column Visibility (⋯)
6. Verifikasi overlay memuat daftar kolom `Date` | `Action` | `Role` | `Field` | `Old Value` | `New Value` | `Modified By`
7. Verifikasi ketujuh kolom Hideable checked dan enabled
8. Verifikasi ketujuh kolom memiliki drag handle
9. Verifikasi item `Setup Column...` tersedia di overlay

### TC-GS-USER-536: Screening Popup Setup Column

10. Klik item `Setup Column...` pada overlay
11. Verifikasi bagian Header: Title `Setup Column`
12. Verifikasi bagian Header: deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
13. Verifikasi bagian Header: icon `[✕]`
14. Verifikasi bagian Body: daftar kolom dengan checkbox
15. Verifikasi bagian Body: drag handle pada tiap kolom
16. Verifikasi bagian Body: icon Pin pada tiap kolom
17. Verifikasi bagian Body: preview tabel
18. Verifikasi bagian Footer: `[Reset to Default]` dan `[Save]`
19. Verifikasi bagian Footer: tidak ada `[Cancel]`

### TC-GS-USER-542: Guard satu kolom tersisa tidak bisa di-uncheck

20. Hilangkan centang enam kolom `Action`, `Role`, `Field`, `Old Value`, `New Value`, dan `Modified By` (tersisa `Date`)
21. Hover checkbox `Date`
22. Verifikasi checkbox `Date` tetap tampil
23. Verifikasi checkbox `Date` disabled
24. Verifikasi Tooltip `At least one column must remain visible.`
25. Klik `[✕]` untuk menutup popup tanpa menyimpan

### TC-GS-USER-543: Maksimal 3 kolom di-pin

26. Klik header (⋯), klik `Setup Column...`, lalu klik Pin pada kolom `Date`, `Action`, dan `Role`
27. Verifikasi ketiga kolom `Date`, `Action`, dan `Role` berstatus pinned pada popup
28. Hover icon Pin kolom keempat (`Field`)
29. Verifikasi icon Pin kolom `Field` disabled
30. Verifikasi Tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`

### TC-GS-USER-541: Tutup Setup Column via [✕] membuang perubahan

31. Hilangkan centang `Field` pada popup yang sama
32. Verifikasi preview tabel pada popup tidak memuat kolom `Field`
33. Klik `[✕]`
34. Verifikasi tabel Changelog kembali ke konfigurasi tersimpan terakhir (7 kolom `Date | Action | Role | Field | Old Value | New Value | Modified By` tampil, tanpa pin)

### TC-GS-USER-537: Setup Column hide dan unhide kelas Hideable

35. Klik header (⋯), klik `Setup Column...`, hilangkan centang `Date`
36. Verifikasi Date: preview tabel pada popup tidak memuat kolom `Date`
37. Klik `[Save]`
38. Verifikasi Date: kolom `Date` tidak tampil di tabel Changelog (tersimpan setelah Save)
39. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
40. Verifikasi kolom `Action` tampil di tabel setelah F5
41. Verifikasi Date: kolom `Date` tetap tidak tampil setelah F5
42. Klik header (⋯), klik `Setup Column...`, centang kembali `Date`, lalu klik `[Save]`
43. Klik header (⋯), klik `Setup Column...`, hilangkan centang `Action`
44. Verifikasi Action: preview tabel pada popup tidak memuat kolom `Action`
45. Klik `[Save]`
46. Verifikasi Action: kolom `Action` tidak tampil di tabel Changelog (tersimpan setelah Save)
47. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
48. Verifikasi kolom `Date` tampil di tabel setelah F5
49. Verifikasi Action: kolom `Action` tetap tidak tampil setelah F5
50. Klik header (⋯), klik `Setup Column...`, centang kembali `Action`, lalu klik `[Save]`
51. Klik header (⋯), klik `Setup Column...`, hilangkan centang `Role`
52. Verifikasi Role: preview tabel pada popup tidak memuat kolom `Role`
53. Klik `[Save]`
54. Verifikasi Role: kolom `Role` tidak tampil di tabel Changelog (tersimpan setelah Save)
55. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
56. Verifikasi kolom `Date` tampil di tabel setelah F5
57. Verifikasi Role: kolom `Role` tetap tidak tampil setelah F5
58. Klik header (⋯), klik `Setup Column...`, centang kembali `Role`, lalu klik `[Save]`
59. Klik header (⋯), klik `Setup Column...`, hilangkan centang `Field`
60. Verifikasi Field: preview tabel pada popup tidak memuat kolom `Field`
61. Klik `[Save]`
62. Verifikasi Field: kolom `Field` tidak tampil di tabel Changelog (tersimpan setelah Save)
63. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
64. Verifikasi kolom `Date` tampil di tabel setelah F5
65. Verifikasi Field: kolom `Field` tetap tidak tampil setelah F5
66. Klik header (⋯), klik `Setup Column...`, centang kembali `Field`, lalu klik `[Save]`
67. Klik header (⋯), klik `Setup Column...`, hilangkan centang `Old Value`
68. Verifikasi Old Value: preview tabel pada popup tidak memuat kolom `Old Value`
69. Klik `[Save]`
70. Verifikasi Old Value: kolom `Old Value` tidak tampil di tabel Changelog (tersimpan setelah Save)
71. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
72. Verifikasi kolom `Date` tampil di tabel setelah F5
73. Verifikasi Old Value: kolom `Old Value` tetap tidak tampil setelah F5
74. Klik header (⋯), klik `Setup Column...`, centang kembali `Old Value`, lalu klik `[Save]`
75. Klik header (⋯), klik `Setup Column...`, hilangkan centang `New Value`
76. Verifikasi New Value: preview tabel pada popup tidak memuat kolom `New Value`
77. Klik `[Save]`
78. Verifikasi New Value: kolom `New Value` tidak tampil di tabel Changelog (tersimpan setelah Save)
79. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
80. Verifikasi kolom `Date` tampil di tabel setelah F5
81. Verifikasi New Value: kolom `New Value` tetap tidak tampil setelah F5
82. Klik header (⋯), klik `Setup Column...`, centang kembali `New Value`, lalu klik `[Save]`
83. Klik header (⋯), klik `Setup Column...`, hilangkan centang `Modified By`
84. Verifikasi Modified By: preview tabel pada popup tidak memuat kolom `Modified By`
85. Klik `[Save]`
86. Verifikasi Modified By: kolom `Modified By` tidak tampil di tabel Changelog (tersimpan setelah Save)
87. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
88. Verifikasi kolom `Date` tampil di tabel setelah F5
89. Verifikasi Modified By: kolom `Modified By` tetap tidak tampil setelah F5
90. Klik header (⋯), klik `Setup Column...`, centang kembali `Modified By`, lalu klik `[Save]`

### TC-GS-USER-538: Setup Column drag reorder kelas Hideable

91. Klik header (⋯), klik `Setup Column...`, geser kolom `Date` ke posisi terakhir
92. Verifikasi Date: preview tabel pada popup menampilkan `Date` di posisi terakhir
93. Klik `[Save]`
94. Verifikasi Date: kolom `Date` di posisi terakhir tabel Changelog (tersimpan setelah Save)
95. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
96. Verifikasi Date: kolom `Date` tetap di posisi terakhir setelah F5
97. Klik header (⋯), klik `Setup Column...`, geser kolom `Action` ke posisi pertama
98. Verifikasi Action: preview tabel pada popup menampilkan `Action` di posisi pertama
99. Klik `[Save]`
100. Verifikasi Action: kolom `Action` di posisi pertama tabel Changelog (tersimpan setelah Save)
101. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
102. Verifikasi Action: kolom `Action` tetap di posisi pertama setelah F5
103. Klik header (⋯), klik `Setup Column...`, geser kolom `Role` ke posisi pertama
104. Verifikasi Role: preview tabel pada popup menampilkan `Role` di posisi pertama
105. Klik `[Save]`
106. Verifikasi Role: kolom `Role` di posisi pertama tabel Changelog (tersimpan setelah Save)
107. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
108. Verifikasi Role: kolom `Role` tetap di posisi pertama setelah F5
109. Klik header (⋯), klik `Setup Column...`, geser kolom `Field` ke posisi pertama
110. Verifikasi Field: preview tabel pada popup menampilkan `Field` di posisi pertama
111. Klik `[Save]`
112. Verifikasi Field: kolom `Field` di posisi pertama tabel Changelog (tersimpan setelah Save)
113. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
114. Verifikasi Field: kolom `Field` tetap di posisi pertama setelah F5
115. Klik header (⋯), klik `Setup Column...`, geser kolom `Old Value` ke posisi pertama
116. Verifikasi Old Value: preview tabel pada popup menampilkan `Old Value` di posisi pertama
117. Klik `[Save]`
118. Verifikasi Old Value: kolom `Old Value` di posisi pertama tabel Changelog (tersimpan setelah Save)
119. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
120. Verifikasi Old Value: kolom `Old Value` tetap di posisi pertama setelah F5
121. Klik header (⋯), klik `Setup Column...`, geser kolom `New Value` ke posisi pertama
122. Verifikasi New Value: preview tabel pada popup menampilkan `New Value` di posisi pertama
123. Klik `[Save]`
124. Verifikasi New Value: kolom `New Value` di posisi pertama tabel Changelog (tersimpan setelah Save)
125. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
126. Verifikasi New Value: kolom `New Value` tetap di posisi pertama setelah F5
127. Klik header (⋯), klik `Setup Column...`, geser kolom `Modified By` ke posisi pertama
128. Verifikasi Modified By: preview tabel pada popup menampilkan `Modified By` di posisi pertama
129. Klik `[Save]`
130. Verifikasi Modified By: kolom `Modified By` di posisi pertama tabel Changelog (tersimpan setelah Save)
131. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
132. Verifikasi Modified By: kolom `Modified By` tetap di posisi pertama setelah F5

### TC-GS-USER-539: Setup Column pin dan unpin kelas Hideable

133. Perkecil lebar viewport hingga tabel Changelog dapat di-scroll horizontal
134. Klik header (⋯), klik `Setup Column...`, klik Pin pada kolom `Date`
135. Verifikasi Date: preview tabel pada popup menampilkan `Date` berstatus pinned
136. Klik `[Save]`
137. Verifikasi Date: kolom `Date` berstatus pinned di tabel Changelog (tersimpan setelah Save)
138. Scroll horizontal tabel Changelog
139. Verifikasi Date: kolom `Date` tetap terlihat saat scroll horizontal (kolom beku)
140. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
141. Verifikasi Date: kolom `Date` tetap berstatus pinned setelah F5
142. Klik header (⋯), klik `Setup Column...`, klik Unpin pada kolom `Date`, lalu klik `[Save]`
143. Klik header (⋯), klik `Setup Column...`, klik Pin pada kolom `Action`
144. Verifikasi Action: preview tabel pada popup menampilkan `Action` berstatus pinned
145. Klik `[Save]`
146. Verifikasi Action: kolom `Action` berstatus pinned di tabel Changelog (tersimpan setelah Save)
147. Scroll horizontal tabel Changelog
148. Verifikasi Action: kolom `Action` tetap terlihat saat scroll horizontal (kolom beku)
149. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
150. Verifikasi Action: kolom `Action` tetap berstatus pinned setelah F5
151. Klik header (⋯), klik `Setup Column...`, klik Unpin pada kolom `Action`, lalu klik `[Save]`
152. Klik header (⋯), klik `Setup Column...`, klik Pin pada kolom `Role`
153. Verifikasi Role: preview tabel pada popup menampilkan `Role` berstatus pinned
154. Klik `[Save]`
155. Verifikasi Role: kolom `Role` berstatus pinned di tabel Changelog (tersimpan setelah Save)
156. Scroll horizontal tabel Changelog
157. Verifikasi Role: kolom `Role` tetap terlihat saat scroll horizontal (kolom beku)
158. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
159. Verifikasi Role: kolom `Role` tetap berstatus pinned setelah F5
160. Klik header (⋯), klik `Setup Column...`, klik Unpin pada kolom `Role`, lalu klik `[Save]`
161. Klik header (⋯), klik `Setup Column...`, klik Pin pada kolom `Field`
162. Verifikasi Field: preview tabel pada popup menampilkan `Field` berstatus pinned
163. Klik `[Save]`
164. Verifikasi Field: kolom `Field` berstatus pinned di tabel Changelog (tersimpan setelah Save)
165. Scroll horizontal tabel Changelog
166. Verifikasi Field: kolom `Field` tetap terlihat saat scroll horizontal (kolom beku)
167. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
168. Verifikasi Field: kolom `Field` tetap berstatus pinned setelah F5
169. Klik header (⋯), klik `Setup Column...`, klik Unpin pada kolom `Field`, lalu klik `[Save]`
170. Klik header (⋯), klik `Setup Column...`, klik Pin pada kolom `Old Value`
171. Verifikasi Old Value: preview tabel pada popup menampilkan `Old Value` berstatus pinned
172. Klik `[Save]`
173. Verifikasi Old Value: kolom `Old Value` berstatus pinned di tabel Changelog (tersimpan setelah Save)
174. Scroll horizontal tabel Changelog
175. Verifikasi Old Value: kolom `Old Value` tetap terlihat saat scroll horizontal (kolom beku)
176. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
177. Verifikasi Old Value: kolom `Old Value` tetap berstatus pinned setelah F5
178. Klik header (⋯), klik `Setup Column...`, klik Unpin pada kolom `Old Value`, lalu klik `[Save]`
179. Klik header (⋯), klik `Setup Column...`, klik Pin pada kolom `New Value`
180. Verifikasi New Value: preview tabel pada popup menampilkan `New Value` berstatus pinned
181. Klik `[Save]`
182. Verifikasi New Value: kolom `New Value` berstatus pinned di tabel Changelog (tersimpan setelah Save)
183. Scroll horizontal tabel Changelog
184. Verifikasi New Value: kolom `New Value` tetap terlihat saat scroll horizontal (kolom beku)
185. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
186. Verifikasi New Value: kolom `New Value` tetap berstatus pinned setelah F5
187. Klik header (⋯), klik `Setup Column...`, klik Unpin pada kolom `New Value`, lalu klik `[Save]`
188. Klik header (⋯), klik `Setup Column...`, klik Pin pada kolom `Modified By`
189. Verifikasi Modified By: preview tabel pada popup menampilkan `Modified By` berstatus pinned
190. Klik `[Save]`
191. Verifikasi Modified By: kolom `Modified By` berstatus pinned di tabel Changelog (tersimpan setelah Save)
192. Scroll horizontal tabel Changelog
193. Verifikasi Modified By: kolom `Modified By` tetap terlihat saat scroll horizontal (kolom beku)
194. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
195. Verifikasi Modified By: kolom `Modified By` tetap berstatus pinned setelah F5
196. Klik header (⋯), klik `Setup Column...`, klik Unpin pada kolom `Modified By`, lalu klik `[Save]`
197. Pulihkan lebar viewport ke ukuran semula

### TC-GS-USER-540: Setup Column Reset to Default

198. Klik header (⋯), klik `Setup Column...`, geser kolom `Modified By` ke posisi pertama, hilangkan centang `Role`, lalu klik `[Save]`
199. Verifikasi tabel Changelog menampilkan kolom `Modified By` di posisi pertama
200. Verifikasi tabel Changelog tidak menampilkan kolom `Role`
201. Klik header (⋯), klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`
202. Verifikasi susunan kolom kembali default (`Date | Action | Role | Field | Old Value | New Value | Modified By`)
203. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Tab `Role`, Klik icon Changelog)
204. Verifikasi susunan kolom default bertahan setelah F5

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Modal Changelog Role dibuka di langkah 2 sampai 4 dan dibuka kembali sesudah tiap muat ulang halaman (F5 menutup modal); pembukaan ulang itu tidak dihitung dalam batas langkah.
- Urutan TC dalam spec: TC-GS-USER-535, 536, 542, 543, 541, 537, 538, 539, 540. Alasan: dua TC screening (535, 536) di awal; TC-GS-USER-542 (guard), 543 (batas pin), dan 541 (`[✕]` membuang perubahan) tidak menyimpan konfigurasi sehingga mendahului TC yang menyimpan (bagian 3 konvensi); TC-GS-USER-537, 538, 539 menyimpan konfigurasi; TC-GS-USER-540 (Reset to Default) terakhir karena mengembalikan susunan ke default. TC-GS-USER-542, 543, dan 541 memakai popup Setup Column yang sama: popup dibuka di langkah 10 (TC-GS-USER-536), ditutup di langkah 25 dan dibuka lagi di langkah 26, dan perubahan pin langkah 26 dibuang bersama perubahan langkah 31 oleh `[✕]` di langkah 33.
- Pada TC-GS-USER-538 reorder berlaku kumulatif: tiap geser dikerjakan di atas urutan hasil geser sebelumnya, tanpa memulihkan urutan sebelumnya. Urutan kolom diuji `Date` (digeser ke posisi terakhir, sesuai langkah TC), lalu `Action`, `Role`, `Field`, `Old Value`, `New Value`, dan `Modified By` (digeser ke posisi pertama). Sesudah `Date` di posisi terakhir, `Action` sudah berada di posisi pertama sehingga langkah TC untuk `Action` tidak mengubah urutan (lihat Temuan untuk QA). Urutan susunan akhir dipulihkan di TC-GS-USER-540 (langkah 201 sampai 204).
- Pada TC-GS-USER-537 dan 539 TC menulis "uncheck lalu check" dan "Pin ... lalu Unpin" sebelum atau sesudah `[Save]` dan F5; spec membaca urutannya sebagai ubah (hide atau Pin), `[Save]`, muat ulang halaman, lalu pulihkan (centang kembali atau Unpin, `[Save]`), sehingga tiap kolom dimulai dari default. Butir Expected "tampil di preview, tersimpan setelah Save, dan bertahan setelah F5" menjadi tiga `Verifikasi` per kolom (preview, setelah Save, setelah F5), dan "kolom beku saat scroll horizontal" menjadi `Verifikasi` keempat pada TC-GS-USER-539.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search nama baris persis sebelum Klik Name, karena User List bisa lebih dari satu halaman; akhiran runId saja tidak cukup), langkah 25 (menutup popup tanpa menyimpan), langkah pemulihan di akhir tiap kolom TC-GS-USER-537 (centang kembali dan `[Save]`) dan TC-GS-USER-539 (Unpin dan `[Save]`), langkah scroll horizontal pada TC-GS-USER-539, serta langkah "Muat ulang halaman (F5), lalu buka kembali Modal Changelog" yang memenuhi langkah "refresh F5" di TC.
- Anchor positif tambahan (S-03, bagian 8b butir 2): sebelum tiap `Verifikasi` kolom hide `tetap tidak tampil setelah F5` ditaruh `Verifikasi` kolom lain tampil setelah F5 (`Action` untuk `Date`, `Date` untuk kolom lain). Pada TC-GS-USER-540, langkah 199 (kolom `Modified By` di posisi pertama) dan langkah 200 (kolom `Role` tidak tampil) mengamati perubahan sebelum reset agar reset tidak lulus pada konfigurasi yang tidak berubah. Langkah memperkecil viewport sebelum Pin pertama dan memulihkannya sesudah Unpin terakhir adalah langkah penghubung TC-GS-USER-539 (langkah scroll horizontal).
- Langkah 27 dan 32 adalah anchor positif untuk asersi berikutnya (pin pada tiga kolom berhasil sebelum Pin keempat disabled; perubahan centang terlihat sebelum `[✕]` membuangnya; S-03). Langkah 34 mengasersi konfigurasi tersimpan terakhir sebagai default (7 kolom, tanpa pin) karena hook `before` mengosongkan konfigurasi.
- Spec melewati sekitar 35 langkah (204 langkah; sekitar 182 tanpa pembukaan ulang modal sesudah F5) karena tujuh kolom Hideable pada TC-GS-USER-537, 538, dan 539 masing-masing menjadi blok sendiri sesuai butir Expected a sampai g (S-01) dengan tiga sampai empat `Verifikasi` per kolom. Semua blok satu kelas harness (Setup Column tabel Modal Changelog Role), satu layar, satu akun, dan satu dataset; tiap blok kolom berdiri sendiri karena konfigurasi dipulihkan ke default di akhir blok (centang kembali atau Unpin), sehingga kegagalan satu kolom tidak membuat kolom lain kehilangan makna; modal dan popup memakai pembukaan yang sama.
- Pembagian TC Setup Column: pengaruh kolom hidden pada Search (TC-GS-USER-516), Filter (TC-GS-USER-530), dan Download (TC-GS-USER-547) diverifikasi di spec 084, 086, dan 089.
- Temuan untuk QA: (1) TC-GS-USER-535 Expected b menyebut "kolom Curated unchecked & enabled", tetapi PRD user.md §4.1.9 menetapkan ketujuh kolom Hideable (tidak ada kolom Curated); spec hanya mengasersi kolom Hideable. (2) TC-GS-USER-535 menyebut header "Actions (⋯)" sedangkan TC-GS-USER-510 menyebut `Column Visibility (⋯)`; spec memakai `Column Visibility (⋯)`. (3) TC-GS-USER-536 menyebut "deskripsi panduan" tanpa teks; spec memakai teks deskripsi dari prd-conventions §9.3 (sumber yang dirujuk kolom Referensi TC). (4) TC-GS-USER-537, 538, dan 539 "uncheck lalu check" dan "Pin ... lalu Unpin" ambigu terhadap urutan Save dan F5; spec menulis penafsiran di Notes. (5) TC-GS-USER-538 menggeser `Date` ke posisi terakhir, lalu `Action` ke posisi pertama padahal `Action` sudah pertama sesudah `Date` dipindah; Expected tidak membedakannya dari kolom lain. (6) TC-GS-USER-539 "scroll horizontal" tidak menyebut lebar viewport; kemampuan mempersempit viewport diminta dari tim FE. (7) TC-GS-USER-542 dan 543 tidak menyebut apakah uji dilakukan di overlay atau popup; spec memakai popup Setup Column. (8) TC-GS-USER-535 sampai 543 menyebut `Ahmad Fauzi` tanpa suffix; spec memakai user seed bersuffix.

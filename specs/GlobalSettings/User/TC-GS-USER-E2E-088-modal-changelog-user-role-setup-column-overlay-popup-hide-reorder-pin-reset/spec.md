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

1. Klik Name `Ahmad Fauzi {runId}-088` di User List
2. Klik Tab `Role`
3. Klik icon Changelog di toolbar Tab Role
4. Klik header kolom Column Visibility (⋯)
5. Verifikasi overlay memuat daftar kolom `Date` | `Action` | `Role` | `Field` | `Old Value` | `New Value` | `Modified By`
6. Verifikasi ketujuh kolom Hideable checked dan enabled
7. Verifikasi ketujuh kolom memiliki drag handle
8. Verifikasi item `Setup Column...` tersedia di overlay

### TC-GS-USER-536: Screening Popup Setup Column

9. Klik item `Setup Column...` pada overlay
10. Verifikasi bagian Header: Title `Setup Column`
11. Verifikasi bagian Header: deskripsi panduan tampil
12. Verifikasi bagian Header: icon `[✕]`
13. Verifikasi bagian Body: daftar kolom dengan checkbox
14. Verifikasi bagian Body: drag handle pada tiap kolom
15. Verifikasi bagian Body: icon Pin pada tiap kolom
16. Verifikasi bagian Body: preview tabel
17. Verifikasi bagian Footer: `[Reset to Default]` dan `[Save]`
18. Verifikasi bagian Footer: tidak ada `[Cancel]`

### TC-GS-USER-542: Guard satu kolom tersisa tidak bisa di-uncheck

19. Hilangkan centang enam kolom `Action`, `Role`, `Field`, `Old Value`, `New Value`, dan `Modified By` (tersisa `Date`)
20. Hover checkbox `Date`
21. Verifikasi checkbox `Date` tetap tampil
22. Verifikasi checkbox `Date` disabled
23. Verifikasi Tooltip `At least one column must remain visible.`
24. Klik `[✕]` untuk menutup popup tanpa menyimpan

### TC-GS-USER-543: Maksimal 3 kolom di-pin

25. Klik header (⋯), klik `Setup Column...`, lalu klik Pin pada kolom `Date`, `Action`, dan `Role`
26. Verifikasi ketiga kolom `Date`, `Action`, dan `Role` berstatus pinned pada popup
27. Hover icon Pin kolom keempat (`Field`)
28. Verifikasi icon Pin kolom `Field` disabled
29. Verifikasi Tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`

### TC-GS-USER-541: Tutup Setup Column via [✕] membuang perubahan

30. Hilangkan centang `Field` pada popup yang sama
31. Verifikasi preview tabel pada popup tidak memuat kolom `Field`
32. Klik `[✕]`
33. Verifikasi tabel Changelog kembali ke konfigurasi tersimpan terakhir (7 kolom `Date | Action | Role | Field | Old Value | New Value | Modified By` tampil, tanpa pin)

### TC-GS-USER-537: Setup Column hide dan unhide kelas Hideable

34. Klik header (⋯), klik `Setup Column...`, hilangkan centang `Date`
35. Verifikasi Date: preview tabel pada popup tidak memuat kolom `Date`
36. Klik `[Save]`
37. Verifikasi Date: kolom `Date` tidak tampil di tabel Changelog (tersimpan setelah Save)
38. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
39. Verifikasi kolom `Action` tampil di tabel setelah F5
40. Verifikasi Date: kolom `Date` tetap tidak tampil setelah F5
41. Klik header (⋯), klik `Setup Column...`, centang kembali `Date`, lalu klik `[Save]`
42. Klik header (⋯), klik `Setup Column...`, hilangkan centang `Action`
43. Verifikasi Action: preview tabel pada popup tidak memuat kolom `Action`
44. Klik `[Save]`
45. Verifikasi Action: kolom `Action` tidak tampil di tabel Changelog (tersimpan setelah Save)
46. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
47. Verifikasi kolom `Date` tampil di tabel setelah F5
48. Verifikasi Action: kolom `Action` tetap tidak tampil setelah F5
49. Klik header (⋯), klik `Setup Column...`, centang kembali `Action`, lalu klik `[Save]`
50. Klik header (⋯), klik `Setup Column...`, hilangkan centang `Role`
51. Verifikasi Role: preview tabel pada popup tidak memuat kolom `Role`
52. Klik `[Save]`
53. Verifikasi Role: kolom `Role` tidak tampil di tabel Changelog (tersimpan setelah Save)
54. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
55. Verifikasi kolom `Date` tampil di tabel setelah F5
56. Verifikasi Role: kolom `Role` tetap tidak tampil setelah F5
57. Klik header (⋯), klik `Setup Column...`, centang kembali `Role`, lalu klik `[Save]`
58. Klik header (⋯), klik `Setup Column...`, hilangkan centang `Field`
59. Verifikasi Field: preview tabel pada popup tidak memuat kolom `Field`
60. Klik `[Save]`
61. Verifikasi Field: kolom `Field` tidak tampil di tabel Changelog (tersimpan setelah Save)
62. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
63. Verifikasi kolom `Date` tampil di tabel setelah F5
64. Verifikasi Field: kolom `Field` tetap tidak tampil setelah F5
65. Klik header (⋯), klik `Setup Column...`, centang kembali `Field`, lalu klik `[Save]`
66. Klik header (⋯), klik `Setup Column...`, hilangkan centang `Old Value`
67. Verifikasi Old Value: preview tabel pada popup tidak memuat kolom `Old Value`
68. Klik `[Save]`
69. Verifikasi Old Value: kolom `Old Value` tidak tampil di tabel Changelog (tersimpan setelah Save)
70. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
71. Verifikasi kolom `Date` tampil di tabel setelah F5
72. Verifikasi Old Value: kolom `Old Value` tetap tidak tampil setelah F5
73. Klik header (⋯), klik `Setup Column...`, centang kembali `Old Value`, lalu klik `[Save]`
74. Klik header (⋯), klik `Setup Column...`, hilangkan centang `New Value`
75. Verifikasi New Value: preview tabel pada popup tidak memuat kolom `New Value`
76. Klik `[Save]`
77. Verifikasi New Value: kolom `New Value` tidak tampil di tabel Changelog (tersimpan setelah Save)
78. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
79. Verifikasi kolom `Date` tampil di tabel setelah F5
80. Verifikasi New Value: kolom `New Value` tetap tidak tampil setelah F5
81. Klik header (⋯), klik `Setup Column...`, centang kembali `New Value`, lalu klik `[Save]`
82. Klik header (⋯), klik `Setup Column...`, hilangkan centang `Modified By`
83. Verifikasi Modified By: preview tabel pada popup tidak memuat kolom `Modified By`
84. Klik `[Save]`
85. Verifikasi Modified By: kolom `Modified By` tidak tampil di tabel Changelog (tersimpan setelah Save)
86. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
87. Verifikasi kolom `Date` tampil di tabel setelah F5
88. Verifikasi Modified By: kolom `Modified By` tetap tidak tampil setelah F5
89. Klik header (⋯), klik `Setup Column...`, centang kembali `Modified By`, lalu klik `[Save]`

### TC-GS-USER-538: Setup Column drag reorder kelas Hideable

90. Klik header (⋯), klik `Setup Column...`, geser kolom `Date` ke posisi terakhir
91. Verifikasi Date: preview tabel pada popup menampilkan `Date` di posisi terakhir
92. Klik `[Save]`
93. Verifikasi Date: kolom `Date` di posisi terakhir tabel Changelog (tersimpan setelah Save)
94. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
95. Verifikasi Date: kolom `Date` tetap di posisi terakhir setelah F5
96. Klik header (⋯), klik `Setup Column...`, geser kolom `Action` ke posisi pertama
97. Verifikasi Action: preview tabel pada popup menampilkan `Action` di posisi pertama
98. Klik `[Save]`
99. Verifikasi Action: kolom `Action` di posisi pertama tabel Changelog (tersimpan setelah Save)
100. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
101. Verifikasi Action: kolom `Action` tetap di posisi pertama setelah F5
102. Klik header (⋯), klik `Setup Column...`, geser kolom `Role` ke posisi pertama
103. Verifikasi Role: preview tabel pada popup menampilkan `Role` di posisi pertama
104. Klik `[Save]`
105. Verifikasi Role: kolom `Role` di posisi pertama tabel Changelog (tersimpan setelah Save)
106. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
107. Verifikasi Role: kolom `Role` tetap di posisi pertama setelah F5
108. Klik header (⋯), klik `Setup Column...`, geser kolom `Field` ke posisi pertama
109. Verifikasi Field: preview tabel pada popup menampilkan `Field` di posisi pertama
110. Klik `[Save]`
111. Verifikasi Field: kolom `Field` di posisi pertama tabel Changelog (tersimpan setelah Save)
112. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
113. Verifikasi Field: kolom `Field` tetap di posisi pertama setelah F5
114. Klik header (⋯), klik `Setup Column...`, geser kolom `Old Value` ke posisi pertama
115. Verifikasi Old Value: preview tabel pada popup menampilkan `Old Value` di posisi pertama
116. Klik `[Save]`
117. Verifikasi Old Value: kolom `Old Value` di posisi pertama tabel Changelog (tersimpan setelah Save)
118. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
119. Verifikasi Old Value: kolom `Old Value` tetap di posisi pertama setelah F5
120. Klik header (⋯), klik `Setup Column...`, geser kolom `New Value` ke posisi pertama
121. Verifikasi New Value: preview tabel pada popup menampilkan `New Value` di posisi pertama
122. Klik `[Save]`
123. Verifikasi New Value: kolom `New Value` di posisi pertama tabel Changelog (tersimpan setelah Save)
124. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
125. Verifikasi New Value: kolom `New Value` tetap di posisi pertama setelah F5
126. Klik header (⋯), klik `Setup Column...`, geser kolom `Modified By` ke posisi pertama
127. Verifikasi Modified By: preview tabel pada popup menampilkan `Modified By` di posisi pertama
128. Klik `[Save]`
129. Verifikasi Modified By: kolom `Modified By` di posisi pertama tabel Changelog (tersimpan setelah Save)
130. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
131. Verifikasi Modified By: kolom `Modified By` tetap di posisi pertama setelah F5

### TC-GS-USER-539: Setup Column pin dan unpin kelas Hideable

132. Perkecil lebar viewport hingga tabel Changelog dapat di-scroll horizontal
133. Klik header (⋯), klik `Setup Column...`, klik Pin pada kolom `Date`
134. Verifikasi Date: preview tabel pada popup menampilkan `Date` berstatus pinned
135. Klik `[Save]`
136. Verifikasi Date: kolom `Date` berstatus pinned di tabel Changelog (tersimpan setelah Save)
137. Scroll horizontal tabel Changelog
138. Verifikasi Date: kolom `Date` tetap terlihat saat scroll horizontal (kolom beku)
139. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
140. Verifikasi Date: kolom `Date` tetap berstatus pinned setelah F5
141. Klik header (⋯), klik `Setup Column...`, klik Unpin pada kolom `Date`, lalu klik `[Save]`
142. Klik header (⋯), klik `Setup Column...`, klik Pin pada kolom `Action`
143. Verifikasi Action: preview tabel pada popup menampilkan `Action` berstatus pinned
144. Klik `[Save]`
145. Verifikasi Action: kolom `Action` berstatus pinned di tabel Changelog (tersimpan setelah Save)
146. Scroll horizontal tabel Changelog
147. Verifikasi Action: kolom `Action` tetap terlihat saat scroll horizontal (kolom beku)
148. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
149. Verifikasi Action: kolom `Action` tetap berstatus pinned setelah F5
150. Klik header (⋯), klik `Setup Column...`, klik Unpin pada kolom `Action`, lalu klik `[Save]`
151. Klik header (⋯), klik `Setup Column...`, klik Pin pada kolom `Role`
152. Verifikasi Role: preview tabel pada popup menampilkan `Role` berstatus pinned
153. Klik `[Save]`
154. Verifikasi Role: kolom `Role` berstatus pinned di tabel Changelog (tersimpan setelah Save)
155. Scroll horizontal tabel Changelog
156. Verifikasi Role: kolom `Role` tetap terlihat saat scroll horizontal (kolom beku)
157. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
158. Verifikasi Role: kolom `Role` tetap berstatus pinned setelah F5
159. Klik header (⋯), klik `Setup Column...`, klik Unpin pada kolom `Role`, lalu klik `[Save]`
160. Klik header (⋯), klik `Setup Column...`, klik Pin pada kolom `Field`
161. Verifikasi Field: preview tabel pada popup menampilkan `Field` berstatus pinned
162. Klik `[Save]`
163. Verifikasi Field: kolom `Field` berstatus pinned di tabel Changelog (tersimpan setelah Save)
164. Scroll horizontal tabel Changelog
165. Verifikasi Field: kolom `Field` tetap terlihat saat scroll horizontal (kolom beku)
166. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
167. Verifikasi Field: kolom `Field` tetap berstatus pinned setelah F5
168. Klik header (⋯), klik `Setup Column...`, klik Unpin pada kolom `Field`, lalu klik `[Save]`
169. Klik header (⋯), klik `Setup Column...`, klik Pin pada kolom `Old Value`
170. Verifikasi Old Value: preview tabel pada popup menampilkan `Old Value` berstatus pinned
171. Klik `[Save]`
172. Verifikasi Old Value: kolom `Old Value` berstatus pinned di tabel Changelog (tersimpan setelah Save)
173. Scroll horizontal tabel Changelog
174. Verifikasi Old Value: kolom `Old Value` tetap terlihat saat scroll horizontal (kolom beku)
175. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
176. Verifikasi Old Value: kolom `Old Value` tetap berstatus pinned setelah F5
177. Klik header (⋯), klik `Setup Column...`, klik Unpin pada kolom `Old Value`, lalu klik `[Save]`
178. Klik header (⋯), klik `Setup Column...`, klik Pin pada kolom `New Value`
179. Verifikasi New Value: preview tabel pada popup menampilkan `New Value` berstatus pinned
180. Klik `[Save]`
181. Verifikasi New Value: kolom `New Value` berstatus pinned di tabel Changelog (tersimpan setelah Save)
182. Scroll horizontal tabel Changelog
183. Verifikasi New Value: kolom `New Value` tetap terlihat saat scroll horizontal (kolom beku)
184. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
185. Verifikasi New Value: kolom `New Value` tetap berstatus pinned setelah F5
186. Klik header (⋯), klik `Setup Column...`, klik Unpin pada kolom `New Value`, lalu klik `[Save]`
187. Klik header (⋯), klik `Setup Column...`, klik Pin pada kolom `Modified By`
188. Verifikasi Modified By: preview tabel pada popup menampilkan `Modified By` berstatus pinned
189. Klik `[Save]`
190. Verifikasi Modified By: kolom `Modified By` berstatus pinned di tabel Changelog (tersimpan setelah Save)
191. Scroll horizontal tabel Changelog
192. Verifikasi Modified By: kolom `Modified By` tetap terlihat saat scroll horizontal (kolom beku)
193. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
194. Verifikasi Modified By: kolom `Modified By` tetap berstatus pinned setelah F5
195. Klik header (⋯), klik `Setup Column...`, klik Unpin pada kolom `Modified By`, lalu klik `[Save]`
196. Pulihkan lebar viewport ke ukuran semula

### TC-GS-USER-540: Setup Column Reset to Default

197. Klik header (⋯), klik `Setup Column...`, geser kolom `Modified By` ke posisi pertama, hilangkan centang `Role`, lalu klik `[Save]`
198. Verifikasi tabel Changelog menampilkan kolom `Modified By` di posisi pertama
199. Verifikasi tabel Changelog tidak menampilkan kolom `Role`
200. Klik header (⋯), klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`
201. Verifikasi susunan kolom kembali default (`Date | Action | Role | Field | Old Value | New Value | Modified By`)
202. Muat ulang halaman (F5), lalu buka kembali Modal Changelog (Klik Name `Ahmad Fauzi {runId}-088`, Tab `Role`, icon Changelog)
203. Verifikasi susunan kolom default bertahan setelah F5

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Modal Changelog Role dibuka di langkah 1 sampai 3 dan dibuka kembali sesudah tiap muat ulang halaman (F5 menutup modal); pembukaan ulang itu tidak dihitung dalam batas langkah.
- Urutan TC dalam spec: TC-GS-USER-535, 536, 542, 543, 541, 537, 538, 539, 540. Alasan: dua TC screening (535, 536) di awal; TC-GS-USER-542 (guard), 543 (batas pin), dan 541 (`[✕]` membuang perubahan) tidak menyimpan konfigurasi sehingga mendahului TC yang menyimpan (bagian 3 konvensi); TC-GS-USER-537, 538, 539 menyimpan konfigurasi; TC-GS-USER-540 (Reset to Default) terakhir karena mengembalikan susunan ke default. TC-GS-USER-542, 543, dan 541 memakai popup Setup Column yang sama: popup dibuka di langkah 9 (TC-GS-USER-536), ditutup di langkah 24 dan dibuka lagi di langkah 25, dan perubahan pin langkah 25 dibuang bersama perubahan langkah 30 oleh `[✕]` di langkah 32.
- Pada TC-GS-USER-538 reorder berlaku kumulatif: tiap geser dikerjakan di atas urutan hasil geser sebelumnya, tanpa memulihkan urutan sebelumnya. Urutan kolom diuji `Date` (digeser ke posisi terakhir, sesuai langkah TC), lalu `Action`, `Role`, `Field`, `Old Value`, `New Value`, dan `Modified By` (digeser ke posisi pertama). Sesudah `Date` di posisi terakhir, `Action` sudah berada di posisi pertama sehingga langkah TC untuk `Action` tidak mengubah urutan (lihat Temuan untuk QA). Urutan susunan akhir dipulihkan di TC-GS-USER-540 (langkah 200 sampai 203).
- Pada TC-GS-USER-537 dan 539 TC menulis "uncheck lalu check" dan "Pin ... lalu Unpin" sebelum atau sesudah `[Save]` dan F5; spec membaca urutannya sebagai ubah (hide atau Pin), `[Save]`, muat ulang halaman, lalu pulihkan (centang kembali atau Unpin, `[Save]`), sehingga tiap kolom dimulai dari default. Butir Expected "tampil di preview, tersimpan setelah Save, dan bertahan setelah F5" menjadi tiga `Verifikasi` per kolom (preview, setelah Save, setelah F5), dan "kolom beku saat scroll horizontal" menjadi `Verifikasi` keempat pada TC-GS-USER-539.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 24 (menutup popup tanpa menyimpan), langkah pemulihan di akhir tiap kolom TC-GS-USER-537 (centang kembali dan `[Save]`) dan TC-GS-USER-539 (Unpin dan `[Save]`), langkah scroll horizontal pada TC-GS-USER-539, serta langkah "Muat ulang halaman (F5), lalu buka kembali Modal Changelog" yang memenuhi langkah "refresh F5" di TC.
- Anchor positif tambahan (S-03, bagian 8b butir 2): sebelum tiap `Verifikasi` kolom hide `tetap tidak tampil setelah F5` ditaruh `Verifikasi` kolom lain tampil setelah F5 (`Action` untuk `Date`, `Date` untuk kolom lain). Pada TC-GS-USER-540, langkah 198 (kolom `Modified By` di posisi pertama) dan langkah 199 (kolom `Role` tidak tampil) mengamati perubahan sebelum reset agar reset tidak lulus pada konfigurasi yang tidak berubah. Langkah memperkecil viewport sebelum Pin pertama dan memulihkannya sesudah Unpin terakhir adalah langkah penghubung TC-GS-USER-539 (langkah scroll horizontal).
- Langkah 26 dan 31 adalah anchor positif untuk asersi berikutnya (pin pada tiga kolom berhasil sebelum Pin keempat disabled; perubahan centang terlihat sebelum `[✕]` membuangnya; S-03). Langkah 33 mengasersi konfigurasi tersimpan terakhir sebagai default (7 kolom, tanpa pin) karena hook `before` mengosongkan konfigurasi.
- Spec melewati sekitar 35 langkah (203 langkah; sekitar 181 tanpa pembukaan ulang modal sesudah F5) karena tujuh kolom Hideable pada TC-GS-USER-537, 538, dan 539 masing-masing menjadi blok sendiri sesuai butir Expected a sampai g (S-01) dengan tiga sampai empat `Verifikasi` per kolom. Semua blok satu kelas harness (Setup Column tabel Modal Changelog Role), satu layar, satu akun, dan satu dataset; tiap blok kolom berdiri sendiri karena konfigurasi dipulihkan ke default di akhir blok (centang kembali atau Unpin), sehingga kegagalan satu kolom tidak membuat kolom lain kehilangan makna; modal dan popup memakai pembukaan yang sama.
- Pembagian TC Setup Column: pengaruh kolom hidden pada Search (TC-GS-USER-516), Filter (TC-GS-USER-530), dan Download (TC-GS-USER-547) diverifikasi di spec 084, 086, dan 089.
- Temuan untuk QA: (1) TC-GS-USER-535 Expected b menyebut "kolom Curated unchecked & enabled", tetapi PRD user.md §4.1.9 menetapkan ketujuh kolom Hideable (tidak ada kolom Curated); spec hanya mengasersi kolom Hideable. (2) TC-GS-USER-535 menyebut header "Actions (⋯)" sedangkan TC-GS-USER-510 menyebut `Column Visibility (⋯)`; spec memakai `Column Visibility (⋯)`. (3) TC-GS-USER-536 menyebut "deskripsi panduan" tanpa teks; spec hanya mengasersi deskripsi tampil. (4) TC-GS-USER-537, 538, dan 539 "uncheck lalu check" dan "Pin ... lalu Unpin" ambigu terhadap urutan Save dan F5; spec menulis penafsiran di Notes. (5) TC-GS-USER-538 menggeser `Date` ke posisi terakhir, lalu `Action` ke posisi pertama padahal `Action` sudah pertama sesudah `Date` dipindah; Expected tidak membedakannya dari kolom lain. (6) TC-GS-USER-539 "scroll horizontal" tidak menyebut lebar viewport; kemampuan mempersempit viewport diminta dari tim FE. (7) TC-GS-USER-542 dan 543 tidak menyebut apakah uji dilakukan di overlay atau popup; spec memakai popup Setup Column. (8) TC-GS-USER-535 sampai 543 menyebut `Ahmad Fauzi` tanpa suffix; spec memakai user seed bersuffix.

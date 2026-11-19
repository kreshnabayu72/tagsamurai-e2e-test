---
id: TC-FA-FASVC-UI-050-form-mekanik-dialog-dan-feedback
title: "Form: Saving, Tutup dan Unsaved Changes, Clear Field, Stay on this form, Toast, dan 5xx"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-FASVC-02", "FI-FASVC-04", "FI-FASVC-06", "FI-FASVC-07", "FI-FASVC-14", "FI-FASVC-15", "FI-FASVC-16", "FI-FASVC-17", "D-FASVC-01", "D-FASVC-02", "DO-FASVC-01", "EC-FASVC-32", "EC-FASVC-33a", "EC-FASVC-33b", "EC-FASVC-36a", "EC-FASVC-36b", "F-FASVC-02.k10", "F-FASVC-02.k11", "F-FASVC-02.k12", "RS-FASVC-01d", "RS-FASVC-01e", "RS-FASVC-01f", "RS-FASVC-02b", "RS-FASVC-02c", "RS-FASVC-02d", "RS-FASVC-02e", "TS-FASVC-01", "TS-FASVC-02", "TS-FASVC-07", "§4.2.2#b11", "§9.9#p1", "EB-FB-1@create-service-center", "EB-FB-1@edit-service-center", "EB-FB-3@form-edit-service-center", "EB-FB-4", "EB-FRM-1@form-create-service-center", "EB-FRM-1@form-edit-service-center", "EB-FRM-2@form-create-service-center", "EB-FRM-2@form-edit-service-center", "EB-FRM-3@form-create-service-center", "EB-FRM-3@form-edit-service-center", "EB-FRM-7@form-create-service-center", "EB-FRM-7@form-edit-service-center", "EB-ERR-1@create-service-center", "EB-ERR-1@edit-service-center", "§4.4#r4"]
smoke: []
dependsOn: []
trace:
  "FI-FASVC-02": [9, 15, 21, 34, 39, 48, 225]
  "FI-FASVC-04": [57, 69]
  "FI-FASVC-06": [125, 126, 127, 128, 130, 138, 139, 302, 303, 311, 317, 318, 319, 305, 313]
  "FI-FASVC-07": [129, 140, 304, 312]
  "FI-FASVC-14": [150, 151, 323, 324, 340, 341, 344, 345, 349, 350]
  "FI-FASVC-15": [88]
  "FI-FASVC-16": [89, 91, 92, 94]
  "FI-FASVC-17": [90]
  "D-FASVC-01": [2, 43]
  "D-FASVC-02": [15, 16, 17, 34]
  "DO-FASVC-01": [15, 16, 30, 34, 41]
  "EC-FASVC-32": [15, 21, 34, 39]
  "EC-FASVC-33a": [144, 150]
  "EC-FASVC-33b": [145, 151]
  "EC-FASVC-36a": [159, 160, 177, 178, 187, 188, 197, 198, 369]
  "EC-FASVC-36b": [158, 176, 186, 196, 368]
  "F-FASVC-02.k10": [144, 145]
  "F-FASVC-02.k11": [15, 19, 21, 34, 39]
  "F-FASVC-02.k12": [158, 176, 186, 196]
  "RS-FASVC-01d": [158, 176, 368]
  "RS-FASVC-01e": [159, 177, 369]
  "RS-FASVC-01f": [160, 178]
  "RS-FASVC-02b": [144]
  "RS-FASVC-02c": [146]
  "RS-FASVC-02d": [146]
  "RS-FASVC-02e": [145]
  "TS-FASVC-01": [63, 88, 158]
  "TS-FASVC-02": [75, 186]
  "TS-FASVC-07": [145]
  "§4.2.2#b11": [15, 21, 34, 39]
  "§9.9#p1": [125, 138]
  "EB-FB-1@create-service-center": [63]
  "EB-FB-1@edit-service-center": [75]
  "EB-FB-3@form-edit-service-center": [145]
  "EB-FB-4": [65, 164, 166]
  "EB-FRM-1@form-create-service-center": [57, 58, 60, 62, 211]
  "EB-FRM-1@form-edit-service-center": [69, 70, 72, 74, 217]
  "EB-FRM-2@form-create-service-center": [9, 10, 15, 19, 23, 24, 26, 27, 30]
  "EB-FRM-2@form-edit-service-center": [34, 36, 37, 41, 48, 49, 221, 222, 225, 226]
  "EB-FRM-3@form-create-service-center": [102, 104, 105, 106, 107, 108, 109, 110, 111, 133, 134, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 356]
  "EB-FRM-3@form-edit-service-center": [113, 115, 116, 117, 118, 119, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 361]
  "EB-FRM-7@form-create-service-center": [3, 5, 6, 7, 11, 131, 289, 291]
  "EB-FRM-7@form-edit-service-center": [44, 45, 46, 50, 141, 294, 295, 296]
  "EB-ERR-1@create-service-center": [158, 159, 160, 161, 162, 168, 169, 176, 177, 178, 179, 181, 182]
  "EB-ERR-1@edit-service-center": [186, 187, 188, 189, 191, 192, 196, 197, 198, 199, 201, 202, 231, 236, 230, 235]
  "§4.4#r4": [125, 126, 127, 128, 129, 138, 139, 140, 302, 303, 304, 311, 312, 317, 318, 319]
anchor: [353, 355, 358, 360]
coverage:
  web: automated
---

# Form: Saving, Tutup dan Unsaved Changes, Clear Field, Stay on this form, Toast, dan 5xx

## Prerequisites
- Aktor: Total Control.
- Layar awal: dialog Create / Edit Service Center yang ditampilkan menurut kondisi di bawah, dibuka dari tombol pemicu dialog.
- Komponen: Dialog Create / Edit Service Center
- Data:
  - DU-050-1: pohon Group cakupan Total Control: root `All groups`, anak `Head Office`, cucu `Branch Surabaya`.
  - DU-050-2: Negara company pada General Settings `Indonesia`, dan `Malaysia` ada pada daftar negara.
  - DU-050-3: input Create valid: Name `Bengkel Mitra Jaya {runId}`, Service type `Routine`, City `Cimahi`, Company email `kontak@mitrajaya-cimahi.co.id`, dengan Available to dan Country memakai nilai awal.
  - DU-050-4: Service Center untuk Edit: Name `CV Genset Prima`, Service type `Routine`, Available to `Branch Surabaya`, Country `Indonesia`, Province / State `Jawa Timur`, City `Surabaya`, Company email `servis@gensetprima-sby.co.id`, Contact persons 0 baris, field lain kosong. Nilai pada langkah: Notes `Vendor genset untuk cabang Surabaya`, dan Name `cv genset prima` yang hanya beda kapital dari Name tersimpan.
  - DU-050-5: Service Center untuk Edit dengan data lengkap: Name `PT Pendingin Sentosa`, Service type `Routine`, Available to `Branch Surabaya`, Specialization `AC`, Brands `Daikin`, Country `Indonesia`, Province / State `Jawa Timur`, City `Surabaya`, Postal code `60175`, Address line `Jl. Darmo Permai No. 8`, Company phone dengan Dial Code `+62` dan nomor `315550199`, Company email `info@pendingin-sentosa.co.id`, Contact persons 2 baris (baris ke-1 Primary: Name `Rina Wijaya`, Phone nomor `85612340001`, Email `rina@pendingin-sentosa.co.id`; baris ke-2: Name `Joko Prasetyo`, Email `joko@pendingin-sentosa.co.id`), Notes `Vendor AC gedung kantor Surabaya`, Attachments `kontrak-pendingin-sentosa.pdf`.
  - DU-050-6: pohon Category: `Cooling` dengan anak `AC` dan `Refrigeration`.
  - DU-050-7: master Brand: `Daikin` dan `Panasonic`, keduanya Active.
  - DU-050-8: input Create lengkap: Name `Bengkel Lengkap Sejahtera {runId}`, Service type `Routine`, Available to `Branch Surabaya`, Specialization `AC`, Brands `Daikin`, Country `Malaysia`, Province / State `Selangor`, City `Shah Alam`, Postal code `40150`, Address line `Jl. Persiaran Kerjaya No. 5`, Company phone dengan Dial Code `+60` dan nomor `355550123`, Company email `info@lengkapsejahtera.co.id`, Contact persons 1 baris dengan Name `Ahmad Fauzi`, Notes `Vendor lengkap untuk uji Clear Field`.
  - DU-050-9: berkas lampiran untuk Create: `kontrak-mitra-jaya.pdf`.
- Kondisi:
  - K1: dialog Create dibuka oleh Total Control; pohon Group DU-050-1 dan Negara company DU-050-2; permintaan simpan dijawab sukses.
  - K2: seperti K1, dan jawaban permintaan simpan ditahan sampai langkah menjawabnya.
  - K3: seperti K1, dan permintaan simpan pertama dijawab gagal karena error server, permintaan berikutnya dijawab sukses.
  - K4: seperti K1, dan permintaan simpan pertama gagal karena timeout, permintaan berikutnya dijawab sukses.
  - K5: dialog Edit untuk Service Center DU-050-4 dibuka oleh Total Control; pohon Group DU-050-1 dan Negara company DU-050-2; permintaan simpan dijawab sukses.
  - K6: seperti K5, dan jawaban permintaan simpan ditahan sampai langkah menjawabnya.
  - K7: seperti K5, dan permintaan simpan pertama dijawab gagal karena error server, permintaan berikutnya dijawab sukses.
  - K8: seperti K5, dan permintaan simpan pertama gagal karena timeout, permintaan berikutnya dijawab sukses.
  - K9: seperti K5, dan permintaan simpan dijawab sukses tanpa perubahan nilai.
  - K10: dialog Edit untuk Service Center DU-050-5 dibuka oleh Total Control; pohon Group DU-050-1, pohon Category DU-050-6, master Brand DU-050-7, dan Negara company DU-050-2; permintaan simpan dijawab sukses.
  - K11: seperti K1, dan pohon Category DU-050-6 serta master Brand DU-050-7.
  - K12: seperti K10, dan permintaan simpan dijawab sukses tanpa perubahan nilai.
  - K13: seperti K1, dan permintaan simpan pertama tidak mendapat respons sama sekali, permintaan berikutnya dijawab sukses.

## Test Steps

### Dialog Create bersih: aksesibilitas dan tutup dengan Esc
1. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
2. Verifikasi tombol utama dialog Create berlabel `[Submit]`
3. Verifikasi fokus berada di dalam dialog Create
4. Tekan `Shift+Tab` dari elemen yang sedang fokus
5. Verifikasi fokus tetap berada di dalam dialog Create
6. Verifikasi field `Name` ditandai wajib untuk teknologi bantu (`aria-required`)
7. Verifikasi tombol `✕` memiliki label aksesibel `Close dialog`
8. Tekan `Esc`
9. Verifikasi dialog Create tertutup
10. Verifikasi dialog `Unsaved Changes` tidak tampil
11. Verifikasi fokus kembali ke tombol pemicu dialog

### Menutup dialog Create dengan isian berubah memunculkan Unsaved Changes
12. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
13. Isi Name `Bengkel Mitra Jaya {runId}`
14. Klik `✕` pada dialog Create
15. Verifikasi dialog `Unsaved Changes` tampil
16. Verifikasi dialog `Unsaved Changes` memuat pesan `You have unsaved changes. Are you sure you want to leave?`
17. Verifikasi dialog `Unsaved Changes` memuat tombol `[Cancel]` dan tombol `[Leave]`
18. Klik `[Cancel]` pada dialog `Unsaved Changes`
19. Verifikasi dialog Create masih terbuka dengan field `Name` berisi `Bengkel Mitra Jaya {runId}`
20. Tekan `Esc`
21. Verifikasi dialog `Unsaved Changes` tampil
22. Tekan `Esc` pada dialog `Unsaved Changes`
23. Verifikasi dialog Create masih terbuka dengan field `Name` berisi `Bengkel Mitra Jaya {runId}`
24. Verifikasi dialog `Unsaved Changes` tidak tampil
25. Klik area di luar dialog Create
26. Verifikasi dialog Create masih terbuka dengan field `Name` berisi `Bengkel Mitra Jaya {runId}`
27. Verifikasi dialog `Unsaved Changes` tidak tampil
28. Klik `✕` pada dialog Create
29. Klik `[Leave]` pada dialog `Unsaved Changes`
30. Verifikasi dialog Create tertutup

### Menutup dialog Edit dengan isian berubah memunculkan Unsaved Changes
31. Tampilkan Dialog Create / Edit Service Center dengan kondisi K5
32. Isi Notes `Vendor genset untuk cabang Surabaya`
33. Klik `✕` pada dialog Edit
34. Verifikasi dialog `Unsaved Changes` tampil
35. Tekan `Esc` pada dialog `Unsaved Changes`
36. Verifikasi dialog Edit masih terbuka dengan field `Notes` berisi `Vendor genset untuk cabang Surabaya`
37. Verifikasi dialog `Unsaved Changes` tidak tampil
38. Tekan `Esc`
39. Verifikasi dialog `Unsaved Changes` tampil
40. Klik `[Leave]` pada dialog `Unsaved Changes`
41. Verifikasi dialog Edit tertutup

### Dialog Edit bersih: aksesibilitas dan tutup dengan Esc
42. Tampilkan Dialog Create / Edit Service Center dengan kondisi K5
43. Verifikasi tombol utama dialog Edit berlabel `[Save]`
44. Verifikasi fokus berada di dalam dialog Edit
45. Verifikasi field `Name` ditandai wajib untuk teknologi bantu (`aria-required`)
46. Verifikasi tombol `✕` memiliki label aksesibel `Close dialog`
47. Tekan `Esc`
48. Verifikasi dialog Edit tertutup
49. Verifikasi dialog `Unsaved Changes` tidak tampil
50. Verifikasi fokus kembali ke tombol pemicu dialog

### Saving Create: tombol dan kontrol terkunci, satu permintaan, toast sukses hilang sendiri
51. Tampilkan Dialog Create / Edit Service Center dengan kondisi K2
52. Isi Name `Bengkel Mitra Jaya {runId}`
53. Centang checkbox `Routine`
54. Isi City `Cimahi`
55. Isi Company email `kontak@mitrajaya-cimahi.co.id`
56. Klik `[Submit]`
57. Verifikasi `[Submit]` tidak bisa diklik selama permintaan berjalan
58. Verifikasi `[Clear Field]`, `✕`, field `Name`, dan checkbox `Routine` disabled selama permintaan berjalan
59. Klik `[Submit]` lagi
60. Verifikasi permintaan simpan yang terkirim berjumlah `1`
61. Respons simpan dijawab sukses
62. Verifikasi dialog Create tertutup
63. Verifikasi toast sukses `Success, Bengkel Mitra Jaya {runId} has been added.` tampil
64. Waktu berlalu sampai 5 detik sejak toast sukses tampil
65. Verifikasi toast sukses `Success, Bengkel Mitra Jaya {runId} has been added.` tidak lagi tampil

### Saving Edit: tombol dan kontrol terkunci, satu permintaan, toast sukses
66. Tampilkan Dialog Create / Edit Service Center dengan kondisi K6
67. Isi Notes `Vendor genset untuk cabang Surabaya`
68. Klik `[Save]`
69. Verifikasi `[Save]` tidak bisa diklik selama permintaan berjalan
70. Verifikasi `[Clear Field]`, `✕`, dan field `Notes` disabled selama permintaan berjalan
71. Klik `[Save]` lagi
72. Verifikasi permintaan simpan yang terkirim berjumlah `1`
73. Respons simpan dijawab sukses
74. Verifikasi dialog Edit tertutup
75. Verifikasi toast sukses `Success, CV Genset Prima has been updated.` tampil

### Create dengan Stay on this form after submitting mengembalikan form ke nilai awal
76. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
77. Isi Name `Bengkel Mitra Jaya {runId}`
78. Centang checkbox `Routine`
79. Isi City `Cimahi`
80. Isi Company email `kontak@mitrajaya-cimahi.co.id`
81. Pilih opsi `Malaysia` pada field `Country`
82. Klik trigger field `Available to`
83. Klik checkbox `All groups` untuk melepas seluruh pilihan
84. Klik checkbox `Branch Surabaya`
85. Klik `[Select]` pada dialog pilihan Available to
86. Centang checkbox `Stay on this form after submitting`
87. Klik `[Submit]`
88. Verifikasi toast sukses `Success, Bengkel Mitra Jaya {runId} has been added.` tampil
89. Verifikasi dialog Create tetap terbuka
90. Verifikasi fokus berada di field `Name`
91. Verifikasi field `Name` menampilkan placeholder `Enter name`
92. Verifikasi field `Country` menampilkan `Indonesia`
93. Klik trigger field `Available to`
94. Verifikasi checkbox `All groups` tercentang
95. Klik `[Cancel]` pada dialog pilihan Available to

### Clear Field pada Create mengosongkan isian tanpa prompt
96. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
97. Isi Name `Bengkel Mitra Jaya {runId}`
98. Centang checkbox `Routine`
99. Isi City `Cimahi`
100. Isi Company email `kontak@mitrajaya-cimahi.co.id`
101. Centang checkbox `Stay on this form after submitting`
102. Verifikasi field `Name` berisi `Bengkel Mitra Jaya {runId}`
103. Klik `[Clear Field]`
104. Verifikasi field `Name` menampilkan placeholder `Enter name`
105. Verifikasi field `City` menampilkan placeholder `Enter city`
106. Verifikasi field `Company email` menampilkan placeholder `Enter email`
107. Verifikasi checkbox `Routine` tidak tercentang
108. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
109. Verifikasi dialog Create tetap terbuka
110. Verifikasi dialog `Unsaved Changes` tidak tampil
111. Verifikasi fokus berada di field `Name`

### Clear Field pada Edit mengosongkan isian, bukan mengembalikan nilai tersimpan
112. Tampilkan Dialog Create / Edit Service Center dengan kondisi K5
113. Verifikasi field `Name` berisi `CV Genset Prima`
114. Klik `[Clear Field]`
115. Verifikasi field `Name` menampilkan placeholder `Enter name`
116. Verifikasi field `City` menampilkan placeholder `Enter city`
117. Verifikasi field `Company email` menampilkan placeholder `Enter email`
118. Verifikasi dialog Edit tetap terbuka
119. Verifikasi dialog `Unsaved Changes` tidak tampil

### Submit Create dengan isian tidak valid menandai semua field bermasalah
120. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
121. Klik trigger field `Available to`
122. Klik checkbox `All groups` untuk melepas seluruh pilihan
123. Klik `[Select]` pada dialog pilihan Available to
124. Klik `[Submit]`
125. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name must not be empty`
126. Verifikasi field `Service type` ditandai tidak valid dengan pesan `Select at least one service type`
127. Verifikasi field `Available to` ditandai tidak valid dengan pesan `Select at least one group`
128. Verifikasi field `City` ditandai tidak valid dengan pesan `City must not be empty`
129. Verifikasi fokus berada di field `Name`
130. Verifikasi tidak ada permintaan simpan yang terkirim
131. Verifikasi pesan `Name must not be empty` menjadi deskripsi aksesibel field `Name` (`aria-describedby`)
132. Klik `[Clear Field]`
133. Verifikasi field `Name` menampilkan placeholder `Enter name`
134. Verifikasi pesan `Name must not be empty` tidak tampil

### Save Edit dengan isian tidak valid menandai field bermasalah
135. Tampilkan Dialog Create / Edit Service Center dengan kondisi K5
136. Klik `[Clear Field]`
137. Klik `[Save]`
138. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name must not be empty`
139. Verifikasi field `City` ditandai tidak valid dengan pesan `City must not be empty`
140. Verifikasi fokus berada di field `Name`
141. Verifikasi pesan `Name must not be empty` menjadi deskripsi aksesibel field `Name` (`aria-describedby`)

### Edit tanpa perubahan menutup dialog dengan toast info
142. Tampilkan Dialog Create / Edit Service Center dengan kondisi K9
143. Klik `[Save]`
144. Verifikasi dialog Edit tertutup
145. Verifikasi toast info `No changes to save.` tampil
146. Verifikasi toast `Success, CV Genset Prima has been updated.` tidak tampil

### Edit yang hanya mengubah kapitalisasi diperlakukan sebagai tanpa perubahan
147. Tampilkan Dialog Create / Edit Service Center dengan kondisi K9
148. Ganti isi Name dengan `cv genset prima`
149. Klik `[Save]`
150. Verifikasi dialog Edit tertutup
151. Verifikasi toast info `No changes to save.` tampil

### Create gagal karena error server: dialog tetap terbuka dan retry berhasil
152. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
153. Isi Name `Bengkel Mitra Jaya {runId}`
154. Centang checkbox `Routine`
155. Isi City `Cimahi`
156. Isi Company email `kontak@mitrajaya-cimahi.co.id`
157. Klik `[Submit]`
158. Verifikasi toast error `Error, failed to add service center.` tampil
159. Verifikasi dialog Create tetap terbuka
160. Verifikasi field `Name` berisi `Bengkel Mitra Jaya {runId}` dan field `City` berisi `Cimahi`
161. Verifikasi `[Submit]` dapat diklik kembali
162. Verifikasi toast error tidak memiliki tombol aksi `[Try Again]`
163. Waktu berlalu sampai 30 detik sejak toast error tampil
164. Verifikasi toast error `Error, failed to add service center.` masih tampil
165. Klik tombol tutup pada toast error
166. Verifikasi toast error `Error, failed to add service center.` tidak lagi tampil
167. Klik `[Submit]`
168. Verifikasi toast sukses `Success, Bengkel Mitra Jaya {runId} has been added.` tampil
169. Verifikasi dialog Create tertutup

### Create gagal karena timeout: dialog tetap terbuka dan retry berhasil
170. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
171. Isi Name `Bengkel Mitra Jaya {runId}`
172. Centang checkbox `Routine`
173. Isi City `Cimahi`
174. Isi Company email `kontak@mitrajaya-cimahi.co.id`
175. Klik `[Submit]`
176. Verifikasi toast error `Connection problem. Please try again.` tampil
177. Verifikasi dialog Create tetap terbuka
178. Verifikasi field `Name` berisi `Bengkel Mitra Jaya {runId}` dan field `City` berisi `Cimahi`
179. Verifikasi `[Submit]` dapat diklik kembali
180. Klik `[Submit]`
181. Verifikasi toast sukses `Success, Bengkel Mitra Jaya {runId} has been added.` tampil
182. Verifikasi dialog Create tertutup

### Edit gagal karena error server: dialog tetap terbuka dan retry berhasil
183. Tampilkan Dialog Create / Edit Service Center dengan kondisi K7
184. Isi Notes `Vendor genset untuk cabang Surabaya`
185. Klik `[Save]`
186. Verifikasi toast error `Error, failed to update service center.` tampil
187. Verifikasi dialog Edit tetap terbuka
188. Verifikasi field `Notes` berisi `Vendor genset untuk cabang Surabaya`
189. Verifikasi `[Save]` dapat diklik kembali
190. Klik `[Save]`
191. Verifikasi toast sukses `Success, CV Genset Prima has been updated.` tampil
192. Verifikasi dialog Edit tertutup

### Edit gagal karena timeout: dialog tetap terbuka dan retry berhasil
193. Tampilkan Dialog Create / Edit Service Center dengan kondisi K8
194. Isi Notes `Vendor genset untuk cabang Surabaya`
195. Klik `[Save]`
196. Verifikasi toast error `Connection problem. Please try again.` tampil
197. Verifikasi dialog Edit tetap terbuka
198. Verifikasi field `Notes` berisi `Vendor genset untuk cabang Surabaya`
199. Verifikasi `[Save]` dapat diklik kembali
200. Klik `[Save]`
201. Verifikasi toast sukses `Success, CV Genset Prima has been updated.` tampil
202. Verifikasi dialog Edit tertutup

### Saving Create: toast sukses tampil satu kali
203. Tampilkan Dialog Create / Edit Service Center dengan kondisi K2
204. Isi Name `Bengkel Mitra Jaya {runId}`
205. Centang checkbox `Routine`
206. Isi City `Cimahi`
207. Isi Company email `kontak@mitrajaya-cimahi.co.id`
208. Klik `[Submit]`
209. Klik `[Submit]` lagi
210. Respons simpan dijawab sukses
211. Verifikasi toast sukses `Success, Bengkel Mitra Jaya {runId} has been added.` tampil satu kali

### Saving Edit: toast sukses tampil satu kali
212. Tampilkan Dialog Create / Edit Service Center dengan kondisi K6
213. Isi Notes `Vendor genset untuk cabang Surabaya`
214. Klik `[Save]`
215. Klik `[Save]` lagi
216. Respons simpan dijawab sukses
217. Verifikasi toast sukses `Success, CV Genset Prima has been updated.` tampil satu kali

### Klik di luar dialog Edit dengan isian berubah tidak menutup dan tanpa Unsaved Changes
218. Tampilkan Dialog Create / Edit Service Center dengan kondisi K5
219. Isi Notes `Vendor genset untuk cabang Surabaya`
220. Klik area di luar dialog Edit
221. Verifikasi dialog Edit masih terbuka dengan field `Notes` berisi `Vendor genset untuk cabang Surabaya`
222. Verifikasi dialog `Unsaved Changes` tidak tampil

### Menutup dialog Edit bersih dengan tombol tutup langsung tertutup
223. Tampilkan Dialog Create / Edit Service Center dengan kondisi K5
224. Klik `✕` pada dialog Edit
225. Verifikasi dialog Edit tertutup
226. Verifikasi dialog `Unsaved Changes` tidak tampil

### Edit gagal karena error server: toast error tanpa tombol aksi
227. Tampilkan Dialog Create / Edit Service Center dengan kondisi K7
228. Isi Notes `Vendor genset untuk cabang Surabaya`
229. Klik `[Save]`
230. Verifikasi toast error `Error, failed to update service center.` tampil
231. Verifikasi toast error tidak memiliki tombol aksi `[Try Again]`

### Edit gagal karena timeout: toast error tanpa tombol aksi
232. Tampilkan Dialog Create / Edit Service Center dengan kondisi K8
233. Isi Notes `Vendor genset untuk cabang Surabaya`
234. Klik `[Save]`
235. Verifikasi toast error `Connection problem. Please try again.` tampil
236. Verifikasi toast error tidak memiliki tombol aksi `[Try Again]`

### Clear Field pada Create mengosongkan semua field
237. Tampilkan Dialog Create / Edit Service Center dengan kondisi K11
238. Isi Name `Bengkel Lengkap Sejahtera {runId}`
239. Centang checkbox `Routine`
240. Klik trigger field `Available to`
241. Klik checkbox `All groups` untuk melepas seluruh pilihan
242. Klik checkbox `Branch Surabaya`
243. Klik `[Select]` pada dialog pilihan Available to
244. Klik trigger field `Specialization`
245. Perluas node `Cooling`
246. Klik checkbox `AC`
247. Klik `[Select]` pada dialog pilihan Specialization
248. Klik field `Brands`
249. Klik opsi `Daikin`
250. Tekan `Esc` untuk menutup daftar Brands
251. Pilih opsi `Malaysia` pada field `Country`
252. Isi Province / State `Selangor`
253. Isi City `Shah Alam`
254. Isi Postal code `40150`
255. Isi Address line `Jl. Persiaran Kerjaya No. 5`
256. Isi Company phone dengan Dial Code `+60` dan nomor `355550123`
257. Isi Company email `info@lengkapsejahtera.co.id`
258. Klik `[+ Contact person]`
259. Isi Name pada baris contact person ke-1 dengan `Ahmad Fauzi`
260. Isi Notes `Vendor lengkap untuk uji Clear Field`
261. Klik `[Clear Field]`
262. Verifikasi field `Name` menampilkan placeholder `Enter name`
263. Verifikasi checkbox `Routine` tidak tercentang
264. Verifikasi trigger field `Available to` menampilkan placeholder `Select groups`
265. Verifikasi trigger field `Specialization` menampilkan placeholder `Select categories`
266. Verifikasi trigger field `Brands` menampilkan placeholder `Select brands`
267. Verifikasi field `Country` menampilkan placeholder `Select country`
268. Verifikasi field `Province / State` menampilkan placeholder `Enter province / state`
269. Verifikasi field `City` menampilkan placeholder `Enter city`
270. Verifikasi field `Postal code` menampilkan placeholder `Enter postal code`
271. Verifikasi field `Address line` menampilkan placeholder `Enter address line`
272. Verifikasi field `Company phone` menampilkan placeholder `Enter phone number` dan field `Company email` menampilkan placeholder `Enter email`
273. Verifikasi field `Contact persons` tidak memiliki baris yang berisi isian
274. Verifikasi field `Notes` menampilkan placeholder `Enter notes`

### Clear Field pada Edit mengosongkan semua field termasuk yang bernilai tersimpan
275. Tampilkan Dialog Create / Edit Service Center dengan kondisi K10
276. Klik `[Clear Field]`
277. Verifikasi checkbox `Routine` tidak tercentang
278. Verifikasi trigger field `Available to` menampilkan placeholder `Select groups`
279. Verifikasi trigger field `Specialization` menampilkan placeholder `Select categories`
280. Verifikasi trigger field `Brands` menampilkan placeholder `Select brands`
281. Verifikasi field `Country` menampilkan placeholder `Select country`
282. Verifikasi field `Province / State` menampilkan placeholder `Enter province / state`
283. Verifikasi field `Postal code` menampilkan placeholder `Enter postal code`
284. Verifikasi field `Address line` menampilkan placeholder `Enter address line`
285. Verifikasi field `Company phone` menampilkan placeholder `Enter phone number`
286. Verifikasi field `Contact persons` tidak memiliki baris yang berisi isian
287. Verifikasi field `Notes` menampilkan placeholder `Enter notes`

### Aksesibilitas dialog Create: field wajib lain dan tombol hapus baris contact person
288. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
289. Verifikasi field `Service type`, field `Available to`, field `Country`, dan field `City` ditandai wajib untuk teknologi bantu (`aria-required`)
290. Klik `[+ Contact person]`
291. Verifikasi tombol hapus baris contact person memiliki label aksesibel

### Aksesibilitas dialog Edit: focus trap, field wajib lain, dan tombol hapus baris contact person
292. Tampilkan Dialog Create / Edit Service Center dengan kondisi K10
293. Tekan `Shift+Tab` dari elemen yang sedang fokus
294. Verifikasi fokus tetap berada di dalam dialog Edit
295. Verifikasi field `Service type`, field `Available to`, field `Country`, dan field `City` ditandai wajib untuk teknologi bantu (`aria-required`)
296. Verifikasi tombol hapus baris contact person memiliki label aksesibel

### Submit Create tanpa Company phone dan Company email menandai kedua field dan memfokuskan field pertama yang tidak valid
297. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
298. Isi Name `Bengkel Mitra Jaya {runId}`
299. Centang checkbox `Routine`
300. Isi City `Cimahi`
301. Klik `[Submit]`
302. Verifikasi field `Company phone` ditandai tidak valid dengan pesan `Add a company phone or email`
303. Verifikasi field `Company email` ditandai tidak valid dengan pesan `Add a company phone or email`
304. Verifikasi fokus berada di field `Company phone`
305. Verifikasi tidak ada permintaan simpan yang terkirim

### Submit Create dengan Service type kosong memfokuskan Service type, bukan Name
306. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
307. Isi Name `Bengkel Mitra Jaya {runId}`
308. Isi City `Cimahi`
309. Isi Company email `kontak@mitrajaya-cimahi.co.id`
310. Klik `[Submit]`
311. Verifikasi field `Service type` ditandai tidak valid dengan pesan `Select at least one service type`
312. Verifikasi fokus berada di field `Service type`
313. Verifikasi tidak ada permintaan simpan yang terkirim

### Save Edit sesudah Clear Field menandai Service type dan kontak perusahaan
314. Tampilkan Dialog Create / Edit Service Center dengan kondisi K10
315. Klik `[Clear Field]`
316. Klik `[Save]`
317. Verifikasi field `Service type` ditandai tidak valid dengan pesan `Select at least one service type`
318. Verifikasi field `Company phone` ditandai tidak valid dengan pesan `Add a company phone or email`
319. Verifikasi field `Company email` ditandai tidak valid dengan pesan `Add a company phone or email`

### Edit yang hanya menambah spasi tepi diperlakukan sebagai tanpa perubahan
320. Tampilkan Dialog Create / Edit Service Center dengan kondisi K12
321. Ganti isi Name dengan `PT Pendingin Sentosa` ditambah satu spasi di akhir
322. Klik `[Save]`
323. Verifikasi dialog Edit tertutup
324. Verifikasi toast info `No changes to save.` tampil

### Edit dengan multi-select dipilih ulang bernilai identik diperlakukan sebagai tanpa perubahan
325. Tampilkan Dialog Create / Edit Service Center dengan kondisi K12
326. Klik trigger field `Available to`
327. Klik checkbox `Branch Surabaya` untuk melepasnya
328. Klik checkbox `Branch Surabaya` untuk memilihnya kembali
329. Klik `[Select]` pada dialog pilihan Available to
330. Klik trigger field `Specialization`
331. Perluas node `Cooling`
332. Klik checkbox `AC` untuk melepasnya
333. Klik checkbox `AC` untuk memilihnya kembali
334. Klik `[Select]` pada dialog pilihan Specialization
335. Klik field `Brands`
336. Klik opsi `Daikin` untuk melepasnya
337. Klik opsi `Daikin` untuk memilihnya kembali
338. Tekan `Esc` untuk menutup daftar Brands
339. Klik `[Save]`
340. Verifikasi dialog Edit tertutup
341. Verifikasi toast info `No changes to save.` tampil

### Edit dengan Contact persons dan lampiran identik diperlakukan sebagai tanpa perubahan
342. Tampilkan Dialog Create / Edit Service Center dengan kondisi K12
343. Klik `[Save]`
344. Verifikasi dialog Edit tertutup
345. Verifikasi toast info `No changes to save.` tampil

### Edit yang memindahkan Primary bukan tanpa perubahan
346. Tampilkan Dialog Create / Edit Service Center dengan kondisi K10
347. Klik pilihan Primary pada baris ke-2
348. Klik `[Save]`
349. Verifikasi toast sukses `Success, PT Pendingin Sentosa has been updated.` tampil
350. Verifikasi toast info `No changes to save.` tidak tampil

### Clear Field pada Create mengosongkan lampiran
351. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
352. Pilih berkas `kontrak-mitra-jaya.pdf` pada field `Attachments`
353. Verifikasi field `Attachments` menampilkan berkas `kontrak-mitra-jaya.pdf`
354. Klik `[Clear Field]`
355. Verifikasi field `Name` menampilkan placeholder `Enter name`
356. Verifikasi tidak ada berkas pada field `Attachments`

### Clear Field pada Edit mengosongkan lampiran tersimpan
357. Tampilkan Dialog Create / Edit Service Center dengan kondisi K10
358. Verifikasi field `Attachments` menampilkan berkas `kontrak-pendingin-sentosa.pdf`
359. Klik `[Clear Field]`
360. Verifikasi field `Name` menampilkan placeholder `Enter name`
361. Verifikasi tidak ada berkas pada field `Attachments`

### Create tanpa respons: toast koneksi tampil dan dialog tetap terbuka
362. Tampilkan Dialog Create / Edit Service Center dengan kondisi K13
363. Isi Name `Bengkel Mitra Jaya {runId}`
364. Centang checkbox `Routine`
365. Isi City `Cimahi`
366. Isi Company email `kontak@mitrajaya-cimahi.co.id`
367. Klik `[Submit]`
368. Verifikasi toast error `Connection problem. Please try again.` tampil
369. Verifikasi dialog Create tetap terbuka

---
id: TC-FA-FASVC-UI-055-form-contact-persons
title: "Form: Contact Persons: Tambah, Primary, Hapus, Maks 3, dan Validasi per Baris"
layer: ui-client
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["V-FASVC-06", "V-FASVC-07", "V-FASVC-16", "V-FASVC-18", "FLD-FASVC-13", "FLD-FASVC-14", "FLD-FASVC-15", "FLD-FASVC-16", "S-FASVC-08", "FI-FASVC-11", "FI-FASVC-12", "FI-FASVC-13", "FASVC-LOGIC-02o", "FASVC-LOGIC-02p", "EC-FASVC-54", "EC-FASVC-55", "F-FASVC-02.k16", "EB-FRM-4@contact-name", "EB-FRM-4@contact-email", "EB-FRM-8@contact-persons", "EB-TBL-5@button-add-contact-person", "V-FASVC-36"]
smoke: []
dependsOn: []
trace:
  "V-FASVC-06": [58, 62, 67, 245, 249, 254]
  "V-FASVC-07": [59, 67, 79, 80, 92, 93, 246, 254, 263, 264, 272, 273]
  "V-FASVC-16": [49, 50, 238, 239, 415, 416, 417, 420, 421]
  "V-FASVC-18": [102, 104, 105, 107, 109, 110, 112, 113, 277, 279, 280, 282, 284, 285, 287, 288]
  "FLD-FASVC-13": [2, 10, 34, 49, 215, 216, 222, 230, 238, 364, 366, 370]
  "FLD-FASVC-14": [58, 62, 101, 104, 107, 121, 122, 124, 125, 128, 129, 132, 133, 136, 149, 150, 245, 249, 276, 279, 282, 291, 292, 294, 295, 298, 299, 302, 303, 306, 311, 312, 399, 403]
  "FLD-FASVC-15": [59, 76, 77, 79, 80, 90, 178, 179, 181, 182, 194, 195, 197, 200, 212, 213, 246, 260, 261, 263, 264, 270, 331, 332, 334, 335, 343, 344, 346, 349, 357, 358, 400, 404, 429, 430, 433, 434, 442, 443, 446, 447]
  "FLD-FASVC-16": [59, 89, 92, 93, 160, 163, 164, 166, 169, 246, 269, 272, 273, 317, 320, 321, 323, 326, 401, 405]
  "S-FASVC-08": [32, 34, 35, 37, 39, 228, 230, 231, 233, 235]
  "FI-FASVC-11": [4, 7, 218]
  "FI-FASVC-12": [5, 8, 22, 385]
  "FI-FASVC-13": [24, 26, 224, 387, 390, 396]
  "FASVC-LOGIC-02o": [58, 59, 62, 80, 93, 102, 105, 107, 110, 113, 167, 169, 245, 246, 249, 264, 273, 277, 280, 282, 285, 288, 324, 326]
  "FASVC-LOGIC-02p": [4, 5, 8, 10, 22, 24, 28, 216, 220, 222, 224, 226, 387, 390, 396]
  "EC-FASVC-54": [24, 26, 28, 224, 226, 387, 390, 396]
  "EC-FASVC-55": [364, 366, 370, 372]
  "F-FASVC-02.k16": [24, 26, 28, 224, 226, 366, 370, 372, 387, 390, 396]
  "EB-FRM-4@contact-name": [101, 102, 104, 105, 107, 109, 110, 112, 113, 121, 128, 276, 277, 279, 280, 282, 284, 285, 287, 288, 291, 298]
  "EB-FRM-4@contact-email": [166, 167, 169, 323, 324, 326]
  "EB-FRM-8@contact-persons": [10, 24, 32, 49, 58, 59, 62, 76, 89, 101, 104, 107, 149, 160, 163, 166, 169, 178, 194, 212, 215, 220, 224, 228, 238, 245, 246, 249, 260, 269, 276, 279, 282, 311, 317, 320, 323, 326, 331, 343, 357]
  "EB-TBL-5@button-add-contact-person": [35, 37, 231, 233]
  "V-FASVC-36": [128, 129, 132, 133, 136, 298, 299, 302, 303, 306]
anchor: []
coverage:
  web: automated
---

# Form: Contact Persons: Tambah, Primary, Hapus, Maks 3, dan Validasi per Baris

## Prerequisites
- Aktor: Total Control.
- Layar awal: dialog Create / Edit Service Center yang ditampilkan menurut kondisi di bawah.
- Komponen: Dialog Create / Edit Service Center
- Data:
  - DU-055-1: pohon Group cakupan Total Control: root `All groups`, anak `Head Office`.
  - DU-055-2: daftar kode negara memuat `Indonesia (+62)` dan `Singapore (+65)`.
  - DU-055-3: Service Center untuk Edit: Name `PT Kontak Person Mitra`, Service type `Routine`, Available to `Head Office`, Country `Indonesia`, City `Bandung`, Company email `admin@kontakpic-mitra.co.id`, Contact persons 2 baris: baris pertama Primary dengan Name `Budi Santoso`, Phone nomor `85611110001`, Email `budi@kontakpic-mitra.co.id`; baris kedua Name `Siti Rahma`, tanpa Phone, Email `siti@kontakpic-mitra.co.id`.
  - Nilai pada langkah tercatat di entri data DU-055-4 dan seterusnya.
- Kondisi:
  - K1: dialog Create dibuka oleh Total Control; pohon Group DU-055-1 dan daftar kode negara DU-055-2; permintaan simpan dijawab sukses.
  - K2: seperti K1, dan permintaan simpan ditolak karena Contact persons melebihi 3 baris atau tidak tepat satu Primary.
  - K3: dialog Edit untuk Service Center DU-055-3 dibuka oleh Total Control; pohon Group DU-055-1 dan daftar kode negara DU-055-2; permintaan simpan dijawab sukses.
  - K4: seperti K3, dan permintaan simpan ditolak karena Contact persons melebihi 3 baris atau tidak tepat satu Primary.

## Test Steps

### Tambah baris contact person dan Primary otomatis (Create)
1. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
2. Verifikasi field `Contact persons` tidak memiliki baris
3. Klik `[+ Contact person]`
4. Verifikasi field `Contact persons` memiliki 1 baris
5. Verifikasi baris ke-1 bertanda Primary
6. Klik `[+ Contact person]`
7. Verifikasi field `Contact persons` memiliki 2 baris
8. Verifikasi baris ke-1 bertanda Primary dan baris ke-2 tidak bertanda Primary
9. Klik pilihan Primary pada baris ke-2
10. Verifikasi baris ke-2 bertanda Primary dan baris ke-1 tidak bertanda Primary

### Hapus baris Primary memindahkan Primary (Create)
11. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
12. Isi Name `Bengkel Kontak Person {runId}`
13. Centang checkbox `Routine`
14. Isi City `Banjarmasin`
15. Isi Company email `admin@kontakpic-banjarmasin.co.id`
16. Klik `[+ Contact person]`
17. Klik `[+ Contact person]`
18. Klik `[+ Contact person]`
19. Isi Name pada baris ke-1 `Andi Pratama`
20. Isi Name pada baris ke-2 `Rina Wijaya`
21. Isi Name pada baris ke-3 `Tono Hartono`
22. Verifikasi baris `Andi Pratama` bertanda Primary
23. Klik tombol hapus pada baris `Andi Pratama`
24. Verifikasi baris `Rina Wijaya` bertanda Primary dan field `Contact persons` memiliki 2 baris
25. Klik tombol hapus pada baris `Rina Wijaya`
26. Verifikasi baris `Tono Hartono` bertanda Primary dan field `Contact persons` memiliki 1 baris
27. Klik tombol hapus pada baris `Tono Hartono`
28. Verifikasi field `Contact persons` tidak memiliki baris

### Contact persons maksimal 3 baris (Create)
29. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
30. Klik `[+ Contact person]`
31. Klik `[+ Contact person]`
32. Verifikasi field `Contact persons` memiliki 2 baris dan tombol `[+ Contact person]` dapat diklik
33. Klik `[+ Contact person]`
34. Verifikasi field `Contact persons` memiliki 3 baris
35. Verifikasi tombol `[+ Contact person]` disabled
36. Arahkan kursor ke tombol `[+ Contact person]`
37. Verifikasi alasan `Up to 3 contact persons.` tersampaikan pada tombol `[+ Contact person]` yang disabled
38. Klik tombol hapus pada baris ke-3
39. Verifikasi tombol `[+ Contact person]` dapat diklik kembali

### Contact persons melebihi batas atau tanpa Primary ditolak server saat Save (Create)
40. Tampilkan Dialog Create / Edit Service Center dengan kondisi K2
41. Isi Name `Bengkel Kontak Person {runId}`
42. Centang checkbox `Routine`
43. Isi City `Banjarmasin`
44. Isi Company email `admin@kontakpic-banjarmasin.co.id`
45. Klik `[+ Contact person]`
46. Isi Name pada baris ke-1 `Andi Pratama`
47. Isi Email pada baris ke-1 `andi@kontakpic-palembang.co.id`
48. Klik `[Submit]`
49. Verifikasi pesan `Up to 3 contact persons, with one primary.` tampil pada field `Contact persons`
50. Verifikasi dialog Create masih terbuka

### Contact person tanpa Name atau tanpa Phone dan Email ditolak saat Save (Create)
51. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
52. Isi Name `Bengkel Kontak Person {runId}`
53. Centang checkbox `Routine`
54. Isi City `Banjarmasin`
55. Isi Company email `admin@kontakpic-banjarmasin.co.id`
56. Klik `[+ Contact person]`
57. Klik `[Submit]` dengan baris ke-1 yang Name, Phone, dan Email-nya kosong
58. Verifikasi baris ke-1 menampilkan pesan `Contact name must not be empty` pada field `Name`
59. Verifikasi baris ke-1 menampilkan pesan `Add a phone or email` pada field `Phone` dan pada field `Email`
60. Isi Name pada baris ke-1 `   `
61. Klik `[Submit]`
62. Verifikasi baris ke-1 menampilkan pesan `Contact name must not be empty` pada field `Name`
63. Klik `[+ Contact person]`
64. Isi Name pada baris ke-2 `Rina Wijaya`
65. Isi Email pada baris ke-2 `rina@kontakpic-palembang.co.id`
66. Klik `[Submit]`
67. Verifikasi baris `Rina Wijaya` tidak menampilkan pesan error

### Contact person dengan Phone saja diterima (Create)
68. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
69. Isi Name `Bengkel Kontak Person {runId}`
70. Centang checkbox `Routine`
71. Isi City `Banjarmasin`
72. Isi Company email `admin@kontakpic-banjarmasin.co.id`
73. Klik `[+ Contact person]`
74. Isi Name pada baris ke-1 `Andi Pratama`
75. Ketik `85611112233` di field `Phone` pada baris ke-1
76. Verifikasi field `Phone` pada baris ke-1 berisi `85611112233`
77. Verifikasi pesan `Min. 4 characters` tidak tampil
78. Klik `[Submit]`
79. Verifikasi dialog Create tertutup
80. Verifikasi permintaan simpan yang terkirim berjumlah `1`

### Contact person dengan Email saja diterima tanpa Phone (Create)
81. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
82. Isi Name `Bengkel Kontak Person {runId}`
83. Centang checkbox `Routine`
84. Isi City `Banjarmasin`
85. Isi Company email `admin@kontakpic-banjarmasin.co.id`
86. Klik `[+ Contact person]`
87. Isi Name pada baris ke-1 `Andi Pratama`
88. Isi Email pada baris ke-1 `andi@kontakpic-palembang.co.id`
89. Verifikasi field `Email` pada baris ke-1 berisi `andi@kontakpic-palembang.co.id`
90. Verifikasi field `Phone` pada baris ke-1 menampilkan placeholder `Enter phone number`
91. Klik `[Submit]`
92. Verifikasi dialog Create tertutup
93. Verifikasi permintaan simpan yang terkirim berjumlah `1`

### Batas 120 karakter pada Contact name (Create)
94. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
95. Isi Name `Bengkel Kontak Person {runId}`
96. Centang checkbox `Routine`
97. Isi City `Banjarmasin`
98. Isi Company email `admin@kontakpic-banjarmasin.co.id`
99. Klik `[+ Contact person]`
100. Isi Name pada baris ke-1 `Q`
101. Verifikasi field `Name` pada baris ke-1 berisi `Q`
102. Verifikasi pesan `Max. 120 characters` tidak tampil
103. Ganti isi Name pada baris ke-1 dengan `Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi`
104. Verifikasi field `Name` pada baris ke-1 berisi `Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi` (120 karakter)
105. Verifikasi pesan `Max. 120 characters` tidak tampil
106. Ganti isi Name pada baris ke-1 dengan `Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andii`
107. Verifikasi baris ke-1 menampilkan pesan `Max. 120 characters` pada field `Name`
108. Ganti isi Name pada baris ke-1 dengan `Andi  Pratama  Wijaya  Hartono  Santoso  Rahma  Nugraha  Saputra  Andi  Pratama  Wijaya  Hartono  Santoso  Rahma  Nugrah`
109. Verifikasi field `Name` pada baris ke-1 berisi `Andi  Pratama  Wijaya  Hartono  Santoso  Rahma  Nugraha  Saputra  Andi  Pratama  Wijaya  Hartono  Santoso  Rahma  Nugrah` (120 karakter)
110. Verifikasi pesan `Max. 120 characters` tidak tampil
111. Ganti isi Name pada baris ke-1 dengan `  Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi  `
112. Verifikasi field `Name` pada baris ke-1 berisi `  Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi  ` (124 karakter)
113. Verifikasi pesan `Max. 120 characters` tidak tampil

### Karakter yang diizinkan dan emoji diblok pada Contact name (Create)
114. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
115. Isi Name `Bengkel Kontak Person {runId}`
116. Centang checkbox `Routine`
117. Isi City `Banjarmasin`
118. Isi Company email `admin@kontakpic-banjarmasin.co.id`
119. Klik `[+ Contact person]`
120. Isi Name pada baris ke-1 `Андрей Иванов 李明`
121. Verifikasi field `Name` pada baris ke-1 berisi `Андрей Иванов 李明`
122. Verifikasi pesan `Contact name contains invalid characters` tidak tampil
123. Ganti isi Name pada baris ke-1 dengan `O'Neil-Smith, Jr. (Ahmad)`
124. Verifikasi field `Name` pada baris ke-1 berisi `O'Neil-Smith, Jr. (Ahmad)`
125. Verifikasi pesan `Contact name contains invalid characters` tidak tampil
126. Hapus seluruh isi field `Name` pada baris ke-1
127. Ketik `Andi📊 Pratama` di field `Name` pada baris ke-1
128. Verifikasi field `Name` pada baris ke-1 berisi `Andi Pratama`
129. Verifikasi pesan `Contact name contains invalid characters` tidak tampil
130. Hapus seluruh isi field `Name` pada baris ke-1
131. Tempel `Rina📎 Wijaya` ke field `Name` pada baris ke-1
132. Verifikasi field `Name` pada baris ke-1 berisi `Rina Wijaya`
133. Verifikasi pesan `Contact name contains invalid characters` tidak tampil
134. Hapus seluruh isi field `Name` pada baris ke-1
135. Lepas teks `Tono🔍 Hartono` ke field `Name` pada baris ke-1 dengan drag-drop
136. Verifikasi baris ke-1 menampilkan pesan `Contact name contains invalid characters` pada field `Name`

### Spasi tepi pada Contact name dibuang dan spasi tengah dipertahankan saat Save (Create)
137. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
138. Isi Name `Bengkel Kontak Person {runId}`
139. Centang checkbox `Routine`
140. Isi City `Banjarmasin`
141. Isi Company email `admin@kontakpic-banjarmasin.co.id`
142. Klik `[+ Contact person]`
143. Klik `[+ Contact person]`
144. Isi Name pada baris ke-1 `  Andi Pratama  `
145. Isi Email pada baris ke-1 `andi@kontakpic-palembang.co.id`
146. Isi Name pada baris ke-2 `Rina  Wijaya Putri`
147. Isi Email pada baris ke-2 `rina@kontakpic-palembang.co.id`
148. Klik `[Submit]`
149. Verifikasi Name contact person pertama pada permintaan simpan adalah `Andi Pratama`
150. Verifikasi Name contact person kedua pada permintaan simpan adalah `Rina  Wijaya Putri`

### Format dan batas 120 karakter pada Contact email (Create)
151. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
152. Isi Name `Bengkel Kontak Person {runId}`
153. Centang checkbox `Routine`
154. Isi City `Banjarmasin`
155. Isi Company email `admin@kontakpic-banjarmasin.co.id`
156. Klik `[+ Contact person]`
157. Isi Name pada baris ke-1 `Andi Pratama`
158. Isi Email pada baris ke-1 `andi.kontakpic-palembang.co.id`
159. Pindahkan fokus dari field `Email` pada baris ke-1 ke field `Name` pada baris ke-1
160. Verifikasi baris ke-1 menampilkan pesan `Enter a valid email` pada field `Email`
161. Ganti isi Email pada baris ke-1 dengan `andi@kontakpic-palembang.co.id`
162. Pindahkan fokus dari field `Email` pada baris ke-1 ke field `Name` pada baris ke-1
163. Verifikasi field `Email` pada baris ke-1 berisi `andi@kontakpic-palembang.co.id`
164. Verifikasi pesan `Enter a valid email` tidak tampil
165. Ganti isi Email pada baris ke-1 dengan `layananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclaya@kontakpic-palembang.co.id`
166. Verifikasi field `Email` pada baris ke-1 berisi `layananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclaya@kontakpic-palembang.co.id` (120 karakter)
167. Verifikasi pesan `Max. 120 characters` tidak tampil
168. Ganti isi Email pada baris ke-1 dengan `layananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayan@kontakpic-palembang.co.id`
169. Verifikasi baris ke-1 menampilkan pesan `Max. 120 characters` pada field `Email`

### Nomor Contact phone kurang dari 4 digit ditandai tidak valid (Create)
170. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
171. Isi Name `Bengkel Kontak Person {runId}`
172. Centang checkbox `Routine`
173. Isi City `Banjarmasin`
174. Isi Company email `admin@kontakpic-banjarmasin.co.id`
175. Klik `[+ Contact person]`
176. Isi Name pada baris ke-1 `Andi Pratama`
177. Ketik `734` di field `Phone` pada baris ke-1
178. Verifikasi field `Phone` pada baris ke-1 berisi `734`
179. Verifikasi baris ke-1 menampilkan pesan `Min. 4 characters` pada field `Phone`
180. Ketik `4` di akhir field `Phone` pada baris ke-1
181. Verifikasi field `Phone` pada baris ke-1 berisi `7345`
182. Verifikasi pesan `Min. 4 characters` tidak tampil

### Batas 15 digit pada nomor Contact phone (Create)
183. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
184. Isi Name `Bengkel Kontak Person {runId}`
185. Centang checkbox `Routine`
186. Isi City `Banjarmasin`
187. Isi Company email `admin@kontakpic-banjarmasin.co.id`
188. Klik `[+ Contact person]`
189. Isi Name pada baris ke-1 `Andi Pratama`
190. Klik tombol kode negara pada field `Phone` pada baris ke-1
191. Ketik `Singapore` di kotak `Search` pada daftar negara
192. Klik opsi `Singapore (+65)`
193. Ketik `712345678901234` di field `Phone` pada baris ke-1
194. Verifikasi field `Phone` pada baris ke-1 berisi `712345678901234`
195. Verifikasi pesan `Max. 15 characters` tidak tampil
196. Ketik `6` di akhir field `Phone` pada baris ke-1
197. Verifikasi field `Phone` pada baris ke-1 berisi `712345678901234`
198. Hapus seluruh isi field `Phone` pada baris ke-1
199. Tempel `7123456789012345` ke field `Phone` pada baris ke-1
200. Verifikasi field `Phone` pada baris ke-1 berisi `712345678901234`

### Dial Code tidak dihitung dalam batas nomor Contact phone (Create)
201. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
202. Isi Name `Bengkel Kontak Person {runId}`
203. Centang checkbox `Routine`
204. Isi City `Banjarmasin`
205. Isi Company email `admin@kontakpic-banjarmasin.co.id`
206. Klik `[+ Contact person]`
207. Isi Name pada baris ke-1 `Andi Pratama`
208. Klik tombol kode negara pada field `Phone` pada baris ke-1
209. Ketik `Indonesia` di kotak `Search` pada daftar negara
210. Klik opsi `Indonesia (+62)`
211. Ketik `813345678901234` di field `Phone` pada baris ke-1
212. Verifikasi field `Phone` pada baris ke-1 berisi `813345678901234`
213. Verifikasi pesan `Max. 15 characters` tidak tampil

### Tambah baris contact person dan Primary (Edit)
214. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
215. Verifikasi field `Contact persons` memiliki 2 baris
216. Verifikasi baris `Budi Santoso` bertanda Primary dan baris `Siti Rahma` tidak bertanda Primary
217. Klik `[+ Contact person]`
218. Verifikasi field `Contact persons` memiliki 3 baris
219. Klik pilihan Primary pada baris ke-2
220. Verifikasi baris ke-2 bertanda Primary dan baris ke-1 tidak bertanda Primary

### Hapus baris Primary memindahkan Primary (Edit)
221. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
222. Verifikasi baris `Budi Santoso` bertanda Primary
223. Klik tombol hapus pada baris `Budi Santoso`
224. Verifikasi baris `Siti Rahma` bertanda Primary dan field `Contact persons` memiliki 1 baris
225. Klik tombol hapus pada baris `Siti Rahma`
226. Verifikasi field `Contact persons` tidak memiliki baris

### Contact persons maksimal 3 baris (Edit)
227. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
228. Verifikasi field `Contact persons` memiliki 2 baris dan tombol `[+ Contact person]` dapat diklik
229. Klik `[+ Contact person]`
230. Verifikasi field `Contact persons` memiliki 3 baris
231. Verifikasi tombol `[+ Contact person]` disabled
232. Arahkan kursor ke tombol `[+ Contact person]`
233. Verifikasi alasan `Up to 3 contact persons.` tersampaikan pada tombol `[+ Contact person]` yang disabled
234. Klik tombol hapus pada baris ke-3
235. Verifikasi tombol `[+ Contact person]` dapat diklik kembali

### Contact persons melebihi batas atau tanpa Primary ditolak server saat Save (Edit)
236. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
237. Klik `[Save]`
238. Verifikasi pesan `Up to 3 contact persons, with one primary.` tampil pada field `Contact persons`
239. Verifikasi dialog Edit masih terbuka

### Contact person tanpa Name atau tanpa Phone dan Email ditolak saat Save (Edit)
240. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
241. Hapus seluruh isi field `Name` pada baris ke-1
242. Hapus seluruh isi field `Phone` pada baris ke-1
243. Hapus seluruh isi field `Email` pada baris ke-1
244. Klik `[Save]` dengan baris ke-1 yang Name, Phone, dan Email-nya kosong
245. Verifikasi baris ke-1 menampilkan pesan `Contact name must not be empty` pada field `Name`
246. Verifikasi baris ke-1 menampilkan pesan `Add a phone or email` pada field `Phone` dan pada field `Email`
247. Ganti isi Name pada baris ke-1 dengan `   `
248. Klik `[Save]`
249. Verifikasi baris ke-1 menampilkan pesan `Contact name must not be empty` pada field `Name`
250. Klik `[+ Contact person]`
251. Isi Name pada baris ke-3 `Rina Wijaya`
252. Isi Email pada baris ke-3 `rina@kontakpic-palembang.co.id`
253. Klik `[Save]`
254. Verifikasi baris `Rina Wijaya` tidak menampilkan pesan error

### Contact person dengan Phone saja diterima (Edit)
255. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
256. Hapus seluruh isi field `Email` pada baris ke-1
257. Ganti isi Name pada baris ke-1 dengan `Andi Pratama`
258. Hapus seluruh isi field `Phone` pada baris ke-1
259. Ketik `85611112233` di field `Phone` pada baris ke-1
260. Verifikasi field `Phone` pada baris ke-1 berisi `85611112233`
261. Verifikasi pesan `Min. 4 characters` tidak tampil
262. Klik `[Save]`
263. Verifikasi dialog Edit tertutup
264. Verifikasi permintaan simpan yang terkirim berjumlah `1`

### Contact person dengan Email saja diterima tanpa Phone (Edit)
265. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
266. Hapus seluruh isi field `Phone` pada baris ke-1
267. Ganti isi Name pada baris ke-1 dengan `Andi Pratama`
268. Ganti isi Email pada baris ke-1 dengan `andi@kontakpic-palembang.co.id`
269. Verifikasi field `Email` pada baris ke-1 berisi `andi@kontakpic-palembang.co.id`
270. Verifikasi field `Phone` pada baris ke-1 menampilkan placeholder `Enter phone number`
271. Klik `[Save]`
272. Verifikasi dialog Edit tertutup
273. Verifikasi permintaan simpan yang terkirim berjumlah `1`

### Batas 120 karakter pada Contact name (Edit)
274. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
275. Ganti isi Name pada baris ke-1 dengan `Q`
276. Verifikasi field `Name` pada baris ke-1 berisi `Q`
277. Verifikasi pesan `Max. 120 characters` tidak tampil
278. Ganti isi Name pada baris ke-1 dengan `Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi`
279. Verifikasi field `Name` pada baris ke-1 berisi `Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi` (120 karakter)
280. Verifikasi pesan `Max. 120 characters` tidak tampil
281. Ganti isi Name pada baris ke-1 dengan `Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andii`
282. Verifikasi baris ke-1 menampilkan pesan `Max. 120 characters` pada field `Name`
283. Ganti isi Name pada baris ke-1 dengan `Andi  Pratama  Wijaya  Hartono  Santoso  Rahma  Nugraha  Saputra  Andi  Pratama  Wijaya  Hartono  Santoso  Rahma  Nugrah`
284. Verifikasi field `Name` pada baris ke-1 berisi `Andi  Pratama  Wijaya  Hartono  Santoso  Rahma  Nugraha  Saputra  Andi  Pratama  Wijaya  Hartono  Santoso  Rahma  Nugrah` (120 karakter)
285. Verifikasi pesan `Max. 120 characters` tidak tampil
286. Ganti isi Name pada baris ke-1 dengan `  Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi  `
287. Verifikasi field `Name` pada baris ke-1 berisi `  Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi Pratama Wijaya Hartono Santoso Rahma Nugraha Saputra Andi  ` (124 karakter)
288. Verifikasi pesan `Max. 120 characters` tidak tampil

### Karakter yang diizinkan dan emoji diblok pada Contact name (Edit)
289. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
290. Ganti isi Name pada baris ke-1 dengan `Андрей Иванов 李明`
291. Verifikasi field `Name` pada baris ke-1 berisi `Андрей Иванов 李明`
292. Verifikasi pesan `Contact name contains invalid characters` tidak tampil
293. Ganti isi Name pada baris ke-1 dengan `O'Neil-Smith, Jr. (Ahmad)`
294. Verifikasi field `Name` pada baris ke-1 berisi `O'Neil-Smith, Jr. (Ahmad)`
295. Verifikasi pesan `Contact name contains invalid characters` tidak tampil
296. Hapus seluruh isi field `Name` pada baris ke-1
297. Ketik `Andi📊 Pratama` di field `Name` pada baris ke-1
298. Verifikasi field `Name` pada baris ke-1 berisi `Andi Pratama`
299. Verifikasi pesan `Contact name contains invalid characters` tidak tampil
300. Hapus seluruh isi field `Name` pada baris ke-1
301. Tempel `Rina📎 Wijaya` ke field `Name` pada baris ke-1
302. Verifikasi field `Name` pada baris ke-1 berisi `Rina Wijaya`
303. Verifikasi pesan `Contact name contains invalid characters` tidak tampil
304. Hapus seluruh isi field `Name` pada baris ke-1
305. Lepas teks `Tono🔍 Hartono` ke field `Name` pada baris ke-1 dengan drag-drop
306. Verifikasi baris ke-1 menampilkan pesan `Contact name contains invalid characters` pada field `Name`

### Spasi tepi pada Contact name dibuang dan spasi tengah dipertahankan saat Save (Edit)
307. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
308. Ganti isi Name pada baris ke-1 dengan `  Andi Pratama  `
309. Ganti isi Name pada baris ke-2 dengan `Rina  Wijaya Putri`
310. Klik `[Save]`
311. Verifikasi Name contact person pertama pada permintaan simpan adalah `Andi Pratama`
312. Verifikasi Name contact person kedua pada permintaan simpan adalah `Rina  Wijaya Putri`

### Format dan batas 120 karakter pada Contact email (Edit)
313. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
314. Ganti isi Name pada baris ke-1 dengan `Andi Pratama`
315. Ganti isi Email pada baris ke-1 dengan `andi.kontakpic-palembang.co.id`
316. Pindahkan fokus dari field `Email` pada baris ke-1 ke field `Name` pada baris ke-1
317. Verifikasi baris ke-1 menampilkan pesan `Enter a valid email` pada field `Email`
318. Ganti isi Email pada baris ke-1 dengan `andi@kontakpic-palembang.co.id`
319. Pindahkan fokus dari field `Email` pada baris ke-1 ke field `Name` pada baris ke-1
320. Verifikasi field `Email` pada baris ke-1 berisi `andi@kontakpic-palembang.co.id`
321. Verifikasi pesan `Enter a valid email` tidak tampil
322. Ganti isi Email pada baris ke-1 dengan `layananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclaya@kontakpic-palembang.co.id`
323. Verifikasi field `Email` pada baris ke-1 berisi `layananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclaya@kontakpic-palembang.co.id` (120 karakter)
324. Verifikasi pesan `Max. 120 characters` tidak tampil
325. Ganti isi Email pada baris ke-1 dengan `layananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayananpiclayan@kontakpic-palembang.co.id`
326. Verifikasi baris ke-1 menampilkan pesan `Max. 120 characters` pada field `Email`

### Nomor Contact phone kurang dari 4 digit ditandai tidak valid (Edit)
327. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
328. Ganti isi Name pada baris ke-1 dengan `Andi Pratama`
329. Hapus seluruh isi field `Phone` pada baris ke-1
330. Ketik `734` di field `Phone` pada baris ke-1
331. Verifikasi field `Phone` pada baris ke-1 berisi `734`
332. Verifikasi baris ke-1 menampilkan pesan `Min. 4 characters` pada field `Phone`
333. Ketik `4` di akhir field `Phone` pada baris ke-1
334. Verifikasi field `Phone` pada baris ke-1 berisi `7345`
335. Verifikasi pesan `Min. 4 characters` tidak tampil

### Batas 15 digit pada nomor Contact phone (Edit)
336. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
337. Ganti isi Name pada baris ke-1 dengan `Andi Pratama`
338. Klik tombol kode negara pada field `Phone` pada baris ke-1
339. Ketik `Singapore` di kotak `Search` pada daftar negara
340. Klik opsi `Singapore (+65)`
341. Hapus seluruh isi field `Phone` pada baris ke-1
342. Ketik `712345678901234` di field `Phone` pada baris ke-1
343. Verifikasi field `Phone` pada baris ke-1 berisi `712345678901234`
344. Verifikasi pesan `Max. 15 characters` tidak tampil
345. Ketik `6` di akhir field `Phone` pada baris ke-1
346. Verifikasi field `Phone` pada baris ke-1 berisi `712345678901234`
347. Hapus seluruh isi field `Phone` pada baris ke-1
348. Tempel `7123456789012345` ke field `Phone` pada baris ke-1
349. Verifikasi field `Phone` pada baris ke-1 berisi `712345678901234`

### Dial Code tidak dihitung dalam batas nomor Contact phone (Edit)
350. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
351. Ganti isi Name pada baris ke-1 dengan `Andi Pratama`
352. Klik tombol kode negara pada field `Phone` pada baris ke-1
353. Ketik `Indonesia` di kotak `Search` pada daftar negara
354. Klik opsi `Indonesia (+62)`
355. Hapus seluruh isi field `Phone` pada baris ke-1
356. Ketik `813345678901234` di field `Phone` pada baris ke-1
357. Verifikasi field `Phone` pada baris ke-1 berisi `813345678901234`
358. Verifikasi pesan `Max. 15 characters` tidak tampil

### Vendor tanpa contact person dengan Company phone saja valid (Create)
359. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
360. Isi Name `Bengkel Kontak Person {runId}`
361. Centang checkbox `Routine`
362. Isi City `Banjarmasin`
363. Ketik `85611112233` di field `Company phone`
364. Verifikasi field `Contact persons` tidak memiliki baris
365. Klik `[Submit]`
366. Verifikasi dialog Create tertutup

### Vendor tanpa contact person dengan Company phone saja valid (Edit)
367. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
368. Klik tombol hapus pada baris `Budi Santoso`
369. Klik tombol hapus pada baris `Siti Rahma`
370. Verifikasi field `Contact persons` tidak memiliki baris
371. Klik `[Save]`
372. Verifikasi dialog Edit tertutup

### Hapus baris Primary di tengah memindahkan Primary ke baris pertama yang tersisa (Create)
373. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
374. Isi Name `Bengkel Kontak Person {runId}`
375. Centang checkbox `Routine`
376. Isi City `Banjarmasin`
377. Isi Company email `admin@kontakpic-banjarmasin.co.id`
378. Klik `[+ Contact person]`
379. Klik `[+ Contact person]`
380. Klik `[+ Contact person]`
381. Isi Name pada baris ke-1 `Andi Pratama`
382. Isi Name pada baris ke-2 `Rina Wijaya`
383. Isi Name pada baris ke-3 `Tono Hartono`
384. Klik pilihan Primary pada baris ke-2
385. Verifikasi baris `Rina Wijaya` bertanda Primary
386. Klik tombol hapus pada baris `Rina Wijaya`
387. Verifikasi baris `Andi Pratama` bertanda Primary dan baris `Tono Hartono` tidak bertanda Primary
388. Klik pilihan Primary pada baris `Tono Hartono`
389. Klik tombol hapus pada baris `Tono Hartono`
390. Verifikasi baris `Andi Pratama` bertanda Primary dan field `Contact persons` memiliki 1 baris

### Hapus baris Primary yang bukan baris pertama memindahkan Primary ke baris pertama yang tersisa (Edit)
391. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
392. Klik `[+ Contact person]`
393. Isi Name pada baris ke-3 `Tono Hartono`
394. Klik pilihan Primary pada baris `Tono Hartono`
395. Klik tombol hapus pada baris `Tono Hartono`
396. Verifikasi baris `Budi Santoso` bertanda Primary dan baris `Siti Rahma` tidak bertanda Primary

### Placeholder field baris contact person (Create)
397. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
398. Klik `[+ Contact person]`
399. Verifikasi field `Name` pada baris ke-1 menampilkan placeholder `Enter name`
400. Verifikasi field `Phone` pada baris ke-1 menampilkan placeholder `Enter phone number`
401. Verifikasi field `Email` pada baris ke-1 menampilkan placeholder `Enter email`

### Nilai tersimpan baris contact person terisi pada Edit
402. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
403. Verifikasi field `Name` pada baris ke-1 berisi `Budi Santoso`
404. Verifikasi field `Phone` pada baris ke-1 berisi `85611110001`
405. Verifikasi field `Email` pada baris ke-1 berisi `budi@kontakpic-mitra.co.id`

### Contact persons ditolak server: isian terjaga (Create)
406. Tampilkan Dialog Create / Edit Service Center dengan kondisi K2
407. Isi Name `Bengkel Kontak Person {runId}`
408. Centang checkbox `Routine`
409. Isi City `Banjarmasin`
410. Isi Company email `admin@kontakpic-banjarmasin.co.id`
411. Klik `[+ Contact person]`
412. Isi Name pada baris ke-1 `Andi Pratama`
413. Isi Email pada baris ke-1 `andi@kontakpic-palembang.co.id`
414. Klik `[Submit]`
415. Verifikasi pesan `Up to 3 contact persons, with one primary.` tampil pada field `Contact persons`
416. Verifikasi field `Name` berisi `Bengkel Kontak Person {runId}` dan field `City` berisi `Banjarmasin`
417. Verifikasi field `Name` pada baris ke-1 berisi `Andi Pratama` dan field `Email` pada baris ke-1 berisi `andi@kontakpic-palembang.co.id`

### Contact persons ditolak server: isian terjaga (Edit)
418. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
419. Klik `[Save]`
420. Verifikasi pesan `Up to 3 contact persons, with one primary.` tampil pada field `Contact persons`
421. Verifikasi field `Contact persons` memiliki 2 baris, yaitu baris `Budi Santoso` dan baris `Siti Rahma`

: Drift PRD vs kontrak komponen. PRD §6 `V-FASVC-35` (Contact phone memakai `V-FASVC-35` yang sama): nomor lebih dari 15 digit menampilkan `Max. 15 characters` langsung saat mengetik. Kontrak `PhoneInput#4` dan `#16`: digit melebihi batas dibuang dan komponen tidak menampilkan pesan sendiri. Diasersi: kontrak, digit ke-16 dibuang dan nomor tetap 15 digit (SB-7).

### Digit ke-16 dibuang tanpa pesan pada Contact phone (Create)
422. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
423. Klik `[+ Contact person]`
424. Klik tombol kode negara pada field `Phone` pada baris ke-1
425. Ketik `Singapore` di kotak `Search` pada daftar negara
426. Klik opsi `Singapore (+65)`
427. Ketik `712345678901234` di field `Phone` pada baris ke-1
428. Ketik `6` di akhir field `Phone` pada baris ke-1
429. Verifikasi field `Phone` pada baris ke-1 berisi `712345678901234`
430. Verifikasi pesan `Max. 15 characters` tidak tampil
431. Hapus seluruh isi field `Phone` pada baris ke-1
432. Tempel `7123456789012345` ke field `Phone` pada baris ke-1
433. Verifikasi field `Phone` pada baris ke-1 berisi `712345678901234`
434. Verifikasi pesan `Max. 15 characters` tidak tampil

### Digit ke-16 dibuang tanpa pesan pada Contact phone (Edit)
435. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
436. Klik tombol kode negara pada field `Phone` pada baris ke-1
437. Ketik `Singapore` di kotak `Search` pada daftar negara
438. Klik opsi `Singapore (+65)`
439. Hapus seluruh isi field `Phone` pada baris ke-1
440. Ketik `712345678901234` di field `Phone` pada baris ke-1
441. Ketik `6` di akhir field `Phone` pada baris ke-1
442. Verifikasi field `Phone` pada baris ke-1 berisi `712345678901234`
443. Verifikasi pesan `Max. 15 characters` tidak tampil
444. Hapus seluruh isi field `Phone` pada baris ke-1
445. Tempel `7123456789012345` ke field `Phone` pada baris ke-1
446. Verifikasi field `Phone` pada baris ke-1 berisi `712345678901234`
447. Verifikasi pesan `Max. 15 characters` tidak tampil


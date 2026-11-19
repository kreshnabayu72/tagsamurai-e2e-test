---
id: TC-FA-FASVC-UI-054-form-validasi-kontak-perusahaan
title: "Form: Company Phone, Company Email, dan Kontak Wajib Salah Satu"
layer: ui-client
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["V-FASVC-09", "V-FASVC-19", "V-FASVC-27", "V-FASVC-34", "V-FASVC-35", "FLD-FASVC-11", "FLD-FASVC-12", "EC-FASVC-18", "EC-FASVC-19", "F-FASVC-02.k8", "EB-FRM-4@company-email", "EB-FRM-8@company-contact"]
smoke: []
dependsOn: []
trace:
  "V-FASVC-09": [81, 84, 85, 169, 172, 173]
  "V-FASVC-19": [88, 89, 91, 176, 177, 179]
  "V-FASVC-27": [10, 11, 12, 22, 33, 100, 101, 102, 111, 120]
  "V-FASVC-34": [19, 29, 30, 36, 37, 39, 40, 108, 116, 117, 124, 125, 127, 128]
  "V-FASVC-35": [47, 48, 50, 53, 59, 60, 61, 136, 137, 139, 142, 149, 150, 151, 186, 187, 190, 191, 199, 200, 203, 204]
  "FLD-FASVC-11": [2, 4, 10, 18, 21, 22, 29, 36, 37, 39, 45, 47, 50, 60, 71, 77, 93, 94, 100, 107, 110, 111, 116, 124, 125, 127, 133, 136, 139, 150, 159, 165, 186, 187, 190, 191, 199, 200, 203, 204]
  "FLD-FASVC-12": [3, 4, 11, 28, 32, 33, 81, 84, 88, 91, 95, 101, 115, 119, 120, 169, 172, 176, 179]
  "EC-FASVC-18": [10, 11, 12, 100, 101, 102]
  "EC-FASVC-19": [71, 72, 76, 77, 159, 160, 164, 165]
  "F-FASVC-02.k8": [10, 11, 12, 100, 101, 102]
  "EB-FRM-4@company-email": [88, 89, 91, 176, 177, 179]
  "EB-FRM-8@company-contact": [10, 11, 18, 22, 28, 33, 36, 37, 47, 60, 71, 81, 84, 88, 91, 100, 101, 107, 111, 115, 120, 124, 125, 136, 150, 159, 169, 172, 176, 179]
anchor: []
coverage:
  web: automated
---

# Form: Company Phone, Company Email, dan Kontak Wajib Salah Satu

## Prerequisites
- Aktor: Total Control.
- Layar awal: dialog Create / Edit Service Center yang ditampilkan menurut kondisi di bawah.
- Komponen: Dialog Create / Edit Service Center
- Data:
  - DU-054-1: pohon Group cakupan Total Control: root `All groups`, anak `Head Office`.
  - DU-054-2: daftar kode negara memuat `Indonesia (+62)`, `Singapore (+65)`, dan `Malaysia (+60)`.
  - DU-054-3: Service Center untuk Edit: Name `PT Servis Kontak Terpadu`, Service type `Routine`, Available to `Head Office`, Country `Indonesia`, City `Bandung`, Company phone dengan Dial Code `+62` dan nomor `227771234`, Company email `kontak@servisterpadu-bdg.co.id`.
  - Nilai nomor dan email pada langkah tercatat di entri data DU-054-4 dan seterusnya.
- Kondisi:
  - K1: dialog Create dibuka oleh Total Control; pohon Group DU-054-1 dan daftar kode negara DU-054-2; permintaan simpan dijawab sukses.
  - K3: dialog Edit untuk Service Center DU-054-3 dibuka oleh Total Control; pohon Group DU-054-1 dan daftar kode negara DU-054-2; permintaan simpan dijawab sukses.

## Test Steps

### Nilai awal Company phone dan Company email (Create)
1. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
2. Verifikasi field `Company phone` menampilkan placeholder `Enter phone number`
3. Verifikasi field `Company email` menampilkan placeholder `Enter email`
4. Verifikasi field `Company phone` dan field `Company email` tidak ditandai wajib

### Phone dan email perusahaan sama-sama kosong ditolak saat Save (Create)
5. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
6. Isi Name `Bengkel Kontak Servis {runId}`
7. Centang checkbox `Routine`
8. Isi City `Palembang`
9. Klik `[Submit]` dengan field `Company phone` dan field `Company email` kosong
10. Verifikasi pesan `Add a company phone or email` tampil di bawah field `Company phone`
11. Verifikasi pesan `Add a company phone or email` tampil di bawah field `Company email`
12. Verifikasi tidak ada permintaan simpan yang terkirim

### Company phone saja diterima tanpa Company email (Create)
13. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
14. Isi Name `Bengkel Kontak Servis {runId}`
15. Centang checkbox `Routine`
16. Isi City `Palembang`
17. Ketik `8567123456` di field `Company phone`
18. Verifikasi field `Company phone` berisi `8567123456`
19. Verifikasi pesan `Min. 4 characters` tidak tampil
20. Klik `[Submit]`
21. Verifikasi dialog Create tertutup
22. Verifikasi permintaan simpan yang terkirim berjumlah `1`

### Company email saja diterima tanpa Company phone (Create)
23. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
24. Isi Name `Bengkel Kontak Servis {runId}`
25. Centang checkbox `Routine`
26. Isi City `Palembang`
27. Isi Company email `layanan@kontakservis-palembang.co.id`
28. Verifikasi field `Company email` berisi `layanan@kontakservis-palembang.co.id`
29. Verifikasi field `Company phone` menampilkan placeholder `Enter phone number`
30. Verifikasi pesan `Min. 4 characters` tidak tampil
31. Klik `[Submit]`
32. Verifikasi dialog Create tertutup
33. Verifikasi permintaan simpan yang terkirim berjumlah `1`

### Nomor Company phone kurang dari 4 digit ditandai tidak valid (Create)
34. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
35. Ketik `812` di field `Company phone`
36. Verifikasi field `Company phone` berisi `812`
37. Verifikasi field `Company phone` ditandai tidak valid dengan pesan `Min. 4 characters`
38. Ketik `3` di akhir field `Company phone`
39. Verifikasi field `Company phone` berisi `8123`
40. Verifikasi pesan `Min. 4 characters` tidak tampil

### Batas 15 digit pada nomor Company phone (Create)
41. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
42. Klik tombol kode negara pada field `Company phone`
43. Ketik `Singapore` di kotak `Search` pada daftar negara
44. Klik opsi `Singapore (+65)`
45. Verifikasi tombol kode negara pada field `Company phone` menampilkan `+65`
46. Ketik `612345678901234` di field `Company phone`
47. Verifikasi field `Company phone` berisi `612345678901234`
48. Verifikasi pesan `Max. 15 characters` tidak tampil
49. Ketik `5` di akhir field `Company phone`
50. Verifikasi field `Company phone` berisi `612345678901234`
51. Hapus seluruh isi field `Company phone`
52. Tempel `6123456789012345` ke field `Company phone`
53. Verifikasi field `Company phone` berisi `612345678901234`

### Dial Code tidak dihitung dalam batas nomor Company phone (Create)
54. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
55. Klik tombol kode negara pada field `Company phone`
56. Ketik `Indonesia` di kotak `Search` pada daftar negara
57. Klik opsi `Indonesia (+62)`
58. Ketik `812345678901234` di field `Company phone`
59. Verifikasi tombol kode negara pada field `Company phone` menampilkan `+62`
60. Verifikasi field `Company phone` berisi `812345678901234`
61. Verifikasi pesan `Max. 15 characters` tidak tampil

### Nomor internasional Company phone diterima (Create)
62. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
63. Isi Name `Bengkel Kontak Servis {runId}`
64. Centang checkbox `Routine`
65. Isi City `Palembang`
66. Klik tombol kode negara pada field `Company phone`
67. Ketik `Singapore` di kotak `Search` pada daftar negara
68. Klik opsi `Singapore (+65)`
69. Ketik `67654321` di field `Company phone`
70. Klik `[Submit]`
71. Verifikasi Company phone pada permintaan simpan adalah `+6567654321`
72. Verifikasi dialog Create tertutup

### Nomor internasional yang ditempel mengisi Dial Code dan nomor (Create)
73. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
74. Hapus seluruh isi field `Company phone`
75. Tempel `+65 67654321` ke field `Company phone`
76. Verifikasi tombol kode negara pada field `Company phone` menampilkan `+65`
77. Verifikasi field `Company phone` berisi `67654321`

### Format Company email diperiksa saat field ditinggalkan (Create)
78. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
79. Isi Company email `info.servisprima-bandung.co.id`
80. Pindahkan fokus dari field `Company email` ke field `Name`
81. Verifikasi field `Company email` ditandai tidak valid dengan pesan `Enter a valid email`
82. Ganti isi Company email dengan `info@servisprima-bandung.co.id`
83. Pindahkan fokus dari field `Company email` ke field `Name`
84. Verifikasi field `Company email` berisi `info@servisprima-bandung.co.id`
85. Verifikasi pesan `Enter a valid email` tidak tampil

### Batas 120 karakter pada Company email (Create)
86. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
87. Isi Company email `layananservislayananservislayananservislayananservislayananservislayananservislayananservislay@servisprima-bandung.co.id`
88. Verifikasi field `Company email` berisi `layananservislayananservislayananservislayananservislayananservislayananservislayananservislay@servisprima-bandung.co.id` (120 karakter)
89. Verifikasi pesan `Max. 120 characters` tidak tampil
90. Ganti isi Company email dengan `layananservislayananservislayananservislayananservislayananservislayananservislayananservislaya@servisprima-bandung.co.id`
91. Verifikasi field `Company email` ditandai tidak valid dengan pesan `Max. 120 characters`

### Nilai awal Company phone dan Company email (Edit)
92. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
93. Verifikasi tombol kode negara pada field `Company phone` menampilkan `+62`
94. Verifikasi field `Company phone` berisi `227771234`
95. Verifikasi field `Company email` berisi `kontak@servisterpadu-bdg.co.id`

### Phone dan email perusahaan sama-sama kosong ditolak saat Save (Edit)
96. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
97. Hapus seluruh isi field `Company phone`
98. Hapus seluruh isi field `Company email`
99. Klik `[Save]` dengan field `Company phone` dan field `Company email` kosong
100. Verifikasi pesan `Add a company phone or email` tampil di bawah field `Company phone`
101. Verifikasi pesan `Add a company phone or email` tampil di bawah field `Company email`
102. Verifikasi tidak ada permintaan simpan yang terkirim

### Company phone saja diterima tanpa Company email (Edit)
103. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
104. Hapus seluruh isi field `Company email`
105. Hapus seluruh isi field `Company phone`
106. Ketik `8567123456` di field `Company phone`
107. Verifikasi field `Company phone` berisi `8567123456`
108. Verifikasi pesan `Min. 4 characters` tidak tampil
109. Klik `[Save]`
110. Verifikasi dialog Edit tertutup
111. Verifikasi permintaan simpan yang terkirim berjumlah `1`

### Company email saja diterima tanpa Company phone (Edit)
112. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
113. Hapus seluruh isi field `Company phone`
114. Ganti isi Company email dengan `layanan@kontakservis-palembang.co.id`
115. Verifikasi field `Company email` berisi `layanan@kontakservis-palembang.co.id`
116. Verifikasi field `Company phone` menampilkan placeholder `Enter phone number`
117. Verifikasi pesan `Min. 4 characters` tidak tampil
118. Klik `[Save]`
119. Verifikasi dialog Edit tertutup
120. Verifikasi permintaan simpan yang terkirim berjumlah `1`

### Nomor Company phone kurang dari 4 digit ditandai tidak valid (Edit)
121. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
122. Hapus seluruh isi field `Company phone`
123. Ketik `812` di field `Company phone`
124. Verifikasi field `Company phone` berisi `812`
125. Verifikasi field `Company phone` ditandai tidak valid dengan pesan `Min. 4 characters`
126. Ketik `3` di akhir field `Company phone`
127. Verifikasi field `Company phone` berisi `8123`
128. Verifikasi pesan `Min. 4 characters` tidak tampil

### Batas 15 digit pada nomor Company phone (Edit)
129. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
130. Klik tombol kode negara pada field `Company phone`
131. Ketik `Singapore` di kotak `Search` pada daftar negara
132. Klik opsi `Singapore (+65)`
133. Verifikasi tombol kode negara pada field `Company phone` menampilkan `+65`
134. Hapus seluruh isi field `Company phone`
135. Ketik `612345678901234` di field `Company phone`
136. Verifikasi field `Company phone` berisi `612345678901234`
137. Verifikasi pesan `Max. 15 characters` tidak tampil
138. Ketik `5` di akhir field `Company phone`
139. Verifikasi field `Company phone` berisi `612345678901234`
140. Hapus seluruh isi field `Company phone`
141. Tempel `6123456789012345` ke field `Company phone`
142. Verifikasi field `Company phone` berisi `612345678901234`

### Dial Code tidak dihitung dalam batas nomor Company phone (Edit)
143. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
144. Klik tombol kode negara pada field `Company phone`
145. Ketik `Indonesia` di kotak `Search` pada daftar negara
146. Klik opsi `Indonesia (+62)`
147. Hapus seluruh isi field `Company phone`
148. Ketik `812345678901234` di field `Company phone`
149. Verifikasi tombol kode negara pada field `Company phone` menampilkan `+62`
150. Verifikasi field `Company phone` berisi `812345678901234`
151. Verifikasi pesan `Max. 15 characters` tidak tampil

### Nomor internasional Company phone diterima (Edit)
152. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
153. Klik tombol kode negara pada field `Company phone`
154. Ketik `Singapore` di kotak `Search` pada daftar negara
155. Klik opsi `Singapore (+65)`
156. Hapus seluruh isi field `Company phone`
157. Ketik `67654321` di field `Company phone`
158. Klik `[Save]`
159. Verifikasi Company phone pada permintaan simpan adalah `+6567654321`
160. Verifikasi dialog Edit tertutup

### Nomor internasional yang ditempel mengisi Dial Code dan nomor (Edit)
161. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
162. Hapus seluruh isi field `Company phone`
163. Tempel `+65 67654321` ke field `Company phone`
164. Verifikasi tombol kode negara pada field `Company phone` menampilkan `+65`
165. Verifikasi field `Company phone` berisi `67654321`

### Format Company email diperiksa saat field ditinggalkan (Edit)
166. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
167. Ganti isi Company email dengan `info.servisprima-bandung.co.id`
168. Pindahkan fokus dari field `Company email` ke field `Name`
169. Verifikasi field `Company email` ditandai tidak valid dengan pesan `Enter a valid email`
170. Ganti isi Company email dengan `info@servisprima-bandung.co.id`
171. Pindahkan fokus dari field `Company email` ke field `Name`
172. Verifikasi field `Company email` berisi `info@servisprima-bandung.co.id`
173. Verifikasi pesan `Enter a valid email` tidak tampil

### Batas 120 karakter pada Company email (Edit)
174. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
175. Ganti isi Company email dengan `layananservislayananservislayananservislayananservislayananservislayananservislayananservislay@servisprima-bandung.co.id`
176. Verifikasi field `Company email` berisi `layananservislayananservislayananservislayananservislayananservislayananservislayananservislay@servisprima-bandung.co.id` (120 karakter)
177. Verifikasi pesan `Max. 120 characters` tidak tampil
178. Ganti isi Company email dengan `layananservislayananservislayananservislayananservislayananservislayananservislayananservislaya@servisprima-bandung.co.id`
179. Verifikasi field `Company email` ditandai tidak valid dengan pesan `Max. 120 characters`

: Drift PRD vs kontrak komponen. PRD §6 `V-FASVC-35`: nomor lebih dari 15 digit menampilkan `Max. 15 characters` langsung saat mengetik. Kontrak `PhoneInput#4` dan `#16`: digit melebihi batas dibuang dan komponen tidak menampilkan pesan sendiri. Diasersi: kontrak, digit ke-16 dibuang dan nomor tetap 15 digit (SB-7); batas 15 mengasumsikan `maxDigit` 15 sesuai PRD.

### Digit ke-16 dibuang tanpa pesan pada Company phone (Create)
180. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
181. Klik tombol kode negara pada field `Company phone`
182. Ketik `Singapore` di kotak `Search` pada daftar negara
183. Klik opsi `Singapore (+65)`
184. Ketik `612345678901234` di field `Company phone`
185. Ketik `5` di akhir field `Company phone`
186. Verifikasi field `Company phone` berisi `612345678901234`
187. Verifikasi pesan `Max. 15 characters` tidak tampil
188. Hapus seluruh isi field `Company phone`
189. Tempel `6123456789012345` ke field `Company phone`
190. Verifikasi field `Company phone` berisi `612345678901234`
191. Verifikasi pesan `Max. 15 characters` tidak tampil

### Digit ke-16 dibuang tanpa pesan pada Company phone (Edit)
192. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
193. Klik tombol kode negara pada field `Company phone`
194. Ketik `Singapore` di kotak `Search` pada daftar negara
195. Klik opsi `Singapore (+65)`
196. Hapus seluruh isi field `Company phone`
197. Ketik `612345678901234` di field `Company phone`
198. Ketik `5` di akhir field `Company phone`
199. Verifikasi field `Company phone` berisi `612345678901234`
200. Verifikasi pesan `Max. 15 characters` tidak tampil
201. Hapus seluruh isi field `Company phone`
202. Tempel `6123456789012345` ke field `Company phone`
203. Verifikasi field `Company phone` berisi `612345678901234`
204. Verifikasi pesan `Max. 15 characters` tidak tampil

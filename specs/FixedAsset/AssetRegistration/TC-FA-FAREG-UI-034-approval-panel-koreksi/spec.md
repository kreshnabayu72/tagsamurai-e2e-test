---
id: TC-FA-FAREG-UI-034-approval-panel-koreksi
title: "Halaman Approval: panel koreksi approver, dialog Corrections, dan preview foto"
layer: ui-client
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: [D-REG-20, D-REG-21, D-REG-25, F-FAREG-07, FAREG-LOGIC-07a, FAREG-LOGIC-07b, FAREG-LOGIC-07c, FAREG-LOGIC-07d, FAREG-LOGIC-07h, FAREG-LOGIC-07i, FAREG-LOGIC-15e, FAREG-LOGIC-17c, FI-REG-19, FI-REG-20, FI-REG-21, FI-REG-22, T-REG-11, T-REG-12, T-REG-13, §4.1#r11, §4.1#r18, §4.1#r20, §4.1#b31, §4.2.4#b3, §4.2.4#b7, §4.2.4#b11, §9.6#r11, §9.9#p3, EB-ERR-1@simpan-koreksi, EB-FB-1@simpan-koreksi, EB-FRM-1@panel-koreksi, EB-FRM-2@panel-koreksi, EB-FRM-3@panel-koreksi, EB-FRM-7@panel-koreksi]
smoke: []
dependsOn: []
trace:
  D-REG-20: [69, 70, 71, 73, 76]
  D-REG-21: [134, 135, 136, 158]
  D-REG-25: [47, 48, 49, 55, 63]
  F-FAREG-07: [188, 190, 191]
  FAREG-LOGIC-07a: [24, 25, 26, 27, 33, 34]
  FAREG-LOGIC-07b: [38, 39, 40]
  FAREG-LOGIC-07c: 41
  FAREG-LOGIC-07d: [72, 188, 190, 191]
  FAREG-LOGIC-07h: [80, 82]
  FAREG-LOGIC-07i: [88, 89, 94, 98, 100, 103, 105, 110]
  FAREG-LOGIC-15e: 41
  FAREG-LOGIC-17c: [6, 18]
  FI-REG-19: [134, 138, 144, 146, 158, 160, 247, 249]
  FI-REG-20: [123, 124, 128, 129]
  FI-REG-21: [221, 222, 224, 225]
  FI-REG-22: [47, 48, 49, 63]
  T-REG-11: [181, 187, 216]
  T-REG-12: [197, 214]
  T-REG-13: 206
  §4.1#r11: [21, 22, 23, 24, 25, 26, 27, 28, 29, 34, 239, 240, 241]
  §4.1#r18: [47, 48, 49]
  §4.1#r20: [69, 71]
  §4.1#b31: [29, 30]
  §4.2.4#b3: [69, 71, 74]
  §4.2.4#b7: [3, 6, 9, 12, 15, 18]
  §4.2.4#b11: [44, 45, 66]
  §9.6#r11: [187, 197]
  §9.9#p3: [86, 88, 94, 100]
  EB-ERR-1@simpan-koreksi: [198, 199, 200, 206, 207, 208, 217]
  EB-FB-1@simpan-koreksi: [187, 197]
  EB-FRM-1@panel-koreksi: [175, 176, 177, 178, 181]
  EB-FRM-2@panel-koreksi: [123, 134, 138, 152, 153, 229, 230, 235]
  EB-FRM-3@panel-koreksi: [165, 166, 167, 168, 169]
  EB-FRM-7@panel-koreksi: [50, 51, 53, 57, 58, 113, 114, 117, 119]
anchor: [2, 37, 62, 163, 220, 238]
coverage:
  web: automated
---
# Halaman Approval: panel koreksi approver, dialog Corrections, dan preview foto

## Prerequisites
- Aktor: Dewi A (approver, role Group Manager, cakupan Group binaan + sub-group termasuk Gudang 1, bukan pengaju pengajuan).
- Layar awal: Halaman Approval pengajuan yang dibuka dari antrean Approvals tab Active.
- Komponen: Halaman Approval
- Data:
  - DU-034-1: pengajuan Registration ID `REG-20261109-00003`, Status `Waiting for Approval`, Group `Gudang 1`, Requested By `Rina W`, Total Asset `4`.
  - DU-034-2: aset Name `Laptop - 128`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason; di panel koreksi: Photo `foto-128-depan.jpg` lalu `foto-128-samping.jpg`, Alias Name `Laptop Kasir, Laptop Cadangan`, Asset labels `Aset Kantor` dan `Prioritas`, Custom field `Serial Number` bernilai `SN-128-0001`.
  - DU-034-3: aset Name `Laptop - 129`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Skipped`, Condition `Damaged`, Damage note `Scratch on the casing`, Corrections `1`, Decision awal `Approve` tanpa Reason; di panel koreksi: Photo `foto-129-depan.jpg`, Alias Name `Laptop Staf`, Asset labels `Aset Kantor`, Custom field `Serial Number` bernilai `SN-129-0001`; koreksi staged Field `Model`, Old Value `Latitude 5440`, New Value `Latitude 5450`.
  - DU-034-4: aset Name `Laptop - 130`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason; di panel koreksi: tanpa Photo, Alias Name `Laptop Gudang`, Asset labels `Prioritas`, Custom field `Serial Number` bernilai `SN-130-0001`.
  - DU-034-5: aset Name `Office Desk - 12`, Category `Furniture`, Brand `Kayu Jati`, Model `No Model`, Group `Gudang 1`, TAG `No tag`, Condition `Normal`, Corrections `—`, Decision awal `Approve`, tanpa Reason.
  - DU-034-6: master Brand `Lenovo` dengan Model `ThinkPad T14`, di samping Brand `Dell` dengan Model `Latitude 5440` dan `Latitude 5450`.
  - Pesan yang diharapkan saat pilihan Model tidak valid `Select Model again`, dari template `Select [Field Name] again` dan Field Name `Model`.
- Kondisi:
  - K1: pengajuan DU-034-1 berisi aset DU-034-2, DU-034-3, dan DU-034-4 dalam grup Accordion `Laptop` dan DU-034-5 dalam grup Accordion `Office Desk`, master DU-034-6 tersedia, dan approver berhak memutuskan, dengan Decision awal `Approve` pada setiap aset.
  - K2: seperti K1, dan menyimpan koreksi berhasil.
  - K3: seperti K1, dan menyimpan koreksi gagal karena error server.
  - K4: seperti K1, dan menyimpan koreksi gagal karena koneksi terputus.
  - K5: seperti K1, dan menyimpan koreksi gagal karena error server pada percobaan pertama, lalu berhasil pada percobaan kedua.
  - K6: seperti K1, dan menyimpan koreksi lambat sehingga respons belum diterima sesudah `[Save correction]` diklik.
  - K7: seperti K1, dan master Model `Latitude 5440` sudah dihapus dari master sejak halaman Approval terbuka, sehingga pilihan Model aset `Laptop - 128` tidak lagi valid.

## Test Steps

### Panel koreksi dibuka lewat row option Edit
1. Tampilkan Halaman Approval dengan kondisi K1
2. Verifikasi tabel aset Halaman Approval memuat baris `Laptop - 128`
3. Verifikasi tabel aset tidak memuat kolom `Action`
4. Klik row option (titik tiga) pada baris `Laptop - 128`
5. Klik `Edit`
6. Verifikasi panel koreksi terbuka

### Row option Edit aktif untuk semua Decision
7. Tampilkan Halaman Approval dengan kondisi K1
8. Klik row option (titik tiga) pada baris `Laptop - 128`
9. Verifikasi pilihan `Edit` aktif pada baris `Laptop - 128` dengan Decision `Approve`
10. Pilih Decision `Return to Draft` pada baris `Laptop - 129`
11. Klik row option (titik tiga) pada baris `Laptop - 129`
12. Verifikasi pilihan `Edit` aktif pada baris `Laptop - 129` dengan Decision `Return to Draft`
13. Pilih Decision `Reject` pada baris `Office Desk - 12`
14. Klik row option (titik tiga) pada baris `Office Desk - 12`
15. Verifikasi pilihan `Edit` aktif pada baris `Office Desk - 12` dengan Decision `Reject`

### Panel koreksi dibuka lewat link Name
16. Tampilkan Halaman Approval dengan kondisi K1
17. Klik nama `Laptop - 130`
18. Verifikasi panel koreksi terbuka

### Isi panel koreksi: data read-only, field koreksi, dan footer
19. Tampilkan Halaman Approval dengan kondisi K1
20. Klik nama `Laptop - 128`
21. Verifikasi panel memuat Photo sebagai thumbnail
22. Verifikasi panel memuat Alias Name `Laptop Kasir, Laptop Cadangan` sebagai teks dipisah koma
23. Verifikasi panel memuat Asset labels `Aset Kantor` dan `Prioritas`
24. Verifikasi panel memuat field koreksi `Brand`
25. Verifikasi panel memuat field koreksi `Model`
26. Verifikasi panel memuat field koreksi `Condition`
27. Verifikasi section Custom fields memuat field koreksi `Serial Number`
28. Verifikasi panel memuat tombol `[Clear Field]`
29. Verifikasi panel memuat tombol `[Save correction]`
30. Verifikasi panel tidak memuat tombol `[Save draft]`

### Damage note tampil pada aset Condition Damaged
31. Tampilkan Halaman Approval dengan kondisi K1
32. Klik nama `Laptop - 129`
33. Verifikasi panel memuat field koreksi `Condition` bernilai `Damaged`
34. Verifikasi panel memuat field koreksi `Damage note`

### Field yang tidak dapat dikoreksi tidak ada di panel
35. Tampilkan Halaman Approval dengan kondisi K1
36. Klik nama `Laptop - 128`
37. Verifikasi panel memuat field koreksi `Brand`
38. Verifikasi panel tidak memuat field koreksi `Asset Name`
39. Verifikasi panel tidak memuat field koreksi `Category`
40. Verifikasi panel tidak memuat field koreksi `Group`
41. Verifikasi panel tidak memuat field data `Purchase`

### Preview foto dengan dua foto
42. Tampilkan Halaman Approval dengan kondisi K1
43. Klik nama `Laptop - 128`
44. Verifikasi panel memuat dua thumbnail foto
45. Verifikasi urutan thumbnail foto `foto-128-depan.jpg` lalu `foto-128-samping.jpg`
46. Klik thumbnail foto `foto-128-depan.jpg`
47. Verifikasi dialog preview foto terbuka
48. Verifikasi dialog preview foto memuat tombol sebelumnya
49. Verifikasi dialog preview foto memuat tombol berikutnya
50. Verifikasi tombol sebelumnya dan tombol berikutnya memiliki label aksesibel
51. Verifikasi fokus berada di dalam dialog preview foto
52. Tekan Tab berulang kali
53. Verifikasi fokus tetap berada di dalam dialog preview foto
54. Klik tombol berikutnya
55. Verifikasi preview menampilkan foto `foto-128-samping.jpg`
56. Tekan `Esc`
57. Verifikasi dialog preview foto tertutup
58. Verifikasi fokus kembali ke thumbnail foto `foto-128-depan.jpg`

### Preview foto dengan satu foto
59. Tampilkan Halaman Approval dengan kondisi K1
60. Klik nama `Laptop - 129`
61. Klik thumbnail foto `foto-129-depan.jpg`
62. Verifikasi dialog preview foto terbuka
63. Verifikasi dialog preview foto tidak memuat tombol sebelumnya dan tombol berikutnya

### Aset tanpa foto menampilkan tanda kosong
64. Tampilkan Halaman Approval dengan kondisi K1
65. Klik nama `Laptop - 130`
66. Verifikasi area Photo menampilkan `—`

### Dialog Corrections menampilkan diff koreksi staged
67. Tampilkan Halaman Approval dengan kondisi K1
68. Klik Badge Corrections `1` pada baris `Laptop - 129`
69. Verifikasi dialog `Corrections` untuk aset `Laptop - 129` terbuka
70. Verifikasi dialog `Corrections` menampilkan nama aset `Laptop - 129`
71. Verifikasi tabel memuat kolom `Field`, `Old Value`, dan `New Value`
72. Verifikasi tabel memuat Field `Model` dengan Old Value `Latitude 5440` dan New Value `Latitude 5450`
73. Verifikasi dialog memuat tombol `[Close]`
74. Verifikasi dialog tidak memuat kontrol untuk mengubah koreksi
75. Klik `[Close]`
76. Verifikasi dialog `Corrections` tertutup

### Koreksi Brand mengosongkan Model
77. Tampilkan Halaman Approval dengan kondisi K1
78. Klik nama `Laptop - 128`
79. Pilih Brand `Lenovo`
80. Verifikasi field `Model` kosong
81. Pilih Model `ThinkPad T14`
82. Verifikasi field `Model` menampilkan `ThinkPad T14`

### Pesan wajib diisi tampil saat Save correction pada Brand dan Model
83. Tampilkan Halaman Approval dengan kondisi K1
84. Klik nama `Laptop - 128`
85. Kosongkan field `Brand`
86. Verifikasi pesan `Brand must not be empty` belum tampil sebelum `[Save correction]` ditekan
87. Klik `[Save correction]`
88. Verifikasi pesan `Brand must not be empty` tampil di bawah field `Brand`
89. Verifikasi pesan `Model must not be empty` tidak tampil untuk field `Model` yang dikosongkan oleh koreksi Brand

### Pesan wajib diisi tampil saat Save correction pada Custom field wajib
90. Tampilkan Halaman Approval dengan kondisi K1
91. Klik nama `Laptop - 128`
92. Kosongkan field `Serial Number`
93. Klik `[Save correction]`
94. Verifikasi pesan `Serial Number must not be empty` tampil di bawah field `Serial Number`

### Damage note wajib bila Condition dikoreksi ke Damaged dan dibuang bila ke Normal
95. Tampilkan Halaman Approval dengan kondisi K1
96. Klik nama `Laptop - 128`
97. Pilih Condition `Damaged`
98. Verifikasi field `Damage note` tampil
99. Klik `[Save correction]`
100. Verifikasi pesan `Damage note must not be empty` tampil di bawah field `Damage note`
101. Isi field `Damage note` dengan `Scratch on the casing`
102. Pilih Condition `Normal`
103. Verifikasi field `Damage note` tidak tampil
104. Pilih Condition `Damaged`
105. Verifikasi field `Damage note` tampil dengan nilai kosong

### Damage note kosong pada aset Damaged ditolak saat Save correction
106. Tampilkan Halaman Approval dengan kondisi K1
107. Klik nama `Laptop - 129`
108. Kosongkan field `Damage note`
109. Klik `[Save correction]`
110. Verifikasi pesan `Damage note must not be empty` tampil di bawah field `Damage note`

### Atribut aksesibilitas field panel koreksi
111. Tampilkan Halaman Approval dengan kondisi K1
112. Klik nama `Laptop - 128`
113. Verifikasi field `Brand` memiliki atribut aria-required
114. Verifikasi field `Serial Number` memiliki atribut aria-required
115. Kosongkan field `Serial Number`
116. Klik `[Save correction]`
117. Verifikasi field `Serial Number` memiliki atribut aria-describedby yang merujuk pesan error di bawahnya

### Label aksesibel pada kontrol icon-only baris aset
118. Tampilkan Halaman Approval dengan kondisi K1
119. Verifikasi row option (titik tiga) pada baris `Laptop - 128` memiliki label aksesibel

### Close tanpa perubahan menutup panel langsung
120. Tampilkan Halaman Approval dengan kondisi K1
121. Klik nama `Laptop - 128`
122. Klik `Close` pada panel
123. Verifikasi panel koreksi tertutup
124. Verifikasi dialog `Unsaved Changes` tidak tampil

### Pindah ke aset lain tanpa perubahan langsung berpindah
125. Tampilkan Halaman Approval dengan kondisi K1
126. Klik nama `Laptop - 128`
127. Klik nama `Laptop - 130`
128. Verifikasi panel menampilkan Custom field `Serial Number` bernilai `SN-130-0001`
129. Verifikasi dialog `Unsaved Changes` tidak tampil

### Close dengan isian belum disimpan memunculkan dialog Unsaved Changes
130. Tampilkan Halaman Approval dengan kondisi K1
131. Klik nama `Laptop - 128`
132. Pilih Brand `Lenovo`
133. Klik `Close` pada panel
134. Verifikasi dialog `Unsaved Changes` tampil
135. Verifikasi isi dialog `You have unsaved changes. Are you sure you want to leave?`
136. Verifikasi dialog memuat tombol `[Cancel]` dan `[Leave]`
137. Klik `[Cancel]` pada dialog `Unsaved Changes`
138. Verifikasi panel koreksi tetap terbuka dengan Brand `Lenovo`

### Leave membuang isian panel
139. Tampilkan Halaman Approval dengan kondisi K1
140. Klik nama `Laptop - 128`
141. Pilih Brand `Lenovo`
142. Klik `Close` pada panel
143. Klik `[Leave]` pada dialog `Unsaved Changes`
144. Verifikasi panel koreksi tertutup
145. Klik nama `Laptop - 128`
146. Verifikasi field `Brand` menampilkan `Dell`

### Esc pada dialog Unsaved Changes setara Cancel
147. Tampilkan Halaman Approval dengan kondisi K1
148. Klik nama `Laptop - 128`
149. Pilih Brand `Lenovo`
150. Klik `Close` pada panel
151. Tekan `Esc`
152. Verifikasi dialog `Unsaved Changes` tertutup
153. Verifikasi panel koreksi tetap terbuka dengan Brand `Lenovo`

### Pindah ke aset lain dengan isian belum disimpan memunculkan dialog Unsaved Changes
154. Tampilkan Halaman Approval dengan kondisi K1
155. Klik nama `Laptop - 128`
156. Pilih Brand `Lenovo`
157. Klik nama `Laptop - 130`
158. Verifikasi dialog `Unsaved Changes` tampil
159. Klik `[Leave]` pada dialog `Unsaved Changes`
160. Verifikasi panel menampilkan Custom field `Serial Number` bernilai `SN-130-0001`

### Clear Field mengosongkan semua field tanpa prompt
161. Tampilkan Halaman Approval dengan kondisi K1
162. Klik nama `Laptop - 128`
163. Verifikasi field `Brand` menampilkan `Dell`
164. Klik `[Clear Field]`
165. Verifikasi field `Brand` kosong
166. Verifikasi field `Model` kosong
167. Verifikasi field `Serial Number` kosong
168. Verifikasi dialog `Unsaved Changes` tidak tampil
169. Verifikasi panel koreksi tetap terbuka

### Saving state saat koreksi disimpan
170. Tampilkan Halaman Approval dengan kondisi K6
171. Klik nama `Laptop - 128`
172. Pilih Brand `Lenovo`
173. Pilih Model `ThinkPad T14`
174. Klik `[Save correction]`
175. Verifikasi tombol `[Save correction]` menampilkan loading dan disabled
176. Verifikasi seluruh field panel disabled
177. Verifikasi tombol `[Clear Field]` disabled
178. Verifikasi tombol `Close` pada panel disabled
179. Klik `[Save correction]`
180. Respons simpan diterima
181. Verifikasi hanya satu toast sukses `Success, correction has been saved.` tampil

### Koreksi berhasil disimpan sebagai staged dan tampil sebagai diff
182. Tampilkan Halaman Approval dengan kondisi K2
183. Klik nama `Laptop - 128`
184. Pilih Brand `Lenovo`
185. Pilih Model `ThinkPad T14`
186. Klik `[Save correction]`
187. Verifikasi toast sukses `Success, correction has been saved.`
188. Verifikasi Badge Corrections pada baris `Laptop - 128` menampilkan `2`
189. Klik Badge Corrections `2` pada baris `Laptop - 128`
190. Verifikasi tabel dialog `Corrections` memuat Field `Brand` dengan Old Value `Dell` dan New Value `Lenovo`
191. Verifikasi tabel dialog `Corrections` memuat Field `Model` dengan Old Value `Latitude 5440` dan New Value `ThinkPad T14`

### Koreksi gagal disimpan karena error server
192. Tampilkan Halaman Approval dengan kondisi K3
193. Klik nama `Laptop - 128`
194. Pilih Brand `Lenovo`
195. Pilih Model `ThinkPad T14`
196. Klik `[Save correction]`
197. Verifikasi toast error `Error, failed to save correction.`
198. Verifikasi panel koreksi tetap terbuka
199. Verifikasi field `Brand` menampilkan `Lenovo` dan field `Model` menampilkan `ThinkPad T14`
200. Verifikasi tombol `[Save correction]` aktif lagi

### Koreksi gagal disimpan karena koneksi terputus
201. Tampilkan Halaman Approval dengan kondisi K4
202. Klik nama `Laptop - 128`
203. Pilih Brand `Lenovo`
204. Pilih Model `ThinkPad T14`
205. Klik `[Save correction]`
206. Verifikasi toast error `Connection problem. Please try again.`
207. Verifikasi panel koreksi tetap terbuka dengan Brand `Lenovo` dan Model `ThinkPad T14`
208. Verifikasi tombol `[Save correction]` aktif lagi

### Simpan ulang sesudah pulih berhasil sekali
209. Tampilkan Halaman Approval dengan kondisi K5
210. Klik nama `Laptop - 128`
211. Pilih Brand `Lenovo`
212. Pilih Model `ThinkPad T14`
213. Klik `[Save correction]`
214. Verifikasi toast error `Error, failed to save correction.`
215. Klik `[Save correction]`
216. Verifikasi toast sukses `Success, correction has been saved.`
217. Verifikasi hanya satu toast sukses koreksi yang tampil

### Pilihan panel yang menjadi tidak valid karena master berubah
218. Tampilkan Halaman Approval dengan kondisi K7
219. Klik nama `Laptop - 128`
220. Verifikasi field `Brand` menampilkan `Dell`
221. Verifikasi field `Model` dikosongkan
222. Verifikasi pesan `Select Model again` tampil di bawah field `Model`
223. Klik `[Save correction]`
224. Verifikasi pesan `Select Model again` tetap tampil
225. Verifikasi toast sukses `Success, correction has been saved.` tidak tampil

### Esc pada panel bersih menutup panel langsung
226. Tampilkan Halaman Approval dengan kondisi K1
227. Klik nama `Laptop - 128`
228. Tekan `Esc`
229. Verifikasi panel koreksi tertutup
230. Verifikasi dialog `Unsaved Changes` tidak tampil

### Esc pada panel dengan isian belum disimpan memunculkan dialog Unsaved Changes
231. Tampilkan Halaman Approval dengan kondisi K1
232. Klik nama `Laptop - 128`
233. Pilih Brand `Lenovo`
234. Tekan `Esc`
235. Verifikasi dialog `Unsaved Changes` tampil

### Data read-only panel koreksi berada di atas field koreksi tanpa judul blok
236. Tampilkan Halaman Approval dengan kondisi K1
237. Klik nama `Laptop - 128`
238. Verifikasi field koreksi `Brand` tampil
239. Verifikasi Photo, Alias Name `Laptop Kasir, Laptop Cadangan`, dan Asset labels `Aset Kantor` dan `Prioritas` tampil sebagai data read-only, tidak ada field input untuk ketiganya
240. Verifikasi Photo, Alias Name, dan Asset labels berada di atas field koreksi `Brand`
241. Verifikasi data read-only tidak memiliki judul blok

### Row option Edit pada aset lain dengan isian belum disimpan memunculkan dialog Unsaved Changes
242. Tampilkan Halaman Approval dengan kondisi K1
243. Klik nama `Laptop - 128`
244. Pilih Brand `Lenovo`
245. Klik row option (titik tiga) pada baris `Laptop - 130`
246. Klik `Edit`
247. Verifikasi dialog `Unsaved Changes` tampil
248. Klik `[Leave]` pada dialog `Unsaved Changes`
249. Verifikasi panel menampilkan Custom field `Serial Number` bernilai `SN-130-0001`

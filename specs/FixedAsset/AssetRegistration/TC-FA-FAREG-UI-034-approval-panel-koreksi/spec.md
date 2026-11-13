---
id: TC-FA-FAREG-UI-034-approval-panel-koreksi
title: "Halaman Approval: panel koreksi approver, dialog Corrections, dan preview foto"
layer: ui-client
priority: High
caseType: Positive
status: draft
sourceRules: [D-REG-20, D-REG-21, D-REG-25, F-FAREG-07, FAREG-LOGIC-07a, FAREG-LOGIC-07b, FAREG-LOGIC-07c, FAREG-LOGIC-07d, FAREG-LOGIC-07h, FAREG-LOGIC-07i, FAREG-LOGIC-15e, FAREG-LOGIC-17c, FI-REG-19, FI-REG-20, FI-REG-21, FI-REG-22, T-REG-11, T-REG-12, T-REG-13, §4.1#r11, §4.1#r18, §4.1#r20, §4.1#b31, §4.2.4#b3, §4.2.4#b7, §4.2.4#b11, §9.6#r11, §9.9#p3, EB-ERR-1@simpan-koreksi, EB-FB-1@simpan-koreksi, EB-FRM-1@panel-koreksi, EB-FRM-2@panel-koreksi, EB-FRM-3@panel-koreksi, EB-FRM-7@panel-koreksi]
smoke: []
dependsOn: []
trace:
  D-REG-20: [67, 68, 69, 71, 74]
  D-REG-21: [132, 133, 134, 156]
  D-REG-25: [45, 46, 47, 53, 61]
  F-FAREG-07: [186, 188, 189]
  FAREG-LOGIC-07a: [22, 23, 24, 25, 31, 32]
  FAREG-LOGIC-07b: [36, 37, 38]
  FAREG-LOGIC-07c: 39
  FAREG-LOGIC-07d: [70, 186, 188, 189]
  FAREG-LOGIC-07h: [78, 80]
  FAREG-LOGIC-07i: [86, 87, 92, 96, 98, 101, 103, 108]
  FAREG-LOGIC-15e: 39
  FAREG-LOGIC-17c: [6, 16]
  FI-REG-19: [132, 136, 142, 144, 156, 158]
  FI-REG-20: [121, 122, 126, 127]
  FI-REG-21: [220, 221, 223, 224]
  FI-REG-22: [45, 46, 47, 61]
  T-REG-11: [179, 185, 214]
  T-REG-12: [195, 212]
  T-REG-13: 204
  §4.1#r11: [19, 20, 21, 22, 23, 24, 25, 26, 27, 32]
  §4.1#r18: [45, 46, 47]
  §4.1#r20: [67, 69]
  §4.1#b31: [27, 28]
  §4.2.4#b3: [67, 69, 72]
  §4.2.4#b7: [3, 6, 9, 11, 13, 16]
  §4.2.4#b11: [42, 43, 64]
  §9.6#r11: [185, 195]
  §9.9#p3: [84, 86, 92, 98]
  EB-ERR-1@simpan-koreksi: [196, 197, 198, 204, 205, 206, 215]
  EB-FB-1@simpan-koreksi: [185, 195]
  EB-FRM-1@panel-koreksi: [173, 174, 175, 176, 179]
  EB-FRM-2@panel-koreksi: [121, 132, 136, 150, 151]
  EB-FRM-3@panel-koreksi: [163, 164, 165, 166, 167]
  EB-FRM-7@panel-koreksi: [48, 49, 51, 55, 56, 111, 112, 115, 117]
anchor: [2, 35, 60, 161, 218]
coverage:
  web: automated
---
# Halaman Approval: panel koreksi approver, dialog Corrections, dan preview foto

## Prerequisites
- Aktor: Dewi A (approver, role Group Manager, cakupan Group binaan + sub-group termasuk Gudang 1, bukan pengaju pengajuan), dan pengguna lain dengan hak mengelola master Brand dan Model yang memicu perubahan master.
- Layar awal: Halaman Approval pengajuan yang dibuka dari antrean Approvals tab Active.
- Komponen: Halaman Approval
- Data:
  - DU-034-1: pengajuan Registration ID `REG-20261109-00003`, Status `Waiting for Approval`, Group `Gudang 1`, Requested By `Rina W`, Total Asset `4`.
  - DU-034-2: aset Name `Laptop - 128`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason; di panel koreksi: Photo `foto-128-depan.jpg` lalu `foto-128-samping.jpg`, Alias Name `Laptop Kasir, Laptop Cadangan`, Asset labels `Aset Kantor` dan `Prioritas`, Custom field `Serial Number` bernilai `SN-128-0001`.
  - DU-034-3: aset Name `Laptop - 129`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Skipped`, Condition `Damaged`, Damage note `Scratch on the casing`, Corrections `1`, Decision `Return to Draft`, Reason `Photo is missing`; di panel koreksi: Photo `foto-129-depan.jpg`, Alias Name `Laptop Staf`, Asset labels `Aset Kantor`, Custom field `Serial Number` bernilai `SN-129-0001`; koreksi staged Field `Model`, Old Value `Latitude 5440`, New Value `Latitude 5450`.
  - DU-034-4: aset Name `Laptop - 130`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason; di panel koreksi: tanpa Photo, Alias Name `Laptop Gudang`, Asset labels `Prioritas`, Custom field `Serial Number` bernilai `SN-130-0001`.
  - DU-034-5: aset Name `Office Desk - 12`, Category `Furniture`, Brand `Kayu Jati`, Model `No Model`, Group `Gudang 1`, TAG `No tag`, Condition `Normal`, Corrections `—`, Decision `Reject`, Reason `Duplicate entry`.
  - DU-034-6: master Brand `Lenovo` dengan Model `ThinkPad T14`, di samping Brand `Dell` dengan Model `Latitude 5440` dan `Latitude 5450`.
  - Pesan yang diharapkan saat pilihan Model tidak valid `Select Model again`, dari template `Select [Field Name] again` dan Field Name `Model`.
- Kondisi:
  - K1: pengajuan DU-034-1 berisi aset DU-034-2, DU-034-3, dan DU-034-4 dalam grup Accordion `Laptop` dan DU-034-5 dalam grup Accordion `Office Desk`, master DU-034-6 tersedia, dan approver berhak memutuskan.
  - K2: seperti K1, dan menyimpan koreksi berhasil.
  - K3: seperti K1, dan menyimpan koreksi gagal karena error server.
  - K4: seperti K1, dan menyimpan koreksi gagal karena koneksi terputus.
  - K5: seperti K1, dan menyimpan koreksi gagal karena error server pada percobaan pertama, lalu berhasil pada percobaan kedua.
  - K6: seperti K1, dan menyimpan koreksi lambat sehingga respons belum diterima sesudah `[Save correction]` diklik.

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
10. Klik row option (titik tiga) pada baris `Laptop - 129`
11. Verifikasi pilihan `Edit` aktif pada baris `Laptop - 129` dengan Decision `Return to Draft`
12. Klik row option (titik tiga) pada baris `Office Desk - 12`
13. Verifikasi pilihan `Edit` aktif pada baris `Office Desk - 12` dengan Decision `Reject`

### Panel koreksi dibuka lewat link Name
14. Tampilkan Halaman Approval dengan kondisi K1
15. Klik nama `Laptop - 130`
16. Verifikasi panel koreksi terbuka

### Isi panel koreksi: data read-only, field koreksi, dan footer
17. Tampilkan Halaman Approval dengan kondisi K1
18. Klik nama `Laptop - 128`
19. Verifikasi panel memuat Photo sebagai thumbnail
20. Verifikasi panel memuat Alias Name `Laptop Kasir, Laptop Cadangan` sebagai teks dipisah koma
21. Verifikasi panel memuat Asset labels `Aset Kantor` dan `Prioritas`
22. Verifikasi panel memuat field koreksi `Brand`
23. Verifikasi panel memuat field koreksi `Model`
24. Verifikasi panel memuat field koreksi `Condition`
25. Verifikasi section Custom fields memuat field koreksi `Serial Number`
26. Verifikasi panel memuat tombol `[Clear Field]`
27. Verifikasi panel memuat tombol `[Save correction]`
28. Verifikasi panel tidak memuat tombol `[Save draft]`

### Damage note tampil pada aset Condition Damaged
29. Tampilkan Halaman Approval dengan kondisi K1
30. Klik nama `Laptop - 129`
31. Verifikasi panel memuat field koreksi `Condition` bernilai `Damaged`
32. Verifikasi panel memuat field koreksi `Damage note`

### Field yang tidak dapat dikoreksi tidak ada di panel
33. Tampilkan Halaman Approval dengan kondisi K1
34. Klik nama `Laptop - 128`
35. Verifikasi panel memuat field koreksi `Brand`
36. Verifikasi panel tidak memuat field koreksi `Asset Name`
37. Verifikasi panel tidak memuat field koreksi `Category`
38. Verifikasi panel tidak memuat field koreksi `Group`
39. Verifikasi panel tidak memuat field data `Purchase`

### Preview foto dengan dua foto
40. Tampilkan Halaman Approval dengan kondisi K1
41. Klik nama `Laptop - 128`
42. Verifikasi panel memuat dua thumbnail foto
43. Verifikasi urutan thumbnail foto `foto-128-depan.jpg` lalu `foto-128-samping.jpg`
44. Klik thumbnail foto `foto-128-depan.jpg`
45. Verifikasi dialog preview foto terbuka
46. Verifikasi dialog preview foto memuat tombol sebelumnya
47. Verifikasi dialog preview foto memuat tombol berikutnya
48. Verifikasi tombol sebelumnya dan tombol berikutnya memiliki label aksesibel
49. Verifikasi fokus berada di dalam dialog preview foto
50. Tekan Tab berulang kali
51. Verifikasi fokus tetap berada di dalam dialog preview foto
52. Klik tombol berikutnya
53. Verifikasi preview menampilkan foto `foto-128-samping.jpg`
54. Tekan `Esc`
55. Verifikasi dialog preview foto tertutup
56. Verifikasi fokus kembali ke thumbnail foto `foto-128-depan.jpg`

### Preview foto dengan satu foto
57. Tampilkan Halaman Approval dengan kondisi K1
58. Klik nama `Laptop - 129`
59. Klik thumbnail foto `foto-129-depan.jpg`
60. Verifikasi dialog preview foto terbuka
61. Verifikasi dialog preview foto tidak memuat tombol sebelumnya dan tombol berikutnya

### Aset tanpa foto menampilkan tanda kosong
62. Tampilkan Halaman Approval dengan kondisi K1
63. Klik nama `Laptop - 130`
64. Verifikasi area Photo menampilkan `—`

### Dialog Corrections menampilkan diff koreksi staged
65. Tampilkan Halaman Approval dengan kondisi K1
66. Klik Badge Corrections `1` pada baris `Laptop - 129`
67. Verifikasi dialog `Corrections` untuk aset `Laptop - 129` terbuka
68. Verifikasi baris di bawah judul dialog memuat `Laptop - 129`
69. Verifikasi tabel memuat kolom `Field`, `Old Value`, dan `New Value`
70. Verifikasi tabel memuat Field `Model` dengan Old Value `Latitude 5440` dan New Value `Latitude 5450`
71. Verifikasi dialog memuat tombol `[Close]`
72. Verifikasi dialog tidak memuat kontrol untuk mengubah koreksi
73. Klik `[Close]`
74. Verifikasi dialog `Corrections` tertutup

### Koreksi Brand mengosongkan Model
75. Tampilkan Halaman Approval dengan kondisi K1
76. Klik nama `Laptop - 128`
77. Pilih Brand `Lenovo`
78. Verifikasi field `Model` kosong
79. Pilih Model `ThinkPad T14`
80. Verifikasi field `Model` menampilkan `ThinkPad T14`

### Pesan wajib diisi tampil saat Save correction pada Brand dan Model
81. Tampilkan Halaman Approval dengan kondisi K1
82. Klik nama `Laptop - 128`
83. Kosongkan field `Brand`
84. Verifikasi pesan `Brand must not be empty` belum tampil sebelum `[Save correction]` ditekan
85. Klik `[Save correction]`
86. Verifikasi pesan `Brand must not be empty` tampil di bawah field `Brand`
87. Verifikasi pesan `Model must not be empty` tidak tampil untuk field `Model` yang dikosongkan oleh koreksi Brand

### Pesan wajib diisi tampil saat Save correction pada Custom field wajib
88. Tampilkan Halaman Approval dengan kondisi K1
89. Klik nama `Laptop - 128`
90. Kosongkan field `Serial Number`
91. Klik `[Save correction]`
92. Verifikasi pesan `Serial Number must not be empty` tampil di bawah field `Serial Number`

### Damage note wajib bila Condition dikoreksi ke Damaged dan dibuang bila ke Normal
93. Tampilkan Halaman Approval dengan kondisi K1
94. Klik nama `Laptop - 128`
95. Pilih Condition `Damaged`
96. Verifikasi field `Damage note` tampil
97. Klik `[Save correction]`
98. Verifikasi pesan `Damage note must not be empty` tampil di bawah field `Damage note`
99. Isi field `Damage note` dengan `Scratch on the casing`
100. Pilih Condition `Normal`
101. Verifikasi field `Damage note` tidak tampil
102. Pilih Condition `Damaged`
103. Verifikasi field `Damage note` tampil dengan nilai kosong

### Damage note kosong pada aset Damaged ditolak saat Save correction
104. Tampilkan Halaman Approval dengan kondisi K1
105. Klik nama `Laptop - 129`
106. Kosongkan field `Damage note`
107. Klik `[Save correction]`
108. Verifikasi pesan `Damage note must not be empty` tampil di bawah field `Damage note`

### Atribut aksesibilitas field panel koreksi
109. Tampilkan Halaman Approval dengan kondisi K1
110. Klik nama `Laptop - 128`
111. Verifikasi field `Brand` memiliki atribut aria-required
112. Verifikasi field `Serial Number` memiliki atribut aria-required
113. Kosongkan field `Serial Number`
114. Klik `[Save correction]`
115. Verifikasi field `Serial Number` memiliki atribut aria-describedby yang merujuk pesan error di bawahnya

### Label aksesibel pada kontrol icon-only baris aset
116. Tampilkan Halaman Approval dengan kondisi K1
117. Verifikasi row option (titik tiga) pada baris `Laptop - 128` memiliki label aksesibel

### Close tanpa perubahan menutup panel langsung
118. Tampilkan Halaman Approval dengan kondisi K1
119. Klik nama `Laptop - 128`
120. Klik `Close` pada panel
121. Verifikasi panel koreksi tertutup
122. Verifikasi dialog `Unsaved Changes` tidak tampil

### Pindah ke aset lain tanpa perubahan langsung berpindah
123. Tampilkan Halaman Approval dengan kondisi K1
124. Klik nama `Laptop - 128`
125. Klik nama `Laptop - 130`
126. Verifikasi panel menampilkan Custom field `Serial Number` bernilai `SN-130-0001`
127. Verifikasi dialog `Unsaved Changes` tidak tampil

### Close dengan isian belum disimpan memunculkan dialog Unsaved Changes
128. Tampilkan Halaman Approval dengan kondisi K1
129. Klik nama `Laptop - 128`
130. Pilih Brand `Lenovo`
131. Klik `Close` pada panel
132. Verifikasi dialog `Unsaved Changes` tampil
133. Verifikasi isi dialog `You have unsaved changes. Are you sure you want to leave?`
134. Verifikasi dialog memuat tombol `[Cancel]` dan `[Leave]`
135. Klik `[Cancel]` pada dialog `Unsaved Changes`
136. Verifikasi panel koreksi tetap terbuka dengan Brand `Lenovo`

### Leave membuang isian panel
137. Tampilkan Halaman Approval dengan kondisi K1
138. Klik nama `Laptop - 128`
139. Pilih Brand `Lenovo`
140. Klik `Close` pada panel
141. Klik `[Leave]` pada dialog `Unsaved Changes`
142. Verifikasi panel koreksi tertutup
143. Klik nama `Laptop - 128`
144. Verifikasi field `Brand` menampilkan `Dell`

### Esc pada dialog Unsaved Changes setara Cancel
145. Tampilkan Halaman Approval dengan kondisi K1
146. Klik nama `Laptop - 128`
147. Pilih Brand `Lenovo`
148. Klik `Close` pada panel
149. Tekan `Esc`
150. Verifikasi dialog `Unsaved Changes` tertutup
151. Verifikasi panel koreksi tetap terbuka dengan Brand `Lenovo`

### Pindah ke aset lain dengan isian belum disimpan memunculkan dialog Unsaved Changes
152. Tampilkan Halaman Approval dengan kondisi K1
153. Klik nama `Laptop - 128`
154. Pilih Brand `Lenovo`
155. Klik nama `Laptop - 130`
156. Verifikasi dialog `Unsaved Changes` tampil
157. Klik `[Leave]` pada dialog `Unsaved Changes`
158. Verifikasi panel menampilkan Custom field `Serial Number` bernilai `SN-130-0001`

### Clear Field mengosongkan semua field tanpa prompt
159. Tampilkan Halaman Approval dengan kondisi K1
160. Klik nama `Laptop - 128`
161. Verifikasi field `Brand` menampilkan `Dell`
162. Klik `[Clear Field]`
163. Verifikasi field `Brand` kosong
164. Verifikasi field `Model` kosong
165. Verifikasi field `Serial Number` kosong
166. Verifikasi dialog `Unsaved Changes` tidak tampil
167. Verifikasi panel koreksi tetap terbuka

### Saving state saat koreksi disimpan
168. Tampilkan Halaman Approval dengan kondisi K6
169. Klik nama `Laptop - 128`
170. Pilih Brand `Lenovo`
171. Pilih Model `ThinkPad T14`
172. Klik `[Save correction]`
173. Verifikasi tombol `[Save correction]` menampilkan loading dan disabled
174. Verifikasi seluruh field panel disabled
175. Verifikasi tombol `[Clear Field]` disabled
176. Verifikasi tombol `Close` pada panel disabled
177. Klik `[Save correction]`
178. Respons simpan diterima
179. Verifikasi hanya satu toast sukses `Success, correction has been saved.` tampil

### Koreksi berhasil disimpan sebagai staged dan tampil sebagai diff
180. Tampilkan Halaman Approval dengan kondisi K2
181. Klik nama `Laptop - 128`
182. Pilih Brand `Lenovo`
183. Pilih Model `ThinkPad T14`
184. Klik `[Save correction]`
185. Verifikasi toast sukses `Success, correction has been saved.`
186. Verifikasi Badge Corrections pada baris `Laptop - 128` menampilkan `2`
187. Klik Badge Corrections `2` pada baris `Laptop - 128`
188. Verifikasi tabel dialog `Corrections` memuat Field `Brand` dengan Old Value `Dell` dan New Value `Lenovo`
189. Verifikasi tabel dialog `Corrections` memuat Field `Model` dengan Old Value `Latitude 5440` dan New Value `ThinkPad T14`

### Koreksi gagal disimpan karena error server
190. Tampilkan Halaman Approval dengan kondisi K3
191. Klik nama `Laptop - 128`
192. Pilih Brand `Lenovo`
193. Pilih Model `ThinkPad T14`
194. Klik `[Save correction]`
195. Verifikasi toast error `Error, failed to save correction.`
196. Verifikasi panel koreksi tetap terbuka
197. Verifikasi field `Brand` menampilkan `Lenovo` dan field `Model` menampilkan `ThinkPad T14`
198. Verifikasi tombol `[Save correction]` aktif lagi

### Koreksi gagal disimpan karena koneksi terputus
199. Tampilkan Halaman Approval dengan kondisi K4
200. Klik nama `Laptop - 128`
201. Pilih Brand `Lenovo`
202. Pilih Model `ThinkPad T14`
203. Klik `[Save correction]`
204. Verifikasi toast error `Connection problem. Please try again.`
205. Verifikasi panel koreksi tetap terbuka dengan Brand `Lenovo` dan Model `ThinkPad T14`
206. Verifikasi tombol `[Save correction]` aktif lagi

### Simpan ulang sesudah pulih berhasil sekali
207. Tampilkan Halaman Approval dengan kondisi K5
208. Klik nama `Laptop - 128`
209. Pilih Brand `Lenovo`
210. Pilih Model `ThinkPad T14`
211. Klik `[Save correction]`
212. Verifikasi toast error `Error, failed to save correction.`
213. Klik `[Save correction]`
214. Verifikasi toast sukses `Success, correction has been saved.`
215. Verifikasi hanya satu toast sukses koreksi yang tampil

### Pilihan panel yang menjadi tidak valid karena master berubah
216. Tampilkan Halaman Approval dengan kondisi K1
217. Klik nama `Laptop - 128`
218. Verifikasi field `Model` menampilkan `Latitude 5440`
219. Pengguna lain menghapus Model `Latitude 5440` dari master
220. Verifikasi field `Model` dikosongkan
221. Verifikasi pesan `Select Model again` tampil di bawah field `Model`
222. Klik `[Save correction]`
223. Verifikasi pesan `Select Model again` tetap tampil
224. Verifikasi toast sukses `Success, correction has been saved.` tidak tampil

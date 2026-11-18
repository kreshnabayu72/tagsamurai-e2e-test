---
id: TC-FA-ASTL-E2E-006-filter-panel
title: "Panel Filter pada tabel All Assets"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [ASTL-LOGIC-02b, ASTL-LOGIC-02e, F-ASTL-04, FLD-01, FLD-02, FLD-03, FLD-04, FLD-05, FLD-06, FLD-07, FLD-08, FLD-09, FLD-10, FLD-11, FLD-12, FLD-13, FLD-14, FLD-15, FLD-16, FLD-17, FLD-18, FLD-19, FLD-20, FLD-21, FLD-22, FLD-23, FLD-24, FLD-25, FLD-26, "§4.1a#b3", "§4.1c#b1", "§4.1c#b2", "§4.1c#b4", "EB-FLT-1@tabel-all-assets", "EB-FLT-4@tabel-all-assets", "EB-FLT-5@tabel-all-assets", EB-FLT-3]
smoke: [EB-FLT-3]
dependsOn: []
trace:
  ASTL-LOGIC-02b: [91, 92, 95, 96, 99, 104, 105, 324, 327, 330, 336, 342, 337, 343]
  ASTL-LOGIC-02e: [110, 111, 330, 331]
  F-ASTL-04: [6, 9]
  FLD-01: 7
  FLD-02: [37, 38, 266]
  FLD-03: 7
  FLD-04: 7
  FLD-05: [43, 44, 267]
  FLD-06: [11, 12, 241, 242]
  FLD-07: [49, 50, 268, 287, 286]
  FLD-08: [55, 56, 269]
  FLD-09: [86, 87, 270]
  FLD-10: 7
  FLD-11: [21, 31, 271]
  FLD-12: [73, 74, 80, 272]
  FLD-13: [91, 104, 273, 372, 377]
  FLD-14: [161, 274, 295]
  FLD-15: [166, 275, 305, 306]
  FLD-16: [61, 62, 276]
  FLD-17: [67, 68, 277, 291, 290]
  FLD-18: [210, 211, 278, 312, 313]
  FLD-19: [210, 211, 279, 319, 320]
  FLD-20: [124, 125, 130, 131, 136, 137, 142, 143, 148, 206, 280]
  FLD-21: [172, 173, 179, 180, 185, 186, 191, 192, 198, 203, 206, 281]
  FLD-22: [154, 155, 282]
  FLD-23: 7
  FLD-24: [256, 283, 348]
  FLD-25: [161, 284, 300]
  FLD-26: [216, 217]
  "§4.1a#b3": [117, 118]
  "§4.1c#b1": [91, 324, 327, 330, 336, 342]
  "§4.1c#b2": [73, 80, 81]
  "§4.1c#b4": [216, 217]
  "EB-FLT-1@tabel-all-assets": [26, 251, 254]
  "EB-FLT-4@tabel-all-assets": [151, 223, 224, 227, 232, 235, 241, 249, 256, 262, 359, 360, 361, 365, 366, 349, 357, 385, 388]
  "EB-FLT-5@tabel-all-assets": [27, 32]
  EB-FLT-3: [15, 21, 22, 124, 172]
anchor: [4, 378]
coverage:
  web: automated
---

# Panel Filter pada tabel All Assets

## Prerequisites
- Aktor: Total Control `Faisal Akbar {runId}`, dan Total Control `Retno Utami {runId}` sebagai aktor lain yang hanya memicu perubahan.
- Layar awal: Fixed Asset > Assets (tab `Assets`).
- Data:
  - DU-006-1: User `Faisal Akbar {runId}`, role Total Control, cakupan seluruh client, dan pengubah terakhir seluruh aset di bawah.
  - DU-006-2: User `Retno Utami {runId}`, role Total Control, cakupan seluruh client, belum pernah mengubah aset mana pun.
  - DU-006-3: Custom field aktif `Lokasi Rak {runId}` bertipe teks pada grup General.
  - DU-006-4: Aset `Printer Epson - 1 {runId}`: Asset Name `Printer Epson`, TAG `QR`, Brand `Epson`, Model / Type `L3250`, Measurement `Unit`, Category `Printer`, Division `Finance`, Labels `Aset Kantor`, berstatus `Available`, Asset Class `Kelas A`, Tax Depreciation Class `Pajak 1`, Purchase Date `T0 - 30 hari`, Purchase Cost `2500000`, dan satu garansi berakhir `T0 + 20 hari`.
  - DU-006-5: Aset `Printer Epson - 2 {runId}`: Asset Name `Printer Epson`, TAG `RFID`, Brand `Epson`, Model / Type `L3250`, Measurement `Set`, Category `Printer`, Division `Operations`, Labels `Aset Kantor` dan `Prioritas`, berstatus `Available`, Asset Class `Kelas A`, Tax Depreciation Class `Pajak 2`, Purchase Date `T0 - 60 hari`, Purchase Cost `900000`, dan satu garansi berakhir `T0 + 400 hari`.
  - DU-006-6: Aset `Printer Canon - 1 {runId}`: Asset Name `Printer Canon`, TAG `QR`, Brand `Canon`, Model / Type `Pixma G3020`, Measurement `Unit`, Category `Kamera`, Division `Finance`, Labels `Prioritas`, berstatus `Available`, Asset Class `Kelas B`, tanpa Tax Depreciation Class, Purchase Date `T0 - 90 hari`, Purchase Cost `10000000`, dan Last Scanned `T0 - 3 hari` (pemindaian terbaru pada Audit).
  - DU-006-7: Aset `Printer Canon - 2 {runId}`: Asset Name `Printer Canon`, TAG `RFID`, Brand `Canon`, Model / Type `Pixma G3020`, Measurement `Set`, Category `Kamera`, Division `Operations`, tanpa Labels, berstatus `Available`, tanpa Asset Class, Tax Depreciation Class `Pajak 1`, Purchase Date `T0 - 10 hari`, dan Purchase Cost `15000000`.
  - DU-006-8: Aset `Laptop Lenovo - 1 {runId}`: Asset Name `Laptop Lenovo`, Brand `Lenovo`, Model / Type `No Model` (default sistem untuk Brand tanpa model), tanpa Division, berstatus `Available`, Purchase Date dan Purchase Cost belum diisi (Purchase status `Pending`).
  - DU-006-9: Aset `Perangkat Uji - 6 {runId}`: berstatus `Borrowed`, Purchase Date `T0 - 5 hari`, dan Purchase Cost `5000000`.
  - DU-006-10: Aset `Perangkat Uji - 7 {runId}`: berstatus `Assigned`, Purchase Date `T0 - 5 hari`, dan Purchase Cost `5000000`.
  - DU-006-11: Aset `Perangkat Uji - 8 {runId}`: berstatus `Borrowed + Damaged`, Purchase Date `T0 - 5 hari`, dan Purchase Cost `5000000`.
  - DU-006-12: Aset `Perangkat Uji - 9 {runId}`: berstatus `Unmanaged + Available`, Purchase Date `T0 - 5 hari`, dan Purchase Cost `5000000`.
  - DU-006-13: Aset `Perangkat Uji - 10 {runId}`: berstatus `Not Paired Yet`, Purchase Date `T0 - 5 hari`, dan Purchase Cost `5000000`.
  - DU-006-20: Aset `Perangkat Uji - 11 {runId}`: berpenanda lisensi `Pending Activation`, Purchase Date `T0 - 5 hari`, dan Purchase Cost `5000000`.
  - DU-006-21: Aset `Perangkat Uji - 12 {runId}`: Tagging `TAG Reported`, Purchase Date `T0 - 5 hari`, dan Purchase Cost `5000000`.
  - DU-006-22: Aset `Perangkat Uji - 13 {runId}`: Activity Lock `In Audit`, Purchase Date `T0 - 5 hari`, dan Purchase Cost `5000000`.
  - DU-006-24: Aset `Perangkat Uji - 15 {runId}`: berstatus `Damaged + Missing`, Purchase Date `T0 - 5 hari`, dan Purchase Cost `5000000`.
  - DU-006-25: Aset `Printer Canon - 3 {runId}`: Asset Name `Printer Canon`, Brand `Canon`, dibuat oleh `Retno Utami {runId}` saat Filter Brand `Epson` aktif.
  - DU-006-26: Aset `Printer Epson - 3 {runId}`: Asset Name `Printer Epson`, Brand `Epson`, dibuat oleh `Retno Utami {runId}` saat Filter Brand `Epson` aktif.
  - DU-006-23: Aset `Perangkat Uji - 14 {runId}`: Tagging `TAG Reported` dan Activity Lock `In Audit`, Purchase Date `T0 - 5 hari`, dan Purchase Cost `5000000`.
  - Aset DU-006-4 sampai DU-006-7 tanpa Additional costs dan tanpa periode penyusutan Posted, sehingga Asset Value (Commercial) dan Asset Value (Fiscal) sama dengan Purchase Cost pada aset yang punya Asset Class dan Purchase Cost, dan `Pending` pada aset tanpa Asset Class.
  - Dengan Search memakai runId spec ini sebagai saringan dasar, tabel hanya memuat aset spec ini; Search itu tetap aktif sampai diganti.
- Kondisi:
  - Akun `Faisal Akbar {runId}` dan `Retno Utami {runId}` aktif dan kredensialnya tersedia.
  - Date Format bernilai `dd/MM/yy`.

## Test Steps

### Filter Panel terbuka dan field yang tersedia
1. Masuk sebagai `Faisal Akbar {runId}`
2. Klik menu `Fixed Asset > Assets` pada sidebar
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi baris `Printer Epson - 1 {runId}` dan `Printer Epson - 2 {runId}` dan `Printer Canon - 1 {runId}` dan `Printer Canon - 2 {runId}` dan `Laptop Lenovo - 1 {runId}` tampil
5. Klik ikon Filter
6. Verifikasi Filter Panel terbuka dengan tombol `[Clear Field]` dan `[Apply]`
7. Verifikasi Filter Panel tidak memuat field untuk kolom `Photo`, `Alias Name`, `Asset ID`, dan `Group`, serta tidak memuat field `Lokasi Rak {runId}`

### Multi-select: cocok, tidak cocok, dan OR dalam satu field
8. Pilih Brand `Epson` pada Filter Panel
9. Verifikasi tabel belum berubah sebelum `[Apply]` diklik dan tetap memuat `Printer Canon - 1 {runId}` dan `Printer Canon - 2 {runId}`
10. Klik `[Apply]`
11. Verifikasi tabel memuat `Printer Epson - 1 {runId}` dan `Printer Epson - 2 {runId}` yang Brand-nya `Epson`
12. Verifikasi tabel tidak memuat `Printer Canon - 1 {runId}` dan `Printer Canon - 2 {runId}` dan `Laptop Lenovo - 1 {runId}` yang Brand-nya bukan `Epson`
13. Pilih Brand `Canon` pada Filter Panel
14. Klik `[Apply]`
15. Verifikasi tabel memuat `Printer Epson - 1 {runId}` dan `Printer Epson - 2 {runId}` dan `Printer Canon - 1 {runId}` dan `Printer Canon - 2 {runId}` karena beberapa pilihan dalam satu field digabung OR
16. Klik `[Clear Field]`
17. Klik `[Apply]`

### Dua field berbeda digabung AND
18. Pilih Brand `Epson` pada Filter Panel
19. Pilih Division `Finance` pada Filter Panel
20. Klik `[Apply]`
21. Verifikasi tabel memuat `Printer Epson - 1 {runId}` yang memenuhi Brand `Epson` dan Division `Finance` sekaligus
22. Verifikasi tabel tidak memuat `Printer Epson - 2 {runId}` (hanya Brand `Epson`), `Printer Canon - 1 {runId}` (hanya Division `Finance`), dan `Printer Canon - 2 {runId}` (tidak memenuhi keduanya)
23. Klik `[Clear Field]`
24. Klik `[Apply]`

### Opsi dropdown berasal dari data tabel, dan nilai kosong tidak menjadi opsi
25. Klik field Division pada Filter Panel
26. Verifikasi opsi Division memuat `Finance` dan `Operations` dari data tabel
27. Verifikasi opsi Division tidak memuat nilai kosong
28. Pilih Division `Finance` pada Filter Panel
29. Pilih Division `Operations` pada Filter Panel
30. Klik `[Apply]`
31. Verifikasi tabel memuat `Printer Epson - 1 {runId}` dan `Printer Epson - 2 {runId}` dan `Printer Canon - 1 {runId}` dan `Printer Canon - 2 {runId}`
32. Verifikasi tabel tidak memuat `Laptop Lenovo - 1 {runId}` yang Division-nya kosong karena memilih opsi apa pun menyaring keluar baris kosong
33. Klik `[Clear Field]`
34. Klik `[Apply]`

### Filter per kolom pilihan
35. Pilih `Asset Name` `Printer Canon` pada Filter Panel
36. Klik `[Apply]`
37. Verifikasi tabel memuat `Printer Canon - 1 {runId}` dan `Printer Canon - 2 {runId}` yang bernilai `Printer Canon` pada `Asset Name`
38. Verifikasi tabel tidak memuat `Printer Epson - 1 {runId}`
39. Klik `[Clear Field]`
40. Klik `[Apply]`
41. Pilih `TAG` `RFID` pada Filter Panel
42. Klik `[Apply]`
43. Verifikasi tabel memuat `Printer Epson - 2 {runId}` dan `Printer Canon - 2 {runId}` yang bernilai `RFID` pada `TAG`
44. Verifikasi tabel tidak memuat `Printer Epson - 1 {runId}`
45. Klik `[Clear Field]`
46. Klik `[Apply]`
47. Pilih `Model/Type` `Pixma G3020` pada Filter Panel
48. Klik `[Apply]`
49. Verifikasi tabel memuat `Printer Canon - 1 {runId}` dan `Printer Canon - 2 {runId}` yang bernilai `Pixma G3020` pada `Model/Type`
50. Verifikasi tabel tidak memuat `Printer Epson - 1 {runId}`
51. Klik `[Clear Field]`
52. Klik `[Apply]`
53. Pilih `Measurement` `Set` pada Filter Panel
54. Klik `[Apply]`
55. Verifikasi tabel memuat `Printer Epson - 2 {runId}` dan `Printer Canon - 2 {runId}` yang bernilai `Set` pada `Measurement`
56. Verifikasi tabel tidak memuat `Printer Epson - 1 {runId}`
57. Klik `[Clear Field]`
58. Klik `[Apply]`
59. Pilih `Asset Class` `Kelas B` pada Filter Panel
60. Klik `[Apply]`
61. Verifikasi tabel memuat `Printer Canon - 1 {runId}` yang bernilai `Kelas B` pada `Asset Class`
62. Verifikasi tabel tidak memuat `Printer Epson - 1 {runId}`
63. Klik `[Clear Field]`
64. Klik `[Apply]`
65. Pilih `Tax Depreciation Class` `Pajak 1` pada Filter Panel
66. Klik `[Apply]`
67. Verifikasi tabel memuat `Printer Epson - 1 {runId}` dan `Printer Canon - 2 {runId}` yang bernilai `Pajak 1` pada `Tax Depreciation Class`
68. Verifikasi tabel tidak memuat `Printer Epson - 2 {runId}`
69. Klik `[Clear Field]`
70. Klik `[Apply]`
71. Pilih `Label` `Aset Kantor` pada Filter Panel
72. Klik `[Apply]`
73. Verifikasi tabel memuat `Printer Epson - 1 {runId}` dan `Printer Epson - 2 {runId}` yang bernilai `Aset Kantor` pada `Label`
74. Verifikasi tabel tidak memuat `Printer Canon - 1 {runId}`
75. Klik `[Clear Field]`
76. Klik `[Apply]`
77. Pilih Label `Aset Kantor` pada Filter Panel
78. Pilih Label `Prioritas` pada Filter Panel
79. Klik `[Apply]`
80. Verifikasi tabel memuat `Printer Epson - 1 {runId}` dan `Printer Epson - 2 {runId}` dan `Printer Canon - 1 {runId}` karena beberapa label digabung OR
81. Verifikasi tabel tidak memuat `Printer Canon - 2 {runId}` yang tidak berlabel
82. Klik `[Clear Field]`
83. Klik `[Apply]`
84. Pilih Category `Printer` pada tree picker Filter Panel
85. Klik `[Apply]`
86. Verifikasi tabel memuat `Printer Epson - 1 {runId}` dan `Printer Epson - 2 {runId}` yang Category-nya `Printer`
87. Verifikasi tabel tidak memuat `Printer Canon - 1 {runId}` yang Category-nya `Kamera`
88. Klik `[Clear Field]`
89. Klik `[Apply]`

### Filter Status per dimensi
90. Klik field Status pada Filter Panel
91. Verifikasi opsi Status memuat `Borrowed`, `Assigned`, `Damaged`, `Not Paired Yet`, `Unmanaged`, dan `Available` tanpa awalan nama dimensi
92. Verifikasi opsi Status tidak memuat `Active` dan `Disposed` karena Lifecycle dipilah oleh kartu
93. Pilih Status `Borrowed` pada Filter Panel
94. Klik `[Apply]`
95. Verifikasi tabel memuat `Perangkat Uji - 6 {runId}` dan `Perangkat Uji - 8 {runId}` yang berstatus `Borrowed`
96. Verifikasi tabel tidak memuat `Perangkat Uji - 7 {runId}` yang berstatus `Assigned`
97. Pilih Status `Assigned` pada Filter Panel
98. Klik `[Apply]`
99. Verifikasi tabel memuat `Perangkat Uji - 6 {runId}` dan `Perangkat Uji - 7 {runId}` dan `Perangkat Uji - 8 {runId}` karena nilai dalam satu dimensi Custody digabung OR
100. Klik `[Clear Field]`
101. Pilih Status `Borrowed` pada Filter Panel
102. Pilih Status `Damaged` pada Filter Panel
103. Klik `[Apply]`
104. Verifikasi tabel memuat `Perangkat Uji - 8 {runId}` yang berstatus `Borrowed` dan `Damaged` sekaligus karena dimensi Custody dan Condition digabung AND
105. Verifikasi tabel tidak memuat `Perangkat Uji - 6 {runId}` yang hanya berstatus `Borrowed`
106. Klik `[Clear Field]`
107. Pilih Status `Unmanaged` pada Filter Panel
108. Pilih Status `Available` pada Filter Panel
109. Klik `[Apply]`
110. Verifikasi tabel memuat `Perangkat Uji - 9 {runId}` yang berpenanda `Unmanaged` dan Custody `Available`
111. Verifikasi tabel tidak memuat `Printer Epson - 1 {runId}` yang berstatus `Available` tanpa penanda `Unmanaged`
112. Klik `[Clear Field]`
113. Klik `[Apply]`
114. Klik kartu `In Transaction`
115. Pilih Status `Damaged` pada Filter Panel
116. Klik `[Apply]`
117. Verifikasi tabel memuat `Perangkat Uji - 8 {runId}`
118. Verifikasi tabel tidak memuat `Perangkat Uji - 6 {runId}` dan `Perangkat Uji - 7 {runId}` yang berada di kartu `In Transaction` tetapi tidak berstatus `Damaged`
119. Klik `[Clear Field]`
120. Klik `[Apply]`
121. Klik kartu `All`

### Filter rentang tanggal
122. Isi Purchase Date dengan rentang `T0 - 70 hari` sampai `T0 - 20 hari`
123. Klik `[Apply]`
124. Verifikasi tabel memuat `Printer Epson - 1 {runId}` dan `Printer Epson - 2 {runId}`
125. Verifikasi tabel tidak memuat `Printer Canon - 1 {runId}` dan `Printer Canon - 2 {runId}`
126. Klik `[Clear Field]`
127. Klik `[Apply]`
128. Isi Purchase Date dengan rentang `T0 - 60 hari` sampai `T0 - 40 hari` (batas awal sama dengan tanggal baris)
129. Klik `[Apply]`
130. Verifikasi tabel memuat `Printer Epson - 2 {runId}`
131. Verifikasi tabel tidak memuat `Printer Epson - 1 {runId}`
132. Klik `[Clear Field]`
133. Klik `[Apply]`
134. Isi Purchase Date dengan rentang `T0 - 100 hari` sampai `T0 - 90 hari` (batas akhir sama dengan tanggal baris)
135. Klik `[Apply]`
136. Verifikasi tabel memuat `Printer Canon - 1 {runId}`
137. Verifikasi tabel tidak memuat `Printer Epson - 2 {runId}`
138. Klik `[Clear Field]`
139. Klik `[Apply]`
140. Isi Purchase Date dengan rentang `T0 - 30 hari` sampai `T0 - 30 hari` (Start Date sama dengan End Date)
141. Klik `[Apply]`
142. Verifikasi tabel memuat `Printer Epson - 1 {runId}`
143. Verifikasi tabel tidak memuat `Printer Epson - 2 {runId}` dan `Printer Canon - 2 {runId}`
144. Klik `[Clear Field]`
145. Klik `[Apply]`
146. Isi Purchase Date dengan rentang `T0 - 29 hari` sampai `T0 - 11 hari`
147. Klik `[Apply]`
148. Verifikasi tabel menampilkan empty state `No results found` karena baris pada `T0 - 30 hari` dan `T0 - 10 hari` berada tepat di luar rentang
149. Klik `[Clear Field]`
150. Klik `[Apply]`
151. Verifikasi baris `Printer Epson - 1 {runId}` dan `Printer Epson - 2 {runId}` dan `Printer Canon - 1 {runId}` dan `Printer Canon - 2 {runId}` dan `Laptop Lenovo - 1 {runId}` tampil kembali sesudah filter dilepas
152. Isi Warranty Expiry dengan rentang `T0 + 10 hari` sampai `T0 + 30 hari`
153. Klik `[Apply]`
154. Verifikasi tabel memuat `Printer Epson - 1 {runId}` yang salah satu garansinya jatuh di dalam rentang
155. Verifikasi tabel tidak memuat `Printer Epson - 2 {runId}`
156. Klik `[Clear Field]`
157. Klik `[Apply]`
158. Isi Register Date dengan rentang `T0 - 10 hari` sampai `T0 - 2 hari`
159. Isi Last Updated dengan rentang `T0 - 10 hari` sampai `T0 - 2 hari`
160. Klik `[Apply]`
161. Verifikasi tabel menampilkan empty state `No results found` karena seluruh aset terdaftar dan diperbarui sesudah rentang
162. Klik `[Clear Field]`
163. Klik `[Apply]`
164. Isi Last Scanned dengan rentang `T0 + 10 hari` sampai `T0 + 20 hari`
165. Klik `[Apply]`
166. Verifikasi tabel menampilkan empty state `No results found` karena tidak ada aset yang terakhir dipindai dalam rentang itu
167. Klik `[Clear Field]`
168. Klik `[Apply]`

### Filter rentang angka Min dan Max
169. Isi Min pada Purchase Cost dengan `900000`
170. Isi Max pada Purchase Cost dengan `2000000`
171. Klik `[Apply]`
172. Verifikasi tabel memuat `Printer Epson - 2 {runId}`
173. Verifikasi tabel tidak memuat `Printer Epson - 1 {runId}`
174. Klik `[Clear Field]`
175. Klik `[Apply]`
176. Isi Min pada Purchase Cost dengan `2000000`
177. Isi Max pada Purchase Cost dengan `2500000`
178. Klik `[Apply]`
179. Verifikasi tabel memuat `Printer Epson - 1 {runId}`
180. Verifikasi tabel tidak memuat `Printer Epson - 2 {runId}` dan `Printer Canon - 1 {runId}`
181. Klik `[Clear Field]`
182. Klik `[Apply]`
183. Isi Min pada Purchase Cost dengan `10000000`
184. Klik `[Apply]`
185. Verifikasi tabel memuat `Printer Canon - 1 {runId}` dan `Printer Canon - 2 {runId}`
186. Verifikasi tabel tidak memuat `Printer Epson - 1 {runId}` dan `Printer Epson - 2 {runId}`
187. Klik `[Clear Field]`
188. Klik `[Apply]`
189. Isi Max pada Purchase Cost dengan `900000`
190. Klik `[Apply]`
191. Verifikasi tabel memuat `Printer Epson - 2 {runId}`
192. Verifikasi tabel tidak memuat `Printer Epson - 1 {runId}` dan `Printer Canon - 1 {runId}`
193. Klik `[Clear Field]`
194. Klik `[Apply]`
195. Isi Min pada Purchase Cost dengan `15000000`
196. Isi Max pada Purchase Cost dengan `900000`
197. Klik `[Apply]`
198. Verifikasi tabel menampilkan empty state `No results found`
199. Klik `[Clear Field]`
200. Klik `[Apply]`
201. Isi Min pada Purchase Cost dengan `20000000`
202. Klik `[Apply]`
203. Verifikasi tabel menampilkan empty state `No results found`
204. Klik `[Clear Field]`
205. Klik `[Apply]`
206. Verifikasi baris `Laptop Lenovo - 1 {runId}` yang `Pending` pada Purchase Cost tidak pernah tampil pada saringan Purchase Cost di atas
207. Isi Min pada Asset Value (Commercial) dengan `0`
208. Isi Min pada Asset Value (Fiscal) dengan `0`
209. Klik `[Apply]`
210. Verifikasi tabel memuat `Printer Epson - 1 {runId}` dan `Printer Epson - 2 {runId}` dan `Printer Canon - 1 {runId}` yang Asset Value-nya terisi
211. Verifikasi tabel tidak memuat `Printer Canon - 2 {runId}` dan `Laptop Lenovo - 1 {runId}` yang sel Asset Value-nya `Pending`
212. Klik `[Clear Field]`
213. Klik `[Apply]`

### Filter Purchase status tanpa kolom
214. Pilih Purchase Status `Pending` pada Filter Panel
215. Klik `[Apply]`
216. Verifikasi tabel memuat `Laptop Lenovo - 1 {runId}` yang data Purchase-nya belum diisi
217. Verifikasi tabel tidak memuat `Printer Epson - 1 {runId}` yang Purchase-nya `Complete`
218. Klik `[Clear Field]`
219. Klik `[Apply]`

### Search dan Filter beririsan, dan pelepasan satu saringan
220. Pilih Brand `Epson` pada Filter Panel
221. Klik `[Apply]`
222. Ganti isi kotak search dengan `- 1 {runId}`, tekan Enter
223. Verifikasi tabel memuat `Printer Epson - 1 {runId}` yang cocok dengan Search `- 1 {runId}` dan Brand `Epson`
224. Verifikasi tabel tidak memuat `Printer Epson - 2 {runId}` (hanya cocok Filter) dan `Printer Canon - 1 {runId}` (hanya cocok Search)
225. Klik `[Clear Field]`
226. Klik `[Apply]`
227. Verifikasi tabel memuat `Printer Epson - 1 {runId}` dan `Printer Canon - 1 {runId}` yang cocok dengan Search `- 1 {runId}` saja, sehingga Clear Field mempertahankan Search
228. Ganti isi kotak search dengan `{runId}`, tekan Enter
229. Pilih Brand `Epson` pada Filter Panel
230. Klik `[Apply]`
231. Ganti isi kotak search dengan `Printer Canon - 1 {runId}`, tekan Enter
232. Verifikasi tabel menampilkan empty state `No results found` karena irisan Search dan Filter kosong, walau masing-masing mencocokkan baris
233. Klik `[Clear Field]`
234. Klik `[Apply]`
235. Verifikasi baris `Printer Canon - 1 {runId}` tampil kembali sesudah Filter dilepas dan Search dipertahankan
236. Klik `(←)` pada kotak Search

### Filter tetap berlaku saat kolom disembunyikan
237. Pilih Brand `Epson` pada Filter Panel
238. Klik `[Apply]`
239. Klik header kolom `Actions`
240. Lepas centang kolom `Brand` pada panel Column Visibility
241. Verifikasi tabel memuat `Printer Epson - 1 {runId}` dan `Printer Epson - 2 {runId}` dan tidak memuat `Printer Canon - 1 {runId}` walau kolom `Brand` disembunyikan
242. Verifikasi Filter Panel masih memuat field Brand berisi `Epson`
243. Centang kolom `Brand` pada panel Column Visibility
244. Klik `[Clear Field]`
245. Klik `[Apply]`

### Aset yang diubah keluar atau masuk dari saringan aktif
246. Isi Min pada Purchase Cost dengan `2000000`
247. Isi Max pada Purchase Cost dengan `2500000`
248. Klik `[Apply]`
249. Verifikasi tabel memuat `Printer Epson - 1 {runId}` dan tidak memuat `Laptop Lenovo - 1 {runId}`
250. Klik field Modified By pada Filter Panel
251. Verifikasi opsi Modified By memuat `Faisal Akbar {runId}` dan tidak memuat `Retno Utami {runId}`
252. `Retno Utami {runId}` melakukan Edit Purchase pada `Laptop Lenovo - 1 {runId}` dengan Purchase Date `T0 - 20 hari` dan Purchase Cost `2300000`
253. Klik field Modified By pada Filter Panel
254. Verifikasi opsi Modified By memuat `Retno Utami {runId}` tanpa muat ulang halaman
255. Klik `[Apply]`
256. Verifikasi tabel memuat `Printer Epson - 1 {runId}` dan `Laptop Lenovo - 1 {runId}` karena `Laptop Lenovo - 1 {runId}` kini masuk ke dalam rentang
257. Klik menu aksi baris `Printer Epson - 1 {runId}`
258. Pilih `Edit Purchase`
259. Isi Purchase Cost dengan `9000000`
260. Klik `[Save]`
261. Klik `[Apply]`
262. Verifikasi tabel memuat `Laptop Lenovo - 1 {runId}` dan tidak memuat `Printer Epson - 1 {runId}` karena kini berada di luar rentang
263. Klik `[Clear Field]`
264. Klik `[Apply]`

### Placeholder field Filter Panel
265. Ketik Search `{runId}`, tekan Enter
266. Verifikasi field `Asset Name` pada Filter Panel memuat placeholder `All asset names`
267. Verifikasi field `TAG` pada Filter Panel memuat placeholder `All tags`
268. Verifikasi field `Model/Type` pada Filter Panel memuat placeholder `All models`
269. Verifikasi field `Measurement` pada Filter Panel memuat placeholder `All units`
270. Verifikasi field `Category` pada Filter Panel memuat placeholder `All categories`
271. Verifikasi field `Division` pada Filter Panel memuat placeholder `All divisions`
272. Verifikasi field `Label` pada Filter Panel memuat placeholder `All labels`
273. Verifikasi field `Status` pada Filter Panel memuat placeholder `All statuses`
274. Verifikasi field `Register Date` pada Filter Panel memuat placeholder `Select date`
275. Verifikasi field `Last Scanned` pada Filter Panel memuat placeholder `Select date`
276. Verifikasi field `Asset Class` pada Filter Panel memuat placeholder `All asset classes`
277. Verifikasi field `Tax Depreciation Class` pada Filter Panel memuat placeholder `All tax depreciation classes`
278. Verifikasi field `Asset Value (Commercial)` pada Filter Panel memuat placeholder `Min` dan `Max`
279. Verifikasi field `Asset Value (Fiscal)` pada Filter Panel memuat placeholder `Min` dan `Max`
280. Verifikasi field `Purchase Date` pada Filter Panel memuat placeholder `Select date`
281. Verifikasi field `Purchase Cost` pada Filter Panel memuat placeholder `Min` dan `Max`
282. Verifikasi field `Warranty Expiry` pada Filter Panel memuat placeholder `Select date`
283. Verifikasi field `Modified By` pada Filter Panel memuat placeholder `All users`
284. Verifikasi field `Last Updated` pada Filter Panel memuat placeholder `Select date`

### Opsi Model/Type dan Tax Depreciation Class mengikuti data tabel
285. Klik field Model/Type pada Filter Panel
286. Verifikasi opsi Model/Type memuat `L3250` dan `Pixma G3020` dari data tabel
287. Verifikasi opsi Model/Type memuat `No Model` sebagai opsi seperti nilai lain
288. Tekan `Esc` untuk menutup daftar opsi
289. Klik field Tax Depreciation Class pada Filter Panel
290. Verifikasi opsi Tax Depreciation Class memuat `Pajak 1` dan `Pajak 2` dari data tabel
291. Verifikasi opsi Tax Depreciation Class tidak memuat nilai kosong walau `Printer Canon - 1 {runId}` tanpa Tax Depreciation Class
292. Tekan `Esc` untuk menutup daftar opsi

### Filter rentang tanggal dengan baris yang cocok
293. Isi Register Date dengan rentang `T0 - 10 hari` sampai `T0 + 10 hari`
294. Klik `[Apply]`
295. Verifikasi tabel memuat `Printer Epson - 1 {runId}` dan `Laptop Lenovo - 1 {runId}` yang terdaftar pada `T0`
296. Klik `[Clear Field]`
297. Klik `[Apply]`
298. Isi Last Updated dengan rentang `T0 - 10 hari` sampai `T0 + 10 hari`
299. Klik `[Apply]`
300. Verifikasi tabel memuat `Printer Epson - 1 {runId}` dan `Laptop Lenovo - 1 {runId}` yang terakhir diperbarui pada `T0`
301. Klik `[Clear Field]`
302. Klik `[Apply]`
303. Isi Last Scanned dengan rentang `T0 - 5 hari` sampai `T0 - 3 hari`
304. Klik `[Apply]`
305. Verifikasi tabel memuat `Printer Canon - 1 {runId}` yang terakhir dipindai pada `T0 - 3 hari`
306. Verifikasi tabel tidak memuat `Printer Epson - 1 {runId}` yang belum pernah dipindai
307. Klik `[Clear Field]`
308. Klik `[Apply]`

### Filter rentang Min dan Max Asset Value
309. Isi Min pada Asset Value (Commercial) dengan `900000`
310. Isi Max pada Asset Value (Commercial) dengan `9000000`
311. Klik `[Apply]`
312. Verifikasi tabel memuat `Printer Epson - 1 {runId}` (Asset Value `9000000` tepat di batas Max) dan `Printer Epson - 2 {runId}` (Asset Value `900000` tepat di batas Min)
313. Verifikasi tabel tidak memuat `Printer Canon - 1 {runId}` yang Asset Value-nya `10000000` di atas Max
314. Klik `[Clear Field]`
315. Klik `[Apply]`
316. Isi Min pada Asset Value (Fiscal) dengan `9000000`
317. Isi Max pada Asset Value (Fiscal) dengan `10000000`
318. Klik `[Apply]`
319. Verifikasi tabel memuat `Printer Epson - 1 {runId}` (Asset Value `9000000` tepat di batas Min) dan `Printer Canon - 1 {runId}` (Asset Value `10000000` tepat di batas Max)
320. Verifikasi tabel tidak memuat `Printer Epson - 2 {runId}` yang Asset Value-nya `900000` di bawah Min
321. Klik `[Clear Field]`
322. Klik `[Apply]`

### Filter Status dimensi penanda lisensi, Tagging, dan Activity Lock
323. Klik field Status pada Filter Panel
324. Verifikasi opsi Status memuat `Pending Activation`, `TAG Reported`, `In Audit`, dan `Under Maintenance`
325. Pilih Status `Pending Activation` pada Filter Panel
326. Klik `[Apply]`
327. Verifikasi tabel memuat `Perangkat Uji - 11 {runId}` yang berpenanda `Pending Activation`
328. Pilih Status `Unmanaged` pada Filter Panel
329. Klik `[Apply]`
330. Verifikasi tabel memuat `Perangkat Uji - 9 {runId}` (`Unmanaged`) dan `Perangkat Uji - 11 {runId}` (`Pending Activation`) karena nilai dalam dimensi penanda lisensi digabung OR
331. Verifikasi tabel tidak memuat `Printer Epson - 1 {runId}` yang tanpa penanda lisensi
332. Klik `[Clear Field]`
333. Pilih Status `TAG Reported` pada Filter Panel
334. Pilih Status `In Audit` pada Filter Panel
335. Klik `[Apply]`
336. Verifikasi tabel memuat `Perangkat Uji - 14 {runId}` yang berstatus `TAG Reported` dan `In Audit` sekaligus karena dimensi Tagging dan Activity Lock digabung AND
337. Verifikasi tabel tidak memuat `Perangkat Uji - 12 {runId}` yang hanya `TAG Reported` dan `Perangkat Uji - 13 {runId}` yang hanya `In Audit`
338. Klik `[Clear Field]`
339. Pilih Status `TAG Reported` pada Filter Panel
340. Pilih Status `Not Paired Yet` pada Filter Panel
341. Klik `[Apply]`
342. Verifikasi tabel memuat `Perangkat Uji - 12 {runId}` (`TAG Reported`) dan `Perangkat Uji - 10 {runId}` (`Not Paired Yet`) karena nilai dalam dimensi Tagging digabung OR
343. Verifikasi tabel tidak memuat `Printer Epson - 1 {runId}` yang tidak berstatus Tagging
344. Klik `[Clear Field]`
345. Klik `[Apply]`

### Filter Modified By dipilih dan di-Apply
346. Pilih Modified By `Retno Utami {runId}` pada Filter Panel
347. Klik `[Apply]`
348. Verifikasi tabel memuat `Laptop Lenovo - 1 {runId}` yang terakhir diubah `Retno Utami {runId}`
349. Verifikasi tabel tidak memuat `Printer Epson - 1 {runId}` yang terakhir diubah `Faisal Akbar {runId}`
350. Klik `[Clear Field]`
351. Klik `[Apply]`

### Clear Field dan Clear Search mempertahankan saringan dan sort lainnya
352. Ketik Search `Printer Epson`, tekan Enter
353. Klik header kolom `Division`
354. Klik header kolom `Division`
355. Pilih Brand `Epson` pada Filter Panel
356. Klik `[Apply]`
357. Verifikasi urutan Division menurun pada hasil: `Printer Epson - 2 {runId}` (`Operations`) mendahului `Printer Epson - 1 {runId}` (`Finance`)
358. Klik `(←)` pada kotak Search
359. Verifikasi Filter Panel masih memuat field Brand berisi `Epson`
360. Verifikasi tabel memuat `Printer Epson - 2 {runId}` lalu `Printer Epson - 1 {runId}` menurut Division menurun
361. Verifikasi tabel tidak memuat `Printer Canon - 1 {runId}` yang Brand-nya bukan `Epson`
362. Ketik Search `Printer Epson`, tekan Enter
363. Klik `[Clear Field]`
364. Klik `[Apply]`
365. Verifikasi tabel memuat `Printer Epson - 2 {runId}` lalu `Printer Epson - 1 {runId}` menurut Division menurun
366. Verifikasi tabel tidak memuat `Printer Canon - 1 {runId}` dan `Laptop Lenovo - 1 {runId}` yang tidak cocok dengan Search `Printer Epson`
367. Klik header kolom `Division`
368. Klik `(←)` pada kotak Search

### Aset Damaged + Missing cocok dengan opsi Damaged maupun Missing
369. Ketik Search `{runId}`, tekan Enter
370. Pilih Status `Damaged` pada Filter Panel
371. Klik `[Apply]`
372. Verifikasi tabel memuat `Perangkat Uji - 15 {runId}` yang berstatus `Damaged` dan `Missing` karena cocok dengan opsi `Damaged`
373. Klik `[Clear Field]`
374. Klik `[Apply]`
375. Pilih Status `Missing` pada Filter Panel
376. Klik `[Apply]`
377. Verifikasi tabel memuat `Perangkat Uji - 15 {runId}` yang berstatus `Damaged` dan `Missing` karena cocok dengan opsi `Missing`
378. Verifikasi tabel tidak memuat `Perangkat Uji - 8 {runId}` yang berstatus `Damaged` tanpa `Missing`
379. Klik `[Clear Field]`
380. Klik `[Apply]`

### Record yang dibuat saat Filter aktif hanya tampil bila cocok
381. Pilih Brand `Epson` pada Filter Panel
382. Klik `[Apply]`
383. `Retno Utami {runId}` membuat aset `Printer Canon - 3 {runId}` dengan Brand `Canon`
384. Klik `[Apply]`
385. Verifikasi tabel tidak memuat `Printer Canon - 3 {runId}` yang Brand-nya `Canon` tidak cocok dengan Filter Brand `Epson`
386. `Retno Utami {runId}` membuat aset `Printer Epson - 3 {runId}` dengan Brand `Epson`
387. Klik `[Apply]`
388. Verifikasi tabel memuat `Printer Epson - 3 {runId}` yang Brand-nya `Epson` cocok dengan Filter
389. Klik `[Clear Field]`
390. Klik `[Apply]`

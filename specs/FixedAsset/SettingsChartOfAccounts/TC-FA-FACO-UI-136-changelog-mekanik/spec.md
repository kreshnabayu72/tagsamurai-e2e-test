---
id: TC-FA-FACO-UI-136-changelog-mekanik
title: "Modal Changelog: Search, sort, Filter Panel, Setup Column, paginasi, dan gagal unduh"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1.1#r21", "§4.1.1#r22", "§4.1.1#r23", "§4.1.1#r24", "§4.1.1#r27", "EB-TBL-7@tabel-changelog", "EB-SRC-4@tabel-changelog", "EB-FLT-2@tabel-changelog", "EB-FLT-6@tabel-changelog", "EB-SRT-3@tabel-changelog", "EB-KOL-1@tabel-changelog", "EB-DL-2@tabel-changelog"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r21": [4, 5, 6]
  "§4.1.1#r22": [4, 7, 8]
  "§4.1.1#r23": [4, 9, 10]
  "§4.1.1#r24": [4, 11, 12]
  "§4.1.1#r27": [4, 13, 14]
  "EB-TBL-7@tabel-changelog": [123, 125, 127, 129, 130, 133, 135, 139, 141, 146, 148, 151, 153, 157, 159, 163, 167]
  "EB-SRC-4@tabel-changelog": [91, 93, 95, 96, 98, 99, 100, 102, 104, 106, 107]
  "EB-FLT-2@tabel-changelog": [19, 21, 22, 23, 29, 31, 39, 41, 43, 45, 46, 59, 65, 66, 68, 70, 75]
  "EB-FLT-6@tabel-changelog": [81, 84, 86, 87]
  "EB-SRT-3@tabel-changelog": [111, 113, 115, 118, 119, 120]
  "EB-KOL-1@tabel-changelog": [171, 173, 174, 175, 176, 177, 178, 179, 185, 187, 188, 193, 199, 201, 209, 211, 212, 214, 221, 222, 228, 230, 241, 243]
  "EB-DL-2@tabel-changelog": [248, 253]
anchor: []
coverage:
  web: automated
---

# Modal Changelog: Search, sort, Filter Panel, Setup Column, paginasi, dan gagal unduh

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Modal Changelog
- Data:
  - DU-136-1: entri Create, Account Code `1-1001`, Field `Account Code`, Old Value kosong, New Value `1-1001`, Modified By `Rina Pratiwi`.
  - DU-136-2: entri Edit, Account Code `1-2001`, Field `Account Name`, Old Value `Accumulated Depreciation`, New Value `Accumulated Depreciation – Equipment`, Modified By `Rina Pratiwi`.
  - DU-136-3: entri Edit, Account Code `1-3001`, Field `Status`, Old Value `Active`, New Value `Inactive`, Modified By `Budi`.
  - DU-136-4: entri Delete, Account Code `4-7001`, Field `Account Code`, Old Value `4-7001`, New Value kosong, Modified By `Alexander Graham Bell`.
  - DU-136-5: entri Edit, Account Code `4-7002`, Field `Account Name`, Old Value `Gain Loss`, New Value `Gain and Loss on Disposal`, Modified By `Budi`.
  - DU-136-6: entri Edit, Account Code `5-6001`, Field `Account Function`, Old Value `Asset Cost`, New Value `Depreciation Expense`, Modified By `Rina Pratiwi`.
  - DU-136-7: entri Edit, Account Code `6-2001`, Field `Status`, Old Value `Inactive`, New Value `Active`, Modified By `Budi`.
  - DU-136-8: entri Edit, Account Code `9-0001`, Field `Last Used in Journal`, Old Value kosong, New Value `Aug 2026`, Modified By `Alexander Graham Bell`.
  - DU-136-9: 101 entri Edit, Account Code `7-{n}`, Field `Account Name`, Old Value `Akun Lama {n}`, New Value `Akun Uji {n}`, Modified By `Rina Pratiwi`.
  - DU-136-10: 30 entri Edit, Account Code `8-{n}`, Field `Account Name`, Old Value `Kas Lama {n}`, New Value `Kas Cabang {n}`, Modified By `Rina Pratiwi`. Entri dengan New Value `Kas Cabang 1` adalah entri terbaru dari seluruh K3.
  - DU-136-11: 20 entri Edit, Account Code `3-{n}`, Field `Account Name`, Old Value `Bank Lama {n}`, New Value `Bank Cabang {n}`, Modified By `Rina Pratiwi`. Entri dengan New Value `Bank Cabang 1` adalah entri terbaru kedua dari seluruh K3, tepat sesudah `Kas Cabang 1`.
  - DU-136-12: daftar entri Changelog kosong, jumlah entri `0`.
  - DU-136-13: nomor halaman yang diketik pada input Jump to page: `abc`, `0`, `-1`, dan `12`.
  - DU-136-14: kata kunci Search `Kas Cabang`.
  - DU-136-15: kata cari di dalam dropdown Modified By: `bu`, `RINA`, dan `Zzz`.
- Kondisi:
  - K1: modal Changelog berisi DU-136-1 sampai DU-136-8, dengan ukuran halaman bawaan dan tanpa filter ter-Apply; Filter Action `Create` hanya menghasilkan DU-136-1.
  - K2: modal Changelog berisi DU-136-9, dengan ukuran halaman bawaan; modal terdiri atas 11 halaman pada ukuran halaman 10.
  - K3: modal Changelog berisi DU-136-10 dan DU-136-11, dengan urutan bawaan Date terbaru sehingga `Kas Cabang 1` dan `Bank Cabang 1` ada di halaman 1 pada ukuran halaman 10; kata kunci Search `Kas Cabang` hanya menghasilkan DU-136-10, dan kotak Search kosong menghasilkan seluruh entri.
  - K4: seperti K2; Filter Action `Edit` menghasilkan seluruh entri DU-136-9.
  - K5: daftar entri Changelog kosong menurut DU-136-12.
  - K6: seperti K1; server menolak permintaan unduhan dengan error 5xx.

## Test Steps

### Field Filter Panel modal Changelog
1. Tampilkan Tab Chart of Accounts dengan kondisi K1
2. Klik ikon Changelog
3. Klik ikon Filter pada toolbar modal Changelog
4. Verifikasi Filter Panel memuat field `Date`, `Action`, `Account Code`, `Field`, dan `Modified By` untuk tabel Changelog
5. Verifikasi field `Date` berupa pemilih rentang tanggal untuk tabel Changelog
6. Verifikasi field `Date` memuat placeholder `Select date` untuk tabel Changelog
7. Verifikasi field `Action` berupa dropdown multi-select yang searchable untuk tabel Changelog
8. Verifikasi field `Action` memuat placeholder `All actions` untuk tabel Changelog
9. Verifikasi field `Account Code` berupa dropdown multi-select yang searchable untuk tabel Changelog
10. Verifikasi field `Account Code` memuat placeholder `All account codes` untuk tabel Changelog
11. Verifikasi field `Field` berupa dropdown multi-select yang searchable untuk tabel Changelog
12. Verifikasi field `Field` memuat placeholder `All fields` untuk tabel Changelog
13. Verifikasi field `Modified By` berupa dropdown multi-select yang searchable untuk tabel Changelog
14. Verifikasi field `Modified By` memuat placeholder `All users` untuk tabel Changelog

### Draf, Apply, dan penanda filter aktif
15. Tampilkan Tab Chart of Accounts dengan kondisi K1
16. Klik ikon Changelog
17. Klik ikon Filter pada toolbar modal Changelog
18. Pilih `Create` pada filter Action
19. Verifikasi entri `1-2001` tetap tampil sebelum `[Apply]` diklik untuk tabel Changelog
20. Klik `[Apply]`
21. Verifikasi entri `1-1001` tampil untuk tabel Changelog
22. Verifikasi entri `1-2001` tidak tampil untuk tabel Changelog
23. Verifikasi penanda filter aktif tampil pada ikon Filter untuk tabel Changelog

### Menutup panel tanpa Apply membuang draf
24. Tampilkan Tab Chart of Accounts dengan kondisi K1
25. Klik ikon Changelog
26. Klik ikon Filter pada toolbar modal Changelog
27. Pilih `Create` pada filter Action
28. Klik ikon Filter pada toolbar modal Changelog
29. Verifikasi entri `1-2001` tetap tampil untuk tabel Changelog
30. Klik ikon Filter pada toolbar modal Changelog
31. Verifikasi field `Action` memuat placeholder `All actions` untuk tabel Changelog

### Chip opsi, uncheck, dan hapus chip
32. Tampilkan Tab Chart of Accounts dengan kondisi K1
33. Klik ikon Changelog
34. Klik ikon Filter pada toolbar modal Changelog
35. Klik field `Action`
36. Pilih `Create`
37. Pilih `Edit`
38. Pilih `Delete`
39. Verifikasi chip `Create`, `Edit`, dan `Delete` tampil pada field `Action` untuk tabel Changelog
40. Klik opsi `Delete` pada daftar opsi untuk menghilangkan centang
41. Verifikasi chip `Delete` tidak tampil pada field `Action` untuk tabel Changelog
42. Klik `(✕)` pada chip `Edit`
43. Verifikasi chip `Edit` tidak tampil pada field `Action` untuk tabel Changelog
44. Klik `[Apply]`
45. Verifikasi entri `1-1001` tampil untuk tabel Changelog
46. Verifikasi entri `1-2001` tidak tampil untuk tabel Changelog

### Chip overflow
47. Tampilkan Tab Chart of Accounts dengan kondisi K1
48. Klik ikon Changelog
49. Klik ikon Filter pada toolbar modal Changelog
50. Klik field `Account Code`
51. Pilih `1-1001`
52. Pilih `1-2001`
53. Pilih `1-3001`
54. Pilih `4-7001`
55. Pilih `4-7002`
56. Pilih `5-6001`
57. Pilih `6-2001`
58. Pilih `9-0001`
59. Verifikasi opsi terpilih yang tidak muat diringkas dalam satu chip `+N more`, dengan jumlah chip yang tampil ditambah N sama dengan `8` untuk tabel Changelog

### Search di dalam dropdown
60. Tampilkan Tab Chart of Accounts dengan kondisi K1
61. Klik ikon Changelog
62. Klik ikon Filter pada toolbar modal Changelog
63. Klik field `Modified By`
64. Ketik `bu` pada kotak cari di dalam dropdown `Modified By`
65. Verifikasi opsi `Budi` tampil untuk tabel Changelog
66. Verifikasi opsi yang memuat `Rina` tidak tampil untuk tabel Changelog
67. Ganti isi kotak cari dengan `RINA`
68. Verifikasi opsi yang memuat `Rina` tampil untuk tabel Changelog
69. Ganti isi kotak cari dengan `Zzz`
70. Verifikasi teks `No results found` tampil untuk tabel Changelog

### Sumber opsi kosong
71. Tampilkan Tab Chart of Accounts dengan kondisi K5
72. Klik ikon Changelog
73. Klik ikon Filter pada toolbar modal Changelog
74. Klik field `Action`
75. Verifikasi teks `No options available` tampil untuk tabel Changelog

### Menyembunyikan kolom tidak menghapus filter
76. Tampilkan Tab Chart of Accounts dengan kondisi K1
77. Klik ikon Changelog
78. Klik ikon Filter pada toolbar modal Changelog
79. Pilih `Create` pada filter Action
80. Klik `[Apply]`
81. Verifikasi entri `1-1001` tampil untuk tabel Changelog
82. Klik `⋯` pada header kolom Actions di modal Changelog
83. Hilangkan centang `Action` pada panel Column Visibility
84. Verifikasi header kolom `Action` tidak tampil untuk tabel Changelog
85. Klik ikon Filter pada toolbar modal Changelog
86. Verifikasi field `Action` masih ada di Filter Panel untuk tabel Changelog
87. Verifikasi entri `1-2001` tetap tidak tampil untuk tabel Changelog

### Siklus kotak Search
88. Tampilkan Tab Chart of Accounts dengan kondisi K3
89. Klik ikon Changelog
90. Klik ikon Search pada toolbar modal Changelog
91. Verifikasi kotak Search terbuka dan fokus berada di input untuk tabel Changelog
92. Ketik `Kas Cabang` pada kotak Search tanpa menekan Enter
93. Verifikasi entri dengan New Value `Bank Cabang 1` tetap tampil dalam 2 detik sesudah mengetik untuk tabel Changelog
94. Tekan Enter pada kotak Search
95. Verifikasi entri dengan New Value `Kas Cabang 1` tampil untuk tabel Changelog
96. Verifikasi entri dengan New Value `Bank Cabang 1` tidak tampil untuk tabel Changelog
97. Klik `✕` pada kotak Search
98. Verifikasi isi kotak Search kosong untuk tabel Changelog
99. Verifikasi entri dengan New Value `Kas Cabang 1` masih tampil untuk tabel Changelog
100. Verifikasi entri dengan New Value `Bank Cabang 1` masih tidak tampil untuk tabel Changelog
101. Tekan Enter pada kotak Search yang kosong
102. Verifikasi entri dengan New Value `Bank Cabang 1` tampil kembali untuk tabel Changelog
103. Ketik Search `Kas Cabang`, tekan Enter
104. Verifikasi entri dengan New Value `Kas Cabang 1` tampil untuk tabel Changelog
105. Klik `(←)` pada kotak Search
106. Verifikasi kotak Search tertutup untuk tabel Changelog
107. Verifikasi entri dengan New Value `Bank Cabang 1` tampil kembali untuk tabel Changelog

### Indikator sort
108. Tampilkan Tab Chart of Accounts dengan kondisi K2
109. Klik ikon Changelog
110. Klik header kolom `Account Code`
111. Verifikasi indikator sort naik `↑` aktif pada header kolom `Account Code` untuk tabel Changelog
112. Klik header kolom `Account Code`
113. Verifikasi indikator sort turun `↓` aktif pada header kolom `Account Code` untuk tabel Changelog
114. Klik header kolom `Account Code`
115. Verifikasi indikator sort pada header kolom `Account Code` hilang untuk tabel Changelog
116. Klik header kolom `Account Code`
117. Klik header kolom `Field`
118. Verifikasi indikator sort aktif pada header kolom `Field` untuk tabel Changelog
119. Verifikasi indikator sort pada header kolom `Account Code` tidak aktif untuk tabel Changelog
120. Verifikasi header kolom Actions `⋯` tidak memiliki ikon sort untuk tabel Changelog

### Ukuran halaman dan kembali ke halaman 1
121. Tampilkan Tab Chart of Accounts dengan kondisi K2
122. Klik ikon Changelog
123. Verifikasi ukuran halaman terpilih `10` dan halaman 1 menampilkan 10 baris untuk tabel Changelog
124. Klik halaman `2`
125. Verifikasi halaman aktif adalah `2` untuk tabel Changelog
126. Klik dropdown Rows per page
127. Verifikasi pilihan `10`, `25`, `50`, dan `100` tersedia untuk tabel Changelog
128. Pilih `25`
129. Verifikasi halaman aktif adalah `1` untuk tabel Changelog
130. Verifikasi halaman 1 menampilkan 25 baris untuk tabel Changelog
131. Klik dropdown Rows per page
132. Pilih `100`
133. Verifikasi halaman 1 menampilkan 100 baris untuk tabel Changelog
134. Klik halaman `2`
135. Verifikasi halaman 2 menampilkan 1 baris untuk tabel Changelog

### Ganti sort tetap di halaman sekarang
136. Tampilkan Tab Chart of Accounts dengan kondisi K2
137. Klik ikon Changelog
138. Klik halaman `2`
139. Verifikasi halaman aktif adalah `2` untuk tabel Changelog
140. Klik header kolom `Account Code`
141. Verifikasi halaman aktif tetap `2` untuk tabel Changelog

### Nomor halaman tidak valid
142. Tampilkan Tab Chart of Accounts dengan kondisi K2
143. Klik ikon Changelog
144. Klik halaman `2`
145. Ketik `abc` pada input Jump to page, tekan Enter
146. Verifikasi halaman aktif tetap `2` untuk tabel Changelog
147. Ketik `0` pada input Jump to page, tekan Enter
148. Verifikasi halaman aktif adalah `1` untuk tabel Changelog[^drift-1]
149. Klik halaman `2`
150. Ketik `-1` pada input Jump to page, tekan Enter
151. Verifikasi halaman aktif adalah `1` untuk tabel Changelog[^drift-1]
152. Ketik `12` pada input Jump to page, tekan Enter
153. Verifikasi halaman aktif adalah halaman terakhir `11` untuk tabel Changelog[^drift-1]

### Search dan Filter Panel mengembalikan ke halaman 1
154. Tampilkan Tab Chart of Accounts dengan kondisi K3
155. Klik ikon Changelog
156. Klik halaman `2`
157. Verifikasi halaman aktif adalah `2` untuk tabel Changelog
158. Ketik Search `Kas Cabang`, tekan Enter
159. Verifikasi halaman aktif adalah `1` untuk tabel Changelog
160. Tampilkan Tab Chart of Accounts dengan kondisi K4
161. Klik ikon Changelog
162. Klik halaman `2`
163. Verifikasi halaman aktif adalah `2` untuk tabel Changelog
164. Klik ikon Filter pada toolbar modal Changelog
165. Pilih `Edit` pada filter Action
166. Klik `[Apply]`
167. Verifikasi halaman aktif adalah `1` untuk tabel Changelog

### Anatomi Setup Column modal Changelog
168. Tampilkan Tab Chart of Accounts dengan kondisi K1
169. Klik ikon Changelog
170. Klik `⋯` pada header kolom Actions di modal Changelog
171. Verifikasi item `Setup Column...` tampil di bagian bawah panel Column Visibility untuk tabel Changelog
172. Klik `Setup Column...`
173. Verifikasi judul modal `Setup Column` tampil untuk tabel Changelog
174. Verifikasi deskripsi `Drag and drop to rearrange the order and click the pin to freeze up to 3 columns.` tampil untuk tabel Changelog
175. Verifikasi ikon `[✕]` tampil di modal untuk tabel Changelog
176. Verifikasi tombol `[Reset to Default]` dan `[Save]` tampil untuk tabel Changelog
177. Verifikasi tidak ada tombol `[Cancel]` di modal untuk tabel Changelog
178. Verifikasi daftar kolom memuat baris `Date`, `Action`, `Account Code`, `Field`, `Old Value`, `New Value`, dan `Modified By` untuk tabel Changelog
179. Verifikasi kolom Actions tidak muncul sebagai baris pada daftar kolom untuk tabel Changelog

### Hide dan show kolom lewat Setup Column
180. Tampilkan Tab Chart of Accounts dengan kondisi K1
181. Klik ikon Changelog
182. Klik `⋯` pada header kolom Actions di modal Changelog
183. Klik `Setup Column...`
184. Hilangkan centang `Field` pada daftar kolom
185. Verifikasi header kolom `Field` tidak tampil pada tabel di balik modal `Setup Column` untuk tabel Changelog
186. Klik `[Save]`
187. Verifikasi modal `Setup Column` tertutup untuk tabel Changelog
188. Verifikasi header kolom `Field` tidak tampil pada tabel Changelog
189. Klik `⋯` pada header kolom Actions di modal Changelog
190. Klik `Setup Column...`
191. Centang `Field` pada daftar kolom
192. Klik `[Save]`
193. Verifikasi header kolom `Field` tampil pada tabel Changelog

### Urutan kolom diubah lewat drag and drop
194. Tampilkan Tab Chart of Accounts dengan kondisi K1
195. Klik ikon Changelog
196. Klik `⋯` pada header kolom Actions di modal Changelog
197. Klik `Setup Column...`
198. Seret baris `Field` ke atas baris `Action` pada daftar kolom
199. Verifikasi header kolom `Field` berada sebelum header kolom `Action` pada tabel di balik modal `Setup Column` untuk tabel Changelog
200. Klik `[Save]`
201. Verifikasi header kolom `Field` berada sebelum header kolom `Action` pada tabel Changelog

### Pin kolom dan batas tiga kolom
202. Tampilkan Tab Chart of Accounts dengan kondisi K1
203. Klik ikon Changelog
204. Klik `⋯` pada header kolom Actions di modal Changelog
205. Klik `Setup Column...`
206. Klik ikon pin pada baris `Date`
207. Klik ikon pin pada baris `Action`
208. Klik ikon pin pada baris `Account Code`
209. Verifikasi baris `Date`, `Action`, dan `Account Code` berstatus pin untuk tabel Changelog
210. Arahkan kursor ke ikon pin pada baris `Field`
211. Verifikasi ikon pin pada baris `Field` disabled untuk tabel Changelog
212. Verifikasi `Maximum 3 columns can be pinned at once. Unpin another column first.` tersampaikan pada ikon pin baris `Field` untuk tabel Changelog
213. Klik ikon pin pada baris `Account Code`
214. Verifikasi ikon pin pada baris `Field` aktif kembali untuk tabel Changelog

### Reset to Default
215. Tampilkan Tab Chart of Accounts dengan kondisi K1
216. Klik ikon Changelog
217. Klik `⋯` pada header kolom Actions di modal Changelog
218. Klik `Setup Column...`
219. Hilangkan centang `Old Value` pada daftar kolom
220. Klik `[Reset to Default]`
221. Verifikasi baris `Old Value` tercentang pada daftar kolom untuk tabel Changelog
222. Verifikasi header kolom `Old Value` tampil pada tabel di balik modal `Setup Column` untuk tabel Changelog

### Menutup Setup Column tanpa Save membuang perubahan
223. Tampilkan Tab Chart of Accounts dengan kondisi K1
224. Klik ikon Changelog
225. Klik `⋯` pada header kolom Actions di modal Changelog
226. Klik `Setup Column...`
227. Hilangkan centang `Field` pada daftar kolom
228. Verifikasi header kolom `Field` tidak tampil pada tabel di balik modal `Setup Column` untuk tabel Changelog
229. Klik `[✕]` pada modal `Setup Column`
230. Verifikasi header kolom `Field` tampil pada tabel Changelog

### Kolom terakhir tidak bisa disembunyikan
231. Tampilkan Tab Chart of Accounts dengan kondisi K1
232. Klik ikon Changelog
233. Klik `⋯` pada header kolom Actions di modal Changelog
234. Klik `Setup Column...`
235. Hilangkan centang `Action` pada daftar kolom
236. Hilangkan centang `Account Code` pada daftar kolom
237. Hilangkan centang `Field` pada daftar kolom
238. Hilangkan centang `Old Value` pada daftar kolom
239. Hilangkan centang `New Value` pada daftar kolom
240. Hilangkan centang `Modified By` pada daftar kolom
241. Verifikasi checkbox baris `Date` disabled untuk tabel Changelog
242. Arahkan kursor ke checkbox baris `Date`
243. Verifikasi `At least one column must remain visible.` tersampaikan pada checkbox baris `Date` untuk tabel Changelog

### Unduhan CSV Changelog gagal
244. Tampilkan Tab Chart of Accounts dengan kondisi K6
245. Klik ikon Changelog
246. Klik ikon Download pada toolbar modal Changelog
247. Klik `Download as CSV`
248. Verifikasi toast `Error, failed to download Changelog-Chart-of-Accounts.` tampil

### Unduhan XLSX Changelog gagal
249. Tampilkan Tab Chart of Accounts dengan kondisi K6
250. Klik ikon Changelog
251. Klik ikon Download pada toolbar modal Changelog
252. Klik `Download as XLSX`
253. Verifikasi toast `Error, failed to download Changelog-Chart-of-Accounts.` tampil

[^drift-1]: Drift foundation vs kontrak komponen. foundation `prd-conventions.md` §9.18: «Nomor halaman tidak valid (0, negatif, melebihi halaman terakhir, bukan angka) pada input nomor halaman: input diabaikan dan tabel tetap di halaman sekarang.» Kontrak `Paginator#9`: «a page past the last goes to the last page, a page below 1 goes to page 1». Diasersi: kontrak, karena input nomor halaman adalah mekanik komponen Paginator (SB-7); PRD (ekspektasi baku EB-TBL-7) hanya merujuk §9.18.

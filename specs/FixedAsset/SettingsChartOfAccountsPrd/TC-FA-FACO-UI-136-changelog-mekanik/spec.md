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
  "EB-TBL-7@tabel-changelog": [122, 124, 126, 128, 129, 132, 134, 138, 140, 145, 147, 150, 152, 156, 158, 162, 166]
  "EB-SRC-4@tabel-changelog": [90, 92, 94, 95, 97, 98, 99, 101, 103, 105, 106]
  "EB-FLT-2@tabel-changelog": [19, 21, 22, 23, 29, 31, 39, 41, 43, 45, 46, 59, 65, 66, 68, 70, 75]
  "EB-FLT-6@tabel-changelog": [81, 84, 85, 86]
  "EB-SRT-3@tabel-changelog": [110, 112, 114, 117, 118, 119]
  "EB-KOL-1@tabel-changelog": [170, 172, 173, 174, 175, 176, 177, 178, 184, 186, 187, 192, 198, 200, 208, 210, 211, 213, 220, 221, 227, 229, 240, 242]
  "EB-DL-2@tabel-changelog": [247, 252]
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
  - DU-136-10: 30 entri Edit, Account Code `8-{n}`, Field `Account Name`, Old Value `Kas Lama {n}`, New Value `Kas Cabang {n}`, Modified By `Rina Pratiwi`.
  - DU-136-11: 20 entri Edit, Account Code `3-{n}`, Field `Account Name`, Old Value `Bank Lama {n}`, New Value `Bank Cabang {n}`, Modified By `Rina Pratiwi`.
  - DU-136-12: daftar entri Changelog kosong, jumlah entri `0`.
  - DU-136-13: nomor halaman yang diketik pada input Jump to page: `abc`, `0`, `-1`, dan `12`.
  - DU-136-14: kata kunci Search `Kas Cabang`.
  - DU-136-15: kata cari di dalam dropdown Modified By: `bu`, `RINA`, dan `Zzz`.
- Kondisi:
  - K1: modal Changelog berisi DU-136-1 sampai DU-136-8, dengan ukuran halaman bawaan dan tanpa filter ter-Apply; Filter Action `Create` hanya menghasilkan DU-136-1.
  - K2: modal Changelog berisi DU-136-9, dengan ukuran halaman bawaan; modal terdiri atas 11 halaman pada ukuran halaman 10.
  - K3: modal Changelog berisi DU-136-10 dan DU-136-11; kata kunci Search `Kas Cabang` hanya menghasilkan DU-136-10, dan kotak Search kosong menghasilkan seluruh entri.
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
66. Verifikasi opsi `Rina Pratiwi` tidak tampil untuk tabel Changelog
67. Ganti isi kotak cari dengan `RINA`
68. Verifikasi opsi `Rina Pratiwi` tampil untuk tabel Changelog
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
85. Verifikasi field `Action` masih ada di Filter Panel untuk tabel Changelog
86. Verifikasi entri `1-2001` tetap tidak tampil untuk tabel Changelog

### Siklus kotak Search
87. Tampilkan Tab Chart of Accounts dengan kondisi K3
88. Klik ikon Changelog
89. Klik ikon Search pada toolbar modal Changelog
90. Verifikasi kotak Search terbuka dan fokus berada di input untuk tabel Changelog
91. Ketik `Kas Cabang` pada kotak Search tanpa menekan Enter
92. Verifikasi entri dengan New Value `Bank Cabang 1` tetap tampil dalam 2 detik sesudah mengetik untuk tabel Changelog
93. Tekan Enter pada kotak Search
94. Verifikasi entri dengan New Value `Kas Cabang 1` tampil untuk tabel Changelog
95. Verifikasi entri dengan New Value `Bank Cabang 1` tidak tampil untuk tabel Changelog
96. Klik `✕` pada kotak Search
97. Verifikasi isi kotak Search kosong untuk tabel Changelog
98. Verifikasi entri dengan New Value `Kas Cabang 1` masih tampil untuk tabel Changelog
99. Verifikasi entri dengan New Value `Bank Cabang 1` masih tidak tampil untuk tabel Changelog
100. Tekan Enter pada kotak Search yang kosong
101. Verifikasi entri dengan New Value `Bank Cabang 1` tampil kembali untuk tabel Changelog
102. Ketik Search `Kas Cabang`, tekan Enter
103. Verifikasi entri dengan New Value `Kas Cabang 1` tampil untuk tabel Changelog
104. Klik `(←)` pada kotak Search
105. Verifikasi kotak Search tertutup untuk tabel Changelog
106. Verifikasi entri dengan New Value `Bank Cabang 1` tampil kembali untuk tabel Changelog

### Indikator sort
107. Tampilkan Tab Chart of Accounts dengan kondisi K2
108. Klik ikon Changelog
109. Klik header kolom `Account Code`
110. Verifikasi indikator sort naik `↑` aktif pada header kolom `Account Code` untuk tabel Changelog
111. Klik header kolom `Account Code`
112. Verifikasi indikator sort turun `↓` aktif pada header kolom `Account Code` untuk tabel Changelog
113. Klik header kolom `Account Code`
114. Verifikasi indikator sort pada header kolom `Account Code` hilang untuk tabel Changelog
115. Klik header kolom `Account Code`
116. Klik header kolom `Field`
117. Verifikasi indikator sort aktif pada header kolom `Field` untuk tabel Changelog
118. Verifikasi indikator sort pada header kolom `Account Code` tidak aktif untuk tabel Changelog
119. Verifikasi header kolom Actions `⋯` tidak memiliki ikon sort untuk tabel Changelog

### Ukuran halaman dan kembali ke halaman 1
120. Tampilkan Tab Chart of Accounts dengan kondisi K2
121. Klik ikon Changelog
122. Verifikasi ukuran halaman terpilih `10` dan halaman 1 menampilkan 10 baris untuk tabel Changelog
123. Klik halaman `2`
124. Verifikasi halaman aktif adalah `2` untuk tabel Changelog
125. Klik dropdown Rows per page
126. Verifikasi pilihan `10`, `25`, `50`, dan `100` tersedia untuk tabel Changelog
127. Pilih `25`
128. Verifikasi halaman aktif adalah `1` untuk tabel Changelog
129. Verifikasi halaman 1 menampilkan 25 baris untuk tabel Changelog
130. Klik dropdown Rows per page
131. Pilih `100`
132. Verifikasi halaman 1 menampilkan 100 baris untuk tabel Changelog
133. Klik halaman `2`
134. Verifikasi halaman 2 menampilkan 1 baris untuk tabel Changelog

### Ganti sort tetap di halaman sekarang
135. Tampilkan Tab Chart of Accounts dengan kondisi K2
136. Klik ikon Changelog
137. Klik halaman `2`
138. Verifikasi halaman aktif adalah `2` untuk tabel Changelog
139. Klik header kolom `Account Code`
140. Verifikasi halaman aktif tetap `2` untuk tabel Changelog

### Nomor halaman tidak valid
141. Tampilkan Tab Chart of Accounts dengan kondisi K2
142. Klik ikon Changelog
143. Klik halaman `2`
144. Ketik `abc` pada input Jump to page, tekan Enter
145. Verifikasi halaman aktif tetap `2` untuk tabel Changelog
146. Ketik `0` pada input Jump to page, tekan Enter
147. Verifikasi halaman aktif adalah `1` untuk tabel Changelog[^drift-1]
148. Klik halaman `2`
149. Ketik `-1` pada input Jump to page, tekan Enter
150. Verifikasi halaman aktif adalah `1` untuk tabel Changelog[^drift-1]
151. Ketik `12` pada input Jump to page, tekan Enter
152. Verifikasi halaman aktif adalah halaman terakhir `11` untuk tabel Changelog[^drift-1]

### Search dan Filter Panel mengembalikan ke halaman 1
153. Tampilkan Tab Chart of Accounts dengan kondisi K3
154. Klik ikon Changelog
155. Klik halaman `2`
156. Verifikasi halaman aktif adalah `2` untuk tabel Changelog
157. Ketik Search `Kas Cabang`, tekan Enter
158. Verifikasi halaman aktif adalah `1` untuk tabel Changelog
159. Tampilkan Tab Chart of Accounts dengan kondisi K4
160. Klik ikon Changelog
161. Klik halaman `2`
162. Verifikasi halaman aktif adalah `2` untuk tabel Changelog
163. Klik ikon Filter pada toolbar modal Changelog
164. Pilih `Edit` pada filter Action
165. Klik `[Apply]`
166. Verifikasi halaman aktif adalah `1` untuk tabel Changelog

### Anatomi Setup Column modal Changelog
167. Tampilkan Tab Chart of Accounts dengan kondisi K1
168. Klik ikon Changelog
169. Klik `⋯` pada header kolom Actions di modal Changelog
170. Verifikasi item `Setup Column...` tampil di bagian bawah panel Column Visibility untuk tabel Changelog
171. Klik `Setup Column...`
172. Verifikasi judul modal `Setup Column` tampil untuk tabel Changelog
173. Verifikasi deskripsi `Drag and drop to rearrange the order and click the pin to freeze up to 3 columns.` tampil untuk tabel Changelog
174. Verifikasi ikon `[✕]` tampil di modal untuk tabel Changelog
175. Verifikasi tombol `[Reset to Default]` dan `[Save]` tampil untuk tabel Changelog
176. Verifikasi tidak ada tombol `[Cancel]` di modal untuk tabel Changelog
177. Verifikasi daftar kolom memuat baris `Date`, `Action`, `Account Code`, `Field`, `Old Value`, `New Value`, dan `Modified By` untuk tabel Changelog
178. Verifikasi kolom Actions tidak muncul sebagai baris pada daftar kolom untuk tabel Changelog

### Hide dan show kolom lewat Setup Column
179. Tampilkan Tab Chart of Accounts dengan kondisi K1
180. Klik ikon Changelog
181. Klik `⋯` pada header kolom Actions di modal Changelog
182. Klik `Setup Column...`
183. Hilangkan centang `Field` pada daftar kolom
184. Verifikasi header kolom `Field` tidak tampil pada tabel di balik modal `Setup Column` untuk tabel Changelog
185. Klik `[Save]`
186. Verifikasi modal `Setup Column` tertutup untuk tabel Changelog
187. Verifikasi header kolom `Field` tidak tampil pada tabel Changelog
188. Klik `⋯` pada header kolom Actions di modal Changelog
189. Klik `Setup Column...`
190. Centang `Field` pada daftar kolom
191. Klik `[Save]`
192. Verifikasi header kolom `Field` tampil pada tabel Changelog

### Urutan kolom diubah lewat drag and drop
193. Tampilkan Tab Chart of Accounts dengan kondisi K1
194. Klik ikon Changelog
195. Klik `⋯` pada header kolom Actions di modal Changelog
196. Klik `Setup Column...`
197. Seret baris `Field` ke atas baris `Action` pada daftar kolom
198. Verifikasi header kolom `Field` berada sebelum header kolom `Action` pada tabel di balik modal `Setup Column` untuk tabel Changelog
199. Klik `[Save]`
200. Verifikasi header kolom `Field` berada sebelum header kolom `Action` pada tabel Changelog

### Pin kolom dan batas tiga kolom
201. Tampilkan Tab Chart of Accounts dengan kondisi K1
202. Klik ikon Changelog
203. Klik `⋯` pada header kolom Actions di modal Changelog
204. Klik `Setup Column...`
205. Klik ikon pin pada baris `Date`
206. Klik ikon pin pada baris `Action`
207. Klik ikon pin pada baris `Account Code`
208. Verifikasi baris `Date`, `Action`, dan `Account Code` berstatus pin untuk tabel Changelog
209. Arahkan kursor ke ikon pin pada baris `Field`
210. Verifikasi ikon pin pada baris `Field` disabled untuk tabel Changelog
211. Verifikasi `Maximum 3 columns can be pinned at once. Unpin another column first.` tersampaikan pada ikon pin baris `Field` untuk tabel Changelog
212. Klik ikon pin pada baris `Account Code`
213. Verifikasi ikon pin pada baris `Field` aktif kembali untuk tabel Changelog

### Reset to Default
214. Tampilkan Tab Chart of Accounts dengan kondisi K1
215. Klik ikon Changelog
216. Klik `⋯` pada header kolom Actions di modal Changelog
217. Klik `Setup Column...`
218. Hilangkan centang `Old Value` pada daftar kolom
219. Klik `[Reset to Default]`
220. Verifikasi baris `Old Value` tercentang pada daftar kolom untuk tabel Changelog
221. Verifikasi header kolom `Old Value` tampil pada tabel di balik modal `Setup Column` untuk tabel Changelog

### Menutup Setup Column tanpa Save membuang perubahan
222. Tampilkan Tab Chart of Accounts dengan kondisi K1
223. Klik ikon Changelog
224. Klik `⋯` pada header kolom Actions di modal Changelog
225. Klik `Setup Column...`
226. Hilangkan centang `Field` pada daftar kolom
227. Verifikasi header kolom `Field` tidak tampil pada tabel di balik modal `Setup Column` untuk tabel Changelog
228. Klik `[✕]` pada modal `Setup Column`
229. Verifikasi header kolom `Field` tampil pada tabel Changelog

### Kolom terakhir tidak bisa disembunyikan
230. Tampilkan Tab Chart of Accounts dengan kondisi K1
231. Klik ikon Changelog
232. Klik `⋯` pada header kolom Actions di modal Changelog
233. Klik `Setup Column...`
234. Hilangkan centang `Action` pada daftar kolom
235. Hilangkan centang `Account Code` pada daftar kolom
236. Hilangkan centang `Field` pada daftar kolom
237. Hilangkan centang `Old Value` pada daftar kolom
238. Hilangkan centang `New Value` pada daftar kolom
239. Hilangkan centang `Modified By` pada daftar kolom
240. Verifikasi checkbox baris `Date` disabled untuk tabel Changelog
241. Arahkan kursor ke checkbox baris `Date`
242. Verifikasi `At least one column must remain visible.` tersampaikan pada checkbox baris `Date` untuk tabel Changelog

### Unduhan CSV Changelog gagal
243. Tampilkan Tab Chart of Accounts dengan kondisi K6
244. Klik ikon Changelog
245. Klik ikon Download pada toolbar modal Changelog
246. Klik `Download as CSV`
247. Verifikasi toast `Error, failed to download Changelog-Chart-of-Accounts.` tampil

### Unduhan XLSX Changelog gagal
248. Tampilkan Tab Chart of Accounts dengan kondisi K6
249. Klik ikon Changelog
250. Klik ikon Download pada toolbar modal Changelog
251. Klik `Download as XLSX`
252. Verifikasi toast `Error, failed to download Changelog-Chart-of-Accounts.` tampil

[^drift-1]: Drift foundation vs kontrak komponen. foundation `prd-conventions.md` §9.18: «Nomor halaman tidak valid (0, negatif, melebihi halaman terakhir, bukan angka) pada input nomor halaman: input diabaikan dan tabel tetap di halaman sekarang.» Kontrak `Paginator#9`: «a page past the last goes to the last page, a page below 1 goes to page 1». Diasersi: kontrak, karena input nomor halaman adalah mekanik komponen Paginator (SB-7); PRD (ekspektasi baku EB-TBL-7) hanya merujuk §9.18.

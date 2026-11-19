---
id: TC-FA-BORROW-E2E-003-tabel-transactions-search-filter-sort
title: "Search, Filter, dan Sort tabel Transactions mengikuti kolom Searchable, Filterable, dan Sortable"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#r22", "§5#r2", "§5#r4", "§5#r5", "EB-SRC-2@tabel-transactions", "EB-SRC-3@tabel-transactions", "EB-SRC-5@tabel-transactions", "EB-FLT-1@tabel-transactions", "EB-FLT-4@tabel-transactions", "EB-FLT-5@tabel-transactions", "EB-SRC-1", "EB-FLT-3", "EB-SRT-1", "EB-SRT-2"]
smoke: ["EB-SRC-1", "EB-FLT-3", "EB-SRT-1", "EB-SRT-2"]
dependsOn: []
trace:
  "§4.1#r22": [4]
  "§5#r2": [4, 7, 9, 10, 194, 225, 226, 230]
  "§5#r4": [2, 12, 16, 41, 43, 52, 200, 202]
  "§5#r5": [53, 62, 64, 67]
  "EB-SRC-2@tabel-transactions": [14, 27, 29]
  "EB-SRC-3@tabel-transactions": [25, 31, 32, 34, 36, 38, 39]
  "EB-SRC-5@tabel-transactions": [45, 48, 49, 113]
  "EB-FLT-1@tabel-transactions": [88, 237, 241]
  "EB-FLT-4@tabel-transactions": [109, 152, 155, 156, 160, 164, 166, 170, 173, 176, 180, 184, 192, 242]
  "EB-FLT-5@tabel-transactions": [117, 120]
  "EB-SRC-1": [18, 19, 21, 23]
  "EB-FLT-3": [91, 92, 95, 102, 105, 106, 126, 129, 134, 135, 139, 143, 147, 148, 215, 216]
  "EB-SRT-1": [55, 57, 60, 64, 78, 80, 82, 84, 205, 207, 209, 211]
  "EB-SRT-2": [62, 64, 69, 71, 73, 76]
anchor: []
coverage:
  web: automated
---

# Search, Filter, dan Sort tabel Transactions mengikuti kolom Searchable, Filterable, dan Sortable

## Prerequisites
- Aktor: Total Control `Admin Borrow {runId}` (DU-003-1), cakupan seluruh client. Aktor lain yang hanya memicu perubahan: `Agus Pratama` (Asset Admin, Group penugasan `Head Office`).
- Layar awal: Transactions > Borrow, tab Transactions.
- Data:
  - DU-003-1: User `Admin Borrow {runId}`, role Total Control, cakupan seluruh client; kolom tabel yang diubah aktor ini hanya berlaku untuk akunnya.
  - Pengaju: `Agus Pratama` (Asset Admin, Group penugasan `Head Office`), tampil `Agus P`; `Rina Wulandari` (Total Control, seluruh client), tampil `Rina W`. Seluruh BRW dibuat lewat form Borrow Request, dengan Source `Admin`, kecuali DU-003-10.
  - Setiap BRW memiliki aset sebanyak Total Asset-nya. Aset selain yang disebut namanya bernama `Aksesori Kantor {n} {runId}` (DU-003-31); BRW DU-003-9 memiliki 10 aset `Printer Lab Unit {n} {runId}` (DU-003-16). Last Updated setiap BRW sama dengan Request Date-nya, kecuali BRW yang diubah langkah. BRW DU-003-2 sampai DU-003-15 dibuat berurutan dari DU-003-2, sehingga Transaction ID bertambah menurut urutan itu.
  - DU-003-2: BRW Borrower `anggi Lestari` (tampil `anggi L`), Group `Head Office`, status header `Waiting for Handover`, Total Asset `1`, Requested By `Agus P`, Request Date `T0 − 13 hari`, aset `Laptop Dell {runId}` ber-TAG RFID dengan kode TAG `E2003412DF5A-{runId}` dan alias `Laptop Kantor Anggi {runId}`.
  - DU-003-3: BRW Borrower `Élan Pratama` (tampil `Élan P`), Group `Head Office`, status header `Waiting for Handover`, Total Asset `2`, Requested By `Agus P`, Request Date `T0 − 12 hari`.
  - DU-003-4: BRW Borrower `Elan Pratama` (tampil `Elan P`), Group `Branch Surabaya`, status header `Borrowed`, Total Asset `3`, Requested By `Rina W`, Request Date `T0 − 11 hari`.
  - DU-003-5: BRW Borrower `Ezra Santoso` (tampil `Ezra S`), Group `Branch Surabaya`, status header `Waiting for Handover`, Total Asset `2`, Requested By `Rina W`, Request Date `T0 − 10 hari`.
  - DU-003-6: BRW Borrower `3D Hartono` (tampil `3D H`), Group `Head Office`, status header `Borrowed`, Total Asset `1`, Requested By `Agus P`, Request Date `T0 − 9 hari`, aset `Handover Dock Station {runId}`.
  - DU-003-7: BRW Borrower `Rudi Hartono` (tampil `Rudi H`), Group `Head Office`, status header `Waiting for Approval`, Total Asset `5`, Requested By `Agus P`, Request Date `T0 − 8 hari`.
  - DU-003-8: BRW Borrower `Maya Putri` (tampil `Maya P`), Group `Branch Surabaya`, status header `Extension Approval`, Total Asset `4`, Requested By `Rina W`, Request Date `T0 − 7 hari`.
  - DU-003-9: BRW Borrower `Budi Santoso` (tampil `Budi S`), Group `Head Office`, status header `Borrowed`, Total Asset `10`, Requested By `Agus P`, Request Date `T0 − 6 hari`.
  - DU-003-10: BRW pinjaman self-service Borrower `Citra Dewi` (tampil `Citra D`), Group `Head Office`, status header `Borrowed`, Total Asset `1`, Source `Self-service`, Requested By `—`, Request Date `T0 − 5 hari`.
  - DU-003-11: BRW Borrower `Dewi Anggraini` (tampil `Dewi A`), Group `Head Office`, status header `Waiting for Approval`, Total Asset `2`, Requested By `Agus P`, Request Date `T0 − 4 hari`.
  - DU-003-12: BRW Borrower `Fajar Nugroho` (tampil `Fajar N`), Group `Head Office`, status header `Borrowed` dengan penanda `Overdue`, Total Asset `2`, Requested By `Agus P`, Request Date `T0 − 3 hari`.
  - DU-003-13: BRW Borrower `Gita Permata` (tampil `Gita P`), Group `Head Office`, status header `Waiting for Handover`, Total Asset `1`, Requested By `Agus P`, Request Date `T0 − 2 hari`, aset `Router_Mikrotik hAP {runId}`.
  - DU-003-14: BRW Borrower `Hendra Wijaya` (tampil `Hendra W`), Group `Head Office`, status header `Borrowed`, Total Asset `2`, Requested By `Agus P`, Request Date `T0 − 1 hari`, aset `Kamera Canon {runId}`.
  - DU-003-15: BRW Borrower `Intan Safitri` (tampil `Intan S`), Group `Head Office`, status header `Waiting for Approval`, Total Asset `3`, Requested By `Agus P`, Request Date `T0`, aset `Kamera Canon Mark II {runId}`.
  - DU-003-16: 10 aset `Printer Lab Unit {n} {runId}` milik BRW DU-003-9.
  - Urutan default tabel untuk 14 BRW ini: `Fajar N`, `Gita P`, `Ezra S`, `Élan P`, `anggi L`, `Intan S`, `Dewi A`, `Rudi H`, `Maya P`, `Hendra W`, `Citra D`, `Budi S`, `3D H`, `Elan P`.
  - Kata kunci dan rentang yang diketik langkah: DU-003-17 sampai DU-003-30.
  - DU-003-31: 24 aset `Aksesori Kantor {n} {runId}` untuk melengkapi Total Asset BRW DU-003-2 sampai DU-003-15.
- Kondisi:
  - Date Format di General Settings entitas bernilai `dd/MM/yy`.

## Test Steps

### Hasil Search memuat BRW milik spec ini
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi hasil Search memuat 14 baris milik spec ini, dengan 10 baris di halaman pertama dan 4 baris di halaman kedua

### Search by Scan membuka dialog dan mengisi Search dengan Asset ID
3. Klik `Search by Scan`
4. Verifikasi dialog memuat pilihan tipe TAG `RFID`, `QR`, dan `NFC`
5. Pilih tipe TAG `RFID`
6. Scan TAG `E200FFFF0000AAAA` yang tidak terdaftar di perusahaan
7. Verifikasi pesan `Not recognized` tampil dan dialog tetap terbuka
8. Scan TAG aset `Laptop Dell {runId}`
9. Verifikasi dialog tertutup dan kotak Search terisi Asset ID aset `Laptop Dell {runId}`
10. Verifikasi baris Borrower `anggi L` tampil dan baris Borrower `Rudi H` tidak tampil

### Search mencocokkan substring tanpa membedakan huruf besar dan kecil di kolom teks, badge, dan angka
11. Ganti isi kotak search dengan `Rudi H`, tekan Enter
12. Verifikasi baris Borrower `Rudi H` tampil
13. Ganti isi kotak search dengan `Extension Approval`, tekan Enter
14. Verifikasi baris Borrower `Maya P` tampil
15. Ganti isi kotak search dengan `10`, tekan Enter
16. Verifikasi baris Borrower `Budi S` tampil
17. Ganti isi kotak search dengan `urabay`, tekan Enter
18. Verifikasi baris Borrower `Ezra S` dan `Maya P` tampil
19. Verifikasi baris Borrower `Rudi H` tidak tampil
20. Ganti isi kotak search dengan `BRANCH SURABAYA`, tekan Enter
21. Verifikasi baris Borrower `Ezra S` dan `Maya P` tampil
22. Ganti isi kotak search dengan `Tidak Ada {runId}`, tekan Enter
23. Verifikasi pesan `No results found` tampil
24. Ganti isi kotak search dengan `   ` (tiga spasi), tekan Enter
25. Verifikasi pesan `No results found` tidak tampil dan tabel memuat baris

### Kata kunci yang cocok di dua kolom berbeda dan nilai tanggal
26. Ganti isi kotak search dengan `Handover`, tekan Enter
27. Verifikasi baris Borrower `anggi L` (status `Waiting for Handover`) dan baris Borrower `3D H` (aset `Handover Dock Station {runId}`) tampil
28. Ganti isi kotak search dengan `/`, tekan Enter
29. Verifikasi baris Borrower `anggi L` dan `Rudi H` tidak tampil, karena nilai Request Date dan Last Updated tidak ikut dicari

### Spasi di tepi dibuang, spasi di tengah dipertahankan, dan karakter khusus dicari sebagai teks
30. Ganti isi kotak search dengan ` Surabaya ` (spasi di awal dan di akhir), tekan Enter
31. Verifikasi baris Borrower `Ezra S` dan `Maya P` tampil
32. Verifikasi isi kotak search tetap ` Surabaya ` dengan spasi di awal dan di akhir
33. Ganti isi kotak search dengan `Laptop Dell {runId}`, tekan Enter
34. Verifikasi baris Borrower `anggi L` tampil
35. Ganti isi kotak search dengan `Laptop  Dell {runId}` (dua spasi di antara `Laptop` dan `Dell`), tekan Enter
36. Verifikasi pesan `No results found` tampil
37. Ganti isi kotak search dengan `_`, tekan Enter
38. Verifikasi baris Borrower `Gita P` tampil
39. Verifikasi baris Borrower `Rudi H` tidak tampil
40. Ganti isi kotak search dengan `Kamera Canon`, tekan Enter
41. Verifikasi baris Borrower `Hendra W` dan `Intan S` tampil
42. Ganti isi kotak search dengan `Kamera Canon Mark II`, tekan Enter
43. Verifikasi baris Borrower `Intan S` tampil dan baris Borrower `Hendra W` tidak tampil

### Kolom searchable yang disembunyikan tidak lagi cocok dan cocok lagi saat ditampilkan
44. Ganti isi kotak search dengan `Admin`, tekan Enter
45. Verifikasi baris Borrower `Rudi H` tidak tampil karena kolom `Source` tersembunyi
46. Klik header kolom Actions `⋯`
47. Centang `Source` pada panel Column Visibility
48. Verifikasi baris Borrower `Rudi H` dan `Maya P` tampil
49. Verifikasi baris Borrower `Citra D` tidak tampil karena Source `Self-service`
50. Hapus centang `Source` pada panel Column Visibility

### Urutan awal dan sort per kolom
51. Ganti isi kotak search dengan `{runId}`, tekan Enter
52. Verifikasi hasil Search memuat 14 baris milik spec ini
53. Verifikasi urutan baris di halaman pertama: `Fajar N`, `Gita P`, `Ezra S`, `Élan P`, `anggi L`, `Intan S`, `Dewi A`, `Rudi H`, `Maya P`, lalu `Hendra W`
54. Klik header kolom `Borrower`
55. Verifikasi urutan baris di halaman pertama: `3D H`, `anggi L`, `Budi S`, `Citra D`, `Dewi A`, `Elan P`, `Élan P`, `Ezra S`, `Fajar N`, lalu `Gita P`
56. Pindah ke halaman 2
57. Verifikasi urutan baris di halaman kedua: `Hendra W`, `Intan S`, `Maya P`, lalu `Rudi H`
58. Klik header kolom `Borrower`
59. Pindah ke halaman 1
60. Verifikasi urutan baris di halaman pertama: `Rudi H`, `Maya P`, `Intan S`, `Hendra W`, `Gita P`, `Fajar N`, `Ezra S`, `Élan P`, `Elan P`, lalu `Dewi A`
61. Klik header kolom `Total Asset`
62. Verifikasi urutan baris di halaman pertama: `Gita P`, `anggi L`, `Citra D`, `3D H`, `Fajar N`, `Ezra S`, `Élan P`, `Dewi A`, `Hendra W`, lalu `Intan S`
63. Pindah ke halaman 2
64. Verifikasi urutan baris di halaman kedua: `Elan P`, `Maya P`, `Rudi H`, lalu `Budi S`
65. Klik header kolom `Total Asset`
66. Klik header kolom `Total Asset`
67. Verifikasi baris pertama adalah Borrower `Fajar N`, sesuai urutan awal tabel
68. Klik header kolom `Group`
69. Verifikasi urutan baris di halaman pertama: `Ezra S`, `Maya P`, `Elan P`, `Fajar N`, `Gita P`, `Élan P`, `anggi L`, `Intan S`, `Dewi A`, lalu `Rudi H`
70. Pindah ke halaman 2
71. Verifikasi urutan baris di halaman kedua: `Hendra W`, `Citra D`, `Budi S`, lalu `3D H`
72. Klik header kolom `Requested By`
73. Verifikasi urutan baris di halaman kedua: `Ezra S`, `Maya P`, `Elan P`, lalu `Citra D` dengan Requested By `—` di akhir
74. Klik header kolom `Requested By`
75. Pindah ke halaman 1
76. Verifikasi empat baris pertama: `Citra D` dengan Requested By `—` di awal, lalu `Ezra S`, `Maya P`, dan `Elan P`
77. Klik header kolom `Status`
78. Verifikasi urutan baris di halaman pertama sama dengan urutan awal: `Fajar N`, `Gita P`, `Ezra S`, `Élan P`, `anggi L`, `Intan S`, `Dewi A`, `Rudi H`, `Maya P`, lalu `Hendra W`
79. Klik header kolom `Status`
80. Verifikasi enam baris pertama: `Hendra W`, `Citra D`, `Budi S`, `3D H`, `Elan P`, lalu `Maya P`
81. Klik header kolom `Request Date`
82. Verifikasi urutan baris di halaman pertama dari yang terlama: `anggi L`, `Élan P`, `Elan P`, `Ezra S`, `3D H`, `Rudi H`, `Maya P`, `Budi S`, `Citra D`, lalu `Dewi A`
83. Klik header kolom `Request Date`
84. Verifikasi urutan baris di halaman pertama dari yang terbaru: `Intan S`, `Hendra W`, `Gita P`, `Fajar N`, `Dewi A`, `Citra D`, `Budi S`, `Maya P`, `Rudi H`, lalu `3D H`
85. Klik header kolom `Request Date`

### Filter Status mencocokkan opsi dan opsinya dari data tabel
86. Klik `Filter`
87. Klik field `Status`
88. Verifikasi opsi `Waiting for Handover`, `Waiting for Approval`, `Extension Approval`, dan `Borrowed` tampil, dan opsi `Returned` tidak tampil
89. Pilih opsi `Borrowed`
90. Klik `[Apply]`
91. Verifikasi baris Borrower `Elan P`, `3D H`, `Budi S`, `Citra D`, `Fajar N`, dan `Hendra W` tampil
92. Verifikasi baris Borrower `anggi L`, `Ezra S`, `Gita P`, `Élan P`, dan `Maya P` tidak tampil
93. Pilih opsi `Waiting for Handover`
94. Klik `[Apply]`
95. Verifikasi baris Borrower `Elan P`, `anggi L`, `Ezra S`, `Gita P`, dan `Élan P` tampil dan baris Borrower `Rudi H` tidak tampil
96. Hapus pilihan `Waiting for Handover` dari field `Status`

### Filter antar-field berlaku AND
97. Klik `[Clear Field]`
98. Klik `[Apply]`
99. Klik field `Group`
100. Pilih `Branch Surabaya` pada field `Group`
101. Klik `[Apply]`
102. Verifikasi baris Borrower `Ezra S`, `Maya P`, dan `Elan P` tampil dan baris Borrower `3D H` tidak tampil
103. Pilih opsi `Borrowed` pada field `Status`
104. Klik `[Apply]`
105. Verifikasi baris Borrower `Elan P` tampil
106. Verifikasi baris Borrower `3D H`, `Ezra S`, dan `anggi L` tidak tampil

### Filter tetap berlaku saat kolom disembunyikan dan nilai kosong tidak menjadi opsi
107. Klik `[Clear Field]`
108. Klik `[Apply]`
109. Verifikasi isi kotak search tetap `{runId}` dan baris Borrower `Rudi H` tampil
110. Klik field `Source`
111. Pilih opsi `Admin`
112. Klik `[Apply]`
113. Verifikasi baris Borrower `Rudi H` tampil dan baris Borrower `Citra D` tidak tampil, walau kolom `Source` tersembunyi
114. Klik `[Clear Field]`
115. Klik `[Apply]`
116. Klik field `Requested By`
117. Verifikasi opsi `Agus P` dan `Rina W` tampil dan opsi `—` tidak tampil
118. Pilih opsi `Agus P`
119. Klik `[Apply]`
120. Verifikasi baris Borrower `Rudi H` tampil dan baris Borrower `Citra D` tidak tampil

### Filter Overdue memilih satu atau kedua nilai
121. Klik `[Clear Field]`
122. Klik `[Apply]`
123. Klik field `Overdue`
124. Pilih opsi `Overdue`
125. Klik `[Apply]`
126. Verifikasi baris Borrower `Fajar N` tampil dan baris Borrower `Rudi H` tidak tampil
127. Pilih opsi `Not overdue`
128. Klik `[Apply]`
129. Verifikasi baris Borrower `Fajar N` dan `Rudi H` tampil

### Filter rentang Total Asset dan rentang Request Date
130. Klik `[Clear Field]`
131. Klik `[Apply]`
132. Isi Total Asset `Min` dengan `4` dan `Max` dengan `5`
133. Klik `[Apply]`
134. Verifikasi baris Borrower `Maya P` (Total Asset `4`) dan `Rudi H` (Total Asset `5`) tampil
135. Verifikasi baris Borrower `Elan P` (Total Asset `3`) dan `Budi S` (Total Asset `10`) tidak tampil
136. Kosongkan `Min` dan `Max`
137. Isi Total Asset `Min` dengan `10`
138. Klik `[Apply]`
139. Verifikasi baris Borrower `Budi S` tampil dan baris Borrower `Rudi H` tidak tampil
140. Kosongkan `Min`
141. Isi Total Asset `Max` dengan `1`
142. Klik `[Apply]`
143. Verifikasi baris Borrower `Gita P`, `anggi L`, `Citra D`, dan `3D H` tampil dan baris Borrower `Fajar N` tidak tampil
144. Kosongkan `Max`
145. Isi Request Date dengan rentang dari `T0 − 12 hari` sampai `T0 − 10 hari`
146. Klik `[Apply]`
147. Verifikasi baris Borrower `Élan P`, `Elan P`, dan `Ezra S` tampil
148. Verifikasi baris Borrower `anggi L` dan `3D H` tidak tampil

### Irisan Search dan Filter, serta Clear mempertahankan kontrol lain
149. Klik `[Clear Field]`
150. Klik `[Apply]`
151. Ganti isi kotak search dengan `Handover`, tekan Enter
152. Verifikasi baris Borrower `anggi L` dan `3D H` tampil
153. Pilih opsi `Borrowed` pada field `Status`
154. Klik `[Apply]`
155. Verifikasi baris Borrower `3D H` tampil
156. Verifikasi baris Borrower `anggi L` dan `Citra D` tidak tampil
157. Klik header kolom `Borrower`
158. Klik `[Clear Field]`
159. Klik `[Apply]`
160. Verifikasi isi kotak search tetap `Handover` dan baris Borrower `3D H`, `anggi L`, lalu `Élan P` berurutan menurut sort Borrower
161. Pilih opsi `Borrowed` pada field `Status`
162. Klik `[Apply]`
163. Klik `(←)` pada kotak Search
164. Verifikasi baris Borrower `3D H`, `Budi S`, `Citra D`, `Elan P`, `Fajar N`, lalu `Hendra W` tampil berurutan menurut sort Borrower yang tetap berlaku, dan baris Borrower `anggi L` tidak tampil
165. Ketik Search `Handover`, tekan Enter
166. Verifikasi baris Borrower `3D H` tampil dan baris Borrower `Citra D` tidak tampil
167. Klik `[Clear Field]`
168. Klik `[Apply]`
169. Ganti isi kotak search dengan `Surabaya`, tekan Enter
170. Verifikasi baris Borrower `Ezra S` tampil
171. Pilih opsi `Waiting for Approval` pada field `Status`
172. Klik `[Apply]`
173. Verifikasi pesan `No results found` tampil
174. Klik `[Clear Field]`
175. Klik `[Apply]`
176. Verifikasi baris Borrower `Ezra S` dan `Maya P` tampil

### Record yang diubah keluar dari saringan aktif
177. Ganti isi kotak search dengan `{runId}`, tekan Enter
178. Pilih opsi `Waiting for Approval` pada field `Status`
179. Klik `[Apply]`
180. Verifikasi baris Borrower `Rudi H`, `Dewi A`, dan `Intan S` tampil
181. Klik `⋯` pada baris Borrower `Intan S`
182. Klik `Cancel Borrow`
183. Klik `[Cancel Borrow]` pada dialog
184. Verifikasi baris Borrower `Intan S` tidak tampil dan baris Borrower `Rudi H` tetap tampil

### Record yang diubah masuk ke saringan aktif
185. Klik `[Clear Field]`
186. Klik `[Apply]`
187. Klik `⋯` pada baris Borrower `Maya P`
188. Klik `Cancel Extension`
189. Klik `[Cancel Extension]` pada dialog
190. Pilih opsi `Borrowed` pada field `Status`
191. Klik `[Apply]`
192. Verifikasi baris Borrower `Maya P` tampil

### Search by Scan tidak tersedia di tab History
193. Klik tab `History`
194. Verifikasi tombol `Search` tampil dan tombol `Search by Scan` tidak tampil di toolbar tabel

### Search mencakup alias aset dan kode TAG
195. Klik tab `Transactions`
196. Klik `Filter`
197. Klik `[Clear Field]`
198. Klik `[Apply]`
199. Ganti isi kotak search dengan `Laptop Kantor Anggi {runId}`, tekan Enter
200. Verifikasi baris Borrower `anggi L` tampil dan baris Borrower `Rudi H` tidak tampil
201. Ganti isi kotak search dengan `E2003412DF5A-{runId}`, tekan Enter
202. Verifikasi baris Borrower `anggi L` tampil dan baris Borrower `Rudi H` tidak tampil

### Sort Transaction ID dan Last Updated
203. Ganti isi kotak search dengan `{runId}`, tekan Enter
204. Klik header kolom `Transaction ID`
205. Verifikasi urutan baris di halaman pertama sesuai urutan pembuatan BRW dari yang paling awal: `anggi L`, `Élan P`, `Elan P`, `Ezra S`, `3D H`, `Rudi H`, `Maya P`, `Budi S`, `Citra D`, lalu `Dewi A`
206. Klik header kolom `Transaction ID`
207. Verifikasi urutan baris di halaman pertama sesuai urutan pembuatan BRW dari yang paling akhir: `Hendra W`, `Gita P`, `Fajar N`, `Dewi A`, `Citra D`, `Budi S`, `Maya P`, `Rudi H`, `3D H`, lalu `Ezra S`
208. Klik header kolom `Last Updated`
209. Verifikasi urutan baris di halaman pertama dari yang terlama: `anggi L`, `Élan P`, `Elan P`, `Ezra S`, `3D H`, `Rudi H`, `Budi S`, `Citra D`, `Dewi A`, lalu `Fajar N`
210. Klik header kolom `Last Updated`
211. Verifikasi urutan baris di halaman pertama dari yang terbaru: `Maya P`, `Hendra W`, `Gita P`, `Fajar N`, `Dewi A`, `Citra D`, `Budi S`, `Rudi H`, `3D H`, lalu `Ezra S`
212. Klik header kolom `Last Updated`

### Filter rentang Last Updated
213. Isi Last Updated dengan rentang dari `T0 − 12 hari` sampai `T0 − 10 hari`
214. Klik `[Apply]`
215. Verifikasi baris Borrower `Élan P`, `Elan P`, dan `Ezra S` tampil
216. Verifikasi baris Borrower `anggi L` dan `3D H` tidak tampil
217. Klik `[Clear Field]`
218. Klik `[Apply]`

### Hasil scan tetap dipotong filter yang aktif
219. Klik field `Status`
220. Pilih opsi `Waiting for Handover`
221. Klik `[Apply]`
222. Klik `Search by Scan`
223. Pilih tipe TAG `RFID`
224. Scan TAG aset `Laptop Dell {runId}`
225. Verifikasi dialog tertutup dan kotak Search terisi Asset ID aset `Laptop Dell {runId}`
226. Verifikasi baris Borrower `anggi L` tampil dan baris Borrower `Rudi H` tidak tampil
227. Hapus pilihan `Waiting for Handover` dari field `Status`
228. Pilih opsi `Borrowed` pada field `Status`
229. Klik `[Apply]`
230. Verifikasi pesan `No results found` tampil

### Record baru menjadi opsi filter dan tidak tampil bila tidak cocok dengan saringan aktif
231. Klik `[Clear Field]`
232. Klik `[Apply]`
233. Ganti isi kotak search dengan `{runId}`, tekan Enter
234. Pilih opsi `Borrowed` pada field `Status`
235. Klik `[Apply]`
236. Klik field `Borrower`
237. Verifikasi opsi `Hendra W` tampil dan opsi `Zahra L` tidak tampil
238. Agus Pratama mengajukan BRW baru untuk Borrower `Zahra Lubis` dengan aset `Webcam Logitech C920 {runId}` lewat form Borrow Request, sehingga BRW itu berstatus `Waiting for Approval`
239. Tutup daftar opsi field `Borrower`
240. Klik field `Borrower`
241. Verifikasi opsi `Zahra L` tampil pada field `Borrower` tanpa muat ulang halaman
242. Verifikasi baris Borrower `Hendra W` tampil dan baris Borrower `Zahra L` tidak tampil

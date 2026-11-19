---
id: TC-FA-BORROW-E2E-019-approval-review-keputusan-per-aset
title: "Halaman Review Approval memutuskan setiap aset dengan Approve atau Reject, Approve Duration, dan Approval Note"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["F-BORROW-05", "FI-BRW-206", "FI-BRW-211", "FI-BRW-212", "§4.1g#p1", "§4.1g#r1", "§4.1g#r2", "§4.1g#r3", "§4.1g#r4", "§4.1g#r5", "§4.1g#r6", "§4.1g#r7", "§4.1g#r8", "§4.1g#r9", "§4.1g#r10", "§4.1g#r11", "§4.1g#r12", "§4.1g#r13", "§4.1g#r14", "§4.1g#r15", "§4.1g#r16", "§4.1g#r17", "§4.1g#r18", "§4.2.9#p1", "§4.3#r4", "§4.4#r7", "§4.4#r8", "§4.4#r9"]
smoke: []
dependsOn: []
trace:
  "F-BORROW-05": [133, 140, 230, 231, 232]
  "FI-BRW-206": 131
  "FI-BRW-211": 137
  "FI-BRW-212": 137
  "§4.1g#p1": [7, 65, 66, 118, 119, 224, 226]
  "§4.1g#r1": [9, 227]
  "§4.1g#r2": [10, 21, 27, 28, 94, 95]
  "§4.1g#r3": [11, 68, 70]
  "§4.1g#r4": [12, 25, 30, 47, 48]
  "§4.1g#r5": [13, 32, 73, 100, 101]
  "§4.1g#r6": [16, 53, 54, 75, 83]
  "§4.1g#r7": [17, 59, 60, 77, 85]
  "§4.1g#r8": [18, 23, 87, 91, 153]
  "§4.1g#r9": [19, 34, 79]
  "§4.1g#r10": [154, 167, 185, 186, 200, 217, 229, 238]
  "§4.1g#r11": [155, 162, 173, 174, 179, 180, 202, 212]
  "§4.1g#r12": [156, 197, 204, 210]
  "§4.1g#r13": [157, 191, 192, 195, 206, 218, 220, 241]
  "§4.1g#r14": [158, 208, 214]
  "§4.1g#r15": [20, 36, 41, 42, 81, 106, 107, 112, 113, 116]
  "§4.1g#r16": [118, 120]
  "§4.1g#r17": [118, 120, 122, 216, 220, 239, 241]
  "§4.1g#r18": [118, 127]
  "§4.2.9#p1": 8
  "§4.3#r4": 8
  "§4.4#r7": 145
  "§4.4#r8": 147
  "§4.4#r9": [127, 146]
anchor: [6, 64, 90, 170, 196, 222]
coverage:
  web: automated
---

# Halaman Review Approval memutuskan setiap aset dengan Approve atau Reject, Approve Duration, dan Approval Note

## Prerequisites
- Aktor: Rina W, Approver (Role Transaksi `Approver`) pada Group `Head Office` dan `Branch Surabaya`.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-019-1: pengajuan approval tipe `Borrow` di antrean Active Rina W, Group `Head Office`, Borrower `Nadia Putri {runId}`, Requested By `Agus Pratama {runId}`, Total Asset `5`, dengan aset DU-019-2 sampai DU-019-6.
  - DU-019-2: aset `Laptop Latitude {runId}`, Brand `Dell`, Model/Type `Latitude 5420`, TAG `RFID`, Category `Laptop`, tanpa foto, Duration `3 / 3 days`, Purpose `Presentasi klien`, Approval Rule `Any one approver · Waiting` (approver Rina W dan `Wawan Setiawan {runId}`).
  - DU-019-3: aset `Proyektor Epson {runId}`, Brand `Epson`, Model/Type `EB-X49`, TAG `QR`, Category `Proyektor`, Duration `2 / 7 days`, Purpose `Rapat divisi`, Approval Rule `Rina W (You) · Waiting` (satu approver, Rina W).
  - DU-019-4: aset `Kamera Sony Alpha {runId}`, Brand `Sony`, Model/Type `A7 III`, TAG `NFC`, Category `Kamera`, Duration `4 / 7 days`, Purpose `Dokumentasi acara`, Approval Rule `All approvers · 0 of 2 approved` (approver Rina W dan `Wawan Setiawan {runId}`).
  - DU-019-5: aset `Tripod Manfrotto {runId}`, Brand `Manfrotto`, Model/Type `MT055`, TAG `Non TAG`, Category `Aksesori Kamera`, Duration `30 / 72 hours`, Purpose `Dokumentasi acara`, Approval Rule `Wawan Setiawan {runId} · Waiting` (satu approver, bukan Rina W).
  - DU-019-6: aset `Mikrofon Rode {runId}`, Brand `Rode`, Model/Type `VideoMic Pro`, TAG `RFID`, Category `Audio`, Duration `5 / 5 days`, Purpose `Wawancara lapangan`, Approval Rule `Rina W (You) · Waiting` (satu approver, Rina W).
  - Asset ID tiap aset dibentuk sistem dan menjadi milik entri aset itu.
  - DU-019-7: pengajuan approval tipe `Extension` di antrean Active Rina W, Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Requested By `Lina Setiawati {runId}`, Total Asset `2`, dengan aset DU-019-8 dan DU-019-10.
  - DU-019-8: aset `Toyota Avanza {runId}`, Brand `Toyota`, Model/Type `Avanza 1.5 G`, TAG `RFID`, Category `Kendaraan`, Current Due Date T0 + 1 hari, Extensions `0 / 1`, Extend By `2 days`, New Due Date T0 + 3 hari (dari Current Due Date T0 + 1 hari ditambah Extend By 2 hari), Reason `Perjalanan dinas diperpanjang`, Approval Rule `Any one approver · Waiting` (approver Rina W dan `Wawan Setiawan {runId}`).
  - DU-019-10: aset `Printer Canon G3010 {runId}`, Brand `Canon`, Model/Type `G3010`, TAG `QR`, Category `Printer`, Current Due Date T0 + 5 hari, pukul 14:00, Extensions `2 / 3`, Extend By `12 hours`, New Due Date T0 + 6 hari, pukul 02:00 (dari Current Due Date T0 + 5 hari, pukul 14:00 ditambah Extend By 12 jam), Reason `Acara vendor mundur`, Approval Rule `Any one approver · Waiting` (approver Rina W dan `Wawan Setiawan {runId}`).
  - DU-019-9: user `Wawan Setiawan {runId}`, Approver (Role Transaksi `Approver`) pada Group `Head Office` dan `Branch Surabaya`.
  - DU-019-11: pengajuan approval tipe `Extension` di antrean Active Rina W, Group `Head Office`, Borrower `Maya Sari {runId}`, Requested By `Lina Setiawati {runId}`, Total Asset `1`, dengan aset DU-019-12.
  - DU-019-12: aset `Genset Honda {runId}`, Brand `Honda`, Model/Type `EU20i`, TAG `QR`, Category `Peralatan`, Current Due Date T0 − 2 hari (sudah lewat), Extensions `0 / 1`, Extend By `2 days`, Reason `Proyek sipil belum selesai`, Approval Rule `Any one approver · Waiting` (approver Rina W dan `Wawan Setiawan {runId}`).
  - Approval Note yang diisi pada baris DU-019-8: `Disetujui untuk kunjungan cabang`.

## Test Steps

### Membuka halaman Review dari antrean Active
1. Klik `Approvals` pada sidebar
2. Klik `Borrow`
3. Ketik Search `Nadia Putri {runId}`, tekan Enter
4. Klik menu ⋯ pada baris DU-019-1
5. Klik `Review`
6. Verifikasi halaman Review pengajuan DU-019-1 terbuka dengan breadcrumb `Approvals > Borrow > Active > Review`
7. Verifikasi tabel aset memuat seluruh aset pengajuan DU-019-1, yaitu aset DU-019-2, DU-019-3, DU-019-4, DU-019-5, dan DU-019-6, termasuk aset milik approver lain
8. Verifikasi notice `You cannot decide a borrow you requested or borrow for.` tidak tampil dan tombol `[Submit]` tampil karena Rina W bukan pengaju, Borrower, maupun PIC Borrower

### Isi kolom tabel aset pada pengajuan Borrow
9. Verifikasi kolom Photo baris DU-019-2 menampilkan placeholder gambar standar
10. Verifikasi kolom Name baris DU-019-2 menampilkan `Laptop Latitude {runId}` diikuti Increment
11. Verifikasi kolom Asset ID baris DU-019-2 menampilkan Asset ID milik DU-019-2
12. Verifikasi kolom Brand baris DU-019-2 `Dell` dan baris DU-019-3 `Epson`
13. Verifikasi kolom Model/Type baris DU-019-2 `Latitude 5420` dan baris DU-019-3 `EB-X49`
14. Buka Setup Column
15. Tampilkan kolom `TAG` dan `Category`
16. Verifikasi kolom TAG baris DU-019-2 menampilkan TAG `RFID` dan baris DU-019-5 menampilkan `—`
17. Verifikasi kolom Category baris DU-019-2 `Laptop` dan baris DU-019-4 `Kamera`
18. Verifikasi kolom Duration baris DU-019-2 `3 / 3 days`, baris DU-019-3 `2 / 7 days`, dan baris DU-019-5 `30 / 72 hours`
19. Verifikasi kolom Purpose baris DU-019-2 `Presentasi klien` dan baris DU-019-3 `Rapat divisi`
20. Verifikasi kolom Approval Rule baris DU-019-2 `Any one approver · Waiting`, baris DU-019-3 `Rina W (You) · Waiting`, baris DU-019-4 `All approvers · 0 of 2 approved`, dan baris DU-019-5 `Wawan Setiawan {runId} · Waiting`

### Sort, search, dan filter tabel aset
21. Verifikasi urutan awal baris dari atas ke bawah adalah DU-019-4, DU-019-2, DU-019-6, DU-019-3, DU-019-5 (Name A–Z)
22. Urutkan kolom `Duration` dengan `Shortest First`
23. Verifikasi urutan dari atas ke bawah adalah DU-019-5, DU-019-3, DU-019-2, DU-019-4, DU-019-6, dengan `30 / 72 hours` dihitung lebih pendek daripada `2 / 7 days` (30 jam lawan 48 jam)
24. Urutkan kolom `Brand` secara Alphabetical (A–Z)
25. Verifikasi urutan dari atas ke bawah adalah DU-019-2, DU-019-3, DU-019-5, DU-019-6, DU-019-4
26. Ketik Search `Kamera Sony Alpha {runId}`, tekan Enter
27. Verifikasi baris DU-019-4 tampil
28. Verifikasi baris DU-019-2, DU-019-3, DU-019-5, dan DU-019-6 tidak tampil
29. Ganti isi kotak search dengan `Dell`, tekan Enter
30. Verifikasi baris DU-019-2 tampil melalui kolom Brand `Dell`, bukan melalui Name aset
31. Ganti isi kotak search dengan `Latitude 5420`, tekan Enter
32. Verifikasi baris DU-019-2 tampil
33. Ganti isi kotak search dengan `Presentasi klien`, tekan Enter
34. Verifikasi baris DU-019-2 tampil
35. Ganti isi kotak search dengan `All approvers`, tekan Enter
36. Verifikasi baris DU-019-4 tampil
37. Klik `(←)` pada kotak Search
38. Klik ikon Filter
39. Pada field `Approval Type` pilih `All approvers`
40. Klik `[Apply]`
41. Verifikasi baris DU-019-4 tampil
42. Verifikasi baris DU-019-2, DU-019-3, DU-019-5, dan DU-019-6 tidak tampil
43. Klik `[Clear Field]`
44. Klik `[Apply]`
45. Pada field `Brand` pilih `Dell` dan `Epson`
46. Klik `[Apply]`
47. Verifikasi baris DU-019-2 dan DU-019-3 tampil
48. Verifikasi baris DU-019-4, DU-019-5, dan DU-019-6 tidak tampil
49. Klik `[Clear Field]`
50. Klik `[Apply]`
51. Pada field `TAG` pilih `RFID`
52. Klik `[Apply]`
53. Verifikasi baris DU-019-2 dan DU-019-6 tampil
54. Verifikasi baris DU-019-3, DU-019-4, dan DU-019-5 tidak tampil
55. Klik `[Clear Field]`
56. Klik `[Apply]`
57. Pada field `Category` pilih `Audio`
58. Klik `[Apply]`
59. Verifikasi baris DU-019-6 tampil
60. Verifikasi baris DU-019-2, DU-019-3, DU-019-4, dan DU-019-5 tidak tampil
61. Klik `[Clear Field]`
62. Klik `[Apply]`
63. Klik ikon Filter

### Toolbar halaman Review memuat Search dengan placeholder dan Filter, tanpa Download
64. Verifikasi `Filter` tampil pada toolbar halaman Review
65. Verifikasi kotak Search yang kosong pada toolbar halaman Review memuat placeholder `Search asset name or ID...`
66. Verifikasi `Download` tidak tampil pada toolbar halaman Review

### Sort dan search kolom Asset ID
67. Urutkan kolom `Asset ID` secara Alphabetical (A–Z)
68. Verifikasi urutan baris dari atas ke bawah mengikuti urutan alfabetis natural Asset ID yang tampil pada tiap baris, untuk kelima baris DU-019-2 sampai DU-019-6
69. Ketik Search Asset ID milik DU-019-2, tekan Enter
70. Verifikasi baris DU-019-2 tampil
71. Klik `(←)` pada kotak Search

### Sort kolom Model/Type, TAG, Category, Purpose, dan Approval Rule
72. Urutkan kolom `Model/Type` secara Alphabetical (A–Z)
73. Verifikasi urutan dari atas ke bawah adalah DU-019-4, DU-019-3, DU-019-2, DU-019-5, DU-019-6
74. Urutkan kolom `TAG` secara Alphabetical (A–Z)
75. Verifikasi baris DU-019-4 berada di atas baris DU-019-3, dan baris DU-019-3 berada di atas baris DU-019-2 dan DU-019-6
76. Urutkan kolom `Category` secara Alphabetical (A–Z)
77. Verifikasi urutan dari atas ke bawah adalah DU-019-5, DU-019-6, DU-019-4, DU-019-2, DU-019-3
78. Urutkan kolom `Purpose` secara Alphabetical (A–Z)
79. Verifikasi baris DU-019-4 dan DU-019-5 berada di atas baris DU-019-2, baris DU-019-2 berada di atas baris DU-019-3, dan baris DU-019-3 berada di atas baris DU-019-6
80. Urutkan kolom `Approval Rule` secara Alphabetical (A–Z)
81. Verifikasi baris DU-019-4 berada di atas baris DU-019-2, baris DU-019-2 berada di atas baris DU-019-3 dan DU-019-6, dan baris DU-019-3 dan DU-019-6 berada di atas baris DU-019-5

### Search kolom TAG, Category, dan Duration
82. Ketik Search `NFC`, tekan Enter
83. Verifikasi baris DU-019-4 tampil
84. Ganti isi kotak search dengan `Audio`, tekan Enter
85. Verifikasi baris DU-019-6 tampil
86. Ganti isi kotak search dengan `3 / 3 days`, tekan Enter
87. Verifikasi baris DU-019-2 tampil
88. Klik `(←)` pada kotak Search

### Filter Asset Name, Model/Type, dan Approval Type, serta kolom Duration tanpa filter
89. Klik ikon Filter
90. Verifikasi field `Brand` dan `Approval Type` tampil di Filter Panel
91. Verifikasi field `Duration` tidak tampil di Filter Panel
92. Pada field `Asset Name` pilih `Kamera Sony Alpha {runId}`
93. Klik `[Apply]`
94. Verifikasi baris DU-019-4 tampil
95. Verifikasi baris DU-019-2, DU-019-3, DU-019-5, dan DU-019-6 tidak tampil
96. Klik `[Clear Field]`
97. Klik `[Apply]`
98. Pada field `Model/Type` pilih `Latitude 5420`
99. Klik `[Apply]`
100. Verifikasi baris DU-019-2 tampil
101. Verifikasi baris DU-019-3, DU-019-4, DU-019-5, dan DU-019-6 tidak tampil
102. Klik `[Clear Field]`
103. Klik `[Apply]`
104. Pada field `Approval Type` pilih `Any one approver`
105. Klik `[Apply]`
106. Verifikasi baris DU-019-2 tampil
107. Verifikasi baris DU-019-3, DU-019-4, DU-019-5, dan DU-019-6 tidak tampil
108. Klik `[Clear Field]`
109. Klik `[Apply]`
110. Pada field `Approval Type` pilih `Single approver`
111. Klik `[Apply]`
112. Verifikasi baris DU-019-3, DU-019-5, dan DU-019-6 tampil
113. Verifikasi baris DU-019-2 dan DU-019-4 tidak tampil
114. Klik `[Clear Field]`
115. Klik `[Apply]`
116. Verifikasi field `Approval Type` memuat placeholder `All approval types`
117. Klik ikon Filter

### Aset milik approver lain tampil read-only
118. Verifikasi baris DU-019-5 menampilkan keterangan `Not your approval` pada kontrol Approval, Approve Duration, dan Approval Note
119. Verifikasi checkbox baris DU-019-5 tidak dapat dicentang

### Keputusan per aset: Approve Duration, Reject, dan Approval Note
120. Verifikasi toggle Approval baris DU-019-2 `Approve` dan Approve Duration baris DU-019-2 `3` sesuai Duration yang diminta
121. Isi Approve Duration baris DU-019-2 dengan `4`
122. Verifikasi Approve Duration baris DU-019-2 menjadi `3`, dijepit ke durasi yang diminta, tanpa pesan di bawah input[^drift-1]
123. Isi Approve Duration baris DU-019-2 dengan `2`
124. Ubah toggle Approval baris DU-019-3 menjadi `Reject`
125. Isi Approve Duration baris DU-019-6 dengan `0`
126. Klik `[Submit]`
127. Verifikasi caption `Approval note must not be empty` tampil pada baris DU-019-3 dan baris DU-019-6
128. Isi Approval Note baris DU-019-3 dengan `Proyektor dipakai kegiatan lain`
129. Isi Approval Note baris DU-019-6 dengan `Durasi terlalu panjang untuk kegiatan ini`
130. Klik `[Submit]`
131. Verifikasi dialog `Submit Approval` tampil dengan teks `You will submit this transaction approval. Asset with 0 approved duration will be rejected and will not appear in the next step of transaction. Are you sure you want to submit it?`
132. Klik `[Submit]` pada dialog `Submit Approval`
133. Verifikasi toast `Success, your approval has been recorded. Waiting for the other approvers.` tampil

### Hasil keputusan tercatat di History dan Detail
134. Klik `Borrow` pada sidebar
135. Klik tab `History`
136. Ketik Search `Nadia Putri {runId}`, tekan Enter
137. Verifikasi baris DU-019-1 tampil di tab `History` dengan Status `Partially Approved`
138. Klik tab `Active`
139. Ketik Search `Nadia Putri {runId}`, tekan Enter
140. Verifikasi tabel Active menampilkan `No results found`
141. Klik tab `History`
142. Ketik Search `Nadia Putri {runId}`, tekan Enter
143. Klik menu ⋯ pada baris DU-019-1
144. Klik `Detail`
145. Verifikasi keputusan aset DU-019-2 `Approved` sebagai keputusan pertama pada mode Any one approver
146. Verifikasi keputusan aset DU-019-3 `Rejected` dan aset DU-019-6 `Rejected`
147. Verifikasi kolom Approval Rule aset DU-019-4 `All approvers · 1 of 2 approved` dan keputusannya `Waiting`

### Kolom khusus pengajuan Extension pada halaman Review
148. Klik `Borrow` pada sidebar
149. Klik tab `Active`
150. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
151. Klik menu ⋯ pada baris DU-019-7
152. Klik `Review`
153. Verifikasi kolom Duration baris DU-019-8 menampilkan `—`
154. Verifikasi kolom Current Due Date baris DU-019-8 menampilkan tanggal Current Due Date milik DU-019-8 menurut format General Settings
155. Verifikasi kolom Extensions baris DU-019-8 `0 / 1`
156. Verifikasi kolom Extend By baris DU-019-8 `2 days`
157. Verifikasi kolom New Due Date baris DU-019-8 menampilkan tanggal New Due Date milik DU-019-8 menurut format General Settings
158. Verifikasi kolom Reason baris DU-019-8 `Perjalanan dinas diperpanjang`
159. Klik ikon Filter
160. Isi field `Extensions` dengan Min `1` dan Max `1`
161. Klik `[Apply]`
162. Verifikasi tabel aset menampilkan `No results found`
163. Klik `[Clear Field]`
164. Klik `[Apply]`
165. Pada field `Current Due Date` pilih rentang dari T0 + 2 hari sampai T0 + 4 hari
166. Klik `[Apply]`
167. Verifikasi tabel aset menampilkan `No results found`
168. Klik `[Clear Field]`
169. Klik `[Apply]`
170. Verifikasi baris DU-019-8 tampil kembali setelah filter dibersihkan

### Filter kolom khusus pengajuan Extension menyaring baris yang cocok
171. Isi field `Extensions` dengan Min `0` dan Max `0`
172. Klik `[Apply]`
173. Verifikasi baris DU-019-8 tampil
174. Verifikasi baris DU-019-10 tidak tampil
175. Klik `[Clear Field]`
176. Klik `[Apply]`
177. Isi field `Extensions` dengan Min `2` dan Max `2`
178. Klik `[Apply]`
179. Verifikasi baris DU-019-10 tampil
180. Verifikasi baris DU-019-8 tidak tampil
181. Klik `[Clear Field]`
182. Klik `[Apply]`
183. Pada field `Current Due Date` pilih rentang dari T0 sampai T0 + 2 hari
184. Klik `[Apply]`
185. Verifikasi baris DU-019-8 tampil
186. Verifikasi baris DU-019-10 tidak tampil
187. Klik `[Clear Field]`
188. Klik `[Apply]`
189. Pada field `New Due Date` pilih rentang dari T0 + 3 hari sampai T0 + 4 hari
190. Klik `[Apply]`
191. Verifikasi baris DU-019-8 tampil
192. Verifikasi baris DU-019-10 tidak tampil
193. Klik `[Clear Field]`
194. Klik `[Apply]`
195. Verifikasi field `New Due Date` memuat placeholder `Select date`
196. Verifikasi field `Current Due Date` dan `Extensions` tampil di Filter Panel
197. Verifikasi field `Extend By` tidak tampil di Filter Panel
198. Klik ikon Filter

### Sort kolom khusus pengajuan Extension
199. Urutkan kolom `Current Due Date` dengan `Newest First`
200. Verifikasi urutan dari atas ke bawah adalah DU-019-10, DU-019-8
201. Urutkan kolom `Extensions` secara Numeric
202. Verifikasi urutan dari atas ke bawah adalah DU-019-8, DU-019-10
203. Urutkan kolom `Extend By` dengan `Shortest First`
204. Verifikasi urutan dari atas ke bawah adalah DU-019-10, DU-019-8, dengan `12 hours` dihitung lebih pendek daripada `2 days`
205. Urutkan kolom `New Due Date` dengan `Newest First`
206. Verifikasi urutan dari atas ke bawah adalah DU-019-10, DU-019-8
207. Urutkan kolom `Reason` secara Alphabetical (A–Z)
208. Verifikasi urutan dari atas ke bawah adalah DU-019-10, DU-019-8

### Search kolom Extension mencari Extend By, Extensions, dan Reason
209. Ketik Search `12 hours`, tekan Enter
210. Verifikasi baris DU-019-10 tampil
211. Ganti isi kotak search dengan `2 / 3`, tekan Enter
212. Verifikasi baris DU-019-10 tampil
213. Ganti isi kotak search dengan `Acara vendor mundur`, tekan Enter
214. Verifikasi baris DU-019-10 tampil
215. Klik `(←)` pada kotak Search

### Approve Duration default dan New Due Date dihitung ulang pada pengajuan Extension
216. Verifikasi Approve Duration baris DU-019-8 `2` sesuai Extend By yang diminta
217. Verifikasi kolom Current Due Date baris DU-019-10 menampilkan tanggal dan jam Current Due Date milik DU-019-10 menurut format General Settings
218. Verifikasi kolom New Due Date baris DU-019-10 menampilkan tanggal dan jam New Due Date milik DU-019-10 menurut format General Settings
219. Isi Approve Duration baris DU-019-8 dengan `1`
220. Verifikasi kolom New Due Date baris DU-019-8 menampilkan tanggal T0 + 2 hari menurut format General Settings, dari Current Due Date T0 + 1 hari ditambah Approve Duration `1`

### Search tidak mencocokkan isi kontrol keputusan dan kolom Photo tidak dapat diurutkan
221. Isi Approval Note baris DU-019-8 dengan `Disetujui untuk kunjungan cabang`
222. Verifikasi Approval Note baris DU-019-8 berisi `Disetujui untuk kunjungan cabang`
223. Ketik Search `Disetujui untuk kunjungan cabang`, tekan Enter
224. Verifikasi tabel aset menampilkan `No results found`, karena isi kontrol `Approval Note` tidak masuk Search
225. Klik `(←)` pada kotak Search
226. Verifikasi baris DU-019-8 tampil kembali setelah search dibersihkan
227. Verifikasi header kolom `Photo` tidak menyediakan opsi urut

### Sort Current Due Date dengan Oldest First
228. Urutkan kolom `Current Due Date` dengan `Oldest First`
229. Verifikasi urutan dari atas ke bawah adalah DU-019-8, DU-019-10

### Header dan footer halaman Review
230. Verifikasi judul halaman Review berformat `BRW-YYYY-NNNN` dengan ikon copy, disertai badge tipe `Extension` dan badge `Waiting for Approval`
231. Verifikasi footer halaman Review memuat `[Cancel]` dan `[Submit]`
232. Verifikasi aksi keputusan pada halaman Review hanya Approve dan Reject, tanpa aksi tanya jawab atau permintaan keterangan tambahan

### New Due Date dihitung dari hari ini bila Due Date saat ini sudah lewat
233. Klik `Borrow` pada sidebar
234. Klik tab `Active`
235. Ketik Search `Maya Sari {runId}`, tekan Enter
236. Klik menu ⋯ pada baris DU-019-11
237. Klik `Review`
238. Verifikasi kolom Current Due Date baris DU-019-12 menampilkan tanggal Current Due Date milik DU-019-12 menurut format General Settings
239. Verifikasi Approve Duration baris DU-019-12 `2` sesuai Extend By yang diminta
240. Isi Approve Duration baris DU-019-12 dengan `1`
241. Verifikasi kolom New Due Date baris DU-019-12 menampilkan tanggal T0 + 1 hari menurut format General Settings, dihitung dari hari ini ditambah Approve Duration `1`, karena Current Due Date T0 − 2 hari sudah lewat

[^drift-1]: Drift PRD vs kontrak komponen. PRD §4.1g (kontrol keputusan T-BRW-08), V-BRW-27, dan FLD-BRW-17: Approve Duration yang melebihi durasi diminta ditolak dengan caption `Max. [Requested] [Unit]` di bawah input. Kontrak `NumberInput#1`: `min` dan `max` adalah rentang, bukan filter ketik; nilai di luar rentang dijepit ke batas terdekat saat blur atau Enter. Kontrak `NumberInput#15`: tidak ada pesan rentang dan tidak ada state invalid untuk nilai di luar `min`/`max`. Diasersi: kontrak, nilai dijepit ke durasi diminta tanpa caption (SB-7).

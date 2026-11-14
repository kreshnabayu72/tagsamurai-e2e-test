---
id: TC-FA-MISS-UI-051-tabel-active-mekanik
title: "Tabel Active: siklus Search, Filter Panel, sort indikator, Setup Column, paginasi, dan isolasi state per tab"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EB-SRC-4@tabel-active, EB-FLT-2@tabel-active, EB-FLT-6@tabel-active, EB-SRT-3@tabel-active, EB-KOL-1@tabel-active, EB-KOL-3, EB-TBL-7@tabel-active, §4.4#r1, §5#r2, §9.5#r4, §4.1a#p1, §4.1a#r6, §4.1a#r1, §4.5#p1, §4.3#r5, EB-DL-2@tabel-active]
smoke: []
dependsOn: []
trace:
  EB-SRC-4@tabel-active: [3, 5, 7, 8, 10, 11, 12, 14, 16, 17, 19, 20]
  EB-FLT-2@tabel-active: [40, 42, 46, 48, 49, 51, 54, 55, 57, 58, 59, 70, 72, 74]
  EB-FLT-6@tabel-active: [89, 92, 93, 94, 95]
  EB-SRT-3@tabel-active: [22, 24, 26, 28, 30, 32, 33, 34]
  EB-KOL-1@tabel-active: [99, 100, 101, 102, 103, 104, 110, 111, 116, 122, 129, 131, 133, 139, 141, 147, 155, 157, 159]
  EB-KOL-3: [168, 169, 171]
  EB-TBL-7@tabel-active: [191, 193, 198, 200, 202, 204]
  §4.4#r1: [178, 180, 181, 182, 184, 185]
  §5#r2: [187, 189, 194, 211]
  §9.5#r4: [187, 189, 194, 206, 207, 214, 216]
  §4.1a#p1: [57, 58, 82, 83]
  §4.1a#r6: [22, 30]
  §4.1a#r1: 34
  §4.5#p1: [77, 151]
  §4.3#r5: [163, 164]
  EB-DL-2@tabel-active: 220
anchor: []
coverage:
  web: automated
---

# Tabel Active: siklus Search, Filter Panel, sort indikator, Setup Column, paginasi, dan isolasi state per tab

## Prerequisites
- Aktor: Group Manager (Aktor Missing) tanpa hak nilai finansial.
- Layar awal: Assets > Missing > Active.
- Komponen: Halaman Missing sub-tab Active (tabel T-MIS-01)
- Data:
  - DU-051-1: Sebelas record Missing untuk dua halaman. Name `Aset Paginasi {n}`; Asset ID `PGN-2026-{n}`; Group `Head Office`; Status `Missing`; Source `Manual`; Last Holder `null`; Last Seen `Unknown`; Reported By `Rina Wulandari`; Reported Date `2026-11-01T08:00:00Z`; Days Missing `10`; Last Updated `2026-11-01T08:00:00Z`.
  - DU-051-2: Sepuluh record Missing tepat satu halaman. Name `Aset Tepat Sepuluh {n}`; Asset ID `TPT-2026-{n}`; Group `Head Office`; Status `Missing`; Source `Manual`; Last Holder `null`; Last Seen `Unknown`; Reported By `Rina Wulandari`; Reported Date `2026-11-01T08:00:00Z`; Days Missing `10`; Last Updated `2026-11-01T08:00:00Z`.
  - DU-051-3: Dua puluh enam record Missing untuk ukuran halaman 25. Name `Aset Dua Puluh Enam {n}`; Asset ID `DPE-2026-{n}`; Group `Head Office`; Status `Missing`; Source `Manual`; Last Holder `null`; Last Seen `Unknown`; Reported By `Rina Wulandari`; Reported Date `2026-11-01T08:00:00Z`; Days Missing `10`; Last Updated `2026-11-01T08:00:00Z`.
  - DU-051-4: Dua belas record Missing hasil pencarian tersaring. Name `Aset Tersaring {n}`; Asset ID `TSR-2026-{n}`; Group `Head Office`; Status `Missing`; Source `Manual`; Last Holder `null`; Last Seen `Unknown`; Reported By `Rina Wulandari`; Reported Date `2026-11-01T08:00:00Z`; Days Missing `10`; Last Updated `2026-11-01T08:00:00Z`.
  - DU-051-5: Input nomor halaman tidak valid. Input nomor halaman `0 | -1 | 2 | abc`.
  - DU-051-6: Record Waiting for Confirmation dengan TAG RFID. Name `Laptop Asus Vivobook - 1`; Asset ID `LPT-2026-0101`; Group `Head Office`; Status `Waiting for Confirmation`; Source `Reported by holder`; Last Holder `Sari Dewanti`; Last Seen `Unknown`; Reported By `Sari Dewanti`; Reported Date `2026-11-08T11:00:00Z`; Days Missing `3`; Last Updated `2026-11-08T11:00:00Z`; TAG `RFID`.
  - DU-051-7: Record Missing dengan TAG NFC dan QR. Name `Printer Canon Pixma - 2`; Asset ID `PRN-2026-0102`; Group `Branch Surabaya`; Status `Missing`; Source `Manual`; Last Holder `null`; Last Seen `2026-11-05T10:00:00Z · Lobby reader`; Reported By `Agus Prasetyo`; Reported Date `2026-11-06T09:00:00Z`; Days Missing `5`; Last Updated `2026-11-06T09:00:00Z`; TAG `NFC, QR`.
  - DU-051-8: Record Missing dengan TAG QR. Name `Scanner Honeywell - 3`; Asset ID `SCN-2026-0103`; Group `Warehouse`; Status `Missing`; Source `Borrow`; Last Holder `Andi Pratama`; Last Seen `2026-10-05T09:00:00Z · Gate A reader`; Reported By `Andi Pratama`; Reported Date `2026-10-05T09:00:00Z`; Days Missing `37`; Last Updated `2026-11-07T00:00:00Z`; TAG `QR`.
  - DU-051-9: Record History Rejected. Name `Camera Canon EOS - 1`; Asset ID `CAM-2026-0001`; Group `Head Office`; Status `Rejected`; Source `Reported by holder`; Last Holder `Budi Santoso`; Reported By `Budi Santoso`; Reported Date `2026-11-05T08:30:00Z`; Duration `1`; Resolved By `Rina Wulandari`; Resolved Date `2026-11-06T09:15:00Z`.
  - DU-051-10: Opsi filter Source: nilai DISTINCT dari baris DU-051-6 sampai DU-051-8 dan DU-051-12 sampai DU-051-15. Source `Borrow, Reported by holder, Stock opname, Transfer, Manual, Work order, Reconciliation`.
  - DU-051-11: Kata kunci Search dan kata kunci opsi filter. Kata kunci Search `Canon`; Kata kunci Search tersaring `Aset Tersaring`; Kata kunci opsi filter tanpa hasil `ZZZ-TIDAK-ADA`.
  - DU-051-12: Record Reported Disposal dengan Source Stock opname. Name `Projector Epson EB-X06 - 7`; Asset ID `PRJ-2026-0007`; Group `Branch Surabaya`; Status `Reported Disposal`; Source `Stock opname`; Last Holder `null`; Last Seen `2026-09-15T14:05:00Z · Agus P`; Reported By `Agus Prasetyo`; Reported Date `2026-10-01T08:00:00Z`; Days Missing `41`; Last Updated `2026-11-05T15:30:00Z`.
  - DU-051-13: Record In Disposal Process dengan Source Work order. Name `Printer HP LaserJet M404 - 5`; Asset ID `PRN-2026-0005`; Group `Head Office`; Status `In Disposal Process`; Source `Work order`; Last Holder `null`; Last Seen `2026-08-20T16:40:00Z · Lobby reader`; Reported By `Rina Wulandari`; Reported Date `2026-08-25T10:00:00Z`; Days Missing `78`; Last Updated `2026-11-02T11:20:00Z`.
  - DU-051-14: Record Missing dengan Source Transfer. Name `Toyota Innova - 2`; Asset ID `VEH-2026-0002`; Group `Branch Surabaya`; Status `Missing`; Source `Transfer`; Last Holder `null`; Last Seen `2026-10-31T16:20:00Z · Gate B reader`; Reported By `Agus Prasetyo`; Reported Date `2026-11-01T09:00:00Z`; Days Missing `10`; Last Updated `2026-11-04T16:10:00Z`.
  - DU-051-15: Record Missing dengan Source Reconciliation. Name `Tablet Samsung Galaxy Tab - 6`; Asset ID `TAB-2026-0106`; Group `Head Office`; Status `Missing`; Source `Reconciliation`; Last Holder `null`; Last Seen `Unknown`; Reported By `Rina Wulandari`; Reported Date `2026-11-01T08:00:00Z`; Days Missing `10`; Last Updated `2026-11-01T08:00:00Z`.
- Kondisi:
  - K1: daftar Active berisi DU-051-6 sampai DU-051-8 dan DU-051-12 sampai DU-051-15; sub-tab History berisi DU-051-9; pencarian `Canon` (DU-051-11) dijawab daftar berisi DU-051-7 saja; opsi filter `Status` berisi nilai Status DISTINCT dari baris itu, yaitu `Waiting for Confirmation`, `Missing`, `Reported Disposal`, dan `In Disposal Process`; opsi filter `Source` berisi nilai Source DISTINCT dari baris itu (DU-051-10); opsi filter `Brand` kosong; filter `Status` bernilai `Waiting for Confirmation` dijawab daftar berisi DU-051-6 saja; filter `Source` bernilai `Manual` dijawab daftar berisi DU-051-7 saja; kolom yang tampil adalah kolom bawaan tabel
  - K2: seperti K1, dengan preferensi kolom tersimpan menampilkan kolom bawaan ditambah `TAG`
  - K3: preferensi kolom tersimpan menampilkan hanya kolom `Name`; daftar Active berisi DU-051-6 sampai DU-051-8
  - K4: daftar Active berisi DU-051-1 (11 record) dengan ukuran halaman bawaan
  - K5: daftar Active berisi DU-051-2 (10 record) dengan ukuran halaman bawaan
  - K6: daftar Active berisi DU-051-3 (26 record) dengan ukuran halaman bawaan
  - K7: daftar Active berisi DU-051-1; pencarian `Aset Tersaring` (DU-051-11) dijawab daftar berisi DU-051-4 (12 record)
  - K8: daftar Active berisi DU-051-6 sampai DU-051-8; mengunduh berkas gagal karena error server

## Test Steps

### Siklus kotak Search
1. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
2. Klik tombol Search
3. Verifikasi kotak Search terbuka dengan fokus berada di input
4. Ketik `Canon` pada kotak Search tanpa menekan Enter
5. Verifikasi baris `Scanner Honeywell - 3` masih tampil selama Enter belum ditekan
6. Tekan Enter
7. Verifikasi baris `Printer Canon Pixma - 2` tampil sesudah Enter
8. Verifikasi baris `Scanner Honeywell - 3` tidak tampil sesudah Enter
9. Klik `✕` pada kotak Search
10. Verifikasi input kotak Search kosong
11. Verifikasi baris `Printer Canon Pixma - 2` masih tampil sesudah `✕`
12. Verifikasi baris `Scanner Honeywell - 3` masih tidak tampil sesudah `✕`
13. Tekan Enter pada kotak Search yang kosong
14. Verifikasi baris `Scanner Honeywell - 3` tampil kembali
15. Ketik Search `Canon`, tekan Enter
16. Verifikasi baris `Printer Canon Pixma - 2` tampil
17. Verifikasi baris `Scanner Honeywell - 3` tidak tampil
18. Klik `(←)` pada kotak Search
19. Verifikasi kotak Search tertutup
20. Verifikasi baris `Scanner Honeywell - 3` tampil kembali sesudah kotak Search ditutup

### Siklus tiga klik sort dan kolom tanpa ikon sort
21. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K2
22. Verifikasi header `TAG` memiliki ikon sort
23. Klik header `Reported Date`
24. Verifikasi indikator `↑` aktif pada header `Reported Date`
25. Klik header `Reported Date`
26. Verifikasi indikator `↓` aktif pada header `Reported Date`
27. Klik header `Reported Date`
28. Verifikasi indikator sort pada header `Reported Date` tidak aktif
29. Klik header `TAG`
30. Verifikasi indikator `↑` aktif pada header `TAG`
31. Klik header `Asset ID`
32. Verifikasi indikator `↑` pindah ke header `Asset ID`
33. Verifikasi indikator sort pada header `TAG` tidak aktif
34. Verifikasi header `Photo` tidak memiliki ikon sort

### Mekanik Filter Panel: draf, chip, dan indikator aktif
35. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
36. Klik tombol Filter
37. Klik field `Status`
38. Centang opsi `Missing`
39. Klik tombol Filter
40. Verifikasi baris `Laptop Asus Vivobook - 1` masih tampil karena `[Apply]` belum diklik
41. Klik tombol Filter
42. Verifikasi field `Status` tidak memuat chip karena draf dibuang
43. Klik field `Status`
44. Centang opsi `Waiting for Confirmation`
45. Centang opsi `Missing`
46. Verifikasi chip `Waiting for Confirmation` dan `Missing` tampil pada field `Status`
47. Klik `✕` pada chip `Missing`
48. Verifikasi chip `Waiting for Confirmation` tetap tampil
49. Verifikasi chip `Missing` hilang
50. Klik field `Status`
51. Verifikasi opsi `Missing` tidak tercentang
52. Centang opsi `Reported Disposal`
53. Hapus centang opsi `Reported Disposal`
54. Verifikasi chip `Waiting for Confirmation` tampil pada field `Status`
55. Verifikasi chip `Reported Disposal` tidak tampil
56. Klik tombol `[Apply]`
57. Verifikasi baris `Laptop Asus Vivobook - 1` tampil sesudah `[Apply]`
58. Verifikasi baris `Printer Canon Pixma - 2` tidak tampil sesudah `[Apply]`
59. Verifikasi indikator titik aktif tampil pada ikon Filter

### Filter Panel: chip overflow, pencarian opsi, dan sumber kosong
60. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
61. Klik tombol Filter
62. Klik field `Source`
63. Centang opsi `Borrow`
64. Centang opsi `Reported by holder`
65. Centang opsi `Stock opname`
66. Centang opsi `Transfer`
67. Centang opsi `Manual`
68. Centang opsi `Work order`
69. Centang opsi `Reconciliation`
70. Verifikasi chip ringkasan `+N more` tampil dan jumlah chip tampil ditambah N sama dengan `7`
71. Ketik `ZZZ-TIDAK-ADA` pada kotak cari di dalam opsi `Source`
72. Verifikasi `No results found` tampil
73. Klik field `Brand`
74. Verifikasi `No options available` tampil
75. Tekan Esc
76. Tekan Esc lagi
77. Verifikasi panel Filter tertutup

### Filter Long missing sebagai satu checkbox
78. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
79. Klik tombol Filter
80. Centang checkbox `Long missing`
81. Klik tombol `[Apply]`
82. Verifikasi checkbox `Long missing` tetap tercentang sesudah `[Apply]`
83. Verifikasi indikator titik aktif tampil pada ikon Filter

### Menyembunyikan kolom tidak membatalkan filter
84. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
85. Klik tombol Filter
86. Klik field `Status`
87. Centang opsi `Waiting for Confirmation`
88. Klik tombol `[Apply]`
89. Verifikasi indikator titik aktif tampil pada ikon Filter
90. Klik header kolom Actions (`⋯`)
91. Hapus centang kolom `Status` pada daftar kolom
92. Verifikasi kolom `Name` tetap tampil pada tabel
93. Verifikasi kolom `Status` tidak tampil pada tabel
94. Verifikasi indikator titik aktif tetap tampil pada ikon Filter
95. Verifikasi field `Status` masih ada pada panel Filter dengan chip `Waiting for Confirmation`

### Setup Column: anatomi modal
96. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
97. Klik header kolom Actions (`⋯`)
98. Klik `Setup Column...`
99. Verifikasi judul modal `Setup Column`
100. Verifikasi deskripsi `Drag and drop to rearrange the order and click the pin to freeze up to 3 columns.` tampil di bawah judul
101. Verifikasi ikon tutup `[✕]` tampil pada modal
102. Verifikasi daftar kolom dengan checkbox tampil pada modal
103. Verifikasi tombol `[Reset to Default]` dan `[Save]` tampil pada footer modal
104. Verifikasi tidak ada tombol `[Cancel]` pada footer modal

### Setup Column: sembunyikan dan tampilkan kolom
105. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
106. Klik header kolom Actions (`⋯`)
107. Klik `Setup Column...`
108. Hapus centang kolom `Source`
109. Klik `[Save]`
110. Verifikasi kolom `Name` tampil pada tabel
111. Verifikasi kolom `Source` tidak tampil pada tabel
112. Klik header kolom Actions (`⋯`)
113. Klik `Setup Column...`
114. Centang kolom `Source`
115. Klik `[Save]`
116. Verifikasi kolom `Source` tampil kembali pada tabel

### Setup Column: urutan kolom
117. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
118. Klik header kolom Actions (`⋯`)
119. Klik `Setup Column...`
120. Seret baris `Source` ke atas baris `Group` pada daftar kolom
121. Klik `[Save]`
122. Verifikasi kolom `Source` tampil sebelum kolom `Group` pada tabel

### Setup Column: pin dan batas pin
123. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
124. Klik header kolom Actions (`⋯`)
125. Klik `Setup Column...`
126. Klik ikon pin pada kolom `Name`
127. Klik ikon pin pada kolom `Asset ID`
128. Klik ikon pin pada kolom `Group`
129. Verifikasi ikon pin pada kolom `Status` disabled
130. Arahkan kursor ke ikon pin pada kolom `Status`
131. Verifikasi `Maximum 3 columns can be pinned at once. Unpin another column first.` tersampaikan pada ikon pin kolom `Status`
132. Klik ikon pin pada kolom `Group`
133. Verifikasi ikon pin pada kolom `Status` aktif kembali

### Setup Column: Reset to Default
134. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
135. Klik header kolom Actions (`⋯`)
136. Klik `Setup Column...`
137. Hapus centang kolom `Source`
138. Klik `[Reset to Default]`
139. Verifikasi kolom `Source` tercentang kembali pada daftar kolom
140. Klik `[Save]`
141. Verifikasi kolom `Source` tampil pada tabel

### Setup Column: tutup tanpa Save membuang perubahan
142. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
143. Klik header kolom Actions (`⋯`)
144. Klik `Setup Column...`
145. Hapus centang kolom `Reported By`
146. Klik `[✕]` pada modal
147. Verifikasi kolom `Reported By` tetap tampil pada tabel
148. Klik header kolom Actions (`⋯`)
149. Klik `Setup Column...`
150. Tekan Esc
151. Verifikasi fokus kembali ke tombol `⋯` pada header kolom Actions

### Setup Column: kolom terakhir tidak bisa disembunyikan
152. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K3
153. Klik header kolom Actions (`⋯`)
154. Klik `Setup Column...`
155. Verifikasi checkbox kolom `Name` disabled karena hanya satu kolom yang tampil
156. Arahkan kursor ke checkbox kolom `Name`
157. Verifikasi `At least one column must remain visible.` tersampaikan pada checkbox kolom `Name`
158. Centang kolom `Asset ID`
159. Verifikasi checkbox kolom `Name` enabled kembali

### Setup Column tanpa kolom finansial bagi aktor tanpa hak
160. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
161. Klik header kolom Actions (`⋯`)
162. Klik `Setup Column...`
163. Verifikasi kolom `Brand` tercantum pada daftar kolom
164. Verifikasi kolom `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)` tidak tercantum pada daftar kolom

### Konfigurasi kolom satu tabel tidak mengubah tabel lain
165. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
166. Klik header kolom Actions (`⋯`)
167. Hapus centang kolom `Source` pada daftar kolom
168. Verifikasi kolom `Name` tampil pada tab Active
169. Verifikasi kolom `Source` tidak tampil pada tab Active
170. Klik sub-tab `History`
171. Verifikasi kolom `Source` tampil pada tab History

### Filter dan sort terisolasi per tab
172. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K1
173. Klik tombol Filter
174. Klik field `Source`
175. Centang opsi `Manual`
176. Klik tombol `[Apply]`
177. Klik header `Name`
178. Verifikasi indikator `↑` aktif pada header `Name`
179. Klik sub-tab `History`
180. Verifikasi sub-tab `History` terpilih
181. Verifikasi indikator titik filter tidak tampil pada ikon Filter di tab History
182. Verifikasi indikator sort tidak aktif pada header kolom `Name` di tab History
183. Klik sub-tab `Active`
184. Verifikasi indikator titik filter tetap tampil pada ikon Filter di tab Active
185. Verifikasi indikator `↑` tetap aktif pada header `Name` di tab Active

### Paginasi: halaman terakhir, ganti sort, ganti ukuran halaman
186. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K4
187. Verifikasi ukuran halaman `10` terpilih secara bawaan pada daftar berisi lebih dari satu halaman
188. Klik halaman `2`
189. Verifikasi satu baris `Aset Paginasi 11` tampil pada halaman terakhir
190. Klik header `Name`
191. Verifikasi halaman `2` tetap aktif sesudah sort berganti
192. Pilih ukuran halaman `25`
193. Verifikasi halaman `1` aktif sesudah ukuran halaman berganti
194. Verifikasi ukuran halaman `25` terpilih

### Paginasi: nomor halaman tidak valid diabaikan
195. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K4
196. Pilih ukuran halaman `25`
197. Ketik `0` pada input nomor halaman, tekan Enter
198. Verifikasi halaman `1` tetap aktif sesudah input `0`
199. Ketik `-1` pada input nomor halaman, tekan Enter
200. Verifikasi halaman `1` tetap aktif sesudah input `-1`
201. Ketik `2` pada input nomor halaman, tekan Enter
202. Verifikasi halaman `1` tetap aktif sesudah input `2` yang melewati halaman terakhir
203. Ketik `abc` pada input nomor halaman, tekan Enter
204. Verifikasi halaman `1` tetap aktif sesudah input `abc`

### Paginasi: daftar tepat satu halaman
205. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K5
206. Verifikasi baris `Aset Tepat Sepuluh 10` tampil pada halaman `1`
207. Verifikasi tombol halaman `2` tidak tampil

### Paginasi: ukuran halaman 25 dengan satu baris di halaman terakhir
208. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K6
209. Pilih ukuran halaman `25`
210. Klik halaman `2`
211. Verifikasi satu baris `Aset Dua Puluh Enam 26` tampil pada halaman terakhir

### Paginasi: hasil pencarian lebih dari satu halaman
212. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K7
213. Ketik Search `Aset Tersaring`, tekan Enter
214. Verifikasi tombol halaman `2` tampil untuk hasil pencarian
215. Klik halaman `2`
216. Verifikasi baris `Aset Tersaring 12` tampil pada halaman `2`

### Unduhan gagal menampilkan toast error
217. Tampilkan Halaman Missing sub-tab Active (tabel T-MIS-01) dengan kondisi K8
218. Klik tombol Download
219. Klik `Download as CSV`
220. Verifikasi toast `Error, failed to download Missing-Active.` tampil

---
id: TC-FA-BORROW-UI-054-tabel-transactions-mekanik-dan-konfigurasi
title: "Tabel Transactions: state kosong dan gagal muat, format sel, mekanik Search, Filter, Sort, Setup Column, dan paginasi"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1#p2", "§4.1#p4", "§4.1#p5", "§4.1#p6", "§4.1a#r1", "§4.1a#r2", "§4.1a#r3", "§4.1a#r4", "§4.1a#r5", "§4.1a#r6", "§4.1a#r7", "§4.1a#r8", "§4.1a#r9", "§4.1a#p6", "§4.1a#p7", "§4.1a#p8", "§4.1a#p9", "§4.2.1#p2", "§4.3#r5", "§5#r10", "§5#r11", "§12#r2", "EB-TBL-1@tabel-transactions", "EB-TBL-2@tabel-transactions", "EB-TBL-4@tabel-transactions", "EB-TBL-5@aksi-baris-transactions", "EB-TBL-7@tabel-transactions", "EB-TBL-8@tabel-transactions", "EB-SRC-4@tabel-transactions", "EB-FLT-2@tabel-transactions", "EB-FLT-6@tabel-transactions", "EB-SRT-3@tabel-transactions", "EB-KOL-1@tabel-transactions", "EB-DL-5", "EB-XM-1"]
smoke: []
dependsOn: []
trace:
  "§4.1#p2": [51, 56, 71, 72, 139, 140, 141]
  "§4.1#p4": [38, 39, 40]
  "§4.1#p5": [24, 25, 26]
  "§4.1#p6": 27
  "§4.1a#r1": [17, 18, 19, 139]
  "§4.1a#r2": [17, 20, 21, 23, 59, 69, 139]
  "§4.1a#r3": [29, 31, 32, 33, 60, 61, 139]
  "§4.1a#r4": [34, 36, 41, 62, 139]
  "§4.1a#r5": [43, 45, 46, 63, 139]
  "§4.1a#r6": [64, 140, 142, 145, 146, 147, 149, 151]
  "§4.1a#r7": [47, 49, 50, 65, 139]
  "§4.1a#r8": [51, 53, 66, 139]
  "§4.1a#r9": [17, 52, 67, 139]
  "§4.1a#p6": [210, 213, 220]
  "§4.1a#p7": [211, 213, 216]
  "§4.1a#p8": 217
  "§4.1a#p9": 212
  "§4.2.1#p2": 110
  "§4.3#r5": [24, 25, 26]
  "§5#r10": 17
  "§5#r11": 52
  "§12#r2": 212
  "EB-TBL-1@tabel-transactions": [2, 3, 10, 11, 13, 14, 15]
  "EB-TBL-2@tabel-transactions": [41, 50]
  "EB-TBL-4@tabel-transactions": [34, 36]
  "EB-TBL-5@aksi-baris-transactions": 224
  "EB-TBL-7@tabel-transactions": [186, 189, 191, 193, 195, 198, 201]
  "EB-TBL-8@tabel-transactions": 54
  "EB-SRC-4@tabel-transactions": [109, 112, 115, 117, 119, 122]
  "EB-FLT-2@tabel-transactions": [6, 71, 74, 80, 82, 83, 86, 87, 93, 96]
  "EB-FLT-6@tabel-transactions": [104, 105]
  "EB-SRT-3@tabel-transactions": [125, 127, 129, 132, 133, 134]
  "EB-KOL-1@tabel-transactions": [137, 144, 153, 157, 158, 159, 164, 166, 168, 170, 173, 178, 183, 184]
  "EB-DL-5": [205, 206, 207]
  "EB-XM-1": [51, 56]
anchor: [85, 92, 107, 114]
coverage:
  web: automated
---
# Tabel Transactions: state kosong dan gagal muat, format sel, mekanik Search, Filter, Sort, Setup Column, dan paginasi

## Prerequisites
- Aktor: Total Control.
- Layar awal: halaman `Transactions > Borrow`, tab Transactions.
- Komponen: Tabel Transactions
- Data:
  - DU-054-1: BRW `BRW-2026-0149`, Status `Borrowed` dengan penanda `Overdue`, Group `Head Office` (hierarki `Head Office`), Borrower `Andi Pratama` (tampil `Andi P`), Total Asset `2` (aset `Projector Epson EB-X06 - 14` berstatus `Overdue`, aset `Laptop Dell Latitude 5420 - 10` berstatus `Borrowed`), Source `Admin`, Requested By `Rina Wijaya` (tampil `Rina W`), Request Date `31/10/26, 09:00`, Last Updated `06/11/26, 17:00`.
  - DU-054-2: BRW `BRW-2026-0161`, Status `Extension Request`, Group `Head Office`, Borrower `Rudi Hartono` (tampil `Rudi H`), Total Asset `4`, Source `Admin`, Requested By `Rina Wijaya`, Request Date `07/11/26, 14:00`, Last Updated `09/11/26, 08:12`.
  - DU-054-3: BRW `BRW-2026-0154`, Status `Waiting for Approval`, Group `Head Office`, Borrower `Rudi Hartono`, Total Asset `1`, Source `Admin`, Requested By `Agus Prasetyo` (tampil `Agus P`), Request Date `09/11/26, 09:20`, Last Updated `09/11/26, 10:15`.
  - DU-054-4: BRW `BRW-2026-0165`, Status `Extension Approval`, Group `Branch Surabaya` (hierarki `Head Office > Branch Surabaya`), Borrower `Maya Putri` (tampil `Maya P`), Total Asset `4`, Source `Admin`, Requested By `Rina Wijaya`, Request Date `06/11/26, 10:00`, Last Updated `09/11/26, 07:50`.
  - DU-054-5: BRW `BRW-2026-0156`, Status `Borrowed`, Group `Head Office`, Borrower `Budi Setiawan` (tampil `Budi S`), Total Asset `1`, Source `Self-service`, Requested By kosong, Request Date `09/11/26, 08:50`, Last Updated `09/11/26, 18:50`.
  - DU-054-6: BRW `BRW-2026-0152`, Status `Waiting for Handover`, Group `Head Office`, Borrower `Budi Setiawan`, Total Asset `6`, Source `Admin`, Requested By `Agus Prasetyo`, Request Date `08/11/26, 16:30`, Last Updated `09/11/26, 20:29`.
  - DU-054-7: BRW `BRW-2026-0170`, Status `Waiting for Handover`, Group `Jakarta Selatan Distribution Center` (hierarki `Region Jawa > Jakarta Selatan Distribution Center`), Borrower `Wawan Setiadi` (tampil `Wawan S`) tanpa akun login dengan PIC `Rina Wijaya`, Total Asset `1`, Source `Self-service`, Requested By `Rina Wijaya`, Request Date `08/11/26, 10:00`, Last Updated `08/11/26, 11:00`.
  - DU-054-8: BRW `BRW-2026-0171`, Status `Waiting for Approval`, Group `Head Office`, Borrower `Tono Saputra` (tampil `Tono S`) tanpa akun login dan tanpa PIC, Total Asset `1`, Source `Admin`, Requested By `Agus Prasetyo`, Request Date `09/11/26, 07:00`, Last Updated `09/11/26, 07:30`.
  - DU-054-9: 26 BRW berstatus `Borrowed` dengan Transaction ID `BRW-2026-{n}`, Group `Head Office`, Borrower `Budi Setiawan`, Requested By `Agus Prasetyo`.
  - DU-054-10: BRW `BRW-2026-0172`, Status `Borrowed`, Group `<i>Gudang</i> Pusat`, Borrower `Budi Setiawan`, Total Asset `1`, Source `Admin`, Requested By `Agus Prasetyo`, Request Date `09/11/26, 08:10`, Last Updated `09/11/26, 09:10`.
  - DU-054-11: kata kunci Search `Andi`, kata kunci tanpa hasil `Tidak Ada`, nomor halaman `99`, `0`, `-1`, dan `abc`, serta Rows per page `25`.
  - DU-054-12: 5.001 BRW berstatus `Borrowed` dengan Transaction ID `BRW-2026-{n}`, Group `Head Office`, Borrower `Budi Setiawan`.
  - DU-054-13: BRW `BRW-2026-0173`, Status `Borrowed`, Group `Head Office`, Borrower `Budi Setiawan`, Total Asset `1`, seluruh aset Borrowed sudah memiliki Damage Report.
- Kondisi:
  - K1: tabel dimuat berisi DU-054-1 sampai DU-054-8 dan DU-054-10; Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`.
  - K2: tabel dimuat tanpa data sama sekali.
  - K3: memuat tabel gagal karena error server.
  - K4: tabel dimuat berisi 26 baris DU-054-9; ukuran halaman bawaan 10 baris.
  - K5: seperti K1; pencarian `Andi` dijawab hanya dengan DU-054-1, pencarian kosong dijawab dengan semua baris K1.
  - K6: tabel dimuat berisi DU-054-1 dan DU-054-3; saringan Status `Borrowed` yang di-Apply dijawab hanya dengan DU-054-1.
  - K7: seperti K1; pencarian `Tidak Ada` dijawab tanpa baris.
  - K8: seperti K1; Date Format bernilai `M/d/yy` dan Time Format bernilai `24h`. Request Date DU-054-1 yang diharapkan `10/31/26, 09:00`, dari Request Date `31/10/26, 09:00` dengan Date Format `M/d/yy`.
  - K9: tabel dimuat dengan total DU-054-12 (5.001 baris); berkas Download siap beberapa saat sesudah format dipilih.
  - K10: tabel dimuat berisi DU-054-13.

## Test Steps

### Kosong alami dan sumber opsi filter kosong dibedakan
1. Tampilkan Tabel Transactions dengan kondisi K2
2. Verifikasi judul `No borrows yet` tampil pada tabel
3. Verifikasi deskripsi `Borrowed assets will appear here.` tampil pada tabel
4. Klik ikon Filter pada toolbar
5. Klik field `Status` pada Filter Panel
6. Verifikasi teks `No options available` tampil pada daftar opsi field `Status`

### Kosong akibat pencarian tanpa hasil
7. Tampilkan Tabel Transactions dengan kondisi K7
8. Klik ikon Search pada toolbar
9. Ketik Search `Tidak Ada`, tekan Enter
10. Verifikasi judul `No results found` tampil pada tabel
11. Verifikasi deskripsi `Try adjusting your search or filter.` tampil pada tabel

### Gagal muat bukan empty state
12. Tampilkan Tabel Transactions dengan kondisi K3
13. Verifikasi pesan `Unable to load this data.` tampil pada tabel
14. Verifikasi tombol `[Try Again]` tampil pada tabel
15. Verifikasi judul `No borrows yet` tidak tampil karena gagal muat bukan empty state

### Urutan kolom, Transaction ID, dan badge status
16. Tampilkan Tabel Transactions dengan kondisi K1
17. Verifikasi urutan kolom data dari kiri ke kanan: `Transaction ID`, `Status`, `Group`, `Borrower`, `Total Asset`, `Requested By`, `Request Date`, `Last Updated`
18. Verifikasi Transaction ID `BRW-2026-0149` tampil sebagai tautan pada baris itu
19. Verifikasi setiap baris tabel memuat Transaction ID
20. Verifikasi baris `BRW-2026-0149` memuat badge status `Borrowed` dan badge `Overdue`
21. Verifikasi baris `BRW-2026-0161` memuat badge status `Extension Request` dan tidak memuat badge `Overdue`
22. Arahkan kursor ke badge status baris `BRW-2026-0149`
23. Verifikasi rincian baris `Borrowed` dan `Overdue` tampil
24. Verifikasi badge `Borrowed` memakai severity `primary`
25. Verifikasi badge `Overdue` memakai severity `danger`
26. Verifikasi badge `Waiting for Approval`, `Waiting for Handover`, `Extension Request`, dan `Extension Approval` memakai severity `warning`
27. Verifikasi tidak ada baris berstatus `Canceled` pada tabel karena BRW yang dibatalkan ada di tab History

### Group dan Borrower
28. Tampilkan Tabel Transactions dengan kondisi K1
29. Verifikasi badge Group baris `BRW-2026-0170` tampil `Jakarta Sela..ution Center`
30. Arahkan kursor ke badge Group baris `BRW-2026-0170`
31. Verifikasi hierarki `Region Jawa > Jakarta Selatan Distribution Center` tampil
32. Verifikasi badge Group `Head Office` baris `BRW-2026-0149` memakai severity `primary`
33. Verifikasi setiap baris tabel memuat badge Group
34. Verifikasi Borrower baris `BRW-2026-0149` tampil `Andi P`
35. Arahkan kursor ke Borrower baris `BRW-2026-0149`
36. Verifikasi nama lengkap `Andi Pratama` tampil
37. Arahkan kursor ke ikon link pada Borrower baris `BRW-2026-0170`
38. Verifikasi tooltip `On behalf of: Rina Wijaya (PIC)` tampil
39. Verifikasi Borrower baris `BRW-2026-0171` memuat badge `No PIC`
40. Verifikasi badge `No PIC` memakai severity `danger`
41. Verifikasi setiap baris tabel memuat Borrower

### Total Asset, Requested By, dan teks sel
42. Tampilkan Tabel Transactions dengan kondisi K1
43. Verifikasi Total Asset baris `BRW-2026-0149` bernilai `2`
44. Arahkan kursor ke Total Asset baris `BRW-2026-0149`
45. Verifikasi aset `Projector Epson EB-X06 - 14` berstatus `Overdue` dan aset `Laptop Dell Latitude 5420 - 10` berstatus `Borrowed` tampil
46. Verifikasi setiap baris tabel memuat Total Asset
47. Verifikasi Requested By baris `BRW-2026-0149` tampil `Rina W`
48. Arahkan kursor ke Requested By baris `BRW-2026-0149`
49. Verifikasi nama lengkap `Rina Wijaya` tampil
50. Verifikasi Requested By baris `BRW-2026-0156` tampil `—`
51. Verifikasi Request Date baris `BRW-2026-0149` tampil `31/10/26, 09:00`
52. Verifikasi Last Updated baris `BRW-2026-0149` tampil `06/11/26, 17:00`
53. Verifikasi setiap baris tabel memuat Request Date dan Last Updated
54. Verifikasi Group baris `BRW-2026-0172` tampil `<i>Gudang</i> Pusat` apa adanya sebagai teks

### Format tanggal mengikuti Date Format General Settings
55. Tampilkan Tabel Transactions dengan kondisi K8
56. Verifikasi Request Date baris `BRW-2026-0149` tampil `10/31/26, 09:00`

### Field dan placeholder Filter Panel
57. Tampilkan Tabel Transactions dengan kondisi K6
58. Klik ikon Filter pada toolbar
59. Verifikasi placeholder `All statuses` tampil pada field `Status`
60. Verifikasi placeholder `All groups` tampil pada field `Group`
61. Verifikasi field `Group` berupa pemilih tree multi-pilih
62. Verifikasi placeholder `All borrowers` tampil pada field `Borrower`
63. Verifikasi input pertama field `Total Asset` memakai placeholder `Min` dan input kedua memakai placeholder `Max`
64. Verifikasi placeholder `All sources` tampil pada field `Source`
65. Verifikasi placeholder `All users` tampil pada field `Requested By`
66. Verifikasi placeholder `Select date` tampil pada field `Request Date`
67. Verifikasi placeholder `Select date` tampil pada field `Last Updated`
68. Klik field `Overdue`
69. Verifikasi opsi `Overdue` dan `Not overdue` tampil pada field `Overdue`
70. Klik field `Status`
71. Verifikasi opsi `Borrowed` dan `Waiting for Approval` tampil pada field `Status`
72. Verifikasi opsi `Extension Request` tidak tampil karena tidak ada baris berstatus itu pada tabel
73. Ketik pada kotak cari di dalam daftar opsi field `Status` kata kunci `Tidak Ada`
74. Verifikasi teks `No results found` tampil pada daftar opsi field `Status`

### Draf Filter Panel, chip, Apply, dan indikator aktif
75. Tampilkan Tabel Transactions dengan kondisi K6
76. Klik ikon Filter pada toolbar
77. Klik field `Status`
78. Centang opsi `Borrowed`
79. Centang opsi `Waiting for Approval`
80. Verifikasi chip `Borrowed` dan `Waiting for Approval` tampil pada field `Status`
81. Klik `(✕)` pada chip `Waiting for Approval`
82. Verifikasi opsi `Waiting for Approval` tidak tercentang pada daftar opsi field `Status`
83. Verifikasi baris `BRW-2026-0154` masih tampil karena saringan belum di-Apply
84. Klik `[Apply]`
85. Verifikasi baris `BRW-2026-0149` tampil pada tabel
86. Verifikasi baris `BRW-2026-0154` tidak tampil pada tabel
87. Verifikasi ikon Filter menampilkan badge titik indikator filter aktif
88. Klik field `Status`
89. Centang opsi `Waiting for Approval`
90. Klik ikon Filter pada toolbar
91. Klik ikon Filter pada toolbar
92. Verifikasi chip `Borrowed` tampil pada field `Status`
93. Verifikasi chip `Waiting for Approval` tidak tampil karena draf dibuang saat panel ditutup tanpa `[Apply]`
94. Klik field `Status`
95. Klik opsi `Borrowed` untuk membatalkan centangnya
96. Verifikasi chip `Borrowed` tidak tampil pada field `Status`

### Filter tetap ada saat kolom disembunyikan
97. Tampilkan Tabel Transactions dengan kondisi K6
98. Klik ikon Filter pada toolbar
99. Klik field `Status`
100. Centang opsi `Borrowed`
101. Klik `[Apply]`
102. Klik header kolom Actions `⋯`
103. Hilangkan centang kolom `Status` pada daftar Column Visibility
104. Verifikasi field `Status` masih tampil pada Filter Panel
105. Verifikasi baris `BRW-2026-0154` tetap tidak tampil pada tabel

### Siklus kotak Search
106. Tampilkan Tabel Transactions dengan kondisi K5
107. Verifikasi ikon Search tampil pada toolbar
108. Klik ikon Search pada toolbar
109. Verifikasi kotak Search terbuka dan fokus berada di input
110. Verifikasi placeholder `Search transaction ID, asset, or borrower...` tampil pada kotak Search
111. Ketik `Andi` pada kotak Search tanpa menekan Enter
112. Verifikasi baris `BRW-2026-0161` masih tampil karena pencarian belum dijalankan
113. Tekan Enter
114. Verifikasi baris `BRW-2026-0149` tampil pada tabel
115. Verifikasi baris `BRW-2026-0161` tidak tampil pada tabel
116. Klik `✕` pada kotak Search
117. Verifikasi baris `BRW-2026-0161` tetap tidak tampil karena `✕` tidak menjalankan pencarian
118. Tekan Enter dengan kotak Search kosong
119. Verifikasi baris `BRW-2026-0161` tampil kembali
120. Ketik Search `Andi`, tekan Enter
121. Klik `(←)` pada kotak Search
122. Verifikasi baris `BRW-2026-0161` tampil kembali dan kotak Search tertutup

### Siklus tiga klik Sort
123. Tampilkan Tabel Transactions dengan kondisi K1
124. Klik header kolom `Transaction ID`
125. Verifikasi indikator sort `↑` aktif pada header `Transaction ID`
126. Klik header kolom `Transaction ID`
127. Verifikasi indikator sort `↓` aktif pada header `Transaction ID`
128. Klik header kolom `Transaction ID`
129. Verifikasi indikator sort tidak aktif pada header `Transaction ID`
130. Klik header kolom `Borrower`
131. Klik header kolom `Total Asset`
132. Verifikasi indikator sort `↑` aktif pada header `Total Asset`
133. Verifikasi indikator sort tidak aktif pada header `Borrower`
134. Verifikasi header kolom Actions `⋯` tidak memiliki ikon sort

### Column Visibility pada panel cepat
135. Tampilkan Tabel Transactions dengan kondisi K1
136. Arahkan kursor ke header kolom Actions `⋯`
137. Verifikasi tooltip `Column Visibility` tampil
138. Klik header kolom Actions `⋯`
139. Verifikasi checkbox `Transaction ID`, `Status`, `Group`, `Borrower`, `Total Asset`, `Requested By`, `Request Date`, dan `Last Updated` tercentang dan enabled
140. Verifikasi checkbox `Source` tidak tercentang dan enabled
141. Verifikasi daftar kolom tidak memuat baris `Actions` maupun kolom Checkbox
142. Verifikasi kolom `Source` tidak tampil pada tabel
143. Centang kolom `Source` pada daftar Column Visibility
144. Verifikasi kolom `Source` tampil pada tabel
145. Verifikasi badge `Admin` baris `BRW-2026-0149` memakai severity `dark`
146. Verifikasi badge `Self-service` baris `BRW-2026-0156` memakai severity `primary`
147. Verifikasi setiap baris tabel memuat badge Source
148. Arahkan kursor ke badge `Admin` baris `BRW-2026-0149`
149. Verifikasi nama pembuat `Rina Wijaya` tampil
150. Arahkan kursor ke badge `Self-service` baris `BRW-2026-0156`
151. Verifikasi keterangan bahwa BRW dipinjam sendiri oleh Borrower tampil
152. Hilangkan centang kolom `Requested By` pada daftar Column Visibility
153. Verifikasi kolom `Requested By` langsung tidak tampil pada tabel

### Modal Setup Column: pin, urutan, Save, Reset, dan batal
154. Tampilkan Tabel Transactions dengan kondisi K1
155. Klik header kolom Actions `⋯`
156. Klik `Setup Column...`
157. Verifikasi judul `Setup Column` tampil pada modal
158. Verifikasi deskripsi `Drag and drop to rearrange the order and click the pin to freeze up to 3 columns.` tampil pada modal
159. Verifikasi tombol `[Reset to Default]` dan `[Save]` tampil pada footer modal
160. Klik ikon pin kolom `Transaction ID`
161. Klik ikon pin kolom `Status`
162. Klik ikon pin kolom `Group`
163. Arahkan kursor ke ikon pin kolom `Borrower`
164. Verifikasi ikon pin kolom `Borrower` disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
165. Klik ikon pin kolom `Group`
166. Verifikasi ikon pin kolom `Borrower` aktif kembali
167. Seret baris `Last Updated` ke atas baris `Borrower` pada daftar kolom
168. Verifikasi tabel di balik modal menampilkan kolom `Last Updated` sebelum kolom `Borrower`
169. Klik `[Reset to Default]`
170. Verifikasi daftar kolom kembali ke urutan bawaan dan kolom `Source` tidak tercentang
171. Hilangkan centang kolom `Group`
172. Klik `[✕]` pada modal
173. Verifikasi kolom `Group` masih tampil pada tabel karena perubahan dibuang
174. Klik header kolom Actions `⋯`
175. Klik `Setup Column...`
176. Hilangkan centang kolom `Group`
177. Klik `[Save]`
178. Verifikasi kolom `Group` tidak tampil pada tabel dan modal tertutup

### Kolom visible terakhir tidak bisa disembunyikan
179. Tampilkan Tabel Transactions dengan kondisi K1
180. Klik header kolom Actions `⋯`
181. Hilangkan centang kolom `Transaction ID`, `Status`, `Group`, `Borrower`, `Total Asset`, `Requested By`, dan `Request Date`
182. Arahkan kursor ke checkbox kolom `Last Updated`
183. Verifikasi checkbox kolom `Last Updated` disabled
184. Verifikasi tooltip `At least one column must remain visible.` tampil

### Paginasi: halaman tidak valid, page size, dan sort
185. Tampilkan Tabel Transactions dengan kondisi K4
186. Verifikasi halaman 1 aktif pada paginasi
187. Klik halaman 2 pada paginasi
188. Klik header kolom `Transaction ID`
189. Verifikasi halaman 2 tetap aktif sesudah sort berganti
190. Isi nomor halaman dengan `abc`, tekan Enter
191. Verifikasi halaman 2 tetap aktif karena input non-angka diabaikan
192. Isi nomor halaman dengan `99`, tekan Enter
193. Verifikasi halaman terakhir aktif
194. Isi nomor halaman dengan `-1`, tekan Enter
195. Verifikasi halaman 1 aktif
196. Klik halaman 2 pada paginasi
197. Pilih Rows per page `25`
198. Verifikasi halaman 1 aktif sesudah page size berganti
199. Klik halaman 2 pada paginasi
200. Isi nomor halaman dengan `0`, tekan Enter
201. Verifikasi halaman 1 aktif karena nomor di bawah 1 menuju halaman 1

### Download di atas 5.000 baris memakai loading screen
202. Tampilkan Tabel Transactions dengan kondisi K9
203. Klik ikon Download pada toolbar
204. Klik `Download as CSV`
205. Verifikasi loading screen tampil sampai berkas siap
206. Verifikasi berkas langsung terunduh begitu siap
207. Verifikasi tidak ada toast atau notifikasi tentang persiapan berkas

### Severity, icon, dan urutan row action
208. Tampilkan Tabel Transactions dengan kondisi K1
209. Klik `⋯` pada baris `BRW-2026-0152`
210. Verifikasi urutan aksi pada menu: `Detail`, `Hand Over`, `Remind Borrower`, `Cancel Borrow`
211. Verifikasi aksi `Detail` memakai icon `FileInfoLine`
212. Verifikasi aksi `Hand Over` dan `Remind Borrower` memakai severity `dark`
213. Verifikasi aksi `Cancel Borrow` memakai icon `CloseLine` dan severity `danger`
214. Tekan Esc
215. Klik `⋯` pada baris `BRW-2026-0149`
216. Verifikasi aksi `Request Extension` memakai icon `ExtensionBorrow` dan severity `dark`
217. Verifikasi menu aksi baris `BRW-2026-0149` tidak memuat `Report Damaged`, `Report Missing`, maupun `I Can't Scan the TAG`
218. Tekan Esc
219. Klik `⋯` pada baris `BRW-2026-0165`
220. Verifikasi aksi `Cancel Extension` memakai icon `CloseLine` dan severity `danger`

### Alasan tersampaikan pada aksi baris yang disabled
221. Tampilkan Tabel Transactions dengan kondisi K10
222. Klik `⋯` pada baris `BRW-2026-0173`
223. Arahkan kursor ke aksi `Request Extension`
224. Verifikasi alasan tersampaikan pada aksi `Request Extension` yang disabled

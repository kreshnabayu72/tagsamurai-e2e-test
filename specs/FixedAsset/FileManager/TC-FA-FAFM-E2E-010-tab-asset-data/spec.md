---
id: TC-FA-FAFM-E2E-010-tab-asset-data
title: "Tab Disposed & Unmanaged Assets: isi, konfigurasi, dan read-only"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["F-FAFM-07a", "F-FAFM-07b", "F-FAFM-07d", "FAFM-LOGIC-05i", "FAFM-LOGIC-08a", "FAFM-LOGIC-08b", "FAFM-LOGIC-08d", "FAFM-LOGIC-08f", "INV-11f", "T-FAFM-02", "TBL-01f", "TBL-03a", "TBL-04b", "TBL-05b", "§4.1#p11", "§9.2#p20", "EB-SRC-5@tabel-asset-data", "EB-FLT-5@tabel-asset-data"]
smoke: []
dependsOn: []
trace:
  "F-FAFM-07a": 2
  "F-FAFM-07b": [5, 7, 9, 248, 258, 273]
  "F-FAFM-07d": [18, 19]
  "FAFM-LOGIC-05i": 19
  "FAFM-LOGIC-08a": [4, 5, 6, 26]
  "FAFM-LOGIC-08b": [7, 8, 9, 248, 258]
  "FAFM-LOGIC-08d": [18, 19, 20]
  "FAFM-LOGIC-08f": [4, 11, 13, 27]
  "INV-11f": 18
  "T-FAFM-02": [4, 5, 6, 7, 8, 22, 23, 24, 26, 31, 32, 37, 38, 42, 47, 54, 55, 58, 59, 62, 63, 66, 71, 72, 75, 79, 80, 82, 83, 101, 102, 109, 110, 117, 118, 125, 126, 137, 139, 140, 142, 143, 145, 146, 148, 149, 151, 152, 154, 155, 157, 158, 165, 167, 169, 172, 174, 177, 179, 182, 184, 187, 189, 192, 194, 197, 199, 202, 204, 207, 209, 221, 223, 226, 229, 232, 234, 236, 238, 259, 260, 262, 265]
  "TBL-01f": [16, 17]
  "TBL-03a": [22, 23]
  "TBL-04b": [223, 236]
  "TBL-05b": 20
  "§4.1#p11": 15
  "§9.2#p20": 19
  "EB-SRC-5@tabel-asset-data": [89, 94]
  "EB-FLT-5@tabel-asset-data": [43, 48, 51]
anchor: [5, 16, 22, 26, 31, 37, 42, 47, 54, 58, 62, 71, 79, 82, 87, 101, 109, 117, 125, 139, 142, 145, 148, 151, 154, 157, 165, 272]
coverage:
  web: automated
---

# Tab Disposed & Unmanaged Assets: isi, konfigurasi, dan read-only

## Prerequisites
- Aktor: Total Control, user `Rahmat Hidayat {runId}` (tampil `Rahmat H`), akun aktif dengan kredensial disediakan fase 2. Aktor kedua: Group Manager `Bima Pengelola {runId}` (tampil `Bima P`) untuk Group `Cabang Surabaya {runId}`.
- Layar awal: halaman Settings > File Manager.
- Data:
  - Group `Kantor Pusat {runId}` (DU-010-1) dan `Cabang Surabaya {runId}` (DU-010-2) ada di entitas aktor.
  - DU-010-3: Aset Name `Excavator Komatsu PC200 {runId}`, Group `Kantor Pusat {runId}`, Status `Disposed`, Division `Logistik {runId}`, Alias Name `Ekskavator Proyek Timur {runId}`, Brand `Komatsu Indonesia {runId}`, Model/Type `PC200-8M0 {runId}`, Category `Alat Berat {runId}`, Register Date `T0 − 30 hari`, Files Size `6.0 MB`, dari DU-010-12 `4.0 MB` dan DU-010-13 `2.0 MB`.
  - DU-010-4: Aset Name `Forklift Heli CPCD30 {runId}`, Group `Kantor Pusat {runId}`, Status `Disposed`, Division `Logistik {runId}`, Register Date `T0 − 20 hari`, Files Size `900.0 KB`, dari DU-010-14 `900.0 KB`.
  - DU-010-5: Aset Name `Mixer Beton Schwing {runId}`, Group `Kantor Pusat {runId}`, Status `Disposed`, Division `Logistik {runId}`, Alias Name `Mixer Proyek Barat {runId}`, Brand `Schwing Stetter {runId}`, Model/Type `SP500-M {runId}`, Category `Alat Berat {runId}`, Register Date `T0 − 10 hari`, Files Size `10.0 MB`, dari DU-010-15 `10.0 MB`.
  - DU-010-6: Aset Name `Printer Epson L3250 {runId}`, Group `Cabang Surabaya {runId}`, Status `Unmanaged`, Division `Keuangan {runId}`, Alias Name `Printer Lantai Dua {runId}`, Brand `Epson Indonesia {runId}`, Model/Type `EcoTank Seri 3 {runId}`, Category `Perangkat Kantor {runId}`, Register Date `T0 − 4 hari`, Files Size `1.2 MB`, dari DU-010-16 `1.2 MB`.
  - DU-010-7: Aset Name `Scanner Canon DR-C225 {runId}`, Group `Cabang Surabaya {runId}`, Status `Unmanaged`, Division `Logistik {runId}`, Register Date `T0 − 3 hari`, Files Size `2.0 MB`, dari DU-010-17 `2.0 MB`.
  - DU-010-8: Aset Name `Router Mikrotik RB4011 {runId}`, Group `Cabang Surabaya {runId}`, Status `Unmanaged`, tanpa Division, Register Date `T0 − 2 hari`, tanpa file, Files Size `0.0 KB`.
  - DU-010-9: delapan aset Name `Aset Massal {n} {runId}` untuk n dari 1 sampai 8, Group `Cabang Surabaya {runId}`, Status `Unmanaged`, tanpa Division, Register Date `T0 − 2 hari`, tanpa file, Files Size `0.0 KB`.
  - DU-010-10: Aset Name `Truk Hino 500 {runId}`, Group `Kantor Pusat {runId}`, Status `Active`.
  - DU-010-11: Aset Name `Kompresor Atlas Copco {runId}`, Group `Kantor Pusat {runId}`, Status `Draft`.
  - DU-010-12: File File Name `serah-terima-ekskavator-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Excavator Komatsu PC200 {runId}`, Group `Kantor Pusat {runId}`, Size `4.0 MB`, Uploaded By `Rahmat H`, ada di tab `Asset Documents`.
  - DU-010-13: File File Name `foto-lelang-ekskavator-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Excavator Komatsu PC200 {runId}`, Group `Kantor Pusat {runId}`, Size `2.0 MB`, Uploaded By `Rahmat H`, ada di tab `Asset Documents`.
  - DU-010-14: File File Name `manual-forklift-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Forklift Heli CPCD30 {runId}`, Group `Kantor Pusat {runId}`, Size `900.0 KB`, Uploaded By `Rahmat H`.
  - DU-010-15: File File Name `kontrak-mixer-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Mixer Beton Schwing {runId}`, Group `Kantor Pusat {runId}`, Size `10.0 MB`, Uploaded By `Rahmat H`.
  - DU-010-16: File File Name `invoice-printer-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Printer Epson L3250 {runId}`, Group `Cabang Surabaya {runId}`, Size `1.2 MB`, Uploaded By `Rahmat H`.
  - DU-010-17: File File Name `panduan-scanner-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Scanner Canon DR-C225 {runId}`, Group `Cabang Surabaya {runId}`, Size `2.0 MB`, Uploaded By `Rahmat H`.
  - DU-010-27: User `Bima Pengelola {runId}`, role `Group Manager`, group yang dikelola `Cabang Surabaya {runId}`.
  - Himpunan aset Disposed dan Unmanaged ber-runId di tab `Disposed & Unmanaged Assets` seluruhnya berjumlah 14: DU-010-3 sampai DU-010-8 dan delapan aset DU-010-9. Aset DU-010-10 dan DU-010-11 tidak termasuk.
  - Urutan Total Size dari terbesar: DU-010-5, DU-010-3, DU-010-7, DU-010-6, DU-010-4, lalu aset tanpa file (DU-010-8 dan DU-010-9). Selisih Files Size antar-aset DU-010-3 sampai DU-010-7 jauh lebih besar daripada Data & Log Size.
- Kondisi:
  - Akun `Bima Pengelola {runId}` aktif dan kredensialnya disediakan fase 2.
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `HH:mm`.

## Test Steps

### Isi tab Disposed & Unmanaged Assets berasal dari aset Disposed dan Unmanaged
1. Klik tab `Disposed & Unmanaged Assets`
2. Verifikasi tab `Disposed & Unmanaged Assets` aktif
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi Pagination menampilkan total `14` baris dalam `2` halaman
5. Verifikasi baris `Excavator Komatsu PC200 {runId}` memuat Group `Kantor Pusat {runId}` dan Status `Disposed`
6. Verifikasi baris `Printer Epson L3250 {runId}` memuat Group `Cabang Surabaya {runId}` dan Status `Unmanaged`
7. Verifikasi baris `Excavator Komatsu PC200 {runId}` memuat Files Size `6.0 MB`
8. Verifikasi baris `Router Mikrotik RB4011 {runId}` memuat Files Size `0.0 KB`
9. Verifikasi Total Size baris `Excavator Komatsu PC200 {runId}` sama dengan jumlah Data & Log Size dan Files Size baris itu

### Aset Active dan Draft tidak didaftar
10. Ganti isi kotak search dengan `Truk Hino 500 {runId}`, tekan Enter
11. Verifikasi pesan `No results found` tampil karena aset Active tidak didaftar
12. Ganti isi kotak search dengan `Kompresor Atlas Copco {runId}`, tekan Enter
13. Verifikasi pesan `No results found` tampil karena aset Draft tidak didaftar
14. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Tab Asset Data read-only dengan toolbar Search, Filter, dan Download
15. Verifikasi caption `Asset data can only be deleted from the Asset menu.` tampil
16. Verifikasi toolbar memuat ikon Search, Filter, dan Download
17. Verifikasi tidak ada tombol `Search by Scan` pada toolbar
18. Verifikasi tidak ada kotak centang pada header tabel maupun pada baris `Excavator Komatsu PC200 {runId}`
19. Verifikasi tidak ada aksi baris pada baris `Excavator Komatsu PC200 {runId}`, termasuk aksi Delete Asset Data
20. Verifikasi tidak ada bar aksi bulk pada tab

### Panel Filter memuat field menurut kolom filterable
21. Klik ikon Filter
22. Verifikasi panel Filter tampil dengan field `Group`, `Status`, `Alias Name`, `TAG`, `Brand`, `Model/Type`, `Category`, `Division`, `Register Date`, `Last Scanned`, `Data & Log Size (KB)`, `Files Size (KB)`, dan `Total Size (KB)`
23. Verifikasi tidak ada field filter untuk `Photo`, `Name`, dan `Asset ID`
24. Verifikasi placeholder field `All groups`, `All statuses`, `All alias names`, `All TAGs`, `All brands`, `All models`, `All categories`, `All divisions`, `Select date`, `Min`, dan `Max`

### Filter Status memuat opsi dari data tabel dan menyaring baris
25. Buka dropdown field `Status`
26. Verifikasi opsi `Disposed` dan `Unmanaged` tampil
27. Verifikasi opsi `Active` dan `Draft` tidak tampil
28. Pilih Status `Unmanaged`
29. Tutup dropdown field `Status`
30. Klik `[Apply]`
31. Verifikasi baris `Printer Epson L3250 {runId}` dan `Scanner Canon DR-C225 {runId}` tampil
32. Verifikasi baris `Excavator Komatsu PC200 {runId}` tidak tampil
33. Klik `[Clear Field]`
34. Klik `[Apply]`

### Filter Group memakai pemilih Tree
35. Pilih Group `Kantor Pusat {runId}` pada panel Filter
36. Klik `[Apply]`
37. Verifikasi baris `Excavator Komatsu PC200 {runId}`, `Forklift Heli CPCD30 {runId}`, dan `Mixer Beton Schwing {runId}` tampil
38. Verifikasi baris `Printer Epson L3250 {runId}` tidak tampil
39. Klik `[Clear Field]`
40. Klik `[Apply]`

### Nilai kosong Division bukan opsi dan tersaring keluar saat filter dipakai
41. Buka dropdown field `Division`
42. Verifikasi opsi `Logistik {runId}` tampil
43. Verifikasi tidak ada opsi kosong di daftar `Division`
44. Pilih Division `Logistik {runId}`
45. Tutup dropdown field `Division`
46. Klik `[Apply]`
47. Verifikasi baris `Mixer Beton Schwing {runId}` tampil
48. Verifikasi baris `Router Mikrotik RB4011 {runId}` tidak tampil karena Division kosong
49. Klik `[Clear Field]`
50. Klik `[Apply]`
51. Verifikasi baris `Router Mikrotik RB4011 {runId}` tampil kembali

### Filter rentang Files Size dengan salah satu batas kosong dan di luar rentang
52. Isi Files Size (KB) Min `1000` dan Max `7000`
53. Klik `[Apply]`
54. Verifikasi baris `Excavator Komatsu PC200 {runId}`, `Scanner Canon DR-C225 {runId}`, dan `Printer Epson L3250 {runId}` tampil
55. Verifikasi baris `Mixer Beton Schwing {runId}`, `Forklift Heli CPCD30 {runId}`, dan `Router Mikrotik RB4011 {runId}` tidak tampil
56. Isi Files Size (KB) hanya Min `5000` dengan Max kosong
57. Klik `[Apply]`
58. Verifikasi baris `Mixer Beton Schwing {runId}` dan `Excavator Komatsu PC200 {runId}` tampil
59. Verifikasi baris `Scanner Canon DR-C225 {runId}` tidak tampil
60. Isi Files Size (KB) hanya Max `1000` dengan Min kosong
61. Klik `[Apply]`
62. Verifikasi baris `Forklift Heli CPCD30 {runId}` dan `Router Mikrotik RB4011 {runId}` tampil
63. Verifikasi baris `Mixer Beton Schwing {runId}` tidak tampil
64. Isi Files Size (KB) Min `20000` dan Max `30000`
65. Klik `[Apply]`
66. Verifikasi pesan `No results found` tampil
67. Klik `[Clear Field]`
68. Klik `[Apply]`

### Filter Register Date walaupun kolomnya tersembunyi
69. Pilih rentang tanggal dari T0 − 25 hari sampai T0 − 15 hari pada field `Register Date`
70. Klik `[Apply]`
71. Verifikasi baris `Forklift Heli CPCD30 {runId}` tampil
72. Verifikasi baris `Excavator Komatsu PC200 {runId}` dan `Mixer Beton Schwing {runId}` tidak tampil
73. Pilih rentang tanggal dari T0 − 60 hari sampai T0 − 40 hari pada field `Register Date`
74. Klik `[Apply]`
75. Verifikasi pesan `No results found` tampil
76. Klik `[Clear Field]`
77. Klik `[Apply]`

### Search kolom Name dan Group
78. Ganti isi kotak search dengan `PC200 {runId}`, tekan Enter
79. Verifikasi baris `Excavator Komatsu PC200 {runId}` tampil
80. Verifikasi baris `Mixer Beton Schwing {runId}` tidak tampil
81. Ganti isi kotak search dengan `Cabang Surabaya {runId}`, tekan Enter
82. Verifikasi baris `Printer Epson L3250 {runId}` tampil
83. Verifikasi baris `Excavator Komatsu PC200 {runId}` tidak tampil

### Kolom searchable yang disembunyikan tidak lagi cocok dan cocok lagi saat ditampilkan
84. Klik header kolom `Actions` (`⋯`) pada tabel
85. Hilangkan centang kolom `Group` pada panel Column Visibility
86. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility
87. Verifikasi header kolom `Group` tidak ada lagi di tabel
88. Ganti isi kotak search dengan `Cabang Surabaya {runId}`, tekan Enter
89. Verifikasi pesan `No results found` tampil
90. Klik header kolom `Actions` (`⋯`) pada tabel
91. Centang kolom `Group` pada panel Column Visibility
92. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility
93. Ganti isi kotak search dengan `Cabang Surabaya {runId}`, tekan Enter
94. Verifikasi baris `Printer Epson L3250 {runId}` tampil
95. Klik `(←)` pada kotak Search

### Filter Alias Name, Brand, Model/Type, dan Category menyaring baris
96. Ketik Search `{runId}`, tekan Enter
97. Buka dropdown field `Alias Name`
98. Pilih Alias Name `Ekskavator Proyek Timur {runId}`
99. Tutup dropdown field `Alias Name`
100. Klik `[Apply]`
101. Verifikasi baris `Excavator Komatsu PC200 {runId}` tampil
102. Verifikasi baris `Mixer Beton Schwing {runId}` tidak tampil
103. Klik `[Clear Field]`
104. Klik `[Apply]`
105. Buka dropdown field `Brand`
106. Pilih Brand `Komatsu Indonesia {runId}`
107. Tutup dropdown field `Brand`
108. Klik `[Apply]`
109. Verifikasi baris `Excavator Komatsu PC200 {runId}` tampil
110. Verifikasi baris `Mixer Beton Schwing {runId}` tidak tampil
111. Klik `[Clear Field]`
112. Klik `[Apply]`
113. Buka dropdown field `Model/Type`
114. Pilih Model/Type `SP500-M {runId}`
115. Tutup dropdown field `Model/Type`
116. Klik `[Apply]`
117. Verifikasi baris `Mixer Beton Schwing {runId}` tampil
118. Verifikasi baris `Excavator Komatsu PC200 {runId}` tidak tampil
119. Klik `[Clear Field]`
120. Klik `[Apply]`
121. Buka dropdown field `Category`
122. Pilih Category `Alat Berat {runId}`
123. Tutup dropdown field `Category`
124. Klik `[Apply]`
125. Verifikasi baris `Excavator Komatsu PC200 {runId}` dan `Mixer Beton Schwing {runId}` tampil
126. Verifikasi baris `Printer Epson L3250 {runId}` tidak tampil
127. Klik `[Clear Field]`
128. Klik `[Apply]`

### Kolom Curated ditampilkan lewat Column Visibility
129. Klik header kolom `Actions` (`⋯`) pada tabel
130. Centang kolom `Alias Name` pada panel Column Visibility
131. Centang kolom `Brand` pada panel Column Visibility
132. Centang kolom `Model / Type` pada panel Column Visibility
133. Centang kolom `Category` pada panel Column Visibility
134. Centang kolom `Division` pada panel Column Visibility
135. Centang kolom `Register Date` pada panel Column Visibility
136. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility
137. Verifikasi header kolom `Alias Name`, `Brand`, `Model / Type`, `Category`, `Division`, dan `Register Date` tampil di tabel

### Search mencocokkan kolom Curated, Asset ID, dan Status
138. Ganti isi kotak search dengan `Ekskavator Proyek Timur {runId}`, tekan Enter
139. Verifikasi baris `Excavator Komatsu PC200 {runId}` tampil
140. Verifikasi baris `Mixer Beton Schwing {runId}` tidak tampil
141. Ganti isi kotak search dengan `Komatsu Indonesia {runId}`, tekan Enter
142. Verifikasi baris `Excavator Komatsu PC200 {runId}` tampil
143. Verifikasi baris `Mixer Beton Schwing {runId}` tidak tampil
144. Ganti isi kotak search dengan `SP500-M {runId}`, tekan Enter
145. Verifikasi baris `Mixer Beton Schwing {runId}` tampil
146. Verifikasi baris `Excavator Komatsu PC200 {runId}` tidak tampil
147. Ganti isi kotak search dengan `Alat Berat {runId}`, tekan Enter
148. Verifikasi baris `Excavator Komatsu PC200 {runId}` dan `Mixer Beton Schwing {runId}` tampil
149. Verifikasi baris `Printer Epson L3250 {runId}` tidak tampil
150. Ganti isi kotak search dengan `Logistik {runId}`, tekan Enter
151. Verifikasi baris `Excavator Komatsu PC200 {runId}` tampil
152. Verifikasi baris `Printer Epson L3250 {runId}` tidak tampil
153. Ganti isi kotak search dengan `Disposed`, tekan Enter
154. Verifikasi baris `Excavator Komatsu PC200 {runId}` tampil
155. Verifikasi baris `Printer Epson L3250 {runId}` tidak tampil
156. Ganti isi kotak search dengan Asset ID milik DU-010-3, tekan Enter
157. Verifikasi baris `Excavator Komatsu PC200 {runId}` tampil
158. Verifikasi baris `Mixer Beton Schwing {runId}` tidak tampil
159. Klik `(←)` pada kotak Search

### Sort kolom Curated, Group, Files Size, Register Date, dan Asset ID pada tiga aset berkategori
160. Buka dropdown field `Category`
161. Pilih Category `Alat Berat {runId}`
162. Pilih Category `Perangkat Kantor {runId}`
163. Tutup dropdown field `Category`
164. Klik `[Apply]`
165. Verifikasi baris `Excavator Komatsu PC200 {runId}`, `Mixer Beton Schwing {runId}`, dan `Printer Epson L3250 {runId}` tampil
166. Klik ikon sort pada header kolom `Group`
167. Verifikasi baris `Printer Epson L3250 {runId}` berada di urutan pertama
168. Klik ikon sort pada header kolom `Group` sekali lagi
169. Verifikasi baris `Printer Epson L3250 {runId}` berada di urutan terakhir
170. Klik ikon sort pada header kolom `Group` untuk ketiga kalinya
171. Klik ikon sort pada header kolom `Alias Name`
172. Verifikasi urutan baris dari atas ke bawah: `Excavator Komatsu PC200 {runId}`, `Mixer Beton Schwing {runId}`, `Printer Epson L3250 {runId}`
173. Klik ikon sort pada header kolom `Alias Name` sekali lagi
174. Verifikasi urutan baris dari atas ke bawah: `Printer Epson L3250 {runId}`, `Mixer Beton Schwing {runId}`, `Excavator Komatsu PC200 {runId}`
175. Klik ikon sort pada header kolom `Alias Name` untuk ketiga kalinya
176. Klik ikon sort pada header kolom `Brand`
177. Verifikasi urutan baris dari atas ke bawah: `Printer Epson L3250 {runId}`, `Excavator Komatsu PC200 {runId}`, `Mixer Beton Schwing {runId}`
178. Klik ikon sort pada header kolom `Brand` sekali lagi
179. Verifikasi urutan baris dari atas ke bawah: `Mixer Beton Schwing {runId}`, `Excavator Komatsu PC200 {runId}`, `Printer Epson L3250 {runId}`
180. Klik ikon sort pada header kolom `Brand` untuk ketiga kalinya
181. Klik ikon sort pada header kolom `Model / Type`
182. Verifikasi urutan baris dari atas ke bawah: `Printer Epson L3250 {runId}`, `Excavator Komatsu PC200 {runId}`, `Mixer Beton Schwing {runId}`
183. Klik ikon sort pada header kolom `Model / Type` sekali lagi
184. Verifikasi urutan baris dari atas ke bawah: `Mixer Beton Schwing {runId}`, `Excavator Komatsu PC200 {runId}`, `Printer Epson L3250 {runId}`
185. Klik ikon sort pada header kolom `Model / Type` untuk ketiga kalinya
186. Klik ikon sort pada header kolom `Category`
187. Verifikasi baris `Printer Epson L3250 {runId}` berada di urutan terakhir
188. Klik ikon sort pada header kolom `Category` sekali lagi
189. Verifikasi baris `Printer Epson L3250 {runId}` berada di urutan pertama
190. Klik ikon sort pada header kolom `Category` untuk ketiga kalinya
191. Klik ikon sort pada header kolom `Division`
192. Verifikasi baris `Printer Epson L3250 {runId}` berada di urutan pertama
193. Klik ikon sort pada header kolom `Division` sekali lagi
194. Verifikasi baris `Printer Epson L3250 {runId}` berada di urutan terakhir
195. Klik ikon sort pada header kolom `Division` untuk ketiga kalinya
196. Klik ikon sort pada header kolom `Files Size`
197. Verifikasi urutan baris dari atas ke bawah: `Printer Epson L3250 {runId}`, `Excavator Komatsu PC200 {runId}`, `Mixer Beton Schwing {runId}`
198. Klik ikon sort pada header kolom `Files Size` sekali lagi
199. Verifikasi urutan baris dari atas ke bawah: `Mixer Beton Schwing {runId}`, `Excavator Komatsu PC200 {runId}`, `Printer Epson L3250 {runId}`
200. Klik ikon sort pada header kolom `Files Size` untuk ketiga kalinya
201. Klik ikon sort pada header kolom `Register Date`
202. Verifikasi urutan baris dari atas ke bawah: `Excavator Komatsu PC200 {runId}`, `Mixer Beton Schwing {runId}`, `Printer Epson L3250 {runId}`
203. Klik ikon sort pada header kolom `Register Date` sekali lagi
204. Verifikasi urutan baris dari atas ke bawah: `Printer Epson L3250 {runId}`, `Mixer Beton Schwing {runId}`, `Excavator Komatsu PC200 {runId}`
205. Klik ikon sort pada header kolom `Register Date` untuk ketiga kalinya
206. Klik ikon sort pada header kolom `Asset ID`
207. Verifikasi Asset ID baris pertama mendahului Asset ID baris kedua menurut urutan alfabetis, dibaca dari tabel
208. Klik ikon sort pada header kolom `Asset ID` sekali lagi
209. Verifikasi Asset ID baris pertama menyusul Asset ID baris kedua menurut urutan alfabetis, dibaca dari tabel
210. Klik ikon sort pada header kolom `Asset ID` untuk ketiga kalinya
211. Klik `[Clear Field]`
212. Klik `[Apply]`

### Kolom Curated disembunyikan kembali
213. Klik header kolom `Actions` (`⋯`) pada tabel
214. Hilangkan centang kolom `Alias Name` pada panel Column Visibility
215. Hilangkan centang kolom `Brand` pada panel Column Visibility
216. Hilangkan centang kolom `Model / Type` pada panel Column Visibility
217. Hilangkan centang kolom `Category` pada panel Column Visibility
218. Hilangkan centang kolom `Division` pada panel Column Visibility
219. Hilangkan centang kolom `Register Date` pada panel Column Visibility
220. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility
221. Verifikasi header kolom `Alias Name`, `Brand`, `Model / Type`, `Category`, `Division`, dan `Register Date` tidak tampil di tabel

### Urutan default Total Size terbesar dan sort Total Size lintas halaman
222. Ketik Search `{runId}`, tekan Enter
223. Verifikasi urutan lima baris pertama dari atas ke bawah: `Mixer Beton Schwing {runId}`, `Excavator Komatsu PC200 {runId}`, `Scanner Canon DR-C225 {runId}`, `Printer Epson L3250 {runId}`, `Forklift Heli CPCD30 {runId}`
224. Klik ikon sort pada header kolom `Total Size`
225. Klik halaman `2` pada Pagination
226. Verifikasi halaman 2 memuat empat baris dari atas ke bawah: `Printer Epson L3250 {runId}`, `Scanner Canon DR-C225 {runId}`, `Excavator Komatsu PC200 {runId}`, `Mixer Beton Schwing {runId}`
227. Klik halaman `1` pada Pagination
228. Klik ikon sort pada header kolom `Total Size` sekali lagi
229. Verifikasi baris pertama halaman 1 adalah `Mixer Beton Schwing {runId}`
230. Klik ikon sort pada header kolom `Total Size` untuk ketiga kalinya

### Sort Name tiga klik kembali ke urutan default
231. Klik ikon sort pada header kolom `Name`
232. Verifikasi baris pertama halaman 1 adalah `Aset Massal 1 {runId}`
233. Klik ikon sort pada header kolom `Name` sekali lagi
234. Verifikasi tiga baris pertama dari atas ke bawah: `Scanner Canon DR-C225 {runId}`, `Router Mikrotik RB4011 {runId}`, `Printer Epson L3250 {runId}`
235. Klik ikon sort pada header kolom `Name` untuk ketiga kalinya
236. Verifikasi baris pertama halaman 1 kembali ke urutan default, yaitu `Mixer Beton Schwing {runId}`

### Sort Status dengan nilai sama diurutkan menurut default sort
237. Klik ikon sort pada header kolom `Status`
238. Verifikasi tiga baris pertama dari atas ke bawah: `Mixer Beton Schwing {runId}`, `Excavator Komatsu PC200 {runId}`, `Forklift Heli CPCD30 {runId}`
239. Klik ikon sort pada header kolom `Status` sekali lagi
240. Klik ikon sort pada header kolom `Status` untuk ketiga kalinya

### Ukuran file di Recycle Bin tetap dihitung dan hilang setelah Permanently Delete
241. Klik tab `Asset Documents`
242. Ketik Search `foto-lelang-ekskavator-{runId}`, tekan Enter
243. Buka aksi baris `foto-lelang-ekskavator-{runId}.pdf`
244. Klik `Delete`
245. Klik `[Delete]` pada dialog `Delete File`
246. Klik tab `Disposed & Unmanaged Assets`
247. Ketik Search `PC200 {runId}`, tekan Enter
248. Verifikasi baris `Excavator Komatsu PC200 {runId}` memuat Files Size `6.0 MB` karena file di Recycle Bin tetap dihitung
249. Klik `Recycle Bin` pada header kartu `Storage Usage`
250. Ketik Search `foto-lelang-ekskavator-{runId}`, tekan Enter
251. Buka aksi baris `foto-lelang-ekskavator-{runId}.pdf`
252. Klik `Permanently Delete`
253. Klik `[Permanently Delete]` pada dialog `Permanently Delete File`
254. Tutup modal `Recycle Bin`
255. Muat ulang halaman
256. Klik tab `Disposed & Unmanaged Assets`
257. Ketik Search `PC200 {runId}`, tekan Enter
258. Verifikasi baris `Excavator Komatsu PC200 {runId}` memuat Files Size `4.0 MB` setelah file dihapus permanen

### Kolom Curated tersembunyi secara default dan tampil setelah dicentang
259. Verifikasi header kolom `Name`, `Asset ID`, `Group`, `Status`, `Data & Log Size`, `Files Size`, dan `Total Size` tampil
260. Verifikasi header kolom `Alias Name`, `TAG`, `Brand`, `Model / Type`, `Category`, `Division`, `Register Date`, dan `Last Scanned` tidak tampil
261. Klik header kolom `Actions` (`⋯`) pada tabel
262. Verifikasi kolom `Division` pada panel Column Visibility tidak tercentang
263. Centang kolom `Division` pada panel Column Visibility
264. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility
265. Verifikasi header kolom `Division` tampil di tabel
266. Klik header kolom `Actions` (`⋯`) pada tabel
267. Hilangkan centang kolom `Division` pada panel Column Visibility
268. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility

### Aset di luar cakupan group aktor tidak tampil di tab Asset Data
269. Aktor kedua `Bima Pengelola {runId}` login di browser lain dan membuka File Manager lewat grup `Settings` di sidebar Fixed Asset
270. Klik tab `Disposed & Unmanaged Assets`
271. Ketik Search `{runId}`, tekan Enter
272. Verifikasi baris `Printer Epson L3250 {runId}` dengan Group `Cabang Surabaya {runId}` tampil
273. Verifikasi baris `Excavator Komatsu PC200 {runId}`, `Forklift Heli CPCD30 {runId}`, dan `Mixer Beton Schwing {runId}` dengan Group `Kantor Pusat {runId}` tidak tampil

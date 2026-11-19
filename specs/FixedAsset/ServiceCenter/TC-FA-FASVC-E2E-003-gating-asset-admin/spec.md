---
id: TC-FA-FASVC-E2E-003-gating-asset-admin
title: "Gating Asset Admin: Role Transaksi, Cakupan, Detail Read-only, dan Tree Available to"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§2.1#b4", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "RA-FASVC-01", "RA-FASVC-02", "RA-FASVC-03", "RA-FASVC-04", "RA-FASVC-05", "RA-FASVC-06", "FASVC-LOGIC-08a", "FASVC-LOGIC-08d", "FASVC-LOGIC-08e", "FASVC-LOGIC-08f", "FASVC-LOGIC-08g", "FASVC-LOGIC-08h", "FASVC-LOGIC-08i", "FASVC-LOGIC-08k", "S-FASVC-13", "S-FASVC-14", "EC-FASVC-15a", "EC-FASVC-15b", "EC-FASVC-15c", "§Aturan Logika Modul#p22", "§Aturan Logika Modul#p24", "§Aturan Logika Modul#p25", "§Aturan Logika Modul#p26", "§2.1#b2", "§12#r1"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [5, 49, 64, 119, 125, 152]
  "§2.1#r2": [23, 33, 82, 141]
  "§2.1#r3": [94, 95, 99, 100, 106]
  "§2.1#r4": [110, 111]
  "§2.1#r5": 10
  "§2.1#b4": [3, 47, 123, 161, 163]
  "§4.8#r1": [3, 47, 123]
  "§4.8#r2": [59, 114, 147, 188]
  "§4.8#r3": [6, 50, 126]
  "§4.8#r4": [60, 61, 86, 87, 115, 116, 148, 149, 190]
  "§4.8#r5": [102, 106, 189]
  "§4.8#r6": [62, 88, 110, 117, 150, 191]
  "§4.8#r7": [7, 51, 127]
  "§4.8#r8": [8, 52, 128]
  "RA-FASVC-01": [59, 114, 147, 188]
  "RA-FASVC-02": [86, 190]
  "RA-FASVC-03": [89, 102, 189]
  "RA-FASVC-04": [87, 103]
  "RA-FASVC-05": [88, 191]
  "RA-FASVC-06": [60, 61, 62, 115, 116, 117, 148, 149, 150]
  "FASVC-LOGIC-08a": [44, 54, 55, 56, 57, 84]
  "FASVC-LOGIC-08d": [23, 33, 82, 141]
  "FASVC-LOGIC-08e": [16, 17, 72, 73, 74, 133, 134, 135, 157]
  "FASVC-LOGIC-08f": [18, 75, 136, 158]
  "FASVC-LOGIC-08g": [86, 87, 88, 91, 94, 99, 106, 110, 115, 116, 117, 189, 190, 191]
  "FASVC-LOGIC-08h": [59, 60, 61, 62, 114, 115, 116, 117, 148, 149, 150, 188, 189, 190, 191]
  "FASVC-LOGIC-08i": [65, 120, 153]
  "FASVC-LOGIC-08k": 82
  "S-FASVC-13": [16, 72, 74, 133, 135]
  "S-FASVC-14": [60, 61, 62, 66, 115, 116, 117, 148, 149, 150]
  "EC-FASVC-15a": [64, 66]
  "EC-FASVC-15b": 65
  "EC-FASVC-15c": [60, 61, 62, 66]
  "§Aturan Logika Modul#p22": 54
  "§Aturan Logika Modul#p24": 59
  "§Aturan Logika Modul#p25": [64, 65]
  "§Aturan Logika Modul#p26": [60, 61, 62, 66, 189, 190, 191]
  "§2.1#b2": [17, 54, 56, 60]
  "§12#r1": 141
anchor: [160, 182]
coverage:
  web: automated
---

# Gating Asset Admin: Role Transaksi, Cakupan, Detail Read-only, dan Tree Available to

## Prerequisites
- Aktor: Asset Admin `Aryo Dua Group {runId}` (Role Transaksi `Maintenance Routine` pada `Branch Surabaya` dan `Branch Malang`), Asset Admin `Anisa Surabaya {runId}` (Role Transaksi `Maintenance Routine` pada `Branch Surabaya`), Asset Admin `Agus Repair Malang {runId}` (Role Transaksi `Repair` pada `Branch Malang`), Asset Admin `Ayu Root {runId}` (Role Transaksi `Maintenance Routine` pada `Head Office`), Asset Admin `Adi Transaksi Lain {runId}` (hanya Role Transaksi `Assignment` pada `Branch Surabaya`), dan Total Control `Tania Control {runId}` sebagai pemicu.
- Layar awal: Dashboard Fixed Asset.
- Data:
  - DU-003-1: Group `Head Office`, node root pohon Group entitas aktor.
  - DU-003-2: Group `Branch Surabaya`, anak dari `Head Office`.
  - DU-003-3: Group `Branch Malang`, anak dari `Head Office`.
  - DU-003-4: Group `Gudang Surabaya`, anak dari `Branch Surabaya`.
  - DU-003-5: Aktor `Aryo Dua Group {runId}` dengan Role `Asset Admin`, Role Transaksi `Maintenance Routine`, cakupan `Branch Surabaya` dan `Branch Malang`.
  - DU-003-6: Aktor `Anisa Surabaya {runId}` dengan Role `Asset Admin`, Role Transaksi `Maintenance Routine`, cakupan `Branch Surabaya` (termasuk `Gudang Surabaya`).
  - DU-003-7: Aktor `Agus Repair Malang {runId}` dengan Role `Asset Admin`, Role Transaksi `Repair`, cakupan `Branch Malang`.
  - DU-003-8: Aktor `Ayu Root {runId}` dengan Role `Asset Admin`, Role Transaksi `Maintenance Routine`, cakupan `Head Office` (node root pohon Group).
  - DU-003-9: Aktor `Adi Transaksi Lain {runId}` dengan Role `Asset Admin`, hanya Role Transaksi `Assignment` pada `Branch Surabaya`.
  - DU-003-10: Aktor `Tania Control {runId}` dengan Role `Total Control`.
  - DU-003-11: Service Center `Servis Dua Group {runId}`, Service type `Routine`, Available to Group dalam cakupan pembuat (`Branch Surabaya` dan `Branch Malang`), City `Surabaya`, Company email `layanan@duagroup.co.id`, dibuat oleh `Aryo Dua Group {runId}`. Usage `0`.
  - DU-003-12: Service Center `Servis Cabang Malang {runId}`, Service type `Routine`, Available to `Branch Malang`, City `Malang`, Company email `info@cabangmalang.co.id`, dibuat oleh `Aryo Dua Group {runId}`. Usage `0`.
  - DU-003-13: Service Center `Servis Semua Group {runId}`, Service type `Routine`, Available to `All groups`, City `Jakarta Selatan`, Company email `layanan@semuagroup.co.id`, dibuat oleh `Tania Control {runId}`. Usage `0`.
  - DU-003-14: Service Center `Servis Gudang Surabaya {runId}`, Service type `Repair`, Available to `Gudang Surabaya`, City `Surabaya`, Company email `layanan@gudangsurabaya.co.id`, dibuat oleh `Anisa Surabaya {runId}`, diubah City-nya menjadi `Sidoarjo`, di-Inactivate, di-Activate, lalu dihapus. Usage `0`.
  - DU-003-15: Service Center `Servis Repair Malang {runId}`, Service type `Repair`, Available to `Branch Malang`, City `Malang`, Company email `layanan@repairmalang.co.id`, dibuat oleh `Agus Repair Malang {runId}`. Usage `0`.
  - DU-003-16: Service Center `Servis Entitas Lain {runId}`, Service type `Routine`, ada di entitas lain (bukan entitas aktor), Usage `0`.
  - DU-003-17: Service Center `Servis Nonaktif Dua Group {runId}`, Service type `Routine`, Available to `Branch Surabaya` dan `Branch Malang`, City `Surabaya`, Company email `layanan@nonaktifduagroup.co.id`, dibuat oleh `Tania Control {runId}` lalu di-Inactivate oleh `Tania Control {runId}`. Status `Inactive`. Usage `0`.
- Kondisi:
  - Lisensi addon Maintenance aktif untuk entitas aktor.
  - Akun semua aktor aktif dan kredensialnya disediakan fase 2.
  - Master Data Count Limit bernilai `1000` dan entitas aktor berisi kurang dari 1.000 Service Center.

## Test Steps

### Menu dan toolbar bagi Asset Admin dua Group
1. Masuk sebagai `Aryo Dua Group {runId}`
2. Buka menu `Add-ons` pada sidebar
3. Verifikasi menu `Service Center` tampil di bawah `Add-ons`
4. Klik `Service Center`
5. Verifikasi halaman daftar Service Center terbuka dengan breadcrumb `Add-ons > Service Center`
6. Verifikasi tombol `[+ Service Center]` tampil
7. Verifikasi tombol `[Download]` tampil
8. Verifikasi tombol `[Changelog]` tampil

### Download menyediakan pilihan unduhan
9. Klik `[Download]`
10. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil
11. Tutup popover Download

### Create bagi Asset Admin dibatasi cakupan Group dan tanpa All groups
12. Klik `[+ Service Center]`
13. Isi Name `Servis Dua Group {runId}`
14. Centang Service type `Routine`
15. Klik field Available to
16. Verifikasi node `Head Office` tampil greyed-out pada tree Available to dengan checkbox disabled, sehingga tidak bisa dipilih
17. Verifikasi node `Branch Surabaya` dan `Branch Malang` tampil pada tree Available to dan tercentang
18. Verifikasi node `All groups` tidak tampil pada tree Available to
19. Klik `[Cancel]` pada dialog tree Available to
20. Isi City `Surabaya`
21. Isi Company email `layanan@duagroup.co.id`
22. Klik `[Submit]`
23. Verifikasi toast `Success, Servis Dua Group {runId} has been added.` tampil

### Create untuk satu Branch saja oleh Asset Admin dua Group
24. Klik `[+ Service Center]`
25. Isi Name `Servis Cabang Malang {runId}`
26. Centang Service type `Routine`
27. Klik field Available to
28. Hapus centang node `Branch Surabaya`
29. Klik `[Select]`
30. Isi City `Malang`
31. Isi Company email `info@cabangmalang.co.id`
32. Klik `[Submit]`
33. Verifikasi toast `Success, Servis Cabang Malang {runId} has been added.` tampil

### Total Control membuat Service Center All groups sebagai pemicu
34. Masuk sebagai `Tania Control {runId}`
35. Buka menu `Add-ons` pada sidebar
36. Klik `Service Center`
37. Klik `[+ Service Center]`
38. Isi Name `Servis Semua Group {runId}`
39. Centang Service type `Routine`
40. Isi City `Jakarta Selatan`
41. Isi Company email `layanan@semuagroup.co.id`
42. Klik `[Submit]`
43. Ketik Search `Servis Semua Group {runId}`, tekan Enter
44. Verifikasi baris `Servis Semua Group {runId}` tampil di tabel

### Menu dan toolbar bagi Asset Admin satu Group
45. Masuk sebagai `Anisa Surabaya {runId}`
46. Buka menu `Add-ons` pada sidebar
47. Verifikasi menu `Service Center` tampil di bawah `Add-ons`
48. Klik `Service Center`
49. Verifikasi halaman daftar Service Center terbuka dengan breadcrumb `Add-ons > Service Center`
50. Verifikasi tombol `[+ Service Center]` tampil
51. Verifikasi tombol `[Download]` tampil
52. Verifikasi tombol `[Changelog]` tampil

### Cakupan baca Asset Admin satu Group mengikuti irisan Available to
53. Ketik Search `{runId}`, tekan Enter
54. Verifikasi baris `Servis Dua Group {runId}` tampil di tabel
55. Verifikasi baris `Servis Semua Group {runId}` tampil di tabel
56. Verifikasi baris `Servis Cabang Malang {runId}` tidak tampil di tabel
57. Verifikasi baris `Servis Entitas Lain {runId}` tidak tampil di tabel

### Service Center yang tersedia untuk dua Group read-only bagi Asset Admin satu Group
58. Klik `⋯` pada baris `Servis Dua Group {runId}`
59. Verifikasi aksi `Detail` tampil
60. Verifikasi aksi `Edit` tidak tampil
61. Verifikasi aksi `Inactivate` tidak tampil
62. Verifikasi aksi `Delete` tidak tampil
63. Klik `Detail`
64. Verifikasi halaman Detail menampilkan nama `Servis Dua Group {runId}`
65. Verifikasi info `This service center also serves groups outside your access. Ask an admin who manages all of them.` tampil
66. Verifikasi menu `⋯` pada header Detail tidak tampil
67. Klik breadcrumb `Service Center`

### Create dengan cakupan Descendant dan Service type Repair oleh Asset Admin Maintenance Routine
68. Klik `[+ Service Center]`
69. Isi Name `Servis Gudang Surabaya {runId}`
70. Centang Service type `Repair`
71. Klik field Available to
72. Verifikasi node `Head Office` tampil greyed-out pada tree Available to dengan checkbox disabled, sehingga tidak bisa dipilih
73. Verifikasi node `Branch Surabaya` dan `Gudang Surabaya` tampil pada tree Available to dan tercentang
74. Verifikasi node `Branch Malang` tidak tampil pada tree Available to
75. Verifikasi node `All groups` tidak tampil pada tree Available to
76. Hapus centang node `Branch Surabaya`
77. Centang node `Gudang Surabaya`
78. Klik `[Select]`
79. Isi City `Surabaya`
80. Isi Company email `layanan@gudangsurabaya.co.id`
81. Klik `[Submit]`
82. Verifikasi toast `Success, Servis Gudang Surabaya {runId} has been added.` tampil
83. Ketik Search `Servis Gudang Surabaya {runId}`, tekan Enter
84. Verifikasi baris `Servis Gudang Surabaya {runId}` tampil di tabel

### Asset Admin mengelola Service Center seluruhnya dalam cakupan dengan Service type Repair
85. Klik `⋯` pada baris `Servis Gudang Surabaya {runId}`
86. Verifikasi aksi `Edit` tampil
87. Verifikasi aksi `Inactivate` tampil
88. Verifikasi aksi `Delete` tampil dan tidak disabled
89. Verifikasi aksi `Activate` tidak tampil
90. Klik `Edit`
91. Verifikasi dialog `Edit Service Center` terbuka
92. Ganti isi City dengan `Sidoarjo`
93. Klik `[Save]`
94. Verifikasi toast `Success, Servis Gudang Surabaya {runId} has been updated.` tampil
95. Verifikasi kolom City pada baris `Servis Gudang Surabaya {runId}` menampilkan `Sidoarjo`
96. Klik `⋯` pada baris `Servis Gudang Surabaya {runId}`
97. Klik `Inactivate`
98. Klik `[Inactivate]`
99. Verifikasi toast `Success, Servis Gudang Surabaya {runId} has been inactivated.` tampil
100. Verifikasi kolom Status pada baris `Servis Gudang Surabaya {runId}` menampilkan `Inactive`
101. Klik `⋯` pada baris `Servis Gudang Surabaya {runId}`
102. Verifikasi aksi `Activate` tampil dan tidak disabled
103. Verifikasi aksi `Inactivate` tidak tampil
104. Klik `Activate`
105. Klik `[Activate]`
106. Verifikasi toast `Success, Servis Gudang Surabaya {runId} has been activated.` tampil
107. Klik `⋯` pada baris `Servis Gudang Surabaya {runId}`
108. Klik `Delete`
109. Klik `[Delete]`
110. Verifikasi toast `Success, Servis Gudang Surabaya {runId} has been deleted.` tampil
111. Verifikasi empty state `No results found` tampil untuk Search `Servis Gudang Surabaya {runId}`

### Service Center All groups read-only bagi Asset Admin satu Group
112. Ganti isi kotak search dengan `Servis Semua Group {runId}`, tekan Enter
113. Klik `⋯` pada baris `Servis Semua Group {runId}`
114. Verifikasi aksi `Detail` tampil
115. Verifikasi aksi `Edit` tidak tampil
116. Verifikasi aksi `Inactivate` tidak tampil
117. Verifikasi aksi `Delete` tidak tampil
118. Klik `Detail`
119. Verifikasi halaman Detail menampilkan nama `Servis Semua Group {runId}`
120. Verifikasi info `This service center also serves groups outside your access. Ask an admin who manages all of them.` tampil

### Menu dan toolbar bagi Asset Admin Repair
121. Masuk sebagai `Agus Repair Malang {runId}`
122. Buka menu `Add-ons` pada sidebar
123. Verifikasi menu `Service Center` tampil di bawah `Add-ons`
124. Klik `Service Center`
125. Verifikasi halaman daftar Service Center terbuka dengan breadcrumb `Add-ons > Service Center`
126. Verifikasi tombol `[+ Service Center]` tampil
127. Verifikasi tombol `[Download]` tampil
128. Verifikasi tombol `[Changelog]` tampil

### Create oleh Asset Admin Repair dan tree dilihat aktor dengan cakupan berbeda
129. Klik `[+ Service Center]`
130. Isi Name `Servis Repair Malang {runId}`
131. Centang Service type `Repair`
132. Klik field Available to
133. Verifikasi node `Head Office` tampil greyed-out pada tree Available to dengan checkbox disabled, sehingga tidak bisa dipilih
134. Verifikasi node `Branch Malang` tampil pada tree Available to dan tercentang
135. Verifikasi node `Branch Surabaya` tidak tampil pada tree Available to
136. Verifikasi node `All groups` tidak tampil pada tree Available to
137. Klik `[Cancel]` pada dialog tree Available to
138. Isi City `Malang`
139. Isi Company email `layanan@repairmalang.co.id`
140. Klik `[Submit]`
141. Verifikasi toast `Success, Servis Repair Malang {runId} has been added.` tampil

### Asset Admin dengan cakupan root tidak melihat info dan tidak memilih All groups
142. Masuk sebagai `Ayu Root {runId}`
143. Buka menu `Add-ons` pada sidebar
144. Klik `Service Center`
145. Ketik Search `Servis Semua Group {runId}`, tekan Enter
146. Klik `⋯` pada baris `Servis Semua Group {runId}`
147. Verifikasi aksi `Detail` tampil
148. Verifikasi aksi `Edit` tidak tampil
149. Verifikasi aksi `Inactivate` tidak tampil
150. Verifikasi aksi `Delete` tidak tampil
151. Klik `Detail`
152. Verifikasi halaman Detail menampilkan nama `Servis Semua Group {runId}`
153. Verifikasi info `This service center also serves groups outside your access. Ask an admin who manages all of them.` tidak tampil
154. Klik breadcrumb `Service Center`
155. Klik `[+ Service Center]`
156. Klik field Available to
157. Verifikasi node `Head Office` tampil pada tree Available to dan bisa dipilih
158. Verifikasi node `All groups` tidak tampil pada tree Available to

### Asset Admin tanpa Role Transaksi Maintenance Routine atau Repair tidak punya akses
159. Masuk sebagai `Adi Transaksi Lain {runId}`
160. Verifikasi menu `Dashboard` tampil pada sidebar
161. Verifikasi menu `Service Center` tidak tampil pada sidebar
162. Buka halaman daftar Service Center lewat alamat langsung
163. Verifikasi empty state `You do not have access to Service Center.` tampil

### Service Center Inactive sebagian di luar cakupan kelola tanpa aksi Activate bagi Asset Admin satu Group
164. Masuk sebagai `Tania Control {runId}`
165. Buka menu `Add-ons` pada sidebar
166. Klik `Service Center`
167. Klik `[+ Service Center]`
168. Isi Name `Servis Nonaktif Dua Group {runId}`
169. Centang Service type `Routine`
170. Klik field Available to
171. Hapus centang node `All groups`
172. Centang node `Branch Surabaya`
173. Centang node `Branch Malang`
174. Klik `[Select]`
175. Isi City `Surabaya`
176. Isi Company email `layanan@nonaktifduagroup.co.id`
177. Klik `[Submit]`
178. Ketik Search `Servis Nonaktif Dua Group {runId}`, tekan Enter
179. Klik `⋯` pada baris `Servis Nonaktif Dua Group {runId}`
180. Klik `Inactivate`
181. Klik `[Inactivate]`
182. Verifikasi kolom Status pada baris `Servis Nonaktif Dua Group {runId}` menampilkan `Inactive`
183. Masuk sebagai `Anisa Surabaya {runId}`
184. Buka menu `Add-ons` pada sidebar
185. Klik `Service Center`
186. Ketik Search `Servis Nonaktif Dua Group {runId}`, tekan Enter
187. Klik `⋯` pada baris `Servis Nonaktif Dua Group {runId}`
188. Verifikasi aksi `Detail` tampil
189. Verifikasi aksi `Activate` tidak tampil
190. Verifikasi aksi `Edit` tidak tampil
191. Verifikasi aksi `Delete` tidak tampil

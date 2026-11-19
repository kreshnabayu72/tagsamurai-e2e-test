---
id: TC-FA-ASTL-E2E-028-gating-manage-asset-tag
title: "Gating UI untuk Manage asset dan TAG"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-10k", "ASTL-LOGIC-10l", "ASTL-LOGIC-10n", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§2#r1", "§2#r2", "§2#r3", "§2#r4", "§2#r5", "§2#r6", "§2#r7", "§2#r8", "§2#r9", "§2#r10", "§2#r11", "§2#r12", "§2#r13", "§2#r14", "§2#r15", "§2#r16", "§2#p3", "§9.11#r1", "§9.11#r2", "§9.11#r3", "§9.11#r4", "§9.11#r5", "§9.11#r6", "§9.11#r7", "EB-AKS-5@add-label", "EB-AKS-5@remove-label", "EB-AKS-5@manage-asset", "EB-AKS-5@delete-asset-data"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-10k": [36, 37, 38, 39, 40, 41]
  "ASTL-LOGIC-10l": [37, 41]
  "ASTL-LOGIC-10n": 31
  "§4.8#r1": [4, 5, 9, 20, 51, 136]
  "§4.8#r2": [10, 123, 229, 230, 233, 234, 238, 243, 250, 253, 256, 260, 265, 270, 277, 280, 283, 287, 292, 297, 304, 307, 310, 314, 319, 324]
  "§4.8#r3": [11, 52, 118, 141]
  "§4.8#r4": [12, 138]
  "§4.8#r5": [13, 122, 138, 150, 167]
  "§4.8#r6": [21, 128, 144, 155, 171, 195]
  "§4.8#r7": [15, 128, 145, 155, 196]
  "§4.8#r8": [16, 137, 163, 180]
  "§4.8#r9": [14, 116, 134, 138, 161, 163]
  "§4.8#r10": [24, 148]
  "§4.8#r11": [26, 134, 150, 167]
  "§4.8#r12": [17, 27]
  "§4.8#r13": [6, 7]
  "§4.8#r14": [36, 37, 38, 39, 40, 41]
  "§2#r1": [13, 14, 15, 21, 145]
  "§2#r2": [36, 37]
  "§2#r3": [17, 27, 40, 41]
  "§2#r4": [11, 36, 37, 38, 39, 52]
  "§2#r5": [2, 3, 4, 5, 7, 9, 13, 15, 20, 21, 36, 37, 51, 116]
  "§2#r6": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37, 51]
  "§2#r7": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37, 51]
  "§2#r8": [109, 110, 111]
  "§2#r9": [101, 102, 103]
  "§2#r10": [21, 93, 94, 95, 145]
  "§2#r11": [2, 3, 4, 5, 7, 9, 13, 15, 20, 21, 36, 37, 51, 145]
  "§2#r12": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37, 51]
  "§2#r13": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37, 51]
  "§2#r14": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37, 51]
  "§2#r15": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37, 51]
  "§2#r16": [2, 3, 4, 5, 7, 9, 13, 15, 20, 36, 37, 51]
  "§2#p3": [2, 3, 7, 13, 15, 21, 145, 186, 187, 188]
  "§9.11#r1": [2, 3, 7]
  "§9.11#r2": [36, 37]
  "§9.11#r3": [32, 40, 41]
  "§9.11#r4": 33
  "§9.11#r5": [38, 39]
  "§9.11#r6": 46
  "§9.11#r7": 49
  "EB-AKS-5@add-label": [61, 62, 204, 205]
  "EB-AKS-5@remove-label": [70, 71, 213, 214]
  "EB-AKS-5@manage-asset": [77, 78, 174, 175]
  "EB-AKS-5@delete-asset-data": [85, 87, 88, 222, 224, 225]
anchor: [43, 45, 48]
coverage:
  web: automated
---

# Gating UI untuk Manage asset dan TAG

## Prerequisites
- Aktor: `Budi Santoso {runId}`, pemegang role Manage asset & TAG (Read + Update + Delete) dengan cakupan Group `IT {runId}` beserta descendant.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-028-1: User, Name `Budi Santoso {runId}`, Role `Manage asset & TAG`, Cakupan `Group IT {runId} beserta descendant`
  - DU-028-2: Group, Name `IT {runId}`
  - DU-028-3: Group, Name `Cabang Bandung {runId}`
  - DU-028-4: Asset, Name `Laptop Pro 16 {runId}`, Group `IT {runId}`, Status `Available`, TAG `RFID` berstatus `Paired`, Asset Class `Peralatan IT {runId}`, Tax Depreciation Class `Kelompok 1 {runId}`, Purchase Date `T0 − 30 hari`, Purchase Cost `18500000`, Warranty Until `T0 + 200 hari`
  - DU-028-5: Asset, Name `Kursi Kerja {runId}`, Group `IT {runId}`, Status `Available`
  - DU-028-6: Asset, Name `Kamera Mirrorless {runId}`, Group `IT {runId}`, Status `Available`, License `Unmanaged`
  - DU-028-7: Asset, Name `Printer Laser {runId}`, Group `Cabang Bandung {runId}`, Status `Available`
  - DU-028-8: Custom Field, Name `Nomor PO {runId}`, Group `Purchasing`
  - DU-028-9: Custom Field, Name `Kode Anggaran {runId}`, Group `Accounting`
  - DU-028-10: Asset, Name `Proyektor X2 {runId}`, Group `IT {runId}`, Status `Damaged`
  - DU-028-11: Asset, Name `Switch Jaringan {runId}`, Group `IT {runId}`, Status `Available`, License `Unmanaged`
  - DU-028-12: Label, Name `Aset Kantor {runId}`
  - DU-028-13: Asset, Name `Tablet Survei {runId}`, Group `IT {runId}`, Status `Missing`
  - DU-028-14: Asset, Name `Kamera Aksi {runId}`, Group `IT {runId}`, Status `Available`, License `Unmanaged`
  - DU-028-15: Asset, Name `Kamera Arsip {runId}`, Group `IT {runId}`, Status `Available`, License `Unmanaged`
  - DU-028-16: User role tambahan, Name `Budi Santoso {runId}`, Role `Manage purchase` (Read + Update), Cakupan `Group IT {runId} beserta descendant`; baru diberikan di langkah 182 dan tidak berlaku sebelum langkah itu
  - DU-028-17: Asset, Name `Proyektor Pinjam {runId}`, Group `IT {runId}`, Status `Borrowed`
  - DU-028-18: Asset, Name `Laptop Tugas {runId}`, Group `IT {runId}`, Status `Assigned`
  - Nama baris yang diharapkan untuk Asset Name `Laptop Pro 16 {runId}` adalah `Laptop Pro 16 {runId} - 1`, dari Asset Name `Laptop Pro 16 {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kursi Kerja {runId}` adalah `Kursi Kerja {runId} - 1`, dari Asset Name `Kursi Kerja {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kamera Mirrorless {runId}` adalah `Kamera Mirrorless {runId} - 1`, dari Asset Name `Kamera Mirrorless {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Printer Laser {runId}` adalah `Printer Laser {runId} - 1`, dari Asset Name `Printer Laser {runId}`.
  - Purchase Cost yang diharapkan untuk Purchase Cost `18500000` adalah `Rp 18.500.000,00`, dari Purchase Cost `18500000`.
  - Kursi Kerja {runId} tidak memiliki Purchase Information dan Asset Name-nya tanpa Asset Class; Kamera Mirrorless {runId} adalah aset Unmanaged.
  - Aset `Laptop Pro 16 {runId}` dan `Kursi Kerja {runId}` tercatat di group `IT {runId}`; user hanya mengakses group yang sesuai cakupannya.
  - Nama baris yang diharapkan untuk Asset Name `Proyektor X2 {runId}` adalah `Proyektor X2 {runId} - 1`, dari Asset Name `Proyektor X2 {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Switch Jaringan {runId}` adalah `Switch Jaringan {runId} - 1`, dari Asset Name `Switch Jaringan {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Tablet Survei {runId}` adalah `Tablet Survei {runId} - 1`, dari Asset Name `Tablet Survei {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kamera Aksi {runId}` adalah `Kamera Aksi {runId} - 1`, dari Asset Name `Kamera Aksi {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kamera Arsip {runId}` adalah `Kamera Arsip {runId} - 1`, dari Asset Name `Kamera Arsip {runId}`.
  - `Switch Jaringan {runId}`, `Kamera Mirrorless {runId}`, `Kamera Aksi {runId}`, dan `Kamera Arsip {runId}` adalah aset Unmanaged tanpa jejak finansial; `Laptop Pro 16 {runId}` adalah aset managed dengan TAG `RFID` berstatus Paired.
  - Nama baris yang diharapkan untuk Asset Name `Proyektor Pinjam {runId}` adalah `Proyektor Pinjam {runId} - 1`, dari Asset Name `Proyektor Pinjam {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Laptop Tugas {runId}` adalah `Laptop Tugas {runId} - 1`, dari Asset Name `Laptop Tugas {runId}`.
  - `Proyektor Pinjam {runId}` sedang dipinjam (Custody `Borrowed`) dan `Laptop Tugas {runId}` sedang ditugaskan (Custody `Assigned`).
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Lisensi `FA-7` aktif pada entitas.
  - Feature Suite Borrow, Assignment, dan Transfer berada di level `Full`.
  - Available license di group `IT {runId}` paling sedikit `2`.

## Test Steps

### Tabel, kartu, dan cakupan group tampil sesuai hak
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Laptop Pro 16 {runId} - 1`, `Kursi Kerja {runId} - 1`, dan `Kamera Mirrorless {runId} - 1` tampil di tabel
3. Verifikasi baris `Printer Laser {runId} - 1` tidak tampil di tabel
4. Verifikasi tabel dan kartu status `All` tampil
5. Verifikasi ikon `Changelog` dan tombol `Download` tampil di toolbar
6. Verifikasi Sidebar Group tampil dengan node `All Groups`
7. Verifikasi Sidebar Group memuat node `IT {runId}` dan tidak memuat node `Cabang Bandung {runId}`

### Aksi baris pada aset Available
8. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
9. Verifikasi aksi `Detail` tampil
10. Verifikasi aksi `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft` tidak dirender (Hidden)
11. Verifikasi aksi `Report Disposal` tidak dirender (Hidden)
12. Verifikasi aksi `Report Damage` dan `Report Missing` tampil
13. Verifikasi aksi `Edit` dan `Replace TAG` tampil
14. Verifikasi aksi `Print Label` tampil
15. Verifikasi aksi `Delete Asset Data` tidak dirender (Hidden) pada aset managed yang belum Disposed
16. Verifikasi aksi `Report TAG` tidak dirender (Hidden)
17. Verifikasi aksi `Edit Purchase` tidak dirender (Hidden)
18. Tekan Esc

### Aksi Manage pada aset Unmanaged
19. Klik `⋯` pada baris `Kamera Mirrorless {runId} - 1`
20. Verifikasi aksi `Detail` tampil
21. Verifikasi aksi `Manage` dan `Delete Asset Data` tampil
22. Tekan Esc

### Checkbox baris, Bar Bulk, dan aksi Bulk
23. Centang baris `Laptop Pro 16 {runId} - 1`
24. Verifikasi checkbox baris dan Bar Bulk tampil
25. Klik tombol Bulk Action
26. Verifikasi aksi Bulk `Print Label`, `Add Label`, dan `Remove Label` tampil
27. Verifikasi aksi Bulk `Edit Purchase` tidak dirender (Hidden)
28. Tekan Esc
29. Klik `×` pada Bar Bulk

### Setup Column dan sel kolom bergerbang
30. Buka Setup Column
31. Verifikasi kolom `Asset Value (Commercial)`, `Asset Class`, `Tax Depreciation Class`, `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry` tersedia di Setup Column
32. Verifikasi kolom custom field Purchasing `Nomor PO {runId}` tidak tersedia di Setup Column
33. Verifikasi kolom custom field Accounting `Kode Anggaran {runId}` tidak tersedia di Setup Column
34. Tampilkan kolom `Asset Value (Commercial)`, `Asset Class`, `Tax Depreciation Class`, `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry`
35. Tutup Setup Column
36. Verifikasi sel `Asset Value (Commercial)` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
37. Verifikasi sel `Asset Value (Commercial)` baris `Kursi Kerja {runId} - 1` menampilkan `No access`, bukan `Pending`
38. Verifikasi sel `Asset Class` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
39. Verifikasi sel `Tax Depreciation Class` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
40. Verifikasi sel `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry` baris `Laptop Pro 16 {runId} - 1` menampilkan `No access`
41. Verifikasi sel `Purchase Date` dan `Purchase Cost` baris `Kursi Kerja {runId} - 1` menampilkan `No access`, bukan `Pending`

### Dokumen Purchase dan data Accounting di Asset Detail
42. Klik Name `Laptop Pro 16 {runId} - 1`
43. Verifikasi halaman detail aset `Laptop Pro 16 {runId} - 1` terbuka bagi `Budi Santoso {runId}`
44. Buka tab `Documents`
45. Verifikasi tab `Documents` terbuka bagi `Budi Santoso {runId}`
46. Verifikasi kelompok Purchase pada tab `Documents` tidak tampil
47. Buka tab `Accounting`
48. Verifikasi tab `Accounting` terbuka bagi `Budi Santoso {runId}`
49. Verifikasi data tab `Accounting` (peringatan fisik vs buku, Depreciation, Acquisition & Value changes, Journals) tidak tampil

### Report Disposal pada aset Damaged
50. Klik `⋯` pada baris `Proyektor X2 {runId} - 1`
51. Verifikasi aksi `Detail` tampil
52. Verifikasi aksi `Report Disposal` tampil
53. Tekan Esc

### Add Label berhasil dijalankan
54. Muat ulang halaman
55. Ketik Search `{runId}`, tekan Enter
56. Centang baris `Laptop Pro 16 {runId} - 1`
57. Klik tombol Bulk Action
58. Klik `Add Label`
59. Pilih label `Aset Kantor {runId}` pada dialog Add Label
60. Klik `[Apply]`
61. Verifikasi toast `Success, label has been added.` tampil
62. Verifikasi kolom Labels baris `Laptop Pro 16 {runId} - 1` memuat chip `Aset Kantor {runId}`

### Remove Label berhasil dijalankan
63. Muat ulang halaman
64. Ketik Search `{runId}`, tekan Enter
65. Centang baris `Laptop Pro 16 {runId} - 1`
66. Klik tombol Bulk Action
67. Klik `Remove Label`
68. Pilih label `Aset Kantor {runId}` pada dialog Remove Label
69. Klik `[Apply]`
70. Verifikasi toast `Success, label has been removed.` tampil
71. Verifikasi kolom Labels baris `Laptop Pro 16 {runId} - 1` tidak lagi memuat chip `Aset Kantor {runId}`

### Manage aset Unmanaged berhasil dijalankan
72. Muat ulang halaman
73. Ketik Search `{runId}`, tekan Enter
74. Klik `⋯` pada baris `Kamera Mirrorless {runId} - 1`
75. Klik `Manage`
76. Klik `[Manage]` pada dialog Manage Asset
77. Verifikasi toast `Success, asset has been sent to be managed.` tampil
78. Verifikasi baris `Kamera Mirrorless {runId} - 1` menampilkan status `Pending Activation`

### Delete Asset Data berhasil dijalankan
79. Muat ulang halaman
80. Ketik Search `{runId}`, tekan Enter
81. Klik `⋯` pada baris `Switch Jaringan {runId} - 1`
82. Klik `Delete Asset Data`
83. Centang `I understand that the asset data, all its logs, and all its attachments will be permanently deleted.`
84. Klik `[Delete]`
85. Verifikasi toast `Success, asset data has been deleted.` tampil
86. Ketik Search `{runId}`, tekan Enter
87. Verifikasi baris `Laptop Pro 16 {runId} - 1` tetap tampil
88. Verifikasi baris `Switch Jaringan {runId} - 1` tidak tampil

### Hak diubah menjadi Manage asset & TAG (Read + Delete)
89. Admin mengubah hak `Budi Santoso {runId}` pada group `IT {runId}` menjadi `Manage asset & TAG` (Read + Delete)
90. Muat ulang halaman
91. Ketik Search `{runId}`, tekan Enter
92. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
93. Verifikasi aksi `Detail` tampil
94. Verifikasi aksi `Edit` tidak dirender (Hidden)
95. Verifikasi aksi `Delete Asset Data` tidak dirender (Hidden) pada aset managed yang belum Disposed
96. Tekan Esc

### Hak diubah menjadi Manage asset & TAG (Read + Update)
97. Admin mengubah hak `Budi Santoso {runId}` pada group `IT {runId}` menjadi `Manage asset & TAG` (Read + Update)
98. Muat ulang halaman
99. Ketik Search `{runId}`, tekan Enter
100. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
101. Verifikasi aksi `Detail` tampil
102. Verifikasi aksi `Edit` tampil
103. Verifikasi aksi `Delete Asset Data` tidak dirender (Hidden)
104. Tekan Esc

### Hak diubah menjadi Manage asset & TAG (Read)
105. Admin mengubah hak `Budi Santoso {runId}` pada group `IT {runId}` menjadi `Manage asset & TAG` (Read)
106. Muat ulang halaman
107. Ketik Search `{runId}`, tekan Enter
108. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
109. Verifikasi aksi `Detail` tampil
110. Verifikasi aksi `Edit` tidak dirender (Hidden)
111. Verifikasi aksi `Delete Asset Data` tidak dirender (Hidden)
112. Tekan Esc

### Hak dikembalikan menjadi Manage asset & TAG (Read + Update + Delete)
113. Admin mengubah hak `Budi Santoso {runId}` pada group `IT {runId}` menjadi `Manage asset & TAG` (Read + Update + Delete)
114. Muat ulang halaman
115. Ketik Search `{runId}`, tekan Enter
116. Verifikasi tombol `Print Label` tampil di toolbar
117. Klik `⋯` pada baris `Tablet Survei {runId} - 1`
118. Verifikasi aksi `Report Disposal` tampil untuk aset berstatus `Missing`
119. Tekan Esc
120. Centang baris `Laptop Pro 16 {runId} - 1`
121. Klik tombol Bulk Action
122. Verifikasi aksi Bulk `Batch Replace TAG` tampil
123. Verifikasi aksi Bulk `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, dan `Add to Transfer Draft` tidak dirender (Hidden)
124. Tekan Esc
125. Klik `×` pada Bar Bulk
126. Centang baris `Kamera Aksi {runId} - 1` dan `Kamera Arsip {runId} - 1`
127. Klik tombol Bulk Action
128. Verifikasi aksi Bulk `Manage` dan `Delete Asset Data` tampil
129. Tekan Esc
130. Klik `×` pada Bar Bulk

### Hak diubah menjadi Manage asset & TAG (Read + Delete) menampilkan Report TAG dan Delete Asset Data pada aset Unmanaged
131. Admin mengubah hak `Budi Santoso {runId}` pada group `IT {runId}` menjadi `Manage asset & TAG` (Read + Delete)
132. Muat ulang halaman
133. Ketik Search `{runId}`, tekan Enter
134. Verifikasi tombol `Print Label` tidak dirender di toolbar (Hidden)
135. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
136. Verifikasi aksi `Detail` tampil
137. Verifikasi aksi `Report TAG` tampil
138. Verifikasi aksi `Replace TAG`, `Report Damage`, `Report Missing`, dan `Print Label` tidak dirender (Hidden)
139. Tekan Esc
140. Klik `⋯` pada baris `Tablet Survei {runId} - 1`
141. Verifikasi aksi `Report Disposal` tidak dirender (Hidden)
142. Tekan Esc
143. Klik `⋯` pada baris `Kamera Arsip {runId} - 1`
144. Verifikasi aksi `Manage` tidak dirender (Hidden)
145. Verifikasi aksi `Delete Asset Data` tampil
146. Tekan Esc
147. Centang baris `Laptop Pro 16 {runId} - 1`
148. Verifikasi checkbox baris dan Bar Bulk tampil
149. Klik tombol Bulk Action
150. Verifikasi aksi Bulk `Print Label`, `Add Label`, `Remove Label`, dan `Batch Replace TAG` tidak dirender (Hidden)
151. Tekan Esc
152. Klik `×` pada Bar Bulk
153. Centang baris `Kamera Arsip {runId} - 1`
154. Klik tombol Bulk Action
155. Verifikasi aksi Bulk `Delete Asset Data` tampil dan aksi Bulk `Manage` tidak dirender (Hidden)
156. Tekan Esc
157. Klik `×` pada Bar Bulk

### Hak diubah menjadi Manage asset & TAG (Read + Update) menjalankan Manage pada aset Unmanaged
158. Admin mengubah hak `Budi Santoso {runId}` pada group `IT {runId}` menjadi `Manage asset & TAG` (Read + Update)
159. Muat ulang halaman
160. Ketik Search `{runId}`, tekan Enter
161. Verifikasi tombol `Print Label` tampil di toolbar
162. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
163. Verifikasi aksi `Print Label` tampil dan aksi `Report TAG` tidak dirender (Hidden)
164. Tekan Esc
165. Centang baris `Laptop Pro 16 {runId} - 1`
166. Klik tombol Bulk Action
167. Verifikasi aksi Bulk `Print Label`, `Add Label`, `Remove Label`, dan `Batch Replace TAG` tampil
168. Tekan Esc
169. Klik `×` pada Bar Bulk
170. Klik `⋯` pada baris `Kamera Aksi {runId} - 1`
171. Verifikasi aksi `Manage` tampil dan aksi `Delete Asset Data` tidak dirender (Hidden)
172. Klik `Manage`
173. Klik `[Manage]` pada dialog Manage Asset
174. Verifikasi toast `Success, asset has been sent to be managed.` tampil
175. Verifikasi baris `Kamera Aksi {runId} - 1` menampilkan status `Pending Activation`

### Hak diubah menjadi Manage asset & TAG (Read) menampilkan Report TAG
176. Admin mengubah hak `Budi Santoso {runId}` pada group `IT {runId}` menjadi `Manage asset & TAG` (Read)
177. Muat ulang halaman
178. Ketik Search `{runId}`, tekan Enter
179. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
180. Verifikasi aksi `Report TAG` tampil
181. Tekan Esc

### Gabungan hak dari beberapa role pada group yang sama
182. Admin menambahkan hak `Manage purchase` (Read + Update) untuk `Budi Santoso {runId}` pada group `IT {runId}`, tanpa mengubah hak `Manage asset & TAG` (Read)
183. Muat ulang halaman
184. Ketik Search `{runId}`, tekan Enter
185. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
186. Verifikasi aksi `Edit Purchase` tampil
187. Verifikasi aksi `Report TAG` tampil
188. Verifikasi aksi `Edit` tidak dirender (Hidden)
189. Tekan Esc

### Hak Manage asset & TAG (Read + Update) menjalankan Bulk Manage, Add Label, dan Remove Label
190. Admin mengubah hak `Budi Santoso {runId}` pada group `IT {runId}` menjadi `Manage asset & TAG` (Read + Update)
191. Muat ulang halaman
192. Ketik Search `{runId}`, tekan Enter
193. Centang baris `Kamera Arsip {runId} - 1`
194. Klik tombol Bulk Action
195. Verifikasi aksi Bulk `Manage` tampil
196. Verifikasi aksi Bulk `Delete Asset Data` tidak dirender (Hidden)
197. Tekan Esc
198. Klik `×` pada Bar Bulk
199. Centang baris `Laptop Pro 16 {runId} - 1`
200. Klik tombol Bulk Action
201. Klik `Add Label`
202. Pilih label `Aset Kantor {runId}` pada dialog Add Label
203. Klik `[Apply]`
204. Verifikasi toast `Success, label has been added.` tampil
205. Verifikasi kolom Labels baris `Laptop Pro 16 {runId} - 1` memuat chip `Aset Kantor {runId}`
206. Muat ulang halaman
207. Ketik Search `{runId}`, tekan Enter
208. Centang baris `Laptop Pro 16 {runId} - 1`
209. Klik tombol Bulk Action
210. Klik `Remove Label`
211. Pilih label `Aset Kantor {runId}` pada dialog Remove Label
212. Klik `[Apply]`
213. Verifikasi toast `Success, label has been removed.` tampil
214. Verifikasi kolom Labels baris `Laptop Pro 16 {runId} - 1` tidak lagi memuat chip `Aset Kantor {runId}`

### Hak Manage asset & TAG (Read + Delete) menjalankan Delete Asset Data
215. Admin mengubah hak `Budi Santoso {runId}` pada group `IT {runId}` menjadi `Manage asset & TAG` (Read + Delete)
216. Muat ulang halaman
217. Ketik Search `{runId}`, tekan Enter
218. Klik `⋯` pada baris `Kamera Arsip {runId} - 1`
219. Klik `Delete Asset Data`
220. Centang `I understand that the asset data, all its logs, and all its attachments will be permanently deleted.`
221. Klik `[Delete]`
222. Verifikasi toast `Success, asset data has been deleted.` tampil
223. Ketik Search `{runId}`, tekan Enter
224. Verifikasi baris `Laptop Pro 16 {runId} - 1` tetap tampil
225. Verifikasi baris `Kamera Arsip {runId} - 1` tidak tampil

### Mark as Returned dan Mark as Unassigned pada aset Borrowed dan Assigned
226. Muat ulang halaman
227. Ketik Search `{runId}`, tekan Enter
228. Klik `⋯` pada baris `Proyektor Pinjam {runId} - 1`
229. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
230. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
231. Tekan Esc
232. Klik `⋯` pada baris `Laptop Tugas {runId} - 1`
233. Verifikasi aksi `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Assigned`
234. Verifikasi aksi `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Assigned`
235. Tekan Esc
236. Centang baris `Proyektor Pinjam {runId} - 1`
237. Klik tombol Bulk Action
238. Verifikasi aksi Bulk `Mark as Returned` tidak dirender (Hidden) untuk aset berstatus `Borrowed`
239. Tekan Esc
240. Klik `×` pada Bar Bulk
241. Centang baris `Laptop Tugas {runId} - 1`
242. Klik tombol Bulk Action
243. Verifikasi aksi Bulk `Mark as Unassigned` tidak dirender (Hidden) untuk aset berstatus `Assigned`
244. Tekan Esc
245. Klik `×` pada Bar Bulk

### Hak diubah menjadi Manage asset & TAG (Read + Update) tidak menampilkan aksi transaksi
246. Admin mengubah hak `Budi Santoso {runId}` pada group `IT {runId}` menjadi `Manage asset & TAG` (Read + Update)
247. Muat ulang halaman
248. Ketik Search `{runId}`, tekan Enter
249. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
250. Verifikasi aksi `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft` tidak dirender (Hidden)
251. Tekan Esc
252. Klik `⋯` pada baris `Proyektor Pinjam {runId} - 1`
253. Verifikasi aksi `Mark as Returned` dan `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
254. Tekan Esc
255. Klik `⋯` pada baris `Laptop Tugas {runId} - 1`
256. Verifikasi aksi `Mark as Unassigned` dan `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Assigned`
257. Tekan Esc
258. Centang baris `Laptop Pro 16 {runId} - 1`
259. Klik tombol Bulk Action
260. Verifikasi aksi Bulk `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft` tidak dirender (Hidden)
261. Tekan Esc
262. Klik `×` pada Bar Bulk
263. Centang baris `Proyektor Pinjam {runId} - 1`
264. Klik tombol Bulk Action
265. Verifikasi aksi Bulk `Mark as Returned` tidak dirender (Hidden) untuk aset berstatus `Borrowed`
266. Tekan Esc
267. Klik `×` pada Bar Bulk
268. Centang baris `Laptop Tugas {runId} - 1`
269. Klik tombol Bulk Action
270. Verifikasi aksi Bulk `Mark as Unassigned` tidak dirender (Hidden) untuk aset berstatus `Assigned`
271. Tekan Esc
272. Klik `×` pada Bar Bulk

### Hak diubah menjadi Manage asset & TAG (Read + Delete) tidak menampilkan aksi transaksi
273. Admin mengubah hak `Budi Santoso {runId}` pada group `IT {runId}` menjadi `Manage asset & TAG` (Read + Delete)
274. Muat ulang halaman
275. Ketik Search `{runId}`, tekan Enter
276. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
277. Verifikasi aksi `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft` tidak dirender (Hidden)
278. Tekan Esc
279. Klik `⋯` pada baris `Proyektor Pinjam {runId} - 1`
280. Verifikasi aksi `Mark as Returned` dan `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
281. Tekan Esc
282. Klik `⋯` pada baris `Laptop Tugas {runId} - 1`
283. Verifikasi aksi `Mark as Unassigned` dan `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Assigned`
284. Tekan Esc
285. Centang baris `Laptop Pro 16 {runId} - 1`
286. Klik tombol Bulk Action
287. Verifikasi aksi Bulk `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft` tidak dirender (Hidden)
288. Tekan Esc
289. Klik `×` pada Bar Bulk
290. Centang baris `Proyektor Pinjam {runId} - 1`
291. Klik tombol Bulk Action
292. Verifikasi aksi Bulk `Mark as Returned` tidak dirender (Hidden) untuk aset berstatus `Borrowed`
293. Tekan Esc
294. Klik `×` pada Bar Bulk
295. Centang baris `Laptop Tugas {runId} - 1`
296. Klik tombol Bulk Action
297. Verifikasi aksi Bulk `Mark as Unassigned` tidak dirender (Hidden) untuk aset berstatus `Assigned`
298. Tekan Esc
299. Klik `×` pada Bar Bulk

### Hak diubah menjadi Manage asset & TAG (Read) tidak menampilkan aksi transaksi
300. Admin mengubah hak `Budi Santoso {runId}` pada group `IT {runId}` menjadi `Manage asset & TAG` (Read)
301. Muat ulang halaman
302. Ketik Search `{runId}`, tekan Enter
303. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
304. Verifikasi aksi `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft` tidak dirender (Hidden)
305. Tekan Esc
306. Klik `⋯` pada baris `Proyektor Pinjam {runId} - 1`
307. Verifikasi aksi `Mark as Returned` dan `Mark as Unassigned` tidak dirender (Hidden) pada aset berstatus `Borrowed`
308. Tekan Esc
309. Klik `⋯` pada baris `Laptop Tugas {runId} - 1`
310. Verifikasi aksi `Mark as Unassigned` dan `Mark as Returned` tidak dirender (Hidden) pada aset berstatus `Assigned`
311. Tekan Esc
312. Centang baris `Laptop Pro 16 {runId} - 1`
313. Klik tombol Bulk Action
314. Verifikasi aksi Bulk `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft` tidak dirender (Hidden)
315. Tekan Esc
316. Klik `×` pada Bar Bulk
317. Centang baris `Proyektor Pinjam {runId} - 1`
318. Klik tombol Bulk Action
319. Verifikasi aksi Bulk `Mark as Returned` tidak dirender (Hidden) untuk aset berstatus `Borrowed`
320. Tekan Esc
321. Klik `×` pada Bar Bulk
322. Centang baris `Laptop Tugas {runId} - 1`
323. Klik tombol Bulk Action
324. Verifikasi aksi Bulk `Mark as Unassigned` tidak dirender (Hidden) untuk aset berstatus `Assigned`
325. Tekan Esc
326. Klik `×` pada Bar Bulk

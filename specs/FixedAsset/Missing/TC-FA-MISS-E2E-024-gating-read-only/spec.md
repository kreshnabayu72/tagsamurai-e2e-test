---
id: TC-FA-MISS-E2E-024-gating-read-only
title: "Gating Read Only dan Manage asset & TAG (Read): tabel dan Missing Log tanpa aksi tulis, tanpa kolom finansial, Search dan Filter aktif"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#r12", "§4.8#r1", "§4.8#r2", "§4.8#r5", "§4.8#r6", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§9.11#r1", "§9.11#r2", "§9.11#b1", "§2.1#b8", "§4.8#b2", "§4.3#r5", "EB-AKS-4", "§2.1#b10"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [3, 8, 12, 77]
  "§2.1#r2": [45, 168]
  "§2.1#r5": [16, 81]
  "§2.1#r6": 22
  "§2.1#r7": [17, 82]
  "§2.1#r9": [18, 83]
  "§2.1#r10": 26
  "§2.1#r11": 30
  "§2.1#r12": [5, 6, 74, 75]
  "§4.8#r1": [1, 3]
  "§4.8#r2": [45, 168]
  "§4.8#r5": [16, 81]
  "§4.8#r6": [17, 22, 91, 125]
  "§4.8#r9": [18, 26]
  "§4.8#r10": [35, 39, 87, 138, 139, 140, 143, 151, 152, 153, 156]
  "§4.8#r11": 32
  "§4.8#r12": [30, 160, 162]
  "§9.11#r1": [8, 77]
  "§9.11#r2": [35, 118, 130]
  "§9.11#b1": [35, 39, 87]
  "§2.1#b8": [35, 39, 87, 138, 139, 140, 143, 151, 152, 153, 156]
  "§4.8#b2": 30
  "§4.3#r5": [35, 39, 87]
  "EB-AKS-4": [50, 51, 56, 57, 60, 63, 64, 66, 69, 94, 95, 100, 101, 104, 107, 108, 110, 113]
  "§2.1#b10": [74, 75, 81, 82, 83]
anchor: [15, 21, 25, 28, 34, 38, 43, 80, 86, 90, 117, 124, 129, 166]
coverage:
  web: automated
---

# Gating Read Only dan Manage asset & TAG (Read): tabel dan Missing Log tanpa aksi tulis, tanpa kolom finansial, Search dan Filter aktif

## Prerequisites
- Aktor: pemegang Read Only, cakupan seluruh client; lalu pemegang Manage asset & TAG dengan Read pada Group `Warehouse {runId}`. Keduanya tanpa `View asset value` dan tanpa capability tulis; lalu pemegang Read Only dengan cakupan seluruh client yang juga memegang `View asset value` pada Group `Head Office {runId}`, dan pemegang Manage asset & TAG dengan Read pada Group `Warehouse {runId}` yang juga memegang `View asset value` pada Group `Warehouse {runId}`.
- Layar awal: halaman Assets.
- Data:
  - DU-024-1: Missing record, Name `Laptop Dell Latitude 5420 {runId}`, Group `Finance Room {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`. Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.
  - DU-024-2: Missing record, Name `Hand Pallet Truck {runId}`, Group `Warehouse {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`. Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.
  - DU-024-3: Missing record, Name `Monitor LG 27UL500 {runId}`, Group `Head Office {runId}`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Sari Dewi {runId}` (pemegang aset tanpa hak Aktor Missing). Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.
  - DU-024-4: Missing record, Name `Projector Epson EB-X06 {runId}`, Group `Branch Surabaya {runId}`, Status `Reported Disposal`, Source `Audit`, Last Holder `—`. Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.
  - DU-024-5: Missing record, Name `Camera Canon EOS {runId}`, Group `Head Office {runId}`, Status `Found`, Source `Borrow`, Last Holder `—`. Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.
  - DU-024-6: Asset, Name `Scanner Zebra DS2208 {runId}`, Group `Finance Room {runId}`, Status `Available`, tanpa record Missing berjalan. Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.
  - DU-024-7: Missing record, Name `Tablet Samsung Galaxy Tab {runId}`, Group `Warehouse {runId}`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Sari Dewi {runId}` (pemegang aset tanpa hak Aktor Missing). Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.
  - DU-024-8: Asset, Name `Pallet Jack Crown PE {runId}`, Group `Warehouse {runId}`, Status `Available`, tanpa record Missing berjalan. Asset ID dan Increment aset dibentuk server dan menjadi milik entri ini.

## Test Steps

### Tab Missing dan sub-tab tampil untuk Read Only
1. Verifikasi tab `Missing` tampil pada halaman Assets
2. Klik tab `Missing`
3. Verifikasi sub-tab `Active` dan `History` tampil
4. Ketik Search `{runId}`, tekan Enter

### Cakupan seluruh client dan Missing Log Read Only
5. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` dengan Group `Finance Room {runId}` tampil
6. Verifikasi baris `Hand Pallet Truck {runId}` dengan Group `Warehouse {runId}` tampil
7. Klik nama `Laptop Dell Latitude 5420 {runId}`
8. Verifikasi dialog `Missing Log` untuk record `Laptop Dell Latitude 5420 {runId}` terbuka
9. Klik `✕` pada dialog Missing Log
10. Klik sub-tab `History`
11. Ketik Search `{runId}`, tekan Enter
12. Verifikasi baris `Camera Canon EOS {runId}` dengan Status `Found` tampil
13. Klik sub-tab `Active`

### Read Only: aksi tulis tidak tampil
14. Klik menu ⋯ pada baris `Laptop Dell Latitude 5420 {runId}`
15. Verifikasi aksi `Missing Log` tampil
16. Verifikasi aksi `Add Update` tidak tampil
17. Verifikasi aksi `Mark as Found` tidak tampil
18. Verifikasi aksi `Report Disposal` tidak tampil
19. Tekan `Esc`
20. Klik menu ⋯ pada baris `Monitor LG 27UL500 {runId}`
21. Verifikasi aksi `Missing Log` tampil
22. Verifikasi aksi `Review` tidak tampil
23. Tekan `Esc`
24. Klik menu ⋯ pada baris `Projector Epson EB-X06 {runId}`
25. Verifikasi aksi `Missing Log` tampil
26. Verifikasi aksi `Cancel Disposal Report` tidak tampil
27. Tekan `Esc`

### Read Only: Download tampil, Scan Found Asset tidak tampil
28. Verifikasi tombol `Download` tampil di toolbar tab Active
29. Klik `Download`
30. Verifikasi opsi `Download as CSV` dan `Download as XLSX` tampil
31. Tekan `Esc`
32. Verifikasi tombol `Scan Found Asset` tidak tampil di toolbar tab Active

### Read Only: kolom nilai finansial tidak tersedia
33. Klik tombol `Column Visibility` pada header tabel
34. Verifikasi kolom `Brand` tersedia pada daftar Column Visibility
35. Verifikasi daftar Column Visibility tidak memuat `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
36. Tekan `Esc`
37. Klik `Filter`
38. Verifikasi field `Brand` tampil di Filter Panel
39. Verifikasi Filter Panel tidak memuat field `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
40. Klik `Filter`

### Read Only: Report Missing tidak tampil dari daftar aset
41. Klik tab `Assets`
42. Ketik Search `{runId}`, tekan Enter
43. Verifikasi baris `Scanner Zebra DS2208 {runId}` tampil
44. Klik menu ⋯ pada baris `Scanner Zebra DS2208 {runId}`
45. Verifikasi aksi `Report Missing` tidak tampil
46. Tekan `Esc`
47. Klik tab `Missing`
48. Ketik Search `{runId}`, tekan Enter

### Read Only: Search aktif
49. Ketik Search `Hand Pallet Truck {runId}`, tekan Enter
50. Verifikasi baris `Hand Pallet Truck {runId}` tampil
51. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tidak tampil
52. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Read Only: Filter aktif
53. Klik `Filter`
54. Pilih `Waiting for Confirmation` pada field `Status`
55. Klik `Apply`
56. Verifikasi baris `Monitor LG 27UL500 {runId}` tampil
57. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tidak tampil
58. Klik `Clear Field`
59. Klik `Apply`
60. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil
61. Klik `Filter`

### Read Only: Sort, Pagination, dan Setup Column aktif
62. Klik header kolom `Name`
63. Verifikasi urutan baris dari atas `Hand Pallet Truck {runId}`, `Laptop Dell Latitude 5420 {runId}`, `Monitor LG 27UL500 {runId}`, `Projector Epson EB-X06 {runId}`, `Tablet Samsung Galaxy Tab {runId}`
64. Verifikasi Pagination tampil di bawah tabel
65. Ubah ukuran halaman menjadi `25`
66. Verifikasi ukuran halaman bernilai `25`
67. Klik tombol `Column Visibility` pada header tabel
68. Centang `Brand`
69. Verifikasi header kolom `Brand` tampil di tabel
70. Tekan `Esc`

### Manage asset & TAG (Read): cakupan Group Read dan Missing Log
71. Masuk sebagai pemegang Manage asset & TAG dengan Read pada Group `Warehouse {runId}`
72. Klik tab `Missing`
73. Ketik Search `{runId}`, tekan Enter
74. Verifikasi baris `Hand Pallet Truck {runId}` dengan Group `Warehouse {runId}` tampil
75. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` dengan Group `Finance Room {runId}` tidak tampil
76. Klik nama `Hand Pallet Truck {runId}`
77. Verifikasi dialog `Missing Log` untuk record `Hand Pallet Truck {runId}` terbuka
78. Klik `✕` pada dialog Missing Log

### Manage asset & TAG (Read): aksi tulis dan kolom finansial tidak tampil
79. Klik menu ⋯ pada baris `Hand Pallet Truck {runId}`
80. Verifikasi aksi `Missing Log` tampil
81. Verifikasi aksi `Add Update` tidak tampil
82. Verifikasi aksi `Mark as Found` tidak tampil
83. Verifikasi aksi `Report Disposal` tidak tampil
84. Tekan `Esc`
85. Klik tombol `Column Visibility` pada header tabel
86. Verifikasi kolom `Brand` tersedia pada daftar Column Visibility
87. Verifikasi daftar Column Visibility tidak memuat `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
88. Tekan `Esc`

### Manage asset & TAG (Read): footer Reject dan Confirm tidak tampil pada laporan pemegang
89. Klik nama `Tablet Samsung Galaxy Tab {runId}`
90. Verifikasi dialog `Missing Log` untuk record `Tablet Samsung Galaxy Tab {runId}` terbuka
91. Verifikasi tombol `[Reject]` dan `[Confirm]` tidak tampil pada footer dialog Missing Log
92. Klik `✕` pada dialog Missing Log

### Manage asset & TAG (Read): Search aktif
93. Ketik Search `Hand Pallet Truck {runId}`, tekan Enter
94. Verifikasi baris `Hand Pallet Truck {runId}` tampil
95. Verifikasi baris `Tablet Samsung Galaxy Tab {runId}` tidak tampil
96. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Manage asset & TAG (Read): Filter aktif
97. Klik `Filter`
98. Pilih `Waiting for Confirmation` pada field `Status`
99. Klik `Apply`
100. Verifikasi baris `Tablet Samsung Galaxy Tab {runId}` tampil
101. Verifikasi baris `Hand Pallet Truck {runId}` tidak tampil
102. Klik `Clear Field`
103. Klik `Apply`
104. Verifikasi baris `Hand Pallet Truck {runId}` tampil
105. Klik `Filter`

### Manage asset & TAG (Read): Sort, Pagination, dan Setup Column aktif
106. Klik header kolom `Name`
107. Verifikasi urutan baris dari atas `Hand Pallet Truck {runId}`, `Tablet Samsung Galaxy Tab {runId}`
108. Verifikasi Pagination tampil di bawah tabel
109. Ubah ukuran halaman menjadi `25`
110. Verifikasi ukuran halaman bernilai `25`
111. Klik tombol `Column Visibility` pada header tabel
112. Centang `Brand`
113. Verifikasi header kolom `Brand` tampil di tabel
114. Tekan `Esc`

### Manage asset & TAG (Read): kolom nilai finansial tab History tidak tersedia
115. Klik sub-tab `History`
116. Klik tombol `Column Visibility` pada header tabel
117. Verifikasi kolom `Brand` tersedia pada daftar Column Visibility
118. Verifikasi daftar Column Visibility tidak memuat `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
119. Tekan `Esc`

### Read Only: footer Reject dan Confirm tidak tampil pada laporan pemegang
120. Masuk sebagai pemegang Read Only dengan cakupan seluruh client
121. Klik tab `Missing`
122. Ketik Search `{runId}`, tekan Enter
123. Klik nama `Monitor LG 27UL500 {runId}`
124. Verifikasi dialog `Missing Log` untuk record `Monitor LG 27UL500 {runId}` terbuka
125. Verifikasi tombol `[Reject]` dan `[Confirm]` tidak tampil pada footer dialog Missing Log
126. Klik `✕` pada dialog Missing Log

### Read Only: kolom nilai finansial tab History tidak tersedia
127. Klik sub-tab `History`
128. Klik tombol `Column Visibility` pada header tabel
129. Verifikasi kolom `Brand` tersedia pada daftar Column Visibility
130. Verifikasi daftar Column Visibility tidak memuat `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
131. Tekan `Esc`

### Read Only yang juga memegang View asset value: kolom nilai finansial tersedia
132. Masuk sebagai pemegang Read Only dengan cakupan seluruh client yang juga memegang `View asset value` pada Group `Head Office {runId}`
133. Klik tab `Missing`
134. Klik tombol `Column Visibility` pada header tabel
135. Centang `Purchase Cost`
136. Centang `Asset Value (Commercial)`
137. Centang `Asset Value (Fiscal)`
138. Verifikasi header kolom `Purchase Cost` tampil di tabel
139. Verifikasi header kolom `Asset Value (Commercial)` tampil di tabel
140. Verifikasi header kolom `Asset Value (Fiscal)` tampil di tabel
141. Tekan `Esc`
142. Klik `Filter`
143. Verifikasi Filter Panel memuat field `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
144. Klik `Filter`

### Manage asset & TAG (Read) yang juga memegang View asset value: kolom nilai finansial tersedia
145. Masuk sebagai pemegang Manage asset & TAG dengan Read pada Group `Warehouse {runId}` yang juga memegang `View asset value` pada Group `Warehouse {runId}`
146. Klik tab `Missing`
147. Klik tombol `Column Visibility` pada header tabel
148. Centang `Purchase Cost`
149. Centang `Asset Value (Commercial)`
150. Centang `Asset Value (Fiscal)`
151. Verifikasi header kolom `Purchase Cost` tampil di tabel
152. Verifikasi header kolom `Asset Value (Commercial)` tampil di tabel
153. Verifikasi header kolom `Asset Value (Fiscal)` tampil di tabel
154. Tekan `Esc`
155. Klik `Filter`
156. Verifikasi Filter Panel memuat field `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)`
157. Klik `Filter`

### Manage asset & TAG (Read): Download tampil dan Report Missing tidak tampil
158. Masuk sebagai pemegang Manage asset & TAG dengan Read pada Group `Warehouse {runId}`
159. Klik tab `Missing`
160. Verifikasi tombol `Download` tampil di toolbar tab Active
161. Klik `Download`
162. Verifikasi opsi `Download as CSV` dan `Download as XLSX` tampil
163. Tekan `Esc`
164. Klik tab `Assets`
165. Ketik Search `{runId}`, tekan Enter
166. Verifikasi baris `Pallet Jack Crown PE {runId}` tampil
167. Klik menu ⋯ pada baris `Pallet Jack Crown PE {runId}`
168. Verifikasi aksi `Report Missing` tidak tampil
169. Tekan `Esc`

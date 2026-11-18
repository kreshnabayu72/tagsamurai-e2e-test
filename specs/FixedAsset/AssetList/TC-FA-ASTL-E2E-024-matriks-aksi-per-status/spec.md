---
id: TC-FA-ASTL-E2E-024-matriks-aksi-per-status
title: "Row Action dan Bulk Action menurut status aset"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-04a", "ASTL-LOGIC-16a", "ASTL-LOGIC-16b", "ASTL-LOGIC-16d", "ASTL-LOGIC-16g", "ASTL-LOGIC-17n", "ASTL-LOGIC-19a", "ASTL-LOGIC-19b", "ASTL-LOGIC-19c", "ASTL-LOGIC-19d", "ASTL-LOGIC-19e", "ASTL-LOGIC-20j", "EC-05", "EC-22", "EC-45", "EC-46", "F-ASTL-16.k1", "F-ASTL-17.k2", "MarkasReturned", "MarkasUnassigned", "AddLabel", "AddtoAssignmentDraft", "AddtoBorrowDraft", "AddtoTransferDraft", "Assign", "BatchReplaceTAG", "Borrow", "DeleteAssetData", "Detail", "Edit", "EditPurchase", "Manage", "PrintLabel", "RemoveLabel", "ReplaceTAG", "ReportDamage", "ReportDisposal", "ReportMissing", "ReportTAG", "Transfer"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-04a": [70, 73, 85]
  "ASTL-LOGIC-16a": 11
  "ASTL-LOGIC-16b": [10, 41]
  "ASTL-LOGIC-16d": [15, 40]
  "ASTL-LOGIC-16g": 12
  "ASTL-LOGIC-17n": [32, 34, 64, 66, 72, 84, 100, 102, 232, 239]
  "ASTL-LOGIC-19a": [31, 53, 77]
  "ASTL-LOGIC-19b": [32, 34, 52, 84, 100, 102, 103, 230, 232, 237, 239]
  "ASTL-LOGIC-19c": [32, 42, 47]
  "ASTL-LOGIC-19d": [35, 41]
  "ASTL-LOGIC-19e": 78
  "ASTL-LOGIC-20j": [6, 135, 140, 145]
  "EC-05": [73, 85]
  "EC-22": 32
  "EC-45": [19, 177, 179, 258]
  "EC-46": [27, 95]
  "F-ASTL-16.k1": 32
  "F-ASTL-17.k2": [32, 64]
  "AddLabel": [31, 40, 103]
  "AddtoAssignmentDraft": [3, 31, 87, 89, 92, 94, 100, 102]
  "AddtoBorrowDraft": [3, 31, 87, 89, 92, 94, 100, 102]
  "AddtoTransferDraft": [3, 31, 87, 89, 92, 94, 100, 102, 221, 225, 230, 232, 237, 239]
  "Assign": [3, 31, 87, 89, 92, 94, 100, 102, 140, 199, 216]
  "BatchReplaceTAG": [31, 129, 154, 159, 164]
  "Borrow": [3, 24, 31, 87, 89, 92, 94, 100, 102, 135, 199, 216]
  "DeleteAssetData": [4, 9, 58, 60, 72]
  "Detail": [3, 9]
  "Edit": [3, 24, 26, 92, 94, 125]
  "EditPurchase": [3, 27, 31, 95, 103]
  "Manage": [4, 9, 16, 42, 47, 107]
  "PrintLabel": [3, 27, 31, 95, 103]
  "RemoveLabel": [31, 40, 103]
  "ReplaceTAG": [3, 110, 113, 150]
  "ReportDamage": [3, 27, 95, 116, 122]
  "ReportDisposal": [3, 9, 21, 87, 89, 92, 94, 122, 125, 168, 171, 174, 181, 196]
  "ReportMissing": [3, 19, 27, 95, 116, 119, 177, 179, 194, 255, 258]
  "ReportTAG": 4
  "MarkasReturned": [182, 185, 189, 193, 200, 204, 211, 217, 244, 251]
  "MarkasUnassigned": [182, 186, 192, 200, 205, 210, 217, 245, 250]
  "Transfer": [3, 31, 87, 89, 92, 94, 100, 102, 145, 221, 225, 230, 232, 237, 239]
anchor: []
coverage:
  web: automated
---
# Row Action dan Bulk Action menurut status aset

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-024-1: aset Active managed Custody `Available` dengan TAG `Paired`, Asset Name `Laptop Pro 16 {runId}`, tampil `Laptop Pro 16 {runId} - 1`, Brand `Lenovo`, Model/Type `ThinkPad T14`, Category `Peralatan IT`, Group `Kantor Pusat {runId}`, Status `Available`.
  - DU-024-2: aset Active managed Custody `Available` dengan TAG `Paired`, Asset Name `Laptop Pro 14 {runId}`, tampil `Laptop Pro 14 {runId} - 1`, Brand `Lenovo`, Model/Type `ThinkPad T14`, Category `Peralatan IT`, Group `Kantor Pusat {runId}`, Status `Available`.
  - DU-024-3: aset Active Unmanaged Custody `Available`, Asset Name `Kamera Mirrorless {runId}`, tampil `Kamera Mirrorless {runId} - 1`, Brand `Sony`, Model/Type `A6400`, Category `Peralatan Foto`, Group `Kantor Pusat {runId}`, Status `Available, Unmanaged`.
  - DU-024-4: aset Active `Pending Activation`, Asset Name `Scanner Gudang {runId}`, tampil `Scanner Gudang {runId} - 1`, Brand `Zebra`, Model/Type `DS2208`, Category `Peralatan Gudang`, Group `Kantor Pusat {runId}`, Status `Pending Activation`.
  - DU-024-5: aset Disposed tanpa blokir, Asset Name `Genset 20kVA {runId}`, tampil `Genset 20kVA {runId} - 1`, Brand `Perkins`, Model/Type `403A-15G2`, Category `Peralatan Listrik`, Group `Kantor Pusat {runId}`, Status `Disposed`.
  - DU-024-6: aset Disposed tanpa blokir, Asset Name `Lemari Besi {runId}`, tampil `Lemari Besi {runId} - 1`, Brand `Brother`, Model/Type `LB-4`, Category `Furniture`, Group `Kantor Pusat {runId}`, Status `Disposed`.
  - DU-024-7: aset Active managed Custody `Borrowed`, Asset Name `Mobil Operasional {runId}`, tampil `Mobil Operasional {runId} - 1`, Brand `Toyota`, Model/Type `Avanza`, Category `Kendaraan`, Group `Kantor Pusat {runId}`, Status `Borrowed`.
  - DU-024-8: aset Active managed Custody `Available` dengan TAG `Paired` dan Activity Lock `In Audit`, Asset Name `Server Rack {runId}`, tampil `Server Rack {runId} - 1`, Brand `Rittal`, Model/Type `TS8`, Category `Peralatan IT`, Group `Kantor Pusat {runId}`, Status `Available, In Audit`.
  - DU-024-9: aset Disposed dengan penyusutan Posted, Asset Name `Mesin Fotokopi {runId}`, tampil `Mesin Fotokopi {runId} - 1`, Brand `Ricoh`, Model/Type `IM 2702`, Category `Peralatan Kantor`, Group `Kantor Pusat {runId}`, Status `Disposed`.
  - DU-024-10: aset Active Unmanaged Custody `Available` pada group lain, Asset Name `Tablet Inventaris {runId}`, tampil `Tablet Inventaris {runId} - 1`, Brand `Samsung`, Model/Type `Tab A8`, Category `Peralatan IT`, Group `Cabang Bandung {runId}`, Status `Available, Unmanaged`.
  - DU-024-11: Group `Kantor Pusat {runId}`.
  - DU-024-12: Group `Cabang Bandung {runId}`.
  - DU-024-13: aset Active managed Custody `Available` dengan Activity Lock `Under Maintenance`, Asset Name `Mesin CNC {runId}`, tampil `Mesin CNC {runId} - 1`, Brand `Haas`, Model/Type `VF-2`, Category `Peralatan Produksi`, Group `Kantor Pusat {runId}`, Status `Available, Under Maintenance`.
  - DU-024-14: aset Active Unmanaged Custody `Available` dengan Activity Lock `In Audit`, Asset Name `Radio Panggil {runId}`, tampil `Radio Panggil {runId} - 1`, Brand `Motorola`, Model/Type `T82`, Category `Peralatan Komunikasi`, Group `Kantor Pusat {runId}`, Status `Available, Unmanaged, In Audit`.
  - DU-024-15: aset Active managed Custody `Available` dengan TAG `Not Paired Yet`, Asset Name `Meja Lipat {runId}`, tampil `Meja Lipat {runId} - 1`, Brand `Informa`, Model/Type `ML-2`, Category `Furniture`, Group `Kantor Pusat {runId}`, Status `Available`.
  - DU-024-16: aset Active managed Custody `Available` dengan Condition `Damaged` dan record berstatus `Damaged`, Asset Name `Kompresor Rusak {runId}`, tampil `Kompresor Rusak {runId} - 1`, Brand `Atlas Copco`, Model/Type `GX 2`, Category `Peralatan Industri`, Group `Kantor Pusat {runId}`, Status `Available, Damaged`.
  - DU-024-17: aset Active managed Custody `Available` dengan Condition `Missing` dan record berstatus `Missing`, Asset Name `Proyektor Hilang {runId}`, tampil `Proyektor Hilang {runId} - 1`, Brand `Epson`, Model/Type `EB-X06`, Category `Peralatan Presentasi`, Group `Kantor Pusat {runId}`, Status `Available, Missing`.
  - DU-024-18: aset Active managed dengan TAG `Paired` yang `In Disposal Process`, Asset Name `Truk Boks {runId}`, tampil `Truk Boks {runId} - 1`, Brand `Hino`, Model/Type `Dutro 130`, Category `Kendaraan`, Group `Kantor Pusat {runId}`, Status `In Disposal Process`.
  - DU-024-19: aset Active managed Custody `Assigned`, Asset Name `Handy Talkie Satpam {runId}`, tampil `Handy Talkie Satpam {runId} - 1`, Brand `Icom`, Model/Type `IC-V86`, Category `Peralatan Komunikasi`, Group `Kantor Pusat {runId}`, Status `Assigned`.
  - DU-024-20: aset Active managed Custody `Borrowed` dengan peminjaman `Overdue`, Asset Name `Forklift Gudang {runId}`, tampil `Forklift Gudang {runId} - 1`, Brand `Toyota`, Model/Type `8FD`, Category `Kendaraan`, Group `Kantor Pusat {runId}`, Status `Borrowed`.
  - DU-024-21: aset Active managed Custody `In Transfer Process` dengan baris Transfer berstatus `In Transit`, Asset Name `Genset Portabel {runId}`, tampil `Genset Portabel {runId} - 1`, Brand `Honda`, Model/Type `EU22i`, Category `Peralatan Listrik`, Group `Kantor Pusat {runId}`, Status `In Transfer Process`.
  - DU-024-22: aset Active managed Custody `Available` dengan Tagging `TAG Reported`, Asset Name `Printer Label {runId}`, tampil `Printer Label {runId} - 1`, Brand `Zebra`, Model/Type `ZD421`, Category `Peralatan Kantor`, Group `Kantor Pusat {runId}`, Status `Available, TAG Reported`.
  - DU-024-23: aset Active managed Custody `In Transfer Process` dengan baris Transfer yang belum `In Transit`, Asset Name `Trafo Distribusi {runId}`, tampil `Trafo Distribusi {runId} - 1`, Brand `Schneider`, Model/Type `Trihal 400`, Category `Peralatan Listrik`, Group `Kantor Pusat {runId}`, Status `In Transfer Process`.

## Test Steps

### Menu aksi baris aset managed Available
1. Ketik Search `{runId}`, tekan Enter
2. Klik menu `⋯` pada baris `Laptop Pro 16 {runId} - 1`
3. Verifikasi menu aksi memuat `Detail`, `Print Label`, `Edit`, `Edit Purchase`, `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft`, `Report Disposal`, `Replace TAG`, `Report Damage`, `Report Missing` dan tidak satu pun `Disabled`
4. Verifikasi menu aksi tidak memuat `Manage`, `Delete Asset Data`, `Report TAG` untuk aset managed yang belum `Disposed`
5. Pilih `Borrow`
6. Verifikasi form transaksi peminjaman terbuka berisi aset `Laptop Pro 16 {runId} - 1`
7. Kembali ke daftar All Assets

### Menu aksi baris aset Unmanaged
8. Klik menu `⋯` pada baris `Kamera Mirrorless {runId} - 1`
9. Verifikasi menu aksi memuat `Detail`, `Manage`, `Report Disposal`, `Delete Asset Data` dan tidak satu pun `Disabled`
10. Verifikasi menu aksi tidak memuat `Print Label`, `Edit`, `Edit Purchase`, `Replace TAG`, `Report TAG` untuk aset Unmanaged
11. Verifikasi menu aksi tidak memuat `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft` untuk aset Unmanaged
12. Verifikasi menu aksi tidak memuat `Report Damage`, `Report Missing` untuk aset Unmanaged
13. Tutup menu aksi baris dengan `Esc`

### Menu aksi baris aset Pending Activation
14. Klik menu `⋯` pada baris `Scanner Gudang {runId} - 1`
15. Verifikasi menu aksi hanya memuat `Detail`, `Report Disposal`, `Delete Asset Data`
16. Verifikasi menu aksi tidak memuat `Manage` karena aset sudah `Pending Activation`
17. Tutup menu aksi baris dengan `Esc`

### Report Missing aktif dan Report Disposal Disabled pada aset Borrowed
18. Klik menu `⋯` pada baris `Mobil Operasional {runId} - 1`
19. Verifikasi `Report Missing` tampil dan tidak `Disabled` walau Custody aset `Borrowed`
20. Arahkan pointer ke `Report Disposal`
21. Verifikasi `Report Disposal` tampil `Disabled` dengan tooltip `This asset is in borrow process.` tampil
22. Tutup menu aksi baris dengan `Esc`

### Aset terkunci Activity Lock In Audit
23. Klik menu `⋯` pada baris `Server Rack {runId} - 1`
24. Verifikasi `Edit` dan `Borrow` tampil `Disabled`
25. Arahkan pointer ke `Edit`
26. Verifikasi tooltip `Asset is in audit. Complete or cancel the audit to continue.` tampil
27. Verifikasi `Print Label`, `Edit Purchase`, `Report Damage`, `Report Missing` tidak `Disabled` walau aset `In Audit`
28. Tutup menu aksi baris dengan `Esc`

### Bulk Action pada seleksi aset managed Available
29. Centang baris `Laptop Pro 16 {runId} - 1` dan baris `Laptop Pro 14 {runId} - 1`
30. Klik `Bulk Action`
31. Verifikasi Bulk Action memuat `Print Label`, `Edit Purchase`, `Add Label`, `Remove Label`, `Batch Replace TAG`, `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft` dan tidak satu pun `Disabled` karena seluruh aset terpilih memenuhi syarat
32. Verifikasi `Delete Asset Data` dan `Manage` tampil `Disabled` karena tidak ada aset terpilih yang `Disposed` maupun Unmanaged
33. Arahkan pointer ke `Delete Asset Data`
34. Verifikasi tooltip `Some selected assets are not eligible for this action. Check the Status column for the cause.` tampil
35. Verifikasi Bulk Action tidak memuat `Edit`, `Replace TAG`, `Report Damage`, `Report Missing`, `Report Disposal`, `Report TAG`, `Detail`
36. Tutup menu Bulk Action dengan `Esc`
37. Klik `×` pada Bar Bulk

### Bulk Action pada seleksi Unmanaged dan Pending Activation
38. Centang baris `Kamera Mirrorless {runId} - 1` dan baris `Scanner Gudang {runId} - 1`
39. Klik `Bulk Action`
40. Verifikasi Bulk Action memuat `Add Label` dan `Remove Label` yang tidak `Disabled`
41. Verifikasi Bulk Action tidak memuat `Print Label` maupun `Edit Purchase` karena ada aset Unmanaged
42. Verifikasi `Manage` tampil `Disabled` karena salah satu aset sudah `Pending Activation`
43. Tutup menu Bulk Action dengan `Esc`
44. Klik `×` pada Bar Bulk

### Bulk Manage pada seleksi lintas group
45. Centang baris `Scanner Gudang {runId} - 1` dan baris `Tablet Inventaris {runId} - 1`
46. Klik `Bulk Action`
47. Verifikasi `Manage` tampil `Disabled` karena seleksi berasal dari dua group dan salah satu aset sudah `Pending Activation`
48. Tutup menu Bulk Action dengan `Esc`
49. Klik `×` pada Bar Bulk

### Bulk Action pada seleksi dengan aset terkunci
50. Centang baris `Laptop Pro 16 {runId} - 1` dan baris `Server Rack {runId} - 1`
51. Klik `Bulk Action`
52. Verifikasi `Borrow` tampil `Disabled` karena salah satu aset terkunci Activity Lock
53. Verifikasi `Print Label` dan `Add Label` tidak `Disabled` karena aksi itu tidak dibatasi Activity Lock
54. Tutup menu Bulk Action dengan `Esc`
55. Klik `×` pada Bar Bulk

### Delete Asset Data diblok pada satu aset Disposed
56. Klik kartu `Disposed`
57. Klik menu `⋯` pada baris `Mesin Fotokopi {runId} - 1`
58. Verifikasi `Delete Asset Data` tampil `Disabled` karena aset punya penyusutan Posted
59. Arahkan pointer ke `Delete Asset Data`
60. Verifikasi tooltip `Asset has posted depreciation or journal entries. Use Disposal.` tampil
61. Tutup menu aksi baris dengan `Esc`
62. Centang baris `Mesin Fotokopi {runId} - 1`
63. Klik `Bulk Action`
64. Verifikasi `Delete Asset Data` tampil `Disabled` pada Bulk Action
65. Arahkan pointer ke `Delete Asset Data`
66. Verifikasi tooltip `Some selected assets are not eligible for this action. Check the Status column for the cause.` tampil pada Bulk Action, berbeda dari tooltip Row Action
67. Tutup menu Bulk Action dengan `Esc`
68. Klik `×` pada Bar Bulk

### Seleksi aset Disposed
69. Centang baris `Genset 20kVA {runId} - 1`
70. Verifikasi checkbox baris `Genset 20kVA {runId} - 1` aktif dan Bar Bulk menampilkan `1 asset selected`
71. Klik `Bulk Action`
72. Verifikasi `Delete Asset Data` tersedia pada Bulk Action dan tidak `Disabled`
73. Verifikasi Bulk Action tidak memuat `Print Label`, `Add Label`, `Remove Label`, `Edit Purchase` karena aset terpilih `Disposed`
74. Tutup menu Bulk Action dengan `Esc`
75. Centang baris `Lemari Besi {runId} - 1`
76. Klik `Bulk Action`
77. Verifikasi `Delete Asset Data` tetap tersedia dan tidak `Disabled` untuk dua aset `Disposed`
78. Verifikasi Bar Bulk menampilkan `2 assets selected` tanpa penyaringan aset dan tanpa ringkasan aset yang dilewati
79. Tutup menu Bulk Action dengan `Esc`
80. Klik `×` pada Bar Bulk
81. Klik kartu `All`
82. Centang baris `Laptop Pro 16 {runId} - 1`, baris `Genset 20kVA {runId} - 1`, dan baris `Lemari Besi {runId} - 1`
83. Klik `Bulk Action`
84. Verifikasi `Delete Asset Data` tampil `Disabled` karena ada aset yang bukan `Disposed` dalam seleksi
85. Verifikasi Bulk Action tidak memuat `Print Label`, `Add Label`, `Remove Label`, `Edit Purchase` karena seleksi memuat aset `Disposed`

### Row Action pada aset terkunci Activity Lock
86. Klik menu `⋯` pada baris `Server Rack {runId} - 1`
87. Verifikasi `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft`, dan `Report Disposal` tampil `Disabled` karena aset `In Audit`
88. Arahkan pointer ke `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft`, dan `Report Disposal` satu per satu
89. Verifikasi tooltip `Asset is in audit. Complete or cancel the audit to continue.` tampil pada masing-masing aksi
90. Tutup menu aksi baris dengan `Esc`
91. Klik menu `⋯` pada baris `Mesin CNC {runId} - 1`
92. Verifikasi `Edit`, `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft`, dan `Report Disposal` tampil `Disabled` karena aset `Under Maintenance`
93. Arahkan pointer ke `Edit`, `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, `Add to Transfer Draft`, dan `Report Disposal` satu per satu
94. Verifikasi tooltip `Asset is under maintenance. Complete the maintenance task to continue.` tampil pada masing-masing aksi
95. Verifikasi `Print Label`, `Edit Purchase`, `Report Damage`, `Report Missing` tidak `Disabled` walau aset `Under Maintenance`
96. Tutup menu aksi baris dengan `Esc`

### Bulk Action pada seleksi terkunci memakai tooltip S-32
97. Klik `×` pada Bar Bulk
98. Centang baris `Server Rack {runId} - 1` dan baris `Mesin CNC {runId} - 1`
99. Klik `Bulk Action`
100. Verifikasi `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, dan `Add to Transfer Draft` tampil `Disabled` karena seleksi memuat aset terkunci
101. Arahkan pointer ke `Borrow`, `Add to Borrow Draft`, `Assign`, `Add to Assignment Draft`, `Transfer`, dan `Add to Transfer Draft` satu per satu
102. Verifikasi tooltip `Some selected assets are not eligible for this action. Check the Status column for the cause.` tampil pada masing-masing aksi, bukan tooltip Row Action
103. Verifikasi `Print Label`, `Add Label`, `Remove Label`, `Edit Purchase` tidak `Disabled`
104. Tutup menu Bulk Action dengan `Esc`
105. Klik `×` pada Bar Bulk

### Manage tidak dibatasi Activity Lock
106. Klik menu `⋯` pada baris `Radio Panggil {runId} - 1`
107. Verifikasi `Manage` tersedia dan tidak `Disabled` walau aset Unmanaged terkunci `In Audit`
108. Tutup menu aksi baris dengan `Esc`

### Syarat aksi menurut TAG, Condition, dan Custody
109. Klik menu `⋯` pada baris `Meja Lipat {runId} - 1`
110. Verifikasi menu aksi memuat `Report Damage` dan `Report Missing` tetapi tidak memuat `Replace TAG` karena aset tidak punya TAG `Paired`
111. Tutup menu aksi baris dengan `Esc`
112. Klik menu `⋯` pada baris `Truk Boks {runId} - 1`
113. Verifikasi menu aksi tidak memuat `Replace TAG` karena aset `In Disposal Process`
114. Tutup menu aksi baris dengan `Esc`
115. Klik menu `⋯` pada baris `Kompresor Rusak {runId} - 1`
116. Verifikasi menu aksi memuat `Report Missing` dan tidak memuat `Report Damage` karena Condition aset bukan `Normal`
117. Tutup menu aksi baris dengan `Esc`
118. Klik menu `⋯` pada baris `Proyektor Hilang {runId} - 1`
119. Verifikasi menu aksi tidak memuat `Report Missing` dan `Report Damage` karena Condition aset `Missing`
120. Tutup menu aksi baris dengan `Esc`
121. Klik menu `⋯` pada baris `Mobil Operasional {runId} - 1`
122. Verifikasi menu aksi memuat `Report Damage` walau Custody aset `Borrowed`, dan memuat `Report Disposal` yang tampil `Disabled`
123. Tutup menu aksi baris dengan `Esc`
124. Klik menu `⋯` pada baris `Genset 20kVA {runId} - 1`
125. Verifikasi menu aksi hanya memuat `Detail` dan `Delete Asset Data`, tanpa `Edit` maupun `Report Disposal`, karena aset `Disposed`
126. Tutup menu aksi baris dengan `Esc`
127. Centang baris `Laptop Pro 16 {runId} - 1` dan baris `Meja Lipat {runId} - 1`
128. Klik `Bulk Action`
129. Verifikasi Bulk Action tidak memuat `Batch Replace TAG` karena `Meja Lipat {runId} - 1` tidak punya TAG `Paired`
130. Tutup menu Bulk Action dengan `Esc`
131. Klik `×` pada Bar Bulk

### Bulk transaksi membuka form berisi seluruh aset terpilih
132. Centang baris `Laptop Pro 16 {runId} - 1` dan baris `Laptop Pro 14 {runId} - 1`
133. Klik `Bulk Action`
134. Pilih `Borrow`
135. Verifikasi form transaksi peminjaman terbuka berisi aset `Laptop Pro 16 {runId} - 1` dan `Laptop Pro 14 {runId} - 1`
136. Kembali ke daftar All Assets
137. Centang baris `Laptop Pro 16 {runId} - 1` dan baris `Laptop Pro 14 {runId} - 1`
138. Klik `Bulk Action`
139. Pilih `Assign`
140. Verifikasi form penugasan aset terbuka berisi aset `Laptop Pro 16 {runId} - 1` dan `Laptop Pro 14 {runId} - 1`
141. Kembali ke daftar All Assets
142. Centang baris `Laptop Pro 16 {runId} - 1` dan baris `Laptop Pro 14 {runId} - 1`
143. Klik `Bulk Action`
144. Pilih `Transfer`
145. Verifikasi form transfer terbuka berisi aset `Laptop Pro 16 {runId} - 1` dan `Laptop Pro 14 {runId} - 1`
146. Kembali ke daftar All Assets

### Replace TAG dan Batch Replace TAG tidak dibatasi Activity Lock
147. Muat ulang halaman
148. Ketik Search `{runId}`, tekan Enter
149. Klik menu `⋯` pada baris `Server Rack {runId} - 1`
150. Verifikasi `Replace TAG` tersedia dan tidak `Disabled` walau aset TAG `Paired` terkunci `In Audit`
151. Tutup menu aksi baris dengan `Esc`
152. Centang baris `Server Rack {runId} - 1` dan baris `Laptop Pro 14 {runId} - 1`
153. Klik `Bulk Action`
154. Verifikasi `Batch Replace TAG` tersedia dan tidak `Disabled` walau seleksi memuat aset TAG `Paired` terkunci `In Audit`
155. Tutup menu Bulk Action dengan `Esc`
156. Klik `×` pada Bar Bulk

### Batch Replace TAG butuh seluruh aset terpilih memenuhi syarat Replace TAG
157. Centang baris `Laptop Pro 16 {runId} - 1` dan baris `Kamera Mirrorless {runId} - 1`
158. Klik `Bulk Action`
159. Verifikasi Bulk Action tidak memuat `Batch Replace TAG` karena `Kamera Mirrorless {runId} - 1` Unmanaged
160. Tutup menu Bulk Action dengan `Esc`
161. Klik `×` pada Bar Bulk
162. Centang baris `Laptop Pro 16 {runId} - 1` dan baris `Genset 20kVA {runId} - 1`
163. Klik `Bulk Action`
164. Verifikasi Bulk Action tidak memuat `Batch Replace TAG` karena `Genset 20kVA {runId} - 1` `Disposed`
165. Tutup menu Bulk Action dengan `Esc`
166. Klik `×` pada Bar Bulk

### Syarat Report Disposal pada Row Action
167. Klik menu `⋯` pada baris `Truk Boks {runId} - 1`
168. Verifikasi menu aksi tidak memuat `Report Disposal` karena aset `In Disposal Process`
169. Tutup menu aksi baris dengan `Esc`
170. Klik menu `⋯` pada baris `Kompresor Rusak {runId} - 1`
171. Verifikasi menu aksi memuat `Report Disposal` dan tidak `Disabled` untuk aset Condition `Damaged` bagi Total Control
172. Tutup menu aksi baris dengan `Esc`
173. Klik menu `⋯` pada baris `Proyektor Hilang {runId} - 1`
174. Verifikasi menu aksi memuat `Report Disposal` dan tidak `Disabled` untuk aset Condition `Missing` bagi Total Control
175. Tutup menu aksi baris dengan `Esc`

### Report Missing dan Report Disposal pada aset Transfer In Transit
176. Klik menu `⋯` pada baris `Genset Portabel {runId} - 1`
177. Verifikasi `Report Missing` tampil `Disabled` dan tidak disembunyikan karena aset berstatus `In Transit`
178. Arahkan pointer ke `Report Missing`
179. Verifikasi tooltip `This asset is in transfer. Report it missing from Transfer.` tampil
180. Arahkan pointer ke `Report Disposal`
181. Verifikasi `Report Disposal` tampil `Disabled` dengan tooltip `This asset is in transfer.` tampil karena Custody aset `In Transfer Process`
182. Verifikasi menu aksi tidak memuat `Mark as Returned` maupun `Mark as Unassigned` karena Custody aset bukan `Borrowed` maupun `Assigned`
183. Tutup menu aksi baris dengan `Esc`

### Mark as Returned dan Mark as Unassigned pada Row Action
184. Klik menu `⋯` pada baris `Mobil Operasional {runId} - 1`
185. Verifikasi menu aksi memuat `Mark as Returned` karena Custody aset `Borrowed`
186. Verifikasi menu aksi tidak memuat `Mark as Unassigned` karena Custody aset bukan `Assigned`
187. Tutup menu aksi baris dengan `Esc`
188. Klik menu `⋯` pada baris `Forklift Gudang {runId} - 1`
189. Verifikasi menu aksi memuat `Mark as Returned` walau peminjaman aset `Overdue`
190. Tutup menu aksi baris dengan `Esc`
191. Klik menu `⋯` pada baris `Handy Talkie Satpam {runId} - 1`
192. Verifikasi menu aksi memuat `Mark as Unassigned` karena Custody aset `Assigned`
193. Verifikasi menu aksi tidak memuat `Mark as Returned` karena Custody aset bukan `Borrowed`
194. Verifikasi `Report Missing` tampil dan tidak `Disabled` walau Custody aset `Assigned`
195. Arahkan pointer ke `Report Disposal`
196. Verifikasi `Report Disposal` tampil `Disabled` dengan tooltip `This asset is in assignment process.` tampil
197. Tutup menu aksi baris dengan `Esc`
198. Klik menu `⋯` pada baris `Laptop Pro 16 {runId} - 1`
199. Verifikasi menu aksi memuat `Borrow` dan `Assign`
200. Verifikasi menu aksi tidak memuat `Mark as Returned` maupun `Mark as Unassigned` karena Custody aset `Available`
201. Tutup menu aksi baris dengan `Esc`

### Mark as Returned dan Mark as Unassigned pada Bulk Action
202. Centang baris `Mobil Operasional {runId} - 1` dan baris `Forklift Gudang {runId} - 1`
203. Klik `Bulk Action`
204. Verifikasi Bulk Action memuat `Mark as Returned` karena seluruh aset terpilih Custody `Borrowed`
205. Verifikasi Bulk Action tidak memuat `Mark as Unassigned` karena tidak ada aset terpilih Custody `Assigned`
206. Tutup menu Bulk Action dengan `Esc`
207. Klik `×` pada Bar Bulk
208. Centang baris `Handy Talkie Satpam {runId} - 1`
209. Klik `Bulk Action`
210. Verifikasi Bulk Action memuat `Mark as Unassigned` karena aset terpilih Custody `Assigned`
211. Verifikasi Bulk Action tidak memuat `Mark as Returned` karena tidak ada aset terpilih Custody `Borrowed`
212. Tutup menu Bulk Action dengan `Esc`
213. Klik `×` pada Bar Bulk
214. Centang baris `Laptop Pro 16 {runId} - 1` dan baris `Laptop Pro 14 {runId} - 1`
215. Klik `Bulk Action`
216. Verifikasi Bulk Action memuat `Borrow` dan `Assign`
217. Verifikasi Bulk Action tidak memuat `Mark as Returned` maupun `Mark as Unassigned` karena seluruh aset terpilih Custody `Available`
218. Tutup menu Bulk Action dengan `Esc`
219. Klik `×` pada Bar Bulk

### Transfer dan Add to Transfer Draft untuk aset Condition Damaged
220. Klik menu `⋯` pada baris `Kompresor Rusak {runId} - 1`
221. Verifikasi `Transfer` dan `Add to Transfer Draft` tampil dan tidak `Disabled` walau Condition aset `Damaged`
222. Tutup menu aksi baris dengan `Esc`
223. Centang baris `Kompresor Rusak {runId} - 1` dan baris `Laptop Pro 14 {runId} - 1`
224. Klik `Bulk Action`
225. Verifikasi `Transfer` dan `Add to Transfer Draft` pada Bulk Action tidak `Disabled` walau seleksi memuat aset Condition `Damaged`
226. Tutup menu Bulk Action dengan `Esc`
227. Klik `×` pada Bar Bulk

### Bulk Transfer dan Add to Transfer Draft pada seleksi Unmanaged, Pending Activation, dan Disposed
228. Centang baris `Kamera Mirrorless {runId} - 1` dan baris `Scanner Gudang {runId} - 1`
229. Klik `Bulk Action`
230. Verifikasi `Transfer` dan `Add to Transfer Draft` tampil `Disabled` karena seleksi memuat aset Unmanaged dan aset `Pending Activation`
231. Arahkan pointer ke `Transfer` dan `Add to Transfer Draft` satu per satu
232. Verifikasi tooltip `Some selected assets are not eligible for this action. Check the Status column for the cause.` tampil pada masing-masing aksi
233. Tutup menu Bulk Action dengan `Esc`
234. Klik `×` pada Bar Bulk
235. Centang baris `Laptop Pro 16 {runId} - 1` dan baris `Genset 20kVA {runId} - 1`
236. Klik `Bulk Action`
237. Verifikasi `Transfer` dan `Add to Transfer Draft` tampil `Disabled` karena seleksi memuat aset `Disposed`
238. Arahkan pointer ke `Transfer` dan `Add to Transfer Draft` satu per satu
239. Verifikasi tooltip `Some selected assets are not eligible for this action. Check the Status column for the cause.` tampil pada masing-masing aksi
240. Tutup menu Bulk Action dengan `Esc`
241. Klik `×` pada Bar Bulk

### Mark as Returned dan Mark as Unassigned pada seleksi campuran
242. Centang baris `Mobil Operasional {runId} - 1` dan baris `Laptop Pro 16 {runId} - 1`
243. Klik `Bulk Action`
244. Verifikasi Bulk Action memuat `Mark as Returned` walau salah satu aset terpilih bukan `Borrowed` (Custody `Available`)
245. Verifikasi Bulk Action tidak memuat `Mark as Unassigned` karena tidak ada aset terpilih Custody `Assigned`
246. Tutup menu Bulk Action dengan `Esc`
247. Klik `×` pada Bar Bulk
248. Centang baris `Handy Talkie Satpam {runId} - 1` dan baris `Laptop Pro 16 {runId} - 1`
249. Klik `Bulk Action`
250. Verifikasi Bulk Action memuat `Mark as Unassigned` walau salah satu aset terpilih bukan `Assigned` (Custody `Available`)
251. Verifikasi Bulk Action tidak memuat `Mark as Returned` karena tidak ada aset terpilih Custody `Borrowed`
252. Tutup menu Bulk Action dengan `Esc`
253. Klik `×` pada Bar Bulk

### Report Missing pada aset TAG Reported dan aset Transfer yang belum In Transit
254. Klik menu `⋯` pada baris `Printer Label {runId} - 1`
255. Verifikasi menu aksi memuat `Report Missing` yang tidak `Disabled` walau Tagging aset `TAG Reported`
256. Tutup menu aksi baris dengan `Esc`
257. Klik menu `⋯` pada baris `Trafo Distribusi {runId} - 1`
258. Verifikasi menu aksi memuat `Report Missing` yang tidak `Disabled` walau Custody aset `In Transfer Process`, karena aset belum berstatus `In Transit`
259. Tutup menu aksi baris dengan `Esc`

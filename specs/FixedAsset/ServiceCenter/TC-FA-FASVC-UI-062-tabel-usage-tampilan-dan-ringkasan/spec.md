---
id: TC-FA-FASVC-UI-062-tabel-usage-tampilan-dan-ringkasan
title: "Tab Usage: Kolom, Nilai Kosong, Ringkasan Teks, Persentase, dan State Kosong atau Gagal"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["T-FASVC-02", "S-FASVC-17", "S-FASVC-18", "EB-TBL-1@tabel-usage", "EB-TBL-2@kolom-brand-usage", "EB-TBL-2@kolom-model-type-usage", "EB-TBL-2@kolom-schedule-usage", "EB-TBL-2@kolom-result-usage", "EB-TBL-2@kolom-finished-at-usage", "EB-TBL-2@kolom-recorded-by-usage", "EB-TBL-2@kolom-cost-usage", "EB-TBL-4@recorded-by-usage", "EC-FASVC-40"]
smoke: []
dependsOn: []
trace:
  "T-FASVC-02": [2, 3, 4, 7, 9, 10, 11, 14, 15, 16, 19, 20, 21, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 49, 51, 53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 97, 99, 100, 101, 102, 104, 105, 106, 128, 130, 133, 136, 139, 140, 142, 143, 144, 145, 146, 147, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174]
  "S-FASVC-17": [112, 113, 118, 119]
  "S-FASVC-18": [121, 122, 125]
  "EB-TBL-1@tabel-usage": [108, 109, 110, 112, 113, 114, 121, 122, 123]
  "EB-TBL-2@kolom-brand-usage": [83]
  "EB-TBL-2@kolom-model-type-usage": [84]
  "EB-TBL-2@kolom-schedule-usage": [77]
  "EB-TBL-2@kolom-result-usage": [44, 55, 62, 68, 78]
  "EB-TBL-2@kolom-finished-at-usage": [61, 67, 79]
  "EB-TBL-2@kolom-recorded-by-usage": [60, 66, 72, 80, 145, 147]
  "EB-TBL-2@kolom-cost-usage": [63, 69, 85, 142, 143]
  "EB-TBL-4@recorded-by-usage": [87, 89, 90, 92, 93, 95]
  "EC-FASVC-40": [74, 75]
anchor: []
coverage:
  web: automated
---
# Tab Usage: Kolom, Nilai Kosong, Ringkasan Teks, Persentase, dan State Kosong atau Gagal

## Prerequisites
- Aktor: Total Control.
- Layar awal: Detail Service Center `PT Sejuk Abadi Teknik`, tab Usage.
- Komponen: Tab Usage Service Center
- Data:
  - DU-062-1: Baris Usage Routine `Chiller Lantai 2`: Reference `TASK-00188`, Asset ID `AST-00188`, Brand `Daikin`, Model/Type `VRV IV`, Group `Branch Surabaya` (di bawah `Head Office`), Schedule `Servis AC Triwulan`, Status `Completed`, Result `Normal`, Finished At `2026-03-10T14:30:00Z`, Due date `2026-03-11`, Recorded By `Dewi Anggraini`, Cost `1250000`.
  - DU-062-2: Baris Usage Routine `Panel Distribusi Utama`: Reference `TASK-00305`, Asset ID `AST-00305`, Brand `LG`, Model/Type `PM-5560`, Group `Head Office`, Schedule `Inspeksi Panel Tahunan`, Status `Completed`, Result `Needs attention`, Finished At `2026-03-08T09:00:00Z`, Due date `2026-03-07`, Recorded By `Rina Wijaya`, Cost `2400000`.
  - DU-062-3: Baris Usage Routine `Genset Gudang Utara`: Reference `TASK-00231`, Asset ID `AST-00231`, Brand `Daikin`, Model/Type `GX-250`, Group `Head Office`, Schedule `Servis Genset Bulanan`, Status `In Progress`, tanpa Result, tanpa Finished At, Recorded By `Rina Wijaya`, tanpa Cost.
  - DU-062-4: Baris Usage Routine `Kompresor Bengkel`: Reference `TASK-00412`, Asset ID `AST-00412`, Brand `LG`, Model/Type `KP-22`, Group `Branch Malang`, Schedule `Servis Kompresor`, Status `Canceled`, tanpa Result, tanpa Finished At, Recorded By `Budi Santoso`, tanpa Cost.
  - DU-062-5: Baris Usage Repair `Forklift Gudang`: Reference `WO-00277`, Asset ID `AST-00277`, Brand `Daikin`, Model/Type `FD-25`, Group `Branch Surabaya`, tanpa Schedule, tanpa Result, tanpa Finished At, Recorded By `Budi Santoso`.
  - DU-062-6: Baris Usage Routine `Genset Portabel`: Reference `TASK-00520`, Asset ID `AST-00520`, tanpa Brand, tanpa Model/Type, Group `Head Office`, Schedule `Servis Genset Bulanan`, Status `Completed`, Result `Normal`, Finished At `2026-03-09T11:15:00Z`, tanpa Due date, Recorded By `Rina Wijaya`, Cost `750000`.
  - DU-062-7: Baris Usage Routine `Servis Pompa`: Reference `TASK-00610`, Asset ID `AST-00610`, Brand `Daikin`, Model/Type `CP-90`, Group `Branch Surabaya`, Schedule `Servis Pompa Bulanan`, Status `To Do`, tanpa Result, tanpa Finished At, tanpa Recorded By, tanpa Cost.
  - DU-062-8: Baris Usage Routine `Pompa Air Lama`: Reference `TASK-00099`, Asset ID `AST-00099`, Brand `Daikin`, Model/Type `CP-50`, Group `Head Office`, Schedule `Servis Pompa Bulanan`, Status `Completed`, Result `Normal`, Finished At `2025-01-15T08:00:00Z`, Recorded By `Rina Wijaya`, Cost `300000`.
  - DU-062-9: Pengaturan General Settings: Date Format `dd/MM/yy`, Time Format `24h`, Time Zone `UTC`, mata uang `IDR` (tampil `Rp 1.250.000,00`); tanggal hari ini `2026-03-18`; filter periode default Finished At `18/03/25` sampai `18/03/26`.
  - DU-062-10: Respons ringkasan K1: Active schedules `3`, Open tasks `2`, Completed `3`, On-time rate `50%`, Needs attention rate `33%`, Total cost `Rp 4.400.000,00`, Avg cost per task `Rp 1.466.666,67`.
  - DU-062-11: Respons ringkasan K2: Active schedules `3`, Open tasks `2`, Completed `0`, On-time rate `—`, Needs attention rate `—`, Avg cost per task `—`.
  - DU-062-12: Baris Usage Routine `Kompresor Cadangan`: Reference `TASK-00720`, Asset ID `AST-00720`, Brand `LG`, Model/Type `KP-30`, Group `Head Office`, Schedule `Servis Kompresor`, Status `Completed`, Result `Normal`, Finished At `2026-03-12T10:00:00Z`, tanpa Due date, Recorded By `Budi Santoso`, Cost `600000`.
  - DU-062-13: Respons ringkasan K3: Active schedules `3`, Open tasks `2`, Completed `2`, On-time rate `—`, Needs attention rate `0%`.
  - DU-062-14: Kata kunci Search `Vendor Tidak Ada`.
  - DU-062-15: Baris Usage Routine `Chiller Gudang Timur`: Reference `TASK-00730`, Asset ID `AST-00730`, Brand `Daikin`, Model/Type `VRV III`, Group `Head Office`, Schedule `Servis AC Bulanan`, Status `Completed`, Result `Normal`, Finished At `2026-03-13T08:00:00Z`, Recorded By `Rina Wijaya`, total biaya tercatat `0` (tampil `Rp 0,00` mengikuti format mata uang General Settings).
  - DU-062-16: Baris Usage Routine `AC Ruang Server`: Reference `TASK-00740`, Asset ID `AST-00740`, Brand `LG`, Model/Type `ARNU18`, Group `Head Office`, Schedule `Servis AC Bulanan`, Status `Completed`, Result `Normal`, Finished At `2026-03-14T08:00:00Z`, Recorded By `Budi Santoso`, tanpa baris biaya.
  - DU-062-17: Baris Usage Routine `Kipas Industri`: Reference `TASK-00750`, Asset ID `AST-00750`, Brand `Daikin`, Model/Type `FX-20`, Group `Head Office`, Schedule `Servis Kipas Bulanan`, Status `On Schedule`, tanpa Recorded By, tanpa Cost.
  - DU-062-18: Baris Usage Routine `Mesin Cuci Industri`: Reference `TASK-00760`, Asset ID `AST-00760`, Brand `LG`, Model/Type `WM-90`, Group `Head Office`, Schedule `Servis Mesin Bulanan`, Status `Waiting for Assignment`, tanpa Recorded By, tanpa Cost.
  - DU-062-19: Pengaturan General Settings: Date Format `dd/MM/yy`, Time Format `24h`, Time Zone `Asia/Jakarta`; waktu saat ini `2026-03-17T20:00:00Z` (tanggal hari ini menurut zona itu `18/03/26`); filter periode default Finished At `18/03/25` sampai `18/03/26`.
- Kondisi:
  - K1: pengaturan memakai DU-062-9; daftar Usage memuat DU-062-1 sampai DU-062-7 di halaman pertama dengan filter periode default aktif (DU-062-8 tidak termasuk); ringkasan memakai DU-062-10; respons setelah filter Finished At dikosongkan memuat juga DU-062-8; respons Search DU-062-14 kosong; Download berhasil.
  - K2: pengaturan memakai DU-062-9; daftar Usage memuat DU-062-3, DU-062-4, DU-062-5, dan DU-062-7 saja; ringkasan memakai DU-062-11.
  - K3: pengaturan memakai DU-062-9; daftar Usage memuat DU-062-6 dan DU-062-12; ringkasan memakai DU-062-13.
  - K4: Service Center dengan Usage `0`; respons Usage kosong.
  - K5: Service Center dengan Usage `148`; respons Usage kosong karena filter periode default.
  - K6: respons Usage pertama gagal karena error server; respons sesudah `[Try Again]` memuat DU-062-1 sampai DU-062-7.
  - K7: pengaturan memakai DU-062-19; daftar Usage memuat DU-062-1 sampai DU-062-7 dengan filter periode default aktif.
  - K8: pengaturan memakai DU-062-9; daftar Usage memuat DU-062-15 sampai DU-062-18.

## Test Steps

### Toolbar dan kolom tab Usage
1. Tampilkan Tab Usage Service Center dengan kondisi K1
2. Verifikasi `Search`, `Filter`, dan `Download` tampil di toolbar
3. Verifikasi tombol `Changelog` tidak tampil di toolbar tab Usage
4. Verifikasi tabel memuat kolom `Type`, `Reference`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Schedule`, `Status`, `Result`, `Finished At`, `Recorded By`, dan `Cost`

### Search tab Usage berplaceholder Search usage
5. Tampilkan Tab Usage Service Center dengan kondisi K1
6. Klik ikon Search
7. Verifikasi kotak Search berplaceholder `Search usage...`

### Urutan default Finished At terbaru dengan baris tanpa Finished At di atas
8. Tampilkan Tab Usage Service Center dengan kondisi K1
9. Verifikasi tabel memuat baris `Chiller Lantai 2`, `Panel Distribusi Utama`, `Genset Gudang Utara`, `Kompresor Bengkel`, `Forklift Gudang`, `Genset Portabel`, dan `Servis Pompa`
10. Verifikasi baris `Genset Gudang Utara`, `Kompresor Bengkel`, `Forklift Gudang`, dan `Servis Pompa` berada di atas semua baris yang punya Finished At; urutan di antara baris tanpa Finished At tidak diasersi
11. Verifikasi baris dengan Finished At berurutan `Chiller Lantai 2`, `Genset Portabel`, lalu `Panel Distribusi Utama`

### Filter periode default 12 bulan terakhir dapat dihapus
12. Tampilkan Tab Usage Service Center dengan kondisi K1
13. Klik `Filter`
14. Verifikasi field Finished At terisi rentang `18/03/25` sampai `18/03/26`
15. Verifikasi baris `Genset Gudang Utara` tampil walau filter periode aktif
16. Verifikasi baris `Pompa Air Lama` tidak tampil
17. Klik `[Clear Field]`
18. Klik `[Apply]`
19. Verifikasi baris `Genset Gudang Utara` tetap tampil
20. Verifikasi field Finished At kosong dengan placeholder `Select date`
21. Verifikasi baris `Pompa Air Lama` tampil dengan Finished At `15/01/25, 08:00`

### Panel Filter tab Usage memuat label dan placeholder kolom yang bisa difilter
22. Tampilkan Tab Usage Service Center dengan kondisi K1
23. Klik `Filter`
24. Verifikasi filter `Type` berupa pilihan ganda dengan pencarian dan placeholder `All types`
25. Verifikasi filter `Name` berupa pilihan ganda dengan pencarian dan placeholder `All names`
26. Verifikasi filter `Brand` berupa pilihan ganda dengan pencarian dan placeholder `All brands`
27. Verifikasi filter `Model/Type` berupa pilihan ganda dengan pencarian dan placeholder `All models/types`
28. Verifikasi filter `Group` berupa pilihan ganda dengan pencarian dan placeholder `All groups`
29. Verifikasi filter `Status` berupa pilihan ganda dengan pencarian dan placeholder `All statuses`
30. Verifikasi filter `Result` berupa pilihan ganda dengan pencarian dan placeholder `All results`
31. Verifikasi filter `Finished At` berupa rentang tanggal dengan placeholder `Select date`
32. Verifikasi filter `Recorded By` berupa pilihan ganda dengan pencarian dan placeholder `All users`
33. Verifikasi filter `Cost` berupa rentang dengan placeholder `Min` dan `Max`
34. Verifikasi tidak ada filter `Reference`, `Asset ID`, dan `Schedule`

### Baris Routine Completed Normal menampilkan seluruh kolom
35. Tampilkan Tab Usage Service Center dengan kondisi K1
36. Verifikasi Type baris `Chiller Lantai 2` menampilkan `Routine`
37. Verifikasi Reference baris `Chiller Lantai 2` menampilkan `TASK-00188` sebagai tautan
38. Verifikasi Asset ID baris `Chiller Lantai 2` menampilkan `AST-00188`
39. Verifikasi kolom `Brand` baris `Chiller Lantai 2` menampilkan badge `Daikin`
40. Verifikasi Model/Type baris `Chiller Lantai 2` menampilkan badge `VRV IV`
41. Verifikasi kolom `Group` baris `Chiller Lantai 2` menampilkan badge `Branch Surabaya`
42. Verifikasi Schedule baris `Chiller Lantai 2` menampilkan `Servis AC Triwulan`
43. Verifikasi Status baris `Chiller Lantai 2` menampilkan `Completed`
44. Verifikasi Result baris `Chiller Lantai 2` menampilkan badge `Normal` bersemantik `success`
45. Verifikasi Finished At baris `Chiller Lantai 2` menampilkan `10/03/26, 14:30`
46. Verifikasi Cost baris `Chiller Lantai 2` menampilkan `Rp 1.250.000,00`

### Hover Brand, Model/Type, dan Group menampilkan nama penuh dan hierarki
47. Tampilkan Tab Usage Service Center dengan kondisi K1
48. Arahkan kursor ke badge kolom `Brand` baris `Chiller Lantai 2`
49. Verifikasi nama penuh `Daikin` tersampaikan
50. Arahkan kursor ke badge Model/Type baris `Chiller Lantai 2`
51. Verifikasi nama penuh `VRV IV` tersampaikan
52. Arahkan kursor ke badge kolom `Group` baris `Chiller Lantai 2`
53. Verifikasi hierarki lengkap `Head Office > Branch Surabaya` tersampaikan

### Result Needs attention bersemantik warning
54. Tampilkan Tab Usage Service Center dengan kondisi K1
55. Verifikasi Result baris `Panel Distribusi Utama` menampilkan badge `Needs attention` bersemantik `warning`
56. Verifikasi Finished At baris `Panel Distribusi Utama` menampilkan `08/03/26, 09:00`
57. Verifikasi Cost baris `Panel Distribusi Utama` menampilkan `Rp 2.400.000,00`

### Task belum selesai menampilkan strip pada Finished At, Result, dan Cost
58. Tampilkan Tab Usage Service Center dengan kondisi K1
59. Verifikasi Status baris `Genset Gudang Utara` menampilkan `In Progress`
60. Verifikasi Recorded By baris `Genset Gudang Utara` menampilkan `Rina W`
61. Verifikasi Finished At baris `Genset Gudang Utara` menampilkan `—`
62. Verifikasi Result baris `Genset Gudang Utara` menampilkan `—`
63. Verifikasi Cost baris `Genset Gudang Utara` menampilkan `—`

### Task Canceled menampilkan strip pada Finished At, Result, dan Cost
64. Tampilkan Tab Usage Service Center dengan kondisi K1
65. Verifikasi Status baris `Kompresor Bengkel` menampilkan `Canceled`
66. Verifikasi Recorded By baris `Kompresor Bengkel` menampilkan `Budi S`
67. Verifikasi Finished At baris `Kompresor Bengkel` menampilkan `—`
68. Verifikasi Result baris `Kompresor Bengkel` menampilkan `—`
69. Verifikasi Cost baris `Kompresor Bengkel` menampilkan `—`

### Task To Do belum punya pencatat
70. Tampilkan Tab Usage Service Center dengan kondisi K1
71. Verifikasi Status baris `Servis Pompa` menampilkan `To Do`
72. Verifikasi Recorded By baris `Servis Pompa` menampilkan `—`

### Baris Repair: Reference bukan tautan, Schedule dan Result strip
73. Tampilkan Tab Usage Service Center dengan kondisi K1
74. Verifikasi Type baris `Forklift Gudang` menampilkan `Repair`
75. Verifikasi Type baris `Chiller Lantai 2` menampilkan `Routine`
76. Verifikasi Reference baris `Forklift Gudang` menampilkan `WO-00277` sebagai teks biasa, bukan tautan
77. Verifikasi Schedule baris `Forklift Gudang` menampilkan `—`
78. Verifikasi Result baris `Forklift Gudang` menampilkan `—`
79. Verifikasi Finished At baris `Forklift Gudang` menampilkan `—`
80. Verifikasi Recorded By baris `Forklift Gudang` menampilkan `Budi S`

### Aset tanpa Brand dan Model/Type menampilkan strip
81. Tampilkan Tab Usage Service Center dengan kondisi K1
82. Verifikasi Name baris `Genset Portabel` menampilkan `Genset Portabel`
83. Verifikasi kolom `Brand` baris `Genset Portabel` menampilkan `—`
84. Verifikasi Model/Type baris `Genset Portabel` menampilkan `—`
85. Verifikasi Cost baris `Genset Portabel` menampilkan `Rp 750.000,00`

### Recorded By tampil singkat tanpa titik dengan nama lengkap saat hover
86. Tampilkan Tab Usage Service Center dengan kondisi K1
87. Verifikasi Recorded By baris `Chiller Lantai 2` menampilkan `Dewi A`
88. Arahkan kursor ke Recorded By baris `Chiller Lantai 2`
89. Verifikasi nama lengkap `Dewi Anggraini` tersampaikan
90. Verifikasi Recorded By baris `Panel Distribusi Utama` menampilkan `Rina W`
91. Arahkan kursor ke Recorded By baris `Panel Distribusi Utama`
92. Verifikasi nama lengkap `Rina Wijaya` tersampaikan
93. Verifikasi Recorded By baris `Kompresor Bengkel` menampilkan `Budi S`
94. Arahkan kursor ke Recorded By baris `Kompresor Bengkel`
95. Verifikasi nama lengkap `Budi Santoso` tersampaikan

### Ringkasan teks tab Usage dengan nilai biaya
96. Tampilkan Tab Usage Service Center dengan kondisi K1
97. Verifikasi ringkasan memuat `Active schedules: 3`, `Open tasks: 2`, `Completed: 3`, `On-time rate: 50%`, `Needs attention rate: 33%`, `Total cost: Rp 4.400.000,00`, `Avg cost per task: Rp 1.466.666,67`

### Ringkasan tanpa Task Completed menampilkan strip pada persentase dan rata-rata biaya
98. Tampilkan Tab Usage Service Center dengan kondisi K2
99. Verifikasi ringkasan memuat `Completed: 0`
100. Verifikasi ringkasan memuat `On-time rate: —`
101. Verifikasi ringkasan memuat `Needs attention rate: —`
102. Verifikasi ringkasan memuat `Avg cost per task: —`

### On-time rate strip bila tidak ada Completed ber-Due date
103. Tampilkan Tab Usage Service Center dengan kondisi K3
104. Verifikasi ringkasan memuat `Completed: 2`
105. Verifikasi ringkasan memuat `Needs attention rate: 0%`
106. Verifikasi ringkasan memuat `On-time rate: —`

### Usage 0 menampilkan Not used yet tanpa tombol
107. Tampilkan Tab Usage Service Center dengan kondisi K4
108. Verifikasi `Not used yet.` tampil
109. Verifikasi empty state tidak memuat tombol
110. Verifikasi `No results found` tidak tampil

### Usage lebih dari 0 tanpa baris karena filter periode menampilkan No results found
111. Tampilkan Tab Usage Service Center dengan kondisi K5
112. Verifikasi `No results found` tampil
113. Verifikasi `Try adjusting your search or filter.` tampil
114. Verifikasi `Not used yet.` tidak tampil

### Search tanpa hasil menampilkan No results found
115. Tampilkan Tab Usage Service Center dengan kondisi K1
116. Klik ikon Search
117. Ketik Search `Vendor Tidak Ada`, tekan Enter
118. Verifikasi `No results found` tampil
119. Verifikasi `Try adjusting your search or filter.` tampil

### Gagal memuat menampilkan pesan error dengan Try Again, bukan empty state
120. Tampilkan Tab Usage Service Center dengan kondisi K6
121. Verifikasi `Unable to load this data.` tampil
122. Verifikasi tombol `[Try Again]` tampil
123. Verifikasi `Not used yet.` dan `No results found` tidak tampil
124. Klik `[Try Again]`
125. Verifikasi baris `Chiller Lantai 2` tampil

### Download tab Usage memakai nama berkas Service-Center-Usage
126. Tampilkan Tab Usage Service Center dengan kondisi K1
127. Klik `Download`
128. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil
129. Pilih `Download as CSV`
130. Verifikasi berkas terunduh bernama `Service-Center-Usage.csv`
131. Klik `Download`
132. Pilih `Download as XLSX`
133. Verifikasi berkas terunduh bernama `Service-Center-Usage.xlsx`

### Filter periode default mengikuti zona waktu General Settings
134. Tampilkan Tab Usage Service Center dengan kondisi K7
135. Klik `Filter`
136. Verifikasi field Finished At terisi rentang `18/03/25` sampai `18/03/26`

### Baris Routine punya aksi Maintenance Routine Log dan baris Repair tanpa aksi
137. Tampilkan Tab Usage Service Center dengan kondisi K1
138. Klik `⋯` pada baris `Chiller Lantai 2`
139. Verifikasi menu aksi baris memuat `Maintenance Routine Log`
140. Verifikasi baris `Forklift Gudang` tidak memiliki aksi baris

### Cost nol dan strip, Recorded By strip sebelum In Progress
141. Tampilkan Tab Usage Service Center dengan kondisi K8
142. Verifikasi Cost baris `Chiller Gudang Timur` menampilkan `Rp 0,00`
143. Verifikasi Cost baris `AC Ruang Server` menampilkan `—`
144. Verifikasi Status baris `Kipas Industri` menampilkan `On Schedule`
145. Verifikasi Recorded By baris `Kipas Industri` menampilkan `—`
146. Verifikasi Status baris `Mesin Cuci Industri` menampilkan `Waiting for Assignment`
147. Verifikasi Recorded By baris `Mesin Cuci Industri` menampilkan `—`

### Setiap kolom data tab Usage dapat diurutkan lewat header
148. Tampilkan Tab Usage Service Center dengan kondisi K1
149. Klik header kolom `Type`
150. Verifikasi header kolom `Type` berstatus terurut
151. Klik header kolom `Reference`
152. Verifikasi header kolom `Reference` berstatus terurut
153. Klik header kolom `Name`
154. Verifikasi header kolom `Name` berstatus terurut
155. Klik header kolom `Asset ID`
156. Verifikasi header kolom `Asset ID` berstatus terurut
157. Klik header kolom `Brand`
158. Verifikasi header kolom `Brand` berstatus terurut
159. Klik header kolom `Model/Type`
160. Verifikasi header kolom `Model/Type` berstatus terurut
161. Klik header kolom `Group`
162. Verifikasi header kolom `Group` berstatus terurut
163. Klik header kolom `Schedule`
164. Verifikasi header kolom `Schedule` berstatus terurut
165. Klik header kolom `Status`
166. Verifikasi header kolom `Status` berstatus terurut
167. Klik header kolom `Result`
168. Verifikasi header kolom `Result` berstatus terurut
169. Klik header kolom `Finished At`
170. Verifikasi header kolom `Finished At` berstatus terurut
171. Klik header kolom `Recorded By`
172. Verifikasi header kolom `Recorded By` berstatus terurut
173. Klik header kolom `Cost`
174. Verifikasi header kolom `Cost` berstatus terurut

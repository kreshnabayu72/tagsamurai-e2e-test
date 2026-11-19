---
id: TC-FA-FASVC-UI-052-form-validasi-cakupan
title: "Form: Service Type, Available to, Specialization, dan Brands"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["V-FASVC-04", "V-FASVC-05", "V-FASVC-13", "V-FASVC-14", "V-FASVC-26", "V-FASVC-31", "V-FASVC-32", "FLD-FASVC-02", "FLD-FASVC-03", "FLD-FASVC-04", "FLD-FASVC-05", "S-FASVC-06", "S-FASVC-13", "FASVC-LOGIC-02c", "FASVC-LOGIC-02e", "FASVC-LOGIC-02l", "FASVC-LOGIC-02n", "FASVC-LOGIC-07h", "FASVC-LOGIC-07i", "EC-FASVC-11", "EB-FRM-8@service-type", "EB-FRM-8@available-to", "EB-SRC-6@tree-available-to", "EB-SRC-6@tree-specialization", "EB-TBL-5@checkbox-service-type"]
smoke: []
dependsOn: []
trace:
  "V-FASVC-04": [5, 14]
  "V-FASVC-05": [21, 28]
  "V-FASVC-13": [98, 99, 102, 103]
  "V-FASVC-14": [89, 90, 91]
  "V-FASVC-26": [130, 131, 171, 172, 170]
  "V-FASVC-31": [110, 111, 114, 115, 149, 150, 154, 148, 153]
  "V-FASVC-32": [122, 123, 162, 163, 161]
  "FLD-FASVC-02": [2, 3, 5, 10, 14, 38, 89]
  "FLD-FASVC-03": [30, 32, 33, 35, 122]
  "FLD-FASVC-04": [30, 32, 33, 36, 41, 43, 45, 46, 47, 50, 130]
  "FLD-FASVC-05": [16, 21, 23, 28, 37, 98, 102, 110, 114, 136, 141]
  "S-FASVC-06": [74, 75, 77, 79]
  "S-FASVC-13": [65, 66, 67, 71]
  "FASVC-LOGIC-02c": [2, 5, 8, 14]
  "FASVC-LOGIC-02e": [83, 84, 85]
  "FASVC-LOGIC-02l": [30, 33, 41, 45]
  "FASVC-LOGIC-02n": [36, 43, 45]
  "FASVC-LOGIC-07h": [74, 75, 81]
  "FASVC-LOGIC-07i": [75, 77, 79]
  "EC-FASVC-11": [75, 81, 89]
  "EB-FRM-8@service-type": [5, 10, 14]
  "EB-FRM-8@available-to": [21, 23, 28, 98, 102, 110, 114]
  "EB-SRC-6@tree-available-to": [54, 55]
  "EB-SRC-6@tree-specialization": [60, 61]
  "EB-TBL-5@checkbox-service-type": [77, 79]
anchor: []
coverage:
  web: automated
---

# Form: Service Type, Available to, Specialization, dan Brands

## Prerequisites
- Aktor: Total Control, dan Asset Admin dengan cakupan Group `Branch Surabaya` (K2).
- Layar awal: dialog Create / Edit Service Center yang ditampilkan menurut kondisi di bawah.
- Komponen: Dialog Create / Edit Service Center
- Data:
  - DU-052-1: pohon Group cakupan Total Control: root `All groups`, anak `Head Office`, cucu `Branch Surabaya` dan `Branch Malang`.
  - DU-052-2: pohon Category: `Cooling` dengan anak `AC` dan `Refrigeration`, serta `Power` dengan anak `Generator` dan `UPS`.
  - DU-052-3: master Brand dengan Brand Active `Daikin`, `Panasonic`, dan `Sharp`, serta Brand Inactive `LG` dan `Hitachi`.
  - DU-052-4: pohon Group cakupan Asset Admin `Branch Surabaya`: `Head Office` sebagai ancestor yang tidak dapat dipilih dan `Branch Surabaya` yang dapat dipilih.
  - DU-052-5: Negara company pada General Settings `Indonesia`.
  - DU-052-6: Service Center untuk Edit tanpa pemakaian: Name `PT Teknik Cakupan Prima`, Service type `Routine` dan `Repair`, Available to `Branch Surabaya`, Specialization `Generator`, Brands `Daikin` dan `Panasonic`, Country `Indonesia`, City `Bekasi`, Company email `admin@teknikcakupan-prima.co.id`.
  - DU-052-7: Service Center untuk Edit yang dipakai: Name `CV Servis Terpakai Jaya`, Service type `Routine` dan `Repair`, Routine dipakai 1 Schedule aktif atau Task terbuka, Repair dipakai 3 Schedule aktif atau Task terbuka, Available to `Branch Surabaya`, Country `Indonesia`, City `Depok`, Company email `admin@servisterpakai-jaya.co.id`.
  - DU-052-8: master Brand kosong.
- Kondisi:
  - K1: dialog Create dibuka oleh Total Control; pohon Group DU-052-1, pohon Category DU-052-2, master Brand DU-052-3, dan Negara company DU-052-5; permintaan simpan dijawab sukses.
  - K2: dialog Create dibuka oleh Asset Admin dengan cakupan Group `Branch Surabaya`; pohon Group DU-052-4, pohon Category DU-052-2, master Brand DU-052-3, dan Negara company DU-052-5.
  - K3: seperti K1, dengan master Brand DU-052-8 (kosong).
  - K4: dialog Edit untuk Service Center DU-052-6 dibuka oleh Total Control; pohon Group DU-052-1, pohon Category DU-052-2, master Brand DU-052-3, dan Negara company DU-052-5; permintaan simpan dijawab sukses.
  - K5: dialog Edit untuk Service Center DU-052-7 dibuka oleh Total Control; pohon Group DU-052-1, pohon Category DU-052-2, dan master Brand DU-052-3.
  - K6: seperti K1, dan permintaan simpan ditolak karena Available to memuat Group di luar cakupan pengguna.
  - K7: seperti K4, dan permintaan simpan ditolak karena Available to memuat Group di luar cakupan pengguna.
  - K8: seperti K1, dan permintaan simpan ditolak karena Available to memuat Group yang tidak ada di master.
  - K9: seperti K4, dan permintaan simpan ditolak karena Available to memuat Group yang tidak ada di master.
  - K10: seperti K1, dan permintaan simpan ditolak karena Specialization memuat Category yang tidak ada di master.
  - K11: seperti K1, dan permintaan simpan ditolak karena Brands memuat Brand yang tidak ada di master atau ganda.
  - K12: seperti K4, dan Service type `Repair` sudah dipakai Schedule aktif sejak dialog dibuka sehingga permintaan simpan yang melepasnya ditolak.

## Test Steps

### Service type kosong ditolak saat Save (Create)
1. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
2. Verifikasi field `Service type` memuat checkbox `Routine` dan checkbox `Repair`
3. Verifikasi field `Service type` ditandai wajib
4. Klik `[Submit]` tanpa mencentang checkbox `Service type`
5. Verifikasi field `Service type` ditandai tidak valid dengan pesan `Select at least one service type`
6. Centang checkbox `Routine`
7. Centang checkbox `Repair`
8. Verifikasi checkbox `Routine` dan checkbox `Repair` tercentang bersamaan

### Service type kosong ditolak saat Save (Edit)
9. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
10. Verifikasi checkbox `Routine` dan checkbox `Repair` tercentang
11. Lepas centang checkbox `Routine`
12. Lepas centang checkbox `Repair`
13. Klik `[Save]`
14. Verifikasi field `Service type` ditandai tidak valid dengan pesan `Select at least one service type`

### Available to kosong ditolak saat Save (Create)
15. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
16. Verifikasi field `Available to` ditandai wajib
17. Klik trigger field `Available to`
18. Klik checkbox `All groups` untuk melepas seluruh pilihan
19. Klik `[Select]` pada dialog pilihan Available to
20. Klik `[Submit]`
21. Verifikasi field `Available to` ditandai tidak valid dengan pesan `Select at least one group`

### Available to kosong ditolak saat Save (Edit)
22. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
23. Verifikasi trigger field `Available to` menampilkan `1 group selected`
24. Klik trigger field `Available to`
25. Klik checkbox `Branch Surabaya` untuk melepasnya
26. Klik `[Select]` pada dialog pilihan Available to
27. Klik `[Save]`
28. Verifikasi field `Available to` ditandai tidak valid dengan pesan `Select at least one group`

### Specialization dan Brands opsional pada Create
29. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
30. Verifikasi field `Specialization` dan field `Brands` tidak ditandai wajib
31. Klik `[Submit]`
32. Verifikasi field `Name` ditandai tidak valid dengan pesan `Name must not be empty`
33. Verifikasi field `Specialization` dan field `Brands` tidak ditandai tidak valid

### Nilai tersimpan terisi pada Edit
34. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
35. Verifikasi trigger field `Specialization` menampilkan `1 category selected`
36. Verifikasi field `Brands` menampilkan chip `Daikin` dan chip `Panasonic`
37. Verifikasi trigger field `Available to` menampilkan `1 group selected`
38. Verifikasi checkbox `Routine` dan checkbox `Repair` tercentang

### Brands memilih dari master dan memilih lebih dari satu
39. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
40. Klik field `Brands`
41. Verifikasi daftar Brands memuat opsi `Daikin`, `Panasonic`, dan `Sharp`
42. Klik opsi `Daikin`
43. Verifikasi chip `Daikin` tampil pada field `Brands`
44. Klik opsi `Panasonic`
45. Verifikasi chip `Daikin` dan chip `Panasonic` tampil pada field `Brands`
46. Verifikasi tidak ada opsi `LG` yang dapat dipilih pada daftar Brands
47. Verifikasi tidak ada opsi `Hitachi` yang dapat dipilih pada daftar Brands

### Brands tanpa opsi bila master Brand kosong
48. Tampilkan Dialog Create / Edit Service Center dengan kondisi K3
49. Klik field `Brands`
50. Verifikasi daftar Brands menampilkan `No options available`

### Pencarian pohon Available to menyaring saat mengetik
51. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
52. Klik trigger field `Available to`
53. Ketik `Surabaya` di kotak `Search` pada dialog pilihan Available to
54. Verifikasi `Branch Surabaya` tampil pada pohon Available to[^drift-1]
55. Verifikasi `Branch Malang` tidak tampil pada pohon Available to[^drift-1]
56. Klik `[Cancel]` pada dialog pilihan Available to

### Pencarian pohon Specialization menyaring saat mengetik
57. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
58. Klik trigger field `Specialization`
59. Ketik `Refrigeration` di kotak `Search` pada dialog pilihan Specialization
60. Verifikasi `Refrigeration` tampil pada pohon Specialization[^drift-1]
61. Verifikasi `Generator` tidak tampil pada pohon Specialization[^drift-1]
62. Klik `[Cancel]` pada dialog pilihan Specialization

### Pohon Available to bagi Asset Admin dengan cakupan satu Group
63. Tampilkan Dialog Create / Edit Service Center dengan kondisi K2
64. Klik trigger field `Available to`
65. Verifikasi `Branch Surabaya` tampil dengan checkbox yang dapat dipilih
66. Verifikasi `Head Office` tampil greyed-out dengan checkbox disabled sehingga tidak dapat dipilih
67. Verifikasi `All groups` tidak tampil pada pohon Available to
68. Klik `[Cancel]` pada dialog pilihan Available to

### Pohon Available to bagi Total Control memuat All groups
69. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
70. Klik trigger field `Available to`
71. Verifikasi `All groups` tampil pada pohon Available to
72. Klik `[Cancel]` pada dialog pilihan Available to

### Checkbox Service type yang dipakai tidak dapat dilepas
73. Tampilkan Dialog Create / Edit Service Center dengan kondisi K5
74. Verifikasi checkbox `Routine` dan checkbox `Repair` tercentang
75. Verifikasi checkbox `Routine` disabled
76. Arahkan kursor ke checkbox `Routine`
77. Verifikasi alasan `Used by 1 active schedule or open task.` tersampaikan pada checkbox `Routine` yang disabled
78. Arahkan kursor ke checkbox `Repair`
79. Verifikasi alasan `Used by 3 active schedules or open tasks.` tersampaikan pada checkbox `Repair` yang disabled
80. Klik checkbox `Routine`
81. Verifikasi checkbox `Routine` tetap tercentang

### Bidang cakupan dijelaskan helper sebagai pembatas pemilih
82. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
83. Verifikasi helper `Groups that can assign work to this service center.` tampil pada field `Available to`
84. Verifikasi helper `Leave empty if they work on all categories.` tampil pada field `Specialization`
85. Verifikasi helper `Leave empty if they work on all brands.` tampil pada field `Brands`

### Service type yang dipakai ditolak server saat Save (Edit)
86. Tampilkan Dialog Create / Edit Service Center dengan kondisi K12
87. Lepas centang checkbox `Repair`
88. Klik `[Save]`
89. Verifikasi field `Service type` ditandai tidak valid dengan pesan `Repair is used by active schedules or open tasks.`
90. Verifikasi dialog Edit masih terbuka
91. Verifikasi checkbox `Routine` tercentang

### Group di luar cakupan ditolak server saat Save (Create)
92. Tampilkan Dialog Create / Edit Service Center dengan kondisi K6
93. Isi Name `Bengkel Cakupan Servis {runId}`
94. Centang checkbox `Routine`
95. Isi City `Bitung`
96. Isi Company email `cs@cakupanservis-bitung.co.id`
97. Klik `[Submit]`
98. Verifikasi toast error `You don't have access to some groups.` tampil
99. Verifikasi dialog Create masih terbuka

### Group di luar cakupan ditolak server saat Save (Edit)
100. Tampilkan Dialog Create / Edit Service Center dengan kondisi K7
101. Klik `[Save]`
102. Verifikasi toast error `You don't have access to some groups.` tampil
103. Verifikasi dialog Edit masih terbuka

### Group yang tidak ada di master ditolak server saat Save (Create)
104. Tampilkan Dialog Create / Edit Service Center dengan kondisi K8
105. Isi Name `Bengkel Cakupan Servis {runId}`
106. Centang checkbox `Routine`
107. Isi City `Bitung`
108. Isi Company email `cs@cakupanservis-bitung.co.id`
109. Klik `[Submit]`
110. Verifikasi field `Available to` ditandai tidak valid dengan pesan `Select a valid group`
111. Verifikasi dialog Create masih terbuka

### Group yang tidak ada di master ditolak server saat Save (Edit)
112. Tampilkan Dialog Create / Edit Service Center dengan kondisi K9
113. Klik `[Save]`
114. Verifikasi field `Available to` ditandai tidak valid dengan pesan `Select a valid group`
115. Verifikasi dialog Edit masih terbuka

### Category yang tidak ada di master ditolak server saat Save (Create)
116. Tampilkan Dialog Create / Edit Service Center dengan kondisi K10
117. Isi Name `Bengkel Cakupan Servis {runId}`
118. Centang checkbox `Routine`
119. Isi City `Bitung`
120. Isi Company email `cs@cakupanservis-bitung.co.id`
121. Klik `[Submit]`
122. Verifikasi field `Specialization` ditandai tidak valid dengan pesan `Select a valid category`
123. Verifikasi dialog Create masih terbuka

### Brand yang tidak ada di master atau ganda ditolak server saat Save (Create)
124. Tampilkan Dialog Create / Edit Service Center dengan kondisi K11
125. Isi Name `Bengkel Cakupan Servis {runId}`
126. Centang checkbox `Routine`
127. Isi City `Bitung`
128. Isi Company email `cs@cakupanservis-bitung.co.id`
129. Klik `[Submit]`
130. Verifikasi field `Brands` ditandai tidak valid dengan pesan `Select a valid brand`
131. Verifikasi dialog Create masih terbuka

### Available to yang dikosongkan menampilkan placeholder pada Create
132. Tampilkan Dialog Create / Edit Service Center dengan kondisi K1
133. Klik trigger field `Available to`
134. Klik checkbox `All groups` untuk melepas seluruh pilihan
135. Klik `[Select]` pada dialog pilihan Available to
136. Verifikasi trigger field `Available to` menampilkan placeholder `Select groups`

### Available to yang dikosongkan menampilkan placeholder pada Edit
137. Tampilkan Dialog Create / Edit Service Center dengan kondisi K4
138. Klik trigger field `Available to`
139. Klik checkbox `Branch Surabaya` untuk melepasnya
140. Klik `[Select]` pada dialog pilihan Available to
141. Verifikasi trigger field `Available to` menampilkan placeholder `Select groups`

### Group yang tidak ada di master: isian terjaga pada Create
142. Tampilkan Dialog Create / Edit Service Center dengan kondisi K8
143. Isi Name `Bengkel Cakupan Servis {runId}`
144. Centang checkbox `Routine`
145. Isi City `Bitung`
146. Isi Company email `cs@cakupanservis-bitung.co.id`
147. Klik `[Submit]`
148. Verifikasi field `Available to` ditandai tidak valid dengan pesan `Select a valid group`
149. Verifikasi field `Name` berisi `Bengkel Cakupan Servis {runId}` dan field `City` berisi `Bitung`
150. Verifikasi checkbox `Routine` tercentang

### Group yang tidak ada di master: isian terjaga pada Edit
151. Tampilkan Dialog Create / Edit Service Center dengan kondisi K9
152. Klik `[Save]`
153. Verifikasi field `Available to` ditandai tidak valid dengan pesan `Select a valid group`
154. Verifikasi field `Name` berisi `PT Teknik Cakupan Prima`

### Category yang tidak ada di master: isian terjaga pada Create
155. Tampilkan Dialog Create / Edit Service Center dengan kondisi K10
156. Isi Name `Bengkel Cakupan Servis {runId}`
157. Centang checkbox `Routine`
158. Isi City `Bitung`
159. Isi Company email `cs@cakupanservis-bitung.co.id`
160. Klik `[Submit]`
161. Verifikasi field `Specialization` ditandai tidak valid dengan pesan `Select a valid category`
162. Verifikasi field `Name` berisi `Bengkel Cakupan Servis {runId}` dan field `City` berisi `Bitung`
163. Verifikasi checkbox `Routine` tercentang

### Brand yang tidak ada di master atau ganda: isian terjaga pada Create
164. Tampilkan Dialog Create / Edit Service Center dengan kondisi K11
165. Isi Name `Bengkel Cakupan Servis {runId}`
166. Centang checkbox `Routine`
167. Isi City `Bitung`
168. Isi Company email `cs@cakupanservis-bitung.co.id`
169. Klik `[Submit]`
170. Verifikasi field `Brands` ditandai tidak valid dengan pesan `Select a valid brand`
171. Verifikasi field `Name` berisi `Bengkel Cakupan Servis {runId}` dan field `City` berisi `Bitung`
172. Verifikasi checkbox `Routine` tercentang

[^drift-1]: Drift PRD dan foundation vs kontrak komponen. PRD §4.2.2 tidak menetapkan waktu pencarian di tree; foundation (EB-SRC-6, `prd-conventions.md` §31.3): pencarian tree berjalan saat Enter, bukan real-time. Kontrak `TreeSelect#9`: kotak pencarian di dialog menyaring node saat teks diketik dan «Enter does nothing». Diasersi: kontrak, pohon menyaring saat mengetik tanpa Enter (SB-7).

---
id: TC-FA-FAREG-UI-011-antrean-approvals-tampilan
title: "Antrean Approvals > Registration: tab, kolom, breadcrumb, dan state tabel"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["S-REG-04", "S-REG-05", "§4.1#r13", "§4.1#p1", "§4.1#p4", "§4.1#r127", "§4.1#r128", "§4.1#r129", "§4.1#r130", "§4.1#r131", "§4.1#r135", "§4.1#r136", "§4.1#r137", "§4.1#r138", "§4.1#r139", "§4.1#r140", "§4.1#r141", "§4.2#p1", "§4.2.5#p2", "§4.2.5#p3", "§4.2.5#r1", "§4.2.5#r2", "§5#r1", "§5#r2", "§5#r5", "§7.1#p1", "§9.5#r8", "EB-FLT-6@antrean-approvals-active", "EB-FLT-6@antrean-approvals-history", "EB-TBL-11", "EB-TBL-1@antrean-approvals-active", "EB-TBL-1@antrean-approvals-history"]
smoke: []
dependsOn: []
trace:
  S-REG-04: [112, 113, 114, 118, 119, 120]
  S-REG-05: [225, 226, 227, 233, 234, 235]
  "§4.1#r13": [2, 3, 6, 8, 9, 10, 34]
  "§4.1#p1": [12, 13, 30]
  "§4.1#p4": [93, 94, 96, 97, 98, 204, 205, 207, 208, 209]
  "§4.1#r127": [33, 42, 43, 44, 90]
  "§4.1#r128": [33, 46, 48, 49, 50, 86]
  "§4.1#r129": [33, 52, 53, 54, 87]
  "§4.1#r130": [33, 56, 58, 59, 61, 62, 64, 88]
  "§4.1#r131": [33, 36, 66, 67, 68, 89]
  "§4.1#r135": [128, 138, 139, 200]
  "§4.1#r136": [128, 142, 144, 145, 194]
  "§4.1#r137": [128, 148, 149, 150, 195]
  "§4.1#r138": [128, 153, 154, 155, 156, 196]
  "§4.1#r139": [128, 159, 161, 162, 164, 197]
  "§4.1#r140": [128, 167, 169, 170, 172, 173, 174, 175, 198, 247]
  "§4.1#r141": [128, 131, 178, 179, 199]
  "§4.2#p1": [16, 17, 19, 243, 244]
  "§4.2.5#p2": [21, 27, 71, 72, 73, 75, 80, 183, 184, 185]
  "§4.2.5#p3": [22, 23, 24, 28]
  "§4.2.5#r1": [21, 31]
  "§4.2.5#r2": 27
  "§5#r1": [71, 72, 73, 76, 183, 184, 185, 186]
  "§5#r2": [37, 38, 132, 133]
  "§5#r5": [40, 135]
  "§7.1#p1": [227, 228]
  "§9.5#r8": [83, 190]
  EB-FLT-6@antrean-approvals-active: [104, 108, 109, 110]
  EB-FLT-6@antrean-approvals-history: [216, 220, 221, 222]
  EB-TBL-11: [22, 23, 24, 28]
  EB-TBL-1@antrean-approvals-active: [112, 113, 118, 121, 123, 124, 125]
  EB-TBL-1@antrean-approvals-history: [225, 226, 233, 236, 239, 240, 241]
anchor: [5, 15, 18, 39, 82, 103, 134, 189, 215]
coverage:
  web: automated
---

# Antrean Approvals > Registration: tab, kolom, breadcrumb, dan state tabel

## Prerequisites
- Aktor: Total Control, approver yang bukan pengaju satu pun pengajuan pada daftar.
- Layar awal: Approvals > Registration > Active.
- Komponen: Menu `Approvals` > `Registration`
- Data:
  - DU-011-1: pengajuan Active Registration ID `REG-20261109-00003`, Group `Gudang 1` (path penuh `PT Sejahtera Abadi > Cabang A > Gudang 1`), Total Asset `12`, Requested By `Rina Wulandari`, Last Updated `2026-11-09T10:20:00Z`.
  - DU-011-2: pengajuan Active Registration ID `REG-20261108-00011`, Group `Kantor Pusat`, Total Asset `30`, Requested By `Hadi Kusuma`, Last Updated `2026-11-08T14:02:00Z`.
  - DU-011-3: pengajuan Active Registration ID `REG-20261107-00002`, Group `Gudang 2`, Total Asset `5`, Requested By `Siti Nurbaya`, Last Updated `2026-11-07T11:30:00Z`.
  - DU-011-4: pengajuan History Registration ID `REG-20261104-00009`, Group `Gudang 1` (path penuh `PT Sejahtera Abadi > Cabang A > Gudang 1`), Total Asset `12`, Status `Approved`, Requested By `Rina Wulandari`, Approver `Budi Santoso`, Last Updated `2026-11-04T15:30:00Z`.
  - DU-011-5: pengajuan History Registration ID `REG-20261103-00004`, Group `Kantor Pusat`, Total Asset `30`, Status `Partially Approved`, Requested By `Hadi Kusuma`, Approver `Agus Prasetyo`, Last Updated `2026-11-03T10:12:00Z`.
  - DU-011-6: pengajuan History Registration ID `REG-20261102-00001`, Group `Gudang 1`, Total Asset `5`, Status `Rejected`, Requested By `Rina Wulandari`, Approver `Budi Santoso`, Last Updated `2026-11-02T09:48:00Z`.
  - DU-011-7: pengajuan History Registration ID `REG-20261101-00006`, Group `Gudang 1`, Total Asset `8`, Status `Canceled`, Requested By `Rina Wulandari`, Approver `—`, Last Updated `2026-11-01T17:05:00Z`.
  - DU-011-8: pengajuan History auto-approve Kondisi A (pengaju Total Control) Registration ID `REG-20261031-00005`, Group `Gudang 2`, Total Asset `6`, Status `Approved`, Requested By `Siti Nurbaya`, Approver `Siti Nurbaya`, Last Updated `2026-10-31T09:00:00Z`.
  - DU-011-9: pengajuan History auto-approve Kondisi B (tanpa approver independen) Registration ID `REG-20261030-00003`, Group `Gudang 2`, Total Asset `4`, Status `Approved`, Requested By `Hadi Kusuma`, Approver `System`, Last Updated `2026-10-30T08:30:00Z`.
  - DU-011-11: pengajuan History approval OFF Registration ID `REG-20261031-00007`, Group `Gudang 1`, Total Asset `7`, Status `Approved`, Requested By `Hadi Kusuma`, Approver `—`, Last Updated `2026-10-31T12:15:00Z`.
  - DU-011-10: kata kunci Search `Gudang Fiktif` yang tidak cocok dengan pengajuan mana pun.
  - Requested By dan Approver yang diharapkan: `Rina W.` dari `Rina Wulandari`; `Hadi K.` dari `Hadi Kusuma`; `Siti N.` dari `Siti Nurbaya`; `Budi S.` dari `Budi Santoso`; `Agus P.` dari `Agus Prasetyo`.
  - Last Updated yang diharapkan dengan Date Format `dd/MM/yy`: `09/11/26, 10:20` dari `2026-11-09T10:20:00Z`; `08/11/26, 14:02` dari `2026-11-08T14:02:00Z`; `07/11/26, 11:30` dari `2026-11-07T11:30:00Z`; `04/11/26, 15:30` dari `2026-11-04T15:30:00Z`; `03/11/26, 10:12` dari `2026-11-03T10:12:00Z`.
- Kondisi:
  - K1: tab Active berisi DU-011-1 sampai DU-011-3 sehingga hitungan tab `Active (3)`; tab History berisi DU-011-4 sampai DU-011-9 dan DU-011-11; Date Format General Settings `dd/MM/yy`, Time Format `24h`, Time Zone `UTC`.
  - K2: tab Active dan tab History kosong, belum ada pengajuan.
  - K3: tab Active berisi DU-011-1 dan tab History berisi DU-011-4; pencarian dengan kata kunci DU-011-10 tidak menghasilkan baris pada kedua tab.
  - K4: memuat antrean gagal karena error server pada tab yang dibuka.
  - K5: sama dengan K1; unduhan gagal karena error server.

## Test Steps

### Sidebar Approvals dan tab antrean
1. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
2. Verifikasi induk `Approvals` tampil pada sidebar
3. Verifikasi anak `Registration` tampil di bawah induk `Approvals`
4. Klik `Approvals` pada sidebar
5. Verifikasi induk `Approvals` tetap tampil pada sidebar
6. Verifikasi anak `Registration` tidak tampil saat induk `Approvals` ditutup
7. Klik `Approvals` pada sidebar
8. Verifikasi anak `Registration` tampil kembali saat induk `Approvals` dibuka
9. Verifikasi tab `Active (3)` dan `History` tampil pada antrean Registration
10. Verifikasi toolbar dan tabel antrean tampil di bawah tab

### Tab antrean awal adalah Active
11. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
12. Verifikasi tab `Active (3)` terpilih saat pertama masuk
13. Verifikasi baris `REG-20261109-00003` tampil pada tabel tab Active

### Struktur halaman antrean mengikuti Breadcrumb dan SectionCard
14. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
15. Verifikasi Breadcrumb tampil di luar `SectionCard`
16. Verifikasi Page Title Header terpisah di bawah Breadcrumb tidak tampil
17. Verifikasi tabel antrean dibungkus `SectionCard`
18. Verifikasi jarak antara Breadcrumb dan `SectionCard` adalah `12px`
19. Verifikasi panel pohon Group di samping tabel tidak tampil pada halaman antrean

### Breadcrumb tab Active
20. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
21. Verifikasi Breadcrumb `Approvals > Registration > Active`
22. Verifikasi segmen `Approvals` tampil sebagai label statis, bukan link
23. Verifikasi segmen `Registration` tampil sebagai link
24. Verifikasi segmen `Active` tampil sebagai label statis, bukan link

### Breadcrumb mengikuti tab History dan tautan Registration kembali ke tab awal
25. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
26. Klik tab `History`
27. Verifikasi Breadcrumb `Approvals > Registration > History`
28. Verifikasi segmen `History` tampil sebagai label statis, bukan link
29. Klik segmen `Registration` pada Breadcrumb
30. Verifikasi tab `Active (3)` terpilih
31. Verifikasi Breadcrumb `Approvals > Registration > Active`

### Kolom antrean tab Active
32. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
33. Verifikasi header kolom `Registration ID`, `Group`, `Total Asset`, `Requested By`, dan `Last Updated` tampil berurutan pada antrean tab Active
34. Verifikasi kolom `Status` dan `Approver` tidak tampil pada antrean tab Active

### Sortable, berpaginasi, dan tanpa Bulk Action pada antrean tab Active
35. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
36. Verifikasi baris pertama antrean tab Active adalah `REG-20261109-00003` dan baris terakhir adalah `REG-20261107-00002`
37. Verifikasi ukuran halaman terpilih antrean tab Active adalah `10`
38. Verifikasi pilihan ukuran halaman antrean tab Active `10`, `25`, `50`, dan `100` tersedia
39. Verifikasi baris `REG-20261109-00003` tampil pada antrean tab Active
40. Verifikasi kolom checkbox pada antrean tab Active tidak tampil

### Registration ID tampil sebagai link pada antrean tab Active
41. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
42. Verifikasi sel Registration ID baris pertama menampilkan `REG-20261109-00003` sebagai link pada antrean tab Active
43. Verifikasi sel Registration ID baris kedua menampilkan `REG-20261108-00011` sebagai link pada antrean tab Active
44. Verifikasi sel Registration ID baris ketiga menampilkan `REG-20261107-00002` sebagai link pada antrean tab Active

### Group tampil sebagai badge dengan path penuh saat hover pada antrean tab Active
45. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
46. Verifikasi sel Group pada baris `REG-20261109-00003` menampilkan badge `Gudang 1`
47. Arahkan kursor ke badge Group `Gudang 1` pada baris `REG-20261109-00003`
48. Verifikasi tooltip menampilkan path penuh `PT Sejahtera Abadi > Cabang A > Gudang 1` pada antrean tab Active
49. Verifikasi sel Group pada baris `REG-20261108-00011` menampilkan badge `Kantor Pusat`
50. Verifikasi sel Group pada baris `REG-20261107-00002` menampilkan badge `Gudang 2`

### Total Asset tampil sebagai bilangan bulat pada antrean tab Active
51. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
52. Verifikasi sel Total Asset pada baris `REG-20261109-00003` menampilkan `12`
53. Verifikasi sel Total Asset pada baris `REG-20261108-00011` menampilkan `30`
54. Verifikasi sel Total Asset pada baris `REG-20261107-00002` menampilkan `5`

### Requested By tampil sebagai nama singkat dan nama lengkap saat hover pada antrean tab Active
55. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
56. Verifikasi sel Requested By pada baris `REG-20261109-00003` menampilkan `Rina W.`[^drift-1]
57. Arahkan kursor ke sel Requested By pada baris `REG-20261109-00003`
58. Verifikasi tooltip menampilkan nama lengkap `Rina Wulandari` pada antrean tab Active
59. Verifikasi sel Requested By pada baris `REG-20261108-00011` menampilkan `Hadi K.`[^drift-1]
60. Arahkan kursor ke sel Requested By pada baris `REG-20261108-00011`
61. Verifikasi tooltip menampilkan nama lengkap `Hadi Kusuma` pada antrean tab Active
62. Verifikasi sel Requested By pada baris `REG-20261107-00002` menampilkan `Siti N.`[^drift-1]
63. Arahkan kursor ke sel Requested By pada baris `REG-20261107-00002`
64. Verifikasi tooltip menampilkan nama lengkap `Siti Nurbaya` pada antrean tab Active

### Last Updated mengikuti General Settings pada antrean tab Active
65. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
66. Verifikasi sel Last Updated pada baris `REG-20261109-00003` menampilkan `09/11/26, 10:20`
67. Verifikasi sel Last Updated pada baris `REG-20261108-00011` menampilkan `08/11/26, 14:02`
68. Verifikasi sel Last Updated pada baris `REG-20261107-00002` menampilkan `07/11/26, 11:30`

### Toolbar antrean tanpa tombol aksi
69. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
70. Klik ikon Search pada toolbar
71. Verifikasi placeholder kotak Search pada antrean tab Active adalah `Search registration ID, group...`
72. Verifikasi toolbar antrean tab Active memuat `Filter`
73. Verifikasi toolbar antrean tab Active memuat `Download`
74. Klik `Download`
75. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil pada antrean tab Active
76. Verifikasi toolbar antrean tab Active tidak memuat tombol `[+ Register Asset]`

### Nama berkas Download antrean Approvals
77. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K5
78. Klik `Download`
79. Klik `Download as CSV`
80. Verifikasi toast `Error, failed to download Approvals-Registration.`

### Tanpa filter aktif saat pertama dibuka pada antrean tab Active
81. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
82. Verifikasi ikon Filter tampil pada toolbar antrean tab Active
83. Verifikasi badge titik pada ikon Filter antrean tab Active tidak tampil

### Field filter antrean tab Active
84. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
85. Klik ikon Filter pada toolbar
86. Verifikasi field `Group` berupa `Tree picker` dengan placeholder `All groups` pada antrean tab Active
87. Verifikasi field `Total Asset` berupa rentang `Min/Max` dengan placeholder `Min` dan `Max` pada antrean tab Active
88. Verifikasi field `Requested By` berupa `Multi-select searchable` dengan placeholder `All users` pada antrean tab Active
89. Verifikasi field `Last Updated` berupa `Date range picker` dengan placeholder `Select date` pada antrean tab Active
90. Verifikasi field filter `Registration ID` tidak tampil pada antrean tab Active

### Column Visibility dan Setup Column pada antrean tab Active
91. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
92. Klik header kolom Actions `⋯`
93. Verifikasi panel Column Visibility pada antrean tab Active memuat kolom `Registration ID`, `Group`, `Total Asset`, `Requested By`, dan `Last Updated`
94. Verifikasi panel memuat `Setup Column...`
95. Klik `Setup Column...`
96. Verifikasi modal `Setup Column` tampil pada antrean tab Active
97. Verifikasi daftar kolom pada modal memuat `Registration ID`, `Group`, `Total Asset`, `Requested By`, dan `Last Updated`
98. Verifikasi daftar kolom pada modal tidak memuat baris `Checkbox` dan `Actions`

### Menyembunyikan kolom tidak menghapus field filter dan filter ter-Apply pada antrean tab Active
99. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
100. Klik ikon Filter pada toolbar
101. Pilih opsi `Siti Nurbaya` pada field `Requested By`
102. Klik `[Apply]`
103. Verifikasi baris `REG-20261107-00002` tampil pada antrean tab Active
104. Verifikasi baris `REG-20261109-00003` tidak tampil pada antrean tab Active
105. Klik header kolom Actions `⋯`
106. Hilangkan centang kolom `Requested By` pada panel Column Visibility
107. Klik ikon Filter pada toolbar
108. Verifikasi field berlabel `Requested By` tampil pada panel Filter antrean tab Active
109. Verifikasi chip `Siti Nurbaya` tampil pada field `Requested By` antrean tab Active
110. Verifikasi baris `REG-20261109-00003` tetap tidak tampil pada antrean tab Active

### Empty state alami pada antrean tab Active
111. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K2
112. Verifikasi ilustrasi empty state antrean tab Active tampil
113. Verifikasi judul empty state `No pending approvals`
114. Verifikasi deskripsi empty state `You have no pending approval requests at this moment.`

### Empty state akibat Search tanpa hasil pada antrean tab Active
115. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K3
116. Klik ikon Search pada toolbar
117. Ketik Search `Gudang Fiktif`, tekan Enter
118. Verifikasi judul empty state `No results found` pada antrean tab Active
119. Verifikasi deskripsi empty state `Try adjusting your search or filter.` pada antrean tab Active
120. Verifikasi ilustrasi empty state hasil pencarian antrean tab Active tampil
121. Verifikasi judul `No pending approvals` tidak tampil saat hasil pencarian kosong

### Gagal muat bukan empty state pada antrean tab Active
122. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K4
123. Verifikasi pesan `Unable to load this data.` pada antrean tab Active
124. Verifikasi tombol `[Try Again]` tampil pada antrean tab Active
125. Verifikasi judul `No pending approvals` tidak tampil saat gagal muat

### Kolom antrean tab History
126. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
127. Klik tab `History`
128. Verifikasi header kolom `Registration ID`, `Group`, `Total Asset`, `Status`, `Requested By`, `Approver`, dan `Last Updated` tampil berurutan pada antrean tab History

### Sortable, berpaginasi, dan tanpa Bulk Action pada antrean tab History
129. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
130. Klik tab `History`
131. Verifikasi baris pertama antrean tab History adalah `REG-20261104-00009` dan baris terakhir adalah `REG-20261030-00003`
132. Verifikasi ukuran halaman terpilih antrean tab History adalah `10`
133. Verifikasi pilihan ukuran halaman antrean tab History `10`, `25`, `50`, dan `100` tersedia
134. Verifikasi baris `REG-20261104-00009` tampil pada antrean tab History
135. Verifikasi kolom checkbox pada antrean tab History tidak tampil

### Registration ID tampil sebagai link pada antrean tab History
136. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
137. Klik tab `History`
138. Verifikasi sel Registration ID baris pertama menampilkan `REG-20261104-00009` sebagai link pada antrean tab History
139. Verifikasi sel Registration ID baris kedua menampilkan `REG-20261103-00004` sebagai link pada antrean tab History

### Group tampil sebagai badge dengan path penuh saat hover pada antrean tab History
140. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
141. Klik tab `History`
142. Verifikasi sel Group pada baris `REG-20261104-00009` menampilkan badge `Gudang 1`
143. Arahkan kursor ke badge Group `Gudang 1` pada baris `REG-20261104-00009`
144. Verifikasi tooltip menampilkan path penuh `PT Sejahtera Abadi > Cabang A > Gudang 1` pada antrean tab History
145. Verifikasi sel Group pada baris `REG-20261103-00004` menampilkan badge `Kantor Pusat`

### Total Asset tampil sebagai bilangan bulat pada antrean tab History
146. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
147. Klik tab `History`
148. Verifikasi sel Total Asset pada baris `REG-20261104-00009` menampilkan `12`
149. Verifikasi sel Total Asset pada baris `REG-20261103-00004` menampilkan `30`
150. Verifikasi sel Total Asset pada baris `REG-20261102-00001` menampilkan `5`

### Status tampil sebagai badge berwarna dengan teks pada antrean tab History
151. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
152. Klik tab `History`
153. Verifikasi sel Status pada baris `REG-20261104-00009` menampilkan badge `Approved` dengan `severity="success"`
154. Verifikasi sel Status pada baris `REG-20261103-00004` menampilkan badge `Partially Approved` dengan `severity="warning"`
155. Verifikasi sel Status pada baris `REG-20261102-00001` menampilkan badge `Rejected` dengan `severity="danger"`
156. Verifikasi sel Status pada baris `REG-20261101-00006` menampilkan badge `Canceled` dengan severity `dark`

### Requested By tampil sebagai nama singkat dan nama lengkap saat hover pada antrean tab History
157. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
158. Klik tab `History`
159. Verifikasi sel Requested By pada baris `REG-20261104-00009` menampilkan `Rina W.`[^drift-1]
160. Arahkan kursor ke sel Requested By pada baris `REG-20261104-00009`
161. Verifikasi tooltip menampilkan nama lengkap `Rina Wulandari` pada antrean tab History
162. Verifikasi sel Requested By pada baris `REG-20261103-00004` menampilkan `Hadi K.`[^drift-1]
163. Arahkan kursor ke sel Requested By pada baris `REG-20261103-00004`
164. Verifikasi tooltip menampilkan nama lengkap `Hadi Kusuma` pada antrean tab History

### Approver tampil sebagai nama singkat, nama lengkap saat hover, dan nilai kosong pada antrean tab History
165. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
166. Klik tab `History`
167. Verifikasi sel Approver pada baris `REG-20261104-00009` menampilkan `Budi S.`[^drift-1]
168. Arahkan kursor ke sel Approver pada baris `REG-20261104-00009`
169. Verifikasi tooltip menampilkan nama lengkap `Budi Santoso` pada antrean tab History
170. Verifikasi sel Approver pada baris `REG-20261103-00004` menampilkan `Agus P.`[^drift-1]
171. Arahkan kursor ke sel Approver pada baris `REG-20261103-00004`
172. Verifikasi tooltip menampilkan nama lengkap `Agus Prasetyo` pada antrean tab History
173. Verifikasi sel Approver pada baris auto-approve `REG-20261031-00005` menampilkan `Siti N.`[^drift-1]
174. Verifikasi sel Approver pada baris auto-approve `REG-20261030-00003` menampilkan `System`
175. Verifikasi sel Approver pada baris Canceled `REG-20261101-00006` menampilkan `—`

### Last Updated mengikuti General Settings pada antrean tab History
176. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
177. Klik tab `History`
178. Verifikasi sel Last Updated pada baris `REG-20261104-00009` menampilkan `04/11/26, 15:30`
179. Verifikasi sel Last Updated pada baris `REG-20261103-00004` menampilkan `03/11/26, 10:12`

### Toolbar antrean tab History
180. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
181. Klik tab `History`
182. Klik ikon Search pada toolbar
183. Verifikasi placeholder kotak Search pada antrean tab History adalah `Search registration ID, group...`
184. Verifikasi toolbar antrean tab History memuat `Filter`
185. Verifikasi toolbar antrean tab History memuat `Download`
186. Verifikasi toolbar antrean tab History tidak memuat tombol `[+ Register Asset]`

### Tanpa filter aktif saat pertama dibuka pada antrean tab History
187. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
188. Klik tab `History`
189. Verifikasi ikon Filter tampil pada toolbar antrean tab History
190. Verifikasi badge titik pada ikon Filter antrean tab History tidak tampil

### Field filter antrean tab History
191. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
192. Klik tab `History`
193. Klik ikon Filter pada toolbar
194. Verifikasi field `Group` berupa `Multi-select searchable` dengan placeholder `All groups` pada antrean tab History
195. Verifikasi field `Total Asset` berupa rentang `Min/Max` dengan placeholder `Min` dan `Max` pada antrean tab History
196. Verifikasi field `Status` berupa `Multi-select searchable` dengan placeholder `All statuses` pada antrean tab History
197. Verifikasi field `Requested By` berupa `Multi-select searchable` dengan placeholder `All users` pada antrean tab History
198. Verifikasi field `Approver` berupa `Multi-select searchable` dengan placeholder `All users` pada antrean tab History
199. Verifikasi field `Last Updated` berupa `Date range picker` dengan placeholder `Select date` pada antrean tab History
200. Verifikasi field filter `Registration ID` tidak tampil pada antrean tab History

### Column Visibility dan Setup Column pada antrean tab History
201. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
202. Klik tab `History`
203. Klik header kolom Actions `⋯`
204. Verifikasi panel Column Visibility pada antrean tab History memuat kolom `Registration ID`, `Group`, `Total Asset`, `Status`, `Requested By`, `Approver`, dan `Last Updated`
205. Verifikasi panel memuat `Setup Column...`
206. Klik `Setup Column...`
207. Verifikasi modal `Setup Column` tampil pada antrean tab History
208. Verifikasi daftar kolom pada modal memuat `Registration ID`, `Group`, `Total Asset`, `Status`, `Requested By`, `Approver`, dan `Last Updated`
209. Verifikasi daftar kolom pada modal tidak memuat baris `Checkbox` dan `Actions`

### Menyembunyikan kolom tidak menghapus field filter dan filter ter-Apply pada antrean tab History
210. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
211. Klik tab `History`
212. Klik ikon Filter pada toolbar
213. Pilih opsi `Rejected` pada field `Status`
214. Klik `[Apply]`
215. Verifikasi baris `REG-20261102-00001` tampil pada antrean tab History
216. Verifikasi baris `REG-20261104-00009` tidak tampil pada antrean tab History
217. Klik header kolom Actions `⋯`
218. Hilangkan centang kolom `Status` pada panel Column Visibility
219. Klik ikon Filter pada toolbar
220. Verifikasi field berlabel `Status` tampil pada panel Filter antrean tab History
221. Verifikasi chip `Rejected` tampil pada field `Status` antrean tab History
222. Verifikasi baris `REG-20261104-00009` tetap tidak tampil pada antrean tab History

### Empty state alami pada antrean tab History
223. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K2
224. Klik tab `History`
225. Verifikasi ilustrasi empty state antrean tab History tampil
226. Verifikasi judul empty state `No history yet` pada antrean tab History
227. Verifikasi deskripsi empty state `Decided or canceled registrations will appear here.` pada antrean tab History
228. Verifikasi deskripsi bergaya Entity Listing `Get started by creating your first [Entity].` tidak tampil pada antrean tab History

### Empty state akibat Search tanpa hasil pada antrean tab History
229. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K3
230. Klik tab `History`
231. Klik ikon Search pada toolbar
232. Ketik Search `Gudang Fiktif`, tekan Enter
233. Verifikasi judul empty state `No results found` pada antrean tab History
234. Verifikasi deskripsi empty state `Try adjusting your search or filter.` pada antrean tab History
235. Verifikasi ilustrasi empty state hasil pencarian antrean tab History tampil
236. Verifikasi judul `No history yet` pada antrean tab History tidak tampil saat hasil pencarian kosong

### Gagal muat bukan empty state pada antrean tab History
237. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K4
238. Klik tab `History`
239. Verifikasi pesan `Unable to load this data.` pada antrean tab History
240. Verifikasi tombol `[Try Again]` tampil pada antrean tab History
241. Verifikasi judul `No history yet` pada antrean tab History tidak tampil saat gagal muat

### SectionCard antrean tidak dapat dibuka atau ditutup
242. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
243. Verifikasi tabel antrean tampil di dalam `SectionCard`
244. Verifikasi `SectionCard` tidak memiliki kontrol untuk membuka atau menutup isinya

### Approver kosong pada pengajuan approval OFF di antrean tab History
245. Tampilkan Menu `Approvals` > `Registration` dengan kondisi K1
246. Klik tab `History`
247. Verifikasi sel Approver pada baris approval OFF `REG-20261031-00007` menampilkan `—`

[^drift-1]: Drift PRD vs foundation vs override. PRD §4.1 kolom Requested By dan Approver: `Nama singkat`. foundation `prd-conventions.md` §9.13: nama singkat `[First Name] [Last Initial]`, contoh tanpa titik (`John L`, `Alexander G`). Override O-4: nama singkat mengakhiri inisial dengan titik (`John L.`, `Alexander G.`). Diasersi: O-4, karena override menang atas foundation (SB-6).

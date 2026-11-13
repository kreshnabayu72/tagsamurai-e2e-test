---
id: TC-FA-FAREG-UI-010-pengajuan-tampilan-kolom-state
title: "Sub tab Waiting for Approval dan History: kolom, toolbar, dan state tabel"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["S-REG-02", "S-REG-03", "§4.1#r3", "§4.1#p4", "§4.1#p11", "§4.1#r38", "§4.1#r39", "§4.1#r40", "§4.1#r41", "§4.1#r42", "§4.1#p15", "§4.1#r46", "§4.1#r47", "§4.1#r48", "§4.1#r49", "§4.1#r50", "§4.1#r51", "§4.1#r52", "§5#r1", "§5#r2", "§5#r5", "§7.1#p1", "§9.5#r8", "EB-FLT-6@tabel-history", "EB-FLT-6@tabel-waiting-for-approval", "EB-TBL-1@tabel-history", "EB-TBL-1@tabel-waiting-for-approval", "EB-TBL-2@kolom-approver", "EB-TBL-4@kolom-approver"]
smoke: []
dependsOn: []
trace:
  S-REG-02: [79, 80, 85, 86]
  S-REG-03: [183, 184, 189, 190]
  "§4.1#r3": [2, 6, 8, 93, 95, 97]
  "§4.1#p4": [61, 62, 64, 65, 66, 165, 166, 168, 169, 170]
  "§4.1#p11": [2, 3, 5]
  "§4.1#r38": [14, 15, 16, 58]
  "§4.1#r39": [18, 20, 21, 22, 54]
  "§4.1#r40": [24, 25, 26, 55]
  "§4.1#r41": [28, 30, 31, 33, 34, 36, 56]
  "§4.1#r42": [7, 38, 39, 57]
  "§4.1#p15": 93
  "§4.1#r46": [103, 104, 162]
  "§4.1#r47": [106, 108, 109, 110, 156]
  "§4.1#r48": [112, 113, 114, 157]
  "§4.1#r49": [116, 117, 118, 119, 158]
  "§4.1#r50": [121, 123, 124, 126, 159]
  "§4.1#r51": [128, 130, 131, 133, 134, 136, 137, 138, 160]
  "§4.1#r52": [96, 140, 141, 161]
  "§5#r1": [42, 43, 44, 46, 47, 48, 144, 145, 146, 148, 149, 150]
  "§5#r2": [9, 10, 98, 99]
  "§5#r5": [12, 101]
  "§7.1#p1": [80, 81, 184, 185]
  "§9.5#r8": [51, 153]
  EB-FLT-6@tabel-history: [176, 179, 180, 181]
  EB-FLT-6@tabel-waiting-for-approval: [72, 75, 76, 77]
  EB-TBL-1@tabel-history: [183, 189, 191, 193, 194, 195]
  EB-TBL-1@tabel-waiting-for-approval: [79, 85, 87, 89, 90, 91]
  EB-TBL-2@kolom-approver: [137, 138]
  EB-TBL-4@kolom-approver: [128, 130, 131, 133, 134, 136]
anchor: [11, 50, 71, 100, 152, 175]
coverage:
  web: automated
---

# Sub tab Waiting for Approval dan History: kolom, toolbar, dan state tabel

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Waiting for Approval.
- Komponen: Sub tab `Waiting for Approval` dan `History` (TBL-REG-02)
- Data:
  - DU-010-1: pengajuan Waiting for Approval Registration ID `REG-20261109-00001`, Group `Gudang 1` (path penuh `PT Sejahtera Abadi > Cabang A > Gudang 1`), Total Asset `12`, Requested By `Budi`, Last Updated `2026-11-12T09:15:00Z`.
  - DU-010-2: pengajuan Waiting for Approval Registration ID `REG-20261108-00004`, Group `Gudang 2`, Total Asset `5`, Requested By `Siti Nurbaya`, Last Updated `2026-11-11T23:30:00Z`.
  - DU-010-3: pengajuan Waiting for Approval Registration ID `REG-20261107-00002`, Group `Kantor Pusat`, Total Asset `30`, Requested By `Alexander Graham Bell`, Last Updated `2026-11-10T09:05:00Z`.
  - DU-010-4: pengajuan History Registration ID `REG-20261105-00007`, Group `Gudang 1` (path penuh `PT Sejahtera Abadi > Cabang A > Gudang 1`), Total Asset `12`, Status `Approved`, Requested By `Budi`, Approver `Dewi Anggraini`, Last Updated `2026-11-12T09:15:00Z`.
  - DU-010-5: pengajuan History Registration ID `REG-20261104-00003`, Group `Gudang 2`, Total Asset `5`, Status `Partially Approved`, Requested By `Siti Nurbaya`, Approver `Dewi Anggraini`, Last Updated `2026-11-11T23:30:00Z`.
  - DU-010-6: pengajuan History Registration ID `REG-20261103-00002`, Group `Kantor Pusat`, Total Asset `30`, Status `Rejected`, Requested By `Alexander Graham Bell`, Approver `Buzzlightyear Sumardi`, Last Updated `2026-11-10T09:05:00Z`.
  - DU-010-7: pengajuan History Registration ID `REG-20261102-00001`, Group `Gudang 4`, Total Asset `8`, Status `Canceled`, Requested By `Budi`, Approver `—`, Last Updated `2026-11-09T13:10:00Z`.
  - DU-010-8: pengajuan History auto-approve Kondisi A (pengaju Total Control) Registration ID `REG-20261101-00005`, Group `Gudang 5`, Total Asset `6`, Status `Approved`, Requested By `Hadi Kusuma`, Approver `Hadi Kusuma`, Last Updated `2026-11-08T10:00:00Z`.
  - DU-010-10: kata kunci Search `Gudang Fiktif` yang tidak cocok dengan pengajuan mana pun.
  - DU-010-11: pengajuan History approval OFF Registration ID `REG-20261030-00002`, Group `Gudang 6`, Total Asset `7`, Status `Approved`, Requested By `Budi`, Approver `—`, Last Updated `2026-11-06T14:45:00Z`.
  - Requested By dan Approver yang diharapkan: `Budi` dari `Budi`; `Siti N` dari `Siti Nurbaya`; `Alexander G` dari `Alexander Graham Bell`; `Dewi A` dari `Dewi Anggraini`; `Buzzlightyear S` dari `Buzzlightyear Sumardi`; `Hadi K` dari `Hadi Kusuma`. Nama tanpa last name (`Budi`) tidak memuat inisial.
  - Last Updated yang diharapkan dengan Date Format `dd/MM/yy`: `12/11/26, 09:15` dari `2026-11-12T09:15:00Z`; `11/11/26, 23:30` dari `2026-11-11T23:30:00Z`.
- Kondisi:
  - K1: sub tab Waiting for Approval berisi DU-010-1 sampai DU-010-3; Date Format General Settings `dd/MM/yy`, Time Format `24h`, Time Zone `UTC`.
  - K2: sub tab History berisi DU-010-4 sampai DU-010-8 dan DU-010-11; Date Format General Settings `dd/MM/yy`, Time Format `24h`, Time Zone `UTC`.
  - K3: sub tab Waiting for Approval kosong, belum ada pengajuan.
  - K4: sub tab Waiting for Approval berisi DU-010-1; pencarian dengan kata kunci DU-010-10 tidak menghasilkan baris.
  - K5: sub tab History kosong, belum ada riwayat.
  - K6: sub tab History berisi DU-010-4; pencarian dengan kata kunci DU-010-10 tidak menghasilkan baris.
  - K7: memuat sub tab Waiting for Approval gagal karena error server.
  - K8: memuat sub tab History gagal karena error server.

## Test Steps

### Kolom tabel Waiting for Approval dan tanpa kolom Status
1. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K1
2. Verifikasi header kolom `Registration ID`, `Group`, `Total Asset`, `Requested By`, dan `Last Updated` tampil berurutan pada sub tab Waiting for Approval
3. Verifikasi kolom `Status` pada sub tab Waiting for Approval tidak tampil

### Satu baris per pengajuan, sortable, berpaginasi, dan tanpa Bulk Action pada Waiting for Approval
4. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K1
5. Verifikasi sub tab Waiting for Approval menampilkan tiga baris, satu baris per Registration ID
6. Verifikasi header kolom `Last Updated` pada sub tab Waiting for Approval memiliki ikon sort
7. Verifikasi baris pertama sub tab Waiting for Approval adalah `REG-20261109-00001` dan baris terakhir adalah `REG-20261107-00002`
8. Verifikasi kontrol paginasi sub tab Waiting for Approval tampil di bawah tabel
9. Verifikasi ukuran halaman terpilih sub tab Waiting for Approval adalah `10`
10. Verifikasi pilihan ukuran halaman sub tab Waiting for Approval `10`, `25`, `50`, dan `100` tersedia
11. Verifikasi baris `REG-20261109-00001` tampil pada sub tab Waiting for Approval
12. Verifikasi kolom checkbox pada sub tab Waiting for Approval tidak tampil

### Registration ID tampil sebagai link pada Waiting for Approval
13. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K1
14. Verifikasi sel Registration ID baris pertama menampilkan `REG-20261109-00001` sebagai link
15. Verifikasi sel Registration ID baris kedua menampilkan `REG-20261108-00004` sebagai link
16. Verifikasi sel Registration ID baris ketiga menampilkan `REG-20261107-00002` sebagai link

### Group tampil sebagai badge dengan path penuh saat hover pada Waiting for Approval
17. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K1
18. Verifikasi sel Group pada baris `REG-20261109-00001` menampilkan badge `Gudang 1`
19. Arahkan kursor ke badge Group `Gudang 1` pada baris `REG-20261109-00001`
20. Verifikasi tooltip menampilkan path penuh `PT Sejahtera Abadi > Cabang A > Gudang 1`
21. Verifikasi sel Group pada baris `REG-20261108-00004` menampilkan badge `Gudang 2`
22. Verifikasi sel Group pada baris `REG-20261107-00002` menampilkan badge `Kantor Pusat`

### Total Asset tampil sebagai bilangan bulat pada Waiting for Approval
23. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K1
24. Verifikasi sel Total Asset pada baris `REG-20261109-00001` menampilkan `12`
25. Verifikasi sel Total Asset pada baris `REG-20261108-00004` menampilkan `5`
26. Verifikasi sel Total Asset pada baris `REG-20261107-00002` menampilkan `30`

### Requested By tampil sebagai nama singkat dan nama lengkap saat hover pada Waiting for Approval
27. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K1
28. Verifikasi sel Requested By pada baris `REG-20261109-00001` menampilkan `Budi`
29. Arahkan kursor ke sel Requested By pada baris `REG-20261109-00001`
30. Verifikasi tooltip menampilkan nama lengkap `Budi`
31. Verifikasi sel Requested By pada baris `REG-20261108-00004` menampilkan `Siti N`
32. Arahkan kursor ke sel Requested By pada baris `REG-20261108-00004`
33. Verifikasi tooltip menampilkan nama lengkap `Siti Nurbaya`
34. Verifikasi sel Requested By pada baris `REG-20261107-00002` menampilkan `Alexander G`
35. Arahkan kursor ke sel Requested By pada baris `REG-20261107-00002`
36. Verifikasi tooltip menampilkan nama lengkap `Alexander Graham Bell`

### Last Updated mengikuti General Settings pada Waiting for Approval
37. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K1
38. Verifikasi sel Last Updated pada baris `REG-20261109-00001` menampilkan `12/11/26, 09:15`
39. Verifikasi sel Last Updated pada baris `REG-20261108-00004` menampilkan `11/11/26, 23:30`

### Toolbar sub tab Waiting for Approval
40. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K1
41. Klik ikon Search pada toolbar
42. Verifikasi placeholder kotak Search pada sub tab Waiting for Approval adalah `Search registration ID, group...`
43. Verifikasi toolbar sub tab Waiting for Approval memuat `Filter`
44. Verifikasi toolbar sub tab Waiting for Approval memuat `Download`
45. Klik `Download`
46. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil pada sub tab Waiting for Approval
47. Verifikasi toolbar sub tab Waiting for Approval memuat `[+ Register Asset]`
48. Verifikasi toolbar sub tab Waiting for Approval tidak memuat tombol `Changelog`

### Tanpa filter aktif saat pertama dibuka pada Waiting for Approval
49. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K1
50. Verifikasi ikon Filter tampil pada toolbar sub tab Waiting for Approval
51. Verifikasi badge titik pada ikon Filter sub tab Waiting for Approval tidak tampil

### Field filter sub tab Waiting for Approval
52. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K1
53. Klik ikon Filter pada toolbar
54. Verifikasi field `Group` berupa `Tree picker` dengan placeholder `All groups`
55. Verifikasi field `Total Asset` berupa rentang `Min/Max` dengan placeholder `Min` dan `Max`
56. Verifikasi field `Requested By` berupa `Multi-select searchable` dengan placeholder `All users`
57. Verifikasi field `Last Updated` berupa `Date range picker` dengan placeholder `Select date`
58. Verifikasi field filter `Registration ID` tidak tampil pada sub tab Waiting for Approval

### Column Visibility dan Setup Column pada Waiting for Approval
59. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K1
60. Klik header kolom Actions `⋯`
61. Verifikasi panel Column Visibility pada sub tab Waiting for Approval memuat kolom `Registration ID`, `Group`, `Total Asset`, `Requested By`, dan `Last Updated`
62. Verifikasi panel memuat `Setup Column...`
63. Klik `Setup Column...`
64. Verifikasi modal `Setup Column` tampil pada sub tab Waiting for Approval
65. Verifikasi daftar kolom pada modal memuat `Registration ID`, `Group`, `Total Asset`, `Requested By`, dan `Last Updated`
66. Verifikasi daftar kolom pada modal tidak memuat baris `Checkbox` dan `Actions`

### Menyembunyikan kolom tidak menghapus field filter dan filter ter-Apply pada Waiting for Approval
67. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K1
68. Klik ikon Filter pada toolbar
69. Pilih opsi `Siti Nurbaya` pada field `Requested By`
70. Klik `[Apply]`
71. Verifikasi baris `REG-20261108-00004` tampil pada sub tab Waiting for Approval
72. Verifikasi baris `REG-20261109-00001` tidak tampil pada sub tab Waiting for Approval
73. Klik header kolom Actions `⋯`
74. Hilangkan centang kolom `Requested By` pada panel Column Visibility
75. Verifikasi field berlabel `Requested By` tampil pada panel Filter sub tab Waiting for Approval
76. Verifikasi chip `Siti Nurbaya` tampil pada field `Requested By` sub tab Waiting for Approval
77. Verifikasi baris `REG-20261109-00001` tetap tidak tampil pada sub tab Waiting for Approval

### Empty state alami pada Waiting for Approval
78. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K3
79. Verifikasi judul empty state `No requests waiting for approval`
80. Verifikasi deskripsi empty state `Submitted registrations that need a decision will appear here.`
81. Verifikasi deskripsi bergaya Entity Listing `Get started by creating your first [Entity].` tidak tampil pada sub tab Waiting for Approval

### Empty state akibat Search tanpa hasil pada Waiting for Approval
82. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K4
83. Klik ikon Search pada toolbar
84. Ketik Search `Gudang Fiktif`, tekan Enter
85. Verifikasi judul empty state `No results found` pada sub tab Waiting for Approval
86. Verifikasi deskripsi empty state `Try adjusting your search or filter.` pada sub tab Waiting for Approval
87. Verifikasi judul `No requests waiting for approval` tidak tampil saat hasil pencarian kosong

### Gagal muat bukan empty state pada Waiting for Approval
88. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K7
89. Verifikasi pesan `Unable to load this data.` pada sub tab Waiting for Approval
90. Verifikasi tombol `[Try Again]` tampil pada sub tab Waiting for Approval
91. Verifikasi judul `No requests waiting for approval` tidak tampil saat gagal muat

### Kolom tabel History
92. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K2
93. Verifikasi header kolom `Registration ID`, `Group`, `Total Asset`, `Status`, `Requested By`, `Approver`, dan `Last Updated` tampil berurutan pada sub tab History

### Sortable, berpaginasi, dan tanpa Bulk Action pada History
94. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K2
95. Verifikasi header kolom `Last Updated` pada sub tab History memiliki ikon sort
96. Verifikasi baris pertama sub tab History adalah `REG-20261105-00007` dan baris terakhir adalah `REG-20261030-00002`
97. Verifikasi kontrol paginasi sub tab History tampil di bawah tabel
98. Verifikasi ukuran halaman terpilih sub tab History adalah `10`
99. Verifikasi pilihan ukuran halaman sub tab History `10`, `25`, `50`, dan `100` tersedia
100. Verifikasi baris `REG-20261105-00007` tampil pada sub tab History
101. Verifikasi kolom checkbox pada sub tab History tidak tampil

### Registration ID tampil sebagai link pada History
102. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K2
103. Verifikasi sel Registration ID baris pertama menampilkan `REG-20261105-00007` sebagai link
104. Verifikasi sel Registration ID baris kedua menampilkan `REG-20261104-00003` sebagai link

### Group tampil sebagai badge dengan path penuh saat hover pada History
105. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K2
106. Verifikasi sel Group pada baris `REG-20261105-00007` menampilkan badge `Gudang 1`
107. Arahkan kursor ke badge Group `Gudang 1` pada baris `REG-20261105-00007`
108. Verifikasi tooltip menampilkan path penuh `PT Sejahtera Abadi > Cabang A > Gudang 1`
109. Verifikasi sel Group pada baris `REG-20261104-00003` menampilkan badge `Gudang 2`
110. Verifikasi sel Group pada baris `REG-20261103-00002` menampilkan badge `Kantor Pusat`

### Total Asset tampil sebagai bilangan bulat pada History
111. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K2
112. Verifikasi sel Total Asset pada baris `REG-20261105-00007` menampilkan `12`
113. Verifikasi sel Total Asset pada baris `REG-20261104-00003` menampilkan `5`
114. Verifikasi sel Total Asset pada baris `REG-20261103-00002` menampilkan `30`

### Status tampil sebagai badge berwarna dengan teks
115. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K2
116. Verifikasi sel Status pada baris `REG-20261105-00007` menampilkan badge `Approved` dengan `severity="success"`
117. Verifikasi sel Status pada baris `REG-20261104-00003` menampilkan badge `Partially Approved` dengan `severity="warning"`
118. Verifikasi sel Status pada baris `REG-20261103-00002` menampilkan badge `Rejected` dengan `severity="danger"`
119. Verifikasi sel Status pada baris `REG-20261102-00001` menampilkan badge `Canceled` dengan severity `dark`

### Requested By tampil sebagai nama singkat dan nama lengkap saat hover pada History
120. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K2
121. Verifikasi sel Requested By pada baris `REG-20261105-00007` menampilkan `Budi`
122. Arahkan kursor ke sel Requested By pada baris `REG-20261105-00007`
123. Verifikasi tooltip menampilkan nama lengkap `Budi`
124. Verifikasi sel Requested By pada baris `REG-20261103-00002` menampilkan `Alexander G`
125. Arahkan kursor ke sel Requested By pada baris `REG-20261103-00002`
126. Verifikasi tooltip menampilkan nama lengkap `Alexander Graham Bell`

### Approver tampil sebagai nama singkat, nama lengkap saat hover, dan nilai kosong
127. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K2
128. Verifikasi sel Approver pada baris `REG-20261105-00007` menampilkan `Dewi A`
129. Arahkan kursor ke sel Approver pada baris `REG-20261105-00007`
130. Verifikasi tooltip menampilkan nama lengkap `Dewi Anggraini`
131. Verifikasi sel Approver pada baris `REG-20261103-00002` menampilkan `Buzzlightyear S`
132. Arahkan kursor ke sel Approver pada baris `REG-20261103-00002`
133. Verifikasi tooltip menampilkan nama lengkap `Buzzlightyear Sumardi`
134. Verifikasi sel Approver pada baris pengajuan auto-approve `REG-20261101-00005` menampilkan `Hadi K`
135. Arahkan kursor ke sel Approver pada baris `REG-20261101-00005`
136. Verifikasi tooltip menampilkan nama lengkap `Hadi Kusuma`
137. Verifikasi sel Approver pada baris Canceled `REG-20261102-00001` menampilkan `—`
138. Verifikasi sel Approver pada baris approval OFF `REG-20261030-00002` menampilkan `—`

### Last Updated mengikuti General Settings pada History
139. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K2
140. Verifikasi sel Last Updated pada baris `REG-20261105-00007` menampilkan `12/11/26, 09:15`
141. Verifikasi sel Last Updated pada baris `REG-20261104-00003` menampilkan `11/11/26, 23:30`

### Toolbar sub tab History
142. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K2
143. Klik ikon Search pada toolbar
144. Verifikasi placeholder kotak Search pada sub tab History adalah `Search registration ID, group...`
145. Verifikasi toolbar sub tab History memuat `Filter`
146. Verifikasi toolbar sub tab History memuat `Download`
147. Klik `Download`
148. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil pada sub tab History
149. Verifikasi toolbar sub tab History memuat `[+ Register Asset]`
150. Verifikasi toolbar sub tab History tidak memuat tombol `Changelog`

### Tanpa filter aktif saat pertama dibuka pada History
151. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K2
152. Verifikasi ikon Filter tampil pada toolbar sub tab History
153. Verifikasi badge titik pada ikon Filter sub tab History tidak tampil

### Field filter sub tab History
154. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K2
155. Klik ikon Filter pada toolbar
156. Verifikasi field `Group` berupa `Multi-select searchable` dengan placeholder `All groups`
157. Verifikasi field `Total Asset` berupa rentang `Min/Max` dengan placeholder `Min` dan `Max`
158. Verifikasi field `Status` berupa `Multi-select searchable` dengan placeholder `All statuses`
159. Verifikasi field `Requested By` berupa `Multi-select searchable` dengan placeholder `All users`
160. Verifikasi field `Approver` berupa `Multi-select searchable` dengan placeholder `All users`
161. Verifikasi field `Last Updated` berupa `Date range picker` dengan placeholder `Select date`
162. Verifikasi field filter `Registration ID` tidak tampil pada sub tab History

### Column Visibility dan Setup Column pada History
163. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K2
164. Klik header kolom Actions `⋯`
165. Verifikasi panel Column Visibility pada sub tab History memuat kolom `Registration ID`, `Group`, `Total Asset`, `Status`, `Requested By`, `Approver`, dan `Last Updated`
166. Verifikasi panel memuat `Setup Column...`
167. Klik `Setup Column...`
168. Verifikasi modal `Setup Column` tampil pada sub tab History
169. Verifikasi daftar kolom pada modal memuat `Registration ID`, `Group`, `Total Asset`, `Status`, `Requested By`, `Approver`, dan `Last Updated`
170. Verifikasi daftar kolom pada modal tidak memuat baris `Checkbox` dan `Actions`

### Menyembunyikan kolom tidak menghapus field filter dan filter ter-Apply pada History
171. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K2
172. Klik ikon Filter pada toolbar
173. Pilih opsi `Rejected` pada field `Status`
174. Klik `[Apply]`
175. Verifikasi baris `REG-20261103-00002` tampil pada sub tab History
176. Verifikasi baris `REG-20261105-00007` tidak tampil pada sub tab History
177. Klik header kolom Actions `⋯`
178. Hilangkan centang kolom `Status` pada panel Column Visibility
179. Verifikasi field berlabel `Status` tampil pada panel Filter sub tab History
180. Verifikasi chip `Rejected` tampil pada field `Status` sub tab History
181. Verifikasi baris `REG-20261105-00007` tetap tidak tampil pada sub tab History

### Empty state alami pada History
182. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K5
183. Verifikasi judul empty state `No history yet`
184. Verifikasi deskripsi empty state `Decided or canceled registrations will appear here.`
185. Verifikasi deskripsi bergaya Entity Listing `Get started by creating your first [Entity].` tidak tampil pada sub tab History

### Empty state akibat Search tanpa hasil pada History
186. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K6
187. Klik ikon Search pada toolbar
188. Ketik Search `Gudang Fiktif`, tekan Enter
189. Verifikasi judul empty state `No results found` pada sub tab History
190. Verifikasi deskripsi empty state `Try adjusting your search or filter.` pada sub tab History
191. Verifikasi judul `No history yet` tidak tampil saat hasil pencarian kosong

### Gagal muat bukan empty state pada History
192. Tampilkan Sub tab `Waiting for Approval` dan `History` (TBL-REG-02) dengan kondisi K8
193. Verifikasi pesan `Unable to load this data.` pada sub tab History
194. Verifikasi tombol `[Try Again]` tampil pada sub tab History
195. Verifikasi judul `No history yet` tidak tampil saat gagal muat

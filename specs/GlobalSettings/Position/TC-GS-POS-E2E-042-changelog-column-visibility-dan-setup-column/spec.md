---
id: TC-GS-POS-E2E-042-changelog-column-visibility-dan-setup-column
title: "Popup Changelog: Overlay Column Visibility dan Setup Column 7 Kolom (Hide, Reorder, Pin, Reset to Default, ✕, dan Kolom Terakhir)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-229
  - TC-GS-POS-230
  - TC-GS-POS-231
  - TC-GS-POS-232
  - TC-GS-POS-233
  - TC-GS-POS-234
  - TC-GS-POS-235
  - TC-GS-POS-236
coverage:
  web: automated
---

# Popup Changelog: Overlay Column Visibility dan Setup Column 7 Kolom (Hide, Reorder, Pin, Reset to Default, ✕, dan Kolom Terakhir)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
  - Manage user and role Create-Only (Sari Dewi) `manageUserRoleCreate_automated_{namaCompany}@qwertysystem.net` (Pre-setup 5), hanya untuk seeding lewat API di hook `before` (Create `Procurement Analyst`), dengan `Spectra.env.GS_CREATE_PASSWORD`. Tidak dipakai login UI.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position (sidebar Global Settings, sub-tab Position). Spec ini tidak menguji navigasi sehingga `## Test Steps` tidak mengulang langkah buka.
- Data Pre-setup: tidak ada yang dipakai.
- Data Dinamis (di-seed lewat API di hook `before` pada entitas Total Control; nama bersuffix per run; fixture baru `Fixture.position.changelogSeed042`), agar Changelog berisi entri Create, Edit, dan Delete:
  - Oleh Budi Santoso: Create `IT Support Specialist {runId}-042`, Edit menjadi `IT Operations Lead {runId}-042`, Create `Temporary Staff {runId}-042`, Delete `Temporary Staff {runId}-042`.
  - Oleh Sari Dewi: Create `Procurement Analyst {runId}-042`.
  - Seluruh seeding di atas dipakai sebagai precondition TC (Changelog berisi Create, Edit, dan Delete), tidak diasersi.
  - Entri Changelog bersifat audit trail permanen dan tidak dibersihkan.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-042` yang masih ada; hapus preferensi Setup Column Changelog yang tersimpan di browser (visibilitas, urutan, dan pin) dan kembalikan viewport ke ukuran awal.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis: seeding lewat API dengan sesi Budi dan Sari; muat ulang halaman (F5) tanpa dialog `beforeunload` (tidak ada form yang dirty saat F5; modal Setup Column sudah disimpan atau ditutup); drag-and-drop pada drag handle kolom; scroll horizontal tabel Changelog; pengubahan ukuran viewport menjadi sempit (TC-GS-POS-233) dan pemulihannya; hover pada ikon Pin dan checkbox; pembacaan urutan, visibilitas, dan status beku kolom.
- State global: preferensi Setup Column Changelog (per user per tabel, disimpan di browser menurut PRD §4.2e) diubah dan dipulihkan lewat `[Reset to Default]` pada TC-GS-POS-234 serta hook `after`; viewport diubah pada TC-GS-POS-233 dan dipulihkan di langkah yang sama; flag Guided Tooltip dipulihkan di `after`.

## Test Steps

### TC-GS-POS-229: Screening Overlay Column Visibility Popup Changelog

1. Klik ikon Changelog
2. Verifikasi User > Position > Popup Changelog: Position terbuka
3. Klik `⋯` pada header kolom Actions
4. Verifikasi daftar 7 kolom tercentang berurutan `Date | Action | Position Name | Field | Old Value | New Value | Modified By`
5. Verifikasi tiap kolom memiliki drag handle
6. Verifikasi item `Setup Column...` tampil di bawah daftar

### TC-GS-POS-230: Screening Popup Setup Column dari Popup Changelog

7. Klik `Setup Column...`
8. Verifikasi Header: title "Setup Column"
9. Verifikasi Header: tombol `[✕]` tampil
10. Verifikasi Header: subtitle "Manage column visibility, reorder, and freeze columns."
11. Verifikasi Body: search dengan placeholder "Search column name..."
12. Verifikasi Body: 7 kolom tercentang
13. Verifikasi Body: drag handle tampil pada tiap kolom
14. Verifikasi Body: kontrol Pin tampil pada tiap kolom
15. Verifikasi Footer: `[Reset to Default]` tampil
16. Verifikasi Footer: `[Save]` tampil
17. Verifikasi Footer: tidak ada `[Cancel]`

### TC-GS-POS-235: ✕ membuang perubahan

18. Hilangkan centang `Field`
19. Klik `[✕]`
20. Verifikasi kolom `Field` tetap tampil di tabel Popup Changelog

### TC-GS-POS-236: Kolom terakhir tidak bisa di-uncheck

21. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
22. Hilangkan centang `Action`
23. Hilangkan centang `Position Name`
24. Hilangkan centang `Field`
25. Hilangkan centang `Old Value`
26. Hilangkan centang `New Value`
27. Hilangkan centang `Modified By`
28. Verifikasi checkbox `Date` disabled
29. Verifikasi checkbox `Date` tetap tampil
30. Arahkan kursor ke checkbox `Date`
31. Verifikasi tooltip "At least one column must remain visible."
32. Klik `[✕]`

### TC-GS-POS-231: Hide dan unhide kelas Hideable (7 kolom)

33. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
34. Hilangkan centang `Date`
35. Verifikasi kolom `Date` hilang di preview
36. Klik `[Save]`
37. Tekan F5
38. Klik ikon Changelog
39. Verifikasi kolom `Action` tampil di tabel Popup Changelog setelah Save dan F5
40. Verifikasi kolom `Date` tetap tersembunyi setelah Save dan F5
41. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
42. Centang `Date`
43. Klik `[Save]`
44. Verifikasi kolom `Date` tampil lagi
45. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
46. Hilangkan centang `Action`
47. Verifikasi kolom `Action` hilang di preview
48. Klik `[Save]`
49. Tekan F5
50. Klik ikon Changelog
51. Verifikasi kolom `Date` tampil di tabel Popup Changelog setelah Save dan F5
52. Verifikasi kolom `Action` tetap tersembunyi setelah Save dan F5
53. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
54. Centang `Action`
55. Klik `[Save]`
56. Verifikasi kolom `Action` tampil lagi
57. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
58. Hilangkan centang `Position Name`
59. Verifikasi kolom `Position Name` hilang di preview
60. Klik `[Save]`
61. Tekan F5
62. Klik ikon Changelog
63. Verifikasi kolom `Date` tampil di tabel Popup Changelog setelah Save dan F5
64. Verifikasi kolom `Position Name` tetap tersembunyi setelah Save dan F5
65. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
66. Centang `Position Name`
67. Klik `[Save]`
68. Verifikasi kolom `Position Name` tampil lagi
69. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
70. Hilangkan centang `Field`
71. Verifikasi kolom `Field` hilang di preview
72. Klik `[Save]`
73. Tekan F5
74. Klik ikon Changelog
75. Verifikasi kolom `Date` tampil di tabel Popup Changelog setelah Save dan F5
76. Verifikasi kolom `Field` tetap tersembunyi setelah Save dan F5
77. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
78. Centang `Field`
79. Klik `[Save]`
80. Verifikasi kolom `Field` tampil lagi
81. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
82. Hilangkan centang `Old Value`
83. Verifikasi kolom `Old Value` hilang di preview
84. Klik `[Save]`
85. Tekan F5
86. Klik ikon Changelog
87. Verifikasi kolom `Date` tampil di tabel Popup Changelog setelah Save dan F5
88. Verifikasi kolom `Old Value` tetap tersembunyi setelah Save dan F5
89. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
90. Centang `Old Value`
91. Klik `[Save]`
92. Verifikasi kolom `Old Value` tampil lagi
93. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
94. Hilangkan centang `New Value`
95. Verifikasi kolom `New Value` hilang di preview
96. Klik `[Save]`
97. Tekan F5
98. Klik ikon Changelog
99. Verifikasi kolom `Date` tampil di tabel Popup Changelog setelah Save dan F5
100. Verifikasi kolom `New Value` tetap tersembunyi setelah Save dan F5
101. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
102. Centang `New Value`
103. Klik `[Save]`
104. Verifikasi kolom `New Value` tampil lagi
105. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
106. Hilangkan centang `Modified By`
107. Verifikasi kolom `Modified By` hilang di preview
108. Klik `[Save]`
109. Tekan F5
110. Klik ikon Changelog
111. Verifikasi kolom `Date` tampil di tabel Popup Changelog setelah Save dan F5
112. Verifikasi kolom `Modified By` tetap tersembunyi setelah Save dan F5
113. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
114. Centang `Modified By`
115. Klik `[Save]`
116. Verifikasi kolom `Modified By` tampil lagi

### TC-GS-POS-232: Drag reorder kelas Hideable

117. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
118. Seret `Date` satu posisi ke bawah
119. Verifikasi `Date` berada di posisi 2 pada preview
120. Seret `Position Name` satu posisi ke atas
121. Verifikasi `Position Name` berada di posisi 2 pada preview
122. Seret `Field` satu posisi ke bawah
123. Verifikasi `Field` berada di posisi 5 pada preview
124. Seret `New Value` satu posisi ke bawah
125. Verifikasi `New Value` berada di posisi 7 pada preview
126. Seret `Action` satu posisi ke bawah
127. Verifikasi `Action` berada di posisi 2 pada preview
128. Seret `Old Value` satu posisi ke atas
129. Verifikasi `Old Value` berada di posisi 3 pada preview
130. Seret `Modified By` satu posisi ke atas
131. Verifikasi `Modified By` berada di posisi 5 pada preview
132. Klik `[Save]`
133. Tekan F5
134. Klik ikon Changelog
135. Verifikasi `Position Name` tetap di posisi 1 setelah Save dan F5
136. Verifikasi `Action` tetap di posisi 2 setelah Save dan F5
137. Verifikasi `Old Value` tetap di posisi 3 setelah Save dan F5
138. Verifikasi `Date` tetap di posisi 4 setelah Save dan F5
139. Verifikasi `Modified By` tetap di posisi 5 setelah Save dan F5
140. Verifikasi `Field` tetap di posisi 6 setelah Save dan F5
141. Verifikasi `New Value` tetap di posisi 7 setelah Save dan F5
142. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
143. Klik `[Reset to Default]`
144. Klik `[Save]`

### TC-GS-POS-233: Pin kelas Hideable dan batas 3 pin

145. Ubah viewport menjadi sempit sehingga tabel Changelog dapat di-scroll horizontal
146. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
147. Klik icon Pin `Date`
148. Klik icon Pin `Action`
149. Klik icon Pin `Position Name`
150. Klik `[Save]`
151. Scroll tabel Changelog secara horizontal ke kanan
152. Verifikasi kolom `Date` beku di kiri saat scroll
153. Verifikasi kolom `Action` beku di kiri saat scroll
154. Verifikasi kolom `Position Name` beku di kiri saat scroll
155. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
156. Arahkan kursor ke icon Pin `Field`
157. Verifikasi icon Pin `Field` disabled
158. Verifikasi tooltip "Maximum 3 columns can be pinned at once. Unpin another column first."
159. Klik icon Pin `Field`
160. Klik `[Reset to Default]`
161. Klik `[Save]`
162. Pulihkan viewport ke ukuran awal

### TC-GS-POS-234: Reset to Default

163. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
164. Hilangkan centang `Field`
165. Klik icon Pin `Date`
166. Klik `[Save]`
167. Buka Popup Setup Column (klik `⋯` pada header kolom Actions, lalu `Setup Column...`)
168. Klik `[Reset to Default]`
169. Klik `[Save]`
170. Verifikasi tabel kembali ke 7 kolom default berurutan `Date | Action | Position Name | Field | Old Value | New Value | Modified By`
171. Verifikasi tidak ada kolom yang beku (tanpa pin)
172. Tutup Popup Changelog dengan klik `✕` di header

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 229, 230, 235, 236, 231, 232, 233, 234. Urutan ini menyimpang dari urutan TC sumber: TC-GS-POS-229 dan 230 (screening) pertama; TC-GS-POS-235 memakai Popup Setup Column yang masih terbuka dari TC-GS-POS-230 (✕ membuang perubahan, tidak menyimpan apa pun); TC-GS-POS-236 juga ditutup lewat `✕` tanpa menyimpan, sehingga keduanya sebelum TC yang menyimpan preferensi; TC-GS-POS-231, 232, 233, 234 menyimpan preferensi dan diurutkan sehingga TC-GS-POS-234 (Reset to Default) menutup state.
- Popup Changelog dibuka pada langkah 1 dan setelah setiap F5; ditutup sekali pada langkah 172.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3 dan 7 (membuka Overlay Column Visibility lalu Setup Column), langkah 19 (✕ pada TC-GS-POS-235) dan 32 (✕ pada TC-GS-POS-236), langkah 142 sampai 144 (Reset to Default dan Save agar urutan kolom kembali default sebelum TC-GS-POS-233), langkah 145 dan 162 (viewport sempit dan pemulihannya), langkah 159 (klik icon Pin yang disabled), langkah 160 dan 161 (Reset to Default dan Save agar pin dibersihkan sebelum TC-GS-POS-234), dan penutupan Popup Changelog di akhir.
- TC-GS-POS-231: tiap kolom diuji satu per satu (hide, F5, unhide) sehingga kolom tersembunyi paling banyak satu pada satu waktu dan guard kolom terakhir (TC-GS-POS-236) tidak terpicu.
- TC-GS-POS-232: TC sumber hanya menyebut "satu posisi ke bawah/atas" tanpa urutan seret; spec memakai urutan seret yang menghasilkan posisi akhir berbeda bagi tiap kolom (Position Name, Action, Old Value, Date, Modified By, Field, New Value). Tiap `Verifikasi` preview menyebut posisi segera setelah seretan kolom itu; `Verifikasi` setelah Save dan F5 menyebut posisi akhir.
- TC-GS-POS-233: ukuran viewport sempit mengikuti precondition e TC; ukuran pastinya disediakan tim FE agar tabel dapat di-scroll horizontal.
- Spec melewati sekitar 35 langkah (172 langkah, sebagian besar tujuh pengulangan hide/unhide dan tujuh asersi posisi/preview pada TC-GS-POS-231 dan 232 yang diminta TC per kolom). Seluruhnya satu kelas (Column Visibility dan Setup Column Popup Changelog, tabel dan akun yang sama; konvensi bagian 3 prinsip 13 mempertahankan Setup Column sebagai satu spec selama dataset dan harness sama). Setiap blok TC memulai dari preferensi default (dipulihkan lewat Reset to Default atau tidak diubah) dan tetap bermakna bila blok lain gagal.
- Tujuh `Verifikasi` kolom lain tampil di tabel Popup Changelog setelah Save dan F5 (langkah 39, 51, 63, 75, 87, 99, 111) adalah asersi tambahan di luar Expected TC-GS-POS-231 yang menjadi anchor positif bagi tujuh absence "kolom X tetap tersembunyi" sesudahnya (langkah 40, 52, 64, 76, 88, 100, 112), sehingga popup yang gagal terbuka sesudah F5 tidak meloloskannya.
- Search, Filter, Sort, dan Pagination Popup Changelog ada di spec 039, 040, dan 041; Download di spec 043.
- Topik satu dataset Changelog (screening 038, Search 039, Filter 040, Sort 041, Setup Column 042, Download 043) dipertahankan sebagai spec terpisah karena gabungan keenamnya melewati batas ukuran jauh dan tiap spec menyiapkan dan membersihkan seeding sendiri, sehingga kegagalan keras satu spec tidak menghilangkan makna spec lain.
- Temuan untuk QA:
  - TC-GS-POS-230 Expected c menulis "`[Reset to Default]` dan `[Save]` tampil ; tidak ada `[Cancel]`" (tanda baca ganda); spec mengasersi kedua tombol tampil dan `[Cancel]` tidak ada. Label tombol sudah sesuai konvensi (modal Setup Column tanpa `[Cancel]`).
  - TC-GS-POS-231 menyebut "amati preview" tanpa mendefinisikan area preview; spec mengasersi tabel Popup Changelog di belakang modal, sesuai PRD §4.2e (perubahan di-preview langsung di tabel).
  - TC-GS-POS-232 tidak menyebut urutan atau arah seret tiap kolom, dan tidak menyatakan apakah "posisi baru" diasersi relatif terhadap urutan akhir; lihat Notes.
  - TC-GS-POS-233 tidak menyebut apa yang diasersi setelah klik icon Pin `Field` yang disabled (tidak berubah); spec tidak menambah asersi.
  - TC-GS-POS-235 dan 236 menutup Setup Column lewat `[✕]`; PRD §4.2e menyatakan tidak ada dialog `Unsaved Changes`, dan TC tidak mengasersinya.
  - TC-GS-POS-229 sampai 236 tidak mencantumkan pembersihan preferensi Setup Column yang tersimpan di browser; spec memulihkannya lewat `[Reset to Default]` dan hook `after`.

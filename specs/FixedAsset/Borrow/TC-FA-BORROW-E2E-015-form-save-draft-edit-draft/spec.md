---
id: TC-FA-BORROW-E2E-015-form-save-draft-edit-draft
title: "Save Draft, Edit draft, dan Add to Borrow Draft menyimpan isi Draft tanpa mengunci aset"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-BRW-39", "FI-BRW-40", "FI-BRW-41", "FI-BRW-43", "FI-BRW-44", "§4.1b#p1", "§4.1b#r1", "§4.1b#r2", "§4.1b#r3", "§4.1b#r4", "§4.1b#p4", "§4.1b#r5", "§4.1b#r6", "§4.1b#r7", "§4.4#r4", "EB-FRM-9"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-39": [9, 10, 20, 168, 171]
  "FI-BRW-40": [23, 34]
  "FI-BRW-41": [23, 27]
  "FI-BRW-43": [33, 34, 56]
  "FI-BRW-44": [35, 57]
  "§4.1b#p1": [64, 65]
  "§4.1b#r1": [66, 67, 75, 80, 88, 93, 97]
  "§4.1b#r2": [65, 68, 77, 82, 89, 102]
  "§4.1b#r3": [69, 73, 84, 90, 106, 108, 112]
  "§4.1b#r4": [70, 71, 86, 91, 117, 122]
  "§4.1b#p4": [126, 128, 156]
  "§4.1b#r5": 128
  "§4.1b#r6": [156, 160]
  "§4.1b#r7": [126, 133, 135, 138, 140, 151]
  "§4.4#r4": [20, 27]
  "EB-FRM-9": [38, 43, 44, 47, 51]
anchor: []
coverage:
  web: automated
---

# Save Draft, Edit draft, dan Add to Borrow Draft menyimpan isi Draft tanpa mengunci aset

## Prerequisites
- Aktor: Asset Admin `Asset Admin Draft {runId}` (Aktor Borrow) dengan Group penugasan `Head Office` dan `Branch Surabaya`; Asset Admin lain `Admin Draft Lain {runId}` dengan Group penugasan `Head Office` adalah pembuat Draft yang sudah ada.
- Layar awal: Transactions > Borrow.
- Data:
  - DU-015-1: Borrower `Kirana Peminjam {runId}`, Email `kirana.peminjam{runId}@example.com`, Position `Staff {runId}`, Division `Finance {runId}`, Home Group `Head Office`, akun ber-login Status `Active` dan Activation Status `Activated`, Active Borrows `0 assets`; subjudul dialog Add to Borrow Draft bila ia punya dua Draft adalah `Kirana Peminjam {runId} has 2 drafts you can edit.`.
  - DU-015-2: Aktor `Asset Admin Draft {runId}`, role Asset Admin, Group penugasan `Head Office` dan `Branch Surabaya`; teks pada form Draft yang terakhir ia ubah adalah `Last modified by Asset Admin Draft {runId}, [Time]`; sel `Modified By` tabel menampilkan `Asset A`.
  - DU-015-3: Asset Admin `Admin Draft Lain {runId}`, role Asset Admin, Group penugasan `Head Office`; teks pada form Draft yang terakhir ia ubah adalah `Last modified by Admin Draft Lain {runId}, [Time]`; sel `Modified By` tabel menampilkan `Admin D`.
  - DU-015-4: aset `Laptop HP ProBook {runId}`, Brand `HP {runId}`, Model/Type `ProBook 450 {runId}`, Group `Head Office`, Category `Laptop {runId}`, Custody `Available`, Max Duration `7 days`, Approval `Needs approval`.
  - DU-015-5: aset `Proyektor Optoma {runId}`, Brand `Optoma {runId}`, Model/Type `HD146X {runId}`, Group `Head Office`, Category `Projector {runId}`, Custody `Available`, Max Duration `7 days`, Approval `Needs approval`.
  - DU-015-6: aset `Toyota Rush {runId}`, Brand `Toyota {runId}`, Model/Type `Rush {runId}`, Group `Branch Surabaya`, Category `Car {runId}`, Custody `Available`, Max Duration `14 days`, Approval `Needs approval`.
  - DU-015-7: aset `Kamera Sony A7 {runId}`, Brand `Sony {runId}`, Model/Type `A7 IV {runId}`, Group `Head Office`, Category `Camera {runId}`, Custody `Available`, Max Duration `7 days`, Approval `Needs approval`.
  - DU-015-8: aset `Monitor LG UltraWide {runId}`, Brand `LG {runId}`, Model/Type `34WN {runId}`, Group `Head Office`, Category `Monitor {runId}`, Custody `Available`, Max Duration `7 days`, Approval `Needs approval`.
  - DU-015-9: aset `Printer Epson L3250 {runId}`, Brand `Epson {runId}`, Model/Type `L3250 {runId}`, Group `Head Office`, Category `Printer {runId}`, Custody `Available`, Max Duration `7 days`, Approval `Needs approval`.
  - DU-015-10: aset `Speaker JBL {runId}`, Brand `JBL {runId}`, Model/Type `Partybox {runId}`, Group `Head Office`, Category `Audio {runId}`, Custody `Available`, Max Duration `7 days`, Approval `Needs approval`.
  - DU-015-11: Draft lama untuk Borrower `Kirana Peminjam {runId}` berisi `Kamera Sony A7 {runId}` dengan Duration `1` dan Purpose `Dokumentasi acara` ditambah 9 aset DU-015-13 sehingga Total Asset Draft ini `10`, dibuat dan terakhir diubah oleh `Admin Draft Lain {runId}`, Last Updated `T0 − 2 hari`; rentang tanggal saring `T0 − 3 hari` sampai `T0 − 1 hari` hanya memuat Draft ini, dan rentang `T0` sampai `T0` hanya memuat Draft yang dibuat di spec ini.
  - DU-015-12: isian form Borrow Request untuk Draft baru: `Laptop HP ProBook {runId}` dengan Duration `3` dan Purpose `Training`; `Proyektor Optoma {runId}` dengan Duration `2` dan Purpose `Rapat vendor`; `Toyota Rush {runId}` tanpa Duration dan Purpose; ubahan saat Edit: Purpose `Laptop HP ProBook {runId}` menjadi `Rapat klien`, dan Purpose `Proyektor Optoma {runId}` menjadi `Perubahan belum tersimpan` (tidak disimpan).
  - DU-015-13: 9 aset `Perlengkapan Studio {n} {runId}` (n `1` sampai `9`), Group `Head Office`, Custody `Borrowed` (sudah dipinjam BRW lain sehingga tidak dimuat di dialog Select Asset), Max Duration `7 days`, Approval `Needs approval`, isi Draft lama DU-015-11 dengan Duration `1` dan Purpose `Dokumentasi acara`.
  - DU-015-14: Borrower `Lukman Peminjam {runId}`, Email `lukman.peminjam{runId}@example.com`, Position `Staff {runId}`, Division `Operations {runId}`, Home Group `Head Office`, akun ber-login Status `Active` dan Activation Status `Activated`, Active Borrows `0 assets`; Draft tanpa aset yang dibuat spec ini berstatus Total Asset `0`.

## Test Steps

### Save Draft ditolak tanpa Borrower
1. Klik `[+ Borrow]`
2. Klik `[+ Asset]`
3. Ketik Search `{runId}`, tekan Enter
4. Centang baris `Laptop HP ProBook {runId}`
5. Centang baris `Proyektor Optoma {runId}`
6. Centang baris `Toyota Rush {runId}`
7. Klik `[Select]`
8. Klik `[Save Draft]`
9. Verifikasi caption error `You must pick a borrower` tampil di bawah field Borrower
10. Verifikasi form tetap terbuka tanpa toast `Success, borrow has been saved as draft.`

### Save Draft menyimpan seluruh baris dengan Borrower saja
11. Klik `[Select Borrower]`
12. Ketik Search `Kirana Peminjam {runId}`, tekan Enter
13. Pilih baris `Kirana Peminjam {runId}`
14. Klik `[Select]`
15. Isi Duration baris `Laptop HP ProBook {runId}` dengan `3`
16. Isi Purpose baris `Laptop HP ProBook {runId}` dengan `Training`
17. Isi Duration baris `Proyektor Optoma {runId}` dengan `2`
18. Isi Purpose baris `Proyektor Optoma {runId}` dengan `Rapat vendor`
19. Klik `[Save Draft]`
20. Verifikasi toast `Success, borrow has been saved as draft.` tampil walau Duration dan Purpose baris ketiga belum diisi
21. Buka tab Drafts
22. Ketik Search `Kirana Peminjam {runId}`, tekan Enter
23. Verifikasi tabel Drafts memuat tepat satu baris Draft dengan Total Asset `3` untuk Borrower itu, yang memuat aset dari Group `Branch Surabaya` dan `Head Office` dalam satu Draft (belum dipecah)
24. Klik `[+ Borrow]`
25. Klik `[+ Asset]`
26. Ketik Search `Laptop HP ProBook {runId}`, tekan Enter
27. Verifikasi kolom `Eligibility` pada baris `Laptop HP ProBook {runId}` memuat `Ready` walau aset itu sudah ada di Draft (Draft tidak mengunci aset)
28. Klik `[Cancel]` pada dialog Select Asset
29. Klik `[Cancel]` pada form yang belum diubah

### Edit draft membuka form dengan nilai tersimpan
30. Buka tab Drafts
31. Ketik Search `Kirana Peminjam {runId}`, tekan Enter
32. Klik ikon pensil `Edit` pada baris Draft dengan Total Asset `3`
33. Verifikasi form Borrow Request terbuka dengan Borrower `Kirana Peminjam {runId}` dan baris aset `Laptop HP ProBook {runId}`, `Proyektor Optoma {runId}`, dan `Toyota Rush {runId}`
34. Verifikasi baris `Laptop HP ProBook {runId}` berisi Duration `3` dan Purpose `Training`, dan baris `Proyektor Optoma {runId}` berisi Duration `2` dan Purpose `Rapat vendor`
35. Verifikasi teks `Last modified by Asset Admin Draft {runId}, [Time]` tampil pada form Edit draft
36. Ganti Purpose baris `Laptop HP ProBook {runId}` dengan `Rapat klien`
37. Klik `[Save Draft]`
38. Verifikasi toast `Success, borrow has been saved as draft.` tampil
39. Muat ulang halaman
40. Buka tab Drafts
41. Ketik Search `Kirana Peminjam {runId}`, tekan Enter
42. Klik ikon pensil `Edit` pada baris Draft dengan Total Asset `3`
43. Verifikasi baris `Laptop HP ProBook {runId}` berisi Purpose `Rapat klien` sesudah muat ulang halaman
44. Verifikasi baris `Laptop HP ProBook {runId}` tetap berisi Duration `3` dan baris `Proyektor Optoma {runId}` tetap berisi Duration `2` dan Purpose `Rapat vendor`
45. Ganti Purpose baris `Proyektor Optoma {runId}` dengan `Perubahan belum tersimpan`
46. Klik `[Submit]`
47. Verifikasi caption error `Please fill in all required fields.` tampil di atas deretan tombol dan form tetap terbuka tanpa toast sukses
48. Klik `[Cancel]` pada form
49. Klik `[Leave]` pada dialog Unsaved Changes
50. Klik ikon pensil `Edit` pada baris Draft dengan Total Asset `3`
51. Verifikasi baris `Proyektor Optoma {runId}` tetap berisi Purpose `Rapat vendor` dan baris `Laptop HP ProBook {runId}` tetap berisi Purpose `Rapat klien`
52. Klik `[Cancel]` pada form yang belum diubah

### Draft milik Aktor lain dalam cakupan dapat dibuka dan diedit
53. Buka tab Drafts
54. Ketik Search `Admin Draft Lain {runId}`, tekan Enter
55. Klik ikon pensil `Edit` pada baris Draft dengan Modified By `Admin Draft Lain {runId}`
56. Verifikasi form Borrow Request terbuka dengan Borrower `Kirana Peminjam {runId}`, baris aset `Kamera Sony A7 {runId}`, Duration `1`, dan Purpose `Dokumentasi acara`
57. Verifikasi teks `Last modified by Admin Draft Lain {runId}, [Time]` tampil pada form Edit draft
58. Klik `[Cancel]` pada form yang belum diubah

### Dialog Add to Borrow Draft memuat Draft Borrower menurut kolomnya
59. Buka Assets > All
60. Ketik Search `Monitor LG UltraWide {runId}`, tekan Enter
61. Pilih aksi baris `Add to Borrow Draft` pada aset `Monitor LG UltraWide {runId}`
62. Pilih baris `Kirana Peminjam {runId}` pada dialog Select Borrower
63. Klik `[Select]`
64. Verifikasi judul dialog `Add to Borrow Draft` dan subjudul `Kirana Peminjam {runId} has 2 drafts you can edit.` tampil
65. Verifikasi dialog memuat tepat dua baris Draft: satu dengan Total Asset `3` dan satu dengan Total Asset `10`
66. Verifikasi kolom `Group` pada baris Draft yang Modified By-nya `Asset Admin Draft {runId}` memuat `Branch Surabaya` dan `Head Office`
67. Verifikasi kolom `Group` pada baris Draft yang Modified By-nya `Admin Draft Lain {runId}` memuat `Head Office`
68. Verifikasi kolom `Total Asset` pada baris Draft yang Modified By-nya `Asset Admin Draft {runId}` memuat `3` dan pada baris Draft yang Modified By-nya `Admin Draft Lain {runId}` memuat `10`
69. Verifikasi kolom `Modified By` pada baris Draft yang Modified By-nya `Asset Admin Draft {runId}` memuat `Asset A` dan pada baris Draft yang Modified By-nya `Admin Draft Lain {runId}` memuat `Admin D`, dan nama lengkap `Asset Admin Draft {runId}` serta `Admin Draft Lain {runId}` tersampaikan saat kursor diarahkan ke sel `Modified By` baris masing-masing
70. Verifikasi kolom `Last Updated` pada baris Draft yang Modified By-nya `Admin Draft Lain {runId}` memuat waktu `T0 − 2 hari` menurut format General Settings
71. Verifikasi baris Draft yang Modified By-nya `Asset Admin Draft {runId}` tampil di atas baris Draft yang Modified By-nya `Admin Draft Lain {runId}` menurut urutan bawaan kolom `Last Updated` dari terbaru ke terlama

### Search Add to Borrow Draft menyaring baris menurut kolom Searchable
72. Ketik Search `Admin Draft Lain {runId}`, tekan Enter
73. Verifikasi baris Draft yang Modified By-nya `Admin Draft Lain {runId}` tampil dan baris Draft yang Modified By-nya `Asset Admin Draft {runId}` tidak tampil (pencarian pada kolom `Modified By`)
74. Ganti isi kotak search dengan `Branch Surabaya`, tekan Enter
75. Verifikasi baris Draft yang Modified By-nya `Asset Admin Draft {runId}` tampil dan baris Draft yang Modified By-nya `Admin Draft Lain {runId}` tidak tampil (pencarian pada kolom `Group`)
76. Ganti isi kotak search dengan `10`, tekan Enter
77. Verifikasi baris Draft yang Modified By-nya `Admin Draft Lain {runId}` tampil (pencarian pada kolom `Total Asset`)
78. Klik `(←)` pada kotak Search

### Sort Add to Borrow Draft mengurutkan baris menurut kolom
79. Klik header kolom `Group`
80. Verifikasi baris Draft yang Modified By-nya `Asset Admin Draft {runId}` (`Branch Surabaya`, `Head Office`) tampil di atas baris Draft yang Modified By-nya `Admin Draft Lain {runId}` (`Head Office`) menurut `Group` dari A ke Z
81. Klik header kolom `Total Asset`
82. Verifikasi baris Draft yang Modified By-nya `Asset Admin Draft {runId}` (`3`) tampil di atas baris Draft yang Modified By-nya `Admin Draft Lain {runId}` (`10`) menurut `Total Asset` secara numerik
83. Klik header kolom `Modified By`
84. Verifikasi baris Draft yang Modified By-nya `Admin Draft Lain {runId}` (`Admin Draft Lain {runId}`) tampil di atas baris Draft yang Modified By-nya `Asset Admin Draft {runId}` (`Asset Admin Draft {runId}`) menurut `Modified By` dari A ke Z
85. Klik header kolom `Last Updated`
86. Verifikasi baris Draft yang Modified By-nya `Admin Draft Lain {runId}` (`T0 − 2 hari`) tampil di atas baris Draft yang Modified By-nya `Asset Admin Draft {runId}` (`T0`) menurut `Last Updated` dari terlama ke terbaru

### Filter Add to Borrow Draft menyaring baris menurut kolom Filterable
87. Klik ikon Filter
88. Verifikasi field `Group` pada Filter Panel dialog Add to Borrow Draft memuat placeholder `All groups`
89. Verifikasi field `Total Asset` memuat placeholder `Min` dan `Max`
90. Verifikasi field `Modified By` memuat placeholder `All users`
91. Verifikasi field `Last Updated` memuat placeholder `Select date`
92. Pilih node `Head Office` dan `Branch Surabaya` pada filter `Group`
93. Verifikasi `Head Office` dan `Branch Surabaya` terpilih bersamaan pada filter `Group`
94. Klik `[Clear Field]`
95. Pilih node `Branch Surabaya` pada filter `Group`
96. Klik `[Apply]`
97. Verifikasi baris Draft yang Modified By-nya `Asset Admin Draft {runId}` tampil dan baris Draft yang Modified By-nya `Admin Draft Lain {runId}` tidak tampil
98. Klik `[Clear Field]`
99. Klik `[Apply]`
100. Isi field `Total Asset` Min `10` dan Max `10`
101. Klik `[Apply]`
102. Verifikasi baris Draft yang Modified By-nya `Admin Draft Lain {runId}` tampil dan baris Draft yang Modified By-nya `Asset Admin Draft {runId}` tidak tampil (batas Min dan Max inklusif)
103. Klik `[Clear Field]`
104. Klik `[Apply]`
105. Pilih opsi `Admin Draft Lain {runId}` dan `Asset Admin Draft {runId}` pada filter `Modified By`
106. Verifikasi `Admin Draft Lain {runId}` dan `Asset Admin Draft {runId}` terpilih bersamaan pada filter `Modified By`
107. Ketik `Admin Draft Lain {runId}` pada pencarian opsi filter `Modified By`
108. Verifikasi opsi `Admin Draft Lain {runId}` tampil dan opsi `Asset Admin Draft {runId}` tidak tampil pada daftar opsi filter `Modified By`
109. Klik `[Clear Field]`
110. Pilih opsi `Admin Draft Lain {runId}` pada filter `Modified By`
111. Klik `[Apply]`
112. Verifikasi baris Draft yang Modified By-nya `Admin Draft Lain {runId}` tampil dan baris Draft yang Modified By-nya `Asset Admin Draft {runId}` tidak tampil
113. Klik `[Clear Field]`
114. Klik `[Apply]`
115. Pilih rentang `T0 − 3 hari` sampai `T0 − 1 hari` pada filter `Last Updated`
116. Klik `[Apply]`
117. Verifikasi baris Draft yang Modified By-nya `Admin Draft Lain {runId}` tampil dan baris Draft yang Modified By-nya `Asset Admin Draft {runId}` tidak tampil
118. Klik `[Clear Field]`
119. Klik `[Apply]`
120. Pilih rentang `T0` sampai `T0` pada filter `Last Updated`
121. Klik `[Apply]`
122. Verifikasi baris Draft yang Modified By-nya `Asset Admin Draft {runId}` tampil dan baris Draft yang Modified By-nya `Admin Draft Lain {runId}` tidak tampil (satu hari yang sama dengan rentang `T0` sampai `T0` inklusif)
123. Klik `[Clear Field]`
124. Klik `[Apply]`
125. Klik ikon Filter

### Aksi footer dialog Add to Borrow Draft
126. Verifikasi tombol `[Add to Borrow Draft]` tidak aktif selama belum ada Draft terpilih
127. Klik `[Cancel]` pada dialog Add to Borrow Draft
128. Verifikasi dialog Add to Borrow Draft tertutup tanpa toast sukses
129. Pilih aksi baris `Add to Borrow Draft` pada aset `Monitor LG UltraWide {runId}`
130. Pilih baris `Kirana Peminjam {runId}` pada dialog Select Borrower
131. Klik `[Select]`
132. Pilih radio baris Draft yang Modified By-nya `Asset Admin Draft {runId}`
133. Verifikasi tombol `[Add to Borrow Draft]` aktif sesudah satu Draft dipilih
134. Klik `[Add to Borrow Draft]`
135. Verifikasi toast `Success, 1 asset has been added to the draft.` tampil
136. Buka tab Drafts
137. Ketik Search `Asset Admin Draft {runId}`, tekan Enter
138. Verifikasi kolom `Total Asset` pada baris Draft yang Modified By-nya sama bertambah menjadi `4`
139. Klik ikon pensil `Edit` pada baris Draft dengan Total Asset `4`
140. Verifikasi baris `Monitor LG UltraWide {runId}` berisi Duration dan Purpose kosong, dan baris `Laptop HP ProBook {runId}` tetap berisi Duration `3`
141. Klik `[Cancel]` pada form yang belum diubah
142. Buka Assets > All
143. Ketik Search `{runId}`, tekan Enter
144. Centang baris `Monitor LG UltraWide {runId}`
145. Centang baris `Printer Epson L3250 {runId}`
146. Pilih aksi bulk `Add to Borrow Draft`
147. Pilih baris `Kirana Peminjam {runId}` pada dialog Select Borrower
148. Klik `[Select]`
149. Pilih radio baris Draft dengan Total Asset `4`
150. Klik `[Add to Borrow Draft]`
151. Verifikasi toast `Success, 1 asset has been added to the draft. 1 was already in it.` tampil
152. Pilih aksi baris `Add to Borrow Draft` pada aset `Speaker JBL {runId}`
153. Pilih baris `Kirana Peminjam {runId}` pada dialog Select Borrower
154. Klik `[Select]`
155. Klik `[New Draft]`
156. Verifikasi toast `Success, 1 asset has been added to the draft.` tampil
157. Buka tab Drafts
158. Ketik Search `Asset Admin Draft {runId}`, tekan Enter
159. Klik ikon pensil `Edit` pada baris Draft dengan Total Asset `1`
160. Verifikasi form Borrow Request berisi Borrower `Kirana Peminjam {runId}` dan baris aset `Speaker JBL {runId}` dengan Duration dan Purpose kosong
161. Klik `[Cancel]` pada form yang belum diubah

### Save Draft tanpa aset hanya memerlukan Borrower
162. Klik `[+ Borrow]`
163. Klik `[Select Borrower]`
164. Ketik Search `Lukman Peminjam {runId}`, tekan Enter
165. Pilih baris `Lukman Peminjam {runId}`
166. Klik `[Select]`
167. Klik `[Save Draft]`
168. Verifikasi toast `Success, borrow has been saved as draft.` tampil walau form tidak memuat baris aset
169. Buka tab Drafts
170. Ketik Search `Lukman Peminjam {runId}`, tekan Enter
171. Verifikasi tabel Drafts memuat satu baris Draft untuk Borrower `Lukman Peminjam {runId}` dengan Total Asset `0`

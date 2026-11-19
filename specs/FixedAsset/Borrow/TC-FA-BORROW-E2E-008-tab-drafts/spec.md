---
id: TC-FA-BORROW-E2E-008-tab-drafts
title: "Tab Drafts menampilkan Draft bersama, Origin, aksi Edit dan Delete, serta Bulk Delete"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1l#p1", "§4.1l#p2", "§4.1l#r1", "§4.1l#r2", "§4.1l#r3", "§4.1l#r4", "§4.1l#r5", "§4.1l#r6", "§4.1l#p6", "§4.1l#r7", "§4.1l#r8", "§4.1l#r9", "§4.1l#r10", "§4.1l#p7", "§9.5#r3", "EB-BLK-2@tabel-drafts", "EB-BLK-3"]
smoke: []
dependsOn: []
trace:
  "§4.1l#p1": [3, 4]
  "§4.1l#p2": [5]
  "§4.1l#r1": [4, 12, 26, 46, 48, 70, 71, 86, 87]
  "§4.1l#r2": [7, 8, 19, 50, 52, 73, 74, 92, 93]
  "§4.1l#r3": [9, 10, 19, 54, 56, 99, 100]
  "§4.1l#r4": [11, 58, 60, 76, 77, 105, 106, 134, 135]
  "§4.1l#r5": [13, 62, 64, 79, 80, 111, 112]
  "§4.1l#r6": [6, 15, 17, 66, 68, 117, 118]
  "§4.1l#p6": [29]
  "§4.1l#r7": [26, 29, 31, 34]
  "§4.1l#r8": [35, 163, 165, 166]
  "§4.1l#r9": [132, 134, 135, 140, 142, 143, 148, 149, 151, 152, 156, 157, 159, 178, 180]
  "§4.1l#r10": [23]
  "§4.1l#p7": [21, 40, 41, 42]
  "§9.5#r3": [6]
  "EB-BLK-2@tabel-drafts": [123, 125, 127]
  "EB-BLK-3": [140, 142, 143, 148, 156, 159]
anchor: [44, 173]
coverage:
  web: automated
---

# Tab Drafts menampilkan Draft bersama, Origin, aksi Edit dan Delete, serta Bulk Delete

## Prerequisites
- Aktor: Asset Admin `Admin Aset {runId}` (DU-008-1), Group penugasan `Head Office`.
- Layar awal: Transactions > Borrow, tab Transactions.
- Data:
  - DU-008-1: User `Admin Aset {runId}`, role Asset Admin, Group penugasan `Head Office`.
  - Pengubah seluruh Draft: `Agus Pratama` (Asset Admin, Group penugasan `Head Office`), tampil `Agus P`; `Rina Wulandari` (Total Control, seluruh client), tampil `Rina W`; dan `System`. Seluruh Draft berada dalam cakupan aktor atau memuat sedikitnya satu aset di Group `Head Office`.
  - DU-008-2: Draft Borrower `Ardi Wicaksono` (tampil `Ardi W`), Origin `New`, Group `Head Office`, aset `Laptop Dell Vostro 3510 {runId}` dan `Mouse Logitech M221 {runId}`, Total Asset `2`, Modified By `Agus P`, Last Updated `T0 − 2 hari`.
  - DU-008-3: Draft Borrower `Bella Safira` (tampil `Bella S`), Origin `Restored`, Group `Head Office`, aset `Printer HP LaserJet M111 {runId}` yang tidak lagi layak dipinjam, Total Asset `1`, Modified By `Rina W`, Last Updated `T0 − 1 hari`, berasal dari BRW yang dibatalkan dengan opsi Save as Draft to edit.
  - DU-008-4: Draft Borrower `Cahyo Utomo` (tampil `Cahyo U`), Origin `Restored by system`, Group `Head Office` (aset `Scanner Epson DS-530 {runId}` dan `Mouse Pad Gaming {runId}`) dan Group `Branch Surabaya` (aset `Kamera Canon M200 {runId}` dan `Lensa Canon EF-M 18-55 {runId}`), Total Asset `4`, Modified By `System`, Last Updated `T0 − 3 hari`.
  - DU-008-5: Draft tanpa aset Borrower `Dedi Kurniawan` (tampil `Dedi K`), Origin `New`, dibuat `Admin Aset {runId}`, Group `—`, Total Asset `0`.
  - DU-008-6: Draft Borrower `Eka Pratiwi` (tampil `Eka P`), Origin `Restored by system`, Group `Head Office`, aset `Proyektor Optoma HD146X {runId}`, Modified By `System`, Last Updated `T0 − 5 hari`, berasal dari BRW yang ditutup sistem karena timeout.
  - DU-008-7: Draft Borrower `Fahmi Rahman` (tampil `Fahmi R`), Origin `New`, Group `Head Office`, aset `Speaker JBL Flip 6 {runId}`, Last Updated `T0 − 6 hari`.
  - DU-008-8: Draft Borrower `Gilang Pratama` (tampil `Gilang P`), Origin `New`, Group `Head Office`, aset `Tablet Samsung Tab S9 {runId}`, Last Updated `T0 − 7 hari`.
  - DU-008-9: Draft Borrower `Hesti Wulandari` (tampil `Hesti W`), Origin `New`, Group `Head Office`, aset `Kamera Sony ZV-E10 {runId}`, Last Updated `T0 − 8 hari`.
  - DU-008-10: Draft Borrower `Indra Gunawan` (tampil `Indra G`), Origin `New`, Group `Head Office`, aset `Monitor LG UltraWide 29 {runId}`, Last Updated `T0 − 9 hari`.
  - Kecuali DU-008-5 dan DU-008-6, Modified By DU-008-7 sampai DU-008-10 adalah `Agus P`.

## Test Steps

### Teks bantu, kolom, dan urutan awal tabel Drafts
1. Klik tab `Drafts`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi teks bantu `Drafts don't reserve assets. Submit to lock them.` tampil di atas tabel
4. Verifikasi hasil Search memuat 8 Draft dengan Borrower `Ardi W`, `Bella S`, `Cahyo U`, `Eka P`, `Fahmi R`, `Gilang P`, `Hesti W`, dan `Indra G`
5. Verifikasi tabel Drafts tidak memiliki kolom `Transaction ID` karena Draft belum bernomor BRW
6. Verifikasi urutan baris dari atas ke bawah: Borrower `Bella S`, `Ardi W`, `Cahyo U`, `Eka P`, `Fahmi R`, `Gilang P`, `Hesti W`, lalu `Indra G`
7. Verifikasi baris Borrower `Ardi W` menampilkan Group `Head Office`
8. Verifikasi baris Borrower `Cahyo U` menampilkan Group `Head Office` dan `Branch Surabaya`
9. Verifikasi baris Borrower `Ardi W` menampilkan Total Asset `2` dan baris Borrower `Cahyo U` menampilkan Total Asset `4`
10. Verifikasi baris Borrower `Bella S` menampilkan Total Asset `1` dengan tanda `⚠` karena asetnya tidak lagi layak
11. Verifikasi baris Borrower `Ardi W` menampilkan Origin `New`, baris Borrower `Bella S` menampilkan Origin `Restored`, dan baris Borrower `Cahyo U` menampilkan Origin `Restored by system`
12. Verifikasi baris Borrower `Bella S` menampilkan `Restored from` beserta nomor BRW asal pada baris kedua kolom Borrower
13. Verifikasi baris Borrower `Ardi W` menampilkan Modified By `Agus P`, baris Borrower `Bella S` menampilkan `Rina W`, dan baris Borrower `Cahyo U` menampilkan `System`
14. Arahkan kursor ke Last Updated baris Borrower `Ardi W`
15. Verifikasi tooltip `2 days ago` tampil
16. Arahkan kursor ke Last Updated baris Borrower `Bella S`
17. Verifikasi tooltip `1 day ago` tampil
18. Ganti isi kotak search dengan `Dedi K`, tekan Enter
19. Verifikasi baris Borrower `Dedi K` menampilkan Group `—` dan Total Asset `0`, karena Draft belum memuat aset
20. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Toolbar tab Drafts dan tombol Borrow
21. Verifikasi urutan tombol toolbar dari kiri ke kanan adalah `Search by Scan`, `Search`, `Filter`, lalu `[+ Borrow]`
22. Klik `[+ Borrow]`
23. Verifikasi form Borrow Request kosong terbuka tanpa Borrower terpilih
24. Klik `[Cancel]` pada form Borrow Request yang belum diisi

### Edit Draft lewat Borrower dan row action
25. Klik Borrower `Ardi W`
26. Verifikasi form Borrow Request mode edit terbuka dengan Borrower `Ardi W` dan aset `Laptop Dell Vostro 3510 {runId}` serta `Mouse Logitech M221 {runId}`
27. Klik `[Cancel]` pada form yang belum diubah
28. Klik `⋯` pada baris Borrower `Ardi W`
29. Verifikasi menu baris memuat `Edit` dan `Delete`
30. Klik `Edit`
31. Verifikasi form Borrow Request mode edit terbuka dengan Borrower `Ardi W`
32. Klik `[Cancel]` pada form yang belum diubah
33. Klik `⋯` pada baris Borrower `Cahyo U`
34. Verifikasi menu baris memuat `Edit` karena cakupan aktor meliputi sedikitnya satu Group di Draft
35. Verifikasi `Delete` pada menu baris disabled dengan tooltip `Some assets are outside your groups.`
36. Tutup menu baris

### Search by Scan menampilkan Draft yang memuat aset itu
37. Klik `Search by Scan`
38. Pilih tipe TAG `RFID`
39. Scan TAG aset `Laptop Dell Vostro 3510 {runId}`
40. Verifikasi dialog tertutup dan kotak Search terisi Asset ID aset `Laptop Dell Vostro 3510 {runId}`
41. Verifikasi baris Borrower `Ardi W` tampil
42. Verifikasi baris Borrower `Bella S` tidak tampil
43. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Sort kolom tabel Drafts lewat klik header
44. Verifikasi hasil Search memuat 8 Draft milik spec ini
45. Klik header kolom `Borrower`
46. Verifikasi urutan baris dari atas ke bawah: Borrower `Ardi W`, lalu Borrower `Cahyo U`
47. Klik header kolom `Borrower`
48. Verifikasi urutan baris dari atas ke bawah: Borrower `Indra G`, lalu Borrower `Ardi W`
49. Klik header kolom `Group`
50. Verifikasi urutan baris dari atas ke bawah: Borrower `Cahyo U`, lalu Borrower `Ardi W` (Group `Branch Surabaya` dan `Head Office` sebelum `Head Office`)
51. Klik header kolom `Group`
52. Verifikasi urutan baris dari atas ke bawah: Borrower `Ardi W`, lalu Borrower `Cahyo U` (Group `Head Office` sebelum `Branch Surabaya` dan `Head Office`)
53. Klik header kolom `Total Asset`
54. Verifikasi urutan baris dari atas ke bawah: Borrower `Hesti W`, lalu Borrower `Ardi W`, lalu Borrower `Cahyo U` (Total Asset `1`, `2`, lalu `4`)
55. Klik header kolom `Total Asset`
56. Verifikasi urutan baris dari atas ke bawah: Borrower `Cahyo U`, lalu Borrower `Ardi W`, lalu Borrower `Hesti W` (Total Asset `4`, `2`, lalu `1`)
57. Klik header kolom `Origin`
58. Verifikasi urutan baris dari atas ke bawah: Borrower `Ardi W`, lalu Borrower `Bella S`, lalu Borrower `Cahyo U` (Origin `New`, `Restored`, lalu `Restored by system`)
59. Klik header kolom `Origin`
60. Verifikasi urutan baris dari atas ke bawah: Borrower `Cahyo U`, lalu Borrower `Bella S`, lalu Borrower `Ardi W` (Origin `Restored by system`, `Restored`, lalu `New`)
61. Klik header kolom `Modified By`
62. Verifikasi urutan baris dari atas ke bawah: Borrower `Ardi W`, lalu Borrower `Bella S`, lalu Borrower `Cahyo U` (Modified By `Agus P`, `Rina W`, lalu `System`)
63. Klik header kolom `Modified By`
64. Verifikasi urutan baris dari atas ke bawah: Borrower `Cahyo U`, lalu Borrower `Bella S`, lalu Borrower `Ardi W` (Modified By `System`, `Rina W`, lalu `Agus P`)
65. Klik header kolom `Last Updated`
66. Verifikasi urutan baris dari atas ke bawah: Borrower `Indra G`, lalu Borrower `Ardi W`, lalu Borrower `Bella S` (Last Updated `T0 − 9 hari`, `T0 − 2 hari`, lalu `T0 − 1 hari`, Oldest First)
67. Klik header kolom `Last Updated`
68. Verifikasi urutan baris dari atas ke bawah: Borrower `Bella S`, lalu Borrower `Ardi W`, lalu Borrower `Indra G` (Last Updated `T0 − 1 hari`, `T0 − 2 hari`, lalu `T0 − 9 hari`, Newest First)

### Search mencocokkan nilai kolom tabel Drafts
69. Ganti isi kotak search dengan `Ardi Wicaksono`, tekan Enter
70. Verifikasi baris Borrower `Ardi W` tampil
71. Verifikasi baris Borrower `Bella S` tidak tampil
72. Ganti isi kotak search dengan `Branch Surabaya`, tekan Enter
73. Verifikasi baris Borrower `Cahyo U` tampil
74. Verifikasi baris Borrower `Ardi W` tidak tampil
75. Ganti isi kotak search dengan `Restored by system`, tekan Enter
76. Verifikasi baris Borrower `Cahyo U` dan `Eka P` tampil
77. Verifikasi baris Borrower `Ardi W` tidak tampil
78. Ganti isi kotak search dengan `Rina Wulandari`, tekan Enter
79. Verifikasi baris Borrower `Bella S` tampil
80. Verifikasi baris Borrower `Ardi W` tidak tampil
81. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Filter Panel tabel Drafts menerapkan saringan per field
82. Klik `Filter`
83. Klik field `Borrower`
84. Pilih opsi `Ardi W`
85. Klik `[Apply]`
86. Verifikasi baris Borrower `Ardi W` tampil
87. Verifikasi baris Borrower `Bella S` tidak tampil
88. Klik `[Clear Field]`
89. Klik field `Group`
90. Pilih node `Branch Surabaya`
91. Klik `[Apply]`
92. Verifikasi baris Borrower `Cahyo U` tampil
93. Verifikasi baris Borrower `Ardi W` tidak tampil
94. Klik `[Clear Field]`
95. Klik field `Total Asset`
96. Isi `Min` dengan `2`
97. Isi `Max` dengan `4`
98. Klik `[Apply]`
99. Verifikasi baris Borrower `Ardi W` dan `Cahyo U` tampil
100. Verifikasi baris Borrower `Bella S` tidak tampil
101. Klik `[Clear Field]`
102. Klik field `Origin`
103. Pilih opsi `Restored`
104. Klik `[Apply]`
105. Verifikasi baris Borrower `Bella S` tampil
106. Verifikasi baris Borrower `Ardi W` tidak tampil
107. Klik `[Clear Field]`
108. Klik field `Modified By`
109. Pilih opsi `Rina W`
110. Klik `[Apply]`
111. Verifikasi baris Borrower `Bella S` tampil
112. Verifikasi baris Borrower `Ardi W` tidak tampil
113. Klik `[Clear Field]`
114. Klik field `Last Updated`
115. Pilih rentang tanggal dari `T0 − 6 hari` sampai `T0 − 5 hari`
116. Klik `[Apply]`
117. Verifikasi baris Borrower `Eka P` tampil
118. Verifikasi baris Borrower `Ardi W` tidak tampil
119. Klik `[Clear Field]`
120. Klik `[Apply]`
121. Klik `Filter`

### Select All memilih lintas halaman dan kembali saat uncheck parsial
122. Centang baris Borrower `Ardi W`
123. Verifikasi bar bulk menampilkan tombol `Select All (8 records)`
124. Klik `Select All (8 records)`
125. Verifikasi tombol berubah menjadi `Unselect All`
126. Hapus centang baris Borrower `Ardi W`
127. Verifikasi tombol kembali menjadi `Select All (8 records)` dengan jumlah total tetap 8
128. Klik ikon `×` pada bar bulk

### Bulk Delete satu Draft
129. Centang baris Borrower `Eka P` (Origin `Restored by system`)
130. Klik `Bulk Action`
131. Klik `Delete`
132. Verifikasi dialog memuat teks `This draft will be removed. Are you sure you want to delete it?`
133. Klik `[Delete]` pada dialog
134. Verifikasi toast `Success, draft has been deleted.` tampil
135. Verifikasi baris Borrower `Eka P` tidak tampil dan baris Borrower `Ardi W` tetap tampil

### Bulk Delete beberapa Draft dengan konfirmasi klik ganda
136. Centang baris Borrower `Fahmi R`
137. Centang baris Borrower `Gilang P`
138. Klik `Bulk Action`
139. Klik `Delete`
140. Verifikasi dialog `Delete Drafts` memuat Draft `Fahmi R` dan `Gilang P` serta teks `Are you sure you want to delete them?`
141. Klik ganda `[Delete]` pada dialog
142. Verifikasi satu toast `Success, draft has been deleted.` tampil
143. Verifikasi baris Borrower `Fahmi R` dan `Gilang P` tidak tampil

### Bulk Delete campuran Draft yang bisa dihapus dan Draft di luar cakupan
144. Centang baris Borrower `Hesti W`
145. Centang baris Borrower `Cahyo U`
146. Klik `Bulk Action`
147. Klik `Delete`
148. Verifikasi dialog memuat teks `The following will be deleted:`, `The following have groups outside your access and will be skipped:`, dan `Are you sure you want to continue?`
149. Verifikasi Draft `Hesti W` tampil di bawah `The following will be deleted:` dan Draft `Cahyo U` tampil di bawah `The following have groups outside your access and will be skipped:`
150. Klik `[Continue]` pada dialog
151. Verifikasi toast `Success, draft has been deleted. Some items were skipped (outside your groups).` tampil
152. Verifikasi baris Borrower `Hesti W` tidak tampil dan baris Borrower `Cahyo U` tetap tampil

### Bulk Delete yang seluruh pilihannya di luar cakupan
153. Centang baris Borrower `Cahyo U`
154. Klik `Bulk Action`
155. Klik `Delete`
156. Verifikasi dialog `Cannot Delete Drafts` memuat teks `None of the selected drafts can be deleted because they have groups outside your access.`
157. Verifikasi toast `Success, draft has been deleted.` tidak tampil
158. Klik `[OK]` pada dialog
159. Verifikasi baris Borrower `Cahyo U` tetap tampil dan masih tercentang
160. Klik ikon `×` pada bar bulk

### Delete satu Draft lewat row action
161. Klik `⋯` pada baris Borrower `Indra G`
162. Klik `Delete`
163. Verifikasi dialog `Delete Draft` memuat teks `This draft will be removed. Are you sure you want to delete it?`
164. Klik `[Delete]` pada dialog
165. Verifikasi toast `Success, draft has been deleted.` tampil
166. Verifikasi baris Borrower `Indra G` tidak tampil dan baris Borrower `Ardi W` tetap tampil

### Bulk Delete Draft tanpa aset milik pembuatnya ikut terhapus
167. Klik `(←)` pada kotak Search
168. Klik `Filter`
169. Klik field `Borrower`
170. Pilih opsi `Dedi K`
171. Pilih opsi `Ardi W`
172. Klik `[Apply]`
173. Verifikasi baris Borrower `Dedi K` dan `Ardi W` tampil
174. Centang baris Borrower `Dedi K`
175. Centang baris Borrower `Ardi W`
176. Klik `Bulk Action`
177. Klik `Delete`
178. Verifikasi dialog `Delete Drafts` memuat Draft `Dedi K` dan `Ardi W` serta teks `Are you sure you want to delete them?`
179. Klik `[Delete]` pada dialog
180. Verifikasi baris Borrower `Dedi K` dan `Ardi W` tidak tampil
181. Klik `[Clear Field]`
182. Klik `[Apply]`

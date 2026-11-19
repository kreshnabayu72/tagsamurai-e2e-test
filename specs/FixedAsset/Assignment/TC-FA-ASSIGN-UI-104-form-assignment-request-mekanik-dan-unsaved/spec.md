---
id: TC-FA-ASSIGN-UI-104-form-assignment-request-mekanik-dan-unsaved
title: "Form Assignment Request: Saving, Unsaved Changes, Restore Changes, dan aksesibilitas"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-FRM-1@assignment-request", "EB-FRM-2@assignment-request", "EB-FRM-7@assignment-request", "EB-FRM-8@edit-draft", "EB-FB-3@edit-draft", "D-ASG-11", "D-ASG-25", "§4.4#r16", "§4.4#r17"]
smoke: []
dependsOn: []
trace:
  "EB-FRM-1@assignment-request": [65, 66, 67, 69, 73, 75, 92, 93, 94, 95, 100, 104, 105, 106, 110, 111, 117]
  "EB-FRM-2@assignment-request": [29, 30, 35, 36, 40, 41, 42, 44, 45, 47, 48, 51, 54, 150, 152, 155, 157]
  "EB-FRM-7@assignment-request": [2, 3, 4, 6, 7, 8, 58, 60, 62]
  "EB-FRM-8@edit-draft": [11, 14, 17, 20, 23, 26, 120, 123, 126, 129, 133, 136, 138, 140, 143, 145, 147, 162, 164, 166, 168, 173, 175, 179]
  "EB-FB-3@edit-draft": [78, 79, 80]
  "D-ASG-11": [40, 41, 42, 51, 54, 150, 152, 155, 157]
  "D-ASG-25": [82, 83, 85, 89]
  "§4.4#r16": 40
  "§4.4#r17": [65, 69, 73, 75, 100, 117]
anchor: [88, 160, 171]
coverage:
  web: automated
---

# Form Assignment Request: Saving, Unsaved Changes, Restore Changes, dan aksesibilitas

## Prerequisites
- Aktor: Aktor Assignment.
- Layar awal: halaman Assignment Request pada level Full.
- Komponen: Form Assignment Request
- Data:
  - DU-104-1: Assignee Employee `Dewi Kartika`, Email `dewi.kartika@example.com`, Position `Staff`, Division `IT`, Home Group `Head Office`.
  - DU-104-2: Assignee Division `Finance`, Code `FIN`, Users `4`.
  - DU-104-3: PIC `Sari Dewi`, Email `sari.dewi@example.com`, anggota Division `Finance`.
  - DU-104-4: Aset `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Group `Head Office`, Approval Rule `No approval`, Confirmation Rule `Yes`.
  - DU-104-5: Purpose awal `Operasional kantor pusat` pada baris DU-104-4.
  - DU-104-6: Purpose awal kosong pada baris DU-104-4.
  - DU-104-7: Draft tersimpan dengan Assignee DU-104-1, aset DU-104-4 ber-Purpose DU-104-6.
  - DU-104-8: Draft tersimpan dengan Assignee DU-104-2, PIC belum dipilih, aset DU-104-4 ber-Purpose DU-104-5.
  - DU-104-9: Draft tersimpan tanpa Assignee, aset DU-104-4 ber-Purpose DU-104-5.
  - DU-104-10: Draft tersimpan dengan Assignee DU-104-1 tanpa aset.
  - DU-104-11: Draft tersimpan dengan Assignee DU-104-1, Note `Peminjaman untuk proyek kantor cabang`, aset DU-104-4 ber-Purpose DU-104-5.
  - DU-104-12: Perubahan belum tersimpan dari kunjungan terakhir berupa Note `Dipakai untuk kegiatan survei`.
  - DU-104-16: Draft tersimpan dengan Assignee DU-104-2, PIC DU-104-3 yang bukan lagi anggota aktif Division `Finance`, aset DU-104-4 ber-Purpose DU-104-5.
  - DU-104-22: Aset `Toyota Avanza - 6`, Asset ID `VEH-2026-0006`, Group `Branch Surabaya`, Approval Rule `Needs approval`, Confirmation Rule `Yes`, dengan dua approver `Hendra Pratama` dan `Maya Lestari`.
- Kondisi:
  - K1: form baru dengan Assignee DU-104-1 dipilih; tabel berisi DU-104-4 ber-Purpose DU-104-5; simpan draft lambat sehingga respons belum diterima.
  - K2: form baru dengan Assignee DU-104-1 dipilih; tabel berisi DU-104-4 ber-Purpose DU-104-5 yang layak; simpan pengajuan lambat sehingga respons belum diterima.
  - K3: form baru dengan Assignee DU-104-1 dipilih; tabel berisi DU-104-4 ber-Purpose DU-104-5; form belum diubah.
  - K4: Edit draft dibuka dengan DU-104-7.
  - K5: Edit draft dibuka dengan DU-104-8.
  - K6: Edit draft dibuka dengan DU-104-9.
  - K7: Edit draft dibuka dengan DU-104-10.
  - K8: Edit draft dibuka dengan DU-104-11 dan belum ada perubahan nilai.
  - K9: form dibuka kembali dengan DU-104-12 tersimpan dari kunjungan terakhir.
  - K10: form baru dengan Assignee DU-104-2 dipilih dan PIC belum dipilih; tabel berisi DU-104-4 dengan Purpose kosong.
  - K11: Edit draft dibuka dengan DU-104-16; simpan ditolak karena PIC itu bukan lagi anggota aktif Division `Finance`.
  - K12: form baru dengan Assignee DU-104-1 dipilih; tabel berisi DU-104-4 ber-Purpose DU-104-5; simpan draft berhasil.
  - K13: form baru dengan Assignee DU-104-2 dipilih dan PIC DU-104-3 dipilih; tabel berisi DU-104-4 ber-Purpose DU-104-5 yang tercentang sehingga bar bulk tampil; simpan draft lambat sehingga respons belum diterima.
  - K14: form baru dengan Assignee DU-104-1 dipilih; tabel berisi DU-104-4 ber-Purpose DU-104-5; simpan draft lambat, lalu respons berhasil diterima.
  - K15: form baru dengan Assignee DU-104-1 dipilih; tabel berisi DU-104-4 ber-Purpose DU-104-5; simpan draft lambat, lalu respons gagal diterima karena error server.
  - K16: form baru dengan Assignee DU-104-1 dipilih; tabel berisi DU-104-22 ber-Purpose DU-104-5 yang layak; simpan pengajuan lambat, lalu respons berhasil diterima.
  - K17: Edit draft dibuka dengan DU-104-7; simpan draft berhasil.

## Test Steps

### Field wajib dan pesan error inline dapat diakses
1. Tampilkan Form Assignment Request dengan kondisi K10
2. Verifikasi field `Assignee` memiliki `aria-required`
3. Verifikasi field `PIC` memiliki `aria-required`
4. Verifikasi isian Purpose baris `Laptop Dell Latitude 5420 - 10` memiliki `aria-required`
5. Klik `[Submit]`
6. Verifikasi isian Purpose baris `Laptop Dell Latitude 5420 - 10` memiliki `aria-describedby` yang merujuk ke pesan error `Purpose must not be empty`
7. Verifikasi field `PIC` memiliki `aria-describedby` yang merujuk ke pesan error `You must pick a PIC`
8. Verifikasi ikon ⋯ pada baris `Laptop Dell Latitude 5420 - 10` memiliki nama aksesibel

### Edit draft: Purpose kosong ditolak
9. Tampilkan Form Assignment Request dengan kondisi K4
10. Klik `[Submit]`
11. Verifikasi `Purpose must not be empty` tampil di bawah Purpose baris `Laptop Dell Latitude 5420 - 10` pada Draft yang diedit

### Edit draft: Purpose di atas batas ditolak
12. Tampilkan Form Assignment Request dengan kondisi K4
13. Isi Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `Penggunaan laptop untuk kegiatan survei aset tetap dan inventarisasi lapangan di kantor cabang tahun 2026 cabang Medan ba` (121 karakter)
14. Verifikasi `Max. 120 characters` tampil di bawah Purpose baris `Laptop Dell Latitude 5420 - 10` pada Draft yang diedit

### Edit draft: Note di atas batas ditolak
15. Tampilkan Form Assignment Request dengan kondisi K4
16. Isi Note dengan `Peminjaman perangkat kerja untuk proyek pemetaan aset di kantor cabang selama satu semester tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian um` (361 karakter)
17. Verifikasi `Max. 360 characters` tampil di bawah Note pada Draft yang diedit

### Edit draft: PIC wajib untuk Assignee Division
18. Tampilkan Form Assignment Request dengan kondisi K5
19. Klik `[Submit]`
20. Verifikasi `You must pick a PIC` tampil di bawah isian PIC pada Draft yang diedit

### Edit draft: Assignee wajib
21. Tampilkan Form Assignment Request dengan kondisi K6
22. Klik `[Submit]`
23. Verifikasi `You must pick an assignee` tampil di bawah isian Assignee pada Draft yang diedit

### Edit draft: minimal satu aset
24. Tampilkan Form Assignment Request dengan kondisi K7
25. Klik `[Submit]`
26. Verifikasi `You must pick an asset` tampil di bawah tabel aset pada Draft yang diedit

### Form bersih ditinggalkan tanpa dialog
27. Tampilkan Form Assignment Request dengan kondisi K3
28. Klik `[Cancel]`
29. Verifikasi form Assignment Request ditutup
30. Verifikasi tidak ada dialog `Unsaved Changes`

### Form kembali ke nilai awal dianggap bersih
31. Tampilkan Form Assignment Request dengan kondisi K3
32. Isi Note dengan `Peminjaman untuk proyek kantor cabang`
33. Kosongkan isi Note
34. Klik `[Cancel]`
35. Verifikasi form Assignment Request ditutup
36. Verifikasi tidak ada dialog `Unsaved Changes` untuk form yang kembali ke nilai awal

### Form kotor memunculkan dialog Unsaved Changes
37. Tampilkan Form Assignment Request dengan kondisi K3
38. Isi Note dengan `Peminjaman untuk proyek kantor cabang`
39. Klik `[Cancel]`
40. Verifikasi dialog `Unsaved Changes` tampil saat form kotor ditinggalkan
41. Verifikasi dialog memuat `You have unsaved changes. Are you sure you want to leave?`
42. Verifikasi dialog memuat tombol `[Cancel]` dan `[Leave]`
43. Klik area backdrop di luar dialog
44. Verifikasi dialog `Unsaved Changes` tetap tampil
45. Verifikasi Note tetap `Peminjaman untuk proyek kantor cabang`
46. Tekan Esc
47. Verifikasi dialog `Unsaved Changes` tertutup dan form Assignment Request tetap tampil
48. Verifikasi Note tetap `Peminjaman untuk proyek kantor cabang` setelah dialog ditutup dengan Esc
49. Klik `[Cancel]`
50. Klik `[Cancel]` pada dialog `Unsaved Changes`
51. Verifikasi dialog `Unsaved Changes` tertutup dan Note tetap `Peminjaman untuk proyek kantor cabang`
52. Klik `[Cancel]`
53. Klik `[Leave]`
54. Verifikasi form Assignment Request ditutup

### Fokus pada dialog Unsaved Changes
55. Tampilkan Form Assignment Request dengan kondisi K3
56. Isi Note dengan `Peminjaman untuk proyek kantor cabang`
57. Klik `[Cancel]`
58. Verifikasi fokus berada di dalam dialog `Unsaved Changes`
59. Tekan Tab tiga kali
60. Verifikasi fokus tetap berada di dalam dialog `Unsaved Changes`
61. Klik `[Cancel]` pada dialog `Unsaved Changes`
62. Verifikasi fokus kembali ke tombol `[Cancel]` pada form

### Save Draft masuk saving state
63. Tampilkan Form Assignment Request dengan kondisi K1
64. Klik `[Save Draft]`
65. Verifikasi tombol `[Save Draft]` dalam keadaan loading dan disabled
66. Verifikasi tombol `[Submit]` dan `[Cancel]` disabled
67. Verifikasi isian Note dan isian Purpose baris `Laptop Dell Latitude 5420 - 10` disabled
68. Klik `[Save Draft]`
69. Verifikasi hanya satu permintaan simpan draft yang terkirim

### Submit pada dialog konfirmasi masuk saving state
70. Tampilkan Form Assignment Request dengan kondisi K2
71. Klik `[Submit]`
72. Klik `[Submit]` pada dialog `Submit Assignment`
73. Verifikasi tombol `[Submit]` pada dialog `Submit Assignment` dalam keadaan loading dan disabled
74. Klik `[Submit]` pada dialog `Submit Assignment`
75. Verifikasi hanya satu permintaan pengajuan yang terkirim

### Save Draft tanpa perubahan pada Draft yang sudah ada
76. Tampilkan Form Assignment Request dengan kondisi K8
77. Klik `[Save Draft]`
78. Verifikasi toast `No changes to save.` tampil untuk Draft yang tidak diubah
79. Verifikasi toast `Success, assignment has been saved as draft.` tidak tampil untuk Draft yang tidak diubah
80. Verifikasi form Assignment Request ditutup setelah Save Draft tanpa perubahan

### Restore Changes dipulihkan
81. Tampilkan Form Assignment Request dengan kondisi K9
82. Verifikasi dialog `Restore Changes` tampil dengan `You have unsaved changes from your last visit. Do you want to restore them?`
83. Verifikasi dialog memuat tombol `[Discard]` dan `[Restore]`
84. Klik `[Restore]`
85. Verifikasi Note `Dipakai untuk kegiatan survei` terisi pada form

### Restore Changes dibuang
86. Tampilkan Form Assignment Request dengan kondisi K9
87. Klik `[Discard]`
88. Verifikasi form Assignment Request tampil setelah dialog ditutup
89. Verifikasi isian Note kosong pada form

### Save Draft: seluruh kontrol form disabled sampai respons diterima
90. Tampilkan Form Assignment Request dengan kondisi K13
91. Klik `[Save Draft]`
92. Verifikasi tombol Assignee `Finance` dan tombol PIC `Sari Dewi` disabled
93. Verifikasi tombol `[+ Asset]` dan `[Add by Scan]` disabled
94. Verifikasi ikon ⋯ pada baris `Laptop Dell Latitude 5420 - 10` disabled
95. Verifikasi menu aksi pada bar bulk disabled

### Save Draft berhasil menampilkan toast satu kali
96. Tampilkan Form Assignment Request dengan kondisi K14
97. Klik `[Save Draft]`
98. Klik `[Save Draft]`
99. Respons simpan draft berhasil diterima
100. Verifikasi toast `Success, assignment has been saved as draft.` tampil satu kali setelah dua klik

### Save Draft gagal melepas keadaan loading
101. Tampilkan Form Assignment Request dengan kondisi K15
102. Klik `[Save Draft]`
103. Respons simpan draft gagal diterima
104. Verifikasi tombol `[Save Draft]` tidak lagi loading dan enabled setelah respons gagal
105. Verifikasi tombol `[Submit]` dan `[Cancel]` enabled setelah respons gagal
106. Verifikasi isian Note dan isian Purpose baris `Laptop Dell Latitude 5420 - 10` enabled setelah respons gagal

### Submit pada dialog konfirmasi: Cancel dialog dan form di belakangnya disabled sampai respons
107. Tampilkan Form Assignment Request dengan kondisi K2
108. Klik `[Submit]`
109. Klik `[Submit]` pada dialog `Submit Assignment`
110. Verifikasi tombol `[Cancel]` pada dialog `Submit Assignment` disabled
111. Verifikasi tombol Assignee `Dewi Kartika`, isian Note, dan tombol `[Save Draft]` pada form di belakang dialog disabled

### Submit berhasil menampilkan toast satu kali
112. Tampilkan Form Assignment Request dengan kondisi K16
113. Klik `[Submit]`
114. Klik `[Submit]` pada dialog `Submit Assignment`
115. Klik `[Submit]` pada dialog `Submit Assignment`
116. Respons pengajuan berhasil diterima
117. Verifikasi toast `Success, assignment has been submitted for approval.` tampil satu kali setelah dua klik

### Edit draft: Assignee wajib saat Save Draft
118. Tampilkan Form Assignment Request dengan kondisi K6
119. Klik `[Save Draft]`
120. Verifikasi `You must pick an assignee` tampil di bawah isian Assignee pada Draft yang diedit saat Save Draft

### Edit draft: PIC wajib saat Save Draft
121. Tampilkan Form Assignment Request dengan kondisi K5
122. Klik `[Save Draft]`
123. Verifikasi `You must pick a PIC` tampil di bawah isian PIC pada Draft yang diedit saat Save Draft

### Edit draft: PIC yang bukan anggota aktif Division ditolak saat Submit
124. Tampilkan Form Assignment Request dengan kondisi K11
125. Klik `[Submit]`
126. Verifikasi `Sari Dewi isn't an active member of Finance.` tampil pada Draft yang diedit saat Submit

### Edit draft: PIC yang bukan anggota aktif Division ditolak saat Save Draft
127. Tampilkan Form Assignment Request dengan kondisi K11
128. Klik `[Save Draft]`
129. Verifikasi `Sari Dewi isn't an active member of Finance.` tampil pada Draft yang diedit saat Save Draft

### Edit draft: Purpose berisi spasi saja ditolak
130. Tampilkan Form Assignment Request dengan kondisi K4
131. Isi Purpose baris `Laptop Dell Latitude 5420 - 10` dengan tiga spasi
132. Klik `[Submit]`
133. Verifikasi `Purpose must not be empty` tampil di bawah Purpose baris `Laptop Dell Latitude 5420 - 10` untuk Purpose berisi spasi saja pada Draft yang diedit

### Edit draft: Purpose tepat di batas dan spasi tepi tidak memunculkan batas
134. Tampilkan Form Assignment Request dengan kondisi K4
135. Isi Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `Penggunaan laptop untuk kegiatan survei aset tetap dan inventarisasi lapangan di kantor cabang tahun 2026 cabang Medan ba` (121 karakter)
136. Verifikasi `Max. 120 characters` tampil di bawah Purpose baris `Laptop Dell Latitude 5420 - 10` untuk Purpose 121 karakter pada Draft yang diedit
137. Ganti Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `Penggunaan laptop untuk kegiatan survei aset tetap dan inventarisasi lapangan di kantor cabang tahun 2026 cabang Medan b` (120 karakter)
138. Verifikasi `Max. 120 characters` tidak tampil untuk Purpose tepat di batas pada Draft yang diedit
139. Ganti Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `  Penggunaan laptop untuk kegiatan survei aset tetap dan inventarisasi lapangan di kantor cabang tahun 2026 cabang Medan b  `, yaitu 120 karakter dengan dua spasi di tiap tepi
140. Verifikasi `Max. 120 characters` tidak tampil untuk Purpose dengan spasi tepi pada Draft yang diedit

### Edit draft: Note tepat di batas dan spasi tepi tidak memunculkan batas
141. Tampilkan Form Assignment Request dengan kondisi K4
142. Isi Note dengan `Peminjaman perangkat kerja untuk proyek pemetaan aset di kantor cabang selama satu semester tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian um` (361 karakter)
143. Verifikasi `Max. 360 characters` tampil di bawah Note untuk Note 361 karakter pada Draft yang diedit
144. Ganti isi Note dengan `Peminjaman perangkat kerja untuk proyek pemetaan aset di kantor cabang selama satu semester tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian u` (360 karakter)
145. Verifikasi `Max. 360 characters` tidak tampil untuk Note tepat di batas pada Draft yang diedit
146. Ganti isi Note dengan `  Peminjaman perangkat kerja untuk proyek pemetaan aset di kantor cabang selama satu semester tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian u  `, yaitu 360 karakter dengan dua spasi di tiap tepi
147. Verifikasi `Max. 360 characters` tidak tampil untuk Note dengan spasi tepi pada Draft yang diedit

### Konfirmasi bawaan browser aktif untuk form kotor dan tidak aktif untuk form yang kembali ke nilai awal
148. Tampilkan Form Assignment Request dengan kondisi K3
149. Isi Note dengan `Peminjaman untuk proyek kantor cabang`
150. Verifikasi konfirmasi bawaan browser untuk muat ulang atau tutup tab aktif pada form kotor
151. Kosongkan isi Note
152. Verifikasi konfirmasi bawaan browser untuk muat ulang atau tutup tab tidak aktif pada form yang kembali ke nilai awal

### Konfirmasi bawaan browser dilepas setelah Save Draft berhasil
153. Tampilkan Form Assignment Request dengan kondisi K12
154. Isi Note dengan `Peminjaman untuk proyek kantor cabang`
155. Verifikasi konfirmasi bawaan browser untuk muat ulang atau tutup tab aktif sebelum Save Draft
156. Klik `[Save Draft]`
157. Verifikasi konfirmasi bawaan browser untuk muat ulang atau tutup tab tidak aktif sesudah Save Draft berhasil

### Edit draft: Purpose dengan spasi tengah, huruf beraksen, satu karakter, atau spasi tepi tidak memunculkan batas
158. Tampilkan Form Assignment Request dengan kondisi K4
159. Isi Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `Penggunaan laptop untuk kegiatan survei aset tetap dan inventarisasi lapangan di kantor cabang tahun 2026 cabang Medan ba` (121 karakter)
160. Verifikasi `Max. 120 characters` tampil di bawah Purpose baris `Laptop Dell Latitude 5420 - 10` untuk Purpose 121 karakter pada Draft yang diedit
161. Ganti Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `Pinjam pakai laptop dan printer untuk tim audit internal selama kunjungan ke cabang Medan Binjai tahun 2026 cabang Medan` (120 karakter)
162. Verifikasi `Max. 120 characters` tidak tampil untuk Purpose yang memuat spasi tengah pada Draft yang diedit
163. Ganti Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `Kantor Cabang Medan Élan 𝒜  tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian um` (120 karakter)
164. Verifikasi `Max. 120 characters` tidak tampil untuk Purpose yang memuat huruf beraksen dan karakter di luar BMP pada Draft yang diedit
165. Ganti Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `P` (1 karakter)
166. Verifikasi `Max. 120 characters` tidak tampil untuk Purpose satu karakter pada Draft yang diedit
167. Ganti Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `  Operasional kantor pusat  ` dengan dua spasi di tiap tepi
168. Verifikasi `Max. 120 characters` tidak tampil untuk Purpose pendek dengan spasi tepi pada Draft yang diedit

### Edit draft: Note dengan spasi tengah atau huruf beraksen tidak memunculkan batas
169. Tampilkan Form Assignment Request dengan kondisi K4
170. Isi Note dengan `Peminjaman perangkat kerja untuk proyek pemetaan aset di kantor cabang selama satu semester tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian um` (361 karakter)
171. Verifikasi `Max. 360 characters` tampil di bawah Note untuk Note 361 karakter pada Draft yang diedit
172. Ganti isi Note dengan `Peminjaman  perangkat kerja untuk proyek pemetaan aset dan  survei lapangan di cabang Medan selama semester genap tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026` (360 karakter)
173. Verifikasi `Max. 360 characters` tidak tampil untuk Note yang memuat spasi tengah pada Draft yang diedit
174. Ganti isi Note dengan `Peminjaman perangkat Élan untuk proyek 𝒜 pemetaan aset di kantor cabang Medan  tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk sur` (360 karakter)
175. Verifikasi `Max. 360 characters` tidak tampil untuk Note yang memuat huruf beraksen dan karakter di luar BMP pada Draft yang diedit

### Edit draft: Purpose dengan spasi tepi dikirim tanpa spasi tepi
176. Tampilkan Form Assignment Request dengan kondisi K17
177. Isi Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `  Operasional kantor pusat  ` dengan dua spasi di tiap tepi
178. Klik `[Save Draft]`
179. Verifikasi Purpose yang dikirim pada permintaan simpan draft adalah `Operasional kantor pusat` tanpa spasi tepi pada Draft yang diedit

---
id: TC-FA-ASSIGN-UI-111-halaman-handover-state-dan-copy
title: "Halaman Handover: state tombol, foto wajib, dan kamera tidak tersedia"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2.5#p1", "§4.2.5#p2", "§4.2.5#p3", "§4.2.5#p4", "§4.2.5#b1", "§4.2.5#b2", "§4.2.5#b3", "§4.2.5#b4", "§4.2.5#b5", "§4.2.5#b6", "§4.2.5#b7", "§4.2.5#b8", "§4.2.5#b9", "§4.2.5#b10", "§4.1#r10", FI-ASG-19, FI-ASG-42, S-ASG-08, S-ASG-09, V-ASG-19, V-ASG-20, V-ASG-21, FLD-ASG-14, FLD-ASG-15, TS-ASG-32, EC-ASG-73, "§4.4#r18", "EB-TBL-5@hand-over-no-pic", FI-ASG-20, ASSIGN-LOGIC-15a, ASSIGN-LOGIC-15c]
smoke: []
dependsOn: []
trace:
  "§4.2.5#p1": 2
  "§4.2.5#p2": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 20, 23, 27, 132, 135, 136, 138, 139, 142, 145, 146, 150, 153, 155]
  "§4.2.5#p3": 105
  "§4.2.5#p4": 59
  "§4.2.5#b1": [101, 106, 107]
  "§4.2.5#b2": [73, 74, 78, 79, 83, 84, 88, 89]
  "§4.2.5#b3": [93, 94, 95]
  "§4.2.5#b4": [60, 61, 62, 64, 65, 68, 69, 157, 158]
  "§4.2.5#b5": 111
  "§4.2.5#b6": [113, 115, 116, 119, 120]
  "§4.2.5#b7": [109, 111]
  "§4.2.5#b8": [122, 123]
  "§4.2.5#b9": [125, 126]
  "§4.2.5#b10": [129, 130]
  "§4.1#r10": 11
  FI-ASG-19: [59, 60]
  FI-ASG-20: [85, 87, 88, 89]
  ASSIGN-LOGIC-15a: [85, 87, 88]
  ASSIGN-LOGIC-15c: 89
  FI-ASG-42: [129, 130]
  S-ASG-08: [21, 24, 25, 89]
  S-ASG-09: 111
  V-ASG-19: 122
  V-ASG-20: 30
  V-ASG-21: [35, 38, 56]
  FLD-ASG-14: [30, 31]
  FLD-ASG-15: [33, 35, 40, 41, 43, 44, 46, 49]
  TS-ASG-32: 52
  EC-ASG-73: [52, 53, 54, 56, 57]
  "§4.4#r18": [99, 101, 102]
  "EB-TBL-5@hand-over-no-pic": 122
anchor: [148]
coverage:
  web: automated
---
# Halaman Handover: state tombol, foto wajib, dan kamera tidak tersedia

## Prerequisites
- Aktor: Asset Admin pada Group `Head Office`, yaitu `Dewi Lestari`.
- Layar awal: halaman Assignment Detail dengan aksi `Hand Over`; halaman Handover dibuka dari aksi itu.
- Komponen: Halaman Handover
- Data:
  - DU-111-1: ASG Transaction ID `ASG-2026-0071`, Status header `Waiting for Handover`, Requested By `Dewi Lestari`, Assignee `Budi Santoso`, Group `Head Office`, Note `Penugasan laptop tim IT`.
  - DU-111-2: ASG Transaction ID `ASG-2026-0072`, Status header `Waiting for Handover`, Requested By `Dewi Lestari`, Assignee `Finance`, PIC `Sari Dewi`, Group `Head Office`, Note `Penugasan printer divisi keuangan`.
  - DU-111-3: Baris aset Handover Name `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Brand `—`, Model/Type `—`, TAG `NFC`, Category `Laptop`, Purpose `Kerja dari rumah`, Confirmation `Yes`, Verification `Unverified`.
  - DU-111-4: Baris aset Handover Name `Laptop Dell Latitude 5420 - 11`, Asset ID `LPT-2026-0011`, Brand `—`, Model/Type `—`, TAG `NFC`, Category `Laptop`, Purpose `Kerja lapangan`, Confirmation `Yes`, Verification `Unverified`.
  - DU-111-5: Baris aset Handover Name `Printer HP M404 - 3`, Asset ID `PRN-2026-0003`, Brand `—`, Model/Type `—`, TAG `RFID`, Category `Printer`, Purpose `Cetak laporan`, Confirmation `No`, Verification `Unverified`.
  - DU-111-6: Baris aset Handover Name `Excavator PC200 - 4`, Asset ID `EXC-2026-0010`, Brand `—`, Model/Type `—`, TAG `Non TAG`, Category `Alat Berat`, Purpose `Proyek tambang`, Confirmation `No`, Verification `Non TAG`.
  - DU-111-7: Baris aset Handover Name `Camera Sony A7 - 9`, Asset ID `CAM-2026-0009`, Brand `—`, Model/Type `—`, TAG `NFC`, Category `Kamera`, Purpose `Dokumentasi proyek`, Confirmation `Yes`, Verification `Unverified`, status baris `Waiting for Handover`.
  - DU-111-8: Aset Name `Laptop Dell Latitude 5420 - 30`, Asset ID `LPT-2026-0099`.
  - DU-111-9: Aset Name `Excavator PC200 - 5`, Approver `Agus Pratama`.
  - DU-111-10: Aset Name `Toyota Avanza - 6`, Group `Branch Surabaya`.
  - DU-111-11: ASG Transaction ID `ASG-2026-0073`, Assignee `Security`, PIC `No PIC`, Group `Head Office`.
  - DU-111-12: Kata kunci Search `Printer`.
  - DU-111-13: Kata kunci Search `LPT-2026-0011`.
- Kondisi:
  - K1: Halaman Handover dibuka dari aksi `Hand Over` pada DU-111-1; baris DU-111-3 dan DU-111-4; Photo at start OFF; belum ada aset terscan.
  - K2: seperti K1; DU-111-3 sudah Verified; teks bantu yang diharapkan `Scanned assets are ready. Ask Budi Santoso to confirm.`, dari Assignee `Budi Santoso`.
  - K3: Halaman Handover dibuka untuk DU-111-1; baris DU-111-5 Verified dan DU-111-6 `Non TAG` tanpa perlu scan; teks bantu yang diharapkan `Scanned assets are ready to be handed over.`.
  - K4: Halaman Handover dibuka untuk DU-111-2 (Assignee Division); baris DU-111-3 dan DU-111-4 Verified; teks bantu yang diharapkan `Scanned assets are ready. Ask Sari Dewi to confirm.`, dari PIC `Sari Dewi`.
  - K5: Halaman Handover dibuka untuk DU-111-11 (Assignee Division tanpa PIC aktif); baris DU-111-3.
  - K6: seperti K1; Photo at start ON; DU-111-3 dan DU-111-4 Verified tanpa foto.
  - K7: seperti K1; Photo at start ON untuk DU-111-3 dan OFF untuk DU-111-5; DU-111-3 dan DU-111-5 Verified; kamera tidak tersedia atau izin kamera ditolak; Confirmation keduanya `No`.
  - K8: seperti K1; Photo at start ON; DU-111-3 Verified dengan satu foto hasil kamera.
  - K9: seperti K1; scan TAG aset DU-111-8, yang bukan aset ASG ini, ditolak; pesan yang diharapkan `Error, this TAG belongs to LPT-2026-0099, not in this assignment.`, dari Asset ID DU-111-8.
  - K10: seperti K1; scan TAG aset DU-111-9, yang masih Waiting for Approval, ditolak; pesan yang diharapkan `Error, this asset is still waiting for approval from Agus Pratama.`, dari Approver DU-111-9.
  - K11: seperti K1; scan TAG aset DU-111-10, yang berada di Group lain, ditolak; pesan yang diharapkan `Error, this asset belongs to Branch Surabaya.`, dari Group DU-111-10.
  - K12: Halaman Handover dibuka untuk ASG yang Assignee-nya adalah Aktor sendiri (`Dewi Lestari`); baris DU-111-3 `Unverified` dan Need recipient confirmation `Yes`; scan TAG DU-111-3 diterima; tombol utama yang diharapkan `[Complete Handover]`, tanpa popup `D-ASG-21` dan tanpa `D-ASG-22`.
  - K13: seperti K1 dengan baris DU-111-3, DU-111-4, dan DU-111-7; scan TAG aset DU-111-7 gagal karena tag tidak terbaca; pesan yang diharapkan `Error, this TAG can't be read. Report the TAG and use another asset.`.
  - K14: Halaman Handover dibuka untuk DU-111-1; baris DU-111-3 Verified dan DU-111-7 `Unverified`; laporan TAG DU-111-7 lewat `I Can't Scan the TAG` berhasil dibuat; teks yang diharapkan `TAG reported. Replace the TAG to hand over.`.
  - K15: seperti K14; Replace TAG untuk DU-111-7 sudah selesai saat halaman terbuka.
  - K18: seperti K2; Request Confirmation sudah ditekan dan popup Waiting for Confirmation tampil.
  - K19: seperti K3; Complete Handover berhasil; toast yang diharapkan `Success, 2 assets have been assigned to Budi Santoso.`, dari 2 aset dan Assignee `Budi Santoso`.
  - K20: seperti K1; Photo at start ON; koneksi sedang offline; DU-111-3 sudah discan dan sudah difoto.
  - K21: seperti K1; DU-111-3 dan DU-111-4 siap diproses dan dapat discan beruntun.
  - K22: seperti K18; Jendela konfirmasi Handover bernilai `15 menit` dan sudah habis tanpa konfirmasi; teks yang diharapkan `Budi Santoso didn't confirm. Try again.`, dari Assignee `Budi Santoso`.
  - K23: seperti K18; `[Cancel Request]` ditekan.
  - K24: seperti K1; tiga baris siap, yaitu DU-111-3, DU-111-4, dan DU-111-5, tetapi hanya DU-111-3 yang terscan; teks yang diharapkan `2 assets will stay Waiting for Handover.`, dari 2 baris siap yang belum terscan.
  - K25: Halaman Handover dibuka untuk DU-111-1; baris DU-111-3, DU-111-4, dan DU-111-5; Photo at start OFF.
  - K26: seperti K8; foto DU-111-3 diambil lewat picker kolom Handover Photo; dialog penyesuaian foto berjudul `Adjust photo`.

## Test Steps

### Halaman Handover dibuka dari aksi Hand Over: header, toolbar, dan kolom
1. Tampilkan Halaman Handover dengan kondisi K1
2. Verifikasi halaman Handover untuk `ASG-2026-0071` tampil setelah aksi `Hand Over`
3. Verifikasi header memuat Transaction ID `ASG-2026-0071` dengan tombol `[Copy]` dan badge status header `Waiting for Handover`
4. Verifikasi header memuat Requested By `Dewi Lestari`
5. Verifikasi header memuat Assignee `Budi Santoso`
6. Verifikasi header memuat Group `Head Office`
7. Verifikasi header memuat Note `Penugasan laptop tim IT`
8. Verifikasi header tidak memuat PIC karena Assignee adalah karyawan
9. Verifikasi kotak Search halaman Handover memuat placeholder `Search asset name or ID...`
10. Verifikasi toolbar memuat Filter dan tombol `[Verify Asset]`
11. Verifikasi daftar progres aset memuat kolom `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `TAG`, `Purpose`, `Confirmation`, dan `Verification`
12. Verifikasi kolom `Group` tidak ada di tabel karena satu ASG hanya satu Group
13. Verifikasi baris `Laptop Dell Latitude 5420 - 10` menampilkan Confirmation `Yes` dan Verification `Unverified`
14. Verifikasi kolom `Handover Photo` tidak tampil karena Photo at start OFF
15. Verifikasi tidak ada teks bantu di bawah tabel sebelum ada aset siap diproses

### Header Assignee Division memuat PIC
16. Tampilkan Halaman Handover dengan kondisi K4
17. Verifikasi header memuat Assignee `Finance`
18. Verifikasi header memuat PIC `Sari Dewi`

### Teks bantu dan tombol utama: Confirmation Yes
19. Tampilkan Halaman Handover dengan kondisi K2
20. Verifikasi teks bantu `Scanned assets are ready. Ask Budi Santoso to confirm.` tampil di bawah tabel
21. Verifikasi tombol utama `[Request Confirmation]` tampil

### Teks bantu dan tombol utama: semua Confirmation No
22. Tampilkan Halaman Handover dengan kondisi K3
23. Verifikasi teks bantu `Scanned assets are ready to be handed over.` tampil di bawah tabel
24. Verifikasi tombol utama `[Complete Handover]` tampil
25. Verifikasi tombol `[Request Confirmation]` tidak tampil

### Teks bantu memakai nama PIC untuk Assignee Division
26. Tampilkan Halaman Handover dengan kondisi K4
27. Verifikasi teks bantu `Scanned assets are ready. Ask Sari Dewi to confirm.` tampil di bawah tabel

### Request Confirmation tanpa aset terverifikasi
28. Tampilkan Halaman Handover dengan kondisi K1
29. Klik `[Request Confirmation]`
30. Verifikasi pesan error `Verify at least one asset with Verify Asset.` tampil di atas tombol
31. Verifikasi daftar tetap berisi baris `Laptop Dell Latitude 5420 - 10` dengan Verification `Unverified`

### Foto handover wajib: pesan jumlah aset tanpa foto
32. Tampilkan Halaman Handover dengan kondisi K6
33. Verifikasi kolom `Handover Photo` tampil
34. Klik `[Request Confirmation]`
35. Verifikasi pesan error `2 assets need a handover photo.` tampil di atas tombol
36. Ambil foto untuk baris `Laptop Dell Latitude 5420 - 10`
37. Klik `[Request Confirmation]`
38. Verifikasi pesan error `1 asset needs a handover photo.` tampil di atas tombol

### Handover Photo kosong: tombol ambil foto tanpa pilihan galeri
39. Tampilkan Halaman Handover dengan kondisi K6
40. Verifikasi baris `Laptop Dell Latitude 5420 - 10` memuat tombol ambil foto pada kolom `Handover Photo`
41. Verifikasi sumber foto hanya kamera tanpa pilihan file atau galeri

### Handover Photo terisi: thumbnail, pratinjau, Edit, dan Delete
42. Tampilkan Halaman Handover dengan kondisi K8
43. Verifikasi baris `Laptop Dell Latitude 5420 - 10` menampilkan thumbnail foto pada kolom `Handover Photo`
44. Verifikasi baris itu memuat ikon Edit dan ikon Delete
45. Klik thumbnail foto baris `Laptop Dell Latitude 5420 - 10`
46. Verifikasi pratinjau foto ukuran penuh tampil
47. Tutup pratinjau
48. Klik ikon Delete pada baris `Laptop Dell Latitude 5420 - 10`
49. Verifikasi baris `Laptop Dell Latitude 5420 - 10` kembali memuat tombol ambil foto

### Kamera tidak tersedia: toast, foto tidak terambil, dan baris lain tidak terhambat
50. Tampilkan Halaman Handover dengan kondisi K7
51. Klik tombol ambil foto pada baris `Laptop Dell Latitude 5420 - 10`
52. Verifikasi toast `Error, camera is not available. Allow camera access or use the mobile app.` tampil
53. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tetap tanpa foto
54. Verifikasi tidak ada pilihan unggah file atau galeri sebagai pengganti kamera
55. Klik `[Complete Handover]`
56. Verifikasi pesan error `1 asset needs a handover photo.` tampil di atas tombol dan hanya menghitung baris `Laptop Dell Latitude 5420 - 10`
57. Verifikasi baris `Printer HP M404 - 3` tidak membutuhkan foto dan tidak terhitung pada pesan error

### Baris nonaktif tetap tampil beserta alasannya
58. Tampilkan Halaman Handover dengan kondisi K14
59. Verifikasi baris `Camera Sony A7 - 9` tetap tampil dan nonaktif
60. Verifikasi kolom `Verification` baris `Camera Sony A7 - 9` menampilkan `TAG reported. Replace the TAG to hand over.`
61. Verifikasi baris `Camera Sony A7 - 9` tidak dapat di-Verify, difoto, atau diikutkan ke Request Confirmation
62. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tetap dapat diproses

### Baris kembali Unverified setelah Replace TAG
63. Tampilkan Halaman Handover dengan kondisi K15
64. Verifikasi baris `Camera Sony A7 - 9` kembali menampilkan Verification `Unverified`
65. Verifikasi baris `Camera Sony A7 - 9` dapat discan dengan TAG pengganti

### Row action I Can't Scan the TAG membuka Dialog Report TAG biasa
66. Tampilkan Halaman Handover dengan kondisi K13
67. Klik row action `I Can't Scan the TAG` pada baris `Camera Sony A7 - 9`
68. Verifikasi Dialog Report TAG biasa tampil dengan pilihan Tag, Report Type default `Unreadable`, dan Note
69. Verifikasi tidak ada pilihan identifikasi manual untuk melewati scan

### Scan ditolak: TAG bukan aset ASG ini
70. Tampilkan Halaman Handover dengan kondisi K9
71. Klik `[Verify Asset]`
72. Pindai TAG aset `Laptop Dell Latitude 5420 - 30`
73. Verifikasi toast `Error, this TAG belongs to LPT-2026-0099, not in this assignment.` tampil
74. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tetap menampilkan Verification `Unverified`

### Scan ditolak: aset masih menunggu approval
75. Tampilkan Halaman Handover dengan kondisi K10
76. Klik `[Verify Asset]`
77. Pindai TAG aset `Excavator PC200 - 5`
78. Verifikasi toast `Error, this asset is still waiting for approval from Agus Pratama.` tampil
79. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tetap menampilkan Verification `Unverified`

### Scan ditolak: aset di Group lain
80. Tampilkan Halaman Handover dengan kondisi K11
81. Klik `[Verify Asset]`
82. Pindai TAG aset `Toyota Avanza - 6`
83. Verifikasi toast `Error, this asset belongs to Branch Surabaya.` tampil
84. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tetap menampilkan Verification `Unverified`

### Scan diterima: penugasan Aktor sendiri
85. Tampilkan Halaman Handover dengan kondisi K12
86. Klik `[Verify Asset]`
87. Pindai TAG aset penugasan Aktor sendiri
88. Verifikasi baris `Laptop Dell Latitude 5420 - 10` menampilkan Verification `Verified` tanpa toast error
89. Verifikasi tombol utama `[Complete Handover]` tampil dan popup `D-ASG-21` tidak tampil

### Tag tidak terbaca: toast dan handover tidak dapat dimulai untuk aset itu
90. Tampilkan Halaman Handover dengan kondisi K13
91. Klik `[Verify Asset]`
92. Pindai TAG aset `Camera Sony A7 - 9`
93. Verifikasi toast `Error, this TAG can't be read. Report the TAG and use another asset.` tampil saat scan aset ber-tag gagal terbaca
94. Verifikasi baris `Camera Sony A7 - 9` tetap menampilkan Verification `Unverified`
95. Verifikasi row action `I Can't Scan the TAG` tersedia pada baris `Camera Sony A7 - 9`

### Scan beruntun diterapkan langsung tanpa dialog
96. Tampilkan Halaman Handover dengan kondisi K21
97. Klik `[Verify Asset]`
98. Pindai TAG aset `Laptop Dell Latitude 5420 - 10`
99. Verifikasi baris `Laptop Dell Latitude 5420 - 10` menampilkan Verification `Verified` tanpa dialog
100. Pindai TAG aset `Laptop Dell Latitude 5420 - 11`
101. Verifikasi baris `Laptop Dell Latitude 5420 - 11` menampilkan Verification `Verified` tanpa dialog
102. Verifikasi tidak ada dialog yang tampil selama scan beruntun

### Handover sebagian: konfirmasi hanya mencakup aset terscan
103. Tampilkan Halaman Handover dengan kondisi K24
104. Klik `[Request Confirmation]`
105. Verifikasi popup `Waiting for Confirmation` tampil
106. Verifikasi popup memuat teks `2 assets will stay Waiting for Handover.` karena dua baris siap belum terscan
107. Verifikasi daftar aset di popup hanya memuat `Laptop Dell Latitude 5420 - 10`

### Confirm on This Device tersedia di popup
108. Tampilkan Halaman Handover dengan kondisi K18
109. Verifikasi popup memuat tombol `[Confirm on This Device]` untuk Assignee yang tidak membawa HP
110. Klik `[Confirm on This Device]`
111. Verifikasi dialog Confirm Receipt mewajibkan Aktor Assignment mencentang pernyataan sebelum `[Confirm]` aktif

### Jendela konfirmasi habis: handover batal dan baris tetap Waiting for Handover
112. Tampilkan Halaman Handover dengan kondisi K22
113. Verifikasi popup memuat teks `Budi Santoso didn't confirm. Try again.`
114. Klik `[Done]`
115. Verifikasi halaman kembali ke langkah scan
116. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tetap Waiting for Handover

### Cancel Request menutup permintaan dan baris tetap Waiting for Handover
117. Tampilkan Halaman Handover dengan kondisi K23
118. Klik `[Cancel Request]`
119. Verifikasi popup Waiting for Confirmation tertutup
120. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tetap Waiting for Handover

### Baris No PIC: Handover tidak dapat dimulai
121. Tampilkan Halaman Handover dengan kondisi K5
122. Verifikasi alasan `Set a PIC for this division first.` tersampaikan karena Handover tidak dapat dimulai untuk baris `No PIC`
123. Verifikasi tombol `[Change PIC]` tersedia

### Hasil Handover: baris Assigned dan toast
124. Tampilkan Halaman Handover dengan kondisi K19
125. Verifikasi baris `Printer HP M404 - 3` dan `Excavator PC200 - 4` berstatus Assigned
126. Verifikasi toast `Success, 2 assets have been assigned to Budi Santoso.` tampil

### Mode offline: scan dan foto boleh, konfirmasi menunggu online
127. Tampilkan Halaman Handover dengan kondisi K20
128. Klik `[Request Confirmation]`
129. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tetap menampilkan hasil scan `Verified` dan foto yang sudah diambil
130. Verifikasi status baris `Laptop Dell Latitude 5420 - 10` belum berubah menjadi Assigned selama offline

### Header memuat Last Updated
131. Tampilkan Halaman Handover dengan kondisi K1
132. Verifikasi header memuat `Last Updated` dengan waktu pembaruan terakhir ASG

### Search dan Filter daftar progres aset
133. Tampilkan Halaman Handover dengan kondisi K25
134. Ketik Search `Printer`, tekan Enter
135. Verifikasi baris `Printer HP M404 - 3` tampil
136. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tidak tampil
137. Ganti isi kotak search dengan `LPT-2026-0011`, tekan Enter
138. Verifikasi baris `Laptop Dell Latitude 5420 - 11` tampil
139. Verifikasi baris `Printer HP M404 - 3` tidak tampil
140. Klik `(←)` pada kotak Search
141. Klik ikon Filter
142. Verifikasi Filter Panel memuat field `Category` dan `Brand`
143. Pilih `Laptop` pada field `Category`
144. Klik `[Apply]`
145. Verifikasi baris `Laptop Dell Latitude 5420 - 10` dan `Laptop Dell Latitude 5420 - 11` tampil
146. Verifikasi baris `Printer HP M404 - 3` tidak tampil

### Kolom Purpose dapat diurutkan
147. Tampilkan Halaman Handover dengan kondisi K25
148. Verifikasi tabel memuat baris `Laptop Dell Latitude 5420 - 10`, `Laptop Dell Latitude 5420 - 11`, dan `Printer HP M404 - 3`
149. Klik header kolom `Purpose`
150. Verifikasi urutan baris menurut Purpose secara menaik: `Printer HP M404 - 3`, `Laptop Dell Latitude 5420 - 10`, lalu `Laptop Dell Latitude 5420 - 11`

### Ikon Edit pada Handover Photo membuka penyesuaian foto
151. Tampilkan Halaman Handover dengan kondisi K26
152. Klik ikon Edit pada baris `Laptop Dell Latitude 5420 - 10`
153. Verifikasi dialog `Adjust photo` tampil
154. Klik `Cancel` pada dialog `Adjust photo`
155. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tetap menampilkan thumbnail foto sebelumnya

### Baris dengan TAG dilaporkan tetap Waiting for Handover
156. Tampilkan Halaman Handover dengan kondisi K14
157. Verifikasi baris `Camera Sony A7 - 9` tetap berstatus `Waiting for Handover`
158. Verifikasi batas serah terima baris `Camera Sony A7 - 9` tetap berjalan

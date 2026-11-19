---
id: TC-FA-BORROW-E2E-037-mobile-scan-borrow-wizard
title: "Wizard mobile Scan > Borrow menambahkan aset, memilih Borrower, dan menangani offline"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FI-BRW-50, FI-BRW-51, FI-BRW-52, FI-BRW-82, FI-BRW-83, FI-BRW-84, "§4.2.13#b3", "§4.6#p1", "§4.6#p3", "§4.6#b1", "§4.6#b2", "§4.6#b3", "§4.6#b4", "§4.6#b5", "§4.6#b7", "§9.11#b3", "§10#r6"]
smoke: []
dependsOn: []
trace:
  FI-BRW-50: [42]
  FI-BRW-51: [46]
  FI-BRW-52: [50]
  FI-BRW-82: [86]
  FI-BRW-83: [87]
  FI-BRW-84: [88, 91]
  "§4.2.13#b3": [8, 17]
  "§4.6#p1": [2, 44, 46, 50, 73]
  "§4.6#p3": [17, 18, 21, 29, 34, 42, 43, 46, 50, 56, 57, 115, 116, 125, 126, 127, 128, 129, 130]
  "§4.6#b1": [24]
  "§4.6#b2": [8, 10, 11, 13, 14, 95, 98, 99]
  "§4.6#b3": [31, 35, 37, 40, 109, 113]
  "§4.6#b4": [61, 63, 65, 67, 151, 155, 156, 157, 159]
  "§4.6#b5": [74, 75, 76, 79, 80, 133, 134]
  "§4.6#b7": [58, 70]
  "§10#r6": [2, 5]
  "§9.11#b3": [70, 86]
anchor: [4, 27, 39, 90, 94, 112]
coverage:
  android: manual
---

# Wizard mobile Scan > Borrow menambahkan aset, memilih Borrower, dan menangani offline

## Prerequisites
- Aktor: Asset Admin pada aplikasi native Android, lalu Borrower pada langkah «Masuk sebagai Borrower».
- Layar awal: layar utama aplikasi native Android Fixed Asset.
- Data:
  - DU-037-1: User `Agus Pratama {runId}`, role Asset Admin, Group penugasan `Head Office {runId}`, aktif, memakai aplikasi native Android.
  - DU-037-2: User `Lina Sari {runId}`, role Asset Admin, Group penugasan `Head Office {runId}`, aktif.
  - DU-037-3: User `Rudi Hartono {runId}`, karyawan tanpa role Borrow, aktif, Home Group `Head Office {runId}`, dengan dua baris pinjaman aktif (DU-037-12 dan DU-037-13).
  - DU-037-4: Karyawan `Wawan Setiadi {runId}`, aktif, tanpa akun login dan tanpa PIC.
  - DU-037-5: Group `Head Office {runId}`.
  - DU-037-6: Group `Branch Surabaya {runId}`.
  - DU-037-7: Aset `Laptop Lenovo T14 {runId}`, Group `Head Office {runId}`, status Available, TAG QR, aturan efektif approval: Approval type `Any one approver`, approver `Budi Santoso {runId}`.
  - DU-037-8: Aset `Scanner Epson DS-530 {runId}`, Group `Head Office {runId}`, status Available, TAG QR.
  - DU-037-9: Aset `Excavator Komatsu PC200 {runId}`, Group `Head Office {runId}`, status Damaged, TAG QR.
  - DU-037-10: Aset `Genset Perkins 20 kVA {runId}`, Group `Branch Surabaya {runId}`, status Available, TAG QR.
  - DU-037-11: Aset `Compressor Atlas Copco {runId}`, Group `Head Office {runId}`, status Available, TAG QR, Allowed borrower hanya Group `Branch Surabaya {runId}`.
  - DU-037-12: BRW berstatus Waiting for Handover, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Duration `3 days`, Purpose `Kunjungan klien`, Requested By `Agus Pratama {runId}`.
  - DU-037-13: BRW berstatus Borrowed, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Toyota Avanza {runId}`, Duration `5 days`, Purpose `Survei lokasi`, Requested By `Agus Pratama {runId}`.
  - DU-037-14: Isian wizard untuk aset `Laptop Lenovo T14 {runId}` dan `Scanner Epson DS-530 {runId}`: Duration `2` dan Purpose `Pemeriksaan gudang`; Submit ditolak karena perangkat offline.
  - DU-037-15: Group `IT Support {runId}`, turunan dari Group penugasan `Head Office {runId}`.
  - DU-037-16: Aset `Router Cisco ISR {runId}`, Group `IT Support {runId}`, status Available, TAG QR, Duration unit `Hours`, aturan efektif approval: Approval type `All approvers`, approver `Budi Santoso {runId}` dan `Citra Dewi {runId}`.
  - DU-037-17: Aset `Printer Canon G3010 {runId}`, Group `Head Office {runId}`, Category `Peralatan Kantor {runId}`, Allow Borrow efektif Deny, status Available, TAG QR.
  - DU-037-18: User `Budi Santoso {runId}`, role Approver, Group penugasan `Head Office {runId}`, aktif.
  - DU-037-19: User `Citra Dewi {runId}`, role Approver, Group penugasan `Head Office {runId}`, aktif.
  - DU-037-20: Karyawan `Dewi Lestari {runId}`, aktif, dengan akun login, Home Group `Branch Surabaya {runId}`.
  - DU-037-21: BRW berstatus Borrowed dengan Source `Self-service`, Group `Branch Surabaya {runId}`, Borrower `Dewi Lestari {runId}`, aset `Pompa Air Grundfos {runId}`, Duration `3 days`, Purpose `Pengairan kebun`, dipinjam sendiri oleh Borrower tanpa pengaju (Requested By `—`).
  - DU-037-22: Isian wizard kedua untuk aset `Laptop Lenovo T14 {runId}`, `Compressor Atlas Copco {runId}`, dan `Router Cisco ISR {runId}`: Duration `2` dan Purpose `Pemeriksaan jaringan`; wizard tidak di-Submit.
  - DU-037-23: Aset `Monitor Dell U2723 {runId}`, Group `Head Office {runId}`, status Available, TAG QR.
  - DU-037-24: Isian wizard ketiga untuk aset `Laptop Lenovo T14 {runId}` dan `Monitor Dell U2723 {runId}`: Duration `2` dan Purpose `Pemeriksaan ruang rapat`; Submit ditolak karena aset `Monitor Dell U2723 {runId}` sudah diambil BRW lain.
- Kondisi:
  - Max assets per borrower bernilai `10`.
  - Perangkat Android terhubung online kecuali pada langkah yang menyatakan koneksi dimatikan.
  - Akun `Rudi Hartono {runId}` dan `Dewi Lestari {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Mobile hanya Android native dan tidak ada mobile web
1. Buka aplikasi native Android Fixed Asset
2. Verifikasi menu `Scan` tersedia di aplikasi native Android
3. Buka alamat aplikasi Fixed Asset lewat peramban perangkat Android
4. Verifikasi halaman aplikasi terbuka di peramban perangkat Android
5. Verifikasi `Scan > Borrow` tidak tersedia di peramban perangkat Android
6. Kembali ke aplikasi native Android Fixed Asset

### Hasil scan pertama menentukan tombol Borrow
7. Pindai TAG aset `Laptop Lenovo T14 {runId}` lewat menu `Scan`
8. Verifikasi aset `Laptop Lenovo T14 {runId}` ditemukan dan tombol `[Borrow]` tampil
9. Pindai TAG aset `Excavator Komatsu PC200 {runId}` lewat menu `Scan`
10. Verifikasi alasan `This asset is Damaged and can't be borrowed.` tampil di bawah tombol `[Borrow]`
11. Verifikasi tombol `[Borrow]` nonaktif
12. Pindai TAG aset `Genset Perkins 20 kVA {runId}` lewat menu `Scan`
13. Verifikasi pesan scan `This asset belongs to` diikuti nama Group `Branch Surabaya {runId}` tampil
14. Verifikasi tombol `[Borrow]` tidak tampil dan identitas aset `Genset Perkins 20 kVA {runId}` tidak ditampilkan

### Wizard Scan > Borrow langkah 1 Asset
15. Pindai TAG aset `Laptop Lenovo T14 {runId}` lewat menu `Scan`
16. Ketuk `[Borrow]`
17. Verifikasi langkah 1 `Asset` menampilkan kode, nama `Laptop Lenovo T14 {runId}`, dan status `Available`
18. Verifikasi tombol `[+ Scan more]` tampil
19. Ketuk `[+ Scan more]`
20. Pindai TAG aset `Scanner Epson DS-530 {runId}`
21. Verifikasi aset `Scanner Epson DS-530 {runId}` ditambahkan ke langkah 1 `Asset`
22. Ketuk `[+ Scan more]`
23. Pindai TAG aset `Excavator Komatsu PC200 {runId}`
24. Verifikasi alasan `This asset is Damaged and can't be borrowed.` tampil dan aset `Excavator Komatsu PC200 {runId}` tidak ditambahkan ke langkah 1 `Asset`
25. Ketuk `[+ Scan more]`
26. Pindai TAG aset `Compressor Atlas Copco {runId}`
27. Verifikasi aset `Compressor Atlas Copco {runId}` ditambahkan ke langkah 1 `Asset`

### Langkah 2 Borrower: daftar Blocked, teks bantu kuota, dan kartu aset yang tidak lolos Allowed borrower
28. Lanjut ke langkah 2 `Borrower`
29. Verifikasi langkah 2 menyediakan pemindaian QR kartu karyawan dan pencarian nama
30. Cari nama `Wawan Setiadi {runId}` pada langkah 2 `Borrower`
31. Verifikasi karyawan `Wawan Setiadi {runId}` berstatus `Blocked` dengan alasan `No login account and no PIC. Set a PIC in Users first.`
32. Cari nama `Rudi Hartono {runId}` pada langkah 2 `Borrower`
33. Pilih `Rudi Hartono {runId}` sebagai Borrower
34. Verifikasi teks bantu `2 of 10 borrowed` tampil
35. Verifikasi kartu aset `Compressor Atlas Copco {runId}` ditandai ⚠ dengan caption `This asset can no longer be borrowed.`
36. Ketuk tanda ⚠ pada kartu aset `Compressor Atlas Copco {runId}`
37. Verifikasi tooltip ⚠ pada kartu `Compressor Atlas Copco {runId}` memuat satu alasan untuk Borrower `Rudi Hartono {runId}` dengan teks `can't borrow assets from` diikuti Group `Head Office {runId}`
38. Keluarkan kartu aset `Compressor Atlas Copco {runId}` dari wizard
39. Verifikasi kartu aset `Laptop Lenovo T14 {runId}` tetap ada di wizard
40. Verifikasi kartu aset `Compressor Atlas Copco {runId}` tidak ada lagi di wizard

### Langkah 3 Duration & purpose: kartu, bottom sheet, dan bar bawah
41. Lanjut ke langkah 3 `Duration & purpose`
42. Verifikasi aset `Laptop Lenovo T14 {runId}` dan `Scanner Epson DS-530 {runId}` tampil sebagai kartu, satu kartu per aset
43. Verifikasi Duration dan Purpose pada kedua kartu masih kosong
44. Verifikasi kartu aset tidak menampilkan checkbox permanen
45. Ketuk kartu aset `Laptop Lenovo T14 {runId}`
46. Verifikasi bottom sheet untuk mengisi Duration dan Purpose terbuka
47. Tutup bottom sheet Duration dan Purpose
48. Tekan lama kartu aset `Laptop Lenovo T14 {runId}`
49. Ketuk kartu aset `Scanner Epson DS-530 {runId}`
50. Verifikasi bar bawah `[Set Duration & Purpose]` tampil untuk kartu terpilih
51. Ketuk `[Set Duration & Purpose]`
52. Isi Duration dengan `2`
53. Isi Purpose dengan `Pemeriksaan gudang`
54. Ketuk `[Apply to 2 assets]`

### Langkah 4 Review: tanpa Note dan Save Draft, kartu yang tidak lagi layak, dan Submit butuh online
55. Lanjut ke langkah 4 `Review`
56. Verifikasi langkah 4 `Review` menampilkan pembagian BRW per Group dan blok Approval per aset
57. Verifikasi tombol `[Submit]` tampil di langkah 4 `Review`
58. Verifikasi wizard tidak memuat Note maupun `[Save Draft]`
59. Asset Admin `Lina Sari {runId}` mengajukan BRW atas aset `Scanner Epson DS-530 {runId}`
60. Kembali ke langkah 3 `Duration & purpose`
61. Verifikasi kartu aset `Scanner Epson DS-530 {runId}` ditandai ⚠ dengan caption `This asset can no longer be borrowed.`
62. Ketuk tanda ⚠ pada kartu aset `Scanner Epson DS-530 {runId}`
63. Verifikasi tooltip ⚠ pada kartu aset `Scanner Epson DS-530 {runId}` memuat satu alasan `This asset is already in another transaction.`
64. Lanjut ke langkah 4 `Review`
65. Verifikasi tombol `[Submit]` diblokir selama kartu aset `Scanner Epson DS-530 {runId}` masih ada
66. Keluarkan kartu aset `Scanner Epson DS-530 {runId}` dari wizard
67. Verifikasi tombol `[Submit]` dapat dipakai setelah kartu dikeluarkan
68. Matikan koneksi data perangkat
69. Ketuk `[Submit]`
70. Verifikasi BRW untuk aset `Laptop Lenovo T14 {runId}` tidak dibuat selama perangkat offline
71. Nyalakan koneksi data perangkat

### Kartu Aktor Borrow dan kartu pinjaman Borrower
72. Buka daftar BRW di aplikasi native Android
73. Verifikasi tabel BRW tampil sebagai kartu, dialog sebagai bottom sheet, dan toolbar sebagai menu ⋯ serta ikon Search
74. Verifikasi kartu aset `Laptop Dell Latitude 5420 {runId}` berlabel `Waiting for Handover` dengan aksi cepat `[Hand Over]`
75. Verifikasi kartu aset `Toyota Avanza {runId}` berlabel `Borrowed` dengan aksi cepat `[Return]` dan `[Request Extension]`
76. Verifikasi label `Ready for handover` tidak tampil pada kartu mana pun
77. Masuk sebagai Borrower `Rudi Hartono {runId}`
78. Buka daftar pinjaman pribadi Borrower di aplikasi native Android
79. Verifikasi kartu pinjaman aset `Laptop Dell Latitude 5420 {runId}` tampil tanpa aksi `[Hand Over]`
80. Verifikasi kartu pinjaman aset `Toyota Avanza {runId}` tampil tanpa aksi `[Return]` karena bukan pinjaman self-service

### Handover saat offline
81. Masuk sebagai Asset Admin `Agus Pratama {runId}`
82. Ketuk `[Hand Over]` pada kartu aset `Laptop Dell Latitude 5420 {runId}`
83. Matikan koneksi data perangkat
84. Pindai TAG aset `Laptop Dell Latitude 5420 {runId}`
85. Ambil foto aset `Laptop Dell Latitude 5420 {runId}`
86. Verifikasi pemindaian TAG dan foto berhasil dilakukan saat perangkat offline
87. Verifikasi konfirmasi Borrower dan perubahan status baris menunggu online
88. Verifikasi status `Pending sync` tampil di perangkat
89. Nyalakan koneksi data perangkat
90. Verifikasi kartu aset `Laptop Dell Latitude 5420 {runId}` tampil di daftar BRW setelah koneksi aktif
91. Verifikasi status `Pending sync` hilang setelah tersinkron

### Pemindai yang bukan Aktor Borrow tidak melihat tombol Borrow
92. Masuk sebagai Borrower `Rudi Hartono {runId}`
93. Pindai TAG aset `Laptop Lenovo T14 {runId}` lewat menu `Scan`
94. Verifikasi aset `Laptop Lenovo T14 {runId}` ditemukan
95. Verifikasi tombol `[Borrow]` tidak tampil bagi pemindai yang bukan Aktor Borrow

### Aset yang ditolak aturan Transaction Settings membuat tombol Borrow nonaktif
96. Masuk sebagai Asset Admin `Agus Pratama {runId}`
97. Pindai TAG aset `Printer Canon G3010 {runId}` lewat menu `Scan`
98. Verifikasi alasan `Borrowing isn't allowed for` diikuti Category `Peralatan Kantor {runId}` tampil di bawah tombol `[Borrow]`
99. Verifikasi tombol `[Borrow]` nonaktif untuk aset `Printer Canon G3010 {runId}`

### Wizard kedua: ganti Borrower menghilangkan tanda tidak layak, dan Review memuat pembagian BRW per Group, blok Approval per aset, dan satuan Duration
100. Pindai TAG aset `Laptop Lenovo T14 {runId}` lewat menu `Scan`
101. Ketuk `[Borrow]`
102. Ketuk `[+ Scan more]`
103. Pindai TAG aset `Compressor Atlas Copco {runId}`
104. Ketuk `[+ Scan more]`
105. Pindai TAG aset `Router Cisco ISR {runId}`
106. Lanjut ke langkah 2 `Borrower`
107. Cari nama `Rudi Hartono {runId}` pada langkah 2 `Borrower`
108. Pilih `Rudi Hartono {runId}` sebagai Borrower
109. Verifikasi kartu aset `Compressor Atlas Copco {runId}` ditandai ⚠ untuk Borrower `Rudi Hartono {runId}`
110. Cari nama `Dewi Lestari {runId}` pada langkah 2 `Borrower`
111. Pilih `Dewi Lestari {runId}` sebagai Borrower
112. Verifikasi kartu aset `Laptop Lenovo T14 {runId}` tetap ada di wizard untuk Borrower `Dewi Lestari {runId}`
113. Verifikasi tanda ⚠ pada kartu aset `Compressor Atlas Copco {runId}` hilang setelah Borrower diganti menjadi `Dewi Lestari {runId}`
114. Lanjut ke langkah 3 `Duration & purpose`
115. Verifikasi satuan Duration kartu aset `Laptop Lenovo T14 {runId}` adalah `days`
116. Verifikasi satuan Duration kartu aset `Router Cisco ISR {runId}` adalah `hours`
117. Tekan lama kartu aset `Laptop Lenovo T14 {runId}`
118. Ketuk kartu aset `Compressor Atlas Copco {runId}`
119. Ketuk kartu aset `Router Cisco ISR {runId}`
120. Ketuk `[Set Duration & Purpose]`
121. Isi Duration dengan `2`
122. Isi Purpose dengan `Pemeriksaan jaringan`
123. Ketuk `[Apply to 3 assets]`
124. Lanjut ke langkah 4 `Review`
125. Verifikasi langkah 4 `Review` memuat BRW untuk Group `Head Office {runId}` dengan aset `Laptop Lenovo T14 {runId}`
126. Verifikasi langkah 4 `Review` memuat BRW untuk Group `IT Support {runId}` dengan aset `Router Cisco ISR {runId}`
127. Verifikasi blok Approval aset `Laptop Lenovo T14 {runId}` menampilkan Approval type `Any one approver`
128. Verifikasi blok Approval aset `Laptop Lenovo T14 {runId}` menampilkan approver `Budi Santoso {runId}`
129. Verifikasi blok Approval aset `Router Cisco ISR {runId}` menampilkan Approval type `All approvers`
130. Verifikasi blok Approval aset `Router Cisco ISR {runId}` menampilkan approver `Budi Santoso {runId}` dan `Citra Dewi {runId}`

### Kartu pinjaman self-service Borrower memuat Return dan Request Extension
131. Masuk sebagai Borrower `Dewi Lestari {runId}`
132. Buka daftar pinjaman pribadi Borrower di aplikasi native Android
133. Verifikasi kartu pinjaman aset `Pompa Air Grundfos {runId}` tampil dengan aksi `[Return]` karena pinjaman self-service
134. Verifikasi kartu pinjaman aset `Pompa Air Grundfos {runId}` tampil dengan aksi `[Request Extension]`

### Kelayakan dinilai ulang saat Submit: aset yang diambil BRW lain sesudah Review dibuka
135. Masuk sebagai Asset Admin `Agus Pratama {runId}`
136. Pindai TAG aset `Laptop Lenovo T14 {runId}` lewat menu `Scan`
137. Ketuk `[Borrow]`
138. Ketuk `[+ Scan more]`
139. Pindai TAG aset `Monitor Dell U2723 {runId}`
140. Lanjut ke langkah 2 `Borrower`
141. Cari nama `Rudi Hartono {runId}` pada langkah 2 `Borrower`
142. Pilih `Rudi Hartono {runId}` sebagai Borrower
143. Lanjut ke langkah 3 `Duration & purpose`
144. Tekan lama kartu aset `Laptop Lenovo T14 {runId}`
145. Ketuk kartu aset `Monitor Dell U2723 {runId}`
146. Ketuk `[Set Duration & Purpose]`
147. Isi Duration dengan `2`
148. Isi Purpose dengan `Pemeriksaan ruang rapat`
149. Ketuk `[Apply to 2 assets]`
150. Lanjut ke langkah 4 `Review`
151. Verifikasi tombol `[Submit]` dapat dipakai selama semua kartu aset layak
152. Asset Admin `Lina Sari {runId}` mengajukan BRW atas aset `Monitor Dell U2723 {runId}`
153. Ketuk `[Submit]`
154. Ketuk tanda ⚠ pada kartu aset `Monitor Dell U2723 {runId}`
155. Verifikasi kartu aset `Monitor Dell U2723 {runId}` ditandai ⚠ dengan caption `This asset can no longer be borrowed.`
156. Verifikasi tooltip ⚠ pada kartu aset `Monitor Dell U2723 {runId}` memuat satu alasan `This asset is already in another transaction.`
157. Verifikasi tombol `[Submit]` diblokir selama kartu aset `Monitor Dell U2723 {runId}` masih ada
158. Keluarkan kartu aset `Monitor Dell U2723 {runId}` dari wizard
159. Verifikasi tombol `[Submit]` dapat dipakai setelah kartu dikeluarkan

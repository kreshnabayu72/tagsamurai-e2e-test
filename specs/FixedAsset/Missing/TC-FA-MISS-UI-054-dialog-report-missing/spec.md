---
id: TC-FA-MISS-UI-054-dialog-report-missing
title: "Dialog Report Missing: judul per jumlah aset, header aset, kotak dampak, validasi What happened, aset dilewati dengan alasan, Alert sudah dilaporkan, dan respons gagal"
layer: ui-client
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [§4.2.3#p1, §4.2.3#p2, §4.2.3#b1, §4.2.3#b2, §4.2.3#b4, §4.2.3#b5, §4.2.4#r12, §4.2.4#r13, §4.2.4#r14, §4.2.4#r15, §4.2.4#r16, §9.9#r1, §6#r14, §7.2#r1, §7.2#r14, §7.2#p1, §7.3#r5, §7.3#r6, §9.2#b4, §9.2#b6, §9.2#b7, §9.2#b15, §9.4.2#r1, §9.4.2#r2, §9.4.4#r3, §9.6#r1, §4.1#r5, §4.1#p1, §1.2#r16, §4.3#r1, EB-FRM-1@report-missing, EB-FRM-2@report-missing, EB-FRM-4@report-missing, EB-FRM-7@report-missing, EB-FB-1@report-missing, EB-FB-1@report-missing-pemegang, EB-FB-4, EB-ERR-1@report-missing, EB-FB-2@cancel-report-missing]
smoke: []
dependsOn: []
trace:
  §4.2.3#p1: 3
  §4.2.3#p2: [2, 5, 6, 7, 8, 9, 12, 13, 14, 15, 18, 19, 20, 21, 24, 28, 188, 189, 191, 193, 195, 197, 214, 216]
  §4.2.3#b1: [34, 37, 39, 128, 131, 132, 133, 134, 135, 136, 137, 138, 142, 143, 144, 145, 195, 196, 197, 198]
  §4.2.3#b2: [132, 133]
  §4.2.3#b4: [30, 32]
  §4.2.3#b5: [15, 16, 24, 25, 216, 217]
  §4.2.4#r12: [30, 32]
  §4.2.4#r13: [18, 195, 197, 198]
  §4.2.4#r14: [34, 37, 40]
  §4.2.4#r15: [15, 196]
  §4.2.4#r16: [24, 25]
  §9.9#r1: [10, 11, 37, 44, 47, 49, 51, 53, 55, 57, 59]
  §6#r14: [149, 150, 151, 155, 156, 157]
  §7.2#r1: [2, 4, 18, 23]
  §7.2#r14: [149, 151]
  §7.2#p1: [62, 65, 71, 77, 81, 86]
  §7.3#r5: [59, 107, 111, 122, 161]
  §7.3#r6: [118, 126, 180]
  §9.2#b4: [132, 133, 134, 135, 136, 143, 144]
  §9.2#b6: [122, 126]
  §9.2#b7: [131, 137, 142, 145]
  §9.2#b15: 149
  §9.4.2#r1: [132, 133]
  §9.4.2#r2: [149, 150]
  §9.4.4#r3: [149, 150]
  §9.6#r1: [161, 162, 200, 203, 204, 205, 206]
  §4.1#r5: 4
  §4.1#p1: 3
  §1.2#r16: [149, 150]
  §4.3#r1: [183, 184, 186]
  EB-FRM-1@report-missing: [103, 104, 107]
  EB-FRM-2@report-missing: [62, 65, 69, 71, 72, 74, 77, 81, 83, 86]
  EB-FRM-4@report-missing: [47, 49, 51, 53, 55]
  EB-FRM-7@report-missing: [38, 93, 94, 95, 97, 99]
  EB-FB-1@report-missing: [107, 111, 112, 161]
  EB-FB-1@report-missing-pemegang: [118, 180]
  EB-FB-4: [114, 166, 210, 212]
  EB-ERR-1@report-missing: [161, 162, 163, 164, 168, 169, 173, 174, 175, 176, 180, 181]
  EB-FB-2@cancel-report-missing: [88, 90, 91]
anchor: [27]
coverage:
  web: automated
---
# Dialog Report Missing: judul per jumlah aset, header aset, kotak dampak, validasi What happened, aset dilewati dengan alasan, Alert sudah dilaporkan, dan respons gagal

## Prerequisites
- Aktor: Pelapor admin, yaitu Aktor Missing pada Group aset; dan pemegang aset tanpa hak Aktor Missing untuk K4, K7, K8, K10, dan K16.
- Layar awal: halaman Assets.
- Komponen: Dialog Report Missing (D-MIS-01)
- Data:
  - DU-054-1: Aset `Hand Pallet Truck - 3`, Asset ID `HPT-2026-0003`, TAG `RFID`, Brand `Jungheinrich`, Group `Warehouse`, Model/Type `JH-HPT25`, Asset Status `Assigned`, Photo `hpt-2026-0003.jpg`, pemegang `Joko S`
  - DU-054-2: Aset `Laptop Dell Latitude 5420 - 22`, Asset ID `LPT-2026-0022`, TAG `NFC`, Brand `Dell`, Group `Finance Room`, Model/Type `Latitude 5420`, Asset Status `Assigned`, Photo `lpt-2026-0022.jpg`, pemegang `Andi P`
  - DU-054-3: Aset `Monitor LG 27UL500 - 11`, Asset ID `MON-2026-0011`, TAG `QR`, Brand `LG`, Group `Head Office`, Model/Type `27UL500`, Asset Status `Assigned`, Photo `mon-2026-0011.jpg`, pemegang `Sari D`
  - DU-054-4: Aset `Toyota Innova - 2`, Asset ID `VEH-2026-0002`, TAG `GPS`, Brand `Toyota`, Group `Branch Surabaya`, Model/Type `Innova`, Asset Status `Available`, Photo `veh-2026-0002.jpg`, tanpa pemegang
  - DU-054-5: Aset `Scanner Zebra DS2208 - 2`, Asset ID `SCN-2026-0002`, TAG `BLE`, Brand `Zebra`, Group `Warehouse`, Model/Type `DS2208`, Asset Status `Assigned`, Photo `scn-2026-0002.jpg`, pemegang `Joko S`
  - DU-054-6: Aset `Camera Canon EOS - 1`, Asset ID `CAM-2026-0001`, TAG `RFID`, Brand `Canon`, Group `Head Office`, Model/Type `EOS 90D`, Asset Status `Assigned`, Photo `cam-2026-0001.jpg`, pemegang `Joko S`
  - DU-054-7: Aset `Printer HP LaserJet M404 - 5`, Asset ID `PRN-2026-0005`, TAG `QR`, Brand `HP`, Group `Head Office`, Model/Type `LaserJet M404`, Asset Status `Assigned`, Photo `prn-2026-0005.jpg`, pemegang `Andi P`
  - DU-054-8: Kotak dampak dengan Borrow `BRW-2026-0141` pada aset DU-054-1; baris yang diharapkan `Hand Pallet Truck in BRW-2026-0141 will be closed as missing.`, dari Asset Name `Hand Pallet Truck` dan Borrow `BRW-2026-0141`.
  - DU-054-9: Kotak dampak dengan Borrow `BRW-2026-0152` pada aset DU-054-2 dan Borrow `BRW-2026-0153` pada aset DU-054-3; baris yang diharapkan `Laptop Dell Latitude 5420 in BRW-2026-0152 will be closed as missing.`, dari Asset Name `Laptop Dell Latitude 5420` dan Borrow `BRW-2026-0152`, serta `Monitor LG 27UL500 in BRW-2026-0153 will be closed as missing.`, dari Asset Name `Monitor LG 27UL500` dan Borrow `BRW-2026-0153`.
  - DU-054-10: Isian awal What happened `Aset tidak ditemukan saat pengecekan rak` dari titik masuk.
  - DU-054-11: Jumlah record Waiting for Confirmation dan Missing `0`.
  - DU-054-12: Jumlah record Waiting for Confirmation dan Missing `2`.
  - DU-054-23: Aset DU-054-2 dengan Borrow `BRW-2026-0150`; aset DU-054-6 dengan Borrow `BRW-2026-0155`. Baris yang diharapkan `Camera Canon EOS in BRW-2026-0155 will be closed as missing.`, dari Asset Name `Camera Canon EOS` dan Borrow `BRW-2026-0155`. Baris Borrow yang tidak boleh tampil adalah `Laptop Dell Latitude 5420 in BRW-2026-0150 will be closed as missing.`, dari Asset Name `Laptop Dell Latitude 5420` dan Borrow `BRW-2026-0150`.
  - DU-054-24: Kotak dampak dengan Assignment `ASG-2026-0071` pada aset DU-054-2; baris yang diharapkan `Laptop Dell Latitude 5420 in ASG-2026-0071 will be closed as missing.`, dari Asset Name `Laptop Dell Latitude 5420` dan Assignment `ASG-2026-0071`.
  - Joko S adalah pemegang aset tanpa hak Aktor Missing; Andi P dan Sari D adalah pemegang aset; Rina W adalah Aktor Missing pada Group aset yang melapor lebih dulu.
- Kondisi:
  - K1: dialog dibuka oleh Pelapor admin untuk aset DU-054-1 dengan kotak dampak DU-054-8; simpan berhasil.
  - K2: dialog dibuka oleh Pelapor admin untuk aset DU-054-2 dan DU-054-3 dengan kotak dampak DU-054-9.
  - K3: dialog dibuka oleh Pelapor admin untuk aset DU-054-4 yang tidak punya pemegang.
  - K4: dialog dibuka oleh Joko S sebagai pemegang aset DU-054-5, tanpa hak Aktor Missing; aset punya transaksi Borrow `BRW-2026-0141`; baris Borrow yang tidak boleh tampil adalah `Scanner Zebra DS2208 in BRW-2026-0141 will be closed as missing.`, dari Asset Name `Scanner Zebra DS2208` dan Borrow `BRW-2026-0141`.
  - K5: dialog dibuka oleh Pelapor admin untuk aset DU-054-4 dengan isian awal What happened dari DU-054-10.
  - K6: dialog dibuka oleh Pelapor admin untuk aset DU-054-2 dan DU-054-3; simpan berhasil untuk DU-054-2 dan dilewati untuk DU-054-3.
  - K7: dialog dibuka oleh Joko S untuk aset DU-054-5; simpan berhasil.
  - K8: dialog dibuka oleh Joko S untuk aset DU-054-5 dan DU-054-6; simpan berhasil untuk DU-054-5 dan dilewati untuk DU-054-6.
  - K9: dialog dibuka oleh Pelapor admin untuk aset DU-054-2, DU-054-3, DU-054-4, dan DU-054-7; tidak ada yang berhasil: DU-054-2 sudah punya record berjalan, DU-054-3 sudah Disposed, DU-054-4 di luar cakupan Group pelapor, dan efek modul pemilik DU-054-7 gagal.
  - K10: dialog dibuka oleh Joko S untuk aset DU-054-6 dan DU-054-5; tidak ada yang berhasil: DU-054-6 tidak lagi dipegang Joko S dan efek modul pemilik DU-054-5 gagal.
  - K11: dialog dibuka oleh Pelapor admin untuk aset DU-054-1; aset baru saja dilaporkan oleh Rina W saat Submit; Alert yang diharapkan `Hand Pallet Truck was just reported missing by Rina W.`, dari Asset Name `Hand Pallet Truck` dan User Name `Rina W`.
  - K12: dialog dibuka oleh Pelapor admin untuk aset DU-054-2 dan DU-054-3; kedua aset baru saja dilaporkan oleh Rina W saat Submit.
  - K13: dialog dibuka oleh Pelapor admin untuk aset DU-054-1; simpan pertama gagal karena error server, simpan berikutnya berhasil.
  - K14: dialog dibuka oleh Pelapor admin untuk aset DU-054-1; simpan gagal karena timeout.
  - K15: dialog dibuka oleh Pelapor admin untuk aset DU-054-1; respons simpan belum diterima sampai langkah menyatakannya.
  - K16: dialog dibuka oleh Joko S untuk aset DU-054-5; simpan gagal karena error server.
  - K17: halaman Assets menerima jumlah record Waiting for Confirmation dan Missing dari DU-054-11.
  - K18: halaman Assets menerima jumlah record Waiting for Confirmation dan Missing dari DU-054-12.
  - K19: dialog dibuka oleh Pelapor admin untuk aset DU-054-6 dan DU-054-2; DU-054-2 sudah punya record berjalan dengan Borrow dari DU-054-23, sedangkan DU-054-6 layak dengan Borrow dari DU-054-23.
  - K20: halaman Assets menampilkan aset DU-054-1 terpilih; dialog dibuka oleh Pelapor admin untuk aset itu; simpan gagal karena error server.
  - K21: dialog dibuka oleh Pelapor admin untuk aset DU-054-2 dengan kotak dampak DU-054-24.

## Test Steps

### Tampilan awal dialog satu aset
1. Tampilkan Dialog Report Missing dengan kondisi K1
2. Verifikasi judul dialog `Report Missing`
3. Verifikasi dialog hanya memuat satu isian, yaitu What happened
4. Verifikasi dialog memuat kotak dampak serta tombol `[Cancel]` dan `[Report Missing]`
5. Verifikasi header aset menampilkan nama `Hand Pallet Truck - 3` dan Asset ID `HPT-2026-0003`
6. Verifikasi header aset menampilkan foto aset `hpt-2026-0003.jpg`
7. Verifikasi header aset menampilkan tipe TAG `RFID`
8. Verifikasi header aset menampilkan Brand `Jungheinrich`, Group `Warehouse`, dan Model/Type `JH-HPT25`
9. Verifikasi header aset menampilkan Asset Status `Assigned`
10. Verifikasi What happened bertanda wajib
11. Verifikasi isian What happened kosong
12. Verifikasi placeholder isian What happened `Enter what happened`
13. Verifikasi kotak dampak memuat baris `Hand Pallet Truck in BRW-2026-0141 will be closed as missing.`
14. Verifikasi kotak dampak memuat tepat satu baris penutupan transaksi, yaitu untuk aset `Hand Pallet Truck`
15. Verifikasi kotak dampak memuat baris `Joko S and the asset admins will be notified.`
16. Verifikasi kotak dampak tidak memuat baris pratinjau efek pada transaksi Disposal maupun transaksi Draft

### Dua aset: judul jamak dan seluruh aset tampil
17. Tampilkan Dialog Report Missing dengan kondisi K2
18. Verifikasi judul dialog `Report Missing Assets`
19. Verifikasi header aset `Laptop Dell Latitude 5420 - 22` dengan Asset ID `LPT-2026-0022` tampil
20. Verifikasi header aset `Monitor LG 27UL500 - 11` dengan Asset ID `MON-2026-0011` tampil
21. Verifikasi kotak dampak memuat baris `Laptop Dell Latitude 5420 in BRW-2026-0152 will be closed as missing.`

### Aset tanpa pemegang
22. Tampilkan Dialog Report Missing dengan kondisi K3
23. Verifikasi judul dialog `Report Missing`
24. Verifikasi kotak dampak memuat baris `The asset admins will be notified.`
25. Verifikasi kotak dampak tidak memuat baris yang menyebut nama pemegang

### Pemegang tanpa hak Aktor Missing
26. Tampilkan Dialog Report Missing dengan kondisi K4
27. Verifikasi header aset `Scanner Zebra DS2208 - 2` dengan Asset ID `SCN-2026-0002` tampil
28. Verifikasi baris `Scanner Zebra DS2208 in BRW-2026-0141 will be closed as missing.` tidak tampil di kotak dampak

### Titik masuk mengisi awal What happened
29. Tampilkan Dialog Report Missing dengan kondisi K5
30. Verifikasi isian What happened berisi `Aset tidak ditemukan saat pengecekan rak`
31. Ganti isi What happened dengan `Aset tidak ditemukan saat pengecekan rak, terakhir terlihat di ruang arsip`
32. Verifikasi isian What happened berisi `Aset tidak ditemukan saat pengecekan rak, terakhir terlihat di ruang arsip`

### What happened kosong ditolak saat Submit
33. Tampilkan Dialog Report Missing dengan kondisi K1
34. Verifikasi `[Report Missing]` aktif
35. Kosongkan isian What happened
36. Klik `[Report Missing]`
37. Verifikasi caption error `What happened must not be empty` tampil di bawah isian What happened
38. Verifikasi isian What happened memiliki `aria-describedby` yang menunjuk ke caption error itu
39. Verifikasi tidak ada dialog konfirmasi kedua
40. Verifikasi `[Report Missing]` tetap aktif

### What happened berisi spasi saja ditolak sebagai kosong
41. Tampilkan Dialog Report Missing dengan kondisi K1
42. Isi What happened `   `
43. Klik `[Report Missing]`
44. Verifikasi caption error `What happened must not be empty` tampil di bawah isian What happened

### Batas panjang What happened
45. Tampilkan Dialog Report Missing dengan kondisi K1
46. Isi What happened `Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke raZ` (361 karakter)
47. Verifikasi caption error `Max. 360 characters` tampil langsung saat teks melebihi batas
48. Ganti isi What happened dengan `Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke ra` (360 karakter)
49. Verifikasi caption error `Max. 360 characters` tidak tampil
50. Ganti isi What happened dengan `Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum dipindahkan ke lantai tiga bangunan baru. Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum dipindahkan ke lantai tiga bangunan baru. Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum.` (360 karakter)
51. Verifikasi caption error `Max. 360 characters` tidak tampil
52. Ganti isi What happened dengan `Aset belum kembali ke rak  penyimpanan sejak inventarisasi akhir bulan  dan tidak ada catatan peminjaman  terbaru.  Aset belum kembali  ke rak penyimpanan sejak inventarisasi  akhir bulan dan tidak ada  catatan peminjaman terbaru.  Aset  belum kembali ke rak penyimpanan  sejak inventarisasi akhir bulan dan  tidak ada catatan peminjaman terbaru.   Aset belum.` (360 karakter)
53. Verifikasi caption error `Max. 360 characters` tidak tampil
54. Ganti isi What happened dengan `  Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke ra  `, yaitu teks batas maksimum yang diapit dua spasi di awal dan di akhir
55. Verifikasi caption error `Max. 360 characters` tidak tampil
56. Ganti isi What happened dengan `H`
57. Verifikasi isian What happened berisi `H`
58. Klik `[Report Missing]`
59. Verifikasi toast `Success, asset has been reported missing.` tampil

### Form bersih ditutup dengan tombol silang
60. Tampilkan Dialog Report Missing dengan kondisi K1
61. Klik `✕` pada dialog
62. Verifikasi dialog Report Missing tertutup tanpa dialog Unsaved Changes

### Form bersih ditutup dengan Esc
63. Tampilkan Dialog Report Missing dengan kondisi K1
64. Tekan Esc
65. Verifikasi dialog Report Missing tertutup tanpa dialog Unsaved Changes

### Form kotor ditutup dengan tombol silang memunculkan Unsaved Changes
66. Tampilkan Dialog Report Missing dengan kondisi K1
67. Isi What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
68. Klik area backdrop di luar dialog
69. Verifikasi dialog Report Missing tetap terbuka dengan isian What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
70. Klik `✕` pada dialog
71. Verifikasi dialog `Unsaved Changes` tampil di atas dialog Report Missing dengan teks `You have unsaved changes. Are you sure you want to leave?`
72. Verifikasi dialog Unsaved Changes pada dialog Report Missing memuat tombol `[Leave]` dan `[Cancel]`
73. Tekan Esc
74. Verifikasi dialog Unsaved Changes tertutup dan dialog Report Missing tetap terbuka dengan isian What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
75. Klik `✕` pada dialog
76. Klik `[Leave]`
77. Verifikasi dialog Report Missing tertutup

### Form kotor ditutup dengan Esc memunculkan Unsaved Changes
78. Tampilkan Dialog Report Missing dengan kondisi K1
79. Isi What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
80. Tekan Esc
81. Verifikasi dialog `Unsaved Changes` tampil di atas dialog Report Missing dengan teks `You have unsaved changes. Are you sure you want to leave?`
82. Klik `[Cancel]` pada dialog Unsaved Changes
83. Verifikasi dialog Report Missing tetap terbuka dengan isian What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
84. Tekan Esc
85. Klik `[Leave]`
86. Verifikasi dialog Report Missing tertutup

### Cancel pada form bersih menutup dialog tanpa toast
87. Tampilkan Dialog Report Missing dengan kondisi K1
88. Verifikasi tombol `[Cancel]` tampil
89. Klik `[Cancel]`
90. Verifikasi dialog Report Missing tertutup
91. Verifikasi tidak ada toast yang tampil

### Aksesibilitas dialog
92. Tampilkan Dialog Report Missing dengan kondisi K1
93. Verifikasi fokus berada di dalam dialog Report Missing
94. Verifikasi isian What happened memiliki `aria-required`
95. Verifikasi tombol `✕` pada dialog Report Missing memiliki label aksesibel `Close dialog`
96. Tekan Tab sepuluh kali berturut-turut
97. Verifikasi fokus tetap berada di dalam dialog Report Missing
98. Klik `✕` pada dialog
99. Verifikasi fokus kembali ke elemen pemicu dialog Report Missing

### Simpan lambat: tombol dan kontrol terkunci, satu toast
100. Tampilkan Dialog Report Missing dengan kondisi K15
101. Isi What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
102. Klik `[Report Missing]`
103. Verifikasi `[Report Missing]` tidak bisa diklik selama simpan berjalan
104. Verifikasi isian What happened, `[Cancel]`, dan `✕` tidak bisa dipakai selama simpan berjalan
105. Klik `[Report Missing]`
106. Respons simpan diterima
107. Verifikasi hanya satu toast `Success, asset has been reported missing.` tampil

### Simpan berhasil oleh Pelapor admin
108. Tampilkan Dialog Report Missing dengan kondisi K1
109. Isi What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
110. Klik `[Report Missing]`
111. Verifikasi toast `Success, asset has been reported missing.` tampil
112. Verifikasi dialog Report Missing tertutup
113. Waktu berlalu sampai 4000 ms sejak toast tampil
114. Verifikasi toast `Success, asset has been reported missing.` sudah hilang dari halaman sesudah animasi keluarnya selesai

### Simpan berhasil oleh pemegang
115. Tampilkan Dialog Report Missing dengan kondisi K7
116. Isi What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
117. Klik `[Report Missing]`
118. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil

### Simpan berhasil sebagian oleh Pelapor admin
119. Tampilkan Dialog Report Missing dengan kondisi K6
120. Isi What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
121. Klik `[Report Missing]`
122. Verifikasi toast `Success, asset has been reported missing. Some items were skipped.` tampil

### Simpan berhasil sebagian oleh pemegang
123. Tampilkan Dialog Report Missing dengan kondisi K8
124. Isi What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
125. Klik `[Report Missing]`
126. Verifikasi toast `Success, your report has been sent to the asset admins. Some items were skipped.` tampil

### Tidak ada aset berhasil: dialog tetap terbuka dengan alasan per aset
127. Tampilkan Dialog Report Missing dengan kondisi K9
128. Verifikasi judul dialog `Report Missing Assets`
129. Isi What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
130. Klik `[Report Missing]`
131. Verifikasi dialog Report Missing tetap terbuka
132. Verifikasi aset `Laptop Dell Latitude 5420 - 22` tampil dengan keterangan `Already reported missing`
133. Verifikasi keterangan aset `Laptop Dell Latitude 5420 - 22` disertai tautan `Missing Log`
134. Verifikasi aset `Monitor LG 27UL500 - 11` tampil dengan keterangan `Disposed`
135. Verifikasi aset `Toyota Innova - 2` tampil dengan keterangan `Outside your group`
136. Verifikasi aset `Printer HP LaserJet M404 - 5` tampil dengan keterangan `Error, failed to report asset as missing.`
137. Verifikasi toast `Success, asset has been reported missing.` tidak tampil
138. Verifikasi `[Report Missing]` tetap aktif

### Tidak ada aset berhasil pada laporan pemegang
139. Tampilkan Dialog Report Missing dengan kondisi K10
140. Isi What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
141. Klik `[Report Missing]`
142. Verifikasi dialog Report Missing tetap terbuka
143. Verifikasi aset `Camera Canon EOS - 1` tampil dengan keterangan `No longer held by you`
144. Verifikasi aset `Scanner Zebra DS2208 - 2` tampil dengan keterangan `Error, failed to send your report.`
145. Verifikasi toast `Success, your report has been sent to the asset admins.` tidak tampil

### Aset baru dilaporkan orang lain pada satu aset
146. Tampilkan Dialog Report Missing dengan kondisi K11
147. Isi What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
148. Klik `[Report Missing]`
149. Verifikasi Alert `Hand Pallet Truck was just reported missing by Rina W.` tampil di dialog Report Missing
150. Verifikasi Alert itu memuat tombol `[View Missing Log]`
151. Verifikasi dialog Report Missing tetap terbuka

### Aset baru dilaporkan orang lain pada banyak aset
152. Tampilkan Dialog Report Missing dengan kondisi K12
153. Isi What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
154. Klik `[Report Missing]`
155. Verifikasi aset `Laptop Dell Latitude 5420 - 22` tampil dengan keterangan `Already reported missing`
156. Verifikasi aset `Monitor LG 27UL500 - 11` tampil dengan keterangan `Already reported missing`
157. Verifikasi dialog Report Missing tetap terbuka

### Simpan gagal karena error server: isian dipertahankan dan submit ulang berhasil
158. Tampilkan Dialog Report Missing dengan kondisi K13
159. Isi What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
160. Klik `[Report Missing]`
161. Verifikasi toast `Error, failed to report asset as missing.` tampil
162. Verifikasi dialog Report Missing tetap terbuka
163. Verifikasi isian What happened tetap berisi `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
164. Verifikasi `[Report Missing]` aktif lagi
165. Waktu berlalu sampai 4000 ms sejak toast tampil
166. Verifikasi toast `Error, failed to report asset as missing.` sudah hilang dari halaman sesudah animasi keluarnya selesai[^drift-1]
167. Klik `[Report Missing]`
168. Verifikasi toast `Success, asset has been reported missing.` tampil
169. Verifikasi dialog Report Missing tertutup

### Simpan gagal karena timeout
170. Tampilkan Dialog Report Missing dengan kondisi K14
171. Isi What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
172. Klik `[Report Missing]`
173. Verifikasi toast `Connection problem. Please try again.` tampil setelah simpan Report Missing
174. Verifikasi dialog Report Missing tetap terbuka
175. Verifikasi isian What happened tetap berisi `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
176. Verifikasi `[Report Missing]` aktif lagi

### Simpan gagal oleh pemegang
177. Tampilkan Dialog Report Missing dengan kondisi K16
178. Isi What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
179. Klik `[Report Missing]`
180. Verifikasi toast `Error, failed to send your report.` tampil
181. Verifikasi dialog Report Missing tetap terbuka

### Badge tab Missing tidak tampil saat jumlah nol
182. Tampilkan Dialog Report Missing dengan kondisi K17
183. Verifikasi tab `Missing` pada halaman Assets tampil
184. Verifikasi tab `Missing` tidak menampilkan badge jumlah

### Badge tab Missing tampil saat jumlah lebih dari nol
185. Tampilkan Dialog Report Missing dengan kondisi K18
186. Verifikasi tab `Missing` pada halaman Assets menampilkan badge jumlah `2`

### Tipe TAG NFC dan QR pada header aset
187. Tampilkan Dialog Report Missing dengan kondisi K2
188. Verifikasi header aset `Laptop Dell Latitude 5420 - 22` menampilkan tipe TAG `NFC`
189. Verifikasi header aset `Monitor LG 27UL500 - 11` menampilkan tipe TAG `QR`

### Tipe TAG GPS pada header aset
190. Tampilkan Dialog Report Missing dengan kondisi K3
191. Verifikasi header aset `Toyota Innova - 2` menampilkan tipe TAG `GPS`

### Tipe TAG BLE pada header aset
192. Tampilkan Dialog Report Missing dengan kondisi K4
193. Verifikasi header aset `Scanner Zebra DS2208 - 2` menampilkan tipe TAG `BLE`

### Kotak dampak hanya menghitung aset yang layak
194. Tampilkan Dialog Report Missing dengan kondisi K19
195. Verifikasi kotak dampak memuat baris `Camera Canon EOS in BRW-2026-0155 will be closed as missing.`
196. Verifikasi kotak dampak memuat baris `Joko S and the asset admins will be notified.`
197. Verifikasi kotak dampak tidak memuat baris `Laptop Dell Latitude 5420 in BRW-2026-0150 will be closed as missing.`
198. Verifikasi judul dialog `Report Missing Assets`

### Simpan gagal mempertahankan seleksi aset dan memuat ulang daftar
199. Tampilkan Dialog Report Missing dengan kondisi K20
200. Verifikasi baris aset `Hand Pallet Truck - 3` pada halaman Assets terpilih
201. Isi What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
202. Klik `[Report Missing]`
203. Verifikasi toast `Error, failed to report asset as missing.` tampil
204. Verifikasi dialog Report Missing tetap terbuka
205. Verifikasi baris aset `Hand Pallet Truck - 3` pada halaman Assets tetap terpilih
206. Verifikasi daftar aset pada halaman Assets dimuat ulang

### Toast error ditutup lewat tombol tutup
207. Tampilkan Dialog Report Missing dengan kondisi K13
208. Isi What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan`
209. Klik `[Report Missing]`
210. Verifikasi toast `Error, failed to report asset as missing.` tampil
211. Klik tombol tutup pada toast `Error, failed to report asset as missing.`
212. Verifikasi toast `Error, failed to report asset as missing.` sudah hilang dari halaman sesudah animasi keluarnya selesai

### Kotak dampak memuat satu baris per aset yang barisnya ditutup
213. Tampilkan Dialog Report Missing dengan kondisi K2
214. Verifikasi kotak dampak memuat baris `Monitor LG 27UL500 in BRW-2026-0153 will be closed as missing.`

### Kotak dampak memuat baris penutupan Assignment
215. Tampilkan Dialog Report Missing dengan kondisi K21
216. Verifikasi kotak dampak memuat baris `Laptop Dell Latitude 5420 in ASG-2026-0071 will be closed as missing.`
217. Verifikasi kotak dampak memuat baris `Andi P and the asset admins will be notified.`

[^drift-1]: Drift foundation vs kontrak komponen. PRD tidak menyatakan durasi toast; ekspektasi baku EB-FB-4: «Toast error bertahan sampai ditutup». foundation `toast-copy.md` Aturan Terkunci #12: «Auto-dismiss: Success 4 detik; Error persists sampai di-dismiss manual.»; kontrak `Toast#2`: «Every severity (`info`, `success`, `warning`, `danger`) auto-dismisses the same way; no severity persists on its own.» Diasersi: kontrak, sehingga toast error ikut hilang sendiri sesudah 4000 ms dan hilang dari halaman sesudah animasi keluar 200 ms (`Toast#10`) (SB-7).

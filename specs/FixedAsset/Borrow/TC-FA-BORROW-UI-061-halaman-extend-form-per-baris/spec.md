---
id: TC-FA-BORROW-UI-061-halaman-extend-form-per-baris
title: "Halaman Extend: Extend By dan Reason per baris aktif, baris nonaktif beralasan, dan New Due Date"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FI-BRW-150", "FI-BRW-151", "FI-BRW-152", "FI-BRW-153", "FI-BRW-154", "FI-BRW-155", "FI-BRW-156", "FI-BRW-157", "FI-BRW-158", "FI-BRW-159", "FI-BRW-160", "FI-BRW-161", "FI-BRW-162", "FI-BRW-163", "FI-BRW-164", "FI-BRW-165", "FI-BRW-166", "FI-BRW-167", "FI-BRW-168", "FI-BRW-169", "FI-BRW-170", "FI-BRW-171", "FI-BRW-172", "FI-BRW-173", "FI-BRW-174", "FI-BRW-175", "FI-BRW-176", "FI-BRW-177", "FI-BRW-178", "FI-BRW-179", "FI-BRW-180", "FI-BRW-181", "FI-BRW-182", "FI-BRW-183", "FI-BRW-184", "FI-BRW-185", "FI-BRW-186", "FLD-BRW-09", "FLD-BRW-10", "V-BRW-21", "V-BRW-22", "V-BRW-23", "V-BRW-24", "V-BRW-25", "§4.2.7#p1", "§4.2.7#p2", "§4.2.7#p4", "§4.2.7#p6", "EB-FRM-1@form-extend", "EB-FRM-4@form-extend", "EB-ERR-1@extend"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-150": 3
  "FI-BRW-151": 4
  "FI-BRW-152": [37, 39]
  "FI-BRW-153": 94
  "FI-BRW-154": 37
  "FI-BRW-155": 44
  "FI-BRW-156": [50, 53]
  "FI-BRW-157": 68
  "FI-BRW-158": [69, 70, 71]
  "FI-BRW-159": 78
  "FI-BRW-160": [69, 72, 73]
  "FI-BRW-161": 74
  "FI-BRW-162": 75
  "FI-BRW-163": 76
  "FI-BRW-164": 77
  "FI-BRW-165": [40, 89]
  "FI-BRW-166": 35
  "FI-BRW-167": [82, 83]
  "FI-BRW-168": 63
  "FI-BRW-169": 66
  "FI-BRW-170": [23, 25]
  "FI-BRW-171": 21
  "FI-BRW-172": 21
  "FI-BRW-173": 66
  "FI-BRW-174": 66
  "FI-BRW-175": [117, 123, 129]
  "FI-BRW-176": [119, 125, 131]
  "FI-BRW-177": [101, 102]
  "FI-BRW-178": 103
  "FI-BRW-179": [104, 105, 106]
  "FI-BRW-180": 107
  "FI-BRW-181": 109
  "FI-BRW-182": 112
  "FI-BRW-183": 113
  "FI-BRW-184": 94
  "FI-BRW-185": 98
  "FI-BRW-186": 93
  "FLD-BRW-09": [44, 50, 66]
  "FLD-BRW-10": [38, 58, 60]
  "V-BRW-21": [66, 69, 74, 75, 76, 77]
  "V-BRW-22": 37
  "V-BRW-23": [50, 53]
  "V-BRW-24": [38, 47]
  "V-BRW-25": 82
  "§4.2.7#p1": 2
  "§4.2.7#p2": [5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 20, 31]
  "§4.2.7#p4": 33
  "§4.2.7#p6": [104, 105, 106]
  "EB-FRM-1@form-extend": [136, 137, 139]
  "EB-FRM-4@form-extend": [58, 60]
  "EB-ERR-1@extend": [144, 145, 146, 148, 153, 154, 156]
anchor: [56, 80]
coverage:
  web: automated
---

# Halaman Extend: Extend By dan Reason per baris aktif, baris nonaktif beralasan, dan New Due Date

## Prerequisites
- Aktor: Aktor Borrow dengan cakupan Group `Finance`.
- Layar awal: Halaman Extend
- Komponen: Halaman Extend
- Data:
  - DU-061-1: Borrower `Budi Santoso`.
  - DU-061-2: baris aktif, Name `Laptop Dell Latitude 5420`, Asset ID `AST-0101`, Transaction ID `BRW-0101`, Group `Finance`, Brand `Dell`, Model/Type `Latitude 5420`, TAG `TAG-0101`, Category `Laptop`, Current Due Date `10/12/2026`, Extensions `0 / 3`, Max Duration `14 days`, Approval `Auto-approve`.
  - DU-061-3: baris aktif, Name `Kamera Sony A7`, Asset ID `AST-0102`, Transaction ID `BRW-0101`, Group `Finance`, Brand `Sony`, Model/Type `A7`, TAG `TAG-0102`, Category `Kamera`, Current Due Date `20/12/2026`, Extensions `1 / 3`, Max Duration `14 days`, Approval `Needs approval`.
  - DU-061-4: baris aktif Overdue, Name `Printer Epson L3110`, Asset ID `AST-0103`, Transaction ID `BRW-0102`, Group `Finance`, Brand `Epson`, Model/Type `L3110`, TAG `TAG-0103`, Category `Printer`, Current Due Date `05/11/2026`, Extensions `0 / 3`, Max Duration `30 days`, Approval `Needs approval`.
  - DU-061-5: baris aktif dengan sisa durasi terbatas, Name `Monitor LG 24MK430`, Asset ID `AST-0104`, Transaction ID `BRW-0103`, Group `Finance`, Brand `LG`, Model/Type `24MK430`, TAG `TAG-0104`, Category `Monitor`, Handover `05/12/2026`, Current Due Date `12/12/2026`, Extensions `0 / 3`, Max Duration `10 days`, Approval `Auto-approve`.
  - DU-061-6: baris nonaktif, Name `Mesin Fotokopi Canon iR2630`, Asset ID `AST-0105`, Transaction ID `BRW-0104`, Group `Finance`, Brand `Canon`, Model/Type `iR2630`, TAG `TAG-0105`, Category `Mesin Kantor`, Current Due Date `15/12/2026`, Extensions `0 / 3`, Max Duration `14 days`, Activity Lock `Under Maintenance`.
  - DU-061-7: baris nonaktif, Name `Genset Honda EU20i`, Asset ID `AST-0106`, Transaction ID `BRW-0104`, Group `Finance`, Brand `Honda`, Model/Type `EU20i`, TAG `TAG-0106`, Category `Mesin Kantor`, Current Due Date `15/12/2026`, Extensions `0 / 3`, Max Duration `14 days`, Activity Lock `In Audit`.
  - DU-061-8: baris nonaktif, Name `Scanner Fujitsu fi-7160`, Asset ID `AST-0107`, Transaction ID `BRW-0104`, Group `Finance`, Brand `Fujitsu`, Model/Type `fi-7160`, TAG `TAG-0107`, Category `Mesin Kantor`, Current Due Date `15/12/2026`, Extensions `0 / 3`, Max Duration `14 days`, status aset `Unmanaged`.
  - DU-061-9: baris nonaktif, Name `Tablet Samsung Galaxy Tab A8`, Asset ID `AST-0108`, Transaction ID `BRW-0105`, Group `Finance`, Brand `Samsung`, Model/Type `Galaxy Tab A8`, TAG `TAG-0108`, Category `Tablet`, Current Due Date `16/12/2026`, Extensions `0 / 3`, Max Duration `14 days`, Damage Report aktif.
  - DU-061-10: baris nonaktif, Name `Speaker JBL PartyBox`, Asset ID `AST-0109`, Transaction ID `BRW-0106`, Group `Finance`, Brand `JBL`, Model/Type `PartyBox`, TAG `TAG-0109`, Category `Audio`, Current Due Date `17/12/2026`, Extensions `1 / 3`, Max Duration `14 days`, pengajuan Extend lain sedang menunggu approval.
  - DU-061-11: baris nonaktif, Name `Drone DJI Mini 3`, Asset ID `AST-0110`, Transaction ID `BRW-0107`, Group `Finance`, Brand `DJI`, Model/Type `Mini 3`, TAG `TAG-0110`, Category `Drone`, Current Due Date `18/12/2026`, Extensions `3 / 3`, Max Duration `30 days`.
  - DU-061-12: baris nonaktif, Name `Proyektor BenQ MX550`, Asset ID `AST-0111`, Transaction ID `BRW-0108`, Group `Finance`, Brand `BenQ`, Model/Type `MX550`, TAG `TAG-0111`, Category `Proyektor`, Handover `01/12/2026`, Current Due Date `07/12/2026`, Extensions `1 / 3`, Max Duration `7 days`.
  - DU-061-13: baris nonaktif dengan beberapa sebab, Name `Kamera Canon EOS 200D`, Asset ID `AST-0112`, Transaction ID `BRW-0109`, Group `Finance`, Brand `Canon`, Model/Type `EOS 200D`, TAG `TAG-0112`, Category `Kamera`, Current Due Date `19/12/2026`, Extensions `3 / 3`, Max Duration `14 days`, Activity Lock `Under Maintenance`, Damage Report aktif.
  - DU-061-14: baris tambahan sampai jumlah baris melebihi Bulk Transaction Row Limit, Name `Kursi Lipat Gudang {n}`, Asset ID `AST-02{n}`, Transaction ID `BRW-0110`, Group `Finance`, Current Due Date `20/12/2026`, Approval `Auto-approve`.
  - DU-061-25: baris dari My Asset, Name `Mouse Logitech MX Master 3`, Asset ID `AST-0113`, Transaction ID `BRW-0111`, Group `Finance`, Current Due Date `18/12/2026`, Approval `Review`.
  - DU-061-26: 10 baris tambahan di dialog Select Asset, Name `Kursi Lipat Cabang {n}`, Asset ID `AST-03{n}`, Transaction ID `BRW-0112`, Group `Finance`, Current Due Date `20/12/2026`, Note `-`.
  - DU-061-27: pinjaman milik pengguna sendiri di dialog Select Asset dari My Asset, Name `Headset Jabra Evolve2`, Asset ID `AST-0114`, Transaction ID `BRW-0113`, Group `Finance`, Current Due Date `21/12/2026`, Note `-`.
  - DU-061-28: baris `On behalf of` milik pengguna sebagai PIC di dialog Select Asset dari My Asset, Name `Webcam Logitech C920`, Asset ID `AST-0115`, Transaction ID `BRW-0114`, Group `Finance`, Current Due Date `22/12/2026`, Note `-`.
  - Nilai New Due Date yang diharapkan: `12/12/2026` dari DU-061-2 `10/12/2026` ditambah Extend By `2` hari, `22/12/2026` dari DU-061-3 `20/12/2026` ditambah Extend By `2` hari, `21/11/2026` dari hari ini `18/11/2026` ditambah Extend By `3` hari untuk DU-061-4 yang Overdue, dan batas total DU-061-5 `14/12/2026` dari Handover `05/12/2026` ditambah Max Duration `10 days`.
  - DU-061-30: tanggal hari ini pada K2, `18/11/2026`.
- Kondisi:
  - K1: Date Format bernilai `DD/MM/YYYY`, halaman dibuka lewat row action Request Extension pada satu aset, Borrower DU-061-1, tabel berisi DU-061-2.
  - K2: Date Format bernilai `DD/MM/YYYY`, tanggal hari ini `18/11/2026`, halaman dibuka dari Borrow Detail, Borrower DU-061-1, tabel berisi DU-061-2, DU-061-3, dan DU-061-4.
  - K3: Date Format bernilai `DD/MM/YYYY`, Borrower DU-061-1, tabel berisi DU-061-2 dan DU-061-3.
  - K4: Borrower DU-061-1, tabel berisi DU-061-2, DU-061-3, dan DU-061-6.
  - K5: Date Format bernilai `DD/MM/YYYY`, Borrower DU-061-1, tabel berisi DU-061-5.
  - K6: Borrower DU-061-1, tabel berisi DU-061-2, DU-061-6, DU-061-7, DU-061-8, DU-061-9, DU-061-10, DU-061-11, DU-061-12, dan DU-061-13.
  - K7: Borrower DU-061-1, tabel berisi DU-061-6 dan DU-061-9.
  - K8: Borrower DU-061-1, tabel berisi DU-061-2, dialog Select Asset memuat DU-061-3, DU-061-6, DU-061-9, lalu DU-061-26 sehingga lebih dari satu halaman.
  - K9: Borrower DU-061-1, tabel berisi DU-061-2 dan DU-061-3, dialog Select Asset memuat DU-061-2.
  - K10: Borrower DU-061-1, tabel berisi DU-061-2 dan DU-061-14, dan jumlah baris melebihi Bulk Transaction Row Limit.
  - K11: Borrower DU-061-1, tabel berisi DU-061-3 dan DU-061-14, dan jumlah baris melebihi Bulk Transaction Row Limit.
  - K12: halaman dibuka dari My Asset, Borrower DU-061-1, tabel berisi DU-061-25 dan DU-061-14, dan jumlah baris melebihi Bulk Transaction Row Limit.
  - K13: Date Format bernilai `DD/MM/YYYY`, Borrower DU-061-1, tabel berisi DU-061-2, simpan lambat.
  - K14: Date Format bernilai `DD/MM/YYYY`, Borrower DU-061-1, tabel berisi DU-061-2, Submit pertama dijawab error server, Submit berikutnya berhasil.
  - K15: Date Format bernilai `DD/MM/YYYY`, Borrower DU-061-1, tabel berisi DU-061-2, Submit pertama tidak mendapat respons karena koneksi putus, Submit berikutnya berhasil.
  - K16: halaman dibuka dari My Asset, Borrower DU-061-1, tabel berisi DU-061-25, dialog Select Asset memuat DU-061-27 dan DU-061-28.

## Test Steps

### Halaman dibuka dari row action pada satu aset
1. Tampilkan Halaman Extend dengan kondisi K1
2. Verifikasi tabel memuat baris `Laptop Dell Latitude 5420`
3. Verifikasi Extend By dan Reason baris `Laptop Dell Latitude 5420` kosong
4. Verifikasi New Due Date baris `Laptop Dell Latitude 5420` menampilkan `—`
5. Verifikasi footer menampilkan tombol `[Cancel]` dan `[Extend]`

### Susunan halaman dan New Due Date per baris
6. Tampilkan Halaman Extend dengan kondisi K2
7. Verifikasi judul `Extension Request` tampil di dalam card utama
8. Verifikasi info Borrower menampilkan `Budi Santoso`
9. Verifikasi toolbar menampilkan kotak Search, Filter `Asset Name`, `Group`, `Brand`, `Model/Type`, `Transaction ID`, dan `Current Due Date`, serta tombol `[+ Asset]`
10. Verifikasi tabel menampilkan kolom `Photo`, `Name`, `Asset ID`, `Transaction ID`, `Group`, `Brand`, `Model/Type`, `TAG`, `Category`, `Current Due Date`, `Extensions`, `Max Duration`, `Extend By`, `New Due Date`, `Approval`, dan `Reason`
11. Verifikasi kolom Extensions baris `Kamera Sony A7` menampilkan `1 / 3`
12. Verifikasi kolom Approval baris `Laptop Dell Latitude 5420` menampilkan `Auto-approve`
13. Verifikasi kolom Approval baris `Kamera Sony A7` menampilkan `Needs approval`
14. Verifikasi catatan di atas footer menampilkan `2 assets need approval before the new due date applies.`
15. Verifikasi footer menampilkan tombol `[Cancel]` dan `[Submit Extension]`
16. Centang baris `Laptop Dell Latitude 5420`
17. Verifikasi bulk action `Set Extension` dan `Remove from List` tampil
18. Isi input Extend by pada `Set Extension` dengan `2`
19. Klik `[Apply]`
20. Verifikasi Extend By baris `Laptop Dell Latitude 5420` terisi `2`
21. Verifikasi New Due Date baris `Laptop Dell Latitude 5420` menampilkan `12/12/2026`, dari Current Due Date `10/12/2026` ditambah `2` hari
22. Isi Extend By baris `Kamera Sony A7` dengan `2`
23. Verifikasi New Due Date baris `Kamera Sony A7` menampilkan `22/12/2026`, dari Current Due Date `20/12/2026` ditambah `2` hari, sehingga baris dengan Due date berbeda diperpanjang dengan durasi yang sama
24. Isi Extend By baris `Printer Epson L3110` dengan `3`
25. Verifikasi New Due Date baris `Printer Epson L3110` menampilkan `21/11/2026`, dihitung dari hari ini `18/11/2026` karena baris Overdue

### Submit campuran: sebagian langsung berlaku, sebagian menunggu approval
26. Tampilkan Halaman Extend dengan kondisi K3
27. Isi Extend By baris `Laptop Dell Latitude 5420` dengan `2`
28. Isi Reason baris `Laptop Dell Latitude 5420` dengan `Proyek audit aset tahunan masih berjalan`
29. Isi Extend By baris `Kamera Sony A7` dengan `2`
30. Isi Reason baris `Kamera Sony A7` dengan `Proyek audit aset tahunan masih berjalan`
31. Verifikasi catatan di atas footer menampilkan `1 asset needs approval before the new due date applies.`
32. Klik `[Submit Extension]`
33. Verifikasi toast `Success, due date has been changed for 1 of 2 assets. 1 submitted for approval.` tampil

### Extend By dan Reason wajib di setiap baris aktif
34. Tampilkan Halaman Extend dengan kondisi K4
35. Verifikasi tombol `[Submit Extension]` aktif walau baris `Mesin Fotokopi Canon iR2630` nonaktif
36. Klik `[Submit Extension]`
37. Verifikasi pesan `Extend by must not be empty` tampil di bawah input Extend By baris `Laptop Dell Latitude 5420`
38. Verifikasi pesan `Reason must not be empty` tampil di bawah input Reason baris `Laptop Dell Latitude 5420`
39. Verifikasi pesan `Extend by must not be empty` tampil di bawah input Extend By baris `Kamera Sony A7`
40. Verifikasi baris `Mesin Fotokopi Canon iR2630` tidak menampilkan pesan `Extend by must not be empty`
41. Isi Extend By baris `Laptop Dell Latitude 5420` dengan `2`
42. Kosongkan Extend By baris `Laptop Dell Latitude 5420`
43. Klik `[Submit Extension]`
44. Verifikasi pesan `Extend by must not be empty` tampil di bawah input Extend By baris `Laptop Dell Latitude 5420` setelah dikosongkan
45. Isi Reason baris `Laptop Dell Latitude 5420` hanya dengan spasi
46. Klik `[Submit Extension]`
47. Verifikasi pesan `Reason must not be empty` tampil di bawah input Reason baris `Laptop Dell Latitude 5420` yang hanya berisi spasi
48. Isi Extend By baris `Laptop Dell Latitude 5420` dengan `0`
49. Klik `[Submit Extension]`
50. Verifikasi caption `Enter an extension of at least 1` tampil di bawah input Extend By baris `Laptop Dell Latitude 5420`
51. Ganti isi Extend By baris `Laptop Dell Latitude 5420` dengan `-3`
52. Klik `[Submit Extension]`
53. Verifikasi caption `Enter an extension of at least 1` tampil di bawah input Extend By baris `Laptop Dell Latitude 5420` untuk nilai negatif

### Batas karakter Reason
54. Tampilkan Halaman Extend dengan kondisi K3
55. Klik `[Submit Extension]`
56. Verifikasi pesan `Reason must not be empty` tampil di bawah input Reason baris `Laptop Dell Latitude 5420` sebelum Reason diisi
57. Isi Reason baris `Laptop Dell Latitude 5420` dengan `Perpanjangan dibutuhkan karena proyek inventarisasi aset gudang cabang Surabaya belum selesai dan laporan akhir menunggu` (120 karakter)
58. Verifikasi pesan `Max. 120 characters` tidak tampil di bawah input Reason baris `Laptop Dell Latitude 5420`
59. Ganti isi Reason baris `Laptop Dell Latitude 5420` dengan `Perpanjangan dibutuhkan karena proyek inventarisasi aset gudang cabang Surabaya belum selesai dan laporan akhir menunggu.` (121 karakter)
60. Verifikasi pesan `Max. 120 characters` tampil di bawah input Reason baris `Laptop Dell Latitude 5420`

### Extend By melewati Max duration
61. Tampilkan Halaman Extend dengan kondisi K5
62. Isi Extend By baris `Monitor LG 24MK430` dengan `5`
63. Verifikasi input Extend By baris `Monitor LG 24MK430` tetap aktif dan dapat diisi walau nilainya melewati Max duration
64. Isi Reason baris `Monitor LG 24MK430` dengan `Proyek audit aset tahunan masih berjalan`
65. Klik `[Extend]`
66. Verifikasi pesan `Max 10 days in total. You can extend until 14/12/2026.` tampil di bawah input Extend By baris `Monitor LG 24MK430`

### Alasan baris nonaktif
67. Tampilkan Halaman Extend dengan kondisi K6
68. Verifikasi baris `Mesin Fotokopi Canon iR2630` tetap tampil di tabel
69. Verifikasi baris `Mesin Fotokopi Canon iR2630` menampilkan `This asset is Under Maintenance and can't be extended.` sebagai pengganti input Extend By
70. Verifikasi checkbox baris `Mesin Fotokopi Canon iR2630` disabled
71. Verifikasi Current Due Date baris `Mesin Fotokopi Canon iR2630` tetap `15/12/2026`
72. Verifikasi baris `Genset Honda EU20i` menampilkan `This asset is In Audit and can't be extended.`
73. Verifikasi baris `Scanner Fujitsu fi-7160` menampilkan `This asset is Unmanaged and can't be extended.`
74. Verifikasi baris `Tablet Samsung Galaxy Tab A8` menampilkan `This asset has a damage report. Return it first.`
75. Verifikasi baris `Speaker JBL PartyBox` menampilkan `An extension is already waiting for approval.`
76. Verifikasi baris `Drone DJI Mini 3` menampilkan `No extensions left (3 / 3).`
77. Verifikasi baris `Proyektor BenQ MX550` menampilkan `Max duration reached (7 days).`
78. Verifikasi baris `Kamera Canon EOS 200D` menampilkan hanya alasan prioritas tertinggi, `This asset is Under Maintenance and can't be extended.`

### Baris nonaktif tidak menahan Submit
79. Tampilkan Halaman Extend dengan kondisi K7
80. Verifikasi baris `Mesin Fotokopi Canon iR2630` menampilkan `This asset is Under Maintenance and can't be extended.`
81. Klik `[Extend]`
82. Verifikasi pesan `None of these assets can be extended` tampil di atas tombol
83. Verifikasi tidak ada toast sukses yang tampil sesudah `[Extend]` diklik

### Submit berhasil dengan baris nonaktif di tabel
84. Tampilkan Halaman Extend dengan kondisi K4
85. Hapus baris `Kamera Sony A7` lewat row action `Remove from List`
86. Isi Extend By baris `Laptop Dell Latitude 5420` dengan `2`
87. Isi Reason baris `Laptop Dell Latitude 5420` dengan `Proyek audit aset tahunan masih berjalan`
88. Klik `[Extend]`
89. Verifikasi toast `Success, due date has been changed to 12/12/2026.` tampil walau baris `Mesin Fotokopi Canon iR2630` nonaktif dan tidak diisi

### Baris dikeluarkan lewat Remove from List
90. Tampilkan Halaman Extend dengan kondisi K9
91. Isi Extend By baris `Laptop Dell Latitude 5420` dengan `2`
92. Klik row action `Remove from List` pada baris `Laptop Dell Latitude 5420`
93. Verifikasi baris `Kamera Sony A7` tetap tampil di tabel
94. Verifikasi baris `Laptop Dell Latitude 5420` tidak tampil di tabel tanpa dialog konfirmasi
95. Klik `[+ Asset]`
96. Centang baris `Laptop Dell Latitude 5420`
97. Klik `[Select]`
98. Verifikasi baris `Laptop Dell Latitude 5420` kembali tampil di tabel dengan Extend By kosong

### Dialog Select Asset dari tombol `[+ Asset]`
99. Tampilkan Halaman Extend dengan kondisi K8
100. Klik `[+ Asset]`
101. Verifikasi dialog Select Asset menampilkan kolom `Photo`, `Name`, `Asset ID`, `Transaction ID`, `Group`, `Current Due Date`, dan `Note`
102. Verifikasi dialog Select Asset menampilkan kotak Search, Filter `Asset Name`, `Transaction ID`, dan `Group`, serta paginasi
103. Verifikasi baris `Mesin Fotokopi Canon iR2630` tampil nonaktif di dialog Select Asset
104. Verifikasi kolom Note baris `Mesin Fotokopi Canon iR2630` menampilkan `This asset is Under Maintenance and can't be extended.`
105. Verifikasi kolom Note baris `Tablet Samsung Galaxy Tab A8` menampilkan `This asset has a damage report. Return it first.`
106. Verifikasi kolom Note baris `Kamera Sony A7` menampilkan `-`
107. Verifikasi tombol `[Select]` aktif sebelum ada baris yang dipilih
108. Klik `[Select]`
109. Verifikasi caption error `You must pick an asset` tampil di footer dialog Select Asset

### Dialog Select Asset yang dibuka dari My Asset
110. Tampilkan Halaman Extend dengan kondisi K16
111. Klik `[+ Asset]`
112. Verifikasi dialog Select Asset memuat baris `Headset Jabra Evolve2` sebagai pinjaman milik pengguna
113. Verifikasi dialog Select Asset memuat baris `Webcam Logitech C920` sebagai baris `On behalf of` milik pengguna sebagai PIC, terpisah dari baris Borrower

### Jumlah baris melebihi Bulk Transaction Row Limit pada `[Extend]`
114. Tampilkan Halaman Extend dengan kondisi K10
115. Isi Extend By baris `Laptop Dell Latitude 5420` dengan `2`
116. Klik `[Extend]`
117. Verifikasi dialog blok Bulk Transaction Row Limit tampil dengan tombol `[OK]`
118. Klik `[OK]`
119. Verifikasi Extend By baris `Laptop Dell Latitude 5420` tetap `2`

### Jumlah baris melebihi Bulk Transaction Row Limit pada `[Submit Extension]`
120. Tampilkan Halaman Extend dengan kondisi K11
121. Isi Extend By baris `Kamera Sony A7` dengan `2`
122. Klik `[Submit Extension]`
123. Verifikasi dialog blok Bulk Transaction Row Limit tampil dengan tombol `[OK]` untuk Submit Extension
124. Klik `[OK]`
125. Verifikasi Extend By baris `Kamera Sony A7` tetap `2` setelah dialog blok ditutup

### Jumlah baris melebihi Bulk Transaction Row Limit pada `[Submit Request]`
126. Tampilkan Halaman Extend dengan kondisi K12
127. Isi Extend By baris `Mouse Logitech MX Master 3` dengan `2`
128. Klik `[Submit Request]`
129. Verifikasi dialog blok Bulk Transaction Row Limit tampil dengan tombol `[OK]` untuk Submit Request
130. Klik `[OK]`
131. Verifikasi Extend By baris `Mouse Logitech MX Master 3` tetap `2` setelah dialog blok ditutup

### Saving state tombol `[Extend]`
132. Tampilkan Halaman Extend dengan kondisi K13
133. Isi Extend By baris `Laptop Dell Latitude 5420` dengan `2`
134. Isi Reason baris `Laptop Dell Latitude 5420` dengan `Proyek audit aset tahunan masih berjalan`
135. Klik `[Extend]`
136. Verifikasi tombol `[Extend]` dalam keadaan saving dan disabled
137. Verifikasi tombol `[Cancel]` dan input Extend By baris `Laptop Dell Latitude 5420` disabled selama saving
138. Klik `[Extend]` sekali lagi selama saving
139. Verifikasi `[Extend]` tetap dalam keadaan saving sampai respons diterima

### Submit Extend gagal karena error server lalu diulang
140. Tampilkan Halaman Extend dengan kondisi K14
141. Isi Extend By baris `Laptop Dell Latitude 5420` dengan `2`
142. Isi Reason baris `Laptop Dell Latitude 5420` dengan `Proyek audit aset tahunan masih berjalan`
143. Klik `[Extend]`
144. Verifikasi toast `Error, failed to extend assets.` tampil
145. Verifikasi toast error Extend tidak menampilkan tombol aksi `[Try Again]`
146. Verifikasi Extend By dan Reason baris `Laptop Dell Latitude 5420` tetap terisi dan tombol `[Extend]` aktif lagi
147. Klik `[Extend]`
148. Verifikasi toast `Success, due date has been changed to 12/12/2026.` tampil sesudah Extend diulang

### Submit Extend gagal karena koneksi putus lalu diulang
149. Tampilkan Halaman Extend dengan kondisi K15
150. Isi Extend By baris `Laptop Dell Latitude 5420` dengan `2`
151. Isi Reason baris `Laptop Dell Latitude 5420` dengan `Proyek audit aset tahunan masih berjalan`
152. Klik `[Extend]`
153. Verifikasi toast `Connection problem. Please try again.` tampil setelah Extend tidak mendapat respons
154. Verifikasi Extend By dan Reason baris `Laptop Dell Latitude 5420` tetap terisi setelah gangguan koneksi dan tombol `[Extend]` aktif lagi
155. Klik `[Extend]`
156. Verifikasi toast `Success, due date has been changed to 12/12/2026.` tampil sesudah koneksi pulih

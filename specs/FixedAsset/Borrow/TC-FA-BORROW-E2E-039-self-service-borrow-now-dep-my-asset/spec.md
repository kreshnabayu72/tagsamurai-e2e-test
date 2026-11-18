---
id: TC-FA-BORROW-E2E-039-self-service-borrow-now-dep-my-asset
title: "Self-service Borrow Now dari My Asset mobile tanpa approval dan tanpa Waiting for Handover"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FI-BRW-85", "FI-BRW-86", "FLD-BRW-06", "§4.2.12#p1", "§4.2.12#p2", "§4.2.12#p3", "§4.2.12#b1", "§4.2.12#b2", "§4.6#b6"]
smoke: []
dependsOn: ["My Asset: Borrow an Asset"]
trace:
  "FI-BRW-85": [10, 17]
  "FI-BRW-86": [19, 22]
  "FLD-BRW-06": [8, 60, 61]
  "§4.2.12#p1": 4
  "§4.2.12#p2": [6, 7, 10, 14, 46, 48, 49, 53]
  "§4.2.12#p3": [17, 19, 22, 30, 65, 74, 75, 78, 82]
  "§4.2.12#b1": [36, 37, 39]
  "§4.2.12#b2": [95, 97]
  "§4.6#b6": 4
anchor: [34, 52, 63, 96]
coverage:
  android: manual
---

# Self-service Borrow Now dari My Asset mobile tanpa approval dan tanpa Waiting for Handover

## Prerequisites
- Aktor: Borrower `Hendra Kusuma {runId}` (DU-039-1), karyawan dengan akun login dan Home Group `Head Office`, bukan PIC siapa pun. Aktor kedua: PIC `Rudi Hartono {runId}` (DU-039-9), karyawan dengan akun login dan Home Group `Head Office`, PIC karyawan tanpa akun `Joko Susilo {runId}` (DU-039-10). Borrower lain `Wawan Setiawan {runId}` (DU-039-13) hanya memicu perubahan state.
- Layar awal: halaman utama aplikasi.
- Data:
  - DU-039-1: karyawan `Hendra Kusuma {runId}`, Home Group `Head Office`, Status `Active`, Eligibility `Can borrow`.
  - DU-039-2: aset `Mesin Label Brother {runId}`, Group `Head Office`, TAG `QR`, Category `Peralatan Kantor {runId}`, Self service `ON`, Allow Borrow `Allow`, Allowed borrower `Employee in any Group`, Custody `Available`, Max Duration `7 days`, Photo at start ON.
  - DU-039-3: aset `Genset Honda EU20 {runId}`, Group `Head Office`, TAG `QR`, Category `Peralatan Kantor {runId}`, Self service `OFF`, Allow Borrow `Allow`, Allowed borrower `Employee in any Group`, Custody `Available`, Max Duration `7 days`, Photo at start ON.
  - DU-039-4: aset `Kamera Mirrorless Fujifilm {runId}`, Group `Head Office`, TAG `RFID`, Category `Peralatan Kantor {runId}`, Self service `ON`, Allow Borrow `Allow`, Allowed borrower `Employee in any Group`, Custody `Available`, Max Duration `24 hours`, Photo at start ON.
  - DU-039-5: aset `Proyektor Epson EB-W06 {runId}`, Group `Head Office`, TAG `QR`, Category `Peralatan Kantor {runId}`, Self service `ON`, Allow Borrow `Allow`, Allowed borrower `Employee in any Group`, Custody `Available`, Max Duration `7 days`, Photo at start ON.
  - DU-039-6: aset `Laptop Acer Aspire {runId}`, Group `Head Office`, TAG `NFC`, Category `Peralatan Kantor {runId}`, Self service `ON`, Allow Borrow `Allow`, Allowed borrower `Employee in any Group`, Custody `Available`, Max Duration `7 days`, Photo at start ON.
  - DU-039-7: aset `Kursi Ergonomis {runId}`, Group `Head Office`, Non TAG, Category `Non TAG {runId}`, Self service `ON`, Allow Borrow `Allow`, Allowed borrower `Employee in any Group`, Custody `Available`, Max Duration `7 days`, Photo at start ON.
  - DU-039-8: aset `Scanner Epson DS-530 {runId}`, Group `Head Office`, TAG `QR`, Category `Peralatan Kantor {runId}`, Self service `ON`, Allow Borrow `Allow`, Allowed borrower `Employee in any Group`, Custody `Available`, Max Duration `7 days`, Photo at start ON.
  - DU-039-9: karyawan `Rudi Hartono {runId}`, Home Group `Head Office`, Status `Active`, Eligibility `Can borrow`.
  - DU-039-10: karyawan tanpa akun login `Joko Susilo {runId}`, Home Group `Branch Medan`, Status `Active`, PIC `Rudi Hartono {runId}` (aktif), Eligibility `Can borrow`.
  - DU-039-11: aset `Printer Zebra ZD220 {runId}`, Group `Head Office`, TAG `QR`, Category `Peralatan Kantor {runId}`, Self service `ON`, Allow Borrow `Allow`, Allowed borrower `Same Group only`, Custody `Available`, Max Duration `7 days`, Photo at start ON.
  - DU-039-12: aset `Mikrofon Shure SM58 {runId}`, Group `Head Office`, TAG `QR`, Category `Peralatan Kantor {runId}`, Self service `ON`, Allow Borrow `Allow`, Allowed borrower `Employee in any Group`, Custody `Available`, Max Duration `7 days`, Photo at start ON.
  - DU-039-13: karyawan `Wawan Setiawan {runId}`, Home Group `Head Office`, Status `Active`, Eligibility `Can borrow`.
  - DU-039-14: isian Borrow Now aset DU-039-2: Duration `2` hari, Purpose `Pelabelan arsip gudang`; Due date T0 + 1 hari, dari tanggal Borrow Now ditambah Duration 2 hari dikurangi 1 hari.
  - DU-039-15: isian Borrow Now aset DU-039-4: Duration `3` jam, Purpose `Dokumentasi acara kantor`; Due date jam Borrow Now + 3 jam.
  - DU-039-16: isian bulk Set Duration & Purpose: Duration `2`, Purpose `Rapat evaluasi`.
  - DU-039-17: isian Borrow Now aset DU-039-8 atas nama `Joko Susilo {runId}`: Duration `1`, Purpose `Inventarisasi aset cabang`.
  - DU-039-18: isian Borrow Now aset DU-039-12: Duration `1`, Purpose `Siaran langsung kegiatan`.

## Test Steps

### Tombol Borrow an Asset tampil di My Asset tab Borrowed
1. Klik menu Profile pada navbar
2. Klik `My Asset`
3. Klik tab `Borrowed`
4. Verifikasi tombol `[Borrow an Asset]` tampil pada tab `Borrowed` karena aset DU-039-2 dapat dipinjam sendiri oleh Aktor

### Borrow Now dengan Duration hari langsung Borrowed tanpa Waiting for Handover
5. Klik `[Borrow an Asset]`
6. Verifikasi halaman `Borrow an Asset` tampil dengan Alert `No approval needed. Your borrow starts as soon as you tap Borrow Now.`
7. Verifikasi halaman `Borrow an Asset` memuat bagian scan TAG, tabel aset, field Note, serta tombol `[Cancel]` dan `[Borrow Now]` pada footer
8. Verifikasi pilihan `Borrow for` tidak tampil karena Aktor bukan PIC karyawan tanpa akun mana pun
9. Pindai TAG aset DU-039-2 lewat komponen scan
10. Verifikasi aset `Mesin Label Brother {runId}` masuk tabel aset dengan kolom `Duration` dan `Purpose` pada barisnya
11. Isi Duration baris `Mesin Label Brother {runId}` dengan `2`
12. Isi Purpose baris `Mesin Label Brother {runId}` dengan `Pelabelan arsip gudang`
13. Klik `[Borrow Now]`
14. Verifikasi pesan `1 asset needs a handover photo.` tampil di atas `[Borrow Now]` karena foto aset belum diambil
15. Ambil foto aset `Mesin Label Brother {runId}` dengan kamera perangkat
16. Klik `[Borrow Now]`
17. Verifikasi panel hasil `Success, 1 asset is now borrowed. Return by [Date].` tampil dengan [Date] berisi T0 + 1 hari, dari tanggal `[Borrow Now]` ditambah Duration 2 hari dikurangi 1 hari
18. Kembali ke tab `Borrowed` pada My Asset
19. Verifikasi baris aset `Mesin Label Brother {runId}` langsung berstatus `Borrowed` dengan Due date T0 + 1 hari, tanpa konfirmasi Borrower dan tanpa Aktor Borrow
20. Klik menu ⋯ pada baris aset `Mesin Label Brother {runId}`
21. Klik `Borrow Log`
22. Verifikasi Borrow Log memuat node `Borrowed via self-service by [Borrower]` dengan [Borrower] berisi `Hendra Kusuma {runId}`
23. Tutup dialog Borrow Log

### Borrow Now dengan Duration jam menetapkan Due date dari jam Borrow Now
24. Klik `[Borrow an Asset]`
25. Pindai TAG aset DU-039-4 lewat komponen scan
26. Isi Duration baris `Kamera Mirrorless Fujifilm {runId}` dengan `3`
27. Isi Purpose baris `Kamera Mirrorless Fujifilm {runId}` dengan `Dokumentasi acara kantor`
28. Ambil foto aset `Kamera Mirrorless Fujifilm {runId}` dengan kamera perangkat
29. Klik `[Borrow Now]`
30. Verifikasi panel hasil `Success, 1 asset is now borrowed. Return by [Date].` tampil dengan [Date] berisi jam `[Borrow Now]` ditambah 3 jam

### Scan aset yang tidak dapat dipinjam sendiri ditolak dan scan berikutnya tetap dapat dilakukan
31. Kembali ke tab `Borrowed` pada My Asset
32. Klik `[Borrow an Asset]`
33. Pindai TAG aset DU-039-5 lewat komponen scan
34. Verifikasi aset `Proyektor Epson EB-W06 {runId}` masuk tabel aset
35. Pindai TAG aset DU-039-3 lewat komponen scan
36. Verifikasi toast `Error, this asset can't be borrowed on your own.` tampil
37. Verifikasi aset `Genset Honda EU20 {runId}` tidak ada di tabel aset sedangkan aset `Proyektor Epson EB-W06 {runId}` tetap ada
38. Pindai TAG aset DU-039-6 lewat komponen scan
39. Verifikasi aset `Laptop Acer Aspire {runId}` masuk tabel aset sehingga scan berikutnya tetap dapat dilakukan

### Bulk Set Duration & Purpose, alternatif Add Assets untuk aset Non TAG, dan foto hanya dari kamera
40. Centang baris `Proyektor Epson EB-W06 {runId}`
41. Centang baris `Laptop Acer Aspire {runId}`
42. Klik aksi bulk `Set Duration & Purpose`
43. Isi Duration pada dialog `Set Duration & Purpose` dengan `2`
44. Isi Purpose pada dialog `Set Duration & Purpose` dengan `Rapat evaluasi`
45. Klik `[Apply to 2 assets]`
46. Verifikasi Duration `2` dan Purpose `Rapat evaluasi` terisi pada baris `Proyektor Epson EB-W06 {runId}` dan baris `Laptop Acer Aspire {runId}`
47. Klik `[+ Add Assets]`
48. Verifikasi dialog `Select Asset` menawarkan aset `Kursi Ergonomis {runId}` dengan Category `Non TAG {runId}`
49. Verifikasi aset bertag `Scanner Epson DS-530 {runId}` tidak ditawarkan pada dialog `Select Asset`
50. Pilih aset `Kursi Ergonomis {runId}` pada dialog `Select Asset`
51. Klik `[Select]`
52. Verifikasi aset `Kursi Ergonomis {runId}` masuk tabel aset
53. Verifikasi pengambilan foto per aset hanya lewat kamera perangkat: tombol ambil foto tampil pada baris `Proyektor Epson EB-W06 {runId}` dan opsi unggah berkas atau galeri tidak tersedia
54. Klik `[Cancel]` pada halaman `Borrow an Asset`

### Borrow for tampil untuk PIC dan menghitung ulang kelayakan aset yang sudah dipindai
55. Masuk sebagai `Rudi Hartono {runId}`
56. Klik menu Profile pada navbar
57. Klik `My Asset`
58. Klik tab `Borrowed`
59. Klik `[Borrow an Asset]`
60. Verifikasi pilihan `Borrow for` tampil dengan nilai awal `Myself` karena Aktor menjadi PIC karyawan tanpa akun
61. Verifikasi pilihan `Borrow for` hanya menawarkan `Myself` dan `Joko Susilo {runId}`
62. Pindai TAG aset DU-039-11 lewat komponen scan
63. Verifikasi aset `Printer Zebra ZD220 {runId}` masuk tabel aset untuk Borrower `Myself`
64. Pilih `Joko Susilo {runId}` pada `Borrow for`
65. Verifikasi kelayakan aset `Printer Zebra ZD220 {runId}` dihitung ulang untuk Borrower `Joko Susilo {runId}` sehingga aset itu tidak lagi layak dipinjam
66. Klik `[Cancel]` pada halaman `Borrow an Asset`

### Borrow Now atas nama karyawan tanpa akun membuka Confirm Receipt dan mencatat PIC
67. Klik `[Borrow an Asset]`
68. Pilih `Joko Susilo {runId}` pada `Borrow for`
69. Pindai TAG aset DU-039-8 lewat komponen scan
70. Isi Duration baris `Scanner Epson DS-530 {runId}` dengan `1`
71. Isi Purpose baris `Scanner Epson DS-530 {runId}` dengan `Inventarisasi aset cabang`
72. Ambil foto aset `Scanner Epson DS-530 {runId}` dengan kamera perangkat
73. Klik `[Borrow Now]`
74. Verifikasi dialog `Confirm Receipt` tampil dengan nama Borrower `Joko Susilo {runId}`, checkbox pernyataan `I confirm that [Borrower] is here and has received the scanned assets.`, dan tanpa daftar aset
75. Verifikasi tombol `[Confirm]` pada dialog `Confirm Receipt` atas nama Borrower `Joko Susilo {runId}` nonaktif sampai checkbox pernyataan dicentang
76. Centang checkbox pernyataan
77. Klik `[Confirm]`
78. Verifikasi panel hasil `Success, 1 asset is now borrowed. Return by [Date].` tampil dengan [Date] berisi T0, dari tanggal `[Borrow Now]` ditambah Duration 1 hari dikurangi 1 hari
79. Kembali ke tab `Borrowed` pada My Asset
80. Klik menu ⋯ pada baris aset `Scanner Epson DS-530 {runId}`
81. Klik `Borrow Log`
82. Verifikasi Borrow Log memuat node `Borrowed via self-service by [PIC] on behalf of [Borrower]` dengan [PIC] berisi `Rudi Hartono {runId}` dan [Borrower] berisi `Joko Susilo {runId}`
83. Tutup dialog Borrow Log

### Dua pemindai atas aset yang sama: Borrow Now yang kedua ditolak
84. Masuk sebagai `Hendra Kusuma {runId}`
85. Klik menu Profile pada navbar
86. Klik `My Asset`
87. Klik tab `Borrowed`
88. Klik `[Borrow an Asset]`
89. Pindai TAG aset DU-039-12 lewat komponen scan
90. Isi Duration baris `Mikrofon Shure SM58 {runId}` dengan `1`
91. Isi Purpose baris `Mikrofon Shure SM58 {runId}` dengan `Siaran langsung kegiatan`
92. Ambil foto aset `Mikrofon Shure SM58 {runId}` dengan kamera perangkat
93. Borrower lain `Wawan Setiawan {runId}` meminjam aset `Mikrofon Shure SM58 {runId}` lewat Borrow Now lebih dulu
94. Klik `[Borrow Now]`
95. Verifikasi pesan `This asset was just borrowed by someone else.` tampil
96. Verifikasi tombol `[Borrow Now]` masih tampil pada halaman `Borrow an Asset`
97. Verifikasi aset `Mikrofon Shure SM58 {runId}` tidak ada lagi di tabel aset karena barisnya dikeluarkan dari form
98. Klik `[Cancel]` pada halaman `Borrow an Asset`

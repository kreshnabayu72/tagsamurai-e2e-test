---
id: TC-FA-BORROW-UI-065-dialog-konfirmasi-handover
title: "Popup Waiting for Confirmation dan dialog Confirm Receipt: countdown, checklist aset, pernyataan, dan jendela konfirmasi"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["D-BRW-19", "D-BRW-20", "D-BRW-21", "DM-BRW-14", "DM-BRW-15", "DO-BRW-01", "DO-BRW-02", "DO-BRW-03", "DO-BRW-04", "DO-BRW-05", "DO-BRW-06", "DO-BRW-07", "DO-BRW-08", "DO-BRW-09", "DO-BRW-10", "FLD-BRW-08", "FLD-BRW-27", "FLD-BRW-28", "V-BRW-32", "V-BRW-33", "§4.3#r8", "§9.5#r11", "EB-ERR-1@handover"]
smoke: []
dependsOn: []
trace:
  "D-BRW-19": [2, 3, 4, 6, 7, 8, 9, 11, 13, 17, 18, 19, 21, 23, 25, 27, 29, 30, 31, 33, 34, 36, 37, 39, 90, 93]
  "D-BRW-20": [50, 51, 52, 53, 54, 55, 56, 60, 61, 64]
  "D-BRW-21": [66, 67, 68, 69, 70, 73]
  "DM-BRW-14": [2, 15]
  "DM-BRW-15": 66
  "DO-BRW-01": 36
  "DO-BRW-02": 36
  "DO-BRW-03": 8
  "DO-BRW-04": 48
  "DO-BRW-05": 41
  "DO-BRW-06": [41, 42]
  "DO-BRW-07": 48
  "DO-BRW-08": 48
  "DO-BRW-09": 44
  "DO-BRW-10": 45
  "FLD-BRW-08": [68, 70, 72]
  "FLD-BRW-27": [55, 56, 58, 68]
  "FLD-BRW-28": [53, 54, 60]
  "V-BRW-32": [3, 36, 60, 63]
  "V-BRW-33": [56, 58, 61, 63, 70, 72]
  "§4.3#r8": [3, 4, 8]
  "§9.5#r11": 5
  "EB-ERR-1@handover": [77, 78, 79, 81, 85, 86, 88]
anchor: []
coverage:
  web: automated
---

# Popup Waiting for Confirmation dan dialog Confirm Receipt: countdown, checklist aset, pernyataan, dan jendela konfirmasi

## Prerequisites
- Aktor: Aktor Borrow dengan cakupan Group `Finance`.
- Layar awal: Halaman Handover
- Komponen: Popup Waiting for Confirmation
- Data:
  - DU-065-1: Borrower `Budi Santoso`.
  - DU-065-2: aset di sesi Handover, Name `Laptop Dell Latitude 5420 - 8`, Due Date `10/12/2026`.
  - DU-065-3: aset di sesi Handover, Name `Printer Epson L3110 - 1`, Due Date `10/12/2026`.
  - DU-065-4: aset di sesi Handover, Name `Kamera Canon EOS 200D`, Due Date `15/12/2026`.
  - DU-065-5: aset di sesi Handover, Name `Speaker JBL PartyBox`, Due Date `15/12/2026`.
  - DU-065-6: 7 aset di sesi Handover, Name `Laptop Lenovo ThinkPad E14 - {n}` (n = 1 sampai 7), Due Date `10/12/2026`.
  - Nilai turunan: pesan aset tidak diterima untuk dua aset, `2 assets not received.`, dari [Not Received] bernilai dua (DU-065-4 dan DU-065-5).
- Kondisi:
  - K1: Date Format bernilai `DD/MM/YYYY`, popup dibuka dari `[Request Confirmation]`, Borrower DU-065-1, jendela konfirmasi 15 menit baru dimulai, daftar sesi berisi DU-065-2 dan DU-065-3 berstatus `Waiting`.
  - K2: Date Format bernilai `DD/MM/YYYY`, popup menunggu, Borrower DU-065-1, daftar sesi berisi DU-065-2 berstatus `Waiting`, DU-065-3 berstatus `Confirmed`, dan DU-065-4 berstatus `Not received`.
  - K3: popup menunggu, Borrower DU-065-1, daftar sesi berisi DU-065-2 dan DU-065-3, dan satu aset siap yang belum terscan.
  - K4: popup menunggu, Borrower DU-065-1, daftar sesi berisi DU-065-2 dan DU-065-3, dan dua aset siap yang belum terscan.
  - K5: popup menunggu, Borrower DU-065-1, daftar sesi berisi DU-065-2, sisa jendela konfirmasi 61 detik.
  - K6: popup hasil, Borrower DU-065-1 mengonfirmasi satu aset, DU-065-2, dan satu aset tidak diterima, DU-065-3.
  - K7: popup hasil, Borrower DU-065-1 mengonfirmasi dua aset, DU-065-2 dan DU-065-3, dan dua aset tidak diterima, DU-065-4 dan DU-065-5.
  - K8: popup hasil karena jendela konfirmasi habis tanpa konfirmasi dari Borrower DU-065-1.
  - K9: popup dibuka lagi lewat `Hand Over` sesudah tertutup tanpa sengaja, sesi yang sama masih berjalan dengan sisa jendela konfirmasi 8 menit, Borrower DU-065-1, daftar sesi berisi DU-065-2 berstatus `Confirmed` dan DU-065-3 berstatus `Waiting`.
  - K10: popup menunggu, Borrower DU-065-1, daftar sesi berisi DU-065-2 dan DU-065-3, konfirmasi Borrower lewat Accept masuk lebih dulu sebelum Confirm on This Device.
  - K11: dialog Confirm Receipt Handover dibuka dari `[Confirm on This Device]`, Date Format bernilai `DD/MM/YYYY`, Borrower DU-065-1, daftar sesi berisi DU-065-2, DU-065-3, dan DU-065-4.
  - K12: dialog Confirm Receipt self-service dibuka dari `[Borrow Now]` atas nama Borrower tanpa akun DU-065-1.
  - K13: dialog Confirm Receipt Handover dengan DU-065-2 dan DU-065-3, konfirmasi pertama dijawab error server, konfirmasi berikutnya berhasil.
  - K14: dialog Confirm Receipt Handover dengan DU-065-2 dan DU-065-3, konfirmasi pertama tidak mendapat respons karena koneksi putus, konfirmasi berikutnya berhasil.
  - K15: popup menunggu, Borrower DU-065-1, daftar sesi berisi seluruh DU-065-6.

## Test Steps

### Popup Waiting for Confirmation saat menunggu
1. Tampilkan Popup Waiting for Confirmation dengan kondisi K1
2. Verifikasi judul popup `Waiting for Confirmation` tampil
3. Verifikasi teks `Waiting for Budi Santoso to confirm…` tampil
4. Verifikasi countdown jendela konfirmasi tampil sebagai badge `primary`
5. Verifikasi countdown dimulai dari jendela konfirmasi 15 menit
6. Verifikasi daftar aset sesi memuat `Laptop Dell Latitude 5420 - 8` dengan `Return by 10/12/2026`
7. Verifikasi daftar aset sesi memuat `Printer Epson L3110 - 1` dengan `Return by 10/12/2026`
8. Verifikasi badge `Waiting` tampil pada baris `Laptop Dell Latitude 5420 - 8`
9. Verifikasi tombol `[Cancel Request]` dan `[Confirm on This Device]` tampil
10. Klik di luar popup
11. Verifikasi popup `Waiting for Confirmation` tetap terbuka sesudah klik di luar popup
12. Tekan `Esc`
13. Verifikasi popup `Waiting for Confirmation` tetap terbuka sesudah `Esc` ditekan
14. Klik `[Confirm on This Device]`
15. Verifikasi dialog `Confirm Receipt` tampil sesudah `[Confirm on This Device]` diklik

### Badge status per aset
16. Tampilkan Popup Waiting for Confirmation dengan kondisi K2
17. Verifikasi badge `Waiting` tampil pada baris `Laptop Dell Latitude 5420 - 8` saat aset belum dikonfirmasi
18. Verifikasi badge `Confirmed` tampil pada baris `Printer Epson L3110 - 1`
19. Verifikasi badge `Not received` tampil pada baris `Kamera Canon EOS 200D`

### Catatan aset siap yang belum terscan untuk satu aset
20. Tampilkan Popup Waiting for Confirmation dengan kondisi K3
21. Verifikasi catatan `1 asset will stay Waiting for Handover.` tampil

### Catatan aset siap yang belum terscan untuk beberapa aset
22. Tampilkan Popup Waiting for Confirmation dengan kondisi K4
23. Verifikasi catatan `2 assets will stay Waiting for Handover.` tampil

### Countdown berubah saat sisa waktu 60 detik
24. Tampilkan Popup Waiting for Confirmation dengan kondisi K5
25. Verifikasi countdown jendela konfirmasi tampil sebagai badge `primary` pada sisa jendela 61 detik
26. Waktu berlalu sampai sisa jendela konfirmasi 60 detik
27. Verifikasi countdown jendela konfirmasi tampil sebagai badge `danger` pada sisa jendela 60 detik

### Hasil konfirmasi satu aset
28. Tampilkan Popup Waiting for Confirmation dengan kondisi K6
29. Verifikasi teks `Budi Santoso confirmed 1 asset.` tampil
30. Verifikasi teks `1 asset not received.` tampil
31. Verifikasi tombol `[Done]` tampil

### Hasil konfirmasi beberapa aset
32. Tampilkan Popup Waiting for Confirmation dengan kondisi K7
33. Verifikasi teks `Budi Santoso confirmed 2 assets.` tampil
34. Verifikasi teks `2 assets not received.` tampil

### Jendela konfirmasi habis
35. Tampilkan Popup Waiting for Confirmation dengan kondisi K8
36. Verifikasi teks `Budi Santoso didn't confirm. Try again.` tampil
37. Verifikasi popup tidak menampilkan daftar aset
38. Klik `[Done]`
39. Verifikasi popup `Waiting for Confirmation` tertutup

### Popup dibuka lagi pada sesi yang sama
40. Tampilkan Popup Waiting for Confirmation dengan kondisi K9
41. Verifikasi baris `Laptop Dell Latitude 5420 - 8` menampilkan badge `Confirmed`, sehingga popup adalah sesi yang sama, bukan sesi baru
42. Verifikasi countdown menampilkan sisa jendela konfirmasi 8 menit dari sesi yang sama, bukan jendela penuh 15 menit

### Konfirmasi pertama yang masuk berlaku
43. Tampilkan Popup Waiting for Confirmation dengan kondisi K10
44. Verifikasi teks `Budi Santoso confirmed 2 assets.` tampil karena konfirmasi pertama masuk lebih dulu
45. Verifikasi tombol `[Confirm on This Device]` tidak tampil sesudah konfirmasi pertama masuk

### Cancel Request menutup popup
46. Tampilkan Popup Waiting for Confirmation dengan kondisi K1
47. Klik `[Cancel Request]`
48. Verifikasi popup `Waiting for Confirmation` tertutup sesudah `[Cancel Request]` diklik

### Dialog Confirm Receipt Handover
49. Tampilkan Popup Waiting for Confirmation dengan kondisi K11
50. Verifikasi judul dialog `Confirm Receipt` tampil
51. Verifikasi nama Borrower `Budi Santoso` tampil di dialog Confirm Receipt
52. Verifikasi teks `Uncheck any asset Budi Santoso didn't receive.` tampil
53. Verifikasi checklist aset memuat `Laptop Dell Latitude 5420 - 8` dengan `Return by 10/12/2026` dalam keadaan tercentang
54. Verifikasi checklist aset memuat `Printer Epson L3110 - 1` dan `Kamera Canon EOS 200D` dalam keadaan tercentang
55. Verifikasi checkbox `I confirm that Budi Santoso is here and has received the checked assets.` tampil dan tidak tercentang
56. Verifikasi tombol `[Confirm]` disabled sebelum checkbox pernyataan dicentang
57. Centang checkbox `I confirm that Budi Santoso is here and has received the checked assets.`
58. Verifikasi tombol `[Confirm]` aktif sesudah checkbox pernyataan dicentang
59. Hilangkan centang semua aset di checklist
60. Verifikasi teks `Check at least one asset received.` tampil
61. Verifikasi tombol `[Confirm]` disabled saat tidak ada aset yang tercentang
62. Centang aset `Laptop Dell Latitude 5420 - 8` di checklist
63. Verifikasi tombol `[Confirm]` aktif sesudah satu aset tercentang dan checkbox pernyataan tercentang
64. Verifikasi tombol `[Cancel]` dan `[Confirm]` tampil di dialog Confirm Receipt

### Dialog Confirm Receipt self-service
65. Tampilkan Popup Waiting for Confirmation dengan kondisi K12
66. Verifikasi judul dialog `Confirm Receipt` tampil dari `[Borrow Now]`
67. Verifikasi nama Borrower `Budi Santoso` tampil di dialog Confirm Receipt
68. Verifikasi checkbox `I confirm that Budi Santoso is here and has received the scanned assets.` tampil dan tidak tercentang
69. Verifikasi dialog Confirm Receipt tidak menampilkan daftar aset
70. Verifikasi tombol `[Confirm]` disabled sebelum checkbox dicentang
71. Centang checkbox `I confirm that Budi Santoso is here and has received the scanned assets.`
72. Verifikasi tombol `[Confirm]` aktif sesudah checkbox dicentang
73. Verifikasi tombol `[Cancel]` dan `[Confirm]` tampil di dialog Confirm Receipt self-service

### Confirm Receipt gagal karena error server lalu diulang
74. Tampilkan Popup Waiting for Confirmation dengan kondisi K13
75. Centang checkbox `I confirm that Budi Santoso is here and has received the checked assets.`
76. Klik `[Confirm]`
77. Verifikasi toast `Error, failed to hand over assets.` tampil
78. Verifikasi toast error Handover tidak menampilkan tombol aksi `[Try Again]`
79. Verifikasi dialog Confirm Receipt tetap terbuka, checkbox pernyataan tetap tercentang, dan tombol `[Confirm]` aktif lagi
80. Klik `[Confirm]`
81. Verifikasi toast `Success, 2 assets have been handed over.` tampil sesudah konfirmasi diulang

### Confirm Receipt gagal karena koneksi putus lalu diulang
82. Tampilkan Popup Waiting for Confirmation dengan kondisi K14
83. Centang checkbox `I confirm that Budi Santoso is here and has received the checked assets.`
84. Klik `[Confirm]`
85. Verifikasi toast `Connection problem. Please try again.` tampil setelah konfirmasi tidak mendapat respons
86. Verifikasi dialog Confirm Receipt tetap terbuka dan tombol `[Confirm]` aktif lagi setelah gangguan koneksi
87. Klik `[Confirm]`
88. Verifikasi toast `Success, 2 assets have been handed over.` tampil sesudah koneksi pulih

### Daftar aset sesi yang panjang dapat di-scroll
89. Tampilkan Popup Waiting for Confirmation dengan kondisi K15
90. Verifikasi daftar aset sesi memuat 7 baris `Laptop Lenovo ThinkPad E14` dengan tinggi daftar maksimal 5 baris, sehingga baris lainnya terjangkau lewat scroll

### Done pada hasil konfirmasi menutup popup
91. Tampilkan Popup Waiting for Confirmation dengan kondisi K6
92. Klik `[Done]`
93. Verifikasi popup `Waiting for Confirmation` tertutup sesudah `[Done]`

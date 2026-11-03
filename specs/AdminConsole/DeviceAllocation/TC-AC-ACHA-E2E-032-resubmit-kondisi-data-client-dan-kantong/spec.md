---
id: TC-AC-ACHA-E2E-032-resubmit-kondisi-data-client-dan-kantong
title: "Resubmit Diblokir Kondisi Data: Validasi Quantity, Saldo Kurang, Client Tidak Valid, dan Kantong Sumber Tidak Tersedia"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHA-243
  - TC-AC-ACHA-244
  - TC-AC-ACHA-245
  - TC-AC-ACHA-246
  - TC-AC-ACHA-476
  - TC-AC-ACHA-477
  - TC-AC-ACHA-486
coverage:
  web: automated
---

# Resubmit Diblokir Kondisi Data: Validasi Quantity, Saldo Kurang, Client Tidak Valid, dan Kantong Sumber Tidak Tersedia

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Group Member Distributor toggle ON MB_ON (Pre-setup #32) `memberOnDistributor_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_MB_ON_PASSWORD`. Akun ganti di tengah spec: Group Member Partner CV Mitra Solusi toggle ON MB_P1 (Pre-setup #44) `memberOnPartner1_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_MB_P1_PASSWORD`. Login MB_ON di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Nama env baru didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Data Pre-setup yang dibaca: Distributor PT Global Distribusi (#3), Partner CV Mitra Solusi (#4), Client PT Sejahtera Logistik (#7), PT Retail Makmur (#8), PT Nusa Distribusi (#6), harga PT ABC (#14), kantong PT Global Distribusi saldo $20,000.00 (#16).
- Data seed milik spec (seeding API di hook `before`, disediakan tim FE/BE; Allocation ID ditangkap saat runtime):
  - Transaksi Canceled manual milik MB_ON dengan atribut Pre-setup #52 (BLE Gateway, Quantity 50, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch lama`, Total Cost $100.00). Semua Submit pada spec ini ditolak, sehingga transaksi ini tetap Canceled dan dipakai berurutan oleh semua blok MB_ON.
  - Transaksi Canceled manual milik MB_P1 dengan atribut Pre-setup #69 (NFC, Quantity 10, Client PT Retail Makmur, Pay From `PT Global Distribusi (Distributor)`, Total Cost $15.00) untuk TC-476.
  - Nilai literal `Batch lama` diasersi oleh TC sehingga tidak bersuffix (pengecualian S-12 nama literal, Lampiran A butir A-11).
- Kemampuan teknis (disediakan tim FE/BE, kontrak fixture tidak tertulis di TC): fixture API untuk (a) menyetel saldo kantong PT Global Distribusi ($99.99, $150.00, lalu $20,000.00) dan menahan Reserve dari sesi lain ($60.00), (b) mengubah status Client PT Sejahtera Logistik menjadi Suspended atau Archived dan memulihkannya ke Active, (c) memindahkan binaan Client PT Sejahtera Logistik ke PT Nusa Distribusi dan memulihkannya, (d) membuat kantong sumber PT Global Distribusi tidak tersedia bagi CV Mitra Solusi dan memulihkannya; pembacaan Reserved kantong dan total baris List.
- State global yang diubah dan pemulihannya: saldo dan Reserve kantong PT Global Distribusi, status Client PT Sejahtera Logistik, binaan Client PT Sejahtera Logistik, kantong sumber CV Mitra Solusi; dipulihkan lewat langkah penghubung sesudah tiap blok dan di hook `after`. Suite berjalan serial (`parallel: false`).
- Hook suite (`suite.md`): flag Guided Tooltip halaman Device Allocation true untuk akun aktor, sesi API aktor, fixture API Pre-setup #20.

## Test Steps

### Validasi Quantity pada form Resubmit (TC-AC-ACHA-245)

1. Catat total baris List (B)
2. Ketik Search Allocation ID transaksi Canceled seed milik MB_ON (Pre-setup #52), tekan Enter
3. Klik `Resubmit` pada transaksi Canceled milik MB_ON
4. Isi Quantity `0`
5. Verifikasi pesan "Quantity must be a positive whole number"
6. Verifikasi `[Submit]` disabled
7. Isi Quantity `1000001`
8. Verifikasi pesan "Quantity must not exceed 1,000,000"
9. Verifikasi `[Submit]` disabled
10. Isi Quantity `1000000000000000` (16 digit)
11. Verifikasi pesan "Max. 15 characters"
12. Verifikasi `[Submit]` disabled
13. Klik `[×]`
14. Verifikasi dialog Unsaved Changes: judul "Unsaved Changes", body "You have unsaved changes. Are you sure you want to leave?", tombol `[Cancel]` dan `[Leave]`
15. Klik `[Leave]`
16. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
17. Verifikasi List menampilkan sedikitnya satu baris
18. Verifikasi total baris sama dengan B (tidak ada transaksi tercipta)

### Saldo kurang pada form Resubmit (TC-AC-ACHA-246)

19. Setel saldo kantong PT Global Distribusi $99.99 lewat fixture API
20. Ketik Search Allocation ID transaksi Canceled seed milik MB_ON (Pre-setup #52), tekan Enter
21. Klik `Resubmit` pada transaksi Canceled milik MB_ON
22. Verifikasi pesan danger "Insufficient balance in your pocket. Available: $99.99. Required: $100.00."
23. Verifikasi `[Submit]` disabled
24. Klik `[×]`
25. Setel saldo kantong PT Global Distribusi kembali $20,000.00 lewat fixture API

### Submit ditolak server karena saldo berkurang setelah cek FE (TC-AC-ACHA-486)

26. Setel saldo kantong PT Global Distribusi $150.00 lewat fixture API
27. Klik `Resubmit` pada transaksi Canceled milik MB_ON
28. Verifikasi Preview biaya $100.00 (50 × $2.00)
29. Verifikasi tidak ada pesan saldo kurang
30. Sesi lain menahan Reserve $60.00 pada kantong PT Global Distribusi lewat fixture API
31. Klik `[Submit]`
32. Verifikasi pesan inline "Insufficient balance in your pocket. Available: $90.00. Required: $100.00." tampil dengan Available terbaru
33. Verifikasi `[Submit]` disabled
34. Verifikasi form Resubmit tetap terbuka dengan input dipertahankan: Category `BLE Gateway`, Client `PT Sejahtera Logistik`, Quantity `50`
35. Verifikasi tidak ada toast dan tidak ada dialog
36. Klik `[×]`
37. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
38. Verifikasi List menampilkan sedikitnya satu baris
39. Verifikasi total baris sama dengan B (tidak ada transaksi baru)
40. Verifikasi Reserved kantong PT Global Distribusi $60.00 (hanya dari sesi lain, Reserve tidak berubah)
41. Verifikasi transaksi Canceled lama tidak berubah: Status `Canceled`, Quantity `50`
42. Lepas Reserve $60.00 dan setel saldo kantong PT Global Distribusi kembali $20,000.00 lewat fixture API

### Client lama Suspended (TC-AC-ACHA-243)

43. Ubah status Client PT Sejahtera Logistik menjadi Suspended lewat fixture API
44. Ketik Search Allocation ID transaksi Canceled seed milik MB_ON (Pre-setup #52), tekan Enter
45. Klik `Resubmit` pada transaksi Canceled milik MB_ON
46. Verifikasi field Client kosong
47. Verifikasi Category `BLE Gateway`, Quantity `50`, dan Notes `Batch lama` tetap terisi
48. Klik `[Submit]` tanpa memilih Client
49. Verifikasi pesan "Client recipient must not be empty"
50. Klik `[×]`
51. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
52. Verifikasi List menampilkan sedikitnya satu baris
53. Verifikasi total baris sama dengan B (tidak ada transaksi baru)
54. Pulihkan status Client PT Sejahtera Logistik menjadi Active lewat fixture API

### Client lama Archived (TC-AC-ACHA-244)

55. Ubah status Client PT Sejahtera Logistik menjadi Archived lewat fixture API
56. Ketik Search Allocation ID transaksi Canceled seed milik MB_ON (Pre-setup #52), tekan Enter
57. Klik `Resubmit` pada transaksi Canceled milik MB_ON
58. Verifikasi field Client kosong
59. Verifikasi Category `BLE Gateway`, Quantity `50`, dan Notes `Batch lama` tetap terisi
60. Klik `[Submit]` tanpa memilih Client
61. Verifikasi pesan "Client recipient must not be empty"
62. Klik `[×]`
63. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
64. Verifikasi List menampilkan sedikitnya satu baris
65. Verifikasi total baris sama dengan B (tidak ada transaksi baru)
66. Pulihkan status Client PT Sejahtera Logistik menjadi Active lewat fixture API

### Client lama di luar scope WRITE (TC-AC-ACHA-477)

67. Pindahkan binaan Client PT Sejahtera Logistik dari PT Global Distribusi ke PT Nusa Distribusi lewat fixture API
68. Ketik Search Allocation ID transaksi Canceled seed milik MB_ON (Pre-setup #52), tekan Enter
69. Klik `Resubmit` pada transaksi Canceled milik MB_ON
70. Verifikasi field Client kosong
71. Verifikasi Category `BLE Gateway`, Quantity `50`, dan Notes `Batch lama` tetap terisi
72. Klik `[Submit]` tanpa memilih Client
73. Verifikasi pesan "Client recipient must not be empty"
74. Klik `[×]`
75. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
76. Verifikasi List menampilkan sedikitnya satu baris
77. Verifikasi total baris sama dengan B (tidak ada transaksi baru)
78. Pulihkan binaan Client PT Sejahtera Logistik ke PT Global Distribusi lewat fixture API

### Kantong sumber tidak tersedia (TC-AC-ACHA-476)

79. Ganti akun ke MB_P1: Logout, login dengan `Spectra.env.AC_DA_MB_P1_PASSWORD`, buka Allocation > Device Allocation, lalu catat total baris List (B2) dan Reserved kantong PT Global Distribusi lewat fixture baca (R2)
80. Jadikan kantong sumber `PT Global Distribusi (Distributor)` tidak tersedia bagi CV Mitra Solusi dan tidak ada kantong sumber lain lewat fixture API
81. Ketik Search Allocation ID transaksi Canceled seed milik MB_P1 (Pre-setup #69), tekan Enter
82. Klik `Resubmit` pada transaksi Canceled milik MB_P1
83. Verifikasi field Pay From tampil disabled tanpa nilai
84. Verifikasi Category `NFC`, Client `PT Retail Makmur`, dan Quantity `10` tetap terisi
85. Klik `[Submit]` tanpa mengubah isian
86. Verifikasi toast error "Error, failed to submit device allocation."
87. Verifikasi form tetap terbuka dengan input dipertahankan
88. Klik `[×]`
89. Klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)
90. Verifikasi List menampilkan sedikitnya satu baris
91. Verifikasi tidak ada transaksi baru milik MB_P1 (total baris sama dengan B2)
92. Baca Reserved kantong PT Global Distribusi lewat fixture baca
93. Verifikasi Reserved kantong PT Global Distribusi sama dengan R2 (Submit ditolak tanpa Reserve)
94. Pulihkan kantong sumber `PT Global Distribusi (Distributor)` bagi CV Mitra Solusi lewat fixture API

## Notes

- Langkah penghubung (S-03, R-16): Search Allocation ID dan pembersihan Search, mencatat total baris B, B2 dan Reserved R2, menyetel dan memulihkan state lewat fixture, menutup form dengan `[×]`, dan ganti akun MB_P1 tidak punya `Verifikasi`. Verifikasi "List menampilkan sedikitnya satu baris" memberi anchor positif untuk asersi "tidak ada transaksi baru" (bagian 8b butir 2).
- Penutupan form: form dirty (TC-245, Quantity diubah) ditutup deterministik dengan `[×]`, `Verifikasi` dialog Unsaved Changes, `[Leave]` (S-08). Form pada blok lain tidak dirty (nilai sama dengan pre-fill; Client dikosongkan otomatis oleh sistem adalah bagian pre-fill), sehingga ditutup dengan `[×]` tanpa dialog (TC-247). Status dirty pada kondisi tersebut tidak dinyatakan TC; spec mengikuti aturan "sama dengan pre-fill".
- Urutan TC-486 mengamati form sebelum List: pesan inline dan state form hanya teramati selagi form terbuka, baru sesudah itu form ditutup dan List diperiksa (bagian 8b butir 5). Seluruh blok TC-243, 244, 477 memakai satu transaksi Canceled karena tiap Submit ditolak; blok TC-476 memakai transaksi MB_P1 dengan ganti akun eksplisit.
- Alasan di atas 35 langkah: semua blok satu topik (Resubmit ditolak karena kondisi data, prinsip 12), tidak ada yang menciptakan data, tiap blok berdiri sendiri dan memulihkan state kondisi datanya; ganti akun hanya satu kali dan bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal.
- Baris target (R-16): transaksi Canceled seed milik MB_ON dan MB_P1 ditemukan lewat Search Allocation ID yang ditangkap saat seeding sebagai langkah penghubung tanpa `Verifikasi` sebelum `Resubmit`, dan Search dikosongkan (klik `(←)` pada kotak Search, lalu muat ulang halaman (F5)) sebelum asersi total baris dan ditulis ulang ("Ketik Search") sebelum `Resubmit` berikutnya; langkah Search dan pembersihan Search tidak punya `Verifikasi`.
- Temuan untuk QA:
  - TC-243, 244, 477: urutan di Expected "Submit menampilkan pesan Client recipient must not be empty" tidak menyatakan apakah form dirty sehingga penutupan tanpa dialog adalah asumsi spec (lihat Notes penutupan form).
  - TC-476 Expected b: "Server menolak Submit tanpa membuat transaksi dan tanpa Reserve" tidak punya langkah observasi di TC; spec mengasersi tidak ada transaksi baru pada List dan Reserved kantong PT Global Distribusi sama dengan baseline R2 yang dibaca lewat fixture baca.
  - TC-476: Langkah 2 TC meminta klik `[Submit]` pada form dengan Pay From kosong; TC tidak menyatakan state tombol `[Submit]` sebelum diklik, sehingga spec tidak mengasersinya.
  - TC-486 Expected c: "Tidak ada toast dan tidak ada dialog" dibaca spec sebagai absence selama form terbuka (setelah klik `[Submit]`).
  - Kontrak fixture Pre-setup #20 (saldo, Reserve dari sesi lain, status Client, binaan Client, kantong sumber) tidak ada di TC, PRD, atau LLD; ditulis "disediakan tim FE/BE" (S-13).

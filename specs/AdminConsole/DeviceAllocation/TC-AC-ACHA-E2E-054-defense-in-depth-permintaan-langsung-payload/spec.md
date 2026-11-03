---
id: TC-AC-ACHA-E2E-054-defense-in-depth-permintaan-langsung-payload
title: "Defense-in-Depth: Permintaan Langsung dengan Payload atau Kondisi Data Tidak Valid, Replay Token, dan Markup pada Notes"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHA-153
  - TC-AC-ACHA-154
  - TC-AC-ACHA-254
  - TC-AC-ACHA-422
  - TC-AC-ACHA-423
  - TC-AC-ACHA-424
  - TC-AC-ACHA-425
  - TC-AC-ACHA-426
  - TC-AC-ACHA-427
  - TC-AC-ACHA-435
  - TC-AC-ACHA-436
  - TC-AC-ACHA-437
  - TC-AC-ACHA-438
  - TC-AC-ACHA-439
coverage:
  web: automated
---

# Defense-in-Depth: Permintaan Langsung dengan Payload atau Kondisi Data Tidak Valid, Replay Token, dan Markup pada Notes

## Prerequisites

- Mode: FE+BE (permintaan langsung lewat klien HTTP dan sesi API aktor; intercept parsial di atas backend nyata untuk replay token).
- Akun (Pre-setup, email lengkap `<alias>_automated_qaTeam1@qwertysystem.net`; password lewat env var, bukan di spec atau fixture):

| Alias | Pre-setup | Nama pengguna | Dipakai di | Env var password |
|---|---|---|---|---|
| `totalControlDistributor` | #27 | Hendra Wibowo (aktor hook `before`) | TC-AC-ACHA-422 sampai 427, 437, 438, 153, 435 | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| `memberOnDistributor` | #32 | Budi Santoso (MB_ON) | TC-AC-ACHA-436, 439, 154, 254 | `Spectra.env.AC_DA_MB_ON_PASSWORD` |

- Login akun pertama (Hendra Wibowo) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite serta memulihkan saldo kantong dan harga produk BLE Gateway.
- Hook suite (dinyatakan di `suite.md`): flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, sesi API aktor, fixture API disediakan tim FE/BE, pemulihan preferensi Setup Column.
- K-1 (konvensi bagian 2): TC kelas a dengan Expected respons API tetap masuk spec FE+BE walau tumpang tindih dengan `tc-device-allocation-backend.md` (tidak ada untuk modul ini).
- Kemampuan teknis: klien HTTP lewat sesi API aktor untuk permintaan langsung ke server (Create, Edit, Cancel, Resubmit) dengan payload yang tidak dapat dibentuk dari UI; asersi permintaan langsung hanya respons server (status dan pesan) dan state data lewat fixture baca (bagian 8b butir 1); `Spectra.intercept()` untuk meneruskan permintaan Submit ke server lalu membuang responsnya (TC-AC-ACHA-153, 154, 254), dilepas segera sesudah pemicu; deteksi dialog `alert` browser (TC-AC-ACHA-435); unduhan berkas CSV ke folder uji yang dikosongkan sebelum unduhan dan pembacaan isinya (TC-AC-ACHA-435 b, langkah 76 dan 77), disediakan tim FE; fixture baca (disediakan tim FE/BE) untuk jumlah transaksi entitas pengirim, status, Quantity, saldo, dan Reserved kantong PT Global Distribusi; fixture yang disediakan tim FE/BE untuk menyetel saldo kantong, menghapus dan memulihkan harga produk, dan membuat data seeding.
- Data Pre-setup: #7 Client PT Sejahtera Logistik, #10 Client PT Manufaktur Unggul (di luar scope WRITE PT Global Distribusi), #12 Client PT Agro Lestari (Suspended), #13 Client Toko Lama Abadi (Archived), #14 harga produk, #16 kantong PT Global Distribusi saldo $20,000.00 (Reserved awal $0.00, dipulihkan fixture di hook `before`), #66 Subcategory `RFID Premium` di bawah node RFID.
- Data seeding milik spec (fixture API tim FE/BE; salinan milik spec dari Pre-setup #49, #52, #54, #55): untuk TC-AC-ACHA-436 tiga transaksi milik MB_ON (satu Completed, satu Rejected, satu Canceled); untuk TC-AC-ACHA-439 tiga transaksi milik MB_ON (satu Waiting for Approval, satu Completed, satu Rejected); untuk TC-AC-ACHA-254 satu transaksi Canceled milik MB_ON (BLE Gateway, Quantity 50, Pay From `PT ABC (Principal)`, Total Cost $100.00); transaksi TC-AC-ACHA-153, 154, 435 dibuat spec lewat UI.
- Baseline (S-12): sebelum tiap blok TC permintaan langsung, dicatat lewat fixture baca jumlah transaksi entitas pengirim, saldo, dan Reserved kantong PT Global Distribusi; asersi "tidak ada transaksi baru, saldo dan Reserve tidak berubah" membandingkan dengan catatan itu.
- State global: saldo kantong dan harga BLE Gateway diubah di TC-AC-ACHA-437 dan 438 dan dipulihkan sebagai langkah penghubung serta di hook `after`. Efek pada Pre-setup bersama (S-06): Last Updated kantong PT Global Distribusi dan harga BLE Gateway ikut berubah dan audit trail wallet/harga bertambah permanen walau nilainya dipulihkan; transaksi yang dibuat spec tidak dapat dihapus lewat UI. Suite berjalan serial (`parallel: false`).
- Klausa "tidak ada entri log baru" pada TC-AC-ACHA-422 sampai 427, 436 sampai 439 dijalankan di spec 049 (`absence-pencatatan-log-aksi-ditolak`); spec ini mengasersi status respons dan state data.

## Test Steps

### Permintaan langsung payload tidak valid

1. Catat jumlah transaksi entitas pengirim PT Global Distribusi, saldo, dan Reserved kantong PT Global Distribusi lewat fixture baca sebagai baseline

### TC-AC-ACHA-422: Type wajib untuk RFID dan Handheld Reader pada permintaan langsung

2. Kirim permintaan Create langsung (sesi API `Hendra Wibowo`) dengan Category `RFID` tanpa Type
3. Kirim permintaan Create langsung dengan Category `Handheld Reader` tanpa Type
4. Verifikasi kedua permintaan ditolak server dengan pesan "Type must not be empty"
5. Baca jumlah transaksi, saldo, dan Reserved kantong PT Global Distribusi lewat fixture baca
6. Verifikasi tidak ada transaksi baru dibanding baseline langkah 1
7. Verifikasi saldo kantong serta Reserve tidak berubah dibanding baseline langkah 1

### TC-AC-ACHA-423: Quantity tidak valid pada permintaan langsung ditolak server

8. Kirim permintaan Create langsung dengan Category `BLE`, Client `PT Sejahtera Logistik`, dan Quantity `-5`
9. Kirim permintaan Create langsung dengan Quantity `2.5`
10. Kirim permintaan Create langsung dengan Quantity `0`
11. Kirim permintaan Create langsung dengan Quantity `1000001`
12. Verifikasi tiga permintaan pertama ditolak server dengan pesan "Quantity must be a positive whole number"
13. Verifikasi permintaan Quantity `1000001` ditolak dengan pesan "Quantity must not exceed 1,000,000"
14. Baca jumlah transaksi, saldo, dan Reserved kantong PT Global Distribusi lewat fixture baca
15. Verifikasi tidak ada transaksi baru dibanding baseline langkah 1
16. Verifikasi saldo kantong serta Reserve tidak berubah dibanding baseline langkah 1

### TC-AC-ACHA-424: Client Suspended pada permintaan langsung ditolak

17. Kirim permintaan Create langsung dengan Client `PT Agro Lestari` (Category `BLE`, Quantity `5`)
18. Verifikasi server menolak dengan HTTP 403 Forbidden
19. Baca jumlah transaksi, saldo, dan Reserved kantong PT Global Distribusi lewat fixture baca
20. Verifikasi tidak ada transaksi baru dibanding baseline langkah 1
21. Verifikasi saldo kantong serta Reserve tidak berubah dibanding baseline langkah 1

### TC-AC-ACHA-425: Client Archived pada permintaan langsung ditolak

22. Kirim permintaan Create langsung dengan Client `Toko Lama Abadi` (Category `BLE`, Quantity `5`)
23. Verifikasi server menolak dengan HTTP 403 Forbidden
24. Baca jumlah transaksi, saldo, dan Reserved kantong PT Global Distribusi lewat fixture baca
25. Verifikasi tidak ada transaksi baru dibanding baseline langkah 1
26. Verifikasi saldo kantong serta Reserve tidak berubah dibanding baseline langkah 1

### TC-AC-ACHA-426: Client di luar scope WRITE pada permintaan langsung ditolak

27. Kirim permintaan Create langsung dengan Client `PT Manufaktur Unggul` (Category `BLE`, Quantity `5`)
28. Verifikasi server menolak permintaan karena Client bukan binaan langsung pengirim
29. Baca jumlah transaksi, saldo, dan Reserved kantong PT Global Distribusi lewat fixture baca
30. Verifikasi tidak ada transaksi baru dibanding baseline langkah 1
31. Verifikasi saldo kantong serta Reserve tidak berubah dibanding baseline langkah 1

### TC-AC-ACHA-427: Category yang bukan node first-level pada permintaan langsung ditolak

32. Kirim permintaan Create langsung dengan Category `TAG` (root grup)
33. Kirim permintaan Create langsung dengan Category `Hardware` (root grup)
34. Kirim permintaan Create langsung dengan Category `RFID Premium` (subcategory level 2 buatan user)
35. Verifikasi ketiga permintaan ditolak server karena Category bukan salah satu dari tujuh node first-level
36. Baca jumlah transaksi, saldo, dan Reserved kantong PT Global Distribusi lewat fixture baca
37. Verifikasi tidak ada transaksi baru dibanding baseline langkah 1
38. Verifikasi saldo kantong serta Reserve tidak berubah dibanding baseline langkah 1

### TC-AC-ACHA-437: Saldo kantong tidak cukup pada permintaan langsung ditolak server

39. Setel kantong PT Global Distribusi ke saldo $99.99 dan harga BLE Gateway ke $2.00 lewat fixture (disediakan tim FE/BE)
40. Kirim permintaan Create langsung dengan Category `BLE Gateway`, Client `PT Sejahtera Logistik`, dan Quantity `50` (Total Cost $100.00, kurang $0.01 dari saldo)
41. Verifikasi server menolak permintaan karena saldo kantong tidak mencukupi
42. Baca jumlah transaksi, saldo, dan Reserved kantong PT Global Distribusi lewat fixture baca
43. Verifikasi tidak ada transaksi baru dibanding baseline langkah 1
44. Verifikasi saldo kantong tetap $99.99
45. Verifikasi Reserve tidak berubah dibanding baseline langkah 1
46. Pulihkan saldo kantong PT Global Distribusi ke $20,000.00 dan harga BLE Gateway ke nilai Pre-setup #14 lewat fixture (disediakan tim FE/BE)

### TC-AC-ACHA-438: Harga produk belum dikonfigurasi pada permintaan langsung ditolak

47. Hapus harga BLE Gateway pada Wallet > Product Price PT ABC lewat fixture (disediakan tim FE/BE)
48. Kirim permintaan Create langsung dengan Category `BLE Gateway`, Client `PT Sejahtera Logistik`, dan Quantity `5`
49. Verifikasi server menolak permintaan dengan pesan "Price not set for this item. Please configure product pricing first."
50. Baca jumlah transaksi, saldo, dan Reserved kantong PT Global Distribusi lewat fixture baca
51. Verifikasi tidak ada transaksi baru dibanding baseline langkah 1
52. Verifikasi saldo kantong serta Reserve tidak berubah dibanding baseline langkah 1
53. Pulihkan harga BLE Gateway ke nilai Pre-setup #14 lewat fixture (disediakan tim FE/BE)

### TC-AC-ACHA-153: Kirim ulang dengan token yang sama jalur langsung tidak menggandakan transaksi (sesi UI Hendra Wibowo)

54. Buka Allocation > Device Allocation, lalu catat jumlah transaksi entitas pengirim dan saldo kantong PT Global Distribusi lewat fixture baca sebagai baseline TC-AC-ACHA-153
55. Klik `[+ Allocation]`
56. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, dan isi Quantity `5`
57. Atur intercept agar permintaan Submit diteruskan ke server tetapi responsnya dibuang
58. Klik `[Submit]`
59. Lepas intercept respons Submit
60. Klik `[Submit]` sekali lagi pada form yang sama
61. Verifikasi toast "Success, device allocation has been created."
62. Baca jumlah transaksi dan saldo kantong PT Global Distribusi lewat fixture baca
63. Verifikasi hanya satu transaksi baru dengan Quantity 5 dibanding baseline langkah 54
64. Verifikasi saldo kantong PT Global Distribusi berkurang $10.00 satu kali dibanding baseline langkah 54

### TC-AC-ACHA-435: Notes dengan markup diperlakukan sebagai teks pada seluruh surface

65. Pasang pendeteksi dialog `alert` browser
66. Klik `[+ Allocation]`, pilih Category `TAG - BLE`, Client `PT Sejahtera Logistik`, isi Quantity `5` dan Notes `<script>alert(1)</script><img src=x onerror=alert(2)>`, lalu klik `[Submit]` jalur langsung dan catat Allocation ID transaksi itu
67. Tampilkan kolom Notes lewat Setup Column dan klik `[Save]`
68. Verifikasi Notes tampil sebagai teks apa adanya `<script>alert(1)</script><img src=x onerror=alert(2)>` pada sel kolom Notes
69. Arahkan kursor ke sel Notes
70. Verifikasi tooltip menampilkan teks Notes apa adanya
71. Buka menu row action `⋯` transaksi itu dan klik `Allocation Log`
72. Verifikasi baris `Notes` di Allocation Log menampilkan teks apa adanya
73. Verifikasi tidak ada dialog `alert` yang terdeteksi
74. Verifikasi tidak ada skrip yang dieksekusi
75. Tutup modal Allocation Log dengan `[×]`
76. Klik Download lalu `Download as CSV`, dan buka berkas
77. Verifikasi berkas CSV memuat teks Notes yang sama sebagai nilai sel biasa

### Ganti akun ke Budi Santoso (MB_ON)

78. Logout lalu login sebagai Group Member Distributor `memberOnDistributor` (Pre-setup #32), lalu buka Allocation > Device Allocation

### TC-AC-ACHA-436: Edit dan Cancel pada status akhir via permintaan langsung ditolak

79. Catat status, Quantity, dan Reserved tiga transaksi `status akhir` (Completed, Rejected, Canceled) lewat fixture baca sebagai baseline
80. Kirim permintaan Edit langsung (Quantity `120`, sesi API `Budi Santoso`) untuk masing-masing dari ketiga transaksi
81. Kirim permintaan Cancel langsung untuk transaksi Completed dan transaksi Rejected
82. Verifikasi seluruh permintaan ditolak karena status transaksi sudah berubah (konflik status)
83. Baca status, Quantity, dan Reserved ketiga transaksi lewat fixture baca
84. Verifikasi status dan Quantity tiga transaksi tidak berubah dibanding baseline langkah 79
85. Verifikasi Reserve tiga transaksi tidak berubah dibanding baseline langkah 79

### TC-AC-ACHA-439: Resubmit pada status selain Canceled via permintaan langsung ditolak

86. Catat jumlah transaksi milik MB_ON dan saldo kantong PT Global Distribusi lewat fixture baca sebagai baseline
87. Kirim permintaan Resubmit langsung (sesi API `Budi Santoso`) untuk masing-masing transaksi Waiting for Approval, Completed, dan Rejected
88. Verifikasi ketiga permintaan ditolak karena Resubmit hanya berlaku untuk status `Canceled` (Rejected tidak termasuk, sesuai `ACHA-LOGIC-03c`)
89. Baca jumlah transaksi dan saldo kantong lewat fixture baca
90. Verifikasi tidak ada transaksi baru dibanding baseline langkah 86
91. Verifikasi saldo tidak berubah dibanding baseline langkah 86

### TC-AC-ACHA-154: Kirim ulang dengan token yang sama jalur persetujuan tidak menggandakan Reserve

92. Catat jumlah transaksi Waiting for Approval milik MB_ON dan Reserved kantong PT Global Distribusi lewat fixture baca sebagai baseline TC-AC-ACHA-154
93. Klik `[+ Allocation]`
94. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, dan isi Quantity `5`
95. Atur intercept agar permintaan Submit diteruskan ke server tetapi responsnya dibuang
96. Klik `[Submit]`
97. Lepas intercept respons Submit
98. Klik `[Submit]` sekali lagi pada form yang sama
99. Verifikasi toast sukses "Success, device allocation has been submitted for approval."
100. Baca jumlah transaksi Waiting for Approval dan Reserved kantong PT Global Distribusi lewat fixture baca
101. Verifikasi hanya satu transaksi Waiting for Approval baru dibanding baseline langkah 92
102. Verifikasi Reserved bertambah $10.00 satu kali dibanding baseline langkah 92

### TC-AC-ACHA-254: Kirim ulang Resubmit dengan token yang sama tidak menggandakan transaksi

103. Catat jumlah transaksi milik MB_ON dan Reserved kantong PT Global Distribusi lewat fixture baca sebagai baseline TC-AC-ACHA-254
104. Klik `Resubmit` pada transaksi Canceled milik MB_ON (salinan untuk blok ini)
105. Atur intercept agar permintaan Submit diteruskan ke server tetapi responsnya dibuang
106. Klik `[Submit]`
107. Lepas intercept respons Submit
108. Klik `[Submit]` sekali lagi
109. Verifikasi toast sukses "Success, device allocation has been resubmitted."
110. Baca jumlah transaksi dan Reserved kantong PT Global Distribusi lewat fixture baca
111. Verifikasi hanya satu transaksi baru yang dibuat dibanding baseline langkah 103
112. Verifikasi Reserved bertambah satu kali sebesar Total Cost transaksi ($100.00) dibanding baseline langkah 103

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (Section 3a-5 untuk TC-AC-ACHA-153 dan 154; Section 3d untuk TC-AC-ACHA-254; Section 8 untuk TC-AC-ACHA-422 sampai 427 dan 435 sampai 439). Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC kelas a dengan Expected respons API (TC-AC-ACHA-422 sampai 427, 436 sampai 439) tetap masuk spec FE+BE walau tumpang tindih dengan dokumen TC backend (tidak ada untuk modul ini); BE mencatatnya pada tingkat endpoint.
- Pembagian TC lintas spec: klausa "tidak ada entri log baru" pada TC-AC-ACHA-422 sampai 427, 436 sampai 439 dijalankan di spec 049 (`absence-pencatatan-log-aksi-ditolak`) dengan permintaan nyata dan baseline sendiri (S-05, bagian 8b butir 1); spec ini mengasersi status respons dan state data (jumlah transaksi, saldo, Reserve, status, Quantity). TC-AC-ACHA-429 sampai 434, 440, dan 489 ada di spec 055 (`defense-in-depth-permintaan-langsung-otorisasi`).
- Penyimpangan urutan: TC dikelompokkan per aktor (Hendra Wibowo, lalu Budi Santoso) dan TC-AC-ACHA-153 serta 435 (aksi yang membuat transaksi lewat UI) ditaruh sesudah semua permintaan langsung supaya baseline blok permintaan langsung tidak terganggu (S-10).
- Baris target (R-16): transaksi seed milik spec pada langkah 104 (Resubmit) dan transaksi hasil Submit UI (langkah 66, Allocation ID dicatat pada langkah itu) ditemukan lewat Search Allocation ID yang dicatat saat seeding sebagai langkah penghubung tanpa `Verifikasi`; langkah ini tidak diberi nomor sendiri.
- Replay token (TC-AC-ACHA-153, 154, 254) adalah objek uji kelas a; pemakaian UI dan intercept pembuang respons mengikuti Langkah Uji TC. Pembuangan respons dilepas segera sesudah pemicu (S-09). Asersi mencakup toast (FE) dan state server (jumlah transaksi dan saldo). Klik `[Submit]` pada langkah 58, 96, dan 106 tidak mengasersi toast jaringan karena TC-AC-ACHA-153 langkah 3 tidak punya Expected untuk itu. Karena kiriman memakai form UI, toast diasersi sesuai Expected TC (bagian 8b butir 1 berlaku untuk permintaan langsung tanpa browser).
- Langkah penghubung (S-03): langkah baseline (1, 79, 86, 54, 92, 103), langkah baca ulang lewat fixture baca, langkah pemulihan saldo dan harga (S-09, R-08), langkah ganti akun (S-07), langkah memasang pendeteksi dialog `alert`, menampilkan kolom Notes lewat Setup Column, dan menutup modal Allocation Log.
- Pembacaan state lewat fixture baca adalah kemampuan "disediakan tim FE/BE" tanpa endpoint karangan (S-11, S-13).
- Ukuran spec: 112 langkah (melewati sekitar 35 langkah). Alasan: seluruh blok satu kelas harness (a, defense-in-depth) dan berdiri sendiri dengan data dan pembanding sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah baca ulang state dan ganti akun tidak dihitung menurut bagian 3 konvensi (Smell).
- Pengecualian S-12 nama literal (Lampiran A butir A-11): payload Notes `<script>alert(1)</script><img src=x onerror=alert(2)>` dan Category `RFID Premium` ditulis persis seperti TC (Pre-setup #66).
- Temuan untuk QA:
  - TC-AC-ACHA-426 dan TC-AC-ACHA-436 tidak menyebut kode atau pesan penolakan; spec hanya mengasersi "ditolak".
  - TC-AC-ACHA-423 a menyebut tiga permintaan pertama ditolak dengan satu pesan tetapi `Quantity 2.5` mungkin ditolak pesan berbeda oleh validator; spec mengikuti TC.
  - TC-AC-ACHA-435 b (isi berkas CSV) adalah asersi isi berkas (kelas f) yang digabung dengan kelas a mengikuti pembagian TC; spec menaruhnya di sini karena TC tunggal. Panjang Notes payload (sekitar 59 karakter) tidak diperiksa terhadap batas Notes.
  - TC-AC-ACHA-153 langkah 3 menyebut toast jaringan tampil sebagai langkah tanpa Expected; spec tidak mengasersinya.
  - TC-AC-ACHA-153 Expected b ("saldo kantong berkurang $10.00") bergantung pada harga BLE Gateway $2.00 (Pre-setup #14) dengan Quantity 5; kategori `Hardware - BLE Gateway` pada TC-AC-ACHA-153 dan 154 berbeda penulisan dari `TAG - BLE` pada TC lain.
  - TC-AC-ACHA-154 dan TC-AC-ACHA-254 menyebut Reserved "bertambah $10.00" (154) dan "satu kali" (254) tanpa nominal; spec memakai Total Cost Pre-setup #52 ($100.00) untuk 254.
  - TC-AC-ACHA-437 dan 438 mengubah saldo dan harga Pre-setup lewat Pre-setup #20 yang tidak menyebut kontrak fixture; ditulis "disediakan tim FE/BE".
  - Post Condition TC-AC-ACHA-153 dan 154 ("Wallet Balance ... ") dan TC-AC-ACHA-435 tidak punya langkah observasi di luar Expected dan tidak diasersi tambahan.

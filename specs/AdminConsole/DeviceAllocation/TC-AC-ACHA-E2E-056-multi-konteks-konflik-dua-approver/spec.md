---
id: TC-AC-ACHA-E2E-056-multi-konteks-konflik-dua-approver
title: "Multi-Konteks: Konflik Dua Approver, Review Basi Setelah Cancel atau Edit, Edit Bersamaan Dua Sesi, dan State List per Tab Browser"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHA-368
  - TC-AC-ACHA-441
  - TC-AC-ACHA-442
  - TC-AC-ACHA-443
  - TC-AC-ACHA-444
  - TC-AC-ACHA-445
  - TC-AC-ACHA-446
  - TC-AC-ACHA-455
coverage:
  web: automated
---

# Multi-Konteks: Konflik Dua Approver, Review Basi Setelah Cancel atau Edit, Edit Bersamaan Dua Sesi, dan State List per Tab Browser

## Prerequisites

- Mode: FE+BE.
- Kelas harness c (multi-konteks): dua konteks UI (browser) atau dua tab berjalan bersamaan dan hasil di konteks atau tab kedua diasersi. Konteks UI ditutup dan sesi login browser terkait dihapus pada akhir blok yang memakainya (S-09).
- Akun (Pre-setup, email lengkap `<alias>_automated_qaTeam1@qwertysystem.net`; password lewat env var, bukan di spec atau fixture):

| Alias | Pre-setup | Nama pengguna | Peran di spec | Env var password |
|---|---|---|---|---|
| `totalControlDistributor` | #27 | Hendra Wibowo | Konteks A (aktor hook `before`): approver pertama dan pembaca Allocation Log, Wallet | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| `groupManagerDistributor` | #29 | Agus Hartono | Konteks B: approver kedua (TC-AC-ACHA-441 dan 442) | `Spectra.env.AC_DA_GM_DIST_PASSWORD` |
| `memberOnDistributor` | #32 | Budi Santoso (MB_ON) | Pembuat transaksi; pelaku kedua lewat sesi API (TC-AC-ACHA-443, 444, 445, 446); dua konteks UI A dan B (TC-AC-ACHA-455) | `Spectra.env.AC_DA_MB_ON_PASSWORD` |
| `totalControlPrincipal` | #21 | Admin Pratama | Konteks A pada TC-AC-ACHA-368 (dua tab pada konteks yang sama) | `Spectra.env.AC_TC_PASSWORD` |

- Login akun pertama (Hendra Wibowo) di hook `before` spec ini (konteks A); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite dan menutup semua konteks tambahan.
- Hook suite (dinyatakan di `suite.md`): flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, sesi API aktor, fixture API disediakan tim FE/BE, pemulihan preferensi Setup Column.
- Data Pre-setup: #7 Client PT Sejahtera Logistik, #14 harga produk (RFID Object TAG PT ABC $2.50), #16 kantong PT Global Distribusi saldo $20,000.00, #48 Seed 30 alokasi (TC-AC-ACHA-368).
- Data seeding milik spec (fixture API tim FE/BE; salinan milik spec dari Pre-setup #49 yang dibuat oleh MB_ON): transaksi Waiting for Approval (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00), satu salinan baru untuk tiap blok TC-AC-ACHA-441, 442, 443, 444 (dipakai juga oleh TC-AC-ACHA-446), 445, dan 455. Tiap salinan dibuat lewat fixture pada langkah pembuka blok (bukan di hook `before`), sehingga waktu pembuatannya per blok dan tidak ada salinan yang lebih tua dari blok yang memakainya. Jam server tidak digeser di spec ini, sehingga job Timeout tidak membatalkan salinan.
- Baseline Reserved dan saldo (S-12): transaksi Waiting for Approval blok sebelumnya yang belum selesai (mis. salinan TC-AC-ACHA-445 yang tetap Waiting) masih memegang Reserve pada kantong PT Global Distribusi, sehingga nilai absolut $0.00, $300.00, $325.00, dan $19,750.00 tidak dipakai. Tiap blok mencatat saldo (S0) dan Reserved (R0) kantong PT Global Distribusi lewat fixture baca pada langkah pembuka blok, sesudah salinan dibuat, dan semua asersi saldo dan Reserved berupa selisih terhadap S0 dan R0.
- Kemampuan teknis: dua konteks browser terpisah (konteks A dan B) dengan sesi login masing-masing, dibuka dan ditutup lewat langkah eksplisit; tab browser kedua pada konteks A (TC-AC-ACHA-368); sesi API aktor untuk pelaku kedua yang hanya memicu perubahan state (Cancel dan Edit oleh MB_ON); fixture baca (disediakan tim FE/BE) untuk Reserved kantong, saldo, status, dan Quantity transaksi; Wallet Balance dan Wallet Transaction List untuk saldo kantong. Pesan dan dialog konflik muncul di Approvals > Device Allocation (aksi Approve dan Reject dilakukan di modul Approvals; mekanik halaman Approvals diuji di `tc-approvals.md`).
- Pemulihan (R-08): hook `after` memulihkan saldo dan Reserved kantong PT Global Distribusi serta seed 30 baris lewat fixture yang disediakan tim FE/BE; transaksi yang dibuat spec tidak dapat dihapus lewat UI dan audit trail bertambah permanen. Tidak ada Pre-setup bersama yang diubah selain saldo dan Reserve kantong PT Global Distribusi.
- Jendela amat SSE (bagian 6 konvensi, pilihan spec, bukan nilai TC atau PRD): tidak dipakai; tidak ada asersi absence propagasi antar-tab.
- Suite berjalan serial (`parallel: false`): saldo kantong dan Reserved adalah state bersama; asersi berupa selisih terhadap baseline blok.

## Test Steps

### TC-AC-ACHA-441: Persetujuan oleh dua approver bersamaan: pemenang commit pertama

1. Buat salinan transaksi Waiting for Approval milik MB_ON lewat fixture, catat Allocation ID-nya, lalu catat saldo (S0) dan Reserved (R0) kantong PT Global Distribusi lewat fixture baca
2. Buka konteks B (browser terpisah), login sebagai Group Manager Group Jakarta `groupManagerDistributor` (Pre-setup #29), buka Approvals > Device Allocation, dan buka Review transaksi (salinan blok ini), lalu biarkan terbuka
3. Di konteks A, buka Approvals > Device Allocation, klik `[Approve]` pada transaksi yang sama, lalu konfirmasi sampai toast sukses
4. Di konteks B, klik `[Approve]` pada Review yang masih terbuka, lalu konfirmasi
5. Verifikasi approver kedua (konteks B) ditolak dengan pesan "Approval cannot be made. This has already been resolved."
6. Di konteks A, buka Allocation > Device Allocation, cari transaksi itu lewat Search Allocation ID, dan baca status
7. Verifikasi approver pertama berhasil: status transaksi `Completed`
8. Baca saldo kantong PT Global Distribusi dan Wallet Transaction List lewat Wallet Balance
9. Verifikasi Wallet Transaction List memuat satu Capture $250.00 untuk transaksi itu
10. Verifikasi tidak ada Capture kedua untuk transaksi itu
11. Verifikasi saldo kantong sama dengan S0 dikurangi $250.00
12. Buka menu row action `⋯` transaksi itu dan klik `Allocation Log`
13. Verifikasi hanya satu entri `Allocation approved` pada Allocation Log
14. Tutup modal Allocation Log dengan `[×]`
15. Tutup konteks B dan hapus sesi login browser terkait

### TC-AC-ACHA-442: Reject setelah transaksi disetujui approver lain ditolak

16. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture, catat Allocation ID-nya, lalu catat saldo (S0) dan Reserved (R0) kantong PT Global Distribusi lewat fixture baca
17. Buka konteks B (browser terpisah), login sebagai Group Manager Group Jakarta `groupManagerDistributor` (Pre-setup #29), buka Approvals > Device Allocation, dan buka Review transaksi (salinan blok ini), lalu biarkan terbuka
18. Di konteks A, buka Approvals > Device Allocation, klik `[Approve]` pada transaksi yang sama, lalu konfirmasi sampai toast sukses
19. Di konteks B, isi Rejection Reason `Terlambat`, klik `[Reject]`, lalu konfirmasi
20. Verifikasi Reject ditolak dengan pesan "Approval cannot be made. This has already been resolved."
21. Di konteks A, buka Allocation > Device Allocation, cari transaksi itu lewat Search Allocation ID, dan baca status
22. Verifikasi status tetap `Completed`
23. Baca Reserved dan saldo kantong PT Global Distribusi lewat Wallet Balance
24. Verifikasi saldo kantong sama dengan S0 dikurangi $250.00 (Capture satu kali)
25. Verifikasi Reserved sama dengan R0 dikurangi $250.00 (tidak ada Release tambahan)
26. Buka menu row action `⋯` transaksi itu dan klik `Allocation Log`
27. Verifikasi modal Allocation Log memuat entri `Allocation approved` (anchor positif sebelum asersi absence)
28. Verifikasi Allocation Log tidak memuat entri `Allocation rejected`
29. Tutup modal Allocation Log dengan `[×]`
30. Tutup konteks B dan hapus sesi login browser terkait

### TC-AC-ACHA-443: Approve pada transaksi yang sudah dibatalkan creator

31. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture, catat Allocation ID-nya, lalu catat saldo (S0) dan Reserved (R0) kantong PT Global Distribusi lewat fixture baca
32. Di konteks A, buka Approvals > Device Allocation dan buka Review transaksi (salinan blok ini), lalu biarkan terbuka
33. Kirim Cancel (`Cancel Allocation`) untuk transaksi itu lewat sesi API `Budi Santoso` hingga status `Canceled` tersimpan
34. Di konteks A, klik `[Approve]` pada Review yang masih terbuka, lalu konfirmasi
35. Verifikasi Approve ditolak dengan dialog `Request No Longer Available`
36. Verifikasi dialog `Request No Longer Available` mengalihkan ke Tab Active di Approvals
37. Buka Allocation > Device Allocation, cari transaksi itu lewat Search Allocation ID, dan baca status
38. Verifikasi status tetap `Canceled`
39. Baca Reserved dan saldo kantong PT Global Distribusi lewat Wallet Balance
40. Verifikasi Reserved sama dengan R0 dikurangi $250.00 (Reserve transaksi blok dilepas oleh Cancel)
41. Verifikasi tidak ada Capture: saldo kantong sama dengan S0

### TC-AC-ACHA-444: Approve dari Review yang dibuka sebelum Edit ditolak

42. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture, catat Allocation ID-nya, lalu catat saldo (S0) dan Reserved (R0) kantong PT Global Distribusi lewat fixture baca
43. Di konteks A, buka Approvals > Device Allocation dan buka Review transaksi (Quantity 100, salinan blok ini), lalu biarkan terbuka
44. Kirim Edit Quantity menjadi `120` untuk transaksi itu lewat sesi API `Budi Santoso` hingga Quantity `120` tersimpan
45. Di konteks A, klik `[Approve]` pada Review yang dibuka sebelum Edit, lalu konfirmasi
46. Verifikasi Approve ditolak dengan pesan "Transaction Data Has Changed"
47. Buka Allocation > Device Allocation, cari transaksi itu lewat Search Allocation ID, dan baca status serta Quantity
48. Verifikasi status tetap `Waiting for Approval`
49. Verifikasi Quantity 120
50. Baca Reserved dan saldo kantong PT Global Distribusi lewat fixture baca
51. Verifikasi Reserved sama dengan R0 ditambah $50.00 (Reserve transaksi blok naik dari $250.00 menjadi $300.00 untuk Quantity 120)
52. Verifikasi tidak ada Capture: saldo kantong sama dengan S0
53. Buka menu row action `⋯` transaksi itu dan klik `Allocation Log`
54. Verifikasi modal Allocation Log tampil dengan entri `Allocation created`
55. Verifikasi tidak ada entri `Allocation approved`
56. Tutup modal Allocation Log dengan `[×]`

### TC-AC-ACHA-446: Approve dari Review yang dibuka ulang setelah Edit berhasil

57. Buka Approvals > Device Allocation
58. Buka kembali Review transaksi yang sama (Quantity 120 hasil Edit MB_ON), lalu klik `[Approve]` dan konfirmasi
59. Verifikasi Approve berhasil dengan toast sukses
60. Buka Allocation > Device Allocation, cari transaksi itu lewat Search Allocation ID, dan baca status
61. Verifikasi status `Completed`
62. Buka Wallet Transaction List kantong PT Global Distribusi dan baca transaksi Capture terbaru
63. Verifikasi Capture $300.00 (Quantity 120 x snapshot $2.50)

### TC-AC-ACHA-445: Reject dari Review yang dibuka sebelum Edit ditolak

64. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture, catat Allocation ID-nya, lalu catat saldo (S0) dan Reserved (R0) kantong PT Global Distribusi lewat fixture baca
65. Di konteks A, buka Approvals > Device Allocation dan buka Review transaksi (Quantity 100, salinan baru untuk blok ini), lalu biarkan terbuka
66. Kirim Edit Quantity menjadi `120` untuk transaksi itu lewat sesi API `Budi Santoso` hingga Quantity `120` tersimpan
67. Di konteks A, isi Rejection Reason `Stok belum siap` pada Review yang dibuka sebelum Edit, klik `[Reject]`, lalu konfirmasi
68. Verifikasi Reject ditolak dengan pesan "Transaction Data Has Changed"
69. Buka Allocation > Device Allocation, cari transaksi itu lewat Search Allocation ID, dan baca status
70. Verifikasi status tetap `Waiting for Approval`
71. Baca Reserved kantong PT Global Distribusi lewat fixture baca
72. Verifikasi Reserved sama dengan R0 ditambah $50.00 (hasil Edit, tidak ada Release)
73. Buka menu row action `⋯` transaksi itu dan klik `Allocation Log`
74. Verifikasi modal Allocation Log tampil dengan entri `Allocation created`
75. Verifikasi Allocation Log tidak memuat entri `Allocation rejected`
76. Tutup modal Allocation Log dengan `[×]`

### Ganti ke Budi Santoso untuk Edit bersamaan

77. Logout dari konteks A lalu login sebagai Group Member Distributor `memberOnDistributor` (Pre-setup #32), lalu buka Allocation > Device Allocation

### TC-AC-ACHA-455: Edit bersamaan pada dua sesi memakai last-write-wins

78. Buat salinan baru transaksi Waiting for Approval milik MB_ON lewat fixture, catat Allocation ID-nya, lalu catat saldo (S0) dan Reserved (R0) kantong PT Global Distribusi lewat fixture baca
79. Buka konteks B (browser terpisah), login sebagai `memberOnDistributor` (akun yang sama), dan buka Allocation > Device Allocation
80. Di konteks A, muat ulang halaman (F5), cari transaksi itu lewat Search Allocation ID, lalu klik `Edit` pada transaksi Waiting for Approval milik MB_ON (salinan blok ini)
81. Di konteks B, cari transaksi yang sama lewat Search Allocation ID, lalu klik `Edit`
82. Di konteks A, ubah Quantity menjadi `120`, klik `[Save]`, dan tunggu toast sukses
83. Di konteks B, ubah Quantity menjadi `130`, lalu klik `[Save]`
84. Verifikasi Save konteks B berhasil
85. Verifikasi tidak ada dialog konflik versi (last-write-wins)
86. Di konteks A, muat ulang halaman (F5), cari transaksi itu lewat Search Allocation ID, dan baca Quantity
87. Verifikasi Quantity tersimpan 130
88. Baca Reserved kantong PT Global Distribusi lewat Wallet Balance
89. Verifikasi Reserved sama dengan R0 ditambah $75.00 (Reserve transaksi blok naik dari $250.00 menjadi $325.00 untuk 130 x $2.50)
90. Buka menu row action `⋯` transaksi itu dan klik `Allocation Log`
91. Verifikasi Allocation Log memuat dua entri `Allocation edited` berurutan (Quantity 120 lalu 130)
92. Verifikasi Allocation Log memuat satu entri `Allocation created`
93. Tutup modal Allocation Log dengan `[×]`
94. Tutup konteks B dan hapus sesi login browser terkait

### Ganti ke Admin Pratama untuk state List per tab

95. Logout dari konteks A lalu login sebagai Total Control Principal `totalControlPrincipal` (Pre-setup #21), lalu buka Allocation > Device Allocation

### TC-AC-ACHA-368: State List terikat per tab browser

96. Catat total baris List tanpa Search (T) dari teks total baris di footer pagination
97. Di tab pertama (konteks A), ketik Search `Budi`, tekan Enter
98. Verifikasi tab pertama menampilkan hasil Search `Budi` (sedikitnya satu baris)
99. Buka tab browser baru pada konteks A, lalu buka Allocation > Device Allocation pada tab baru
100. Verifikasi kotak Search pada tab baru kosong
101. Verifikasi tab baru menampilkan total baris di footer pagination sama dengan T (default tanpa Search)
102. Tutup tab baru, kembali ke tab pertama
103. Klik `(←)` pada kotak Search

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (Section 9a dan TC-AC-ACHA-455 di Section 9b; TC-AC-ACHA-368 di bagian 4a-8). Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan: TC-AC-ACHA-446 ditaruh tepat sesudah TC-AC-ACHA-444 karena TC-AC-ACHA-446 melanjutkan transaksi hasil Edit pada TC-AC-ACHA-444 (S-04: precondition TC-AC-ACHA-446 e; langkah TC-AC-ACHA-444 disalin utuh di blok sebelumnya); TC-AC-ACHA-445 memakai transaksi baru. TC-AC-ACHA-455 ditaruh sesudahnya karena memakai akun Budi Santoso dan ganti akun eksplisit (S-07); TC-AC-ACHA-368 ditaruh terakhir karena memakai akun Total Control Principal dan ganti akun eksplisit (S-07).
- S-04: TC-AC-ACHA-368 mencantumkan TC-AC-ACHA-366 sebagai dependensi. TC-AC-ACHA-366 (state List dipertahankan setelah F5) dijalankan utuh di spec 042; langkah TC-AC-ACHA-368 tidak memakai data atau hasil TC-AC-ACHA-366 (Search `Budi` diketik baru pada tab pertama), sehingga langkah TC-AC-ACHA-366 tidak disalin ke blok ini.
- TC-AC-ACHA-368 (kelas c): tab browser kedua adalah objek asersi (state List terikat per tab), bukan pemicu, sehingga `P-2` tidak berlaku (bagian 3 prinsip 13, kalimat tentang konteks kedua yang menjadi objek asersi) dan TC ini berada di spec multi-konteks bersama TC kelas c lain. Tab kedua dibuka pada konteks A (sesi login dibagi); konteks B tidak dipakai. Asersi memakai baseline total baris (T, dibaca dari footer pagination) karena transaksi spec ini dan spec lain menambah baris Seed List 30.
- Pelaku kedua lewat sesi API (R-20): Cancel (TC-AC-ACHA-443) dan Edit (TC-AC-ACHA-444, 445, 446) oleh `Budi Santoso` hanya memicu perubahan state; hasilnya diasersi di konteks UI A. Tidak memakai `P-2`. Konteks B pada TC-AC-ACHA-441, 442, dan 455 adalah objek asersi (kelas c) sehingga ditulis sebagai konteks UI kedua di spec ini; konteks B ditutup dengan sesi login dihapus (S-09).
- Langkah penghubung (S-03): langkah membuat salinan dan mencatat baseline S0 dan R0 (1, 16, 31, 42, 64, 78); langkah membuka konteks B (2, 17, 79); langkah menutup konteks B dan menghapus sesi login (15, 30, 94); langkah mencari transaksi di List (R-16, Search Allocation ID); langkah menutup modal Allocation Log; langkah membuka Approvals > Device Allocation sesudah Review lama ditinggalkan (57); langkah mencatat total baris T (96); langkah menutup tab baru dan mengosongkan Search lewat `(←)` (102, 103); langkah ganti akun (77, 95; S-07).
- Asersi tambahan di luar Expected TC: langkah baca status di List sebelum asersi lain pada TC-AC-ACHA-441, 442, 443 (Expected a/b memuat status), baca Reserved pada TC-AC-ACHA-442 (langkah 25) untuk "tidak ada Release" (kemampuan baca lewat Wallet Balance), `Verifikasi` modal Allocation Log memuat entri `Allocation approved` pada TC-AC-ACHA-442 (langkah 27) sebagai anchor positif sebelum asersi absence `Allocation rejected`, dan `Verifikasi` tab pertama menampilkan hasil `Budi` (langkah 98) sebagai anchor positif sebelum asersi tab baru.
- Pengecualian S-12 nama literal (Lampiran A butir A-11): Rejection Reason `Terlambat` dan `Stok belum siap`, serta Notes `Batch uji`, ditulis persis seperti TC.
- Ukuran spec: 103 langkah (melewati sekitar 35 langkah). Alasan: seluruh blok satu kelas harness (c, multi-konteks/race antar-sesi dan multi-tab) dan tiap blok memakai transaksi sendiri (kecuali TC-AC-ACHA-446 yang melanjutkan TC-AC-ACHA-444), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; pembukaan konteks, pencatatan baseline, pembacaan state lewat Wallet Balance dan Allocation Log menambah langkah tanpa verifikasi.
- Temuan untuk QA:
  - TC-AC-ACHA-441 b ("saldo kantong $19,750.00"), 443 b ("Reserved $0.00"), 444 b dan 445 b ("Reserved $300.00"), serta 455 a ("Reserved $325.00") mengandaikan tidak ada transaksi Waiting for Approval lain yang memegang Reserve pada kantong yang sama; precondition TC tidak menyatakannya. Spec mengasersi selisih terhadap baseline saldo (S0) dan Reserved (R0) per blok.
  - TC-AC-ACHA-441 dan 442 tidak menyebut di mana pesan "Approval cannot be made. This has already been resolved." tampil (toast, dialog, atau inline); spec hanya mengasersi "pesan tampil".
  - TC-AC-ACHA-442 a ("tidak ada Release") tidak memberi cara mengamati Release; spec membaca Reserved dan saldo kantong lewat Wallet Balance.
  - TC-AC-ACHA-443 a menyebut dialog `Request No Longer Available` dengan pengalihan ke Tab Active tanpa judul, isi, dan tombol dialog; spec mengasersi nama dialog dan pengalihan saja.
  - TC-AC-ACHA-444 dan 445 tidak menyebut apakah Review yang basi tetap terbuka sesudah penolakan; langkah berikutnya membuka Allocation > Device Allocation lewat navigasi.
  - TC-AC-ACHA-446 precondition e berbunyi "Review lama sudah ditolak (TC-AC-ACHA-444)"; spec menjalankan TC-AC-ACHA-444 utuh pada transaksi yang sama sebelum TC-AC-ACHA-446.
  - TC-AC-ACHA-455 menyebut "akun yang sama" untuk sesi A dan B tanpa menyebut apakah ada batas satu sesi web per akun; bila ada, konteks B memerlukan kemampuan yang disediakan tim FE/BE.
  - TC-AC-ACHA-368 Expected ("Tab baru mulai dari default tanpa Search") tidak menyebut jumlah baris atau indikator default selain Search; spec mengasersi kotak Search kosong dan total baris sama dengan baseline T.
  - Post Condition TC-AC-ACHA-441 dan 446 ("Wallet Balance ... Client Dashboard ...") dan TC-AC-ACHA-455 tidak punya langkah observasi di luar Expected dan tidak diasersi tambahan.

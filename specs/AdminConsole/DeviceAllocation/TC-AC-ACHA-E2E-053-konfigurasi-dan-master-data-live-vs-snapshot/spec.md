---
id: TC-AC-ACHA-E2E-053-konfigurasi-dan-master-data-live-vs-snapshot
title: "Konfigurasi dan Data Master: Dibaca Live atau Snapshot (Harga, Nama Client, Pengirim, Paid From, Allocated By, Toggle Approval, Lingkup Group Manager, dan Resubmit)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHA-413
  - TC-AC-ACHA-414
  - TC-AC-ACHA-415
  - TC-AC-ACHA-416
  - TC-AC-ACHA-417
  - TC-AC-ACHA-418
  - TC-AC-ACHA-419
  - TC-AC-ACHA-420
coverage:
  web: automated
---

# Konfigurasi dan Data Master: Dibaca Live atau Snapshot (Harga, Nama Client, Pengirim, Paid From, Allocated By, Toggle Approval, Lingkup Group Manager, dan Resubmit)

## Prerequisites

- Mode: FE+BE.
- Akun (Pre-setup, email lengkap `<alias>_automated_qaTeam1@qwertysystem.net`; password lewat env var, bukan di spec atau fixture):

| Alias | Pre-setup | Nama pengguna | Dipakai di | Env var password |
|---|---|---|---|---|
| `totalControlPrincipal` | #21 | Admin Pratama (aktor hook `before`) | TC-AC-ACHA-414, 415, 416, 417 | `Spectra.env.AC_TC_PASSWORD` |
| `totalControlDistributor` | #27 | Hendra Wibowo | TC-AC-ACHA-413 | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| `memberOnDistributor` | #32 | Budi Santoso (MB_ON) | TC-AC-ACHA-413 (Edit), 418, 420 | `Spectra.env.AC_DA_MB_ON_PASSWORD` |
| `groupManagerDistributor` | #29 | Agus Hartono | TC-AC-ACHA-419 | `Spectra.env.AC_DA_GM_DIST_PASSWORD` |
| `memberOnPartner1` | #44 | Andi Wijaya (MB_P1) | Pembuat transaksi TC-AC-ACHA-415 (sesi API) | `Spectra.env.AC_DA_MB_P1_PASSWORD` |

- Login akun pertama (Admin Pratama) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite dan memulihkan seluruh state global di bawah ini.
- Hook suite (dinyatakan di `suite.md`): flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, sesi API aktor, fixture API disediakan tim FE/BE, pemulihan preferensi Setup Column.
- State global yang diubah spec (dipulihkan sebagai langkah penghubung sesudah tiap blok dan di hook `after`, yang tetap jalan walau spec gagal di tengah; suite berjalan serial, `parallel: false`):
  - harga RFID Object TAG PT ABC (Wallet > Product Price) dari $2.50 menjadi $4.00 (TC-AC-ACHA-413);
  - nama Client `PT Sejahtera Logistik` (Pre-setup #7) menjadi `PT Nusantara Telematika` (TC-AC-ACHA-414);
  - nama Partner `CV Mitra Solusi` (Pre-setup #4) menjadi `CV Bintang Timur` (TC-AC-ACHA-415);
  - nama Distributor `PT Global Distribusi` (Pre-setup #3) menjadi `PT Global Distribusi Utama` (TC-AC-ACHA-416);
  - nama belakang pengguna `Budi Santoso` (Pre-setup #32) menjadi `Kurniawan`, nama lengkap `Budi Kurniawan` (TC-AC-ACHA-417);
  - toggle Require Approval for Allocation role Manage allocation `Budi Santoso` di Group Jakarta ON menjadi OFF (TC-AC-ACHA-418 dan 420);
  - keanggotaan `Agus Hartono` di Group Jakarta dari Group Manager menjadi Group Member dengan role Manage allocation toggle ON (TC-AC-ACHA-419).
- Dasar S-06: nama Client, Partner, Distributor, dan pengguna Pre-setup, toggle Require Approval for Allocation, keanggotaan Group Manager, dan harga produk PT ABC adalah data bersama yang tidak dapat dimiliki spec, karena yang diasersi adalah entitas Pre-setup yang dipakai baris Seed List dan akun Pre-setup. Syaratnya dipenuhi: pemulihan ke keadaan awal dijamin fixture yang disediakan tim FE/BE (pengubah nama Client, Partner, Distributor, dan pengguna; toggle Require Approval; keanggotaan Group Manager; harga produk) dan dinyatakan di `suite.md`; fixture memulihkan semuanya ke nilai Pre-setup di hook `before` (idempotent), di hook `after`, dan sebagai langkah penghubung sesudah tiap blok; suite berjalan serial.
- Efek pada Pre-setup bersama (S-06): Last Updated pada modul Client, Partner, Distributor, pengguna, role, group, dan harga produk berubah, dan entri audit trail pengubahan nama, hak, dan harga bertambah permanen (tidak dapat dihapus lewat UI) walau nilainya dipulihkan.
- "Muat ulang List" berarti muat ulang halaman (F5); Search List dipertahankan setelah F5 (TC-AC-ACHA-366), sehingga isi kotak Search diganti dengan "ganti isi kotak search dengan `X`, tekan Enter".
- Kemampuan teknis (disediakan tim FE/BE): fixture pengubah nama Client, Partner, Distributor, dan pengguna (setara perubahan di modul Client, Partner, dan Settings > User), fixture pengubah toggle Require Approval for Allocation di Settings > Role & Permission, fixture pengubah keanggotaan Group Manager di Settings > Group, fixture baca Reserved kantong PT Global Distribusi, dan fixture pemulihan semuanya; akses UI Wallet Balance dan Wallet Transaction List kantong PT Global Distribusi untuk membaca saldo dan transaksi Capture (TC-AC-ACHA-413, langkah 74 sampai 79).
- Data Pre-setup: #3, #4, #7, #14 (harga produk), #16 kantong PT Global Distribusi saldo $20,000.00 (Reserved awal $0.00, dipulihkan fixture di hook `before`), #48 Seed 30 alokasi (baris `HALC-20260901-00001` dengan Allocated By `Budi S (Budi Santoso)` dan baris `HALC-20260901-00003` milik CV Mitra Solusi dengan Paid From `PT Global Distribusi (Distributor)`; keduanya hanya dibaca, tidak diubah), #52 transaksi Canceled milik MB_ON.
- Data seeding milik spec (fixture API disediakan tim FE/BE): transaksi Waiting for Approval milik MB_ON (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00) salinan Pre-setup #49 untuk TC-AC-ACHA-413; transaksi Canceled milik MB_ON (BLE Gateway, Quantity 50, Pay From `PT ABC (Principal)`, Notes `Batch lama`, Total Cost $100.00) salinan Pre-setup #52 untuk TC-AC-ACHA-420. Transaksi TC-AC-ACHA-415 (NFC, Quantity 10, Client PT Retail Makmur) dibuat sesi API `Andi Wijaya` sebelum nama Partner diganti. Transaksi TC-AC-ACHA-418 dan 419 dibuat lewat UI; yang berstatus Waiting for Approval dibatalkan di hook `after`. Allocation ID tiap salinan ditangkap dari respons fixture seeding (Dynamic Reference) dan dipakai sebagai penanda Search, asersi, dan cleanup hook `after`.
- Kolom Cost dan Paid From tidak tampil secara default: spec menampilkannya lewat Setup Column (TC-AC-ACHA-413 dan 416); preferensi kolom dipulihkan hook `after` suite.

## Test Steps

### TC-AC-ACHA-414: Nama Client mengikuti nama terkini

1. Ganti nama Client `PT Sejahtera Logistik` menjadi `PT Nusantara Telematika` lewat fixture pengubah nama
2. Muat ulang halaman (F5), lalu ketik Search `Nusantara`, tekan Enter
3. Verifikasi tabel memuat sedikitnya satu baris hasil Search
4. Verifikasi seluruh baris hasil Search menampilkan Client `PT Nusantara Telematika` (nama terkini)
5. Buka Filter Panel dan buka opsi field Client
6. Verifikasi opsi filter Client memuat `PT Nusantara Telematika`
7. Verifikasi opsi filter Client tidak lagi memuat `PT Sejahtera Logistik`
8. Tutup Filter Panel tanpa menerapkan filter, lalu buka menu row action `⋯` salah satu baris hasil Search dan klik `Allocation Log`
9. Verifikasi header Client pada modal Allocation Log menampilkan `PT Nusantara Telematika` (nama terkini)
10. Tutup modal Allocation Log dengan `[×]`
11. Kembalikan nama Client menjadi `PT Sejahtera Logistik` lewat fixture pengubah nama

### TC-AC-ACHA-415: Nama pengirim mengikuti nama terkini sedangkan entri log tetap

12. Kirim Submit alokasi NFC Quantity `10` untuk Client `PT Retail Makmur` lewat sesi API `Andi Wijaya` hingga transaksi berstatus Waiting for Approval tersimpan, lalu catat Allocation ID
13. Ganti nama Partner `CV Mitra Solusi` menjadi `CV Bintang Timur` lewat fixture pengubah nama
14. Muat ulang halaman (F5), lalu ganti isi kotak search dengan Allocation ID itu, tekan Enter
15. Verifikasi kolom From pada baris transaksi itu menampilkan `CV Bintang Timur` (nama terkini)
16. Buka Filter Panel dan buka opsi field From
17. Verifikasi opsi filter From memuat `CV Bintang Timur`
18. Verifikasi opsi filter From tidak lagi memuat `CV Mitra Solusi`
19. Tutup Filter Panel tanpa menerapkan filter, lalu buka menu row action `⋯` transaksi itu dan klik `Allocation Log`
20. Verifikasi entri `Allocation created` tetap menampilkan `From: CV Mitra Solusi` (nilai saat kejadian, entri log immutable)
21. Tutup modal Allocation Log dengan `[×]`
22. Kembalikan nama Partner menjadi `CV Mitra Solusi` lewat fixture pengubah nama

### TC-AC-ACHA-416: Nama Paid From mengikuti nama terkini

23. Tampilkan kolom Paid From lewat Setup Column dan klik `[Save]`
24. Ganti nama Distributor `PT Global Distribusi` menjadi `PT Global Distribusi Utama` lewat fixture pengubah nama
25. Muat ulang halaman (F5), lalu ganti isi kotak search dengan `HALC-20260901-00003`, tekan Enter
26. Verifikasi kolom Paid From baris `HALC-20260901-00003` menampilkan `PT Global Distribusi Utama (Distributor)`
27. Buka Filter Panel dan buka opsi field Paid From
28. Verifikasi opsi filter Paid From memakai nama terkini `PT Global Distribusi Utama (Distributor)`
29. Tutup Filter Panel tanpa menerapkan filter, lalu buka menu row action `⋯` baris `HALC-20260901-00003` dan klik `Allocation Log`
30. Verifikasi header Paid From pada modal Allocation Log memakai nama terkini yang sama
31. Tutup modal Allocation Log dengan `[×]`
32. Kembalikan nama Distributor menjadi `PT Global Distribusi` lewat fixture pengubah nama

### TC-AC-ACHA-417: Allocated By mengikuti nama terkini sedangkan judul entri log tetap

33. Ganti nama belakang pengguna `Budi Santoso` menjadi `Kurniawan` (nama lengkap `Budi Kurniawan`) lewat fixture pengubah nama
34. Muat ulang halaman (F5), lalu ganti isi kotak search dengan `HALC-20260901-00001`, tekan Enter
35. Verifikasi kolom Allocated By baris `HALC-20260901-00001` menampilkan `Budi K` (nama terkini)
36. Buka Filter Panel dan buka opsi field Allocated By
37. Verifikasi opsi filter Allocated By memuat `Budi K`
38. Verifikasi opsi filter Allocated By tidak lagi memuat `Budi S`
39. Tutup Filter Panel tanpa menerapkan filter, lalu buka menu row action `⋯` baris `HALC-20260901-00001` dan klik `Allocation Log`
40. Verifikasi judul entri log lama tetap `Allocation created by Budi S` (nilai saat kejadian)
41. Tutup modal Allocation Log dengan `[×]`
42. Kembalikan nama belakang pengguna menjadi `Santoso` lewat fixture pengubah nama

### Ganti akun ke Hendra Wibowo

43. Logout lalu login sebagai Total Control Distributor `totalControlDistributor` (Pre-setup #27), lalu buka Allocation > Device Allocation

### TC-AC-ACHA-413: Perubahan harga master tidak memengaruhi riwayat transaksi

44. Tampilkan kolom Cost lewat Setup Column dan klik `[Save]`
45. Ubah harga RFID Object TAG PT ABC dari $2.50 menjadi $4.00 di Wallet > Product Price lewat fixture (disediakan tim FE/BE)
46. Muat ulang halaman (F5), lalu ketik Search Allocation ID transaksi Waiting for Approval milik MB_ON (salinan untuk blok ini), tekan Enter
47. Verifikasi Cost transaksi itu tetap `$250.00` setelah perubahan harga (snapshot harga, bukan harga terkini)
48. Logout lalu login sebagai Group Member Distributor `memberOnDistributor` (Pre-setup #32), lalu buka Allocation > Device Allocation
49. Klik `Edit` pada transaksi itu dan ubah Quantity menjadi `120`
50. Verifikasi Preview pada form Edit memakai `Unit Price (Snapshot)` $2.50
51. Verifikasi Preview pada form Edit menampilkan Estimated Cost $300.00 untuk Quantity 120
52. Klik `[Save]`

### TC-AC-ACHA-418: Toggle Require Approval dibaca live saat Submit

53. Klik `[+ Allocation]`, pilih Category `TAG - BLE`, Client `PT Sejahtera Logistik`, isi Quantity `20`, klik `[Submit]`, lalu catat Allocation ID sebagai alokasi pertama
54. Ganti isi kotak search dengan Allocation ID alokasi pertama, tekan Enter
55. Verifikasi alokasi pertama berstatus `Waiting for Approval`
56. Ubah toggle Require Approval for Allocation role Manage allocation `Budi Santoso` di Group Jakarta menjadi OFF di Settings > Role & Permission lewat fixture, tanpa login ulang
57. Klik `[+ Allocation]`, pilih Category `TAG - BLE`, Client `PT Sejahtera Logistik`, isi Quantity `20`, klik `[Submit]`, lalu catat Allocation ID sebagai alokasi kedua
58. Ganti isi kotak search dengan Allocation ID alokasi kedua, tekan Enter
59. Verifikasi alokasi kedua langsung `Completed` karena toggle dibaca saat Submit dari role pada group target
60. Ganti isi kotak search dengan Allocation ID alokasi pertama, tekan Enter
61. Verifikasi alokasi pertama tetap `Waiting for Approval`
62. Kembalikan toggle Require Approval for Allocation role itu menjadi ON lewat fixture

### TC-AC-ACHA-420: Resubmit membaca toggle approval saat Submit ulang

63. Ubah toggle Require Approval for Allocation role Manage allocation `Budi Santoso` di Group Jakarta menjadi OFF lewat fixture
64. Baca Reserved kantong PT Global Distribusi lewat fixture baca dan catat bersama saldo kantong sebagai kondisi awal
65. Klik `Resubmit` pada transaksi Canceled milik MB_ON (salinan untuk blok ini)
66. Klik `[Submit]` tanpa perubahan dan catat Allocation ID transaksi baru
67. Ganti isi kotak search dengan Allocation ID transaksi baru, tekan Enter
68. Verifikasi transaksi baru langsung `Completed` karena toggle dibaca saat Submit ulang, bukan saat transaksi lama dibuat
69. Baca Reserved dan saldo kantong PT Global Distribusi lewat fixture baca
70. Verifikasi Capture dilakukan tanpa Reserve: Reserved sama dengan kondisi awal
71. Verifikasi saldo kantong berkurang $100.00 (Total Cost transaksi) dibanding kondisi awal
72. Kembalikan toggle Require Approval for Allocation role itu menjadi ON lewat fixture

### Ganti akun ke Hendra Wibowo untuk Approve TC-AC-ACHA-413

73. Logout lalu login sebagai Total Control Distributor `totalControlDistributor` (Pre-setup #27)
74. Baca saldo kantong PT Global Distribusi di Wallet Balance dan catat sebagai saldo sebelum Approve
75. Buka Approvals > Device Allocation, klik `[Approve]` pada transaksi milik blok TC-AC-ACHA-413, lalu konfirmasi sampai toast sukses
76. Buka Wallet Transaction List kantong PT Global Distribusi dan baca transaksi Capture terbaru
77. Verifikasi Capture saat Approve sebesar $300.00 (snapshot harga)
78. Baca saldo kantong PT Global Distribusi di Wallet Balance
79. Verifikasi saldo kantong PT Global Distribusi berkurang $300.00 dari saldo sebelum Approve
80. Kembalikan harga RFID Object TAG PT ABC menjadi $2.50 di Wallet > Product Price lewat fixture (disediakan tim FE/BE)

### Ganti akun ke Agus Hartono (Group Manager)

81. Logout lalu login sebagai Group Manager Distributor `groupManagerDistributor` (Pre-setup #29), lalu buka Allocation > Device Allocation

### TC-AC-ACHA-419: Lingkup Group Manager dibaca live saat Submit

82. Klik `[+ Allocation]`, pilih Category `TAG - BLE`, Client `PT Sejahtera Logistik`, isi Quantity `20`, klik `[Submit]`, lalu catat Allocation ID sebagai alokasi pertama
83. Ketik Search Allocation ID alokasi pertama, tekan Enter
84. Verifikasi alokasi pertama langsung `Completed` (Group Manager pada group target auto-bypass)
85. Ubah keanggotaan `Agus Hartono` di Settings > Group menjadi Group Member Group Jakarta (bukan Group Manager) dengan role Manage allocation toggle ON lewat fixture, tanpa login ulang
86. Klik `[+ Allocation]`, pilih Category `TAG - BLE`, Client `PT Sejahtera Logistik`, isi Quantity `20`, klik `[Submit]`, lalu catat Allocation ID sebagai alokasi kedua
87. Ganti isi kotak search dengan Allocation ID alokasi kedua, tekan Enter
88. Verifikasi alokasi kedua berstatus `Waiting for Approval` karena status Group Manager sudah dicabut dan toggle ON dibaca dari role
89. Kembalikan keanggotaan `Agus Hartono` menjadi Group Manager Group Jakarta lewat fixture

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (Section 7d). Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan (S-10): TC dikelompokkan per akun aktor (Admin Pratama, Hendra Wibowo, Budi Santoso, Hendra Wibowo, Agus Hartono) supaya ganti akun minimal. TC-AC-ACHA-413 terbagi dalam tiga bagian lintas akun (harga dan Cost oleh Hendra Wibowo, Edit oleh Budi Santoso, Approve oleh Hendra Wibowo) dengan TC-AC-ACHA-418 dan 420 di antaranya; tiap TC memakai transaksi sendiri sehingga tidak bergantung pada TC lain (S-04).
- Langkah penghubung (S-03): langkah mengganti nama, toggle, keanggotaan, dan harga lewat fixture beserta langkah mengembalikannya (S-09, R-08); langkah Search Allocation ID untuk menemukan baris target (R-16, S-14); langkah menampilkan kolom Cost dan Paid From lewat Setup Column; langkah menutup Filter Panel tanpa menerapkan filter dan menutup modal Allocation Log; langkah ganti akun (S-07); langkah mencatat saldo, Reserved, dan Allocation ID sebelum aksi pemicu (baseline S-12).
- Baris target (R-16): transaksi pada langkah 49 (Edit TC-AC-ACHA-413) dan 65 (Resubmit TC-AC-ACHA-420) ditemukan lewat Search Allocation ID salinan blok yang dicatat saat seeding sebagai langkah penghubung tanpa `Verifikasi` sebelum aksi baris. Sesudah ganti akun kotak Search kosong (state List dibuang saat logout, TC-AC-ACHA-369), sehingga pencarian pertama pada akun itu memakai "ketik Search"; pencarian berikutnya dalam sesi yang sama memakai "ganti isi kotak search".
- Pemulihan toggle Require Approval dikerjakan segera sesudah asersi (langkah terakhir tiap blok) karena dua TC berbagi role yang sama; hook `after` memulihkan bila spec gagal di tengah.
- Pengecualian S-12 nama literal: nama hasil rename (`PT Nusantara Telematika`, `CV Bintang Timur`, `PT Global Distribusi Utama`, `Budi Kurniawan`) ditulis persis seperti TC (S-12: nama hasil rename ditulis, seeding dan cleanup deterministik); seed `HALC-20260901-00001` dan `HALC-20260901-00003` dibaca saja dan diasersi persis (Lampiran A butir A-6). Dasar S-06 untuk entitas Pre-setup yang diubah sementara ada di Prerequisites.
- Efek samping pada Pre-setup bersama (Last Updated dan audit trail) dicatat di Prerequisites sesuai S-06.
- Ukuran spec: 89 langkah (melewati sekitar 35 langkah). Alasan: seluruh blok satu topik (konfigurasi atau data master dibaca live atau snapshot), tiap blok memakai data sendiri dan dipulihkan, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; ganti akun (S-07) dan langkah pemulihan state menambah langkah tanpa verifikasi.
- Temuan untuk QA:
  - TC-AC-ACHA-414 dan 415 (TC sudah diperbarui): nama hasil rename `PT Nusantara Telematika` dan `CV Bintang Timur` tidak memuat nama lama, sehingga asersi absence "tidak lagi memuat nama lama" memakai pencocokan substring (R-13 terpenuhi); Search `Nusantara` pada TC-AC-ACHA-414 memakai nama baru karena nama lama tidak lagi ada pada baris.
  - TC-AC-ACHA-414 a ("seluruh baris lama") tidak menyebut baris pembanding; spec memakai Search `Nusantara` dan `Verifikasi` tabel memuat sedikitnya satu baris sebelum asersi universal.
  - TC-AC-ACHA-413 langkah 1 menyebut perubahan harga di Wallet > Product Price tanpa menyebut akun yang berhak mengubah harga PT ABC; spec memakai fixture (disediakan tim FE/BE).
  - TC-AC-ACHA-414 sampai 417 tidak menyebut jalur perubahan nama (modul Client, Partner, Settings > User) dan akun pelakunya; spec memakai fixture pengubah nama sebagai penyiapan state.
  - TC-AC-ACHA-415 precondition e menyebut transaksi "dibuat CV Mitra Solusi sebelum rename" tanpa menyebut akun pembuat; spec memakai MB_P1 (Pre-setup #44).
  - TC-AC-ACHA-416 menyebut baris Seed List "Transaksi CV Mitra Solusi dengan Pay From PT Global Distribusi (Distributor)" tanpa Allocation ID; spec memakai `HALC-20260901-00003`.
  - TC-AC-ACHA-413 c menyebut saldo $19,700.00 yang bergantung pada saldo awal $20,000.00 dan tidak ada transaksi lain; spec mengasersi selisih terhadap saldo sebelum Approve.
  - TC-AC-ACHA-418 sampai 420 tidak menyebut Reserve dan Capture yang harus teramati dari sisi akun aktor; spec hanya mengasersi status dan, untuk TC-AC-ACHA-420, Reserved lewat fixture baca.
  - Post Condition TC-AC-ACHA-418, 419, 420 ("Wallet Balance ... Client Dashboard ...") tidak punya langkah observasi di luar Expected dan tidak diasersi tambahan.

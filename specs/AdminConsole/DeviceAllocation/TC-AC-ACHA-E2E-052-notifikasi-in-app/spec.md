---
id: TC-AC-ACHA-E2E-052-notifikasi-in-app
title: "Notifikasi In-App: Penerima, Dedup Multi-Role, Tier Actionable dan View-Only, Tujuan Klik, dan Edit Tanpa Notifikasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-404
  - TC-AC-ACHA-405
  - TC-AC-ACHA-406
  - TC-AC-ACHA-407
  - TC-AC-ACHA-408
  - TC-AC-ACHA-409
  - TC-AC-ACHA-410
  - TC-AC-ACHA-411
  - TC-AC-ACHA-412
coverage:
  web: automated
---

# Notifikasi In-App: Penerima, Dedup Multi-Role, Tier Actionable dan View-Only, Tujuan Klik, dan Edit Tanpa Notifikasi

## Prerequisites

- Mode: FE+BE.
- Akun (Pre-setup, email lengkap `<alias>_automated_qaTeam1@qwertysystem.net`; password lewat env var, bukan di spec atau fixture):

| Alias | Pre-setup | Nama pengguna | Peran | Env var password |
|---|---|---|---|---|
| `totalControlDistributor` | #27 | Hendra Wibowo | Total Control, approver; aktor hook `before` | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| `groupManagerDistributor` | #29 | Agus Hartono | Group Manager Group Jakarta, approver | `Spectra.env.AC_DA_GM_DIST_PASSWORD` |
| `additionalApprover` | #37 | Bambang Prasetyo | Additional Approver Group Jakarta | `Spectra.env.AC_DA_ADD_APPROVER_PASSWORD` |
| `defaultUserDistributor` | #28 | Default User Distributor | Bukan approver | `Spectra.env.AC_DA_DU_PASSWORD` |
| `memberOnDistributor` | #32 | Budi Santoso (MB_ON) | Pembuat transaksi | `Spectra.env.AC_DA_MB_ON_PASSWORD` |
| `multiRoleApprover` | #38 | Yusuf Hidayat | Total Control sekaligus Group Manager dan Additional Approver Group Jakarta | `Spectra.env.AC_DA_MULTI_APPROVER_PASSWORD` |

- Login akun pertama (Hendra Wibowo) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite dan memulihkan jam server.
- Hook suite (dinyatakan di `suite.md`): flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, sesi API aktor, fixture API disediakan tim FE/BE, pemulihan preferensi Setup Column.
- Data Pre-setup: #7 Client PT Sejahtera Logistik, #14 harga produk, #16 kantong PT Global Distribusi saldo $20,000.00, #63 Approval Timeout 3 day(s). Approver pool Group Jakarta: Hendra Wibowo, Agus Hartono, Bambang Prasetyo (dan Yusuf Hidayat); Default User Distributor bukan approver.
- Aksi pemicu (Submit, Cancel, Edit, Approve, Reject) dikirim lewat sesi API aktor yang bersangkutan, sebagai pemicu perubahan state; asersi memakai sesi UI Notification Center akun penerima (R-20: langkah pemicu pelaku kedua ditulis "... hingga ... tersimpan"). Aksi UI Approvals tidak diasersi di spec ini.
- Baseline notifikasi (S-12, analog R-11): jumlah notifikasi per akun dicatat sebelum aksi pemicu lewat fixture baca notifikasi (disediakan tim FE/BE, jumlah per akun dan per Title), dan asersi "menerima satu notifikasi" memakai selisih satu terhadap baseline. Notifikasi dibuat asinkron: sebelum baseline akun approver dicatat, notifikasi `Waiting for your approval` untuk transaksi pemicu ditunggu terbaca lewat fixture baca notifikasi (polling 5 detik, batas 2 menit). Notification Center dimuat ulang tiap 5 detik sampai notifikasi tampil, batas tunggu 2 menit (idiom polling bagian 6 konvensi).
- Jendela absence notifikasi in-app (pilihan spec sesuai TC-AC-ACHA-408 b dan 412, bukan nilai PRD): "Tunggu 5 detik tanpa memuat ulang halaman" ditulis sebelum asersi absence pada TC-AC-ACHA-408 (approver yang menyetujui) dan TC-AC-ACHA-412 (pembuat dan approver), sesudah anchor positif pengiriman notifikasi.
- Data seeding milik spec: tidak ada Pre-setup tulis yang dipakai; semua transaksi dibuat spec lewat sesi API `Budi Santoso` (Category `TAG - BLE`, Client `PT Sejahtera Logistik`, Quantity `20`, jalur persetujuan) tepat pada langkah pembuka tiap blok (bukan di hook `before`) sehingga ber-status Waiting for Approval dan memicu notifikasi lewat jalur normal. Allocation ID transaksi blok TC-AC-ACHA-404, 405, dan 412 dicatat saat Submit karena transaksi itu tetap Waiting dan dibatalkan sebelum blok geser jam.
- Kemampuan teknis: pergeseran jam server absolut ke `T1 + 3 hari + 1 menit` lewat fixture yang disediakan tim FE/BE (T1 = waktu terbit transaksi dibaca lewat fixture; margin 1 menit dihitung dari T1) untuk TC-AC-ACHA-407; sesi UI dan API tetap valid saat jam digeser (dinyatakan di `suite.md`); jam browser tidak diubah karena Timeout dihitung di server dan tidak diamati lewat hitung mundur UI; jam server dipulihkan sebelum Notification Center dibuka.
- Efek samping geser jam: job Timeout membatalkan semua transaksi Waiting for Approval yang melewati 3 hari dari waktu terbitnya dan mengirim notifikasi pembatalan untuk tiap transaksi. Karena itu blok TC-AC-ACHA-407 berada di akhir spec dan, sebelum transaksi blok dibuat, transaksi Waiting for Approval sisa blok TC-AC-ACHA-404, 405, dan 412 dibatalkan lewat sesi API supaya pertambahan notifikasi pada baseline blok hanya berasal dari transaksi blok itu.
- Pemulihan (R-08): hook `after` memulihkan seed ke 30 baris dan jam server lewat fixture yang disediakan tim FE/BE; transaksi yang dibuat spec tidak dapat dihapus lewat UI dan notifikasi bertambah permanen. Tidak ada Pre-setup bersama yang diubah selain jam server dan saldo/Reserve kantong PT Global Distribusi.
- Suite berjalan serial (`parallel: false`): jumlah notifikasi dan jam server adalah state bersama.

## Test Steps

### TC-AC-ACHA-404: Notifikasi Waiting for Approval ke approver pool termasuk Additional Approver

1. Catat jumlah notifikasi ber-Title "Waiting for your approval" milik `Hendra Wibowo`, `Agus Hartono`, `Bambang Prasetyo`, Default User Distributor, dan `Budi Santoso` lewat fixture baca notifikasi sebagai baseline
2. Kirim Submit alokasi BLE Quantity `20` untuk PT Sejahtera Logistik lewat sesi API `Budi Santoso` hingga transaksi berstatus Waiting for Approval tersimpan, lalu catat Allocation ID
3. Buka Notification Center `Hendra Wibowo` dan muat ulang tiap 5 detik sampai notifikasi baru tampil (batas tunggu 2 menit)
4. Verifikasi Total Control `Hendra Wibowo` menerima satu notifikasi baru dengan Title "Waiting for your approval": jumlah notifikasi ber-Title itu bertambah satu terhadap baseline langkah 1
5. Verifikasi notifikasi baru itu berjenis `actionable`
6. Logout lalu login sebagai Group Manager `groupManagerDistributor` (Pre-setup #29), lalu buka Notification Center dan muat ulang tiap 5 detik sampai notifikasi baru tampil (batas tunggu 2 menit)
7. Verifikasi Group Manager Group Jakarta `Agus Hartono` menerima satu notifikasi baru dengan Title "Waiting for your approval": jumlah notifikasi ber-Title itu bertambah satu terhadap baseline langkah 1
8. Verifikasi notifikasi baru itu berjenis `actionable`
9. Logout lalu login sebagai Additional Approver `additionalApprover` (Pre-setup #37), lalu buka Notification Center dan muat ulang tiap 5 detik sampai notifikasi baru tampil (batas tunggu 2 menit)
10. Verifikasi Additional Approver `Bambang Prasetyo` menerima satu notifikasi baru dengan Title "Waiting for your approval": jumlah notifikasi ber-Title itu bertambah satu terhadap baseline langkah 1
11. Verifikasi notifikasi baru itu berjenis `actionable`
12. Logout lalu login sebagai Default User Distributor `defaultUserDistributor` (Pre-setup #28), lalu buka Notification Center
13. Verifikasi Notification Center Default User Distributor tampil
14. Verifikasi Default User Distributor tidak menerima notifikasi "Waiting for your approval" baru: jumlahnya sama dengan baseline langkah 1
15. Logout lalu login sebagai Group Member Distributor `memberOnDistributor` (Pre-setup #32), lalu buka Notification Center
16. Verifikasi Notification Center `Budi Santoso` tampil
17. Verifikasi pembuat `Budi Santoso` tidak menerima notifikasi "Waiting for your approval" baru: jumlahnya sama dengan baseline langkah 1

### TC-AC-ACHA-405: Approver multi-role menerima satu notifikasi

18. Catat jumlah notifikasi ber-Title "Waiting for your approval" milik `Yusuf Hidayat` lewat fixture baca notifikasi sebagai baseline
19. Kirim Submit alokasi BLE Quantity `20` untuk PT Sejahtera Logistik lewat sesi API `Budi Santoso` hingga transaksi berstatus Waiting for Approval tersimpan, lalu catat Allocation ID
20. Logout lalu login sebagai `multiRoleApprover` (Pre-setup #38), lalu buka Notification Center dan muat ulang tiap 5 detik sampai notifikasi baru tampil (batas tunggu 2 menit)
21. Verifikasi `Yusuf Hidayat` menerima tepat satu notifikasi "Waiting for your approval" baru: jumlahnya bertambah satu terhadap baseline langkah 18 (dedup multi-role: satu notifikasi per orang)

### TC-AC-ACHA-406: Notifikasi Cancel manual ke approver yang sudah dinotifikasi

22. Catat jumlah notifikasi ber-Title "Allocation request has been canceled" milik `Hendra Wibowo`, `Agus Hartono`, dan Default User Distributor lewat fixture baca notifikasi sebagai baseline
23. Kirim Submit alokasi BLE Quantity `20` untuk PT Sejahtera Logistik lewat sesi API `Budi Santoso` hingga transaksi berstatus Waiting for Approval tersimpan
24. Tunggu notifikasi "Waiting for your approval" untuk transaksi itu terbaca lewat fixture baca notifikasi (Precondition d TC-AC-ACHA-406: approver pool sudah dinotifikasi sebelum Cancel)
25. Kirim Cancel (`Cancel Allocation`) untuk transaksi itu lewat sesi API `Budi Santoso` hingga status `Canceled` tersimpan
26. Logout lalu login sebagai Total Control Distributor `totalControlDistributor` (Pre-setup #27), lalu buka Notification Center dan muat ulang tiap 5 detik sampai notifikasi baru ber-Title "Allocation request has been canceled" tampil (batas tunggu 2 menit)
27. Verifikasi Total Control `Hendra Wibowo` menerima satu notifikasi baru dengan Title "Allocation request has been canceled": jumlah notifikasi ber-Title itu bertambah satu terhadap baseline langkah 22
28. Verifikasi notifikasi baru itu berjenis `view-only`
29. Logout lalu login sebagai Group Manager `groupManagerDistributor` (Pre-setup #29), lalu buka Notification Center dan muat ulang tiap 5 detik sampai notifikasi baru tampil (batas tunggu 2 menit)
30. Verifikasi Group Manager Group Jakarta `Agus Hartono` menerima satu notifikasi baru dengan Title "Allocation request has been canceled": jumlah notifikasi ber-Title itu bertambah satu terhadap baseline langkah 22
31. Verifikasi notifikasi baru itu berjenis `view-only`
32. Logout lalu login sebagai Default User Distributor `defaultUserDistributor` (Pre-setup #28), lalu buka Notification Center
33. Verifikasi Notification Center Default User Distributor tampil
34. Verifikasi Default User Distributor yang bukan bagian approver pool tidak menerima notifikasi "Allocation request has been canceled" baru: jumlahnya sama dengan baseline langkah 22

### TC-AC-ACHA-408: Notifikasi Approve ke pembuat

35. Kirim Submit alokasi BLE Quantity `20` untuk PT Sejahtera Logistik lewat sesi API `Budi Santoso` hingga transaksi berstatus Waiting for Approval tersimpan
36. Tunggu notifikasi "Waiting for your approval" untuk transaksi itu terbaca lewat fixture baca notifikasi, lalu catat jumlah seluruh notifikasi milik `Budi Santoso` dan `Hendra Wibowo` sebagai baseline
37. Kirim Approve untuk transaksi itu lewat sesi API `Hendra Wibowo` hingga status `Completed` tersimpan
38. Logout lalu login sebagai Group Member Distributor `memberOnDistributor` (Pre-setup #32), lalu buka Notification Center dan muat ulang tiap 5 detik sampai notifikasi baru tampil (batas tunggu 2 menit)
39. Verifikasi pembuat `Budi Santoso` menerima satu notifikasi baru untuk persetujuan: jumlah seluruh notifikasi bertambah satu terhadap baseline langkah 36 (Title dan Body tidak diasersi karena event Approve tidak ada di `notification.md` §5.1b, PRD §9.7)
40. Verifikasi notifikasi baru itu berjenis `view-only`
41. Klik notifikasi itu
42. Verifikasi klik notifikasi membuka modal Allocation Log untuk transaksi itu
43. Tutup modal Allocation Log dengan `[×]`
44. Logout lalu login sebagai Total Control Distributor `totalControlDistributor` (Pre-setup #27), lalu buka Notification Center
45. Tunggu 5 detik tanpa memuat ulang halaman
46. Verifikasi Notification Center `Hendra Wibowo` memuat sedikitnya satu notifikasi lain (pembanding)
47. Verifikasi approver yang menyetujui tidak menerima notifikasi untuk keputusannya sendiri: jumlah seluruh notifikasi `Hendra Wibowo` sama dengan baseline langkah 36

### TC-AC-ACHA-409: Notifikasi Reject ke pembuat

48. Kirim Submit alokasi BLE Quantity `20` untuk PT Sejahtera Logistik lewat sesi API `Budi Santoso` hingga transaksi berstatus Waiting for Approval tersimpan
49. Catat jumlah notifikasi ber-Title "Your allocation request has been rejected" milik `Budi Santoso` lewat fixture baca notifikasi sebagai baseline
50. Kirim Reject dengan Rejection Reason `Stok belum siap` untuk transaksi itu lewat sesi API `Hendra Wibowo` hingga status `Rejected` tersimpan
51. Buka Notification Center `Budi Santoso` dan muat ulang tiap 5 detik sampai notifikasi baru ber-Title "Your allocation request has been rejected" tampil (batas tunggu 2 menit)
52. Verifikasi pembuat `Budi Santoso` menerima satu notifikasi baru dengan Title "Your allocation request has been rejected": jumlah notifikasi ber-Title itu bertambah satu terhadap baseline langkah 49
53. Verifikasi notifikasi baru itu berjenis `view-only`
54. Klik notifikasi itu
55. Verifikasi klik notifikasi membuka modal Allocation Log untuk transaksi itu
56. Tutup modal Allocation Log dengan `[×]`

### TC-AC-ACHA-411: Notifikasi view-only hanya Read lewat tombol Mark as Read

57. Kirim Submit alokasi BLE Quantity `20` untuk PT Sejahtera Logistik lewat sesi API `Budi Santoso` hingga transaksi berstatus Waiting for Approval tersimpan, lalu Reject dengan Rejection Reason `Stok belum siap` lewat sesi API `Hendra Wibowo` hingga status `Rejected` tersimpan
58. Buka Notification Center `Budi Santoso` dan muat ulang tiap 5 detik sampai notifikasi baru ber-Title "Your allocation request has been rejected" tampil di baris teratas (batas tunggu 2 menit)
59. Klik area judul notifikasi teratas itu
60. Verifikasi klik area item membuka modal Allocation Log untuk transaksi itu
61. Tutup modal Allocation Log dengan `[×]`
62. Kembali ke Notification Center dan baca status notifikasi teratas itu
63. Verifikasi notifikasi tetap Unread
64. Verifikasi tombol `[Mark as Read]` tetap ada pada notifikasi itu
65. Klik tombol `[Mark as Read]` pada notifikasi itu
66. Verifikasi notifikasi berstatus Read

### TC-AC-ACHA-412: Edit tidak mengirim notifikasi

67. Kirim Submit alokasi BLE Quantity `20` untuk PT Sejahtera Logistik lewat sesi API `Budi Santoso` hingga transaksi berstatus Waiting for Approval tersimpan, lalu catat Allocation ID
68. Tunggu notifikasi "Waiting for your approval" untuk transaksi itu terbaca lewat fixture baca notifikasi, lalu catat jumlah seluruh notifikasi milik `Budi Santoso` dan `Hendra Wibowo` sebagai baseline
69. Kirim Edit Quantity menjadi `120` untuk transaksi itu lewat sesi API `Budi Santoso` hingga Quantity `120` tersimpan
70. Tunggu 5 detik tanpa memuat ulang halaman
71. Buka Notification Center `Budi Santoso`
72. Verifikasi Notification Center `Budi Santoso` memuat sedikitnya satu notifikasi lain (pembanding)
73. Verifikasi tidak ada notifikasi baru untuk pembuat akibat Edit: jumlah seluruh notifikasi `Budi Santoso` sama dengan baseline langkah 68
74. Logout lalu login sebagai Total Control Distributor `totalControlDistributor` (Pre-setup #27), lalu buka Notification Center
75. Verifikasi Notification Center `Hendra Wibowo` memuat sedikitnya satu notifikasi lain (pembanding)
76. Verifikasi tidak ada notifikasi baru untuk approver akibat Edit: jumlah seluruh notifikasi `Hendra Wibowo` sama dengan baseline langkah 68

### TC-AC-ACHA-410: Notifikasi actionable hanya Read saat task diselesaikan

77. Kirim Submit alokasi BLE Quantity `20` untuk PT Sejahtera Logistik lewat sesi API `Budi Santoso` hingga transaksi berstatus Waiting for Approval tersimpan
78. Buka Notification Center `Hendra Wibowo` dan muat ulang tiap 5 detik sampai notifikasi `actionable` baru ber-Title "Waiting for your approval" tampil di baris teratas (batas tunggu 2 menit), lalu catat badge count
79. Klik `[Detail]` pada notifikasi teratas itu
80. Tutup halaman Detail tanpa memutuskan (tanpa Approve atau Reject), lalu kembali ke Notification Center
81. Verifikasi notifikasi tetap Unread
82. Verifikasi badge count tidak berkurang dibanding badge count yang dicatat
83. Kirim Approve untuk transaksi itu lewat sesi API `Agus Hartono` (Group Manager Group Jakarta) hingga status `Completed` tersimpan
84. Muat ulang Notification Center `Hendra Wibowo`
85. Verifikasi notifikasi Total Control `Hendra Wibowo` untuk transaksi itu berstatus Read otomatis (task diselesaikan pihak lain)

### TC-AC-ACHA-407: Notifikasi Timeout Auto-Cancel ke pembuat dan approver

86. Batalkan lewat sesi API `Budi Santoso` semua transaksi Waiting for Approval sisa blok TC-AC-ACHA-404, 405, dan 412 (Allocation ID dicatat pada langkah 2, 19, dan 67) hingga status `Canceled` tersimpan, lalu tunggu notifikasi pembatalannya terbaca lewat fixture baca notifikasi
87. Kirim Submit alokasi BLE Quantity `20` untuk PT Sejahtera Logistik lewat sesi API `Budi Santoso` hingga transaksi berstatus Waiting for Approval tersimpan, lalu catat Allocation ID dan T1 lewat fixture
88. Tunggu notifikasi "Waiting for your approval" untuk transaksi itu terbaca lewat fixture baca notifikasi, lalu catat jumlah seluruh notifikasi milik `Budi Santoso` dan `Hendra Wibowo` sebagai baseline
89. Geser jam server ke `T1 + 3 hari + 1 menit` lewat fixture
90. Tunggu satu siklus job pengecekan dengan memuat ulang halaman Allocation > Device Allocation tiap 5 detik sampai status transaksi itu (dicari lewat Search Allocation ID) `Canceled` (batas tunggu 2 menit)
91. Pulihkan jam server ke waktu nyata lewat fixture
92. Logout lalu login sebagai Group Member Distributor `memberOnDistributor` (Pre-setup #32), lalu buka Notification Center dan muat ulang tiap 5 detik sampai notifikasi baru tampil (batas tunggu 2 menit)
93. Verifikasi pembuat `Budi Santoso` menerima satu notifikasi baru untuk pembatalan oleh timeout: jumlah seluruh notifikasi bertambah satu terhadap baseline langkah 88 (Title dan Body tidak diasersi, PRD §9.7)
94. Verifikasi notifikasi baru itu berjenis `view-only`
95. Klik notifikasi itu
96. Verifikasi klik notifikasi membuka modal Allocation Log untuk transaksi itu
97. Tutup modal Allocation Log dengan `[×]`
98. Logout lalu login sebagai Total Control Distributor `totalControlDistributor` (Pre-setup #27), lalu buka Notification Center
99. Verifikasi approver `Hendra Wibowo` yang sudah dinotifikasi menerima satu notifikasi baru untuk pembatalan oleh timeout: jumlah seluruh notifikasi bertambah satu terhadap baseline langkah 88 (Title dan Body tidak diasersi, PRD §9.7)
100. Verifikasi notifikasi baru itu berjenis `view-only`

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (Section 7c). Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan (S-10): TC-AC-ACHA-411 dan 412 ditaruh sebelum TC-AC-ACHA-410 supaya ganti akun minimal dan TC-AC-ACHA-410 menutup bagian UI di akun Hendra Wibowo yang sama dengan akhir TC-AC-ACHA-412; urutan TC-AC-ACHA-408 sebelum 409 mengikuti nomor TC. TC-AC-ACHA-407 ditaruh paling akhir karena geser jam server membatalkan semua transaksi Waiting for Approval yang melewati batas (S-09); sebelum blok itu, transaksi sisa blok 404, 405, dan 412 dibatalkan (langkah 86) supaya pertambahan notifikasi pada baseline langkah 88 hanya berasal dari transaksi blok. Tiap TC memakai transaksi baru sehingga tidak bergantung pada hasil TC lain (S-04).
- Urutan asersi TC-AC-ACHA-408 (S-10): Langkah Uji TC membuka Notification Center pembuat lebih dulu (asersi a dan c), baru approver yang menyetujui (asersi b); notifikasi pembuat yang terbaca (langkah 39) menjadi anchor positif bahwa pengiriman selesai sebelum asersi absence pada langkah 47, yang didahului jendela 5 detik pada langkah 45.
- Pelaku kedua lewat sesi API (R-20): Submit, Cancel, Edit, Approve, dan Reject hanya memicu state; Approve oleh Hendra Wibowo, Reject oleh Hendra Wibowo, dan Approve oleh Agus Hartono tidak diasersi di Approvals. Bukan konteks kedua kelas c, tidak memakai `P-2`. Aksi UI Approve dan Reject di Approvals diuji di spec 034; Expected TC di sini hanya notifikasi.
- P-2 (pemicu bukan objek uji): langkah memajukan jam server pada TC-AC-ACHA-407 hanya memicu Timeout yang memunculkan notifikasi; jam dipulihkan segera sesudah job selesai (S-09).
- Langkah penghubung (S-03): langkah "Catat jumlah ... lewat fixture baca notifikasi" (1, 18, 22, 36, 49, 68, 88) sebagai baseline S-12; langkah ganti akun (S-07) tiap `Logout lalu login ...`; langkah memuat ulang Notification Center (polling 5 detik, batas 2 menit); langkah 24 (tunggu notifikasi `Waiting for your approval` terbaca sebelum Cancel, TC-AC-ACHA-406); langkah 45 dan 70 ("Tunggu 5 detik tanpa memuat ulang halaman" sebelum asersi absence); tutup modal Allocation Log; langkah 86 sampai 91 (pembatalan transaksi sisa, geser dan pulihkan jam, menunggu satu siklus job TC-AC-ACHA-407).
- Baris target (R-16): transaksi di langkah 90 ditemukan lewat Search Allocation ID yang dicatat pada langkah 87.
- Asersi notifikasi (S-01): tiap butir "menerima satu notifikasi" dipecah menjadi `Verifikasi` jumlah (bertambah satu terhadap baseline yang dicatat) dan `Verifikasi` tier (`actionable` atau `view-only`); Title hanya diasersi bila TC menyebutnya.
- Anchor absence: tiap asersi "tidak menerima" didahului `Verifikasi` bahwa Notification Center akun itu tampil atau memuat notifikasi pembanding. Default User Distributor mungkin belum punya notifikasi lain, sehingga anchor berupa tampilnya Notification Center (lihat Temuan untuk QA).
- Notifikasi yang dibuka pada TC-AC-ACHA-411 dan TC-AC-ACHA-410 dikenali sebagai baris teratas karena baru dibuat oleh pemicu dan diurutkan terbaru di atas (S-14: baris dijamin berada di halaman teramati).
- Ukuran spec: 100 langkah (melewati sekitar 35 langkah). Alasan: seluruh blok satu topik (notifikasi in-app per event) dengan penerima berbeda per TC sehingga ganti akun (S-07) dan baca ulang Notification Center menambah langkah tanpa verifikasi; tiap blok memakai transaksi sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-ACHA-404 b menyebut Default User tidak menerima notifikasi, tetapi precondition tidak menyebut data pembanding (notifikasi lain) pada Notification Center Default User; spec memakai tampilnya Notification Center sebagai anchor dan baseline jumlah.
  - TC-AC-ACHA-404 a menyebut "Total Control, Group Manager, dan Additional Approver masing-masing menerima satu notifikasi" tanpa menyebut bahwa Total Control `Yusuf Hidayat` (Pre-setup #38) juga bagian approver pool Group Jakarta; spec tidak mengasersi Yusuf pada TC-AC-ACHA-404.
  - TC-AC-ACHA-406 b dan TC-AC-ACHA-407, 408 tidak menyebut Title notifikasi Timeout dan Approve (PRD §9.7: tidak di-assert); spec hanya mengasersi keberadaan, tier `view-only`, dan tujuan klik.
  - TC-AC-ACHA-407 tidak menyebut precondition "tidak ada transaksi Waiting for Approval lain": geser jam server membatalkan juga transaksi Waiting lain milik pembuat dan approver yang sama, sehingga hitungan "satu notifikasi" hanya benar bila transaksi sisa dibatalkan lebih dulu (langkah 86); transaksi Waiting milik spec lain di akun yang sama tidak dikendalikan spec ini.
  - TC-AC-ACHA-410 langkah 1 tidak menyebut tujuan klik `[Detail]` dan cara "menutup halaman"; spec kembali ke Notification Center sesudah klik.
  - TC-AC-ACHA-410 dan 411 tidak menyebut cara mengidentifikasi notifikasi milik transaksi tertentu (Title tidak memuat Allocation ID); spec memakai baris teratas.
  - Post Condition TC-AC-ACHA-404 sampai 412 ("-") tidak ada.

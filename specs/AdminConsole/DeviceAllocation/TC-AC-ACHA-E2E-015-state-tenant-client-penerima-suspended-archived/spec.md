---
id: TC-AC-ACHA-E2E-015-state-tenant-client-penerima-suspended-archived
title: "State Tenant: Aksi Tulis Ditolak Saat Client Penerima Suspended atau Archived, Timeout Tetap Berjalan, Kuota Tidak Ditarik"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHA-279
  - TC-AC-ACHA-403
  - TC-AC-ACHA-456
  - TC-AC-ACHA-457
  - TC-AC-ACHA-458
  - TC-AC-ACHA-459
  - TC-AC-ACHA-460
  - TC-AC-ACHA-461
coverage:
  web: automated
---

# State Tenant: Aksi Tulis Ditolak Saat Client Penerima Suspended atau Archived, Timeout Tetap Berjalan, Kuota Tidak Ditarik

## Prerequisites

- Mode: FE+BE.
- Akun yang dipakai:

| TC | Akun | Pre-setup | Email | Env var password |
|---|---|---|---|---|
| TC-456, TC-457, TC-460 | Group Member Distributor toggle ON (alias MB_ON, Budi Santoso) | #32 | `memberOnDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_MB_ON_PASSWORD` |
| TC-458, TC-459, TC-461, TC-403, TC-279 | Total Control Distributor PT Global Distribusi (alias TC_DIST) | #27 | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |

- Login akun aktor pertama (MB_ON) di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite. Hook `after` mengembalikan status Client PT Sejahtera Logistik menjadi Active, memulihkan baseline transaksi dan jam server, serta mengembalikan sesi ke akun default suite (Total Control Principal PT ABC, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah logout dan login eksplisit.
- Hook suite: sesi API aktor, flag Guided Tooltip, pemulihan preferensi Setup Column, seed 30 baris idempotent (Lampiran A butir A-6), dan fixture Pre-setup #20 dinyatakan di `suite.md` (endpoint tidak dikarang di spec ini). Suite berjalan serial (`parallel: false`).
- Kelas harness: h (state tenant: status Client penerima). Spec ini kondisi data tersendiri (prinsip 12).
- Nilai literal: `Stok belum siap` (Rejection Reason) adalah nama stok seed yang sah sebagai literal menurut Lampiran A butir A-6.
- Data Pre-setup yang dipakai: Client `PT Sejahtera Logistik` (Pre-setup #7, Active, binaan PT Global Distribusi; diubah menjadi Suspended atau Archived oleh fixture); transaksi Waiting for Approval milik MB_ON (Pre-setup #49: RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Total Cost $250.00, Reserve $250.00 pada kantong PT Global Distribusi, Approval Timeout 3 day(s) per Pre-setup #63); kantong PT Global Distribusi saldo $20,000.00 (Pre-setup #16); Seed 30 alokasi (Pre-setup #48) dengan baris Completed `HALC-20260901-00001` milik PT Sejahtera Logistik (RFID, Quantity 500). Allocation ID Pre-setup #49 dan waktu terbit T1 dibaca lewat fixture seed (disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak dikarang): fixture Pre-setup #20 untuk (a) mengatur status Client PT Sejahtera Logistik menjadi Active, Suspended, atau Archived setelah transaksi #49 dibuat, (b) memulihkan baseline transaksi #49 (Waiting for Approval, Quantity 100) dan kantong PT Global Distribusi (saldo $20,000.00, Reserved $250.00), membaca saldo dan Reserved kantong, dan membaca kuota Client PT Sejahtera Logistik (nilai Client Dashboard), (c) membuka Client Dashboard PT Sejahtera Logistik lewat UI untuk membaca kuota pada langkah 57 (dibandingkan dengan baseline kuota yang dicatat lewat fixture pada langkah 2), dan menggeser dan memulihkan jam server. Browser uji menangani dialog `beforeunload` secara otomatis pada muat ulang halaman (S-08). Penunggu job memakai idiom polling worker commit (muat ulang tiap 5 detik, batas 2 menit).
- Jam: hanya jam server yang digeser (Approval Timeout 3 hari dihitung murni di server); jam server diset absolut ke T1 + 3 hari + 1 menit (T1 dibaca dari fixture seed) dan dipulihkan segera sesudah status Canceled terbaca dan di hook `after`.
- Kemampuan teknis (jam): sesi UI dan sesi API tetap valid selama jam server digeser (dinyatakan di `suite.md`).
- General Settings Pre-setup #1 tidak diubah.
- State global: status Client PT Sejahtera Logistik, jam server, baseline transaksi #49, dan saldo kantong diubah dan dipulihkan; suite berjalan serial.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DA_MB_ON_PASSWORD` dan `AC_DA_TC_DIST_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.

## Test Steps

### Persiapan Client Suspended

1. Pulihkan baseline lewat fixture Pre-setup #20: status Client PT Sejahtera Logistik Active, transaksi #49 Waiting for Approval (Quantity 100), kantong PT Global Distribusi saldo $20,000.00 dan Reserved $250.00
2. Catat kuota Client PT Sejahtera Logistik (nilai Client Dashboard) lewat fixture sebagai baseline kuota
3. Atur status Client PT Sejahtera Logistik menjadi Suspended lewat fixture Pre-setup #20

### TC-AC-ACHA-456: Edit ditolak saat Client penerima Suspended

4. Ketik Search `Allocation ID` transaksi #49, tekan Enter
5. Klik `[⋯]` pada baris hasil
6. Klik `Edit`
7. Ubah Quantity dari `100` menjadi `120`
8. Klik `[Save]`
9. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
10. Muat ulang halaman Allocation > Device Allocation (F5)
11. Ganti isi kotak search dengan `Allocation ID` transaksi #49, tekan Enter
12. Verifikasi baris transaksi #49 berstatus `Waiting for Approval`
13. Verifikasi Quantity baris transaksi #49 tetap `100`
14. Verifikasi Reserved kantong PT Global Distribusi tetap $250.00 (dibaca lewat fixture)
15. Klik `(←)` pada kotak Search

### TC-AC-ACHA-457: Cancel ditolak saat Client penerima Suspended

16. Ketik Search `Allocation ID` transaksi #49, tekan Enter
17. Klik `[⋯]` pada baris hasil
18. Klik `Cancel Allocation`
19. Klik `[Cancel Allocation]` pada dialog
20. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
21. Muat ulang halaman Allocation > Device Allocation (F5)
22. Ganti isi kotak search dengan `Allocation ID` transaksi #49, tekan Enter
23. Verifikasi baris transaksi #49 berstatus `Waiting for Approval`
24. Verifikasi Reserved kantong PT Global Distribusi tetap $250.00 (dibaca lewat fixture)
25. Klik `(←)` pada kotak Search

### Ganti akun ke Total Control Distributor

26. Logout dari akun MB_ON
27. Login sebagai TC_DIST (`totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_DIST_PASSWORD`)
28. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-458: Approve ditolak saat Client penerima Suspended

29. Buka Approvals > Device Allocation lewat sidebar
30. Buka transaksi #49
31. Klik `[Approve]`
32. Konfirmasi Approve pada dialog
33. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
34. Buka Allocation > Device Allocation lewat sidebar
35. Ketik Search `Allocation ID` transaksi #49, tekan Enter
36. Verifikasi status tetap `Waiting for Approval`
37. Verifikasi Reserved kantong PT Global Distribusi tetap $250.00 (dibaca lewat fixture)
38. Verifikasi tidak ada Capture pada kantong PT Global Distribusi: saldo tetap $20,000.00 (dibaca lewat fixture)
39. Klik `(←)` pada kotak Search

### TC-AC-ACHA-459: Reject ditolak saat Client penerima Suspended

40. Buka Approvals > Device Allocation lewat sidebar
41. Tunggu toast error sebelumnya hilang
42. Buka transaksi #49
43. Isi Rejection Reason `Stok belum siap`
44. Klik `[Reject]`
45. Konfirmasi Reject pada dialog
46. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
47. Buka Allocation > Device Allocation lewat sidebar
48. Ketik Search `Allocation ID` transaksi #49, tekan Enter
49. Verifikasi status tetap `Waiting for Approval`
50. Verifikasi Reserved kantong PT Global Distribusi tetap $250.00 (tidak ada Release, dibaca lewat fixture)
51. Klik `(←)` pada kotak Search

### TC-AC-ACHA-403: Kuota Completed tidak ditarik saat Client di-Suspend

52. Muat ulang halaman Allocation > Device Allocation (F5)
53. Ketik Search `Allocation ID` transaksi Completed `HALC-20260901-00001` milik PT Sejahtera Logistik, tekan Enter
54. Verifikasi baris `HALC-20260901-00001` tetap berstatus `Completed`
55. Klik `(←)` pada kotak Search
56. Buka Client Dashboard PT Sejahtera Logistik
57. Verifikasi kuota pada Client Dashboard sama dengan baseline kuota (tidak berkurang)
58. Buka Allocation > Device Allocation lewat sidebar
59. Verifikasi panel `Allocated quota` menampilkan RFID 500 | NFC 1 | BLE 80 | GPS 9 | Handheld Reader 8 | Smart Fixed Reader 3 | BLE Gateway 65 (tidak berkurang)

### TC-AC-ACHA-279: Timeout Auto-Cancel berjalan walau Client penerima Suspended

60. Catat T1 (waktu terbit transaksi #49) dari fixture seed
61. Ketik Search `Allocation ID` transaksi #49, tekan Enter
62. Verifikasi baris transaksi #49 berstatus `Waiting for Approval`
63. Geser jam server ke T1 + 3 hari + 1 menit lewat fixture Pre-setup #20
64. Ulangi tiap 5 detik: muat ulang halaman, ganti isi kotak search dengan `Allocation ID` transaksi #49, tekan Enter, sampai baris transaksi #49 berstatus `Canceled` (batas tunggu 2 menit)
65. Pulihkan jam server ke waktu nyata lewat fixture Pre-setup #20
66. Verifikasi baris transaksi #49 berstatus `Canceled` (Timeout Auto-Cancel tetap berjalan walau Client Suspended)
67. Verifikasi Reserved kantong PT Global Distribusi $0.00 (dibaca lewat fixture)
68. Klik `(←)` pada kotak Search

### Persiapan Client Archived

69. Pulihkan baseline lewat fixture Pre-setup #20: status Client PT Sejahtera Logistik Active, transaksi #49 Waiting for Approval (Quantity 100), kantong PT Global Distribusi saldo $20,000.00 dan Reserved $250.00
70. Atur status Client PT Sejahtera Logistik menjadi Archived lewat fixture Pre-setup #20
71. Muat ulang halaman Allocation > Device Allocation (F5)

### TC-AC-ACHA-461: Approve ditolak saat Client penerima Archived

72. Buka Approvals > Device Allocation lewat sidebar
73. Buka transaksi #49
74. Klik `[Approve]`
75. Konfirmasi Approve pada dialog
76. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
77. Buka Allocation > Device Allocation lewat sidebar
78. Ketik Search `Allocation ID` transaksi #49, tekan Enter
79. Verifikasi status tetap `Waiting for Approval`
80. Verifikasi Reserved kantong PT Global Distribusi tetap $250.00 (dibaca lewat fixture)
81. Verifikasi tidak ada Capture pada kantong PT Global Distribusi: saldo tetap $20,000.00 (dibaca lewat fixture)
82. Klik `(←)` pada kotak Search

### Ganti akun ke Group Member Distributor

83. Logout dari akun TC_DIST
84. Login sebagai MB_ON (`memberOnDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_MB_ON_PASSWORD`)
85. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-460: Edit ditolak saat Client penerima Archived

86. Ketik Search `Allocation ID` transaksi #49, tekan Enter
87. Klik `[⋯]` pada baris hasil
88. Klik `Edit`
89. Ubah Quantity dari `100` menjadi `120`
90. Klik `[Save]`
91. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired."
92. Muat ulang halaman Allocation > Device Allocation (F5)
93. Ganti isi kotak search dengan `Allocation ID` transaksi #49, tekan Enter
94. Verifikasi baris transaksi #49 berstatus `Waiting for Approval`
95. Verifikasi Quantity baris transaksi #49 tetap `100`
96. Verifikasi Reserved kantong PT Global Distribusi tetap $250.00 (dibaca lewat fixture)
97. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Spec kelas h (state tenant): write-lockdown akibat status Client penerima Suspended atau Archived; Timeout Auto-Cancel tetap berjalan; kuota yang sudah diterima tidak ditarik. Serial; fixture status Client.
- Urutan TC di spec: TC-456, 457, 458, 459, 403, 279 (blok Suspended), lalu 461, 460 (blok Archived) (penyimpangan dari urutan nomor, S-05). Alasan: TC-279 membatalkan transaksi #49 lewat Timeout sehingga ditaruh paling akhir pada blok Suspended dengan baseline dipulihkan sesudahnya (prinsip 5); blok geser jam TC-279 tidak berada di akhir spec (S-10) dan efeknya pada transaksi lain dinetralkan oleh pemulihan baseline dan status Client pada langkah persiapan Client Archived; TC-403 membutuhkan Client Suspended; aksi dikelompokkan per akun agar ganti akun minimal.
- P-2 (pemicu bukan objek uji, `[KEPUTUSAN 2026-10-21]`): job latar Timeout dan jam server yang digeser pada TC-279 hanya memicu kondisi yang diamati lewat List dan fixture; Approve oleh UI Approvals (TC-458, TC-459, TC-461) adalah objek uji penolakan.
- Langkah penghubung (S-03, R-12): langkah "Tunggu toast error sebelumnya hilang" sebelum `[Reject]` (toast error identik dengan toast Approve sebelumnya), langkah persiapan (pemulihan baseline dan status Client lewat fixture), langkah ganti akun, `(←)` yang mereset Search, buka halaman via sidebar, muat ulang halaman, pencarian transaksi target, pencatatan T1 dan baseline kuota, serta pemulihan jam server. Aksi yang ditolak server tidak dinyatakan TC meninggalkan form atau dialog dalam keadaan apa; setelah toast spec memuat ulang halaman (dialog `beforeunload` ditangani otomatis, S-08) lalu mengamati state dari List dan fixture.
- Aksi Approve dan Reject dipecah per kontrol (S-01, S-03): buka transaksi #49, klik `[Approve]` atau isi Rejection Reason lalu klik `[Reject]`, lalu konfirmasi pada dialog sebagai langkah terpisah.
- Ukuran spec (di atas sekitar 35 langkah): satu kelas harness (h), satu dataset (transaksi #49 pada entitas PT Global Distribusi dan Client PT Sejahtera Logistik), tiap Expected menjadi `Verifikasi` sendiri (S-01), dan dua ganti akun eksplisit. Bagian sesudah ganti akun tetap bermakna karena baseline dipulihkan sebelum tiap blok (bagian 3, pemisah (b)).
- Pembagian TC lintas spec: write-lockdown akibat status entitas aktor (TC-80 sampai 88, 278, 480 sampai 484) ada di spec 014; dampak lintas modul perubahan status Client lain (TC-399 sampai 402) ada di spec 051.
- Temuan untuk QA:
  - TC-279 Precondition a menyebut login sebagai MB_ON sedangkan Langkah Uji hanya "muat ulang List"; spec memakai TC_DIST sebagai aktor pengamat yang berada di sesi pada saat itu.
  - TC-403 Dependensi menunjuk TC-401 (spec 051) sebagai pembuat kondisi; spec ini mengatur Client Suspended sendiri lewat fixture. Nilai kuota Client Dashboard tidak disebut TC; dibaca lewat fixture sebagai baseline (disediakan tim FE/BE) dan diasersi sama setelah Suspend.
  - TC-403 Expected b menyebut kuota "tidak berkurang" pada panel Stock Balance Summary tanpa nilai; spec memakai nilai panel PT Global Distribusi dari TC-21 (RFID 500, NFC 1, BLE 80, GPS 9, Handheld Reader 8, Smart Fixed Reader 3, BLE Gateway 65).
  - TC-456 sampai TC-461 tidak menyatakan keadaan form atau dialog sesudah toast penolakan; spec tidak mengasersinya dan memuat ulang halaman.
  - TC-458, TC-459, TC-461 menulis klik `[Approve]` atau `[Reject]` di Approvals tanpa menyebut cara membuka transaksi; Page Object Approvals menentukan (modul Approvals).
  - TC-458 dan TC-461 Expected "tidak ada Capture": diasersi lewat saldo kantong tetap $20,000.00 (dibaca lewat fixture); TC tidak menyebut kontrol UI untuk Capture.
  - TC-279 Post Condition (Wallet Release, Approvals Active Tab, Dashboard, notifikasi in-app) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-279 dapat dibaca sebagai kelas d (background job sebagai objek uji); spec ini menempatkannya di kelas h berdasarkan `[KEPUTUSAN 2026-10-21]`; penempatan ini perlu dikonfirmasi.

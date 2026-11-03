---
id: TC-AC-ACHS-E2E-274-event-log-screening-isi-detail-snapshot-dan-scope
title: "Event Log: Screening, Isi, Detail, Snapshot, dan Scope"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-514
  - TC-AC-ACHS-515
  - TC-AC-ACHS-516
  - TC-AC-ACHS-517
  - TC-AC-ACHS-518
  - TC-AC-ACHS-520
  - TC-AC-ACHS-521
  - TC-AC-ACHS-523
  - TC-AC-ACHS-524
  - TC-AC-ACHS-525
  - TC-AC-ACHS-586
  - TC-AC-ACHS-587
coverage:
  web: automated
---

# Event Log: Screening, Isi, Detail, Snapshot, dan Scope

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; penahanan respons lewat intercept parsial di atas backend nyata).
- Akun aktor pertama: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Akun kedua (TC-523): Distributor Manage hardware stock `Fixture.hardwareStock.account.p10.distributorCakra.fullName` (entitas `Fixture.hardwareStock.p10.entityName`), Local Registration aktif, `Fixture.hardwareStock.account.p10.distributorCakra.email` (Pre-setup #10, `Spectra.env.AC_DISTRIBUTOR_CAKRA_PASSWORD`, nama ditetapkan tim FE). Ganti akun memakai Step eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag halaman Stock List disetel hook `before` dan dipulihkan hook `after` spec ini (juga untuk Distributor di langkah ganti akun; kemampuan disediakan tim FE/BE; lihat suite.md). Hook suite: seeding Population Stock Pre-setup #16 sampai #20; suite serial `parallel: false` (lihat suite.md).
- Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal Pre-setup di langkah, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat. Dipakai: SKU `Fixture.hardwareStock.p16.a[4].sku` dengan 12 sesi Event Log (Pre-setup #20, Tabel B) termasuk sesi `Add Stock` `Fixture.hardwareStock.p20.b[2].date` (Success 15, Waiting for Approval 1, Modified By `Fixture.hardwareStock.account.p11.distributorMitra.shortName`), sesi `Add Stock` `Fixture.hardwareStock.p20.b[4].date` (Success 13, Waiting for Approval 2, Modified By `Fixture.hardwareStock.account.p01.totalControl.shortName`), sesi `Delete Stock` `Fixture.hardwareStock.p20.b[1].date` (Success 1, Waiting for Approval `—`, Modified By `Fixture.hardwareStock.account.p01.totalControl.shortName`), dan satu sesi tanpa unit tercatat (Pre-setup #20b); SKU `Fixture.hardwareStock.p16.a[6].sku` tanpa sesi Event Log.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture |
|---|---|---|---|
| `abbrDistA` | #10 | Singkatan `[Nama Depan] [Inisial]` user akun #10 (format Modified By dan Registered By, R-14) | `Fixture.hardwareStock.account.p10.distributorCakra.shortName` |
| `fullDistB` | #11 | Nama lengkap user akun #11 (tampil pada hover pelaku) | `Fixture.hardwareStock.account.p11.distributorMitra.fullName` |
| `abbrDistB` | #11 | Singkatan `[Nama Depan] [Inisial]` user akun #11 | `Fixture.hardwareStock.account.p11.distributorMitra.shortName` |
| `dnHh (4)` | #16 (Tabel A) | Device Name SKU Handheld Reader (sama untuk `skuLong`, `skuShort`, `skuEda`) | `Fixture.hardwareStock.p16.a[4].deviceName` |
| `skuLong` | #16, #17, #18 (Tabel A baris ke-4) | SKU Handheld Reader Range Type Long Range, Total Registered 25 (18 Available, 7 In Use) ditambah 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `skuIx4` | #16 (Tabel A baris ke-6) | SKU Smart Fixed Reader tanpa unit (Total Registered 0, Last Updated `—`) | `Fixture.hardwareStock.p16.a[6].sku` |
| `snMatch524` | milik spec | unit Available pada SKU Bulk IX6 (Pre-setup #16, Tabel A baris ke-8) yang cocok pada Sync TC-524 (bypass E2a) | `SN-MATCH524-{runId}-274` |
| `nEventLog` | #20 | jumlah sesi Event Log SKU `skuLong` yang dibaca hook `before` lewat kemampuan baca sebelum aksi pertama (baseline, S-12; Pre-setup #20 menyediakan 12 sesi, spec lain dapat menambahkan sesi) | dibaca saat run |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName`, `Fixture.hardwareStock.account.p01.totalControl.shortName` |
| `akun distributorCakra` | #10 | Akun Distributor PT Cakra Distribusi (Manage hardware stock) | `Fixture.hardwareStock.account.p10.distributorCakra.email`, `Fixture.hardwareStock.account.p10.distributorCakra.fullName` |
| `sesiAddA` | #20 (Tabel B baris ke-2) | Sesi Event Log `Add Stock` Success 15, Waiting for Approval 1, Modified By user akun #11; identitas sesi = Date | `Fixture.hardwareStock.p20.b[2].date` |
| `sesiAddB` | #20 (Tabel B baris ke-4) | Sesi Event Log `Add Stock` Success 13, Waiting for Approval 2, Modified By akun #1; identitas sesi = Date | `Fixture.hardwareStock.p20.b[4].date` |
| `sesiDel` | #20 (Tabel B baris ke-1) | Sesi Event Log `Delete Stock` Success 1, Waiting for Approval `—`, Modified By akun #1; identitas sesi = Date | `Fixture.hardwareStock.p20.b[1].date` |
| `sesiNoUnit` | #20b | Sesi Event Log tanpa unit tercatat; identitas sesi = Date; kunci fixture belum terdaftar (dibuat tim FE/BE dari Pre-setup #20b) | `Fixture.hardwareStock.p20b.sessionNoUnit` |

- Data milik spec (S-06, S-12; suffix `{runId}-274`): unit Available `SN-MATCH524-{runId}-274` pada SKU Bulk IX6 di-seed hook `before` lewat sesi API aktor (kemampuan seed disediakan tim FE/BE; endpoint tidak disebut TC, PRD, atau LLD). Data Dinamis yang dibuat langkah: `SN-ZEBRA-RFD40-{runId}-274` (unit OK TC-524). Hook `after` menghapus semua data bersuffix `-274` yang masih ada (idempotent, juga bila spec gagal di tengah). Satu sesi `Add Stock` baru dibuat TC-524 (audit trail permanen, tidak dihapus).
- State global yang diubah (pengecualian S-06 `[KEPUTUSAN 2026-10-30]`): Device Name `Fixture.hardwareStock.p16.a[4].deviceName` di-rename menjadi `Fixture.hardwareStock.p16.a[4].deviceName R274` pada TC-518 lewat sesi API aktor (Settings > Device > Name, kemampuan disediakan tim BE/FE). Data ini tidak dapat dimiliki spec karena terikat pada sesi Event Log Pre-setup #20 (audit trail permanen) yang diamati snapshot-nya. Pemulihan ke `Fixture.hardwareStock.p16.a[4].deviceName` dijamin fixture backend yang disediakan tim FE/BE (dinyatakan di `suite.md` pada butir fixture pemulihan Pre-setup (1)), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung (langkah 81); suite berjalan serial; efeknya (Last Updated SKU dan entri audit trail rename) tidak dipulihkan.
- Kemampuan teknis (disediakan tim FE): intercept dan penahanan respons HTTP daftar Event Log dan detail sesi selama 3 detik (nilai dari Data Uji TC-586 dan TC-587) lalu melepasnya; simulator reader USB Handheld Reader (service driver mock, Pre-setup #25) hanya sebagai pemicu Add Stock Sync pada TC-524.
- Waktu: format tanggal dan jam mengikuti General Settings Pre-setup #15; tidak ada pergeseran jam.

## Test Steps

### TC-AC-ACHS-520: Popup Event Log genuinely empty

1. Ketik Search `Fixture.hardwareStock.p16.a[6].sku`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[6].sku`
3. Klik icon `[Event Log]`
4. Verifikasi empty state: ilustrasi (empty box) dengan Title `No event log yet` dan Description `Add Stock and Delete Stock sessions for this SKU will appear here.`
5. Tutup popup lewat `[X]`

### TC-AC-ACHS-525: Tooltip icon Event Log

6. Klik segmen breadcrumb `Stock`
7. Ganti isi kotak search dengan `Fixture.hardwareStock.p16.a[4].sku`, tekan Enter
8. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
9. Klik Tab `Available`
10. Hover icon `[Event Log]`
11. Verifikasi tooltip `Event Log` tampil saat hover
12. Fokuskan icon `[Event Log]` dengan keyboard (Tab)
13. Verifikasi tooltip `Event Log` tampil saat fokus keyboard
14. Klik icon `[Event Log]`
15. Verifikasi popup berjudul `Event Log` terbuka

### TC-AC-ACHS-514: Screening popup Event Log

16. Verifikasi Header: Title `Event Log` dan tombol close `[X]`
17. Verifikasi Header: Table Tools `Search`, `Filter`, `Download`
18. Verifikasi Header: placeholder Search `Search by activity or modified by...`
19. Verifikasi Body: kolom `Date` (sortable), `Activity` (sortable), `Success` (sortable), `Waiting for Approval` (sortable), `Modified By` (sortable), dan Column Visibility `(⋯)` (unsortable)
20. Verifikasi Body: tiap baris memuat row action `Detail` (ikon FileInfoLine)
21. Verifikasi Body: default sort Date Newest First
22. Verifikasi Footer: pagination default 10 baris per halaman
23. Verifikasi Footer: info `Showing 1–10 of {nEventLog} entries` dengan `{nEventLog}` jumlah sesi baseline hook `before` (bukan angka absolut, S-12)

### TC-AC-ACHS-515: Isi sel Event Log

24. Verifikasi Activity tampil teks biasa `Add Stock` atau `Delete Stock` (bukan badge)
25. Pindah halaman Event Log lewat `Next` sampai baris sesi `Fixture.hardwareStock.p20.b[1].date` dan `Fixture.hardwareStock.p20.b[2].date` teramati
26. Verifikasi baris `Add Stock` `Fixture.hardwareStock.p20.b[2].date`: Success `15` dan Waiting for Approval `1`
27. Verifikasi baris `Delete Stock` `Fixture.hardwareStock.p20.b[1].date`: Success `1` dan Waiting for Approval `—`
28. Verifikasi Modified By `Fixture.hardwareStock.account.p11.distributorMitra.shortName` pada baris `Add Stock` `Fixture.hardwareStock.p20.b[2].date`
29. Hover nilai Modified By `Fixture.hardwareStock.account.p11.distributorMitra.shortName`
30. Verifikasi hover menampilkan `Fixture.hardwareStock.account.p11.distributorMitra.fullName`

### TC-AC-ACHS-516: Popup Detail sesi Add Stock

31. Pindah halaman Event Log lewat `Next` atau `Prev` sampai baris sesi `Fixture.hardwareStock.p20.b[4].date` teramati
32. Klik `Detail` pada sesi `Add Stock` yang memuat unit Waiting for Approval (`Fixture.hardwareStock.p20.b[4].date`)
33. Verifikasi Title popup `Add Stock Detail`
34. Verifikasi section `Added` dan `Waiting for Approval` masing-masing berisi tabel read-only kolom `Device Name` dan `Serial Number`
35. Verifikasi urutan awal Serial Number A–Z di dalam tiap section
36. Verifikasi tanpa Search, Filter, Sort, Setup Column, maupun paginasi
37. Scroll isi popup
38. Verifikasi scroll internal dengan header tetap
39. Tutup popup Detail

### TC-AC-ACHS-587: Loading popup Detail

40. Pindah halaman Event Log lewat `Next` atau `Prev` sampai baris sesi `Fixture.hardwareStock.p20.b[4].date` teramati
41. Pasang penahanan respons detail sesi selama 3 detik
42. Klik `Detail` pada sesi `Add Stock` (`Fixture.hardwareStock.p20.b[4].date`)
43. Verifikasi isi popup Detail menampilkan Loading component sampai data tiba
44. Lepas penahanan respons
45. Verifikasi popup `Add Stock Detail` menampilkan section `Added` dengan 13 baris
46. Verifikasi section `Waiting for Approval` dengan 2 baris
47. Tutup popup Detail

### TC-AC-ACHS-517: Popup Detail sesi Delete Stock

48. Pindah halaman Event Log lewat `Next` atau `Prev` sampai baris sesi `Fixture.hardwareStock.p20.b[1].date` teramati
49. Klik `Detail` pada sesi `Delete Stock` (`Fixture.hardwareStock.p20.b[1].date`)
50. Verifikasi Title popup `Delete Stock Detail`
51. Verifikasi section `Deleted` berisi satu baris Device Name dan Serial Number snapshot saat sesi
52. Verifikasi section tanpa baris (`Added` dan `Waiting for Approval`) tidak ditampilkan dan judulnya ikut disembunyikan
53. Tutup popup Detail

### TC-AC-ACHS-521: Popup Detail tanpa unit

54. Pindah halaman Event Log lewat `Next` atau `Prev` sampai baris sesi `Fixture.hardwareStock.p20b.sessionNoUnit` teramati
55. Klik `Detail` pada sesi tanpa unit tercatat (`Fixture.hardwareStock.p20b.sessionNoUnit`)
56. Verifikasi empty state: ilustrasi (empty box) dengan Title `No details to show` dan Description `There are no units recorded for this session.`
57. Tutup popup Detail dan popup Event Log

### TC-AC-ACHS-586: Loading popup Event Log

58. Pasang penahanan respons daftar Event Log selama 3 detik
59. Klik icon `[Event Log]`
60. Verifikasi popup `Event Log` terbuka dan area tabelnya menampilkan Loading component sampai data tiba
61. Lepas penahanan respons
62. Verifikasi tabel menampilkan 10 baris
63. Verifikasi footer `Showing 1–10 of {nEventLog} entries` dengan `{nEventLog}` jumlah sesi baseline hook `before` (bukan angka absolut, S-12)
64. Tutup popup Event Log

### TC-AC-ACHS-518: Snapshot sesi

65. Klik icon `[Event Log]`
66. Pindah halaman Event Log lewat `Next` sampai baris sesi `Fixture.hardwareStock.p20.b[4].date` teramati
67. Klik `Detail` pada sesi `Add Stock` (`Fixture.hardwareStock.p20.b[4].date`)
68. Catat Device Name dan Serial Number pada Popup Detail
69. Tutup popup Detail dan popup Event Log
70. Rename Device Name `Fixture.hardwareStock.p16.a[4].deviceName` menjadi `Fixture.hardwareStock.p16.a[4].deviceName R274` di Settings > Device > Name lewat sesi API hingga perubahan tersimpan; tunggu aksi selesai
71. Klik icon `[Event Log]`
72. Pindah halaman Event Log lewat `Next` sampai baris sesi `Fixture.hardwareStock.p20.b[4].date` teramati
73. Klik `Detail` pada sesi `Add Stock` yang sama
74. Verifikasi Popup Detail tetap menampilkan Device Name dan Serial Number saat sesi (snapshot) sesuai langkah 68, bukan nilai terbaru
75. Tutup popup Detail dan popup Event Log
76. Muat ulang halaman (F5)
77. Verifikasi unit pada Tab Available menampilkan Device Name terbaru `Fixture.hardwareStock.p16.a[4].deviceName R274` (live)
78. Klik segmen breadcrumb `Stock`
79. Ganti isi kotak search dengan `Fixture.hardwareStock.p16.a[4].sku`, tekan Enter
80. Verifikasi Stock List baris SKU `Fixture.hardwareStock.p16.a[4].sku` menampilkan Device Name terbaru `Fixture.hardwareStock.p16.a[4].deviceName R274` (live)
81. Pulihkan Device Name `Fixture.hardwareStock.p16.a[4].deviceName R274` menjadi `Fixture.hardwareStock.p16.a[4].deviceName` lewat sesi API hingga perubahan tersimpan; tunggu aksi selesai

### TC-AC-ACHS-524: Success menghitung unit bypass E2a

82. Ganti isi kotak search dengan `Fixture.hardwareStock.p16.a[4].sku`, tekan Enter
83. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
84. Klik icon `[Event Log]`, catat sesi teratas, lalu tutup popup
85. Klik `[Add Stock]` pada toolbar Tab Available
86. Sync `SN-ZEBRA-RFD40-{runId}-274` (unit OK) dan `{snMatch524}` (unit match, bypass E2a) lewat simulator reader USB
87. Klik `[Submit]`, lalu klik `[Continue]`
88. Tunggu aksi selesai dan kembali ke Stock Detail SKU `Fixture.hardwareStock.p16.a[4].sku` Tab Available
89. Klik icon `[Event Log]`
90. Verifikasi footer popup `Showing 1–10 of N entries` dengan N = `{nEventLog}` + 1 (satu sesi baru, selisih terhadap baseline, S-12)
91. Verifikasi sesi baru `Add Stock` tercatat di atas sesi yang dicatat pada langkah 84 dengan Success `2` (unit OK dan unit bypass E2a)
92. Verifikasi sesi baru itu memiliki Waiting for Approval `0`
93. Tutup popup Event Log
94. Logout, lalu login sebagai Distributor `Fixture.hardwareStock.account.p10.distributorCakra.fullName`; tunggu aksi selesai

### TC-AC-ACHS-523: Scope Distributor

95. Buka Hardware > Stock
96. Ketik Search `Fixture.hardwareStock.p16.a[4].sku`, tekan Enter
97. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
98. Klik icon `[Event Log]`
99. Verifikasi sedikitnya satu sesi tampil di popup Event Log (pembanding)
100. Verifikasi seluruh baris memiliki Modified By `Fixture.hardwareStock.account.p10.distributorCakra.shortName`
101. Verifikasi sesi `Fixture.hardwareStock.account.p11.distributorMitra.shortName` dan `Fixture.hardwareStock.account.p01.totalControl.shortName` tidak tampil

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-514, 515, 516, 517, 518, 520, 521, 523, 524, 525, 586, 587). Tidak ada TC hanya-BE di spec ini.
- Urutan menyimpang dari TC (alasan): TC-520 di awal (SKU berbeda, tanpa state); TC-525 sebelum TC-514 (membuka popup lewat icon yang diuji tooltip-nya); TC-587 sesudah TC-516 memakai sesi yang sama; TC-518 dan TC-524 (mengubah state) di akhir dan TC-523 paling akhir karena ganti akun (bagian 3, ganti akun eksplisit).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 2, 5, 6, 9, 14, 39, 47, 53, 57, 64, 69, 75, 78, 83, 84, 93, 95, 98 (navigasi, membuka dan menutup popup; langkah 37 menggulir popup Detail), 29 (hover), 41, 44, 58, 61 (menahan dan melepas respons, S-09), 65, 68, 71, 76, 85 sampai 89 (aksi alur TC), 70 dan 81 (pelaku kedua lewat sesi API, "Tunggu aksi selesai", R-20), 88 dan 94 (tunggu aksi selesai dan ganti akun), 1, 7, 79, 82, 96 (Search baris SKU sebelum asersi baris SKU atau row action `Detail`, R-16 dan 8b.13; langkah 79 mengganti isi kotak search sebelum Verifikasi Stock List langkah 80 karena Stock List dibuka lewat breadcrumb dan kotak search masih berisi nilai sebelumnya, state Search bertahan, 8b.9), 25, 31, 40, 48, 54, 66, 72 (pindah halaman Event Log, lihat butir cara baca di bawah).
- Cara baca baris sesi Event Log (S-14): baris sesi seed dikenali lewat kolom Date `Fixture.hardwareStock.p20.b[n].date` dan `Fixture.hardwareStock.p20b.sessionNoUnit` yang tertulis di Prerequisites. Popup menampilkan 10 baris per halaman pada sort default Date terbaru lebih dulu, dan Event Log adalah audit trail permanen yang ditambah spec lain (juga spec ini pada TC-524), sehingga baris seed dapat berada di halaman berikutnya. Karena itu langkah 25, 31, 40, 48, 54, 66, dan 72 memindahkan halaman lewat `Next` atau `Prev` sampai baris sesi yang disebut langkah sesudahnya teramati, sebelum baris itu diasersi atau dibuka lewat `Detail`.
- Spec ini 101 langkah, lebih dari 35 langkah. Alasan: seluruh blok membaca surface popup Event Log satu SKU dengan dataset Pre-setup #20 yang sama dan masing-masing berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Asersi tambahan yang tidak ada di TC (S-03, S-12): langkah 90 (`Verifikasi` footer `{nEventLog}` + 1) membuktikan selisih satu sesi terhadap baseline hook `before` sebelum sesi baru TC-524 dibaca pada baris teratas (langkah 91); suite serial dan hanya spec ini yang menulis Event Log SKU `Fixture.hardwareStock.p16.a[4].sku` pada blok ini.
- Penahanan respons pada TC-586 dan TC-587 hanya mengamati state Loading (bukan kelas b). Simulator USB (kelas d) pada TC-524 dan rename Device Name pada TC-518 hanya pemicu state; pelaku kedua lewat sesi API bukan konteks kedua.
- `P-11`: TC-524 memakai simulator reader USB hanya untuk memicu Add Stock Sync (satu Sync OK dan satu unit match); USB (driver, Sync) bukan objek asersi dan kemampuan simulator dinyatakan di Prerequisites.
- Pasangan kolom Header, Body, dan Footer pada TC-514 ditulis satu `Verifikasi` per klausa kecuali daftar kolom dan daftar ikon Table Tools yang disebut utuh dalam satu butir Expected TC (S-01).
- Temuan untuk QA:
  - TC-524 tidak menyebut Serial Number unit match; spec memakai unit milik spec `{snMatch524}` sebagai unit yang cocok. Sesi baru tercatat di atas sesi yang dicatat, bukan pada posisi absolut (audit trail permanen, S-12, S-14).
  - TC-518 menyebut nama baru tanpa nilai; spec memakai `Fixture.hardwareStock.p16.a[4].deviceName R274`.
  - TC-514 dan TC-586 menyebut total `12 entries` (absolut); spec memakai baseline `{nEventLog}` yang dibaca sebelum aksi karena Event Log audit trail permanen (S-12).
  - Seed unit milik spec `{snMatch524}` dan pembersihan data bersuffix `-274` di `after` disediakan tim FE/BE; mekanismenya tidak didefinisikan di TC, PRD, atau LLD.
  - TC-523 menyebut Modified By `Fixture.hardwareStock.account.p10.distributorCakra.shortName` untuk Distributor; asersi memakai nilai dari Pre-setup #20 (Tabel B).

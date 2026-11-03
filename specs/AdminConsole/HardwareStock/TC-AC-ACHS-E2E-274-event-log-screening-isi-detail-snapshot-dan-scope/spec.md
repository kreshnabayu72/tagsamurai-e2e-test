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
- Hook suite: flag Guided Tooltip halaman Stock List diatur hook suite `before` dan dipulihkan `after` (juga untuk Distributor di langkah ganti akun); seeding Population Stock Pre-setup #16 sampai #20; suite serial `parallel: false` (lihat suite.md).
- Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal Pre-setup di langkah, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat. Dipakai: SKU `Fixture.hardwareStock.p16.a[4].sku` dengan 12 sesi Event Log (Pre-setup #20, Tabel B) termasuk sesi `Add Stock` `Fixture.hardwareStock.p20.b[2].date` (Success 15, Waiting for Approval 1, Modified By `Fixture.hardwareStock.account.p11.distributorMitra.shortName`), sesi `Add Stock` `Fixture.hardwareStock.p20.b[4].date` (Success 13, Waiting for Approval 2, Modified By `Fixture.hardwareStock.account.p01.totalControl.shortName`), sesi `Delete Stock` `Fixture.hardwareStock.p20.b[1].date` (Success 1, Waiting for Approval `—`, Modified By `Fixture.hardwareStock.account.p01.totalControl.shortName`), dan satu sesi tanpa unit tercatat (Pre-setup #20b); SKU `Fixture.hardwareStock.p16.a[6].sku` tanpa sesi Event Log.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture |
|---|---|---|---|
| `abbrDistA` | #10 | Singkatan `[Nama Depan] [Inisial]` user akun #10 (format Modified By dan Registered By, R-14) | `Fixture.hardwareStock.account.p10.distributorCakra.shortName` |
| `fullDistB` | #11 | Nama lengkap user akun #11 (tampil pada hover pelaku) | `Fixture.hardwareStock.account.p11.distributorMitra.fullName` |
| `abbrDistB` | #11 | Singkatan `[Nama Depan] [Inisial]` user akun #11 | `Fixture.hardwareStock.account.p11.distributorMitra.shortName` |
| `distA` | #10 | Nama entitas Distributor akun #10 | `Fixture.hardwareStock.p10.entityName` |
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

- Data milik spec (S-06, S-12; suffix `{runId}-274`): unit Available `SN-MATCH524-{runId}-274` pada SKU Bulk IX6 di-seed hook `before` lewat sesi API aktor (kemampuan seed disediakan tim FE/BE; endpoint tidak disebut TC, PRD, atau LLD). Data Dinamis yang dibuat langkah: `SN-ZEBRA-RFD40-{runId}-274` (unit OK TC-524). Hook `after` menghapus semua data bersuffix `-274` yang masih ada (idempotent, juga bila spec gagal di tengah). Satu sesi `Add Stock` baru dibuat TC-524 (audit trail permanen, tidak dihapus).
- State global yang diubah (pengecualian S-06 `[KEPUTUSAN 2026-10-30]`): Device Name `Fixture.hardwareStock.p16.a[4].deviceName` di-rename menjadi `Fixture.hardwareStock.p16.a[4].deviceName R274` pada TC-518 lewat sesi API aktor (Settings > Device > Name, kemampuan disediakan tim BE/FE). Data ini tidak dapat dimiliki spec karena terikat pada sesi Event Log Pre-setup #20 (audit trail permanen) yang diamati snapshot-nya. Pemulihan ke `Fixture.hardwareStock.p16.a[4].deviceName` dijamin fixture backend yang disediakan tim FE/BE (belum dinyatakan di `suite.md`, lihat Temuan untuk QA), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung (langkah 68); suite berjalan serial; efeknya (Last Updated SKU dan entri audit trail rename) tidak dipulihkan.
- Kemampuan teknis (disediakan tim FE): intercept dan penahanan respons HTTP daftar Event Log dan detail sesi selama 3 detik (nilai dari Data Uji TC-586 dan TC-587) lalu melepasnya; simulator reader USB Handheld Reader (service driver mock, Pre-setup #25) hanya sebagai pemicu Add Stock Sync pada TC-524.
- Waktu: format tanggal dan jam mengikuti General Settings Pre-setup #15; tidak ada pergeseran jam.

## Test Steps

### TC-AC-ACHS-520: Popup Event Log genuinely empty

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[6].sku`
2. Klik icon `[Event Log]`
3. Verifikasi empty state: ilustrasi (empty box) dengan Title `No event log yet` dan Description `Add Stock and Delete Stock sessions for this SKU will appear here.`
4. Tutup popup lewat `[X]`

### TC-AC-ACHS-525: Tooltip icon Event Log

5. Klik segmen breadcrumb `Stock`, lalu klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
6. Klik Tab `Available`
7. Hover icon `[Event Log]`
8. Verifikasi tooltip `Event Log` tampil saat hover
9. Fokuskan icon `[Event Log]` dengan keyboard (Tab)
10. Verifikasi tooltip `Event Log` tampil saat fokus keyboard
11. Klik icon `[Event Log]`
12. Verifikasi popup berjudul `Event Log` terbuka

### TC-AC-ACHS-514: Screening popup Event Log

13. Verifikasi Header: Title `Event Log` dan tombol close `[X]`
14. Verifikasi Header: Table Tools `Search`, `Filter`, `Download`
15. Verifikasi Header: placeholder Search `Search by activity or modified by...`
16. Verifikasi Body: kolom `Date` (sortable), `Activity` (sortable), `Success` (sortable), `Waiting for Approval` (sortable), `Modified By` (sortable), dan Column Visibility `(⋯)` (unsortable)
17. Verifikasi Body: tiap baris memuat row action `Detail` (ikon FileInfoLine)
18. Verifikasi Body: default sort Date Newest First
19. Verifikasi Footer: pagination default 10 baris per halaman
20. Verifikasi Footer: info `Showing 1–10 of {nEventLog} entries` dengan `{nEventLog}` jumlah sesi baseline hook `before` (bukan angka absolut, S-12)

### TC-AC-ACHS-515: Isi sel Event Log

21. Verifikasi Activity tampil teks biasa `Add Stock` atau `Delete Stock` (bukan badge)
22. Verifikasi baris `Add Stock` `Fixture.hardwareStock.p20.b[2].date`: Success `15` dan Waiting for Approval `1`
23. Verifikasi baris `Delete Stock` `Fixture.hardwareStock.p20.b[1].date`: Success `1` dan Waiting for Approval `—`
24. Verifikasi Modified By `Fixture.hardwareStock.account.p11.distributorMitra.shortName` pada baris `Add Stock` `Fixture.hardwareStock.p20.b[2].date`
25. Hover nilai Modified By `Fixture.hardwareStock.account.p11.distributorMitra.shortName`
26. Verifikasi hover menampilkan `Fixture.hardwareStock.account.p11.distributorMitra.fullName`

### TC-AC-ACHS-516: Popup Detail sesi Add Stock

27. Klik `Detail` pada sesi `Add Stock` yang memuat unit Waiting for Approval (`Fixture.hardwareStock.p20.b[4].date`)
28. Verifikasi Title popup `Add Stock Detail`
29. Verifikasi section `Added` dan `Waiting for Approval` masing-masing berisi tabel read-only kolom `Device Name` dan `Serial Number`
30. Verifikasi urutan awal Serial Number A–Z di dalam tiap section
31. Verifikasi tanpa Search, Filter, Sort, Setup Column, maupun paginasi
32. Scroll isi popup
33. Verifikasi scroll internal dengan header tetap
34. Tutup popup Detail

### TC-AC-ACHS-587: Loading popup Detail

35. Pasang penahanan respons detail sesi selama 3 detik
36. Klik `Detail` pada sesi `Add Stock` (`Fixture.hardwareStock.p20.b[4].date`)
37. Verifikasi isi popup Detail menampilkan Loading component sampai data tiba
38. Lepas penahanan respons
39. Verifikasi popup `Add Stock Detail` menampilkan section `Added` dengan 13 baris
40. Verifikasi section `Waiting for Approval` dengan 2 baris
41. Tutup popup Detail

### TC-AC-ACHS-517: Popup Detail sesi Delete Stock

42. Klik `Detail` pada sesi `Delete Stock` (`Fixture.hardwareStock.p20.b[1].date`)
43. Verifikasi Title popup `Delete Stock Detail`
44. Verifikasi section `Deleted` berisi satu baris Device Name dan Serial Number snapshot saat sesi
45. Verifikasi section tanpa baris (`Added` dan `Waiting for Approval`) tidak ditampilkan dan judulnya ikut disembunyikan
46. Tutup popup Detail

### TC-AC-ACHS-521: Popup Detail tanpa unit

47. Klik `Detail` pada sesi tanpa unit tercatat (fixture Pre-setup #20b)
48. Verifikasi empty state: ilustrasi (empty box) dengan Title `No details to show` dan Description `There are no units recorded for this session.`
49. Tutup popup Detail dan popup Event Log

### TC-AC-ACHS-586: Loading popup Event Log

50. Pasang penahanan respons daftar Event Log selama 3 detik
51. Klik icon `[Event Log]`
52. Verifikasi popup `Event Log` terbuka dan area tabelnya menampilkan Loading component sampai data tiba
53. Lepas penahanan respons
54. Verifikasi tabel menampilkan 10 baris
55. Verifikasi footer `Showing 1–10 of {nEventLog} entries` dengan `{nEventLog}` jumlah sesi baseline hook `before` (bukan angka absolut, S-12)
56. Tutup popup Event Log

### TC-AC-ACHS-518: Snapshot sesi

57. Klik icon `[Event Log]`, lalu klik `Detail` pada sesi `Add Stock` (`Fixture.hardwareStock.p20.b[4].date`)
58. Catat Device Name dan Serial Number pada Popup Detail
59. Tutup popup Detail dan popup Event Log
60. Rename Device Name `Fixture.hardwareStock.p16.a[4].deviceName` menjadi `Fixture.hardwareStock.p16.a[4].deviceName R274` di Settings > Device > Name lewat sesi API hingga perubahan tersimpan; tunggu aksi selesai
61. Klik icon `[Event Log]`, lalu klik `Detail` pada sesi `Add Stock` yang sama
62. Verifikasi Popup Detail tetap menampilkan Device Name dan Serial Number saat sesi (snapshot) sesuai langkah 58, bukan nilai terbaru
63. Tutup popup Detail dan popup Event Log
64. Muat ulang halaman (F5)
65. Verifikasi unit pada Tab Available menampilkan Device Name terbaru `Fixture.hardwareStock.p16.a[4].deviceName R274` (live)
66. Klik segmen breadcrumb `Stock`
67. Verifikasi Stock List baris SKU `Fixture.hardwareStock.p16.a[4].sku` menampilkan Device Name terbaru `Fixture.hardwareStock.p16.a[4].deviceName R274` (live)
68. Pulihkan Device Name `Fixture.hardwareStock.p16.a[4].deviceName R274` menjadi `Fixture.hardwareStock.p16.a[4].deviceName` lewat sesi API hingga perubahan tersimpan

### TC-AC-ACHS-524: Success menghitung unit bypass E2a

69. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
70. Klik icon `[Event Log]`, catat sesi teratas, lalu tutup popup
71. Klik `[Add Stock]` pada toolbar Tab Available
72. Sync `SN-ZEBRA-RFD40-{runId}-274` (unit OK) dan `{snMatch524}` (unit match, bypass E2a) lewat simulator reader USB
73. Klik `[Submit]`, lalu klik `[Continue]`
74. Tunggu aksi selesai dan kembali ke Stock Detail SKU `Fixture.hardwareStock.p16.a[4].sku` Tab Available
75. Klik icon `[Event Log]`
76. Verifikasi sesi baru `Add Stock` tercatat di atas sesi yang dicatat pada langkah 70 dengan Success `2` (unit OK dan unit bypass E2a)
77. Verifikasi sesi baru itu memiliki Waiting for Approval `0`
78. Tutup popup Event Log
79. Logout, lalu login sebagai Distributor `Fixture.hardwareStock.account.p10.distributorCakra.fullName`; tunggu aksi selesai

### TC-AC-ACHS-523: Scope Distributor

80. Buka Hardware > Stock, klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
81. Klik icon `[Event Log]`
82. Verifikasi sedikitnya satu sesi tampil di popup Event Log (pembanding)
83. Verifikasi seluruh baris memiliki Modified By `Fixture.hardwareStock.account.p10.distributorCakra.shortName`
84. Verifikasi sesi `Fixture.hardwareStock.account.p11.distributorMitra.shortName` dan `Fixture.hardwareStock.account.p01.totalControl.shortName` tidak tampil

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-514, 515, 516, 517, 518, 520, 521, 523, 524, 525, 586, 587). Tidak ada TC hanya-BE di spec ini.
- Urutan menyimpang dari TC (alasan): TC-520 di awal (SKU berbeda, tanpa state); TC-525 sebelum TC-514 (membuka popup lewat icon yang diuji tooltip-nya); TC-587 sesudah TC-516 memakai sesi yang sama; TC-518 dan TC-524 (mengubah state) di akhir dan TC-523 paling akhir karena ganti akun (bagian 3, ganti akun eksplisit).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 5, 6, 11 (kecuali Verifikasi), 32, 34, 41, 46, 49, 56, 59, 63, 66, 69, 70, 78, 80, 81 (navigasi, membuka dan menutup popup), 25 (hover), 35, 38, 50, 53 (menahan dan melepas respons, S-09), 57, 58, 61, 64, 70, 71 sampai 75 (aksi alur TC), 60 dan 68 (pelaku kedua lewat sesi API, "Tunggu aksi selesai", R-20), 74 dan 79 (tunggu aksi selesai dan ganti akun).
- Spec ini 84 langkah, lebih dari sekitar 35 langkah. Alasan: seluruh blok membaca surface popup Event Log satu SKU dengan dataset Pre-setup #20 yang sama dan masing-masing berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Penahanan respons pada TC-586 dan TC-587 hanya mengamati state Loading (bukan kelas b). Simulator USB (kelas d) pada TC-524 dan rename Device Name pada TC-518 hanya pemicu state; pelaku kedua lewat sesi API bukan konteks kedua.
- `P-8`: TC-524 memakai simulator reader USB hanya untuk memicu Add Stock Sync (satu Sync OK dan satu unit match); USB (driver, Sync) bukan objek asersi dan kemampuan simulator dinyatakan di Prerequisites.
- Pasangan kolom Header, Body, dan Footer pada TC-514 ditulis satu `Verifikasi` per klausa kecuali daftar kolom dan daftar ikon Table Tools yang disebut utuh dalam satu butir Expected TC (S-01).
- Temuan untuk QA:
  - TC-524 tidak menyebut Serial Number unit match; spec memakai unit milik spec `{snMatch524}` sebagai unit yang cocok. Sesi baru tercatat di atas sesi yang dicatat, bukan pada posisi absolut (audit trail permanen, S-12, S-14).
  - TC-518 menyebut nama baru tanpa nilai; spec memakai `Fixture.hardwareStock.p16.a[4].deviceName R274`. Pemulihan Device Name dijamin fixture backend yang belum dinyatakan di `suite.md` (syarat pengecualian S-06 2026-10-30); perlu ditambahkan oleh pemilik `suite.md`.
  - TC-514 dan TC-586 menyebut total `12 entries` (absolut); spec memakai baseline `{nEventLog}` yang dibaca sebelum aksi karena Event Log audit trail permanen (S-12).
  - Seed unit milik spec `{snMatch524}` dan pembersihan data bersuffix `-274` di `after` disediakan tim FE/BE; mekanismenya tidak didefinisikan di TC, PRD, atau LLD.
  - TC-523 menyebut Modified By `Fixture.hardwareStock.account.p10.distributorCakra.shortName` untuk Distributor; asersi memakai nilai dari Pre-setup #20 (Tabel B).

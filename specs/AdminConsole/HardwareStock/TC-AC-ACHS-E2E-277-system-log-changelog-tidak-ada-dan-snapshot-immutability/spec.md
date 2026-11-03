---
id: TC-AC-ACHS-E2E-277-system-log-changelog-tidak-ada-dan-snapshot-immutability
title: "System Log, Changelog Tidak Ada, dan Snapshot Immutability"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-542
  - TC-AC-ACHS-543
  - TC-AC-ACHS-545
  - TC-AC-ACHS-564
coverage:
  web: automated
---

# System Log, Changelog Tidak Ada, dan Snapshot Immutability

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List, Approvals, dan Activity Log disetel hook `before` dan dipulihkan hook `after` spec ini; seeding Population Stock Pre-setup #16 sampai #22 dan #27; suite serial `parallel: false` (lihat suite.md).
- Aksi sumber (dipakai sebagai precondition, dijalankan hook `before` lewat sesi API aktor, kemampuan disediakan tim BE/FE, tidak diasersi): Add Stock manual satu Serial Number `SN-ZEBRA-FX9600-{runId}-277D` pada SKU `Fixture.hardwareStock.p16.a[3].sku` (sumber TC-80), Delete unit milik spec `{snDel277}` (TC-162), Approve Register Duplicate Subject milik spec `{snWfa}` (TC-180), auto-approve E3 `System` (TC-144, pool Additional Approver fixture Pre-setup #28 disetel lalu dipulihkan hook sebelum langkah UI), Cancel Request dan pelepasan unit oleh Client (TC-561 dan TC-557), dan Waiting for Approval hasil Sync (TC-535) atas unit Available milik spec `{snSync277}`. Akun Client pelaku disediakan tim FE.
- Data milik spec (S-06, R-08, S-12; suffix `{runId}-277`): unit Available `{snDel277}` (target Delete), unit Waiting for Approval `{snWfa}` beserta Subject Register Duplicate pending (target Approve; Existing Record Available, requester Distributor #12, struktur #17 Tabel E baris N = 28 dan #21 Tabel C baris ke-10), dan unit Available `{snSync277}` pada SKU `Fixture.hardwareStock.p16.a[4].sku` (target Sync match langkah 34) di-seed hook `before` lewat sesi API aktor (kemampuan seed disediakan tim FE/BE; endpoint tidak disebut TC, PRD, atau LLD). Unit Pre-setup #17 (termasuk `Fixture.hardwareStock.p17.e[10]` dan `Fixture.hardwareStock.p17.e[28]`) hanya dibaca dan tidak dihapus atau di-approve spec ini.
- Cleanup (R-08): hook `after` menghapus semua data milik spec bersuffix `{runId}-277` yang masih ada (unit, Subject, entri pending; idempotent, juga bila spec gagal di tengah). Entri Activity Log, System Log, Event Log, dan Hardware Log adalah audit trail permanen dan tidak dihapus.
- Baseline (S-12): jumlah entri System Log `Fixture.hardwareStock.account.p01.totalControl.fullName` dan Activity Log Object `Hardware` dicatat hook `before` sebelum aksi sumber pertama, per jenis entri (Add Stock, Delete, Duplicate Approved), agar langkah 23 sampai 25 memakai selisih per entri.
- State global yang diubah: Device Name `Fixture.hardwareStock.p16.a[4].deviceName` di-rename menjadi `Fixture.hardwareStock.p16.a[4].deviceName R277` (TC-545) dan Device Name `Fixture.hardwareStock.p16.a[3].deviceName` di-rename menjadi `Fixture.hardwareStock.p16.a[3].deviceName Pro` (TC-564) lewat sesi API aktor (Settings > Device > Name, kemampuan disediakan tim BE/FE); keduanya dipulihkan ke nama semula di langkah penghubung dan hook `after`.
- Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal Pre-setup, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture |
|---|---|---|---|
| `dnSfr` | #16 (Tabel A) | Device Name SKU Smart Fixed Reader (sama untuk `skuSfr`, `skuIx4`) | `Fixture.hardwareStock.p16.a[3].deviceName` |
| `skuSfr` | #16, #27 (Tabel A baris ke-3) | SKU Smart Fixed Reader dengan 8 unit Available (5 milik Distributor #10, 3 milik Distributor #11) | `Fixture.hardwareStock.p16.a[3].sku` |
| `dnHh (4)` | #16 (Tabel A) | Device Name SKU Handheld Reader (sama untuk `skuLong`, `skuShort`, `skuEda`) | `Fixture.hardwareStock.p16.a[4].deviceName` |
| `skuLong` | #16, #17, #18 (Tabel A baris ke-4) | SKU Handheld Reader Range Type Long Range, Total Registered 25 (18 Available, 7 In Use) ditambah 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `unitE19` | #17 (Tabel E baris N = 19) | Device Name unit Available pada `skuLong` yang tidak diubah aksi sumber, dibuka Hardware Log-nya (TC-543) | `Fixture.hardwareStock.p17.e[19].deviceName` |
| `snDel277` | milik spec | unit Available pada `skuLong` yang dihapus aksi sumber TC-162 | `SN-ZEBRA-RFD40-{runId}-277A` |
| `snWfa` | milik spec (struktur #17 Tabel E baris N = 28 dan #21 Tabel C baris ke-10) | Serial Number unit Waiting for Approval milik spec; sekaligus Matched Identifier Subject Register Duplicate pending yang di-approve aksi sumber TC-180 | `SN-ZEBRA-RFD40-{runId}-277B` |
| `snSync277` | milik spec | unit Available pada `skuLong` yang menjadi target Sync match (langkah 34) | `SN-ZEBRA-RFD40-{runId}-277C` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName` |


## Test Steps

### TC-AC-ACHS-543: Surface Changelog tidak ada

1. Verifikasi toolbar Stock List tidak memiliki icon Changelog (Table Tools `Search`, `Filter`, `Download` tampil sebagai pembanding)
2. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
3. Verifikasi toolbar Tab Available tidak memiliki icon Changelog (Table Tools lain tampil sebagai pembanding)
4. Klik Tab `In Use`
5. Verifikasi toolbar Tab In Use tidak memiliki icon Changelog (Table Tools lain tampil sebagai pembanding)
6. Buka Approvals > Hardware Stock
7. Verifikasi toolbar Approvals Tab Active tidak memiliki icon Changelog (Table Tools lain tampil sebagai pembanding)
8. Klik Tab `History`
9. Verifikasi toolbar Approvals Tab History tidak memiliki icon Changelog (Table Tools lain tampil sebagai pembanding)
10. Buka Hardware > Stock, klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`, lalu klik icon `[Event Log]`
11. Verifikasi toolbar popup Event Log tidak memiliki icon Changelog (Table Tools lain tampil sebagai pembanding)
12. Verifikasi tidak ada modal Changelog pada keenam surface
13. Verifikasi popup Event Log menampilkan sedikitnya satu sesi riwayat (Event Log per SKU)
14. Tutup popup Event Log
15. Klik Tab `Available`, ketik Search `Fixture.hardwareStock.p17.e[19].serialNumber`, tekan Enter
16. Klik `(⋯)` pada baris unit `Fixture.hardwareStock.p17.e[19].deviceName`, lalu klik row action `Hardware Log`
17. Verifikasi popup Hardware Log unit `Fixture.hardwareStock.p17.e[19].deviceName` menampilkan sedikitnya satu entri riwayat (Hardware Log per unit)
18. Tutup popup Hardware Log
19. Kosongkan kolom Search Tab Available, tekan Enter
20. Buka Admin Console > Activity Log, lalu terapkan Filter Object = `Hardware`
21. Verifikasi Activity Log menampilkan sedikitnya satu entri Object `Hardware` (Activity Log lintas SKU)

### TC-AC-ACHS-542: System Log aktor

22. Buka Settings > User, lalu klik Detail `Fixture.hardwareStock.account.p01.totalControl.fullName`, lalu klik Tab `System Log`
23. Verifikasi System Log `Fixture.hardwareStock.account.p01.totalControl.fullName` memuat entri Add Stock dan jumlah entri Add Stock bertambah 1 dari baseline
24. Verifikasi System Log `Fixture.hardwareStock.account.p01.totalControl.fullName` memuat entri Delete dan jumlah entri Delete bertambah 1 dari baseline
25. Verifikasi System Log `Fixture.hardwareStock.account.p01.totalControl.fullName` memuat entri keputusan Approve (`Duplicate Approved`) dan jumlah entri bertambah 1 dari baseline
26. Buka Detail User Client pelaku Cancel dan Release, lalu klik Tab `System Log`
27. Verifikasi System Log user Client pelaku memuat `Device Activation Canceled`
28. Verifikasi System Log user Client pelaku memuat `Device Released`
29. Verifikasi aksi E3 (`System`) tidak menghasilkan entri System Log baru (jumlah entri System Log tidak bertambah dari baseline untuk aksi E3)

### TC-AC-ACHS-545: Snapshot immutability pada Activity Log

30. Buka Admin Console > Activity Log, lalu terapkan Filter Object = `Hardware`
31. Cari entri terbaru dengan Name `Fixture.hardwareStock.p16.a[4].deviceName` Action `Waiting for Approval` (entri lama)
32. Catat Name pada entri `Waiting for Approval` lama
33. Rename Device Name `Fixture.hardwareStock.p16.a[4].deviceName` menjadi `Fixture.hardwareStock.p16.a[4].deviceName R277` di Settings > Device > Name lewat sesi API hingga perubahan tersimpan; tunggu aksi selesai
34. Jalankan Sync match baru yang menghasilkan entri `Waiting for Approval` lewat sesi API aktor hingga tersimpan; tunggu aksi selesai
35. Muat ulang Activity Log, lalu terapkan Filter Object = `Hardware`
36. Verifikasi entri lama tetap menampilkan Name `Fixture.hardwareStock.p16.a[4].deviceName` sesuai langkah 32 (snapshot, tidak berubah retroaktif)
37. Verifikasi entri baru memakai nama baru `Fixture.hardwareStock.p16.a[4].deviceName R277`
38. Pulihkan Device Name `Fixture.hardwareStock.p16.a[4].deviceName R277` menjadi `Fixture.hardwareStock.p16.a[4].deviceName` lewat sesi API hingga perubahan tersimpan

### TC-AC-ACHS-564: Nama live di Stock List dan unit, snapshot di Event Log

39. Buka Hardware > Stock, klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[3].sku`, klik icon `[Event Log]`, lalu klik `Detail` pada sesi Add Stock lama
40. Catat Device Name pada Popup Detail sesi lama, lalu tutup popup Detail dan popup Event Log
41. Rename Device Name `Fixture.hardwareStock.p16.a[3].deviceName` menjadi `Fixture.hardwareStock.p16.a[3].deviceName Pro` di Settings > Device > Name lewat sesi API hingga perubahan tersimpan; tunggu aksi selesai
42. Muat ulang halaman (F5)
43. Verifikasi label unit pada Stock Detail menampilkan `Fixture.hardwareStock.p16.a[3].deviceName Pro` (live-join)
44. Klik segmen breadcrumb `Stock`
45. Verifikasi Stock List baris SKU `Fixture.hardwareStock.p16.a[3].sku` menampilkan `Fixture.hardwareStock.p16.a[3].deviceName Pro` (live-join)
46. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[3].sku`, klik icon `[Event Log]`, lalu klik `Detail` pada sesi Add Stock lama yang sama
47. Verifikasi Popup Detail Event Log sesi lama tetap menampilkan nama saat sesi sesuai langkah 40 (snapshot)
48. Pulihkan Device Name `Fixture.hardwareStock.p16.a[3].deviceName Pro` menjadi `Fixture.hardwareStock.p16.a[3].deviceName` lewat sesi API hingga perubahan tersimpan

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-542, 543, 545, 564). Tidak ada TC hanya-BE di spec ini.
- `R-16`: langkah 15 memakai Search `Fixture.hardwareStock.p17.e[19].serialNumber` karena hook `before` menambah unit sehingga unit itu dapat pindah ke halaman 2 Tab Available; Search dikosongkan di langkah 19.
- Urutan menyimpang dari TC: TC-543 (baca murni) di awal; TC-545 dan TC-564 (mengubah state global) di akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 2, 4, 6, 8, 10, 14, 18, 19 (navigasi, menutup popup, dan mengosongkan Search), 15 dan 16 (Search unit dan membuka Hardware Log unit), 20 (Activity Log dengan Filter Object), 22, 26 (membuka Detail User), 30, 31, 35 (Activity Log dan mencari entri target, R-16), 32, 40 (mencatat nilai), 33, 34, 38, 41, 48 (pelaku kedua lewat sesi API, "Tunggu aksi selesai", R-20), 39, 42, 44, 46.
- `P-1`: langkah 29 (aksi E3 tidak menghasilkan entri System Log) bergantung pada state berat E3 yang dibangun di hook spec ini dan memakai baseline serta anchor positif entri keputusan Approve pada langkah 25 (S-05, butir 8b nomor 2).
- Batasan langkah 23 sampai 25: yang diasersi hanya entri Add Stock, Delete, dan keputusan Approve (`Duplicate Approved`); keputusan Reject yang disebut Expected a TC-542 tidak punya aksi sumber di spec ini dan tidak diasersi.
- Pelaku kedua lewat sesi API bukan konteks kedua kelas c dan tidak memakai `P-2`.
- Expected b TC-543 (riwayat dibaca di Event Log, Hardware Log, dan Activity Log) diasersi pada langkah 13, 17, dan 21 (satu `Verifikasi` per surface); langkah 15 sampai 21 adalah langkah penghubung dan Verifikasi dari Expected TC, bukan tambahan.
- Spec ini 48 langkah, lebih dari sekitar 35 langkah. Alasan: empat TC pencatatan lintas surface yang berbagi precondition aksi sumber yang sama; tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-542 menyebut "Detail User Client pelaku Cancel/Release" tanpa nama user; akun Client disediakan tim FE. Surface Settings > User > Detail > Tab System Log tidak didefinisikan langkah klik di TC.
  - TC-545 butir b ("entri baru memakai nama baru") tidak menyebut aksi yang menghasilkan entri baru; spec menjalankan Sync match baru (langkah 34) lewat sesi API aktor (mekanisme tidak didefinisikan di TC, PRD, atau LLD).
  - TC-545 dan TC-564 menyebut nama baru tanpa nilai; spec memakai `Fixture.hardwareStock.p16.a[4].deviceName R277` dan `Fixture.hardwareStock.p16.a[3].deviceName Pro` (TC-564 menyebutnya).
  - TC-542 Expected a menyebut entri "ditulis dalam satu dokumen yang sama dengan Activity Log", tetapi kesatuan dokumen backend tidak teramati lewat UI dan TC tidak memberi cara cek. Spec tidak mengasersinya karena kesatuan dokumen backend tidak teramati lewat UI (S-15); QA diminta menghapus klausa itu dari Expected atau menyebut cara observasinya.
  - TC-543 Expected b tidak menyebut unit yang dibuka Hardware Log-nya maupun isi riwayat; spec memakai unit `Fixture.hardwareStock.p17.e[19].deviceName` dan mengasersi sedikitnya satu entri riwayat di tiap surface (Event Log, Hardware Log, Activity Log). Kecukupan seed Hardware Log unit itu diasumsikan dari Pre-setup #17.
  - Aksi sumber Cancel Request dan pelepasan unit oleh Client (TC-561, TC-557) dan auto-approve E3 (TC-144) belum disebut berdata milik spec bersuffix `-277`; QA/FE diminta menetapkan target data milik spec untuk aksi itu.
  - TC-543 menyebut keenam surface tanpa Table Tools pembanding eksplisit; spec memakai ikon Table Tools lain sebagai pembanding.

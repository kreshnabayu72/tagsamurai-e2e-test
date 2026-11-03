---
id: TC-AC-ACHS-E2E-272-multi-konteks-race-add-stock-dan-delete
title: "Multi-Konteks: Race Add Stock dan Delete"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHS-99
  - TC-AC-ACHS-153
  - TC-AC-ACHS-166
  - TC-AC-ACHS-585
coverage:
  web: automated
---

# Multi-Konteks: Race Add Stock dan Delete

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun Sesi A awal: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite dan menutup semua konteks kedua.
- Konteks browser kedua (Sesi B) dibuka di langkah (konteks UI kedua yang hasilnya diasersi, kelas c). Akun Sesi B untuk TC-99, TC-585, dan TC-166: Total Control lain `Fixture.hardwareStock.account.p02.defaultUser.fullName` `Fixture.hardwareStock.account.p02.defaultUser.email` (Pre-setup #2, kata sandi `Spectra.env.AC_DEFAULT_USER_PASSWORD`, nama ditetapkan tim FE). Akun TC-153: Sesi A Create-Only `Fixture.hardwareStock.account.p04.createOnly.fullName` `Fixture.hardwareStock.account.p04.createOnly.email` (Pre-setup #4, `Spectra.env.AC_CREATE_ONLY_PASSWORD`, nama ditetapkan tim FE) dan Sesi B Distributor Manage hardware stock `Fixture.hardwareStock.account.p10.distributorCakra.fullName` (entitas `Fixture.hardwareStock.p10.entityName`), toggle Local Registration aktif, `Fixture.hardwareStock.account.p10.distributorCakra.email` (Pre-setup #10, `Spectra.env.AC_DISTRIBUTOR_CAKRA_PASSWORD`, nama ditetapkan tim FE); keduanya bukan Total Control.
- Hook suite: flag Guided Tooltip halaman Stock List diatur hook suite `before` dan dipulihkan `after` (untuk tiap akun dan sesi yang dipakai spec ini); seeding Population Stock Pre-setup #16 sampai #20 dan #27; suite serial `parallel: false` (lihat suite.md).
- Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal Pre-setup di langkah, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat. Dipakai hanya sebagai SKU induk: `Fixture.hardwareStock.p16.a[3].sku` (Smart Fixed Reader), `Fixture.hardwareStock.p16.a[5].sku` (BLE Gateway), `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`. Spec tidak menghapus atau mengubah unit Pre-setup (S-06). Data milik spec (suffix `{runId}-272`): unit Available `SN-RACE166-{runId}-272` pada `skuLong` (target Delete TC-166) di-seed hook `before` lewat sesi API aktor (kemampuan seed disediakan tim FE/BE; endpoint tidak disebut TC, PRD, atau LLD). Data Dinamis bersuffix yang dibuat langkah: `SN-CONC-0001-{runId}-272`, `SN-XSKU-0001-{runId}-272` (dua unit pada dua SKU), `SN-RACE-0001-{runId}-272`. Hook `after` menghapus semua data bersuffix `-272` yang masih ada (idempotent, juga bila spec gagal di tengah). Efek pada Pre-setup: hitungan unit SKU `skuSfr`, `skuBle`, `skuLong`, dan `skuShort` serta Last Updated keempat SKU berubah selama spec berjalan; hitungan dipulihkan hook `after`, Last Updated tidak dipulihkan.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture |
|---|---|---|---|
| `distA` | #10 | Nama entitas Distributor akun #10 | `Fixture.hardwareStock.p10.entityName` |
| `skuShort` | #16, #19 (Tabel A baris ke-1) | SKU Handheld Reader Range Type Short Range, Total Registered 50 (34 Available, 16 In Use), Device Name sama dengan `dnHh` | `Fixture.hardwareStock.p16.a[1].sku` |
| `skuSfr` | #16, #27 (Tabel A baris ke-3) | SKU Smart Fixed Reader dengan 8 unit Available (5 milik Distributor #10, 3 milik Distributor #11) | `Fixture.hardwareStock.p16.a[3].sku` |
| `skuLong` | #16, #17, #18 (Tabel A baris ke-4) | SKU Handheld Reader Range Type Long Range, Total Registered 25 (18 Available, 7 In Use) ditambah 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `skuBle` | #16, #27 (Tabel A baris ke-5) | SKU BLE Gateway dengan 5 unit (4 Available, 1 In Use) | `Fixture.hardwareStock.p16.a[5].sku` |
| `snRace166` | milik spec | unit Available pada `skuLong` yang dihapus dua sesi (TC-166) | `SN-RACE166-{runId}-272` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName` |
| `akun defaultUserPrincipal` | #2 | Akun Principal Default User | `Fixture.hardwareStock.account.p02.defaultUser.email`, `Fixture.hardwareStock.account.p02.defaultUser.fullName` |
| `akun createOnlyPrincipal` | #4 | Akun Principal Create-Only | `Fixture.hardwareStock.account.p04.createOnly.email`, `Fixture.hardwareStock.account.p04.createOnly.fullName` |
| `akun distributorCakra` | #10 | Akun Distributor PT Cakra Distribusi (Manage hardware stock) | `Fixture.hardwareStock.account.p10.distributorCakra.email`, `Fixture.hardwareStock.account.p10.distributorCakra.fullName` |

- Kemampuan teknis (disediakan tim FE): penyelarasan klik `[Submit]` atau `[Delete]` pada dua konteks browser secara hampir bersamaan; simulator reader USB Handheld Reader (service driver mock, Pre-setup #25) untuk TC-153. Konteks kedua dan sesi login browser terkait ditutup dan dihapus di akhir tiap TC (S-09).

## Test Steps

### TC-AC-ACHS-99: Dua Add Stock dengan Serial Number sama

1. Buka konteks browser kedua (Sesi B), login sebagai `Fixture.hardwareStock.account.p02.defaultUser.fullName`, dan buka Hardware > Stock
2. Sesi A dan Sesi B klik `(⋯)` pada baris SKU `Fixture.hardwareStock.p16.a[3].sku`, lalu klik opsi `Add Stock`
3. Sesi A dan Sesi B mengetik `SN-CONC-0001-{runId}-272`
4. Klik `[Submit]` pada kedua sesi hampir bersamaan
5. Verifikasi tepat satu sesi menampilkan toast sukses `Success, unit has been added to stock.`
6. Verifikasi sesi lain menampilkan error banner V-05 `Serial number SN-CONC-0001-{runId}-272 already exists in the system`
7. Buka Hardware > Stock Detail SKU `Fixture.hardwareStock.p16.a[3].sku` pada Sesi A, ketik Search `SN-CONC-0001-{runId}-272`, tekan Enter
8. Verifikasi hanya satu unit `SN-CONC-0001-{runId}-272` tersimpan
9. Tutup konteks Sesi B dan hapus sesi login browser terkait

### TC-AC-ACHS-585: Add Stock dua admin pada SKU berbeda dengan Serial Number sama

10. Buka konteks browser kedua (Sesi B), login sebagai `Fixture.hardwareStock.account.p02.defaultUser.fullName`, dan buka Hardware > Stock
11. Sesi A buka Hardware > Stock
12. Sesi A klik `(⋯)` pada baris SKU `Fixture.hardwareStock.p16.a[3].sku`, klik opsi `Add Stock`; Sesi B klik `(⋯)` pada baris SKU `Fixture.hardwareStock.p16.a[5].sku`, klik opsi `Add Stock`
13. Sesi A dan Sesi B mengetik `SN-XSKU-0001-{runId}-272`
14. Klik `[Submit]` pada kedua sesi
15. Verifikasi Sesi A menampilkan toast sukses `Success, unit has been added to stock.`
16. Verifikasi Sesi B menampilkan toast sukses `Success, unit has been added to stock.`
17. Verifikasi dua unit `SN-XSKU-0001-{runId}-272` tersimpan pada SKU masing-masing (satu pada SKU `Fixture.hardwareStock.p16.a[3].sku`, satu pada SKU `Fixture.hardwareStock.p16.a[5].sku`)
18. Tutup konteks Sesi B dan hapus sesi login browser terkait

### TC-AC-ACHS-166: Delete oleh dua admin pada unit yang sama

19. Buka konteks browser kedua (Sesi B), login sebagai `Fixture.hardwareStock.account.p02.defaultUser.fullName`, dan buka Hardware > Stock
20. Sesi A buka Hardware > Stock
21. Sesi A dan Sesi B klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
22. Sesi A dan Sesi B ketik Search `SN-RACE166-{runId}-272`, tekan Enter
23. Sesi A dan Sesi B membuka dialog Delete untuk unit `SN-RACE166-{runId}-272` (`(⋯)`, `Delete`)
24. Sesi A klik `[Delete]`
25. Verifikasi Sesi A menampilkan toast `Success, unit has been deleted.`
26. Sesi B klik `[Delete]`
27. Verifikasi Sesi B menampilkan toast netral `This unit is no longer available.`
28. Verifikasi tabel Sesi B di-refresh dan baris `SN-RACE166-{runId}-272` hilang
29. Verifikasi Sesi B tidak menampilkan toast sukses
30. Verifikasi tidak ada dialog D-04 pada Sesi B
31. Tutup konteks Sesi B dan hapus sesi login browser terkait

### TC-AC-ACHS-153: Dua Submit Sync bersamaan dengan Serial Number sama lintas SKU

32. Sesi A: logout dari `Fixture.hardwareStock.account.p01.totalControl.fullName`, login sebagai Create-Only `Fixture.hardwareStock.account.p04.createOnly.fullName`; tunggu aksi selesai
33. Buka konteks browser kedua (Sesi B), login sebagai Distributor `Fixture.hardwareStock.account.p10.distributorCakra.fullName` (`Fixture.hardwareStock.p10.entityName`), dan buka Hardware > Stock
34. Sesi A buka Hardware > Stock
35. Sesi A klik `(⋯)` pada baris SKU `Fixture.hardwareStock.p16.a[4].sku`, klik opsi `Add Stock`; Sesi B klik `(⋯)` pada baris SKU `Fixture.hardwareStock.p16.a[1].sku`, klik opsi `Add Stock`
36. Sesi A dan Sesi B Sync `SN-RACE-0001-{runId}-272` lewat simulator reader USB (badge `OK`)
37. Klik `[Submit]` pada kedua sesi hampir bersamaan
38. Amati hasil kedua sesi
39. Verifikasi tepat satu sesi menyimpan `SN-RACE-0001-{runId}-272` berstatus `Available` (commit pertama menang)
40. Verifikasi sesi kedua mencocokkan unit baru itu dan dialihkan ke Register Duplicate: unit berstatus `Waiting for Approval`
41. Verifikasi tidak ada pesan error duplikat pada kedua sesi (diverifikasi setelah hasil langkah 39 dan 40 teramati)
42. Verifikasi tidak ada bypass E2a: unit sesi kedua menunggu approval karena kedua pemohon bukan Total Control
43. Tutup konteks Sesi B dan hapus sesi login browser terkait

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-99, 153, 166, 585). Tidak ada TC hanya-BE di spec ini.
- Urutan menyimpang dari TC: TC-153 di akhir karena ganti akun Sesi A (bagian 3: ganti akun eksplisit) dan TC-166 (menghapus data) sebelum TC-153.
- `P-7`: TC-153 inheren membutuhkan simulator reader USB (kelas d: Sync pada langkah 35) bersama konteks lain kelas c (dua sesi, race antar-sesi) dalam alurnya sendiri; berada dalam spec kelas c ini sebagai pengecualian atas pemisahan kelas d. TC lain (TC-99, 166, 585) tidak membutuhkan USB.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 10, 19, 33 (membuka konteks kedua), 2, 11, 12, 20, 21, 23, 34, 35 (Sesi A membuka Hardware > Stock, S-14, serta membuka halaman dan dialog), 7 dan 22 (Search untuk menemukan baris target, R-16), 9, 18, 31, 43 (menutup konteks kedua, S-09), 32 (ganti akun), 38 (mengamati hasil).
- `P-1`: langkah 41 (tidak ada pesan error duplikat, TC-153) diverifikasi setelah hasil positif langkah 39 dan 40 sebagai anchor (8b.2); urutan ini menyimpang dari urutan Expected TC.
- Spec ini 43 langkah, di atas sekitar 35 langkah. Alasan: empat TC satu kelas multi-konteks; tiap blok berdiri sendiri dan memakai data Dinamis bersuffix atau unit milik spec berbeda, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Post Condition TC-166 ("hanya satu entri Activity Log `Delete` untuk unit tersebut") tidak punya langkah observasi di TC dan tidak diasersi; Expected butir c TC-166 ("tidak ada entri log kedua") dicatat sebagai Temuan untuk QA karena tidak diberi langkah observasi.
- Temuan untuk QA:
  - TC-99 dan TC-166 menyebut "Dua sesi Total Control" atau "Admin A dan B" tanpa akun kedua; spec memakai `Fixture.hardwareStock.account.p02.defaultUser.fullName` (Pre-setup #2, tier Total Control).
  - TC-585 memakai Serial Number `SN-XSKU-0001` pada SKU BLE Gateway yang identitasnya berformat MAC (Pre-setup #27 memuat identitas berformat MAC untuk SKU BLE); validasi format identitas pada SKU BLE tidak disebut TC.
  - TC-166 butir c ("tidak ada entri log kedua") tidak punya langkah observasi log di TC.
  - TC-153 tidak menyebut cara menentukan sesi pemenang; spec mengasersi hasil gabungan kedua sesi.
  - Seed unit milik spec `SN-RACE166-{runId}-272` dan pembersihan semua data bersuffix `-272` di `after` disediakan tim FE/BE; mekanismenya tidak didefinisikan di TC, PRD, atau LLD.

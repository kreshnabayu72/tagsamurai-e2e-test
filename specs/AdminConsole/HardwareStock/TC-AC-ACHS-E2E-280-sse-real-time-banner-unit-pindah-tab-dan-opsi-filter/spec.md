---
id: TC-AC-ACHS-E2E-280-sse-real-time-banner-unit-pindah-tab-dan-opsi-filter
title: "SSE Real-Time: Banner, Unit Pindah Tab, dan Opsi Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-553
  - TC-AC-ACHS-554
  - TC-AC-ACHS-603
coverage:
  web: automated
---

# SSE Real-Time: Banner, Unit Pindah Tab, dan Opsi Filter

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor (User A, sesi UI): Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List diatur hook suite `before` dan dipulihkan `after`; seeding Population Stock Pre-setup #16 sampai #22; suite serial `parallel: false` (lihat suite.md).
- Pelaku kedua (tanpa konteks UI kedua, lewat sesi API aktor; kemampuan disediakan tim BE/FE): User B Total Control lain `Fixture.hardwareStock.account.p02.defaultUser.fullName` `Fixture.hardwareStock.account.p02.defaultUser.email` (Pre-setup #2, `Spectra.env.AC_DEFAULT_USER_PASSWORD`, nama ditetapkan tim FE) yang memutuskan Subject unit milik spec `SN-ZEBRA-RFD40-{runId}-280W` (TC-553); Client yang mengaktivasi unit milik spec `SN-ZEBRA-RFD40-{runId}-280A` (TC-554, akun Client disediakan tim FE; sumber TC modul asal `global-settings/hardware-handheld-reader` ID 64); Create-Only `Fixture.hardwareStock.account.p04.createOnly.fullName` `Fixture.hardwareStock.account.p04.createOnly.email` (Pre-setup #4, `Spectra.env.AC_CREATE_ONLY_PASSWORD`, nama ditetapkan tim FE) yang menjalankan Add Stock manual `SN-IX4-0002-{runId}-280` (TC-603).
- Data milik spec (S-06, S-12; Model/Type `E2E280-{runId}` dengan `{runId}` terdiri atas digit; seeding di hook `before` lewat sesi API aktor, disediakan tim BE/FE tanpa endpoint karangan, kunci fixture-nya belum ada): satu SKU Handheld Reader milik spec yang memiliki 1 unit Available `SN-ZEBRA-RFD40-{runId}-280A` (target aktivasi TC-554) dan 1 unit Waiting for Approval `SN-ZEBRA-RFD40-{runId}-280W` beserta satu Subject Register Duplicate pending untuk unit itu pada Approvals Tab Active (struktur sama dengan unit `Fixture.hardwareStock.p17.e[28].deviceName` Pre-setup #17 dan #21). Data Pre-setup SKU `Fixture.hardwareStock.p16.a[4].sku` tidak diubah spec ini.
- Data Pre-setup yang diubah lalu dipulihkan (S-06): SKU `Fixture.hardwareStock.p16.a[6].sku` pada Pre-setup tidak memiliki unit (Total Registered 0, Last Updated `—`); spec yang membutuhkan SKU itu kosong (TC-46, TC-520) dijalankan sebelum spec ini (suite serial, urutan diputuskan di tahap script). Spec ini menambah unit `SN-IX4-0001-{runId}-280` (dibuat hook `before` lewat sesi API aktor, Registered By `Fixture.hardwareStock.account.p01.totalControl.shortName`; sumber TC-600) dan `SN-IX4-0002-{runId}-280` (langkah 34). Efeknya: Total Registered, Last Updated baris SKU itu, dan entri audit trail berubah.
- Cleanup (R-08): hook `after` menghapus secara idempotent unit `SN-IX4-0001-{runId}-280` dan `SN-IX4-0002-{runId}-280` dari SKU `Fixture.hardwareStock.p16.a[6].sku` serta SKU milik spec beserta unit `SN-ZEBRA-RFD40-{runId}-280A`, `SN-ZEBRA-RFD40-{runId}-280W`, dan Subject-nya. Pemulihan Last Updated baris SKU `Fixture.hardwareStock.p16.a[6].sku` ke keadaan awal (`—`) dijamin fixture backend yang disediakan tim FE/BE dan belum ada.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture |
|---|---|---|---|
| `dnSfr` | #16 (Tabel A) | Device Name SKU Smart Fixed Reader (sama untuk `skuSfr`, `skuIx4`) | `Fixture.hardwareStock.p16.a[3].deviceName` |
| `skuIx4` | #16 (Tabel A baris ke-6) | SKU Smart Fixed Reader tanpa unit (Total Registered 0, Last Updated `—`) | `Fixture.hardwareStock.p16.a[6].sku` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName`, `Fixture.hardwareStock.account.p01.totalControl.shortName` |
| `akun defaultUserPrincipal` | #2 | Akun Principal Default User | `Fixture.hardwareStock.account.p02.defaultUser.email`, `Fixture.hardwareStock.account.p02.defaultUser.fullName` |
| `akun createOnlyPrincipal` | #4 | Akun Principal Create-Only | `Fixture.hardwareStock.account.p04.createOnly.email`, `Fixture.hardwareStock.account.p04.createOnly.fullName`, `Fixture.hardwareStock.account.p04.createOnly.shortName` |

- Waktu: jendela propagasi real-time sampai 30 detik tanpa memuat ulang halaman mengikuti Data TC-553 dan TC-603 (bukan aturan PRD); tidak ada pergeseran jam.
- Baseline (S-12): Summary bar SKU milik spec dicatat sebelum keputusan Subject (langkah 3) dan sebelum aktivasi (langkah 14); asersi Summary bar relatif terhadap nilai itu.

## Test Steps

### TC-AC-ACHS-553: Banner dan baris Waiting for Approval hilang real-time

1. Ketik Search `E2E280-{runId}`, tekan Enter, lalu klik row action `Detail` pada SKU milik spec
2. Klik Tab `Available`
3. Catat Summary bar (Total Registered, Available, In Use)
4. Verifikasi banner Waiting for Approval tampil
5. Verifikasi unit `SN-ZEBRA-RFD40-{runId}-280W` berbadge `Waiting for Approval`
6. User B menyetujui (Approve) Subject `SN-ZEBRA-RFD40-{runId}-280W` lewat sesi API hingga keputusan tersimpan
7. Tunggu hingga banner hilang tanpa memuat ulang halaman (batas tunggu 30 detik)
8. Verifikasi banner hilang tanpa reload
9. Verifikasi baris `SN-ZEBRA-RFD40-{runId}-280W` berubah menjadi badge `Available`
10. Verifikasi Summary bar: Total Registered dan Available masing-masing bertambah 1 dari nilai langkah 3, In Use tidak berubah

### TC-AC-ACHS-554: Aktivasi unit oleh Client, unit pindah ke Tab In Use

11. Buka Hardware > Stock, ketik Search `E2E280-{runId}`, tekan Enter
12. Catat baris SKU milik spec di Stock List (Last Updated)
13. Klik row action `Detail` pada SKU milik spec
14. Biarkan Tab `Available` terbuka dan catat Summary bar (Total Registered, Available, In Use)
15. Client mengaktivasi unit `SN-ZEBRA-RFD40-{runId}-280A` dari Global Settings > Hardware lewat sesi API hingga tersimpan
16. Tunggu hingga unit `SN-ZEBRA-RFD40-{runId}-280A` hilang dari Tab Available tanpa memuat ulang halaman (batas tunggu 30 detik)
17. Verifikasi unit `SN-ZEBRA-RFD40-{runId}-280A` hilang dari Tab Available
18. Klik Tab `In Use`
19. Verifikasi unit `SN-ZEBRA-RFD40-{runId}-280A` muncul di Tab In Use dengan kolom Client terisi
20. Verifikasi kolom Activated At unit itu terisi
21. Verifikasi Status unit itu `Active`
22. Verifikasi Summary bar: Available berkurang 1 dan In Use bertambah 1 dari nilai langkah 14
23. Verifikasi Total Registered tidak berubah dari nilai langkah 14
24. Buka Hardware > Stock, ketik Search `E2E280-{runId}`, tekan Enter
25. Verifikasi baris SKU milik spec di Stock List ter-update
26. Verifikasi Last Updated baris SKU itu berubah dari nilai langkah 12

### TC-AC-ACHS-603: Opsi dropdown Filter Registered By real-time

27. Buka Hardware > Stock
28. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[6].sku`
29. Klik Tab `Available`
30. Klik icon Filter
31. Buka dropdown Registered By dan catat opsi
32. Verifikasi opsi Registered By hanya `Fixture.hardwareStock.account.p01.totalControl.shortName` (1 opsi)
33. Tutup dropdown
34. `Fixture.hardwareStock.account.p04.createOnly.fullName` menjalankan Add Stock manual `SN-IX4-0002-{runId}-280` pada SKU yang sama lewat sesi API hingga tersimpan
35. Tunggu hingga baris unit baru tampil di tabel tanpa memuat ulang halaman (batas tunggu 30 detik)
36. Buka kembali dropdown Registered By
37. Verifikasi opsi `Fixture.hardwareStock.account.p04.createOnly.shortName` muncul tanpa reload halaman
38. Verifikasi opsi Registered By menjadi `Fixture.hardwareStock.account.p04.createOnly.shortName`, `Fixture.hardwareStock.account.p01.totalControl.shortName` (2 opsi)
39. Verifikasi baris unit baru `Fixture.hardwareStock.p16.a[3].deviceName - 2` tampil di tabel tanpa reload

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-553, 554, 603). Tidak ada TC hanya-BE di spec ini.
- Kelas c (SSE dan real-time antar-sesi): pelaku kedua lewat sesi API aktor bukan konteks UI kedua dan tidak memakai `P-2`; objek ujinya adalah propagasi real-time ke sesi UI User A.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 2, 11, 13, 14, 18, 24, 27, 28, 29, 30 (navigasi dan pindah tab), 6, 15, 34 (pelaku kedua lewat sesi API, R-20), 7, 16, 35 (menunggu propagasi), 3, 12 (baseline), 31 dan 33 (membuka dan menutup dropdown), 36. Langkah TC "Pastikan Tab `Available` aktif" ditulis sebagai `Klik Tab` pada langkah 2 dan 29 (aksi deterministik, `[KEPUTUSAN 2026-11-02]`). Search `E2E280-{runId}` pada langkah 1, 11, dan 24 menemukan SKU milik spec (R-16).
- Dropdown Registered By pada langkah 31 sampai 33 dibuka dua kali (sebelum dan sesudah Sesi B); pembukaan kedua pada langkah 36.
- Post Condition TC-554 (`Hardware Log` unit memuat `Hardware Activated by [PIC]` dengan Description `Client`) tidak punya langkah observasi di TC dan tidak diasersi; dicatat di Temuan untuk QA.
- Spec ini 39 langkah, di atas sekitar 35 langkah. Alasan: tiga TC satu kelas (propagasi real-time antar-sesi) dengan sesi UI User A yang sama; tiap blok memakai SKU atau unit sendiri dan berdiri sendiri, dan menunggu propagasi dilakukan satu per blok.
- Temuan untuk QA:
  - TC-553 menyebut "User B klik Review... Submit"; spec memakai sesi API karena User B tidak diasersi (pelaku kedua), dan akun User B tidak disebut TC (Pre-setup #2 dipakai).
  - TC-553 dan TC-554 memutuskan Subject dan mengaktivasi unit Pre-setup (`Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[11].deviceName`); spec memakai SKU, unit, dan Subject milik spec dengan struktur sama (S-06). Seeding SKU, unit Available, unit Waiting for Approval, dan Subject itu tidak didefinisikan di TC, PRD, atau LLD sehingga ditulis sebagai kemampuan "disediakan tim BE/FE". Asersi absolut `26 | 19 | 7` TC-553 butir b diganti selisih terhadap baseline langkah 3 karena SKU milik spec tidak memiliki hitungan itu.
  - TC-603 mensyaratkan unit hasil TC-600 (`SN-IX4-0001`, Registered By `Fixture.hardwareStock.account.p01.totalControl.shortName`); spec menyiapkannya di hook `before` (TC-600 dihubungkan lewat seed) dan memulihkannya di hook `after`.
  - Nama baris unit baru `Fixture.hardwareStock.p16.a[3].deviceName - 2` bergantung penomoran unit; unit pertama IX4 harus bernomor 1.

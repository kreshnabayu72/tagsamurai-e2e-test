---
id: TC-AC-ACHS-E2E-279-lintas-modul-status-unit-aktivasi-pelepasan-global-settings
title: "Lintas Modul: Status Unit, Aktivasi, dan Pelepasan dari Global Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-555
  - TC-AC-ACHS-556
  - TC-AC-ACHS-557
  - TC-AC-ACHS-558
  - TC-AC-ACHS-559
coverage:
  web: automated
---

# Lintas Modul: Status Unit, Aktivasi, dan Pelepasan dari Global Settings

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List dan Activity Log diatur hook suite `before` dan dipulihkan `after`; seeding Population Stock Pre-setup #16 sampai #20 dan #23; suite serial `parallel: false` (lihat suite.md).
- Pelaku lintas modul: Client di Global Settings > Hardware (aksi Mark as Damaged, Mark as Missing, Mark as Available, aktivasi Jalur A, Delete reader, penghapusan atau penggantian perangkat BLE Gateway). Dijalankan lewat sesi API Client (akun Client `Fixture.hardwareStock.p23.client[4].name` (TC-558) disediakan tim FE; tidak ada di Pre-setup TC; kemampuan disediakan tim BE/FE; tidak ada endpoint yang ditulis di spec). Sumber TC modul asal: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (rujukan ID TC modul asal pada Expected: 64, 139, 141, 143, 151, 458).
- Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal Pre-setup di langkah, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat. Dipakai read-only: SKU `Fixture.hardwareStock.p16.a[4].sku` (Pre-setup #16, #17, #18) dan SKU `Fixture.hardwareStock.p16.a[5].sku` (Pre-setup #16, #27).
- Data milik spec (S-06, S-12; target aksi ubah atau lepas, di-seed hook `before` lewat sesi API aktor dengan struktur yang sama dengan unit Pre-setup yang digantikannya, urutan seeding: unit milik spec dibuat terakhir sehingga tampil pada halaman pertama tab, S-14): pada SKU `Fixture.hardwareStock.p16.a[4].sku` unit In Use `SN-ZEBRA-RFD40-{runId}-279A` (TC-555), unit Available `SN-ZEBRA-RFD40-{runId}-279B` (TC-556), unit In Use `SN-ZEBRA-RFD40-{runId}-279C` (TC-557), dan unit In Use `SN-ZEBRA-RFD40-{runId}-279D` (TC-559); pada SKU `Fixture.hardwareStock.p16.a[5].sku` perangkat BLE Gateway In Use `BLE-{runId}-279E` (TC-558, Client ke-4 Pre-setup #23). Seeding disediakan tim BE/FE tanpa endpoint karangan dan kunci fixture-nya belum ada (Temuan untuk QA). Data Pre-setup #16 sampai #20, #23, dan #27 tidak diubah spec ini.
- Cleanup (R-08): hook `after` menghapus secara idempotent seluruh data milik spec di atas (`{runId}-279A` sampai `{runId}-279E`). Entri Activity Log adalah audit trail permanen dan tidak dihapus.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture |
|---|---|---|---|
| `skuLong` | #16, #17, #18 (Tabel A baris ke-4) | SKU Handheld Reader Range Type Long Range, Total Registered 25 (18 Available, 7 In Use) ditambah 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `skuBle` | #16, #27 (Tabel A baris ke-5) | SKU BLE Gateway dengan 5 unit (4 Available, 1 In Use) | `Fixture.hardwareStock.p16.a[5].sku` |
| `client4` | #23 (urutan penulisan daftar Client, butir ke-4) | Nama Client ke-4 pada daftar Client Pre-setup #23 | `Fixture.hardwareStock.p23.client[4].name` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName` |

- Waktu: batas tunggu 30 detik tanpa memuat ulang halaman untuk TC-557 dan jendela 5 detik tanpa memuat ulang halaman sebelum asersi absence notifikasi in-app (langkah 32 dan 33, TC-557 butir d) adalah pilihan spec (nilai bukan aturan PRD; propagasi real-time); tidak ada pergeseran jam.
- Baseline (S-12): jumlah notifikasi di panel Notifikasi aktor (TC-557) serta jumlah entri Activity Log Object `Hardware` Action `Device Released` (TC-559) dicatat sebelum aksi.

## Test Steps

### TC-AC-ACHS-555: Kondisi unit tercermin di Tab In Use

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Klik Tab `In Use`
3. Catat Status unit `SN-ZEBRA-RFD40-{runId}-279A` (`Active`)
4. Client menjalankan Mark as Damaged pada unit `SN-ZEBRA-RFD40-{runId}-279A` lewat sesi API hingga tersimpan; tunggu aksi selesai
5. Muat ulang halaman (F5), lalu klik Tab `In Use`
6. Verifikasi Status unit `SN-ZEBRA-RFD40-{runId}-279A` `Damaged` (badge danger)
7. Client menjalankan Mark as Missing pada unit yang sama lewat sesi API hingga tersimpan; tunggu aksi selesai
8. Muat ulang halaman (F5), lalu klik Tab `In Use`
9. Verifikasi Status unit `Missing` (badge danger)
10. Client menjalankan Mark as Available pada unit yang sama lewat sesi API hingga tersimpan; tunggu aksi selesai
11. Muat ulang halaman (F5), lalu klik Tab `In Use`
12. Verifikasi Status unit `Active` (badge success)
13. Verifikasi unit `SN-ZEBRA-RFD40-{runId}-279A` tetap berstatus In Use di Tab In Use
14. Klik Tab `Available`
15. Verifikasi Tab Available tidak menampilkan data kondisi (tidak ada kolom Status kondisi `Damaged`, `Missing`, atau `Active`)

### TC-AC-ACHS-556: Unit baru In Use berstatus Active

16. Client mengaktivasi unit `SN-ZEBRA-RFD40-{runId}-279B` (Jalur A) lewat sesi API hingga tersimpan; tunggu aksi selesai
17. Muat ulang halaman (F5), lalu klik Tab `In Use`
18. Verifikasi Status unit `SN-ZEBRA-RFD40-{runId}-279B` `Active` (badge success)

### TC-AC-ACHS-557: Pelepasan unit Handheld Reader Jalur A

19. Catat Summary bar (Total Registered, Available, In Use) dan baris In Use `SN-ZEBRA-RFD40-{runId}-279C`
20. Catat jumlah notifikasi pada panel Notifikasi (baseline)
21. Client menghapus reader terkait unit `SN-ZEBRA-RFD40-{runId}-279C` di Global Settings > Hardware lewat sesi API hingga tersimpan
22. Tunggu hingga unit `SN-ZEBRA-RFD40-{runId}-279C` hilang dari Tab In Use tanpa memuat ulang halaman (batas tunggu 30 detik)
23. Verifikasi unit `SN-ZEBRA-RFD40-{runId}-279C` hilang dari Tab In Use
24. Klik Tab `Available`
25. Verifikasi unit `SN-ZEBRA-RFD40-{runId}-279C` muncul di Tab Available berstatus `Available`
26. Verifikasi In Use berkurang 1 dan Available bertambah 1 dari nilai langkah 19
27. Verifikasi Total Registered tetap sama dengan nilai langkah 19
28. Klik `(⋯)` pada baris unit `SN-ZEBRA-RFD40-{runId}-279C` di Tab `Available`
29. Verifikasi row action unit `SN-ZEBRA-RFD40-{runId}-279C` tidak memuat Recall (row action `Hardware Log` tampil sebagai pembanding)
30. Buka panel Notifikasi aktor (`Fixture.hardwareStock.account.p01.totalControl.fullName`)
31. Verifikasi panel Notifikasi terbuka dan memuat daftar notifikasi terbaru (anchor positif: panel yang diamati berfungsi sebelum asersi absence)
32. Tunggu 5 detik tanpa memuat ulang halaman
33. Verifikasi tidak ada notifikasi baru ke Principal: jumlah notifikasi sama dengan nilai langkah 20

### TC-AC-ACHS-558: Smart Fixed Reader atau BLE Gateway tidak dilepas

34. Buka Hardware > Stock, klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[5].sku`
35. Klik Tab `In Use`
36. Catat unit In Use `BLE-{runId}-279E` (kolom Client dan Status)
37. Client menghapus atau mengganti perangkat BLE Gateway di Global Settings lewat sesi API hingga tersimpan; tunggu aksi selesai
38. Muat ulang halaman (F5), lalu klik Tab `In Use`
39. Verifikasi unit `BLE-{runId}-279E` tetap In Use dengan kolom Client dan Status sama dengan langkah 36
40. Klik Tab `Available`
41. Verifikasi unit `BLE-{runId}-279E` tidak berpindah ke Tab Available (sedikitnya satu unit lain tampil sebagai pembanding)

### TC-AC-ACHS-559: Pelepasan ganda idempoten

42. Buka Hardware > Stock, klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`, lalu klik Tab `In Use`
43. Catat Summary bar (In Use) dan jumlah entri `Device Released` di Activity Log (baseline)
44. Dua sesi Client menghapus reader yang sama untuk unit `SN-ZEBRA-RFD40-{runId}-279D` di Global Settings lewat sesi API hingga tersimpan; tunggu aksi selesai
45. Muat ulang halaman (F5), lalu klik Tab `Available`
46. Verifikasi unit `SN-ZEBRA-RFD40-{runId}-279D` kembali Available satu kali
47. Verifikasi hitungan In Use berkurang tepat 1 dari nilai langkah 43
48. Buka Admin Console > Activity Log, lalu terapkan Filter Object = `Hardware`
49. Verifikasi hanya satu entri `Device Released` baru untuk unit tersebut

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-555, 556, 557, 558, 559). Tidak ada TC hanya-BE di spec ini.
- Pelaku lintas modul lewat sesi API Client bukan konteks kedua kelas c dan tidak memakai `P-2`.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 2, 14, 24, 28, 34, 35, 40, 42, 48 (navigasi, pindah tab, dan membuka menu `(⋯)`), 3, 19, 20, 36, 43 (baseline), 5, 8, 11, 17, 38, 45 (memuat ulang), 4, 7, 10, 16, 21, 37, 44 (pelaku kedua lewat sesi API, "Tunggu aksi selesai", R-20), 22 (menunggu propagasi), 30 (membuka panel Notifikasi), 32 (jendela 5 detik sebelum asersi absence notifikasi in-app pada langkah 33, butir 8b; langkah 31 adalah anchor positifnya).
- Spec ini 49 langkah, lebih dari sekitar 35 langkah. Alasan: lima TC lintas modul satu dataset unit RFD40 dan BLE; tiap blok memakai unit berbeda dan berdiri sendiri.
- Penempatan: TC-556 dan TC-558 tidak bergantung pada TC-554 atau TC-557; aktivasi dilakukan di langkah 16.
- `S-05`: TC-558 terbelah presence dan absence. Spec ini mengasersi Expected a dan b (langkah 39 dan 41: unit BLE tetap In Use dan tidak berpindah ke Tab Available); Expected c (tidak ada entri Activity Log `Device Released`) dipindah ke spec absence TC-AC-ACHS-E2E-281 yang menjalankan pemicu, baseline, dan anchor positif sendiri. Id TC-AC-ACHS-558 tetap di `sourceTc` kedua spec (keputusan 2026-11-02).
- Langkah 28 dan 29 (TC-557 butir c): membuka `(⋯)` pada baris unit sebelum mengasersi tidak adanya Recall, dengan `Hardware Log` sebagai pembanding.
- Post Condition TC-557 (Activity Log `Device Released`, Hardware Log unit `Hardware Returned to Stock by [PIC]`) tidak punya langkah observasi di TC; Activity Log diuji di spec 276.
- Temuan untuk QA:
  - TC-555, 556, 557, 558, 559 mengandalkan aksi Client di modul Global Settings yang tidak didefinisikan di TC ini; spec memakai sesi API Client (mekanisme tidak didefinisikan di TC, PRD, atau LLD).
  - TC-557 butir d ("tidak ada notifikasi ke Principal") dan butir c ("tidak ada aksi Recall") tidak menyebut langkah observasi; spec membandingkan jumlah notifikasi dengan baseline dan membuka row action unit.
  - TC-559 menyebut "dua sesi Client" tanpa menyebut akun; spec memakai dua sesi API Client yang disediakan tim FE.
  - Seeding unit In Use dan BLE Gateway milik spec (`{runId}-279A` sampai `-279E`, termasuk penugasan ke Client dan kuota) beserta cleanup `after` tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim BE/FE dan kunci fixture-nya belum ada.
  - Urutan default Tab Available (Registered At, Newest First) dan Tab In Use (Activated At, Newest First) didefinisikan PRD (`hardware-stock.md` baris 615 dan 663); spec mengandalkan unit milik spec yang di-seed terakhir tampil pada halaman pertama (S-14).
  - TC-557 butir d (tidak ada notifikasi ke Principal) tidak menyebut notifikasi pembanding yang pasti terkirim; anchor positif langkah 31 hanya membuktikan panel Notifikasi termuat, bukan jalur pengiriman. Butuh keputusan QA bila anchor pengiriman diperlukan.

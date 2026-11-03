---
id: TC-AC-ACHS-E2E-275-activity-log-add-stock-dan-delete
title: "Activity Log: Pencatatan Add Stock dan Delete"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-532
  - TC-AC-ACHS-533
  - TC-AC-ACHS-534
  - TC-AC-ACHS-544
coverage:
  web: automated
---

# Activity Log: Pencatatan Add Stock dan Delete

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Activity Log disetel hook `before` spec ini dan dipulihkan hook `after` spec ini; seeding Population Stock Pre-setup #16 sampai #20 dan #27; suite serial `parallel: false` (lihat suite.md).
- Aksi sumber (dipakai sebagai precondition TC-532, 533, 534, dijalankan hook `before` lewat sesi API aktor Total Control, kemampuan disediakan tim BE/FE, tidak diasersi): Add Stock manual satu Serial Number `SN-ZEBRA-FX9600-{runId}-275a` dan tiga Serial Number `SN-ZEBRA-FX9600-{runId}-275b` sampai `-275d` pada SKU `Fixture.hardwareStock.p16.a[3].sku` (sumber TC-80 dan TC-81); Submit Sync campuran pada SKU `Fixture.hardwareStock.p16.a[4].sku` (dua unit OK `SN-ZEBRA-RFD40-{runId}-275a`, `-275b` dan satu unit match milik spec `{snMatch533a}`) dan Submit Sync seluruhnya match (`{snMatch533b}`) (sumber TC-136 dan TC-137); Delete unit milik spec `{snDel534}` (sumber TC-162). Mekanisme pemicu Sync tanpa perangkat USB tidak didefinisikan di TC, PRD, atau LLD (lihat Temuan untuk QA).
- Baseline (S-12): jumlah entri Activity Log Object `Hardware` per Name dan Action dicatat hook `before` sebelum aksi sumber pertama; asersi "tepat satu entri" memakai selisih terhadap baseline (audit trail permanen, total tidak diasersi absolut).
- Kemampuan teknis (disediakan tim BE/FE): membaca jumlah entri Activity Log sebelum aksi; sesi API aktor untuk TC-544. Data Pre-setup hanya dibaca (SKU); spec tidak menghapus atau mengubah unit Pre-setup (S-06). Data milik spec (S-06, S-12; suffix `{runId}-275`): unit Available `{snDel534}` pada SKU `skuLong`, `{snDel544}` pada SKU `skuSfr`, serta `{snMatch533a}` dan `{snMatch533b}` pada SKU Bulk IX6 (Pre-setup #16, Tabel A baris ke-8) di-seed hook `before` lewat sesi API aktor (kemampuan seed disediakan tim FE/BE; endpoint tidak disebut TC, PRD, atau LLD). Data Dinamis yang dibuat aksi sumber dan langkah: semua Serial Number bersuffix `-275` di atas dan `SN-ZEBRA-FX9600-{runId}-275e` sampai `-275g` (TC-544). Hook `after` menghapus semua data bersuffix `-275` yang masih ada (idempotent, juga bila spec gagal di tengah); entri Activity Log tidak dihapus (audit trail permanen). Efek pada Pre-setup: hitungan unit SKU `skuSfr` dan `skuLong` serta Last Updated kedua SKU berubah selama spec berjalan; hitungan dipulihkan hook `after`, Last Updated tidak dipulihkan.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture |
|---|---|---|---|
| `skuSfr` | #16, #27 (Tabel A baris ke-3) | SKU Smart Fixed Reader dengan 8 unit Available (5 milik Distributor #10, 3 milik Distributor #11) | `Fixture.hardwareStock.p16.a[3].sku` |
| `skuLong` | #16, #17, #18 (Tabel A baris ke-4) | SKU Handheld Reader Range Type Long Range, Total Registered 25 (18 Available, 7 In Use) ditambah 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `snDel534` | milik spec | unit Available pada `skuLong` yang dihapus aksi sumber TC-534 | `SN-DEL534-{runId}-275` |
| `snMatch533a` | milik spec | unit Available pada SKU Bulk IX6 yang cocok pada Submit Sync campuran (TC-533) | `SN-MATCH533A-{runId}-275` |
| `snMatch533b` | milik spec | unit Available pada SKU Bulk IX6 yang cocok pada Submit Sync seluruhnya match (TC-533) | `SN-MATCH533B-{runId}-275` |
| `snDel544` | milik spec | unit Available pada `skuSfr` yang dihapus pada TC-544 | `SN-DEL544-{runId}-275` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName`, `Fixture.hardwareStock.account.p01.totalControl.shortName` (Modified By, format `[First Name] [Last Initial]`) |

- Waktu: kolom Date berketelitian menit; tidak ada asersi Date absolut.

## Test Steps

1. Buka Admin Console > Activity Log
2. Terapkan Filter Object = `Hardware`

### TC-AC-ACHS-532: Add Stock manual, Quantity

3. Verifikasi tiap submit menghasilkan tepat satu entri: jumlah entri `Add Stock` Name `Fixture.hardwareStock.p16.a[3].sku` bertambah 2 dari baseline untuk dua submit
4. Cari entri Name `Fixture.hardwareStock.p16.a[3].sku` untuk Add Stock satu Serial Number pada himpunan dua baris teratas urutan `Date` terbaru
5. Verifikasi entri satu Serial Number: Object `Hardware`, Name `Fixture.hardwareStock.p16.a[3].sku`, Action `Add Stock`, Field `Quantity`, Old Value `—`, New Value `+1 unit`, Modified By `Fixture.hardwareStock.account.p01.totalControl.shortName`
6. Cari entri Name `Fixture.hardwareStock.p16.a[3].sku` untuk Add Stock tiga Serial Number pada himpunan dua baris teratas yang sama
7. Verifikasi entri tiga Serial Number memiliki New Value `+3 units`

### TC-AC-ACHS-533: Add Stock dari Sync

8. Verifikasi Submit Sync seluruhnya match tidak menambah entri `Add Stock` (jumlah entri `Add Stock` Name `Fixture.hardwareStock.p16.a[4].sku` bertambah 1 dari baseline, hanya dari Submit campuran)
9. Verifikasi jumlah entri Activity Log Object `Hardware` dengan Name `Fixture.hardwareStock.p16.a[4].deviceName` dan Action `Waiting for Approval` bertambah 2 dari baseline (satu unit match pada Submit campuran, satu unit match pada Submit seluruhnya match)
10. Cari entri Name `Fixture.hardwareStock.p16.a[4].sku` (Add Stock) dan Name `Fixture.hardwareStock.p16.a[4].deviceName` (Waiting for Approval) untuk Submit Sync campuran pada himpunan baris teratas urutan `Date` terbaru sebanyak selisih langkah 8 dan 9
11. Verifikasi satu entri `Add Stock` dengan New Value `+2 units`
12. Verifikasi satu entri `Waiting for Approval` untuk unit match
13. Cari entri untuk Submit Sync yang seluruh barisnya match pada himpunan baris teratas yang sama
14. Verifikasi entri `Waiting for Approval` per unit match tampil

### TC-AC-ACHS-534: Delete per unit

15. Verifikasi tepat satu entri untuk satu unit yang dihapus (selisih 1 dari baseline, Name `{snDel534}` bersuffix unik)
16. Cari entri terbaru dengan Name `{snDel534}`
17. Verifikasi entri: Object `Hardware`, Name `{snDel534}`, Action `Delete`, Field `Serial Number`, Old Value `{snDel534}`, New Value `—`, Modified By `Fixture.hardwareStock.account.p01.totalControl.shortName`

### TC-AC-ACHS-544: Satu aksi satu entri per field

18. Catat jumlah entri Activity Log Object `Hardware` untuk Name `Fixture.hardwareStock.p16.a[3].sku`, Name `{snDel544}`, dan Name `Fixture.hardwareStock.p16.a[4].sku` sebagai baseline
19. Jalankan Add Stock tiga Serial Number `SN-ZEBRA-FX9600-{runId}-275e` sampai `-275g` pada SKU `Fixture.hardwareStock.p16.a[3].sku` lewat sesi API aktor hingga tersimpan; tunggu aksi selesai
20. Muat ulang Activity Log dan terapkan Filter Object = `Hardware`
21. Verifikasi Add Stock tiga Serial Number: tepat satu entri baru `+3 units`
22. Jalankan Add Stock yang gagal V-05 (Serial Number `SN-ZEBRA-FX9600-{runId}-275a` sudah ada) lewat sesi API aktor hingga ditolak; tunggu aksi selesai
23. Muat ulang Activity Log dan terapkan Filter Object = `Hardware`
24. Verifikasi Add Stock gagal V-05 tidak menambah entri: jumlah entri `Add Stock` Name `Fixture.hardwareStock.p16.a[3].sku` sama dengan sesudah langkah 21
25. Jalankan Delete unit `{snDel544}` lewat sesi API aktor hingga tersimpan; tunggu aksi selesai
26. Muat ulang Activity Log dan terapkan Filter Object = `Hardware`
27. Verifikasi Delete satu unit: tepat satu entri baru `Delete` Name `{snDel544}`
28. Verifikasi aksi pada SKU `Fixture.hardwareStock.p16.a[3].sku` tidak menghasilkan entri dengan Name SKU atau Serial Number SKU lain: jumlah entri Name `Fixture.hardwareStock.p16.a[4].sku` sama dengan baseline langkah 18

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-532, 533, 534, 544). Tidak ada TC hanya-BE di spec ini.
- `P-1`: langkah 8, 24, dan 28 (asersi jumlah "tidak menambah entri") bergantung pada state berat yang baru dibangun di spec ini (aksi sumber, Add Stock gagal V-05, Delete) dan memakai baseline serta anchor positif entri yang sudah tampil pada langkah sebelumnya (langkah 11, 21, 27) atau selisih jumlah positif pada langkah itu sendiri (langkah 8); bukan spec absence karena aksi nyata TC-544 ada di spec ini (S-05).
- Cara baca entri baru (S-14 `[KEPUTUSAN 2026-11-03]`): selisih jumlah entri terhadap baseline dibuktikan lebih dulu (langkah 3, 8, 9, 15); entri dibaca pada himpunan baris teratas urutan `Date` terbaru sebanyak selisih itu, tanpa mengandalkan urutan di antaranya karena beberapa entri bisa jatuh dalam menit yang sama (langkah 4, 6, 10, 13, 16); pada TC-544, langkah 21 (tepat satu entri baru `+3 units`) dan langkah 27 (tepat satu entri baru `Delete`) dibaca dengan cara yang sama: satu entri baru adalah himpunan baris teratas urutan `Date` terbaru sebanyak selisih jumlah entri terhadap baseline langkah 18 (selisih satu), tanpa mengandalkan urutan di antara entri se-menit.
- Langkah 9 (selisih `Waiting for Approval` +2 pada Activity Log Object `Hardware`, Name `Fixture.hardwareStock.p16.a[4].deviceName`, satu unit match per Submit Sync) asersi tambahan di luar TC, diturunkan dari aksi sumber di Prerequisites; Name entri `Waiting for Approval` = Device Name unit dan Name entri `Add Stock` = SKU (TC-533 langkah 3, PRD 8.2); dicatat sebagai bukti selisih sebelum entri dibaca (S-03, S-14).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 dan 2 (navigasi dan Filter), 4, 6, 10, 13, 16 (mencari entri target, R-16), 18 (baseline), 19, 22, 25 (pelaku lewat sesi API, "Tunggu aksi selesai", R-20), 20, 23, 26 (muat ulang dan Filter).
- Temuan untuk QA:
  - TC-532 sampai TC-534 memakai Dependensi ke TC aksi (TC-80, 81, 136, 137, 162); aksi sumber dijalankan lewat sesi API aktor karena spec tidak boleh bergantung pada spec lain, dan mekanismenya (terutama Sync tanpa perangkat USB) tidak didefinisikan di TC, PRD, atau LLD.
  - TC-533 dan TC-535 sudah selaras (Name `Add Stock` = SKU, Name `Waiting for Approval` = Device Name unit, PRD 8.2); langkah 9 sampai 14 spec 275 mengikuti itu.
  - TC-532 dan TC-533 tidak menyebut jumlah entri baseline per Name; spec memakai selisih terhadap baseline yang dicatat hook.
  - TC-544 butir d menyebut "Name SKU atau Serial Number SKU lain" tanpa SKU pembanding; spec memakai `Fixture.hardwareStock.p16.a[4].sku`.
  - Seed unit milik spec dan pembersihan data bersuffix `-275` di `after` disediakan tim FE/BE; mekanismenya tidak didefinisikan di TC, PRD, atau LLD.

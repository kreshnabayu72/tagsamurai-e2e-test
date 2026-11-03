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
- Hook suite: flag Guided Tooltip halaman Activity Log diatur hook suite `before` dan dipulihkan `after`; seeding Population Stock Pre-setup #16 sampai #20 dan #27; suite serial `parallel: false` (lihat suite.md).
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

3. Cari entri terbaru dengan Name `Fixture.hardwareStock.p16.a[3].sku` untuk Add Stock satu Serial Number
4. Verifikasi entri satu Serial Number: Object `Hardware`, Name `Fixture.hardwareStock.p16.a[3].sku`, Action `Add Stock`, Field `Quantity`, Old Value `—`, New Value `+1 unit`, Modified By `Fixture.hardwareStock.account.p01.totalControl.shortName`
5. Cari entri terbaru dengan Name `Fixture.hardwareStock.p16.a[3].sku` untuk Add Stock tiga Serial Number
6. Verifikasi entri tiga Serial Number memiliki New Value `+3 units`
7. Verifikasi tiap submit menghasilkan tepat satu entri: entri `Add Stock` Name `Fixture.hardwareStock.p16.a[3].sku` bertambah 2 dari baseline untuk dua submit

### TC-AC-ACHS-533: Add Stock dari Sync

8. Cari entri terbaru dengan Name `Fixture.hardwareStock.p16.a[4].sku` untuk Submit Sync campuran
9. Verifikasi satu entri `Add Stock` dengan New Value `+2 units`
10. Verifikasi satu entri `Waiting for Approval` untuk unit match
11. Cari entri untuk Submit Sync yang seluruh barisnya match
12. Verifikasi entri `Waiting for Approval` per unit match tampil
13. Verifikasi Submit Sync seluruhnya match tidak menambah entri `Add Stock` (jumlah entri `Add Stock` Name `Fixture.hardwareStock.p16.a[4].sku` bertambah 1 dari baseline, hanya dari Submit campuran)

### TC-AC-ACHS-534: Delete per unit

14. Cari entri terbaru dengan Name `{snDel534}`
15. Verifikasi entri: Object `Hardware`, Name `{snDel534}`, Action `Delete`, Field `Serial Number`, Old Value `{snDel534}`, New Value `—`, Modified By `Fixture.hardwareStock.account.p01.totalControl.shortName`
16. Verifikasi tepat satu entri untuk satu unit yang dihapus (selisih 1 dari baseline)

### TC-AC-ACHS-544: Satu aksi satu entri per field

17. Catat jumlah entri Activity Log Object `Hardware` untuk Name `Fixture.hardwareStock.p16.a[3].sku`, Name `{snDel544}`, dan Name `Fixture.hardwareStock.p16.a[4].sku` sebagai baseline
18. Jalankan Add Stock tiga Serial Number `SN-ZEBRA-FX9600-{runId}-275e` sampai `-275g` pada SKU `Fixture.hardwareStock.p16.a[3].sku` lewat sesi API aktor hingga tersimpan; tunggu aksi selesai
19. Muat ulang Activity Log dan terapkan Filter Object = `Hardware`
20. Verifikasi Add Stock tiga Serial Number: tepat satu entri baru `+3 units`
21. Jalankan Add Stock yang gagal V-05 (Serial Number `SN-ZEBRA-FX9600-{runId}-275a` sudah ada) lewat sesi API aktor hingga ditolak; tunggu aksi selesai
22. Muat ulang Activity Log dan terapkan Filter Object = `Hardware`
23. Verifikasi Add Stock gagal V-05 tidak menambah entri: jumlah entri `Add Stock` Name `Fixture.hardwareStock.p16.a[3].sku` sama dengan sesudah langkah 20
24. Jalankan Delete unit `{snDel544}` lewat sesi API aktor hingga tersimpan; tunggu aksi selesai
25. Muat ulang Activity Log dan terapkan Filter Object = `Hardware`
26. Verifikasi Delete satu unit: tepat satu entri baru `Delete` Name `{snDel544}`
27. Verifikasi aksi pada SKU `Fixture.hardwareStock.p16.a[3].sku` tidak menghasilkan entri dengan Name SKU atau Serial Number SKU lain: jumlah entri Name `Fixture.hardwareStock.p16.a[4].sku` sama dengan baseline langkah 17

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-532, 533, 534, 544). Tidak ada TC hanya-BE di spec ini.
- `P-1`: langkah 13, 23, dan 27 (asersi jumlah "tidak menambah entri") bergantung pada state berat yang baru dibangun di spec ini (aksi sumber, Add Stock gagal V-05, Delete) dan memakai baseline serta anchor positif entri yang sudah tampil pada langkah sebelumnya (langkah 9, 20, 26); bukan spec absence karena aksi nyata TC-544 ada di spec ini (S-05).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 dan 2 (navigasi dan Filter), 3, 5, 8, 11, 14 (mencari entri target, R-16), 17 (baseline), 18, 21, 24 (pelaku lewat sesi API, "Tunggu aksi selesai", R-20), 19, 22, 25 (muat ulang dan Filter).
- Temuan untuk QA:
  - TC-532 sampai TC-534 memakai Dependensi ke TC aksi (TC-80, 81, 136, 137, 162); aksi sumber dijalankan lewat sesi API aktor karena spec tidak boleh bergantung pada spec lain, dan mekanismenya (terutama Sync tanpa perangkat USB) tidak didefinisikan di TC, PRD, atau LLD.
  - TC-532 dan TC-533 tidak menyebut jumlah entri baseline per Name; spec memakai selisih terhadap baseline yang dicatat hook.
  - TC-544 butir d menyebut "Name SKU atau Serial Number SKU lain" tanpa SKU pembanding; spec memakai `Fixture.hardwareStock.p16.a[4].sku`.
  - Seed unit milik spec dan pembersihan data bersuffix `-275` di `after` disediakan tim FE/BE; mekanismenya tidak didefinisikan di TC, PRD, atau LLD.

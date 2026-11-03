---
id: TC-AC-ACHS-E2E-265-role-matrix-positif-delete-unit
title: "Role Matrix Positif: Delete Unit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-169
  - TC-AC-ACHS-170
  - TC-AC-ACHS-171
coverage:
  web: automated
---

# Role Matrix Positif: Delete Unit

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Hook suite: flag Guided Tooltip diatur hook suite `before` dan dipulihkan `after`; seeding Population Stock Pre-setup #16 sampai #20 dan #27; suite serial `parallel: false` (lihat suite.md). Flag Guided Tooltip halaman Stock List diatur untuk tiap akun yang dipakai spec ini di hook `before` dan dipulihkan di `after`.
- Role yang diuji (aksi Delete Unit berhasil):

| Role | Akun (Pre-setup) | Kata sandi | SKU dan unit target |
|---|---|---|---|
| Delete-Only | `Fixture.hardwareStock.account.p05.deleteOnly.fullName` `Fixture.hardwareStock.account.p05.deleteOnly.email` (#5) | `Spectra.env.AC_DELETE_ONLY_PASSWORD` (nama ditetapkan tim FE) | `{skuLong}`, unit milik spec `{snDel169}` |
| Distributor Manage hardware stock, Local Registration aktif | `Fixture.hardwareStock.account.p10.distributorCakra.fullName` (entitas `Fixture.hardwareStock.p10.entityName`) `Fixture.hardwareStock.account.p10.distributorCakra.email` (#10) | `Spectra.env.AC_DISTRIBUTOR_CAKRA_PASSWORD` (nama ditetapkan tim FE) | `{skuSfr}`, unit milik spec `{snDel171a}` dan `{snDel171b}` (milik `Fixture.hardwareStock.p10.entityName`) |
| Total Control | `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (#1) | `Spectra.env.AC_TC_PASSWORD` | `{skuSfr}`, unit registrasi mandiri milik spec `{snDel170}` (milik `Fixture.hardwareStock.p10.entityName`) |

- Login akun pertama (Delete-Only) di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Spec ditulis per blok role karena langkah tiap role berbeda dan ganti akun memakai Step eksplisit.
- Data Pre-setup hanya dibaca (S-12: tanpa nama literal Pre-setup di langkah): SKU `Fixture.hardwareStock.p16.a[4].sku` dan SKU `Fixture.hardwareStock.p16.a[3].sku` dengan 8 unit Available, `Fixture.hardwareStock.p27.fx[1].serialNumber` sampai `Fixture.hardwareStock.p27.fx[5].serialNumber` milik `Fixture.hardwareStock.p10.entityName` dan `Fixture.hardwareStock.p27.fx[6].serialNumber` sampai `Fixture.hardwareStock.p27.fx[8].serialNumber` milik `Fixture.hardwareStock.p11.entityName` (Pre-setup #27). Spec tidak menghapus atau mengubah unit Pre-setup (S-06).
- Data milik spec (S-06, S-12; suffix `{runId}-265`): `{snDel169}` di-seed hook `before` (lewat sesi API aktor Total Control); `{snDel171a}`, `{snDel171b}`, dan `{snDel170}` di-seed pada langkah 11 (langkah penghubung, sesudah hitungan 5 unit Pre-setup pada langkah 9 diasersi) lewat sesi API pelaku Distributor (kemampuan baca dan tulis disediakan tim BE/FE). Hook `after` menghapus semua data bersuffix `-265` yang masih ada (idempotent). Efek pada Pre-setup: hitungan unit SKU `{skuLong}` dan `{skuSfr}` serta Last Updated kedua SKU berubah selama spec berjalan; hitungan dipulihkan hook `after`, Last Updated tidak dipulihkan.

| Parameter | Pre-setup | Peran/atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture atau nilai |
|---|---|---|---|
| `distA` | #10 | Nama entitas Distributor akun #10 | `Fixture.hardwareStock.p10.entityName` |
| `distB` | #11 | Nama entitas Distributor akun #11 | `Fixture.hardwareStock.p11.entityName` |
| `skuSfr` | #16, #27 (Tabel A baris ke-3) | SKU Smart Fixed Reader dengan 8 unit Available (5 milik Distributor #10, 3 milik Distributor #11) | `Fixture.hardwareStock.p16.a[3].sku` |
| `skuLong` | #16, #17, #18 (Tabel A baris ke-4) | SKU Handheld Reader Range Type Long Range, Total Registered 25 (18 Available, 7 In Use) ditambah 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `snDel169` | milik spec | unit Available pada `skuLong` untuk Delete-Only (TC-169) | `SN-DEL169-{runId}-265` |
| `snDel171a` | milik spec | unit Available milik `distA` pada `skuSfr` untuk Distributor (TC-171, toggle Local Registration aktif) | `SN-DEL171A-{runId}-265` |
| `snDel171b` | milik spec | unit Available milik `distA` pada `skuSfr` untuk Distributor (TC-171, toggle Local Registration nonaktif) | `SN-DEL171B-{runId}-265` |
| `snDel170` | milik spec | unit registrasi mandiri milik `distA` pada `skuSfr` untuk Principal (TC-170) | `SN-DEL170-{runId}-265` |
| `snFx6` | #27 | Serial Number unit Available ke-6 pada `skuSfr` (urutan Serial Number naik), milik Distributor #11 | `Fixture.hardwareStock.p27.fx[6].serialNumber` |
| `snFx8` | #27 | Serial Number unit Available ke-8 pada `skuSfr` (urutan Serial Number naik), milik Distributor #11 | `Fixture.hardwareStock.p27.fx[8].serialNumber` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName` |
| `akun deleteOnlyPrincipal` | #5 | Akun Principal Delete-Only | `Fixture.hardwareStock.account.p05.deleteOnly.email`, `Fixture.hardwareStock.account.p05.deleteOnly.fullName` |
| `akun distributorCakra` | #10 | Akun Distributor PT Cakra Distribusi (Manage hardware stock) | `Fixture.hardwareStock.account.p10.distributorCakra.email`, `Fixture.hardwareStock.account.p10.distributorCakra.fullName` |

- Kemampuan teknis (disediakan tim BE/FE): sesi API pelaku (Principal untuk mengubah toggle Local Registration `Fixture.hardwareStock.p10.entityName`, sesi Distributor untuk membaca hitungan unit milik sendiri dan membuat unit milik sendiri); seed unit milik spec dan pembersihannya di `after`. Toggle Local Registration dipulihkan ke aktif di hook `after`.

## Test Steps

### TC-AC-ACHS-169: Delete-Only menghapus unit

1. Klik row action `Detail` pada SKU `{skuLong}`
2. Ketik Search `{snDel169}`, tekan Enter
3. Klik `(⋯)` pada baris `{snDel169}`, klik `Delete`, lalu klik `[Delete]` pada dialog
4. Verifikasi toast sukses `Success, unit has been deleted.`
5. Verifikasi unit `{snDel169}` terhapus dari Tab Available
6. Logout, lalu login sebagai Distributor `Fixture.hardwareStock.account.p10.distributorCakra.fullName` (tabel Role yang diuji); tunggu aksi selesai

### TC-AC-ACHS-171: Distributor menghapus unit milik sendiri

7. Buka Hardware > Stock
8. Klik row action `Detail` pada SKU `{skuSfr}`
9. Verifikasi Tab Available memuat 5 unit milik `{distA}`
10. Verifikasi 3 unit `{distB}` (`{snFx6}` sampai `{snFx8}`) tidak tampil
11. Buat unit milik `{distA}` `{snDel171a}`, `{snDel171b}`, dan `{snDel170}` pada SKU `{skuSfr}` lewat sesi API pelaku hingga unit tersimpan; tunggu aksi selesai
12. Muat ulang halaman (F5)
13. Catat hitungan unit `{distA}` pada SKU lewat kemampuan baca sesi Distributor
14. Klik `(⋯)` pada baris unit milik sendiri `{snDel171a}`, klik `Delete`, lalu klik `[Delete]`
15. Verifikasi toast sukses `Success, unit has been deleted.`
16. Principal mematikan toggle Local Registration `{distA}` lewat sesi API hingga perubahan tersimpan; tunggu aksi selesai
17. Muat ulang halaman (F5)
18. Klik `(⋯)` pada baris unit milik sendiri `{snDel171b}`, klik `Delete`, lalu klik `[Delete]`
19. Verifikasi toast sukses `Success, unit has been deleted.` (Delete tidak tunduk pada toggle Local Registration)
20. Principal mengaktifkan kembali toggle Local Registration lewat sesi API hingga perubahan tersimpan
21. Logout, lalu login sebagai Total Control `Fixture.hardwareStock.account.p01.totalControl.fullName` (tabel Role yang diuji); tunggu aksi selesai

### TC-AC-ACHS-170: Principal menghapus unit hasil Local Registration Distributor

22. Buka Hardware > Stock
23. Klik row action `Detail` pada SKU `{skuSfr}`
24. Catat Summary bar (Total Registered) dan hitungan unit `{distA}` pada SKU lewat kemampuan baca sesi Distributor
25. Ketik Search `{snDel170}`, tekan Enter
26. Klik `(⋯)` pada baris unit registrasi mandiri `{distA}` `{snDel170}`, klik `Delete`, lalu klik `[Delete]`
27. Verifikasi toast sukses `Success, unit has been deleted.`
28. Verifikasi unit `{snDel170}` terhapus dari Tab Available
29. Verifikasi Total Registered SKU berkurang 1 dari nilai langkah 24
30. Verifikasi hitungan unit `{distA}` berkurang 1 dari nilai langkah 24

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-169, 170, 171). Tidak ada TC hanya-BE di spec ini. Kombinasi role x aksi lain tanpa TC sumber (mis. Read Only atau Create-Only menghapus) dilaporkan ke QA dan tidak ditulis di sini.
- Urutan menyimpang dari TC: TC-171 sebelum TC-170 supaya Distributor masih melihat tepat 5 unit milik `{distA}` (TC-171 butir a) sebelum unit milik spec ditambahkan dan sebelum Principal menghapus salah satunya.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 6 dan 21 (ganti akun), 13 dan 24 (mencatat baseline), 2 dan 25 (Search untuk menemukan baris target, R-16), 11 (seed unit milik spec lewat sesi API), 12, 16, 17, 20 (pelaku kedua lewat sesi API dan memuat ulang). Langkah 16 sampai 19 menambah satu penghapusan unit kedua dengan toggle Local Registration nonaktif sebagai observasi Expected TC-171 butir c ("Delete tidak tunduk pada toggle Local Registration"), karena TC-171 tidak memberi langkah observasinya (S-01, S-03); asersi tambahan ini dicatat di sini beserta alasannya.
- Pelaku kedua (Principal) lewat sesi API bukan konteks kedua kelas c dan tidak memakai `P-2`.
- Temuan untuk QA:
  - TC-170 butir c menyebut "hitungan Distributor berkurang 1" tanpa menyebut surface tempat hitungan itu dibaca; spec membacanya lewat kemampuan baca sesi Distributor yang disediakan tim BE/FE.
  - TC-171 butir c tidak punya langkah observasi di TC (toggle Local Registration tidak diubah pada langkah TC); spec menambah langkah 16 sampai 19.
  - TC-170 menyebut "unit registrasi mandiri `Fixture.hardwareStock.p10.entityName`" tanpa Serial Number; spec memakai unit milik spec `{snDel170}`.
  - Email dan kata sandi akun selain Total Control mengikuti Pre-setup TC; nama env password ditetapkan tim FE (suite.md).
  - Seed unit milik spec (termasuk unit milik entitas Distributor) dan pembersihannya di `after` disediakan tim FE/BE; mekanismenya tidak didefinisikan di TC, PRD, atau LLD.

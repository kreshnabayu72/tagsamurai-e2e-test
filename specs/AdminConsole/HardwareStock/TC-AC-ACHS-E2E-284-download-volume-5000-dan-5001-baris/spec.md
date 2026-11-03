---
id: TC-AC-ACHS-E2E-284-download-volume-5000-dan-5001-baris
title: "Download Volume: 5.000 dan 5.001 Baris"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHS-579
coverage:
  web: automated
---

# Download Volume: 5.000 dan 5.001 Baris

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List diatur hook suite `before` dan dipulihkan `after`; suite serial `parallel: false` (lihat suite.md).
- Data (kelas e, volume): SKU `Fixture.hardwareStock.p30.sku` dengan 5.001 unit Available disiapkan lewat seed API (Pre-setup #30): 5.000 unit Registered By `Fixture.hardwareStock.account.p01.totalControl.shortName` dan 1 unit Registered By `Fixture.hardwareStock.account.p10.distributorCakra.shortName` (Serial Number berurutan sesuai Pre-setup #30). Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal, tanpa pengecualian S-12). Seed 5.001 unit dimuat hook `before` spec ini dan dihapus hook `after` (kemampuan seed disediakan tim BE/FE).

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture |
|---|---|---|---|
| `abbrDistA` | #10 | Singkatan `[Nama Depan] [Inisial]` user akun #10 (format Modified By dan Registered By, R-14) | `Fixture.hardwareStock.account.p10.distributorCakra.shortName` |
| `skuBulk5001` | #30 | SKU Smart Fixed Reader dengan 5.001 unit Available (5.000 unit Registered By akun #1 dan 1 unit Registered By Distributor #10) | `Fixture.hardwareStock.p30.sku` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName`, `Fixture.hardwareStock.account.p01.totalControl.shortName` |

- Waktu: jendela tunggu 5 detik tanpa memuat ulang halaman sebelum asersi absence notifikasi in-app (langkah 11 dan 12) adalah pilihan spec (bukan nilai TC atau PRD).
- Kemampuan teknis (disediakan tim FE): membaca isi berkas CSV hasil unduhan (jumlah baris data) dan mendeteksi loading screen serta toast, notifikasi in-app, dan jendela kedaluwarsa selama unduhan.

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p30.sku`
2. Klik icon Filter
3. Terapkan Filter Registered By = `Fixture.hardwareStock.account.p01.totalControl.shortName` (5.000 baris tersisa)
4. Klik icon Download, pilih `Download as CSV`
5. Verifikasi berkas CSV terunduh sinkron untuk 5.000 baris
6. Klik icon Filter, lalu hapus Filter Registered By (5.001 baris)
7. Klik icon Download, pilih `Download as CSV`
8. Verifikasi loading screen tampil sampai berkas siap
9. Verifikasi berkas CSV langsung terunduh dengan 5.001 baris data
10. Verifikasi tidak ada toast informasional
11. Tunggu 5 detik tanpa memuat ulang halaman
12. Verifikasi tidak ada notifikasi in-app
13. Verifikasi tidak ada jendela kedaluwarsa

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-579). Tidak ada TC hanya-BE di spec ini.
- Kelas e (volume data khusus 5.000 dan 5.001 baris); isi berkas dibaca hanya untuk jumlah baris (asersi fungsional); isi sel dan BOM adalah kelas f (spec 286, 138, 168, 188, 208, 228).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 2, 3, 6 (navigasi dan Filter), 4, 7 (membuka menu Download), 11 (jendela tunggu 5 detik sebelum asersi absence notifikasi in-app pada langkah 12, butir 8b). Asersi absence langkah 10, 12, dan 13 didahului pemicu unduhan (langkah 7) dan `Verifikasi` berkas terunduh (langkah 9) sebagai anchor positif (butir 8b nomor 11).
- Temuan untuk QA:
  - Expected a ("berkas terunduh sinkron") tidak menyebut cara membedakan sinkron dari loading screen; spec mengasersi berkas terunduh tanpa memeriksa ketiadaan loading screen pada 5.000 baris.
  - Expected b menyebut "5.001 baris data" tanpa menyebut baris header; spec menghitung baris data tanpa header.

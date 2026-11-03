---
id: TC-AC-ACHS-E2E-266-blokir-kondisi-data-delete-unit-sudah-in-use
title: "Blokir Kondisi Data: Delete Unit yang Sudah In Use"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHS-165
coverage:
  web: automated
---

# Blokir Kondisi Data: Delete Unit yang Sudah In Use

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.fullName` `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip diatur hook suite `before` dan dipulihkan `after`; seeding Population Stock Pre-setup #16 sampai #20; suite serial `parallel: false` (lihat suite.md).
- Data Pre-setup hanya dibaca: SKU `Fixture.hardwareStock.p16.a[4].sku` (Pre-setup #16 sampai #18). Spec tidak mengubah unit Pre-setup (S-06).
- Data milik spec (S-06, S-12; suffix `{runId}-266`): unit Available `SN-BLOK165-{runId}-266` pada `skuLong` di-seed hook `before` lewat sesi API aktor (kemampuan disediakan tim FE/BE) dan dihapus hook `after` (idempotent, termasuk bila unit sudah berstatus In Use akibat aktivasi Client pada langkah 5). Efek pada Pre-setup: hitungan Total Registered, Available, dan In Use SKU `skuLong` berubah selama spec berjalan dan dipulihkan hook `after`; Last Updated SKU berubah dan tidak dipulihkan.

| Parameter | Pre-setup | Peran dan atribut penentu (nilai dibaca penulis script dari tabel Pre-setup TC) | Kunci fixture atau nilai |
|---|---|---|---|
| `skuLong` | #16, #17, #18 (Tabel A baris ke-4) | SKU Handheld Reader Range Type Long Range, Total Registered 25 (18 Available, 7 In Use) ditambah 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `snBlok165` | milik spec | unit Available pada `skuLong` yang menjadi In Use akibat aktivasi Client di langkah 5 | `SN-BLOK165-{runId}-266` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName` |

- Kemampuan teknis (disediakan tim BE/FE): sesi API Client yang mengaktivasi unit (aksi Global Settings > Hardware, Jalur A Handheld Reader); seed unit milik spec dan pembersihannya di `after`; tidak ada endpoint yang ditulis di spec.

## Test Steps

1. Klik row action `Detail` pada SKU `{skuLong}`
2. Klik Tab `Available`
3. Ketik Search `{snBlok165}`, tekan Enter
4. Klik `(⋯)` pada baris `{snBlok165}`, klik `Delete` (jangan konfirmasi)
5. Client mengaktivasi unit `{snBlok165}` lewat sesi API hingga status In Use tersimpan; tunggu aksi selesai
6. Klik `[Delete]` pada dialog
7. Verifikasi dialog blok dengan Title `Cannot Delete Unit`, Body bullet `• {snBlok165}` dan teks `This unit is no longer available and cannot be deleted.`, dan tombol `[OK]`
8. Verifikasi tidak ada toast tambahan
9. Klik `[OK]`
10. Muat ulang halaman (F5)
11. Verifikasi Summary bar tampil
12. Klik Tab `In Use`
13. Ketik Search `{snBlok165}`, tekan Enter
14. Verifikasi unit `{snBlok165}` tetap ada di Tab In Use
15. Verifikasi unit `{snBlok165}` berstatus In Use

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-165). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 2 (`Klik Tab Available`, pengganti "Pastikan Tab `Available` aktif" TC), 3 dan 13 (Search untuk menemukan baris target, R-16), 9 (menutup dialog), 10 (memuat ulang), 12 (pindah tab). Langkah 11 menjadi anchor positif bahwa halaman termuat sebelum pembacaan tab (butir 8b nomor 2).
- Pelaku kedua (Client) lewat sesi API, bukan konteks kedua kelas c. Dialog `Cannot Delete Unit` ditulis satu `Verifikasi` karena Expected TC menyebut title, body, dan tombolnya sebagai satu butir dialog (S-01).
- Temuan untuk QA:
  - TC-165 diberi label Manual Only kriteria (d) dua sesi paralel; spec memakai sesi API untuk pelaku kedua, tanpa konteks UI kedua.
  - Mekanisme aktivasi Client lewat API tidak didefinisikan di TC, PRD, atau LLD yang dibaca; disediakan tim BE/FE. Seed unit milik spec dan pembersihannya di `after` (termasuk unit yang sudah In Use) juga disediakan tim FE/BE.

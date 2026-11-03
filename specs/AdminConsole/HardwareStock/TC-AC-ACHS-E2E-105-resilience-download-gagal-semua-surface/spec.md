---
id: TC-AC-ACHS-E2E-105-resilience-download-gagal-semua-surface
title: "Resilience Download: Gagal pada Semua Surface"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHS-254
  - TC-AC-ACHS-313
  - TC-AC-ACHS-365
  - TC-AC-ACHS-413
  - TC-AC-ACHS-463
  - TC-AC-ACHS-511
  - TC-AC-ACHS-580
coverage:
  web: automated
---

# Resilience Download: Gagal pada Semua Surface

## Prerequisites

- Mode: FE+BE (backend nyata dengan intercept parsial pada respons download).
- Akun aktor: Total Control Principal `{Fixture.hardwareStock.account.p01.totalControl.email}` (Pre-setup #1), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List dan Approvals diatur hook suite `before` dan dipulihkan `after`; seeding Population Stock Pre-setup #16 sampai #22; suite serial `parallel: false` (lihat suite.md).
- Kemampuan teknis (disediakan tim FE): `Spectra.intercept()` untuk memaksa respons HTTP 500 pada request download tiap surface dan melepasnya segera setelah asersi tiap blok (S-09); hook `after` melepas intercept yang tersisa; mendeteksi ketiadaan berkas terunduh. Tidak ada endpoint yang ditulis di spec.
- Data Pre-setup dirujuk lewat parameter (S-12: tanpa nama literal Pre-setup di langkah, tanpa pengecualian S-12); nilai dibaca dari tabel Pre-setup TC saat script dibuat. Dipakai: SKU `{Fixture.hardwareStock.p16.a[4].sku}` (Long Range) dengan 18 unit Available dan 1 Waiting for Approval (Pre-setup #17), 7 unit In Use (Pre-setup #18), 12 sesi Event Log (Pre-setup #20); Stock List 30 SKU (Pre-setup #16); Approvals Tab Active 12 Subject (Pre-setup #21) dan Tab History 12 Subject (Pre-setup #22). Tidak ada data yang diubah.

- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<kunci>`, identitas data bukan rahasia; berkas fixture belum ada dan dibuat tim FE/BE dari tabel Data Uji Pre-setup TC; nilai tidak ditulis ulang di spec ini):

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | `{Fixture.hardwareStock.account.p01.totalControl.email}` | No 1 | email akun Pre-setup No 1 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | `{Fixture.hardwareStock.p16.a[4].sku}` | No 16, 17, 18, Tabel A baris 4 | kode SKU Handheld Reader Long Range (25 Total Registered: 18 Available, 7 In Use) | `Fixture.hardwareStock.p16.a[4].sku` |

- Surface yang diuji (parameter langkah 1 sampai 6):

| TC | Surface | Cara membuka | Toast error yang diharapkan |
|---|---|---|---|
| TC-254 | Stock List | Halaman awal Hardware > Stock (dibuka hook `beforeEach`) | `Error, failed to download Hardware-Stock.` |
| TC-313 | Stock Detail Tab Available | Klik row action `Detail` pada SKU `{Fixture.hardwareStock.p16.a[4].sku}`, Tab `Available` aktif | `Error, failed to download Hardware-Stock-{Fixture.hardwareStock.p16.a[4].sku}.` |
| TC-365 | Stock Detail Tab In Use | Klik Tab `In Use` | `Error, failed to download Hardware-Stock-InUse-{Fixture.hardwareStock.p16.a[4].sku}.` |
| TC-511 | Popup Event Log | Klik Tab `Available`, lalu klik icon `[Event Log]` di toolbar | `Error, failed to download Hardware-Stock-EventLog-{Fixture.hardwareStock.p16.a[4].sku}.` |
| TC-413 | Approvals Tab Active | Buka Approvals > Hardware Stock, Tab `Active` aktif | `Error, failed to download Hardware-Stock.` |
| TC-463 | Approvals Tab History | Klik Tab `History` | `Error, failed to download Hardware-Stock.` |

## Test Steps

Untuk setiap baris tabel Prerequisites (enam surface berurutan dari atas ke bawah), lakukan langkah 1 sampai 6:

1. Buka surface sesuai kolom Cara membuka (Stock List tidak perlu dibuka karena sudah dibuka hook)
2. Pasang intercept respons download dengan status 500
3. Klik icon Download, pilih `Download as CSV`
4. Verifikasi toast error sesuai kolom Toast error yang diharapkan
5. Verifikasi tidak ada berkas terunduh
6. Lepas intercept; tutup popup Event Log dengan `[X]` bila surface adalah popup

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-254, 313, 365, 413, 463, 511, 580). Tidak ada TC hanya-BE di spec ini. Spec kelas b.
- Langkah 1 sampai 6 diulang enam kali (ekspansi 36 langkah), di atas sekitar 35 langkah. Alasan: enam surface satu kelas (kegagalan download) dengan alur identik dan parameter di tabel; tiap iterasi berdiri sendiri.
- TC-580 memerintahkan intercept download pada tiap surface dan mengharapkan toast per surface (butir a sampai e: Stock List, Tab Available, Tab In Use, Event Log, Approvals). Kelima asersi TC-580 dipenuhi oleh iterasi yang sama: butir a oleh iterasi TC-254, b oleh TC-313, c oleh TC-365, d oleh TC-511, e oleh TC-413 dan TC-463. Satu alur dipakai bersama karena langkah dan Expected TC-580 identik dengan TC per surface; id TC-580 tetap di `sourceTc`.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 (navigasi), 2 dan 6 (memasang dan melepas intercept). Asersi absence berkas (langkah 5) memakai toast error pada langkah 4 sebagai anchor positif bahwa respons gagal sudah diproses (butir 8b nomor 2 dan 11).
- Temuan untuk QA:
  - TC-580 duplikat dengan TC-254, 313, 365, 413, 463, dan 511 (surface dan toast yang sama); disarankan menandai TC-580 sebagai ringkasan atau menghapus duplikat.
  - Urutan surface dalam tabel mengikuti dataset (Event Log sebelum Approvals) dan bukan urutan nomor TC.

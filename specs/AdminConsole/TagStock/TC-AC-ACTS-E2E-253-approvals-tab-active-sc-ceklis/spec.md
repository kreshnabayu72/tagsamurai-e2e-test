---
id: TC-AC-ACTS-E2E-253-approvals-tab-active-sc-ceklis
title: "Approvals Tab Active: Setup Column: Ceklis dan Unceklis Kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-595
coverage:
  web: automated
---

# Approvals Tab Active: Setup Column: Ceklis dan Unceklis Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Halaman kerja spec ini adalah Approvals > TAG Stock, dibuka oleh langkah 1 dan 2.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Approvals > TAG Stock > Tab Active: sedikitnya 5 Subject Register Duplicate dan Activation Collision dengan sedikitnya dua nilai distinct pada tiap kolom (SKU `Fixture.tagStock.skuRfid`, Existing Record `TAG-4F7K2XQ9`, Requested By `PT Principal Utama (Principal)`, `PT Maju Bersama (Distributor)`, dan `PT ABC Logistics (Client)`, serta satu Subject Client BYO tanpa SKU). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Tabel "Kolom Hideable Tab Active":

  | Kolom |
  |---|
  | `Type` |
  | `Device Name (SKU)` |
  | `Category` |
  | `Matched Identifier` |
  | `Existing Record` |
  | `Requested By` |
  | `Requested At` |

- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pemulihan Setup Column: hook `before` dan `after` menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE.
- State global: konfigurasi kolom Setup Column yang disimpan spec dipulihkan di hook `before` dan `after` (menghapus preferensi kolom di browser).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar
2. Klik Tab `Active`

### TC-AC-ACTS-595: Setup Column Approvals > TAG Stock > Tab Active: ceklis dan unceklis kolom (kelas Hideable)

3. Klik header kolom Column Visibility (⋯)
4. Klik `[Setup Column]`
Langkah 5 sampai 8 diulang untuk setiap baris tabel "Kolom Hideable Tab Active" pada Prerequisites (7 iterasi).

5. Hilangkan centang kolom `<Kolom>` di Setup Column
6. Verifikasi preview langsung menyembunyikan kolom `<Kolom>`
7. Centang kembali kolom `<Kolom>`
8. Verifikasi preview langsung menampilkan kolom `<Kolom>` kembali
9. Hilangkan centang kolom `Type` dan `Device Name (SKU)`, klik `[Save]`
10. Verifikasi kolom `Type` dan `Device Name (SKU)` hilang dari tabel
11. Muat ulang halaman (F5)
12. Verifikasi kolom `Type` dan `Device Name (SKU)` tetap hilang setelah F5
13. Klik header kolom Column Visibility (⋯)
14. Klik `[Setup Column]`
15. Centang kembali kolom `Type` dan `Device Name (SKU)`, klik `[Save]`
16. Verifikasi kolom `Type` dan `Device Name (SKU)` tampil lagi di tabel

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 membuka Approvals > TAG Stock dan Tab `Active`; tidak ada `Verifikasi` karena hanya menyiapkan halaman kerja.
- Perulangan bagian 8b butir 7: langkah 5 sampai 8 diulang untuk setiap baris tabel "Kolom Hideable Tab Active" (7 iterasi); parameter tiap iterasi ada di tabel itu pada Prerequisites, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa.
- Alasan di atas sekitar 35 langkah: spec ini 40 langkah dihitung dengan ekspansi; seluruh blok memakai satu kelas harness dan satu dataset seed, dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang diulang per baris tabel sah menurut bagian 8b butir 7.
- Temuan untuk QA (S-15):

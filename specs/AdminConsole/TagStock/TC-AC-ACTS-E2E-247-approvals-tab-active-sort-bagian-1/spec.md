---
id: TC-AC-ACTS-E2E-247-approvals-tab-active-sort-bagian-1
title: "Approvals Tab Active: Sort 3-State Per Kelas Kolom (Bagian 1)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-575
  - TC-AC-ACTS-576
coverage:
  web: automated
---

# Approvals Tab Active: Sort 3-State Per Kelas Kolom (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Halaman kerja spec ini adalah Approvals > TAG Stock, dibuka oleh langkah 1 dan 2.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Approvals > TAG Stock > Tab Active: sedikitnya 5 Subject Register Duplicate dan Activation Collision dengan sedikitnya dua nilai distinct pada tiap kolom (SKU `Fixture.tagStock.skuRfid`, Existing Record `TAG-4F7K2XQ9`, Requested By `PT Principal Utama (Principal)`, `PT Maju Bersama (Distributor)`, dan `PT ABC Logistics (Client)`, serta satu Subject Client BYO tanpa SKU). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Tabel "Kolom sort kelas teks Tab Active":

  | Kolom | Urutan Ascending |
  |---|---|
  | `Device Name (SKU)` | A-Z, case-insensitive |
  | `Category` | A-Z, case-insensitive |
  | `Matched Identifier` | A-Z, case-insensitive |
  | `Existing Record` | A-Z, case-insensitive |
  | `Requested By` | A-Z, case-insensitive |

- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar
2. Klik Tab `Active`
3. Verifikasi tabel memuat sedikitnya satu baris Subject

### TC-AC-ACTS-575: Sort 3-state kelas badge di Approvals > TAG Stock > Tab Active: Type

4. Klik header kolom `Type` sekali
5. Verifikasi urutan kolom `Type` Ascending (↑) (A-Z menurut label badge)
6. Klik header kolom `Type` kedua kali
7. Verifikasi urutan kolom `Type` Descending (↓), terbalik dari urutan Ascending
8. Klik header kolom `Type` ketiga kali
9. Verifikasi indikator sort kolom `Type` hilang dan tabel kembali ke urutan default Requested At Oldest First

### TC-AC-ACTS-576: Sort 3-state kelas teks di Approvals > TAG Stock > Tab Active: Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By

Langkah 10 sampai 15 diulang untuk setiap baris tabel "Kolom sort kelas teks Tab Active" pada Prerequisites (5 iterasi).

10. Klik header kolom `<Kolom>` sekali
11. Verifikasi urutan kolom `<Kolom>` Ascending (↑) (<Urutan Ascending>)
12. Klik header kolom `<Kolom>` kedua kali
13. Verifikasi urutan kolom `<Kolom>` Descending (↓), terbalik dari urutan Ascending
14. Klik header kolom `<Kolom>` ketiga kali
15. Verifikasi indikator sort kolom `<Kolom>` hilang dan tabel kembali ke urutan default Requested At Oldest First

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 membuka Approvals > TAG Stock dan Tab `Active`; tidak ada `Verifikasi` karena hanya menyiapkan halaman kerja.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Perulangan bagian 8b butir 7: langkah 10 sampai 15 diulang untuk setiap baris tabel "Kolom sort kelas teks Tab Active" (5 iterasi); parameter tiap iterasi ada di tabel itu pada Prerequisites, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa.
- Alasan di atas sekitar 35 langkah: spec ini 39 langkah dihitung dengan ekspansi; seluruh blok memakai satu kelas harness dan satu dataset seed, dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang diulang per baris tabel sah menurut bagian 8b butir 7.
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.

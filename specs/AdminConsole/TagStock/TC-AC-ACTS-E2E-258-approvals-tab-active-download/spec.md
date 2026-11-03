---
id: TC-AC-ACTS-E2E-258-approvals-tab-active-download
title: "Approvals Tab Active: Download CSV dan XLSX"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-607
  - TC-AC-ACTS-608
coverage:
  web: automated
---

# Approvals Tab Active: Download CSV dan XLSX

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Halaman kerja spec ini adalah Approvals > TAG Stock, dibuka oleh langkah 1 dan 2.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Approvals > TAG Stock > Tab Active: sedikitnya 5 Subject Register Duplicate dan Activation Collision dengan sedikitnya dua nilai distinct pada tiap kolom (SKU `Fixture.tagStock.skuRfid`, Existing Record `TAG-4F7K2XQ9`, Requested By `PT Principal Utama (Principal)`, `PT Maju Bersama (Distributor)`, dan `PT ABC Logistics (Client)`, serta satu Subject Client BYO tanpa SKU). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Berkas hasil unduhan diasersi nama dan ekstensinya saja; isi sel berkas XLSX (kelas f) ada di spec 260.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pembaca nama berkas unduhan di browser, disediakan tim FE.
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar
2. Klik Tab `Active`

### TC-AC-ACTS-607: Download Approvals > TAG Stock > Tab Active sebagai CSV: nama file dan extension

3. Klik icon Download, pilih `Download as CSV`
4. Verifikasi tidak muncul toast sukses
5. Verifikasi file terunduh bernama `TAG-Stock_YYYYMMDD_HHmmss.csv`

### TC-AC-ACTS-608: Download Approvals > TAG Stock > Tab Active sebagai XLSX: nama file dan extension

6. Klik icon Download, pilih `Download as XLSX`
7. Verifikasi tidak muncul toast sukses
8. Verifikasi file terunduh bernama `TAG-Stock_YYYYMMDD_HHmmss.xlsx`

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 membuka Approvals > TAG Stock dan Tab `Active`; tidak ada `Verifikasi` karena hanya menyiapkan halaman kerja.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Isi sel berkas XLSX Tab Active (TC-AC-ACTS-609) ada di spec 260.
- Temuan untuk QA (S-15):

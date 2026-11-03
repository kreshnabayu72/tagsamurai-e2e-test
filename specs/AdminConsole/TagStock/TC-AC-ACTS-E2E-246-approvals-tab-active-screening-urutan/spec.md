---
id: TC-AC-ACTS-E2E-246-approvals-tab-active-screening-urutan
title: "Approvals Tab Active: Screening Header, Kolom, Footer dan Urutan Default"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-573
  - TC-AC-ACTS-574
coverage:
  web: automated
---

# Approvals Tab Active: Screening Header, Kolom, Footer dan Urutan Default

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Halaman kerja spec ini adalah Approvals > TAG Stock, dibuka oleh langkah 1 dan 2.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Approvals > TAG Stock > Tab Active: sedikitnya 5 Subject Register Duplicate dan Activation Collision dengan sedikitnya dua nilai distinct pada tiap kolom (SKU `Fixture.tagStock.skuRfid`, Existing Record `TAG-4F7K2XQ9`, Requested By `PT Principal Utama (Principal)`, `PT Maju Bersama (Distributor)`, dan `PT ABC Logistics (Client)`, serta satu Subject Client BYO tanpa SKU). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar
2. Klik Tab `Active`

### TC-AC-ACTS-573: Screening Approvals > TAG Stock > Tab Active: header, kolom, footer

3. Verifikasi breadcrumb `Approvals > TAG Stock` tampil sebagai dua segmen statis yang tidak bisa diklik
4. Verifikasi Tab `Active` dan `History` tampil dengan `Active` terpilih
5. Verifikasi Table Tools memuat `Search`, `Filter`, `Download`
6. Verifikasi kolom `Type`, `Device Name (SKU)`, `Category`, `Matched Identifier`, `Existing Record`, `Requested By`, `Requested At` sortable
7. Verifikasi kolom Column Visibility (⋯) tidak dapat disortir dan menu baris per baris memuat row action
8. Verifikasi footer memuat pagination default 10 data per halaman

### TC-AC-ACTS-574: Default sort Approvals > TAG Stock > Tab Active: Requested At Oldest First

9. Verifikasi baris terurut Requested At Oldest First saat halaman dibuka
10. Verifikasi tidak ada panah sort aktif pada kolom lain

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 membuka Approvals > TAG Stock dan Tab `Active`; tidak ada `Verifikasi` karena hanya menyiapkan halaman kerja.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA (S-15):

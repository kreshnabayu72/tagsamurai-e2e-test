---
id: TC-AC-ACTS-E2E-182-tab-in-use-screening-urutan
title: "Detail SKU Tab In Use: Screening Header, Kolom, Footer dan Urutan Default"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-433
  - TC-AC-ACTS-434
coverage:
  web: automated
---

# Detail SKU Tab In Use: Screening Header, Kolom, Footer dan Urutan Default

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki unit In Use milik beberapa Client (sedikitnya 5 unit) dengan Status Available dan Damaged/Missing dan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit `TAG-5D8J2LM6` milik `PT Maju Bersama`, unit ber-Identifier EPC `E280...` dan UID `A1B2...`, dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab In Use, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, klik Tab `In Use`

### TC-AC-ACTS-433: Screening header, kolom, footer

2. Verifikasi Header: Breadcrumb `TAG > Stock > Detail`, header SKU, Summary bar, Tab `In Use` aktif
3. Verifikasi Header Table Tools: `Search | Filter | Download`
4. Verifikasi Body kolom berurutan: `TAG Code (sortable) | Identifier (sortable) | Identifier (UID, RFID) (sortable) | Client (sortable) | Status (sortable) | Registered At (sortable) | Registered By (sortable) | Activated At (sortable) | Column Visibility (⋯) (unsortable)`
5. Verifikasi Footer pagination default 10 data per halaman

### TC-AC-ACTS-434: Default sort Activated At Newest First

6. Verifikasi tabel memuat sedikitnya satu baris data
7. Verifikasi baris terurut Activated At Newest First saat halaman dibuka
8. Verifikasi tidak ada panah sort aktif pada kolom lain

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AC-ACTS-433 dan TC-AC-ACTS-434 memiliki langkah pembuka yang sama dan diamati pada satu pembukaan Tab In Use (langkah 1); tidak ada navigasi ulang (S-10).
- Temuan untuk QA: butir Expected b TC-AC-ACTS-433 menyisipkan keterangan "(sortable)" dan "(unsortable)" pada nama kolom; spec mengasersinya sebagai bagian daftar kolom, bukan uji sort (uji sort ada di spec 183 sampai 184).

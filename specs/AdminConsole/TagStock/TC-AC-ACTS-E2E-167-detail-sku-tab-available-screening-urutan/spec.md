---
id: TC-AC-ACTS-E2E-167-detail-sku-tab-available-screening-urutan
title: "Detail SKU Tab Available: Screening Header, Kolom, Footer dan Urutan Default"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-388
  - TC-AC-ACTS-389
coverage:
  web: automated
---

# Detail SKU Tab Available: Screening Header, Kolom, Footer dan Urutan Default

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki sedikitnya 5 unit berstatus Available dan Damaged/Missing dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit Available `TAG-4F7K2XQ9` (Data Dinamis #5, U1), unit ber-Identifier EPC `E280...` dan UID `A1B2...` (Data Dinamis #1), dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab Available, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`; pastikan Tab `Available` aktif

### TC-AC-ACTS-388: Screening header, kolom, footer

2. Verifikasi Header: Breadcrumb `TAG > Stock > Detail`, header SKU, Summary bar `Total Registered | Available | In Use`, Tab `Available | In Use`
3. Verifikasi Header Table Tools: `Search | Filter | Download | [Event Log] | [Delete by Scan] | [Audit TAG] | [Add Stock]`
4. Verifikasi Body kolom berurutan: `TAG Code (sortable) | Identifier (sortable) | Identifier (UID, RFID) (sortable) | Status (sortable) | Registered At (sortable) | Registered By (sortable) | Column Visibility (⋯) (unsortable)`
5. Verifikasi Footer pagination default 10 data per halaman
6. Verifikasi tidak ada info banner kuota alokasi di atas tabel
7. Verifikasi tidak ada tab `Allocation History`

### TC-AC-ACTS-389: Default sort Registered At Newest First

8. Verifikasi tabel memuat sedikitnya satu baris data
9. Verifikasi baris terurut Registered At Newest First saat halaman dibuka
10. Verifikasi tidak ada panah sort aktif pada kolom lain

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AC-ACTS-388 dan TC-AC-ACTS-389 memiliki langkah pembuka yang sama dan diamati pada satu pembukaan Detail SKU (langkah 1); tidak ada navigasi ulang (S-10).
- Absence pada TC-AC-ACTS-388 (banner kuota, tab `Allocation History`) memakai Header yang sudah diasersi (Breadcrumb, Summary bar, Tab) sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA: butir Expected b TC-AC-ACTS-388 menyisipkan keterangan "(sortable)" dan "(unsortable)" pada nama kolom; spec mengasersinya sebagai bagian dari daftar kolom, bukan sebagai uji sort (uji sort ada di spec 168 dan 169).

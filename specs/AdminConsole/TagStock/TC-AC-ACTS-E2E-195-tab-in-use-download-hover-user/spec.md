---
id: TC-AC-ACTS-E2E-195-tab-in-use-download-hover-user
title: "Detail SKU Tab In Use: Download CSV dan XLSX; Hover Nama User"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-468
  - TC-AC-ACTS-469
  - TC-AC-ACTS-471
coverage:
  web: automated
---

# Detail SKU Tab In Use: Download CSV dan XLSX; Hover Nama User

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki unit In Use milik beberapa Client (sedikitnya 5 unit) dengan Status Available dan Damaged/Missing dan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit `TAG-5D8J2LM6` milik `PT Maju Bersama`, unit ber-Identifier EPC `E280...` dan UID `A1B2...`, dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab In Use, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Data TC-AC-ACTS-471: User hover `Budi Santoso` (Data Dinamis #3).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, klik Tab `In Use`

### TC-AC-ACTS-468: Download CSV nama file dan extension

2. Klik icon Download
3. Pilih `Download as CSV`
4. Verifikasi tidak muncul toast sukses
5. Verifikasi file terunduh bernama `TAG-Stock-InUse-RFID-ASSET-CORE-R5.csv`

### TC-AC-ACTS-469: Download XLSX nama file dan extension

6. Klik icon Download
7. Pilih `Download as XLSX`
8. Verifikasi tidak muncul toast sukses
9. Verifikasi file terunduh bernama `TAG-Stock-InUse-RFID-ASSET-CORE-R5.xlsx`

### TC-AC-ACTS-471: Hover nama user kolom Registered By

10. Hover nama user `Budi S` di kolom `Registered By`
11. Verifikasi kolom menampilkan `Budi S` (first name lengkap dan inisial last name)
12. Verifikasi tooltip menampilkan nama lengkap `Budi Santoso`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini hanya mengasersi nama berkas dan ekstensi; isi sel berkas (TC-AC-ACTS-470, kelas f) ada di spec 265.
- Pengamatan toast sukses (absence state sementara) diletakkan segera sesudah pemicu dan sebelum asersi berkas terunduh (bagian 8b butir 11).

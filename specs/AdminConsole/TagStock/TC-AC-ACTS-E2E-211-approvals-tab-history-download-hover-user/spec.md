---
id: TC-AC-ACTS-E2E-211-approvals-tab-history-download-hover-user
title: "Approvals Tab History: Download CSV dan XLSX; Hover Nama User"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-651
  - TC-AC-ACTS-652
  - TC-AC-ACTS-654
coverage:
  web: automated
---

# Approvals Tab History: Download CSV dan XLSX; Hover Nama User

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya. Spec ini membuka Approvals > TAG Stock lewat sidebar pada langkah 1.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data (disediakan fixture BE): Tab History memuat Subject Approved, Rejected, dan Canceled (sedikitnya 5 baris) dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; Subject berisi Type `Register Duplicate` dan `Activation Collision`, SKU `BLE-BEACON-ALPHA-B1` (Category `BLE - Object TAG`) dan `RFID-ASSET-CORE-R5` (Category `RFID - Object TAG`), Matched Identifier ber-UID `A1B2C3D4E5F6` (mengandung `D4E5`), Existing Record `TAG-9N1Q6VX3`, TAG Code baru `TAG-6R9V3ZL4`, Requested By `PT ABC Logistics (Client)` dan `PT Maju Bersama (Distributor)`, dan Approver `Andi Wijaya` (Data Dinamis #3). `N` = jumlah total baris Tab History, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Data: nama berkas memakai waktu unduh (`YYYYMMDD_HHmmss`). User hover (TC-AC-ACTS-654): `Andi Wijaya` (Data Dinamis #3).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar, klik Tab `History`

### TC-AC-ACTS-651: Download CSV nama file dan extension

2. Klik icon Download
3. Pilih `Download as CSV`
4. Verifikasi tidak muncul toast sukses
5. Verifikasi file terunduh bernama `TAG-Stock_YYYYMMDD_HHmmss.csv` (tanggal dan jam waktu unduh)

### TC-AC-ACTS-652: Download XLSX nama file dan extension

6. Klik icon Download
7. Pilih `Download as XLSX`
8. Verifikasi tidak muncul toast sukses
9. Verifikasi file terunduh bernama `TAG-Stock_YYYYMMDD_HHmmss.xlsx` (tanggal dan jam waktu unduh)

### TC-AC-ACTS-654: Hover nama user kolom Approver

10. Hover nama user `Andi W` di kolom `Approver`
11. Verifikasi kolom menampilkan `Andi W` (first name lengkap dan inisial last name)
12. Verifikasi tooltip menampilkan nama lengkap `Andi Wijaya`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini hanya mengasersi nama berkas dan ekstensi; isi sel berkas (TC-AC-ACTS-653, kelas f) ada di spec 265.
- Pengamatan toast sukses (absence state sementara) diletakkan segera sesudah pemicu dan sebelum asersi berkas terunduh (bagian 8b butir 11).
- Temuan untuk QA: (1) Nama berkas TC-AC-ACTS-651 dan 652 berpola `TAG-Stock_YYYYMMDD_HHmmss` (tidak memuat tab maupun SKU), berbeda dengan pola Detail SKU (`TAG-Stock-Available-<SKU>` dan `TAG-Stock-InUse-<SKU>`); spec mengikuti TC. (2) Perbandingan nama berkas dengan waktu unduh (toleransi satu menit) tidak disebut TC.

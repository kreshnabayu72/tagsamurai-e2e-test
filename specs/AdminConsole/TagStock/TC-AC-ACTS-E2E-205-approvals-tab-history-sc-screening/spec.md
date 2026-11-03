---
id: TC-AC-ACTS-E2E-205-approvals-tab-history-sc-screening
title: "Approvals Tab History: Setup Column: Screening Overlay dan Popup"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-637
  - TC-AC-ACTS-638
coverage:
  web: automated
---

# Approvals Tab History: Setup Column: Screening Overlay dan Popup

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya. Spec ini membuka Approvals > TAG Stock lewat sidebar pada langkah 1.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data (disediakan fixture BE): Tab History memuat Subject Approved, Rejected, dan Canceled (sedikitnya 5 baris) dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; Subject berisi Type `Register Duplicate` dan `Activation Collision`, SKU `BLE-BEACON-ALPHA-B1` (Category `BLE - Object TAG`) dan `RFID-ASSET-CORE-R5` (Category `RFID - Object TAG`), Matched Identifier ber-UID `A1B2C3D4E5F6` (mengandung `D4E5`), Existing Record `TAG-9N1Q6VX3`, TAG Code baru `TAG-6R9V3ZL4`, Requested By `PT ABC Logistics (Client)` dan `PT Maju Bersama (Distributor)`, dan Approver `Andi Wijaya` (Data Dinamis #3). `N` = jumlah total baris Tab History, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Konfigurasi kolom Setup Column yang disimpan spec ini dihapus (preferensi kolom tabel di browser) di hook `before` dan `after`, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar, klik Tab `History`

### TC-AC-ACTS-637: Setup Column screening Overlay Column Visibility

2. Klik header kolom Column Visibility (⋯)
3. Verifikasi Overlay memuat tombol `[Setup Column]`
4. Verifikasi Overlay memuat daftar kolom berurutan `Type`, `Device Name (SKU)`, `Category`, `Matched Identifier`, `Existing Record`, `Requested By`, `Approval`, `Approver`, `TAG Code`, `Requested At`, `Resolved At`
5. Verifikasi tiap kolom berstatus checkbox checked dan enabled (Hideable)
6. Verifikasi tiap kolom memiliki drag handle
7. Verifikasi Overlay tidak menutup tabel (tanpa backdrop)

### TC-AC-ACTS-638: Setup Column screening Popup dan Live Preview

8. Klik `[Setup Column]`
9. Verifikasi Popup `Setup Column`: Title `Setup Column` dan deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
10. Verifikasi Popup `Setup Column` memuat tombol close (X)
11. Verifikasi Body memuat daftar kolom `Type`, `Device Name (SKU)`, `Category`, `Matched Identifier`, `Existing Record`, `Requested By`, `Approval`, `Approver`, `TAG Code`, `Requested At`, `Resolved At`
12. Verifikasi tiap kolom pada daftar memiliki checkbox
13. Verifikasi tiap kolom pada daftar memiliki drag handle
14. Verifikasi tiap kolom pada daftar memiliki icon Pin
15. Verifikasi Live Preview urutan header tampil
16. Verifikasi Footer memuat `[Reset to Default]` dan `[Save]` rata kanan
17. Verifikasi Footer tanpa `[Cancel]`
18. Klik (X) untuk menutup Popup `Setup Column`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Konfigurasi Setup Column yang disimpan spec ini dihapus lewat preferensi kolom di browser pada hook `before` dan `after`, bukan lewat `[Reset to Default]` (bagian 4 konvensi).
- Langkah penghubung (S-03): menutup Popup `Setup Column` sesudah screening.
- Temuan untuk QA: TC-AC-ACTS-637 menyebut kolom Column Visibility (⋯) sebagai header; daftar kolom pada Overlay tidak memuat kolom itu sendiri.

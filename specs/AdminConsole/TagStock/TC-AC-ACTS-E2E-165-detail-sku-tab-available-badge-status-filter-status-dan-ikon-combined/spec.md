---
id: TC-AC-ACTS-E2E-165-detail-sku-tab-available-badge-status-filter-status-dan-ikon-combined
title: "Detail SKU Tab Available: Badge Status, Filter Status, Ikon Combined, dan Popup Combined TAG Read-Only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-376
  - TC-AC-ACTS-377
  - TC-AC-ACTS-379
  - TC-AC-ACTS-380
  - TC-AC-ACTS-381
coverage:
  web: automated
---

# Detail SKU Tab Available: Badge Status, Filter Status, Ikon Combined, dan Popup Combined TAG Read-Only

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki sedikitnya 5 unit berstatus Available dan Damaged/Missing dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit Available `TAG-4F7K2XQ9` (Data Dinamis #5, U1), unit ber-Identifier EPC `E280...` dan UID `A1B2...` (Data Dinamis #1), dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab Available, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Data Pre-setup tambahan: satu unit Combined (Combined dengan satu unit NFC) dan satu unit standalone pada SKU yang sama; unit Available dan Damaged/Missing ada.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`; pastikan Tab `Available` aktif

### TC-AC-ACTS-376: Badge Status dua severity

2. Verifikasi tabel memuat sedikitnya satu baris data
3. Verifikasi badge Status `Available` bergaya success
4. Verifikasi badge Status `Damaged/Missing` bergaya danger
5. Verifikasi kolom Status tidak memuat nilai `Waiting for Approval` maupun `Combined` (Status murni kondisi fisik)

### TC-AC-ACTS-377: Filter Status tanpa opsi Waiting, Combined, dan In Use

6. Klik icon Filter, buka dropdown `Status`
7. Verifikasi opsi dropdown `Status` hanya `Available` dan `Damaged/Missing`
8. Verifikasi dropdown `Status` tidak memuat opsi `Waiting for Approval`, `In Combined Set`, `In Use`, atau `Reserved`
9. Klik icon Filter untuk menutup panel

### TC-AC-ACTS-379: Ikon Combined

10. Verifikasi ikon 🔗 tampil pada TAG Code unit Combined
11. Verifikasi unit standalone tidak memiliki ikon 🔗 pada TAG Code
12. Verifikasi Status unit Combined tetap `Available` atau `Damaged/Missing`

### TC-AC-ACTS-380: Popup Combined TAG

13. Klik ikon 🔗 pada TAG Code unit Combined
14. Verifikasi Popup `Combined TAG` tampil dengan tombol (X)
15. Verifikasi Popup `Combined TAG` tanpa footer
16. Verifikasi daftar memuat satu pasangan dengan ikon TAG Type, Code (EPC Code untuk RFID, UID Code untuk NFC), dan Device Name

### TC-AC-ACTS-381: Popup Combined TAG read-only

17. Klik baris sibling pada daftar popup
18. Verifikasi tidak ada aksi atau navigasi dari baris sibling
19. Klik (X)
20. Verifikasi Popup `Combined TAG` tertutup

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (S-03): langkah menutup panel Filter pada TC-AC-ACTS-377. Pembanding generik "sedikitnya satu baris" pada TC-AC-ACTS-376 mengikuti bagian 8b butir 2.
- Spec membaca data Pre-setup tanpa mengubahnya (S-06).
- Temuan untuk QA: TC-AC-ACTS-379 menyebut "satu unit Combined dengan NFC" tanpa menamai identifier unitnya; spec mencarinya lewat ikon 🔗 pada TAG Code. TC-AC-ACTS-376 butir b ("Status murni kondisi fisik") adalah penjelasan dari butir a; diasersi sebagai absence nilai `Waiting for Approval` dan `Combined` di kolom Status.

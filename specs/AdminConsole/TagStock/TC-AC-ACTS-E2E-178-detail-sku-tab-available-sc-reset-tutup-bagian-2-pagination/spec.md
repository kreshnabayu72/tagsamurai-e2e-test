---
id: TC-AC-ACTS-E2E-178-detail-sku-tab-available-sc-reset-tutup-bagian-2-pagination
title: "Detail SKU Tab Available: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 2)"
priority: Low
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-416
coverage:
  web: automated
---

# Detail SKU Tab Available: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 2)

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki sedikitnya 5 unit berstatus Available dan Damaged/Missing dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit Available `TAG-4F7K2XQ9` (Data Dinamis #5, U1), unit ber-Identifier EPC `E280...` dan UID `A1B2...` (Data Dinamis #1), dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab Available, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Konfigurasi kolom Setup Column yang disimpan spec ini dihapus (preferensi kolom tabel di browser) di hook `before` dan `after`, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`; pastikan Tab `Available` aktif
2. Klik header kolom Column Visibility (⋯)
3. Klik `[Setup Column]`

### TC-AC-ACTS-416: Pin ke-4 diblokir di Setup Column

4. Klik icon Pin pada kolom `TAG Code`, `Identifier`, dan `Identifier (UID, RFID)` (3 kolom)
5. Arahkan kursor ke icon Pin kolom `Status` dan coba klik
6. Verifikasi icon Pin kolom `Status` disabled dan kolom tidak ter-pin
7. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
8. Klik icon Pin kolom `TAG Code` lagi (unpin)
9. Verifikasi icon Pin kolom lain aktif kembali
10. Klik icon (X) untuk menutup Popup `Setup Column`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Konfigurasi Setup Column yang disimpan spec ini dihapus lewat preferensi kolom di browser pada hook `before` dan `after`, bukan lewat `[Reset to Default]` (bagian 4 konvensi).
- Langkah penghubung (S-03): menutup Popup `Setup Column` tanpa Save sesudah TC-AC-ACTS-416.
- Temuan untuk QA: TC-AC-ACTS-416 Expected c "icon Pin kolom lain aktif kembali" tidak menyebut kolom yang dicek; spec mengasersi kolom lain tanpa menyebut nama.

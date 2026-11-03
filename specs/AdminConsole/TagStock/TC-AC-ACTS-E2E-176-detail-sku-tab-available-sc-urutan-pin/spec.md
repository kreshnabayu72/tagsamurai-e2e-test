---
id: TC-AC-ACTS-E2E-176-detail-sku-tab-available-sc-urutan-pin
title: "Detail SKU Tab Available: Setup Column: Geser Urutan serta Pin dan Unpin"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-411
  - TC-AC-ACTS-412
coverage:
  web: automated
---

# Detail SKU Tab Available: Setup Column: Geser Urutan serta Pin dan Unpin

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
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

### TC-AC-ACTS-411: Setup Column geser urutan kolom

4. Geser kolom `TAG Code` ke bawah kolom `Identifier`
5. Verifikasi Live Preview mengikuti urutan baru
6. Klik `[Save]`
7. Verifikasi tabel mengikuti urutan baru
8. Muat ulang halaman (F5)
9. Verifikasi urutan baru bertahan setelah F5

### TC-AC-ACTS-412: Setup Column pin dan unpin kolom

10. Klik header kolom Column Visibility (⋯)
11. Klik `[Setup Column]`
12. Klik icon Pin kolom `TAG Code`
13. Klik `[Save]`
14. Scroll tabel secara horizontal
15. Verifikasi kolom ter-pin tetap diam di sisi kiri saat scroll horizontal
16. Klik header kolom Column Visibility (⋯)
17. Klik `[Setup Column]`
18. Klik icon Pin kolom `TAG Code` lagi (unpin)
19. Klik `[Save]`
20. Scroll tabel secara horizontal
21. Verifikasi kolom `TAG Code` ikut bergeser lagi setelah unpin

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Konfigurasi Setup Column yang disimpan spec ini dihapus lewat preferensi kolom di browser pada hook `before` dan `after`, bukan lewat `[Reset to Default]` (bagian 4 konvensi).
- Langkah penghubung (S-03): scroll horizontal kedua sebelum `Verifikasi` unpin membawa tabel ke keadaan yang diasersi (S-14).
- Temuan untuk QA: TC-AC-ACTS-412 tidak menyebut lebar viewport yang membuat tabel dapat di-scroll horizontal; langkah 9 TC tidak memuat scroll sesudah unpin padahal Expected b memerlukannya.

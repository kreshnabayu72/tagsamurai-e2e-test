---
id: TC-AC-ACTS-E2E-189-tab-in-use-filter-bagian-2-sc-screening
title: "Detail SKU Tab In Use: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 2); Setup Column: Screening Overlay dan Popup"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-452
  - TC-AC-ACTS-453
  - TC-AC-ACTS-454
  - TC-AC-ACTS-455
coverage:
  web: automated
---

# Detail SKU Tab In Use: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 2); Setup Column: Screening Overlay dan Popup

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki unit In Use milik beberapa Client (sedikitnya 5 unit) dengan Status Available dan Damaged/Missing dan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit `TAG-5D8J2LM6` milik `PT Maju Bersama`, unit ber-Identifier EPC `E280...` dan UID `A1B2...`, dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab In Use, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Konfigurasi kolom Setup Column yang disimpan spec ini dihapus (preferensi kolom tabel di browser) di hook `before` dan `after`, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, klik Tab `In Use`

### TC-AC-ACTS-452: Isi opsi dropdown Filter = DISTINCT data tabel

2. Klik icon Filter
3. Buka dropdown `Client`
4. Verifikasi opsi `Client` hanya berisi nilai yang ada di baris tabel saat ini
5. Verifikasi nilai yang tidak muncul di tabel tidak menjadi opsi

### TC-AC-ACTS-453: Kombinasi AND dua field Filter

6. Pilih `PT Maju Bersama` pada `Client`
7. Pilih `Available` pada `Status`
8. Klik `[Apply]`
9. Verifikasi tabel memuat sedikitnya satu baris data
10. Verifikasi hanya baris yang memenuhi kedua kriteria (`PT Maju Bersama` dan `Available`) yang tampil
11. Klik `[Clear Field]`
12. Klik `[Apply]`
13. Klik icon Filter untuk menutup panel

### TC-AC-ACTS-454: Setup Column screening Overlay Column Visibility

14. Klik header kolom Column Visibility (⋯)
15. Verifikasi Overlay memuat tombol `[Setup Column]`
16. Verifikasi Overlay memuat daftar kolom berurutan `TAG Code`, `Identifier`, `Identifier (UID, RFID)`, `Client`, `Status`, `Registered At`, `Registered By`, `Activated At`
17. Verifikasi tiap kolom berstatus checkbox checked dan enabled (Hideable)
18. Verifikasi tiap kolom memiliki drag handle
19. Verifikasi Overlay tidak menutup tabel (tanpa backdrop)

### TC-AC-ACTS-455: Setup Column screening Popup dan Live Preview

20. Klik `[Setup Column]`
21. Verifikasi Popup `Setup Column`: Title `Setup Column` dan deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
22. Verifikasi Popup `Setup Column` memuat tombol close (X)
23. Verifikasi Body memuat daftar kolom `TAG Code`, `Identifier`, `Identifier (UID, RFID)`, `Client`, `Status`, `Registered At`, `Registered By`, `Activated At`
24. Verifikasi tiap kolom pada daftar memiliki checkbox
25. Verifikasi tiap kolom pada daftar memiliki drag handle
26. Verifikasi tiap kolom pada daftar memiliki icon Pin
27. Verifikasi Live Preview urutan header tampil
28. Verifikasi Footer memuat `[Reset to Default]` dan `[Save]` rata kanan
29. Verifikasi Footer tanpa `[Cancel]`
30. Klik (X) untuk menutup Popup `Setup Column`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Konfigurasi Setup Column yang disimpan spec ini dihapus lewat preferensi kolom di browser pada hook `before` dan `after`, bukan lewat `[Reset to Default]` (bagian 4 konvensi).
- Langkah penghubung (S-03): `[Clear Field]`, `[Apply]`, menutup panel Filter, dan menutup Popup `Setup Column` sesudah screening.
- Temuan untuk QA: TC-AC-ACTS-454 menyebut kolom Column Visibility (⋯) sebagai header; daftar kolom pada Overlay tidak memuat kolom itu sendiri. TC-AC-ACTS-452 tidak menyebut nilai Client yang tidak muncul; spec mengasersi tanpa menyebut nilai.

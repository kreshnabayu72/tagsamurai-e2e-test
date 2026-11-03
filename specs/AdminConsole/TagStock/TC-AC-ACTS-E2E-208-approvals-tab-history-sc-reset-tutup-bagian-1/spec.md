---
id: TC-AC-ACTS-E2E-208-approvals-tab-history-sc-reset-tutup-bagian-1
title: "Approvals Tab History: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 1)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-642
  - TC-AC-ACTS-643
  - TC-AC-ACTS-644
coverage:
  web: automated
---

# Approvals Tab History: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 1)

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya. Spec ini membuka Approvals > TAG Stock lewat sidebar pada langkah 1.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data (disediakan fixture BE): Tab History memuat Subject Approved, Rejected, dan Canceled (sedikitnya 5 baris) dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; Subject berisi Type `Register Duplicate` dan `Activation Collision`, SKU `BLE-BEACON-ALPHA-B1` (Category `BLE - Object TAG`) dan `RFID-ASSET-CORE-R5` (Category `RFID - Object TAG`), Matched Identifier ber-UID `A1B2C3D4E5F6` (mengandung `D4E5`), Existing Record `TAG-9N1Q6VX3`, TAG Code baru `TAG-6R9V3ZL4`, Requested By `PT ABC Logistics (Client)` dan `PT Maju Bersama (Distributor)`, dan Approver `Andi Wijaya` (Data Dinamis #3). `N` = jumlah total baris Tab History, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Konfigurasi kolom Setup Column yang disimpan spec ini dihapus (preferensi kolom tabel di browser) di hook `before` dan `after`, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar, klik Tab `History`
2. Klik header kolom Column Visibility (⋯)
3. Klik `[Setup Column]`

### TC-AC-ACTS-642: Setup Column Reset to Default

4. Sembunyikan kolom `Device Name (SKU)` dan geser kolom `Type` ke posisi lain
5. Klik `[Save]`
6. Klik header kolom Column Visibility (⋯)
7. Klik `[Setup Column]`
8. Klik `[Reset to Default]`
9. Verifikasi preview kembali ke susunan default modul (bukan ke susunan tersimpan terakhir)
10. Klik `[Save]`
11. Muat ulang halaman (F5)
12. Verifikasi susunan default bertahan setelah F5

### TC-AC-ACTS-643: Setup Column tutup dengan (X) atau Esc membuang perubahan

13. Klik header kolom Column Visibility (⋯)
14. Klik `[Setup Column]`
15. Sembunyikan kolom `Device Name (SKU)` di preview
16. Klik icon (X)
17. Verifikasi modal tertutup tanpa dialog konfirmasi
18. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir
19. Klik header kolom Column Visibility (⋯)
20. Klik `[Setup Column]`
21. Sembunyikan kolom `Device Name (SKU)` di preview
22. Tekan Esc
23. Verifikasi modal tertutup tanpa dialog konfirmasi
24. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir

### TC-AC-ACTS-644: Setup Column satu kolom tersisa tidak bisa di-uncheck

25. Klik header kolom Column Visibility (⋯)
26. Klik `[Setup Column]`
27. Hilangkan centang semua kolom kecuali satu
28. Arahkan kursor ke checkbox kolom terakhir dan coba hilangkan centangnya
29. Verifikasi checkbox kolom terakhir disabled
30. Verifikasi tooltip `At least one column must remain visible.`
31. Klik icon (X)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Konfigurasi Setup Column yang disimpan spec ini dihapus lewat preferensi kolom di browser pada hook `before` dan `after`, bukan lewat `[Reset to Default]` (bagian 4 konvensi).
- Langkah penghubung (S-03): membuka Setup Column kembali tiap TC, menutup Popup tanpa Save sesudah TC-AC-ACTS-644. State kolom dibersihkan hook `after` lewat preferensi kolom.
- Temuan untuk QA: TC-AC-ACTS-642 langkah 5 "geser `Type`" tidak menyebut tujuan geser; spec menggesernya ke posisi lain. TC-AC-ACTS-643 judul "(X) atau Esc" ditulis sebagai dua penutupan berurutan.

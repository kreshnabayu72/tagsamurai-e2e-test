---
id: TC-AC-ACTS-E2E-255-approvals-tab-active-sc-reset-tutup-bagian-1
title: "Approvals Tab Active: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 1)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-598
  - TC-AC-ACTS-599
  - TC-AC-ACTS-600
coverage:
  web: automated
---

# Approvals Tab Active: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Halaman kerja spec ini adalah Approvals > TAG Stock, dibuka oleh langkah 1 dan 2.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Approvals > TAG Stock > Tab Active: sedikitnya 5 Subject Register Duplicate dan Activation Collision dengan sedikitnya dua nilai distinct pada tiap kolom (SKU `Fixture.tagStock.skuRfid`, Existing Record `TAG-4F7K2XQ9`, Requested By `PT Principal Utama (Principal)`, `PT Maju Bersama (Distributor)`, dan `PT ABC Logistics (Client)`, serta satu Subject Client BYO tanpa SKU). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pemulihan Setup Column: hook `before` dan `after` menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE.
- State global: konfigurasi kolom Setup Column yang disimpan spec dipulihkan di hook `before` dan `after` (menghapus preferensi kolom di browser).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar
2. Klik Tab `Active`

### TC-AC-ACTS-598: Setup Column Approvals > TAG Stock > Tab Active: Reset to Default

3. Klik header kolom Column Visibility (⋯)
4. Klik `[Setup Column]`
5. Sembunyikan kolom `Device Name (SKU)` dan geser `Type`, klik `[Save]`
6. Klik header kolom Column Visibility (⋯), klik `[Setup Column]`
7. Klik `[Reset to Default]`
8. Verifikasi preview kembali ke susunan default modul (bukan ke state tersimpan terakhir)
9. Klik `[Save]`
10. Muat ulang halaman (F5)
11. Verifikasi susunan default bertahan setelah F5

### TC-AC-ACTS-599: Setup Column Approvals > TAG Stock > Tab Active: tutup dengan (X) atau Esc membuang perubahan

12. Klik header kolom Column Visibility (⋯)
13. Klik `[Setup Column]`
14. Sembunyikan kolom `Device Name (SKU)` di preview
15. Klik icon (X)
16. Verifikasi Popup Setup Column tertutup tanpa dialog konfirmasi
17. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir
18. Klik header kolom Column Visibility (⋯), klik `[Setup Column]`
19. Sembunyikan kolom `Device Name (SKU)` di preview
20. Tekan Esc
21. Verifikasi Popup Setup Column tertutup tanpa dialog konfirmasi
22. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir

### TC-AC-ACTS-600: Setup Column Approvals > TAG Stock > Tab Active: satu kolom tersisa tidak bisa di-uncheck

23. Klik header kolom Column Visibility (⋯)
24. Klik `[Setup Column]`
25. Hilangkan centang semua kolom kecuali satu
26. Arahkan kursor ke checkbox kolom terakhir
27. Verifikasi checkbox kolom terakhir disabled
28. Verifikasi tooltip `At least one column must remain visible.` tampil
29. Tutup Popup Setup Column dengan klik (X)

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 membuka Approvals > TAG Stock dan Tab `Active`; tidak ada `Verifikasi` karena hanya menyiapkan halaman kerja.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA (S-15):

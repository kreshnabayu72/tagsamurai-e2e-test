---
id: TC-FA-CAT-E2E-189-wizard-seleksi-diubah-lagi-dan-status-per-node-independen-catexcess
title: "Wizard Consolidation CatExcess: Seleksi Diubah Lagi dan Status Usable atau Excess Independen per Node"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-293
  - TC-FA-CAT-296
coverage:
  web: automated
---

# Wizard Consolidation CatExcess: Seleksi Diubah Lagi dan Status Usable atau Excess Independen per Node

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatExcess (Pre-setup #31), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #31 (CatExcess, 9 kategori, cap 5): usable `Electronics` (anak `Laptop`, `Monitor`), `Office`, `Spare Parts`; Excess `Furniture`, `Heavy Equipment`, `Vehicle`, `Old Parts`. Spec menyimpan seleksi dua kali sehingga mengubah status kategori; langkah penghubung memulihkan Pre-setup #31 lewat fixture backend yang disediakan tim FE/BE sebelum TC-FA-CAT-296, dan hook `after` memulihkannya. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Modal Changelog per Action sebelum aksi (baseline NR untuk `Restored from Excess (Category Consolidation)` dan NM untuk `Marked as Excess (Category Consolidation)`, S-12).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-293: Seleksi dapat diubah lagi selama jumlah kategori masih di atas cap

1. Klik `[Choose Categories]` pada Alert Category Consolidation
2. Centang `Keep usable` pada `Furniture`, `Heavy Equipment`, `Electronics`, `Laptop`, dan `Monitor`
3. Catat baseline NR dan NM jumlah baris Changelog
4. Klik `[Save Selection]`
5. Tunggu popup tertutup
6. Verifikasi `Furniture` dan `Heavy Equipment` berstatus usable (tidak redup)
7. Verifikasi `Office` dan `Spare Parts` berstatus Excess (redup)
8. Verifikasi Alert Category Consolidation tetap tampil (jumlah kategori tetap 9)
9. Buka Modal Changelog
10. Verifikasi Changelog bertambah tepat dua baris `Restored from Excess (Category Consolidation)` untuk `Furniture` dan `Heavy Equipment` (NR + 2)
11. Verifikasi tiap baris `Restored` berisi Old Value `Excess` dan New Value `Usable`
12. Verifikasi Changelog bertambah tepat dua baris `Marked as Excess (Category Consolidation)` untuk `Office` dan `Spare Parts` (NM + 2)
13. Tutup Modal Changelog

### TC-FA-CAT-296: Status usable atau Excess ditetapkan per node secara independen

14. Pulihkan Pre-setup #31 lewat fixture dan muat ulang halaman Categories
15. Klik `[Choose Categories]` pada Alert Category Consolidation
16. Centang `Keep usable` pada `Laptop`, `Monitor`, `Office`, `Spare Parts`, dan `Furniture`
17. Verifikasi checkbox `Keep usable` pada `Electronics` tetap unchecked (mencentang anak tidak mengubah centang parent)
18. Klik `[Save Selection]`
19. Tunggu popup tertutup
20. Verifikasi `Electronics` (parent, tidak dicentang) berstatus Excess (redup)
21. Verifikasi `Laptop` dan `Monitor` (anak, dicentang) tetap usable (tidak redup)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec 085 memuat TC-FA-CAT-292, 294, dan 295 (client CatPostT0); spec ini memuat TC yang memakai CatExcess.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 3 (baseline), 5 dan 19 (menunggu popup tertutup), 13 (menutup Modal Changelog), 14 (pemulihan fixture dan muat ulang).
- Temuan untuk QA:
  - TC-FA-CAT-293 dan TC-FA-CAT-296 tidak menyebut toast; spec tidak mengasersinya (S-02) dan menunggu popup tertutup sebelum membaca status.
  - TC-FA-CAT-296 Expected b menyebut "mencentang anak tidak mengubah centang parent"; spec mengasersinya sebelum `[Save Selection]` (langkah 17), urutan state (8b.5).

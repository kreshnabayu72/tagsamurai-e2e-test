---
id: TC-GS-GSET-E2E-033-download-changelog-sesuai-filter-dan-hidden
title: Download changelog sesuai filter dan kolom hidden tidak diexport
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-103
  - TC-GS-GSET-159
coverage:
  web: automated
---

# Download changelog: sesuai filter aktif dan kolom hidden tidak tinggal

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Environment mengizinkan aksi download (misal direktori download dev terpasang) untuk menangkap file.
- Data changelog ≥ 3 baris; filter yang dipilih pada langkah 3 membatasi hasil menjadi subset yang jelas.

## Test Steps

### Download mengikuti filter & search aktif

1. Buka Modal Changelog
2. Terapkan filter `Field = Currency` dan search `Session`
3. Klik tombol `Download` dan pilih format `CSV` (dan `XLSX` di langkah terpisah)
4. Verifikasi file terunduh bernama sesuai (misal `Changelog-General-Settings.csv` /
   `Changelog-General-Settings.xlsx`)
5. Buka file; verifikasi hanya baris yang memenuhi filter & search (Field Currency & mengandung
   "Session") yang muncul
6. Verifikasi header kolom pada file mengikuti seluruh kolom aktif (Action, Field, Old Value,
   New Value, Modified By, Date Modified)

### Kolom hidden tidak diexport

7. Sembunyikan kolom `Old Value` via Setup Column
8. Download CSV lagi
9. Verifikasi file hasil download TIDAK memiliki kolom `Old Value`
10. Verifikasi file hasil download tetap berisi seluruh baris yang memenuhi filter
11. Kembalikan kolom `Old Value`

### Download tanpa filter

12. Hapus semua filter dan download file baru
13. Verifikasi file berisi seluruh baris changelog (semua data, tanpa filter)
14. Verifikasi tidak ada error pada dialog/toast setelah berhasil download

## Notes

- Format download & nama file mengikuti PRD §3.5.2; spec hanya membuktikan bahwa filter aktif dan
  kolom hidden ikut menentukan isi file.
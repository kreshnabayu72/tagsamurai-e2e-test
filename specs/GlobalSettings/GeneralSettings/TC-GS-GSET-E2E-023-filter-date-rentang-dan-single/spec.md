---
id: TC-GS-GSET-E2E-023-filter-date-rentang-dan-single
title: Filter Date rentang Start/End dan single tanggal
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-52
  - TC-GS-GSET-155
coverage:
  web: automated
---

# Filter Date: rentang (Start ≠ End) dan seleksi single date

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Data changelog:
  - Baris A tanggal `10/07/2026`
  - Baris B tanggal `15/07/2026`
  - Baris C tanggal `20/07/2026`
- Format tanggal mengikuti Time Zone sesi (`dd/MM/yy`); script mengunci rentang tanggal uji terhadap
  UTC agar konsisten.

## Test Steps

### Rentang Start ≠ End

1. Buka Modal Changelog
2. Klik `Filter`, set `Start Date = 01/07/2026` dan `End Date = 10/07/2026`
3. Klik `[Apply]`
4. Verifikasi hanya baris A (`10/07/2026`) yang tampil (inklusif di kedua ujung)
5. Verifikasi baris B dan C di luar rentang tidak tampil

### Rentang hanya Start

6. Buka Filter, set hanya `Start Date = 15/07/2026` (End kosong)
7. Klik `[Apply]`
8. Verifikasi baris B dan C tampil, baris A tidak tampil

### Rentang hanya End

9. Buka Filter, set hanya `End Date = 15/07/2026` (Start kosong)
10. Klik `[Apply]`
11. Verifikasi baris A dan B tampil, baris C tidak tampil

### Single date (Start = End)

12. Buka Filter, set `Start Date = 15/07/2026` dan `End Date = 15/07/2026`
13. Klik `[Apply]`
14. Verifikasi hanya baris B yang tampil (seleksi 1 hari diterima, hasil beda dari range)

### Guard urutan tanggal

15. Buka Filter, set `Start Date = 31/07/2026` dan `End Date = 01/07/2026` (terbalik)
16. Verifikasi sistem menolak/menormalisasi (validasi Start tidak boleh lebih besar dari End)
17. Reset filter dan verifikasi seluruh baris tampil kembali

## Notes

- PMC `DATE-FILTER-CONTRACT` dipenuhi: `Start Date` dan `End Date` inklusif; differensiasi single-date
  vs range dibuktikan pada langkah 12-14 (sesuai pembeda TC-GS-GSET-52 vs 155).
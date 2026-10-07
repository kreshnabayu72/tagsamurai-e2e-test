---
id: TC-GS-DIV-E2E-043-tabel-utama-header-checkbox-dan-seleksi-lintas-halaman
title: "Tabel Utama: Checkbox Header, Status Indeterminate, dan Seleksi Lintas Halaman Select All"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-127
  - TC-GS-DIV-128
coverage:
  web: automated
---

# Tabel Utama: Checkbox Header, Status Indeterminate, dan Seleksi Lintas Halaman Select All

## Prerequisites

- Login sebagai Role: Total Control
- Tabel Division terisi 32 baris tanpa filter lintas halaman (TC-GS-DIV-30)
- User berada di Global Settings > User > Division
- Tabel Division terisi data (TC-GS-DIV-30)
- Tabel Division terisi 32 baris tanpa filter (TC-GS-DIV-30)

## Test Steps

### Checkbox header memilih seluruh baris halaman dan status indeterminate (TC-GS-DIV-127)

1. Klik checkbox header
2. Klik checkbox header lagi
3. Centang 1 baris saja
4. Verifikasi Klik checkbox header: 10 baris halaman aktif checked dan counter `10 Divisions selected`
5. Verifikasi Klik lagi: seluruh baris unchecked dan Bulk Action Bar hilang
6. Verifikasi Centang 1 baris: checkbox header berstatus indeterminate `[-]` dan counter `1 Division selected`

### Select All lintas halaman memilih seluruh baris dan toggle menjadi Unselect All (TC-GS-DIV-128)

7. Centang 1 baris
8. Klik `Select All (32 records)`
9. Pindah ke halaman 2
10. Klik `Unselect All`
11. Verifikasi Seluruh 32 baris terselect dan counter menampilkan `32 Divisions selected`
12. Verifikasi Baris pada halaman 2 tetap checked
13. Verifikasi Tombol berubah menjadi `Unselect All`
14. Verifikasi Klik `Unselect All` membatalkan seluruh seleksi dan Bulk Action Bar tertutup

## Notes

- Memvalidasi mekanisme seleksi tabel: checkbox header memilih 10 baris halaman aktif, toggle unselect, status indeterminate [-], serta tombol Select All (32 records) memilih seluruh 32 baris lintas halaman, retensi seleksi di halaman 2, dan toggle Unselect All (PRD §4.8, prd-conventions.md §8).
- Sumber pemetaan test case granular: TC-GS-DIV-127, TC-GS-DIV-128.

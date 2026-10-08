---
id: TC-AC-SG-E2E-052-setup-column-tabel-utama-screening-dan-toggle
title: "Setup Column tabel utama: screening modal 3 zona, toggle visibilitas kolom, dan guard minimal 1 kolom tersisa"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-95
  - TC-AC-SG-204
  - TC-AC-SG-205
  - TC-AC-SG-206
coverage:
  web: automated
---

# Setup Column tabel utama: screening modal 3 zona, toggle visibilitas kolom, dan guard minimal 1 kolom tersisa

## Prerequisites

- Login sebagai Role: Total Control

## Test Steps

### Screening Struktur Modal (3 Zona)
1. Klik icon Setup Column di toolbar tabel utama
2. Verifikasi modal Setup Column terbuka dengan 3 zona lengkap:
   - Zona 1 (Header): Judul Setup Column dan tombol tutup `[✕]`
   - Zona 2 (Body): Daftar 5 kolom data bertipe Hideable (`Group`, `Total User`, `Total Member`, `Modified By`, `Last Updated`) dan panel Live Preview
   - Zona 3 (Footer): `[Reset to Default]`, `[Cancel]`, `[Save]`
### Toggle Hide/Unhide 1 Kolom & Save
3. Hilangkan centang (uncheck) pada kolom `Modified By`
4. Verifikasi panel Live Preview seketika menyembunyikan kolom Modified By
5. Klik tombol `[Save]`
6. Verifikasi modal tertutup dan kolom `Modified By` hilang dari tabel utama
### Boundary Guard Minimal 1 Kolom Tersisa
7. Buka kembali Setup Column
8. Hilangkan centang pada kolom-kolom lainnya satu per satu hingga hanya tersisa tepat 1 kolom terakhir (contoh: `Group`)
9. Amati status checkbox pada kolom terakhir tersebut
10. Verifikasi checkbox kolom terakhir otomatis menjadi DISABLED
11. Hover pada checkbox kolom terakhir
12. Verifikasi muncul tooltip 🔖 `"At least one column must remain visible."` (sistem mencegah tabel kosong tanpa kolom)

## Notes

- Seluruh kolom data berstatus Hideable; tidak ada kolom yang berstatus Locked permanen.

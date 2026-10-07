---
id: TC-GS-DIV-E2E-054-tabel-utama-filter-chips-badge-counter-dan-search-coexistence
title: "Filter Tabel Utama: Chip Filter Aktif, Badge Counter Toolbar, dan Koeksistensi Search-Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-153
  - TC-GS-DIV-154
  - TC-GS-DIV-155
  - TC-GS-DIV-156
  - TC-GS-DIV-157
coverage:
  web: automated
---

# Filter Tabel Utama: Chip Filter Aktif, Badge Counter Toolbar, dan Koeksistensi Search-Filter

## Prerequisites

- Login sebagai Role: Total Control
- Tabel terisi data divisi (TC-GS-DIV-30)
- User berada di Global Settings > User > Division
- Tabel Division terisi 32 baris (TC-GS-DIV-30)

## Test Steps

### Search lalu Filter menghasilkan irisan keduanya (TC-GS-DIV-153)

1. Cari `es` lalu Enter
2. Buka Filter, pilih rentang tanggal pre-setup, klik `[Apply]`
3. Verifikasi Hanya `Human Resources` yang tampil (irisan Name memuat `es` dan Last Updated pre-setup; Division Data Uji Dinamis seperti `Facilities` dan `Sales` tersaring keluar)
4. Verifikasi Keyword Search tidak tereset setelah Apply

### Filter lalu Search menghasilkan irisan keduanya (TC-GS-DIV-154)

5. Buka Filter, pilih rentang tanggal pre-setup, klik `[Apply]`
6. Cari `es` lalu Enter
7. Verifikasi Hasil identik dengan TC Search lalu Filter: hanya `Human Resources` tampil
8. Verifikasi Kriteria filter tetap aktif saat Search dijalankan

### Kombinasi Search, Filter, Sort, dan Pagination bersamaan (TC-GS-DIV-155)

9. Cari `a` lalu Enter
10. Terapkan Filter rentang tanggal pre-setup
11. Klik header Name sampai descending
12. Ubah page size ke 25
13. Verifikasi Seluruh kondisi berlaku bersamaan: 6 Division Pre-setup terurut Name Z-A (`Treasury`, `Operations`, `Legal`, `Human Resources`, `Finance`, `Compliance`) pada page size 25
14. Verifikasi Tidak ada kontrol yang menimpa kontrol lain

### Clear Filter saat Search dan Sort aktif mempertahankan Search dan Sort (TC-GS-DIV-156)

15. Cari `a` lalu Enter
16. Terapkan Filter, lalu klik header Name sampai descending
17. Buka Filter, klik `[Clear Field]` dan `[Apply]`
18. Verifikasi Keyword `a` dan sort Name descending tetap aktif setelah filter dilepas

### Clear Search saat Filter dan Sort aktif mempertahankan Filter dan Sort (TC-GS-DIV-157)

19. Terapkan Filter rentang tanggal pre-setup
20. Cari `a` lalu Enter dan klik header Name sampai descending
21. Klik `(✕)` lalu Enter pada input kosong
22. Verifikasi Filter rentang tanggal dan sort Name descending tetap aktif setelah Search dikosongkan

## Notes

- Memvalidasi status filter aktif: kemunculan chip filter di bawah toolbar, hapus chip lewat icon (✕), badge counter pada icon filter toolbar, kombinasi Search dan Filter saling mempersempit (irisan AND), dan independensi pembersihan masing-masing kontrol (PRD §4.1.1, §4.4, §5).
- Sumber pemetaan test case granular: TC-GS-DIV-153, TC-GS-DIV-154, TC-GS-DIV-155, TC-GS-DIV-156, TC-GS-DIV-157.

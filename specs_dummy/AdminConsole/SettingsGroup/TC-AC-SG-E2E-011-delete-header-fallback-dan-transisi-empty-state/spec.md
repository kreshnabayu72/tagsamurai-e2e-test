---
id: TC-AC-SG-E2E-011-delete-header-fallback-dan-transisi-empty-state
title: "Fallback seleksi ke All Groups saat node header dihapus dan transisi ke empty state No subgroup yet"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-193
  - TC-AC-SG-194
coverage:
  web: automated
---

# Fallback seleksi ke All Groups saat node header dihapus dan transisi ke empty state No subgroup yet

## Prerequisites

- Login sebagai Role: Total Control
- Node `"Region A"` aktif di header dan tepat memiliki 1 subgroup `"Branch 1"` (kedua node memiliki 0 member)

## Test Steps

### Transisi Masuk ke Empty State No Subgroup Yet
1. Buka `Settings > Group` dan klik `"Region A"` di sidebar
2. Klik row action elipsis `[⋯]` pada baris `"Branch 1"` di tabel lalu pilih `[Delete]`
3. Pada dialog konfirmasi delete, klik `[Delete]`
4. Verifikasi toast sukses `"Success, group has been deleted."` tampil
5. Verifikasi baris `"Branch 1"` hilang dan tabel seketika beralih ke empty state `"No subgroup yet"`
6. Verifikasi icon expander pada node `"Region A"` di sidebar menghilang
### Fallback Seleksi Saat Node Header Dihapus
7. Klik elipsis `[⋯]` pada `"Region A"` di sidebar lalu klik `[Delete]`
8. Pada dialog konfirmasi delete, klik `[Delete]`
9. Verifikasi toast sukses `"Success, group has been deleted."` tampil
10. Verifikasi node `"Region A"` hilang dari sidebar tree
11. Verifikasi seleksi aktif otomatis fallback ke virtual root `"All Groups"`
12. Verifikasi Group Context Header kembali menampilkan `"All Groups"`
13. Verifikasi tabel utama me-refresh dan merender seluruh tree entitas secara flat (ACSG-LOGIC-09)

## Notes

- Menghapus node yang sedang menjadi header memicu fallback identik dengan toggle-off manual.

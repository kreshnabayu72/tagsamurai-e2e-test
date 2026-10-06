---
id: TC-GS-DIV-E2E-055-changelog-filter-search-internal-dropdown-dan-chip-cycles
title: "Pencarian Internal Dropdown Filter, Logika OR, Siklus Chip Removal, dan Overflow"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-209
  - TC-GS-DIV-210
  - TC-GS-DIV-211
  - TC-GS-DIV-212
  - TC-GS-DIV-224
coverage:
  web: automated
---

# Pencarian Internal Dropdown Filter, Logika OR, Siklus Chip Removal, dan Overflow

## Prerequisites

- Login sebagai Role: Total Control
- Daftar opsi dropdown memuat banyak entri

## Test Steps

1. Buka Filter Panel pada Modal Changelog Division lalu klik dropdown 'Action'
2. Ketik substring pada input pencarian di dalam dropdown dan verifikasi daftar opsi tersaring
3. Pilih dua opsi sekaligus: 'Create' dan 'Edit'
4. Klik '[Apply]' dan verifikasi tabel menampilkan entri Create ATAU Edit (logika OR di dalam satu field)
5. Verifikasi chip seleksi muncul di dalam kotak field filter
6. Klik ikon '[✕]' langsung pada salah satu chip tanpa membuka dropdown
7. Verifikasi chip tersebut terhapus dan filter terupdate
8. Buka kembali dropdown dan batalkan centang (uncheck) checkbox pada opsi yang aktif
9. Verifikasi chip terkait otomatis hilang dari field filter (alur pembatalan dua arah)
10. Pilih banyak opsi pada filter 'Modified By' hingga melebihi lebar field
11. Verifikasi chip menerapkan pola overflow indikator '+N more'

## Notes

- Menerapkan konvensi interaksi chip dan search multi-select dropdown prd-conventions.md §9.8.

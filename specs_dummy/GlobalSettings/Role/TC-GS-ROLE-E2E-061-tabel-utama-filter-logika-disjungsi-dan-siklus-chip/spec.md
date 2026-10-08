---
id: TC-GS-ROLE-E2E-061-tabel-utama-filter-logika-disjungsi-dan-siklus-chip
title: "Filter Tabel Utama: Evaluasi Logika OR/AND, Pencarian di Dropdown Filter, dan Siklus Hapus Chip via (X) vs Uncheck"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-147
  - TC-GS-ROLE-148
  - TC-GS-ROLE-149
  - TC-GS-ROLE-150
coverage:
  web: automated
---

# Filter Tabel Utama: Evaluasi Logika OR/AND, Pencarian di Dropdown Filter, dan Siklus Hapus Chip via (X) vs Uncheck

## Prerequisites

- Login sebagai Total Control
- Data Uji: User dengan variasi Position dan Division
- Setup Hook: beforeEach: navigateTo(Tab Total Control)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup tersedia; Tab Total Control dan Tab Read Only masing-masing berisi ≥3 user dengan Position/Division berbeda

## Test Steps

### Filter OR dalam satu field dan AND antar field (TC-GS-ROLE-147)

1. Filter Division Finance + IT → Apply
2. Tambah Status Active → Apply
3. Verifikasi Langkah 1: baris Finance ATAU IT
4. Verifikasi Langkah 2: hanya baris (Finance atau IT) DAN Active

### Search di dalam dropdown filter dan chip terpilih (TC-GS-ROLE-148)

5. Buka dropdown Position, ketik "man"
6. Centang "IT Manager" dan "HR Manager"
7. Verifikasi Daftar opsi menyempit ke yang mengandung "man" (case-insensitive)
8. Verifikasi Dua chip "IT Manager" dan "HR Manager" tampil di dalam field Position

### Hapus chip filter lewat (X) pada chip (TC-GS-ROLE-149)

9. Pilih Position IT Manager dan HR Manager → Apply
10. Klik (X) pada chip HR Manager
11. Apply
12. Verifikasi Chip HR Manager hilang, checkbox HR Manager di dropdown ikut unchecked
13. Verifikasi Chip IT Manager tetap
14. Verifikasi Tabel hanya IT Manager

### Hapus pilihan filter lewat uncheck di dropdown (TC-GS-ROLE-150)

15. Pilih Position IT Manager dan HR Manager → Apply
16. Buka dropdown, uncheck IT Manager
17. Apply
18. Verifikasi Chip IT Manager hilang, chip HR Manager tetap
19. Verifikasi Tabel hanya HR Manager

## Notes

- Memvalidasi alur skenario "Filter Tabel Utama: Evaluasi Logika OR/AND, Pencarian di Dropdown Filter, dan Siklus Hapus Chip via (X) vs Uncheck".
- Aturan PRD terkait: foundation/process/prd-process/prd-conventions.md §9.8; global-settings/role/PRD/role.md §4.1.1.
- Sumber pemetaan test case granular: TC-GS-ROLE-147, TC-GS-ROLE-148, TC-GS-ROLE-149, TC-GS-ROLE-150.

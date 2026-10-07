---
id: TC-GS-DIV-E2E-001-screening-tabel-utama-dan-urutan-default
title: "Screening Halaman Global Settings > User > Division, Default Sort Name A-Z, dan Data Seed Awal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-1
  - TC-GS-DIV-3
coverage:
  web: automated
---

# Screening Halaman Global Settings > User > Division, Default Sort Name A-Z, dan Data Seed Awal

## Prerequisites

- Login sebagai Role: Total Control
- Tabel Division terisi data Pre-setup (Finance, Human Resources, Legal, Operations, Compliance, Treasury)
- Tabel Division terisi data (Division Pre-setup: Finance, Human Resources, Legal, Operations, Compliance, Treasury)
- User berada di Global Settings > User > Division

## Test Steps

### Screening Halaman Global Settings > User > Division oleh Total Control (TC-GS-DIV-1)

1. Buka Global Settings > User
2. Klik Tab Division
3. Verifikasi Breadcrumb: `User > Division` dengan trigger Guided Tooltip `[?]`
4. Verifikasi Tab: `User List | Position | Division (aktif) | Custom Field`
5. Verifikasi Table Tools: `Search | Filter | Download | Changelog | [+ Division]`
6. Verifikasi Kolom: `Checkbox | Name (sortable) | Code (sortable) | Last Updated (sortable) | Column Visibility (⋯) (unsortable — header klik = buka overlay Column Visibility → CTA [Setup Column] di dalamnya, body per baris = row action menu)`
7. Verifikasi Baris Division Pre-setup tampil dengan Name, Code, dan Last Updated terisi (tidak ada sel kosong)
8. Verifikasi Pagination: default 10 data per halaman

### Urutan default tabel Division adalah Name A-Z tanpa membedakan huruf besar kecil (TC-GS-DIV-3)

9. Buka Tab Division
10. Perhatikan urutan baris halaman pertama dan ikon sort kolom Name
11. Verifikasi Baris terurut ascending: `Compliance`, `Finance`, `Human Resources`, `Legal`, `Operations`, `Treasury`
12. Verifikasi Ikon sort kolom Name menunjukkan ascending, kolom Code dan Last Updated netral

## Notes

- Memvalidasi screening komponen dasar header, sub-tab, toolbar, struktur kolom, dan urutan default alfabetis A-Z tanpa membedakan huruf besar kecil (PRD §4.1.1, §4.2, §5).
- Sumber pemetaan test case granular: TC-GS-DIV-1, TC-GS-DIV-3.

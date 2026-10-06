---
id: TC-GS-ROLE-E2E-034-tabel-total-control-filter-dropdown-populate-search-dan-chip-cycles
title: "Mekanisme Dropdown Filter Tab Total Control: Hardcode vs Populate, Search-Within, Logika OR, dan Siklus Chip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-231
  - TC-GS-ROLE-232
  - TC-GS-ROLE-233
  - TC-GS-ROLE-234
  - TC-GS-ROLE-235
  - TC-GS-ROLE-236
coverage:
  web: automated
---

# Mekanisme Dropdown Filter Tab Total Control: Hardcode vs Populate, Search-Within, Logika OR, dan Siklus Chip

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia data user dengan beragam nilai Position dan Status

## Test Steps

1. Buka Tab Total Control dan buka Filter Panel
2. Buka dropdown filter Position dan verifikasi opsi di-populate secara dinamis dari master data
3. Ketik keyword di dalam kolom pencarian dropdown (search-within-dropdown)
4. Verifikasi daftar opsi di dalam dropdown terfilter secara instan
5. Centang 2 opsi posisi berbeda (mis. Manager dan Staff)
6. Verifikasi sistem menerapkan logika OR antar-opsi dalam field yang sama
7. Klik [Apply] dan verifikasi chip filter muncul di panel/toolbar dengan label yang sesuai
8. Klik icon silang (✕) pada salah satu chip filter di toolbar
9. Verifikasi chip terhapus dan tabel langsung me-refresh hasil filter
10. Buka kembali dropdown filter, dan lakukan uncheck checkbox langsung di dalam menu dropdown yang terbuka
11. Verifikasi chip filter yang bersangkutan otomatis hilang dari daftar filter aktif

## Notes

- Siklus chip mencakup removal dua arah: via icon (✕) pada chip dan via uncheck di dalam dropdown terbuka (testcase-conventions §5p).

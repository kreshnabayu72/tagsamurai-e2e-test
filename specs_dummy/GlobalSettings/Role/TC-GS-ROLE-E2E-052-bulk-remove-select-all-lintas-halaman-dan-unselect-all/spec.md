---
id: TC-GS-ROLE-E2E-052-bulk-remove-select-all-lintas-halaman-dan-unselect-all
title: "Seleksi Massal Select All Lintas Halaman, Retensi Paginasi, dan Pembatalan Massal Unselect All"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-123
coverage:
  web: automated
---

# Seleksi Massal Select All Lintas Halaman, Retensi Paginasi, dan Pembatalan Massal Unselect All

## Prerequisites

- Login sebagai Total Control; Detail dengan >10 record eligible
- Data Uji: Detail dengan multi-halaman data
- Setup Hook: beforeEach: navigateTo(Detail)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Detail "Manage hardware" berisi >10 baris eligible (Pre-setup #17)

## Test Steps

### Select All lintas halaman dan Unselect All (TC-GS-ROLE-123)

1. Klik button Select All
2. Buka halaman 2
3. Klik button Unselect All
4. Verifikasi Semua baris eligible di semua halaman checked; counter = jumlah baris eligible
5. Verifikasi Halaman 2 baris tetap checked
6. Verifikasi Setelah 100% terselect button berubah menjadi "Unselect All"; klik membatalkan seluruh seleksi dan Bulk Action Bar tertutup

## Notes

- Memvalidasi alur skenario "Seleksi Massal Select All Lintas Halaman, Retensi Paginasi, dan Pembatalan Massal Unselect All".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Bulk Action Bar — Detail; global-settings/role/PRD/role.md §4.4; foundation/process/prd-process/prd-conventions.md §8.
- Sumber pemetaan test case granular: TC-GS-ROLE-123.

---
id: TC-GS-ROLE-E2E-009-hover-tooltip-toolbar-table-tools-dan-modified-by
title: "Hover Tooltip Toolbar Table Tools dan Tooltip Nama Lengkap Kolom Modified By"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-23
  - TC-GS-ROLE-25
coverage:
  web: automated
---

# Hover Tooltip Toolbar Table Tools dan Tooltip Nama Lengkap Kolom Modified By

## Prerequisites

- Login sebagai Role: Total Control
- Data Uji: Baris Modified By Budi S (Pre-setup #2)
- Spectra.intercept aktif untuk penanganan simulasi network/mock response
- Setup Hook: beforeEach: navigateTo(Role & Permission)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup tersedia
- User berada di Global Settings > Role & Permission > Total Control
- Dewi Lestari di-assign TC oleh Budi Santoso (Modified By "Budi S")

## Test Steps

### Hover tooltip icon Table Tools pada tiap surface (TC-GS-ROLE-23)

1. Tab Total Control: hover Search, Filter, Download, Changelog, header (⋯)
2. Tab System: hover Search, Download, Changelog, header (⋯)
3. Detail: hover Search, Filter, Download, Changelog, header (⋯)
4. Verifikasi Tab Total Control: tooltip "Search", "Filter", "Download", "Changelog", "Column Visibility"
5. Verifikasi Tab System: tooltip "Search", "Download", "Changelog", "Column Visibility"
6. Verifikasi Detail: tooltip "Search", "Filter", "Download", "Changelog", "Column Visibility"

### Hover Modified By menampilkan nama lengkap (TC-GS-ROLE-25)

7. Hover sel Modified By baris Dewi Lestari
8. Verifikasi Sel menampilkan "Budi S"
9. Verifikasi Tooltip menampilkan "Budi Santoso"

## Notes

- Memvalidasi alur skenario "Hover Tooltip Toolbar Table Tools dan Tooltip Nama Lengkap Kolom Modified By".
- Aturan PRD terkait: global-settings/role/PRD/role.md §5; foundation/process/prd-process/prd-conventions.md §9.1; foundation/process/prd-process/prd-conventions.md §9.3; global-settings/role/PRD/role.md §4.1.1 Modified By; foundation/process/prd-process/prd-conventions.md §9.13.
- Sumber pemetaan test case granular: TC-GS-ROLE-23, TC-GS-ROLE-25.

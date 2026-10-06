---
id: TC-GS-ROLE-E2E-046-changelog-total-control-filter-dropdown-search-dan-chip-cycles
title: "Mekanisme Dropdown Filter Modal Changelog Total Control: Populate Scoped, Search-Within, Logika OR, dan Chip Cycles"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-211
  - TC-GS-ROLE-212
  - TC-GS-ROLE-213
  - TC-GS-ROLE-214
  - TC-GS-ROLE-226
coverage:
  web: automated
---

# Mekanisme Dropdown Filter Modal Changelog Total Control: Populate Scoped, Search-Within, Logika OR, dan Chip Cycles

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia data log di modal Changelog Total Control

## Test Steps

1. Buka Modal Changelog Total Control dan buka Filter Panel
2. Buka dropdown Action dan verifikasi opsi berisi nilai yang tercatat (Edit, Assign, Remove)
3. Buka dropdown User Name dan Modified By dan verifikasi opsi di-populate secara scoped dari data log yang ada (bukan live master user)
4. Ketik keyword di dalam dropdown untuk menguji search-within-dropdown
5. Centang lebih dari satu opsi dan verifikasi sistem menerapkan logika OR
6. Klik [Apply] dan amati chip filter yang muncul di toolbar/panel
7. Hapus chip filter via icon silang (✕) pada chip
8. Buka kembali dropdown filter dan uncheck checkbox langsung di dalam dropdown menu yang terbuka
9. Verifikasi chip filter otomatis hilang

## Notes

- Opsi filter User Name dan Modified By pada modal Changelog di-populate khusus dari histori log entitas tersebut (role.md §8.1).

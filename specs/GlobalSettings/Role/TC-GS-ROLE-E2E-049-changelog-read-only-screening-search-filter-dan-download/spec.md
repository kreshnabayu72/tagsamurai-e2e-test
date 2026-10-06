---
id: TC-GS-ROLE-E2E-049-changelog-read-only-screening-search-filter-dan-download
title: "Pengujian Modal Changelog Tab Read Only: Search, Filter, Sort, Setup Column, dan Download CSV/XLSX"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-79
  - TC-GS-ROLE-215
  - TC-GS-ROLE-345
  - TC-GS-ROLE-350
coverage:
  web: automated
---

# Pengujian Modal Changelog Tab Read Only: Search, Filter, Sort, Setup Column, dan Download CSV/XLSX

## Prerequisites

- Login sebagai Role: Total Control
- Buka Modal Changelog dari Tab Read Only

## Test Steps

1. Buka Tab Read Only dan klik icon Changelog (⏱)
2. Verifikasi modal Changelog terbuka dengan judul: "Changelog: Role & Permission > Read Only"
3. Ketik keyword pada Search box modal Changelog dan verifikasi data log terfilter
4. Buka Filter Panel modal Changelog, terapkan filter Action, User Name, dan filter Date (1 hari)
5. Uji sorting kolom Date dan buka Setup Column modal Changelog
6. Klik tombol Download pada toolbar modal Changelog
7. Verifikasi file bernama Changelog-Role-Permission-Read-Only.csv berhasil diunduh

## Notes

- Modal Changelog Tab Read Only mencatat mutasi khusus akses Read Only (role.md §8.2).

---
id: TC-GS-DIV-E2E-054-changelog-filter-dropdown-populate-loading-dan-stale-reference
title: "Sumber Opsi Dropdown Filter Changelog: Hardcode Action vs Populate Scoped dan Stale Reference"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-205
  - TC-GS-DIV-206
  - TC-GS-DIV-207
  - TC-GS-DIV-208
  - TC-GS-DIV-278
coverage:
  web: automated
---

# Sumber Opsi Dropdown Filter Changelog: Hardcode Action vs Populate Scoped dan Stale Reference

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat divisi yang memiliki riwayat log dan divisi yang belum pernah dimutasi (0 log)
- Terdapat divisi hasil aksi Create Missing dari modul Import

## Test Steps

1. Buka Filter Panel pada Modal Changelog Division
2. Klik dropdown 'Action'
3. Verifikasi opsi dropdown Action bersifat hardcode memuat TEPAT 3 opsi: 'Create', 'Edit', dan 'Delete'
4. Verifikasi record hasil trigger Create Missing dari import tercatat sebagai 'Create' biasa tanpa qualifier tambahan
5. Klik dropdown 'Division Name'
6. Verifikasi daftar opsi terpopulasi secara dinamis (DISTINCT) HANYA dari data yang benar-benar tercatat di riwayat Changelog (divisi dengan 0 log tidak muncul)
7. Lakukan mutasi baru pada divisi lain, lalu buka kembali dropdown dan verifikasi opsi Name terupdate secara real-time
8. Terapkan filter pada nama divisi yang kemudian dihapus dari master data utama
9. Verifikasi entri log historis tetap dapat disaring menggunakan nama snapshot tersebut tanpa error stale reference

## Notes

- Membuktikan aturan populate scoped ke data changelog bukan live-join master data (division.md §9.5 dan GAP-020).

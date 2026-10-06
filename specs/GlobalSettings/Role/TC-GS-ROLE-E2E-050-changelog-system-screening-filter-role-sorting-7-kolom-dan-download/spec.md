---
id: TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download
title: "Pengujian Modal Changelog Tab System: Filter Unik Role, Dropdown Populate, Sorting 3-State 7 Kolom, dan Download"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-80
  - TC-GS-ROLE-216
  - TC-GS-ROLE-217
  - TC-GS-ROLE-218
  - TC-GS-ROLE-219
  - TC-GS-ROLE-220
  - TC-GS-ROLE-227
  - TC-GS-ROLE-238
  - TC-GS-ROLE-239
  - TC-GS-ROLE-240
  - TC-GS-ROLE-241
  - TC-GS-ROLE-242
  - TC-GS-ROLE-243
  - TC-GS-ROLE-343
  - TC-GS-ROLE-351
coverage:
  web: automated
---

# Pengujian Modal Changelog Tab System: Filter Unik Role, Dropdown Populate, Sorting 3-State 7 Kolom, dan Download

## Prerequisites

- Login sebagai Role: Total Control
- Buka Modal Changelog dari Tab System

## Test Steps

1. Buka Tab System dan klik icon Changelog (⏱)
2. Verifikasi modal Changelog terbuka dengan judul: "Changelog: Role & Permission > System"
3. Buka Filter Panel modal Changelog
4. Verifikasi ketersediaan filter unik 'Role' yang berisi 6 pilihan role sistem
5. Pilih salah satu role (mis. 'Manage TAG') pada filter Role lalu klik [Apply]
6. Verifikasi tabel Changelog hanya menampilkan aktivitas terkait role Manage TAG
7. Uji uncheck dropdown dan siklus chip removal
8. Uji sorting 3-state untuk 7 kolom modal: Date, Action, Role — User, Field, Old Value, New Value, Modified By
9. Klik tombol Download pada toolbar modal Changelog
10. Verifikasi file bernama Changelog-Role-Permission-System.csv berhasil diunduh

## Notes

- Modal Changelog Tab System adalah superset log seluruh role dan menyediakan filter khusus Role (role.md §8.3).

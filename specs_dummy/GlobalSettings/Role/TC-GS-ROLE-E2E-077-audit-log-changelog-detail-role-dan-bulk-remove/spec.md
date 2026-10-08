---
id: TC-GS-ROLE-E2E-077-audit-log-changelog-detail-role-dan-bulk-remove
title: "Pencatatan Audit Trail Changelog Detail: Edit CRUD C/U/D, Assign Role, Remove Row, dan Bulk Remove"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-212
  - TC-GS-ROLE-213
  - TC-GS-ROLE-214
  - TC-GS-ROLE-215
  - TC-GS-ROLE-216
  - TC-GS-ROLE-217
  - TC-GS-ROLE-218
  - TC-GS-ROLE-219
coverage:
  web: automated
---

# Pencatatan Audit Trail Changelog Detail: Edit CRUD C/U/D, Assign Role, Remove Row, dan Bulk Remove

## Prerequisites

- Login sebagai Total Control
- Data Uji: Riwayat mutasi Detail Manage user and role & Manage hardware
- Setup Hook: beforeEach: openChangelogModalDetail()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Edit CRUD Create dilakukan pada baris role Manage hardware milik user target
- Edit CRUD Update dilakukan pada baris role Manage TAG milik user target
- Edit CRUD Delete dilakukan pada baris role Manage files milik user target
- Ada entry Edit di Manage TAG dan Manage files

## Test Steps

### Changelog System dan Detail — entry Edit Field Create (TC-GS-ROLE-212)

1. Buka Changelog Detail "Manage hardware"
2. Buka Changelog Tab System
3. Verifikasi Detail: tepat 1 entry Action "Edit", Role — User "Manage hardware — [User]", Field "Create", Old "Inactive", New "Active", Modified By aktor
4. Verifikasi Tab System: entry yang sama tampil
5. Verifikasi Tidak ada entry untuk kolom CRUD lain yang tidak berubah

### Changelog System dan Detail — entry Edit Field Update (TC-GS-ROLE-213)

6. Buka Changelog Detail "Manage TAG"
7. Buka Changelog Tab System
8. Verifikasi Detail: tepat 1 entry Action "Edit", Role — User "Manage TAG — [User]", Field "Update", Old "Inactive", New "Active", Modified By aktor
9. Verifikasi Tab System: entry yang sama tampil
10. Verifikasi Tidak ada entry untuk kolom CRUD lain yang tidak berubah

### Changelog System dan Detail — entry Edit Field Delete (TC-GS-ROLE-214)

11. Buka Changelog Detail "Manage files"
12. Buka Changelog Tab System
13. Verifikasi Detail: tepat 1 entry Action "Edit", Role — User "Manage files — [User]", Field "Delete", Old "Active", New "Inactive", Modified By aktor
14. Verifikasi Tab System: entry yang sama tampil
15. Verifikasi Tidak ada entry untuk kolom CRUD lain yang tidak berubah

### Changelog System dan Detail — entry Assign baris role (TC-GS-ROLE-215)

16. Changelog Detail "Manage TAG"
17. Changelog Tab System
18. Verifikasi Per user (Wawan Setiawan, Nina Kartika) tepat 1 entry Action "Assign", Field "Access", Old "—", New "Assigned"
19. Verifikasi Tidak ada entry Edit tambahan untuk Read

### Changelog System dan Detail — entry Remove baris role (TC-GS-ROLE-216)

20. Changelog Detail "Manage TAG"
21. Changelog Tab System
22. Verifikasi Entry Action "Remove", Role — User "Manage TAG — Doni Pratama", Field "Access", Old "Assigned", New "—"

### Remove baris target TC mencatat Remove dan Auto-Revert terpisah (TC-GS-ROLE-217)

23. Changelog Detail "Manage files"
24. Changelog Tab Total Control
25. Verifikasi Detail: entry Remove "Manage files — Rudi Hartono", Field Access
26. Verifikasi Tab Total Control: entry Auto-Revert Total Control untuk Rudi Hartono
27. Verifikasi Tidak ada entry per-role untuk role lain Rudi Hartono

### Bulk Remove mencatat satu entry per baris dan Auto-Revert per user tier (TC-GS-ROLE-218)

28. Changelog Detail "Manage master reference"
29. Changelog Tab Total Control dan Tab Read Only
30. Verifikasi Tepat 3 entry Remove (Wawan Setiawan, Siti Nurhaliza, Rina Putri), tanpa duplikat
31. Verifikasi 1 entry Auto-Revert Total Control (Siti Nurhaliza) dan 1 entry Auto-Revert Read Only (Rina Putri)

### Changelog Detail memuat entry role itu saja, Changelog System superset (TC-GS-ROLE-219)

32. Changelog Detail "Manage TAG"
33. Changelog Tab System
34. Verifikasi Detail Manage TAG hanya memuat entry ber-Role — User "Manage TAG — …"
35. Verifikasi Tab System memuat entry Manage TAG dan Manage files

## Notes

- Memvalidasi alur skenario "Pencatatan Audit Trail Changelog Detail: Edit CRUD C/U/D, Assign Role, Remove Row, dan Bulk Remove".
- Aturan PRD terkait: global-settings/role/PRD/role.md §8.3; global-settings/role/PRD/role.md §8.4; global-settings/role/PRD/role.md §8.7; global-settings/role/PRD/role.md §9.2 [F-ROLE-07]; global-settings/role/PRD/role.md §8.7 Bulk Remove.
- Sumber pemetaan test case granular: TC-GS-ROLE-212, TC-GS-ROLE-213, TC-GS-ROLE-214, TC-GS-ROLE-215, TC-GS-ROLE-216, TC-GS-ROLE-217, TC-GS-ROLE-218, TC-GS-ROLE-219.

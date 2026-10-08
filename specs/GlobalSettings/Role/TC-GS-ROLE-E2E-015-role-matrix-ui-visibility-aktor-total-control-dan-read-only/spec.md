---
id: TC-GS-ROLE-E2E-015-role-matrix-ui-visibility-aktor-total-control-dan-read-only
title: "Role Matrix: UI Visibility Aktor Total Control, Read Only, dan Manage User and Role Read Saja"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-36
  - TC-GS-ROLE-37
  - TC-GS-ROLE-38
coverage:
  web: automated
---

# Role Matrix: UI Visibility Aktor Total Control, Read Only, dan Manage User and Role Read Saja

## Prerequisites

- Login bergantian sebagai Ahmad Fauzi (TC), Siti Nurhaliza (RO), Fajar Nugroho (MUR Read)
- Data Uji: Pre-setup #1, #4, #6
- Setup Hook: beforeEach: switchActor()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup tersedia
- Login sbg Role: Read Only (Siti Nurhaliza)
- Login sbg Role: Manage user and role Read saja (Fajar Nugroho)

## Test Steps

### Visibilitas elemen untuk aktor Total Control (TC-GS-ROLE-36)

1. Screening Tab Total Control
2. Screening Tab Read Only
3. Buka Detail "Manage TAG" dan screening baris Doni Pratama
4. Verifikasi Tab Total Control: [+ Assign] tampil; Download, Changelog tampil; overlay (⋯) baris Dewi Lestari berisi Remove (enabled)
5. Verifikasi Tab Read Only: [+ Assign] tampil; Remove pada baris Siti Nurhaliza enabled
6. Verifikasi Detail: [+ Assign] tampil; kolom checkbox seleksi tampil; checkbox Update Doni Pratama enabled; Remove Doni Pratama enabled
7. Verifikasi Search, Filter, Sort, Pagination, header Column Visibility aktif di ketiga surface

### Visibilitas elemen untuk aktor Read Only (TC-GS-ROLE-37)

8. Screening Tab Total Control
9. Screening Tab Read Only
10. Screening Tab System
11. Buka Detail "Manage TAG", hover checkbox Update baris Doni Pratama
12. Verifikasi Tab Total Control dan Tab Read Only: [+ Assign] tidak tampil; overlay (⋯) baris tidak memuat Remove; Download dan Changelog tampil
13. Verifikasi Tab System: Detail tetap tersedia via Role Name dan row action
14. Verifikasi Detail: [+ Assign] tidak tampil; kolom checkbox seleksi tidak tampil; row action Remove tidak tampil
15. Verifikasi Checkbox Create/Update/Delete tetap tampil (visible) namun disabled; tooltip "Read Only access cannot modify data."
16. Verifikasi Search, Filter, Sort, Pagination, header Column Visibility tetap aktif

### Visibilitas elemen untuk aktor Manage user and role Read saja (TC-GS-ROLE-38)

17. Screening Tab Total Control
18. Screening Tab Read Only
19. Screening Tab System
20. Buka Detail "Manage TAG", hover checkbox Update baris Doni Pratama
21. Verifikasi Tab Total Control dan Tab Read Only: [+ Assign] tidak tampil; overlay (⋯) baris tidak memuat Remove; Download dan Changelog tampil
22. Verifikasi Tab System: Detail tetap tersedia via Role Name dan row action
23. Verifikasi Detail: [+ Assign] tidak tampil; kolom checkbox seleksi tidak tampil; row action Remove tidak tampil
24. Verifikasi Checkbox Create/Update/Delete tetap tampil (visible) namun disabled; tooltip "Read Only access cannot modify data."
25. Verifikasi Search, Filter, Sort, Pagination, header Column Visibility tetap aktif

## Notes

- Memvalidasi alur skenario "Role Matrix: UI Visibility Aktor Total Control, Read Only, dan Manage User and Role Read Saja".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.8; global-settings/role/PRD/role.md §2.3; global-settings/role/PRD/role.md §4.3.
- Sumber pemetaan test case granular: TC-GS-ROLE-36, TC-GS-ROLE-37, TC-GS-ROLE-38.

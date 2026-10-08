---
id: TC-GS-ROLE-E2E-016-role-matrix-ui-visibility-aktor-manage-user-and-role
title: "Role Matrix: UI Visibility Aktor Manage User and Role Tanpa Update vs Berhak Update"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-39
  - TC-GS-ROLE-40
coverage:
  web: automated
---

# Role Matrix: UI Visibility Aktor Manage User and Role Tanpa Update vs Berhak Update

## Prerequisites

- Login bergantian sebagai Lina Marlina (MUR C/R/D) dan Hendra Wijaya (MUR C/R/U/D)
- Data Uji: Pre-setup #5, #7
- Setup Hook: beforeEach: switchActor()
- Login sbg Role: Manage user and role Create+Read+Delete tanpa Update (Lina Marlina)
- Pre-setup tersedia
- Login sbg Role: Manage user and role C/R/U/D (Hendra Wijaya)

## Test Steps

### Visibilitas elemen untuk aktor Manage user and role tanpa Update (TC-GS-ROLE-39)

1. Screening Tab Total Control
2. Screening Tab Read Only
3. Screening Tab System
4. Buka Detail "Manage TAG", hover checkbox Update baris Doni Pratama
5. Verifikasi Tab Total Control dan Tab Read Only: [+ Assign] tidak tampil; overlay (⋯) baris tidak memuat Remove; Download dan Changelog tampil
6. Verifikasi Tab System: Detail tetap tersedia via Role Name dan row action
7. Verifikasi Detail: [+ Assign] tidak tampil; kolom checkbox seleksi tidak tampil; row action Remove tidak tampil
8. Verifikasi Checkbox Create/Update/Delete tetap tampil (visible) namun disabled; tooltip "Read Only access cannot modify data."
9. Verifikasi Search, Filter, Sort, Pagination, header Column Visibility tetap aktif

### Visibilitas elemen untuk aktor Manage user and role dengan Update (TC-GS-ROLE-40)

10. Screening Tab Total Control dan Tab Read Only
11. Buka Detail "Manage TAG"
12. Hover checkbox Update dan Remove pada baris Doni Pratama, Dewi Lestari (TC), Siti Nurhaliza (RO), Hendra Wijaya (diri sendiri), Budi Santoso (Default User)
13. Verifikasi Tab Total Control/Read Only: [+ Assign] tidak tampil; Remove tidak ada di overlay (⋯) baris
14. Verifikasi Detail: [+ Assign] tampil
15. Verifikasi Doni Pratama: checkbox Update dan Remove enabled
16. Verifikasi Dewi Lestari dan Siti Nurhaliza: checkbox Update, Remove, dan checkbox seleksi tetap tampil namun disabled; tooltip "You don't have permission to edit."
17. Verifikasi Hendra Wijaya: checkbox Update, Remove, dan checkbox seleksi disabled; tooltip "You can't manage your own account from here."
18. Verifikasi Budi Santoso: checkbox Update, Remove, dan checkbox seleksi disabled; tooltip "Default User cannot be modified."

## Notes

- Memvalidasi alur skenario "Role Matrix: UI Visibility Aktor Manage User and Role Tanpa Update vs Berhak Update".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.8; global-settings/role/PRD/role.md §2.3; global-settings/role/PRD/role.md §4.3.
- Sumber pemetaan test case granular: TC-GS-ROLE-39, TC-GS-ROLE-40.

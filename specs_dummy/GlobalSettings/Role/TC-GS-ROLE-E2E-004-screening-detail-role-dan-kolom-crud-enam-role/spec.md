---
id: TC-GS-ROLE-E2E-004-screening-detail-role-dan-kolom-crud-enam-role
title: "Screening Halaman Detail Role, Deskripsi dan Kolom CRUD Dinamis untuk 6 Role Sistem"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-4
  - TC-GS-ROLE-5
  - TC-GS-ROLE-281
coverage:
  web: automated
---

# Screening Halaman Detail Role, Deskripsi dan Kolom CRUD Dinamis untuk 6 Role Sistem

## Prerequisites

- Login sebagai Role: Total Control (Ahmad Fauzi)
- Data Uji: Pre-setup #2, #5, #10 (Budi Santoso, Hendra Wijaya, Doni Pratama)
- Setup Hook: beforeEach: navigateTo(Role & Permission > System > Detail)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup #5 (Hendra Wijaya, Manage user and role C/R/U/D) dan #10 (Doni Pratama, Manage user and role R) tersedia
- Pre-setup tersedia
- User berada di Global Settings > Role & Permission > System > Detail "Manage user and role"

## Test Steps

### Screening halaman Detail role "Manage user and role" (web) (TC-GS-ROLE-4)

1. Buka Global Settings > Role & Permission > System
2. Klik Role Name "Manage user and role"
3. Screening halaman Detail dari atas ke bawah
4. Verifikasi **Header**:
5. Verifikasi Breadcrumb: "Role & Permission > System > Detail"; segmen "System" clickable
6. Verifikasi Title: "Manage user and role"
7. Verifikasi Teks di bawah Title: "This role allows the user to manage user accounts and role permissions through the User and Role & Permission menus."
8. Verifikasi Table Tools: `Search | Filter | Download | Changelog | [+ Assign]`
9. Verifikasi **Body**:
10. Verifikasi Kolom: `Checkbox (pinned kiri) | Name (sortable) | Position (sortable) | Division (sortable) | Create (unsortable) | Read (unsortable) | Update (unsortable) | Delete (unsortable) | Actions (⋯) (unsortable — header = overlay Column Visibility, body = row action Remove)`
11. Verifikasi Kolom Read di semua baris: checked dan disabled
12. Verifikasi Tidak ada kolom Status (Active/Inactive)
13. Verifikasi Baris Budi Santoso (Default User) tampil dengan Position "—" dan Division "—"
14. Verifikasi **Footer**: Pagination default 10

### Detail — kolom CRUD dinamis dan deskripsi per role untuk 6 role (TC-GS-ROLE-5)

15. Buka Global Settings > Role & Permission > System
16. Untuk tiap role pada Data Uji: klik Role Name → screening Title, deskripsi, dan kolom CRUD → klik breadcrumb "System"
17. Verifikasi Import data: kolom `Create | Read`; deskripsi "This role allows the user to import external data into the system through the Import menu."
18. Verifikasi Manage files: kolom `Read | Delete`; deskripsi "This role allows the user to manage uploaded files and attachments through the File Manager menu."
19. Verifikasi Manage hardware: kolom `Create | Read | Update | Delete`; deskripsi "This role allows the user to manage handheld reader devices through the Hardware menu."
20. Verifikasi Manage master reference: kolom `Create | Read | Update | Delete`; deskripsi "This role allows the user to manage brand and measurement master data through the Brand and Measurement menus."
21. Verifikasi Manage TAG: kolom `Read | Update`; deskripsi "This role allows the user to manage, audit, and combine or separate TAGs through the TAG menu."
22. Verifikasi Manage user and role: kolom `Create | Read | Update | Delete`; deskripsi "This role allows the user to manage user accounts and role permissions through the User and Role & Permission menus."
23. Verifikasi Kolom yang tidak berlaku untuk role tidak dirender sama sekali (bukan kolom berisi "—")

### Detail — checkbox CRUD rata tengah di sel (TC-GS-ROLE-281)

24. Amati posisi checkbox Create, Read, Update, Delete pada tiap baris
25. Verifikasi Checkbox Create, Read, Update, Delete berada di tengah sel (centered) di semua baris

## Notes

- Memvalidasi alur skenario "Screening Halaman Detail Role, Deskripsi dan Kolom CRUD Dinamis untuk 6 Role Sistem".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Page: Detail; global-settings/role/PRD/role.md §4.1.4; global-settings/role/PRD/role.md §2.1; global-settings/role/PRD/role.md §4.5.
- Sumber pemetaan test case granular: TC-GS-ROLE-4, TC-GS-ROLE-5, TC-GS-ROLE-281.

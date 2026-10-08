---
id: TC-GS-ROLE-E2E-014-sidebar-menu-visibility-per-role-dan-direct-url-guard
title: "Visibilitas Menu Role & Permission pada Sidebar per Peran dan Penolakan Akses Direct URL 403"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-33
  - TC-GS-ROLE-34
  - TC-GS-ROLE-35
coverage:
  web: automated
---

# Visibilitas Menu Role & Permission pada Sidebar per Peran dan Penolakan Akses Direct URL 403

## Prerequisites

- Multi-role context (Total Control, Read Only, Manage user and role, Manage TAG)
- Data Uji: Akun Pre-setup #1, #4, #5, #8 (Yusuf Hidayat)
- Setup Hook: beforeEach: switchActor()
- Akun uji per aktor tersedia (Pre-setup #1, #4, #5, #6, #7)
- Login sbg Role: Manage TAG Read saja, bukan TC/RO (Yusuf Hidayat)
- Login sbg Role: Manage TAG Read saja (Yusuf Hidayat)

## Test Steps

### Menu Role & Permission tampil di sidebar untuk aktor yang punya akses baca (TC-GS-ROLE-33)

1. Untuk tiap aktor pada Data Uji: login → buka Global Settings → amati sidebar → logout
2. Verifikasi Total Control: menu "Role & Permission" tampil
3. Verifikasi Read Only: tampil
4. Verifikasi Manage user and role C/R/U/D: tampil
5. Verifikasi Manage user and role Read saja: tampil
6. Verifikasi Manage user and role tanpa Update: tampil

### Menu Role & Permission tersembunyi untuk user tanpa role Manage user and role (TC-GS-ROLE-34)

7. Login
8. Buka Global Settings
9. Amati sidebar
10. Verifikasi Menu "Role & Permission" tidak tampil
11. Verifikasi Menu "TAG" tampil (anchor)

### Akses langsung URL Role & Permission tanpa role Manage user and role (TC-GS-ROLE-35)

12. Ketik URL halaman Role & Permission > Total Control di address bar
13. Ulangi untuk URL Detail "Manage TAG"
14. Verifikasi Muncul toast error: "You don't have permission to do this."
15. Verifikasi Data tabel Role & Permission tidak ditampilkan
16. Verifikasi Tidak redirect ke halaman unauthorized terpisah

## Notes

- Memvalidasi alur skenario "Visibilitas Menu Role & Permission pada Sidebar per Peran dan Penolakan Akses Direct URL 403".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.8; global-settings/role/PRD/role.md §2.3; global-settings/role/PRD/role.md §4.3; global-settings/role/PRD/role.md §9.3; global-settings/role/PRD/role.md §9.11; foundation/process/prd-process/error-handling-convention.md §2.
- Sumber pemetaan test case granular: TC-GS-ROLE-33, TC-GS-ROLE-34, TC-GS-ROLE-35.

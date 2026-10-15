---
id: TC-GS-USER-E2E-009-role-matrix-visibilitas-menu-dan-direct-url
title: "Role Matrix: Visibilitas menu sidebar User dan penolakan Direct URL tanpa izin"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-41
  - TC-GS-USER-42
  - TC-GS-USER-43
  - TC-GS-USER-44
  - TC-GS-USER-45
  - TC-GS-USER-46
coverage:
  web: automated
---

# Role Matrix: Visibilitas menu sidebar User dan penolakan Direct URL tanpa izin

## Prerequisites

- Akun aktor Total Control, Read Only, Full CRUD, Read-Only role, dan Basic User tersedia

## Test Steps

### Visibilitas Menu Sidebar

1. Login sebagai Total Control, verifikasi menu 'User' tampil di sidebar Global Settings
2. Login sebagai Read Only, verifikasi menu 'User' tampil di sidebar
3. Login sebagai Manage user and role (Full CRUD), verifikasi menu 'User' tampil di sidebar
4. Login sebagai Manage user and role (Read-Only role), verifikasi menu 'User' tampil di sidebar
5. Login sebagai Basic User tanpa capability, verifikasi menu 'User' tersembunyi dari sidebar

### Direct URL Guard

6. Sebagai Basic User, akses langsung URL '/settings/users' di browser
7. Verifikasi navigasi ditolak dengan tampilan 403 Forbidden atau dialihkan ke halaman dashboard dengan toast permission

## Notes

- Menggabungkan 6 test case granular (TC-GS-USER-41 s.d. TC-GS-USER-46).

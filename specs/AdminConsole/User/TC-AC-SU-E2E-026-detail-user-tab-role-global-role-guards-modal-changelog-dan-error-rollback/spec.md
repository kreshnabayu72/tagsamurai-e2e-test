---
id: TC-AC-SU-E2E-026-detail-user-tab-role-global-role-guards-modal-changelog-dan-error-rollback
title: "Guard Sub-tab Global Role (Default User, Self-edit, target TC/RO), modal Changelog, dan rollback CRUD error 5xx"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-69
  - TC-AC-SU-71
  - TC-AC-SU-72
  - TC-AC-SU-73
  - TC-AC-SU-161
  - TC-AC-SU-176
  - TC-AC-SU-252
coverage:
  web: automated
---

# Guard Sub-tab Global Role (Default User, Self-edit, target TC/RO), modal Changelog, dan rollback CRUD error 5xx

## Prerequisites

- Login sebagai Role: Principal Total Control dan Role: Manage user and role
- Terdapat target Default User, Self User, dan Target Read Only; simulasi mock error 500 pada update permission

## Test Steps

### Verifikasi Guard Role pada Default User, Self, dan Target TC/RO

1. Buka Tab Role Sub-tab Global Role untuk Default User: verifikasi seluruh 10 switch ON dan Disabled, serta seluruh checkbox CRUD tercentang dan Disabled permanen
2. Buka Tab Role Sub-tab Global Role untuk akun yang sedang login (Self): coba klik switch role atau checkbox CRUD, verifikasi seluruh elemen Disabled dengan tooltip `"You cannot edit your own roles."` (berlaku untuk semua tier)
3. Login sebagai aktor "Manage user and role", buka Tab Role target pengguna Read Only: coba ubah switch role, verifikasi Disabled dengan tooltip `"Only Default User or Total Control can edit this user's roles."`

### Modal Changelog Global Role dan Rollback Error 5xx

1. Buka Tab Role Sub-tab Global Role pengguna target, klik icon `[📋 Changelog]` di toolbar sub-tab
2. Verifikasi modal `"Changelog: User > Global Role"` terbuka dengan kolom Date, Action, Role Name, Field, Old Value, New Value, Modified By
3. Tutup modal Changelog
4. Konfigurasikan mock error 500 pada endpoint update role permission
5. Centang salah satu checkbox CRUD pada role aktif
6. Verifikasi checkbox otomatis rollback ke status awal dan toast error muncul: `"Error, failed to update permissions."` / `"Error, failed to update role."`

## Notes

- Guard role mencegah eskalasi hak istimewa secara mandiri oleh admin.

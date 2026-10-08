---
id: TC-GS-USER-E2E-118-list-baris-default-user-dan-self
title: 'Baris Default User dan akun sendiri di User List memiliki aksi terbatas'
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-5
  - TC-GS-USER-6
coverage:
  web: automated
---

# Baris Default User dan akun sendiri di User List memiliki aksi terbatas

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Default User (`totalControlGlobalSettings_automated_qaTeam1`) ada
- Spec ini tidak mengubah data

## Test Steps

### Baris Default User

1. Amati baris Default User di User List
2. Verifikasi checkbox baris Disabled
3. Verifikasi toggle Active Disabled dengan tooltip "Default User cannot be modified."
4. Buka menu row action `[⋯]`
5. Verifikasi menu hanya berisi `Detail` dan `Edit` (keduanya Enabled), dan `Delete` tidak muncul di menu (tersembunyi, bukan Disabled)

### Baris akun sendiri

6. Amati baris akun aktor sendiri
7. Verifikasi checkbox baris Disabled
8. Verifikasi toggle Active Disabled dengan tooltip "You can't manage your own account from here."
9. Buka menu row action `[⋯]`
10. Verifikasi menu hanya berisi `Detail` (Enabled), dan `Edit` serta `Delete` tidak muncul di menu

## Notes

- Sumber `user.md` bagian 2.5 dan 4.2. Dua tooltip sengaja berbeda. Aksi yang sama dari User Detail dicakup `TC-GS-USER-E2E-074-user-detail-header-guard-target`.

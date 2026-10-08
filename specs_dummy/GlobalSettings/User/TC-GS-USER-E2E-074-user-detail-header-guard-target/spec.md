---
id: TC-GS-USER-E2E-074-user-detail-header-guard-target
title: 'Toggle Active dan menu Header User Detail Disabled untuk target yang dilindungi'
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-502
  - TC-GS-USER-503
  - TC-GS-USER-504
coverage:
  web: automated
---

# Toggle Active dan menu Header User Detail Disabled untuk target yang dilindungi

## Prerequisites

- Sesi aktor Total Control biasa (`totalControl2_automated_qaTeam1`), bukan Default User
- Sesi aktor capability holder: role "Manage user and role" Full CRUD, bukan Total Control
- Default User (`totalControlGlobalSettings_automated_qaTeam1`) ada, dan user "Siti Rahmawati" berstatus Total Control
- Spec ini tidak mengubah data

## Test Steps

### Target Default User

1. Di sesi Total Control, buka User Detail Default User
2. Verifikasi toggle Active Disabled dengan tooltip "Default User cannot be modified."
3. Klik menu `[⋯]` dan verifikasi "Edit Profile" tetap Enabled (pengecualian untuk Default User), sedangkan "Delete User" Disabled dengan tooltip yang sama

### Target akun sendiri

4. Buka User Detail akun aktor sendiri
5. Verifikasi toggle Active Disabled
6. Klik menu `[⋯]` dan verifikasi "Edit Profile" dan "Delete User" keduanya Disabled, dengan tooltip "You can't manage your own account from here." pada ketiga elemen

### Capability holder terhadap target Total Control

7. Di sesi capability holder, buka User Detail "Siti Rahmawati"
8. Verifikasi toggle Active Disabled
9. Klik menu `[⋯]` dan verifikasi "Edit Profile" dan "Delete User" keduanya Disabled, dengan tooltip "Only Default User or Total Control can edit users with Total Control or Read Only access." pada ketiga elemen

## Notes

- Sumber `user.md` bagian 2.5 dan 4.1. Guard yang sama berlaku dari baris User List, dan dicakup `TC-GS-USER-E2E-018-role-negatif-target-terlindungi` serta spec role matrix lainnya.
- Tiga tooltip sengaja berbeda: Default User, akun sendiri, dan target Total Control/Read Only untuk capability holder.
- Cara menjalankan dua sesi berbeda ditentukan tim FE di tahap script.

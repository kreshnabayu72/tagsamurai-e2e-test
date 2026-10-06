---
id: TC-AC-SU-E2E-015-activate-deactivate-guards-dan-disabled-states
title: "Guard proteksi switch Active: Default User, Self-edit, entitas suspended, isActiveGlobal=false, dan tier restrictions"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-30
  - TC-AC-SU-31
  - TC-AC-SU-32
  - TC-AC-SU-33
  - TC-AC-SU-34
  - TC-AC-SU-35
  - TC-AC-SU-36
  - TC-AC-SU-160
coverage:
  web: automated
---

# Guard proteksi switch Active: Default User, Self-edit, entitas suspended, isActiveGlobal=false, dan tier restrictions

## Prerequisites

- Login sebagai Role: Principal Total Control dan Role: Manage user and role
- Terdapat target Default User, Self User, Suspended Entity, User dengan isActiveGlobal=false, Target Total Control, dan Target Group Manager

## Test Steps

### Verifikasi Guard Switch Active pada Akun Terlindungi

1. Buka User List, amati baris Default User: coba klik switch Active, verifikasi switch berstatus Disabled permanen dengan tooltip `"Default User cannot be modified."`
2. Amati baris akun sendiri (Self): coba klik switch Active, verifikasi switch berstatus Disabled dengan tooltip `"You cannot deactivate your own account."`
3. Buka User List pada entitas yang sedang dalam status suspend, verifikasi seluruh switch Active berstatus Disabled dengan tooltip organisasi tersuspensi
4. Amati pengguna yang berstatus `isActiveGlobal = false` di Global Settings: verifikasi switch Active di Admin Console berstatus Disabled dengan tooltip `"This user is inactive in Global Settings..."` sementara posisi switch terakhir tetap dipertahankan
5. Aktifkan kembali pengguna tersebut di Global Settings, muat ulang User List di Admin Console, verifikasi switch kembali Enabled pada posisi semula

### Verifikasi Guard Berdasarkan Tier Aktor vs Target

1. Login sebagai pengguna dengan role "Manage user and role" (bukan Total Control)
2. Buka User List, coba klik switch Active pada pengguna dengan tier Total Control atau Read Only
3. Verifikasi switch berstatus Disabled dengan tooltip `"Only Default User or Total Control can activate or deactivate this user."`
4. Amati baris pengguna dengan status Group Manager, verifikasi switch Active tetap Enabled dan dapat diubah oleh aktor ini

## Notes

- Guard perlindungan status akun mencegah penguncian sistem dan eskalasi hak akses.

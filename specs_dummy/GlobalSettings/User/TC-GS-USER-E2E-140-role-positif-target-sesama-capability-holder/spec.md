---
id: TC-GS-USER-E2E-140-role-positif-target-sesama-capability-holder
title: Role Update-saja memperlakukan sesama pemegang role sebagai target biasa
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-599
coverage:
  web: automated
---

# Role Update-saja memperlakukan sesama pemegang role sebagai target biasa

## Prerequisites

Spec ini memakai satu role. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

| Role | Akun |
|---|---|
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` |

- Entity Client
- Target "Hadi Manajer" memegang role individual "Manage user and role" tetapi bukan `access_level` Total Control atau Read Only, bukan Default User, bukan akun yang login, aktif
- Position "Supervisor" ada di master data dan berbeda dari Position target

## Test Steps

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Buka Modal Edit "Hadi Manajer", ubah Position menjadi "Supervisor", lalu klik `[Save]`
3. Verifikasi toast "Success, user has been updated." muncul dan baris target menampilkan Position "Supervisor"
4. Klik Toggle Active [Global] pada baris target untuk mematikannya, lalu klik `[Deactivate]` pada dialog "Deactivate User"
5. Verifikasi toast "Success, user has been deactivated." muncul dan Toggle Active [Global] target menjadi OFF

## Notes

- `USER-LOGIC-03` hanya menutup target ber-`access_level` Total Control atau Read Only. Spec ini membuktikan sesama capability holder tidak ikut terlarang.
- Target harus dikembalikan ke Position awal dan diaktifkan kembali, atau di-seed ulang setelah run.

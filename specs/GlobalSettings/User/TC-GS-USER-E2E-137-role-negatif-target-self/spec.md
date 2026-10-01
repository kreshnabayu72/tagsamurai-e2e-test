---
id: TC-GS-USER-E2E-137-role-negatif-target-self
title: Role Update-saja tidak dapat menyentuh akunnya sendiri
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-596
coverage:
  web: automated
---

# Role Update-saja tidak dapat menyentuh akunnya sendiri

## Prerequisites

Spec ini memakai satu role. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

| Role | Akun |
|---|---|
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` |

- Entity Client
- Target adalah akun yang login (`manageUserRoleUpdateOnly_automated_qaTeam1`)
- Spec ini tidak membuat atau mengubah data

## Test Steps

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Pada baris akun sendiri, verifikasi checkbox dan Toggle Active [Global] Disabled
3. Buka menu `[⋯]` pada baris itu dan verifikasi hanya `Detail` yang tersedia, tanpa `Edit` dan `Delete`
4. Buka User Detail akun sendiri dan verifikasi Toggle Active dan menu `[⋯]` di header Disabled
5. Verifikasi tombol `Reset Authenticator` Disabled dengan tooltip "You can't manage your own account from here."

## Notes

- Berlaku `USER-LOGIC-01` untuk capability holder. Pasangan untuk aktor Total Control dan Default User adalah `TC-GS-USER-E2E-018`.
- Resend dan Pair/Unpair tidak dinilai karena `user.md` §4.8 tidak menggerbanginya per target.
- Spec ini tidak mengubah data, jadi tidak butuh cleanup.

---
id: TC-GS-USER-E2E-136-role-negatif-target-default-user
title: Role Update-saja tidak dapat menyentuh Default User kecuali Edit
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-595
coverage:
  web: automated
---

# Role Update-saja tidak dapat menyentuh Default User kecuali Edit

## Prerequisites

Spec ini memakai satu role. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

| Role | Akun |
|---|---|
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` |

- Entity Client
- Target adalah Default User (`totalControlGlobalSettings_automated_qaTeam1`), Activated, Authenticator enrolled
- Spec ini tidak membuat atau mengubah data

## Test Steps

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Pada baris Default User, verifikasi checkbox dan Toggle Active [Global] Disabled
3. Verifikasi row action `Delete` tidak tersedia atau Disabled
4. Verifikasi row action `Edit` tetap Enabled
5. Buka Modal Edit Default User dan verifikasi info dasar bisa diedit, sementara semua checkbox Access tercentang dan Disabled dengan tooltip "Default User cannot be modified."
6. Klik `✕` untuk menutup modal
7. Buka User Detail Default User dan verifikasi tombol `Reset Authenticator` Disabled dengan tooltip "You don't have permission to edit"

## Notes

- Berlaku `USER-LOGIC-02` untuk capability holder sama seperti Total Control. Pasangan untuk aktor Total Control adalah `TC-GS-USER-E2E-018`.
- Resend dan Pair/Unpair tidak dinilai karena `user.md` §4.8 tidak menggerbanginya per target.
- Spec ini tidak mengubah data, jadi tidak butuh cleanup.

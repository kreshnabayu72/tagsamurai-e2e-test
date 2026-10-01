---
id: TC-GS-USER-E2E-138-role-negatif-target-read-only
title: Role Update-saja tidak dapat menyentuh user ber-tier Read Only
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-597
coverage:
  web: automated
---

# Role Update-saja tidak dapat menyentuh user ber-tier Read Only

## Prerequisites

Spec ini memakai satu role. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

| Role | Akun |
|---|---|
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` |

- Entity Client
- Target "Rudi Readonly" adalah user ber-`access_level` Read Only, bukan Default User dan bukan akun yang login, dengan Access `[Global Settings, FAMS]`
- Spec ini tidak membuat atau mengubah data

## Test Steps

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Pada baris "Rudi Readonly", verifikasi checkbox, tombol row action `(⋯)`, dan `Detail` tetap tampil dan aktif, tidak Hidden
3. Verifikasi Toggle Active [Global] Disabled dengan tooltip "Only Default User or Total Control can edit users with Total Control or Read Only access."
4. Verifikasi row action `Edit` dan `Delete` Disabled dengan tooltip yang sama
5. Buka User Detail "Rudi Readonly" dan verifikasi tombol `Reset Authenticator` Disabled dengan tooltip yang sama

## Notes

- Berlaku `USER-LOGIC-03` untuk tier Read Only. Spec `TC-GS-USER-E2E-019` hanya memakai target Total Control.
- Spec ini tidak mengubah data, jadi tidak butuh cleanup.

---
id: TC-GS-USER-E2E-017-role-negatif-delete
title: Role tanpa hak Delete tidak dapat menghapus user
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-08
  - TC-GS-USER-85
  - TC-GS-USER-581
  - TC-GS-USER-582
coverage:
  web: automated
---

# Role tanpa hak Delete tidak dapat menghapus user

## Prerequisites

Spec ini dijalankan untuk setiap role pada tabel. Langkahnya identik, hanya akun login dan keadaan yang diharapkan yang berbeda. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

Role yang diuji dan keadaan yang diharapkan pada baris target biasa:

| Role | Akun | Delete |
|---|---|---|
| Read Only | `readOnlyGlobalSettings_automated_qaTeam1` | Hidden |
| Manage user and role (hanya Create) | `manageUserRoleCreateOnly_automated_qaTeam1` | Disabled, tooltip "You don't have permission to edit" |
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` | Disabled, tooltip "You don't have permission to edit" |

- Entity Client
- Ada minimal satu target User Basic biasa (bukan Total Control, Read Only, Default User, atau akun yang login) di User List

## Test Steps

Lakukan langkah 1–2 untuk setiap role pada tabel "Role yang diuji".

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Pada baris target biasa, verifikasi row action `Delete` sesuai kolom "Delete" pada tabel

## Notes

- Ini spec negatif Delete dari Role Matrix (`docs/e2e-conventions.md` bagian 3a). Pasangan positifnya adalah `TC-GS-USER-E2E-013-role-positif-delete`.
- Keadaan `Delete` mengikuti tabel gerbang UI `user.md` §4.8: tampil dan aktif hanya jika role punya Delete, Disabled bila tidak punya, dan Hidden untuk Read Only.
- Cara skrip menjalankan banyak role diputuskan di tahap script.
- Lapisan frontend mencakup TC-GS-USER-08 dan 85 dengan payload izin yang di-mock (TC-GS-USER-FE-018, 159). TC-GS-USER-581 dan 582 belum punya padanan frontend. TC-GS-USER-08 dan 85 berprioritas P0, jadi tumpang tindih disengaja (`docs/e2e-conventions.md` bagian 2).
- Spec ini tidak membuat atau mengubah data, jadi tidak butuh cleanup.

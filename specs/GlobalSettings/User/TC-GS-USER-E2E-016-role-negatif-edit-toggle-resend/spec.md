---
id: TC-GS-USER-E2E-016-role-negatif-edit-toggle-resend
title: Role tanpa hak Update tidak dapat Edit, Toggle Active, dan Resend
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-08
  - TC-GS-USER-85
  - TC-GS-USER-581
  - TC-GS-USER-583
coverage:
  web: automated
---

# Role tanpa hak Update tidak dapat Edit, Toggle Active, dan Resend

## Prerequisites

Spec ini dijalankan untuk setiap role pada tabel. Langkahnya identik, hanya akun login dan keadaan yang diharapkan yang berbeda. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

Role yang diuji dan keadaan yang diharapkan pada baris target biasa:

| Role | Akun | Edit | Toggle Active | Resend Activation/Confirmation Email | Pair/Unpair TAG |
|---|---|---|---|---|---|
| Read Only | `readOnlyGlobalSettings_automated_qaTeam1` | Hidden | Disabled, tooltip "You don't have permission to edit" | Hidden | Tidak diverifikasi |
| Manage user and role (hanya Create) | `manageUserRoleCreateOnly_automated_qaTeam1` | Disabled, tooltip "You don't have permission to edit" | Disabled, tooltip "You don't have permission to edit" | Hidden | Hidden |
| Manage user and role (hanya Delete) | `manageUserRoleDeleteOnly_automated_qaTeam1` | Disabled, tooltip "You don't have permission to edit" | Disabled, tooltip "You don't have permission to edit" | Hidden | Hidden |

- Entity Client
- Ada minimal satu target User Basic biasa (bukan Total Control, Read Only, Default User, atau akun yang login) di User List

## Test Steps

Lakukan langkah 1–5 untuk setiap role pada tabel "Role yang diuji".

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Pada baris target biasa, verifikasi row action `Edit` sesuai kolom "Edit" pada tabel
3. Verifikasi Toggle Active sesuai kolom "Toggle Active" pada tabel, dan pada keadaan Disabled state toggle tetap terlihat
4. Verifikasi row action `Resend Activation/Confirmation Email` sesuai kolom pada tabel
5. Verifikasi `Pair/Unpair TAG` sesuai kolom pada tabel, kecuali untuk role dengan keterangan "Tidak diverifikasi"

## Notes

- Ini spec negatif Edit, Toggle Active, dan Resend dari Role Matrix (`docs/e2e-conventions.md` bagian 3a). Remove Access ikut tidak tersedia karena titik masuknya adalah Modal Edit. Pasangan positifnya adalah `TC-GS-USER-E2E-011-role-positif-edit-remove-access` dan `TC-GS-USER-E2E-012-role-positif-toggle-active`.
- Keadaan tiap elemen mengikuti tabel gerbang UI `user.md` §4.8: `Edit` dan Toggle Active digerbang Update (Disabled bila tidak punya, Hidden untuk Read Only), `Resend` dan `Pair/Unpair TAG` digerbang Update (Hidden bila tidak punya).
- `Pair/Unpair TAG` untuk Read Only tidak diverifikasi karena TC-GS-USER-08 dan 85 tidak menyebutnya, sedangkan TC-GS-USER-581 dan 583 menyebutnya untuk capability holder.
- Cara skrip menjalankan banyak role diputuskan di tahap script.
- Lapisan frontend mencakup TC-GS-USER-08 dan 85 dengan payload izin yang di-mock (TC-GS-USER-FE-018, 159). TC-GS-USER-581 dan 583 belum punya padanan frontend. TC-GS-USER-08 dan 85 berprioritas P0, jadi tumpang tindih disengaja (`docs/e2e-conventions.md` bagian 2).
- Spec ini tidak membuat atau mengubah data, jadi tidak butuh cleanup.

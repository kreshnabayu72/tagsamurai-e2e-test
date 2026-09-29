---
id: TC-GS-USER-E2E-015-role-negatif-create
title: Role tanpa hak Create tidak melihat tombol tambah user
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-08
  - TC-GS-USER-582
  - TC-GS-USER-583
coverage:
  web: automated
---

# Role tanpa hak Create tidak melihat tombol tambah user

## Prerequisites

Spec ini dijalankan untuk setiap role pada tabel. Langkahnya identik, hanya akun login yang berbeda. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

Role yang diuji:

| Role | Akun | Keterangan |
|---|---|---|
| Read Only | `readOnlyGlobalSettings_automated_qaTeam1` | Access level Read Only |
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` | Read baseline dan Update, tanpa Create dan Delete |
| Manage user and role (hanya Delete) | `manageUserRoleDeleteOnly_automated_qaTeam1` | Read baseline dan Delete, tanpa Create dan Update |

- Entity Client

## Test Steps

Lakukan langkah 1–2 untuk setiap role pada tabel "Role yang diuji".

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Verifikasi `[+ User]` tidak tampil (Hidden)

## Notes

- Ini spec negatif Create dari Role Matrix (`docs/e2e-conventions.md` bagian 3a). Pasangan positifnya adalah `TC-GS-USER-E2E-010-role-positif-create`.
- Keadaan `[+ User]` untuk capability holder mengikuti tabel gerbang UI `user.md` §4.8: tampil hanya jika role punya Create, selain itu Hidden.
- Cara skrip menjalankan banyak role diputuskan di tahap script.
- Lapisan frontend mencakup TC-GS-USER-08 dengan payload izin yang di-mock (TC-GS-USER-FE-018). TC-GS-USER-582 dan 583 belum punya padanan frontend. TC-GS-USER-08 berprioritas P0, jadi tumpang tindih disengaja (`docs/e2e-conventions.md` bagian 2).
- Spec ini tidak membuat atau mengubah data, jadi tidak butuh cleanup.

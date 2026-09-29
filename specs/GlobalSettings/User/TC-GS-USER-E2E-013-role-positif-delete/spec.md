---
id: TC-GS-USER-E2E-013-role-positif-delete
title: Role berhak Delete berhasil menghapus user
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-33
  - TC-GS-USER-396
  - TC-GS-USER-586
coverage:
  web: automated
---

# Role berhak Delete berhasil menghapus user

## Prerequisites

Spec ini dijalankan untuk setiap role pada tabel. Langkahnya identik, hanya akun login dan target yang berbeda. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

Role yang diuji dan target masing-masing:

| Role | Akun | Target |
|---|---|---|
| Total Control | `totalControl2_automated_qaTeam1` | "Dedi Kusuma" |
| Manage user and role (Full CRUD) | `manageUserRoleFull_automated_qaTeam1` | "Dodi Kusuma" |
| Manage user and role (hanya Delete) | `manageUserRoleDeleteOnly_automated_qaTeam1` | "Dani Kusuma" |

- Entity Client
- Setiap target adalah User Basic biasa tanpa borrowed asset dan tanpa pending approval (bukan Total Control, Read Only, Default User, atau akun yang login)

## Test Steps

Lakukan langkah 1–5 untuk setiap role pada tabel "Role yang diuji", dengan target milik role itu.

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Klik `Delete` pada baris target
3. Verifikasi dialog "Delete User" muncul dengan isi "• [Nama target]\nHistorical transaction data will be preserved.\nThis action cannot be undone. Are you sure you want to delete it?"
4. Klik `[Delete]` pada dialog
5. Verifikasi toast "Success, user has been deleted." muncul dan baris target tidak lagi muncul di User List

## Notes

- Ini spec positif Delete dari Role Matrix (`docs/e2e-conventions.md` bagian 3a). Pasangan negatifnya adalah `TC-GS-USER-E2E-017-role-negatif-delete`.
- Role Total Control mengulang sebagian alur `TC-GS-USER-E2E-005` (TC-GS-USER-33). Tumpang tindih ini disengaja.
- Cara skrip menjalankan banyak role diputuskan di tahap script.
- Lapisan frontend mencakup TC ini dengan payload izin yang di-mock (TC-GS-USER-FE-026, 074). TC-GS-USER-33 berprioritas P0, jadi tumpang tindih disengaja (`docs/e2e-conventions.md` bagian 2).
- Setiap target dihapus oleh spec ini sendiri, sehingga harus di-seed ulang sebelum setiap run.

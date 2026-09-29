---
id: TC-GS-USER-E2E-012-role-positif-toggle-active
title: Role berhak Update berhasil menonaktifkan user lewat Toggle Active
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-41
  - TC-GS-USER-584
  - TC-GS-USER-586
coverage:
  web: automated
---

# Role berhak Update berhasil menonaktifkan user lewat Toggle Active

## Prerequisites

Spec ini dijalankan untuk setiap role pada tabel. Langkahnya identik, hanya akun login dan target yang berbeda. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

Role yang diuji dan target masing-masing:

| Role | Akun | Target |
|---|---|---|
| Total Control | `totalControl2_automated_qaTeam1` | "Tito Nugroho" |
| Manage user and role (Full CRUD) | `manageUserRoleFull_automated_qaTeam1` | "Tama Nugroho" |
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` | "Toni Nugroho" |

- Entity Client
- Setiap target adalah User Basic biasa yang aktif di semua produk (bukan Total Control, Read Only, Default User, atau akun yang login)

## Test Steps

Lakukan langkah 1–5 untuk setiap role pada tabel "Role yang diuji", dengan target milik role itu.

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Klik Toggle Active [Global] pada baris target untuk mematikannya
3. Verifikasi dialog "Deactivate User" muncul dengan isi "• [Nama target]\nThis will deactivate user across all products. Are you sure you want to deactivate it?"
4. Klik `[Deactivate]` pada dialog
5. Verifikasi toast "Success, user has been deactivated." muncul dan Toggle Active [Global] target menjadi OFF

## Notes

- Ini spec positif Toggle Active dari Role Matrix (`docs/e2e-conventions.md` bagian 3a). Toggle Active digerbang izin Update (`user.md` §4.8). Pasangan negatifnya adalah `TC-GS-USER-E2E-016-role-negatif-edit-toggle-resend`.
- Role Total Control mengulang sebagian alur `TC-GS-USER-E2E-008` (TC-GS-USER-41). Tumpang tindih ini disengaja.
- Cara skrip menjalankan banyak role diputuskan di tahap script.
- Lapisan frontend mencakup TC ini dengan payload izin yang di-mock (TC-GS-USER-FE-087). TC-GS-USER-41 berprioritas P0, jadi tumpang tindih disengaja (`docs/e2e-conventions.md` bagian 2).
- Target harus diaktifkan kembali atau di-seed ulang setelah run.

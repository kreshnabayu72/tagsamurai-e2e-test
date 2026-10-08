---
id: TC-GS-USER-E2E-011-role-positif-edit-remove-access
title: Role berhak Update berhasil mengedit user dan mencabut Access
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-09
  - TC-GS-USER-395
  - TC-GS-USER-585
  - TC-GS-USER-586
coverage:
  web: automated
---

# Role berhak Update berhasil mengedit user dan mencabut Access

## Prerequisites

Spec ini dijalankan untuk setiap role pada tabel. Langkahnya identik, hanya akun login dan target yang berbeda. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

Role yang diuji dan target masing-masing:

| Role | Akun | Target Edit | Target Remove Access |
|---|---|---|---|
| Manage user and role (Full CRUD) | `manageUserRoleFull_automated_qaTeam1` | "Rian Pratama" | "Ella Wijaya" |
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` | "Rico Pratama" | "Elsa Wijaya" |

- Entity Client
- Setiap target Edit adalah User Basic biasa (bukan Total Control, Read Only, Default User, atau akun yang login) dengan Position "Staff"
- Setiap target Remove Access punya Access `[Global Settings, FAMS]`, tanpa aset atau approval di FAMS
- Position "Supervisor" ada di master data

## Test Steps

Lakukan langkah 1–9 untuk setiap role pada tabel "Role yang diuji", dengan target milik role itu.

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Buka Modal Edit pada target Edit
3. Ubah Position menjadi "Supervisor"
4. Klik `[Save]`
5. Verifikasi toast "Success, user has been updated." muncul dan baris target Edit menampilkan Position "Supervisor"
6. Buka Modal Edit pada target Remove Access
7. Hilangkan centang `FAMS` di field Access
8. Klik `[Save]`
9. Verifikasi tidak ada dialog tambahan, toast "Success, user has been updated." muncul, dan Access target Remove Access menjadi `[Global Settings]`

## Notes

- Ini spec positif Edit dan Remove Access dari Role Matrix (`docs/e2e-conventions.md` bagian 3a). Remove Access digerbang izin Update karena titik masuknya adalah Modal Edit (`user.md` §4.8, §9.2 [F-USER-03]). Pasangan negatifnya adalah `TC-GS-USER-E2E-016-role-negatif-edit-toggle-resend`.
- Role Total Control tidak diuji di sini karena Remove Access oleh Total Control sudah dicek di `TC-GS-USER-E2E-009` (TC-GS-USER-49).
- Cara skrip menjalankan banyak role diputuskan di tahap script.
- Lapisan frontend mencakup TC ini dengan payload izin yang di-mock (TC-GS-USER-FE-019, 025). TC-GS-USER-09 berprioritas P0, jadi tumpang tindih disengaja (`docs/e2e-conventions.md` bagian 2).
- Target Edit harus dikembalikan ke Position "Staff" dan target Remove Access harus di-seed ulang setelah run.

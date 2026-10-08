---
id: TC-GS-USER-E2E-134-role-positif-bulk-activate-deactivate
title: Role berhak Update berhasil menonaktifkan dan mengaktifkan beberapa user sekaligus
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-593
coverage:
  web: automated
---

# Role berhak Update berhasil menonaktifkan dan mengaktifkan beberapa user sekaligus

## Prerequisites

Spec ini memakai satu role. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

| Role | Akun |
|---|---|
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` |

- Entity Client
- Target "Ani Lestari" dan "Bayu Saputra" adalah User Basic biasa (bukan Total Control, Read Only, Default User, atau akun yang login), aktif, dan tidak Temporary-expired

## Test Steps

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Centang baris "Ani Lestari" dan "Bayu Saputra", lalu klik `Deactivate` pada bulk bar
3. Verifikasi dialog "Deactivate Users" memuat bullet kedua nama dan teks "They will be deactivated across all products. Are you sure you want to deactivate them?"
4. Klik `[Deactivate]` dan verifikasi toast "Success, user has been deactivated." muncul
5. Centang kedua baris yang sama lagi, lalu klik `Activate` pada bulk bar
6. Verifikasi dialog "Activate Users" memuat bullet kedua nama dan teks "They will be activated across all products. Are you sure you want to activate them?"
7. Klik `[Activate]` dan verifikasi toast "Success, user has been activated." muncul dan kedua target kembali aktif

## Notes

- Bulk bar hanya tampil untuk aktor yang punya Update atau Total Control (`user.md` §4.4). Kasus partial karena Temporary-expired diuji di spec Bulk milik Total Control.
- Kedua target kembali aktif di akhir spec, jadi tidak butuh cleanup.

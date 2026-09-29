---
id: TC-GS-USER-E2E-019-role-negatif-holder-ke-total-control
title: Capability holder Full CRUD diblokir pada target Total Control
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-339
  - TC-GS-USER-84
coverage:
  web: automated
---

# Capability holder Full CRUD diblokir pada target Total Control

## Prerequisites

Spec ini dijalankan untuk setiap role pada tabel. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

Role yang diuji:

| Role | Akun | Keterangan |
|---|---|---|
| Manage user and role (Full CRUD) | `manageUserRoleFull_automated_qaTeam1` | Bukan Total Control |

- Entity Client
- User "Siti Rahmawati" adalah Total Control biasa, bukan Default User
- Reset Authenticator adalah aksi yang endpoint-nya masih ditunda di modul. Spec ini hanya memverifikasi aksi itu tidak aktif dan tidak pernah menjalankannya

## Test Steps

Lakukan langkah 1–7 untuk setiap role pada tabel "Role yang diuji".

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Pada baris "Siti Rahmawati", verifikasi checkbox, tombol row action `(⋯)`, dan detail/read tetap tampil dan aktif, tidak Hidden
3. Verifikasi Toggle Active [Global] Disabled dengan tooltip "Only Default User or Total Control can edit users with Total Control or Read Only access."
4. Verifikasi row action `Delete` Disabled dengan tooltip yang sama
5. Buka Modal Edit "Siti Rahmawati" dan verifikasi checkbox Access, yang menjadi titik masuk Remove Access, Disabled dengan tooltip yang sama
6. Klik `✕` untuk menutup modal
7. Verifikasi row action `Reset Authenticator` Disabled dengan tooltip yang sama

## Notes

- Ini spec negatif capability holder terhadap target Total Control dari Role Matrix (`docs/e2e-conventions.md` bagian 3a), sesuai `USER-LOGIC-03`. Pasangan positifnya adalah `TC-GS-USER-E2E-014-role-positif-target-total-control`.
- Baris target tidak pernah Hidden karena "Manage user and role" adalah Global Role dengan cakupan seluruh entity (`user.md` §9.11). Hanya aksi tulis yang Disabled.
- Kombinasi capability holder parsial (hanya Create, Update, atau Delete) terhadap target Total Control tidak punya TC sumber, sehingga hanya role Full CRUD yang diuji di sini.
- Cara skrip menjalankan banyak role diputuskan di tahap script.
- Lapisan frontend mencakup TC ini dengan payload izin yang di-mock (TC-GS-USER-FE-023, 158).
- Spec ini tidak membuat atau mengubah data, jadi tidak butuh cleanup.

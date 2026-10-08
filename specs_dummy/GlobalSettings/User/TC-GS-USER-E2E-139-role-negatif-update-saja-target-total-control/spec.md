---
id: TC-GS-USER-E2E-139-role-negatif-update-saja-target-total-control
title: Role Update-saja tidak dapat mengelola user Total Control untuk enam aksi
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-598
coverage:
  web: automated
---

# Role Update-saja tidak dapat mengelola user Total Control untuk enam aksi

## Prerequisites

Spec ini memakai satu role. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

| Role | Akun |
|---|---|
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` |

- Entity Client
- User "Siti Rahmawati" adalah Total Control biasa, bukan Default User dan bukan akun yang login, Activated
- User "Tika Total" adalah Total Control biasa berstatus Pending Activation, untuk mengamati `Resend`
- Spec ini tidak membuat atau mengubah data

## Test Steps

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Pada baris "Siti Rahmawati", verifikasi checkbox dan tombol row action `(⋯)` tetap tampil dan aktif
3. Verifikasi Toggle Active [Global], row action `Edit`, dan row action `Delete` Disabled dengan tooltip "Only Default User or Total Control can edit users with Total Control or Read Only access."
4. Buka Modal Edit "Siti Rahmawati" dan verifikasi checkbox Access Disabled dengan tooltip yang sama
5. Klik `✕` untuk menutup modal
6. Buka User Detail "Siti Rahmawati" dan verifikasi tombol `Reset Authenticator` Disabled dengan tooltip yang sama, serta `Scan TAG` dan `Unpair` tidak tersedia
7. Pada baris "Tika Total", verifikasi row action `Resend Activation Email` tidak tersedia

## Notes

- Melengkapi `TC-GS-USER-E2E-019` yang memakai Full CRUD dan hanya empat aksi. Spec ini memakai hak Update-saja dan enam aksi (Toggle Active, Edit, Delete atau Remove Access, Reset Authenticator, Resend, Pair/Unpair). Berlaku `USER-LOGIC-03`.
- Spec ini tidak mengubah data, jadi tidak butuh cleanup.

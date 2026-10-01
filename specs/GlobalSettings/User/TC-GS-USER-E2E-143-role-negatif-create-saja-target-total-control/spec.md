---
id: TC-GS-USER-E2E-143-role-negatif-create-saja-target-total-control
title: Role Create-saja tidak dapat mengelola user Total Control
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-602
coverage:
  web: automated
---

# Role Create-saja tidak dapat mengelola user Total Control

## Prerequisites

Spec ini memakai satu role. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

| Role | Akun |
|---|---|
| Manage user and role (hanya Create) | `manageUserRoleCreateOnly_automated_qaTeam1` |

- Entity Client
- User "Siti Rahmawati" adalah Total Control biasa, bukan Default User dan bukan akun yang login
- Spec ini tidak membuat atau mengubah data

## Test Steps

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Verifikasi tombol `[+ User]` tampil
3. Pada baris "Siti Rahmawati", verifikasi checkbox dan tombol row action `(⋯)` tetap tampil dan aktif
4. Verifikasi row action `Edit`, row action `Delete`, dan Toggle Active [Global] Disabled

## Notes

- Hak Create tidak memberi akses atas target ber-tier Total Control. Melengkapi `TC-GS-USER-E2E-016` dan `017` yang memakai target biasa.
- Teks tooltip tidak diverifikasi karena prioritas tooltip tier dan generik tidak tegas di PRD. Lihat `GAP-297` di `foundation/prd-gap-registry.md`.
- Pasangan hak Update-saja adalah `TC-GS-USER-E2E-139`. Spec ini tidak mengubah data, jadi tidak butuh cleanup.

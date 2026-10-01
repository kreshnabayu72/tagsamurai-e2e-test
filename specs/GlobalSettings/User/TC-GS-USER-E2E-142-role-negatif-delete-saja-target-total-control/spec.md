---
id: TC-GS-USER-E2E-142-role-negatif-delete-saja-target-total-control
title: Role Delete-saja tidak dapat mengelola user Total Control
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-601
coverage:
  web: automated
---

# Role Delete-saja tidak dapat mengelola user Total Control

## Prerequisites

Spec ini memakai satu role. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

| Role | Akun |
|---|---|
| Manage user and role (hanya Delete) | `manageUserRoleDeleteOnly_automated_qaTeam1` |

- Entity Client
- User "Siti Rahmawati" adalah Total Control biasa, bukan Default User dan bukan akun yang login
- Spec ini tidak membuat atau mengubah data

## Test Steps

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Pada baris "Siti Rahmawati", verifikasi checkbox dan tombol row action `(⋯)` tetap tampil dan aktif
3. Verifikasi row action `Delete`, row action `Edit`, dan Toggle Active [Global] Disabled

## Notes

- Gerbang Delete tidak berlaku untuk target ber-tier Total Control (`USER-LOGIC-03`). Melengkapi `TC-GS-USER-E2E-015` dan `017` yang memakai target biasa.
- Teks tooltip tidak diverifikasi karena prioritas tooltip tier dan generik tidak tegas di PRD. Lihat `GAP-297` di `foundation/prd-gap-registry.md`.
- Pasangan hak Update-saja adalah `TC-GS-USER-E2E-139`. Spec ini tidak mengubah data, jadi tidak butuh cleanup.

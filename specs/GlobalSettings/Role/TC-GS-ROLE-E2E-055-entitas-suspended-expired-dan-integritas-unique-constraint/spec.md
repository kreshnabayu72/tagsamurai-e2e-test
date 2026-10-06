---
id: TC-GS-ROLE-E2E-055-entitas-suspended-expired-dan-integritas-unique-constraint
title: "Pemblokiran Aksi Tulis Saat Client Suspended atau Expired Serta Integritas Unique Constraint User-Role"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-112
  - TC-GS-ROLE-113
coverage:
  web: automated
---

# Pemblokiran Aksi Tulis Saat Client Suspended atau Expired Serta Integritas Unique Constraint User-Role

## Prerequisites

- Mode: mock
- Status client disimulasikan sebagai Suspended atau Expired
- Login sebagai Role: Total Control

## Test Steps

1. Simulasikan status entitas client berstatus Suspended atau Expired
2. Buka Global Settings > Role & Permission
3. Verifikasi seluruh tombol aksi tulis ([+ Assign], checkbox CRUD, dan row action Remove) diblokir atau dinonaktifkan
4. Coba submit aksi penugasan atau perubahan izin
5. Verifikasi server menolak aksi tulis dengan status 403 atau pesan penolakan lisensi
6. Pulihkan status client ke aktif
7. Verifikasi integritas database: 1 user tidak dapat memiliki lebih dari 1 baris assignment untuk role yang sama di tabel Detail

## Notes

- Status client Suspended/Expired memblokir seluruh aksi mutasi tulis (role.md §9.4 D1).

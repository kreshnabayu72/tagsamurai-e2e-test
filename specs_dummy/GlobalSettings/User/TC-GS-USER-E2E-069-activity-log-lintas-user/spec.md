---
id: TC-GS-USER-E2E-069-activity-log-lintas-user
title: 'Activity Log level Global Settings menampilkan aksi semua user'
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-116
coverage:
  web: automated
---

# Activity Log level Global Settings menampilkan aksi semua user

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Sudah ada aktivitas dari sedikitnya dua aktor berbeda (Create, Edit, Delete, atau Toggle) pada beberapa user
- Spec ini tidak mengubah data

## Test Steps

1. Buka Global Settings > Activity Log (menu tingkat atas, bukan Tab di User Detail)
2. Verifikasi tabel menampilkan aksi dari lebih dari satu user dan lebih dari satu jenis aksi
3. Verifikasi tabel tidak difilter ke satu user tertentu

## Notes

- Sumber `user.md` bagian 8. Isi baris per aksi diverifikasi di spec masing-masing aksi (mis. `TC-GS-USER-E2E-002-create-users-success-flow-stay-open`).

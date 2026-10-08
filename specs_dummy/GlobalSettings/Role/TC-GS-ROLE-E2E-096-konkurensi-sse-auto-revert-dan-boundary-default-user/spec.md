---
id: TC-GS-ROLE-E2E-096-konkurensi-sse-auto-revert-dan-boundary-default-user
title: "Konkurensi Antar-Admin: Sinkronisasi SSE Realtime Auto-Revert Lintas Tab dan Batas Proteksi Default User"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-277
  - TC-GS-ROLE-278
coverage:
  web: automated
---

# Konkurensi Antar-Admin: Sinkronisasi SSE Realtime Auto-Revert Lintas Tab dan Batas Proteksi Default User

## Prerequisites

- Dual session context dengan SSE connection aktif; Sesi Budi Santoso
- Data Uji: Indra Gunawan (Dinamis #8), Budi Santoso, Eko Prasetyo
- Setup Hook: dualContext: sessionA, sessionB
- Admin B membuka Tab Total Control (sesi B)
- Login sbg Role: Total Control di sesi A
- Indra Gunawan (Pre-setup #18) Total Control (Given)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Total Control: Budi Santoso (Default), Ahmad Fauzi, Eko Prasetyo

## Test Steps

### Auto-revert menghilangkan user dari Tab Total Control sesi admin lain secara realtime (TC-GS-ROLE-277)

1. Sesi A: auto-revert Indra Gunawan lewat Edit CRUD > [Remove]
2. Sesi B: amati tanpa reload
3. Verifikasi Indra Gunawan hilang dari Tab Total Control sesi B tanpa reload

### Default User tetap Total Control setelah semua Total Control lain di-Remove (TC-GS-ROLE-278)

4. Login sbg Eko Prasetyo: Remove Total Control Ahmad Fauzi
5. Login sbg Budi Santoso: Remove Total Control Eko Prasetyo
6. Amati Tab Total Control
7. Verifikasi Kedua Remove sukses tanpa pemeriksaan jumlah
8. Verifikasi Tab Total Control hanya berisi Budi Santoso
9. Verifikasi Remove Budi Santoso disabled

## Notes

- Memvalidasi alur skenario "Konkurensi Antar-Admin: Sinkronisasi SSE Realtime Auto-Revert Lintas Tab dan Batas Proteksi Default User".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.2 [F-ROLE-06]; foundation/process/prd-process/error-handling-convention.md §5.4; global-settings/role/PRD/role.md ROLE-LOGIC-02e; global-settings/role/PRD/role.md §9.2 [F-ROLE-05].
- Sumber pemetaan test case granular: TC-GS-ROLE-277, TC-GS-ROLE-278.

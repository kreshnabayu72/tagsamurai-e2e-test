---
id: TC-GS-POS-E2E-053-state-tenant-write-lockdown-entitas-suspended-expired-dan-plan-matrix
title: "State Tenant: Write-lockdown pada entitas Suspended/Expired (Create, Edit, Delete ditolak) dan independensi plan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-268
  - TC-GS-POS-272
  - TC-GS-POS-273
  - TC-GS-POS-274
coverage:
  web: automated
---

# State Tenant: Write-lockdown pada entitas Suspended/Expired (Create, Edit, Delete ditolak) dan independensi plan

## Prerequisites

- Entitas Client Suspended / Expired tersedia
- Akun pada entitas paket Starter, Growth, Professional, dan Enterprise

## Test Steps

### Write-Lockdown pada Entitas Suspended/Expired

1. Login ke entitas yang berstatus "Suspended" atau "Expired"
2. Buka Global Settings > User > Position
3. Coba lakukan Create Position, verifikasi aksi ditolak server dengan pesan entitas non-aktif
4. Coba lakukan Edit Position pada record yang ada, verifikasi simpan ditolak
5. Coba lakukan Delete Position, verifikasi penghapusan ditolak

### Parity Antar Paket Lisensi (Tanpa Plan Gating)

6. Login bergantian ke entitas dengan plan Starter, Growth, Professional, dan Enterprise
7. Buka tab Position pada masing-masing entitas
8. Verifikasi seluruh fitur tabel, Create, Edit, Delete, dan Changelog tersedia identik tanpa ada batasan plan gating

## Notes

- Menggabungkan TC-GS-POS-268, 272, 273, dan 274 dalam kelas State Tenant.

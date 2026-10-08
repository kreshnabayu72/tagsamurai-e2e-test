---
id: TC-GS-ROLE-E2E-085-plan-gating-dan-isolasi-scope-produk
title: "Ketersediaan Modul pada Semua Tier Paket Langganan dan Isolasi Hak Akses Khusus Global Settings"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-246
  - TC-GS-ROLE-283
coverage:
  web: automated
---

# Ketersediaan Modul pada Semua Tier Paket Langganan dan Isolasi Hak Akses Khusus Global Settings

## Prerequisites

- Client tenant Starter, Growth, Professional, Enterprise (Pre-setup #16)
- Data Uji: Pre-setup #16
- Setup Hook: beforeEach: switchTenantPlan()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Client uji pada plan Starter, Growth, Professional, Enterprise (Pre-setup #16)
- Sari Wulandari punya akses Admin Console tanpa access level Admin Console

## Test Steps

### Fitur ber-plan tetap muncul sebagai role di semua plan (TC-GS-ROLE-246)

1. Pada tiap plan buka Tab System
2. Lakukan Assign Role Manage TAG ke 1 user
3. Verifikasi Keenam role tampil di tiap plan
4. Verifikasi Assign Role sukses dengan toast "Success, role has been assigned." di tiap plan

### Assign Total Control Global Settings tidak mengubah akses produk lain (TC-GS-ROLE-283)

5. Assign Total Control Global Settings ke Sari Wulandari
6. Buka Admin Console > Settings > Role & Permission > Tab Total Control
7. Verifikasi Sari Wulandari tampil di Tab Total Control Global Settings
8. Verifikasi Sari Wulandari tidak tampil di Tab Total Control Admin Console; akses Admin Console-nya tidak berubah

## Notes

- Memvalidasi alur skenario "Ketersediaan Modul pada Semua Tier Paket Langganan dan Isolasi Hak Akses Khusus Global Settings".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.10; global-settings/role/PRD/role.md §9.4.1 D2; global-settings/role/PRD/role.md §9.4.1 D8; global-settings/role/PRD/role.md §11 Catatan Lintas-Modul Role per-produk.
- Sumber pemetaan test case granular: TC-GS-ROLE-246, TC-GS-ROLE-283.

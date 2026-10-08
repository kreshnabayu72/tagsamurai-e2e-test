---
id: TC-GS-ROLE-E2E-092-client-suspended-akses-baca-murni-seluruh-surface
title: "Client Suspended: Akses Baca Murni Seluruh Tab dan Detail Berfungsi Normal Tanpa Gangguan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-271
coverage:
  web: automated
---

# Client Suspended: Akses Baca Murni Seluruh Tab dan Detail Berfungsi Normal Tanpa Gangguan

## Prerequisites

- Login sebagai Total Control pada tenant Client C berstatus Suspended
- Data Uji: Pre-setup #16
- Setup Hook: before: setTenantSuspended()
- Login sbg Role: Total Control pada client suspended

## Test Steps

### Client suspended tetap dapat melihat Role & Permission (TC-GS-ROLE-271)

1. Buka Tab Total Control, Read Only, System, Detail
2. Verifikasi Semua tab dan Detail termuat normal

## Notes

- Memvalidasi alur skenario "Client Suspended: Akses Baca Murni Seluruh Tab dan Detail Berfungsi Normal Tanpa Gangguan".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.4.1 D1.
- Sumber pemetaan test case granular: TC-GS-ROLE-271.

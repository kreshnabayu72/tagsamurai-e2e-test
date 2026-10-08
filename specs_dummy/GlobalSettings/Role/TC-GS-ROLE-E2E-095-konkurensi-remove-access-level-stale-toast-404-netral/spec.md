---
id: TC-GS-ROLE-E2E-095-konkurensi-remove-access-level-stale-toast-404-netral
title: "Konkurensi Antar-Admin Remove Access Level: Toast 404 Netral Saat Target Sudah Dihapus Admin Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-275
coverage:
  web: automated
---

# Konkurensi Antar-Admin Remove Access Level: Toast 404 Netral Saat Target Sudah Dihapus Admin Lain

## Prerequisites

- Dual session context (Sesi A dan Sesi B Total Control)
- Data Uji: Joko Prasetyo (Pre-setup #18)
- Setup Hook: dualContext: sessionA, sessionB
- Dua admin Total Control (sesi A, B)
- Joko Prasetyo (Pre-setup #18) Total Control (Given)

## Test Steps

### Remove access level saat target sudah di-Remove admin lain sejak render (TC-GS-ROLE-275)

1. Sesi A membuka Tab Total Control
2. Sesi B: Remove Total Control Joko Prasetyo
3. Sesi A: Remove baris Joko Prasetyo > [Remove]
4. Verifikasi Muncul toast netral: "This access level is no longer available."
5. Verifikasi Tab Total Control di-refresh, Joko Prasetyo tidak ada
6. Verifikasi Tidak ada dialog, tidak ada toast sukses, dan tidak ada entry Remove kedua di Changelog

## Notes

- Memvalidasi alur skenario "Konkurensi Antar-Admin Remove Access Level: Toast 404 Netral Saat Target Sudah Dihapus Admin Lain".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.4.2 D6; global-settings/role/PRD/role.md §4.4 Target sudah tidak tersedia (404); foundation/process/prd-process/error-handling-convention.md §2.
- Sumber pemetaan test case granular: TC-GS-ROLE-275.

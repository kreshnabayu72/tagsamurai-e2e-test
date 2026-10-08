---
id: TC-GS-ROLE-E2E-020-gating-seleksi-bulk-action-bar-per-aktor
title: "Gating Seleksi Checkbox Baris Bulk Action Bar pada Detail Berdasarkan Tingkat Wewenang Aktor"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-49
  - TC-GS-ROLE-50
coverage:
  web: automated
---

# Gating Seleksi Checkbox Baris Bulk Action Bar pada Detail Berdasarkan Tingkat Wewenang Aktor

## Prerequisites

- Login sebagai Total Control (Ahmad Fauzi) lalu Manage user and role (Hendra Wijaya)
- Data Uji: Pre-setup #1, #2, #4, #5, #10
- Setup Hook: beforeEach: switchActor()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Detail "Manage TAG" berisi Ahmad Fauzi, Budi Santoso, Dewi Lestari, Doni Pratama, Siti Nurhaliza
- Login sbg Role: Manage user and role C/R/U/D (Hendra Wijaya)

## Test Steps

### Checkbox seleksi Detail untuk aktor Total Control dan Select All mengecualikan baris disabled (TC-GS-ROLE-49)

1. Buka Detail "Manage TAG"
2. Klik button Select All di Bulk Action toolbar
3. Amati baris yang terselect
4. Verifikasi Checkbox Ahmad Fauzi dan Budi Santoso tidak pernah checked
5. Verifikasi Dewi Lestari, Doni Pratama, Siti Nurhaliza checked
6. Verifikasi Angka pada button Select All dan counter = 3

### Checkbox seleksi Detail untuk aktor Manage user and role Update (TC-GS-ROLE-50)

7. Buka Detail "Manage TAG"
8. Klik button Select All
9. Verifikasi Checkbox Hendra Wijaya, Budi Santoso, Ahmad Fauzi (TC), Dewi Lestari (TC), Siti Nurhaliza (RO) tetap disabled
10. Verifikasi Hanya baris user tanpa access level (Doni Pratama) yang terselect; angka Select All = jumlah baris itu

## Notes

- Memvalidasi alur skenario "Gating Seleksi Checkbox Baris Bulk Action Bar pada Detail Berdasarkan Tingkat Wewenang Aktor".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Bulk Action Bar — Detail; global-settings/role/PRD/role.md §4.8 Bulk; foundation/process/prd-process/prd-conventions.md §8; global-settings/role/PRD/role.md §9.4.2 Remove Role Assignment (bulk) D9.
- Sumber pemetaan test case granular: TC-GS-ROLE-49, TC-GS-ROLE-50.

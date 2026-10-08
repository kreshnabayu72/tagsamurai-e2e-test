---
id: TC-GS-ROLE-E2E-036-remove-total-control-happy-path-dan-user-inactive
title: "Pencabutan Total Control Berhasil pada User Aktif dan User Inactive Tanpa Batasan Kuota Minimum"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-86
  - TC-GS-ROLE-87
coverage:
  web: automated
---

# Pencabutan Total Control Berhasil pada User Aktif dan User Inactive Tanpa Batasan Kuota Minimum

## Prerequisites

- Login sebagai Total Control
- Data Uji: Dewi Lestari (Inactive), Sari Wulandari (Active)
- Setup Hook: beforeEach: navigateTo(Tab Total Control)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > Total Control
- Sari Wulandari Total Control
- Dewi Lestari Total Control, user Inactive

## Test Steps

### Remove Total Control dari user (TC-GS-ROLE-86)

1. Klik Remove baris Sari Wulandari
2. Klik [Remove]
3. Buka Tab System
4. Buka Detail "Manage TAG"
5. Verifikasi Muncul toast sukses: "Success, Total Control has been removed."
6. Verifikasi Sari Wulandari hilang dari Tab Total Control
7. Verifikasi Kolom Users keenam role berkurang 1
8. Verifikasi Sari Wulandari tidak ada di Detail "Manage TAG" maupun Detail role lain

### Remove Total Control user Inactive tanpa batasan jumlah Total Control (TC-GS-ROLE-87)

9. Klik Remove baris Dewi Lestari
10. Klik [Remove]
11. Verifikasi Toast sukses: "Success, Total Control has been removed."
12. Verifikasi Dewi Lestari hilang dari Tab Total Control tanpa peringatan jumlah Total Control

## Notes

- Memvalidasi alur skenario "Pencabutan Total Control Berhasil pada User Aktif dan User Inactive Tanpa Batasan Kuota Minimum".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.4 D-01; global-settings/role/PRD/role.md §9.2 [F-ROLE-05]; global-settings/role/PRD/role.md §9.7.
- Sumber pemetaan test case granular: TC-GS-ROLE-86, TC-GS-ROLE-87.

---
id: TC-GS-ROLE-E2E-017-guard-proteksi-default-user-dan-self-edit-pada-detail
title: "Guard Proteksi Default User dan Self-Edit pada Halaman Detail: Checkbox dan Aksi Remove Disabled"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-41
  - TC-GS-ROLE-42
  - TC-GS-ROLE-45
coverage:
  web: automated
---

# Guard Proteksi Default User dan Self-Edit pada Halaman Detail: Checkbox dan Aksi Remove Disabled

## Prerequisites

- Login sebagai Total Control (Ahmad Fauzi) dan Budi Santoso (Default User)
- Data Uji: Pre-setup #1, #2
- Setup Hook: beforeEach: navigateTo(Detail Manage user and role)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Ahmad Fauzi punya baris role Manage TAG (bulk-write Total Control)
- User berada di Global Settings > Role & Permission > Total Control
- Login sbg Role: Total Control (Budi Santoso, Default User)

## Test Steps

### Detail untuk aktor Total Control — baris diri sendiri, Default User, dan target TC/RO (TC-GS-ROLE-41)

1. Buka Detail "Manage TAG"
2. Hover checkbox Update, Remove, dan checkbox seleksi pada baris Ahmad Fauzi, Budi Santoso, Dewi Lestari, Siti Nurhaliza
3. Verifikasi Ahmad Fauzi: checkbox Update, Remove, checkbox seleksi tetap tampil namun disabled; tooltip "You can't manage your own account from here."
4. Verifikasi Budi Santoso: checkbox Update, Remove, checkbox seleksi disabled; tooltip "Default User cannot be modified."
5. Verifikasi Dewi Lestari (TC) dan Siti Nurhaliza (RO): checkbox Update, Remove, checkbox seleksi enabled

### Remove di Tab Total Control untuk Default User dan diri sendiri (TC-GS-ROLE-42)

6. Buka overlay (⋯) baris Budi Santoso dan hover Remove
7. Buka overlay (⋯) baris Ahmad Fauzi dan hover Remove
8. Buka overlay (⋯) baris Dewi Lestari
9. Verifikasi Budi Santoso: Remove tampil disabled; tooltip "Default User cannot be modified."
10. Verifikasi Ahmad Fauzi: Remove disabled; tooltip "You can't manage your own account from here."
11. Verifikasi Dewi Lestari: Remove enabled, icon DeleteBin6Line severity danger

### Prioritas tooltip — Default User login melihat barisnya sendiri (TC-GS-ROLE-45)

12. Buka Detail "Manage TAG", hover checkbox Update, Remove, checkbox seleksi baris Budi Santoso
13. Buka Tab Total Control, hover Remove baris Budi Santoso
14. Verifikasi Detail: ketiga elemen tetap disabled; tooltip "Default User cannot be modified."
15. Verifikasi Tab Total Control: Remove disabled; tooltip "Default User cannot be modified."

## Notes

- Memvalidasi alur skenario "Guard Proteksi Default User dan Self-Edit pada Halaman Detail: Checkbox dan Aksi Remove Disabled".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.8; global-settings/role/PRD/role.md §2.3; global-settings/role/PRD/role.md §4.3; global-settings/role/PRD/role.md §4.3 Row Action Remove — Tab Total Control / Tab Read Only; global-settings/role/PRD/role.md §4.1 Row Actions; global-settings/role/PRD/role.md §4.3 Prioritas tooltip.
- Sumber pemetaan test case granular: TC-GS-ROLE-41, TC-GS-ROLE-42, TC-GS-ROLE-45.

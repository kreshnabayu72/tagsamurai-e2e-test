---
id: TC-GS-ROLE-E2E-056-bulk-remove-tepat-satu-baris-fallback-dialog-single
title: "Fallback Bulk Remove Tepat 1 Baris: Pemakaian Otomatis Dialog Single D-03 dan Single Auto-Revert D-04"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-294
  - TC-GS-ROLE-295
coverage:
  web: automated
---

# Fallback Bulk Remove Tepat 1 Baris: Pemakaian Otomatis Dialog Single D-03 dan Single Auto-Revert D-04

## Prerequisites

- Login sebagai Total Control
- Data Uji: Nina Kartika (Regular), Rina Putri (RO)
- Setup Hook: beforeEach: navigateTo(Detail)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage hardware"
- Nina Kartika punya baris Manage hardware, tanpa access level
- User berada di Global Settings > Role & Permission > System > Detail "Manage master reference"
- Rina Putri Read Only (Given: di-assign Read Only ulang)

## Test Steps

### Bulk Remove tepat 1 baris memakai dialog single (target bukan Total Control/Read Only) (TC-GS-ROLE-294)

1. Centang Nina Kartika saja
2. Klik Bulk Action > Remove
3. Screening dialog
4. Klik [Remove]
5. Verifikasi Counter "1 User selected"
6. Verifikasi Dialog Title "Remove Access"; body "• Nina Kartika" + "This will remove Manage hardware access from this user. Are you sure you want to remove it?" (bukan varian bulk "remove them?")
7. Verifikasi Tombol `[Cancel]` | `[Remove]` (danger)
8. Verifikasi Muncul toast sukses: "Success, user has been removed."
9. Verifikasi Baris Nina Kartika hilang; Bulk Action Bar tertutup

### Bulk Remove tepat 1 baris target Read Only memakai dialog single auto-revert (TC-GS-ROLE-295)

10. Centang Rina Putri saja
11. Klik Bulk Action > Remove
12. Screening dialog
13. Klik [Remove]
14. Buka Tab Read Only
15. Verifikasi Dialog Title "Remove Access"; body "• Rina Putri" + "Editing this permission will remove Read Only access from this user. Are you sure you want to remove it?"
16. Verifikasi Tombol `[Cancel]` | `[Remove]` (danger)
17. Verifikasi Muncul toast sukses: "Success, user has been removed."
18. Verifikasi Baris Rina Putri hilang dari Detail dan Rina Putri hilang dari Tab Read Only
19. Verifikasi Bulk Action Bar tertutup

## Notes

- Memvalidasi alur skenario "Fallback Bulk Remove Tepat 1 Baris: Pemakaian Otomatis Dialog Single D-03 dan Single Auto-Revert D-04".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.4 D-03; global-settings/role/PRD/role.md §4.4 Bulk; foundation/functions/toast-copy.md Aturan Terkunci #7; global-settings/role/PRD/role.md §4.4 D-04.
- Sumber pemetaan test case granular: TC-GS-ROLE-294, TC-GS-ROLE-295.

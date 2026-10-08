---
id: TC-GS-ROLE-E2E-049-remove-role-assignment-single-auto-revert-tc-dan-ro
title: "Pencabutan Baris Role Assignment Memunculkan Dialog Auto-Revert D-04 untuk Target TC dan RO"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-114
  - TC-GS-ROLE-115
  - TC-GS-ROLE-116
coverage:
  web: automated
---

# Pencabutan Baris Role Assignment Memunculkan Dialog Auto-Revert D-04 untuk Target TC dan RO

## Prerequisites

- Login sebagai Total Control
- Data Uji: Rudi Hartono (TC, Dinamis #2), Rina Putri (RO, Pre-setup #4)
- Setup Hook: beforeEach: navigateTo(Detail)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage files"
- Rudi Hartono Total Control
- Rina Putri Read Only
- Siti Nurhaliza Total Control

## Test Steps

### Remove baris role target Total Control memicu dialog auto-revert (TC-GS-ROLE-114)

1. Klik Remove baris Rudi Hartono
2. Screening dialog
3. Klik [Remove]
4. Buka Tab Total Control
5. Buka Detail "Manage TAG"
6. Verifikasi Dialog Title "Remove Access"; body "• Rudi Hartono" + "Editing this permission will remove Total Control access from this user. Are you sure you want to remove it?"; `[Cancel]` | `[Remove]` (danger)
7. Verifikasi Toast sukses: "Success, permissions have been updated. Rudi Hartono is no longer Total Control."
8. Verifikasi Baris Rudi Hartono hilang dari Detail "Manage files"; Rudi hilang dari Tab Total Control
9. Verifikasi Baris Rudi Hartono di Detail "Manage TAG" tetap ada dengan R,U checked

### Remove baris role target Read Only memicu dialog auto-revert (TC-GS-ROLE-115)

10. Klik Remove baris Rina Putri
11. Klik [Remove]
12. Verifikasi Body dialog menyebut "Read Only"
13. Verifikasi Toast sukses: "Success, permissions have been updated. Rina Putri is no longer Read Only."
14. Verifikasi Rina Putri hilang dari Tab Read Only

### Cancel dialog auto-revert dari Remove baris (TC-GS-ROLE-116)

15. Klik Remove baris Siti Nurhaliza
16. Klik [Cancel]
17. Verifikasi Baris tetap ada
18. Verifikasi Siti Nurhaliza tetap di Tab Total Control
19. Verifikasi Tidak ada toast

## Notes

- Memvalidasi alur skenario "Pencabutan Baris Role Assignment Memunculkan Dialog Auto-Revert D-04 untuk Target TC dan RO".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.4 D-04; global-settings/role/PRD/role.md §9.2 [F-ROLE-07]; global-settings/role/PRD/role.md §7.1 T-09; global-settings/role/PRD/role.md §4.4.
- Sumber pemetaan test case granular: TC-GS-ROLE-114, TC-GS-ROLE-115, TC-GS-ROLE-116.

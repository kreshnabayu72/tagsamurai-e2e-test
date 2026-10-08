---
id: TC-GS-ROLE-E2E-045-edit-crud-detail-auto-revert-total-control-user
title: "Auto-Revert pada Edit CRUD: Dialog D-02 Saat Uncheck Sel User Total Control dan Pencabutan Akses TC"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-104
  - TC-GS-ROLE-105
  - TC-GS-ROLE-106
coverage:
  web: automated
---

# Auto-Revert pada Edit CRUD: Dialog D-02 Saat Uncheck Sel User Total Control dan Pencabutan Akses TC

## Prerequisites

- Login sebagai Total Control; Maya Anggraini berstatus Total Control
- Data Uji: Maya Anggraini (Pre-setup #11 / Dinamis #2)
- Setup Hook: beforeEach: navigateTo(Detail)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage TAG"
- Maya Anggraini Total Control
- Maya Anggraini Total Control dengan keenam role CRUD penuh

## Test Steps

### Screening dialog auto-revert saat mengedit role user Total Control (TC-GS-ROLE-104)

1. Uncheck Update baris Maya Anggraini
2. Screening dialog
3. Verifikasi Title "Remove Access"
4. Verifikasi Body "• Maya Anggraini" + "Editing this permission will remove Total Control access from this user. Are you sure you want to remove it?"
5. Verifikasi Tombol `[Cancel]` (contrast) | `[Remove]` (danger)
6. Verifikasi Belum ada toast dan belum ada perubahan tersimpan

### Cancel dialog auto-revert (TC-GS-ROLE-105)

7. Uncheck Update baris Maya Anggraini
8. Klik [Cancel]
9. Buka Tab Total Control
10. Verifikasi Checkbox Update kembali checked
11. Verifikasi Tidak ada toast
12. Verifikasi Maya Anggraini tetap di Tab Total Control
13. Verifikasi Changelog "Manage TAG" tidak memuat entry baru untuk Maya Anggraini

### Konfirmasi auto-revert user Total Control (TC-GS-ROLE-106)

14. Uncheck Update baris Maya Anggraini
15. Klik [Remove]
16. Buka Tab Total Control
17. Buka Detail "Manage user and role" dan "Import data"
18. Verifikasi Muncul toast sukses (template "Success, permissions have been updated. [User Name] is no longer Total Control/Read Only."): "Success, permissions have been updated. Maya Anggraini is no longer Total Control."
19. Verifikasi Maya Anggraini hilang dari Tab Total Control
20. Verifikasi Detail "Manage TAG": Read checked, Update unchecked
21. Verifikasi Detail "Manage user and role": C,R,U,D tetap checked; Detail "Import data": C,R tetap checked

## Notes

- Memvalidasi alur skenario "Auto-Revert pada Edit CRUD: Dialog D-02 Saat Uncheck Sel User Total Control dan Pencabutan Akses TC".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.4 D-02; global-settings/role/PRD/role.md ROLE-LOGIC-04; global-settings/role/PRD/role.md §3 Alur auto-revert; global-settings/role/PRD/role.md §9.2 [F-ROLE-06]; global-settings/role/PRD/role.md §7.1 T-07; global-settings/role/PRD/role.md ROLE-LOGIC-04a; global-settings/role/PRD/role.md ROLE-LOGIC-04b.
- Sumber pemetaan test case granular: TC-GS-ROLE-104, TC-GS-ROLE-105, TC-GS-ROLE-106.

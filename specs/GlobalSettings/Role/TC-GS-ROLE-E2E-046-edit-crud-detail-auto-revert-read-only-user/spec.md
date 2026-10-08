---
id: TC-GS-ROLE-E2E-046-edit-crud-detail-auto-revert-read-only-user
title: "Auto-Revert pada Edit CRUD: Dialog D-02 Saat Check Sel Tulis User Read Only dan Pencabutan Hak RO"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-107
  - TC-GS-ROLE-108
coverage:
  web: automated
---

# Auto-Revert pada Edit CRUD: Dialog D-02 Saat Check Sel Tulis User Read Only dan Pencabutan Hak RO

## Prerequisites

- Login sebagai Total Control; Wawan Setiawan berstatus Read Only
- Data Uji: Wawan Setiawan (Pre-setup #11 / Dinamis #7)
- Setup Hook: beforeEach: navigateTo(Detail)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage hardware"
- Wawan Setiawan di-assign Read Only (Tab Read Only > [+ Assign])
- User berada di Global Settings > Role & Permission > System > Detail "Manage TAG"
- Response Edit CRUD dibuat gagal 5xx

## Test Steps

### Konfirmasi auto-revert user Read Only (TC-GS-ROLE-107)

1. Centang Create baris Wawan Setiawan
2. Amati dialog
3. Klik [Remove]
4. Buka Tab Read Only
5. Verifikasi Body dialog "• Wawan Setiawan" + "Editing this permission will remove Read Only access from this user. Are you sure you want to remove it?"
6. Verifikasi Toast sukses: "Success, permissions have been updated. Wawan Setiawan is no longer Read Only."
7. Verifikasi Wawan Setiawan hilang dari Tab Read Only; Create checked di Manage hardware

### Edit CRUD gagal 5xx pada target biasa (TC-GS-ROLE-108)

8. Centang Update baris Wawan Setiawan
9. Verifikasi Muncul toast error: "Error, failed to update permissions."
10. Verifikasi Checkbox Update kembali ke nilai tersimpan (unchecked)
11. Verifikasi Setelah reload Update tetap unchecked; retry dilakukan dengan mencentang ulang

## Notes

- Memvalidasi alur skenario "Auto-Revert pada Edit CRUD: Dialog D-02 Saat Check Sel Tulis User Read Only dan Pencabutan Hak RO".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.4 D-02; global-settings/role/PRD/role.md §7.1 T-07; global-settings/role/PRD/role.md §7.1 T-01; global-settings/role/PRD/role.md §9.6 Edit CRUD.
- Sumber pemetaan test case granular: TC-GS-ROLE-107, TC-GS-ROLE-108.

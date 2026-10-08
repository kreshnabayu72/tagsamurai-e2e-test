---
id: TC-GS-ROLE-E2E-079-audit-log-immutability-rename-user-dan-fan-out-modul-user
title: "Immutability Snapshot Nama User Pasca-Rename, Segregasi Changelog User vs User > Role, dan Update Modified By"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-220
  - TC-GS-ROLE-223
  - TC-GS-ROLE-224
  - TC-GS-ROLE-225
  - TC-GS-ROLE-290
coverage:
  web: automated
---

# Immutability Snapshot Nama User Pasca-Rename, Segregasi Changelog User vs User > Role, dan Update Modified By

## Prerequisites

- Login sebagai Total Control
- Data Uji: Modul User Changelog & User Detail Tab Role
- Setup Hook: beforeEach: navigateTo(User Changelog)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Ada entry Assign untuk Sari Wulandari
- Siti Nurhaliza di-upgrade ke Total Control oleh Ahmad Fauzi; sebelumnya RO oleh Budi Santoso

## Test Steps

### Entry log lama tidak berubah setelah user di-rename (TC-GS-ROLE-220)

1. Rename Sari Wulandari menjadi Sari Wulandari Putri di modul User
2. Buka Changelog Tab Total Control
3. Verifikasi Entry lama tetap User Name "Sari Wulandari"
4. Verifikasi Entry baru setelah rename memakai nama baru

### Changelog: User mencatat aksi access level dan role; Changelog: User > Role hanya aksi per-role (TC-GS-ROLE-223)

5. Buka Global Settings > User > Sari Wulandari > Changelog
6. Buka Changelog: User > Role milik Maya Anggraini
7. Verifikasi Changelog: User Sari Wulandari memuat entry Assign dan Remove Access Level
8. Verifikasi Changelog: User > Role Maya Anggraini memuat entry Edit Manage TAG Update
9. Verifikasi Changelog: User > Role Maya Anggraini tidak memuat entry Auto-Revert

### Assign Total Control tidak menulis entry ke Changelog: User > Role (TC-GS-ROLE-224)

10. Buka Changelog: User > Role milik Sari Wulandari
11. Verifikasi Tidak ada entry per-role akibat Assign Total Control; tab menampilkan "No changelog yet" atau entry lain yang tidak terkait

### Modified By dan Last Updated hanya diperbarui oleh Assign (TC-GS-ROLE-225)

12. Tab Total Control: amati Modified By dan Last Updated Siti Nurhaliza
13. Verifikasi Modified By "Ahmad F"
14. Verifikasi Last Updated = waktu upgrade

### Changelog: User > Role mencatat Assign/Remove baris role; Changelog: User mencatat Auto-Revert (TC-GS-ROLE-290)

15. Buka Global Settings > User > Wawan Setiawan > Changelog: User > Role
16. Buka Global Settings > User > Doni Pratama > Changelog: User > Role
17. Buka Global Settings > User > Maya Anggraini > Changelog: User
18. Verifikasi Wawan Setiawan: entry Assign "Manage TAG", Field Access, Old "—", New "Assigned"
19. Verifikasi Doni Pratama: entry Remove "Manage TAG", Field Access, Old "Assigned", New "—"
20. Verifikasi Maya Anggraini: Changelog: User memuat entry Auto-Revert Total Control, Field "Access Level", Old "Total Control", New "—"

## Notes

- Memvalidasi alur skenario "Immutability Snapshot Nama User Pasca-Rename, Segregasi Changelog User vs User > Role, dan Update Modified By".
- Aturan PRD terkait: foundation/functions/changelog-entry.md; global-settings/role/PRD/role.md §4.1.6 User Name snapshot; global-settings/role/PRD/role.md §8.7; global-settings/user/PRD/user.md §8.2; global-settings/role/PRD/role.md §4.1.1 Modified By; global-settings/role/PRD/role.md §4.1.1 Last Updated.
- Sumber pemetaan test case granular: TC-GS-ROLE-220, TC-GS-ROLE-223, TC-GS-ROLE-224, TC-GS-ROLE-225, TC-GS-ROLE-290.

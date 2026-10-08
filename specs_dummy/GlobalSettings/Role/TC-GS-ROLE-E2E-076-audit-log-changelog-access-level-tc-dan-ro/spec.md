---
id: TC-GS-ROLE-E2E-076-audit-log-changelog-access-level-tc-dan-ro
title: "Pencatatan Audit Trail Changelog: Assign Baru, Upgrade, Remove, dan Auto-Revert Access Level TC/RO"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-207
  - TC-GS-ROLE-208
  - TC-GS-ROLE-209
  - TC-GS-ROLE-210
  - TC-GS-ROLE-211
coverage:
  web: automated
---

# Pencatatan Audit Trail Changelog: Assign Baru, Upgrade, Remove, dan Auto-Revert Access Level TC/RO

## Prerequisites

- Login sebagai Total Control
- Data Uji: Riwayat mutasi Sari Wulandari, Siti Nurhaliza, Maya Anggraini
- Setup Hook: beforeEach: openChangelogModal()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Sari Wulandari baru di-assign Total Control oleh Ahmad Fauzi

## Test Steps

### Changelog Total Control — entry Assign user baru (TC-GS-ROLE-207)

1. Tab Total Control > Changelog
2. Cari entry Sari Wulandari
3. Verifikasi Tepat 1 entry: Action "Assign", User Name "Sari Wulandari", Field "Access Level", Old Value "—", New Value "Total Control", Modified By "Ahmad F"
4. Verifikasi Tidak ada entry Sari Wulandari di Changelog Tab System

### Changelog Total Control — entry Assign upgrade dari Read Only (TC-GS-ROLE-208)

5. Tab Total Control > Changelog
6. Cari entry Siti Nurhaliza
7. Buka Tab Read Only > Changelog, cari entry Siti Nurhaliza
8. Verifikasi Changelog Tab Total Control: tepat 1 entry Action "Assign", User Name "Siti Nurhaliza", Field "Access Level", Old Value "Read Only", New Value "Total Control", Modified By "Ahmad F"
9. Verifikasi Changelog Tab Read Only: tidak ada entry baru untuk Siti Nurhaliza akibat upgrade (tidak ada entry Remove atau Auto-Revert Read Only)

### Changelog Total Control — entry Remove (TC-GS-ROLE-209)

10. Tab Total Control > Changelog
11. Cari entry Remove Sari Wulandari
12. Verifikasi Tepat 1 entry: Action "Remove", Field "Access Level", Old Value "Total Control", New Value "—", Modified By "Ahmad F"
13. Verifikasi Changelog Tab System dan Detail tidak memuat entry Remove per-role untuk Sari Wulandari

### Changelog Total Control — entry Auto-Revert Total Control (TC-GS-ROLE-210)

14. Tab Total Control > Changelog
15. Cari entry Maya Anggraini
16. Verifikasi Entry Action "Auto-Revert Total Control", Field "Access Level", Old Value "Total Control", New Value "—", Modified By "Ahmad F" (bukan "System")
17. Verifikasi Entry Edit pemicunya tercatat terpisah di Changelog "Manage TAG" (Field Update, Active → Inactive)

### Changelog Read Only — entry Assign, Remove, Auto-Revert Read Only (TC-GS-ROLE-211)

18. Tab Read Only > Changelog
19. Cari entry Rahmat Hidayat dan Wawan Setiawan
20. Verifikasi Rahmat Hidayat: Action "Assign", Field "Access Level", Old "—", New "Read Only"
21. Verifikasi Rahmat Hidayat: Action "Remove", Old "Read Only", New "—"
22. Verifikasi Wawan Setiawan: Action "Auto-Revert Read Only", Old "Read Only", New "—", Modified By "Ahmad F"

## Notes

- Memvalidasi alur skenario "Pencatatan Audit Trail Changelog: Assign Baru, Upgrade, Remove, dan Auto-Revert Access Level TC/RO".
- Aturan PRD terkait: global-settings/role/PRD/role.md §8.1; global-settings/role/PRD/role.md §8.7; global-settings/role/PRD/role.md §8.2; global-settings/role/PRD/role.md §9.2 [F-ROLE-06].
- Sumber pemetaan test case granular: TC-GS-ROLE-207, TC-GS-ROLE-208, TC-GS-ROLE-209, TC-GS-ROLE-210, TC-GS-ROLE-211.

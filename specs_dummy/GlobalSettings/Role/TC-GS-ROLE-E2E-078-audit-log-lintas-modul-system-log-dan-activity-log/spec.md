---
id: TC-GS-ROLE-E2E-078-audit-log-lintas-modul-system-log-dan-activity-log
title: "Pencatatan Log Aktor ke System Log & Activity Log untuk Mutasi Access Level dan System Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-221
  - TC-GS-ROLE-222
  - TC-GS-ROLE-289
coverage:
  web: automated
---

# Pencatatan Log Aktor ke System Log & Activity Log untuk Mutasi Access Level dan System Role

## Prerequisites

- Login sebagai Total Control
- Data Uji: Log surface GS Activity Log dan User Detail System Log
- Setup Hook: beforeEach: navigateTo(Activity Log / User Detail)
- Login sbg Role: Total Control (Ahmad Fauzi)

## Test Steps

### System Log aktor dan Activity Log untuk Assign/Remove/Auto-Revert access level (TC-GS-ROLE-221)

1. Buka Global Settings > User > Ahmad Fauzi > Tab System Log
2. Buka Global Settings > Activity Log
3. Verifikasi System Log Ahmad Fauzi: Assign, Object "Total Control", Name "Sari Wulandari", Field "Access Level", Old "—", New "Total Control"
4. Verifikasi Remove, Object "Total Control", Name "Sari Wulandari", Old "Total Control", New "—"
5. Verifikasi Auto-Revert Total Control, Object "Total Control", Name "Maya Anggraini", Old "Total Control", New "—"
6. Verifikasi Activity Log: tiga baris yang sama + Modified By "Ahmad F"

### System Log aktor dan Activity Log untuk Edit/Assign/Remove baris role (TC-GS-ROLE-222)

7. Tab System Log Ahmad Fauzi
8. Activity Log
9. Verifikasi Edit, Object "System Role", Name "Doni Pratama", Field "Role — Manage TAG — Update", Old "Inactive", New "Active"
10. Verifikasi Assign, Object "System Role", Name "Wawan Setiawan", Field "Role — Manage TAG — Access", Old "—", New "Assigned"
11. Verifikasi Remove, Object "System Role", Name "Doni Pratama", Field "Role — Manage TAG — Access", Old "Assigned", New "—"
12. Verifikasi Activity Log: baris yang sama + Modified By "Ahmad F"

### System Log aktor dan Activity Log untuk Assign/Remove/Auto-Revert Read Only (TC-GS-ROLE-289)

13. Buka Global Settings > User > Ahmad Fauzi > Tab System Log
14. Buka Global Settings > Activity Log
15. Verifikasi System Log: Assign, Object "Read Only", Name "Rahmat Hidayat", Field "Access Level", Old "—", New "Read Only"
16. Verifikasi Remove, Object "Read Only", Name "Rahmat Hidayat", Field "Access Level", Old "Read Only", New "—"
17. Verifikasi Auto-Revert Read Only, Object "Read Only", Name "Wawan Setiawan", Field "Access Level", Old "Read Only", New "—"
18. Verifikasi Activity Log: tiga baris yang sama + Modified By "Ahmad F"

## Notes

- Memvalidasi alur skenario "Pencatatan Log Aktor ke System Log & Activity Log untuk Mutasi Access Level dan System Role".
- Aturan PRD terkait: global-settings/role/PRD/role.md §8.5; global-settings/role/PRD/role.md §8.6.
- Sumber pemetaan test case granular: TC-GS-ROLE-221, TC-GS-ROLE-222, TC-GS-ROLE-289.

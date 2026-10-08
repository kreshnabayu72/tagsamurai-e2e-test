---
id: TC-GS-ROLE-E2E-055-bulk-remove-auto-revert-single-tier-dan-campuran
title: "Pencabutan Massal User Campuran: Dialog D-06 Auto-Revert Single Tier, Campuran TC+RO, dan Eksekusi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-129
  - TC-GS-ROLE-130
  - TC-GS-ROLE-131
coverage:
  web: automated
---

# Pencabutan Massal User Campuran: Dialog D-06 Auto-Revert Single Tier, Campuran TC+RO, dan Eksekusi

## Prerequisites

- Login sebagai Total Control
- Data Uji: Wawan Setiawan, Siti Nurhaliza (TC), Rina Putri (RO)
- Setup Hook: beforeEach: navigateTo(Detail)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage master reference"
- Wawan Setiawan (tanpa access level) dan Rina Putri (Read Only) punya baris (Rina Putri di-assign ulang Read Only bila sudah kehilangan RO di TC-GS-ROLE-115, Tabel Data Uji Dinamis #14)
- Siti Nurhaliza (Total Control) dan Rina Putri (Read Only) punya baris (Rina Putri di-assign ulang Read Only bila sudah kehilangan RO di TC-GS-ROLE-115, Tabel Data Uji Dinamis #14)

## Test Steps

### Screening dialog Bulk Remove dengan satu baris Read Only (TC-GS-ROLE-129)

1. Centang Wawan Setiawan dan Rina Putri
2. Klik Bulk Action > Remove
3. Screening dialog
4. Verifikasi Title "Remove Access"
5. Verifikasi Body "• Wawan Setiawan", "• Rina Putri (Read Only)", "Rina Putri will lose their Read Only access as a result." (template "[User Name] will lose their Total Control/Read Only access as a result."), "This action cannot be undone. Are you sure you want to remove them?"
6. Verifikasi Tombol `[Cancel]` | `[Remove]` (danger)

### Screening dialog Bulk Remove dengan baris Total Control dan Read Only (TC-GS-ROLE-130)

7. Centang Siti Nurhaliza dan Rina Putri
8. Klik Bulk Action > Remove
9. Verifikasi Body "• Siti Nurhaliza (Total Control)", "• Rina Putri (Read Only)", "The users marked above will lose their Total Control/Read Only access as a result.", "This action cannot be undone. Are you sure you want to remove them?"
10. Verifikasi Tombol `[Cancel]` | `[Remove]` (danger)

### Bulk Remove campuran regular dan Total Control/Read Only (TC-GS-ROLE-131)

11. Centang Wawan Setiawan, Siti Nurhaliza (TC), Rina Putri (RO)
12. Klik Bulk Action > Remove > [Remove]
13. Buka Tab Total Control dan Tab Read Only
14. Buka Detail "Manage TAG"
15. Verifikasi Toast sukses: "Success, user has been removed."
16. Verifikasi Ketiga baris hilang dari Detail "Manage master reference"
17. Verifikasi Siti Nurhaliza hilang dari Tab Total Control; Rina Putri hilang dari Tab Read Only
18. Verifikasi Baris Manage TAG milik Siti Nurhaliza dan Rina Putri tetap ada

## Notes

- Memvalidasi alur skenario "Pencabutan Massal User Campuran: Dialog D-06 Auto-Revert Single Tier, Campuran TC+RO, dan Eksekusi".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.4 D-06; global-settings/role/PRD/role.md §4.4 Render teks; global-settings/role/PRD/role.md §9.2 [F-ROLE-07] Selection campuran; global-settings/role/PRD/role.md §9.4.2 Bulk D9 campuran; global-settings/role/PRD/role.md §7.1 Delta.
- Sumber pemetaan test case granular: TC-GS-ROLE-129, TC-GS-ROLE-130, TC-GS-ROLE-131.

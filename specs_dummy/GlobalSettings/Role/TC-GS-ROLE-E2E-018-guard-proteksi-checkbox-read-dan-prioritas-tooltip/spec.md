---
id: TC-GS-ROLE-E2E-018-guard-proteksi-checkbox-read-dan-prioritas-tooltip
title: "Guard Proteksi Checkbox Read Selalu Checked & Disabled, Serta Prioritas Tooltip Elemen Non-Aktif"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-43
  - TC-GS-ROLE-44
  - TC-GS-ROLE-46
coverage:
  web: automated
---

# Guard Proteksi Checkbox Read Selalu Checked & Disabled, Serta Prioritas Tooltip Elemen Non-Aktif

## Prerequisites

- Login sebagai Total Control dan Manage user and role (Update)
- Data Uji: Pre-setup #1, #5, #10
- Setup Hook: beforeEach: navigateTo(Detail)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Login sbg Role: Read Only (Siti Nurhaliza)
- Login sbg Role: Manage user and role C/R/U/D (Hendra Wijaya)

## Test Steps

### Checkbox Read selalu checked dan terkunci untuk semua aktor (TC-GS-ROLE-43)

1. Buka Detail "Manage TAG"
2. Klik checkbox Read baris Doni Pratama
3. Hover checkbox Read
4. Ulangi langkah 1–3 login sbg Hendra Wijaya
5. Verifikasi Klik tidak mengubah state; Read tetap checked; tidak ada toast dan tidak ada request
6. Verifikasi Tooltip "Read access is required and can only be removed by removing the role." untuk Ahmad Fauzi dan Hendra Wijaya

### Prioritas tooltip CRUD — aktor Read Only pada baris Default User (TC-GS-ROLE-44)

7. Buka Detail "Manage TAG"
8. Hover checkbox Update baris Budi Santoso
9. Verifikasi Tooltip "Read Only access cannot modify data." (bukan "Default User cannot be modified.")

### Prioritas tooltip — aktor Manage user and role Update pada Default User (target TC) (TC-GS-ROLE-46)

10. Buka Detail "Manage TAG"
11. Hover checkbox Update dan Remove baris Budi Santoso
12. Verifikasi Tooltip "Default User cannot be modified." (bukan "You don't have permission to edit.")

## Notes

- Memvalidasi alur skenario "Guard Proteksi Checkbox Read Selalu Checked & Disabled, Serta Prioritas Tooltip Elemen Non-Aktif".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.3; global-settings/role/PRD/role.md ROLE-LOGIC-05a; global-settings/role/PRD/role.md §4.3 Prioritas tooltip.
- Sumber pemetaan test case granular: TC-GS-ROLE-43, TC-GS-ROLE-44, TC-GS-ROLE-46.

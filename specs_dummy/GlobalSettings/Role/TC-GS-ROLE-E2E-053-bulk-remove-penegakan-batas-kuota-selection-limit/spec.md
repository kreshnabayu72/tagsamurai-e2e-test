---
id: TC-GS-ROLE-E2E-053-bulk-remove-penegakan-batas-kuota-selection-limit
title: "Penegakan Batas Kuota Selection Limit 100 Baris: Penonaktifan Baris ke-101 dan Capping Parsial Select All"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-124
  - TC-GS-ROLE-125
coverage:
  web: automated
---

# Penegakan Batas Kuota Selection Limit 100 Baris: Penonaktifan Baris ke-101 dan Capping Parsial Select All

## Prerequisites

- Login sebagai Total Control; Detail dengan ≥101 record eligible (Pre-setup #17); Selection Limit = 100
- Data Uji: Pre-setup #17 (Volume data ≥101 baris)
- Setup Hook: before: seedLargeUsers(101)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Selection Limit diturunkan ke 100 (nilai minimum; Admin Console > Plans & Licensing > Lifecycle Settings > System Limits)
- Detail "Manage hardware" berisi ≥101 baris eligible (Pre-setup #17)
- Selection Limit diturunkan ke 100 (nilai minimum)
- Detail "Manage hardware" berisi tepat 101 baris eligible (Pre-setup #17)

## Test Steps

### Selection Limit — centang manual melewati batas (TC-GS-ROLE-124)

1. Centang 100 baris
2. Hover checkbox baris ke-101
3. Verifikasi Checkbox baris ke-101 dan seterusnya tetap tampil namun disabled
4. Verifikasi Tooltip "You've reached the maximum selection of 100 rows."
5. Verifikasi 100 baris tetap tercentang, Bulk Action Bar tetap aktif

### Selection Limit — Select All di-cap otomatis (TC-GS-ROLE-125)

6. Klik button Select All
7. Verifikasi 100 baris pertama terselect
8. Verifikasi Toast error persist sampai di-dismiss: "Error, only the first 100 of 101 rows were selected. Narrow your filter to include the rest."
9. Verifikasi Bulk Action Bar tetap dapat dipakai

## Notes

- Memvalidasi alur skenario "Penegakan Batas Kuota Selection Limit 100 Baris: Penonaktifan Baris ke-101 dan Capping Parsial Select All".
- Aturan PRD terkait: global-settings/role/PRD/role.md §5 Bulk; foundation/process/prd-process/prd-conventions.md §8 Selection Limit.
- Sumber pemetaan test case granular: TC-GS-ROLE-124, TC-GS-ROLE-125.

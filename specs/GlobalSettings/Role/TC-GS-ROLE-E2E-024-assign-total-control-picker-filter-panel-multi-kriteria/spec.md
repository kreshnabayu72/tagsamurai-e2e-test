---
id: TC-GS-ROLE-E2E-024-assign-total-control-picker-filter-panel-multi-kriteria
title: "Penyaringan Filter Panel Modal Picker Assign Total Control: Position, Division, Status, Activation Status, Temporary, dan Custom Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-73
  - TC-GS-ROLE-74
coverage:
  web: automated
---

# Penyaringan Filter Panel Modal Picker Assign Total Control: Position, Division, Status, Activation Status, Temporary, dan Custom Field

## Prerequisites

- Login sebagai Total Control
- Data Uji: Pre-setup #11 (Kandidat dengan atribut lengkap)
- Setup Hook: beforeEach: openModalAssignTC()
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > Total Control

## Test Steps

### Filter Popup Assign berdasarkan Position, Division, dan Status (TC-GS-ROLE-73)

1. Klik [+ Assign]
2. Klik Filter, screening field
3. Pilih Position "Staff" > Apply
4. Reset; pilih Division "Logistics" > Apply
5. Reset; pilih Status "Inactive" > Apply
6. Verifikasi Field Position ("All positions"), Division ("All divisions"), Status ("All statuses") bertipe multi-select searchable
7. Verifikasi Position Staff: hanya Maya Anggraini dan user ber-Position Staff
8. Verifikasi Division Logistics: hanya Ahmad Fauzan (Warehouse Staff)
9. Verifikasi Status Inactive: hanya Maya Anggraini dan user Inactive lain di pool

### Filter Popup Assign berdasarkan Activation Status, Temporary User, Temporary Until, Custom Field (TC-GS-ROLE-74)

10. Klik [+ Assign]
11. Klik Filter
12. Verifikasi Activation Status ("All statuses", multi-select searchable): pilih Pending Activation, hanya Rudi Hartono
13. Verifikasi Temporary User ("All options"): pilih Yes, hanya user temporary
14. Verifikasi Temporary Until ("Select date", date range picker): hanya user dengan tanggal di rentang
15. Verifikasi [Custom Field aktif] Region: pilih Bandung, hanya user Region Bandung

## Notes

- Memvalidasi alur skenario "Penyaringan Filter Panel Modal Picker Assign Total Control: Position, Division, Status, Activation Status, Temporary, dan Custom Field".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.1.5; global-settings/role/PRD/role.md §4.2 Filter Panel.
- Sumber pemetaan test case granular: TC-GS-ROLE-73, TC-GS-ROLE-74.

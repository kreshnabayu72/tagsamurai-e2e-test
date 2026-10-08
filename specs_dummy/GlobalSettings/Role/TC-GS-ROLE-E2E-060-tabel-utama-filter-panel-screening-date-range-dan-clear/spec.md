---
id: TC-GS-ROLE-E2E-060-tabel-utama-filter-panel-screening-date-range-dan-clear
title: "Filter Panel Tabel Utama Tab TC & RO: Screening Multi-Select, Date Range Last Updated & Temporary Until, dan Reset Clear Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-142
  - TC-GS-ROLE-143
  - TC-GS-ROLE-144
  - TC-GS-ROLE-145
  - TC-GS-ROLE-146
coverage:
  web: automated
---

# Filter Panel Tabel Utama Tab TC & RO: Screening Multi-Select, Date Range Last Updated & Temporary Until, dan Reset Clear Field

## Prerequisites

- Login sebagai Total Control
- Data Uji: Pre-setup #1 s/d #4
- Setup Hook: beforeEach: navigateTo(Tab Total Control)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup tersedia; Tab Total Control dan Tab Read Only masing-masing berisi ≥3 user dengan Position/Division berbeda
- Custom Field aktif "Region" (Dropdown) diisi pada user Total Control
- User berada di Global Settings > Role & Permission > Total Control

## Test Steps

### Screening Filter Panel Tab Total Control dan Tab Read Only (TC-GS-ROLE-142)

1. Tab Total Control: klik Filter
2. Screening field
3. Ulangi di Tab Read Only
4. Verifikasi Field (label → placeholder → tipe): Position → "All positions" → multi-select searchable; Division → "All divisions" → multi-select searchable; Status → "All statuses" → multi-select searchable; Activation Status → "All statuses" → multi-select searchable; Temporary User → "All options" → multi-select searchable; Temporary Until → "Select date" → date range picker; [Custom Field aktif Dropdown/Date] → "All [plural noun]" → sesuai tipe; Modified By → "All users" → multi-select searchable; Last Updated → "Select date" → date range picker
5. Verifikasi Tab Read Only: field identik

### Opsi dropdown filter Tab Total Control diisi dari data tab itu (TC-GS-ROLE-143)

6. Tab Total Control: buka dropdown Position, Division, Status, Modified By
7. Bandingkan dengan nilai yang tampil di baris Tab Total Control
8. Verifikasi Position: hanya Position user Total Control yang ada
9. Verifikasi Division: hanya Division user Total Control
10. Verifikasi Status: Active, Inactive sesuai baris
11. Verifikasi Modified By: hanya nama Modified By di tab itu
12. Verifikasi Position user yang hanya ada di Tab Read Only tidak muncul

### Filter multi-select per field Tab Total Control dan Tab Read Only (TC-GS-ROLE-144)

13. Tab Total Control: untuk tiap field pada Data Uji pilih 1 opsi → Apply → catat → Clear
14. Tab Read Only: Filter Position "HR Manager" → Apply → Clear; Status "Active" → Apply → Clear; Modified By "Ahmad F" → Apply
15. Verifikasi Position: hanya baris IT Manager
16. Verifikasi Division: hanya Finance
17. Verifikasi Status: Inactive hanya Dewi Lestari (Default User tidak ikut karena Status-nya Active); Active menampilkan Ahmad Fauzi dan Budi Santoso (Default User)
18. Verifikasi Activation Status: hanya Pending Activation
19. Verifikasi Temporary User: hanya Yes
20. Verifikasi Modified By: hanya baris Modified By Budi S
21. Verifikasi Tab Read Only: Position HR Manager → hanya Rina Putri; Status Active → hanya Siti Nurhaliza; Modified By Ahmad F → hanya Siti Nurhaliza

### Filter date range Last Updated dan Temporary Until (TC-GS-ROLE-145)

22. Filter Last Updated rentang tanggal assign Dewi Lestari → Apply
23. Clear; filter Temporary Until rentang yang memuat Temporary Until satu user → Apply
24. Tab Read Only: filter Last Updated rentang tanggal assign Rina Putri → Apply
25. Verifikasi Last Updated: hanya baris dengan Last Updated di rentang; Default User (—) tidak ikut
26. Verifikasi Temporary Until: hanya baris Temporary User dengan tanggal di rentang
27. Verifikasi Tab Read Only: hanya baris Read Only dengan Last Updated di rentang (Rina Putri)

### Search, Filter, dan Sort Custom Field aktif bertipe Dropdown (TC-GS-ROLE-146)

28. Tampilkan kolom Region
29. Filter Region = "Jakarta" → Apply
30. Clear Filter; Search "jakarta" + Enter
31. Kosongkan Search; klik header Region 3 kali
32. Verifikasi Field filter label "Region" dengan placeholder "All regions"
33. Verifikasi Filter: hanya baris Region Jakarta
34. Verifikasi Search: baris Region Jakarta cocok (case-insensitive)
35. Verifikasi Sort: klik 1 A-Z by badge label, klik 2 Z-A, klik 3 default Name A-Z

## Notes

- Memvalidasi alur skenario "Filter Panel Tabel Utama Tab TC & RO: Screening Multi-Select, Date Range Last Updated & Temporary Until, dan Reset Clear Field".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.1.1; global-settings/role/PRD/role.md §4.1.2; global-settings/role/PRD/role.md §5; global-settings/role/PRD/role.md §9.5 Sumber opsi filter; foundation/process/prd-process/prd-conventions.md §9.8; global-settings/role/PRD/role.md §4.1.1 [Custom Field aktif].
- Sumber pemetaan test case granular: TC-GS-ROLE-142, TC-GS-ROLE-143, TC-GS-ROLE-144, TC-GS-ROLE-145, TC-GS-ROLE-146.

---
id: TC-GS-ROLE-E2E-023-assign-total-control-picker-search-dan-scoping-kolom-tersembunyi
title: "Pencarian Modal Picker Assign Total Control: Empty States, Substring Name/Email/Position/Division, dan Scoping Kolom Hidden"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-68
  - TC-GS-ROLE-69
  - TC-GS-ROLE-70
  - TC-GS-ROLE-71
  - TC-GS-ROLE-72
coverage:
  web: automated
---

# Pencarian Modal Picker Assign Total Control: Empty States, Substring Name/Email/Position/Division, dan Scoping Kolom Hidden

## Prerequisites

- Login sebagai Total Control
- Data Uji: Pre-setup #11 (Ahmad Fauzan dkk.), Pre-setup #14 (Client tanpa eligible)
- Setup Hook: beforeEach: openModalAssignTC()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Client uji B (Pre-setup #14): semua user ber-Access Global Settings sudah Total Control
- User berada di Global Settings > Role & Permission > Total Control

## Test Steps

### Empty state Popup Assign saat semua user eligible sudah di-assign (TC-GS-ROLE-68)

1. Tab Total Control > klik [+ Assign]
2. Verifikasi Illustration + Title "All eligible users have been assigned" + Description "There are no additional eligible users available to select."

### No-result Search pada Popup Assign (TC-GS-ROLE-69)

3. Klik [+ Assign]
4. Search "zzqx" + Enter
5. Verifikasi Illustration + Title "No results found" + Description "Try adjusting your search or filter."

### Search Popup Assign berdasarkan Name dan Email (TC-GS-ROLE-70)

6. Klik [+ Assign]
7. Search "wula" + Enter
8. Search "AHMAD.FZ" + Enter
9. Verifikasi Name: hanya Sari Wulandari tampil (substring)
10. Verifikasi Email: hanya Ahmad Fauzan (ahmad.fz@client.com) tampil (case-insensitive)

### Search Popup Assign berdasarkan Position dan Division serta kolom yang tidak dicari (TC-GS-ROLE-71)

11. Klik [+ Assign]
12. Search "Warehouse" + Enter
13. Search "logis" + Enter
14. Search "TG-00877" + Enter
15. Search "Bandung" + Enter
16. Search "Pending" + Enter, lalu "Yes" + Enter
17. Verifikasi Position "Warehouse": Ahmad Fauzan (Warehouse Staff) cocok
18. Verifikasi Division "logis": Ahmad Fauzan (Logistics) cocok
19. Verifikasi TAG "TG-00877": tidak cocok (kolom TAG Hidden di picker)
20. Verifikasi [Custom Field aktif] Region "Bandung": tidak cocok (kolom Hidden di picker)
21. Verifikasi Activation Status dan Temporary User: keyword "Pending" dan "Yes" tidak mencocokkan (kolom Hidden di picker)

### Search Popup Assign tidak mencocokkan kolom Status (TC-GS-ROLE-72)

22. Klik [+ Assign]
23. Search "Inactive" + Enter
24. Verifikasi Maya Anggraini (Status Inactive, nama/email tanpa kata "Inactive") tidak tampil
25. Verifikasi Tampil "No results found"

## Notes

- Memvalidasi alur skenario "Pencarian Modal Picker Assign Total Control: Empty States, Substring Name/Email/Position/Division, dan Scoping Kolom Hidden".
- Aturan PRD terkait: global-settings/role/PRD/role.md §7.1 S-10; global-settings/role/PRD/role.md §4.1.5; global-settings/role/PRD/role.md §4.2 Toolbar; global-settings/role/PRD/role.md §4.1.5 Status; foundation/process/prd-process/prd-conventions.md §37.2.
- Sumber pemetaan test case granular: TC-GS-ROLE-68, TC-GS-ROLE-69, TC-GS-ROLE-70, TC-GS-ROLE-71, TC-GS-ROLE-72.

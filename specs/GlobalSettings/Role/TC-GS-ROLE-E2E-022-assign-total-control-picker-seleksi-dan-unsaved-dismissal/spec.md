---
id: TC-GS-ROLE-E2E-022-assign-total-control-picker-seleksi-dan-unsaved-dismissal
title: "Interaksi Modal Picker Assign Total Control: Seleksi Multi-User, Validasi Kosong, Focus Trap, dan Dialog D-01"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-55
  - TC-GS-ROLE-56
  - TC-GS-ROLE-57
  - TC-GS-ROLE-61
  - TC-GS-ROLE-62
  - TC-GS-ROLE-77
coverage:
  web: automated
---

# Interaksi Modal Picker Assign Total Control: Seleksi Multi-User, Validasi Kosong, Focus Trap, dan Dialog D-01

## Prerequisites

- Login sebagai Total Control
- Data Uji: Pre-setup #11 (Kandidat picker)
- Setup Hook: beforeEach: openModalAssignTC()
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > Total Control
- Doni Pratama: Manage TAG (R), Import data (C,R), Manage files (R,D), Manage user and role (R); tanpa baris Manage hardware dan Manage master reference
- Sari Wulandari login di sesi B
- Login sbg Role: Total Control (Ahmad Fauzi) di sesi A

## Test Steps

### Selection counter Popup Assign Total Control (TC-GS-ROLE-55)

1. Klik [+ Assign]
2. Centang Sari Wulandari
3. Centang Maya Anggraini
4. Uncheck Maya Anggraini
5. Verifikasi Langkah 2: "1 user selected"
6. Verifikasi Langkah 3: "2 users selected"
7. Verifikasi Langkah 4: "1 user selected"

### Checkbox header Popup Assign memilih semua baris halaman aktif (TC-GS-ROLE-56)

8. Klik [+ Assign]
9. Centang checkbox header
10. Uncheck satu baris
11. Uncheck checkbox header
12. Verifikasi Langkah 2: semua baris halaman aktif checked, counter = jumlah baris halaman
13. Verifikasi Langkah 3: checkbox header tidak lagi checked penuh
14. Verifikasi Langkah 4: semua baris unchecked

### Cancel Popup Assign Total Control (TC-GS-ROLE-57)

15. Klik [+ Assign]
16. Centang Sari Wulandari
17. Klik [Cancel]
18. Verifikasi Popup tertutup tanpa dialog
19. Verifikasi Sari Wulandari tidak muncul di Tab Total Control
20. Verifikasi Tidak ada toast

### Assign Total Control menimpa baris role parsial yang sudah ada (TC-GS-ROLE-61)

21. Tab Total Control > [+ Assign] > centang Doni Pratama > [Assign]
22. Buka Detail keenam role dan amati baris Doni Pratama
23. Verifikasi Toast sukses: "Success, Total Control has been assigned."
24. Verifikasi Manage TAG: R,U checked
25. Verifikasi Import data: C,R checked
26. Verifikasi Manage files: R,D checked
27. Verifikasi Manage user and role: C,R,U,D checked
28. Verifikasi Manage hardware dan Manage master reference: baris baru C,R,U,D checked
29. Verifikasi Tiap role hanya punya 1 baris Doni Pratama

### Assign Total Control tidak memicu notifikasi ke target (TC-GS-ROLE-62)

30. Sesi A: Tab Total Control > [+ Assign] > centang Sari Wulandari > [Assign]
31. Sesi B: buka Overlay Notifikasi
32. Verifikasi Overlay Notifikasi Sari Wulandari tidak memuat notifikasi terkait Total Control
33. Verifikasi Toast sukses di sesi A: "Success, Total Control has been assigned."

### Accessibility Popup Assign — focus trapped dan Esc menutup (TC-GS-ROLE-77)

34. Klik [+ Assign]
35. Tekan Tab berulang
36. Tekan Esc
37. Verifikasi Fokus berputar di dalam popup
38. Verifikasi Esc menutup popup tanpa assign

## Notes

- Memvalidasi alur skenario "Interaksi Modal Picker Assign Total Control: Seleksi Multi-User, Validasi Kosong, Focus Trap, dan Dialog D-01".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Selection Counter; global-settings/role/PRD/role.md §4.2 Popup: Table User Picker; global-settings/role/PRD/role.md §4.1.5; foundation/process/prd-process/prd-conventions.md §37; global-settings/role/PRD/role.md §9.2 [F-ROLE-04] Upsert; global-settings/role/PRD/role.md §9.4.3 Must NOT; global-settings/role/PRD/role.md §8.8; global-settings/role/PRD/role.md §4.5.
- Sumber pemetaan test case granular: TC-GS-ROLE-55, TC-GS-ROLE-56, TC-GS-ROLE-57, TC-GS-ROLE-61, TC-GS-ROLE-62, TC-GS-ROLE-77.

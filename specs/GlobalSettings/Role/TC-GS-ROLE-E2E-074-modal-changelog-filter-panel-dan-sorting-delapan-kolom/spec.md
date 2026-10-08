---
id: TC-GS-ROLE-E2E-074-modal-changelog-filter-panel-dan-sorting-delapan-kolom
title: "Modal Changelog: Filter Panel Multi-Kriteria, Dropdown Dinamis per Role, dan Pengurutan 3-State pada 8 Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-200
  - TC-GS-ROLE-201
  - TC-GS-ROLE-202
coverage:
  web: automated
---

# Modal Changelog: Filter Panel Multi-Kriteria, Dropdown Dinamis per Role, dan Pengurutan 3-State pada 8 Kolom

## Prerequisites

- Login sebagai Total Control
- Data Uji: Dataset Changelog dengan variasi entri
- Setup Hook: beforeEach: openChangelogModal()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Changelog Tab Total Control berisi Assign, Remove, Auto-Revert Total Control
- Changelog Tab System berisi Edit, Assign, Remove
- Changelog Tab System berisi ≥3 entry

## Test Steps

### Filter Modal Changelog Tab Total Control/Read Only (TC-GS-ROLE-200)

1. Klik Filter: screening field
2. Filter Action "Remove" → Apply → Clear
3. Filter User Name tertentu → Apply → Clear
4. Filter Modified By → Apply → Clear
5. Filter Date rentang → Apply
6. Verifikasi Field: Date "Select date" (date range), Action "All actions", User Name "All users", Modified By "All users" (multi-select searchable); tidak ada filter Field
7. Verifikasi Opsi Action hanya nilai yang ada di log (Assign, Remove, Auto-Revert Total Control)
8. Verifikasi Tiap filter hanya menampilkan entry yang cocok

### Filter Modal Changelog Tab System dan Detail (TC-GS-ROLE-201)

9. Changelog Tab System: Filter, screening field
10. Filter Role — User, Field "Update", Action "Edit" (satu per satu, Apply, Clear)
11. Detail "Manage TAG" Changelog: buka dropdown Field
12. Verifikasi Field: Date, Action "All actions", Role — User "All roles — users", Field "All fields", Modified By "All users"
13. Verifikasi Opsi Action hanya Edit/Assign/Remove
14. Verifikasi Tiap filter hanya entry cocok
15. Verifikasi Detail Manage TAG: opsi Field populate dari data log role tsb (nilai Field unik yang tercatat, mis. Update dan Access pada data uji); tidak ada opsi untuk kolom yang tidak pernah tercatat

### Sort Modal Changelog (TC-GS-ROLE-202)

16. Klik header Date 3 kali
17. Klik header Action 3 kali
18. Klik header Old Value 3 kali
19. Klik header Role — User, Field, New Value, Modified By masing-masing 3 kali
20. Buka Changelog Tab Total Control, klik header User Name 3 kali
21. Verifikasi Date: Oldest First / Newest First / default Newest First
22. Verifikasi Action: A-Z / Z-A / default
23. Verifikasi Old Value: kolom campuran; kosong (—, Assign) selalu di akhir untuk kedua arah
24. Verifikasi Role — User: A-Z / Z-A / default
25. Verifikasi Field: A-Z / Z-A / default
26. Verifikasi New Value: kolom campuran; kosong (—, Remove) selalu di akhir untuk kedua arah
27. Verifikasi Modified By: A-Z / Z-A / default
28. Verifikasi User Name (Changelog Tab Total Control): A-Z / Z-A / default

## Notes

- Memvalidasi alur skenario "Modal Changelog: Filter Panel Multi-Kriteria, Dropdown Dinamis per Role, dan Pengurutan 3-State pada 8 Kolom".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Modal: Changelog; global-settings/role/PRD/role.md §4.1.6; foundation/process/prd-process/prd-conventions.md §9.10.
- Sumber pemetaan test case granular: TC-GS-ROLE-200, TC-GS-ROLE-201, TC-GS-ROLE-202.

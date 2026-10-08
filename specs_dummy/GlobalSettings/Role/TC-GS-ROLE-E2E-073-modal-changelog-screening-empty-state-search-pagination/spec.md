---
id: TC-GS-ROLE-E2E-073-modal-changelog-screening-empty-state-search-pagination
title: "Screening Modal Changelog pada 4 Surface, Empty State, Pencarian per Kelas Kolom, dan Paginasi Halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-196
  - TC-GS-ROLE-197
  - TC-GS-ROLE-198
  - TC-GS-ROLE-199
  - TC-GS-ROLE-206
coverage:
  web: automated
---

# Screening Modal Changelog pada 4 Surface, Empty State, Pencarian per Kelas Kolom, dan Paginasi Halaman

## Prerequisites

- Login sebagai Total Control
- Data Uji: Riwayat log Changelog Tab TC, RO, System, Detail
- Setup Hook: beforeEach: openChangelogModal()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Ada entry Assign/Remove di kedua changelog
- Ada entry Edit/Assign/Remove
- Client uji B tanpa riwayat Role & Permission (Pre-setup #14)
- Changelog Tab System berisi entry Edit dan Assign
- Changelog Tab System berisi >10 entry

## Test Steps

### Screening Modal Changelog Tab Total Control dan Tab Read Only (TC-GS-ROLE-196)

1. Tab Total Control: klik Changelog
2. Screening modal
3. Ulangi di Tab Read Only
4. Verifikasi Title "Changelog: Role & Permission > Total Control"; toolbar `Search | Filter | Download`; placeholder "Search action, user, or value..."
5. Verifikasi Kolom `Date (sortable) | Action (sortable) | User Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Actions (⋯) (header = Column Visibility, tanpa row action)`
6. Verifikasi Default sort Date terbaru dulu; pagination default 10
7. Verifikasi Tab Read Only: Title "Changelog: Role & Permission > Read Only", struktur identik

### Screening Modal Changelog Tab System dan Detail (TC-GS-ROLE-197)

8. Tab System: klik Changelog
9. Screening modal
10. Detail "Manage TAG": klik Changelog
11. Verifikasi Title "Changelog: Role & Permission > System"; placeholder "Search action, role, user, or value..."
12. Verifikasi Kolom `Date | Action | Role — User | Field | Old Value | New Value | Modified By | Actions (⋯)` (semua data sortable)
13. Verifikasi Detail: Title "Changelog: Role & Permission > Manage TAG"; placeholder "Search action, user, or value..."; kolom identik
14. Verifikasi Default sort Date terbaru dulu

### Empty state dan no-result Modal Changelog (TC-GS-ROLE-198)

15. Buka Changelog Tab Read Only
16. Di client utama, buka Changelog Tab Total Control, search "zzqx" + Enter
17. Verifikasi Illustration + Title "No changelog yet" + Description "Activities and changes will appear here."
18. Verifikasi Illustration + Title "No results found" + Description "Try adjusting your search or filter."

### Search Modal Changelog per kelas kolom (TC-GS-ROLE-199)

19. Changelog Tab System: search "assign" + Enter (Action)
20. "hendra" (Role — User)
21. "Delete" (Field)
22. "inactive" (Old/New Value)
23. "ahmad" (Modified By)
24. Tanggal entry (Date)
25. Changelog Tab Total Control: search "sari" (User Name) dan "read only" (Old Value, New Value)
26. Verifikasi Action: entry Assign cocok
27. Verifikasi Role — User: entry Hendra Wijaya cocok
28. Verifikasi Field: entry Field Delete cocok
29. Verifikasi Value: entry dengan Old/New Value Inactive cocok
30. Verifikasi Modified By: entry oleh Ahmad F cocok
31. Verifikasi Date: "No results found" (tidak searchable)
32. Verifikasi User Name: entry Sari Wulandari cocok; Old Value, New Value: entry bernilai Read Only cocok

### Pagination Modal Changelog (TC-GS-ROLE-206)

33. Amati default
34. Ubah page size 25
35. Navigasi halaman
36. Verifikasi Default 10
37. Verifikasi Opsi 10/25/50/100
38. Verifikasi Navigasi berfungsi

## Notes

- Memvalidasi alur skenario "Screening Modal Changelog pada 4 Surface, Empty State, Pencarian per Kelas Kolom, dan Paginasi Halaman".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Modal: Changelog; global-settings/role/PRD/role.md §4.1.6; foundation/process/prd-process/prd-conventions.md §9.10; global-settings/role/PRD/role.md §7.1 S-05.
- Sumber pemetaan test case granular: TC-GS-ROLE-196, TC-GS-ROLE-197, TC-GS-ROLE-198, TC-GS-ROLE-199, TC-GS-ROLE-206.

---
id: TC-GS-ROLE-E2E-070-tab-system-search-guard-setup-kolom-dan-download
title: "Tabel Tab System: Pencarian Role Name, Guard Kolom Non-Sortable, Setup Kolom, dan Download Ekspor"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-181
  - TC-GS-ROLE-182
  - TC-GS-ROLE-183
  - TC-GS-ROLE-184
  - TC-GS-ROLE-185
coverage:
  web: automated
---

# Tabel Tab System: Pencarian Role Name, Guard Kolom Non-Sortable, Setup Kolom, dan Download Ekspor

## Prerequisites

- Login sebagai Total Control
- Data Uji: 6 role katalog
- Setup Hook: beforeEach: navigateTo(Tab System)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System

## Test Steps

### Search Tab System (TC-GS-ROLE-181)

1. Klik Search: amati placeholder
2. Search "master" + Enter
3. Search "6" + Enter
4. Verifikasi Placeholder "Search role..."
5. Verifikasi Hanya baris "Manage master reference"
6. Verifikasi Kolom Users tidak dapat dicari: "No results found" (tidak ada Role Name memuat "6")

### Kolom Tab System tidak dapat di-sort (TC-GS-ROLE-182)

7. Hover dan klik header Role Name
8. Hover dan klik header Users
9. Verifikasi Tidak ada ikon sort pada kedua header
10. Verifikasi Urutan baris tetap urutan fixed

### Screening overlay dan popup Setup Column Tab System (TC-GS-ROLE-183)

11. Klik header (⋯)
12. Klik [Setup Column]
13. Verifikasi Overlay: [Setup Column]; Role Name dan Users checked & enabled
14. Verifikasi Popup: Title "Setup Column", icon close (X), daftar Role Name dan Users, `[Reset to Default]` | `[Save]`

### Setup Column Tab System — hide, drag, pin, reset, discard, guard (TC-GS-ROLE-184)

15. Popup: uncheck Users > Save
16. Drag Users ke depan > Save
17. Pin Role Name > Save
18. Uncheck Role Name saat Users hidden
19. Reset to Default > Save
20. Ubah lalu (X)
21. Verifikasi Users tersembunyi lalu persist F5
22. Verifikasi Urutan Users–Role Name tersimpan
23. Verifikasi Role Name ter-pin
24. Verifikasi Checkbox Role Name disabled dengan tooltip "At least one column must remain visible."
25. Verifikasi Reset mengembalikan Role Name | Users tampil
26. Verifikasi (X) membuang perubahan

### Download Tab System sebagai CSV dan XLSX (TC-GS-ROLE-185)

27. Download > "Download as CSV"
28. Download > "Download as XLSX"
29. Verifikasi File "Role-Permission-System.csv" dan "Role-Permission-System.xlsx"
30. Verifikasi Kolom Users bertipe angka di XLSX
31. Verifikasi Enam baris sesuai urutan fixed
32. Verifikasi Tidak ada toast sukses

## Notes

- Memvalidasi alur skenario "Tabel Tab System: Pencarian Role Name, Guard Kolom Non-Sortable, Setup Kolom, dan Download Ekspor".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.1.3; global-settings/role/PRD/role.md §4.2 Tab: System; foundation/process/prd-process/prd-conventions.md §9.3; global-settings/role/PRD/role.md §4.1 Filename Download; global-settings/role/PRD/role.md §5 Download; foundation/process/prd-process/prd-conventions.md §9.9.
- Sumber pemetaan test case granular: TC-GS-ROLE-181, TC-GS-ROLE-182, TC-GS-ROLE-183, TC-GS-ROLE-184, TC-GS-ROLE-185.

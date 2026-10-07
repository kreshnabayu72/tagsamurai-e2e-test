---
id: TC-GS-DIV-E2E-009-role-matrix-granular-write-capabilities-scoping
title: "Role Matrix: Isolasi Visibilitas Hak Akses Tulis Granular (Create-Only, Update-Only, dan Delete-Only)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-20
  - TC-GS-DIV-21
  - TC-GS-DIV-22
coverage:
  web: automated
---

# Role Matrix: Isolasi Visibilitas Hak Akses Tulis Granular (Create-Only, Update-Only, dan Delete-Only)

## Prerequisites

- Login sebagai Role: System Role (Create+Read, Update+Read, Delete+Read)
- Tersedia akun System Role dengan kombinasi capability terbatas: Create+Read, Update+Read, Delete+Read
- Tabel Division terisi data

## Test Steps

### Aktor dengan capability Create dan Read (TC-GS-DIV-20)

1. Buka Global Settings > User
2. Buka Tab Division (bila tampil)
3. Perhatikan Table Tools, kolom checkbox, dan menu baris
4. Centang 1 baris (bila checkbox tampil) dan perhatikan Bulk Action Bar
5. Verifikasi Show: Tab `Division`
6. Verifikasi Show: Toolbar Search, Filter, Download, Changelog
7. Verifikasi Show: Tombol `[+ Division]`
8. Verifikasi Hidden: Row action `Edit`
9. Verifikasi Hidden: Row action `Delete`
10. Verifikasi Hidden: Checkbox baris tabel
11. Verifikasi Hidden: Bulk Action Bar `[Delete]`

### Aktor dengan capability Update dan Read (TC-GS-DIV-21)

12. Buka Global Settings > User
13. Buka Tab Division (bila tampil)
14. Perhatikan Table Tools, kolom checkbox, dan menu baris
15. Centang 1 baris (bila checkbox tampil) dan perhatikan Bulk Action Bar
16. Verifikasi Show: Tab `Division`
17. Verifikasi Show: Toolbar Search, Filter, Download, Changelog
18. Verifikasi Show: Row action `Edit` (menu baris hanya memuat Edit)
19. Verifikasi Hidden: Tombol `[+ Division]`
20. Verifikasi Hidden: Row action `Delete`
21. Verifikasi Hidden: Checkbox baris tabel
22. Verifikasi Hidden: Bulk Action Bar `[Delete]`

### Aktor dengan capability Delete dan Read (TC-GS-DIV-22)

23. Buka Global Settings > User
24. Buka Tab Division (bila tampil)
25. Perhatikan Table Tools, kolom checkbox, dan menu baris
26. Centang 1 baris (bila checkbox tampil) dan perhatikan Bulk Action Bar
27. Verifikasi Show: Tab `Division`
28. Verifikasi Show: Toolbar Search, Filter, Download, Changelog
29. Verifikasi Show: Row action `Delete` (menu baris hanya memuat Delete)
30. Verifikasi Show: Checkbox baris tabel
31. Verifikasi Show: Bulk Action Bar `[Delete]` saat >=1 baris dicentang
32. Verifikasi Hidden: Tombol `[+ Division]`
33. Verifikasi Hidden: Row action `Edit`

## Notes

- Memvalidasi pembatasan elemen UI spesifik aksi tulis: aktor Create-Only hanya melihat tombol [+ Division] tanpa Edit/Delete, aktor Update-Only hanya melihat row action Edit tanpa [+ Division]/Delete, dan aktor Delete-Only hanya melihat row action Delete, checkbox tabel, dan Bulk Action Bar (PRD §2, §4.8).
- Sumber pemetaan test case granular: TC-GS-DIV-20, TC-GS-DIV-21, TC-GS-DIV-22.

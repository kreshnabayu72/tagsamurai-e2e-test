---
id: TC-GS-DIV-E2E-008-role-matrix-baseline-access-dan-read-only-scoping
title: "Role Matrix: Akses Dasar Tanpa Hak Akses, Read-Only, Read-Only Access Level, dan Total Control Baseline"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-18
  - TC-GS-DIV-19
  - TC-GS-DIV-23
  - TC-GS-DIV-24
coverage:
  web: automated
---

# Role Matrix: Akses Dasar Tanpa Hak Akses, Read-Only, Read-Only Access Level, dan Total Control Baseline

## Prerequisites

- Login sebagai Role: Total Control, Read Only, dan System Role Tanpa Akses
- Tersedia akun untuk masing-masing role: Total Control, Read Only, System Role (Tanpa Capability, Read Saja)
- Tabel Division terisi data

## Test Steps

### Aktor tanpa capability Manage user and role tidak melihat Tab Division (TC-GS-DIV-18)

1. Buka Global Settings > User
2. Buka Tab Division (bila tampil)
3. Perhatikan Table Tools, kolom checkbox, dan menu baris
4. Centang 1 baris (bila checkbox tampil) dan perhatikan Bulk Action Bar
5. Verifikasi Hidden: Tab `Division` di halaman User
6. Verifikasi Hidden: Tombol `[+ Division]`
7. Verifikasi Hidden: Row action `Edit` dan `Delete`
8. Verifikasi Hidden: Checkbox baris tabel
9. Verifikasi Hidden: Bulk Action Bar `[Delete]`
10. Verifikasi Hidden: Toolbar Search, Filter, Download, Changelog

### Aktor dengan capability Read saja (TC-GS-DIV-19)

11. Buka Global Settings > User
12. Buka Tab Division (bila tampil)
13. Perhatikan Table Tools, kolom checkbox, dan menu baris
14. Centang 1 baris (bila checkbox tampil) dan perhatikan Bulk Action Bar
15. Verifikasi Show: Tab `Division`
16. Verifikasi Show: Toolbar Search, Filter, Download, Changelog
17. Verifikasi Hidden: Tombol `[+ Division]`
18. Verifikasi Hidden: Row action `Edit`
19. Verifikasi Hidden: Row action `Delete` (menu baris tidak tampil)
20. Verifikasi Hidden: Checkbox baris tabel
21. Verifikasi Hidden: Bulk Action Bar `[Delete]`

### Total Control melihat seluruh elemen (TC-GS-DIV-23)

22. Buka Global Settings > User
23. Buka Tab Division (bila tampil)
24. Perhatikan Table Tools, kolom checkbox, dan menu baris
25. Centang 1 baris (bila checkbox tampil) dan perhatikan Bulk Action Bar
26. Verifikasi Show: Tab `Division`
27. Verifikasi Show: Toolbar Search, Filter, Download, Changelog
28. Verifikasi Show: Tombol `[+ Division]`
29. Verifikasi Show: Row action `Edit`
30. Verifikasi Show: Row action `Delete`
31. Verifikasi Show: Checkbox baris tabel
32. Verifikasi Show: Bulk Action Bar `[Delete]` saat >=1 baris dicentang

### Read Only (Access Level) hanya dapat melihat (TC-GS-DIV-24)

33. Buka Global Settings > User
34. Buka Tab Division (bila tampil)
35. Perhatikan Table Tools, kolom checkbox, dan menu baris
36. Centang 1 baris (bila checkbox tampil) dan perhatikan Bulk Action Bar
37. Verifikasi Show: Tab `Division`
38. Verifikasi Show: Toolbar Search, Filter, Download, Changelog
39. Verifikasi Hidden: Tombol `[+ Division]`
40. Verifikasi Hidden: Row action `Edit` dan `Delete`
41. Verifikasi Hidden: Checkbox baris tabel
42. Verifikasi Hidden: Bulk Action Bar `[Delete]`

## Notes

- Memvalidasi visibilitas dasar antarmuka per peran: Tab Division tersembunyi total bagi aktor tanpa capability, mode baca murni bagi aktor Read-Only (tombol aksi dan checkbox tersembunyi), peran Read-Only Access Level, serta visibilitas penuh bagi Total Control (PRD §2, §4.8).
- Sumber pemetaan test case granular: TC-GS-DIV-18, TC-GS-DIV-19, TC-GS-DIV-23, TC-GS-DIV-24.

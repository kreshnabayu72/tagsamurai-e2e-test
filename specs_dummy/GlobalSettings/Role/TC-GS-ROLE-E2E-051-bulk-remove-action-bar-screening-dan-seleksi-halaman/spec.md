---
id: TC-GS-ROLE-E2E-051-bulk-remove-action-bar-screening-dan-seleksi-halaman
title: "Screening Bulk Action Bar Detail, Seleksi Baris Halaman Aktif, Counter, Clear (X), dan Retensi Saat Saring"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-120
  - TC-GS-ROLE-121
  - TC-GS-ROLE-122
  - TC-GS-ROLE-136
coverage:
  web: automated
---

# Screening Bulk Action Bar Detail, Seleksi Baris Halaman Aktif, Counter, Clear (X), dan Retensi Saat Saring

## Prerequisites

- Login sebagai Total Control
- Data Uji: Detail Manage hardware dengan multi-user
- Setup Hook: beforeEach: navigateTo(Detail)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage hardware"

## Test Steps

### Screening Bulk Action Bar Detail (TC-GS-ROLE-120)

1. Centang 1 baris
2. Screening Bulk Action Bar
3. Centang baris kedua
4. Verifikasi Urutan elemen: button Bulk Action | counter | button Select All | icon (X)
5. Verifikasi Langkah 1: counter "1 User selected"; button "Select All ({N} records)" dengan N = jumlah baris eligible
6. Verifikasi Langkah 3: counter "2 Users selected"

### Checkbox header Detail — select page, header tidak checked penuh, deselect (TC-GS-ROLE-121)

7. Centang checkbox header
8. Uncheck satu baris
9. Uncheck checkbox header
10. Verifikasi Langkah 1: semua baris eligible di halaman checked, baris disabled tetap unchecked; Bulk Action Bar muncul
11. Verifikasi Langkah 2: checkbox header tidak lagi checked penuh
12. Verifikasi Langkah 3: semua unchecked, Bulk Action Bar hilang

### Clear seleksi via (X) di Bulk Action Bar (TC-GS-ROLE-122)

13. Centang 2 baris
14. Klik (X)
15. Verifikasi Seleksi dibatalkan
16. Verifikasi Bulk Action Bar tertutup

### Seleksi tetap bertahan saat Search dikosongkan (TC-GS-ROLE-136)

17. Search "Wawan" + Enter
18. Centang Wawan Setiawan
19. Kosongkan Search + Enter
20. Verifikasi Wawan Setiawan tetap tercentang
21. Verifikasi Counter tetap 1

## Notes

- Memvalidasi alur skenario "Screening Bulk Action Bar Detail, Seleksi Baris Halaman Aktif, Counter, Clear (X), dan Retensi Saat Saring".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Bulk Action Bar — Detail; global-settings/role/PRD/role.md §4.4; foundation/process/prd-process/prd-conventions.md §8.
- Sumber pemetaan test case granular: TC-GS-ROLE-120, TC-GS-ROLE-121, TC-GS-ROLE-122, TC-GS-ROLE-136.

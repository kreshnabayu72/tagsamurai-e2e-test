---
id: TC-GS-USER-E2E-153-pagination-opsi-page-size
title: Pagination User List menyediakan page size 10, 25, 50, dan 100 tanpa opsi All
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-612
coverage:
  web: automated
---

# Pagination User List menyediakan page size 10, 25, 50, dan 100 tanpa opsi All

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Minimal 101 login user di entity ini (seeding)
- Spec ini hanya membaca data

## Test Steps

1. Buka sub-tab "Login User" di User List
2. Verifikasi page size default 10
3. Buka dropdown Page Size dan verifikasi opsinya persis 10, 25, 50, dan 100, tanpa "All"
4. Pilih 25 dan verifikasi 25 baris dengan 5 halaman
5. Pilih 50 dan verifikasi 50 baris dengan 3 halaman
6. Pilih 100 dan verifikasi 100 baris pada halaman 1

## Notes

- Melengkapi `TC-GS-USER-E2E-007` yang hanya menguji page size 25. Pasangan `TC-GS-ROLE-334`.
- Seeding 101 user dibutuhkan; kebutuhannya disampaikan ke tim FE.

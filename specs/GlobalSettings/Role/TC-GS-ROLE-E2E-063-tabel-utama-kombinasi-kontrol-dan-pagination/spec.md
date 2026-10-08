---
id: TC-GS-ROLE-E2E-063-tabel-utama-kombinasi-kontrol-dan-pagination
title: "Kombinasi 4 Kontrol Tabel Utama, Pemulihan Empty Result Saat Filter Dilepas, dan Paginasi 10/25/50/100"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-151
  - TC-GS-ROLE-157
  - TC-GS-ROLE-158
  - TC-GS-ROLE-159
coverage:
  web: automated
---

# Kombinasi 4 Kontrol Tabel Utama, Pemulihan Empty Result Saat Filter Dilepas, dan Paginasi 10/25/50/100

## Prerequisites

- Login sebagai Total Control
- Data Uji: Pre-setup volume data (≥11 baris)
- Setup Hook: beforeEach: navigateTo(Tab Total Control)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup tersedia; Tab Total Control dan Tab Read Only masing-masing berisi ≥3 user dengan Position/Division berbeda
- Tab Total Control berisi >10 user
- Tab Total Control dan Tab Read Only masing-masing berisi >10 user

## Test Steps

### Search lalu Filter dan Filter lalu Search (TC-GS-ROLE-151)

1. Search "a" + Enter, lalu Filter Division Finance + Status Active → Apply
2. Reset; Filter Division Finance + Status Active → Apply, lalu Search "a" + Enter
3. Verifikasi Langkah 1: hasil = baris cocok "a" ∩ Finance ∩ Active; keyword tetap di search bar
4. Verifikasi Langkah 2: hasil identik langkah 1; filter tetap aktif

### Kombinasi Search, Filter, Sort, dan Pagination (TC-GS-ROLE-157)

5. Search "a" + Enter
6. Filter Status Active → Apply
7. Sort Name Z-A
8. Ubah page size 25
9. Clear Filter → Apply
10. Kosongkan Search + Enter
11. Verifikasi Langkah 1–4: hasil = cocok "a" ∩ Active, urut Z-A, 25 per halaman
12. Verifikasi Langkah 5: Search dan Sort tetap berlaku
13. Verifikasi Langkah 6: Filter yang tersisa dan Sort tetap berlaku

### Pulih dari no-result saat satu saringan dilepas (TC-GS-ROLE-158)

14. Search "Dewi" + Enter
15. Filter Status Active → Apply (Dewi Inactive)
16. Clear Filter → Apply
17. Verifikasi Langkah 2: "No results found"
18. Verifikasi Langkah 3: baris Dewi Lestari tampil kembali

### Pagination Tab Total Control dan Tab Read Only (TC-GS-ROLE-159)

19. Amati default
20. Buka dropdown page size
21. Klik halaman berikutnya lalu sebelumnya
22. Ulangi di Tab Read Only
23. Verifikasi Default 10 baris
24. Verifikasi Opsi 10/25/50/100
25. Verifikasi Navigasi halaman berfungsi
26. Verifikasi Tab Read Only identik

## Notes

- Memvalidasi alur skenario "Kombinasi 4 Kontrol Tabel Utama, Pemulihan Empty Result Saat Filter Dilepas, dan Paginasi 10/25/50/100".
- Aturan PRD terkait: foundation/process/prd-process/prd-conventions.md §9.8; global-settings/role/PRD/role.md §5; global-settings/role/PRD/role.md §4.1.1; global-settings/role/PRD/role.md §4.1.2; global-settings/role/PRD/role.md §5 Pagination.
- Sumber pemetaan test case granular: TC-GS-ROLE-151, TC-GS-ROLE-157, TC-GS-ROLE-158, TC-GS-ROLE-159.

---
id: TC-GS-ROLE-E2E-025-assign-total-control-picker-sorting-pagination-retensi
title: "Pengurutan 3-State 5 Kolom, Paginasi 10/25/50/100, dan Retensi Seleksi Lintas Halaman pada Picker Assign Total Control"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-75
  - TC-GS-ROLE-293
coverage:
  web: automated
---

# Pengurutan 3-State 5 Kolom, Paginasi 10/25/50/100, dan Retensi Seleksi Lintas Halaman pada Picker Assign Total Control

## Prerequisites

- Login sebagai Total Control; pool kandidat >10 user
- Data Uji: Pre-setup #11 + #17 (Volume user)
- Setup Hook: beforeEach: openModalAssignTC()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pool picker berisi >10 user (Pre-setup #11 + #17)
- User berada di Global Settings > Role & Permission > Total Control
- Kandidat Pre-setup #11 tersedia

## Test Steps

### Pagination Popup Assign (TC-GS-ROLE-75)

1. Klik [+ Assign]
2. Ubah page size ke 25
3. Kembali ke 10, klik halaman 2
4. Centang 1 user di halaman 2, kembali ke halaman 1
5. Verifikasi Default 10 baris; opsi 10/25/50/100
6. Verifikasi Navigasi halaman berfungsi
7. Verifikasi Centang di halaman 2 tetap tersimpan (counter tetap 1)

### Sort kolom Popup Assign (TC-GS-ROLE-293)

8. Klik [+ Assign]
9. Klik header Name 3 kali
10. Klik header Email 3 kali
11. Klik header Position 3 kali
12. Klik header Division 3 kali
13. Klik header Status 3 kali
14. Verifikasi Name: A-Z / Z-A / default Name A-Z
15. Verifikasi Email: A-Z / Z-A / default
16. Verifikasi Position: A-Z / Z-A / default
17. Verifikasi Division: A-Z / Z-A / default
18. Verifikasi Status: Active First / Inactive First (Maya Anggraini di atas) / default
19. Verifikasi Seleksi checkbox tidak berubah saat sort

## Notes

- Memvalidasi alur skenario "Pengurutan 3-State 5 Kolom, Paginasi 10/25/50/100, dan Retensi Seleksi Lintas Halaman pada Picker Assign Total Control".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Pagination; global-settings/role/PRD/role.md §5; global-settings/role/PRD/role.md §4.1.5; global-settings/role/PRD/role.md §4.2 Sort; foundation/process/prd-process/prd-conventions.md §9.7.
- Sumber pemetaan test case granular: TC-GS-ROLE-75, TC-GS-ROLE-293.

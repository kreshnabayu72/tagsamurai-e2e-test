---
id: TC-GS-ROLE-E2E-039-tabel-read-only-search-filter-sort-download-dan-pagination
title: "Pengujian Table Tools Tab Read Only: Search, Filter 8 Field, Sort Name, Download CSV/XLSX, dan Pagination"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-71
  - TC-GS-ROLE-128
  - TC-GS-ROLE-138
  - TC-GS-ROLE-154
  - TC-GS-ROLE-174
  - TC-GS-ROLE-184
  - TC-GS-ROLE-204
  - TC-GS-ROLE-335
  - TC-GS-ROLE-340
  - TC-GS-ROLE-347
coverage:
  web: automated
---

# Pengujian Table Tools Tab Read Only: Search, Filter 8 Field, Sort Name, Download CSV/XLSX, dan Pagination

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia dataset user pada Tab Read Only

## Test Steps

1. Buka Global Settings > Role & Permission > Tab Read Only
2. Uji Search box: ketik nama user lalu tekan Enter, verifikasi tabel terfilter, lalu reset
3. Buka Filter Panel: verifikasi 8 field penyaringan tersedia lengkap
4. Terapkan filter date pada kolom Last Updated dan filter dropdown multi-select
5. Verifikasi irisan data Search dan Filter bekerja akurat pada Tab Read Only
6. Klik header kolom Name untuk menguji sorting 3-state (Ascending, Descending, Default)
7. Buka Setup Column Tab Read Only dan verifikasi pengaturan kolom independen dari Tab Total Control
8. Klik tombol Download lalu pilih 'Download as CSV'
9. Verifikasi file bernama Role-Permission-Read-Only.csv berhasil diunduh
10. Uji navigasi pagination footer: ubah page size ke 25 dan navigasi halaman berikutnya

## Notes

- Tab Read Only memiliki fungsionalitas Table Tools penuh yang independen dari Tab Total Control (role.md §4.2a).

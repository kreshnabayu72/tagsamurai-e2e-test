---
id: TC-GS-ROLE-E2E-024-detail-bulk-action-bar-screening-server-select-all-dan-selection-limit
title: "Screening Bulk Action Bar, Counter Seleksi, Server Select All Lintas Halaman, Toggle Unselect All, dan Selection Limit 1000"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-45
  - TC-GS-ROLE-229
  - TC-GS-ROLE-320
  - TC-GS-ROLE-321
coverage:
  web: automated
---

# Screening Bulk Action Bar, Counter Seleksi, Server Select All Lintas Halaman, Toggle Unselect All, dan Selection Limit 1000

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia lebih dari 10 user ter-assign pada Detail role (tersebar di minimal 2 halaman paginasi)

## Test Steps

1. Buka Global Settings > Role & Permission > Tab System > Detail salah satu role
2. Centang checkbox pada 2 baris user pertama
3. Verifikasi Bulk Action Bar melayang (floating bar) muncul di bagian bawah layar menampilkan counter: "2 users selected"
4. Verifikasi Bulk Action Bar memuat tombol [Remove] dan tombol "Select All ({N} records)"
5. Klik tombol "Select All ({N} records)"
6. Verifikasi seluruh data tercentang lintas halaman dan tombol bertransformasi label menjadi "Unselect All"
7. Klik tombol "Unselect All"
8. Verifikasi seluruh centang dibatalkan dan Bulk Action Bar tertutup
9. Centang baris user satu per satu hingga mencapai batas 1000 record (atau simulasikan via mock limit)
10. Verifikasi checkbox baris ke-1001 dinonaktifkan (disabled) dengan tooltip: "You've reached the maximum selection of 1000 rows."
11. Klik tombol "Select All" saat dataset melebihi 1000 baris
12. Verifikasi seleksi dibatasi otomatis pada 1000 baris pertama dengan toast peringatan: "Error, only the first 1000 of {total} rows were selected. Narrow your filter to include the rest."

## Notes

- Mekanisme seleksi massal menerapkan batas maksimal 1000 baris dan toggle Unselect All saat seluruh record tercentang (prd-conventions §Bulk Selection).

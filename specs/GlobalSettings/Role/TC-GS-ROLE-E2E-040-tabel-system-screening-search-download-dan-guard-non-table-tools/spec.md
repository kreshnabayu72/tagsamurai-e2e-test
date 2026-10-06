---
id: TC-GS-ROLE-E2E-040-tabel-system-screening-search-download-dan-guard-non-table-tools
title: "Pengujian Tabel Tab System: 6 Baris Fixed, Pencarian Role Name, Download CSV/XLSX, dan Guard Ketiadaan Sort/Pagination"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-72
  - TC-GS-ROLE-129
  - TC-GS-ROLE-185
  - TC-GS-ROLE-337
  - TC-GS-ROLE-348
coverage:
  web: automated
---

# Pengujian Tabel Tab System: 6 Baris Fixed, Pencarian Role Name, Download CSV/XLSX, dan Guard Ketiadaan Sort/Pagination

## Prerequisites

- Login sebagai Role: Total Control

## Test Steps

1. Buka Global Settings > Role & Permission > Tab System
2. Verifikasi tabel menampilkan 6 baris role tetap: Import data, Manage files, Manage hardware, Manage master reference, Manage TAG, Manage user and role
3. Klik icon Search, ketik 'Import data', lalu tekan Enter
4. Verifikasi tabel hanya menampilkan baris role Import data
5. Reset pencarian dan amati header tabel Tab System
6. Verifikasi kolom tabel Tab System tidak memiliki icon sort dan tidak dapat diklik untuk mengurutkan (non-sortable)
7. Verifikasi pada toolbar Tab System tidak ada icon Setup Column
8. Verifikasi di bagian footer Tab System tidak ada komponen pagination (tabel statis 6 baris tanpa pagination)
9. Klik tombol Download pada toolbar lalu pilih 'Download as CSV'
10. Verifikasi file bernama Role-Permission-System.csv berhasil diunduh dengan isi tepat 6 baris role data dan header Role Name | Users

## Notes

- Tab System adalah katalog 6 role tetap tanpa fitur sorting, setup column, maupun pagination (role.md §4.2, §5).

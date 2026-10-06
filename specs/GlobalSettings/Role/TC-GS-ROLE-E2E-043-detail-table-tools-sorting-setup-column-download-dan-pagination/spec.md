---
id: TC-GS-ROLE-E2E-043-detail-table-tools-sorting-setup-column-download-dan-pagination
title: "Sorting 3-State 6 Kolom, Setup Column, Download CSV/XLSX Dinamis, dan Pagination Halaman Detail"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-175
  - TC-GS-ROLE-176
  - TC-GS-ROLE-177
  - TC-GS-ROLE-178
  - TC-GS-ROLE-179
  - TC-GS-ROLE-180
  - TC-GS-ROLE-186
  - TC-GS-ROLE-205
  - TC-GS-ROLE-336
  - TC-GS-ROLE-349
coverage:
  web: automated
---

# Sorting 3-State 6 Kolom, Setup Column, Download CSV/XLSX Dinamis, dan Pagination Halaman Detail

## Prerequisites

- Login sebagai Role: Total Control
- Buka halaman Detail pada role 'Manage TAG'

## Test Steps

1. Buka Tab System > Detail role 'Manage TAG'
2. Uji sorting 3-state (Ascending, Descending, Default) pada 6 kolom: Position, Division, Activation Status, Temporary User, Temporary Until, TAG
3. Klik icon Setup Column pada toolbar Detail
4. Verifikasi bahwa kontrol fungsional Checkbox seleksi dan kolom CRUD dinamis (R, U) selalu tampil permanen
5. Uji pengaturan visibilitas kolom data lainnya melalui Setup Column modal
6. Klik tombol Download pada toolbar Detail lalu pilih 'Download as CSV'
7. Verifikasi file bernama Role-Permission-Manage-TAG.csv berhasil diunduh dengan substitusi nama role aktual secara dinamis pada nama file
8. Amati kontrol pagination di footer Detail dan ubah page size ke 25 record
9. Verifikasi paginasi berfungsi lancar dan merender jumlah data sesuai pilihan

## Notes

- Filename ekspor pada halaman Detail secara dinamis menyertakan nama role yang sedang dibuka (role.md §4.2a, §9.9).

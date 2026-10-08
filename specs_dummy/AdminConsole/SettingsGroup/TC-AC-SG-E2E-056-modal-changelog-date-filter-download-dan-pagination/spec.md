---
id: TC-AC-SG-E2E-056-modal-changelog-date-filter-download-dan-pagination
title: "Modal Changelog: filter Date Range (termasuk single date), overlay download CSV/XLSX, dan paginasi modal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-200
  - TC-AC-SG-201
  - TC-AC-SG-202
  - TC-AC-SG-203
coverage:
  web: automated
---

# Modal Changelog: filter Date Range (termasuk single date), overlay download CSV/XLSX, dan paginasi modal

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat > 10 entri riwayat pada Modal Changelog lintas tanggal

## Test Steps

### Filter Date Range & Single Date
1. Buka Modal Changelog lalu buka Filter Panel
2. Pilih rentang tanggal Start Date dan End Date spesifik lalu klik `[Apply]`
3. Verifikasi tabel Changelog hanya menampilkan entri dalam rentang tanggal tersebut
4. Buka kembali Filter Panel, pilih tanggal yang sama untuk Start dan End Date (single date, 1 hari saja)
5. Klik `[Apply]`
6. Verifikasi tabel Changelog hanya menampilkan mutasi tepat pada tanggal tersebut
### Overlay Format Download Changelog
7. Klik icon Download di toolbar Modal Changelog
8. Verifikasi overlay memunculkan 2 opsi: `"Download as CSV"` dan `"Download as XLSX"`
9. Klik `"Download as CSV"` dan verifikasi file terunduh dengan nama `"Changelog-Group.csv"` tanpa toast sukses
### Paginasi Modal Changelog
10. Amati footer paginasi modal Changelog (default 10 baris)
11. Buka dropdown baris per halaman, verifikasi opsi `10`, `25`, `50`, dan `100`
12. Pilih opsi `25` dan verifikasi kuota baris log bertambah sesuai pilihan

## Notes

- Download Changelog menggunakan nama kanonikal Changelog-Group.

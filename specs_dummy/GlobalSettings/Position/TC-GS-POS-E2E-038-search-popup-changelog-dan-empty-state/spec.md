---
id: TC-GS-POS-E2E-038-search-popup-changelog-dan-empty-state
title: "Search Popup Changelog: siklus interaksi, pencarian lintas kolom teks, Field, Date guard, dan no-match"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-205
  - TC-GS-POS-206
  - TC-GS-POS-207
  - TC-GS-POS-208
  - TC-GS-POS-209
  - TC-GS-POS-210
coverage:
  web: automated
---

# Search Popup Changelog: siklus interaksi, pencarian lintas kolom teks, Field, Date guard, dan no-match

## Prerequisites

- Login sebagai Total Control
- Popup Changelog terbuka dan memuat entri riwayat Create, Edit, dan Delete

## Test Steps

### Siklus Pencarian Lintas Kolom Teks

1. Buka Popup Changelog
2. Masukkan kata kunci "Create" pada input Search Changelog
3. Verifikasi baris dengan Action "Create" tersaring
4. Masukkan nama jabatan (misal "Manager")
5. Verifikasi baris dengan Position Name, Old Value, atau New Value yang mengandung "Manager" tersaring
6. Masukkan kata kunci nama aktor Modified By (misal "Budi")
7. Verifikasi baris yang dimodifikasi oleh aktor tersebut tersaring

### Pencarian Kolom Field & Guard Kolom Date

8. Masukkan kata kunci "Position Name" (nilai kolom Field)
9. Verifikasi baris perubahan field tersebut tersaring
10. Masukkan angka tahun "2026"
11. Verifikasi pencarian tidak mencari kolom Date (Date guard aktif)

### No-Match Empty State

12. Masukkan keyword tanpa kecocokan "nomatchstring123"
13. Verifikasi Changelog menampilkan empty state pencarian: "No results found"
14. Bersihkan search input dan verifikasi seluruh riwayat kembali tampil

## Notes

- Menggabungkan TC-GS-POS-205 s.d. 210.

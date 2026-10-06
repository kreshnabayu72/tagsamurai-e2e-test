---
id: TC-GS-DIV-E2E-035-bulk-delete-mixed-sebagian-aman-sebagian-in-use
title: "Bulk Delete Campuran: Menghapus Divisi Aman dan Melewati Divisi In-Use"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-51
coverage:
  web: automated
---

# Bulk Delete Campuran: Menghapus Divisi Aman dan Melewati Divisi In-Use

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia 1 divisi aman 'Human Resources 2' dan 1 divisi in-use 'Head Office'

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Centang checkbox pada baris 'Human Resources 2' (aman) dan 'Head Office' (in-use)
3. Klik tombol '[Delete]' pada Bulk Action Bar
4. Verifikasi muncul dialog konfirmasi campuran 'Delete Divisions' (severity warning, Dialog 3)
5. Verifikasi body dialog terbagi menjadi 2 kelompok bullet yang jelas:
6.   - Kelompok 'The following will be deleted:' memuat 'Human Resources 2'
7.   - Kelompok 'The following are still in use and will be skipped:' memuat 'Head Office'
8. Verifikasi terdapat kalimat konfirmasi 'Are you sure you want to continue? This action cannot be undone.' serta tombol '[Cancel]' dan '[Continue]'
9. Klik tombol '[Continue]'
10. Verifikasi toast sukses campuran muncul: 'Success, division has been deleted. Some items were skipped (still in use).'
11. Verifikasi baris 'Human Resources 2' terhapus dari tabel sedangkan baris 'Head Office' tetap ada

## Notes

- Memvalidasi pemisahan item aman dan item in-use pada bulk delete mixed (division.md §4.2d Dialog 3).

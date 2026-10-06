---
id: TC-GS-DIV-E2E-036-bulk-delete-uniform-semua-item-aman
title: "Bulk Delete Homogen: Menghapus Seluruh Divisi Terpilih yang Bebas Relasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-50
coverage:
  web: automated
---

# Bulk Delete Homogen: Menghapus Seluruh Divisi Terpilih yang Bebas Relasi

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia divisi aman 'Marketing' dan 'Operations' yang bebas relasi

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Centang checkbox baris 'Marketing' dan 'Operations'
3. Klik tombol '[Delete]' pada Bulk Action Bar
4. Verifikasi muncul dialog konfirmasi homogen 'Delete Divisions' (severity danger, Dialog 4)
5. Verifikasi body dialog memuat list bullet '• Marketing' dan '• Operations' serta kalimat 'Are you sure you want to delete them? This action cannot be undone.'
6. Klik tombol '[Delete]'
7. Verifikasi toast sukses muncul: 'Success, division has been deleted.'
8. Verifikasi kedua divisi ('Marketing' dan 'Operations') terhapus tuntas dari tabel utama

## Notes

- Memvalidasi penghapusan serentak record bebas relasi sesuai division.md §4.2d Dialog 4.

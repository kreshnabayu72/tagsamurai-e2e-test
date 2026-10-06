---
id: TC-GS-DIV-E2E-034-bulk-delete-blocked-total-seluruh-item-in-use
title: "Pemblokiran Bulk Delete Total Saat Seluruh Divisi Terpilih Sedang In-Use"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-52
coverage:
  web: automated
---

# Pemblokiran Bulk Delete Total Saat Seluruh Divisi Terpilih Sedang In-Use

## Prerequisites

- Login sebagai Role: Total Control
- Seluruh divisi yang dipilih berstatus in-use (misal Head Office dan Human Resources)

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Centang checkbox pada baris 'Head Office' dan 'Human Resources'
3. Klik tombol '[Delete]' pada Bulk Action Bar
4. Verifikasi langsung muncul dialog peringatan blocker 'Cannot Delete Data' (Dialog 2)
5. Verifikasi body dialog menampilkan seluruh nama divisi yang terpilih dengan suffix '— still in use' di dalam container scrollable
6. Verifikasi terdapat penjelasan 'These divisions are still in use. Remove the references before deleting.' dan tombol tunggal '[OK]'
7. Klik '[OK]'
8. Verifikasi tidak ada data yang terhapus dan tidak ada toast sukses palsu

## Notes

- Menguji evaluasi bulk blocked total sesuai division.md §4.2d Dialog 2.

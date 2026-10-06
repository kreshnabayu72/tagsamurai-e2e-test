---
id: TC-GS-DIV-E2E-032-bulk-selection-server-select-all-dan-selection-limit
title: "Server Select All Lintas Halaman, Unselect All, dan Pembatasan Batas 1000 Baris"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-227
  - TC-GS-DIV-254
  - TC-GS-DIV-255
coverage:
  web: automated
---

# Server Select All Lintas Halaman, Unselect All, dan Pembatasan Batas 1000 Baris

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat dataset divisi multi-halaman (>10 data)

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Centang checkbox header untuk memilih seluruh baris di halaman aktif
3. Verifikasi muncul banner / tombol tautan 'Select All {N} records' untuk seleksi server-side lintas halaman
4. Klik tombol tautan 'Select All {N} records'
5. Verifikasi seluruh record terhitung terpilih dan tombol teks berubah / menghilang menyisakan tombol '[✕]'
6. Hapus centang pada salah satu baris secara manual
7. Verifikasi status kembali menjadi seleksi parsial dan tombol tautan Select All muncul kembali
8. Simulasikan seleksi manual hingga baris ke-1001
9. Verifikasi checkbox ke-1001 berstatus disabled dengan tooltip 'You\'ve reached the maximum selection of 1000 rows.'
10. Simulasikan klik Select All saat hasil filter >1000 baris
11. Verifikasi seleksi otomatis ter-cap pada 1000 baris pertama disertai toast peringatan persisten 'Error, only the first 1000 of {total} rows were selected. Narrow your filter to include the rest.'

## Notes

- Menguji aturan platform Selection Limit / Bulk Action Checkbox Limit sesuai prd-conventions.md.

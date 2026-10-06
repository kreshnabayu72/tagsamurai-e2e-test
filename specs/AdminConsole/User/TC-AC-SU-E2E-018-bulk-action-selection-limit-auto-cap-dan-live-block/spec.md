---
id: TC-AC-SU-E2E-018-bulk-action-selection-limit-auto-cap-dan-live-block
title: "Selection Limit 1000 baris: auto-cap pada Server Select All dan live-block disabled pada centang manual ke-1001"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-39
  - TC-AC-SU-222
coverage:
  web: automated
---

# Selection Limit 1000 baris: auto-cap pada Server Select All dan live-block disabled pada centang manual ke-1001

## Prerequisites

- Login sebagai Role: Principal Total Control
- Dataset simulasi >1000 data pengguna (contoh: 1500 baris)

## Test Steps

### Auto-Cap pada Server Select All >1000 Baris

1. Buka User List pada dataset 1500 baris
2. Klik tombol `"Select All (1500 records)"` pada Bulk Action Bar
3. Verifikasi seleksi dibatasi otomatis (auto-cap) tepat pada 1000 baris pertama
4. Verifikasi toast error persisten muncul: `"Error, only the first 1000 of 1500 rows were selected. Narrow your filter to include the rest."`

### Live-Block Seleksi Manual pada Baris ke-1001

1. Lepas seleksi data
2. Lakukan seleksi manual baris per baris hingga mencapai 1000 baris terpilih
3. Amati checkbox pada baris data ke-1001
4. Verifikasi checkbox baris ke-1001 otomatis berstatus Disabled dengan tooltip `"You've reached the maximum selection of 1000 rows."`
5. Verifikasi 1000 baris sebelumnya tetap tercentang dan Bulk Action Bar dapat digunakan normal

## Notes

- Batas seleksi 1000 baris melindungi beban komputasi transaksi massal backend.

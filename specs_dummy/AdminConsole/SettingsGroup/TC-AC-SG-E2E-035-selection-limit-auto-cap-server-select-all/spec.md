---
id: TC-AC-SG-E2E-035-selection-limit-auto-cap-server-select-all
title: "Selection Limit: Auto-cap Server Select All pada hasil filtered melebihi 1000 baris"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-152
coverage:
  web: automated
---

# Selection Limit: Auto-cap Server Select All pada hasil filtered melebihi 1000 baris

## Prerequisites

- Login sebagai Role: Total Control
- Total baris group hasil filter melebihi 1000 (contoh: 1500 baris)

## Test Steps

### Auto-Cap Select All
1. Terapkan filter hingga total baris yang cocok berjumlah 1500 records
2. Amati tombol `"Select All (1500 records)"` pada Bulk Action Bar
3. Klik tombol `"Select All (1500 records)"`
4. Verifikasi sistem tidak memblokir seleksi, melainkan secara otomatis meng-cap seleksi ke 1000 baris pertama
5. Verifikasi muncul Toast Error yang persisten (tidak auto-dismiss): `"Error, only the first 1000 of 1500 rows were selected. Narrow your filter to include the rest."`
6. Verifikasi Bulk Action Bar menampilkan counter `1000 selected` dan tombol Delete dapat dieksekusi

## Notes

- Toast auto-cap persisten hingga di-dismiss manual oleh pengguna.

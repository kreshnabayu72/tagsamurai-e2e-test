---
id: TC-AC-SG-E2E-036-bulk-delete-select-all-cycle-dan-persistensi
title: "Siklus seleksi massal: kemunculan Bulk Action Bar, persistensi seleksi lintas halaman, dan Server Select All"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-69
  - TC-AC-SG-96
  - TC-AC-SG-148
coverage:
  web: automated
---

# Siklus seleksi massal: kemunculan Bulk Action Bar, persistensi seleksi lintas halaman, dan Server Select All

## Prerequisites

- Login sebagai Role: Total Control
- Dataset > 10 group tersebar pada ≥ 2 halaman tabel

## Test Steps

### Kemunculan Bar & Persistensi Halaman
1. Buka `Settings > Group`
2. Centang checkbox pada baris ke-1 di Halaman 1
3. Verifikasi Bulk Action Bar muncul di bawah tabel memuat tombol `[Delete]`
4. Pindah navigasi ke Halaman 2 tabel
5. Centang baris ke-1 di Halaman 2
6. Kembali navigasi ke Halaman 1
7. Verifikasi baris ke-1 di Halaman 1 tetap dalam kondisi tercentang (persist lintas halaman)
### Siklus Button Select All Lintas Halaman
8. Amati button `"Select All ({N} records)"` pada Bulk Action Bar
9. Klik button `"Select All ({N} records)"`
10. Verifikasi seluruh baris di seluruh halaman tercentang (Server Select All)
11. Verifikasi button bertransformasi label menjadi `"Unselect All"`
12. Hilangkan centang pada 1 baris
13. Verifikasi button kembali bertransformasi menjadi `"Select All ({N} records)"`
14. Centang ulang baris tersebut lalu klik `"Unselect All"`
15. Verifikasi seluruh seleksi dibatalkan dan Bulk Action Bar tertutup

## Notes

- Menerapkan standar perilaku Bulk Selection GAP-021.

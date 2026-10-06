---
id: TC-GS-DIV-E2E-031-bulk-action-bar-screening-counter-dan-checkbox-header
title: "Screening Bulk Action Bar, Counter Seleksi, dan Checkbox Header 3-State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-47
  - TC-GS-DIV-48
  - TC-GS-DIV-49
coverage:
  web: automated
---

# Screening Bulk Action Bar, Counter Seleksi, dan Checkbox Header 3-State

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Tabel memuat minimal 3 data divisi

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Verifikasi Bulk Action Bar dalam keadaan tersembunyi secara default
3. Centang checkbox pada baris pertama
4. Verifikasi Bulk Action Bar melayang (floating bar) muncul memuat counter '1 division selected', tombol '[Delete]', dan tombol close '[✕]'
5. Centang checkbox pada baris kedua
6. Verifikasi counter realtime berubah menjadi '2 divisions selected' (bentuk jamak)
7. Verifikasi checkbox di header tabel berada pada kondisi indeterminate (garis strip minus)
8. Klik checkbox header tabel
9. Verifikasi seluruh baris pada halaman aktif tercentang dan counter terupdate
10. Klik kembali checkbox header tabel
11. Verifikasi seluruh centang terlepas dan Bulk Action Bar otomatis menghilang
12. Centang kembali 1 baris lalu klik tombol '[✕]' pada Bulk Action Bar
13. Verifikasi seluruh centang dibersihkan dan bar melayang tertutup

## Notes

- Mengikuti spesifikasi komponen Bulk Action Bar pada division.md §4.1 item 10 dan §4.4 item 2.

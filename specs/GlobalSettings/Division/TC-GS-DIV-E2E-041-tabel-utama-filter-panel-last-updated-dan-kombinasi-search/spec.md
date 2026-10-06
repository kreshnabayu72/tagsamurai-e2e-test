---
id: TC-GS-DIV-E2E-041-tabel-utama-filter-panel-last-updated-dan-kombinasi-search
title: "Filter Panel Last Updated Tunggal dan Irisan Presisi dengan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-58
  - TC-GS-DIV-59
  - TC-GS-DIV-60
  - TC-GS-DIV-61
coverage:
  web: automated
---

# Filter Panel Last Updated Tunggal dan Irisan Presisi dengan Search

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat data divisi dengan tanggal Last Updated bervariasi

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Klik tombol 'Filter' pada toolbar TableTools
3. Verifikasi Filter Panel terbuka menampilkan tepat 1 field: 'Last Updated' dengan DateRangePicker placeholder 'Select date', serta tombol '[Clear Field]' dan '[Apply]'
4. Pilih rentang tanggal spesifik pada date picker 'Last Updated' lalu klik '[Apply]'
5. Verifikasi tabel tersaring hanya menampilkan baris data yang tanggal perubahannya berada dalam rentang terpilih
6. Lakukan pencarian keyword 'Mark' di kotak search
7. Verifikasi tabel menampilkan irisan data presisi (Nama mengandung 'Mark' DAN Last Updated sesuai rentang)
8. Buka kembali Filter Panel, ubah tanggal, dan klik '[Apply]'
9. Verifikasi filter tanggal terbarui tanpa menghilangkan keyword pencarian yang aktif

## Notes

- Satu-satunya field filter pada tabel utama Division adalah Last Updated (division.md §4.2 dan GAP-157).

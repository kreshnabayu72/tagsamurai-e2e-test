---
id: TC-GS-USER-E2E-032-delete-single-screening-dialog-dan-proteksi
title: "Delete Single: Screening dialog konfirmasi Delete, proteksi guard, dan pembatalan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-261
  - TC-GS-USER-262
  - TC-GS-USER-263
  - TC-GS-USER-264
  - TC-GS-USER-265
  - TC-GS-USER-266
  - TC-GS-USER-267
  - TC-GS-USER-268
  - TC-GS-USER-1015
coverage:
  web: automated
---

# Delete Single: Screening dialog konfirmasi Delete, proteksi guard, dan pembatalan

## Prerequisites

- Login sebagai Role: Total Control
- User Rudi Hakim (siap dihapus) tersedia

## Test Steps

### Screening Dialog Delete

1. Klik ikon menu (⋯) pada baris Rudi Hakim, pilih 'Delete'
2. Verifikasi dialog konfirmasi Delete muncul dengan pesan peringatan dan tombol '[Cancel]' serta '[Delete]'
3. Klik '[Cancel]', verifikasi dialog tertutup dan user Rudi Hakim tetap ada di tabel

## Notes

- Menggabungkan 9 test case granular (TC-GS-USER-261 s.d. TC-GS-USER-1015).

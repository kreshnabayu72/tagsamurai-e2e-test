---
id: TC-GS-DIV-E2E-037-bulk-delete-oleh-actor-capability-delete-only
title: "Penghapusan Massal Divisi Berhasil oleh Aktor Ber-capability Delete-Only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-215
coverage:
  web: automated
---

# Penghapusan Massal Divisi Berhasil oleh Aktor Ber-capability Delete-Only

## Prerequisites

- Login sebagai pengguna dengan peran Manage User Role berizin Delete-Only
- Tersedia minimal 2 divisi aman yang bebas relasi

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Centang checkbox pada 2 divisi aman
3. Verifikasi Bulk Action Bar muncul dengan tombol '[Delete]'
4. Klik '[Delete]' pada Bulk Action Bar dan klik '[Delete]' pada dialog konfirmasi
5. Verifikasi toast sukses muncul dan kedua divisi berhasil terhapus

## Notes

- Memastikan hak akses bulk delete didukung penuh pada role Delete-Only (division.md §2).

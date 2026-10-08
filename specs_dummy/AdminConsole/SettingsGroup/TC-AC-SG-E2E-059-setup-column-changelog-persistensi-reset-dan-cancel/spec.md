---
id: TC-AC-SG-E2E-059-setup-column-changelog-persistensi-reset-dan-cancel
title: "Setup Column Modal Changelog: persistensi reload F5, Reset to Default, dan Cancel Discard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-218
  - TC-AC-SG-219
  - TC-AC-SG-220
coverage:
  web: automated
---

# Setup Column Modal Changelog: persistensi reload F5, Reset to Default, dan Cancel Discard

## Prerequisites

- Login sebagai Role: Total Control
- Modal Changelog terbuka

## Test Steps

### Persistensi Reload F5
1. Ubah visibilitas dan urutan kolom Changelog lalu Save
2. Reload halaman browser (F5)
3. Buka kembali Modal Changelog -> Setup Column
4. Verifikasi setting kolom tetap sesuai penyimpanan terakhir
### Reset to Default
5. Klik tombol `[Reset to Default]` di footer modal
6. Verifikasi seluruh kolom kembali ke susunan dan visibilitas bawaan
7. Klik `[Save]`
### Cancel Discard Perubahan
8. Buka kembali Setup Column, ubah checkbox, lalu klik `[Cancel]` (atau `[✕]`)
9. Verifikasi perubahan dibatalkan tanpa tersimpan

## Notes

- Pengaturan kolom Changelog tersimpan persisten secara independen.

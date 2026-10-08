---
id: TC-AC-SU-E2E-020-bulk-action-bar-single-row-collapse-dialog-format
title: "Bulk Action Bar dengan 1 Baris Terpilih Collapse ke Format Dialog Baris Tunggal"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-230
  - TC-AC-SU-231
coverage:
  web: automated
---

# Bulk Action Bar dengan 1 Baris Terpilih Collapse ke Format Dialog Baris Tunggal

## Prerequisites

- Login sebagai Total Control
- Terdapat data user di User List

## Test Steps

### Seleksi Baris Tunggal via Checkbox
1. Buka `Admin Console > Settings > User`
2. Centang tepat 1 checkbox baris user aktif
3. Verifikasi Bulk Action Bar muncul dengan teks counter `"1 User Selected"`

### Verifikasi Format Dialog Kolaps
4. Klik tombol `[Deactivate User]` pada Bulk Action Bar
5. Verifikasi dialog konfirmasi yang muncul adalah format baris tunggal: `"Are you sure to deactivate this user?"`
6. Verifikasi isi dialog TIDAK memuat bullet list nama user maupun accordion pemilih (tampilan identik dengan aksi via row action menu)
7. Klik tombol `[Cancel]` untuk menutup dialog
8. Buka kembali aksi `[Activate User]` dan verifikasi format dialog tunggal yang serupa

## Notes

Memastikan konsistensi tampilan modal saat seleksi bulk hanya memuat 1 entitas.

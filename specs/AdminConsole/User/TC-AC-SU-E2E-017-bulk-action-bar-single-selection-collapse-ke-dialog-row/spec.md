---
id: TC-AC-SU-E2E-017-bulk-action-bar-single-selection-collapse-ke-dialog-row
title: "Bulk Action Bar dengan 1 baris terpilih collapse ke format dialog baris tunggal (tanpa bullet list)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-230
  - TC-AC-SU-231
coverage:
  web: automated
---

# Bulk Action Bar dengan 1 baris terpilih collapse ke format dialog baris tunggal (tanpa bullet list)

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat pengguna Inactive dan pengguna Active

## Test Steps

### Single Selection Bulk Activate Collapse

1. Buka User List dan centang tepat 1 checkbox baris pengguna berstatus Inactive
2. Verifikasi Bulk Action Bar muncul dengan tombol `[Activate]`
3. Klik tombol `[Activate]` pada Bulk Action Bar
4. Verifikasi dialog konfirmasi yang muncul berformat Single (identik row action):
5.   - Title singular: `"Activate User"` (bukan `"Activate Users"`)
6.   - Tanpa bullet list nama pengguna di body dialog
7.   - Body teks: `"This user will regain access to the portal. Are you sure you want to activate it?"`
8. Klik `[Activate]`, verifikasi pengguna berhasil diaktifkan

### Single Selection Bulk Deactivate Collapse

1. Centang tepat 1 checkbox baris pengguna berstatus Active
2. Klik tombol `[Deactivate]` pada Bulk Action Bar
3. Verifikasi dialog konfirmasi yang muncul berformat Single:
4.   - Title singular: `"Deactivate User"`
5.   - Tanpa bullet list nama pengguna
6.   - Body teks: `"This user will lose portal access immediately. Any active sessions will be ended. Are you sure you want to deactivate it?"`
7. Klik `[Deactivate]`, verifikasi pengguna berhasil dinonaktifkan

## Notes

- Bulk Action Bar secara cerdas mengadaptasi dialog konfirmasi tunggal saat hanya 1 data yang dipilih.

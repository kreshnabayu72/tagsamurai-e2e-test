---
id: TC-GS-ROLE-E2E-083-sinkronisasi-atribut-user-format-tanggal-dan-custom-field
title: "Sinkronisasi Atribut Perubahan Posisi User, Format Tanggal General Settings, dan Kolom Custom Field"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-237
  - TC-GS-ROLE-238
  - TC-GS-ROLE-239
  - TC-GS-ROLE-240
coverage:
  web: automated
---

# Sinkronisasi Atribut Perubahan Posisi User, Format Tanggal General Settings, dan Kolom Custom Field

## Prerequisites

- Login sebagai Total Control
- Data Uji: General settings date format (dd MMM yy), Position catalog
- Setup Hook: beforeEach: navigateTo(Role & Permission)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Ahmad Fauzi ber-Position IT Manager
- General Settings: Date Format dd/MM/yy, Time 24h (HH:mm), Timezone Asia/Jakarta
- General Settings: Date Format dd/MM/yy, Time 24h (HH:mm)
- Custom Field "Region" aktif

## Test Steps

### Rename Position tercermin di Tab Total Control (TC-GS-ROLE-237)

1. Rename Position "IT Manager" menjadi "IT Head" di modul Position
2. Buka Tab Total Control
3. Verifikasi Kolom Position Ahmad Fauzi menampilkan "IT Head"

### Format tanggal mengikuti General Settings pada Tab Total Control dan filternya (TC-GS-ROLE-238)

4. Buka Tab Total Control, amati Last Updated
5. Filter Last Updated pilih rentang
6. Ubah Date Format ke dd MMM yy dan Time 12h (hh:mm a), reload
7. Verifikasi Last Updated dan nilai di input filter tampil dengan format dd/MM/yy HH:mm (mis. 17/03/23 14:30)
8. Verifikasi Setelah diubah tampil dengan format dd MMM yy hh:mm a (mis. 17 Mar 23 02:30 PM)

### Format tanggal mengikuti General Settings pada Modal Changelog dan filternya (TC-GS-ROLE-239)

9. Buka Changelog Tab System, amati Date
10. Filter Date rentang, amati input
11. Verifikasi Kolom Date dan input filter tampil dengan format dd/MM/yy HH:mm (mis. 17/03/23 14:30)

### Kolom Custom Field mengikuti status Custom Field (TC-GS-ROLE-240)

12. Tampilkan kolom Region di Tab Total Control
13. Nonaktifkan Custom Field Region di Custom Field User
14. Reload Tab Total Control
15. Verifikasi Langkah 1: kolom Region tersedia di Setup Column
16. Verifikasi Langkah 3: kolom Region tidak lagi tersedia

## Notes

- Memvalidasi alur skenario "Sinkronisasi Atribut Perubahan Posisi User, Format Tanggal General Settings, dan Kolom Custom Field".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.1.1 Position; global-settings/role/PRD/role.md §4.1.1 Last Updated; foundation/process/prd-process/prd-conventions.md §32; global-settings/role/PRD/role.md §4.1.6 Date; global-settings/role/PRD/role.md §4.1.1 [Custom Field aktif].
- Sumber pemetaan test case granular: TC-GS-ROLE-237, TC-GS-ROLE-238, TC-GS-ROLE-239, TC-GS-ROLE-240.

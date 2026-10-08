---
id: TC-GS-POS-E2E-046-cross-module-format-tanggal-general-settings
title: "External Harness: Kepatuhan format tanggal General Settings pada tabel, filter, changelog, dan filter date"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-254
  - TC-GS-POS-255
coverage:
  web: automated
---

# External Harness: Kepatuhan format tanggal General Settings pada tabel, filter, changelog, dan filter date

## Prerequisites

- Login sebagai Total Control
- Akses ke Global Settings > General Settings untuk mengubah format tanggal

## Test Steps

### Ubah Format Tanggal di General Settings

1. Buka Global Settings > General Settings
2. Ubah format tampilan Date & Time (misal dari "DD/MM/YYYY" menjadi "YYYY-MM-DD")
3. Simpan perubahan

### Verifikasi Dampak di Modul Position

4. Buka Global Settings > User > Position
5. Verifikasi seluruh tanggal pada kolom Last Updated di tabel utama mengikuti format baru "YYYY-MM-DD"
6. Buka Filter Panel tabel utama, verifikasi placeholder dan format pada date-picker mengikuti konfigurasi tersebut
7. Buka Popup Changelog: Position
8. Verifikasi kolom Date pada tabel Changelog mengikuti format tanggal yang baru
9. Buka Filter Panel Changelog, verifikasi kontrol filter tanggal juga mengikuti format tersebut

## Notes

- Menggabungkan TC-GS-POS-254 dan 255 dalam kelas External Harness.

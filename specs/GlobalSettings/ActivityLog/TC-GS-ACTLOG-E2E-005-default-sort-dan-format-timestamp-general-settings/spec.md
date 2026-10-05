---
id: TC-GS-ACTLOG-E2E-005-default-sort-dan-format-timestamp-general-settings
title: "Default sort Date descending dan format timestamp mengikuti konfigurasi General Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-12
  - TC-GS-ACTLOG-13
  - TC-GS-ACTLOG-220
  - TC-GS-ACTLOG-221
coverage:
  web: automated
---

# Default sort Date descending dan format timestamp mengikuti konfigurasi General Settings

## Prerequisites

- Login sebagai Role: Total Control
- Konfigurasi General Settings entitas: Date Format `DD/MM/YYYY`, Time Format `24-hour`
- Terdapat ≥3 entri aktivitas dengan tanggal dan waktu berbeda di Tab Session dan Tab User Action

## Test Steps

### Tab Session
1. Buka Tab Session tanpa melakukan klik pengurutan kolom apa pun
2. Verifikasi entri dengan waktu terbaru berada pada baris paling atas (default sort Date descending)
3. Amati format penulisan pada setiap baris di kolom Date
4. Verifikasi format tanggal dan waktu mengikuti pola `DD/MM/YYYY HH:mm` sesuai konfigurasi General Settings
### Tab User Action
5. Klik tab "User Action" tanpa melakukan pengurutan kolom apa pun
6. Verifikasi entri dengan waktu terbaru berada pada baris paling atas (default sort Date descending)
7. Amati format penulisan pada setiap baris di kolom Date
8. Verifikasi format tanggal dan waktu mengikuti pola `DD/MM/YYYY HH:mm` sesuai konfigurasi General Settings

## Notes

- Nilai timestamp di seluruh tabel Activity Log wajib mematuhi preferensi format lokal entitas di General Settings.

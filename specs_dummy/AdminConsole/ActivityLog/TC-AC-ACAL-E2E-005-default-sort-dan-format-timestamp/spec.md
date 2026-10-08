---
id: TC-AC-ACAL-E2E-005-default-sort-dan-format-timestamp
title: "Default sort Date newest first dan format tanggal sesuai General Settings pada kedua tab"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-04
  - TC-AC-ACAL-05
  - TC-AC-ACAL-231
  - TC-AC-ACAL-232
coverage:
  web: automated
---

# Default sort Date newest first dan format tanggal sesuai General Settings pada kedua tab

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat minimal 3 baris data log dengan timestamp berbeda pada Tab Session dan Tab User Action
- Konfigurasi General Settings format tanggal entitas: `DD/MM/YYYY` dan format waktu `24h`

## Test Steps

### Default Sort & Format Tanggal Tab Session

1. Buka menu `Admin Console > Activity Log`
2. Verifikasi baris tabel Tab Session terurut secara descending berdasarkan kolom `Date` (entri terbaru berada di baris paling atas)
3. Verifikasi teks tanggal pada setiap baris di kolom Date terformat presisi mengikuti aturan General Settings (contoh: `14/07/2026, 14:30`)

### Default Sort & Format Tanggal Tab User Action

4. Klik tab `"User Action"`
5. Verifikasi baris tabel Tab User Action terurut secara descending berdasarkan kolom `Date` (entri terbaru di paling atas)
6. Verifikasi teks tanggal pada setiap baris kolom Date terformat konsisten sesuai konfigurasi General Settings

## Notes

- Modul Activity Log menerapkan default sort Date (Newest First) secara otomatis tanpa interaksi manual dari user.

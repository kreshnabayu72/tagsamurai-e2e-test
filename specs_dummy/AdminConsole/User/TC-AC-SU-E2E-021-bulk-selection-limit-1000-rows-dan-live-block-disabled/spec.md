---
id: TC-AC-SU-E2E-021-bulk-selection-limit-1000-rows-dan-live-block-disabled
title: "Batas Seleksi Maksimum 1000 Baris dan Live Block Disabled Checkbox"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-39
  - TC-AC-SU-222
coverage:
  web: automated
---

# Batas Seleksi Maksimum 1000 Baris dan Live Block Disabled Checkbox

## Prerequisites

- Dataset sistem memuat lebih dari 1000 pengguna terdaftar
- Login sebagai Administrator Total Control

## Test Steps

### Verifikasi Auto-Cap Server Select All 1000 Baris
1. Buka `Admin Console > Settings > User`
2. Centang master checkbox pada header tabel dan klik tautan seleksi seluruh sistem
3. Verifikasi sistem melakukan auto-cap seleksi pada angka tepat `1000 users`
4. Verifikasi muncul badge peringatan: `"Selection capped at maximum limit of 1,000 users"`

### Verifikasi Live Block Checkbox ke-1001
5. Batalkan seleksi massal via `[Clear selection]`
6. Lakukan penandaan seleksi hingga kuota 1000 tercapai
7. Arahkan kursor ke checkbox baris ke-1001
8. Verifikasi checkbox baris ke-1001 secara reaktif berubah menjadi `disabled`
9. Hover pada checkbox disabled tersebut dan verifikasi tooltip: `"Maximum selection limit of 1,000 users reached"`

## Notes

Menguji batas beban seleksi DOM dan proteksi overload backend.

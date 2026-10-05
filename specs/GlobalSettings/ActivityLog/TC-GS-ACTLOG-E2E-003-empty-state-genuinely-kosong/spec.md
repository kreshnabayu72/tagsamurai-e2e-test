---
id: TC-GS-ACTLOG-E2E-003-empty-state-genuinely-kosong
title: "Tampilan empty state genuinely kosong saat entitas baru belum memiliki riwayat aktivitas"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-06
  - TC-GS-ACTLOG-07
coverage:
  web: automated
---

# Tampilan empty state genuinely kosong saat entitas baru belum memiliki riwayat aktivitas

## Prerequisites

- Login sebagai Role: Total Control
- Entitas client baru yang baru diaktifkan dan belum pernah ada aktivitas login atau mutasi data di modul Global Settings manapun

## Test Steps

1. Buka menu `Global Settings > Activity Log` pada entitas baru
2. Verifikasi Tab Session aktif secara default
3. Verifikasi area tabel Tab Session menampilkan ilustrasi empty state dan teks "No activity yet"
4. Klik tab "User Action"
5. Verifikasi area tabel Tab User Action menampilkan ilustrasi empty state dan teks "No activity yet"

## Notes

- Empty state genuinely kosong dibedakan dari no-result state yang disebabkan oleh filter atau keyword pencarian.

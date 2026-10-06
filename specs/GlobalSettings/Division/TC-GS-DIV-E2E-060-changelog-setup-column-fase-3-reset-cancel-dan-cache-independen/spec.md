---
id: TC-GS-DIV-E2E-060-changelog-setup-column-fase-3-reset-cancel-dan-cache-independen
title: "Setup Column Modal Changelog Fase 3: Reset Default, Cancel, dan Independensi Cache"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-126
  - TC-GS-DIV-127
  - TC-GS-DIV-128
coverage:
  web: automated
---

# Setup Column Modal Changelog Fase 3: Reset Default, Cancel, dan Independensi Cache

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control

## Test Steps

1. Buka modal Setup Column pada tabel Changelog
2. Ubah urutan dan visibilitas kolom lalu klik '[Cancel]'
3. Verifikasi perubahan dibatalkan dan tabel tetap pada susunan sebelumnya
4. Buka kembali modal Setup Column lalu klik '[Reset to Default]'
5. Verifikasi susunan kolom kembali ke standar awal (Date di Col 1, Modified By di Col akhir)
6. Klik '[Apply]'
7. Buka tabel utama Division List dan verifikasi pengaturan Setup Column tabel utama tidak terganggu sama sekali

## Notes

- Memastikan independensi penuh preferensi kolom antar surface tabel (division.md §4.2e).

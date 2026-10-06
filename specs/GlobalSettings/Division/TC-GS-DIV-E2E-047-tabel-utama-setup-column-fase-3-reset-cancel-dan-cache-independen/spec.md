---
id: TC-GS-DIV-E2E-047-tabel-utama-setup-column-fase-3-reset-cancel-dan-cache-independen
title: "Setup Column Fase 3: Reset to Default, Cancel Discard, dan Independensi Cache"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-78
  - TC-GS-DIV-79
  - TC-GS-DIV-80
coverage:
  web: automated
---

# Setup Column Fase 3: Reset to Default, Cancel Discard, dan Independensi Cache

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control

## Test Steps

1. Buka modal Setup Column tabel utama
2. Ubah konfigurasi kolom (sembunyikan kolom Code dan geser posisi)
3. Klik tombol '[Cancel]' atau icon close '[✕]'
4. Verifikasi seluruh modifikasi dibatalkan (discarded) dan konfigurasi tabel kembali ke state sebelum modal dibuka
5. Buka kembali modal Setup Column lalu klik tombol '[Reset to Default]'
6. Verifikasi susunan kolom dan visibilitas otomatis kembali ke default bawaan sistem (semua visible terurut Name, Code, Last Updated)
7. Klik '[Apply]'
8. Buka Modal Changelog Division lalu periksa Setup Column Changelog
9. Verifikasi pengaturan Setup Column tabel utama TIDAK mempengaruhi konfigurasi kolom tabel Changelog (independensi cache per-tabel)

## Notes

- Memastikan preferensi kolom tersimpan mandiri per tabel (division.md §4.2e).

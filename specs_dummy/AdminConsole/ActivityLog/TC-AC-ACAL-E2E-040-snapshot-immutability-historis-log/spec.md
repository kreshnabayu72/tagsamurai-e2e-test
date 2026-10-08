---
id: TC-AC-ACAL-E2E-040-snapshot-immutability-historis-log
title: "Integritas Data — Snapshot immutability data historis log terhadap mutasi nama master data"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-240
coverage:
  web: automated
---

# Integritas Data — Snapshot immutability data historis log terhadap mutasi nama master data

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat entri log lama di Tab User Action yang mencatat aksi oleh user `"Ahmad Dahlan"` pada object Partner `"Mitra Sentosa"`

## Test Steps

1. Buka menu `Admin Console > Settings > User` (atau modul Partner)
2. Ubah nama user `"Ahmad Dahlan"` menjadi `"Ahmad Dahlan Perkasa"`
3. Buka menu `Admin Console > Activity Log` > klik tab `"User Action"`
4. Cari entri log transaksi lama yang dibuat sebelum perubahan nama
5. Verifikasi kolom Modified By pada entri log lama TETAP tertulis `"Ahmad Dahlan"` (snapshot immutability historis terjaga, tidak berubah secara retroaktif)
6. Verifikasi entri log baru yang mencatat aksi pengubahan nama user menampilkan nama baru sesuai waktu kejadian

## Notes

- Riwayat audit trail harus bersifat immutable (snapshot) untuk keperluan audit compliance hukum dan forensik digital.

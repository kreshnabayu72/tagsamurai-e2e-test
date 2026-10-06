---
id: TC-AC-SU-E2E-007-user-list-filter-date-range-dan-format-general-settings
title: "Filter rentang tanggal Last Updated dan Temporary Until serta kepatuhan format General Settings"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-271
  - TC-AC-SU-273
  - TC-AC-SU-285
coverage:
  web: automated
---

# Filter rentang tanggal Last Updated dan Temporary Until serta kepatuhan format General Settings

## Prerequisites

- Login sebagai Role: Principal Total Control
- Format tanggal General Settings terkonfigurasi (contoh: `DD/MM/YYYY`)
- Terdapat data pengguna dengan variasi tanggal Last Updated dan Temporary Until

## Test Steps

### Filter Rentang Tanggal Last Updated

1. Buka Filter Panel di halaman User List
2. Pilih rentang tanggal pada date-range picker field `Last Updated` (Start Date dan End Date)
3. Klik `[Apply]`
4. Verifikasi tabel hanya menampilkan pengguna yang memiliki tanggal modifikasi terakhir di dalam rentang tanggal terpilih

### Filter Rentang Tanggal Temporary Until dan Kepatuhan Format

1. Buka kembali Filter Panel
2. Pilih rentang tanggal pada field `Temporary Until`
3. Klik `[Apply]`
4. Verifikasi tabel hanya menampilkan pengguna Temporary User dengan batas tanggal di dalam rentang tersebut
5. Amati teks tanggal yang tampil pada kolom tabel dan di dalam input Filter Panel
6. Verifikasi seluruh string tanggal terformat presisi mengikuti format General Settings (`DD/MM/YYYY`)

## Notes

- Format tanggal mengikuti konfigurasi terpusat di General Settings.

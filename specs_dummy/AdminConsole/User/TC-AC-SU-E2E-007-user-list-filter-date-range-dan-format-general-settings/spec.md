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

- Login sebagai Role: Total Control
- Pengaturan General Settings entitas memiliki format tanggal `DD/MM/YYYY`
- Data pengguna memiliki rentang tanggal Last Updated dan Temporary Until yang bervariasi

## Test Steps

### Filter Rentang Tanggal Last Updated
1. Buka halaman `Settings > User` dan buka Filter Panel
2. Pada field `Last Updated`, buka date range picker
3. Pilih tanggal awal (Start Date) dan tanggal akhir (End Date) yang mencakup 7 hari terakhir
4. Klik tombol `[Apply]`
5. Verifikasi hanya pengguna yang diperbarui dalam rentang tanggal tersebut yang ditampilkan di tabel

### Filter Rentang Tanggal Temporary Until
6. Buka kembali Filter Panel
7. Pada field `Temporary Until`, tentukan rentang tanggal masa aktif temporary user
8. Klik tombol `[Apply]`
9. Verifikasi hanya pengguna Temporary User dengan tanggal kedaluwarsa di dalam rentang yang tampil di tabel

### Verifikasi Kepatuhan Format Tanggal General Settings
10. Amati representasi teks tanggal pada kolom `Last Updated` di tabel
11. Verifikasi format tampilan tanggal mengikuti pola yang dikonfigurasi di General Settings (contoh: `DD/MM/YYYY HH:mm`)
12. Amati representasi tanggal pada date picker Filter Panel dan verifikasi format konsisten lintas seluruh permukaan

## Notes

- Filter rentang tanggal bersifat inklusif (mencakup start date dan end date).

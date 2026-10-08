---
id: TC-AC-SU-E2E-006-user-list-filter-panel-multi-select-dan-dropdown-populate
title: "Filter Panel User List, multi-select searchable, populate dropdown dinamis, dan enum hardcode"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-15
  - TC-AC-SU-16
  - TC-AC-SU-17
  - TC-AC-SU-18
  - TC-AC-SU-226
  - TC-AC-SU-269
  - TC-AC-SU-270
  - TC-AC-SU-272
coverage:
  web: automated
---

# Filter Panel User List, multi-select searchable, populate dropdown dinamis, dan enum hardcode

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat data pengguna dengan variasi Position, Division, Status, Role, User Type, Activation, Modified By, dan Temporary User

## Test Steps

### Screening Struktur Filter Panel dan Opsi Dropdown

1. Buka halaman User List dan klik tombol `[Filter]` di toolbar
2. Verifikasi Filter Panel terbuka memuat field: `Position`, `Division`, `Status`, `Role`, `User Type`, `Activation`, `Modified By`, `Last Updated`, `Temporary User`, `Temporary Until`
3. Buka dropdown filter `Position` dan `Division`, verifikasi opsi dropdown terpopulasi secara dinamis dari nilai DISTINCT yang tercatat pada pengguna aktif entitas ini
4. Buka dropdown filter `User Type` dan `Status`, verifikasi opsi dropdown memuat daftar enum hardcode baku (`Total Control`, `Read Only`, `Group Manager`, `Admin`, `Basic` / `Active`, `Inactive`)
5. Buka dropdown filter `Role`, verifikasi hanya nama role yang berlaku untuk entitas login (Global + Group) yang tampil

### Pengujian Multi-Select dan Logika OR Antar Pilihan

1. Pilih 2 opsi pada filter `Position` (contoh: Position A dan Position B)
2. Pilih 2 opsi pada filter `Status` (`Active` dan `Inactive`)
3. Pilih opsi `Group Manager` pada filter `User Type` (meskipun kolom User Type sedang hidden via Setup Column)
4. Pilih 2 nilai pada filter `Activation` (`Activated` dan `Pending Activation`)
5. Pilih 2 opsi pada filter `Modified By` dan pilih `Yes` + `No` pada filter `Temporary User`
6. Klik tombol `[Apply]`
7. Verifikasi tabel User List menampilkan irisan data yang memenuhi seluruh kriteria filter (logika OR di dalam satu field multi-select, logika AND antar field berbeda)

## Notes

- Filter Panel mendukung multi-select searchable sesuai konvensi GAP-213 dan GAP-219.

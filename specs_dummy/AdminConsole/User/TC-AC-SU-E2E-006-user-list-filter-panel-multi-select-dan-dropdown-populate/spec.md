---
id: TC-AC-SU-E2E-006-user-list-filter-panel-multi-select-dan-dropdown-populate
title: "Filter Panel User List, multi-select searchable, populate dropdown dinamis, dan enum hardcode"
priority: High
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

- Login sebagai Role: Total Control
- Terdapat pengguna dengan ragam Position, Division, Status portal, Role aktif, Modified By, User Type, Activation, dan Temporary User

## Test Steps

### Buka Filter Panel & Verifikasi Opsi Dropdown
1. Buka halaman `Settings > User` dan klik tombol `[Filter]` pada toolbar
2. Verifikasi Filter Panel terbuka menampilkan field: `Status`, `Role`, `Position`, `Division`, `Modified By`, `Last Updated`, `User Type`, `Activation`, `Temporary User`, `Temporary Until`
3. Buka dropdown `Position` dan `Division`
4. Verifikasi opsi yang muncul diisi secara dinamis (*populate DISTINCT*) hanya dari nilai yang genuinely tercatat pada pengguna Admin Console entitas ini
5. Buka dropdown `User Type`
6. Verifikasi opsi berisi enum hardcoded kanonikal: `Total Control`, `Read Only`, `Group Manager`, `Admin`, `Basic`
7. Buka dropdown `Role` dan verifikasi hanya memuat nama role yang berlaku untuk entitas login (Global + Group)

### Penerapan Multi-Select Filter (Logika OR dalam 1 Field)
8. Pada field `Position`, pilih 2 nilai berbeda (contoh: `"Staff"` dan `"Supervisor"`)
9. Klik tombol `[Apply]`
10. Verifikasi tabel menampilkan pengguna yang memiliki salah satu dari kedua posisi tersebut (logika OR internal field)
11. Buka kembali Filter Panel, pilih 2 opsi pada field `Status` (misal: `Active` dan `Inactive`), lalu klik `[Apply]`
12. Verifikasi hasil saringan menampilkan pengguna berstatus Active atau Inactive
13. Pilih 2 opsi pada field `Activation` (contoh: `"Activated"` dan `"Pending Activation"`)
14. Klik `[Apply]` dan verifikasi pengguna dengan status aktivasi terpilih tampil, bahkan jika kolom Activation Status di tabel masih dalam keadaan tersembunyi (curated hidden)
15. Buka kembali Filter Panel, pilih `"Yes"` dan `"No"` pada field `Temporary User`, lalu klik `[Apply]`
16. Verifikasi serikat pilihan Yes+No menampilkan seluruh pengguna tanpa error
17. Buka field `Modified By`, pilih 2 modifier berbeda, dan verifikasi tabel tersaring sesuai kedua modifier tersebut

## Notes

- Filter tetap berfungsi penuh meskipun kolom yang bersangkutan sedang disembunyikan via Setup Column.

---
id: TC-AC-SG-E2E-023-create-subgroup-entry-point-dan-path-display
title: "Pembuatan subgroup sukses via row action dan sidebar serta verifikasi display parent path"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-41
  - TC-AC-SG-42
  - TC-AC-SG-43
  - TC-AC-SG-44
coverage:
  web: automated
---

# Pembuatan subgroup sukses via row action dan sidebar serta verifikasi display parent path

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia node target `"Region A"`

## Test Steps

### Add Subgroup via Row Action Tabel
1. Buka `Settings > Group`
2. Klik row action elipsis `[⋯]` pada baris `"Region A"` di tabel lalu klik `[+ Add Subgroup]`
3. Verifikasi modal yang terbuka memiliki judul polos `"Add Subgroup"`
4. Verifikasi di bawah judul modal terdapat teks penunjuk parent `"Under: Region A"`
5. Isi Group Name dengan `"Branch 3"` lalu klik `[Submit]`
6. Verifikasi toast sukses `"Success, group has been created."` tampil
7. Verifikasi `"Branch 3"` terdaftar sebagai child di bawah Region A
### Add Subgroup via Sidebar Elipsis
8. Klik elipsis `[⋯]` pada node `"Region A"` di sidebar lalu klik `[+ Add Subgroup]`
9. Verifikasi judul `"Add Subgroup"` dan teks `"Under: Region A"` tampil identik
10. Isi Group Name dengan `"Branch 4"` lalu submit
11. Verifikasi `"Branch 4"` berhasil dibuat dengan parent_id Region A

## Notes

- TC-AC-SG-48 (race condition database insert) dicakup pada pengujian backend.

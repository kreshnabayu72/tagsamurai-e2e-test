---
id: TC-GS-POS-E2E-007-role-matrix-visibilitas-tab-dan-kontrol
title: "Role Matrix: Visibilitas tab Position dan kontrol UI per capability Manage user and role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-25
  - TC-GS-POS-26
  - TC-GS-POS-27
  - TC-GS-POS-28
  - TC-GS-POS-29
  - TC-GS-POS-30
  - TC-GS-POS-31
  - TC-GS-POS-36
coverage:
  web: automated
---

# Role Matrix: Visibilitas tab Position dan kontrol UI per capability Manage user and role

## Prerequisites

- Akun aktor pre-setup No. 1 s.d. 8 telah disiapkan:
  | Role / Akun | Capability Manage user and role |
  |---|---|
  | Total Control | C, R, U, D |
  | Read Only | R (Access Level) |
  | No Capability | None |
  | R-Only | R |
  | C+R | C, R |
  | U+R | U, R |
  | D+R | D, R |

## Test Steps

### Role Matrix UI Visibility

1. Login sebagai Total Control, buka tab Position:
   - Verifikasi tab Position tampil
   - Verifikasi tombol "[+ Position]" tampil
   - Verifikasi menu baris ⋯ memuat aksi "Edit" dan "Delete"
   - Verifikasi checkbox baris dan header tampil

2. Login sebagai Read Only, buka tab Position:
   - Verifikasi tab Position tampil read-only
   - Verifikasi tombol "[+ Position]" tersembunyi
   - Verifikasi menu baris ⋯ tidak memuat aksi edit/delete (atau menu ditiadakan)
   - Verifikasi kolom checkbox ditiadakan

3. Login sebagai No Capability (tanpa akses Manage user and role):
   - Verifikasi sub-tab "Position" tersembunyi dari navigasi
   - Buka URL langsung tab Position, verifikasi diarahkan ke 403 Forbidden atau landing default

4. Login sebagai R-Only:
   - Verifikasi tab Position tampil dengan kontrol edit/create tersembunyi

5. Login sebagai C+R:
   - Verifikasi tombol "[+ Position]" tampil aktif
   - Verifikasi menu baris tidak memuat Edit maupun Delete

6. Login sebagai U+R:
   - Verifikasi tombol "[+ Position]" tersembunyi
   - Verifikasi menu baris memuat opsi "Edit", opsi "Delete" tidak tampil

7. Login sebagai D+R:
   - Verifikasi tombol "[+ Position]" tersembunyi
   - Verifikasi menu baris memuat opsi "Delete", checkbox seleksi aktif untuk bulk delete

## Notes

- Menggabungkan TC-GS-POS-25 sampai 31 dan 36 dalam Role Matrix terpadu per konvensi 3a.

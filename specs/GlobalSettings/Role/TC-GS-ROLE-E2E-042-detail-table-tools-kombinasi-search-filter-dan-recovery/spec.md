---
id: TC-GS-ROLE-E2E-042-detail-table-tools-kombinasi-search-filter-dan-recovery
title: "Kombinasi Search dan Filter pada Halaman Detail Serta Pemulihan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-155
  - TC-GS-ROLE-156
  - TC-GS-ROLE-157
  - TC-GS-ROLE-158
  - TC-GS-ROLE-159
  - TC-GS-ROLE-160
  - TC-GS-ROLE-161
  - TC-GS-ROLE-162
  - TC-GS-ROLE-163
coverage:
  web: automated
---

# Kombinasi Search dan Filter pada Halaman Detail Serta Pemulihan Empty State

## Prerequisites

- Login sebagai Role: Total Control
- Data user ter-assign di Detail role

## Test Steps

1. Buka Tab System > Detail role 'Manage user and role'
2. Masukkan kata kunci pada Search box dan terapkan filter pada Filter Panel secara bersamaan
3. Verifikasi tabel Detail menampilkan data yang memenuhi kedua kriteria tersebut secara presisi
4. Hapus filter via tombol [Clear All] pada Filter Panel dan verifikasi kriteria pencarian tetap aktif
5. Lakukan pengurutan (sort) saat kriteria pencarian aktif dan verifikasi data terurut dalam batas hasil pencarian
6. Ketik kata kunci yang tidak cocok dengan user mana pun sehingga memicu no-result state
7. Verifikasi ilustrasi kosong "No results found" tampil di halaman Detail
8. Klik tombol [Clear Search/Filter] pada tampilan no-result
9. Verifikasi tabel Detail kembali menampilkan seluruh daftar user assignment

## Notes

- Pengujian kombinasi dan pemulihan memastikan keandalan navigasi data assignment pada halaman Detail (role.md §9.8).

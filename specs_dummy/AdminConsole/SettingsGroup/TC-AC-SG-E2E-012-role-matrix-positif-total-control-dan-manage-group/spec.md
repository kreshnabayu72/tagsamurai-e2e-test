---
id: TC-AC-SG-E2E-012-role-matrix-positif-total-control-dan-manage-group
title: "Role Matrix Positif: Akses penuh seluruh tree untuk Total Control, Default User, dan Manage group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-18
  - TC-AC-SG-25
coverage:
  web: automated
---

# Role Matrix Positif: Akses penuh seluruh tree untuk Total Control, Default User, dan Manage group

## Prerequisites

- Tersedia akun dengan Role yang diuji: Total Control, Default User, dan Global Role Manage group (C/U/D lengkap)
- Tersedia data tree multi-level dengan node level 1 dan subgroup

## Test Steps

### Pengujian Akses Penuh per Role
1. Lakukan pengujian berikut secara berurutan untuk setiap aktor (Total Control, Default User, Manage group):
2. Login sebagai aktor dan buka menu `Settings > Group`
3. Verifikasi tombol `[+ New Group]` di sidebar berstatus Show dan enabled
4. Verifikasi kolom Checkbox untuk seleksi massal di tabel berstatus Show dan dapat dicentang
5. Verifikasi tombol elipsis `[⋯]` pada baris tabel dan sidebar berstatus Show di seluruh level (termasuk level 1)
6. Buka menu elipsis pada baris level 1 dan subgroup, verifikasi opsi `+ Add Subgroup`, `Edit`, dan `Delete` seluruhnya tampil dan dapat diakses

## Notes

- Akses Global Role Manage group berlaku seragam entity-wide ke seluruh tree termasuk level 1 (ACSG-LOGIC-01).

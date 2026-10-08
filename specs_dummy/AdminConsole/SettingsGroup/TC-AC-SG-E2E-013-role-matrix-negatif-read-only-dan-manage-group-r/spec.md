---
id: TC-AC-SG-E2E-013-role-matrix-negatif-read-only-dan-manage-group-r
title: "Role Matrix Negatif: Penolakan mutasi dan elipsis tersembunyi untuk Read Only dan Manage group R-only"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-19
  - TC-AC-SG-179
coverage:
  web: automated
---

# Role Matrix Negatif: Penolakan mutasi dan elipsis tersembunyi untuk Read Only dan Manage group R-only

## Prerequisites

- Tersedia akun Role Read Only (`access_level = Read Only`)
- Tersedia akun Manage group dengan izin Read-only saja (`can_read=true`, `can_create=can_update=can_delete=false`)

## Test Steps

### Pengujian Zero Mutation Rights
1. Lakukan pengujian berikut untuk masing-masing aktor (Read Only dan Manage group R-only):
2. Login sebagai aktor dan buka `Settings > Group`
3. Verifikasi seluruh pohon grup dapat dilihat secara utuh di sidebar dan tabel (view only)
4. Verifikasi tombol `[+ New Group]` pada sidebar berstatus Hidden (tidak dirender)
5. Verifikasi kolom Checkbox seleksi massal pada tabel utama berstatus Hidden (tidak dirender)
6. Verifikasi tombol elipsis `[⋯]` pada seluruh baris tabel dan pada seluruh node sidebar berstatus Hidden total di seluruh tree (ACSG-LOGIC-06)

## Notes

- Karena tidak ada wewenang mutasi di node mana pun, tombol elipsis disembunyikan total (Hidden), bukan Disabled.

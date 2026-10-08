---
id: TC-AC-SG-E2E-015-role-matrix-granular-visibilitas-checkbox-bulk
title: "Visibilitas kolom Checkbox bulk select berdasarkan kepemilikan capability Delete"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-27
  - TC-AC-SG-156
  - TC-AC-SG-157
coverage:
  web: automated
---

# Visibilitas kolom Checkbox bulk select berdasarkan kepemilikan capability Delete

## Prerequisites

- Aktor A: Manage group dengan capability Delete aktif (`can_delete = true`)
- Aktor B: Manage group tanpa capability Delete (hanya Create/Update aktif, `can_delete = false`)

## Test Steps

### Checkbox Bulk Show Saat Memiliki Delete
1. Login sebagai Aktor A dan buka `Settings > Group`
2. Verifikasi kolom Checkbox bulk select berstatus Show dan enabled pada seluruh baris tabel (level 1 maupun subgroup)
3. Verifikasi checkbox dapat dicentang secara normal
### Checkbox Bulk Hidden Saat Tanpa Delete
4. Login sebagai Aktor B dan buka `Settings > Group`
5. Verifikasi kolom Checkbox bulk select TIDAK DIRENDER (Hidden total) di seluruh tabel
6. Verifikasi tombol elipsis `[⋯]` tetap Show untuk aksi yang diizinkan (Create/Update)

## Notes

- Checkbox bulk select hanya memiliki 2 state: Enabled atau Tidak Dirender (Hidden), seragam entity-wide.

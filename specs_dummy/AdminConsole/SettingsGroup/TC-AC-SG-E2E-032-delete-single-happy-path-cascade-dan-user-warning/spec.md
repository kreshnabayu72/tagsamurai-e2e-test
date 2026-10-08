---
id: TC-AC-SG-E2E-032-delete-single-happy-path-cascade-dan-user-warning
title: "Eksekusi Delete Single sukses dengan cascade subtree dan peringatan pelepasan user"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-60
  - TC-AC-SG-61
  - TC-AC-SG-62
  - TC-AC-SG-63
coverage:
  web: automated
---

# Eksekusi Delete Single sukses dengan cascade subtree dan peringatan pelepasan user

## Prerequisites

- Login sebagai Role: Total Control
- Node parent `"Region Multi"` memiliki 2 subgroup (`"Branch A"`, `"Branch B"`), Total Member = 0, dan terdapat user ter-assign (Total User ≥ 1)

## Test Steps

### Peringatan User Ter-assign (Kondisi #3)
1. Klik row action `[Delete]` pada baris `"Region Multi"`
2. Verifikasi dialog warning `"Delete Group"` muncul
3. Verifikasi teks dialog menampilkan: `"This group has [N] user(s) assigned — deleting it will remove their group assignments. This action cannot be undone. Are you sure you want to delete it?"` dengan tombol `[Cancel]` dan `[Delete]`
### Konfirmasi & Cascade Subtree
4. Klik tombol `[Delete]` pada dialog
5. Verifikasi toast sukses `"Success, group has been deleted."` tampil
6. Verifikasi `"Region Multi"` beserta kedua subgroupnya (`"Branch A"` dan `"Branch B"`) seluruhnya hilang dari tabel utama dan sidebar tree
7. Verifikasi penugasan role pada user terkait telah dilepas otomatis tanpa error
8. Buka Changelog dan verifikasi tercatat 3 entri penghapusan (1 entri per group di subtree)

## Notes

- Delete selalu cascade ke seluruh turunan tanpa opsi include/exclude (ACSG-LOGIC-02).
- TC-AC-SG-64, 66, 67 dicakup di level pengujian backend.

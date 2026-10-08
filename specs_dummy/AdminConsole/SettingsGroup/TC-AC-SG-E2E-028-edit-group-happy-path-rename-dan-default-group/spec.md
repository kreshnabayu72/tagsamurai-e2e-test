---
id: TC-AC-SG-E2E-028-edit-group-happy-path-rename-dan-default-group
title: "Pengubahan nama group sukses (termasuk Default Group) dan retensi referensi sistem"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-49
  - TC-AC-SG-51
coverage:
  web: automated
---

# Pengubahan nama group sukses (termasuk Default Group) dan retensi referensi sistem

## Prerequisites

- Login sebagai Role: Total Control
- Node `"Region A"` dan data seed awal `"Default Group"`

## Test Steps

### Rename Group Biasa
1. Buka modal `[Edit]` pada `"Region A"`
2. Ubah nama menjadi `"Region A Update"` lalu klik `[Save]`
3. Verifikasi toast sukses `"Success, group has been updated."` tampil
4. Verifikasi nama baru `"Region A Update"` tercermin di tabel utama dan sidebar tree
5. Verifikasi referensi relasi id tetap utuh
### Rename Data Seed Awal (Default Group)
6. Buka modal `[Edit]` pada baris `"Default Group"`
7. Ubah nama menjadi `"Headquarters Main"` lalu klik `[Save]`
8. Verifikasi toast sukses `"Success, group has been updated."` tampil
9. Verifikasi Default Group berhasil direname seperti group biasa tanpa hambatan penguncian

## Notes

- TC-AC-SG-54 (race Edit vs Edit simultan) diselesaikan di level backend (last write wins).

---
id: TC-GS-ACTLOG-E2E-036-tab-user-action-pola-entri-non-crud-relasi-dan-import-bulk
title: "Tab User Action: Pola Entri Non-CRUD Relasi User, System Role, Status, dan Import Bulk"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-145
  - TC-GS-ACTLOG-146
  - TC-GS-ACTLOG-147
  - TC-GS-ACTLOG-148
  - TC-GS-ACTLOG-149
coverage:
  web: automated
---

# Tab User Action: Pola Entri Non-CRUD Relasi User, System Role, Status, dan Import Bulk

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat aksi relasi User (Pair/Unpair TAG, Assign/Unassign Handheld, Add/Remove Access)
- Terdapat aksi edit permission System Role, Activate/Deactivate user, dan Import massal

## Test Steps

### Relasi Tambah & Pasang
1. Buka Tab User Action, cari entri Action 'Pair TAG', verifikasi tercatat dengan Object 'User'.
2. Cari entri 'Assign Handheld', verifikasi tercatat di bawah Object 'User'.
3. Cari entri 'Add Access', verifikasi tercatat penambahan hak akses produk.
### Perubahan Permission & Status Pengguna
4. Cari entri Action 'Edit' pada Object 'System Role', verifikasi perubahan permission dari Inactive menjadi Active tercatat di Old/New Value.
5. Cari entri Action 'Activate' dan 'Deactivate' pada Object 'User', verifikasi perubahan status tercatat.
### Relasi Lepas & Cabut
6. Cari entri Action 'Unpair TAG', verifikasi tercatat pelepasan TAG.
7. Cari entri 'Unassign Handheld', verifikasi tercatat pelepasan reader handheld.
8. Cari entri 'Remove Access', verifikasi pencabutan akses produk tercatat.
### Aksi Massal Import
9. Cari entri Action 'Import' hasil dari import data massal.
10. Verifikasi kolom Name menampilkan tanda '—' untuk aksi massal.

## Notes

- Aksi non-CRUD mencatat relasi antar-entitas secara terperinci sesuai log modul produsen.

---
id: TC-GS-ACTLOG-E2E-035-tab-user-action-pola-entri-crud-dan-multi-field-edit
title: "Tab User Action: Pola Entri CRUD (Create, Edit, Delete) dan Multi-Field Edit dalam Satu Simpan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-141
  - TC-GS-ACTLOG-142
  - TC-GS-ACTLOG-143
  - TC-GS-ACTLOG-144
coverage:
  web: automated
---

# Tab User Action: Pola Entri CRUD (Create, Edit, Delete) dan Multi-Field Edit dalam Satu Simpan

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat aksi Create User 'John Doe', Edit User 'Siti Nurbaya' (Division), Delete Brand 'Acme'
- Aksi simpan multi-field pada General Settings (Currency, Timezone, Date Format)

## Test Steps

### Verifikasi Entri Create
1. Buka Tab User Action, cari entri Action 'Create' dengan Object 'User' dan Name 'John Doe'.
2. Verifikasi kolom Old Value menampilkan tanda '—'.
3. Verifikasi kolom New Value memuat data user baru dan kolom Modified By memuat nama admin.
### Verifikasi Entri Edit
4. Cari entri Action 'Edit' dengan Object 'User' dan Name 'Siti Nurbaya'.
5. Verifikasi kolom Field menampilkan 'Division', Old Value menampilkan 'Marketing', New Value menampilkan 'Finance'.
### Verifikasi Entri Delete
6. Cari entri Action 'Delete' dengan Object 'Brand' dan Name 'Acme'.
7. Verifikasi kolom New Value menampilkan tanda '—' dan Old Value memuat data sebelum dihapus.
### Multi-Field Edit dalam Satu Transaksi Simpan
8. Cari entri dengan Object 'General Settings' pada waktu perubahan Currency, Timezone, dan Date Format dilakukan.
9. Verifikasi sistem mencatat tepat 3 baris terpisah (satu baris per field yang berubah).
10. Verifikasi ketiga baris tersebut memiliki timestamp Date identik.

## Notes

- Setiap field yang berubah dicatat sebagai baris mutasi atomik terpisah untuk transparansi audit.

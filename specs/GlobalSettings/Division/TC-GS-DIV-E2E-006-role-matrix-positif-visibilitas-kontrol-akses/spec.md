---
id: TC-GS-DIV-E2E-006-role-matrix-positif-visibilitas-kontrol-akses
title: "Role Matrix Positif: Total Control dan Pemegang Capability CRUD"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-07
  - TC-GS-DIV-09
  - TC-GS-DIV-10
  - TC-GS-DIV-11
  - TC-GS-DIV-12
coverage:
  web: automated
---

# Role Matrix Positif: Total Control dan Pemegang Capability CRUD

## Prerequisites

- Tersedia akun dengan peran: Total Control, Manage User Role Full CRUD, Create-Only, Update-Only, dan Delete-Only

## Test Steps

1. Login sebagai pengguna dengan Role: Total Control
2. Buka menu Global Settings > User > tab Division
3. Verifikasi tombol '[+ Division]' tampil dan aktif, checkbox seleksi baris tampil, dan menu row action (⋯) memuat opsi 'Edit' dan 'Delete'
4. Login sebagai pengguna dengan Capability: Manage User Role (Full CRUD)
5. Buka tab Division dan verifikasi tombol '[+ Division]', checkbox baris, serta opsi row action 'Edit' dan 'Delete' seluruhnya tampil aktif
6. Login sebagai pengguna dengan Capability: Create-Only
7. Buka tab Division dan verifikasi tombol '[+ Division]' tampil aktif, sedangkan checkbox seleksi dan row action (⋯) tidak menampilkan opsi Delete atau Edit
8. Login sebagai pengguna dengan Capability: Update-Only
9. Buka tab Division dan verifikasi tombol '[+ Division]' tersembunyi, checkbox baris tersembunyi, dan row action (⋯) hanya memuat opsi 'Edit'
10. Login sebagai pengguna dengan Capability: Delete-Only
11. Buka tab Division dan verifikasi tombol '[+ Division]' tersembunyi, checkbox baris tampil aktif, dan row action (⋯) hanya memuat opsi 'Delete'

## Notes

- Matriks kontrol UI mengikuti aturan pemetaan capability division.md §4.8.

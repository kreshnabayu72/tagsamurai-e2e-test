---
id: TC-GS-ROLE-E2E-006-role-matrix-positif-total-control-dan-capability-holder
title: "Role Matrix Positif: Visibilitas Kontrol dan Hak Akses Penuh Total Control serta Update Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-10
  - TC-GS-ROLE-12
  - TC-GS-ROLE-354
coverage:
  web: automated
---

# Role Matrix Positif: Visibilitas Kontrol dan Hak Akses Penuh Total Control serta Update Role

## Prerequisites

- Tersedia akun aktor Total Control: totalControl2@qwertysystem.net
- Tersedia akun aktor pemegang role Manage user and role (Update): manageUserRoleUpdate@qwertysystem.net
- Tersedia akun aktor pemegang role Manage user and role (Read-only): manageUserRoleRead@qwertysystem.net
- Tersedia user target reguler di halaman Detail

## Test Steps

1. Login sebagai akun totalControl2
2. Buka menu Global Settings > Role & Permission
3. Verifikasi semua tab (Total Control, Read Only, System) dapat diakses penuh
4. Verifikasi tombol [+ Assign] tampil dan aktif pada Tab Total Control dan Read Only
5. Buka Tab System dan masuk ke Detail role 'Manage master reference'
6. Verifikasi checkbox CRUD dan tombol [+ Assign] aktif, serta row action [⋯] Remove tersedia
7. Logout dan login sebagai akun manageUserRoleUpdate
8. Buka Global Settings > Role & Permission > Tab System > Detail role 'Manage master reference'
9. Verifikasi checkbox CRUD untuk target user reguler aktif dan dapat diubah
10. Ubah checkbox Create pada user target reguler dan verifikasi toast "Success, permissions have been updated."
11. Logout dan login sebagai akun manageUserRoleRead
12. Buka Global Settings > Role & Permission
13. Verifikasi aktor dengan kapabilitas Read-only dapat melihat seluruh data tab dan Detail secara read-only tanpa kontrol edit

## Notes

- Aktor dengan capability Manage user and role Read-only memiliki hak melihat seluruh konfigurasi role (role.md §4.8, §2.3).

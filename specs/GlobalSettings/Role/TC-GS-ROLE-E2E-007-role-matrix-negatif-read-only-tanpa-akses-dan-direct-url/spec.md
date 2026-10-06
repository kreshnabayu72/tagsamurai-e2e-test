---
id: TC-GS-ROLE-E2E-007-role-matrix-negatif-read-only-tanpa-akses-dan-direct-url
title: "Role Matrix Negatif: Hak Akses Read Only, Menu Tersembunyi No Role, dan Direct URL 403"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-11
  - TC-GS-ROLE-13
  - TC-GS-ROLE-101
  - TC-GS-ROLE-104
coverage:
  web: automated
---

# Role Matrix Negatif: Hak Akses Read Only, Menu Tersembunyi No Role, dan Direct URL 403

## Prerequisites

- Tersedia akun aktor Read Only: readOnlyGlobalSettings@qwertysystem.net
- Tersedia akun aktor No Role: noRoleGlobalSettings@qwertysystem.net

## Test Steps

1. Login sebagai akun readOnlyGlobalSettings
2. Buka menu Global Settings > Role & Permission
3. Verifikasi data pada Tab Total Control, Read Only, dan System dapat dilihat secara utuh
4. Verifikasi tombol [+ Assign] tersembunyi (Hidden) pada Tab Total Control dan Read Only
5. Verifikasi row action [⋯] Remove tersembunyi (Hidden) pada seluruh tabel
6. Buka Tab System dan masuk ke Detail salah satu role
7. Verifikasi seluruh checkbox CRUD berada dalam status Disabled dengan tooltip "Read Only access cannot modify data."
8. Logout dan login sebagai akun noRoleGlobalSettings
9. Verifikasi menu 'Role & Permission' tidak muncul di navigasi sidebar Global Settings
10. Coba buka URL langsung /global-settings/roles
11. Verifikasi sistem menolak akses dengan respons 403 Forbidden atau mengarahkan ke halaman fallback tanpa izin

## Notes

- User Read Only dapat melihat seluruh data tetapi semua aksi mutasi disembunyikan atau dinonaktifkan (role.md §4.8).

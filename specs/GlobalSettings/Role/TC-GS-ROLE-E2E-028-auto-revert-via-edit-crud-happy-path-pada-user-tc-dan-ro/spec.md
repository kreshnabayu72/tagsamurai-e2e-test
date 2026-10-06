---
id: TC-GS-ROLE-E2E-028-auto-revert-via-edit-crud-happy-path-pada-user-tc-dan-ro
title: "Eksekusi Auto-Revert Sukses via Edit CRUD: Pelepasan Access Level Menjadi Null dan Preservasi Sisa Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-54
  - TC-GS-ROLE-55
  - TC-GS-ROLE-56
  - TC-GS-ROLE-57
  - TC-GS-ROLE-70
coverage:
  web: automated
---

# Eksekusi Auto-Revert Sukses via Edit CRUD: Pelepasan Access Level Menjadi Null dan Preservasi Sisa Role

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia Siti Rahmawati (Total Control) dan Budi Hartono (Read Only) ter-assign pada role sistem

## Test Steps

1. Buka Tab System > Detail role 'Manage user and role'
2. Uncheck checkbox Create pada baris Siti Rahmawati
3. Pada dialog konfirmasi Auto-Revert, klik tombol [Continue]
4. Verifikasi toast sukses spesifik muncul: "Success, permissions have been updated. Siti Rahmawati is no longer Total Control."
5. Buka Tab Total Control dan verifikasi Siti Rahmawati langsung hilang dari daftar Total Control (access_level menjadi null)
6. Buka halaman Detail untuk kelima role sistem lainnya
7. Verifikasi seluruh hak akses individual Siti Rahmawati pada kelima role tersebut tetap utuh dan tidak ter-reset
8. Buka Detail role 'Manage user and role' dan centang Create pada baris Budi Hartono (Read Only)
9. Pada dialog konfirmasi Auto-Revert, klik tombol [Continue]
10. Verifikasi toast sukses muncul: "Success, permissions have been updated. Budi Hartono is no longer Read Only."
11. Buka Tab Read Only dan verifikasi Budi Hartono hilang dari daftar Read Only

## Notes

- Auto-Revert melepaskan access_level tanpa mereset konfigurasi role lainnya di database (role.md §9.2 [F-ROLE-06]).

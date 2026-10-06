---
id: TC-GS-ROLE-E2E-053-sinkronisasi-dua-arah-tab-role-detail-user-dan-format-datetime
title: "Sinkronisasi Dua Arah dengan Tab Role pada Modul User Serta Konsistensi Format Tanggal dan Waktu"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-102
  - TC-GS-ROLE-103
  - TC-GS-ROLE-105
coverage:
  web: automated
---

# Sinkronisasi Dua Arah dengan Tab Role pada Modul User Serta Konsistensi Format Tanggal dan Waktu

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia user target Doni Pratama

## Test Steps

1. Buka Tab System > Detail role 'Manage TAG'
2. Ubah checkbox Update pada baris Doni Pratama menjadi tercentang
3. Buka menu Global Settings > User > buka Detail user Doni Pratama > Tab Role
4. Verifikasi pada Tab Role Detail User, hak akses role Manage TAG tercentang Update secara sinkron dua arah
5. Buka form Edit User untuk Doni Pratama dan hilangkan centang akses "Global Settings"
6. Simpan perubahan form User
7. Buka kembali Global Settings > Role & Permission > Tab System > Detail role 'Manage TAG'
8. Verifikasi Doni Pratama otomatis terhapus dari daftar assignment role
9. Verifikasi bahwa perubahan hak akses berlaku pada request berikutnya dan tidak membatalkan token yang sedang aktif secara surut

## Notes

- Tabel user_system_roles menjadi sumber kebenaran bersama antara modul Role & Permission dan Detail User Tab Role (role.md §9.7).

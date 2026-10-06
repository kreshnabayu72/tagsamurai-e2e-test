---
id: TC-GS-ROLE-E2E-029-auto-revert-via-remove-role-assignment-single-pada-user-tc-dan-ro
title: "Eksekusi Auto-Revert Sukses via Remove Baris Role Tunggal pada User Total Control dan Read Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-58
  - TC-GS-ROLE-59
  - TC-GS-ROLE-60
  - TC-GS-ROLE-68
coverage:
  web: automated
---

# Eksekusi Auto-Revert Sukses via Remove Baris Role Tunggal pada User Total Control dan Read Only

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia user target berstatus Total Control ter-assign pada Detail role Manage files

## Test Steps

1. Buka Tab System > Detail role 'Manage files'
2. Cari baris user berstatus Total Control
3. Klik row action [⋯] lalu pilih 'Remove'
4. Verifikasi dialog konfirmasi yang muncul identik dengan dialog Auto-Revert (memperingatkan pelepasan status Total Control) dengan tombol [Cancel] dan [Continue]
5. Klik tombol [Continue]
6. Verifikasi toast sukses muncul dan baris user tersebut terhapus dari role 'Manage files'
7. Buka Tab Total Control dan verifikasi user tersebut telah hilang dari daftar Total Control
8. Buka Detail kelima role lainnya dan verifikasi hak akses user pada role lainnya tetap dipertahankan

## Notes

- Menghapus baris role individual dari user TC/RO juga memicu Auto-Revert yang melepaskan access_level dalam transaksi yang sama (role.md §3).

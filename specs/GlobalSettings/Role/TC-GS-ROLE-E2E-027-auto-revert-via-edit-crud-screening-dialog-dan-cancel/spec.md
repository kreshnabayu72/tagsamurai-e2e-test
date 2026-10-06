---
id: TC-GS-ROLE-E2E-027-auto-revert-via-edit-crud-screening-dialog-dan-cancel
title: "Screening Dialog Konfirmasi Auto-Revert Saat Mengedit CRUD User Total Control / Read Only dan Pembatalan Cancel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-52
  - TC-GS-ROLE-53
coverage:
  web: automated
---

# Screening Dialog Konfirmasi Auto-Revert Saat Mengedit CRUD User Total Control / Read Only dan Pembatalan Cancel

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia target user Siti Rahmawati berstatus Total Control di Detail role Manage user and role

## Test Steps

1. Buka Tab System > Detail role 'Manage user and role'
2. Cari baris Siti Rahmawati yang saat ini berstatus Total Control
3. Klik checkbox Create untuk meng-uncheck hak akses tersebut sehingga menyimpang dari pattern Total Control
4. Verifikasi dialog konfirmasi Auto-Revert otomatis muncul dengan bullet nama: "• Siti Rahmawati"
5. Verifikasi deskripsi dialog memuat: "Modifying individual permissions will remove Total Control from this user. Are you sure you want to continue?"
6. Verifikasi dialog menyediakan tombol [Cancel] dan tombol [Continue]
7. Klik tombol [Cancel] pada dialog konfirmasi
8. Verifikasi dialog tertutup, checkbox Create kembali tercentang (revert), dan status Total Control Siti Rahmawati tidak berubah

## Notes

- Menyunting hak akses individual user TC/RO hingga menyimpang dari pola tier wajib memicu konfirmasi peringatan Auto-Revert (ROLE-LOGIC-04).

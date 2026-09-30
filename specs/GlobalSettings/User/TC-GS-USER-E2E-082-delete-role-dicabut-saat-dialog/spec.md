---
id: TC-GS-USER-E2E-082-delete-role-dicabut-saat-dialog
title: 'Delete ditolak saat role aktor dicabut ketika dialog masih terbuka'
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-452
coverage:
  web: automated
---

# Delete ditolak saat role aktor dicabut ketika dialog masih terbuka

## Prerequisites

- Sesi pertama: aktor dengan role "Manage user and role" Full CRUD, bukan Total Control
- Sesi kedua dengan akun Total Control biasa (`totalControl2_automated_qaTeam1`)
- User "Target Hapus" ada
- Spec ini mencabut role aktor, jadi role dipulihkan oleh seeding sebelum run berikutnya

## Test Steps

1. Di sesi pertama, klik row action `Delete` pada baris "Target Hapus" dan biarkan dialog konfirmasi terbuka
2. Di sesi kedua, cabut role "Manage user and role" dari aktor sesi pertama
3. Di sesi pertama, klik `[Delete]` di dialog konfirmasi
4. Verifikasi dialog tertutup dan toast "You don't have permission to do this." muncul
5. Verifikasi elemen yang aktor tidak lagi berhak (mis. row action `Delete`) tidak tampil setelah UI di-refresh
6. Verifikasi "Target Hapus" masih ada di User List (dilihat dari sesi kedua)

## Notes

- Sumber `user.md` bagian 4.1 dan `error-handling-convention.md` (403: toast error, tanpa redirect, UI di-refresh).
- Cara mencabut role aktor dari sesi lain disediakan tim FE di tahap script.

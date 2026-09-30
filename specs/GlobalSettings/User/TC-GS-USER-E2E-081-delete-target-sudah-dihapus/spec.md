---
id: TC-GS-USER-E2E-081-delete-target-sudah-dihapus
title: 'Delete user yang sudah dihapus admin lain saat dialog masih terbuka'
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-451
coverage:
  web: automated
---

# Delete user yang sudah dihapus admin lain saat dialog masih terbuka

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client, sesi pertama
- Sesi kedua dengan akun Total Control lain di entity yang sama
- User "Target Hapus" ada dan tidak punya data yang menghalangi Delete
- Spec ini menghapus "Target Hapus", jadi datanya dibuat ulang oleh seeding sebelum run berikutnya. Jalankan bersama spec Delete lain di akhir, tidak paralel

## Test Steps

1. Di sesi pertama, klik row action `Delete` pada baris "Target Hapus" dan biarkan dialog konfirmasi terbuka
2. Di sesi kedua, hapus "Target Hapus" dan konfirmasi
3. Di sesi pertama, klik `[Delete]` di dialog konfirmasi
4. Verifikasi dialog tertutup otomatis, toast "This user is no longer available." muncul, dan baris "Target Hapus" hilang dari User List setelah refresh

## Notes

- Sumber `user.md` bagian 4.1, 7, dan `foundation/process/prd-process/error-handling-convention.md` (404: toast netral dan refresh).
- Dialog tertutup otomatis karena premis dialog sudah tidak valid, berbeda dari kasus 5xx yang dialognya tetap terbuka.

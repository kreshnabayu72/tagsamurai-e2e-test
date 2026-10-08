---
id: TC-GS-USER-E2E-066-custom-field-inline-edit-race
title: 'Custom Field yang dinonaktifkan admin lain saat inline-edit terbuka hilang setelah Save'
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-121
coverage:
  web: automated
---

# Custom Field yang dinonaktifkan admin lain saat inline-edit terbuka hilang setelah Save

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client, sesi pertama
- Sesi kedua dengan akun Total Control lain di entity yang sama, membuka daftar Custom Field User
- User "Budi Santoso" dengan Custom Field aktif `Golongan Darah` yang value-nya boleh diubah
- Spec ini menonaktifkan Custom Field `Golongan Darah`, jadi datanya dibuat ulang oleh seeding sebelum run berikutnya. Jalankan sendirian karena Custom Field berlaku untuk semua user

## Test Steps

1. Di sesi pertama, buka User Detail "Budi Santoso", expand Section Custom Fields, lalu klik ikon `Edit2Line` pada `Golongan Darah` dan ubah value
2. Di sesi kedua, nonaktifkan Custom Field `Golongan Darah`
3. Di sesi pertama, klik `[✓ Save]`
4. Verifikasi Save tidak berhasil (tidak ada toast sukses), lalu Section Custom Fields dimuat ulang dan `Golongan Darah` tidak lagi dirender
5. Verifikasi field lain di Section Custom Fields tidak berubah

## Notes

- Sumber `user.md` bagian 4.3. TC sumber (`TC-GS-USER-121`) menyebut respons `404 field_not_found`. Kode itu tidak ada di `user.md`, jadi spec hanya memverifikasi perilaku terlihat di FE. Respons server diverifikasi di lapisan BE.
- Kebutuhan dua sesi dan pemicu penonaktifan field ditentukan tim FE di tahap script.

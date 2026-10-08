---
id: TC-GS-USER-E2E-062-tab-non-login-reverse-lookup
title: 'Tab Non-Login User di Detail Login User menampilkan Non-Login User yang diwakilinya'
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-108
  - TC-GS-USER-109
  - TC-GS-USER-560
  - TC-GS-USER-561
  - TC-GS-USER-562
  - TC-GS-USER-565
coverage:
  web: automated
---

# Tab Non-Login User di Detail Login User menampilkan Non-Login User yang diwakilinya

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User Login "Ahmad Fauzi" adalah Represented By untuk Non-Login "Rudi Hartono" (Position `Staff`, Division `Finance`, Employee ID `EMP-002`, Active) dan "Sari Dewi" (Employee ID kosong, Inactive)
- Non-Login milik user Login lain, dan satu Non-Login "Tomi Terhapus" yang sudah di-Delete dan sebelumnya diwakili "Ahmad Fauzi"
- User Login "Doni Pratama" tidak mewakili Non-Login mana pun
- Spec ini menambah satu Non-Login untuk "Ahmad Fauzi" di langkah akhir. Datanya dibuat ulang oleh seeding sebelum run berikutnya

## Test Steps

### Isi dan kolom

1. Buka User Detail "Ahmad Fauzi" > Tab Non-Login User
2. Verifikasi hanya "Rudi Hartono" dan "Sari Dewi" yang tampil, tanpa Non-Login milik user lain dan tanpa "Tomi Terhapus"
3. Verifikasi kolom default: Name (avatar dan nama lengkap), Email, Employee ID (`—` bila kosong), Position (`—` bila kosong), Division, Active (badge, bukan switch), Last Update, dengan urutan default Name A-Z
4. Buka Column Visibility dan verifikasi kolom Temporary User, Temporary Until, dan Custom Field aktif tersedia dengan status default Hidden, lalu aktifkan kolom tersebut

### Read-only dan navigasi

5. Verifikasi toolbar hanya Search, Filter, Download (tanpa ikon Changelog dan tanpa tombol tambah Non-Login User), serta tidak ada kolom Actions, checkbox, atau toggle
6. Klik area baris selain nama "Rudi Hartono" dan verifikasi tidak terjadi apa pun
7. Klik nama "Rudi Hartono"
8. Verifikasi navigasi ke Detail Non-Login User "Rudi Hartono" dan verifikasi Tab Non-Login User tidak dirender di halaman itu

### Empty state

9. Buka User Detail "Doni Pratama" > Tab Non-Login User
10. Verifikasi empty state "No non-login users represented" dengan deskripsi "This user does not represent any non-login users."

### Badge count

11. Buka kembali User Detail "Ahmad Fauzi" dan verifikasi label tab "Non-Login User (2)" tanpa menghitung yang sudah di-Delete
12. Buat satu Non-Login baru dengan Represented By "Ahmad Fauzi" lewat modul Non-Login User, lalu buka ulang User Detail "Ahmad Fauzi"
13. Verifikasi label tab menjadi "Non-Login User (3)"

## Notes

- Sumber `user.md` bagian 4.1, 4.2, 4.2a, 7, dan 9.2 ([F-USER-15]). Pencarian, filter, sort, dan download tab ini dicakup `TC-GS-USER-E2E-063-tab-non-login-toolbar`.
- Tab Non-Login User hanya muncul di Detail Login User dan tidak dirender di Detail Non-Login User (`user_type=non_login`).
- Membuat Non-Login memakai form modul Non-Login User. Pengisian form itu dicakup spec modul tersebut, jadi di sini cukup hasilnya.

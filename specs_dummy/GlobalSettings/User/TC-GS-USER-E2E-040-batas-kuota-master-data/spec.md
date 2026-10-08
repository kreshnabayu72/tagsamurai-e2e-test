---
id: TC-GS-USER-E2E-040-batas-kuota-master-data
title: Pembuatan user diblokir saat Master Data Count Limit tercapai
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-255
  - TC-GS-USER-23
  - TC-GS-USER-87
  - TC-GS-USER-402
coverage:
  web: automated
---

# Pembuatan user diblokir saat Master Data Count Limit tercapai

## Prerequisites

- Login sebagai Role: Total Control, entity Client. Sesi kedua dengan akun Total Control lain di entity yang sama untuk langkah 15 sampai 18
- Master Data Count Limit entity ini dikecilkan lewat Admin Console > Plans & Licensing > Lifecycle Settings > tab System Limits (default 10.000), sehingga limit mudah dicapai. Nilai N ditentukan tim FE
- Jumlah `users` (Login dan Non-Login) saat spec dimulai tepat N-1 (sisa kuota tinggal 1)
- Spec ini harus dijalankan paling akhir dan sendirian, karena membuat entity penuh di batas N. Sesudahnya limit dikembalikan ke nilai semula dan user hasil spec ini dihapus
- User seeding "Umar Cadangan" ada dan boleh dihapus oleh spec ini untuk membebaskan satu slot (langkah 14)
- Pemicu kondisi hampir bersamaan untuk dua aktor pada langkah 15 sampai 18 disediakan tim FE

## Test Steps

### Slot terakhir dan sesudahnya dalam satu sesi modal

1. Klik `[+ User]` untuk membuka modal Create
2. Centang "Stay on this form after submitting"
3. Isi user "Final Allowed User" dengan semua field wajib lengkap lalu klik `[Submit]`
4. Verifikasi toast "User created successfully." muncul, baris masuk tabel di latar belakang, dan form ter-reset sementara popup tetap terbuka
5. Isi user "Exceed Limit User" dengan semua field wajib lengkap lalu klik `[Submit]`
6. Verifikasi Dialog Blok muncul di dalam popup yang masih terbuka dengan judul "Limit Reached", isi "You've reached the user limit for this workspace.", dan tombol tunggal `[OK]`, dan "Exceed Limit User" tidak tersimpan
7. Klik `[OK]` lalu klik `✕` untuk menutup modal

### Klik [+ User] saat sudah di batas

8. Klik `[+ User]`
9. Verifikasi tombol `[+ User]` tetap aktif (tidak Disabled) dan Dialog Blok "Limit Reached" dengan isi "You've reached the user limit for this workspace." muncul, bukan toast
10. Verifikasi modal Create tidak terbuka
11. Klik `[OK]`

### Dua aktor berebut slot terakhir

12. Di sesi pertama, buka User Detail "Umar Cadangan"
13. Klik `Delete` pada baris "Umar Cadangan" di User List, lalu konfirmasi
14. Verifikasi jumlah `users` kembali N-1 (sisa kuota tinggal 1)
15. Di sesi pertama dan sesi kedua, buka modal Create terpisah dan isi data valid yang berbeda: "Race User A" dan "Race User B" tanpa duplikat satu sama lain
16. Klik `[Submit]` di kedua sesi hampir bersamaan
17. Verifikasi salah satu berhasil dengan toast "User created successfully." dan yang lain ditolak dengan Dialog Blok "Limit Reached" yang sama dengan langkah 6
18. Verifikasi hanya satu dari "Race User A" dan "Race User B" yang ada di User List, dan pesan penolakan bukan pesan duplikat atau validasi lain

## Notes

- Spec ini dipisah dari alur Create biasa karena butuh entity yang jumlah usernya berada di ambang limit (prinsip 12 di `docs/e2e-conventions.md` bagian 3).
- Limit dihitung gabungan Login dan Non-Login (PRD `user.md` bagian 9.10). Skenario `TC-GS-USER-23` dan `87` sama, sehingga digabung di langkah 8 sampai 11. Sumber TC-23 menyebut "limit lisensi" dan hasil ambigu, sudah diselaraskan ke PRD pada 2026-09-30.
- Copy Dialog Blok mengikuti PRD `user.md` bagian 9.4.2 baris Create D2 (`GAP-278` sudah ditutup): satu pesan untuk Login dan Non-Login User, pola sama dengan Position.
- Selection Limit (1.000 baris, `Bulk Action Checkbox Limit`) ada di tab System Limits yang sama dan dicakup di section 9 (`TC-GS-USER-176`, `393`, `410`).
- Cara mengecilkan limit dan mengembalikannya setelah run diputuskan tim FE di tahap script.

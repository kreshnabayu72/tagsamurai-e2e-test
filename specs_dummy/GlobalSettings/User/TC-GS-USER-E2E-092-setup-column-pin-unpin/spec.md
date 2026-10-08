---
id: TC-GS-USER-E2E-092-setup-column-pin-unpin
title: 'Setup Column User List: pin dan unpin kolom'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-291
  - TC-GS-USER-292
  - TC-GS-USER-293
  - TC-GS-USER-294
  - TC-GS-USER-295
  - TC-GS-USER-296
  - TC-GS-USER-297
  - TC-GS-USER-298
  - TC-GS-USER-299
  - TC-GS-USER-301
  - TC-GS-USER-302
  - TC-GS-USER-303
  - TC-GS-USER-304
coverage:
  web: automated
---

# Setup Column User List: pin dan unpin kolom

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Data User List mock dengan sedikitnya 15 baris supaya tabel bisa di-scroll ke samping
- Konfigurasi kolom disimpan di browser per user, jadi setiap spec Setup Column dimulai dari konfigurasi default

## Test Steps

1. Aktifkan keempat kolom Curated lalu klik ikon Pin pada baris `Active` dan `Access` di popup modal Setup Column
2. Klik `[Save]` dan scroll tabel ke samping
3. Verifikasi kolom `Active` dan `Access` membeku di posisinya saat tabel di-scroll dan kolom lain bergeser
4. Refresh halaman
5. Verifikasi kedua kolom masih membeku
6. Buka popup modal, klik ikon Pin pada `Access` untuk melepas, lalu `[Save]`
7. Verifikasi `Access` ikut bergeser saat di-scroll sedangkan `Active` tetap membeku
8. Buka popup modal, klik `[Reset to Default]`, lalu `[Save]` untuk mengembalikan konfigurasi

## Notes

- Sumber `user.md` bagian 4.2a dan `prd-conventions.md` bagian 9.3. Dua kolom mewakili semua kolom Hideable dan Curated karena perilaku pin sama.

---
id: TC-GS-USER-E2E-091-setup-column-urutan-kolom
title: 'Setup Column User List: ubah urutan kolom dengan drag'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-276
  - TC-GS-USER-277
  - TC-GS-USER-278
  - TC-GS-USER-279
  - TC-GS-USER-280
  - TC-GS-USER-281
  - TC-GS-USER-282
  - TC-GS-USER-283
  - TC-GS-USER-284
  - TC-GS-USER-286
  - TC-GS-USER-287
  - TC-GS-USER-288
  - TC-GS-USER-289
  - TC-GS-USER-130
coverage:
  web: automated
---

# Setup Column User List: ubah urutan kolom dengan drag

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Data User List mock dengan sedikitnya 15 baris supaya tabel bisa di-scroll ke samping
- Konfigurasi kolom disimpan di browser per user, jadi setiap spec Setup Column dimulai dari konfigurasi default

## Test Steps

1. Aktifkan keempat kolom Curated lewat popup modal Setup Column
2. Drag baris `Division` ke posisi paling atas
3. Verifikasi urutan di Live Preview dan tabel asli menempatkan `Division` sebagai kolom pertama
4. Drag baris `Active` ke posisi paling bawah
5. Verifikasi `Active` menjadi kolom terakhir
6. Drag baris Curated `TAG` ke posisi kedua
7. Verifikasi `TAG` berada di posisi kedua
8. Klik `[Save]` lalu refresh halaman
9. Verifikasi urutan kolom di tabel sama seperti langkah 3, 5, dan 7
10. Buka popup modal, klik `[Reset to Default]`, lalu `[Save]` untuk mengembalikan konfigurasi

## Notes

- Sumber `user.md` bagian 4.2a dan `prd-conventions.md` bagian 9.3. Tiga contoh drag mewakili kolom Hideable dan Curated. Perilaku drag sama untuk 13 kolom.

---
id: TC-GS-USER-E2E-090-setup-column-hide-unhide-kolom
title: 'Setup Column User List: sembunyikan dan munculkan kolom serta minimal satu kolom tetap terlihat'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-261
  - TC-GS-USER-262
  - TC-GS-USER-263
  - TC-GS-USER-264
  - TC-GS-USER-265
  - TC-GS-USER-266
  - TC-GS-USER-267
  - TC-GS-USER-268
  - TC-GS-USER-269
  - TC-GS-USER-271
  - TC-GS-USER-272
  - TC-GS-USER-273
  - TC-GS-USER-274
coverage:
  web: automated
---

# Setup Column User List: sembunyikan dan munculkan kolom serta minimal satu kolom tetap terlihat

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Data User List mock dengan sedikitnya 15 baris supaya tabel bisa di-scroll ke samping
- Konfigurasi kolom disimpan di browser per user, jadi setiap spec Setup Column dimulai dari konfigurasi default

## Test Steps

1. Buka popup modal Setup Column lalu hapus centang delapan kolom Hideable selain `Name`: `Active`, `Email`, `Position`, `Division`, `Access`, `Employee ID`, `Modified By`, `Last Update`
2. Verifikasi Live Preview dan tabel asli hanya menyisakan kolom `Name` dan kedelapan kolom itu hilang satu per satu setiap dicentang
3. Verifikasi checkbox `Name` Disabled dengan tooltip "At least one column must remain visible."
4. Centang kembali `Position`
5. Verifikasi checkbox `Name` kembali aktif dan kolom `Position` muncul di Live Preview
6. Centang keempat kolom Curated: `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`
7. Verifikasi keempat kolom muncul di Live Preview dan tabel asli
8. Klik `[Save]` lalu refresh halaman
9. Verifikasi hanya kolom `Name`, `Position`, dan keempat kolom Curated yang tampil, dan konfigurasi tetap ada setelah refresh
10. Buka popup modal, klik `[Reset to Default]`, lalu `[Save]` untuk mengembalikan konfigurasi

## Notes

- Sumber `user.md` bagian 4.2a dan `prd-conventions.md` bagian 9.3 (guard minimal satu kolom terlihat). Satu spec memverifikasi semua 13 kolom karena perilaku ceklis identik untuk tiap kolom.
- Tooltip diambil dari TC sumber `TC-GS-USER-262`.

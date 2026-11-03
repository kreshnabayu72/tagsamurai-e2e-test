---
id: TC-FA-RP-E2E-173-tab-system-search-setup-column-download-dan-state-1
title: "Tab System: Search, Setup Column, Download, dan state (1/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-577
  - TC-FA-RP-578
  - TC-FA-RP-579
  - TC-FA-RP-580
coverage:
  web: automated
---

# Tab System: Search, Setup Column, Download, dan state (1/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #39 (Detail Role Group Role `Manage files` terisi; Global Role `Manage Open API` dan `Manage accounting` terisi; Tab System memuat 9 Global Role dan 7 Group Role). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- State yang diubah: tidak ada (Search dikosongkan pada langkah 22 dan overlay Column Visibility ditutup pada langkah 35).

## Test Steps

### Search per kolom Role Name dan Users (TC-FA-RP-577)

1. Klik Tab `System`
2. Klik ikon Search
3. Ketik Search `OPEN`, tekan Enter
4. Verifikasi kolom Role Name: baris `Manage Open API` pada section Global Role tampil
5. Verifikasi section Group Role menampilkan empty state `No results found`
6. Catat angka Users pada baris `Manage Open API` (salin dari sel)
7. Ganti isi kotak search dengan angka Users yang dicatat, tekan Enter
8. Verifikasi kolom Users: baris `Manage Open API` tampil
9. Verifikasi setiap baris lain yang tampil memuat angka itu pada kolom Users
10. Klik ikon `(←)` pada kotak Search

### Siklus interaksi Search toolbar (TC-FA-RP-578)

11. Hover ikon Search
12. Verifikasi tooltip `Search`
13. Klik ikon Search
14. Verifikasi kotak Search melebar dan kursor otomatis fokus di input
15. Ketik `files` tanpa menekan Enter
16. Verifikasi tabel belum tersaring (seluruh baris tampil)
17. Tekan Enter
18. Verifikasi hanya baris `Manage files` pada section Group Role yang tampil
19. Klik ikon `(✕)` pada kotak Search
20. Verifikasi input kosong
21. Verifikasi tabel tetap tersaring
22. Tekan Enter pada input kosong
23. Verifikasi seluruh baris kembali tampil

### Tab System tanpa Filter Panel dan tanpa sort (TC-FA-RP-579)

24. Verifikasi toolbar hanya memuat `Search | Download | Changelog`
25. Verifikasi tidak ada ikon Filter pada toolbar
26. Verifikasi header Role Name dan Users tidak memiliki ikon sort
27. Catat urutan baris section Global Role dan section Group Role
28. Klik header Role Name
29. Klik header Users
30. Verifikasi klik header tidak mengubah urutan baris

### Overlay Column Visibility (TC-FA-RP-580)

31. Klik header `(⋯)` kolom Column Visibility
32. Verifikasi overlay memuat item `Setup Column...` di bagian bawah
33. Verifikasi kolom bawaan tampil tercentang aktif: `Role Name`, `Users`
34. Verifikasi drag handle tersedia pada daftar
35. Tutup overlay dengan Esc

## Notes

- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab dan ikon Search (langkah 1, 2, 13); mencatat angka dan urutan (langkah 6, 27); mengganti isi Search (langkah 7); menutup kotak Search dengan `(←)` (langkah 10); klik header (langkah 28, 29); menutup overlay (langkah 35).
- Langkah 19 sampai 23 memetakan Expected d dan e TC-FA-RP-578; state Search dikosongkan sebelum TC-FA-RP-579 oleh langkah 22.
- Asersi "hanya baris X" menyebut nama baris yang tampil sehingga baris itu sendiri menjadi anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-RP-577 Expected b ("bersama baris lain yang Users-nya memuat angka itu") tidak menyebut baris lain yang diharapkan; spec mengasersi bahwa setiap baris lain yang tampil memuat angka itu pada kolom Users (langkah 9) tanpa daftar baris.
  - TC-FA-RP-577 tidak menyebut apakah hasil Search pada section Group Role untuk angka Users juga ditampilkan; spec tidak mengasersi section Group Role pada langkah 7 sampai 9.
  - TC-FA-RP-578 Expected c menyebut hanya baris `Manage files` pada section Group Role; spec mengasersi tidak ada baris lain pada kedua section.
  - TC-FA-RP-580 memuat Expected b untuk kolom bawaan saja; TC tidak menyebut kolom curated pada Tab System.

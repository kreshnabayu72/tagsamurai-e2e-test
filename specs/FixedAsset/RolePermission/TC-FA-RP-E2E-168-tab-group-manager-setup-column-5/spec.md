---
id: TC-FA-RP-E2E-168-tab-group-manager-setup-column-5
title: "Tab Group Manager: Setup Column (5/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-562
  - TC-FA-RP-1068
  - TC-FA-RP-1069
  - TC-FA-RP-1070
coverage:
  web: automated
---

# Tab Group Manager: Setup Column (5/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #38 (Tab Group Manager enam baris), #18 (pohon group), dan #22 (Custom Field `Cost Center`, `Joined Date`, `Badge No`). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- Tabel Kolom Custom Field (TC-FA-RP-1068, TC-FA-RP-1069, TC-FA-RP-1070): `Cost Center`, `Joined Date`, `Badge No`.

## Test Steps

### Konfigurasi kolom tidak memengaruhi tabel lain (TC-FA-RP-562)

1. Klik Tab `Group Manager`
2. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, hapus centang kolom `Division`, lalu klik `[Save]`
3. Klik Tab `Total Control`
4. Verifikasi Tab Total Control tetap memakai konfigurasi kolomnya sendiri (kolom `Division` tampil; cache per tabel)

### Ceklis dan unceklis kolom curated Custom Field (TC-FA-RP-1068)

5. Klik Tab `Group Manager`
6. Untuk setiap baris pada Tabel Kolom Custom Field, lakukan langkah 7 sampai 16
7. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
8. Centang kolom
9. Verifikasi Live Preview menampilkan kolom
10. Klik `[Save]`
11. Verifikasi tabel menampilkan kolom
12. Muat ulang halaman (F5), lalu buka kembali popup Setup Column
13. Verifikasi kolom tetap tampil pada tabel
14. Verifikasi checkbox kolom tercentang
15. Hapus centang kolom, lalu klik `[Save]`
16. Verifikasi kolom tidak tampil lagi pada tabel

### Geser urutan kolom curated Custom Field (TC-FA-RP-1069)

17. Untuk setiap baris pada Tabel Kolom Custom Field, lakukan langkah 18 sampai 25
18. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
19. Centang kolom agar tampil pada Live Preview
20. Seret kolom ke posisi paling akhir pada daftar
21. Verifikasi kolom berada di posisi paling akhir pada Live Preview
22. Klik `[Save]`
23. Verifikasi tabel memakai urutan kolom yang sama dengan Live Preview
24. Muat ulang halaman (F5)
25. Verifikasi urutan kolom tetap

### Pin dan unpin kolom curated Custom Field (TC-FA-RP-1070)

26. Untuk setiap baris pada Tabel Kolom Custom Field, lakukan langkah 27 sampai 36
27. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
28. Klik ikon Pin pada kolom
29. Verifikasi ikon Pin aktif pada Live Preview
30. Klik `[Save]`
31. Scroll tabel horizontal
32. Verifikasi kolom membeku (sticky)
33. Muat ulang halaman (F5)
34. Verifikasi kolom tetap ter-pin
35. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, klik ikon Pin kolom itu lagi, lalu klik `[Save]`
36. Verifikasi pembekuan terlepas

## Notes

- Alasan di atas 35 langkah (dengan ekspansi): langkah 7 sampai 16, 18 sampai 25, dan 27 sampai 36 adalah blok berulang dengan parameter pada Tabel Kolom Custom Field (tiga iterasi tiap blok); nominal 36 langkah, ekspansi 6 + 3 x 10 + 1 + 3 x 8 + 1 + 3 x 10 = 92. Seluruh blok berkelas fungsional sama, dataset sama (Pre-setup #38 dan #22), dan tiap iterasi berdiri sendiri karena centang atau pin dilepas di akhir iterasi. Langkah yang diulang: 7 sampai 16, 18 sampai 25, dan 27 sampai 36.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1, 3, 5); membuka popup Setup Column (langkah 7, 18, 27); langkah 19 mencentang kolom agar tampil sebelum diseret; scroll horizontal (langkah 31).
- Langkah 1 sampai 4 memakai Tab `Total Control` sebagai "tabel lain pada modul" (TC-FA-RP-562 menyebut "tab lain atau modal Changelog").
- Temuan untuk QA:
  - TC-FA-RP-1069 menyeret kolom curated Custom Field yang tersembunyi setelah TC-FA-RP-1068 ke posisi paling akhir dan menyebut posisi pada Live Preview; spec mencentang kolom sebelum diseret (langkah 19).
  - TC-FA-RP-562 tidak menyebut perubahan susunan yang disimpan; spec menyembunyikan kolom `Division` pada Tab Group Manager.

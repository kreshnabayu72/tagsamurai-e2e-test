---
id: TC-FA-TDC-E2E-021-role-matrix-gabungan-update-delete-dan-create-update
title: "Role Matrix: Gabungan Capability Update+Delete dan Create+Update"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-69
  - TC-FA-TDC-70
coverage:
  web: automated
---

# Role Matrix: Gabungan Capability Update+Delete dan Create+Update

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Update+Delete (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_UPDDEL_PASSWORD` | langkah 1 sampai 15 |
| Create+Update (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_CREUPD_PASSWORD` | langkah 16 sampai 32 |

- Login di hook `before` spec ini sebagai Update+Delete (Manage accounting); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji" belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; penulis script mendaftarkannya.
- Data (kondisi awal): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; 9 baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Hook `before` spec ini menyeed ulang kondisi itu lewat API dan hook `after` memulihkannya; Class Code dibatasi 15 karakter sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Akun tiap aktor sudah tersedia dan memiliki akses tab (Read) ke Settings > Accounting > Tax Depreciation Class.
- Kebutuhan data: NB-4 Active dan NB-OLD Inactive (seleksi); BLD-NP memiliki satu versi Scheduled. Spec ini tidak mengubah data.
- Login hook `before`: akun Update+Delete (Manage accounting) disediakan tim FE; capability gabungan disiapkan lewat perubahan capability role.
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps


### Role Update+Delete (TC-FA-TDC-69)

1. Verifikasi `+ Class` tidak dirender
2. Verifikasi `Restore default classes` tidak ada
3. Klik ikon `⋯` pada baris NB-4
4. Verifikasi menu `⋯` memuat `Edit` dan `Delete`
5. Tutup menu dengan Esc
6. Centang baris NB-4 dan NB-OLD
7. Verifikasi Bulk Action Bar memuat `Deactivate`, `Activate`, dan `Delete`
8. Hover toggle Active baris NB-OLD
9. Verifikasi toggle Active Show dan aktif
10. Klik Unselect All
11. Klik Class Code BLD-NP
12. Verifikasi Drawer BLD-NP: field dapat diubah
13. Verifikasi `[Save]` Show
14. Verifikasi tombol `Cancel scheduled version` Show
15. Tutup Drawer dengan `[×]`

### Role Create+Update (TC-FA-TDC-70)

16. Ganti akun: logout, login sebagai Create+Update (Manage accounting), lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
17. Verifikasi `+ Class` Show
18. Klik ikon `⋯` pada baris NB-4
19. Verifikasi menu `⋯` hanya memuat `Edit`
20. Verifikasi `Delete` tidak dirender
21. Tutup menu dengan Esc
22. Centang baris NB-4 dan NB-OLD
23. Verifikasi Bulk Action Bar memuat `Deactivate` dan `Activate`
24. Verifikasi `Delete` tidak ada pada Bulk Action Bar
25. Hover toggle Active baris NB-OLD
26. Verifikasi toggle Active Show dan aktif
27. Klik Unselect All
28. Klik Class Code BLD-NP
29. Verifikasi Drawer BLD-NP: field dapat diubah
30. Verifikasi `[Save]` Show
31. Verifikasi tombol `Cancel scheduled version` Show
32. Tutup Drawer dengan `[×]`

## Notes

- Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (akun pertama login di hook `before`) dan hasil kedua gabungan berbeda (bagian 3a). Spec ini matriks visibilitas gabungan capability, sehingga memuat dua polaritas (tampil dan Hidden).
- Langkah penghubung (S-03): langkah 5 dan 21 (menutup menu), langkah 15 dan 32 (menutup Drawer), langkah 10 dan 27 (Unselect All, S-09), langkah 16 (ganti akun dan membuka layar).
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - TC-69 butir a menyebut `Restore default classes` tidak ada pada tabel berisi class; tombol itu hanya muncul di Empty State, sehingga asersi ini tidak membedakan role. Spec mengasersi sesuai Expected.
  - TC-69 butir e dan TC-70 butir e menyebut "field dapat diubah" tanpa daftar field; spec mengasersi field Drawer dapat diubah sebagai satu klausa.

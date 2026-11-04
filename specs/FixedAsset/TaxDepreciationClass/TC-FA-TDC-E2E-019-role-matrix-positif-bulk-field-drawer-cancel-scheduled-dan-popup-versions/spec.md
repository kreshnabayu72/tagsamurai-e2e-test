---
id: TC-FA-TDC-E2E-019-role-matrix-positif-bulk-field-drawer-cancel-scheduled-dan-popup-versions
title: "Role Matrix Positif: Bulk Action Bar, Field Drawer Edit, Cancel Scheduled Version, dan Popup Versions"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-59
  - TC-FA-TDC-60
  - TC-FA-TDC-61
  - TC-FA-TDC-63
  - TC-FA-TDC-65
  - TC-FA-TDC-67
coverage:
  web: automated
---

# Role Matrix Positif: Bulk Action Bar, Field Drawer Edit, Cancel Scheduled Version, dan Popup Versions

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Total Control | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_TC_PASSWORD` | langkah 1 sampai 19 |
| Update-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_UPDATEONLY_PASSWORD` | langkah 20 sampai 40 |
| Delete-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_DELETEONLY_PASSWORD` | langkah 41 sampai 46 |

- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji" belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; penulis script mendaftarkannya.
- Data (kondisi awal): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; 9 baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Hook `before` spec ini menyeed ulang kondisi itu lewat API dan hook `after` memulihkannya; Class Code dibatasi 15 karakter sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Akun tiap aktor sudah tersedia dan memiliki akses tab (Read) ke Settings > Accounting > Tax Depreciation Class.
- Kebutuhan data: NB-4 Active dan NB-OLD Inactive (seleksi bulk); NB-2 tidak terkunci dan tanpa versi Scheduled (TC-FA-TDC-63); BLD-NP memiliki satu versi Scheduled Effective From Jan 2027 (tahun pajak belum dimulai), satu versi Current, dan satu versi Past (TC-FA-TDC-65 dan 67). Spec ini tidak mengubah data.
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps


### Role Total Control (TC-FA-TDC-59, 63 butir a, 65 butir a, 67 butir a)

1. Centang baris NB-4 (Active) dan NB-OLD (Inactive)
2. Verifikasi kolom checkbox Show
3. Verifikasi Bulk Action Bar memuat `Deactivate`, `Activate`, dan `Delete`
4. Klik Unselect All
5. Klik Class Code NB-2
6. Verifikasi Regulation Reference, Class Code, Class Name, Useful Life (years), dan Allowed Methods dapat diubah
7. Verifikasi Asset Type Disabled (selalu)
8. Verifikasi Straight Line Rate dan Declining Balance Rate berupa teks read-only
9. Verifikasi `[Clear Field]` dan `[Save]` Show
10. Tutup Drawer dengan `[×]`
11. Klik Class Code BLD-NP
12. Verifikasi Alert versi Scheduled tampil
13. Verifikasi tombol `Cancel scheduled version` Show
14. Klik `View versions`
15. Verifikasi kolom Action tampil
16. Verifikasi tombol `Cancel` Show hanya pada baris berstatus Scheduled
17. Verifikasi baris Current dan Past tanpa tombol
18. Tutup Popup `Versions`
19. Tutup Drawer dengan `[×]`

### Role Update-Only (TC-FA-TDC-60, 63 butir b, 65 butir b, 67 butir b)

20. Ganti akun: logout, login sebagai Update-Only (Manage accounting), lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
21. Centang baris NB-4 (Active) dan NB-OLD (Inactive)
22. Verifikasi kolom checkbox Show
23. Verifikasi Bulk Action Bar memuat `Deactivate` dan `Activate`
24. Verifikasi `Delete` tidak ada pada Bulk Action Bar
25. Klik Unselect All
26. Klik Class Code NB-2
27. Verifikasi Regulation Reference, Class Code, Class Name, Useful Life (years), dan Allowed Methods dapat diubah
28. Verifikasi Asset Type Disabled (selalu)
29. Verifikasi Straight Line Rate dan Declining Balance Rate berupa teks read-only
30. Verifikasi `[Clear Field]` dan `[Save]` Show
31. Tutup Drawer dengan `[×]`
32. Klik Class Code BLD-NP
33. Verifikasi Alert versi Scheduled tampil
34. Verifikasi tombol `Cancel scheduled version` Show
35. Klik `View versions`
36. Verifikasi kolom Action tampil
37. Verifikasi tombol `Cancel` Show hanya pada baris berstatus Scheduled
38. Verifikasi baris Current dan Past tanpa tombol
39. Tutup Popup `Versions`
40. Tutup Drawer dengan `[×]`

### Role Delete-Only (TC-FA-TDC-61)

41. Ganti akun: logout, login sebagai Delete-Only (Manage accounting), lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
42. Centang baris NB-4 (Active) dan NB-OLD (Inactive)
43. Verifikasi kolom checkbox Show
44. Verifikasi Bulk Action Bar hanya memuat `Delete`
45. Verifikasi `Deactivate` dan `Activate` tidak ada pada Bulk Action Bar
46. Klik Unselect All

## Notes

- Satu spec memuat beberapa aksi positif (Bulk Action Bar, field Drawer Edit, Cancel scheduled version, Popup Versions) karena seluruhnya Role Matrix positif atas pemegang Update/Delete dengan polaritas seragam (bagian 3a, keputusan 2026-11-02). Urutan TC diubah menjadi per blok role supaya ganti akun minimal; TC-FA-TDC-65 dan 67 dijalankan berurutan pada satu pembukaan Drawer BLD-NP per role (S-10).
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas (Role Matrix positif), berdiri sendiri per role, dan kegagalan satu role tidak membuat role lain kehilangan makna.
- Langkah penghubung (S-03): langkah 4, 25, 46 (Unselect All, S-09), langkah 10, 19, 31, 40 (menutup Drawer), langkah 18 dan 39 (menutup Popup), langkah 20 dan 41 (ganti akun dan membuka layar).
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - TC-67 menyebut baris Past tanpa Effective From tanpa nilai kolom; spec mengasersi status Scheduled/Current/Past, bukan Effective From.

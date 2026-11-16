---
id: TC-FA-TDC-E2E-016-role-matrix-positif-create-row-action-dan-toggle-active
title: "Role Matrix Positif: Tombol Create, Menu Row Action, dan Toggle Active"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-49
  - TC-FA-TDC-53
  - TC-FA-TDC-54
  - TC-FA-TDC-55
  - TC-FA-TDC-57
sourceRules: ["§4.8#r9", "§4.1#r2", "§4.2b#p1", "FLD-18", "§9.5#r7", "§4.8#r11", "§4.8#r12", "§4.1.1#p3", "§4.8#r13", "§4.8#r15", "§4.8#r14", "§3.9#r5", "FATDC-LOGIC-08h"]
smoke: []
dependsOn: []
trace:
  "§4.8#r9": [1, 18]
  "§4.1#r2": [3, 20]
  "§4.2b#p1": [3, 20]
  "FLD-18": [4, 21]
  "§9.5#r7": [4, 21]
  "§4.8#r11": [5, 22]
  "§4.8#r12": [8, 26, 38]
  "§4.1.1#p3": 9
  "§4.8#r13": [9, 27, 40]
  "§4.8#r15": [9, 28, 39]
  "§4.8#r14": [13, 32]
  "§3.9#r5": [14, 33]
  "FATDC-LOGIC-08h": [15, 34]
coverage:
  web: automated
---

# Role Matrix Positif: Tombol Create, Menu Row Action, dan Toggle Active

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Total Control | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_TC_PASSWORD` | langkah 1 sampai 16 |
| Create-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_CREATEONLY_PASSWORD` | langkah 17 sampai 23 |
| Update-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_UPDATEONLY_PASSWORD` | langkah 24 sampai 35 |
| Delete-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_DELETEONLY_PASSWORD` | langkah 36 sampai 41 |

- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji" belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; penulis script mendaftarkannya.
- Data (kondisi awal): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; 9 baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Hook `before` spec ini menyeed ulang kondisi itu lewat API dan hook `after` memulihkannya; Class Code dibatasi 15 karakter sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Akun tiap aktor sudah tersedia dan memiliki akses tab (Read) ke Settings > Accounting > Tax Depreciation Class.
- Kebutuhan data: NB-4 aktif dengan Used By 0 (target menu row action); NB-OLD berstatus Inactive (target toggle Active). Spec ini hanya membuka dialog dan menutupnya dengan `[Cancel]`; tidak ada data yang diubah.
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps


### Role Total Control (TC-FA-TDC-49 butir a, TC-FA-TDC-53, TC-FA-TDC-57 butir a)

1. Verifikasi `+ Class` Show
2. Klik `+ Class`
3. Verifikasi Drawer mode Create terbuka
4. Verifikasi checkbox `Stay on this form after submitting` tampil dan tidak dicentang
5. Verifikasi footer `[Clear Field]` dan `[Submit]` Show
6. Tutup Drawer dengan `[×]`
7. Klik ikon `⋯` pada baris NB-4
8. Verifikasi tombol `⋯` per baris Show
9. Verifikasi menu row action memuat `Edit` dan `Delete`
10. Tutup menu dengan Esc
11. Hover toggle Active baris NB-OLD
12. Klik toggle Active baris NB-OLD
13. Verifikasi toggle Active Show dan aktif
14. Verifikasi dialog `Activate Tax Depreciation Class` terbuka
15. Verifikasi toggle NB-OLD tetap Off sampai Confirm
16. Tutup dialog dengan `[Cancel]`

### Role Create-Only (TC-FA-TDC-49 butir b)

17. Ganti akun: logout, login sebagai Create-Only (Manage accounting), lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
18. Verifikasi `+ Class` Show
19. Klik `+ Class`
20. Verifikasi Drawer mode Create terbuka
21. Verifikasi checkbox `Stay on this form after submitting` tampil dan tidak dicentang
22. Verifikasi footer `[Clear Field]` dan `[Submit]` Show
23. Tutup Drawer dengan `[×]`

### Role Update-Only (TC-FA-TDC-54, TC-FA-TDC-57 butir b)

24. Ganti akun: logout, login sebagai Update-Only (Manage accounting), lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
25. Klik ikon `⋯` pada baris NB-4
26. Verifikasi tombol `⋯` per baris Show
27. Verifikasi menu row action hanya memuat `Edit`
28. Verifikasi `Delete` tidak dirender (Hidden)
29. Tutup menu dengan Esc
30. Hover toggle Active baris NB-OLD
31. Klik toggle Active baris NB-OLD
32. Verifikasi toggle Active Show dan aktif
33. Verifikasi dialog `Activate Tax Depreciation Class` terbuka
34. Verifikasi toggle NB-OLD tetap Off sampai Confirm
35. Tutup dialog dengan `[Cancel]`

### Role Delete-Only (TC-FA-TDC-55)

36. Ganti akun: logout, login sebagai Delete-Only (Manage accounting), lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
37. Klik ikon `⋯` pada baris NB-4
38. Verifikasi tombol `⋯` per baris Show
39. Verifikasi menu row action hanya memuat `Delete`
40. Verifikasi `Edit` tidak dirender (Hidden)
41. Tutup menu dengan Esc

## Notes

- Satu spec memuat beberapa aksi positif (tombol Create, menu row action, toggle Active) karena seluruhnya Role Matrix positif atas tabel yang sama dan berpolaritas seragam (bagian 3a, keputusan 2026-11-02). Urutan TC diubah menjadi per blok role supaya ganti akun minimal: TC-FA-TDC-49 dan 57 terbagi ke dua blok role, TC-FA-TDC-53, 54, dan 55 masing-masing satu blok.
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas (Role Matrix positif), berdiri sendiri per role, dan kegagalan satu role tidak membuat role lain kehilangan makna.
- Langkah penghubung (S-03): langkah 6 dan 23 (menutup Drawer), langkah 10, 29, dan 41 (menutup menu), langkah 16 dan 35 (menutup dialog), langkah 17, 24, 36 (ganti akun dan membuka layar). Dialog `Activate Tax Depreciation Class` ditutup dengan `[Cancel]` sesuai TC; tidak ada perubahan data, sehingga tidak ada pemulihan.
- Pembagian TC lintas spec: TC-FA-TDC-51 (`Restore default classes` di Empty State) ada di spec 229.
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - TC-57 menyebut toggle "aktif" tanpa cara cek selain dialog terbuka; spec mengasersi toggle Show dan aktif lalu dialog terbuka sesuai Expected.

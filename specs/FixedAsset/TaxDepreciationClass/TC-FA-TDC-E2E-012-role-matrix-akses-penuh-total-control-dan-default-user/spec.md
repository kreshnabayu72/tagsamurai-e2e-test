---
id: TC-FA-TDC-E2E-012-role-matrix-akses-penuh-total-control-dan-default-user
title: "Role Matrix: Akses Penuh Total Control dan Default User pada Tab Tax Depreciation Class"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-38
  - TC-FA-TDC-39
  - TC-FA-TDC-40
coverage:
  web: automated
---

# Role Matrix: Akses Penuh Total Control dan Default User pada Tab Tax Depreciation Class

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Total Control | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_TC_PASSWORD` | langkah 1 sampai 19 |
| Default User (Total Control permanen) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_DU_PASSWORD` | langkah 20 sampai 29 |

- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji": `FA_TC_PASSWORD` dan `FA_DU_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Data (kondisi awal): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; 9 baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Hook `before` spec ini menyeed ulang kondisi itu lewat API dan hook `after` memulihkannya; Class Code dibatasi 15 karakter sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Kebutuhan data TC-39: class NB-1 memiliki Used By 5 dan Last Posted Tax Year terisi (Class Code terkunci); NB-4 aktif dengan Used By 0. Plan company Growth.
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps


### Role Total Control (TC-FA-TDC-38, TC-FA-TDC-39)

1. Verifikasi tab `Tax Depreciation Class` tampil
2. Verifikasi data seluruh client tampil pada tabel
3. Verifikasi tombol `+ Class` tampil
4. Klik ikon `⋯` pada baris NB-4
5. Verifikasi menu row action NB-4 memuat `Edit` dan `Delete`
6. Tutup menu dengan Esc
7. Klik Class Code NB-1
8. Verifikasi Drawer NB-1 terbuka
9. Verifikasi field Drawer selain Class Code dan Asset Type dapat diubah
10. Verifikasi Class Code Disabled (terkunci karena Last Posted Tax Year terisi)
11. Verifikasi Asset Type Disabled (selalu)
12. Verifikasi `[Clear Field]` dan `[Save]` tampil
13. Tutup Drawer dengan `[×]`
14. Klik toggle Active pada baris NB-1 (Used By 5)
15. Verifikasi dialog blok tampil dengan title `Cannot Deactivate Tax Depreciation Class`
16. Verifikasi isi dialog: bullet `NB-1 – Bukan bangunan – Kelompok 1` dan teks `Used by 5 asset classes. Change them in Asset Class first.`
17. Verifikasi tombol `[OK]` tampil
18. Klik `[OK]`
19. Verifikasi toggle NB-1 tetap On setelah dialog ditutup

### Role Default User (TC-FA-TDC-40)

20. Ganti akun: logout, login sebagai Default User, lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
21. Verifikasi tab tampil dengan seluruh data client
22. Verifikasi tombol `+ Class` tampil
23. Klik ikon `⋯` pada baris NB-4
24. Verifikasi menu row action NB-4 memuat `Edit` dan `Delete`
25. Tutup menu dengan Esc
26. Klik `+ Class`
27. Verifikasi Drawer mode Create terbuka
28. Verifikasi footer Drawer memuat `[Clear Field]` dan `[Submit]`
29. Tutup Drawer dengan `[×]`

## Notes

- Satu spec memuat beberapa aksi positif (menu row action, Drawer, toggle Active, tombol Create) karena seluruhnya Role Matrix positif atas tabel yang sama dan berpolaritas seragam (bagian 3a, keputusan 2026-11-02).
- Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (akun pertama login di hook `before`); langkah tiap blok tidak identik (bagian 3a).
- Langkah penghubung (S-03): langkah 6 dan 25 (menutup menu), langkah 13 dan 29 (menutup Drawer tanpa perubahan, sehingga tanpa dialog `Unsaved Changes`), langkah 20 (ganti akun dan membuka layar).
- Pembagian TC lintas spec: Role Read Only dan Read ada di spec 013; role tanpa capability di spec 014.
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - TC-38 butir a menyebut "data seluruh client tampil" tanpa menyebut baris yang harus tampil; spec mengasersi data tabel tampil tanpa menghitung baris.

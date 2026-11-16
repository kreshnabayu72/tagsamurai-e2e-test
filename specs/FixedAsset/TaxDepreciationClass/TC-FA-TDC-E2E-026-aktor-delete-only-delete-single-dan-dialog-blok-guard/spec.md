---
id: TC-FA-TDC-E2E-026-aktor-delete-only-delete-single-dan-dialog-blok-guard
title: "Aktor Delete-Only: Delete Single dan Dialog Blok Guard"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-82
  - TC-FA-TDC-83
  - TC-FA-TDC-84
sourceRules: ["D-05", "F-FATDC-06.k2", "D-04", "F-FATDC-06.k1", "D-06", "F-FATDC-06.k6", "§[F-FATDC-06] Delete Tax Depreciation Class#b3"]
smoke: []
dependsOn: []
trace:
  "D-05": 3
  "F-FATDC-06.k2": [3, 5, 6]
  "D-04": 9
  "F-FATDC-06.k1": [9, 11, 12]
  "D-06": 15
  "F-FATDC-06.k6": [15, 18]
  "§[F-FATDC-06] Delete Tax Depreciation Class#b3": 17
coverage:
  web: automated
---

# Aktor Delete-Only: Delete Single dan Dialog Blok Guard

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Delete-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_DELETEONLY_PASSWORD` | langkah 1 sampai 18 |

- Login di hook `before` spec ini sebagai Delete-Only (Manage accounting); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji" belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; penulis script mendaftarkannya.
- Data (kondisi awal): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; 9 baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Hook `before` spec ini menyeed ulang kondisi itu lewat API dan hook `after` memulihkannya; Class Code dibatasi 15 karakter sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Akun aktor sudah tersedia dan memiliki akses tab (Read) ke Settings > Accounting > Tax Depreciation Class.
- Kebutuhan data: NB-2 dipakai 3 Asset Class dan belum pernah diposting (Guard 2, TC-FA-TDC-83); NB-KHS memiliki Last Posted Tax Year 2026 dan Used By 0 (Guard 1, TC-FA-TDC-84); NB-4 dengan Used By 0 dan belum pernah diposting (TC-FA-TDC-82). Hook `after` menyeed ulang NB-4 lewat API.
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps


### Dialog blok Guard 2 (TC-FA-TDC-83)

1. Klik ikon `⋯` pada baris NB-2
2. Klik `Delete`
3. Verifikasi dialog `Cannot Delete Tax Depreciation Class` tampil dengan bullet `NB-2 – Bukan bangunan – Kelompok 2`, teks `This class is used by 3 asset classes.`, tombol `[OK]`
4. Klik `[OK]`
5. Verifikasi tidak ada toast
6. Verifikasi baris NB-2 tetap ada

### Dialog blok Guard 1 (TC-FA-TDC-84)

7. Klik ikon `⋯` pada baris NB-KHS
8. Klik `Delete`
9. Verifikasi dialog `Cannot Delete Tax Depreciation Class` tampil dengan bullet `NB-KHS – Kelompok khusus pernah diposting`, teks `It was used for fiscal depreciation in 2026.`, tombol `[OK]`
10. Klik `[OK]`
11. Verifikasi tidak ada toast
12. Verifikasi baris NB-KHS tetap ada

### Delete class yang lolos kedua guard (TC-FA-TDC-82)

13. Klik ikon `⋯` pada baris NB-4
14. Klik `Delete`
15. Verifikasi dialog `Delete Tax Depreciation Class` tampil dengan bullet `NB-4 – Bukan bangunan – Kelompok 4`, teks `This action cannot be undone. Are you sure you want to delete it?`, tombol `[Cancel]` dan `[Delete]`
16. Klik `[Delete]`
17. Verifikasi toast sukses `Success, tax depreciation class has been deleted.`
18. Verifikasi baris NB-4 hilang dari tabel

## Notes

- Satu aktor (Delete-Only) untuk seluruh spec; login di hook `before`, tidak ada ganti akun. Urutan TC: dialog blok (TC-FA-TDC-83, 84) lebih dulu, Delete yang menghapus data (TC-FA-TDC-82) di akhir (prinsip aksi yang menghapus data di akhir).
- Absence "tidak ada toast" ditulis tepat sesudah klik `[OK]` dengan dialog blok yang baru diasersi sebagai anchor (8b.2, 8b.11); baris yang tetap ada dan baris NB-4 yang hilang memakai toast sukses sebagai anchor.
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - Post Condition TC-82, 83, dan 84 ("Class ... terhapus/tidak terhapus") tidak punya langkah observasi terpisah dari Expected; tidak diasersi di luar Expected (S-01).

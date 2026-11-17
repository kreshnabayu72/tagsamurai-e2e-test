---
id: TC-FA-TDC-E2E-229-role-matrix-positif-restore-default-classes-di-empty-state-pemegang-create
title: "Role Matrix Positif: Restore default classes di Empty State bagi Pemegang Create"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-51
sourceRules: ["ST-23", "§4.8#r10"]
smoke: []
dependsOn: []
trace:
  "ST-23": [1, 4]
  "§4.8#r10": [2, 5]
coverage:
  web: automated
---

# Role Matrix Positif: Restore default classes di Empty State bagi Pemegang Create

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Total Control | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_TC_PASSWORD` | langkah 1 sampai 2 |
| Create-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_CREATEONLY_PASSWORD` | langkah 3 sampai 5 |

- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji" belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; penulis script mendaftarkannya.
- Data (kondisi awal): tabel Tax Depreciation Class tanpa class sama sekali (seluruh class sudah dihapus lewat API), sehingga Empty State tampil. Hook `before` spec ini menyiapkan kondisi itu dan hook `after` memulihkan 7 class seed lewat API.
- Akun tiap aktor sudah tersedia dan memiliki akses tab (Read) ke Settings > Accounting > Tax Depreciation Class. Spec ini tidak mengklik `Restore default classes`; tidak ada data yang diubah selain kondisi awal di atas.
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps


### Role Total Control (TC-FA-TDC-51 butir a)

1. Verifikasi Empty State `No tax depreciation class` tampil
2. Verifikasi tombol `Restore default classes` Show

### Role Create-Only (TC-FA-TDC-51 butir b)

3. Ganti akun: logout, login sebagai Create-Only (Manage accounting), lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
4. Verifikasi Empty State `No tax depreciation class` tampil
5. Verifikasi tombol `Restore default classes` Show

## Notes

- Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (akun pertama login di hook `before`); langkah kedua blok identik (bagian 3a).
- Spec memuat satu TC pada tabel tanpa class; spec Role Matrix lain memakai tabel berisi class, sehingga TC ini ditempatkan sendiri (kondisi data berbeda, bagian 3 prinsip 12).
- Langkah penghubung (S-03): langkah 3 (ganti akun dan membuka layar).
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.

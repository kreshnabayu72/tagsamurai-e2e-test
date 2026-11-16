---
id: TC-FA-TDC-E2E-017-role-matrix-negatif-create-restore-dan-tombol-baris-tanpa-hak
title: "Role Matrix Negatif: Tombol Create, Restore default classes, dan Tombol Baris Tanpa Hak"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-50
  - TC-FA-TDC-52
  - TC-FA-TDC-56
sourceRules: ["§4.1.1#p5", "§4.8#r2", "§4.8#r9", "§4.1.1#r19", "§4.8#r12", "§4.8#r13", "§4.8#r15", "ST-23", "§4.8#r10"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#p5": 3
  "§4.8#r2": 3
  "§4.8#r9": 4
  "§4.1.1#r19": 7
  "§4.8#r12": 8
  "§4.8#r13": 9
  "§4.8#r15": 9
  "ST-23": [13, 14]
  "§4.8#r10": 14
coverage:
  web: automated
---

# Role Matrix Negatif: Tombol Create, Restore default classes, dan Tombol Baris Tanpa Hak

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Read Only | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_RO_PASSWORD` | langkah 2-4, 6-9, 12-14 (iterasi) |
| Read (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_READ_PASSWORD` | idem |
| Create-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_CREATEONLY_PASSWORD` | langkah 6-9 (iterasi) |
| Update-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_UPDATEONLY_PASSWORD` | langkah 2-4 dan 12-14 (iterasi) |
| Delete-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_DELETEONLY_PASSWORD` | langkah 2-4 dan 12-14 (iterasi) |

- Login di hook `before` spec ini sebagai Read Only; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji" belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; penulis script mendaftarkannya.
- Data (kondisi awal): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; 9 baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Hook `before` spec ini menyeed ulang kondisi itu lewat API dan hook `after` memulihkannya; Class Code dibatasi 15 karakter sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Akun tiap aktor sudah tersedia dan memiliki akses tab (Read) ke Settings > Accounting > Tax Depreciation Class.
- Tabel "Role yang diuji" per blok: TC-FA-TDC-50 dan TC-FA-TDC-52 memakai Read Only, Read, Update-Only, dan Delete-Only; TC-FA-TDC-56 memakai Read Only, Read, dan Create-Only.
- State global: blok TC-FA-TDC-52 mengosongkan seluruh class lewat API; hook `after` memulihkan 7 class seed dan 9 class Example Data lewat API.
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps


### Tombol `+ Class` (TC-FA-TDC-50)

1. Untuk setiap role Read Only, Read, Update-Only, dan Delete-Only, lakukan langkah 2 sampai 4
2. Ganti akun: logout, login sebagai role iterasi, lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
3. Verifikasi toolbar hanya `Search | Filter | Download | Changelog`
4. Verifikasi `+ Class` tidak dirender (Hidden)

### Tombol `⋯` per baris (TC-FA-TDC-56)

5. Untuk setiap role Read Only, Read, dan Create-Only, lakukan langkah 6 sampai 9
6. Ganti akun: logout, login sebagai role iterasi, lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
7. Verifikasi baris NB-4 tampil dengan Class Code `NB-4`
8. Verifikasi tombol `⋯` per baris tidak dirender (Hidden)
9. Verifikasi row action `Edit` dan `Delete` tidak ada

### Restore default classes di Empty State (TC-FA-TDC-52)

10. Kosongkan seluruh class lewat API hingga tabel tanpa class tersimpan, lalu muat ulang halaman
11. Untuk setiap role Read Only, Read, Update-Only, dan Delete-Only, lakukan langkah 12 sampai 14
12. Ganti akun: logout, login sebagai role iterasi, lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
13. Verifikasi Empty State `No tax depreciation class` dengan Description `Tax depreciation cannot be calculated.` tampil
14. Verifikasi tombol `Restore default classes` tidak dirender (Hidden)

## Notes

- Spec memuat beberapa aksi negatif (tombol Create, tombol baris, Restore default classes) karena seluruhnya Role Matrix negatif dengan polaritas seragam (bagian 3a). Tiga perulangan atas role: langkah 2 sampai 4, 6 sampai 9, dan 12 sampai 14, dengan langkah ganti akun eksplisit di awal tiap iterasi. Iterasi pertama (Read Only) mengulang login akun yang sudah aktif dari hook `before`.
- Spec melewati sekitar 35 langkah setelah ekspansi perulangan. Alasan: seluruh blok satu kelas (Role Matrix negatif), parameter iterasi hanya akun login, dan kegagalan satu role tidak membuat role lain kehilangan makna.
- Urutan TC: blok Empty State (TC-FA-TDC-52) diletakkan terakhir karena mengosongkan data; TC-FA-TDC-56 sebelum TC-FA-TDC-52 sesuai prinsip aksi yang menghapus data di akhir.
- Langkah penghubung (S-03): langkah 2, 6, 12 (ganti akun dan membuka layar), langkah mengosongkan class lewat API dan memuat ulang halaman.
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - TC-50 LK menyebut "klik `+ Class` dan amati footer Drawer" untuk aktor yang `+ Class`-nya tidak dirender; langkah itu tidak dapat dijalankan dan Expected tidak memuat asersi footer. Spec mengasersi toolbar dan `+ Class` Hidden saja.

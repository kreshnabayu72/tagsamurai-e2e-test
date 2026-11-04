---
id: TC-FA-TDC-E2E-014-role-matrix-negatif-tanpa-capability-menu-accounting-dan-url-langsung
title: "Role Matrix Negatif: Tanpa Capability Menu Accounting dan URL Langsung"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-44
  - TC-FA-TDC-45
coverage:
  web: automated
---

# Role Matrix Negatif: Tanpa Capability Menu Accounting dan URL Langsung

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Group Manager | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_GM_PASSWORD` | langkah 1 sampai 2 dan 9 sampai 13 |
| Role lain tanpa capability Manage accounting | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_NOCAP_PASSWORD` | langkah 3 sampai 8 |

- Login di hook `before` spec ini sebagai Group Manager. Spec ini membuka layar sendiri: hook `beforeEach` suite tidak membuka tab Tax Depreciation Class untuk akun tanpa capability (layar awal spec = halaman utama Fixed Asset). Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji": `FA_GM_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; `FA_NOCAP_PASSWORD` belum terdaftar di keduanya dan didaftarkan penulis script.
- Data (kondisi awal): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; 9 baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Hook `before` spec ini menyeed ulang kondisi itu lewat API dan hook `after` memulihkannya; Class Code dibatasi 15 karakter sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Plan company Growth. URL halaman tab Tax Depreciation Class diketahui dan dipakai pada TC-FA-TDC-45 (disediakan tim FE).
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps


### Group Manager dan role lain tanpa capability: menu Accounting (TC-FA-TDC-44)

1. Verifikasi sedikitnya satu item menu lain pada sidebar tampil
2. Verifikasi menu `Accounting` tidak muncul (Hidden)
3. Ganti akun: logout, lalu login sebagai Role lain tanpa capability Manage accounting
4. Verifikasi sedikitnya satu item menu lain pada sidebar tampil
5. Verifikasi menu `Accounting` tidak muncul (Hidden)

### Membuka URL tab langsung (TC-FA-TDC-45)

6. Ketik URL tab Tax Depreciation Class langsung di address bar
7. Verifikasi toast error `You don't have permission to do this.` tampil
8. Verifikasi tidak ada data tabel yang tampil
9. Ganti akun: logout, lalu login sebagai Group Manager
10. Ketik URL tab Tax Depreciation Class langsung di address bar
11. Verifikasi toast error `You don't have permission to do this.` tampil
12. Verifikasi tidak ada data tabel yang tampil
13. Verifikasi tidak ada redirect ke halaman unauthorized terpisah

## Notes

- Satu spec memuat beberapa aksi negatif (melihat menu Accounting dan membuka URL tab langsung) karena seluruhnya Role Matrix negatif atas role tanpa capability dengan polaritas seragam (bagian 3a, keputusan 2026-11-02).
- Urutan TC-FA-TDC-45 diubah dari Group Manager lalu role lain menjadi role lain lalu Group Manager supaya tidak menambah satu ganti akun; asersi tiap role berdiri sendiri. Pada langkah 7 dan 11 toast error yang sama muncul berurutan; ganti akun (langkah 9) menutup toast sebelumnya (R-12).
- Langkah penghubung (S-03): langkah 3 dan 9 (ganti akun). Langkah 1 dan 4 (item menu lain tampil) adalah anchor absence menu `Accounting` (8b.2).
- Jumlah role tanpa capability: TC menyebut "role lain tanpa capability" tanpa nama; satu akun dipakai sebagai wakil.
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - TC-44 dan TC-45 menyebut "role lain tanpa capability Manage accounting" tanpa nama role atau akun; Prerequisites menandainya disediakan tim FE.
  - TC-44 tidak menyebut item menu pembanding pada sidebar; spec mengasersi sedikitnya satu item menu lain tampil sebagai anchor.
  - TC-45 butir a untuk Group Manager menyebut "tidak ada redirect ke halaman unauthorized terpisah" sementara butir b role lain tidak menyebutnya; spec mengasersi hanya pada Group Manager sesuai TC.

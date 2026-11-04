---
id: TC-FA-TDC-E2E-020-role-matrix-negatif-alert-versi-scheduled-dan-popup-versions-tanpa-update
title: "Role Matrix Negatif: Alert Versi Scheduled dan Popup Versions tanpa Hak Update"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-66
  - TC-FA-TDC-68
coverage:
  web: automated
---

# Role Matrix Negatif: Alert Versi Scheduled dan Popup Versions tanpa Hak Update

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Read Only | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_RO_PASSWORD` | langkah 2 sampai 11 (iterasi) |
| Read (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_READ_PASSWORD` | idem |
| Create-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_CREATEONLY_PASSWORD` | idem |
| Delete-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_DELETEONLY_PASSWORD` | idem |

- Login di hook `before` spec ini sebagai Read Only; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji": `FA_RO_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; `FA_READ_PASSWORD`, `FA_CREATEONLY_PASSWORD`, dan `FA_DELETEONLY_PASSWORD` belum terdaftar di keduanya dan didaftarkan penulis script.
- Data (kondisi awal): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; 9 baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Hook `before` spec ini menyeed ulang kondisi itu lewat API dan hook `after` memulihkannya; Class Code dibatasi 15 karakter sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Akun tiap aktor sudah tersedia dan memiliki akses tab (Read) ke Settings > Accounting > Tax Depreciation Class.
- Kebutuhan data: BLD-NP memiliki satu versi Scheduled Effective From Jan 2027 (tahun pajak belum dimulai), satu versi Current, dan satu versi Past. Spec ini tidak mengubah data.
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps

1. Untuk setiap role pada tabel "Role yang diuji", lakukan langkah 2 sampai 11
2. Ganti akun: logout, login sebagai role iterasi, lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
3. Klik Class Code BLD-NP
4. Verifikasi Alert versi Scheduled tampil
5. Verifikasi tombol `Cancel scheduled version` tidak dirender (Hidden)
6. Klik `View versions`
7. Verifikasi baris berstatus Scheduled tampil pada Popup Versions
8. Verifikasi tabel Popup Versions tanpa kolom Action
9. Verifikasi tidak ada tombol `Cancel` pada baris mana pun
10. Tutup Popup `Versions`
11. Tutup Drawer dengan `[×]`

## Notes

- Satu perulangan atas empat role (langkah 2 sampai 11) dengan langkah ganti akun eksplisit di awal iterasi; langkah tiap role identik (bagian 3a, 8b butir 7). Iterasi pertama (Read Only) mengulang login akun yang sudah aktif dari hook `before`.
- Spec melewati sekitar 35 langkah setelah ekspansi perulangan: 11 langkah nominal, 41 langkah dengan empat iterasi (langkah 2 sampai 11 diulang per role). Alasan: satu topik (Role Matrix negatif untuk BLD-NP yang memiliki versi Scheduled), parameter iterasi hanya akun login, tidak ada data yang diubah sehingga tidak ada blok yang menyambung ke iterasi lain, dan kegagalan satu role tidak membuat role lain kehilangan makna.
- TC-FA-TDC-66 dan TC-FA-TDC-68 memakai pembukaan Drawer BLD-NP yang sama per role; urutan asersi mengikuti LK keduanya (Alert dan tombol lebih dulu, lalu Popup Versions) dan tidak mengulang pembukaan Drawer (S-10).
- Langkah penghubung (S-03): langkah 2 (ganti akun dan membuka layar), langkah menutup Popup `Versions` dan Drawer. Langkah "Verifikasi baris berstatus Scheduled tampil" adalah anchor untuk asersi absence kolom Action dan tombol `Cancel` (8b.2).
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.

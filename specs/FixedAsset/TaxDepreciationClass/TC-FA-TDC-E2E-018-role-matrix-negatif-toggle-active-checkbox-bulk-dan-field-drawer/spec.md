---
id: TC-FA-TDC-E2E-018-role-matrix-negatif-toggle-active-checkbox-bulk-dan-field-drawer
title: "Role Matrix Negatif: Toggle Active, Checkbox Bulk, dan Field Drawer tanpa Hak Update"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-58
  - TC-FA-TDC-62
  - TC-FA-TDC-64
sourceRules: ["FATDC-LOGIC-08i", "§4.8#b3", "§4.8#r14", "ST-29", "§3.9#r6", "§4.1.1#r2", "§4.1.1#r19", "§4.8#r16", "§4.1.1#p4", "§4.8#r7", "§4.8#r8"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-08i": 4
  "§4.8#b3": [4, 17, 19, 21, 23, 25, 27]
  "§4.8#r14": 5
  "ST-29": 5
  "§3.9#r6": 7
  "§4.1.1#r2": 10
  "§4.1.1#r19": 10
  "§4.8#r16": [11, 12]
  "§4.1.1#p4": 12
  "§4.8#r7": [17, 19, 21, 23, 25, 27]
  "§4.8#r8": 28
coverage:
  web: automated
---

# Role Matrix Negatif: Toggle Active, Checkbox Bulk, dan Field Drawer tanpa Hak Update

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Read Only | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_RO_PASSWORD` | langkah 2-7, 9-12, 14-29 (iterasi) |
| Read (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_READ_PASSWORD` | idem |
| Create-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_CREATEONLY_PASSWORD` | idem |
| Delete-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_DELETEONLY_PASSWORD` | langkah 2-7 dan 14-29 (iterasi) |

- Login di hook `before` spec ini sebagai Read Only; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji": `FA_RO_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; `FA_READ_PASSWORD`, `FA_CREATEONLY_PASSWORD`, dan `FA_DELETEONLY_PASSWORD` belum terdaftar di keduanya dan didaftarkan penulis script.
- Data (kondisi awal): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; 9 baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Hook `before` spec ini menyeed ulang kondisi itu lewat API dan hook `after` memulihkannya; Class Code dibatasi 15 karakter sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Akun tiap aktor sudah tersedia dan memiliki akses tab (Read) ke Settings > Accounting > Tax Depreciation Class.
- Tabel "Role yang diuji" per blok: TC-FA-TDC-58 dan TC-FA-TDC-64 memakai Read Only, Read, Create-Only, dan Delete-Only; TC-FA-TDC-62 memakai Read Only, Read, dan Create-Only.
- Kebutuhan data: NB-OLD berstatus Inactive (target toggle); NB-2 tidak terkunci dan tanpa versi Scheduled (target Drawer). Tidak ada data yang diubah.
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps


### Toggle Active (TC-FA-TDC-58)

1. Untuk setiap role Read Only, Read, Create-Only, dan Delete-Only, lakukan langkah 2 sampai 7
2. Ganti akun: logout, login sebagai role iterasi, lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
3. Hover toggle Active baris NB-OLD
4. Verifikasi tooltip `You don't have permission to edit.` tampil
5. Verifikasi toggle Active tetap tampil (visible) namun Disabled (non-interaktif)
6. Klik toggle Active baris NB-OLD
7. Verifikasi dialog tidak terbuka

### Kolom checkbox dan Bulk Action Bar (TC-FA-TDC-62)

8. Untuk setiap role Read Only, Read, dan Create-Only, lakukan langkah 9 sampai 12
9. Ganti akun: logout, login sebagai role iterasi, lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
10. Verifikasi header kolom Class Code dan baris NB-4 tampil
11. Verifikasi kolom checkbox di header dan baris tidak dirender (Hidden)
12. Verifikasi Bulk Action Bar tidak dapat dimunculkan

### Field Drawer mode Edit (TC-FA-TDC-64)

13. Untuk setiap role Read Only, Read, Create-Only, dan Delete-Only, lakukan langkah 14 sampai 29
14. Ganti akun: logout, login sebagai role iterasi, lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
15. Klik Class Code NB-2
16. Hover field Regulation Reference Drawer
17. Verifikasi field Regulation Reference tetap tampil namun Disabled dengan tooltip `You don't have permission to edit.`
18. Hover field Class Code Drawer
19. Verifikasi field Class Code tetap tampil namun Disabled dengan tooltip `You don't have permission to edit.`
20. Hover field Class Name Drawer
21. Verifikasi field Class Name tetap tampil namun Disabled dengan tooltip `You don't have permission to edit.`
22. Hover field Asset Type Drawer
23. Verifikasi field Asset Type tetap tampil namun Disabled dengan tooltip `You don't have permission to edit.`
24. Hover field Useful Life (years) Drawer
25. Verifikasi field Useful Life (years) tetap tampil namun Disabled dengan tooltip `You don't have permission to edit.`
26. Hover field Allowed Methods Drawer
27. Verifikasi field Allowed Methods tetap tampil namun Disabled dengan tooltip `You don't have permission to edit.`
28. Verifikasi `[Clear Field]` dan `[Save]` tidak dirender (Hidden)
29. Tutup Drawer dengan `[×]`

## Notes

- Spec memuat beberapa aksi negatif (toggle Active, checkbox bulk, field Drawer) karena seluruhnya Role Matrix negatif atas aksi Update/Delete dengan polaritas seragam (bagian 3a). Tiga perulangan atas role: langkah 2 sampai 7, 9 sampai 12, dan 14 sampai 29, dengan langkah ganti akun eksplisit di awal tiap iterasi. Iterasi pertama (Read Only) mengulang login akun yang sudah aktif dari hook `before`.
- Spec melewati sekitar 35 langkah setelah ekspansi perulangan. Alasan: seluruh blok satu kelas (Role Matrix negatif), parameter iterasi hanya akun login, dan kegagalan satu role tidak membuat role lain kehilangan makna.
- Langkah penghubung (S-03): langkah 2, 9, 14 (ganti akun dan membuka layar), langkah 29 (menutup Drawer), dan langkah 10 (Verifikasi header Class Code dan baris NB-4 tampil: anchor positif untuk asersi Hidden langkah 11-12, bukan klausa Expected TC-62).
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - TC-62 "Bulk Action Bar tidak dapat dimunculkan" tidak menyebut cara mencoba memunculkannya selain tidak adanya checkbox; spec mengasersi Bar tidak tampil sesudah checkbox terbukti tidak dirender.

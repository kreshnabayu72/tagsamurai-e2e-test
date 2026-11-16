---
id: TC-FA-TDC-E2E-015-role-matrix-visibilitas-elemen-baca-dan-drawer-baca-semua-aktor
title: "Role Matrix: Visibilitas Elemen Baca dan Drawer Baca untuk Semua Aktor"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-47
  - TC-FA-TDC-48
sourceRules: ["§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.4#r11", "§4.1.1#r3", "§5#b5", "§9.5#r3", "§4.8#r4", "§4.1.1#r16", "§4.1.1#r9", "§4.8#r5", "ST-30", "§4.8#r6", "FATDC-LOGIC-04ad", "§4.8#r20", "§4.1.6#p5"]
smoke: []
dependsOn: []
trace:
  "§4.8#r1": 5
  "§4.8#r2": 6
  "§4.8#r3": 7
  "§4.4#r11": 7
  "§4.1.1#r3": 8
  "§5#b5": 9
  "§9.5#r3": 9
  "§4.8#r4": [10, 11]
  "§4.1.1#r16": [10, 11]
  "§4.1.1#r9": 11
  "§4.8#r5": 16
  "ST-30": 17
  "§4.8#r6": 17
  "FATDC-LOGIC-04ad": 18
  "§4.8#r20": [18, 20]
  "§4.1.6#p5": 20
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Baca dan Drawer Baca untuk Semua Aktor

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Total Control | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_TC_PASSWORD` | langkah 2 sampai 12 dan 14 sampai 22 (iterasi) |
| Read Only | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_RO_PASSWORD` | idem |
| Read (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_READ_PASSWORD` | idem |
| Create-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_CREATEONLY_PASSWORD` | idem |
| Update-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_UPDATEONLY_PASSWORD` | idem |
| Delete-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_DELETEONLY_PASSWORD` | idem |

- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji" belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; penulis script mendaftarkannya.
- Data (kondisi awal): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; 9 baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Hook `before` spec ini menyeed ulang kondisi itu lewat API dan hook `after` memulihkannya; Class Code dibatasi 15 karakter sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Akun tiap aktor sudah tersedia dan memiliki akses tab (Read) ke Settings > Accounting > Tax Depreciation Class.
- Kebutuhan data TC-FA-TDC-48: class BLD-NP memiliki satu versi Scheduled dengan Effective From Jan 2027. NB-1 memiliki Used By 5 (link Used By `5`).
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps


### Elemen baca per role (TC-FA-TDC-47)

1. Untuk setiap role pada tabel "Role yang diuji", lakukan langkah 2 sampai 12
2. Ganti akun: logout, login sebagai role iterasi, lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
3. Klik header Class Name untuk sort
4. Buka Overlay Column Visibility lewat header Actions `⋯`
5. Verifikasi tab `Tax Depreciation Class` Show
6. Verifikasi Search, Filter, Download, dan Changelog Show
7. Verifikasi header Actions `⋯` Show dan membuka Overlay Column Visibility
8. Verifikasi ikon sort Class Name berfungsi
9. Verifikasi Pagination tampil
10. Verifikasi link Class Code pada NB-1 Show
11. Verifikasi link Used By `5` pada NB-1 Show
12. Tutup Overlay Column Visibility

### Drawer baca per role (TC-FA-TDC-48)

13. Untuk setiap role pada tabel "Role yang diuji", lakukan langkah 14 sampai 22
14. Ganti akun: logout, login sebagai role iterasi, lalu buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
15. Klik Class Code BLD-NP
16. Verifikasi Drawer form General Show
17. Verifikasi Alert versi Scheduled Show
18. Verifikasi tautan `View versions` Show
19. Klik `View versions`
20. Verifikasi Popup `Versions` untuk BLD-NP terbuka
21. Tutup Popup `Versions`
22. Tutup Drawer dengan `[×]`

## Notes

- Spec berisi matriks visibilitas: satu daftar elemen, enam role dengan hasil yang sama. Dua perulangan atas tabel "Role yang diuji" (langkah 2 sampai 12 untuk TC-FA-TDC-47 dan langkah 14 sampai 22 untuk TC-FA-TDC-48); langkah ganti akun eksplisit di awal tiap iterasi. Iterasi pertama (Total Control) mengulang login akun yang sudah aktif dari hook `before` supaya isi iterasi identik.
- Spec melewati sekitar 35 langkah setelah ekspansi perulangan (enam iterasi dua kali). Alasan: seluruh blok satu kelas (Role Matrix visibilitas baca), parameter iterasi hanya akun login, dan kegagalan satu role tidak membuat role lain kehilangan makna.
- Langkah penghubung (S-03): langkah 2 dan 14 (ganti akun dan membuka layar), langkah 12 (menutup Overlay), langkah menutup Popup `Versions` dan Drawer sebelum iterasi berikutnya. Klik header Class Name (langkah 3) dilakukan agar sort dapat diasersi; urutan hasil sort tidak diasersi karena TC hanya meminta ikon sort berfungsi.
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - TC-47 butir "ikon sort Class Name berfungsi" tidak menyebut urutan hasil; spec mengasersi ikon sort tampil dan dapat diklik tanpa memeriksa urutan baris.
  - TC-47 dan TC-48 tidak menyebut apakah Search/Filter diuji dengan aksi atau hanya tampil; spec mengasersi tampil (Show) sesuai Expected.

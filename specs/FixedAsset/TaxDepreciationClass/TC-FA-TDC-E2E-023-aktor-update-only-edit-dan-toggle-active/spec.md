---
id: TC-FA-TDC-E2E-023-aktor-update-only-edit-dan-toggle-active
title: "Aktor Update-Only: Edit Class dan Toggle Active"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-73
  - TC-FA-TDC-74
  - TC-FA-TDC-75
  - TC-FA-TDC-76
  - TC-FA-TDC-77
sourceRules: ["F-FATDC-02.k11a", "§[F-FATDC-02] Edit Tax Depreciation Class#b4", "T-02a", "§[F-FATDC-02] Edit Tax Depreciation Class#b6", "S-02a", "ST-06", "FATDC-LOGIC-07a", "ST-30", "D-03", "T-04", "§3.9#r5", "D-01", "§[F-FATDC-05] Deactivate Tax Depreciation Class#b3", "§3.9#r3"]
smoke: []
dependsOn: []
trace:
  "F-FATDC-02.k11a": [4, 18]
  "§[F-FATDC-02] Edit Tax Depreciation Class#b4": [4, 18]
  "T-02a": [5, 13, 19]
  "§[F-FATDC-02] Edit Tax Depreciation Class#b6": [6, 20]
  "S-02a": [7, 14]
  "ST-06": 10
  "FATDC-LOGIC-07a": 10
  "ST-30": 22
  "D-03": 25
  "T-04": 27
  "§3.9#r5": 28
  "D-01": 30
  "§[F-FATDC-05] Deactivate Tax Depreciation Class#b3": 32
  "§3.9#r3": 33
coverage:
  web: automated
---

# Aktor Update-Only: Edit Class dan Toggle Active

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Update-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_UPDATEONLY_PASSWORD` | langkah 1 sampai 33 |

- Login di hook `before` spec ini sebagai Update-Only (Manage accounting); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji" belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; penulis script mendaftarkannya.
- Data (kondisi awal): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; 9 baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Hook `before` spec ini menyeed ulang kondisi itu lewat API dan hook `after` memulihkannya; Class Code dibatasi 15 karakter sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Akun aktor sudah tersedia dan memiliki akses tab (Read) ke Settings > Accounting > Tax Depreciation Class.
- Kebutuhan data: NB-2 tidak terkunci dan tanpa versi Scheduled (TC-FA-TDC-73); NB-1 memiliki Last Posted Tax Year 2026 sehingga Class Code terkunci (TC-FA-TDC-74); BLD-NP memiliki satu versi Scheduled Effective From Jan 2027 (TC-FA-TDC-75); NB-OLD Inactive (TC-FA-TDC-76); NB-4 Active dengan Used By 0 (TC-FA-TDC-77). Nilai awal Class Name NB-2 dan NB-1 dan Regulation Reference BLD-NP dipulihkan hook `after` lewat API.
- TC-FA-TDC-73 menyebut kondisi 7 class seed; spec memakai 9 class Example Data (7 class seed termasuk di dalamnya) sebagai kondisi dasar spec.
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps


### Edit Class Name pada class biasa (TC-FA-TDC-73)

1. Klik Class Code NB-2
2. Ubah Class Name menjadi `Bukan bangunan – Kelompok 2 Revisi`
3. Klik `[Save]`
4. Verifikasi dialog Save Changes tidak tampil karena hanya Class Name yang berubah
5. Verifikasi toast sukses `Success, tax depreciation class has been updated.`
6. Verifikasi Drawer menutup
7. Verifikasi tabel menampilkan Class Name baru pada NB-2

### Edit pada class dengan Class Code terkunci (TC-FA-TDC-74)

8. Klik Class Code NB-1
9. Hover field Class Code
10. Verifikasi Class Code Disabled dengan ikon gembok dan tooltip `Code can't be changed after fiscal depreciation has been posted.`
11. Ubah Class Name menjadi `Bukan bangunan – Kelompok 1 Revisi`
12. Klik `[Save]`
13. Verifikasi toast sukses `Success, tax depreciation class has been updated.`
14. Verifikasi tabel menampilkan Class Name baru pada NB-1 dengan Class Code tetap `NB-1`

### Edit Regulation Reference pada class dengan versi Scheduled (TC-FA-TDC-75)

15. Klik Class Code BLD-NP
16. Ubah Regulation Reference menjadi `PMK 72/2023`
17. Klik `[Save]`
18. Verifikasi dialog Save Changes tidak tampil karena hanya Regulation Reference yang berubah
19. Verifikasi toast sukses `Success, tax depreciation class has been updated.`
20. Verifikasi Drawer menutup
21. Klik Class Code BLD-NP
22. Verifikasi Alert versi Scheduled masih tampil
23. Tutup Drawer dengan `[×]`

### Mengaktifkan class lewat toggle Active (TC-FA-TDC-76)

24. Klik toggle Active pada baris NB-OLD
25. Verifikasi dialog `Activate Tax Depreciation Class` tampil dengan bullet `NB-OLD – Kelompok khusus lama`, teks `Are you sure you want to activate it?`, tombol `[Cancel]` dan `[Activate]`
26. Klik `[Activate]`
27. Verifikasi toast sukses `Success, tax depreciation class has been activated.`
28. Verifikasi toggle NB-OLD berubah On

### Menonaktifkan class Used By 0 lewat toggle Active (TC-FA-TDC-77)

29. Klik toggle Active pada baris NB-4
30. Verifikasi dialog `Deactivate Tax Depreciation Class` tampil dengan bullet `NB-4 – Bukan bangunan – Kelompok 4`, teks `Are you sure you want to deactivate it?`, tombol `[Cancel]` dan `[Deactivate]`
31. Klik `[Deactivate]`
32. Verifikasi toast sukses `Success, tax depreciation class has been deactivated.`
33. Verifikasi toggle NB-4 berubah Off

## Notes

- Satu aktor (Update-Only) untuk seluruh spec; login di hook `before`, tidak ada ganti akun. Urutan TC mengikuti nomor; aksi mengubah status (TC-FA-TDC-76 dan 77) diletakkan di akhir.
- Langkah penghubung (S-03): langkah menutup Drawer pada blok TC-FA-TDC-75 sebelum membuka kembali. Tidak ada pemulihan form dirty karena setiap `[Save]` menutup Drawer.
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - TC-74 tidak menyebut Drawer menutup setelah `[Save]` (TC-73 dan 75 menyebutnya), tetapi Expected c menilai isi tabel; spec tidak mengasersi penutupan Drawer pada TC-74.
  - Post Condition TC-73 ("tidak ada versi baru"), TC-74, TC-75, TC-76, dan TC-77 tidak punya langkah observasi di TC; tidak diasersi (S-01).

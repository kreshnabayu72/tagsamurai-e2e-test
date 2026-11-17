---
id: TC-FA-TDC-E2E-027-aktor-delete-only-bulk-delete-lolos-campuran-dan-diblokir
title: "Aktor Delete-Only: Bulk Delete Lolos, Campuran, dan Diblokir"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-88
  - TC-FA-TDC-89
  - TC-FA-TDC-90
sourceRules: ["D-04", "F-FATDC-13.k10", "F-FATDC-13.k11", "D-15", "T-06b", "F-FATDC-13.k9", "D-06", "F-FATDC-13.k8"]
smoke: []
dependsOn: []
trace:
  "D-04": 3
  "F-FATDC-13.k10": [3, 5, 6]
  "F-FATDC-13.k11": 7
  "D-15": 11
  "T-06b": 13
  "F-FATDC-13.k9": 14
  "D-06": 18
  "F-FATDC-13.k8": [18, 20, 21]
coverage:
  web: automated
---

# Aktor Delete-Only: Bulk Delete Lolos, Campuran, dan Diblokir

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Delete-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_DELETEONLY_PASSWORD` | langkah 1 sampai 21 |

- Login di hook `before` spec ini sebagai Delete-Only (Manage accounting); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji" belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; penulis script mendaftarkannya.
- Data (kondisi awal): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; 9 baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Hook `before` spec ini menyeed ulang kondisi itu lewat API dan hook `after` memulihkannya; Class Code dibatasi 15 karakter sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Akun aktor sudah tersedia dan memiliki akses tab (Read) ke Settings > Accounting > Tax Depreciation Class.
- Kebutuhan data: NB-1 (Last Posted Tax Year 2026) dan NB-2 (dipakai Asset Class) diblokir guard; NB-KHS memiliki Last Posted Tax Year 2026; NB-4 dan class tambahan `NB-5` dengan Used By 0 dan belum pernah diposting (TC-FA-TDC-88). Dengan NB-5 tabel berisi 10 baris, satu halaman Pagination. NB-4 dan NB-5 diseed ulang lewat API sebelum TC-FA-TDC-88 (langkah 15), karena TC-FA-TDC-89 menghapus NB-4.
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps


### Bulk Delete seleksi yang semuanya diblokir (TC-FA-TDC-90)

1. Centang baris NB-1 dan NB-2
2. Klik aksi `Delete` pada Bulk Action Bar
3. Verifikasi dialog `Cannot Delete Tax Depreciation Classes` tampil dengan bullet `NB-1 – Bukan bangunan – Kelompok 1 — "has posted fiscal depreciation"` dan `NB-2 – Bukan bangunan – Kelompok 2 — "used by asset classes"`, teks `These classes cannot be deleted.`, tombol `[OK]`
4. Klik `[OK]`
5. Verifikasi tidak ada toast
6. Verifikasi kedua class (NB-1 dan NB-2) tetap ada
7. Verifikasi seleksi dipertahankan setelah `[OK]`

### Bulk Delete seleksi campuran (TC-FA-TDC-89)

8. Klik Unselect All
9. Centang baris NB-4, NB-2, dan NB-KHS
10. Klik aksi `Delete` pada Bulk Action Bar
11. Verifikasi dialog `Delete Tax Depreciation Classes`: `The following will be deleted:` bullet `NB-4 – Bukan bangunan – Kelompok 4`; `The following cannot be deleted and will be skipped:` bullet `NB-2 – Bukan bangunan – Kelompok 2 — "used by asset classes"` dan `NB-KHS – Kelompok khusus pernah diposting — "has posted fiscal depreciation"`; `Are you sure you want to continue?`; tombol `[Cancel]` dan `[Continue]`
12. Klik `[Continue]`
13. Verifikasi toast sukses `Success, tax depreciation class has been deleted. Some items were skipped (posted or used by asset classes).`
14. Verifikasi hanya NB-4 yang hilang dari tabel; NB-2 dan NB-KHS tetap ada

### Bulk Delete seleksi yang lolos guard (TC-FA-TDC-88)

15. Seed ulang NB-4 dan NB-5 (Used By 0, belum pernah diposting) lewat API hingga tersimpan, lalu muat ulang halaman
16. Centang baris NB-4 dan NB-5
17. Klik aksi `Delete` pada Bulk Action Bar
18. Verifikasi dialog `Delete Tax Depreciation Classes` tampil dengan bullet `NB-4 – Bukan bangunan – Kelompok 4` dan `NB-5 – Bukan bangunan – Kelompok 5`, teks `This action cannot be undone. Are you sure you want to delete them?`
19. Klik `[Delete]`
20. Verifikasi toast sukses `Success, tax depreciation class has been deleted.`
21. Verifikasi baris NB-4 dan NB-5 hilang dari tabel

## Notes

- Satu aktor (Delete-Only) untuk seluruh spec; login di hook `before`, tidak ada ganti akun. Urutan TC diubah menjadi 90, 89, 88: seleksi yang diblokir lebih dulu (tanpa menghapus data), Bulk Delete yang menghapus data di akhir. TC-FA-TDC-89 menghapus NB-4 sehingga NB-4 diseed ulang di langkah 15 (langkah penghubung, S-03).
- Langkah penghubung (S-03): Unselect All sebelum TC-FA-TDC-89 karena seleksi dipertahankan setelah `[OK]` (S-09); seed ulang pada langkah 15.
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - Post Condition TC-88, 89, dan 90 tidak punya langkah observasi terpisah dari Expected; tidak diasersi di luar Expected (S-01).
  - TC-89 dan TC-88 tidak menyebut keadaan seleksi sesudah aksi; TC-90 menyebutnya dipertahankan.

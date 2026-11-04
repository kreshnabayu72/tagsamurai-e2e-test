---
id: TC-FA-TDC-E2E-022-aktor-create-only-membuat-class-dan-memulihkan-seed
title: "Aktor Create-Only: Membuat Class dan Memulihkan Seed lewat Restore default classes"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-71
  - TC-FA-TDC-72
  - TC-FA-TDC-323
coverage:
  web: automated
---

# Aktor Create-Only: Membuat Class dan Memulihkan Seed lewat Restore default classes

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Create-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_CREATEONLY_PASSWORD` | langkah 1 sampai 25 |

- Login di hook `before` spec ini sebagai Create-Only (Manage accounting); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji" belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; penulis script mendaftarkannya.
- Data (kondisi awal TC-FA-TDC-71): tabel berisi 7 class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) belum diubah; hook `before` spec ini menyeed kondisi itu lewat API dan hook `after` memulihkannya. Blok TC-FA-TDC-72 dan TC-FA-TDC-323 mengosongkan seluruh class lewat API (tabel tanpa class, Empty State tampil); Master Data Count Limit tidak membatasi tujuh class. Tabel tidak melebihi satu halaman Pagination.
- Akun aktor sudah tersedia dan memiliki akses tab (Read) ke Settings > Accounting > Tax Depreciation Class.
- Class `NB-5` yang dibuat TC-FA-TDC-71 dihapus oleh hook `after` lewat API (aktor Create-Only tidak memiliki hak Delete).
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps


### Create class (TC-FA-TDC-71)

1. Klik `+ Class`
2. Isi Regulation Reference `UU HPP 7/2021; PMK 72/2023`
3. Isi Class Code `NB-5`
4. Isi Class Name `Bukan bangunan – Kelompok 5`
5. Pilih Asset Type `Non-building`
6. Isi Useful Life `12`
7. Pilih Allowed Methods `Straight Line` dan `Declining Balance`
8. Biarkan checkbox `Stay on this form after submitting` tidak dicentang, lalu klik `[Submit]`
9. Verifikasi toast sukses `Success, tax depreciation class has been created.`
10. Verifikasi Drawer menutup
11. Verifikasi tabel dimuat ulang dan baris NB-5 tampil di-highlight sesaat
12. Verifikasi baris NB-5: Active On, Used By 0, Effective From `—`

### Restore dari Empty State (TC-FA-TDC-72)

13. Kosongkan seluruh class lewat API hingga tabel tanpa class tersimpan, lalu muat ulang halaman
14. Klik tombol `Restore default classes` di Empty State
15. Verifikasi dialog pratinjau memuat bagian `To be created` dengan 7 bullet class seed dan tombol `[Cancel]` dan `[Restore]`
16. Klik `[Restore]`
17. Verifikasi toast sukses `Success, default classes have been restored.`
18. Verifikasi tabel menampilkan 7 class seed

### Restore membuat ketujuh class seed (TC-FA-TDC-323)

19. Kosongkan seluruh class lewat API hingga tabel tanpa class tersimpan, lalu muat ulang halaman
20. Klik `Restore default classes`
21. Klik `[Restore]`
22. Verifikasi toast sukses `Success, default classes have been restored.`
23. Verifikasi dialog D-12 tertutup
24. Verifikasi Empty State hilang
25. Verifikasi tabel memuat tujuh baris: NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND, semuanya Active = On

## Notes

- Satu aktor (Create-Only) untuk seluruh spec; login di hook `before`, tidak ada ganti akun.
- TC-FA-TDC-72 dan TC-FA-TDC-323 membutuhkan tabel tanpa class; data tabel milik spec ini dikosongkan lewat API di langkah 13 dan 19 (langkah penghubung, S-03). Kemampuan itu disediakan tim FE/BE (lihat `suite.md`).
- Urutan TC-FA-TDC-71 (tabel berisi class) mendahului dua blok tabel kosong supaya pengosongan data berada di akhir.
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - TC-71 menyebut 7 class seed, sedangkan TC lain di slice ini memakai 9 class Example Data; spec memakai kondisi masing-masing TC.
  - Post Condition TC-71 ("Class NB-5 tersimpan berstatus Active"), TC-72 ("7 class seed tersimpan berstatus Active"), dan TC-323 (versi pertama tanpa Effective From, tujuh entri L-01 per surface, tujuh class muncul sebagai opsi Asset Class) tidak punya langkah observasi di TC; tidak diasersi di spec ini (S-01). Entri log tiap surface diasersi di spec pencatatan log; opsi Asset Class di TC modul Asset Class.
  - TC-323 menyebut "tabel memuat tujuh baris" dan daftar kode kelas; urutan baris tidak ditentukan sehingga tidak diasersi.

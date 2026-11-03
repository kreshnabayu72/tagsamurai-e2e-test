---
id: TC-FA-CAT-E2E-169-atomisitas-log-rollback-create-edit-delete
title: "Atomisitas Log: Kegagalan Penulisan Log Membatalkan Seluruh Aksi Create, Edit, dan Delete"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-580
coverage:
  web: automated
---

# Atomisitas Log: Kegagalan Penulisan Log Membatalkan Seluruh Aksi Create, Edit, dan Delete

## Prerequisites

- Mode: FE+BE.
- Kelas harness b (fault injection di sisi server: penulisan log dipaksa gagal, rollback DB). Kegagalan sisi server tidak dapat di-intercept di browser sehingga spec tetap FE+BE (bagian 6).
- Akun login hook `before` spec ini: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; kemampuan seed disediakan tim FE/BE), nama berakhiran `{runId}-169`, client CatMain: `Furniture Rb {runId}-169` (Code `FRB169`, leaf, Description kosong) sebagai target Edit dan `Vehicle Rb {runId}-169` (Code `VRB169`, leaf) sebagai target Delete. Kategori `Rollback Cat {runId}-169` tidak di-seed (target Create yang harus gagal).
- Kemampuan teknis yang dibutuhkan, disediakan tim BE/FE tanpa endpoint karangan (S-13):
  - Fault injection sisi server yang membuat penulisan log (Changelog, System Log, Activity Log) gagal, dapat diaktifkan dan dinonaktifkan oleh spec; hook `after` menonaktifkannya walau spec gagal di tengah (R-08). TC menyebut mekanisme ini sebagai syarat (testcase-conventions P21 21g).
  - Membaca dari server: jumlah kategori client CatMain, Description kategori, keberadaan kategori, serta jumlah entri Modal Changelog, System Log, dan Activity Log sebelum dan sesudah aksi (bagian 8b butir 10; baseline S-12).
  - Konfirmasi dialog `beforeunload` saat muat ulang halaman (S-08).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-580: Rollback atomik Create, Edit, dan Delete

1. Catat baseline: jumlah kategori client CatMain dan jumlah entri Modal Changelog, System Log, serta Activity Log
2. Aktifkan fault injection kegagalan penulisan log (Changelog, System Log, Activity Log) di sisi server hingga aktif
3. Klik `[+] Category` pada sidebar
4. Isi Category Name `Rollback Cat {runId}-169`
5. Klik `[Submit]`
6. Verifikasi toast `Error, failed to create category.` tanpa tombol aksi
7. Verifikasi popup New Category tetap terbuka
8. Verifikasi `Rollback Cat {runId}-169` tidak tersimpan pada data dari server
9. Muat ulang halaman Categories
10. Klik elipsis (⋯) pada baris `Furniture Rb {runId}-169` > `Edit`
11. Ubah Description menjadi `Rollback Desc`
12. Klik `[Save]`
13. Verifikasi toast `Error, failed to update category.`
14. Verifikasi Description `Furniture Rb {runId}-169` tidak berubah pada data dari server
15. Muat ulang halaman Categories
16. Klik elipsis (⋯) pada baris `Vehicle Rb {runId}-169` > `Delete`
17. Klik `[Delete]` pada dialog
18. Verifikasi toast `Error, failed to delete category.`
19. Verifikasi `Vehicle Rb {runId}-169` tetap ada pada data dari server
20. Nonaktifkan fault injection hingga nonaktif
21. Muat ulang halaman Categories
22. Buka Modal Changelog
23. Verifikasi Modal Changelog memuat sedikitnya satu baris
24. Verifikasi jumlah kategori client CatMain dari server sama dengan baseline
25. Verifikasi jumlah entri Modal Changelog, System Log, dan Activity Log sama dengan baseline (tidak ada baris log untuk ketiga aksi)
26. Tutup Modal Changelog

## Notes

- `P-1` (state berat): asersi absence log (langkah 25, Expected d) milik TC-FA-CAT-580 tetap di spec ini karena kondisinya bergantung pada fault injection dan rangkaian tiga aksi gagal yang baru dibangun langkah 2 sampai 19 dalam satu keadaan; spec absence 168 tidak memuat aksi Create, Edit, dan Delete yang gagal akibat kegagalan log. Langkah 25 memakai baseline (langkah 1) dan anchor langkah 23 (Modal Changelog memuat baris).
- Langkah penghubung (S-03): langkah 1 (baseline), langkah 2 dan 20 (mengatur fault injection), langkah 9, 15, 21 (muat ulang halaman; form dirty dari popup atau Edit yang gagal tidak terbawa, dialog `beforeunload` dikonfirmasi, kemampuan tertulis di Prerequisites), langkah 22 dan 26 (membuka dan menutup Modal Changelog).
- Langkah 8, 14, 19, 24 memakai pembacaan data dari server karena kegagalan penulisan log hanya terlihat dari state data; hal ini sejalan dengan Expected TC (tidak ada state parsial).
- Target Edit dan Delete memakai data bersuffix milik spec (S-06) walau TC menyebut `Furniture` dan `Vehicle` Pre-setup; Expected "jumlah kategori tetap 15" ditulis sebagai selisih terhadap baseline (langkah 24) karena jumlah kategori CatMain berubah antar spec.
- Temuan untuk QA:
  - TC-FA-CAT-580 berlabel Manual Only BE; mekanisme fault injection penulisan log tidak ada di TC, PRD, atau LLD. Spec ditulis dengan kemampuan "disediakan tim BE"; bila tim BE tidak menyediakannya, `coverage.web` perlu diubah menjadi `unsupported`.
  - TC-FA-CAT-580 Expected a menyebut popup tetap terbuka hanya untuk Create; keadaan form Edit dan dialog Delete sesudah kegagalan tidak disebut, sehingga spec tidak mengasersinya dan memuat ulang halaman.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.

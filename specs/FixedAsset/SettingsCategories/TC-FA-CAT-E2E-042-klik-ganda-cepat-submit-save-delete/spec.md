---
id: TC-FA-CAT-E2E-042-klik-ganda-cepat-submit-save-delete
title: "Klik Ganda Cepat pada Submit, Save, Delete, dan Bulk Delete Hanya Menjalankan Aksi Sekali"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-140
  - TC-FA-CAT-629
  - TC-FA-CAT-208
  - TC-FA-CAT-237
  - TC-FA-CAT-268
coverage:
  web: automated
---

# Klik Ganda Cepat pada Submit, Save, Delete, dan Bulk Delete Hanya Menjalankan Aksi Sekali

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #20 (CatMain), dibaca: parent `Peripheral` (Internal).
- Data milik spec (seed lewat API di hook `before`, disediakan tim FE/BE, menggantikan `Furniture`, `Vehicle`, dan `Heavy Tools` Pre-setup agar Pre-setup tidak berubah, S-06): leaf L1 `Edit Dbl {runId}-042`, `Del Dbl {runId}-042`, `Bulk A {runId}-042`, `Bulk B {runId}-042` (Total Asset 0).
- Data Dinamis (dibuat spec): `Double Cat {runId}-042` (L1) dan `Double Sub {runId}-042` (di bawah `Peripheral`). Hook `after` menghapus semua kategori milik spec yang masih ada.
- Changelog: seluruh nama kategori di spec ini bersuffix unik sehingga baseline jumlah baris Changelog adalah nol (S-12).
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-140: Klik ganda Submit pada Create

1. Klik `[+] Category` pada sidebar
2. Isi Category Name `Double Cat {runId}-042`
3. Klik `[Submit]` dua kali dengan cepat
4. Verifikasi hanya satu kategori `Double Cat {runId}-042` tersimpan
5. Verifikasi hanya satu toast sukses
6. Buka Modal Changelog dan filter Category Name `Double Cat {runId}-042`
7. Verifikasi Changelog memuat tepat satu baris Create untuk `Double Cat {runId}-042`
8. Tutup Modal Changelog

### TC-FA-CAT-629: Klik ganda Submit pada New Subcategory

9. Tunggu toast lama hilang otomatis
10. Klik elipsis (⋯) pada baris `Peripheral` > `+ Add Subcategory`
11. Isi Category Name `Double Sub {runId}-042`
12. Klik `[Submit]` dua kali dengan cepat
13. Verifikasi hanya satu kategori `Double Sub {runId}-042` tersimpan di bawah `Peripheral`
14. Verifikasi hanya satu toast sukses
15. Buka Modal Changelog dan filter Category Name `Double Sub {runId}-042`
16. Verifikasi Changelog memuat tepat satu baris Create untuk `Double Sub {runId}-042`
17. Tutup Modal Changelog

### TC-FA-CAT-208: Klik ganda Save pada Edit

18. Tunggu toast lama hilang otomatis
19. Klik elipsis (⋯) pada baris `Edit Dbl {runId}-042` > `Edit`
20. Ubah Description menjadi `Double desc`
21. Klik `[Save]` dua kali dengan cepat
22. Verifikasi hanya satu toast sukses
23. Buka Modal Changelog dan filter Category Name `Edit Dbl {runId}-042`
24. Verifikasi Changelog memuat tepat satu baris Edit Field `Description`
25. Tutup Modal Changelog

### TC-FA-CAT-237: Klik ganda Delete

26. Tunggu toast lama hilang otomatis
27. Klik elipsis (⋯) pada baris `Del Dbl {runId}-042` > `Delete`
28. Klik `[Delete]` dua kali dengan cepat
29. Verifikasi hanya satu toast sukses
30. Buka Modal Changelog dan filter Category Name `Del Dbl {runId}-042`
31. Verifikasi Changelog memuat tepat satu baris Delete untuk `Del Dbl {runId}-042`
32. Tutup Modal Changelog

### TC-FA-CAT-268: Klik ganda Delete pada Bulk Delete

33. Tunggu toast lama hilang otomatis
34. Centang checkbox baris `Bulk A {runId}-042` dan `Bulk B {runId}-042`
35. Klik `[Delete]` pada Bulk Action Bar
36. Klik `[Delete]` pada dialog konfirmasi dua kali dengan cepat
37. Verifikasi hanya satu toast sukses
38. Buka Modal Changelog dan filter Category Name `Bulk A {runId}-042`
39. Verifikasi Changelog memuat tepat satu baris Delete untuk `Bulk A {runId}-042`
40. Filter Category Name `Bulk B {runId}-042`
41. Verifikasi Changelog memuat tepat satu baris Delete untuk `Bulk B {runId}-042`
42. Tutup Modal Changelog

## Notes

- Alasan di atas sekitar 35 langkah: lima TC satu topik (klik ganda) pada halaman yang sama; tiap blok memakai kategori milik spec sendiri dan berdiri sendiri, dan pembacaan Changelog diulang per blok (blok baca-log berpola, bagian 3 prinsip 13).
- Langkah penghubung (S-03): langkah 8, 17, 25, 32, 42 (menutup Modal Changelog), langkah 9, 18, 26, 33 (menunggu toast lama hilang, R-12).
- TC-268 langkah 1 sampai 3 digabung dengan konfirmasi `[Delete]` karena klik ganda terjadi pada dialog konfirmasi; "satu set baris log per node" diasersi per node pada langkah 39 dan 41.
- Temuan untuk QA:
  - TC-268 menyebut klik ganda `[Delete]` tanpa membedakan tombol Bulk Action Bar dan dialog konfirmasi; spec memakai klik ganda pada dialog konfirmasi (TC-237 pola yang sama).
  - TC-140 dan TC-208 tidak menyebut cara membuka Changelog; spec memakai pola TC-FA-CAT-166.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.

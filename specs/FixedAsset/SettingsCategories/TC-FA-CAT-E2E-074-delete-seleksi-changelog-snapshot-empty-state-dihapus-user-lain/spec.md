---
id: TC-FA-CAT-E2E-074-delete-seleksi-changelog-snapshot-empty-state-dihapus-user-lain
title: "Delete: Seleksi Sidebar, Snapshot Path Changelog, Transisi ke Empty State, dan Node yang Dihapus User Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-230
  - TC-FA-CAT-239
  - TC-FA-CAT-540
  - TC-FA-CAT-234
coverage:
  web: automated
---

# Delete: Seleksi Sidebar, Snapshot Path Changelog, Transisi ke Empty State, dan Node yang Dihapus User Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data milik spec (di-seed hook `before` lewat API, kemampuan seed disediakan tim FE/BE; dibersihkan hook `after` bila tersisa), nama berakhiran `{runId}-074`:
  - `Peripheral {runId}-074` (Code `PE74`) berisi `Keyboard {runId}-074` dan `Mouse {runId}-074` (TC-FA-CAT-230).
  - `Accessory A {runId}-074` (Code `AA74`) berisi `Cable A {runId}-074` (TC-FA-CAT-239).
  - `Accessory B {runId}-074` (Code `AB74`) berisi satu anak `Cable B {runId}-074` (TC-FA-CAT-540).
  - `Vehicle {runId}-074` (Code `V74`) leaf (TC-FA-CAT-234).
  - Data hasil rename: `Accessory A X {runId}-074`.
- Pelaku kedua TC-FA-CAT-234: sesi API Total Control (Pre-setup #1) yang hanya memicu penghapusan; mengikuti butir "Sesi API aktor" di `suite.md`.
- Kemampuan teknis: membaca jumlah entri Changelog kategori sebelum dan sesudah aksi (baseline); disediakan tim FE/BE.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-230: Delete node terpilih mengembalikan seleksi ke All Categories, Delete node lain tidak mengubah seleksi

1. Klik node `Peripheral {runId}-074` di sidebar
2. Klik elipsis (⋯) pada baris `Keyboard {runId}-074` > `Delete`
3. Klik `[Delete]`
4. Verifikasi seleksi sidebar tetap `Peripheral {runId}-074`
5. Klik node `Mouse {runId}-074` di sidebar
6. Klik elipsis node `Peripheral {runId}-074` di sidebar > `Delete`
7. Klik `[Delete]`
8. Verifikasi seleksi sidebar kembali ke `All Categories`
9. Verifikasi Category Context Header kembali ke `All Categories`

### TC-FA-CAT-239: Entri Changelog Delete memuat path sebelum dihapus dan tidak berubah oleh aksi berikutnya

10. Klik node `Accessory A {runId}-074` di sidebar
11. Klik elipsis (⋯) pada baris `Cable A {runId}-074` > `Delete`
12. Klik `[Delete]`
13. Klik node `All Categories` di sidebar
14. Ketik Search `Accessory A {runId}-074`, tekan Enter
15. Klik elipsis (⋯) pada baris `Accessory A {runId}-074` > `Edit`
16. Ubah Category Name menjadi `Accessory A X {runId}-074`
17. Klik `[Save]`
18. Buka Modal Changelog
19. Verifikasi entri Delete `Cable A {runId}-074` menampilkan Category Name path `Accessory A {runId}-074 › Cable A {runId}-074` dan tidak berubah menjadi `Accessory A X {runId}-074 › Cable A {runId}-074`
20. Verifikasi Old Value `Cable A {runId}-074` dan New Value `—`
21. Tutup Modal Changelog

### TC-FA-CAT-540: Transisi masuk ke empty state S-12, menghapus subkategori terakhir node terpilih

22. Klik node `Accessory B {runId}-074` di sidebar
23. Klik elipsis (⋯) pada baris `Cable B {runId}-074` > `Delete`
24. Klik `[Delete]` pada dialog D-09
25. Verifikasi toast `Success, category has been deleted.`
26. Verifikasi area tabel berpindah ke empty state dengan ilustrasi, Title `No subcategory yet`, dan Description `This category does not have any subcategories.`
27. Verifikasi seleksi sidebar tetap `Accessory B {runId}-074`
28. Verifikasi `Accessory B {runId}-074` menjadi Leaf

### TC-FA-CAT-234: Delete node yang sudah dihapus user lain, toast netral T-12 tanpa log baru

29. Klik node `All Categories` di sidebar
30. Ketik Search `Vehicle {runId}-074`, tekan Enter
31. Klik elipsis (⋯) pada baris `Vehicle {runId}-074` > `Delete` sampai dialog tampil
32. Sesi API Total Control menghapus `Vehicle {runId}-074` hingga penghapusan tersimpan
33. Catat baseline jumlah entri Changelog kategori (N1)
34. Klik `[Delete]`
35. Verifikasi toast netral `This category is no longer available.`
36. Verifikasi tabel dan sidebar di-refresh sehingga `Vehicle {runId}-074` tidak lagi tampil
37. Verifikasi jumlah entri Changelog kategori masih N1 (tidak ada baris log baru)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas (fungsional Delete) dengan data milik spec yang terpisah per TC, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`, S-03/R-16): klik node All Categories dan Search untuk menemukan baris target, membuka dan menutup Modal Changelog, pencatatan baseline.
- P-1: asersi "tidak ada baris log baru" pada TC-FA-CAT-234 berada di spec ini dengan baseline (S-12) karena konteksnya (dialog terbuka dan penghapusan oleh sesi lain) dibangun langkah sebelumnya.
- Temuan untuk QA:
  - TC-FA-CAT-234 menyebut "tidak ada baris log baru" tanpa surface; spec hanya memeriksa Changelog. Baseline dicatat sesudah penghapusan oleh sesi API karena penghapusan itu sendiri menulis log.
  - TC-FA-CAT-234 berlabel Manual Only (dua sesi paralel), tetapi pelaku kedua hanya memicu perubahan state sehingga memakai sesi API.
  - TC-FA-CAT-239 mengubah nama lewat row action Edit; TC tidak menyebut jalur Edit secara rinci.

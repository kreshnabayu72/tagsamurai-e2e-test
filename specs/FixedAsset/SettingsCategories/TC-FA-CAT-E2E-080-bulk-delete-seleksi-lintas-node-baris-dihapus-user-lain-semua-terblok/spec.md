---
id: TC-FA-CAT-E2E-080-bulk-delete-seleksi-lintas-node-baris-dihapus-user-lain-semua-terblok
title: "Bulk Delete: Seleksi Lintas Node Sidebar, Semua Baris Menjadi Terblok saat Eksekusi, dan Baris Dihapus User Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-573
  - TC-FA-CAT-263
  - TC-FA-CAT-265
coverage:
  web: automated
---

# Bulk Delete: Seleksi Lintas Node Sidebar, Semua Baris Menjadi Terblok saat Eksekusi, dan Baris Dihapus User Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua: sesi API Total Control (Pre-setup #1) yang hanya memicu perubahan state (membuat Asset Name, menghapus kategori); mengikuti butir "Sesi API aktor" di `suite.md`. Kemampuan membuat Asset Name yang menunjuk kategori dan menghapusnya kembali disediakan tim FE/BE tanpa endpoint karangan.
- Data Pre-setup #20 yang hanya dibaca: `Furniture` (dicentang, tidak dihapus), `Electronics` berisi `Laptop` (dicentang, tidak dihapus).
- Data milik spec (di-seed hook `before` lewat API, kemampuan seed disediakan tim FE/BE; Asset Name buatan sesi API dan kategori dibersihkan hook `after`): `Vehicle A {runId}-080` dan `Heavy Tools A {runId}-080` (leaf, untuk TC-FA-CAT-263); `Vehicle B {runId}-080` dan `Heavy Tools B {runId}-080` (leaf, untuk TC-FA-CAT-265). Menggantikan `Vehicle` dan `Heavy Tools` (Pre-setup #39).
- Kemampuan teknis: membaca jumlah entri Changelog kategori sebelum dan sesudah aksi (baseline); disediakan tim FE/BE.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Atur jumlah baris per halaman menjadi 25

### TC-FA-CAT-573: Seleksi Bulk Delete bertahan saat node sidebar berganti dan counter menghitung lintas node

2. Pada node `All Categories`, centang checkbox baris `Furniture`
3. Klik node `Electronics` di Sidebar Category Tree
4. Verifikasi Bulk Action Bar tetap tampil dengan counter `1 category selected` walau `Furniture` tidak tampil di tabel node `Electronics`
5. Centang checkbox baris `Laptop`
6. Verifikasi counter `2 categories selected`
7. Klik node `All Categories` di Sidebar Category Tree
8. Verifikasi `Furniture` tetap tercentang
9. Verifikasi counter tetap `2 categories selected` walau `Laptop` tidak tampil di tabel
10. Klik node `Electronics` di Sidebar Category Tree
11. Verifikasi `Laptop` masih tercentang
12. Klik icon (×) pada Bulk Action Bar
13. Klik node `All Categories` di Sidebar Category Tree

### TC-FA-CAT-263: Seluruh baris menjadi terblok saat eksekusi, dialog blok tanpa toast dan seleksi dipertahankan

14. Atur jumlah baris per halaman menjadi 25
15. Centang checkbox baris `Vehicle A {runId}-080` dan `Heavy Tools A {runId}-080`
16. Klik `[Delete]` pada Bulk Action Bar sampai dialog D-11 tampil
17. Sesi API Total Control membuat Asset Name yang menunjuk `Vehicle A {runId}-080` dan `Heavy Tools A {runId}-080` hingga tersimpan
18. Catat baseline jumlah entri Changelog kategori (N1)
19. Klik `[Delete]` pada dialog D-11
20. Verifikasi dialog blok D-13 `Cannot Delete Categories` menampilkan `Vehicle A {runId}-080` dan `Heavy Tools A {runId}-080`
21. Verifikasi tidak ada toast
22. Klik `[OK]`
23. Verifikasi seleksi dan Bulk Action Bar dipertahankan
24. Verifikasi daftar di-refresh
25. Verifikasi jumlah entri Changelog kategori masih N1 (tidak ada log)
26. Klik icon (×) pada Bulk Action Bar

### TC-FA-CAT-265: Baris yang sudah dihapus user lain dilewati dan masuk hitungan skip tanpa log

27. Centang checkbox baris `Vehicle B {runId}-080` dan `Heavy Tools B {runId}-080`
28. Klik `[Delete]` pada Bulk Action Bar sampai dialog tampil
29. Sesi API Total Control menghapus `Heavy Tools B {runId}-080` hingga penghapusan tersimpan
30. Catat baseline jumlah entri Changelog kategori (N2)
31. Klik `[Delete]` pada dialog
32. Verifikasi toast ringkasan `Success, category has been deleted. Some items were skipped.`
33. Verifikasi `Vehicle B {runId}-080` terhapus
34. Verifikasi `Heavy Tools B {runId}-080` dilewati sebagai skip
35. Verifikasi jumlah entri Changelog kategori bertambah tepat satu (N2 + 1, hanya baris Delete `Vehicle B {runId}-080`)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Urutan: TC-FA-CAT-573 (hanya seleksi), TC-FA-CAT-263 (tanpa eksekusi), lalu TC-FA-CAT-265 (menghapus data) sesuai S-10.
- Langkah penghubung (tanpa `Verifikasi`, S-03/S-09): pengaturan jumlah baris per halaman, klik node All Categories, `[OK]`, icon (×), pencatatan baseline.
- P-1: asersi "tidak ada log" pada TC-FA-CAT-263 berada di spec ini dengan baseline (S-12) karena konteksnya (dialog D-11 terbuka dan perubahan Asset Name oleh sesi lain) dibangun langkah sebelumnya.
- Data milik spec menggantikan `Vehicle` dan `Heavy Tools` (S-06).
- Temuan untuk QA:
  - TC-FA-CAT-263 tidak menyebut jumlah Asset Name yang dibuat sesi B sehingga body dialog D-13 tidak diasersi.
  - TC-FA-CAT-265 Expected a ("dilewati sebagai skip tanpa baris log baru") ambigu karena penghapusan oleh sesi B sendiri menulis log; spec memakai baseline sesudah penghapusan itu dan mengharapkan hanya satu baris baru (Delete `Vehicle B {runId}-080`).
  - TC-FA-CAT-263 dan TC-FA-CAT-265 berlabel Manual Only (dua sesi paralel), tetapi pelaku kedua hanya memicu perubahan state sehingga memakai sesi API.
  - TC-FA-CAT-263 menyebut "tidak ada log" tanpa surface; spec hanya memeriksa Changelog.

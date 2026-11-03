---
id: TC-AC-DC-E2E-013-filter-category-perubahan-tree
title: "Filter Category saat Tree Berubah: Child Baru, Hapus Node Terpilih, Hapus Ancestor Node Terpilih, dan Rename Node Terpilih"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-32
  - TC-AC-DC-33
  - TC-AC-DC-34
  - TC-AC-DC-282
coverage:
  web: automated
---

# Filter Category saat Tree Berubah: Child Baru, Hapus Node Terpilih, Hapus Ancestor Node Terpilih, dan Rename Node Terpilih

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #14 (node `Hardware` dan `Handheld Reader`) hanya dibaca; semua target aksi tulis (Add, Edit, Delete) adalah node milik spec (S-06). Nilai literal diacu lewat `Fixture.settingsDeviceCategory.<kunci>` (`fixtures/settings-device-category.json`, belum ada; ditandai untuk tahap script).
- Data Dinamis milik spec, dibuat lewat sesi API aktor oleh hook `before` (kemampuan disediakan tim BE/FE; nilai field wajib Device Name lain disediakan tim FE) dan dihapus lewat API oleh hook `after` tanpa mengasumsikan setup berhasil penuh. Semua node berada di bawah `Handheld Reader`:
  - `Filter Induk {runId}-013` dengan anak `Filter Anak 1 {runId}-013` (Device Name `FN-1-{runId}-013`), `Filter Anak 2 {runId}-013` > `Filter Cucu {runId}-013` (Device Name `FN-2-{runId}-013`), dan `Filter Anak 3 {runId}-013` (Device Name `FN-3-{runId}-013`).
  - `Hapus Daun {runId}-013` (leaf, tanpa Device Name).
  - `Hapus Keluarga {runId}-013` dengan anak `Hapus Keluarga Anak A {runId}-013` (leaf) dan `Hapus Keluarga Anak B {runId}-013` > `Hapus Keluarga Cucu {runId}-013`, tanpa Device Name.
  - Node `Filter Anak 4 {runId}-013` dibuat lewat UI pada TC-AC-DC-32.
- Pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- State yang diubah spec: pohon Category (hanya node milik spec) dan pilihan filter Category (tersimpan per user); pilihan dikosongkan lewat `All Categories` setelah tiap TC dan oleh hook `after` sebagai cadangan.
- Kondisi awal tiap spec: halaman baru dibuka hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DC-32: Child baru di bawah parent yang tercentang tidak tercentang dan parent menjadi partial-check

1. Expand `Hardware`, `Handheld Reader`, dan `Filter Induk {runId}-013`
2. Centang kotak `Filter Induk {runId}-013`
3. Hover `Filter Induk {runId}-013`
4. Klik aksi `+ Subcategory`
5. Ketik `Filter Anak 4 {runId}-013` pada input inline Add
6. Klik `[Submit]`
7. Verifikasi node `Filter Anak 4 {runId}-013` muncul di bawah `Filter Induk {runId}-013` dalam keadaan tidak tercentang
8. Verifikasi `Filter Induk {runId}-013` berubah menjadi partial-check
9. Verifikasi tabel Device Name tetap menampilkan `FN-1-{runId}-013`, `FN-2-{runId}-013`, dan `FN-3-{runId}-013` (child baru belum masuk pilihan)
10. Klik baris `All Categories`

### TC-AC-DC-33: Node terpilih yang dihapus otomatis keluar dari pilihan filter

11. Klik node `Hapus Daun {runId}-013`
12. Klik node `Filter Anak 1 {runId}-013`
13. Hover node `Hapus Daun {runId}-013`
14. Klik aksi Delete
15. Klik `[Delete]` pada dialog Delete Category
16. Verifikasi `Hapus Daun {runId}-013` hilang dari tree
17. Verifikasi `Hapus Daun {runId}-013` hilang dari pilihan filter (hanya `Filter Anak 1 {runId}-013` yang tercentang)
18. Verifikasi `Filter Anak 1 {runId}-013` tetap tercentang
19. Verifikasi tabel tetap menampilkan `FN-1-{runId}-013`
20. Klik baris `All Categories`

### TC-AC-DC-34: Node ancestor dari node terpilih dihapus: node terhapus keluar dari pilihan, pilihan lain tetap

21. Expand `Hapus Keluarga {runId}-013` dan `Hapus Keluarga Anak B {runId}-013`
22. Klik node `Hapus Keluarga Cucu {runId}-013`
23. Klik node `Filter Anak 1 {runId}-013`
24. Hover node `Hapus Keluarga {runId}-013`
25. Klik aksi Delete
26. Klik `[Delete]` pada dialog Delete Category
27. Verifikasi `Hapus Keluarga {runId}-013` beserta seluruh descendant (termasuk `Hapus Keluarga Cucu {runId}-013`) hilang dari tree
28. Verifikasi `Hapus Keluarga {runId}-013` dan descendant-nya hilang dari pilihan filter (hanya `Filter Anak 1 {runId}-013` yang tercentang)
29. Verifikasi `Filter Anak 1 {runId}-013` tetap tercentang
30. Verifikasi tabel tetap menampilkan `FN-1-{runId}-013`
31. Klik baris `All Categories`

### TC-AC-DC-282: Rename node yang sedang menjadi pilihan filter: pilihan tetap dan label ikut berubah

32. Klik node `Filter Anak 1 {runId}-013`
33. Hover node `Filter Anak 1 {runId}-013`
34. Klik aksi Edit
35. Ganti isi input inline Edit dengan `Filter Anak Satu {runId}-013`
36. Klik `[Save]`
37. Verifikasi node tampil dengan label `Filter Anak Satu {runId}-013`
38. Verifikasi node `Filter Anak Satu {runId}-013` tetap tercentang
39. Verifikasi tabel Device Name tetap menampilkan `FN-1-{runId}-013`
40. Klik baris `All Categories`

## Notes

- Spec ini melewati sekitar 35 langkah (40 langkah). Alasan: seluruh blok berupa satu topik (pilihan filter Category saat tree berubah oleh aksi tulis), berbagi data seed `Filter Induk {runId}-013` dan state tree yang sama, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah mengulang pola klik node dan Delete dengan parameter berbeda.
- Langkah penghubung (S-03): `All Categories` (langkah 10, 20, 31, 40) melepas pilihan sebelum TC berikutnya (S-09); langkah 21 meng-expand family yang diasersi; setelah langkah 6 `Filter Induk {runId}-013` tetap ter-expand untuk langkah 12, 23, dan 32.
- Nama node dan Device Name seed bersuffix `{runId}-013` (S-12); TC menulis nama literal Pre-setup (`Filter Induk`, `Hapus Daun`, `Hapus Keluarga`, `FN-1`) sehingga asersi memakai nama bersuffix.
- Temuan untuk QA: (1) TC-AC-DC-32, 33, 34, dan 282 memakai node Pre-setup #14 sebagai target aksi tulis dan hapus (`Filter Induk`, `Hapus Daun`, `Hapus Keluarga`, `Filter Anak 1`); spec memakai node bersuffix milik sendiri dengan struktur yang sama. (2) TC-AC-DC-33 dan 34 menyebut `[Delete]` tetapi tidak menguraikan isi dialog; isi dialog diuji di spec Delete Category. (3) Pada TC-AC-DC-32, TC tidak menyatakan apakah node baru langsung terlihat; spec mengasersi node muncul di bawah `Filter Induk {runId}-013` yang sudah ter-expand.

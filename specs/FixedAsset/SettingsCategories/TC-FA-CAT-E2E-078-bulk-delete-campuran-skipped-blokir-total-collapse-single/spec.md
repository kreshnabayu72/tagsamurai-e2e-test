---
id: TC-FA-CAT-E2E-078-bulk-delete-campuran-skipped-blokir-total-collapse-single
title: "Bulk Delete Campuran: Dialog D-12 dengan Kelompok Skipped, Blokir Total D-13, dan Collapse ke Dialog Single"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-250
  - TC-FA-CAT-251
  - TC-FA-CAT-252
  - TC-FA-CAT-253
  - TC-FA-CAT-257
coverage:
  web: automated
---

# Bulk Delete Campuran: Dialog D-12 dengan Kelompok Skipped, Blokir Total D-13, dan Collapse ke Dialog Single

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup in-use yang hanya dibaca dan menjadi target aksi yang selalu dilewati atau diblokir guard (tidak diubah, Last Updated tidak berubah; S-06): `Tools` (ditunjuk Asset Name `Drill Set`), `Furniture` (ditunjuk `Office Chair`), `Electronics` (anak `Laptop` ditunjuk Asset Name `Laptop Dell` dan `Laptop HP`), `Pointer B` berisi `Pointer A` (Pre-setup #39, ditunjuk Asset Name `Pointer Item`). Asset Name Pre-setup #21 dan #39.
- Data milik spec (di-seed hook `before` lewat API, kemampuan seed disediakan tim FE/BE; dibersihkan hook `after` bila tersisa): `Vehicle A {runId}-078` (Code `VA78`, leaf, target eksekusi campuran) dan `Vehicle B {runId}-078` (Code `VB78`, leaf, target dialog dan collapse single).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Atur jumlah baris per halaman menjadi 25

### TC-FA-CAT-252: Bulk Delete blokir total, dialog D-13 plural tanpa toast

2. Centang checkbox baris `Furniture` dan `Tools`
3. Klik `[Delete]` pada Bulk Action Bar
4. Verifikasi dialog `Cannot Delete Categories` dengan bullet `Furniture` dan `Tools` (daftar penuh scrollable), body `These categories (or their subcategories) are still used by 2 Asset Name templates in Asset Master. Update Asset Master before deleting.`, dan tombol `[OK]`
5. Klik `[OK]`
6. Verifikasi tidak ada eksekusi, baris `Furniture` dan `Tools` masih tampil
7. Verifikasi tidak ada toast
8. Verifikasi seleksi dan Bulk Action Bar dipertahankan
9. Klik icon (×) pada Bulk Action Bar

### TC-FA-CAT-253: Blokir total dengan satu Asset Name distinct memakai bentuk tunggal

10. Pada node `All Categories`, centang checkbox baris `Pointer B`
11. Klik node `Pointer B` di Sidebar Category Tree
12. Centang checkbox baris `Pointer A`
13. Klik `[Delete]` pada Bulk Action Bar
14. Verifikasi dialog D-13 dengan body `These categories (or their subcategories) are still used by 1 Asset Name template in Asset Master. Update Asset Master before deleting.`
15. Klik `[OK]`
16. Klik icon (×) pada Bulk Action Bar
17. Klik node `All Categories` di Sidebar Category Tree

### TC-FA-CAT-251: Node dengan descendant ditunjuk Asset Name masuk kelompok skipped

18. Atur jumlah baris per halaman menjadi 25
19. Centang checkbox baris `Electronics` dan `Vehicle B {runId}-078`
20. Klik `[Delete]` pada Bulk Action Bar
21. Verifikasi dialog D-12 memuat `Vehicle B {runId}-078` pada kelompok yang akan dihapus
22. Verifikasi `Electronics` pada kelompok yang dilewati
23. Verifikasi tidak ada kalimat `The selected categories have ... subcategories` pada kelompok yang akan dihapus
24. Klik `[Cancel]`
25. Klik icon (×) pada Bulk Action Bar

### TC-FA-CAT-250: Bulk Delete campuran, dialog D-12 dua kelompok dan toast T-08

26. Centang checkbox baris `Vehicle A {runId}-078` dan `Tools`
27. Klik `[Delete]` pada Bulk Action Bar
28. Verifikasi dialog `Delete Categories` memuat kelompok `The following will be deleted:` dengan bullet `Vehicle A {runId}-078`
29. Verifikasi kelompok `The following are used by Asset Names and will be skipped:` dengan bullet `Tools`
30. Verifikasi kalimat `Are you sure you want to continue? This action cannot be undone.` dan tombol `[Cancel]` serta `[Continue]`
31. Klik `[Continue]`
32. Verifikasi toast `Success, category has been deleted. Some items were skipped.`
33. Verifikasi `Vehicle A {runId}-078` terhapus
34. Verifikasi `Tools` tetap ada

### TC-FA-CAT-257: Seleksi tepat satu kategori collapse ke dialog single (D-09)

35. Centang checkbox baris `Vehicle B {runId}-078`
36. Klik `[Delete]` pada Bulk Action Bar
37. Verifikasi dialog `Delete Category` D-09 dengan title singular dan satu bullet `Vehicle B {runId}-078` (bukan varian Homogen atau Campuran)
38. Klik `[Delete]`
39. Verifikasi toast `Success, category has been deleted.`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas (fungsional Bulk Delete campuran), satu client, dan berdiri sendiri; delapan langkah di antaranya hanya langkah penghubung (pengaturan halaman, penutupan dialog, pembatalan seleksi).
- Urutan TC: TC-FA-CAT-252, TC-FA-CAT-253, TC-FA-CAT-251, TC-FA-CAT-250, lalu TC-FA-CAT-257. Alasan: dialog yang tidak mengeksekusi mendahului eksekusi, dan eksekusi yang menghapus data di akhir (S-10).
- Langkah penghubung (tanpa `Verifikasi`, S-03/S-09): pengaturan jumlah baris per halaman, `[OK]`, `[Cancel]`, icon (×), klik node All Categories.
- Data milik spec menggantikan `Vehicle` Pre-setup #20 (S-06). Dialog D-09 pada TC-FA-CAT-257 hanya diasersi title dan bullet karena kalimat `...delete it?` tidak tertulis utuh di TC.
- Temuan untuk QA:
  - TC-FA-CAT-250 Post Condition (Changelog hanya mencatat `Vehicle`, skip tidak menulis entri) tidak punya langkah observasi di TC, sehingga tidak diasersi.
  - TC-FA-CAT-253 mensyaratkan Pre-setup #39; diikuti sesuai Precondition (ACC hanya #20).

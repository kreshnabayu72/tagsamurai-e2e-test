---
id: TC-FA-CAT-E2E-028-new-subcategory-validasi-category-name-wajib-spasi-panjang-trim
title: "New Subcategory: Validasi Category Name Wajib, Hanya Spasi, Batas Panjang 120, dan Trim"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-81
  - TC-FA-CAT-82
  - TC-FA-CAT-83
  - TC-FA-CAT-84
  - TC-FA-CAT-519
coverage:
  web: automated
---

# New Subcategory: Validasi Category Name Wajib, Hanya Spasi, Batas Panjang 120, dan Trim

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang dipaksa lewat `Spectra.intercept()`.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settingsCategories.totalControl` (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`, client CatMain (Pre-setup #20). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan; keputusan tim).
- Data Pre-setup: client CatMain (Pre-setup #20); baris `Peripheral` (level 1) dipakai sebagai parent dan hanya dibaca.
- Data milik spec: dua subkategori di bawah `Peripheral` yang dibuat lewat UI: `NamaA120` (TC-FA-CAT-83) dan `NamaB120` (TC-FA-CAT-519, spasi akhir dibuang). Keduanya tepat 120 karakter dan unik per run (S-12): `NamaA120` = `A` sebanyak (120 dikurangi panjang `-{runId}-028`) diikuti `-{runId}-028`; `NamaB120` = `B` sebanyak jumlah yang sama diikuti `-{runId}-028`. Hook `after` menghapus keduanya lewat API berdasarkan nama.
- Nilai bantu `VAL81` (Code) dan `Desc 81` (Description) hanya diketik pada TC-FA-CAT-81 untuk mengamati klausa "input lain dipertahankan"; tidak ada kategori yang tersimpan dengan nilai itu.
- Seed dan pemulihan lewat API, flag Guided Tooltip, dan hook suite lain: lihat `suite.md`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-81: Category Name kosong ditolak setelah Submit (New Subcategory)

1. Klik elipsis (⋯) pada baris `Peripheral`
2. Klik `+ Add Subcategory`
3. Biarkan Category Name kosong, isi Code `VAL81` dan Description `Desc 81` (nilai bantu agar klausa "input lain dipertahankan" teramati; nilai ini tidak ada di Data Uji TC)
4. Klik `[Submit]`
5. Verifikasi error inline `Category name must not be empty` tampil setelah klik `[Submit]`
6. Verifikasi popup tetap terbuka
7. Verifikasi Code tetap `VAL81`
8. Verifikasi Description tetap `Desc 81`
9. Verifikasi tidak ada kategori tersimpan (toast sukses tidak tampil)
10. Kosongkan Code dan Description

### TC-FA-CAT-82: Category Name yang hanya berisi spasi diperlakukan kosong dan ditolak (New Subcategory)

11. Isi Category Name dengan 5 karakter spasi
12. Klik `[Submit]`
13. Verifikasi error inline `Category name must not be empty` tampil
14. Verifikasi popup tetap terbuka
15. Verifikasi tidak ada kategori tersimpan (toast sukses tidak tampil)

### TC-FA-CAT-84: Category Name 121 karakter menampilkan error langsung tanpa memotong ketikan (New Subcategory)

16. Ganti Category Name dengan 121 karakter `A` tanpa menekan Submit
17. Verifikasi border field `severity="danger"` tampil langsung saat melebihi batas
18. Verifikasi pesan `Max. 120 characters` tampil langsung saat melebihi batas
19. Verifikasi seluruh 121 karakter tetap tertulis di field (ketikan tidak dipotong)
20. Klik `[Submit]`
21. Verifikasi Submit diblok: popup tetap terbuka
22. Verifikasi tidak ada kategori tersimpan (toast sukses tidak tampil)

### TC-FA-CAT-83: Category Name tepat 120 karakter diterima (New Subcategory)

23. Ganti Category Name dengan `NamaA120`
24. Verifikasi tidak ada error `Max. 120 characters`
25. Klik `[Submit]`
26. Verifikasi toast `Success, category has been created.` tampil
27. Klik node `Peripheral` pada sidebar
28. Verifikasi subkategori `NamaA120` (120 karakter) tersimpan penuh di bawah `Peripheral`

### TC-FA-CAT-519: Add Subcategory: panjang Category Name dihitung setelah trim, spasi tepi tidak menimbulkan error

29. Klik node `All Categories` pada sidebar (kembali ke daftar level 1 agar baris `Peripheral` tampil)
30. Klik elipsis (⋯) pada baris `Peripheral`
31. Klik `+ Add Subcategory`
32. Isi Category Name dengan `NamaB120` diikuti 5 spasi di akhir
33. Verifikasi tidak ada error `Max. 120 characters` (kelebihan hanya spasi tepi)
34. Klik `[Submit]`
35. Verifikasi toast `Success, category has been created.` tampil
36. Klik node `Peripheral` pada sidebar
37. Verifikasi subkategori tersimpan sebagai `NamaB120` (120 karakter) tanpa spasi akhir di bawah `Peripheral`

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan dan penggabungan form (S-10, prinsip 6): validasi diblokir (TC-FA-CAT-81, 82, 84) sebelum aksi sukses (TC-FA-CAT-83, 519). TC-FA-CAT-82, 84, dan 83 membuka popup baru pada langkah pertamanya; spec memakai satu sesi popup dari TC-FA-CAT-81 dengan mengganti isi Category Name (langkah 11, 16, 23). Jumlah buka form (langkah 1 dan 30) sama dengan jumlah kejadian menutup (Submit sukses langkah 25 dan 34).
- Langkah penghubung (S-03, S-14, R-12): langkah 10 (mengosongkan Code dan Description bantu), langkah 11, 16, dan 23 sekaligus mengganti nilai input sehingga error inline sebelumnya tidak terbawa ke TC berikutnya; langkah 27 dan 36 (memilih node parent untuk melihat anak); langkah 29 (kembali ke `All Categories` karena baris `Peripheral` tidak ada di tabel saat node `Peripheral` terpilih).
- Penyimpangan data (S-12, R-06): TC menyebut "120 karakter `A`" dan "120 karakter `B`"; spec memakai `NamaA120` dan `NamaB120` (tetap tepat 120 karakter, diakhiri `-{runId}-028`) agar unik per run.
- Temuan untuk QA:
  - TC-FA-CAT-81 dan TC-FA-CAT-82 menyebut "tidak ada kategori tersimpan" tanpa langkah observasi; spec mengasersi lewat popup yang tetap terbuka dan tidak adanya toast sukses.
  - TC-FA-CAT-81 butir b menyebut "input lain dipertahankan" tanpa Data Uji untuk input lain; spec mengisi Code `VAL81` dan Description `Desc 81` sebagai nilai bantu (langkah penghubung) agar klausa itu dapat diasersi.
  - TC-FA-CAT-83 Expected b ("tersimpan penuh") dan TC-FA-CAT-519 Expected b tidak memberi langkah observasi; spec mengasersi lewat pemilihan node `Peripheral` di sidebar (langkah 27 dan 36) dan tabel anak.
  - TC-FA-CAT-83 dan TC-FA-CAT-519 menyebut nama 120 karakter murni `A` dan `B`; spec memakai nama 120 karakter berakhiran suffix run agar unik (S-12).
- Spec melewati 35 langkah (37 langkah). Alasan: satu kelas harness dan satu dataset; langkah penghubung wajib (S-03, S-08, S-09) menambah langkah dan blok berdiri sendiri.

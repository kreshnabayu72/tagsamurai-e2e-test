---
id: TC-FA-CAT-E2E-070-delete-diblok-would-empty-d-06-catfresh-dan-catdeep
title: "Delete Diblok Would-Empty (D-06 dan D-10): Client CatFresh dan CatDeep"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-223
  - TC-FA-CAT-259
  - TC-FA-CAT-225
  - TC-FA-CAT-256
  - TC-FA-CAT-224
  - TC-FA-CAT-255
coverage:
  web: automated
---

# Delete Diblok Would-Empty (D-06 dan D-10): Client CatFresh dan CatDeep

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang di-mock.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatFresh (Pre-setup #25) dengan `{namaCompany}` client CatFresh, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini (akun pertama spec bukan akun default suite); halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite.
- Akun aktor kedua (TC-224 dan TC-255): Total Control (Pre-setup #1) client CatDeep (Pre-setup #26) dengan `{namaCompany}` client CatDeep, password `Spectra.env.FA_TC_PASSWORD`. Login lewat langkah ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup yang dibaca dan tidak diubah (seluruh aksi Delete di spec ini diblokir guard Would-Empty sehingga data dan Last Updated tidak berubah, S-06):
  - CatFresh (#25) keadaan dasar: hanya `Default Category` (Code `DC`, leaf). Hook `before` memastikan keadaan dasar dan hook `after` memulihkannya lewat seed API (disediakan tim FE).
  - Varian CatFresh yang diatur lewat seed API di langkah penghubung (disediakan tim FE, tanpa endpoint karangan): varian A `Default Category` ditunjuk Asset Name `Seed Item` (TC-225); varian B dua kategori `Used One` (ditunjuk Asset Name) dan `Free One`, tanpa `Default Category` (TC-256).
  - CatDeep (#26, plan Professional): rantai `Level One` > `Level Two` > `Level Three` > `Level Four` > `Level Five`, seluruh tree adalah satu family `Level One`.
- Kemampuan teknis: pemilihan baris lewat checkbox dan Bulk Action Bar pada tabel Categories List.
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-223: Delete kategori tunggal client diblok D-06 (Would-Empty, node tanpa subkategori)

1. Klik elipsis (⋯) pada baris `Default Category` > `Delete`
2. Verifikasi dialog `Cannot Delete Category` dengan bullet `Default Category`, body `This is your only category. You must have at least one category — create another one before deleting this.`, dan tombol `[OK]`
3. Verifikasi tidak ada toast
4. Verifikasi kategori tidak terhapus: baris `Default Category` tetap tampil di tabel
5. Klik `[OK]`

### TC-FA-CAT-259: Seleksi satu kategori tunggal client collapse ke dialog D-06

6. Centang checkbox baris `Default Category`
7. Klik `[Delete]` pada Bulk Action Bar
8. Verifikasi dialog D-06 `Cannot Delete Category` dengan body `This is your only category. You must have at least one category — create another one before deleting this.` tampil
9. Verifikasi dialog D-10 `Cannot Delete Categories` tidak tampil
10. Klik `[OK]`
11. Hilangkan centang baris `Default Category`

### TC-FA-CAT-225: Urutan guard: Would-Empty dievaluasi sebelum In-Use

12. Siapkan varian A CatFresh: `Default Category` ditunjuk Asset Name `Seed Item` (seed API), lalu muat ulang halaman
13. Klik elipsis (⋯) pada baris `Default Category` > `Delete`
14. Verifikasi dialog yang tampil D-06 (`This is your only category. You must have at least one category — create another one before deleting this.`) dan bukan D-07
15. Verifikasi hanya satu dialog blok yang tampil
16. Klik `[OK]`

### TC-FA-CAT-256: Would-Empty dicek paling awal walau sebagian baris sedang dipakai Asset Name

17. Siapkan varian B CatFresh: dua kategori `Used One` (ditunjuk Asset Name) dan `Free One` (seed API), lalu muat ulang halaman
18. Centang checkbox baris `Used One` dan `Free One`
19. Klik `[Delete]` pada Bulk Action Bar
20. Verifikasi dialog yang tampil D-10 `Cannot Delete Categories` dengan body `You've selected all remaining categories. At least one category must always exist — deselect at least one category and try again.` (blok seluruh aksi), bukan D-12 atau D-13
21. Klik `[OK]`
22. Hilangkan centang baris `Used One` dan `Free One`

### Ganti akun ke client CatDeep

23. Logout
24. Login sebagai Total Control client CatDeep (Pre-setup #26)
25. Buka Fixed Asset > Settings > Categories

### TC-FA-CAT-224: Delete root yang family-nya seluruh tree diblok D-06 varian subkategori

26. Klik elipsis (⋯) pada baris `Level One` > `Delete`
27. Verifikasi dialog `Cannot Delete Category` dengan bullet `Level One`, body `Deleting this category and its subcategories would leave you with no category. You must have at least one category — create another one before deleting this.`, dan tombol `[OK]`
28. Verifikasi tidak ada node yang terhapus: baris `Level One` tetap tampil di tabel
29. Klik `[OK]`

### TC-FA-CAT-255: Would-Empty gabungan: seleksi induk dan anak yang bersama menghabiskan seluruh tree diblok D-10

30. Pada node `All Categories`, centang checkbox baris `Level One`
31. Klik node `Level One` di sidebar untuk membuka anaknya
32. Centang checkbox baris `Level Two`
33. Klik `[Delete]` pada Bulk Action Bar
34. Verifikasi dialog D-10 `Cannot Delete Categories` tampil (seleksi gabungan lintas node menyisakan 0 kategori)
35. Verifikasi tidak ada yang terhapus: baris `Level Two` tetap tampil di tabel
36. Klik `[OK]`
37. Hilangkan centang baris `Level Two`
38. Klik node `All Categories` di sidebar
39. Hilangkan centang baris `Level One`

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-223, TC-259, TC-225, TC-256, TC-224, dan TC-255 ada di spec ini.
- Spec ini melewati sekitar 35 langkah karena Expected ditulis per klausa (S-01) dan ada ganti akun ke client CatDeep. Keenam blok berkelas fungsional yang sama (guard Would-Empty), tiap blok berdiri sendiri pada varian atau client sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC: TC-259 ditulis sebelum TC-225 agar varian CatFresh yang membutuhkan seeding (TC-225, lalu TC-256) berurutan tanpa memulihkan keadaan dasar di antaranya (S-10); client CatDeep di akhir karena ganti akun (S-07).
- Penyesuaian data (S-06): seluruh aksi Delete diblokir guard sehingga baris Pre-setup `Default Category`, `Used One`, `Free One`, `Level One`, dan `Level Two` tidak diubah; tidak ada data milik spec.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): menghilangkan centang seleksi (S-09); menyiapkan varian CatFresh dan memuat ulang halaman; ganti akun ke client CatDeep (Logout, Login, buka halaman); memilih node di sidebar.
- Temuan untuk QA:
  - TC-259 Expected mengutip D-06 terpotong (`This is your only category...`); spec memakai teks lengkap D-06 PRD §6 dan memeriksa dialog D-10 tidak tampil.
  - TC-256 dan TC-255 hanya menyebut "dialog D-10" tanpa teks; spec memakai title `Cannot Delete Categories` dan body dari PRD §6 D-10.
  - TC-225 dan TC-256 memakai varian Pre-setup #25 (`Seed Item`; `Used One` dan `Free One`) yang tidak ada di keadaan dasar; seeding varian dan pemulihan keadaan dasar disediakan tim FE (S-13).
  - TC-255 Expected hanya menyebut "tidak ada yang terhapus"; spec mengasersi baris `Level Two` tetap tampil di tabel.

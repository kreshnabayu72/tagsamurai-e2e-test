---
id: TC-AC-DC-E2E-048-delete-diblok-referensi-descendant-dan-device-sku
title: "Delete Category: Diblok oleh Referensi pada Descendant, Klik Backdrop, dan Sub-tab Device SKU"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-135
  - TC-AC-DC-274
  - TC-AC-DC-266
  - TC-AC-DC-271
coverage:
  web: automated
---

# Delete Category: Diblok oleh Referensi pada Descendant, Klik Backdrop, dan Sub-tab Device SKU

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup yang hanya dibaca dan tidak pernah diubah (Delete selalu diblokir guard; pengecualian S-06 untuk Pre-setup in-use yang dirancang TC untuk blokir): pohon #14 node `Filter Induk` > `Filter Anak 2` > `Filter Cucu` dan `Dipakai Leaf` di bawah `Hardware` > `Handheld Reader`; Device Name Pre-setup #15 `FN-2` (Category `Filter Cucu`) dan `HR-100` (`Dipakai Leaf`). Nama node dan Device Name dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE). Spec tidak mengubah data Pre-setup; Last Updated tidak berubah.
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-048`): family `Keluarga {runId}-048` dengan anak `Anak A {runId}-048` (leaf) dan `Anak B {runId}-048`, serta cucu `Cucu {runId}-048` di bawah `Anak B {runId}-048`; Device Name `DEEP-1 {runId}-048` dengan Category `Cucu {runId}-048` (Dinamis #5 TC). Hook `after` menghapus Device Name `DEEP-1 {runId}-048` lalu `Keluarga {runId}-048` beserta seluruh descendant lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: pembuatan Device Name `DEEP-1 {runId}-048` lewat sesi API aktor (kolom wajib selain Category tidak disebut TC; disediakan tim FE/BE tanpa endpoint karangan). Jumlah total entri Changelog dibaca sebagai baseline sebelum aksi (kemampuan baca jumlah total disediakan tim FE/BE).

## Test Steps

### Baseline Changelog

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik ikon Changelog pada header Sidebar Category
3. Catat jumlah total entri Changelog sebagai baseline
4. Klik `[×]` pada modal Changelog

### Delete diblok oleh referensi pada descendant saja (TC-135)

5. Expand `Filter Induk`
6. Hover node `Filter Anak 2`, klik aksi Delete
7. Verifikasi dialog blok "Cannot Delete Category" memuat bullet `FN-2` (Device Name pada `Filter Cucu`)
8. Verifikasi isi dialog memuat teks "This category (or one of its subcategories) is still used by a device name. Remove the reference before deleting."
9. Klik `[OK]`
10. Verifikasi `Filter Anak 2` dan `Filter Cucu` tetap ada tanpa penghapusan sebagian

### Delete diblok oleh referensi pada cucu (TC-274)

11. Expand `Keluarga {runId}-048` dan `Anak B {runId}-048`
12. Hover node `Keluarga {runId}-048`, klik aksi Delete
13. Verifikasi dialog blok "Cannot Delete Category" memuat bullet `DEEP-1 {runId}-048`
14. Verifikasi isi dialog memuat teks "This category (or one of its subcategories) is still used by a device name. Remove the reference before deleting."
15. Verifikasi hanya satu tombol `[OK]`
16. Klik `[OK]`
17. Verifikasi `Keluarga {runId}-048`, `Anak A {runId}-048`, `Anak B {runId}-048`, dan `Cucu {runId}-048` tetap ada

### Klik backdrop tidak menutup dialog blok (TC-266)

18. Hover node `Dipakai Leaf`, klik aksi Delete
19. Klik area backdrop di luar dialog
20. Verifikasi dialog blok "Cannot Delete Category" tetap terbuka
21. Klik `[OK]`
22. Verifikasi dialog tertutup
23. Verifikasi node `Dipakai Leaf` tetap ada
24. Verifikasi tidak ada toast

### Delete diblok lewat sub-tab Device SKU (TC-271)

25. Buka sub-tab `Device SKU` pada Settings > Device
26. Expand `Hardware` lalu `Handheld Reader`
27. Hover node `Dipakai Leaf`, klik aksi Delete
28. Verifikasi dialog blok "Cannot Delete Category" memuat bullet `HR-100`
29. Verifikasi isi dialog memuat teks "This category (or one of its subcategories) is still used by a device name. Remove the reference before deleting."
30. Verifikasi hanya satu tombol `[OK]`
31. Klik `[OK]`
32. Verifikasi node `Dipakai Leaf` tetap ada

### Pemeriksaan akhir tidak ada entri baru

33. Klik ikon Changelog pada header Sidebar Category
34. Verifikasi jumlah total entri Changelog sama dengan baseline
35. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1, 5, 11, 26 (membuka cabang tree), langkah 4 dan 35 (menutup modal Changelog), langkah 9, 16, 21, 31 (`[OK]` menutup dialog blok), langkah 25 (membuka sub-tab Device SKU).
- S-05: klausa "tidak ada entri log" pada TC-135, TC-274, TC-266, TC-271 dinyatakan sebagai asersi jumlah dengan baseline (langkah 3 dan 34), bukan asersi absence kelas g. Verifikasi absence toast pada langkah 24 memakai dialog blok yang baru tertutup pada langkah 22 sebagai anchor.
- Spec ini mencapai 35 langkah, di batas smell.
- Temuan untuk QA:
  - Asersi TC-135, TC-266, dan TC-271 bergantung pada nama literal Pre-setup #14 dan #15 (`Filter Anak 2`, `FN-2`, `Dipakai Leaf`, `HR-100`) yang hanya dibaca. Pada TC-274 TC memakai Device Name `DEEP-1` dan node `Hapus Keluarga Cucu` milik automation baseline; spec memakai Device Name dan family milik spec bersuffix `{runId}-048`.
  - TC-271 tidak menyebut apakah dialog blok pada sub-tab Device SKU memiliki perilaku backdrop yang sama; spec hanya mengasersi isi dialog.

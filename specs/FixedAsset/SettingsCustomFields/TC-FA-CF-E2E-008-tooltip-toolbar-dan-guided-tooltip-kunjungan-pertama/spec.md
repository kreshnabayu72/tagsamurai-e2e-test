---
id: TC-FA-CF-E2E-008-tooltip-toolbar-dan-guided-tooltip-kunjungan-pertama
title: "Tooltip Toolbar dan Guided Tooltip Kunjungan Pertama"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-24
  - TC-FA-CF-25
  - TC-FA-CF-26
coverage:
  web: automated
---

# Tooltip Toolbar dan Guided Tooltip Kunjungan Pertama

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11) dengan baseline tab General (Pre-setup #12), dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE); spec hanya membaca dan tidak mengubah data.
- Guided Tooltip (pengecualian atas hook suite): spec ini menguji flag `guided_tooltip_seen_fa-settings-custom-fields` sendiri, sehingga hook `before` suite tidak menyetel flag untuk akun Total Control spec ini. Spec mengatur flag lewat langkah 1, 12, dan 25 (kemampuan membaca dan menyetel flag per akun disediakan tim FE/BE; nilai awal dicatat) dan hook `after` memulihkan nilai awal.
- Kemampuan teknis: hover; fokus dan klik tombol walkthrough; membaca nilai flag Guided Tooltip akun aktor (langkah 32 dan 37).
- State global: flag Guided Tooltip akun Total Control Company Alpha (dipulihkan hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-24: Tooltip icon toolbar dan header kolom Actions

1. Setel flag Guided Tooltip akun Total Control menjadi true lalu muat ulang halaman
2. Arahkan kursor ke icon Search
3. Verifikasi tooltip `Search` tampil pada icon Search
4. Arahkan kursor ke icon Filter
5. Verifikasi tooltip `Filter` tampil pada icon Filter
6. Arahkan kursor ke icon Download
7. Verifikasi tooltip `Download` tampil pada icon Download
8. Arahkan kursor ke icon Changelog
9. Verifikasi tooltip `Changelog` tampil pada icon Changelog
10. Arahkan kursor ke header kolom Actions (⋯)
11. Verifikasi tooltip `Column Visibility` tampil pada header kolom Actions

### TC-FA-CF-25: Guided Tooltip otomatis pada kunjungan pertama dengan empat step

12. Hapus flag Guided Tooltip akun Total Control (belum pernah membuka halaman) lalu muat ulang halaman
13. Verifikasi Step 1 menyorot Tabs Bar dengan Title `Field Groups` dan Description `Switch between field groups to organize and manage your asset custom fields.`
14. Klik `[Next]`
15. Verifikasi Step 2 menyorot tombol `[+ Custom Field]` dengan Title `Add Custom Field` dan Description `Define a new attribute field to capture information specific to your business.`
16. Klik `[Next]`
17. Verifikasi Step 3 menyorot header kolom Scope dengan Title `Scope` dan Description `Shows which assets each field applies to.`
18. Klik `[Next]`
19. Verifikasi Step 4 menyorot header kolom Value Type dengan Title `Value Type` dan Description `Shows how each field's value is filled in: individually per asset or shared from a template.`
20. Verifikasi tombol `[Next]` berubah menjadi `[Done]`
21. Klik `[Done]`
22. Verifikasi walkthrough tertutup
23. Muat ulang halaman
24. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya

### TC-FA-CF-26: Back tersembunyi di step 1, Skip menutup dan menandai seen, replay lewat [?]

25. Hapus flag Guided Tooltip akun Total Control lalu muat ulang halaman
26. Verifikasi Step 1 tidak menampilkan `[Back]`
27. Klik `[Next]`
28. Klik `[Back]`
29. Verifikasi `[Back]` pada Step 2 kembali ke Step 1
30. Klik `[Skip]`
31. Verifikasi walkthrough tertutup
32. Verifikasi flag Guided Tooltip ditandai seen
33. Muat ulang halaman
34. Verifikasi walkthrough tidak muncul otomatis
35. Klik tombol `[?]` di kanan Breadcrumb
36. Verifikasi walkthrough dimulai ulang dari Step 1
37. Verifikasi flag Guided Tooltip seen tidak direset

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (37 langkah). Seluruhnya satu halaman, satu akun, satu dataset (baseline Company Alpha, hanya dibaca), dan satu pengecualian pengaturan flag yang sama; tiap blok TC berdiri sendiri dengan flag yang diatur ulang di awal blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 12, dan 25 (mengatur flag dan memuat ulang halaman; TC-FA-CF-24 butuh flag true supaya walkthrough tidak menutupi hover), langkah 2, 4, 6, 8, 10 (hover untuk mengamati tooltip), dan langkah 23 dan 33 (muat ulang sesuai langkah uji TC).
- Sorotan target, Title, dan Description satu tooltip walkthrough diasersi sebagai satu `Verifikasi` per step (komposit tooltip; Expected TC menyebutnya satu butir per step). Langkah 26 (tidak ada `[Back]`) beranchor Step 1 yang tampil setelah langkah 25.
- Temuan untuk QA:
  - TC-FA-CF-25 Post Condition ("flag bernilai true") tidak punya langkah observasi di TC; tidak diasersi di spec ini (S-01).
  - TC-FA-CF-26 Expected c dan e menyebut "menandai flag seen" dan "flag seen tidak direset" tanpa menyebut cara membaca flag; spec memakai kemampuan baca flag yang disediakan tim FE/BE (langkah 32 dan 37) tanpa mengarang endpoint.

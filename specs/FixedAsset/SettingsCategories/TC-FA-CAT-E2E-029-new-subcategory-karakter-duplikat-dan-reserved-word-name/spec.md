---
id: TC-FA-CAT-E2E-029-new-subcategory-karakter-duplikat-dan-reserved-word-name
title: "New Subcategory: Karakter Simbol, Duplikat Nama Tanpa Beda Huruf dan Trim, serta Reserved Word pada Category Name"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-520
  - TC-FA-CAT-521
  - TC-FA-CAT-522
  - TC-FA-CAT-523
coverage:
  web: automated
---

# New Subcategory: Karakter Simbol, Duplikat Nama Tanpa Beda Huruf dan Trim, serta Reserved Word pada Category Name

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #20 (CatMain), dibaca: parent `Peripheral` (Internal) dengan anak `Keyboard` dan `Mouse`. Tidak ada kategori Pre-setup yang diubah.
- Data Dinamis (dibuat spec, bersuffix `{runId}-029` kecuali dinyatakan lain): subcategory `IT & Network (Core) - 2/3: A+B {runId}-029` (Code `ITNSUB`) dan subcategory `All  Categories` (dua spasi di tengah, literal karena nilainya objek uji; Code `ALLSP2`). Hook `before` menghapus sisa kategori ber-Code `ITNSUB` dan `ALLSP2` di bawah `Peripheral`; hook `after` menghapus kedua subcategory. Kemampuan seed dan pemulihan lewat API disediakan tim FE/BE (butir hook suite di `suite.md`).
- Fixture `fixtures/settings-categories.json` (identitas data Pre-setup #20) disediakan tim FE.
- Jam server dan jam browser sinkron tidak dibutuhkan; spec tidak mengasersi waktu.

## Test Steps

### TC-FA-CAT-521: Duplikasi nama tanpa membedakan huruf besar-kecil dan setelah trim

1. Klik elipsis (⋯) pada baris `Peripheral` > `+ Add Subcategory`
2. Ketik Category Name ` keyboard ` (huruf kecil dengan spasi tepi), lalu tunggu 500ms
3. Verifikasi pesan `Category name already exists` tampil sekitar 500ms setelah berhenti mengetik
4. Klik `[Submit]`
5. Verifikasi Submit diblok: popup New Subcategory tetap terbuka
6. Kosongkan field Category Name

### TC-FA-CAT-522: Reserved word tanpa membedakan huruf besar-kecil dan setelah trim

7. Isi Category Name `all categories ` (huruf kecil dengan spasi akhir)
8. Klik `[Submit]`
9. Verifikasi pesan `'All Categories' is a reserved name and cannot be used` tampil setelah klik `[Submit]`
10. Verifikasi Submit diblok: popup New Subcategory tetap terbuka

### TC-FA-CAT-520: Tanda baca dan simbol umum diizinkan

11. Ganti isi Category Name dengan `IT & Network (Core) - 2/3: A+B {runId}-029`
12. Isi Code `ITNSUB`
13. Verifikasi tidak ada error karakter terlarang pada field Category Name
14. Klik `[Submit]`
15. Klik node `Peripheral` di Sidebar Category Tree
16. Verifikasi baris `Keyboard` dan `Mouse` tampil di tabel
17. Verifikasi subcategory `IT & Network (Core) - 2/3: A+B {runId}-029` tersimpan dengan nama persis seperti diketik
18. Verifikasi tidak ada baris bernama `keyboard` atau `all categories` selain `Keyboard` di bawah `Peripheral`
19. Klik node `All Categories` di Sidebar Category Tree

### TC-FA-CAT-523: Dua spasi di tengah nama reserved tidak dinormalisasi

20. Klik elipsis (⋯) pada baris `Peripheral` > `+ Add Subcategory`
21. Isi Category Name `All  Categories` (dua spasi di tengah) dan Code `ALLSP2`
22. Klik `[Submit]`
23. Verifikasi toast `Success, category has been created.` tampil
24. Verifikasi tidak ada error reserved word
25. Klik node `Peripheral` di Sidebar Category Tree
26. Verifikasi subcategory `All  Categories` tersimpan di bawah `Peripheral`
27. Klik node `All Categories` di Sidebar Category Tree

## Notes

- Langkah penghubung (S-03): langkah 6 (mengosongkan field antar-TC, R-12), langkah 11 (mengganti isi field), langkah 15, 19, 25, 27 (pindah node sidebar untuk membaca hasil dan kembali ke layar awal).
- Urutan TC: validasi yang diblokir (521, 522) mendahului aksi sukses (520, 523) (S-10). Satu pembukaan popup dipakai untuk 521, 522, dan 520; TC-523 membuka popup kedua karena popup pertama tertutup oleh Submit sukses.
- Bukti "tidak ada subcategory tersimpan" untuk TC-521 dan TC-522 dibaca di langkah 16 sampai 18 (baris pembanding `Keyboard` dan `Mouse` sebagai anchor).
- Nama `All  Categories` memakai literal tanpa suffix karena nilai itu objek uji; pembersihan Code `ALLSP2` dijamin hook `before` dan `after`.
- Temuan untuk QA:
  - TC-521 dan TC-522 menyebut "Submit diblok" tanpa menyebut wujud pemblokiran; spec mengasersi popup tetap terbuka.
  - TC-523 tidak menyebut asersi posisi baris; hanya subcategory tersimpan yang diasersi.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.

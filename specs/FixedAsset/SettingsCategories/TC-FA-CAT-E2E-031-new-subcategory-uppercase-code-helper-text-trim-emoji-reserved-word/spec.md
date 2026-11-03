---
id: TC-FA-CAT-E2E-031-new-subcategory-uppercase-code-helper-text-trim-emoji-reserved-word
title: "New Subcategory: Uppercase Code, Helper Text, Trim, Emoji, Reserved Word, dan Description Bebas"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-524
  - TC-FA-CAT-525
  - TC-FA-CAT-526
  - TC-FA-CAT-141
  - TC-FA-CAT-142
  - TC-FA-CAT-143
  - TC-FA-CAT-144
coverage:
  web: automated
---

# New Subcategory: Uppercase Code, Helper Text, Trim, Emoji, Reserved Word, dan Description Bebas

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #20 (CatMain), dibaca: parent `Peripheral` (Internal) dengan anak `Keyboard` dan `Mouse`.
- Data Dinamis (dibuat spec): `Sub Desc Free {runId}-031` (Description `Catatan @#%& (uji) / 100% <ok>`) dan `Sub Trim {runId}-031` (Code `STRIM`, input dengan spasi tepi). Hook `before` menghapus sisa kategori ber-Code `STRIM`; hook `after` menghapus kedua subcategory. Seed dan pemulihan lewat API disediakan tim FE/BE (butir hook suite di `suite.md`).
- Kemampuan teknis: paste teks emoji ke field dan injeksi value langsung ke DOM field Category Name (melewati filter keystroke FE) lewat kemampuan browser automation.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-525: Helper text Code

1. Klik elipsis (⋯) pada baris `Peripheral` > `+ Add Subcategory`
2. Verifikasi helper text `Letters, numbers, hyphens, underscores, and dots only` tampil di bawah field Code sejak popup dibuka
3. Ketik Code `A!`
4. Verifikasi helper text digantikan `Code contains invalid characters` selama error aktif
5. Hapus karakter `!` dari Code
6. Verifikasi helper text `Letters, numbers, hyphens, underscores, and dots only` tampil kembali

### TC-FA-CAT-524: Code di-uppercase otomatis

7. Ganti isi Code dengan `ab-1_c.d`
8. Verifikasi field Code menampilkan `AB-1_C.D`
9. Verifikasi tidak ada error pada field Code
10. Kosongkan field Code

### TC-FA-CAT-142: Emoji diblok di level input

11. Paste teks `Sub 🔥` pada Category Name
12. Verifikasi hanya `Sub ` yang masuk ke field Category Name
13. Verifikasi tidak ada pesan error pada field Category Name
14. Kosongkan field Category Name

### TC-FA-CAT-143: Emoji yang lolos filter FE ditolak server

15. Injeksi value `Sub 🔥` langsung ke DOM field Category Name (melewati filter keystroke FE)
16. Klik `[Submit]`
17. Verifikasi pesan inline `Category name contains invalid characters` tampil
18. Kosongkan field Category Name

### TC-FA-CAT-144: Reserved word All Categories

19. Isi Category Name `ALL CATEGORIES`
20. Klik `[Submit]`
21. Verifikasi pesan inline `'All Categories' is a reserved name and cannot be used` tampil setelah klik `[Submit]`

### TC-FA-CAT-526: Description bebas karakter

22. Ganti isi Category Name dengan `Sub Desc Free {runId}-031`
23. Isi Description `Catatan @#%& (uji) / 100% <ok>`
24. Klik `[Submit]`
25. Klik node `Peripheral` di Sidebar Category Tree
26. Verifikasi baris `Keyboard`, `Mouse`, dan `Sub Desc Free {runId}-031` tampil
27. Verifikasi tidak ada baris bernama `Sub 🔥` atau `ALL CATEGORIES` di bawah `Peripheral`
28. Buka Popup Detail `Sub Desc Free {runId}-031`
29. Verifikasi Description tampil persis `Catatan @#%& (uji) / 100% <ok>`
30. Tutup Popup Detail

### TC-FA-CAT-141: Category Name disimpan ter-trim

31. Klik elipsis (⋯) pada node `Peripheral` di sidebar > `+ Add Subcategory`
32. Isi Category Name `  Sub Trim {runId}-031  ` (spasi awal dan akhir) dan Code `STRIM`
33. Klik `[Submit]`
34. Verifikasi subcategory tersimpan sebagai `Sub Trim {runId}-031` tanpa spasi tepi di bawah `Peripheral`

## Notes

- Alasan sekitar 35 langkah: seluruh TC satu topik (field New Subcategory pada parent `Peripheral`), tiap blok dimulai dari field kosong dan berdiri sendiri.
- Urutan: TC-525 mendahului TC-524 karena helper text hanya teramati sejak popup baru dibuka (8b butir 5); validasi diblok (142, 143, 144) mendahului aksi sukses (526, 141) (S-10).
- Langkah penghubung (S-03): langkah 10, 14, 18 (mengosongkan field antar-TC, R-12); langkah 22 (mengganti isi field); langkah 25 dan 30 (membaca hasil dan menutup Popup Detail).
- Bukti "tidak ada subcategory tersimpan" untuk TC-143 dan TC-144 dibaca di langkah 26 sampai 27 (baris pembanding sebagai anchor).
- Temuan untuk QA:
  - TC-142 dan TC-143 tidak menyebut Code; Submit pada TC-143 hanya ditahan oleh pesan Category Name.
  - TC-144 tidak menyebut hasil pada tabel; ditutup oleh langkah 27.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.

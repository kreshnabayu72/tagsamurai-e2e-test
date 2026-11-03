---
id: TC-FA-CAT-E2E-052-edit-validasi-emoji-duplikat-reserved-word-dan-nama-sendiri
title: "Edit Category: Emoji, Nama Duplikat Sibling, Reserved Word All Categories, dan Nama Sendiri"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-181
  - TC-FA-CAT-182
  - TC-FA-CAT-183
  - TC-FA-CAT-184
  - TC-FA-CAT-185
  - TC-FA-CAT-533
  - TC-FA-CAT-534
coverage:
  web: automated
---

# Edit Category: Emoji, Nama Duplikat Sibling, Reserved Word All Categories, dan Nama Sendiri

## Prerequisites

- Mode: FE+BE (backend nyata; validasi server dan state tersimpan diasersi lewat UI dan pembacaan state BE).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #20 (CatMain): baris `Furniture` (Code `FURN`, leaf, Total Asset 5) dibuka di popup Edit; `Tools` (Code `TOOL`, level 1) menjadi sibling pembanding duplikat. Semua blok ditolak atau tidak disimpan, sehingga data Pre-setup dan Last Updated tidak berubah (S-06).
- Kemampuan teknis: menyuntikkan nilai langsung ke DOM field Category Name tanpa keystroke (TC-FA-CAT-182, bypass filter FE); membaca state BE kategori `Furniture`; disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`).
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-181: Emoji pada Category Name diblok di level input

1. Klik elipsis (⋯) pada baris `Furniture` > `Edit`
2. Paste teks `Furn 😊` pada Category Name
3. Verifikasi hanya `Furn ` yang masuk ke field
4. Verifikasi tidak ada pesan error

### TC-FA-CAT-182: Emoji yang lolos filter FE ditolak server

5. Injeksi value `Furn 😊` langsung ke DOM field Category Name (bypass keystroke filter FE)
6. Klik `[Save]`
7. Verifikasi pesan inline `Category name contains invalid characters` tampil
8. Verifikasi tidak ada perubahan tersimpan (dibaca dari state BE)

### TC-FA-CAT-183: Nama duplikat sibling ditolak real-time

9. Ubah Category Name menjadi `Tools`
10. Tunggu 500ms
11. Verifikasi pesan `Category name already exists` tampil sekitar 500ms setelah berhenti mengetik
12. Klik `[Save]`
13. Verifikasi Save diblok: popup tetap terbuka dan `Furniture` tidak berubah (dibaca dari state BE)

### TC-FA-CAT-184: Mengetik nama diri sendiri tidak dianggap duplikat

14. Hapus Category Name lalu ketik ulang `Furniture`
15. Tunggu 500ms
16. Verifikasi pesan `Category name already exists` tidak tampil

### TC-FA-CAT-185: Reserved word All Categories ditolak setelah Save

17. Ubah Category Name menjadi `all categories`
18. Klik `[Save]`
19. Verifikasi pesan `'All Categories' is a reserved name and cannot be used` tampil
20. Verifikasi tidak ada perubahan tersimpan (dibaca dari state BE)

### TC-FA-CAT-533: Duplikasi nama tanpa membedakan huruf besar-kecil dan setelah trim

21. Ubah Category Name menjadi ` tools ` (huruf kecil dengan spasi tepi)
22. Tunggu 500ms
23. Verifikasi pesan `Category name already exists` tampil sekitar 500ms setelah berhenti mengetik
24. Klik `[Save]`
25. Verifikasi Save diblok: popup tetap terbuka dan nilai tersimpan tidak berubah (dibaca dari state BE)

### TC-FA-CAT-534: Reserved word tanpa membedakan huruf besar-kecil dan setelah trim

26. Ubah Category Name menjadi `all categories ` (huruf kecil dengan spasi akhir)
27. Klik `[Save]`
28. Verifikasi pesan `'All Categories' is a reserved name and cannot be used` tampil setelah klik `[Save]`
29. Verifikasi tidak ada perubahan tersimpan (dibaca dari state BE)
30. Klik icon close (✕)
31. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
32. Klik `[Leave]`

## Notes

- Mode: FE+BE. Tujuh blok berdiri sendiri (validasi Category Name pada satu popup Edit tanpa Save sukses) dan memakai popup yang sama; popup dipakai berulang tanpa dibuka ulang karena semua kasus ditolak atau tidak menutup popup.
- Langkah penghubung (S-03, S-08, S-09, R-12): langkah 30 sampai 32 (menutup form dirty secara deterministik); pergantian isi Category Name antar blok menghapus pesan error sebelumnya, dan pesan identik (reserved word, langkah 19 dan 28; duplikat, langkah 11 dan 23) dipisahkan oleh blok berpesan lain.
- Langkah 24 menambahkan klik `[Save]` yang tidak tertulis di langkah TC-FA-CAT-533, karena Expected "Save diblok" membutuhkan aksi Save (S-03).
- Pengecualian `P-5`: TC-FA-CAT-182 (kelas a, injeksi DOM yang melewati filter FE) adalah satu-satunya TC objek-uji ringan kelas a di spec fungsional ini dan tidak memakai harness eksternal maupun state berat.
- Temuan untuk QA:
  - TC-FA-CAT-533 tidak menyertakan langkah klik `[Save]` padahal Expected b menyebut "Save diblok"; spec menambah klik Save (langkah 24).
  - TC-FA-CAT-184 hanya menyatakan ketiadaan pesan; ketiadaan itu diasersi setelah mengetik ulang nama sendiri tanpa menyimpan.
  - TC-FA-CAT-182 menyebut bypass filter FE tanpa menyebut mekanisme injeksi DOM; mekanisme ditulis sebagai kemampuan disediakan tim FE/BE (S-13).

---
id: TC-FA-CAT-E2E-025-new-category-karakter-name-duplikat-sibling-case-insensitive
title: "New Category: Karakter Category Name, Duplikat Sibling, dan Pencocokan Case-Insensitive"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-87
  - TC-FA-CAT-88
  - TC-FA-CAT-89
  - TC-FA-CAT-90
  - TC-FA-CAT-92
  - TC-FA-CAT-93
coverage:
  web: automated
---

# New Category: Karakter Category Name, Duplikat Sibling, dan Pencocokan Case-Insensitive

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang dipaksa lewat `Spectra.intercept()`. Penolakan emoji oleh server (TC-FA-CAT-88) dipicu dengan menyuntikkan nilai ke DOM, bukan intercept.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settingsCategories.totalControl` (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`, client CatMain (Pre-setup #20). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan; keputusan tim).
- Data Pre-setup: client CatMain (Pre-setup #20); baris `Furniture` (level 1) menjadi pembanding duplikat dan baris `Peripheral` (level 1) menjadi parent; keduanya hanya dibaca.
- Data milik spec: kategori level 1 `IT & Network (Core) - 2/3: A+B {runId}-025` (TC-FA-CAT-89) dan subkategori `Furniture` dengan Code `PF1` di bawah `Peripheral` (TC-FA-CAT-93; nama dan Code literal sesuai TC). Hook `after` menghapus keduanya lewat API.
- Kemampuan teknis: mengetik emoji dan paste teks ber-emoji ke input; menyuntikkan value langsung ke DOM field (bypass filter keystroke FE) disediakan tim FE.
- Seed dan pemulihan lewat API, flag Guided Tooltip, dan hook suite lain: lihat `suite.md`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-87: Emoji pada Category Name diblok di level input (keystroke dan paste)

1. Klik `[+] Category` pada sidebar
2. Ketik karakter emoji `😊` pada Category Name
3. Verifikasi emoji tidak masuk ke field
4. Paste teks `Cat 😊` pada Category Name
5. Verifikasi field hanya berisi `Cat `
6. Verifikasi tidak ada pesan error pada Category Name

### TC-FA-CAT-88: Emoji yang lolos filter FE ditolak server dengan pesan fallback

7. Kosongkan Category Name
8. Suntikkan value `Fallback 😊` langsung ke DOM field Category Name (bypass filter keystroke FE)
9. Klik `[Submit]`
10. Verifikasi pesan inline `Category name contains invalid characters` tampil
11. Verifikasi tidak ada kategori tersimpan dan popup tetap terbuka (toast sukses tidak tampil)

### TC-FA-CAT-90: Nama duplikat di antara sibling ditolak real-time dengan debounce (New Category)

12. Ganti Category Name dengan `Furniture`, lalu tunggu 500ms tanpa berpindah fokus
13. Verifikasi pesan `Category name already exists` tampil sekitar 500ms setelah berhenti mengetik tanpa menunggu kursor keluar dari field
14. Klik `[Submit]`
15. Verifikasi Submit diblok dan tidak ada kategori tersimpan (popup tetap terbuka, toast sukses tidak tampil)

### TC-FA-CAT-92: Duplikasi nama dinilai tanpa membedakan huruf besar-kecil dan setelah trim

16. Ganti Category Name dengan ` furniture ` (huruf kecil dengan spasi tepi), lalu tunggu 500ms
17. Verifikasi pesan `Category name already exists` tampil karena `Furniture` sudah ada di level 1

### TC-FA-CAT-89: Tanda baca dan simbol umum diizinkan pada Category Name

18. Ganti Category Name dengan `IT & Network (Core) - 2/3: A+B {runId}-025`
19. Klik `[Submit]`
20. Verifikasi toast `Success, category has been created.` tampil
21. Ketik Search `IT & Network (Core) - 2/3: A+B {runId}-025`, tekan Enter
22. Verifikasi kategori tersimpan dengan nama persis seperti diketik tanpa error karakter terlarang

### TC-FA-CAT-93: Nama yang sama di parent berbeda diizinkan

23. Klik elipsis (⋯) pada baris `Peripheral`
24. Klik `+ Add Subcategory`
25. Isi Category Name `Furniture` dan Code `PF1`
26. Verifikasi tidak ada error duplikat karena keunikan per parent (sibling)
27. Klik `[Submit]`
28. Verifikasi toast `Success, category has been created.` tampil
29. Klik node `Peripheral` pada sidebar
30. Verifikasi `Furniture` tampil sebagai anak `Peripheral`

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan dan penggabungan form (S-10, prinsip 6): validasi diblokir (TC-FA-CAT-87, 88, 90, 92) sebelum aksi sukses (TC-FA-CAT-89, 93). TC-FA-CAT-88, 90, 92, dan 89 membuka popup baru pada langkah pertamanya; spec memakai satu sesi popup dari TC-FA-CAT-87 dengan mengganti isi Category Name (langkah 7, 12, 16, 18). Jumlah buka form (langkah 1 dan 23) sama dengan jumlah kejadian menutup (Submit sukses langkah 19 dan 27).
- Langkah penghubung (S-03, R-12, R-16): langkah 7 (mengosongkan field setelah paste), langkah 21 (Search untuk menemukan baris target), langkah 29 (memilih node parent untuk melihat anak).
- Langkah 12 dan 16 menggunakan tunggu 500ms sebagai debounce 500ms yang diuji; asersi pesan memakai polling dengan batas atas pendek (8b butir 5).
- Penyimpangan data (S-06, S-12): TC-FA-CAT-93 memakai nama `Furniture` dan Code `PF1` literal karena nama yang sama dengan sibling lain adalah objek uji; kolisi Code `PF1` antar-run dicegah cleanup `after`.
- Temuan untuk QA:
  - TC-FA-CAT-88 menyebut "injeksi value langsung ke DOM" tanpa mekanisme; spec menyatakannya sebagai kemampuan teknis tim FE (S-13).
  - TC-FA-CAT-92 dan TC-FA-CAT-90 menyebut `Furniture` "sudah ada di level 1" sebagai prasyarat tanpa Pre-setup eksplisit; spec memakai baris seed Pre-setup #20.
  - TC-FA-CAT-89 Post Condition tidak punya langkah observasi selain tanpa error; spec mengasersi tersimpan lewat Search.

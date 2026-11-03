---
id: TC-AC-DC-E2E-015-mobile-android-crud-dan-read-only
title: "Mobile Android: Add dan Edit Memakai Input Inline, Delete dan Unsaved Changes sebagai Bottom Sheet, serta Read Only Tanpa Ikon Aksi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-42
  - TC-AC-DC-302
  - TC-AC-DC-39
coverage:
  mobile: automated
---

# Mobile Android: Add dan Edit Memakai Input Inline, Delete dan Unsaved Changes sebagai Bottom Sheet, serta Read Only Tanpa Ikon Aksi

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android (PRD §4.6 Mobile Layout); data Device Name tampil sebagai Card List.
- Perangkat atau emulator Android dengan aplikasi TAG Samurai Admin Console terpasang (perangkat uji tidak disebut di Pre-setup TC; disediakan tim FE), serta kemampuan mengetuk elemen UI dan menampilkan aksi node pada baris tree. `parallel: false` untuk perangkat fisik bersama.
- Akun: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`, login di hook `before` spec ini (halaman Settings > Device > Device Name dibuka hook `beforeEach` suite). Read Only (Pre-setup #3) `readOnlyDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Rina Wijaya`), password `Spectra.env.AC_DC_RO_PASSWORD` (nama env baru; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Ganti akun ke Read Only ditulis eksplisit pada langkah 23; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup #14 (Pohon Uji Kategori) hanya dibaca. Aksi Add dan Edit pada `Rugged Scanner` hanya membuka input inline lalu menutupnya tanpa submit; aksi Delete diakhiri `[Cancel]`; dialog Unsaved Changes diakhiri `[Leave]`; spec tidak membuat, mengubah, atau menghapus node. Nilai literal diacu lewat `Fixture.settingsDeviceCategory.<kunci>` (`fixtures/settings-device-category.json`, belum ada; ditandai untuk tahap script).
- Pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- State global yang diubah dan dipulihkan: state Open atau Collapsed sidebar per user dan per halaman, serta pilihan filter Category. Hook `before` dan `after` menghapus preferensi sidebar tersimpan akun aktor (kemampuan disediakan tim FE) supaya sidebar tersembunyi pada kunjungan pertama.
- Kondisi awal tiap spec: halaman baru dibuka hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DC-42: Mobile: Add dan Edit memakai input inline, Delete memakai dialog konfirmasi bottom sheet

1. Klik floating toggle pada tepi kanan layar
2. Expand `Hardware` dan `Handheld Reader`
3. Munculkan aksi node `Rugged Scanner`
4. Klik aksi `+ Subcategory`
5. Verifikasi input inline Add terbuka dengan placeholder "Enter category name"
6. Verifikasi input inline Add memiliki tombol `[Submit]` dan `[Clear Field]`
7. Tutup input inline Add
8. Klik aksi Edit pada `Rugged Scanner`
9. Verifikasi input inline Edit berisi nama saat ini "Rugged Scanner"
10. Verifikasi input inline Edit memiliki tombol `[Save]` dan `[Clear Field]`
11. Tutup input inline Edit
12. Klik aksi Delete pada `Rugged Scanner`
13. Verifikasi dialog "Delete Category" tampil sebagai bottom sheet
14. Verifikasi dialog memuat bullet Rugged Scanner dan teks "Are you sure you want to delete it? This action cannot be undone." dengan tombol `[Cancel]` dan `[Delete]`
15. Klik `[Cancel]`

### TC-AC-DC-302: Mobile: dialog Unsaved Changes pada input inline Add tampil sebagai bottom sheet

16. Munculkan aksi node `Rugged Scanner`
17. Klik aksi `+ Subcategory`
18. Ketik `Draft Name` pada input inline Add
19. Klik node `Barcode Handheld`
20. Verifikasi dialog Unsaved Changes tampil sebagai bottom sheet (bukan dialog di tengah layar)
21. Verifikasi dialog memuat teks "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]`
22. Verifikasi node `Draft Name` belum dibuat (node `Rugged Scanner` tampil di tree sebagai anchor)
23. Klik `[Leave]`
24. Klik baris `All Categories`

### TC-AC-DC-39: Mobile: user Read Only tidak melihat ikon aksi per node

25. Ganti akun: logout, lalu login sebagai Read Only (Pre-setup #3) di aplikasi mobile Android
26. Buka halaman `Settings > Device > Device Name`
27. Klik floating toggle pada tepi kanan layar
28. Expand `Hardware` dan `Handheld Reader`
29. Munculkan aksi node pada seluruh baris node yang tampil
30. Verifikasi tidak ada node yang menampilkan ikon aksi untuk user Read Only

## Notes

- Langkah penghubung (S-03): langkah 7 dan 11 menutup input inline yang kosong (tidak dirty); langkah 15 menutup dialog Delete tanpa menghapus; langkah 23 menutup dialog Unsaved Changes lewat `[Leave]` (S-08) dan langkah 24 melepas pilihan filter bila klik node pada langkah 19 diteruskan setelah `[Leave]` (S-09).
- Ganti akun: langkah 25 adalah satu-satunya ganti akun (akun aktor pertama login di hook `before`).
- Temuan untuk QA: (1) TC-AC-DC-42 dan TC-AC-DC-302 tidak menyatakan cara menutup input inline pada mobile (tanpa Esc); langkah 7 dan 11 memakai aksi tutup bawaan input, ditentukan tim FE. (2) TC-AC-DC-302 langkah 5 menyebut "klik node lain" tanpa nama; spec memakai `Barcode Handheld`, dan tidak dinyatakan apakah klik itu diteruskan sebagai pemilihan filter setelah `[Leave]`. (3) TC-AC-DC-39 tidak menyebut cara memunculkan aksi node pada mobile; ditentukan tim FE. (4) Env var password Read Only `AC_DC_RO_PASSWORD` belum terdaftar di konvensi; nama ini dipilih karena nama `AC_RO_PASSWORD` dipakai suite Activity Log untuk akun berbeda (satu nama satu arti).

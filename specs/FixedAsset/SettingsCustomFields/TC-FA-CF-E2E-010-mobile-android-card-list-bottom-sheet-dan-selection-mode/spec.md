---
id: TC-FA-CF-E2E-010-mobile-android-card-list-bottom-sheet-dan-selection-mode
title: "Mobile Android: Card List, Tooltip Disabled, Bottom Sheet, dan Selection Mode"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-29
  - TC-FA-CF-30
  - TC-FA-CF-31
  - TC-FA-CF-32
  - TC-FA-CF-612
  - TC-FA-CF-613
coverage:
  mobile: automated
---

# Mobile Android: Card List, Tooltip Disabled, Bottom Sheet, dan Selection Mode

## Prerequisites

- Mode: FE+BE (aplikasi Android terhadap backend nyata).
- Platform: aplikasi mobile TAG Samurai pada perangkat atau emulator Android (Pre-setup #33, disediakan tim FE); spec tidak berjalan di web (`coverage.mobile`). Perangkat atau emulator dipakai bersama sehingga spec ini `parallel: false`.
- Akun aktor pertama: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha. Login di hook `before` spec ini pada aplikasi Android dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Akun kedua (langkah 30 dan 31, Ganti akun untuk TC-FA-CF-30): Read Only (Pre-setup #3) `readOnly_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_RO_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Nama env baru (`FA_TC_PASSWORD`, `FA_RO_PASSWORD`) didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11) dengan baseline tab General (Pre-setup #12; dipakai: `Equipment Class`, `Asset Serial Tag` Active, `Depreciated Ratio` Inactive), dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE). Spec tidak menyimpan perubahan data: dialog pada TC-FA-CF-613 dibatalkan.
- Kemampuan teknis: tap, long-press, dan membaca bottom sheet, tooltip, serta toast pada aplikasi Android.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`); akun Read Only ikut disetel.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-29: Tabel tampil sebagai card list tanpa Placeholder dan Modified By

1. Verifikasi card `Equipment Class` menampilkan `Field Name` sebagai identifier utama, badge Required, Data Type, Scope, Value Type, switch Active, Value Setting (maksimum dua badge lalu `+N more`), Last Updated, dan ikon `[⋯]`
2. Verifikasi Placeholder dan Modified By tidak tampil di card `Equipment Class`

### TC-FA-CF-612: Toolbar, search bar inline, tombol Create, dan ikon Changelog

3. Verifikasi tombol `[+ Custom Field]` terlihat di bawah toolbar dan di atas card list
4. Verifikasi ikon Changelog berada di header halaman
5. Tap `[⋯]` pada toolbar
6. Verifikasi bottom sheet berisi Column Visibility, Filter, dan Download
7. Tutup bottom sheet
8. Tap `[🔍]`
9. Verifikasi search bar inline terbuka
10. Tutup search bar inline

### TC-FA-CF-31: Modal Create dan Popup All Values sebagai bottom sheet

11. Tap `[+ Custom Field]`
12. Verifikasi modal Create Custom Field tampil sebagai bottom sheet
13. Tutup bottom sheet Create
14. Tap `+1 more` pada card `Equipment Class` kolom Value Setting
15. Verifikasi Popup All Values Preview tampil sebagai bottom sheet
16. Tutup popup All Values Preview

### TC-FA-CF-613: Tap switch Active membuka dialog konfirmasi yang sama dengan web

17. Tap switch Active card `Asset Serial Tag`
18. Verifikasi dialog `Deactivate Custom Field` dengan bullet `• Asset Serial Tag` tampil
19. Tap `[Cancel]`
20. Verifikasi dialog tertutup
21. Verifikasi switch Active card `Asset Serial Tag` kembali ON
22. Tap switch Active card `Depreciated Ratio`
23. Verifikasi dialog `Activate Custom Field` dengan bullet `• Depreciated Ratio` tampil
24. Tap `[Cancel]`

### TC-FA-CF-32: Long-press card masuk selection mode

25. Long-press card `Asset Serial Tag`
26. Verifikasi checkbox muncul di tiap card
27. Verifikasi card `Asset Serial Tag` terpilih
28. Verifikasi Floating Bottom Bulk Bar memuat `[✕]`, penghitung `1 custom field selected`, `[Select All]`, `[Activate]`, `[Deactivate]`, dan `[Delete]`
29. Tap `[✕]` pada Floating Bottom Bulk Bar untuk keluar dari selection mode

### TC-FA-CF-30: Tap elemen Disabled menampilkan tooltip yang hilang otomatis

30. Ganti akun: Logout dari aplikasi Android
31. Login sebagai Read Only (Pre-setup #3) dengan `Spectra.env.FA_RO_PASSWORD`
32. Tap switch Active card `Asset Serial Tag`
33. Verifikasi tooltip `You don't have permission to do this.` tampil
34. Verifikasi tidak ada toast
35. Verifikasi tooltip hilang otomatis

## Notes

- Mode: FE+BE (Android). Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Satu TC universal berlaku untuk web dan mobile; spec ini hanya memuat aturan yang berbeda di mobile. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 29, 612, 31, 613, 32, lalu 30. TC-FA-CF-30 berada di akhir karena memakai akun Read Only (Ganti akun, langkah 30 dan 31); akun aktor pertama adalah Total Control (S-07).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 dan 8 (aksi toolbar sesuai langkah uji TC), langkah 7, 10, 13, 16 (menutup bottom sheet, search bar, dan popup), langkah 24 (membatalkan dialog `Activate Custom Field` supaya status field tidak berubah), dan langkah 29 (keluar dari selection mode).
- Langkah 2 (absence Placeholder dan Modified By) beranchor langkah 1 yang membuktikan card tampil. Langkah 34 (tidak ada toast) ditulis segera setelah pemicu dan sesudah tooltip tampil (langkah 33) sebagai anchor positif (8b butir 11).
- Langkah 28 menulis `[✕]`, penghitung, dan tiga tombol sebagai satu daftar elemen yang disebut utuh oleh Expected TC (komposit Floating Bottom Bulk Bar).
- Temuan untuk QA:
  - TC-FA-CF-613 Langkah Uji 3 ("Tap switch Active card `Depreciated Ratio`") tidak menyebut cara menutup dialog `Activate Custom Field`; spec menutupnya dengan `[Cancel]` (langkah 24) agar tidak mengubah data.
  - TC-FA-CF-30 tidak menyebut cara membuktikan "hilang otomatis" (durasi tooltip); spec mengasersi tooltip hilang tanpa aksi pengguna.

---
id: TC-FA-FAAM-E2E-018-mobile-list-card-bottom-sheet-toolbar-dan-notice
title: "Mobile: Card List, Bottom Sheet Detail, Toolbar, Truncation Badge, Tooltip Tap, dan Notice"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-39
  - TC-FA-FAAM-40
  - TC-FA-FAAM-41
  - TC-FA-FAAM-42
  - TC-FA-FAAM-43
  - TC-FA-FAAM-706
coverage:
  web: unsupported
  mobile: automated
---

# Mobile: Card List, Bottom Sheet Detail, Toolbar, Truncation Badge, Tooltip Tap, dan Notice

## Prerequisites

- Mode: FE+BE (backend nyata), aplikasi FAMS mobile native Android.
- Perangkat: perangkat atau emulator Android dengan aplikasi FAMS terpasang (disediakan tim FE). Perangkat bersama: `parallel: false`.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan akses ke client utama, client downgrade (#20), client Starter (#16), dan client `AutoLocked` (#12c). Login di aplikasi di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya. Hook `after` memulihkan client aktif ke client utama.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.catalog`):
  - Client utama: `Dell Latitude` (#10), `MacBook Pro` (#12, Category Locked), dan Asset Name ber-Category 11 karakter (#14g, `Fixture.faAssetName.category11Item`).
  - Client downgrade (#20): `Excess Gamma` excess.
  - Client Starter tanpa subscription Paid (#16): opsi TAG Type `RFID` terkunci.
  - Client `AutoLocked` (#12c): 30 `Seed Item` dan 3 Asset Name Category Locked `Lock Alpha`, `Lock Beta`, `Lock Gamma` (hitungan Needs Update 3).
- Kemampuan teknis (disediakan tim FE/BE): berpindah client untuk aktor Total Control di aplikasi (langkah 21, 24, 30).
- State global: tidak ada yang diubah selain client aktif (dipulihkan hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-40: Mobile: tap card membuka Popup Detail sebagai bottom sheet

1. Ketik Search `Dell Latitude`, tekan Enter
2. Tap card `Dell Latitude`
3. Verifikasi Detail Asset Name terbuka sebagai bottom sheet dengan Title `Asset Name Detail`
4. Tutup bottom sheet Detail

### TC-FA-FAAM-41: Mobile: toolbar memakai bottom sheet dan search inline

5. Tap `[⋯]` toolbar
6. Verifikasi bottom sheet memuat Column Visibility, Filter, dan Download
7. Tutup bottom sheet lalu tap `[🔍]`
8. Verifikasi Search bar inline terbuka
9. Verifikasi `[+ Asset Name]` tetap terlihat di bawah toolbar dan di atas card list
10. Verifikasi ikon Changelog tetap di header halaman

### TC-FA-FAAM-42: Mobile: badge lebih dari 10 karakter terpotong 5 + .. + 5

11. Ganti isi Search dengan nama Asset Name ber-Category 11 karakter (`Fixture.faAssetName.category11Item`), tekan Enter
12. Verifikasi badge Category pada card tersebut menampilkan 5 karakter pertama, `..`, lalu 5 karakter terakhir

### TC-FA-FAAM-39: Mobile: List tampil sebagai card list dengan konten kunci

13. Tutup Search inline sehingga seluruh card tampil
14. Verifikasi satu card per Asset Name
15. Verifikasi urutan card mengikuti default sort A-Z
16. Ketik Search `MacBook Pro`, tekan Enter
17. Verifikasi nama `MacBook Pro` tebal sebagai primary identifier
18. Verifikasi card `MacBook Pro` memuat badge Category dan badge `Needs Update`
19. Verifikasi field kunci card berurutan Code, TAG Type, Total Asset
20. Verifikasi icon `⋯` di pojok kanan atas card
21. Ganti client ke client downgrade (Pre-setup #20)
22. Ketik Search `Excess Gamma`, tekan Enter
23. Verifikasi card `Excess Gamma` memuat badge `Over Plan Limit`

### TC-FA-FAAM-706: Mobile: notice Category Locked di atas card list, aksi tautan, dan chip quick filter

24. Ganti client ke client `AutoLocked` (Pre-setup #12c)
25. Verifikasi notice `3 asset names need a category update.` tampil di atas card list dan di bawah `[+ Asset Name]` dengan aksi tautan teks `Show only these`
26. Tap tautan `Show only these`
27. Verifikasi card list hanya memuat `Lock Alpha`, `Lock Beta`, `Lock Gamma`
28. Verifikasi chip `Needs Update` tepat di bawah notice
29. Verifikasi notice menjadi `Showing 3 asset names that need a category update.` dengan aksi `Clear filter`

### TC-FA-FAAM-43: Mobile: tap elemen terkunci menampilkan tooltip yang hilang otomatis bukan toast

30. Ganti client ke client Starter tanpa subscription Paid (Pre-setup #16)
31. Tap `[+ Asset Name]`
32. Tap opsi `RFID` di field TAG Type yang terkunci
33. Verifikasi tidak ada toast muncul
34. Verifikasi tooltip `Upgrade to unlock` tampil
35. Verifikasi tooltip `Upgrade to unlock` hilang otomatis

## Notes

- Mode: FE+BE (aplikasi FAMS Android native). Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular. `coverage.web: unsupported` dan `coverage.mobile: automated` karena seluruh langkah berjalan di aplikasi mobile.
- Urutan TC di spec: 40, 41, 42, 39, 706, 43. TC di client utama lebih dahulu; berpindah client terjadi satu kali per TC yang membutuhkannya (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 11, 16 (Search untuk menemukan card target, R-16), langkah 4 dan 7 (menutup bottom sheet sesuai Langkah uji), langkah 13 (menutup Search inline), langkah 22 (Search pada client downgrade), langkah 21, 24, 30 (Ganti client eksplisit), langkah 26 dan 31 (tap sesuai Langkah uji).
- Langkah 33 (absence toast) ditulis segera setelah pemicu dan sebelum asersi tooltip; tap opsi `RFID` menjadi anchor positif yang buktinya menyusul pada langkah 34 (bagian 8b butir 11). Langkah 35 mengamati tooltip hilang sendiri tanpa tap tambahan.
- Temuan untuk QA:
  - TC-39 melewati dua client (client utama dan client downgrade #20) dalam satu TC; spec memakai Ganti client eksplisit di tengah TC (langkah 21), dan Search card `Excess Gamma` dilakukan sesudah berpindah client (langkah 22).
  - TC-42 menyebut "Category 11 karakter (Pre-setup #14g)" tanpa nama Asset Name; spec memakai kunci fixture baru `Fixture.faAssetName.category11Item`.
  - TC-43 tidak menyebut durasi tooltip hilang otomatis; spec mengasersi hilang tanpa tap tambahan.
  - TC-706 Precondition menyebut client dengan Pre-setup #12c tanpa akun aktor; spec memakai akun Total Control yang punya akses ke client itu (kemampuan disediakan tim FE/BE).

---
id: TC-GS-UOM-E2E-074-mobile-card-list-menu-dan-dialog
title: "Mobile Android: Card List, Tap Detail, Menu Card, Search, Filter, Create, dan Delete sebagai Bottom Sheet"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-250
  - TC-GS-UOM-251
  - TC-GS-UOM-252
  - TC-GS-UOM-356
  - TC-GS-UOM-391
coverage:
  mobile: automated
---

# Mobile Android: Card List, Tap Detail, Menu Card, Search, Filter, Create, dan Delete sebagai Bottom Sheet

## Prerequisites

- Mode: FE+BE (aplikasi Android terhadap backend nyata).
- Platform: aplikasi Android TAG Samurai Mobile (`coverage.mobile`); spec tidak berjalan di web. Perangkat atau emulator Android uji dipakai bersama sehingga spec ini `parallel: false` (S-09).
- Akun yang diuji (spec memakai dua akun dan berganti akun secara eksplisit):

  | Urutan | Role | Email | Environment variable password |
  |---|---|---|---|
  | 1 | Total Control Client A (Sari Dewi, `Sari D`) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |
  | 2 | System Role: Update dan Read (Agus Wijaya) | `updateOnly_automated_qaTeam1@qwertysystem.net` | `GS_UPDATE_PASSWORD` |

  Login akun 1 di hook `before` spec ini pada aplikasi Android (akun default suite); hook `after` mengembalikan sesi ke akun 1. Halaman awal: Global Settings > Master Reference > Tab Measurement.
- Environment variable: `GS_TC_PASSWORD`, `GS_UPDATE_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`, bagian Hook suite).
- Data Pre-setup Client A (hanya dibaca, tidak diubah, tanpa suffix `{runId}`): `Pieces` (Used By (Items) 3), `Box` (Used By (Items) 4), `Liter` (Used By (Items) 0), `Kilogram` (kata kunci Search `kilo`).
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi), bebas relasi, di-seed lewat API di hook `before`: `Kilogram Force {runId}-074` / `kgf` (D-07) supaya Search `kilo` memuat dua unit (pengganti Kilogram Force dari TC-GS-UOM-53), dan `Meter {runId}-074` / `m` yang hanya dibuka dialog Delete lalu dibatalkan pada TC-GS-UOM-356 (pengganti Meter Pre-setup; S-06). Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Kilogram Force {runId}-074` dan `Meter {runId}-074` bila ada.
- Kemampuan teknis: tap, ketik, dan pembukaan bottom sheet di perangkat atau emulator Android; ganti akun di aplikasi (logout lalu login).
- Tidak ada state global yang diubah.
- TC-GS-UOM-250, 251, 391, 356: login sebagai Total Control pada aplikasi Android. TC-GS-UOM-252: login sebagai System Role: Update dan Read.

## Test Steps

### TC-GS-UOM-250: Screening tab Measurement pada aplikasi mobile

1. Buka Global Settings > Master Reference > Tab Measurement di aplikasi Android
2. Verifikasi Breadcrumb `Master Reference > Measurement`
3. Verifikasi Tab `Brand | Measurement`
4. Verifikasi Toolbar memuat `[🔍]` dan `[⋯]`
5. Verifikasi tombol `[+ Unit]` di bawah toolbar
6. Verifikasi Card List tampil tanpa checkbox secara default
7. Verifikasi card memuat `[Unit Name] ([Symbol])`
8. Verifikasi card memuat `Used By (Items): [angka]` sebagai link
9. Verifikasi card memuat `Updated: [Last Updated]`
10. Verifikasi card memuat `[⋯ Menu]`
11. Verifikasi card tidak memuat teks `Item Types`

### TC-GS-UOM-251: Tap card membuka Unit Detail

12. Tap `[🔍]`, ketik `Pieces`, tekan Enter, lalu tap card `Pieces`
13. Verifikasi Unit Detail tampil sebagai bottom sheet full-height
14. Verifikasi Unit Detail memuat Accordion `Item Type List`
15. Tutup Unit Detail

### TC-GS-UOM-391: Card menampilkan Used By (Items) sebagai link ke Detail, termasuk 0

16. Ganti isi Search dengan `Box`, tekan Enter
17. Verifikasi card `Box` menampilkan `Used By (Items): 4` sebagai link
18. Tap angka Used By (Items) pada card `Box`
19. Verifikasi Unit Detail tampil sebagai bottom sheet full-height
20. Verifikasi Total Item `4`
21. Tutup Unit Detail, ganti isi Search dengan `Liter`, tekan Enter
22. Verifikasi card `Liter` menampilkan `Used By (Items): 0` sebagai link
23. Verifikasi card `Liter` menampilkan `0`, bukan `—`
24. Tap angka `0` pada card `Liter`
25. Verifikasi Detail `Liter` terbuka dengan Total Item `0`
26. Verifikasi empty state Accordion
27. Tutup Unit Detail

### TC-GS-UOM-356: Search inline, Filter, form Create, dan dialog Delete tampil sebagai bottom sheet

28. Ganti isi Search dengan `kilo`, tekan Enter
29. Verifikasi Search bar inline mengembang pada toolbar
30. Verifikasi card list hanya memuat `Kilogram` dan `Kilogram Force {runId}-074`
31. Kosongkan isi kotak search, tekan Enter, tap `[⋯]` pada toolbar > Filter
32. Verifikasi Filter Panel tampil sebagai bottom sheet
33. Tutup Filter, tap `[+ Unit]`
34. Verifikasi form `Create Unit` tampil sebagai bottom sheet
35. Tutup form, ketik Search `Meter {runId}-074`, tekan Enter, tap `[⋯ Menu]` card `Meter {runId}-074` > Delete
36. Verifikasi dialog `Delete Unit` tampil sebagai bottom sheet
37. Klik [Cancel] pada dialog
38. Verifikasi card `Meter {runId}-074` tetap ada

### TC-GS-UOM-252: Menu card mobile mengikuti capability dan toolbar bottom sheet

39. Ganti akun: logout, lalu login sebagai System Role: Update dan Read (`updateOnly_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_UPDATE_PASSWORD`, lalu buka Global Settings > Master Reference > Tab Measurement
40. Ketik Search `Liter`, tekan Enter, tap `[⋯ Menu]` card `Liter`
41. Verifikasi menu berisi `Detail` dan `Edit` saja
42. Tutup menu, tap `[⋯]` toolbar
43. Verifikasi bottom sheet memuat Column Visibility, Filter, Download, dan Changelog

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Spec mobile Android (`coverage.mobile: automated`), preseden `TC-GS-BRAND-E2E-074-mobile-card-list-dan-selection-mode`.
- Urutan TC di spec berbeda dari urutan sumber: blok Total Control (250, 251, 391, 356) lebih dulu, lalu satu kali ganti akun (langkah 39) ke System Role: Update dan Read untuk 252. Tidak ada aksi yang menghabisi data (Delete pada 356 dibatalkan).
- Langkah penghubung: langkah 1 (salinan Langkah Uji TC-GS-UOM-250 "Buka ... Tab Measurement"; halaman awal dinyatakan di Prerequisites), langkah 12, 16, 21, 28, 35, dan 40 (mencari card target lewat Search inline atau mengganti isi Search; daftar card memuat lebih dari satu layar), langkah 15, 21, 27, 33, 35, dan 42 (menutup Unit Detail, Filter, form, atau menu sebelum aksi berikutnya), langkah 31 (mengosongkan isi kotak search sebelum membuka Filter; Langkah Uji TC-GS-UOM-356 menulis "Kosongkan Search" tanpa aksi), langkah 39 (ganti akun eksplisit, S-07).
- Langkah 17 dan 22 (angka Used By pada card Box dan Liter) berasal dari Expected a TC-GS-UOM-391; Used By (Items) Pre-setup Client A: Box 4, Liter 0 dan Pieces 3 (Tabel Data Uji).
- Langkah 30: asersi "hanya memuat" didahului hasil Search yang memuat kedua card tersebut sebagai pembanding; `Kilogram Force` diganti `Kilogram Force {runId}-074` milik spec (S-12).
- Langkah 35 dan 38 memakai `Meter {runId}-074` milik spec sebagai pengganti baris Pre-setup Meter yang disebut Langkah Uji dan Data Uji TC-GS-UOM-356 (S-06, S-12); aksi Delete dibatalkan pada langkah 37.
- Pembagian TC lintas spec: Tab Measurement di web (tabel) ada di spec 001; TC mobile selection mode Bulk Delete ada di spec 075.
- Spec ini di atas batas 35 langkah (43): seluruhnya satu kelas (mobile Android) pada satu sesi perangkat dengan satu kali ganti akun; memecahnya menambah pembukaan sesi perangkat.
- Temuan untuk QA:
  - TC-GS-UOM-252 menyebut "Menu berisi Detail dan Edit saja" untuk System Role: Update dan Read; TC tidak menyebut nama item menu lain yang harus Hidden. Spec mengasersi isi menu dengan daftar utuh.
  - TC-GS-UOM-250 butir c menulis `Updated: [Last Updated]`; format tanggal mengikuti General Settings dan tidak diasersi nilainya.
  - TC-GS-UOM-356 butir a menyebut Search `kilo` menyaring ke Kilogram dan Kilogram Force; Kilogram Force dibuat TC-GS-UOM-53 (spec lain), sehingga spec men-seed unit milik spec.

---
id: TC-FA-LBL-E2E-006-mobile-card-list-labels-list-menu-card-per-role-long-press-dan-tooltip-disabled
title: "Mobile: Card List Labels List, Menu Card per Role, Long-Press, Bottom Sheet Toolbar, dan Tooltip Disabled"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-21
  - TC-FA-LBL-22
  - TC-FA-LBL-23
  - TC-FA-LBL-24
  - TC-FA-LBL-503
  - TC-FA-LBL-525
coverage:
  mobile: automated
---

# Mobile: Card List Labels List, Menu Card per Role, Long-Press, Bottom Sheet Toolbar, dan Tooltip Disabled

## Prerequisites

- Mode: FE+BE. Platform: aplikasi mobile Fixed Asset di perangkat Android (Card List, long-press, bottom sheet).
- Perangkat atau emulator Android dengan aplikasi mobile Fixed Asset terpasang, serta kemampuan mengetuk (tap), menekan lama (long-press), dan mengamati tooltip (disediakan tim FE). Perangkat Android bersama: `parallel: false` (suite berjalan serial, lihat `suite.md`). Hook suite web (`beforeEach` yang membuka tab Labels) tidak berlaku di aplikasi mobile; layar Labels dibuka oleh langkah spec ini.
- Hook suite: `before` dan `after` berlaku sesuai `suite.md` untuk akun default (Total Control Company Alpha); `after` mengembalikan sesi ke akun default suite.
- Akun aktor (Role yang diuji; login akun pertama di aplikasi mobile pada hook `before` spec ini, akun berikutnya lewat langkah Ganti akun):

| Role | Pre-setup | Fixture | Env | Dipakai |
|---|---|---|---|---|
| Total Control | #1 | `Fixture.assetLabeling.akun.totalControl` | `Spectra.env.FA_LBL_TC_PASSWORD` | langkah 1 sampai 26 |
| Update-Only | #4 | `Fixture.assetLabeling.akun.updateOnly` | `Spectra.env.FA_UPDATEONLY_PASSWORD` | langkah 27 sampai 32 |
| Delete-Only | #5 | `Fixture.assetLabeling.akun.deleteOnly` | `Spectra.env.FA_DELETEONLY_PASSWORD` | langkah 33 sampai 35 |
| Read Only | #2 | `Fixture.assetLabeling.akun.readOnly` | `Spectra.env.FA_RO_PASSWORD` | langkah 36 sampai 40 |

- Environment variable: `FA_LBL_TC_PASSWORD`, `FA_UPDATEONLY_PASSWORD`, `FA_DELETEONLY_PASSWORD`, `FA_RO_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Pre-setup (dibaca saja, tidak diubah spec): #12 (katalog Company Alpha 9 label; dipakai: `Seasonal Event`, `Finance Department`) dan #13 (aset berlabel `Finance Department` untuk isi Drawer).
- State global: tidak ada yang diubah selain sesi login di perangkat.

## Test Steps

### TC-FA-LBL-21: Mobile: screening Labels List berbentuk Card List

1. Buka Settings > Asset Master > Labels di aplikasi mobile Fixed Asset
2. Verifikasi tabel diganti Card List satu card per label
3. Verifikasi tiap card menampilkan chip badge Label (tebal), tombol `⋯`, Color Hex, Total Asset, dan baris `Modified By · Last Updated`
4. Verifikasi ikon Changelog tampil di header halaman
5. Verifikasi tombol `[+ Label]` tampil di bawah toolbar di atas Card List

### TC-FA-LBL-22: Mobile: tap chip Label membuka Drawer Tagged Asset, tap area card lain tidak melakukan apa pun

6. Tap area card `Finance Department` di luar chip dan `⋯`
7. Verifikasi Card List Labels tetap tampil
8. Verifikasi tap area card di luar chip dan `⋯` tidak membuka apa pun (tidak ada Drawer, bottom sheet, atau dialog)
9. Tap chip `Finance Department`
10. Verifikasi Drawer Tagged Asset terbuka sebagai full-screen bottom sheet
11. Tutup Drawer Tagged Asset

### TC-FA-LBL-24: Mobile: isi bottom sheet toolbar, search inline, dan tombol `[+ Label]`

12. Tap `⋯` toolbar
13. Verifikasi bottom sheet toolbar memuat `Filter` dan `Download` saja
14. Verifikasi opsi Column Visibility tidak tersedia di bottom sheet toolbar
15. Tutup bottom sheet toolbar
16. Tap `🔍`
17. Verifikasi search inline terbuka
18. Tutup search inline

### TC-FA-LBL-525: Mobile: tooltip alasan elemen Disabled tampil saat di-tap dan hilang otomatis

19. Tap `[+ Label]`
20. Biarkan Label Name kosong dan tap `[Submit]` yang berstatus disabled
21. Verifikasi tooltip `Enter a label name to continue.` tampil
22. Tunggu tanpa menyentuh layar
23. Verifikasi tooltip hilang otomatis tanpa tap tambahan
24. Tutup modal Create Label dengan `✕`

### TC-FA-LBL-23: Mobile: menu `⋯` pada card hanya memuat aksi yang diizinkan (Total Control)

25. Tap `⋯` pada card `Seasonal Event`
26. Verifikasi menu memuat `Edit` dan `Delete`

### Update-Only: TC-FA-LBL-23 dan TC-FA-LBL-503

27. Ganti akun: Logout, login sebagai Update-Only `Fixture.assetLabeling.akun.updateOnly` (`Spectra.env.FA_UPDATEONLY_PASSWORD`) di aplikasi mobile, buka Settings > Asset Master > Labels
28. Tap `⋯` pada card `Seasonal Event`
29. Verifikasi menu memuat `Edit` saja
30. Tutup menu card
31. Long-press card `Seasonal Event`
32. Verifikasi mode seleksi tidak aktif, tidak ada checkbox di card, dan Floating Bottom Bulk Bar tidak tampil

### Delete-Only: TC-FA-LBL-23

33. Ganti akun: Logout, login sebagai Delete-Only `Fixture.assetLabeling.akun.deleteOnly` (`Spectra.env.FA_DELETEONLY_PASSWORD`) di aplikasi mobile, buka Settings > Asset Master > Labels
34. Tap `⋯` pada card `Seasonal Event`
35. Verifikasi menu memuat `Delete` saja

### Read Only: TC-FA-LBL-23 dan TC-FA-LBL-503

36. Ganti akun: Logout, login sebagai Read Only `Fixture.assetLabeling.akun.readOnly` (`Spectra.env.FA_RO_PASSWORD`) di aplikasi mobile, buka Settings > Asset Master > Labels
37. Verifikasi card `Seasonal Event` tampil
38. Verifikasi icon `⋯` pada card `Seasonal Event` tidak tampil (Hidden)
39. Long-press card `Seasonal Event`
40. Verifikasi mode seleksi tidak aktif, tidak ada checkbox di card, dan Floating Bottom Bulk Bar tidak tampil

## Notes

- Langkah penghubung (S-03): langkah 11 (menutup Drawer), langkah 18 (menutup search inline), langkah 24 (menutup modal Create yang tidak dirty), langkah 30 (menutup menu card sebelum long-press).
- Urutan TC: TC-FA-LBL-23 dan TC-FA-LBL-503 diurutkan per role (Total Control, Update-Only, Delete-Only, Read Only) agar tiap akun hanya sekali login; langkah per role tetap mengikuti urutan TC (S-10).
- Absence: langkah 8 didahului langkah 7 (Card List tetap tampil) sebagai anchor; langkah 32 dan 40 didahului Card List yang sudah termuat dan menu card pada langkah sebelumnya (langkah 29 dan 37).
- Alasan di atas sekitar 35 langkah (40 langkah): seluruh blok adalah layar Labels aplikasi mobile pada perangkat Android yang sama (satu kelas harness), tiap blok berdiri sendiri dan pergantian role mengikuti TC-FA-LBL-23 dan TC-FA-LBL-503.
- Temuan untuk QA:
  - TC-FA-LBL-525 tidak menyebut durasi hilangnya tooltip otomatis; langkah 22 ditulis tanpa durasi dan asersi langkah 23 menunggu tooltip hilang (batas tunggu ditetapkan tim FE).
  - TC-FA-LBL-23 menyebut menu card mobile hanya `Edit` dan `Delete` tanpa `Detail` (web memuat `Detail`, TC-FA-LBL-16); spec mengikuti TC.
  - Kolom Pre-setup #4 (Update-Only), #5 (Delete-Only), dan #2 (Read Only) di aplikasi mobile memakai akun yang sama dengan web; tidak ada akun mobile khusus di Pre-setup.

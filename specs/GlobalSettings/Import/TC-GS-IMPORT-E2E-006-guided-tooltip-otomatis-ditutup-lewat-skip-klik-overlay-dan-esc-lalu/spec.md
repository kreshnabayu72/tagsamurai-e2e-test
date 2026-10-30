---
id: TC-GS-IMPORT-E2E-006-guided-tooltip-otomatis-ditutup-lewat-skip-klik-overlay-dan-esc-lalu
title: "Guided Tooltip Otomatis Ditutup Lewat Skip, Klik Overlay, dan Esc Lalu Ditandai Sudah Dilihat"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-587
  - TC-GS-IMPORT-588
  - TC-GS-IMPORT-589
coverage:
  web: automated
---

# Guided Tooltip Otomatis Ditutup Lewat Skip, Klik Overlay, dan Esc Lalu Ditandai Sudah Dilihat

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Pengecualian flag Guided Tooltip: spec ini menguji flag `guided_tooltip_seen_gs-import` sendiri sehingga tidak memakai pernyataan hook suite `before` yang men-set flag true. Flag akun Total Control Tooltip Baru Client A direset (belum ada) lewat fixture sebelum tiap blok TC (langkah reset ditulis eksplisit); hook `after` memulihkan nilai awal flag. Mekanisme reset/set flag disediakan tim FE/BE (S-13).
- Akun aktor: Total Control Tooltip Baru Client A (Umar Faruq) `totalControlTooltipNew_automated_qaTeam1@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_TCTOOLTIPNEW_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: spec menguji tampil otomatis saat menu Import dibuka, sehingga tidak mengandalkan layar yang dibuka hook `beforeEach`. Sesudah tiap reset flag, spec membuka File Manager lewat address bar lalu membuka menu Import (langkah 2 dan 3, 16 dan 17, 30 dan 31) sehingga halaman Import dimuat segar dan flag terbaca saat pemuatan.
- Data: tanpa draft; tidak ada Data Dinamis.
- Kemampuan teknis: reset/set flag Guided Tooltip per akun; klik overlay gelap di luar spotlight; muat ulang halaman.
- State global: flag Guided Tooltip akun Tooltip Baru (dipulihkan hook `after`).

## Test Steps

### TC-GS-IMPORT-587: Klik [Skip] menutup Guided Tooltip dan menandai sudah dilihat

1. Reset flag Guided Tooltip `gs-import` akun Tooltip Baru (belum ada)
2. Buka halaman Global Settings > File Manager dengan memasukkan alamatnya di address bar browser
3. Buka menu Import dari sidebar
4. Perhatikan halaman
5. Verifikasi Guided Tooltip tampil otomatis pada Step 1 of 3
6. Verifikasi Step 1 of 3 menampilkan tombol `[Skip]` dan `[Next]`
7. Klik `[Skip]` pada Step 1
8. Perhatikan halaman
9. Verifikasi walkthrough tertutup
10. Verifikasi overlay gelap hilang
11. Muat ulang halaman Import
12. Perhatikan halaman
13. Verifikasi Breadcrumb `Import > Brand` tampil
14. Verifikasi Guided Tooltip tidak tampil otomatis

### TC-GS-IMPORT-588: Klik overlay menutup Guided Tooltip dan menandai sudah dilihat

15. Reset flag Guided Tooltip `gs-import` akun Tooltip Baru (belum ada)
16. Buka halaman Global Settings > File Manager dengan memasukkan alamatnya di address bar browser
17. Buka menu Import dari sidebar
18. Perhatikan halaman
19. Verifikasi Guided Tooltip tampil otomatis pada Step 1 of 3
20. Verifikasi Step 1 of 3 menampilkan tombol `[Skip]` dan `[Next]`
21. Klik overlay gelap di luar spotlight dan tooltip
22. Perhatikan halaman
23. Verifikasi walkthrough tertutup
24. Verifikasi overlay gelap hilang
25. Muat ulang halaman Import
26. Perhatikan halaman
27. Verifikasi Breadcrumb `Import > Brand` tampil
28. Verifikasi Guided Tooltip tidak tampil otomatis

### TC-GS-IMPORT-589: Tombol Esc menutup Guided Tooltip dan menandai sudah dilihat

29. Reset flag Guided Tooltip `gs-import` akun Tooltip Baru (belum ada)
30. Buka halaman Global Settings > File Manager dengan memasukkan alamatnya di address bar browser
31. Buka menu Import dari sidebar
32. Perhatikan halaman
33. Verifikasi Guided Tooltip tampil otomatis pada Step 1 of 3
34. Verifikasi Step 1 of 3 menampilkan tombol `[Skip]` dan `[Next]`
35. Tekan tombol Esc
36. Perhatikan halaman
37. Verifikasi walkthrough tertutup
38. Verifikasi overlay gelap hilang
39. Muat ulang halaman Import
40. Perhatikan halaman
41. Verifikasi Breadcrumb `Import > Brand` tampil
42. Verifikasi Guided Tooltip tidak tampil otomatis

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 15, dan 29 (reset flag sebelum tiap blok lewat fixture sinkron, tanpa penanda tunggu, S-09: tiap TC menandai flag sehingga blok berikutnya wajib direset), langkah 2, 16, dan 30 (membuka File Manager lewat address bar) serta langkah mengamati sesuai Langkah Uji TC (4, 8, 12, 18, 22, 26, 32, 36, 40).
- Langkah 13, 27, dan 41 (`Verifikasi` Breadcrumb `Import > Brand` tampil) adalah asersi tambahan di luar Expected TC: anchor positif untuk absence "Guided Tooltip tidak tampil otomatis" sesudah muat ulang (8b butir 2, S-03).
- Spec melewati sekitar 35 langkah (42 langkah). Tiga blok memakai pola homogen (buka Import, verifikasi tampil otomatis, tutup, muat ulang, verifikasi tidak tampil) dan berdiri sendiri; kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - Mekanisme reset flag `guided_tooltip_seen_gs-import` per akun ("direset lewat fixture") tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).

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
- Layar awal: spec menguji tampil otomatis saat menu Import dibuka, sehingga membuka menu lewat langkah sendiri.
- Data: tanpa draft; tidak ada Data Dinamis.
- Kemampuan teknis: reset/set flag Guided Tooltip per akun; klik overlay gelap di luar spotlight; muat ulang halaman.
- State global: flag Guided Tooltip akun Tooltip Baru (dipulihkan hook `after`).

## Test Steps

### TC-GS-IMPORT-587: Klik [Skip] menutup Guided Tooltip dan menandai sudah dilihat

1. Reset flag Guided Tooltip `gs-import` akun Tooltip Baru (belum ada)
2. Buka menu Import dari sidebar
3. Perhatikan halaman
4. Verifikasi Guided Tooltip tampil otomatis pada Step 1 of 3
5. Verifikasi Step 1 of 3 menampilkan tombol `[Skip]` dan `[Next]`
6. Klik `[Skip]` pada Step 1
7. Perhatikan halaman
8. Verifikasi walkthrough tertutup
9. Verifikasi overlay gelap hilang
10. Muat ulang halaman Import
11. Perhatikan halaman
12. Verifikasi Breadcrumb `Import > Brand` tampil
13. Verifikasi Guided Tooltip tidak tampil otomatis

### TC-GS-IMPORT-588: Klik overlay menutup Guided Tooltip dan menandai sudah dilihat

14. Reset flag Guided Tooltip `gs-import` akun Tooltip Baru (belum ada)
15. Buka menu Import dari sidebar
16. Perhatikan halaman
17. Verifikasi Guided Tooltip tampil otomatis pada Step 1 of 3
18. Verifikasi Step 1 of 3 menampilkan tombol `[Skip]` dan `[Next]`
19. Klik overlay gelap di luar spotlight dan tooltip
20. Perhatikan halaman
21. Verifikasi walkthrough tertutup
22. Verifikasi overlay gelap hilang
23. Muat ulang halaman Import
24. Perhatikan halaman
25. Verifikasi Breadcrumb `Import > Brand` tampil
26. Verifikasi Guided Tooltip tidak tampil otomatis

### TC-GS-IMPORT-589: Tombol Esc menutup Guided Tooltip dan menandai sudah dilihat

27. Reset flag Guided Tooltip `gs-import` akun Tooltip Baru (belum ada)
28. Buka menu Import dari sidebar
29. Perhatikan halaman
30. Verifikasi Guided Tooltip tampil otomatis pada Step 1 of 3
31. Verifikasi Step 1 of 3 menampilkan tombol `[Skip]` dan `[Next]`
32. Tekan tombol Esc
33. Perhatikan halaman
34. Verifikasi walkthrough tertutup
35. Verifikasi overlay gelap hilang
36. Muat ulang halaman Import
37. Perhatikan halaman
38. Verifikasi Breadcrumb `Import > Brand` tampil
39. Verifikasi Guided Tooltip tidak tampil otomatis

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 14, dan 27 (reset flag sebelum tiap blok, S-09: tiap TC menandai flag sehingga blok berikutnya wajib direset) serta langkah mengamati sesuai Langkah Uji TC (3, 7, 11, 16, 20, 24, 29, 33, 37).
- Langkah 12, 25, dan 38 (`Verifikasi` Breadcrumb `Import > Brand` tampil) adalah asersi tambahan di luar Expected TC: anchor positif untuk absence "Guided Tooltip tidak tampil otomatis" sesudah muat ulang (8b butir 2, S-03).
- Spec melewati sekitar 35 langkah (39 langkah). Tiga blok memakai pola homogen (buka Import, verifikasi tampil otomatis, tutup, muat ulang, verifikasi tidak tampil) dan berdiri sendiri; kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - Mekanisme reset flag `guided_tooltip_seen_gs-import` per akun ("direset lewat fixture") tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).

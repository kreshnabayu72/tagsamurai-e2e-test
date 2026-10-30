---
id: TC-GS-IMPORT-E2E-005-guided-tooltip-otomatis-selesai-sampai-done-keluar-halaman-di-tengah
title: "Guided Tooltip Otomatis: Selesai Sampai Done, Keluar Halaman di Tengah, Replay, dan Keluar Tidak Menandai Ulang"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-24
  - TC-GS-IMPORT-590
  - TC-GS-IMPORT-593
coverage:
  web: automated
---

# Guided Tooltip Otomatis: Selesai Sampai Done, Keluar Halaman di Tengah, Replay, dan Keluar Tidak Menandai Ulang

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Pengecualian flag Guided Tooltip: spec ini menguji flag `guided_tooltip_seen_gs-import` sendiri sehingga tidak memakai pernyataan hook suite `before` yang men-set flag true. Pengaturannya:
  - Akun Total Control Tooltip Baru Client A: flag direset (belum ada) lewat fixture sebelum TC-GS-IMPORT-24 dan sebelum TC-GS-IMPORT-590 (langkah reset ditulis eksplisit); hook `before` suite tidak men-set flag ini.
  - Akun Total Control Tooltip Selesai Client A: flag seen aktif (sudah selesai) sejak Pre-setup; dicatat nilai awalnya dan dipulihkan hook `after`.
  - Mekanisme penyetelan/reset flag disediakan tim FE/BE (S-13).
- Akun aktor:
  - Total Control Tooltip Baru Client A (Umar Faruq) `totalControlTooltipNew_automated_qaTeam1@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-24 dan 590. Login sekali di hook `before` dengan `Spectra.env.GS_TCTOOLTIPNEW_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`).
  - Total Control Tooltip Selesai Client A (Vina Oktavia) `totalControlTooltipDone_automated_qaTeam1@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-593: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_TCTOOLTIPDONE_PASSWORD` (env baru). Hook `after` mengembalikan sesi ke Total Control Client A.
  - Password tidak ditulis di spec atau fixture.
- Layar awal: spec menguji pembukaan menu Import dan navigasi keluar, sehingga membuka menu lewat langkah sendiri.
- Data: tanpa draft (Client A tanpa draft pada keadaan awal spec ini; reset melalui hook `beforeEach`). Tidak ada Data Dinamis.
- Kemampuan teknis: reset/set flag Guided Tooltip per akun; membuka halaman lewat address bar; muat ulang halaman; ganti akun.
- State global: flag Guided Tooltip akun Tooltip Baru dan Tooltip Selesai (dipulihkan hook `after`).

## Test Steps

### TC-GS-IMPORT-24: Guided Tooltip otomatis tampil pada kunjungan pertama, selesai sampai Done, dan tidak muncul lagi

1. Reset flag Guided Tooltip `gs-import` akun Tooltip Baru (belum ada)
2. Buka menu Import dari sidebar
3. Perhatikan halaman
4. Verifikasi Guided Tooltip tampil otomatis pada Step 1 of 3
5. Verifikasi Title Step 1 "Download Template"
6. Klik `[Next]` pada Step 1
7. Klik `[Next]` pada Step 2
8. Perhatikan Step 3
9. Verifikasi Step 3 of 3 menampilkan tombol `[Done]` menggantikan `[Next]`
10. Klik `[Done]`
11. Verifikasi walkthrough tertutup
12. Muat ulang halaman Import
13. Perhatikan halaman
14. Verifikasi Breadcrumb `Import > Brand` tampil
15. Verifikasi Guided Tooltip tidak tampil otomatis

### TC-GS-IMPORT-590: Meninggalkan halaman di tengah Guided Tooltip tidak menandai sudah dilihat

16. Reset flag Guided Tooltip `gs-import` akun Tooltip Baru (belum ada)
17. Buka menu Import dari sidebar
18. Perhatikan halaman
19. Verifikasi Guided Tooltip tampil otomatis pada Step 1 of 3
20. Klik `[Next]` pada Step 1
21. Perhatikan Step 2
22. Verifikasi Guided Tooltip menampilkan Step 2 of 3
23. Verifikasi Title Step 2 "Upload File"
24. Buka halaman Global Settings > File Manager dengan memasukkan alamatnya di address bar browser
25. Buka menu Import dari sidebar
26. Perhatikan halaman
27. Verifikasi Guided Tooltip tampil otomatis lagi pada Step 1 of 3

### TC-GS-IMPORT-593: Replay lewat [?] dan keluar di tengah walkthrough tidak membuat Guided Tooltip tampil otomatis lagi

28. Ganti akun: logout dari akun Tooltip Baru
29. Login sebagai Total Control Tooltip Selesai Client A dengan `Spectra.env.GS_TCTOOLTIPDONE_PASSWORD`
30. Buka menu Import dari sidebar
31. Perhatikan halaman
32. Verifikasi Breadcrumb `Import > Brand` tampil
33. Verifikasi Guided Tooltip tidak tampil otomatis
34. Klik tombol `[?]` di kanan Breadcrumb
35. Klik `[Next]` pada Step 1
36. Perhatikan Step 2
37. Verifikasi replay menampilkan Step 2 of 3
38. Verifikasi Title Step 2 "Upload File"
39. Buka halaman Global Settings > File Manager dengan memasukkan alamatnya di address bar browser
40. Buka menu Import dari sidebar
41. Perhatikan halaman
42. Verifikasi Breadcrumb `Import > Brand` tampil
43. Verifikasi Guided Tooltip tidak tampil otomatis

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 24, 590, 593. TC-GS-IMPORT-24 menyelesaikan walkthrough sehingga flag aktif; langkah 16 mereset flag sebelum TC-GS-IMPORT-590 (S-09). TC-GS-IMPORT-593 di akhir karena ganti akun ke Tooltip Selesai.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 16 (reset flag), 3, 8, 13, 18, 21, 26, 31, 36, 41 (mengamati sesuai Langkah Uji TC), serta langkah 28 dan 29 (ganti akun).
- Langkah 14, 32, dan 42 (`Verifikasi` Breadcrumb `Import > Brand` tampil) adalah asersi tambahan di luar Expected TC: anchor positif untuk absence "Guided Tooltip tidak tampil otomatis" sesudah muat ulang, ganti akun, dan kembali dari File Manager (8b butir 2, S-03).
- Spec melewati sekitar 35 langkah (43 langkah). Seluruhnya satu topik (Guided Tooltip otomatis dan replay), tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain; blok pada akun lain berada di akhir dengan langkah ganti akun eksplisit.
- Temuan untuk QA:
  - Mekanisme reset flag `guided_tooltip_seen_gs-import` per akun tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
  - TC-GS-IMPORT-593 dan 590 membuka File Manager lewat address bar tanpa menyebut alamat route; spec menulis "memasukkan alamatnya di address bar" sesuai TC.

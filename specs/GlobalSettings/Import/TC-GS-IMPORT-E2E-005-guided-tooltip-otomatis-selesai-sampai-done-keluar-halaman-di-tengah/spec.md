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
- Layar awal: spec menguji pembukaan menu Import dan navigasi keluar, sehingga tidak mengandalkan layar yang dibuka hook `beforeEach`. Sesudah tiap reset flag, spec membuka File Manager lewat address bar lalu membuka menu Import (langkah 2 dan 3, langkah 18 dan 19) sehingga halaman Import dimuat segar dan flag terbaca saat pemuatan. Langkah 30 menutup walkthrough yang masih terbuka dengan Esc sebelum ganti akun; efek penutupan itu pada flag tidak diasersi, dan hook `after` memulihkan nilai awal flag akun Tooltip Baru.
- Data: tanpa draft (Client A tanpa draft pada keadaan awal spec ini; reset melalui hook `beforeEach`). Tidak ada Data Dinamis.
- Kemampuan teknis: reset/set flag Guided Tooltip per akun; membuka halaman lewat address bar; muat ulang halaman; ganti akun.
- State global: flag Guided Tooltip akun Tooltip Baru dan Tooltip Selesai (dipulihkan hook `after`).

## Test Steps

### TC-GS-IMPORT-24: Guided Tooltip otomatis tampil pada kunjungan pertama, selesai sampai Done, dan tidak muncul lagi

1. Reset flag Guided Tooltip `gs-import` akun Tooltip Baru (belum ada)
2. Buka halaman Global Settings > File Manager dengan memasukkan alamatnya di address bar browser
3. Buka menu Import dari sidebar
4. Perhatikan halaman
5. Verifikasi Guided Tooltip tampil otomatis pada Step 1 of 3
6. Verifikasi Title Step 1 "Download Template"
7. Klik `[Next]` pada Step 1
8. Klik `[Next]` pada Step 2
9. Perhatikan Step 3
10. Verifikasi Step 3 of 3 menampilkan tombol `[Done]` menggantikan `[Next]`
11. Klik `[Done]`
12. Verifikasi walkthrough tertutup
13. Muat ulang halaman Import
14. Perhatikan halaman
15. Verifikasi Breadcrumb `Import > Brand` tampil
16. Verifikasi Guided Tooltip tidak tampil otomatis

### TC-GS-IMPORT-590: Meninggalkan halaman di tengah Guided Tooltip tidak menandai sudah dilihat

17. Reset flag Guided Tooltip `gs-import` akun Tooltip Baru (belum ada)
18. Buka halaman Global Settings > File Manager dengan memasukkan alamatnya di address bar browser
19. Buka menu Import dari sidebar
20. Perhatikan halaman
21. Verifikasi Guided Tooltip tampil otomatis pada Step 1 of 3
22. Klik `[Next]` pada Step 1
23. Perhatikan Step 2
24. Verifikasi Guided Tooltip menampilkan Step 2 of 3
25. Verifikasi Title Step 2 "Upload File"
26. Buka halaman Global Settings > File Manager dengan memasukkan alamatnya di address bar browser
27. Buka menu Import dari sidebar
28. Perhatikan halaman
29. Verifikasi Guided Tooltip tampil otomatis lagi pada Step 1 of 3
30. Tekan Esc untuk menutup walkthrough

### TC-GS-IMPORT-593: Replay lewat [?] dan keluar di tengah walkthrough tidak membuat Guided Tooltip tampil otomatis lagi

31. Ganti akun: logout dari akun Tooltip Baru
32. Login sebagai Total Control Tooltip Selesai Client A dengan `Spectra.env.GS_TCTOOLTIPDONE_PASSWORD`
33. Buka menu Import dari sidebar
34. Perhatikan halaman
35. Verifikasi Breadcrumb `Import > Brand` tampil
36. Verifikasi Guided Tooltip tidak tampil otomatis
37. Klik tombol `[?]` di kanan Breadcrumb
38. Klik `[Next]` pada Step 1
39. Perhatikan Step 2
40. Verifikasi replay menampilkan Step 2 of 3
41. Verifikasi Title Step 2 "Upload File"
42. Buka halaman Global Settings > File Manager dengan memasukkan alamatnya di address bar browser
43. Buka menu Import dari sidebar
44. Perhatikan halaman
45. Verifikasi Breadcrumb `Import > Brand` tampil
46. Verifikasi Guided Tooltip tidak tampil otomatis

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 24, 590, 593. TC-GS-IMPORT-24 menyelesaikan walkthrough sehingga flag aktif; langkah 17 mereset flag sebelum TC-GS-IMPORT-590 (S-09). TC-GS-IMPORT-593 di akhir karena ganti akun ke Tooltip Selesai.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 17 (reset flag lewat fixture sinkron, tanpa penanda tunggu), 2 dan 18 (membuka File Manager lewat address bar), 30 (Esc menutup walkthrough), 4, 9, 14, 20, 23, 28, 34, 39, 44 (mengamati sesuai Langkah Uji TC), serta langkah 31 dan 32 (ganti akun).
- Langkah 15, 35, dan 45 (`Verifikasi` Breadcrumb `Import > Brand` tampil) adalah asersi tambahan di luar Expected TC: anchor positif untuk absence "Guided Tooltip tidak tampil otomatis" sesudah muat ulang, ganti akun, dan kembali dari File Manager (8b butir 2, S-03).
- Spec melewati sekitar 35 langkah (46 langkah). Seluruhnya satu topik (Guided Tooltip otomatis dan replay), tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain; blok pada akun lain berada di akhir dengan langkah ganti akun eksplisit.
- Temuan untuk QA:
  - Mekanisme reset flag `guided_tooltip_seen_gs-import` per akun tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
  - TC-GS-IMPORT-593 dan 590 membuka File Manager lewat address bar tanpa menyebut alamat route; spec menulis "memasukkan alamatnya di address bar" sesuai TC.

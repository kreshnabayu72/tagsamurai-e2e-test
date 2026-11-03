---
id: TC-AC-PF-E2E-015-konkurensi-archive-dan-retry-archive-oleh-sesi-lain-edit-plan-yang-di-archive
title: "Konkurensi Archive: Client Baru Ter-assign, Retry Archive, dan Edit Plan yang Di-archive Sesi Lain"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-593
  - TC-AC-PF-594
  - TC-AC-PF-598
coverage:
  web: automated
---

# Konkurensi Archive: Client Baru Ter-assign, Retry Archive, dan Edit Plan yang Di-archive Sesi Lain

## Prerequisites

- Mode: FE+BE.
- Akun sesi A (aktor pertama): Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Akun sesi B pada TC-AC-PF-594 (konteks browser kedua): Total Control Principal kedua `secondAdminPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Rina Kusuma`, Pre-setup #9), password dari `Spectra.env.AC_PF_SA_PASSWORD`. Pelaku sesi B pada TC-AC-PF-593 ("sesi lain/modul Allocation") dan TC-AC-PF-598 hanya memicu perubahan state lewat sesi API; akunnya tidak tertulis di Pre-setup #46 dan disediakan tim FE. Kelas harness: c multi-konteks.
- Login sesi A di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Sesi B (UI) login pada langkah 14 di konteks browser kedua; hook `after` menutup konteks kedua dan mengembalikan sesi ke akun default suite.
- Data milik spec (hook `before`, dibuat lewat fixture BE, dibersihkan di hook `after`): tiga custom plan Principal aktif tanpa subscription bersuffix (Dataset Plan G `Paket Tanpa Client`, satu plan per blok TC): `Paket Race Satu {runId}-015` (TC-AC-PF-593), `Paket Archive Ganda {runId}-015` (TC-AC-PF-594), `Paket Edit Archive {runId}-015` (TC-AC-PF-598, Group count awal `3`). Client dinamis `PT Race Satu {runId}-015` (subscription Active, dibuat sesi API pada langkah 2). General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`) untuk kedua akun; spec ini tidak mengubahnya.
- Kemampuan teknis: konteks browser kedua dengan login akun #9; sesi API aktor untuk memicu pembuatan subscription (langkah 2) dan Archive oleh pelaku kedua (langkah 27) tanpa endpoint karangan (S-13, R-20); fixture BE (pembuatan dan pembersihan plan serta client) disediakan tim FE/BE (lihat `suite.md`).
- State global: entri Changelog baru pada Changelog Custom bersifat permanen dan tidak dapat dihapus lewat UI; plan dan client buatan spec dihapus lewat fixture BE di hook `after`.
- Env var: `Spectra.env.AC_TC_PASSWORD` (sesi A) dan `Spectra.env.AC_PF_SA_PASSWORD` (sesi B UI); nama `AC_PF_SA_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-593: Client baru ter-assign ke plan antara dialog Archive dibuka dan Confirm: guard dicek ulang dan dialog blok tampil

1. Sesi A: klik tab Custom, ketik Search `Paket Race Satu {runId}-015`, tekan Enter, buka Overlay Row Action `Paket Race Satu {runId}-015`, klik `Archive` sehingga dialog `Archive Plan` terbuka
2. Sesi B (sesi API): buat subscription berstatus Active untuk `PT Race Satu {runId}-015` pada plan itu hingga subscription tersimpan
3. Sesi A: klik `[Archive]`
4. Verifikasi dialog `Cannot Archive Plan` tampil dengan bullet `• PT Race Satu {runId}-015` dan tombol `[OK]`
5. Verifikasi tidak ada toast sukses
6. Sesi A: klik `[OK]`
7. Verifikasi `Paket Race Satu {runId}-015` tetap tampil di sub-tab Active
8. Sesi A: klik ikon Changelog pada toolbar tab Custom
9. Verifikasi modal Changelog Custom menampilkan sedikitnya satu entri
10. Verifikasi tidak ada entri Archive untuk `Paket Race Satu {runId}-015`
11. Tutup modal Changelog lewat `✕`
12. Sesi A: klik `(←)` pada kotak Search

### TC-AC-PF-594: Re-submit Archive pada plan yang sudah archived adalah no-op sukses tanpa entri log baru

13. Sesi A: ketik Search `Paket Archive Ganda {runId}-015`, tekan Enter
14. Sesi B: buka konteks browser kedua, login sebagai Total Control kedua (Principal), buka Plans & Licensing > Plans & Features, klik tab Custom, ketik Search `Paket Archive Ganda {runId}-015`, tekan Enter
15. Sesi A: buka Overlay Row Action `Paket Archive Ganda {runId}-015`, klik `Archive` sehingga dialog `Archive Plan` terbuka
16. Sesi B: buka Overlay Row Action `Paket Archive Ganda {runId}-015`, klik `Archive` sehingga dialog `Archive Plan` terbuka
17. Sesi A: klik `[Archive]`
18. Verifikasi sesi A menampilkan toast sukses: "Success, plan has been archived."
19. Sesi B: klik `[Archive]`
20. Verifikasi sesi B menampilkan toast sukses yang sama: "Success, plan has been archived." (no-op sukses, bukan error)
21. Sesi A: klik sub-tab Archive
22. Sesi A: klik ikon Changelog pada toolbar tab Custom
23. Verifikasi modal Changelog Custom menampilkan entri Archive untuk `Paket Archive Ganda {runId}-015`
24. Verifikasi Changelog memuat tepat satu entri Archive untuk `Paket Archive Ganda {runId}-015`
25. Tutup modal Changelog lewat `✕`

### TC-AC-PF-598: Edit yang dikirim setelah plan di-archive oleh sesi lain ditolak tanpa kenaikan versi

26. Sesi A: klik menu Plans & Licensing > Plans & Features di sidebar, klik tab Custom, ketik Search `Paket Edit Archive {runId}-015`, tekan Enter, buka Overlay Row Action `Paket Edit Archive {runId}-015`, klik `Edit`, ubah Group count `3` menjadi `25`
27. Sesi B (sesi API): Archive `Paket Edit Archive {runId}-015` hingga status archived tersimpan
28. Sesi A: klik `[Save]`
29. Sesi A: klik segmen Breadcrumb `Plans & Features`
30. Verifikasi sesi A menampilkan dialog `Unsaved Changes`
31. Sesi A: klik `[Leave]`
32. Sesi A: klik tab Custom, lalu klik sub-tab Archive
33. Verifikasi `Paket Edit Archive {runId}-015` tampil di sub-tab Archive
34. Verifikasi kolom Version `Paket Edit Archive {runId}-015` tetap `v1`
35. Sesi A: klik teks `Paket Edit Archive {runId}-015` pada kolom Plan Name
36. Verifikasi Plan Detail menampilkan Group count `3` (nilai lama)
37. Sesi A: klik menu Plans & Licensing > Plans & Features di sidebar, lalu klik tab Custom
38. Sesi A: klik ikon Changelog pada toolbar tab Custom
39. Verifikasi modal Changelog Custom menampilkan entri Archive untuk `Paket Edit Archive {runId}-015`
40. Verifikasi tidak ada entri Edit untuk `Paket Edit Archive {runId}-015`
41. Tutup modal Changelog lewat `✕`

## Notes

- P-1: asersi absence entri Changelog pada langkah 10 dan 40 (TC-AC-PF-593 dan TC-AC-PF-598) tetap di spec ini karena konteksnya bergantung pada state dua sesi yang baru dibangun langkah sebelumnya (dialog Archive terbuka sebelum client ditambahkan; form Edit terbuka sebelum plan di-archive); baseline-nya nama plan bersuffix (baseline nol) dan anchor positif langkah 9 serta langkah 39 (S-05, S-12, bagian 8b butir 2).
- Langkah penghubung (S-03): klik tab, sub-tab, atau menu sidebar pada langkah 1, 21, 26, 32, dan 37 mengarahkan layar ke tab yang disyaratkan precondition TC; Search pada langkah 1, 13, 14, dan 26 untuk menemukan baris target (R-16); langkah 12 mengosongkan Search; penutupan modal pada langkah 11 dan 25 membuka jalan bagi langkah berikutnya; langkah 29 sampai 31 menutup form Edit yang dirty setelah Save ditolak (S-08, S-09).
- Plan uji memakai nama bersuffix (S-12) sebagai ganti `Paket Tanpa Client` (Dataset Plan G) agar TC-AC-PF-593, TC-AC-PF-594, dan TC-AC-PF-598 tidak saling bergantung (S-06); client `PT Race Satu` ditulis dengan suffix sehingga bullet dialog pada langkah 4 memuat nama bersuffix.
- Alasan di atas sekitar 35 langkah (41 langkah): ketiga blok satu kelas harness (c multi-konteks, state plan diubah sesi lain saat dialog atau form terbuka) dan satu topik (konflik Archive), tiap blok memakai plan sendiri dan berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-PF-593: Pre-setup #46 menyebut "akun Allocation" untuk sesi B tanpa email; spec memakai sesi API dengan akun yang disediakan tim FE (hanya memicu perubahan state).
  - TC-AC-PF-598: Expected "Save ditolak server" tidak menyebut pesan atau state form di UI sesudah penolakan; spec tidak mengasersi pesan penolakan dan menutup form lewat klik segmen Breadcrumb `Plans & Features` serta `[Leave]` (langkah 29 sampai 31) dengan asumsi form tetap terbuka dan dirty. Mohon QA melengkapi perilaku UI.

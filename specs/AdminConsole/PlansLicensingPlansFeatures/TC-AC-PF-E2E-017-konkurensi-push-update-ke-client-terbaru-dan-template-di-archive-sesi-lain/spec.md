---
id: TC-AC-PF-E2E-017-konkurensi-push-update-ke-client-terbaru-dan-template-di-archive-sesi-lain
title: "Konkurensi: Template Di-archive Sesudah Form Create Dibuka dan Push Update ke Client yang Sudah Terbaru"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-597
  - TC-AC-PF-599
coverage:
  web: automated
---

# Konkurensi: Template Di-archive Sesudah Form Create Dibuka dan Push Update ke Client yang Sudah Terbaru

## Prerequisites

- Mode: FE+BE.
- Akun sesi A (aktor pertama): Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Akun sesi B pada TC-AC-PF-597 (konteks browser kedua): Total Control Principal kedua `secondAdminPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Rina Kusuma`, Pre-setup #9), password dari `Spectra.env.AC_PF_SA_PASSWORD`. Pelaku sesi B pada TC-AC-PF-599 hanya memicu Archive Template lewat sesi API (akun disediakan tim FE). Kelas harness: c multi-konteks.
- Login sesi A di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Sesi B (UI) login pada langkah 22 di konteks browser kedua; hook `after` menutup konteks kedua dan mengembalikan sesi ke akun default suite.
- Data Pre-setup (hook `before`): Dataset Plan Y (Pre-setup #37: default FAMS tanpa subscription: Starter Free, Growth, Professional, Enterprise Paid) untuk TC-AC-PF-599; Dataset Plan Y menggantikan default plan Dataset Plan A selama blok TC-AC-PF-599 karena slot Free dan Paid per Product terbatas. Dataset Plan P (Pre-setup #28): custom plan Principal `Paket Push` v3 (v1 Group count 3, Open API OFF; v2 Group count 25; v3 Open API ON dan API call quota 100K/month) dengan `PT Push Dua` Active v2 (eligible Push Update) untuk TC-AC-PF-597; Dataset Plan A dipulihkan sebelum blok TC-AC-PF-597. General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Data Dinamis milik spec (bersuffix): custom plan gagal dibuat `Paket Template Basi {runId}-017` (TC-AC-PF-599).
- Pengecualian S-06/S-12 butir A-14: default plan `Enterprise` (Dataset Plan Y) dan custom plan `Paket Push` dengan `PT Push Dua` (Dataset Plan P) menjadi target aksi tulis karena berupa data Pre-setup yang tidak dapat dimiliki spec (slot default plan terbatas; histori versi client). Pemulihan ke keadaan awal dijamin fixture BE yang idempoten (disediakan tim FE/BE): dijalankan di hook `before` dan `after` serta pada langkah 21 dan 37. Efek yang tersisa dan tidak dapat dipulihkan lewat UI: Last Updated plan dan entri Changelog Archive `Enterprise` dan Push Update `PT Push Dua` (Changelog permanen). Suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`) untuk kedua akun; spec ini tidak mengubahnya.
- Kemampuan teknis: konteks browser kedua dengan login akun #9; sesi API aktor untuk memicu Archive `Enterprise` (langkah 2) tanpa endpoint karangan (S-13, R-20); kemampuan membaca jumlah entri Changelog sebelum aksi (bagian 8b butir 10); fixture BE (pemulihan Dataset) disediakan tim FE/BE (lihat `suite.md`).
- Env var: `Spectra.env.AC_TC_PASSWORD` (sesi A) dan `Spectra.env.AC_PF_SA_PASSWORD` (sesi B UI); nama `AC_PF_SA_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-599: Template di-archive sesudah form Create Custom Plan dibuka: Submit ditolak dan custom plan tidak dibuat

1. Sesi A: klik tab Custom, klik `+ Custom Plan`, pilih Product `FAMS`, pilih Template `Enterprise`, isi Plan Name `Paket Template Basi {runId}-017`
2. Sesi B (sesi API): Archive default plan `Enterprise` hingga status archived tersimpan
3. Sesi A: klik `[Submit]`
4. Verifikasi pesan inline `This template no longer exists. Please select another.` tampil tepat di bawah dropdown Template
5. Verifikasi tidak ada toast sukses
6. Verifikasi field Template dikosongkan otomatis
7. Sesi A: buka dropdown Template
8. Verifikasi opsi Template dimuat ulang tanpa `Enterprise`
9. Verifikasi Product `FAMS` dan Plan Name `Paket Template Basi {runId}-017` tetap dipertahankan
10. Verifikasi form tetap terbuka
11. Sesi A: klik segmen `Plans & Features` pada breadcrumb
12. Verifikasi dialog `Unsaved Changes` tampil
13. Sesi A: klik `[Leave]`
14. Sesi A: klik tab Custom, ketik Search `Paket Template Basi {runId}-017`, tekan Enter
15. Verifikasi empty state `No results found` tampil dan `Paket Template Basi {runId}-017` tidak ada di sub-tab Active
16. Sesi A: klik `(←)` pada kotak Search
17. Sesi A: klik ikon Changelog pada toolbar tab Custom
18. Verifikasi modal Changelog Custom menampilkan sedikitnya satu entri
19. Verifikasi tidak ada entri Create untuk `Paket Template Basi {runId}-017`
20. Tutup modal Changelog lewat `✕`
21. Pulihkan Dataset Plan Y (default plan `Enterprise` kembali aktif) dan kembalikan Dataset Plan A lalu pasang Dataset Plan P lewat fixture BE hingga tersimpan

### TC-AC-PF-597: Push Update ke client yang sudah di versi terbaru adalah no-op sukses tanpa entri log

22. Sesi B: buka konteks browser kedua, login sebagai Total Control kedua (Principal), buka Plans & Licensing > Plans & Features, klik tab Custom, buka Plan Detail `Paket Push`, klik Tab Assigned Clients
23. Sesi A: klik menu Plans & Licensing > Plans & Features di sidebar, klik tab Custom, klik ikon Changelog pada toolbar tab Custom
24. Catat jumlah entri Push Update untuk `PT Push Dua` pada Changelog Custom (baseline N0) lewat kemampuan baca yang disediakan tim FE/BE
25. Tutup modal Changelog lewat `✕`
26. Sesi A: buka Plan Detail `Paket Push`, klik Tab Assigned Clients, buka Overlay Row Action `PT Push Dua`, klik `Push Update` sehingga dialog `Push Plan Update` terbuka
27. Sesi B: buka Overlay Row Action `PT Push Dua`, klik `Push Update` sehingga dialog `Push Plan Update` terbuka
28. Sesi A: klik `[Push Update]`
29. Verifikasi sesi A menampilkan toast sukses: "Success, plan update has been pushed."
30. Sesi B: klik `[Push Update]`
31. Verifikasi sesi B menampilkan toast sukses yang sama: "Success, plan update has been pushed." (no-op sukses)
32. Verifikasi Plan Version `PT Push Dua` pada Tab Assigned Clients sesi A tetap `v3`
33. Sesi A: klik menu Plans & Licensing > Plans & Features di sidebar, klik tab Custom, klik ikon Changelog pada toolbar tab Custom
34. Verifikasi Changelog memuat entri Push Update untuk `PT Push Dua`
35. Verifikasi jumlah entri Push Update untuk `PT Push Dua` bertambah tepat satu dari N0
36. Tutup modal Changelog lewat `✕`
37. Pulihkan `PT Push Dua` ke v2 lewat fixture BE hingga tersimpan

## Notes

- P-1: asersi `tepat satu entri` pada langkah 35 dan absence entri Create pada langkah 19 bergantung pada state dua sesi yang baru dibangun langkah sebelumnya; baseline berupa jumlah entri sebelum aksi (langkah 24) atau nama plan bersuffix (baseline nol) dengan anchor positif langkah 18 dan 34 (S-12, bagian 8b butir 2 dan 10).
- Langkah penghubung (S-03): klik tab Custom dan klik menu sidebar pada langkah 1, 14, 22, 23, dan 33 mengarahkan layar ke tab yang disyaratkan precondition TC; Search pada langkah 14 untuk menemukan baris target (R-16); langkah 16 mengosongkan Search; penutupan modal pada langkah 20, 25, dan 36 membuka jalan bagi langkah berikutnya; langkah 11 sampai 13 menutup form dirty lewat breadcrumb sesuai langkah TC (S-08, `Verifikasi` dialog `Unsaved Changes`); langkah 21 dan 37 memulihkan data Pre-setup (S-06, A-6).
- Nama plan memakai suffix `{runId}-017` (S-12) sebagai ganti `Paket Template Basi` pada TC-AC-PF-599.
- Alasan di atas sekitar 35 langkah (37 langkah): kedua blok satu kelas harness (c multi-konteks, state diubah sesi lain sesudah form atau dialog dibuka) dan satu topik (konflik dua sesi), tiap blok memakai dataset sendiri dan berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; kelebihan dua langkah berasal dari baseline Changelog (bagian 8b butir 10) dan pemulihan data Pre-setup (langkah 21 dan 37).
- TC-AC-PF-79 dan TC-AC-PF-567 ada di spec 025.
- Temuan untuk QA:
  - TC-AC-PF-599: Expected a ("Server menolak permintaan karena Template sudah archived") tidak teramati di UI; spec mengasersi pesan inline dan keadaan form (Expected b, c, d) saja.
  - TC-AC-PF-599: precondition "Dataset Plan Y" berbenturan dengan Dataset Plan A (slot Free dan Paid per Product); spec menggantikan Dataset Plan A lewat fixture BE selama blok ini.
  - TC-AC-PF-597: Expected "versi client tetap `v3`" mengandaikan `PT Push Dua` sudah di versi terbaru, sedangkan Dataset Plan P mencatat `PT Push Dua` Active v2 sebelum Push Update; spec mengasersi `v3` sesudah Push Update sesi A dan sesudah Push Update sesi B.

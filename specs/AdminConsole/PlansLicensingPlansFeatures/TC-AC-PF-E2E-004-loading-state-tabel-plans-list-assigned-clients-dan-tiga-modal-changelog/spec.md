---
id: TC-AC-PF-E2E-004-loading-state-tabel-plans-list-assigned-clients-dan-tiga-modal-changelog
title: "Loading State Tabel Plans List, Tab Assigned Clients, dan Tiga Modal Changelog"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-17
  - TC-AC-PF-684
  - TC-AC-PF-685
  - TC-AC-PF-686
  - TC-AC-PF-687
coverage:
  web: automated
---

# Loading State Tabel Plans List, Tab Assigned Clients, dan Tiga Modal Changelog

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata: `Spectra.intercept` hanya menahan respons agar state Loading teramati, lalu dilepas; tidak ada respons yang dipalsukan).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21: Starter, Growth, Professional, Enterprise, SIEM aktif), Dataset Plan D (Pre-setup #24: `Growth` v5 dengan 9 client), Dataset Log D (Pre-setup #40: Changelog Default 5 entri), Dataset Log C (Pre-setup #41: Changelog Custom Principal 6 entri), Dataset Log G (Pre-setup #42: Changelog Global Settings 5 entri). General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal `Growth` dipakai karena Dataset Plan D menentukan baris client yang tampil; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset ke keadaan awal lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: `Spectra.intercept` untuk menunda respons daftar plan, daftar client, dan daftar Changelog (URL request tidak disebut di TC, PRD, atau LLD yang dibaca; pola intercept disediakan tim FE tanpa endpoint karangan, S-13); fixture BE dan sesi API aktor disediakan tim FE/BE (lihat `suite.md`).
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-17: Loading state tabel Plans List tampil saat data sedang diambil

1. Pasang intercept yang menunda respons daftar plan
2. Muat ulang halaman dengan F5
3. Verifikasi area tabel menampilkan Loading component (Shimmer)
4. Verifikasi area tabel bukan empty state maupun pesan error
5. Lepas tahanan respons daftar plan dan lepas intercept
6. Verifikasi baris Dataset Plan A (Starter, Growth, Professional, Enterprise, SIEM) tampil

### TC-AC-PF-684: Loading state Tab Assigned Clients tampil saat data client sedang diambil

7. Klik teks `Growth` pada kolom Plan Name untuk membuka Plan Detail
8. Pasang intercept yang menunda respons daftar client
9. Klik Tab Assigned Clients
10. Verifikasi area tabel Tab Assigned Clients menampilkan Loading component (Shimmer)
11. Verifikasi area tabel bukan empty state maupun pesan error
12. Lepas tahanan respons daftar client dan lepas intercept
13. Verifikasi baris client Dataset Plan D (9 client `Growth` v5) tampil

### TC-AC-PF-685: Loading state modal Changelog Default tampil saat riwayat sedang diambil

14. Klik menu Plans & Licensing > Plans & Features di sidebar
15. Pasang intercept yang menunda respons daftar Changelog
16. Klik ikon Changelog pada toolbar tab Default
17. Verifikasi area tabel modal Changelog Default menampilkan Loading component (Shimmer)
18. Verifikasi area tabel modal bukan empty state maupun pesan error
19. Lepas tahanan respons daftar Changelog dan lepas intercept
20. Verifikasi entri Changelog Default tampil
21. Tutup modal Changelog lewat `✕`

### TC-AC-PF-686: Loading state modal Changelog Custom tampil saat riwayat sedang diambil

22. Klik tab Custom
23. Pasang intercept yang menunda respons daftar Changelog
24. Klik ikon Changelog pada toolbar tab Custom
25. Verifikasi area tabel modal Changelog Custom menampilkan Loading component (Shimmer)
26. Verifikasi area tabel modal bukan empty state maupun pesan error
27. Lepas tahanan respons daftar Changelog dan lepas intercept
28. Verifikasi entri Changelog Custom tampil
29. Tutup modal Changelog lewat `✕`

### TC-AC-PF-687: Loading state modal Changelog Global Settings tampil saat riwayat sedang diambil

30. Klik tab Global Settings
31. Pasang intercept yang menunda respons daftar Changelog
32. Klik ikon Changelog di pojok kanan atas Card
33. Verifikasi area tabel modal Changelog Global Settings menampilkan Loading component (Shimmer)
34. Verifikasi area tabel modal bukan empty state maupun pesan error
35. Lepas tahanan respons daftar Changelog dan lepas intercept
36. Verifikasi entri Changelog Global Settings tampil
37. Tutup modal Changelog lewat `✕`

## Notes

- Langkah penghubung (S-03): langkah 14 mengembalikan layar ke Default > Active sesudah Plan Detail; klik tab pada langkah 22 dan 30 mengarahkan layar ke tab yang disyaratkan precondition TC; penutupan modal pada langkah 21, 29, dan 37 membuka jalan bagi langkah berikutnya. Intercept dilepas segera setelah asersi Loading (S-09).
- Menahan respons hanya untuk mengamati state UI (Loading) bukan kelas b (fault injection); spec tetap fungsional (bagian 3 prinsip 13 butir b).
- Alasan di atas sekitar 35 langkah (37 langkah): kelima blok satu kelas harness (tahan respons untuk mengamati Loading), setiap blok pada surface sendiri dengan dataset sendiri dan berdiri sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; tiap Expected dipecah satu `Verifikasi` per klausa (S-01).
- Temuan untuk QA:
  - TC-AC-PF-17: Expected b menyebut "baris Dataset Plan A tampil" tanpa menyebut baris tertentu; spec menulis kelima baris Dataset Plan A.

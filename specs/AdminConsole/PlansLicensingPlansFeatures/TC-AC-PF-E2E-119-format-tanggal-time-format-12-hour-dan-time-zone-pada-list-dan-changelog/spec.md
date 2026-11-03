---
id: TC-AC-PF-E2E-119-format-tanggal-time-format-12-hour-dan-time-zone-pada-list-dan-changelog
title: "Format Tanggal, Time Format 12-hour, dan Time Zone General Settings pada List, Assigned Clients, dan Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-549
  - TC-AC-PF-767
  - TC-AC-PF-768
  - TC-AC-PF-769
  - TC-AC-PF-770
coverage:
  web: automated
---

# Format Tanggal, Time Format 12-hour, dan Time Zone General Settings pada List, Assigned Clients, dan Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Data Pre-setup (hanya dibaca, tidak diubah): Dataset Plan A (Pre-setup #21: `Starter`, `Growth`, `SIEM`, `Enterprise` dengan Last Modified 15 Jun 26 10:00, 15 Jun 26 10:00, 09 Jul 26 11:00, 12 Aug 26 09:00), Dataset Plan C (Pre-setup #23: `alpha Tier` 05 Jun 26 09:00, `Beta Pro` 18 Jun 26 14:30, `Zeta Max` 28 Jun 26 16:00), Dataset Plan D (Pre-setup #24: `Growth` dengan `PT Wahana Nusantara` Assigned Date 05 Jun 26), dan Dataset Log D (Pre-setup #40: Changelog Default 5 entri, dipulihkan lewat Fixture BE di hook `before` sehingga kelima entri berada di halaman pertama; S-14). Waktu tersimpan data uji dinyatakan dalam UTC. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix pada data Pre-setup, hanya dibaca).
- Mengubah General Settings (state global, Pre-setup #44 dan #61): Date Format, Time Format, dan Time Zone diatur lewat Fixture BE (disediakan tim FE/BE) pada langkah 1, 9, dan 19, lalu dipulihkan ke baseline (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) pada langkah 28 dan di hook `after`. Suite serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk mengatur dan memulihkan General Settings serta memulihkan Dataset Log D.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.

## Test Steps

### TC-AC-PF-549: Date Format `dd/MM/yy` pada Last Modified, Assigned Date, dan Date Changelog

1. Atur General Settings Date Format `dd/MM/yy` (Time Format 24-hour, Time Zone UTC) lewat Fixture BE, lalu muat ulang halaman Plans & Features
2. Verifikasi Last Modified baris `Growth` pada tab Default sub-tab Active `15/06/26, 10:00`
3. Buka Plan Detail `Growth`, lalu klik Tab Assigned Clients
4. Verifikasi Assigned Date baris `PT Wahana Nusantara` mengikuti `dd/MM/yy` (`05/06/26`)
5. Kembali ke Plans List tab Default sub-tab Active
6. Klik ikon Changelog pada toolbar tab Default
7. Verifikasi Date entri `Create` `Enterprise` mengikuti `dd/MM/yy` (`12/08/26, 09:00`)
8. Tutup modal Changelog

### TC-AC-PF-767: Time Format 12-hour pada Last Modified tab Custom

9. Atur General Settings Date Format `dd MMM yy`, Time Format 12-hour, Time Zone UTC lewat Fixture BE, muat ulang halaman Plans & Features, lalu klik tab `Custom` sub-tab `Active`
10. Verifikasi Last Modified baris `alpha Tier` `05 Jun 26, 09:00 AM`
11. Verifikasi Last Modified baris `Beta Pro` `18 Jun 26, 02:30 PM`
12. Verifikasi Last Modified baris `Zeta Max` `28 Jun 26, 04:00 PM`

### TC-AC-PF-768: Time Format 12-hour pada Date modal Changelog Default

13. Klik tab `Default` sub-tab `Active`
14. Klik ikon Changelog pada toolbar tab Default
15. Verifikasi Date entri `Create` `Enterprise` `12 Aug 26, 09:00 AM`
16. Verifikasi Date entri `Delete` `Pilot Default` `10 Jul 26, 12:00 PM`
17. Verifikasi Date entri `Edit` `Growth` `05 Jun 26, 03:40 PM`
18. Tutup modal Changelog

### TC-AC-PF-769: Time Zone Asia/Jakarta pada Last Modified tab Default

19. Atur General Settings Date Format `dd MMM yy`, Time Format 24-hour, Time Zone Asia/Jakarta (UTC+07:00) lewat Fixture BE, lalu muat ulang halaman Plans & Features
20. Verifikasi Last Modified baris `Starter` `15 Jun 26, 17:00`
21. Verifikasi Last Modified baris `SIEM` `09 Jul 26, 18:00`
22. Verifikasi Last Modified baris `Enterprise` `12 Aug 26, 16:00`

### TC-AC-PF-770: Time Zone Asia/Jakarta pada Date modal Changelog Default

23. Klik ikon Changelog pada toolbar tab Default
24. Verifikasi Date entri `Create` `Enterprise` `12 Aug 26, 16:00`
25. Verifikasi Date entri `Delete` `Pilot Default` `10 Jul 26, 19:00`
26. Verifikasi Date entri `Edit` `Growth` `05 Jun 26, 22:40`
27. Tutup modal Changelog
28. Pulihkan General Settings ke baseline (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) lewat Fixture BE

## Notes

- Langkah penghubung (S-03): pengaturan dan pemulihan General Settings lewat Fixture BE disertai muat ulang halaman supaya format baru terbaca (langkah 1, 9, 19, 28), buka Plan Detail dan Tab Assigned Clients lalu kembali ke Plans List (langkah 3 dan 5), pindah tab dan sub-tab (langkah 13), dan tutup modal Changelog (langkah 8, 18, 27).
- Pembagian TC lintas spec: TC-AC-PF-771 sampai TC-AC-PF-776 (Date Format pada kotak input date range Filter Panel) ada di spec 120.
- Baris yang diasersi dijamin berada di halaman teramati: baris Pre-setup bernama literal (Dataset Plan A dan C) dan lima entri Dataset Log D yang dipulihkan di hook `before` (S-14).
- Temuan untuk QA:
  - TC-AC-PF-549 Expected butir a menyebut "Last Modified `15/06/26, 10:00`" tanpa menyebut baris; spec memakai baris `Growth` (Last Modified 15 Jun 26 10:00 pada Dataset Plan A). Butir b dan c menyebut "contoh" nilai tanpa baris; spec memakai `PT Wahana Nusantara` (05 Jun 26) dan entri `Create` `Enterprise` (12 Aug 26, 09:00).
  - TC-AC-PF-549 precondition menyebut Dataset Plan D, tetapi Tabel Pre-setup mencantumkan TC-AC-PF-549 pada Dataset Plan A, D, dan Log D; General Settings varian (Pre-setup #61) tidak mencantumkan TC-AC-PF-549 (rentang #61 hanya TC-AC-PF-766 sampai TC-AC-PF-776).
  - Post Condition "Tidak ada perubahan data" tidak diasersi (S-01).

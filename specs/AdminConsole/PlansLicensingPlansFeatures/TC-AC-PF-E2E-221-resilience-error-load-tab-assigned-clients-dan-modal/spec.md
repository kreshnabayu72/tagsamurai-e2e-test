---
id: TC-AC-PF-E2E-221-resilience-error-load-tab-assigned-clients-dan-modal
title: "Resilience: Error Load Tab Assigned Clients dan Tiga Modal Changelog serta Try Again"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-452
  - TC-AC-PF-494
  - TC-AC-PF-679
  - TC-AC-PF-632
coverage:
  web: automated
---

# Resilience: Error Load Tab Assigned Clients dan Tiga Modal Changelog serta Try Again

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; TC mengasersi state backend).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Kelas harness: b fault injection / resilience.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan D (Pre-setup #24; default `Growth` v5 dengan 9 client, termasuk `PT Sejahtera Abadi`), Dataset Log D (Pre-setup #40; Changelog Default 5 entri), Dataset Log C (Pre-setup #41; Changelog Custom Principal 6 entri), dan Dataset Log G (Pre-setup #42; Changelog Global Settings 5 entri). General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Pengecualian S-06/S-12 butir A-14: nama Plan dan client Pre-setup literal tanpa suffix dipakai sebagai baris yang diasersi; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): `Spectra.intercept` parsial atas respons daftar client Tab Assigned Clients dan daftar Changelog Default, Custom, serta Global Settings yang dijawab server error (endpoint diidentifikasi tim FE; tidak tercantum di sumber TC), dilepas segera setelah pemicu (S-09); sesi API aktor.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-452: Error load Tab Assigned Clients menampilkan Unable to load this data. dengan Try Again

1. Klik teks `Growth` pada kolom Plan Name sehingga Plan Detail `Growth` terbuka
2. Pasang intercept: respons daftar client dijawab server error
3. Klik Tab Assigned Clients
4. Verifikasi area tabel menampilkan "Unable to load this data." dan `[Try Again]`
5. Verifikasi area tabel bukan empty state
6. Lepas intercept
7. Klik `[Try Again]`
8. Verifikasi baris client tampil (`PT Sejahtera Abadi`)

### TC-AC-PF-494: Error load modal Changelog Default menampilkan Unable to load this data. dengan Try Again

9. Klik segmen Breadcrumb `Plans & Features`
10. Pasang intercept: respons daftar Changelog dijawab server error
11. Klik ikon Changelog pada toolbar tab Default
12. Verifikasi modal Changelog Default menampilkan "Unable to load this data." dengan `[Try Again]`
13. Lepas intercept
14. Klik `[Try Again]`
15. Verifikasi entri Changelog Default tampil
16. Tutup modal Changelog lewat `✕`

### TC-AC-PF-679: Error load modal Changelog Custom menampilkan Unable to load this data. dengan Try Again

17. Klik tab Custom
18. Pasang intercept: respons daftar Changelog dijawab server error
19. Klik ikon Changelog pada toolbar tab Custom
20. Verifikasi modal Changelog Custom menampilkan "Unable to load this data." dengan `[Try Again]`
21. Lepas intercept
22. Klik `[Try Again]`
23. Verifikasi entri Changelog Custom tampil
24. Tutup modal Changelog lewat `✕`

### TC-AC-PF-632: Error load modal Changelog Global Settings menampilkan Unable to load this data. dengan Try Again

25. Klik tab Global Settings
26. Pasang intercept: respons daftar Changelog dijawab server error
27. Klik ikon Changelog di pojok kanan atas Card
28. Verifikasi modal Changelog Global Settings menampilkan "Unable to load this data." dengan `[Try Again]`
29. Verifikasi modal bukan empty state
30. Lepas intercept
31. Klik `[Try Again]`
32. Verifikasi lima entri Changelog Global Settings tampil
33. Tutup modal Changelog lewat `✕`

## Notes

- Langkah penghubung (S-03): langkah 9 mengembalikan layar ke list tab Default sesuai precondition TC-AC-PF-494; langkah 17 dan 25 mengarahkan layar ke tab yang disyaratkan precondition TC-AC-PF-679 dan TC-AC-PF-632; langkah 16, 24, dan 33 menutup modal.
- Asersi "bukan empty state" (langkah 5 dan 29) memakai tampilnya "Unable to load this data." pada area yang sama sebagai anchor positif (langkah 4 dan 28).
- Temuan untuk QA:
  - TC-AC-PF-494 dan TC-AC-PF-679: Expected setelah Try Again hanya menyebut "entri tampil" tanpa jumlah; spec tidak mengasersi jumlah entri.
  - TC-AC-PF-632: precondition menyebut "User berada di ... Global Settings", sedangkan TC-AC-PF-494 dan TC-AC-PF-679 memulai dari tab Default atau Custom; spec menambah langkah penghubung untuk berpindah tab.

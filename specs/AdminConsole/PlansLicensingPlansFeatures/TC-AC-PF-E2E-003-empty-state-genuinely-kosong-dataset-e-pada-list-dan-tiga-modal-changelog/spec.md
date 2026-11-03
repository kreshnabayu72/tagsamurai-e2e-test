---
id: TC-AC-PF-E2E-003-empty-state-genuinely-kosong-dataset-e-pada-list-dan-tiga-modal-changelog
title: "Empty State Genuinely Kosong (Dataset Plan E) pada Plans List dan Tiga Modal Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-19
  - TC-AC-PF-20
  - TC-AC-PF-21
  - TC-AC-PF-22
  - TC-AC-PF-23
  - TC-AC-PF-493
  - TC-AC-PF-519
  - TC-AC-PF-678
coverage:
  web: automated
---

# Empty State Genuinely Kosong (Dataset Plan E) pada Plans List dan Tiga Modal Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Akun kedua (hanya TC-AC-PF-23): Read Only Principal `readOnlyPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Dewi Lestari`, Pre-setup #2), password dari `Spectra.env.AC_PF_RO_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Ganti akun ke Read Only Principal ditulis eksplisit pada langkah 28 dan 29; hook `after` mengembalikan sesi ke akun default suite.
- Data: Dataset Plan E (Pre-setup #25): Principal tanpa default plan, tanpa custom plan, dan tanpa entri Changelog (Default, Custom, Global Settings) pada seluruh tab. Dataset ini mengosongkan tenant Principal yang dipakai semua spec lain, sehingga suite berjalan serial (`parallel: false`) dan spec ini dijalankan sesudah spec lain. Hook `before` mengosongkan tenant lewat fixture BE; hook `after` memulihkan baseline (Dataset Pre-setup) lewat fixture BE yang idempoten. Kemampuan fixture BE disediakan tim FE/BE. General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`) untuk kedua akun; spec ini tidak mengubahnya.
- Kemampuan teknis: fixture BE (pengosongan dan pemulihan tenant, termasuk entri Changelog) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: tenant Principal kosong selama spec berjalan; pemulihan di hook `after` seperti tertulis pada baris Data.
- Env var: `Spectra.env.AC_TC_PASSWORD` (akun #1) dan `Spectra.env.AC_PF_RO_PASSWORD` (akun #2); nama `AC_PF_RO_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-19: Empty state genuinely kosong pada tab sub-tab Default Active tanpa CTA

1. Verifikasi area tabel Default Active menampilkan Illustration, Title "No default plans yet", dan Description "System default plans will appear here."
2. Verifikasi tombol `+ Default Plan` tetap tampil di toolbar
3. Verifikasi tidak ada tombol CTA di area empty state

### TC-AC-PF-20: Empty state genuinely kosong pada tab sub-tab Default Archive tanpa CTA

4. Klik sub-tab Archive
5. Verifikasi area tabel Default Archive menampilkan Illustration, Title "No archived default plans", dan Description "Default plans you archive will appear here."
6. Verifikasi toolbar tidak memiliki tombol create dan area empty state tidak memiliki tombol CTA

### TC-AC-PF-21: Empty state genuinely kosong pada tab sub-tab Custom Archive tanpa CTA

7. Klik tab Custom
8. Klik sub-tab Archive
9. Verifikasi area tabel Custom Archive menampilkan Illustration, Title "No archived custom plans", dan Description "Custom plans you archive will appear here."
10. Verifikasi toolbar tidak memiliki tombol create dan area empty state tidak memiliki tombol CTA

### TC-AC-PF-22: Empty state tab Custom sub-tab Active menampilkan CTA [+ Custom Plan] untuk aktor dengan capability Create

11. Klik sub-tab Active
12. Verifikasi area tabel Custom Active menampilkan Illustration, Title "No custom plans yet", dan Description "Create a custom plan to configure specific feature sets for clients."
13. Verifikasi tombol `[+ Custom Plan]` tampil di area empty state
14. Klik tombol `[+ Custom Plan]` pada area empty state
15. Verifikasi halaman Plans & Licensing > Plans & Features > New Custom Plan terbuka
16. Tutup form New Custom Plan tanpa mengubah apa pun: klik segmen Breadcrumb `Plans & Features`

### TC-AC-PF-678: Empty state modal Changelog Custom belum ada riwayat

17. Klik tab Custom, lalu klik ikon Changelog pada toolbar tab Custom
18. Verifikasi modal Changelog Custom menampilkan Illustration, Title "No changelog yet", dan Description "Activities and changes will appear here."
19. Tutup modal Changelog lewat `✕`

### TC-AC-PF-493: Empty state modal Changelog Default belum ada riwayat

20. Klik tab Default
21. Klik ikon Changelog pada toolbar tab Default
22. Verifikasi modal Changelog Default menampilkan Illustration, Title "No changelog yet", dan Description "Activities and changes will appear here."
23. Tutup modal Changelog lewat `✕`

### TC-AC-PF-519: Empty state modal Changelog Global Settings belum ada riwayat

24. Klik tab Global Settings
25. Klik ikon Changelog di pojok kanan atas Card
26. Verifikasi modal Changelog Global Settings menampilkan Illustration, Title "No changelog yet", dan Description "Activities and changes will appear here."
27. Tutup modal Changelog lewat `✕`

### TC-AC-PF-23: Empty state tab Custom sub-tab Active tanpa tombol CTA untuk aktor Read Only

28. Ganti akun: Logout dari akun Total Control Principal
29. Login sebagai Read Only Principal (`readOnlyPrincipal_automated_{namaCompany}@qwertysystem.net`)
30. Klik menu Plans & Licensing > Plans & Features di sidebar
31. Klik tab Custom
32. Verifikasi area tabel Custom Active menampilkan Illustration, Title "No custom plans yet", dan Description "Create a custom plan to configure specific feature sets for clients."
33. Verifikasi area empty state tidak memuat tombol `[+ Custom Plan]`
34. Verifikasi toolbar tidak memuat tombol `+ Custom Plan`

## Notes

- Urutan blok: blok modal Changelog (TC-AC-PF-678, TC-AC-PF-493, TC-AC-PF-519) ditempatkan sebelum TC-AC-PF-23 karena TC-AC-PF-23 memakai akun kedua dan menutup spec (S-10, S-07); urutan TC sumber lain tidak berubah.
- Langkah penghubung (S-03): klik tab dan sub-tab pada langkah 4, 7, 8, 11, 17, 20, dan 24 mengarahkan layar ke tab yang disyaratkan precondition TC; langkah 16, 19, 23, dan 27 menutup form atau modal agar langkah berikutnya dapat berjalan; langkah 30 dan 31 membuka layar awal sesudah ganti akun.
- Pada TC-AC-PF-22 form New Custom Plan dibuka tanpa input sehingga penutupan lewat klik segmen Breadcrumb `Plans & Features` tidak memunculkan dialog Unsaved Changes.
- Temuan untuk QA:
  - TC-AC-PF-19 sampai TC-AC-PF-23, TC-AC-PF-493, TC-AC-PF-519, dan TC-AC-PF-678 membutuhkan Principal tanpa plan dan tanpa Changelog padahal akun #1 dipakai spec lain; spec mengosongkan lalu memulihkan tenant lewat fixture BE (mekanisme tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE tanpa endpoint karangan, S-13).
  - TC-AC-PF-22 Expected b menyebut "halaman New Custom Plan terbuka" tanpa menyebut cara menutupnya; spec menutup lewat klik segmen Breadcrumb `Plans & Features` sebagai langkah penghubung.
  - TC-AC-PF-23: Description empty state untuk aktor Read Only sama dengan aktor Create ("Create a custom plan to configure specific feature sets for clients."), yang mengundang instruksi Create bagi aktor yang tidak berhak; spec mengikuti TC.

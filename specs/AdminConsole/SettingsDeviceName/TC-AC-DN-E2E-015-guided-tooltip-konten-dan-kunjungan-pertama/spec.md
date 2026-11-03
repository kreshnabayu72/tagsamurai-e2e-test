---
id: TC-AC-DN-E2E-015-guided-tooltip-konten-dan-kunjungan-pertama
title: "Guided Tooltip: Konten Tiap Step dan Kunjungan Pertama"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-644
  - TC-AC-DN-645
coverage:
  web: automated
---

# Guided Tooltip: Konten Tiap Step dan Kunjungan Pertama

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Guided Fresh (Pre-setup #28) `Fixture.settings-device-name.guidedFresh` (email `guidedFresh_automated_{namaCompany}@qwertysystem.net`, nama tampil `Dewi Lestari`, Principal), password `Spectra.env.AC_DN_GUIDED_PASSWORD` (nama env berkode modul sesuai `suite.md`, didaftarkan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_DN_GUIDED_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name`; hook `before` suite menyetel flag `guided_tooltip_seen_ac-settings-device` ke `seen` untuk akun UI yang dipakai suite dan hook `after` suite memulihkannya. Spec ini memakai akun Pre-setup #28 dan mengatur flag sendiri sesudah hook (pengecualian bagian 4).
- Kemampuan teknis (disediakan tim FE/BE): menyetel flag `guided_tooltip_seen_ac-settings-device` akun uji menjadi belum diset sebelum tiap TC dan membaca nilainya; mengubah lebar viewport dan memulihkannya (minimal 1280 px pada awal tiap TC).
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Device Name inti (#16), baca-saja. Tidak ada data Dinamis. State global yang diubah: flag Guided Tooltip akun #28 (dipulihkan hook `after` suite).

## Test Steps

### TC-AC-DN-644: Walkthrough Guided Tooltip halaman Settings > Device: konten tiap step

1. Setel flag `guided_tooltip_seen_ac-settings-device` akun uji menjadi belum diset
2. Muat ulang halaman `Settings > Device > Device Name` (kunjungan pertama)
3. Verifikasi Step 1 of 6: spotlight pada sub-tab bar
4. Verifikasi Step 1 of 6: Title "Device Sections" dan Description "Move between the sections of the device catalog. Each section keeps its own search, filter, sort, and page while you stay on this page."
5. Verifikasi Step 1 of 6: tombol `[Skip]` dan `[Next]` tampil
6. Verifikasi Step 1 of 6: tombol `[Back]` Hidden
7. Klik `[Next]`
8. Verifikasi Step 2 of 6: spotlight pada Category Sidebar yang terbuka
9. Verifikasi Step 2 of 6: Title "Category Tree" dan Description "Narrow the list to one or more device categories. The selection is shared by the sections that use categories."
10. Klik `[Next]`
11. Verifikasi Step 3 of 6: spotlight pada Search dan Filter di toolbar
12. Verifikasi Step 3 of 6: Title "Search and Filter" dan Description "Find a specific record or narrow the list. Available filters depend on the section you are on."
13. Klik `[Next]`
14. Verifikasi Step 4 of 6: spotlight pada ikon Changelog
15. Verifikasi Step 4 of 6: Title "Changelog" dan Description "Review who changed what and when for the section you are on."
16. Klik `[Next]`
17. Verifikasi Step 5 of 6: spotlight pada tabel utama
18. Verifikasi Step 5 of 6: Title "Device List" dan Description "Browse the records of the current section. Click a column header to sort the list."
19. Klik `[Next]`
20. Verifikasi Step 6 of 6: spotlight pada header kolom Actions
21. Verifikasi Step 6 of 6: Title "Column Visibility" dan Description "Choose which columns to show and open Setup Column for more options. Available row actions depend on your access."
22. Verifikasi Step 6 of 6: tombol `[Next]` berubah menjadi `[Done]`
23. Klik `[Done]`

### TC-AC-DN-645: Walkthrough Guided Tooltip muncul otomatis pada kunjungan pertama dan tidak muncul lagi setelah ditutup

24. Setel flag `guided_tooltip_seen_ac-settings-device` akun uji menjadi belum diset
25. Muat ulang halaman `Settings > Device > Device Name` (kunjungan pertama)
26. Verifikasi walkthrough tampil otomatis dimulai dari Step 1 of 6
27. Klik `[Skip]`
28. Muat ulang halaman dengan F5
29. Verifikasi Breadcrumb `Settings > Device > Device Name` tampil
30. Verifikasi setelah F5 walkthrough tidak muncul otomatis
31. Logout
32. Login ulang sebagai akun yang sama (`Fixture.settings-device-name.guidedFresh`, password `Spectra.env.AC_DN_GUIDED_PASSWORD`)
33. Buka halaman `Settings > Device > Device Name`
34. Verifikasi Breadcrumb `Settings > Device > Device Name` tampil
35. Verifikasi setelah login ulang walkthrough tidak muncul otomatis (flag `guided_tooltip_seen_ac-settings-device` tersimpan per akun)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 dan 24 menyetel flag sebelum tiap TC (kemampuan disediakan tim FE/BE); langkah 2 memuat ulang halaman untuk memicu kunjungan pertama; langkah 23 menutup walkthrough TC-AC-DN-644.
- Langkah 31 dan sesudahnya (Logout, login ulang akun yang sama) mengikuti langkah TC-AC-DN-645, bukan ganti akun (S-07).
- Judul dan isi (Title dan Description) tiap step ditulis satu `Verifikasi` per step karena Expected TC menyebutnya dalam satu butir tooltip.
- Asersi "tidak muncul otomatis" (setelah F5 dan login ulang) didahului `Verifikasi` Breadcrumb tampil sebagai anchor positif (bagian 8b butir 2, R-21).
- TC-AC-DN-646 (tombol `[?]`) berada di spec 023 karena memakai akun Pre-setup #1.
- Temuan untuk QA:
  - Pre-setup #28 hanya memberi email akun, tanpa nama env password; spec memakai `AC_DN_GUIDED_PASSWORD` sesuai pola `suite.md`.

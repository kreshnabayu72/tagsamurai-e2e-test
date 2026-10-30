---
id: TC-GS-UOM-E2E-010-guided-tooltip-konten-navigasi-keyboard
title: "Konten, Navigasi Keyboard, dan Step 1 Dilewati pada Guided Tooltip Tab Measurement"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-16
  - TC-GS-UOM-21
  - TC-GS-UOM-22
coverage:
  web: automated
---

# Konten, Navigasi Keyboard, dan Step 1 Dilewati pada Guided Tooltip Tab Measurement

## Prerequisites

- Mode: mock (seluruh API di-mock; dijalankan tim FE sebagai integration test tanpa backend nyata).
- Aktor yang dimodelkan lewat payload izin mock:
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` untuk TC-GS-UOM-16 dan TC-GS-UOM-21.
  - System Role: Read saja (Tono Hartono) `readCapability_automated_qaTeam1@qwertysystem.net` (capability Manage master reference: Read, tanpa Create) untuk TC-GS-UOM-22.
  - Sesi dibangun dari payload mock sehingga tidak ada login nyata dan tidak membutuhkan password. Bila spec dijalankan terhadap backend nyata, kredensial memakai `Spectra.env.GS_TC_PASSWORD` dan `Spectra.env.GS_READ_PASSWORD`.
- Kebutuhan mock (respons yang dipaksa; nama endpoint modul mengikuti `openapi.yaml` dan `low-level-design.md` modul Measurement):
  - Respons sesi/profil, menu, dan payload izin: Total Control (semua aksi Measurement) dan System Role: Read saja (hanya baca; tanpa Create sehingga Step 1 `[+ Unit]` dilewati). Disediakan tim FE (API pendukung di luar sumber modul).
  - Respons daftar Measurement: minimal 10 baris sehingga Table Tools (`[+ Unit]`, Search) dan tabel ter-render.
  - Respons daftar Brand: isi minimal supaya tab Brand (tab default saat Master Reference dibuka) ter-render sebelum Tab Measurement diklik.
  - Respons preferensi Guided Tooltip untuk flag `guided_tooltip_seen_gs-measurement`: belum ada (TC-GS-UOM-16; penyimpanan flag oleh `[Skip]` tidak mengubah respons selama TC itu), true (TC-GS-UOM-21 dan TC-GS-UOM-22). Flag `guided_tooltip_seen_gs-brand`: true. Disediakan tim FE.
- Tidak ada data backend atau state global yang diubah, sehingga tidak ada cleanup selain melepas mock di hook `after`.
- Spec ini menguji flag Guided Tooltip Measurement sehingga dikecualikan dari pernyataan hook suite (`suite.md`); pengaturan flag ada di Prerequisites dan langkah di atas.

## Test Steps

### TC-GS-UOM-16: Konten 2 step Guided Tooltip tab Measurement sesuai urutan

1. Terapkan mock sesi Total Control dengan flag `guided_tooltip_seen_gs-measurement` belum ada
2. Buka Global Settings > Master Reference, lalu klik Tab Measurement
3. Klik [Skip] untuk menutup walkthrough otomatis
4. Klik `[?]` di Breadcrumb
5. Baca Step 1
6. Verifikasi Step 1 menyorot tombol `[+ Unit]`
7. Verifikasi Step 1 menampilkan `Step 1 of 2`
8. Verifikasi Step 1 Title `Add a Measurement Unit`
9. Verifikasi Step 1 Description `Create a unit of measure (e.g. Kilogram, Liter) that products across the platform can use.`
10. Verifikasi tombol `[Back]` Hidden pada Step 1
11. Klik [Next]
12. Baca Step 2
13. Verifikasi Step 2 menyorot Search
14. Verifikasi Step 2 menampilkan `Step 2 of 2`
15. Verifikasi Step 2 Title `Find a Measurement`
16. Verifikasi Step 2 Description `Use search to find a measurement in this list.`
17. Verifikasi tombol `[Done]` menggantikan `[Next]` pada Step 2
18. Klik [Done] untuk menutup walkthrough

### TC-GS-UOM-21: Keyboard pada walkthrough: Esc, Enter, panah kanan, panah kiri

19. Terapkan mock flag `guided_tooltip_seen_gs-measurement` = true lalu muat ulang tab Measurement
20. Klik `[?]`
21. Tekan panah kanan
22. Verifikasi panah kanan berpindah ke Step 2
23. Tekan panah kiri
24. Verifikasi panah kiri kembali ke Step 1
25. Tekan Enter
26. Verifikasi Enter berpindah ke Step 2
27. Tekan Esc
28. Verifikasi Esc menutup walkthrough

### TC-GS-UOM-22: Step 1 dilewati bagi aktor tanpa capability Create

29. Ganti mock sesi ke System Role: Read saja (flag tetap true) lalu buka Global Settings > Master Reference > Measurement
30. Klik `[?]`
31. Verifikasi tour dimulai dari Step 2 `Find a Measurement`
32. Verifikasi Step yang menyorot `[+ Unit]` tidak ditampilkan
33. Verifikasi Step indicator memakai total step yang tampil
34. Tekan Esc untuk menutup walkthrough

## Notes

- Mode: mock. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-GS-UOM-16 mensyaratkan flag belum ada, sehingga walkthrough otomatis muncul saat tab dibuka. Langkah 2 sampai 3 menutup walkthrough otomatis itu agar `[?]` (langkah 4) bisa diklik dan Step 1 dan Step 2 dibaca dari awal. Perilaku walkthrough otomatis, Skip, dan penyimpanan flag diuji di spec `TC-GS-UOM-E2E-011-guided-tooltip-flag-seen-dan-dismiss`.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (mock sesi dan flag awal), 3 (Skip walkthrough otomatis), 18 dan 34 (Done atau Esc menutup walkthrough), 19 (mock flag true lalu muat ulang), 29 (ganti mock sesi ke System Role: Read saja).
- TC-GS-UOM-21 dan TC-GS-UOM-22 tidak menyebut kondisi flag; spec memakai flag true agar walkthrough hanya muncul lewat `[?]`.
- Asersi "Step 1 tidak ditampilkan" (langkah 32) memakai langkah 31 (Step 2 tampil) sebagai anchor positif pada surface yang sama.
- Readback respons mock tidak diasersi di spec ini (konvensi bagian 6, mock): isi respons mock list hanya menyediakan baris agar halaman ter-render.
- Temuan untuk QA:
  - TC-GS-UOM-22 Expected c menyebut "Step indicator memakai total step yang tampil" tanpa nilai literal; spec tidak menulis teks indicator (sumber lain menyebut `Step N of M`, tetapi nilai untuk satu step tidak disebut TC).
  - TC-GS-UOM-21 Expected d menyebut Esc "setara Skip" (menyimpan flag seen); pada spec mock hanya penutupan walkthrough yang diasersi, tanpa pembacaan flag.
  - Daftar lengkap endpoint yang dipanggil halaman pada kondisi tes (S-13): path dan skema endpoint disediakan tim FE sesuai `openapi.yaml` dan `low-level-design.md` modul.

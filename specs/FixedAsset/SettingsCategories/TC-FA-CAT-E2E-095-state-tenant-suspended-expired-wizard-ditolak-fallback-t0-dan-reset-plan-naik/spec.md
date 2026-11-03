---
id: TC-FA-CAT-E2E-095-state-tenant-suspended-expired-wizard-ditolak-fallback-t0-dan-reset-plan-naik
title: "State Tenant Suspended: Wizard Submit Ditolak, Fallback T-0 Tetap Berjalan, dan Reset Excess saat Plan Naik"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-303
  - TC-FA-CAT-319
  - TC-FA-CAT-544
coverage:
  web: automated
---

# State Tenant Suspended: Wizard Submit Ditolak, Fallback T-0 Tetap Berjalan, dan Reset Excess saat Plan Naik

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini pada client CatSuspended (Pre-setup #35); halaman dibuka hook `beforeEach` suite. Langkah 23 berganti akun ke Total Control client CatExcess (Pre-setup #31); hook `after` mengembalikan sesi ke akun default suite.
- Principal Automation (Pre-setup #11) lewat sesi API (butir hook suite di `suite.md`; akun disediakan tim FE) mengaktifkan kembali entitas lewat Admin Console (langkah 14 dan 28), mengubah status entitas CatExcess (langkah 26), dan menaikkan plan (langkah 27). Principal hanya pemicu perubahan state; tidak ada sesi UI kedua.
- Data Pre-setup #35 (CatSuspended, entitas Suspended, jumlah kategori melebihi cap plan). Varian yang disiapkan fixture backend (disediakan tim FE/BE): (a) pasca-T-0, Alert Category Consolidation tampil (TC-FA-CAT-303, disiapkan hook `before`); (b) downgrade terjadwal, jumlah kategori melebihi cap baru, entitas Suspended, T-0 belum tiba (TC-FA-CAT-319, langkah 11). Nama kategori seed #35 disediakan tim FE.
- Data Pre-setup #31 (CatExcess, plan Starter cap 5, 9 kategori): Excess `Furniture`, `Heavy Equipment`, `Vehicle`, `Old Parts`; usable `Electronics` (anak `Laptop`, `Monitor`), `Office`, `Spare Parts`.
- Waktu: T-0 dibaca dari data downgrade terjadwal client lewat API seeding (8b.3); jam server dan jam browser diatur bersama ke T-0 pada langkah 13 dan dipulihkan ke waktu nyata pada langkah 20 sebelum System Log dibuka (S-09; bagian 6 konvensi). Kemampuan disediakan tim FE/BE.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Modal Changelog per Action (NM untuk `Marked as Excess (Category Consolidation)`, NR untuk `Restored from Excess (Category Consolidation)`), Activity Log (NA), dan System Log akun (NS) sebelum aksi (S-12, 8b.10) pada langkah 12 dan 25.
- State yang diubah spec: status entitas, plan, dan jam server. Pemulihan seed, status entitas, plan, dan jam dilakukan fixture backend pada langkah 11, 20, dan 24 serta di hook `after` (tetap berjalan walau spec gagal di tengah). Suite berjalan serial (`parallel: false`).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-303: Wizard Submit pada entitas Suspended ditolak dengan toast baku

1. Klik `[Choose Categories]` pada Alert Category Consolidation
2. Centang `Keep usable` pada dua kategori dari seed Pre-setup #35
3. Klik `[Save Selection]`
4. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
5. Verifikasi halaman tetap di Categories tanpa redirect
6. Verifikasi popup Consolidation tetap terbuka
7. Verifikasi centang `Keep usable` pada kedua kategori tetap ada
8. Klik icon (✕) pada popup
9. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
10. Klik `[Leave]` pada dialog

### TC-FA-CAT-319: Fallback T-0 tetap berjalan pada entitas Suspended karena bukan aksi aktor

11. Pulihkan seed Pre-setup #35 ke varian (b) lewat fixture dan muat ulang halaman Categories
12. Catat baseline NM dan NS (System Log Total Control)
13. Majukan jam server dan jam browser ke T-0 hingga tersimpan
14. Principal Automation (sesi API) mengaktifkan kembali entitas lewat Admin Console hingga tersimpan
15. Buka Fixed Asset > Settings > Categories
16. Verifikasi kategori selain yang terlama sesuai cap baru berstatus Excess (hasil Fallback T-0 yang berjalan saat entitas Suspended)
17. Buka Modal Changelog dan filter Modified By `System`
18. Verifikasi Changelog bertambah baris `Marked as Excess (Category Consolidation)` dengan Modified By `System` (NM + jumlah kategori Excess)
19. Hapus filter Modified By dan tutup Modal Changelog
20. Pulihkan jam server dan jam browser ke waktu nyata hingga tersimpan (fixture, disediakan tim FE/BE)
21. Buka Detail User Total Control > Tab System Log
22. Verifikasi jumlah baris System Log Total Control sama dengan NS (Fallback tanpa System Log)

### TC-FA-CAT-544: Plan naik saat entitas Suspended, reset Excess tetap berjalan sebagai aksi sistem

23. Ganti akun: logout, lalu login sebagai Total Control client CatExcess (Pre-setup #31) dengan `Spectra.env.FA_TC_PASSWORD`
24. Pulihkan seed Pre-setup #31 (plan Starter, entitas aktif) lewat fixture dan muat ulang halaman Categories
25. Catat baseline NR, NA, dan NS (System Log Total Control)
26. Principal Automation (sesi API) mengubah status entitas CatExcess menjadi Suspended hingga tersimpan
27. Principal Automation (sesi API) menaikkan plan client CatExcess dari Starter ke Professional (cap 100) saat entitas Suspended hingga tersimpan
28. Principal Automation (sesi API) mengaktifkan kembali entitas hingga tersimpan
29. Buka Fixed Asset > Settings > Categories
30. Verifikasi `Heavy Equipment`, `Vehicle`, `Furniture`, dan `Old Parts` berstatus usable
31. Verifikasi Alert Category Consolidation hilang
32. Buka Modal Changelog dan filter Modified By `System`
33. Verifikasi Changelog bertambah tepat empat baris `Restored from Excess (Category Consolidation)` (NR + 4) dengan Modified By `System`, satu per node
34. Hapus filter Modified By, tutup Modal Changelog, dan buka Activity Log
35. Verifikasi Activity Log bertambah tepat empat baris `Restored from Excess (Category Consolidation)` (NA + 4) dengan Modified By `System`
36. Buka Detail User Total Control > Tab System Log
37. Verifikasi jumlah baris System Log Total Control sama dengan NS (tidak memuat baris itu)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Urutan TC: TC-FA-CAT-303 dan TC-FA-CAT-319 pada client CatSuspended (login hook `before`), lalu TC-FA-CAT-544 pada CatExcess karena berganti client (S-10).
- Principal Automation lewat sesi API bukan konteks kedua (tidak ada `P-2`).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 8 dan 10 (menutup popup dirty deterministik, S-08), 11 dan 24 (pemulihan seed), 12 dan 25 (baseline), 13 (pemicu T-0), 14, 26, 27, 28 (pemicu Principal), 15 dan 29 (navigasi), 19 dan 34 (menutup Modal Changelog), 20 (pemulihan jam sebelum System Log dibuka, S-09).
- Asersi jumlah langkah 22 dan 37 (System Log tidak memuat baris) memakai selisih terhadap baseline NS dan langkah 16 serta 35 sebagai anchor positif (8b.2).
- Temuan untuk QA:
  - TC-FA-CAT-303 menyebut "centang beberapa kategori" tanpa nama dan Pre-setup #35 tanpa daftar kategori; spec mencentang dua kategori dari seed yang disediakan tim FE.
  - TC-FA-CAT-303 Expected menyebut UI "di-refresh tanpa redirect" sekaligus popup tetap terbuka dengan seleksi; spec mengasersi tetap di halaman Categories dan popup beserta centang masih ada.
  - TC-FA-CAT-319 tidak menyebut jumlah kategori Excess; spec mengasersi selisih Changelog sebagai satu baris per kategori Excess dari seed.
  - TC-FA-CAT-303, 319, dan 544 mensyaratkan Pre-setup #35 tanpa email; spec memakai akun Total Control pada client CatSuspended yang disediakan tim FE.
- Spec melewati 35 langkah (37 langkah). Alasan: satu kelas harness dan satu dataset; langkah penghubung wajib (S-03, S-08, S-09) menambah langkah dan blok berdiri sendiri.

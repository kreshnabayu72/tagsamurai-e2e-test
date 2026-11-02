---
id: TC-FA-CAT-E2E-190-fallback-t0-kategori-terlama-urutan-nama-seleksi-di-bawah-cap-dan-downgrade-baru
title: "Fallback T-0: Kategori Terlama Tetap Usable, Urutan Nama A-Z, Seleksi di Bawah Cap, dan Downgrade Baru Mereset Status Submit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-308
  - TC-FA-CAT-309
  - TC-FA-CAT-310
  - TC-FA-CAT-311
coverage:
  web: automated
---

# Fallback T-0: Kategori Terlama Tetap Usable, Urutan Nama A-Z, Seleksi di Bawah Cap, dan Downgrade Baru Mereset Status Submit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini pada client CatPreT0 (Pre-setup #32); halaman dibuka hook `beforeEach` suite. Langkah 25 berganti akun ke Total Control client CatExcess (Pre-setup #31); hook `after` mengembalikan sesi ke akun default suite.
- Principal Automation (Pre-setup #11) lewat sesi API (butir hook suite di `suite.md`; akun disediakan tim FE) hanya memicu perubahan plan target pada langkah 27.
- Data Pre-setup #32 (CatPreT0, downgrade terjadwal Professional cap 100 ke Starter cap 5): 8 kategori `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear` (lima terlama), `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`. Varian yang disiapkan fixture backend (disediakan tim FE/BE): (a) tanpa seleksi tersimpan, T-0 belum tiba (langkah 1); (b) lima kategori berwaktu pembuatan identik `bravo`, `Alpha`, `charlie`, `Delta`, `echo` ditambah satu kategori lebih baru, cap plan baru 3, T-0 belum tiba (langkah 11); (c) seleksi tersimpan 4 kategori `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, cap plan baru 5, T-0 belum tiba (langkah 16).
- Data Pre-setup #31 (CatExcess) untuk TC-FA-CAT-311: Submit siklus sebelumnya meninggalkan 5 usable; varian disiapkan fixture pada langkah 26.
- Waktu: T-0 dibaca dari data downgrade terjadwal lewat API seeding (8b.3); jam server dan jam browser diatur bersama ke T-0 pada langkah 2, 12, 18, dan 28 (bagian 6 konvensi). Kemampuan disediakan tim FE/BE; hook `after` memulihkan jam dan seed Pre-setup #32 dan #31. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Modal Changelog per Modified By sebelum aksi (baseline, S-12).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-308: Fallback T-0 tanpa submit, lima kategori terlama tetap usable, Modified By System

1. Pulihkan Pre-setup #32 ke varian (a) lewat fixture dan muat ulang halaman Categories
2. Majukan jam server dan jam browser ke T-0 (T-0 tiba tanpa seleksi tersimpan) hingga tersimpan
3. Buka Fixed Asset > Settings > Categories
4. Verifikasi `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, dan `Epsilon Gear` (kategori terlama) berstatus usable
5. Verifikasi `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy` berstatus Excess
6. Verifikasi Alert Category Consolidation tampil untuk Total Control
7. Buka Modal Changelog dan filter Modified By `System`
8. Verifikasi Changelog memuat tiga baris `Marked as Excess (Category Consolidation)` dengan Modified By `System`
9. Verifikasi Last Updated ketiga node sama dengan waktu T-0
10. Hapus filter Modified By dan tutup Modal Changelog

### TC-FA-CAT-309: Fallback, waktu pembuatan sama diurutkan Category Name A-Z case-insensitive

11. Pulihkan Pre-setup #32 ke varian (b) lewat fixture dan muat ulang halaman Categories
12. Majukan jam server dan jam browser ke T-0 (cap 3) hingga tersimpan
13. Buka Fixed Asset > Settings > Categories
14. Verifikasi `Alpha`, `bravo`, dan `charlie` berstatus usable (tiga pertama menurut Category Name A-Z case-insensitive)
15. Verifikasi `Delta`, `echo`, dan kategori terbaru berstatus Excess

### TC-FA-CAT-310: Client yang sudah submit dengan usable di bawah atau sama dengan cap baru tidak terkena fallback

16. Pulihkan Pre-setup #32 ke varian (c) lewat fixture dan muat ulang halaman Categories
17. Catat baseline NS jumlah baris Changelog dengan Modified By `System`
18. Majukan jam server dan jam browser ke T-0 hingga tersimpan
19. Buka Fixed Asset > Settings > Categories
20. Verifikasi `Alpha Tech`, `Beta Tools`, `Gamma Parts`, dan `Delta Supply` berstatus usable sesuai hasil Submit sebelumnya
21. Verifikasi `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy` berstatus Excess sesuai hasil Submit sebelumnya
22. Buka Modal Changelog dan filter Modified By `System`
23. Verifikasi jumlah baris Changelog Modified By `System` sama dengan NS (tidak ada baris baru)
24. Hapus filter Modified By dan tutup Modal Changelog

### TC-FA-CAT-311: Downgrade baru mereset status sudah-submit, fallback berlaku bila usable lebih dari cap baru

25. Ganti akun: logout, lalu login sebagai Total Control client CatExcess (Pre-setup #31) dengan `Spectra.env.FA_TC_PASSWORD`
26. Pulihkan Pre-setup #31 lewat fixture ke keadaan Submit sebelumnya meninggalkan 5 usable dan muat ulang halaman Categories
27. Principal Automation (sesi API) menurunkan plan target downgrade CatExcess menjadi cap 3 hingga tersimpan
28. Majukan jam server dan jam browser ke T-0 (cap baru 3 berlaku, tanpa Submit ulang) hingga tersimpan
29. Buka Fixed Asset > Settings > Categories
30. Verifikasi tiga kategori terlama berstatus usable tanpa membawa hasil Submit siklus sebelumnya
31. Verifikasi kategori selain tiga terlama berstatus Excess
32. Buka Modal Changelog dan filter Modified By `System`
33. Verifikasi Changelog memuat baris `Marked as Excess (Category Consolidation)` dengan Modified By `System` untuk kategori yang menjadi Excess
34. Verifikasi node yang sebelumnya Excess dan masuk tiga terlama memiliki baris `Restored from Excess (Category Consolidation)`
35. Hapus filter Modified By dan tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah (35 langkah nominal). Alasan: seluruh blok satu kelas (harness eksternal: time-travel T-0 untuk Fallback) yang berdiri sendiri; tiap blok memulai dari varian seed sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-FA-CAT-311 diletakkan terakhir karena berganti client (S-10).
- Pemicu T-0 (kemampuan jam server) membentuk kondisi uji sekaligus objek uji Fallback; Principal Automation pada TC-FA-CAT-311 lewat sesi API bukan konteks kedua (tidak ada `P-2`).
- Spec 089 memuat TC-FA-CAT-305, 306, dan 307 (penerapan seleksi pra-T-0).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 11, 16, 26 (pemulihan varian), 2, 12, 18, 28 (pemicu T-0), 10, 24, 35 (menutup Modal Changelog dan menghapus filter), 17 (baseline).
- Asersi absence langkah 23 memakai selisih terhadap baseline NS (asersi jumlah, bukan kelas g) dan langkah 20 sampai 21 sebagai anchor positif.
- Temuan untuk QA:
  - TC-FA-CAT-310 tidak menyebut nama keempat kategori yang tersimpan; spec memakai empat kategori terlama CatPreT0.
  - TC-FA-CAT-311 mensyaratkan Pre-setup #31 dan #11 tanpa menyebut nama kategori yang menjadi tiga terlama; spec mengasersi berdasarkan urutan waktu pembuatan seed yang disediakan tim FE/BE.
  - TC-FA-CAT-311 berlabel "Manual Only, dua sesi paralel" tetapi pelaku kedua hanya memicu perubahan plan; ditulis lewat sesi API.
  - Kolom ACC TC-FA-CAT-311 menyebut Total Control pada client Pre-setup #31 yang berbeda dari client Pre-setup #32 TC lain di spec ini; spec berganti akun secara eksplisit.

---
id: TC-FA-CAT-E2E-172-format-tanggal-general-settings-di-semua-surface-categories
title: "Format Tanggal General Settings pada Tabel Utama, Filter, Modal Changelog, Popup Detail, dan Popup Category Consolidation"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-491
  - TC-FA-CAT-492
  - TC-FA-CAT-493
  - TC-FA-CAT-494
  - TC-FA-CAT-495
coverage:
  web: automated
---

# Format Tanggal General Settings pada Tabel Utama, Filter, Modal Changelog, Popup Detail, dan Popup Category Consolidation

## Prerequisites

- Mode: FE+BE.
- Akun login hook `before` spec ini: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Satu ganti akun eksplisit pada langkah 27 ke Total Control client CatExcess (Pre-setup #31) dengan `Spectra.env.FA_TC_PASSWORD` (TC-FA-CAT-495).
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- State global yang diubah spec: Date Format, Time Format, dan Time Zone di Global Settings > General Settings untuk client CatMain (langkah 2, 11, 19) dan client CatExcess (langkah 28). Nilai awal dibaca pada langkah 1 lewat kemampuan baca (disediakan tim FE/BE) dan dipulihkan hook `after` lewat API (disediakan tim FE/BE). Suite berjalan serial (`parallel: false`).
- Data milik spec (di-seed hook `before` lewat API; dibersihkan hook `after`): kategori `Date Fmt {runId}-172` (Code `DF172`, leaf) pada CatMain dengan Last Updated UTC yang dibaca lewat kemampuan baca (acuan konversi Asia/Jakarta pada langkah 6). Popup Detail `Laptop` (langkah 22; Pre-setup #20 dan #22) dan popup Category Consolidation CatExcess (langkah 31; Pre-setup #31 dengan Alert Category Consolidation) hanya dibaca.
- Jam server dan jam browser sinkron; Last Updated dibandingkan dengan waktu UTC kategori yang dibaca lewat kemampuan baca (S-12). Zona waktu yang diatur: Asia/Jakarta (UTC+7).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.

## Test Steps

1. Catat nilai awal Date Format, Time Format, dan Time Zone General Settings client CatMain

### TC-FA-CAT-491: Last Updated tabel utama (dd MMM yy, 24 jam, Asia/Jakarta)

2. Buka Global Settings > General Settings, atur Date Format `dd MMM yy`, Time Format 24 jam, dan Time Zone Asia/Jakarta, lalu simpan
3. Tunggu aksi selesai (perubahan tersimpan)
4. Buka Fixed Asset > Settings > Categories
5. Verifikasi kolom Last Updated baris `Date Fmt {runId}-172` berformat `dd MMM yy` 24 jam
6. Verifikasi waktu pada kolom Last Updated baris `Date Fmt {runId}-172` dikonversi ke zona Asia/Jakarta dari waktu UTC kategori

### TC-FA-CAT-492: Isian tanggal Filter Last Updated tabel utama

7. Buka Filter pada tabel utama
8. Pilih rentang tanggal Last Updated dari tanggal Last Updated kategori `Date Fmt {runId}-172` sampai tanggal yang sama
9. Verifikasi teks tanggal di kotak input date range ditampilkan dalam Date Format `dd MMM yy`
10. Tutup panel Filter dengan `Esc`

### TC-FA-CAT-493: Kolom Date dan filter Date Modal Changelog

11. Buka Global Settings > General Settings, atur Date Format `M/d/yy` dan Time Format 12 jam (Time Zone tetap Asia/Jakarta), lalu simpan
12. Tunggu aksi selesai (perubahan tersimpan)
13. Buka Fixed Asset > Settings > Categories
14. Buka Modal Changelog
15. Verifikasi kolom Date berformat `M/d/yy` dengan jam 12 jam
16. Buka Filter pada Modal Changelog dan pilih rentang tanggal Date
17. Verifikasi isian filter Date memakai Date Format `M/d/yy`
18. Tutup Modal Changelog

### TC-FA-CAT-494: Last Updated dan filter tabel Assets Popup Detail

19. Buka Global Settings > General Settings, atur Date Format `dd/MM/yy` dan Time Format 24 jam (Time Zone tetap Asia/Jakarta), lalu simpan
20. Tunggu aksi selesai (perubahan tersimpan)
21. Buka Fixed Asset > Settings > Categories
22. Buka Popup Detail `Laptop`
23. Verifikasi kolom Last Updated tabel Assets berformat `dd/MM/yy` 24 jam
24. Buka Filter tabel Assets dan pilih rentang tanggal Last Updated
25. Verifikasi isian filter Last Updated berformat `dd/MM/yy`
26. Tutup Popup Detail

### TC-FA-CAT-495: Last Updated dan filter popup Category Consolidation

27. Ganti akun: logout, lalu login sebagai Total Control (Pre-setup #1) client CatExcess dengan `Spectra.env.FA_TC_PASSWORD`
28. Buka Global Settings > General Settings, atur Date Format `dd MMM yy`, Time Format 24 jam, dan Time Zone Asia/Jakarta, lalu simpan
29. Tunggu aksi selesai (perubahan tersimpan)
30. Buka Fixed Asset > Settings > Categories
31. Klik `[Choose Categories]` pada Alert Category Consolidation
32. Verifikasi kolom Last Updated popup Category Consolidation berformat `dd MMM yy` 24 jam
33. Buka Filter pada popup Category Consolidation dan pilih rentang tanggal Last Updated
34. Verifikasi isian filter Last Updated mengikuti `dd MMM yy` 24 jam
35. Klik `✕` pada popup Category Consolidation

## Notes

- Langkah penghubung (S-03): langkah 1 (membaca nilai awal), langkah 3, 12, 20, 29 (menunggu perubahan General Settings tersimpan sebelum pindah surface), langkah 4, 13, 21, 30 (membuka Categories), langkah 10 (menutup panel Filter tanpa menerapkan rentang), langkah 18, 26, 35 (menutup modal atau popup, tidak dirty).
- Langkah pengaturan Date Format TC-FA-CAT-492 tidak diulang karena nilainya `dd MMM yy` sudah berlaku dari langkah 2; TC-FA-CAT-492 diletakkan tepat sesudah TC-FA-CAT-491 (urutan dikelompokkan menurut nilai General Settings, S-10).
- TC-FA-CAT-493 dan TC-FA-CAT-494 tidak menyebut Time Zone; spec mempertahankan Asia/Jakarta dari langkah 2.
- Tidak ada asersi format tanggal pada berkas export (TC-FA-CAT-496); TC itu bukan bagian spec ini.
- Temuan untuk QA:
  - TC-FA-CAT-495 hanya menyebut Pre-setup #20 padahal popup Category Consolidation hanya tersedia pada client dengan Alert Category Consolidation (CatMain tidak memilikinya); spec memakai CatExcess (Pre-setup #31) dengan ganti akun.
  - TC-FA-CAT-492 hanya menyebut `dd MMM yy` tanpa Time Format dan Time Zone; TC-FA-CAT-493 dan TC-FA-CAT-494 tidak menyebut Time Zone.
  - Tombol simpan pada Global Settings > General Settings dan penerapan rentang tanggal pada Filter tidak disebut TC; spec menulis "simpan" tanpa label tombol dan tidak menerapkan rentang.
  - TC tidak menyebut apakah General Settings berlaku per client; spec mengaturnya pada CatMain dan pada CatExcess.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.

---
id: TC-FA-PREF-E2E-130-sinkronisasi-asset-class-dan-tax-depreciation-class-threshold-dan-awal-tahun-pajak
title: "Sinkronisasi ke Asset Class dan Tax Depreciation Class: Threshold dan Awal Tahun Pajak"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-393
  - TC-FA-PREF-396
  - TC-FA-PREF-409
sourceRules: ["FAPREF-LOGIC-06c", "FAPREF-LOGIC-08b", "D-01", "PV-01", "FAPREF-LOGIC-03b", "PV-04", "PV-05", "FAPREF-LOGIC-02f"]
smoke: []
dependsOn: []
trace:
  "FAPREF-LOGIC-06c": 5
  "FAPREF-LOGIC-08b": 6
  "D-01": [10, 24]
  "PV-01": 10
  "FAPREF-LOGIC-03b": [15, 17, 20]
  "PV-04": 24
  "PV-05": 24
  "FAPREF-LOGIC-02f": 32
anchor: [31]
coverage:
  web: automated
---

# Sinkronisasi ke Asset Class dan Tax Depreciation Class: Threshold dan Awal Tahun Pajak

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth, entitas Active) seri PC (PC-1): modul akuntansi aktif; Preferences bernilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents Sell/Scrap/Lost/Donate/Trade-in/Write-off Optional, Journal Grouping Group); bulan berjalan Oktober 2026. Asset Class (PC-6): IT Equipment (threshold sendiri 2.000.000; akun Gain dan Loss kosong), Vehicles dan Furniture (tanpa threshold sendiri). Tax Depreciation Class hanya memiliki versi pertama tanpa Effective From; kelas NB-1 (Bukan bangunan – Kelompok 1) dengan Useful Life 4. Jumlah periode pada dialog (16) bergantung bulan berjalan Oktober 2026 (kendali jam di `suite.md`; jam dipulihkan di hook `after`).
- Jam sistem: bulan berjalan Oktober 2026 menurut Time Zone entitas, dasar hitungan "The period calendar will have 16 accounting periods."; jam server dan browser diatur lewat kendali jam (butir "Kendali jam sistem" di `suite.md`) di hook `before` dan dipulihkan di hook `after` spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): Seed dan pemulihan lewat API (Preferences ke nilai awal PC-1, Asset Class, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- State yang diubah spec: Preferences company (Default Capitalization Threshold, Fiscal Year Start). Tidak ada perubahan Asset Class dan Tax Depreciation Class (form Edit NB-1 dibatalkan dan dikembalikan ke nilai tersimpan). Preferences dipulihkan ke nilai awal PC-1 lewat seed antar-TC dan di hook `after`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-409: Asset Class tidak memiliki akun Capitalization Offset per kelas

1. Buka Settings > Accounting > Asset Class
2. Ketik Search "IT Equipment", tekan Enter
3. Buka kelas IT Equipment
4. Pilih tab Accounts dan telusuri seluruh field akun pada kelas itu
5. Verifikasi field akun Gain on Disposal dan Loss on Disposal tampil pada kelas IT Equipment
6. Verifikasi tidak ada field akun Capitalization Offset pada kelas IT Equipment
7. Buka Settings > Accounting > Preferences (klik sidebar mereset Search)

### TC-FA-PREF-393: Asset Class membaca Default Capitalization Threshold baru tanpa salinan nilai

8. Ubah Default Capitalization Threshold menjadi "10000000"
9. Klik [Save changes]
10. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default threshold." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
11. Klik [Save] pada dialog Save Changes
12. Tunggu aksi selesai
13. Buka Settings > Accounting > Asset Class
14. Ketik Search "Vehicles", tekan Enter
15. Verifikasi kolom Capitalization Threshold pada baris kelas Vehicles tabel Asset Class tetap menampilkan "Default"
16. Buka Edit kelas Vehicles (halaman Detail Asset Class) dan pilih tab Depreciation
17. Verifikasi field Capitalization Threshold pada bagian Capitalization kelas Vehicles tetap kosong (tidak ada salinan 10.000.000 tersimpan pada kelas)
18. Kembali ke daftar Asset Class lewat Breadcrumb, lalu ganti isi kotak search dengan "IT Equipment", tekan Enter
19. Buka kelas IT Equipment dan pilih tab Depreciation
20. Verifikasi field Capitalization Threshold pada bagian Capitalization kelas IT Equipment tetap threshold sendiri 2.000.000
21. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan, lalu buka Settings > Accounting > Preferences

### TC-FA-PREF-396: Tax Depreciation Class membaca Fiscal Year Start baru sebagai awal tahun pajak

22. Pilih "July" pada Select Fiscal Year Start
23. Klik [Save changes]
24. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "The period calendar will have 16 accounting periods."; "Tax year start also follows Fiscal Year Start." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
25. Klik [Save] pada dialog Save Changes
26. Tunggu aksi selesai
27. Buka Settings > Accounting > Tax Depreciation Class
28. Ketik Search "NB-1", tekan Enter
29. Klik Edit pada kelas NB-1 (Bukan bangunan – Kelompok 1)
30. Ubah Useful Life menjadi "5" lalu klik [Save]
31. Verifikasi dialog "Save Changes" pada Edit kelas Tax Depreciation Class menampilkan Select Effective From dengan sedikitnya satu opsi
32. Verifikasi setiap opsi pada Select Effective From berlabel [MMM] [YYYY] berbulan "Jul" (bulan Fiscal Year Start baru)
33. Klik [Cancel] pada dialog Save Changes
34. Kembalikan Useful Life kelas NB-1 ke "4" (nilai tersimpan) agar form tidak dirty, lalu klik (←) pada kotak Search
35. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan

## Notes

- Kelas fungsional: Save atau perubahan state pelaku kedua, lalu pembacaan modul konsumen (Asset Class, Tax Depreciation Class, Chart of Accounts, Changelog). Tidak ada asersi absence log (kelas g).
- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 2, 7, 12, 14, 18, 21, 26, 28, 34, 35 (seed precondition TC, menunggu aksi selesai, Search untuk menemukan baris target (R-16, 8b butir 12), membersihkan Search, pemulihan state antar-TC).
- Urutan TC: TC-FA-PREF-409 (baca saja, tanpa Save) di depan, lalu TC-FA-PREF-393 dan 396 yang menyimpan Preferences (S-10); nomor TC di judul langkah tidak mengikuti urutan angka karena alasan itu.
- TC-FA-PREF-410 (Save Preferences tidak mengubah data Asset Class dan periode diposting) ada di spec 171 karena membutuhkan data posting penyusutan pertama (PC-2) yang berbeda dari data spec ini.
- TC-FA-PREF-396: dialog Save Changes pada Edit kelas Tax Depreciation Class dibuka hanya untuk mengamati Select Effective From dan dibatalkan; Useful Life dikembalikan ke nilai tersimpan dengan langkah eksplisit (S-09). Pemilihan opsi "setiap opsi" didahului `Verifikasi` sedikitnya satu opsi tampil (8b butir 2).
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Post Condition TC-FA-PREF-393, 396, dan 409 tidak punya langkah observasi sendiri; padanannya ada pada Expected (S-01). Post Condition "dibaca oleh ... saat dipakai" tidak diasersi terpisah.
  - Precondition TC-FA-PREF-409 menulis IT Equipment "terdaftar dengan akun Gain dan Loss (PC-6)", sedangkan PC-6 menulis akun Gain dan Loss IT Equipment kosong; spec mengasersi keberadaan field akun (Expected a), bukan nilainya.
  - Expected TC-FA-PREF-396 b menyebut "setiap opsi ... berbulan Jul" tanpa daftar opsi; spec mengasersi semua opsi yang tampil.

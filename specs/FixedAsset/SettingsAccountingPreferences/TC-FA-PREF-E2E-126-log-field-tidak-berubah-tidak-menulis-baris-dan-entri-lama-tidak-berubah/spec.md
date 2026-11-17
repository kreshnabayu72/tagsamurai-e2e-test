---
id: TC-FA-PREF-E2E-126-log-field-tidak-berubah-tidak-menulis-baris-dan-entri-lama-tidak-berubah
title: "Log: Field Tidak Berubah Tidak Menulis Baris dan Entri Changelog Lama Tidak Berubah"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-380
  - TC-FA-PREF-381
sourceRules: ["D-01", "FAPREF-LOGIC-10a", "F-FAPREF-01.k21a", "PV-01", "§4.2b#b1", "FAPREF-LOGIC-10k", "T-01", "L-02a", "L-02e", "§4.1.4#r3", "§8#b1", "§4.1.4#r4", "SET-02", "L-02j", "§4.1.4#r1", "SET-03", "L-02f", "§8#r3", "SET-01", "SET-12", "SET-04", "SET-11", "L-02b", "L-02c", "L-02d", "§8.3#p1", "§4.1.4#p1", "L-02k"]
smoke: []
dependsOn: []
trace:
  "D-01": [5, 27, 34]
  "FAPREF-LOGIC-10a": [5, 27, 34]
  "F-FAPREF-01.k21a": [5, 27, 34]
  "PV-01": [5, 27, 34]
  "§4.2b#b1": 6
  "FAPREF-LOGIC-10k": 6
  "T-01": 8
  "L-02a": [10, 11, 12, 13, 38, 39, 40, 41]
  "L-02e": [10, 13, 16, 18, 20, 22, 38]
  "§4.1.4#r3": [11, 12]
  "§8#b1": [11, 12]
  "§4.1.4#r4": [11, 12, 39]
  "SET-02": [11, 13, 17, 18, 21, 22, 39, 40, 41]
  "L-02j": [11, 40, 41]
  "§4.1.4#r1": 12
  "SET-03": [12, 13, 17, 18, 21, 22]
  "L-02f": 12
  "§8#r3": [13, 18, 22]
  "SET-01": 13
  "SET-12": 13
  "SET-04": 13
  "SET-11": 13
  "L-02b": [16, 17, 18]
  "L-02c": [20, 21, 22]
  "L-02d": 21
  "§8.3#p1": 21
  "§4.1.4#p1": [39, 40, 41]
  "L-02k": 41
coverage:
  web: automated
---

# Log: Field Tidak Berubah Tidak Menulis Baris dan Entri Changelog Lama Tidak Berubah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth, entitas Active) seri PC (PC-1): modul akuntansi aktif; Preferences bernilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents Sell/Scrap/Lost/Donate/Trade-in/Write-off Optional, Journal Grouping Group); bulan berjalan Oktober 2026. Seluruh setting tersimpan pada nilai awal; Asset Class Vehicles dan Furniture tidak mengisi threshold sendiri, IT Equipment mengisi threshold sendiri 2.000.000 (PC-6).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): Seed dan pemulihan lewat API (Preferences ke nilai awal PC-1, Asset Class, akun Chart of Accounts, pelepasan, kunci periode, status company) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`). Pembacaan jumlah baris Changelog Preferences, System Log milik pelaku, dan Activity Log FAMS sebelum aksi lewat kemampuan baca BE (disediakan tim FE/BE; 8b.10, S-12). Jam server dan jam browser sinkron untuk asersi "Date = waktu Save" dengan toleransi satu menit (S-12).
- State yang diubah spec: Preferences company dan entri log (audit trail permanen, tidak dihapus). Preferences dipulihkan ke nilai awal PC-1 lewat seed di antara TC dan di hook `after` (hook tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-380: Save threshold dan In-service Date Source tidak menulis log untuk field yang tidak berubah

1. Catat jumlah baris awal Changelog Preferences (N_cl), System Log milik Rina Anggraini (N_sl), dan Activity Log FAMS (N_al) lewat kemampuan baca BE
2. Ubah isi CurrencyInput Default Capitalization Threshold menjadi "10000000"
3. Pilih "Manual by Accounting" pada Select In-service Date Source
4. Klik [Save changes]
5. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default threshold." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
6. Verifikasi dialog Save Changes tidak memuat baris dampak untuk In-service Date Source
7. Klik [Save] pada dialog Save Changes
8. Verifikasi toast "Success, accounting preferences have been saved." tampil
9. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
10. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 2 dari N_cl
11. Verifikasi baris baru Changelog: Field = Default Capitalization Threshold (Old Value = 5.000.000, New Value = 10.000.000, Section = Capitalization)
12. Verifikasi baris baru Changelog: Field = In-service Date Source (Old Value = Activation date, New Value = Manual by Accounting, Section = Capitalization)
13. Verifikasi tidak ada baris baru Changelog untuk Fiscal Year Start, First Accounting Period, Depreciation in Disposal Month, akun, Disposal Documents, maupun Journal Grouping (dua baris baru hanyalah Default Capitalization Threshold dan In-service Date Source)
14. Tutup modal Changelog
15. Buka Global Settings > User > Detail > Tab System Log milik Rina Anggraini
16. Verifikasi jumlah baris System Log bertambah tepat 2 dari N_sl
17. Verifikasi baris baru System Log: Field = Default Capitalization Threshold dan Field = In-service Date Source
18. Verifikasi tidak ada baris baru System Log untuk field yang tidak berubah (dua baris baru hanyalah Default Capitalization Threshold dan In-service Date Source)
19. Buka Activity Log FAMS
20. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 2 dari N_al
21. Verifikasi baris baru Activity Log FAMS: Field = Default Capitalization Threshold dan Field = In-service Date Source
22. Verifikasi tidak ada baris baru Activity Log FAMS untuk field yang tidak berubah (dua baris baru hanyalah Default Capitalization Threshold dan In-service Date Source)
23. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan, lalu buka Settings > Accounting > Preferences

### TC-FA-PREF-381: Entri Changelog lama tidak berubah setelah field yang sama diubah lagi

24. Catat jumlah baris awal Changelog Preferences (N_cl) lewat kemampuan baca BE
25. Ubah Default Capitalization Threshold menjadi "10000000"
26. Klik [Save changes]
27. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default threshold." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
28. Klik [Save] pada dialog Save Changes
29. Tunggu aksi selesai
30. Klik ikon View history dan catat baris teratas modal Changelog: Preferences sebagai R1 (Date, Action, Section, Field, Old Value, New Value, Modified By), lalu tutup modal
31. Catat jumlah baris Changelog Preferences sesudah Save pertama sebagai N_cl1 lewat kemampuan baca BE
32. Ubah Default Capitalization Threshold menjadi "7500000"
33. Klik [Save changes]
34. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default threshold." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
35. Klik [Save] pada dialog Save Changes
36. Tunggu aksi selesai
37. Klik ikon View history dan amati modal Changelog: Preferences
38. Verifikasi jumlah baris modal Changelog: Preferences bertambah 2 dari N_cl, dan 1 dari N_cl1
39. Verifikasi kedua baris teratas modal Changelog: Preferences memiliki Field = Default Capitalization Threshold
40. Verifikasi baris terbaru (posisi teratas): Old Value = 10.000.000, New Value = 7.500.000
41. Verifikasi baris pertama (di bawah baris terbaru) tetap sama dengan R1: Old Value = 5.000.000, New Value = 10.000.000
42. Tutup modal Changelog
43. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan

## Notes

- Kelas fungsional: tiap TC menyimpan Preferences lewat UI lalu membaca tiga surface log. Asersi "tepat N baris baru" adalah asersi jumlah terhadap baseline (bukan absence kelas g); S-05 tidak berlaku.
- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 14, 23, 24, 29, 31, 36, 42, 43 (pencatatan baseline, pencatatan waktu Save, menutup modal Changelog, pemulihan Preferences antar-TC lewat seed). Baseline dicatat ulang sebelum pemicu tiap TC (S-12).
- Urutan baca log: jumlah baris dibuktikan bertambah dari baseline lebih dulu, baru baris teratas dibaca (S-14). Jumlah langkah nominal 43; blok baca-log berpola (buka surface, `Verifikasi` jumlah, `Verifikasi` kolom log) pada langkah 9 sampai 22, 37 sampai 41 tidak dihitung ke ambang ~35 langkah (bagian 3 prinsip 13, smell). Seluruh TC berkelas sama (fungsional Save lalu log tiga surface) dan tiap blok berdiri sendiri dengan pemulihan seed di antaranya.
- TC-FA-PREF-380 c, d dan TC-FA-PREF-381 b mengasersi jumlah baris (selisih dari baseline) dan identitas baris, bukan absence kelas g: "tidak ada baris baru untuk field yang tidak berubah" diasersi sebagai `Verifikasi` setelah `Verifikasi` jumlah tepat 2 baris dan kedua baris yang ada (anchor positif, 8b butir 2).
- Langkah 30 sampai 31: R1 mencatat baris teratas sesudah Save pertama (langkah TC 4) sebagai pembanding asersi Expected d; N_cl1 mencatat jumlah baris sesudah Save pertama agar selisih Save kedua terhadap Save pertama dapat diasersi.
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Expected TC menyebut baris log baru sebagai "tepat N baris baru" tanpa menyebut baseline; spec mencatat baseline jumlah baris tiap surface sebelum aksi lewat kemampuan baca BE dan mengasersi selisih (S-12, S-14).
  - Post Condition TC 380 dan 381 tidak punya langkah observasi sendiri di TC; padanannya ada pada Expected yang diasersi (S-01). Post Condition "Nilai terbaru dibaca oleh ... (belum disusun)" tidak diasersi karena modul konsumen belum disusun.
  - Expected b TC-FA-PREF-381 menulis "memuat 2 baris Field = Default Capitalization Threshold" sebagai jumlah absolut; Changelog adalah audit trail permanen sehingga spec mengasersi selisih terhadap baseline dan dua baris teratas. Mohon TC ditulis ulang relatif (S-12).

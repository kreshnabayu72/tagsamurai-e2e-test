---
id: TC-FA-PREF-E2E-137-deferred-rekonsiliasi-j-01-membuat-preferences-periode-paling-awal-dan-field-terkunci
title: "[DEFERRED] Rekonsiliasi J-01: Membuat Preferences, Periode Paling Awal sebagai First Accounting Period, dan Field Terkunci"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-421
  - TC-FA-PREF-422
  - TC-FA-PREF-423
  - TC-FA-PREF-424
sourceRules: ["SET-01", "SET-12", "SET-02", "SET-03", "SET-04", "SET-05", "SET-06", "SET-08", "SET-09", "DOC-01", "DOC-02", "DOC-03", "DOC-04", "DOC-05", "DOC-06", "SET-11", "§[F-FAPREF-03] Initialize Default Preferences#b1", "FAPREF-LOGIC-01g", "FAPREF-LOGIC-03e", "E-FAPREF-16", "R-04", "FAPREF-LOGIC-01h", "§[F-FAPREF-03] Initialize Default Preferences#r4", "FAPREF-LOGIC-02c", "E-FAPREF-41", "ST-05", "FAPREF-LOGIC-02e"]
smoke: []
dependsOn: []
trace:
  "SET-01": 5
  "SET-12": 5
  "SET-02": [5, 11]
  "SET-03": 5
  "SET-04": 5
  "SET-05": 5
  "SET-06": 5
  "SET-08": 5
  "SET-09": 5
  "DOC-01": 5
  "DOC-02": 5
  "DOC-03": 5
  "DOC-04": 5
  "DOC-05": 5
  "DOC-06": 5
  "SET-11": 5
  "§[F-FAPREF-03] Initialize Default Preferences#b1": 5
  "FAPREF-LOGIC-01g": 5
  "FAPREF-LOGIC-03e": 11
  "E-FAPREF-16": 11
  "R-04": 13
  "FAPREF-LOGIC-01h": [19, 23, 28]
  "§[F-FAPREF-03] Initialize Default Preferences#r4": [19, 28]
  "FAPREF-LOGIC-02c": [20, 21, 29]
  "E-FAPREF-41": 23
  "ST-05": [29, 30, 32, 34]
  "FAPREF-LOGIC-02e": 30
coverage:
  web: automated
---

# [DEFERRED] Rekonsiliasi J-01: Membuat Preferences, Periode Paling Awal sebagai First Accounting Period, dan Field Terkunci

## Prerequisites

- Mode: FE+BE.
- Kelas fungsional; TC `[DEFERRED]`. Modul pemilik transaksi aktivasi modul akuntansi, job rekonsiliasi J-01, modul Asset (status dan in-service date), serta modul Accounting Period adalah modul pemilik/konsumen yang belum disusun: TC `[DEFERRED]` (NC-08, NC-09) ditulis dengan langkah generik pada modul itu dan hanya mengasersi klaim yang tertulis di TC dan PRD; seluruh kebutuhan modul disediakan tim FE setelah modul tersedia.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: modul akuntansi `PT Contoh Konstruksi` aktif tanpa baris Preferences (PC-13, PC-16) untuk TC-FA-PREF-421, 423, dan 424; baris Preferences ada dengan Default Capitalization Threshold 10.000.000 (PC-1) untuk TC-FA-PREF-422; periode Jan 2026 sampai Dec 2026 seluruhnya Open tanpa posting penyusutan untuk TC-FA-PREF-423; periode dari Jan 2026 dengan posting penyusutan pertama (PC-2) untuk TC-FA-PREF-424; Time Zone entitas Asia/Jakarta (PC-15).
- Tabel "Nilai awal Preferences" (Expected TC; PC-1):

  | Setting | Nilai awal |
  |---|---|
  | Fiscal Year Start | January |
  | First Accounting Period | Mar 2026 |
  | Default Capitalization Threshold | 5.000.000 (tampil Rp 5.000.000,00) |
  | In-service Date Source | Activation date |
  | Depreciation in Disposal Month | Up to previous month |
  | Default Gain on Disposal | kosong |
  | Default Loss on Disposal | kosong |
  | Default Capitalization Offset | kosong |
  | Found Asset Credit Account | kosong |
  | Disposal Documents — Sell | Optional |
  | Disposal Documents — Scrap | Optional |
  | Disposal Documents — Lost | Optional |
  | Disposal Documents — Donate | Optional |
  | Disposal Documents — Trade-in | Optional |
  | Disposal Documents — Write-off | Optional |
  | Journal Grouping | Group |
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): pemicu job rekonsiliasi J-01 (lewat penjadwal platform atau pemicu manual tim BE; disediakan tim BE); pembentukan periode akuntansi dan posting penyusutan pertama lewat fixture BE (PC-2); seed dan pemulihan kondisi company (PC-13, PC-16, status plan dan entitas) lewat API (butir "Seed dan pemulihan lewat API" di `suite.md`); kendali jam sistem (clock; butir "Kendali jam sistem" di `suite.md`); pembacaan jumlah baris Changelog Preferences, System Log, dan Activity Log lewat kemampuan baca BE sebelum aksi (8b.10, S-12). Jam sistem (clock): jam server dan jam browser diatur bersama ke 10 Maret 2026 dan Time Zone entitas Asia/Jakarta (PC-15) pada langkah 1, dipulihkan di hook `after`.
- State yang diubah spec: Preferences, periode akuntansi, kunci posting penyusutan pertama, entri log (permanen), dan jam sistem. Seluruhnya dipulihkan lewat seed antar-TC dan di hook `after`; jam sistem dipulihkan di hook `after`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-421: Rekonsiliasi J-01 membuat Preferences bernilai awal bagi company aktif tanpa baris Preferences

1. Atur jam server dan jam browser ke 10 Maret 2026 dan Time Zone entitas Asia/Jakarta
2. Bentuk kondisi PC-13 dan PC-16 lewat seed: modul akuntansi PT Contoh Konstruksi sudah aktif tetapi belum memiliki baris Preferences (precondition TC, tidak diasersi); company belum memiliki periode akuntansi
3. Jalankan job rekonsiliasi J-01 (lewat penjadwal platform atau pemicu manual tim BE) hingga putaran job selesai
4. Buka Settings > Accounting > Preferences dan amati nilai semua setting
5. Verifikasi untuk setiap baris tabel "Nilai awal Preferences" di Prerequisites (16 baris), nilai pada setting baris itu sama dengan kolom Nilai awal
6. Kembalikan company ke kondisi awal PC-1 lewat seed

### TC-FA-PREF-422: Rekonsiliasi J-01 tidak membuat ulang Preferences yang sudah ada

7. Bentuk kondisi PC-1 lewat seed: modul akuntansi aktif dan baris Preferences ada dengan Default Capitalization Threshold 10.000.000 (precondition TC, tidak diasersi)
8. Catat jumlah baris Action = Create di Changelog Preferences (N_create) lewat kemampuan baca BE
9. Jalankan job rekonsiliasi J-01 (lewat penjadwal platform atau pemicu manual tim BE) hingga putaran job selesai
10. Buka Settings > Accounting > Preferences dan amati Default Capitalization Threshold
11. Verifikasi Default Capitalization Threshold tetap 10.000.000 (tampil Rp 10.000.000,00)
12. Klik ikon View history dan hitung baris Action = Create
13. Verifikasi jumlah baris Action = Create di Changelog: Preferences tidak bertambah (sama dengan N_create)
14. Tutup modal Changelog
15. Pulihkan Preferences ke nilai awal PC-1 lewat seed hingga tersimpan

### TC-FA-PREF-423: J-01 untuk company yang sudah memiliki periode memakai periode paling awal sebagai First Accounting Period

16. Bentuk kondisi PC-13 dan PC-16 lewat seed: modul akuntansi PT Contoh Konstruksi sudah aktif tetapi belum memiliki baris Preferences (precondition TC, tidak diasersi); company sudah memiliki periode akuntansi Jan 2026 sampai Dec 2026, seluruhnya Open, belum ada posting penyusutan
17. Jalankan job rekonsiliasi J-01 (lewat penjadwal platform atau pemicu manual tim BE) hingga putaran job selesai
18. Buka Settings > Accounting > Preferences dan amati Select bulan dan tahun First Accounting Period serta Fiscal Year Start
19. Verifikasi First Accounting Period menampilkan bulan Jan dan tahun 2026
20. Verifikasi Fiscal Year Start Enabled (tidak terkunci)
21. Verifikasi First Accounting Period Enabled (tidak terkunci)
22. Buka daftar periode di modul Accounting Period (`settings-accounting-period/`), atur ukuran halaman ke 25, dan amati periode yang tampil
23. Verifikasi Accounting Period tetap memuat periode Jan 2026 sampai Dec 2026 tanpa dibuat ulang
24. Kembalikan company ke kondisi awal PC-1 lewat seed

### TC-FA-PREF-424: J-01 untuk company yang sudah memiliki periode dan penyusutan terposting menghasilkan field terkunci

25. Bentuk kondisi PC-13 dan PC-16 lewat seed: modul akuntansi PT Contoh Konstruksi sudah aktif tetapi belum memiliki baris Preferences (precondition TC, tidak diasersi); company sudah memiliki periode akuntansi dari Jan 2026 dan posting penyusutan pertama sudah ada (PC-2)
26. Jalankan job rekonsiliasi J-01 (lewat penjadwal platform atau pemicu manual tim BE) hingga putaran job selesai
27. Buka Settings > Accounting > Preferences dan amati Fiscal Year Start dan First Accounting Period beserta tooltip kunci
28. Verifikasi First Accounting Period menampilkan bulan Jan dan tahun 2026
29. Verifikasi Fiscal Year Start tampil Disabled dengan ikon gembok
30. Verifikasi First Accounting Period tampil Disabled dengan ikon gembok
31. Arahkan kursor ke ikon gembok Fiscal Year Start
32. Verifikasi tooltip Fiscal Year Start "Fiscal year start is locked because depreciation has been posted or a period has been closed. It cannot be changed from this page."
33. Arahkan kursor ke ikon gembok First Accounting Period
34. Verifikasi tooltip First Accounting Period "First accounting period is locked because depreciation has been posted or a period has been closed. It cannot be changed from this page."
35. Kembalikan company ke kondisi awal PC-1 lewat seed dan hapus kunci posting penyusutan pertama lewat fixture BE

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 2, 6, 7, 8, 14, 15, 16, 24, 25, 35 (seed precondition TC, pengaturan jam atau fault injection bila dipakai spec, pencatatan baseline, menutup modal, pemulihan kondisi).
- Langkah 5 diulang per baris tabel "Nilai awal Preferences" di Prerequisites (8b butir 7); parameter tiap iterasi ada di tabel itu dan `Verifikasi` tetap satu per klausa (S-01).
- Job latar J-01 hanya memicu kondisi yang diuji (bagian 3 prinsip 13, P-2); TC memintanya "lewat penjadwal platform atau pemicu manual tim BE".
- TC-FA-PREF-423: "tanpa dibuat ulang" tidak teramati terpisah di UI; diasersi sebagai satu `Verifikasi` periode Jan 2026 sampai Dec 2026 tetap tampil.
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Kolom Automatable TC menandai pemicu job J-01, kegagalan sisi server, atau aktivasi sebagai "Manual Only" atau memakai langkah generik pada modul yang belum disusun; spec tetap ditulis penuh sesuai bagian 2 dan menyatakan kebutuhannya di Prerequisites.
  - Expected TC menulis "Default Capitalization Threshold = 5.000.000", sedangkan Catatan TC menyatakan tampilan input memakai simbol mata uang dan dua desimal (Rp 5.000.000,00); spec mengasersi nilai 5.000.000 dan menyebut tampilannya di tabel.
  - Expected TC-FA-PREF-422 b menulis jumlah baris Action = Create tanpa angka baseline; spec mencatat jumlah awal lewat kemampuan baca BE dan mengasersi tidak bertambah (S-12).
  - Expected TC-FA-PREF-423 b memakai istilah "Enabled (tidak terkunci)" untuk dua field; spec mengasersi tiap field dalam `Verifikasi` terpisah.
  - Post Condition TC-FA-PREF-421 sampai 424 tidak punya langkah observasi sendiri; padanannya ada pada Expected (S-01).

---
id: TC-FA-PREF-E2E-138-deferred-j-01-changelog-dan-activity-log-dengan-modified-by-system-dan-retry-putaran-berikutnya
title: "[DEFERRED] J-01: Changelog dan Activity Log dengan Modified By System serta Retry pada Putaran Berikutnya"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-425
  - TC-FA-PREF-426
  - TC-FA-PREF-428
sourceRules: ["L-01a", "J-01", "§8#b3", "§4.1.4#p3", "§[F-FAPREF-03] Initialize Default Preferences#b3", "L-01b", "L-02d", "§8.3#p1", "F-FAPREF-03.k3", "R-04", "SET-01", "SET-12", "SET-02", "SET-03", "SET-04", "SET-05", "SET-06", "SET-08", "SET-09", "DOC-01", "DOC-02", "DOC-03", "DOC-04", "DOC-05", "DOC-06", "SET-11"]
smoke: []
dependsOn: []
trace:
  "L-01a": 6
  "J-01": [6, 13]
  "§8#b3": [7, 14]
  "§4.1.4#p3": 7
  "§[F-FAPREF-03] Initialize Default Preferences#b3": [7, 14]
  "L-01b": [13, 14]
  "L-02d": 14
  "§8.3#p1": 14
  "F-FAPREF-03.k3": [18, 20, 21, 25]
  "R-04": [20, 21]
  "SET-01": 25
  "SET-12": 25
  "SET-02": 25
  "SET-03": 25
  "SET-04": 25
  "SET-05": 25
  "SET-06": 25
  "SET-08": 25
  "SET-09": 25
  "DOC-01": 25
  "DOC-02": 25
  "DOC-03": 25
  "DOC-04": 25
  "DOC-05": 25
  "DOC-06": 25
  "SET-11": 25
coverage:
  web: automated
---

# [DEFERRED] J-01: Changelog dan Activity Log dengan Modified By System serta Retry pada Putaran Berikutnya

## Prerequisites

- Mode: FE+BE.
- Kelas fungsional; TC `[DEFERRED]`. Modul pemilik transaksi aktivasi modul akuntansi, job rekonsiliasi J-01, modul Asset (status dan in-service date), serta modul Accounting Period adalah modul pemilik/konsumen yang belum disusun: TC `[DEFERRED]` (NC-08, NC-09) ditulis dengan langkah generik pada modul itu dan hanya mengasersi klaim yang tertulis di TC dan PRD; seluruh kebutuhan modul disediakan tim FE setelah modul tersedia.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: modul akuntansi `PT Contoh Konstruksi` aktif tanpa baris Preferences (PC-13, PC-16); Time Zone entitas Asia/Jakarta (PC-15). Modified By job tanpa user aktor tampil "System" (Expected TC).
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
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): pemicu job rekonsiliasi J-01 (lewat penjadwal platform atau pemicu manual tim BE; disediakan tim BE); fault injection putaran pertama job lewat fixture BE; pembacaan status job dan keberadaan Preferences atau log Create lewat kemampuan baca BE (kemampuan baca status job perlu dikonfirmasi tim FE/BE); seed dan pemulihan kondisi company (PC-13, PC-16, status plan dan entitas) lewat API (butir "Seed dan pemulihan lewat API" di `suite.md`); pembacaan jumlah baris Changelog Preferences, System Log, dan Activity Log lewat kemampuan baca BE sebelum aksi (8b.10, S-12). 
- State yang diubah spec: Preferences dan entri log (permanen), serta fault injection job. Preferences dipulihkan lewat seed antar-TC dan di hook `after`; fault injection dilepas di langkah 22 dan di hook `after`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-425: J-01 menulis entri Create di Changelog dengan Modified By System

1. Bentuk kondisi PC-13 dan PC-16 lewat seed: modul akuntansi PT Contoh Konstruksi sudah aktif tetapi belum memiliki baris Preferences (precondition TC, tidak diasersi)
2. Catat jumlah baris awal Changelog Preferences (N_cl) lewat kemampuan baca BE (company belum memiliki Preferences)
3. Jalankan job rekonsiliasi J-01 (lewat penjadwal platform atau pemicu manual tim BE) hingga putaran job selesai
4. Buka Settings > Accounting > Preferences
5. Klik ikon View history dan amati modal Changelog: Preferences
6. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
7. Verifikasi baris baru modal Changelog: Preferences: Action = Create, Section = —, Field = Preferences, Old Value = —, New Value = Initial values, Modified By = System
8. Tutup modal Changelog

### TC-FA-PREF-426: J-01 menulis entri Create di Activity Log FAMS dengan Modified By System

9. Bentuk kondisi PC-13 dan PC-16 lewat seed: modul akuntansi PT Contoh Konstruksi sudah aktif tetapi belum memiliki baris Preferences (precondition TC, tidak diasersi)
10. Catat jumlah baris awal Activity Log FAMS (N_al) lewat kemampuan baca BE
11. Jalankan job rekonsiliasi J-01 (lewat penjadwal platform atau pemicu manual tim BE) hingga putaran job selesai
12. Buka Activity Log FAMS dan amati baris teratas
13. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 1 dari N_al
14. Verifikasi baris baru Activity Log FAMS: Action = Create, Object = Preferences, Name = —, Field = Preferences, Old Value = —, New Value = Initial values, Modified By = System

### TC-FA-PREF-428: J-01 yang gagal dicoba ulang pada putaran berikutnya sampai berhasil

15. Bentuk kondisi PC-13 dan PC-16 lewat seed: modul akuntansi PT Contoh Konstruksi sudah aktif tetapi belum memiliki baris Preferences (precondition TC, tidak diasersi); catat jumlah entri log Create Preferences company sebagai baseline (dibaca lewat kemampuan baca BE)
16. Atur kegagalan pembuatan Preferences pada putaran pertama job lewat fixture BE untuk sesi ini
17. Jalankan job rekonsiliasi J-01 (lewat penjadwal platform atau pemicu manual tim BE) hingga putaran pertama selesai (putaran pertama, gagal)
18. Verifikasi putaran pertama job J-01 berstatus gagal (dibaca lewat kemampuan baca BE)
19. Buka Settings > Accounting > Preferences dan amati ketersediaan tab
20. Verifikasi tidak ada baris Preferences tersimpan setelah putaran pertama (dibaca lewat kemampuan baca BE)
21. Verifikasi jumlah entri log Create sama dengan baseline langkah 15 setelah putaran pertama, tidak ada entri log Create baru (dibaca lewat kemampuan baca BE)
22. Lepaskan kegagalan buatan lewat fixture BE
23. Jalankan putaran job J-01 berikutnya hingga putaran selesai
24. Buka Settings > Accounting > Preferences dan amati nilai semua setting
25. Verifikasi untuk setiap baris tabel "Nilai awal Preferences" di Prerequisites (16 baris), nilai pada setting baris itu sama dengan kolom Nilai awal
26. Kembalikan company ke kondisi awal PC-1 lewat seed

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 2, 8, 9, 10, 15, 16, 22, 26 (seed precondition TC, pengaturan jam atau fault injection bila dipakai spec, pencatatan baseline, menutup modal, pemulihan kondisi).
- Langkah 25 diulang per baris tabel "Nilai awal Preferences" di Prerequisites (8b butir 7); parameter tiap iterasi ada di tabel itu dan `Verifikasi` tetap satu per klausa (S-01).
- P-2: job latar J-01 dan fault injection putaran pertama (TC-FA-PREF-428) hanya memicu kondisi yang diuji; asersi TC-FA-PREF-428 b pada Preferences terbentuk setelah putaran berikutnya.
- TC-FA-PREF-428: `Verifikasi` status gagal putaran pertama ditambahkan sebagai anchor positif bagi asersi absence "tidak ada Preferences dan tidak ada log Create" (8b butir 2, S-03); kemampuan baca status job tidak disebut TC.
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Kolom Automatable TC menandai pemicu job J-01, kegagalan sisi server, atau aktivasi sebagai "Manual Only" atau memakai langkah generik pada modul yang belum disusun; spec tetap ditulis penuh sesuai bagian 2 dan menyatakan kebutuhannya di Prerequisites.
  - Expected TC menulis "Default Capitalization Threshold = 5.000.000", sedangkan Catatan TC menyatakan tampilan input memakai simbol mata uang dan dua desimal (Rp 5.000.000,00); spec mengasersi nilai 5.000.000 dan menyebut tampilannya di tabel.
  - Expected TC menyebut jumlah baris log sebagai angka absolut ("tepat 1 baris", "1 baris"); log adalah audit trail permanen sehingga spec memakai baseline jumlah baris sebelum aksi dan mengasersi selisih (S-12). Mohon TC ditulis relatif.
  - Post Condition TC-FA-PREF-425, 426, dan 428 tidak punya langkah observasi sendiri; padanannya ada pada Expected (S-01).
  - Expected TC-FA-PREF-428 a memuat dua klausa absence (tidak ada Preferences, tidak ada log Create) tanpa cara cek di UI; spec membacanya lewat kemampuan baca BE (S-11).

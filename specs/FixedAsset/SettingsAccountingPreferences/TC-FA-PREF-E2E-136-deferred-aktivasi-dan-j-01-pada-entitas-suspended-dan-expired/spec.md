---
id: TC-FA-PREF-E2E-136-deferred-aktivasi-dan-j-01-pada-entitas-suspended-dan-expired
title: "[DEFERRED] Aktivasi dan Job J-01 pada Entitas Suspended dan Expired"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-419
  - TC-FA-PREF-420
  - TC-FA-PREF-429
  - TC-FA-PREF-430
sourceRules: ["SET-01", "SET-12", "SET-02", "SET-03", "SET-04", "SET-05", "SET-06", "SET-08", "SET-09", "DOC-01", "DOC-02", "DOC-03", "DOC-04", "DOC-05", "DOC-06", "SET-11", "N-15", "L-01a", "J-05", "§8#r4", "§8.4#p2"]
smoke: []
dependsOn: []
trace:
  "SET-01": [6, 16, 25, 30]
  "SET-12": [6, 16, 25, 30]
  "SET-02": [6, 16, 25, 30]
  "SET-03": [6, 16, 25, 30]
  "SET-04": [6, 16, 25, 30]
  "SET-05": [6, 16, 25, 30]
  "SET-06": [6, 16, 25, 30]
  "SET-08": [6, 16, 25, 30]
  "SET-09": [6, 16, 25, 30]
  "DOC-01": [6, 16, 25, 30]
  "DOC-02": [6, 16, 25, 30]
  "DOC-03": [6, 16, 25, 30]
  "DOC-04": [6, 16, 25, 30]
  "DOC-05": [6, 16, 25, 30]
  "DOC-06": [6, 16, 25, 30]
  "SET-11": [6, 16, 25, 30]
  "N-15": [6, 8, 9, 16, 18, 19]
  "L-01a": [8, 18]
  "J-05": [8, 18]
  "§8#r4": [9, 19]
  "§8.4#p2": [25, 30]
coverage:
  web: automated
---

# [DEFERRED] Aktivasi dan Job J-01 pada Entitas Suspended dan Expired

## Prerequisites

- Mode: FE+BE.
- Kelas fungsional; TC `[DEFERRED]`. Modul pemilik transaksi aktivasi modul akuntansi, job rekonsiliasi J-01, modul Asset (status dan in-service date), serta modul Accounting Period adalah modul pemilik/konsumen yang belum disusun: TC `[DEFERRED]` (NC-08, NC-09) ditulis dengan langkah generik pada modul itu dan hanya mengasersi klaim yang tertulis di TC dan PRD; seluruh kebutuhan modul disediakan tim FE setelah modul tersedia.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` tanpa aktivasi modul akuntansi (PC-16) berstatus Suspended (PC-9) untuk TC-FA-PREF-419 dan Expired (PC-10) untuk TC-FA-PREF-420; modul akuntansi aktif tanpa baris Preferences (PC-13, PC-16) berstatus Suspended (PC-9) untuk TC-FA-PREF-429 dan Expired (PC-10) untuk TC-FA-PREF-430; Time Zone entitas Asia/Jakarta (PC-15). Login di hook `before` dilakukan saat company Active; status Suspended atau Expired dibentuk lewat fixture BE pada langkah dan dikembalikan ke Active di akhir tiap TC.
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
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): perubahan status company (Suspended, Expired) lewat fixture BE; pemicu aktivasi dan job J-01 pada modul pemilik (disediakan tim FE/BE setelah modul tersedia); seed dan pemulihan kondisi company (PC-13, PC-16, status plan dan entitas) lewat API (butir "Seed dan pemulihan lewat API" di `suite.md`); kendali jam sistem (clock; butir "Kendali jam sistem" di `suite.md`); pembacaan jumlah baris Changelog Preferences, System Log, dan Activity Log lewat kemampuan baca BE sebelum aksi (8b.10, S-12). Jam sistem (clock): jam server dan jam browser diatur bersama ke 10 Maret 2026 dan Time Zone entitas Asia/Jakarta (PC-15) pada langkah 1, dipulihkan di hook `after`.
- State yang diubah spec: status company (global tenant), Preferences, aktivasi modul akuntansi, entri log (permanen), dan jam sistem. Status company dikembalikan ke Active di akhir tiap TC dan di hook `after`; jam sistem dipulihkan di hook `after`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-419: Pembuatan Preferences pada transaksi aktivasi tidak diblokir entitas Suspended

1. Atur jam server dan jam browser ke 10 Maret 2026 dan Time Zone entitas Asia/Jakarta
2. Bentuk kondisi PC-16 lewat seed: company PT Contoh Konstruksi belum pernah mengaktifkan modul akuntansi dan berstatus Suspended lewat fixture BE (PC-9; precondition TC, tidak diasersi)
3. Catat jumlah baris awal Changelog Preferences (N_cl) lewat kemampuan baca BE (company belum memiliki Preferences)
4. Aktifkan modul akuntansi untuk PT Contoh Konstruksi pada modul pemilik transaksi aktivasi modul akuntansi (belum disusun; disediakan tim FE setelah modul tersedia) hingga aktivasi selesai
5. Buka Settings > Accounting > Preferences
6. Verifikasi untuk setiap baris tabel "Nilai awal Preferences" di Prerequisites (16 baris), nilai pada setting baris itu sama dengan kolom Nilai awal
7. Klik ikon View history dan amati modal Changelog: Preferences
8. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
9. Verifikasi baris baru modal Changelog: Preferences memiliki Action = Create
10. Tutup modal Changelog
11. Kembalikan status company ke Active lewat fixture BE hingga tersimpan

### TC-FA-PREF-420: Pembuatan Preferences pada transaksi aktivasi tidak diblokir entitas Expired

12. Bentuk kondisi PC-16 lewat seed: company PT Contoh Konstruksi belum pernah mengaktifkan modul akuntansi dan berstatus Expired lewat fixture BE (PC-10; precondition TC, tidak diasersi)
13. Catat jumlah baris awal Changelog Preferences (N_cl) lewat kemampuan baca BE (company belum memiliki Preferences)
14. Aktifkan modul akuntansi untuk PT Contoh Konstruksi pada modul pemilik transaksi aktivasi modul akuntansi (belum disusun; disediakan tim FE setelah modul tersedia) hingga aktivasi selesai
15. Buka Settings > Accounting > Preferences
16. Verifikasi untuk setiap baris tabel "Nilai awal Preferences" di Prerequisites (16 baris), nilai pada setting baris itu sama dengan kolom Nilai awal
17. Klik ikon View history dan amati modal Changelog: Preferences
18. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
19. Verifikasi baris baru modal Changelog: Preferences memiliki Action = Create
20. Tutup modal Changelog
21. Kembalikan status company ke Active lewat fixture BE hingga tersimpan

### TC-FA-PREF-429: J-01 tetap membuat Preferences pada entitas Suspended

22. Bentuk kondisi PC-13 dan PC-16 lewat seed: modul akuntansi PT Contoh Konstruksi sudah aktif, belum memiliki baris Preferences, dan berstatus Suspended lewat fixture BE (PC-9; precondition TC, tidak diasersi)
23. Jalankan job rekonsiliasi J-01 (lewat penjadwal platform atau pemicu manual tim BE) hingga putaran job selesai
24. Buka Settings > Accounting > Preferences dan amati nilai semua setting
25. Verifikasi untuk setiap baris tabel "Nilai awal Preferences" di Prerequisites (16 baris), nilai pada setting baris itu sama dengan kolom Nilai awal
26. Kembalikan status company ke Active lewat fixture BE hingga tersimpan

### TC-FA-PREF-430: J-01 tetap membuat Preferences pada entitas Expired

27. Bentuk kondisi PC-13 dan PC-16 lewat seed: modul akuntansi PT Contoh Konstruksi sudah aktif, belum memiliki baris Preferences, dan berstatus Expired lewat fixture BE (PC-10; precondition TC, tidak diasersi)
28. Jalankan job rekonsiliasi J-01 (lewat penjadwal platform atau pemicu manual tim BE) hingga putaran job selesai
29. Buka Settings > Accounting > Preferences dan amati nilai semua setting
30. Verifikasi untuk setiap baris tabel "Nilai awal Preferences" di Prerequisites (16 baris), nilai pada setting baris itu sama dengan kolom Nilai awal
31. Kembalikan status company ke Active lewat fixture BE hingga tersimpan

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 2, 3, 10, 11, 12, 13, 20, 21, 22, 26, 27, 31 (seed precondition TC, pengaturan jam atau fault injection bila dipakai spec, pencatatan baseline, menutup modal, pemulihan kondisi).
- Langkah 6, 16, 25, dan 30 diulang per baris tabel "Nilai awal Preferences" di Prerequisites (8b butir 7); parameter tiap iterasi ada di tabel itu dan `Verifikasi` tetap satu per klausa (S-01).
- Kelas h (state tenant, bagian 3 prinsip 13h): semua TC mengasersi bahwa pembuatan Preferences tidak diblokir status entitas; job latar J-01 hanya pemicu kondisi (bagian 3 prinsip 13, P-2).
- TC-FA-PREF-420 dan 430 merujuk PC-9 pada Precondition untuk entitas Expired; spec memakai PC-10 (Expired) sesuai tabel Pre-setup.
- Pada TC-FA-PREF-419 dan 420, "Preferences terbentuk dengan nilai awal" diasersi memakai tabel nilai awal yang sama dengan TC-FA-PREF-429 dan 430.
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Kolom Automatable TC menandai pemicu job J-01, kegagalan sisi server, atau aktivasi sebagai "Manual Only" atau memakai langkah generik pada modul yang belum disusun; spec tetap ditulis penuh sesuai bagian 2 dan menyatakan kebutuhannya di Prerequisites.
  - Expected TC menulis "Default Capitalization Threshold = 5.000.000", sedangkan Catatan TC menyatakan tampilan input memakai simbol mata uang dan dua desimal (Rp 5.000.000,00); spec mengasersi nilai 5.000.000 dan menyebut tampilannya di tabel.
  - Expected TC menyebut jumlah baris log sebagai angka absolut ("tepat 1 baris", "1 baris"); log adalah audit trail permanen sehingga spec memakai baseline jumlah baris sebelum aksi dan mengasersi selisih (S-12). Mohon TC ditulis relatif.
  - Precondition TC-FA-PREF-420 dan 430 menulis (PC-9) untuk entitas Expired, padahal PC-9 adalah varian Suspended dan PC-10 adalah varian Expired.
  - TC-FA-PREF-419 dan 420 tidak menyatakan apakah Total Control dapat membuka Settings > Accounting > Preferences pada entitas Suspended atau Expired; spec mengikuti TC.
  - Post Condition TC-FA-PREF-419, 420, 429, dan 430 tidak punya langkah observasi sendiri; padanannya ada pada Expected (S-01).

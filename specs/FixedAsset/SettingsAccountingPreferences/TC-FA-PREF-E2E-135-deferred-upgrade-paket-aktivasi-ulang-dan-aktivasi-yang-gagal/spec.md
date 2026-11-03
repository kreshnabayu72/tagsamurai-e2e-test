---
id: TC-FA-PREF-E2E-135-deferred-upgrade-paket-aktivasi-ulang-dan-aktivasi-yang-gagal
title: "[DEFERRED] Upgrade Paket, Aktivasi Ulang, dan Aktivasi yang Gagal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-416
  - TC-FA-PREF-417
  - TC-FA-PREF-418
coverage:
  web: automated
---

# [DEFERRED] Upgrade Paket, Aktivasi Ulang, dan Aktivasi yang Gagal

## Prerequisites

- Mode: FE+BE.
- Kelas fungsional; TC `[DEFERRED]`. Modul pemilik transaksi aktivasi modul akuntansi, job rekonsiliasi J-01, modul Asset (status dan in-service date), serta modul Accounting Period adalah modul pemilik/konsumen yang belum disusun: TC `[DEFERRED]` (NC-08, NC-09) ditulis dengan langkah generik pada modul itu dan hanya mengasersi klaim yang tertulis di TC dan PRD; seluruh kebutuhan modul disediakan tim FE setelah modul tersedia.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` pada plan Starter (PC-11) tanpa aktivasi modul akuntansi (PC-16) untuk TC-FA-PREF-416; modul pernah aktif lalu dinonaktifkan dengan Default Capitalization Threshold tersimpan 10.000.000 dan Changelog 1 baris Create untuk TC-FA-PREF-417; company tanpa aktivasi (PC-16) untuk TC-FA-PREF-418; Time Zone entitas Asia/Jakarta (PC-15). Pengecualian layar awal: pada awal spec company dapat berplan Starter atau belum aktif sehingga Preferences tidak terjangkau; hook `beforeEach` suite hanya menutup dialog dan langkah membuka Preferences ditulis eksplisit pada langkah.
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
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): upgrade plan company ke Growth dan pemicu aktivasi pada modul pemilik (disediakan tim FE setelah modul tersedia); fault injection pembuatan Preferences lewat fixture BE (disediakan tim BE); pembacaan keberadaan Preferences, periode awal, dan log Create lewat kemampuan baca BE. seed dan pemulihan kondisi company (PC-13, PC-16, status plan dan entitas) lewat API (butir "Seed dan pemulihan lewat API" di `suite.md`); kendali jam sistem (clock; butir "Kendali jam sistem" di `suite.md`); pembacaan jumlah baris Changelog Preferences, System Log, dan Activity Log lewat kemampuan baca BE sebelum aksi (8b.10, S-12). Jam sistem (clock): jam server dan jam browser diatur bersama ke 10 Maret 2026 dan Time Zone entitas Asia/Jakarta (PC-15) pada langkah 1, dipulihkan di hook `after`.
- State yang diubah spec: plan company, aktivasi modul akuntansi, Preferences, periode, entri log (permanen), fault injection, dan jam sistem. Seluruhnya dipulihkan lewat seed antar-TC dan di hook `after` (fault injection dilepas pada langkah 28).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-416: Upgrade paket yang mengaktifkan modul akuntansi dihitung sebagai aktivasi dan membuat Preferences

1. Atur jam server dan jam browser ke 10 Maret 2026 dan Time Zone entitas Asia/Jakarta
2. Bentuk kondisi PC-11 dan PC-16 lewat seed: company PT Contoh Konstruksi pada plan Starter dan belum pernah mengaktifkan modul akuntansi (precondition TC, tidak diasersi)
3. Catat jumlah baris awal Changelog Preferences (N_cl) lewat kemampuan baca BE (company belum memiliki Preferences)
4. Upgrade plan company dari Starter ke Growth dan selesaikan transaksi aktivasi modul akuntansi pada modul pemilik transaksi aktivasi modul akuntansi (belum disusun; disediakan tim FE setelah modul tersedia) hingga aktivasi selesai
5. Buka Settings > Accounting > Preferences
6. Verifikasi untuk setiap baris tabel "Nilai awal Preferences" di Prerequisites (16 baris), nilai pada setting baris itu sama dengan kolom Nilai awal
7. Klik ikon View history dan amati modal Changelog: Preferences
8. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
9. Verifikasi baris baru modal Changelog: Preferences memiliki Action = Create
10. Tutup modal Changelog

### TC-FA-PREF-417: Aktivasi ulang modul akuntansi tidak membuat Preferences baru dan mempertahankan nilai tersimpan

11. Bentuk kondisi PC-16 lewat seed: modul akuntansi pernah aktif lalu dinonaktifkan; Default Capitalization Threshold tersimpan 10.000.000 dan Changelog memuat 1 baris Create (precondition TC, tidak diasersi)
12. Catat jumlah baris Action = Create di Changelog Preferences (N_create; 1 menurut Precondition TC) lewat kemampuan baca BE
13. Aktifkan kembali modul akuntansi untuk PT Contoh Konstruksi pada modul pemilik transaksi aktivasi modul akuntansi (belum disusun; disediakan tim FE setelah modul tersedia) hingga aktivasi selesai
14. Buka Settings > Accounting > Preferences dan amati Default Capitalization Threshold
15. Verifikasi Default Capitalization Threshold tetap 10.000.000 (tampil Rp 10.000.000,00)
16. Klik ikon View history dan hitung baris Action = Create
17. Verifikasi modal Changelog: Preferences tetap memuat tepat 1 baris Action = Create (sama dengan N_create)
18. Tutup modal Changelog

### TC-FA-PREF-418: Pembuatan Preferences yang gagal pada aktivasi membatalkan aktivasi

19. Bentuk kondisi PC-16 lewat seed: company PT Contoh Konstruksi belum pernah mengaktifkan modul akuntansi dan belum memiliki baris Preferences (precondition TC, tidak diasersi)
20. Atur kegagalan pembuatan Preferences di tengah transaksi aktivasi lewat fixture BE untuk sesi ini
21. Aktifkan modul akuntansi untuk PT Contoh Konstruksi pada modul pemilik transaksi aktivasi modul akuntansi (belum disusun; disediakan tim FE setelah modul tersedia) hingga aktivasi selesai
22. Amati hasil aktivasi
23. Verifikasi aktivasi dibatalkan dan modul akuntansi tetap belum aktif
24. Buka Settings > Accounting
25. Verifikasi tidak ada baris Preferences tersimpan untuk company (dibaca lewat kemampuan baca BE)
26. Verifikasi tidak ada periode akuntansi awal tersimpan untuk company (dibaca lewat kemampuan baca BE)
27. Verifikasi tidak ada entri log Create untuk Preferences tersimpan (dibaca lewat kemampuan baca BE)
28. Lepas kegagalan buatan lewat fixture BE

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 2, 3, 10, 11, 12, 18, 19, 20, 28 (seed precondition TC, pengaturan jam atau fault injection bila dipakai spec, pencatatan baseline, menutup modal, pemulihan kondisi).
- Langkah 6 diulang per baris tabel "Nilai awal Preferences" di Prerequisites (8b butir 7); parameter tiap iterasi ada di tabel itu dan `Verifikasi` tetap satu per klausa (S-01).
- P-2: kegagalan pembuatan Preferences (langkah fault injection TC-FA-PREF-418) hanya membentuk kondisi gagal yang diamati; P-5 butir b: TC-FA-PREF-418 adalah satu-satunya TC objek uji ringan kelas b pada spec ini (pemicu fixture BE, tanpa harness eksternal).
- TC-FA-PREF-418: Expected b (tidak ada Preferences, periode awal, maupun log Create) dibaca lewat kemampuan baca BE karena modul akuntansi belum aktif dan tidak ada permukaan UI; anchor positif adalah `Verifikasi` hasil aktivasi dibatalkan (8b butir 2). Langkah TC 3 ("amati ketersediaan tab Preferences dan periode") tidak punya Expected UI sehingga hanya menjadi langkah navigasi.
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Kolom Automatable TC menandai pemicu job J-01, kegagalan sisi server, atau aktivasi sebagai "Manual Only" atau memakai langkah generik pada modul yang belum disusun; spec tetap ditulis penuh sesuai bagian 2 dan menyatakan kebutuhannya di Prerequisites.
  - Expected TC menulis "Default Capitalization Threshold = 5.000.000", sedangkan Catatan TC menyatakan tampilan input memakai simbol mata uang dan dua desimal (Rp 5.000.000,00); spec mengasersi nilai 5.000.000 dan menyebut tampilannya di tabel.
  - Expected TC menyebut jumlah baris log sebagai angka absolut ("tepat 1 baris", "1 baris"); log adalah audit trail permanen sehingga spec memakai baseline jumlah baris sebelum aksi dan mengasersi selisih (S-12). Mohon TC ditulis relatif.
  - Kolom Automatable TC-FA-PREF-418 menandai "Manual Only" (pemicu kegagalan sisi server tidak tersedia lewat test API); spec ditulis penuh dengan pemicu fixture BE yang disediakan tim BE.
  - Precondition TC-FA-PREF-416 menyebut "User berada di Settings > Accounting > Preferences" pada company plan Starter; spec membuka Preferences setelah upgrade (S-15).
  - Post Condition TC-FA-PREF-416 sampai 418 tidak punya langkah observasi sendiri; padanannya ada pada Expected (S-01).

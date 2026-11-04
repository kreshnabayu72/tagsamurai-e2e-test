---
id: TC-FA-PREF-E2E-134-deferred-aktivasi-pertama-modul-akuntansi-membuat-preferences-periode-awal-changelog-tanpa-offset
title: "[DEFERRED] Aktivasi Pertama Modul Akuntansi Membuat Preferences, Periode Awal, dan Changelog tanpa Offset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-411
  - TC-FA-PREF-412
  - TC-FA-PREF-413
  - TC-FA-PREF-414
  - TC-FA-PREF-415
coverage:
  web: automated
---

# [DEFERRED] Aktivasi Pertama Modul Akuntansi Membuat Preferences, Periode Awal, dan Changelog tanpa Offset

## Prerequisites

- Mode: FE+BE.
- Kelas fungsional; TC `[DEFERRED]`. Modul pemilik transaksi aktivasi modul akuntansi, job rekonsiliasi J-01, modul Asset (status dan in-service date), serta modul Accounting Period adalah modul pemilik/konsumen yang belum disusun: TC `[DEFERRED]` (NC-08, NC-09) ditulis dengan langkah generik pada modul itu dan hanya mengasersi klaim yang tertulis di TC dan PRD; seluruh kebutuhan modul disediakan tim FE setelah modul tersedia.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth) belum pernah mengaktifkan modul akuntansi dan belum memiliki baris Preferences (PC-16); Rina Anggraini melakukan aktivasi dan tampil "Rina A" (PC-8); Time Zone entitas Asia/Jakarta (PC-15). Kondisi awal dibentuk ulang lewat seed sebelum tiap TC.
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
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): pemicu aktivasi modul akuntansi pada modul pemilik (disediakan tim FE setelah modul tersedia); seed dan pemulihan kondisi company (PC-13, PC-16, status plan dan entitas) lewat API (butir "Seed dan pemulihan lewat API" di `suite.md`); kendali jam sistem (clock; butir "Kendali jam sistem" di `suite.md`); pembacaan jumlah baris Changelog Preferences, System Log, dan Activity Log lewat kemampuan baca BE sebelum aksi (8b.10, S-12). Jam sistem (clock): jam server dan jam browser diatur bersama ke 10 Maret 2026 dan Time Zone entitas Asia/Jakarta (PC-15) pada langkah 1, dipulihkan di hook `after`.
- State yang diubah spec: aktivasi modul akuntansi company, Preferences, periode akuntansi awal, entri log (permanen), dan jam sistem. Kondisi company dipulihkan lewat seed antar-TC dan di hook `after`; jam sistem dipulihkan di hook `after`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Cara menemukan baris berdasarkan isi pada log berpaginasi: jam diatur ke masa lalu sehingga entri baru tidak dijamin berada di halaman pertama; di modal Changelog pakai Filter Field dan New Value, di System Log dan Activity Log pakai Search, atau telusuri semua halaman hingga baris dengan isi itu ditemukan.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-411: Aktivasi pertama modul akuntansi membuat Preferences dengan nilai awal

1. Atur jam server dan jam browser ke 10 Maret 2026 dan Time Zone entitas Asia/Jakarta
2. Bentuk kondisi PC-16 lewat seed: company PT Contoh Konstruksi belum pernah mengaktifkan modul akuntansi dan belum memiliki baris Preferences (precondition TC, tidak diasersi)
3. Aktifkan modul akuntansi untuk PT Contoh Konstruksi pada modul pemilik transaksi aktivasi modul akuntansi (belum disusun; disediakan tim FE setelah modul tersedia) sebagai Rina Anggraini hingga aktivasi selesai
4. Buka Settings > Accounting > Preferences dan amati nilai semua setting pada tab
5. Verifikasi untuk setiap baris tabel "Nilai awal Preferences" di Prerequisites (16 baris), nilai pada setting baris itu sama dengan kolom Nilai awal

### TC-FA-PREF-412: Aktivasi pertama membuat periode akuntansi awal Open dari First Accounting Period sampai akhir tahun fiskal

6. Bentuk kondisi PC-16 lewat seed: company PT Contoh Konstruksi belum pernah mengaktifkan modul akuntansi dan belum memiliki baris Preferences (precondition TC, tidak diasersi)
7. Aktifkan modul akuntansi untuk PT Contoh Konstruksi pada modul pemilik transaksi aktivasi modul akuntansi (belum disusun; disediakan tim FE setelah modul tersedia) hingga aktivasi selesai
8. Buka daftar periode di modul Accounting Period (`settings-accounting-period/`), atur ukuran halaman ke 25, dan amati periode yang tampil
9. Verifikasi Accounting Period memuat 10 periode bulanan dari Mar 2026 sampai Dec 2026
10. Verifikasi seluruh 10 periode berstatus Open

### TC-FA-PREF-413: Aktivasi pertama menulis satu entri Create di Changelog

11. Bentuk kondisi PC-16 lewat seed: company PT Contoh Konstruksi belum pernah mengaktifkan modul akuntansi dan belum memiliki baris Preferences (precondition TC, tidak diasersi)
12. Catat jumlah baris awal Changelog Preferences (N_cl) lewat kemampuan baca BE (company belum memiliki Preferences)
13. Aktifkan modul akuntansi untuk PT Contoh Konstruksi pada modul pemilik transaksi aktivasi modul akuntansi (belum disusun; disediakan tim FE setelah modul tersedia) sebagai Rina Anggraini hingga aktivasi selesai
14. Buka Settings > Accounting > Preferences
15. Klik ikon View history dan amati modal Changelog: Preferences
16. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
17. Verifikasi baris modal Changelog: Preferences (dicari berdasarkan isi: Field = Preferences, New Value = Initial values): Action = Create, Section = —, Field = Preferences, Old Value = —, New Value = Initial values, Modified By = Rina A
18. Tutup modal Changelog

### TC-FA-PREF-414: Aktivasi pertama menulis entri Create di System Log dan Activity Log user yang mengaktifkan modul

19. Bentuk kondisi PC-16 lewat seed: company PT Contoh Konstruksi belum pernah mengaktifkan modul akuntansi dan belum memiliki baris Preferences (precondition TC, tidak diasersi)
20. Catat jumlah baris awal System Log milik Rina Anggraini (N_sl) dan Activity Log FAMS (N_al) lewat kemampuan baca BE
21. Aktifkan modul akuntansi untuk PT Contoh Konstruksi pada modul pemilik transaksi aktivasi modul akuntansi (belum disusun; disediakan tim FE setelah modul tersedia) sebagai Rina Anggraini hingga aktivasi selesai
22. Buka Global Settings > User
23. Ketik Search "Rina Anggraini", tekan Enter
24. Klik Name "Rina Anggraini"
25. Klik Tab System Log
26. Verifikasi jumlah baris System Log bertambah tepat 1 dari N_sl
27. Verifikasi baris System Log (dicari berdasarkan isi: Field = Preferences, New Value = Initial values): Action = Create, Object = Preferences, Name = —, Field = Preferences, Old Value = —, New Value = Initial values
28. Buka Activity Log FAMS dan cari baris Create dengan Field = Preferences dan New Value = Initial values (berdasarkan isi, bukan posisi)
29. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 1 dari N_al
30. Verifikasi baris Activity Log FAMS yang ditemukan pada langkah 28: Action = Create, Object = Preferences, Name = —, Field = Preferences, Old Value = —, New Value = Initial values, Modified By = Rina A

### TC-FA-PREF-415: Aktivasi pertama tidak meminta Default Capitalization Offset

31. Bentuk kondisi PC-16 lewat seed: company PT Contoh Konstruksi belum pernah mengaktifkan modul akuntansi dan belum memiliki baris Preferences (precondition TC, tidak diasersi)
32. Aktifkan modul akuntansi untuk PT Contoh Konstruksi pada modul pemilik transaksi aktivasi modul akuntansi (belum disusun; disediakan tim FE setelah modul tersedia) dan amati seluruh langkah aktivasi hingga aktivasi selesai
33. Verifikasi aktivasi modul akuntansi selesai (modul akuntansi aktif)
34. Verifikasi tidak ada permintaan akun Default Capitalization Offset selama langkah aktivasi
35. Buka Settings > Accounting > Preferences dan amati field Default Capitalization Offset
36. Verifikasi Select Default Capitalization Offset menampilkan placeholder "Select account" (kosong)

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 2, 6, 8, 11, 12, 18, 19, 20, 22, 23, 24, 25, 31 (seed precondition TC, pengaturan jam atau fault injection bila dipakai spec, pencatatan baseline sesudah seed pembentuk kondisi, atur ukuran halaman ke 25 pada daftar periode, menutup modal, navigasi ke System Log milik Rina Anggraini lewat Global Settings > User, Search, Name, dan Tab System Log, pemulihan kondisi).
- Langkah 15 dan 17 (modal Changelog) serta langkah 22 sampai 25 dan 28 (System Log dan Activity Log) membuka log lewat UI saat jam masih diatur (langkah 1, dipulihkan di hook `after`); asersinya jumlah baris bertambah tepat 1 dari baseline (tidak memakai kolom Date) dan isi baris baru (langkah 17, 27, 30: Action, Field, New Value) dicari berdasarkan isi, yaitu Field = Preferences dan New Value = Initial values, bukan berdasarkan posisi, karena jam diset mundur ke 10 Maret 2026 sehingga entri baru tidak dijamin menjadi baris teratas (S-09 [KEPUTUSAN 2026-10-13], S-12); langkah tidak disusun ulang.
- Spec ini melewati sekitar 35 langkah (36 langkah nominal) karena lima TC berurutan memakai pemicu aktivasi yang sama, masing-masing membentuk kondisi dan mengasersi sendiri; blok baca-log berpola (buka surface, Search, Name, Tab, lalu `Verifikasi` kolom log) tidak dihitung dalam ambang (bagian 3 prinsip 13, smell).
- Langkah 5 diulang per baris tabel "Nilai awal Preferences" di Prerequisites (8b butir 7); parameter tiap iterasi ada di tabel itu dan `Verifikasi` tetap satu per klausa (S-01).
- TC-FA-PREF-411 sampai 415 ditulis dengan langkah generik aktivasi pada modul pemilik karena TC memintanya; indikator "aktivasi selesai" (langkah TC 415) ditetapkan modul pemilik.
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Kolom Automatable TC menandai pemicu job J-01, kegagalan sisi server, atau aktivasi sebagai "Manual Only" atau memakai langkah generik pada modul yang belum disusun; spec tetap ditulis penuh sesuai bagian 2 dan menyatakan kebutuhannya di Prerequisites.
  - Expected TC menulis "Default Capitalization Threshold = 5.000.000", sedangkan Catatan TC menyatakan tampilan input memakai simbol mata uang dan dua desimal (Rp 5.000.000,00); spec mengasersi nilai 5.000.000 dan menyebut tampilannya di tabel.
  - Expected TC menyebut jumlah baris log sebagai angka absolut ("tepat 1 baris", "1 baris"); log adalah audit trail permanen sehingga spec memakai baseline jumlah baris sebelum aksi dan mengasersi selisih (S-12). Mohon TC ditulis relatif.
  - Post Condition TC-FA-PREF-411 (Preferences tersimpan, periode awal dibuat, log Create) tidak punya langkah observasi sendiri; padanannya ada pada Expected TC-FA-PREF-412, 413, dan 414. Post Condition TC-FA-PREF-412 sampai 415 juga tidak punya langkah observasi sendiri.

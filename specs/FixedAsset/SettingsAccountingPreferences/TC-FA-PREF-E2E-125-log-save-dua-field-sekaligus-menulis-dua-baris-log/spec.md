---
id: TC-FA-PREF-E2E-125-log-save-dua-field-sekaligus-menulis-dua-baris-log
title: "Log: Save Dua Field Sekaligus Menulis Dua Baris Log di Tiga Surface"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-378
  - TC-FA-PREF-379
sourceRules: ["D-01", "FAPREF-LOGIC-10a", "F-FAPREF-01.k21a", "PV-04", "F-FAPREF-01.k20c", "PV-05", "F-FAPREF-01.k20e", "F-FAPREF-01.k20a", "T-01", "L-02a", "L-02e", "§4.1.4#r1", "§4.1.4#r2", "§8#r4", "§4.1.4#r3", "§8#b1", "§4.1.4#r4", "§4.1.4#r7", "SET-01", "L-02g", "SET-12", "L-02l", "L-02b", "§8.2#r1", "§8.2#p2", "L-02c", "L-02d", "§8.3#p1", "FAPREF-LOGIC-10j", "§4.2b#b1", "§8#b2", "SET-07", "L-02f"]
smoke: []
dependsOn: []
trace:
  "D-01": 5
  "FAPREF-LOGIC-10a": 5
  "F-FAPREF-01.k21a": 5
  "PV-04": 5
  "F-FAPREF-01.k20c": 5
  "PV-05": 5
  "F-FAPREF-01.k20e": 5
  "F-FAPREF-01.k20a": 5
  "T-01": [7, 27]
  "L-02a": [9, 11, 12, 30, 32, 33]
  "L-02e": [9, 10, 15, 19, 30, 31, 36, 40]
  "§4.1.4#r1": [10, 31]
  "§4.1.4#r2": [11, 12, 32, 33]
  "§8#r4": [11, 12, 32, 33]
  "§4.1.4#r3": [11, 12, 32, 33]
  "§8#b1": [11, 12, 32, 33]
  "§4.1.4#r4": [11, 12, 32, 33]
  "§4.1.4#r7": [11, 12, 20, 21, 32, 33, 41, 42]
  "SET-01": [11, 16, 20]
  "L-02g": [11, 16, 20]
  "SET-12": [12, 17, 21]
  "L-02l": [12, 17, 21]
  "L-02b": [15, 16, 17, 36, 37, 38]
  "§8.2#r1": [16, 17, 20, 21]
  "§8.2#p2": [16, 17, 20, 21]
  "L-02c": [19, 20, 21, 40, 41, 42]
  "L-02d": [20, 21, 41, 42]
  "§8.3#p1": [20, 21, 41, 42]
  "FAPREF-LOGIC-10j": 28
  "§4.2b#b1": 28
  "§8#b2": [32, 33, 37, 38, 41, 42]
  "SET-07": [32, 33, 37, 38, 41, 42]
  "L-02f": [32, 33, 37, 38, 41, 42]
coverage:
  web: automated
---

# Log: Save Dua Field Sekaligus Menulis Dua Baris Log di Tiga Surface

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth, entitas Active) seri PC (PC-1): modul akuntansi aktif; Preferences bernilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents Sell/Scrap/Lost/Donate/Trade-in/Write-off Optional, Journal Grouping Group); bulan berjalan Oktober 2026. Untuk TC-FA-PREF-378: belum ada posting penyusutan, semua periode Open, tidak ada transaksi bertanggal; jumlah periode pada dialog (15) bergantung bulan berjalan Oktober 2026 (kendali jam di `suite.md`; jam dipulihkan di hook `after`).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): Seed dan pemulihan lewat API (Preferences ke nilai awal PC-1, Asset Class, akun Chart of Accounts, pelepasan, kunci periode, status company) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`). Pembacaan jumlah baris Changelog Preferences, System Log milik pelaku, dan Activity Log FAMS sebelum aksi lewat kemampuan baca BE (disediakan tim FE/BE; 8b.10, S-12). Jam server dan jam browser sinkron untuk asersi "Date = waktu Save" dengan toleransi satu menit (S-12).
- State yang diubah spec: Preferences company dan entri log (audit trail permanen, tidak dihapus). Preferences dipulihkan ke nilai awal PC-1 lewat seed di antara TC dan di hook `after` (hook tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-378: Save mengubah Fiscal Year Start dan First Accounting Period sekaligus menulis dua baris log

1. Catat jumlah baris awal Changelog Preferences (N_cl), System Log milik Rina Anggraini (N_sl), dan Activity Log FAMS (N_al) lewat kemampuan baca BE
2. Pilih "April" pada Select Fiscal Year Start
3. Pilih bulan "January" dan tahun "2026" pada Select First Accounting Period
4. Klik [Save changes]
5. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "15 accounting periods will be rebuilt."; "Tax year start also follows Fiscal Year Start." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
6. Klik [Save] pada dialog Save Changes
7. Verifikasi toast "Success, accounting preferences have been saved." tampil
8. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
9. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 2 dari N_cl
10. Verifikasi kedua baris baru modal Changelog: Preferences memiliki Date yang sama
11. Verifikasi baris baru Changelog: Action = Edit, Section = General, Field = Fiscal Year Start, Old Value = January, New Value = April, Modified By = Rina A
12. Verifikasi baris baru Changelog: Action = Edit, Section = General, Field = First Accounting Period, Old Value = Mar 2026, New Value = Jan 2026, Modified By = Rina A
13. Tutup modal Changelog
14. Buka Global Settings > User > Detail > Tab System Log milik Rina Anggraini
15. Verifikasi jumlah baris System Log bertambah tepat 2 dari N_sl
16. Verifikasi baris baru System Log: Object = Preferences, Name = —, Field = Fiscal Year Start (January -> April)
17. Verifikasi baris baru System Log: Object = Preferences, Name = —, Field = First Accounting Period (Mar 2026 -> Jan 2026)
18. Buka Activity Log FAMS
19. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 2 dari N_al
20. Verifikasi baris baru Activity Log FAMS: Object = Preferences, Name = —, Modified By = Rina A, Field = Fiscal Year Start (January -> April)
21. Verifikasi baris baru Activity Log FAMS: Object = Preferences, Name = —, Modified By = Rina A, Field = First Accounting Period (Mar 2026 -> Jan 2026)
22. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan, lalu buka Settings > Accounting > Preferences

### TC-FA-PREF-379: Save mengubah Disposal Documents Sell dan Scrap sekaligus menulis dua baris log

23. Catat jumlah baris awal Changelog Preferences (N_cl), System Log milik Rina Anggraini (N_sl), dan Activity Log FAMS (N_al) lewat kemampuan baca BE
24. Pilih "Required" pada Select Disposal Documents jenis Sell
25. Pilih "Required" pada Select Disposal Documents jenis Scrap
26. Klik [Save changes]
27. Verifikasi toast "Success, accounting preferences have been saved." tampil
28. Verifikasi dialog Save Changes tidak tampil
29. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
30. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 2 dari N_cl
31. Verifikasi kedua baris baru modal Changelog: Preferences memiliki Date yang sama
32. Verifikasi baris baru Changelog: Action = Edit, Section = Disposal, Field = Disposal Documents — Sell, Old Value = Optional, New Value = Required, Modified By = Rina A
33. Verifikasi baris baru Changelog: Action = Edit, Section = Disposal, Field = Disposal Documents — Scrap, Old Value = Optional, New Value = Required, Modified By = Rina A
34. Tutup modal Changelog
35. Buka Global Settings > User > Detail > Tab System Log milik Rina Anggraini
36. Verifikasi jumlah baris System Log bertambah tepat 2 dari N_sl
37. Verifikasi baris baru System Log untuk Field Disposal Documents — Sell (Optional -> Required)
38. Verifikasi baris baru System Log untuk Field Disposal Documents — Scrap (Optional -> Required)
39. Buka Activity Log FAMS
40. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 2 dari N_al
41. Verifikasi baris baru Activity Log FAMS untuk Field Disposal Documents — Sell (Optional -> Required, Modified By = Rina A)
42. Verifikasi baris baru Activity Log FAMS untuk Field Disposal Documents — Scrap (Optional -> Required, Modified By = Rina A)
43. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan

## Notes

- Kelas fungsional: tiap TC menyimpan Preferences lewat UI lalu membaca tiga surface log. Asersi "tepat N baris baru" adalah asersi jumlah terhadap baseline (bukan absence kelas g); S-05 tidak berlaku.
- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 13, 22, 23, 34, 43 (pencatatan baseline, pencatatan waktu Save, menutup modal Changelog, pemulihan Preferences antar-TC lewat seed). Baseline dicatat ulang sebelum pemicu tiap TC (S-12).
- Urutan baca log: jumlah baris dibuktikan bertambah dari baseline lebih dulu, baru baris teratas dibaca (S-14). Jumlah langkah nominal 43; blok baca-log berpola (buka surface, `Verifikasi` jumlah, `Verifikasi` kolom log) pada langkah 8 sampai 21, 29 sampai 42 tidak dihitung ke ambang ~35 langkah (bagian 3 prinsip 13, smell). Seluruh TC berkelas sama (fungsional Save lalu log tiga surface) dan tiap blok berdiri sendiri dengan pemulihan seed di antaranya.
- Expected TC-FA-PREF-378 c dan TC-FA-PREF-379 b meminta "dua baris dengan Date yang sama"; spec mengasersi kesamaan Date kedua baris sebagai satu `Verifikasi` dan nilai tiap baris sebagai `Verifikasi` terpisah (S-01). Date = waktu Save tidak diminta pada kedua TC sehingga waktu Save tidak dicatat.
- Expected TC-FA-PREF-378 d dan e, serta TC-FA-PREF-379 c dan d, menyebut "Object = Preferences, Name = —" untuk kedua baris; kolom itu diasersi pada baris Field Fiscal Year Start dan First Accounting Period pada TC-FA-PREF-378 dan hanya Field/Old/New pada TC-FA-PREF-379 sesuai teks TC.
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Expected TC menyebut baris log baru sebagai "tepat N baris baru" tanpa menyebut baseline; spec mencatat baseline jumlah baris tiap surface sebelum aksi lewat kemampuan baca BE dan mengasersi selisih (S-12, S-14).
  - Post Condition TC 378 dan 379 tidak punya langkah observasi sendiri di TC; padanannya ada pada Expected yang diasersi (S-01). Post Condition "Nilai terbaru dibaca oleh ... (belum disusun)" tidak diasersi karena modul konsumen belum disusun.

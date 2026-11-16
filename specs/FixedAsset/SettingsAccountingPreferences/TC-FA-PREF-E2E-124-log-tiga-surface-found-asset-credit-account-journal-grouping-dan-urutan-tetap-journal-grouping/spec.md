---
id: TC-FA-PREF-E2E-124-log-tiga-surface-found-asset-credit-account-journal-grouping-dan-urutan-tetap-journal-grouping
title: "Log Tiga Surface: Found Asset Credit Account, Journal Grouping, dan Urutan Tetap Journal Grouping"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-376
  - TC-FA-PREF-377
  - TC-FA-PREF-388
sourceRules: ["T-01", "§3.1#b6", "L-02a", "L-02e", "§4.1.4#r1", "§4.1.4#r2", "§8#r4", "§4.1.4#r3", "§8#b1", "§4.1.4#r4", "§4.1.4#r7", "§4.1.4#p1", "SET-09", "L-02i", "L-02h", "L-02b", "§8.2#r1", "§8.2#p2", "§8.2#p1", "L-02c", "L-02d", "§8.3#p1", "SET-11", "L-02f", "FAPREF-LOGIC-10j", "§4.2b#b1"]
smoke: []
dependsOn: []
trace:
  "T-01": [4, 22, 40]
  "§3.1#b6": [5, 23]
  "L-02a": [8, 9, 26, 27, 43, 44]
  "L-02e": [8, 12, 16, 26, 30, 34, 43]
  "§4.1.4#r1": [9, 27]
  "§4.1.4#r2": [9, 27, 44]
  "§8#r4": [9, 27, 44]
  "§4.1.4#r3": [9, 27, 44]
  "§8#b1": [9, 27, 44]
  "§4.1.4#r4": [9, 27, 44]
  "§4.1.4#r7": [9, 17, 27, 35]
  "§4.1.4#p1": [9, 27, 44]
  "SET-09": [9, 13, 17]
  "L-02i": [9, 13, 17]
  "L-02h": [9, 13, 17]
  "L-02b": [12, 13, 30, 31]
  "§8.2#r1": [13, 17, 31, 35]
  "§8.2#p2": [13, 17, 31, 35]
  "§8.2#p1": [14, 32]
  "L-02c": [16, 17, 34, 35]
  "L-02d": [17, 35]
  "§8.3#p1": [17, 35]
  "SET-11": [27, 31, 35, 44]
  "L-02f": [27, 31, 35, 44]
  "FAPREF-LOGIC-10j": 41
  "§4.2b#b1": 41
coverage:
  web: automated
---

# Log Tiga Surface: Found Asset Credit Account, Journal Grouping, dan Urutan Tetap Journal Grouping

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth, entitas Active) seri PC (PC-1): modul akuntansi aktif; Preferences bernilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents Sell/Scrap/Lost/Donate/Trade-in/Write-off Optional, Journal Grouping Group); bulan berjalan Oktober 2026. Untuk TC-FA-PREF-376: Found Asset Credit Account tersimpan kosong; akun 4-1500 – Pendapatan Lain-lain Active (PC-5).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): Seed dan pemulihan lewat API (Preferences ke nilai awal PC-1, Asset Class, akun Chart of Accounts, pelepasan, kunci periode, status company) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`). Pembacaan jumlah baris Changelog Preferences, System Log milik pelaku, dan Activity Log FAMS sebelum aksi lewat kemampuan baca BE (disediakan tim FE/BE; 8b.10, S-12). Jam server dan jam browser sinkron untuk asersi "Date = waktu Save" dengan toleransi satu menit (S-12).
- State yang diubah spec: Preferences company dan entri log (audit trail permanen, tidak dihapus). Preferences dipulihkan ke nilai awal PC-1 lewat seed di antara TC dan di hook `after` (hook tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-376: Save perubahan Found Asset Credit Account tercatat di tiga surface

1. Catat jumlah baris awal Changelog Preferences (N_cl), System Log milik Rina Anggraini (N_sl), dan Activity Log FAMS (N_al) lewat kemampuan baca BE
2. Pilih "4-1500 – Pendapatan Lain-lain" pada Select Found Asset Credit Account
3. Klik [Save changes]
4. Verifikasi toast "Success, accounting preferences have been saved." tampil
5. Verifikasi form Preferences tetap terbuka dengan nilai tersimpan
6. Catat waktu Save (jam server dan jam browser sinkron)
7. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
8. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
9. Verifikasi baris baru di posisi teratas modal Changelog: Preferences: Date = waktu Save (toleransi satu menit), Action = Edit, Section = Chart of Accounts, Field = Found Asset Credit Account, Old Value = —, New Value = 4-1500 – Pendapatan Lain-lain, Modified By = Rina A
10. Tutup modal Changelog
11. Buka Global Settings > User > Detail > Tab System Log milik Rina Anggraini
12. Verifikasi jumlah baris System Log bertambah tepat 1 dari N_sl
13. Verifikasi baris baru di posisi teratas System Log: Action = Edit, Object = Preferences, Name = —, Field = Found Asset Credit Account, Old Value = —, New Value = 4-1500 – Pendapatan Lain-lain
14. Verifikasi header tabel System Log tidak memuat kolom Modified By
15. Buka Activity Log FAMS
16. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 1 dari N_al
17. Verifikasi baris baru di posisi teratas Activity Log FAMS: Action = Edit, Object = Preferences, Name = —, Field = Found Asset Credit Account, Old Value = —, New Value = 4-1500 – Pendapatan Lain-lain, Modified By = Rina A
18. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan, lalu buka Settings > Accounting > Preferences

### TC-FA-PREF-377: Save perubahan Journal Grouping tercatat di tiga surface

19. Catat jumlah baris awal Changelog Preferences (N_cl), System Log milik Rina Anggraini (N_sl), dan Activity Log FAMS (N_al) lewat kemampuan baca BE
20. Tambahkan opsi "Category" pada MultiSelect Journal Grouping sehingga terpilih Group dan Category
21. Klik [Save changes]
22. Verifikasi toast "Success, accounting preferences have been saved." tampil
23. Verifikasi form Preferences tetap terbuka dengan nilai tersimpan
24. Catat waktu Save (jam server dan jam browser sinkron)
25. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
26. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
27. Verifikasi baris baru di posisi teratas modal Changelog: Preferences: Date = waktu Save (toleransi satu menit), Action = Edit, Section = Journal Export, Field = Journal Grouping, Old Value = Group, New Value = Group, Category, Modified By = Rina A
28. Tutup modal Changelog
29. Buka Global Settings > User > Detail > Tab System Log milik Rina Anggraini
30. Verifikasi jumlah baris System Log bertambah tepat 1 dari N_sl
31. Verifikasi baris baru di posisi teratas System Log: Action = Edit, Object = Preferences, Name = —, Field = Journal Grouping, Old Value = Group, New Value = Group, Category
32. Verifikasi header tabel System Log tidak memuat kolom Modified By
33. Buka Activity Log FAMS
34. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 1 dari N_al
35. Verifikasi baris baru di posisi teratas Activity Log FAMS: Action = Edit, Object = Preferences, Name = —, Field = Journal Grouping, Old Value = Group, New Value = Group, Category, Modified By = Rina A
36. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan, lalu buka Settings > Accounting > Preferences

### TC-FA-PREF-388: Journal Grouping dicatat dengan urutan tetap Group, Category, Asset Class

37. Catat jumlah baris awal Changelog Preferences (N_cl) lewat kemampuan baca BE
38. Pada MultiSelect Journal Grouping pilih "Asset Class" terlebih dahulu, lalu pilih "Category" sehingga terpilih Group, Asset Class, dan Category
39. Klik [Save changes]
40. Verifikasi toast "Success, accounting preferences have been saved." tampil
41. Verifikasi dialog Save Changes tidak tampil
42. Klik ikon View history dan amati modal Changelog: Preferences
43. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
44. Verifikasi baris baru di posisi teratas modal Changelog: Preferences: Section = Journal Export, Field = Journal Grouping, Old Value = Group, New Value = Group, Category, Asset Class, Action = Edit
45. Tutup modal Changelog
46. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan

## Notes

- Kelas fungsional: tiap TC menyimpan Preferences lewat UI lalu membaca tiga surface log. Asersi "tepat N baris baru" adalah asersi jumlah terhadap baseline (bukan absence kelas g); S-05 tidak berlaku.
- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 6, 10, 18, 19, 24, 28, 36, 37, 45, 46 (pencatatan baseline, pencatatan waktu Save, menutup modal Changelog, pemulihan Preferences antar-TC lewat seed). Baseline dicatat ulang sebelum pemicu tiap TC (S-12).
- Urutan baca log: jumlah baris dibuktikan bertambah dari baseline lebih dulu, baru baris teratas dibaca (S-14). Jumlah langkah nominal 46; blok baca-log berpola (buka surface, `Verifikasi` jumlah, `Verifikasi` kolom log) pada langkah 7 sampai 17, 25 sampai 35, 42 sampai 44 tidak dihitung ke ambang ~35 langkah (bagian 3 prinsip 13, smell). Seluruh TC berkelas sama (fungsional Save lalu log tiga surface) dan tiap blok berdiri sendiri dengan pemulihan seed di antaranya.
- TC-FA-PREF-388 hanya meminta baris Changelog (Expected b); spec tidak menambah asersi System Log dan Activity Log untuk TC itu, sehingga baseline yang dicatat hanya N_cl.
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Expected TC menyebut baris log baru sebagai "tepat N baris baru" tanpa menyebut baseline; spec mencatat baseline jumlah baris tiap surface sebelum aksi lewat kemampuan baca BE dan mengasersi selisih (S-12, S-14).
  - Post Condition TC 376, 377, dan 388 tidak punya langkah observasi sendiri di TC; padanannya ada pada Expected yang diasersi (S-01). Post Condition "Nilai terbaru dibaca oleh ... (belum disusun)" tidak diasersi karena modul konsumen belum disusun.

---
id: TC-FA-PREF-E2E-122-log-tiga-surface-disposal-documents-scrap-lost-donate
title: "Log Tiga Surface: Disposal Documents Scrap, Lost, dan Donate"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-370
  - TC-FA-PREF-371
  - TC-FA-PREF-372
coverage:
  web: automated
---

# Log Tiga Surface: Disposal Documents Scrap, Lost, dan Donate

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth, entitas Active) seri PC (PC-1): modul akuntansi aktif; Preferences bernilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents Sell/Scrap/Lost/Donate/Trade-in/Write-off Optional, Journal Grouping Group); bulan berjalan Oktober 2026.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): Seed dan pemulihan lewat API (Preferences ke nilai awal PC-1, Asset Class, akun Chart of Accounts, pelepasan, kunci periode, status company) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`). Pembacaan jumlah baris Changelog Preferences, System Log milik pelaku, dan Activity Log FAMS sebelum aksi lewat kemampuan baca BE (disediakan tim FE/BE; 8b.10, S-12). Jam server dan jam browser sinkron untuk asersi "Date = waktu Save" dengan toleransi satu menit (S-12).
- State yang diubah spec: Preferences company dan entri log (audit trail permanen, tidak dihapus). Preferences dipulihkan ke nilai awal PC-1 lewat seed di antara TC dan di hook `after` (hook tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-370: Save perubahan Disposal Documents — Scrap tercatat di tiga surface

1. Catat jumlah baris awal Changelog Preferences (N_cl), System Log milik Rina Anggraini (N_sl), dan Activity Log FAMS (N_al) lewat kemampuan baca BE
2. Pilih "Required" pada Select Disposal Documents jenis Scrap
3. Klik [Save changes]
4. Verifikasi toast "Success, accounting preferences have been saved." tampil
5. Verifikasi form Preferences tetap terbuka dengan nilai tersimpan
6. Catat waktu Save (jam server dan jam browser sinkron)
7. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
8. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
9. Verifikasi baris baru di posisi teratas modal Changelog: Preferences: Date = waktu Save (toleransi satu menit), Action = Edit, Section = Disposal, Field = Disposal Documents — Scrap, Old Value = Optional, New Value = Required, Modified By = Rina A
10. Tutup modal Changelog
11. Buka Global Settings > User > Detail > Tab System Log milik Rina Anggraini
12. Verifikasi jumlah baris System Log bertambah tepat 1 dari N_sl
13. Verifikasi baris baru di posisi teratas System Log: Action = Edit, Object = Preferences, Name = —, Field = Disposal Documents — Scrap, Old Value = Optional, New Value = Required
14. Verifikasi header tabel System Log tidak memuat kolom Modified By
15. Buka Activity Log FAMS
16. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 1 dari N_al
17. Verifikasi baris baru di posisi teratas Activity Log FAMS: Action = Edit, Object = Preferences, Name = —, Field = Disposal Documents — Scrap, Old Value = Optional, New Value = Required, Modified By = Rina A
18. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan, lalu buka Settings > Accounting > Preferences

### TC-FA-PREF-371: Save perubahan Disposal Documents — Lost tercatat di tiga surface

19. Catat jumlah baris awal Changelog Preferences (N_cl), System Log milik Rina Anggraini (N_sl), dan Activity Log FAMS (N_al) lewat kemampuan baca BE
20. Pilih "Required" pada Select Disposal Documents jenis Lost
21. Klik [Save changes]
22. Verifikasi toast "Success, accounting preferences have been saved." tampil
23. Verifikasi form Preferences tetap terbuka dengan nilai tersimpan
24. Catat waktu Save (jam server dan jam browser sinkron)
25. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
26. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
27. Verifikasi baris baru di posisi teratas modal Changelog: Preferences: Date = waktu Save (toleransi satu menit), Action = Edit, Section = Disposal, Field = Disposal Documents — Lost, Old Value = Optional, New Value = Required, Modified By = Rina A
28. Tutup modal Changelog
29. Buka Global Settings > User > Detail > Tab System Log milik Rina Anggraini
30. Verifikasi jumlah baris System Log bertambah tepat 1 dari N_sl
31. Verifikasi baris baru di posisi teratas System Log: Action = Edit, Object = Preferences, Name = —, Field = Disposal Documents — Lost, Old Value = Optional, New Value = Required
32. Verifikasi header tabel System Log tidak memuat kolom Modified By
33. Buka Activity Log FAMS
34. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 1 dari N_al
35. Verifikasi baris baru di posisi teratas Activity Log FAMS: Action = Edit, Object = Preferences, Name = —, Field = Disposal Documents — Lost, Old Value = Optional, New Value = Required, Modified By = Rina A
36. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan, lalu buka Settings > Accounting > Preferences

### TC-FA-PREF-372: Save perubahan Disposal Documents — Donate tercatat di tiga surface

37. Catat jumlah baris awal Changelog Preferences (N_cl), System Log milik Rina Anggraini (N_sl), dan Activity Log FAMS (N_al) lewat kemampuan baca BE
38. Pilih "Required" pada Select Disposal Documents jenis Donate
39. Klik [Save changes]
40. Verifikasi toast "Success, accounting preferences have been saved." tampil
41. Verifikasi form Preferences tetap terbuka dengan nilai tersimpan
42. Catat waktu Save (jam server dan jam browser sinkron)
43. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
44. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
45. Verifikasi baris baru di posisi teratas modal Changelog: Preferences: Date = waktu Save (toleransi satu menit), Action = Edit, Section = Disposal, Field = Disposal Documents — Donate, Old Value = Optional, New Value = Required, Modified By = Rina A
46. Tutup modal Changelog
47. Buka Global Settings > User > Detail > Tab System Log milik Rina Anggraini
48. Verifikasi jumlah baris System Log bertambah tepat 1 dari N_sl
49. Verifikasi baris baru di posisi teratas System Log: Action = Edit, Object = Preferences, Name = —, Field = Disposal Documents — Donate, Old Value = Optional, New Value = Required
50. Verifikasi header tabel System Log tidak memuat kolom Modified By
51. Buka Activity Log FAMS
52. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 1 dari N_al
53. Verifikasi baris baru di posisi teratas Activity Log FAMS: Action = Edit, Object = Preferences, Name = —, Field = Disposal Documents — Donate, Old Value = Optional, New Value = Required, Modified By = Rina A
54. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan

## Notes

- Kelas fungsional: tiap TC menyimpan Preferences lewat UI lalu membaca tiga surface log. Asersi "tepat N baris baru" adalah asersi jumlah terhadap baseline (bukan absence kelas g); S-05 tidak berlaku.
- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 6, 10, 18, 19, 24, 28, 36, 37, 42, 46, 54 (pencatatan baseline, pencatatan waktu Save, menutup modal Changelog, pemulihan Preferences antar-TC lewat seed). Baseline dicatat ulang sebelum pemicu tiap TC (S-12).
- Urutan baca log: jumlah baris dibuktikan bertambah dari baseline lebih dulu, baru baris teratas dibaca (S-14). Jumlah langkah nominal 54; blok baca-log berpola (buka surface, `Verifikasi` jumlah, `Verifikasi` kolom log) pada langkah 7 sampai 17, 25 sampai 35, 43 sampai 53 tidak dihitung ke ambang ~35 langkah (bagian 3 prinsip 13, smell). Seluruh TC berkelas sama (fungsional Save lalu log tiga surface) dan tiap blok berdiri sendiri dengan pemulihan seed di antaranya.
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Expected TC menyebut baris log baru sebagai "tepat N baris baru" tanpa menyebut baseline; spec mencatat baseline jumlah baris tiap surface sebelum aksi lewat kemampuan baca BE dan mengasersi selisih (S-12, S-14).
  - Post Condition TC 370 sampai 372 tidak punya langkah observasi sendiri di TC; padanannya ada pada Expected yang diasersi (S-01). Post Condition "Nilai terbaru dibaca oleh ... (belum disusun)" tidak diasersi karena modul konsumen belum disusun.

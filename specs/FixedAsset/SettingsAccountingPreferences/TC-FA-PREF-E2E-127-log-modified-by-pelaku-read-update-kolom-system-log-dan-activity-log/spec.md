---
id: TC-FA-PREF-E2E-127-log-modified-by-pelaku-read-update-kolom-system-log-dan-activity-log
title: "Log: Kolom System Log dan Activity Log serta Modified By Pelaku Manage accounting - Read + Update"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-383
  - TC-FA-PREF-384
  - TC-FA-PREF-385
coverage:
  web: automated
---

# Log: Kolom System Log dan Activity Log serta Modified By Pelaku Manage accounting - Read + Update

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Akun kedua (TC-FA-PREF-385): Manage accounting - Read + Update (Budi Santoso, tampil "Budi S"; PC-8) `manageAccountingReadUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_MARU_PASSWORD`. Email Budi Santoso tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Env var `FA_MARU_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth, entitas Active) seri PC (PC-1): modul akuntansi aktif; Preferences bernilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents Sell/Scrap/Lost/Donate/Trade-in/Write-off Optional, Journal Grouping Group); bulan berjalan Oktober 2026. Total Control Rina Anggraini tampil "Rina A"; Manage accounting - Read + Update bernama Budi Santoso dan tampil "Budi S" (PC-8). Default Capitalization Threshold tersimpan 5.000.000; Asset Class Vehicles dan Furniture tidak mengisi threshold sendiri (PC-6).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): login akun kedua Manage accounting - Read + Update di langkah ganti akun. Seed dan pemulihan lewat API (Preferences ke nilai awal PC-1, Asset Class, akun Chart of Accounts, pelepasan, kunci periode, status company) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`). Pembacaan jumlah baris Changelog Preferences, System Log milik pelaku, dan Activity Log FAMS sebelum aksi lewat kemampuan baca BE (disediakan tim FE/BE; 8b.10, S-12). Jam server dan jam browser sinkron untuk asersi "Date = waktu Save" dengan toleransi satu menit (S-12).
- State yang diubah spec: Preferences company dan entri log (audit trail permanen, tidak dihapus). Preferences dipulihkan ke nilai awal PC-1 lewat seed di antara TC dan di hook `after` (hook tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-383: Screening System Log setelah Save: kolom dan baris Preferences

1. Catat jumlah baris awal System Log milik Rina Anggraini (N_sl) lewat kemampuan baca BE
2. Ubah Default Capitalization Threshold menjadi "10000000"
3. Klik [Save changes]
4. Klik [Save] pada dialog Save Changes
5. Tunggu aksi selesai
6. Buka Global Settings > User > Detail > Tab System Log milik Rina Anggraini
7. Verifikasi jumlah baris System Log bertambah tepat 1 dari N_sl
8. Verifikasi header tabel System Log berurutan: Date, Action, Object, Name, Field, Old Value, New Value
9. Verifikasi header tabel System Log tidak memuat kolom Modified By
10. Verifikasi baris teratas System Log: Action = Edit, Object = Preferences, Name = —, Field = Default Capitalization Threshold, Old Value = 5.000.000, New Value = 10.000.000
11. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan, lalu buka Settings > Accounting > Preferences

### TC-FA-PREF-384: Screening Activity Log FAMS setelah Save: kolom dan baris Preferences

12. Catat jumlah baris awal Activity Log FAMS (N_al) lewat kemampuan baca BE
13. Ubah Default Capitalization Threshold menjadi "10000000"
14. Klik [Save changes]
15. Klik [Save] pada dialog Save Changes
16. Tunggu aksi selesai
17. Buka Activity Log FAMS
18. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 1 dari N_al
19. Verifikasi header tabel Activity Log berurutan: Date, Action, Object, Name, Field, Old Value, New Value, Modified By
20. Verifikasi baris teratas Activity Log: Action = Edit, Object = Preferences, Name = —, Field = Default Capitalization Threshold, Old Value = 5.000.000, New Value = 10.000.000, Modified By = Rina A
21. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan, lalu buka Settings > Accounting > Preferences

### TC-FA-PREF-385: Save oleh Manage accounting - Read + Update mencatat Modified By pelaku di tiga surface

22. Ganti akun: Logout dari akun Total Control
23. Login sebagai Manage accounting - Read + Update (Budi Santoso, `manageAccountingReadUpdate_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_MARU_PASSWORD`), lalu buka Settings > Accounting > Preferences
24. Catat jumlah baris awal Changelog Preferences (N_cl), System Log milik Budi Santoso (N_sl), dan Activity Log FAMS (N_al) lewat kemampuan baca BE
25. Pilih "Manual by Accounting" pada Select In-service Date Source
26. Klik [Save changes]
27. Verifikasi toast "Success, accounting preferences have been saved." tampil
28. Verifikasi dialog Save Changes tidak tampil
29. Catat waktu Save (jam server dan jam browser sinkron)
30. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
31. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
32. Verifikasi baris baru di posisi teratas modal Changelog: Preferences: Date = waktu Save (toleransi satu menit), Action = Edit, Section = Capitalization, Field = In-service Date Source, Old Value = Activation date, New Value = Manual by Accounting, Modified By = Budi S
33. Tutup modal Changelog
34. Buka Global Settings > User > Detail > Tab System Log milik Budi Santoso
35. Verifikasi jumlah baris System Log bertambah tepat 1 dari N_sl
36. Verifikasi baris baru di posisi teratas System Log: Action = Edit, Object = Preferences, Name = —, Field = In-service Date Source, Old Value = Activation date, New Value = Manual by Accounting
37. Verifikasi header tabel System Log tidak memuat kolom Modified By
38. Buka Activity Log FAMS
39. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 1 dari N_al
40. Verifikasi baris baru di posisi teratas Activity Log FAMS: Action = Edit, Object = Preferences, Name = —, Field = In-service Date Source, Old Value = Activation date, New Value = Manual by Accounting, Modified By = Budi S
41. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan

## Notes

- Kelas fungsional: tiap TC menyimpan Preferences lewat UI lalu membaca tiga surface log. Asersi "tepat N baris baru" adalah asersi jumlah terhadap baseline (bukan absence kelas g); S-05 tidak berlaku.
- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 5, 11, 12, 16, 21, 22, 23, 24, 29, 33, 41 (pencatatan baseline, pencatatan waktu Save, menutup modal Changelog, pemulihan Preferences antar-TC lewat seed). Baseline dicatat ulang sebelum pemicu tiap TC (S-12).
- Urutan baca log: jumlah baris dibuktikan bertambah dari baseline lebih dulu, baru baris teratas dibaca (S-14). Jumlah langkah nominal 41; blok baca-log berpola (buka surface, `Verifikasi` jumlah, `Verifikasi` kolom log) pada langkah 6 sampai 10, 17 sampai 20, 30 sampai 40 tidak dihitung ke ambang ~35 langkah (bagian 3 prinsip 13, smell). Seluruh TC berkelas sama (fungsional Save lalu log tiga surface) dan tiap blok berdiri sendiri dengan pemulihan seed di antaranya.
- TC-FA-PREF-383 dan 384 hanya meminta satu surface masing-masing (Expected a dan b); baseline yang dicatat hanya surface itu. `Verifikasi` jumlah baris bertambah tepat 1 ditambahkan sebelum baris teratas dibaca karena entri baru dibaca pada baris teratas setelah selisih dari baseline dibuktikan (S-12, S-14, S-03).
- Langkah ganti akun pada TC-FA-PREF-385 eksplisit (S-07); hook `after` mengembalikan sesi ke akun default suite.
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Expected TC menyebut baris log baru sebagai "tepat N baris baru" tanpa menyebut baseline; spec mencatat baseline jumlah baris tiap surface sebelum aksi lewat kemampuan baca BE dan mengasersi selisih (S-12, S-14).
  - Post Condition TC 383 sampai 385 tidak punya langkah observasi sendiri di TC; padanannya ada pada Expected yang diasersi (S-01). Post Condition "Nilai terbaru dibaca oleh ... (belum disusun)" tidak diasersi karena modul konsumen belum disusun.
  - Email Budi Santoso (Manage accounting - Read + Update, PC-8) tidak tertulis di Pre-setup TC; spec memakai pola email akun role Manage accounting - Read + Update dan meminta konfirmasi tim FE (S-11).
  - TC-FA-PREF-385 membuka Global Settings > User > Detail > Tab System Log milik Budi Santoso tanpa menyatakan apakah akun Manage accounting - Read + Update memiliki akses ke Global Settings > User; spec mengikuti TC dan akses itu perlu dikonfirmasi tim FE.

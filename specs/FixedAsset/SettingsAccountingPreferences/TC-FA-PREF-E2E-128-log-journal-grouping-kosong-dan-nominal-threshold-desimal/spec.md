---
id: TC-FA-PREF-E2E-128-log-journal-grouping-kosong-dan-nominal-threshold-desimal
title: "Log: Journal Grouping Dikosongkan atau Diisi dari Kosong dan Nominal Threshold Desimal"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-389
  - TC-FA-PREF-390
  - TC-FA-PREF-391
sourceRules: ["T-01", "FAPREF-LOGIC-10a", "L-02a", "L-02j", "SET-11", "D-01", "PV-01", "FAPREF-LOGIC-03e", "S-01g"]
smoke: []
dependsOn: []
trace:
  "T-01": [4, 15]
  "FAPREF-LOGIC-10a": [5, 16]
  "L-02a": [7, 18, 29, 42]
  "L-02j": [8, 19, 30, 34, 43, 47]
  "SET-11": [8, 19]
  "D-01": [25, 38]
  "PV-01": [25, 38]
  "FAPREF-LOGIC-03e": [27, 40]
  "S-01g": [33, 46]
coverage:
  web: automated
---

# Log: Journal Grouping Dikosongkan atau Diisi dari Kosong dan Nominal Threshold Desimal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth, entitas Active) seri PC (PC-1): modul akuntansi aktif; Preferences bernilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents Sell/Scrap/Lost/Donate/Trade-in/Write-off Optional, Journal Grouping Group); bulan berjalan Oktober 2026. Format angka tetap platform: pemisah ribuan titik dan pemisah desimal koma (PC-15). Default Capitalization Threshold tersimpan 5.000.000; Asset Class Vehicles dan Furniture tidak mengisi threshold sendiri (PC-6). TC-FA-PREF-390 memerlukan Journal Grouping tersimpan kosong (PC-1 dengan Journal Grouping dikosongkan).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): Seed dan pemulihan lewat API (Preferences ke nilai awal PC-1, Asset Class, akun Chart of Accounts, pelepasan, kunci periode, status company) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`). Pembacaan jumlah baris Changelog Preferences, System Log milik pelaku, dan Activity Log FAMS sebelum aksi lewat kemampuan baca BE (disediakan tim FE/BE; 8b.10, S-12). Jam server dan jam browser sinkron untuk asersi "Date = waktu Save" dengan toleransi satu menit (S-12).
- State yang diubah spec: Preferences company dan entri log (audit trail permanen, tidak dihapus). Preferences dipulihkan ke nilai awal PC-1 lewat seed di antara TC dan di hook `after` (hook tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-389: Journal Grouping dikosongkan dicatat dengan New Value em dash

1. Catat jumlah baris awal Changelog Preferences (N_cl) lewat kemampuan baca BE
2. Hapus pilihan "Group" pada MultiSelect Journal Grouping sehingga tidak ada dimensi terpilih
3. Klik [Save changes]
4. Verifikasi toast "Success, accounting preferences have been saved." tampil
5. Verifikasi dialog Save Changes tidak tampil
6. Klik ikon View history dan amati modal Changelog: Preferences
7. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
8. Verifikasi baris baru Changelog: Section = Journal Export, Field = Journal Grouping, Old Value = Group, New Value = —, Action = Edit
9. Tutup modal Changelog
10. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan, lalu buka Settings > Accounting > Preferences

### TC-FA-PREF-390: Journal Grouping diisi dari kosong dicatat dengan Old Value em dash

11. Seed Preferences PC-1 dengan Journal Grouping dikosongkan hingga tersimpan, lalu muat ulang halaman Preferences (dipakai sebagai precondition TC, tidak diasersi)
12. Catat jumlah baris awal Changelog Preferences (N_cl) lewat kemampuan baca BE
13. Pilih "Asset Class" pada MultiSelect Journal Grouping
14. Klik [Save changes]
15. Verifikasi toast "Success, accounting preferences have been saved." tampil
16. Verifikasi dialog Save Changes tidak tampil
17. Klik ikon View history dan amati modal Changelog: Preferences
18. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
19. Verifikasi baris baru Changelog: Section = Journal Export, Field = Journal Grouping, Old Value = —, New Value = Asset Class, Action = Edit
20. Tutup modal Changelog
21. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan, lalu buka Settings > Accounting > Preferences

### TC-FA-PREF-391: Default Capitalization Threshold desimal dicatat dengan pemisah ribuan tanpa simbol mata uang

22. Catat jumlah baris awal Changelog Preferences (N_cl_1) dan Activity Log FAMS (N_al_1) lewat kemampuan baca BE
23. Ubah Default Capitalization Threshold menjadi "7500000,25"
24. Klik [Save changes]
25. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default threshold." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
26. Klik [Save] pada dialog Save Changes
27. Verifikasi addon awalan "Rp" dan input "7.500.000,25" setelah Save
28. Klik ikon View history dan amati modal Changelog: Preferences
29. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl_1
30. Verifikasi baris baru Changelog: Old Value = 5.000.000, New Value = 7.500.000,25 (tanpa simbol mata uang)
31. Tutup modal Changelog
32. Buka Activity Log FAMS dan amati baris teratas
33. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 1 dari N_al_1
34. Verifikasi baris teratas Activity Log: Old Value = 5.000.000, New Value = 7.500.000,25
35. Buka Settings > Accounting > Preferences dan catat jumlah baris awal Changelog Preferences (N_cl_2) dan Activity Log FAMS (N_al_2) lewat kemampuan baca BE
36. Ubah Default Capitalization Threshold menjadi "7500000,5"
37. Klik [Save changes]
38. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default threshold." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
39. Klik [Save] pada dialog Save Changes
40. Verifikasi addon awalan "Rp" dan input "7.500.000,50" setelah Save kedua (tampilan dua desimal)
41. Klik ikon View history dan amati baris Changelog terbaru
42. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl_2
43. Verifikasi baris baru Changelog: Old Value = 7.500.000,25, New Value = 7.500.000,5 (satu digit desimal tetap satu digit, tanpa padding)
44. Tutup modal Changelog
45. Buka Activity Log FAMS dan amati baris teratas
46. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 1 dari N_al_2
47. Verifikasi baris teratas Activity Log: Old Value = 7.500.000,25, New Value = 7.500.000,5
48. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan

## Notes

- Kelas fungsional: tiap TC menyimpan Preferences lewat UI lalu membaca tiga surface log. Asersi "tepat N baris baru" adalah asersi jumlah terhadap baseline (bukan absence kelas g); S-05 tidak berlaku.
- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 9, 10, 11, 12, 20, 21, 22, 31, 35, 44, 48 (pencatatan baseline, pencatatan waktu Save, menutup modal Changelog, pemulihan Preferences antar-TC lewat seed). Baseline dicatat ulang sebelum pemicu tiap TC (S-12).
- Urutan baca log: jumlah baris dibuktikan bertambah dari baseline lebih dulu, baru baris teratas dibaca (S-14). Jumlah langkah nominal 48; blok baca-log berpola (buka surface, `Verifikasi` jumlah, `Verifikasi` kolom log) pada langkah 6 sampai 8, 17 sampai 19, 28 sampai 34, 41 sampai 47 tidak dihitung ke ambang ~35 langkah (bagian 3 prinsip 13, smell). Seluruh TC berkelas sama (fungsional Save lalu log tiga surface) dan tiap blok berdiri sendiri dengan pemulihan seed di antaranya.
- TC-FA-PREF-389 sampai 391 hanya meminta baris Changelog (dan Activity Log pada TC-FA-PREF-391); baseline yang dicatat hanya surface yang dibaca. Baseline dicatat ulang sebelum Save kedua pada TC-FA-PREF-391 (N_cl_2 dan N_al_2) dan sebelum pemicu tiap TC (S-12). Sesudah langkah 34, Preferences dibuka kembali sebagai langkah navigasi ke modul asal (S-14).
- TC-FA-PREF-390: seed Journal Grouping kosong pada awal TC adalah precondition TC yang eksplisit dan tidak diasersi.
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Expected TC menyebut baris log baru sebagai "tepat N baris baru" tanpa menyebut baseline; spec mencatat baseline jumlah baris tiap surface sebelum aksi lewat kemampuan baca BE dan mengasersi selisih (S-12, S-14).
  - Post Condition TC 389 sampai 391 tidak punya langkah observasi sendiri di TC; padanannya ada pada Expected yang diasersi (S-01). Post Condition "Nilai terbaru dibaca oleh ... (belum disusun)" tidak diasersi karena modul konsumen belum disusun.
  - Expected b TC-FA-PREF-391 menulis nilai tampilan "7.500.000,25" untuk input dan "7.500.000,5" untuk log; spec mengikuti TC persis. Alasan "satu digit desimal tetap satu digit" pada log tidak punya padanan di Precondition selain Catatan TC (format angka).

---
id: TC-FA-PREF-E2E-121-log-tiga-surface-save-default-loss-dan-disposal-documents-sell
title: "Log Tiga Surface: Save Default Loss on Disposal dan Disposal Documents Sell"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-368
  - TC-FA-PREF-369
coverage:
  web: automated
---

# Log Tiga Surface: Save Default Loss on Disposal dan Disposal Documents Sell

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth, entitas Active) seri PC (PC-1): modul akuntansi aktif; Preferences bernilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents Sell/Scrap/Lost/Donate/Trade-in/Write-off Optional, Journal Grouping Group); bulan berjalan Oktober 2026. Untuk TC-FA-PREF-368: Default Loss on Disposal tersimpan kosong; hanya Asset Class IT Equipment yang mengosongkan akun Loss (PC-6); tiga pelepasan belum diposting (PC-7); akun 5-9100 – Rugi Pelepasan Aset Active (PC-5).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): Seed dan pemulihan lewat API (Preferences ke nilai awal PC-1, Asset Class, akun Chart of Accounts, pelepasan, kunci periode, status company) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`). Pembacaan jumlah baris Changelog Preferences, System Log milik pelaku, dan Activity Log FAMS sebelum aksi lewat kemampuan baca BE (disediakan tim FE/BE; 8b.10, S-12). Jam server dan jam browser sinkron untuk asersi "Date = waktu Save" dengan toleransi satu menit (S-12).
- State yang diubah spec: Preferences company dan entri log (audit trail permanen, tidak dihapus). Preferences dipulihkan ke nilai awal PC-1 lewat seed di antara TC dan di hook `after` (hook tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-368: Save perubahan Default Loss on Disposal tercatat di tiga surface

1. Catat jumlah baris awal Changelog Preferences (N_cl), System Log milik Rina Anggraini (N_sl), dan Activity Log FAMS (N_al) lewat kemampuan baca BE
2. Pilih "5-9100 – Rugi Pelepasan Aset" pada Select Default Loss on Disposal
3. Klik [Save changes]
4. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "1 asset class uses the default account. 3 unposted disposals will use the new account." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
5. Klik [Save] pada dialog Save Changes
6. Verifikasi toast "Success, accounting preferences have been saved." tampil
7. Verifikasi form Preferences tetap terbuka dengan nilai tersimpan
8. Catat waktu Save (jam server dan jam browser sinkron)
9. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
10. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
11. Verifikasi baris baru di posisi teratas modal Changelog: Preferences: Date = waktu Save (toleransi satu menit), Action = Edit, Section = Disposal, Field = Default Loss on Disposal, Old Value = —, New Value = 5-9100 – Rugi Pelepasan Aset, Modified By = Rina A
12. Tutup modal Changelog
13. Buka Global Settings > User > Detail > Tab System Log milik Rina Anggraini
14. Verifikasi jumlah baris System Log bertambah tepat 1 dari N_sl
15. Verifikasi baris baru di posisi teratas System Log: Action = Edit, Object = Preferences, Name = —, Field = Default Loss on Disposal, Old Value = —, New Value = 5-9100 – Rugi Pelepasan Aset
16. Verifikasi header tabel System Log tidak memuat kolom Modified By
17. Buka Activity Log FAMS
18. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 1 dari N_al
19. Verifikasi baris baru di posisi teratas Activity Log FAMS: Action = Edit, Object = Preferences, Name = —, Field = Default Loss on Disposal, Old Value = —, New Value = 5-9100 – Rugi Pelepasan Aset, Modified By = Rina A
20. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan, lalu buka Settings > Accounting > Preferences

### TC-FA-PREF-369: Save perubahan Disposal Documents — Sell tercatat di tiga surface

21. Catat jumlah baris awal Changelog Preferences (N_cl), System Log milik Rina Anggraini (N_sl), dan Activity Log FAMS (N_al) lewat kemampuan baca BE
22. Pilih "Required" pada Select Disposal Documents jenis Sell
23. Klik [Save changes]
24. Verifikasi toast "Success, accounting preferences have been saved." tampil
25. Verifikasi form Preferences tetap terbuka dengan nilai tersimpan
26. Catat waktu Save (jam server dan jam browser sinkron)
27. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
28. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
29. Verifikasi baris baru di posisi teratas modal Changelog: Preferences: Date = waktu Save (toleransi satu menit), Action = Edit, Section = Disposal, Field = Disposal Documents — Sell, Old Value = Optional, New Value = Required, Modified By = Rina A
30. Tutup modal Changelog
31. Buka Global Settings > User > Detail > Tab System Log milik Rina Anggraini
32. Verifikasi jumlah baris System Log bertambah tepat 1 dari N_sl
33. Verifikasi baris baru di posisi teratas System Log: Action = Edit, Object = Preferences, Name = —, Field = Disposal Documents — Sell, Old Value = Optional, New Value = Required
34. Verifikasi header tabel System Log tidak memuat kolom Modified By
35. Buka Activity Log FAMS
36. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 1 dari N_al
37. Verifikasi baris baru di posisi teratas Activity Log FAMS: Action = Edit, Object = Preferences, Name = —, Field = Disposal Documents — Sell, Old Value = Optional, New Value = Required, Modified By = Rina A
38. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan

## Notes

- Kelas fungsional: tiap TC menyimpan Preferences lewat UI lalu membaca tiga surface log. Asersi "tepat N baris baru" adalah asersi jumlah terhadap baseline (bukan absence kelas g); S-05 tidak berlaku.
- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 8, 12, 20, 21, 26, 30, 38 (pencatatan baseline, pencatatan waktu Save, menutup modal Changelog, pemulihan Preferences antar-TC lewat seed). Baseline dicatat ulang sebelum pemicu tiap TC (S-12).
- Urutan baca log: jumlah baris dibuktikan bertambah dari baseline lebih dulu, baru baris teratas dibaca (S-14). Jumlah langkah nominal 38; blok baca-log berpola (buka surface, `Verifikasi` jumlah, `Verifikasi` kolom log) pada langkah 9 sampai 19, 27 sampai 37 tidak dihitung ke ambang ~35 langkah (bagian 3 prinsip 13, smell). Seluruh TC berkelas sama (fungsional Save lalu log tiga surface) dan tiap blok berdiri sendiri dengan pemulihan seed di antaranya.
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Expected TC menyebut baris log baru sebagai "tepat N baris baru" tanpa menyebut baseline; spec mencatat baseline jumlah baris tiap surface sebelum aksi lewat kemampuan baca BE dan mengasersi selisih (S-12, S-14).
  - Post Condition TC 368 dan 369 tidak punya langkah observasi sendiri di TC; padanannya ada pada Expected yang diasersi (S-01). Post Condition "Nilai terbaru dibaca oleh ... (belum disusun)" tidak diasersi karena modul konsumen belum disusun.

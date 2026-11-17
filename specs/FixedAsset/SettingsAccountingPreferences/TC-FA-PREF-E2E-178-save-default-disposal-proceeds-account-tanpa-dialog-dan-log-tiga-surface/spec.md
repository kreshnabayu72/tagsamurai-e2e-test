---
id: TC-FA-PREF-E2E-178-save-default-disposal-proceeds-account-tanpa-dialog-dan-log-tiga-surface
title: "Save Default Disposal Proceeds Account (SET-13): langsung tersimpan tanpa dialog dan tercatat di Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-625
  - TC-FA-PREF-626
sourceRules: ["F-FAPREF-01.k22a", "FAPREF-LOGIC-10j", "F-FAPREF-01.k22b", "T-01", "§3.1#b6", "ST-01", "L-02a", "L-02e", "§8#b1", "L-02h", "L-02i", "§4.1.4#r7", "L-02b", "§8.2#r1", "§8.2#p2", "§8.2#p1", "L-02c", "L-02d", "§8.3#p1"]
smoke: []
dependsOn: []
trace:
  "F-FAPREF-01.k22a": 5
  "FAPREF-LOGIC-10j": 5
  "F-FAPREF-01.k22b": [6, 13]
  "T-01": [6, 13]
  "§3.1#b6": 7
  "ST-01": 8
  "L-02a": 15
  "L-02e": 15
  "§8#b1": 16
  "L-02h": 16
  "L-02i": 16
  "§4.1.4#r7": 16
  "L-02b": 19
  "§8.2#r1": 20
  "§8.2#p2": 20
  "§8.2#p1": 21
  "L-02c": [23, 24]
  "L-02d": 24
  "§8.3#p1": 24
coverage:
  web: automated
---

# Save Default Disposal Proceeds Account (SET-13): langsung tersimpan tanpa dialog dan tercatat di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC; kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: seri PC (TC-FA-PREF-362-631), company `PT Contoh Konstruksi` plan Growth (PC-1): seluruh setting tersimpan pada nilai awal (Default Disposal Proceeds Account kosong), belum ada posting penyusutan, semua periode Open. Chart of Accounts PC-22: akun Active `1-3100 – Kliring Hasil Pelepasan` ber-function Disposal Proceeds.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat API (butir "Seed dan pemulihan lewat API" di `suite.md`). Pembacaan jumlah baris Changelog Preferences, System Log milik pelaku, dan Activity Log FAMS sebelum aksi lewat kemampuan baca BE (8b.10, S-12).
- State yang diubah spec: Preferences company dan entri log (audit trail permanen, tidak dihapus). Preferences dipulihkan ke nilai awal PC-1 lewat seed di antara TC dan di hook `after` (hook tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-625: Save hanya mengubah Default Disposal Proceeds Account langsung tersimpan tanpa dialog

1. Seed company ke seri PC (Preferences PC-1 dan Chart of Accounts PC-22) lewat API hingga tersimpan
2. Buka ulang Fixed Asset > Settings > Accounting > Preferences
3. Pilih "1-3100 – Kliring Hasil Pelepasan" pada Select Default Disposal Proceeds Account
4. Klik [Save changes]
5. Verifikasi dialog Save Changes tidak tampil
6. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
7. Verifikasi form tetap terbuka dengan Select Default Disposal Proceeds Account menampilkan "1-3100 – Kliring Hasil Pelepasan"
8. Verifikasi [Save changes] dan [Cancel] berstatus Disabled
9. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan, lalu buka ulang Settings > Accounting > Preferences

### TC-FA-PREF-626: Save perubahan Default Disposal Proceeds Account tercatat di Changelog, System Log, dan Activity Log

10. Catat jumlah baris awal Changelog Preferences (N_cl), System Log milik Rina Anggraini (N_sl), dan Activity Log FAMS (N_al) lewat kemampuan baca BE
11. Pilih "1-3100 – Kliring Hasil Pelepasan" pada Select Default Disposal Proceeds Account
12. Klik [Save changes]
13. Verifikasi toast "Success, accounting preferences have been saved." tampil
14. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
15. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
16. Verifikasi baris baru di posisi teratas modal Changelog: Preferences: Action = Edit, Section = Disposal, Field = Default Disposal Proceeds Account, Old Value = —, New Value = 1-3100 – Kliring Hasil Pelepasan, Modified By = Rina A
17. Tutup modal Changelog
18. Buka Global Settings > User > Detail > Tab System Log milik Rina Anggraini
19. Verifikasi jumlah baris System Log bertambah tepat 1 dari N_sl
20. Verifikasi baris baru di posisi teratas System Log: Action = Edit, Object = Preferences, Name = —, Field = Default Disposal Proceeds Account, Old Value = —, New Value = 1-3100 – Kliring Hasil Pelepasan
21. Verifikasi header tabel System Log tidak memuat kolom Modified By
22. Buka Activity Log FAMS
23. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 1 dari N_al
24. Verifikasi baris baru di posisi teratas Activity Log FAMS: Action = Edit, Object = Preferences, Name = —, Field = Default Disposal Proceeds Account, Old Value = —, New Value = 1-3100 – Kliring Hasil Pelepasan, Modified By = Rina A
25. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah TC-FA-PREF-625 dan 626 mengandaikan halaman Preferences terbuka; layar dibuka ulang pada langkah 2 sesudah seed seri PC.
- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 2, 9, 10, 17, 25 (seed seri PC, membuka ulang halaman, pencatatan baseline, menutup modal Changelog, pemulihan Preferences). Baseline dicatat sebelum pemicu TC (S-12).
- Urutan baca log: jumlah baris dibuktikan bertambah dari baseline lebih dulu, baru baris teratas dibaca (S-14). Asersi "tepat 1 baris baru" adalah asersi jumlah terhadap baseline (bukan absence kelas g); S-05 tidak berlaku.
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC; spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - TC-FA-PREF-626 Expected b tidak menyebut kolom Date baris Changelog; spec tidak mengasersi Date (berbeda dengan TC-FA-PREF-376).
  - Expected TC menyebut baris log baru sebagai "tepat 1 baris baru" tanpa menyebut baseline; spec mencatat baseline jumlah baris tiap surface sebelum aksi lewat kemampuan baca BE dan mengasersi selisih (S-12, S-14).
  - TC-FA-PREF-625 Expected c memuat tiga klausa ("form tetap terbuka", "Select menampilkan nilai", "[Save changes] dan [Cancel] Disabled"); langkah 7 menggabungkan dua klausa pertama sesuai kalimat TC dan langkah 8 memisahkan klausa ketiga.
  - Post Condition TC-FA-PREF-625 dan 626 padanannya ada pada Expected yang diasersi (S-01); tidak ada asersi terpisah.

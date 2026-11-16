---
id: TC-FA-PREF-E2E-119-log-tiga-surface-save-default-capitalization-threshold-dan-in-service-date-source
title: "Log tiga surface: Save perubahan Default Capitalization Threshold dan In-service Date Source tercatat di Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-364
  - TC-FA-PREF-365
sourceRules: ["D-01", "PV-01", "T-01", "§3.1#b6", "FAPREF-LOGIC-03e", "L-02a", "L-02e", "§4.1.4#r15", "L-02j", "L-02b", "§8.2#p1", "§8.2#p2", "L-02c", "§8.3#p1", "SET-03", "§8#b1", "L-02f"]
smoke: []
dependsOn: []
trace:
  "D-01": 4
  "PV-01": 4
  "T-01": [7, 28]
  "§3.1#b6": [8, 29]
  "FAPREF-LOGIC-03e": 8
  "L-02a": [10, 31]
  "L-02e": [10, 31]
  "§4.1.4#r15": 11
  "L-02j": [11, 18, 22]
  "L-02b": [17, 38]
  "§8.2#p1": [18, 19, 39, 40]
  "§8.2#p2": [18, 39]
  "L-02c": [21, 42]
  "§8.3#p1": [22, 43]
  "SET-03": 32
  "§8#b1": 32
  "L-02f": [32, 39, 43]
coverage:
  web: automated
---

# Log tiga surface: Save perubahan Default Capitalization Threshold dan In-service Date Source tercatat di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PC-8; tampil sebagai Modified By `Rina A`), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PC-1), password `Spectra.env.FA_TC_PASSWORD`. Aktor yang sama membuka System Log milik Rina Anggraini dan Activity Log FAMS. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (password akun Total Control) belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Nama sama dengan spec lain di suite karena TC tidak menyebutnya (lihat Temuan untuk QA). Password tidak ditulis di spec atau fixture.
- Data awal (seed lewat API di hook `before`): Preferences company sesuai PC-1 (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group); belum ada posting penyusutan; periode Mar 2026 sampai Dec 2026 Open; tidak ada transaksi bertanggal; bulan berjalan Oktober 2026. Asset Class sesuai PC-6 (IT Equipment threshold sendiri 2.000.000; Vehicles dan Furniture tanpa threshold sendiri) menjadi dasar angka bullet dialog TC-FA-PREF-364 ("2 asset classes use the default threshold."); disediakan tim FE/BE.
- Baseline jumlah entri Changelog Preferences, System Log milik Rina Anggraini, dan Activity Log FAMS dibaca lewat kemampuan baca BE tepat sebelum aksi pemicu tiap TC (kemampuan disediakan tim FE/BE; audit trail permanen sehingga jumlah absolut tidak diasersi).
- Jam server dan jam browser sinkron; kolom Date entri log dibandingkan dengan waktu yang dicatat sesudah klik `[Save]`, dengan toleransi satu menit (kolom Date berketelitian menit).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); seed ulang Preferences ke PC-1 dijalankan oleh langkah penghubung di antara TC dan oleh hook `after`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-364: Save perubahan Default Capitalization Threshold tercatat di Changelog, System Log, dan Activity Log

1. Catat jumlah entri Changelog Preferences, System Log milik Rina Anggraini, dan Activity Log FAMS sebagai baseline (lewat kemampuan baca BE)
2. Ubah isi CurrencyInput Default Capitalization Threshold menjadi "10000000"
3. Klik `[Save changes]`
4. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default threshold.", lalu pertanyaan "Are you sure you want to save these changes?", tombol `[Cancel]` dan `[Save]`
5. Klik `[Save]` pada dialog Save Changes
6. Catat waktu sesudah Save (untuk asersi kolom Date)
7. Verifikasi toast "Success, accounting preferences have been saved." tampil
8. Verifikasi form tetap terbuka dengan nilai tersimpan "Rp 10.000.000,00" pada Default Capitalization Threshold
9. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
10. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline
11. Verifikasi baris teratas modal Changelog: Date = waktu Save, Action = Edit, Section = Capitalization, Field = Default Capitalization Threshold, Old Value = 5.000.000, New Value = 10.000.000, Modified By = Rina A
12. Tutup modal Changelog lewat `✕`
13. Buka Global Settings > User
14. Ketik Search "Rina Anggraini", tekan Enter
15. Klik Name "Rina Anggraini"
16. Klik Tab System Log
17. Verifikasi jumlah entri System Log milik Rina Anggraini bertambah tepat 1 dari baseline
18. Verifikasi baris teratas System Log: Action = Edit, Object = Preferences, Name = —, Field = Default Capitalization Threshold, Old Value = 5.000.000, New Value = 10.000.000
19. Verifikasi System Log tanpa kolom Modified By
20. Buka Activity Log FAMS
21. Verifikasi jumlah entri Activity Log FAMS bertambah tepat 1 dari baseline
22. Verifikasi baris teratas Activity Log FAMS: Action = Edit, Object = Preferences, Name = —, Field = Default Capitalization Threshold, Old Value = 5.000.000, New Value = 10.000.000, Modified By = Rina A
23. Seed ulang Preferences ke PC-1 lewat API, lalu buka ulang Fixed Asset > Settings > Accounting > Preferences

### TC-FA-PREF-365: Save perubahan In-service Date Source tercatat di Changelog, System Log, dan Activity Log

24. Catat jumlah entri Changelog Preferences, System Log milik Rina Anggraini, dan Activity Log FAMS sebagai baseline (lewat kemampuan baca BE)
25. Pilih "Manual by Accounting" pada Select In-service Date Source
26. Klik `[Save changes]`
27. Catat waktu sesudah Save (untuk asersi kolom Date)
28. Verifikasi toast "Success, accounting preferences have been saved." tampil
29. Verifikasi form tetap terbuka dengan nilai tersimpan "Manual by Accounting" pada Select In-service Date Source
30. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
31. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline
32. Verifikasi baris teratas modal Changelog: Date = waktu Save, Action = Edit, Section = Capitalization, Field = In-service Date Source, Old Value = Activation date, New Value = Manual by Accounting, Modified By = Rina A
33. Tutup modal Changelog lewat `✕`
34. Buka Global Settings > User
35. Ketik Search "Rina Anggraini", tekan Enter
36. Klik Name "Rina Anggraini"
37. Klik Tab System Log
38. Verifikasi jumlah entri System Log milik Rina Anggraini bertambah tepat 1 dari baseline
39. Verifikasi baris teratas System Log: Action = Edit, Object = Preferences, Name = —, Field = In-service Date Source, Old Value = Activation date, New Value = Manual by Accounting
40. Verifikasi System Log tanpa kolom Modified By
41. Buka Activity Log FAMS
42. Verifikasi jumlah entri Activity Log FAMS bertambah tepat 1 dari baseline
43. Verifikasi baris teratas Activity Log FAMS: Action = Edit, Object = Preferences, Name = —, Field = In-service Date Source, Old Value = Activation date, New Value = Manual by Accounting, Modified By = Rina A

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): "Seed ulang Preferences ke PC-1 lewat API, lalu buka ulang Fixed Asset > Settings > Accounting > Preferences" memulihkan Preferences setelah TC-FA-PREF-364 (S-09, R-08); Preferences setelah TC-FA-PREF-365 dipulihkan oleh hook `after`.
- Blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) tidak dihitung dalam ambang sekitar 35 langkah (bagian 3 prinsip 13, smell).
- Baseline dicatat ulang sebelum aksi pemicu tiap TC (S-12). Entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih jumlah dari baseline dibuktikan (S-14). Langkah "Ketik Search ... Klik Name" pada Global Settings > User memenuhi 8b.12 dan R-23, dan Search itu tidak perlu dibersihkan karena spec berpindah surface.
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-364 dan 365; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - Post Condition b dan c ("tercatat satu entri ... dalam transaksi Save yang sama", "nilai terbaru dibaca oleh ...") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01); keduanya tidak diklaim teruji.
  - TC-FA-PREF-364 Expected b menyebut "form tetap terbuka dengan nilai tersimpan" tanpa format tampil nilai; spec memakai format "Rp 10.000.000,00" yang sama dengan spec lain di suite (CurrencyInput setelah blur).
  - TC-FA-PREF-365 Post Condition c ("Detail aset dan Depreciation Run (belum disusun)") merujuk modul yang belum disusun dan tidak diasersi.
  - Langkah "Buka Activity Log FAMS" dan "Buka Global Settings > User > Detail > Tab System Log milik Rina Anggraini" tidak menyebut jalur menu; spec menuliskan navigasi Global Settings > User, Search, Name, Tab System Log, dan mengikuti teks TC untuk Activity Log FAMS.

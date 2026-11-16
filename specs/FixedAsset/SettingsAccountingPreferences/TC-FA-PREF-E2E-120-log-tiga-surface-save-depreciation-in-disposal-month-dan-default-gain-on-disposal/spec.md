---
id: TC-FA-PREF-E2E-120-log-tiga-surface-save-depreciation-in-disposal-month-dan-default-gain-on-disposal
title: "Log tiga surface: Save perubahan Depreciation in Disposal Month dan Default Gain on Disposal tercatat di Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-366
  - TC-FA-PREF-367
sourceRules: ["D-01", "PV-03", "T-01", "§3.1#b6", "L-02a", "L-02e", "SET-04", "L-02f", "L-02b", "§8.2#p1", "§8.2#p2", "L-02c", "§8.3#p1", "PV-02", "§4.1.1#p4", "§4.1.4#r12", "L-02i"]
smoke: []
dependsOn: []
trace:
  "D-01": [4, 28]
  "PV-03": 4
  "T-01": [7, 31]
  "§3.1#b6": [8, 32]
  "L-02a": [10, 34]
  "L-02e": [10, 34]
  "SET-04": 11
  "L-02f": [11, 18, 22]
  "L-02b": [17, 41]
  "§8.2#p1": [18, 19, 42, 43]
  "§8.2#p2": [18, 42]
  "L-02c": [21, 45]
  "§8.3#p1": [22, 46]
  "PV-02": 28
  "§4.1.1#p4": 32
  "§4.1.4#r12": 35
  "L-02i": [35, 42, 46]
coverage:
  web: automated
---

# Log tiga surface: Save perubahan Depreciation in Disposal Month dan Default Gain on Disposal tercatat di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PC-8; tampil sebagai Modified By `Rina A`), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PC-1), password `Spectra.env.FA_TC_PASSWORD`. Aktor yang sama membuka System Log milik Rina Anggraini dan Activity Log FAMS. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (password akun Total Control) belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Nama sama dengan spec lain di suite karena TC tidak menyebutnya (lihat Temuan untuk QA). Password tidak ditulis di spec atau fixture.
- Data awal (seed lewat API di hook `before`): Preferences company sesuai PC-1 (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group); belum ada posting penyusutan; periode Mar 2026 sampai Dec 2026 Open; tidak ada transaksi bertanggal; bulan berjalan Oktober 2026. Tiga transaksi pelepasan belum diposting (PC-7) menjadi dasar angka bullet dialog; disediakan tim FE/BE karena modul Disposal belum disusun.
- Data blok TC-FA-PREF-367 (seed lewat API oleh langkah penghubung sebelum blok itu): Default Gain on Disposal tersimpan 4-9100 – Laba Pelepasan Aset (akun Chart of Accounts PC-5); Asset Class sesuai PC-6 (IT Equipment dan Vehicles mengosongkan akun Gain) menjadi dasar bullet "2 asset classes use the default account."; tiga pelepasan belum diposting (PC-7) menjadi dasar bullet "3 unposted disposals will use the new account."; disediakan tim FE/BE.
- Baseline jumlah entri Changelog Preferences, System Log milik Rina Anggraini, dan Activity Log FAMS dibaca lewat kemampuan baca BE tepat sebelum aksi pemicu tiap TC (kemampuan disediakan tim FE/BE; audit trail permanen sehingga jumlah absolut tidak diasersi).
- Jam server dan jam browser sinkron; kolom Date entri log dibandingkan dengan waktu yang dicatat sesudah klik `[Save]`, dengan toleransi satu menit (kolom Date berketelitian menit).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); seed ulang Preferences ke PC-1 dijalankan oleh langkah penghubung di antara TC dan oleh hook `after`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-366: Save perubahan Depreciation in Disposal Month tercatat di Changelog, System Log, dan Activity Log

1. Catat jumlah entri Changelog Preferences, System Log milik Rina Anggraini, dan Activity Log FAMS sebagai baseline (lewat kemampuan baca BE)
2. Pilih "Including disposal month" pada Select Depreciation in Disposal Month
3. Klik `[Save changes]`
4. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "3 disposals waiting posting are affected.", lalu pertanyaan "Are you sure you want to save these changes?", tombol `[Cancel]` dan `[Save]`
5. Klik `[Save]` pada dialog Save Changes
6. Catat waktu sesudah Save (untuk asersi kolom Date)
7. Verifikasi toast "Success, accounting preferences have been saved." tampil
8. Verifikasi form tetap terbuka dengan nilai tersimpan "Including disposal month" pada Select Depreciation in Disposal Month
9. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
10. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline
11. Verifikasi baris teratas modal Changelog: Date = waktu Save, Action = Edit, Section = Depreciation, Field = Depreciation in Disposal Month, Old Value = Up to previous month, New Value = Including disposal month, Modified By = Rina A
12. Tutup modal Changelog lewat `✕`
13. Buka Global Settings > User
14. Ketik Search "Rina Anggraini", tekan Enter
15. Klik Name "Rina Anggraini"
16. Klik Tab System Log
17. Verifikasi jumlah entri System Log milik Rina Anggraini bertambah tepat 1 dari baseline
18. Verifikasi baris teratas System Log: Action = Edit, Object = Preferences, Name = —, Field = Depreciation in Disposal Month, Old Value = Up to previous month, New Value = Including disposal month
19. Verifikasi System Log tanpa kolom Modified By
20. Buka Activity Log FAMS
21. Verifikasi jumlah entri Activity Log FAMS bertambah tepat 1 dari baseline
22. Verifikasi baris teratas Activity Log FAMS: Action = Edit, Object = Preferences, Name = —, Field = Depreciation in Disposal Month, Old Value = Up to previous month, New Value = Including disposal month, Modified By = Rina A
23. Seed ulang Preferences ke PC-1 lewat API, lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
24. Seed Default Gain on Disposal = 4-9100 – Laba Pelepasan Aset lewat API (precondition TC-FA-PREF-367), lalu buka ulang Fixed Asset > Settings > Accounting > Preferences

### TC-FA-PREF-367: Save perubahan Default Gain on Disposal tercatat di Changelog, System Log, dan Activity Log

25. Catat jumlah entri Changelog Preferences, System Log milik Rina Anggraini, dan Activity Log FAMS sebagai baseline (lewat kemampuan baca BE)
26. Kosongkan Select Default Gain on Disposal hingga placeholder "Select account" tampil
27. Klik `[Save changes]`
28. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default account. 3 unposted disposals will use the new account." lalu pertanyaan "Are you sure you want to save these changes?", tombol `[Cancel]` dan `[Save]`
29. Klik `[Save]` pada dialog Save Changes
30. Catat waktu sesudah Save (untuk asersi kolom Date)
31. Verifikasi toast "Success, accounting preferences have been saved." tampil
32. Verifikasi form tetap terbuka dengan nilai tersimpan (Select Default Gain on Disposal kosong dengan placeholder "Select account")
33. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
34. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline
35. Verifikasi baris teratas modal Changelog: Date = waktu Save, Action = Edit, Section = Disposal, Field = Default Gain on Disposal, Old Value = 4-9100 – Laba Pelepasan Aset, New Value = —, Modified By = Rina A
36. Tutup modal Changelog lewat `✕`
37. Buka Global Settings > User
38. Ketik Search "Rina Anggraini", tekan Enter
39. Klik Name "Rina Anggraini"
40. Klik Tab System Log
41. Verifikasi jumlah entri System Log milik Rina Anggraini bertambah tepat 1 dari baseline
42. Verifikasi baris teratas System Log: Action = Edit, Object = Preferences, Name = —, Field = Default Gain on Disposal, Old Value = 4-9100 – Laba Pelepasan Aset, New Value = —
43. Verifikasi System Log tanpa kolom Modified By
44. Buka Activity Log FAMS
45. Verifikasi jumlah entri Activity Log FAMS bertambah tepat 1 dari baseline
46. Verifikasi baris teratas Activity Log FAMS: Action = Edit, Object = Preferences, Name = —, Field = Default Gain on Disposal, Old Value = 4-9100 – Laba Pelepasan Aset, New Value = —, Modified By = Rina A

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): "Seed ulang Preferences ke PC-1 lewat API" dan "Seed Default Gain on Disposal = 4-9100 – Laba Pelepasan Aset lewat API" memulihkan dan menyiapkan Preferences antar TC (S-09, R-08); Preferences setelah TC-FA-PREF-367 dipulihkan oleh hook `after`.
- Blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) tidak dihitung dalam ambang sekitar 35 langkah (bagian 3 prinsip 13, smell).
- Baseline dicatat ulang sebelum aksi pemicu tiap TC (S-12). Entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih jumlah dari baseline dibuktikan (S-14). Langkah "Ketik Search ... Klik Name" pada Global Settings > User memenuhi 8b.12 dan R-23, dan Search itu tidak perlu dibersihkan karena spec berpindah surface.
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-366 dan 367; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - Post Condition b dan c ("tercatat satu entri ... dalam transaksi Save yang sama", "nilai terbaru dibaca oleh ...") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01); keduanya tidak diklaim teruji.
  - TC-FA-PREF-367 Precondition menyebut Default Gain tersimpan 4-9100 dengan rujukan PC-1, padahal PC-1 menyatakan Default Gain/Loss on Disposal kosong; spec men-seed nilai itu lewat API sebagai langkah penghubung sebelum TC-FA-PREF-367.
  - TC-FA-PREF-366 dan 367 bergantung pada tiga pelepasan yang menunggu posting (PC-7) yang dibuat lewat seed karena modul Disposal belum disusun; kemampuan seed itu dicatat sebagai kebutuhan tim FE/BE (S-13).
  - Langkah "Buka Activity Log FAMS" dan "Buka Global Settings > User > Detail > Tab System Log milik Rina Anggraini" tidak menyebut jalur menu; spec menuliskan navigasi Global Settings > User, Search, Name, Tab System Log, dan mengikuti teks TC untuk Activity Log FAMS.

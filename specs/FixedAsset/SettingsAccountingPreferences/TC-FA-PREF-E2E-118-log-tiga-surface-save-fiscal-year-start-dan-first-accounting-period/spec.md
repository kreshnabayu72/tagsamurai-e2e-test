---
id: TC-FA-PREF-E2E-118-log-tiga-surface-save-fiscal-year-start-dan-first-accounting-period
title: "Log tiga surface: Save perubahan Fiscal Year Start dan First Accounting Period tercatat di Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-362
  - TC-FA-PREF-363
sourceRules: ["D-01", "PV-04", "PV-05", "T-01", "§3.1#b6", "L-02a", "L-02e", "§4.1.4#r13", "L-02g", "L-02b", "§8.2#p1", "§8.2#p2", "L-02c", "§8.3#p1", "L-02d", "§4.1.4#r14", "L-02l"]
smoke: []
dependsOn: []
trace:
  "D-01": [4, 28]
  "PV-04": [4, 28]
  "PV-05": 4
  "T-01": [7, 31]
  "§3.1#b6": [8, 32]
  "L-02a": [10, 34]
  "L-02e": [10, 34]
  "§4.1.4#r13": 11
  "L-02g": 11
  "L-02b": [17, 41]
  "§8.2#p1": [18, 19, 42, 43]
  "§8.2#p2": [18, 42]
  "L-02c": [21, 45]
  "§8.3#p1": [22, 46]
  "L-02d": 22
  "§4.1.4#r14": 35
  "L-02l": [35, 42, 46]
coverage:
  web: automated
---

# Log tiga surface: Save perubahan Fiscal Year Start dan First Accounting Period tercatat di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PC-8; tampil sebagai Modified By `Rina A`), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PC-1), password `Spectra.env.FA_TC_PASSWORD`. Aktor yang sama membuka System Log milik Rina Anggraini dan Activity Log FAMS. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (password akun Total Control) belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Nama sama dengan spec lain di suite karena TC tidak menyebutnya (lihat Temuan untuk QA). Password tidak ditulis di spec atau fixture.
- Data awal (seed lewat API di hook `before`): Preferences company sesuai PC-1 (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group); belum ada Run Posted; tidak ada transaksi bertanggal; bulan berjalan Oktober 2026. Modal Changelog Preferences, System Log milik Rina Anggraini, dan Activity Log FAMS dipakai apa adanya; entri seed tidak diasersi.
- Baseline jumlah entri Changelog Preferences, System Log milik Rina Anggraini, dan Activity Log FAMS dibaca lewat kemampuan baca BE tepat sebelum aksi pemicu tiap TC (kemampuan disediakan tim FE/BE; audit trail permanen sehingga jumlah absolut tidak diasersi).
- Jam sistem: bulan berjalan Oktober 2026 menurut Time Zone entitas, dasar hitungan "The period calendar will have 13 accounting periods." dan "The period calendar will have 12 accounting periods."; jam server dan browser diatur lewat kendali jam (butir "Kendali jam sistem" di `suite.md`) di hook `before` dan dipulihkan di hook `after` spec ini, lalu disinkronkan; kolom Date entri log dibandingkan dengan waktu yang dicatat sesudah klik `[Save]` pada jam yang sama (langkah 6 dan 30), dengan toleransi satu menit (kolom Date berketelitian menit); entri baru dicari berdasarkan isi (Field dan New Value), bukan posisi teratas, karena jam diatur ke Oktober 2026 dan entri bercap itu tidak dijamin menjadi baris teratas.
- Cara menemukan baris berdasarkan isi pada log berpaginasi: jam diatur ke masa lalu sehingga entri baru tidak dijamin berada di halaman pertama; di modal Changelog pakai Filter Field dan New Value, di System Log dan Activity Log pakai Search, atau telusuri semua halaman hingga baris dengan isi itu ditemukan.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); seed ulang Preferences ke PC-1 dijalankan oleh langkah penghubung di antara TC dan oleh hook `after`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-362: Save perubahan Fiscal Year Start tercatat di Changelog, System Log, dan Activity Log

1. Catat jumlah entri Changelog Preferences, System Log milik Rina Anggraini, dan Activity Log FAMS sebagai baseline (lewat kemampuan baca BE)
2. Pilih "April" pada Select Fiscal Year Start
3. Klik `[Save changes]`
4. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "The period calendar will have 13 accounting periods." dan "Tax year start also follows Fiscal Year Start.", lalu pertanyaan "Are you sure you want to save these changes?", tombol `[Cancel]` dan `[Save]`
5. Klik `[Save]` pada dialog Save Changes
6. Catat waktu sesudah Save (untuk asersi kolom Date)
7. Verifikasi toast "Success, accounting preferences have been saved." tampil
8. Verifikasi form tetap terbuka dengan nilai tersimpan "April" pada Select Fiscal Year Start
9. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
10. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline
11. Verifikasi baris modal Changelog (dicari berdasarkan isi: Field = Fiscal Year Start, New Value = April): Date = waktu Save (langkah 6), Action = Edit, Section = General, Field = Fiscal Year Start, Old Value = January, New Value = April, Modified By = Rina A
12. Tutup modal Changelog lewat `✕`
13. Buka Global Settings > User
14. Ketik Search "Rina Anggraini", tekan Enter
15. Klik Name "Rina Anggraini"
16. Klik Tab System Log
17. Verifikasi jumlah entri System Log milik Rina Anggraini bertambah tepat 1 dari baseline
18. Verifikasi baris System Log (dicari berdasarkan isi: Field = Fiscal Year Start, New Value = April): Action = Edit, Object = Preferences, Name = —, Field = Fiscal Year Start, Old Value = January, New Value = April
19. Verifikasi System Log tanpa kolom Modified By
20. Buka Activity Log FAMS
21. Verifikasi jumlah entri Activity Log FAMS bertambah tepat 1 dari baseline
22. Verifikasi baris Activity Log FAMS (dicari berdasarkan isi: Field = Fiscal Year Start, New Value = April): Action = Edit, Object = Preferences, Name = —, Field = Fiscal Year Start, Old Value = January, New Value = April, Modified By = Rina A
23. Seed ulang Preferences ke PC-1 lewat API, lalu buka ulang Fixed Asset > Settings > Accounting > Preferences

### TC-FA-PREF-363: Save perubahan First Accounting Period tercatat di Changelog, System Log, dan Activity Log

24. Catat jumlah entri Changelog Preferences, System Log milik Rina Anggraini, dan Activity Log FAMS sebagai baseline (lewat kemampuan baca BE)
25. Pilih bulan "January" pada Select bulan First Accounting Period
26. Pilih tahun "2026" pada Select tahun First Accounting Period
27. Klik `[Save changes]`
28. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "The period calendar will have 12 accounting periods.", lalu pertanyaan "Are you sure you want to save these changes?", tombol `[Cancel]` dan `[Save]`
29. Klik `[Save]` pada dialog Save Changes
30. Catat waktu sesudah Save (untuk asersi kolom Date)
31. Verifikasi toast "Success, accounting preferences have been saved." tampil
32. Verifikasi form tetap terbuka dengan nilai tersimpan Jan 2026 pada First Accounting Period
33. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
34. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline
35. Verifikasi baris modal Changelog (dicari berdasarkan isi: Field = First Accounting Period, New Value = Jan 2026): Date = waktu Save (langkah 30), Action = Edit, Section = General, Field = First Accounting Period, Old Value = Mar 2026, New Value = Jan 2026, Modified By = Rina A
36. Tutup modal Changelog lewat `✕`
37. Buka Global Settings > User
38. Ketik Search "Rina Anggraini", tekan Enter
39. Klik Name "Rina Anggraini"
40. Klik Tab System Log
41. Verifikasi jumlah entri System Log milik Rina Anggraini bertambah tepat 1 dari baseline
42. Verifikasi baris System Log (dicari berdasarkan isi: Field = First Accounting Period, New Value = Jan 2026): Action = Edit, Object = Preferences, Name = —, Field = First Accounting Period, Old Value = Mar 2026, New Value = Jan 2026
43. Verifikasi System Log tanpa kolom Modified By
44. Buka Activity Log FAMS
45. Verifikasi jumlah entri Activity Log FAMS bertambah tepat 1 dari baseline
46. Verifikasi baris Activity Log FAMS (dicari berdasarkan isi: Field = First Accounting Period, New Value = Jan 2026): Action = Edit, Object = Preferences, Name = —, Field = First Accounting Period, Old Value = Mar 2026, New Value = Jan 2026, Modified By = Rina A

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): "Seed ulang Preferences ke PC-1 lewat API, lalu buka ulang Fixed Asset > Settings > Accounting > Preferences" memulihkan Preferences setelah TC-FA-PREF-362 (S-09, R-08); Preferences setelah TC-FA-PREF-363 dipulihkan oleh hook `after`.
- Blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) tidak dihitung dalam ambang sekitar 35 langkah (bagian 3 prinsip 13, smell).
- Baseline dicatat ulang sebelum aksi pemicu tiap TC (S-12). Entri baru dicari berdasarkan isi (Field dan New Value hasil aksi spec) setelah selisih jumlah dari baseline dibuktikan, bukan berdasarkan posisi teratas. Alasan: spec ini menggeser jam (Prerequisites), sehingga S-12 (cari berdasarkan isi) diutamakan atas pola baris teratas S-14, karena cap waktu entri tidak dijamin menjadikannya baris teratas. Langkah "Ketik Search ... Klik Name" pada Global Settings > User memenuhi 8b.13 dan R-23, dan Search itu tidak perlu dibersihkan karena spec berpindah surface.
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-362 dan 363; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - Post Condition b dan c ("tercatat satu entri ... dalam transaksi Save yang sama", "nilai terbaru dibaca oleh kalender periode (Derived view) dan Tax Depreciation Class") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01); keduanya tidak diklaim teruji.
  - TC-FA-PREF-362 Expected a menyebut dua bullet baris dampak sedangkan TC-FA-PREF-363 satu; spec menuliskan keduanya sesuai teks TC.
  - Langkah "Buka Activity Log FAMS" dan "Buka Global Settings > User > Detail > Tab System Log milik Rina Anggraini" tidak menyebut jalur menu; spec menuliskan navigasi Global Settings > User, Search, Name, Tab System Log, dan mengikuti teks TC untuk Activity Log FAMS.

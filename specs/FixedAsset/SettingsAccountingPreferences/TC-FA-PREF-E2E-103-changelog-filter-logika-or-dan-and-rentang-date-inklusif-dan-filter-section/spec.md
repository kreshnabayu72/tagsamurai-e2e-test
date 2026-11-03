---
id: TC-FA-PREF-E2E-103-changelog-filter-logika-or-dan-and-rentang-date-inklusif-dan-filter-section
title: "Changelog Filter: logika OR dalam dropdown, AND antar dropdown, rentang Date inklusif, filter Section menyaring baris tanpa Section"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-308
  - TC-FA-PREF-309
  - TC-FA-PREF-310
  - TC-FA-PREF-311
coverage:
  web: automated
---

# Changelog Filter: logika OR dalam dropdown, AND antar dropdown, rentang Date inklusif, filter Section menyaring baris tanpa Section

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4 dan PB-U), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PB-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (password akun Total Control) belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Nama sama dengan spec lain di suite karena TC tidak menyebutnya (lihat Temuan untuk QA). Password tidak ditulis di spec atau fixture.
- Data awal (seed lewat API di hook `before`): Preferences company sesuai PB-1 (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month; periode Mar 2026 sampai Dec 2026 Open). Changelog Preferences berisi 9 entri contoh (PB-C1) sebagai seluruh isi Changelog; seed disediakan tim FE/BE. Baris disebut "baris N" mengikuti nomor berikut (urutan tampil default Newest First; kolom Modified By tampil `Budi S` dan `Rina A`):
  - Baris 1: Date 27/10/26 16:40, Action Edit, Section Chart of Accounts, Field Default Capitalization Offset, Old Value —, New Value 1-2900 – Biaya Dikapitalisasi, Modified By Budi S
  - Baris 2: Date 26/10/26, Action Edit, Section Disposal, Field Disposal Documents — Sell, Old Value Optional, New Value Required, Modified By Rina A
  - Baris 3: Date 26/10/26, Action Edit, Section Disposal, Field Disposal Documents — Scrap, Old Value Optional, New Value Required, Modified By Rina A
  - Baris 4: Date tidak tertulis di TC, Action Edit, Section Journal Export, Field Journal Grouping, Old Value Group, New Value Group, Category, Modified By Budi S
  - Baris 5: Date tidak tertulis di TC, Action Edit, Section Disposal, Field Default Gain on Disposal, Old Value 4-9100 – Laba Pelepasan Aset, New Value —, Modified By Rina A
  - Baris 6: Date 22/10/26 sampai 23/10/26, Action Edit, Section General, Field Fiscal Year Start, Old Value January, New Value April, Modified By Rina A
  - Baris 7: Date 22/10/26 sampai 23/10/26, Action Edit, Section General, Field First Accounting Period, Old Value Mar 2026, New Value Jan 2026, Modified By Rina A
  - Baris 8: Date 22/10/26 sampai 23/10/26, Action Edit, Section Capitalization, Field Default Capitalization Threshold, Old Value 5.000.000, New Value 10.000.000, Modified By Rina A
  - Baris 9: Date 20/10/26 09:12, Action Create, Section —, Field Preferences, Old Value —, New Value Initial values, Modified By Budi S
  - Urutan tulis seed: baris 3 ditulis sebelum baris 2 dan baris 7 sebelum baris 6 pada Date yang sama (tie-break sort).
- Format tanggal General Settings `dd/MM/yy` dengan waktu 24 jam (PB-1).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-308: Dua opsi dalam satu dropdown digabung dengan logika OR

1. Klik ikon View history di header tab Preferences
2. Klik ikon Filter
3. Pilih opsi General dan Capitalization pada dropdown Section
4. Klik `[Apply]`
5. Verifikasi tabel menampilkan baris 6, baris 7, dan baris 8 (Section General atau Capitalization)
6. Verifikasi baris dengan Section lain (baris 1, 2, 3, 4, 5, dan 9) tidak tampil
7. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-PREF-309: Dua dropdown berbeda digabung dengan logika AND

8. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
9. Klik ikon Filter
10. Pilih opsi Edit pada dropdown Action
11. Pilih opsi Budi Santoso pada dropdown Modified By
12. Klik `[Apply]`
13. Verifikasi tabel menampilkan baris 1 dan baris 4 (Action Edit dan Modified By Budi S)
14. Verifikasi baris 9 (Action Create, Modified By Budi S) tidak tampil
15. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-PREF-310: Filter Date menyaring rentang tanggal dengan batas awal dan akhir inklusif

16. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
17. Klik ikon Filter
18. Pada field Date pilih rentang 22/10/26 sampai 23/10/26
19. Klik `[Apply]`
20. Verifikasi tabel menampilkan baris 6, baris 7, dan baris 8
21. Klik ikon Filter, lalu pilih rentang 26/10/26 sampai 26/10/26 dan klik `[Apply]`
22. Verifikasi tabel menampilkan baris 2 dan baris 3
23. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-PREF-311: Memilih opsi Section menyaring keluar baris dengan Section kosong

24. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
25. Klik ikon Filter
26. Pilih seluruh lima opsi pada dropdown Section: Capitalization, Chart of Accounts, Disposal, General, Journal Export
27. Klik `[Apply]`
28. Verifikasi tabel menampilkan baris 1 sampai baris 8
29. Verifikasi baris 9 (Section "—") tidak tampil
30. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Baris seed Changelog disebut "baris N" mengikuti tabel PB-C1 di Prerequisites; Modified By ditulis `Budi S` dan `Rina A` sesuai format kolom (R-14).
- Langkah penghubung (S-03): "Tutup modal Changelog lewat `✕`, lalu klik ikon View history" membuka ulang modal bersih untuk tiap TC; "Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`" di akhir tiap blok mengosongkan filter (S-09).
- Asersi absence baris (langkah 6, 14, 29) didahului Verifikasi baris pembanding yang tampil pada tabel yang sama (8b.2).
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-308 sampai 311; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - Kolom Section baris seed 1 (Chart of Accounts) dan baris 4 (Journal Export) serta Date baris seed 4 dan 5 tidak tertulis eksplisit di TC; Section disimpulkan dari urutan sort TC-FA-PREF-325 dan daftar opsi Section TC-FA-PREF-306.

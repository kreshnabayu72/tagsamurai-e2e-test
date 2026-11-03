---
id: TC-FA-PREF-E2E-102-changelog-filter-panel-screening-sumber-opsi-dan-filter-satu-opsi
title: "Changelog Filter Panel: screening, sumber opsi dropdown, filter satu opsi pada empat dropdown"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-305
  - TC-FA-PREF-306
  - TC-FA-PREF-307
coverage:
  web: automated
---

# Changelog Filter Panel: screening, sumber opsi dropdown, filter satu opsi pada empat dropdown

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

### TC-FA-PREF-305: Screening Filter Panel modal Changelog

1. Klik ikon View history di header tab Preferences
2. Klik ikon Filter pada toolbar modal
3. Verifikasi ikon Filter berubah gelap
4. Verifikasi Filter Panel tampil di bawah toolbar modal
5. Verifikasi Filter Panel memuat field "Date" berupa date range picker dengan placeholder "Select date"
6. Verifikasi Filter Panel memuat field "Action" berupa multi-select searchable dengan placeholder "All actions"
7. Verifikasi Filter Panel memuat field "Section" berupa multi-select searchable dengan placeholder "All sections"
8. Verifikasi Filter Panel memuat field "Field" berupa multi-select searchable dengan placeholder "All fields"
9. Verifikasi Filter Panel memuat field "Modified By" berupa multi-select searchable dengan placeholder "All users"
10. Verifikasi Filter Panel tidak memuat field filter untuk Old Value dan New Value
11. Verifikasi footer panel memuat tombol `[Clear Field]` (kiri, variant text) dan `[Apply]` (kanan, variant filled)

### TC-FA-PREF-306: Opsi dropdown filter bersumber dari data tabel Changelog

12. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
13. Klik ikon Filter
14. Buka dropdown Action
15. Verifikasi dropdown Action memuat dua opsi: Create dan Edit
16. Buka dropdown Section
17. Verifikasi dropdown Section memuat lima opsi: Capitalization, Chart of Accounts, Disposal, General, dan Journal Export
18. Verifikasi dropdown Section tidak memuat opsi untuk nilai kosong "—" dan tidak memuat opsi Depreciation
19. Buka dropdown Field
20. Verifikasi dropdown Field memuat sembilan opsi: Default Capitalization Offset, Default Capitalization Threshold, Default Gain on Disposal, Disposal Documents — Scrap, Disposal Documents — Sell, First Accounting Period, Fiscal Year Start, Journal Grouping, dan Preferences
21. Buka dropdown Modified By
22. Verifikasi dropdown Modified By memuat dua opsi: user Budi Santoso dan user Rina Anggraini

### TC-FA-PREF-307: Filter satu opsi pada empat dropdown menyaring baris sesuai opsi

23. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
24. Klik ikon Filter, pilih opsi Create pada dropdown Action, lalu klik `[Apply]`
25. Verifikasi tabel menampilkan baris 9
26. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
27. Klik ikon Filter, pilih opsi General pada dropdown Section, lalu klik `[Apply]`
28. Verifikasi tabel menampilkan baris 6 lalu baris 7
29. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
30. Klik ikon Filter, pilih opsi Fiscal Year Start pada dropdown Field, lalu klik `[Apply]`
31. Verifikasi tabel menampilkan baris 6
32. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
33. Klik ikon Filter, pilih opsi Budi Santoso pada dropdown Modified By, lalu klik `[Apply]`
34. Verifikasi tabel menampilkan baris 1 lalu baris 4 lalu baris 9
35. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Baris seed Changelog disebut "baris N" mengikuti tabel PB-C1 di Prerequisites; Modified By ditulis `Budi S` dan `Rina A` sesuai format kolom (R-14).
- Langkah penghubung (S-03): "Tutup modal Changelog lewat `✕`, lalu klik ikon View history" membuka ulang modal bersih untuk tiap TC; "Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`" setelah tiap blok TC-FA-PREF-307 mengosongkan filter (S-09).
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-305 sampai 307; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - Kolom Section baris seed 1 (Chart of Accounts) dan baris 4 (Journal Export) serta Date baris seed 4 dan 5 tidak tertulis eksplisit di TC; Section disimpulkan dari urutan sort TC-FA-PREF-325 dan daftar opsi Section TC-FA-PREF-306.

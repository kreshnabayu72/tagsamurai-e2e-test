---
id: TC-FA-PREF-E2E-131-sinkronisasi-accounting-period-save-fiscal-year-start-dan-first-accounting-period-membangun-ulang-periode
title: "Sinkronisasi Kalender Periode (Derived View): Save Fiscal Year Start dan First Accounting Period Mengubah Kalender Tanpa Log Terpisah"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-394
  - TC-FA-PREF-395
sourceRules: ["D-01", "PV-04", "PV-05", "T-01", "FAPREF-LOGIC-02l"]
smoke: []
dependsOn: []
trace:
  "D-01": [4, 15]
  "PV-04": [4, 15]
  "PV-05": [4, 16]
  "T-01": [6, 18]
  "FAPREF-LOGIC-02l": [8, 20]
anchor: [15]
coverage:
  web: automated
---

# Sinkronisasi Kalender Periode (Derived View): Save Fiscal Year Start dan First Accounting Period Mengubah Kalender Tanpa Log Terpisah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth, entitas Active) seri PC (PC-1): modul akuntansi aktif; Preferences bernilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents Sell/Scrap/Lost/Donate/Trade-in/Write-off Optional, Journal Grouping Group); bulan berjalan Oktober 2026. Belum ada Depreciation Run berstatus Posted dan transaksi bertanggal; Tax Depreciation Class hanya versi pertama. Jumlah periode pada dialog (kalender periode, Derived view; tidak disimpan) bergantung bulan berjalan Oktober 2026: jam sistem Oktober 2026 (lihat butir Jam sistem; PC-15 Time Zone Asia/Jakarta).
- Jam sistem: bulan berjalan Oktober 2026 menurut Time Zone entitas; jam server dan browser diatur lewat kendali jam (butir "Kendali jam sistem" di `suite.md`) di hook `before` dan dipulihkan di hook `after` spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): kendali jam sistem (clock); kemampuan baca jumlah baris Changelog Preferences (baseline sebelum aksi, S-12). Seed dan pemulihan lewat API (Preferences ke nilai awal PC-1, Asset Class, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- State yang diubah spec: Preferences company dan baris Changelog Preferences. Preferences dipulihkan ke nilai awal PC-1 lewat seed antar-TC dan di hook `after`; jam sistem dipulihkan di hook `after`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-394: Save Fiscal Year Start mengubah kalender periode tanpa log terpisah

1. Catat jumlah baris modal Changelog: Preferences (baseline)
2. Pilih "July" pada Select Fiscal Year Start
3. Klik [Save changes]
4. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "The period calendar will have 16 accounting periods."; "Tax year start also follows Fiscal Year Start." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
5. Klik [Save] pada dialog Save Changes
6. Verifikasi toast "Success, accounting preferences have been saved." tampil
7. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
8. Verifikasi modal Changelog: Preferences memuat tepat 1 baris baru dibanding baseline langkah 1 (tidak ada baris terpisah untuk kalender periode)
9. Verifikasi baris baru: Field = Fiscal Year Start, Old Value = January, New Value = July
10. Klik ikon [✕] di header modal Changelog
11. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan, lalu buka Settings > Accounting > Preferences

### TC-FA-PREF-395: Save First Accounting Period mengubah kalender periode dari bulan baru tanpa log terpisah

12. Catat jumlah baris modal Changelog: Preferences (baseline)
13. Pilih bulan "January" dan tahun "2026" pada Select First Accounting Period
14. Klik [Save changes]
15. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "The period calendar will have 12 accounting periods." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
16. Verifikasi dialog Save Changes tidak memuat bullet "Tax year start also follows Fiscal Year Start." (PV-05, Fiscal Year Start tidak berubah)
17. Klik [Save] pada dialog Save Changes
18. Verifikasi toast "Success, accounting preferences have been saved." tampil
19. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
20. Verifikasi modal Changelog: Preferences memuat tepat 1 baris baru dibanding baseline langkah 12 (tidak ada baris terpisah untuk kalender periode)
21. Verifikasi baris baru: Field = First Accounting Period, Old Value = Mar 2026, New Value = Jan 2026
22. Klik ikon [✕] di header modal Changelog
23. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan

## Notes

- Kelas fungsional: Save atau perubahan state pelaku kedua, lalu pembacaan modul konsumen (Asset Class, Tax Depreciation Class, Accounting Period, Chart of Accounts, Changelog). Tidak ada asersi absence log (kelas g).
- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 10, 11, 22, 23 (menutup modal Changelog dan pemulihan state antar-TC). Langkah 1 dan 12 adalah baseline jumlah baris Changelog (S-12), tambahan di luar langkah TC.
- Kalender periode adalah Derived view dari Fiscal Year Start dan First Accounting Period (FAPREF-LOGIC-02p); tidak ada halaman atau tabel periode tersimpan, sehingga isi kalender (Post Condition b TC-394 dan 395) tidak diasersi lewat UI.
- Pada TC-FA-PREF-395, PV-05 tidak tampil karena Fiscal Year Start tidak berubah; asersi absence bullet itu didahului `Verifikasi` dialog dengan bullet pertama tampil (anchor positif, 8b butir 2; langkah 15).
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Post Condition TC-FA-PREF-394 dan 395 butir b (kalender periode Derived view: Mar 2026 sampai Jun 2027 dengan tahun fiskal pertama 4 periode; Jan 2026 sampai Dec 2026) tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - Slug id spec ini masih memuat "accounting-period" dan "membangun-ulang-periode" (id mengikuti nama folder; tidak diubah).

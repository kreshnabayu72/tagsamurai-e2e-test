---
id: TC-FA-PREF-E2E-067-kunci-fiscal-year-start-dan-first-accounting-period-setelah-posting-atau-periode-ditutup
title: "Kunci Fiscal Year Start dan First Accounting Period Setelah Posting Penyusutan"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-238
sourceRules: ["FAPREF-LOGIC-02e", "ST-05", "FAPREF-LOGIC-02c", "ST-01"]
smoke: []
dependsOn: []
trace:
  "FAPREF-LOGIC-02e": [2, 3, 6, 7]
  "ST-05": [3, 5, 7, 9]
  "FAPREF-LOGIC-02c": [10]
  "ST-01": [11]
coverage:
  web: automated
---

# Kunci Fiscal Year Start dan First Accounting Period Setelah Posting Penyusutan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; belum ada Run Posted) dan PB-2 (akun Chart of Accounts uji). Varian kunci dibentuk lewat seed API pada awal TC: PB-7a (Depreciation Run berstatus Posted; Last Posted Period terisi pada Asset Class IT Equipment).
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-238: Terkunci setelah posting penyusutan pertama

1. Seed posting penyusutan pertama (PB-7a) lewat API, lalu muat ulang halaman dengan F5
2. Verifikasi Select Fiscal Year Start tetap tampil (visible) menampilkan "January"
3. Verifikasi Select Fiscal Year Start berstatus Disabled dengan ikon gembok
4. Arahkan kursor ke Select Fiscal Year Start
5. Verifikasi tooltip "Fiscal year start is locked because depreciation has been posted. It cannot be changed from this page." tampil pada Select Fiscal Year Start
6. Verifikasi Select bulan dan Select tahun First Accounting Period tetap tampil (visible) menampilkan "March" dan "2026"
7. Verifikasi Select bulan dan Select tahun First Accounting Period berstatus Disabled dengan ikon gembok
8. Arahkan kursor ke Select bulan First Accounting Period
9. Verifikasi tooltip "First accounting period is locked because depreciation has been posted. It cannot be changed from this page." tampil pada First Accounting Period
10. Verifikasi CurrencyInput Default Capitalization Threshold dan Select In-service Date Source berstatus Enabled
11. Verifikasi [Save changes] dan [Cancel] berstatus Disabled karena form pristine

### Pemulihan

12. Pulihkan kunci dan Preferences ke PB-1 lewat seed API

## Notes

- Langkah penghubung (S-03): seed kunci tiap TC dan muat ulang. Hook `after` memulihkan kunci ke PB-1 lewat seed API.
- Urutan Verifikasi mengikuti urutan state (bagian 8b butir 5): tampil dan Disabled, hover, tooltip.
- Temuan untuk QA:
  - Post Condition "Preferences company belum berubah ..." tidak punya langkah observasi di TC ini, sehingga tidak diasersi (S-01).

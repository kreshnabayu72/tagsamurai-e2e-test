---
id: TC-FA-PREF-E2E-071-v09-v10-v04-tampil-bersamaan-saat-tidak-terkunci
title: "V-09, V-10, V-04 Tampil Bersamaan Saat Tidak Terkunci"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-257
sourceRules: ["F-FAPREF-01.k4c", "F-FAPREF-01.k23", "V-09", "FAPREF-LOGIC-02k", "V-10", "FAPREF-LOGIC-02n", "V-04", "D-03", "§6#p2"]
smoke: []
dependsOn: []
trace:
  "F-FAPREF-01.k4c": [8, 9, 12]
  "F-FAPREF-01.k23": 9
  "V-09": 10
  "FAPREF-LOGIC-02k": 10
  "V-10": 11
  "FAPREF-LOGIC-02n": 11
  "V-04": 12
  "D-03": 13
  "§6#p2": 13
coverage:
  web: automated
---

# V-09, V-10, V-04 Tampil Bersamaan Saat Tidak Terkunci

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; periode Mar 2026 sampai Dec 2026 Open; belum ada penyusutan diposting) dan PB-2 (akun Chart of Accounts uji). PB-8 (Tax Depreciation Class `Commercial Building` dengan versi kedua Effective From 01/07/26) dan PB-9 (transaksi aktivasi aset bertanggal 15/05/26). Fiscal Year Start dan First Accounting Period tidak terkunci.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Sesi API aktor untuk pemicu perubahan state (fixture BE): kemampuan disediakan tim BE/FE (butir "Sesi API aktor" di `suite.md`).
- Langkah muat ulang saat form dirty: dialog `beforeunload` dikonfirmasi (kemampuan disediakan tim FE; dipakai pada langkah pemulihan).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-257: V-09, V-10, dan V-04 tampil bersamaan pada fieldnya masing-masing

1. Seed PB-8 dan PB-9 lewat API, lalu muat ulang halaman dengan F5
2. Ubah Select Fiscal Year Start dari "January" menjadi "April"
3. Ubah Select bulan First Accounting Period dari "March" menjadi "June"
4. Pilih "4-9100 – Laba Pelepasan Aset" pada Select Default Gain on Disposal
5. Klik [Save changes] sampai dialog D-01 tampil
6. Lewat sesi API (fixture BE), ubah status akun 4-9100 menjadi Inactive hingga status tersimpan
7. Klik [Save] pada dialog D-01
8. Verifikasi dialog D-01 ditutup
9. Verifikasi form tetap memuat seluruh perubahan yang belum disimpan
10. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tampil pada Select Fiscal Year Start
11. Verifikasi caption "First accounting period cannot be later than existing dated transactions." tampil pada First Accounting Period
12. Verifikasi caption "This default gain on disposal no longer exists. Please select another." tampil pada Select Default Gain on Disposal
13. Verifikasi tidak ada dialog D-03 dan tidak ada toast
14. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)
15. Pulihkan akun 4-9100, PB-8, PB-9 dan Preferences ke PB-1 lewat seed API, lalu muat ulang halaman dengan F5

## Notes

- Langkah penghubung (S-03): seed PB-8 dan PB-9, membuang perubahan form dengan F5, dan pemulihan seed. Pemicu akun Inactive lewat sesi API aktor bukan konteks kedua.
- Asersi absence D-03 dan toast didahului Verifikasi tiga caption tampil sebagai anchor. TC-559 ada di spec 164.
- Temuan untuk QA:
  - Post Condition "Preferences company belum berubah ..." tidak punya langkah observasi di TC ini, sehingga tidak diasersi (S-01).

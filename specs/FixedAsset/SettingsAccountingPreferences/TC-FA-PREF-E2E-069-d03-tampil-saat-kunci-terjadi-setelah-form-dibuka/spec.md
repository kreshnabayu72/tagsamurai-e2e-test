---
id: TC-FA-PREF-E2E-069-d03-tampil-saat-kunci-terjadi-setelah-form-dibuka
title: "D-03 Tampil Saat Kunci Terjadi Setelah Form Dibuka (Posting Pertama)"
layer: ui-e2e
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-251
sourceRules: ["D-03", "E-FAPREF-06", "ST-27", "§4.2b#r12"]
smoke: []
dependsOn: []
trace:
  "D-03": [5, 6, 7]
  "E-FAPREF-06": 5
  "ST-27": 8
  "§4.2b#r12": 9
coverage:
  web: automated
---

# D-03 Tampil Saat Kunci Terjadi Setelah Form Dibuka (Posting Pertama)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; belum ada Run Posted) dan PB-2 (akun Chart of Accounts uji). Fiscal Year Start dan First Accounting Period tidak terkunci saat form dibuka.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Sesi API aktor untuk pemicu perubahan state (fixture BE): kemampuan disediakan tim BE/FE (butir "Sesi API aktor" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-251: D-03 tampil saat posting penyusutan pertama terjadi setelah form dibuka

1. Ubah Select Fiscal Year Start dari "January" menjadi "July"
2. Klik [Save changes] sampai dialog D-01 tampil
3. Lewat sesi API (fixture BE), lakukan posting penyusutan pertama (Depreciation Run berstatus Posted) hingga status tersimpan
4. Klik [Save] pada dialog D-01
5. Verifikasi dialog D-03 berjudul "Cannot Save Preferences" tampil
6. Verifikasi body dialog D-03: "Fiscal Year Start and First Accounting Period are locked because depreciation has been posted. The page has been reloaded with the latest lock status."
7. Verifikasi dialog D-03 hanya memuat tombol [OK]
8. Verifikasi tidak ada toast yang tampil bersama D-03
9. Verifikasi dialog D-01 tidak lagi tampil
10. Klik [OK] pada dialog D-03
11. Pulihkan kunci dan Preferences ke PB-1 lewat seed API, lalu muat ulang halaman dengan F5

## Notes

- Langkah penghubung (S-03): klik [OK] pada D-03 dan pemulihan kunci di akhir TC. Pemicu kunci lewat sesi API aktor (fixture BE); dialog D-01 yang tampil menjadi wait eksplisit pada langkah Save changes sebelum pemicu.
- Asersi tidak ada toast pada D-03 didahului Verifikasi D-03 tampil sebagai anchor.
- Temuan untuk QA:
  - Post Condition "Preferences company belum berubah ..." tidak punya langkah observasi di TC ini, sehingga tidak diasersi (S-01).

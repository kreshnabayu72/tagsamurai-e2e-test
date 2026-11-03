---
id: TC-FA-PREF-E2E-022-role-matrix-visibilitas-total-control-default-user-read-only
title: "Role Matrix: Visibilitas dan Kontrol Preferences untuk Total Control, Default User, dan Read Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-96
  - TC-FA-PREF-97
  - TC-FA-PREF-98
coverage:
  web: automated
---

# Role Matrix: Visibilitas dan Kontrol Preferences untuk Total Control, Default User, dan Read Only

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

  | TC | Role | Pre-setup | Email | Env var password |
  |---|---|---|---|---|
  | TC-FA-PREF-96 | Total Control | PA-4 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
  | TC-FA-PREF-97 | Default User | PA-4 | `defaultUserFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` |
  | TC-FA-PREF-98 | Read Only | PA-4 | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
- Login akun aktor pertama (Total Control, company `PT Contoh Konstruksi`, PA-1) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun di tengah spec memakai langkah logout dan login eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Env var `FA_TC_PASSWORD`, `FA_DU_PASSWORD`, dan `FA_RO_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data awal (seed di hook `before`): Preferences company sesuai PA-5 (Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, dan Depreciation in Disposal Month kosong; setting lain bernilai awal) sehingga banner Setup Incomplete tampil untuk ketiga role. Hook `after` memulihkan Preferences ke PA-2.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk ketiga akun.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-96: Total Control

1. Buka Settings > Accounting > Preferences
2. Verifikasi Total Control: Tab "Preferences" tampil (Show) pada tab bar Settings > Accounting
3. Verifikasi Total Control: ikon View history tampil (Show) di header tab
4. Verifikasi Total Control: banner Setup Incomplete tampil (Show), Alert severity danger "Accounting setup is incomplete: Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, Depreciation in Disposal Month. Depreciation and journal export are blocked until completed."
5. Verifikasi Total Control: field form tampil (Show) dan Enabled (dapat diedit)
6. Verifikasi Total Control: `[Save changes]` dan `[Cancel]` tampil (Show)
7. Verifikasi Total Control: `[Save changes]` dan `[Cancel]` Disabled karena form pristine
8. Verifikasi Total Control: shortcut `+ Create account` tampil (Show) pada Select Default Gain on Disposal dan Default Loss on Disposal

### TC-FA-PREF-97: Default User

9. Logout dari akun Total Control
10. Login sebagai Default User (`defaultUserFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_DU_PASSWORD`)
11. Buka Settings > Accounting > Preferences
12. Verifikasi Default User: Tab "Preferences" tampil (Show) pada tab bar Settings > Accounting
13. Verifikasi Default User: ikon View history tampil (Show) di header tab
14. Verifikasi Default User: banner Setup Incomplete tampil (Show), Alert severity danger "Accounting setup is incomplete: Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, Depreciation in Disposal Month. Depreciation and journal export are blocked until completed."
15. Verifikasi Default User: field form tampil (Show) dan Enabled (dapat diedit)
16. Verifikasi Default User: `[Save changes]` dan `[Cancel]` tampil (Show)
17. Verifikasi Default User: `[Save changes]` dan `[Cancel]` Disabled karena form pristine
18. Verifikasi Default User: shortcut `+ Create account` tampil (Show) pada Select Default Gain on Disposal dan Default Loss on Disposal

### TC-FA-PREF-98: Read Only

19. Logout dari akun Default User
20. Login sebagai Read Only (`readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_RO_PASSWORD`)
21. Buka Settings > Accounting > Preferences
22. Verifikasi Read Only: Tab "Preferences" tampil (Show) pada tab bar Settings > Accounting
23. Verifikasi Read Only: ikon View history tampil (Show) di header tab
24. Verifikasi Read Only: banner Setup Incomplete tampil (Show), Alert severity danger "Accounting setup is incomplete: Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, Depreciation in Disposal Month. Depreciation and journal export are blocked until completed."
25. Hover Select In-service Date Source
26. Verifikasi Read Only: seluruh field form tetap tampil namun Disabled dengan tooltip "You don't have permission to edit."
27. Verifikasi Read Only: `[Save changes]` dan `[Cancel]` Hidden (tidak dirender)
28. Verifikasi Read Only: shortcut `+ Create account` Hidden (tidak dirender)

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Role Matrix (bagian 3a): matriks visibilitas, satu daftar elemen untuk banyak role dengan hasil berbeda (Show dan Hidden), sehingga memuat dua polaritas. Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`, S-07).
- Langkah penghubung (S-03): pasangan logout dan login di awal blok TC-FA-PREF-97 dan TC-FA-PREF-98 (langkah 9, 10, 19, 20). Langkah 1, 11, dan 21 membuka Settings > Accounting > Preferences sesuai Langkah Uji TC.
- Absence Hidden (langkah 27 dan 28) memakai tab Preferences dan banner yang sudah termuat sebagai anchor permukaan (8b butir 2).
- Temuan untuk QA:
  - TC-FA-PREF-98 Expected butir d tidak menyebut field mana yang di-hover; spec memakai Select In-service Date Source mengikuti TC-FA-PREF-229.
  - TC-FA-PREF-96, 97, dan 98 tidak menyebut nama env var password; nama `FA_TC_PASSWORD`, `FA_DU_PASSWORD`, dan `FA_RO_PASSWORD` diusulkan spec dan perlu keputusan tim.

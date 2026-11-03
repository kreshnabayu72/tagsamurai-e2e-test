---
id: TC-FA-PREF-E2E-023-role-matrix-visibilitas-manage-accounting-read-dan-read-update
title: "Role Matrix: Visibilitas Preferences untuk Manage accounting Read dan Read + Update, termasuk tombol tersembunyi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-99
  - TC-FA-PREF-100
  - TC-FA-PREF-229
  - TC-FA-PREF-561
coverage:
  web: automated
---

# Role Matrix: Visibilitas Preferences untuk Manage accounting Read dan Read + Update, termasuk tombol tersembunyi

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

  | TC | Role | Pre-setup | Email | Env var password |
  |---|---|---|---|---|
  | TC-FA-PREF-99, TC-FA-PREF-229, TC-FA-PREF-561 | Manage accounting - Read | PA-4 | `manageAccountingRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAR_PASSWORD` |
  | TC-FA-PREF-100 | Manage accounting - Read + Update | PA-4 | `manageAccountingReadUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MARU_PASSWORD` |
- Login akun aktor pertama (Manage accounting - Read, company `PT Contoh Konstruksi`, PA-1) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun ke Manage accounting - Read + Update memakai langkah logout dan login eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Env var `FA_MAR_PASSWORD` dan `FA_MARU_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data awal blok TC-FA-PREF-99 (seed di hook `before`): Preferences company sesuai PA-5 (Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, dan Depreciation in Disposal Month kosong; setting lain bernilai awal) sehingga banner Setup Incomplete tampil.
- Data blok TC-FA-PREF-229 (seed lewat API oleh langkah penghubung): Preferences dalam nilai awal PB-1; akun Chart of Accounts tersedia (PB-2). Data blok TC-FA-PREF-561: seluruh setting tersimpan pada nilai awal PC-1; belum ada posting penyusutan, semua periode Open. Data blok TC-FA-PREF-100: PA-5 (seed ulang lewat API sebelum ganti akun). Nilai awal PA-2, PB-1, dan PC-1 setara. Hook `after` memulihkan Preferences ke PA-2.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk kedua akun.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-99: Manage accounting Read, setting dan View history tanpa akses tulis

1. Buka Settings > Accounting > Preferences
2. Verifikasi Manage accounting - Read: Tab "Preferences" tampil (Show) pada tab bar Settings > Accounting
3. Verifikasi Manage accounting - Read: ikon View history tampil (Show) di header tab
4. Verifikasi Manage accounting - Read: banner Setup Incomplete tampil (Show), Alert severity danger "Accounting setup is incomplete: Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, Depreciation in Disposal Month. Depreciation and journal export are blocked until completed."
5. Hover Select In-service Date Source
6. Verifikasi Manage accounting - Read: seluruh field form tetap tampil namun Disabled dengan tooltip "You don't have permission to edit."
7. Verifikasi Manage accounting - Read: `[Save changes]` dan `[Cancel]` Hidden (tidak dirender)
8. Verifikasi Manage accounting - Read: shortcut `+ Create account` Hidden (tidak dirender)

### TC-FA-PREF-229: Field Disabled dan tombol Save changes serta Cancel Hidden

9. Seed ulang Preferences company ke PB-1 lewat API lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
10. Verifikasi Manage accounting - Read: seluruh field form tetap tampil (visible) namun berstatus Disabled
11. Hover Select In-service Date Source
12. Verifikasi Manage accounting - Read: tooltip "You don't have permission to edit." tampil pada field Disabled
13. Verifikasi Manage accounting - Read: tombol `[Save changes]` dan `[Cancel]` Hidden (tidak dirender)

### TC-FA-PREF-561: Aktor Read tanpa Update melihat field Disabled dan tombol Hidden

14. Seed ulang Preferences company ke PC-1 lewat API lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
15. Verifikasi Manage accounting - Read: seluruh field tetap tampil (visible) namun berstatus Disabled
16. Hover salah satu field Disabled (Select In-service Date Source)
17. Verifikasi Manage accounting - Read: tooltip "You don't have permission to edit." tampil pada field Disabled
18. Verifikasi Manage accounting - Read: tombol `[Save changes]` dan `[Cancel]` Hidden (tidak dirender)
19. Verifikasi Manage accounting - Read: ikon View history tampil dan Enabled
20. Verifikasi Manage accounting - Read: shortcut `+ Create account` Hidden

### TC-FA-PREF-100: Manage accounting Read + Update dapat melihat dan mengubah Preferences

21. Seed ulang Preferences company ke PA-5 lewat API
22. Logout dari akun Manage accounting - Read
23. Login sebagai Manage accounting - Read + Update (`manageAccountingReadUpdate_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_MARU_PASSWORD`)
24. Buka Settings > Accounting > Preferences
25. Verifikasi Manage accounting - Read + Update: Tab "Preferences" tampil (Show) pada tab bar Settings > Accounting
26. Verifikasi Manage accounting - Read + Update: ikon View history tampil (Show) di header tab
27. Verifikasi Manage accounting - Read + Update: banner Setup Incomplete tampil (Show), Alert severity danger "Accounting setup is incomplete: Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, Depreciation in Disposal Month. Depreciation and journal export are blocked until completed."
28. Verifikasi Manage accounting - Read + Update: field form tampil (Show) dan Enabled (dapat diedit)
29. Verifikasi Manage accounting - Read + Update: `[Save changes]` dan `[Cancel]` tampil (Show)
30. Verifikasi Manage accounting - Read + Update: `[Save changes]` dan `[Cancel]` Disabled karena form pristine
31. Verifikasi Manage accounting - Read + Update: shortcut `+ Create account` Hidden (tidak dirender) karena aktor tidak memegang huruf Create

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Role Matrix (bagian 3a): matriks visibilitas yang memuat dua polaritas (Show dan Hidden/Disabled). Satu spec memuat empat TC karena keempatnya memeriksa visibilitas elemen Preferences pada dua akun Manage accounting dengan elemen yang sama; spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`, S-07).
- Urutan blok: TC-FA-PREF-100 (Read + Update) ditaruh di akhir supaya hanya ada satu pergantian akun (S-10).
- Langkah penghubung (S-03): langkah 9, 14, dan 21 (seed ulang Preferences dan, bila disebut, buka ulang halaman); pasangan logout dan login di langkah 22 dan 23.
- Absence Hidden (langkah 7, 8, 13, 18, 20, 31) memakai tab Preferences dan halaman yang sudah termuat sebagai anchor permukaan (8b butir 2).
- Temuan untuk QA:
  - TC-FA-PREF-99 Expected butir d tidak menyebut field mana yang di-hover; spec memakai Select In-service Date Source mengikuti TC-FA-PREF-229. TC-FA-PREF-561 menulis "salah satu field Disabled" dan spec memakai field yang sama.
  - TC-FA-PREF-99, 100, 229, dan 561 tidak menyebut nama env var password; nama `FA_MAR_PASSWORD` dan `FA_MARU_PASSWORD` diusulkan spec dan perlu keputusan tim.

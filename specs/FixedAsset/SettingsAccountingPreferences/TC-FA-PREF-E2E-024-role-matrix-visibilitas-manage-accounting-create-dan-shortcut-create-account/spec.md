---
id: TC-FA-PREF-E2E-024-role-matrix-visibilitas-manage-accounting-create-dan-shortcut-create-account
title: "Role Matrix: Visibilitas Preferences untuk Manage accounting Read + Create dan Read + Create + Update, shortcut Create account"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-101
  - TC-FA-PREF-102
  - TC-FA-PREF-122
  - TC-FA-PREF-123
sourceRules: ["§4.8#r1", "§4.8#r2", "ST-07", "§4.8#r3", "ST-08", "§4.8#r5", "§4.8#r6", "FAPREF-LOGIC-06i", "FI-03", "FAPREF-LOGIC-01b", "§2.1#r7", "§4.8#r4", "ST-01"]
smoke: []
dependsOn: []
trace:
  "§4.8#r1": [2, 26]
  "§4.8#r2": [3, 27]
  "ST-07": [4, 28]
  "§4.8#r3": [4, 28]
  "ST-08": 6
  "§4.8#r5": [7, 30]
  "§4.8#r6": [8, 22, 32]
  "FAPREF-LOGIC-06i": [8, 13, 22, 32]
  "FI-03": [11, 12, 15, 17, 18]
  "FAPREF-LOGIC-01b": 23
  "§2.1#r7": 24
  "§4.8#r4": 29
  "ST-01": 31
coverage:
  web: automated
---

# Role Matrix: Visibilitas Preferences untuk Manage accounting Read + Create dan Read + Create + Update, shortcut Create account

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

  | TC | Role | Pre-setup | Email | Env var password |
  |---|---|---|---|---|
  | TC-FA-PREF-101, TC-FA-PREF-122 | Manage accounting - Read + Create | PA-4 | `manageAccountingReadCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MARC_PASSWORD` |
  | TC-FA-PREF-102, TC-FA-PREF-123 | Manage accounting - Read + Create + Update | PA-4 | `manageAccountingReadCreateUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MARCU_PASSWORD` |
- Login akun aktor pertama (Manage accounting - Read + Create, company `PT Contoh Konstruksi`, PA-1) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun ke Manage accounting - Read + Create + Update memakai langkah logout dan login eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Env var `FA_MARC_PASSWORD` dan `FA_MARCU_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data awal blok TC-FA-PREF-101 (seed di hook `before`): Preferences company sesuai PA-5 (Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, dan Depreciation in Disposal Month kosong; setting lain bernilai awal) sehingga banner Setup Incomplete tampil.
- Data blok TC-FA-PREF-122, TC-FA-PREF-123 (seed lewat API oleh langkah penghubung): Preferences company sesuai PA-2 (nilai awal, tidak terkunci, semua setting wajib terisi); Chart of Accounts sesuai PA-3. Data blok TC-FA-PREF-102: PA-5 (seed ulang lewat API).
- Data Dinamis TC-FA-PREF-122 (DA-1): akun baru Account Code `4-9400` dan Account Name `Laba Selisih Pelepasan {runId}-024` (nama bersuffix per run, S-12). Kode `4-9400` literal dibersihkan di hook `before` (R-13) dan akun yang dibuat spec dihapus di hook `after`, keduanya lewat fixture BE yang disediakan tim FE/BE. Hook `after` juga memulihkan Preferences ke PA-2.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk kedua akun.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Kemampuan baca BE (disediakan tim FE/BE): keberadaan akun di Chart of Accounts dan nilai tersimpan Preferences, dipakai TC-FA-PREF-122 untuk Expected butir c.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-101: Manage accounting Read + Create, field Disabled dan shortcut Create account tampil

1. Buka Settings > Accounting > Preferences
2. Verifikasi Manage accounting - Read + Create: Tab "Preferences" tampil (Show) pada tab bar Settings > Accounting
3. Verifikasi Manage accounting - Read + Create: ikon View history tampil (Show) di header tab
4. Verifikasi Manage accounting - Read + Create: banner Setup Incomplete tampil (Show), Alert severity danger "Accounting setup is incomplete: Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, Depreciation in Disposal Month. Depreciation and journal export are blocked until completed."
5. Hover Select In-service Date Source
6. Verifikasi Manage accounting - Read + Create: seluruh field form tetap tampil namun Disabled dengan tooltip "You don't have permission to edit."
7. Verifikasi Manage accounting - Read + Create: `[Save changes]` dan `[Cancel]` Hidden (tidak dirender)
8. Verifikasi Manage accounting - Read + Create: shortcut `+ Create account` tampil (Show) pada Select Default Gain on Disposal dan Default Loss on Disposal meskipun kedua Select Disabled

### TC-FA-PREF-122: Shortcut Create account dapat dipakai walau Select Disabled

9. Seed ulang Preferences company ke PA-2 (Chart of Accounts PA-3) lewat API lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
10. Klik `+ Create account` pada Select Default Gain on Disposal
11. Verifikasi Select Default Gain on Disposal tetap Disabled
12. Verifikasi modal Add Account di Chart of Accounts terbuka
13. Verifikasi modal Add Account memiliki function terisi Gain on Disposal
14. Lengkapi modal Add Account dengan Account Code "4-9400" dan Account Name "Laba Selisih Pelepasan {runId}-024" lalu simpan
15. Verifikasi akun "4-9400 – Laba Selisih Pelepasan {runId}-024" tersimpan di Chart of Accounts
16. Buka Tab Preferences
17. Verifikasi Select Default Gain on Disposal tetap Disabled
18. Verifikasi Select Default Gain on Disposal tidak terisi otomatis

### TC-FA-PREF-123: Read + Create + Update tanpa kontrol Create atau Delete Preferences

19. Logout dari akun Manage accounting - Read + Create
20. Login sebagai Manage accounting - Read + Create + Update (`manageAccountingReadCreateUpdate_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_MARCU_PASSWORD`)
21. Buka Tab Preferences
22. Verifikasi Manage accounting - Read + Create + Update: shortcut `+ Create account` tampil pada Select Default Gain on Disposal dan Default Loss on Disposal
23. Verifikasi Manage accounting - Read + Create + Update: tidak ada kontrol untuk membuat atau menghapus Preferences pada header, SectionCard, dan footer
24. Verifikasi Manage accounting - Read + Create + Update: huruf Create hanya memunculkan shortcut `+ Create account`

### TC-FA-PREF-102: Read + Create + Update, gabungan elemen Show seluruh hurufnya

25. Seed ulang Preferences company ke PA-5 lewat API lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
26. Verifikasi Manage accounting - Read + Create + Update: Tab "Preferences" tampil (Show) pada tab bar Settings > Accounting
27. Verifikasi Manage accounting - Read + Create + Update: ikon View history tampil (Show) di header tab
28. Verifikasi Manage accounting - Read + Create + Update: banner Setup Incomplete tampil (Show), Alert severity danger "Accounting setup is incomplete: Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, Depreciation in Disposal Month. Depreciation and journal export are blocked until completed."
29. Verifikasi Manage accounting - Read + Create + Update: field form tampil (Show) dan Enabled (dapat diedit)
30. Verifikasi Manage accounting - Read + Create + Update: `[Save changes]` dan `[Cancel]` tampil (Show)
31. Verifikasi Manage accounting - Read + Create + Update: `[Save changes]` dan `[Cancel]` Disabled karena form pristine
32. Verifikasi Manage accounting - Read + Create + Update: shortcut `+ Create account` tampil (Show) pada Select Default Gain on Disposal dan Default Loss on Disposal

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Role Matrix (bagian 3a): spec memuat matriks visibilitas (TC-FA-PREF-101 dan TC-FA-PREF-102, dua polaritas Show dan Hidden/Disabled) beserta pemakaian shortcut `+ Create account` (TC-FA-PREF-122) dan ketiadaan kontrol Create/Delete Preferences (TC-FA-PREF-123) pada dua akun Manage accounting berhuruf Create yang sama. Satu spec memuat beberapa aksi karena keempat TC menguji perilaku huruf Create pada akun yang sama dan pengelompokan per akun menjaga satu pergantian akun saja. Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`, S-07).
- Urutan blok: TC-FA-PREF-123 ditaruh sebelum TC-FA-PREF-102 supaya dua TC berdata PA-2 berurutan, lalu satu seed ulang PA-5 untuk TC-FA-PREF-102 (S-10).
- Langkah penghubung (S-03): langkah 9, 25 (seed ulang Preferences dan buka ulang halaman); langkah 16 dan 21 (membuka Tab Preferences setelah modal Add Account atau setelah ganti akun); pasangan logout dan login di langkah 19 dan 20.
- Absence Hidden (langkah 7) memakai tab Preferences dan banner yang sudah termuat sebagai anchor permukaan (8b butir 2). Langkah 22 adalah anchor positif untuk absence kontrol pada langkah 23.
- Temuan untuk QA:
  - TC-FA-PREF-122 memakai nama akun literal "Laba Selisih Pelepasan" tanpa suffix; spec menambah suffix `{runId}-024` pada Account Name (S-12) dan membersihkan kode `4-9400` di hook.
  - TC-FA-PREF-122 tidak menyebut apakah modal Add Account menutup ke tab Preferences atau berpindah ke Chart of Accounts setelah Save; spec memakai langkah penghubung membuka Tab Preferences (langkah 16).
  - TC-FA-PREF-122 Expected butir a ("tetap Disabled") dan butir d tidak menyebut cara membuktikan "tidak terisi otomatis" selain membaca nilai Select; spec memverifikasi Select Default Gain on Disposal tidak terisi.
  - TC-FA-PREF-122 Post Condition ("nilai Preferences tidak berubah") sepadan dengan Expected butir d dan tidak diasersi terpisah. TC-FA-PREF-123 Expected "huruf Delete tidak dipakai" tidak punya perilaku teramati terpisah dan dicakup oleh `Verifikasi` tidak ada kontrol Create atau Delete (S-03).
  - TC-FA-PREF-101, 102, 122, dan 123 tidak menyebut nama env var password; nama `FA_MARC_PASSWORD` dan `FA_MARCU_PASSWORD` diusulkan spec dan perlu keputusan tim.

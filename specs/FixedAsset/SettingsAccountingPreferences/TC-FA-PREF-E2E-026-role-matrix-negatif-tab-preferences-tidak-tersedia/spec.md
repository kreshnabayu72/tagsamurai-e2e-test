---
id: TC-FA-PREF-E2E-026-role-matrix-negatif-tab-preferences-tidak-tersedia
title: "Role Matrix Negatif: Tab Preferences Tidak Tersedia di Menu untuk Update Saja, Create Saja, Delete Saja, Group Manager, dan Role Lain"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-103
  - TC-FA-PREF-104
  - TC-FA-PREF-105
  - TC-FA-PREF-106
  - TC-FA-PREF-107
coverage:
  web: automated
---

# Role Matrix Negatif: Tab Preferences Tidak Tersedia di Menu untuk Update Saja, Create Saja, Delete Saja, Group Manager, dan Role Lain

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

  | Role | Email Pre-setup | Env var password | TC |
  |---|---|---|---|
  | Manage accounting - Update | `manageAccountingUpdateOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAU_PASSWORD` | TC-FA-PREF-103 |
  | Manage accounting - Create | `manageAccountingCreateOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAC_PASSWORD` | TC-FA-PREF-104 |
  | Manage accounting - Delete | `manageAccountingDeleteOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAD_PASSWORD` | TC-FA-PREF-105 |
  | Group Manager (tanpa Manage accounting) | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | TC-FA-PREF-106 |
  | Role lain (tanpa Manage accounting) | `otherRoleFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_OT_PASSWORD` | TC-FA-PREF-107 |

- Akun aktor pertama: Manage accounting - Update. Login di hook `before` spec ini. Pengecualian layar awal: akun tanpa capability tidak dapat membuka Preferences, sehingga hook `beforeEach` suite hanya menutup dialog dan spec dimulai dari halaman beranda aplikasi. Ganti akun memakai langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Env var `FA_MAU_PASSWORD`, `FA_MAC_PASSWORD`, `FA_MAD_PASSWORD`, `FA_GM_PASSWORD`, dan `FA_OT_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` dengan Preferences PA-5 (Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, dan Depreciation in Disposal Month kosong; setting lain bernilai awal), dibentuk lewat seed. Spec hanya membaca.
- State yang diubah spec: tidak ada selain Preferences PA-5 hasil seed; hook `after` memulihkan Preferences ke PA-2.
- Kemampuan teknis: seed Preferences PA-5 dan pemulihan lewat sesi API aktor (butir "Seed dan pemulihan lewat API" dan "Sesi API aktor" di `suite.md`), disediakan tim FE/BE.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-103: Manage accounting Update saja tidak memiliki akses tab Preferences

1. Buka Settings > Accounting dari sidebar
2. Verifikasi tab bar Settings > Accounting menampilkan sedikitnya satu tab
3. Verifikasi Tab "Preferences" tidak dirender (Hidden) dan tidak dapat dibuka

### TC-FA-PREF-104: Manage accounting Create saja tidak melihat tab Preferences

4. Logout dari akun Manage accounting - Update
5. Login sebagai Manage accounting - Create (`manageAccountingCreateOnly_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_MAC_PASSWORD`)
6. Buka Settings > Accounting dari sidebar
7. Verifikasi tab bar Settings > Accounting menampilkan sedikitnya satu tab
8. Verifikasi Tab "Preferences" tidak dirender (Hidden) dan tidak dapat dibuka
9. Verifikasi shortcut `+ Create account` tidak terjangkau karena tab tidak dirender

### TC-FA-PREF-105: Manage accounting Delete saja tidak melihat tab Preferences

10. Logout dari akun Manage accounting - Create
11. Login sebagai Manage accounting - Delete (`manageAccountingDeleteOnly_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_MAD_PASSWORD`)
12. Buka Settings > Accounting dari sidebar
13. Verifikasi tab bar Settings > Accounting menampilkan sedikitnya satu tab
14. Verifikasi Tab "Preferences" tidak dirender (Hidden) dan tidak dapat dibuka

### TC-FA-PREF-106: Group Manager tanpa Manage accounting tidak memiliki akses menu Preferences

15. Logout dari akun Manage accounting - Delete
16. Login sebagai Group Manager (`groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_GM_PASSWORD`)
17. Verifikasi sidebar menampilkan sedikitnya satu entri menu selain Accounting
18. Verifikasi entri sidebar "Accounting" tidak dirender (Hidden)
19. Verifikasi Tab "Preferences" tidak tersedia bagi aktor

### TC-FA-PREF-107: Role lain tanpa Manage accounting tidak memiliki akses menu Preferences

20. Logout dari akun Group Manager
21. Login sebagai Role lain (`otherRoleFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_OT_PASSWORD`)
22. Verifikasi sidebar menampilkan sedikitnya satu entri menu selain Accounting
23. Verifikasi entri sidebar "Accounting" tidak dirender (Hidden)
24. Verifikasi Tab "Preferences" tidak tersedia bagi aktor

## Notes

- Role Matrix negatif (bagian 3a): spec polaritas seragam (tab Preferences tidak tersedia) dan memuat satu aksi (membuka tab dari menu). Ditulis per blok role karena ganti akun menuntut langkah eksplisit (akun pertama login di hook `before`) dan Expected tiap kelompok role berbeda: Update, Create, dan Delete saja mengamati tab bar, Group Manager dan Role lain mengamati sidebar.
- Langkah penghubung (S-03): langkah 4, 5, 10, 11, 15, 16, 20, 21 (ganti akun).
- Verifikasi anchor positif (8b.2, S-03): langkah 2, 7, 13 (tab bar menampilkan tab lain) dan 17, 22 (sidebar menampilkan entri menu lain) tidak ada di Expected TC dan ditambahkan sebagai anchor asersi Hidden.
- Temuan untuk QA:
  - Step 1 TC-FA-PREF-103 sampai 105 menulis "Buka Settings > Accounting dari sidebar bila entri tersedia" (bersyarat), sedangkan Expected tidak menyebut apakah entri sidebar "Accounting" tampil untuk Update saja, Create saja, dan Delete saja. Spec mengasumsikan entri tersedia (tab bar harus diperiksa pada step 2 TC). Precondition TC-FA-PREF-103 juga menyatakan aktor "diperlakukan seperti aktor tanpa akses", yang bertentangan dengan asumsi itu bila entri sidebar tidak dirender; perlu dikonfirmasi.
  - Step TC-FA-PREF-106 dan 107 ("Periksa tab bar Settings > Accounting") tidak dapat dijalankan karena entri sidebar tidak dirender; spec mengasersi Expected b lewat absennya jalur sidebar.
  - Email akun tidak ditulis utuh di TC (`{namaCompany}`); nama company perlu dikonfirmasi tim FE.

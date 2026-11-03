---
id: TC-FA-PREF-E2E-027-role-matrix-negatif-akses-url-langsung-ditolak
title: "Role Matrix Negatif: Akses Langsung URL Preferences Ditolak untuk Update Saja, Create Saja, Delete Saja, Group Manager, dan Role Lain"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-108
  - TC-FA-PREF-109
  - TC-FA-PREF-110
  - TC-FA-PREF-111
  - TC-FA-PREF-112
coverage:
  web: automated
---

# Role Matrix Negatif: Akses Langsung URL Preferences Ditolak untuk Update Saja, Create Saja, Delete Saja, Group Manager, dan Role Lain

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

  | Role | Email Pre-setup | Env var password | TC |
  |---|---|---|---|
  | Manage accounting - Update | `manageAccountingUpdateOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAU_PASSWORD` | TC-FA-PREF-108 |
  | Manage accounting - Create | `manageAccountingCreateOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAC_PASSWORD` | TC-FA-PREF-109 |
  | Manage accounting - Delete | `manageAccountingDeleteOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAD_PASSWORD` | TC-FA-PREF-110 |
  | Group Manager (tanpa Manage accounting) | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | TC-FA-PREF-111 |
  | Role lain (tanpa Manage accounting) | `otherRoleFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_OT_PASSWORD` | TC-FA-PREF-112 |

- Akun aktor pertama: Manage accounting - Update. Login di hook `before` spec ini. Pengecualian layar awal: akun tanpa capability tidak dapat membuka Preferences, sehingga hook `beforeEach` suite hanya menutup dialog dan spec dimulai dari halaman beranda aplikasi. Ganti akun memakai langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Env var `FA_MAU_PASSWORD`, `FA_MAC_PASSWORD`, `FA_MAD_PASSWORD`, `FA_GM_PASSWORD`, dan `FA_OT_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` dengan Preferences PA-5 (Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, dan Depreciation in Disposal Month kosong; setting lain bernilai awal), dibentuk lewat seed. Spec hanya membaca. URL langsung: Settings > Accounting > Preferences.
- State yang diubah spec: tidak ada selain Preferences PA-5 hasil seed; hook `after` memulihkan Preferences ke PA-2.
- Kemampuan teknis: seed Preferences PA-5 dan pemulihan lewat sesi API aktor (butir "Seed dan pemulihan lewat API" dan "Sesi API aktor" di `suite.md`), disediakan tim FE/BE.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-108: Akses langsung URL Preferences oleh Manage accounting Update saja ditolak

1. Ketik atau tempel URL langsung Settings > Accounting > Preferences pada address bar lalu tekan Enter
2. Verifikasi muncul toast error: "You don't have permission to do this."
3. Verifikasi tidak ada redirect ke halaman unauthorized terpisah
4. Verifikasi UI di-refresh sehingga Tab Preferences tidak dirender
5. Verifikasi nilai Preferences tidak ditampilkan

### TC-FA-PREF-109: Akses langsung URL Preferences oleh Manage accounting Create saja ditolak

6. Tutup toast error, lalu Logout dari akun Manage accounting - Update
7. Login sebagai Manage accounting - Create (`manageAccountingCreateOnly_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_MAC_PASSWORD`)
8. Ketik atau tempel URL langsung Settings > Accounting > Preferences pada address bar lalu tekan Enter
9. Verifikasi muncul toast error: "You don't have permission to do this."
10. Verifikasi tidak ada redirect ke halaman unauthorized terpisah
11. Verifikasi UI di-refresh sehingga Tab Preferences tidak dirender
12. Verifikasi nilai Preferences tidak ditampilkan

### TC-FA-PREF-110: Akses langsung URL Preferences oleh Manage accounting Delete saja ditolak

13. Tutup toast error, lalu Logout dari akun Manage accounting - Create
14. Login sebagai Manage accounting - Delete (`manageAccountingDeleteOnly_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_MAD_PASSWORD`)
15. Ketik atau tempel URL langsung Settings > Accounting > Preferences pada address bar lalu tekan Enter
16. Verifikasi muncul toast error: "You don't have permission to do this."
17. Verifikasi tidak ada redirect ke halaman unauthorized terpisah
18. Verifikasi UI di-refresh sehingga Tab Preferences tidak dirender
19. Verifikasi nilai Preferences tidak ditampilkan

### TC-FA-PREF-111: Akses langsung URL Preferences oleh Group Manager tanpa Manage accounting ditolak

20. Tutup toast error, lalu Logout dari akun Manage accounting - Delete
21. Login sebagai Group Manager (`groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_GM_PASSWORD`)
22. Ketik atau tempel URL langsung Settings > Accounting > Preferences pada address bar lalu tekan Enter
23. Verifikasi muncul toast error: "You don't have permission to do this."
24. Verifikasi tidak ada redirect ke halaman unauthorized terpisah
25. Verifikasi UI di-refresh sehingga Tab Preferences tidak dirender
26. Verifikasi nilai Preferences tidak ditampilkan

### TC-FA-PREF-112: Akses langsung URL Preferences oleh Role lain tanpa Manage accounting ditolak

27. Tutup toast error, lalu Logout dari akun Group Manager
28. Login sebagai Role lain (`otherRoleFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_OT_PASSWORD`)
29. Ketik atau tempel URL langsung Settings > Accounting > Preferences pada address bar lalu tekan Enter
30. Verifikasi muncul toast error: "You don't have permission to do this."
31. Verifikasi tidak ada redirect ke halaman unauthorized terpisah
32. Verifikasi UI di-refresh sehingga Tab Preferences tidak dirender
33. Verifikasi nilai Preferences tidak ditampilkan

## Notes

- Role Matrix negatif (bagian 3a): spec polaritas seragam (akses langsung URL ditolak) dan memuat satu aksi. Ditulis per blok role karena ganti akun menuntut langkah eksplisit (akun pertama login di hook `before`); langkah tiap role identik tetapi tiap blok memuat Step ganti akun. Spec berlangkah 33, di bawah ambang ~35.
- Langkah penghubung (S-03): langkah 6, 7, 13, 14, 20, 21, 27, 28 (menutup toast error dan ganti akun; R-12).
- Asersi `Hidden` pada Role Matrix memakai halaman yang sudah termuat sebagai anchor permukaan (8b.2); tidak ada anchor tambahan.
- Temuan untuk QA:
  - Klausa "UI di-refresh" (Expected c) tidak punya padanan yang teramati terpisah; spec mengasersi hasilnya (Tab Preferences tidak dirender dan nilai tidak ditampilkan).
  - Expected b ("tidak ada redirect ke halaman unauthorized terpisah") tidak menyebut halaman tujuan setelah penolakan; spec hanya mengasersi bahwa halaman unauthorized terpisah tidak tampil.
  - Email akun tidak ditulis utuh di TC (`{namaCompany}`); nama company perlu dikonfirmasi tim FE.

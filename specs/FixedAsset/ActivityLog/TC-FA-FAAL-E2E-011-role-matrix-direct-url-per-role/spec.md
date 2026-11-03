---
id: TC-FA-FAAL-E2E-011-role-matrix-direct-url-per-role
title: "Role Matrix: Buka URL Activity Log Langsung per Role"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAL-44
  - TC-FA-FAAL-45
  - TC-FA-FAAL-46
  - TC-FA-FAAL-47
coverage:
  web: automated
---

# Role Matrix: Buka URL Activity Log Langsung per Role

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (semuanya tanpa tingkat akses Total Control, Read Only, maupun Group Manager, kecuali baris Group Manager):

  | TC | Role | Pre-setup | Email | Env var password |
  |---|---|---|---|---|
  | TC-FA-FAAL-44 | Group Manager (Group Manager untuk group Gedung A) | #8 | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |
- Tabel "Global Role (Pre-setup #5)" untuk TC-FA-FAAL-45; password semuanya `Spectra.env.FA_ROLEHOLDER_PASSWORD`:

  | No | Global Role | Email |
  |---|---|---|
  | 1 | `Import data` | `importData_automated_{namaCompany}@qwertysystem.net` |
  | 2 | `Manage asset master data` | `manageAssetMasterData_automated_{namaCompany}@qwertysystem.net` |
  | 3 | `Manage asset transactional policy` | `manageAssetTransactionalPolicy_automated_{namaCompany}@qwertysystem.net` |
  | 4 | `Manage accounting` | `manageAccounting_automated_{namaCompany}@qwertysystem.net` |
  | 5 | `Manage transaction settings` | `manageTransactionSettings_automated_{namaCompany}@qwertysystem.net` |
  | 6 | `Manage Open API` | `manageOpenApi_automated_{namaCompany}@qwertysystem.net` |
  | 7 | `Manage asset ID configuration` | `manageAssetIdConfiguration_automated_{namaCompany}@qwertysystem.net` |
  | 8 | `Manage global license` | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` |
  | 9 | `Manage global user & role` | `manageGlobalUserRole_automated_{namaCompany}@qwertysystem.net` |
- Tabel "Group Role (Pre-setup #6)" untuk TC-FA-FAAL-46; role pada group Gedung A, password semuanya `Spectra.env.FA_ROLEHOLDER_PASSWORD`:

  | No | Group Role | Email |
  |---|---|---|
  | 1 | `Manage asset & TAG` | `manageAssetTag_automated_{namaCompany}@qwertysystem.net` |
  | 2 | `Manage files` | `manageFiles_automated_{namaCompany}@qwertysystem.net` |
  | 3 | `Manage group` | `manageGroup_automated_{namaCompany}@qwertysystem.net` |
  | 4 | `Manage user & role` | `manageUserRole_automated_{namaCompany}@qwertysystem.net` |
  | 5 | `Manage asset license` | `manageAssetLicense_automated_{namaCompany}@qwertysystem.net` |
  | 6 | `Manage purchase` | `managePurchase_automated_{namaCompany}@qwertysystem.net` |
  | 7 | `View asset value` | `viewAssetValue_automated_{namaCompany}@qwertysystem.net` |
- Tabel "Transaction Role (Pre-setup #7)" untuk TC-FA-FAAL-47; role pada sub-tab Disposal group Gedung A, password semuanya `Spectra.env.FA_ROLEHOLDER_PASSWORD`:

  | No | Transaction Role | Email |
  |---|---|---|
  | 1 | `Asset Admin` | `assetAdmin_automated_{namaCompany}@qwertysystem.net` |
  | 2 | `Staff` | `staff_automated_{namaCompany}@qwertysystem.net` |
  | 3 | `Monitoring & Report` | `monitoringReport_automated_{namaCompany}@qwertysystem.net` |
  | 4 | `Approver` | `approver_automated_{namaCompany}@qwertysystem.net` |
- URL halaman Reports & Logs > Activity Log dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Login akun aktor pertama (Group Manager, Pre-setup #8) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Pengecualian atas `suite.md`: precondition semua TC adalah Fixed Asset > Dashboard, sehingga hook `beforeEach` membuka Fixed Asset > Dashboard (bukan Activity Log) untuk spec ini. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Setiap ganti akun di tengah spec memakai satu langkah logout dan login eksplisit.
- Env var `FA_GM_PASSWORD` dan `FA_ROLEHOLDER_PASSWORD` (satu password bersama untuk 20 user pemegang Global, Group, dan Transaction Role) didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (R-07). Password tidak ditulis di spec atau fixture.
- Data: spec tidak memakai baris log tertentu; yang diamati adalah penolakan akses.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk semua akun aktor spec ini.
- Seed dan pemulihan lewat API (user pemegang role Pre-setup #5, #6, #7, dan #8) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-44: Group Manager membuka URL Activity Log langsung

1. Ketik URL halaman Reports & Logs > Activity Log langsung di address bar lalu tekan Enter
2. Verifikasi Group Manager: muncul toast error "You don't have permission to do this."
3. Verifikasi Group Manager: UI di-refresh
4. Verifikasi Group Manager: tidak menampilkan data Tab Session maupun Tab User Action
5. Verifikasi Group Manager: tidak ada redirect ke halaman unauthorized terpisah

### TC-FA-FAAL-45: Pemegang Global Role membuka URL Activity Log langsung

Untuk setiap baris tabel "Global Role (Pre-setup #5)" di Prerequisites, lakukan langkah 6 sampai 9.

6. Ganti akun: Logout dari akun sebelumnya, lalu Login sebagai user pada baris tabel (email baris, password dari `Spectra.env.FA_ROLEHOLDER_PASSWORD`) dan buka Fixed Asset > Dashboard
7. Ketik URL halaman Reports & Logs > Activity Log langsung di address bar lalu tekan Enter
8. Verifikasi pemegang `<Global Role baris>`: toast error "You don't have permission to do this."
9. Verifikasi pemegang `<Global Role baris>`: data log tidak tampil

### TC-FA-FAAL-46: Pemegang Group Role membuka URL Activity Log langsung

Untuk setiap baris tabel "Group Role (Pre-setup #6)" di Prerequisites, lakukan langkah 10 sampai 13.

10. Ganti akun: Logout dari akun sebelumnya, lalu Login sebagai user pada baris tabel (email baris, password dari `Spectra.env.FA_ROLEHOLDER_PASSWORD`) dan buka Fixed Asset > Dashboard
11. Ketik URL halaman Reports & Logs > Activity Log langsung di address bar lalu tekan Enter
12. Verifikasi pemegang `<Group Role baris>`: toast error "You don't have permission to do this."
13. Verifikasi pemegang `<Group Role baris>`: data log tidak tampil

### TC-FA-FAAL-47: Pemegang Transaction Role membuka URL Activity Log langsung

Untuk setiap baris tabel "Transaction Role (Pre-setup #7)" di Prerequisites, lakukan langkah 14 sampai 17.

14. Ganti akun: Logout dari akun sebelumnya, lalu Login sebagai user pada baris tabel (email baris, password dari `Spectra.env.FA_ROLEHOLDER_PASSWORD`) dan buka Fixed Asset > Dashboard
15. Ketik URL halaman Reports & Logs > Activity Log langsung di address bar lalu tekan Enter
16. Verifikasi pemegang `<Transaction Role baris>`: toast error "You don't have permission to do this."
17. Verifikasi pemegang `<Transaction Role baris>`: data log tidak tampil

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix (bagian 3a), akses ditolak per role. Ganti akun memakai satu langkah eksplisit per iterasi (akun pertama login di hook `before`, S-07).
- Langkah 6 sampai 9 diulang 9 kali, langkah 10 sampai 13 diulang 7 kali, dan langkah 14 sampai 17 diulang 4 kali. Verifikasi diulang satu per baris dan satu per klausa (S-01: toast, lalu data log tidak tampil; Expected butir a sampai i TC-FA-FAAL-45, a sampai g TC-FA-FAAL-46, a sampai d TC-FA-FAAL-47).
- Langkah penghubung (S-03): langkah 6, 10, dan 14 (ganti akun, lalu membuka Fixed Asset > Dashboard sebagai precondition TC).
- Anchor asersi absence data log (bagian 8b butir 2): toast penolakan pada langkah 2, 8, 12, dan 16 menjadi anchor positif.
- Ukuran spec (sekitar 85 langkah setelah ekspansi: 5 untuk TC-FA-FAAL-44, 36 untuk TC-FA-FAAL-45, 28 untuk TC-FA-FAAL-46, 16 untuk TC-FA-FAAL-47; 17 langkah nominal): melewati sekitar 35 langkah karena Role Matrix mengulang urutan yang sama untuk tiap role (bagian 3a) dan tiap klausa Expected menjadi satu `Verifikasi` (S-01). Semua blok satu kelas (akses ditolak lewat URL langsung) dan berdiri sendiri: tiap iterasi mulai dengan ganti akun eksplisit dan membuka halaman sendiri, sehingga kegagalan satu role tidak membuat iterasi lain kehilangan makna. Langkah tiap role identik, sehingga spec dipertahankan utuh.
- Temuan untuk QA:
  - TC-FA-FAAL-44 sampai 47 tidak menyebut env var password; nama env var diusulkan dari butir "Env var" di `suite.md`.
  - TC-FA-FAAL-44 dan 45 sampai 47 menyebut "UI di-refresh" tanpa cara mengamatinya; spec memverifikasi refresh sebagai klausa TC-FA-FAAL-44 butir b dan tidak menambahkan asersi serupa untuk TC-FA-FAAL-45 sampai 47 yang tidak menyebutnya.
  - Pre-setup #6 dan #7 hanya menulis awalan email (mis. `manageAssetTag_...`); format lengkap `_automated_{namaCompany}@qwertysystem.net` mengikuti Pre-setup #5 dan perlu dikonfirmasi.

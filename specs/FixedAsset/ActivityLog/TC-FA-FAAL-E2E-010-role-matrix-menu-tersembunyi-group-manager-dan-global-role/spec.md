---
id: TC-FA-FAAL-E2E-010-role-matrix-menu-tersembunyi-group-manager-dan-global-role
title: "Role Matrix: Menu Activity Log Tersembunyi (Group Manager dan Global Role)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAL-40
  - TC-FA-FAAL-41
coverage:
  web: automated
---

# Role Matrix: Menu Activity Log Tersembunyi (Group Manager dan Global Role)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (semuanya tanpa tingkat akses Total Control, Read Only, maupun Group Manager, kecuali baris Group Manager):

  | TC | Role | Pre-setup | Email | Env var password |
  |---|---|---|---|---|
  | TC-FA-FAAL-40 | Group Manager (Group Manager untuk group Gedung A) | #8 | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |

- Tabel "Global Role (Pre-setup #5)" untuk TC-FA-FAAL-41; satu user per baris, password semuanya `Spectra.env.FA_ROLEHOLDER_PASSWORD`:

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
- Login akun aktor pertama (Group Manager, Pre-setup #8) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Pengecualian atas `suite.md`: precondition kedua TC adalah Fixed Asset > Dashboard, sehingga hook `beforeEach` membuka Fixed Asset > Dashboard (bukan Activity Log) untuk spec ini. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Ganti akun di tengah spec memakai satu langkah logout dan login eksplisit.
- Env var `FA_GM_PASSWORD` dan `FA_ROLEHOLDER_PASSWORD` (satu password bersama untuk 20 user pemegang Global, Group, dan Transaction Role) didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (R-07). Password tidak ditulis di spec atau fixture.
- Data: spec tidak memakai baris log tertentu; hanya menu sidebar yang diamati.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk semua akun aktor spec ini.
- Seed dan pemulihan lewat API (user pemegang role Pre-setup #5 dan #8) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas akun Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-40: Menu Activity Log tersembunyi untuk Group Manager

1. Buka sidebar Fixed Asset
2. Telusuri seluruh daftar menu sidebar Fixed Asset
3. Verifikasi Group Manager: menu `Activity Log` Hidden (tidak ada di daftar menu sidebar), bukan Disabled

### TC-FA-FAAL-41: Menu Activity Log tersembunyi untuk pemegang Global Role

Untuk setiap baris tabel "Global Role (Pre-setup #5)" di Prerequisites, lakukan langkah 4 sampai 6.

4. Ganti akun: Logout dari akun sebelumnya, lalu Login sebagai user pada baris tabel (email baris, password dari `Spectra.env.FA_ROLEHOLDER_PASSWORD`) dan buka Fixed Asset > Dashboard
5. Buka sidebar Reports & Logs
6. Verifikasi pemegang `<Global Role baris>`: menu `Activity Log` Hidden

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-FA-FAAL-40 dan 41 ada di spec ini; TC-FA-FAAL-42 dan 43 ada di spec 065.
- Spec Role Matrix visibilitas (bagian 3a), polaritas Hidden saja. Ganti akun memakai satu langkah eksplisit per iterasi (akun pertama login di hook `before`, S-07); tiap iterasi berdiri sendiri.
- Langkah 4 sampai 6 diulang untuk 9 baris tabel Global Role. Verifikasi diulang satu per baris (S-01, Expected butir a sampai i TC-FA-FAAL-41).
- Langkah penghubung (S-03): langkah 2 adalah observasi TC ("Telusuri seluruh daftar menu") yang hasilnya diasersi di langkah 3; langkah 4 (ganti akun, lalu membuka Fixed Asset > Dashboard sebagai precondition TC) dan langkah 5 (observasi).
- Anchor asersi Hidden (bagian 8b butir 2, Role Matrix): halaman dan sidebar yang sudah termuat menjadi anchor permukaan.
- Ukuran spec: 3 langkah nominal untuk TC-FA-FAAL-40 dan 3 langkah nominal yang diulang 9 kali untuk TC-FA-FAAL-41, sekitar 30 langkah setelah ekspansi; di bawah ambang.
- Temuan untuk QA:
  - TC-FA-FAAL-40 sampai 43 tidak menyebut env var password; nama env var diusulkan dari butir "Env var" di `suite.md`.
  - Pre-setup #5 memuat format email lengkap `_automated_{namaCompany}@qwertysystem.net`; spec memakai format yang sama dengan awalan kecil per role yang tertulis di Pre-setup (mis. `importData`, `manageAccounting`).
  - TC-FA-FAAL-40 tidak menyebut item menu pembanding pada sidebar Group Manager; spec memakai halaman termuat sebagai anchor.

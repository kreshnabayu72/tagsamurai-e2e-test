---
id: TC-FA-FAAL-E2E-065-role-matrix-menu-tersembunyi-group-role-dan-transaction-role
title: "Role Matrix: Menu Activity Log Tersembunyi (Group Role dan Transaction Role)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAL-42
  - TC-FA-FAAL-43
coverage:
  web: automated
---

# Role Matrix: Menu Activity Log Tersembunyi (Group Role dan Transaction Role)

## Prerequisites

- Mode: FE+BE.
- Semua user di bawah ini memegang tepat satu role tanpa tingkat akses Total Control, Read Only, maupun Group Manager. Password semuanya `Spectra.env.FA_ROLEHOLDER_PASSWORD`.
- Tabel "Group Role (Pre-setup #6)" untuk TC-FA-FAAL-42; role pada group Gedung A:

  | No | Group Role | Email |
  |---|---|---|
  | 1 | `Manage asset & TAG` | `manageAssetTag_automated_{namaCompany}@qwertysystem.net` |
  | 2 | `Manage files` | `manageFiles_automated_{namaCompany}@qwertysystem.net` |
  | 3 | `Manage group` | `manageGroup_automated_{namaCompany}@qwertysystem.net` |
  | 4 | `Manage user & role` | `manageUserRole_automated_{namaCompany}@qwertysystem.net` |
  | 5 | `Manage asset license` | `manageAssetLicense_automated_{namaCompany}@qwertysystem.net` |
  | 6 | `Manage purchase` | `managePurchase_automated_{namaCompany}@qwertysystem.net` |
  | 7 | `View asset value` | `viewAssetValue_automated_{namaCompany}@qwertysystem.net` |
- Tabel "Transaction Role (Pre-setup #7)" untuk TC-FA-FAAL-43; role pada sub-tab Disposal untuk Group Gedung A:

  | No | Transaction Role | Email |
  |---|---|---|
  | 1 | `Asset Admin` | `assetAdmin_automated_{namaCompany}@qwertysystem.net` |
  | 2 | `Staff` | `staff_automated_{namaCompany}@qwertysystem.net` |
  | 3 | `Monitoring & Report` | `monitoringReport_automated_{namaCompany}@qwertysystem.net` |
  | 4 | `Approver` | `approver_automated_{namaCompany}@qwertysystem.net` |
- Login akun aktor pertama (Total Control, Pre-setup #1) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Pengecualian atas `suite.md`: precondition kedua TC adalah Fixed Asset > Dashboard, sehingga hook `beforeEach` membuka Fixed Asset > Dashboard (bukan Activity Log) untuk spec ini. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Setiap iterasi memakai satu langkah ganti akun eksplisit.
- Env var `FA_ROLEHOLDER_PASSWORD` (satu password bersama untuk 20 user pemegang Global, Group, dan Transaction Role) didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (R-07). Password tidak ditulis di spec atau fixture.
- Data: spec tidak memakai baris log tertentu; hanya menu sidebar yang diamati.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk semua akun aktor spec ini.
- Seed dan pemulihan lewat API (user pemegang role Pre-setup #6 dan #7) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas akun Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-42: Menu Activity Log tersembunyi untuk pemegang Group Role

Untuk setiap baris tabel "Group Role (Pre-setup #6)" di Prerequisites, lakukan langkah 1 sampai 3.

1. Ganti akun: Logout dari akun sebelumnya, lalu Login sebagai user pada baris tabel (email baris, password dari `Spectra.env.FA_ROLEHOLDER_PASSWORD`) dan buka Fixed Asset > Dashboard
2. Buka sidebar Reports & Logs
3. Verifikasi pemegang `<Group Role baris>`: menu `Activity Log` Hidden

### TC-FA-FAAL-43: Menu Activity Log tersembunyi untuk pemegang Transaction Role

Untuk setiap baris tabel "Transaction Role (Pre-setup #7)" di Prerequisites, lakukan langkah 4 sampai 6.

4. Ganti akun: Logout dari akun sebelumnya, lalu Login sebagai user pada baris tabel (email baris, password dari `Spectra.env.FA_ROLEHOLDER_PASSWORD`) dan buka Fixed Asset > Dashboard
5. Buka sidebar Reports & Logs
6. Verifikasi pemegang `<Transaction Role baris>`: menu `Activity Log` Hidden

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-FA-FAAL-42 dan 43 ada di spec ini; TC-FA-FAAL-40 dan 41 ada di spec 010.
- Spec Role Matrix visibilitas (bagian 3a), polaritas Hidden saja. Karena akun pertama aktor spec ini (Total Control) bukan akun role yang diuji, setiap iterasi memulai dengan langkah ganti akun eksplisit (S-07).
- Langkah 1 sampai 3 diulang 7 kali dan langkah 4 sampai 6 diulang 4 kali; Verifikasi diulang satu per baris (S-01, Expected butir a sampai g TC-FA-FAAL-42 dan a sampai d TC-FA-FAAL-43).
- Langkah penghubung (S-03): langkah 1 dan 4 (ganti akun, lalu membuka Fixed Asset > Dashboard sebagai precondition TC); langkah 2 dan 5 adalah observasi TC yang hasilnya diasersi di langkah berikutnya.
- Anchor asersi Hidden (bagian 8b butir 2, Role Matrix): halaman dan sidebar yang sudah termuat menjadi anchor permukaan.
- Ukuran spec: 3 langkah nominal per blok, sekitar 33 langkah setelah ekspansi (21 untuk TC-FA-FAAL-42 dan 12 untuk TC-FA-FAAL-43); di bawah ambang.
- Temuan untuk QA:
  - TC-FA-FAAL-42 dan 43 tidak menyebut env var password; nama env var diusulkan dari butir "Env var" di `suite.md`.
  - Pre-setup #6 dan #7 hanya menulis awalan email (mis. `manageAssetTag_...`); format lengkap `_automated_{namaCompany}@qwertysystem.net` mengikuti Pre-setup #5 dan perlu dikonfirmasi.

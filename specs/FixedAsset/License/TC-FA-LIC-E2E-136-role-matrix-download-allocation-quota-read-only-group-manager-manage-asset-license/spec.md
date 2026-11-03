---
id: TC-FA-LIC-E2E-136-role-matrix-download-allocation-quota-read-only-group-manager-manage-asset-license
title: "Role Matrix: Download Allocation Quota Tersedia untuk Read Only, Group Manager, dan Manage Asset License"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-562
coverage:
  web: automated
---

# Role Matrix: Download Allocation Quota Tersedia untuk Read Only, Group Manager, dan Manage Asset License

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (spec positif, bagian 3a):

  | Role | Pre-setup | Akun (fixture) | Password (env) |
  |---|---|---|---|
  | Read Only | #2 | `Fixture.fixedAssetLicense.akunReadOnly` (pola `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net`) | `Spectra.env.FA_RO_PASSWORD` |
  | Group Manager | #6 | `Fixture.fixedAssetLicense.akunGroupManagerHq` (pola `groupManagerHQ_automated_{namaCompany}@qwertysystem.net`; Kantor Pusat) | `Spectra.env.FA_GM_HQ_PASSWORD` |
  | Manage asset license | #4 | `Fixture.fixedAssetLicense.akunManageAssetLicenseHq` (pola `manageAssetLicenseHQ_automated_{namaCompany}@qwertysystem.net`; Group Role Manage asset license pada Kantor Pusat) | `Spectra.env.FA_MAL_HQ_PASSWORD` |

- Akun aktor pertama: Read Only. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control Pre-setup #1). Akun kedua dan ketiga lewat langkah ganti akun eksplisit. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite untuk akun aktor pertama (dinyatakan sekali di `suite.md`); flag akun lain sudah true menurut catatan TC (semua akun kecuali Pre-setup #19).
- Data Pre-setup (hanya dibaca): #12 (kuota dan hierarki PT Sejahtera, client Paid), lewat `Fixture.fixedAssetLicense.kuotaHierarki` (fixture belum ada; disediakan tim FE/BE).
- Kemampuan teknis (dinyatakan di `suite.md`, dirujuk satu baris): membaca isi berkas unduhan CSV; berkas tiap unduhan ditangkap ke direktori bersih.

## Test Steps

### Role Read Only

1. Klik Tab `Allocation Quota`
2. Verifikasi ikon Download aktif pada toolbar Section 2
3. Klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
4. Verifikasi berkas `License-Allocation-Quota.csv` terunduh

### Role Group Manager

5. Ganti akun: Logout, lalu login sebagai Group Manager (Pre-setup #6) dengan `Spectra.env.FA_GM_HQ_PASSWORD`, lalu buka Fixed Asset > License > Tab `Allocation Quota`
6. Verifikasi ikon Download aktif pada toolbar Section 2
7. Klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
8. Verifikasi berkas `License-Allocation-Quota.csv` terunduh

### Role Manage asset license

9. Ganti akun: Logout, lalu login sebagai Manage asset license (Pre-setup #4) dengan `Spectra.env.FA_MAL_HQ_PASSWORD`, lalu buka Fixed Asset > License > Tab `Allocation Quota`
10. Verifikasi ikon Download aktif pada toolbar Section 2
11. Klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
12. Verifikasi berkas `License-Allocation-Quota.csv` terunduh
13. Verifikasi isi ketiga berkas (Read Only, Group Manager, Manage asset license) sama

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke role. Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`): langkah 1 (membuka Tab `Allocation Quota`), langkah 3, 7, dan 11 (membuka isi berkas), langkah 5 dan 9 (ganti akun eksplisit, S-07, dan membuka halaman untuk akun baru).
- Temuan untuk QA:
  - TC-FA-LIC-562 tidak menyebut email dan Pre-setup akun Read Only, Group Manager, dan Manage asset license; spec memakai Pre-setup #2, #6, dan #4 (Manage asset license pada Kantor Pusat) sesuai tabel Pre-setup.
  - TC mensyaratkan isi berkas sama untuk ketiga akun. Group Manager #6 dan Manage asset license #4 hanya ditugaskan pada Kantor Pusat sedangkan Read Only melihat node `All Groups`; TC tidak menyebut apakah cakupan data berkas berbeda per akun. Spec mengikuti TC (isi sama).
  - TC-FA-LIC-562 tidak memiliki Post Condition (`-`); tidak ada yang diasersi.

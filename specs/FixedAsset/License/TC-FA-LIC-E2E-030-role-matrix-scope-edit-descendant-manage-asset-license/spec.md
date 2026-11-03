---
id: TC-FA-LIC-E2E-030-role-matrix-scope-edit-descendant-manage-asset-license
title: "Role Matrix: Scope Edit Descendant untuk Manage Asset License dan Group Manager"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-99
  - TC-FA-LIC-100
  - TC-FA-LIC-101
  - TC-FA-LIC-530
coverage:
  web: automated
---

# Role Matrix: Scope Edit Descendant untuk Manage Asset License dan Group Manager

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage asset license (Kantor Pusat) (Pre-setup #4): `manageAssetLicenseHQ_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_MAL_HQ_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun lain pada tabel "Role yang diuji" lewat langkah Ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; seluruh nama env pada tabel adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Role yang diuji (Tabel Data Uji Pre-setup #4, #5, #6, #29):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-FA-LIC-99 | Manage asset license (Kantor Pusat) (Pre-setup #4) | `manageAssetLicenseHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAL_HQ_PASSWORD` |
| TC-FA-LIC-100 | Group Manager (Kantor Pusat) (Pre-setup #6) | `groupManagerHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_HQ_PASSWORD` |
| TC-FA-LIC-101 | Manage asset license tumpang tindih (Kantor Pusat dan Divisi Logistik) (Pre-setup #5) | `manageAssetLicenseOverlap_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAL_OVERLAP_PASSWORD` |
| TC-FA-LIC-530 | Group Manager tumpang tindih (Kantor Pusat dan Divisi Logistik) (Pre-setup #29) | `groupManagerOverlap_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_OVERLAP_PASSWORD` |

- Data Pre-setup #12 (`Fixture.fixedAssetLicense.kuotaHierarki`): hierarki Produksi, Kantor Pusat (Divisi Logistik (Gudang A), Divisi IT, Divisi Keuangan), Cabang Surabaya, Cabang Medan dengan alokasi, Used, dan Reserved sesuai Example Data PRD §4.1.3; disediakan tim FE/BE. Divisi Logistik beralokasi 500 (Maximum Quota 700).
- S-06: target aksi tulis adalah alokasi grup Pre-setup #12 bernama literal yang hierarki dan kuotanya tidak dapat dimiliki spec. Pemulihan ke keadaan awal dijamin fixture BE (disediakan tim FE/BE, dinyatakan di `suite.md`) di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan Pre-setup #12"; efeknya (Last Updated grup, entri Changelog: Allocation Quota, System Log, dan Activity Log) tidak dipulihkan. Suite serial (`parallel: false`).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.

## Test Steps

### TC-FA-LIC-99: Manage asset license: tombol Edit Show hanya pada descendant dari grup yang di-assign

1. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
2. Arahkan kursor ke tombol `[Edit]` yang Disabled pada Group Quota Summary
3. Verifikasi `[Edit]` Group Quota Summary Kantor Pusat (grup yang di-assign) Disabled dengan tooltip `You don't have permission to edit.`
4. Verifikasi `[Edit]` Show pada baris child Divisi Logistik, Divisi IT, dan Divisi Keuangan
5. Klik node `Divisi Logistik`
6. Verifikasi `[Edit]` Show pada Group Quota Summary Divisi Logistik
7. Klik node `Gudang A`
8. Verifikasi `[Edit]` Show pada Group Quota Summary Gudang A
9. Klik node `All Groups`
10. Arahkan kursor ke tombol `[Edit]` yang Disabled pada Section 2
11. Verifikasi `[Edit]` Disabled dengan tooltip `You don't have permission to edit.` pada keempat grup level 1 (Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat)
12. Klik tombol `[Edit]` yang Disabled pada Section 2
13. Verifikasi klik tidak membuka modal Edit Allocation

### TC-FA-LIC-100: Group Manager: tombol Edit mengikuti scope descendant dari grup yang ditugaskan

14. Ganti akun: logout, lalu login sebagai Group Manager (Kantor Pusat) dengan `Spectra.env.FA_GM_HQ_PASSWORD`
15. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
16. Arahkan kursor ke tombol `[Edit]` yang Disabled pada Group Quota Summary
17. Verifikasi Group Quota Summary Kantor Pusat: `[Edit]` Disabled dengan tooltip `You don't have permission to edit.`
18. Verifikasi `[Edit]` Show pada baris child Divisi Logistik, Divisi IT, dan Divisi Keuangan
19. Klik node `Produksi`
20. Arahkan kursor ke tombol `[Edit]` yang Disabled pada Group Quota Summary
21. Verifikasi Group Quota Summary Produksi (di luar scope): `[Edit]` Disabled dengan tooltip `You don't have permission to edit.`

### TC-FA-LIC-101: Assignment tumpang tindih: grup yang di-assign tetapi descendant dari assignment lain dapat diedit (union)

22. Ganti akun: logout, lalu login sebagai Manage asset license tumpang tindih (Kantor Pusat dan Divisi Logistik) dengan `Spectra.env.FA_MAL_OVERLAP_PASSWORD`
23. Buka Tab `Allocation Quota`, lalu klik node `Divisi Logistik`
24. Verifikasi Divisi Logistik: `[Edit]` Show (descendant dari Kantor Pusat walau juga di-assign)
25. Klik node `Kantor Pusat`
26. Arahkan kursor ke tombol `[Edit]` pada Group Quota Summary
27. Verifikasi Kantor Pusat: `[Edit]` Disabled dengan tooltip `You don't have permission to edit.` (di-assign dan bukan descendant dari assignment lain)
28. Klik node `Gudang A`
29. Verifikasi Gudang A: `[Edit]` Show

### TC-FA-LIC-530: Group Manager dengan assignment tumpang tindih: Edit descendant lewat UI berhasil (union), grup level 1 Edit Disabled

30. Ganti akun: logout, lalu login sebagai Group Manager tumpang tindih (Kantor Pusat dan Divisi Logistik) dengan `Spectra.env.FA_GM_OVERLAP_PASSWORD`
31. Buka Tab `Allocation Quota`
32. Arahkan kursor ke tombol `[Edit]` pada baris grup level 1
33. Verifikasi tombol `[Edit]` pada grup level 1 berstatus Disabled dengan tooltip `You don't have permission to edit.`
34. Klik node `Kantor Pusat`
35. Verifikasi tombol `[Edit]` Divisi Logistik (ditugaskan dan descendant dari assignment Kantor Pusat) tampil
36. Klik `[Edit]` pada Divisi Logistik
37. Isi New Allocated Quota `650`
38. Klik `[Save]`
39. Verifikasi toast sukses `Success, group license quota updated.`
40. Verifikasi Allocated Quota Divisi Logistik = 650
41. Pulihkan Pre-setup #12 lewat fixture BE

## Notes

- Spec Role Matrix (bagian 3a konvensi) atas scope edit descendant yang memuat dua polaritas (Show dan Disabled dengan tooltip); ditulis per blok role karena langkah tiap role berbeda dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`): "Buka Tab `Allocation Quota`" setelah ganti akun, arahkan kursor, dan "Pulihkan Pre-setup #12".
- Spec di atas 35 langkah (41 langkah): seluruh blok adalah scope tombol Edit per role pada tab yang sama dan setiap akun berdiri sendiri; hanya TC-FA-LIC-530 mengubah data (Divisi Logistik), dan pemulihannya ditulis di blok itu.
- Temuan untuk QA:
  - TC-FA-LIC-99 butir Expected b dan c menyebut `[Edit]` Show pada baris child dan Group Quota Summary tanpa menyebut tooltip; spec mengasersi Show saja.
  - TC-FA-LIC-530 mengubah alokasi Divisi Logistik Pre-setup #12 (500 menjadi 650) tanpa menyebut pemulihan; pemulihan oleh fixture BE.

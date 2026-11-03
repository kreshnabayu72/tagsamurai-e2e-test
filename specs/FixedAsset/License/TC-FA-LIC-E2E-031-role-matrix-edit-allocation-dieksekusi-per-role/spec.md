---
id: TC-FA-LIC-E2E-031-role-matrix-edit-allocation-dieksekusi-per-role
title: "Role Matrix: Edit Allocation Dieksekusi Sukses per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-102
  - TC-FA-LIC-104
  - TC-FA-LIC-105
coverage:
  web: automated
---

# Role Matrix: Edit Allocation Dieksekusi Sukses per Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage asset license (Kantor Pusat) (Pre-setup #4): `manageAssetLicenseHQ_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_MAL_HQ_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun lain pada tabel "Role yang diuji" lewat langkah Ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; seluruh nama env pada tabel adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Role yang diuji (Tabel Data Uji Pre-setup #3, #4, #6):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-FA-LIC-102 | Manage asset license (Kantor Pusat) (Pre-setup #4) | `manageAssetLicenseHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAL_HQ_PASSWORD` |
| TC-FA-LIC-104 | Group Manager (Kantor Pusat) (Pre-setup #6) | `groupManagerHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_HQ_PASSWORD` |
| TC-FA-LIC-105 | Manage global license (Pre-setup #3) | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_PASSWORD` |

- Data Pre-setup #12 (`Fixture.fixedAssetLicense.kuotaHierarki`): hierarki Produksi, Kantor Pusat (Divisi Logistik (Gudang A), Divisi IT, Divisi Keuangan), Cabang Surabaya, Cabang Medan dengan alokasi, Used, dan Reserved sesuai Example Data PRD §4.1.3; disediakan tim FE/BE. Alokasi yang diedit: Divisi IT 100 (Used 60), Gudang A 100 (Used 100), Kantor Pusat level 1 1.500 (Unallocated Pool 200).
- S-06: target aksi tulis adalah alokasi grup Pre-setup #12 bernama literal yang hierarki dan kuotanya tidak dapat dimiliki spec. Alokasi Divisi IT, Gudang A, dan Kantor Pusat dipulihkan ke keadaan awal; pemulihan dijamin fixture BE (disediakan tim FE/BE, dinyatakan di `suite.md`) di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan Pre-setup #12"; efeknya (Last Updated grup, entri Changelog: Allocation Quota, System Log, dan Activity Log) tidak dipulihkan. Suite serial (`parallel: false`).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.

## Test Steps

### TC-FA-LIC-102: Manage asset license mengedit alokasi descendant sampai sukses

1. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
2. Klik `[Edit]` pada baris Divisi IT
3. Isi New Allocated Quota `120`
4. Klik `[Save]`
5. Verifikasi toast sukses `Success, group license quota updated.`
6. Verifikasi baris Divisi IT menampilkan Allocated Quota 120
7. Pulihkan Pre-setup #12 lewat fixture BE

### TC-FA-LIC-104: Group Manager mengedit alokasi descendant sampai sukses

8. Ganti akun: logout, lalu login sebagai Group Manager (Kantor Pusat) dengan `Spectra.env.FA_GM_HQ_PASSWORD`
9. Buka Tab `Allocation Quota`, lalu klik node `Divisi Logistik`
10. Klik `[Edit]` pada baris Gudang A
11. Isi New Allocated Quota `150`
12. Klik `[Save]`
13. Verifikasi toast sukses `Success, group license quota updated.`
14. Verifikasi Allocated Quota Gudang A = 150
15. Pulihkan Pre-setup #12 lewat fixture BE

### TC-FA-LIC-105: Manage global license mengedit alokasi grup level 1 sampai sukses

16. Ganti akun: logout, lalu login sebagai Manage global license dengan `Spectra.env.FA_MGL_PASSWORD`
17. Buka Tab `Allocation Quota`
18. Klik `[Edit]` di samping Allocated Quota Kantor Pusat pada node `All Groups`
19. Isi New Allocated Quota `1600`
20. Klik `[Save]`
21. Verifikasi toast sukses `Success, group license quota updated.`
22. Verifikasi Allocated Quota Kantor Pusat = 1600
23. Pulihkan Pre-setup #12 lewat fixture BE

## Notes

- Spec Role Matrix positif (bagian 3a konvensi) atas Edit Allocation yang dieksekusi; ditulis per blok role karena nilai, target grup, dan node berbeda per role dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`): "Buka Tab `Allocation Quota`" dan klik node setelah ganti akun, serta "Pulihkan Pre-setup #12" yang mengembalikan alokasi sebelum blok berikutnya.
- Temuan untuk QA:
  - TC-FA-LIC-102, 104, dan 105 mengedit alokasi Pre-setup #12 bernama literal tanpa menyebut pemulihan; pemulihan oleh fixture BE.

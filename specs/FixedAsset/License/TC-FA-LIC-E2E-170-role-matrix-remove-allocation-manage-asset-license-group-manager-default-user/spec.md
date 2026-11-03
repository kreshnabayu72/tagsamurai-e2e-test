---
id: TC-FA-LIC-E2E-170-role-matrix-remove-allocation-manage-asset-license-group-manager-default-user
title: "Role Matrix: Manage Asset License, Group Manager, dan Default User Menghapus Alokasi dengan Mengosongkan Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-103
  - TC-FA-LIC-528
  - TC-FA-LIC-529
coverage:
  web: automated
---

# Role Matrix: Manage Asset License, Group Manager, dan Default User Menghapus Alokasi dengan Mengosongkan Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun lain pada tabel "Role yang diuji" lewat langkah Ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; seluruh nama env pada tabel adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Role yang diuji (Tabel Data Uji Pre-setup #4, #6, #7):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-FA-LIC-103 | Manage asset license (Kantor Pusat) (Pre-setup #4) | `manageAssetLicenseHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAL_HQ_PASSWORD` |
| TC-FA-LIC-528 | Group Manager (Kantor Pusat) (Pre-setup #6) | `groupManagerHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_HQ_PASSWORD` |
| TC-FA-LIC-529 | Default User (Pre-setup #7) | `defaultUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` |

- Data Pre-setup #12 (`Fixture.fixedAssetLicense.kuotaHierarki`): hierarki Produksi, Kantor Pusat (Divisi Logistik (Gudang A), Divisi IT, Divisi Keuangan), Cabang Surabaya, Cabang Medan dengan alokasi, Used, dan Reserved sesuai Example Data PRD §4.1.3; disediakan tim FE/BE. Divisi IT beralokasi 100 tanpa subgroup.
- S-06: target aksi tulis adalah alokasi grup Pre-setup #12 bernama literal yang hierarki dan kuotanya tidak dapat dimiliki spec. Alokasi Divisi IT dipulihkan ke keadaan awal; pemulihan dijamin fixture BE (disediakan tim FE/BE, dinyatakan di `suite.md`) di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan Pre-setup #12"; efeknya (Last Updated grup, entri Changelog: Allocation Quota, System Log, dan Activity Log) tidak dipulihkan. Suite serial (`parallel: false`).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.

## Test Steps

### TC-FA-LIC-103: Manage asset license menghapus alokasi descendant dengan mengosongkan field

1. Ganti akun: logout, lalu login sebagai Manage asset license (Kantor Pusat) dengan `Spectra.env.FA_MAL_HQ_PASSWORD`
2. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
3. Klik `[Edit]` pada Divisi IT
4. Klik `[Clear Field]`
5. Klik `[Save]`
6. Verifikasi toast sukses `Success, group license allocation removed.`
7. Verifikasi Allocated Quota Divisi IT menjadi `—`
8. Pulihkan Pre-setup #12 lewat fixture BE

### TC-FA-LIC-528: Group Manager menghapus alokasi descendant dengan mengosongkan field

9. Ganti akun: logout, lalu login sebagai Group Manager (Kantor Pusat) dengan `Spectra.env.FA_GM_HQ_PASSWORD`
10. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
11. Klik `[Edit]` pada Divisi IT
12. Klik `[Clear Field]`
13. Klik `[Save]`
14. Verifikasi tidak ada dialog konfirmasi
15. Verifikasi modal Edit Allocation tertutup
16. Verifikasi toast sukses `Success, group license allocation removed.`
17. Verifikasi Allocated Quota Divisi IT menjadi `—`
18. Pulihkan Pre-setup #12 lewat fixture BE

### TC-FA-LIC-529: Default User menghapus alokasi grup dengan mengosongkan field

19. Ganti akun: logout, lalu login sebagai Default User dengan `Spectra.env.FA_DU_PASSWORD`
20. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
21. Klik `[Edit]` pada Divisi IT
22. Klik `[Clear Field]`
23. Klik `[Save]`
24. Verifikasi tidak ada dialog konfirmasi
25. Verifikasi modal Edit Allocation tertutup
26. Verifikasi toast sukses `Success, group license allocation removed.`
27. Verifikasi Allocated Quota Divisi IT menjadi `—`
28. Pulihkan Pre-setup #12 lewat fixture BE

## Notes

- Spec Role Matrix positif (bagian 3a konvensi) atas Remove Allocation; ditulis per blok role karena langkah tiap role berbeda dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`): "Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`" setelah ganti akun dan "Pulihkan Pre-setup #12".
- Temuan untuk QA:
  - TC-FA-LIC-103, 528, 529 menghapus alokasi Divisi IT Pre-setup #12 tanpa menyebut pemulihan; pemulihan oleh fixture BE.

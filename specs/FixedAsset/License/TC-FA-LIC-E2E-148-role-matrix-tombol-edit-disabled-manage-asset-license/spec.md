---
id: TC-FA-LIC-E2E-148-role-matrix-tombol-edit-disabled-manage-asset-license
title: "Role Matrix: Tombol Edit Disabled untuk Manage Asset License"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-106
  - TC-FA-LIC-597
coverage:
  web: automated
---

# Role Matrix: Tombol Edit Disabled untuk Manage Asset License

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage asset license tumpang tindih (Kantor Pusat dan Divisi Logistik) (Pre-setup #5): `manageAssetLicenseOverlap_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_MAL_OVERLAP_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun lain pada tabel "Role yang diuji" lewat langkah Ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; seluruh nama env pada tabel adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Role yang diuji (Tabel Data Uji Pre-setup #4, #5, #34):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-FA-LIC-106 | Manage asset license tumpang tindih (Kantor Pusat dan Divisi Logistik) (Pre-setup #5) | `manageAssetLicenseOverlap_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAL_OVERLAP_PASSWORD` |
| TC-FA-LIC-106 | Manage asset license (Kantor Pusat) (Pre-setup #4) | `manageAssetLicenseHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAL_HQ_PASSWORD` |
| TC-FA-LIC-597 | Manage asset license dimensi Read saja (Kantor Pusat) (Pre-setup #34) | `manageAssetLicenseRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAL_READ_PASSWORD` |

- Data Pre-setup #12 (`Fixture.fixedAssetLicense.kuotaHierarki`): hierarki Produksi, Kantor Pusat (Divisi Logistik (Gudang A), Divisi IT, Divisi Keuangan), Cabang Surabaya, Cabang Medan dengan alokasi, Used, dan Reserved sesuai Example Data PRD §4.1.3; disediakan tim FE/BE.
- Spec hanya mengamati tombol dan tooltip; tidak ada data yang diubah.
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.
- Suite serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-FA-LIC-106: Manage asset license tidak pernah dapat mengedit grup level 1

1. Buka Tab `Allocation Quota`
2. Arahkan kursor ke tombol `[Edit]` pada grup level 1 `Produksi`
3. Verifikasi tombol `[Edit]` pada `Produksi` berstatus Disabled (Manage asset license tumpang tindih)
4. Verifikasi tooltip `You don't have permission to edit.` tampil pada `Produksi`
5. Arahkan kursor ke tombol `[Edit]` pada grup level 1 `Kantor Pusat`
6. Verifikasi tombol `[Edit]` pada `Kantor Pusat` berstatus Disabled (Manage asset license tumpang tindih)
7. Verifikasi tooltip `You don't have permission to edit.` tampil pada `Kantor Pusat`
8. Arahkan kursor ke tombol `[Edit]` pada grup level 1 `Cabang Surabaya`
9. Verifikasi tombol `[Edit]` pada `Cabang Surabaya` berstatus Disabled (Manage asset license tumpang tindih)
10. Verifikasi tooltip `You don't have permission to edit.` tampil pada `Cabang Surabaya`
11. Arahkan kursor ke tombol `[Edit]` pada grup level 1 `Cabang Medan`
12. Verifikasi tombol `[Edit]` pada `Cabang Medan` berstatus Disabled (Manage asset license tumpang tindih)
13. Verifikasi tooltip `You don't have permission to edit.` tampil pada `Cabang Medan`
14. Klik tombol `[Edit]` pada `Produksi` yang Disabled
15. Verifikasi klik tidak membuka modal Edit Allocation
16. Ganti akun: logout, lalu login sebagai Manage asset license (Kantor Pusat) dengan `Spectra.env.FA_MAL_HQ_PASSWORD`
17. Buka Tab `Allocation Quota`
18. Arahkan kursor ke tombol `[Edit]` pada grup level 1 `Produksi`
19. Verifikasi tombol `[Edit]` pada `Produksi` berstatus Disabled (Manage asset license)
20. Verifikasi tooltip `You don't have permission to edit.` tampil pada `Produksi`
21. Arahkan kursor ke tombol `[Edit]` pada grup level 1 `Kantor Pusat`
22. Verifikasi tombol `[Edit]` pada `Kantor Pusat` berstatus Disabled (Manage asset license)
23. Verifikasi tooltip `You don't have permission to edit.` tampil pada `Kantor Pusat`
24. Arahkan kursor ke tombol `[Edit]` pada grup level 1 `Cabang Surabaya`
25. Verifikasi tombol `[Edit]` pada `Cabang Surabaya` berstatus Disabled (Manage asset license)
26. Verifikasi tooltip `You don't have permission to edit.` tampil pada `Cabang Surabaya`
27. Arahkan kursor ke tombol `[Edit]` pada grup level 1 `Cabang Medan`
28. Verifikasi tombol `[Edit]` pada `Cabang Medan` berstatus Disabled (Manage asset license)
29. Verifikasi tooltip `You don't have permission to edit.` tampil pada `Cabang Medan`
30. Klik tombol `[Edit]` pada `Produksi` yang Disabled
31. Verifikasi klik tidak membuka modal Edit Allocation

### TC-FA-LIC-597: Pemegang Manage asset license hanya dimensi Read: tombol Edit Disabled dengan tooltip `to do this` pada semua baris

32. Ganti akun: logout, lalu login sebagai Manage asset license dimensi Read saja (Kantor Pusat) dengan `Spectra.env.FA_MAL_READ_PASSWORD`
33. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
34. Verifikasi Tab Allocation Quota dan data terbaca lengkap (Show)
35. Arahkan kursor ke `[Edit]` Group Quota Summary Kantor Pusat
36. Verifikasi `[Edit]` Group Quota Summary Kantor Pusat tampil Disabled
37. Verifikasi tooltip `You don't have permission to do this.` tampil pada `[Edit]` Group Quota Summary Kantor Pusat
38. Arahkan kursor ke `[Edit]` baris child Divisi Logistik
39. Verifikasi `[Edit]` baris child Divisi Logistik tampil Disabled
40. Verifikasi tooltip `You don't have permission to do this.` tampil pada `[Edit]` baris child Divisi Logistik
41. Arahkan kursor ke `[Edit]` baris child Divisi IT
42. Verifikasi `[Edit]` baris child Divisi IT tampil Disabled
43. Verifikasi tooltip `You don't have permission to do this.` tampil pada `[Edit]` baris child Divisi IT
44. Arahkan kursor ke `[Edit]` baris child Divisi Keuangan
45. Verifikasi `[Edit]` baris child Divisi Keuangan tampil Disabled
46. Verifikasi tooltip `You don't have permission to do this.` tampil pada `[Edit]` baris child Divisi Keuangan
47. Klik `[Edit]` Divisi Logistik yang Disabled
48. Verifikasi klik tidak membuka modal Edit Allocation

## Notes

- Spec Role Matrix (bagian 3a konvensi) atas tombol Edit berpolaritas Disabled dengan tooltip; ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung: ganti akun (langkah 16 dan 32) dan "Buka Tab `Allocation Quota`" setelah ganti akun; hook `beforeEach` suite membuka halaman License saja.
- Spec di atas 35 langkah (48 langkah): alasan dipertahankan, TC-FA-LIC-106 dan 597 menetapkan hover satu per satu pada tiap elemen dan tooltip tiap elemen diasersi sebelum hover berpindah (8b.5), sehingga langkah hover dan `Verifikasi` berulang per grup level 1 (TC-FA-LIC-106, untuk dua akun) dan per tombol `[Edit]` (TC-FA-LIC-597).
- Temuan untuk QA:
  - Tooltip memakai dua teks berbeda: `You don't have permission to edit.` (Manage asset license di luar cakupan) dan `You don't have permission to do this.` (pemegang capability dimensi Read saja); spec mengikuti teks tiap TC.

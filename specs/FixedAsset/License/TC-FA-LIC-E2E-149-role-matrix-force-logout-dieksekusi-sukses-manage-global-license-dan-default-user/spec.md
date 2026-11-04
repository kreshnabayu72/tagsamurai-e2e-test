---
id: TC-FA-LIC-E2E-149-role-matrix-force-logout-dieksekusi-sukses-manage-global-license-dan-default-user
title: "Role Matrix Positif: Force Logout Dieksekusi Sukses oleh Manage Global License dan Default User"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-95
  - TC-FA-LIC-96
coverage:
  web: automated
---

# Role Matrix Positif: Force Logout Dieksekusi Sukses oleh Manage Global License dan Default User

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage global license (Pre-setup #3): `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_MGL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun lain pada tabel "Role yang diuji" lewat langkah Ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; seluruh nama env pada tabel adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Role yang diuji (Tabel Data Uji Pre-setup #3 dan #7):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-FA-LIC-95 | Manage global license (Pre-setup #3) | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_PASSWORD` |
| TC-FA-LIC-96 | Default User (Pre-setup #7) | `defaultUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` |

- Data Pre-setup #14 (`Fixture.fixedAssetLicense.sesiAktif`): 18 sesi aktif PT Sejahtera, seat 25, termasuk sesi Budi Santoso (akun login Budi Santoso disediakan tim FE); disediakan tim FE/BE.
- S-06: target Force Logout pada TC-FA-LIC-95 dan 96 adalah sesi Budi Santoso Pre-setup #14 yang tidak dapat dimiliki spec; pemulihan sesinya dijamin fixture BE (disediakan tim FE/BE, dinyatakan di `suite.md`) di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan sesi Budi Santoso"; efeknya (entri Changelog: Concurrent User, System Log, Activity Log) dicatat dan tidak dipulihkan. Suite serial (`parallel: false`).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.

## Test Steps

### TC-FA-LIC-95: Force Logout dieksekusi sukses oleh Manage global license (hak tunggal)

1. Buka License > Concurrent User
2. Catat nilai Online Users
3. Ketik Search `Budi Santoso`, tekan Enter
4. Klik `[Force Logout]` pada baris Budi Santoso
5. Klik `[Confirm Logout]`
6. Verifikasi toast sukses `Success, user session has been terminated.`
7. Verifikasi baris Budi Santoso hilang dari daftar
8. Verifikasi Online Users berkurang satu dari nilai yang dicatat
9. Pulihkan sesi Budi Santoso (Pre-setup #14) lewat fixture BE

### TC-FA-LIC-96: Force Logout dieksekusi sukses oleh Default User

10. Ganti akun: logout, lalu login sebagai Default User dengan `Spectra.env.FA_DU_PASSWORD`
11. Buka License > Concurrent User
12. Ketik Search `Budi Santoso`, tekan Enter
13. Klik `[Force Logout]` pada baris Budi Santoso
14. Klik `[Confirm Logout]`
15. Verifikasi toast sukses `Success, user session has been terminated.`
16. Verifikasi baris Budi Santoso hilang dari daftar

## Notes

- Spec Role Matrix positif (bagian 3a konvensi) atas eksekusi sukses Force Logout; ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Urutan blok: TC-FA-LIC-95 (Manage global license) lebih dulu, TC-FA-LIC-96 (Default User) terakhir. Visibilitas dan penolakan Force Logout per role (TC-FA-LIC-93, 94, 110, 596) ada di spec `TC-FA-LIC-E2E-028`.
- Langkah penghubung (aksi tanpa `Verifikasi`): "Buka License > Concurrent User", "Catat nilai Online Users", dan "Pulihkan sesi Budi Santoso" (langkah 9; S-09, sesi Budi Santoso dipulihkan sebelum blok TC-FA-LIC-96 bergantung padanya).
- Baris Budi Santoso di tabel Active Sessions (18 sesi, lebih dari satu halaman) dibuka lewat Search sebagai langkah penghubung (R-16, bagian 8b butir 13): langkah 3 dan 12. Ganti akun pada langkah 10 mereset Search.
- Temuan untuk QA:
  - Akun Budi Santoso (Pre-setup #14) tidak punya email di Pre-setup TC; disediakan tim FE.

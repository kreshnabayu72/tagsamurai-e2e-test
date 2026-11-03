---
id: TC-FA-LIC-E2E-026-role-matrix-visibilitas-menu-license-dan-direct-url
title: "Role Matrix: Visibilitas Menu License dan Akses URL Langsung per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-88
  - TC-FA-LIC-89
  - TC-FA-LIC-90
coverage:
  web: automated
---

# Role Matrix: Visibilitas Menu License dan Akses URL Langsung per Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun lain pada tabel "Role yang diuji" lewat langkah Ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; seluruh nama env pada tabel adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Role yang diuji (Tabel Data Uji Pre-setup #1, #2, #3, #4, #6, #7, #8):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-FA-LIC-88 | Total Control (Pre-setup #1) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| TC-FA-LIC-88 | Read Only (Pre-setup #2) | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
| TC-FA-LIC-88 | Manage global license (Pre-setup #3) | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_PASSWORD` |
| TC-FA-LIC-88 | Manage asset license (Kantor Pusat) (Pre-setup #4) | `manageAssetLicenseHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAL_HQ_PASSWORD` |
| TC-FA-LIC-88 | Group Manager (Kantor Pusat) (Pre-setup #6) | `groupManagerHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_HQ_PASSWORD` |
| TC-FA-LIC-88 | Default User (Pre-setup #7) | `defaultUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` |
| TC-FA-LIC-89, TC-FA-LIC-90 | Role lain tanpa capability License (Pre-setup #8) | `noCapability_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_NOCAP_PASSWORD` |

- Client Paid (PT Sejahtera, plan Professional, `License allocation per group` ON). Spec hanya membaca sidebar dan URL; tidak ada data yang diubah.
- Kemampuan teknis: mengetik URL di address bar browser (navigasi browser, bukan request HTTP langsung); URL halaman License disediakan tim FE.
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.
- Suite serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-FA-LIC-88: Menu License Show untuk Total Control, Read Only, Manage global license, Manage asset license, Group Manager, dan Default User

1. Verifikasi item `License` tampil pada sidebar Fixed Asset (Total Control)
2. Ganti akun: logout, lalu login sebagai Read Only dengan `Spectra.env.FA_RO_PASSWORD`
3. Verifikasi item `License` tampil pada sidebar Fixed Asset (Read Only)
4. Ganti akun: logout, lalu login sebagai Manage global license dengan `Spectra.env.FA_MGL_PASSWORD`
5. Verifikasi item `License` tampil pada sidebar Fixed Asset (Manage global license)
6. Ganti akun: logout, lalu login sebagai Manage asset license (Kantor Pusat) dengan `Spectra.env.FA_MAL_HQ_PASSWORD`
7. Verifikasi item `License` tampil pada sidebar Fixed Asset (Manage asset license)
8. Ganti akun: logout, lalu login sebagai Group Manager (Kantor Pusat) dengan `Spectra.env.FA_GM_HQ_PASSWORD`
9. Verifikasi item `License` tampil pada sidebar Fixed Asset (Group Manager)
10. Ganti akun: logout, lalu login sebagai Default User dengan `Spectra.env.FA_DU_PASSWORD`
11. Verifikasi item `License` tampil pada sidebar Fixed Asset (Default User)

### TC-FA-LIC-89: Menu License Hidden untuk role tanpa capability

12. Ganti akun: logout, lalu login sebagai Role lain tanpa capability License dengan `Spectra.env.FA_NOCAP_PASSWORD`
13. Verifikasi sidebar Fixed Asset tampil dengan item menu lain
14. Verifikasi item `License` tidak tampil sama sekali di sidebar

### TC-FA-LIC-90: Akses URL langsung License oleh role tanpa capability

15. Ketik URL halaman License langsung di address bar
16. Verifikasi toast error `You don't have permission to do this.` tampil
17. Verifikasi UI di-refresh sehingga elemen tidak berhak tersembunyi
18. Verifikasi tidak ada redirect ke halaman unauthorized terpisah
19. Verifikasi sidebar Fixed Asset tampil
20. Verifikasi halaman License tidak menampilkan data

## Notes

- Spec Role Matrix (bagian 3a konvensi) yang memuat dua polaritas (Show untuk enam role, Hidden untuk role tanpa capability); ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung: tiap "Ganti akun" mengganti akun aktor; TC-FA-LIC-88 mengamati sidebar setelah login tiap akun.
- Asersi "item `License` tidak tampil" didahului `Verifikasi sidebar Fixed Asset tampil dengan item menu lain` sebagai anchor positif; asersi "tidak menampilkan data" didahului `Verifikasi sidebar Fixed Asset tampil`.
- Temuan untuk QA:
  - TC-FA-LIC-90 tidak memberi URL literal halaman License dan tidak menyatakan halaman tujuan setelah toast; spec hanya mengasersi toast, UI di-refresh, tanpa redirect, dan tanpa data.
  - Klausa "UI di-refresh sehingga elemen tidak berhak tersembunyi" pada TC-FA-LIC-90 tidak menyebut elemen yang diamati; spec mengasersinya dari keadaan halaman setelah toast.

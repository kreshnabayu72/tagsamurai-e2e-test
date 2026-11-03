---
id: TC-FA-LIC-E2E-027-role-matrix-elemen-baca-license-tab-toolbar-banner-data
title: "Role Matrix: Elemen Baca License (Tab, Toolbar, Banner, dan Data) per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-91
  - TC-FA-LIC-92
  - TC-FA-LIC-108
  - TC-FA-LIC-109
  - TC-FA-LIC-485
coverage:
  web: automated
---

# Role Matrix: Elemen Baca License (Tab, Toolbar, Banner, dan Data) per Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun lain pada tabel "Role yang diuji" lewat langkah Ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; seluruh nama env pada tabel adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Role yang diuji (Tabel Data Uji Pre-setup #1, #2, #3, #4, #6):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-FA-LIC-91, TC-FA-LIC-108 | Total Control (Pre-setup #1) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| TC-FA-LIC-91, TC-FA-LIC-108 | Manage global license (Pre-setup #3) | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_PASSWORD` |
| TC-FA-LIC-91, TC-FA-LIC-108 | Manage asset license (Kantor Pusat) (Pre-setup #4) | `manageAssetLicenseHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAL_HQ_PASSWORD` |
| TC-FA-LIC-91, TC-FA-LIC-108 | Group Manager (Kantor Pusat) (Pre-setup #6) | `groupManagerHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_HQ_PASSWORD` |
| TC-FA-LIC-91, TC-FA-LIC-108, TC-FA-LIC-92, TC-FA-LIC-109, TC-FA-LIC-485 | Read Only (Pre-setup #2) | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |

- Client Paid (PT Sejahtera, plan Professional). Data Pre-setup #12 (`Fixture.fixedAssetLicense.kuotaHierarki`), #13 (`Fixture.fixedAssetLicense.riwayat`), #14 (`Fixture.fixedAssetLicense.sesiAktif`, profil Curated dengan Activation Status dan Temporary User), dan #15 (banner Notice, N = 30: tanggal fixture hari ini `01/12/26`) dibaca tanpa diubah selain tanggal fixture; disediakan tim FE/BE.
- Tanggal fixture hari ini diatur lewat fixture BE (jam server tidak digeser) dan dipulihkan di hook `after`.
- Setup Column: TC-FA-LIC-485 menyimpan konfigurasi kolom Tab Concurrent User untuk Read Only; hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`), kemampuan disediakan tim FE (dinyatakan di `suite.md`).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.
- Suite serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-FA-LIC-91 dan TC-FA-LIC-108: Tab, License Summary, dan banner Notice Show untuk kelima akun

1. Atur tanggal fixture hari ini ke `01/12/26` (N = 30) lewat fixture BE
2. Buka License > All License
3. Verifikasi Tab `All License`, `Allocation Quota`, `Concurrent User`, tabel License Summary, dan banner Notice tampil (Total Control)
4. Ganti akun: logout, lalu login sebagai Manage global license dengan `Spectra.env.FA_MGL_PASSWORD`
5. Buka License > All License
6. Verifikasi Tab `All License`, `Allocation Quota`, `Concurrent User`, tabel License Summary, dan banner Notice tampil (Manage global license)
7. Ganti akun: logout, lalu login sebagai Manage asset license (Kantor Pusat) dengan `Spectra.env.FA_MAL_HQ_PASSWORD`
8. Buka License > All License
9. Verifikasi Tab `All License`, `Allocation Quota`, `Concurrent User`, tabel License Summary, dan banner Notice tampil (Manage asset license)
10. Ganti akun: logout, lalu login sebagai Group Manager (Kantor Pusat) dengan `Spectra.env.FA_GM_HQ_PASSWORD`
11. Buka License > All License
12. Verifikasi Tab `All License`, `Allocation Quota`, `Concurrent User`, tabel License Summary, dan banner Notice tampil (Group Manager)
13. Ganti akun: logout, lalu login sebagai Read Only dengan `Spectra.env.FA_RO_PASSWORD`
14. Buka License > All License
15. Verifikasi Tab `All License`, `Allocation Quota`, `Concurrent User`, tabel License Summary, dan banner Notice tampil (Read Only)

### TC-FA-LIC-92: Toolbar TableTools dan tombol Download License Summary Show untuk Read Only

16. Verifikasi tombol Download License Summary tampil dan aktif
17. Verifikasi toolbar riwayat: Search, Filter, Download tampil dan aktif
18. Klik Tab `Concurrent User`
19. Verifikasi Tab Concurrent User: Search, Filter, Changelog aktif
20. Klik Tab `Allocation Quota`
21. Verifikasi Tab Allocation Quota: Search, Filter, Download, Changelog aktif

### TC-FA-LIC-109: Akses baca License oleh Read Only: data client-wide tampil lengkap

22. Klik Tab `All License`, lalu Sub-Tab `Subscription History`
23. Verifikasi tabel Subscription History menampilkan data client-wide tanpa pembatasan baris
24. Klik Sub-Tab `Allocation History`
25. Verifikasi tabel Allocation History menampilkan data client-wide tanpa pembatasan baris
26. Klik Tab `Allocation Quota`
27. Verifikasi tabel Tab Allocation Quota menampilkan data client-wide tanpa pembatasan baris
28. Verifikasi tidak ada kontrol tulis pada Tab Allocation Quota (tidak ada `[Edit]` dan tidak ada kontrol kosongkan field)
29. Klik Tab `Concurrent User`
30. Verifikasi tabel Tab Concurrent User menampilkan data client-wide tanpa pembatasan baris
31. Verifikasi tidak ada kontrol tulis pada Tab Concurrent User (tidak ada `[Force Logout]`)

### TC-FA-LIC-485: Kolom profil user di Tab Concurrent User tampil client-wide untuk Read Only tanpa mask

32. Verifikasi kolom Position dan Division tampil penuh untuk semua baris sesi, tidak dibatasi grup akun dan tanpa mask
33. Klik header kolom Column Visibility (⋯)
34. Klik item `Setup Column...`
35. Aktifkan kolom Activation Status dan Temporary User pada Popup Setup Column
36. Klik `[Save]`
37. Verifikasi kolom Activation Status dan Temporary User tampil dengan nilai penuh untuk semua baris
38. Verifikasi kolom Email tampil penuh (client-wide)

## Notes

- Spec Role Matrix (bagian 3a konvensi) atas visibilitas elemen baca; ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Urutan akun Total Control, Manage global license, Manage asset license, Group Manager, lalu Read Only dipilih supaya blok Read Only (TC-FA-LIC-92, 109, 485) berjalan pada sesi Read Only yang sama tanpa ganti akun tambahan.
- Pembagian TC: TC-FA-LIC-91 (elemen Tab, License Summary, dan banner) dan TC-FA-LIC-108 (banner Notice tampil untuk kelima akun) dijalankan dalam satu putaran akun; satu `Verifikasi` per akun memuat daftar elemen yang disebut utuh pada Expected kedua TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): penyetelan tanggal fixture dan "Buka License > All License" setelah ganti akun.
- Spec di atas 35 langkah (38 langkah): seluruh blok adalah visibilitas baca per role pada satu halaman, setiap akun berdiri sendiri; sekitar 16 langkah adalah ganti akun dan pembukaan halaman.
- Temuan untuk QA:
  - TC-FA-LIC-109 Expected "tanpa pembatasan baris" tidak menyebut jumlah baris acuan; spec mengasersinya sebagai data client-wide terbaca.
  - TC-FA-LIC-485 Expected tidak menyatakan daftar sel yang dibandingkan; spec mengasersi nilai penuh sesuai Expected.

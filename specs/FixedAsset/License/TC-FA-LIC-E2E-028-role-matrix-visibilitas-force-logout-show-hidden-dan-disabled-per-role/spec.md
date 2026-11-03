---
id: TC-FA-LIC-E2E-028-role-matrix-visibilitas-force-logout-show-hidden-dan-disabled-per-role
title: "Role Matrix: Visibilitas Force Logout Show, Hidden, dan Disabled per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-93
  - TC-FA-LIC-94
  - TC-FA-LIC-110
  - TC-FA-LIC-596
coverage:
  web: automated
---

# Role Matrix: Visibilitas Force Logout Show, Hidden, dan Disabled per Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun lain pada tabel "Role yang diuji" lewat langkah Ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; seluruh nama env pada tabel adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Role yang diuji (Tabel Data Uji Pre-setup #1, #2, #3, #4, #6, #34):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-FA-LIC-110, TC-FA-LIC-93 | Total Control (Pre-setup #1) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| TC-FA-LIC-93 | Manage global license (Pre-setup #3) | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_PASSWORD` |
| TC-FA-LIC-94 | Manage asset license (Kantor Pusat) (Pre-setup #4) | `manageAssetLicenseHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MAL_HQ_PASSWORD` |
| TC-FA-LIC-94 | Group Manager (Kantor Pusat) (Pre-setup #6) | `groupManagerHQ_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_HQ_PASSWORD` |
| TC-FA-LIC-94 | Read Only (Pre-setup #2) | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
| TC-FA-LIC-596 | Manage global license dimensi Read saja (Pre-setup #34) | `manageGlobalLicenseRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_READ_PASSWORD` |

- Data Pre-setup #14 (`Fixture.fixedAssetLicense.sesiAktif`, hanya dibaca): 18 sesi aktif PT Sejahtera, seat 25; disediakan tim FE/BE.
- Sesi kedua akun Total Control Pre-setup #1 di perangkat lain (dua sesi aktif akun yang sama) untuk TC-FA-LIC-93 dan TC-FA-LIC-110: dibuat lewat sesi API di hook `before` (disediakan tim FE/BE).
- Data Pre-setup #12 (dibaca untuk TC-FA-LIC-596) (`Fixture.fixedAssetLicense.kuotaHierarki`): hierarki Produksi, Kantor Pusat (Divisi Logistik (Gudang A), Divisi IT, Divisi Keuangan), Cabang Surabaya, Cabang Medan dengan alokasi, Used, dan Reserved sesuai Example Data PRD §4.1.3; disediakan tim FE/BE.
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-110: Aktor tanpa konflik mutasi mandiri: hak terhadap sesi sendiri tidak membuka Force Logout sendiri

1. Buka Tab `Concurrent User`
2. Verifikasi dua baris sesi milik akun sendiri tampil
3. Verifikasi kedua baris sesi milik aktor tidak memiliki tombol `[Force Logout]`

### TC-FA-LIC-93: Force Logout Show untuk Total Control dan Manage global license, Hidden pada baris sesi milik aktor sendiri

4. Verifikasi `[Force Logout]` tampil pada baris sesi pengguna lain (Total Control)
5. Verifikasi `[Force Logout]` tidak tampil pada baris sesi aktor sendiri, termasuk sesi aktor di perangkat lain (Total Control)
6. Ganti akun: logout, lalu login sebagai Manage global license dengan `Spectra.env.FA_MGL_PASSWORD`
7. Buka License > Concurrent User
8. Verifikasi `[Force Logout]` tampil pada baris sesi pengguna lain (Manage global license)
9. Verifikasi `[Force Logout]` tidak tampil pada baris sesi aktor sendiri, termasuk sesi aktor di perangkat lain (Manage global license)

### TC-FA-LIC-94: Force Logout Hidden untuk Manage asset license, Group Manager, dan Read Only

10. Ganti akun: logout, lalu login sebagai Manage asset license (Kantor Pusat) dengan `Spectra.env.FA_MAL_HQ_PASSWORD`
11. Buka License > Concurrent User
12. Verifikasi tidak ada tombol `[Force Logout]` pada semua baris (Manage asset license)
13. Ganti akun: logout, lalu login sebagai Group Manager (Kantor Pusat) dengan `Spectra.env.FA_GM_HQ_PASSWORD`
14. Buka License > Concurrent User
15. Verifikasi tidak ada tombol `[Force Logout]` (Group Manager)
16. Ganti akun: logout, lalu login sebagai Read Only dengan `Spectra.env.FA_RO_PASSWORD`
17. Buka License > Concurrent User
18. Verifikasi tidak ada tombol `[Force Logout]` (Read Only)
19. Verifikasi baris sesi tetap terbaca lengkap (Read client-wide)

### TC-FA-LIC-596: Pemegang Manage global license hanya dimensi Read: Force Logout dan Edit Disabled dengan tooltip izin

20. Ganti akun: logout, lalu login sebagai Manage global license dimensi Read saja dengan `Spectra.env.FA_MGL_READ_PASSWORD`
21. Buka License > Concurrent User
22. Verifikasi Tab, tabel, dan data License terbaca lengkap (Show)
23. Arahkan kursor ke `[Force Logout]` pada baris sesi pengguna lain
24. Verifikasi `[Force Logout]` tampil Disabled dengan tooltip `You don't have permission to do this.` pada baris sesi pengguna lain
25. Klik `[Force Logout]` yang Disabled
26. Verifikasi klik tidak membuka dialog `Force Logout User`
27. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
28. Arahkan kursor ke `[Edit]` pada baris Divisi Logistik
29. Verifikasi `[Edit]` tampil Disabled di samping `Total` dan `Allocated Quota` dengan tooltip `You don't have permission to do this.`
30. Klik `[Edit]` Divisi Logistik yang Disabled
31. Verifikasi klik tidak membuka modal Edit Allocation

## Notes

- Spec Role Matrix visibilitas (bagian 3a konvensi: matriks visibilitas per role, boleh memuat Show, Hidden, dan Disabled) atas Force Logout; ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Urutan blok: TC-FA-LIC-110 dan 93 pada Total Control lebih dulu, lalu TC-FA-LIC-94, dan TC-FA-LIC-596 terakhir. Eksekusi sukses Force Logout (TC-FA-LIC-95 dan 96) ada di spec `TC-FA-LIC-E2E-149`.
- Langkah penghubung (aksi tanpa `Verifikasi`): "Buka License > Concurrent User" setelah ganti akun.
- Asersi `[Force Logout]` tidak tampil didahului `Verifikasi` baris sesi tampil (TC-FA-LIC-110) atau `[Force Logout]` tampil pada baris pengguna lain (TC-FA-LIC-93) sebagai anchor positif.
- Temuan untuk QA:
  - TC-FA-LIC-94 Expected d ("Baris sesi tetap terbaca lengkap") tidak menyebut akun; spec mengasersinya pada akun terakhir (Read Only).
  - TC-FA-LIC-93 dan TC-FA-LIC-110 tidak memberi cara membuat sesi kedua aktor di perangkat lain; disediakan tim FE/BE lewat sesi API.

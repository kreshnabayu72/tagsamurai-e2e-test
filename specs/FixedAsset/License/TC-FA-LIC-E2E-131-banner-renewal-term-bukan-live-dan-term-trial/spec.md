---
id: TC-FA-LIC-E2E-131-banner-renewal-term-bukan-live-dan-term-trial
title: "Banner Renewal: Term Bukan Live dan Term Trial"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LIC-472
  - TC-FA-LIC-473
coverage:
  web: automated
---

# Banner Renewal: Term Bukan Live dan Term Trial

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`) untuk TC-FA-LIC-472, lalu Total Control client Pre-setup #24 (hanya term Trial Active, Trial Asset Quota 150; email tidak tertulis di Pre-setup TC, disediakan tim FE) untuk TC-FA-LIC-473 lewat langkah Ganti akun. Login akun pertama di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; kata sandi akun Pre-setup #24 memakai env `FA_TRIAL_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Data Pre-setup #15 (`Fixture.fixedAssetLicense.banner`): term live Active milik PT Sejahtera, Plan Owner `PT Maju Bersama` (Distributor), End Date 31/12/26, konfigurasi Client Lifecycle 30/7/1 (nilai bawaan), Grace End 30/01/27. Tanggal "hari ini" dan status term diatur lewat fixture BE (disediakan tim FE/BE, endpoint tidak dikarang); jam server tidak digeser. Fixture `fixedAssetLicense` adalah fixture baru yang isinya ditetapkan tim FE.
- Pre-setup #24 (`Fixture.fixedAssetLicense.bannerTrial`): client dengan hanya term Trial Active, Plan Owner `PT Maju Bersama`, End Date 31/12/26, konfigurasi Client Lifecycle 30/7/1 (nilai bawaan), Trial Asset Quota 150; disediakan tim FE/BE.
- Status term terbaru Purge, Deleted, Renewed, dan Converted untuk TC-FA-LIC-472 diatur lewat fixture BE; tidak ada term Active, Expired, atau Grace pada kondisi itu.
- State global: tanggal fixture hari ini, status term, Plan Owner, dan konfigurasi Client Lifecycle dipulihkan ke Pre-setup #15 di hook `after` (tetap jalan walau spec gagal di tengah).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.
- Suite serial (`parallel: false`, lihat `suite.md`): spec mengubah state global bersama (tanggal fixture, status term).

## Test Steps

### TC-FA-LIC-472: Banner: status Purge, Deleted, Renewed, atau Converted bukan term live sehingga tidak dirender

1. Atur tanggal fixture hari ini ke `01/03/27` lewat fixture BE
2. Ubah status term terbaru menjadi `Purge` lewat fixture BE
3. Buka License > All License
4. Verifikasi Tabs Bar tampil
5. Verifikasi banner tidak dirender pada status `Purge`
6. Ubah status term terbaru menjadi `Deleted` lewat fixture BE
7. Muat ulang halaman License
8. Verifikasi Tabs Bar tampil
9. Verifikasi banner tidak dirender pada status `Deleted`
10. Ubah status term terbaru menjadi `Renewed` lewat fixture BE
11. Muat ulang halaman License
12. Verifikasi Tabs Bar tampil
13. Verifikasi banner tidak dirender pada status `Renewed`
14. Ubah status term terbaru menjadi `Converted` lewat fixture BE
15. Muat ulang halaman License
16. Verifikasi Tabs Bar tampil
17. Verifikasi banner tidak dirender pada status `Converted`

### TC-FA-LIC-473: Banner tidak berlaku untuk term Trial

18. Ganti akun: logout, lalu login sebagai Total Control client Pre-setup #24 dengan `Spectra.env.FA_TRIAL_TC_PASSWORD`
19. Atur tanggal fixture hari ini ke `01/12/26` lewat fixture BE
20. Buka License > All License
21. Verifikasi Tabs Bar tampil
22. Verifikasi banner tidak dirender
23. Verifikasi tabel License Summary tetap dirender dengan Total kolom Asset = 150 (Trial Asset Quota; term Trial sebagai term live)

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): penyetelan tanggal fixture dan status term; "Muat ulang halaman License" memicu muat ulang banner tanpa jeda 60 detik.
- Asersi "banner tidak dirender" didahului `Verifikasi Tabs Bar tampil` sebagai anchor positif; anchor diulang setelah tiap muat ulang.
- TC-FA-LIC-473 berjalan terakhir karena membutuhkan Ganti akun ke client lain; TC-FA-LIC-472 tidak bergantung padanya.
- Temuan untuk QA:
  - TC-FA-LIC-473 precondition a menyebut login Total Control Pre-setup #1, sedangkan data b (Pre-setup #24) adalah client lain dengan hanya term Trial; spec memakai Total Control client Pre-setup #24, yang email dan kata sandinya tidak tertulis di Pre-setup TC.
  - TC-FA-LIC-472 tidak menyebut cara mengubah status term terbaru selain "fixture"; kontrak fixture disediakan tim FE/BE.

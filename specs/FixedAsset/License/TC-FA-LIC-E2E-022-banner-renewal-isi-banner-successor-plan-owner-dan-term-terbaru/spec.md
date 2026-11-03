---
id: TC-FA-LIC-E2E-022-banner-renewal-isi-banner-successor-plan-owner-dan-term-terbaru
title: "Banner Renewal: Isi Banner, Successor, Plan Owner, dan Term Terbaru"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-455
  - TC-FA-LIC-474
  - TC-FA-LIC-482
  - TC-FA-LIC-483
coverage:
  web: automated
---

# Banner Renewal: Isi Banner, Successor, Plan Owner, dan Term Terbaru

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup #15 (`Fixture.fixedAssetLicense.banner`): term live Active milik PT Sejahtera, Plan Owner `PT Maju Bersama` (Distributor), End Date 31/12/26, konfigurasi Client Lifecycle 30/7/1 (nilai bawaan), Grace End 30/01/27. Tanggal "hari ini" dan status term diatur lewat fixture BE (disediakan tim FE/BE, endpoint tidak dikarang); jam server tidak digeser. Fixture `fixedAssetLicense` adalah fixture baru yang isinya ditetapkan tim FE.
- Rantai Renewal untuk TC-FA-LIC-474 (Pre-setup #25): successor berstatus Waiting for Approval, Pending, dan Active; disediakan tim FE/BE lewat fixture BE (kontrak fixture tidak tertulis di TC). Pada TC-FA-LIC-483 term Renewed lama dan term Active berjalan tersedia lewat fixture BE. Plan Owner diganti menjadi `PT Baru Jaya` (Partner) untuk TC-FA-LIC-482.
- Jam browser (klien) tidak digeser; muat ulang banner dilakukan dengan memuat ulang halaman License.
- State global: tanggal fixture hari ini, status term, Plan Owner, dan konfigurasi Client Lifecycle dipulihkan ke Pre-setup #15 di hook `after` (tetap jalan walau spec gagal di tengah).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.
- Suite serial (`parallel: false`, lihat `suite.md`): spec mengubah state global bersama (tanggal fixture, status term).

## Test Steps

### TC-FA-LIC-455: Banner tidak memuat aksi Renew (batas Reflected)

1. Atur tanggal fixture hari ini ke `01/12/26` (N = 30) lewat fixture BE
2. Buka License > All License
3. Verifikasi banner hanya memuat ikon, Title, Body, dan `[×]`
4. Verifikasi banner tidak memuat tombol Renew atau tautan aksi

### TC-FA-LIC-483: Banner memakai term live terbaru bila ada beberapa term bersejarah

5. Atur tanggal fixture hari ini ke `01/12/26` (N = 30); riwayat: term Renewed lama dan term Active berjalan lewat fixture BE
6. Buka License > All License
7. Verifikasi hanya satu banner tampil, berdasarkan term Active berjalan (End Date 31/12/26) dan term Renewed tidak dipertimbangkan

### TC-FA-LIC-482: Plan Owner pada banner memakai nama entitas plain text

8. Atur tanggal fixture hari ini ke `01/12/26` (N = 30) lewat fixture BE
9. Ganti Plan Owner menjadi `PT Baru Jaya` (Partner) lewat fixture BE
10. Buka License > All License
11. Verifikasi Body banner Notice `Contact PT Baru Jaya to renew and keep your license and assets uninterrupted.` (tanpa tipe entitas)
12. Verifikasi `PT Baru Jaya` pada Body banner bukan tautan

### TC-FA-LIC-474: Successor Pending menyembunyikan banner; successor Waiting for Approval tidak; successor Active mengganti term live

13. Pulihkan Plan Owner menjadi `PT Maju Bersama` lewat fixture BE
14. Atur tanggal fixture hari ini ke `01/12/26` (N = 30) lewat fixture BE
15. Buka License > All License
16. Verifikasi banner Notice tampil
17. Buat successor Renewal berstatus `Waiting for Approval` lewat fixture BE
18. Muat ulang halaman License
19. Verifikasi banner Notice tetap tampil
20. Ubah successor Renewal menjadi `Pending` lewat fixture BE
21. Muat ulang halaman License
22. Verifikasi Tabs Bar tampil
23. Verifikasi banner tidak dirender
24. Atur tanggal fixture hari ini ke Start Date successor `01/01/27` sehingga successor `Active` dan term predecessor `Renewed` lewat fixture BE
25. Muat ulang halaman License
26. Verifikasi Tabs Bar tampil
27. Verifikasi term live baru dievaluasi sendiri: banner tidak dirender karena di luar jendela pengingat

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): penyetelan tanggal fixture, Plan Owner, dan status successor; "Pulihkan Plan Owner" mengembalikan Plan Owner Pre-setup #15 sebelum TC-FA-LIC-474; "Muat ulang halaman License" memicu muat ulang banner tanpa jeda 60 detik.
- Urutan blok: TC-FA-LIC-482 mendahului TC-FA-LIC-474 supaya Plan Owner dipulihkan sebelum rantai successor dibuat; TC-FA-LIC-474 terakhir karena mengubah status term.
- Asersi "banner tidak dirender" didahului `Verifikasi Tabs Bar tampil` sebagai anchor positif.
- TC-FA-LIC-474: tanggal Start Date successor 01/01/27 diambil dari rantai Renewal Pre-setup #25 (TC-FA-LIC-525).
- Temuan untuk QA:
  - TC-FA-LIC-455 berjudul "tidak mengambil data lain selain Admin Console (batas Reflected)" tetapi Expected hanya mengasersi isi banner; bagian pengambilan data tidak diasersi.
  - TC-FA-LIC-474 butir Expected d tidak menyebut tanggal; spec memakai Start Date successor 01/01/27 dari Pre-setup #25 sehingga N berada jauh di luar jendela pengingat.
  - TC-FA-LIC-483 tidak menyebut Title banner; spec tidak mengasersi Title.

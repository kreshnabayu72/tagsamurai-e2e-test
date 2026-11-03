---
id: TC-FA-LIC-E2E-122-aksi-manage-aset-unmanaged-kuota-grup-batas-sisa-slot
title: "Aksi Manage Aset Unmanaged terhadap Kuota Grup: Batas Sisa Slot, Ditolak Seluruhnya, dan Reserved"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-497
  - TC-FA-LIC-498
  - TC-FA-LIC-499
  - TC-FA-LIC-500
  - TC-FA-LIC-501
coverage:
  web: automated
---

# Aksi Manage Aset Unmanaged terhadap Kuota Grup: Batas Sisa Slot, Ditolak Seluruhnya, dan Reserved

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki, alokasi grup, kuota, dan status aset dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #12 (License Summary Total 5.000, Used 4320, Reserved 15, Remaining 665, Unmanaged 27; Divisi IT beralokasi 100; Gudang A beralokasi 100) dan #28 (aset Unmanaged: 6 di Divisi IT dan 5 di Gudang A; pemicu aksi Manage sesuai PRD `asset/`). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-500 Divisi IT Used by This Group 97 (Remaining 3) dan 4 aset Unmanaged di Divisi IT; blok TC-FA-LIC-501 Gudang A Used by This Group 100 (Remaining 0) dan 1 aset Unmanaged di Gudang A; blok TC-FA-LIC-499 Divisi IT Used by This Group 97 (Remaining 3) dan 3 aset Unmanaged di Divisi IT; blok TC-FA-LIC-497 Divisi IT Used by This Group 60, Reserved by This Group 0, Remaining 40, dan 1 aset Unmanaged di Divisi IT; blok TC-FA-LIC-498 kondisi yang sama dengan 3 aset Unmanaged di Divisi IT.
- Blok TC-FA-LIC-497, TC-FA-LIC-498, dan TC-FA-LIC-499 (asersi Reserved dari Manage) berlaku setelah `asset/` menetapkan penanda aset dalam transisi Manage (PRD License §12 Open Item #1); selama belum ditetapkan, Reserved dari Manage bernilai 0 dan seluruh aset Unmanaged dihitung pada baris Unmanaged (TC-FA-LIC-612). Pemicu aksi Manage dan penyebab penolakannya dimiliki PRD `asset/` yang belum memuat aksi itu; kemampuan memicunya disediakan tim FE.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup dan aset Pre-setup #12 dan #28 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Used, Reserved, Unmanaged, dan Remaining, status aset, dan Last Updated berubah; fixture memulihkannya. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: intercept jaringan yang mengamati respons pemeriksaan kuota `check_group_quota()` (kode hasil dan `qty_to_add`), dipasang sebelum aksi Manage dan dilepas segera sesudah pengamatan.

## Test Steps

### TC-FA-LIC-500: Aksi Manage satu aset di atas sisa slot (Remaining 3, qty_to_add 4) ditolak seluruhnya

1. Jalankan fixture BE pemulih Pre-setup #12 dengan Divisi IT Used by This Group `97` (Remaining 3) dan 4 aset Unmanaged di Divisi IT hingga tersimpan
2. Buka License > All License; catat Reserved dan Unmanaged pada License Summary kolom Asset
3. Pasang intercept jaringan yang mengamati respons pemeriksaan kuota
4. Jalankan aksi Manage atas 4 aset Unmanaged di Divisi IT dalam satu aksi sesuai PRD `asset/`
5. Verifikasi pemeriksaan kuota dengan `qty_to_add` `4` terhadap Remaining 3 mengembalikan `QUOTA_EXCEEDED`
6. Verifikasi seluruh aksi ditolak dengan pesan `Group quota exceeded. Available slots: 3. Please contact administrator to increase quota.` pada surface aksi Manage (sesuai PRD `asset/`)
7. Lepas intercept jaringan
8. Muat ulang License > All License
9. Verifikasi Reserved dan Unmanaged pada License Summary tidak berubah dibanding nilai pada langkah 2 (tidak ada aset yang diproses, termasuk 3 aset yang masih muat)
10. Buka License > Allocation Quota > node `Divisi IT`
11. Verifikasi Divisi IT: Reserved by This Group `0` dan Remaining `3`

### TC-FA-LIC-501: Aksi Manage ke grup beralokasi yang penuh (Remaining 0) ditolak QUOTA_EXCEEDED

12. Jalankan fixture BE pemulih Pre-setup #12 dengan Gudang A Used by This Group `100` (Remaining 0) dan 1 aset Unmanaged di Gudang A hingga tersimpan
13. Buka License > All License; catat Reserved dan Unmanaged pada License Summary kolom Asset
14. Pasang intercept jaringan yang mengamati respons pemeriksaan kuota
15. Jalankan aksi Manage atas 1 aset Unmanaged di Gudang A sesuai PRD `asset/`
16. Verifikasi pemeriksaan kuota mengembalikan `QUOTA_EXCEEDED`
17. Verifikasi aksi ditolak dengan pesan `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.` pada surface aksi Manage (sesuai PRD `asset/`)
18. Lepas intercept jaringan
19. Muat ulang License > All License
20. Verifikasi aset tetap Unmanaged: Reserved dan Unmanaged pada License Summary tidak berubah dibanding nilai pada langkah 13
21. Buka License > Allocation Quota > node `Gudang A`
22. Verifikasi Gudang A: Used by This Group `100`, Reserved by This Group `0`, dan Remaining `0`

### TC-FA-LIC-499: Aksi Manage tepat sebesar sisa slot grup (Remaining 3, qty_to_add 3) diterima

23. Jalankan fixture BE pemulih Pre-setup #12 dengan Divisi IT Used by This Group `97` (Remaining 3) dan 3 aset Unmanaged di Divisi IT hingga tersimpan
24. Pasang intercept jaringan yang mengamati respons pemeriksaan kuota
25. Buka License > Allocation Quota > node `Divisi IT`; catat Remaining
26. Jalankan aksi Manage atas 3 aset Unmanaged di Divisi IT sesuai PRD `asset/`
27. Verifikasi pemeriksaan kuota dengan `qty_to_add` `3` terhadap Remaining 3 mengembalikan `OK` (tepat di batas kuota)
28. Lepas intercept jaringan
29. Muat ulang node `Divisi IT`
30. Verifikasi aksi diterima
31. Verifikasi Divisi IT: Reserved by This Group `3`, Used by This Group `97`, dan Remaining `0`

### TC-FA-LIC-497: Aksi Manage 1 aset Unmanaged ke grup beralokasi dengan sisa cukup

32. Jalankan fixture BE pemulih Pre-setup #12 dengan Divisi IT beralokasi 100 (Used by This Group 60, Reserved by This Group 0, Remaining 40) dan 1 aset Unmanaged di Divisi IT hingga tersimpan
33. Buka License > All License; catat Total, Used, Reserved, Remaining, dan Unmanaged pada License Summary kolom Asset
34. Buka License > Allocation Quota > node `Divisi IT`; catat Used by This Group, Reserved by This Group, dan Remaining
35. Pasang intercept jaringan yang mengamati respons pemeriksaan kuota
36. Jalankan aksi Manage atas 1 aset Unmanaged di Divisi IT sesuai PRD `asset/`
37. Verifikasi pemeriksaan kuota Divisi IT dengan `qty_to_add` `1` mengembalikan `OK` (diamati lewat respons API)
38. Lepas intercept jaringan
39. Muat ulang License > All License
40. Verifikasi License Summary: Reserved `16`, Used `4320` (tidak berubah), Remaining `664`, dan Unmanaged `26` (aset dalam transisi tidak dihitung Unmanaged)
41. Buka License > Allocation Quota > node `Divisi IT`
42. Verifikasi Divisi IT: Used by This Group `60`, Reserved by This Group `1`, dan Remaining `39`

### TC-FA-LIC-498: Aksi Manage 3 aset di satu grup memeriksa kuota sekali dengan qty_to_add 3

43. Jalankan fixture BE pemulih Pre-setup #12 dengan Divisi IT Used by This Group 60 dan 3 aset Unmanaged di Divisi IT hingga tersimpan
44. Buka License > All License; catat Reserved, Remaining, dan Unmanaged pada License Summary kolom Asset
45. Pasang intercept jaringan yang mengamati respons pemeriksaan kuota
46. Jalankan aksi Manage atas 3 aset Unmanaged di Divisi IT dalam satu aksi sesuai PRD `asset/`
47. Verifikasi pemeriksaan kuota dipanggil sekali untuk Divisi IT dengan `qty_to_add` `3` dan mengembalikan `OK` (diamati lewat respons API)
48. Lepas intercept jaringan
49. Muat ulang License > All License
50. Verifikasi License Summary: Reserved `18`, Used `4320`, Remaining `662`, dan Unmanaged `24`
51. Buka License > Allocation Quota > node `Divisi IT`
52. Verifikasi Divisi IT: Reserved by This Group `3` dan Remaining `37`
53. Jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 12, 23, 32, 43, dan 53 (fixture BE pemulih dan penyetel state), pemasangan dan pelepasan intercept (langkah 3, 7, 14, 18, 24, 28, 35, 38, 45, dan 48), muat ulang halaman, navigasi License, serta pencatatan baseline pada langkah 2, 13, 25, 33, 34, dan 44 (S-12).
- Urutan TC diubah dari urutan nomor: TC-FA-LIC-500 dan TC-FA-LIC-501 (penolakan) lebih dulu, lalu TC-FA-LIC-499, TC-FA-LIC-497, dan TC-FA-LIC-498 yang menerima aksi Manage (S-10).
- Alasan di atas sekitar 35 langkah (53 langkah): semua blok satu topik (aksi Manage terhadap `check_group_quota()` pada satu grup) dan berdiri sendiri dengan fixture sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya intercept, pembacaan baseline, dan pemulihan fixture.
- Temuan untuk QA:
  - Pemicu aksi Manage ("sesuai PRD `asset/`") belum tertulis di PRD `asset/` (GAP-695); spec memakai kalimat TC tanpa mengarang langkah UI, dan eksekusi menunggu kemampuan pemicu dari tim FE.
  - TC-FA-LIC-499 langkah 1 menyebut Remaining dicatat tanpa Expected; nilai itu hanya dicatat.
  - TC-FA-LIC-497, TC-FA-LIC-498, dan TC-FA-LIC-499 mengasersi Reserved dari Manage yang bergantung pada penanda transisi Manage (Open Item #1).

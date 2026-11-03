---
id: TC-FA-LIC-E2E-123-aksi-manage-grup-tanpa-alokasi-over-used-gagal-diproses
title: "Aksi Manage: Grup Tanpa Alokasi, Over-used, Gagal Diproses, dan Jeda managed_transition_time"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-503
  - TC-FA-LIC-504
  - TC-FA-LIC-506
  - TC-FA-LIC-507
  - TC-FA-LIC-508
coverage:
  web: automated
---

# Aksi Manage: Grup Tanpa Alokasi, Over-used, Gagal Diproses, dan Jeda managed_transition_time

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki, alokasi grup, kuota, status aset, dan jam fixture dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #12 (License Summary Reserved 15, Used 4320, Remaining 665, Unmanaged 27; Kantor Pusat dengan Divisi Keuangan belum beralokasi; Divisi IT beralokasi 100) dan #28 (aset Unmanaged: 6 di Divisi IT dan 2 di Divisi Keuangan; pemicu aksi Manage dan penyebab kegagalan pemrosesan sesuai PRD `asset/`). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-504 Remaining Kantor Pusat 0 dan 1 aset Unmanaged di Divisi Keuangan; blok TC-FA-LIC-506 Divisi IT beralokasi 100 dengan Used by This Group 98 dan 3 aset Waiting for Approval (Reserved by This Group 3) sehingga hasil rumus Remaining −1, serta 1 aset Unmanaged di Divisi IT; blok TC-FA-LIC-507 Divisi IT Used by This Group 60, Remaining 40, 2 aset Unmanaged di Divisi IT, dan pemrosesan aset digagalkan fixture BE (penyebab dan penanda gagal sesuai PRD `asset/`); blok TC-FA-LIC-503 Remaining Kantor Pusat 200 dan 1 aset Unmanaged di Divisi Keuangan; blok TC-FA-LIC-508 `managed_transition_time` 24 jam (nilai bawaan `plans-licensing-config.md`), jam fixture T, Divisi IT Used by This Group 60, Remaining 40, dan 1 aset Unmanaged di Divisi IT.
- Blok TC-FA-LIC-503, TC-FA-LIC-507, dan TC-FA-LIC-508 (asersi Reserved dari Manage) berlaku setelah `asset/` menetapkan penanda aset dalam transisi Manage (PRD License §12 Open Item #1); selama belum ditetapkan, Reserved dari Manage bernilai 0 dan seluruh aset Unmanaged dihitung pada baris Unmanaged (TC-FA-LIC-612). Pemicu aksi Manage disediakan tim FE.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup dan aset Pre-setup #12 dan #28 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Used, Reserved, Unmanaged, dan Remaining, status aset, jam fixture, dan Last Updated berubah; fixture memulihkannya. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: intercept jaringan yang mengamati respons pemeriksaan kuota `check_group_quota()` (kode hasil), dipasang sebelum aksi Manage dan dilepas segera sesudah pengamatan. Jam fixture digeser maju pada blok TC-FA-LIC-508: sesi UI dan sesi API aktor tetap valid selama jam digeser (dinyatakan di `suite.md`) dan jam dipulihkan pada langkah 57 serta di hook `after`. Penantian hasil eventual memakai muat ulang halaman tiap 5 detik dengan batas tunggu 2 menit.

## Test Steps

### TC-FA-LIC-504: Aksi Manage ke grup tanpa alokasi ditolak saat Remaining leluhur habis

1. Jalankan fixture BE pemulih Pre-setup #12 dengan Remaining Kantor Pusat `0` dan 1 aset Unmanaged di Divisi Keuangan hingga tersimpan
2. Pasang intercept jaringan yang mengamati respons pemeriksaan kuota
3. Jalankan aksi Manage atas 1 aset Unmanaged di Divisi Keuangan sesuai PRD `asset/`
4. Verifikasi pemeriksaan kuota terhadap Remaining Kantor Pusat mengembalikan `QUOTA_EXCEEDED`
5. Verifikasi aksi ditolak dengan pesan `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`
6. Lepas intercept jaringan
7. Buka License > Allocation Quota > node `Divisi Keuangan`
8. Verifikasi Reserved by This Group Divisi Keuangan `0`
9. Klik node `Kantor Pusat` di Sidebar
10. Verifikasi Remaining Kantor Pusat tetap `0`

### TC-FA-LIC-506: Aksi Manage ke grup yang pemakaiannya melampaui Allocated Quota ditolak dengan sisa slot 0

11. Jalankan fixture BE pemulih Pre-setup #12 dengan Divisi IT beralokasi 100, Used by This Group 98, 3 aset Waiting for Approval, dan 1 aset Unmanaged di Divisi IT hingga tersimpan
12. Buka License > Allocation Quota > node `Divisi IT`
13. Verifikasi Remaining Divisi IT `0` (bukan nilai negatif)
14. Pasang intercept jaringan yang mengamati respons pemeriksaan kuota
15. Jalankan aksi Manage atas 1 aset Unmanaged di Divisi IT sesuai PRD `asset/`
16. Verifikasi aksi ditolak `QUOTA_EXCEEDED`
17. Verifikasi pesan `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`
18. Lepas intercept jaringan
19. Muat ulang node `Divisi IT`
20. Verifikasi Reserved by This Group Divisi IT tetap `3`

### TC-FA-LIC-507: Aksi Manage yang gagal diproses melepas Reserved dan aset tetap Unmanaged

21. Jalankan fixture BE pemulih Pre-setup #12 dengan Divisi IT Used by This Group 60 (Remaining 40), 2 aset Unmanaged di Divisi IT, dan pemrosesan aset digagalkan hingga tersimpan
22. Buka License > All License; catat Reserved, Used, Remaining, dan Unmanaged pada License Summary kolom Asset
23. Jalankan aksi Manage atas 2 aset Unmanaged di Divisi IT sesuai PRD `asset/`
24. Muat ulang License > All License
25. Verifikasi aksi lolos pemeriksaan kuota: License Summary Reserved `17`, Remaining `663`, dan Unmanaged `25`
26. Buka License > Allocation Quota > node `Divisi IT` (aset dalam jeda transisi)
27. Verifikasi Divisi IT: Reserved by This Group `2` dan Remaining `38`
28. Picu kegagalan pemrosesan kedua aset lewat fixture BE hingga tersimpan
29. Muat ulang License > All License
30. Verifikasi setelah pemrosesan gagal, License Summary: Reserved `15`, Used `4320`, Remaining `665`, dan Unmanaged `27`
31. Buka License > Allocation Quota > node `Divisi IT`
32. Verifikasi Divisi IT: Reserved by This Group `0` dan Remaining `40`
33. Buka daftar aset
34. Verifikasi kedua aset tetap berstatus Unmanaged

### TC-FA-LIC-503: Aksi Manage ke grup tanpa alokasi mengurangi Remaining leluhur beralokasi terdekat

35. Jalankan fixture BE pemulih Pre-setup #12 dengan Remaining Kantor Pusat `200` dan 1 aset Unmanaged di Divisi Keuangan hingga tersimpan
36. Pasang intercept jaringan yang mengamati respons pemeriksaan kuota
37. Jalankan aksi Manage atas 1 aset Unmanaged di Divisi Keuangan sesuai PRD `asset/`
38. Verifikasi pemeriksaan kuota terhadap Remaining Kantor Pusat (leluhur beralokasi terdekat) mengembalikan `OK`
39. Verifikasi aksi diterima
40. Lepas intercept jaringan
41. Buka License > Allocation Quota > node `Divisi Keuangan`
42. Verifikasi Divisi Keuangan: Reserved by This Group `1` dan Remaining `199` (mengikuti Kantor Pusat)
43. Klik node `Kantor Pusat` di Sidebar
44. Verifikasi Kantor Pusat: Allocated to Subgroups `601` dan Remaining `199`

### TC-FA-LIC-508: Jeda managed_transition_time, Reserved ditahan selama jeda dan menjadi Used saat aset managed kembali

45. Jalankan fixture BE pemulih Pre-setup #12 dengan `managed_transition_time` 24 jam, jam fixture T, Divisi IT Used by This Group 60 (Remaining 40), dan 1 aset Unmanaged di Divisi IT hingga tersimpan
46. Jalankan aksi Manage atas 1 aset Unmanaged di Divisi IT pada jam fixture T sesuai PRD `asset/`
47. Majukan jam fixture ke T + 12 jam
48. Muat ulang License > All License
49. Verifikasi pada T + 12 jam, License Summary: Reserved `16`, Used `4320`, Remaining `664`, dan Unmanaged `26`
50. Buka License > Allocation Quota > node `Divisi IT`
51. Verifikasi Divisi IT: Reserved by This Group `1`
52. Majukan jam fixture melewati T + `managed_transition_time`
53. Muat ulang License > All License tiap 5 detik sampai pemrosesan aset selesai (aset berstatus Active; batas tunggu 2 menit)
54. Verifikasi setelah transisi selesai, License Summary: Reserved `15`, Used `4321`, Remaining `664` (tidak berubah dari langkah 49), dan Unmanaged `26`
55. Buka License > Allocation Quota > node `Divisi IT`
56. Verifikasi Divisi IT: Reserved by This Group `0`, Used by This Group `61`, dan Remaining `39`
57. Pulihkan jam fixture dan jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 11, 21, 35, 45, dan 57 (fixture BE pemulih dan penyetel state), pemasangan dan pelepasan intercept (langkah 2, 6, 14, 18, 36, dan 40), langkah 28 (memicu kegagalan pemrosesan), langkah 33 (membuka daftar aset), langkah 47 dan 52 (menggeser jam fixture), muat ulang halaman, navigasi License, serta pencatatan baseline pada langkah 22.
- Urutan TC diubah dari urutan nomor: TC-FA-LIC-504 dan TC-FA-LIC-506 (penolakan) lebih dulu, lalu TC-FA-LIC-507, TC-FA-LIC-503, dan TC-FA-LIC-508 yang menerima aksi Manage (S-10).
- Alasan di atas sekitar 35 langkah (57 langkah): semua blok satu topik (aksi Manage terhadap kuota grup tanpa alokasi, over-used, kegagalan pemrosesan, dan jeda transisi) dan berdiri sendiri dengan fixture sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya intercept, navigasi, dan pemulihan fixture.
- Temuan untuk QA:
  - Pemicu aksi Manage dan penyebab kegagalan pemrosesan ("sesuai PRD `asset/`") belum tertulis di PRD `asset/` (GAP-695); spec mengikuti kalimat TC tanpa mengarang langkah UI.
  - TC-FA-LIC-504, TC-FA-LIC-506, dan TC-FA-LIC-503 tidak menyebut cara mengamati kode `QUOTA_EXCEEDED` atau `OK`; spec memakai intercept jaringan seperti TC-FA-LIC-497 sampai TC-FA-LIC-501 (diamati lewat respons API).
  - TC-FA-LIC-507 langkah 2 dan Expected a menyebut "aset dalam jeda transisi" tanpa tempat mengamatinya selain nilai Reserved; spec hanya mengasersi nilai itu.
  - TC-FA-LIC-507 Expected c tidak menyebut tempat mengamati status Unmanaged; spec memakai daftar aset.

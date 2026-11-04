---
id: TC-FA-LIC-E2E-120-unmanaged-transisi-manage-dan-konsistensi-used
title: "Aset Unmanaged, Transisi Manage, dan Konsistensi Used pada License Summary"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-401
  - TC-FA-LIC-402
  - TC-FA-LIC-403
  - TC-FA-LIC-404
  - TC-FA-LIC-493
coverage:
  web: automated
---

# Aset Unmanaged, Transisi Manage, dan Konsistensi Used pada License Summary

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
- Data Pre-setup: #12 (License Summary Reserved 15, Used 4320, Remaining 665, Unmanaged 27; Divisi IT), #20 (aset Active dan aset Waiting for Approval untuk Approve dan Delete), dan #28 (aset Unmanaged dan aset dalam transisi Manage; pemicu dan penyebab sesuai PRD `asset/`). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-401 sekurangnya dua aset Active yang dapat ditandai Unmanaged; blok TC-FA-LIC-402 tiga aset Unmanaged dalam jeda transisi Manage di Divisi IT; blok TC-FA-LIC-403 ketiga aset itu menyelesaikan transisi dan menjadi Active (managed kembali); blok TC-FA-LIC-493 client Paid dengan Used 100, Reserved 0, dan Unmanaged 3 termasuk satu aset dalam transisi Manage ke Divisi IT (aksi Manage tidak dieksekusi di spec ini); blok TC-FA-LIC-404 aset Waiting for Approval pada plan Paid.
- Blok TC-FA-LIC-402, TC-FA-LIC-403, dan TC-FA-LIC-493 berlaku setelah `asset/` menetapkan penanda aset dalam transisi Manage (PRD License §12 Open Item #1); selama belum ditetapkan, Reserved dari Manage bernilai 0 dan seluruh aset Unmanaged dihitung pada baris Unmanaged (TC-FA-LIC-612). Kemampuan memicu dan menyelesaikan transisi Manage disediakan tim FE.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup dan aset Pre-setup #12, #20, dan #28 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Used, Reserved, Unmanaged, dan Remaining, status aset, dan Last Updated berubah; fixture memulihkannya. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.

## Test Steps

### TC-FA-LIC-401: Aset Unmanaged tidak dihitung Used dan menambah baris Unmanaged

1. Jalankan fixture BE pemulih Pre-setup #12 dengan sekurangnya dua aset Active hingga tersimpan
2. Buka License > All License; catat Used, Remaining, dan Unmanaged pada License Summary kolom Asset
3. Tandai 2 aset Active sebagai Unmanaged lewat fixture BE hingga tersimpan
4. Muat ulang halaman License
5. Verifikasi Used turun 2, Remaining naik 2, dan Unmanaged naik 2 dibanding nilai pada langkah 2

### TC-FA-LIC-402: Aset dalam jeda transisi Manage dihitung Reserved

6. Jalankan fixture BE pemulih Pre-setup #12 dengan 3 aset Unmanaged dalam jeda transisi Manage di Divisi IT hingga tersimpan
7. Buka License > All License
8. Verifikasi License Summary kolom Asset: Reserved `18`, Remaining `662`, dan Used `4320` (tidak berubah)
9. Catat Unmanaged pada License Summary kolom Asset
10. Buka License > Allocation Quota > node `Divisi IT`
11. Verifikasi Divisi IT: Reserved by This Group `3` dan Remaining Quota `37`

### TC-FA-LIC-403: Aset yang selesai transisi Manage menjadi Active dan Reserved menjadi Used

12. Jalankan fixture BE yang mengubah 3 aset dalam transisi menjadi Active (managed kembali) hingga tersimpan
13. Muat ulang License > All License
14. Verifikasi Reserved turun 3 dan Used naik 3 dibanding nilai pada langkah 8
15. Verifikasi Remaining tidak berubah dibanding nilai pada langkah 8
16. Verifikasi Unmanaged tidak mencakup aset tersebut: nilai sama dengan langkah 9

### TC-FA-LIC-493: Transisi Manage selesai, Reserved menjadi Used, dan aset transisi tidak masuk hitungan Unmanaged

17. Jalankan fixture BE: client Paid dengan Used 100, Reserved 0, dan Unmanaged 3 termasuk 1 aset dalam transisi Manage ke Divisi IT hingga tersimpan
18. Buka License > All License; catat Remaining pada License Summary kolom Asset
19. Verifikasi selama transisi: Reserved `1`, Used `100`, dan Unmanaged `2` (aset transisi tidak dihitung Unmanaged)
20. Buka License > Allocation Quota > node `Divisi IT`; catat Used by This Group
21. Verifikasi Reserved by This Group Divisi IT `1`
22. Jalankan fixture BE yang menyelesaikan transisi Manage hingga tersimpan
23. Muat ulang License > All License
24. Verifikasi setelah transisi selesai: Reserved `0`, Used `101`, dan Unmanaged `2`
25. Verifikasi Remaining tenant tidak berubah dibanding nilai pada langkah 18
26. Buka License > Allocation Quota > node `Divisi IT`
27. Verifikasi Reserved by This Group `0` dan Used by This Group bertambah satu dibanding nilai pada langkah 20

### TC-FA-LIC-404: Used pada License Summary konsisten segera setelah Approve dan Delete

28. Jalankan fixture BE pemulih Pre-setup #12 dan #20 dengan aset Waiting for Approval pada plan Paid hingga tersimpan
29. Buka License > All License; catat Used, Reserved, dan Remaining pada License Summary kolom Asset
30. Approve aset di Fixed Asset > Approvals
31. Tunggu aksi selesai
32. Buka License > All License (langsung muat ulang)
33. Verifikasi Used naik 1, Reserved turun 1, dan Remaining sama dibanding nilai pada langkah 29, tanpa jeda
34. Catat Used dan Remaining pada License Summary kolom Asset
35. Delete satu aset Active
36. Tunggu aksi selesai
37. Muat ulang halaman License
38. Verifikasi Used turun 1 dan Remaining naik 1 dibanding nilai pada langkah 34, tanpa jeda
39. Jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 6, 12, 17, 22, 28, dan 39 (fixture BE pemulih dan penyetel state), langkah 4, 13, 23, dan 37 (muat ulang License), langkah 9, 18, 20, 29, dan 34 (mencatat baseline, S-12), langkah 31 dan 36 (Tunggu aksi selesai sesudah Approve dan Delete, 8b.8), serta navigasi License.
- Urutan TC diubah dari urutan nomor: TC-FA-LIC-401, TC-FA-LIC-402, dan TC-FA-LIC-403 berurutan karena TC-FA-LIC-403 mengubah ketiga aset TC-FA-LIC-402 menjadi Active; TC-FA-LIC-493 sebelum TC-FA-LIC-404 yang menghapus aset (S-10).
- TC-FA-LIC-402 dan TC-FA-LIC-403 menyebut "(sisi tampilan dengan data seed)": spec hanya mengasersi tampilan License atas data seed fixture, tidak menjalankan aksi Manage.
- Alasan di atas sekitar 35 langkah (39 langkah): semua blok satu topik (konsistensi Used, Reserved, dan Unmanaged pada License Summary) dan berdiri sendiri dengan fixture sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LIC-402, TC-FA-LIC-403, dan TC-FA-LIC-493 bergantung pada penanda transisi Manage yang belum ditetapkan `asset/` (Open Item #1); pada kondisi sekarang nilai Expected memang tidak tercapai (TC-FA-LIC-612).
  - TC-FA-LIC-403 tidak menyebut nilai absolut; spec membandingkan dengan nilai langkah 8 dan 9.
  - TC-FA-LIC-493 tidak menyebut akun client Paid dengan Used 100; disediakan tim FE/BE.
  - TC-FA-LIC-404 tidak menyebut tempat Approve dan Delete selain menu Approvals; spec mengikuti kalimat TC.

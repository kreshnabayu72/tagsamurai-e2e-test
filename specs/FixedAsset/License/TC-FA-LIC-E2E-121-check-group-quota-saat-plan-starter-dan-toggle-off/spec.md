---
id: TC-FA-LIC-E2E-121-check-group-quota-saat-plan-starter-dan-toggle-off
title: "check_group_quota pada Plan Paid, Plan Starter, dan License allocation per group OFF"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-489
  - TC-FA-LIC-505
  - TC-FA-LIC-609
  - TC-FA-LIC-613
coverage:
  web: automated
---

# check_group_quota pada Plan Paid, Plan Starter, dan License allocation per group OFF

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono), akun awal hook `before` | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| Pre-setup #9 | Total Control client Starter | `totalControlStarter_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_STARTER_TC_PASSWORD` |
| Pre-setup #35 | Total Control client Paid dengan `License allocation per group` OFF | `totalControlToggleOff_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TOGGLEOFF_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; ganti akun ke Pre-setup #9 (langkah 15) dan Pre-setup #35 (langkah 29) memakai langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; setiap `Spectra.env.*` di atas didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): plan, toggle `License allocation per group`, Total Asset License, hierarki, alokasi grup, dan status aset dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #12 (hierarki dan kuota; Divisi IT Remaining 40), #9 (client Starter; cap plan Asset 500), #35 (client Paid, toggle OFF; data kuota dan hierarki Pre-setup #12 dengan baris alokasi grup dipertahankan), #20 (draf aset siap Submit di Divisi IT), dan #28 (2 aset Unmanaged Divisi IT pada client Starter). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-609 Total Asset License diturunkan di Admin Console menjadi 4338 sehingga Remaining tenant 3 (4338 − 4320 − 15) dan Total lebih kecil dari Total Allocated 4800, Divisi IT Remaining 40, 7 draf aset di Divisi IT, approval OFF; blok TC-FA-LIC-489 login Pre-setup #9, Starter Total 500, Used 498, Reserved 1 (Remaining 1; menyimpang dari Pre-setup #9: Used 120, Reserved 0) lewat fixture BE, baris alokasi Divisi IT 5 dengan Used 5 dipertahankan, dua draf aset di Divisi IT; blok TC-FA-LIC-505 Starter Total 500, Used 498, Reserved 1, baris alokasi Divisi IT 5 dengan Used 5, 2 aset Unmanaged di Divisi IT; blok TC-FA-LIC-613 Total Asset License 4336 sehingga Remaining tenant 1 (4336 − 4320 − 15), baris alokasi Divisi IT 5 dengan Used by This Group 5, draf ke-1 dan ke-2 Pre-setup #20 siap Submit di Divisi IT, approval OFF.
- Blok TC-FA-LIC-505 berlaku setelah `asset/` menetapkan penanda aset dalam transisi Manage (PRD License §12 Open Item #1; Reserved dari Manage); pemicu aksi Manage sesuai PRD `asset/` disediakan tim FE.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup, aset, dan Total Asset License Pre-setup #9, #12, #20, #28, dan #35 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Total Asset License, Used, Reserved, Remaining, status aset, dan Last Updated berubah; fixture memulihkannya. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.

## Test Steps

### TC-FA-LIC-609: Paid dengan toggle ON, sisa slot adalah nilai terkecil antara Remaining grup dan Remaining tenant

1. Jalankan fixture BE pemulih Pre-setup #12 dengan Total Asset License `4338` (Remaining tenant 3), Divisi IT Remaining `40`, 7 draf aset di Divisi IT, dan approval OFF hingga tersimpan
2. Buka License > All License
3. Verifikasi `Remaining` kolom `Asset` `3`
4. Buka Fixed Asset > Asset Registration
5. Registrasi massal 4 aset ke Divisi IT
6. Verifikasi seluruh batch ditolak `QUOTA_EXCEEDED` dengan pesan `Group quota exceeded. Available slots: 3. Please contact administrator to increase quota.`
7. Verifikasi 0 aset dibuat
8. Registrasi massal 3 aset ke Divisi IT
9. Verifikasi 3 aset (tepat batas Remaining tenant) berhasil
10. Buka License > All License
11. Verifikasi License Summary: Used `4323` dan Remaining `0`
12. Buka License > Allocation Quota > node `Divisi IT`
13. Verifikasi Divisi IT: Used by This Group `63` dan Remaining `37`
14. Jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan

### Ganti akun ke Total Control client Starter

15. Ganti akun: keluar dari sesi, lalu login sebagai Total Control client Starter (Pre-setup #9)

### TC-FA-LIC-489: Plan Starter, batas Total plan menjadi penanggung kuota

16. Jalankan fixture BE pemulih Pre-setup #9 dengan Total 500, Used 498, Reserved 1, baris alokasi Divisi IT 5 dengan Used 5, dan dua draf aset di Divisi IT hingga tersimpan
17. Buka Fixed Asset > Asset Registration
18. Registrasi satu aset ke Divisi IT
19. Verifikasi registrasi pertama berhasil walau alokasi Divisi IT sudah terpakai penuh (alokasi grup diabaikan, penanggung = batas Total plan: Total − Used − Reserved = 1)
20. Registrasi satu aset lagi ke Divisi IT
21. Verifikasi registrasi kedua ditolak `QUOTA_EXCEEDED` dengan pesan `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`

### TC-FA-LIC-505: Plan Starter, aksi Manage memakai batas Total plan sebagai penanggung kuota

22. Jalankan fixture BE pemulih Pre-setup #9 dengan Total 500, Used 498, Reserved 1, baris alokasi Divisi IT 5 dengan Used 5, dan 2 aset Unmanaged di Divisi IT hingga tersimpan
23. Jalankan aksi Manage atas 1 aset Unmanaged di Divisi IT sesuai PRD `asset/`
24. Verifikasi aksi pertama diterima walau alokasi Divisi IT sudah terpakai penuh (alokasi grup diabaikan; penanggung kuota = batas Total plan: Total − Used − Reserved = 1)
25. Buka License > All License
26. Verifikasi License Summary: Reserved `2` dan Remaining `0`
27. Jalankan aksi Manage atas 1 aset Unmanaged lagi di Divisi IT sesuai PRD `asset/`
28. Verifikasi aksi kedua ditolak `QUOTA_EXCEEDED` dengan pesan `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`

### Ganti akun ke Total Control client dengan toggle OFF

29. Ganti akun: keluar dari sesi, lalu login sebagai Total Control client Paid dengan `License allocation per group` OFF (Pre-setup #35)

### TC-FA-LIC-613: Paid dengan License allocation per group OFF, check_group_quota hanya memakai batas Total tenant

30. Jalankan fixture BE pemulih Pre-setup #35 dengan Total Asset License `4336` (Remaining tenant 1), baris alokasi Divisi IT 5 dengan Used by This Group 5, draf ke-1 dan ke-2 Pre-setup #20 siap Submit di Divisi IT, dan approval OFF hingga tersimpan
31. Buka Fixed Asset > Asset Registration
32. Registrasi satu aset ke Divisi IT (draf ke-1 Pre-setup #20)
33. Verifikasi registrasi pertama berhasil walau alokasi Divisi IT sudah terpakai penuh (alokasi grup diabaikan, penanggung = batas Total tenant: Total − Used − Reserved = 1)
34. Registrasi satu aset lagi ke Divisi IT (draf ke-2 Pre-setup #20)
35. Verifikasi registrasi kedua ditolak `QUOTA_EXCEEDED` dengan pesan `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`
36. Jalankan fixture BE pemulih Pre-setup #35 dan Pre-setup #9 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 14, 16, 22, 30, dan 36 (fixture BE pemulih dan penyetel state) serta navigasi License dan Asset Registration. Ganti akun pada langkah 15 dan 29 mengikuti S-07.
- Urutan TC diubah dari urutan nomor: dikelompokkan per akun (Pre-setup #1, #9, lalu #35) agar ganti akun hanya dua kali (S-10).
- Spec ini berkelas h (state tenant: plan Starter dan toggle `License allocation per group` OFF) karena objek ujinya adalah perilaku `check_group_quota()` pada kondisi plan dan toggle itu.
- Alasan di atas sekitar 35 langkah (36 langkah): semua blok satu topik (penanggung kuota `check_group_quota()` menurut plan dan toggle) dan berdiri sendiri dengan fixture sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LIC-489 tidak menyebut draf aset siap Submit di Divisi IT pada Precondition; spec menyiapkan dua draf aset lewat fixture.
  - TC-FA-LIC-609 Expected b menyebut nilai terkecil antara Remaining grup 40 dan Remaining tenant 3; spec mengasersi pesan `Available slots: 3` dan hasil akhir Used `4323`.

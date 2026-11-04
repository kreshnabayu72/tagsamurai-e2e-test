---
id: TC-FA-LIC-E2E-117-registrasi-massal-all-or-nothing-import-dan-used
title: "Registrasi Massal dan Import: Pemeriksaan Kuota Sekali, All-or-Nothing, dan Batas Tepat Remaining"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-388
  - TC-FA-LIC-389
  - TC-FA-LIC-390
  - TC-FA-LIC-488
coverage:
  web: automated
---

# Registrasi Massal dan Import: Pemeriksaan Kuota Sekali, All-or-Nothing, dan Batas Tepat Remaining

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki, alokasi grup, dan kuota dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #12 (hierarki dan kuota; Divisi IT Used by This Group 60; Divisi Keuangan belum beralokasi di bawah Kantor Pusat) dan #20 (draf aset siap Submit di Divisi IT dan Divisi Keuangan; berkas impor 31 aset). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-389 Divisi IT diatur Allocated Quota 90 (Used by This Group 60, Reserved 0, Remaining 30; menyimpang dari Pre-setup #12: Allocated 100, Remaining 40) dan 50 draf aset (langkah 1); blok TC-FA-LIC-488 Remaining Kantor Pusat 5, 8 draf aset di Divisi Keuangan, dan approval OFF; blok TC-FA-LIC-388 Divisi IT Remaining 30, 31 draf aset, dan approval OFF; blok TC-FA-LIC-390 Divisi IT Remaining 30, berkas impor 31 aset dan berkas impor 30 aset (aset hasil impor mengikuti mekanik Import).
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup dan aset Pre-setup #12 dan #20 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Used dan Remaining grup, status aset, dan Last Updated berubah; fixture memulihkannya. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: intercept jaringan yang mengamati respons pemeriksaan kuota `check_group_quota()` (kode hasil dan `qty_to_add`), dilepas segera sesudah pengamatan (langkah 18).

## Test Steps

### TC-FA-LIC-389: Registrasi massal 50 aset ke grup dengan sisa 30 slot ditolak seluruhnya

1. Jalankan fixture BE: Divisi IT Allocated Quota `90` (Used by This Group `60`, Reserved `0`, Remaining `30`) dan 50 draf aset siap Submit di Divisi IT hingga tersimpan
2. Buka Fixed Asset > Asset Registration
3. Registrasi massal 50 aset ke Divisi IT
4. Verifikasi seluruh batch ditolak dengan pesan `Group quota exceeded. Available slots: 30. Please contact administrator to increase quota.`
5. Buka License > Allocation Quota
6. Klik node `Divisi IT` di Sidebar
7. Verifikasi tidak ada aset yang dibuat: Used by This Group Divisi IT tetap `60`

### TC-FA-LIC-488: Registrasi massal ke grup tanpa alokasi diperiksa sekali terhadap penanggung kuotanya

8. Jalankan fixture BE pemulih Pre-setup #12 dan penyetel: Divisi Keuangan belum beralokasi, Remaining Kantor Pusat `5`, 8 draf aset di Divisi Keuangan, approval OFF hingga tersimpan
9. Buka License > Allocation Quota
10. Klik node `Kantor Pusat` di Sidebar; catat Used by This Group
11. Klik node `Divisi Keuangan` di Sidebar; catat Used by This Group
12. Pasang intercept jaringan yang mengamati respons pemeriksaan kuota
13. Buka Fixed Asset > Asset Registration
14. Registrasi massal 8 aset ke Divisi Keuangan (satu grup per submit)
15. Verifikasi `check_group_quota()` dipanggil sekali untuk grup Divisi Keuangan dengan `qty_to_add` `8` (jumlah aset batch)
16. Verifikasi penanggung kuota (Kantor Pusat) mengembalikan `QUOTA_EXCEEDED` karena 8 melebihi Remaining 5
17. Verifikasi seluruh batch ditolak dengan pesan `Group quota exceeded. Available slots: 5. Please contact administrator to increase quota.`
18. Lepas intercept jaringan
19. Buka daftar aset
20. Verifikasi tidak ada aset yang dibuat (kedelapan draf tetap berstatus `Draft`)
21. Buka License > Allocation Quota
22. Klik node `Kantor Pusat` di Sidebar
23. Verifikasi Used by This Group Kantor Pusat sama dengan nilai pada langkah 9
24. Klik node `Divisi Keuangan` di Sidebar
25. Verifikasi Used by This Group Divisi Keuangan sama dengan nilai pada langkah 10

### TC-FA-LIC-388: Tepat di batas, Remaining 30: 30 aset berhasil dan 31 aset ditolak seluruhnya

26. Jalankan fixture BE pemulih Pre-setup #12 dengan Divisi IT Remaining `30`, 31 draf aset di Divisi IT, dan approval OFF hingga tersimpan
27. Buka Fixed Asset > Asset Registration
28. Registrasi massal 30 aset ke Divisi IT
29. Verifikasi semua 30 aset berhasil
30. Buka License > Allocation Quota
31. Klik node `Divisi IT` di Sidebar
32. Verifikasi Remaining Divisi IT `0` (tepat di batas = OK)
33. Reset fixture BE: Divisi IT Remaining `30` dan 31 draf aset hingga tersimpan
34. Buka Fixed Asset > Asset Registration
35. Registrasi massal 31 aset ke Divisi IT
36. Verifikasi seluruh batch ditolak dengan pesan `Group quota exceeded. Available slots: 30. Please contact administrator to increase quota.`
37. Verifikasi 0 aset dibuat

### TC-FA-LIC-390: Import banyak aset melewati check_group_quota satu kali

38. Jalankan fixture BE pemulih Pre-setup #12 dengan Divisi IT Remaining `30` hingga tersimpan
39. Impor berkas 31 aset ke Divisi IT melalui Import
40. Verifikasi hasil Import: seluruh batch 31 aset ditolak karena kuota grup tidak cukup
41. Buka daftar aset
42. Verifikasi 0 aset tercipta dari berkas 31 aset
43. Impor berkas 30 aset ke Divisi IT melalui Import
44. Verifikasi impor 30 aset berhasil
45. Buka License > Allocation Quota
46. Klik node `Divisi IT` di Sidebar
47. Verifikasi Remaining Divisi IT `0`
48. Verifikasi hasil impor identik dengan registrasi manual 30 aset (Remaining Divisi IT `0`, sama seperti langkah 32)
49. Jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 8, 26, 33, 38, dan 49 (fixture BE pemulih dan penyetel state), pemasangan dan pelepasan intercept (langkah 12 dan 18), klik tab dan node Sidebar, serta membuka daftar aset (langkah 19 dan 41). Catatan Used by This Group pada langkah 10 dan 11 menjadi baseline langkah 23 dan 25 (S-12).
- Urutan TC diubah dari urutan nomor: TC-FA-LIC-389 dan TC-FA-LIC-488 (penolakan murni) lebih dulu, lalu TC-FA-LIC-388 dan TC-FA-LIC-390 yang memuat registrasi berhasil di batas Remaining (S-10).
- Spec di atas 35 langkah (49 langkah): alasan semua blok satu topik (registrasi massal dan Import terhadap kuota grup) dan berdiri sendiri dengan fixture sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya navigasi, pembacaan baseline, dan pemulihan fixture.
- Temuan untuk QA:
  - TC-FA-LIC-390 menyebut Import sebagai UI modul lain (mekanik import/) tanpa langkah rinci dan tanpa teks pesan penolakan; spec hanya mengasersi "ditolak karena kuota grup tidak cukup" sesuai Expected.
  - TC-FA-LIC-390 Expected "hasil identik dengan registrasi manual" tidak punya ukuran; spec membandingkan dengan Remaining Divisi IT `0` pada langkah 32.
  - TC-FA-LIC-389 Precondition tidak menyebut approval ON atau OFF; spec memakai kondisi default fixture.

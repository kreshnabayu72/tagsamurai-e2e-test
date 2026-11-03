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
- Data Pre-setup: #12 (hierarki dan kuota; Divisi IT Used by This Group 60; Divisi Keuangan belum beralokasi di bawah Kantor Pusat) dan #20 (draf aset siap Submit di Divisi IT dan Divisi Keuangan; berkas impor 31 aset). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-389 Divisi IT Remaining 30 dan 50 draf aset; blok TC-FA-LIC-488 Remaining Kantor Pusat 5, 8 draf aset di Divisi Keuangan, dan approval OFF; blok TC-FA-LIC-388 Divisi IT Remaining 30, 31 draf aset, dan approval OFF; blok TC-FA-LIC-390 Divisi IT Remaining 30, berkas impor 31 aset dan berkas impor 30 aset (aset hasil impor mengikuti mekanik Import).
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup dan aset Pre-setup #12 dan #20 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Used dan Remaining grup, status aset, dan Last Updated berubah; fixture memulihkannya. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: intercept jaringan yang mengamati respons pemeriksaan kuota `check_group_quota()` (kode hasil dan `qty_to_add`), dilepas segera sesudah pengamatan (langkah 17).

## Test Steps

### TC-FA-LIC-389: Registrasi massal 50 aset ke grup dengan sisa 30 slot ditolak seluruhnya

1. Buka Fixed Asset > Asset Registration
2. Registrasi massal 50 aset ke Divisi IT
3. Verifikasi seluruh batch ditolak dengan pesan `Group quota exceeded. Available slots: 30. Please contact administrator to increase quota.`
4. Buka License > Allocation Quota
5. Klik node `Divisi IT` di Sidebar
6. Verifikasi tidak ada aset yang dibuat: Used by This Group Divisi IT tetap `60`

### TC-FA-LIC-488: Registrasi massal ke grup tanpa alokasi diperiksa sekali terhadap penanggung kuotanya

7. Jalankan fixture BE: Divisi Keuangan belum beralokasi, Remaining Kantor Pusat `5`, 8 draf aset di Divisi Keuangan, approval OFF hingga tersimpan
8. Buka License > Allocation Quota
9. Klik node `Kantor Pusat` di Sidebar; catat Used by This Group
10. Klik node `Divisi Keuangan` di Sidebar; catat Used by This Group
11. Pasang intercept jaringan yang mengamati respons pemeriksaan kuota
12. Buka Fixed Asset > Asset Registration
13. Registrasi massal 8 aset ke Divisi Keuangan (satu grup per submit)
14. Verifikasi `check_group_quota()` dipanggil sekali untuk grup Divisi Keuangan dengan `qty_to_add` `8` (jumlah aset batch)
15. Verifikasi penanggung kuota (Kantor Pusat) mengembalikan `QUOTA_EXCEEDED` karena 8 melebihi Remaining 5
16. Verifikasi seluruh batch ditolak dengan pesan `Group quota exceeded. Available slots: 5. Please contact administrator to increase quota.`
17. Lepas intercept jaringan
18. Buka daftar aset
19. Verifikasi tidak ada aset yang dibuat (kedelapan draf tetap berstatus `Draft`)
20. Buka License > Allocation Quota
21. Klik node `Kantor Pusat` di Sidebar
22. Verifikasi Used by This Group Kantor Pusat sama dengan nilai pada langkah 9
23. Klik node `Divisi Keuangan` di Sidebar
24. Verifikasi Used by This Group Divisi Keuangan sama dengan nilai pada langkah 10

### TC-FA-LIC-388: Tepat di batas, Remaining 30: 30 aset berhasil dan 31 aset ditolak seluruhnya

25. Jalankan fixture BE pemulih Pre-setup #12 dengan Divisi IT Remaining `30`, 31 draf aset di Divisi IT, dan approval OFF hingga tersimpan
26. Buka Fixed Asset > Asset Registration
27. Registrasi massal 30 aset ke Divisi IT
28. Verifikasi semua 30 aset berhasil
29. Buka License > Allocation Quota
30. Klik node `Divisi IT` di Sidebar
31. Verifikasi Remaining Divisi IT `0` (tepat di batas = OK)
32. Reset fixture BE: Divisi IT Remaining `30` dan 31 draf aset hingga tersimpan
33. Buka Fixed Asset > Asset Registration
34. Registrasi massal 31 aset ke Divisi IT
35. Verifikasi seluruh batch ditolak dengan pesan `Group quota exceeded. Available slots: 30. Please contact administrator to increase quota.`
36. Verifikasi 0 aset dibuat

### TC-FA-LIC-390: Import banyak aset melewati check_group_quota satu kali

37. Jalankan fixture BE pemulih Pre-setup #12 dengan Divisi IT Remaining `30` hingga tersimpan
38. Impor berkas 31 aset ke Divisi IT melalui Import
39. Verifikasi hasil Import: seluruh batch 31 aset ditolak karena kuota grup tidak cukup
40. Buka daftar aset
41. Verifikasi 0 aset tercipta dari berkas 31 aset
42. Impor berkas 30 aset ke Divisi IT melalui Import
43. Verifikasi impor 30 aset berhasil
44. Buka License > Allocation Quota
45. Klik node `Divisi IT` di Sidebar
46. Verifikasi Remaining Divisi IT `0`
47. Verifikasi hasil impor identik dengan registrasi manual 30 aset (Remaining Divisi IT `0`, sama seperti langkah 31)
48. Jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 7, 25, 32, 37, dan 48 (fixture BE pemulih dan penyetel state), pemasangan dan pelepasan intercept (langkah 11 dan 17), klik tab dan node Sidebar, serta membuka daftar aset (langkah 18 dan 40). Catatan Used by This Group pada langkah 9 dan 10 menjadi baseline langkah 22 dan 24 (S-12).
- Urutan TC diubah dari urutan nomor: TC-FA-LIC-389 dan TC-FA-LIC-488 (penolakan murni) lebih dulu, lalu TC-FA-LIC-388 dan TC-FA-LIC-390 yang memuat registrasi berhasil di batas Remaining (S-10).
- Alasan di atas sekitar 35 langkah (48 langkah): semua blok satu topik (registrasi massal dan Import terhadap kuota grup) dan berdiri sendiri dengan fixture sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya navigasi, pembacaan baseline, dan pemulihan fixture.
- Temuan untuk QA:
  - TC-FA-LIC-390 menyebut Import sebagai UI modul lain (mekanik import/) tanpa langkah rinci dan tanpa teks pesan penolakan; spec hanya mengasersi "ditolak karena kuota grup tidak cukup" sesuai Expected.
  - TC-FA-LIC-390 Expected "hasil identik dengan registrasi manual" tidak punya ukuran; spec membandingkan dengan Remaining Divisi IT `0` pada langkah 31.
  - TC-FA-LIC-389 Precondition tidak menyebut approval ON atau OFF; spec memakai kondisi default fixture.

---
id: TC-FA-LIC-E2E-124-perhitungan-edge-remaining-0-saat-over-used-dan-minimum
title: "Perhitungan Edge: Remaining Ditampilkan 0 Saat Over-used dan Minimum Quota dengan Reserved"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LIC-410
  - TC-FA-LIC-494
  - TC-FA-LIC-510
  - TC-FA-LIC-612
coverage:
  web: automated
---

# Perhitungan Edge: Remaining Ditampilkan 0 Saat Over-used dan Minimum Quota dengan Reserved

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki, alokasi grup, dan status aset dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #12 (hierarki dan kuota; License Summary Reserved 15, Unmanaged 27; Divisi IT beralokasi 100 dengan Used by This Group 60), #20 (draf aset siap Submit), dan #28 (3 aset Unmanaged di Divisi IT). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-410 grup A beralokasi 100 dengan Used 50 dan child B tanpa alokasi dengan Used 70 pada subtree (rumus Remaining 100 − 50 − 0 − 70 = −20), nama grup A dan child B ditentukan fixture; blok TC-FA-LIC-494 Divisi IT beralokasi 100 dengan Used 110 pada subtree dan satu subgroup tanpa alokasi di bawahnya; blok TC-FA-LIC-612 penanda aset dalam transisi Manage belum ditetapkan `asset/`, Divisi IT Used by This Group 60 dan Remaining 40, serta 3 aset Unmanaged di Divisi IT; blok TC-FA-LIC-510 Divisi IT beralokasi 100 dengan Used by This Group 60 dan 3 aset Unmanaged di Divisi IT.
- Blok TC-FA-LIC-510 berlaku setelah `asset/` menetapkan penanda aset dalam transisi Manage (PRD License §12 Open Item #1; Reserved dari Manage); blok TC-FA-LIC-612 menguji kondisi saat penanda belum ditetapkan. Pemicu aksi Manage sesuai PRD `asset/` disediakan tim FE.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup dan aset Pre-setup #12, #20, dan #28 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Used, Reserved, Unmanaged, Remaining, status aset, dan Last Updated berubah; fixture memulihkannya. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: intercept jaringan yang mengamati respons pemeriksaan kuota `check_group_quota()` (kode hasil, `qty_to_add`, dan sisa slot).

## Test Steps

### TC-FA-LIC-410: Remaining negatif karena pemakaian subtree child tanpa alokasi ditampilkan 0

1. Jalankan fixture BE: grup A beralokasi 100 dengan Used 50 dan child B tanpa alokasi dengan Used 70 pada subtree hingga tersimpan
2. Buka License > Allocation Quota > node grup A
3. Verifikasi Remaining grup A ditampilkan `0` (bukan `-20`)
4. Buka Fixed Asset > Asset Registration
5. Submit 1 draf aset di grup A
6. Verifikasi registrasi ditolak

### TC-FA-LIC-494: Grup over-used, Remaining ditampilkan 0 dan Maximum Quota parent memakai Remaining 0

7. Jalankan fixture BE pemulih Pre-setup #12 dengan Divisi IT beralokasi 100, Used 110 pada subtree, dan satu subgroup tanpa alokasi di bawah Divisi IT hingga tersimpan
8. Buka License > Allocation Quota > node `Kantor Pusat`
9. Verifikasi Remaining Divisi IT ditampilkan `0`, bukan angka negatif
10. Klik node `Divisi IT` di Sidebar
11. Klik tombol ikon `[Edit]` pada subgroup tanpa alokasi di bawah Divisi IT
12. Verifikasi Maximum Quota subgroup memakai Remaining parent `0` (di-clamp minimal 0)
13. Klik `[×]` pada modal Edit Allocation (form tidak diubah)
14. Buka Fixed Asset > Asset Registration
15. Registrasi satu aset ke Divisi IT
16. Verifikasi registrasi ditolak dengan pesan `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`

### TC-FA-LIC-612: Selama penanda transisi Manage belum ditetapkan, seluruh aset Unmanaged dihitung di baris Unmanaged

17. Jalankan fixture BE pemulih Pre-setup #12 dengan penanda aset dalam transisi Manage belum ditetapkan, Divisi IT Used by This Group 60 (Remaining 40), dan 3 aset Unmanaged di Divisi IT hingga tersimpan
18. Buka License > All License; catat Reserved dan Unmanaged pada License Summary kolom Asset
19. Pasang intercept jaringan yang mengamati respons pemeriksaan kuota
20. Jalankan aksi Manage atas 3 aset Unmanaged di Divisi IT sesuai PRD `asset/`
21. Verifikasi `check_group_quota()` dipanggil untuk Divisi IT dengan `qty_to_add` `3` dan memperoleh `OK` (Remaining 40)
22. Lepas intercept jaringan
23. Muat ulang License > All License
24. Verifikasi License Summary: Reserved tetap `15` (Reserved dari Manage bernilai 0), sama dengan nilai pada langkah 18
25. Verifikasi License Summary: Unmanaged tetap `27` (seluruh aset Unmanaged dihitung pada baris Unmanaged), sama dengan nilai pada langkah 18
26. Buka License > Allocation Quota > node `Divisi IT`
27. Verifikasi Divisi IT: Reserved by This Group `0`
28. Atur Remaining Divisi IT menjadi `2` lewat fixture BE hingga tersimpan
29. Pasang intercept jaringan yang mengamati respons pemeriksaan kuota
30. Ulangi aksi Manage atas 3 aset itu sesuai PRD `asset/`
31. Verifikasi pemeriksaan kuota mengembalikan `QUOTA_EXCEEDED` dengan sisa slot `2`
32. Verifikasi seluruh aksi ditolak (pemeriksaan kuota tetap berlaku)
33. Lepas intercept jaringan

### TC-FA-LIC-510: Minimum Quota Edit Allocation memuat Reserved dari aset dalam transisi Manage

34. Jalankan fixture BE pemulih Pre-setup #12 dengan Divisi IT beralokasi 100 (Used by This Group 60) dan 3 aset Unmanaged di Divisi IT hingga tersimpan
35. Jalankan aksi Manage atas 3 aset Unmanaged di Divisi IT sesuai PRD `asset/` hingga tersimpan
36. Buka License > Allocation Quota > node `Kantor Pusat`
37. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
38. Verifikasi Minimum Quota `63 = 60 assets in this group + 3 reserved + 0 allocated to subgroups`
39. Isi New Allocated Quota `62`
40. Pindahkan fokus keluar dari field (blur)
41. Verifikasi field berborder danger
42. Verifikasi pesan inline `Cannot set quota below used, reserved, and subgroup-allocated quota (63).`
43. Verifikasi modal tetap terbuka
44. Verifikasi nilai `62` dipertahankan
45. Klik `[×]` pada modal Edit Allocation
46. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
47. Klik `[Leave]`
48. Jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 7, 17, 28, 34, dan 48 (fixture BE pemulih dan penyetel state), pemasangan dan pelepasan intercept (langkah 19, 22, 29, dan 33), langkah 13 (menutup modal Edit Allocation yang tidak diubah sehingga dialog `Unsaved Changes` tidak muncul), langkah 35 (pemicu aksi Manage hingga tersimpan sebelum membuka Allocation Quota, bagian 8b butir 8), muat ulang halaman, navigasi License, serta pencatatan baseline pada langkah 18 (S-12). Modal pada TC-FA-LIC-510 ditutup deterministik lewat `[×]`, dialog `Unsaved Changes`, dan `[Leave]` (S-08).
- Urutan TC diubah dari urutan nomor: TC-FA-LIC-410, TC-FA-LIC-494, dan TC-FA-LIC-612 lebih dulu, TC-FA-LIC-510 di akhir karena berakhir dengan form dirty yang ditutup lewat `[Leave]` (S-10).
- Alasan di atas sekitar 35 langkah (48 langkah): semua blok satu topik (perhitungan Remaining di batas 0 dan Minimum Quota) dan berdiri sendiri dengan fixture sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya intercept, navigasi, dan pemulihan fixture.
- Temuan untuk QA:
  - TC-FA-LIC-410 butir b dan TC-FA-LIC-494 butir c menulis `QUOTA_EXCEEDED` pada Expected tetapi tidak menyebut cara mengamatinya (intercept respons pemeriksaan kuota hanya terpasang pada blok TC-FA-LIC-612); spec tidak mengasersi kode itu dan mengasersi hasil yang teramati: registrasi ditolak (langkah 6 dan 16), dengan pesan `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.` pada langkah 16.
  - TC-FA-LIC-410 memakai nama generik "grup A" dan "child B" tanpa nama Pre-setup; nama ditentukan fixture BE.
  - TC-FA-LIC-410 Expected b menyebut "grup A atau subgroup tanpa alokasinya" ditolak; langkah TC hanya meregistrasi di grup A, sehingga hanya grup A yang diasersi.
  - TC-FA-LIC-494 langkah 2 tidak menyebut nama subgroup dan tidak menyebut node tempat tombol `[Edit]` subgroup tampil; spec menambah klik node `Divisi IT` sebagai langkah penghubung.
  - TC-FA-LIC-510 dan TC-FA-LIC-612 bergantung pada penanda transisi Manage (Open Item #1); TC-FA-LIC-510 hanya tercapai setelah penanda ditetapkan.

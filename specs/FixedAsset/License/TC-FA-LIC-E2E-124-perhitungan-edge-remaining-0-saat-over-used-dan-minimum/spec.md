---
id: TC-FA-LIC-E2E-124-perhitungan-edge-remaining-0-saat-over-used-dan-minimum
title: "Perhitungan Edge: Remaining Ditampilkan 0 Saat Over-used, Tingkat Full, dan Minimum Quota dengan Reserved"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LIC-410
  - TC-FA-LIC-494
  - TC-FA-LIC-495
  - TC-FA-LIC-510
  - TC-FA-LIC-612
coverage:
  web: automated
---

# Perhitungan Edge: Remaining Ditampilkan 0 Saat Over-used, Tingkat Full, dan Minimum Quota dengan Reserved

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| Pre-setup #3 | Manage global license, penerima peringatan kuota (daftar notifikasinya dibaca lewat kemampuan baca, tanpa login) | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` dan `Spectra.env.FA_MGL_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki, alokasi grup, kuota tenant, penanda tingkat peringatan, status aset, dan jam fixture dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #12 (hierarki dan kuota; License Summary Reserved 15, Unmanaged 27; Divisi IT beralokasi 100 dengan Used by This Group 60), #16 (tenant peringatan kuota Total Asset License 100, penanda Normal, penerima #3 dan #1), #20 (draf aset siap Submit), dan #28 (3 aset Unmanaged di Divisi IT). Kondisi per blok (diatur fixture BE): blok TC-FA-LIC-410 grup A beralokasi 100 dengan Used 50 dan child B tanpa alokasi dengan Used 70 pada subtree (rumus Remaining 100 − 50 − 0 − 70 = −20), nama grup A dan child B ditentukan fixture; blok TC-FA-LIC-494 Divisi IT beralokasi 100 dengan Used 110 pada subtree dan satu subgroup tanpa alokasi di bawahnya; blok TC-FA-LIC-495 Used 95 dan Reserved 10 (Remaining rumus −5); blok TC-FA-LIC-612 penanda aset dalam transisi Manage belum ditetapkan `asset/`, Divisi IT Used by This Group 60 dan Remaining 40, serta 3 aset Unmanaged di Divisi IT; blok TC-FA-LIC-510 Divisi IT beralokasi 100 dengan Used by This Group 60 dan 3 aset Unmanaged di Divisi IT.
- Blok TC-FA-LIC-510 berlaku setelah `asset/` menetapkan penanda aset dalam transisi Manage (PRD License §12 Open Item #1; Reserved dari Manage); blok TC-FA-LIC-612 menguji kondisi saat penanda belum ditetapkan. Pemicu aksi Manage sesuai PRD `asset/` disediakan tim FE.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup, aset, dan Total Asset License Pre-setup #12, #16, #20, dan #28 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Used, Reserved, Unmanaged, Remaining, penanda tingkat, status aset, dan Last Updated berubah; fixture memulihkannya. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: intercept jaringan yang mengamati respons pemeriksaan kuota `check_group_quota()` (kode hasil, `qty_to_add`, dan sisa slot); kemampuan membaca daftar notifikasi akun penerima Pre-setup #3 lewat fixture BE (disediakan tim FE/BE; endpoint tidak dikarang); jam fixture digeser pada blok TC-FA-LIC-495 dan dipulihkan pada langkah 25 serta di hook `after` (sesi UI dan sesi API aktor tetap valid selama jam digeser, dinyatakan di `suite.md`).
- Asersi absence notifikasi in-app didahului anchor positif dan langkah `Tunggu 5 detik tanpa memuat ulang halaman` (jendela standar pilihan spec, bukan nilai TC atau PRD).

## Test Steps

### TC-FA-LIC-410: Remaining negatif karena pemakaian subtree child tanpa alokasi ditampilkan 0

1. Jalankan fixture BE: grup A beralokasi 100 dengan Used 50 dan child B tanpa alokasi dengan Used 70 pada subtree hingga tersimpan
2. Buka License > Allocation Quota > node grup A
3. Verifikasi Remaining grup A ditampilkan `0` (bukan `-20`)
4. Buka Fixed Asset > Asset Registration
5. Submit 1 draf aset di grup A
6. Verifikasi registrasi ditolak `QUOTA_EXCEEDED`

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
16. Verifikasi registrasi ditolak `QUOTA_EXCEEDED` dengan pesan `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`

### TC-FA-LIC-495: Used + Reserved tenant melampaui Total, Remaining ditampilkan 0 dan tingkat Full

17. Jalankan fixture BE pemulih Pre-setup #16 dengan Used `95`, Reserved `10`, dan penanda tingkat Normal hingga tersimpan
18. Buka License > All License
19. Verifikasi Remaining tenant ditampilkan `0`, bukan `-5`
20. Catat jumlah notifikasi `Asset license quota is full` dan `Asset license quota is running low` pada Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3
21. Geser jam fixture sampai penilaian berjalan
22. Tunggu 5 detik tanpa memuat ulang halaman
23. Verifikasi Bell Notification akun Pre-setup #1 dan daftar notifikasi akun Pre-setup #3 masing-masing memuat tepat satu notifikasi baru `Asset license quota is full` dibanding langkah 20
24. Verifikasi tidak ada notifikasi baru `Asset license quota is running low` dibanding langkah 20
25. Pulihkan jam fixture

### TC-FA-LIC-612: Selama penanda transisi Manage belum ditetapkan, seluruh aset Unmanaged dihitung di baris Unmanaged

26. Jalankan fixture BE pemulih Pre-setup #12 dengan penanda aset dalam transisi Manage belum ditetapkan, Divisi IT Used by This Group 60 (Remaining 40), dan 3 aset Unmanaged di Divisi IT hingga tersimpan
27. Buka License > All License; catat Reserved dan Unmanaged pada License Summary kolom Asset
28. Pasang intercept jaringan yang mengamati respons pemeriksaan kuota
29. Jalankan aksi Manage atas 3 aset Unmanaged di Divisi IT sesuai PRD `asset/`
30. Verifikasi `check_group_quota()` dipanggil untuk Divisi IT dengan `qty_to_add` `3` dan memperoleh `OK` (Remaining 40)
31. Lepas intercept jaringan
32. Muat ulang License > All License
33. Verifikasi License Summary: Reserved tetap `15` (Reserved dari Manage bernilai 0) dan Unmanaged tetap `27` (seluruh aset Unmanaged dihitung pada baris Unmanaged), sama dengan nilai pada langkah 27
34. Buka License > Allocation Quota > node `Divisi IT`
35. Verifikasi Divisi IT: Reserved by This Group `0`
36. Atur Remaining Divisi IT menjadi `2` lewat fixture BE hingga tersimpan
37. Pasang intercept jaringan yang mengamati respons pemeriksaan kuota
38. Ulangi aksi Manage atas 3 aset itu sesuai PRD `asset/`
39. Verifikasi pemeriksaan kuota mengembalikan `QUOTA_EXCEEDED` dengan sisa slot `2`
40. Verifikasi seluruh aksi ditolak (pemeriksaan kuota tetap berlaku)
41. Lepas intercept jaringan

### TC-FA-LIC-510: Minimum Quota Edit Allocation memuat Reserved dari aset dalam transisi Manage

42. Jalankan fixture BE pemulih Pre-setup #12 dengan Divisi IT beralokasi 100 (Used by This Group 60) dan 3 aset Unmanaged di Divisi IT hingga tersimpan
43. Jalankan aksi Manage atas 3 aset Unmanaged di Divisi IT sesuai PRD `asset/`
44. Buka License > Allocation Quota > node `Kantor Pusat`
45. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
46. Verifikasi Minimum Quota `63 = 60 assets in this group + 3 reserved + 0 allocated to subgroups`
47. Isi New Allocated Quota `62`
48. Pindahkan fokus keluar dari field (blur)
49. Verifikasi field berborder danger
50. Verifikasi pesan inline `Cannot set quota below used, reserved, and subgroup-allocated quota (63).`
51. Verifikasi modal tetap terbuka dengan nilai `62` dipertahankan
52. Klik `[×]` pada modal Edit Allocation
53. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
54. Klik `[Leave]`
55. Jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1, 7, 17, 26, 36, 42, dan 55 (fixture BE pemulih dan penyetel state), pemasangan dan pelepasan intercept (langkah 28, 31, 37, dan 41), langkah 21 dan 25 (menggeser dan memulihkan jam fixture), langkah 13 (menutup modal Edit Allocation yang tidak diubah sehingga dialog `Unsaved Changes` tidak muncul), langkah 43 (pemicu aksi Manage), muat ulang halaman, navigasi License, serta pencatatan baseline pada langkah 20 dan 27 (S-12). Modal pada TC-FA-LIC-510 ditutup deterministik lewat `[×]`, dialog `Unsaved Changes`, dan `[Leave]` (S-08). Langkah `Tunggu 5 detik tanpa memuat ulang halaman` mendahului asersi absence notifikasi.
- Urutan TC diubah dari urutan nomor: TC-FA-LIC-410, TC-FA-LIC-494, TC-FA-LIC-495, dan TC-FA-LIC-612 lebih dulu, TC-FA-LIC-510 di akhir karena berakhir dengan form dirty yang ditutup lewat `[Leave]` (S-10).
- Alasan di atas sekitar 35 langkah (55 langkah): semua blok satu topik (perhitungan Remaining di batas 0 dan Minimum Quota) dan berdiri sendiri dengan fixture sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya intercept, navigasi, dan pemulihan fixture.
- Temuan untuk QA:
  - TC-FA-LIC-410 memakai nama generik "grup A" dan "child B" tanpa nama Pre-setup; nama ditentukan fixture BE.
  - TC-FA-LIC-410 Expected b menyebut "grup A atau subgroup tanpa alokasinya" ditolak; langkah TC hanya meregistrasi di grup A, sehingga hanya grup A yang diasersi.
  - TC-FA-LIC-494 langkah 2 tidak menyebut nama subgroup dan tidak menyebut node tempat tombol `[Edit]` subgroup tampil; spec menambah klik node `Divisi IT` sebagai langkah penghubung.
  - TC-FA-LIC-495 Expected tidak menyebut akun yang menerima notifikasi; spec mengasersi akun Pre-setup #1 dan #3 sesuai Precondition Pre-setup #16.
  - TC-FA-LIC-510 dan TC-FA-LIC-612 bergantung pada penanda transisi Manage (Open Item #1); TC-FA-LIC-510 hanya tercapai setelah penanda ditetapkan.

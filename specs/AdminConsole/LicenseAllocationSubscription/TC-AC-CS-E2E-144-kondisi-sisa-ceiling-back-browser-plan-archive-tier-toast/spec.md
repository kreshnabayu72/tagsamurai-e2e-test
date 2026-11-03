---
id: TC-AC-CS-E2E-144-kondisi-sisa-ceiling-back-browser-plan-archive-tier-toast
title: "Kondisi Sisa: Ceiling, Back Browser, Plan Archive, Tier, Toast"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-CS-537
  - TC-AC-CS-538
  - TC-AC-CS-539
  - TC-AC-CS-540
  - TC-AC-CS-562
coverage:
  web: automated
---

# Kondisi Sisa: Ceiling, Back Browser, Plan Archive, Tier, Toast

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-144`):
  1. TC-AC-CS-537: trial SAMS Growth Active `T537` dengan Duration 50 hari (setara `SUBS-20260810-00007`, Pre-setup #103: Client Toko Uji Trial).
  2. TC-AC-CS-538 dan 539: Client `C540a` dipilih dari dropdown (tidak ada data tambahan).
  3. TC-AC-CS-539: term Active FAMS `T539` dengan plan custom `Maju Custom+{runId}-144` (badge Custom; setara `SUBS-20260101-00005`, Pre-setup #130).
  4. TC-AC-CS-540: Client `C540a` dan `C540b` (setara `Client Tanpa Subscription`, #48, dan `Toko Bandung Raya`, #89) yang belum punya term FAMS maupun SAMS; dipakai untuk FAMS `Starter` dan SAMS `Enterprise`.
  5. TC-AC-CS-562: Client `C562` (setara `Client Tanpa Subscription`, #48) tanpa term, untuk Add SAMS `Growth`, Duration `1`, Start Date `19/08/26`.
- State global yang diubah (suite serial): Max Trial Duration (60 hari menjadi 30 hari, TC-AC-CS-537) dan status Archive plan `Maju Custom+{runId}-144` (TC-AC-CS-539); keduanya dipulihkan oleh fixture backend yang disediakan tim FE/BE di hook `after` (S-06, pengecualian 2026-10-30), dan efeknya (Last Updated dan entri audit trail) tercatat di spec ini. Term yang terbentuk pada TC-AC-CS-540 dan 562 dibersihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): mengubah Max Trial Duration dan meng-Archive plan lewat fixture backend; tombol Back browser dijalankan oleh runner; jeda 5 detik pada langkah 46 adalah pilihan spec (jeda nyata di bawah ±30 detik, bagian 6); jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu, disediakan tim FE/BE), dipulihkan di hook `after`.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-537: Penurunan ceiling Trial tidak mengubah trial yang sudah aktif

1. Turunkan Max Trial Duration dari 60 menjadi 30 hari lewat fixture backend hingga tersimpan
2. Ketik Search `T537`, tekan Enter
3. Klik baris trial `T537`
4. Verifikasi trial Active tetap berjalan dengan parameter 50 hari pada Subscription Detail
5. Klik menu `Client Subscription` di sidebar
6. Klik `[+ Activate Trial]`
7. Pilih Product `FAMS`
8. Verifikasi helper Trial Duration menampilkan "Maximum 30 days" (ceiling baru berlaku untuk pengajuan baru)
9. Klik `✕` pada modal
10. Verifikasi dialog `Unsaved Changes` tampil
11. Klik `[Leave]`

### TC-AC-CS-538: Tombol Back browser saat modal form terbuka mengikuti pencegahan navigasi

12. Klik `[+ Subscription]`
13. Pilih Client `C540a`
14. Klik tombol Back browser
15. Verifikasi perpindahan route dicegat dan dialog `Unsaved Changes` muncul dengan tombol `[Cancel]` dan `[Leave]`
16. Klik `[Cancel]`
17. Verifikasi form dipertahankan
18. Klik `✕` pada modal
19. Verifikasi dialog `Unsaved Changes` tampil
20. Klik `[Leave]`

### TC-AC-CS-539: Plan di-Archive tidak mengubah term yang sudah dibuat

21. Archive plan `Maju Custom+{runId}-144` di Plans & Features lewat fixture backend hingga tersimpan
22. Klik menu `Client Subscription` di sidebar
23. Ketik Search `T539`, tekan Enter
24. Verifikasi baris `T539` di List berstatus Active dengan plan `Maju Custom+{runId}-144`
25. Klik baris `T539`
26. Verifikasi Subscription Detail menampilkan term Active dengan plan `Maju Custom+{runId}-144` dan data tidak berubah
27. Klik menu `Client Subscription` di sidebar
28. Klik `[+ Subscription]`, pilih Client `C540a` dan Product `FAMS`, buka dropdown Plan
29. Verifikasi sedikitnya satu opsi plan lain tampil pada dropdown Plan
30. Verifikasi plan `Maju Custom+{runId}-144` tidak ada pada opsi dropdown Plan
31. Klik `✕` pada modal
32. Verifikasi dialog `Unsaved Changes` tampil
33. Klik `[Leave]`

### TC-AC-CS-540: Pembuatan term tidak digerbang oleh tier plan

34. Klik `[+ Subscription]`
35. Pilih Client `C540a`, Product `FAMS`, Plan `Starter`, isi Duration dan Start Date nilai fixture, klik `[Submit]`
36. Verifikasi toast sukses "Success, subscription has been added."
37. Klik `[+ Subscription]`
38. Pilih Client `C540b`, Product `SAMS`, Plan `Enterprise`, isi Duration dan Start Date nilai fixture, klik `[Submit]`
39. Verifikasi toast sukses "Success, subscription has been added."
40. Verifikasi tidak ada penolakan terkait tier atau rank plan pada kedua pembuatan (naik atau turun rank diizinkan)

### TC-AC-CS-562: Toast sukses muncul di kanan bawah dan hilang otomatis dalam 4 detik

41. Klik `[+ Subscription]`
42. Pilih Client `C562`, Product `SAMS`, Plan `Growth`, isi Duration `1`, Start Date `19/08/26`
43. Klik `[Submit]`
44. Verifikasi toast berada di kanan bawah layar
45. Verifikasi toast sukses "Success, subscription has been added." tampil
46. Tunggu 5 detik tanpa interaksi
47. Verifikasi toast sukses hilang sendiri setelah 4 detik

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 2 dan 23 (Search untuk menemukan baris target, R-16), langkah 5, 22, 27 (pindah halaman), langkah 9 sampai 11, 18 sampai 20, 31 sampai 33 (menutup form dirty, S-08; langkah 18 sampai 20 menutup form sesudah `[Cancel]` pada dialog), dan langkah 46 (jeda 5 detik tanpa `Verifikasi`).
- Spec ini melewati ~35 langkah (47). Alasan: kelima TC adalah kondisi sisa yang berdiri sendiri dan tidak berbagi state (kegagalan satu blok tidak membuat blok lain kehilangan makna), semuanya kelas fungsional ringan pada halaman yang sama, dan pemecahan hanya menambah login dan hook.
- Langkah 36 dan 39 memakai teks toast "Success, subscription has been added." dari TC-AC-CS-562 dan TC-AC-CS-172; TC-AC-CS-540 sendiri hanya menyebut "berhasil".
- Temuan untuk QA:
  - TC-AC-CS-537 Expected b ("ceiling baru hanya berlaku untuk pengajuan dan Edit baru") menyebut Edit baru tanpa langkah; spec hanya mengasersi pengajuan baru (Activate Trial) lewat helper "Maximum 30 days".
  - TC-AC-CS-537 Expected a tidak menyebut cara menampilkan "parameter 50 hari" pada Detail; spec mengasersi nilai 50 hari tanpa menamai field.
  - TC-AC-CS-538 langkah 1 menyebut "isi Client" saja; spec memilih Client `C540a`.
  - TC-AC-CS-539 Expected b ("hanya hilang dari opsi dropdown") tidak menyebut Product atau Client yang dipilih; spec memilih Client `C540a` dan Product `FAMS`.
  - TC-AC-CS-540 Expected b ("naik atau turun rank diizinkan") tidak punya langkah pembanding rank; spec mengasersi tidak ada penolakan tier.
  - TC-AC-CS-540 tidak menyebut nilai Duration dan Start Date; dirujuk lewat fixture.

---
id: TC-AC-CS-E2E-047-activate-trial-opsi-plan-dan-eligibilitas
title: "Activate Trial: Opsi Plan dan Eligibilitas"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-178
  - TC-AC-CS-179
  - TC-AC-CS-194
  - TC-AC-CS-195
coverage:
  web: automated
---

# Activate Trial: Opsi Plan dan Eligibilitas

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Data Pre-setup yang dibaca (dropdown dibuka dan Submit ditolak guard; tidak diubah dan Last Updated tidak berubah, S-06):
  - Client `Toko Uji Trial` (Pre-setup #103) dengan riwayat trial FAMS: plan Enterprise Active (`SUBS-20260810-00006`), plan Growth Converted, plan Professional Canceled, plan Starter Rejected, tanpa trial Waiting for Approval.
  - Client `Toko Semua Trial` (Pre-setup #104) yang sudah punya trial untuk seluruh plan FAMS yang tersedia bagi Principal: Starter, Growth, Professional, Enterprise, dan Custom Plan `Mitra Premium`.
  - Client `PT Sejahtera` (Pre-setup #38) dengan trial FAMS Enterprise Active (`SUBS-20260810-00001`, Pre-setup #60), plan Growth belum pernah di-trial.
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`, beserta trial yang dibuat sesi API): Client `Client Tanpa Subscription+{runId}-047` (padanan Pre-setup #48: tanpa term dan tanpa trial) untuk TC-AC-CS-194.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan; sesi API aktor Principal): membuat trial plan `Growth` untuk Client seed hingga tersimpan (TC-AC-CS-194); membaca jumlah trial per Client lewat fixture BE.
- Ceiling Trial 60 hari, 200 assets, 50 users (Pre-setup #25) tidak diubah; kuota yang diisi 30 hari, 50 assets, 10 users (nilai awal form).

## Test Steps

### TC-AC-CS-178: Plan yang sudah pernah di-trial Client dan Product disembunyikan dari dropdown

1. Klik `[+ Activate Trial]`
2. Pilih Client `Toko Uji Trial` dan Product `FAMS`
3. Buka dropdown Plan
4. Verifikasi plan Starter tampil karena trial Rejected tidak dihitung
5. Verifikasi plan Growth, Professional, dan Enterprise tidak ditampilkan (Hidden, bukan Disabled)
6. Verifikasi helper "Plans this client has already trialed are not listed" tampil
7. Tekan `Esc` untuk menutup dropdown Plan

### TC-AC-CS-179: Semua plan sudah di-trial menghasilkan dropdown Plan tanpa opsi

8. Pilih Client `Toko Semua Trial` dan Product `FAMS`
9. Buka dropdown Plan
10. Verifikasi dropdown Plan menampilkan empty state Select standar tanpa opsi
11. Verifikasi helper "Plans this client has already trialed are not listed" tetap tampil
12. Tekan `Esc` untuk menutup dropdown Plan, lalu isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`
13. Klik `[Submit]`
14. Verifikasi error inline "Plan must not be empty"
15. Verifikasi tidak ada trial dibuat (jumlah trial Client `Toko Semua Trial` tetap, dibaca lewat fixture BE)
16. Klik `[Clear Field]`

### TC-AC-CS-194: Eligibilitas gagal: trial plan ini sudah dipakai ditampilkan inline pada Plan

17. Pilih Client `Client Tanpa Subscription+{runId}-047`, Product `FAMS`, Plan `Growth`, isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`
18. Buat trial plan `Growth` untuk Client `Client Tanpa Subscription+{runId}-047` dan Product `FAMS` lewat sesi API aktor hingga trial tersimpan
19. Klik `[Submit]`
20. Verifikasi error inline pada field Plan "Trial already used for Growth"
21. Verifikasi `[Submit]` memblok pengajuan
22. Verifikasi modal tetap terbuka
23. Klik `[Clear Field]`

### TC-AC-CS-195: Eligibilitas gagal: sudah ada trial aktif produk sama ditampilkan inline pada Client

24. Pilih Client `PT Sejahtera`, Product `FAMS`, Plan `Growth`, isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`
25. Klik `[Submit]`
26. Verifikasi error inline pada field Client "This client already has an active trial. Wait until it expires or it converts."
27. Verifikasi modal tetap terbuka
28. Verifikasi tidak ada trial baru (jumlah trial Client `PT Sejahtera` tetap, dibaca lewat fixture BE)
29. Klik `[✕]` pada header modal
30. Verifikasi dialog Unsaved Changes tampil
31. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Satu pembukaan form untuk seluruh TC (kasus tanpa Submit sukses; `[Clear Field]` di antara kasus).
- Langkah penghubung (S-03): `Esc` menutup dropdown (langkah 7, 12), `[Clear Field]` antar kasus (langkah 16, 23), dan penutupan form dirty (langkah 29 sampai 31, S-08).
- Anchor absence (butir 8b.2): langkah 4 (Starter tampil) mendahului langkah 5.
- Pembuatan trial lewat sesi API ditulis "... hingga ... tersimpan" (R-20).
- Temuan untuk QA:
  - TC-AC-CS-179 Langkah 3 mengisi kuota "lalu klik `[Submit]`" tanpa nilai kuota; spec memakai nilai awal form (30, 50, 10).
  - TC-AC-CS-194 Precondition menyatakan trial Growth dibuat dari sesi lain tanpa menyebut aktor atau mekanismenya; ditulis sebagai kemampuan "disediakan tim FE/BE".
  - TC-AC-CS-195 Langkah 2 mengisi nilai kuota yang sama tanpa menyebut nilai; spec memakai nilai awal form.

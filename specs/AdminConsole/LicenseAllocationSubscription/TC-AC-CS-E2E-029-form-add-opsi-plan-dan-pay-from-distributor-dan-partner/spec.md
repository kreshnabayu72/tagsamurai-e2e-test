---
id: TC-AC-CS-E2E-029-form-add-opsi-plan-dan-pay-from-distributor-dan-partner
title: "Form Add: Opsi Plan dan Pay From Distributor dan Partner"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-109
  - TC-AC-CS-110
  - TC-AC-CS-556
coverage:
  web: automated
---

# Form Add: Opsi Plan dan Pay From Distributor dan Partner

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Distributor PT Maju Bersama (Pre-setup #9) `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (ganti akun eksplisit): Total Control Partner CV Karya Mandiri (Pre-setup #11) `totalControlPartnerSub_automated_{namaCompany}@qwertysystem.net` (`Lestari Wulandari`), password `Spectra.env.AC_SUB_PARTNER_TC_PASSWORD`. Akun ketiga: Total Control Partner CV Sinar Abadi (Pre-setup #88) `totalControlSinarSub_automated_{namaCompany}@qwertysystem.net` (`Maria Setiawan`), password `Spectra.env.AC_SUB_SINAR_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Client Tanpa Subscription+{runId}-029` (padanan Pre-setup #48) untuk TC-AC-CS-109; Client `Bengkel Maju Jaya+{runId}-029` binaan CV Karya Mandiri tanpa term FAMS (padanan Pre-setup #30) untuk TC-AC-CS-110; Client `Client Sinar Timur+{runId}-029` binaan langsung CV Sinar Abadi tanpa term FAMS (padanan Pre-setup #47) untuk TC-AC-CS-556; Custom Plan FAMS `Maju Custom` milik PT Maju Bersama dan Custom Plan FAMS `Custom Lain+{runId}-029` milik entitas lain (Pre-setup tidak mencantumkan nama Custom Plan entitas lain; disediakan fixture).
- Kemampuan baca BE daftar default plan SIEM yang aktif (untuk asersi langkah 7; disediakan tim FE/BE).
- Wallet: CV Karya Mandiri dengan dua kantong sumber `Partner Pocket` saldo tersedia $25,000.00 dan `Distributor Pocket` saldo tersedia $12,000.00 (Pre-setup #21); CV Sinar Abadi dengan satu kantong `Partner Pocket` saldo tersedia $25,000.00 (Pre-setup #87); harga FAMS Growth $4,000.00 per tahun (Pre-setup #27). Saldo dibaca lewat fixture BE (kemampuan disediakan tim FE/BE) dan dipulihkan di hook `after`. Submit pada TC-AC-CS-556 membuat satu term; term itu dihapus di hook `after`.

## Test Steps

### TC-AC-CS-109: Opsi Plan per Product termasuk Custom Plan milik entitas aktor

1. Klik `[+ Subscription]`
2. Pilih Client `Client Tanpa Subscription+{runId}-029` dan Product `FAMS`, lalu buka dropdown Plan
3. Verifikasi Plan FAMS memuat `Starter`, `Growth`, `Professional`, `Enterprise`, dan `Maju Custom`
4. Verifikasi Custom Plan milik entitas lain `Custom Lain+{runId}-029` tidak ada di dropdown Plan
5. Tekan `Esc` untuk menutup dropdown Plan, lalu ganti Product ke `SIEM`
6. Buka dropdown Plan
7. Verifikasi Plan SIEM memuat seluruh default plan SIEM yang aktif
8. Tekan `Esc` untuk menutup dropdown Plan, lalu klik `[✕]` pada header modal
9. Verifikasi dialog Unsaved Changes tampil
10. Klik `[Leave]`

### TC-AC-CS-110: Opsi Pay From Partner berlabel Nama dan Type

11. Logout, lalu login sebagai Total Control Partner `Lestari Wulandari` (Pre-setup #11)
12. Buka menu Allocation > Client Subscription
13. Klik `[+ Subscription]`
14. Isi Client `Bengkel Maju Jaya+{runId}-029`, Product `FAMS`, Plan `Growth`, Duration `1`
15. Buka dropdown Pay From
16. Verifikasi field Pay From Enabled dan wajib dipilih karena lebih dari satu kantong
17. Verifikasi opsi berlabel `[Nama] (Type)` untuk `Partner Pocket` dan `Distributor Pocket`
18. Tekan `Esc` untuk menutup dropdown Pay From, lalu klik `[✕]` pada header modal
19. Verifikasi dialog Unsaved Changes tampil
20. Klik `[Leave]`

### TC-AC-CS-556: Pay From Partner dengan satu kantong sumber pre-filled dan Disabled

21. Logout, lalu login sebagai Total Control Partner `Maria Setiawan` (Pre-setup #88)
22. Buka menu Allocation > Client Subscription
23. Klik `[+ Subscription]`
24. Isi Client `Client Sinar Timur+{runId}-029`, Product `FAMS`, Plan `Growth`, Duration `1`, Start Date `19/08/26`
25. Verifikasi field Pay From Disabled dan terisi `Partner Pocket`
26. Klik `[Submit]`
27. Verifikasi tidak ada error "Pay from must not be empty"
28. Verifikasi toast sukses "Success, subscription has been added." muncul
29. Verifikasi saldo `Partner Pocket` CV Sinar Abadi menjadi $21,000.00 (dibaca lewat fixture BE)

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): `Esc` menutup dropdown (langkah 5, 8, 18); pindah akun eksplisit di langkah 11 dan 21 (S-07), masing-masing diikuti `Buka menu Allocation > Client Subscription` (langkah 12 dan 22).
- Penutupan form dirty pada langkah 8 sampai 10 dan 18 sampai 20 mengikuti S-08. Langkah 5 mengganti Product sebagai bagian TC-AC-CS-109 Langkah 2.
- Urutan: TC tanpa Submit lebih dulu, TC dengan Submit (TC-AC-CS-556) di akhir (S-10).
- Temuan untuk QA:
  - TC-AC-CS-109 Expected c menyebut "seluruh default plan SIEM yang aktif" tanpa menyebut nama; TC-AC-CS-145 memakai Plan `SIEM`. Spec mengasersi seluruh default plan aktif lewat fixture.
  - TC-AC-CS-110 dan TC-AC-CS-556 tidak menyebut apakah Duration dan Start Date wajib diisi sebelum dropdown Pay From tampil; spec mengisi Duration (dan Start Date pada TC-AC-CS-556 sesuai langkah TC).
  - TC-AC-CS-110 memakai Client `Bengkel Maju Jaya` (Pre-setup #30) yang sudah punya term SAMS Expired; spec memakai seed bersuffix tanpa term FAMS.

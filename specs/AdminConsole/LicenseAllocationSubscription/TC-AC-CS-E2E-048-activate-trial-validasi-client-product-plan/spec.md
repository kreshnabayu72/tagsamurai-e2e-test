---
id: TC-AC-CS-E2E-048-activate-trial-validasi-client-product-plan
title: "Activate Trial: Validasi Client, Product, Plan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-183
  - TC-AC-CS-184
  - TC-AC-CS-185
  - TC-AC-CS-186
coverage:
  web: automated
---

# Activate Trial: Validasi Client, Product, Plan

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Client Tanpa Subscription+{runId}-048` (padanan Pre-setup #48: tanpa term dan tanpa trial). Tidak ada Submit sukses pada spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan; sesi API aktor Principal): mengarsipkan plan `Growth` hingga tersimpan lalu memulihkannya (Un-archive) di hook `after`.
- Ceiling Trial 60 hari, 200 assets, 50 users (Pre-setup #25) tidak diubah; kuota yang diisi 30 hari, 50 assets, 10 users (nilai awal form).

## Test Steps

### TC-AC-CS-183: Validasi Client wajib pada Activate Trial

1. Klik `[+ Activate Trial]`
2. Pilih Product `FAMS`, lalu isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10` tanpa memilih Client
3. Klik `[Submit]`
4. Verifikasi error inline "Client must not be empty"
5. Verifikasi modal tetap terbuka
6. Klik `[Clear Field]`

### TC-AC-CS-184: Validasi Product wajib pada Activate Trial

7. Pilih Client `Client Tanpa Subscription+{runId}-048` tanpa memilih Product
8. Klik `[Submit]`
9. Verifikasi error inline "Product must not be empty"
10. Verifikasi modal tetap terbuka
11. Klik `[Clear Field]`

### TC-AC-CS-185: Validasi Plan wajib pada Activate Trial

12. Pilih Client `Client Tanpa Subscription+{runId}-048` dan Product `FAMS`, isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10` tanpa memilih Plan
13. Klik `[Submit]`
14. Verifikasi error inline "Plan must not be empty"
15. Verifikasi modal tetap terbuka
16. Klik `[Clear Field]`

### TC-AC-CS-186: Plan di-Archive sesi lain sebelum Submit Activate Trial

17. Pilih Client `Client Tanpa Subscription+{runId}-048`, Product `FAMS`, Plan `Growth`, isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`
18. Arsipkan plan `Growth` lewat sesi API aktor hingga status Archive tersimpan
19. Klik `[Submit]`
20. Verifikasi error inline "This plan no longer exists. Please select another."
21. Buka dropdown Plan
22. Verifikasi dropdown Plan memuat sedikitnya satu opsi plan
23. Verifikasi field Plan dikosongkan dan opsi dimuat ulang tanpa plan `Growth`
24. Tekan `Esc` untuk menutup dropdown Plan
25. Verifikasi Client `Client Tanpa Subscription+{runId}-048`, Product `FAMS`, Trial Duration `30`, Trial Asset Quota `50`, dan Trial Concurrent User Quota `10` dipertahankan
26. Pulihkan plan `Growth` (Un-archive) lewat sesi API aktor, lalu klik `[✕]` pada header modal
27. Verifikasi dialog Unsaved Changes tampil
28. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Satu pembukaan form untuk seluruh TC; kasus dengan efek server (TC-AC-CS-186) berada di akhir (S-10).
- Langkah penghubung (S-03): `[Clear Field]` antar kasus dengan error inline berbeda (R-12; langkah 6, 11, 16), Un-archive plan (langkah 26; juga di hook `after`), dan penutupan form dirty (langkah 26 sampai 28, S-08).
- Anchor absence (butir 8b.2): dropdown Plan dibuka pada langkah 21 dan opsi plan lain terbukti tampil pada langkah 22 sebelum langkah 23 (tanpa plan `Growth`); `Esc` menutup dropdown pada langkah 24.
- Arsip plan lewat sesi API ditulis "... hingga ... tersimpan" (R-20).
- Temuan untuk QA:
  - TC-AC-CS-183 Langkah 2 menyebut "pilih Product `FAMS` dan Plan lalu isi kuota" tanpa menyebut Plan; Plan tidak dapat dipilih tanpa Client (TC-AC-CS-180), sehingga spec tidak memilih Plan.
  - TC-AC-CS-186 Precondition tidak menyebut cara mengarsipkan plan dari sesi lain; ditulis sebagai kemampuan "disediakan tim FE/BE".
  - TC-AC-CS-184 Langkah 2 tidak menyebut Plan atau kuota; spec hanya memilih Client.

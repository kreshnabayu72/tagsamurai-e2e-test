---
id: TC-AC-CS-E2E-032-form-add-validasi-start-date-dan-pay-from
title: "Form Add: Validasi Start Date dan Pay From"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-121
  - TC-AC-CS-122
  - TC-AC-CS-123
  - TC-AC-CS-124
coverage:
  web: automated
---

# Form Add: Validasi Start Date dan Pay From

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (ganti akun eksplisit): Total Control Partner CV Karya Mandiri (Pre-setup #11) `totalControlPartnerSub_automated_{namaCompany}@qwertysystem.net` (`Lestari Wulandari`), password `Spectra.env.AC_SUB_PARTNER_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (General Settings Principal PT ABC: Date Format `dd/MM/yy`, Time Format 24-hour, Timezone `Asia/Jakarta UTC+07:00`; Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Client Tanpa Subscription+{runId}-032` (padanan Pre-setup #48: tanpa term dan tanpa trial) untuk TC-AC-CS-121 sampai 123; Client `Bengkel Maju Jaya+{runId}-032` binaan CV Karya Mandiri tanpa term FAMS (padanan Pre-setup #30) untuk TC-AC-CS-124. Submit sukses pada TC-AC-CS-123 menghasilkan satu term milik Principal pada Client seed (dihapus di hook `after`).
- Wallet: CV Karya Mandiri dengan dua kantong sumber `Partner Pocket` saldo tersedia $25,000.00 dan `Distributor Pocket` saldo tersedia $12,000.00 (Pre-setup #21), dibaca lewat fixture BE (kemampuan disediakan tim FE/BE) dan dipulihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah term Client seed lewat fixture BE.

## Test Steps

### TC-AC-CS-121: Validasi Start Date kosong varian Add

1. Klik `[+ Subscription]`
2. Pilih Client `Client Tanpa Subscription+{runId}-032`, Product `SAMS`, Plan `Growth`, Duration `1`, kosongkan Start Date
3. Klik `[Submit]`
4. Verifikasi error inline "Start date must not be empty"
5. Verifikasi modal tetap terbuka

### TC-AC-CS-122: Validasi Start Date sebelum hari ini varian Add

6. Isi Start Date `18/08/26`
7. Klik `[Submit]`
8. Verifikasi error inline "Start date cannot be in the past"
9. Verifikasi jumlah term Client `Client Tanpa Subscription+{runId}-032` tetap 0 (dibaca lewat fixture BE)

### TC-AC-CS-123: Start Date tepat hari ini diterima varian Add

10. Isi Start Date `19/08/26`
11. Klik `[Submit]`
12. Tunggu aksi selesai (dialog/modal tertutup)
13. Verifikasi tidak ada error Start Date
14. Ketik Search `Client Tanpa Subscription+{runId}-032`, tekan Enter
15. Verifikasi term baru berstatus Active dengan Start Date `19/08/26` dan End Date `18/08/27`
16. Klik `(←)` pada kotak Search

### TC-AC-CS-124: Validasi Pay From wajib bagi Partner dengan lebih dari satu kantong

17. Logout, lalu login sebagai Total Control Partner `Lestari Wulandari` (Pre-setup #11)
18. Buka menu Allocation > Client Subscription
19. Klik `[+ Subscription]`
20. Pilih Client `Bengkel Maju Jaya+{runId}-032`, Product `FAMS`, Plan `Growth`, Duration `1`, Start Date `19/08/26` tanpa memilih Pay From
21. Klik `[Submit]`
22. Verifikasi error inline "Pay from must not be empty"
23. Verifikasi modal tetap terbuka
24. Verifikasi saldo `Partner Pocket` tetap $25,000.00 dan `Distributor Pocket` tetap $12,000.00, tanpa Reserve (dibaca lewat fixture BE)
25. Klik `[✕]` pada header modal
26. Verifikasi dialog Unsaved Changes tampil
27. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Satu pembukaan form untuk TC-AC-CS-121 sampai 123 (nilai Start Date diganti di antara kasus); TC-AC-CS-123 sebagai satu-satunya Submit sukses berada di akhir kelompok Principal (S-10).
- Langkah penghubung (S-03): Search untuk menemukan baris term baru (R-16; langkah 14), `(←)` pada kotak Search (langkah 16), dan ganti akun eksplisit di langkah 17 (S-07) yang diikuti `Buka menu Allocation > Client Subscription` (langkah 18), dan `Tunggu aksi selesai (dialog/modal tertutup)` sesudah Submit sukses (langkah 12; 8b.8). Pada TC-AC-CS-123 modal tertutup sesudah Submit sukses (checkbox Stay tidak dicentang).
- Penutupan form dirty pada langkah 25 sampai 27 mengikuti S-08.
- Temuan untuk QA:
  - TC-AC-CS-123 Expected b menyebut status Active dengan Start Date `19/08/26` tanpa menyebut toast sukses; spec tidak mengasersi toast (S-02).
  - TC-AC-CS-122 dan TC-AC-CS-124 "tidak ada record dibuat" dan "tidak ada Reserve" tidak menyebut cara cek; spec memakai pembacaan lewat fixture BE.

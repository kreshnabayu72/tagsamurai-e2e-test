---
id: TC-AC-CS-E2E-036-add-group-manager-ancestor-dan-start-date-29-februari
title: "Add: Group Manager Ancestor dan Start Date 29 Februari"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-CS-554
  - TC-AC-CS-579
  - TC-AC-CS-580
coverage:
  web: automated
---

# Add: Group Manager Ancestor dan Start Date 29 Februari

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Group Manager scope Group `Jawa`, Distributor PT Maju Bersama (Pre-setup #5) `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`), password `Spectra.env.AC_SUB_GM_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Toko Bandung Raya+{runId}-036` binaan langsung PT Maju Bersama pada group `Jawa > Jawa Barat > Bandung` (cucu group `Jawa`, dua level di bawah group yang di-assign; padanan Pre-setup #89, belum punya term SAMS) untuk TC-AC-CS-554; Client `Client Tanpa Subscription A+{runId}-036` untuk TC-AC-CS-579 dan Client `Client Tanpa Subscription B+{runId}-036` untuk TC-AC-CS-580 (padanan Pre-setup #48: group `Jawa`, tanpa term dan tanpa trial).
- State global yang diubah (suite serial) dan pemulihannya di hook `after` lewat fixture BE (disediakan tim FE/BE): toggle `Require Approval for Allocation` PT Maju Bersama (Pre-setup #23) diatur ON; saldo `Main Pocket` PT Maju Bersama $25,000.00 (Pre-setup #20) berkurang oleh Capture dan Reserve (dipulihkan antar blok dan di hook `after`); harga SAMS Growth $3,000.00 per tahun (Pre-setup #27).
- Kemampuan teknis (disediakan tim FE/BE): membaca Reserve dan Capture Wallet lewat fixture BE.
- Data uji tanggal: Start Date `29/02/28` (2028 kabisat; 2029 non-kabisat) dengan Duration `1` dan `4` (2032 kabisat).

## Test Steps

### TC-AC-CS-554: Add mode New oleh Group Manager di group induk (ancestor) memakai bypass

1. Klik `[+ Subscription]`
2. Pilih Client `Toko Bandung Raya+{runId}-036`, Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `19/08/26`
3. Klik `[Submit]`
4. Verifikasi toast sukses "Success, subscription has been added." muncul
5. Ketik Search `Toko Bandung Raya+{runId}-036`, tekan Enter
6. Verifikasi term berstatus Active, bukan Waiting for Approval
7. Verifikasi Wallet `Main Pocket` di-Capture sesuai Estimated Cost $3,000.00 (dibaca lewat fixture BE)
8. Klik `(←)` pada kotak Search, lalu pulihkan saldo `Main Pocket` ke $25,000.00 tanpa Reserve lewat fixture BE

### TC-AC-CS-579: Add mode New Start Date 29 Februari dengan Duration 1 tahun

9. Klik `[+ Subscription]`
10. Pilih Client `Client Tanpa Subscription A+{runId}-036`, Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `29/02/28`
11. Klik `[Submit]`
12. Verifikasi toast sukses "Success, subscription has been added." muncul
13. Ketik Search `Client Tanpa Subscription A+{runId}-036`, tekan Enter
14. Verifikasi baris baru berstatus Pending dengan Start Date `29/02/28`
15. Verifikasi End Date `27/02/29` (tanggal ulang tahun jatuh pada 28/02/29 karena 29/02/29 tidak ada, lalu dikurangi 1 hari)
16. Verifikasi Reserve $3,000.00 ditahan pada `Main Pocket` (dibaca lewat fixture BE)
17. Klik `(←)` pada kotak Search, lalu pulihkan saldo `Main Pocket` ke $25,000.00 tanpa Reserve lewat fixture BE

### TC-AC-CS-580: Add mode New Start Date 29 Februari dengan Duration 4 tahun

18. Klik `[+ Subscription]`
19. Pilih Client `Client Tanpa Subscription B+{runId}-036`, Product `SAMS`, Plan `Growth`, Duration `4`, Start Date `29/02/28`
20. Klik `[Submit]`
21. Verifikasi toast sukses "Success, subscription has been added." muncul
22. Ketik Search `Client Tanpa Subscription B+{runId}-036`, tekan Enter
23. Verifikasi baris baru berstatus Pending dengan Start Date `29/02/28`
24. Verifikasi End Date `28/02/32` (29/02/32 ada sehingga tanggal ulang tahun 29/02/32, lalu dikurangi 1 hari)
25. Verifikasi Reserve $12,000.00 ditahan pada `Main Pocket` (dibaca lewat fixture BE)
26. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-CS-584 (Edit Duration atas term hasil TC-AC-CS-579) ada di spec 147.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16; langkah 5, 13, 22), `(←)` pada kotak Search (langkah 8, 17, 26), dan pemulihan saldo Wallet antar blok lewat fixture BE (langkah 8, 17; pengecualian suite 2026-10-30, juga di hook `after`).
- Pada TC-AC-CS-554 Expected b, "tidak muncul di Approvals" diasersi lewat status Active (langkah 6); asersi absence di Approvals tidak ditulis karena TC tidak memberi anchor.
- Temuan untuk QA:
  - TC-AC-CS-554 Expected b menyebut "tidak muncul di Approvals" tanpa langkah observasi di Approvals; diwakili status Active.
  - TC-AC-CS-579 dan 580 menyatakan Reserve tanpa menyebut cara membacanya; spec memakai pembacaan Wallet lewat fixture BE.

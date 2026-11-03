---
id: TC-AC-ACTS-E2E-121-approvals-duplicate-existing-record-unit-paling-awal-saat-dua-unit-live-berbagi-identifier
title: "Approvals Duplicate: Existing Record Menunjuk Unit Paling Awal Terdaftar bila Dua Unit Live Berbagi Identifier"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-780
coverage:
  web: automated
---

# Approvals Duplicate: Existing Record Menunjuk Unit Paling Awal Terdaftar bila Dua Unit Live Berbagi Identifier

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Toggle ON (Local Registration aktif; jalur approval normal tanpa bypass E2a) `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun ganti di tengah spec: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Halaman awal: halaman Add Stock SKU `RFID-ASSET-CORE-R5` (dari Stock List lewat row action Add Stock), dibuka oleh hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Kelas d (harness eksternal): simulator reader RFID (scan, `[Add by Scan]`, `[Stop]`) disediakan tim FE; mekanismenya tidak dikarang di spec.
- SKU `RFID-ASSET-CORE-R5` (Data Pre-setup #12). Dua unit Available berbagi UID `A1B2C3D4E5F6` (Data Dinamis #1): unit U1 terdaftar lebih awal dan unit U2 terdaftar kemudian lewat Approve Register Duplicate. Identifier tetap tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE sebelum spec ini; Subject yang dibuat spec ini dihapus lewat fixture BE di hook `after`. Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Kemampuan teknis disediakan tim FE/BE: kemampuan baca jumlah Subject di Approvals > TAG Stock > Tab Active (baseline, S-12).
- Env var password akun aktor: `Spectra.env.AC_DIST_ON_PASSWORD`, `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_DIST_ON_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-780: Existing Record unit paling awal terdaftar bila lebih dari satu unit live memegang identifier yang sama

1. Klik `[Add by Scan]`
2. Scan TAG dengan UID `A1B2C3D4E5F6` dan EPC baru lewat simulator reader RFID
3. Klik `[Stop]`
4. Klik `[Submit]`
5. Verifikasi toast "Success, 1 TAG has been sent for approval."
6. Verifikasi tidak ada toast error konflik unik ("Error, failed to register TAGs.")
7. Ganti akun: klik Logout
8. Login sebagai Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`)
9. Buka Approvals > TAG Stock > Tab Active
10. Verifikasi hanya satu Subject dibuat (jumlah Subject bertambah tepat 1)
11. Klik `Review` pada Subject baru
12. Verifikasi Existing Record pada kolom dan blok Existing Record di dialog menunjuk unit U1 (paling awal terdaftar), bukan U2
13. Verifikasi Matched Identifier `A1B2C3D4E5F6` dengan badge `[UID]`
14. Klik `[Cancel]`

## Notes

- Mode: FE+BE.
- Langkah penghubung tanpa Verifikasi (S-03): langkah ganti akun dan buka Approvals, serta `[Cancel]` menutup dialog Review. Baseline jumlah Subject dicatat di hook `before` lewat kemampuan baca.
- Klausa d TC-AC-ACTS-780 ("dua unit live berbagi identifier tidak menimbulkan error konflik unik") diasersi lewat toast sukses dan tidak adanya toast error pada Submit (langkah 5 dan 6).
- Temuan untuk QA:
  - TC-AC-ACTS-780 menyebut "Login ulang sbg Total Control" tanpa menyebut akun Distributor sebagai aktor awal; spec memakai Distributor Toggle ON (ACC TC).
  - TC-AC-ACTS-780 tidak menyebut toast hasil Submit; spec memakai toast "Success, 1 TAG has been sent for approval." (T-04).

---
id: TC-FA-PREF-E2E-048-versi-tdc-dan-transaksi-bertanggal-dibuat-setelah-dialog-save-terbuka
title: "Versi Tax Depreciation Class dan baris Disposal Executed dibuat setelah dialog D-01 terbuka menolak Save"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-221
  - TC-FA-PREF-225
sourceRules: ["F-FAPREF-01.k19d", "V-09", "E-FAPREF-38", "F-FAPREF-01.k23", "V-10", "E-FAPREF-42"]
smoke: []
dependsOn: []
trace:
  "F-FAPREF-01.k19d": [5, 6]
  "V-09": 7
  "E-FAPREF-38": 8
  "F-FAPREF-01.k23": [15, 16]
  "V-10": 17
  "E-FAPREF-42": 18
coverage:
  web: automated
---

# Versi Tax Depreciation Class dan baris Disposal Executed dibuat setelah dialog D-01 terbuka menolak Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: seri PB (TC-FA-PREF-176-361), company `PT Contoh Konstruksi` plan Growth (PB-1): Preferences nilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, akun default kosong, Journal Grouping Group), tidak ada penyusutan diposting, Tax Depreciation Class hanya versi pertama tanpa Effective From, tidak ada catatan berefek akuntansi. Untuk TC-FA-PREF-221: Tax Depreciation Class hanya versi pertama tanpa Effective From; untuk TC-FA-PREF-225: tidak ada catatan berefek akuntansi.
- Kemampuan teknis: fixture BE untuk membuat versi kedua Tax Depreciation Class dengan Effective From 01/07/26 (DB-2) dan baris Disposal berstatus Executed dengan Execution date 15/05/26 (DB-3) setelah dialog Save terbuka, serta menghapus keduanya; disediakan tim FE/BE, hanya pemicu state. Langkah pemicu ditulis "... hingga ... tersimpan".
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`. Hook `after` spec ini memulihkan state server yang diubah spec ke nilai awal.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-221: Versi Tax Depreciation Class ber-Effective From dibuat setelah D-01 terbuka menolak Save dengan V-09

1. Ubah Select Fiscal Year Start dari "January" menjadi "April"
2. Klik `[Save changes]` sampai dialog D-01 tampil
3. Lewat fixture BE, buat versi kedua Tax Depreciation Class dengan Effective From 01/07/26 hingga tersimpan
4. Klik `[Save]` pada dialog D-01
5. Verifikasi dialog D-01 ditutup
6. Verifikasi form tetap memuat seluruh perubahan yang belum disimpan
7. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tampil pada Select Fiscal Year Start
8. Verifikasi tidak ada toast
9. Klik `[Cancel]`

### TC-FA-PREF-225: Baris Disposal Executed dibuat setelah D-01 terbuka menolak Save dengan V-10

10. Hapus versi kedua Tax Depreciation Class (kembali ke versi pertama saja) lewat fixture BE hingga terhapus
11. Ubah Select bulan First Accounting Period dari "March" menjadi "June"
12. Klik `[Save changes]` sampai dialog D-01 tampil
13. Lewat fixture BE, buat baris Disposal berstatus Executed dengan Execution date 15/05/26 hingga tersimpan
14. Klik `[Save]` pada dialog D-01
15. Verifikasi dialog D-01 ditutup
16. Verifikasi form tetap memuat seluruh perubahan yang belum disimpan
17. Verifikasi caption "First accounting period cannot be later than May 2026, the earliest disposal or value change." tampil pada First Accounting Period
18. Verifikasi tidak ada toast
19. Klik `[Cancel]`

## Notes
- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): mengembalikan form dirty ke nilai tersimpan dengan `[Cancel]` (S-09): langkah 9, 19; memulihkan state server lewat seed/API sebelum TC berikutnya: langkah 10.
- Pemicu versi Tax Depreciation Class dan baris Disposal Executed lewat fixture BE.
- Temuan untuk QA:
  - TC-FA-PREF-221 dan 225 tidak mencantumkan isi dialog D-01 pada Expected; spec tidak mengasersinya.
  - Post Condition TC yang tidak punya langkah observasi di TC (nilai tersimpan, kalender periode mengikuti nilai baru, entri log) tidak diasersi; Post Condition "tidak ada entri log baru" dicatat sebagai rujukan ke spec absence (S-05) dan tidak diklaim teruji di spec ini.

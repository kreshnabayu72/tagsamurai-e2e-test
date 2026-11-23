---
id: TC-FA-PREF-E2E-176-versi-tdc-dan-transaksi-bertanggal-dibuat-saat-dialog-save-changes-terbuka-menolak-save
title: "Versi Tax Depreciation Class dan transaksi bertanggal dibuat saat dialog Save Changes terbuka menolak Save"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-581
  - TC-FA-PREF-582
sourceRules: ["D-01", "PV-04", "PV-05", "F-FAPREF-01.k19d", "V-09", "E-FAPREF-38", "F-FAPREF-01.k23", "V-10", "E-FAPREF-42"]
smoke: []
dependsOn: []
trace:
  "D-01": [3, 14]
  "PV-04": [3, 14]
  "PV-05": 3
  "F-FAPREF-01.k19d": [6, 8]
  "V-09": 7
  "E-FAPREF-38": 9
  "F-FAPREF-01.k23": [17, 19]
  "V-10": 18
  "E-FAPREF-42": 20
coverage:
  web: automated
---

# Versi Tax Depreciation Class dan transaksi bertanggal dibuat saat dialog Save Changes terbuka menolak Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Jam sistem: bulan berjalan Oktober 2026 menurut Time Zone entitas, dasar hitungan "The period calendar will have 13 accounting periods." dan "The period calendar will have 7 accounting periods."; jam server dan browser diatur lewat kendali jam (butir "Kendali jam sistem" di `suite.md`) di hook `before` dan dipulihkan di hook `after` spec ini.
- Data: seri PC (TC-FA-PREF-362-621), company `PT Contoh Konstruksi` plan Growth (PC-1): Preferences nilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, akun default kosong), belum ada Run Posted. Untuk TC-FA-PREF-581 dan 582: belum ada transaksi bertanggal dan belum ada versi Tax Depreciation Class ber-Effective From.
- Kemampuan teknis: fixture BE untuk membuat versi kedua Tax Depreciation Class dengan Effective From dan transaksi bertanggal 15 Mei 2026 setelah dialog Save Changes terbuka, serta menghapus keduanya; disediakan tim FE/BE, hanya pemicu state. Langkah pemicu ditulis "... hingga ... tersimpan".
- Kemampuan teknis: Baca state Preferences dan akun Chart of Accounts di server (kemampuan baca state BE) disediakan tim FE/BE tanpa endpoint karangan; dipakai untuk Expected "tidak ada yang tersimpan".
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`. Hook `after` spec ini memulihkan state server yang diubah spec ke nilai awal.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-581: Versi Tax Depreciation Class dibuat saat dialog Save Changes terbuka membuat Save Fiscal Year Start ditolak V-09

1. Pilih "April" pada Select Fiscal Year Start
2. Klik `[Save changes]`
3. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "The period calendar will have 13 accounting periods."; "Tax year start also follows Fiscal Year Start.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
4. Lewat fixture BE (pengganti sesi B), buat versi kedua dengan Effective From pada satu kelas Tax Depreciation Class hingga tersimpan
5. Klik `[Save]` pada dialog "Save Changes"
6. Verifikasi dialog "Save Changes" tertutup
7. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tampil pada field Fiscal Year Start
8. Verifikasi form tetap memuat April sebagai perubahan yang belum disimpan
9. Verifikasi tidak ada yang tersimpan: Fiscal Year Start tersimpan tetap January
10. Klik `[Cancel]`

### TC-FA-PREF-582: Transaksi bertanggal dibuat saat dialog Save Changes terbuka membuat Save First Accounting Period ditolak V-10

11. Hapus versi kedua Tax Depreciation Class lewat fixture BE hingga terhapus
12. Pilih bulan "June" dan tahun "2026" pada Select First Accounting Period
13. Klik `[Save changes]`
14. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "The period calendar will have 7 accounting periods.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
15. Lewat fixture BE (pengganti sesi B), buat transaksi bertanggal 15 Mei 2026 pada modul transaksi aset hingga tersimpan
16. Klik `[Save]` pada dialog "Save Changes"
17. Verifikasi dialog "Save Changes" tertutup
18. Verifikasi caption "First accounting period cannot be later than existing dated transactions." tampil pada field First Accounting Period
19. Verifikasi form tetap memuat Jun 2026 sebagai perubahan yang belum disimpan
20. Verifikasi tidak ada yang tersimpan: First Accounting Period tersimpan tetap Mar 2026
21. Klik `[Cancel]`

## Notes
- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): mengembalikan form dirty ke nilai tersimpan dengan `[Cancel]` (S-09): langkah 10, 21; memulihkan state server lewat seed/API sebelum TC berikutnya: langkah 11.
- Pemicu versi Tax Depreciation Class dan transaksi bertanggal lewat fixture BE; sesi B TC-FA-PREF-581 dan 582 tidak dipakai sebagai sesi UI karena hanya memicu state (Temuan untuk QA).
- Temuan untuk QA:
  - TC-FA-PREF-581 dan 582 meminta sesi B lewat UI (Tax Depreciation Class, modul transaksi aset) dan Data Dinamis DC-7 menyebutnya "hanya untuk eksekusi manual"; spec memakai fixture BE sebagai pemicu agar tetap otomatis. Email akun sesi A (Rina Anggraini, PC-8) tidak tertulis di Pre-setup; spec memakai akun aktor Total Control suite.
  - TC-FA-PREF-581 dan 582 tidak menyebut cara membaca "tidak ada yang tersimpan"; spec memakai kemampuan baca state BE.
  - Post Condition TC yang tidak punya langkah observasi di TC (nilai tersimpan, kalender periode Derived view, entri log) tidak diasersi; Post Condition "tidak ada entri log baru" dicatat sebagai rujukan ke spec absence (S-05) dan tidak diklaim teruji di spec ini.

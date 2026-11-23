---
id: TC-FA-PREF-E2E-047-first-accounting-period-batas-transaksi-bertanggal-15-mei-2026-seri-pc
title: "First Accounting Period terhadap catatan berefek akuntansi terawal (Disposal Executed 15 Mei 2026): April, Mei, dan Juni (seri PC)"
layer: ui-e2e
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-585
  - TC-FA-PREF-586
  - TC-FA-PREF-587
sourceRules: ["D-01", "PV-04", "F-FAPREF-01.k23", "V-10", "E-FAPREF-42", "T-01", "E-FAPREF-37"]
smoke: []
dependsOn: []
trace:
  "D-01": [3, 12, 20]
  "PV-04": [3, 12, 20]
  "F-FAPREF-01.k23": [5, 7]
  "V-10": 6
  "E-FAPREF-42": 8
  "T-01": [14, 22]
  "E-FAPREF-37": [15, 23]
coverage:
  web: automated
---

# First Accounting Period terhadap catatan berefek akuntansi terawal (Disposal Executed 15 Mei 2026): April, Mei, dan Juni (seri PC)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Jam sistem: bulan berjalan Oktober 2026 menurut Time Zone entitas, dasar hitungan "The period calendar will have 7 accounting periods.", "The period calendar will have 9 accounting periods." dan "The period calendar will have 8 accounting periods."; jam server dan browser diatur lewat kendali jam (butir "Kendali jam sistem" di `suite.md`) di hook `before` dan dipulihkan di hook `after` spec ini.
- Data: seri PC (TC-FA-PREF-362-621), company `PT Contoh Konstruksi` plan Growth (PC-1): Preferences nilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, akun default kosong), belum ada posting penyusutan. Catatan berefek akuntansi terawal: baris Disposal Executed ber-Execution date 15 Mei 2026 (PC-4); First Accounting Period tersimpan Mar 2026 dan Fiscal Year Start tersimpan January.
- Kemampuan teknis: Baca state Preferences, kalender periode, dan akun Chart of Accounts di server (kemampuan baca state BE) disediakan tim FE/BE tanpa endpoint karangan; dipakai untuk Expected "tidak ada yang tersimpan".
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`. Hook `after` spec ini memulihkan state server yang diubah spec ke nilai awal.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-587: First Accounting Period Jun 2026 terhadap catatan berefek akuntansi terawal (Disposal Executed 15 Mei 2026) ditolak

1. Pilih bulan "June" dan tahun "2026" pada Select First Accounting Period
2. Klik `[Save changes]`
3. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "The period calendar will have 7 accounting periods.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
4. Klik `[Save]` pada dialog "Save Changes"
5. Verifikasi dialog "Save Changes" tertutup
6. Verifikasi caption "First accounting period cannot be later than May 2026, the earliest disposal or value change." tampil pada field First Accounting Period
7. Verifikasi form tetap memuat Jun 2026 sebagai perubahan yang belum disimpan
8. Verifikasi tidak ada yang tersimpan: First Accounting Period tersimpan tetap Mar 2026
9. Klik `[Cancel]`

### TC-FA-PREF-585: First Accounting Period Apr 2026 terhadap catatan berefek akuntansi terawal (Disposal Executed 15 Mei 2026) diterima

10. Pilih bulan "April" dan tahun "2026" pada Select First Accounting Period
11. Klik `[Save changes]`
12. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "The period calendar will have 9 accounting periods.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
13. Klik `[Save]` pada dialog "Save Changes"
14. Verifikasi toast "Success, accounting preferences have been saved." tampil
15. Verifikasi First Accounting Period menampilkan Apr 2026

### TC-FA-PREF-586: First Accounting Period May 2026 terhadap catatan berefek akuntansi terawal (Disposal Executed 15 Mei 2026) diterima

16. Pulihkan First Accounting Period ke Mar 2026 lewat seed API hingga tersimpan
17. Buka ulang Fixed Asset > Settings > Accounting > Preferences
18. Pilih bulan "May" dan tahun "2026" pada Select First Accounting Period
19. Klik `[Save changes]`
20. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "The period calendar will have 8 accounting periods.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
21. Klik `[Save]` pada dialog "Save Changes"
22. Verifikasi toast "Success, accounting preferences have been saved." tampil
23. Verifikasi First Accounting Period menampilkan May 2026

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): mengembalikan form dirty ke nilai tersimpan dengan `[Cancel]` (S-09): langkah 9; memulihkan state server lewat seed/API sebelum TC berikutnya: langkah 16; membuka ulang halaman Preferences agar form memuat nilai tersimpan: langkah 17.
- Urutan TC diubah dari 585, 586, 587 menjadi 587, 585, 586: Save yang ditolak lebih dulu (S-10, S-05).
- Temuan untuk QA:
  - TC-FA-PREF-585 sampai 587 menulis langkah "Amati dialog Save Changes dan klik [Save]"; spec memecahnya menjadi Verifikasi dialog lalu klik `[Save]`.
  - Post Condition TC yang tidak punya langkah observasi di TC (nilai tersimpan, kalender periode mengikuti nilai baru, entri log) tidak diasersi; Post Condition "tidak ada entri log baru" dicatat sebagai rujukan ke spec absence (S-05) dan tidak diklaim teruji di spec ini.

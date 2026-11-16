---
id: TC-FA-PREF-E2E-046-first-accounting-period-batas-transaksi-bertanggal-paling-awal-seri-pb
title: "Save First Accounting Period terhadap transaksi bertanggal paling awal: batas satu bulan sebelum, sama, dan sesudah (seri PB)"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-222
  - TC-FA-PREF-223
  - TC-FA-PREF-224
  - TC-FA-PREF-226
sourceRules: ["F-FAPREF-01.k23", "V-10", "E-FAPREF-42", "F-FAPREF-01.k21b", "T-01", "E-FAPREF-37"]
smoke: []
dependsOn: []
trace:
  "F-FAPREF-01.k23": [4, 5]
  "V-10": [6, 34]
  "E-FAPREF-42": 7
  "F-FAPREF-01.k21b": [12, 22, 32]
  "T-01": [13, 23, 33]
  "E-FAPREF-37": [14, 15, 16, 24, 25, 26, 35]
coverage:
  web: automated
---

# Save First Accounting Period terhadap transaksi bertanggal paling awal: batas satu bulan sebelum, sama, dan sesudah (seri PB)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: seri PB (TC-FA-PREF-176-361), company `PT Contoh Konstruksi` plan Growth (PB-1): Preferences nilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, akun default kosong, Journal Grouping Group), periode Mar 2026 sampai Dec 2026 Open, tidak ada penyusutan diposting, Tax Depreciation Class hanya versi pertama tanpa Effective From, tidak ada transaksi bertanggal. Transaksi bertanggal paling awal: aktivasi aset bertanggal 15/05/26 (PB-9, M = Mei 2026); untuk TC-FA-PREF-226 tidak ada versi Tax Depreciation Class ber-Effective From.
- Data: akun Chart of Accounts PB-2.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`. Hook `after` spec ini memulihkan state server yang diubah spec ke nilai awal.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-224: Save First Accounting Period ke satu bulan setelah transaksi bertanggal paling awal ditolak V-10

1. Ubah Select bulan First Accounting Period dari "March" menjadi "June" dan Select tahun menjadi "2026"
2. Klik `[Save changes]`
3. Klik `[Save]` pada dialog D-01
4. Verifikasi dialog D-01 ditutup
5. Verifikasi form tetap memuat seluruh perubahan yang belum disimpan
6. Verifikasi caption "First accounting period cannot be later than existing dated transactions." tampil pada First Accounting Period
7. Verifikasi tidak ada toast
8. Klik `[Cancel]`

### TC-FA-PREF-222: Save First Accounting Period ke satu bulan sebelum transaksi bertanggal paling awal diizinkan

9. Ubah Select bulan First Accounting Period dari "March" menjadi "April" dan Select tahun menjadi "2026"
10. Klik `[Save changes]`
11. Klik `[Save]` pada dialog D-01
12. Verifikasi dialog D-01 tertutup
13. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
14. Verifikasi tidak ada caption V-10
15. Verifikasi Select bulan First Accounting Period menampilkan "April"
16. Verifikasi Select tahun menampilkan "2026"

### TC-FA-PREF-223: Save First Accounting Period ke bulan yang sama dengan transaksi bertanggal paling awal diizinkan

17. Pulihkan First Accounting Period ke Mar 2026 lewat seed API hingga tersimpan
18. Buka ulang Fixed Asset > Settings > Accounting > Preferences
19. Ubah Select bulan First Accounting Period dari "March" menjadi "May" dan Select tahun menjadi "2026"
20. Klik `[Save changes]`
21. Klik `[Save]` pada dialog D-01
22. Verifikasi dialog D-01 tertutup
23. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
24. Verifikasi tidak ada caption V-10
25. Verifikasi Select bulan First Accounting Period menampilkan "May"
26. Verifikasi Select tahun menampilkan "2026"

### TC-FA-PREF-226: Save hanya mengubah Fiscal Year Start tidak ditolak V-10 walau ada transaksi bertanggal

27. Pulihkan Preferences ke nilai awal PB-1 (Fiscal Year Start January, First Accounting Period Mar 2026) lewat seed API hingga tersimpan
28. Buka ulang Fixed Asset > Settings > Accounting > Preferences
29. Ubah Select Fiscal Year Start dari "January" menjadi "July"
30. Klik `[Save changes]`
31. Klik `[Save]` pada dialog D-01
32. Verifikasi dialog D-01 tertutup
33. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
34. Verifikasi tidak ada caption V-10
35. Verifikasi Select Fiscal Year Start menampilkan "July"

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): mengembalikan form dirty ke nilai tersimpan dengan `[Cancel]` (S-09): langkah 8; memulihkan state server lewat seed/API sebelum TC berikutnya: langkah 17, 27; membuka ulang halaman Preferences agar form memuat nilai tersimpan: langkah 18, 28.
- Urutan TC diubah dari 222, 223, 224, 226 menjadi 224, 222, 223, 226: Save yang ditolak lebih dulu (S-10, S-05).
- Temuan untuk QA:
  - TC-FA-PREF-222 sampai 226 tidak mencantumkan isi dialog D-01 pada Expected; spec tidak mengasersinya.
  - TC-FA-PREF-222 sampai 224 menyebut tahun "2026" pada langkah; nilai awal tahun First Accounting Period (2026) tidak tertulis eksplisit di Precondition selain "Mar 2026".
  - Post Condition TC yang tidak punya langkah observasi di TC (nilai tersimpan, periode dibangun ulang, entri log) tidak diasersi; Post Condition "tidak ada entri log baru" dicatat sebagai rujukan ke spec absence (S-05) dan tidak diklaim teruji di spec ini.

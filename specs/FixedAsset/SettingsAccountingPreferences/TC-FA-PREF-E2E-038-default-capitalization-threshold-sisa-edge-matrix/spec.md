---
id: TC-FA-PREF-E2E-038-default-capitalization-threshold-sisa-edge-matrix
title: "Default Capitalization Threshold sisa edge matrix: V-01, V-02, V-03, digit desimal ketiga, nilai 0, dan 16 digit dengan 2 desimal"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-551
  - TC-FA-PREF-552
  - TC-FA-PREF-553
  - TC-FA-PREF-554
  - TC-FA-PREF-555
coverage:
  web: automated
---

# Default Capitalization Threshold sisa edge matrix: V-01, V-02, V-03, digit desimal ketiga, nilai 0, dan 16 digit dengan 2 desimal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: seri PC (TC-FA-PREF-362-621), company `PT Contoh Konstruksi` plan Growth (PC-1): Preferences nilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, akun default kosong), periode Mar 2026 sampai Dec 2026 Open, belum ada posting penyusutan.
- Data: Asset Class Vehicles dan Furniture tidak mengisi threshold sendiri (PC-1, PC-6), sehingga dialog "Save Changes" memuat bullet "2 asset classes use the default threshold.". Format angka platform: pemisah ribuan titik, desimal koma, mata uang Rupiah.
- Kemampuan teknis: Baca state Preferences, periode akuntansi, dan akun Chart of Accounts di server (kemampuan baca state BE) disediakan tim FE/BE tanpa endpoint karangan; dipakai untuk Expected "tidak ada yang tersimpan".
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`. Hook `after` spec ini memulihkan state server yang diubah spec ke nilai awal.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-551: Default Capitalization Threshold bernilai minus menampilkan caption V-02 langsung dan Save ditolak

1. Ketik "-1" pada CurrencyInput Default Capitalization Threshold
2. Verifikasi input menerima tanda minus
3. Verifikasi caption "Capitalization threshold must be 0 or more" tampil langsung pada field tanpa menunggu Save
4. Klik `[Save changes]`
5. Verifikasi tidak ada dialog "Save Changes"
6. Verifikasi tidak ada yang tersimpan: Default Capitalization Threshold tersimpan tetap 5.000.000
7. Klik `[Cancel]`

### TC-FA-PREF-552: Digit bulat ke-17 menampilkan caption V-03 langsung dan Save ditolak

8. Ketik "12345678901234567" pada CurrencyInput Default Capitalization Threshold
9. Verifikasi input menerima digit ke-17
10. Verifikasi caption "Capitalization threshold is too large" tampil langsung pada field tanpa menunggu Save
11. Klik `[Save changes]`
12. Verifikasi tidak ada dialog "Save Changes"
13. Verifikasi tidak ada yang tersimpan: Default Capitalization Threshold tersimpan tetap 5.000.000
14. Klik `[Cancel]`

### TC-FA-PREF-553: Digit desimal ke-3 diblok di input tanpa caption

15. Ketik "10,255" pada CurrencyInput Default Capitalization Threshold
16. Verifikasi input menampilkan 10,25 karena digit desimal ke-3 diblok
17. Verifikasi tidak ada caption pada field
18. Klik `[Cancel]`

### TC-FA-PREF-554: Default Capitalization Threshold bernilai 0 diterima dan disimpan

19. Ubah Default Capitalization Threshold menjadi "0"
20. Klik `[Save changes]`
21. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "2 asset classes use the default threshold.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
22. Klik `[Save]` pada dialog
23. Verifikasi toast "Success, accounting preferences have been saved." tampil
24. Verifikasi Default Capitalization Threshold menampilkan 0

### TC-FA-PREF-555: Default Capitalization Threshold 16 digit bulat dengan 2 desimal diterima dan disimpan

25. Pulihkan Preferences ke nilai awal PC-1 (Default Capitalization Threshold 5.000.000) lewat seed API hingga tersimpan
26. Buka ulang Fixed Asset > Settings > Accounting > Preferences
27. Ubah Default Capitalization Threshold menjadi "9999999999999999,99"
28. Klik `[Save changes]`
29. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "2 asset classes use the default threshold.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
30. Klik `[Save]` pada dialog
31. Verifikasi toast "Success, accounting preferences have been saved." tampil
32. Verifikasi Default Capitalization Threshold menampilkan Rp 9.999.999.999.999.999,99
33. Verifikasi tidak ada caption pada field

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): mengembalikan form dirty ke nilai tersimpan dengan `[Cancel]` (S-09): langkah 7, 14, 18; memulihkan state server lewat seed/API sebelum TC berikutnya: langkah 25; membuka ulang halaman Preferences agar form memuat nilai tersimpan: langkah 26.
- Urutan: TC-FA-PREF-551 sampai 553 (validasi diblokir, tanpa Save sukses) lebih dulu, lalu TC-FA-PREF-554 dan 555 (Save sukses) sesuai S-10. Preferences dipulihkan pada awal blok TC-FA-PREF-555 dan oleh hook `after` setelah TC-FA-PREF-555.
- Temuan untuk QA:
  - TC-FA-PREF-551 dan 552 menyebut "tidak ada yang tersimpan" sebagai Expected; spec membacanya lewat kemampuan baca state BE (Prerequisites) karena TC tidak memberi cara cek lain.
  - Post Condition TC yang tidak punya langkah observasi di TC (nilai tersimpan, periode dibangun ulang, entri log) tidak diasersi; Post Condition "tidak ada entri log baru" dicatat sebagai rujukan ke spec absence (S-05) dan tidak diklaim teruji di spec ini.

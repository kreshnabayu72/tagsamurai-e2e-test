---
id: TC-FA-PREF-E2E-062-d01-pv04-pv05-pembangunan-ulang-periode-dan-awal-tahun-fiskal
title: "D-01 PV-04 dan PV-05: Pembangunan Ulang Periode dan Awal Tahun Fiskal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-194
  - TC-FA-PREF-195
  - TC-FA-PREF-196
  - TC-FA-PREF-197
coverage:
  web: automated
---

# D-01 PV-04 dan PV-05: Pembangunan Ulang Periode dan Awal Tahun Fiskal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; periode Mar 2026 sampai Dec 2026 Open; belum ada penyusutan diposting) dan PB-2 (akun Chart of Accounts uji).
- Jam sistem fixture: bulan berjalan menurut Time Zone entitas = Oktober 2026 (dasar hitungan periode D-01); spec tidak mengubah jam.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Langkah muat ulang saat form dirty: dialog `beforeunload` dikonfirmasi (kemampuan disediakan tim FE; dipakai pada langkah pemulihan).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-194: PV-04 dan PV-05 saat Fiscal Year Start berubah dari January ke July

1. Ubah Select Fiscal Year Start dari "January" menjadi "July"
2. Klik [Save changes]
3. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
4. Verifikasi body dialog memuat daftar bullet: "16 accounting periods will be rebuilt."; "Tax year start also follows Fiscal Year Start."
5. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
6. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
7. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

### TC-FA-PREF-195: PV-04 tanpa PV-05 saat hanya First Accounting Period berubah ke Jan 2026

8. Ubah Select bulan First Accounting Period dari "March" menjadi "January" dengan Select tahun tetap "2026"
9. Klik [Save changes]
10. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
11. Verifikasi body dialog memuat daftar bullet: "12 accounting periods will be rebuilt."
12. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
13. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
14. Verifikasi dialog D-01 tidak memuat bullet "Tax year start also follows Fiscal Year Start."
15. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

### TC-FA-PREF-196: PV-04 bentuk tunggal saat hasil pembangunan ulang hanya 1 periode

16. Seed varian PB-10 lewat API (First Accounting Period tersimpan Oct 2026; periode Oct 2026 sampai Dec 2026 Open)
17. Ubah Select Fiscal Year Start dari "January" menjadi "November"
18. Klik [Save changes]
19. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
20. Verifikasi body dialog memuat daftar bullet: "1 accounting period will be rebuilt."; "Tax year start also follows Fiscal Year Start."
21. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
22. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
23. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

### TC-FA-PREF-197: PV-04 dengan hitungan besar saat First Accounting Period diubah ke Jan 2000

24. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5
25. Ubah Select tahun First Accounting Period menjadi "2000"
26. Ubah Select bulan First Accounting Period menjadi "January"
27. Klik [Save changes]
28. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
29. Verifikasi body dialog memuat daftar bullet: "324 accounting periods will be rebuilt."
30. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
31. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
32. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

## Notes

- Langkah penghubung (S-03): seed varian PB-10, pemulihan ke PB-1, dan membuang perubahan form dengan F5 setelah tiap TC.
- Hitungan periode bergantung pada bulan berjalan fixture (Oktober 2026) dan First Accounting Period tersimpan; nilai bullet mengikuti Data Uji TC.
- Temuan untuk QA:
  - Post Condition "Preferences company belum berubah ..." tidak punya langkah observasi di TC ini, sehingga tidak diasersi (S-01).

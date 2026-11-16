---
id: TC-FA-PREF-E2E-058-d01-screening-dan-hitungan-pv01-asset-class-threshold-default
title: "D-01 Screening dan Hitungan PV-01 (Asset Class Memakai Threshold Default)"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-183
  - TC-FA-PREF-184
  - TC-FA-PREF-185
  - TC-FA-PREF-186
sourceRules: ["D-01", "PV-01", "F-FAPREF-01.k21c"]
smoke: []
dependsOn: []
trace:
  "D-01": [3, 5, 6, 12, 14, 15, 20, 22, 23, 28, 30, 31]
  "PV-01": [4, 13, 21, 29]
  "F-FAPREF-01.k21c": 8
anchor: [7]
coverage:
  web: automated
---

# D-01 Screening dan Hitungan PV-01 (Asset Class Memakai Threshold Default)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; periode Mar 2026 sampai Dec 2026 Open; belum ada penyusutan diposting) dan PB-2 (akun Chart of Accounts uji). PB-3 (Asset Class IT Equipment, Vehicles, Furniture). Varian PB-4 (hanya IT Equipment tanpa threshold sendiri) dan PB-5 (ketiganya mengisi threshold dan akun sendiri) dibentuk lewat seed API pada langkah penghubung.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Langkah muat ulang saat form dirty: dialog `beforeunload` dikonfirmasi (kemampuan disediakan tim FE; dipakai pada langkah pemulihan).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-183: Screening dialog D-01 Save Changes saat Default Capitalization Threshold diubah

1. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
2. Klik [Save changes]
3. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
4. Verifikasi body dialog memuat daftar bullet: "2 asset classes use the default threshold."
5. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
6. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
7. Verifikasi tidak ada toast yang tampil
8. Verifikasi form di belakang dialog masih memuat nilai "Rp 10.000.000,00" yang belum disimpan
9. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

### TC-FA-PREF-184: D-01 menampilkan PV-01 bentuk jamak saat 2 Asset Class memakai threshold default

10. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
11. Klik [Save changes]
12. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
13. Verifikasi body dialog memuat daftar bullet: "2 asset classes use the default threshold."
14. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
15. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
16. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

### TC-FA-PREF-185: D-01 menampilkan PV-01 bentuk tunggal saat 1 Asset Class memakai threshold default

17. Seed varian PB-4 lewat API (hanya IT Equipment yang tidak mengisi threshold sendiri)
18. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
19. Klik [Save changes]
20. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
21. Verifikasi body dialog memuat daftar bullet: "1 asset class uses the default threshold."
22. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
23. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
24. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

### TC-FA-PREF-186: D-01 menampilkan PV-01 bentuk N dengan hitungan 0

25. Seed varian PB-5 lewat API (seluruh Asset Class mengisi threshold dan akun sendiri)
26. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
27. Klik [Save changes]
28. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
29. Verifikasi body dialog memuat daftar bullet: "0 asset classes use the default threshold."
30. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
31. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
32. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)
33. Pulihkan Asset Class ke PB-3 lewat seed API

## Notes

- Langkah penghubung (S-03): membuang perubahan form dengan F5 setelah tiap TC (dialog D-01 tidak disimpan) dan seed varian Asset Class.
- Asersi tidak ada toast pada TC-183 didahului Verifikasi dialog D-01 tampil sebagai anchor positif.
- Temuan untuk QA:
  - Post Condition "Preferences company belum berubah ..." tidak punya langkah observasi di TC ini, sehingga tidak diasersi (S-01).

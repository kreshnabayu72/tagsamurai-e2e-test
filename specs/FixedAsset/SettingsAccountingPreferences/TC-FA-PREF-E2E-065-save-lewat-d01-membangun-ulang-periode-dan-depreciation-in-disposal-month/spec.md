---
id: TC-FA-PREF-E2E-065-save-lewat-d01-membangun-ulang-periode-dan-depreciation-in-disposal-month
title: "Save Lewat D-01 Membangun Ulang Periode: Fiscal Year Start, First Accounting Period, Depreciation in Disposal Month"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-207
  - TC-FA-PREF-208
  - TC-FA-PREF-209
coverage:
  web: automated
---

# Save Lewat D-01 Membangun Ulang Periode: Fiscal Year Start, First Accounting Period, Depreciation in Disposal Month

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; periode Mar 2026 sampai Dec 2026 Open; belum ada penyusutan diposting) dan PB-2 (akun Chart of Accounts uji). PB-6b (2 pelepasan menunggu posting) untuk TC-209.
- Jam sistem fixture: bulan berjalan menurut Time Zone entitas = Oktober 2026 (dasar hitungan periode D-01); spec tidak mengubah jam.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Data Dinamis DB-1 (nilai Preferences hasil Save) dipulihkan ke PB-1 lewat seed API sebelum TC berikutnya dan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-207: Save mengubah Fiscal Year Start ke July lewat D-01

1. Ubah Select Fiscal Year Start dari "January" menjadi "July"
2. Klik [Save changes]
3. Verifikasi body dialog memuat daftar bullet: "16 accounting periods will be rebuilt."; "Tax year start also follows Fiscal Year Start."
4. Klik [Save] pada dialog D-01
5. Verifikasi dialog D-01 tertutup
6. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
7. Verifikasi tidak ada dialog konfirmasi tambahan setelah klik [Save]
8. Verifikasi Select Fiscal Year Start menampilkan "July"
9. Verifikasi form tetap terbuka dengan nilai tersimpan
10. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
11. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-208: Save mengubah First Accounting Period ke Jan 2026 lewat D-01

12. Ubah Select bulan First Accounting Period dari "March" menjadi "January"
13. Klik [Save changes]
14. Verifikasi body dialog memuat daftar bullet: "12 accounting periods will be rebuilt."
15. Verifikasi dialog D-01 tidak memuat bullet "Tax year start also follows Fiscal Year Start."
16. Klik [Save] pada dialog D-01
17. Verifikasi dialog D-01 tertutup
18. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
19. Verifikasi Select bulan First Accounting Period menampilkan "January"
20. Verifikasi Select tahun First Accounting Period menampilkan "2026"
21. Verifikasi form tetap terbuka dengan nilai tersimpan
22. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
23. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-209: Save mengubah Depreciation in Disposal Month lewat D-01

24. Seed 2 pelepasan menunggu posting (PB-6b) lewat API
25. Ubah Select Depreciation in Disposal Month dari "Up to previous month" menjadi "Including disposal month"
26. Klik [Save changes]
27. Verifikasi body dialog memuat daftar bullet: "2 disposals waiting posting are affected."
28. Klik [Save] pada dialog D-01
29. Verifikasi dialog D-01 tertutup
30. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
31. Verifikasi Select Depreciation in Disposal Month menampilkan "Including disposal month"
32. Verifikasi form tetap terbuka dengan nilai tersimpan
33. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
34. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

## Notes

- Langkah penghubung (S-03): pemulihan Preferences lewat seed API dan muat ulang di akhir tiap TC, seed pelepasan.
- Urutan Verifikasi: toast sukses lebih dulu sebagai anchor sebelum asersi absence dialog konfirmasi tambahan (bagian 8b butir 2).
- Temuan untuk QA:
  - Post Condition "Entri log L-02 untuk setting yang berubah ditulis (diuji pada Section 5)" tidak punya langkah observasi di TC ini, sehingga tidak diasersi; pencatatan log diuji pada TC Section 5.
  - TC-207 dan TC-208 Post Condition (periode akuntansi dibangun ulang; diuji pada Section 7) dan TC-209 Post Condition b (pelepasan yang diposting memakai nilai baru) tidak punya langkah observasi di TC ini; tidak diasersi.
  - TC-207 Precondition d menyebut versi pertama Tax Depreciation Class tidak bertanggal (PB-1) sebagai kondisi; tidak ada langkah observasinya.

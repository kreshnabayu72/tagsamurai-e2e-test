---
id: TC-AC-LA-E2E-100-filter-list-eksekusi-tanggal-dan-logika
title: "Filter List: Tanggal Last Updated dan Logika OR AND"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-296
  - TC-AC-LA-297
coverage:
  web: automated
---

# Filter List: Tanggal Last Updated dan Logika OR AND

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status; License Type `Concurrent User` dan `Storage`; Client `PT Sejahtera`; nilai Last Updated pada sedikitnya dua hari berbeda) bersifat baca-saja untuk spec ini. Rentang tanggal TC-AC-LA-296 diambil dari nilai Last Updated dua baris seed pada hari berbeda; satu hari diambil dari nilai Last Updated salah satu baris seed. Kombinasi `Concurrent User` atau `Storage` dengan Client `PT Sejahtera` diasumsikan memiliki sedikitnya satu baris pada seed.
- Kemampuan teknis: Date Format General Settings terbaca oleh langkah verifikasi format tanggal; nilainya mengikuti pengaturan akun uji (bukan diubah spec ini).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-296: Filter tanggal Last Updated

1. Klik ikon Filter
2. Verifikasi placeholder `Select date` pada field Last Updated
3. Pilih rentang tanggal pada Last Updated dari tanggal dua baris seed pada hari berbeda
4. Verifikasi teks tanggal pada input mengikuti Date Format General Settings
5. Klik `[Apply]`
6. Verifikasi sedikitnya satu baris tampil
7. Verifikasi hasil memuat baris dengan Last Updated dalam rentang inklusif
8. Klik ikon Filter
9. Pilih satu hari pada Last Updated (Start sama dengan End)
10. Klik `[Apply]`
11. Verifikasi hasil memuat baris pada hari itu
12. Klik ikon Filter
13. Klik `[Clear Field]` lalu `[Apply]`

### TC-AC-LA-297: Logika OR dalam satu field dan AND antar field

14. Klik ikon Filter
15. Buka dropdown License Type
16. Centang `Concurrent User` dan `Storage`
17. Klik `[Apply]`
18. Verifikasi sedikitnya satu baris tampil
19. Verifikasi baris dengan salah satu nilai License Type (`Concurrent User` atau `Storage`) tampil
20. Klik ikon Filter
21. Buka dropdown Client
22. Centang `PT Sejahtera`
23. Klik `[Apply]`
24. Verifikasi sedikitnya satu baris tampil
25. Verifikasi hanya baris yang memenuhi kedua field (License Type `Concurrent User` atau `Storage`, dan Client `PT Sejahtera`) tampil
26. Klik ikon Filter
27. Klik `[Clear Field]` lalu `[Apply]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-LA-292 ada di spec 120.
- Langkah penghubung (S-03): langkah 12, 13, 26, 27 (membersihkan filter), langkah 20 (membuka panel lagi).
- Temuan untuk QA:
  - TC-AC-LA-296 tidak menyebut tanggal konkret untuk rentang dan satu hari; spec memakai tanggal Last Updated baris seed #54 yang dibaca saat uji.
  - TC-AC-LA-296 Expected c tidak menyebut nilai Date Format General Settings akun uji; spec mengasersi bahwa input mengikuti format yang berlaku tanpa menyebut nilainya.
  - TC-AC-LA-297 tidak menyebut kombinasi License Type dan Client yang dijamin ada di seed; spec mengasumsikan sedikitnya satu baris `PT Sejahtera` dengan `Concurrent User` atau `Storage`.

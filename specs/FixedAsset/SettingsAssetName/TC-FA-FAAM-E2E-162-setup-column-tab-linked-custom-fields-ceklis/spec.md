---
id: TC-FA-FAAM-E2E-162-setup-column-tab-linked-custom-fields-ceklis
title: "Setup Column Tab Linked Custom Fields: Kolom Actions dan Ceklis"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-556
  - TC-FA-FAAM-557
coverage:
  web: automated
---

# Setup Column Tab Linked Custom Fields: Kolom Actions dan Ceklis

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`): `Dell Latitude` (Pre-setup #10) dengan custom field berscope (Pre-setup #27): `Cost Center`, `Operating System`, dan `Warranty Notes`, sehingga label tab `Linked Custom Fields (3)`. Konfigurasi kolom bawaan tabel Linked Custom Fields: `Field Name | Data Type | Global Value`. Spec ini hanya membuka Popup Detail dan tidak mengubah data (S-06).
- Kemampuan teknis: hapus preferensi kolom tabel Linked Custom Fields di browser (disediakan tim FE).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: konfigurasi kolom tabel Linked Custom Fields (preferensi di browser) diubah spec ini. Pemulihan: langkah 24 menghapus preferensi kolom di browser, dan hook `after` melakukannya sebagai cadangan (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik nama `Dell Latitude`
3. Klik tab `Linked Custom Fields (3)`

### TC-FA-FAAM-556: Kolom Actions dan overlay Column Visibility Tab Linked Custom Fields

4. Verifikasi kolom Actions (⋯) tersedia pada tabel Linked Custom Fields
5. Klik header kolom Actions (⋯)
6. Verifikasi overlay memuat kolom `Field Name`, `Data Type`, dan `Global Value` dengan `Setup Column...`

### TC-FA-FAAM-557: Setup Column Tab Linked Custom Fields ceklis dan unceklis kolom Field Name, Data Type, Global Value

7. Klik `Setup Column...`
8. Uncheck `Field Name` dan `Data Type`
9. Verifikasi Live Preview hanya memuat kolom `Global Value`
10. Verifikasi checkbox `Global Value` disabled (guard satu kolom tersisa)
11. Check `Field Name`, lalu uncheck `Global Value`
12. Verifikasi Live Preview hanya memuat kolom `Field Name`
13. Verifikasi checkbox `Field Name` disabled (guard satu kolom tersisa)
14. Check `Data Type`, lalu uncheck `Field Name`
15. Verifikasi Live Preview hanya memuat kolom `Data Type`
16. Verifikasi checkbox `Data Type` disabled (guard satu kolom tersisa)
17. Check `Field Name` dan `Global Value`
18. Verifikasi Live Preview memuat kolom `Field Name | Data Type | Global Value`
19. Uncheck `Global Value`
20. Klik `[Save]`
21. Verifikasi tabel Linked Custom Fields hanya memuat kolom `Field Name | Data Type`
22. Tekan F5, klik nama `Dell Latitude`, lalu klik tab `Linked Custom Fields (3)`
23. Verifikasi konfigurasi tersimpan: tabel Linked Custom Fields hanya memuat kolom `Field Name | Data Type`
24. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, tekan F5

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (langkah 1, R-16), menyimpan perubahan sebelum asersi tabel (langkah 20), membuka kembali Popup Detail sesudah F5 (langkah 22), dan memulihkan konfigurasi kolom (langkah 24, S-09).
- Pada langkah 8 sampai 16 tiap kolom (`Global Value`, `Field Name`, `Data Type`) bergiliran menjadi kolom tersisa terakhir sehingga guard satu kolom tersisa diuji pada ketiga kolom. Live Preview yang menyebut "hanya memuat" kolom tertentu juga membuktikan kolom lain tidak tampil (bagian 8b butir 2).
- Geser dan pin tab ini ada di spec 163.
- Temuan untuk QA:
  - TC-FA-FAAM-556 dan 557 memuat ACC `#14; #10`, tetapi langkahnya hanya memakai `Dell Latitude` (#10); `Service Vehicle` (#14) tidak dipakai.
  - TC-FA-FAAM-557 Expected "tersimpan" tidak menyebut caranya diamati; spec memakai F5 lalu membuka kembali Popup Detail.

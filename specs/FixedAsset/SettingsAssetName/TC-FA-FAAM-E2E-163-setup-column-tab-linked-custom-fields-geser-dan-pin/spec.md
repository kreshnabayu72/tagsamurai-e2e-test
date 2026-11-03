---
id: TC-FA-FAAM-E2E-163-setup-column-tab-linked-custom-fields-geser-dan-pin
title: "Setup Column Tab Linked Custom Fields: Geser dan Pin"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-558
  - TC-FA-FAAM-559
coverage:
  web: automated
---

# Setup Column Tab Linked Custom Fields: Geser dan Pin

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`): `Dell Latitude` (Pre-setup #10) dengan custom field berscope (Pre-setup #27): `Cost Center`, `Operating System`, dan `Warranty Notes`, sehingga label tab `Linked Custom Fields (3)`. Konfigurasi kolom bawaan tabel Linked Custom Fields: `Field Name | Data Type | Global Value`. Spec ini hanya membuka Popup Detail dan tidak mengubah data (S-06).
- Kemampuan teknis: drag and drop pada popup Setup Column dan hapus preferensi kolom tabel Linked Custom Fields di browser (disediakan tim FE).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: konfigurasi kolom tabel Linked Custom Fields (preferensi di browser) diubah spec ini. Pemulihan: langkah 14 dan 27 menghapus preferensi kolom di browser, dan hook `after` melakukannya sebagai cadangan (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik nama `Dell Latitude`
3. Klik tab `Linked Custom Fields (3)`

### TC-FA-FAAM-558: Setup Column Tab Linked Custom Fields geser urutan kolom Field Name, Data Type, Global Value

4. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
5. Geser kolom `Global Value` ke posisi pertama, lalu `Data Type` ke posisi kedua, sehingga urutan kolom terbalik
6. Verifikasi Live Preview berurutan `Global Value | Data Type | Field Name`
7. Uncheck `Data Type` dan `Global Value`
8. Verifikasi checkbox `Field Name` disabled (guard satu kolom tersisa)
9. Check `Data Type` dan `Global Value`
10. Klik `[Save]`
11. Verifikasi tabel Linked Custom Fields berurutan `Global Value | Data Type | Field Name`
12. Tekan F5, klik nama `Dell Latitude`, lalu klik tab `Linked Custom Fields (3)`
13. Verifikasi konfigurasi tersimpan: tabel Linked Custom Fields berurutan `Global Value | Data Type | Field Name`
14. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, tekan F5, klik nama `Dell Latitude`, lalu klik tab `Linked Custom Fields (3)`

### TC-FA-FAAM-559: Setup Column Tab Linked Custom Fields pin dan unpin kolom Field Name, Data Type, Global Value

15. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
16. Pin kolom `Field Name`, `Data Type`, dan `Global Value`
17. Verifikasi Live Preview menampilkan kolom `Field Name`, `Data Type`, dan `Global Value` ter-pin
18. Uncheck `Data Type` dan `Global Value`
19. Verifikasi checkbox `Field Name` disabled (guard satu kolom tersisa)
20. Check `Data Type` dan `Global Value`
21. Unpin kolom `Data Type` dan `Global Value`
22. Verifikasi Live Preview menampilkan kolom `Field Name` ter-pin dan kolom `Data Type` serta `Global Value` tanpa pin
23. Klik `[Save]`
24. Verifikasi tabel Linked Custom Fields menampilkan kolom `Field Name` ter-pin dan kolom `Data Type` serta `Global Value` tanpa pin
25. Tekan F5, klik nama `Dell Latitude`, lalu klik tab `Linked Custom Fields (3)`
26. Verifikasi konfigurasi tersimpan: tabel Linked Custom Fields menampilkan kolom `Field Name` ter-pin dan kolom `Data Type` serta `Global Value` tanpa pin
27. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, tekan F5

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (langkah 1, R-16), menyimpan perubahan sebelum asersi tabel (langkah 10 dan 23), membuka kembali Popup Detail dan tab sesudah F5 (langkah 12 dan 25), dan memulihkan konfigurasi kolom (langkah 14 dan 27, S-09).
- Pada langkah 5 urutan terbalik diperoleh dengan memindahkan `Global Value` ke posisi pertama dan `Data Type` ke posisi kedua sehingga ketiga kolom berpindah posisi.
- Pada TC-FA-FAAM-558 dan 559, Expected "Guard satu kolom tersisa berlaku" dijalankan sekali pada kolom `Field Name` sebagai satu-satunya kolom tersisa (langkah 8 dan 19); guard untuk ketiga kolom sudah dijalankan pada spec 162.
- Temuan untuk QA:
  - TC-FA-FAAM-558 dan 559 Expected ii ("Guard satu kolom tersisa berlaku") tidak relevan untuk geser dan pin, dan tampak disalin dari TC-FA-FAAM-557; spec mengasersi guard sekali per TC.
  - TC-FA-FAAM-558 dan 559 memuat ACC `#14; #10`, tetapi langkahnya hanya memakai `Dell Latitude` (#10); `Service Vehicle` (#14) tidak dipakai.
  - Expected "tersimpan" tidak menyebut caranya diamati; spec memakai F5 lalu membuka kembali Popup Detail.

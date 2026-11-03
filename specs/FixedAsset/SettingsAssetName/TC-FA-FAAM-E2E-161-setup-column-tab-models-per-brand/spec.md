---
id: TC-FA-FAAM-E2E-161-setup-column-tab-models-per-brand
title: "Setup Column Tab Models per Brand: Kolom Actions, Ceklis, Geser, dan Pin"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-552
  - TC-FA-FAAM-553
  - TC-FA-FAAM-554
  - TC-FA-FAAM-555
coverage:
  web: automated
---

# Setup Column Tab Models per Brand: Kolom Actions, Ceklis, Geser, dan Pin

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.catalog`): `Service Vehicle` (Pre-setup #14: Brand `Isuzu` model `D-Max`, Brand `Toyota` model `Hilux`). Konfigurasi kolom bawaan tabel Models per Brand: `Brand | Model/Type`. Spec ini hanya membuka Popup Detail dan tidak mengubah data Asset Name (S-06).
- Kemampuan teknis: drag and drop pada popup Setup Column dan hapus preferensi kolom tabel Models per Brand di browser (disediakan tim FE).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: konfigurasi kolom tabel Models per Brand (preferensi di browser) diubah spec ini. Pemulihan: langkah 17, 28, dan 41 menghapus preferensi kolom di browser, dan hook `after` melakukannya sebagai cadangan (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Service Vehicle`, tekan Enter
2. Klik nama `Service Vehicle`

### TC-FA-FAAM-552: Kolom Actions dan overlay Column Visibility Tab Models per Brand

3. Verifikasi kolom Actions (⋯) tampil pada tabel Models per Brand tanpa row action
4. Klik header kolom Actions (⋯) di tabel Models per Brand
5. Verifikasi overlay memuat kolom `Brand` dan `Model/Type` dengan `Setup Column...`

### TC-FA-FAAM-553: Setup Column Tab Models per Brand ceklis dan unceklis kolom Brand dan Model/Type

6. Klik `Setup Column...`
7. Uncheck `Brand`
8. Verifikasi Live Preview hanya memuat kolom `Model/Type`
9. Verifikasi checkbox `Model/Type` disabled (guard satu kolom tersisa)
10. Check `Brand`, lalu uncheck `Model/Type`
11. Verifikasi Live Preview hanya memuat kolom `Brand`
12. Verifikasi checkbox `Brand` disabled (guard satu kolom tersisa)
13. Klik `[Save]`
14. Verifikasi tabel Models per Brand hanya memuat kolom `Brand`
15. Tekan F5, lalu klik nama `Service Vehicle`
16. Verifikasi konfigurasi tersimpan: tabel Models per Brand hanya memuat kolom `Brand`
17. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, tekan F5, lalu klik nama `Service Vehicle`

### TC-FA-FAAM-554: Setup Column Tab Models per Brand geser urutan kolom Brand dan Model/Type

18. Klik header kolom Actions (⋯) di tabel Models per Brand, lalu klik `Setup Column...`
19. Geser kolom `Model/Type` ke posisi sebelum `Brand`
20. Verifikasi Live Preview berurutan `Model/Type | Brand`
21. Uncheck `Brand`
22. Verifikasi checkbox `Model/Type` disabled (guard satu kolom tersisa)
23. Check `Brand`
24. Klik `[Save]`
25. Verifikasi tabel Models per Brand berurutan `Model/Type | Brand`
26. Tekan F5, lalu klik nama `Service Vehicle`
27. Verifikasi konfigurasi tersimpan: tabel Models per Brand berurutan `Model/Type | Brand`
28. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, tekan F5, lalu klik nama `Service Vehicle`

### TC-FA-FAAM-555: Setup Column Tab Models per Brand pin dan unpin kolom Brand dan Model/Type

29. Klik header kolom Actions (⋯) di tabel Models per Brand, lalu klik `Setup Column...`
30. Pin kolom `Brand` dan `Model/Type`
31. Verifikasi Live Preview menampilkan kolom `Brand` dan `Model/Type` ter-pin
32. Uncheck `Model/Type`
33. Verifikasi checkbox `Brand` disabled (guard satu kolom tersisa)
34. Check `Model/Type`
35. Unpin kolom `Model/Type`
36. Verifikasi Live Preview menampilkan kolom `Brand` ter-pin dan kolom `Model/Type` tanpa pin
37. Klik `[Save]`
38. Verifikasi tabel Models per Brand menampilkan kolom `Brand` ter-pin dan kolom `Model/Type` tanpa pin
39. Tekan F5, lalu klik nama `Service Vehicle`
40. Verifikasi konfigurasi tersimpan: tabel Models per Brand menampilkan kolom `Brand` ter-pin dan kolom `Model/Type` tanpa pin
41. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, tekan F5

## Notes

- Spec ini melewati sekitar 35 langkah (41). Alasan: seluruh blok satu kelas harness (Setup Column tab Models per Brand), satu akun, satu dataset (`Service Vehicle`), dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (langkah 1, R-16), membuka kembali Popup Detail sesudah F5 (langkah 15, 26, 39), menyimpan perubahan sebelum asersi tabel (langkah 13, 24, 37), dan memulihkan konfigurasi kolom ke bawaan sebelum TC berikutnya (langkah 17, 28, 41; S-09).
- Pada TC-FA-FAAM-553 uncheck `Brand` dan `Model/Type` bergantian supaya tiap kolom menjadi kolom tersisa terakhir (guard); Live Preview yang menyebut "hanya memuat" kolom tertentu juga membuktikan kolom lain tidak tampil (bagian 8b butir 2).
- Pada TC-FA-FAAM-554 dan 555, Expected "Guard satu kolom tersisa berlaku" dijalankan sekali pada satu kolom tersisa (langkah 22 dan 33); guard untuk kedua kolom sudah dijalankan pada TC-FA-FAAM-553.
- Setup Column tab Linked Custom Fields ada di spec 162 dan 163.
- Temuan untuk QA:
  - TC-FA-FAAM-554 dan 555 Expected ii ("Guard satu kolom tersisa berlaku") tidak relevan untuk geser dan pin, dan tampak disalin dari TC-FA-FAAM-553; spec mengasersi guard sekali per TC.
  - TC-FA-FAAM-552 sampai 555 memuat ACC `#14; #10`, tetapi langkahnya hanya memakai `Service Vehicle` (#14); `Dell Latitude` (#10) tidak dipakai.
  - Expected "tersimpan" tidak menyebut caranya diamati; spec memakai F5 lalu membuka kembali Popup Detail.

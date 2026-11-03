---
id: TC-FA-FAAM-E2E-158-tab-models-per-brand-screening-sort-no-model-dan-hover
title: "Tab Models per Brand: Screening, Sort Brand dan Model/Type, No Model, dan Hover Badge"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-542
  - TC-FA-FAAM-543
  - TC-FA-FAAM-544
  - TC-FA-FAAM-545
  - TC-FA-FAAM-668
coverage:
  web: automated
---

# Tab Models per Brand: Screening, Sort Brand dan Model/Type, No Model, dan Hover Badge

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.catalog`): `Service Vehicle` (Pre-setup #14: Brand `Isuzu` model `D-Max`, Brand `Toyota` model `Hilux`), `Multi Brand Item` (Pre-setup #14m: lebih dari 2 Brand dan model beragam), Asset Name dengan Brand `Dell` tanpa model ketikan (Pre-setup #14k, `Fixture.faAssetName.noModelItem`; nama tidak tertulis di TC, lihat Temuan untuk QA), dan `Long Badge Item` (Pre-setup #26d, Total Asset 1: Brand `Long Brand Name Twenty-Six`, model `Long Model Name Twenty Six`). Spec ini hanya membuka Popup Detail dan tidak mengubah data (S-06).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: tidak ada yang diubah. Spec ini tidak menyimpan konfigurasi kolom. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Service Vehicle`, tekan Enter
2. Klik nama `Service Vehicle`

### TC-FA-FAAM-542: Screening Tab Models per Brand: tanpa toolbar dan tanpa paginasi

3. Verifikasi tab `Models per Brand (2)` tampil dengan tabel `Brand | Model/Type`
4. Verifikasi baris `Isuzu` model `D-Max` dan baris `Toyota` model `Hilux`
5. Verifikasi tabel Models per Brand tanpa toolbar dan tanpa paginasi
6. Verifikasi default sort Brand A-Z

### TC-FA-FAAM-543: Sort kolom Brand Tab Models per Brand

7. Klik header Brand
8. Verifikasi Klik 1: A-Z (default)
9. Klik header Brand
10. Verifikasi Klik 2: Z-A
11. Klik header Brand
12. Verifikasi Klik 3: netral kembali default Brand A-Z

### TC-FA-FAAM-544: Sort kolom Model/Type: menurut model pertama dalam sel, badge di sel tetap A-Z

13. Tutup Popup Detail, lalu ganti isi kotak search dengan `Multi Brand Item`, tekan Enter
14. Klik nama `Multi Brand Item`
15. Di tab Models per Brand klik header Model/Type
16. Verifikasi baris diurut menurut model pertama dalam sel (tiebreaker Brand A-Z)
17. Verifikasi badge di dalam sel tetap A-Z
18. Klik header Model/Type
19. Verifikasi arah descending membalik urutan baris
20. Verifikasi badge di dalam sel tetap A-Z pada arah descending

### TC-FA-FAAM-545: Brand tanpa model nyata menampilkan badge No Model

21. Tutup Popup Detail, lalu ganti isi kotak search dengan nama Asset Name Pre-setup #14k (`Fixture.faAssetName.noModelItem`), tekan Enter
22. Klik nama Asset Name tersebut
23. Verifikasi baris `Dell` menampilkan badge `No Model`

### TC-FA-FAAM-668: Hover Brand dan Model/Type di Tab Models per Brand menampilkan nama penuh badge

24. Tutup Popup Detail, lalu ganti isi kotak search dengan `Long Badge Item`, tekan Enter
25. Klik nama `Long Badge Item`
26. Verifikasi badge Brand tampil `Long Brand N..e Twenty-Six`
27. Verifikasi badge Model/Type tampil `Long Model N..e Twenty Six`
28. Arahkan kursor ke badge Brand
29. Verifikasi hover menampilkan nama penuh `Long Brand Name Twenty-Six`
30. Arahkan kursor ke badge Model/Type
31. Verifikasi hover menampilkan nama penuh `Long Model Name Twenty Six`

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (langkah 1, 13, 21, 24, R-16) dan menutup Popup Detail sebelum membuka Asset Name lain (langkah 13, 21, 24).
- Asersi `Verifikasi` tabel tanpa toolbar dan paginasi (langkah 5) beranchor tabel yang tampil dengan baris (langkah 3 dan 4).
- Temuan untuk QA:
  - TC-FA-FAAM-545 menyebut Asset Name ber-Brand `Dell` tanpa model tanpa nama (Pre-setup #14k); nama tidak tertulis, sehingga spec merujuk fixture.
  - TC-FA-FAAM-668 memuat ACC `#26` (42 aset `Dell Latitude`), sedangkan Precondition menyebut `#26d`; spec mengikuti Precondition.
  - TC-FA-FAAM-542 sampai 545 memuat ACC `#14`; TC-FA-FAAM-544 memakai `Multi Brand Item` (`#14m`) dan TC-FA-FAAM-545 memakai `#14k`, yang tidak tercantum di ACC. TC-FA-FAAM-542 Precondition juga menyebut `Dell Latitude` (#10, #27) yang tidak dipakai langkahnya.

---
id: TC-GS-UOM-E2E-001-screening-tab-measurement-layout-tooltip-dan-sticky
title: "Screening Tab Measurement: Layout, Tab Default, Tooltip Table Tools, Sticky Kolom, Katalog Flat"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-2
  - TC-GS-UOM-1
  - TC-GS-UOM-249
  - TC-GS-UOM-4
  - TC-GS-UOM-15
coverage:
  web: automated
---

# Screening Tab Measurement: Layout, Tab Default, Tooltip Table Tools, Sticky Kolom, Katalog Flat

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data (hanya dibaca, spec tidak membuat atau mengubah data): Pre-setup Client A (8 unit: Box, Dozen, Gram, Kilogram, Liter, Meter, Pack, Pieces) dan Population D-01 (12 unit: Centimeter, Foot, Gallon, Inch, Milliliter, Millimeter, Ounce, Pound, Roll, Set, Sheet, Ton), total N = 20 unit (diturunkan dari seeding, bukan dibaca dari tabel yang hanya menampilkan satu halaman). Hook `before` men-seed Population secara idempotent lewat API sesuai pernyataan "Data bersama" di `suite.md` (nama yang sudah ada dilewati; sisa unit non-Population dibersihkan hook suite).
- Guided Tooltip: flag Measurement (`guided_tooltip_seen_gs-measurement`) mengikuti pernyataan hook suite di `suite.md`. Flag `guided_tooltip_seen_gs-brand` (tab default Brand) juga mengikuti hook suite.
- Layar awal: sesi baru tanpa membuka Master Reference. Spec ini dikecualikan dari pembukaan layar oleh hook `beforeEach` suite (lihat `suite.md`, bagian Hook suite); langkah 1 membuka Global Settings > Master Reference dari sidebar karena masuk Master Reference dari sidebar adalah objek uji (TC-GS-UOM-2).
- Kemampuan teknis: hover ikon; mengubah lebar viewport menjadi 1024px (TC-GS-UOM-15) dan scroll horizontal pada tabel; viewport dipulihkan di langkah 38, hook `after` sebagai cadangan.
- State global yang diubah: hanya flag Guided Tooltip dan viewport (dipulihkan seperti di atas). Tidak ada perubahan plan, status Client, atau format tanggal.

## Test Steps

### TC-GS-UOM-2: Tab aktif default saat pertama masuk Master Reference adalah Brand

1. Buka Global Settings > Master Reference dari sidebar
2. Perhatikan Tab yang aktif dan Breadcrumb
3. Verifikasi Tab `Brand` aktif dan Tab `Measurement` tidak aktif
4. Verifikasi Breadcrumb `Master Reference > Brand`
5. Klik Tab Measurement
6. Verifikasi Breadcrumb berubah menjadi `Master Reference > Measurement`

### TC-GS-UOM-1: Screening tab Measurement oleh Total Control

7. Perhatikan tab Measurement dari atas ke bawah tanpa mengisi atau mengklik apa pun
8. Verifikasi Header: Breadcrumb `Master Reference > Measurement` dengan trigger Guided Tooltip `[?]`
9. Verifikasi Header: Tab `Brand | Measurement (aktif)`
10. Verifikasi Header: Table Tools (rata kanan) `Search | Filter | Download | Changelog | [+ Unit]`
11. Verifikasi `[+ Unit]` variant filled, severity primary, icon AddLine
12. Verifikasi Body: header kolom `Checkbox | Unit Name (sortable, text link) | Symbol (sortable) | Used By (Items) (sortable, number link) | Last Updated (sortable) | Actions (⋯)`
13. Verifikasi Body: 10 baris pertama dari 20 unit (8 Pre-setup dan 12 Population) tampil di halaman 1
14. Verifikasi Body: Unit Name, Symbol, Used By (Items), dan Last Updated terisi pada 10 baris itu (tidak ada sel kosong)
15. Verifikasi Body: Used By (Items) bernilai `0` tampil `0`, bukan `—`
16. Verifikasi Footer: Pagination default 10 data per halaman dengan 2 halaman
17. Verifikasi Filter Panel tidak tampil (collapsed) sebelum tombol Filter diklik

### TC-GS-UOM-249: Katalog flat tanpa hierarki

18. Verifikasi sedikitnya satu baris unit tampil pada tabel
19. Verifikasi tidak ada baris bertingkat atau expand child pada tabel

### TC-GS-UOM-4: Hover icon Table Tools menampilkan tooltip

20. Hover icon Search
21. Verifikasi tooltip `Search`
22. Hover icon Filter
23. Verifikasi tooltip `Filter`
24. Hover icon Download
25. Verifikasi tooltip `Download`
26. Hover icon Changelog
27. Verifikasi tooltip `Changelog`
28. Hover header kolom Actions (⋯)
29. Verifikasi tooltip `Column Visibility` pada header kolom Actions (⋯)

### TC-GS-UOM-15: Kolom Checkbox sticky kiri dan Actions sticky kanan saat tabel di-scroll horizontal

30. Ubah lebar viewport menjadi 1024px
31. Muat ulang halaman Global Settings > Master Reference lalu klik Tab Measurement
32. Scroll tabel horizontal ke kanan
33. Verifikasi kolom Checkbox tetap terlihat di kiri
34. Verifikasi kolom Actions (⋯) tetap terlihat di kanan
35. Scroll tabel horizontal ke kiri
36. Verifikasi kolom Checkbox tetap terlihat di kiri
37. Verifikasi kolom Actions (⋯) tetap terlihat di kanan
38. Kembalikan lebar viewport ke ukuran awal

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-UOM-2 (masuk Master Reference, tab default) paling awal karena TC-GS-UOM-1 memulai dari pembukaan yang sama; langkah 1 dan 5 menjadi langkah 1 dan 2 TC-GS-UOM-1 (buka Master Reference, klik Tab Measurement). TC-GS-UOM-15 (ubah viewport) paling akhir karena mengubah state browser.
- Spec ini sekitar 38 langkah, sedikit di atas batas 35 langkah: seluruh blok satu kelas harness (baca UI, tanpa membuat data), satu akun, satu layar, dan tiap blok berdiri sendiri (kegagalan satu blok tidak mengubah makna blok lain).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 31 (muat ulang pada lebar 1024px agar tab Measurement dibuka pada viewport itu) dan 38 (pulihkan viewport; hook `after` sebagai cadangan).
- Verifikasi tambahan di luar Expected TC: langkah 18 (baris pembanding sebagai anchor positif bagi asersi absence langkah 19, bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-UOM-15: scroll horizontal hanya bermakna bila tabel melebar melebihi 1024px; TC tidak menyebut kolom atau konten yang membuat tabel overflow pada lebar itu. Spec tetap mengikuti TC.
  - TC-GS-UOM-1 mensyaratkan total tepat 20 unit; asumsi ini bergantung pada pembersihan unit sisa spec lain oleh hook suite (lihat `suite.md`, Data bersama).

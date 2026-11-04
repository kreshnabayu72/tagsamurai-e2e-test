---
id: TC-FA-TDC-E2E-248-filter-baris-bernilai-kosong-dan-independen-dari-visibilitas-kolom
title: "Filter: Baris Bernilai Kosong dan Independen dari Visibilitas Kolom"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-526
  - TC-FA-TDC-527
coverage:
  web: automated
---

# Filter: Baris Bernilai Kosong dan Independen dari Visibilitas Kolom

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; tabel muat pada satu halaman. LAND bernilai `—` pada Useful Life dan Allowed Methods, Asset Type `Land`; 8 class lain bernilai terisi pada keduanya.
- Data uji (literal TC): Useful Life Min `1`; Allowed Methods `Straight Line`; Asset Type `Land`.
- Data Dinamis: tidak ada.
- Kemampuan teknis: seeding sembilan class Example Data lewat API (`suite.md`); Overlay Column Visibility; pemulihan Setup Column dengan langkah eksplisit (8b.14, R-24).
- State global yang diubah: Filter pada tabel dan konfigurasi kolom (Asset Type disembunyikan lalu ditampilkan kembali oleh langkah di spec). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### Filter menyaring keluar baris bernilai kosong (TC-FA-TDC-526)

1. Klik icon Filter
2. Isi Useful Life Min `1`
3. Klik `[Apply]`
4. Verifikasi 8 class lain tampil
5. Verifikasi LAND (Useful Life `—`) tidak tampil
6. Klik `[Clear Field]`
7. Pilih Allowed Methods `Straight Line`
8. Klik `[Apply]`
9. Verifikasi 8 class lain tampil
10. Verifikasi LAND (Allowed Methods `—`) tidak tampil

### Filter independen dari visibilitas kolom (TC-FA-TDC-527)

11. Klik `[Clear Field]`
12. Pilih Asset Type `Land`
13. Klik `[Apply]`
14. Klik header Actions `⋯`
15. Hapus centang kolom Asset Type
16. Tutup Overlay Column Visibility
17. Verifikasi tabel tetap menampilkan hanya baris LAND setelah kolom disembunyikan
18. Klik icon Filter untuk membuka kembali Filter Panel
19. Verifikasi field Asset Type tetap tersedia di Filter Panel dengan nilai `Land`
20. Klik `[Clear Field]`
21. Klik `[Apply]`
22. Klik header Actions `⋯`
23. Centang kolom Asset Type
24. Tutup Overlay Column Visibility

## Notes

- Langkah penghubung (S-03, S-09): langkah 6 dan 11 (membersihkan field Filter sebelum kriteria berikutnya), langkah 20 dan 21 (melepas Filter Land), langkah 22 sampai 24 (pemulihan Setup Column agar kolom Asset Type kembali tampil; 8b.14, R-24), langkah 16 dan 24 (menutup Overlay Column Visibility). Hook `after` hanya cadangan.
- Filter Panel dibuka pada langkah 1 dan tetap terbuka sesudah `[Apply]` (8b.9), sehingga langkah 6 dan 11 langsung memakai `[Clear Field]` tanpa klik icon Filter (klik icon itu menutup panel). Klik header Actions dan Overlay Column Visibility pada langkah 14 sampai 16 berada di luar panel dan menutupnya; karena itu langkah 18 membuka panel kembali lewat klik icon Filter.
- Asersi tidak tampil langkah 5 dan 10 didahului `Verifikasi` positif pada tabel yang sama: langkah 4 dan 9 (8 class lain tampil) membuktikan tabel sudah dimuat (8b.2).
- Temuan untuk QA:
  - TC-FA-TDC-526 Expected "8 class lain tampil" tidak menyebut kode class; spec mengasersi jumlah delapan baris selain LAND.
  - TC-FA-TDC-527 langkah 2 tidak menyebut `[Save]` pada Overlay Column Visibility; spec mengikuti TC (perubahan langsung).
  - Email akun Total Control tidak tertulis di TC.

---
id: TC-GS-UOM-E2E-037-filter-panel-screening-last-updated-dan-clear
title: "Filter Panel: Screening, Placeholder, Last Updated, Clear Field, dan Tutup Tanpa Apply"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-133
  - TC-GS-UOM-134
  - TC-GS-UOM-140
  - TC-GS-UOM-141
  - TC-GS-UOM-293
  - TC-GS-UOM-378
coverage:
  web: automated
---

# Filter Panel: Screening, Placeholder, Last Updated, Clear Field, dan Tutup Tanpa Apply

## Prerequisites

- Mode: FE+BE. Suite berjalan serial (`parallel: false`, lihat `suite.md`). Spec tidak mengubah data unit.
- Flag Guided Tooltip halaman Measurement mengikuti pernyataan hook suite di `suite.md`.
- Akun: Total Control Client A, Sari Dewi (Sari D), `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Measurement dilakukan sekali di hook `before` suite.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (hanya dibaca; Last Updated lebih lama dari hari uji): Box / box (Used By 4), Dozen / dz (2), Gram / g (1), Kilogram / kg (1), Liter / L (0), Meter / m (0), Pack / pk (0), Pieces / pc (3).
- Data Dinamis: Population D-01 (12 unit, nama literal, Used By 0): Centimeter / cm, Millimeter / mm, Inch / in, Foot / ft, Milliliter / mL, Gallon / gal, Ounce / oz, Pound / lb, Ton / t, Roll / roll, Set / set, Sheet / sht. Di-seed lewat API di hook `before` (setara TC-GS-UOM-36), idempotent (dilewati bila sudah ada); total tabel N = 20 unit (8 Pre-setup + 12 Population), diturunkan dari seeding. Last Updated Population = hari uji: unit Population yang tercatat dibuat sebelum hari uji dihapus dan dibuat ulang lewat API di hook `before` supaya filter "hari ini" (TC-GS-UOM-140) bermakna. Nama literal disengaja (asersi hasil bergantung pada nama; pengecualian S-12); cleanup hanya menghapus unit yang dibuat spec ini.
- Tanggal "hari ini" mengikuti jam server dan jam browser yang sinkron (penguji dan server pada zona waktu yang sama).
- State global yang dipulihkan: Filter dikosongkan di hook `after`.
- Hook `beforeEach`: buka Global Settings > Master Reference > Measurement.
- Kemampuan teknis: pengisian date range picker Last Updated; klien HTTP/API untuk seeding Population (disediakan tim FE).
- Fixture: `fixtures/measurement.json` belum ada; tim FE menyiapkannya (lihat `suite.md`, bagian Data bersama).

## Test Steps

### TC-GS-UOM-133: Screening Filter Panel tabel Measurement

1. Klik Filter
2. Verifikasi panel Filter tampil dengan dua field: `Used By (Items)` (range `Min`–`Max`) dan `Last Updated` (date range picker)
3. Verifikasi tombol `[Clear Field]` dan `[Apply]`
4. Verifikasi tidak ada field filter `Item Type`, `In Use`, maupun `Modified By` pada tabel utama
5. Verifikasi icon Filter berubah gelap selama panel terbuka

### TC-GS-UOM-378: Screening field filter Used By (Items) pada Filter Panel

6. Verifikasi field `Used By (Items)` bertipe range dengan dua input bersebelahan, placeholder `Min` dan `Max`
7. Verifikasi field `Last Updated` date range picker tetap ada
8. Verifikasi tombol `[Clear Field]` dan `[Apply]`
9. Verifikasi tidak ada filter `Item Type`, `In Use`, maupun `Modified By`

### TC-GS-UOM-134: Placeholder field Last Updated pada Filter Panel

10. Verifikasi placeholder field Last Updated: `Select date`

### TC-GS-UOM-140: Filter Last Updated menyaring baris dalam rentang tanggal

11. Isi Last Updated rentang hari uji – hari uji (hari ini – hari ini)
12. Klik [Apply]
13. Verifikasi halaman 1 menampilkan 10 unit Population: Centimeter, Foot, Gallon, Inch, Milliliter, Millimeter, Ounce, Pound, Roll, Set
14. Klik Next
15. Verifikasi halaman 2 hanya menampilkan Sheet dan Ton (tidak ada unit Pre-setup yang tampil)
16. Klik Previous

### TC-GS-UOM-141: Clear Field Filter Panel lalu Apply mengembalikan seluruh data

17. Isi Last Updated rentang 01 Jan 2020 – 01 Jan 2020
18. Klik [Apply]
19. Klik [Clear Field]
20. Verifikasi field `Used By (Items)` kosong
21. Verifikasi field `Last Updated` kosong
22. Klik [Apply]
23. Verifikasi seluruh baris kembali: halaman 1 menampilkan 10 baris dan pagination 2 halaman (20 unit)

### TC-GS-UOM-293: Menutup Filter Panel tanpa Apply membuang perubahan yang belum di-Apply

24. Isi Used By (Items) Min `1`
25. Klik [Apply]
26. Ubah Min menjadi `3` tanpa klik [Apply]
27. Klik icon Filter untuk menutup panel
28. Verifikasi tabel tetap menampilkan hasil filter Min `1` (lima baris): Box, Dozen, Gram, Kilogram, Pieces
29. Klik icon Filter untuk membuka panel kembali
30. Verifikasi field Min berisi `1` dan nilai `3` dibuang
31. Klik [Clear Field]
32. Klik [Apply]

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 133, 378, 134 (semua screening pada satu pembukaan panel), lalu 140, 141, 293 (urutan sumber 133, 134, 140, 141, 293, 378). TC-GS-UOM-378 dan TC-GS-UOM-134 tidak membuka panel ulang: langkah "Klik Filter" masing-masing sudah terpenuhi oleh pembukaan panel pada langkah 1.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 14 dan 16 (pindah ke halaman 2 untuk menuntaskan asersi "hanya unit yang dibuat hari ini" pada seluruh hasil, lalu kembali); langkah 31 dan 32 (mengosongkan filter di akhir spec, hook `after` sebagai cadangan).
- Langkah 11 sampai 32 mengikuti urutan langkah TC: panel tetap terbuka sesudah `[Apply]` (TC-GS-UOM-141 langkah 2 dan TC-GS-UOM-293 langkah 2 melanjutkan tanpa membuka ulang panel); panel hanya dibuka ulang pada langkah 29 setelah ditutup eksplisit.
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-UOM-140 mensyaratkan "Population dibuat hari ini" tanpa menyebut cara memastikannya bila Population sudah ada dari hari sebelumnya; spec menangani lewat hook `before` (hapus dan buat ulang bila dibuat sebelum hari uji).
  - TC-GS-UOM-293: Expected mencantumkan hasil filter Min `1` sebagai `Gram`, `Kilogram`, `Dozen`, `Pieces`, `Box`; spec mengasersi himpunan yang sama tanpa urutan (urutan tabel default Unit Name A-Z).
  - TC-GS-UOM-133 dan TC-GS-UOM-378 memiliki Expected yang sebagian identik (field filter, tombol, daftar filter yang tidak ada); keduanya dipertahankan sesuai TC.
  - TC tidak menyatakan eksplisit apakah panel Filter menutup setelah `[Apply]`; spec mengikuti urutan langkah TC (panel tetap terbuka).

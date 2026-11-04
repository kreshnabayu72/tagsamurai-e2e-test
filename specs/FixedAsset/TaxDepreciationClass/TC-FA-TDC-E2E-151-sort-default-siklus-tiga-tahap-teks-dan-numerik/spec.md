---
id: TC-FA-TDC-E2E-151-sort-default-siklus-tiga-tahap-teks-dan-numerik
title: "Sort: Urutan Default, Siklus Tiga Tahap, Kolom Teks, dan Kolom Numerik"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-14
  - TC-FA-TDC-528
  - TC-FA-TDC-529
  - TC-FA-TDC-530
  - TC-FA-TDC-531
coverage:
  web: automated
---

# Sort: Urutan Default, Siklus Tiga Tahap, Kolom Teks, dan Kolom Numerik

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; tabel muat pada satu halaman. Class Name: BLD-P `Bangunan permanen`, BLD-NP `Bangunan tidak permanen`, NB-1 `Bukan bangunan – Kelompok 1`, NB-2 `... Kelompok 2`, NB-4 `... Kelompok 4`, NB-OLD `Kelompok khusus lama`, NB-KHS `Kelompok khusus pernah diposting`, NB-SL `Kelompok khusus Straight Line`, LAND `Tanah`. Regulation Reference NB-SL `PMK 99/2099`, class lain `UU HPP 7/2021; PMK 72/2023`; Modified By NB-SL `Rina P`, class lain `System` (user penyunting disediakan tim FE). Kolom Regulation Reference dan Modified By Hidden (default) dan ditampilkan oleh langkah spec.
- Tabel parameter perulangan TC-FA-TDC-531 (sort numerik, dua klik per kolom), literal TC:

  | Kolom | Ascending | Descending |
  |---|---|---|
  | Useful Life (years) | NB-1 (4), NB-OLD (5), NB-2 (8), BLD-NP dan NB-KHS (10), NB-SL (16), BLD-P dan NB-4 (20), LAND (`—` di akhir) | LAND (`—` di awal), BLD-P, NB-4, NB-SL, BLD-NP, NB-KHS, NB-2, NB-OLD, NB-1 |
  | Straight Line Rate | berdasar nilai angka: BLD-P dan NB-4 (5%), NB-SL (6.25%), BLD-NP dan NB-KHS (10%), NB-2 (12.5%), NB-OLD (20%), NB-1 (25%), LAND (`—` di akhir) | LAND (`—` di awal), NB-1, NB-OLD, NB-2, BLD-NP, NB-KHS, NB-SL, BLD-P, NB-4 |
  | Declining Balance Rate | NB-4 (10%), NB-KHS (20%), NB-2 (25%), NB-1 (50%), lalu baris `—`: BLD-NP, BLD-P, LAND, NB-OLD, NB-SL | baris `—` di awal, lalu NB-1, NB-2, NB-KHS, NB-4 |
  | Used By | BLD-NP, LAND, NB-4, NB-KHS, NB-OLD (0), BLD-P (1), NB-2 (3), NB-SL (4), NB-1 (5) | NB-1, NB-SL, NB-2, BLD-P, lalu BLD-NP, LAND, NB-4, NB-KHS, NB-OLD |

- Data Dinamis: tidak ada.
- Kemampuan teknis: seeding sembilan class Example Data lewat API (`suite.md`); Overlay Column Visibility; membaca indikator sort pada header; pemulihan Setup Column dengan langkah eksplisit (8b.14, R-24).
- State global yang diubah: Sort pada tabel (kembali netral oleh `beforeEach` suite) dan konfigurasi kolom (Regulation Reference dan Modified By ditampilkan lalu disembunyikan kembali oleh langkah di spec). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### Urutan bawaan tabel: Class Code A-Z (TC-FA-TDC-14)

1. Verifikasi baris berurutan Class Code A-Z: BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL
2. Verifikasi tidak ada indikator sort aktif pada kolom selain default

### Siklus sort 3 tahap pada kolom Class Code (TC-FA-TDC-528)

3. Klik header Class Code
4. Verifikasi Ascending `↑`: BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL
5. Klik header Class Code
6. Verifikasi Descending `↓`: NB-SL, NB-OLD, NB-KHS, NB-4, NB-2, NB-1, LAND, BLD-P, BLD-NP
7. Klik header Class Code
8. Verifikasi indikator sort hilang
9. Verifikasi urutan kembali ke default Class Code A-Z (BLD-NP sampai NB-SL)

### Sort kolom teks Class Name, Asset Type, dan Allowed Methods (TC-FA-TDC-529)

10. Klik header Class Name
11. Verifikasi Class Name Ascending: BLD-P, BLD-NP, NB-1, NB-2, NB-4, NB-OLD, NB-KHS, NB-SL, LAND
12. Klik header Class Name
13. Verifikasi Class Name Descending kebalikannya: LAND, NB-SL, NB-KHS, NB-OLD, NB-4, NB-2, NB-1, BLD-NP, BLD-P
14. Klik header Class Name
15. Verifikasi urutan kembali ke default
16. Klik header Asset Type
17. Verifikasi Asset Type Ascending: BLD-NP, BLD-P (Building), LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL (Non-building)
18. Klik header Asset Type
19. Verifikasi Asset Type Descending: Non-building (NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL), LAND, lalu Building (BLD-NP, BLD-P)
20. Verifikasi baris bernilai sama mengikuti Class Code A-Z
21. Klik header Allowed Methods
22. Verifikasi Allowed Methods Ascending: BLD-NP, BLD-P, NB-OLD, NB-SL (`Straight Line`), NB-1, NB-2, NB-4, NB-KHS (`Straight Line · Declining Balance`), LAND (`—` di akhir)
23. Klik header Allowed Methods
24. Verifikasi Allowed Methods Descending: LAND (`—` di awal), NB-1, NB-2, NB-4, NB-KHS, BLD-NP, BLD-P, NB-OLD, NB-SL

### Sort kolom teks Regulation Reference dan Modified By setelah ditampilkan (TC-FA-TDC-530)

25. Klik header Actions `⋯`
26. Centang kolom Regulation Reference
27. Centang kolom Modified By
28. Tutup Overlay Column Visibility
29. Klik header Regulation Reference
30. Verifikasi Regulation Reference Ascending: NB-SL di atas lalu 8 class lain urut Class Code
31. Klik header Regulation Reference
32. Verifikasi Regulation Reference Descending: 8 class lain urut Class Code lalu NB-SL di bawah
33. Klik header Modified By
34. Verifikasi Modified By Ascending: NB-SL (`Rina P`) di atas lalu class `System` urut Class Code
35. Klik header Modified By
36. Verifikasi Modified By Descending: class `System` urut Class Code lalu NB-SL di bawah
37. Klik header Actions `⋯`
38. Hapus centang kolom Regulation Reference
39. Hapus centang kolom Modified By
40. Tutup Overlay Column Visibility

### Sort numerik (TC-FA-TDC-531)

Untuk setiap baris tabel parameter TC-FA-TDC-531 pada Prerequisites, lakukan langkah 41 sampai 44.

41. Klik header kolom pada kolom Kolom
42. Verifikasi kolom Ascending dengan urutan pada kolom Ascending
43. Klik header kolom yang sama
44. Verifikasi kolom Descending dengan urutan pada kolom Descending

## Notes

- Langkah penghubung (S-03): langkah 25 sampai 28 (menampilkan kolom Regulation Reference dan Modified By yang Hidden), langkah 37 sampai 40 (pemulihan Setup Column agar kedua kolom kembali Hidden; 8b.14, R-24). Langkah 1 TC-FA-TDC-14 ("Buka tab `Tax Depreciation Class`") dikerjakan hook `beforeEach` suite.
- Berpindah kolom sort menjadikan kolom lama netral dan kolom baru mulai Ascending (TC-FA-TDC-535, spec lain); spec ini mengandalkan perilaku itu pada langkah 16, 21, 29, 33, dan perulangan 41 sampai 44.
- Langkah 20 menguji klausa "baris bernilai sama mengikuti Class Code A-Z" dari Expected TC-FA-TDC-529 b sebagai `Verifikasi` tersendiri.
- Spec ini 44 langkah nominal dan sekitar 56 langkah setelah ekspansi perulangan 41 sampai 44 (empat kolom), di atas ~35 langkah. Alasan: satu topik (Sort tabel utama) pada dataset Example Data yang sama, tiap blok TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan S-01 mengharuskan satu `Verifikasi` per klausa; perulangan 41 sampai 44 mengikuti idiom 8b.7 dengan parameter di Prerequisites.
- Temuan untuk QA:
  - TC-FA-TDC-14 Expected b ("tidak ada indikator sort aktif pada kolom selain default") tidak menyebut indikator pada kolom default Class Code; spec mengasersi apa adanya.
  - TC-FA-TDC-529 Expected a "Descending kebalikannya" tidak menyebut daftar eksplisit; spec menuliskan kebalikan dari Ascending.
  - TC-FA-TDC-531 Expected c Descending menyebut baris `—` "di awal" tanpa urutan antar baris `—`; spec mengasersi apa adanya.
  - TC-FA-TDC-530 langkah tidak menyebut cara menampilkan kolom Regulation Reference dan Modified By (Hidden default); spec menambah langkah penghubung lewat Overlay Column Visibility.
  - Email akun Total Control dan nama user penyunting selain `Rina P` tidak tertulis di TC.

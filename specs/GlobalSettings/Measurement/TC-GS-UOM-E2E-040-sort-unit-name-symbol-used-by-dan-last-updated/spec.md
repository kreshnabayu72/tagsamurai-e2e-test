---
id: TC-GS-UOM-E2E-040-sort-unit-name-symbol-used-by-dan-last-updated
title: "Sort 3-State Unit Name, Symbol, Used By (Items), dan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-148
  - TC-GS-UOM-149
  - TC-GS-UOM-151
  - TC-GS-UOM-152
  - TC-GS-UOM-376
  - TC-GS-UOM-377
coverage:
  web: automated
---

# Sort 3-State Unit Name, Symbol, Used By (Items), dan Last Updated

## Prerequisites

- Mode: FE+BE. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Flag Guided Tooltip halaman Measurement mengikuti pernyataan hook suite di `suite.md`.
- Akun: Total Control Client A, Sari Dewi (Sari D), `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Measurement dilakukan sekali di hook `before` suite.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (hanya dibaca; Last Updated lebih lama dari hari uji): Box / box (Used By (Items) 4), Dozen / dz (2), Gram / g (1), Kilogram / kg (1), Liter / L (0), Meter / m (0), Pack / pk (0), Pieces / pc (3).
- Data Dinamis: Population D-01 (12 unit, nama literal, Used By (Items) 0): Centimeter / cm, Millimeter / mm, Inch / in, Foot / ft, Milliliter / mL, Gallon / gal, Ounce / oz, Pound / lb, Ton / t, Roll / roll, Set / set, Sheet / sht. Di-seed lewat API di hook `before` (setara TC-GS-UOM-36), idempotent (dilewati bila sudah ada); total tabel N = 20 unit (8 Pre-setup + 12 Population), diturunkan dari seeding. Nama literal disengaja (asersi hasil bergantung pada nama; pengecualian S-12); cleanup hanya menghapus unit yang dibuat spec ini. Last Updated Population = hari uji: unit Population yang tercatat dibuat sebelum hari uji dihapus dan dibuat ulang lewat API di hook `before` supaya filter "hari ini" bermakna; jam server dan jam browser sinkron.
- Fixture backend Used By (Items) besar (D-38, D-39: Tote, Mass) tidak boleh ada selama spec ini berjalan karena mengubah urutan sort Used By (Items); fixture itu dibuat dan dibersihkan oleh spec pemakainya.
- Spec tidak mengubah data unit. Asersi sort Last Updated memakai dua nilai distinct: Pre-setup (Last Updated lebih lama dari hari uji) dan Population (Last Updated hari uji).
- State global yang dipulihkan: Sort tabel dikembalikan ke default (netral, Unit Name A-Z) di hook `after`.
- Hook `beforeEach`: buka Global Settings > Master Reference > Measurement.
- Kemampuan teknis: klik header sort; membaca indikator sort pada header kolom; hover header Checkbox dan Actions; klien HTTP/API untuk seeding Population (disediakan tim FE).
- Fixture: `fixtures/measurement.json` belum ada; tim FE menyiapkannya (lihat `suite.md`, bagian Data bersama).

## Test Steps

### TC-GS-UOM-152: Kolom Checkbox dan Actions tidak memiliki ikon sort

1. Arahkan kursor ke header kolom Checkbox
2. Arahkan kursor ke header kolom Actions
3. Verifikasi header Checkbox dan Actions tidak memiliki ikon sort

### TC-GS-UOM-148: Sort 3-state kolom Unit Name

4. Klik header Unit Name
5. Verifikasi halaman 1 terurut ascending A-Z (sama dengan urutan default): Box, Centimeter, Dozen, Foot, Gallon, Gram, Inch, Kilogram, Liter, Meter
6. Klik header Unit Name
7. Verifikasi halaman 1 terurut descending Z-A: Ton, Sheet, Set, Roll, Pound, Pieces, Pack, Ounce, Millimeter, Milliliter
8. Klik header Unit Name
9. Verifikasi indikator sort Unit Name hilang
10. Verifikasi urutan kembali ke default Unit Name A-Z: Box, Centimeter, Dozen, Foot, Gallon, Gram, Inch, Kilogram, Liter, Meter

### TC-GS-UOM-149: Sort 3-state kolom Symbol

11. Klik header Symbol
12. Verifikasi urutan ascending A-Z: baris Box (box), Centimeter (cm), Dozen (dz), dan Foot (ft) tampil berurutan dalam urutan itu pada halaman 1
13. Klik header Symbol
14. Verifikasi urutan descending: baris Ton (t), Sheet (sht), Set (set), dan Roll (roll) tampil berurutan dalam urutan itu pada halaman 1
15. Klik header Symbol
16. Verifikasi indikator sort Symbol hilang
17. Verifikasi urutan kembali ke default Unit Name A-Z: Box, Centimeter, Dozen, Foot, Gallon, Gram, Inch, Kilogram, Liter, Meter

### TC-GS-UOM-151: Sort kolom Last Updated Newest/Oldest

18. Klik header Last Updated
19. Verifikasi Oldest First (ascending, terlama di atas): halaman 1 berisi delapan unit Pre-setup (Box, Dozen, Gram, Kilogram, Liter, Meter, Pack, Pieces) di atas unit Population
20. Klik header Last Updated
21. Verifikasi sedikitnya satu baris tampil pada halaman 1
22. Verifikasi Newest First (descending, terbaru di atas): seluruh 10 baris halaman 1 adalah unit Population (tidak ada unit Pre-setup)
23. Klik header Last Updated
24. Verifikasi indikator sort Last Updated hilang
25. Verifikasi urutan kembali ke default Unit Name A-Z: Box, Centimeter, Dozen, Foot, Gallon, Gram, Inch, Kilogram, Liter, Meter

### TC-GS-UOM-376: Sort 3-state kolom Used By (Items)

26. Klik header Used By (Items) sekali
27. Verifikasi ascending numerik pada halaman 1: Centimeter, Foot, Gallon, Inch, Liter, Meter, Milliliter, Millimeter, Ounce, Pack
28. Klik Next
29. Verifikasi ascending numerik pada halaman 2: Pound, Roll, Set, Sheet, Ton, Gram, Kilogram, Dozen, Pieces, Box
30. Klik Previous
31. Klik header Used By (Items) kedua kali
32. Verifikasi descending pada halaman 1: Box, Pieces, Dozen, Gram, Kilogram, Centimeter, Foot, Gallon, Inch, Liter
33. Klik header Used By (Items) ketiga kali
34. Verifikasi indikator sort Used By (Items) hilang
35. Verifikasi urutan kembali ke default Unit Name A-Z: Box, Centimeter, Dozen, Foot, Gallon, Gram, Inch, Kilogram, Liter, Meter

### TC-GS-UOM-377: Sort Used By (Items): angka sama diurutkan Unit Name A-Z (ascending dan descending)

36. Klik header Used By (Items) sekali
37. Verifikasi ascending pada halaman 1: kelompok bernilai `0` terurut A-Z (Centimeter sebelum Foot sebelum Gallon)
38. Klik Next
39. Verifikasi ascending pada halaman 2: kelompok bernilai `1` terurut Gram sebelum Kilogram
40. Klik Previous
41. Klik header Used By (Items) kedua kali
42. Verifikasi descending pada halaman 1: kelompok bernilai `1` tetap Gram sebelum Kilogram (tiebreaker A-Z, tidak dibalik)
43. Verifikasi descending pada halaman 1: kelompok bernilai `0` tetap A-Z (Centimeter sebelum Foot sebelum Gallon)
44. Klik header Used By (Items) ketiga kali

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (44). Alasan: semua blok satu topik (Sort header kolom) pada dataset dan akun yang sama tanpa mengubah data; tiap blok diakhiri klik ketiga yang mengembalikan sort ke netral (default Unit Name A-Z), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC dalam spec: 152, 148, 149, 151, 376, 377 (urutan sumber 148, 149, 151, 152, 376, 377); TC-GS-UOM-152 (screening tanpa aksi sort) dipindah ke awal.
- Langkah 21 adalah `Verifikasi` pembanding (butir 2 bagian 8b), bukan dari Expected TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 30 dan 40 (kembali ke halaman 1 sebelum klik header kedua, karena posisi halaman setelah perubahan sort tidak dinyatakan TC); langkah 44 (mengembalikan sort ke netral di akhir spec; hook `after` sebagai cadangan).
- Asersi urutan memakai baseline N = 20 unit (8 Pre-setup + 12 Population) dengan 10 baris per halaman; urutan Used By (Items) pada TC-GS-UOM-376 mengikuti Data Uji TC (15 unit bernilai 0, Gram 1, Kilogram 1, Dozen 2, Pieces 3, Box 4).
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-UOM-149: Expected tidak menyebut isi urutan Symbol dan TC tidak menyatakan apakah pengurutan Symbol sensitif huruf besar-kecil (Symbol `L` Liter berhuruf besar). Spec hanya mengasersi urutan relatif Symbol yang sama untuk kedua aturan (box, cm, dz, ft; t, sht, set, roll).
  - TC-GS-UOM-151: Expected tidak menyebut baris yang tampil dan Last Updated berketelitian menit; urutan antarbaris dengan menit yang sama tidak diasersi. Spec mengasersi kelompok (Pre-setup lebih lama dari Population).
  - TC-GS-UOM-376: posisi halaman sesudah klik header kedua tidak dinyatakan TC; spec kembali ke halaman 1 dengan `Previous` sebelum klik kedua.

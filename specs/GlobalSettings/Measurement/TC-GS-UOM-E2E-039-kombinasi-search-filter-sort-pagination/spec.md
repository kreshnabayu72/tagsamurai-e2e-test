---
id: TC-GS-UOM-E2E-039-kombinasi-search-filter-sort-pagination
title: "Kombinasi Search, Filter, Sort, dan Pagination serta Pemulihan Empty State dan Dampak Mutasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-142
  - TC-GS-UOM-143
  - TC-GS-UOM-144
  - TC-GS-UOM-145
  - TC-GS-UOM-146
  - TC-GS-UOM-147
  - TC-GS-UOM-155
  - TC-GS-UOM-284
  - TC-GS-UOM-285
  - TC-GS-UOM-286
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, dan Pagination serta Pemulihan Empty State dan Dampak Mutasi

## Prerequisites

- Mode: FE+BE. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Flag Guided Tooltip halaman Measurement mengikuti pernyataan hook suite di `suite.md`.
- Akun: Total Control Client A, Sari Dewi (Sari D), `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Measurement dilakukan sekali di hook `before` suite.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (hanya dibaca; Last Updated lebih lama dari hari uji): Box / box (Used By (Items) 4), Dozen / dz (2), Gram / g (1), Kilogram / kg (1), Liter / L (0), Meter / m (0), Pack / pk (0), Pieces / pc (3).
- Data Dinamis: Population D-01 (12 unit, nama literal, Used By (Items) 0): Centimeter / cm, Millimeter / mm, Inch / in, Foot / ft, Milliliter / mL, Gallon / gal, Ounce / oz, Pound / lb, Ton / t, Roll / roll, Set / set, Sheet / sht. Di-seed lewat API di hook `before` (setara TC-GS-UOM-36), idempotent (dilewati bila sudah ada); total tabel N = 20 unit (8 Pre-setup + 12 Population), diturunkan dari seeding. Nama literal disengaja (asersi hasil bergantung pada nama; pengecualian S-12); cleanup hanya menghapus unit yang dibuat spec ini. Last Updated Population = hari uji: unit Population yang tercatat dibuat sebelum hari uji dihapus dan dibuat ulang lewat API di hook `before` supaya filter "hari ini" bermakna; jam server dan jam browser sinkron.
- Data milik spec (bersuffix `{runId}-039`, dibuat lewat API; klien HTTP/API disediakan tim FE): `Kilogram Force {runId}-039` / `kg` (dibuat sebelum TC-GS-UOM-142, dipakai sebagai precondition Expected TC-GS-UOM-142 dan TC-GS-UOM-143, dihapus sesudah TC-GS-UOM-143); `Tub {runId}-039` / `tb` bebas relasi (D-23, dibuat sebelum TC-GS-UOM-286 dan diubah nama menjadi `Basin {runId}-039`); `Yard {runId}-039` / `yd` (D-15, dibuat lewat UI oleh TC-GS-UOM-147). Hook `after` menghapus ketiganya lewat API tanpa berasumsi seeding berhasil penuh.
- Rentang "01 Jan 2020 – hari ini" mengasumsikan Last Updated seluruh unit Pre-setup berada pada atau setelah 01 Jan 2020.
- State global yang dipulihkan: Search, Filter, Sort, dan page size tabel dikembalikan ke default di hook `after`.
- Hook `beforeEach`: buka Global Settings > Master Reference > Measurement.
- Kemampuan teknis: pengisian date range picker Last Updated; klik header sort; pemilihan page size; klien HTTP/API untuk seeding dan cleanup.
- Fixture: `fixtures/measurement.json` belum ada; tim FE menyiapkannya (lihat `suite.md`, bagian Data bersama).

## Test Steps

### TC-GS-UOM-142: Search lalu Filter Last Updated menghasilkan irisan keduanya

1. Buat unit `Kilogram Force {runId}-039` dengan Symbol `kg` lewat API
2. Ketik Search `kilo`, tekan Enter
3. Klik Filter
4. Isi Last Updated rentang 01 Jan 2020 – hari ini
5. Klik [Apply]
6. Verifikasi tabel menampilkan tepat dua baris: Kilogram dan `Kilogram Force {runId}-039`

### TC-GS-UOM-143: Filter Last Updated lalu Search menghasilkan irisan keduanya

7. Klik `(←)` pada kotak Search
8. Klik [Clear Field]
9. Klik [Apply]
10. Isi Last Updated rentang 01 Jan 2020 – hari ini
11. Klik [Apply]
12. Ketik Search `kilo`, tekan Enter
13. Verifikasi tabel menampilkan tepat dua baris: Kilogram dan `Kilogram Force {runId}-039`
14. Hapus unit `Kilogram Force {runId}-039` lewat API

### TC-GS-UOM-144: Kombinasi Search, Filter, Sort, dan Pagination

15. Klik `(←)` pada kotak Search
16. Klik [Clear Field]
17. Klik [Apply]
18. Ketik Search `m`, tekan Enter
19. Isi Last Updated rentang hari uji – hari uji (hari ini – hari ini)
20. Klik [Apply]
21. Klik header Symbol sekali (ascending)
22. Pilih page size 25
23. Verifikasi tabel menampilkan Centimeter, Milliliter, dan Millimeter (memenuhi Search `m` dan Filter hari ini)
24. Verifikasi Meter tidak tampil (Last Updated lebih lama dari hari uji)
25. Verifikasi hasil terurut Symbol A-Z: cm, mL, mm
26. Verifikasi hasil berada dalam satu halaman

### TC-GS-UOM-145: Clear Filter saat Search dan Sort aktif mempertahankan keduanya

27. Pilih page size 10
28. Klik `(←)` pada kotak Search
29. Klik [Clear Field]
30. Klik [Apply]
31. Klik header Symbol dua kali (descending lalu netral)
32. Ketik Search `m`, tekan Enter
33. Klik header Symbol sekali (ascending)
34. Isi Last Updated rentang 01 Jan 2020 – hari ini
35. Klik [Apply]
36. Klik [Clear Field]
37. Klik [Apply]
38. Verifikasi kotak Search tetap berisi `m`
39. Verifikasi tabel menampilkan enam baris yang memuat `m`: Centimeter, Gram, Kilogram, Meter, Milliliter, Millimeter
40. Verifikasi sort Symbol ascending tetap aktif

### TC-GS-UOM-146: Clear Search saat Filter dan Sort aktif mempertahankan keduanya

41. Klik `(←)` pada kotak Search
42. Klik header Symbol dua kali (descending lalu netral)
43. Isi Last Updated rentang hari uji – hari uji (hari ini – hari ini)
44. Klik [Apply]
45. Klik header Unit Name dua kali (descending)
46. Ketik Search `m`, tekan Enter
47. Klik `(✕)` pada input Search
48. Tekan Enter
49. Verifikasi halaman 1 menampilkan berurutan Ton, Sheet, Set, Roll, Pound, Ounce, Millimeter, Milliliter, Inch, Gallon
50. Verifikasi filter Last Updated hari ini tetap aktif: Pieces tidak tampil
51. Verifikasi sort Unit Name descending tetap aktif

### TC-GS-UOM-155: Apply Filter dari halaman 2 mereset ke halaman 1

52. Klik `(←)` pada kotak Search
53. Klik header Unit Name sekali (netral)
54. Klik [Clear Field]
55. Klik [Apply]
56. Klik Next untuk pindah ke halaman 2
57. Isi Last Updated rentang hari uji – hari uji (hari ini – hari ini)
58. Klik [Apply]
59. Verifikasi halaman 1 aktif
60. Verifikasi halaman 1 menampilkan Centimeter, Foot, Gallon, Inch, Milliliter, Millimeter, Ounce, Pound, Roll, Set

### TC-GS-UOM-284: Berpindah kolom sort saat Search dan Filter aktif tidak mereset Search maupun Filter

61. Ketik Search `m`, tekan Enter
62. Isi Last Updated rentang 01 Jan 2020 – hari ini
63. Klik [Apply]
64. Klik header Unit Name sekali
65. Verifikasi hasil terurut Unit Name A-Z: Centimeter, Gram, Kilogram, Meter, Milliliter, Millimeter
66. Verifikasi kotak Search tetap berisi `m`
67. Verifikasi filter Last Updated 01 Jan 2020 – hari ini tetap aktif
68. Klik header Symbol sekali
69. Verifikasi indikator sort Unit Name hilang (netral)
70. Verifikasi sort Symbol ascending A-Z
71. Verifikasi kotak Search tetap berisi `m`
72. Verifikasi filter Last Updated 01 Jan 2020 – hari ini tetap aktif
73. Verifikasi himpunan baris hasil sama: Centimeter, Gram, Kilogram, Meter, Milliliter, Millimeter

### TC-GS-UOM-285: Empty state akibat kombinasi Search dan Filter pulih saat salah satu kontrol dilepas

74. Klik header Symbol dua kali (descending lalu netral)
75. Ganti isi kotak Search dengan `Dozen`, tekan Enter
76. Isi Last Updated rentang hari uji – hari uji (hari ini – hari ini)
77. Klik [Apply]
78. Verifikasi tabel menampilkan `No results found`
79. Verifikasi tabel menampilkan `Try adjusting your search or filter.`
80. Klik [Clear Field]
81. Klik [Apply]
82. Verifikasi baris Dozen tampil
83. Verifikasi kotak Search tetap berisi `Dozen`

### TC-GS-UOM-147: Unit baru yang tidak cocok dengan Search aktif tidak muncul

84. Ganti isi kotak Search dengan `kilo`, tekan Enter
85. Klik [+ Unit]
86. Isi Unit Name `Yard {runId}-039`
87. Isi Symbol `yd`
88. Klik [Submit]
89. Verifikasi toast `Success, unit has been created.`
90. Verifikasi baris Kilogram tampil (Search `kilo` aktif)
91. Verifikasi baris `Yard {runId}-039` tidak tampil selama Search `kilo` aktif

### TC-GS-UOM-286: Edit yang membuat nama tidak cocok dengan Search aktif mengeluarkan baris dari hasil

92. Klik `(←)` pada kotak Search
93. Buat unit `Tub {runId}-039` dengan Symbol `tb` lewat API
94. Ketik Search `Tub`, tekan Enter
95. Verifikasi baris `Tub {runId}-039` tampil
96. Klik `⋯` pada baris `Tub {runId}-039`, pilih Edit
97. Ubah Unit Name menjadi `Basin {runId}-039`
98. Klik [Save]
99. Verifikasi toast `Success, unit has been updated.`
100. Verifikasi kotak Search tetap berisi `Tub`
101. Verifikasi baris `Basin {runId}-039` tidak lagi tampil pada hasil Search `Tub`
102. Kosongkan isi kotak Search, tekan Enter
103. Verifikasi baris `Basin {runId}-039` dengan Symbol `tb` tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (103). Alasan: semua blok satu topik (kombinasi kontrol tabel: Search, Filter, Sort, Pagination) pada satu dataset dan akun; tiap blok dimulai dari state kontrol yang dibersihkan eksplisit (langkah penghubung di bawah) dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Aksi tulis (TC-GS-UOM-147 dan TC-GS-UOM-286) ditaruh paling akhir.
- Urutan TC dalam spec: 142, 143, 144, 145, 146, 155, 284, 285, 147, 286 (urutan sumber 142, 143, 144, 145, 146, 147, 155, 284, 285, 286). TC-GS-UOM-147 dan TC-GS-UOM-286 membuat atau mengubah unit sehingga dipindah ke akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7, 27, 41, 52, dan 74 beserta langkah pembersih sesudahnya dalam blok yang sama (mengosongkan Search, Filter, Sort, dan page size dari blok sebelumnya); langkah 14 (menghapus Kilogram Force sebelum TC yang membaca baseline 20 unit); langkah 84 (mengganti isi kotak Search yang masih berisi `Dozen`).
- Nama unit milik spec bersuffix menggantikan literal `Yard` dan `Tub`/`Basin` pada Expected TC (S-06, S-12).
- Panel Filter tetap terbuka sesudah `[Apply]` (mengikuti urutan langkah TC-GS-UOM-141, 293, 285); langkah "Klik Filter" hanya pada pembukaan pertama.
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec. Dampak mutasi dari tabel (Yard, Tub) di surface lain (log) tidak diasersi di spec ini.
- Temuan untuk QA:
  - TC-GS-UOM-142 dan TC-GS-UOM-143: Expected menyebut `Kilogram Force` (D-07, dibuat TC-GS-UOM-53) tetapi kolom Dependensi dan Precondition tidak mencantumkannya. Spec membuat `Kilogram Force {runId}-039` lewat API dan memakai nama bersuffix pada asersi.
  - TC-GS-UOM-144: Expected tidak menyebut baris hasil; spec mengasersi Centimeter, Milliliter, Millimeter berdasarkan Population (Symbol cm, mL, mm). Urutan Symbol `mL` dan `mm` sama untuk pengurutan sensitif maupun tidak sensitif huruf besar.
  - TC-GS-UOM-145, 146: Expected hanya menyatakan Search/Filter dan Sort "tetap aktif"; spec mengasersinya lewat isi kotak Search, himpunan baris, dan urutan, bukan indikator visual.
  - TC-GS-UOM-284: urutan Unit Name A-Z dan Symbol A-Z pada himpunan hasil kebetulan sama, sehingga perpindahan sort dibuktikan lewat hilangnya indikator Unit Name dan indikator Symbol, bukan lewat perubahan urutan baris.
  - TC-GS-UOM-286 langkah 4: "Kosongkan Search lalu tekan Enter" tidak menyebut aksi (`(←)` atau hapus isi); spec memakai "kosongkan isi kotak Search, tekan Enter".

---
id: TC-GS-UOM-E2E-038-filter-used-by-items-rentang
title: "Filter Used By (Items): Min, Max, Inklusif, Input Angka, Min > Max, dan Kombinasi dengan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-379
  - TC-GS-UOM-380
  - TC-GS-UOM-381
  - TC-GS-UOM-382
  - TC-GS-UOM-383
  - TC-GS-UOM-392
coverage:
  web: automated
---

# Filter Used By (Items): Min, Max, Inklusif, Input Angka, Min > Max, dan Kombinasi dengan Last Updated

## Prerequisites

- Mode: FE+BE. Suite berjalan serial (`parallel: false`, lihat `suite.md`). Spec tidak mengubah data unit.
- Flag Guided Tooltip halaman Measurement mengikuti pernyataan hook suite di `suite.md`.
- Akun: Total Control Client A, Sari Dewi (Sari D), `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Measurement dilakukan sekali di hook `before` suite.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (hanya dibaca; Last Updated lebih lama dari hari uji; relasi tidak diubah TC lain): Box / box (Used By 4), Dozen / dz (2), Gram / g (1), Kilogram / kg (1), Pieces / pc (3), Liter / L (0), Meter / m (0), Pack / pk (0).
- Data Dinamis: Population D-01 (12 unit, nama literal, Used By 0, Last Updated hari uji): Centimeter / cm, Millimeter / mm, Inch / in, Foot / ft, Milliliter / mL, Gallon / gal, Ounce / oz, Pound / lb, Ton / t, Roll / roll, Set / set, Sheet / sht. Di-seed lewat API di hook `before` (setara TC-GS-UOM-36), idempotent (dilewati bila sudah ada); total tabel N = 20 unit (8 Pre-setup + 12 Population), diturunkan dari seeding; 15 unit bernilai 0 (3 Pre-setup + 12 Population). Unit Population yang tercatat dibuat sebelum hari uji dihapus dan dibuat ulang lewat API di hook `before` supaya Last Updated = hari uji (TC-GS-UOM-383). Nama literal disengaja (asersi hasil bergantung pada nama; pengecualian S-12); cleanup hanya menghapus unit yang dibuat spec ini.
- Fixture backend Used By (Items) besar (D-38, D-39: Tote, Mass) tidak boleh ada selama spec ini berjalan karena mengubah himpunan hasil filter; fixture itu dibuat dan dibersihkan oleh spec pemakainya.
- State global yang dipulihkan: Filter dan Sort tabel dikembalikan ke default di hook `after`.
- Hook `beforeEach`: buka Global Settings > Master Reference > Measurement.
- Kemampuan teknis: pengetikan keystroke ke input Min dan Max Filter Panel; pengisian date range picker Last Updated; klien HTTP/API untuk seeding Population (disediakan tim FE).
- Fixture: `fixtures/measurement.json` belum ada; tim FE menyiapkannya (lihat `suite.md`, bagian Data bersama).

## Test Steps

### TC-GS-UOM-392: Input filter Used By (Items) hanya menerima angka bulat 0 ke atas

1. Klik Filter
2. Ketik `-3` di field Min
3. Verifikasi field Min berisi `3` (tanda minus tidak masuk)
4. Kosongkan field Min
5. Ketik `2.5` di field Min
6. Verifikasi field Min berisi `25` (titik tidak masuk)
7. Kosongkan field Min
8. Ketik `abc` di field Min
9. Verifikasi field Min tetap kosong (huruf tidak masuk)
10. Ketik `-3` di field Max
11. Verifikasi field Max berisi `3` (tanda minus tidak masuk)
12. Kosongkan field Max
13. Ketik `2.5` di field Max
14. Verifikasi field Max berisi `25` (titik tidak masuk)
15. Kosongkan field Max
16. Ketik `abc` di field Max
17. Verifikasi field Max tetap kosong (huruf tidak masuk)
18. Verifikasi tidak ada pesan error di field Min
19. Verifikasi tidak ada pesan error di field Max

### TC-GS-UOM-379: Filter Used By (Items) hanya Min

20. Isi Min `2`, biarkan Max kosong
21. Klik [Apply]
22. Verifikasi tabel menampilkan tepat tiga baris: Dozen (2), Pieces (3), Box (4)
23. Verifikasi tidak ada pesan error

### TC-GS-UOM-380: Filter Used By (Items) hanya Max, termasuk Max 0

24. Kosongkan field Min, isi Max `1`
25. Klik [Apply]
26. Verifikasi halaman 1 menampilkan 10 baris termasuk Gram dan Kilogram
27. Verifikasi Dozen dan Box tidak tampil di halaman 1
28. Klik Next
29. Verifikasi halaman 2 menampilkan 7 baris (total 17 unit: 15 bernilai 0, Gram, dan Kilogram)
30. Verifikasi Pieces tidak tampil di halaman 2
31. Ubah Max menjadi `0`
32. Klik [Apply]
33. Verifikasi halaman 1 menampilkan 10 baris bernilai 0 (Centimeter, Foot, Gallon, Inch, Liter, Meter, Milliliter, Millimeter, Ounce, Pack)
34. Verifikasi Gram dan Kilogram tidak tampil di halaman 1
35. Klik Next
36. Verifikasi halaman 2 menampilkan 5 baris bernilai 0 (Pound, Roll, Set, Sheet, Ton; total 15 unit)
37. Verifikasi Gram dan Kilogram tidak tampil di halaman 2

### TC-GS-UOM-381: Filter Used By (Items) Min dan Max bersifat inklusif

38. Isi Min `1` dan Max `3`
39. Klik [Apply]
40. Verifikasi tabel menampilkan Gram (1), Kilogram (1), Dozen (2), Pieces (3); batas 1 dan 3 ikut tampil
41. Verifikasi Box (4) dan unit bernilai 0 tidak tampil (hasil tepat empat baris)

### TC-GS-UOM-383: Kombinasi filter Used By (Items) dan Last Updated bersifat AND

42. Isi Last Updated rentang hari uji – hari uji (hari ini – hari ini), Min `0`, Max `0`
43. Klik [Apply]
44. Verifikasi halaman 1 menampilkan 10 unit Population (Centimeter, Foot, Gallon, Inch, Milliliter, Millimeter, Ounce, Pound, Roll, Set) tanpa Liter, Meter, Pack
45. Klik Next
46. Verifikasi halaman 2 hanya menampilkan Sheet dan Ton (total 12 unit Population)
47. Ubah Min menjadi `1` dan kosongkan Max
48. Klik [Apply]
49. Verifikasi empty state `No results found`

### TC-GS-UOM-382: Filter Used By (Items) Min lebih besar dari Max mengikuti perilaku bawaan komponen Range Filter

50. Klik [Clear Field]
51. Isi Min `4` dan Max `2`
52. Verifikasi field Min berisi `4` dan field Max berisi `2`
53. Klik [Apply]
54. Verifikasi tidak ada copy error khusus modul Measurement pada Filter Panel

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (54; langkah 2 sampai 17 mengulang pola ketik-verifikasi-kosongkan untuk dua field dan tiga nilai uji). Alasan: semua blok satu topik (Filter Used By (Items)) pada satu Filter Panel, dataset, dan akun yang sama; tiap blok diawali penggantian nilai field dari blok sebelumnya dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC dalam spec: 392, 379, 380, 381, 383, 382 (urutan sumber 379, 380, 381, 382, 383, 392). TC-GS-UOM-392 (input tanpa Apply) di awal; TC-GS-UOM-382 paling akhir karena Expected-nya tidak deterministik dan hasil perilaku bawaan tidak boleh memengaruhi TC lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 28, 35, dan 45 (pindah ke halaman 2 untuk menuntaskan asersi hasil lintas halaman) dan langkah 50 (mengosongkan seluruh field sebelum TC-GS-UOM-382). Panel Filter tetap terbuka sesudah `[Apply]`, mengikuti urutan langkah TC-GS-UOM-380 dan TC-GS-UOM-383, sehingga nilai field blok berikutnya langsung menggantikan nilai blok sebelumnya.
- Reset halaman: `[Apply]` dari halaman >1 mereset ke halaman 1 (TC-GS-UOM-155 di spec 039), sehingga asersi halaman 1 sesudah langkah 32, 39, 43, dan 48 tidak memerlukan langkah kembali ke halaman 1.
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-UOM-382 (Manual Only): Expected "perilaku sesuai bawaan komponen FilterContainer varian Range Filter (Storybook)" tidak deterministik. Spec hanya mengasersi bagian yang pasti (tidak ada copy error khusus modul Measurement) dan tidak mengasersi tebakan atas hasil `[Apply]`; hasil perilaku bawaan (apakah field ditolak, hasil kosong, atau Apply dinonaktifkan) perlu dicatat QA saat eksekusi. Butir "Catatan QA" pada Expected tidak punya padanan asersi.
  - TC-GS-UOM-392: Expected menyebut "tanda minus, titik/koma desimal, dan huruf", tetapi Data Uji hanya `-3`, `2.5`, dan `abc` (tanpa koma). Spec mengikuti Data Uji; input dengan koma tidak diuji.
  - TC-GS-UOM-380 dan TC-GS-UOM-383: hitungan 17, 15, dan 12 unit bergantung pada baseline tepat 20 unit; hitungan hasil diasersi lewat isi halaman 1 dan halaman 2 (10 baris per halaman).
  - TC-GS-UOM-383: Expected langkah 4 (`No results found`) mengasumsikan semua unit bernilai ≥ 1 adalah Pre-setup dengan Last Updated lama.
  - TC tidak menyatakan eksplisit apakah panel Filter menutup setelah `[Apply]`; spec mengikuti urutan langkah TC (panel tetap terbuka).

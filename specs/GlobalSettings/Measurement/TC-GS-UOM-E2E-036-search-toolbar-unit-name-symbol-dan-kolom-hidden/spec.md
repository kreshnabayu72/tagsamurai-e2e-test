---
id: TC-GS-UOM-E2E-036-search-toolbar-unit-name-symbol-dan-kolom-hidden
title: "Search Toolbar: Siklus Search, Pencocokan Unit Name dan Symbol, Kolom Hidden, dan Reset Halaman"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-125
  - TC-GS-UOM-126
  - TC-GS-UOM-127
  - TC-GS-UOM-130
  - TC-GS-UOM-131
  - TC-GS-UOM-132
  - TC-GS-UOM-338
  - TC-GS-UOM-384
coverage:
  web: automated
---

# Search Toolbar: Siklus Search, Pencocokan Unit Name dan Symbol, Kolom Hidden, dan Reset Halaman

## Prerequisites

- Mode: FE+BE. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Flag Guided Tooltip halaman Measurement mengikuti pernyataan hook suite di `suite.md`.
- Akun: Total Control Client A, Sari Dewi (Sari D), `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Measurement dilakukan sekali di hook `before` suite.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (hanya dibaca; Last Updated lebih lama dari hari uji): Box / box, Dozen / dz, Gram / g, Kilogram / kg, Liter / L, Meter / m, Pack / pk, Pieces / pc. Used By (Items): Box 4, Dozen 2, Gram 1, Kilogram 1, Pieces 3, Liter 0, Meter 0, Pack 0.
- Data Dinamis: Population D-01 (12 unit, nama literal): Centimeter / cm, Millimeter / mm, Inch / in, Foot / ft, Milliliter / mL, Gallon / gal, Ounce / oz, Pound / lb, Ton / t, Roll / roll, Set / set, Sheet / sht. Di-seed lewat API di hook `before` (setara TC-GS-UOM-36), idempotent (dilewati bila sudah ada), sehingga total tabel N = 20 unit (8 Pre-setup + 12 Population), diturunkan dari seeding. Nama literal disengaja (asersi hasil Search bergantung pada nama Population; pengecualian S-12); suite serial dan cleanup hanya menghapus unit yang dibuat spec ini.
- Data milik spec (dipakai di TC-GS-UOM-126): unit `Kilogram Force {runId}-036` dengan Symbol `kg`, dibuat lewat API tepat sebelum Search TC-GS-UOM-126 (dipakai sebagai precondition TC, Dependensi TC-GS-UOM-53) dan dihapus lewat API segera sesudahnya; hook `after` menghapusnya bila masih ada.
- State global yang dipulihkan: visibilitas kolom tabel Measurement (semua kolom tampil), Search, dan Sort dikembalikan ke default di hook `after`.
- Hook `beforeEach`: buka Global Settings > Master Reference > Measurement.
- Kemampuan teknis: Column Visibility lewat header kolom Actions (`⋯`); membaca teks sel Last Updated baris Meter; klien HTTP/API untuk seeding dan cleanup unit (disediakan tim FE).
- Fixture: `fixtures/measurement.json` belum ada; tim FE menyiapkannya (lihat `suite.md`, bagian Data bersama).

## Test Steps

### TC-GS-UOM-125: Siklus Search toolbar: reveal, auto-focus, icon clear, Enter, dan collapse

1. Arahkan kursor ke icon Search
2. Verifikasi tooltip `Search` muncul
3. Klik icon Search
4. Verifikasi input Search muncul dengan placeholder `Search unit name or symbol...`
5. Verifikasi input Search langsung fokus
6. Ketik `kilo` di input Search tanpa menekan Enter
7. Verifikasi icon `(✕)` muncul di sisi kanan input
8. Verifikasi tabel belum tersaring (halaman 1 masih 10 baris dari 20 unit, 2 halaman)
9. Tekan Enter
10. Verifikasi baris Kilogram tampil
11. Verifikasi tabel hanya menampilkan baris yang memuat `kilo` (Kilogram)
12. Klik `(✕)` pada input
13. Verifikasi teks input terhapus
14. Verifikasi input tetap terbuka dengan kursor fokus
15. Verifikasi tabel masih menampilkan hasil `kilo` (Kilogram), belum reset
16. Tekan Enter pada input yang sudah kosong
17. Verifikasi tabel reset menampilkan seluruh data (10 baris di halaman 1, 2 halaman)
18. Ketik Search `kilo`, tekan Enter
19. Klik icon panah `(←)`
20. Verifikasi kotak pencarian menutup menjadi icon Search
21. Verifikasi tabel langsung reset menampilkan seluruh data (10 baris di halaman 1, 2 halaman)
22. Klik icon Search
23. Verifikasi input Search kosong (keyword `kilo` sudah dikosongkan)

### TC-GS-UOM-127: Search mencocokkan Symbol

24. Ketik Search `gal`, tekan Enter
25. Verifikasi baris Gallon dengan Symbol `gal` tampil
26. Verifikasi tabel hanya menampilkan Gallon

### TC-GS-UOM-130: Last Updated tidak dapat dicari

27. Klik `(←)` pada kotak Search
28. Baca teks sel Last Updated baris Meter
29. Ketik Search teks Last Updated baris Meter yang dibaca pada langkah 28, tekan Enter
30. Verifikasi tidak ada baris cocok: empty state `No results found`

### TC-GS-UOM-384: Search tabel utama tidak mencocokkan angka Used By (Items)

31. Ganti isi kotak Search dengan `4`, tekan Enter
32. Verifikasi empty state `No results found`
33. Verifikasi baris Box tidak muncul (angka Used By (Items) `4` tidak dicari)
34. Ganti isi kotak Search dengan `3`, tekan Enter
35. Verifikasi empty state `No results found`
36. Verifikasi baris Pieces tidak muncul (angka Used By (Items) `3` tidak dicari)

### TC-GS-UOM-132: Search dari halaman 2 mereset ke halaman 1

37. Klik `(←)` pada kotak Search
38. Klik Next untuk pindah ke halaman 2
39. Ketik Search `m`, tekan Enter
40. Verifikasi baris Meter tampil
41. Verifikasi hasil ditampilkan mulai halaman 1 (halaman 1 aktif)

### TC-GS-UOM-131: Search tidak mencari kolom Symbol yang di-hide

42. Klik `(←)` pada kotak Search
43. Ketik Search `kg`, tekan Enter
44. Verifikasi baris Kilogram ditemukan (Symbol `kg`)
45. Klik header kolom Actions (`⋯`) untuk membuka panel Column Visibility
46. Uncheck kolom `Symbol`
47. Ganti isi kotak Search dengan `kg`, tekan Enter
48. Verifikasi empty state `No results found` dengan teks `Try adjusting your search or filter.`
49. Klik header kolom Actions (`⋯`)
50. Check kembali kolom `Symbol`
51. Ganti isi kotak Search dengan `kg`, tekan Enter
52. Verifikasi baris Kilogram kembali ditemukan

### TC-GS-UOM-338: Search tidak mencari kolom Unit Name yang di-hide

53. Klik `(←)` pada kotak Search
54. Klik header kolom Actions (`⋯`) untuk membuka panel Column Visibility
55. Uncheck kolom `Unit Name`
56. Ketik Search `Kilogram`, tekan Enter
57. Verifikasi tabel menampilkan empty state `No results found`
58. Klik header kolom Actions (`⋯`)
59. Check kembali kolom `Unit Name`
60. Tekan Enter pada kotak Search `Kilogram`
61. Verifikasi baris Kilogram tampil kembali

### TC-GS-UOM-126: Search Unit Name substring tanpa membedakan huruf besar kecil

62. Klik `(←)` pada kotak Search
63. Buat unit `Kilogram Force {runId}-036` dengan Symbol `kg` lewat API
64. Ketik Search `GRAM`, tekan Enter
65. Verifikasi hasil Search tepat tiga baris: Gram, Kilogram, dan `Kilogram Force {runId}-036`
66. Klik `(←)` pada kotak Search
67. Hapus unit `Kilogram Force {runId}-036` lewat API

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (67). Alasan: semua blok satu topik (Search tabel utama) pada dataset dan akun yang sama, tanpa mengubah data baris Pre-setup atau Population; tiap blok dimulai dari Search bersih (langkah penghubung `(←)`) dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC dalam spec: 125, 127, 130, 384, 132, 131, 338, 126 (urutan sumber 125, 126, 127, 130, 131, 132, 338, 384). TC-GS-UOM-131 dan TC-GS-UOM-338 mengubah visibilitas kolom dan dipulihkan di dalam bloknya (langkah 50 dan 59); TC-GS-UOM-126 ditaruh paling akhir karena memerlukan unit tambahan (Kilogram Force) yang akan mengubah baseline 20 unit bagi TC lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 22 dan 23 membuka ulang input Search untuk membuktikan keyword `kilo` terhapus oleh `(←)` (Expected TC-GS-UOM-125 butir f "keyword dikosongkan"); langkah 27, 37, 42, 53, 62, 66 menutup Search dan mereset tabel antar-TC; langkah 28 membaca teks Last Updated Meter (TC-GS-UOM-130 hanya memberi contoh `15 Jun`); langkah 38 memindah ke halaman 2 (TC-GS-UOM-132 langkah 1); langkah 63 dan 67 menyiapkan dan memulihkan unit tambahan.
- TC-GS-UOM-384: Data Uji menyebut `1250` "atau angka lain dari kolom Used By (Items)". Angka 1250 hanya ada di fixture backend D-39 yang tidak ada pada baseline 20 unit, sehingga spec memakai angka nyata Pieces (`3`) di samping `4` milik Box.
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-UOM-126: Expected memuat `Kilogram Force` (D-07, dibuat TC-GS-UOM-53) dan Dependensi mencantumkan TC-GS-UOM-53, tetapi Precondition menyebut "20 unit tersedia" tanpa Kilogram Force. Spec membuat unit bersuffix `Kilogram Force {runId}-036` lewat API; nama unit di Expected diganti nama bersuffix.
  - TC-GS-UOM-130: Data Uji `15 Jun` hanya contoh; format sel Last Updated mengikuti General Settings (default `dd/MM/yy` + `HH:mm`), sehingga spec mencari teks sel yang dibaca dari baris Meter, bukan literal `15 Jun`.
  - TC-GS-UOM-131 dan TC-GS-UOM-338 sama-sama menguji Search terhadap kolom yang di-hide (Symbol dan Unit Name); keduanya dipertahankan sesuai TC.
  - TC-GS-UOM-132: Expected "Hasil ditampilkan mulai halaman 1" tidak menyebut jumlah hasil; spec hanya mengasersi baris Meter dan halaman 1 aktif.

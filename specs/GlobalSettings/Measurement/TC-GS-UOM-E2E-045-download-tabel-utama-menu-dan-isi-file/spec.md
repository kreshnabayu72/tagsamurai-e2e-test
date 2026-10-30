---
id: TC-GS-UOM-E2E-045-download-tabel-utama-menu-dan-isi-file
title: "Download Tabel Measurement: Menu, Isi File CSV dan XLSX, Kolom Visible, dan Used By (Items)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-165
  - TC-GS-UOM-166
  - TC-GS-UOM-167
  - TC-GS-UOM-168
  - TC-GS-UOM-170
  - TC-GS-UOM-386
coverage:
  web: automated
---

# Download Tabel Measurement: Menu, Isi File CSV dan XLSX, Kolom Visible, dan Used By (Items)

## Prerequisites

- Mode: FE+BE. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Flag Guided Tooltip halaman Measurement mengikuti pernyataan hook suite di `suite.md`.
- Fixture: `fixtures/measurement.json` belum ada; tim FE menyiapkannya (lihat `suite.md`, bagian Data bersama).
- Akun: Total Control Client A, Sari Dewi (Sari D), `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Measurement dilakukan sekali di hook `before` suite.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (hanya dibaca; Last Updated lebih lama dari hari uji): Box / box (Used By (Items) 4), Dozen / dz (2), Gram / g (1), Kilogram / kg (1), Liter / L (0), Meter / m (0), Pack / pk (0), Pieces / pc (3).
- Data Dinamis: Population D-01 (12 unit, nama literal, Used By (Items) 0): Centimeter / cm, Millimeter / mm, Inch / in, Foot / ft, Milliliter / mL, Gallon / gal, Ounce / oz, Pound / lb, Ton / t, Roll / roll, Set / set, Sheet / sht. Di-seed lewat API di hook `before` (setara TC-GS-UOM-36), idempotent (dilewati bila sudah ada); total tabel N = 20 unit (8 Pre-setup + 12 Population), diturunkan dari seeding. Nama literal disengaja (asersi hasil bergantung pada nama; pengecualian S-12); cleanup hanya menghapus unit yang dibuat spec ini. Last Updated Population = hari uji: unit Population yang tercatat dibuat sebelum hari uji dihapus dan dibuat ulang lewat API di hook `before` supaya filter "hari ini" bermakna; jam server dan jam browser sinkron.
- Data milik spec: `Kilogram Force {runId}-045` / `kg`, dibuat lewat API sebelum TC-GS-UOM-167 (dipakai sebagai precondition Expected TC-GS-UOM-167) dan dihapus lewat API sesudahnya; hook `after` menghapusnya bila masih ada. Klien HTTP/API disediakan tim FE.
- Rentang "01 Jan 2020 – hari ini" mengasumsikan Last Updated seluruh unit Pre-setup berada pada atau setelah 01 Jan 2020.
- Date Format dan Time Format General Settings memakai nilai default environment (`dd/MM/yy` dan `HH:mm`); spec ini tidak mengubah General Settings.
- State global yang dipulihkan: Search, Filter, dan visibilitas kolom tabel Measurement dikembalikan ke default (semua kolom tampil) di hook `after`.
- Hook `beforeEach`: buka Global Settings > Master Reference > Measurement.
- Kemampuan teknis (kelas binary buffer, prinsip 13f): menangkap berkas unduhan browser (event download) ke direktori bersih per unduhan supaya nama berkas yang sama tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV dan XLSX (nama kolom, jumlah baris data tanpa header, nilai sel). Berkas unduhan dihapus di hook `after`. Pengisian date range picker Last Updated dan Column Visibility lewat header kolom Actions (`⋯`).

## Test Steps

### TC-GS-UOM-165: Screening menu Download tabel Measurement

1. Klik Download
2. Verifikasi popover berisi `Download CSV` dan `Download XLSX`

### TC-GS-UOM-166: Download tanpa Search dan Filter mengekspor seluruh baris

3. Klik `Download XLSX` pada popover yang terbuka
4. Verifikasi tidak ada toast sukses
5. Verifikasi file `Measurement.xlsx` terunduh berisi 20 baris data (bukan hanya halaman 1)

### TC-GS-UOM-170: Isi file ekspor: kolom dan format tanggal General Settings

6. Buka isi file `Measurement.xlsx` yang diunduh pada langkah 5
7. Verifikasi kolom file: `Unit Name`, `Symbol`, `Used By (Items)`, `Last Updated`
8. Verifikasi kolom `Used By (Items)` berisi angka (Kilogram `1`, Box `4`, Liter `0`)
9. Verifikasi tidak ada kolom `Item Type`
10. Verifikasi kolom `Last Updated` memakai Date Format dan Time Format General Settings yang berlaku

### TC-GS-UOM-386: Download CSV dan XLSX memuat angka Used By (Items)

11. Klik Download, lalu klik `Download CSV`
12. Verifikasi file `Measurement.csv` terunduh
13. Verifikasi kolom `Used By (Items)` pada `Measurement.csv` berisi angka (Box `4`, Liter `0`), bukan teks link atau `—`
14. Verifikasi kolom `Used By (Items)` pada `Measurement.xlsx` (unduhan langkah 5) berisi angka (Box `4`, Liter `0`), bukan teks link atau `—`
15. Klik Filter, isi Used By (Items) Min `2`
16. Klik [Apply]
17. Klik Download, lalu klik `Download CSV`
18. Verifikasi file `Measurement.csv` hasil filter terunduh dan hanya berisi Dozen, Pieces, dan Box
19. Verifikasi kolom `Used By (Items)` pada file hasil filter bernilai Dozen `2`, Pieces `3`, Box `4`
20. Klik [Clear Field], klik [Apply]

### TC-GS-UOM-167: Download dengan Search dan Filter aktif hanya mengekspor baris yang cocok

21. Buat unit `Kilogram Force {runId}-045` dengan Symbol `kg` lewat API
22. Ketik Search `kilo`, tekan Enter
23. Isi Last Updated rentang 01 Jan 2020 – hari ini
24. Klik [Apply]
25. Klik Download, lalu klik `Download CSV`
26. Verifikasi file `Measurement.csv` (extension mengikuti pilihan CSV) hanya berisi baris Kilogram dan `Kilogram Force {runId}-045`
27. Hapus unit `Kilogram Force {runId}-045` lewat API

### TC-GS-UOM-168: Download hanya mengekspor kolom yang visible

28. Klik `(←)` pada kotak Search
29. Klik [Clear Field], klik [Apply]
30. Klik header kolom Actions (`⋯`), uncheck `Symbol`
31. Klik Download, lalu klik `Download CSV`
32. Verifikasi file CSV pertama memuat kolom `Unit Name`
33. Verifikasi file CSV pertama tidak memuat kolom `Symbol`
34. Klik header kolom Actions (`⋯`), check kembali `Symbol`
35. Klik Download, lalu klik `Download CSV`
36. Verifikasi file CSV kedua memuat kolom `Symbol`

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 165, 166, 170, 386, 167, 168 (urutan sumber 165, 166, 167, 168, 170, 386). TC yang membaca seluruh data tanpa Search/Filter lebih dulu, lalu Search/Filter, lalu Column Visibility di akhir.
- TC-GS-UOM-170 membaca berkas `Measurement.xlsx` yang sama dengan unduhan TC-GS-UOM-166 (langkah 5) tanpa unduh ulang: state tabel keduanya identik (tanpa Search/Filter, semua kolom, 20 baris), sehingga langkah "Download XLSX" TC-GS-UOM-170 dan langkah 2 TC-GS-UOM-386 (XLSX) terpenuhi oleh unduhan itu. TC-GS-UOM-386 langkah 1 (CSV) dan langkah 3 (CSV hasil filter) diunduh sendiri.
- Berkas `Measurement.csv` hasil filter (TC-GS-UOM-386) dan hasil Search+Filter (TC-GS-UOM-167) ditangkap ke direktori unduhan bersih masing-masing.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 20 (mengosongkan filter Used By (Items) sebelum TC berikutnya; panel Filter tetap terbuka sesudah `[Apply]`, sehingga langkah berikutnya tidak membuka panel lagi); langkah 27 (menghapus Kilogram Force agar baseline 20 unit tidak berubah bagi TC berikutnya); langkah "Klik `(←)`..." dan "Klik [Clear Field], klik [Apply]" pada TC-GS-UOM-168 membersihkan Search dan Filter dari TC-GS-UOM-167; langkah terakhir yang me-check `Symbol` memulihkan kolom (hook `after` sebagai cadangan).
- Jumlah baris "20" dihitung dari baris data berkas tanpa baris header.
- Langkah 32 adalah `Verifikasi` pembanding (butir 2 bagian 8b), bukan dari Expected TC: berkas CSV pertama terbukti terunduh dan terbaca sebelum asersi kolom `Symbol` tidak ada pada langkah 33.
- Spec ini melewati sekitar 35 langkah (36 langkah). Alasan: seluruh TC membaca satu tabel Measurement dengan satu kelas harness (binary buffer, prinsip 13f) dan satu pembukaan layar; satu langkah di atas ambang berasal dari `Verifikasi` pembanding langkah 32. TC-GS-UOM-170 dan TC-GS-UOM-386 memakai ulang berkas unduhan TC-GS-UOM-166 (lihat butir di atas) sehingga tidak berdiri sendiri; memisahkannya hanya menambah seeding Population dan hook ganda.
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-UOM-167: Expected menyebut `Kilogram Force` (D-07, dibuat TC-GS-UOM-53) tetapi Dependensi dan Precondition tidak mencantumkannya. Spec membuat `Kilogram Force {runId}-045` lewat API dan memakai nama bersuffix.
  - TC-GS-UOM-166, 170, 386: label header dan format sel tanggal berkas ekspor diasersi mengikuti TC (nama kolom `Unit Name`, `Symbol`, `Used By (Items)`, `Last Updated`; Date/Time Format General Settings), tetapi `tc-measurement-backend.md` menyatakan label header dan format sel tanggal berkas ekspor tidak diasersi di BE (BEGAP-410); pemilik label header berkas perlu dikonfirmasi QA.
  - TC-GS-UOM-170: Expected butir b tidak menyebut format konkret; spec mengasersi kesesuaian dengan Date/Time Format General Settings yang berlaku (default environment `dd/MM/yy` dan `HH:mm`).
  - TC-GS-UOM-166: nama berkas `Measurement.xlsx` ditulis di Expected sebagai "nama file `Measurement` dan extension mengikuti pilihan XLSX"; spec mengasersi nama persis `Measurement.xlsx`.

---
id: TC-FA-TDC-E2E-158-pagination-halaman-terakhir-dan-state-tabel-dipertahankan-atau-direset
title: "Pagination: State Tabel Dipertahankan atau Direset dan Halaman Terakhir Sesudah Delete"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-559
  - TC-FA-TDC-560
  - TC-FA-TDC-561
  - TC-FA-TDC-562
  - TC-FA-TDC-931
coverage:
  web: automated
---

# Pagination: State Tabel Dipertahankan atau Direset dan Halaman Terakhir Sesudah Delete

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Asset Type BLD-NP dan BLD-P `Building`, LAND `Land`, class lain `Non-building`.
- Data Dinamis (milik spec, dibuat di hook `before` lewat seeding API, idempotent, dihapus di `after`): 17 class Active tambahan `TDC-01` sampai `TDC-17` (Asset Type `Building`, Allowed Methods `Straight Line`, Class Name `Kelas uji 01` sampai `Kelas uji 17`), sehingga tabel berisi 26 class dengan urutan default Class Code A-Z (9 class Example Data lalu TDC-01 sampai TDC-17). Untuk TC-FA-TDC-559 tabel berisi 21 class (TDC-01 sampai TDC-12) sehingga halaman 3 hanya berisi TDC-12; TDC-13 sampai TDC-17 dihapus lewat seeding API pada langkah 40. TDC-12 Used By `0` dan tanpa Last Posted Tax Year sehingga lolos kedua guard hapus. Kode class memakai literal TC tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (lihat Temuan untuk QA). Page size awal adalah 10 baris per halaman (default).
- Data uji (literal TC): keyword Search `TDC`; Filter Asset Type `Building`; sort Class Name Descending; halaman 2.
- Kemampuan teknis: seeding dan penghapusan class lewat API (`suite.md`); muat ulang halaman (F5); menu sidebar `Accounting` dan tab `Asset Class`.
- State global yang diubah: Search, Filter, Sort, dan nomor halaman pada tabel (dilepas oleh langkah di spec dan oleh `beforeEach` suite); TDC-12 dihapus oleh aksi TC-FA-TDC-559 dan TDC-01 sampai TDC-11 dihapus hook `after`.

## Test Steps

### Membangun state tabel (dipakai TC-FA-TDC-560 dan 561)

1. Ketik Search `TDC`, tekan Enter
2. Klik icon Filter
3. Pilih Asset Type `Building`
4. Klik `[Apply]`
5. Klik header Class Name dua kali (Descending)
6. Pindah ke halaman 2

### State tabel dipertahankan setelah Drawer ditutup (TC-FA-TDC-560)

7. Klik Class Code pada salah satu baris untuk membuka Drawer
8. Tutup Drawer dengan ikon `✕`
9. Verifikasi keyword Search `TDC` tetap sama
10. Verifikasi chip filter Asset Type `Building` tetap sama
11. Verifikasi sort Class Name Descending tetap sama
12. Verifikasi halaman 2 tetap sama

### State tabel dipertahankan setelah refresh manual (TC-FA-TDC-561)

13. Tekan F5 pada tab browser yang sama
14. Verifikasi keyword Search `TDC` tetap sama setelah refresh
15. Verifikasi filter Asset Type `Building` tetap sama setelah refresh
16. Verifikasi sort Class Name Descending tetap sama setelah refresh
17. Verifikasi halaman 2 tetap sama setelah refresh
18. Verifikasi jumlah baris per halaman tetap sama setelah refresh

### Klik ulang menu Accounting mereset state tabel (TC-FA-TDC-562)

19. Klik menu sidebar `Accounting`
20. Klik tab `Tax Depreciation Class`
21. Verifikasi halaman 1 dengan 10 baris
22. Verifikasi Search kosong
23. Verifikasi tidak ada chip filter
24. Verifikasi sort kembali default Class Code A-Z

### State dipertahankan saat berpindah ke tab Accounting lain lalu kembali (TC-FA-TDC-931)

25. Ketik Search `TDC`, tekan Enter
26. Klik icon Filter
27. Pilih Asset Type `Building`
28. Klik `[Apply]`
29. Klik header Class Name dua kali (Descending)
30. Pindah ke halaman 2
31. Klik tab `Asset Class`
32. Klik tab `Tax Depreciation Class`
33. Verifikasi keyword Search `TDC` tetap sama
34. Verifikasi chip filter Asset Type `Building` tetap sama
35. Verifikasi sort Class Name Descending tetap sama
36. Verifikasi halaman 2 tetap sama

### Menghapus baris terakhir di halaman terakhir (TC-FA-TDC-559)

37. Klik `Clear all` pada chip filter
38. Klik `(←)` pada kotak Search
39. Klik header Class Name satu kali (sort kembali netral)
40. Hapus class TDC-13 sampai TDC-17 lewat seeding API hingga tabel berisi 21 class, lalu muat ulang halaman
41. Pindah ke halaman 3
42. Klik `⋯` pada baris TDC-12, lalu `Delete`
43. Verifikasi dialog `Delete Tax Depreciation Class` tampil
44. Klik `[Delete]` pada dialog
45. Verifikasi toast sukses `Success, tax depreciation class has been deleted.`
46. Verifikasi halaman 3 menjadi kosong sehingga tabel pindah ke halaman 2 (halaman terakhir yang masih ada)
47. Verifikasi halaman 2 menampilkan 10 baris

## Notes

- Urutan TC dalam spec: TC-FA-TDC-560, 561, 562, 931, 559. TC-FA-TDC-559 terakhir karena menghapus data (S-10) dan butuh tabel 21 class. Keadaan hasil langkah 1 sampai 6 dipakai ulang oleh TC-FA-TDC-561 karena TC-FA-TDC-561 memulai dari keadaan yang sama persis (Search `TDC`, Filter `Building`, sort Class Name Descending, halaman 2) dan TC-FA-TDC-560 hanya membuka lalu menutup Drawer tanpa mengubahnya; keadaan dibangun ulang pada langkah 25 sampai 30 untuk TC-FA-TDC-931 karena TC-FA-TDC-562 mereset state.
- Langkah penghubung (S-03, S-09): langkah 37 sampai 39 (melepas Filter, Search, dan Sort sebelum TC-FA-TDC-559), langkah 40 (menghapus TDC-13 sampai TDC-17 lewat seeding API). Langkah 42 menargetkan baris TDC-12 tanpa Search karena halaman 3 hanya berisi satu baris (TDC-12) dan Search akan mengubah halaman (8b.13, R-23; Search bukan langkah penghubung di sini).
- Asersi absence langkah 23 (tidak ada chip filter) didahului anchor positif langkah 21 (halaman 1 dengan 10 baris tampil pada tabel yang sama; 8b.2).
- Spec ini 47 langkah, di atas ~35 langkah. Alasan: satu topik (state tabel utama dan pagination) pada dataset 26 class yang sama, tiap blok TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan S-01 mengharuskan satu `Verifikasi` per klausa; keadaan Search, Filter, Sort, dan halaman hanya dibangun dua kali (bukan lima).
- Temuan untuk QA:
  - Class Code maksimal 15 karakter: suffix `{runId}-<NNN>` (S-12) tidak muat, jadi kode `TDC-01` sampai `TDC-17` memakai literal TC dengan syarat seeding idempotent, cleanup oleh spec, dan suite serial. Kode yang sama dipakai spec 146, 152, dan 157; Lampiran A belum punya butir modul ini.
  - TC-FA-TDC-559 Expected a menyebut dialog `Delete Tax Depreciation Class` "dikonfirmasi" tanpa teks isi dialog; spec mengasersi judul dialog dan toast saja.
  - TC-FA-TDC-559 precondition (21 class) berbeda dari TC-FA-TDC-560 sampai 562 dan 931 (26 class); spec menyesuaikan tabel dengan seeding API pada langkah 40.
  - TC-FA-TDC-560 langkah 5 ("Klik Class Code pada salah satu baris") tidak menyebut baris tertentu; spec mengikuti TC.
  - Email akun Total Control tidak tertulis di TC.

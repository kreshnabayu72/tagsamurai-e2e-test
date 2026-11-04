---
id: TC-FA-TDC-E2E-146-kombinasi-search-filter-sort-dan-pagination-berlaku-bersamaan
title: "Kombinasi Search, Filter, Sort, dan Pagination Berlaku Bersamaan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-503
  - TC-FA-TDC-504
  - TC-FA-TDC-505
  - TC-FA-TDC-506
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, dan Pagination Berlaku Bersamaan

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Class Name yang memuat `Kelompok`: NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL (Asset Type `Non-building`); Allowed Methods `Declining Balance` pada NB-1, NB-2, NB-4, NB-KHS; Used By NB-1 `5`, NB-2 `3`, NB-SL `4`, NB-4, NB-KHS, dan NB-OLD `0`.
- Data Dinamis (milik spec, dibuat di hook `before` lewat seeding API, idempotent, dihapus di `after`): 17 class Active tambahan `TDC-01` sampai `TDC-17` (Asset Type `Building`, Allowed Methods `Straight Line`, Class Name `Kelas uji 01` sampai `Kelas uji 17`), sehingga tabel berisi 26 class dengan urutan default Class Code A-Z (9 class Example Data lalu TDC-01 sampai TDC-17). Kode class memakai literal TC tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (lihat Temuan untuk QA).
- Data uji (literal TC): keyword Search `Kelompok`; Filter Allowed Methods `Declining Balance`; Filter Asset Type `Non-building`; page size `25`.
- Kemampuan teknis: seeding class lewat API (`suite.md`).
- State global yang diubah: Search, Filter, Sort, dan page size pada tabel (dilepas oleh langkah di spec dan oleh `beforeEach` suite).

## Test Steps

### Kombinasi Search, Filter, Sort, dan Pagination (TC-FA-TDC-503)

1. Ketik Search `Kelompok`, tekan Enter
2. Klik icon Filter
3. Pilih Allowed Methods `Declining Balance`
4. Klik `[Apply]`
5. Klik header Used By dua kali
6. Verifikasi tabel menampilkan empat baris berurutan: NB-1 (5), NB-2 (3), lalu NB-4 dan NB-KHS (0, urut Class Code)
7. Verifikasi chip filter tetap aktif
8. Verifikasi keyword Search `Kelompok` tetap aktif
9. Ubah page size menjadi 25
10. Verifikasi page size 25
11. Verifikasi halaman 1
12. Verifikasi keempat baris tetap sama
13. Verifikasi Search tidak direset
14. Verifikasi Filter tidak direset
15. Verifikasi Sort tidak direset
16. Klik `(←)` pada kotak Search
17. Klik `Clear all` pada chip filter
18. Klik header Used By satu kali

### Clear Field pada Filter Panel tidak melepas Search dan Sort (TC-FA-TDC-504)

19. Ketik Search `Kelompok`, tekan Enter
20. Pilih Asset Type `Non-building`
21. Klik `[Apply]`
22. Klik header Used By satu kali
23. Klik `[Clear Field]`
24. Klik `[Apply]`
25. Verifikasi setelah Apply kosong chip filter hilang
26. Verifikasi keyword Search `Kelompok` tetap aktif
27. Verifikasi Used By tetap Ascending
28. Verifikasi tabel menampilkan NB-1 sampai NB-SL yang namanya memuat `Kelompok` (6 baris)
29. Verifikasi urutan baris menurut Used By naik
30. Klik `(←)` pada kotak Search
31. Klik header Used By dua kali

### Mengosongkan Search tidak melepas Filter dan Sort (TC-FA-TDC-505)

32. Ketik Search `Kelompok`, tekan Enter
33. Pilih Asset Type `Non-building`
34. Klik `[Apply]`
35. Klik header Used By satu kali
36. Klik icon `(✕)` pada input Search, tekan Enter pada input kosong
37. Verifikasi Filter Asset Type `Non-building` tetap aktif
38. Verifikasi Sort Used By Ascending tetap aktif
39. Verifikasi tabel menampilkan 6 class Non-building tanpa pembatasan keyword
40. Verifikasi urutan baris menurut Used By naik: NB-4, NB-KHS, NB-OLD, NB-2, NB-SL, NB-1
41. Klik `Clear all` pada chip filter
42. Klik header Used By dua kali

### Mengganti kolom Sort tidak mereset Search dan Filter (TC-FA-TDC-506)

43. Ketik Search `Kelompok`, tekan Enter
44. Pilih Asset Type `Non-building`
45. Klik `[Apply]`
46. Klik header Used By
47. Klik header Class Name
48. Verifikasi indikator sort Used By netral
49. Verifikasi Class Name Ascending
50. Verifikasi keyword Search `Kelompok` tetap aktif
51. Verifikasi chip filter Asset Type tetap aktif

## Notes

- Langkah penghubung (S-03, S-09): langkah 16 sampai 18, 30 dan 31, 41 dan 42 (melepas Search, Filter, dan Sort antar TC supaya tiap TC mulai dari tabel dengan sort netral dan tanpa Search atau Filter). Arah sort diasersi lewat urutan baris dan indikator pada langkah 6, 27, 29, 38, 40, dan 49, bukan di teks langkah klik.
- Filter Panel dibuka sekali pada langkah 2 dan tetap terbuka sesudah `[Apply]` sampai akhir spec (8b.9); langkah `[Clear Field]` dan "Pilih ..." pada blok TC-FA-TDC-504 (langkah 20 sampai 24), TC-FA-TDC-505 (langkah 33 dan 34), dan TC-FA-TDC-506 (langkah 44 dan 45) tidak didahului klik icon Filter (klik icon itu menutup panel).
- Kombinasi kontrol tabel dalam satu spec memakai dataset 26 class yang sama untuk keempat TC (pagination pada TC-FA-TDC-503 butuh lebih dari 10 baris). Page size 25 yang dipilih pada langkah 9 tidak dipulihkan karena tidak memengaruhi hasil TC berikutnya (hasil Search dan Filter di bawah 10 baris); `beforeEach` suite membuka ulang halaman.
- Spec ini 51 langkah, di atas ~35 langkah. Alasan: satu topik (kombinasi Search, Filter, Sort, Pagination tabel utama) pada dataset 26 class yang sama, tiap blok TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan S-01 mengharuskan satu `Verifikasi` per klausa.
- Temuan untuk QA:
  - Class Code maksimal 15 karakter: suffix `{runId}-<NNN>` (S-12) tidak muat, jadi kode `TDC-01` sampai `TDC-17` memakai literal TC dengan syarat seeding idempotent, cleanup oleh spec, dan suite serial. Kode yang sama dipakai spec 152, 157, dan 158 karena TC memakainya sebagai literal; Lampiran A belum punya butir modul ini.
  - TC-FA-TDC-503 langkah 2 tidak menyebut kriteria Filter dibuka lewat Filter Panel; spec menambah klik icon Filter.
  - TC-FA-TDC-505 langkah 4 menyebut "Klik icon (✕) lalu Enter pada input kosong" tanpa menyebut apakah kotak Search tetap terbuka; spec mengikuti TC.
  - Asumsi spec, belum dikonfirmasi FE: Filter Panel tetap terbuka sesudah `Clear all`, klik `(←)` pada kotak Search, dan klik header sort (langkah 17, 18, 30, 31, 41, 42), sehingga langkah 20, 33, dan 44 memilih Asset Type tanpa klik icon Filter; TC dan PRD tidak menyebutnya (sama dengan asumsi di spec 248). Perlu konfirmasi FE bersama keputusan spec 176.
  - Email akun Total Control tidak tertulis di TC.

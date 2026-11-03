---
id: TC-AC-LA-E2E-101-filter-list-chip-dropdown-clear-dan-tab-history
title: "Filter List: Chip, Search Dropdown, Clear Field, Kolom Disembunyikan, Reset Halaman, dan Tab History"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-298
  - TC-AC-LA-299
  - TC-AC-LA-300
  - TC-AC-LA-301
  - TC-AC-LA-302
  - TC-AC-LA-303
coverage:
  web: automated
---

# Filter List: Chip, Search Dropdown, Clear Field, Kolom Disembunyikan, Reset Halaman, dan Tab History

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada kedua tab, lebih dari 25 baris di tab Current; Client `PT Sejahtera`, `Klinik Medika Jaya`, `Toko Serba Ada`, `CV Mitra Sejati`, `PT Abadi Jaya`, `Bengkel Cahaya Motor`, `Klinik Harapan Bunda`; Product `FAMS` pada lebih dari 10 baris tab Current; License Type `Concurrent User` pada tab History) bersifat baca-saja untuk spec ini.
- Kemampuan teknis: spec menyembunyikan kolom `Client` lewat overlay Column Visibility (langkah 37 dan 44 memulihkannya). Hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE (konvensi bagian 4).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-298: Chip opsi terpilih

1. Klik ikon Filter
2. Buka dropdown Client
3. Centang `PT Sejahtera` dan `Klinik Medika Jaya`
4. Verifikasi tiap opsi terpilih menjadi chip di dalam field Client
5. Klik `(✕)` pada chip `PT Sejahtera`
6. Verifikasi chip `PT Sejahtera` hilang
7. Buka dropdown Client
8. Verifikasi opsi `PT Sejahtera` ter-uncheck di dropdown
9. Verifikasi chip `Klinik Medika Jaya` tetap tampil
10. Hapus centang `Klinik Medika Jaya` di dropdown
11. Verifikasi chip `Klinik Medika Jaya` hilang
12. Centang seluruh opsi Client hingga melebihi lebar field
13. Verifikasi chip berlebih diringkas menjadi chip `+N more`

### TC-AC-LA-299: Pencarian di dalam dropdown filter

14. Ketik `sejah` di kotak cari dropdown Client
15. Verifikasi daftar opsi menyempit ke yang mengandung `sejah` tanpa membedakan huruf besar kecil
16. Ganti isi kotak cari dropdown Client dengan `zzzz`
17. Verifikasi teks `No results found` tampil

### TC-AC-LA-300: Tutup panel tanpa Apply dan Clear Field

18. Klik menu `License Allocation` di sidebar
19. Terapkan filter Client `PT Sejahtera`
20. Verifikasi ikon Filter menampilkan titik indikator
21. Klik ikon Filter
22. Ubah pilihan Client menjadi `Klinik Medika Jaya` tanpa Apply
23. Klik ikon Filter untuk menutup panel
24. Klik ikon Filter untuk membuka panel lagi
25. Verifikasi panel menampilkan nilai ter-Apply terakhir `PT Sejahtera`
26. Verifikasi draft `Klinik Medika Jaya` dibuang
27. Klik `[Clear Field]` lalu `[Apply]`
28. Klik ikon Filter
29. Verifikasi semua kriteria filter kosong
30. Klik ikon Filter
31. Verifikasi tabel pulih menampilkan baris tab Current
32. Verifikasi titik indikator pada ikon Filter hilang

### TC-AC-LA-301: Filter pada kolom yang disembunyikan

33. Klik menu `License Allocation` di sidebar
34. Terapkan filter Client `PT Sejahtera`
35. Catat isi halaman pertama hasil filter
36. Klik `⋯` pada header kolom Actions
37. Hapus centang `Client` pada overlay Column Visibility
38. Tekan `Esc` untuk menutup overlay
39. Klik ikon Filter
40. Verifikasi field Client tetap ada di Filter Panel
41. Verifikasi filter ter-Apply tetap menyaring tabel (isi halaman pertama sama dengan langkah 35)
42. Klik ikon Filter
43. Klik `⋯` pada header kolom Actions
44. Centang `Client` pada overlay Column Visibility
45. Tekan `Esc` untuk menutup overlay

### TC-AC-LA-302: Apply mengembalikan paginasi ke halaman 1

46. Klik menu `License Allocation` di sidebar
47. Pindah ke halaman 2 dengan 10 data per halaman
48. Terapkan filter Product `FAMS`
49. Verifikasi tabel kembali ke halaman 1

### TC-AC-LA-303: Filter pada tab History

50. Klik tab `History`
51. Terapkan filter License Type `Concurrent User`
52. Verifikasi sedikitnya satu baris tampil
53. Verifikasi setiap baris hasil ber-License Type `Concurrent User` dan berstatus milik tab History
54. Klik ikon Filter
55. Buka dropdown Status
56. Verifikasi opsi Status memuat status tab History (`Expired`, `Rejected`, `Canceled`)

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah `Terapkan filter <Field> <opsi>` berarti: klik ikon Filter, buka dropdown Field, centang opsi, klik `[Apply]`.
- Langkah penghubung (S-03): langkah 18, 33, 46 (klik menu sidebar mereset Search, Sort, Filter, dan paginasi), langkah 23, 24, 28, 30, 42 (membuka dan menutup panel), langkah 35 (baseline), langkah 38 dan 45 (menutup overlay), langkah 54 (membuka panel).
- Alasan spec melewati sekitar 35 langkah: semua blok satu kelas harness (fungsional) dan satu dataset baca-saja (#54); tiap blok berdiri sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-LA-298 menyebut "dua opsi Client" tanpa nama; spec memakai `PT Sejahtera` dan `Klinik Medika Jaya` (nama dari TC-AC-LA-300).
  - TC-AC-LA-301 Expected a ("filter ter-Apply tetap menyaring tabel") tidak dapat dibaca dari kolom Client yang tersembunyi; spec membandingkan isi halaman pertama dengan hasil filter yang dicatat sebelum kolom disembunyikan.
  - TC-AC-LA-302 membutuhkan halaman 2 pada tab Current tanpa filter (lebih dari 10 baris), dipenuhi seed #54.
  - TC-AC-LA-303 tidak menyebut cara membuktikan "hanya baris tab History yang disaring"; spec memakai status milik tab History sebagai pembeda.

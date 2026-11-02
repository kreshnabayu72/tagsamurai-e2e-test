---
id: TC-FA-CAT-E2E-098-filter-tabel-utama-panel-range-total-asset-modified-by-dan-chip
title: "Filter Tabel Utama: Screening Panel, Range Total Asset, Modified By Multi-select, dan Sinkronisasi Chip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-332
  - TC-FA-CAT-333
  - TC-FA-CAT-334
  - TC-FA-CAT-335
  - TC-FA-CAT-336
  - TC-FA-CAT-337
coverage:
  web: automated
---

# Filter Tabel Utama: Screening Panel, Range Total Asset, Modified By Multi-select, dan Sinkronisasi Chip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMany (Pre-setup #24), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #24 (CatMany): 30 kategori L1 `Seed Cat 01` sampai `Seed Cat 30`; nilai Total Asset tersebar sehingga ada baris bernilai 5 dan 10 serta baris di luar rentang 5 sampai 10; Modified By tersebar pada `Alex B`, `Jane S`, `John D`, dan `System`. Spec hanya membaca data; tidak ada state yang diubah selain filter di layar, yang dibersihkan pada langkah penghubung.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-332: Screening Filter Panel, field, placeholder, urutan tombol, dan ikon aktif

1. Klik icon Filter
2. Verifikasi panel muncul di bawah toolbar
3. Verifikasi icon Filter menjadi gelap
4. Verifikasi field berurutan: `Total Asset`, `Modified By`, `Last Updated`
5. Verifikasi field `Total Asset` berupa Range dengan input berplaceholder `Min` dan `Max`
6. Verifikasi field `Modified By` berupa multi-select searchable berplaceholder `All users`
7. Verifikasi field `Last Updated` berupa date range picker berplaceholder `Select date`
8. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan

### TC-FA-CAT-333: Filter Total Asset (Range Min-Max) inklusif dan salah satu ujung boleh kosong

9. Isi Min `5` dan Max `10`, klik `[Apply]`
10. Verifikasi tabel memuat sedikitnya satu baris
11. Verifikasi seluruh baris bernilai Total Asset 5 sampai 10
12. Verifikasi baris bernilai Total Asset `5` dan `10` ikut tampil (inklusif di kedua ujung)
13. Kosongkan Max, klik `[Apply]`
14. Verifikasi seluruh baris bernilai Total Asset 5 atau lebih
15. Isi Max `10`, kosongkan Min, klik `[Apply]`
16. Verifikasi seluruh baris bernilai Total Asset 10 atau kurang

### TC-FA-CAT-334: Filter Modified By multi-select, logika OR dalam field dan opsi dari data tabel

17. Klik `[Clear Field]` dan `[Apply]`
18. Buka dropdown Modified By
19. Verifikasi opsi berisi Modified By distinct dari baris tabel (`Alex B`, `Jane S`, `John D`, `System`)
20. Verifikasi opsi berformat `[First Name] [Last Initial]`, dengan `System` bila ada
21. Centang `Jane S` dan `John D`, klik `[Apply]`
22. Verifikasi tabel memuat sedikitnya satu baris
23. Verifikasi seluruh baris bermodified by `Jane S` atau `John D` (OR dalam field)

### TC-FA-CAT-335: Dropdown Modified By memiliki pencarian internal dan state No results found

24. Klik `[Clear Field]` dan `[Apply]`
25. Buka dropdown Modified By
26. Ketik `jan` pada kotak cari dalam dropdown
27. Verifikasi opsi menyempit ke `Jane S`
28. Ganti isi kotak cari dalam dropdown dengan `zzz`
29. Verifikasi teks `No results found` tampil (tanpa ilustrasi)

### TC-FA-CAT-336: Chip Modified By, hapus lewat (✕) pada chip menyinkronkan checkbox

30. Kosongkan kotak cari dalam dropdown
31. Centang `Jane S` dan `John D`
32. Tutup dropdown
33. Klik (✕) pada chip `Jane S`
34. Verifikasi chip `Jane S` hilang
35. Verifikasi chip `John D` tetap ada
36. Buka dropdown Modified By
37. Verifikasi checkbox `Jane S` ter-uncheck
38. Klik `[Apply]`
39. Verifikasi tabel memuat sedikitnya satu baris
40. Verifikasi seluruh baris bermodified by `John D` (hasil tabel berubah mengikuti chip tersisa)

### TC-FA-CAT-337: Uncheck di dalam dropdown menyinkronkan chip (arah sebaliknya)

41. Buka dropdown Modified By
42. Centang `Jane S` dan `John D`
43. Uncheck `John D` dari dalam dropdown yang masih terbuka
44. Verifikasi chip `John D` hilang
45. Verifikasi chip `Jane S` tetap ada
46. Klik `[Clear Field]` dan `[Apply]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah (46 langkah nominal). Alasan: seluruh blok satu halaman (Filter Panel tabel utama) dan satu dataset (CatMany) yang sama; tiap blok berdiri sendiri dan didahului pembersihan filter (S-09), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC: TC-FA-CAT-332 (screening), TC-FA-CAT-333, TC-FA-CAT-334, TC-FA-CAT-335, TC-FA-CAT-336, TC-FA-CAT-337. Panel Filter tetap terbuka setelah `[Apply]` (dasar langkah 13 sampai 17 yang tidak membuka ulang panel).
- Spec 099 memuat TC-FA-CAT-338 sampai TC-FA-CAT-345 (Filter lanjutan).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 17, 24, 46 (membersihkan filter), 30, 32, 41, 42 (menyiapkan state dropdown), 18, 25, 36 (membuka dropdown).
- Temuan untuk QA:
  - TC-FA-CAT-336 Expected c ("hasil tabel berubah setelah `[Apply]` ulang") tidak menyebut `[Apply]` pertama; spec menekan `[Apply]` sekali setelah chip `Jane S` dihapus dan mengasersi hanya baris `John D`.
  - TC-FA-CAT-337 tidak menyebut keadaan filter awal; spec membersihkan filter pada langkah 46 TC sebelumnya dan mencentang ulang kedua opsi pada langkah 42.
  - TC-FA-CAT-333 tidak menyebut nilai Total Asset seed; spec mengasersi inklusivitas terhadap baris bernilai `5` dan `10` dari seed Pre-setup #24.

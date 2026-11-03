---
id: TC-FA-CAT-E2E-099-filter-tabel-utama-last-updated-draft-badge-independen-kolom-dan-opsi-dinamis
title: "Filter Tabel Utama: Chip +N more, Last Updated, Logika AND, Draft Dibuang, Badge, Independen Kolom, Reset Paginasi, dan Opsi Dinamis"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-338
  - TC-FA-CAT-339
  - TC-FA-CAT-340
  - TC-FA-CAT-341
  - TC-FA-CAT-342
  - TC-FA-CAT-343
  - TC-FA-CAT-345
  - TC-FA-CAT-344
coverage:
  web: automated
---

# Filter Tabel Utama: Chip +N more, Last Updated, Logika AND, Draft Dibuang, Badge, Independen Kolom, Reset Paginasi, dan Opsi Dinamis

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMany (Pre-setup #24), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua (Sesi B pada TC-FA-CAT-344): Total Control Kedua (Pre-setup #46, akun disediakan tim FE) lewat sesi API (butir hook suite di `suite.md`), hanya sebagai pemicu perubahan data pada langkah 52; tidak ada sesi UI kedua.
- Data Pre-setup #24 (CatMany): 30 kategori L1 `Seed Cat 01` sampai `Seed Cat 30` (3 halaman pada 10 baris per halaman; N total = 30 dari seeding); nilai Total Asset tersebar dengan sedikitnya satu baris bernilai 5 atau lebih dan baris bernilai di bawah 5; Modified By tersebar pada `Alex B`, `Jane S`, `John D`, dan `System`; Last Updated tersebar pada lebih dari satu tanggal.
- State yang diubah spec: TC-FA-CAT-344 mengubah Modified By seluruh kategori milik `John D` pada seed Pre-setup #24 (langkah 52). Pemulihan seed lewat fixture backend yang disediakan tim FE/BE pada langkah 61 dan di hook `after`. Konfigurasi Setup Column (kolom Total Asset) disembunyikan dan ditampilkan kembali pada langkah 35 dan 40; hook `after` menghapus preferensi kolom di browser (butir hook suite di `suite.md`; kemampuan disediakan tim FE). Suite berjalan serial (`parallel: false`).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-338: Banyak chip Modified By diringkas menjadi chip +N more

1. Klik icon Filter
2. Buka dropdown Modified By
3. Centang seluruh opsi hingga melebihi lebar field
4. Verifikasi chip ditampilkan sebanyak yang muat dan sisanya diringkas dalam satu chip `+N more` (N = jumlah chip tersembunyi)
5. Verifikasi field tidak melebar keluar panel
6. Tutup dropdown, klik `[Clear Field]` dan `[Apply]`

### TC-FA-CAT-339: Filter Last Updated (date range) inklusif

7. Catat nilai Last Updated baris-baris pada halaman 1 tabel
8. Pilih rentang tanggal pada field Last Updated yang mencakup sebagian baris, klik `[Apply]`
9. Verifikasi tabel memuat sedikitnya satu baris
10. Verifikasi seluruh baris memiliki Last Updated di dalam rentang (inklusif di kedua tanggal)
11. Pilih rentang satu hari (Start sama dengan End) pada tanggal salah satu baris yang dicatat, klik `[Apply]`
12. Verifikasi baris yang diperbarui pada hari itu tampil
13. Klik `[Clear Field]` dan `[Apply]`

### TC-FA-CAT-340: Kombinasi filter beberapa field menggunakan logika AND

14. Isi Min `5` pada Total Asset dan pilih Modified By `Jane S`, klik `[Apply]`
15. Verifikasi tabel memuat sedikitnya satu baris
16. Verifikasi seluruh baris bernilai Total Asset 5 atau lebih DAN Modified By `Jane S`
17. Klik `[Clear Field]` dan `[Apply]`

### TC-FA-CAT-341: Menutup panel Filter tanpa Apply membuang draft

18. Centang `Jane S` pada dropdown Modified By, klik `[Apply]`
19. Catat jumlah baris hasil (baseline H)
20. Ubah Min menjadi `3` tanpa menekan `[Apply]`
21. Klik area di luar panel
22. Buka Filter lagi
23. Verifikasi panel menampilkan nilai ter-Apply terakhir (`Jane S`, Min kosong), bukan draft `3`
24. Verifikasi jumlah baris tabel sama dengan H (tabel tidak berubah)
25. Klik `[Clear Field]` dan `[Apply]`

### TC-FA-CAT-342: Badge titik pada icon Filter muncul saat ada filter ter-Apply dan hilang saat di-clear

26. Verifikasi titik indikator tidak ada pada icon Filter (tanpa filter ter-Apply)
27. Centang `Jane S` pada dropdown Modified By, klik `[Apply]`
28. Verifikasi titik indikator muncul pada icon Filter saat panel terbuka
29. Tutup panel
30. Verifikasi titik indikator tetap tampil pada icon Filter saat panel tertutup
31. Buka panel, klik `[Clear Field]` dan `[Apply]`
32. Verifikasi titik indikator hilang dari icon Filter

### TC-FA-CAT-343: Filter independen dari visibilitas kolom

33. Isi Min `5` pada Total Asset, klik `[Apply]`
34. Catat jumlah total baris hasil (baseline H2)
35. Buka Setup Column, hilangkan centang kolom Total Asset, lalu Save
36. Buka Filter Panel
37. Verifikasi field `Total Asset` tetap ada pada Filter Panel
38. Verifikasi nilai Min `5` tetap ter-Apply
39. Verifikasi jumlah total baris sama dengan H2 (filter tetap menyaring tabel walau kolom disembunyikan)
40. Buka Setup Column, munculkan kembali kolom Total Asset, lalu Save
41. Klik `[Clear Field]` dan `[Apply]`

### TC-FA-CAT-345: Apply Filter dan Search saat berada di halaman 2 mereset paginasi ke halaman 1

42. Pindah ke halaman 2
43. Isi Min `0` pada Total Asset, klik `[Apply]`
44. Verifikasi tabel kembali ke halaman 1
45. Pindah ke halaman 2 lagi
46. Ketik Search `Seed`, tekan Enter
47. Verifikasi tabel kembali ke halaman 1
48. Klik icon panah (←) di kiri toolbar
49. Klik `[Clear Field]` dan `[Apply]`

### TC-FA-CAT-344: Opsi filter dinamis dari data tabel, opsi baru muncul dan nilai stale dibersihkan tanpa error

50. Centang `John D` pada dropdown Modified By, klik `[Apply]`
51. Verifikasi tabel memuat sedikitnya satu baris bermodified by `John D`
52. Total Control Kedua (Sesi B, sesi API) mengubah seluruh kategori milik `John D` hingga tersimpan sehingga Modified By-nya berganti
53. Tunggu aksi selesai
54. Buka ulang dropdown Modified By
55. Verifikasi opsi `Jane S` tampil pada dropdown
56. Verifikasi opsi `John D` tidak lagi muncul (hanya nilai yang ada di data tabel)
57. Klik `[Apply]` ulang
58. Verifikasi tidak ada pesan error yang tampil
59. Verifikasi hasil tabel mengikuti kriteria tersisa tanpa `John D` (tabel memuat seluruh data, jumlah total baris 30)
60. Klik `[Clear Field]` dan `[Apply]`
61. Pulihkan seed Pre-setup #24 lewat fixture dan muat ulang halaman Categories

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah (61 langkah nominal). Alasan: seluruh blok satu halaman (Filter Panel tabel utama) dan satu dataset (CatMany) yang sama; tiap blok berdiri sendiri dan didahului pembersihan filter (S-09), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-FA-CAT-344 yang mengubah data seed diletakkan terakhir (S-10).
- Spec 098 memuat TC-FA-CAT-332 sampai TC-FA-CAT-337 (Filter dasar).
- Sesi B pada TC-FA-CAT-344 memakai sesi API sehingga bukan konteks UI kedua (konvensi bagian 3, P-2 butir 2026-10-30); tidak ada butir `P-2`.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 6, 13, 17, 25, 41, 49, 60 (membersihkan filter), 7, 19, 34 (mencatat nilai atau baseline), 29 dan 36 (menutup atau membuka panel), 35 dan 40 (Setup Column), 53 (menunggu aksi selesai), 61 (pemulihan seed), 48 (menutup Search).
- Asersi tidak adanya opsi `John D` (langkah 56) memakai langkah 55 (opsi lain tampil pada dropdown yang sama) sebagai anchor positif (8b.2).
- Temuan untuk QA:
  - TC-FA-CAT-340 diberi petunjuk kelas multi-konteks di sumber, tetapi isinya kombinasi filter AND; spec memperlakukannya fungsional.
  - TC-FA-CAT-344 berlabel "Manual Only, dua sesi paralel" tetapi Sesi B hanya memicu perubahan data; spec memakai sesi API. TC tidak menyebut akun Sesi B; spec memakai Total Control Kedua (Pre-setup #46).
  - TC-FA-CAT-344 tidak menyebut kriteria tersisa setelah nilai stale dibersihkan; spec mengasersi tabel memuat seluruh data (30 baris).
  - TC-FA-CAT-339 tidak menyebut tanggal rentang; spec memakai tanggal Last Updated yang dicatat dari tabel seed (langkah 7).
  - TC-FA-CAT-341 menyebut Min `3` sebagai draft tanpa nilai ter-Apply awal untuk Min; spec mengasersi Min kosong sesuai Expected.

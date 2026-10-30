---
id: TC-AC-PP-E2E-035-filter-rentang-and-apply-clear-indikator
title: "Filter Panel: Rentang Tanggal, Logika AND, Apply, Clear Field, dan Indikator"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-112
  - TC-AC-PP-113
  - TC-AC-PP-114
  - TC-AC-PP-116
  - TC-AC-PP-117
  - TC-AC-PP-118
  - TC-AC-PP-119
coverage:
  web: automated
---

# Filter Panel: Rentang Tanggal, Logika AND, Apply, Clear Field, dan Indikator

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Andi Wijaya), password dari `Spectra.env.AC_TC_PASSWORD`. Login dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active `John Doe` 10 Aug 2026, Version 2 `John Doe` 02 Jul 2026, Version 1 `Jane Smith` 15 Jan 2026 akun sudah dihapus). Hook `before` men-seed lewat Fixture BE; hook `after` mengembalikan ke Riwayat A. Spec ini hanya membaca data.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (rentang tanggal pada langkah ditulis dalam format ini). Spec tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk membuat ulang dataset Riwayat A.
- State UI yang diubah spec dan dipulihkan: filter ter-Apply dikosongkan lewat `[Clear Field]` lalu `[Apply]` di antara TC; kolom `Published By` disembunyikan lalu ditampilkan kembali (TC-AC-PP-118; konfigurasi kolom tersimpan di cache browser); keyword Search `e` dikosongkan di akhir (TC-AC-PP-116). Hook `after` menampilkan kembali semua kolom sebagai cadangan.
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide; spec ini sendiri tidak mengubah data.
- Tidak ada fixture file yang dibutuhkan; halaman dibuka lewat menu Settings > Privacy Policy.

## Test Steps

### TC-AC-PP-112: Filter Published At dengan rentang tanggal bersifat inklusif di kedua ujung

1. Buka panel Filter
2. Pada field `Published At` pilih rentang 02 Jul 26 sampai 10 Aug 26
3. Klik `[Apply]`
4. Verifikasi tabel menampilkan `Version 3` (10 Aug 26) dan `Version 2` (02 Jul 26)
5. Verifikasi footer `1–2 of 2`
6. Verifikasi `Version 1` (15 Jan 26) tidak tampil
7. Verifikasi baris pada tanggal ujung akhir (10 Aug 26) termasuk dalam hasil
8. Verifikasi baris pada tanggal ujung awal (02 Jul 26) termasuk dalam hasil
9. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-PP-113: Filter Published At dengan satu hari saja (Start sama dengan End) menampilkan versi pada hari itu

10. Buka panel Filter
11. Pada field `Published At` pilih rentang 02 Jul 26 sampai 02 Jul 26
12. Klik `[Apply]`
13. Verifikasi tabel hanya menampilkan `Version 2` (02 Jul 26)
14. Verifikasi footer `1–1 of 1`
15. Verifikasi `Version 3` dan `Version 1` tidak tampil
16. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-PP-114: Kombinasi dua field filter berbeda memakai logika AND

17. Buka panel Filter
18. Pada field `Published By` centang `John Doe`
19. Pada field `Published At` pilih rentang 01 Aug 26 sampai 31 Aug 26
20. Klik `[Apply]`
21. Verifikasi tabel hanya menampilkan `Version 3` (10 Aug 26, `John D`)
22. Verifikasi footer `1–1 of 1`
23. Verifikasi `Version 2` (02 Jul 26, `John D`) tidak tampil karena di luar rentang
24. Verifikasi `Version 1` (`Jane S`) tidak tampil
25. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-PP-119: Filter tanpa hasil menampilkan empty state pencarian dan pulih setelah filter dilepas

26. Buka panel Filter
27. Pada field `Published At` pilih rentang 01 Jan 25 sampai 31 Jan 25
28. Klik `[Apply]`
29. Verifikasi body tabel menampilkan Title "No results found"
30. Verifikasi body tabel menampilkan Description "Try adjusting your search or filter."
31. Verifikasi toolbar dan table head tetap tampil
32. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`
33. Verifikasi 3 baris Riwayat A tampil kembali

### TC-AC-PP-117: Icon Filter menampilkan indikator titik selama ada filter ter-Apply dan hilang saat dilepas

34. Buka panel Filter
35. Pada field `Published By` centang `John Doe`
36. Klik `[Apply]`
37. Tutup panel Filter
38. Verifikasi icon Filter menampilkan badge titik tanpa angka walau panel tertutup
39. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`
40. Verifikasi badge titik pada icon Filter hilang

### TC-AC-PP-118: Filter ter-Apply tetap berlaku dan field filter tetap tersedia walau kolom disembunyikan

41. Buka panel Filter
42. Pada field `Published By` centang `John Doe`
43. Klik `[Apply]`
44. Klik header kolom Actions `(⋯)` untuk membuka overlay Column Visibility
45. Uncheck `Published By`
46. Tutup overlay
47. Verifikasi tabel tetap hanya menampilkan baris hasil Filter (`Version 3` dan `Version 2`)
48. Buka panel Filter
49. Verifikasi panel Filter masih memiliki field `Published By`
50. Verifikasi field `Published By` terisi chip `John Doe`
51. Klik header `(⋯)`, check kembali `Published By`, lalu tutup overlay
52. Klik `[Clear Field]` pada panel Filter, lalu klik `[Apply]`

### TC-AC-PP-116: Menutup Filter Panel tanpa Apply membuang draft dan Clear Field mengosongkan field tanpa menyentuh Search

53. Klik icon Search, ketik "e", tekan Enter
54. Buka panel Filter
55. Centang `John Doe` pada `Published By`
56. Klik ulang icon Filter untuk menutup panel (tanpa Apply)
57. Buka panel Filter lagi
58. Verifikasi field `Published By` kosong dengan placeholder "All users" (draft tanpa Apply dibuang)
59. Verifikasi tabel tetap menampilkan 3 baris hasil Search `e`
60. Verifikasi input Search tetap `e`
61. Centang `John Doe` pada `Published By`
62. Klik `[Apply]`
63. Verifikasi tabel menampilkan `Version 3` dan `Version 2`
64. Verifikasi input Search tetap `e`
65. Buka panel Filter dan klik `[Clear Field]`
66. Klik `[Apply]`
67. Verifikasi tabel kembali menampilkan 3 baris
68. Verifikasi input Search tetap `e`
69. Klik icon `(←)` untuk menutup search bar dan mereset keyword

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa awalan Verifikasi): langkah `[Clear Field]` lalu `[Apply]` di akhir tiap blok TC-AC-PP-112, 113, 114, 119, 117, dan 118 agar filter ter-Apply dibersihkan sebelum TC berikutnya; langkah menutup panel di blok TC-AC-PP-117; langkah menutup overlay Column Visibility di blok TC-AC-PP-118 (yang kedua juga memulihkan kolom `Published By`); langkah pemasangan Search `e` yang menjadi Precondition TC-AC-PP-116; langkah menutup search bar di akhir blok TC-AC-PP-116.
- Urutan TC di dalam spec: 112, 113, 114, 119, 117, 118, 116 (bukan urutan nomor). Alasan: TC-AC-PP-118 mengubah konfigurasi kolom dan TC-AC-PP-116 membutuhkan Search aktif, sehingga keduanya ditaruh di akhir; TC-AC-PP-119 (empty state) dimajukan di depan TC-AC-PP-117 agar semua asersi hasil tabel berurutan.
- Spec ini tidak membuat atau mengubah data.
- Ukuran spec melewati sekitar 35 langkah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tujuh blok TC memakai dataset Riwayat A yang hanya dibaca, satu topik (Filter Panel tabel Version History) dan satu kelas (fungsional), dan tiap blok diakhiri dengan membersihkan filter ter-Apply sehingga kegagalan satu blok tidak membuat blok lain tidak bermakna; spec tidak dipecah.
- Pembagian TC lintas spec: logika OR dua opsi dalam satu field (TC-AC-PP-111) ada di `TC-AC-PP-E2E-037`; screening panel dan dropdown (TC-AC-PP-106, 108-110) di `TC-AC-PP-E2E-034`; overflow chip (TC-AC-PP-201) di `TC-AC-PP-E2E-036`; irisan Search dan Filter pada dataset besar (TC-AC-PP-115) di `TC-AC-PP-E2E-042`.
- Temuan untuk QA:
  - TC-AC-PP-112 Expected c ("kedua tanggal ujung rentang termasuk (inklusif)") adalah kesimpulan dari Expected a; spec mengasersinya sebagai dua `Verifikasi` (ujung akhir dan ujung awal).
  - TC-AC-PP-116 langkah 2 menulis "Centang `John Doe`, klik `[Apply]`, lalu buka panel dan klik `[Clear Field]` → klik `[Apply]`" tanpa menyebut kondisi panel setelah Apply; spec membuka panel kembali sebelum `[Clear Field]`.
  - TC-AC-PP-116 Precondition menyebut Search `e` aktif tetapi tidak menyebut cara mengaktifkannya; spec mengaktifkannya lewat Search toolbar di awal blok TC-AC-PP-116.

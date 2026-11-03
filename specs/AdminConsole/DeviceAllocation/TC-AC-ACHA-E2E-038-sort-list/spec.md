---
id: TC-AC-ACHA-E2E-038-sort-list
title: "Sort pada List Device Allocation"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-315
  - TC-AC-ACHA-316
  - TC-AC-ACHA-317
  - TC-AC-ACHA-318
  - TC-AC-ACHA-319
  - TC-AC-ACHA-320
  - TC-AC-ACHA-321
  - TC-AC-ACHA-322
  - TC-AC-ACHA-323
  - TC-AC-ACHA-324
  - TC-AC-ACHA-325
coverage:
  web: automated
---

# Sort pada List Device Allocation

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #21) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (entitas PT ABC), password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor (lihat `suite.md`).
- Data Pre-setup: Seed 30 alokasi (Pre-setup #48, rincian Seed List) yang dilihat Total Control Principal sebagai seluruh 30 baris, Page size default 10 (tiga halaman). Nilai seed dirujuk lewat fixture `AdminConsoleDeviceAllocation`. Allocation ID, Allocated By, dan Last Updated seed bernilai literal dan diasersi (pengecualian S-12 nama literal, Lampiran A butir A-11: seeding idempotent, tidak diubah atau dihapus oleh spec ini, suite serial). Tidak ada Data Dinamis kecuali disebut di bawah.
- Data uji TC-AC-ACHA-316 (sort per kelas A, diulang per baris tabel; nilai Last Updated default Newest First):

  | Kolom | Ascending: dua baris teratas | Descending: dua baris teratas |
  |---|---|---|
  | Allocation ID | `HALC-20260901-00001`, `HALC-20260901-00002` | `HALC-20260909-00003`, `HALC-20260909-00002` |
  | Category | `HALC-20260908-00003`, `HALC-20260906-00003` | `HALC-20260907-00003`, `HALC-20260905-00001` |
  | From | `HALC-20260908-00001`, `HALC-20260907-00001` | `HALC-20260908-00004`, `HALC-20260906-00003` |
  | Client | `HALC-20260908-00004`, `HALC-20260906-00003` | `HALC-20260909-00003`, `HALC-20260909-00002` |
  | Status | `HALC-20260906-00004`, `HALC-20260904-00002` | `HALC-20260909-00002`, `HALC-20260908-00004` |
  | Payment | `HALC-20260908-00003`, `HALC-20260907-00002` | `HALC-20260909-00003`, `HALC-20260909-00002` |

- Data uji TC-AC-ACHA-317 (sort per kelas B dengan nilai kosong `—`, diulang per baris tabel):

  | Kolom | Ascending: dua baris teratas | Descending: dua baris teratas (nilai kosong) |
  |---|---|---|
  | Type | `HALC-20260906-00001`, `HALC-20260902-00003` | `HALC-20260909-00003`, `HALC-20260909-00001` |
  | Notes | `HALC-20260901-00001`, `HALC-20260902-00002` | `HALC-20260909-00003`, `HALC-20260909-00001` |
  | Paid From | `HALC-20260909-00003`, `HALC-20260909-00002` | `HALC-20260908-00003`, `HALC-20260907-00002` |

- Kemampuan teknis (disediakan tim FE): menampilkan atau menyembunyikan kolom lewat overlay Column Visibility (perubahan overlay langsung diterapkan tanpa Save); menghapus preferensi kolom di browser.
- State yang diubah: kolom Notes, Payment, Paid From, dan Cost ditampilkan di awal spec dan disembunyikan kembali di langkah pemulihan akhir; sort dikembalikan netral di akhir tiap TC.
- Preferensi kolom tabel (Setup Column) tersimpan di browser; hook `after` suite menghapusnya (kemampuan disediakan tim FE, didaftarkan di `suite.md`).
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### Persiapan kolom

1. Klik ikon `⋯` pada header kolom terakhir
2. Centang kolom Notes, Payment, Paid From, dan Cost di overlay Column Visibility
3. Tutup overlay Column Visibility

### TC-AC-ACHA-315: Siklus sort tiga tahap

4. Klik header kolom Client sekali
5. Verifikasi indikator sort Client ascending (`↑`)
6. Verifikasi baris teratas `HALC-20260908-00004`, `HALC-20260906-00003`
7. Klik header kolom Client lagi
8. Verifikasi indikator sort Client descending (`↓`)
9. Verifikasi baris teratas `HALC-20260909-00003`, `HALC-20260909-00002`
10. Klik header kolom Client untuk ketiga kalinya
11. Verifikasi indikator sort hilang (netral)
12. Verifikasi urutan kembali ke default Last Updated Newest First dengan baris teratas `HALC-20260909-00003`

### TC-AC-ACHA-316: Sort per kelas A, alfabetis tanpa nilai kosong

13. Untuk setiap baris tabel Data uji TC-AC-ACHA-316 (langkah 13 sampai 17): klik header kolom itu sekali (ascending)
14. Verifikasi dua baris teratas sesuai kolom "Ascending" baris tabel itu
15. Klik header kolom itu lagi (descending)
16. Verifikasi dua baris teratas sesuai kolom "Descending" baris tabel itu
17. Klik header kolom itu sekali lagi (netral)

### TC-AC-ACHA-317: Sort per kelas B, alfabetis dengan nilai kosong

18. Untuk setiap baris tabel Data uji TC-AC-ACHA-317 (langkah 18 sampai 26): klik header kolom itu sekali (ascending)
19. Verifikasi dua baris teratas sesuai kolom "Ascending" baris tabel itu (nilai terisi lebih dulu)
20. Ketik `3` pada input nomor halaman, tekan Enter
21. Verifikasi nilai kosong `—` berada di akhir daftar (baris terakhir halaman 3 bernilai `—` pada kolom itu)
22. Ketik `1` pada input nomor halaman, tekan Enter
23. Klik header kolom itu lagi (descending)
24. Verifikasi dua baris teratas sesuai kolom "Descending" baris tabel itu
25. Verifikasi nilai kosong `—` berada di awal daftar (kedua baris teratas bernilai `—` pada kolom itu)
26. Klik header kolom itu sekali lagi (netral)

### TC-AC-ACHA-318: Sort per kelas C, numerik natural Quantity

27. Klik header kolom Quantity sekali (ascending)
28. Verifikasi tiga baris teratas bernilai Quantity `1`, `3`, `5` (urutan numerik natural, bukan urutan teks `1, 10, 100`)
29. Klik header kolom Quantity lagi (descending)
30. Verifikasi tiga baris teratas bernilai Quantity `5,000`, `500`, `300`
31. Klik header kolom Quantity sekali lagi (netral)

### TC-AC-ACHA-319: Sort per kelas C2, numerik dengan nilai kosong Cost

32. Klik header kolom Cost sekali (ascending)
33. Verifikasi tiga baris teratas bernilai Cost `$1.20`, `$22.50`, `$66.00` (urutan numerik nilai asli)
34. Ketik `3` pada input nomor halaman, tekan Enter
35. Verifikasi lima baris dengan Cost `—` berada di akhir daftar (lima baris terakhir halaman 3)
36. Ketik `1` pada input nomor halaman, tekan Enter
37. Klik header kolom Cost lagi (descending)
38. Verifikasi lima baris Cost `—` berada di awal daftar (lima baris pertama halaman 1)
39. Verifikasi baris keenam bernilai Cost `$12,500.00`
40. Klik header kolom Cost sekali lagi (netral)

### TC-AC-ACHA-320: Sort per kelas D, tanggal Last Updated

41. Klik header kolom Last Updated sekali (ascending)
42. Verifikasi Oldest First: baris teratas `HALC-20260901-00001` (01/09/26 08:00)
43. Klik header kolom Last Updated lagi (descending)
44. Verifikasi Newest First: baris teratas `HALC-20260909-00003` (09/09/26 19:00)
45. Klik header kolom Last Updated sekali lagi (netral)
46. Verifikasi netral kembali ke default Newest First dengan baris teratas `HALC-20260909-00003`

### TC-AC-ACHA-321: Sort per kelas E, Allocated By berdasarkan nama lengkap

47. Klik header kolom Allocated By sekali (ascending)
48. Verifikasi tiga baris teratas dibuat oleh `Admin P` (`HALC-20260908-00003`, `HALC-20260907-00002`, `HALC-20260905-00001`), urutan berdasarkan nama lengkap dasar (Admin Pratama, Andi Wijaya, Budi Santoso, Hendra Wibowo, Siti Rahmawati), bukan teks tampilan singkat
49. Klik header kolom Allocated By lagi (descending)
50. Verifikasi tiga baris teratas dibuat oleh `Siti R` (`HALC-20260909-00002`, `HALC-20260908-00001`, `HALC-20260906-00004`)
51. Klik header kolom Allocated By sekali lagi (netral)

### TC-AC-ACHA-322: Berpindah kolom sort memulai siklus dari ascending

52. Klik header kolom Quantity sekali (ascending)
53. Klik header kolom Status sekali
54. Verifikasi indikator sort Quantity kembali netral
55. Verifikasi Status memulai siklus dari ascending (`↑`)
56. Verifikasi baris teratas `HALC-20260906-00004`, `HALC-20260904-00002`
57. Klik header kolom Status dua kali hingga netral

### TC-AC-ACHA-323: Tie-breaker dan determinisme urutan antar halaman

58. Klik header kolom Status sekali (ascending)
59. Catat ID baris halaman 1 berdasarkan urutan tampil
60. Verifikasi baris pertama kelompok `Completed` (tepat setelah tiga baris `Canceled`) adalah `HALC-20260909-00003`, urutan default Last Updated terbaru lebih dulu
61. Ketik `2` pada input nomor halaman, tekan Enter
62. Catat ID baris halaman 2 berdasarkan urutan tampil
63. Ketik `3` pada input nomor halaman, tekan Enter
64. Catat ID baris halaman 3 berdasarkan urutan tampil
65. Verifikasi 7 baris `Waiting for Approval` berurutan menurut Last Updated terbaru lebih dulu dengan tiga baris pertama `HALC-20260909-00002`, `HALC-20260908-00004`, `HALC-20260907-00001`
66. Ketik `1` pada input nomor halaman, tekan Enter
67. Verifikasi urutan baris halaman 1 sama dengan catatan awal
68. Verifikasi tidak ada baris ganda atau terlewat pada halaman 1 sampai 3 (30 Allocation ID berbeda)
69. Klik header kolom Status dua kali hingga netral

### TC-AC-ACHA-324: Guard kolom non-sortable

70. Amati header kolom Actions (`⋯`)
71. Verifikasi header kolom Actions tidak punya ikon sort
72. Klik header kolom Actions
73. Verifikasi klik pada header Actions hanya membuka overlay Column Visibility
74. Tutup overlay Column Visibility

### TC-AC-ACHA-325: Mengganti sort tidak mengubah nomor halaman

75. Ketik `2` pada input nomor halaman, tekan Enter
76. Catat baris teratas halaman 2
77. Klik header kolom Quantity sekali
78. Verifikasi tabel tetap berada di halaman 2
79. Verifikasi urutan dataset berubah (baris teratas halaman 2 berbeda dari catatan)
80. Klik header kolom Quantity dua kali hingga netral
81. Ketik `1` pada input nomor halaman, tekan Enter

### Pemulihan state

82. Klik ikon `⋯` pada header kolom terakhir
83. Hilangkan centang kolom Notes, Payment, Paid From, dan Cost di overlay Column Visibility
84. Tutup overlay Column Visibility

## Notes

- Sumber TC: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (bagian 4a-3). Seluruh TC primer spec ini (TC-AC-ACHA-315 sampai 325) dikerjakan di sini.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): persiapan dan pemulihan kolom lewat overlay Column Visibility; klik header kolom sampai netral di akhir tiap TC (S-09, berpindah kolom memulai siklus dari ascending menurut TC-AC-ACHA-322); pindah halaman lewat input nomor halaman; pencatatan ID baris (TC-AC-ACHA-323) dan baris teratas (TC-AC-ACHA-325). Perpindahan ke halaman 3 dan kembali ke halaman 1 pada TC-AC-ACHA-317 dan TC-AC-ACHA-319 adalah langkah menuju keadaan "di akhir daftar" (S-14).
- Langkah 13 sampai 17 berulang untuk setiap baris tabel Data uji TC-AC-ACHA-316 (enam iterasi) dan langkah 18 sampai 26 untuk Data uji TC-AC-ACHA-317 (tiga iterasi), bagian 8b butir 7. Langkah perulangan tidak bersyarat.
- Asersi tambahan (S-03): pada TC-AC-ACHA-323 kelompok `Completed` dibaca sebagai posisi sesudah tiga baris `Canceled` (Seed List memuat tepat tiga alokasi Canceled) dan tiga baris pertama kelompok `Waiting for Approval` memakai urutan default Last Updated dari TC-AC-ACHA-300; pada TC-AC-ACHA-325 "urutan dataset berubah" diamati sebagai baris teratas halaman 2 berbeda dari catatan sebelum sort.
- Spec memiliki 84 langkah nominal dan lebih banyak setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu topik (Sort List) pada dataset seed dan akun yang sama; tiap TC berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna); ekspansi berasal dari dua perulangan per kolom data tanpa langkah bersyarat.
- Pemisahan topik satu dataset (prinsip 1): Search, Filter Panel, Sort, Setup Column, kombinasi kontrol, dan Pagination List memakai dataset Seed List yang sama (Pre-setup #48) dan dipisah menjadi spec 036 sampai 041 karena gabungannya jauh melewati batas ukuran (spec Sort ini saja 84 langkah nominal, belum termasuk ekspansi perulangan). Pemisahan per kontrol dipertahankan karena tiap spec memulai dari kondisi default yang dipulihkan di akhir spec dan di hook `after` (sort netral), sehingga kegagalan keras satu spec tidak membuat spec lain kehilangan makna; di dalam spec ini tiap TC mengakhiri dengan pemulihan state (S-09) dan tidak bergantung pada hasil TC lain, sehingga spec tetap satu (tanpa pemisah nyata: akun, kelas harness, dan dataset sama).
- Temuan untuk QA:
  - TC-AC-ACHA-316, 317, dan 319 mensyaratkan kolom Notes, Payment, Paid From, dan Cost ditampilkan lewat Setup Column tanpa menyebut cara; spec memakai overlay Column Visibility.
  - TC-AC-ACHA-324 langkah 1 ("Amati header kolom Column Visibility `⋯`") tidak menyebut apa yang diamati; spec mengamati header kolom Actions dan Expected-nya.
  - TC-AC-ACHA-321 Expected menyebut urutan berdasarkan nama lengkap dasar, bukan teks tampilan singkat, tetapi tiga baris teratas hasil sort sama untuk kedua kriteria (`Admin P`); asersi nama lengkap tidak dapat dibedakan dari teks singkat pada data ini.
  - TC-AC-ACHA-317 tidak menyebut halaman tempat nilai kosong `—` diamati di akhir daftar; spec berpindah ke halaman 3 (halaman terakhir pada Page size default 10).

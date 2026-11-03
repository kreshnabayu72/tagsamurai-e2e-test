---
id: TC-AC-ACHA-E2E-036-search-list
title: "Search pada List Device Allocation"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-282
  - TC-AC-ACHA-283
  - TC-AC-ACHA-284
  - TC-AC-ACHA-285
  - TC-AC-ACHA-286
  - TC-AC-ACHA-287
  - TC-AC-ACHA-288
  - TC-AC-ACHA-289
  - TC-AC-ACHA-290
  - TC-AC-ACHA-291
  - TC-AC-ACHA-292
  - TC-AC-ACHA-293
  - TC-AC-ACHA-294
  - TC-AC-ACHA-295
  - TC-AC-ACHA-296
coverage:
  web: automated
---

# Search pada List Device Allocation

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #21) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (entitas PT ABC), password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor (lihat `suite.md`).
- Data Pre-setup: Seed 30 alokasi (Pre-setup #48, rincian Seed List) yang dilihat Total Control Principal sebagai seluruh 30 baris, Page size default 10 (tiga halaman). Nilai seed dirujuk lewat fixture `AdminConsoleDeviceAllocation`. Allocation ID, Allocated By, dan Last Updated seed bernilai literal dan diasersi (pengecualian S-12 nama literal, Lampiran A butir A-6: seeding idempotent, tidak diubah atau dihapus oleh spec ini, suite serial). Tidak ada Data Dinamis kecuali disebut di bawah.
- Data uji TC-AC-ACHA-288 (kata kunci per kolom, diulang per baris tabel):

  | Kolom | Kata kunci | Jumlah baris | Baris teratas |
  |---|---|---|---|
  | Allocation ID | `HALC-20260909-00003` | 1 | `HALC-20260909-00003` |
  | Type | `Long Range` | 2 | `HALC-20260906-00001`, `HALC-20260902-00003` |
  | From | `Nusa` | 3 | `HALC-20260908-00004`, `HALC-20260906-00003`, `HALC-20260903-00004` |
  | Client | `Retail` | 6 | `HALC-20260908-00001`, `HALC-20260907-00001`, `HALC-20260905-00003` |

- Kemampuan teknis (disediakan tim FE): menampilkan atau menyembunyikan kolom lewat overlay Column Visibility (perubahan overlay langsung diterapkan tanpa Save); menghapus preferensi kolom di browser.
- State yang diubah: kolom Notes, Payment, Paid From, dan Cost ditampilkan di TC-AC-ACHA-292 dan dikembalikan tersembunyi di langkah pemulihan akhir; visibilitas kolom Client diubah dan dipulihkan di TC-AC-ACHA-295.
- Preferensi kolom tabel (Setup Column) tersimpan di browser; hook `after` suite menghapusnya (kemampuan disediakan tim FE, didaftarkan di `suite.md`).
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHA-282: Reveal dan auto-focus Search toolbar

1. Arahkan kursor ke ikon Search
2. Verifikasi tooltip ikon Search `Search`
3. Klik ikon Search
4. Verifikasi Search bar melebar (reveal)
5. Verifikasi kursor otomatis fokus di input Search
6. Verifikasi placeholder `Search allocation ID, client name...` tampil
7. Verifikasi ikon Search berganti menjadi panah kembali `(←)` di kiri toolbar
8. Klik `(←)` pada kotak Search

### TC-AC-ACHA-283: Search dieksekusi saat Enter, bukan live

9. Klik ikon Search
10. Ketik `Retail` di input Search tanpa menekan Enter
11. Verifikasi ikon `(✕)` muncul di dalam input
12. Verifikasi tabel belum tersaring (pagination tetap tiga halaman, Search tidak live-as-you-type)
13. Tekan Enter
14. Verifikasi tabel tersaring menjadi 6 baris dengan baris teratas `HALC-20260908-00001`, `HALC-20260907-00001`, `HALC-20260905-00003`
15. Klik `(←)` pada kotak Search

### TC-AC-ACHA-284: Clear lewat ikon silang tidak langsung mereset tabel

16. Ketik Search `Retail`, tekan Enter
17. Klik ikon `(✕)` di dalam input
18. Verifikasi input Search kosong
19. Verifikasi search bar tetap terbuka dengan kursor fokus
20. Verifikasi tabel tetap menampilkan hasil `Retail` (6 baris, belum reset)
21. Tekan Enter pada input yang sudah kosong
22. Verifikasi tabel reset menampilkan 30 baris pada tiga halaman

### TC-AC-ACHA-285: Collapse Search lewat ikon panah

23. Ketik Search `Retail`, tekan Enter
24. Klik ikon `(←)` di kiri toolbar
25. Verifikasi kotak pencarian menutup menjadi ikon Search biasa
26. Verifikasi tabel langsung reset ke 30 baris tanpa menekan Enter
27. Klik ikon Search
28. Verifikasi input Search kosong (keyword dikosongkan)

### TC-AC-ACHA-286: Substring dan tidak case-sensitive

29. Ketik Search `nusa`, tekan Enter
30. Verifikasi `nusa` (huruf kecil) cocok dengan From `PT Nusa Distribusi`: 3 baris dengan baris teratas `HALC-20260908-00004`, `HALC-20260906-00003`, `HALC-20260903-00004`
31. Ganti isi kotak search dengan `GISTIK`, tekan Enter
32. Verifikasi `GISTIK` (huruf besar, potongan di tengah kata) cocok dengan Client `PT Sejahtera Logistik`: 16 baris dengan baris teratas `HALC-20260909-00003`, `HALC-20260909-00002`, `HALC-20260909-00001`

### TC-AC-ACHA-287: Query di-trim saat Enter

33. Ganti isi kotak search dengan ` Retail ` (spasi awal dan akhir), tekan Enter
34. Verifikasi hasil sama dengan `Retail`: 6 baris dengan baris teratas `HALC-20260908-00001`, `HALC-20260907-00001`, `HALC-20260905-00003`
35. Verifikasi isi input di layar tetap persis seperti yang diketik (spasi awal dan akhir tidak dibuang dari tampilan)
36. Ganti isi kotak search dengan tiga spasi, tekan Enter
37. Verifikasi tabel kembali ke 30 baris (query yang hanya berisi spasi diperlakukan sebagai kosong)

### TC-AC-ACHA-288: Search per kelas S1, teks kolom Allocation ID, Type, From, dan Client

38. Untuk setiap baris tabel Data uji TC-AC-ACHA-288 (langkah 38 sampai 39): ganti isi kotak search dengan kata kunci baris itu, tekan Enter
39. Verifikasi hasil: jumlah baris dan baris teratas sesuai kolom "Jumlah baris" dan "Baris teratas" baris tabel itu

### TC-AC-ACHA-289: Search per kelas S2, nama user pada Allocated By

40. Ganti isi kotak search dengan `Budi`, tekan Enter
41. Verifikasi kolom Allocated By (`Budi S`) cocok: 6 baris dengan baris teratas `HALC-20260908-00002`, `HALC-20260906-00002`, `HALC-20260905-00002`

### TC-AC-ACHA-290: Search per kelas S3, badge Category dan Status

42. Ganti isi kotak search dengan `NFC`, tekan Enter
43. Verifikasi Category `NFC`: 4 baris dengan baris teratas `HALC-20260908-00004`, `HALC-20260906-00002`, `HALC-20260904-00001`
44. Ganti isi kotak search dengan `Rejected`, tekan Enter
45. Verifikasi Status `Rejected`: 4 baris dengan baris teratas `HALC-20260908-00002`, `HALC-20260906-00003`, `HALC-20260903-00002`
46. Verifikasi kolom badge (Category dan Status) masuk cakupan Search bersama Filter Panel (kesimpulan dari dua hasil di atas)

### TC-AC-ACHA-291: Search per kelas S4, Quantity berformat Visible

47. Ganti isi kotak search dengan `5,000`, tekan Enter
48. Verifikasi `5,000` cocok dengan teks sel Quantity `5,000`: 1 baris dengan baris teratas `HALC-20260903-00004`
49. Ganti isi kotak search dengan `5000`, tekan Enter
50. Verifikasi `5000` tanpa pemisah tidak cocok: tampil `No results found` (Search mencocokkan teks sel sebagaimana tampil)
51. Ganti isi kotak search dengan `250`, tekan Enter
52. Verifikasi `250`: 1 baris dengan baris teratas `HALC-20260907-00001`

### TC-AC-ACHA-292: Search per kelas S5, teks kolom Curated Notes, Payment, dan Paid From

53. Klik ikon `⋯` pada header kolom terakhir
54. Centang kolom Notes, Payment, Paid From, dan Cost di overlay Column Visibility
55. Tutup overlay Column Visibility
56. Ganti isi kotak search dengan `Prioritas`, tekan Enter
57. Verifikasi Notes `Prioritas`: 1 baris dengan baris teratas `HALC-20260909-00002`
58. Ganti isi kotak search dengan `Free`, tekan Enter
59. Verifikasi Payment `Free`: 5 baris dengan baris teratas `HALC-20260908-00003`, `HALC-20260907-00002`, `HALC-20260905-00001`
60. Ganti isi kotak search dengan `Principal`, tekan Enter
61. Verifikasi Paid From `Principal` (teks `PT ABC (Principal)`): 19 baris dengan baris teratas `HALC-20260909-00003`, `HALC-20260909-00002`, `HALC-20260909-00001`

### TC-AC-ACHA-293: Search per kelas S6, Cost berformat Curated

62. Ganti isi kotak search dengan `$12,500.00`, tekan Enter
63. Verifikasi `$12,500.00` cocok dengan teks sel Cost `$12,500.00`: 1 baris dengan baris teratas `HALC-20260903-00004`
64. Verifikasi baris dengan Cost `—` (pengirim Principal) tidak tampil pada hasil kata kunci angka `$12,500.00`
65. Ganti isi kotak search dengan `12500`, tekan Enter
66. Verifikasi `12500` tanpa pemisah tidak cocok: tampil `No results found`

### TC-AC-ACHA-294: Guard, kolom tanggal tidak dapat dicari

67. Ganti isi kotak search dengan `09/09/26`, tekan Enter
68. Verifikasi kolom Last Updated tidak masuk cakupan Search: tampil `No results found`

### TC-AC-ACHA-295: Search terikat visibilitas kolom

69. Ganti isi kotak search dengan `Sejahtera`, tekan Enter
70. Verifikasi kolom Client tampil dan `Sejahtera` cocok 16 baris
71. Klik ikon `⋯` pada header kolom terakhir
72. Hilangkan centang kolom Client di overlay Column Visibility
73. Tutup overlay Column Visibility
74. Tekan Enter pada kotak Search berisi `Sejahtera`
75. Verifikasi pencarian `Sejahtera` tidak mencocokkan baris mana pun: tampil `No results found` (Search terikat visibilitas kolom)
76. Klik ikon `⋯` pada header kolom terakhir
77. Centang kembali kolom Client di overlay Column Visibility
78. Tutup overlay Column Visibility
79. Tekan Enter pada kotak Search berisi `Sejahtera`
80. Verifikasi pencarian `Sejahtera` kembali cocok 16 baris (reversibel)

### TC-AC-ACHA-296: Karakter khusus pada Search diperlakukan literal

81. Ganti isi kotak search dengan `%`, tekan Enter
82. Verifikasi tampil `No results found`
83. Ganti isi kotak search dengan `<script>alert(1)</script>`, tekan Enter
84. Verifikasi tampil `No results found`
85. Verifikasi tidak ada skrip yang dieksekusi (tidak ada dialog alert tampil)

### Pemulihan state

86. Klik `(←)` pada kotak Search
87. Klik ikon `⋯` pada header kolom terakhir
88. Hilangkan centang kolom Notes, Payment, Paid From, dan Cost di overlay Column Visibility
89. Tutup overlay Column Visibility

## Notes

- Sumber TC: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (bagian 4a-1). Seluruh TC primer spec ini (TC-AC-ACHA-282 sampai 296) dikerjakan di sini. TC-AC-ACHA-7 dan TC-AC-ACHA-9 (empty state Filtered dari Search) ada di spec 037.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): penutupan Search `(←)` di akhir TC-282, TC-283, dan pemulihan akhir; pembukaan, pencentangan, dan penutupan overlay Column Visibility (TC-292, TC-295, pemulihan akhir); langkah "Ganti isi kotak search dengan" yang membuka input bila tertutup dan mengosongkan isi lama (bagian 8b butir 9). Search `(←)` pada TC-285 diikuti "Klik ikon Search" dan `Verifikasi` input kosong sebagai observasi "keyword dikosongkan" (TC tidak memberi langkah observasi lain).
- Langkah 38 sampai 39 berulang untuk setiap baris tabel Data uji TC-AC-ACHA-288 (empat iterasi, bagian 8b butir 7). `Verifikasi` hasil dibaca per baris tabel, satu per klausa hasil (jumlah baris dan baris teratas satu hasil).
- Asersi tambahan (S-03): hasil `Retail` 6 baris di TC-284 diambil dari hasil TC-283, TC-287, dan TC-288 karena TC-284 hanya menulis "tabel tetap menampilkan hasil `Retail`". Pada TC-293 klausa "sel Cost `—` tidak cocok dengan kata kunci angka apa pun" diamati sebagai baris pengirim Principal tidak tampil pada hasil `$12,500.00` (anchor positif: satu baris `HALC-20260903-00004` tampil pada hasil yang sama). Pada TC-290 butir c adalah kesimpulan dari dua hasil sebelumnya, ditulis satu `Verifikasi`. TC-296 "tidak ada skrip yang dieksekusi" diamati sebagai tidak adanya dialog alert; anchor positif `No results found` pada langkah sebelumnya.
- Spec memiliki 89 langkah nominal, di atas smell 35 langkah. Alasan: seluruh blok berupa satu topik (Search List) pada dataset seed dan akun yang sama; tiap TC berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna); ekspansi berasal dari satu perulangan per kolom data (langkah 38 sampai 39) tanpa langkah bersyarat (prinsip 1 dan 13 bagian 3).
- Pemisahan topik satu dataset (prinsip 1): Search, Filter Panel, Sort, Setup Column, kombinasi kontrol, dan Pagination List memakai dataset Seed List yang sama (Pre-setup #48) dan dipisah menjadi spec 036 sampai 041 karena gabungannya jauh melewati batas ukuran (spec Search ini saja 89 langkah nominal, belum termasuk ekspansi perulangan). Pemisahan per kontrol dipertahankan karena tiap spec memulai dari kondisi default yang dipulihkan di akhir spec dan di hook `after` (Search kosong), sehingga kegagalan keras satu spec tidak membuat spec lain kehilangan makna; di dalam spec ini tiap TC mengakhiri dengan pemulihan state (S-09) dan tidak bergantung pada hasil TC lain, sehingga spec tetap satu (tanpa pemisah nyata: akun, kelas harness, dan dataset sama).
- Temuan untuk QA:
  - TC-AC-ACHA-292 sampai 293 mensyaratkan kolom Notes, Payment, Paid From, dan Cost ditampilkan lewat Setup Column, tetapi tidak menyebut cara (overlay Column Visibility atau popup Setup Column); spec memakai overlay Column Visibility (perubahan langsung diterapkan, TC-AC-ACHA-339).
  - TC-AC-ACHA-285 Expected "keyword dikosongkan" tidak punya langkah observasi; spec mengamatinya dengan membuka kembali Search dan memeriksa input kosong.
  - TC-AC-ACHA-283 Expected a "tabel belum tersaring" tidak menyebut jumlah baris; spec mengasersi pagination tetap tiga halaman dan 30 baris dari Seed List.
  - TC-AC-ACHA-296 Expected "tidak ada skrip yang dieksekusi" tidak memberi cara cek; spec mengasersi tidak adanya dialog alert.

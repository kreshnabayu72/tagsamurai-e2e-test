---
id: TC-GS-UCF-E2E-051-search-tabel-utama
title: "Search Tabel Utama Custom Field: Siklus Interaksi, Scope Kolom, Substring, Trim, Hasil Kosong, Visibilitas Kolom, dan Karakter Literal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-10
  - TC-GS-UCF-190
  - TC-GS-UCF-191
  - TC-GS-UCF-192
  - TC-GS-UCF-193
  - TC-GS-UCF-194
  - TC-GS-UCF-195
  - TC-GS-UCF-196
  - TC-GS-UCF-197
  - TC-GS-UCF-198
  - TC-GS-UCF-199
  - TC-GS-UCF-200
  - TC-GS-UCF-379
  - TC-GS-UCF-510
  - TC-GS-UCF-311
coverage:
  web: automated
---

# Search Tabel Utama Custom Field: Siklus Interaksi, Scope Kolom, Substring, Trim, Hasil Kosong, Visibilitas Kolom, dan Karakter Literal

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tetap di environment, tidak diubah spec ini, tanpa suffix; fixture baru (belum ada; lihat coverage) `Fixture.customFieldUser.preset14`):
  - `Cost Center`: Dropdown `Finance`, `Operations`, `Marketing`; Placeholder `Select cost center`; Required Yes; Active; Modified By `Budi S`; Last Updated 11 Sep 2026 10:35.
  - `Employee Grade`: Text; Placeholder kosong (efektif `Enter employee grade`); Required No; Active; `Siti R`; 10 Sep 2026 14:15.
  - `Job Description`: Text Area; Placeholder `Describe the job`; Required No; Active; `Siti R`; 10 Sep 2026 11:00.
  - `Bonus`: Numeric Decimal Places 2; Placeholder `Enter bonus`; Required No; Active; `Budi S`; 9 Sep 2026 15:20.
  - `Office Phone`: Phone; Placeholder `Enter phone number`; Required Yes; Active; `Budi S`; 9 Sep 2026 10:10.
  - `Joining Date`: Date; Placeholder `Select date`; Required No; Inactive; `Budi S`; 9 Sep 2026 09:00.
- Data Dinamis Population D-01 (8 field; fixture baru (belum ada; lihat coverage) `Fixture.customFieldUser.population`): `Blood Type` (Dropdown `A`, `B`, `AB`, `O`), `Shirt Size` (Dropdown `S`, `M`, `L`, `XL`; Placeholder `Choose shirt size`), `Emergency Phone` (Phone), `Birth Date` (Date), `Tax ID` (Text; Placeholder `Enter tax ID number`; Required Yes), `Work Notes` (Text Area), `Annual Target` (Numeric Decimal Places 1), `badge number` (Text); Required No kecuali `Tax ID`; Active; Placeholder lain kosong (efektif default). Di-seed lewat API oleh akun Total Control Client A di hook `before` (mekanisme seeding disediakan tim FE/BE, endpoint tidak ditulis di spec) sehingga Modified By `Sari D`. Nama literal tanpa suffix karena asersi jumlah 14 baris dan kata kunci Search bergantung pada nama (pengecualian Population, S-12); seeding idempotent (dilewati bila sudah ada); cleanup hanya menghapus yang dibuat hook spec ini. Total Custom Field Client A tepat 14 saat spec berjalan (6 Pre-setup + 8 Population) karena suite serial dan seed spec lain dibersihkan hook `after` spec itu.
- Data Dinamis milik spec (di-seed lewat API oleh akun Total Control Client A pada langkah yang menyebutnya, bukan di hook `before`, agar jumlah 14 baris tidak berubah untuk TC sebelumnya; nama bersuffix per run; fixture baru `Fixture.customFieldUser.searchSeed051`): `Long Value DD {runId}-051` (D-162: Dropdown `ABCDEFGHIJKLMNOPQRSTUVWXYZ` (26 karakter), `Beta`, `Gamma`; bebas nilai User) dan `Percent_100% Field {runId}-051` (D-93: Text; nama memuat `%` dan `_`).
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; spec tidak menguji navigasi sehingga tidak mengulang langkah buka di `## Test Steps`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Long Value DD {runId}-051`, `Percent_100% Field {runId}-051`, dan field Population yang dibuat hook `before`; pulihkan preferensi visibilitas kolom tabel utama ke default (8 kolom terlihat) dan ukuran halaman ke 10.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` halaman Custom Field true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: salin dan tempel teks (clipboard browser); pembacaan fokus input, nilai input Search (termasuk spasi di tepi), tooltip, visibilitas kolom, dan isi sel Value Setting; membuka Overlay Column Visibility.
- General Settings Date Format Client A tidak diubah spec ini; teks tanggal Last Updated dibaca dari sel tabel sesuai format yang berlaku.
- State global: ukuran halaman tabel diubah ke 25 (langkah 1) dan dikembalikan ke 10 (langkah 95); visibilitas kolom Data Type disembunyikan lalu ditampilkan kembali oleh TC-GS-UCF-199 (langkah 63 dan 68).

## Test Steps

### Persiapan

1. Ubah ukuran halaman tabel ke 25

### TC-GS-UCF-190: Siklus Search toolbar

2. Hover ikon Search
3. Verifikasi tooltip "Search"
4. Klik ikon Search
5. Verifikasi input Search melebar
6. Verifikasi input Search langsung fokus
7. Verifikasi placeholder input "Search custom field..."
8. Ketik `phone` (belum Enter)
9. Verifikasi icon `(✕)` muncul di dalam input
10. Verifikasi tabel belum tersaring (14 baris)
11. Tekan Enter
12. Verifikasi tabel menampilkan tepat dua baris: `Emergency Phone` dan `Office Phone`
13. Klik `(✕)`
14. Verifikasi isi input kosong
15. Verifikasi tabel masih tersaring (tetap dua baris `Emergency Phone` dan `Office Phone`)
16. Tekan Enter pada input kosong
17. Verifikasi tabel kembali menampilkan 14 baris
18. Ketik Search `phone`, tekan Enter
19. Klik `(←)`
20. Verifikasi input Search tertutup
21. Verifikasi tabel langsung kembali menampilkan 14 baris

### TC-GS-UCF-10: Empty state hasil Search kosong

22. Ketik Search `zzqx`, tekan Enter
23. Verifikasi Illustration tampil
24. Verifikasi Title "No results found"
25. Verifikasi Description "Try adjusting your search or filter."
26. Verifikasi tabel tidak menampilkan baris
27. Verifikasi Search tetap terisi `zzqx`
28. Klik `(←)`

### TC-GS-UCF-191: Search Field Name, substring dan tidak case-sensitive

29. Ketik Search `COST`, tekan Enter
30. Verifikasi tabel menampilkan tepat satu baris `Cost Center`
31. Ganti isi kotak search dengan `grade`, tekan Enter
32. Verifikasi tabel menampilkan tepat satu baris `Employee Grade`
33. Klik `(←)`

### TC-GS-UCF-192: Search kolom Data Type

34. Ketik Search `numeric`, tekan Enter
35. Verifikasi tabel menampilkan tepat dua baris: `Annual Target` dan `Bonus`
36. Klik `(←)`

### TC-GS-UCF-193: Search kolom Value Setting

37. Ketik Search `Finance`, tekan Enter
38. Verifikasi tabel menampilkan tepat satu baris `Cost Center`
39. Ganti isi kotak search dengan `decimal`, tekan Enter
40. Verifikasi tabel menampilkan tepat dua baris: `Annual Target` dan `Bonus`
41. Klik `(←)`

### TC-GS-UCF-194: Search kolom Required

42. Ketik Search `yes`, tekan Enter
43. Verifikasi tabel menampilkan tepat tiga baris: `Cost Center`, `Office Phone`, dan `Tax ID`
44. Klik `(←)`

### TC-GS-UCF-195: Search kolom Modified By

45. Ketik Search `siti`, tekan Enter
46. Verifikasi tabel menampilkan tepat dua baris: `Employee Grade` dan `Job Description`
47. Verifikasi kolom Modified By kedua baris bernilai `Siti R`
48. Klik `(←)`

### TC-GS-UCF-196: Search kolom Placeholder (nilai efektif)

49. Ketik Search `describe`, tekan Enter
50. Verifikasi tabel menampilkan tepat satu baris `Job Description` (Placeholder custom `Describe the job`)
51. Ganti isi kotak search dengan `select date`, tekan Enter
52. Verifikasi tabel menampilkan tepat dua baris: `Birth Date` (Placeholder default) dan `Joining Date` (Placeholder custom)
53. Klik `(←)`

### TC-GS-UCF-197: Kolom Active tidak tercakup Search

54. Ketik Search `Inactive`, tekan Enter
55. Verifikasi empty state "No results found" tampil
56. Ganti isi kotak search dengan `Active`, tekan Enter
57. Verifikasi empty state "No results found" tampil
58. Klik `(←)`

### TC-GS-UCF-198: Search nilai Last Updated tidak mencocokkan baris

59. Salin teks Last Updated pada baris `Cost Center` persis seperti tampil di tabel
60. Ketik Search teks Last Updated yang disalin, tekan Enter
61. Verifikasi empty state "No results found" tampil
62. Klik `(←)`

### TC-GS-UCF-199: Kolom yang di-hide dikecualikan dari Search

63. Klik ikon `⋯` pada header kolom Actions, uncheck `Data Type`, tutup Overlay Column Visibility
64. Ketik Search `numeric`, tekan Enter
65. Verifikasi empty state "No results found" tampil
66. Klik `(←)`
67. Verifikasi tabel kembali menampilkan 14 baris
68. Klik ikon `⋯` pada header kolom Actions, centang `Data Type`, tutup Overlay Column Visibility
69. Ketik Search `numeric`, tekan Enter
70. Verifikasi tabel menampilkan tepat dua baris: `Annual Target` dan `Bonus`
71. Klik `(←)`

### TC-GS-UCF-200: Search dengan spasi di tepi di-trim

72. Ketik Search `  phone  `, tekan Enter
73. Verifikasi tabel menampilkan tepat dua baris: `Emergency Phone` dan `Office Phone` (hasil sama dengan `phone`)
74. Verifikasi isi kotak Search tetap `  phone  ` seperti yang diketik
75. Klik `(←)`

### TC-GS-UCF-379: Search mencocokkan value Dropdown di balik chip +N more

76. Ketik Search `Marketing`, tekan Enter
77. Verifikasi tabel menampilkan tepat satu baris `Cost Center`
78. Verifikasi sel Value Setting baris `Cost Center` menampilkan badge `Finance`, badge `Operations`, dan chip `+1 more`
79. Verifikasi `Marketing` tidak tampil sebagai badge
80. Klik `(←)`

### TC-GS-UCF-510: Search mencocokkan bagian value yang tersembunyi di balik pemotongan badge

81. Buat lewat API field `Long Value DD {runId}-051` (Dropdown `ABCDEFGHIJKLMNOPQRSTUVWXYZ`, `Beta`, `Gamma`) hingga tersimpan, lalu muat ulang halaman (F5)
82. Ketik Search `LMNO`, tekan Enter
83. Verifikasi tabel menampilkan tepat satu baris `Long Value DD {runId}-051`
84. Verifikasi sel Value Setting baris tersebut menampilkan badge `ABCDEFGHIJKL..OPQRSTUVWXYZ`, badge `Beta`, dan chip `+1 more`
85. Verifikasi teks `LMNO` tidak tampil utuh pada badge
86. Klik `(←)`

### TC-GS-UCF-311: Search memperlakukan % dan _ sebagai karakter literal

87. Buat lewat API field `Percent_100% Field {runId}-051` (Text) hingga tersimpan, lalu muat ulang halaman (F5)
88. Ketik Search `%`, tekan Enter
89. Verifikasi tabel menampilkan tepat satu baris `Percent_100% Field {runId}-051`
90. Ganti isi kotak search dengan `_`, tekan Enter
91. Verifikasi tabel menampilkan tepat satu baris `Percent_100% Field {runId}-051` (bukan seluruh baris)
92. Ganti isi kotak search dengan `' OR 1=1 --`, tekan Enter
93. Verifikasi empty state "No results found" tampil
94. Klik `(←)`
95. Ubah ukuran halaman tabel kembali ke 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 95 langkah (di atas smell sekitar 35 langkah). Alasan: seluruhnya satu topik dan satu dataset (Search tabel utama), satu akun, tanpa mengubah data Pre-setup atau Population; tiap blok TC dimulai dari state Search tertutup dan tetap bermakna bila blok lain gagal, dan langkah `Verifikasi` per baris hasil mendominasi jumlah langkah.
- Urutan TC mengikuti urutan TC sumber, kecuali TC-GS-UCF-510 dan TC-GS-UCF-311 yang ditaruh paling akhir karena field `Long Value DD {runId}-051` dan `Percent_100% Field {runId}-051` baru dibuat pada langkah 81 dan 87; dengan begitu total tetap 14 baris untuk asersi "14 baris" pada TC-GS-UCF-190 (langkah 10, 17, 21) dan TC-GS-UCF-199 (langkah 67). TC-GS-UCF-199 menyembunyikan kolom Data Type dan menampilkannya kembali pada blok yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 95 (ukuran halaman 25 agar seluruh 14 baris tampil pada satu halaman sehingga "14 baris" dapat diasersi, lalu dikembalikan ke 10), langkah 19, 28, 33, 36, 41, 44, 48, 53, 58, 62, 66, 71, 75, 80, 86, dan 94 (`(←)` menutup input dan mengosongkan keyword sebelum TC berikutnya), langkah 59 (menyalin teks tanggal), langkah 81 dan 87 (seeding field milik spec lewat API di tengah spec, alasan di butir urutan di atas), serta langkah 63 dan 68 (hide dan unhide kolom, bagian dari TC-GS-UCF-199).
- Search pada TC selain TC-GS-UCF-190 ditulis atomik ("Ketik Search `X`, tekan Enter") sesuai bagian 8b butir 9 konvensi; klik ikon Search eksplisit hanya pada siklus TC-GS-UCF-190 (langkah 4). Asersi hasil Search memakai bentuk "tepat N baris: X dan Y" agar asersi universal terhubung ke baris yang disebut TC (bagian 8b butir 2).
- Langkah 65 (empty state sebagai anchor positif) mendahului pemulihan kolom pada TC-GS-UCF-199; langkah 67 menjadi `Verifikasi` baseline tambahan (14 baris kembali setelah Search ditutup) di luar Expected TC, supaya langkah unhide berjalan dari state tabel utuh.
- P-5: TC-GS-UCF-311 (kelas defense-in-depth, input `%`, `_`, dan payload SQL pada kolom Search) adalah satu TC objek-uji ringan tanpa harness eksternal dan tanpa state berat, sehingga ditaruh di spec Search yang berbagi permukaan yang sama.
- Pembagian TC lintas spec: Filter Panel tabel utama (TC-GS-UCF-201 sampai 213, 221, 351 sampai 354, 397) ada di spec 052; kombinasi Search, Filter, Sort, dan Pagination (TC-GS-UCF-214 sampai 220, 231, 504 sampai 507) di spec 053; Sort di spec 054; Pagination di spec 055; Setup Column di spec 056; Download di spec 057.
- Temuan untuk QA:
  - TC-GS-UCF-190 tidak menyebut ukuran halaman; Expected e dan f menyebut "14 baris kembali" sedangkan ukuran halaman bawaan 10 hanya menampilkan 10 baris. Spec memakai ukuran halaman 25 (langkah 1).
  - Keputusan NC yang berbeda dari API/LLD (NC-06, NC-10): TC-GS-UCF-196 (Search Placeholder nilai efektif), TC-GS-UCF-197 (kolom Active tidak searchable), dan TC-GS-UCF-193 (kata kunci `decimal` pada teks Value Setting `Decimal Places` Title Case) ditulis sesuai TC dan PRD; asersi dapat gagal pada backend nyata sampai API/LLD diselaraskan.
  - TC-GS-UCF-198 tidak menyebut teks tanggal Last Updated yang diketik; spec menyalin teks sel baris `Cost Center` apa adanya (sesuai Date Format General Settings yang berlaku saat run).
  - TC-GS-UCF-199 menyebut "Column Visibility" tanpa menyebut kontrolnya; spec memakai Overlay Column Visibility dari header kolom Actions `⋯` (keputusan NC-01).
  - TC-GS-UCF-197 Expected tidak menyebut Title dan Description empty state terpisah untuk kedua kata kunci; spec mengasersi empty state "No results found" (teks Title dan Description diasersi pada TC-GS-UCF-10).
  - Post Condition TC-GS-UCF-510 dan TC-GS-UCF-311 kosong ("-"); tidak ada yang diasersi.
  - Nama field D-93 dan D-162 diberi suffix `{runId}-051`; Expected TC yang menyebut `Percent_100% Field` dan `Long Value DD` tanpa suffix diasersi pada nama bersuffix.

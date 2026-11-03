---
id: TC-GS-HHR-E2E-061-changelog-modal-screening-search-filter-sort
title: "Modal Changelog Handheld Reader: Screening, Isi Baris, Search, Filter, Sort 3-State, dan Empty State Client E"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-326
  - TC-GS-HHR-327
  - TC-GS-HHR-328
  - TC-GS-HHR-329
  - TC-GS-HHR-330
  - TC-GS-HHR-331
  - TC-GS-HHR-332
  - TC-GS-HHR-333
  - TC-GS-HHR-334
  - TC-GS-HHR-335
  - TC-GS-HHR-336
coverage:
  web: automated
---

# Modal Changelog Handheld Reader: Screening, Isi Baris, Search, Filter, Sort 3-State, dan Empty State Client E

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini hanya membaca Modal Changelog (tidak ada aksi tulis); baris seed dikenali lewat `Date` dan jumlah baris tabel tidak diasersi sebagai angka absolut (lihat aturan baca seed di bawah).
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` membuka layar lagi hanya sesudah ganti akun.
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Akun kedua (TC-GS-HHR-328, langkah 106): Total Control Client E, email `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup TC, Client E), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Client E belum memiliki reader, entri Changelog, maupun Event Log; keadaan kosong itu dijaga reset tingkat entitas (DD-08; Client E) yang disediakan tim FE/BE dan dinyatakan di `suite.md` (pengecualian A-6, lihat `## Notes`). Hook `after` mengembalikan sesi ke akun default suite (Client A).
- Data Pre-setup: Client A plan Growth, Seed Reader A (DD-01 s.d. DD-10; `Fixture.hardwareHandheldReader.seedReaderA`) dipakai sebagai precondition TC, tidak diasersi. Format tanggal Client A `dd/MM/yy` 24-hour Asia/Jakarta.
- Seed Changelog Client A (CL-01 s.d. CL-09; fixture `Fixture.hardwareHandheldReader.seedChangelogClientA`), urut Date terbaru di atas:

  | ID | Date | Action | Device Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|---|
  | CL-01 | 23/06/26 08:50 | Edit | Gudang Reader - 2 (SKU-HHR-03) | Status | Available | Missing | Budi S |
  | CL-02 | 22/06/26 10:00 | Activate | Honeywell CK65 - 1 | Status | — | Available | Budi S |
  | CL-03 | 21/06/26 08:00 | Activate | Zebra RFID Reader - 1 (SKU-HHR-01) | Status | — | Available | Budi S |
  | CL-04 | 20/06/26 11:10 | Activate | Chainway C72 - 1 | Status | — | Waiting for Approval | Sari D |
  | CL-05 | 19/06/26 10:30 | Edit | Reader Gudang 02 (SKU-HHR-03) | Alias Name | Gudang 02 | Reader Gudang 02 | Sari D |
  | CL-06 | 18/06/26 16:20 | Edit | Zebra Mobile Reader - 1 (SKU-HHR-02) | Reader Power | 30 dBm | 25 dBm | Budi S |
  | CL-07 | 17/06/26 09:05 | Edit | Zebra Mobile Reader - 1 (SKU-HHR-02) | Status | Available | Damaged | Sari D |
  | CL-08 | 16/06/26 14:40 | Edit | Zebra Mobile Reader - 1 (SKU-HHR-02) | Status | Damaged | Available | Budi S |
  | CL-09 | 15/06/26 11:15 | Delete | Reader Lama | Device Name | Reader Lama | — | Sari D |

  Kolom Action dan nilai Status berupa teks polos (bukan badge). Nilai distinct pada tiap kolom yang diuji Search, Filter, dan Sort tersedia pada seed (S-11).
- Aturan baca seed: audit trail bersifat permanen dan spec lain menambah entri Changelog Client A bertanggal waktu aksi (Okt 2026), di luar rentang `Date` seed `15/06/26` sampai `23/06/26`. Fixture backend hanya menulis entri seed bertanggal Juni 2026 dan tidak memulihkan audit trail (kemampuan disediakan tim FE/BE tanpa endpoint yang dikarang; lihat Temuan untuk QA). Baris seed dikenali lewat `Date`; "N baris" pada Expected berarti N baris seed yang cocok (dibaca pada kolom `Date` seluruh halaman hasil atau pada hasil Filter `Date` seed), baris non-seed boleh tampil dan jumlahnya tidak diasersi; kembali ke tabel penuh diasersi terhadap baseline N0 yang dicatat sebelum Search atau Filter; baris pertama hanya dibaca pada tabel yang dibatasi Filter `Date` seed. Hasil Search dan Filter non-`Date` dibaca setelah tabel dibatasi Filter `Date` seed `15/06/26` sampai `23/06/26` (langkah 32 sampai 35 untuk Search, diisi bersama filter lain pada kasus Filter dan gabungan Search+Filter), sehingga seluruh baris seed berada pada satu halaman hasil (maksimum 9 baris seed, ukuran halaman 10) dan tidak perlu pindah halaman (S-14).
- Tabel "Kasus Search Modal Changelog" (parameter langkah 36 sampai 39):

  | Keyword | Kolom yang dicari | Hasil |
  |---|---|---|
  | `Delete` | Action | 1 baris seed `Reader Lama` (CL-09) |
  | `SKU-HHR-02` | Device Name (cocok dengan bagian SKU pada format `[Name] ([SKU])`) | 3 baris seed `Zebra Mobile Reader - 1` (CL-06, CL-07, CL-08) |
  | `Alias` | Field | 1 baris seed `Reader Gudang 02` (CL-05) |
  | `30 dBm` | Old Value | 1 baris seed Reader Power (CL-06) |
  | `Missing` | New Value | 1 baris seed `Gudang Reader - 2` (CL-01) |
  | `Budi` | Modified By | 5 baris seed (CL-01, CL-02, CL-03, CL-06, CL-08) |

- Tabel "Kasus Filter Modal Changelog" (parameter langkah 77 sampai 83):

  | Filter | Cara isi | Hasil |
  |---|---|---|
  | Action | pilih `Edit` pada `Action` | 5 baris seed (CL-01, CL-05, CL-06, CL-07, CL-08) |
  | Field | pilih `Status` pada `Field` | 6 baris seed (CL-01, CL-02, CL-03, CL-04, CL-07, CL-08) |
  | Device Name | pilih `Reader Lama` pada `Device Name` | 1 baris seed (CL-09) |
  | Modified By | pilih nama lengkap `Sari Dewi` pada `Modified By` | 4 baris seed (CL-04, CL-05, CL-07, CL-09) |
  | Date | isi rentang `17/06/26` s.d. `19/06/26` pada `Date` | 3 baris (CL-05, CL-06, CL-07; kedua batas termasuk) |

- Tabel "Kasus Sort Modal Changelog" (parameter langkah 98 sampai 103; baris pertama dibaca pada tabel yang dibatasi Filter `Date` seed `15/06/26` sampai `23/06/26`, langkah 95 sampai 97):

  | Kolom | Ascending, baris 1 | Descending, baris 1 |
  |---|---|---|
  | `Date` | `15/06/26` (Reader Lama) | `23/06/26` |
  | `Action` | `Activate` terbaru (`22/06/26` Honeywell CK65 - 1) | `Edit` terbaru (`23/06/26`) |
  | `Device Name` | `Chainway C72 - 1` | `Zebra RFID Reader - 1 (SKU-HHR-01)` |
  | `Field` | `Alias Name` | `Status` terbaru (`23/06/26`) |
  | `Old Value` | tiga baris `—` (Activate) di akhir, urut Date terbaru: `Honeywell CK65 - 1` (`22/06/26`), `Zebra RFID Reader - 1 (SKU-HHR-01)` (`21/06/26`), `Chainway C72 - 1` (`20/06/26`) | tiga baris `—` (Activate) di awal, urutan dalam kelompok sama |
  | `New Value` | baris `—` (Delete, `Reader Lama`) di akhir (satu baris, tanpa urutan sekunder) | baris `—` (Delete, `Reader Lama`) di awal |
  | `Modified By` | `Budi S` terbaru (`23/06/26`) | `Sari D` terbaru (`20/06/26`) |

- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor (termasuk akun Client E) dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pembacaan Modal Changelog (baris, kolom, empty state, opsi dropdown filter), pengisian rentang tanggal pada Filter `Date` lewat date picker (Filter `Date` diproses server-side dan inklusif kedua ujung), penulisan entri seed Changelog bertanggal Juni 2026 oleh fixture backend (tanpa memulihkan audit trail).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-HHR-326 dan TC-GS-HHR-327: Screening Modal Changelog dan isi baris

1. Klik ikon Changelog
2. Catat jumlah baris tabel sebagai baseline N0
3. Verifikasi N0 tidak kurang dari 9 (N0 tidak diasersi sebagai angka absolut)
4. Verifikasi Header menampilkan Judul `Changelog: Handheld Reader`
5. Verifikasi Header menampilkan ikon `[✕]`
6. Verifikasi Table Tools menampilkan `Search`, `Filter`, `Download`
7. Verifikasi kolom tabel berurutan: `Date`, `Action`, `Device Name`, `Field`, `Old Value`, `New Value`, `Modified By`, `Column Visibility (⋯)`
8. Verifikasi tujuh kolom `Date`, `Action`, `Device Name`, `Field`, `Old Value`, `New Value`, `Modified By` sortable
9. Verifikasi kolom `Column Visibility (⋯)` tidak sortable
10. Klik header kolom `Column Visibility (⋯)`
11. Verifikasi overlay Column Visibility terbuka
12. Tutup overlay Column Visibility dengan klik di luar overlay
13. Klik ikon Filter di modal
14. Isi `Date` rentang `15/06/26` s.d. `23/06/26`
15. Klik `[Apply]`
16. Verifikasi tabel menampilkan 9 baris seed CL-01 sampai CL-09 (`Date` `15/06/26` sampai `23/06/26`)
17. Verifikasi baris pertama berdasarkan `Date` terbaru pada hasil Filter itu adalah `23/06/26`
18. Verifikasi Footer menampilkan pagination dengan ukuran halaman default 10 per halaman
19. Verifikasi baris `23/06/26 08:50`: Action `Edit`, Device Name `Gudang Reader - 2 (SKU-HHR-03)`, Field `Status`, Old Value `Available`, New Value `Missing`, Modified By `Budi S`
20. Verifikasi baris `22/06/26 10:00`: Action `Activate`, Device Name `Honeywell CK65 - 1`, Field `Status`, Old Value `—`, New Value `Available`, Modified By `Budi S`
21. Verifikasi baris `21/06/26 08:00`: Action `Activate`, Device Name `Zebra RFID Reader - 1 (SKU-HHR-01)`, Field `Status`, Old Value `—`, New Value `Available`, Modified By `Budi S`
22. Verifikasi baris `20/06/26 11:10`: Action `Activate`, Device Name `Chainway C72 - 1`, Field `Status`, Old Value `—`, New Value `Waiting for Approval`, Modified By `Sari D`
23. Verifikasi baris `19/06/26 10:30`: Action `Edit`, Device Name `Reader Gudang 02 (SKU-HHR-03)`, Field `Alias Name`, Old Value `Gudang 02`, New Value `Reader Gudang 02`, Modified By `Sari D`
24. Verifikasi baris `18/06/26 16:20`: Action `Edit`, Device Name `Zebra Mobile Reader - 1 (SKU-HHR-02)`, Field `Reader Power`, Old Value `30 dBm`, New Value `25 dBm`, Modified By `Budi S`
25. Verifikasi baris `17/06/26 09:05`: Action `Edit`, Device Name `Zebra Mobile Reader - 1 (SKU-HHR-02)`, Field `Status`, Old Value `Available`, New Value `Damaged`, Modified By `Sari D`
26. Verifikasi baris `16/06/26 14:40`: Action `Edit`, Device Name `Zebra Mobile Reader - 1 (SKU-HHR-02)`, Field `Status`, Old Value `Damaged`, New Value `Available`, Modified By `Budi S`
27. Verifikasi baris `15/06/26 11:15`: Action `Delete`, Device Name `Reader Lama`, Field `Device Name`, Old Value `Reader Lama`, New Value `—`, Modified By `Sari D`
28. Verifikasi kolom `Action` dan nilai `Status` berupa teks polos, bukan badge
29. Klik `[Clear Field]`
30. Klik `[Apply]`
31. Klik ikon Filter di modal untuk menutup Filter Panel

### TC-GS-HHR-330: Search per kolom searchable

32. Klik ikon Filter di modal
33. Isi `Date` rentang `15/06/26` s.d. `23/06/26` (pembatas seed)
34. Klik `[Apply]`
35. Klik ikon Filter di modal untuk menutup Filter Panel

Untuk setiap baris tabel "Kasus Search Modal Changelog" (langkah 36 sampai 39):

36. Ketik Search `{Keyword}`, tekan Enter
37. Verifikasi hasil memuat baris seed sesuai kolom "Hasil" pada baris tabel untuk kolom {Kolom yang dicari}, dibaca pada hasil yang dibatasi Filter `Date` seed `15/06/26` sampai `23/06/26` (seluruh baris seed berada pada satu halaman hasil)
38. Verifikasi setiap baris yang tampil memuat `{Keyword}` pada kolom {Kolom yang dicari}; baris non-seed boleh tampil dan jumlahnya tidak diasersi
39. Klik `(←)` pada kotak Search di modal
40. Klik ikon Filter di modal
41. Klik `[Clear Field]`
42. Klik `[Apply]`
43. Klik ikon Filter di modal untuk menutup Filter Panel

### TC-GS-HHR-331: Nilai tanggal tidak dicari lewat Search

44. Ketik Search `21/06/26`, tekan Enter
45. Verifikasi empty state `No results found` tampil (kolom `Date` tidak searchable)
46. Klik `(←)` pada kotak Search di modal

### TC-GS-HHR-329: Search tanpa hasil dan Reset Filters

47. Catat jumlah baris tabel sebagai baseline N0
48. Klik ikon Filter di modal
49. Pilih `Edit` pada `Action`
50. Klik `[Apply]`
51. Ketik Search `zzzz`, tekan Enter
52. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
53. Verifikasi tombol `[Reset Filters]` tampil
54. Klik `[Reset Filters]`
55. Verifikasi kotak Search kosong
56. Verifikasi ikon Filter tanpa titik indikator
57. Verifikasi tabel kembali ke halaman 1
58. Verifikasi jumlah baris tabel sama dengan N0 (langkah 47), yaitu seluruh baris Changelog Client A

### TC-GS-HHR-332 dan TC-GS-HHR-333: Screening Filter Panel dan opsi dropdown

59. Klik ikon Filter di modal
60. Verifikasi field `Date` berupa date range dengan placeholder `Select date`
61. Verifikasi field `Action` dengan placeholder `All actions`
62. Verifikasi field `Device Name` dengan placeholder `All devices`
63. Verifikasi field `Field` dengan placeholder `All fields`
64. Verifikasi field `Modified By` dengan placeholder `All users`
65. Verifikasi kolom `Old Value` dan `New Value` tidak punya field filter
66. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil
67. Buka dropdown `Action`
68. Verifikasi opsi `Action`: `Activate`, `Edit`, `Delete`
69. Tutup dropdown `Action`
70. Buka dropdown `Device Name`
71. Verifikasi dropdown `Device Name` memuat 7 nama seed: `Gudang Reader - 2 (SKU-HHR-03)`, `Honeywell CK65 - 1`, `Zebra RFID Reader - 1 (SKU-HHR-01)`, `Chainway C72 - 1`, `Reader Gudang 02 (SKU-HHR-03)`, `Zebra Mobile Reader - 1 (SKU-HHR-02)` (nama dengan SKU sebagai snapshot), dan `Reader Lama` (tanpa SKU); opsi tambahan dari entri non-seed tidak diasersi jumlahnya
72. Tutup dropdown `Device Name`
73. Buka dropdown `Field`
74. Verifikasi opsi `Field`: `Status`, `Alias Name`, `Reader Power`, `Device Name`
75. Tutup dropdown `Field`
76. Tutup Filter Panel

### TC-GS-HHR-334: Filter per field

Untuk setiap baris tabel "Kasus Filter Modal Changelog" (langkah 77 sampai 83):

77. Klik ikon Filter di modal
78. Terapkan filter sesuai kolom "Cara isi" pada baris tabel; untuk baris selain `Date`, isi juga `Date` rentang `15/06/26` s.d. `23/06/26` sebagai pembatas seed
79. Klik `[Apply]`
80. Verifikasi baris seed yang cocok sesuai kolom "Hasil" pada baris tabel, dibaca pada hasil yang dibatasi Filter `Date` seed `15/06/26` sampai `23/06/26` (seluruh baris seed berada pada satu halaman hasil)
81. Klik `[Clear Field]`
82. Klik `[Apply]`
83. Klik ikon Filter di modal untuk menutup Filter Panel

### TC-GS-HHR-335: Search dan Filter digabung AND

84. Ketik Search `Zebra`, tekan Enter
85. Klik ikon Filter di modal
86. Pilih `Edit` pada `Action` dan isi `Date` rentang `15/06/26` s.d. `23/06/26` sebagai pembatas seed
87. Klik `[Apply]`
88. Verifikasi hasil memuat 3 baris seed `Zebra Mobile Reader - 1 (SKU-HHR-02)` (baris seed = `Date` `15/06/26` sampai `23/06/26`): CL-06 Field `Reader Power`, CL-07 Field `Status` (`Available` ke `Damaged`), dan CL-08 Field `Status` (`Damaged` ke `Available`)
89. Verifikasi baris seed Activate `Zebra RFID Reader - 1 (SKU-HHR-01)` (CL-03) tidak tampil
90. Verifikasi setiap baris yang tampil ber-Action `Edit` dan memuat `Zebra`; baris non-seed boleh tampil dan jumlahnya tidak diasersi
91. Klik `(←)` pada kotak Search di modal
92. Klik `[Clear Field]`
93. Klik `[Apply]`
94. Klik ikon Filter di modal untuk menutup Filter Panel

### TC-GS-HHR-336: Sort 3-state per kolom

95. Klik ikon Filter di modal
96. Isi `Date` rentang `15/06/26` s.d. `23/06/26`
97. Klik `[Apply]` (tabel dibatasi ke baris seed CL-01 sampai CL-09)

Untuk setiap baris tabel "Kasus Sort Modal Changelog" (langkah 98 sampai 103):

98. Klik header kolom {Kolom} satu kali
99. Verifikasi baris tabel diurutkan Ascending pada {Kolom} dengan hasil kolom "Ascending, baris 1" pada baris tabel
100. Klik header kolom {Kolom} kedua kali
101. Verifikasi baris tabel diurutkan Descending pada {Kolom} dengan hasil kolom "Descending, baris 1" pada baris tabel
102. Klik header kolom {Kolom} ketiga kali
103. Verifikasi urutan netral: kembali `Date` terbaru di atas (baris pertama `23/06/26`)

### TC-GS-HHR-328: Empty state Modal Changelog Client E

104. Tutup Modal Changelog dengan `✕`
105. Logout dari akun Total Control Client A
106. Login sebagai Total Control Client E (`totalControl_automated_qaTeam5@qwertysystem.net`, `Spectra.env.GS_CLIENTE_TC_PASSWORD`)
107. Buka Global Settings > Hardware > Handheld Reader
108. Klik ikon Changelog
109. Verifikasi ilustrasi dengan judul `No changelog yet` dan deskripsi `Activities and changes will appear here.`
110. Verifikasi empty state tanpa tombol aksi

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 4b). Spec hanya membaca; tidak ada data yang dibuat atau dihapus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok menyimpang dari urutan nomor TC: TC-GS-HHR-330, 331, 329 (Search) berurutan; 332 dan 333 (screening Filter dan opsi dropdown) sebelum 334 dan 335; Sort (TC-GS-HHR-336) paling akhir di Client A; TC-GS-HHR-328 (Client E) paling akhir karena ganti akun. Bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal, dan hanya satu kali ganti akun (langkah 105 dan 106).
- Langkah penghubung (aksi tanpa `Verifikasi`): mencatat baseline N0 (langkah 2 dan 47), menutup overlay Column Visibility, menutup dropdown dan Filter Panel, `(←)` pada Search, Filter `Date` seed sebagai pembatas sebelum dan sesudah blok Search (langkah 32 sampai 35 dan 40 sampai 43, S-14), `[Clear Field]` lalu `[Apply]` lalu menutup Filter Panel dengan ikon Filter sesudah blok TC-GS-HHR-326 dan 327 (langkah 29 sampai 31; panel Filter tetap terbuka sesudah `[Apply]`, jadi `[Clear Field]` diklik tanpa menekan ikon Filter lebih dulu), pada akhir tiap kasus Filter, dan sesudah TC-GS-HHR-335 (S-09, state dibersihkan sebelum blok berikutnya), menutup Modal Changelog, Logout, Login, dan membuka layar Handheld Reader sesudah ganti akun. Langkah "Klik header kolom `Column Visibility (⋯)`" dan Verifikasi overlay Column Visibility menjalankan klausa Expected TC-GS-HHR-326 "header klik = buka overlay Column Visibility".
- Langkah berulang per baris tabel: Search (langkah 36 sampai 39), Filter (langkah 77 sampai 83), dan Sort (langkah 98 sampai 103); parameter tiap iterasi ada di tabel `## Prerequisites`. Ekspansi: Search 6 iterasi x 4, Filter 5 iterasi x 7, Sort 7 iterasi x 6, sehingga ekspansi total jauh di atas 35 langkah. Alasan spec tetap satu: semua blok berada pada satu kelas (fungsional baca) dan satu dataset (Seed Changelog Client A), tidak ada data yang dibuat atau diubah sehingga tidak ada cleanup, dan kegagalan satu blok (misalnya Sort) tidak membuat blok lain kehilangan makna karena tiap blok memulai dari state yang dibersihkan; kegagalan keras hanya pada pembukaan Modal Changelog (langkah pertama).
- Hasil Search dan Filter diasersi sebagai baris seed (CL-ID per baris dari TC-GS-HHR-330 dan 334) yang dibaca lewat `Date`, ditambah invarian bahwa setiap baris yang tampil memuat keyword (langkah 38 dan 90); jumlah baris yang disebut TC (1, 3, 5, 6, 4) berasal dari baris seed pada `## Prerequisites`, bukan dari total entri tabel (8b butir 10). Kembali ke tabel penuh (langkah 58) diasersi terhadap baseline N0, bukan terhadap 9. Pembanding untuk asersi absence (langkah 89, baris Activate tidak tampil) adalah tiga baris seed `Zebra Mobile Reader - 1` yang diasersi pada langkah 88; pembanding untuk asersi universal pada langkah 38 dan 90 adalah baris seed yang diasersi tepat sebelumnya. Empty state `No results found` pada TC-GS-HHR-331 dan 329 sah sebagai anchor positif Search karena tabel pada langkah sebelumnya menampilkan baris.
- Pengecualian A-6 (empty state entitas bersih): TC-GS-HHR-328 mengasersi empty state Modal Changelog Client E sebagai nol absolut tanpa baseline (empty state tidak dapat relatif). Client E tidak pernah ditulis spec mana pun dan keadaan kosongnya dijaga reset tingkat entitas (DD-08; Client E) yang disediakan tim FE/BE, dinyatakan di `suite.md` dan Prerequisites; suite serial; spec ini tidak menulis apa pun di Client E.
- Pembagian TC lintas spec: Setup Column Modal Changelog (TC-GS-HHR-292 sampai 305) di spec 056; pagination sekunder (TC-GS-HHR-325) di spec 060; kegagalan unduh Modal Changelog (TC-GS-HHR-339) di spec 028; tutup, Download, dan Tab Changelog Popup Detail (TC-GS-HHR-337, 338, 340 sampai 342, 454, 469, 470) di spec 062.
- Temuan untuk QA:
  - Pembatas Filter `Date` seed (langkah 32 sampai 35, 78, dan 86) ditambahkan spec di luar langkah TC-GS-HHR-330, 334, dan 335 agar baris seed berada pada satu halaman (S-14); Expected TC (baris seed dibaca pada seluruh halaman hasil) tetap terpenuhi karena filter tidak mengubah identitas baris seed. Tolong konfirmasi bahwa penambahan itu tidak mengubah maksud TC.
  - Klik header sort (kontrol di luar panel) dilakukan saat Filter Panel masih terbuka (langkah 98 sampai 103); apakah klik itu menutup panel belum ditetapkan (keputusan D-A audit e2e delta 1).
  - TC-GS-HHR-326 sampai 336 bergantung pada Filter `Date` yang diproses server-side dan inklusif kedua ujung, pada fixture backend yang dapat menulis entri Changelog Client A bertanggal Juni 2026 (CL-01 sampai CL-09), dan pada date picker yang menerima rentang `15/06/26` sampai `23/06/26`; hal ini tidak didefinisikan di TC, PRD, atau LLD dan disediakan tim FE/BE. Audit trail tidak dipulihkan.
  - Nama env password akun Total Control Client E (`GS_CLIENTE_TC_PASSWORD`) tidak tertulis di Pre-setup TC dan belum tentu terdaftar di `spectra.config.ts` dan `.env.example` (diusulkan ke owner suite).
  - TC-GS-HHR-336 butir h ("Klik ketiga: netral") dibaca berlaku untuk setiap kolom; spec mengasersi urutan netral sesudah klik ketiga pada tiap kolom.
  - Cara menutup Filter Panel dan dropdown tidak dinyatakan di TC; spec menulis langkah penghubung generik "Tutup".
  - TC-GS-HHR-326 Expected c ("Pagination default 10 per halaman") tidak menyebut teks footer; spec mengasersi ukuran halaman default 10.

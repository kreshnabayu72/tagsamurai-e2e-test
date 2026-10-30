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
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini hanya membaca Modal Changelog (tidak ada aksi tulis); isi Seed Changelog Client A harus utuh karena asersi bergantung pada sembilan baris seed.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` membuka layar lagi hanya sesudah ganti akun.
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Akun kedua (TC-GS-HHR-328, langkah 80): Total Control Client E, email `totalControl_automated_{namaClient}@qwertysystem.net` dengan nilai `{namaClient}` dari fixture `Fixture.hardwareHandheldReader` (nilai tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Client E belum memiliki reader, entri Changelog, maupun Event Log. Hook `after` mengembalikan sesi ke akun default suite (Client A).
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
- Isolasi seed: audit trail bersifat permanen dan spec lain menambah entri Changelog Client A. Seed Changelog Client A dipulihkan lewat fixture backend di hook `before` dan `after` (kemampuan disediakan tim FE/BE tanpa endpoint yang dikarang; lihat Temuan untuk QA).
- Tabel "Kasus Search Modal Changelog" (parameter langkah 24 sampai 26):

  | Keyword | Kolom yang dicari | Hasil |
  |---|---|---|
  | `Delete` | Action | 1 baris `Reader Lama` |
  | `SKU-HHR-02` | Device Name dan SKU | 3 baris `Zebra Mobile Reader - 1` |
  | `Alias` | Field | 1 baris `Reader Gudang 02` |
  | `30 dBm` | Old Value | 1 baris Reader Power |
  | `Missing` | New Value | 1 baris `Gudang Reader - 2` |
  | `Budi` | Modified By | 5 baris |

- Tabel "Kasus Filter Modal Changelog" (parameter langkah 55 sampai 61):

  | Filter | Cara isi | Hasil |
  |---|---|---|
  | Action | pilih `Edit` pada `Action` | 5 baris |
  | Field | pilih `Status` pada `Field` | 6 baris |
  | Device Name | pilih `Reader Lama` pada `Device Name` | 1 baris |
  | Modified By | pilih nama lengkap `Sari Dewi` pada `Modified By` | 4 baris |
  | Date | isi rentang `17/06/26` s.d. `19/06/26` pada `Date` | 3 baris (kedua batas termasuk) |

- Tabel "Kasus Sort Modal Changelog" (parameter langkah 72 sampai 77):

  | Kolom | Ascending, baris 1 | Descending, baris 1 |
  |---|---|---|
  | `Date` | `15/06/26` (Reader Lama) | `23/06/26` |
  | `Action` | `Activate` terbaru (`22/06/26` Honeywell CK65 - 1) | `Edit` terbaru (`23/06/26`) |
  | `Device Name` | `Chainway C72 - 1` | `Zebra RFID Reader - 1 (SKU-HHR-01)` |
  | `Field` | `Alias Name` | `Status` terbaru (`23/06/26`) |
  | `Old Value` | tiga baris `—` (Activate) di akhir | tiga baris `—` (Activate) di awal |
  | `New Value` | baris `—` (Delete) di akhir | baris `—` (Delete) di awal |
  | `Modified By` | `Budi S` terbaru (`23/06/26`) | `Sari D` terbaru (`20/06/26`) |

- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor (termasuk akun Client E) dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pembacaan Modal Changelog (baris, kolom, empty state, opsi dropdown filter), pengisian rentang tanggal pada Filter Date, pemulihan Seed Changelog Client A lewat fixture backend.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-HHR-326 dan TC-GS-HHR-327: Screening Modal Changelog dan isi baris

1. Klik ikon Changelog
2. Verifikasi Header menampilkan Judul `Changelog: Handheld Reader`
3. Verifikasi Header menampilkan ikon `[✕]`
4. Verifikasi Table Tools menampilkan `Search`, `Filter`, `Download`
5. Verifikasi kolom tabel berurutan: `Date`, `Action`, `Device Name`, `Field`, `Old Value`, `New Value`, `Modified By`, `Column Visibility (⋯)`
6. Verifikasi tujuh kolom `Date`, `Action`, `Device Name`, `Field`, `Old Value`, `New Value`, `Modified By` sortable
7. Verifikasi kolom `Column Visibility (⋯)` tidak sortable
8. Klik header kolom `Column Visibility (⋯)`
9. Verifikasi overlay Column Visibility terbuka
10. Tutup overlay Column Visibility dengan klik di luar overlay
11. Verifikasi tabel menampilkan 9 baris
12. Verifikasi baris pertama berdasarkan `Date` terbaru adalah `23/06/26`
13. Verifikasi Footer menampilkan pagination dengan ukuran halaman default 10 per halaman
14. Verifikasi baris `23/06/26 08:50`: Action `Edit`, Device Name `Gudang Reader - 2 (SKU-HHR-03)`, Field `Status`, Old Value `Available`, New Value `Missing`, Modified By `Budi S`
15. Verifikasi baris `22/06/26 10:00`: Action `Activate`, Device Name `Honeywell CK65 - 1`, Field `Status`, Old Value `—`, New Value `Available`, Modified By `Budi S`
16. Verifikasi baris `21/06/26 08:00`: Action `Activate`, Device Name `Zebra RFID Reader - 1 (SKU-HHR-01)`, Field `Status`, Old Value `—`, New Value `Available`, Modified By `Budi S`
17. Verifikasi baris `20/06/26 11:10`: Action `Activate`, Device Name `Chainway C72 - 1`, Field `Status`, Old Value `—`, New Value `Waiting for Approval`, Modified By `Sari D`
18. Verifikasi baris `19/06/26 10:30`: Action `Edit`, Device Name `Reader Gudang 02 (SKU-HHR-03)`, Field `Alias Name`, Old Value `Gudang 02`, New Value `Reader Gudang 02`, Modified By `Sari D`
19. Verifikasi baris `18/06/26 16:20`: Action `Edit`, Device Name `Zebra Mobile Reader - 1 (SKU-HHR-02)`, Field `Reader Power`, Old Value `30 dBm`, New Value `25 dBm`, Modified By `Budi S`
20. Verifikasi baris `17/06/26 09:05`: Action `Edit`, Device Name `Zebra Mobile Reader - 1 (SKU-HHR-02)`, Field `Status`, Old Value `Available`, New Value `Damaged`, Modified By `Sari D`
21. Verifikasi baris `16/06/26 14:40`: Action `Edit`, Device Name `Zebra Mobile Reader - 1 (SKU-HHR-02)`, Field `Status`, Old Value `Damaged`, New Value `Available`, Modified By `Budi S`
22. Verifikasi baris `15/06/26 11:15`: Action `Delete`, Device Name `Reader Lama`, Field `Device Name`, Old Value `Reader Lama`, New Value `—`, Modified By `Sari D`
23. Verifikasi kolom `Action` dan nilai `Status` berupa teks polos, bukan badge

### TC-GS-HHR-330: Search per kolom searchable

Untuk setiap baris tabel "Kasus Search Modal Changelog" (langkah 24 sampai 26):

24. Ketik Search `{Keyword}`, tekan Enter
25. Verifikasi hasil Search sesuai kolom "Hasil" pada baris tabel untuk kolom {Kolom yang dicari}
26. Klik `(←)` pada kotak Search di modal

### TC-GS-HHR-331: Nilai tanggal tidak dicari lewat Search

27. Ketik Search `21/06/26`, tekan Enter
28. Verifikasi empty state `No results found` tampil (kolom `Date` tidak searchable)
29. Klik `(←)` pada kotak Search di modal

### TC-GS-HHR-329: Search tanpa hasil dan Reset Filters

30. Ketik Search `zzzz`, tekan Enter
31. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
32. Verifikasi tombol `[Reset Filters]` tampil
33. Klik `[Reset Filters]`
34. Verifikasi kotak Search kosong
35. Verifikasi tabel kembali ke halaman 1
36. Verifikasi tabel menampilkan seluruh baris Changelog Client A (9 baris)

### TC-GS-HHR-332 dan TC-GS-HHR-333: Screening Filter Panel dan opsi dropdown

37. Klik ikon Filter di modal
38. Verifikasi field `Date` berupa date range dengan placeholder `Select date`
39. Verifikasi field `Action` dengan placeholder `All actions`
40. Verifikasi field `Device Name` dengan placeholder `All devices`
41. Verifikasi field `Field` dengan placeholder `All fields`
42. Verifikasi field `Modified By` dengan placeholder `All users`
43. Verifikasi kolom `Old Value` dan `New Value` tidak punya field filter
44. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil
45. Buka dropdown `Action`
46. Verifikasi opsi `Action`: `Activate`, `Edit`, `Delete`
47. Tutup dropdown `Action`
48. Buka dropdown `Device Name`
49. Verifikasi dropdown `Device Name` memuat 7 opsi: `Gudang Reader - 2 (SKU-HHR-03)`, `Honeywell CK65 - 1`, `Zebra RFID Reader - 1 (SKU-HHR-01)`, `Chainway C72 - 1`, `Reader Gudang 02 (SKU-HHR-03)`, `Zebra Mobile Reader - 1 (SKU-HHR-02)` (nama dengan SKU sebagai snapshot), dan `Reader Lama` (tanpa SKU)
50. Tutup dropdown `Device Name`
51. Buka dropdown `Field`
52. Verifikasi opsi `Field`: `Status`, `Alias Name`, `Reader Power`, `Device Name`
53. Tutup dropdown `Field`
54. Tutup Filter Panel

### TC-GS-HHR-334: Filter per field

Untuk setiap baris tabel "Kasus Filter Modal Changelog" (langkah 55 sampai 61):

55. Klik ikon Filter di modal
56. Terapkan filter sesuai kolom "Cara isi" pada baris tabel
57. Klik `[Apply]`
58. Verifikasi jumlah baris sesuai kolom "Hasil" pada baris tabel
59. Klik ikon Filter di modal
60. Klik `[Clear Field]`
61. Klik `[Apply]`

### TC-GS-HHR-335: Search dan Filter digabung AND

62. Ketik Search `Zebra`, tekan Enter
63. Klik ikon Filter di modal
64. Pilih `Edit` pada `Action`
65. Klik `[Apply]`
66. Verifikasi tabel menampilkan tepat 3 baris `Zebra Mobile Reader - 1 (SKU-HHR-02)`: Field `Reader Power`, Field `Status` (`Available` ke `Damaged`), dan Field `Status` (`Damaged` ke `Available`)
67. Verifikasi baris Activate `Zebra RFID Reader - 1 (SKU-HHR-01)` tidak tampil
68. Klik `(←)` pada kotak Search di modal
69. Klik ikon Filter di modal
70. Klik `[Clear Field]`
71. Klik `[Apply]`

### TC-GS-HHR-336: Sort 3-state per kolom

Untuk setiap baris tabel "Kasus Sort Modal Changelog" (langkah 72 sampai 77):

72. Klik header kolom {Kolom} satu kali
73. Verifikasi baris tabel diurutkan Ascending pada {Kolom} dengan hasil kolom "Ascending, baris 1" pada baris tabel
74. Klik header kolom {Kolom} kedua kali
75. Verifikasi baris tabel diurutkan Descending pada {Kolom} dengan hasil kolom "Descending, baris 1" pada baris tabel
76. Klik header kolom {Kolom} ketiga kali
77. Verifikasi urutan netral: kembali `Date` terbaru di atas (baris pertama `23/06/26`)

### TC-GS-HHR-328: Empty state Modal Changelog Client E

78. Tutup Modal Changelog dengan `✕`
79. Logout dari akun Total Control Client A
80. Login sebagai Total Control Client E (`Spectra.env.GS_CLIENTE_TC_PASSWORD`)
81. Buka Global Settings > Hardware > Handheld Reader
82. Klik ikon Changelog
83. Verifikasi ilustrasi dengan judul `No changelog yet` dan deskripsi `Activities and changes will appear here.`
84. Verifikasi empty state tanpa tombol aksi

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 4b). Spec hanya membaca; tidak ada data yang dibuat atau dihapus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok menyimpang dari urutan nomor TC: TC-GS-HHR-330, 331, 329 (Search) berurutan; 332 dan 333 (screening Filter dan opsi dropdown) sebelum 334 dan 335; Sort (TC-GS-HHR-336) paling akhir di Client A; TC-GS-HHR-328 (Client E) paling akhir karena ganti akun. Bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal, dan hanya satu kali ganti akun (langkah 79 dan 80).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah menutup overlay Column Visibility, menutup dropdown dan Filter Panel, `(←)` pada Search, `[Clear Field]` lalu `[Apply]` pada akhir tiap kasus Filter dan sesudah TC-GS-HHR-335 (S-09, state dibersihkan sebelum blok berikutnya), menutup Modal Changelog, Logout, Login, dan membuka layar Handheld Reader sesudah ganti akun. Langkah "Klik header kolom `Column Visibility (⋯)`" dan Verifikasi overlay Column Visibility menjalankan klausa Expected TC-GS-HHR-326 "header klik = buka overlay Column Visibility".
- Langkah berulang per baris tabel: Search (langkah 24 sampai 26), Filter (langkah 55 sampai 61), dan Sort (langkah 72 sampai 77); parameter tiap iterasi ada di tabel `## Prerequisites`. Ekspansi: Search 6 iterasi x 3, Filter 5 iterasi x 7, Sort 7 iterasi x 6, sehingga ekspansi total jauh di atas 35 langkah. Alasan spec tetap satu: semua blok berada pada satu kelas (fungsional baca) dan satu dataset (Seed Changelog Client A), tidak ada data yang dibuat atau diubah sehingga tidak ada cleanup, dan kegagalan satu blok (misalnya Sort) tidak membuat blok lain kehilangan makna karena tiap blok memulai dari state yang dibersihkan; kegagalan keras hanya pada pembukaan Modal Changelog (langkah pertama).
- Hasil Search dan Filter diasersi sebagai jumlah baris beserta identitas baris yang disebut Expected TC; jumlah baris yang disebut TC (9, 5, 6, 1, 4, 3) berasal dari Seed Changelog Client A pada `## Prerequisites`, bukan dibaca dari total entri tabel (8b butir 10). Pembanding untuk asersi absence (langkah "baris Activate ... tidak tampil") adalah tiga baris `Zebra Mobile Reader - 1` yang diasersi pada langkah sebelumnya. Empty state `No results found` pada TC-GS-HHR-331 dan 329 sah sebagai anchor positif Search karena Search pada langkah sebelumnya menghasilkan baris.
- Pembagian TC lintas spec: Setup Column Modal Changelog (TC-GS-HHR-292 sampai 305) di spec 056; pagination sekunder (TC-GS-HHR-325) di spec 060; kegagalan unduh Modal Changelog (TC-GS-HHR-339) di spec 028; tutup, Download, dan Tab Changelog Popup Detail (TC-GS-HHR-337, 338, 340 sampai 342, 454, 469, 470) di spec 062.
- Temuan untuk QA:
  - TC-GS-HHR-326 sampai 336 mengasersi jumlah baris absolut (9 baris seed) dan nilai seed, padahal audit trail permanen dan aksi spec lain menambah entri Changelog Client A (S-12). Spec mengandalkan pemulihan Seed Changelog Client A lewat fixture backend yang tidak didefinisikan di TC, PRD, atau LLD; mekanismenya disediakan tim FE/BE.
  - Email akun Total Control Client E dan nilai `{namaClient}` tidak tertulis di Pre-setup TC; spec memakai pola `totalControl_automated_{namaClient}@qwertysystem.net` dari fixture dan nama env password baru `GS_CLIENTE_TC_PASSWORD` yang belum tentu terdaftar di `spectra.config.ts` dan `.env.example` (diusulkan ke owner suite).
  - TC-GS-HHR-329 Expected b menyebut "seluruh Filter" dikosongkan, tetapi langkah TC hanya memakai Search; spec mengasersi kotak Search kosong, halaman 1, dan 9 baris tanpa asersi state Filter terpisah.
  - TC-GS-HHR-330 menulis keyword `SKU-HHR-02` sebagai pencarian pada "Device Name dan SKU", padahal Modal Changelog tidak punya kolom SKU terpisah (SKU hanya muncul sebagai bagian snapshot Device Name); spec mengasersi 3 baris `Zebra Mobile Reader - 1`.
  - TC-GS-HHR-336 butir e dan f ("di akhir saat Ascending", "di awal saat Descending") tidak menyebut apakah urutan sekunder antar baris `—` ditentukan; spec mengasersi posisi kelompok baris `—`, bukan urutan di dalam kelompok.
  - TC-GS-HHR-336 butir h ("Klik ketiga: netral") dibaca berlaku untuk setiap kolom; spec mengasersi urutan netral sesudah klik ketiga pada tiap kolom.
  - TC-GS-HHR-333 Expected b menyebut "7 opsi" tanpa daftar utuh; spec menurunkan tujuh nama dari Seed Changelog Client A.
  - Cara menutup Filter Panel dan dropdown tidak dinyatakan di TC; spec menulis langkah penghubung generik "Tutup".
  - TC-GS-HHR-326 Expected c ("Pagination default 10 per halaman") tidak menyebut teks footer; spec mengasersi ukuran halaman default 10.

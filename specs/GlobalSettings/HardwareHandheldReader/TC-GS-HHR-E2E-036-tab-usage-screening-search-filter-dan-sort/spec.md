---
id: TC-GS-HHR-E2E-036-tab-usage-screening-search-filter-dan-sort
title: "Tab Usage Popup Detail: Screening, Isi Baris, Badge Product, Search, Filter Panel, Sort 3-State, serta Empty State"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-169
  - TC-GS-HHR-170
  - TC-GS-HHR-171
  - TC-GS-HHR-172
  - TC-GS-HHR-173
  - TC-GS-HHR-174
  - TC-GS-HHR-175
  - TC-GS-HHR-176
  - TC-GS-HHR-177
  - TC-GS-HHR-178
coverage:
  web: automated
---

# Tab Usage Popup Detail: Screening, Isi Baris, Badge Product, Search, Filter Panel, Sort 3-State, serta Empty State

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec hanya membaca Seed Reader A dan Seed Usage Event; tidak ada unduhan file (Download Tab Usage, TC-GS-HHR-183, ada di spec 058).
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader (Client A); spec tidak mengulang pembukaan layar.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup, Client A, plan Growth). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Seed Reader A, dipulihkan fixture backend; pengecualian S-12 Population Seed Reader A HHR): Seed Reader A (DD-01 sampai DD-10; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`) dan Seed Usage Event DD-01 UE-01 sampai UE-06 (fixture baru `Fixture.hardwareHandheldReader.seedUsageDd01`), format tanggal default Client A `dd/MM/yy` 24-hour. DD-01 (`Zebra RFID Reader - 1`, Serial Number `SN-HHR-00101`) memiliki enam Usage Event seed bertanggal `16/06/26` sampai `21/06/26` dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji sort, search, dan filter (Product `Fixed Asset` dan `Global Settings`; Event Type enam nilai; PIC `Budi S` dan `Sari D`; Date enam nilai berbeda). DD-04 (`Gudang Reader - 2`) adalah reader tanpa Usage Event. Seed bernama literal tanpa suffix karena asersi bergantung pada nilai dan urutan seed, dan Device Name bawaan ditentukan sistem (HHR-LOGIC-02g); DD-01 dan DD-06 sama-sama bernama `Zebra RFID Reader - 1` sehingga baris diidentifikasi lewat Serial Number. Mekanisme seeding Usage Event disediakan tim FE/BE (lihat Temuan untuk QA).
- Aturan baca seed Tab Usage (S-12): Seed Usage Event dibuat fixture backend dengan `Date` Juni 2026 dan tidak dipulihkan; Tab Usage tidak dibaca sebagai total absolut. Baris seed dikenali lewat `Date` `16/06/26` sampai `21/06/26` (UE-01 sampai UE-06). Jumlah baris tab dicatat sebagai baseline N0 sebelum Search atau Filter lalu dibandingkan terhadap N0; baris seed dicari lewat Filter `Date` pada rentang seed (inklusif kedua ujung, bekerja pada seluruh data di server); posisi "baris pertama" hanya dibaca pada tab yang dibatasi Filter `Date` seed.
- Kemampuan teknis: pemilih rentang tanggal pada Filter Panel (nilai `Date` pada langkah ditulis dalam format tampil `dd/MM/yy`; input date picker memakai format `MM/dd/yyyy`, mis. `06/16/2026`, dan dipilih lewat date picker; perilaku date picker belum diverifikasi di UI); membaca jumlah baris tab (N0) lewat kemampuan baca yang disediakan tim FE/BE (8b butir 10); membaca severity badge `Product`; klik header kolom berulang untuk sort 3-state.
- Reader DD-04 tanpa Usage Event pada awal spec (TC-GS-HHR-172, langkah 95 sampai 99): tim FE/BE menyediakan kemampuan reset tingkat reader yang mengembalikan Tab Usage DD-04 ke kosong (lihat Temuan untuk QA).
- Cleanup: Seed Reader A dipulihkan fixture backend sebelum spec (hook `before`) dan sesudah spec (hook `after`); spec tidak mengubah reader, dan Seed Usage Event tidak dipulihkan karena hanya dibaca. Mekanisme disediakan tim FE/BE.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-HHR-169: Screening Tab Usage

1. Klik `Device Name` baris DD-01 (Serial Number `SN-HHR-00101`)
2. Verifikasi tab `Usage` aktif
3. Catat jumlah baris tab sebagai baseline N0 TC-GS-HHR-169
4. Verifikasi Header menampilkan tab `Usage` (aktif) dan `Changelog`
5. Verifikasi Table Tools `Search`, `Filter`, `Download` tampil
6. Verifikasi kolom tabel `Date`, `Product`, `Event Type`, `Transaction ID`, `PIC`, dan `Column Visibility (⋯)`
7. Verifikasi kolom `Date`, `Product`, `Event Type`, `Transaction ID`, dan `PIC` sortable
8. Verifikasi kolom `Column Visibility (⋯)` unsortable
9. Klik ikon Filter pada tab, isi `Date` rentang `16/06/26` sampai `21/06/26`, klik `[Apply]`
10. Verifikasi baris seed UE-01 sampai UE-06 (`Date` `16/06/26` sampai `21/06/26`) tampil seluruhnya
11. Verifikasi baris diurut `Date` terbaru di atas dengan `21/06/26` paling atas pada hasil Filter
12. Verifikasi tab bersifat read-only: tidak ada tombol atau row action tulis
13. Verifikasi Pagination default 10 per halaman

### TC-GS-HHR-170: Isi baris Tab Usage

14. Verifikasi baris 1 `21/06/26 10:15` | `Fixed Asset` | `Audit Scan` | `TSK-202606-0014` | `Budi S`
15. Verifikasi baris 2 `20/06/26 11:00` | `Fixed Asset` | `Transfer Departure Verify` | `XFER-202606-0007` | `Sari D`
16. Verifikasi baris 3 `19/06/26 09:30` | `Fixed Asset` | `Borrow Verify` | `BRW-202606-0031` | `Sari D`
17. Verifikasi baris 4 `18/06/26 15:45` | `Global Settings` | `Audit TAG` | `—` | `Budi S`
18. Verifikasi baris 5 `17/06/26 13:10` | `Global Settings` | `Pair TAG` | `—` | `Sari D`
19. Verifikasi baris 6 `16/06/26 08:20` | `Global Settings` | `Combine TAG` | `—` | `Sari D`

### TC-GS-HHR-171: Badge Product

20. Verifikasi badge `Fixed Asset` pada kolom `Product` baris 1 (UE-01) memiliki `severity="info"`
21. Verifikasi badge `Global Settings` pada kolom `Product` baris 4 (UE-04) memiliki `severity="secondary"`
22. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-HHR-174: Search per kolom searchable

23. Ketik Search `Fixed Asset`, tekan Enter
24. Verifikasi tabel memuat 3 baris seed (baris ber-`Date` `16/06/26` sampai `21/06/26`): `Audit Scan`, `Transfer Departure Verify`, `Borrow Verify`
25. Klik `(←)` pada kotak Search
26. Ketik Search `pair`, tekan Enter
27. Verifikasi tabel memuat 1 baris seed `Pair TAG`
28. Klik `(←)` pada kotak Search
29. Ketik Search `XFER-2026`, tekan Enter
30. Verifikasi tabel memuat 1 baris seed `Transfer Departure Verify`
31. Klik `(←)` pada kotak Search
32. Ketik Search `Sari`, tekan Enter
33. Verifikasi tabel memuat 4 baris seed: `Transfer Departure Verify`, `Borrow Verify`, `Pair TAG`, `Combine TAG`
34. Klik `(←)` pada kotak Search

### TC-GS-HHR-175: Nilai tanggal tidak dicari lewat Search

35. Ketik Search `21/06/26`, tekan Enter
36. Verifikasi tabel menampilkan empty state `No results found`
37. Klik `(←)` pada kotak Search

### TC-GS-HHR-173: Search tanpa hasil dan Reset Filters

38. Catat jumlah baris tab sebagai baseline N0 TC-GS-HHR-173
39. Ketik Search `zzzz`, tekan Enter
40. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
41. Verifikasi tombol `[Reset Filters]` tampil
42. Klik `[Reset Filters]`
43. Verifikasi kotak Search kosong
44. Verifikasi tabel kembali ke halaman 1
45. Verifikasi jumlah baris Tab Usage DD-01 sama dengan baseline N0 TC-GS-HHR-173

### TC-GS-HHR-176: Screening Filter Panel

46. Klik ikon Filter
47. Verifikasi field `Date` berupa date range dengan placeholder `Select date`
48. Verifikasi field `Product` berupa multi-select searchable dengan placeholder `All products`
49. Verifikasi field `Event Type` dengan placeholder `All event types`
50. Verifikasi field `PIC` dengan placeholder `All users`
51. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil
52. Verifikasi kolom `Transaction ID` tidak punya field filter

### TC-GS-HHR-177: Filter per kelas (multi-select dan date range)

53. Pilih `Product` = `Global Settings`, klik `[Apply]`
54. Verifikasi tabel memuat 3 baris seed: `Audit TAG`, `Pair TAG`, `Combine TAG`
55. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`
56. Buka panel Filter, pilih `Event Type` = `Borrow Verify` dan `Pair TAG`, klik `[Apply]`
57. Verifikasi tabel memuat 2 baris seed (OR dalam satu field): `Borrow Verify`, `Pair TAG`
58. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`
59. Buka panel Filter, pilih `PIC` = `Budi Santoso`, klik `[Apply]`
60. Verifikasi tabel memuat 2 baris seed: `Audit Scan`, `Audit TAG`
61. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`
62. Buka panel Filter, pilih `Date` rentang `17/06/26` sampai `19/06/26`, klik `[Apply]`
63. Verifikasi tabel menampilkan 3 baris inklusif kedua ujung: `Borrow Verify`, `Audit TAG`, `Pair TAG`
64. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-HHR-178: Sort 3-state per kolom

65. Buka panel Filter, isi `Date` rentang `16/06/26` sampai `21/06/26`, klik `[Apply]` (tab dibatasi ke baris seed UE-01 sampai UE-06)
66. Klik header `Date` satu kali
67. Verifikasi `Oldest First` dengan baris pertama `16/06/26`
68. Klik header `Date` kedua kali
69. Verifikasi `Newest First` dengan baris pertama `21/06/26`
70. Klik header `Date` ketiga kali
71. Verifikasi sort kembali netral ke urutan default dengan baris pertama `21/06/26` (terbaru di atas)
72. Klik header `Product` satu kali
73. Verifikasi baris pertama `Fixed Asset` (A-Z)
74. Klik header `Product` kedua kali
75. Verifikasi baris pertama `Global Settings`
76. Klik header `Product` ketiga kali
77. Klik header `Event Type` satu kali
78. Verifikasi baris pertama `Audit Scan`
79. Klik header `Event Type` kedua kali
80. Verifikasi baris pertama `Transfer Departure Verify`
81. Klik header `Event Type` ketiga kali
82. Klik header `Transaction ID` satu kali
83. Verifikasi baris pertama `BRW-202606-0031`
84. Verifikasi tiga baris bernilai `—` berada di akhir saat ascending
85. Klik header `Transaction ID` kedua kali
86. Verifikasi tiga baris `—` berada di awal saat descending
87. Verifikasi baris bernilai pertama sesudah tiga baris `—` adalah `XFER-202606-0007`
88. Klik header `Transaction ID` ketiga kali
89. Klik header `PIC` satu kali
90. Verifikasi baris pertama `Budi S`
91. Klik header `PIC` kedua kali
92. Verifikasi baris pertama `Sari D`
93. Klik header `PIC` ketiga kali
94. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-HHR-172: Empty state Tab Usage untuk reader yang belum pernah dipakai

95. Klik `[✕]`
96. Klik `Device Name` baris DD-04 (`Gudang Reader - 2`)
97. Verifikasi tab `Usage` aktif
98. Verifikasi ilustrasi dengan judul `No usage yet` dan deskripsi `Scans and transactions using this reader will appear here.`
99. Verifikasi tidak ada tombol aksi pada empty state

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pengecualian S-12 Population Seed Reader A HHR (A-5): Seed Reader A dan Seed Usage Event DD-01 bernama dan bernilai literal tanpa suffix; Seed Reader A dipulihkan fixture backend yang disediakan tim FE/BE di hook `before` dan `after`, dinyatakan di `suite.md` dan Prerequisites; suite serial. Total entri Seed Usage Event tidak diasersi absolut: spec memakai N0, baris seed, dan Filter `Date` seed.
- Urutan TC dalam spec: 169, 170, 171, 174, 175, 173, 176, 177, 178, 172. Urutan menyimpang dari urutan TC sumber: screening dan isi baris di awal; Search sebelum Filter dan Sort; TC-GS-HHR-172 memakai reader lain (DD-04) sehingga ditaruh terakhir sesudah popup DD-01 ditutup. TC-GS-HHR-175 mendahului TC-GS-HHR-173 supaya Search `21/06/26` ditutup lewat `(←)` sebelum Search `zzzz`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 25, 28, 31, 34, 37 (menutup input Search lewat `(←)` dan mereset tabel); langkah 22, 55, 58, 61, 64, 94 (`[Clear Field]` lalu `[Apply]` sebelum Search atau filter berikutnya dan di akhir blok Sort); langkah 56, 59, 62 (membuka panel Filter); langkah 65 (Filter `Date` seed yang membatasi tab untuk sort, S-14); langkah 76, 81, 88, 93 (klik ketiga yang mengembalikan sort ke netral sebelum kolom berikutnya, S-09); dan langkah 95 (menutup popup DD-01).
- Langkah pencatatan baseline (aksi tanpa `Verifikasi`): langkah 3 (N0 TC-GS-HHR-169, sebelum Filter) dan langkah 38 (N0 TC-GS-HHR-173, sesudah Filter dibersihkan dan Search dikosongkan). N0 tidak diasersi sebagai angka absolut; TC-GS-HHR-169 b.ii menyatakan hanya N0 sedikitnya 6.
- Asersi universal "tabel memuat N baris seed" memakai nama baris spesifik hasil Search, Filter, atau sort dari seed (butir 2: baris spesifik dijamin tampil oleh Search atau Filter yang dipakai); langkah 10 dan 14 sampai 19 menunjukkan tabel tidak kosong sebelum Search dan Filter lain.
- Baris "pertama" pada langkah 11, 67, 69, 71, 73, 75, 78, 80, 83, 87, 90, dan 92 dibaca pada tab yang dibatasi Filter `Date` seed (langkah 9 dan 65), sehingga hanya di antara baris seed UE-01 sampai UE-06 (S-14).
- Langkah 2 dan 97 (`Pastikan Tab Usage aktif` pada Langkah TC) ditulis sebagai `Verifikasi` tab `Usage` aktif.
- Spec memuat 99 langkah, di atas sekitar 35 langkah (blok berulang per kolom pada langkah 66 sampai 93 dan per keyword pada langkah 23 sampai 34). Seluruhnya satu dataset dan satu kelas fungsional (Tab Usage DD-01: Search, Filter, Sort berbagi dataset yang sama, prinsip 1); langkah per kolom dan per keyword memakai parameter tetap dari Data Uji TC tanpa langkah bersyarat. Tiap blok memulai dari state bersih (Search dikosongkan lewat `(←)`, Filter dibersihkan lewat `[Clear Field]` dan `[Apply]`, sort dikembalikan netral lewat klik ketiga), sehingga kegagalan satu blok tidak mengubah makna blok lain, kecuali kegagalan keras pada pembukaan Popup Detail atau tab `Usage`.
- Pembagian TC lintas spec: TC-GS-HHR-163 sampai 168, 472, dan 489 ada di spec 035; TC-GS-HHR-179 sampai 182 ada di spec 037; TC-GS-HHR-183 (Download Tab Usage: nama berkas, tanpa toast sukses, isi berkas CSV dan XLSX) ada di spec 058; TC-GS-HHR-184 ada di spec 028; TC-GS-HHR-185 dan 186 ada di spec 038; TC-GS-HHR-312 dan 314 (isi file daftar utama) ada di spec 058.
- Temuan untuk QA:
  - TC-GS-HHR-172 mengasersi nol absolut pada Tab Usage DD-04 (reader belum pernah dipakai), sehingga tidak dapat ditulis relatif terhadap baseline. Spec mengandalkan kemampuan reset tingkat reader yang disediakan tim FE/BE (Tab Usage DD-04 kosong pada awal spec). Risiko urutan: TC-GS-HHR-185 dan 187 menulis Usage Event DD-04 di spec 038 dan 065; DD-04 aman bila urutan eksekusi suite serial mengikuti nomor spec (spec 038 dan 065 bernomor di atas 036), tetapi `suite.md` belum menyatakan urutan itu dan belum ada keputusan FE/BE.
  - TC-GS-HHR-173 Expected b ("mengosongkan Search dan seluruh Filter") tidak mengaktifkan Filter sebelum `[Reset Filters]`; spec hanya mengasersi Search kosong dan tabel kembali ke halaman 1 dengan jumlah baris sama dengan N0, sehingga bagian "seluruh Filter" tidak teramati.
  - TC-GS-HHR-177 tidak menyebut apakah Filter Panel menutup sesudah `[Apply]`; spec menulis "Buka panel Filter" sebelum tiap penerapan berikutnya.
  - TC-GS-HHR-177 memakai `PIC` nama lengkap `Budi Santoso` pada filter sedangkan kolom tabel menampilkan `Budi S` (NC-18); spec mengikuti TC.
  - TC-GS-HHR-178 hanya menyebut hasil klik 1 dan 2 untuk `Product`, `Event Type`, `Transaction ID`, dan `PIC`; klik ketiga ditulis sebagai langkah penghubung tanpa `Verifikasi` untuk mengembalikan sort netral (state netral hanya diasersi pada `Date`).
  - TC-GS-HHR-169 Expected b.i menyebut kolom `Column Visibility (⋯)` sebagai kolom `unsortable`; spec mengasersi kolom tersebut tampil dan tidak sortable.
  - TC-GS-HHR-169 dan 173 menyebut "jumlah baris tab" sebagai baseline N0 tanpa menyatakan cara membacanya (halaman 1 hanya menampilkan sampai 10 baris); spec menuliskannya sebagai kemampuan baca yang disediakan tim FE/BE.
  - Mekanisme seeding Usage Event (UE-01 sampai UE-06 untuk DD-01, bertanggal Juni 2026), pemulihan Seed Reader A, dan reset tingkat reader untuk DD-04 tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - Tidak ada Post Condition pada TC sumber spec ini.

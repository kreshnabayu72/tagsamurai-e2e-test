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
- Kemampuan teknis: pemilih rentang tanggal pada Filter Panel (nilai `Date` pada langkah ditulis dalam format tampil `dd/MM/yy`; input date picker memakai format `MM/dd/yyyy`, mis. `06/16/2026`, dan dipilih lewat date picker; perilaku date picker belum diverifikasi di UI); membaca jumlah baris tab (N0) lewat kemampuan baca yang disediakan tim FE/BE (8b butir 10); Filter `Date` server-side dan inklusif kedua ujung (rentang seed dibatasi di server, bukan per halaman); membaca severity badge `Product`; klik header kolom berulang untuk sort 3-state.
- Reader DD-04 tanpa Usage Event pada awal spec (TC-GS-HHR-172, langkah 98 sampai 102; pengecualian A-6): tim FE/BE menyediakan kemampuan reset tingkat reader yang mengembalikan Tab Usage DD-04 ke kosong (lihat Temuan untuk QA).
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

### TC-GS-HHR-174: Search per kolom searchable

22. Ketik Search `Fixed Asset`, tekan Enter
23. Verifikasi tabel memuat 3 baris seed (baris ber-`Date` `16/06/26` sampai `21/06/26`, tab masih dibatasi Filter `Date` seed dari langkah 9): `Audit Scan`, `Transfer Departure Verify`, `Borrow Verify`
24. Klik `(←)` pada kotak Search
25. Ketik Search `pair`, tekan Enter
26. Verifikasi tabel memuat 1 baris seed `Pair TAG`
27. Klik `(←)` pada kotak Search
28. Ketik Search `XFER-2026`, tekan Enter
29. Verifikasi tabel memuat 1 baris seed `Transfer Departure Verify`
30. Klik `(←)` pada kotak Search
31. Ketik Search `Sari`, tekan Enter
32. Verifikasi tabel memuat 4 baris seed: `Transfer Departure Verify`, `Borrow Verify`, `Pair TAG`, `Combine TAG`
33. Klik `(←)` pada kotak Search

### TC-GS-HHR-175: Nilai tanggal tidak dicari lewat Search

34. Ketik Search `21/06/26`, tekan Enter
35. Verifikasi tabel menampilkan empty state `No results found`
36. Klik `(←)` pada kotak Search
37. Klik `[Clear Field]` pada panel Filter yang masih terbuka, lalu klik `[Apply]`
38. Klik ikon Filter untuk menutup panel Filter

### TC-GS-HHR-173: Search tanpa hasil dan Reset Filters

39. Catat jumlah baris tab sebagai baseline N0 TC-GS-HHR-173
40. Ketik Search `zzzz`, tekan Enter
41. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
42. Verifikasi tombol `[Reset Filters]` tampil
43. Klik `[Reset Filters]`
44. Verifikasi kotak Search kosong
45. Verifikasi tabel kembali ke halaman 1
46. Verifikasi jumlah baris Tab Usage DD-01 sama dengan baseline N0 TC-GS-HHR-173

### TC-GS-HHR-176: Screening Filter Panel

47. Klik ikon Filter
48. Verifikasi field `Date` berupa date range dengan placeholder `Select date`
49. Verifikasi field `Product` berupa multi-select searchable dengan placeholder `All products`
50. Verifikasi field `Event Type` dengan placeholder `All event types`
51. Verifikasi field `PIC` dengan placeholder `All users`
52. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil
53. Verifikasi kolom `Transaction ID` tidak punya field filter

### TC-GS-HHR-177: Filter per kelas (multi-select dan date range)

54. Pilih `Product` = `Global Settings` dan isi `Date` rentang `16/06/26` sampai `21/06/26`, klik `[Apply]`
55. Verifikasi tabel memuat 3 baris seed: `Audit TAG`, `Pair TAG`, `Combine TAG`
56. Klik `[Clear Field]` pada panel Filter yang masih terbuka, lalu klik `[Apply]`
57. Pilih `Event Type` = `Borrow Verify` dan `Pair TAG` dan isi `Date` rentang `16/06/26` sampai `21/06/26`, klik `[Apply]`
58. Verifikasi tabel memuat 2 baris seed (OR dalam satu field): `Borrow Verify`, `Pair TAG`
59. Klik `[Clear Field]` pada panel Filter yang masih terbuka, lalu klik `[Apply]`
60. Pilih `PIC` = `Budi Santoso` dan isi `Date` rentang `16/06/26` sampai `21/06/26`, klik `[Apply]`
61. Verifikasi tabel memuat 2 baris seed: `Audit Scan`, `Audit TAG`
62. Klik `[Clear Field]` pada panel Filter yang masih terbuka, lalu klik `[Apply]`
63. Pilih `Date` rentang `17/06/26` sampai `19/06/26`, klik `[Apply]`
64. Verifikasi tabel menampilkan 3 baris inklusif kedua ujung: `Borrow Verify`, `Audit TAG`, `Pair TAG`
65. Klik `[Clear Field]` pada panel Filter yang masih terbuka, lalu klik `[Apply]`
66. Klik ikon Filter untuk menutup panel Filter

### TC-GS-HHR-178: Sort 3-state per kolom

67. Klik ikon Filter untuk membuka panel, isi `Date` rentang `16/06/26` sampai `21/06/26`, klik `[Apply]` (tab dibatasi ke baris seed UE-01 sampai UE-06)
68. Klik header `Date` satu kali
69. Verifikasi `Oldest First` dengan baris pertama `16/06/26`
70. Klik header `Date` kedua kali
71. Verifikasi `Newest First` dengan baris pertama `21/06/26`
72. Klik header `Date` ketiga kali
73. Verifikasi sort kembali netral ke urutan default dengan baris pertama `21/06/26` (terbaru di atas)
74. Klik header `Product` satu kali
75. Verifikasi baris pertama `Fixed Asset` (A-Z)
76. Klik header `Product` kedua kali
77. Verifikasi baris pertama `Global Settings`
78. Klik header `Product` ketiga kali
79. Klik header `Event Type` satu kali
80. Verifikasi baris pertama `Audit Scan`
81. Klik header `Event Type` kedua kali
82. Verifikasi baris pertama `Transfer Departure Verify`
83. Klik header `Event Type` ketiga kali
84. Klik header `Transaction ID` satu kali
85. Verifikasi baris pertama `BRW-202606-0031`
86. Verifikasi tiga baris bernilai `—` berada di akhir saat ascending
87. Klik header `Transaction ID` kedua kali
88. Verifikasi tiga baris `—` berada di awal saat descending
89. Verifikasi baris bernilai pertama sesudah tiga baris `—` adalah `XFER-202606-0007`
90. Klik header `Transaction ID` ketiga kali
91. Klik header `PIC` satu kali
92. Verifikasi baris pertama `Budi S`
93. Klik header `PIC` kedua kali
94. Verifikasi baris pertama `Sari D`
95. Klik header `PIC` ketiga kali
96. Klik `[Clear Field]` pada panel Filter yang masih terbuka, lalu klik `[Apply]`
97. Klik ikon Filter untuk menutup panel Filter

### TC-GS-HHR-172: Empty state Tab Usage untuk reader yang belum pernah dipakai

98. Klik `[✕]`
99. Klik `Device Name` baris DD-04 (`Gudang Reader - 2`)
100. Verifikasi tab `Usage` aktif
101. Verifikasi ilustrasi dengan judul `No usage yet` dan deskripsi `Scans and transactions using this reader will appear here.`
102. Verifikasi tidak ada tombol aksi pada empty state

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pengecualian S-12 Population Seed Reader A HHR (A-5): Seed Reader A dan Seed Usage Event DD-01 bernama dan bernilai literal tanpa suffix; Seed Reader A dipulihkan fixture backend yang disediakan tim FE/BE di hook `before` dan `after`, dinyatakan di `suite.md` dan Prerequisites; suite serial. Total entri Seed Usage Event tidak diasersi absolut: spec memakai N0, baris seed, dan Filter `Date` seed.
- Pengecualian S-12 A-6 (empty state entitas bersih): TC-GS-HHR-172 mengasersi empty state Tab Usage DD-04 (nol baris tanpa baseline, karena empty state tidak dapat relatif). DD-04 ditulis spec lain (038 dan 065), sehingga keadaan kosong dijamin reset tingkat reader yang disediakan tim FE/BE dan dinyatakan di `suite.md` dan Prerequisites; suite serial; hitungan sesudah aksi tetap selisih terhadap baseline.
- Model Filter Panel (PRD dan TC-GS-HHR-177 Langkah 3): panel tetap terbuka sesudah `[Apply]` dan ditutup dengan klik ikon Filter; panel dibuka pada langkah 9, 47, dan 67 dan ditutup pada langkah 38, 66, dan 97. Panel yang dibuka pada langkah 9 tetap terbuka (Filter `Date` seed tetap aktif) melewati blok Search langkah 22 sampai 36 sampai langkah 38; panel yang dibuka pada langkah 47 (screening) tetap terbuka melewati blok TC-GS-HHR-177 sampai langkah 66.
- Batas Filter `Date` ditambahkan spec (S-14, `[KEPUTUSAN 2026-11-02]`), bukan langkah TC: blok Search (langkah 22 sampai 36) memakai Filter `Date` `16/06/26` sampai `21/06/26` dari langkah 9, dan Filter `Product`, `Event Type`, `PIC` non-Date (langkah 54, 57, 60) diisi bersama `Date` yang sama, sehingga baris seed dibaca pada hasil yang dibatasi di server dan tidak bergantung pada halaman. QA perlu mengonfirmasi bahwa batas ini tidak mengubah maksud TC-GS-HHR-174 dan 177 (kombinasi Date dengan Search atau Filter lain tidak dinyatakan TC).
- Urutan TC dalam spec: 169, 170, 171, 174, 175, 173, 176, 177, 178, 172. Urutan menyimpang dari urutan TC sumber: screening dan isi baris di awal; Search sebelum Filter dan Sort; TC-GS-HHR-172 memakai reader lain (DD-04) sehingga ditaruh terakhir sesudah popup DD-01 ditutup. TC-GS-HHR-175 mendahului TC-GS-HHR-173 supaya Search `21/06/26` ditutup lewat `(←)` sebelum Search `zzzz`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 24, 27, 30, 33, 36 (menutup input Search lewat `(←)` dan mereset tabel); langkah 37, 56, 59, 62, 65, 96 (`[Clear Field]` lalu `[Apply]` pada panel Filter yang masih terbuka, sebelum Search atau filter berikutnya dan di akhir blok Sort); langkah 38, 66, 97 (menutup panel Filter lewat klik ikon Filter); langkah 67 (Filter `Date` seed yang membatasi tab untuk sort, S-14); langkah 78, 83, 90, 95 (klik ketiga yang mengembalikan sort ke netral sebelum kolom berikutnya, S-09); dan langkah 98 (menutup popup DD-01).
- Langkah pencatatan baseline (aksi tanpa `Verifikasi`): langkah 3 (N0 TC-GS-HHR-169, sebelum Filter) dan langkah 39 (N0 TC-GS-HHR-173, sesudah Filter dibersihkan dan Search dikosongkan). N0 tidak diasersi sebagai angka absolut; TC-GS-HHR-169 b.ii menyatakan hanya N0 sedikitnya 6.
- Asersi universal "tabel memuat N baris seed" memakai nama baris spesifik hasil Search, Filter, atau sort dari seed (butir 2: baris spesifik dijamin tampil oleh Search atau Filter yang dipakai); langkah 10 dan 14 sampai 19 menunjukkan tabel tidak kosong sebelum Search dan Filter lain.
- Baris "pertama" pada langkah 11, 69, 71, 73, 75, 77, 80, 82, 85, 89, 92, dan 94 dibaca pada tab yang dibatasi Filter `Date` seed (langkah 9 dan 67), sehingga hanya di antara baris seed UE-01 sampai UE-06 (S-14).
- Langkah 2 dan 100 (`Pastikan Tab Usage aktif` pada Langkah TC) ditulis sebagai `Verifikasi` tab `Usage` aktif.
- Spec memuat 102 langkah, di atas sekitar 35 langkah (blok berulang per kolom pada langkah 68 sampai 95 dan per keyword pada langkah 22 sampai 33). Seluruhnya satu dataset dan satu kelas fungsional (Tab Usage DD-01: Search, Filter, Sort berbagi dataset yang sama, prinsip 1); langkah per kolom dan per keyword memakai parameter tetap dari Data Uji TC tanpa langkah bersyarat. Tiap blok memulai dari state bersih (Search dikosongkan lewat `(←)`, Filter dibersihkan lewat `[Clear Field]` dan `[Apply]`, sort dikembalikan netral lewat klik ketiga), sehingga kegagalan satu blok tidak mengubah makna blok lain, kecuali kegagalan keras pada pembukaan Popup Detail atau tab `Usage`.
- Pembagian TC lintas spec: TC-GS-HHR-163 sampai 168, 472, dan 489 ada di spec 035; TC-GS-HHR-179 sampai 182 ada di spec 037; TC-GS-HHR-183 (Download Tab Usage: nama berkas, tanpa toast sukses, isi berkas CSV dan XLSX) ada di spec 058; TC-GS-HHR-184 ada di spec 028; TC-GS-HHR-185 dan 186 ada di spec 038; TC-GS-HHR-312 dan 314 (isi file daftar utama) ada di spec 058.
- Temuan untuk QA:
  - TC-GS-HHR-172 mengasersi nol absolut pada Tab Usage DD-04 (reader belum pernah dipakai), sehingga tidak dapat ditulis relatif terhadap baseline (pengecualian A-6). Spec mengandalkan kemampuan reset tingkat reader yang disediakan tim FE/BE (Tab Usage DD-04 kosong pada awal spec) dan dinyatakan di `suite.md`. TC-GS-HHR-185 dan 187 menulis Usage Event DD-04 di spec 038 dan 065, sehingga keadaan kosong bergantung pada reset itu, bukan pada urutan eksekusi.
  - TC-GS-HHR-173 Expected b ("mengosongkan Search dan seluruh Filter") tidak mengaktifkan Filter sebelum `[Reset Filters]`; spec hanya mengasersi Search kosong dan tabel kembali ke halaman 1 dengan jumlah baris sama dengan N0, sehingga bagian "seluruh Filter" tidak teramati.
  - TC-GS-HHR-177 memakai `PIC` nama lengkap `Budi Santoso` pada filter sedangkan kolom tabel menampilkan `Budi S` (NC-18); spec mengikuti TC.
  - TC-GS-HHR-178 hanya menyebut hasil klik 1 dan 2 untuk `Product`, `Event Type`, `Transaction ID`, dan `PIC`; klik ketiga ditulis sebagai langkah penghubung tanpa `Verifikasi` untuk mengembalikan sort netral (state netral hanya diasersi pada `Date`).
  - TC-GS-HHR-169 Expected b.i menyebut kolom `Column Visibility (⋯)` sebagai kolom `unsortable`; spec mengasersi kolom tersebut tampil dan tidak sortable.
  - TC-GS-HHR-169 dan 173 menyebut "jumlah baris tab" sebagai baseline N0 tanpa menyatakan cara membacanya (halaman 1 hanya menampilkan sampai 10 baris); spec menuliskannya sebagai kemampuan baca yang disediakan tim FE/BE.
  - Mekanisme seeding Usage Event (UE-01 sampai UE-06 untuk DD-01, bertanggal Juni 2026), pemulihan Seed Reader A, dan reset tingkat reader untuk DD-04 tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - Tidak ada Post Condition pada TC sumber spec ini.

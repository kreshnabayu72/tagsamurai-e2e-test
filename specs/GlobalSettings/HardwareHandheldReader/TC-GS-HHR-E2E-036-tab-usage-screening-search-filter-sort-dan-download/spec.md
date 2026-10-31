---
id: TC-GS-HHR-E2E-036-tab-usage-screening-search-filter-sort-dan-download
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
- Suite serial (`parallel: false`): spec hanya membaca Seed Reader A dan Seed Usage Event; tidak ada unduhan file (Download Tab Usage, TC-GS-HHR-183, dipindah ke spec 058).
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader (Client A); spec tidak mengulang pembukaan layar.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup, Client A, plan Growth). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis: Seed Reader A (DD-01 sampai DD-10; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`) dan Seed Usage Event DD-01 UE-01 sampai UE-06 (fixture baru `Fixture.hardwareHandheldReader.seedUsageDd01`), format tanggal default Client A `dd/MM/yy` 24-hour. DD-01 (`Zebra RFID Reader - 1`, Serial Number `SN-HHR-00101`) memiliki enam Usage Event dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji sort, search, dan filter (Product `Fixed Asset` dan `Global Settings`; Event Type enam nilai; PIC `Budi S` dan `Sari D`; Date enam nilai berbeda). DD-04 (`Gudang Reader - 2`) adalah reader tanpa Usage Event. Seed bernama literal tanpa suffix karena asersi bergantung pada nilai dan urutan seed, dan Device Name bawaan ditentukan sistem (HHR-LOGIC-02g); DD-01 dan DD-06 sama-sama bernama `Zebra RFID Reader - 1` sehingga baris diidentifikasi lewat Serial Number. Mekanisme seeding Usage Event disediakan tim FE/BE (lihat Temuan untuk QA).
- Cleanup: Seed Reader A dan Seed Usage Event tidak diubah spec ini; fixture backend memulihkannya ke kondisi awal sebelum spec (hook `before`) dan sesudah spec (hook `after`). Mekanisme pemulihan disediakan tim FE/BE.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: pemilih rentang tanggal pada Filter Panel; membaca severity badge `Product`; klik header kolom berulang untuk sort 3-state.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-HHR-169: Screening Tab Usage

1. Klik `Device Name` baris DD-01 (Serial Number `SN-HHR-00101`)
2. Verifikasi tab `Usage` aktif
3. Verifikasi Header menampilkan tab `Usage` (aktif) dan `Changelog`
4. Verifikasi Table Tools `Search`, `Filter`, `Download` tampil
5. Verifikasi kolom tabel `Date`, `Product`, `Event Type`, `Transaction ID`, `PIC`, dan `Column Visibility (⋯)`
6. Verifikasi kolom `Date`, `Product`, `Event Type`, `Transaction ID`, dan `PIC` sortable, dan kolom `Column Visibility (⋯)` unsortable
7. Verifikasi 6 baris tampil
8. Verifikasi baris diurut `Date` terbaru di atas dengan `21/06/26` paling atas
9. Verifikasi tab bersifat read-only: tidak ada tombol atau row action tulis
10. Verifikasi Pagination default 10 per halaman

### TC-GS-HHR-170: Isi baris Tab Usage

11. Verifikasi baris 1 `21/06/26 10:15` | `Fixed Asset` | `Audit Scan` | `TSK-202606-0014` | `Budi S`
12. Verifikasi baris 2 `20/06/26 11:00` | `Fixed Asset` | `Transfer Departure Verify` | `XFER-202606-0007` | `Sari D`
13. Verifikasi baris 3 `19/06/26 09:30` | `Fixed Asset` | `Borrow Verify` | `BRW-202606-0031` | `Sari D`
14. Verifikasi baris 4 `18/06/26 15:45` | `Global Settings` | `Audit TAG` | `—` | `Budi S`
15. Verifikasi baris 5 `17/06/26 13:10` | `Global Settings` | `Pair TAG` | `—` | `Sari D`
16. Verifikasi baris 6 `16/06/26 08:20` | `Global Settings` | `Combine TAG` | `—` | `Sari D`

### TC-GS-HHR-171: Badge Product

17. Verifikasi badge `Fixed Asset` pada kolom `Product` baris 1 memiliki `severity="info"`
18. Verifikasi badge `Global Settings` pada kolom `Product` baris 4 memiliki `severity="secondary"`

### TC-GS-HHR-174: Search per kolom searchable

19. Ketik Search `Fixed Asset`, tekan Enter
20. Verifikasi tabel menampilkan 3 baris: `Audit Scan`, `Transfer Departure Verify`, `Borrow Verify`
21. Klik `(←)` pada kotak Search
22. Ketik Search `pair`, tekan Enter
23. Verifikasi tabel menampilkan 1 baris `Pair TAG`
24. Klik `(←)` pada kotak Search
25. Ketik Search `XFER-2026`, tekan Enter
26. Verifikasi tabel menampilkan 1 baris `Transfer Departure Verify`
27. Klik `(←)` pada kotak Search
28. Ketik Search `Sari`, tekan Enter
29. Verifikasi tabel menampilkan 4 baris: `Transfer Departure Verify`, `Borrow Verify`, `Pair TAG`, `Combine TAG`
30. Klik `(←)` pada kotak Search

### TC-GS-HHR-175: Nilai tanggal tidak dicari lewat Search

31. Ketik Search `21/06/26`, tekan Enter
32. Verifikasi tabel menampilkan empty state `No results found`
33. Klik `(←)` pada kotak Search

### TC-GS-HHR-173: Search tanpa hasil dan Reset Filters

34. Ketik Search `zzzz`, tekan Enter
35. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
36. Verifikasi tombol `[Reset Filters]` tampil
37. Klik `[Reset Filters]`
38. Verifikasi kotak Search kosong
39. Verifikasi tabel kembali ke halaman 1 dengan 6 baris Tab Usage DD-01

### TC-GS-HHR-176: Screening Filter Panel

40. Klik ikon Filter
41. Verifikasi field `Date` berupa date range dengan placeholder `Select date`
42. Verifikasi field `Product` berupa multi-select searchable dengan placeholder `All products`
43. Verifikasi field `Event Type` dengan placeholder `All event types`
44. Verifikasi field `PIC` dengan placeholder `All users`
45. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil
46. Verifikasi kolom `Transaction ID` tidak punya field filter

### TC-GS-HHR-177: Filter per kelas (multi-select dan date range)

47. Pilih `Product` = `Global Settings`, klik `[Apply]`
48. Verifikasi tabel menampilkan 3 baris: `Audit TAG`, `Pair TAG`, `Combine TAG`
49. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`
50. Buka panel Filter, pilih `Event Type` = `Borrow Verify` dan `Pair TAG`, klik `[Apply]`
51. Verifikasi tabel menampilkan 2 baris (OR dalam satu field): `Borrow Verify`, `Pair TAG`
52. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`
53. Buka panel Filter, pilih `PIC` = `Budi Santoso`, klik `[Apply]`
54. Verifikasi tabel menampilkan 2 baris: `Audit Scan`, `Audit TAG`
55. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`
56. Buka panel Filter, pilih `Date` rentang `17/06/26` sampai `19/06/26`, klik `[Apply]`
57. Verifikasi tabel menampilkan 3 baris inklusif kedua ujung: `Borrow Verify`, `Audit TAG`, `Pair TAG`
58. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-HHR-178: Sort 3-state per kolom

59. Klik header `Date` satu kali
60. Verifikasi `Oldest First` dengan baris pertama `16/06/26`
61. Klik header `Date` kedua kali
62. Verifikasi `Newest First` dengan baris pertama `21/06/26`
63. Klik header `Date` ketiga kali
64. Verifikasi sort kembali netral ke urutan default dengan baris pertama `21/06/26` (terbaru di atas)
65. Klik header `Product` satu kali
66. Verifikasi baris pertama `Fixed Asset` (A-Z)
67. Klik header `Product` kedua kali
68. Verifikasi baris pertama `Global Settings`
69. Klik header `Product` ketiga kali
70. Klik header `Event Type` satu kali
71. Verifikasi baris pertama `Audit Scan`
72. Klik header `Event Type` kedua kali
73. Verifikasi baris pertama `Transfer Departure Verify`
74. Klik header `Event Type` ketiga kali
75. Klik header `Transaction ID` satu kali
76. Verifikasi baris pertama `BRW-202606-0031`
77. Verifikasi tiga baris bernilai `—` berada di akhir saat ascending
78. Klik header `Transaction ID` kedua kali
79. Verifikasi tiga baris `—` berada di awal saat descending
80. Verifikasi baris bernilai pertama sesudah tiga baris `—` adalah `XFER-202606-0007`
81. Klik header `Transaction ID` ketiga kali
82. Klik header `PIC` satu kali
83. Verifikasi baris pertama `Budi S`
84. Klik header `PIC` kedua kali
85. Verifikasi baris pertama `Sari D`
86. Klik header `PIC` ketiga kali

### TC-GS-HHR-172: Empty state Tab Usage untuk reader yang belum pernah dipakai

87. Klik `[✕]`
88. Klik `Device Name` baris DD-04 (`Gudang Reader - 2`)
89. Verifikasi tab `Usage` aktif
90. Verifikasi ilustrasi dengan judul `No usage yet`
91. Verifikasi deskripsi `Scans and transactions using this reader will appear here.`
92. Verifikasi tidak ada tombol aksi pada empty state

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 169, 170, 171, 174, 175, 173, 176, 177, 178, 172. Urutan menyimpang dari urutan TC sumber: screening dan isi baris di awal; Search sebelum Filter dan Sort; TC-GS-HHR-172 memakai reader lain (DD-04) sehingga ditaruh terakhir sesudah popup DD-01 ditutup. TC-GS-HHR-175 mendahului TC-GS-HHR-173 supaya Search `21/06/26` ditutup lewat `(←)` sebelum Search `zzzz`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 21, 24, 27, 30, 33 (menutup input Search lewat `(←)` dan mereset tabel), langkah 49, 52, 55, 58 (`[Clear Field]` lalu `[Apply]` sebelum filter berikutnya; langkah 58 membersihkan filter terakhir), langkah 50, 53, 56 (membuka panel Filter), langkah 69, 74, 81, 86 (klik ketiga yang mengembalikan sort ke netral sebelum kolom berikutnya, S-09), dan langkah 87 (menutup popup DD-01).
- Asersi universal "tabel menampilkan N baris" memakai nama baris spesifik hasil Search, Filter, atau sort dari seed (butir 2: baris spesifik dijamin tampil oleh Search atau Filter yang dipakai); langkah 7 dan 11 sampai 16 menunjukkan tabel tidak kosong sebelum Search dan Filter.
- Langkah 2 dan 89 (`Pastikan Tab Usage aktif` pada Langkah TC) ditulis sebagai `Verifikasi` tab `Usage` aktif.
- Spec melewati sekitar 35 langkah (92 langkah, termasuk blok berulang per kolom pada langkah 59 sampai 86 dan per keyword pada langkah 19 sampai 30). Seluruhnya satu dataset dan satu kelas fungsional (Tab Usage DD-01: Search, Filter, Sort berbagi dataset yang sama, prinsip 1); langkah per kolom dan per keyword memakai parameter tetap dari Data Uji TC tanpa langkah bersyarat. Tiap blok memulai dari state bersih (Search dikosongkan lewat `(←)`, Filter dibersihkan lewat `[Clear Field]` dan `[Apply]`, sort dikembalikan netral lewat klik ketiga), sehingga kegagalan satu blok tidak mengubah makna blok lain, kecuali kegagalan keras pada pembukaan Popup Detail atau tab `Usage`.
- Pembagian TC lintas spec: TC-GS-HHR-163 sampai 168, 472, dan 489 ada di spec 035; TC-GS-HHR-179 sampai 182 ada di spec 037; TC-GS-HHR-183 (Download Tab Usage: nama berkas, tanpa toast sukses, isi berkas CSV dan XLSX) dipindah seluruhnya ke spec 058 (kelas isi berkas, keputusan user 2026-10-30); TC-GS-HHR-184 ada di spec 028; TC-GS-HHR-185 dan 186 ada di spec 038; TC-GS-HHR-312 dan 314 (isi file daftar utama) ada di spec 058.
- Temuan untuk QA:
  - TC-GS-HHR-183 (Download Tab Usage, termasuk Expected c isi berkas kelas f) dipindah seluruhnya ke spec 058 sesuai keputusan user 2026-10-30; TC-183 punya klausa fungsional (nama berkas, tanpa toast) dan klausa isi berkas sehingga satu rumah terbersih adalah spec 058. `id` spec ini masih memuat kata `download` dari penamaan awal; folder tidak diubah.
  - TC-GS-HHR-173 Expected b ("mengosongkan Search dan seluruh Filter") tidak mengaktifkan Filter sebelum `[Reset Filters]`; spec hanya mengasersi Search kosong dan tabel kembali ke halaman 1 dengan 6 baris, sehingga bagian "seluruh Filter" tidak teramati.
  - TC-GS-HHR-177 tidak menyebut apakah Filter Panel menutup sesudah `[Apply]`; spec menulis "Buka panel Filter" sebelum tiap penerapan berikutnya.
  - TC-GS-HHR-177 memakai `PIC` nama lengkap `Budi Santoso` pada filter sedangkan kolom tabel menampilkan `Budi S` (NC-18); spec mengikuti TC.
  - TC-GS-HHR-178 hanya menyebut hasil klik 1 dan 2 untuk `Product`, `Event Type`, `Transaction ID`, dan `PIC`; klik ketiga ditulis sebagai langkah penghubung tanpa `Verifikasi` untuk mengembalikan sort netral (state netral hanya diasersi pada `Date`).
  - TC-GS-HHR-169 Expected b.i menyebut kolom `Column Visibility (⋯)` sebagai kolom `unsortable`; spec mengasersi kolom tersebut tampil dan tidak sortable.
  - Mekanisme seeding Usage Event (UE-01 sampai UE-06 untuk DD-01) dan pemulihan Seed Reader A tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - Tidak ada Post Condition pada TC sumber spec ini.

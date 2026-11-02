---
id: TC-GS-HHR-E2E-066-event-log-activate-popup-screening-search-filter-sort
title: "Popup Event Log Activate: Screening, Isi Baris, Search, Filter, Sort 3-State, Download, dan Empty State Client E"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-356
  - TC-GS-HHR-357
  - TC-GS-HHR-358
  - TC-GS-HHR-359
  - TC-GS-HHR-360
  - TC-GS-HHR-361
  - TC-GS-HHR-362
  - TC-GS-HHR-363
coverage:
  web: automated
---

# Popup Event Log Activate: Screening, Isi Baris, Search, Filter, Sort 3-State, Download, dan Empty State Client E

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini hanya membaca Popup Event Log Activate dan mengunduh berkas; asersi bergantung pada lima baris seed EL-01 sampai EL-05 yang dibaca lewat `Date`, bukan pada total isi Event Log.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` membuka layar lagi hanya sesudah ganti akun.
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Akun kedua (TC-GS-HHR-358, langkah 77): Total Control Client E, `totalControl_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Client E belum memiliki sesi aktivasi. Hook `after` mengembalikan sesi ke akun default suite (Client A).
- Data Pre-setup: Client A plan Growth, Seed Reader A (`Fixture.hardwareHandheldReader.seedReaderA`) dipakai sebagai precondition TC, tidak diasersi. Format tanggal `dd/MM/yy` 24-hour Asia/Jakarta.
- Seed Event Log Client A (EL-01 s.d. EL-05; fixture baru `Fixture.hardwareHandheldReader.seedEventLogClientA`), dibuat fixture backend dengan `Date` Juni 2026 (`11/06/26` s.d. `21/06/26`), urut Date terbaru di atas saat ditampilkan:

  | ID | Date | Range Type | Device Name | Result | PIC |
  |---|---|---|---|---|---|
  | EL-01 | 21/06/26 08:00 | Long Range | Zebra RFID Reader - 1 (SKU-HHR-01) | Activated | Budi S |
  | EL-02 | 20/06/26 11:10 | Long Range | Chainway C72 - 1 | Waiting for Approval | Sari D |
  | EL-03 | 19/06/26 09:05 | Short Range | — | Failed | Budi S |
  | EL-05 | 17/06/26 14:20 | Long Range | — | Failed | Sari D |
  | EL-04 | 11/06/26 08:30 | Short Range | Gudang Reader - 1 (SKU-HHR-03) | Activated | Sari D |

  Nilai distinct pada tiap kolom yang diuji Search, Filter, dan Sort tersedia pada seed (S-11).
- Aturan baca seed Event Log (S-12): audit trail permanen tidak dipulihkan ke seed dan spec aktivasi lain menambah baris Event Log Client A bertanggal waktu aksi (Okt 2026), di luar rentang seed. Jumlah baris dicatat sebagai baseline N0 sebelum Search atau Filter; kembali ke tabel penuh dibandingkan terhadap N0 (tidak terhadap 5). "N baris" pada hasil Search dan Filter berarti N baris seed (baris ber-`Date` `11/06/26` s.d. `21/06/26`) yang cocok; baris non-seed tidak diasersi jumlahnya. "Baris pertama" dan urutan hanya dibaca pada tabel yang dibatasi Filter `Date` `11/06/26` s.d. `21/06/26`. Filter `Date` bekerja pada seluruh data di server dan inklusif kedua ujung.
- Tabel "Kasus Search Popup Event Log" (parameter langkah 41 sampai 44):

  | Keyword | Kolom yang dicari | Hasil |
  |---|---|---|
  | `Long` | Range Type | 3 baris seed EL-01, EL-02, EL-05 |
  | `Chainway` | Device Name | 1 baris seed EL-02 |
  | `failed` | Result | 2 baris seed EL-03, EL-05 |
  | `Sari` | PIC | 3 baris seed EL-02, EL-04, EL-05 |
  | `21/06/26` | Date | `No results found` (kolom `Date` tidak searchable) |

- Tabel "Kasus Filter Popup Event Log" (parameter langkah 52 sampai 58):

  | Filter | Cara isi | Hasil |
  |---|---|---|
  | Result | pilih `Failed` pada `Result` | 2 baris seed EL-03, EL-05 |
  | Range Type | pilih `Short Range` pada `Range Type` | 2 baris seed EL-03, EL-04 |
  | Date | isi rentang `19/06/26` s.d. `20/06/26` pada `Date` | 2 baris EL-02, EL-03 (kedua batas termasuk) |
  | PIC | pilih nama lengkap `Budi Santoso` pada `PIC` | 2 baris seed EL-01, EL-03 |

- Tabel "Kasus Sort Popup Event Log" (parameter langkah 60 sampai 65; dibaca pada tabel yang dibatasi Filter `Date` seed, langkah 59):

  | Kolom | Ascending, baris 1 | Descending, baris 1 |
  |---|---|---|
  | `Date` | `11/06/26 08:30` | `21/06/26 08:00` |
  | `Range Type` | `Long Range` terbaru (`21/06/26 08:00`) | `Short Range` terbaru (`19/06/26 09:05`) |
  | `Device Name` | `Chainway C72 - 1`, dua baris `—` di akhir | dua baris `—` di awal |
  | `Result` | `Activated` terbaru | `Waiting for Approval` |
  | `PIC` | `Budi S` terbaru (`21/06/26 08:00`) | `Sari D` terbaru (`20/06/26 11:10`) |

- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor (termasuk akun Client E) dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pembacaan Popup Event Log Activate (baris, kolom, badge `severity`, empty state, placeholder, opsi dropdown filter); pembacaan jumlah baris Event Log (N0) yang disediakan tim FE/BE (8b butir 10); pengisian rentang tanggal pada Filter Date (nilai `Date` pada langkah ditulis dalam format tampil `dd/MM/yy`; input date picker memakai format `MM/dd/yyyy`, mis. `06/11/2026`, dan dipilih lewat date picker; perilaku date picker belum diverifikasi di UI); pembuatan Seed Event Log bertanggal Juni 2026 oleh fixture backend; pembaca berkas unduhan (nama berkas).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-HHR-356 dan TC-GS-HHR-357: Screening Popup Event Log Activate dan isi baris

1. Klik ikon Event Log
2. Catat jumlah baris Event Log sebagai baseline N0 TC-GS-HHR-356
3. Verifikasi Judul popup `Activate`
4. Verifikasi ikon `[✕]` tampil di Header
5. Verifikasi Table Tools menampilkan `Search`, `Filter`, `Download`
6. Verifikasi placeholder Search `Search device name, PIC...`
7. Verifikasi kolom tabel berurutan: `Date`, `Range Type`, `Device Name`, `Result`, `PIC`, `Column Visibility (⋯)`
8. Verifikasi kolom `Date`, `Range Type`, `Device Name`, `Result`, `PIC` sortable
9. Verifikasi kolom `Column Visibility (⋯)` tidak sortable
10. Klik header kolom `Column Visibility (⋯)`
11. Verifikasi overlay Column Visibility terbuka
12. Tutup overlay Column Visibility dengan klik di luar overlay
13. Klik ikon Filter di popup, isi `Date` rentang `11/06/26` sampai `21/06/26`, klik `[Apply]`
14. Verifikasi baris seed EL-01 sampai EL-05 (`Date` `11/06/26` sampai `21/06/26`) tampil seluruhnya
15. Verifikasi tabel urut `Date` terbaru di atas
16. Verifikasi popup read-only tanpa row action tulis
17. Verifikasi Footer menampilkan pagination dengan ukuran halaman default 10 per halaman
18. Verifikasi baris `21/06/26 08:00`: Range Type `Long Range`, Device Name `Zebra RFID Reader - 1 (SKU-HHR-01)`, Result `Activated`, PIC `Budi S`
19. Verifikasi baris `20/06/26 11:10`: Range Type `Long Range`, Device Name `Chainway C72 - 1`, Result `Waiting for Approval`, PIC `Sari D`
20. Verifikasi baris `19/06/26 09:05`: Range Type `Short Range`, Device Name `—`, Result `Failed`, PIC `Budi S`
21. Verifikasi baris `17/06/26 14:20`: Range Type `Long Range`, Device Name `—`, Result `Failed`, PIC `Sari D`
22. Verifikasi baris `11/06/26 08:30`: Range Type `Short Range`, Device Name `Gudang Reader - 1 (SKU-HHR-03)`, Result `Activated`, PIC `Sari D`
23. Verifikasi badge `Result` `Activated` memakai `severity="success"`
24. Verifikasi badge `Result` `Waiting for Approval` memakai `severity="warning"`
25. Verifikasi badge `Result` `Failed` memakai `severity="danger"`
26. Verifikasi badge `Range Type` `Short Range` memakai `severity="primary"`
27. Verifikasi badge `Range Type` `Long Range` memakai `severity="dark"`
28. Klik ikon Filter di popup, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-HHR-359: Search tanpa hasil dan Reset Filters

29. Catat jumlah baris Event Log sebagai baseline N0 TC-GS-HHR-359
30. Klik ikon Filter di popup
31. Pilih `Activated` pada `Result`
32. Klik `[Apply]`
33. Ketik Search `zzzz`, tekan Enter
34. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
35. Verifikasi tombol `[Reset Filters]` tampil
36. Klik `[Reset Filters]`
37. Verifikasi kotak Search kosong
38. Verifikasi ikon Filter tanpa titik indikator
39. Verifikasi tabel kembali ke halaman 1
40. Verifikasi jumlah baris Event Log sama dengan baseline N0 TC-GS-HHR-359 (seluruh baris Event Log Client A)

### TC-GS-HHR-360: Search per kolom searchable

Untuk setiap baris tabel "Kasus Search Popup Event Log" (langkah 41 sampai 44):

41. Ketik Search `{Keyword}`, tekan Enter
42. Verifikasi hasil Search sesuai kolom "Hasil" pada baris tabel untuk kolom {Kolom yang dicari}
43. Verifikasi setiap baris yang tampil memuat `{Keyword}` pada kolom {Kolom yang dicari}
44. Klik `(←)` pada kotak Search di popup

### TC-GS-HHR-361: Filter Popup Event Log Activate

45. Klik ikon Filter di popup
46. Verifikasi field `Date` dengan placeholder `Select date`
47. Verifikasi field `Range Type` dengan placeholder `All range types`
48. Verifikasi field `Result` dengan placeholder `All results`
49. Verifikasi field `PIC` dengan placeholder `All users`
50. Verifikasi kolom `Device Name` tidak punya field filter
51. Tutup Filter Panel

Untuk setiap baris tabel "Kasus Filter Popup Event Log" (langkah 52 sampai 58):

52. Klik ikon Filter di popup
53. Terapkan filter sesuai kolom "Cara isi" pada baris tabel
54. Klik `[Apply]`
55. Verifikasi baris seed sesuai kolom "Hasil" pada baris tabel
56. Klik ikon Filter di popup
57. Klik `[Clear Field]`
58. Klik `[Apply]`

### TC-GS-HHR-362: Sort 3-state per kolom

59. Klik ikon Filter di popup, isi `Date` rentang `11/06/26` sampai `21/06/26`, klik `[Apply]` (tabel dibatasi ke baris seed EL-01 sampai EL-05)

Untuk setiap baris tabel "Kasus Sort Popup Event Log" (langkah 60 sampai 65):

60. Klik header kolom {Kolom} satu kali
61. Verifikasi baris tabel diurutkan Ascending pada {Kolom} dengan hasil kolom "Ascending, baris 1" pada baris tabel
62. Klik header kolom {Kolom} kedua kali
63. Verifikasi baris tabel diurutkan Descending pada {Kolom} dengan hasil kolom "Descending, baris 1" pada baris tabel
64. Klik header kolom {Kolom} ketiga kali
65. Verifikasi urutan netral: kembali `Date` terbaru di atas (baris pertama `21/06/26 08:00`)

66. Klik ikon Filter di popup, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-HHR-363: Download Popup Event Log Activate

67. Klik ikon Download di popup
68. Klik `Download as CSV`
69. Verifikasi tidak ada toast sukses
70. Verifikasi berkas `Handheld-Reader-Activate-Log.csv` terunduh
71. Klik ikon Download di popup
72. Klik `Download as XLSX`
73. Verifikasi tidak ada toast sukses
74. Verifikasi berkas `Handheld-Reader-Activate-Log.xlsx` terunduh

### TC-GS-HHR-358: Empty state Popup Event Log Activate Client E

75. Tutup Popup Event Log Activate dengan `✕`
76. Logout dari akun Total Control Client A
77. Login sebagai Total Control Client E (`Spectra.env.GS_CLIENTE_TC_PASSWORD`)
78. Buka Global Settings > Hardware > Handheld Reader
79. Klik ikon Event Log
80. Verifikasi ilustrasi dengan judul `No activation log yet` dan deskripsi `Activation sessions will appear here.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 5b). Spec hanya membaca dan mengunduh; tidak ada data yang dibuat atau dihapus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pengecualian S-12 Population Seed Reader A HHR (A-5): Seed Reader A dan Seed Event Log Client A bernama dan bernilai literal tanpa suffix; Seed Reader A dipulihkan fixture backend yang disediakan tim FE/BE di hook `before` dan `after`, dinyatakan di `suite.md` dan Prerequisites; suite serial. Total entri Seed Event Log tidak diasersi absolut: spec memakai N0, baris seed, dan Filter `Date` seed.
- Urutan blok menyimpang dari urutan nomor TC: Search (359, 360) mendahului Filter (361) dan Sort (362); Download (363) sebelum TC-GS-HHR-358 yang paling akhir karena ganti akun ke Client E (langkah 76 dan 77); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal. Popup Event Log dibuka satu kali di Client A dan tetap terbuka sepanjang blok, ditutup sebelum Logout.
- Langkah penghubung (aksi tanpa `Verifikasi`): pencatatan baseline N0 (langkah 2 dan 29, sebelum Filter atau Search dipasang); menutup overlay Column Visibility dan Filter Panel (cara menutup Filter Panel tidak dinyatakan di TC); Filter `Date` seed (langkah 13 dan 59) yang membatasi tabel ke baris seed sebelum pembacaan isi, urutan, dan sort (S-14); `[Clear Field]` lalu `[Apply]` sesudah Filter seed (langkah 28 dan 66) dan di akhir tiap kasus Filter (S-09); `(←)` pada Search; menutup popup, Logout, Login, dan membuka layar Handheld Reader sesudah ganti akun. Langkah klik header `Column Visibility (⋯)` dan Verifikasi overlay Column Visibility menjalankan klausa Expected TC-GS-HHR-356 "header klik = buka overlay Column Visibility". N0 TC-GS-HHR-356 tidak diasersi sebagai angka absolut (TC-GS-HHR-356 b.ii menyatakan hanya N0 sedikitnya 5).
- Langkah berulang per baris tabel: Search (langkah 41 sampai 44), Filter (langkah 52 sampai 58), dan Sort (langkah 60 sampai 65); parameter tiap iterasi ada di tabel `## Prerequisites`. Spec memuat 80 langkah nominal dan ekspansi iterasi (Search 5 x 4, Filter 4 x 7, Sort 5 x 6) menambah 61 langkah, jauh di atas sekitar 35 langkah. Alasan spec tetap satu: semua blok fungsional baca pada satu dataset (Seed Event Log Client A) dan satu kelas, tanpa data yang dibuat atau diubah sehingga tidak ada cleanup; tiap blok memulai dari state yang dibersihkan sehingga kegagalan satu blok (misalnya Sort) tidak membuat blok lain kehilangan makna; kegagalan keras hanya pada pembukaan popup (langkah pertama).
- Hasil Search dan Filter diasersi sebagai baris seed yang disebut Expected TC (identitas baris EL-xx) dibaca lewat `Date`; baris non-seed boleh tampil dan jumlahnya tidak diasersi. Langkah 43 (setiap baris yang tampil memuat keyword) menjalankan butir f TC-GS-HHR-360; untuk keyword `21/06/26` hasilnya `No results found` sehingga tidak ada baris yang diperiksa. Empty state `No results found` pada TC-GS-HHR-359 dan baris Search `21/06/26` sah sebagai anchor positif karena Search lain pada blok yang sama menghasilkan baris.
- Pembagian TC lintas spec: Setup Column Popup Event Log Activate (TC-GS-HHR-292 sampai 305) di spec 056; kegagalan unduh Popup Event Log (TC-GS-HHR-339) di spec 028; hover `PIC` Popup Event Log (TC-GS-HHR-469) di spec 062; pencatatan hasil aktivasi (TC-GS-HHR-364 sampai 368) di spec 067 dan spec 026 (TC-GS-HHR-368); kegagalan driver dan penolakan Suspended tanpa baris (TC-GS-HHR-369 dan 370) di spec 065.
- Temuan untuk QA:
  - Mekanisme pembuatan Seed Event Log bertanggal Juni 2026 oleh fixture backend dan pembacaan jumlah baris Event Log (N0) tidak didefinisikan di TC, PRD, atau LLD (disediakan tim FE/BE); N0 dibaca sebelum Search atau Filter dan tidak diasersi absolut.
  - Seed Event Log pada Tabel Data Uji menulis EL-04 `11/06/26` sebelum EL-05 `17/06/26` padahal urutan tampil mengikuti Date; spec memakai urutan tampil di TC-GS-HHR-357.
  - TC-GS-HHR-360 butir e tidak menyebut apakah teks Search `21/06/26` dibandingkan terhadap Date terformat atau nilai mentah; spec mengasersi `No results found`.
  - TC-GS-HHR-362 butir f ("Klik ketiga: netral") dibaca berlaku untuk setiap kolom; spec mengasersi urutan netral sesudah klik ketiga pada tiap kolom.
  - TC-GS-HHR-361 butir a menyebut kolom `Device Name` tidak punya filter; spec mengasersinya sebagai "kolom Device Name tidak punya field filter" sesudah daftar field.
  - TC-GS-HHR-363 tidak menyebut isi berkas; spec hanya mengasersi nama berkas dan tidak adanya toast sukses.

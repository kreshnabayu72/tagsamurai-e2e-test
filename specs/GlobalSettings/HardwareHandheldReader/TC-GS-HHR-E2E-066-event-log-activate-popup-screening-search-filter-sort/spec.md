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
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini hanya membaca Popup Event Log Activate dan mengunduh berkas; isi Seed Event Log Client A harus utuh karena asersi bergantung pada lima baris seed.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` membuka layar lagi hanya sesudah ganti akun.
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Akun kedua (TC-GS-HHR-358, langkah 69): Total Control Client E, email `totalControl_automated_{namaClient}@qwertysystem.net` dengan nilai `{namaClient}` dari fixture `Fixture.hardwareHandheldReader` (fixture baru; nilai tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Client E belum memiliki sesi aktivasi. Hook `after` mengembalikan sesi ke akun default suite (Client A).
- Data Pre-setup: Client A plan Growth, Seed Reader A (`Fixture.hardwareHandheldReader.seedReaderA`) dipakai sebagai precondition TC, tidak diasersi. Format tanggal `dd/MM/yy` 24-hour Asia/Jakarta.
- Seed Event Log Client A (EL-01 s.d. EL-05; fixture `Fixture.hardwareHandheldReader.seedEventLogClientA`), urut Date terbaru di atas saat ditampilkan:

  | ID | Date | Range Type | Device Name | Result | PIC |
  |---|---|---|---|---|---|
  | EL-01 | 21/06/26 08:00 | Long Range | Zebra RFID Reader - 1 (SKU-HHR-01) | Activated | Budi S |
  | EL-02 | 20/06/26 11:10 | Long Range | Chainway C72 - 1 | Waiting for Approval | Sari D |
  | EL-03 | 19/06/26 09:05 | Short Range | — | Failed | Budi S |
  | EL-05 | 17/06/26 14:20 | Long Range | — | Failed | Sari D |
  | EL-04 | 11/06/26 08:30 | Short Range | Gudang Reader - 1 (SKU-HHR-03) | Activated | Sari D |

  Nilai distinct pada tiap kolom yang diuji Search, Filter, dan Sort tersedia pada seed (S-11). Seed Event Log Client A dipulihkan lewat fixture backend di hook `before` dan `after` (kemampuan disediakan tim FE/BE tanpa endpoint yang dikarang; lihat Temuan untuk QA).
- Tabel "Kasus Search Popup Event Log" (parameter langkah 36 sampai 38):

  | Keyword | Kolom yang dicari | Hasil |
  |---|---|---|
  | `Long` | Range Type | 3 baris EL-01, EL-02, EL-05 |
  | `Chainway` | Device Name | 1 baris EL-02 |
  | `failed` | Result | 2 baris EL-03, EL-05 |
  | `Sari` | PIC | 3 baris EL-02, EL-04, EL-05 |
  | `21/06/26` | Date | `No results found` (kolom `Date` tidak searchable) |

- Tabel "Kasus Filter Popup Event Log" (parameter langkah 46 sampai 52):

  | Filter | Cara isi | Hasil |
  |---|---|---|
  | Result | pilih `Failed` pada `Result` | 2 baris |
  | Range Type | pilih `Short Range` pada `Range Type` | 2 baris EL-03, EL-04 |
  | Date | isi rentang `19/06/26` s.d. `20/06/26` pada `Date` | 2 baris EL-02, EL-03 (kedua batas termasuk) |
  | PIC | pilih nama lengkap `Budi Santoso` pada `PIC` | 2 baris EL-01, EL-03 |

- Tabel "Kasus Sort Popup Event Log" (parameter langkah 53 sampai 58):

  | Kolom | Ascending, baris 1 | Descending, baris 1 |
  |---|---|---|
  | `Date` | `11/06/26 08:30` | `21/06/26 08:00` |
  | `Range Type` | `Long Range` terbaru (`21/06/26 08:00`) | `Short Range` terbaru (`19/06/26 09:05`) |
  | `Device Name` | `Chainway C72 - 1`, dua baris `—` di akhir | dua baris `—` di awal |
  | `Result` | `Activated` terbaru | `Waiting for Approval` |
  | `PIC` | `Budi S` terbaru (`21/06/26 08:00`) | `Sari D` terbaru (`20/06/26 11:10`) |

- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor (termasuk akun Client E) dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pembacaan Popup Event Log Activate (baris, kolom, badge `severity`, empty state, placeholder, opsi dropdown filter); pengisian rentang tanggal pada Filter Date; pembaca berkas unduhan (nama berkas); pemulihan Seed Event Log lewat fixture backend.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-HHR-356 dan TC-GS-HHR-357: Screening Popup Event Log Activate dan isi baris

1. Klik ikon Event Log
2. Verifikasi Judul popup `Activate`
3. Verifikasi ikon `[✕]` tampil di Header
4. Verifikasi Table Tools menampilkan `Search`, `Filter`, `Download`
5. Verifikasi placeholder Search `Search device name, PIC...`
6. Verifikasi kolom tabel berurutan: `Date`, `Range Type`, `Device Name`, `Result`, `PIC`, `Column Visibility (⋯)`
7. Verifikasi kolom `Date`, `Range Type`, `Device Name`, `Result`, `PIC` sortable
8. Verifikasi kolom `Column Visibility (⋯)` tidak sortable
9. Klik header kolom `Column Visibility (⋯)`
10. Verifikasi overlay Column Visibility terbuka
11. Tutup overlay Column Visibility dengan klik di luar overlay
12. Verifikasi tabel menampilkan 5 baris urut `Date` terbaru di atas
13. Verifikasi popup read-only tanpa row action tulis
14. Verifikasi Footer menampilkan pagination dengan ukuran halaman default 10 per halaman
15. Verifikasi baris `21/06/26 08:00`: Range Type `Long Range`, Device Name `Zebra RFID Reader - 1 (SKU-HHR-01)`, Result `Activated`, PIC `Budi S`
16. Verifikasi baris `20/06/26 11:10`: Range Type `Long Range`, Device Name `Chainway C72 - 1`, Result `Waiting for Approval`, PIC `Sari D`
17. Verifikasi baris `19/06/26 09:05`: Range Type `Short Range`, Device Name `—`, Result `Failed`, PIC `Budi S`
18. Verifikasi baris `17/06/26 14:20`: Range Type `Long Range`, Device Name `—`, Result `Failed`, PIC `Sari D`
19. Verifikasi baris `11/06/26 08:30`: Range Type `Short Range`, Device Name `Gudang Reader - 1 (SKU-HHR-03)`, Result `Activated`, PIC `Sari D`
20. Verifikasi badge `Result` `Activated` memakai `severity="success"`
21. Verifikasi badge `Result` `Waiting for Approval` memakai `severity="warning"`
22. Verifikasi badge `Result` `Failed` memakai `severity="danger"`
23. Verifikasi badge `Range Type` `Short Range` memakai `severity="primary"`
24. Verifikasi badge `Range Type` `Long Range` memakai `severity="dark"`

### TC-GS-HHR-359: Search tanpa hasil dan Reset Filters

25. Klik ikon Filter di popup
26. Pilih `Activated` pada `Result`
27. Klik `[Apply]`
28. Ketik Search `zzzz`, tekan Enter
29. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
30. Verifikasi tombol `[Reset Filters]` tampil
31. Klik `[Reset Filters]`
32. Verifikasi kotak Search kosong
33. Verifikasi ikon Filter tanpa titik indikator
34. Verifikasi tabel kembali ke halaman 1
35. Verifikasi tabel menampilkan seluruh baris Event Log Client A (5 baris)

### TC-GS-HHR-360: Search per kolom searchable

Untuk setiap baris tabel "Kasus Search Popup Event Log" (langkah 36 sampai 38):

36. Ketik Search `{Keyword}`, tekan Enter
37. Verifikasi hasil Search sesuai kolom "Hasil" pada baris tabel untuk kolom {Kolom yang dicari}
38. Klik `(←)` pada kotak Search di popup

### TC-GS-HHR-361: Filter Popup Event Log Activate

39. Klik ikon Filter di popup
40. Verifikasi field `Date` dengan placeholder `Select date`
41. Verifikasi field `Range Type` dengan placeholder `All range types`
42. Verifikasi field `Result` dengan placeholder `All results`
43. Verifikasi field `PIC` dengan placeholder `All users`
44. Verifikasi kolom `Device Name` tidak punya field filter
45. Tutup Filter Panel

Untuk setiap baris tabel "Kasus Filter Popup Event Log" (langkah 46 sampai 52):

46. Klik ikon Filter di popup
47. Terapkan filter sesuai kolom "Cara isi" pada baris tabel
48. Klik `[Apply]`
49. Verifikasi jumlah baris sesuai kolom "Hasil" pada baris tabel
50. Klik ikon Filter di popup
51. Klik `[Clear Field]`
52. Klik `[Apply]`

### TC-GS-HHR-362: Sort 3-state per kolom

Untuk setiap baris tabel "Kasus Sort Popup Event Log" (langkah 53 sampai 58):

53. Klik header kolom {Kolom} satu kali
54. Verifikasi baris tabel diurutkan Ascending pada {Kolom} dengan hasil kolom "Ascending, baris 1" pada baris tabel
55. Klik header kolom {Kolom} kedua kali
56. Verifikasi baris tabel diurutkan Descending pada {Kolom} dengan hasil kolom "Descending, baris 1" pada baris tabel
57. Klik header kolom {Kolom} ketiga kali
58. Verifikasi urutan netral: kembali `Date` terbaru di atas (baris pertama `21/06/26 08:00`)

### TC-GS-HHR-363: Download Popup Event Log Activate

59. Klik ikon Download di popup
60. Klik `Download as CSV`
61. Verifikasi tidak ada toast sukses
62. Verifikasi berkas `Handheld-Reader-Activate-Log.csv` terunduh
63. Klik ikon Download di popup
64. Klik `Download as XLSX`
65. Verifikasi tidak ada toast sukses
66. Verifikasi berkas `Handheld-Reader-Activate-Log.xlsx` terunduh

### TC-GS-HHR-358: Empty state Popup Event Log Activate Client E

67. Tutup Popup Event Log Activate dengan `✕`
68. Logout dari akun Total Control Client A
69. Login sebagai Total Control Client E (`Spectra.env.GS_CLIENTE_TC_PASSWORD`)
70. Buka Global Settings > Hardware > Handheld Reader
71. Klik ikon Event Log
72. Verifikasi ilustrasi dengan judul `No activation log yet` dan deskripsi `Activation sessions will appear here.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 5b). Spec hanya membaca dan mengunduh; tidak ada data yang dibuat atau dihapus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok menyimpang dari urutan nomor TC: Search (359, 360) mendahului Filter (361) dan Sort (362); Download (363) sebelum TC-GS-HHR-358 yang paling akhir karena ganti akun ke Client E (langkah 68 dan 69); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal. Popup Event Log dibuka satu kali di Client A dan tetap terbuka sepanjang blok, ditutup sebelum Logout.
- Langkah penghubung (aksi tanpa `Verifikasi`): menutup overlay Column Visibility dan Filter Panel (cara menutup Filter Panel tidak dinyatakan di TC), `(←)` pada Search, `[Clear Field]` lalu `[Apply]` di akhir tiap kasus Filter (S-09), menutup popup, Logout, Login, dan membuka layar Handheld Reader sesudah ganti akun. Langkah klik header `Column Visibility (⋯)` dan Verifikasi overlay Column Visibility menjalankan klausa Expected TC-GS-HHR-356 "header klik = buka overlay Column Visibility".
- Langkah berulang per baris tabel: Search (langkah 36 sampai 38), Filter (langkah 46 sampai 52), dan Sort (langkah 53 sampai 58); parameter tiap iterasi ada di tabel `## Prerequisites`. Spec memuat 72 langkah nominal dan ekspansi iterasi (Search 5 x 3, Filter 4 x 7, Sort 5 x 6) menambah 57 langkah, jauh di atas sekitar 35 langkah. Alasan spec tetap satu: semua blok fungsional baca pada satu dataset (Seed Event Log Client A) dan satu kelas, tanpa data yang dibuat atau diubah sehingga tidak ada cleanup; tiap blok memulai dari state yang dibersihkan sehingga kegagalan satu blok (misalnya Sort) tidak membuat blok lain kehilangan makna; kegagalan keras hanya pada pembukaan popup (langkah pertama).
- Hasil Search dan Filter diasersi sebagai jumlah baris beserta identitas baris yang disebut Expected TC; jumlah 5 baris berasal dari Seed Event Log Client A pada `## Prerequisites` (8b butir 10). Empty state `No results found` pada TC-GS-HHR-359 dan baris Search `21/06/26` sah sebagai anchor positif karena Search lain pada blok yang sama menghasilkan baris.
- Pembagian TC lintas spec: Setup Column Popup Event Log Activate (TC-GS-HHR-292 sampai 305) di spec 056; kegagalan unduh Popup Event Log (TC-GS-HHR-339) di spec 028; hover `PIC` Popup Event Log (TC-GS-HHR-469) di spec 062; pencatatan hasil aktivasi (TC-GS-HHR-364 sampai 368) di spec 067 dan spec 026 (TC-GS-HHR-368); kegagalan driver dan penolakan Suspended tanpa baris (TC-GS-HHR-369 dan 370) di spec 065.
- Temuan untuk QA:
  - TC-GS-HHR-356 sampai 363 mengasersi lima baris seed Event Log Client A (jumlah absolut) padahal spec aktivasi lain menambah baris Event Log Client A; spec mengandalkan pemulihan Seed Event Log lewat fixture backend yang tidak didefinisikan di TC, PRD, atau LLD (disediakan tim FE/BE).
  - Seed Event Log pada Tabel Data Uji menulis EL-04 `11/06/26` sebelum EL-05 `17/06/26` padahal urutan tampil mengikuti Date; spec memakai urutan tampil di TC-GS-HHR-357.
  - Email akun Total Control Client E dan nilai `{namaClient}` tidak tertulis di Pre-setup TC; spec memakai pola fixture dan nama env password baru `GS_CLIENTE_TC_PASSWORD` yang diusulkan ke owner suite.
  - TC-GS-HHR-360 butir e tidak menyebut apakah teks Search `21/06/26` dibandingkan terhadap Date terformat atau nilai mentah; spec mengasersi `No results found`.
  - TC-GS-HHR-362 butir f ("Klik ketiga: netral") dibaca berlaku untuk setiap kolom; spec mengasersi urutan netral sesudah klik ketiga pada tiap kolom.
  - TC-GS-HHR-361 butir a menyebut kolom `Device Name` tidak punya filter; spec mengasersinya sebagai "kolom Device Name tidak punya field filter" sesudah daftar field.
  - TC-GS-HHR-363 tidak menyebut isi berkas; spec hanya mengasersi nama berkas dan tidak adanya toast sukses.

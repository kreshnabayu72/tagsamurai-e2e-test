---
id: TC-GS-HHR-E2E-050-search-daftar-reader
title: "Search Daftar Reader Handheld Reader: Siklus Interaksi, Kelas Kolom, Hasil Kosong, Trim, Karakter Khusus, dan Visibilitas Kolom"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-230
  - TC-GS-HHR-231
  - TC-GS-HHR-232
  - TC-GS-HHR-233
  - TC-GS-HHR-234
  - TC-GS-HHR-235
  - TC-GS-HHR-236
  - TC-GS-HHR-237
  - TC-GS-HHR-238
  - TC-GS-HHR-455
  - TC-GS-HHR-476
coverage:
  web: automated
---

# Search Daftar Reader Handheld Reader: Siklus Interaksi, Kelas Kolom, Hasil Kosong, Trim, Karakter Khusus, dan Visibilitas Kolom

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Sari Dewi), Client A, `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; spec tidak mengulang langkah buka di `## Test Steps`.
- Client A: plan Growth, format tanggal default General Settings `dd/MM/yy` 24-hour (tidak diubah spec ini).
- Data Dinamis Seed Reader A (10 reader DD-01 sampai DD-10), dibuat lewat fixture backend sebelum eksekusi (`Fixture.hardwareHandheldReader.seedReaderA`) dan dipulihkan antar TC oleh fixture backend. Nama literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah baris (lihat "Temuan untuk QA"). Spec hanya membaca daftar; tidak ada reader yang dibuat, diubah, atau dihapus. Jumlah baris awal N = 10 diturunkan dari seeding ini, bukan dibaca dari tabel:

| ID | Device Name | Alias Name | Serial Number | SKU | Range Type | Reader Power | Brand | Model/Type | Source | Last Scanned | Last Scanned In | Last User | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DD-01 | Zebra RFID Reader - 1 | — | SN-HHR-00101 | SKU-HHR-01 | Long Range | 30 dBm | Zebra | RFD40 | Official | 21/06/26 10:15 | Fixed Asset | Budi S | Available |
| DD-02 | Gudang Reader - 1 | Reader Gudang 02 | SN-HHR-00102 | SKU-HHR-03 | Short Range | — | Chainway | C66 | Official | 20/06/26 09:40 | Supply | Sari D | Available |
| DD-03 | Zebra Mobile Reader - 1 | — | SN-HHR-00103 | SKU-HHR-02 | Long Range | 25 dBm | Zebra | MC3300R | Official | 17/06/26 16:05 | Global Settings | Sari D | Damaged |
| DD-04 | Gudang Reader - 2 | — | SN-HHR-00104 | SKU-HHR-03 | Short Range | — | Chainway | C66 | Official | — | — | — | Missing |
| DD-05 | Chainway C72 - 1 | — | SN-HHR-00105 | — | Long Range | 30 dBm | Chainway | C72 | Self-Purchased | — | — | — | Waiting for Approval |
| DD-06 | Zebra RFID Reader - 1 | — | SN-HHR-00107 | SKU-HHR-04 | Short Range | — | Zebra | RFD40 | Official | 19/06/26 13:20 | Supply | Sari D | Available |
| DD-07 | Honeywell CK65 - 1 | — | SN-HHR-00108 | — | Long Range | 30 dBm | Honeywell | CK65 | Self-Purchased | — | — | — | Available |
| DD-08 | Unitech EA520 - 1 | — | SN-HHR-00109 | — | Short Range | — | Unitech | — | Self-Purchased | — | — | — | Available |
| DD-09 | International Handheld Terminals Ltd Ultra-Rugged Series 7000 Pro Max - 1 | — | SN-HHR-00110 | — | Long Range | 30 dBm | International Handheld Terminals Ltd | Ultra-Rugged Series 7000 Pro Max | Self-Purchased | — | — | — | Available |
| DD-10 | Gudang Reader - 4 | — | SN-HHR-00205 | SKU-HHR-03 | Short Range | — | Chainway | C66 | Official | — | — | — | Waiting for Approval |

- Kolom curated `Brand`, `Model/Type`, `Last Scanned In`, dan `Last User` tersembunyi pada keadaan awal (TC-GS-HHR-234 mensyaratkan `Model/Type` tersembunyi); kolom `Device Name` dan `Alias Name` tampil. Kolom `Last Scanned` dan `Activated At` bukan kolom yang dicari Search.
- Tabel "Keyword TC-GS-HHR-231" (kolom, keyword, hasil yang diharapkan):

| Keyword | Kolom yang dicocokkan | Hasil |
|---|---|---|
| `Gudang` | Device Name | 3 baris DD-02, DD-04, DD-10 |
| `gudang` (huruf kecil) | Device Name | 3 baris DD-02, DD-04, DD-10 (sama dengan `Gudang`) |
| `Reader Gudang` | Alias Name | 1 baris DD-02 |
| `00105` | Serial Number | 1 baris DD-05 |
| `SKU-HHR-03` | SKU | 3 baris DD-02, DD-04, DD-10 |

- Tabel "Keyword TC-GS-HHR-232":

| Keyword | Kolom yang dicocokkan | Hasil |
|---|---|---|
| `short` | Range Type | 5 baris DD-02, DD-04, DD-06, DD-08, DD-10 |
| `self` | Source | 4 baris DD-05, DD-07, DD-08, DD-09 |
| `damaged` | Status | 1 baris DD-03 |
| `waiting` | Status | 2 baris DD-05, DD-10 |

- Tabel "Keyword TC-GS-HHR-235" (kolom `Device Name` dan `Alias Name` disembunyikan; baris dikenali lewat Serial Number):

| Keyword | Kolom yang dicocokkan | Hasil |
|---|---|---|
| `Zebra` | Brand | 3 baris `SN-HHR-00101` (DD-01), `SN-HHR-00103` (DD-03), `SN-HHR-00107` (DD-06) |
| `MC3300R` | Model/Type | 1 baris `SN-HHR-00103` (DD-03) |
| `Fixed Asset` | Last Scanned In | 1 baris `SN-HHR-00101` (DD-01) |
| `Budi` | Last User | 1 baris `SN-HHR-00101` (DD-01) |

- Kemampuan teknis: pembacaan fokus input, placeholder, nilai input Search (termasuk spasi di depan dan belakang), tooltip hover, dan visibilitas kolom lewat Overlay Column Visibility.
- State yang diubah spec: visibilitas kolom (langkah 54 sampai 67); dipulihkan lewat langkah penghubung pada langkah 67 dan hook `after` cadangan memulihkan Overlay Column Visibility ke bawaan.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` true untuk akun Total Control dan hook `after` memulihkannya (lihat `suite.md`).

## Test Steps

### TC-GS-HHR-230: Siklus interaksi Search box

1. Arahkan kursor ke ikon Search
2. Verifikasi tooltip ikon `Search` tampil
3. Klik ikon Search
4. Verifikasi search bar melebar
5. Verifikasi kursor fokus di input
6. Verifikasi placeholder `Search reader, serial, alias...`
7. Ketik `Gudang` tanpa menekan Enter
8. Verifikasi ikon `(✕)` muncul di search box
9. Verifikasi tabel belum tersaring (10 baris)
10. Tekan `Enter`
11. Verifikasi tabel menampilkan 3 baris `Gudang Reader - 1`, `Gudang Reader - 2`, `Gudang Reader - 4`
12. Klik ikon `(✕)` pada search box
13. Verifikasi teks pada search box terhapus
14. Verifikasi kursor tetap fokus di search box
15. Verifikasi tabel tetap 3 baris
16. Tekan `Enter` pada input kosong
17. Verifikasi tabel kembali 10 baris
18. Ketik Search `Gudang`, tekan Enter
19. Klik ikon panah `(←)` pada search box
20. Verifikasi search bar menutup menjadi ikon Search
21. Verifikasi keyword Search kosong
22. Verifikasi tabel langsung 10 baris

### TC-GS-HHR-231: Search kelas kolom teks (Device Name, Alias Name, Serial Number, SKU)

23. Ketik Search `<Keyword>`, tekan Enter (diulang untuk setiap baris tabel "Keyword TC-GS-HHR-231", langkah 23 sampai 25)
24. Verifikasi tabel menampilkan baris pada kolom Hasil baris tabel yang sama
25. Klik ikon `(←)` pada search box

### TC-GS-HHR-232: Search kelas kolom enum (Range Type, Source, Status)

26. Ketik Search `<Keyword>`, tekan Enter (diulang untuk setiap baris tabel "Keyword TC-GS-HHR-232", langkah 26 sampai 28)
27. Verifikasi tabel menampilkan baris pada kolom Hasil baris tabel yang sama
28. Klik ikon `(←)` pada search box

### TC-GS-HHR-233 dan TC-GS-HHR-476: Search angka Reader Power dan satuan dBm

29. Ketik Search `25`, tekan Enter
30. Verifikasi tabel menampilkan 1 baris DD-03 (`Zebra Mobile Reader - 1`, Reader Power `25 dBm`)
31. Klik ikon `(←)` pada search box
32. Ketik Search `dBm`, tekan Enter
33. Verifikasi empty state `No results found` tampil
34. Ganti isi kotak search dengan `25`, tekan Enter
35. Verifikasi tabel menampilkan 1 baris DD-03 (angka tanpa satuan tetap dapat dicari)
36. Klik ikon `(←)` pada search box

### TC-GS-HHR-236: Nilai tanggal tidak dicari lewat Search

37. Ketik Search `21/06/26`, tekan Enter
38. Verifikasi empty state `No results found` tampil
39. Klik ikon `(←)` pada search box

### TC-GS-HHR-237: Spasi di awal dan akhir keyword dibuang

40. Ketik Search `  Gudang  ` (spasi di awal dan akhir), tekan Enter
41. Verifikasi tabel menampilkan 3 baris `Gudang Reader - 1`, `Gudang Reader - 2`, `Gudang Reader - 4` (sama dengan keyword `Gudang`)
42. Verifikasi teks pada search box tetap `  Gudang  ` apa adanya
43. Klik ikon `(←)` pada search box

### TC-GS-HHR-238: Karakter khusus dicocokkan sebagai teks biasa

44. Ketik Search `<b>%_`, tekan Enter
45. Verifikasi empty state `No results found` tampil
46. Verifikasi tidak ada pesan error yang tampil
47. Verifikasi teks `<b>%_` tampil apa adanya pada search box (tag HTML tidak diinterpretasi)
48. Klik ikon `(←)` pada search box

### TC-GS-HHR-455: Search berisi spasi saja diperlakukan seperti input kosong

49. Ketik Search `Gudang`, tekan Enter
50. Verifikasi tabel menampilkan 3 baris `Gudang Reader - 1`, `Gudang Reader - 2`, `Gudang Reader - 4`
51. Ganti isi kotak search dengan tiga spasi, tekan Enter
52. Verifikasi tabel kembali 10 baris tanpa saringan Search
53. Klik ikon `(←)` pada search box

### TC-GS-HHR-234: Search terikat visibilitas kolom (Model/Type)

54. Ketik Search `RFD40`, tekan Enter
55. Verifikasi empty state `No results found` tampil (kolom `Model/Type` tersembunyi)
56. Klik ikon `(←)` pada search box
57. Aktifkan kolom `Model/Type` lewat Overlay Column Visibility
58. Ketik Search `RFD40`, tekan Enter
59. Verifikasi tabel menampilkan 2 baris DD-01 dan DD-06 (`Zebra RFID Reader - 1` ganda)
60. Klik ikon `(←)` pada search box
61. Nonaktifkan kolom `Model/Type` lewat Overlay Column Visibility

### TC-GS-HHR-235: Search kolom curated yang ditampilkan (Brand, Model/Type, Last Scanned In, Last User)

62. Aktifkan kolom `Brand`, `Model/Type`, `Last Scanned In`, dan `Last User` lewat Overlay Column Visibility
63. Sembunyikan kolom `Device Name` dan `Alias Name` lewat Overlay Column Visibility
64. Ketik Search `<Keyword>`, tekan Enter (diulang untuk setiap baris tabel "Keyword TC-GS-HHR-235", langkah 64 sampai 66)
65. Verifikasi tabel menampilkan baris pada kolom Hasil baris tabel yang sama
66. Klik ikon `(←)` pada search box
67. Aktifkan kolom `Device Name` dan `Alias Name`, nonaktifkan kolom `Brand`, `Model/Type`, `Last Scanned In`, dan `Last User` lewat Overlay Column Visibility (pemulihan keadaan awal)

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 230, 231, 232, 233 dan 476, 236, 237, 238, 455, lalu 234 dan 235. TC-GS-HHR-234 dan 235 mengubah visibilitas kolom sehingga ditaruh paling akhir; TC-GS-HHR-476 digabung ke blok TC-GS-HHR-233 karena Expected 476 merujuk pencarian `25`. Urutan ini menyimpang dari urutan TC sumber.
- Langkah penghubung (aksi tanpa `Verifikasi`): klik `(←)` yang menutup input dan mengosongkan keyword sebelum TC berikutnya (langkah 25, 28, dan klik `(←)` lain tepat sesudah asersi hasil), langkah Nonaktifkan `Model/Type` sesudah TC-GS-HHR-234, dan langkah 67 (pemulihan kolom). Search lain ditulis atomik ("Ketik Search `X`, tekan Enter"); "Klik ikon Search" eksplisit hanya pada siklus TC-GS-HHR-230.
- Langkah yang diulang per baris tabel Prerequisites: langkah 23 sampai 25 (5 iterasi), 26 sampai 28 (4 iterasi), dan 64 sampai 66 (4 iterasi). Tiap iterasi punya satu `Verifikasi` hasil.
- Langkah 30 dan `Verifikasi` empty state `No results found` pada blok TC-GS-HHR-476 menjadi anchor positif untuk asersi hasil kosong. Langkah "angka tanpa satuan tetap dapat dicari" (TC-GS-HHR-476 butir a) ditulis sebagai pencarian `25` ulang di blok yang sama, bukan rujukan ke langkah 30.
- Tidak ada asersi tambahan di luar Expected TC. Langkah "tidak ada pesan error" dan "teks `<b>%_` tampil apa adanya" pada blok TC-GS-HHR-238 adalah cara mengamati klausa Expected "tidak ada error dan tag HTML pada keyword tidak diinterpretasi".
- Spec memuat 67 langkah nominal (sekitar 97 langkah dengan ekspansi blok ulang; di atas smell sekitar 35 langkah). Seluruhnya satu kelas harness (Search daftar reader), satu akun, satu dataset, tanpa aksi yang mengubah data; tiap blok TC dimulai dari search bar tertutup dan tetap bermakna bila blok lain gagal. Blok yang mengubah visibilitas kolom (TC-GS-HHR-234, 235) ada di akhir sehingga kegagalannya tidak menutupi blok sebelumnya.
- Temuan untuk QA:
  - TC-GS-HHR-234: precondition tidak menyatakan bahwa kolom `Model/Type` tersembunyi pada keadaan awal; spec mengasumsikan kolom curated (`Brand`, `Model/Type`, `Last Scanned In`, `Last User`) tersembunyi secara bawaan, sesuai Expected a.
  - TC-GS-HHR-235 langkah 3: "klik ikon Search" disebut per keyword, sedangkan siklus buka-tutup input hanya diuji TC-GS-HHR-230; spec memakai langkah atomik.
  - Seed Reader A bernama literal tanpa suffix `{runId}` karena asersi bergantung pada nama dan jumlah baris (pola pengecualian S-12 untuk Population belum tertulis untuk HHR); fixture backend dan pemulihannya antar TC disediakan tim FE/BE (Catatan TC: seed Seed Reader A dipulihkan antar TC), tanpa mekanisme yang ditulis di TC.
  - TC-GS-HHR-236 tidak mencantumkan deskripsi empty state; spec hanya mengasersi `No results found` sesuai Expected.
  - Post Condition semua TC di spec ini `-`; tidak ada yang diasersi.

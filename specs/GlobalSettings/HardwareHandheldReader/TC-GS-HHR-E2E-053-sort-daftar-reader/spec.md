---
id: TC-GS-HHR-E2E-053-sort-daftar-reader
title: "Sort Daftar Reader Handheld Reader: Siklus 3 Klik, Nilai Kosong, Numerik, Label Badge, Nama Pengguna, Tanggal, dan Kolom Actions"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-269
  - TC-GS-HHR-270
  - TC-GS-HHR-271
  - TC-GS-HHR-272
  - TC-GS-HHR-273
  - TC-GS-HHR-274
  - TC-GS-HHR-275
  - TC-GS-HHR-276
coverage:
  web: automated
---

# Sort Daftar Reader Handheld Reader: Siklus 3 Klik, Nilai Kosong, Numerik, Label Badge, Nama Pengguna, Tanggal, dan Kolom Actions

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Sari Dewi), Client A, `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; spec tidak mengulang langkah buka di `## Test Steps`.
- Client A: plan Growth, format tanggal default General Settings `dd/MM/yy` 24-hour (tidak diubah spec ini). Jam server dan jam browser tidak diatur karena data tanggal berasal dari seeding tetap.
- Data Dinamis Seed Reader A (10 reader DD-01 sampai DD-10), dibuat lewat fixture backend sebelum eksekusi (`Fixture.hardwareHandheldReader.seedReaderA`) dan dipulihkan antar TC oleh fixture backend. Nama dan tanggal literal tanpa suffix `{runId}` karena asersi urutan bergantung pada nilai dan jumlah baris (lihat "Temuan untuk QA"). Spec hanya membaca daftar. Setiap kolom yang diasersi sortnya memuat sedikitnya dua nilai distinct (kolom `Last Scanned` dan `Activated At` berbeda hari, bukan hanya berbeda menit):

| ID | Device Name | Alias Name | Serial Number | SKU | Range Type | Reader Power | Brand | Model/Type | Source | Last Scanned | Last Scanned In | Last User | Activated At | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DD-01 | Zebra RFID Reader - 1 | — | SN-HHR-00101 | SKU-HHR-01 | Long Range | 30 dBm | Zebra | RFD40 | Official | 21/06/26 10:15 | Fixed Asset | Budi S | 21/06/26 08:00 | Available |
| DD-02 | Gudang Reader - 1 | Reader Gudang 02 | SN-HHR-00102 | SKU-HHR-03 | Short Range | — | Chainway | C66 | Official | 20/06/26 09:40 | Supply | Sari D | 11/06/26 08:30 | Available |
| DD-03 | Zebra Mobile Reader - 1 | — | SN-HHR-00103 | SKU-HHR-02 | Long Range | 25 dBm | Zebra | MC3300R | Official | 17/06/26 16:05 | Global Settings | Sari D | 12/06/26 09:00 | Damaged |
| DD-04 | Gudang Reader - 2 | — | SN-HHR-00104 | SKU-HHR-03 | Short Range | — | Chainway | C66 | Official | — | — | — | 01/06/26 07:45 | Missing |
| DD-05 | Chainway C72 - 1 | — | SN-HHR-00105 | — | Long Range | 30 dBm | Chainway | C72 | Self-Purchased | — | — | — | 20/06/26 11:10 | Waiting for Approval |
| DD-06 | Zebra RFID Reader - 1 | — | SN-HHR-00107 | SKU-HHR-04 | Short Range | — | Zebra | RFD40 | Official | 19/06/26 13:20 | Supply | Sari D | 18/06/26 15:30 | Available |
| DD-07 | Honeywell CK65 - 1 | — | SN-HHR-00108 | — | Long Range | 30 dBm | Honeywell | CK65 | Self-Purchased | — | — | — | 22/06/26 10:00 | Available |
| DD-08 | Unitech EA520 - 1 | — | SN-HHR-00109 | — | Short Range | — | Unitech | — | Self-Purchased | — | — | — | 23/06/26 10:30 | Available |
| DD-09 | International Handheld Terminals Ltd Ultra-Rugged Series 7000 Pro Max - 1 | — | SN-HHR-00110 | — | Long Range | 30 dBm | International Handheld Terminals Ltd | Ultra-Rugged Series 7000 Pro Max | Self-Purchased | — | — | — | 24/06/26 09:15 | Available |
| DD-10 | Gudang Reader - 4 | — | SN-HHR-00205 | SKU-HHR-03 | Short Range | — | Chainway | C66 | Official | — | — | — | 25/06/26 14:00 | Waiting for Approval |

- Kolom `Device Name`, `Alias Name`, `Serial Number`, `SKU`, `Range Type`, `Reader Power`, `Source`, `Last Scanned`, dan `Status` tampil pada keadaan awal; kolom `Brand`, `Model/Type`, `Last Scanned In`, `Last User`, dan `Activated At` tersembunyi dan diaktifkan lewat Overlay Column Visibility oleh langkah spec (lihat "Temuan untuk QA"). Spec mengubah visibilitas kolom; langkah 53 memulihkannya dan hook `after` cadangan memulihkan Overlay Column Visibility ke bawaan.
- Tabel "Kolom TC-GS-HHR-269" (baris pertama hasil sort; tie-breaker `Device Name` A-Z kecuali kolom `Serial Number`):

| Kolom | Ascending, baris 1 | Descending, baris 1 |
|---|---|---|
| Device Name | `Chainway C72 - 1` | baris 1 dan 2 dua reader `Zebra RFID Reader - 1` (DD-01 dan DD-06) |
| Serial Number | `SN-HHR-00101` | `SN-HHR-00205` |
| Range Type | `Chainway C72 - 1` (grup Long Range) | `Gudang Reader - 1` (grup Short Range) |
| Source | `Gudang Reader - 1` (grup Official) | `Chainway C72 - 1` (grup Self-Purchased) |
| Brand | `Chainway C72 - 1` (grup Chainway) | `Zebra Mobile Reader - 1` (grup Zebra) |
| Status | `Gudang Reader - 1` (grup Available) | `Chainway C72 - 1` (grup Waiting for Approval) |

- Kemampuan teknis: pembacaan indikator sort pada header, urutan baris, dan visibilitas kolom lewat Overlay Column Visibility.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` true untuk akun Total Control dan hook `after` memulihkannya (lihat `suite.md`).

## Test Steps

### TC-GS-HHR-269: Sort 3-state kelas teks tanpa nilai kosong

1. Aktifkan kolom `Brand` lewat Overlay Column Visibility
2. Klik header kolom `<Kolom>` sekali (Ascending) (diulang untuk setiap baris tabel "Kolom TC-GS-HHR-269", langkah 2 sampai 8)
3. Verifikasi baris pertama sesuai kolom "Ascending, baris 1" baris tabel yang sama
4. Klik header kolom yang sama kali kedua (Descending)
5. Verifikasi baris pertama sesuai kolom "Descending, baris 1" baris tabel yang sama
6. Klik header kolom yang sama kali ketiga
7. Verifikasi indikator sort header kolom netral
8. Verifikasi urutan baris kembali Device Name A-Z (baris pertama `Chainway C72 - 1`)

### TC-GS-HHR-270: Sort kolom dengan nilai kosong (Alias Name, SKU, Model/Type)

9. Klik header `Alias Name` sekali
10. Verifikasi Ascending: baris 1 `Reader Gudang 02` (DD-02) dan sembilan baris `—` di akhir
11. Klik header `Alias Name` kali kedua
12. Verifikasi Descending: sembilan baris `—` di awal dan `Reader Gudang 02` (DD-02) di akhir
13. Klik header `Alias Name` kali ketiga
14. Verifikasi indikator sort header `Alias Name` netral
15. Verifikasi urutan baris kembali Device Name A-Z
16. Klik header `SKU` sekali
17. Verifikasi Ascending: urutan `SKU-HHR-01`, `SKU-HHR-02`, `SKU-HHR-03` (3 baris), `SKU-HHR-04`, lalu 4 baris `—` di akhir
18. Klik header `SKU` kali kedua
19. Verifikasi Descending: 4 baris `—` di awal, lalu `SKU-HHR-04`, `SKU-HHR-03` (3 baris), `SKU-HHR-02`, `SKU-HHR-01`
20. Aktifkan kolom `Model/Type` lewat Overlay Column Visibility
21. Klik header `Model/Type` sekali
22. Verifikasi Ascending: tiga baris `C66` (DD-02, DD-04, DD-10) di awal
23. Verifikasi Ascending: baris `—` (DD-08, `Unitech EA520 - 1`) di akhir
24. Klik header `Model/Type` kali kedua
25. Verifikasi Descending: baris `—` (DD-08) di awal, lalu `Ultra-Rugged Series 7000 Pro Max` (DD-09)

### TC-GS-HHR-271: Sort Reader Power numerik dengan nilai kosong

26. Klik header `Reader Power` sekali
27. Verifikasi Ascending: baris 1 `Zebra Mobile Reader - 1` (25 dBm), diikuti empat reader 30 dBm, lalu lima reader `—` di akhir
28. Klik header `Reader Power` kali kedua
29. Verifikasi Descending: lima reader `—` di awal, diikuti empat reader 30 dBm, lalu `Zebra Mobile Reader - 1` (25 dBm)

### TC-GS-HHR-272: Sort Last Scanned In berdasarkan label badge

30. Aktifkan kolom `Last Scanned In` lewat Overlay Column Visibility
31. Klik header `Last Scanned In` sekali
32. Verifikasi Ascending: `Fixed Asset` (DD-01), `Global Settings` (DD-03), `Supply` (DD-02, DD-06), lalu 6 baris `—` di akhir

### TC-GS-HHR-273: Sort Last User berdasarkan nama lengkap

33. Aktifkan kolom `Last User` lewat Overlay Column Visibility
34. Klik header `Last User` sekali
35. Verifikasi Ascending: baris 1 `Budi S` (Budi Santoso, DD-01), kemudian `Sari D` (Sari Dewi), dan `—` di akhir
36. Klik header `Last User` kali kedua
37. Verifikasi Descending: `—` di awal, kemudian `Sari D`, lalu `Budi S`

### TC-GS-HHR-274: Sort Activated At, Oldest First dan Newest First

38. Aktifkan kolom `Activated At` lewat Overlay Column Visibility
39. Klik header `Activated At` sekali
40. Verifikasi Ascending (`Oldest First`): baris 1 `Gudang Reader - 2` (DD-04, 01/06/26)
41. Klik header `Activated At` kali kedua
42. Verifikasi Descending (`Newest First`): baris 1 `Gudang Reader - 4` (DD-10, 25/06/26)

### TC-GS-HHR-275: Sort Last Scanned dengan reader yang belum pernah dipindai

43. Klik header `Last Scanned` sekali
44. Verifikasi Ascending (`Oldest First`): `Zebra Mobile Reader - 1` (17/06/26), DD-06 (19/06/26), DD-02 (20/06/26), DD-01 (21/06/26), lalu 6 baris `—` di akhir
45. Klik header `Last Scanned` kali kedua
46. Verifikasi Descending (`Newest First`): 6 baris `—` di awal, lalu DD-01 (21/06/26), DD-02 (20/06/26), DD-06 (19/06/26), `Zebra Mobile Reader - 1` (17/06/26)
47. Klik header `Last Scanned` kali ketiga

### TC-GS-HHR-276: Kolom Actions tidak memiliki ikon sort

48. Amati header kolom paling kanan (Actions)
49. Verifikasi tidak ada ikon sort pada kolom Actions
50. Klik header kolom Actions
51. Verifikasi Overlay Column Visibility terbuka
52. Tutup Overlay Column Visibility
53. Nonaktifkan kolom `Brand`, `Model/Type`, `Last Scanned In`, `Last User`, dan `Activated At` lewat Overlay Column Visibility (pemulihan keadaan awal)

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti urutan TC sumber (269 sampai 276); semua blok hanya membaca dan tidak mengubah data. Klik header kolom lain memulai sort Ascending baru dan mereset kolom sebelumnya, sehingga blok tidak membersihkan sort satu per satu kecuali lewat klik ketiga yang diminta TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): aktivasi kolom lewat Overlay Column Visibility pada langkah awal blok TC-GS-HHR-269, 270, 272, 273, dan 274; klik ketiga header `Last Scanned` pada blok TC-GS-HHR-275 (mereset sort sebelum blok berikutnya); tutup Overlay Column Visibility dan pemulihan kolom pada langkah 53.
- Langkah yang diulang per baris tabel Prerequisites: langkah 2 sampai 8 (6 iterasi). Tiap iterasi punya tiga `Verifikasi`.
- `Verifikasi` urutan kombinasi (mis. "empat reader 30 dBm, lalu lima reader `—`") ditulis sebagai satu `Verifikasi` urutan baris karena Expected TC menyebutnya sebagai satu butir pengamatan urutan.
- Spec memuat 53 langkah nominal (sekitar 88 langkah dengan ekspansi blok ulang; di atas smell sekitar 35 langkah). Alasan: seluruhnya satu kelas harness (Sort daftar reader), satu akun, satu dataset, tanpa aksi yang mengubah data; tiap blok TC memulai dari sort yang di-reset oleh klik header kolom berikutnya dan tetap bermakna bila blok lain gagal.
- Pembagian TC lintas spec: kombinasi Sort dengan Search dan Filter (TC-GS-HHR-262 sampai 265, 268) ada di spec 054; Overlay Column Visibility dan Setup Column daftar ada di spec 055.
- Temuan untuk QA:
  - TC-GS-HHR-269 tidak menyebut bahwa kolom `Brand` harus ditampilkan lebih dulu (PRD: Brand perlu ditampilkan lewat Column Visibility); spec menambah langkah mengaktifkan `Brand` sebagai langkah penghubung.
  - TC-GS-HHR-269, 271, dan 275 tidak menyebut kolom `Range Type`, `Source`, `Status`, `Reader Power`, dan `Last Scanned` tampil pada keadaan awal; spec mengasumsikan kolom itu tampil secara bawaan (TC-GS-HHR-270, 272, 273, dan 274 mengaktifkan kolom lain secara eksplisit).
  - TC-GS-HHR-270 langkah 1 sampai 5 tidak menutup siklus sort `SKU` dengan klik ketiga; spec mengikuti TC (sort `SKU` digantikan oleh klik header `Model/Type`).
  - TC-GS-HHR-276 tidak menyebut cara menutup Overlay Column Visibility; spec menulis "Tutup Overlay Column Visibility" sebagai langkah penghubung.
  - TC-GS-HHR-274 dan 275 memakai tanggal yang berbeda hari (bukan hanya menit), sehingga hook tidak menunggu pergantian menit.
  - Seed Reader A bernama dan bertanggal literal tanpa suffix `{runId}` karena asersi urutan bergantung pada nilai tetap; fixture backend dan pemulihannya antar TC disediakan tim FE/BE tanpa mekanisme yang ditulis di TC.
  - Post Condition semua TC di spec ini `-`; tidak ada yang diasersi.

---
id: TC-GS-HHR-E2E-002-format-isi-sel-kolom-badge-tanggal-dan-kolom-curated
title: "Format Isi Sel Kolom Daftar Reader: Text Link Device Name, Nilai Kosong, Reader Power, Badge, Tanggal, dan Kolom Curated lewat Column Visibility"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-3
  - TC-GS-HHR-4
  - TC-GS-HHR-5
  - TC-GS-HHR-6
  - TC-GS-HHR-7
  - TC-GS-HHR-8
  - TC-GS-HHR-9
  - TC-GS-HHR-10
  - TC-GS-HHR-11
  - TC-GS-HHR-12
  - TC-GS-HHR-13
  - TC-GS-HHR-14
coverage:
  web: automated
---

# Format Isi Sel Kolom Daftar Reader: Text Link Device Name, Nilai Kosong, Reader Power, Badge, Tanggal, dan Kolom Curated lewat Column Visibility

## Prerequisites

- Mode: FE+BE (backend nyata). Suite `parallel: false`.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1, Client A). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Hardware > Handheld Reader untuk akun Total Control; spec ini tidak menguji navigasi sidebar sehingga tidak mengulang langkah buka.
- Guided Tooltip: flag halaman Handheld Reader (`guided_tooltip_seen_gs-handheld-reader`) mengikuti hook suite (lihat `suite.md`).
- Data Pre-setup (Client A, plan Growth, General Settings `dd/MM/yy` 24-hour Asia/Jakarta): Seed Reader A (DD-01 s.d. DD-10) dan Seed Usage Event reader DD-03 (dua event: `Audit Scan` Fixed Asset `TSK-202606-0009` 14/06/26 oleh Budi S dan `Pair TAG` Global Settings 17/06/26 16:05 oleh Sari D), dipulihkan fixture backend (disediakan tim FE) sebelum spec berjalan. Spec hanya membaca; satu-satunya state yang diubah adalah visibilitas kolom (dipulihkan di langkah terakhir spec dan oleh hook `after` sebagai cadangan).
- Peta baris Seed Reader A yang dipakai langkah:

| ID | Device Name | Serial Number | Status |
|---|---|---|---|
| DD-01 | `Zebra RFID Reader - 1` | `SN-HHR-00101` | Available |
| DD-02 | `Gudang Reader - 1` | `SN-HHR-00102` | Available |
| DD-03 | `Zebra Mobile Reader - 1` | `SN-HHR-00103` | Damaged |
| DD-04 | `Gudang Reader - 2` | `SN-HHR-00104` | Missing |
| DD-05 | `Chainway C72 - 1` | `SN-HHR-00105` | Waiting for Approval |
| DD-06 | `Zebra RFID Reader - 1` | `SN-HHR-00107` | Available |
| DD-07 | `Honeywell CK65 - 1` | `SN-HHR-00108` | Available |
| DD-08 | `Unitech EA520 - 1` | `SN-HHR-00109` | Available |
| DD-09 | `International Handheld Terminals Ltd Ultra-Rugged Series 7000 Pro Max - 1` | `SN-HHR-00110` | Available |
| DD-10 | `Gudang Reader - 4` | `SN-HHR-00205` | Waiting for Approval |

- Data Dinamis: tidak ada.
- Kemampuan teknis: hover; pembacaan gaya terhitung (warna teks, garis bawah, tinggi baris) dan varian badge (`severity`) pada sel tabel; pembacaan tooltip.
- State global: visibilitas kolom tabel daftar reader akun Total Control (kolom curated `Brand`, `Model/Type`, `Last Scanned In`, `Last User`, `Activated At` default Hidden) diaktifkan oleh langkah dan dipulihkan ke default di langkah terakhir; hook `after` memulihkannya sebagai cadangan (mekanisme pemulihan di luar UI disediakan tim FE).

## Test Steps

### TC-GS-HHR-3: Device Name sebagai text link

1. Amati warna teks Device Name baris `Gudang Reader - 1` (`SN-HHR-00102`, DD-02)
2. Verifikasi warna teks default sama dengan teks body tabel (netral), bukan warna link browser
3. Arahkan kursor ke `Gudang Reader - 1`
4. Verifikasi saat hover warna teks berubah mengikuti warna primary Global Settings (hitam)
5. Verifikasi saat hover teks tidak memakai garis bawah
6. Klik `Gudang Reader - 1`
7. Verifikasi Popup Detail `Handheld Reader Detail` untuk reader `Gudang Reader - 1` terbuka
8. Tutup Popup Detail dengan `Esc`

### TC-GS-HHR-4: Device Name panjang tidak dipotong dan kolom melebar mengikuti isi

9. Amati baris DD-09 pada kolom `Device Name`
10. Verifikasi teks `International Handheld Terminals Ltd Ultra-Rugged Series 7000 Pro Max - 1` tampil utuh tanpa tanda `..`
11. Arahkan kursor ke nama tersebut
12. Verifikasi hover tidak memunculkan tooltip
13. Verifikasi baris DD-09 tidak berubah menjadi lebih dari satu baris data pada kolom lain (tinggi baris tabel konsisten dengan baris lain)

### TC-GS-HHR-6: Kolom Reader Power

14. Amati kolom `Reader Power` pada baris DD-01 (`Zebra RFID Reader - 1`, `SN-HHR-00101`), DD-03 (`Zebra Mobile Reader - 1`), dan DD-02 (`Gudang Reader - 1`)
15. Verifikasi DD-01 menampilkan `30 dBm`
16. Verifikasi DD-03 menampilkan `25 dBm`
17. Verifikasi DD-02 (Short Range) menampilkan `—`
18. Verifikasi judul kolom tetap `Reader Power`

### TC-GS-HHR-7: Badge kolom Range Type dan Status serta teks kolom Source

19. Amati kolom `Range Type`, `Source`, dan `Status` pada DD-01, DD-02, DD-03, DD-04 (`Gudang Reader - 2`), DD-05 (`Chainway C72 - 1`), dan DD-07 (`Honeywell CK65 - 1`)
20. Verifikasi `Range Type` DD-01 `Long Range` memakai badge `severity="dark"`
21. Verifikasi `Range Type` DD-02 `Short Range` memakai badge `severity="primary"`
22. Verifikasi `Source` DD-01 berupa teks polos `Official`
23. Verifikasi `Source` DD-07 berupa teks polos `Self-Purchased`
24. Verifikasi `Status` DD-01 `Available` memakai badge `severity="success"`
25. Verifikasi `Status` DD-03 `Damaged` memakai badge `severity="danger"`
26. Verifikasi `Status` DD-04 `Missing` memakai badge `severity="danger"`
27. Verifikasi `Status` DD-05 `Waiting for Approval` memakai badge `severity="warning"`

### TC-GS-HHR-5: Nilai kosong kolom Alias Name, SKU, dan Model/Type, kolom Serial Number selalu terisi

28. Klik header kolom Actions `(⋯)` untuk membuka Overlay Column Visibility
29. Centang `Model/Type`
30. Tutup Overlay Column Visibility dengan `Esc`
31. Amati kolom `Alias Name`, `Serial Number`, `SKU`, dan `Model/Type` pada seluruh 10 baris
32. Verifikasi `Alias Name`: hanya DD-02 berisi `Reader Gudang 02`, sembilan baris lain menampilkan `—`
33. Verifikasi `SKU` baris Jalur B (DD-05, DD-07, DD-08, DD-09) menampilkan `—`
34. Verifikasi `SKU` baris Jalur A: DD-01 `SKU-HHR-01`, DD-03 `SKU-HHR-02`, DD-02, DD-04, dan DD-10 `SKU-HHR-03`, DD-06 `SKU-HHR-04`
35. Verifikasi `Serial Number` terisi pada 10 baris (`SN-HHR-00101` sampai `SN-HHR-00205`), tidak ada sel kosong
36. Verifikasi `Model/Type`: hanya DD-08 (Jalur B tanpa Model/Type) menampilkan `—`, sembilan baris lain terisi
37. Klik header kolom Actions `(⋯)` untuk membuka Overlay Column Visibility dan hapus centang `Model/Type`
38. Tutup Overlay Column Visibility dengan `Esc`

### TC-GS-HHR-8: Kolom curated tampil setelah diaktifkan lewat Column Visibility

39. Klik header kolom Actions `(⋯)` untuk membuka Overlay Column Visibility
40. Centang `Brand`, `Model/Type`, `Last Scanned In`, `Last User`, dan `Activated At`
41. Verifikasi kolom `Brand`, `Model/Type`, `Last Scanned In`, `Last User`, dan `Activated At` tampil langsung pada tabel tanpa menekan Save (panel cepat ter-apply)
42. Tutup Overlay Column Visibility dengan `Esc`
43. Amati baris DD-01, DD-04, dan DD-08
44. Verifikasi DD-01 `Brand` `Zebra`
45. Verifikasi DD-01 `Model/Type` `RFD40`
46. Verifikasi DD-01 `Last Scanned In` `Fixed Asset`
47. Verifikasi DD-01 `Last User` `Budi S`
48. Verifikasi DD-01 `Activated At` `21/06/26 08:00`
49. Verifikasi DD-04 (belum pernah dipindai) `Last Scanned In` `—`
50. Verifikasi DD-04 `Last User` `—`
51. Verifikasi DD-04 `Activated At` `01/06/26 07:45`
52. Verifikasi DD-08 (Jalur B tanpa Model/Type) `Brand` badge `Unitech`
53. Verifikasi DD-08 `Model/Type` `—`

### TC-GS-HHR-9: Badge Last Scanned In per produk

54. Amati kolom `Last Scanned In` baris DD-01, DD-02, dan DD-03
55. Verifikasi `Last Scanned In` DD-01 `Fixed Asset` memakai badge `severity="info"`
56. Verifikasi `Last Scanned In` DD-02 `Supply` memakai badge `severity="success"`
57. Verifikasi `Last Scanned In` DD-03 `Global Settings` memakai badge `severity="secondary"`

### TC-GS-HHR-10: Last User tampil `[First Name] [Last Initial]` dan tooltip nama lengkap

58. Amati kolom `Last User` baris DD-01
59. Verifikasi `Last User` DD-01 berupa teks polos `Budi S` (bukan badge)
60. Arahkan kursor ke nilai `Last User` DD-01
61. Verifikasi tooltip `Budi Santoso`

### TC-GS-HHR-11: Badge Brand dan Model/Type, nama pendek tampil penuh dan nama di atas 25 karakter dipotong 12+..+12 dengan tooltip nama lengkap

62. Amati kolom `Brand` dan `Model/Type` baris DD-01, DD-08, dan DD-09
63. Verifikasi DD-01: badge `Zebra` dan `RFD40` tampil penuh dengan `severity="dark"`
64. Arahkan kursor ke badge `Brand` DD-01
65. Verifikasi badge `Brand` DD-01 tanpa tooltip
66. Arahkan kursor ke badge `Model/Type` DD-01
67. Verifikasi badge `Model/Type` DD-01 tanpa tooltip
68. Verifikasi DD-09 `Brand` tampil `Internationa..erminals Ltd`
69. Arahkan kursor ke badge `Brand` DD-09
70. Verifikasi tooltip `International Handheld Terminals Ltd`
71. Verifikasi DD-09 `Model/Type` tampil `Ultra-Rugged..7000 Pro Max`
72. Arahkan kursor ke badge `Model/Type` DD-09
73. Verifikasi tooltip `Ultra-Rugged Series 7000 Pro Max`
74. Verifikasi DD-08 `Brand` badge `Unitech` tampil penuh
75. Verifikasi DD-08 `Model/Type` tampil `—`

### TC-GS-HHR-12: Format tanggal Last Scanned dan Activated At mengikuti General Settings Client A

76. Amati kolom `Last Scanned` dan `Activated At` baris DD-01
77. Verifikasi `Last Scanned` DD-01 `21/06/26 10:15`
78. Verifikasi `Activated At` DD-01 `21/06/26 08:00`

### TC-GS-HHR-13: Reader yang belum pernah memindai menampilkan `—`

79. Amati baris DD-04
80. Verifikasi `Last Scanned` DD-04 `—`
81. Verifikasi `Last Scanned In` DD-04 `—`
82. Verifikasi `Last User` DD-04 `—`

### TC-GS-HHR-14: Last Scanned, Last Scanned In, dan Last User berasal dari satu Usage Event terbaru

83. Amati baris DD-03
84. Verifikasi `Last Scanned` DD-03 `17/06/26 16:05`
85. Verifikasi `Last Scanned In` DD-03 `Global Settings`
86. Verifikasi `Last User` DD-03 `Sari D`
87. Verifikasi ketiga nilai DD-03 berasal dari event `Pair TAG` (17/06/26), bukan campuran dengan event `Audit Scan` 14/06/26 (nilai tidak ada yang `Fixed Asset`, `Budi S`, atau `14/06/26`)

### Pemulihan visibilitas kolom

88. Klik header kolom Actions `(⋯)` untuk membuka Overlay Column Visibility dan hapus centang `Brand`, `Model/Type`, `Last Scanned In`, `Last User`, dan `Activated At`
89. Tutup Overlay Column Visibility dengan `Esc`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 3, 4, 6, 7, 5, 8, 9, 10, 11, 12, 13, 14. Kolom default (TC-GS-HHR-3, 4, 6, 7) lebih dulu karena tidak butuh kolom curated; TC-GS-HHR-5 mengaktifkan `Model/Type` lalu langkah 37 memulihkannya sebelum TC-GS-HHR-8 supaya centang kelima kolom di langkah 40 tidak membalik state `Model/Type`; TC-GS-HHR-9 sampai 14 memakai kolom curated yang sudah diaktifkan di langkah 40. Langkah "Aktifkan kolom ..." pada TC-GS-HHR-9, 10, 11, 12, 13, dan 14 tidak diulang karena kolom yang sama sudah aktif sejak langkah 40 dan tidak ada langkah yang menyembunyikannya sebelum langkah 88 (halaman yang sama dipakai berulang, prinsip 13 konvensi).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8 (tutup Popup Detail), langkah 30, 38, 42, dan 89 (tutup Overlay Column Visibility dengan `Esc`), langkah 37 (pulihkan `Model/Type`), langkah 88 (pulihkan visibilitas kolom ke default).
- TC-GS-HHR-3 langkah 6 sampai 8 membuka Popup Detail lewat klik Device Name sebagai Expected c TC itu; isi Popup Detail diuji di spec lain.
- TC-GS-HHR-14 langkah 87 adalah kesimpulan dari langkah 84 sampai 86 (Expected d TC) dan tetap satu `Verifikasi` karena tidak teramati terpisah.
- Spec melewati sekitar 35 langkah (89 langkah). Seluruhnya satu kelas (screening baca isi sel tabel daftar reader pada Seed Reader A, tanpa aksi yang mengubah data reader), dan tiap blok TC memeriksa sel yang berbeda. Blok TC-GS-HHR-9 sampai 14 bergantung pada kolom curated yang diaktifkan di blok TC-GS-HHR-8; bila langkah 39 sampai 42 gagal keras, blok 9 sampai 14 ikut gagal. Risiko ini diterima karena alternatifnya (mengaktifkan dan menyembunyikan kolom yang sama pada tiap TC) menambah sekitar 12 langkah tanpa cakupan baru, dan aktivasi kolom itu sendiri sudah diasersi di blok TC-GS-HHR-8. Blok TC-GS-HHR-3, 4, 5, 6, dan 7 berdiri sendiri.
- Temuan untuk QA:
  - TC-GS-HHR-4 Expected c ("tinggi baris tabel konsisten") tidak menyebut ukuran pembanding; spec membandingkan tinggi baris DD-09 dengan baris lain.
  - TC-GS-HHR-3 Expected b menulis warna primary Global Settings "(hitam)" tanpa nilai warna; spec mengasersi perubahan warna ke warna primary tanpa nilai heksadesimal.
  - TC-GS-HHR-7 sampai 9 menyebut varian badge lewat nilai `severity`; spec mengasumsikan `severity` terbaca dari komponen badge tanpa menamai atribut DOM (tim FE menyediakan pembacaannya).
  - TC-GS-HHR-5 dan 8 tidak menyebut cara menutup Overlay Column Visibility sebelum mengamati tabel; spec menutup dengan `Esc`.

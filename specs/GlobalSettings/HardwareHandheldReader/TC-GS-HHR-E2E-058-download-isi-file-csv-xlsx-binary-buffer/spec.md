---
id: TC-GS-HHR-E2E-058-download-isi-file-csv-xlsx-binary-buffer
title: "Isi File Download Daftar Reader Handheld Reader: Transformasi Nilai Sel XLSX, Escape CSV dengan BOM, Download Tab Usage, Kolom Checkbox pada Export, dan Download Modal serta Tab Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-312
  - TC-GS-HHR-314
  - TC-GS-HHR-183
  - TC-GS-HHR-195
  - TC-GS-HHR-338
  - TC-GS-HHR-454
coverage:
  web: automated
---

# Isi File Download Daftar Reader Handheld Reader: Transformasi Nilai Sel XLSX, Escape CSV dengan BOM, Download Tab Usage, Kolom Checkbox pada Export, dan Download Modal serta Tab Changelog

## Prerequisites

- Mode: FE+BE (backend nyata). Kelas harness binary buffer (konvensi bagian 3, prinsip 13f): isi berkas CSV dan XLSX dipisah dari kegagalan ekspor.
- Akun aktor hook `before`: Total Control (Sari Dewi), Client A, `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader dengan Search dan Filter kosong dan konfigurasi kolom default.
- Client A: plan Growth, format tanggal default General Settings `dd/MM/yy` 24-hour Asia/Jakarta (tidak diubah spec ini). Asersi tanggal mengikuti format ini; jam server dan jam browser tidak diatur karena data tanggal berasal dari seeding tetap.
- Data Dinamis Seed Reader A (10 reader DD-01 sampai DD-10), dibuat lewat fixture backend sebelum eksekusi (`Fixture.hardwareHandheldReader.seedReaderA`, fixture baru) dan dipulihkan antar TC oleh fixture backend. Nama dan tanggal literal tanpa suffix `{runId}` karena asersi sel bergantung pada nilai tetap (lihat Temuan untuk QA). Baris dikenali lewat Serial Number karena DD-01 dan DD-06 sama-sama bernama `Zebra RFID Reader - 1`. Nilai yang diasersi:

| ID | Serial Number | Range Type | Reader Power | Alias Name | SKU | Last Scanned | Last Scanned In | Last User | Status |
|---|---|---|---|---|---|---|---|---|---|
| DD-01 | SN-HHR-00101 | Long Range | 30 dBm | — | SKU-HHR-01 | 21/06/26 10:15 | Fixed Asset | Budi S (Budi Santoso) | Available |
| DD-02 | SN-HHR-00102 | Short Range | — | Reader Gudang 02 | SKU-HHR-03 | 20/06/26 09:40 | Supply | Sari D | Available |
| DD-04 | SN-HHR-00104 | Short Range | — | — | SKU-HHR-03 | — | — | — | Missing |
| DD-07 | SN-HHR-00108 | Long Range | 30 dBm | — | — | — | — | — | Available |

- Precondition TC-GS-HHR-314 (langkah 22): Alias Name DD-02 diubah menjadi `Gudang, "Utama"` lewat fixture backend; mekanisme fixture disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD). Alias Name DD-02 dipulihkan ke `Reader Gudang 02` oleh fixture backend di hook `after`.
- Data tambahan untuk TC-GS-HHR-183, 338, dan 454:
  - Seed Usage Event DD-01 UE-01 sampai UE-06 (`Fixture.hardwareHandheldReader.seedUsageDd01`): enam baris Tab Usage DD-01 (`SN-HHR-00101`), sebagian dengan `Transaction ID` kosong; pemulihan oleh fixture backend.
  - Seed Changelog Client A CL-01 sampai CL-09 (`Fixture.hardwareHandheldReader.seedChangelogClientA`): DD-03 (`Zebra Mobile Reader - 1`, `SN-HHR-00103`) memiliki 3 entri Changelog (CL-06, CL-07, CL-08); Modal Changelog memuat baris dengan nilai kosong. Pemulihan oleh fixture backend.
- Kemampuan teknis: menangkap berkas unduhan browser ke direktori bersih per unduhan supaya nama berkas yang sama (`Handheld-Reader-List.xlsx`, `Handheld-Reader-List.csv`) tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV (byte mentah untuk BOM dan pemisah, serta sel) dan XLSX (nilai dan tipe sel, termasuk sel angka vs teks). Berkas unduhan dihapus di hook `after`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-handheld-reader`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan: visibilitas kolom `Last Scanned In` dan `Last User` (dipulihkan tersembunyi pada langkah penutup TC-GS-HHR-312), Alias Name DD-02 (dipulihkan di hook `after`); hook `after` juga memulihkan konfigurasi kolom Daftar Reader ke default sebagai cadangan.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-HHR-312: Transformasi nilai sel pada file export Daftar Reader

1. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
2. Centang kolom `Last Scanned In` pada Overlay Column Visibility
3. Centang kolom `Last User` pada Overlay Column Visibility
4. Tekan `Esc` (tutup overlay)
5. Klik ikon Download
6. Klik `Download as XLSX`
7. Buka file `Handheld-Reader-List.xlsx` yang diunduh dan baca baris Serial Number `SN-HHR-00101` (DD-01), `SN-HHR-00102` (DD-02), `SN-HHR-00104` (DD-04), dan `SN-HHR-00108` (DD-07)
8. Verifikasi sel `Range Type` ditulis teks label saja (tanpa warna badge): DD-01 `Long Range`, DD-02 `Short Range`, DD-04 `Short Range`
9. Verifikasi sel `Status` ditulis teks: DD-01 `Available`, DD-02 `Available`, DD-04 `Missing`
10. Verifikasi sel `Reader Power` DD-01 berupa angka `30` (tanpa satuan `dBm`)
11. Verifikasi sel `Reader Power` DD-02 ditulis `-`
12. Verifikasi sel `Alias Name` DD-01 yang kosong ditulis `-`
13. Verifikasi sel `SKU` DD-07 yang kosong ditulis `-`
14. Verifikasi sel `Last Scanned` DD-01 ditulis `21/06/26 10:15` mengikuti General Settings
15. Verifikasi sel `Last Scanned` DD-04 ditulis `-`
16. Verifikasi sel `Last Scanned In` DD-01 ditulis `Fixed Asset`
17. Verifikasi sel `Last User` DD-01 ditulis nama lengkap `Budi Santoso`
18. Verifikasi sel `Last User` DD-04 ditulis `-`
19. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
20. Lepas centang kolom `Last Scanned In` dan `Last User` pada Overlay Column Visibility (pemulihan kolom)
21. Tekan `Esc` (tutup overlay)

### TC-GS-HHR-314: CSV menggandakan tanda kutip dan membungkus nilai berisi koma

22. Ubah Alias Name DD-02 menjadi `Gudang, "Utama"` lewat fixture backend (aksi seeding, bukan lewat UI)
23. Muat ulang halaman (F5)
24. Klik ikon Download
25. Klik `Download as CSV`
26. Buka file `Handheld-Reader-List.csv` yang diunduh dan baca baris Serial Number `SN-HHR-00102` (DD-02)
27. Verifikasi sel `Alias Name` DD-02 ditulis `"Gudang, ""Utama"""`
28. Verifikasi file memakai pemisah koma
29. Verifikasi file berencoding UTF-8 dengan BOM

### TC-GS-HHR-183: Download Tab Usage dengan nama file Handheld-Reader-Usage

30. Klik `Device Name` baris DD-01 (Serial Number `SN-HHR-00101`)
31. Verifikasi tab `Usage` aktif
32. Klik ikon Download, pilih `Download as CSV`
33. Verifikasi tidak ada toast sukses
34. Verifikasi file `Handheld-Reader-Usage.csv` terunduh
35. Verifikasi isi file CSV mengikuti 6 baris dan kolom yang tampil
36. Verifikasi `Transaction ID` kosong ditulis `-` pada file CSV
37. Klik ikon Download, pilih `Download as XLSX`
38. Verifikasi tidak ada toast sukses
39. Verifikasi file `Handheld-Reader-Usage.xlsx` terunduh
40. Verifikasi isi file XLSX mengikuti 6 baris dan kolom yang tampil
41. Verifikasi `Transaction ID` kosong ditulis `-` pada file XLSX
42. Tutup Popup `Handheld Reader Detail` dengan `✕`

### TC-GS-HHR-195: Kolom Checkbox bukan bagian Setup Column dan tidak ikut export

43. Klik header kolom Actions `(⋯)` untuk membuka Overlay Column Visibility
44. Verifikasi daftar Overlay Column Visibility memuat sedikitnya satu kolom tabel
45. Verifikasi daftar Overlay Column Visibility tidak memuat `Checkbox`
46. Verifikasi checkbox header dan checkbox baris tetap tampil di tabel
47. Tutup Overlay Column Visibility dengan klik di luar Overlay
48. Klik ikon Download, pilih `Download as CSV`
49. Buka file `Handheld-Reader-List.csv` dan baca header
50. Verifikasi header file memuat kolom tabel selain `Checkbox`
51. Verifikasi file `Handheld-Reader-List.csv` tidak memuat kolom `Checkbox`

### TC-GS-HHR-338: Download Modal Changelog

52. Klik ikon Changelog
53. Klik ikon Download di modal
54. Klik `Download as CSV`
55. Verifikasi tidak ada toast sukses
56. Verifikasi berkas `Changelog-Handheld-Reader.csv` terunduh
57. Verifikasi nilai kosong ditulis `-` pada berkas CSV
58. Klik ikon Download di modal
59. Klik `Download as XLSX`
60. Verifikasi tidak ada toast sukses
61. Verifikasi berkas `Changelog-Handheld-Reader.xlsx` terunduh
62. Verifikasi nilai kosong ditulis `-` pada berkas XLSX
63. Tutup Modal Changelog dengan `✕`

### TC-GS-HHR-454: Download Tab Changelog Popup Detail

64. Klik `Device Name` baris DD-03 (Serial Number `SN-HHR-00103`)
65. Klik tab `Changelog`
66. Klik ikon Download di tab
67. Klik `Download as CSV`
68. Verifikasi tidak ada toast sukses
69. Verifikasi berkas `Changelog-Handheld-Reader.csv` terunduh
70. Verifikasi berkas memuat 3 baris entri DD-03
71. Verifikasi berkas hanya memuat kolom yang tampil di tab (tanpa kolom `Device Name`)
72. Tutup Popup `Handheld Reader Detail` dengan `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`, section 4a-6. Kelas binary buffer (prinsip 13f): isi berkas dipisah dari Download biasa (spec 057) dan kegagalan ekspor (spec 028).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC di spec: 312, 314 (daftar utama), lalu 183, 195, 338, 454 (Tab Usage, Overlay Column Visibility, Modal Changelog, Tab Changelog). Tiap TC berada utuh di spec ini karena klausa fungsional (nama berkas, nama kolom, jumlah baris, tanpa toast sukses, Overlay Column Visibility) dan klausa isi berkas (nilai sel, BOM, tipe sel) berada dalam satu TC yang sama. Nama berkas, nama kolom, dan jumlah baris adalah asersi fungsional (konvensi bagian 3 prinsip 13f); asersi serupa untuk Daftar Reader ada di spec 057, sedangkan nilai sel, BOM, dan tipe sel hanya di spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`): menutup overlay dengan `Esc`; mengaktifkan kolom `Last Scanned In` dan `Last User` serta memulihkannya; membuka isi berkas unduhan; membuka dan menutup Popup Detail, Modal Changelog, dan Overlay (langkah 30, 42, 43, 47, 52, 63, 64, 65, 72); memuat ulang halaman sesudah fixture mengubah Alias Name DD-02 (langkah 23).
- Spec memuat 72 langkah (di atas sekitar 35 langkah). Alasan: satu kelas (isi berkas unduhan, prinsip 13f), satu akun, hanya membaca data (satu-satunya perubahan state adalah Alias Name DD-02 oleh fixture dan kolom yang dipulihkan); tiap blok TC membuka dan menutup popup atau modal sendiri dari layar daftar, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Asersi "tidak ada toast sukses" (TC-GS-HHR-183, 338, 454) diletakkan segera sesudah pemicu pilihan format dan sebelum asersi berkas terunduh yang menjadi anchor positifnya; absence kolom `Checkbox` (langkah 51) didahului langkah 50 (header memuat kolom lain).
- Pembagian TC lintas spec: Download biasa (TC-GS-HHR-306 sampai 311, 313) di spec 057; kegagalan Download (TC-GS-HHR-315) di spec 028; Download lebih dari 5.000 baris (TC-GS-HHR-316) di spec 059; TC-GS-HHR-469 (hover nama pengguna) ada di spec 062.
- Temuan untuk QA:
  - TC-GS-HHR-312: Expected a ("warna badge tidak ikut") tidak punya cara pengamatan sendiri pada berkas; spec mengasersi sel berisi teks label saja.
  - TC-GS-HHR-312 dan 314: TC tidak menyebut cara menangkap berkas unduhan dan membaca isinya (tipe sel angka, byte BOM, pemisah); kemampuan tersebut disediakan tim FE (Prerequisites).
  - TC-GS-HHR-314: precondition d mengubah Alias Name DD-02 lewat fixture tanpa menyebut mekanismenya; perubahan itu dapat menambah entri Changelog dan mengubah Seed Reader A. Spec tidak mengasersi Changelog.
  - TC-GS-HHR-314: Expected tidak menyebut baris header dan nama kolom `Alias Name`; spec membaca sel berdasarkan baris Serial Number `SN-HHR-00102`.
  - TC-GS-HHR-183, 195, 338, dan 454: temuan TC masing-masing (nilai kosong `-` tidak menyebut kolom pada 338; letak unduhan tidak disebut) mengikuti catatan di atas. Mekanisme membaca berkas unduhan disediakan tim FE.
  - Post Condition semua TC di spec ini `-`; tidak ada yang diasersi.

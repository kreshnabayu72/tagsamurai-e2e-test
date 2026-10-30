---
id: TC-GS-HHR-E2E-057-download-csv-xlsx-daftar-reader
title: "Download Daftar Reader Handheld Reader: CSV dan XLSX, Seluruh Baris, Search dan Filter Aktif, Kolom Visible, dan Hasil Nol Baris"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-306
  - TC-GS-HHR-307
  - TC-GS-HHR-308
  - TC-GS-HHR-309
  - TC-GS-HHR-310
  - TC-GS-HHR-311
  - TC-GS-HHR-313
coverage:
  web: automated
---

# Download Daftar Reader Handheld Reader: CSV dan XLSX, Seluruh Baris, Search dan Filter Aktif, Kolom Visible, dan Hasil Nol Baris

## Prerequisites

- Mode: FE+BE (backend nyata). Spec membaca daftar reader dan isi berkas unduhan; spec hanya mengubah visibilitas kolom (preferensi di browser) dan mengosongkan Search dan Filter.
- Akun aktor hook `before`: Total Control (Sari Dewi), Client A, `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Akun kedua (langkah 54 sampai 56, TC-GS-HHR-306): Total Control Client L, `totalControl_automated_{namaClient}@qwertysystem.net` dengan namaClient Client L; email persisnya tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE. Password `Spectra.env.GS_CLIENTL_TC_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` oleh pemilik suite). Client L memiliki 26 reader `Large Reader - 1` sampai `Large Reader - 26` (kondisi data disediakan tim FE). Hook `after` mengembalikan sesi ke akun default suite.
- Environment variable: `GS_TC_PASSWORD`, `GS_CLIENTL_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader dengan Search dan Filter kosong dan konfigurasi kolom default.
- Client A: plan Growth, format tanggal default General Settings `dd/MM/yy` 24-hour (tidak diubah spec ini).
- Data Dinamis Seed Reader A (10 reader DD-01 sampai DD-10), dibuat lewat fixture backend sebelum eksekusi (`Fixture.hardwareHandheldReader.seedReaderA`) dan dipulihkan antar TC oleh fixture backend. Asersi memakai `Gudang Reader - 1` (DD-02, `Available`) sebagai satu-satunya reader yang cocok dengan Search `Gudang` dan Filter `Status` = `Available` (reader `Gudang` lain: DD-04 `Missing`, DD-10 `Waiting for Approval`, sehingga kolom `Status` memiliki sedikitnya dua nilai distinct). Selebihnya dipakai sebagai precondition TC, tidak diasersi.
- Data uji: format `CSV` (TC-GS-HHR-310, 308, 309, 307, 313, 306) dan `XLSX` (TC-GS-HHR-311); kolom `Alias Name` dan `Source` di-hide lalu di-unhide (TC-GS-HHR-308, 309); keyword Search `Gudang` dan `zzzz`; Filter `Status` = `Available`.
- Kemampuan teknis (membaca berkas, bukan kelas binary buffer): menangkap berkas unduhan browser ke direktori bersih per unduhan supaya nama berkas yang sama (`Handheld-Reader-List.csv`) tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV dan XLSX untuk nama kolom, jumlah baris, dan nama sheet. Berkas unduhan dihapus di hook `after`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-handheld-reader`: diatur hook suite (lihat `suite.md`, bagian Hook suite) untuk akun Client A dan Client L; spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan: visibilitas kolom `Alias Name` dan `Source` (dipulihkan tampil pada langkah penghubung sesudah TC-GS-HHR-308 dan lewat TC-GS-HHR-309), Search dan Filter (dikosongkan sesudah TC-GS-HHR-307 dan 313); hook `after` sebagai cadangan (`[Reset to Default]` lalu `[Save]` pada Setup Column Daftar Reader).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-HHR-310: Download CSV menghasilkan file dengan nama dan ekstensi sesuai pilihan

1. Klik ikon Download
2. Klik `Download as CSV`
3. Verifikasi tidak ada toast
4. Verifikasi file `Handheld-Reader-List.csv` terunduh

### TC-GS-HHR-311: Download XLSX menghasilkan file dengan nama dan ekstensi sesuai pilihan

5. Klik ikon Download
6. Klik `Download as XLSX`
7. Verifikasi tidak ada toast
8. Verifikasi file `Handheld-Reader-List.xlsx` terunduh
9. Buka isi file `Handheld-Reader-List.xlsx` yang diunduh
10. Verifikasi file memiliki satu sheet bernama `Sheet1`

### TC-GS-HHR-308: Kolom yang disembunyikan tidak ikut ter-export

11. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
12. Hilangkan centang kolom `Alias Name` pada Overlay Column Visibility
13. Hilangkan centang kolom `Source` pada Overlay Column Visibility
14. Tekan `Esc` (tutup overlay)
15. Klik ikon Download
16. Klik `Download as CSV`
17. Verifikasi tidak ada toast peringatan
18. Buka isi file `Handheld-Reader-List.csv` yang diunduh
19. Verifikasi file memuat kolom lain yang tampil: `Device Name`, `Serial Number`, `SKU`, `Range Type`, `Reader Power`, `Last Scanned`, dan `Status`
20. Verifikasi file tidak memuat kolom `Alias Name`
21. Verifikasi file tidak memuat kolom `Source`
22. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
23. Centang kembali kolom `Alias Name` dan `Source` pada Overlay Column Visibility (pemulihan kolom)
24. Tekan `Esc` (tutup overlay)

### TC-GS-HHR-309: Kolom yang ditampilkan kembali ikut ter-export lagi

25. Klik header kolom Actions `(⋯)` pada tabel Daftar Reader
26. Hilangkan centang kolom `Alias Name` pada Overlay Column Visibility, lalu centang kembali
27. Tekan `Esc` (tutup overlay)
28. Klik ikon Download
29. Klik `Download as CSV`
30. Buka isi file `Handheld-Reader-List.csv` yang diunduh
31. Verifikasi file memuat kolom `Alias Name`

### TC-GS-HHR-307: Download mengikuti Search dan Filter yang aktif

32. Ketik Search `Gudang`, tekan Enter
33. Klik ikon Filter
34. Pilih `Available` pada field `Status`
35. Klik `[Apply]`
36. Klik ikon Download
37. Klik `Download as CSV`
38. Buka isi file `Handheld-Reader-List.csv` yang diunduh
39. Verifikasi file memuat baris header
40. Verifikasi file memuat tepat 1 baris data, yaitu `Gudang Reader - 1`, ditambah baris header
41. Klik `[Clear Field]` pada panel Filter
42. Klik `[Apply]`
43. Klik ikon Filter untuk menutup panel
44. Klik ikon panah `(←)` pada search box

### TC-GS-HHR-313: Download saat hasil nol baris tetap aktif dan berisi header saja

45. Ketik Search `zzzz`, tekan Enter
46. Verifikasi tombol Download aktif
47. Klik ikon Download
48. Klik `Download as CSV`
49. Verifikasi tidak ada toast
50. Buka isi file `Handheld-Reader-List.csv` yang diunduh
51. Verifikasi file memuat baris header kolom yang tampil
52. Verifikasi file tidak memuat baris data (hanya berisi baris header)
53. Klik ikon panah `(←)` pada search box

### TC-GS-HHR-306: Download tanpa Search atau Filter mengekspor seluruh baris, bukan satu halaman

54. Logout
55. Login sebagai Total Control Client L (`totalControl_automated_{namaClient}@qwertysystem.net` dengan namaClient Client L, `Spectra.env.GS_CLIENTL_TC_PASSWORD`)
56. Buka Global Settings > Hardware > Handheld Reader
57. Klik ikon Download
58. Klik `Download as CSV`
59. Verifikasi tidak ada toast sukses
60. Verifikasi file `Handheld-Reader-List.csv` terunduh
61. Buka isi file `Handheld-Reader-List.csv` yang diunduh
62. Verifikasi file memuat baris header
63. Verifikasi file berisi 26 baris data ditambah baris header (bukan 10 baris halaman aktif)

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`, section 4a-6.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 310, 311, 308, 309 (semua baris, tanpa Search dan Filter), lalu 307 dan 313 (Search dan Filter aktif, dikosongkan sesudahnya), dan TC-GS-HHR-306 di akhir karena memerlukan ganti akun ke Client L. Urutan di `tc-hardware-handheld-reader.md`: 306 sampai 311, 313.
- Langkah penghubung (aksi tanpa `Verifikasi`): menutup overlay dengan `Esc`; membuka isi berkas unduhan; memulihkan kolom `Alias Name` dan `Source` sesudah TC-GS-HHR-308; mengosongkan Filter dan Search sesudah TC-GS-HHR-307 dan Search sesudah TC-GS-HHR-313; logout, login Client L, dan membuka halaman pada langkah 54 sampai 56.
- Asersi absence atas state sementara (toast sukses atau toast peringatan) diletakkan segera sesudah klik pilihan format dan sebelum asersi berkas; klik pilihan format menjadi anchor positif yang buktinya menyusul pada asersi berkas terunduh atau isi berkas. Asersi absence kolom pada berkas (TC-GS-HHR-308) didahului `Verifikasi` kolom lain yang tampil pada berkas yang sama; asersi "tidak memuat baris data" (TC-GS-HHR-313) didahului `Verifikasi` baris header pada berkas yang sama.
- Spec memuat 63 langkah (di atas smell sekitar 35 langkah). Alasan: seluruhnya satu kelas harness (fungsional: Download daftar reader), satu dataset Client A (Seed Reader A) ditambah satu blok Client L dengan Step ganti akun eksplisit dan bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal; tiap blok mengunduh berkasnya sendiri, memulihkan state (kolom, Search, Filter) sebelum blok berikutnya, dan tidak mengubah data reader.
- Pembagian TC lintas spec: isi sel berkas (TC-GS-HHR-312) dan escape CSV dengan BOM (TC-GS-HHR-314) ada di spec 058 (kelas binary buffer); kegagalan Download (TC-GS-HHR-315) di spec 028; Download lebih dari 5.000 baris (TC-GS-HHR-316) di spec 059; Download Modal Changelog (TC-GS-HHR-337, 338) di spec 062 dan kegagalannya (TC-GS-HHR-339) di spec 028; Setup Column daftar reader di spec 055.
- Temuan untuk QA:
  - TC-GS-HHR-306: email akun Client L tidak tertulis di Pre-setup TC (hanya pola `totalControl_automated_{namaClient}@qwertysystem.net`) dan env var passwordnya belum terdaftar di `spectra.config.ts` maupun `.env.example`; spec memakai `GS_CLIENTL_TC_PASSWORD` (env baru). Status dan Range Type 26 reader Client L tidak disebut TC.
  - TC-GS-HHR-306, 307, 308, 309, 310, 311, 313: TC tidak menyebut cara menangkap berkas unduhan dan membaca isinya; kemampuan tersebut disediakan tim FE (Prerequisites).
  - TC-GS-HHR-307: Expected a hanya menyebut `Gudang Reader - 1`; spec mengasersi tepat 1 baris data berdasarkan Seed Reader A (hanya DD-02 yang `Gudang` dan `Available`).
  - TC-GS-HHR-308: Expected a ("kolom lain yang tampil ada") tidak menyebut daftar kolom; spec memakai 7 kolom default tersisa. TC tidak menyebut cara menutup Overlay Column Visibility; spec memakai `Esc`.
  - TC-GS-HHR-309: Langkah Uji menggabungkan sembunyikan dan tampilkan kembali dalam satu langkah; spec memisahkan aksi tetapi hanya mengasersi akhir (file memuat `Alias Name`).
  - TC-GS-HHR-313: Expected ("tombol Download aktif") tidak punya langkah observasi terpisah; spec mengasersinya segera sesudah Search `zzzz`.
  - Post Condition semua TC di spec ini `-`; tidak ada yang diasersi.

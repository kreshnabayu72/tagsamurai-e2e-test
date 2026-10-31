---
id: TC-GS-IMPORT-E2E-047-resilience-kegagalan-5xx-timeout-pada-pembacaan-staging-table-upload
title: "Resilience: Kegagalan 5xx dan Timeout pada Pembacaan Staging Table, Upload, dan Confirm Mapping (Toast, Banner Generik, Retry Tanpa Baris Ganda)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-18
  - TC-GS-IMPORT-79
  - TC-GS-IMPORT-80
  - TC-GS-IMPORT-81
  - TC-GS-IMPORT-578
  - TC-GS-IMPORT-610
coverage:
  web: automated
---

# Resilience: Kegagalan 5xx dan Timeout pada Pembacaan Staging Table, Upload, dan Confirm Mapping (Toast, Banner Generik, Retry Tanpa Baris Ganda)

## Prerequisites

- Mode: FE+BE (backend nyata dengan `Spectra.intercept()` parsial). TC-GS-IMPORT-18, 79, 578, dan 610 hanya mengasersi perilaku FE atas respons yang dipaksa dan dapat dijalankan juga sebagai `Mode: mock`; TC-GS-IMPORT-80 dan 81 mengasersi state server (jumlah notifikasi lonceng, draft terbentuk) sehingga membutuhkan backend nyata. Suite serial (`parallel: false`); lihat `suite.md`.
- Intercept (endpoint dari alur Import yang sama dengan permintaan nyata halaman):
  - Pembacaan Staging Table dibalas 500 (TC-GS-IMPORT-18).
  - Permintaan upload dibalas 500 (TC-GS-IMPORT-79) atau ditahan tanpa respons (TC-GS-IMPORT-610).
  - Permintaan Confirm Mapping dibalas 500 (TC-GS-IMPORT-80), dibalas 500 satu kali (TC-GS-IMPORT-81), atau ditahan tanpa respons (TC-GS-IMPORT-578).
  - Intercept dilepas segera setelah pemicu selesai. Batas waktu permintaan FE tidak tertulis di TC; spec menunggu sampai FE menampilkan toast timeout.
- Akun, password lewat env:
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD` (TC-GS-IMPORT-18; akun default suite, login di hook `before`).
  - Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, `Spectra.env.GS_CLIENTC_TC_PASSWORD` (TC-GS-IMPORT-79, 80, 578, 610, 81; login UI lewat langkah ganti akun). Hook `after` mengembalikan sesi ke akun default suite.
  - Password tidak ditulis di spec atau fixture.
- Data: berkas `brand-12.csv` (D-01; header `Brand Name`, 12 baris). Client C tanpa draft Tab Brand sebelum tiap TC (Kontrak Fixture R1); Client A memakai draft sesuai kondisi suite (TC-GS-IMPORT-18 tidak mensyaratkan draft).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import untuk akun aktor.
- Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor spec ini diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: intercept dilepas di tiap blok; hook `after` melepas intercept yang tersisa dan mereset draft Brand Client C (R1).

## Test Steps

### TC-GS-IMPORT-18: Pembacaan Staging Table gagal menampilkan pesan dan Try Again

1. Aktifkan intercept network yang membuat pembacaan Staging Table gagal 500
2. Buka menu Import dari sidebar
3. Verifikasi pesan "Unable to load this data." tampil di area tabel
4. Verifikasi tombol `[Try Again]` tampil
5. Hapus intercept network
6. Klik `[Try Again]`
7. Verifikasi data dimuat ulang dan state normal tampil
8. Verifikasi pesan error tidak tampil

### TC-GS-IMPORT-79: Kegagalan teknis saat upload

9. Ganti akun: login UI sebagai Total Control Client C (Client C tanpa draft Tab Brand), buka Import > Brand
10. Aktifkan intercept network yang membuat permintaan upload gagal 500
11. Klik [Upload File]
12. Pilih berkas `brand-12.csv` di file picker
13. Hapus intercept network
14. Verifikasi toast error persisten: "Error, failed to upload file."
15. Verifikasi Modal Column Mapping tidak terbuka
16. Verifikasi halaman tetap menampilkan Dropzone tanpa draft
17. Tutup toast "Error, failed to upload file."

### TC-GS-IMPORT-80: Kegagalan teknis saat Confirm Mapping menampilkan banner generik

18. Catat jumlah notifikasi lonceng
19. Aktifkan intercept network yang membuat permintaan Confirm Mapping gagal 500
20. Klik [Upload File]
21. Pilih berkas `brand-12.csv` di file picker
22. Klik [Confirm Mapping]
23. Hapus intercept network
24. Verifikasi Error Banner generik di dalam modal berheader "Failed to process brand-12.csv. Please try uploading again."
25. Verifikasi Error Banner tanpa rincian per-rule
26. Verifikasi Error Banner tanpa link download
27. Verifikasi dropdown mapping yang diisi tetap ada
28. Verifikasi tidak ada baris parsial di Staging Table
29. Verifikasi jumlah notifikasi lonceng sama dengan jumlah yang dicatat pada langkah 18
30. Klik [Cancel] pada Modal Column Mapping

### TC-GS-IMPORT-578: Timeout saat Confirm Mapping

31. Klik [Upload File]
32. Pilih berkas `brand-12.csv` di file picker
33. Aktifkan intercept network yang menahan respons permintaan Confirm Mapping tanpa mengembalikan respons
34. Klik [Confirm Mapping]
35. Tunggu hingga batas waktu permintaan habis dan toast timeout tampil
36. Hapus intercept network
37. Verifikasi toast error persisten: "Connection problem. Please try again."
38. Verifikasi toast tanpa tombol aksi
39. Verifikasi Modal Column Mapping tetap terbuka dengan dropdown Brand Name `Brand Name`
40. Verifikasi tombol `[Confirm Mapping]` Enabled
41. Verifikasi tidak ada Error Banner kegagalan teknis
42. Verifikasi halaman di balik modal tetap menampilkan Dropzone tanpa draft
43. Tutup toast "Connection problem. Please try again."
44. Klik [Cancel] pada Modal Column Mapping

### TC-GS-IMPORT-610: Timeout saat Upload File

45. Aktifkan intercept network yang menahan respons permintaan upload tanpa mengembalikan respons
46. Klik [Upload File]
47. Pilih berkas `brand-12.csv` di file picker
48. Tunggu hingga batas waktu permintaan habis dan toast timeout tampil
49. Hapus intercept network
50. Verifikasi toast error persisten: "Connection problem. Please try again."
51. Verifikasi toast tanpa tombol aksi
52. Verifikasi Modal Column Mapping tidak terbuka
53. Verifikasi halaman tetap menampilkan Dropzone tanpa draft
54. Tutup toast "Connection problem. Please try again."
55. Klik [Upload File]
56. Pilih berkas `brand-12.csv` di file picker
57. Verifikasi Modal Column Mapping `Column Mapping: Brand` terbuka
58. Klik [Cancel] pada Modal Column Mapping

### TC-GS-IMPORT-81: Retry Confirm Mapping setelah kegagalan teknis

59. Aktifkan intercept network yang membuat permintaan Confirm Mapping gagal 500 satu kali
60. Klik [Upload File]
61. Pilih berkas `brand-12.csv` di file picker
62. Klik [Confirm Mapping]
63. Verifikasi Error Banner tampil di Modal Column Mapping dengan header "Failed to process brand-12.csv. Please try uploading again."
64. Klik [Confirm Mapping] lagi
65. Verifikasi toast sukses: "Success, row has been added."
66. Verifikasi draft Brand terbentuk dengan 12 baris tanpa baris ganda (Total Rows 12)

## Notes

- Mode: FE+BE (intercept parsial di atas backend nyata). Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fault injection / resilience (kelas b, prinsip 13b).
- Spec memuat 66 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (kegagalan 5xx dan timeout pada alur Upload dan Confirm Mapping), tiap blok berdiri sendiri dengan intercept dan kondisi awal sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan blok: TC-GS-IMPORT-81 di akhir karena membentuk draft Brand 12 baris; blok lain mensyaratkan Client C tanpa draft. TC-GS-IMPORT-18 di awal memakai akun default suite sehingga hook `before` tidak perlu mengganti akun.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5, 13, 23, 36, 49 (melepas intercept segera setelah pemicu); langkah 9 (ganti akun); langkah 30, 44, 58 (menutup Modal Column Mapping dengan `[Cancel]` agar blok berikutnya mulai dari layar awal); langkah 35 dan 48 (menunggu batas waktu permintaan FE); langkah 17, 43, 54 (menutup toast error persisten sebelum blok berikutnya, supaya asersi toast berikutnya tidak lulus dari toast basi; TC tidak menyebut penutupan toast).
- Pada TC-GS-IMPORT-80 dan 578, `Verifikasi` absence (langkah 28, 41, 42) memakai Error Banner atau toast hasil kegagalan sebagai anchor (respons gagal sudah diterima).
- Temuan untuk QA:
  - TC-GS-IMPORT-578 dan 610 menyebut "Tunggu hingga batas waktu permintaan habis" tanpa menyebut durasi batas waktu permintaan FE; spec menunggu sampai toast timeout tampil.
  - Post Condition TC-GS-IMPORT-81 ("Draft Brand 12 baris") setara dengan Expected c dan sudah diasersi.

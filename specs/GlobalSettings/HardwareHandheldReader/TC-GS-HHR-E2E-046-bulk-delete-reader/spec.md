---
id: TC-GS-HHR-E2E-046-bulk-delete-reader
title: "Bulk Delete Reader: Screening Dialog, Cancel, Delete Jalur A dan B, Pengembalian Kuota, dan Pencatatan Log per Reader"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-214
  - TC-GS-HHR-215
  - TC-GS-HHR-216
  - TC-GS-HHR-217
  - TC-GS-HHR-220
coverage:
  web: automated
---

# Bulk Delete Reader: Screening Dialog, Cancel, Delete Jalur A dan B, Pengembalian Kuota, dan Pencatatan Log per Reader

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini menghapus reader Seed Reader A dan memulihkannya (lihat butir pemulihan); aksi Bulk Delete berada sesudah semua screening yang membutuhkan baris tetap ada.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka kecuali sesudah pemulihan (muat ulang halaman) atau pembacaan log (kembali ke halaman).
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Seed Reader A Client A (Tabel Data Uji Dinamis TC; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`): 10 reader DD-01 s.d. DD-10, kartu kuota `Short Range` `5 of 8` dan `Long Range` `5 of 6`, plan Growth, format tanggal default `dd/MM/yy` 24-hour. Spec memakai DD-01 (`Zebra RFID Reader - 1`, SN-HHR-00101, Jalur A, Long Range), DD-07 (`Honeywell CK65 - 1`, SN-HHR-00108, Jalur B, Long Range), DD-08 (`Unitech EA520 - 1`, SN-HHR-00109, Jalur B, Short Range), DD-09 (Jalur B, Long Range), DD-03 (`Zebra Mobile Reader - 1`, Jalur A, Damaged, Long Range), dan DD-04 (`Gudang Reader - 2`, Jalur A, Missing, Short Range). Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya; urutan bullet dialog mengikuti urutan baris tabel.
- Pemulihan Seed Reader A: TC menyatakan Seed Reader A dipulihkan oleh fixture backend sebelum tiap TC yang mensyaratkannya, dan nilai Expected (pagination, kartu kuota) mengasumsikan state awal tiap TC. Spec memulihkannya sebelum tiap TC yang menghapus data (kemampuan "pulihkan Seed Reader A lewat fixture backend" disediakan tim FE/BE tanpa endpoint yang dikarang), lalu memuat ulang halaman. Hook `before` dan `after` juga memulihkannya.
- Tiga surface log (dibaca TC-GS-HHR-220): Changelog Handheld Reader (ikon Changelog di halaman), System Log aktor (Global Settings > User > Detail akun aktor > tab System Log), dan Activity Log (Global Settings > Activity Log > tab User Action). Baseline jumlah entri dicatat per surface sebelum aksi pemicu.
- Guided Tooltip: hook suite `before` menyetel flag Guided Tooltip halaman Handheld Reader menjadi true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pembacaan dialog, teks pagination, kartu kuota, dan tiga surface log (jumlah dan isi entri); pemulihan Seed Reader A lewat fixture backend.
- State global: tidak ada yang diubah selain Seed Reader A (dipulihkan seperti di atas) dan flag Guided Tooltip (diatur hook suite).

## Test Steps

### TC-GS-HHR-214: Screening dialog bulk Delete untuk seleksi Jalur A dan Jalur B

1. Centang checkbox baris DD-01 (Jalur A)
2. Centang checkbox baris DD-07 (Jalur B)
3. Klik tombol `Bulk Action`
4. Klik `Delete`
5. Verifikasi dialog tampil utuh: Judul `Delete Readers`, Body berisi bullet `Honeywell CK65 - 1 (SN-HHR-00108)` lalu bullet `Zebra RFID Reader - 1 (SN-HHR-00101)`, kalimat dampak `Their license quota will be returned.`, kalimat tambahan `Official units will be available again in Hardware Stock.`, kalimat penutup `Are you sure you want to delete them? This action cannot be undone.`, Footer `[Cancel]` dan `[Delete]` (`[Delete]` `severity="danger"`)
6. Klik `[Cancel]`
7. Verifikasi tidak ada toast
8. Verifikasi dialog tertutup
9. Verifikasi baris DD-01 dan DD-07 tetap tercentang
10. Verifikasi baris DD-01 dan DD-07 tetap ada di tabel
11. Klik ikon `×`

### TC-GS-HHR-215: Dialog bulk Delete seleksi Jalur B saja tidak memuat kalimat Hardware Stock

12. Centang checkbox baris DD-07
13. Centang checkbox baris DD-08
14. Klik tombol `Bulk Action`
15. Klik `Delete`
16. Verifikasi dialog tampil: Judul `Delete Readers`, Body berisi bullet `Honeywell CK65 - 1 (SN-HHR-00108)` lalu bullet `Unitech EA520 - 1 (SN-HHR-00109)`, kalimat dampak `Their license quota will be returned.`, kalimat penutup `Are you sure you want to delete them? This action cannot be undone.`
17. Verifikasi Body dialog tidak memuat kalimat tentang Hardware Stock
18. Klik `[Cancel]`
19. Klik ikon `×`

### TC-GS-HHR-217: Bulk Delete reader Jalur A menghapus baris dan mengembalikan kuota

20. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
21. Centang checkbox baris DD-03 (Damaged)
22. Centang checkbox baris DD-04 (Missing)
23. Klik tombol `Bulk Action`
24. Klik `Delete`
25. Klik `[Delete]` pada dialog
26. Verifikasi muncul toast sukses: "Success, reader has been deleted."
27. Verifikasi baris DD-03 dan DD-04 hilang dari tabel
28. Verifikasi pagination menampilkan `Showing 1 - 8 of 8 readers`
29. Verifikasi kartu `Long Range` menjadi `4 of 6`, `2 remaining`
30. Verifikasi kartu `Short Range` menjadi `4 of 8`, `4 remaining`

### TC-GS-HHR-216: Bulk Delete reader Jalur B menghapus baris dan mengembalikan kuota per Range Type

31. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
32. Centang checkbox baris DD-07
33. Centang checkbox baris DD-08
34. Centang checkbox baris DD-09
35. Klik tombol `Bulk Action`
36. Klik `Delete`
37. Klik `[Delete]` pada dialog
38. Verifikasi muncul toast sukses: "Success, reader has been deleted."
39. Verifikasi baris DD-07, DD-08, dan DD-09 hilang dari tabel
40. Verifikasi pagination menampilkan `Showing 1 - 7 of 7 readers`
41. Verifikasi kartu `Long Range` menjadi `3 of 6`, `3 remaining`
42. Verifikasi kartu `Short Range` menjadi `4 of 8`, `4 remaining`
43. Verifikasi Bulk Action Bar hilang
44. Verifikasi seleksi di-reset (tidak ada checkbox tercentang)

### TC-GS-HHR-220: Bulk Delete menulis satu entri per reader pada tiga surface log

45. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
46. Catat baseline Changelog: buka ikon Changelog, catat jumlah entri, tutup dengan `✕`
47. Catat baseline System Log aktor: buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri
48. Catat baseline Activity Log: buka Global Settings > Activity Log > tab User Action, catat jumlah entri
49. Buka Global Settings > Hardware > Handheld Reader
50. Centang checkbox baris DD-07
51. Centang checkbox baris DD-08
52. Klik tombol `Bulk Action`
53. Klik `Delete`
54. Klik `[Delete]` pada dialog
55. Tunggu aksi selesai (dialog tertutup)
56. Buka ikon Changelog
57. Verifikasi jumlah entri Changelog bertambah tepat 2 dibanding baseline langkah 46
58. Verifikasi dua entri baru masing-masing Action `Delete`, Field `Device Name`, Old Value nama reader (`Honeywell CK65 - 1` dan `Unitech EA520 - 1`), New Value `—`
59. Tutup Modal Changelog dengan `✕`
60. Buka Global Settings > User > Detail akun aktor > tab System Log
61. Verifikasi jumlah entri System Log aktor bertambah tepat 2 dibanding baseline langkah 47
62. Buka Global Settings > Activity Log > tab User Action
63. Verifikasi jumlah entri Activity Log bertambah tepat 2 dibanding baseline langkah 48
64. Verifikasi dua entri baru dengan Action `Delete`, satu per reader
65. Verifikasi tidak ada entri gabungan satu baris untuk dua reader

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 3k).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di spec: 214 dan 215 (screening dengan `[Cancel]`, tidak menghapus), lalu 217, 216, dan 220 (Bulk Delete yang menghapus data) paling akhir. TC-GS-HHR-217 memakai DD-03 dan DD-04 yang tidak bersinggungan dengan 216 dan 220, tetapi nilai Expected tiap TC (pagination, kartu kuota) mengasumsikan state awal sehingga Seed Reader A dipulihkan sebelum tiap eksekusi. Menyimpang dari urutan nomor TC sumber (216 sebelum 217).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11, 19 (mengosongkan seleksi lewat `×`), langkah 18 (`[Cancel]` menutup dialog TC-GS-HHR-215 yang di TC hanya diamati), langkah 20, 31, dan 45 (pemulihan dan muat ulang), langkah 46 sampai 48 (baseline jumlah entri sebelum aksi pemicu; S-12), langkah 49 (kembali ke halaman Handheld Reader), langkah 55 (Tunggu aksi selesai karena langkah berikutnya berpindah surface; 8b butir 8), langkah 56, 60, dan 62 (membuka surface log), dan langkah 59 (menutup Modal Changelog).
- Langkah 17 (tidak ada kalimat Hardware Stock) didahului langkah 16 yang membuktikan Body dialog tampil beserta kalimat lainnya (anchor positif; 8b butir 2). Langkah 65 (tidak ada entri gabungan) didahului langkah 64 yang membuktikan dua entri per reader pada surface yang sama. Asersi jumlah entri memakai selisih terhadap baseline (S-12).
- Spec memuat 65 langkah (di atas sekitar 35 langkah). Alasan: seluruh blok satu kelas (Bulk Delete Seed Reader A), tiap eksekusi memakai pemulihan Seed Reader A sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain, semua aksi yang menghapus data berada di akhir, dan blok log (langkah 46 sampai 65) adalah blok baca-log berpola.
- Opsi bulk per status (TC-GS-HHR-196 sampai 200) ada di spec 044; Bulk Mark as (TC-GS-HHR-207 sampai 213, 218, 219, 461) di spec 045; Delete tunggal di spec 042; resilience 5xx Bulk Delete (TC-GS-HHR-226) di spec 027.
- Temuan untuk QA:
  - TC-GS-HHR-217 Expected d ("Unit `SN-HHR-00103` dan `SN-HHR-00104` kembali `Available` di Hardware Stock (TC section 7)") dan Post Condition c membutuhkan pembacaan Admin Console > Hardware Stock (akun Principal, konteks lain) yang tidak punya langkah di TC ini. Spec tidak mengasersinya agar tetap satu konteks (Global Settings Client A); klausa itu perlu ditempatkan di spec sinkronisasi Hardware Stock (spec 068 menurut plan, mis. TC-GS-HHR-382 untuk Delete Jalur A) atau diputuskan QA.
  - Post Condition TC-GS-HHR-216 ("Reader Jalur B tidak mengubah stok Admin Console") dan TC-GS-HHR-217 (log per reader) tanpa langkah observasi di TC masing-masing tidak diasersi; log per reader hanya diasersi pada TC-GS-HHR-220 yang punya langkah observasinya.
  - TC-GS-HHR-220 Expected a menulis Old Value "nama reader" tanpa menyebut SKU atau Alias Name; spec memakai Device Name tanpa SKU (`Honeywell CK65 - 1` dan `Unitech EA520 - 1`) karena DD-07 dan DD-08 berstatus Jalur B tanpa SKU.
  - TC-GS-HHR-220 Expected b tidak menyebut isi kolom entri System Log aktor selain "2 entri baru"; spec mengasersi hanya selisih jumlah.
  - TC-GS-HHR-215 Langkah 5 hanya "Amati dialog" tanpa menutup dialog; spec menambahkan `[Cancel]` sebagai langkah penghubung (langkah 18).
  - Seed Reader A tidak diberi suffix per run (nama literal) dan mekanisme pemulihannya hanya disebut "fixture backend" di Catatan TC; pengecualian Population S-12 untuk HHR belum ada di konvensi.

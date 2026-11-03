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
- Data Dinamis (Seed Reader A, dipulihkan fixture backend): Seed Reader A Client A (Tabel Data Uji Dinamis TC; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`): 10 reader DD-01 s.d. DD-10, kartu kuota `Short Range` `5 of 8` dan `Long Range` `5 of 6`, plan Growth, format tanggal default `dd/MM/yy` 24-hour. Spec memakai DD-01 (`Zebra RFID Reader - 1`, SN-HHR-00101, Jalur A, Long Range), DD-07 (`Honeywell CK65 - 1`, SN-HHR-00108, Jalur B, Long Range), DD-08 (`Unitech EA520 - 1`, SN-HHR-00109, Jalur B, Short Range), dan DD-09 (Jalur B, Long Range). Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya (pengecualian S-12 Population Seed Reader A HHR); urutan bullet dialog mengikuti urutan baris tabel.
- Pemulihan Seed Reader A: TC menyatakan Seed Reader A dipulihkan oleh fixture backend sebelum tiap TC yang mensyaratkannya, dan nilai Expected (pagination, kartu kuota) mengasumsikan state awal tiap TC. Spec memulihkannya sebelum tiap TC yang menghapus data (kemampuan "pulihkan Seed Reader A lewat fixture backend" disediakan tim FE/BE tanpa endpoint yang dikarang), lalu memuat ulang halaman. Hook `before` dan `after` juga memulihkannya.
- Tiga surface log (dibaca TC-GS-HHR-220): Changelog Handheld Reader (ikon Changelog di halaman), System Log aktor (Global Settings > User > Detail akun aktor > tab System Log), dan Activity Log (tab `User Action`, dibuka lewat Global Settings > Activity Log). Baseline jumlah entri dicatat per surface sebelum aksi pemicu.
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
18. Klik `[Cancel]` pada dialog
19. Verifikasi dialog tertutup tanpa perubahan
20. Verifikasi baris DD-07 dan DD-08 tetap ada di tabel
21. Verifikasi seleksi dipertahankan: `2 Readers selected`
22. Klik ikon `×`

### TC-GS-HHR-216: Bulk Delete reader Jalur B menghapus baris dan mengembalikan kuota per Range Type

23. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
24. Centang checkbox baris DD-07
25. Centang checkbox baris DD-08
26. Centang checkbox baris DD-09
27. Klik tombol `Bulk Action`
28. Klik `Delete`
29. Klik `[Delete]` pada dialog
30. Verifikasi muncul toast sukses: "Success, reader has been deleted."
31. Verifikasi baris DD-07, DD-08, dan DD-09 hilang dari tabel
32. Verifikasi pagination menampilkan `Showing 1 - 7 of 7 readers`
33. Verifikasi kartu `Long Range` menjadi `3 of 6`, `3 remaining`
34. Verifikasi kartu `Short Range` menjadi `4 of 8`, `4 remaining`
35. Verifikasi Bulk Action Bar hilang
36. Verifikasi seleksi di-reset (tidak ada checkbox tercentang)

### TC-GS-HHR-220: Bulk Delete menulis satu entri per reader pada tiga surface log

37. Pulihkan Seed Reader A lewat fixture backend, lalu muat ulang halaman
38. Catat baseline Changelog: buka ikon Changelog, catat jumlah entri, tutup dengan `✕`
39. Catat baseline System Log aktor: buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri
40. Catat baseline Activity Log (tab `User Action`): buka Global Settings > Activity Log > tab User Action, catat jumlah entri
41. Buka Global Settings > Hardware > Handheld Reader
42. Centang checkbox baris DD-07
43. Centang checkbox baris DD-08
44. Klik tombol `Bulk Action`
45. Klik `Delete`
46. Klik `[Delete]` pada dialog
47. Tunggu aksi selesai (dialog tertutup)
48. Buka ikon Changelog
49. Verifikasi jumlah entri Changelog bertambah tepat 2 dibanding baseline langkah 38
50. Verifikasi dua entri baru pada dua baris teratas urutan default `Date` terbaru, masing-masing Action `Delete`, Field `Device Name`, Old Value nama reader (`Honeywell CK65 - 1` dan `Unitech EA520 - 1`), New Value `—`
51. Tutup Modal Changelog dengan `✕`
52. Buka Global Settings > User > Detail akun aktor > tab System Log
53. Verifikasi jumlah entri System Log aktor bertambah tepat 2 dibanding baseline langkah 39
54. Buka Activity Log (tab `User Action`) lewat Global Settings > Activity Log > tab User Action
55. Verifikasi jumlah entri Activity Log (tab `User Action`) bertambah tepat 2 dibanding baseline langkah 40
56. Verifikasi dua entri baru pada dua baris teratas urutan default `Date` terbaru dengan Action `Delete`, satu per reader
57. Verifikasi tidak ada entri gabungan satu baris untuk dua reader

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 3k).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembagian TC lintas spec: TC-GS-HHR-217 (Bulk Delete Jalur A beserta efeknya di Admin Console > Hardware Stock) ada di spec 068.
- Pengecualian S-12 Population Seed Reader A HHR berlaku untuk Seed Reader A (nama literal tanpa suffix `{runId}`); pemulihannya dijamin fixture backend dan dinyatakan di `suite.md`.
- Urutan TC di spec: 214 dan 215 (screening dengan `[Cancel]`, tidak menghapus), lalu 216 dan 220 (Bulk Delete yang menghapus data) paling akhir. Nilai Expected tiap TC (pagination, kartu kuota) mengasumsikan state awal sehingga Seed Reader A dipulihkan sebelum tiap eksekusi yang menghapus data.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11 dan 22 (mengosongkan seleksi lewat `×`), langkah 23 dan 37 (pemulihan dan muat ulang), langkah 38 sampai 40 (baseline jumlah entri sebelum aksi pemicu; S-12), langkah 41 (kembali ke halaman Handheld Reader), langkah 47 (Tunggu aksi selesai karena langkah berikutnya berpindah surface; 8b butir 8), langkah 48, 52, dan 54 (membuka surface log), dan langkah 51 (menutup Modal Changelog).
- Langkah 17 (tidak ada kalimat Hardware Stock) didahului langkah 16 yang membuktikan Body dialog tampil beserta kalimat lainnya (anchor positif; 8b butir 2). Langkah 57 (tidak ada entri gabungan) didahului langkah 56 yang membuktikan dua entri per reader pada surface yang sama. Asersi jumlah entri memakai selisih terhadap baseline (S-12). Baseline Changelog, System Log aktor, dan Activity Log dicatat pada langkah 38, 39, dan 40 sehingga Verifikasi selisih pada langkah 49, 53, dan 55 merujuk ke ketiganya.
- Entri baru pada langkah 50 dan 56 dibaca pada baris teratas urutan default `Date` terbaru setelah selisih jumlah dari baseline dibuktikan (langkah 49 dan 55); jumlah baris teratas yang dibaca = selisih, dan bila dua entri jatuh dalam menit yang sama himpunan dua baris teratas diasersi tanpa mengandalkan urutan di antaranya (S-14). Activity Log yang dibaca adalah tab `User Action`, bukan tab `Session` (PRD Activity Log).
- Spec memuat 57 langkah (di atas sekitar 35 langkah). Alasan: seluruh blok satu kelas (Bulk Delete Seed Reader A), tiap eksekusi memakai pemulihan Seed Reader A sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain, semua aksi yang menghapus data berada di akhir, dan blok log (langkah 38 sampai 57) adalah blok baca-log berpola.
- Opsi bulk per status (TC-GS-HHR-196 sampai 200) ada di spec 044; Bulk Mark as (TC-GS-HHR-207 sampai 213, 218, 219, 461) di spec 045; Delete tunggal di spec 042; resilience 5xx Bulk Delete (TC-GS-HHR-226) di spec 027.
- Temuan untuk QA:
  - Post Condition TC-GS-HHR-216 ("Satu entri per reader pada tiga surface log" dan "Reader Jalur B tidak mengubah stok Admin Console") tanpa langkah observasi di TC tidak diasersi; log per reader hanya diasersi pada TC-GS-HHR-220 yang punya langkah observasinya.
  - TC-GS-HHR-220 Expected a menulis Old Value "nama reader" tanpa menyebut SKU atau Alias Name; spec memakai Device Name tanpa SKU (`Honeywell CK65 - 1` dan `Unitech EA520 - 1`) karena DD-07 dan DD-08 berstatus Jalur B tanpa SKU.
  - TC-GS-HHR-220 Expected b tidak menyebut isi kolom entri System Log aktor selain "2 entri baru"; spec mengasersi hanya selisih jumlah.

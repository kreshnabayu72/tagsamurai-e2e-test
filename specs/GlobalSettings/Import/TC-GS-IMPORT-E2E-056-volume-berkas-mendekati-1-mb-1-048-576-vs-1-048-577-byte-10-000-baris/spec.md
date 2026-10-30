---
id: TC-GS-IMPORT-E2E-056-volume-berkas-mendekati-1-mb-1-048-576-vs-1-048-577-byte-10-000-baris
title: "Volume: Berkas Mendekati 1 MB (1.048.576 vs 1.048.577 Byte) dan 10.000 Baris per Draft (10.001 Ditolak, 9995+6 Ditolak, 9995+5 Diterima, Baris Kosong Tidak Dihitung)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-77
  - TC-GS-IMPORT-78
  - TC-GS-IMPORT-91
  - TC-GS-IMPORT-92
  - TC-GS-IMPORT-584
  - TC-GS-IMPORT-812
coverage:
  web: automated
---

# Volume: Berkas Mendekati 1 MB (1.048.576 vs 1.048.577 Byte) dan 10.000 Baris per Draft (10.001 Ditolak, 9995+6 Ditolak, 9995+5 Diterima, Baris Kosong Tidak Dihitung)

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Akun: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, `Spectra.env.GS_CLIENTC_TC_PASSWORD`; login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis yang disediakan tim FE/BE: generator berkas besar dan skrip seed; reset Client C ke tanpa draft Tab Brand (Kontrak Fixture R1) sebelum blok yang mensyaratkannya.
- Berkas uji (disediakan tim QA sesuai D-07; tiap nama berkas satu isi, header `Brand Name`):
  - `brand-1mb.csv`: 1.048.576 byte, UTF-8 tanpa BOM, akhir baris LF; header + LF (11 byte); baris 1 sampai 9986 `Brand NNNN` (NNNN = 0001 sampai 9986) + satu spasi + huruf `x` hingga panjang nama 104 karakter (105 byte dengan LF); baris 9987 `Brand 9987` + spasi + huruf `x` hingga panjang nama 34 karakter (35 byte dengan LF); total 11 + 9986 x 105 + 35 = 1.048.576 byte.
  - `brand-1mb-plus1.csv`: 1.048.577 byte; isi sama dengan `brand-1mb.csv` dengan satu huruf `x` tambahan di akhir nama baris 9987 (36 byte dengan LF).
  - `brand-10001.csv`: 10001 baris data `Brand 00001` sampai `Brand 10001` (ukuran di bawah 1 MB).
  - `brand-10000-blank.csv`: 10000 baris data unik `Brand 0001` sampai `Brand 10000` diselingi 5 baris kosong sepenuhnya.
  - `brand-10.csv`: 10 baris `Brand Baru 01` sampai `Brand Baru 10`; `brand-5.csv`: 5 baris `Brand Baru 1` sampai `Brand Baru 5`.
  - D-16: draft Brand 9995 baris `pending` (`Brand 00001` sampai `Brand 09995`) pada Client C, disiapkan oleh langkah 32 lewat skrip fixture sebelum TC-GS-IMPORT-77 (tidak berubah sesudah penolakan sehingga dipakai ulang oleh TC-GS-IMPORT-78).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Brand Client C direset (R1) setelah blok yang menciptakan draft.

## Test Steps

### TC-GS-IMPORT-92: Berkas 1.048.577 byte tersaring

1. Klik [Upload File]
2. Pilih berkas `brand-1mb-plus1.csv` di file picker
3. Verifikasi berkas tidak diproses tanpa toast
4. Verifikasi berkas tidak diproses tanpa pesan error
5. Verifikasi Modal Column Mapping tidak terbuka
6. Verifikasi halaman tetap menampilkan Dropzone tanpa draft

### TC-GS-IMPORT-91: Berkas tepat 1 MB lolos

7. Klik [Upload File]
8. Pilih berkas `brand-1mb.csv` di file picker
9. Verifikasi Modal Column Mapping `Column Mapping: Brand` terbuka
10. Klik [Cancel] pada Modal Column Mapping

### TC-GS-IMPORT-812: Upload 10.001 baris tanpa draft ditolak all-or-nothing

11. Klik [Upload File]
12. Pilih berkas `brand-10001.csv` di file picker
13. Klik [Confirm Mapping] tanpa mengubah dropdown File Column dari hasil auto-match
14. Verifikasi tidak ada toast setelah langkah 13
15. Verifikasi seluruh berkas ditolak (all-or-nothing) dan Modal Column Mapping tetap terbuka
16. Verifikasi Error Banner hanya memuat baris pesan "Exceeds maximum 10.000 rows per session"
17. Verifikasi Error Banner tanpa header jumlah baris yang gagal diimpor
18. Verifikasi Error Banner tanpa nomor baris
19. Klik [Cancel]
20. Verifikasi modal tertutup tanpa dialog Unsaved Changes
21. Verifikasi halaman Import > Brand menampilkan Dropzone tanpa Staging Table
22. Verifikasi Unsaved Banner tidak tampil

### TC-GS-IMPORT-584: Baris kosong tidak dihitung pada batas 10000 baris

23. Klik [Upload File]
24. Pilih berkas `brand-10000-blank.csv` di file picker
25. Klik [Confirm Mapping] tanpa mengubah dropdown File Column dari hasil auto-match
26. Verifikasi modal tertutup tanpa Error Banner
27. Verifikasi toast "Success, row has been added."
28. Verifikasi Staging Table halaman 1 menampilkan 10 baris `Brand 0001` sampai `Brand 0010` berstatus `pending`
29. Verifikasi Pagination `Showing 1 - 10 of 10000 items`
30. Verifikasi Staging Metric Cards: Total Rows 10000 (Active), Ready to Import 10000, Errors 0 (Disabled), Duplicates 0 (Disabled)
31. Verifikasi pesan "Exceeds maximum 10.000 rows per session" tidak tampil
32. Reset Client C ke tanpa draft Tab Brand; siapkan draft D-16 (9995 baris) pada Client C
33. Muat ulang halaman Import > Brand

### TC-GS-IMPORT-77: Upload yang membuat total melebihi 10.000 ditolak all-or-nothing

34. Klik [Upload File]
35. Pilih berkas `brand-10.csv` di file picker
36. Klik [Append Records] pada dialog Append to Draft
37. Klik [Confirm Mapping] tanpa mengubah dropdown File Column dari hasil auto-match
38. Verifikasi seluruh berkas ditolak (all-or-nothing)
39. Verifikasi Error Banner di modal hanya memuat baris pesan "Exceeds maximum 10.000 rows per session"
40. Verifikasi Error Banner tanpa header jumlah baris yang gagal diimpor
41. Verifikasi Error Banner tanpa nomor baris
42. Verifikasi modal tetap terbuka
43. Klik [Cancel]
44. Ubah Rows per page menjadi 100
45. Pindah ke halaman terakhir lewat Pagination
46. Verifikasi halaman terakhir (halaman 100) memuat 95 baris
47. Verifikasi tidak ada baris `Brand Baru` di halaman terakhir

### TC-GS-IMPORT-78: Upload yang membuat total tepat 10.000 diterima

48. Klik [Upload File]
49. Pilih berkas `brand-5.csv` di file picker
50. Klik [Append Records] pada dialog Append to Draft
51. Klik [Confirm Mapping]
52. Verifikasi berkas diterima dan modal tertutup tanpa Error Banner
53. Ubah Rows per page menjadi 100
54. Pindah ke halaman terakhir lewat Pagination
55. Verifikasi halaman terakhir (halaman 100) memuat 100 baris
56. Verifikasi lima baris `Brand Baru 1` sampai `Brand Baru 5` berada di akhir halaman
57. Reset Client C ke tanpa draft Tab Brand (draft 10000 baris)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: volume data khusus (kelas e, prinsip 13e; draft 9995 dan 10000 baris, berkas mendekati 1 MB).
- Spec memuat 57 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (volume data dan berkas besar), tiap blok berdiri sendiri dengan kondisi awal sendiri (Client C tanpa draft atau draft D-16), dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan blok: blokir lebih dulu (TC-GS-IMPORT-92, 91, 812), lalu TC-GS-IMPORT-584 yang menerima 10000 baris dan memerlukan Client C tanpa draft, kemudian seed D-16 untuk TC-GS-IMPORT-77 (blokir) dan TC-GS-IMPORT-78 (sukses, memakai draft D-16 yang tidak berubah oleh penolakan).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10, 19, 43 (menutup Modal Column Mapping dengan `[Cancel]`); langkah 32 dan 57 (reset dan seed draft); langkah 33 (muat ulang halaman sesudah seed draft D-16); langkah 44, 45, 53, 54 (Rows per page dan halaman terakhir).
- Langkah 21 menjadi anchor positif bagi langkah 22; langkah 28 menjadi anchor bagi langkah 31; langkah 46 menjadi anchor bagi langkah 47. Langkah 14 (absence toast) ditulis tepat sesudah `[Confirm Mapping]` langkah 13 dan mendahului `Verifikasi` artefak; anchor positifnya adalah langkah 15 (modal tetap terbuka) dan langkah 16 (Error Banner).
- Temuan untuk QA:
  - TC-GS-IMPORT-92 mengharapkan berkas "tersaring" tanpa toast dan tanpa pesan error; spec mengasersi tidak adanya toast, pesan error, dan modal sebagai absence dengan Dropzone sebagai anchor.
  - TC-GS-IMPORT-91 dan 92 butuh berkas yang dihasilkan skrip (sekitar 9986 baris); kebutuhan generator berkas dicatat di Prerequisites.

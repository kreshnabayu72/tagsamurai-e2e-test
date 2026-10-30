---
id: TC-GS-IMPORT-E2E-021-penyaringan-berkas-senyap-xlsx-sheet-kosong-format-selain-csv-xlsx
title: "Penyaringan Berkas Senyap: XLSX Sheet Kosong, Format Selain CSV/XLSX, Hanya Header, Enkoding Rusak, 0 Byte, dan Header Plus Baris Kosong"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-89
  - TC-GS-IMPORT-90
  - TC-GS-IMPORT-93
  - TC-GS-IMPORT-95
  - TC-GS-IMPORT-96
  - TC-GS-IMPORT-582
coverage:
  web: automated
---

# Penyaringan Berkas Senyap: XLSX Sheet Kosong, Format Selain CSV/XLSX, Hanya Header, Enkoding Rusak, 0 Byte, dan Header Plus Baris Kosong

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; spec ini tidak menguji navigasi.
- Data: Client C tanpa draft Tab Brand (Kontrak Fixture R1; skrip reset disediakan tim FE/BE). Dropzone dibiarkan tanpa draft sepanjang spec; tidak ada draft yang tercipta. Berkas fixture (D-07, isi literal, satu nama berkas satu isi):
  - `brand-empty-first-sheet.xlsx`: sheet 1 kosong tanpa isi sel; sheet 2 berisi header `Brand Name` dan 3 baris Nikon, Ricoh, Xerox.
  - `notes.txt` (teks biasa); `legacy.xls` (Excel 97-2003, header `Brand Name`, 3 baris Nikon, Ricoh, Xerox); `scan.pdf` (PDF satu halaman).
  - `brand-header-only.csv`: hanya header `Brand Name`, tanpa baris data.
  - `brand-bad-encoding.csv`: CSV Windows-1252 (bukan UTF-8); header `Brand Name`; 3 baris `Café Brand` (byte `0xE9`), Nikon, Ricoh.
  - `empty.csv`: berkas CSV 0 byte.
  - `brand-header-blank.csv`: header `Brand Name` diikuti 3 baris yang seluruh selnya kosong.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker dengan berkas biner (xlsx, xls, pdf, 0 byte, enkoding Windows-1252); skrip reset draft.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-IMPORT-89: XLSX dengan sheet pertama kosong tersaring senyap

1. Klik `[Upload File]`
2. Pilih berkas `brand-empty-first-sheet.xlsx` di file picker
3. Perhatikan halaman
4. Verifikasi halaman tetap menampilkan Dropzone tanpa draft
5. Verifikasi berkas tidak diproses: tanpa toast dan tanpa pesan error
6. Verifikasi Modal Column Mapping tidak terbuka

### TC-GS-IMPORT-90: Berkas berformat selain CSV dan XLSX tersaring

7. Klik `[Upload File]`
8. Pilih berkas `notes.txt` di file picker
9. Perhatikan halaman
10. Verifikasi `notes.txt` tidak diproses: tanpa toast dan tanpa pesan error
11. Klik `[Upload File]`
12. Pilih berkas `legacy.xls` di file picker
13. Perhatikan halaman
14. Verifikasi `legacy.xls` tidak diproses: tanpa toast dan tanpa pesan error
15. Klik `[Upload File]`
16. Pilih berkas `scan.pdf` di file picker
17. Perhatikan halaman
18. Verifikasi `scan.pdf` tidak diproses: tanpa toast dan tanpa pesan error
19. Verifikasi halaman tetap menampilkan Dropzone tanpa draft

### TC-GS-IMPORT-93: Berkas hanya berisi header tanpa baris data tersaring

20. Klik `[Upload File]`
21. Pilih berkas `brand-header-only.csv` di file picker
22. Perhatikan halaman
23. Verifikasi halaman tetap menampilkan Dropzone tanpa draft
24. Verifikasi berkas tidak diproses: tanpa toast dan tanpa pesan error
25. Verifikasi Modal Column Mapping tidak terbuka

### TC-GS-IMPORT-95: Berkas CSV dengan enkoding rusak tersaring

26. Klik `[Upload File]`
27. Pilih berkas `brand-bad-encoding.csv` di file picker
28. Perhatikan halaman
29. Verifikasi halaman tetap menampilkan Dropzone tanpa draft
30. Verifikasi berkas tidak diproses: tanpa toast dan tanpa pesan error
31. Verifikasi Modal Column Mapping tidak terbuka

### TC-GS-IMPORT-96: Berkas 0 byte tersaring

32. Klik `[Upload File]`
33. Pilih berkas `empty.csv` di file picker
34. Perhatikan halaman
35. Verifikasi halaman tetap menampilkan Dropzone tanpa draft
36. Verifikasi berkas tidak diproses: tanpa toast dan tanpa pesan error
37. Verifikasi Modal Column Mapping tidak terbuka

### TC-GS-IMPORT-582: Berkas yang hanya memuat header dan baris kosong sepenuhnya tersaring senyap

38. Klik `[Upload File]`
39. Pilih berkas `brand-header-blank.csv` di file picker
40. Perhatikan halaman
41. Verifikasi halaman tetap menampilkan Dropzone tanpa draft
42. Verifikasi berkas tidak diproses: tanpa toast dan tanpa pesan error
43. Verifikasi Modal Column Mapping tidak terbuka

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (43 langkah). Enam blok homogen (pola: klik `[Upload File]`, pilih berkas, verifikasi tersaring) pada satu Dropzone yang tidak pernah berubah state; tiap blok berdiri sendiri dan tidak membuat data.
- Asersi absence "tanpa toast dan tanpa pesan error" didahului `Verifikasi` Dropzone tampil sebagai anchor positif (halaman telah dimuat dan berada di state Dropzone); pada TC-GS-IMPORT-90 anchor Dropzone ada di langkah 19 untuk ketiga berkas, dan setiap berkas dipicu dari Dropzone yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah mengamati sesuai Langkah Uji TC (3, 9, 13, 17, 22, 28, 34, 40).
- Temuan untuk QA:
  - TC-GS-IMPORT-89, 90, 93, 95, 96, 582 mengasersi "tanpa toast dan tanpa pesan error" tanpa batas waktu pengamatan; spec mengamati setelah file picker selesai. Berkas biner (xlsx, xls, pdf, 0 byte, Windows-1252) disediakan tim FE/BE dengan isi sesuai Data Uji TC.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).

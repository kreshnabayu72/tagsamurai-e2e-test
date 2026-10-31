---
id: TC-GS-IMPORT-E2E-022-berkas-lolos-penyaringan-csv-utf-8-tanpa-dengan-bom-xlsx-sheet-pertama
title: "Berkas Lolos Penyaringan: CSV UTF-8 Tanpa dan Dengan BOM, XLSX Sheet Pertama, Sheet Lain Diabaikan, dan Berkas Tidak Tersimpan di File Manager Permanen"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-85
  - TC-GS-IMPORT-86
  - TC-GS-IMPORT-87
  - TC-GS-IMPORT-88
  - TC-GS-IMPORT-97
coverage:
  web: automated
---

# Berkas Lolos Penyaringan: CSV UTF-8 Tanpa dan Dengan BOM, XLSX Sheet Pertama, Sheet Lain Diabaikan, dan Berkas Tidak Tersimpan di File Manager Permanen

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; TC-GS-IMPORT-97 berpindah ke File Manager lewat langkah eksplisit.
- Data: Client C tanpa draft Tab Brand (Kontrak Fixture R1; skrip reset disediakan tim FE/BE); daftar berkas File Manager Client C tidak berisi `brand-12.csv`. Berkas fixture (D-07, isi literal): `brand-12.csv` (CSV UTF-8 tanpa BOM; header `Brand Name`; 12 baris D-01), `brand-12-bom.csv` (UTF-8 dengan BOM; isi sama), `brand-12.xlsx` (satu sheet; header `Brand Name`; 12 baris D-01), `brand-two-sheets.xlsx` (sheet 1: header `Brand Name` dan Nikon, Ricoh, Xerox; sheet 2: header `Brand Name` dan 50 baris `Sheet2 Brand 01` sampai `Sheet2 Brand 50`).
- Reset dan cleanup: TC-GS-IMPORT-88 dan 97 membuat draft Brand pada Client C; draft dibuang (langkah reset ditulis eksplisit) antar blok dan di hook `after`, tidak berasumsi seeding berhasil penuh.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker dengan berkas biner (xlsx, BOM); skrip reset draft (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain draft Client C (dibuang hook).

## Test Steps

### TC-GS-IMPORT-85: Berkas CSV UTF-8 tanpa BOM lolos penyaringan

1. Klik `[Upload File]`
2. Pilih berkas `brand-12.csv` di file picker
3. Perhatikan halaman
4. Verifikasi Modal Column Mapping `Column Mapping: Brand` terbuka
5. Verifikasi dropdown Brand Name terpilih otomatis ke kolom `Brand Name`
6. Klik `[Cancel]` (tutup bersih)

### TC-GS-IMPORT-86: Berkas CSV UTF-8 dengan BOM lolos penyaringan

7. Klik `[Upload File]`
8. Pilih berkas `brand-12-bom.csv` di file picker
9. Perhatikan halaman
10. Verifikasi Modal Column Mapping `Column Mapping: Brand` terbuka
11. Verifikasi dropdown Brand Name terpilih otomatis ke kolom `Brand Name`
12. Klik `[Cancel]` (tutup bersih)

### TC-GS-IMPORT-87: Berkas XLSX lolos penyaringan dan dibaca dari sheet pertama

13. Klik `[Upload File]`
14. Pilih berkas `brand-12.xlsx` di file picker
15. Perhatikan halaman
16. Verifikasi Modal Column Mapping `Column Mapping: Brand` terbuka
17. Verifikasi dropdown Brand Name terpilih otomatis ke kolom `Brand Name` dari sheet pertama
18. Klik `[Cancel]` (tutup bersih)

### TC-GS-IMPORT-88: Sheet selain sheet pertama pada XLSX diabaikan

19. Klik `[Upload File]`
20. Pilih berkas `brand-two-sheets.xlsx` di file picker
21. Perhatikan halaman
22. Verifikasi Modal Column Mapping terbuka
23. Klik `[Confirm Mapping]`
24. Perhatikan Staging Table
25. Verifikasi Staging Table menampilkan 3 baris Nikon, Ricoh, Xerox
26. Verifikasi Total Rows 3 (tanpa baris dari sheet 2)
27. Buang draft Brand Client C (reset ke tanpa draft, Kontrak Fixture R1)

### TC-GS-IMPORT-97: Berkas unggahan tidak tersimpan di File Manager permanen

28. Buka Global Settings > File Manager
29. Perhatikan daftar berkas File Manager dan catat jumlah berkas sebagai baseline
30. Buka menu Import dari sidebar
31. Klik `[Upload File]`
32. Pilih berkas `brand-12.csv` di file picker
33. Klik `[Confirm Mapping]`
34. Tunggu aksi selesai (modal tertutup)
35. Buka Global Settings > File Manager
36. Perhatikan daftar berkas File Manager
37. Verifikasi daftar File Manager tidak memuat `brand-12.csv`
38. Verifikasi jumlah berkas File Manager sama dengan baseline langkah 29

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Spec berisi 38 langkah, di atas 35 langkah. Alasan: lima TC (85, 86, 87, 88, 97) satu kelas (penyaringan berkas) dan tiap blok berdiri sendiri dengan pembuangan draft eksplisit sebelum TC berikutnya (S-09).
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 85, 86, 87 (modal ditutup bersih tanpa draft), lalu 88 dan 97 (membuat draft). Draft dari TC-GS-IMPORT-88 dibuang pada langkah 27 sebelum TC-GS-IMPORT-97 yang mensyaratkan Client C tanpa draft (S-09); draft TC-GS-IMPORT-97 dibuang hook `after`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3, 9, 15, 21, 24, 29, 36 (mengamati sesuai Langkah Uji TC), langkah 6, 12, 18 (menutup modal bersih dengan `[Cancel]`; TC tidak menyebut cara menutup modal), langkah 27 (reset), langkah 28 dan 35 (buka File Manager), langkah 30 (buka menu Import), langkah 34 (menunggu modal tertutup sebelum pindah ke File Manager; penanda tidak ada di TC). Langkah 29 mencatat baseline jumlah berkas sebelum Upload (S-12).
- Temuan untuk QA:
  - TC-GS-IMPORT-85, 86, 87 tidak menyebut cara menutup Modal Column Mapping; spec menutup lewat `[Cancel]`.
  - TC-GS-IMPORT-97 Precondition d ("daftar berkas File Manager Client C tidak berisi `brand-12.csv`") disediakan lewat Pre-setup File Manager Client C yang tidak ada di Tabel Pre-setup TC; disediakan tim FE.
  - Penanda "modal tertutup" pada langkah 34 tidak ditulis di TC-GS-IMPORT-97; spec memakai penanda aman agar permintaan Confirm Mapping selesai sebelum pindah ke File Manager.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).

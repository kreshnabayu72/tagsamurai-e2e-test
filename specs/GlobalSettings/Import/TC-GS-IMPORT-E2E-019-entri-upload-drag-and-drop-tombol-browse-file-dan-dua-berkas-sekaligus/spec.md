---
id: TC-GS-IMPORT-E2E-019-entri-upload-drag-and-drop-tombol-browse-file-dan-dua-berkas-sekaligus
title: "Entri Upload: Drag-and-Drop, Tombol Browse File, dan Dua Berkas Sekaligus"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-69
  - TC-GS-IMPORT-70
  - TC-GS-IMPORT-563
coverage:
  web: automated
---

# Entri Upload: Drag-and-Drop, Tombol Browse File, dan Dua Berkas Sekaligus

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C.
- Data: Client C tanpa draft Tab Brand (Kontrak Fixture R1; skrip reset disediakan tim FE/BE). Berkas fixture (D-07, isi literal): `brand-12.csv` (header `Brand Name`; 12 baris D-01) dan `brand-6.csv` (Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp).
- Cleanup: TC-GS-IMPORT-563 membuat draft Brand 12 baris pada Client C; hook `after` membuang draft itu dan tidak berasumsi seeding berhasil penuh.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: simulasi drag-and-drop berkas dan drop multi-berkas ke Dropzone; file picker; skrip reset draft.
- State global: tidak ada yang diubah selain draft Client C (dibuang hook).

## Test Steps

### TC-GS-IMPORT-69: Drag and drop berkas CSV ke Dropzone langsung membuka Modal Column Mapping

1. Seret berkas `brand-12.csv` ke Dropzone
2. Perhatikan halaman
3. Verifikasi Modal Column Mapping `Column Mapping: Brand` terbuka
4. Verifikasi tidak ada toast
5. Klik `[Cancel]` (tutup bersih)

### TC-GS-IMPORT-70: Tombol Browse File di Dropzone membuka file picker

6. Klik `[Browse File]` di Dropzone
7. Perhatikan file picker
8. Verifikasi file picker terbuka
9. Pilih berkas `brand-12.csv` di file picker
10. Perhatikan halaman
11. Verifikasi Modal Column Mapping `Column Mapping: Brand` terbuka
12. Klik `[Cancel]` (tutup bersih)

### TC-GS-IMPORT-563: Menjatuhkan dua berkas sekaligus ke Dropzone hanya memproses berkas pertama

13. Seret `brand-12.csv` dan `brand-6.csv` bersamaan ke Dropzone dengan `brand-12.csv` sebagai berkas pertama
14. Perhatikan Modal Column Mapping
15. Verifikasi Modal Column Mapping terbuka untuk berkas pertama (`brand-12.csv`)
16. Verifikasi berkas kedua diabaikan tanpa toast dan tanpa pesan error
17. Klik `[Confirm Mapping]`
18. Perhatikan Staging Table
19. Verifikasi draft berisi 12 baris (Total Rows 12)
20. Verifikasi Staging Table tanpa baris Nikon

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 69, 70, 563. TC-GS-IMPORT-563 membuat draft sehingga ditaruh terakhir; TC-GS-IMPORT-69 dan 70 menutup modal bersih sehingga Dropzone tetap tampil untuk TC berikutnya.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2, 7, 10, 14, 18 (mengamati sesuai Langkah Uji TC) dan langkah 5 dan 12 (menutup modal bersih dengan `[Cancel]`; TC tidak menyebut cara menutup modal; tidak ada dialog karena mapping tidak diubah).
- Temuan untuk QA:
  - TC-GS-IMPORT-69 dan 70 tidak menyebut cara menutup Modal Column Mapping sesudah asersi; spec menutup lewat `[Cancel]` sebagai langkah penghubung.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).

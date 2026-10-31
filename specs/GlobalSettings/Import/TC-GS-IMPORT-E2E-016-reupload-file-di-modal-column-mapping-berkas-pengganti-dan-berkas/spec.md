---
id: TC-GS-IMPORT-E2E-016-reupload-file-di-modal-column-mapping-berkas-pengganti-dan-berkas
title: "Reupload File di Modal Column Mapping: Berkas Pengganti dan Berkas Tersaring"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-60
  - TC-GS-IMPORT-61
coverage:
  web: automated
---

# Reupload File di Modal Column Mapping: Berkas Pengganti dan Berkas Tersaring

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; spec ini tidak menguji navigasi.
- Data: Client C tanpa draft Tab Brand (Kontrak Fixture R1; skrip reset disediakan tim FE/BE). Spec tidak menjalankan Confirm Mapping sehingga tidak ada draft yang tercipta. Berkas fixture (D-07, isi literal): `brand-12.csv` (header `Brand Name`; 12 baris D-01), `brand-6.csv` (header `Brand Name`; Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp), `notes.txt` (teks biasa).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-IMPORT-60: Reupload File menggantikan berkas, auto-match dihitung ulang, tanpa dialog

1. Klik `[Upload File]`
2. Pilih berkas `brand-12.csv` di file picker
3. Ubah dropdown Brand Name menjadi "No Column"
4. Klik `[Reupload File]`
5. Verifikasi file picker terbuka
6. Pilih berkas `brand-6.csv` di file picker
7. Perhatikan modal
8. Verifikasi berkas pengganti menggantikan berkas lama tanpa dialog konfirmasi
9. Verifikasi dropdown Brand Name kembali ke default auto-match (terpetakan ke kolom `Brand Name`)
10. Klik `[Cancel]`
11. Perhatikan halaman
12. Verifikasi modal tertutup tanpa dialog Unsaved Changes
13. Verifikasi halaman menampilkan Dropzone tanpa draft

### TC-GS-IMPORT-61: Reupload dengan berkas tidak lolos penyaringan tersaring dan mapping lama tetap

14. Klik `[Upload File]`
15. Pilih berkas `brand-12.csv` di file picker
16. Klik `[Reupload File]`
17. Pilih berkas `notes.txt` di file picker
18. Perhatikan modal
19. Verifikasi berkas `notes.txt` tidak diproses dan tidak ada toast
20. Verifikasi Modal Column Mapping tetap menampilkan mapping berkas `brand-12.csv`: dropdown Brand Name terpilih `Brand Name`
21. Klik `[Cancel]` (tutup bersih)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7, 11, 18 (mengamati sesuai Langkah Uji TC) dan langkah 21 (menutup modal bersih dengan `[Cancel]`; tidak ada perubahan mapping setelah auto-match sehingga tidak ada dialog; TC-GS-IMPORT-61 tidak menyebut cara menutup modal).
- Tiap TC membuka modal baru karena TC-GS-IMPORT-60 menutup modal; urutan menjaga bagian bersih (TC-GS-IMPORT-61) sesudah bagian yang mengubah mapping.
- Temuan untuk QA:
  - TC-GS-IMPORT-61 tidak menyebut cara menutup Modal Column Mapping sesudah asersi; spec menutup lewat `[Cancel]`.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).

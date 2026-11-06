---
id: TC-GS-IMPORT-E2E-217-toolbar-menggantikan-dropzone-setelah-draft-terbentuk-dari-upload-pertama
title: "Toolbar Menggantikan Dropzone Setelah Draft Terbentuk dari Upload Pertama"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-973
coverage:
  web: automated
---

# Toolbar Menggantikan Dropzone Setelah Draft Terbentuk dari Upload Pertama

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C.
- Data: Client C tanpa draft Tab Brand (Kontrak Fixture R1; skrip reset disediakan tim FE/BE). Berkas fixture `brand-12.csv` (D-07; header `Brand Name`, 12 baris D-01).
- Cleanup: spec ini membuat draft Brand 12 baris pada Client C; hook `after` membuang draft itu dan tidak berasumsi pembuatan berhasil penuh.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft.
- State global: tidak ada yang diubah selain draft Client C (dibuang hook).

## Test Steps

1. Perhatikan halaman
2. Verifikasi halaman menampilkan Dropzone
3. Verifikasi TableTools Toolbar tidak tampil
4. Klik `[Upload File]` di Dropzone
5. Pilih berkas `brand-12.csv` di file picker
6. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column
7. Perhatikan halaman
8. Verifikasi TableTools Toolbar tampil dengan sisi kiri kosong
9. Verifikasi sisi kanan toolbar memuat Switch `Edit this page`
10. Verifikasi Button `[Download Template]` di toolbar bergaya outline
11. Verifikasi Button `[Upload File]` di toolbar bergaya filled, aksi utama, paling kanan
12. Verifikasi Staging DataTable berisi draft 12 baris
13. Verifikasi Dropzone tidak tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 7 (mengamati sesuai Langkah Uji TC) dan langkah 5 (memilih berkas di file picker).
- Langkah 3 (absence Toolbar) memakai Dropzone langkah 2 sebagai anchor positif; langkah 13 (absence Dropzone) memakai Toolbar dan Staging DataTable langkah 8 sampai 12 sebagai anchor positif.
- Temuan untuk QA:
  - TC-GS-IMPORT-973 tidak menyebut cara menutup atau membersihkan draft sesudah asersi; pembersihan dilakukan hook `after`.

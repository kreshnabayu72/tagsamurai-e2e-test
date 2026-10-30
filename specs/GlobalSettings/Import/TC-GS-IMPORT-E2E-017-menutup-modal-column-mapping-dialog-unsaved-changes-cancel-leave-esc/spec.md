---
id: TC-GS-IMPORT-E2E-017-menutup-modal-column-mapping-dialog-unsaved-changes-cancel-leave-esc
title: "Menutup Modal Column Mapping: Dialog Unsaved Changes (Cancel, Leave, Esc) dan Tutup Bersih (Cancel, Icon Close)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-62
  - TC-GS-IMPORT-63
  - TC-GS-IMPORT-64
  - TC-GS-IMPORT-65
  - TC-GS-IMPORT-66
  - TC-GS-IMPORT-67
coverage:
  web: automated
---

# Menutup Modal Column Mapping: Dialog Unsaved Changes (Cancel, Leave, Esc) dan Tutup Bersih (Cancel, Icon Close)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; perpindahan Sub-Tab ditulis sebagai langkah eksplisit.
- Data: Client C tanpa draft Tab Measurement dan Brand (Kontrak Fixture R1; skrip reset disediakan tim FE/BE). Spec tidak menjalankan Confirm Mapping sehingga tidak ada draft yang tercipta. Berkas fixture (D-07, isi literal): `measurement-6.csv` (D-02; header `Unit Name,Symbol`; Meter/m, Liter/L, Piece/pcs, Gram/g, Centimeter/cm, Dozen/dz), `brand-12.csv` (D-01; header `Brand Name`; 12 baris).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft.
- State global: tidak ada yang diubah.

## Test Steps

### Modal dengan dropdown diubah (dirty): TC-GS-IMPORT-64, 65, 67, 66 pada satu modal Measurement

1. Klik Sub-Tab Measurement
2. Klik `[Upload File]`
3. Pilih berkas `measurement-6.csv` di file picker
4. Ubah dropdown Symbol menjadi "No Column"
5. Klik `[Cancel]`
6. Perhatikan dialog
7. Verifikasi dialog dengan Title "Unsaved Changes" dan Body "You have unsaved changes. Are you sure you want to leave?"
8. Verifikasi dialog memuat tombol `[Cancel]` dan `[Leave]`
9. Klik `[Cancel]` pada dialog Unsaved Changes
10. Perhatikan modal
11. Verifikasi dialog tertutup
12. Verifikasi Modal Column Mapping tetap terbuka
13. Verifikasi dropdown Symbol tetap "No Column"
14. Klik `[Cancel]` pada modal
15. Verifikasi dialog Unsaved Changes tampil
16. Tekan Esc
17. Perhatikan modal
18. Verifikasi dialog Unsaved Changes tertutup
19. Verifikasi Modal Column Mapping tetap terbuka dengan dropdown Symbol "No Column"
20. Klik icon `[✕]`
21. Klik `[Leave]` pada dialog Unsaved Changes
22. Perhatikan halaman
23. Verifikasi Modal Column Mapping tertutup
24. Verifikasi halaman kembali ke state Dropzone tanpa draft
25. Verifikasi tidak ada toast

### TC-GS-IMPORT-62: Cancel tanpa perubahan dropdown langsung menutup modal

26. Klik Sub-Tab Brand
27. Klik `[Upload File]`
28. Pilih berkas `brand-12.csv` di file picker
29. Klik `[Cancel]` tanpa mengubah dropdown
30. Perhatikan halaman
31. Verifikasi dialog Unsaved Changes tidak muncul
32. Verifikasi modal tertutup
33. Verifikasi halaman kembali ke state Dropzone tanpa draft

### TC-GS-IMPORT-63: Icon close tanpa perubahan langsung menutup modal

34. Klik `[Upload File]`
35. Pilih berkas `brand-12.csv` di file picker
36. Klik icon `[✕]`
37. Perhatikan halaman
38. Verifikasi dialog Unsaved Changes tidak muncul
39. Verifikasi modal tertutup
40. Verifikasi halaman kembali ke state Dropzone tanpa draft

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Blok dirty (langkah 1 sampai 25) memakai satu modal dan memuat TC-GS-IMPORT-64 (langkah 5 sampai 8), TC-GS-IMPORT-65 (langkah 9 sampai 13), TC-GS-IMPORT-67 (langkah 14 sampai 19), dan TC-GS-IMPORT-66 (langkah 20 sampai 25).
- Urutan TC dalam spec: 64, 65, 67, 66, 62, 63. Urutan ini menyimpang dari urutan TC sumber supaya satu modal dirty dipakai berurutan (Cancel membuka dialog, Cancel dialog mempertahankan, Esc dialog setara Cancel, lalu Leave menutup) dan penutupan bersih (TC-GS-IMPORT-62 dan 63) berada di akhir karena masing-masing butuh modal baru (prinsip 6). Jumlah buka modal: 3, sama dengan jumlah kejadian menutup modal.
- TC-GS-IMPORT-64, 65, 67, dan 66 menyebut Langkah Uji yang sama (ubah Symbol ke "No Column" lalu tutup); langkah 4 dilakukan sekali karena modal dipakai berurutan; state modal setelah tiap TC dijaga oleh asersi pada langkah 11 sampai 13 dan 18 sampai 19.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 26 (pindah Sub-Tab), langkah 6, 10, 17, 22, 30, 37 (mengamati sesuai Langkah Uji TC). Langkah 15 mengasersi bahwa klik `[Cancel]` pada modal setelah dialog sebelumnya ditutup kembali membuka dialog (dibutuhkan agar TC-GS-IMPORT-67 punya prasyarat dialog terbuka).
- Spec melewati sekitar 35 langkah (40 langkah). Satu topik (menutup Modal Column Mapping) tanpa aksi yang mengubah data; blok dirty dan blok bersih berdiri sendiri; kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-GS-IMPORT-64, 65, 67, dan 66 berbagi Precondition dan Langkah awal yang sama; spec memakai satu modal berurutan dan mencatat urutan di Notes.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).

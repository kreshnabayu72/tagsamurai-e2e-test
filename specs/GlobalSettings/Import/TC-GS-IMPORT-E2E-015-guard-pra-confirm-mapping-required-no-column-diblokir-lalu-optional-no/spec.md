---
id: TC-GS-IMPORT-E2E-015-guard-pra-confirm-mapping-required-no-column-diblokir-lalu-optional-no
title: "Guard Pra-Confirm Mapping: Required No Column Diblokir, Lalu Optional No Column Valid dan Kolom Tak Terpetakan Diabaikan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-56
  - TC-GS-IMPORT-57
  - TC-GS-IMPORT-59
coverage:
  web: automated
---

# Guard Pra-Confirm Mapping: Required No Column Diblokir, Lalu Optional No Column Valid dan Kolom Tak Terpetakan Diabaikan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import untuk Total Control Client C; perpindahan Sub-Tab ditulis sebagai langkah eksplisit.
- Data: Client C tanpa draft Tab Measurement, Division, dan Brand (Kontrak Fixture R1; skrip reset disediakan tim FE/BE). Berkas fixture (D-07, isi literal):
  - `measurement-6.csv` (D-02; header `Unit Name,Symbol`; Meter/m, Liter/L, Piece/pcs, Gram/g, Centimeter/cm, Dozen/dz).
  - `division-6.csv` (D-04; header `Division Name,Code`; Finance & Accounting/FIN, Operations/(Code kosong), IT Support/ITS, Receiving/RCV, Procurement/PRC, Sales/SLS).
  - `brand-extra-col.csv` (header `Brand Name,Catatan`; 3 baris: Nikon/a, Ricoh/b, Xerox/c).
- Cleanup: TC-GS-IMPORT-57 dan 59 membuat draft Division (6 baris) dan Brand (3 baris) pada Client C; hook `after` membuang kedua draft (Discard Draft atau reset) dan tidak berasumsi seeding berhasil penuh.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; pengamatan permintaan jaringan (tidak ada permintaan Confirm Mapping yang terkirim pada TC-GS-IMPORT-56); skrip reset draft.
- State global: tidak ada yang diubah selain draft Client C (dibuang hook).

## Test Steps

### TC-GS-IMPORT-56: Required field yang masih No Column memicu Error Banner pra-Confirm

1. Klik Sub-Tab Measurement
2. Klik `[Upload File]`
3. Pilih berkas `measurement-6.csv` di file picker
4. Ubah dropdown Symbol menjadi "No Column"
5. Perhatikan modal
6. Verifikasi Error Banner tampil berheader "The following columns contain errors and cannot be imported:" dengan daftar `Symbol`
7. Verifikasi tombol `[Confirm Mapping]` tetap Enabled
8. Klik `[Confirm Mapping]` saat Symbol masih "No Column"
9. Perhatikan modal
10. Verifikasi tidak ada permintaan Confirm Mapping yang terkirim
11. Verifikasi modal tetap terbuka
12. Verifikasi Error Banner tetap tampil
13. Klik `[Cancel]`
14. Klik `[Leave]` pada dialog Unsaved Changes
15. Perhatikan halaman
16. Verifikasi tidak ada baris masuk Staging Table
17. Verifikasi halaman menampilkan Dropzone tanpa draft

### TC-GS-IMPORT-57: Field opsional dengan No Column adalah pilihan final yang valid

18. Klik Sub-Tab Division
19. Klik `[Upload File]`
20. Pilih berkas `division-6.csv` di file picker
21. Ubah dropdown Code menjadi "No Column"
22. Perhatikan modal
23. Verifikasi tidak ada Error Banner untuk Code
24. Klik `[Confirm Mapping]`
25. Verifikasi modal tertutup
26. Perhatikan Staging Table
27. Verifikasi Staging Table menampilkan 6 baris berstatus `pending`
28. Verifikasi sel Code tiap baris berisi `—`

### TC-GS-IMPORT-59: Kolom berkas yang tidak dipetakan diabaikan

29. Klik Sub-Tab Brand
30. Klik `[Upload File]`
31. Pilih berkas `brand-extra-col.csv` di file picker
32. Klik `[Confirm Mapping]` tanpa memetakan kolom `Catatan`
33. Verifikasi modal tertutup
34. Perhatikan Staging Table
35. Verifikasi Staging Table menampilkan 3 baris Nikon, Ricoh, Xerox dengan kolom `Brand Name`
36. Verifikasi Staging Table tanpa kolom `Catatan`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Spec berisi 36 langkah, hanya sedikit di atas 35 langkah. Alasan: tiga TC (56, 57, 59) berstruktur sama dalam satu kelas (guard pra-Confirm Mapping) dan memakai Sub-Tab berbeda sehingga tidak saling memengaruhi; satu TC yang gagal tidak membuat TC lain kehilangan makna.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 56 (diblokir, tidak membuat data), lalu 57 dan 59 (membuat draft pada Sub-Tab berbeda sehingga tidak saling memengaruhi); sesuai prinsip validasi diblokir sebelum aksi berhasil.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 18, 29 (pindah Sub-Tab), langkah 5, 9, 15, 22, 26, 34 (mengamati sesuai Langkah Uji TC), langkah 13 dan 14 (tutup modal dengan `[Cancel]` lalu `[Leave]`, sesuai Langkah Uji TC-GS-IMPORT-56).
- Temuan untuk QA:
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13). Berkas fixture literal tanpa suffix `{runId}`; keunikan dijaga lewat reset draft.
  - Post Condition TC-GS-IMPORT-57 dan 59 tidak ada; draft yang tercipta dibuang oleh hook `after`.

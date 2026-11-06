---
id: TC-GS-IMPORT-E2E-065-role-matrix-state-belum-ada-draft-untuk-read-only-dan-import-data-read
title: "Role Matrix: State Belum Ada Draft untuk Read Only dan Import data (Read Only) (Import (0), Upload, Dropzone Disabled, Berkas yang Diseret Tidak Diproses)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-32
  - TC-GS-IMPORT-34
  - TC-GS-IMPORT-594
coverage:
  web: automated
---

# Role Matrix: State Belum Ada Draft untuk Read Only dan Import data (Read Only) (Import (0), Upload, Dropzone Disabled, Berkas yang Diseret Tidak Diproses)

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Akun (Client B), password lewat env:
  - Import data (Read Only) Client B (Gita Savitri) `importRead_automated_qaTeam2@qwertysystem.net`, `Spectra.env.GS_CLIENTB_IMPORTRO_PASSWORD` (TC-GS-IMPORT-32 dan 34; login di hook `before`).
  - Read Only Client B (Mega Puspita) `readOnly_automated_qaTeam2@qwertysystem.net`, `Spectra.env.GS_CLIENTB_RO_PASSWORD` (TC-GS-IMPORT-594; login lewat langkah ganti akun).
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite.
- Data: Client B tanpa draft Tab Brand (Kontrak Fixture R1); berkas `brand-12.csv` (D-01; header `Brand Name`, 12 baris). Kemampuan teknis: simulasi drag-and-drop berkas ke Dropzone.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk akun aktor pertama. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk kedua akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.

## Test Steps

### TC-GS-IMPORT-32: Tooltip izin pada Import dan Upload (Import data (Read Only))

1. Hover `[Import (0)]`
2. Verifikasi `[Import (0)]` Disabled dengan tooltip "You don't have permission to do this."
3. Verifikasi tooltip "No rows are ready to import." tidak tampil
4. Hover `[Upload File]` di Dropzone
5. Verifikasi `[Upload File]` Disabled dengan tooltip "You don't have permission to do this."
6. Hover area drag-and-drop Dropzone
7. Verifikasi Dropzone Disabled dengan tooltip "You don't have permission to do this."
8. Hover `[Download Template]` di Dropzone
9. Verifikasi `[Download Template]` Enabled tanpa tooltip izin

### TC-GS-IMPORT-34: Dropzone Disabled dan berkas diseret tidak diproses (Import data (Read Only))

10. Hover Dropzone
11. Verifikasi Dropzone tampil Disabled dengan tooltip "You don't have permission to do this."
12. Seret berkas `brand-12.csv` ke Dropzone
13. Verifikasi Modal Column Mapping tidak terbuka
14. Verifikasi halaman tetap menampilkan Dropzone tanpa draft

### TC-GS-IMPORT-594: Dropzone Disabled dan berkas diseret tidak diproses (Read Only)

15. Ganti akun: login sebagai Read Only Client B, buka Import > Brand
16. Hover Dropzone
17. Verifikasi Dropzone tampil Disabled dengan tooltip "You don't have permission to do this."
18. Seret berkas `brand-12.csv` ke Dropzone
19. Verifikasi Modal Column Mapping tidak terbuka
20. Verifikasi halaman tetap menampilkan Dropzone tanpa draft

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Spec Role Matrix (bagian 3a) untuk dua role pada state belum ada draft.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 15 (ganti akun).
- Langkah 3 (absence tooltip) memakai tooltip izin langkah 2 sebagai anchor positif pada elemen yang sama; langkah 13 memakai Dropzone Disabled langkah 11 atau 17 sebagai anchor.
- Temuan untuk QA:
  - TC-GS-IMPORT-32 Expected a menggabungkan Disabled, tooltip izin, dan tidak adanya tooltip "No rows are ready to import." dalam satu butir; spec memecahnya per klausa.
  - Post Condition "Tidak ada draft Brand pada Client B" pada TC-GS-IMPORT-34 dan 594 setara dengan Expected b.

---
id: TC-GS-IMPORT-E2E-194-tombol-changelog-di-header-icon-only-dan-empty-state-modal-changelog
title: "Tombol Changelog di header (icon-only) dan empty state Modal Changelog tanpa entri"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-491
  - TC-GS-IMPORT-499
coverage:
  web: automated
---

# Tombol Changelog di header (icon-only) dan empty state Modal Changelog tanpa entri

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena state global dibagi antar spec (lihat `suite.md`).
- Akun aktor pertama (login di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Akun kedua (ganti akun eksplisit di langkah): Total Control Client B (Bayu Santoso) `totalControl_automated_qaTeam2@qwertysystem.net`, password `Spectra.env.GS_CLIENTB_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Layar awal: hook `beforeEach` membuka Import > Brand Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor, termasuk Total Control Client B (nilai awal dicatat dan dipulihkan hook suite `after`), lihat `suite.md`.
- Pre-setup: Client B tanpa entri Changelog Import (belum ada commit import apa pun; Client B tanpa data master dan tanpa draft, Kontrak Fixture R1). Hook `before` mereset entri Changelog Import Client B ke kosong sebelum spec. Langkah spec tidak membuat, mengubah, atau menghapus data.
- Kemampuan teknis (disediakan tim FE/BE): reset entri Changelog Import Client B ke kosong sebelum spec.
- State global: tidak ada yang diubah selain flag Guided Tooltip.

## Test Steps

### Tombol Changelog di header (TC-GS-IMPORT-491)

1. Verifikasi `[Changelog]` berbentuk icon-only paling kanan baris header
2. Verifikasi tidak ada icon Changelog di TableTools Toolbar
3. Hover icon `[Changelog]`
4. Verifikasi tooltip "Changelog"

### Empty state Modal Changelog (TC-GS-IMPORT-499)

5. Ganti akun: logout dari Total Control Client A, lalu login sebagai Total Control Client B (Bayu Santoso)
6. Buka Import > Brand
7. Klik `[Changelog]`
8. Verifikasi Modal `Changelog: Import` menampilkan ilustrasi empty state
9. Verifikasi Title "No changelog yet"
10. Verifikasi Description "Activities and changes will appear here."

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 5 dan 6 adalah ganti akun eksplisit dan pembukaan layar untuk akun kedua (hook `beforeEach` membuka layar hanya untuk akun awal); keduanya langkah penghubung (S-03, S-07).
- Kedua TC berupa screening tanpa data; bagian setelah ganti akun tetap bermakna walau bagian awal gagal.
- Temuan untuk QA:
  - TC-GS-IMPORT-499 Pre-setup menyebut Client B "tanpa commit import apa pun" tanpa mekanisme menjamin ketiadaan entri bila run sebelumnya pernah commit di Client B; reset entri Changelog Import Client B dikerjakan hook `before` (kemampuan disediakan tim FE/BE, tertulis di Prerequisites).
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.

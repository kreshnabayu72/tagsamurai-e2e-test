---
id: TC-GS-IMPORT-E2E-187-confirm-mapping-berkas-brand-campuran-menghasilkan-5-pending-3-error-2
title: "Confirm Mapping berkas Brand campuran menghasilkan 5 pending, 3 error, 2 duplicate beserta kartu, callout, footer"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-458
coverage:
  web: automated
---

# Confirm Mapping berkas Brand campuran menghasilkan 5 pending, 3 error, 2 duplicate beserta kartu, callout, footer

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena state global dibagi antar spec (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client F (Hendra Wijaya) `totalControl_automated_qaTeam6@qwertysystem.net`, password `Spectra.env.GS_CLIENTF_TC_PASSWORD` (TC tidak menyebut password per akun, lihat Temuan untuk QA). Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Import > Brand Client F.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Pre-setup: Client F bersih tanpa draft (Kontrak Fixture R1; reset oleh hook `beforeEach` suite, mekanisme skrip reset disediakan tim FE/BE); Brand `Samsung` ada di sistem Client F (Pre-setup Client F, data master seperti Client A, R4).
- Data Dinamis: berkas `brand-mixed.csv` (Data Uji TC-GS-IMPORT-458; fixture uji): header `Brand Name`; 10 baris berurutan: Row 1 `Nexus`, Row 2 `Orion`, Row 3 `Vertex`, Row 4 `Helios`, Row 5 `Samsung`, Row 6 `Pioneer`, Row 7 nama 121 karakter (huruf `A` diulang 121 kali), Row 8 `Rocket 🚀`, Row 9 `Star ⭐`, Row 10 `Pioneer`. Draft D-10 yang tercipta dibuat lewat UI di spec ini. Nilai literal dipakai karena asersi bergantung pada urutan dan nama baris, Client F khusus draft campuran, dan draft dibuang di hook `after`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): draft Brand Client F dibuang lewat skrip reset (D-10 tidak dibawa ke spec lain).
- Kemampuan teknis: pemilihan berkas pada dialog unggah dan pengamatan toast.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### TC-GS-IMPORT-458: Confirm Mapping berkas Brand campuran

1. Klik `[Upload File]` dan pilih berkas `brand-mixed.csv`
2. Klik `[Confirm Mapping]`
3. Verifikasi modal Column Mapping tertutup
4. Verifikasi muncul toast sukses: "Success, row has been added."
5. Verifikasi Staging Table menampilkan 10 baris
6. Verifikasi Row # 1, 2, 3, 4, dan 10 berstatus `pending`
7. Verifikasi Row # 5 dan 6 berstatus `duplicate`
8. Verifikasi Row # 7, 8, dan 9 berstatus `error`
9. Verifikasi Staging Metric Cards menampilkan Total Rows 10, Ready to Import 5, Errors 3, Duplicates 2
10. Verifikasi Error Summary Callout memuat baris pesan `Brand Name: Max. 120 characters` dengan badge "1 row"
11. Verifikasi Error Summary Callout memuat baris pesan `Brand name contains invalid characters` dengan badge "2 rows"
12. Verifikasi footer menampilkan `[Import (5)]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Spec satu TC; Data Dinamis D-10 dibuat lewat UI di langkah 1-2 dan dipakai spec 188 sampai 190 sebagai draft seed lewat skrip (spec itu tidak bergantung pada hasil spec ini).
- Temuan untuk QA:
  - TC-GS-IMPORT-458 Post Condition ("Draft Brand pada Client F berisi 10 baris campuran") tidak punya langkah observasi sendiri; tidak diasersi terpisah (S-01).
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.

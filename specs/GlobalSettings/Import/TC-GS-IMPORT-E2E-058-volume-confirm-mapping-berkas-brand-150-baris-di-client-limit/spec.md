---
id: TC-GS-IMPORT-E2E-058-volume-confirm-mapping-berkas-brand-150-baris-di-client-limit
title: "Volume: Confirm Mapping Berkas Brand 150 Baris di Client Limit Menghasilkan 120 Pending dan 30 Error"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-758
coverage:
  web: automated
---

# Volume: Confirm Mapping Berkas Brand 150 Baris di Client Limit Menghasilkan 120 Pending dan 30 Error

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Akun: Total Control Client Limit (Bima Saputra) `totalControl_automated_qaTeam7@qwertysystem.net`, `Spectra.env.GS_CLIENTLIMIT_TC_PASSWORD`; login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data: Client Limit tanpa draft Tab Brand (Kontrak Fixture R1) dan berisi 999 Brand seed `Seed Brand 0001` sampai `Seed Brand 0999` (Pre-setup, Kontrak Fixture R7; Master Data Count Limit 1000). Berkas `brand-150-mixed.csv` (D-61): header `Brand Name`; 150 baris: Row 1 sampai 120 `Brand 001` sampai `Brand 120`; Row 121 sampai 145 (25 baris) nama unik 121 karakter berawalan `Overlong 01` sampai `Overlong 25` yang dilengkapi huruf `A` sampai 121 karakter; Row 146 sampai 150 (5 baris) `Emoji 1 🚀` sampai `Emoji 5 🚀`.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Brand Client Limit (150 baris, D-61) direset ke tanpa draft sesudah spec (R1); Sub-Tab Brand Client Limit dibagi dengan D-32 sehingga dibuat ulang per TC pemakai.

## Test Steps

1. Klik [Upload File]
2. Pilih berkas `brand-150-mixed.csv`
3. Klik [Confirm Mapping]
4. Verifikasi modal tertutup
5. Verifikasi toast sukses: "Success, row has been added."
6. Verifikasi Staging Metric Cards: Total Rows 150, Ready to Import 120, Errors 30, Duplicates 0 (Disabled)
7. Verifikasi Pagination "Showing 1 - 10 of 150 items"
8. Verifikasi Error Summary Callout memuat `Brand Name: Max. 120 characters` dengan badge "25 rows"
9. Verifikasi Error Summary Callout memuat `Brand name contains invalid characters` dengan badge "5 rows"
10. Verifikasi footer menampilkan `[Import (120)]`
11. Reset Client Limit ke tanpa draft Tab Brand lewat skrip fixture

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: volume data khusus (kelas e, prinsip 13e; 150 baris dan seed 999 record per katalog).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11 (reset draft).
- Temuan untuk QA:
  - Expected a-e TC-GS-IMPORT-758 ditulis tanpa awalan "Setelah langkah N" pada b sampai e; spec memetakannya ke pembacaan sesudah modal tertutup.

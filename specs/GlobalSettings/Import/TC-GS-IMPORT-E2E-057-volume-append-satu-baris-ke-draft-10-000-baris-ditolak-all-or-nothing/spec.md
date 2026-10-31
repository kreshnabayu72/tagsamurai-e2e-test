---
id: TC-GS-IMPORT-E2E-057-volume-append-satu-baris-ke-draft-10-000-baris-ditolak-all-or-nothing
title: "Volume: Append Satu Baris ke Draft 10.000 Baris Ditolak All-or-Nothing"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-813
coverage:
  web: automated
---

# Volume: Append Satu Baris ke Draft 10.000 Baris Ditolak All-or-Nothing

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Akun: Total Control Client B (Bayu Santoso) `totalControl_automated_qaTeam2@qwertysystem.net`, `Spectra.env.GS_CLIENTB_TC_PASSWORD`; login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client B): D-35 draft Brand 10000 baris `pending` (`Brand 00001` sampai `Brand 10000`, `brand-10000.csv`), disiapkan oleh langkah 1 lewat skrip fixture; D-76 varian 1 (`created_at` dimundurkan 25 jam, hanya seed backdate) sehingga Unsaved Banner tampil. Berkas `brand-append-1.csv`: header `Brand Name`; satu baris `Brand Tambahan 1`.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Brand Client B direset ke tanpa draft (R1) di akhir spec.

## Test Steps

1. Reset Client B ke tanpa draft; seed draft D-35 (Brand 10000 baris `pending` dari `brand-10000.csv`) dengan D-76 varian 1 (`created_at` dimundurkan 25 jam) lewat skrip fixture
2. Muat ulang halaman Import > Brand
3. Klik [Upload File]
4. Pilih berkas `brand-append-1.csv` di file picker
5. Verifikasi dialog Title "Append to Draft" dengan Body "The organization already has an active draft for this import type. Do you want to append new records to it?" dan tombol `[Cancel]` dan `[Append Records]`
6. Klik [Append Records] pada dialog Append to Draft
7. Klik [Confirm Mapping] tanpa mengubah dropdown File Column dari hasil auto-match
8. Verifikasi tidak ada toast setelah langkah 7
9. Verifikasi seluruh berkas ditolak (all-or-nothing)
10. Verifikasi Modal Column Mapping tetap terbuka
11. Verifikasi Error Banner hanya memuat baris pesan "Exceeds maximum 10.000 rows per session"
12. Verifikasi Error Banner tanpa header jumlah baris yang gagal diimpor
13. Verifikasi Error Banner tanpa nomor baris
14. Klik [Cancel]
15. Verifikasi modal tertutup tanpa dialog Unsaved Changes
16. Verifikasi Unsaved Banner tetap tampil
17. Verifikasi Staging Metric Cards: Total Rows 10000 (Active), Ready to Import 10000, Errors 0 (Disabled), Duplicates 0 (Disabled)
18. Verifikasi Pagination "Showing 1 - 10 of 10000 items"
19. Reset Client B ke tanpa draft Tab Brand lewat skrip fixture

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: volume data khusus (kelas e, prinsip 13e; draft 10000 baris).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (reset dan seed draft D-35 dengan D-76 varian 1), langkah 2 (muat ulang halaman), langkah 14 (menutup modal), langkah 19 (reset draft).
- Langkah 8 (absence toast) ditulis tepat sesudah `[Confirm Mapping]` langkah 7 dan mendahului `Verifikasi` artefak; anchor positifnya adalah Error Banner langkah 11 dan modal yang tetap terbuka langkah 10.
- Temuan untuk QA:
  - Tidak ada temuan khusus pada TC-GS-IMPORT-813; Post Condition ("Draft Brand Client B tetap 10000 baris pending") setara dengan Expected f.

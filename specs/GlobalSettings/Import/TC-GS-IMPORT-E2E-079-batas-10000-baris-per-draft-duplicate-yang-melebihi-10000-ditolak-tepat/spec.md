---
id: TC-GS-IMPORT-E2E-079-batas-10000-baris-per-draft-duplicate-yang-melebihi-10000-ditolak-tepat
title: "Batas 10000 Baris per Draft: Duplicate yang Melebihi 10000 Ditolak, Tepat 10000 Diterima"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-233
  - TC-GS-IMPORT-670
coverage:
  web: automated
---

# Batas 10000 Baris per Draft: Duplicate yang Melebihi 10000 Ditolak, Tepat 10000 Diterima

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Akun: Total Control Client B (Bayu Santoso) `totalControl_automated_qaTeam2@qwertysystem.net`, `Spectra.env.GS_CLIENTB_TC_PASSWORD`; login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client B, disiapkan oleh langkah pembuka tiap blok lewat skrip fixture: D-35 oleh langkah 1, D-37 oleh langkah 21): D-35 draft Brand 10000 baris `pending` (`Brand 00001` sampai `Brand 10000`, `brand-10000.csv`) untuk TC-GS-IMPORT-233; D-37 draft Brand 9999 baris `pending` (`Brand 00001` sampai `Brand 09999`, `brand-9999.csv`) untuk TC-GS-IMPORT-670. Nama baris salinan TC-GS-IMPORT-233: `Brand Salinan {runId}-079`.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Client B direset ke tanpa draft (R1) di akhir tiap blok (langkah 21 dan 30).

## Test Steps

### TC-GS-IMPORT-233: Duplicate yang membuat total melebihi 10000

1. Reset Client B ke tanpa draft Tab Brand; siapkan draft D-35 (10000 baris `pending`) lewat skrip fixture; muat ulang halaman Import > Brand
2. Klik `⋯` pada baris #1
3. Pilih Duplicate
4. Ubah Brand Name baris salinan menjadi `Brand Salinan {runId}-079`
5. Klik `[Save]`
6. Verifikasi `[Save]` ditolak tanpa toast sukses
7. Verifikasi draft tidak bertambah
8. Verifikasi Error Summary Callout tampil walau draft tidak memiliki baris `error`
9. Verifikasi Error Summary Callout memuat satu baris pesan "Exceeds maximum 10.000 rows per session"
10. Verifikasi pesan tanpa badge jumlah baris, tanpa nomor baris, tanpa `[View Data]`, dan tanpa `[Delete All Rows]`
11. Verifikasi footer tetap `[Cancel]` dan `[Save]`
12. Verifikasi baris salinan tetap tampil sebagai input (sesi tetap terbuka)
13. Verifikasi kartu Total Rows tetap menampilkan 10000
14. Klik `[Cancel]`
15. Verifikasi dialog Title "Discard Changes" dengan Body "Your changes will not be saved." dan tombol `[Keep Editing]` dan `[Discard]`
16. Klik `[Discard]` pada dialog
17. Verifikasi Error Summary Callout tidak tampil
18. Verifikasi baris pesan "Exceeds maximum 10.000 rows per session" hilang
19. Verifikasi footer `[Import (10000)]` tampil kembali
20. Verifikasi kartu Total Rows menampilkan 10000
21. Reset Client B ke tanpa draft Tab Brand; siapkan draft D-37 (9999 baris `pending`) lewat skrip fixture; muat ulang halaman Import > Brand

### TC-GS-IMPORT-670: Duplicate yang membuat total tepat 10000

22. Klik `⋯` pada baris #1
23. Pilih Duplicate
24. Klik `[Save]`
25. Verifikasi toast sukses "Success, row has been added."
26. Verifikasi Error Summary Callout tidak memuat pesan "Exceeds maximum 10.000 rows per session"
27. Verifikasi footer `[Import (9999)]` tampil kembali tanpa `[Cancel]` dan `[Save]` (sesi tertutup)
28. Verifikasi baris #1 `Brand 00001` berstatus `duplicate`
29. Verifikasi baris salinan #2 `Brand 00001` berstatus `pending`
30. Reset Client B ke tanpa draft Tab Brand

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: volume data khusus (kelas e, prinsip 13e; draft 10000 dan 9999 baris).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (reset dan seed D-35), langkah 14 dan 16 (menutup sesi Duplicate lewat `[Cancel]` dan `[Discard]` mengikuti TC), langkah 21 (reset, seed D-37, muat ulang halaman) dan langkah 30 (reset draft). Skrip fixture sinkron (`suite.md`); muat ulang halaman sesudah reset (langkah 1 dan 21) membuat langkah berikutnya bekerja pada draft baru.
- Langkah 26 (absence pesan) memakai toast sukses langkah 25 sebagai anchor; langkah 17 dan 18 memakai footer `[Import (10000)]` langkah 19 sebagai anchor.
- Temuan untuk QA:
  - TC-GS-IMPORT-233 dan 670 tidak merujuk TC dependensi untuk pembuatan draft 10000 dan 9999 baris selain Data Dinamis; draft disiapkan lewat skrip fixture.
  - TC-GS-IMPORT-233 Expected a-g memetakan pembacaan setelah langkah 5 dan 9; spec mengikuti urutan state.

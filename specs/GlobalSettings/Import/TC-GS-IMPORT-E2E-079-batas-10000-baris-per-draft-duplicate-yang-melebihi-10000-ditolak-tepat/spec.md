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
- Data Dinamis (Client B, disiapkan lewat skrip fixture sebelum tiap TC): D-35 draft Brand 10000 baris `pending` (`Brand 00001` sampai `Brand 10000`, `brand-10000.csv`) untuk TC-GS-IMPORT-233; D-37 draft Brand 9999 baris `pending` (`Brand 00001` sampai `Brand 09999`, `brand-9999.csv`) untuk TC-GS-IMPORT-670. Nama baris salinan TC-GS-IMPORT-233: `Brand Salinan {runId}-079`.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Client B direset ke tanpa draft (R1) di akhir tiap blok.

## Test Steps

### TC-GS-IMPORT-233: Duplicate yang membuat total melebihi 10000

1. Klik `⋯` pada baris #1
2. Pilih Duplicate
3. Ubah Brand Name baris salinan menjadi `Brand Salinan {runId}-079`
4. Klik `[Save]`
5. Verifikasi `[Save]` ditolak tanpa toast sukses
6. Verifikasi draft tidak bertambah
7. Verifikasi Error Summary Callout tampil walau draft tidak memiliki baris `error`
8. Verifikasi Error Summary Callout memuat satu baris pesan "Exceeds maximum 10.000 rows per session"
9. Verifikasi pesan tanpa badge jumlah baris, tanpa nomor baris, tanpa `[View Data]`, dan tanpa `[Delete All Rows]`
10. Verifikasi footer tetap `[Cancel]` dan `[Save]`
11. Verifikasi baris salinan tetap tampil sebagai input (sesi tetap terbuka)
12. Verifikasi kartu Total Rows tetap menampilkan 10000
13. Klik `[Cancel]`
14. Verifikasi dialog Title "Discard Changes" dengan Body "Your changes will not be saved." dan tombol `[Keep Editing]` dan `[Discard]`
15. Klik `[Discard]` pada dialog
16. Verifikasi Error Summary Callout tidak tampil
17. Verifikasi baris pesan "Exceeds maximum 10.000 rows per session" hilang
18. Verifikasi footer `[Import (10000)]` tampil kembali
19. Verifikasi kartu Total Rows menampilkan 10000
20. Reset Client B ke tanpa draft Tab Brand; siapkan draft D-37

### TC-GS-IMPORT-670: Duplicate yang membuat total tepat 10000

21. Klik `⋯` pada baris #1
22. Pilih Duplicate
23. Klik `[Save]`
24. Verifikasi toast sukses "Success, row has been added."
25. Verifikasi Error Summary Callout tidak memuat pesan "Exceeds maximum 10.000 rows per session"
26. Verifikasi footer `[Import (9999)]` tampil kembali tanpa `[Cancel]` dan `[Save]` (sesi tertutup)
27. Verifikasi baris #1 `Brand 00001` berstatus `duplicate`
28. Verifikasi baris salinan #2 `Brand 00001` berstatus `pending`
29. Reset Client B ke tanpa draft Tab Brand

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: volume data khusus (kelas e, prinsip 13e; draft 10000 dan 9999 baris).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 13 dan 15 (menutup sesi Duplicate lewat `[Cancel]` dan `[Discard]` mengikuti TC), langkah 20 dan 29 (reset draft).
- Langkah 25 (absence pesan) memakai toast sukses langkah 24 sebagai anchor; langkah 16 dan 17 memakai footer `[Import (10000)]` langkah 18 sebagai anchor.
- Temuan untuk QA:
  - TC-GS-IMPORT-233 dan 670 tidak merujuk TC dependensi untuk pembuatan draft 10000 dan 9999 baris selain Data Dinamis; draft disiapkan lewat skrip fixture.
  - TC-GS-IMPORT-233 Expected a-g memetakan pembacaan setelah langkah 5 dan 9; spec mengikuti urutan state.

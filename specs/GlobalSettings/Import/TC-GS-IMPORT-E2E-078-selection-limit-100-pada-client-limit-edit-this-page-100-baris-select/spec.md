---
id: TC-GS-IMPORT-E2E-078-selection-limit-100-pada-client-limit-edit-this-page-100-baris-select
title: "Selection Limit 100 pada Client Limit: Edit this page 100 Baris, Select All Di-cap, Checkbox Tambahan Disabled, dan Bulk Delete Hanya 100 Baris"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-194
  - TC-GS-IMPORT-270
  - TC-GS-IMPORT-271
  - TC-GS-IMPORT-272
coverage:
  web: automated
---

# Selection Limit 100 pada Client Limit: Edit this page 100 Baris, Select All Di-cap, Checkbox Tambahan Disabled, dan Bulk Delete Hanya 100 Baris

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Akun: Total Control Client Limit (Bima Saputra) `totalControl_automated_qaTeam7@qwertysystem.net`, `Spectra.env.GS_CLIENTLIMIT_TC_PASSWORD`; login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client Limit): D-32 draft Brand 150 baris `pending` dari `brand-150-limit.csv` (`Brand 001` sampai `Brand 150`), disiapkan oleh langkah 1 dan dibuat ulang oleh langkah 9, 14, dan 24 karena Sub-Tab Brand Client Limit dibagi dengan D-61. Selection Limit Client Limit bernilai 100 (Pre-setup, NC-01).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Client Limit direset ke tanpa draft (R1) di akhir spec.

## Test Steps

### TC-GS-IMPORT-194: Edit this page pada 100 baris

1. Reset Client Limit ke tanpa draft Tab Brand; seed draft D-32 lewat skrip fixture; muat ulang halaman Import > Brand
2. Set Rows per page menjadi 100
3. Aktifkan Switch `Edit this page`
4. Hitung baris tabel yang berupa input aktif
5. Verifikasi tepat 100 baris (`Row #` 1 sampai 100) menjadi input aktif
6. Verifikasi footer `[Import (150)]` tidak tampil
7. Verifikasi footer menampilkan `[Cancel]` dan `[Save]`
8. Klik `[Cancel]` pada footer

### TC-GS-IMPORT-270: Select All melebihi Selection Limit

9. Buat ulang draft D-32 dan muat ulang halaman Import > Brand
10. Klik checkbox baris #1
11. Klik `[Select All (150 records)]`
12. Verifikasi Bulk Action Bar tetap tampil dengan counter "100 Rows selected"
13. Verifikasi toast error persisten "Error, only the first 100 of 150 rows were selected. Narrow your filter to include the rest."

### TC-GS-IMPORT-271: Seleksi satu-satu melewati Selection Limit

14. Buat ulang draft D-32 dan muat ulang halaman Import > Brand
15. Set Rows per page menjadi 100
16. Untuk n = 1 sampai 100 (100 klik berurutan): centang checkbox baris #n
17. Klik tombol halaman 2 pada paginator
18. Hover checkbox baris #101
19. Verifikasi checkbox baris #101 tampil Disabled
20. Verifikasi hover menampilkan tooltip "You've reached the maximum selection of 100 rows."
21. Verifikasi Bulk Action Bar tetap menampilkan "100 Rows selected"
22. Klik `[Bulk Action ▾]`
23. Verifikasi overlay `[Bulk Action ▾]` berisi item `[Delete]`

### TC-GS-IMPORT-272: Bulk Delete setelah Select All ter-cap

24. Buat ulang draft D-32 dan muat ulang halaman Import > Brand
25. Klik checkbox baris #1
26. Klik `[Select All (150 records)]`
27. Klik `[Bulk Action ▾]`
28. Klik `[Delete]` pada overlay
29. Gulir daftar baris pada dialog sampai bullet terakhir
30. Verifikasi dialog "Delete Rows" menampilkan item list `Row #1` sampai `Row #100` secara lengkap dalam container scrollable
31. Verifikasi bullet terakhir `Row #100`
32. Klik `[Delete]` pada dialog Delete Rows
33. Verifikasi toast sukses "Success, row has been deleted."
34. Verifikasi draft tersisa 50 baris: footer `[Import (50)]`
35. Reset Client Limit ke tanpa draft Tab Brand

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: volume data khusus (kelas e, prinsip 13e; draft 150 baris dan Selection Limit 100).
- Spec memuat 35 langkah nominal (langkah 16 diulang 100 kali; ekspansi sekitar 134 langkah). Alasan: semua blok satu kelas harness (Selection Limit pada Client Limit dengan draft 150 baris) dan tiap blok berdiri sendiri dengan draft yang dibuat ulang; parameter ulang n = 1 sampai 100 dinyatakan di langkah 16 dan 100 klik checkbox mengikuti TC-GS-IMPORT-271. TC-GS-IMPORT-272 menghapus 100 baris sehingga di akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (reset dan seed fixture sebelum TC pertama), langkah 2 sampai 4, 10, 15 sampai 18, 22, 25 sampai 29 (aksi menuju keadaan yang diasersi), langkah 8 dan 35 (menutup sesi edit dan reset), langkah 9, 14, 24 (membuat ulang draft D-32).
- Temuan untuk QA:
  - TC-GS-IMPORT-194 tidak menyebut cara menutup sesi edit sesudah Expected; spec menambahkan `[Cancel]` (tanpa perubahan, tanpa dialog) sebagai langkah penghubung.
  - TC-GS-IMPORT-271 mensyaratkan 100 klik checkbox satu per satu; spec menuliskannya sebagai satu langkah berulang.

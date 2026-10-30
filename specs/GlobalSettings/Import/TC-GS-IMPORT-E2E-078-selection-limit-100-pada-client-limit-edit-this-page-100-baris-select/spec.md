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
- Data Dinamis (Client Limit): D-32 draft Brand 150 baris `pending` dari `brand-150-limit.csv` (`Brand 001` sampai `Brand 150`), dibuat ulang lewat skrip fixture sebelum tiap TC karena Sub-Tab Brand Client Limit dibagi dengan D-61. Selection Limit Client Limit bernilai 100 (Pre-setup, NC-01).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Client Limit direset ke tanpa draft (R1) di akhir spec.

## Test Steps

### TC-GS-IMPORT-194: Edit this page pada 100 baris

1. Set Rows per page menjadi 100
2. Aktifkan Switch `Edit this page`
3. Hitung baris tabel yang berupa input aktif
4. Verifikasi tepat 100 baris (`Row #` 1 sampai 100) menjadi input aktif
5. Verifikasi footer `[Import (150)]` tidak tampil
6. Verifikasi footer menampilkan `[Cancel]` dan `[Save]`
7. Klik `[Cancel]` pada footer

### TC-GS-IMPORT-270: Select All melebihi Selection Limit

8. Buat ulang draft D-32 dan muat ulang halaman Import > Brand
9. Klik checkbox baris #1
10. Klik `[Select All (150 records)]`
11. Verifikasi Bulk Action Bar tetap tampil dengan counter "100 Rows selected"
12. Verifikasi toast error persisten "Error, only the first 100 of 150 rows were selected. Narrow your filter to include the rest."

### TC-GS-IMPORT-271: Seleksi satu-satu melewati Selection Limit

13. Buat ulang draft D-32 dan muat ulang halaman Import > Brand
14. Set Rows per page menjadi 100
15. Untuk n = 1 sampai 100 (100 klik berurutan): centang checkbox baris #n
16. Klik tombol halaman 2 pada paginator
17. Hover checkbox baris #101
18. Verifikasi checkbox baris #101 tampil Disabled
19. Verifikasi hover menampilkan tooltip "You've reached the maximum selection of 100 rows."
20. Verifikasi Bulk Action Bar tetap menampilkan "100 Rows selected"
21. Klik `[Bulk Action ▾]`
22. Verifikasi overlay `[Bulk Action ▾]` berisi item `[Delete]`

### TC-GS-IMPORT-272: Bulk Delete setelah Select All ter-cap

23. Buat ulang draft D-32 dan muat ulang halaman Import > Brand
24. Klik checkbox baris #1
25. Klik `[Select All (150 records)]`
26. Klik `[Bulk Action ▾]`
27. Klik `[Delete]` pada overlay
28. Gulir daftar baris pada dialog sampai bullet terakhir
29. Verifikasi dialog "Delete Rows" menampilkan item list `Row #1` sampai `Row #100` secara lengkap dalam container scrollable
30. Verifikasi bullet terakhir `Row #100`
31. Klik `[Delete]` pada dialog Delete Rows
32. Verifikasi toast sukses "Success, row has been deleted."
33. Verifikasi draft tersisa 50 baris: footer `[Import (50)]`
34. Reset Client Limit ke tanpa draft Tab Brand

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: volume data khusus (kelas e, prinsip 13e; draft 150 baris dan Selection Limit 100).
- Spec memuat 34 langkah nominal (langkah 15 diulang 100 kali; ekspansi sekitar 133 langkah). Alasan: semua blok satu kelas harness (Selection Limit pada Client Limit dengan draft 150 baris) dan tiap blok berdiri sendiri dengan draft yang dibuat ulang; parameter ulang n = 1 sampai 100 dinyatakan di langkah 15 dan 100 klik checkbox mengikuti TC-GS-IMPORT-271. TC-GS-IMPORT-272 menghapus 100 baris sehingga di akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 3, 9, 14 sampai 17, 21, 24 sampai 28 (aksi menuju keadaan yang diasersi), langkah 7 dan 34 (menutup sesi edit dan reset), langkah 8, 13, 23 (membuat ulang draft D-32).
- Temuan untuk QA:
  - TC-GS-IMPORT-194 tidak menyebut cara menutup sesi edit sesudah Expected; spec menambahkan `[Cancel]` (tanpa perubahan, tanpa dialog) sebagai langkah penghubung.
  - TC-GS-IMPORT-271 mensyaratkan 100 klik checkbox satu per satu; spec menuliskannya sebagai satu langkah berulang.

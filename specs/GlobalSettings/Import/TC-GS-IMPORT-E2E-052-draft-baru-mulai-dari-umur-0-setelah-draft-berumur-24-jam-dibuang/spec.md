---
id: TC-GS-IMPORT-E2E-052-draft-baru-mulai-dari-umur-0-setelah-draft-berumur-24-jam-dibuang
title: "Draft Baru Mulai dari Umur 0 Setelah Draft Berumur 24 Jam Dibuang (Select All dan Bulk Delete, Discard, Delete All Rows)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-882
  - TC-GS-IMPORT-883
  - TC-GS-IMPORT-885
coverage:
  web: automated
---

# Draft Baru Mulai dari Umur 0 Setelah Draft Berumur 24 Jam Dibuang (Select All dan Bulk Delete, Discard, Delete All Rows)

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Akun: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, `Spectra.env.GS_CLIENTC_TC_PASSWORD`; login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client C, dibuat ulang lewat skrip fixture sebelum tiap TC):
  - D-77 draft Brand 6 baris `pending` dari `brand-6.csv` (Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp) dengan hook umur draft D-76 varian 1 (`created_at` dimundurkan 25 jam; hanya seed backdate) untuk TC-GS-IMPORT-882 dan 883.
  - D-78 draft Brand 2 baris `error` dari `brand-2-error.csv` (Row 1 Brand Name 121 karakter huruf `A`, Row 2 121 karakter huruf `B`) dengan D-76 varian 1 untuk TC-GS-IMPORT-885.
  - `brand-6.csv` diunggah ulang lewat UI pada tiap blok untuk membentuk draft baru.
- Hook umur draft D-76: kemampuan teknis yang disediakan tim FE/BE (fixture timestamp atau jam server).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Brand Client C direset (R1) di akhir tiap blok (aksi destruktif pada draft milik spec).

## Test Steps

### TC-GS-IMPORT-882: Select All dan Bulk Delete

1. Muat ulang halaman Import > Brand
2. Verifikasi Unsaved Banner "You have an unsaved import from [Date]. [Discard]" tampil
3. Centang baris #1
4. Klik `[Select All (6 records)]`
5. Klik `[Bulk Action ▾]`
6. Klik item `[Delete]`
7. Klik `[Delete]` pada dialog Delete Rows
8. Verifikasi toast sukses "Success, row has been deleted."
9. Verifikasi halaman kembali ke state belum ada draft: Dropzone tampil
10. Verifikasi Unsaved Banner tidak tampil
11. Klik [Upload File] di toolbar
12. Pilih berkas `brand-6.csv` di file picker
13. Klik [Confirm Mapping] tanpa mengubah dropdown File Column dari hasil auto-match
14. Verifikasi toast sukses: "Success, row has been added."
15. Muat ulang halaman Import > Brand
16. Verifikasi Staging Table menampilkan 6 baris `pending`
17. Verifikasi Unsaved Banner tidak tampil
18. Verifikasi tidak ada tombol `[Discard]` di halaman (draft baru berumur 0)
19. Reset Client C ke tanpa draft Tab Brand lewat skrip fixture

### TC-GS-IMPORT-883: Discard Draft pada draft berumur 24 jam

20. Atur ulang draft D-77 dengan umur 25 jam (varian 1)
21. Muat ulang halaman Import > Brand
22. Verifikasi Unsaved Banner "You have an unsaved import from [Date]. [Discard]" tampil
23. Klik `[Discard]` pada Unsaved Banner
24. Klik `[Discard Draft]` pada dialog Discard Draft
25. Verifikasi toast sukses "Success, draft has been discarded."
26. Verifikasi halaman kembali ke state belum ada draft: Dropzone tampil
27. Verifikasi Unsaved Banner tidak tampil
28. Klik [Upload File] di toolbar
29. Pilih berkas `brand-6.csv` di file picker
30. Klik [Confirm Mapping] tanpa mengubah dropdown File Column dari hasil auto-match
31. Verifikasi toast sukses: "Success, row has been added."
32. Muat ulang halaman Import > Brand
33. Verifikasi Staging Table menampilkan 6 baris `pending`
34. Verifikasi Unsaved Banner tidak tampil
35. Verifikasi tidak ada tombol `[Discard]` di halaman (draft baru berumur 0)
36. Reset Client C ke tanpa draft Tab Brand lewat skrip fixture

### TC-GS-IMPORT-885: Delete All Rows pada draft berumur 24 jam

37. Buat ulang draft D-78 (2 baris `error`) dengan umur 25 jam (varian 1)
38. Muat ulang halaman Import > Brand
39. Verifikasi Unsaved Banner "You have an unsaved import from [Date]. [Discard]" tampil
40. Verifikasi Staging Metric Cards Total Rows 2
41. Verifikasi Staging Metric Cards Errors 2
42. Verifikasi Error Summary Callout memuat baris pesan "Brand Name: Max. 120 characters" dengan `[Delete All Rows]`
43. Klik `[Delete All Rows]` pada baris pesan "Brand Name: Max. 120 characters"
44. Verifikasi baris dihapus seketika tanpa dialog konfirmasi
45. Verifikasi toast sukses "Success, row has been deleted."
46. Verifikasi halaman kembali ke state belum ada draft: Dropzone tampil
47. Verifikasi Unsaved Banner tidak tampil
48. Klik [Upload File] di toolbar
49. Pilih berkas `brand-6.csv` di file picker
50. Klik [Confirm Mapping] tanpa mengubah dropdown File Column dari hasil auto-match
51. Verifikasi toast sukses: "Success, row has been added."
52. Muat ulang halaman Import > Brand
53. Verifikasi Staging Table menampilkan 6 baris `pending`
54. Verifikasi Unsaved Banner tidak tampil
55. Verifikasi tidak ada tombol `[Discard]` di halaman (draft baru berumur 0)
56. Reset Client C ke tanpa draft Tab Brand lewat skrip fixture

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (kelas d, prinsip 13d; objek uji umur draft sebagai batas waktu: draft baru mulai dari umur 0).
- Spec memuat 56 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (hook umur draft D-76), tiap blok membuang draft berumur 24 jam dengan cara berbeda lalu membentuk draft baru dan berdiri sendiri dengan draft yang dibuat ulang, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 15, 21, 32, 38, 52 (muat ulang halaman); langkah 19, 36, 56 (reset Client C); langkah 20 dan 37 (menyiapkan ulang draft berumur 25 jam).
- Langkah 10, 27, 47 (absence Unsaved Banner) memakai Dropzone dan toast sukses yang diasersi sebelumnya sebagai anchor; langkah 17/18, 34/35, 54/55 memakai Staging Table 6 baris sebagai anchor.
- Temuan untuk QA:
  - TC-GS-IMPORT-882, 883, dan 885 menyebut D-76 varian 1 tanpa menyebut bahwa umur draft baru "0" hanya dapat diasersi lewat tidak adanya banner; spec mengasersi lewat Unsaved Banner dan `[Discard]` yang tidak tampil.
  - Post Condition "Draft Brand 6 baris pending baru pada Client C" setara dengan Expected d masing-masing TC.

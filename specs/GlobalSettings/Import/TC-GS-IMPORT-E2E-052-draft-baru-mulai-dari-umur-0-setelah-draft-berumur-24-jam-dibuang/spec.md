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
- Data Dinamis (Client C, disiapkan lewat skrip fixture oleh langkah 1 (TC-GS-IMPORT-882), langkah 21 (TC-GS-IMPORT-883), dan langkah 38 (TC-GS-IMPORT-885)):
  - D-77 draft Brand 6 baris `pending` dari `brand-6.csv` (Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp) dengan hook umur draft D-76 varian 1 (`created_at` dimundurkan 25 jam; hanya seed backdate) untuk TC-GS-IMPORT-882 dan 883.
  - D-78 draft Brand 2 baris `error` dari `brand-2-error.csv` (Row 1 Brand Name 121 karakter huruf `A`, Row 2 121 karakter huruf `B`) dengan D-76 varian 1 untuk TC-GS-IMPORT-885.
  - `brand-6.csv` diunggah ulang lewat UI pada tiap blok untuk membentuk draft baru.
- Hook umur draft D-76: kemampuan teknis yang disediakan tim FE/BE (fixture timestamp atau jam server).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Brand Client C direset (R1) di akhir tiap blok (aksi destruktif pada draft milik spec).

## Test Steps

### TC-GS-IMPORT-882: Select All dan Bulk Delete

1. Atur ulang draft D-77 dengan umur 25 jam (varian 1)
2. Muat ulang halaman Import > Brand
3. Verifikasi Unsaved Banner "You have an unsaved import from [Date]. [Discard]" tampil
4. Centang baris #1
5. Klik `[Select All (6 records)]`
6. Klik `[Bulk Action ▾]`
7. Klik item `[Delete]`
8. Klik `[Delete]` pada dialog Delete Rows
9. Verifikasi toast sukses "Success, row has been deleted."
10. Verifikasi halaman kembali ke state belum ada draft: Dropzone tampil
11. Verifikasi Unsaved Banner tidak tampil
12. Klik [Upload File] di toolbar
13. Pilih berkas `brand-6.csv` di file picker
14. Klik [Confirm Mapping] tanpa mengubah dropdown File Column dari hasil auto-match
15. Verifikasi toast sukses: "Success, row has been added."
16. Muat ulang halaman Import > Brand
17. Verifikasi Staging Table menampilkan 6 baris `pending`
18. Verifikasi Unsaved Banner tidak tampil
19. Verifikasi tidak ada tombol `[Discard]` di halaman (draft baru berumur 0)
20. Reset Client C ke tanpa draft Tab Brand lewat skrip fixture

### TC-GS-IMPORT-883: Discard Draft pada draft berumur 24 jam

21. Atur ulang draft D-77 dengan umur 25 jam (varian 1)
22. Muat ulang halaman Import > Brand
23. Verifikasi Unsaved Banner "You have an unsaved import from [Date]. [Discard]" tampil
24. Klik `[Discard]` pada Unsaved Banner
25. Klik `[Discard Draft]` pada dialog Discard Draft
26. Verifikasi toast sukses "Success, draft has been discarded."
27. Verifikasi halaman kembali ke state belum ada draft: Dropzone tampil
28. Verifikasi Unsaved Banner tidak tampil
29. Klik [Upload File] di toolbar
30. Pilih berkas `brand-6.csv` di file picker
31. Klik [Confirm Mapping] tanpa mengubah dropdown File Column dari hasil auto-match
32. Verifikasi toast sukses: "Success, row has been added."
33. Muat ulang halaman Import > Brand
34. Verifikasi Staging Table menampilkan 6 baris `pending`
35. Verifikasi Unsaved Banner tidak tampil
36. Verifikasi tidak ada tombol `[Discard]` di halaman (draft baru berumur 0)
37. Reset Client C ke tanpa draft Tab Brand lewat skrip fixture

### TC-GS-IMPORT-885: Delete All Rows pada draft berumur 24 jam

38. Buat ulang draft D-78 (2 baris `error`) dengan umur 25 jam (varian 1)
39. Muat ulang halaman Import > Brand
40. Verifikasi Unsaved Banner "You have an unsaved import from [Date]. [Discard]" tampil
41. Verifikasi Staging Metric Cards Total Rows 2
42. Verifikasi Staging Metric Cards Errors 2
43. Verifikasi Error Summary Callout memuat baris pesan "Brand Name: Max. 120 characters" dengan `[Delete All Rows]`
44. Klik `[Delete All Rows]` pada baris pesan "Brand Name: Max. 120 characters"
45. Verifikasi baris dihapus seketika tanpa dialog konfirmasi
46. Verifikasi toast sukses "Success, row has been deleted."
47. Verifikasi halaman kembali ke state belum ada draft: Dropzone tampil
48. Verifikasi Unsaved Banner tidak tampil
49. Klik [Upload File] di toolbar
50. Pilih berkas `brand-6.csv` di file picker
51. Klik [Confirm Mapping] tanpa mengubah dropdown File Column dari hasil auto-match
52. Verifikasi toast sukses: "Success, row has been added."
53. Muat ulang halaman Import > Brand
54. Verifikasi Staging Table menampilkan 6 baris `pending`
55. Verifikasi Unsaved Banner tidak tampil
56. Verifikasi tidak ada tombol `[Discard]` di halaman (draft baru berumur 0)
57. Reset Client C ke tanpa draft Tab Brand lewat skrip fixture

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (kelas d, prinsip 13d; objek uji umur draft sebagai batas waktu: draft baru mulai dari umur 0).
- Spec memuat 57 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (hook umur draft D-76), tiap blok membuang draft berumur 24 jam dengan cara berbeda lalu membentuk draft baru dan berdiri sendiri dengan draft yang dibuat ulang, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2, 16, 22, 33, 39, 53 (muat ulang halaman); langkah 20, 37, 57 (reset Client C); langkah 1, 21, dan 38 (menyiapkan ulang draft berumur 25 jam).
- Langkah 11, 28, 48 (absence Unsaved Banner) memakai Dropzone dan toast sukses yang diasersi sebelumnya sebagai anchor; langkah 18/19, 35/36, 55/56 memakai Staging Table 6 baris sebagai anchor.
- Temuan untuk QA:
  - TC-GS-IMPORT-882, 883, dan 885 menyebut D-76 varian 1 tanpa menyebut bahwa umur draft baru "0" hanya dapat diasersi lewat tidak adanya banner; spec mengasersi lewat Unsaved Banner dan `[Discard]` yang tidak tampil.
  - Post Condition "Draft Brand 6 baris pending baru pada Client C" setara dengan Expected d masing-masing TC.

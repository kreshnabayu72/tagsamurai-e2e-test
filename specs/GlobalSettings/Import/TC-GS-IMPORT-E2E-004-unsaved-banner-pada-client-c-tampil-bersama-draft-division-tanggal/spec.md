---
id: TC-GS-IMPORT-E2E-004-unsaved-banner-pada-client-c-tampil-bersama-draft-division-tanggal
title: "Unsaved Banner pada Client C: Tampil Bersama Draft Division, Tanggal Tetap Setelah Edit dan Append, Tidak Tampil Setelah Confirm Mapping, dan Draft Kurang dari 24 Jam Dibuang Tanpa Discard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-19
  - TC-GS-IMPORT-21
  - TC-GS-IMPORT-876
  - TC-GS-IMPORT-884
coverage:
  web: automated
---

# Unsaved Banner pada Client C: Tampil Bersama Draft Division, Tanggal Tetap Setelah Edit dan Append, Tidak Tampil Setelah Confirm Mapping, dan Draft Kurang dari 24 Jam Dibuang Tanpa Discard

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena spec memakai draft bersama Client C dan hook umur draft; lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import untuk Total Control Client C (TC-GS-IMPORT-19 dimulai di Import > Division; langkah memilih Sub-Tab ditulis eksplisit).
- Data Dinamis (skrip fixture, nama literal Population; D-12 disiapkan oleh langkah 1, D-13 oleh langkah 14, dan D-77 oleh langkah 49, bukan lewat UI):
  - D-12: draft Division 6 baris `pending` (isi seperti `division-6.csv`) pada Client C dengan tanggal pembuatan tiga hari sebelum hari uji (hanya seed backdate, bukan batas waktu yang diuji). Client C tanpa draft Tab Brand (Kontrak Fixture R1) untuk TC-GS-IMPORT-19.
  - D-13: draft Brand 12 baris `pending` (isi seperti `brand-12.csv`, baris #1 `Acme Corp`) pada Client C dengan tanggal pembuatan 17 Maret 2023 (TC-GS-IMPORT-21). Format tanggal General Settings Client C `dd/MM/yy`.
  - `brand-6.csv` (header `Brand Name`; 6 baris Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp) untuk TC-GS-IMPORT-21 dan 876.
  - D-77: draft Brand 6 baris `pending` (isi `brand-6.csv`) pada Client C dengan umur 0 tanpa varian D-76 (TC-GS-IMPORT-884).
- Reset: hook `beforeEach` mereset Client C sebelum langkah 1; sesudah itu, pada awal tiap blok TC (langkah 1, 14, 32, 49), draft Client C dipulihkan ke keadaan Precondition TC itu lewat skrip reset/seed (disediakan tim FE/BE; langkah reset ditulis sebagai aksi tanpa `Verifikasi`). Hook `after` menghapus draft sisa; tidak berasumsi seeding berhasil penuh.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: hook umur draft D-76 (backdate `created_at`; disediakan tim FE/BE), skrip seed/reset draft, file picker, muat ulang halaman.
- State global: tidak ada yang diubah selain draft Client C (dipulihkan hook).

## Test Steps

### TC-GS-IMPORT-19: Unsaved Banner tampil bersama draft Division dan tidak tampil di Sub-Tab Brand tanpa draft

1. Reset Client C ke tanpa draft; seed draft Division D-12 (6 baris `pending`, `created_at` dimundurkan ke tiga hari sebelum hari uji) tanpa draft Brand lewat skrip fixture; muat ulang halaman Import > Brand
2. Klik Sub-Tab Division
3. Perhatikan area di atas Staging Metric Cards di Sub-Tab Division
4. Verifikasi Unsaved Banner "You have an unsaved import from [Date]. [Discard]" tampil di Sub-Tab Division
5. Verifikasi [Date] berisi tanggal tiga hari sebelum hari uji menurut format tanggal General Settings
6. Klik Sub-Tab Brand
7. Perhatikan area di atas Staging Metric Cards dan area tabel di Sub-Tab Brand
8. Verifikasi Sub-Tab Brand menampilkan Dropzone
9. Verifikasi Sub-Tab Brand tidak menampilkan Unsaved Banner
10. Klik Sub-Tab Division kembali
11. Perhatikan area di atas Staging Metric Cards di Sub-Tab Division
12. Verifikasi Sub-Tab Division menampilkan satu Unsaved Banner
13. Verifikasi tidak ada banner kedua tentang usia draft di Sub-Tab Division

### TC-GS-IMPORT-21: Tanggal pada Unsaved Banner tidak berubah setelah draft diedit atau di-Append

14. Siapkan draft Brand D-13 (tanggal pembuatan 17 Maret 2023) pada Client C, muat ulang halaman, lalu klik Sub-Tab Brand
15. Perhatikan tanggal pada Unsaved Banner
16. Verifikasi tanggal pada Unsaved Banner `17/03/23`
17. Klik `[⋯]` pada baris #1
18. Pilih Edit
19. Ubah Brand Name baris #1 dari `Acme Corp` menjadi `Acme Corporation`
20. Klik `[Save]`
21. Perhatikan Staging Table
22. Verifikasi baris #1 tampil dengan Brand Name `Acme Corporation`
23. Klik `[Upload File]`
24. Pilih berkas `brand-6.csv` di file picker
25. Klik `[Append Records]`
26. Klik `[Confirm Mapping]`
27. Perhatikan Unsaved Banner dan Staging Metric Cards
28. Verifikasi tanggal pada Unsaved Banner tetap `17/03/23` dan tidak mengikuti tanggal edit maupun Append
29. Verifikasi Sub-Tab Brand menampilkan satu Unsaved Banner
30. Verifikasi tidak ada banner kedua tentang usia draft
31. Verifikasi Staging Metric Cards: Total Rows 18

### TC-GS-IMPORT-876: Unsaved Banner tidak tampil tepat setelah Confirm Mapping pertama

32. Reset draft Brand Client C ke tanpa draft (Kontrak Fixture R1), muat ulang halaman Import > Brand
33. Klik `[Upload File]` di toolbar
34. Pilih berkas `brand-6.csv` di file picker
35. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
36. Verifikasi muncul toast sukses "Success, row has been added."
37. Perhatikan area di atas Staging Metric Cards, toolbar, dan footer
38. Verifikasi Staging Table menampilkan 6 baris berstatus `pending`
39. Verifikasi Staging Metric Cards: Total Rows 6 (Active)
40. Verifikasi Staging Metric Cards: Ready to Import 6
41. Verifikasi footer `[Import (6)]` Enabled
42. Verifikasi Unsaved Banner tidak tampil
43. Verifikasi tidak ada tombol `[Discard]` di halaman
44. Muat ulang halaman Import > Brand
45. Perhatikan area di atas Staging Metric Cards, toolbar, dan footer
46. Verifikasi draft tetap 6 baris
47. Verifikasi Unsaved Banner tetap tidak tampil
48. Verifikasi tidak ada tombol `[Discard]` di halaman

### TC-GS-IMPORT-884: Draft baru berumur kurang dari 24 jam dibuang lewat Select All dan Bulk Delete tanpa Discard

49. Pulihkan draft Brand 6 baris D-77 (umur 0, tanpa hook umur draft) pada Client C, muat ulang halaman Import > Brand
50. Perhatikan area di atas Staging Metric Cards, toolbar, dan footer
51. Verifikasi Unsaved Banner tidak tampil
52. Verifikasi tidak ada tombol `[Discard]` di halaman
53. Verifikasi Staging Metric Cards: Total Rows 6 (Active)
54. Centang baris #1
55. Klik `[Select All (6 records)]`
56. Klik `[Bulk Action ▾]`
57. Klik item `[Delete]`
58. Perhatikan dialog
59. Verifikasi dialog dengan Title "Delete Rows" tampil
60. Verifikasi Body dialog berisi item list `Row #1` sampai `Row #6`
61. Verifikasi Body dialog memuat "The selected rows will be permanently removed from this draft. Are you sure you want to delete them? This action cannot be undone."
62. Verifikasi dialog memuat tombol `[Cancel]` dan `[Delete]`
63. Klik `[Delete]` pada dialog Delete Rows
64. Perhatikan toast dan halaman
65. Verifikasi toast sukses "Success, row has been deleted."
66. Verifikasi halaman kembali ke state belum ada draft: Dropzone tampil
67. Verifikasi Staging Metric Cards Total Rows 0
68. Muat ulang halaman Import > Brand
69. Perhatikan halaman
70. Verifikasi Dropzone tetap tampil
71. Verifikasi Unsaved Banner tidak tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 19, 21, 876, 884. TC-GS-IMPORT-884 (Select All dan Bulk Delete, destruktif) di akhir; draft Client C direset antar blok (langkah 14, 32, 49) karena tiap TC memiliki Precondition draft berbeda (Kontrak Fixture R1 dan R2).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2, 6, 10 (pindah Sub-Tab), langkah 1, 14, 32, 49 (reset/seed draft lewat skrip fixture sinkron, tanpa penanda tunggu), dan langkah mengamati sesuai Langkah Uji TC (3, 7, 11, 15, 21, 27, 37, 45, 50, 58, 64, 69). Langkah 2 memilih Sub-Tab Division karena Precondition TC-GS-IMPORT-19 menyebut user berada di Import > Division.
- TC-GS-IMPORT-884 memakai Select All dan Bulk Delete sungguhan atas seluruh draft Client C (data milik automation, konvensi bagian 2).
- Spec melewati sekitar 35 langkah (71 langkah). Seluruhnya satu topik (Unsaved Banner pada Client C) dengan akun dan client yang sama; tiap blok berdiri sendiri dengan draft yang disiapkan ulang, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-GS-IMPORT-876 mengasersi Unsaved Banner tidak tampil dan tanpa `[Discard]` tepat setelah Confirm Mapping pertama; klausa serupa sudah ada di klausa g TC-GS-IMPORT-1 sampai 6 (tumpang tindih cakupan, tidak kontradiktif).
  - TC-GS-IMPORT-884 membawa penanda `clock` dan `f5` padahal data hanya D-77 tanpa varian umur dan Expected tidak menyentuh batas 24 jam; spec tidak memakai hook jam untuk TC itu.
  - Skrip seed/reset draft dan hook backdate `created_at` (D-12, D-13, D-76, D-77) tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13). Nama berkas dan isi draft literal tanpa suffix `{runId}`; keunikan dijaga lewat reset draft.

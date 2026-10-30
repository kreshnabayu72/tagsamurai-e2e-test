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
- Data Dinamis (skrip fixture, nama literal Population; disiapkan sebelum tiap blok TC, bukan lewat UI):
  - D-12: draft Division 6 baris `pending` (isi seperti `division-6.csv`) pada Client C dengan tanggal pembuatan tiga hari sebelum hari uji (hanya seed backdate, bukan batas waktu yang diuji). Client C tanpa draft Tab Brand (Kontrak Fixture R1) untuk TC-GS-IMPORT-19.
  - D-13: draft Brand 12 baris `pending` (isi seperti `brand-12.csv`, baris #1 `Acme Corp`) pada Client C dengan tanggal pembuatan 17 Maret 2023 (TC-GS-IMPORT-21). Format tanggal General Settings Client C `dd/MM/yy`.
  - `brand-6.csv` (header `Brand Name`; 6 baris Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp) untuk TC-GS-IMPORT-21 dan 876.
  - D-77: draft Brand 6 baris `pending` (isi `brand-6.csv`) pada Client C dengan umur 0 tanpa varian D-76 (TC-GS-IMPORT-884).
- Reset: sebelum tiap blok TC, draft Client C dipulihkan ke keadaan Precondition TC itu lewat skrip reset/seed (disediakan tim FE/BE; langkah reset ditulis sebagai aksi tanpa `Verifikasi`). Hook `after` menghapus draft sisa; tidak berasumsi seeding berhasil penuh.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: hook umur draft D-76 (backdate `created_at`; disediakan tim FE/BE), skrip seed/reset draft, file picker, muat ulang halaman.
- State global: tidak ada yang diubah selain draft Client C (dipulihkan hook).

## Test Steps

### TC-GS-IMPORT-19: Unsaved Banner tampil bersama draft Division dan tidak tampil di Sub-Tab Brand tanpa draft

1. Klik Sub-Tab Division
2. Perhatikan area di atas Staging Metric Cards di Sub-Tab Division
3. Verifikasi Unsaved Banner "You have an unsaved import from [Date]. [Discard]" tampil di Sub-Tab Division
4. Verifikasi [Date] berisi tanggal tiga hari sebelum hari uji menurut format tanggal General Settings
5. Klik Sub-Tab Brand
6. Perhatikan area di atas Staging Metric Cards dan area tabel di Sub-Tab Brand
7. Verifikasi Sub-Tab Brand menampilkan Dropzone
8. Verifikasi Sub-Tab Brand tidak menampilkan Unsaved Banner
9. Klik Sub-Tab Division kembali
10. Perhatikan area di atas Staging Metric Cards di Sub-Tab Division
11. Verifikasi Sub-Tab Division menampilkan satu Unsaved Banner
12. Verifikasi tidak ada banner kedua tentang usia draft di Sub-Tab Division

### TC-GS-IMPORT-21: Tanggal pada Unsaved Banner tidak berubah setelah draft diedit atau di-Append

13. Siapkan draft Brand D-13 (tanggal pembuatan 17 Maret 2023) pada Client C, muat ulang halaman, lalu klik Sub-Tab Brand
14. Perhatikan tanggal pada Unsaved Banner
15. Verifikasi tanggal pada Unsaved Banner `17/03/23`
16. Klik `[⋯]` pada baris #1
17. Pilih Edit
18. Ubah Brand Name baris #1 dari `Acme Corp` menjadi `Acme Corporation`
19. Klik `[Save]`
20. Perhatikan Staging Table
21. Verifikasi baris #1 tampil dengan Brand Name `Acme Corporation`
22. Klik `[Upload File]`
23. Pilih berkas `brand-6.csv` di file picker
24. Klik `[Append Records]`
25. Klik `[Confirm Mapping]`
26. Perhatikan Unsaved Banner dan Staging Metric Cards
27. Verifikasi tanggal pada Unsaved Banner tetap `17/03/23` dan tidak mengikuti tanggal edit maupun Append
28. Verifikasi Sub-Tab Brand menampilkan satu Unsaved Banner
29. Verifikasi tidak ada banner kedua tentang usia draft
30. Verifikasi Staging Metric Cards: Total Rows 18

### TC-GS-IMPORT-876: Unsaved Banner tidak tampil tepat setelah Confirm Mapping pertama

31. Reset draft Brand Client C ke tanpa draft (Kontrak Fixture R1), muat ulang halaman Import > Brand
32. Klik `[Upload File]` di toolbar
33. Pilih berkas `brand-6.csv` di file picker
34. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
35. Verifikasi muncul toast sukses "Success, row has been added."
36. Perhatikan area di atas Staging Metric Cards, toolbar, dan footer
37. Verifikasi Staging Table menampilkan 6 baris berstatus `pending`
38. Verifikasi Staging Metric Cards: Total Rows 6 (Active)
39. Verifikasi Staging Metric Cards: Ready to Import 6
40. Verifikasi footer `[Import (6)]` Enabled
41. Verifikasi Unsaved Banner tidak tampil
42. Verifikasi tidak ada tombol `[Discard]` di halaman
43. Muat ulang halaman Import > Brand
44. Perhatikan area di atas Staging Metric Cards, toolbar, dan footer
45. Verifikasi draft tetap 6 baris
46. Verifikasi Unsaved Banner tetap tidak tampil
47. Verifikasi tidak ada tombol `[Discard]` di halaman

### TC-GS-IMPORT-884: Draft baru berumur kurang dari 24 jam dibuang lewat Select All dan Bulk Delete tanpa Discard

48. Pulihkan draft Brand 6 baris D-77 (umur 0, tanpa hook umur draft) pada Client C, muat ulang halaman Import > Brand
49. Perhatikan area di atas Staging Metric Cards, toolbar, dan footer
50. Verifikasi Unsaved Banner tidak tampil
51. Verifikasi tidak ada tombol `[Discard]` di halaman
52. Verifikasi Staging Metric Cards: Total Rows 6 (Active)
53. Centang baris #1
54. Klik `[Select All (6 records)]`
55. Klik `[Bulk Action ▾]`
56. Klik item `[Delete]`
57. Perhatikan dialog
58. Verifikasi dialog dengan Title "Delete Rows" tampil
59. Verifikasi Body dialog berisi item list `Row #1` sampai `Row #6`
60. Verifikasi Body dialog memuat "The selected rows will be permanently removed from this draft. Are you sure you want to delete them? This action cannot be undone."
61. Verifikasi dialog memuat tombol `[Cancel]` dan `[Delete]`
62. Klik `[Delete]` pada dialog Delete Rows
63. Perhatikan toast dan halaman
64. Verifikasi toast sukses "Success, row has been deleted."
65. Verifikasi halaman kembali ke state belum ada draft: Dropzone tampil
66. Verifikasi Staging Metric Cards Total Rows 0
67. Muat ulang halaman Import > Brand
68. Perhatikan halaman
69. Verifikasi Dropzone tetap tampil
70. Verifikasi Unsaved Banner tidak tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 19, 21, 876, 884. TC-GS-IMPORT-884 (Select All dan Bulk Delete, destruktif) di akhir; draft Client C direset antar blok (langkah 13, 31, 48) karena tiap TC memiliki Precondition draft berbeda (Kontrak Fixture R1 dan R2).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 5, 9 (pindah Sub-Tab), langkah 13, 31, 48 (reset/seed draft), dan langkah mengamati sesuai Langkah Uji TC (2, 6, 10, 14, 20, 26, 36, 44, 49, 57, 63, 68). Langkah 1 memilih Sub-Tab Division karena Precondition TC-GS-IMPORT-19 menyebut user berada di Import > Division.
- TC-GS-IMPORT-884 memakai Select All dan Bulk Delete sungguhan atas seluruh draft Client C (data milik automation, konvensi bagian 2).
- Spec melewati sekitar 35 langkah (70 langkah). Seluruhnya satu topik (Unsaved Banner pada Client C) dengan akun dan client yang sama; tiap blok berdiri sendiri dengan draft yang disiapkan ulang, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-GS-IMPORT-876 mengasersi Unsaved Banner tidak tampil dan tanpa `[Discard]` tepat setelah Confirm Mapping pertama; klausa serupa sudah ada di klausa g TC-GS-IMPORT-1 sampai 6 (tumpang tindih cakupan, tidak kontradiktif).
  - TC-GS-IMPORT-884 membawa penanda `clock` dan `f5` padahal data hanya D-77 tanpa varian umur dan Expected tidak menyentuh batas 24 jam; spec tidak memakai hook jam untuk TC itu.
  - Skrip seed/reset draft dan hook backdate `created_at` (D-12, D-13, D-76, D-77) tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13). Nama berkas dan isi draft literal tanpa suffix `{runId}`; keunikan dijaga lewat reset draft.

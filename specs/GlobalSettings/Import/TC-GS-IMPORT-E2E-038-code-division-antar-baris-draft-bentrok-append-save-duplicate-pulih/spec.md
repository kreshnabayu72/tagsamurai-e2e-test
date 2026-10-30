---
id: TC-GS-IMPORT-E2E-038-code-division-antar-baris-draft-bentrok-append-save-duplicate-pulih
title: "Code Division Antar-Baris dan Draft: Bentrok Append, Save Duplicate, dan Pulih Saat Baris Pembanding Dihapus atau Diubah"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-638
  - TC-GS-IMPORT-639
  - TC-GS-IMPORT-640
  - TC-GS-IMPORT-641
coverage:
  web: automated
---

# Code Division Antar-Baris dan Draft: Bentrok Append, Save Duplicate, dan Pulih Saat Baris Pembanding Dihapus atau Diubah

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; langkah pertama memilih Sub-Tab Division.
- Data:
  - Client C tanpa draft Tab Division untuk TC-GS-IMPORT-638 dan 639 (Kontrak Fixture R1; skrip reset disediakan tim FE/BE).
  - Berkas fixture D-07 (isi literal; berheader `Division Name,Code`): `division-code-base.csv` (`Billing,BIL` / `Procurement,PRC`) dan `division-code-append.csv` (`Invoicing,BIL`).
  - D-21: draft Division 3 baris pada Client C, disiapkan skrip fixture sebelum TC-GS-IMPORT-640 dan sebelum TC-GS-IMPORT-641: #1 `Billing` Code `BIL` berstatus `error` (pesan sel Code "Code already exists"), #2 `Procurement` Code `PRC` berstatus `pending`, #3 `Invoicing` Code `BIL` berstatus `pending`.
- Reset dan cleanup: tiap blok membuat atau menyiapkan draft Division pada Client C; draft dibuang atau disiapkan ulang (langkah eksplisit, S-09) sebelum blok berikutnya dan di hook `after`; tidak berasumsi seeding berhasil penuh.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; sesi edit baris (Duplicate, Edit, Remove, Save); skrip seed/reset draft D-21 (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain draft Client C (dibuang hook).

## Test Steps

### TC-GS-IMPORT-638: Code manual bentrok antara draft lama dan berkas Append

1. Klik Sub-Tab Division
2. Klik `[Upload File]`
3. Pilih berkas `division-code-base.csv` di file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Perhatikan Staging Table
6. Verifikasi Staging Table menampilkan 2 baris berstatus `pending`
7. Klik `[Upload File]`
8. Pilih berkas `division-code-append.csv` di file picker
9. Klik `[Append Records]` pada dialog "Append to Draft"
10. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
11. Perhatikan Staging Table, Error Summary Callout, dan Staging Metric Cards
12. Verifikasi Staging Table menampilkan 3 baris
13. Verifikasi #1 `Billing` berstatus `error` dengan pesan sel Code "Code already exists"
14. Verifikasi #2 `Procurement` berstatus `pending`
15. Verifikasi #3 `Invoicing` berstatus `pending`
16. Verifikasi Error Summary Callout memuat satu baris pesan "Code already exists" dengan badge "1 row"
17. Verifikasi Staging Metric Cards: Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled)
18. Buang draft Division Client C (reset ke tanpa draft, Kontrak Fixture R1) lalu muat ulang halaman Import > Division

### TC-GS-IMPORT-639: Save sesi Duplicate dengan Code manual identik tidak diblokir

19. Klik `[Upload File]`
20. Pilih berkas `division-code-base.csv` di file picker
21. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
22. Klik `⋯` pada baris #2 `Procurement`
23. Pilih Duplicate
24. Ubah Division Name salinan menjadi `Sourcing` dan biarkan Code `PRC`
25. Klik `[Save]`
26. Verifikasi `[Save]` tidak diblokir dan muncul toast "Success, row has been added."
27. Perhatikan Staging Table, Error Summary Callout, dan Staging Metric Cards
28. Verifikasi Staging Table menampilkan 3 baris
29. Verifikasi #1 `Billing` berstatus `pending`
30. Verifikasi #2 `Procurement` berstatus `error` dengan pesan sel Code "Code already exists"
31. Verifikasi #3 `Sourcing` berstatus `pending`
32. Verifikasi Error Summary Callout memuat satu baris pesan "Code already exists" dengan badge "1 row"
33. Verifikasi Staging Metric Cards: Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled)
34. Buang draft Division Client C (reset ke tanpa draft, Kontrak Fixture R1) lalu siapkan draft D-21 dan muat ulang halaman Import > Division

### TC-GS-IMPORT-641: Status error Code Division kembali pending saat Code baris pembanding diubah lewat Save

35. Klik `⋯` pada baris #3 `Invoicing`
36. Pilih Edit
37. Ubah Code baris #3 dari `BIL` menjadi `INV`
38. Klik `[Save]`
39. Verifikasi muncul toast "Success, row has been updated."
40. Perhatikan Staging Table dan Staging Metric Cards
41. Verifikasi Staging Table menampilkan 3 baris berstatus `pending`: #1 `Billing` `BIL`, #2 `Procurement` `PRC`, #3 `Invoicing` `INV`
42. Verifikasi baris #1 tidak menampilkan pesan "Code already exists"
43. Verifikasi Staging Metric Cards: Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled)
44. Siapkan ulang draft D-21 pada Client C dan muat ulang halaman Import > Division

### TC-GS-IMPORT-640: Status error Code Division kembali pending saat baris pembanding dihapus

45. Klik `⋯` pada baris #3 `Invoicing`
46. Pilih Remove
47. Klik `[Delete]` pada dialog Delete Row
48. Verifikasi muncul toast "Success, row has been deleted."
49. Verifikasi draft berisi 2 baris
50. Muat ulang halaman Import > Division
51. Perhatikan baris #1
52. Verifikasi baris #1 `Billing` berstatus `pending` tanpa pesan "Code already exists"
53. Verifikasi Staging Metric Cards: Total Rows 2 (Active), Ready to Import 2, Errors 0 (Disabled), Duplicates 0 (Disabled)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 638, 639, 641, 640. Urutan menyimpang dari urutan TC sumber karena TC-GS-IMPORT-640 menghapus baris draft (destruktif) dan ditaruh paling akhir; draft D-21 disiapkan ulang sebelum tiap blok yang memakainya (langkah 34 dan 44, Kontrak Fixture R1/R2).
- Alasan di atas sekitar 35 langkah (53 langkah): satu topik (status Code Division antar-baris pada draft Client C); tiap blok memakai draft sendiri yang dibuang atau disiapkan ulang sehingga berdiri sendiri; kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (pindah Sub-Tab), langkah 5, 11, 27, 40, 51 (mengamati sesuai Langkah Uji TC), langkah 18, 34, 44 (reset/seed draft), langkah 50 (muat ulang sesuai Langkah Uji TC-GS-IMPORT-640).
- Temuan untuk QA:
  - TC-GS-IMPORT-640 dan 641 memakai D-21 yang "disiapkan lewat skrip fixture sebelum setiap TC pemakai"; skrip tidak didefinisikan di TC, PRD, atau LLD dan disediakan tim FE/BE (S-13). Nama Division draft literal (`Billing`, `Procurement`, `Invoicing`, `Sourcing`) tidak di-commit sehingga tidak bentrok dengan master data; tanpa suffix `{runId}`.
  - TC-GS-IMPORT-638 sampai 641 menyebut "Code already exists" pada baris `error`; tidak ada Post Condition observasi tambahan.

---
id: TC-GS-IMPORT-E2E-197-modal-changelog-import-kombinasi-search-dan-filter-clear-field-empty
title: "Modal Changelog Import: kombinasi Search dan Filter, Clear Field, empty state pulih"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-784
  - TC-GS-IMPORT-785
  - TC-GS-IMPORT-786
  - TC-GS-IMPORT-787
coverage:
  web: automated
---

# Modal Changelog Import: kombinasi Search dan Filter, Clear Field, empty state pulih

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena state global dibagi antar spec dan Changelog Import Client E disetel ulang oleh skrip seed (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Import > Brand Client E.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis D-60: Changelog Import Client E berisi tepat 30 entri seed, disiapkan lewat skrip seed di hook `before` (skrip juga membersihkan entri hasil commit spec lain; mekanisme disediakan tim FE/BE). Entri ke-i (i = 1 sampai 30) bertanggal i Sep 2026 pukul 10:00 UTC+7; Action berulang Import Brand, Import Measurement, Import Position, Import Division, Import User Login, Import User Non Login (lima entri per Action); Modified By Yoga Permana (i ganjil) dan Dimas Anggoro (i genap). Spec hanya membaca.
- General Settings Client E: Date Format `dd MMM yy`, Time Format 24 jam (`HH:mm`), Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` (Pre-setup, tidak diubah).
- Cleanup (hook `after`): entri seed D-60 dibersihkan; urutan sort modal tidak disimpan di server.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Search lalu Filter (TC-GS-IMPORT-784)

1. Klik `[Changelog]`
2. Ketik Search `dimas`, tekan Enter
3. Verifikasi tabel menampilkan sedikitnya satu baris
4. Verifikasi seluruh baris tabel bermodified `Dimas A`
5. Verifikasi pagination menampilkan "Showing 1 - 10 of 15 items"
6. Klik icon Filter
7. Pilih Action `Import Measurement`
8. Klik `[Apply]`
9. Verifikasi tabel menampilkan 5 entri `Import Measurement` oleh `Dimas A` (Date `26 Sep 26`, `20 Sep 26`, `14 Sep 26`, `08 Sep 26`, dan `02 Sep 26`)
10. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
11. Klik `(←)` pada kotak Search

### Filter lalu Search (TC-GS-IMPORT-785)

12. Klik icon Filter
13. Pilih Action `Import Measurement`
14. Klik `[Apply]`
15. Verifikasi tabel menampilkan 5 entri `Import Measurement`
16. Ketik Search `dimas`, tekan Enter
17. Verifikasi tabel menampilkan 5 entri `Import Measurement` oleh `Dimas A` (Date `26 Sep 26`, `20 Sep 26`, `14 Sep 26`, `08 Sep 26`, dan `02 Sep 26`), identik dengan hasil Search lalu Filter
18. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
19. Klik `(←)` pada kotak Search

### Clear Field tidak mereset Search dan Sort (TC-GS-IMPORT-786)

20. Ketik Search `dimas`, tekan Enter
21. Klik icon Filter
22. Pilih Action `Import Measurement`
23. Klik `[Apply]`
24. Klik header kolom Date sekali
25. Verifikasi baris pertama Date `02 Sep 26` (Oldest First)
26. Klik icon Filter
27. Klik `[Clear Field]`
28. Klik `[Apply]`
29. Verifikasi filter Action terlepas
30. Verifikasi Search `dimas` tetap aktif dengan pagination "Showing 1 - 10 of 15 items"
31. Verifikasi baris pertama tetap Date `02 Sep 26`
32. Klik `✕` pada input Search, tekan Enter
33. Verifikasi pagination menampilkan "Showing 1 - 10 of 30 items"
34. Verifikasi baris pertama Date `01 Sep 26` (sort Oldest First tetap aktif)
35. Klik header kolom Date dua kali hingga indikator sort hilang dan urutan kembali default Date descending

### Empty state pulih saat Search dikosongkan (TC-GS-IMPORT-787)

36. Klik icon Filter
37. Pilih Action `Import Brand`
38. Klik `[Apply]`
39. Verifikasi tabel menampilkan 5 entri `Import Brand`
40. Ketik Search `dimas`, tekan Enter
41. Verifikasi tabel menampilkan Title "No results found"
42. Verifikasi tabel menampilkan Description "Try adjusting your search or filter."
43. Klik `✕` pada input Search, tekan Enter
44. Verifikasi tabel kembali menampilkan 5 entri `Import Brand`
45. Verifikasi Filter Action `Import Brand` tetap aktif
46. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 46 langkah, di atas 35 langkah. Alasan: satu surface (Modal Changelog) dan satu dataset seed read-only (D-60); empat blok berdiri sendiri dengan pembersihan Search, Filter, dan Sort eksplisit antar blok (langkah 10, 11, 18, 19, 35, 46).
- Langkah 10, 11, 18, 19, 35, 46 adalah langkah penghubung (S-03, S-09). Langkah 35 mereset sort lewat tahap ketiga yang kembali ke Date descending.
- Langkah 3-4 dan 15: pembanding generik sebelum asersi universal (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-IMPORT-786 menulis "Kosongkan input Search lewat icon (✕) ... Tekan Enter"; spec menuliskannya "Klik `✕` pada input Search, tekan Enter" sesuai konvensi Search.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.

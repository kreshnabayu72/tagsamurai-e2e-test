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
- Data Dinamis D-60: Changelog Import Client E berisi tepat 30 entri seed, disiapkan oleh langkah 1 lewat skrip seed (skrip juga membersihkan entri hasil commit spec lain; mekanisme disediakan tim FE/BE). Entri ke-i (i = 1 sampai 30) bertanggal i Sep 2026 pukul 10:00 UTC+7; Action berulang Import Brand, Import Measurement, Import Position, Import Division, Import User Login, Import User Non Login (lima entri per Action); Modified By Yoga Permana (i ganjil) dan Dimas Anggoro (i genap). Spec hanya membaca.
- General Settings Client E: Date Format `dd MMM yy`, Time Format 24 jam (`HH:mm`), Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` (Pre-setup, tidak diubah).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog Import Client E (total entri, dibaca sebelum aksi sebagai N untuk `Verifikasi` selisih).
- Cleanup (hook `after`): entri seed D-60 dibersihkan; urutan sort modal tidak disimpan di server.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Search lalu Filter (TC-GS-IMPORT-784)

1. Seed Changelog Import Client E 30 entri (D-60) lewat skrip seed, lalu muat ulang halaman Import > Brand
2. Baca jumlah entri Changelog Import Client E sebagai N lewat kemampuan baca jumlah entri
3. Klik `[Changelog]`
4. Ketik Search `dimas`, tekan Enter
5. Verifikasi tabel menampilkan sedikitnya satu baris
6. Verifikasi seluruh baris tabel bermodified `Dimas A`
7. Verifikasi pagination menampilkan "Showing 1 - 10 of 15 items"
8. Klik icon Filter
9. Pilih Action `Import Measurement`
10. Klik `[Apply]`
11. Verifikasi tabel menampilkan 5 entri `Import Measurement` oleh `Dimas A` (Date `26 Sep 26`, `20 Sep 26`, `14 Sep 26`, `08 Sep 26`, dan `02 Sep 26`)
12. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
13. Klik `(←)` pada kotak Search

### Filter lalu Search (TC-GS-IMPORT-785)

14. Klik icon Filter
15. Pilih Action `Import Measurement`
16. Klik `[Apply]`
17. Verifikasi tabel menampilkan 5 entri `Import Measurement`
18. Ketik Search `dimas`, tekan Enter
19. Verifikasi tabel menampilkan 5 entri `Import Measurement` oleh `Dimas A` (Date `26 Sep 26`, `20 Sep 26`, `14 Sep 26`, `08 Sep 26`, dan `02 Sep 26`), identik dengan hasil Search lalu Filter
20. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
21. Klik `(←)` pada kotak Search

### Clear Field tidak mereset Search dan Sort (TC-GS-IMPORT-786)

22. Ketik Search `dimas`, tekan Enter
23. Klik icon Filter
24. Pilih Action `Import Measurement`
25. Klik `[Apply]`
26. Klik header kolom Date sekali
27. Verifikasi baris pertama Date `02 Sep 26` (Oldest First)
28. Klik icon Filter
29. Klik `[Clear Field]`
30. Klik `[Apply]`
31. Verifikasi filter Action terlepas
32. Verifikasi Search `dimas` tetap aktif dengan pagination "Showing 1 - 10 of 15 items"
33. Verifikasi baris pertama tetap Date `02 Sep 26`
34. Klik `✕` pada input Search, tekan Enter
35. Verifikasi pagination menampilkan "Showing 1 - 10 of N items" dan selisih total terhadap N yang dibaca pada langkah 2 adalah 0
36. Verifikasi baris pertama Date `01 Sep 26` (sort Oldest First tetap aktif)
37. Klik header kolom Date dua kali hingga indikator sort hilang dan urutan kembali default Date descending

### Empty state pulih saat Search dikosongkan (TC-GS-IMPORT-787)

38. Klik icon Filter
39. Pilih Action `Import Brand`
40. Klik `[Apply]`
41. Verifikasi tabel menampilkan 5 entri `Import Brand`
42. Ketik Search `dimas`, tekan Enter
43. Verifikasi tabel menampilkan Title "No results found"
44. Verifikasi tabel menampilkan Description "Try adjusting your search or filter."
45. Klik `✕` pada input Search, tekan Enter
46. Verifikasi tabel kembali menampilkan 5 entri `Import Brand`
47. Verifikasi Filter Action `Import Brand` tetap aktif
48. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 48 langkah, di atas 35 langkah. Alasan: satu surface (Modal Changelog) dan satu dataset seed read-only (D-60); empat blok berdiri sendiri dengan pembersihan Search, Filter, dan Sort eksplisit antar blok (langkah 12, 13, 20, 21, 37, 48).
- Langkah 1 adalah langkah penghubung pembuka (seed D-60 lalu muat ulang halaman; S-03, K-7), tanpa `Verifikasi`.
- Langkah 12, 13, 20, 21, 37, 48 adalah langkah penghubung (S-03, S-09). Langkah 37 mereset sort lewat tahap ketiga yang kembali ke Date descending. Langkah 2 membaca N lewat kemampuan baca (penghubung tanpa `Verifikasi`, sesudah seed dan sebelum aksi UI apa pun).
- Langkah 5-6 dan 17: pembanding generik sebelum asersi universal (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-IMPORT-786 menulis "Kosongkan input Search lewat icon (✕) ... Tekan Enter"; spec menuliskannya "Klik `✕` pada input Search, tekan Enter" sesuai konvensi Search.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
  - Jumlah 30 entri adalah keadaan seed D-60 yang dijamin skrip seed (langkah 1), bukan total audit trail yang tumbuh; TC-GS-IMPORT-786 Expected menulis total "of 30 items" absolut, sedangkan spec mengasersi selisih 0 terhadap N yang dibaca sebelum aksi (langkah 2, 35; S-12). Hitungan yang dibatasi Search ("of 15" pada langkah 7 dan 32) dipertahankan sebagai angka dari keadaan seed D-60 dan tidak dijadikan selisih karena kemampuan baca hanya memberi total entri tanpa Search; Expected TC menulis angka itu absolut. Mekanisme skrip seed dan kemampuan baca disediakan tim FE/BE.

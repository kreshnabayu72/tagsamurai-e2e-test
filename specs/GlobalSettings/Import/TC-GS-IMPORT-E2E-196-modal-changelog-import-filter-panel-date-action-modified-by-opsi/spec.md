---
id: TC-GS-IMPORT-E2E-196-modal-changelog-import-filter-panel-date-action-modified-by-opsi
title: "Modal Changelog Import: Filter Panel (Date, Action, Modified By), opsi dropdown, chip +N more, filter gabungan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-493
  - TC-GS-IMPORT-494
  - TC-GS-IMPORT-495
  - TC-GS-IMPORT-496
  - TC-GS-IMPORT-780
  - TC-GS-IMPORT-781
  - TC-GS-IMPORT-782
  - TC-GS-IMPORT-783
coverage:
  web: automated
---

# Modal Changelog Import: Filter Panel (Date, Action, Modified By), opsi dropdown, chip +N more, filter gabungan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena state global dibagi antar spec dan Changelog Import Client E disetel ulang oleh skrip seed (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Import > Brand Client E.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis D-60: Changelog Import Client E berisi tepat 30 entri seed, disiapkan oleh langkah 1 lewat skrip seed (skrip juga membersihkan entri hasil commit spec lain; mekanisme disediakan tim FE/BE). Entri ke-i (i = 1 sampai 30) bertanggal i Sep 2026 pukul 10:00 UTC+7; Action berulang Import Brand, Import Measurement, Import Position, Import Division, Import User Login, Import User Non Login (lima entri per Action); Modified By Yoga Permana (i ganjil) dan Dimas Anggoro (i genap). Tanggal dan hitungan yang diasersi dibaca dari tabel seed ini. Spec hanya membaca.
- General Settings Client E: Date Format `dd MMM yy`, Time Format 24 jam (`HH:mm`), Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` (Pre-setup, tidak diubah).
- Cleanup (hook `after`): entri seed D-60 dibersihkan; state filter modal tidak disimpan di server.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Struktur Filter Panel (TC-GS-IMPORT-493)

1. Seed Changelog Import Client E 30 entri (D-60) lewat skrip seed, lalu muat ulang halaman Import > Brand
2. Klik `[Changelog]`
3. Klik icon Filter
4. Verifikasi Filter Panel memuat field Date dengan placeholder "Select date"
5. Verifikasi Filter Panel memuat field Action (multi-select searchable) dengan placeholder "All actions"
6. Verifikasi Filter Panel memuat field Modified By (multi-select searchable) dengan placeholder "All users"
7. Verifikasi tidak ada field filter Field
8. Verifikasi Filter Panel memuat tombol `[Clear Field]` dan `[Apply]`

### Opsi dropdown (TC-GS-IMPORT-780)

9. Buka dropdown Action
10. Verifikasi dropdown Action memuat enam opsi: Import Brand, Import Measurement, Import Position, Import Division, Import User Login, dan Import User Non Login
11. Ketik `user` pada input pencarian di dalam dropdown Action
12. Verifikasi opsi tersaring menjadi `Import User Login` dan `Import User Non Login`
13. Buka dropdown Modified By
14. Verifikasi dropdown Modified By memuat dua opsi, satu untuk Yoga Permana dan satu untuk Dimas Anggoro

### Filter Action dan Modified By (TC-GS-IMPORT-494, 496)

15. Klik `[Clear Field]`, lalu klik `[Apply]`
16. Klik icon Filter
17. Pilih Action `Import Brand`
18. Klik `[Apply]`
19. Verifikasi tabel menampilkan 5 entri `Import Brand` (Date `25 Sep 26`, `19 Sep 26`, `13 Sep 26`, `07 Sep 26`, dan `01 Sep 26`)
20. Verifikasi pagination menampilkan "Showing 1 - 5 of 5 items"
21. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
22. Klik icon Filter
23. Pilih Modified By `Dimas Anggoro`
24. Klik `[Apply]`
25. Verifikasi tabel menampilkan sedikitnya satu baris
26. Verifikasi seluruh baris tabel bermodified `Dimas A`
27. Verifikasi pagination menampilkan "Showing 1 - 10 of 15 items"
28. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### Filter Date inklusif (TC-GS-IMPORT-495)

29. Klik icon Filter
30. Pilih tanggal 10 Sep 26 sebagai awal dan 12 Sep 26 sebagai akhir pada field Date
31. Verifikasi field Date menampilkan rentang `10 Sep 26` sampai `12 Sep 26` dalam format `dd MMM yy`
32. Klik `[Apply]`
33. Verifikasi tabel menampilkan 3 entri (Date `12 Sep 26`, `11 Sep 26`, dan `10 Sep 26`) termasuk kedua tanggal batas
34. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### Dua opsi Action dan chip +N more (TC-GS-IMPORT-782, 781)

35. Klik icon Filter
36. Pilih Action `Import Brand` dan `Import Measurement`
37. Klik `[Apply]`
38. Verifikasi tabel menampilkan 10 entri: 5 entri `Import Brand` dan 5 entri `Import Measurement`
39. Verifikasi pagination menampilkan "Showing 1 - 10 of 10 items"
40. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
41. Klik icon Filter
42. Pilih keenam opsi Action berurutan dari Import Brand sampai Import User Non Login
43. Verifikasi field Action menampilkan chip opsi terpilih dan satu chip `+N more` dengan jumlah chip yang tampil ditambah N sama dengan 6
44. Klik tanda silang (✕) pada chip `Import Brand`
45. Buka dropdown Action
46. Verifikasi opsi `Import Brand` tidak lagi tercentang
47. Verifikasi jumlah opsi terpilih menjadi 5
48. Klik `[Apply]`
49. Verifikasi tabel hanya memuat entri dari lima Action yang tersisa
50. Verifikasi pagination menampilkan "Showing 1 - 10 of 25 items"
51. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### Filter Action dan Date (AND) (TC-GS-IMPORT-783)

52. Klik icon Filter
53. Pilih Action `Import Brand`
54. Pilih tanggal 01 Sep 26 sebagai awal dan 14 Sep 26 sebagai akhir pada field Date
55. Klik `[Apply]`
56. Verifikasi tabel menampilkan 3 entri `Import Brand` (Date `13 Sep 26`, `07 Sep 26`, dan `01 Sep 26`)
57. Verifikasi entri `Import Brand` tanggal 19 Sep 26 dan 25 Sep 26 tidak tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 57 langkah, di atas 35 langkah. Alasan: satu surface (Filter Panel Modal Changelog) dan satu dataset seed read-only (D-60); blok filter berdiri sendiri dengan pembersihan filter eksplisit antar blok (langkah 15, 21, 28, 34, 40, 51), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah 1 adalah langkah penghubung pembuka (seed D-60 lalu muat ulang halaman; S-03, K-7), tanpa `Verifikasi`.
- Langkah 15, 21, 28, 34, 40, 51 adalah langkah penghubung pembersih filter (S-03, S-09). Langkah 15 menutup pembukaan dropdown pada blok sebelumnya.
- Langkah 25 dan 26: pembanding generik sebelum asersi universal (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-IMPORT-781 Expected a ("satu chip `+N more` dengan jumlah chip yang tampil ditambah N sama dengan 6") tidak menyebut jumlah chip yang tampil maupun nilai N; langkah 43 mengasersi persis rumusan TC (jumlah chip yang tampil + N = 6) dan tidak menetapkan angka.
  - TC-GS-IMPORT-781 Expected b menyebut "jumlah opsi terpilih menjadi 5" tanpa menyebut cara mengamatinya; spec mengasersi centang opsi di dropdown Action.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
  - Hitungan berfilter ("of 5" pada langkah 20, "of 15" pada langkah 27, "of 10" pada langkah 39, "of 25" pada langkah 50) dibatasi Filter Panel dan bergantung pada keadaan seed D-60 (lima entri per Action, 15 entri Dimas Anggoro, skrip seed membersihkan entri lain); tidak dijadikan selisih karena spec ini tidak memakai kemampuan baca jumlah entri (total entri tanpa Filter) dan Expected TC menulis angka itu absolut (S-14: Filter pembatas). Spec ini tidak mengasersi total entri tanpa Filter.

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
- Data Dinamis D-60: Changelog Import Client E berisi tepat 30 entri seed, disiapkan lewat skrip seed di hook `before` (skrip juga membersihkan entri hasil commit spec lain; mekanisme disediakan tim FE/BE). Entri ke-i (i = 1 sampai 30) bertanggal i Sep 2026 pukul 10:00 UTC+7; Action berulang Import Brand, Import Measurement, Import Position, Import Division, Import User Login, Import User Non Login (lima entri per Action); Modified By Yoga Permana (i ganjil) dan Dimas Anggoro (i genap). Tanggal dan hitungan yang diasersi dibaca dari tabel seed ini. Spec hanya membaca.
- General Settings Client E: Date Format `dd MMM yy`, Time Format 24 jam (`HH:mm`), Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` (Pre-setup, tidak diubah).
- Cleanup (hook `after`): entri seed D-60 dibersihkan; state filter modal tidak disimpan di server.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Struktur Filter Panel (TC-GS-IMPORT-493)

1. Klik `[Changelog]`
2. Klik icon Filter
3. Verifikasi Filter Panel memuat field Date dengan placeholder "Select date"
4. Verifikasi Filter Panel memuat field Action (multi-select searchable) dengan placeholder "All actions"
5. Verifikasi Filter Panel memuat field Modified By (multi-select searchable) dengan placeholder "All users"
6. Verifikasi tidak ada field filter Field
7. Verifikasi Filter Panel memuat tombol `[Clear Field]` dan `[Apply]`

### Opsi dropdown (TC-GS-IMPORT-780)

8. Buka dropdown Action
9. Verifikasi dropdown Action memuat enam opsi: Import Brand, Import Measurement, Import Position, Import Division, Import User Login, dan Import User Non Login
10. Ketik `user` pada input pencarian di dalam dropdown Action
11. Verifikasi opsi tersaring menjadi `Import User Login` dan `Import User Non Login`
12. Buka dropdown Modified By
13. Verifikasi dropdown Modified By memuat dua opsi, satu untuk Yoga Permana dan satu untuk Dimas Anggoro

### Filter Action dan Modified By (TC-GS-IMPORT-494, 496)

14. Klik `[Clear Field]`, lalu klik `[Apply]`
15. Klik icon Filter
16. Pilih Action `Import Brand`
17. Klik `[Apply]`
18. Verifikasi tabel menampilkan 5 entri `Import Brand` (Date `25 Sep 26`, `19 Sep 26`, `13 Sep 26`, `07 Sep 26`, dan `01 Sep 26`)
19. Verifikasi pagination menampilkan "Showing 1 - 5 of 5 items"
20. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
21. Klik icon Filter
22. Pilih Modified By `Dimas Anggoro`
23. Klik `[Apply]`
24. Verifikasi tabel menampilkan sedikitnya satu baris
25. Verifikasi seluruh baris tabel bermodified `Dimas A`
26. Verifikasi pagination menampilkan "Showing 1 - 10 of 15 items"
27. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### Filter Date inklusif (TC-GS-IMPORT-495)

28. Klik icon Filter
29. Pilih tanggal 10 Sep 26 sebagai awal dan 12 Sep 26 sebagai akhir pada field Date
30. Verifikasi field Date menampilkan rentang `10 Sep 26` sampai `12 Sep 26` dalam format `dd MMM yy`
31. Klik `[Apply]`
32. Verifikasi tabel menampilkan 3 entri (Date `12 Sep 26`, `11 Sep 26`, dan `10 Sep 26`) termasuk kedua tanggal batas
33. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### Dua opsi Action dan chip +N more (TC-GS-IMPORT-782, 781)

34. Klik icon Filter
35. Pilih Action `Import Brand` dan `Import Measurement`
36. Klik `[Apply]`
37. Verifikasi tabel menampilkan 10 entri: 5 entri `Import Brand` dan 5 entri `Import Measurement`
38. Verifikasi pagination menampilkan "Showing 1 - 10 of 10 items"
39. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
40. Klik icon Filter
41. Pilih keenam opsi Action berurutan dari Import Brand sampai Import User Non Login
42. Verifikasi field Action menampilkan chip opsi terpilih dan satu chip `+N more` dengan jumlah chip yang tampil ditambah N sama dengan 6
43. Klik tanda silang (✕) pada chip `Import Brand`
44. Buka dropdown Action
45. Verifikasi opsi `Import Brand` tidak lagi tercentang
46. Verifikasi jumlah opsi terpilih menjadi 5
47. Klik `[Apply]`
48. Verifikasi tabel hanya memuat entri dari lima Action yang tersisa
49. Verifikasi pagination menampilkan "Showing 1 - 10 of 25 items"
50. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### Filter Action dan Date (AND) (TC-GS-IMPORT-783)

51. Klik icon Filter
52. Pilih Action `Import Brand`
53. Pilih tanggal 01 Sep 26 sebagai awal dan 14 Sep 26 sebagai akhir pada field Date
54. Klik `[Apply]`
55. Verifikasi tabel menampilkan 3 entri `Import Brand` (Date `13 Sep 26`, `07 Sep 26`, dan `01 Sep 26`)
56. Verifikasi entri `Import Brand` tanggal 19 Sep 26 dan 25 Sep 26 tidak tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 56 langkah, di atas 35 langkah. Alasan: satu surface (Filter Panel Modal Changelog) dan satu dataset seed read-only (D-60); blok filter berdiri sendiri dengan pembersihan filter eksplisit antar blok (langkah 14, 20, 27, 33, 39, 50), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah 14, 20, 27, 33, 39, 50 adalah langkah penghubung pembersih filter (S-03, S-09). Langkah 14 menutup pembukaan dropdown pada blok sebelumnya.
- Langkah 24 dan 25: pembanding generik sebelum asersi universal (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-IMPORT-781 Expected a ("satu chip `+N more` dengan jumlah chip yang tampil ditambah N sama dengan 6") tidak menyebut jumlah chip yang tampil maupun nilai N; langkah 42 mengasersi persis rumusan TC (jumlah chip yang tampil + N = 6) dan tidak menetapkan angka.
  - TC-GS-IMPORT-781 Expected b menyebut "jumlah opsi terpilih menjadi 5" tanpa menyebut cara mengamatinya; spec mengasersi centang opsi di dropdown Action.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.

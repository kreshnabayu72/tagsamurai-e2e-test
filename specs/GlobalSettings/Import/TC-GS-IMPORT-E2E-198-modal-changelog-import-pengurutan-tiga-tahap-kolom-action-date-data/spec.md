---
id: TC-GS-IMPORT-E2E-198-modal-changelog-import-pengurutan-tiga-tahap-kolom-action-date-data
title: "Modal Changelog Import: pengurutan tiga tahap kolom Action, Date, Data, Modified By"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-497
  - TC-GS-IMPORT-788
  - TC-GS-IMPORT-789
  - TC-GS-IMPORT-790
coverage:
  web: automated
---

# Modal Changelog Import: pengurutan tiga tahap kolom Action, Date, Data, Modified By

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena state global dibagi antar spec dan Changelog Import Client E disetel ulang oleh skrip seed (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Import > Brand Client E.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis D-60: Changelog Import Client E berisi tepat 30 entri seed, disiapkan oleh langkah 1 lewat skrip seed (skrip juga membersihkan entri hasil commit spec lain; mekanisme disediakan tim FE/BE). Entri ke-i (i = 1 sampai 30) bertanggal i Sep 2026 pukul 10:00 UTC+7; Action berulang Import Brand, Import Measurement, Import Position, Import Division, Import User Login, Import User Non Login (lima entri per Action); Data `[i] records imported, 0 duplicates ignored, 0 errors remaining` (`1 record imported` bila i = 1); Modified By Yoga Permana (i ganjil) dan Dimas Anggoro (i genap). Nilai berbeda pada kolom yang diurutkan: enam Action, 30 Date berbeda, 30 string Data berbeda, dan dua Modified By. Spec hanya membaca.
- General Settings Client E: Date Format `dd MMM yy`, Time Format 24 jam (`HH:mm`), Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` (Pre-setup, tidak diubah).
- Cleanup (hook `after`): entri seed D-60 dibersihkan; urutan sort modal tidak disimpan di server.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Urutan awal dan kolom Action (TC-GS-IMPORT-497)

1. Seed Changelog Import Client E 30 entri (D-60) lewat skrip seed, lalu muat ulang halaman Import > Brand
2. Klik `[Changelog]`
3. Verifikasi urutan awal: baris pertama Date `30 Sep 26`
4. Klik header Action sekali
5. Verifikasi indikator panah naik pada header Action
6. Verifikasi 5 baris pertama Action `Import Brand`
7. Verifikasi 5 baris berikutnya Action `Import Division`
8. Klik header Action sekali lagi
9. Verifikasi indikator panah turun pada header Action
10. Verifikasi 5 baris pertama Action `Import User Non Login`
11. Verifikasi 5 baris berikutnya Action `Import User Login`
12. Klik header Action sekali lagi
13. Verifikasi indikator sort hilang
14. Verifikasi urutan kembali default Date descending dengan baris pertama Date `30 Sep 26`

### Kolom Date (TC-GS-IMPORT-788)

15. Klik header Date sekali
16. Verifikasi indikator panah naik (Oldest First)
17. Verifikasi baris pertama Date `01 Sep 26`
18. Klik header Date sekali lagi
19. Verifikasi indikator panah turun (Newest First)
20. Verifikasi baris pertama Date `30 Sep 26`
21. Klik header Date sekali lagi
22. Verifikasi indikator sort hilang
23. Verifikasi urutan kembali default Date descending dengan baris pertama Date `30 Sep 26`

### Kolom Data (TC-GS-IMPORT-789)

24. Klik header Data sekali
25. Verifikasi baris pertama Data `1 record imported, 0 duplicates ignored, 0 errors remaining` (A-Z)
26. Klik header Data sekali lagi
27. Verifikasi baris pertama Data `9 records imported, 0 duplicates ignored, 0 errors remaining` (Z-A)
28. Klik header Data sekali lagi
29. Verifikasi indikator sort hilang
30. Verifikasi urutan kembali default Date descending dengan baris pertama Date `30 Sep 26`

### Kolom Modified By (TC-GS-IMPORT-790)

31. Klik header Modified By sekali
32. Verifikasi seluruh 10 baris halaman 1 bermodified `Dimas A` (A-Z menurut nama lengkap)
33. Klik header Modified By sekali lagi
34. Verifikasi seluruh 10 baris halaman 1 bermodified `Yoga P` (Z-A)
35. Klik header Modified By sekali lagi
36. Verifikasi indikator sort hilang
37. Verifikasi urutan kembali default Date descending dengan baris pertama Date `30 Sep 26`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 37 langkah, di atas 35 langkah (sekitar batas 35), satu surface dan satu dataset seed; tiap kolom diakhiri tahap ketiga yang mengembalikan urutan default sehingga blok berikutnya mulai dari state yang sama.
- Langkah 1 adalah langkah penghubung pembuka (seed D-60 lalu muat ulang halaman; S-03, K-7), tanpa `Verifikasi`.
- Tahap ketiga tiap kolom (langkah 12, 21, 28, 35) sekaligus berfungsi sebagai pemulihan sort antar blok.
- Temuan untuk QA:
  - TC-GS-IMPORT-497 Expected b dan c tidak menyebut urutan di dalam kelompok Action yang sama; spec hanya mengasersi lima baris pertama dan lima berikutnya per Action sesuai TC.
  - TC-GS-IMPORT-789 mengasersi urutan string "1 record imported ..." sebelum "9 records imported ..." (urutan leksikografis); spec mengikuti TC.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.

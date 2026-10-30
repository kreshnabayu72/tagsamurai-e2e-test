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
- Data Dinamis D-60: Changelog Import Client E berisi tepat 30 entri seed, disiapkan lewat skrip seed di hook `before` (skrip juga membersihkan entri hasil commit spec lain; mekanisme disediakan tim FE/BE). Entri ke-i (i = 1 sampai 30) bertanggal i Sep 2026 pukul 10:00 UTC+7; Action berulang Import Brand, Import Measurement, Import Position, Import Division, Import User Login, Import User Non Login (lima entri per Action); Data `[i] records imported, 0 duplicates ignored, 0 errors remaining` (`1 record imported` bila i = 1); Modified By Yoga Permana (i ganjil) dan Dimas Anggoro (i genap). Nilai berbeda pada kolom yang diurutkan: enam Action, 30 Date berbeda, 30 string Data berbeda, dan dua Modified By. Spec hanya membaca.
- General Settings Client E: Date Format `dd MMM yy`, Time Format 24 jam (`HH:mm`), Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` (Pre-setup, tidak diubah).
- Cleanup (hook `after`): entri seed D-60 dibersihkan; urutan sort modal tidak disimpan di server.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Urutan awal dan kolom Action (TC-GS-IMPORT-497)

1. Klik `[Changelog]`
2. Verifikasi urutan awal: baris pertama Date `30 Sep 26`
3. Klik header Action sekali
4. Verifikasi indikator panah naik pada header Action
5. Verifikasi 5 baris pertama Action `Import Brand`
6. Verifikasi 5 baris berikutnya Action `Import Division`
7. Klik header Action sekali lagi
8. Verifikasi indikator panah turun pada header Action
9. Verifikasi 5 baris pertama Action `Import User Non Login`
10. Verifikasi 5 baris berikutnya Action `Import User Login`
11. Klik header Action sekali lagi
12. Verifikasi indikator sort hilang
13. Verifikasi urutan kembali default Date descending dengan baris pertama Date `30 Sep 26`

### Kolom Date (TC-GS-IMPORT-788)

14. Klik header Date sekali
15. Verifikasi indikator panah naik (Oldest First)
16. Verifikasi baris pertama Date `01 Sep 26`
17. Klik header Date sekali lagi
18. Verifikasi indikator panah turun (Newest First)
19. Verifikasi baris pertama Date `30 Sep 26`
20. Klik header Date sekali lagi
21. Verifikasi indikator sort hilang
22. Verifikasi urutan kembali default Date descending dengan baris pertama Date `30 Sep 26`

### Kolom Data (TC-GS-IMPORT-789)

23. Klik header Data sekali
24. Verifikasi baris pertama Data `1 record imported, 0 duplicates ignored, 0 errors remaining` (A-Z)
25. Klik header Data sekali lagi
26. Verifikasi baris pertama Data `9 records imported, 0 duplicates ignored, 0 errors remaining` (Z-A)
27. Klik header Data sekali lagi
28. Verifikasi indikator sort hilang
29. Verifikasi urutan kembali default Date descending dengan baris pertama Date `30 Sep 26`

### Kolom Modified By (TC-GS-IMPORT-790)

30. Klik header Modified By sekali
31. Verifikasi seluruh 10 baris halaman 1 bermodified `Dimas A` (A-Z menurut nama lengkap)
32. Klik header Modified By sekali lagi
33. Verifikasi seluruh 10 baris halaman 1 bermodified `Yoga P` (Z-A)
34. Klik header Modified By sekali lagi
35. Verifikasi indikator sort hilang
36. Verifikasi urutan kembali default Date descending dengan baris pertama Date `30 Sep 26`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 36 langkah, di atas 35 langkah (sekitar batas 35), satu surface dan satu dataset seed; tiap kolom diakhiri tahap ketiga yang mengembalikan urutan default sehingga blok berikutnya mulai dari state yang sama.
- Tahap ketiga tiap kolom (langkah 11, 20, 27, 34) sekaligus berfungsi sebagai pemulihan sort antar blok.
- Temuan untuk QA:
  - TC-GS-IMPORT-497 Expected b dan c tidak menyebut urutan di dalam kelompok Action yang sama; spec hanya mengasersi lima baris pertama dan lima berikutnya per Action sesuai TC.
  - TC-GS-IMPORT-789 mengasersi urutan string "1 record imported ..." sebelum "9 records imported ..." (urutan leksikografis); spec mengikuti TC.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.

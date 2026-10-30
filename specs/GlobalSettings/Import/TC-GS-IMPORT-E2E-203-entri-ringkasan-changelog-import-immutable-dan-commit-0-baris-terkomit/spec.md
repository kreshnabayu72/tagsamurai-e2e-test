---
id: TC-GS-IMPORT-E2E-203-entri-ringkasan-changelog-import-immutable-dan-commit-0-baris-terkomit
title: "Entri ringkasan Changelog Import immutable, dan commit 0 baris terkomit tetap menulis satu entri"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-427
  - TC-GS-IMPORT-756
coverage:
  web: automated
---

# Entri ringkasan Changelog Import immutable, dan commit 0 baris terkomit tetap menulis satu entri

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec melakukan commit sungguhan di Client E (pembuat data, destruktif) dan menunggu worker commit nyata (batas tunggu 2 menit per commit) (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC_PASSWORD`.
- Pelaku kedua (pemicu via sesi API, bukan sesi UI): Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC2_PASSWORD` (nama env baru). Sesi API membuat Brand `Nikon` dan `Pentax` di Master Reference > Brand untuk TC-GS-IMPORT-756; klien HTTP dan kontrak endpoint pembuatan Brand disediakan tim FE/BE (tidak tertulis di TC).
- Layar awal: hook `beforeEach` membuka Import > Brand Client E.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis (draft Brand Client E, disiapkan lewat skrip seed; Client E direset tanpa draft sebelum tiap TC, Kontrak Fixture R1):
  - TC-GS-IMPORT-427: D-58 (`brand-partial-15.csv`): 15 baris, 10 `pending`, 3 `duplicate` (2 duplikat antar-baris `Brand Kembar` dan `Samsung`), 2 `error` (Brand Name 121 karakter). Nilai pengganti baris error: `Kamera Baru` dan `Printer Baru`.
  - TC-GS-IMPORT-756: draft Brand 2 baris `pending` dari `brand-cap-2.csv` (kolom Brand Name): #1 `Nikon`, #2 `Pentax`, tanpa baris `error` dan `duplicate`. Nama literal dipakai karena late-binding mensyaratkan Brand dengan nama sama dibuat Admin kedua; hook `before` menghapus Brand `Nikon` dan `Pentax` sisa run sebelumnya.
- Log (baseline S-12): total entri pada Pagination Changelog Import (Filter Action = `Import Brand`) dicatat sebelum commit pertama tiap TC; asersi "bertambah tepat satu" atau "dua" membandingkan dengan baseline itu (0 bila empty state). Total tidak diasersi sebagai angka absolut.
- Akun tampil: Modified By `Yoga P` (Total Control Client E: Yoga Permana), format `[First Name] [Last Initial]`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh, D-47): hapus Brand hasil commit (`Kamera Baru`, `Printer Baru`, dan 10 Brand `pending` D-58) serta Brand `Nikon` dan `Pentax` di Client E; hapus draft; reset hasil commit terakhir dan penanda Banner Hasil Commit.
- Kemampuan teknis: skrip seed draft; skrip reset Client E (D-47); sesi API Admin kedua; worker commit berjalan normal.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Entri ringkasan immutable (TC-GS-IMPORT-427)

1. Buka Changelog Import, terapkan Filter Action = `Import Brand`, lalu catat total entri pada Pagination sebagai baseline (0 bila empty state)
2. Tutup modal Changelog Import
3. Klik `[Import (10)]`
4. Muat ulang halaman Import > Brand setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
5. Buka Changelog Import, terapkan Filter Action = `Import Brand`, lalu baca total entri pada Pagination
6. Verifikasi total bertambah tepat satu dibanding baseline langkah 1
7. Verifikasi baris pertama tabel (sort default Date descending): Data `10 records imported, 3 duplicates ignored, 2 errors remaining`
8. Tutup modal Changelog Import
9. Buka row action Edit pada baris `error` pertama dari atas
10. Ubah Brand Name menjadi `Kamera Baru`
11. Klik `[Save]`
12. Buka row action Edit pada baris `error` yang tersisa
13. Ubah Brand Name menjadi `Printer Baru`
14. Klik `[Save]`
15. Klik `[Import (2)]`
16. Muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
17. Buka Changelog Import, terapkan Filter Action = `Import Brand`, lalu baca total entri pada Pagination
18. Verifikasi total bertambah tepat dua dibanding baseline langkah 1
19. Verifikasi baris pertama tabel: Data `2 records imported, 0 duplicates ignored, 0 errors remaining`
20. Verifikasi baris kedua tabel: Data `10 records imported, 3 duplicates ignored, 2 errors remaining`, sama dengan langkah 7, tanpa perubahan
21. Tutup modal Changelog Import

### Commit 0 baris terkomit (TC-GS-IMPORT-756)

22. Seed draft Brand 2 baris (`Nikon`, `Pentax`) di Client E lewat skrip seed, lalu muat ulang halaman Import > Brand
23. Buka Changelog Import, terapkan Filter Action = `Import Brand`, lalu catat total entri pada Pagination sebagai baseline (0 bila empty state)
24. Tutup modal Changelog Import
25. Admin kedua Client E (sesi API) membuat Brand `Nikon` dan `Pentax` di Master Reference > Brand hingga tersimpan, tanpa membuka Staging Table
26. Klik `[Import (2)]` di halaman Import > Brand
27. Muat ulang halaman Import > Brand setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
28. Buka Changelog Import, terapkan Filter Action = `Import Brand`, lalu baca total entri pada Pagination
29. Verifikasi total bertambah tepat satu dibanding baseline langkah 23
30. Verifikasi baris pertama tabel (sort default Date descending): Action `Import Brand`, Data `0 records imported, 0 duplicates ignored, 2 errors remaining`, Modified By `Yoga P`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- P-2: Admin kedua Client E hanya memicu kegagalan late-binding lewat sesi API (membuat Brand dengan nama sama) dan tidak menjadi objek asersi; spec tetap fungsional (bukan kelas c).
- Langkah 5 dan 17 membaca Changelog segera setelah commit; langkah 7 dan 20 membuktikan entri langkah 7 tidak berubah (immutable) dengan membandingkan Data yang sama setelah commit kedua.
- Langkah 22 adalah langkah penghubung yang menyiapkan draft kedua (S-03).
- Temuan untuk QA:
  - TC-GS-IMPORT-756 Precondition tidak merujuk Data Dinamis (D-ref `-`) untuk draft Brand 2 baris; spec membuat draft dari `brand-cap-2.csv` lewat skrip seed.
  - TC-GS-IMPORT-756 langkah 5 ("lewat fixture") tidak menyebut mekanisme; spec memakai sesi API Admin kedua (kemampuan disediakan tim FE/BE).
  - TC-GS-IMPORT-427 dan 756 Post Condition (draft dihapus; dua entri ringkasan; Brand `Nikon` dan `Pentax` tersimpan satu kali) tidak punya langkah observasi di TC selain Expected; tidak diasersi terpisah (S-01).
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.

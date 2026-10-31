---
id: TC-GS-IMPORT-E2E-091-edit-mode-error-callout-dan-chip-disabled-upload-file-dan-discard
title: "Edit Mode: Error Callout dan chip Disabled, Upload File dan Discard Disabled dengan Download Template dan Changelog aktif, navigasi keyboard grid"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-201
  - TC-GS-IMPORT-202
  - TC-GS-IMPORT-235
coverage:
  web: automated
---

# Edit Mode: Error Callout dan chip Disabled, Upload File dan Discard Disabled dengan Download Template dan Changelog aktif, navigasi keyboard grid

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Dinamis (nama literal karena asersi bergantung pada isi dan jumlah baris; pengecualian S-12):
  - D-01: Draft Brand 12 baris `pending` dari `brand-12.csv` (#1 `Acme Corp`, ..., #12 `Asus`), dipulihkan oleh skrip pemulihan (Kontrak Fixture R2) sebelum TC-235 dan TC-202.
  - D-09: Draft Brand 13 baris Client A: D-01 ditambah baris #13 berstatus `error` dengan Brand Name 121 karakter (nilai sumber Brand pertama tabel D-41), dipulihkan sebelum TC-201.
  - D-76 varian 1 (hook umur draft, jam server dan `created_at` job): untuk TC-202 `created_at` job draft dimundurkan 25 jam sehingga Unsaved Banner tampil. Umur draft hanya dipakai sebagai pemicu banner (bukan batas waktu yang diuji).
- Kemampuan teknis: hover untuk tooltip, pengamatan unduhan berkas (tanpa memeriksa isi), tombol keyboard Tab, Shift+Tab, panah atas dan bawah, hook umur draft D-76 (jam server atau `created_at`) serta skrip pemulihan draft (disediakan tim FE/BE).
- State global: jam server atau `created_at` draft dimajukan pada langkah 11 (D-76 varian 1); hook `after` memulihkan draft Client A ke D-01 dan jam server ke nilai awal. Jam browser tidak diubah.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan draft Brand Client A ke D-01, pulihkan jam server, dan lepas kunci sesi edit.

## Test Steps

### TC-GS-IMPORT-235: Navigasi keyboard pada grid Edit this page

1. Aktifkan Switch `Edit this page`
2. Klik input Brand Name baris #1 untuk menempatkan fokus
3. Tekan Tab
4. Verifikasi fokus tidak lagi berada pada sel Brand Name baris #1
5. Tekan Shift+Tab
6. Verifikasi fokus kembali ke sel Brand Name baris #1
7. Tekan panah bawah
8. Verifikasi fokus tidak lagi berada pada sel Brand Name baris #1
9. Tekan panah atas
10. Verifikasi fokus kembali ke sel Brand Name baris #1
11. Verifikasi seluruh baris halaman 1 tetap input aktif dengan nilai semula
12. Verifikasi footer tetap menampilkan `[Cancel]` dan `[Save]`
13. Klik `[Cancel]`

### TC-GS-IMPORT-202: Upload File dan Discard Disabled; Download Template dan Changelog tetap aktif

14. Mundurkan `created_at` draft Brand 25 jam (hook umur draft D-76 varian 1), lalu muat ulang halaman
15. Klik `⋯` pada baris #1, pilih `Edit`
16. Arahkan kursor ke `[Upload File]` di toolbar
17. Verifikasi `[Upload File]` tampil Disabled
18. Verifikasi tooltip pada `[Upload File]`: "Finish or cancel the current edit first."
19. Arahkan kursor ke `[Discard]` pada Unsaved Banner
20. Verifikasi `[Discard]` tampil Disabled
21. Verifikasi tooltip pada `[Discard]`: "Finish or cancel the current edit first."
22. Klik `[Download Template]`
23. Verifikasi berkas template Brand terunduh
24. Klik `[Changelog]` di header halaman
25. Verifikasi modal Changelog Import terbuka
26. Tutup modal Changelog Import
27. Verifikasi footer tetap menampilkan `[Cancel]` dan `[Save]` (sesi edit tidak berakhir)
28. Klik `[Cancel]`

### TC-GS-IMPORT-201: Tombol Error Summary Callout dan chip filter Disabled

29. Pulihkan draft Client A ke D-09 lewat skrip pemulihan, lalu muat ulang halaman
30. Klik `[View Data]` pada baris pesan "Brand Name: Max. 120 characters" di Error Summary Callout
31. Verifikasi chip "Showing rows with: Brand Name: Max. 120 characters" dengan `[×]` tampil
32. Verifikasi kartu Errors tampil Active
33. Klik `⋯` pada baris #13, pilih `Edit`
34. Arahkan kursor ke `[View Data]` pada Error Summary Callout
35. Verifikasi `[View Data]` tampil Disabled
36. Verifikasi tooltip pada `[View Data]`: "Finish or cancel the current edit first."
37. Arahkan kursor ke `[Delete All Rows]` pada Error Summary Callout
38. Verifikasi `[Delete All Rows]` tampil Disabled
39. Verifikasi tooltip pada `[Delete All Rows]`: "Finish or cancel the current edit first."
40. Arahkan kursor ke chip filter `[×]`
41. Verifikasi chip `[×]` tampil Disabled
42. Verifikasi tooltip pada chip `[×]`: "Finish or cancel the current edit first."

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional (hook umur draft D-76 hanya pemicu banner, bukan objek uji).
- Spec berisi 42 langkah, di atas 35 langkah. Alasan: tiga TC (235, 202, 201) satu surface (mode Edit this page) dan satu kelas fungsional; tiap blok berdiri sendiri dengan pemulihan draft antar blok.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-235 dijalankan pertama, lalu TC-202, lalu TC-201 (TC-201 memakai D-09 yang berbeda dari D-01 sehingga dijalankan terakhir setelah pemulihan draft; prinsip 3 bagian 3).
- Langkah penghubung (tanpa `Verifikasi`): `[Cancel]` pada langkah 13 dan 28 menutup sesi tanpa perubahan; langkah 14 dan 29 menyiapkan Precondition TC; langkah 26 menutup modal Changelog. Langkah 14 menggeser jam server atau `created_at` draft sebagai pemicu banner dan tidak mengubah state yang diasersi di Activity Log.
- Sesi edit TC-201 (langkah 33) tidak ditutup oleh spec; hook `afterEach` dan `after` memulihkan draft dan melepas kunci.
- Pembagian TC lintas spec: TC-GS-IMPORT-190, 192, 193, 196 sampai 200, 203, dan 664 ada di spec 090.
- Temuan untuk QA:
  - TC-GS-IMPORT-202 Dependensi D-76 varian 1 menyebut kolom Precondition d "hook umur draft"; mekanismenya (fixture timestamp atau jam server) disediakan tim FE/BE (S-13), dan jam browser tidak digeser karena Unsaved Banner dievaluasi di server saat pembacaan.
  - TC-GS-IMPORT-202 Expected b mengasersi unduhan "berkas template Brand" tanpa nama berkas; spec hanya memeriksa unduhan terjadi (isi berkas kelas f tidak diasersi).
  - TC-GS-IMPORT-235 Expected a, c memuat asersi "fokus tidak lagi berada pada sel" tanpa menyebut ke elemen mana fokus pindah; spec mengikuti TC dan tidak mengasersi tujuan fokus.
  - Post Condition semua TC di spec ini kosong atau tidak ada observasi; tidak diasersi (S-01).

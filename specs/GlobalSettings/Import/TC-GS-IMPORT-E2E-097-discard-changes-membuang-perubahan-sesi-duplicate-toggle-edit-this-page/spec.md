---
id: TC-GS-IMPORT-E2E-097-discard-changes-membuang-perubahan-sesi-duplicate-toggle-edit-this-page
title: "Discard Changes: membuang perubahan, sesi Duplicate, toggle Edit this page OFF dan ON dengan perubahan, klik sel baris lain"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-204
  - TC-GS-IMPORT-228
  - TC-GS-IMPORT-229
  - TC-GS-IMPORT-230
  - TC-GS-IMPORT-231
coverage:
  web: automated
---

# Discard Changes: membuang perubahan, sesi Duplicate, toggle Edit this page OFF dan ON dengan perubahan, klik sel baris lain

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Dinamis: D-01 (Draft Brand 12 baris `pending`: #1 `Acme Corp`, #2 `Lenovo`, ..., #4 `Honeywell`, ..., #12 `Asus`; nama literal karena asersi bergantung pada isi, pengecualian S-12), dipulihkan oleh hook `beforeEach` sesuai Kontrak Fixture R2. Nilai ubahan: `Acme Corporation`, `Lenovo Group`.
- Kemampuan teknis: pengamatan dialog, skrip pemulihan draft D-01 (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain draft Client A dan flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan draft Client A ke D-01 dan lepas kunci sesi edit.

## Test Steps

### TC-GS-IMPORT-228: Discard membuang perubahan dan menutup sesi

1. Klik `⋯` pada baris #1, pilih `Edit`
2. Ubah Brand Name baris #1 menjadi `Acme Corporation`
3. Klik `[Cancel]`
4. Klik `[Discard]` pada dialog Discard Changes
5. Verifikasi dialog tertutup
6. Verifikasi baris #1 menampilkan `Acme Corp` sebagai teks
7. Verifikasi footer `[Import (12)]` tampil kembali

### TC-GS-IMPORT-229: Discard pada sesi Duplicate

8. Klik `⋯` pada baris #2, pilih `Duplicate`
9. Ubah Brand Name salinan menjadi `Lenovo Group`
10. Klik `[Cancel]`
11. Klik `[Discard]` pada dialog Discard Changes
12. Verifikasi baris salinan `Lenovo Group` tidak tampil
13. Verifikasi draft tetap 12 baris: footer `[Import (12)]`

### TC-GS-IMPORT-230: Toggle Edit this page OFF dengan perubahan

14. Aktifkan Switch `Edit this page`
15. Ubah Brand Name baris #1 menjadi `Acme Corporation`
16. Matikan Switch `Edit this page`
17. Verifikasi dialog dengan Title "Discard Changes" dan Body "Unsaved edits will be lost." tampil dengan tombol `[Keep Editing]` dan `[Discard]`
18. Klik `[Discard]`
19. Verifikasi baris #1 menampilkan `Acme Corp` sebagai teks
20. Verifikasi footer `[Import (12)]` tampil kembali

### TC-GS-IMPORT-231: Toggle Edit this page ON dari sesi Edit Baris dengan perubahan

21. Klik `⋯` pada baris #1, pilih `Edit`
22. Ubah Brand Name baris #1 menjadi `Acme Corporation`
23. Aktifkan Switch `Edit this page`
24. Verifikasi dialog dengan Title "Discard Changes" dan Body "Unsaved edits will be lost." tampil dengan tombol `[Keep Editing]` dan `[Discard]`
25. Klik `[Discard]`
26. Verifikasi perubahan lama dibuang (baris #1 menampilkan input `Acme Corp`)
27. Verifikasi seluruh 10 baris halaman 1 menjadi input aktif
28. Klik `[Cancel]`

### TC-GS-IMPORT-204: Klik sel baris lain dengan perubahan

29. Klik `⋯` pada baris #1, pilih `Edit`
30. Ubah Brand Name baris #1 menjadi `Acme Corporation`
31. Klik sel Brand Name baris #4
32. Verifikasi tidak ada dialog yang tampil
33. Verifikasi footer tetap `[Cancel]` dan `[Save]`
34. Verifikasi baris #1 tetap input dengan nilai `Acme Corporation`
35. Verifikasi baris #4 tetap tampil sebagai teks
36. Klik `[Cancel]` pada footer
37. Verifikasi dialog dengan Title "Discard Changes" dan Body "Unsaved edits will be lost." tampil dengan tombol `[Keep Editing]` dan `[Discard]`
38. Klik `[Discard]` pada dialog
39. Verifikasi dialog tertutup
40. Verifikasi baris #1 kembali menampilkan `Acme Corp`
41. Verifikasi footer `[Import (12)]` tampil kembali
42. Verifikasi baris #4 tampil sebagai teks

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Spec berisi 42 langkah, di atas 35 langkah. Alasan: satu surface (sesi Duplicate dan Edit this page) dan satu kelas fungsional; tiap blok berakhir pada tampilan normal sehingga blok berdiri sendiri.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-204 dijalankan paling akhir karena rantai Expected-nya terpanjang; tidak ada TC yang menghapus data. Tiap blok berakhir pada tampilan normal (Discard atau Cancel tanpa perubahan), sehingga tidak ada pemulihan draft antar-blok.
- Langkah penghubung (tanpa `Verifikasi`): langkah 28 menutup sesi Edit this page tanpa perubahan (tanpa dialog).
- Pembagian TC lintas spec: TC-GS-IMPORT-224 sampai 227, 232, dan 656 sampai 658 (Cancel) ada di spec 096.
- Temuan untuk QA:
  - TC-GS-IMPORT-204 Expected c menyebut "baris #4 tampil sebagai teks" setelah Discard tanpa kolom perubahan; spec mengikuti TC.
  - Post Condition semua TC di spec ini kosong atau tidak punya langkah observasi; tidak diasersi (S-01).

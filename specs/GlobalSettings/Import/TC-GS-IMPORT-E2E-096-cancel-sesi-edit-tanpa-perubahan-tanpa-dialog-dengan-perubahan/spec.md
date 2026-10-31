---
id: TC-GS-IMPORT-E2E-096-cancel-sesi-edit-tanpa-perubahan-tanpa-dialog-dengan-perubahan
title: "Cancel sesi edit: tanpa perubahan tanpa dialog, dengan perubahan memunculkan dialog Discard Changes, Keep Editing mempertahankan sesi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-224
  - TC-GS-IMPORT-225
  - TC-GS-IMPORT-226
  - TC-GS-IMPORT-227
  - TC-GS-IMPORT-232
  - TC-GS-IMPORT-656
  - TC-GS-IMPORT-657
  - TC-GS-IMPORT-658
coverage:
  web: automated
---

# Cancel sesi edit: tanpa perubahan tanpa dialog, dengan perubahan memunculkan dialog Discard Changes, Keep Editing mempertahankan sesi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Dinamis: D-01 (Draft Brand 12 baris `pending`: #1 `Acme Corp`, #2 `Lenovo`, #3 `Zebra Technologies`, #4 `Honeywell`, ..., #12 `Asus`; nama literal karena asersi bergantung pada isi, pengecualian S-12), dipulihkan oleh hook `beforeEach` sesuai Kontrak Fixture R2. Nilai ubahan: `Acme Corporation`, `Lenovo Group`.
- Kemampuan teknis: pengamatan dialog, skrip pemulihan draft D-01 (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain draft Client A dan flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan draft Client A ke D-01 dan lepas kunci sesi edit.

## Test Steps

### TC-GS-IMPORT-224: Cancel tanpa perubahan

1. Klik `⋯` pada baris #1, pilih `Edit`
2. Klik `[Cancel]` tanpa mengubah nilai
3. Verifikasi tidak ada dialog yang tampil
4. Verifikasi footer `[Import (12)]` tampil kembali
5. Verifikasi baris #1 tampil sebagai teks `Acme Corp`

### TC-GS-IMPORT-656: Switch Edit this page dimatikan tanpa perubahan

6. Aktifkan Switch `Edit this page`
7. Matikan Switch `Edit this page` tanpa mengubah nilai
8. Verifikasi tidak ada dialog yang tampil
9. Verifikasi baris #1 sampai #10 tampil kembali sebagai teks
10. Verifikasi footer `[Import (12)]` tampil kembali

### TC-GS-IMPORT-232: Toggle Edit this page dari sesi Edit Baris tanpa perubahan

11. Klik `⋯` pada baris #1, pilih `Edit`
12. Aktifkan Switch `Edit this page`
13. Verifikasi tidak ada dialog yang tampil
14. Verifikasi seluruh 10 baris halaman 1 menjadi input aktif
15. Verifikasi footer tetap `[Cancel]` dan `[Save]`
16. Klik `[Cancel]`

### TC-GS-IMPORT-225, 658, 227: Cancel dengan perubahan pada sesi Edit Baris, lalu Keep Editing

17. Klik `⋯` pada baris #1, pilih `Edit`
18. Ubah Brand Name baris #1 menjadi `Acme Corporation`
19. Klik `[Cancel]` pada footer
20. Verifikasi dialog dengan Title "Discard Changes" dan Body "Unsaved edits will be lost." tampil dengan tombol `[Keep Editing]` dan `[Discard]`
21. Klik `[Keep Editing]`
22. Verifikasi dialog tertutup
23. Verifikasi baris #1 tetap input dengan nilai `Acme Corporation`
24. Verifikasi baris #4 tetap tampil sebagai teks
25. Verifikasi footer tetap `[Cancel]` dan `[Save]`
26. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog Discard Changes

### TC-GS-IMPORT-226, 657: Cancel dengan perubahan pada sesi Duplicate, lalu Keep Editing

27. Klik `⋯` pada baris #2, pilih `Duplicate`
28. Ubah Brand Name salinan menjadi `Lenovo Group`
29. Klik `[Cancel]`
30. Verifikasi dialog dengan Title "Discard Changes" dan Body "Your changes will not be saved." tampil dengan tombol `[Keep Editing]` dan `[Discard]`
31. Klik `[Keep Editing]`
32. Verifikasi dialog tertutup
33. Verifikasi baris salinan #3 tetap input dengan nilai `Lenovo Group`
34. Verifikasi footer tetap `[Cancel]` dan `[Save]`
35. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog Discard Changes

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penggabungan: TC-225, TC-227, dan TC-658 berbagi satu sesi Edit Baris (Cancel dengan perubahan, dialog, Keep Editing) serta TC-226 dan TC-657 berbagi satu sesi Duplicate; Expected tiap TC tetap punya `Verifikasi` sendiri (langkah 20, 22 sampai 25, 30, 32 sampai 34). Verifikasi baris #4 teks (langkah 24) berasal dari TC-658.
- Langkah penghubung (tanpa `Verifikasi`): langkah 16 menutup sesi tanpa perubahan; langkah 26 dan 35 (`[Cancel]` lalu `[Discard]`) membuang perubahan agar tampilan kembali normal (Discard diuji di spec 097).
- Pembagian TC lintas spec: TC-GS-IMPORT-204 dan 228 sampai 231 (Discard Changes) ada di spec 097.
- Temuan untuk QA:
  - Post Condition semua TC di spec ini kosong atau tidak punya langkah observasi; tidak diasersi (S-01).
  - TC-GS-IMPORT-227 dan 658 hampir sama (Keep Editing pada sesi Edit Baris); 658 menambah asersi baris #4 teks. Bukan duplikat penuh tetapi tumpang tindih.
